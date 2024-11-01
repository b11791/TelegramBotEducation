import random

import aiogram
from aiogram import Router
from aiogram.filters import Command

from stickers_bot.create_bot import bot
from stickers_bot.db import SQLite

setter_router = Router()

@setter_router.message(Command("give"))
async def sticker(message: aiogram.types.Message):
    pass
    with open("static/sticker_packs.txt") as file:
        sticker_packs = file.read().split("\n")
    for pack_name in sticker_packs:
        with SQLite() as db:
            pack_id = db.cursor.execute(
                f"""
                INSERT INTO stickerpacks (name, category_id)
                VALUES ('{pack_name}', '{random.randint(1, 4)}')
                RETURNING id
                """
            ).fetchone()[0]
            db.connection.commit()

            object_stickers = await bot.get_sticker_set(pack_name)
            sql = """
                INSERT INTO stickers (tg_code, stickerpack_id)
                VALUES {}
            """.format(
                ",\n".join(
                    f"('{sticker.file_id}', '{pack_id}')"
                    for sticker in object_stickers.stickers
                )
            )
            db.cursor.execute(sql)
            db.connection.commit()