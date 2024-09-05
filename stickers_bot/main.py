import json

import aiogram
import random

from aiogram.types import BotCommand

TOKEN = '7442995070:AAGxh9m7LBzPly6kqTFq58w-vrtNdvP2qMk'

sticker_packs = [
    "CheapChocolateChicken_by_fStikBot",
    "Coconutyk_by_fStikBot",
    "rostikgay",
]

bot = aiogram.Bot(TOKEN)
dp = aiogram.Dispatcher(bot)
stickers_id = []

@dp.message_handler(commands=["go_joke"])
async def echo(message: aiogram.types.Message):
    await message.answer(text='Ку\n Када месячные\n Анекдот для поднятия кондиций:'
                              '\n Ебет один клоун другого, а режиссер думает: «Блять, что-то съемки "Оно 3" пошли не'
                              ' по плану», но продолжает снимать')


@dp.message_handler(commands=["give"])
async def echo(message: aiogram.types.Message):
    await bot.send_sticker(message.from_user.id, sticker=random.choice(stickers_id))


@dp.message_handler()
async def all(message: aiogram.types.Message):
    print(await bot.get_sticker_set("legalogu"))
    # await message.answer(text=f'Я тебя не понял, но вот твой чат id {message.chat.id}')
    # if message.text == "Пися":
    #     await bot.send_message(
    #         chat_id=537932720,
    #         text='А Денис балуется',
    #     )


async def setup_bot_commands():
    bot_commands = [
        BotCommand(command="/go_joke", description="анекдот для поднятия кондиций"),
        BotCommand(command="/give", description="рандомная херь"),
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
    aiogram.executor.start_polling(dp, skip_updates=True, on_startup=start)