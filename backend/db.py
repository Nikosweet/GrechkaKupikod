from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from models.db_url import settings
import asyncio

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True, # Вывод SQL-запроов в консоль
    pool_size = 5, # Количество возможных подключений
    max_overflow=10, # Доп. подключения при перегрузе (pool_size + max_overflow)
)


async def get_table():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT * FROM person"))
        print(res.all())

asyncio.run(get_table())

