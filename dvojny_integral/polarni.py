import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np

plt.xkcd()

matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{euler,amsmath}"]
matplotlib.rc('text', usetex=True)

xmin, xmax, ymin, ymax = -0.2, 1.2, -0.2, 1.2

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)


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

x0, y0 = 0.95, .8

plot ([x0],[y0], 'ro', zorder=10)


import matplotlib.patches as mpatches



#tmin=0
#tmax=1
#tt = np.linspace(tmin, tmax, 50, endpoint=True)

#kk=0.8
#xt = k*np.cos(tt*y0/x0*kk)
#yt = k*np.sin(tt*y0/x0*kk)

#plot(xt,yt, ls="-|>")

#ar=mpatches.FancyArrowPatch(posA=[k*np.sqrt(x0**2+y0**2),0],posB=[k*x0, k*y0],)
#ar.set_connectionstyle("angle, angleA=45, angleB=0, rad=10")
#print dir(ar)
#ax.add_artist(ar)



#ellipse = Arc([0,0],0.5,0.5,0,0,38)
#ax.add_patch(ellipse)

def stred(a,b):
	return (0.5*a[0]+0.5*b[0], 0.5*a[1]+0.5*b[1])

def stred_text(a,b,c,**kws):
	return ax.text( 0.5*a[0]+0.5*b[0], 0.5*a[1]+0.5*b[1], c,**kws)


from matplotlib.patches import ConnectionPatch
#annotate ('', xy=(x3[0], funkce(x3[0])), xytext=(x3[1], funkce(x3[1])), arrowprops={'arrowstyle':'<->', 'color':'red', 'shrinkA':'7'})

def sipka(A, B, **kwds):
	con=ConnectionPatch(xyA=A, xyB=B, coordsA='data', coordsB='data', mutation_scale=20, lw=2, zorder=10, **kwds)
	ax.add_artist(con)

bbox_props = dict()

fontsize=30
alpha=1
sipka ((0,0), (x0,y0), shrinkB=5, arrowstyle="-|>")

y1=-0.05
sipka ((0,y1), (x0,y1), shrinkB=1, arrowstyle="<|-|>", color='gray')

sipka ((x0,0), (x0,y0), shrinkB=5, arrowstyle="<|-|>", color="gray")

plot([x0,x0], [y0,y1], linestyle="--", color='gray')

stred_text ( (0,0) , (x0,y0) , r"$r$",fontsize=fontsize, ha='right', va='bottom', alpha=alpha, color='k', bbox=bbox_props )

stred_text ( (x0,0) , (x0,y0) , r"$y$",fontsize=fontsize, ha='left', va='bottom', alpha=alpha, color='gray', bbox=bbox_props )

y1=-0.05
stred_text ( (0,y1) , (x0,y1) , r"$x$",fontsize=fontsize, ha='left', alpha=alpha, va='top', color='gray', bbox=bbox_props )

#stred_text( (x3[0], funkce(x3[0])), (x3[1], funkce(x3[0])),r"$\approx |\varphi'(t)\Delta t|$",fontsize=20, ha='center', va='top', alpha=alpha, bbox=bbox_props )
#stred_text( (x3[1], funkce(x3[1])), (x3[1], funkce(x3[0])),r"$\approx |\psi'(t)\Delta t|$",fontsize=20, ha='left', va='top', alpha=alpha, bbox=bbox_props )


k=0.15
#con=ConnectionPatch(xyA=(k*np.sqrt(x0**2+y0**2),0), xyB=(k*x0,k*y0), coordsA='data', coordsB='data', mutation_scale=20, lw=2, zorder=10)
#ax.add_artist(con)

ax.annotate("",
            xytext=(k*np.sqrt(x0**2+y0**2),0), xycoords='data',
            xy=(k*x0,k*y0), textcoords='data', color='k', zorder=15, 
            arrowprops=dict(arrowstyle="->", #linestyle="dashed",
                            color="k", linewidth=2,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )

k3=1.0/4
ax.text(k3*x0, 1.0/3*k3*y0, r"$\varphi$", fontsize=30, ha='center', va='bottom')



# k = 0.96
# ax.arrow (0,0,k*x0,k*y0)

k=1.05
ax.text(k*x0*0.8, k*y0, r"$\begin{aligned}x&=r\cos\varphi \\ y&=r\sin\varphi\end{aligned}$", fontsize=30, ha='right', va='bottom')
ax.text(x0+0.03, y0, r"$A$", fontsize=30, ha='left', va='bottom')
ax.text(0-0.03, 0-0.03, r"$0$", fontsize=30, ha='right', va='top')

# ax.plot(X,Y1, color='blue')
# ax.plot(X,Y2, color='blue')

# for i in (60, 105, 150):
#     od = (X[i], Y1[i])
#     do = (X[i], Y2[i])
#     annotate ('', od, do, arrowprops={'arrowstyle':'<->'})

# Y=0.5*(Y1[jmin])
# annotate ('', (X[jmin],Y), (X[jmax], Y), arrowprops={'arrowstyle':'<->'})


# for j in (jmin, jmax):
#     plot ([X[j],X[j]], [Y1[j],0], ls="--", color='gray', zorder=-3 )



# fontsize=20
# ax.text(1,Y1[-1], r"$y=\varphi(x)$",  ha='right', va='bottom', fontsize=fontsize)
# ax.text(1,Y2[-1], r"$y=\psi(x)$",  ha='right', va='top', fontsize=fontsize)

# ax.text(X[jmin],0.5*(Y1[0]+Y2[0]), r"$\begin{gathered}a\leq x \leq b\\ \varphi(x)\leq y \leq \phi(x) \end{gathered}$", ha='right', fontsize=fontsize)

# for x,t in ((X[jmin],'$a$'), (X[jmax], '$b$')):
#     ax.text(x,-0.01, t,  ha='center', va='top', fontsize=fontsize)



fig.savefig("polarni_souradnice.png",bbox_inches="tight", pad_inches=.15)



