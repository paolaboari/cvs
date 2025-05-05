import ollama

from ollama import chat
from ollama import ChatResponse

while True:
    
  prompt = input("Ciao, sono il tuo ChatBot personale. Cosa vuoi chiedermi? ")

  if prompt == "Exit":
    break

  response: ChatResponse = chat(model='llama3.2:1b', messages=[
    {
      'role': 'user',
      'content': prompt,
    },
  ], format="json")
  print(response['message']['content'])

print("Grazie, alla prossima!")