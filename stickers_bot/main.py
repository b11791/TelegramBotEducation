import asyncio

import aiogram

from aiogram.types import BotCommand

from stickers_bot import sql_queries
from stickers_bot.create_bot import bot
from stickers_bot.db import SQLite
from stickers_bot.handlers.random_ import random_router

dp = aiogram.Dispatcher()
dp.include_router(
    random_router,
)


async def create_tables():
    with SQLite() as db:
        db.cursor.execute(sql_queries.create_table)
        db.cursor.execute(sql_queries.create_super_user)
        db.connection.commit()
    print("База данных настроена")


async def setup_bot_commands():
    bot_commands = [
        BotCommand(command="/go_joke", description="анекдот для поднятия кондиций"),
        BotCommand(command="/give", description="рандомная херь"),
        BotCommand(command="/start", description="начать заново"),
        BotCommand(command="/picture", description="асхаб тамаев"),
        BotCommand(command="/location", description="спортики сват"),
    ]
    await bot.set_my_commands(bot_commands)
    print("Комманды обновлены")


async def set_stickers():
    with open("static/sticker_packs.txt") as file:
        sticker_packs = file.readlines()
    stickers_id = []
    for sticker_pack_name in sticker_packs:
        sticker_pack = await bot.get_sticker_set(sticker_pack_name)
        stickers_id.extend(
            sticker.file_id
            for sticker in sticker_pack.stickers
        )
    with open("static/sticker_id.txt", "w") as file:
        file.write("\n".join(stickers_id))
    print("Стикерпаки обновлены")


@dp.startup()
async def start():
    await setup_bot_commands()
    # await set_stickers()
    await create_tables()
    print("Бот запущен. ИДИТЕ НАХУЙ!")


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
