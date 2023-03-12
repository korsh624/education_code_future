import logging
import asyncio
from os import getenv
from aiogram import Bot, Dispatcher,types
from aiogram.utils.exceptions import BotBlocked
logging.basicConfig(level=logging.INFO)
bot_token=getenv('BOT_TOKEN')
bot=Bot(token=bot_token)
dp=Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message:types.Message):
    await message.answer("Привет! \n Напиши мне что-нибудь")

@dp.message_handler(commands=["help"])
async def cmd_test1(message:types.Message):
    await message.reply('Напиши мне что-нибудь и я отправлю этот текст тебе в ответ')

@dp.message_handler(commands='block')
async def cmd_block(msg:types.Message):
    await asyncio.sleep(10.0)
    await msg.reply('Вы заблокированы')

@dp.errors_handlers(exception=BotBlocked)
async def error_bot_blocked(update:types.Update,exception:BotBlocked):
    return True


@dp.message_handler()
async def echo_message(msg:types.Message):
    await bot.send_message(msg.from_user.id,msg.text)

async  def main():
    await dp.start_polling(bot)
if __name__=='__main__':
    asyncio.run(main())
