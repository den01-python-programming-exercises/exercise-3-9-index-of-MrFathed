def main():
    #write your code below this line
    numbers = []

    while True:
        number = int(input())

        if number == -1:
            break

        numbers.append(number)

    query = int(input("Search for?"))
    for i in range(len(numbers)):
        if numbers[i] == query:
            print("{} is at index {}".format(query, i))

if __name__ == '__main__':
    main()
