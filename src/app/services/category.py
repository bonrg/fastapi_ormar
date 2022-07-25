from .. import models


class CategoryService:

    async def create(self, category: models.Category) -> models.Category:
        await category.save()
        return category

    # async def get_heroes(self, offset: int = 0, limit: int = 100) -> list[models.Hero]:
    #     pass
    #
    async def get(self, category_id: int) -> models.Category:
        category = await models.Category.objects.get(pk=category_id)
        return category
    #
    # async def update(self, hero_id: int, hero: models.Hero) -> models.Hero:
    #     pass
    #
    # async def delete(self, hero_id: int) -> dict:
    #     pass
