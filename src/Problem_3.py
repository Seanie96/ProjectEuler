import math
import sympy

NUM = 600851475143.0 # 4 million max

def main():
    """ main function """
    num1 = NUM
    num2 = 1.0
    while num1 >= 1:
        if num1 % 1 == 0.00:
            if sympy.isprime( int( num1 ) ):
                print str( num1 )
                print str( "here" )
                break
            else:
                print str( num1 )
                
        num2 = num2 + 1
        num1 = NUM / num2

    return 0

if __name__ == "__main__":
    main()
