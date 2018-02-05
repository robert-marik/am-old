from pylab import *
from numpy import ma

plt.xkcd()
X,Y = meshgrid( arange(-1,1,.2),arange(-1,1,.2) )
U = -Y
V = X


figure(figsize=(8,8))
plt.axes().set_aspect('equal', 'datalim')

plt.quiver(X,Y,U,V, color='#02ff02')
l,r,b,t = axis()
dx, dy = r-l, t-b
axis([l-0.05*dx, r+0.05*dx, b-0.05*dy, t+0.05*dy])


plt.savefig("2d_pole.png",bbox_inches="tight", pad_inches=.15)
plt.savefig("2d_pole.svg",bbox_inches="tight", pad_inches=.15)

