import numpy as np


x1=1
x2=2
x3=3
x4=4
x5=5
x6=6


A = np.array([[1, x1, x1**2],
	      [1, x2, x2**2],
	      [1, x3, x3**2],
	      [1, x4, x4**2],
	      [1, x5, x5**2],
	      [1, x6, x6**2]])

C=A.T@np.array([[2],
	    [5],
	    [6],
	    [15],
	    [20],
	    [30]])

AI=(np.linalg.inv(A.T@A))

a = str((AI@C)[2][0])
b = str((AI@C)[1][0])
c = str((AI@C)[0][0])
print(a+"x**2 "+b+'x '+c)
