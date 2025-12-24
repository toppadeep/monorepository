from fastapi import FastAPI
from src.core.config import settings
from src.routes.health import router as health_router
from src.routes.users import router as users_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.include_router(health_router)
app.include_router(users_router)