import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.figure(1,(8,8)) 

plt.xkcd()

xmin, xmax, ymin, ymax = 1.5, 3, 0, 1.5
x0,y0 = 2,1

def f(x,y): return ((x**2)*y-x*(y**3)-2)

def dfx(x,y): return (2*x*y-(y**3))
def dfy(x,y): return (x**2-x*3*(y**2))


delta = 0.05
x = np.arange(xmin, xmax, delta)
y = np.arange(ymin, ymax, delta)
X, Y = np.meshgrid(x, y)

Z=f(X,Y)

plt.contourf(X, Y, Z, [-3,-2,-1,0,1,2,3,4,5], cmap=cm.jet)
CS=plt.contour(X, Y, Z, [-3,-2,-1,1,2,3,4,5], cmap=cm.gray)
plt.clabel(CS, inline=1, fontsize=15, fmt='%1.1f')
CS=plt.contour(X, Y, Z, [0], linewidths=[4], colors='gray')
#plt.clabel(CS, inline=1, fontsize=15)

plt.plot([x0],[y0],'ro', markersize=10, zorder=20)
zmenseni=0.2
plt.arrow(x0, y0, zmenseni*dfx(x0,y0), zmenseni*dfy(x0,y0), lw=4, zorder=10)

plt.arrow(x0, y0, -zmenseni*dfy(x0,y0), zmenseni*dfx(x0,y0), lw=4, zorder=10, color='red')
plt.arrow(x0, y0, 3*zmenseni*dfy(x0,y0), -3*zmenseni*dfx(x0,y0), lw=4, zorder=10, color='red')


plt.axes().set_aspect('equal', 'datalim')
plt.savefig("tecna.svg")
plt.savefig("tecna.png")
