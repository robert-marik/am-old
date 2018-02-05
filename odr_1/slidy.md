% Diferenciální rovnice prvního řádu
% Robert Mařík
% jaro 2014, jaro 2015


# Obyčejná diferenciální rovnice prvního řádu

Obyčejná diferenciální rovnice je rovnice, kde vystupuje neznámá
funkce a její derivace. Setkáváme se s\ ní například všude tam, kde
rychlost růstu nebo poklesu veličiny souvisí s\ její
velikostí. Například rychlost s\ jakou se mění teplota horkého tělesa
je funkcí teploty samotné. Rychlost tepelné výměny mezi dvěma tělesy
je totiž úměrná rozdílu jejich teplot (Newtonův zákon).

<div class=sloupce>

<div>

<def>

> **Definice.** *Obyčejnou diferenciální rovnicí prvního řádu rozřešenou vzhledem
> k derivaci* (stručněji též diferenciální rovnicí, DR) s neznámou $y$
> rozumíme rovnici tvaru $$ y'=\varphi(x,y) \tag{ODE}$$ kde $\varphi$ je funkce
> dvou proměnných.

</def>

(anglicky ordinary differential equation, ODE)

</div>

**Další formy zápisu**:
  $$\frac{\mathrm{d}y}{\mathrm{d}x}=\varphi(x,y)$$
  $${\mathrm{d}y}=\varphi(x,y)\mathrm{d}x$$
  $${\mathrm{d}y}-\varphi(x,y)\mathrm{d}x=0$$

</div>

# Příklady diferenciálních rovnic

Z\ fyzikálního hlediska diferenciální rovnice popisuje mechanismus
vývoje systému.

<div class="sloupce">

<div>

### Tepelná výměna

Rychlost tepelné výměny mezi dvěma tělesy je úměrná rozdílu jejich
teplot (Newtonův zákon).  Tento proces je tedy možno modelovat
diferenciální rovnicí
$$
  y'=-k(y-T)
$$
teplota $y$ horkého tělesa se mění (rychlost změny je derivace $y'$)
tak, že klesá (znaménko minus) rychlostí úměrnou (konstanta $k$)
teplotnímu rozdílu mezi teplotou tělesa a teplotou okolí (člen $y-T$).

</div>

<div>

### Vývoj populace

Udává-li $y$ velikost určité populace, $K$ nosnou kapacitu prostředí,
$h(y)$ intenzitu lovu a $r\left(1-\frac yK\right)$ specifickou míru
růstu populace (rychlost s jakou se velikost populace zvětšuje
vztažená na jednotkové množství populace, přičemž tato rychlost klesá
s tím, jak se velikost populace přibližuje k nosné kapacitě
prostředí), je možno populaci modelovat rovnicí
$$y'=ry\left(1-\frac yK\right)-h(y).$$

Podle velkosti koeficientů v této rovnici dělíme živočichy na
[r-stratégy a
K-stratégy](http://cs.wikipedia.org/wiki/%C5%BDivotn%C3%AD_strategie),
toto dělení odráží, jak se snaží druh přežít.

</div>
</div>


# Cauchyova úloha, počáteční podmínka 

Diferenciální rovnice udává scénář vývoje systému. K\ jednoznačnému
předpovězení budoucího stavu je ovšem nutno znát nejenom, jaký
mechanismus ovlivňuje vývoj systému, ale také stav současný.

<def>

> **Definice.** Nechť $x_0$, $y_0$ jsou reálná čísla. Úloha najít
> řešení rovnice  
> $$  y'=\varphi(x,y), \tag{ODE}$$
> které splňuje zadanou *počáteční podmínku*
> $$  y(x_0)=y_0 \tag{IC}$$
> se nazývá *počáteční* (též *Cauchyova*) *úloha*. 
> 
> Řešení Cauchyovy úlohy nazýváme též *partikulárním řešením
> rovnice*. Graf libovolného partikulárního řešení se nazývá *integrální
> křivka*.

</def>

(anglicky initial condition, IC, initial value problem, IVP)



# Geometrická interpretace ODE

<div class=sloupce>
Protože derivace funkce v bodě udává směrnici tečny ke grafu funkce
v tomto bodě, lze rovnici $$y'=\varphi(x,y)\tag{ODE}$$ chápat jako předpis, který
každému bodu v rovině přiřadí směrnici tečny k integrální křivce,
která tímto bodem prochází.  Sestrojíme-li v dostatečném počtu
(například i náhodně zvolených) bodů $[x,y]$ v rovině vektory
$(1,\varphi(x,y))$, obdržíme **směrové pole diferenciální rovnice** —
systém lineárních elementů, které jsou tečné k integrálním křivkám.

Počáteční podmínka $y(x_0)=y_0$ geometricky vyjadřuje skutečnost, že graf
příslušného řešení prochází v rovině bodem $[x_0,y_0]$. Má-li tato
počáteční úloha jediné řešení, neprochází bodem $[x_0,y_0]$ žádná další
křivka. Má-li každá počáteční úloha jediné řešení (což bude pro nás
velice častý případ), znamená to, že integrální křivky se *nikde
neprotínají*.

Vrstevnice funkce $\varphi(x,y)$ mají tu vlastnost, že derivace
integrálních křivek podél každé z\ vrstevnic je konstantní. Proto tyto
křivky nazýváme **isokliny**.

<div class=sloupce>

![Směrové pole diferenciálni rovnice](smerove_pole.png)

![Směrové pole diferenciálni rovnice, integrální křivky, isokliny](smerove_pole_2.png)

</div>
</div>


# Obecné a partikulární řešení

<div class=sloupce>

Řešení diferenciální rovnice je nekonečně mnoho. Zpravidla je dokážeme
zapsat pomocí jediného vzorce, který obsahuje nějakou (alespoň do
jisté míry libovolnou) konstantu $C$. Takový vzorec se nazývá **obecné
řešení rovnice**. Pokud není zadána počáteční podmínka a mluvíme o
**partikulárním řešení**, máme tím na mysli jednu libovolnou funkci
splňující diferenciální rovnici.

**Příklad:** Obecným řešením diferenciální rovnice $$y'=2xy$$ je
  $$y=Ce^{x^2}, \quad C\in\mathbb{R}.$$ Žádná jiná řešení neexistují,
  všechna řešení se dají zapsat v tomto tvaru pro nějakou vhodnou
  konstantu $C$.  Partikulárním řešením je například
  $y=5e^{x^2}$. Řešením počáteční úlohy $$y'=2xy, \quad y(0)=3$$ je
  $$y=3e^{x^2}.$$

**Online řešiče ODE (symbolicky):**

* [Wolfram Alpha](http://www.wolframalpha.com/input/?i=solve+y%27%2Bx*y%3Dx%2Fy)
* [Mathematical Assistant on Web](http://um.mendelu.cz/maw-html/index.php?lang=cs&form=ode&ode2=y%27%2Bx*y%3Dx%2Fy)
* [Sage](http://user.mendelu.cz/marik/akademie/sagecell.php?short=1&in=y%3Dfunction%28%27y%27%2Cx%29%0A%0A%23+rovnice+y%27%3Dy%2Fx%2B1%0Arovnice+%3D+diff%28y%2Cx%29+%3D%3D+y%2Fx+%2B+1%0A%0A%23+%3Fe%3Fen%3F%0Adesolve%28rovnice%2C+y%29.show%28%29%0A%23+%3Fe%3Fen%3F+v+rozn%3Fsoben%3Fm+tvaru%0Adesolve%28rovnice%2C+y%29.expand%28%29.show%28%29)


</div>

# Numerické řešení IVP

<div class=sloupce>

Řešení počáteční úlohy lze numericky aproximovat poměrně snadno:
začneme v bodě zadaném počáteční podmínkou a v okolí tohoto bodu
nahradíme integrální křivku její tečnou. Tím se dostaneme do dalšího
bodu, odkud opět integrální křivku aproximujeme tečnou.

Směrnici tečny zjistíme z diferenciální rovnice, buď přímo z derivace
(Eulerova metoda), nebo poněkud rafinovaněji, kdy bereme v úvahu
i konvexnost či konkávnost a fakt, že se derivace mění s měnícím se
$x$ i $y$ (metoda Runge–Kutta). Stačí tedy mít zvolen *krok* numerické
metody (délku intervalu, na kterém aproximaci tečnou použijeme) a
výstupem metody bude aproximace integrální křivky pomocí lomené čáry.

<div>

**Online řešiče ODE (numericky):**

* [dfield](http://math.rice.edu/~dfield/dfpp.html)
* [Sage](http://user.mendelu.cz/marik/akademie/sagecell.php?short=1&in=f%28x%2Cy%29%3Dy*%28x-y%29%0A%0Aymin%2C+ymax+%3D+0%2C+2%0A%0Aics1%3D%5B0%2C0.1%5D%0Aics2%3D%5B0%2C1%5D%0A%0AP2%3Ddesolve_rk4%28f%28x%2Cy%29%2Cy%2Cics%3Dics1%2Civar%3Dx%2Cend_points%3D%5B0%2C3%5D%2Coutput%3D%27slope_field%27%29%0AP1%3Ddesolve_rk4%28f%28x%2Cy%29%2Cy%2Cics%3Dics2%2Civar%3Dx%2Cend_points%3D%5B0%2C3%5D%2Coutput%3D%27plot%27%2C+color%3D%27red%27%29%0A%0A%28P1%2BP2%29.show%28ymax%3Dymax%2Cymin%3Dymin%29)

</div>

![Metoda Runge Kutta s velmi dlouhým krokem (modrou barvou, jde jasně
 vidět aproximace lomenou čarou). Přesné řešení je nakresleno šedou
 barvou.](rk.png)

</div>

# ODE se separovanými proměnnými

<div class=sloupce>

<def>

> **Definice.** Diferenciální rovnice tvaru
> $$    y'=f(x)g(y) \tag{S}$$
> kde $f$ a $g$ jsou funkce spojité na (nějakých) otevřených intervalech
> se nazývá *obyčejná diferenciální rovnice se separovanými proměnnými.*

</def>

**Příklad:** Rovnice $$y'+xy +xy^2=0$$ je rovnicí se separovanými
  proměnnými, protože je možno ji zapsat ve tvaru $$y'=-xy(y+1).$$
  Rovnice $$y'=x^2-y^2$$ není rovnice se separovatelnými proměnnými.

**Test separovatelnosti proměnných:** Diferenciální rovnice
  $$y'=\varphi(x,y)$$ je rovnicí se separovanými proměnnými právě
  tehdy, když existují funkce $f(x)$ a $g(y)$ takové, že
  $$\varphi(x,y)=f(x)g(y). $$ Pokud je $\varphi$ nezáporná a
  dostatečně hladká na nějaké otevřené konvexní množině, je rovnice
  rovnicí se separovanými proměnnými právě tehdy, když platí
  $$\begin{vmatrix}\varphi&\frac{\partial}{\partial x}\varphi\\
  \frac{\partial}{\partial y}\varphi&\frac{\partial^2}{\partial
  x\partial y}\varphi \end{vmatrix}=0.$$

</div>

# Řešení ODE se separovanými proměnnými

<div class=sloupce>

1.  Má-li algebraická rovnice $g(y)=0$ řešení $k_1$, $k_2$, …, $k_n$,
    jsou konstantní funkce $y\equiv k_1$, $y\equiv k_2$, …,
    $y\equiv k_n$ řešeními rovnice.

2.  Pracujme na intervalech, kde $g(y)\neq 0$. Formálně nahradíme
    derivaci $y'$ podílem diferenciálů $\frac{\mathrm{d}y}{\mathrm{d}x}$
    $$   \frac{\mathrm{d}y}{\mathrm{d}x}=f(x)g(y).$$

3.  Odseparujeme proměnné
    $$          \frac{\mathrm{d}y}{g(y)}=f(x)\mathrm{d}x.$$

4.  Získanou rovnost integrujeme
    $$
          \int \frac{\mathrm{d}y}{g(y)}=\int f(x)\mathrm{d}x+C.$$

5.  Pokud je zadána počáteční podmínka, je možné ji na tomto místě
    dosadit do obecného řešení a určit hodnotu konstanty $C$. Tuto
    hodnotu poté dosadíme zpět do obecného řešení a obdržíme řešení
    *partikulární*.

6.  Pokud je to možné, převedeme řešení (obecné nebo partikulární) do
    explicitního tvaru (vyjádříme odsud $y$).


</div>


# Proč funguje postup z předchozího slidu?

<div class=sloupce>


Výraz $\frac{\mathrm{d}y}{\mathrm{d}x}$ je derivace, nikoliv podíl,
proto je s podivem, že výše uvedený postup funguje. Berme jej prosím
jako mnemotechinckou pomůcku při řešení a představme si
sofistikovanější zdůvodnění tohoto postupu (pro případ $g(y)\neq 0$) založené na integrování a substituci v neučitém integrálu.

$$ 
 \begin{aligned}    
  y'&=f(x)g(y)\\
  \frac{1}{g(y)} y' &= f(x) \\
  \int \frac{1}{g(y(x))} y'(x)\mathrm{d}x &= \int f(x) \mathrm{d}x\\
  \int \frac{1}{g(y)} \mathrm{d}y &= \int f(x) \mathrm{d}x
 \end{aligned}
$$

Za povšimnutí také stojí fakt, že ekvivalentní vyjádření rovnice ve tvaru
$$ f(x)\mathrm{d}x - \frac{1}{g(y)} \mathrm{d}y = 0 $$
obsahuje na levé straně totální diferenciál. Kmenová funkce tohoto diferenciálu je 
$$F(x,y)=   \int f(x) \mathrm{d}x - \int \frac{1}{g(y)} \mathrm{d}y $$
a řešení rovnice jsou tvaru $$F(x,y)=C, \qquad C\in\mathbb{R}.$$ Pohlížíme-li
na tento vztah jako na implicitně zadanou funkci a počítáme-li pomocí
aparátu funkce dvou proměnných derivaci této funkce, dostaneme přesně vztah 
$$  y'=f(x)g(y). $$

</div>

# Existence a jednoznačnost řešení

> **Věta o existenci a jednoznačnosti řešení:** Je-li $g(y_0)\neq 0$, je řešení počáteční
> úlohy $$y'=f(x)g(y), \qquad y(x_0)=y_0,$$ které obdržíme pomocí
> postupu z předchozích odstavců, definované a jednoznačně určené v nějakém okolí
> bodu $x_0$.

**Vzorec pro řešení IVP pro rovnici se separovatelnými proměnnými:**
Partikulární řešení počáteční úlohy $$y'=f(x)g(y), \qquad y(x_0)=y_0$$
lze psát též přímo ve tvaru určitého integrálu $$\int_{y_0}^y\frac
{\mathrm{d}t}{g(t)}=\int_{x_0}^x f(t)\mathrm{d}t$$


# Lineární diferenciální rovnice prvního řádu
<div class=sloupce>

<def>

> **Definice.** Nechť funkce $a$, $b$ jsou spojité na intervalu $I$.
> Rovnice
> $$  y'+a(x)y=b(x) \tag{LDE}$$
> se nazývá *obyčejná lineární diferenciální rovnice prvního řádu*
> (zkráceně píšeme LDE). Je-li navíc $b(x)\equiv 0$ na $I$, nazývá se
> rovnice *homogenní*, v opačném případě *nehomogenní*.

</def>
<div>
> **Věta o řešitelnosti LDE.** Jsou-li funkce $a$, $b$ spojité na
> intervalu $I$, $x_0\in I$ a $y_0\in\mathbb{R}$ libovolné, má každá počáteční
> úloha právě jedno řešení definované na celém
> intervalu $I$.
</div>

<def>

> **Definice.** Buď dána lineární diferenciální rovnice. Homogenní rovnice, která
> vznikne z\ rovnice nahrazením pravé strany nulovou funkcí, tj.
> rovnice
> $$    y'+a(x)y=0$$
> se nazývá *homogenní rovnice, asociovaná s nehomogenní rovnicí (LDE)*

</def>

Homogenní LDE má vždy (bez
ohledu na konkrétní tvar funkce $a(x)$) konstantní řešení $y=0$, jak lze
ověřit přímým dosazením. Toto řešení se nazývá *triviální řešení*.

</div>

# Operátorová symbolika a linearita operátoru

Definujeme-li na množině všech funkcí
diferencovatelných na intervalu $I$ operátor $L$ vztahem

$$L[y](x)=y'(x)+a(x)y(x)$$

pro každé $x\in I$, je možno LDE a s\ ní
asociovanou homogenní rovnici zapsat v\ krátkém tvaru $L[y]=b(x)$ a
$L[y]=0$.

Operátor $L$ splňuje pro všechna
reálná čísla $C_1$, $C_2$ a všechny diferencovatelné funkce $y_1(x)$,
$y_2(x)$ vztah

$$L[C_1y_1+C_2y_2]=C_1L[y_1]+C_2L[y_2].$$

Vskutku:

$$\begin{aligned}
    L[C_1y_1+C_2y_2](x)&{}=\Bigl(C_1y_1(x)+C_2y_2(x)\Bigr)'+a(x)\Bigl(C_1y_1(x)+C_2y_2(x)\Bigr)\\
    &{}=C_1y_1'(x)+C_2y_2'(x)+a(x)C_1y_1(x)+a(x)C_2y_2(x)\\
    &{}=C_1\Bigl(y_1'(x)+a(x)y_1(x)\Bigr)+C_2\Bigl(y_2'(x)+a(x)y_2(x)\Bigr)\\ 
    &{}=C_1L[y_1](x)+C_2L[y_2](x).
  \end{aligned}$$

# Operátorová symbolika a linearita operátoru (pokračování)

Důsledkem vztahu $$L[C_1y_1+C_2y_2]=C_1L[y_1]+C_2L[y_2],$$
tj. důsledkem skutečnosti že lineární operátor zachovává lineární
kombinaci funkcí jsou vztahy $$L[Cy]=CL[y]$$ (pro $C_2=0$, $C_1=C$, $y_1=y$) a 
$$L[y_1+y_2]=L[y_1]+L[y_2]$$ (pro $C_1=C_2=1$). 

Tedy lineární operátor aplikovaný na
součet je možno zapsat jako součet lineárních operátorů aplikovaných
na jednotlivé sčítance a dále je možno z operátoru vytáhnout ven
multiplikativní konstanty. To jsou obraty dobře známé při výpočtu
derivací a je možné je použít i při dosazování do lineárního
operátoru.

# Násobek řešení homogenní LDE je řešením téže LDE

<div class=sloupce>
Buď $y_{p0}(x)$ řešením rovnice $$L[y]=0,$$ tj. nechť platí
$L[y_{p0}]=0$. Buď $C\in\mathbb{R}$ libovolné reálné číslo.

**Násobek řešení hom. LDE je také řešením.**

Ukážeme, že $y_1=Cy_{p0}(x)$ je řešením téže rovnice, tj. že platí $L[y_1]=0$. Toto však platí, neboť
$$L[y_1]=L[Cy_{p0}]=CL[y_{p0}]=C\cdot 0=0.$$

Máme-li jedno řešení homogenní lineární diferenciální rovnice,
vynásobením konstantou dostaneme další řešení téže rovnice. Ještě
ukážeme, že pokud řešení které násobíme není triviální, dostaneme
tímto způsobem dokonce všechna řešení.

<div>
**$C$-násobek nenulového řešení hom. LDE je obecným řešením.**

Ukážeme, že je-li $y_{p0}(x)$ nenulovým řešením rovnice $L[y]=0$, je
obecným řešením této rovnice $$y(x)=Cy_{p0}(x), \qquad C\in\mathbb{R}.$$ Vskutku, podle
předchozího se jedná o řešení a stačí ukázat, že zde jsou zahrnuta
všechna možná řešení. Stačí ukázat, že pro libovolnou počáteční
podmínku $y(x_0)=y_0$, kde $x_0,y_0\in\mathbb{R}$ je možno
partikulární řešení IVP dostat vhodnou volbou konstanty. Toto je však
triviální, protože funkce $$y(x)=\frac{y_0}{y_{p0}(x_0)}y_{p0(x)}$$ má
požadované vlastnosti.

</div>
</div>

# Obecné řešení homogenní LDE

Uvažujme homogenní LDE
$$y'+a(x)y=0. \tag{HLDE}$$
Přepsáním do 
$$y'=-a(x)y$$
a přímým dosazením vidíme, že 
$$y_{p0}=e^{-\int a(x)\mathrm{d}x}$$
je řešením této rovnice. Obecné řešení rovnice (HLDE) je potom 
$$y=Ce^{-\int a(x)\mathrm{d}x}.$$

# Jedno řešení nehomogenní LDE stačí

Je-li $y_p$ řešením nehomogenní LDE
$$y'+a(x)y=b(x),$$ je obecným řešením této rovnice
$$y(x)=Cy_{p0}(x)+y_p(x),$$
kde $Cy_{p0}(x)$ je obecným řešením asociované homogenní LDE.

Vskutku, jestliže $L[y_p]=b(x)$ a $L[y_{p0}(x)]=0$, potom 
$$L[y]=L[Cy_{p0}+y_p]=CL[y_{p0}]+L[y_p]=C\cdot 0+b(x)=b(x).$$
Funkce $y(x)$ tedy je řešením. 

Pokud potřebujeme splnit libovolnou počáteční podmínku $y(x_0)=y_0$,
kde $x_0,y_0\in\mathbb{R}$, stačí vzít řešení
$$y(x)=\frac{y_0-y_{p}(x_0)}{y_{p0}(x_0)}y_{p0}(x)+y_p(x),$$



# Jedno řešení nehomogenní LDE stačí (pokračování)

<div class=sloupce>
Slovně:

-   Všechna řešení homogenní lineární rovnice jsou násobky jednoho
    libovolného nenulového řešení této rovnice.

-   Součet jednoho libovolného řešení zadané nehomogenní a obecného
    řešení asociované homogenní lineární rovnice je obecným řešením dané
    nehomogenní rovnice.

Stačí tedy najít dvě (do jisté míry speciální) řešení a z\ nich snadno
sestavíme obecné řešení zadané rovnice. 

<div>
**Příklad:** Rovnice $$y'+y=3 \tag{*}$$ má partikulární řešení $y=3$ (vidíme
  hned po dosazení). Asociovaná homogenní rovnice $$y'+y=0$$ má obecné
  řešení $y=Ce^{-x}$. Obecné řešení rovnice (*) tedy je 
	  $$y=3+Ce^{-x}.$$
</div>	
</div>	

# Nehomogenní LDE – metoda variace konstanty
 
 <div class=sloupce>
Než začneme hledat řešení
nehomogenní rovnice, prozkoumejme, jak se lineární operátor $L$ chová
vzhledem k\ součinu funkcí. Buďte $u=u(x)$ a $v=v(x)$ funkce. Platí
$$\begin{aligned}
  L[u\cdot v]&{}=\Bigl(uv\Bigr)'+auv\\
  &{}=u'v+uv'+auv\\
  &{}=v\Bigl(u'+au\Bigr)+uv'\\
  &{}=vL[u]+uv'.\end{aligned}$$
Tento výpočet ukazuje, že pokud $L[u]=0$, tj. pokud je funkce $u$
řešením asociované homogenní diferenciální rovnice, je možno řešení
nehomogenní rovnice $L[y]=b(x)$ hledat ve tvaru součinu $y(x)=u(x)v(x)$,
kde funkce $v(x)$ splňuje vztah
$$\begin{aligned}b(x)&=L[u\cdot v]\\&=vL[u]+uv'\\&=0+uv'\\&=uv'.\end{aligned}$$
tj. $$v'(x)=\frac{b(x)}{u(x)}.$$ Odsud však funkci $v$ můžeme nalézt již
pouhou integrací a součin $u(x)v(x)$ poté bude řešením nehomogenní
rovnice. V\ praxi je také obvyklé, že si pamatujeme pouze hlavní myšlenku
– *budeme hledat řešení nehomogenní rovnice ve tvaru součinu nějaké
funkce a řešení asociované homogenní rovnice* – a provádíme všechny
úvahy pro konkrétní funkce $a$, $b$ v\ běžném neoperátorovém označení.

</div>

# Nehomogenní LDE – metoda variace konstanty (pokračování)

 <div class=sloupce> 
Pokud v předchozím volíme $u=e^{-\int a(x)\mathrm{d}x}$, je $$v'=b(x)e^{\int a(x)\mathrm{d}x}$$ a odsud $$v=\int b(x)e^{\int a(x)\mathrm{d}x}\mathrm{d}x.$$ Partikulární řešení je $$uv=e^{-\int a(x)\mathrm{d}x}\int b(x)e^{\int a(x)\mathrm{d}x}\mathrm{d}x$$ a obecné řešení LDE
$$y'+a(x)y=b(x)$$ je 
$$y=Ce^{-\int a(x)\mathrm{d}x}+e^{-\int a(x)\mathrm{d}x}\int b(x)e^{\int a(x)\mathrm{d}x}\mathrm{d}x$$
</div>

# Nehomogenní LDE – metoda integračního faktoru

 <div class=sloupce>
Protože platí
$$\left(y e^{\int a(x)\mathrm{d}x}\right)'=y'e^{\int a(x)\mathrm{d}x}+y a(x) e^{\int a(x)\mathrm{d}x},$$
je možno rovinci 
$$y'+a(x)y=b(x)$$
přepsat do tvaru
$$y'e^{\int a(x)\mathrm{d}x}+a(x)ye^{\int a(x)\mathrm{d}x}=b(x)e^{\int a(x)\mathrm{d}x}$$
a odsud
$$\left (y e^{\int a(x)\mathrm{d}x}\right)'=b(x)e^{\int a(x)\mathrm{d}x}.$$
Integrací dostáváme
$$y e^{\int a(x)\mathrm{d}x}=\int b(x)e^{\int a(x)\mathrm{d}x}\mathrm{d}x+C$$
a explicitní tvar řešení je
$$y =Ce^{-\int a(x)\mathrm{d}x}+e^{-\int a(x)\mathrm{d}x}\int b(x)e^{\int a(x)\mathrm{d}x}\mathrm{d}x$$
</div>