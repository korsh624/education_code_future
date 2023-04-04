import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
API_TOKEN='5077133016:AAFeAjz4GDOe_39siIkaenFULthrEQ07YLY'
WEBHOOK_HOST='https://5df6-37-19-76-51.eu.ngrok.io'
WEBHOOK_PATH=''
WEBHOOK_URL=f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
WEBAPP_HOST='127.0.0.1'
WEBAPP_PORT=8000
logging.basicConfig(level=logging.INFO)
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
async def on_shutdown(dp):
    logging.warning('Shutdown bot')
    await bot.delete_webhook()
    logging.warning('Bye!')
@dp.message_handler(commands=['start'])
async def echo(message:types.Message):
    return SendMessage(message.chat.id,message.text)
@dp.message_handler(commands=['help'])
async def echo(message:types.Message):
    return SendMessage(message.chat.id,'Это справка бота')
if __name__=='__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )