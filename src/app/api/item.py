from fastapi import (
    APIRouter,
    Depends,
    status as st,
    Query
)
from .. import models
from ..services.item import ItemService

router = APIRouter(
    prefix='/items',
    tags=['Item'],
)


@router.post("/", response_model=models.Item, status_code=st.HTTP_201_CREATED)
async def create_team(item: models.Item, service: ItemService = Depends()):
    return await service.create(item=item)
#
#
# @router.get("/", response_model=list[models.TeamRead])
# async def get_teams(
#         offset: int = 0,
#         limit: int = Query(default=100, lte=100),
#         service: TeamService = Depends()):
#     return await service.get_teams(offset=offset, limit=limit)
#
#
# @router.get("/{team_id}", response_model=models.TeamReadWithHeroes)
# async def get(team_id: int, service: TeamService = Depends()):
#     return await service.get(team_id=team_id)
#
#
# @router.patch("/{team_id}", response_model=models.TeamRead)
# async def update(team_id: int, team: models.TeamUpdate, service: TeamService = Depends()):
#     return await service.update(team_id=team_id, team=team)
#
#
# @router.delete("/{team_id}")
# async def delete(team_id: int, service: TeamService = Depends()):
#     return await service.delete(team_id=team_id)
