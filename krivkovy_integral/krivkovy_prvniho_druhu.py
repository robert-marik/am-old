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
import numpy as np
from  matplotlib.patches import Rectangle
import sympy

plt.xkcd()

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.view_init(elev=40)


# pocatecni hodnoty
xmin=-1
xmax=1.55
ymin=-0.8
ymax=1.5
zmin=0
zmax=10
tmin=0
tmax=1

outputfile="krivkovy_integral_prvniho_druhu_"+str(priklad)+".png" # jmeno vystupniho souboru


# funkce
lambdifyf = False  # true pokud je nutno derivaci funkce f prevest ze sympy do numpy
def f(x,y):
    return 10-2*(x**2+y**2)

def fx(t):
    return 1.4*t

def fy(t):
    return np.cos(5*t)*t

tt = np.linspace(tmin, tmax, 300, endpoint=True)

xt = fx(tt)
yt = fy(tt)
zt = f(fx(tt),fy(tt))
z0 = [0 for i in tt]


X = np.arange(xmin, xmax, .05)
Y = np.arange(ymin, 0.5, .05)
X, Y = np.meshgrid(X, Y)
Z = f(X,Y)

#iX = np.linspace(0,1,0.1)
#iY = np.linspace(0,1,0.1)
iX = np.arange(0, 1, .01)
iY = np.arange(0, 1, .01)
iX, iY = np.meshgrid(iX, iY)

iXplot = fx(tmax*iX)
iYplot = fy(tmax*iX)
iZplot = f(fx(tmax*iX),fy(tmax*iX))*iY

if bez_znacek:
    plt.setp(ax, xticks=[], yticks=[], zticks=[])

#plt.title(u"Krivkovy integral prvniho druhu", loc='center')

#ax.plot_surface(iXplot, iYplot, iZplot, alpha=.5, lw=1, rstride=100, cstride=100)
ax.plot_wireframe(iXplot, iYplot, iZplot, color='gray', alpha=0.3, lw=1, cstride=1, rstride=1)

ax.plot_surface(X, Y, Z, alpha=.11, lw=0.1, cmap='autumn')

if not animovat:
    #ax.plot(xt, yt, zt, color='red', zorder=1)
    ax.plot(xt, yt, z0, color='blue', zorder=-1)

ax.set_xlabel('x')
ax.set_xlim(xmin, xmax)
ax.set_ylabel('y')
ax.set_ylim(ymin, ymax)
ax.set_zlabel('f(x,y)')
ax.set_zlim(zmin, zmax)

ax.view_init(elev=10., azim=294)

plt.savefig(outputfile,bbox_inches="tight", pad_inches=.15)

u1 = range(-80,0,4)
u2 = [i for i in reversed(u1)]

if animovat:
    #    ax.axis("off")
    cislo = 0
    for ii in u1+u2:
        cislo = cislo + 1 
        imin=80
        imax=190
        #ax.plot(xt[imin:imax], yt[imin:imax], z0[imin:imax], color='gray', alpha=0.6)
        ax.view_init(elev=10., azim=ii)
        jmeno="000"+str(cislo)
        jmeno=jmeno[-3:]
        plt.savefig("movie"+jmeno+".png")


# convert -delay 20 movie*.png animation.gif && rm movie
