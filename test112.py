import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text
from aiogram.types import BotCommandScopeDefault, BotCommand, BotCommandScopeChat, BotCommand
from filtres import IsPrivate, IsGroup
from config import BOT_TOKEN

# Объект бота
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

@dp.message_handler(IsPrivate(),commands='private')
async def start_bot(message: types.Message):
   await message.answer('Личный чат')

@dp.message_handler(IsGroup(),commands='group')
async def start_bot(message: types.Message):
   await message.answer('Групповой чат')

if __name__ == "__main__":
   # Запуск бота
   executor.start_polling(dp, skip_updates=True)
