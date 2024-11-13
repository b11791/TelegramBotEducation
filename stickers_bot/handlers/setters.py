import random

import aiogram
from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command

from stickers_bot.create_bot import bot
from stickers_bot.db import SQLite

setter_router = Router()


@setter_router.message(Command("set_stickers"))
async def sticker(message: aiogram.types.Message):
    with open("static/sticker_packs.txt") as file:
        sticker_packs = file.read().split("\n")
    for pack_name in sticker_packs:
        with SQLite() as db:
            pack_id = db.cursor.execute(
                f"""
                INSERT INTO stickerpacks (name, category_id)
                VALUES ('{pack_name}', '{random.randint(1, 4)}')
                ON CONFLICT(name) 
                DO NOTHING
                RETURNING id
                """
            ).fetchone()[0]
            db.connection.commit()

            try:
                object_stickers = await bot.get_sticker_set(pack_name)
            except TelegramBadRequest:
                await message.answer(f'Стикепака {pack_name} нет в природе блять.')
            else:
                sql = """
                    INSERT INTO stickers (tg_code, stickerpack_id)
                    VALUES {}
                    ON CONFLICT(tg_code) 
                    DO NOTHING;
                """.format(
                    ",\n".join(
                        f"('{sticker.file_id}', '{pack_id}')"
                        for sticker in object_stickers.stickers
                    )
                )
                db.cursor.execute(sql)
                db.connection.commit()

    await message.answer('Стикеры установлены')
