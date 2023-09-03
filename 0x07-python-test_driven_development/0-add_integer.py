#!/usr/bin/python3
def add_integer(number1, number2=98):
    if not isinstance(number1, int) and not isinstance(number1, float):
        raise TypeError("number1 must be an integer")
    if not isinstance(number2, int) and not isinstance(number2, float):
        raise TypeError("number2 must be an integer")
    if isinstance(number1, float):
        number1 = int(number1)
    if isinstance(number2, float):
        number2 = int(number2)
    return number1 + number2

