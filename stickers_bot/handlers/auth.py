import aiogram
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from db import SQLite
from filters.register_check import UnregisterCheckFilter
from keyboards.random_ import kb3, kb_1
from sql_queries import insert_user

auth_router = Router()


class Reg(StatesGroup):
    name = State()
    cm = State()
    age = State()


@auth_router.message(UnregisterCheckFilter(), aiogram.F.text == "Вступить в Вагнер")
async def reg1(message: aiogram.types.Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Введите ваше имя")


@auth_router.message(Reg.name)
async def reg2(message: aiogram.types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.cm)
    await message.answer("Введите ваши сантиблятьметры")


@auth_router.message(Reg.cm)
async def reg3(message: aiogram.types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Сантиметры должны быть числом")
        return
    if int(message.text) < 20:
        await message.answer("Ебать ты лох ебанный пиздец")
    await state.update_data(cm=message.text)
    await state.set_state(Reg.age)
    await message.answer("Введите ваше да мне похуй")


@auth_router.message(Reg.age)
async def reg3(message: aiogram.types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Возраст должен быть числом")
        return
    await state.update_data(age=message.text)
    data = await state.get_data()
    await state.clear()
    try:
        with SQLite() as db:
            db.cursor.execute(insert_user.format(
                message.from_user.id,
                data["name"],
                data["cm"],
                data["age"]
            ))
            db.connection.commit()
    except:
        await message.answer("У вас бульон кипит")
    else:
        await message.answer("Кроме вас ошибок в природе нет", reply_markup=kb_1)


@auth_router.message(UnregisterCheckFilter())
async def register_handler(message: aiogram.types.Message):
    await message.answer("Регистрация блять нахуй охладите свое трахание", reply_markup=kb3)
