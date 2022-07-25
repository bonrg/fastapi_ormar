import ormar

from ..database import BaseMeta


class Category(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'categories'

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
