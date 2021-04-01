#!/usr/bin/env python3
""" Author: Jeffrey Moreta """

response = {
    'question': {
        'x': 'What is your first number?\t\t',
        'y': 'What is your second number?\t\t',
        'operator': 'What is your operator? '
    },
    'symbols': {
        'operator': '+, -, *, /\t',
    },
    'err': {
        'num': "That's definitely not a number. Only premium subscribers can use letters.",
        'operator': 'Please input the symbol and not text',
        'divide': {
            'zero': 'Nice try. Only premium subscribers can divide by zero.'
        }
    }
}

# declaring operators that are allowed
valid_operator = ['+', '-', '*', '/']
