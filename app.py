# app.py - Web interface for FAQ Bot using Streamlit

import json
import os
from difflib import get_close_matches
from openai import OpenAI
import streamlit as st

# Load API key from .env file
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Page configuration
st.set_page_config(
    page_title="AI FAQ Bot",
    page_icon="🤖",
    layout="centered"
)

# Title and description
st.title("🤖 AI-Powered FAQ Bot")
st.markdown("Ask me anything about our products or services!")

# Load FAQs from file
def load_faqs(file_path='faq_data.json'):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['faqs']

def extract_question_list(faqs):
    return [faq['question'].lower() for faq in faqs]

def find_best_match(user_question, question_list, cutoff=0.6):
    matches = get_close_matches(user_question.lower(), question_list, n=1, cutoff=cutoff)
    return matches[0] if matches else None

def get_answer_from_question(question, faqs):
    for faq in faqs:
        if faq['question'].lower() == question.lower():
            return faq['answer']
    return None

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant. Answer briefly in 1-2 sentences."},
                {"role": "user", "content": question}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I'm having technical difficulties. Error: {e}"

def save_new_faq(question, answer, file_path='faq_data.json'):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    data['faqs'].append({"question": question, "answer": answer})
    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

# Load FAQs into session state
if 'faqs' not in st.session_state:
    st.session_state.faqs = load_faqs()
    st.session_state.question_list = extract_question_list(st.session_state.faqs)
    st.session_state.messages = []
    st.session_state.last_question = None
    st.session_state.last_answer = None

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            best_match = find_best_match(user_input, st.session_state.question_list)
            
            if best_match:
                answer = get_answer_from_question(best_match, st.session_state.faqs)
                source = "📚 from FAQ database"
                full_response = f"{answer}\n\n*{source}*"
            else:
                answer = ask_ai(user_input)
                source = "🤖 from AI (OpenAI)"
                full_response = f"{answer}\n\n*{source}*"
                st.session_state.last_question = user_input
                st.session_state.last_answer = answer
            
            st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.rerun()

# Sidebar
with st.sidebar:
    st.markdown("## 📊 Bot Stats")
    st.metric("FAQs in Database", len(st.session_state.faqs))
    
    st.markdown("---")
    st.markdown("## 🧠 How It Works")
    st.markdown("""
    1. Tries to match your question with FAQ database
    2. If no match, asks OpenAI for help
    3. You can save new Q&As for next time
    """)
    
    # Save button (appears when AI answered)
    if st.session_state.last_question and st.session_state.last_answer:
        st.markdown("---")
        st.markdown("## 💾 Save This Answer")
        st.write(f"**Q:** {st.session_state.last_question}")
        st.write(f"**A:** {st.session_state.last_answer[:100]}...")
        
        if st.button("✅ Save to FAQ Database"):
            save_new_faq(st.session_state.last_question, st.session_state.last_answer)
            st.session_state.faqs = load_faqs()
            st.session_state.question_list = extract_question_list(st.session_state.faqs)
            st.session_state.last_question = None
            st.session_state.last_answer = None
            st.success("✅ Saved! I'll remember this for next time.")
            st.rerun()
    
    st.markdown("---")
    st.markdown("## 🗑️ Clear Chat")
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()