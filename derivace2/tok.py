import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

fig=plt.figure(1,(8,4)) 

ax = fig.gca()

plt.xkcd()

xmin, xmax, ymin, ymax = -1, 3, -1, 1

def f(x,y): return ((x**2)*y-x*(y**3))

def dfx(x,y): return (3*(1-y)*(1+y))
def dfy(x,y): return (0)


delta = 0.05
#x = np.arange(xmin, xmax, delta)
#y = np.arange(ymin, ymax, delta)
#X, Y = np.meshgrid(x, y)
#Z=f(X,Y)
#CS = plt.contour(X, Y, Z, 30)


delta = 0.2
x = np.arange(xmin, xmax, 0.6)
y = np.arange(ymin, ymax, 0.2)
X, Y = np.meshgrid(x, y)

U = dfx(X,Y)
V = dfy(X,Y)

plt.quiver(X,Y,U,V, color='b')


e1 = patches.Ellipse((2, -0.03), 0.05, 0.3, angle=90, linewidth=2, fill=True, zorder=2, color='r')
e2 = patches.Ellipse((1.1, -0.2), 0.05, 0.3, angle=-58, linewidth=2, fill=True, zorder=2, color='r')
e3 = patches.Ellipse((-0.5, -0.9), 0.05, 0.3, angle=0, linewidth=2, fill=True, zorder=2, color='r')
e4 = patches.Ellipse((0.2, -0.5), 0.05, 0.3, angle=-30, linewidth=2, fill=True, zorder=2, color='r')

plt.text(-0.5-0.1, -1, '1.')
plt.text(0.2-0.1, -0.5, '2.')
plt.text(1.1-0.1, -0.2, '3.')
plt.text(2, 0.05, '4.')
plt.axis('off')
plt.plot([xmin,xmax], [ymin,ymin], color='g')
plt.plot([xmin,xmax], [ymax,ymax], color='g')

ax.add_patch(e1)
ax.add_patch(e2)
ax.add_patch(e3)
ax.add_patch(e4)

plt.axes().set_aspect('equal', 'datalim')
plt.savefig("tok.svg")
plt.savefig("tok.png")
