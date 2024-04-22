from sympy import integrate, diff, Symbol
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,3, 0.01)

def a(x):
	y = -0.5+x*0
	return y

def v(x):
	y = -0.5*x + 1.0
	return y

def z(x):
	y = -0.25*x**2 + 1.0*x
	return y

plt.plot(np.array([0, 10]), np.array([0,0]), 'black')
plt.plot(np.array([0.015, 0.015]), np.array([-6,2]), 'black')

plt.plot(x,v(x),color="blue", linewidth=3.5, label='v(t) [m s⁻¹]')
plt.plot(x,z(x),color="red", linewidth=3.5, label='z(t) [m]')
plt.plot(x,a(x),color="black", linewidth=3.5, label='a(t) [m s⁻²]')

plt.xlabel('t (s)')

plt.grid(True)
plt.title("Gráfico Geral")

plt.axis([0,3,-1.05,1.05])
plt.legend(loc='lower left')
plt.show()
