from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    if state:
        await state.finish()
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}!\n"
                         f"Nodirabegim nomidagi Namangan viloyati axborot-kutubxona markazi rasmiy botiga xush kelibsiz. ")

