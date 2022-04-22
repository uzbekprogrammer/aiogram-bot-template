from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from data.config import CHANNELS
from loader import dp, bot
from utils.misc import subscriotion


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    if state:
        await state.finish()
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}!\n"
                         f"Nodirabegim nomidagi Namangan viloyati axborot-kutubxona markazi rasmiy botiga xush kelibsiz. ",
                         reply_markup=ReplyKeyboardRemove())


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscriotion.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz ✅\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz ❌ \n"
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)