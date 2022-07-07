# Original Function

def pi_sum(a , b):
    if (a > b):
        return 0
    else:
        ( (1.0 / (a * ( a + 2))) + (pi_sum( a + 4, b)))

        

# Lambdafied

def sum (term, a , next, b):
    if (a > b):
        return 0
    else:
        (term(a) + sum (term, next(a), next, b))

def pi_sum(a , b):
    return (sum( 
            lambda x: (1 / (x * x + 2)),
            a,
            lambda x: x + 4),
            b)
