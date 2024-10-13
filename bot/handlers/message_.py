from settings import *
from tools.weather import get_weather

router = Router()

@router.message(F.text)
async def get_city(message: types.Message):
    city = message.text
    weather = await get_weather(city)
    if weather:
        response = (f"Погода в {city}:\n"
                    f"Температура: {weather['temperature']}°C\n"
                    f"Влажность: {weather['humidity']}%\n"
                    f"Описание: {weather['description'].capitalize()}")
        await message.reply(response, parse_mode=ParseMode.HTML)
    else:
        await message.reply("Не удалось получить данные о погоде. Проверьте название города.")
