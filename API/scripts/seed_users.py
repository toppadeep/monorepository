import sys
from pathlib import Path

# Добавляем корень проекта в sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.models.base import Base
from src.models.user import User
from src.core.config import settings

import asyncio
import httpx
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

URL = "https://jsonplaceholder.typicode.com/users"

async def seed():
    engine = create_async_engine(settings.database_url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with AsyncSession(engine) as session:
        async with httpx.AsyncClient() as client:
            resp = await client.get(URL)
            data = resp.json()

        users = []
        for item in data:
            users.append(User(
                id=item["id"],
                name=item["name"],
                username=item["username"],
                email=item["email"],
                website=item.get("website"),
                company_name=item["company"].get("name")
            ))

        session.add_all(users)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed())