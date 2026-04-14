---
title: AI FAQ Bot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.35.0"
app_file: app.py
pinned: false
---
# 🤖 AI-Powered FAQ Bot
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-deployed-link-here)

A smart FAQ chatbot that answers customer questions using **fuzzy matching** AND **OpenAI**. Built as a portfolio project for AI/Automation roles.

---

## 🚀 Features

| Version | Features | Status |
|---------|----------|--------|
| **v1** | Basic keyword matching | ✅ Complete |
| **v2** | Fuzzy matching (handles typos) | ✅ Complete |
| **v3** | OpenAI integration + learning | ✅ Complete |
| **v4** | Web interface (Streamlit) | ✅ Complete |
- [ ] Deploy to cloud (Hugging Face Spaces)
- [ ] Document processing pipeline

## 🌐 Web Interface

The bot now has a **beautiful web interface** built with Streamlit:

- 💬 Chat-based interaction
- 📚 Shows whether answers come from FAQ or AI
- 💾 Save new Q&As with one click
- 📊 Real-time stats in the sidebar

### Screenshot

![FAQ Bot Web Interface](screenshot.png)

*Run locally with `streamlit run app.py`*

### What the Bot Can Do

- ✅ Answer questions from its FAQ database (instant)
- ✅ Handle typos like `"reset my passwerd"` using fuzzy matching
- ✅ Answer ANY question using OpenAI (fallback)
- ✅ Learn new answers and save them for next time
- ✅ Remember what it learned (persistent JSON storage)

---

## 🛠️ Technologies Used

- Python 3.9+
- OpenAI API (GPT-3.5-turbo)
- difflib (fuzzy string matching)
- JSON (data storage)
- python-dotenv (environment variables)
- Git & GitHub

---

## 🔑 API Key Required

This bot uses OpenAI's API. To run it yourself:

1. Sign up at [OpenAI Platform](https://platform.openai.com)
2. Go to **API Keys** → **Create new secret key**
3. Add **$5-10 credit** (very cheap, ~$0.002 per question)
4. Create a `.env` file in the project folder with:
OPENAI_API_KEY=your-key-here


> ⚠️ **Never commit your `.env` file to GitHub.** It's already in `.gitignore`.

---

## 📋 How to Run

```bash
### Option 1

# 1. Clone the repository
git clone https://github.com/lemiyarasheed/faq-ai-bot.git
cd faq-ai-bot

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file with your OpenAI API key
# (see API Key Required section above)

# 6. Run the bot
python bot_v3.py

### Option 2: Web Interface (Recommended)

```bash
streamlit run app.py

Then open http://localhost:8501 in your browser.

==================================================
🤖 AI-POWERED FAQ BOT
==================================================
Loaded 4 FAQs from memory
I can answer from my FAQ list OR use AI!
Type 'quit' to exit, 'learn' to teach me something

You: reset my passwerd
Bot (from FAQ): Click 'Forgot Password' on the login page.

You: do you ship to Dubai?
Bot: Let me think... 🤔
Bot (AI): Yes, we ship to over 50 countries including UAE. Delivery takes 5-10 business days.

Bot: Was this answer helpful? Save answer? (yes/no)
You: yes
📚 Bot: I've learned this answer for next time!

You: do you ship to Dubai?
Bot (from FAQ): Yes, we ship to over 50 countries including UAE. Delivery takes 5-10 business days.

You: quit
Bot: Goodbye! 👋


---

## ✅ How to Add It to GitHub

### Method 1: Directly on GitHub (Easiest)

1. Go to: `https://github.com/lemiyarasheed/faq-ai-bot`
2. Click on `README.md`
3. Click the **pencil icon (✏️)**
4. **Delete everything** in the file
5. **Copy and paste** the entire README above
6. Scroll down and click **"Commit changes"**

### Method 2: Local + Push

```bash
# 1. Open README.md in your editor
# 2. Replace with the content above
# 3. Save

# 4. Pull latest (just in case)
git pull origin main

# 5. Add and commit
git add README.md
git commit -m "Final README with API instructions, sample conversation, author, and status"

# 6. Push
git push origin main

Security Note
The .env file containing your API key is excluded from GitHub via .gitignore

Never commit secrets to version control

If you accidentally expose a key, revoke it immediately on OpenAI's dashboard

📈 What I Learned Building This
File I/O and JSON handling in Python

Fuzzy string matching with difflib

API integration (OpenAI)

Environment variables for secrets

Git workflow (commit, push, pull, merge, merge conflicts)

Virtual environments for dependency management

Debugging real errors (TypeError, variable naming, exposed keys)

👩‍💻 Author
Lemiya Rasheed
AI & Automation Specialist | Operations + AI Hybrid
GitHub | LinkedIn

*10+ years in operations, systems, and automation. Currently building AI automation startup (Noova).*

📅 Status
Item	Info
Current version	v3 (AI-powered)
Last updated	April 10, 2026
Status	✅ Working, production-ready
Next milestone	Web interface with Streamlit
Known issues	None
🚀 Coming Soon
Web interface with Streamlit

Document processing pipeline (PDF, DOCX)

SQL database integration

Deployment to cloud (Hugging Face Spaces)

📄 License
This project is open source for portfolio purposes. Feel free to use, learn from, and modify.

