#!/usr/bin/env python3
""" Author: Jeffrey Moreta """

# declaring operators that are allowed
valid_operators = ('+', '-', '*', '/')

response = {
    'input': {
        'spacer': {
            'sm': '\t',
            'md': '\t\t',
            'lg': '\t\t\t'
        }
    },
    'question': {
        'x': 'What is your first number?',
        'y': 'What is your second number?',
        'operator': 'What is your operator? '
    },
    'symbols': {
        'operator': "{}".format(", ".join(valid_operators)),        # converts all valid_operators into a string
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
