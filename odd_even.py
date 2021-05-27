
def main():
    num_str = input('enter a number:')
    try:
        num = float(num_str)
    except ValueError:
        print('Invalid input')
    else:
        if num % 2 == 0:
            print('num is even')
        else:
            print('num is odd')


if __name__ == "__main__":

     main()