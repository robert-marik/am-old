#from pylab import *
#from numpy import linspace,log
#from matplotlib.pyplot import *

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np

plt.xkcd()

matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{euler,amsmath}"]
matplotlib.rc('text', usetex=True)


X = np.linspace(0, 1, 256,endpoint=True)

Y1 = 0.1*(5-(2-X)**2)
Y2 = 0.4+0.1*np.cos(X*3)

jmin, jmax=30,187

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

facecolor='#d2ffd2'
edgecolor='#006131'

from matplotlib.patches import Polygon
verts = list(zip(X[jmin:jmax], Y1[jmin:jmax]))+list(reversed(zip(X[jmin:jmax], Y2[jmin:jmax])))
poly = Polygon(verts, facecolor=facecolor, edgecolor=edgecolor)
ax.add_patch(poly)


ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('none')
ax.spines['left'].set_color('none')
ax.set_xlabel('')
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylabel('')


lw=4
ax.plot(X,Y1, color='#006131', lw=lw)
ax.plot(X,Y2, color='#006131', lw=lw)

for i in (60, 105, 150):
    od = (X[i], Y1[i])
    do = (X[i], Y2[i])
    annotate ('', od, do, arrowprops={'arrowstyle':'<->'})

Y=0.5*(Y1[jmin])
annotate ('', (X[jmin],Y), (X[jmax], Y), arrowprops={'arrowstyle':'<->'})


for j in (jmin, jmax):
    plot ([X[j],X[j]], [Y1[j],0], ls="--", color='gray', zorder=-3 )



fontsize=20
ax.text(1,Y1[-1], r"$y=\varphi(x)$",  ha='right', va='bottom', fontsize=fontsize)
ax.text(1,Y2[-1], r"$y=\psi(x)$",  ha='right', va='top', fontsize=fontsize)

ax.text(X[jmin],0.5*(Y1[0]+Y2[0]), r"$\begin{gathered}a\leq x \leq b\\ \varphi(x)\leq y \leq \psi(x) \end{gathered}$", ha='right', fontsize=fontsize)

for x,t in ((X[jmin],'$a$'), (X[jmax], '$b$')):
    ax.text(x,-0.01, t,  ha='center', va='top', fontsize=fontsize)


fig.savefig("fub_1.png",bbox_inches="tight", pad_inches=.15)



#########################################################





fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('none')
ax.spines['left'].set_position(('data',0))
ax.set_xlabel('')
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylabel('')

ax.spines['bottom'].set_color('none')


verts = list(zip( Y1[jmin:jmax], X[jmin:jmax]))+list(reversed(zip( Y2[jmin:jmax], X[jmin:jmax])))
poly = Polygon(verts, facecolor=facecolor, edgecolor=edgecolor)
ax.add_patch(poly)


ax.plot(Y1,X, color='#006131', lw=lw)
ax.plot(Y2,X, color='#006131', lw=lw)



fontsize=20
ax.text(Y1[0],0, r"$x=\varphi(y)$",  ha='center', va='top', fontsize=fontsize)
ax.text(Y2[0],0, r"$x=\psi(y)$",  ha='center', va='top', fontsize=fontsize)

ax.text(0.5*(Y1[jmax]+Y2[jmax]),X[jmin+40], r"$\begin{gathered}a\leq y \leq b\\ \varphi(y)\leq x \leq \psi(y) \end{gathered}$", ha='center', fontsize=fontsize)

for j in (jmin, jmax):
    plot ([Y1[j],0], [X[j],X[j]], ls="--", color='gray', zorder=-3 )


for x,t in ((X[jmin],'$a$'), (X[jmax], '$b$')):
    ax.text(-0.01,x, t,  ha='center', va='top', fontsize=fontsize)














fig.savefig("fub_2.png",bbox_inches="tight", pad_inches=.15)




##############################################################

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('none')
ax.spines['left'].set_position(('data',0))
ax.set_xlabel('')
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylabel('')



Y1 = 3
Y2 = 1

XX=X[jmin:jmax]
ax.plot([X[jmin], X[jmax], X[jmax], X[jmin], X[jmin] ],[Y1, Y1, Y2, Y2, Y1], color='#006131', lw=lw)


verts = list(zip([X[jmin], X[jmax], X[jmax], X[jmin], X[jmin] ],[Y1, Y1, Y2, Y2, Y1]))
poly = Polygon(verts, facecolor=facecolor, edgecolor=edgecolor)
ax.add_patch(poly)


ax.set_ylim(0, 4)
ax.set_xlim(0, 1)

for x,t in ((X[jmin],'$a$'), (X[jmax], '$b$')):
    ax.text(x,-0.01, t,  ha='center', va='top', fontsize=fontsize)

for y,t in ((Y1,r'$d$'), (Y2, r'$c$')):
    ax.text(-0.01,y, t,  ha='right', va='center', fontsize=fontsize)

for i,j in ((Y1, X[jmax]), (Y2, X[jmin]) ):
    plot ([0,X[jmin]],[i,i], color='gray', ls='--', zorder=-3)
    plot ([j,j],[0,Y2], color='gray', ls='--', zorder=-3)

ax.text(0.5*(X[jmin]+X[jmax]),0.5*(Y1+Y2), r"$\begin{gathered}a\leq x \leq b\\ c\leq y \leq d \end{gathered}$", ha='center', fontsize=fontsize)




fig.savefig("fub_3.png",bbox_inches="tight", pad_inches=.15)


###### 


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

X = np.linspace(-0.5, 2.5, 300,endpoint=True)

Y1 = 0*X
Y2 = X**2

jmin, jmax=50,249

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

facecolor='#d2ffd2'
edgecolor='#006131'

from matplotlib.patches import Polygon
verts = list(zip(X[jmin:jmax], Y1[jmin:jmax]))+list(reversed(zip(X[jmin:jmax], Y2[jmin:jmax])))
poly = Polygon(verts, facecolor=facecolor, edgecolor=edgecolor)
ax.add_patch(poly)


ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('none')
#ax.spines['left'].set_color('none')
ax.set_xlabel('')
#ax.set_xticks([])
#ax.set_yticks([])
ax.set_ylabel('')


lw=4
ax.plot(X,Y1, color='#006131', lw=lw)
ax.plot(X,Y2, color='#006131', lw=lw)

#for i in (60, 105, 150):
#    od = (X[i], Y1[i])
#    do = (X[i], Y2[i])
#    annotate ('', od, do, arrowprops={'arrowstyle':'<->'})

#Y=0.5*(Y1[jmin])
#annotate ('', (X[jmin],Y), (X[jmax], Y), arrowprops={'arrowstyle':'<->'})


for j in (jmin, jmax):
    plot ([X[j],X[j]], [Y1[j],0], ls="--", color='gray', zorder=-3 )



fontsize=20
#ax.text(1,Y1[-1], r"$y=\varphi(x)$",  ha='right', va='bottom', fontsize=fontsize)
ax.text(1,Y2[-1]*0.5, r"$y=x^2$",  ha='right', va='top', fontsize=fontsize)

#ax.text(X[jmin],0.5*(Y1[0]+Y2[0]), r"$\begin{gathered}a\leq x \leq b\\ \varphi(x)\leq y \leq \psi(x) \end{gathered}$", ha='right', fontsize=fontsize)

#for x,t in ((X[jmin],'$a$'), (X[jmax], '$b$')):
#    ax.text(x,-0.01, t,  ha='center', va='top', fontsize=fontsize)



fig.savefig("fub_4.png",bbox_inches="tight", pad_inches=.15)



