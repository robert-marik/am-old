% Diferenciální rovnice druhého řádu

https://youtu.be/a308Zs_6bq0

# Okrajová úloha

Ukažte, že úloha
$$y''-my=0, \quad y(0)=0=y(1), \ m>0$$
má pouze nulové řešení.

<div class=reseni>

Charakteristcká rovnice je $$\lambda^2-m=0$$ s reálnými kořeny $\lambda_{1,2}=-\sqrt m$.
Obecným řešením je funkce 
$$y(t)=C_1 e^{\sqrt m t} + C_2 e^{-\sqrt m t}$$
a dosazením získáváme
$$y(0)=C_1  + C_2 =0$$
a
$$y(1)=C_1 e^{\sqrt m} + C_2 e^{-\sqrt m}=0.$$
Z první rovnice dostáváme $C_2=-C_1$ a druhá rovnice má tvar
$$C_1 e^{\sqrt m} - C_1 e^{-\sqrt m}=0.$$
Odsud
$$C_1 (e^{\sqrt m} - e^{-\sqrt m})=0 $$
a
$C_1=0$. Poto však $C_2=-C_1=0$ a řešení se redukuje na 
$$y(t)=0 e^{\sqrt m t} + 0 e^{-\sqrt m t}=0$$
tj. na konstantní nulovou funkci.
</div>


# Separce proměnných ve vlnové rovnici, kmity struny

Rovnice kmitů struny je (po eliminaci konstant)
$$\frac{\partial^2 u}{\partial t^2}=\frac{\partial^2 u}{\partial x^2}$$
s nulovými okrajovými podmínkami na koncích. Je-li délka struny $l$, platí  pro
výchylku $u(x,t)$ podmínky $u(0,t)=u(l,t)$ v libovolném čase $t$.

Budeme řešení hledat ve tvaru $u(x,t)=\varphi(x)\psi(t)$, kde $\varphi$ a $\psi$ jsou funkcemi jedné proměnné.
Platí
$$\frac{\partial^2 u}{\partial t^2}=\varphi(x)\psi''(t), \quad \frac{\partial^2 u}{\partial x^2}=\varphi''(x) \psi(t)$$
a rovnice má tvar
$$\varphi(x)\psi''(t)=\varphi''(x)\psi (t).$$
Vydělením této rovnice součinem $\varphi(x)\psi(t)$ dostáváme
$$\frac {\psi''(t)}{\psi(t)}=\frac{\varphi''(x)}{\varphi (x)}.$$
Toto je rovnice, kde levá strana je funkcí proměnné $t$ a pravá strana funkcí proměnné $x$. Obě proměnné jsou však nezávislé a uvedená rovnost může být splněna jen tehdy, když se rovnají společné konstantě. Označme tuto konstantu $-\lambda^2$. Platí tedy
$$\frac {\psi''(t)}{\psi(t)}=-\lambda ^2,\quad \frac{\varphi''(x)}{\varphi (x)}=-\lambda ^2.$$
První rovnice představuje lineární diferenciální rovnici druhého řádu
$$\psi''+\lambda^2\psi=0.$$
Druhá rovnice představuje lineární diferenciální rovnici druhého řádu
$$\varphi''+\lambda^2\varphi=0$$
a okrajové podmínky si vynucují platnost vztahů $\varphi(0)=\varphi(l)=0$. Máme tedy Dirichletovu úlohu na vlastní čísla a vlastní funkce, jak jsme ji použili [v přednášce](http://user.mendelu.cz/marik/am/slidy/11/). Řešením je funkce $\varphi(x)=\sin\left (k\frac{\pi}l x\right)$, kde $k\in\mathbb N$.


