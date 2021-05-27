
def display(a, b, c=3, d=4, e=5):
    print(a,b,c,d,e)


if __name__ == "__main__":
    display(5,10,15,20,25)
    display(a=5, b= 10, c= 15, d= 20, e=25)
    display(1, 2, 3, d=4, e=5)
    display(1, 2, 3, e=4, d=5)
    display(1,2,3)
    display(1,2)
    display(1,2,e=30)