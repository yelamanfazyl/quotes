import requests
import os
from dotenv import load_dotenv
import base64

load_dotenv()

url = "https://send.api.mailtrap.io/api/send"

payload = {
    "to": [{"email": "fazil.el2003@gmail.com", "name": "Yelaman"}],
    "from": {"email": "yelaman@demomailtrap.co", "name": "Yelaman"},
    "subject": "Hello World",
    "text": "Hello nfactorial!",
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Api-Token": os.getenv("MAILTRAP_API_KEY"),
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
