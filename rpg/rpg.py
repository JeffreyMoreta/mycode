#!/usr/bin/python3
from rooms import rooms


def showInstructions():
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


def main():
    inventory = []
    currentRoom = 'Hall'

    showInstructions()

    # loop forever
    while True:

        showStatus()

        # get the player's next 'move'
        # .split() breaks it up into an list array
        # eg typing 'go east' would give the list:
        # ['go','east']
        move = ''
        while move == '':
            move = input('>')

        # split allows an items to have a space on them
        # get golden key is returned ["get", "golden key"]
        verb, subject = move.lower().split(" ", 1)

        # if they type 'go' first
        if verb == 'go':
            # check that they are allowed wherever they want to go
            if subject in rooms[currentRoom]:
                # set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            # there is no door (link) to the new room
            else:
                print('You can\'t go that way!')

        # if they type 'get' first
        if verb == 'get':
            # if the room contains an item, and the item is the one they want to get
            if "item" in rooms[currentRoom] and subject in rooms[currentRoom]['item']:
                # add the item to their inventory
                inventory += [move[1]]
                # display a helpful message
                print(move[1] + ' got!')
                # delete the item from the room
                del rooms[currentRoom]['item']
            # otherwise, if the item isn't there to get
            else:
                # tell them they can't get it
                print('Can\'t get ' + move[1] + '!')

        # Define how a player can win
        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
            print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            break

        # If a player enters a room with a monster
        elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            print('A monster has got you... GAME OVER!')
            break


if __name__ == "__main__":
    main()
