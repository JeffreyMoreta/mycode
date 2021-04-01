#!/usr/bin/env python3
""" Author: Jeffrey Moreta """

question = {
    'x': 'What is your first number?\t',
    'y': 'What is your second number?\t',
    'operator': 'What is your operator?\t',
    'operator-symbols': '+, -, *, /\t',
    'err': {
        'num': "That's definitely not a number. Only premium subscribers can use letters.",
        'operator': 'Please input the symbol and not text',
        'divide': {
            'zero': 'Nice try. Only premium subscribers can divide by zero.'
        }
    }
}


def add(x, y):
    return x.__add__(y)


def subtract(x, y):
    return x.__sub__(y)


def divide(x, y):
    try:
        return x.__truediv__(y)
    except ZeroDivisionError:
        print(question.get('err').get('divide').get('zero'))


def multiply(x, y):
    return x.__mul__(y)


def ask_input(user_prompt):
    return input(user_prompt)


def ask_questions():
    # declaring operators that are allowed
    valid_operator = ['+', '-', '*', '/']

    # repeated myself too much - figure out way to condense
    while True:
        # prompt user for a valid number
        try:
            x = float(ask_input(question.get('x')))
            if type(x) is float:
                break
        except ValueError:
            print(question.get('err').get('num'))

    while True:
        # prompt user for a second valid number
        try:
            y = float(ask_input(question.get('y')))
            if type(y) is float:
                break
        except ValueError:
            print(question.get('err').get('num'))

    while True:
        # prompt user for a valid operator
        operator = ask_input(question.get('operator') + question.get('operator-symbols'))
        if operator in valid_operator:
            break
        else:
            print(question.get('err').get('operator'))

    return [x, y, operator]


def calc(user_response):
    # deconstruct array, user_response, into manageable variables
    x, y, operator = user_response
    # this is the 'switch' that holds and calls my functions
    operator_switch = {
        '+': add,
        '-': subtract,
        '/': divide,
        '*': multiply
    }

    math = operator_switch.get(operator)
    print(f'Result: {math(x, y)}')


def main():
    calc(ask_questions())


if __name__ == "__main__":
    main()
