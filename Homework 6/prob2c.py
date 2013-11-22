import scipy as sp
import numpy as np
import pylab as plt

def f(x):
	return 4+4*(x+1)

def g(x):
	return 8-8*x
	
def h(x):
	return -3*(x+1)**3+11*(x+1)-4*x
	
def l(x):
	return -3*(1-x)**3+11*(1-x)	
	
x1 = np.linspace(-1,0,100)
x2 = np.linspace(0,1,100)
x3 = np.linspace(-1,0,100)
x4 = np.linspace(0,1,100)

y1 = f(x1)
plt.plot(x1,y1,linestyle='-', color='r',label="1a")
y2=g(x2)
plt.plot(x2,y2,linestyle=':', color='g',label="1b")
y3=h(x3)
plt.plot(x3,y3,linestyle='--', color='b',label="3a")
y4=l(x4)
plt.plot(x4,y4,linestyle='-.', color='y',label="3b")
plt.legend()
plt.show()
