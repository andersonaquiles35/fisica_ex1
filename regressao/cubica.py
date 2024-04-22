import numpy as np

x1=1
x2=2
x3=3
x4=4
x5=5
x6=6

A = np.array([[1, x1, x1**2, x1**3],
	      [1, x2, x2**2, x2**3],
	      [1, x3, x3**2, x3**3],
	      [1, x4, x4**2, x4**3],
	      [1, x5, x5**2, x5**3],
	      [1, x6, x6**2, x6**3]])

C=A.T@np.array([[2],
	    [5],
	    [6],
	    [15],
	    [20],
	    [30]])

AI=(np.linalg.inv(A.T@A))

b = str((AI@C)[3][0])
c = str((AI@C)[2][0])
d = str((AI@C)[1][0])
e = str((AI@C)[0][0])

print(b)
print(c)
print(d)
print(e)
