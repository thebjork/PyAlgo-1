"""
Large powers
implementation
"""

def power(num1: int, num2: int) -> int:
    """
    num1 ^ num2 using binary operations,
    where num1 and num2 are large
    numbers
    """
    result = 1
    while num2 > 0:
        if num2 & 1:
            result = result * num1
        num1 = num1 ** 2
        num2 >>= 1
    return result
