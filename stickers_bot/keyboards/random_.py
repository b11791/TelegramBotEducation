from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

kb_1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='/go_joke 😂'), KeyboardButton(text='/give 🖕')],
        [KeyboardButton(text='/location 🆘')],
        [KeyboardButton(text='/picture 🐵')],
    ],
)


kb_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мем хуйня смотреть спанчбоба', url="https://rt.pornhub.com/"),
    InlineKeyboardButton(text='Новый анекдот', callback_data="new_anec")]
])
