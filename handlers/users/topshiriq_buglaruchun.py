import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

from states.user_state import UserState
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import db, dp, bot
#
 #
 #

 #
 #
 #
 #
 #
 #Buxgalter2

@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_Mohir(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Mohir" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_MohZoxid(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Isomiddin" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_Zoxid(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Zoxid" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_Iroda(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Iroda" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_Begzod(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Begzod" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_Azim(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Azim" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_Abduraxmon(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Abduraxmon" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_Abdulvosit(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Abdulvosit" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")


@dp.message_handler(text="/Buxgalter1", user_id=ADMINS[0])
async def topshiriq_Abdulvosit1(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Buxgalter1" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[0])
async def topshiriq_Buxgalter2(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Buxgalter2" in user[4]:
            await message.answer(f"🧑‍💼{user[1]} tomindan \n🗂Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}\nJarayon : {user[5]}")



