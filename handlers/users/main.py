from aiogram import types

from loader import dp



def poll(bot, update):
    options = ['a', 'b']
    bot.send_poll(update.message.chat_id, "please choose option a or    b: ",options)
    updater.dispatcher.add_handler(CommandHandler('set', poll))
    updater.start_polling()