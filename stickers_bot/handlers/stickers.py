import random

import aiogram
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from aiogram import F

from stickers_bot.create_bot import bot
from stickers_bot.db import SQLite

sticker_router = Router()

@sticker_router.message(Command("give"))
async def sticker(message: aiogram.types.Message):
    with SQLite() as db:
        result = db.cursor.execute("SELECT tg_code from stickers").fetchall()
        tg_code = random.choice(result)["tg_code"]
    await bot.send_sticker(message.from_user.id, sticker=tg_code)


@sticker_router.callback_query(F.data.startswith("category_"))
async def sticker_take(call: CallbackQuery):
    pk = call.data.split("_")[1]
    with SQLite() as db:
        result = db.cursor.execute(f"""
            SELECT tg_code 
            from stickers s
            JOIN stickerpacks sp ON s.stickerpack_id = sp.id
            where sp.category_id = {pk} 
        """).fetchall()
    if not result:
        await call.message.answer("Стикеров такой категории не существует")
        return
    await call.message.answer_sticker(random.choice(result)["tg_code"])


