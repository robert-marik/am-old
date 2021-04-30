# Using the magic encoding
# -*- coding: utf-8 -*-


import sys
if len(sys.argv) > 1:
    priklad = sys.argv[1]
else:
    priklad = "1"


bez_znacek = True
#bez_znacek = False

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
from  matplotlib.patches import Arrow

plt.xkcd()

import matplotlib
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath,euler,amsfonts}"]



fig = plt.figure(figsize=(12,12))

ax0 = fig.add_subplot(221, projection='3d')
ax1 = fig.add_subplot(222, projection='3d')
ax2 = fig.add_subplot(223, projection='3d')
ax3 = fig.add_subplot(224)

ax=[ax0,ax1,ax2,ax3]

for i in (1,2,0):
    ax[i].view_init(elev=40)


# pocatecni hodnoty
xmin=0
xmax=1
ymin=0
ymax=1
zmin=0
zmax=0.12
tmin=0
tmax=1

outputfile="nezavislost_na_ceste_"+str(priklad)+".png" # jmeno vystupniho souboru

X,Y = np.meshgrid( np.arange(xmin,xmax,.2),np.arange(xmin,xmax,.2) )


def Utemp(x,y):
    return -y
def Vtemp(x,y):
    return x


delka=0.1
ij_krit=900
delkaxy=delka
scalexy=0.45
mujtext=r"$\vec F=\frac{1}{\sqrt{x^2+y^2}}(-y\vec i + x\vec j),\quad \mathop{rot}\vec F=-\frac {1}{\sqrt{x^2+y^2}}$"
def U(x,y):    return Utemp(x,y)/sqrt(Vtemp(x,y)**2+Utemp(x,y)**2)*delka
def V(x,y):    return Vtemp(x,y)/sqrt(Vtemp(x,y)**2+Utemp(x,y)**2)*delka

if priklad=="2":
    mujtext=r"$\vec F=\frac{1}{{x^2+y^2}}(-y\vec i + x\vec j),\quad \mathop{rot}\vec F=0$"
    def U(x,y):   return Utemp(x,y)/(Vtemp(x,y)**2+Utemp(x,y)**2)*delka
    def V(x,y):   return Vtemp(x,y)/(Vtemp(x,y)**2+Utemp(x,y)**2)*delka
    zmax=0.16
    ij_krit=1000
    scalexy=0.2

# funkce

def fxa(t):      return 1-t
def fya(t):      return t
def dfxa(t):     return -1
def dfya(t):     return 1

def fxb(t):      return np.cos(np.pi*t/2.0)
def fyb(t):      return np.sin(np.pi*t/2.0)
def dfxb(t):     return -np.sin(np.pi*t/2.0)*np.pi/2.0
def dfyb(t):     return np.cos(np.pi*t/2.0)*np.pi/2.0

def fxc(t):      return 1-np.sin(np.pi*t/2.0)
def fyc(t):      return 1-np.cos(np.pi*t/2.0)
def dfxc(t):     return -np.cos(np.pi*t/2.0)*np.pi/2.0
def dfyc(t):     return np.sin(np.pi*t/2.0)*np.pi/2.0

def fxc(t):      return 1-t
def fyc(t):      return (t)**3
def dfxc(t):     return -1
def dfyc(t):     return 3*t**2

def fxc(t):      return (1-t)**3
def fyc(t):      return t
def dfxc(t):     return -3*(1-t**2)
def dfyc(t):     return 1

fx=(fxa,fxb,fxc)
fy=(fya,fyb,fyc)
dfx=(dfxa,dfxb,dfxc)
dfy=(dfya,dfyb,dfyc)

def f(t,i):
    return ( ( U(fx[i](t),fy[i](t))*dfx[i](t)+V(fx[i](t),fy[i](t))*(dfy[i](t)) )/sqrt((dfx[i](t)) ** 2 + (dfy[i](t)) **2) ) 

tt = np.linspace(tmin, tmax, 100, endpoint=True)

xt=[0,1,2]
yt=[0,1,2]
zt=[0,1,2]
zo=[0,1,2]

for i in (0,1,2):
    xt[i] = [fx[i](j) for j in tt]
    yt[i] = [fy[i](j) for j in tt]
    zt[i] = [f(j,i) for j in tt]
    zo[i] = [0*f(j,i) for j in tt]



iX = np.arange(0, 1, .01)
iY = np.arange(0, 1, .01)
iX, iY = np.meshgrid(iX, iY)

iXplot=[0,1,2]
iYplot=[0,1,2]
iZplot=[0,1,2]

for i in (0,1,2):
    iXplot[i] = fx[i](tmax*iX)
    iYplot[i] = fy[i](tmax*iX)
    iZplot[i] = f(tmax*iX,i)*iY

if bez_znacek:
    plt.setp(ax0, xticks=[], yticks=[], zticks=[])
    plt.setp(ax1, xticks=[], yticks=[], zticks=[])
    plt.setp(ax2, xticks=[], yticks=[], zticks=[])
    plt.setp(ax3, xticks=[], yticks=[])

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

for i in range (-5,imax, 10):
    for j in range (-3,jmax, 10):
        if (i**2+j**2>ij_krit):
            xpos=(i)*(xmax-xmin)/(1.0*imax)+xmin
            ypos=j*(ymax-ymin)/(1.0*jmax)+ymin
            a = Arrow3D([xpos,xpos+U(xpos,ypos)],[ypos,ypos+V(xpos, ypos)],[0,0], mutation_scale=15, lw=1, arrowstyle="-|>", color="k", zorder=0)
            ax1.add_artist(a)
            a = Arrow3D([xpos,xpos+U(xpos,ypos)],[ypos,ypos+V(xpos, ypos)],[0,0], mutation_scale=15, lw=1, arrowstyle="-|>", color="k", zorder=0)
            ax2.add_artist(a)
            a = Arrow3D([xpos,xpos+U(xpos,ypos)],[ypos,ypos+V(xpos, ypos)],[0,0], mutation_scale=15, lw=1, arrowstyle="-|>", color="k", zorder=0)
            ax0.add_artist(a)
            ax3.arrow(xpos, ypos, scalexy*U(xpos, ypos), scalexy*V(xpos, ypos), color='k')

ax1.plot_wireframe(iXplot[1], iYplot[1], iZplot[1], color='gray', alpha=0.25, lw=1, cstride=1, rstride=1, zorder=-20)
ax1.plot(xt[1], yt[1], zt[1], color='red')
ax1.plot(xt[1], yt[1], zo[1], color='blue', zorder=10)
ax1.set_xlabel('')
ax1.set_xlim(xmin, xmax)
ax1.set_ylabel('')
ax1.set_ylim(ymin, ymax)
ax1.set_zlabel('')
ax1.set_zlim(zmin, zmax)

ax2.plot_wireframe(iXplot[2], iYplot[2], iZplot[2], color='gray', alpha=0.25, lw=1, cstride=1, rstride=1, zorder=-20)
ax2.plot(xt[2], yt[2], zt[2], color='red')
ax2.plot(xt[2], yt[2], zo[2], color='green', zorder=10)
ax2.set_xlabel('')
ax2.set_xlim(xmin, xmax)
ax2.set_ylabel('')
ax2.set_ylim(ymin, ymax)
ax2.set_zlabel('')
ax2.set_zlim(zmin, zmax)

ax0.plot_wireframe(iXplot[0], iYplot[0], iZplot[0], color='gray', alpha=0.25, lw=1, cstride=1, rstride=1, zorder=-20)
ax0.plot(xt[0], yt[0], zt[0], color='red')
ax0.plot(xt[0], yt[0], zo[0], color='purple', zorder=10)
ax0.set_xlabel('')
ax0.set_xlim(xmin, xmax)
ax0.set_ylabel('')
ax0.set_ylim(ymin, ymax)
ax0.set_zlabel('')
ax0.set_zlim(zmin, zmax)

zorder=5
lw=3
ax3.plot(xt[0],yt[0],color='purple', lw=lw, zorder=zorder)
ax3.plot(xt[1],yt[1],color='blue', lw=lw, zorder=zorder)
ax3.plot(xt[2],yt[2],color='green', lw=lw, zorder=zorder)
ax3.set_xlim(-0.051, 1.05)
ax3.set_ylim(-0.051, 1.05)

elev=40
azim=10
for i in (0,1,2):
    ax[i].view_init(elev=elev, azim=azim)


fig.suptitle(mujtext,x=0.5, y=0.55, fontsize=30)

plt.savefig(outputfile,bbox_inches="tight", pad_inches=.15)


# convert -delay 20 movie*.png animation.gif && rm movie



# sage:
# var ('x,y,t')
# pole1 = (-y/sqrt(x^2+y^2),x/sqrt(x^2+y^2))
# pole2 = (-y/(x^2+y^2), x/(x^2+y^2) )

# latex(str(pole1))
# c1=(1-t,t)
# c2=(cos(pi*t/2), sin(pi*t/2) )
# c3=(1-t, t^3)

# def krivkovy_integral (p0, p1, k0, k1):
#     return((numerical_integral (p0.subs(x=k0, y=k1)*diff(k0,t)+p1.subs(x=k0, y=k1)*diff(k1,t),0,1)[0]),
#     r"Pole: $\vec F=(%s,%s)$,<br> Køivka: $x=%s, y=%s, t\in[0,1]$"% (latex(p0),latex(p1),latex(k0),latex(k1)))

# for P in (pole1, pole2):
#     for K in (c1, c2, c3):
#         temp=krivkovy_integral(P[0], P[1], K[0], K[1])
#         print(html("<hr>"))
#         print(html(temp[1]))
#         print(temp[0])
