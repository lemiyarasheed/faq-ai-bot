# 🤖 FAQ Bot with AI Capabilities

A smart FAQ chatbot that answers customer questions. Built step by step for learning and portfolio.

## 🚀 Features

### Version 1 (Basic)
- Loads FAQs from JSON file
- Simple keyword matching
- Case-insensitive search

### Version 2 (Current)
- ✅ **Fuzzy matching** for typos and variations
- ✅ Handles questions like "reset my passwerd" (typo)
- ✅ Understands word order differences
- ✅ Similarity threshold (60% match)

### Version 3 (Coming Soon)
- OpenAI API integration
- Answers questions not in FAQ
- "Learn and save" feature

## 📋 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/lemiyarasheed/faq-ai-bot.git

# 2. Navigate to folder
cd faq-ai-bot

# 3. Create virtual environment
python -m venv venv

# 4. Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 5. Run the bot
python bot_v2.py
