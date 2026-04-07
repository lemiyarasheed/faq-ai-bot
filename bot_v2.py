import json
from difflib import get_close_matches

def load_faqs(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        data=json.load(file)
    return data['faqs']

def get_all_questions(faqs):
    return [faq['question'].lower() for faq in faqs]

def find_best_match(user_question,all_questions,cutoff=0.6):
    matches=get_close_matches(user_question,all_questions,n=1,cutoff=cutoff)
    return matches[0] if matches else None

def get_answer_from_question(question,faqs):
    for faq in faqs:
        if faq['question'].lower()==question.lower():
            return faq['answer']
    return None

def main():
    faqs=load_faqs('faq_data.json')
    all_questions=get_all_questions(faqs)
    print('='*50)
    print('FAQ Bot with Fuzzy Matching')
    print('='*50)
    print(f"Loaded {len(faqs)} FAQs")
    print("I can handle typos and similar questions!")
    print("Type 'quit' to exit\n")

    while True:
        user_input=input("You:").strip()

        if user_input.lower()=="quit":
            print("GoodBye!")
            break

        best_match=find_best_match(user_input,all_questions)
        if best_match:
            answer=get_answer_from_question(best_match,faqs)
            print(f"Bot:{answer}\n")
        else:
            print("Bot: I could not find a good match. Please rephrase")

if __name__=="__main__":
    main()




