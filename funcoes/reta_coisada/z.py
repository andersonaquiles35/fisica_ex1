import matplotlib.pyplot as plt
import numpy as np

p_dt = open('data.txt')

zz=[]
t=[]
c=0
passo=0.03

for dt in p_dt.readlines():
	dt = float(dt.replace('\n', '').replace('\r', ''))/100
	if dt <= 1:
		zz.append(dt)

for i in range(0,len(zz)):
	t.append(float(round(c, 3)))
	c=c+passo

print(len(t))

plt.scatter(np.array(t), np.array(zz), color='black', s=4)

# Parte inicial
plt.plot(np.arange(0,1.9,0.001), 1+np.arange(0,1.9,0.001)*(-0.2), 'red', linewidth=3.5)   # z - espaço

# Primeira quebra
x1=np.arange(1.9,2.0,0.001)
xt=x1-1.9

yz1=-0.2*xt+((xt**3)/6)*(0.968/0.1)+0.62
plt.plot(x1, yz1, color="red", linewidth=3.5)

x1=np.arange(2.0,2.1,0.001)
xt=x1-2.0

yz1=-0.15*xt-((xt**3)/6)*(0.968/0.1)+(0.968*(xt)**2)/2+0.6
plt.plot(x1, yz1, color="red", label='z(t)', linewidth=3.5)

# Parte do meio
plt.plot(np.arange(2.1,3.9,0.001), 0.588+np.arange(2.1-2.1,3.9-2.1,0.001)*(-0.1), 'red', linewidth=3.5)   # z - espaço

# Segunda quebra
x1=np.arange(3.9,4.0,0.001)
xt=x1-3.9

yz1=-0.1*xt-((xt**3)/6)*(0.968/0.1)+0.408
plt.plot(x1, yz1, color="red", linewidth=3.5)
###
x1=np.arange(4.0,4.1,0.001)
xt=x1-4.0

yz1=-0.15*xt+((xt**3)/6)*(0.968/0.1)+(0.968*(xt)**2)/2+0.3963
plt.plot(x1, yz1, color="red", linewidth=3.5)

# Parte Final
plt.plot(np.arange(4.1,6.0,0.001), 0.38775+np.arange(0,1.901,0.001)*(-0.2), 'red', linewidth=3.5)   # z - espaço

plt.xlabel('t (s)')

plt.ylabel('z (m)')
plt.grid(True)
plt.title("Espaço")
#plt.savefig('a.png', transparent=True)

plt.axis([0,6,-1,1])
plt.legend(loc='lower left')
plt.show()
