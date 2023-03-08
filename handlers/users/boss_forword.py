from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

from aiogram import types
from data.config import ADMINS
from loader import dp, bot





@dp.message_handler( user_id=ADMINS[0])
async def hammasi_uchun(message: types.Message):
    topshiriq = message.text


    Menuboss = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👨‍💻Mohir', callback_data=f"M00ohir{topshiriq}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Isomiddin', callback_data=f"I00somiddin{topshiriq}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Zoxid', callback_data=f"Z00oxid{topshiriq}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Iroda', callback_data=f"I00roda{topshiriq}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Begzod', callback_data=f"B00egzod{topshiriq}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Azim', callback_data=f"A00zim{topshiriq}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Abduraxmon', callback_data=f"A00bduraxmon{topshiriq}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Abdulvosit', callback_data=f"A00bdulvosit{topshiriq}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻bugalter1', callback_data=f"R00asul{topshiriq}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻bugalter2', callback_data=f"J00asur{topshiriq}")
            ],
        ],
        one_time_keyboard=True
    )
    await message.answer(f"Bug'alterni tanlang", reply_markup=Menuboss)


@dp.callback_query_handler(text_contains="M00ohir", user_id=ADMINS[0])
async def answer_boss0901(message: CallbackQuery):
    data1 = message.data
    top = data1[7:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Mohirga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=top)


@dp.callback_query_handler(text_contains="I00somiddin", user_id=ADMINS[0])
async def answer_boss09002(message: CallbackQuery):
    data1 = message.data
    top = data1[11:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Isomiddinga yuborildi")
    await bot.send_message(chat_id=ADMINS[2], text=top)



@dp.callback_query_handler(text_contains="Z00oxid", user_id=ADMINS[0])
async def answer_boss09003(message: CallbackQuery):
    data1 = message.data
    top = data1[7:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Zoxidga yuborildi")
    await bot.send_message(chat_id=ADMINS[3], text=top)


@dp.callback_query_handler(text_contains="I00roda", user_id=ADMINS[0])
async def answer_boss09004(message: CallbackQuery):
    data1 = message.data
    top = data1[7:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Irodaga yuborildi")
    await bot.send_message(chat_id=ADMINS[4], text=top)


@dp.callback_query_handler(text_contains="B00egzod", user_id=ADMINS[0])
async def answer_boss09050(message: CallbackQuery):
    data1 = message.data
    top = data1[8:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Bekzodga yuborildi")
    await bot.send_message(chat_id=ADMINS[5], text=top)


@dp.callback_query_handler(text_contains="A00zim", user_id=ADMINS[0])
async def answer_boss09006(message: CallbackQuery):
    data1 = message.data
    top = data1[6:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Azimga yuborildi")
    await bot.send_message(chat_id=ADMINS[6], text=top)


@dp.callback_query_handler(text_contains="A00bduraxmon", user_id=ADMINS[0])
async def answer_boss09007(message: CallbackQuery):
    data1 = message.data
    top = data1[12:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Abduraxmonga yuborildi")
    await bot.send_message(chat_id=ADMINS[7], text=top)


@dp.callback_query_handler(text_contains="A00bdulvosit", user_id=ADMINS[0])
async def answer_boss09080(message: CallbackQuery):
    data1 = message.data
    top = data1[12:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Abdulvosit yuborildi")
    await bot.send_message(chat_id=ADMINS[8], text=top)


@dp.callback_query_handler(text_contains="R00asul", user_id=ADMINS[0])
async def answer_boss09090(message: CallbackQuery):
    data1 = message.data
    top = data1[7:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Bug'alter1ga yuborildi")
    await bot.send_message(chat_id=ADMINS[9], text=top)


@dp.callback_query_handler(text_contains="J00asur", user_id=ADMINS[0])
async def answer_boss0900(message: CallbackQuery):
    data1 = message.data
    top = data1[7:]

    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"✅Topshiq Bug'alter2ga yuborildi")
    await bot.send_message(chat_id=ADMINS[10], text=top)
