import logging

from telegram.ext import Updater, CommandHandler


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


updater = Updater(
    token='1394630757:AAEp9iWkfngy4dn61fpi_GeVjXOu3t7yk30'
    )
dispatcher = updater.dispatcher


def start(upd, ctx):
    ctx.bot.send_message(
        chat_id=upd.effective_chat.id,
        text="Hello World!",
    )


start_handler = CommandHandler(
    'start', start
)

dispatcher.add_handler(start_handler)

updater.start_polling()