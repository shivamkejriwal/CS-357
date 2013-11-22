import numpy as np
import random
import time
import pylab as pl

#vector-vector multiplication
def level1(n):
	start = time.time()
	vector1 = np.random.rand(n)
	vector2 = np.random.rand(n)
	result = np.dot(vector1,vector2)
	elapsed = (time.time() - start)
	return elapsed

#vector-matrix multiplication
def level2(n):
	start = time.time()
	vector = np.random.rand(n)
	matrix = np.random.rand(n,n)
	result = np.dot(vector,matrix)
	elapsed = (time.time() - start)
	return elapsed

#matrix-matrix multiplication
def level3(n):
	start = time.time()
	matrix1 = np.random.rand(n,n)
	matrix2 = np.random.rand(n,n)
	result = np.dot(matrix1,matrix2)
	elapsed = (time.time() - start)
	return elapsed

# main function 
nValues = [10,20,40,50,80,100,200,400,500,800,1000]
level1Times = []
level2Times = []
level3Times = []

print 'Sizes of N: {0}'.format(nValues)

for n in nValues:
	sum = 0
	for i in range (0,10):
		sum+=level1(n)
	level1Times.append(sum/10)
print 'level1 time: {0}'.format(level1Times)

for n in nValues:
	sum = 0
	for i in range (0,10):
		sum+=level2(n)
	level2Times.append(sum/10)
print 'leve2 time: {0}'.format(level2Times)

for n in nValues:
	sum = 0
	for i in range (0,10):
		sum+=level3(n)
	level3Times.append(sum/10)
print 'level3 time: {0}'.format(level3Times)

pl.plot(nValues,level1Times,marker='o', linestyle='-', color='r', label="level1")
pl.plot(nValues,level2Times,marker='o', linestyle=':', color='g', label="level2")
pl.plot(nValues,level3Times,marker='o', linestyle='--', color='b', label="level3")
pl.xlabel('N')
pl.ylabel('time')
pl.legend()
pl.show()
