import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
rc('text', usetex=True)

plt.figure(1,(8,8))
plt.axes().set_aspect('equal', 'datalim')
#ax.set_aspect('equal', 'datalim')

#plt.xkcd()

xmin, xmax, ymin, ymax = .5, 2, .5, 2

# import matplotlib.gridspec as gridspec
# gs = gridspec.GridSpec(2, 2,
#                        width_ratios=[1,2],
#                        height_ratios=[1,1], hspace=0.3
#                        )
# ax1 = plt.subplot(gs[0])
# ax2 = plt.subplot(gs[1])
# ax3 = plt.subplot(gs[2])
# ax4 = plt.subplot(gs[3])


n=2
if n==0:
    # https://sagecell.sagemath.org/?z=eJxty8sOgjAQheG9ie_gjjNaIHbPq2Ca4JQmFQwXnXl7G7vQBM7y_3LEaPNyEwo5aUHHA0OMUnOt7TmOHtLai7Y2gc_gFjdAa0ll7sc3kA8mM_1y5SfXhfuwgL5UzeHxjIH1xmuMIIMuMCP_9rz8d9l42ge6lTpG&lang=sage
    def f(x,y): return (1.0/2*np.log(x**2+y**2))
    def g(x,y): return (np.arctan(y/x))
    def dfx(x,y): return (x/(x**2+y**2))
    def dfy(x,y): return (y/(x**2+y**2))
    text=r'$\displaystyle\vec v_1=\frac {1}{r^2}(x\vec i+y\vec j)=\nabla\left(\frac 12 \ln(x^2+y^2)\right)=\mathop{\mathrm{rot}}\left(\mathop{\mathrm{arctg}}\frac {y}{x}\right)$'
    plt.title(text, fontsize=16)

if n==1:
    # 
    def g(x,y): return (-1.0/2*np.log(x**2+y**2))
    def f(x,y): return (np.arctan(y/x))
    def dfx(x,y): return (-y/(x**2+y**2))
    def dfy(x,y): return (x/(x**2+y**2))
    text=r'$\displaystyle\vec v_2=\frac {1}{r^2}(-y\vec i+x\vec j)=\nabla\left(\mathop{\mathrm{arctg}}\frac {y}{x}\right)=\mathop{\mathrm{rot}}\left(-\frac 12 \ln(x^2+y^2)\right)$'
    plt.title(text, fontsize=16)

    
if n==2:
    # 
    def g(x,y): return y
    def f(x,y): return x
    def dfx(x,y): return 1
    def dfy(x,y): return 0
    text=r'$\displaystyle\vec v_3=\vec i=\nabla\left(x\right)=\mathop{\mathrm{rot}}\left(y\right)$'
    plt.title(text, fontsize=16)

if n==3:
    # 
    def g(x,y): return (-1.0/2*np.log(x**2+y**2)+y)
    def f(x,y): return (np.arctan(y/x)+x)
    def dfx(x,y): return (-y/(x**2+y**2)+1)
    def dfy(x,y): return (x/(x**2+y**2))
    text=r'$\displaystyle\vec v_4=\vec v_2+\vec v_3$'
    plt.title(text, fontsize=16)


# x,y=var('x y')
# g, f = -1/2*log(x^2+y^2), atan(y/x)
# f, g = 1/2*log(x^2+y^2), atan(y/x)
# f, g =  x,y
# g, f = -1/2*log(x^2+y^2)+y, atan(y/x)+x
# show((f,g))
# show((f.gradient([x,y]).simplify_full(),(diff(g,y).simplify_full(),-diff(g,x).simplify_full())))
    

delta = 0.05
x = np.arange(xmin, xmax, delta)
y = np.arange(ymin, ymax, delta)
X, Y = np.meshgrid(x, y)

Z=g(X,Y)
CS = plt.contour(X, Y, Z, colors=['blue'])

Z=f(X,Y)
CS = plt.contour(X, Y, Z, colors=['gray'])

delta = 0.1
x = np.arange(xmin, xmax, delta)
y = np.arange(ymin, ymax, delta)
X, Y = np.meshgrid(x, y)

U = dfx(X,Y)#/np.sqrt(dfx(X,Y)**2+dfy(X,Y)**2)
V = dfy(X,Y)#/np.sqrt(dfx(X,Y)**2+dfy(X,Y)**2)

plt.quiver(X,Y,U,V, color='blue')

#plt.axes().set_aspect('equal', 'datalim')
plt.savefig("stream"+str(n)+".svg")
plt.savefig("stream"+str(n)+".png")
