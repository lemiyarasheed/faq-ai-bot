# AI powered FAQ Bot with Open AI
import json
import os
from difflib import get_close_matches
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def load_faqs(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        data=json.load(file)
    return data['faqs']

def get_all_questions(faqs):
    return [faq['question'].lower() for faq in faqs]

def find_best_match(user_question,all_questions,cutoff=0.6):
    matches=get_close_matches(user_question.lower(),all_questions,n=1,cutoff=cutoff)
    return matches[0] if matches else None

def get_answer_from_question(question,faqs):
    for faq in faqs:
        if question.lower()==faq['question'].lower():
            return faq['answer']
    return None

def ask_ai(question):
    try:
        response=client.chat.completions.create(model='gpt-3.5-turbo',messages=[{"role":"system","content":"You are a helpful customer support assistant. Answer questions in 1 or 2 sentences"},
        {"role":"user","content":question}],max_tokens=150,temperature=0.7)
        return response.choices[0].message.content

    except Exception as e:
        return f"Sorry, I am having technical difficulties.Error: {e}"

def save_new_faq(question, answer, filepath='faq_data.json'):
    with open(filepath,'r',encoding='utf-8') as file:
        data=json.load(file)

    data['faqs'].append({"question":question,"answer":answer})

    with open(filepath,'w',encoding='utf-8') as file:
        json.dump(data,file,indent=2,ensure_ascii=False)

    print("Bot: I have learnt this answer for next time")

def main():
    faqs=load_faqs('faq_data.json')
    all_questions=get_all_questions(faqs)

    print("="*50)
    print("FAQ AI BOT")
    print("="*50)
    print(f"Loaded {len(faqs)} FAQs")
    print("I can answer from my FAQ list or use AI!")
    print("Type 'quit' to exit or 'learn' to teach me something new\n")

    while True:
        user_input=input("You:").strip()

        if user_input.lower()=='quit':
            print("Bot: Good Bye!")
            break

        if user_input.lower()=='learn':
            new_q=input("Bot: What question should I learn?")
            new_a=input("Bot: What is the answer?")
            save_new_faq(new_q,new_a)
            all_questions=get_all_questions(faqs)
            print("Bot ready for next question!\n")
            continue

        best_match=find_best_match(user_input,all_questions)
        if best_match:
            answer=get_answer_from_question(best_match,faqs)
            print(f"Bot: {answer}\n")

        else:
            ai_answer=ask_ai(user_input)
            print(f"Bot(AI):{ai_answer}\n")

            save_choice=input("Bot: Was this answer helpful? Save answer?(Yes/No)\n").lower()
            if save_choice=="yes":
                save_new_faq(user_input,ai_answer)
                faqs=load_faqs("faq_data.json")
                all_questions=get_all_questions(faqs)
                print("Bot: I will remember that for next time.\n")
            else:
                print("Bot: No problem! I will still try my best next time.\n")

if __name__=="__main__":
    main()














