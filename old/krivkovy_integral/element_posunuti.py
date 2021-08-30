from numpy import linspace,log
from matplotlib.pyplot import *

matplotlib.pyplot.xkcd()


import matplotlib
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath,euler,amsfonts}"]

funkce = lambda x:log(x+0.5)
#funkce = lambda x:np.cos(x)

funkce = lambda x:(x-4)**3


alpha=1

x1 = linspace(0.4,2.4,10)
y1 = funkce(x1)
x2 = linspace(0.3,2.4,3)
x3 = [0.8,1.8,1.8]
 
fig = figure(figsize=(8,8))
ax = fig.add_subplot(111)
 
xmin=min(x1)
xmax=max(x1)
ymin=min(y1)
ymax=max(y1)

#arrow_length = 10
# X-axis arrow
#ax.annotate('', xy=(1, 0), xycoords=('axes fraction', 'data'), 
#            xytext=(arrow_length, 0), textcoords='offset points',
#            ha='left', va='center',
#            arrowprops=dict(arrowstyle='<-', fc='black'))


fontsize=20

ax.set_xticks([])
ax.set_yticks([])
ax.plot(x1,y1,'g',linewidth=4)

def stred(a,b):
	return (0.5*a[0]+0.5*b[0], 0.5*a[1]+0.5*b[1])

def stred_text(a,b,c,**kws):
	return ax.text( 0.5*a[0]+0.5*b[0], 0.5*a[1]+0.5*b[1], c,**kws)


from matplotlib.patches import ConnectionPatch
#annotate ('', xy=(x3[0], funkce(x3[0])), xytext=(x3[1], funkce(x3[1])), arrowprops={'arrowstyle':'<->', 'color':'red', 'shrinkA':'7'})

def sipka(A, B, **kwds):
	con=ConnectionPatch(xyA=A, xyB=B, coordsA='data', coordsB='data', arrowstyle="-|>", mutation_scale=20, lw=2, zorder=10, **kwds)
	ax.add_artist(con)

bbox_props = dict()

stred_text ( (x3[0], funkce(x3[0])) , (x3[1], funkce(x3[1])) , r"$\Delta \vec r$",fontsize=fontsize, ha='left', va='top', alpha=alpha, color='red', bbox=bbox_props )
posun=0.3
stred_text( (x3[0], funkce(x3[0])-posun), (x3[1], funkce(x3[0])-posun),r"$\approx \varphi'(t)\Delta t\cdot \vec i$",fontsize=20, ha='center', va='top', alpha=alpha, bbox=bbox_props )
stred_text( (x3[1], funkce(x3[1])), (x3[1], funkce(x3[0])),r"$\approx \psi'(t)\Delta t\cdot \vec j$",fontsize=20, ha='left', va='top', alpha=alpha, bbox=bbox_props )

ax.plot(x3[0],funkce(x3[0]),'ro')
ax.plot(x3[1],funkce(x3[1]),'ro')

ax.text(x3[0]-0.05,funkce(x3[0]),"$t=t_0$",fontsize=20, ha='right', color='green')
ax.text(x3[1]-0.05,funkce(x3[1]),"$t=t_0+\Delta t$",fontsize=20, ha='right', va='bottom', color='green')

sipka ( (x3[0], funkce(x3[0])), (x3[1], funkce(x3[1])), color='red', shrinkA=5, shrinkB=5 )
sipka ( (x3[0], funkce(x3[0])), (x3[1], funkce(x3[0])), shrinkA=5 )
sipka ( (x3[2], funkce(x3[0])), (x3[1], funkce(x3[1])), shrinkB=5 )


ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

bbox_props = dict(boxstyle="Round, pad=0.3", fc="white", ec="gray", lw=2)

ax.text(0.5*(xmin+xmax),(10*ymin + ymax)/11,r"$\Delta \vec r\approx \Bigl(\varphi'(t), \psi'(t)\Bigr)\Delta t$", fontsize=25, ha='center' , bbox=bbox_props )
ax.text(xmin+0.05,ymax-1,r"$C\equiv\begin{cases}x=\varphi(t)\\y=\psi(t)\\t\in[\alpha,\beta]\end{cases}$", fontsize=20, ha='left', va='top', bbox=bbox_props )


fig.savefig("element_posunuti.png",bbox_inches="tight",\
	pad_inches=.15)
