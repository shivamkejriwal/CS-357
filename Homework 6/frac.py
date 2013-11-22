import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


imgx = 512
imgy = 512
rgb = np.zeros((imgx, imgy, 3), dtype=np.uint8)

# drawing area
xa = -1.0
xb = 1.0
ya = -1.0
yb = 1.0

maxIt = 20 # max iterations allowed
h = 1e-6 # step size for numerical derivative
eps = 1e-3 # max error allowed

# put any complex function here to generate a fractal for it!
def f1(z):
	return z * z * z - 1.0
	
def f2(z):
	return z*z*z-2*z+2	

def f3(z):
	return 4*z*z*z+3*z*z+2*z+1
	
def f(x):
	return f3(x)	

# draw the fractal
finalZ = 0
for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1) + ya
    for x in range(imgx):
        zx = x * (xb - xa) / (imgx - 1) + xa
        z = complex(zx, zy)
        for i in range(maxIt):
            # complex numerical derivative
            dz = (f(z + complex(h, h)) - f(z)) / complex(h, h)
            z0 = z - f(z) / dz # Newton iteration
            if abs(z0 - z) < eps: # stop when close enough to any root
            	finalZ=z0
                break
            z = z0
            rgb[x,y,0]=i % 4 * 64
            rgb[x,y,1]=i % 8 * 32
            rgb[x,y,2]=i % 16 * 16
        
print 'root is: {0}'.format(finalZ)
plt.imshow(rgb)
plt.show()
