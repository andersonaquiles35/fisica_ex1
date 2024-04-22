import matplotlib.pyplot as plt
import numpy as np

# Parte inicial
plt.plot(np.arange(0,1.9,0.001), 1+np.arange(0,1.9,0.001)*(-0.2), 'red', linewidth=3.5)   # z - espaço
plt.plot(np.arange(0,1.9,0.001), -0.2+np.arange(0,1.9,0.001)*0, 'blue', linewidth=3.5)    # v - velocidade
plt.plot(np.arange(0,1.9,0.001), np.arange(0,1.9,0.001)*0, 'black', linewidth=3.5)       # a - aceleração

# Primeira quebra
x1=np.arange(1.9,2.0,0.001)
xt=x1-1.9
ya1=(xt*(0.968/0.1))
plt.plot(x1, ya1, color="black", linewidth=3.5)

yv1=-0.2+((xt**2)/2)*(0.968/0.1)
plt.plot(x1, yv1, color="blue", linewidth=3.5)

yz1=-0.2*xt+((xt**3)/6)*(0.968/0.1)+0.62
plt.plot(x1, yz1, color="red", linewidth=3.5)

x1=np.arange(2.0,2.1,0.001)
xt=x1-2.0
ya1=-(xt*(0.968/0.1))+0.968
plt.plot(x1, ya1, color="black", label='a(t) [m s⁻²]', linewidth=3.5)

yv1=-0.15-((xt**2)/2)*(0.968/0.1)+0.968*xt
plt.plot(x1, yv1, color="blue", label='v(t) [m s⁻¹]', linewidth=3.5)

yz1=-0.15*xt-((xt**3)/6)*(0.968/0.1)+(0.968*(xt)**2)/2+0.6
plt.plot(x1, yz1, color="red", label='z(t) [m]', linewidth=3.5)

# Parte do meio
plt.plot(np.arange(2.1,3.9,0.001), 0.588+np.arange(2.1-2.1,3.9-2.1,0.001)*(-0.1), 'red', linewidth=3.5)   # z - espaço
plt.plot(np.arange(2.1,3.9,0.001), -0.1+np.arange(2.1,3.9,0.001)*0, 'blue', linewidth=3.5)    # v - velocidade
plt.plot(np.arange(2.1,3.9,0.001), np.arange(2.1,3.9,0.001)*0, 'black', linewidth=3.5)       # a - aceleração

# Segunda quebra
x1=np.arange(3.9,4.0,0.001)
xt=x1-3.9
ya1=-(xt*(0.968/0.1))
plt.plot(x1, ya1, color="black", linewidth=3.5)

yv1=-0.1-((xt**2)/2)*(0.968/0.1)
plt.plot(x1, yv1, color="blue", linewidth=3.5)

yz1=-0.1*xt-((xt**3)/6)*(0.968/0.1)+0.408
plt.plot(x1, yz1, color="red", linewidth=3.5)
###
x1=np.arange(4.0,4.1,0.001)
xt=x1-4.0
ya1=(xt*(0.968/0.1))-0.968
plt.plot(x1, ya1, color="black", linewidth=3.5)

yv1=-0.148399+((xt**2)/2)*(0.968/0.1)-0.968*xt
plt.plot(x1, yv1, color="blue", linewidth=3.5)

yz1=-0.15*xt+((xt**3)/6)*(0.968/0.1)+(0.968*(xt)**2)/2+0.3963
plt.plot(x1, yz1, color="red", linewidth=3.5)

# Parte Final
plt.plot(np.arange(4.1,6.0,0.001), 0.38775+np.arange(0,1.901,0.001)*(-0.2), 'red', linewidth=3.5)   # z - espaço
plt.plot(np.arange(4.1,6.0,0.001), -0.2+np.arange(0,1.901,0.001)*0, 'blue', linewidth=3.5)    # v - velocidade
plt.plot(np.arange(4.1,6.0,0.001), np.arange(0,1.901,0.001)*0, 'black', linewidth=3.5)       # a - aceleração

plt.xlabel('t (s)')

plt.grid(True)
plt.title("Gráfico Geral")
#plt.savefig('a.png', transparent=True)

plt.axis([0,6,-1,1])
plt.legend(loc='lower left')
plt.show()
