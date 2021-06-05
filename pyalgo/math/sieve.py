"""
Sieve of Eratosthenes
implementation
"""

def sieve(number: int) -> list:
    """
    the sieve of Eratosthenes is an algorithm for
    finding all prime numbers up to any given limit
    """
    num1: int = (number - 1) // 2
    num2: int = 0
    num3: int = 3
    arr: list = [True] * num1
    result: list = [2]

    while (num3 ** 2) < number:
        if arr[num2]:
            result.append(num3)
            num4 = 2 * num2 * num2 + 6 * num2 + 3

            while num4 < num1:
                arr[num4] = False
                num4 = num4 + 2 * num2 + 3
        num2 += 1
        num3 += 2

    while num2 < num1:
        if arr[num2]:
            result.append(num3)
        num2 += 1
        num3 += 2

    return result
