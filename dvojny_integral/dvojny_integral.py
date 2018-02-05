from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xpos = np.arange(0, 4, 1)
ypos = np.arange(0, 4, 1)
xpos, ypos = np.meshgrid(xpos, ypos)
xpos = xpos.flatten()
ypos = ypos.flatten()

dx=1
dy=1

def f(i,j): return 25-.52*(i)**2-.62*(j-5)**2

def fp(i,j): 
    A=f_pom(i,j)
    print A
    return (A)

dz=[f(i[0],i[1]) for i in zip(xpos,ypos)]
zpos=[0 for i in zip(xpos,ypos)]

print xpos
print ypos
print dz

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#006131', alpha=0.9)


xmin, xmax, ymin, ymax, zmin, zmax= -1,5.5,-1,5,0,25

X = np.arange(xmin, xmax, 0.25)
Y = np.arange(ymin, ymax, 0.25)
X, Y = np.meshgrid(X, Y)
Z = f(X,Y)


#print Z


ax.set_xlabel('x')
ax.set_xlim(xmin, xmax)
ax.set_ylabel('y')
ax.set_ylim(ymin, ymax)
ax.set_zlabel('f(x,y)')
ax.set_zlim(zmin, zmax)


ax.plot_surface(X, Y, Z, rstride=25, cstride=25, color='gray', zorder=50, alpha=0.15)




fig.savefig("dvojny_integral.png",bbox_inches="tight", pad_inches=.15)




