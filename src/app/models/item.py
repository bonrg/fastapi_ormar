import ormar

from ..database import BaseMeta
from .category import Category


class Item(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'items'

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
    category: Category | None = ormar.ForeignKey(Category, nullable=True)
