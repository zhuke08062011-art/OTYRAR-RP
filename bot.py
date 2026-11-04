import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "♕ OTYRAR RP-ға қош келдіңіз! ♕\n"
        "Біздің ресми арна: @otyrarkzt"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "OTYRAR RP — ресми бот.\n"
        "Командалар: /start, /info"
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN орнатылмаған!")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    print("OTYRAR RP боты іске қосылды!")
    app.run_polling()

if __name__ == "__main__":
    main()
