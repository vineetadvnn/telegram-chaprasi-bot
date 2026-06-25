import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Configure Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """You are a personal productivity assistant on Telegram.
You help with:
- Breaking down tasks and setting priorities
- Drafting emails and messages
- Summarising notes or meeting points
- To-do lists and reminders
- Reviewing and improving written content
- Quick research questions

Keep replies concise and practical — this is a messaging app.
Use bullet points and short sentences. Be direct and friendly."""

# Store chat sessions per user
chat_sessions = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    # Create or reuse chat session (keeps conversation memory)
    if user_id not in chat_sessions:
        chat_sessions[user_id] = model.start_chat(history=[])

    chat = chat_sessions[user_id]

    # Prepend system context on first message
    if len(chat.history) == 0:
        full_message = f"{SYSTEM_PROMPT}\n\nUser: {user_message}"
    else:
        full_message = user_message

    response = chat.send_message(full_message)
    await update.message.reply_text(response.text)

if __name__ == "__main__":
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
