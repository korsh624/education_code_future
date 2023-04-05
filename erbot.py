import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Update
from config import BOT_TOKEN
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(CommandStart())
async def bot_start(message:types.Message):
   not_exist_user=1111
   try:
      await message.answer('bag tag <b>error<b>')
   except Exception as err:
      await message.answer(f'not in eeror handler {err}')
   try:
      await bot.send_message(chat_id=not_exist_user,text='not exist user hello')
   except Exception as err:
      await message.answer(f'not in errorhandler {err}')
   await message.answer('not exist <fff>tag</fff>')
   logging.info('is not worcking and not ckrash bot')
   await message.answer('hello')
@dp.errors_handler()
async def errors_handler(update,exception):
   """
       Exceptions handler. Catches all exceptions within task factory tasks.
       :param update:
       :param exception:
       :return: stdout logging
       """
   from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                         CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                         MessageTextIsEmpty, RetryAfter,
                                         CantParseEntities, MessageCantBeDeleted, BadRequest)

   if isinstance(exception, CantDemoteChatCreator):
      logging.debug("Can't demote chat creator")
      return True

   if isinstance(exception, MessageNotModified):
      logging.debug('Message is not modified')
      return True
   if isinstance(exception, MessageCantBeDeleted):
      logging.debug('Message cant be deleted')
      return True

   if isinstance(exception, MessageToDeleteNotFound):
      logging.debug('Message to delete not found')
      return True

   if isinstance(exception, MessageTextIsEmpty):
      logging.debug('MessageTextIsEmpty')
      return True

   if isinstance(exception, Unauthorized):
      logging.info(f'Unauthorized: {exception}')
      return True

   if isinstance(exception, InvalidQueryID):
      logging.exception(f'InvalidQueryID: {exception} \nUpdate: {update}')
      return True

   if isinstance(exception, TelegramAPIError):
      logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
      return True
   if isinstance(exception, RetryAfter):
      logging.exception(f'RetryAfter: {exception} \nUpdate: {update}')
      return True
   if isinstance(exception, CantParseEntities):
      logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
      return True
   if isinstance(exception, BadRequest):
      logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
      return True
   logging.exception(f'Update: {update} \n{exception}')
   if isinstance(exception, CantParseEntities):
      await Update.get_current().message.answer(f'Попало в error handler. CantParseEntities: {exception.args}')
      return True


if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)
