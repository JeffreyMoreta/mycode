#!/usr/bin/env python3
""" Author: Jeffrey Moreta """

from responses import response, valid_operators


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
        print(response.get('err').get('operator').get('divide').get('zero'))


# prompt user for a valid number
def ask_num(number):
    while True:
        try:
            return float(input(response.get('question').get(number) +
                               response.get('input').get('spacer').get('md')).strip())
        except ValueError:
            print(response.get('err').get('num').get('invalid'))


# prompt user for a valid operator
def ask_operator():
    while True:
        operator = input(response.get('question').get('operator') +
                         response.get('symbols').get('operator') +
                         response.get('input').get('spacer').get('sm')).strip()

        if operator in valid_operators:
            return operator
        else:
            print(response.get('err').get('operator').get('invalid'))


def ask_questions():
    return [ask_num('x'), ask_num('y'), ask_operator()]


def main():
    x, y, operator = ask_questions()                                # deconstruct list, returned from ask_questions()
    math = {'+': add, '-': subtract, '/': divide, '*': multiply}    # 'switch' that references and calls my functions

    print(response.get('result').format(x, operator, y, math.get(operator)(x, y)))


if __name__ == '__main__':
    while __name__ == '__main__':                                   # doesn't seem like something I should be doing
        main()
