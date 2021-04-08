# A dictionary linking a room to other rooms

rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
        'north': 'Pantry',
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie',
    }
}