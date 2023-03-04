

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from states.user_state import UserState
from aiogram import types

from data.config import ADMINS
from loader import db, dp, bot


@dp.message_handler(text="/start")
async def bot_start(message: types.Message):

    await message.answer(f"      Xush kelibsiz!\n📕To'liq Ism Familyangizni kiriting")
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def topshiriq_menu(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {"name": fullname}
    )

    await message.answer("📕 Telefon Raqamingizni kiriting\n📱 (Masalan) : 991112233 ")
    await UserState.nomer.set()


@dp.message_handler(state=UserState.nomer)
async def nomer_menu(message: types.Message, state: FSMContext):
    nomer = message.text
    await state.update_data(
        {"nomer": nomer}
    )

    await message.answer("Bug'alteriya borasida \nBizdan qanaday yordam kerak")
    await UserState.topshiriq.set()


@dp.message_handler(state=UserState.topshiriq)
async def topshiriq_menu(message: types.Message, state: FSMContext):
    topshiriq = message.text
    await state.update_data(
        {"topshiriq": topshiriq}
    )
    id = message.from_user.id
    data = await state.get_data()
    name = data.get("name")
    nomer= data.get("nomer")
    topshiriq = data.get("topshiriq")
    user_id = []
    users = db.select_all_users()
    for user in users:
        user_id.append(user[0])
    if id in user_id:
        db.update_user_sorov(sorov=topshiriq, id=id)
        db.update_user_nomer(nomer=nomer, id=id)
    else:
        db.add_user(id=message.from_user.id, name=name, nomer=nomer, sorov=topshiriq, bugalter="null", jarayon="null")

    bugalterlarMenu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👨‍💻Mohir', callback_data=f"Mohir{id}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Isomiddin', callback_data=f"Isomiddin{id}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Zoxid', callback_data=f"Zoxid{id}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Iroda', callback_data=f"Iroda{id}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Begzod', callback_data=f"Begzod{id}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Azim', callback_data=f"Azim{id}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Abduraxmon', callback_data=f"Abduraxmon{id}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻Abdulvosit', callback_data=f"Abdulvosit{id}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻bugalter1', callback_data=f"Rasul{id}")
            ],
            [
                InlineKeyboardButton(text='👨‍💻bugalter2', callback_data=f"Jasur{id}")
            ],
        ],
        one_time_keyboard=True
    )
    user = db.select_user(id=id)
    await message.answer(f"Sizning so'rovingiz tez orada ko'rib chiqiladi")
    await bot.send_message(chat_id=ADMINS[0], text=f"🙋🏻‍♂️Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami :  {user[2]}\n")
    await bot.send_message(chat_id=ADMINS[0], text=f"Bug'alterni tanlang", reply_markup=bugalterlarMenu)
    await state.finish()
