#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"


def print_result(result):
    print("", requests.get(result).json().get('name'))


def combine_requests(info):
    result = []

    for request in info:
        result.extend(request)

    return result


def main():
    # Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! ")

    # Send HTTPS GET to the API of ICE and Fire character resource & decode response
    got_dj = requests.get(AOIF_CHAR + got_charToLookup).json()

    # Get Name
    print("Name:")
    print_result(AOIF_CHAR + got_charToLookup)

    # Get Allegiance
    print("House:")
    for allegiance in got_dj.get('allegiances'):
        print_result(allegiance)

    # Get Books
    print("Appearances:")
    for book in combine_requests([got_dj.get('books'), got_dj.get('povBooks')]):
        print_result(book)


if __name__ == "__main__":
    main()
