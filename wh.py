API_TOKEN='5778460602:AAGZXwts3NRufWb3ygixgSM0H7hlkuksCZw'
import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

WEBHOOK_HOST = ' https://4379-77-40-95-217.eu.ngrok.io'
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '127.0.0.1'
WEBAPP_PORT = 4040
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    logging.warning('Shutdown...')
    await bot.delete_webhook()
    logging.warning('Bye!')

@dp.message_handler(commands=['start'])
async def start_message(msg:types.Message):
    username=msg.from_user.username
    return SendMessage(msg.chat.id, f'Приветствую уважаемый(ая) @{username}, нажми /help')

@dp.message_handler(commands=['help'])
async def help_message(msg:types.Message):
    return SendMessage(msg.chat.id, 'Напиши мне что нибудь и я за тобой повторю!(Не добавил...)')

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
