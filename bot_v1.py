import json

def load_faqs(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
          data=json.load(file)
    return data['faqs']

def find_answer(question,faqs):
    question_lower=question.lower()
    
    for faq in faqs:
       if question_lower in faq['question'].lower():
               return faq['answer']
    return None


def main():
 faqs=load_faqs('faq_data.json')
 print(f"Loaded {len(faqs)} FAQs")
 print("FAQ Bot: Ask me a question! (type 'quit' to exit)\n")
 
 while(True):

  user_input=input("You:").strip()
 
  if user_input.lower()=='quit':
   print("Bot:GoodBye!")
   break
  answer=find_answer(user_input,faqs)
  if answer:
   print(f"Bot:{answer}\n")
  else:
   print("I don't have an answer for that\n")

if __name__=="__main__":
  main()