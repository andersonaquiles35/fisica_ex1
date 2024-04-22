from sympy import integrate, diff, Symbol, sin, cos
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10, 0.01)

def z(x):
	y = 0.50129+0.50021*np.sin(x*0.9434)-0.002357*np.cos(x*0.9434)+1.005880e-05*np.sin(2*x*0.9434)+0.0010670*np.cos(2*x*0.9434)
	return y

def v(x):
	y = 0.0022235938*np.sin(0.9434*x) - 0.0020132156*np.sin(1.8868*x) + 0.471898114*np.cos(0.9434*x) + 1.897894384e-5*np.cos(1.8868*x)
	return y

def a(x):
	y = -0.4451886807476*np.sin(0.9434*x) - 3.5809471237312e-5*np.sin(1.8868*x) + 0.00209773839092*np.cos(0.9434*x) - 0.00379853519408*np.cos(1.8868*x)
	return y

plt.plot(np.array([0, 10]), np.array([0,0]), 'black')
plt.plot(np.array([0.05, 0.05]),  np.array([-6,2]), 'black')

plt.plot(x,v(x),color="blue", linewidth=3.5, label='v(t) [m s⁻¹]')
plt.plot(x,z(x),color="red", linewidth=3.5, label='z(t) [m]')
plt.plot(x,a(x),color="black", linewidth=3.5, label='a(t) [m s⁻²]')

plt.xlabel('t (s)')

plt.grid(True)
plt.title("Gráfico Geral")

plt.axis([0,10,-1.1,1.1])
plt.legend(loc='lower left')
plt.show()
