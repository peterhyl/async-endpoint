import json
import logging.config
from datetime import date, datetime

import peewee_async
from aiohttp import web
from playhouse.shortcuts import model_to_dict

import config
from managers.data import DataManager
from models.data import Data

# logging.config.dictConfig(config.debug_dict_config)
logging.config.dictConfig(config.info_dict_config)

logger = logging.getLogger('endpoint')

database = peewee_async.PostgresqlDatabase('test', user='postgres', password='root')
manager = DataManager(database)
routes = web.RouteTableDef()


def json_serial(obj):
    """
    JSON serializer for objects not serializable(datetime) by default json code
    """
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


@routes.view('/{name}')
class DataHandler(web.View):

    async def get(self):
        """
        Handler for get requests, async load from database.
        """
        result = []
        name = self.request.match_info.get('name', None)

        if not name:
            logger.error('Missing request attribute "name"')
            raise web.HTTPBadRequest()

        data = await manager.execute(Data.select().where(Data.name == name))
        for item in data:
            result.append(model_to_dict(item))

        logger.info(f'Result contain: {len(data)} Data items by name: {name}')
        # lambda used to serialization datetime
        return web.json_response(data=result, dumps=lambda x: json.dumps(x, default=json_serial))

    async def post(self):
        """
        Handler for post requests, async create new row into database.
        """
        data = await self.request.json()
        name = self.request.match_info.get('name', None)

        if not name:
            logger.error('Missing request attribute "name"')
            raise web.HTTPBadRequest()

        async with manager.atomic():
            new_data = await manager.create(name=name, description=data.get('description', None))

        logger.info(f'Successful create new object: {new_data}')
        return web.json_response(status=201, data=model_to_dict(new_data),
                                 dumps=lambda x: json.dumps(x, default=json_serial))


async def init_app(_):
    app = web.Application()
    app.add_routes(routes)
    logger.info('Startup async endpoint')
    return app
