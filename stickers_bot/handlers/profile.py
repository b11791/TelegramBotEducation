import aiogram
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery

from stickers_bot.db import SQLite
from stickers_bot.keyboards.random_ import kb_profile
from stickers_bot.sql_queries import select_user_info

profile_router = Router()


class Edit(StatesGroup):
    value = State()


@profile_router.message(Command("edit_profile"))
async def edit_profile(message: aiogram.types.Message):

    with SQLite() as db:
        user_data = db.cursor.execute(
            select_user_info.format(message.from_user.id)
        ).fetchone()
    await message.answer(f"Твои даннцнгусеуЖ\n   Имя: <b>{user_data[0]}</b>\n"
                         f"   Метры в жопе: <span class='tg-spoiler'>{user_data[2]}</span>\n"
                         f"   Возраст: <b>{user_data[1]}</b>", parse_mode="html")
    await message.answer("Выбери что хочешь жестко отредактировать", reply_markup=kb_profile)


@profile_router.callback_query(aiogram.F.data.startswith("edit_"))
async def take_callback(callback: CallbackQuery, state: FSMContext):
    field_name = callback.data.split("_")[1]
    await callback.message.answer("Введи новое значение")
    await state.update_data(field_name=field_name)
    await state.update_data(count=0)
    await state.set_state(Edit.value)


@profile_router.message(Edit.value)
async def take_callback(message: aiogram.types.Message, state: FSMContext):
    data = await state.get_data()
    field_name = data["field_name"]
    count = data["count"] + 1

    new_data = message.text
    if field_name in ("age", "cm") and not new_data.isdigit():
        await state.update_data(count=count)
        if count >= 3:
            await message.answer("1 Я ебал твою жирпную мамашу\n"
                                 "2 Я ебал твою сестру\n"
                                 "3 Чемодан - вокзал - нахуц")
            sql_delete = f"DELETE FROM profile WHERE tg_id = {message.from_user.id}"
            with SQLite() as db:
                db.cursor.execute(sql_delete)
                db.connection.commit()
            await state.clear()
        else:
            await message.answer("ААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА ДОЛБАЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁБ")
            await message.answer("ЦИФРЫ ВВОДИ НАХУЙ")
        return

    sql_insert = f"UPDATE profile SET {field_name} = '{new_data}' WHERE tg_id = {message.from_user.id}"
    with SQLite() as db:
        db.cursor.execute(sql_insert)
        db.connection.commit()

    await state.clear()
    await edit_profile(message)