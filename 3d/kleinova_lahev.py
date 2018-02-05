import mpl_toolkits.mplot3d.axes3d as axes3d
import matplotlib.pyplot as plt
from numpy import *
plt.xkcd()

def surf(u, v):
    """
    http://paulbourke.net/geometry/klein/
    """
    half = (0 <= u) & (u < pi)
    r = 4*(1 - cos(u)/2)
    x = 6*cos(u)*(1 + sin(u)) + r*cos(v + pi)
    x[half] = (
        (6*cos(u)*(1 + sin(u)) + r*cos(u)*cos(v))[half])
    y = 16 * sin(u)
    y[half] = (16*sin(u) + r*sin(u)*cos(v))[half]
    z = r * sin(v)
    return x, y, z

u, v = linspace(0, 2*pi, 80), linspace(0, 2*pi, 80)
ux, vx =  meshgrid(u,v)
x, y, z = surf(ux, vx)

fig = plt.figure()
ax = fig.gca(projection = '3d')
plot = ax.plot_surface(x, y, z, rstride = 2, cstride = 2, linewidth=0.3)

outputfile="kleinova_lahev.png" # jmeno vystupniho souboru
plt.savefig(outputfile)
