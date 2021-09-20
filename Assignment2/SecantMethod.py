import math
# Epsilon = eps
# x^-1 = x1
# x^0 = x0 

# 7.10 A, B

# let g(x) = (2x-1)^2 + 4(4-1024x)^4
def function(x):
    f = ( 2*x -1 )**2 + 4 * ( 4 - 1024*x )**4
    return f

def secant(x0,x1,eps):
    print('\n Secant Method Implementation for Python')
    while True:
        eps = 0.00001
        secantMethod = x0 - ( x1 - x0 ) * function(x0) / ( function(x1 ) - function(x0) ) 
        x0 = x1
        x1 = secantMethod
        # condition : abs(x0 - x1) < eps * abs(x0) 
        if abs(x0 - x1) < eps * abs(x0):
            print("\n abs(x0 - x1) < eps * abs(x0) is false so it's done!")
            break
        
    print('\n Required root is: %0.8f \n' % secantMethod )

# Initialization
x0 = 0
x1 = 1
eps = 0.00001

# Start the secant Method
secant(x0,x1,eps)



