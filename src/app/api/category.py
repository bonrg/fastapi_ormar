from fastapi import (
    APIRouter,
    Depends,
    status as st,
)
from .. import models
from ..services.category import CategoryService


router = APIRouter(
    prefix='/categories',
    tags=['Category'],
)


@router.post("/", response_model=models.Category, status_code=st.HTTP_201_CREATED)
async def create(category: models.Category, service: CategoryService = Depends()):
    return await service.create(category=category)


@router.get("/", response_model=list[models.Category])
async def get_categories(service: CategoryService = Depends()):
    return await service.get_categories()


@router.get("/{category_id}", response_model=models.Category)
async def get(category_id: int, service: CategoryService = Depends()):
    return await service.get(category_id=category_id)


@router.put("/{category_id}", response_model=models.Category)
async def update(category_id: int, category: models.Category, service: CategoryService = Depends()):
    return await service.update(category_id=category_id, category=category)


@router.delete("/{category_id}")
async def delete(category_id: int, category: models.Category, service: CategoryService = Depends()):
    return await service.delete(category_id=category_id, category=category)
