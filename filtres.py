from aiogram import types
from aiogram.dispatcher.filters import BoundFilter



class IsPrivate(BoundFilter):
   async def check(self,message:types.Message):
       return message.chat.type == types.ChatType.PRIVATE


class IsGroup(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )


