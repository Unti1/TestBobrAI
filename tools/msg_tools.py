from settings import *


async def send_split_messages(sender:types.CallbackQuery | types.Message, text: str, keyboard: types.ReplyKeyboardMarkup| types.InlineKeyboardMarkup|None = None, chunk_size=4048):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    if isinstance(sender, types.CallbackQuery):
        sender = sender.message
    elif isinstance(sender, types.Message):
        pass
    else:
        raise TypeError('Sendes does not Message or Callback')

    with suppress(TelegramBadRequest):
        for i, chunk in enumerate(chunks):
            if i == len(chunks) - 1:  # Если это последний чанк 
                await sender.answer(chunk, parse_mode='Markdown', reply_markup=keyboard)
            else:
                await sender.answer(chunk, parse_mode='Markdown')
