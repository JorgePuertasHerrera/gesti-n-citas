from app.models.user import User
from app.models.quotes import Quotes
from app.models.centers import Center
from app.models.categories import Categories
from app.models.message import Message
from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers.auth import router as auth_router
from app.routers.categories import router as categories_router
from app.routers.center import router as centers_router
from app.routers.quotes import router as quotes_router
from app.routers.users import router as users_router
from app.routers.chat import router as chat_router
app = FastAPI()

app.include_router(auth_router)
app.include_router(centers_router)
app.include_router(categories_router)
app.include_router(quotes_router)
app.include_router(users_router)
app.include_router(chat_router)
Base.metadata.create_all(engine)