import numpy as np
import scipy as sp

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in xrange(1, n):
        s += 2 * f(a + i * h)
    return s * h / 2

def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)
    return s * h / 3

def gq3 ( f, a, b, n ):
	h = (b-a)/(2*n)
	x = np.linspace(a,b,n)
	c1 = 5.0 / 9.0
	c2 = 8.0 / 9.0

	total = 0.0
	for i in range(n):
		total = total +( c1 * f( x[i] + h - np.sqrt(3/5) * h ) 
						+ c2 * f( x[i] + h )
						+ c1 * f( x[i] + h + np.sqrt(3/5) * h ) )
	return (h) * total
	
#--------------------------------	

def func(x):
	return np.sin(x);
		
n = 120
a = 0
b = (np.pi)/2

ans1=trapezoidal_rule(func,a,b,n)
print 'ans1 is: {0}'.format(ans1)

ans2=gq3(func,a,b,n)
print 'ans2 is: {0}'.format(ans2)

ans3=simpson(func,a,b,n)
print 'ans3 is: {0}'.format(ans3)

