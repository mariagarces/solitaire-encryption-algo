from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from main import *

app = FastAPI()
main = Main()

@app.post("/message")
def load_message(message):
    main.load_message(message)
    return {"response": "Message loaded"}

@app.get("/cards")
def get_key_cards():
    cards = main.get_key_cards()
    return {cards}

@app.get("/message/encrypt")
def get_encrypted_message():
    encrypt_message = main.get_encrypted_message()
    return {encrypt_message}
