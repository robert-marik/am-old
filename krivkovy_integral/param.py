# Using the magic encoding
# -*- coding: utf-8 -*-

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()

matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{euler,amsmath}\def\sin{\mathop{sin}}\def\cos{\mathop{cos}}"]

import sys
if len(sys.argv) > 1:
    priklad = sys.argv[1]
else:
    priklad = "1"

plt.figure(1)

tmin=0
tmax=2*np.pi

outputfile="parametricke_krivky.png"

def fx(t):
    return np.cos(t)

def fy(t):
    return np.sin(t)

t= np.linspace(tmin, tmax, 200, endpoint=True)

xmin, xmax, ymin, ymax = -1.1, 1.1, -1.3, 1.3


x=fx(t)
y=fy(t)

plt.figure(0)
#ax1 = plt.subplot2grid((2,3), (0,0))
#ax2 = plt.subplot2grid((2,3), (0,1), colspan=2)
#ax3 = plt.subplot2grid((2,3), (1, 0))
#ax4 = plt.subplot2grid((2,3), (1, 1), colspan=2)

import matplotlib.gridspec as gridspec
gs = gridspec.GridSpec(2, 2,
                       width_ratios=[1,2],
                       height_ratios=[1,1], hspace=0.3
                       )
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax4 = plt.subplot(gs[3])
#ax1 = plt.subplot2grid((2,2), (0,0))
#ax2 = plt.subplot2grid((2,2), (0,1))
#ax3 = plt.subplot2grid((2,2), (1, 0))
#ax4 = plt.subplot2grid((2,2), (1, 1))

ax2.set_title(r'$\begin{aligned}x&=\cos(t)\\y&=\sin(t), t\in [0,2\pi]\end{aligned}$', va='center')
ax4.set_title(r'$\begin{aligned}x&=\cos(2\pi t^2)\\y&=\sin(2\pi t^2), t\in [0,1]\end{aligned}$', va='center')

#axes().set_aspect('equal', 'datalim')


ax1.plot(x, y, 'k', color='green', lw=3)
#ax1.set_aspect('equal', 'datalim')

ax2.plot(t, x, 'k', color='red', lw=3, label='$x(t)$')
ax2.plot(t, y, 'k', color='blue', lw=3, label='$y(t)$')

#ax3.set_aspect('equal', 'datalim')

t2= np.linspace(0, 1, 200, endpoint=True)

x2=fx(t2**2*2*np.pi)
y2=fy(t2**2*2*np.pi)

ax3.plot(x2, y2, 'k', color='green', lw=3)
#axes().set_aspect('equal', 'datalim')
#ax2 = plt.axes(aspect='equal')



ax4.plot(t2, x2, 'k', color='red', lw=3, label='$x(t)$')
ax4.plot(t2, y2, 'k', color='blue', lw=3, label='$y(t)$')
#axes().set_aspect('equal', 'datalim')

ax2.legend(loc='lower left', shadow=True)
ax4.legend(loc='lower left', shadow=True)


for i in (ax1,ax2,ax3,ax4):
    i.spines['right'].set_color('none')
    i.spines['top'].set_color('none')
    i.xaxis.set_ticks_position('bottom')
    i.spines['bottom'].set_position(('data',0))
    i.yaxis.set_ticks_position('left')
    i.spines['left'].set_position(('data',0))
    i.yaxis.set_ticks([])
    i.xaxis.set_ticks([])
    i.set_ylim(ymin, ymax)
    i.set_xlabel('$t$')
    i.set_ylabel('$x$, $y$', ha='right')
    i.xaxis.set_label_coords(1.05, 0.5)
    i.yaxis.set_label_coords(-0.01, 1.07)

for i in (ax1,ax3):
    i.set_xlim(xmin, xmax)
    i.set_xlabel('$x$')
    i.set_ylabel('$y$')
    i.xaxis.set_label_coords(1.05, 0.5)
    i.yaxis.set_label_coords(0.5, 1.05)


ax2.set_xlim(0, tmax)
ax4.set_xlim(0, 1)

plt.savefig(outputfile)
