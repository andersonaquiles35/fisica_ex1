import matplotlib.pyplot as plt
import numpy as np

p_dt = open('data.txt')

zz=[]
vv=[]
aa=[]
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
for i in range(0,len(zz)-1):
	v = (zz[i+1]-zz[i])/passo
	vv.append(v)

vv.append(v)

for i in range(0,len(vv)-1):
	a = (vv[i+1]-vv[i])/passo
	aa.append(a)

aa.append(a)

print(len(t))

plt.scatter(np.array(t), np.array(aa), color='black', s=4)

# Parte inicial
plt.plot(np.arange(0,1.9,0.001), np.arange(0,1.9,0.001)*0, 'black', linewidth=3.5)       # a - aceleração

# Primeira quebra
x1=np.arange(1.9,2.0,0.001)
xt=x1-1.9
ya1=(xt*(0.968/0.1))
plt.plot(x1, ya1, color="black", linewidth=3.5)

x1=np.arange(2.0,2.1,0.001)
xt=x1-2.0
ya1=-(xt*(0.968/0.1))+0.968
plt.plot(x1, ya1, color="black", label='a(t)', linewidth=3.5)

# Parte do meio
plt.plot(np.arange(2.1,3.9,0.001), np.arange(2.1,3.9,0.001)*0, 'black', linewidth=3.5)       # a - aceleração

# Segunda quebra
x1=np.arange(3.9,4.0,0.001)
xt=x1-3.9
ya1=-(xt*(0.968/0.1))
plt.plot(x1, ya1, color="black", linewidth=3.5)
###
x1=np.arange(4.0,4.1,0.001)
xt=x1-4.0
ya1=(xt*(0.968/0.1))-0.968
plt.plot(x1, ya1, color="black", linewidth=3.5)

# Parte Final
plt.plot(np.arange(4.1,6.0,0.001), np.arange(0,1.901,0.001)*0, 'black', linewidth=3.5)       # a - aceleração

plt.xlabel('t (s)')
plt.ylabel('a (m s⁻²)')

plt.grid(True)
plt.title("Aceleração")
#plt.savefig('a.png', transparent=True)

plt.axis([0,6,-15,15])
plt.legend(loc='lower left')
plt.show()
