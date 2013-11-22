import scipy as sp
import numpy as np
import pylab as plt

def f(x):
	return x*np.exp(2*x)

def h(a,b,weights,roots):
	tot=0
	for i in range(len(weights)):
		tot=tot+ (b-a)*0.5*( weights[i]*f( (b-a)*0.5*roots[i]+ (b+a)*0.5 ) )
	return tot	 	

weights =  [0.34785485,0.65214515,0.65214515,0.34785485]
roots =  [-0.86113631,-0.33998104,0.33998104,0.86113631]

ans= h(1,2,weights,roots)
print 'ans: {0}'.format(ans)
