import logging
import multiprocessing.connection

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text
from aiogram.dispatcher import filters, FSMContext
from config import BOT_TOKEN
from config import SUPERUSER_IDS
bot=Bot(token=BOT_TOKEN,parse_mode=types.ParseMode.HTML)
dp=Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
IMLINCK=r'https://.+?\.(jpg|jpeg|png)'
IMCOMAND=r"/image: "+IMLINCK
FRASE=['C++', 'Python']

@dp.message_handler(chat_type='private', commands='is_pm')
async def chattypechek(msg:types.Message):
    await msg.answer('Это личные сообщения')

@dp.message_handler(is_forwarded=True)
async def checkforw(msg:types.Message):
    await msg.answer('Это чужле вообщение, пришли свое')

@dp.message_handler(is_reply=True,commands='user_id')
async def checkrepl(msg:types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)

@dp.message_handler(commands='change_photo',is_chat_admin=True)
async def chphoto(msg:types.Message):
    await msg.answer('Сменим фотку')

@dp.message_handler(filters.Text(contains=FRASE, ignore_case=True))
async def langprog(msg:types.Message):
    await msg.reply('Я тоже люблю программировать ')

@dp.message_handler(regexp_commands=[IMCOMAND])
async def imcmd(msg:types.Message):
    await msg.answer('Пришла команда на обработку картинки')

@dp.message_handler(regexp=IMLINCK)
async def images_link(msg:types.Message):
    await msg.answer('Классная картинка')


@dp.message_handler(hashtags='вопрос')
async def htchek(msg: types.Message):
    await msg.answer('мы получили ваш вопрос и обязательно на него ответим')

@dp.message_handler(chat_id=SUPERUSER_IDS)
async def superusercheck(msg:types.Message):
    await msg.answer('Super user!')
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
