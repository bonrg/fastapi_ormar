from .. import models


class CategoryService:

    async def create(self, category: models.Category) -> models.Category:
        await category.save()
        return category

    async def get_categories(self) -> list[models.Category]:
        categories = await models.Category.objects.select_related('items').all()
        return categories

    async def get(self, category_id: int) -> models.Category:
        category = await models.Category.objects.get(pk=category_id)
        return category

    async def update(self, category_id: int, category: models.Category) -> models.Category:
        category_db = await models.Category.objects.get(pk=category_id)
        return await category_db.update(**category.dict())

    async def delete(self, category_id: int, category: models.Category) -> dict:
        if category:
            return {"deleted_rows": await category.delete()}
        category_db = await models.Category.objects.get(pk=category_id)
        return {"deleted_rows": await category_db.delete()}
