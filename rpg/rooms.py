rooms = {
    'HALL': {
        'south': 'KITCHEN',
        'east': 'DINING ROOM',
        'item': 'sword',
        'item_status': ' inside of a display case. It is unlocked',
        'randenc': '20',
        'desc': 'You are in the hall of a large, decrepit house. The walls are blackened from some ancient fire. You get the feeling you are being watched. To the east is a dusty dining room. South is the kitchen... something is moving there.'
    },
    'KITCHEN': {
        'north': 'HALL',
        'randenc': '0',
        'down': 'BASEMENT',
        'desc': 'You are in what was once a kitchen. Nests made of human bones are draped across every countertop. There is a large hole in the floor. Where it leads you have no idea.'
    },
    'BASEMENT': {
        'spell': 'fireball',
        'desc': 'You are in a stinking basement with an earthen floor. You can\'t even see your hand in front of your face. You are likely to be eaten by a grue.',
        'randenc': '0',
        'up': 'KITCHEN',
    },
    'DINING ROOM': {
        'west': 'HALL',
        'south': 'GARDEN',
        'north': 'PANTRY',
        'desc': 'You are in the dining room. The table is set for an elegant party but is covered a blanket of dust. Sleeping bats cling to the chandelier. North is a dark pantry. South lies the garden. West returns to the hall.',
        'randenc': '0',
        'item': 'potion',
        'item_status': ' hiding among the bottles of wine. It is cherry red in color'
    },
    'GARDEN': {
        'north': 'DINING ROOM',
        'spell': 'fireball',
        'randenc': '0',
    },
    'PANTRY': {
        'south': 'DINING ROOM',
        'randenc': '0',
        'item': 'cookie'
    }
}