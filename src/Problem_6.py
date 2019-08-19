import math
""" solution to problem 6 """

def main():
    max_num = 100
    counter = 1
    sum_ = 0
    sum_of_squares = 0
    while counter <= max_num:
        print str(counter)
        sum_of_squares = sum_of_squares + math.pow(counter, 2)
        sum_ = sum_ + counter
        counter = counter + 1
    sum_ = math.pow(sum_, 2)
    print str(sum_ - sum_of_squares)
    return 0

if __name__ == "__main__":
    main()
