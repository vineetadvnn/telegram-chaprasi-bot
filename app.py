import os
import telebot
from google import genai
from google.genai import types

# Setup
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

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

    conversations[user_id].append(
        types.Content(role="user", parts=[types.Part(text=user_text)])
    )

    # Keep last 10 messages
    history = conversations[user_id][-10:]

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
        contents=history
    )

    reply = response.text

    conversations[user_id].append(
        types.Content(role="model", parts=[types.Part(text=reply)])
    )

    bot.reply_to(message, reply)

print("Bot is running...")
bot.infinity_polling()
