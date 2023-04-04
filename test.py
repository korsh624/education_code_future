import logging
from aiogram import Bot, Dispatcher, executor, types
TOKEN='5077133016:AAFeAjz4GDOe_39siIkaenFULthrEQ07YLY'
API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Вы ввели одну из команд.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
