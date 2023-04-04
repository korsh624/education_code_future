import logging
from aiogram import types, Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
TOKEN = "6005078473:AAFb89MDRIIM-DNBV8FMGrfWNcuOq48tjzQ"
WH_HOST = "ngrok бла бла бла"
WH_PATH = ""
WH_URL = f"{WH_HOST}{WH_PATH}"
WEBAPP_HOST = "127.0.0.documents"
WEBAPP_PORT = 8000
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = dispatcher.Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def starting(dp):
    await bot.set_webhook(WH_URL)


async def shutdown(dp):
    logging.warning("выключаемся")
    await bot.delete_webhook()
    logging.warning("пока-пока")


@dp.message_handler(commands=["help"])
async def help(msg: types.Message):
    return SendMessage(msg.from_user.id, 'SkecthDuudeBot — бот, созданный на языке програмирования питон чуваком '
                                               'под ником @De_Duude в рамках проекта "Код будущего" '
                                               'от Университета Иннополис \n'
                                               '\n'
                                               'Комманды:\n'
                                               '\n'
                                               '/start - поприветствовать\n'
                                               '/help - справка о боте и различные команды\n'
                                               '/echo - запустить "эхо"')



@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    return SendMessage(msg.from_user.id, "Привет, я SketchDuudeBot, рад знакомству!")
    

@dp.message_handler(commands=["echo"])
async def echo(msg: types.Message):
    SendMessage(msg.from_user.id, 'Запущен "эхо режим"')

    @dp.message_handler(content_types=["text"])
    async def echo_text(msg: types.Message):
        return SendMessage(msg.from_user.id, msg.text)

    @dp.message_handler(content_types=["photo"])
    async def echo_photo(msg: types.Message):
        return SendMessage(msg.from_user.id, msg.photo[0].file_id)

    @dp.message_handler(content_types=["video"])
    async def echo_video(msg: types.Message):
        return SendMessage(msg.from_user.id, msg.video.file_id)

    @dp.message_handler(content_types=["sticker"])
    async def echo_sticker(msg: types.Message):
        return SendMessage(msg.from_user.id, msg.sticker.file_id)

    @dp.message_handler(content_types=["document"])
    async def echo_document(msg: types.Message):
        return SendMessage(msg.from_user.id, msg.document.file_id)

    @dp.message_handler(content_types=["audio"])
    async def echo_audio(msg: types.Message):
        return SendMessage(msg.from_user.id, msg.audio.file_id)

    @dp.message_handler(content_types=["voice"])
    async def echo_voice(msg: types.Message):
        return SendMessage(msg.from_user.id, msg.voice.file_id)

    @dp.message_handler(content_types=["animation"])
    async def echo_sticker(msg: types.Message):
        return SendMessage(msg.from_user.id, msg.animation.file_id)


if True:
    start_webhook(dispatcher=dp, webhook_path=WH_PATH, on_startup=starting(dp), on_shutdown=shutdown(dp),
                  skip_updates=True, host=WEBAPP_HOST, port=WEBAPP_PORT)