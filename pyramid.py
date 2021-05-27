def main(row):
    #row = int(input("Enter a number of rows::"))
    for i in range(row):
        for j in range(i + 1):
            print("* ", end="")
        print()


if __name__ == "__main__":
    main(5)
    main(7)
    main(10)