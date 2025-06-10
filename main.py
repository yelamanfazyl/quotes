from fastapi import FastAPI
import random

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
