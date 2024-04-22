import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10, 0.01)

def v(x):
	y = (-0.9797201553931814) + (0.02383178644072359*x) + (0.10350634333491371*x**2) + (-0.021978356641056962*x**3) + (0.0003145243114115459*x**4) + (0.00010642708773228593*x**5)
	return y

def z(x):
	y=2+1.7737847955381e-5*x**6 + 6.29048622823092e-5*x**5 - 0.00549458916026424*x**4 + 0.0345021144449712*x**3 + 0.0119158932203618*x**2 - 0.979720155393181*x
	return y

def a(x):
	y=0.00053213543866143*x**4 + 0.00125809724564618*x**3 - 0.065935069923171*x**2 + 0.207012686669828*x + 0.0238317864407236
	return y

plt.plot(np.array([0, 10]), np.array([0,0]), 'black')
plt.plot(np.array([0.05, 0.05]),  np.array([-6,2]), 'black')


plt.plot(x,v(x),color="blue", linewidth=3.5, label='v(t) [m s⁻¹]')
plt.plot(x,z(x),color="red", linewidth=3.5, label='z(t) [m]')
plt.plot(x,a(x),color="black", linewidth=3.5, label='a(t) [m s⁻²]')

plt.xlabel('t (s)')

plt.grid(True)
plt.title("Gráfico Geral")

plt.axis([0,10,-4,2])
plt.legend(loc='lower left')

plt.show()
