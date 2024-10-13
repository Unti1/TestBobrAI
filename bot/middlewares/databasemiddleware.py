
from typing import Any, Awaitable, Callable, Coroutine, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from tools.database import AsyncSession

class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, database_session) -> None:
        super().__init__()
        self.database: AsyncSession = database_session

    async def __call__(self,
                 handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                 event: TelegramObject,
                 data: Dict[str, Any]) -> Coroutine[Any, Any, Any]:
        data['db'] = self.database
        return await handler(event, data)
