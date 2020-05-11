""" solution to problem 7 """

def main():
    size = 1000000
    counter = 2
    primeCounter = 1
    primes = [True] * size
    while counter <= size - 1:
        if primes[counter]:
            print(str(primeCounter) + " : " + str(counter))
            if primeCounter == 10001:
                break
            else:
                primeCounter = primeCounter + 1
            scalar = 2
            while True:
                innerCounter = counter*scalar
                if innerCounter >= size:
                    break
                else:
                    primes[innerCounter] = False
                scalar = scalar + 1
        counter = counter + 1

if __name__ == "__main__":
    main()
