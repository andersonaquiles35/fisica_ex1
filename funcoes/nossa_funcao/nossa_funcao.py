from sympy import integrate, diff, Symbol
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0, 3, 0.01)

def a(x):
	return x*0+1

def v(x):
	return x

def z(x):
	return (x**2)/2

plt.plot(np.array([-0.045, 100]), np.array([-0.045,0]), 'black')
plt.plot(np.array([0.009, 0.009]),  np.array([-10,10]), 'black')

plt.plot(x,v(x),color="blue", linewidth=3.5, label='v(x)')
plt.plot(x,z(x),color="red", linewidth=3.5, label='z(x)')
plt.plot(x,a(x),color="black", linewidth=3.5, label='a(x)')

plt.xlabel('t (s)')

plt.grid(True)
plt.title("Gráfico Geral")
#plt.savefig('a.png', transparent=True)

plt.axis([0,3,-0.05,4.55])
plt.legend(loc='upper left')
plt.show()
