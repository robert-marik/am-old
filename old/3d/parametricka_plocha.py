from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#plt.xkcd()

fig=plt.figure()
ax=axes3d.Axes3D(fig,azim=30,elev=30)

ax.set_xlabel('X')
#ax.set_xlim(xmin, xmax)
ax.set_ylabel('Y')
#ax.set_ylim(ymin, ymax)
ax.set_zlabel('Z')
ax.set_zlim(0, 1.4)
#ax.axis("off")


u=np.linspace(0,1,40)
v=np.linspace(0,1,40)
U, V=np.meshgrid(u,v)

X=U
Y=2*V
Z=np.sqrt(1-X**2)

ax.plot_surface(X, Y, Z, lw=0, cstride = 3, rstride=3, alpha=0.1)
ax.plot_surface(Y, X, Z, lw=0, cstride = 3, rstride=3, alpha=0.1)

X=U
Y=U*V
Z=np.sqrt(1-X**2)

ax.plot_surface(X, Y, Z, alpha=.45, lw=0.1, cstride = 3, rstride=3)
ax.plot_surface(Y, X, Z, alpha=.45, lw=0.1, cstride = 3, rstride=3)

#ax.axis("off")

plt.savefig('parametricka_plocha.png')
