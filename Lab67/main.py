def main():
    file = open("dracula.txt", "r")
    filew = open("vampytimes.txt", "a")
    
    count = 0
    for line in file:
        if "vampire" in line.lower():
            print(line)
            count += 1
            filew.write(line)
    
    file.close()
    filew.close()

    print("The vampire word appears", count, "times")

main()