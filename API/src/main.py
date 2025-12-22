from fastapi import FastAPI
from src.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from src.routes.health import router as health_router
from src.routes.users import router as users_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(health_router)
app.include_router(users_router)