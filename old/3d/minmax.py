# Using the magic encoding
# -*- coding: utf-8 -*-


import sys
if len(sys.argv) > 1:
    priklad = sys.argv[1]
else:
    priklad = "1"

import matplotlib
matplotlib.rc('text', usetex=False)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{euler,amsmath}"]

#animovat=True
bez_znacek = True
bez_znacek = False
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

#ax.axis(off)
ax.w_xaxis.line.set_color("red")
ax.w_yaxis.line.set_color("red")


# pocatecni hodnoty
xmin=-2.5
xmax=4.2
ymin=-4.2
ymax=3
zmin=-35
zmax=5

x0,y0=2,-2

delkax=2    # delka obdelnicku ve smeru x
delkay=2  # delka obdelnicku ve smeru y
delkaz=1  # delka obdelnicku ve smeru y

outputfile="extrem_"+str(priklad)+".png" # jmeno vystupniho souboru
posun_z=-30  # rovina ve ktere se kresli vrstevnice

# funkce
lambdifyf = False  # true pokud je nutno derivaci funkce f prevest ze sympy do numpy
def f(x,y):
    return 1-x**2-y**2


########################################################
########################################################
if priklad == "2":
    x0,y0=0,0


########################################################
########################################################
if priklad == "3":
    x0,y0=0,0
    def f(x,y):
        return x**2-y**2


# vypocet gradientu a tecne roviny
from sympy.abc import x, y
from sympy.utilities.lambdify import lambdify, implemented_function
gradfx=lambdify((x,y), f(x,y).diff(x))
gradfy=lambdify((x,y), f(x,y).diff(y))
if lambdifyf:
    f=lambdify((x,y), f(x,y), 'numpy')


def tecna_rovina(x,y):
    return f(x0,y0)+gradfx(x0,y0)*(x-x0)+gradfy(x0,y0)*(y-y0)

X = np.arange(xmin, xmax, .1)
Y = np.arange(ymin, ymax, .1)
X, Y = np.meshgrid(X, Y)
Z = f(X,Y)

xxx = np.linspace(x0-delkax, x0+delkax)
yyy = np.linspace(y0-delkay, y0+delkay)

def gy(xa):
     return f(xa,y0)
zzzy = [gy(i) for i in xxx]

mez_z_x_min=min(zzzy)-0.2*(max(zzzy)-min(zzzy))
mez_z_x_max=max(zzzy)+0.2*(max(zzzy)-min(zzzy))

def gx(ya):
     return f(x0,ya)
zzzx = [gx(i) for i in yyy]

mez_z_y_min=min(zzzx)-0.2*(max(zzzx)-min(zzzx))
mez_z_y_max=max(zzzx)+0.2*(max(zzzx)-min(zzzx))


if bez_znacek:
    plt.setp(ax, xticks=[], yticks=[], zticks=[])

plt.title(u'3D graf:', loc='center')

ax.plot_surface(X, Y, Z, alpha=.15, lw=0.1, cmap='autumn')
ax.plot(xxx, [y0 for i in xxx], zzzy, color='red')
ax.plot([x0 for i in yyy], yyy, zzzx, color='blue')

ax.scatter(x0,y0,f(x0,y0), c='r')

ax.set_xlabel('x')
ax.set_xlim(xmin, xmax)
ax.set_ylabel('y')
ax.set_ylim(ymin, ymax)
ax.set_zlabel('f(x,y)')
ax.set_zlim(zmin, zmax)


ax2 = plt.axes([.7, .7, .2, .2], axisbg='yellow')
plt.setp(ax2, xticks=[], yticks=[])
ax2.set_xlim(x0-delkax, x0+delkax)
ax2.set_ylim(mez_z_x_min, mez_z_x_max)
ax2.set_xlabel('x')
ax2.set_ylabel('f(x,y)')
ax2.plot(xxx, zzzy, linewidth=2, color='red')
plt.title('Rovina $y=y_0$')
plt.plot(x0,f(x0,y0), 'ko')


ax3 = plt.axes([.1, .7, .2, .2], axisbg='yellow')
plt.setp(ax3, xticks=[], yticks=[])
ax3.set_xlim(y0-delkay, y0+delkay)
ax3.set_ylim(mez_z_y_min, mez_z_y_max)
ax3.set_xlabel('Y')
ax3.set_ylabel('f(x,y)')
ax3.plot(yyy, zzzx, linewidth=2, color='blue')
plt.title('Rovina $x=x_0$')
ax3.plot(y0,f(x0,y0), 'ko')

plt.savefig(outputfile)

# if animovat:
#     ax.axis("off")
#     for ii in xrange(0,360,4):
#         ax.view_init(elev=10., azim=ii)
#         jmeno="000"+str(ii)
#         jmeno=jmeno[-3:]
#         plt.savefig("movie"+jmeno+".png")


# convert -delay 20 movie*.png animation.gif && rm movie
