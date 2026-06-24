import json
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

import os

TOKEN = os.environ["TELEGRAM_TOKEN"]

app = Application.builder().token(TOKEN).build()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Hello":
        await update.message.reply_text("Hello there!")
    elif text == "I love you":
        await update.message.reply_text("Who the hell are you?")
    else:
        await update.message.reply_text("What are you saying?")

app.add_handler(MessageHandler(filters.TEXT, handle_message))


async def handler(request):
    body = await request.json()
    update = Update.de_json(body, app.bot)

    await app.initialize()
    await app.process_update(update)

    return {
        "statusCode": 200,
        "body": json.dumps({"ok": True})
    }
