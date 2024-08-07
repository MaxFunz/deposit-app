from fastapi import FastAPI
from .db.database import create_tables
from .api.routes import router

app = FastAPI()

async def lifespan(app: FastAPI):
    create_tables()
    yield
app = FastAPI(lifespan=lifespan)
app.include_router(router)