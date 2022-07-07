def square( x ):
    return x * x

def average( a , b):
    return ( a + b ) / 2


#A procedure that returns a procedure
def avg_damp( f ):
    return lambda x: average(x, f(x))


#Using the output procedure
print( (avg_damp(square))( 10 ) )