farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

coords = {
        "NE": ["NE Farm", "Northeast Farm"]
    }

def print_farms_list():
    count = 1
    for farm in farms:
        print(count + ": ", farm.get("name"))

def select_a_farm():
    while True:
        print_farms_list()
        user_input = input(": ")
        farm = list.pop()

def print_animals(farmName):
    farm = list(filter(lambda x: x.get("name") in coords[farmName], farms)).pop(0)
    for animal in farm.get("agriculture"):
        print(animal)

def main():
    print("Part 1: All animals in the NE farm:")
    print_animals("NE")
    print("-----------------------------------")


    print("Part2: Choose a Farm:")
    select_a_farm()
    print("-----------------------------------")

main()