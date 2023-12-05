# ------------------------- Google Generative AI Chat ------------------------ #

from google import generativeai
import os, time

PALM_KEY = os.getenv('PALM_API_KEY')

prompt = (input('Adelante... '))


generativeai.configure(api_key= PALM_KEY)


PaLMs_reply = generativeai.chat(prompt= [prompt])


print(PaLMs_reply.last)