import asyncio

import aiogram

from aiogram.types import BotCommand

from handlers.auth import auth_router
from handlers.setters import setter_router
from stickers_bot import sql_queries
from stickers_bot.create_bot import bot
from stickers_bot.db import SQLite
from stickers_bot.handlers.profile import profile_router
from stickers_bot.handlers.random_ import random_router
from stickers_bot.handlers.stickers import sticker_router

dp = aiogram.Dispatcher()

dp.include_routers(
    auth_router,
    random_router,
    sticker_router,
    setter_router,
    profile_router,
)


async def create_tables():
    with SQLite() as db:
        db.cursor.execute(sql_queries.create_table_user)
        db.cursor.execute(sql_queries.create_super_user)
        db.cursor.execute(sql_queries.create_table_category)
        db.cursor.execute(sql_queries.create_table_stickerpacks)
        db.cursor.execute(sql_queries.create_table_stickers)
        db.cursor.execute(sql_queries.create_categories)
        db.connection.commit()
    print("База данных настроена")


async def setup_bot_commands():
    bot_commands = [
        BotCommand(command="/go_joke", description="анекдот для поднятия кондиций"),
        BotCommand(command="/give", description="рандомная херь"),
        BotCommand(command="/start", description="начать заново"),
        BotCommand(command="/picture", description="асхаб тамаев"),
        BotCommand(command="/location", description="спортики сват"),
        BotCommand(command="/edit_profile", description="переобулся тряпка"),
    ]
    await bot.set_my_commands(bot_commands)
    print("Комманды обновлены")


async def set_stickers():
    sql = """
        INSERT INTO stickerpack (name, category)
        VALUES ({name}, {category})
        """
    #

    # with open("static/sticker_packs.txt", "r") as file:
    #     sticker_packs = file.read().split("\n")
    # for pack_name in sticker_packs:
    #     stickers_in_pack = await bot.get_sticker_set(pack_name)
    #     stickers(pack_name) = stickers_in_pack
    #
    # for sticker_pack_name in sticker_packs:
    #     stickers_id(sticker_pack)

        # .extend(
        #     sticker.file_ida
        #     for sticker in sticker_pack.stickers
        # )

    # for name in sticker_packs:
    #     print(name)
    with SQLite() as db:
        db.cursor.execute(
            sql.format(
                name=...,
                category=...,
            )
        )
    # db.connection.commit()
#    with open("static/sticker_id.txt", "w") as file:
#        file.write("\n".join(stickers_id))
    print("Стикерпаки обновлены")


@dp.startup()
async def start():
    await setup_bot_commands()
    # await set_stickers()
    await create_tables()
    print("Бот запущен. ИДИТЕ НАХУЙ!")


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
