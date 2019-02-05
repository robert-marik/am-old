from pylab import *
from numpy import linspace,log
from matplotlib.pyplot import *
from scipy.interpolate import make_interp_spline, BSpline

#0matplotlib.pyplot.xkcd()

def f(x,a,b):
    if x<a:
        return 0
    elif x<(a+b)*0.5:
        return (x-a)*2/(b-a)
    elif x<b:
        return (b-x)*2*1.0/(b-a)
    else:
        return 0

fig = figure(figsize=(8,8))
ax = fig.add_subplot(111)

xmin, xmax, ymin, ymax=0,0.5,0,2.5
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0))
ax.set_xlabel('X')
ax.set_ylabel('Y')
#ax.text( xmax+0.02, 0, 'X', ha='left')
#ax.text(0, ymax+0.02, 'Y', ha='left')


X = np.linspace(0, 1, 1000,endpoint=True)
for j in (0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1):
    Y = [f(i,j-0.1,j+0.1) for i in X]
    plot(X,Y)

XD=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
XD=[0,0.1,0.2,0.3,0.4,0.5]
YD=[1.5-2*x**2+2*x for x in XD]


YD=[2-10*(x-0.1)**2 for x in XD]
YD[3]=1.5
YD[4]=1.2
YD[5]=1.2

Xs = np.linspace(0, 0.5, 300,endpoint=True)
spl = make_interp_spline(XD, YD, k=3) #BSpline object
power_smooth = spl(Xs)


Y=[2-10*(x-0.1)**2 for x in X]

#plot (X,Y, color='r', linewidth=2)
plot (Xs, power_smooth, color='r')
plot (XD,YD, color='k', linewidth=2)

fig.savefig("2D_graf.png",bbox_inches="tight", pad_inches=.15)
fig.savefig("2D_graf.svg",bbox_inches="tight", pad_inches=.15)

