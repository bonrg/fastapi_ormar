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
async def create(item: models.Item, service: ItemService = Depends()):
    return await service.create(item=item)


@router.get("/", response_model=list[models.Item])
async def get_items(service: ItemService = Depends()):
    return await service.get_items()


@router.get("/{item_id}", response_model=models.Item)
async def get(item_id: int, service: ItemService = Depends()):
    return await service.get(item_id=item_id)


@router.put("/{item_id}", response_model=models.Item)
async def update(item_id: int, item: models.Item, service: ItemService = Depends()):
    return await service.update(item_id=item_id, item=item)


@router.delete("/{item_id}")
async def delete(item_id: int, item: models.Item, service: ItemService = Depends()):
    return await service.delete(item_id=item_id, item=item)
