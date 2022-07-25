from fastapi import (
    APIRouter,
    Depends,
    status as st,
    Query
)
from .. import models
from ..services.category import CategoryService


router = APIRouter(
    prefix='/categories',
    tags=['Category'],
)


@router.post("/", response_model=models.Category, status_code=st.HTTP_201_CREATED)
async def create_hero(category: models.Category, service: CategoryService = Depends()):
    return await service.create(category=category)


# @router.get("/", response_model=list[models.HeroRead])
# async def get_heroes(
#         offset: int = 0,
#         limit: int = Query(default=100, lte=100),
#         service: HeroService = Depends()):
#     return await service.get_heroes(offset=offset, limit=limit)
#
#
@router.get("/{category_id}", response_model=models.Category)
async def get(category_id: int, service: CategoryService = Depends()):
    return await service.get(category_id=category_id)
#
#
# @router.patch("/{hero_id}", response_model=models.HeroRead)
# async def update(hero_id: int, hero: models.HeroUpdate, service: HeroService = Depends()):
#     return await service.update(hero_id=hero_id, hero=hero)
#
#
# @router.delete("/{hero_id}")
# async def delete(hero_id: int, service: HeroService = Depends()):
#     return await service.delete(hero_id=hero_id)
