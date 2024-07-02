# main.py
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"Welcome" : "Aboard"}

@app.get("/items/{item_id}")
def read(item_id : int, q : str | None = None):
    return {"item_id" : item_id, "q" : q}

class Item(BaseModel):
    name : int
    price : float
    is_offer : bool | None = None

@app.put("/items/{item_name}")
def update(item_id : int, item : Item):
    return {"item_name" : item.name, "item_id" : item_id}