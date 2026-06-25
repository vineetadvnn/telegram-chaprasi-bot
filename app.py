import os
from google import genai
from google.genai import types
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Configure Gemini
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

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

# Store conversation history per user
conversations = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    if user_id not in conversations:
        conversations[user_id] = []

    # Add user message to history
    conversations[user_id].append(
        types.Content(role="user", parts=[types.Part(text=user_message)])
    )

    # Keep last 10 exchanges to avoid token overload
    history = conversations[user_id][-10:]

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
        contents=history
    )

    reply_text = response.text

    # Add assistant reply to history
    conversations[user_id].append(
        types.Content(role="model", parts=[types.Part(text=reply_text)])
    )

    await update.message.reply_text(reply_text)

if __name__ == "__main__":
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
