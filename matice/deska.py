import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(1,(8,8))
ax = fig.add_subplot(111)

plt.axes().set_aspect('equal', 'datalim')

plt.xkcd()
plt.axis('off')

xmin, xmax, ymin, ymax = 0, 3, 0, 3

plt.plot([0,3,3,0,0],[0,0,3,3,0], color='b')
plt.plot([0,3],[1,1], color='b')
plt.plot([0,3],[2,2], color='b')
plt.plot([1,1],[0,3], color='b')
plt.plot([2,2],[0,3], color='b')

plt.savefig("deska.svg")
plt.savefig("deska.png")
