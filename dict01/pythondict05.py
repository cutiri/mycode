#!/usr/bin/env python3

def main():
    dict = {
        "name": "Darth Vader",
        "real_name": "Anakin Skywalker",
        "species": "Human",
        "homeworld": "Tatooine",
        "affiliation": "Sith",
        "spouse": "Padmé Amidala",
        "children": ["Luke Skywalker", "Leia Organa"],
        "masters": ["Obi-Wan Kenobi (Jedi)", "Darth Sidious (Sith)"],
        "apprentices": {
            "Jedi": ["Ahsoka Tano"],
            "Sith": ["Galen Marek / Starkiller", "Shira Brie / Lumiya"]
        },
        "weapon": "Red Lightsaber",
    }

    print("Choose a key from the list: ")
    print(dict.keys())

    userinput = input()

    print(dict.get(userinput))

    userinput_key = input("Enter a new key: ")
    userinput_value = input("Enter a new value: ")

    dict[userinput_key] = userinput_value

    print("Dictionary has a new key/value: " + userinput_key + " - " + dict[userinput_key])


main()