#!/usr/bin/env python3
""" Author: Jeffrey Moreta """

# declaring operators that are allowed
valid_operators = ['+', '-', '*', '/']

response = {
    'question': {
        'x': 'What is your first number?\t\t',
        'y': 'What is your second number?\t\t',
        'operator': 'What is your operator? '
    },
    'symbols': {
        # converts all valid operators into a string
        'operator': f'{", ".join(valid_operators)}\t',
    },
    'err': {
        'num': "That's definitely not a number. Only premium subscribers can use letters.",
        'operator': 'Please input the symbol and not text',
        'divide': {
            'zero': 'Nice try. Only premium subscribers can divide by zero.'
        }
    }
}
