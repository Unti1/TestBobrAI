import json
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, TypeDecorator, or_, and_, distinct
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.future import select
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import case

from settings import config


class JSONEncodedType(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value, ensure_ascii=False)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

# Определение базового класса
DB: declarative_base = declarative_base()
# from models import *

async def database_init() -> AsyncSession:
    
    # Создание асинхронного движка
    engine = create_async_engine(
        config['database']['url'], 
        echo=True,
        connect_args={"check_same_thread": False}
    )
    
    # Асинхронное создание таблиц
    async with engine.begin() as conn:
        await conn.run_sync(DB.metadata.create_all)
    
    # Создание асинхронной сессии
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    
    return async_session