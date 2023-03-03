from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    name = State()
    nomer = State()
    topshiriq = State()
