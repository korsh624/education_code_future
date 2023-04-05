import logging
from aiogram import Bot,Dispatcher,executor,types
bot=Bot(token='5077133016:AAFeAjz4GDOe_39siIkaenFULthrEQ07YLY',parse_mode=types.ParseMode.HTML )
dp=Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
ip=r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'
comand=r'\/help\:' +ip

@dp.message_handler(commands=['start'])
async def start(msg:types.Message):
    await msg.answer('Напиши /help чтобы получить помощь')

@dp.message_handler(regexp_commands=r'\/help\:' + ip)
async def help(msg:types.Message):
    await msg.answer('Запрос на проверку айпи адреса получен')

@dp.message_handler(regexp=ip)
async def regexpIp(msg:types.Message):
    await msg.answer('Правильный айпи')

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)