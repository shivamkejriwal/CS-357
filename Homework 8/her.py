import numpy as np
import scipy as sp
from scipy import linalg as LA


def getDiagMatrix(mat):
	e_vals, e_vecs = LA.eig(B)
	print e_vals
	S2 = np.zeros(A.shape)
	for i in range((S2.shape)[1]):
		S2[i][i]=e_vals[i]
	return S2



#A = np.mat('2 2; -1 1')
A = np.mat('2 -2; 1 1')
ATA =np.transpose(A)*A
print "transpose(A)*A:\n",ATA
e_vals, e_vecs = LA.eig(ATA)
vT = np.array(e_vecs)
print "vT:\n",vT,"--------"
for i in range(e_vals.size):
	temp1= np.array(ATA-e_vals[i]*np.identity(e_vals.size))
	temp2= vT[:,i]
	print "temp1:\n",temp1
	print "eig:",e_vals[i]
	print temp2
	#print temp1* temp2

##S2 = getDiagMatrix(A)
##print S2





#------------------------
#A = np.array([[2,2],
#			[-1,1]])
#U = A.getH();
#D = (np.diag(A))
#print U
#print D

