from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.user import get_user, get_users
from src.db.deps import get_db
from src.schemas.user import UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await get_users(db, skip, limit)

@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(404, "Такой пользователь не найден")
    return user