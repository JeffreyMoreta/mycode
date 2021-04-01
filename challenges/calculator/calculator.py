#!/usr/bin/env python3
""" Author: Jeffrey Moreta """

from responses import response
from responses import valid_operators


def add(x, y):
    return x.__add__(y)


def subtract(x, y):
    return x.__sub__(y)


def multiply(x, y):
    return x.__mul__(y)


def divide(x, y):
    try:
        return x.__truediv__(y)
    except ZeroDivisionError:
        print(response.get('err').get('divide').get('zero'))


def ask_num(value):
    # prompt user for a valid number
    while True:
        try:
            return float(input(response.get('question').get(value)).strip())
        except ValueError:
            print(response.get('err').get('num'))


def ask_operator():
    # prompt user for a valid operator
    while True:
        operator = input(response.get('question').get('operator') + response.get('symbols').get('operator')).strip()

        if operator in valid_operators:
            return operator
        else:
            print(response.get('err').get('operator'))


def ask_questions():
    return [ask_num('x'), ask_num('y'), ask_operator()]


def main():
    # deconstruct array, returned from ask_questions(), into manageable variables
    x, y, operator = ask_questions()
    # this is the 'switch' that holds and calls my functions
    math = {'+': add, '-': subtract, '/': divide, '*': multiply}

    print(f'Result: {math.get(operator)(x, y)}\n')


if __name__ == "__main__":
    while __name__ == "__main__":
        main()
