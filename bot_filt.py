import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat, BotCommandScopeAllPrivateChats, \
    BotCommandScopeAllGroupChats, BotCommandScopeAllChatAdministrators

from config import BOT_TOKEN
bot=Bot(token=BOT_TOKEN,parse_mode=types.ParseMode.HTML)
dp=Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async  def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('command_default_1', 'Стандартная команда 1'),
            BotCommand('command_default_2', 'Стандартная команда 2'),
            BotCommand('command_default_3', 'Стандартная команда 3'),

        ],
        scope=BotCommandScopeDefault(),
    )
async def set_starting_commands(bot: Bot, chat_id: int):
    STARTING_COMMANDS = {
        'ru':[
            BotCommand('start', 'Начать заново'),
            BotCommand('get_commands', 'Получить список команд'),
            BotCommand('reset_commands', 'Сбросить команды')
        ],
        'en':[
            BotCommand('start', 'Restart bot'),
            BotCommand('get_commands', 'Retrieve command list'),
            BotCommand('reset_commands', 'Reset commands')

        ]
    }
    for language_code, commands in STARTING_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code
        )
@dp.message_handler(commands='start')
async def user_start(message: types.Message):
   await message.reply('Hello')
   await set_starting_commands(message.bot, message.from_user.id)

@dp.message_handler(commands='reset_commands')
async def force_reset_all_commands(bot: Bot):
    for language_code in ('ru', 'en', 'el'):
        for scope in (
                BotCommandScopeDefault(),
                BotCommandScopeAllPrivateChats(),
                BotCommandScopeAllGroupChats(),
                BotCommandScopeAllChatAdministrators(),
        ):
            await bot.delete_my_commands(scope, language_code)



@dp.message_handler(commands='get_commands')
async def message_get_command(message: types.Message):
    no_lang=await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id))
    no_args = await message.bot.get_my_commands()
    ru_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id), language_code='ru')
    await message.reply('\n'.join(
        f'{arg}' for arg in (no_lang, no_args, ru_lang)
    ))


@dp.message_handler(lambda message: message.text == 'Пока')
async def bye(message: types.Message):
    await message.answer('Пока')

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)