from pylab import *
from numpy import linspace,log
from matplotlib.pyplot import *

matplotlib.pyplot.xkcd()
 

X = np.linspace(-1, 5, 256,endpoint=True)
Y = X*np.exp(-X)

fig = figure(figsize=(8,8))
ax = fig.add_subplot(111)

xmin, xmax, ymin, ymax=-1,5,-1,0.5
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


fig.savefig("2D_graf.png",bbox_inches="tight", pad_inches=.15)
fig.savefig("2D_graf.svg",bbox_inches="tight", pad_inches=.15)

