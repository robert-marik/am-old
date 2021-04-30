# Using the magic encoding
# -*- coding: utf-8 -*-


bez_znacek = True
bez_znacek = False

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.view_init(elev=40)


# pocatecni hodnoty
xmin=-15
xmax=15
ymin=-15
ymax=15
zmin=0
zmax=20


delkax=2    # delka obdelnicku ve smeru x
delkay=2  # delka obdelnicku ve smeru y
delkaz=1  # delka obdelnicku ve smeru y

outputfile="3d_krivka" # jmeno vystupniho souboru
posun_z=-30  # rovina ve ktere se kresli vrstevnice

T = np.linspace(0, 6*np.pi, 360,endpoint=True)
X = T*np.cos(T)
Y = T*np.sin(T)
Z = T


# if bez_znacek:
#     plt.setp(ax, xticks=[], yticks=[], zticks=[])

ax.plot(X,Y,Z, color='#006131')

ax.set_xlabel('x')
ax.set_xlim(xmin, xmax)
ax.set_ylabel('y')
ax.set_ylim(ymin, ymax)
ax.set_zlabel('z')
ax.set_zlim(zmin, zmax)


plt.savefig(outputfile+".png",bbox_inches="tight", pad_inches=.15)
plt.savefig(outputfile+".svg",bbox_inches="tight", pad_inches=.15)

# convert -delay 20 movie*.png animation.gif && rm movie
