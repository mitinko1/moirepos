from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="6708171543:AAGzgZhcUFiugtUu17s5HrRe1Pfcmh0zcEc")
dispather = Dispatcher(bot)

@dispather.message_handler()
async def handle_massage(message: types.Message):
    await message.answer(message.text)

executor.start_polling(dispather, skip_updates=True)