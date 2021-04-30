# Using the magic encoding
# -*- coding: utf-8 -*-


import sys
if len(sys.argv) > 1:
    priklad = sys.argv[1]
else:
    priklad = "1"

#import matplotlib
#matplotlib.rc('text', usetex=False)
#matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{euler,amsmath}"]


animovat=True
animovat=False
bez_znacek = True
#bez_znacek = False
tecna_rovina_kreslit = True

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import *
import numpy as np
from  matplotlib.patches import Rectangle
import sympy

plt.xkcd()

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.view_init(elev=40)


# pocatecni hodnoty
xmin=0
xmax=1.55
ymin=-0.8
ymax=.8
zmin=0
zmax=0.17
tmin=0
tmax=1

outputfile="krivkovy_integral_druheho_druhu_"+str(priklad)+".png" # jmeno vystupniho souboru

X,Y = np.meshgrid( np.arange(xmin,xmax,.2),np.arange(xmin,xmax,.2) )


def Utemp(x,y):
    return x
def Vtemp(x,y):
    return y

def Utemp(x,y):
    return 1
def Vtemp(x,y):
    return 0


delka=0.15
def U(x,y):
    return Utemp(x,y)/sqrt(Vtemp(x,y)**2+Utemp(x,y)**2)*delka
def V(x,y):
    return Vtemp(x,y)/sqrt(Vtemp(x,y)**2+Utemp(x,y)**2)*delka


# funkce
lambdifyf = False  # true pokud je nutno derivaci funkce f prevest ze sympy do numpy
def fx(t):
    return 1.4*t

def fy(t):
    return np.cos(5*t)*t

def f(t):
    return ( U(fx(t),fy(t))*1.4+V(fx(t),fy(t))*( (-5*np.sin(5*t)*t + np.cos(5*t))) )/sqrt(1.4 ** 2 + ( ( (-5*np.sin(5*t)*t + np.cos(5*t))) )**2) 

tt = np.linspace(tmin, tmax, 300, endpoint=True)

xt = fx(tt)
yt = fy(tt)
zt = f(tt)
z0 = [0 for i in tt]

iX = np.arange(0, 1, .01)
iY = np.arange(0, 1, .01)
iX, iY = np.meshgrid(iX, iY)

iXplot = fx(tmax*iX)
iYplot = fy(tmax*iX)
iZplot = f(tmax*iX)*iY

if bez_znacek:
    plt.setp(ax, xticks=[], yticks=[], zticks=[])

ax.plot_wireframe(iXplot, iYplot, iZplot, color='gray', alpha=0.25, lw=1, cstride=1, rstride=1, zorder=-20)

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

imax=100
jmax=100

i=10
j=40

for i in range (2,imax, 10):
    for j in range (5,jmax, 10):
        xpos=(i)*(xmax-xmin)/imax+xmin
        ypos=j*(ymax-ymin)/jmax+ymin
        a = Arrow3D([xpos,xpos+U(xpos,ypos)],[ypos,ypos+V(xpos, ypos)],[0,0], mutation_scale=15, lw=1, arrowstyle="-|>", color="k", zorder=-4)
        ax.add_artist(a)

#ax.plot_surface(X, Y, Z, alpha=.41, lw=0.1, cmap='autumn', zorder=20)

ax.plot(xt, yt, zt, color='red')
ax.plot(xt, yt, z0, color='blue', zorder=10)
b=298
e=299
a=Arrow3D([xt[b],xt[e]], [yt[b],yt[e]], [0,0], lw=3, mutation_scale=30, arrowstyle="->", color='blue', zorder=10)
ax.add_artist(a)

ax.set_xlabel('x')
ax.set_xlim(xmin, xmax)
ax.set_ylabel('y')
ax.set_ylim(ymin, ymax)
ax.set_zlabel('')
ax.set_zlim(zmin, zmax)

ax.view_init(elev=30., azim=294)

plt.savefig(outputfile,bbox_inches="tight", pad_inches=.15)

if animovat:
    #    ax.axis("off")
    for ii in xrange(0,360,4):
        ax.view_init(elev=10., azim=ii)
        jmeno="000"+str(ii)
        jmeno=jmeno[-3:]
        plt.savefig("movie"+jmeno+".png")


# convert -delay 20 movie*.png animation.gif && rm movie
