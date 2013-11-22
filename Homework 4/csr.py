import pylab as pl
import numpy as np
#import scipy as sp
import math
from scipy.sparse import *
from scipy import *

A = np.array([[ 11,  0,  0,  0, 0,  0,  14],
			[ 0,  0,  0,  0,  23,  0,  0],
			[ 0,  0,  0,  0,  33,  34,  0],
			[ 0,  15,  0,  0,  43,  44,  0],
			[ 0,  0,  0,  0,  0,  54,  0],
			[ 0,  0,  62,  0,  0,  0,  0],
			[ 0,  0,  72,  0,  0,  0,  0]])
AA=[]
JA=[]
IA=[]

for i in range(0,len(A)):
	flag=1
	for j in range(0,len(A)):
		if A[i][j] != 0:
			if flag==1 :
				IA.append(len(AA))
				flag=0
			AA.append(A[i][j])
			JA.append(j)
			
print A
print len(A)

IA.append(len(AA));#append last value on data

numpyAA = array(AA)
numpyJA = array(JA)
numpyIA = array(IA)

print numpyAA
print numpyJA
print numpyIA


#sparseMatrix = csr_matrix( (numpyAA,numpyJA,numpyIA), shape=(len(A),len(A)) ).todense
#print sparseMatrix

lilMatrix = csr_matrix( (numpyAA,numpyJA,numpyIA), shape=(len(A),len(A)) ).tolil()
print lilMatrix

