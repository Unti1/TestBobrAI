from typing import Any, Awaitable, Callable, Coroutine, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from tools.history import MessageHistory


class MessageHistoryMiddleware(BaseMiddleware):
    def __init__(self, bot) -> None:
        super().__init__()
        self.message_history = MessageHistory(bot)

    async def __call__(self, 
                 handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                 event: TelegramObject, 
                 data: Dict[str, Any]) -> Coroutine[Any, Any, Any]:
        data['history'] = self.message_history
        return await handler(event, data)