import math

def main():
    """ main function """
    counter = 1
    total = 0
    while counter < 1000:
        if counter % 3 == 0 or counter % 5 == 0:
            total = total + counter
        counter= counter + 1
        print str(counter)

    print str(total)
    return 0

if __name__ == "__main__":
    main()
