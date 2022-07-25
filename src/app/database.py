import databases
import ormar
import sqlalchemy

from app.settings import settings

metadata = sqlalchemy.MetaData()
database = databases.Database(settings.database_url)
engine = sqlalchemy.create_engine(settings.database_url)


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
