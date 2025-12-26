import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import asyncio
from faker import Faker

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.dialects.postgresql import insert

from src.models.base import Base
from src.models.user import User
from src.core.config import settings


USERS_COUNT = 1000 


async def seed_users() -> None:
    fake = Faker()

    engine = create_async_engine(settings.database_url, echo=False)
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    # создаём таблицы (dev-safe)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    rows = [
        {
            "name": fake.name(),
            "username": fake.unique.user_name(),
            "email": fake.unique.email(),
            "website": fake.url(),
            "company_name": fake.company(),
        }
        for _ in range(USERS_COUNT)
    ]

    async with async_session() as session:
        stmt = (
            insert(User)
            .values(rows)
            .on_conflict_do_nothing(index_elements=["email"])
        )
        await session.execute(stmt)
        await session.commit()

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(seed_users())
