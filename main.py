import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from utils import load_memory, save_memory, init_db
from replies import get_priyanka_reply

TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    print("❌ ERROR: TOKEN not found in Railway Variables!")
    exit()

memory = load_memory()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! मैं Priyanka हूँ ❤️, कैसे हो?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply = get_priyanka_reply(user_text, memory)
    await update.message.reply_text(reply)
    save_memory(memory)

async def show_memory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    last_msgs = memory["short_term"][-5:]
    msg = ""
    for item in last_msgs:
        msg += f"You: {item['user']}\nPriyanka: {item['reply']}\n\n"
    await update.message.reply_text(msg if msg else "Memory empty ❤️")

async def forget(update: Update, context: ContextTypes.DEFAULT_TYPE):
    memory["short_term"] = []
    save_memory(memory)
    await update.message.reply_text("Short-term memory clear हो गया ❤️")

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn, cursor = init_db()
    cursor.execute("DELETE FROM memory")
    conn.commit()
    conn.close()
    await update.message.reply_text("Long-term memory reset हो गया ❤️")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("memory", show_memory))
app.add_handler(CommandHandler("forget", forget))
app.add_handler(CommandHandler("reset", reset))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("🚀 Bot Starting...")
app.run_polling()
