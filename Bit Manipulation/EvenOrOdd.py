def even_or_odd(number):
    '''
    Checks if integer number is even or odd
    by checking last digit of binary number.

    Only works on integers
    '''
    if bin(number)[-1] == "0":
        # If last binary number is 0, it is even
        print("even")
    else:
        # If not even, it is odd
        print("odd")

if __name__ == '__main__':
    somenumber = 5819011
    even_or_odd(somenumber) # odd