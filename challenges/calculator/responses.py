#!/usr/bin/env python3
""" Author: Jeffrey Moreta """

# declaring operators that are allowed
valid_operators = ('+', '-', '*', '/')

response = {
    'question': {
        'x': 'What is your first number?\t\t',
        'y': 'What is your second number?\t\t',
        'operator': 'What is your operator? '
    },
    'symbols': {
        # converts all valid_operators into a string
        'operator': f'{", ".join(valid_operators)}\t',
    },
    'err': {
        'num': {
            'invalid': "That's definitely not a number. Try again. Bozo."
        },
        'operator': {
            'invalid': 'What? No. Please input a CORRECT operator.',
            'divide': {
                'zero': 'Nice try. Only premium subscribers can divide by zero.'
            }
        }
    },
    'result': 'Result:\n\t{} {} {} = {}\n'
}
