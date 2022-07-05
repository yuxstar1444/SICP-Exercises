from ast import excepthandler


def f_rec(n):
    if n < 3:
        return n
    else:
        return f_rec(n - 1) + 2 * f_rec(n - 2) + 3 * f_rec(n - 3)


def f_iter (n):
    if n < 3 : return n
    #a represents f(n-1)
    #b represents f(n-2)
    #c represents f(n-3)
    #initialize a, b, and c for n = 3
    a = 2 
    b = 1 
    c = 0 
    for i in range(3 , n):
        a = a + 2 * b + 3 * c
        b = a
        c = b
    return a

try:
    f_rec(3) == f_iter(3)
except:
    print("They are not equivalent!")