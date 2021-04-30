# Using the magic encoding
# -*- coding: utf-8 -*-


import sys
if len(sys.argv) > 1:
    priklad = sys.argv[1]
else:
    priklad = "1"

#priklad = "4"
animovat=False
#animovat=True
bez_znacek = True
#bez_znacek = False
tecna_rovina_kreslit = True

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import exp,sin,cos
from  matplotlib.patches import Rectangle
import sympy

plt.xkcd()

# pocatecni hodnoty
xmin=-2.5
xmax=5.5
ymin=-4
ymax=3
zmin=-35
zmax=5

x0=1 # bod na vrstevnici - souradnice x
start_fsolve = 0.5*(ymin+ymax) # bod na vrstevnici - pocatecni odhad pro hledani souradnice y

vrstevnice=[-12,-9,-3,-6,3,6,9]
delkax=2    # delka obdelnicku ve smeru x
delkay=1.3  # delka obdelnicku ve smeru y

outputfile="implicitni_"+str(priklad)+".png" # jmeno vystupniho souboru
posun_z=-30  # rovina ve ktere se kresli vrstevnice

# funkce
lambdifyf = False  # true pokud je nutno derivaci funkce f prevest ze sympy do numpy
def f(x,y):
    return 7-(2*x**2+y**2)+.4*(x)**3

########################################################
########################################################

if priklad == "2":
# druhy priklad
    def f(x,y):
        return 7-(x**2-y**3/2)
    delkax=2
    delkay=1
    x0=2
    start_fsolve = 0.5*(ymin+ymax)
    vrstevnice=[-12,-9,-6,-3,3,6,9,12,15,7.2]



########################################################
########################################################

if priklad == "3":

    def f(x,y):
        return 9-x**2+(1+y**4/(1+y**4))-2*y**2

    def f(x,y):
        return 9-x**2*(x+1/(1+x**2))+(1+y**4/(1+y**4))-2*y**2

    xmin=-2
    xmax=3
    ymin=-4
    ymax=2
    start_fsolve = 0.5*(ymin+ymax)
    zmin=-35
    zmax=10
    
    # bod na vrstevnici
    x0=1
    start_fsolve = 0.5*(ymin+ymax)
    vrstevnice=range(-10,10,3)
    delkax=2
    delkay=1
    posun_z=-30


########################################################
########################################################


if priklad == "4":
    def f(x,y):
        return (x**2*y-y**2*x)/10 +2
    lambdifyf = True
    xmin,xmax=-6,6
    ymin,ymax=-6,6
    zmin,zmax=0,10
    x0=3
    start_fsolve = ymin
    posun_z=0
    delkax=2
    delkay=2
    tecna_rovina_kreslit = False
    bez_znacek = False

fig = plt.figure()
ax = fig.gca(projection='3d')


# vypocet gradientu a tecne roviny
from sympy.abc import x, y
from sympy.utilities.lambdify import lambdify, implemented_function
gradfx=lambdify((x,y), f(x,y).diff(x))
gradfy=lambdify((x,y), f(x,y).diff(y))
if lambdifyf:
    f=lambdify((x,y), f(x,y), 'numpy')

# dopocitani bodu na vrstevnici
from scipy import *
from scipy import optimize
g = lambda y:f(x0,y)
try:
    y0 = optimize.fsolve(g, start_fsolve)[0]
except:
    print "nenalezeno y0"
    y0=0



def tecna_rovina(x,y):
    return f(x0,y0)+gradfx(x0,y0)*(x-x0)+gradfy(x0,y0)*(y-y0)



X = np.arange(xmin, xmax, .1)
Y = np.arange(ymin, ymax, .1)
X, Y = np.meshgrid(X, Y)
Z = f(X,Y)

X2 = np.arange(x0-delkax, x0+delkax, .1)
Y2 = np.arange(y0-delkay, y0+delkay, .1)
X2, Y2 = np.meshgrid(X2, Y2)
Z2 = tecna_rovina(X2,Y2)

if bez_znacek:
    plt.setp(ax, xticks=[], yticks=[], zticks=[])

plt.title(u'3D graf:', loc='left')

if tecna_rovina_kreslit:
    ax.plot_surface(X2, Y2, Z2, alpha=0.3, lw=0)

ax.plot_surface(X, Y, Z, alpha=.15, lw=0.1, cmap='autumn')

#ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.73)
ax.contour(X, Y, Z, zdir='z', levels=[0], offset=posun_z, colors='r')
if tecna_rovina_kreslit:
    ax.contour(X, Y, Z, levels=[0], colors='k')

ax.contour(X, Y, Z, zdir='z', levels=vrstevnice, offset=posun_z, linewidths=0.5, colors='k')
ax.contour(X2, Y2, Z2, zdir='z', levels=[0], offset=posun_z, linewidths=2, colors='b')

if tecna_rovina_kreslit:
    ax.contour(X2, Y2, Z2, levels=[0], linewidths=2, colors='b')
    ax.scatter(x0,y0,f(x0,y0), c='r')

ax.scatter(x0,y0,posun_z, c='r', zorder=10)

ax.set_xlabel('X')
ax.set_xlim(xmin, xmax)
ax.set_ylabel('Y')
ax.set_ylim(ymin, ymax)
ax.set_zlabel('Z')
ax.set_zlim(zmin, zmax)

import mpl_toolkits.mplot3d.art3d as art3d
rect1=Rectangle((x0-delkax,y0-delkay),2*delkax,2*delkay, color='#ffff99', alpha=0.3)
ax.add_patch(rect1)
art3d.pathpatch_2d_to_3d(rect1, z=posun_z, zdir="z")

ax.plot([x0+delkax,x0-delkax],[y0+delkay, y0+delkay],[posun_z,posun_z], 'k-', lw=0.8, color='black')
ax.plot([x0+delkax,x0-delkax],[y0-delkay, y0-delkay],[posun_z,posun_z], 'k-', lw=0.8, color='black')
ax.plot([x0-delkax,x0-delkax],[y0+delkay, y0-delkay],[posun_z,posun_z], 'k-', lw=0.8, color='black')
ax.plot([x0+delkax,x0+delkax],[y0+delkay, y0-delkay],[posun_z,posun_z], 'k-', lw=0.8, color='black')

xxx = np.linspace(x0-delkax, x0+delkax)


def gy(xa):
    return optimize.fsolve( lambda ya:f(xa,ya), start_fsolve)[0]
yyy = [gy(i) for i in xxx]

#for myx,myy in zip(xxx,yyy):
#    ax.plot([myx,myx],[myy,myy],[posun_z,0], color='black', alpha=0.1)

ax2 = plt.axes([.7, .7, .2, .2], axisbg='#ffff99', aspect='equal')

plt.setp(ax2, xticks=[], yticks=[])
ax2.set_ylim(y0-delkay, y0+delkay)
ax2.set_xlim(x0-delkax, x0+delkax)

plt.plot(xxx, yyy, linewidth=2, color='red')
plt.title('Detail ve 2D:')

def ty(xa):
    return optimize.fsolve( lambda ya:tecna_rovina(xa,ya), 0.5*(ymin+ymax))[0]

yyy = [ty(i) for i in xxx]
plt.plot(xxx, yyy, linewidth=2, color='blue')
plt.plot(x0,y0, 'ko')

plt.savefig(outputfile,bbox_inches="tight", pad_inches=.15)

if animovat:
    ax.axis("off")
    for ii in xrange(0,360,4):
        ax.view_init(elev=10., azim=ii)
        jmeno="000"+str(ii)
        jmeno=jmeno[-3:]
        plt.savefig("movie"+jmeno+".png")

# convert -delay 20 movie*.png animation.gif && rm movie
