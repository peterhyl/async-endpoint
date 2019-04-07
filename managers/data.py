import logging

from peewee_async import Manager

from models.data import Data


class DataManager(Manager):
    """
    Basic manager for model Data
    """
    model = Data

    def __init__(self, db):
        db.allow_sync = False
        super().__init__(db)
        self.logger = logging.getLogger(__name__)
        self.model._meta.database = db

    async def get_by_id(self, id):
        self.logger.debug('Get data by the ID: %d', id)
        return await super().get(self.model, id=id)

    async def create(self, **kwargs):
        self.logger.debug('Create new data with args: %s', kwargs)
        return await super().create(self.model, **kwargs)

    async def execute(self, query):
        self.logger.debug('Execute query: %s', query)
        return await super().execute(query)
