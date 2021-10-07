# import math
# # Epsilon = eps
# # x^-1 = x1
# # x^0 = x0 

# # 7.10 A, B

# # let g(x) = (2x-1)^2 + 4(4-1024x)^4
# def function(x):
#     # can change the function
#     f = ( 2*x -1 )**2 + 4 * ( 4 - 1024*x )**4
#     return f

# def secant(x0,x1,eps):
#     print('\n Secant Method Implementation for Python')
#     while True:
#         eps = 0.00001
#         secantMethod = x0 - ( x1 - x0 ) * function(x0) / ( function(x1 ) - function(x0) ) 
#         x0 = x1
#         x1 = secantMethod
#         # condition : abs(x1) < eps 
#         if abs(x1) < eps:
#             print("\n abs(x0 - x1) < abs(x1) < eps is false so it's done!")
#             break
        
#     print('\n Number of ietrations to satisfy the stopping criterion : %0.8f \n' % secantMethod)
#     print(' Final point to see how close it is to 0 : %0.8f \n' % function(secantMethod))
# # Initialization
# x0 = 0
# x1 = 1
# eps = 0.00001

# # Start the secant Method
# secant(x0,x1,eps)
nargin = 0
if nargin != 3:
    options =[]
    if nargin !=2:
        print('Wrong number of Argument')

if len(options) >= 14:
    if options(14)==0:
        options(14)=1000*len(xnew)
    else:
        options(14)=1000*len(xnew)
        


