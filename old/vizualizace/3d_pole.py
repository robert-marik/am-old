# Using the magic encoding
# -*- coding: utf-8 -*-


bez_znacek = True
#bez_znacek = False

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import *
import numpy as np

plt.xkcd()

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.view_init(elev=40)


# pocatecni hodnoty
xmin=0
xmax=1
ymin=0
ymax=1
zmin=0
zmax=1

outputfile="3d_pole"

X,Y = np.meshgrid( np.arange(xmin,xmax,.2),np.arange(xmin,xmax,.2) )

def Utemp(x,y,z):
    return 1+x
def Vtemp(x,y,z):
    return 0
def Wtemp(x,y,z):
    return z+x+y


delka=0.1
def U(x,y,z):
    return Utemp(x,y,z)/sqrt(Vtemp(x,y,z)**2+Utemp(x,y,z)**2+Wtemp(x,y,z)**2)*delka
def V(x,y,z):
    return Vtemp(x,y,z)/sqrt(Vtemp(x,y,z)**2+Utemp(x,y,z)**2+Wtemp(x,y,z)**2)*delka
def W(x,y,z):
    return Wtemp(x,y,z)/sqrt(Vtemp(x,y,z)**2+Utemp(x,y,z)**2+Wtemp(x,y,z)**2)*delka


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

plt.setp(ax, xticks=[], yticks=[], zticks=[])

imax=100
jmax=100

i=10
j=40

color=['red','blue','black','green']
zposs=[0, 0.3, 0.6, 0.9]

np.random.seed(15)

for i in range(0,250):
    xpos=np.random.rand()
    ypos=np.random.rand()
    zpos=np.random.rand()
    #print xpos,ypos,zpos
    a = Arrow3D([xpos,xpos+U(xpos,ypos,zpos)],[ypos,ypos+V(xpos, ypos,zpos)],[zpos,zpos+W(xpos, ypos, zpos)], mutation_scale=15, lw=1, arrowstyle="->", color="#006131", zorder=-4, alpha=0.65)
    ax.add_artist(a)

ax.set_xlabel('x')
ax.set_xlim(xmin, xmax)
ax.set_ylabel('y')
ax.set_ylim(ymin, ymax)
ax.set_zlabel('z')
ax.set_zlim(zmin, zmax)

ax.view_init(elev=30., azim=294)

plt.savefig(outputfile+".png",bbox_inches="tight", pad_inches=.15)
plt.savefig(outputfile+".svg",bbox_inches="tight", pad_inches=.15)

