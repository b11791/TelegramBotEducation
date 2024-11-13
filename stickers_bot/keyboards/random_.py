from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from unicodedata import category

from stickers_bot.db import SQLite
from stickers_bot.funcs import design_buttons

kb_1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='/go_joke 😂'), KeyboardButton(text='/stickers')],
        [KeyboardButton(text='/location 🆘'), KeyboardButton(text='/picture 🐵')],
    ],
)


kb_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мем хуйня смотреть спанчбоба', url="https://rt.pornhub.com/"),
    InlineKeyboardButton(text='Новый анекдот', callback_data="new_anec")]
])

def get_stickers_keyboard() -> InlineKeyboardMarkup:
    with SQLite() as db:
        result = db.cursor.execute("SELECT * from category").fetchall()

    buttons = design_buttons([
        InlineKeyboardButton(
            text=category["name"],
            callback_data=f"category_{category['id']}"
        )
        for category in result
    ])
    kb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=buttons,
    )

    return kb

kb3 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Вступить в Вагнер")],
    ],
)
