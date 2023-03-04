
from aiogram import types
from data.config import ADMINS
from loader import db, dp


@dp.message_handler(text="/topshiriq", user_id=ADMINS[1])
async def topshiriq_Mohir(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Mohir" in user[4]:
            await message.answer(f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[2])
async def topshiriq_MohZoxid(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Isomiddin" in user[4]:
            await message.answer(f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[3])
async def topshiriq_Zoxid(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Zoxid" in user[4]:
            await message.answer(f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[4])
async def topshiriq_Iroda(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Iroda" in user[4]:
            await message.answer(f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[5])
async def topshiriq_Begzod(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Begzod" in user[4]:
            await message.answer(f"🧑🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[6])
async def topshiriq_Azim(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Azim" in user[4]:
            await message.answer(f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[7])
async def topshiriq_Abduraxmon(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Abduraxmon" in user[4]:
            await message.answer(f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[8])
async def topshiriq_Abdulvosit(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Abdulvosit" in user[4]:
            await message.answer(f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")


@dp.message_handler(text="/Buxgalter1", user_id=ADMINS[9])
async def topshiriq_Abdulvosit1(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Buxgalter1" in user[4]:
            await message.answer(f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")


@dp.message_handler(text="/topshiriq", user_id=ADMINS[10])
async def topshiriq_Buxgalter2(message: types.Message):
    users = db.select_all_users()
    for user in users:
        if "Buxgalter2" in user[4]:
            await message.answer(f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}\n♻️ Jarayon : {user[5]}")



