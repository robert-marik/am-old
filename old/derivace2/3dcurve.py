import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()

fig = plt.figure()

ax = fig.gca(projection='3d')
theta = np.linspace(0, 2 * np.pi, 100)

nasobek=6
x = 10 + nasobek * np.sin(theta)
y = 10 + nasobek * np.cos(theta)
#z = y**3/8-x**2
z=(y-.1*x)**2

dz = [-2*i for i in range(0,100)]
dx = nasobek * (np.cos(theta))
dy = nasobek * (- np.sin(theta))
#dz = 3*y**2/8*dy-2*x*dx
dz = (dy-0.1*dx)*2*(y-0.1*x)

X = np.arange(0, 20, 1)
Y = np.arange(0, 20, 1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
#Z = Y**3/8-X**2
Z = (Y-0.1*X)**2

from matplotlib import cm

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,  cmap='hot',  
        linewidth=0.1, alpha=0.95)

ax.plot(x, y, z, color='red', lw=5)

#draw a vector
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

for i in range(5,100, 8):
    a = Arrow3D([x[i],x[i]+dx[i]],[y[i],y[i]+dy[i]],[z[i],z[i]+dz[i]], mutation_scale=20, lw=1.5, arrowstyle="-|>", color="b", zorder=4)
    ax.add_artist(a)

#plt.show()
plt.savefig("3dcurve.png",bbox_inches="tight", pad_inches=.15)

