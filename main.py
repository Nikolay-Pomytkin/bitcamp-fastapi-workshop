from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from data import wizards, spells, spell_history


app = FastAPI()


@app.get('/')
def home():
    return {
        'status': 'Welcome to Bitcamp!',
    }


@app.get("/wizard/{wizard_id}")
async def get_wizard(wizard_id: int):
    if wizard_id in wizards.keys():
        return wizards[wizard_id]
    return {"error": "wizard doesn't exist"}


@app.get("/wizards")
async def get_wizards(wizard_id: Optional[int] = None, hogwarts_house: Optional[str] = None):
    if wizard_id:
        return wizards[wizard_id]
    if hogwarts_house:
        filtered_wizards = []
        for key, value in wizards.items():
            value_dict = value.__dict__ if type(value) != dict else value
            if value_dict["hogwarts_house"] == hogwarts_house:
                value_dict["wizard_id"] = key
                filtered_wizards.append(value_dict)
        return filtered_wizards

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
    wizards[len(wizards)+1] = wizard
    return wizard
