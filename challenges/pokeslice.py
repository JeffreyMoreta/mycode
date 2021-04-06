#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import argparse


def main():
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/{args.poke}").json()

    # Print front_default
    print("front_default url:", pokeapi.get('sprites').get('front_default'))

    # Count game_indices
    print("# of games:", len(pokeapi.get('game_indices')))

    # Print all the moves
    print("Moves")
    for move_collection in pokeapi.get('moves'):
        print("", move_collection.get('move').get('name'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--poke', help='Provide the name of a Pokemon (or its PokeDex number)').lower()
    args = parser.parse_args()
    main()
