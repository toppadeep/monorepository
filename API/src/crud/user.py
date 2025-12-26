from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.user import User
from src.schemas.user import UserCreate

async def get_user(db: AsyncSession, user_id: int) -> User | None:
    return await db.get(User, user_id)

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 1000) -> list[User]:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

async def create_user(db: AsyncSession, obj_in: UserCreate) -> User:
    db_obj = User(**obj_in.model_dump())
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(
        select(User).where(User.username == username)
    )
    return result.scalars().first()