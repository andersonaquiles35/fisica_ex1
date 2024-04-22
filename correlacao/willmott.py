#!/usr/bin/python3

#Física experimental - IMPATech
import numpy as np

ll = open('data.txt','r').read()
list = ll.replace('\n', ' ').replace(',', '.').split(' ')
c=1
t=[]
z=[]
v=[]
a=[]
for i in list:
	if i=='':
		pass
	elif c==1:
		t.append(float(i)-2.65)
		c=c+1
	elif c==2:
		z.append(float(i)-2.264+0.4)
		c=c+1
	elif c==3:
		v.append(float(i))
		c=c+1
	elif c==4:
		a.append(float(i))
		c=1
#z=a
zz = []
for x in t:
'	y = (x**2)/2 #função
	zz.append(y)
c=0
b=0
O=0
for j in z:
	O = O+j
O = O/len(z)
for i in range(0,len(z)-1):
	c = c+(z[i]-zz[i])**2
	f = z[i]-O
	if f<0:
		f = f*(-1)
	g = zz[i]-O
	if g<0:
		g = g*(-1)
	b = b+(g+f)**2
coeficiente = 1-c/b
print(coeficiente)



