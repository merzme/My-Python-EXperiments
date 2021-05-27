
def sum(x,y):
    """
    sum = x+y
    """
    z = x+y
    return z

def print_sum(p,q,r):
    """
    the print sum fn will print the sum of the 3 numbers passing to it
    """
    s = p+q+r
    print("s",s)

def main():
    a = 5
    b = 10
    c = 25
    print_sum(p=a,r=b,q=c)


if __name__ == "__main__":
    main()