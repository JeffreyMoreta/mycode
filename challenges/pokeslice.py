#!/usr/bin/env python3

# imports always go at the top of your code
import requests


def main():
    pokemon = input("Which pokemon would you like to look up?").lower()
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon).json()

    # Print front_default
    print("front_default url:", pokeapi.get('sprites').get('front_default'))

    # Count game_indices
    print("# of games:", len(pokeapi.get('game_indices')))

    # Print all the moves
    print("Moves")
    for move_collection in pokeapi.get('moves'):
        print("", move_collection.get('move').get('name'))


if __name__ == "__main__":
    main()
