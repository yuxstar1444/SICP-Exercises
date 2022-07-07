def sum_int( a, b ):
    if (a > b):
        return 0
    else:
        ( (a) + sum_int( a + 1, b))

def sum_cubes(a, b):
    if (a > b):
        return 0
    else:
        ( (a ^ 2) + sum_cubes( a + 1, b))

def pi_sum(a , b):
    if (a > b):
        return 0
    else:
        ( (1.0 / (a * ( a + 2))) + (pi_sum( a + 4, b)))

#These summation procedures can more generally be defined as

def sum (term, a , next, b):
    if (a > b):
        return 0
    else:
        (term(a) + sum (term, next(a), next, b))