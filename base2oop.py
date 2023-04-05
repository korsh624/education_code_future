import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart

from config import BOT_TOKEN
import sqlite3
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
def logger(statement):
   print(f'''__________________EXECUTING{statement}___________''')
class Database:
   def __init__(self,path_to_db='test1.db'):
      self.path_to_db=path_to_db
   @property
   def connection(self):
      return sqlite3.connect(self.path_to_db)
   def execute(self,sql:str,parametrs:tuple=None,fetchone=False,fetchall=False,commit=False):
      if not parametrs:
         parametrs=tuple()
      connection=self.connection
      connection.set_trace_callback(logger)
      cursor=connection.cursor()
      data=None
      cursor.execute(sql,parametrs)
      if commit:
         connection.commit()
      if fetchone:
         data=cursor.fetchone()
      if fetchall:
         data=cursor.fetchall()
      connection.close()
      return data
   def create_table_users(self):
      sql="""CREATE TABLE Users(
      id int NOT NULL,
      name varchar(255) NOT NULL,
      email varchar(255),
      PRIMARY KEY (id)
      );
      """
      return self.execute(sql)
   def add_user(self,id:int, name:str,emaail:str=None):
      sql="INSERT INTO Users(id, name, email) VALUES(?,?,?)"
      parametrs=(id,name,emaail)
      self.execute(sql, parametrs=parametrs, commit=True)
   @staticmethod
   def format_args(sql,parametrs:dict):
      sql+=' AND '.join([f'{item}=?' for item in parametrs])
      return sql,tuple(parametrs.values())
   def select_all_users(self):
      sql="SELECT * FROM Users"
      return self.execute(sql,fetchall=True)
   def select_user(self,**kwargs):
      sql="SELECT * FROM User WHERE "
      sql,parameters=self.format_args(sql,kwargs)
      return self.execute(sql,parameters,fetchone=True)
   def count_users(self):
      return self.execute("SELECT COUNT(*) FROM Users;",fetchone=True)
   def update_email(self,email,id):
      sql="UPDATE User SET email=? WHERE id=?"
      return self.execute(sql,parametrs=(email,id),commit=True)
   def delete_all_users(self):
      self.execute("DELETEFROM Users WHERE TRUE")

db=Database()
try:
   db.create_table_users()
   print('Table created')
except Exception as e:
   print(e)
@dp.message_handler(CommandStart())
async def bot_start(message:types.Message):
   name=message.from_user.full_name
   try:
      db.add_user(id=message.from_user.id, name=name)
   except sqlite3.IntegrityError as err:
      print(err)
   count_users=db.count_users()[0]
   await message.answer(
      '\n'.join([
         f'Привет, {message.from_user.full_name}!',
         'Ты был занесен в базу данных',
         f'В базе данных {count_users} пользователей'
      ])
   )


if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)
