from bot.handlers import message_, commands_
from bot.middlewares.album_midddlleware import AlbumMiddleware
from bot.middlewares.databasemiddleware import DatabaseMiddleware
from bot.middlewares.message_history_middleware import MessageHistoryMiddleware
from tools.database import database_init 
from settings import *

async def bot_startup():
    bot = Bot(token = TELEGRAM_TOKEN)
    
    # async_session = await database_init()
    # database = async_session()
    # print(colored('[Database]', color = 'light_blue'), 'initilized')
    
    storage = RedisStorage.from_url(f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}')
    print(colored('[Redis]', color = 'light_blue'), 'initilized')

    dp = Dispatcher(storage=storage)
    dp.include_routers(
                       message_.router,
                       commands_.router,
                       )
    # dp.message.middleware(AlbumMiddleware())

    # # dp.message.middleware(DatabaseMiddleware(database))
    # # dp.callback_query.middleware(DatabaseMiddleware(database))
    
    # dp.message.middleware(MessageHistoryMiddleware(bot))
    # dp.callback_query.middleware(MessageHistoryMiddleware(bot))
    
    # print(colored('[Middlewares]', color = 'light_blue'), 'initilized')

    print(colored('[Bot]', color = 'light_green'), 'started')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(bot_startup())