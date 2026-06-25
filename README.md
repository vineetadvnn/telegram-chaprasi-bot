# 🤖 Personal Productivity Telegram Bot
Completely free. No credit card. Powered by Google Gemini AI.

---

## What You Need
- Telegram account (you have this)
- Google account (for Gemini API)
- GitHub account (free)
- Render account (free)

---

## STEP 1 — Create Your Telegram Bot (2 mins)

1. Open Telegram → search for **@BotFather**
2. Send: `/newbot`
3. Give it a name e.g. `Vineeta Assistant`
4. Give it a username e.g. `vineeta_productivity_bot`
5. BotFather sends you a **token** — copy it (looks like `123456:ABCdef...`)

---

## STEP 2 — Get Free Gemini API Key (2 mins)

1. Go to https://aistudio.google.com
2. Sign in with Google
3. Click **Get API Key** → Create API key
4. Copy the key

Free tier = **1,500 requests/day** — more than enough for personal use.

---

## STEP 3 — Upload to GitHub (3 mins)

1. Go to https://github.com → New repository
2. Name it: `telegram-productivity-bot`
3. Upload these 3 files: `app.py`, `requirements.txt`, `render.yaml`

---

## STEP 4 — Deploy on Render (5 mins)

1. Go to https://render.com → Sign up with GitHub
2. Click **New → Background Worker** (important — NOT Web Service)
3. Connect your `telegram-productivity-bot` repo
4. Settings:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python app.py`
5. Add two Environment Variables:
   - `TELEGRAM_BOT_TOKEN` = your token from Step 1
   - `GEMINI_API_KEY` = your key from Step 2
6. Click **Deploy**

---

## ✅ Done! Test It

1. Open Telegram → search your bot by username
2. Send any message — it will reply instantly

**Try these:**
- "Break down this task: prepare for a job interview next week"
- "Draft a follow-up message to a recruiter I met yesterday"
- "Summarise this: [paste any text]"
- "I have 2 hours free, help me prioritise my day"
- "Review this email and make it more professional: [paste email]"

---

## 💡 Tips
- The bot remembers your conversation until the server restarts
- To reset memory, restart the Render service
- To change the bot's personality, edit `SYSTEM_PROMPT` in `app.py`
- Render free tier keeps it running 24/7 for background workers
