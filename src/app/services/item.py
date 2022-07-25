from .. import models


class ItemService:

    async def create(self, item: models.Item) -> models.Item:
        await item.save()
        return item

    # async def get_teams(self, offset: int = 0, limit: int = 100) -> list[models.Team]:
    #     pass
    #
    # async def get(self, team_id: int) -> models.Team:
    #     pass
    #
    # async def update(self, team_id: int, team: models.Team) -> models.Team:
    #     pass
    #
    # async def delete(self, team_id: int) -> dict:
    #     pass
