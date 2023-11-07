#!/usr/bin/python3

import requests

# define the URL we want to use
POSTURL = "https://petstore.swagger.io/v2/pet"

def main():
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    pet = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Jimmy",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "status": "available"
        }
    # use requests library to send an HTTP POST
    resp = requests.post(POSTURL, json=pet)

    print(resp.status_code)

    # display our PYTHONIC data (LIST / DICT)
    print(resp.json())

    # JUST display the value of "validate"
   

if __name__ == "__main__":
    main()
