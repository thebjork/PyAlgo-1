import os
import json
import pyalgo
from fastapi import FastAPI

DIRECTORY = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(DIRECTORY, "info.json")) as file:
    JSON = json.loads(file.read())

app = FastAPI()

@app.get("/")
def status() -> str:
    return "PyAlgo API is working"

@app.get("/math")
def functions() -> list:
    return JSON["math"]

@app.get("/math/sieve")
def solve_sieve(number: int) -> list:

    if number <= 0:
        return [None]

    else:
        result = pyalgo.math.sieve.sieve(number)
        return result

@app.get("/math/factorial")
def solve_factorial(number: int) -> int:

    if number < 0:
        return -1

    elif number == 0:
        return 1

    else:
        result = pyalgo.math.factorial.factorial(number)
        return result

@app.get("/math/graycode")
def solve_gray_code(number: int) -> list:

    if number <= 0:
        return [None]
    
    else:
        result = pyalgo.math.gray_code.gray_code(number)
        return result
