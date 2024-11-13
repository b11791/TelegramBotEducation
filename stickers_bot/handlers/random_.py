from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery

import random
import aiogram

from stickers_bot.create_bot import bot
from stickers_bot.db import SQLite
from stickers_bot.keyboards.random_ import kb_1, kb_2, get_stickers_keyboard

random_router = Router()


@random_router.message(Command("start"))
async def startuem(message: aiogram.types.Message):
    await message.answer(text='HI', reply_markup=kb_1)


@random_router.message(Command("go_joke"))
async def joke(message: aiogram.types.Message):

    await message.answer(text='Анекдот для поднятия кондиций:'
                              '\n Ебет один клоун другого, а режиссер думает: «Блять, что-то съемки "Оно 3" пошли не'
                              ' по плану», но продолжает снимать', reply_markup=kb_2)

@random_router.message(Command("location"))
async def location(message: aiogram.types.Message):
    await bot.send_location(message.from_user.id, latitude=random.randint(1, 90),
                            longitude=random.randint(1, 180), reply_markup=kb_1)


@random_router.message(Command("picture"))
async def picmi(message: aiogram.types.Message):
    await bot.send_photo(message.from_user.id,
                         photo="https://avatars.dzeninfra.ru/get-zen_doc/1594475/pub_5ceb78dcae6fed00b3fbe21f_5ceb7e82ae6fed00b3fbe27e/scale_1200",
                         caption="Мишаня кондиции",
                         reply_markup=kb_1)

@random_router.callback_query(aiogram.F.data == "new_anec")
async def take_callback(callback: CallbackQuery):
    await callback.answer(show_alert=True, text="Ты чё сигма")
    await joke(message=callback.message)

@random_router.message(Command("stickers"))
async def stickers_menu(message: aiogram.types.Message):
    keyboard = get_stickers_keyboard()
    await message.answer("ВЫбери категорию стикеров", reply_markup=keyboard)

