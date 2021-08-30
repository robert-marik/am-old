import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np

plt.xkcd()

matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{euler,amsmath}"]
matplotlib.rc('text', usetex=True)

xmin, xmax, ymin, ymax = -0.1, 0.85, -0.2, 1


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

plt.axes().set_aspect('equal', 'datalim')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
ax.yaxis.set_ticks_position('none')
#ax.spines['left'].set_color('none')
ax.set_xlabel('')
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylabel('')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)

rinit=0.7
phiinit=0.6

x0=rinit*np.cos(phiinit)
y0=rinit*np.sin(phiinit)

phi=np.arctan(y0/x0)
r=np.sqrt(x0**2+y0**2)
dr=0.25
dphi=0.35

phit=np.linspace(phi, phi+dphi, 256,endpoint=True)
xt=r*np.cos(phit)
yt=r*np.sin(phit)
x2t=(r+dr)*np.cos(phit)
y2t=(r+dr)*np.sin(phit)


#plot(xt,yt)
#plot(x2t,y2t)

x2t=reversed(x2t)
y2t=reversed(y2t)

from matplotlib.patches import Polygon
verts = list(zip(xt,yt)) + list(zip(x2t, y2t))
facecolor='#d2ffd2'
edgecolor='#006131'

poly = Polygon(verts, facecolor=facecolor, edgecolor=edgecolor)
ax.add_patch(poly)

import matplotlib.patches as mpatches


def stred(a,b):
	return (0.5*a[0]+0.5*b[0], 0.5*a[1]+0.5*b[1])

def stred_text(a,b,c,**kws):
	return ax.text( 0.5*a[0]+0.5*b[0], 0.5*a[1]+0.5*b[1], c,**kws)


from matplotlib.patches import ConnectionPatch
#annotate ('', xy=(x3[0], funkce(x3[0])), xytext=(x3[1], funkce(x3[1])), arrowprops={'arrowstyle':'<->', 'color':'red', 'shrinkA':'7'})

def sipka(A, B, **kwds):
	con=ConnectionPatch(xyA=A, xyB=B, coordsA='data', coordsB='data', mutation_scale=20, zorder=10, **kwds)
	ax.add_artist(con)

bbox_props = dict()

fontsize=20
alpha=1
sipka ((0,0), (x0,y0), shrinkB=0, arrowstyle="-|>", lw=2)
sipka ((0,0), (r*np.cos(phiinit+dphi),r*np.sin(phiinit+dphi)), shrinkB=0, lw=1, arrowstyle="-|>", linestyle='dashed')

stred_text ( (0,0) , (x0,y0) , r"$r$",fontsize=fontsize, ha='left', va='top', alpha=alpha, color='k', bbox=bbox_props )

k=0.2
ax.annotate("",
            xytext=(k*np.sqrt(x0**2+y0**2),0), xycoords='data',
            xy=(k*x0,k*y0), textcoords='data', color='k', zorder=15, 
            arrowprops=dict(arrowstyle="->", #linestyle="dashed",
                            color="k", linewidth=2,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )

R5=0.25
dphi5=0.4

ax.annotate("",
            xytext=(R5*np.cos(phiinit),R5*np.sin(phiinit)), 
            xycoords='data',
            xy=(R5*np.cos(phiinit+dphi),R5*np.sin(phiinit+dphi)), 
            textcoords='data', color='k', zorder=15, 
            arrowprops=dict(arrowstyle="<|-|>", #linestyle="dashed",
                            color="k", linewidth=2,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.2", linestyle='dashed', lw=1
                            ),
            )

k3=.8/4
ax.text(k3*x0, 1.0/7*k3*y0, r"$\varphi$", fontsize=fontsize, ha='center', va='bottom')

k3=2.80/7.6
ax.text(k3*x0, 1.0/0.8*k3*y0, r"$\mathrm{d}\varphi$", fontsize=fontsize, ha='center', va='bottom')

r_=r+0.5*dr
phi_=phi+0.5*dphi
ax.text( r_*np.cos(phi_), r_*np.sin(phi_),'$\mathrm{d}A$', fontsize=fontsize, ha='center', va='center')


phi_=phi+-0.05
r_=r+dr

sipka ((r*np.cos(phi_),r*np.sin(phi_)), (r_*np.cos(phi_),r_*np.sin(phi_)), shrinkB=0, lw=1, arrowstyle="<|-|>", linestyle='dashed', color='k')

A=[0.5*(i[0]+i[1]) for i in zip ((r*np.cos(phi_),r*np.sin(phi_)) ,(r_*np.cos(phi_),r_*np.sin(phi_) ) ) ]
sipka ((r*np.cos(phi_),r*np.sin(phi_)), (r_*np.cos(phi_),r_*np.sin(phi_)), shrinkB=0, lw=1, arrowstyle="<|-|>", linestyle='dashed', color='k')
ax.text(A[0], A[1], r'$\mathrm{d}r$', ha='left', va='top', fontsize=fontsize)

r_=r+dr+0.04

Ax=r*np.cos(phi)
Ay=r*np.sin(phi)
Dx=r*np.cos(phi+dphi)
Dy=r*np.sin(phi+dphi)
Bx=r*np.cos(phi)+(r_-r)*np.cos(phi+0.5*dphi)
By=r*np.sin(phi)+(r_-r)*np.sin(phi+0.5*dphi)
Cx=r*np.cos(phi+dphi)+(r_-r)*np.cos(phi+0.5*dphi)
Cy=r*np.sin(phi+dphi)+(r_-r)*np.sin(phi+0.5*dphi)

#plot([Ax,Bx],[Ay,By], color='k', linestyle='dotted', lw=0.5)
#plot([Cx,Dx],[Cy,Dy], color='k', linestyle='dotted', lw=0.5)

#sipka ((r_*np.cos(phi),r_*np.sin(phi)), (r_*np.cos(phi+dphi),r_*np.sin(phi+dphi)), shrinkB=0, lw=1, arrowstyle="<|-|>", linestyle='dashed', color='k')
#sipka ((Bx,By), (Cx,Cy), shrinkB=0, lw=1, arrowstyle="<|-|>", linestyle='dashed', color='k')
sipka ((Ax,Ay), (Dx,Dy), shrinkA=2, shrinkB=2, lw=1, arrowstyle="<|-|>", linestyle='dashed', color='k')

phi_=phi+0.5*dphi
#ax.text(r_*np.cos(phi_), r_*np.sin(phi_), r'$r\mathrm{d}\varphi$', ha='left', fontsize=fontsize)
ax.text(r*np.cos(phi_)-0.02, r*np.sin(phi_), r'$r\mathrm{d}\varphi$', ha='right', va='top', fontsize=fontsize)

y_=0.8
ax.text(0.1,y_, r'$\mathrm{d}A\approx r\mathrm{d}\varphi \mathrm{d}r$', fontsize=fontsize)

Ax_=0.7
Ay_=0.1
d_=0.08
shift_=0.01
y_=Ay_-0.01
x_=Ax_+d_+0.01

verts = [[Ax_, Ay_], [Ax_+d_, Ay_], [Ax_+d_, Ay_+d_], [Ax_, Ay_+d_], [Ax_, Ay_]]
poly = Polygon(verts, facecolor='0.8', edgecolor='0.4')
ax.add_patch(poly)

color='0.4'
fontsize=20
sipka ((Ax_, y_), (Ax_+d_, y_), shrinkB=0, lw=1, arrowstyle="<|-|>", color=color)
text (Ax_+0.5*d_, y_-shift_, r'$\mathrm{d}x$', ha='center', va='top', color=color, fontsize=fontsize)
sipka ((x_, Ay_), (x_, Ay_+d_), shrinkB=0, lw=1, arrowstyle="<|-|>", color=color)
text (Ax_+d_+2*shift_, Ay_+0.5*d_, r'$\mathrm{d}y$', ha='left', va='center', color=color, fontsize=fontsize)

text (Ax_+0.5*d_, Ay_+1.1*d_, r'$\mathrm{d}A=\mathrm{d}x\mathrm{d}y$', ha='center', va='bottom', color=color, fontsize=fontsize)

fig.savefig("jakobian.png",bbox_inches="tight", pad_inches=.15)



