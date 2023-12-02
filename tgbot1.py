from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import *

bot = Bot(token="6708171543:AAGzgZhcUFiugtUu17s5HrRe1Pfcmh0zcEc")
dispather = Dispatcher(bot)

button1 = KeyboardButton("/Дай_кораблллллъъъъ!!!!")
button2 = KeyboardButton("/s")
keyboard = ReplyKeyboardMarkup()
keyboard.add(button1).add(button2)
@dispather.message_handler(commands=['start'])
async def handle_massage1(message: types.Message):
    await message.answer("Вот клавиатура", reply_markup=keyboard)

@dispather.message_handler(commands=['s'])
async def handle_massage2(message: types.Message):
    await bot.send_message(message.from_user.id, "стартуееем")
@dispather.message_handler(commands=['Дай_кораблллллъъъъ!!!!'])
async def handle_massage3(message: types.Message):
    await message.answer("стартуееем")

executor.start_polling(dispather, skip_updates=True)
