from fastapi import FastAPI, HTTPException, Response
import random
import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api_key}"
mailtrap_url = "https://send.api.mailtrap.io/api/send"
from_email = "yelaman@demomailtrap.co"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Api-Token": os.getenv("MAILTRAP_API_KEY"),
}


def send_text_to_email(email: str, name: str, text: str):
    payload = {
        "to": [{"email": email, "name": name}],
        "from": {"email": from_email, "name": from_email},
        "subject": "Random Quote",
        "text": text,
    }

    response = requests.post(mailtrap_url, json=payload, headers=headers)

    if not response.json()["success"]:
        raise Exception("Email was not sent properly")


def generate_content(prompt: str) -> str:
    json = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url=gemini_url, json=json)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception("There was an error with Gemini API")

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]


app = FastAPI()

quotes = [
    "I'm not lazy, I'm on energy-saving mode.",
    "My bed is a magical place where I suddenly remember everything I forgot to do.",
    "I tried to be good, but then the bonfire was lit and there was wine.",
    "Adulting is soup, and I am a fork.",
    "I've got 99 problems, but a clean house isn't one.",
    "My brain has too many tabs open.",
    "I'm not a morning person. I'm a coffee person.",
    "Life is short. Smile while you still have teeth.",
    "I need a six-month vacation, twice a year.",
    "The only thing getting 'lit' tonight are my scented candles.",
    "I whisper 'what the heck' to myself at least 20 times a day.",
    "My therapist told me to embrace my flaws. I hugged myself.",
    "I'm not saying I'm Wonder Woman, I'm just saying no one has ever seen us in the same room together.",
    "My life is a series of embarrassing moments interrupted by snack breaks.",
    "I'm on a seafood diet. I see food, and I eat it.",
]


@app.get("/")
def get_random_quote():
    return {"quote": random.choice(quotes)}


@app.get("/send-to-email")
def send_to_email(email: str, name: str):
    try:
        send_text_to_email(
            email,
            name,
            generate_content(
                "Create short and funny quote. It should be about programming."
            ),
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return Response(status_code=200)
