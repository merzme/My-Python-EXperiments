"""
1xxxx
12xxx
123xx
1234x
12345"""
def main():
    row = int(input("enter the number of row:"))

    for i in range(1,row+1):
        for j in range(1,i+1):
             print(j, end = " ")

        for j in range(i,row ):
            print('* ', end='')
        print()



if __name__ == "__main__":
     main()