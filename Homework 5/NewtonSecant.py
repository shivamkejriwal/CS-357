import pylab as pl
import numpy as np
import math



def newton(x):
	tempA = f(x)
	tempB = f2(x)
	tempx = x-(tempA/tempB)
	return tempx

def secant(xk,xk1):
	tempA = f(xk)
	tempB = f(xk1)
	tempx = xk-tempA*(xk-xk1)/(tempA-tempB)
	return tempx
    
def f(x):
    tempx = (5 - x) * np.exp(x) - 5
    return tempx

def f2(x):
     tempx = -1* np.exp(x)*(x-4)
     return tempx


# Main function
ynewton = [5]
ysecant = [1,5]

#claculate newton approximation    
while True:
    lastvalue = ynewton[len(ynewton)-1]
    newvalue = newton(lastvalue)
    ynewton.append(newvalue)
    if abs(f(newvalue)) < (10**(-8)):
        break
        
print ynewton[len(ynewton)-1]


#claculate secant approximation

while True:
	xk = ysecant[len(ysecant)-1]
	xk1 = ysecant[len(ysecant)-2]
	newvalue = secant(xk,xk1)
	ysecant.append(newvalue)
	if abs(f(newvalue)) < (10**(-8)):
		break
		
print ysecant[len(ysecant)-1]



arraysize = len(ysecant)
if len(ysecant)<len(ynewton):
	arraysize=len(ynewton)
data = []
for i in range(0,arraysize):
	data.append(i)
for i in range(0,arraysize-len(ynewton) ):
	ynewton.append(ynewton[len(ynewton)-1])


#convert to log
logNewton = []
logSecant = []
for i in range(0,arraysize):
	logNewton.append(math.log(ynewton[i]))
	logSecant.append(math.log(ysecant[i]))


#plot
pl.plot(data,logSecant,marker='o', linestyle=':', color='g', label="ysecant")
pl.plot(data,logNewton,marker='o', linestyle='-', color='r', label="ynewton")

pl.xlabel('x')
pl.ylabel('y')
pl.legend()
pl.show()


#------------------- Old Code------------------------------
#nValues = [0,1,2,3,4,5]
#y = []
#for n in nValues:
#    temp = f(n)
#pl.plot(nValues, y,marker='o', linestyle='-', color='r', label="y") # prints original f(x)
