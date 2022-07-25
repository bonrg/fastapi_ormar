from fastapi import APIRouter
from . import (
    category,
    item
)


router = APIRouter()
router.include_router(category.router)
router.include_router(item.router)
