def main():
    start = int(input("How many bottles of beer? "))

    for num in reversed(range(start)):
        print(num, "bottles of beer on the wall!")
        if num != 0:
            print(num, "bottles of beer on the wall!", num, "bottles of beer! You take one down, pass it around!")

main()