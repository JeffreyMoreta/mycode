#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    print(got_dj)

if __name__ == "__main__":
    main()
