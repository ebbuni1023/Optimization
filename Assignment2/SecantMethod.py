import math
# Epsilon = e
# x^-1 = x1
# x^0 = x0 

# 7.10 A.

def function(x):
    f = (2*x-1)**2 + 4*(4-1024*x)**4
    return f


# Implementing Secant Method

def secant(x0,x1,e,N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1

    while True:
        # if function(x0) == function(x1):
        #     print('Divide by zero error!')
        #     break
        eps = 0.00001
        x2 = x0 - (x1-x0)*function(x0)/( function(x1) - function(x0) ) 
        # print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, function(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if abs(x0 - x1) < eps * abs(x0):
            print('Exit')
            break
        
        condition = abs(function(x2)) > e
    print('\n Required root is: %0.8f' % x2)


# Input Section
x0 = 0
x1 = 1
eps = 0.00001
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
x1 = float(x1)
eps = float(eps)

# Converting N to integer
N = int(N)


#Note: You can combine above three section like this
# x0 = float(input('Enter First Guess: '))
# x1 = float(input('Enter Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Secant Method
secant(x0,x1,eps,N)



