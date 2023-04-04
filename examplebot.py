import logging
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
bot=Bot(token=BOT_TOKEN,parse_mode=types.ParseMode.HTML)
dp=Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(CommandStart())
async def bot_start(message:types.Message):
    await message.answer(f'Привет <b>{message.from_user.full_name}</b>')

@dp.message_handler(CommandHelp())
async def bot_help(message:types.Message):
    await message.answer(f' {message.from_user.full_name}, вам нужна помощь ?')

@dp.message_handler(Text(startswith='Бот'))
async def startswichex(message:types.Message):
    await message.answer(f' {message.from_user.full_name}, начинается на Бот')

@dp.message_handler(Text(equals='проверка'))
async def startswichex(message:types.Message):
    await message.answer(f' {message.from_user.full_name}, проверка прошла')

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)