from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Application, filters



TOKEN = '5513479285:AAG4SGngQcnQycQYBkj59noDkgSSYDOLOyA'


async def handle_message(update: Update, context: CallbackContext):
    message = update.message.text
    
    if message == "Hello":
        await update.message.reply_text("Hello there!")
    elif message == "I love you":
        await update.message.reply_text("Who the hell are you?")
    else:
        await update.message.reply_text("What are you saying?")


if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling()

