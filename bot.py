import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor,types
API_TOKEN='5077133016:AAFeAjz4GDOe_39siIkaenFULthrEQ07YLY'
logging.basicConfig(level=logging.INFO)
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
def create_table():
   conn=sqlite3.connect('users.db')
   cur=conn.cursor()
   print('create_table()')
   cur.execute('''CREATE TABLE IF NOT EXISTS users(
      userid INT PRIMARY KEY,
      username TEXT,
      message TEXT);
   ''')
   conn.commit()
   cur.close()
   conn.close()
@dp.message_handler(commands=['start'])
async def start_func(message:types.Message):
   await message.answer('Вы ввели команду /start')
@dp.message_handler(text='база')
async def echo(message:types.Message):
   conn = sqlite3.connect('users.db')
   cur = conn.cursor()
   user=cur.execute(f'''SELECT* FROM users WHERE userid={message.chat.id}''').fetchone()
   if not user:
      print('no')
      data=(message.chat.id,message.chat.username)
      cur.execute('''INSERT INTO users(userid, username) VALUES(?,?)''',data)
      conn.commit()
      conn.close()
      await message.answer('Вы добавлены в базу данных')
   else:
      print('yes')
   await message.answer('вы уже в базе данных')
if __name__=='__main__':
   create_table()
   executor.start_polling(dp,skip_updates=True)
