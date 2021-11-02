import matplotlib.pyplot as plt
from math import sin, cos, pi

def f1(o):
    return 3*cos(3*o)-cos(o)

def f2(o):
    return 3*sin(3*o)-sin(o)

def f3(o):
    return -7*cos(2*o)+2*cos(o)-1

def f4(o):
    return -7*sin(2*o)+2*sin(o)

n=100

angle=[pi*i/(n/2) for i in range(n)]

u=[0 for i in range(len(angle)+1)]
v=[0 for i in range(len(angle)+1)]

for i in range(len(angle)):
    u[i]=(f1(angle[i])*f3(angle[i])+f2(angle[i])*f4(angle[i]))/(f3(angle[i])**2+f4(angle[i])**2)
    v[i]=(f2(angle[i])*f3(angle[i])-f1(angle[i])*f4(angle[i]))/(f3(angle[i])**2+f4(angle[i])**2)
v[-1]=v[0]
u[-1]=u[0]

a=(3*(0.1**3-0.1))/(-7*0.1**2+2*0.1-1)

if a>=u[0] and a<=u[int(n/2)]:
    print("inside")
    plt.fill_between(u,v, color='g')
else:
    plt.gca().set_facecolor('g')
    plt.fill_between(u,v, color='w')

plt.plot(u,v)
plt.plot(a, 0, marker='o',color='r', markersize=5)

plt.show()
