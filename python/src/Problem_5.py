""" solution to problem 5 """

def main():
    """ euclids algorithm => (n1 * n2 * n3 ... * nm) / gcd(n1, gcd(n2, gcd(n3, ... gcd(nm-1, nm)))) """

    #nums = [20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    nums = [20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0]
    """
    dividend = 1.0
    for i in nums:
        dividend = dividend * i

    print "dividend: " + str(dividend)
    gcd = gcdList(nums.pop(0), nums)
    print "gcd: " + str(gcd)
    print "lcm: " + str(dividend/gcd)
    """
    counter = 20
    while True:
        for i in nums:
            if int(counter % i) != 0:
                break
            if nums[len(nums)-1] == i:
                print str(counter)
                return 0
        counter = counter + 20
    return 0

def gcdList(num_1, l):
    if len(l) > 1:
        num_2 = gcdList(l.pop(0), l)
    elif len(l) == 1:
        num_2 = l.pop(0)

    return gcd(num_1, num_2)

def gcd(num_1, num_2):
    if int(num_1) == 0:
        print str(num_2)
        return num_2
    elif int(num_2) == 0:
        print str(num_1)
        return num_1

    res = int(num_1/num_2)
    remainder = (res%1)*num_2
    return gcd(num_2, remainder)

if __name__ == "__main__":
    main()
