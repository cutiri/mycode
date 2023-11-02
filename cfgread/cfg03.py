#!/usr/bin/env python3
## create file object in "r"ead mode



while True:
    try:
        filename = input("Enter filename: ")
        with open(filename, "r") as configfile:
            ## readlines() creates a list by reading target
            ## file line by line
            configlist = configfile.readlines()
            print("The file has", len(configlist), "lines.")
            break
    except Exception:
        print("Can't open", filename, "try again")

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
