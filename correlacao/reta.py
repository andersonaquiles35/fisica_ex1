import numpy as np


x1=1
x2=2
x3=3
x4=4
x5=5
x6=6


A = np.array([[1, x1],
	      [1, x2],
	      [1, x3],
	      [1, x4],
	      [1, x5],
	      [1, x6]])

C=A.T@np.array([[2],
	    [5],
	    [6],
	    [15],
	    [20],
	    [30]])

AI=(np.linalg.inv(A.T@A))

d = str((AI@C)[1][0])
e = str((AI@C)[0][0])

print(d)
print(e)
