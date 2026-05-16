from fastapi import FastAPI
from abacus import Abacus

app = FastAPI()

abacus = Abacus()

@app.get("/")
def home():
    return {"message": "Abacus AI Backend Running"}

@app.get("/add")
def add(number: int, value: int):
    abacus.set_number(number)
    abacus.add(value)

    return {
        "result": abacus.get_number()
    }

@app.get("/subtract")
def subtract(number: int, value: int):
    abacus.set_number(number)
    abacus.subtract(value)

    return {
        "result": abacus.get_number()
    }
@app.get("/multiply")
def multiply(number: int, value: int):

    abacus.set_number(number)
    abacus.multiply(value)

    return {
        "result": abacus.get_number()
    }