"""
Gray Code
implementation
"""

def gray_code(number: int) -> list:
    """
    Gray Code is an ordering of the binary numeral
    system such that two successive values differ
    in only one bit
    """
    if number <= 0:
        return -1

    result: list = []
    result.append("0")
    result.append("1")
    num1 = 2

    while True:
        if num1 >= 1 << number:
            break

        for j in range (num1 - 1, -1, -1):
            result.append(result[j])

        for j in range (num1):
            result[j] = "0" + result[j]

        for j in range (num1, 2 * num1):
            result[j] = "1" + result[j]

        num1 = num1 << 1

    return result
