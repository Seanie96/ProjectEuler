""" solution to problem 4 """
NUM = 998001.0

def main():
    """ main function """
    starting_num = NUM
    while starting_num > 0.0:
        num = int(starting_num)
        if palindrome(num):
            print "palindrome: " + str(num)
            if two_factors(num):
                print "largest number: " + str(num)
                return 0
        starting_num = starting_num - 1.0
    return 0

def palindrome(num):
    """ checkes whether the passed number is a palindrome """
    num_str = str(num)
    index = 0
    length = len(num_str)
    while index <= (length / 2):
        if num_str[index] != num_str[length - 1 - index]:
            return False
        index = index + 1
    return True

def two_factors(num_1):
    """ Function that discoveres whether the passed number can be 
        broken down into 2 three digit number factors. """
    num_1 = float(num_1)
    index = 100.0
    while index < num_1 and index < 1000.0:
        num_2 = num_1 / index
        if num_2 % 1.0 == 0 and num_2 >= 100.0 and num_2 < 1000.0:
            return True
        index = index + 1.0
    return False

if __name__ == "__main__":
    main()
