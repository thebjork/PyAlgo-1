"""
Factorial of numbers
implementation
"""

def factorial(number: int):
    """
    Calculating factorial of a number using
    prime decomposition method

    Params
    :number:    =>  number whose factorial has
                    to be calculated
    """
    prime: list = [True] * (number + 1)
    result: int = 1

    for i in range (2, number + 1):

        if prime[i]:
            j: int = 2 * i
            while j <= number:
                prime[j] = False
                j += i
            SUM: int = 0
            num: int = i

            while num <= number:
                SUM += number // num
                num *= i

            result *= i ** SUM

    return result
