""" solution to problem 9 """

def pythagTripletExists(c):
    ab = 1000 - c
    a = 1
    b = ab - a
    while True:
        a2 = a*a
        b2 = b*b
        c2 = c*c
        if (a2 + b2) == c2:
            return (True, a, b, c)
        else:
            a = a + 1
            b = b - 1
            if b <= a:
                return (False, -1, -1, -1)      # returning arbitrary values since they are not checked

def main():
    c = 997
    while c >= 334:
        res = pythagTripletExists(c)
        if res[0]:
            break
        else:
            c = c - 1

    if res[0] == False:
        print("Did not find")
    else:
        print(str(res[1]*res[2]*res[3]))

if __name__ == "__main__":
    main()
