#!/usr/bin/env python3
import requests
import argparse
from pprint import pprint

def main():
    URL= "http://127.0.0.1:2224/api/"

    resp = 'No data obtained...'

    if args.room:
        resp= requests.get(URL + 'room/' + args.room).json()
    elif args.rooms:
        resp = requests.get(URL + 'rooms/').json()
    elif args.item:
        resp= requests.get(URL + 'item/' + args.item).json()
    elif args.items:
        resp = requests.get(URL + 'items/').json() 
    pprint(resp)



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Pass a word to search the StarCraft RPG API")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--room', metavar='SEARCHW',type=str, default='', help="Pass a room's name")
    group.add_argument('--item', metavar='SEARCHW',type=str, default='', help="Pass an item's name")
    group.add_argument('--rooms', action='store_true', help="Returns all the rooms")
    group.add_argument('--items', action='store_true', help="Returns all the items")
    args = parser.parse_args()
    main()
    