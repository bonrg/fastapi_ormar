from .. import models


class ItemService:

    async def create(self, item: models.Item) -> models.Item:
        await item.save()
        return item

    async def get_items(self) -> list[models.Item]:
        items = await models.Item.objects.select_related("category").all()
        return items
    
    async def get(self, item_id: int) -> models.Item:
        item = await models.Item.objects.get(pk=item_id)
        return item

    async def update(self, item_id: int, item: models.Item) -> models.Item:
        item_db = await models.Item.objects.get(pk=item_id)
        return await item_db.update(**item.dict())

    async def delete(self, item_id: int, item: models.Item) -> dict:
        if item:
            return {"deleted_rows": await item.delete()}
        item_db = await models.Item.objects.get(pk=item_id)
        return {"deleted_rows": await item_db.delete()}
