import numpy as np
import matplotlib.pyplot as plt

plt.xkcd()

Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -Y
V = X+np.exp(Y)
speed = np.sqrt(U*U + V*V)

plt.figure(1,(8,8)) 
plt.streamplot(X, Y, U, V, density=0.5, color="#02ff02", arrowsize=3)
plt.axes().set_aspect('equal', 'datalim')
 
plt.savefig("streamplot.svg",bbox_inches="tight", pad_inches=.15)
plt.savefig("streamplot.png",bbox_inches="tight", pad_inches=.15)
