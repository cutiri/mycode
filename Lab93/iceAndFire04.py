#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"


def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        print("Houses:")
        allegiancesURLs = got_dj.get("allegiances")
        for allegiance in allegiancesURLs:
            request = requests.get(allegiance)
            house = request.json()
            pprint.pprint(house.get("name"))


        print("Books:")
        booksURLs = got_dj.get("books")
        for bookURL in booksURLs:
            request = requests.get(bookURL)
            book = request.json()
            pprint.pprint(book.get("name"))

if __name__ == "__main__":
        main()
