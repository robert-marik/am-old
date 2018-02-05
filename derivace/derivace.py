from numpy import linspace,log
from matplotlib.pyplot import *

matplotlib.pyplot.xkcd()
 
lineEQ = lambda k,a: log(a)+(k-a+0.5)/a
funkce = lambda x:log(x+0.5)

x1 = linspace(0.4,2.4,10)
y1 = funkce(x1)
x2 = linspace(0.3,2.4,3)
y2 = lineEQ(x2,1.2)
x3 = [0.8,1.8,1.8]
y3 = lineEQ(x3[0],1.2), lineEQ(x3[0],1.2), lineEQ(x3[1],1.2)
 
fig = figure(figsize=(8,8))
ax = fig.add_subplot(211)
 
#arrow_length = 10
# X-axis arrow
#ax.annotate('', xy=(1, 0), xycoords=('axes fraction', 'data'), 
#            xytext=(arrow_length, 0), textcoords='offset points',
#            ha='left', va='center',
#            arrowprops=dict(arrowstyle='<-', fc='black'))


for direction in ["left","bottom"]:
	ax.spines[direction].set_position('zero')
	ax.spines[direction].set_smart_bounds(True)
for direction in ["right","top"]:
	ax.spines[direction].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
 
#ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(-0.2,1.5)
ax.set_xlim(-0.2,2.4)
ax.plot(x1,y1,'g',linewidth=3.)
ax.plot(x2,y2,'k--',linewidth=1.)
ax.plot((x3[0],x3[0]),(y3[0],0),'k:',linewidth=1.)
#ax.plot((x3[1],x3[1]),(y3[1],0),'k:',linewidth=1.)
ax.plot((0,x3[0]),(y3[0],y3[0]),'k:',linewidth=1.)
#ax.plot((0,x3[1]),(y3[2],y3[2]),'k:',linewidth=1.)
#ax.plot((0,x3[1]),(funkce(x3[2]),funkce(x3[2])),'k:',linewidth=1.)
#ax.plot(x3,y3,'k--',linewidth=1.)
annotate ('', (x3[0], y3[0]), (x3[1], y3[1]), arrowprops={'arrowstyle':'<->'})
annotate ('', (x3[2], funkce(x3[2])), (x3[1], y3[1]), arrowprops={'arrowstyle':'<->', 'color':'red'})
ax.plot(0.8,log(0.8+0.5),'ro')
ax.text(2.45,.02,"$x$",fontsize=18)
ax.text(0.02,1.55,"$y$",fontsize=18)
ax.text(1.85,0.5,r"$f(x_0+h)-f(x_0)$",fontsize=20)
ax.text(1.25,.3,"$h$",fontsize=20)
ax.text(2.45,1,r"$y=f(x)$",fontsize=18)

ax.text(-0.05,0.24,"$f(x_0)$",fontsize=18, ha='right')
ax.text(0.75,-0.05,"$x_0$",fontsize=18, va='top')
#ax.text(0,0.8,"$f(x_0+h)$",fontsize=18, ha='right')
ax.minorticks_on()


#
#
#
#
#

ax2 = fig.add_subplot(212)
 
#arrow_length = 10
# X-axis arrow
#ax2.annotate('', xy=(1, 0), xycoords=('axes fraction', 'data'), 
#            xytext=(arrow_length, 0), textcoords='offset points',
#            ha='left', va='center',
#            arrowprops=dict(arrowstyle='<-', fc='black'))


for direction in ["left","bottom"]:
	ax2.spines[direction].set_position('zero')
	ax2.spines[direction].set_smart_bounds(True)
for direction in ["right","top"]:
	ax2.spines[direction].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
 
#ax2.grid(False)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_ylim(-0.2,1.5)
ax2.set_xlim(-0.2,2.4)
ax2.plot(x1,y1,'g',linewidth=3.)
ax2.plot(x2,y2,'k--',linewidth=1.)
ax2.plot((x3[0],x3[0]),(y3[0],0),'k:',linewidth=1.)
#ax2.plot((x3[1],x3[1]),(y3[1],0),'k:',linewidth=1.)
ax2.plot((0,x3[0]),(y3[0],y3[0]),'k:',linewidth=1.)
#ax2.plot((0,x3[1]),(y3[2],y3[2]),'k:',linewidth=1.)
#ax2.plot((0,x3[1]),(funkce(x3[2]),funkce(x3[2])),'k:',linewidth=1.)
#ax2.plot(x3,y3,'k--',linewidth=1.)
annotate ('', (x3[0], y3[0]), (x3[1], y3[1]), arrowprops={'arrowstyle':'<->'})
annotate ('', (x3[2], y3[2]), (x3[1], y3[1]), arrowprops={'arrowstyle':'<->', 'color':'red'})
ax2.plot(0.8,log(0.8+0.5),'ro')
ax2.text(2.45,.02,"$x$",fontsize=18)
ax2.text(0.02,1.55,"$y$",fontsize=18)
ax2.text(1.85,0.5,r"$f^{\,\prime}(x_0)h$",fontsize=20)
ax2.text(1.25,.3,"$h$",fontsize=20)
ax2.text(2.45,1,r"$y=f(x)$",fontsize=18)

ax2.text(-0.05,0.24,"$f(x_0)$",fontsize=18, ha='right')
ax2.text(0.75,-0.05,"$x_0$",fontsize=18, va='top')
#ax2.text(0,0.8,"$f(x_0+h)$",fontsize=18, ha='right')
ax2.minorticks_on()

fig.show()
fig.savefig("derivace.png",bbox_inches="tight",\
	pad_inches=.15)
