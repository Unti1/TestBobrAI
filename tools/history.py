import traceback
from typing import Dict, List, Optional
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

class MessageHistory():
    
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        self.data: Dict[str, List[Message]] = {}

    async def add(self, state: FSMContext, *messages: Optional[List[Message]]):
        data = await state.get_data()
        message_ids: List[str] = list(map(lambda x: x.message_id, messages)) # convert to ids
        try:
            if 'message_history' in data:
                data['id_for_history'] = messages[0].from_user.id
                data['message_history'].extend(message_ids)
            else:
                data['id_for_history'] = messages[0].from_user.id
                data['message_history'] = message_ids
            await state.update_data(data)
            return True
        except:
            print(traceback.format_exc())
            return False
        
    async def clear(self, state: FSMContext):
        data = await state.get_data()
        try:
            if 'message_history' in data:
                await self.bot.delete_messages(chat_id=data['id_for_history'], message_ids=data['message_history'])
            else:
                print('History does not exsist')
            return True
        except:
            print(traceback.format_exc())
            return False
    

