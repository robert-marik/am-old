import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np

plt.xkcd()

matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{euler,amsmath}"]
matplotlib.rc('text', usetex=True)

xmin, xmax, ymin, ymax = -0.1, 2.2, -0.2, 2.2


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

plt.axes().set_aspect('equal', 'datalim')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_color('none')
ax.set_xlabel('')
#ax.set_xticks([])
#ax.set_yticks([])
ax.set_ylabel('')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)

rinit=1
phiinit=0

x0=rinit*np.cos(phiinit)
y0=rinit*np.sin(phiinit)

phi=np.arctan(y0/x0)
r=np.sqrt(x0**2+y0**2)
dr=1
dphi=3.141592/2

phit=np.linspace(phi, phi+dphi, 256,endpoint=True)
xt=r*np.cos(phit)
yt=r*np.sin(phit)
x2t=(r+dr)*np.cos(phit)
y2t=(r+dr)*np.sin(phit)

x2t=reversed(x2t)
y2t=reversed(y2t)

from matplotlib.patches import Polygon
verts = list(zip(xt,yt)) + list(zip(x2t, y2t))
facecolor='#d2ffd2'
edgecolor='#006131'

poly = Polygon(verts, facecolor=facecolor, edgecolor=edgecolor)
ax.add_patch(poly)

#import matplotlib.patches as mpatches

fig.savefig("polarni_1.png",bbox_inches="tight", pad_inches=.1, transparent=True)

####################################3

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)


rinit=0
phiinit=0

x0=rinit*np.cos(phiinit)
y0=rinit*np.sin(phiinit)

phi=0
r=0
dr=1
dphi=3.141592*2

ax.spines['bottom'].set_position(('zero'))
ax.spines['left'].set_position(('zero'))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')



phit=np.linspace(phi, phi+dphi, 256,endpoint=True)
xt=r*np.cos(phit)
yt=r*np.sin(phit)
x2t=(r+dr)*np.cos(phit)
y2t=(r+dr)*np.sin(phit)

x2t=reversed(x2t)
y2t=reversed(y2t)

from matplotlib.patches import Polygon
verts = list(zip(xt,yt)) + list(zip(x2t, y2t))
facecolor='#d2ffd2'
edgecolor='#006131'

poly = Polygon(verts, facecolor=facecolor, edgecolor=edgecolor)
ax.add_patch(poly)

xmin, xmax, ymin, ymax = -1.2, 1.2, -1.2, 1.2
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)

#import matplotlib.patches as mpatches

fig.savefig("polarni_2.png",bbox_inches="tight", pad_inches=.1, transparent=True)

#################################


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)


rinit=0
phiinit=0

x0=rinit*np.cos(phiinit)
y0=rinit*np.sin(phiinit)

phi=3.141592/4
r=0
dr=1
dphi=3.141592/4

ax.spines['bottom'].set_position(('zero'))
ax.spines['left'].set_position(('zero'))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')



phit=np.linspace(phi, phi+dphi, 256,endpoint=True)
xt=r*np.cos(phit)
yt=r*np.sin(phit)
x2t=(r+dr)*np.cos(phit)
y2t=(r+dr)*np.sin(phit)

x2t=reversed(x2t)
y2t=reversed(y2t)

from matplotlib.patches import Polygon
verts = list(zip(xt,yt)) + list(zip(x2t, y2t))
facecolor='#d2ffd2'
edgecolor='#006131'

poly = Polygon(verts, facecolor=facecolor, edgecolor=edgecolor)
ax.add_patch(poly)

xmin, xmax, ymin, ymax = -0.2, 1.2, -0.2, 1.2
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)

#import matplotlib.patches as mpatches

fig.savefig("polarni_3.png",bbox_inches="tight", pad_inches=.1, transparent=True)

