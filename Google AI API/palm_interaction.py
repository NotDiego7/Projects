# # --------------------- Google Image Recognition Attempt --------------------- #
# from google import generativeai
# import os, time


# PALM_KEY = os.getenv('PALM_API_KEY')


# image_path = f'https://i.insider.com/6215411745889c0019d1c946?width=1000&format=jpeg&auto=webp&t={time.time()}' # TODO: Change

# # # Open image
# # with open(image_path, 'rb') as image:
# #     image_bytes = image.read()


# # # Encode image bytes to Base64 string
# # encoded_image = base64.b64encode(image_bytes).decode('utf-8')


# prompt = f"Who was the first president of the US of A and was he a slave holder?"


# generativeai.configure(api_key= PALM_KEY)


# PaLMs_reply = generativeai.chat(prompt= [prompt])


# print(PaLMs_reply.last)


# ------------------------- Google Generative AI Chat ------------------------ #
from google import generativeai
import os, time

PALM_KEY = os.getenv('PALM_API_KEY')

prompt = ""


generativeai.configure(api_key= PALM_KEY)


PaLMs_reply = generativeai.chat(prompt= [prompt])


print(PaLMs_reply.last)