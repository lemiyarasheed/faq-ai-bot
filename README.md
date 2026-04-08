# 🤖 AI-Powered FAQ Bot

A smart FAQ chatbot that answers customer questions using **fuzzy matching** AND **OpenAI**. Built step by step as a portfolio project for AI/Automation roles.

## 🚀 Live Features

| Version | Features | Status |
|---------|----------|--------|
| **v1** | Basic keyword matching | ✅ Complete |
| **v2** | Fuzzy matching (handles typos) | ✅ Complete |
| **v3** | OpenAI integration + learning | ✅ Complete |
| **v4** | Web interface (Streamlit) | 🔜 Coming soon |

## 🎯 What This Bot Can Do

- ✅ Answer questions from its FAQ database (instant)
- ✅ Handle typos like `"reset my passwerd"` using fuzzy matching
- ✅ Answer ANY question using OpenAI (fallback)
- ✅ Learn new answers and save them for next time
- ✅ Remember what it learned (persistent storage)

## 🛠️ Technologies Used

- Python 3.9+
- OpenAI API (GPT-3.5-turbo)
- difflib (fuzzy string matching)
- JSON (data storage)
- python-dotenv (environment variables)
- Git & GitHub

## 📋 How to Run

```bash
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

# 5. Set up your OpenAI API key
# Create a .env file with:
OPENAI_API_KEY=your-key-here

# 6. Run the bot
python bot_v3.py
