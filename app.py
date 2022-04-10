from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# from data import wizards, spells, spell_history

app = FastAPI()


@app.get('/')
def home():
    return {
        'status': 'Welcome to Bitcamp!',
    }


@app.get("/wizard/{wizard_id}")
async def get_wizard(wizard_id: int):
    return {"wizard_id": wizard_id}


@app.get("/spell/{spell_name}")
async def get_spell(spell_name: str, q: Optional[str] = None):
    if q:
        return {"spell_name": spell_name, "q": q}
    return {"spell_name": spell_name}


class Wizard(BaseModel):
    first_name: str
    last_name: str
    age: int
    hogwarts_house: Optional[str]


@app.post("/wizard", response_model=Wizard)
async def add_wizard(wizard: Wizard):
    return wizard
