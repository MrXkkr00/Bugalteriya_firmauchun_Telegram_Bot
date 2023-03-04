from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from data.config import ADMINS
from loader import db, dp, bot


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[1])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅Mohir✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[1])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]} \n✅Mohir✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[2])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅Isomiddin✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[2])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]} \n✅Isomiddin✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[3])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅Zoxid✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[3])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]} \n✅Zoxid✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[4])
async def answer_boss2(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅Iroda✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[4])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️Mijoz : {user[1]} \n🗂 Topshiriq : {user[2]}\n📱Mijoz raqami : {user[2]} \n✅Iroda✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[5])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅Begzod✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[5])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]} \n✅Begzod✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[6])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅Azim✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[6])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]} \n✅Azim✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[7])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅Abduraxmon✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[7])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]} \n✅Abduraxmon✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[8])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅Abdulvosit✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[8])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]} \n✅Abdulvosit✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[9])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅bug'alter1✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[9])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[2]}\n📱Mijoz raqami : {user[2]} \n✅bug'alter1✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")


@dp.callback_query_handler(text_contains="qabul", user_id=ADMINS[10])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[5:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="qabul_qilindi", id=uid)
    jarayon_haqida1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Tugatdim', callback_data=f"finish{uid}")
            ],
        ]
    )
    await message.message.delete()
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n✅bug'alter2✅ topshiriqni Qabul qildi")
    await bot.send_message(chat_id=ADMINS[1],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]}",
                           reply_markup=jarayon_haqida1)


@dp.callback_query_handler(text_contains="finish", user_id=ADMINS[10])
async def answer_boss1(message: CallbackQuery):
    data1 = message.data
    uid = int(data1[6:])
    user = db.select_user(id=uid)
    db.update_user_jarayon(jarayon="tugatildi", id=uid)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"🙋🏻‍♂️ Mijoz : {user[1]} \n🗂 Topshiriq : {user[3]}\n📱 Mijoz raqami : {user[2]} \n✅bug'alter2✅ topshiriqni tugatdi")
    await bot.send_message(chat_id=ADMINS[1], text=f"Katta Raxmat")
    await bot.send_message(chat_id=user[0], text=f"Sizning vazifangiz \n {user[3]} \nBajarildi")
