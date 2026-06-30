# 🤖 My Chaprasi — Personal Productivity Telegram Bot
Fully free, running 24/7. Powered by Groq (Llama 3.3 70B) + Telegram + Railway.

---

## ✅ Final Working Stack

| Part | Tool | Cost |
|---|---|---|
| AI brain | Groq API (Llama 3.3 70B) | Free (14,400 requests/day) |
| Bot platform | Telegram Bot API | Free forever |
| Hosting | Railway (Background Worker) | Free ($5 trial credit/month) |
| Code storage | GitHub | Free |

---

## 📁 Files in this repo

- `app.py` — the bot logic
- `requirements.txt` — Python dependencies (`pyTelegramBotAPI`, `groq`)

---

## STEP 1 — Create Your Telegram Bot

1. Open Telegram → search **@BotFather** → tap **Start**
2. Send: `/newbot`
3. Give it a name (e.g. `My Chaprasi`)
4. Give it a username ending in `bot` (e.g. `mychaprasibot`)
5. Copy the **token** BotFather gives you (looks like `7123456789:AAFxxxxx`)

---

## STEP 2 — Get a Free Groq API Key

1. Go to **console.groq.com** → sign up (free)
2. Go to **API Keys** → **Create API Key**
3. Copy the key (starts with `gsk_...`)

> Free tier = 14,400 requests/day — more than enough for personal use.

---

## STEP 3 — Upload to GitHub

1. Go to **github.com** → create a new repository (e.g. `telegram-chaprasi-bot`)
2. Upload `app.py` and `requirements.txt`

---

## STEP 4 — Deploy on Railway

1. Go to **railway.app** → sign up with GitHub
2. **New Project → Deploy from GitHub repo** → select your repo
3. Railway auto-detects Python — no special build/start commands needed
4. Go to your service → **Variables** tab → add:

   | Key | Value |
   |---|---|
   | `TELEGRAM_BOT_TOKEN` | token from Step 1 |
   | `GROQ_API_KEY` | key from Step 2 |

5. Railway deploys automatically. Check **Deployments → View Logs** — you should see:
   ```
   Bot is running...
   ```

---

## ✅ Test It

Open Telegram → search your bot's username → tap **Start** or send `/start`.

**Try these:**
- "Break down this task: prepare for a job interview next week"
- "Draft a follow-up message to a recruiter I met yesterday"
- "Summarise this: [paste any text]"
- "I have 2 hours free, help me prioritise my day"
- "Review this email and make it more professional: [paste email]"

---

## 🔧 Customise

Edit the `SYSTEM_PROMPT` in `app.py` to change the bot's personality, tone, or focus area.

---

## 🛠️ Troubleshooting

**Bot doesn't reply / "409 Conflict" in logs**
→ Means more than one instance is polling Telegram at once. Fix: revoke and regenerate your bot token via BotFather (`/mybots → API Token → Revoke`), then update `TELEGRAM_BOT_TOKEN` on Railway.

**"429 RESOURCE_EXHAUSTED" or quota errors**
→ Your AI provider's free daily limit is used up. With Groq this is rare (14,400/day), but if it happens, wait 24 hours or create a new API key.

**Deployment fails during build**
→ Check Railway's **Build** tab for the exact error — usually a `requirements.txt` version conflict. Keep dependencies minimal and avoid pinning unrelated packages.

**Bot replies once then stops**
→ Check Railway logs for crashes. Railway auto-restarts on crash, but repeated crash loops can trigger rate limits — let it stabilise for a few minutes.

---

## 📝 Notes

- Conversation memory is in-session only (resets if the server restarts)
- Railway free tier gives ~$5/month credit — a lightweight polling bot like this uses a small fraction of that
- To reset the bot's memory, restart the service on Railway
