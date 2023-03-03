from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="6011353395:AAEEi_ONTnc7-oZM5ILMUSE_H5gQOPc0ydE")
dp = Dispatcher(bot)

chat_id = '984568970'


@dp.message_handler()
async def pars(msg:types.Message):
    await bot.send_message(chat_id, msg.text[6:])

if __name__ == '__main__':
    executor.start_polling(dp)