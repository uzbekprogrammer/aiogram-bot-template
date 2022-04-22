from aiogram import types

from data.config import ADMINS
from loader import dp, bot


@dp.message_handler(commands="quiz")
async def poll(msg: types.Message):
    ques = "Isming nima"
    ans1 = "Abdurahim"
    ans2 = "daskdj"
    ans3 = 'dasdsda'
    await bot.send_poll(chat_id=ADMINS[0], question=ques,options=[ans1, ans2, ans3], is_anonymous=True)
