import datetime
import peewee


class Data(peewee.Model):
    """
    Basic model for database table, you can edit it and create new models and manager
    """
    name = peewee.CharField(max_length=40)
    description = peewee.CharField(max_length=280, null=True)
    created_at = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        """
        Set database via model manager that will be manage all operation in database
        and out model is just most simple entity
        """
        database = None
