import numpy as np
import matplotlib.pyplot as plt


fig=plt.figure(1,(8,8)) 
ax = fig.gca()
plt.xkcd()

xmin, xmax, ymin, ymax = -3, 3, -3, 3
n, ntex, limit = 1.0/2, r'\frac{1}{2}', 0.1
n, ntex, limit = 1, r'', 1.2

def dfx(x,y): return (-y/(x**2+y**2)**n)
def dfy(x,y): return (x/(x**2+y**2)**n)
def kreslit(x,y): return(x**2+y**2>limit)

delta = 0.2
X,Y,U,V=[],[],[],[]

for x in np.arange(xmin, xmax, delta):
    for y in np.arange(ymin, ymax, delta):
        if kreslit(x,y):
            X+=[x]
            Y+=[y]
            U+=[dfx(x,y)]
            V+=[dfy(x,y)]

plt.quiver(X,Y,U,V, color='b')
plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.title(r'$\vec F=\frac {1}{(x^2+y^2)^{'+ntex+r'}}(-y\vec i+x\vec j)$')

ax.set_aspect('equal', 'datalim')
plt.savefig("pole.svg")
plt.savefig("pole.pdf")
plt.savefig("pole.png")
