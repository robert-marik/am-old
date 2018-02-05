from pylab import *
from mpl_toolkits.mplot3d import Axes3D

plt.xkcd()

xmin, xmax, ymin, ymax, zmin, zmax= -4,4,-4,4,-2,2

outputfile="3D_graf_b.png"
fig = figure()
ax = Axes3D(fig)
X = np.arange(xmin, xmax, 0.25)
Y = np.arange(ymin, ymax, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

ax.set_xlabel('x')
ax.set_xlim(xmin, xmax)
ax.set_ylabel('y')
ax.set_ylim(ymin, ymax)
ax.set_zlabel('f(x,y)')
ax.set_zlim(zmin, zmax)


ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

plt.savefig(outputfile,bbox_inches="tight", pad_inches=.15)
