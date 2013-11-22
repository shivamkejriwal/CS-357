import pylab as pylab
import numpy as np

def showfunc():
    x = np.linspace(0,5,100)
    y = ((5-x)*np.exp(x))-5
    pylab.plot(x,y)
    pylab.show()
    

def f(x):
    return ((5-x)*np.exp(x))-5
    
def df(x):
    return (-np.exp(x))*(x-4)
    
def NewtonsMethod(guess):
    xklist = [5]
    while (True):
        guess = guess - (f(guess)/df(guess))
        xklist.append(guess)
        if (abs(f(guess)) < 10**(-8)):
            return xklist
            break
            
def SecantMethod(prevguess):
    guess = 4
    xklist = [5]
    while (True):
        newguess = guess - ((f(guess)*(guess-prevguess))/f(guess)-f(prevguess))
        prevguess=guess
        guess=newguess
        xklist.append(newguess)
        if (abs(f(newguess)) < 10**(-8)):
            return xklist
            break

def convergancegraph():
    y = np.log10(NewtonsMethod(5))
    z = np.log10(SecantMethod(5))
    pylab.plot(z)
    pylab.plot(y)
    pylab.show()
   
convergancegraph()
