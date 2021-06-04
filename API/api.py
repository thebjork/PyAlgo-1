import os
import json
from unittest import result
import pyalgo
from fastapi import FastAPI

DIRECTORY = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(DIRECTORY, "info.json")) as file:
    JSON = json.loads(file.read())

app = FastAPI()

@app.get("/")
def status() -> str:
    return "PyAlgo API is working"

@app.get("/info")
def info():
    return JSON["information"]

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

@app.get("/math/gcd")
def solve_gcd(num1: int, num2: int) -> int:

    result = pyalgo.math.euler.gcd(num1, num2)
    return result

@app.get("/math/lcm")
def solve_gcd(num1: int, num2: int) -> int:

    result = pyalgo.math.euler.lcm(num1, num2)
    return result

@app.get("/math/totient")
def solve_gcd(number: int) -> int:

    result = pyalgo.math.euler.gcd(number)
    return result
