from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery

import random
import aiogram

from stickers_bot.create_bot import bot
from stickers_bot.db import SQLite
from stickers_bot.keyboards.random_ import kb_1, kb_2


random_router = Router()


@random_router.message(Command("start"))
async def startuem(message: aiogram.types.Message):
    await message.answer(text='HI', reply_markup=kb_1)


@random_router.message(Command("go_joke"))
async def joke(message: aiogram.types.Message):

    await message.answer(text='Анекдот для поднятия кондиций:'
                              '\n Ебет один клоун другого, а режиссер думает: «Блять, что-то съемки "Оно 3" пошли не'
                              ' по плану», но продолжает снимать', reply_markup=kb_2)


@random_router.message(Command("give"))
async def sticker(message: aiogram.types.Message):
    with open("static/sticker_packs.txt") as file:
        sticker_packs = file.read().split("\n")
    full_stickers = {}
    for pack_name in sticker_packs:
        with SQLite() as db:
            pack_id = db.cursor.execute(
                f"""
                INSERT INTO stickepacks (name, category_id)
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
            with SQLite() as db:
                db.cursor.execute(sql)
                db.connection.commit()




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


@random_router.message()
async def all(message: aiogram.types.Message):
    print(await bot.get_sticker_set("legalogu"))
    # await message.answer(text=f'Я тебя не понял, но вот твой чат id {message.chat.id}')
    # if message.text == "Пися":
    #     await bot.send_message(
    #         chat_id=537932720,
    #         text='А Денис балуется',
    #     )`


@random_router.callback_query()
async def take_callback(callback: CallbackQuery):
    if callback.data == "new_anec":
        await callback.answer(show_alert=True, text="Ты чё сигма")
        await joke(message=callback.message)



# Пример динамической клавиатуры
# kb_1 = ReplyKeyboardMarkup(
#         resize_keyboard=True,
#         keyboard=[
#             [KeyboardButton(text=i["name"])
#              for i in categories
#         ],
#     )