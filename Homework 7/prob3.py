import numpy as np
import scipy as sp


def GaussSeidel(A,b,y,N):
	n = y.size
	x=np.zeros(n)
	for k in range (1,N):
		for i in range (1,n): 
			s=b[i]
			for j in range(1,i-1):
				s=s-A[i][j]*y[j] 
			for j in range( i+1,n ):
				s=s-A[i][j]*y[j] 
			x[i]=s/A[i][i]
			x[i]=x[k]  
	return x



A = np.array([[ -10,  -2,  1],
			[ -2,  10,  -2 ],
			[ -2,  -5,  10]])

B = np.array([ 9,  12,  18])

y=np.zeros(3)
print GaussSeidel(A,B,y,2)
