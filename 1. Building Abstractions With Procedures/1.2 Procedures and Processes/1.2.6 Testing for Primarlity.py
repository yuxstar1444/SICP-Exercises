#Methods of finding the primality of a number

#Using divisor searching



def smallest_divisor(n):
    find_divisor (n, 2)

def find_divisor (n ,test_div):
    if (test_div * test_div) > n:
        return n
    elif (divides(n, test_div)):
        return test_div
    else:
        find_divisor(n, test_div + 1)


def divides (a, b):
    return ((b % a) == 0)

def isPrime ( n ):
    return (smallest_divisor( n ) == n)
    