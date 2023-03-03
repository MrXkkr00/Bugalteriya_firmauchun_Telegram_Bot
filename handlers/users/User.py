# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from data.config import ADMINS
# from keyboards.inline.inline_bugalater import bugalterlarMenu
# from keyboards.inline.Javob_bossga import answer_qabulMenu, answer_yakunMenu
# from keyboards.default.bugalterlar_boss import bugalter_list
# from loader import dp, bot
# from aiogram.types import Message, CallbackQuery
# from states.Topshiriq import TopshiriqData
#
# # # Echo bot
# # @dp.message_handler(text="salom")
# # async def bot_echo(message: types.Message):
# #     await message.answer(f"chat_id=984568970", reply_markup=bugalterlarMenu)
#
#
# @dp.message_handler(state=None)
# async def select_category(message: Message):
#     await message.answer(f"Asslomu Alekum {message.from_user.full_name} \nBug'alteriya bo'yicha sizga qanday yordam kerak")
#     await TopshiriqData.topshiriq.set()
#
#
# @dp.message_handler(state=TopshiriqData.topshiriq)
# async def topshiriq_menu(message: Message, state: FSMContext):
#     await bot.send_message(chat_id=ADMINS[0], text=f"bug'alterni tanlang", reply_markup=bugalterlarMenu)
#     await TopshiriqData.bug_yonaltirish.set()
#
#
# @dp.callback_query_handler(text="Mohir1", state=TopshiriqData.bug_yonaltirish,)
# async def javob_bug(call: types.Message, state: FSMContext):
#     # await call.message.delete()
#     await bot.send_message(chat_id=ADMINS[1], text=f"Javob bering", reply_markup=answer_qabulMenu)
#     await state.finish()
# #
# #
# # @dp.callback_query_handler(text="qabul1", state=TopshiriqData.qabul_haqida)
# # async def boss_jav_qabul(call: CallbackQuery, state: FSMContext):
# #     await call.message.delete()
# #     await bot.send_message(chat_id=ADMINS[0], text=f"\nTopshiriq qabul qilindi")
# #     await bot.send_message(chat_id=ADMINS[1], text=f"\nHali Tugatmadingizmi", reply_markup=answer_yakunMenu)
# #     await TopshiriqData.about_finish.set()
# #
# #
# # @dp.callback_query_handler(text="tugatildi1", state=TopshiriqData.about_finish)
# # async def boss_jav_qabul(call: CallbackQuery, state: FSMContext):
# #     await call.message.delete()
# #     await bot.send_message(chat_id=ADMINS[0], text=f"\nTopshiriq balarildi", )
# #     await state.finish()
# #
# #
# #  topshiriq = State()
# #     bug_yonaltirish = State()
# #     qabul_haqida = State()
# # #
# # @dp.callback_query_handler(text="Isomiddin1")
# # async def buy_courses(call: CallbackQuery):
# #     await call.message.delete()
# #     await call.message.answer("Kurs tanlang")
# #     await call.answer(cache_time=60)
# #
# #
# # @dp.callback_query_handler(text="Zoxid1")
# # async def buy_courses(call: CallbackQuery):
# #     await call.message.delete()
# #     await call.message.answer("Kurs tanlang")
# #     await call.answer(cache_time=60)
# #
# #
# # @dp.callback_query_handler(text="Iroda1")
# # async def buy_courses(call: CallbackQuery):
# #     await call.message.delete()
# #     await call.message.answer("Kurs tanlang")
# #     await call.answer(cache_time=60)
# #
# #
# # @dp.callback_query_handler(text="Begzod1")
# # async def buy_courses(call: CallbackQuery):
# #     await call.message.delete()
# #     await call.message.answer("Kurs tanlang")
# #     await call.answer(cache_time=60)
# #
# #
# # @dp.callback_query_handler(text="Azim1")
# # async def buy_courses(call: CallbackQuery):
# #     await call.message.delete()
# #     await call.message.answer("Kurs tanlang")
# #     await call.answer(cache_time=60)
# #
# #
# # @dp.callback_query_handler(text="Abduraxmon1")
# # async def buy_courses(call: CallbackQuery):
# #     await call.message.delete()
# #     await call.message.answer("Kurs tanlang")
# #     await call.answer(cache_time=60)
# #
# #
# # @dp.callback_query_handler(text="Abdulvosit1")
# # async def buy_courses(call: CallbackQuery):
# #     await call.message.delete()
# #     await call.message.answer("Kurs tanlang")
# #     await call.answer(cache_time=60)
# #
# #
# # @dp.callback_query_handler(text="Buxgalter1")
# # async def buy_courses(call: CallbackQuery):
# #     await call.message.delete()
# #     await call.message.answer("Kurs tanlang" )
# #     await call.answer(cache_time=60)
# #
# #
# # @dp.callback_query_handler(text="Buxgalter2")
# # async def buy_courses(call: CallbackQuery):
# #     await call.message.delete()
# #     await call.message.answer("Kurs tanlang")
# #     await call.answer(cache_time=60)
