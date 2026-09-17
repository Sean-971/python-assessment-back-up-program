#!/usr/bin/python3

import math
import sys

def main():
    """
    This Python code demonstrates the following features:

    * import and use of a library, in this case the math library
    * definition and use of a main() function
    * basic exception handling
    * use of the sys.exit() function to exit a program
    * concatentation of items into a string
    * conversion between integers and strings using the int() and str() functions, respectively.

    """
    try:
        number = int(input("Enter a number: "))
        
        for n in range(1, number + 1):
            print("The number is " + str(n) + ", its square is " + str(int(math.pow(n , 2))) + " and its cube is " + str(int(math.pow(n, 3))) + ".")
	sys.exit(0)
            
    except ValueError:
        print("ERROR: The value entered must be an integer.")
        sys.exit(1)

if __name__ == '__main__':
    main()