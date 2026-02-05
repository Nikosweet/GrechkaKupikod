from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text
from database.database_url import settings
import asyncio


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False, # Вывод SQL-запросов в консоль
    pool_size = 5, # Количество возможных подключений
    max_overflow=10, # Доп. подключения при перегрузе (pool_size + max_overflow)
)



session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass

