import numpy as np
import matplotlib.pyplot as plt

plt.figure(1,(8,8)) 

plt.xkcd()

xmin, xmax, ymin, ymax = 1, 4, -1, 2

def f(x,y): return ((x**2)*y-x*(y**3))

def dfx(x,y): return (2*x*y-(y**3))
def dfy(x,y): return (x**2-x*3*(y**2))


delta = 0.05
x = np.arange(xmin, xmax, delta)
y = np.arange(ymin, ymax, delta)
X, Y = np.meshgrid(x, y)

Z=f(X,Y)

CS = plt.contour(X, Y, Z, 30)


delta = 0.2
x = np.arange(xmin, xmax, delta)
y = np.arange(ymin, ymax, delta)
X, Y = np.meshgrid(x, y)

U = dfx(X,Y)/np.sqrt(dfx(X,Y)**2+dfy(X,Y)**2)
V = dfy(X,Y)/np.sqrt(dfx(X,Y)**2+dfy(X,Y)**2)

plt.quiver(X,Y,U,V, color='gray')

plt.axes().set_aspect('equal', 'datalim')
plt.savefig("gradient.svg")
plt.savefig("gradient.png")
