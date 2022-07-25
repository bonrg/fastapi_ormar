from fastapi import FastAPI
from . import api
from .database import engine, metadata, database

tags_metadata = [
    {
        'name': 'Category',
        'description': 'Category',
    },
    {
        'name': 'Item',
        'description': 'Item',
    },
]

app = FastAPI(
    title='Ormar+Fastapi',
    description='Ormar+Fastapi',
    version='1.0.0',
    openapi_tags=tags_metadata,
)


@app.on_event("startup")
async def on_startup():
    metadata.create_all(engine)
    app.state.database = database
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(api.router)
