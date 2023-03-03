import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

from states.user_state import UserState
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import db, dp, bot


@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_uchun(message: types.Message):
    boss_xisob = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Qabul qilingan'),
                KeyboardButton(text='Tugagan'),
            ],
        ],
        resize_keyboard=True
    )

    await message.answer("yo'nalishni tanlang", reply_markup=boss_xisob)


@dp.message_handler(text="Qabul qilingan", user_id=ADMINS[0])
async def topshiriq_uchun1(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Qabul qildim" in user[5]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\n🙎🏻‍♂qabul qildi : ❓{user[4]}❓")


@dp.message_handler(text="Tugagan", user_id=ADMINS[0])
async def topshiriq_uchun2(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "tugatildi" in user[5]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\n🙎🏻‍♂️bajardi : ✅{user[4]}✅")


@dp.callback_query_handler(text_contains="Mohir", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Mohir", id=uid)
    qabul_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq Mohirga yuborildi",reply_markup = ReplyKeyboardRemove())
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida1)


@dp.callback_query_handler(text_contains="Isomiddin", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[9:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Isomiddin", id=uid)
    qabul_haqida2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq Isomiddinga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida2)


@dp.callback_query_handler(text_contains="Zoxid", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Zoxid", id=uid)
    qabul_haqida3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq Zoxidga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida3)


@dp.callback_query_handler(text_contains="Iroda", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Iroda", id=uid)
    qabul_haqida4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq Irodaga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida4)


@dp.callback_query_handler(text_contains="Begzod", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Begzod", id=uid)
    qabul_haqida5 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq Begzodga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida5)


@dp.callback_query_handler(text_contains="Azim", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[4:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Azim", id=uid)
    qabul_haqida6 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq Azimga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida6)


@dp.callback_query_handler(text_contains="Abduraxmon", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[10:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Abduraxmon", id=uid)
    qabul_haqida7 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq Abduraxmonga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida7)


@dp.callback_query_handler(text_contains="Abdulvosit", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[10:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Abdulvosit", id=uid)
    qabul_haqida8 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq Abdulvositga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼  {user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida8)


@dp.callback_query_handler(text_contains="Rasul", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Buxgalter1", id=uid)
    qabul_haqida9 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq bug'alter1ga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼 {user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida9)


@dp.callback_query_handler(text_contains="Jasur", user_id=ADMINS[0])
async def answer_boss(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_bugalter(bugalter="Buxgalter2", id=uid)
    qabul_haqida10 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Qabul qildim', callback_data=f"qabul{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0], text=f"Topshiq bug'alter2ga yuborildi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Yangi topshiriq\n🧑‍💼 {user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=qabul_haqida10)