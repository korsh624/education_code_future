import logging
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from config import BOT_TOKEN
bot=Bot(token=BOT_TOKEN,parse_mode=types.ParseMode.HTML)
dp=Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
@dp.message_handler(Command('start',ignore_caption=False))
async def cmd_test1(message:types.Message):
    await message.answer(f'Привет, <b>{fmt.quote_html(message.text)}</b>')

@dp.message_handler(content_types=[types.ContentType.ANIMATION])
async def echo_document(message:types.Message):
    await message.reply_animation(message.animation.file_id)

@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def echo_document(message:types.Message):
    await message.reply_photo(message.photo[-1].file_id)


@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def download_doc(message:types.Message):
    await message.document.download()
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)