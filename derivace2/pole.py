import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(1,(8,8)) 
ax = fig.gca()
plt.xkcd()

xmin, xmax, ymin, ymax = -3, 3, -3, 3
n, limit = 1.0/2, 1

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
      
ax.set_aspect('equal', 'datalim')
plt.savefig("pole.svg")
plt.savefig("pole.png")
