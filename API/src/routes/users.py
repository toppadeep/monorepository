from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.user import get_user, get_users, get_user_by_username
from src.db.deps import get_db
from src.schemas.user import UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead])
async def read_users(skip: int = 0, limit: int = 1000, db: AsyncSession = Depends(get_db)):
    return await get_users(db, skip, limit)

@router.get("/{username}", response_model=UserRead)
async def read_user(username: str, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_username(db, username)
    if not user:
        raise HTTPException(404, "Такой пользователь не найден")
    return user