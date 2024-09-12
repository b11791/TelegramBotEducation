import json

import aiogram
import random

from aiogram.types import BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '7442995070:AAGxh9m7LBzPly6kqTFq58w-vrtNdvP2qMk'

pictures = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


jokes = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


sticker_packs = [
    "CheapChocolateChicken_by_fStikBot",
    "Coconutyk_by_fStikBot",
    "rostikgay",
    "bcgqindc_by_stickrubot",
    "heavysu1te_by_fStikBot",
    "goluboj5368",
    "Lyagushki1936",
    "pk_1428111_by_Ctikerubot",
    "YYPVVADFJS_by_stikeri_stikeri_bot",
    "Yellowboi",
    "Ura527",
    "JANCDOAXPM_by_stikeri_stikeri_bot",
    "hentaqqq_by_fStikBot",
    "Pip228_by_fStikBot",
    "katzenmann1337",
    "bolshe_stikov_c3d45_by_MoiStikiBot",
    "simka_moment_by_fStikBot",
    "Ex_da",
    "whycantikissallthekitties",
    "stickersfailed",
    "shlendrii_by_fStikBot",
    "Govno_obami",
    "yoneegas_by_fStikBot",
    "KomaruRofls",
    "CSNAVI",
    "KiTjpg",
    "HannahAestheticallyowo",
    "l1nkyspastinginc_by_fStikBot",
    "cheatcomm_by_fStikBot",
    "xentach_by_fStikBot",
    "Tresxxx",
]

bot = aiogram.Bot(TOKEN)
dp = aiogram.Dispatcher(bot)
stickers_id = []


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1, b2, b3, b4 = (KeyboardButton('/go_joke 😂'),
                  KeyboardButton('/give 🖕'),
                  KeyboardButton('/location 🆘'),
                  KeyboardButton('/picture 🐵'))
kb.add(b1, b2, b3, b4)

@dp.message_handler(commands=["start"])
async def echo(message: aiogram.types.Message):
    await message.answer(text='HI', reply_markup=kb)


@dp.message_handler(commands=["go_joke"])
async def echo(message: aiogram.types.Message):
    await message.answer(text='Анекдот для поднятия кондиций:'
                              '\n Ебет один клоун другого, а режиссер думает: «Блять, что-то съемки "Оно 3" пошли не'
                              ' по плану», но продолжает снимать')


@dp.message_handler(commands=["give"])
async def echo(message: aiogram.types.Message):
    await bot.send_sticker(message.from_user.id, sticker=random.choice(stickers_id), reply_markup=kb)


@dp.message_handler(commands=["location"])
async def echo(message: aiogram.types.Message):
    await bot.send_location(message.from_user.id, latitude=random.randint(1, 90),
                            longitude=random.randint(1, 180), reply_markup=kb)


@dp.message_handler(commands=["picture"])
async def echo(message: aiogram.types.Message):
    await bot.send_photo(message.from_user.id,
                         "https://avatars.dzeninfra.ru/get-zen_doc/1594475/pub_5ceb78dcae6fed00b3fbe21f_5ceb7e82ae6fed00b3fbe27e/scale_1200",
                         reply_markup=kb)


@dp.message_handler()
async def all(message: aiogram.types.Message):
    print(await bot.get_sticker_set("legalogu"))
    # await message.answer(text=f'Я тебя не понял, но вот твой чат id {message.chat.id}')
    # if message.text == "Пися":
    #     await bot.send_message(
    #         chat_id=537932720,
    #         text='А Денис балуется',
    #     )`


async def setup_bot_commands():
    bot_commands = [
        BotCommand(command="/go_joke", description="анекдот для поднятия кондиций"),
        BotCommand(command="/give", description="рандомная херь"),
        BotCommand(command="/start", description="начать заново"),
        BotCommand(command="/picture", description="асхаб тамаев"),
        BotCommand(command="/location", description="спортики сват"),
    ]
    await bot.set_my_commands(bot_commands)


async def set_stickers():
    for sticker_pack_name in sticker_packs:
        sticker_pack = await bot.get_sticker_set(sticker_pack_name)
        stickers_id.extend(
            sticker.file_id
            for sticker in sticker_pack.stickers
        )


async def start(dp):
    await setup_bot_commands()
    await set_stickers()


if __name__ == "__main__":
    aiogram.executor.start_polling(dp, skip_updates=False, on_startup=start)