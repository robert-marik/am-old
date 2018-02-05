# Parametricky zadana krivka
t=var('t')

import matplotlib
matplotlib.pyplot.xkcd()

x(t)=(t)*cos(t)
y(t)=(t)*sin(t)
tmin,tmax=0,2*pi
pocet=20

#x(t)=t
#y(t)=cos(t)


P=parametric_plot([x, y], (tmin,tmax), color='red', thickness=3)
for i in range (1,pocet):
    t0=tmin+i/pocet*(tmax-tmin)
    deltax=diff(x(t),t).subs(t=t0).n()
    deltay=diff(y(t),t).subs(t=t0).n()
    posun=vector((deltax,deltay))
    P=P+arrow( (x(t0), y(t0)), vector((x(t0),y(t0)))+posun/norm(posun) )
    
show(P,aspect_ratio=1)
