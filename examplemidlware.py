from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

block_users = ['id пользователя']


class SomeMiddleware(BaseMiddleware):
   async def on_pre_process_update(self, update: types.Update, data: dict):
       print('on_pre_process_update')
       data['middleware_data'] = 'some update data'
       if update.message:
           await update.message.answer('on_pre_process_update')

   async def on_process_update(self, update: types.Update, data: dict):
       print(f'on_process_update, {data=}')

   async def on_pre_process_message(self, message: types.Message, data: dict):
       print(f'on_pre_process_message, {data=}')
       data['middleware_data1'] = 'some message data1'
       user_id = str(message.from_user.id)
       print(user_id, user_id in block_users)
       data['is_blocked'] = user_id in block_users
       # if user_id in block_users:
       #     await message.answer('ты в бане')
       #     raise CancelHandler()

   async def on_process_message(self, message: types.Message, data: dict):
       print(f'on_process_message, {data=}')
       data['middleware_data2'] = 'some message data2'
       user_id = str(message.from_user.id)
       data['user_id'] = user_id
       data['user'] = '123456'

   async def on_post_process_message(self, message: types.Message, data_from_handler: list, data: dict):
       print(f'on_post_process_message, {data=}, {data_from_handler=}')
       data['middleware_data3'] = 'some message data3'


if __name__ == '__main__':
   dp.middleware.setup(SomeMiddleware())
   executor.start_polling(dp, skip_updates=True)
