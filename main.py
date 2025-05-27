from fastapi import FastAPI, Request
import asyncio
from aiogram import Bot
import os

# Конфигурация из переменных среды
API_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=API_TOKEN)
app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    signal = data.get("signal")
    tp = data.get("tp")
    sl = data.get("sl")
    timeframe = data.get("timeframe")

    if signal:
        text = (
            f"📡 *AI Signal*\n\n"
            f"🔔 Signal: *{signal}*\n"
            f"🕒 Timeframe: `{timeframe}`\n"
            f"🎯 Take Profit: `{tp}`\n"
            f"🛑 Stop Loss: `{sl}`"
        )
        await bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")
    return {"status": "ok"}
