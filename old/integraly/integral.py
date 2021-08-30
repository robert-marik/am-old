import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()

def func(x):
    return 1+(1/(1+(x-2)**2))

def func2(x):
    return 1.76


a, b = 0.5, np.exp(1) # integral limits
X = np.linspace(0.1, 3,50)

ymin, ymax = -0.2,2.5

fig = plt.figure(figsize=(8,8))
ax=fig.add_subplot(212)

ax.set_ylim(ymin, ymax)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

Y = func(X)
Y2 = [func2(i) for i in X]



ax.plot(X, Y, color='#006131', linewidth=3)

from matplotlib.patches import Polygon
# Make the shaded region
ix = np.linspace(a, b)
iy = func(ix)
iy2 = [func2(i) for i in X]
verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)


print X
print Y2

ax2 = fig.add_subplot(211)
ax2.text(0.5 * (a + b), 1, r"$S=(b-a)f(x)$",
         horizontalalignment='center', fontsize=20)

ax2.text(0.25 * (a + 3*b), func2(2)+0.2, r"$f(x)\equiv\mathrm{konst}$",
         horizontalalignment='center', fontsize=20)

ax.text(0.5 * (a + b), 1, r"$S=\int_a^b f(x)\mathrm{d}x$",
         horizontalalignment='center', fontsize=20)
ax.text(0.25 * (a + 3*b), func2(2)+0.4, r"$f(x)\neq\mathrm{konst}$",
         horizontalalignment='center', fontsize=20)

ax2.plot(X, Y2, color='#006131', linewidth=3)
ax2.set_ylim(ymin, ymax)
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.spines['bottom'].set_position(('data',0))
ax2.yaxis.set_ticks_position('left')
ax2.spines['left'].set_position(('data',0))

# Make the shaded region
verts = [(a, 0)] + list(zip(ix, iy2)) + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax2.add_patch(poly)

ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'),fontsize=20)
ax.set_yticks([])
ax2.set_xticks((a, b))
ax2.set_xticklabels(('$a$', '$b$'),fontsize=20)
ax2.set_yticks([])

plt.savefig("integral.png",bbox_inches="tight", pad_inches=.15)

