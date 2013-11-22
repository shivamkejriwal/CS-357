from scipy import linalg as la
import numpy as np
x = np.roots([10,5,-5,1])
print x
a = la.companion([10,5,-5,1])
print a
b=la.eig(a)
print b
