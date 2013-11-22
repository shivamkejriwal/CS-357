import pylab as pylab
import numpy as np


x = np.linspace(0,5,100)
y = ((5-x)*np.exp(x))-5
pylab.plot(x,y)
pylab.show()
    
