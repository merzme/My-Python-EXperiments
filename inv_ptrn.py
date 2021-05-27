
def main():
    row = int(input("enter number of rows:"))
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*", end = "")
        print(sep = "/n")


if __name__ == "__main__":
    main()