from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Body
from .main import *

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://solitaire-encryption.vercel.app/",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main = Main()

@app.post("/message")
def load_message(message: str = Body(..., embed=True)):
    main.load_message(message)
    return {"response": "Message loaded"}

@app.get("/cards")
def get_key_cards():
    cards = main.get_key_cards()
    return cards

@app.get("/cards/shuffle")
def get_key_cards_shuffle():
    cards = main.get_key_cards_shuffle()
    return cards

@app.get("/cards/current-state")
def get_current_state_cards():
    cards = main.get_current_state_cards()
    return cards

@app.get("/message/encrypt")
def get_encrypted_message():
    encrypt_message = main.get_encrypted_message()
    return encrypt_message

@app.get("/message/decrypt")
def get_decrypted_message():
    decrypt_message = main.get_decrypted_message()
    return decrypt_message

@app.post("/load-cards")
def load_cards(cards: list = Body(..., embed=True)):
    main.load_cards(cards)
    return {"response": "Cards loaded"}