from IPython.display import display, Markdown
import numpy
import scipy

epsilon = 10 ** (-6)
stop_value = 10 ** (-4)
# initial x vector
x_0 = numpy.array([-2.0,2.0])

# our vector function, fully expanded
# in this case it is rosenbrock's function
def f(x):
	x1 = x[0]
	x2 = x[1]
	f = ( 100 * (x1 ** 4) - 200 *(x1 ** 2) * (x2) + (x1 ** 2) - 2 * (x1) + 100 * (x2 ** 2) +1 )
	return f

# gradient of f named Df
def Df(x):
	x1 = x[0]
	x2 = x[1]

	g1 = ( 400 * (x1 ** 3) - 400 * (x1) * (x2) + 2 * (x1) - 2 )
	g2 = ( -200 * (x1 ** 2) + 200 * (x2) )

	g = numpy.array([g1, g2])
	return g

# simple gradient descend, iterate once
def f_descend(x_k):
	# partial derivatives at x_k for each respective element
	g1_k = Df(x_k)[0]
	g2_k = Df(x_k)[1]

	# combine elements back into gradient vector
	g_k = numpy.array([g1_k, g2_k])

	# get our optimized alpha for current iteration k
	a_k = a_minimizer(x_k, g_k)

	# simple descent 
	x_kplus1 = numpy.array( x_k - a_k * g_k )
	return x_kplus1

def f_minimizer():
	# initialize iterator k
	k = 0

	# initialize first k at initial x
	x_k = x_0

	# initialize our stop condition
	stop_condition = False

	while (stop_condition == False):

		# Update current next iteration x-valu
		x_kplus1 = f_descend(x_k)

		# observe current gradient (g_k) at x_k, 
		g_k = Df(x_k)
		
		# Update stop condition value
		# in this case, we stop when the norm of the current gradient is less than 10^-4
		stop_condition = numpy.linalg.norm(g_k) < 10 ** stop_value

		# Shift up one iteration ###
		x_k = x_kplus1
		k += 1

	return x_k, k

# phi of alpha function at current iteration k for x vector and gradient g
def phi(a, x_k, g_k):
	# actually plugging in our values to get our phi function. recall: phi is just renamed function f, for new special input value x - a * g
	phi = f(x_k - a * g_k)
	return phi

# explicity defined phi instead of relying on passing input to f
def phi_ex(a, x_k, g_k):
	x1 = x_k[0]
	x2 = x_k[1]

	g1 = g_k[0]
	g2 = g_k[1]

	phi = ( 100 * ((x1 - a * g1) ** 4) - 200 *((x1 - a * g1) ** 2) * (x2 - a * g2) + ((x1 - a * g1) ** 2) - 2 * (x1 - a * g1) + 100 * ((x2 - a * g2) ** 2) +1 )

# Dphi, but instead we use fully written derivative of phi to avoid using scipy.misc.derivative
def Dphi_ex(a, x_k, g_k):
	x1 = x_k[0]
	x2 = x_k[1]

	g1 = g_k[0]
	g2 = g_k[1]
	
	phi_ex =400 * a**3 * g1**4 - 1200 * a**2 * g1**3 * x1 + 600 * a**2 * g1**2 * g2 + 1200 * a * g1**2 * x1**2 - 400 * a * g1**2 * x2 + 2 * a * g1**2 - 800 * a * g1 * g2 * x1 + 200 * a * g2**2 - 400 * g1 * x1**3 + 400 * g1 * x1 * x2 - 2 * g1 * x1 + 2 * g1 + 200 * g2 * x1**2 - 200 * g2 * x2
	return phi_ex

# derivative of phi using scipy.misc.derivative
# major bugs from this function, throwing lots of object type errors
def Dphi(a, x_k, g_k):
	# wolfram calculated d/da (phi):
	# 400 a^3 g1^4 - 1200 a^2 g1^3 x1 + 600 a^2 g1^2 g2 + 1200 a g1^2 x1^2 - 400 a g1^2 x2 + 2 a g1^2 - 800 a g1 g2 x1 + 200 a g2^2 - 400 g1 x1^3 + 400 g1 x1 x2 - 2 g1 x1 + 2 g1 + 200 g2 x1^2 - 200 g2 x2
	# far too unweildy, so I will just approximate derivative value at point a using scipy
	# for this library function, we pass our function to be derived, phi,
	# and we pass our point to be derived at, in this case wherever our a is
	return scipy.misc.derivative(phi_ex(a, x_k, g_k), a)

# alpha minimizer using secant algorithm
def a_minimizer(x_k, g_k):
	# epsilon value for alpha search
	a_epsilon = 10 ** (-6)
	
	# initial values for alpha
	a_0 = 0.0
	a_1 = 0.0001

	# initialize index
	j = 0

	# set current index to initial values
	a_jminus1 = a_0
	a_j = a_1
	a_jplus1 = a_secant(a_jminus1, a_j, x_k, g_k)

	# initialize stop condition
	stop_condition = False

	while (stop_condition == False):

		# Update current next iteration a-value using secant method 
		a_jplus1 = a_secant(a_jminus1, a_j, x_k, g_k)

		# Update stop condition value 
		stop_condition = (abs(a_jplus1 - a_j) < abs(a_j)*a_epsilon)

		# Shift up one iteration 
		a_jminus1 = a_j
		a_j = a_jplus1
		j += 1

	# after the while loop has terminated, variable a_j should have been updated
	# with the final value after minimization
	return a_j


# secant iterator for alpha. needs inputs x_k, g_k because it needs to know where current x_k, g_k are. These are constants.
# function takes current and previous alpha values, denoted a_j and a_jminus1 respectively
# and returns next alpha value, a_jplus1.
# index j is being used because index k is reserved for the main function, 
# and for now we are looking at just one index k to find minimized alpha, 
# which will need iterating over several j indeces.
def a_secant(a_jminus1, a_j, x_k, g_k):
	numerator = (Dphi_ex(a_j, x_k, g_k)*a_jminus1 - Dphi_ex(a_jminus1, x_k, g_k)*a_j)
	denominator = (Dphi_ex(a_j, x_k, g_k) - Dphi_ex(a_jminus1, x_k, g_k))
	a_jplus1 = (numerator) / (denominator)
	return a_jplus1


def  run():
	minimum, iterations = f_minimizer()
	print("minimum:", minimum)
	print("iterations:", iterations)

run()