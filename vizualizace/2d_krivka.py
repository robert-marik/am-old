from pylab import *
from numpy import linspace,log
from matplotlib.pyplot import *

matplotlib.pyplot.xkcd()
 

T = np.linspace(0, 2*np.pi, 360,endpoint=True)
X = np.cos(T)*(1+0.45*T/np.pi)
Y = np.sin(T)*(1+0.65*T/np.pi)

fig = figure(figsize=(8,8))
ax = fig.add_subplot(111)

xmin, xmax, ymin, ymax=-2,2,-2.2,1.5
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.set_xlabel('')
ax.set_ylabel('')
ax.text( xmax+0.2, 0, 'X', ha='left')
ax.text( 0.1, ymax, 'Y', ha='left')
plot(X,Y, color='#02ff02')


fig.savefig("2d_krivka.png",bbox_inches="tight", pad_inches=.15)
fig.savefig("2d_krivka.svg",bbox_inches="tight", pad_inches=.15)
