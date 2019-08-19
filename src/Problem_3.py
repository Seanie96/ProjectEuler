import math
import sympy

NUM = 600851475143 # 4 million max

def main():
    """ main function """
    num1 = 1
    num2 = 2
    total = 0
    while num2 < LIMIT:
        if num2 % 2 == 0:
            total = total + num2
        tmp = num1
        num1 = num2
        num2 = tmp + num2

        print str(num2)

    print str(total)
    return 0

if __name__ == "__main__":
    main()
