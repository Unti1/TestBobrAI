from settings import *

router = Router()

@router.message(Command('start'))
async def start_command(message: types.Message):
    await message.reply("Привет! Отправь мне название города, и я расскажу тебе какая погода сейчас в нём!")
