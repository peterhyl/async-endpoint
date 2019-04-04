import json
import peewee_async

from datetime import date, datetime
from aiohttp import web
from playhouse.shortcuts import model_to_dict

from managers.data import DataManager
from models.data import Data


database = peewee_async.PostgresqlDatabase('test')
manager = DataManager(database)
routes = web.RouteTableDef()


def json_serial(obj):
    """
    JSON serializer for objects not serializable(datetime) by default json code
    """
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


@routes.get('/{name}')
async def handle_get(request):
    """
    Handler for get requests, async load from database.
    """
    result = []
    name = request.match_info.get('name', None)

    if not name:
        raise web.HTTPNotFound()

    data = await manager.execute(Data.select().where(Data.name == name))
    for item in data:
        result.append(model_to_dict(item))

    # lambda used to serialization datetime
    return web.json_response(data=result, dumps=lambda x: json.dumps(x, default=json_serial))


@routes.post('/{name}')
async def handle_post(request):
    """
    Handler for post requests, async create new row into database.
    """
    data = await request.json()
    name = request.match_info.get('name', None)

    if not name:
        raise web.HTTPNotFound()

    new_data = await manager.create(name=name, description=data.get('description', None))

    return web.json_response(status=201, data=model_to_dict(new_data),
                             dumps=lambda x: json.dumps(x, default=json_serial))


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
