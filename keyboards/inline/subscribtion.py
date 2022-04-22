from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='NAMANGAN AKM', url='https://t.me/namanganakm')
    ],
                     [
        InlineKeyboardButton(text="Obunani tekshirish",callback_data="check_subs")
    ]]
)