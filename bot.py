import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Elion Bot! 🚀\n\n"
        "Your digital assistant is now active.\n"
        "Type /help to see what I can do."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ELION BOT COMMANDS\n\n"
        "/start - Start the bot\n"
        "/help - Get help\n"
        "/about - About Elion"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Elion is a growing digital project. 🌍\n"
        "Stay connected for updates!"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Thanks for messaging Elion Bot! 🚀"
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing!")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Elion Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
