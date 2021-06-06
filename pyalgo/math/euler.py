"""
Euler's algorithms
implementation
"""

def gcd(num1: int, num2: int) -> int:
    """
    Greatest Common Divisor of two numbers
    using Euler's theorem & recursion
    """
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 > num2:
        return gcd(num1 % num2, num2)
    else:
        return gcd(num1, num2 % num1)

def lcm(num1: int, num2: int) -> int:
    """
    Least Common Divisor of two numbers
    using GCD
    """
    result = (num1 * num2) // gcd(num1, num2)
    return result

def totient(number: int) -> int:
    """
    Euler's totient function counts the positive
    integers up to a given integer n that are relatively
    prime to n
    """
    result = number
    p = 2

    while p ** 2 <= number:
        if number % p == 0:
            while number % p == 0:
                number = int(number / p)
            result -= int(result / p)
        p += 1

    if number > 1:
        result -= int(result / number)
    return result
