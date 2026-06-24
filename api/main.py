import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.environ["TELEGRAM_TOKEN"]

# ساخت اپلیکیشن تلگرام
tg_app = Application.builder().token(TOKEN).build()

# هندلر پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Hello":
        await update.message.reply_text("Hello there!")
    elif text == "I love you":
        await update.message.reply_text("Who are you exactly?")
    else:
        await update.message.reply_text("What are you saying?")

tg_app.add_handler(MessageHandler(filters.TEXT, handle_message))

# ساخت FastAPI
app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, tg_app.bot)

    await tg_app.initialize()
    await tg_app.process_update(update)

    return {"ok": True}
