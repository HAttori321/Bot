from aiogram import Bot, Dispatcher, types, Router
import asyncio
from aiogram.filters import CommandStart, Command
from filter.chat_types import ChatTypeFilter
from API.api import get_chat_gpt_response


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))
@user_private_router.message(CommandStart())#message
async def start_cmd(message: types.Message):
    await message.answer("Hello, i`m your virtual helper")

@user_private_router.message(Command("menu"))#message
async def menu_cmd(message: types.Message):
    await message.answer("Menu:\n1. /menu\n2. /help\n3. /echo\n4. /start")

@user_private_router.message(Command("gpt"))
async def gpt_cmd(message: types.Message):
    answer=get_chat_gpt_response(message[4:])
    await message.answer(answer)


@user_private_router.message()#message
async def new_method(message: types.Message, bot:Bot):
    await bot.send_message(message.from_user.id, "Answer from new method")
    await message.answer(message.text)
    await message.reply(message.text)






@user_private_router.message()#message
async def echo(message: types.Message):
    # text = message.text
    # if text in ["hi", "hello", "привет", "привіт"]:
    #     await message.answer("Hello to you!")
    # elif text in ["bye", "goodbye", "пока", "бувай"]:
    #     await message.answer("Goodbye!")
    # else:
    await message.answer(message.text)

