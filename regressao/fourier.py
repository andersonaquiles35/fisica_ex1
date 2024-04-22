import numpy as np


A = np.array([[1, -0.2146, 0.9766],
	      [1, -0.0094, -0.999],
	      [1, 0.0939, 0.99557]])

C=np.array([[1],
	    [0],
	    [1]])

AI=(np.linalg.inv(A))

a = (AI@C)[0][0]
b = (AI@C)[1][0]
c = (AI@C)[2][0]
print(a)
print(b)
print(c)
