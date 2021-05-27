
def main():
    row = int(input("enter number of rows:"))
    a = 0
    for i in range(row,0,-1):
        a = a + 1
        for j in range(1, i+1):

            print(j, end = "")
        print(sep = "/n")


if __name__ == "__main__":
    main()