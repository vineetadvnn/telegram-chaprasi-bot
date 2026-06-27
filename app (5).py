import os
import telebot
from groq import Groq

# Setup
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

# Clear any existing webhook to avoid 409 conflicts
bot.remove_webhook()

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

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    user_text = message.text

    if user_id not in conversations:
        conversations[user_id] = []

    conversations[user_id].append({
        "role": "user",
        "content": user_text
    })

    # Keep last 10 messages
    history = conversations[user_id][-10:]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
        max_tokens=500
    )

    reply = response.choices[0].message.content

    conversations[user_id].append({
        "role": "assistant",
        "content": reply
    })

    bot.reply_to(message, reply)

print("Bot is running...")
bot.infinity_polling(allowed_updates=["message"])
