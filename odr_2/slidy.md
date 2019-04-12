% Lineární diferenciální rovnice prvního a druhého řádu
% Robert Mařík
% 2014–2019

# Lineární operátor


**Operátorem** rozumíme zobrazení, které má na vstupu i na výstupu
funkci. Například pro funkce jedné proměnné mohou být operátory
derivace, druhá derivace, vynásobení funkce funkcí $\ln x$ anebo vnoření zadané funkce do funkce $\ln x$. Tj. pro $y=y(x)$ můžeme uvažovat operátory
$$F_1[y]=\frac{dy}{dx}, \quad
F_2[y]=\frac{d^2y}{dx^2}, \quad 
F_3[y](x)=y(x)\ln(x), \quad 
F_4[y](x)=\ln(y(x)).
$$

\iffalse 

<div class='obtekat'>

![Rovnice s lineárním operátorem jsou silně předvídatelné. Překvapení se nekonají. Proto je (lineární operátory) v matematice máme tak rádi. Zdroj: pixabay.com](prekvapeni.jpg)

</div>

\fi

**Lineárním operátorem** rozumíme zobrazení, které zachovává součet
funkcí a násobek konstantou, tj. platí $$L[y_1+y_2]=L[y_1]+L[y_2]$$ a
$$L[C y_1]=C L[y_1]$$ pro libovolné reálné číslo $C$ a libovolné
funkce $y_1$ a $y_2$ z definičního oboru operátoru $L$.

# Příklady lineárních operátorů

* Operátor derivace, tj. operátor definovaný vztahem $L[y]=\frac{dy}{dx}$ je lineární.
* Buď dána funkce $a(x)$. Operátor násobení funkcí $a(x)$, tj. $L[y](x)=a(x)y(x)$ je lineární.
* Složení (postupná aplikace) lineárních operátorů je lineární operátor. Například tedy
$$\frac{d^2 y}{dx^2}$$ je lineární operátor.
* Součet lineárních operátorů je lineární operátor. 
* Buď pevně dána funkce $a(x)$. Lineární operátor
$$L[y]=\frac{dy}{dx}+a(x)y$$
se nazývá *lineární diferenciální operátor prvního řádu*.
* Buďte pevně dány funkce $p(x)$ a $q(x)$. Lineární operátor
$$L[y]=\frac{d^2y}{dx^2}+p(x)\frac{dy}{dx}+q(x)y$$
se nazývá *lineární diferenciální operátor druhého řádu*.

# Princip superpozice

> Každý lineární operátor zachovává lineární kombinaci funkcí, tj. platí
> $$L[C_1 y_1+C_2 y_2]=C_1 L[y_1]+C_2 L[y_2]$$
> vždy, když $C_{1,2}\in\mathbb{R}$ a $y_{1,2}$ jsou funkce z definičního oboru operátoru $L$.

Plyne přímo rozepsáním
$$
\begin{aligned}L[C_1 y_1+C_2 y_2]&=
L[C_1 y_1]+L[C_2 y_2]\\
&=
C_1 L[y_1]+C_2 L[y_2]
\end{aligned}
$$

# Operátorové rovnice 

Operátorovou rovnicí budeme rozumět rovnici $$L[y]=b(x),$$ kde $b(x)$
je funkce a $L$ operátor. Například pro $b(x)=0$ a $L[y]=y'-y$ má
rovnice tvar
$$y'-y=0,$$
tj.
$$y'=y.$$


<div>
> **Důsledek linearity.** Jsou-li funkce $y_1(x)$ a $y_2(x)$ po řadě řešeními rovnic $$L[y]=b_1(x),\quad L[y]=b_2(x),$$
> Je funkce $$y(x)=C_1 y_1(x)+C_2 y_2(x)$$ řešením rovnice $$L[y]=C_1 b_1(x)+C_2 b_2(x).$$
</div>

Například pro $L[y]=y''-y$ a $b_1(x)=b_2(x)=0$ všechny tři výše uvedené rovnice splynou v $$y''-y=0.$$ Protože $y_1(x)=e^x$ je řešením této rovnice a $y_2(x)=e^{-x}$ je také řešením této rovnice, je řešením této rovnice i každá funkce tvaru
$$y(x)=C_1 e^x+C_2 e^{-x},$$
kde $C_{1,2}\in\mathbb{R}.$


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

<!--

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

Vskutku. Platí

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



-->

# Obecné řešení homogenní LDE

Uvažujme homogenní LDE
$$y'+a(x)y=0. \tag{HLDE}$$

* Přepsáním do 
$$y'=-a(x)y$$
vidíme, že jedno řešení je možno uhodnout. Je to řešení
$$y_{p0}=e^{-\int a(x)\mathrm{d}x}.$$
* Další řešení dostaneme z linearity. Funkce 
$$y(x)=Cy_{p0}(x)$$
je řešením  rovnice (HLDE) pro libovolné $C$.
* Pro počáteční podmínku $y(x_0)=y_0$ stačí najít $C$ takové, aby platilo
$$y_0=C y_{p0}(x_0)$$ a tuto rovnici je možno vyřešit vzhledem k $C$ vždy, protože $y_{p0}(x_0)\neq 0$.

**Závěr:** Obecné řešení rovnice (HLDE) je 
$$y(x)=C e^{-\int a(x)\mathrm{d}x}.$$


# Obecné řešení nehomogenní LDE pomocí partikulárního řešení

Je-li $y_p$ řešením nehomogenní LDE
$$y'+a(x)y=b(x),$$ je obecným řešením této rovnice
$$y(x)=Cy_{p0}(x)+y_p(x),$$
kde $Cy_{p0}(x)$ je obecným řešením asociované homogenní LDE.

**Závěr:** Stačí mít jedno řešení nehomogenní rovnice a jedno nenulové
  řešení asociované homogenní rovnice. Protože množina všech řešení má
  pevnou strukturu, dokážeme z těchto informací napsat libovolné
  řešení.


* Vskutku, jestliže $L[y_p]=b(x)$ a $L[y_{p0}(x)]=0$, potom 
  $$L[y]=L[Cy_{p0}+y_p]=CL[y_{p0}]+L[y_p]=C\cdot 0+b(x)=b(x).$$
  Funkce $y(x)$ tedy je řešením.
* Pokud potřebujeme splnit libovolnou počáteční podmínku $y(x_0)=y_0$,
  kde $x_0,y_0\in\mathbb{R}$, stačí vzít řešení
  $$y(x)=\frac{y_0-y_{p}(x_0)}{y_{p0}(x_0)}y_{p0}(x)+y_p(x),$$



# Obecné řešení nehomogenní LDE ještě jednou a prakticky

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

<!--

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


-->


# Nehomogenní LDE – metoda integračního faktoru

Zůstává otázka, jak najít partikulární řešení nehomogenní rovnice.

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

Pozn: Partikulární řešení nehomogenní rovnice je $$y_p(x)=e^{-\int a(x)\mathrm{d}x}\int b(x)e^{\int a(x)\mathrm{d}x}\mathrm{d}x.$$

# Lineární diferenciální rovnice druhého řádu

<def>

> **Definice.** Buďte $p$, $q$ a $f$
> funkce definované a spojité na intervalu $I$. Diferenciální rovnice
> $$
>     y''+p(x)y'+q(x)y=f(x) \tag{LDE}\label{LDE}$$
> se nazývá *lineární diferenciální rovnice druhého řádu*. *Řešením
> rovnice* (nebo též *integrálem rovnice*) na intervalu $I$ rozumíme
> funkci, která má spojité derivace do řádu $2$ na
> intervalu $I$ a po dosazení identicky splňuje rovnost (LDE) na $I$.
> Úloha nalézt řešení rovnice, které splňuje v\ bodě $x_0\in I$ *počáteční
> podmínky*
> $$\tag{IC}
>     \begin{cases}
>       y(x_0)=y_0,\\y'(x_0)=y'_0,
>     \end{cases}$$
> kde $y_0$ a $y'_0$ jsou reálná čísla, se nazývá *počáteční úloha*
> (*Cauchyova úloha*). Řešení počáteční úlohy se nazývá *partikulární
> řešení rovnice.*

</def>

**Zkratky:** LDE - lineární diferenciální rovnice, IC - počáteční podmínka, IVP - počáteční úloha 

# Příklad - těleso na pružině

\iffalse 

<div class='obtekat'>

![Těleso na pružině je nejjednodušší model pro rovnice druhého řádu. Přesto není vhodné tento model podceňovat, dokáže být velmi užitečný i u jiných úloh, které se týkají oscilací. Chemické oscilace, považované za základ tzv. buněčných hodin i jiných vnitřních cyklů biologických organismů, jsou ale založeny na jiném popisu. (Viz Brusselator.) Zdroj: pixabay.com](pruzina.jpg)

</div>

\fi

Kmity tělesa o\ hmotnosti $m$ pružně připevněného k\ nehybné podložce
spojem tuhosti $k$ jsou popsány diferenciální rovnicí ${\ddot x+\frac
km x=0}.$ Zde navíc používáme fyzikální úzus označovat derivace podle
času pomocí tečky a ne čárky. Symbol $\ddot x$ tedy značí druhou
derivaci funkce $x$, kde $x$ bereme jako funkci času.

Jednoduchým mechanickým modelem je těleso na pružině. Zde je deformace
úměrná působící síle. Analogické situace vedoucí na stejnou rovnici
však dostáváme i obecněji. Pokud pro jednoduchost předpokládáme, že
těleso s jedním stupněm volnosti se nachází ve stabilním stavu s
minimem potenciální energie a energie závisí na poloze $x$, můžeme v
okolí minima $x_0$ potenciální energii aproximovat Taylorovým rozvojem
druhého řádu $$E(x)\approx E(x_0)+E'(x_0)x+\frac 12E''(x_0)x^2.$$
Vzhledem k tomu, že v $x_0$ je minimum, platí $E'(x_0)=0$. Síla je
poté dána vztahem $$F(x)=-\frac{\partial}{\partial x}E(x)=-E''(0)x.$$
Síla $F$ je tedy úměrná výchylce $x$ a vrací těleso do rovnovážné
polohy. Situace tedy perfektně koresponduje s kmitáním na pružině i
když potenciální energie uvažovaná v tomto odstavci může být jiného
charakteru.

# Řešitelnost LDE druhého řádu

<div class=sloupce>

$$y''+p(x)y'+q(x)y=f(x) \tag{LDE}$$

> **Věta o existenci a jednoznačnosti řešení LDE druhého řádu.** Každá
> počáteční úloha pro LDE druhého řádu má řešení, které je určeno
> jednoznačně a toto řešení je definované na celém intervalu $I$.

<def>

> **Definice (speciální typy LDE druhého řádu).** Platí-li v\ rovnici (LDE) $f(x)=0$
> pro všechna $x\in I$, nazývá se rovnice (LDE) *homogenní*, v\ opačném
> případě *nehomogenní*. 
> 
> Jsou-li koeficienty $p(x)$ a $q(x)$ na intervalu
> $I$ konstantní funkce, nazývá se (LDE) *rovnice s\ konstantními
> koeficienty*.

</def>

<def>

> **Definice (triviální řešení).** Funkce $y(x)\equiv 0$ je řešením
> homogenní LDE druhého řádu vždy, bez ohledu na tvar koeficientů $p$,
> $q$. Toto řešení nazýváme *triviální řešení
> rovnice LDE*.

</def>

<def>

> **Definice (asociovaná homogenní rovnice).** Nahradíme-li v\ nehomogenní LDE
> pravou stranu (tj. funkci $f$) nulovou funkcí obdržíme rovnici
> $$ y''+p(x)y'+q(x)y=0.$$
> Tato rovnice se nazývá *asociovaná homogenní rovnice k\ rovnici (LDE)*.

</def>

<def>

> **Definice (obecné řešení).** Všechna řešení LDE druhého řádu 
> lze vyjádřit ve tvaru obsahujícím dvě nezávislé konstanty $C_1$,
> $C_2\in\mathbb{R}$. Takovýto předpis se nazývá *obecné řešení rovnice (LDE)*.

</def>


</div>


<!--
# Operátorová symbolika

$$y''+p(x)y'+q(x)y=f(x) \tag{LDE}$$

<div class="sloupce__">

<div>

Podobně jako lineární diferenciální rovnice
prvního řádu, i\ u (LDE) často pravou stranu rovnice často zkracujeme do
tvaru $L[y](x)$. Definujeme-li tedy
$$  L[y](x)=y''(x)+p(x)y'(x)+q(x)y(x),$$
je tímto předpisem definován operátor, který každé dvakrát
diferencovatelné funkci přiřazuje levou stranu rovnice (LDE). Rovnici
(LDE) je potom možno zapsat ve tvaru $$L[y]=f(x).$$

</div>

> **Věta o linearitě.** Operátor $L[y]$ zachovává lineární kombinaci funkcí,
> tj. pro libovolné dvě funkce $y_1$ a $y_2$ a libovolné reálné
> konstanty $C_1$ a $C_2$ platí
> $$L[C_1y_1+C_2y_2]=C_1L[y_1]+C_2L[y_2].$$

</div>

-->

# Důsledky linearity

Jako speciální případ vztahu  $$L[C_1y_1+C_2y_2]=C_1L[y_1]+C_2L[y_2]$$ dostáváme následující. 


* Platí $$L[y_1]=L[y_2]=0\ \implies \ L[C_1y_1+C_2y_2]=0,$$ tj. každá
  lineární kombinace dvou řešení homogenní LDE je opět řešením této
  rovnice. Pokud se nám navíc podaří volbou konstant $C_1$ a $C_2$
  splnit libovolnou počáteční podmínku, je jistota, že máme obecné
  řešení.
* Platí $$L[y_2]=0 \text{ a } L[y_1]=f(x)\ \implies\
    L[y_1+y_2]=f(x),$$ tj. součet řešení nehomogenní a asociované
    homogenní LDE je řešením původní nehomogenní rovnice. Pokud je
    navíc $y_2$ obecným řešením homogenní rovnice, je $y_1+y_2$
    obecným řešením nehomogenní rovnice, protože se podaří splnit
    libovolnou počáteční podmínku.

# Důsledky linearity prakticky

Vztah
$$L[C_1y_1+C_2y_2]=C_1L[y_1]+C_2L[y_2]$$
poslouží (podobně jako u lineárních rovnic prvního řádu), abychom popsali strukturu množiny všech řešení rovnice a dokázali tuto množinu vytvořit jenom na základě znalosti několika prvků.

Rovnice $$y''+y=x\tag{A}$$ má partikulární řešení $y=x$. 

Asociovaná homogenní rovnice je $$y''+y=0.\tag{B}$$ Tato rovnice má řešení
například $y=\sin x$, $y=\cos x$. Z linearity plyne

* Funkce $y=C_1 \sin x+C_2 \cos x$ je řešením rovnice (B) pro
  libovolná reálná $C_1$, $C_2$. Protože platí $y(0)=C_2$ a
  $y'(0)=C_1$, je možné splnit libovolnou podmínku $y(0)=\alpha$,
  $y'(0)=\beta$ volbou $C_2=\alpha$ a $C_1=\beta$. Jedná se tedy o
  obecné řešení.

* Funkce $y=C_1 \sin x+C_2\cos x +x$ je obecným řešením rovnice (A). 



# Kdy pomocí linearity získáme obecné řešení?


\iffalse 

<div class='obtekat'>

![Dvě funkce mohou stačit na založení celého rodu všech řešení. Jako kdysi Adam a Eva? Zdroj: pixabay.com](adam_eva.jpg)

</div>

\fi

Budeme studovat homogenní LDE druhého řádu, tj.
rovnici 
$$y''+p(x)y'+q(x)y=0,$$
kterou můžeme zkráceně zapsat jako $L[y]=0$, kde operátor $L$ je
lineární diferenciální operátor druhého řádu.

**Motivace.** Budeme předpokládat že funkce $y_1(x)$ a $y_2(x)$ jsou obě
řešeními a budeme hledat podmínky, za kterých je funkce

$$y(x)=C_1y_1(x)+C_2y_2(x)$$

obecným řešením. Derivováním tohoto vztahu získáváme

$$y'(x)=C_1y'_1(x)+C_2y'_2(x)$$

a dosazení počátečních podmínek $y(\alpha)=\beta$, $y'(\alpha)=\gamma$
vede k\ následující soustavě lineárních rovnic s\ neznámými $C_1$, $C_2$

$$
\begin{aligned}
  \beta&{}=C_1y_1(\alpha)+C_2y_2(\alpha),\\
  \gamma&{}=C_1y'_1(\alpha)+C_2y'_2(\alpha).
\end{aligned}$$

Jak je známo z\ lineární algebry, tato soustava má právě jedno řešení pro
libovolnou volbu čísel $\beta$, $\gamma$ právě tehdy, když matice
soustavy, tj. matice $\begin{pmatrix}
  y_1(\alpha)&y_2(\alpha)\\
  y_1'(\alpha)&y_2'(\alpha)
\end{pmatrix},$ je regulární. Tato matice je regulární právě tehdy, když její
determinant je nenulový a to nastane právě tehdy když jeden sloupec není
násobkem druhého. 


# Homogenní LDE 2. řádu (wronskián, lineárně nezávislá řešení)

$$y''+p(x)y'+q(x)y=f(x) \tag{LDE0}$$

<def>

> **Definice (lineární (ne-)závislost funkcí).** Buďte $y_1$ a $y_2$ funkce definované
> na intervalu $I$. Řekneme, že funkce $y_1$ a $y_2$ jsou na intervalu $I$
> *lineárně závislé*, jestliže jedna z\ nich je na intervalu $I$ násobkem
> druhé, tj. jestliže existuje reálné číslo $k\in\mathbb{R}$ s\ vlastností
> $$y_1(x)=ky_2(x) \qquad\text{pro všechna $x\in I$},$$
> nebo
> $$y_2(x)=ky_1(x) \qquad\text{pro všechna $x\in I$}.$$
> V\ opačném případě říkáme, že funkce $y_1$, $y_2$ jsou na intervalu $I$
> *lineárně nezávislé*.

</def>

<def>

> **Definice (Wronskián).** Buďte $y_1(x)$ a $y_2(x)$ dvě libovolná
> řešení homogenní rovnice (LDE0). *Wronskiánem* funkcí $y_1(x)$,
> $y_2(x)$ rozumíme determinant
> $$
>     W[y_1, y_2](x)=
>     \begin{vmatrix}
>       y_1(x)&y_2(x)\\y_1'(x)&y_2'(x)
>     \end{vmatrix}.
>  $$

</def>

> **Věta o lineární (ne)závislostí řešení.** Buďte $y_1(x)$ a $y_2(x)$ dvě řešení rovnice
> (LDE0) na intervalu $I$. Tato řešení jsou lineárně nezávislá právě
> tehdy když je jejich Wronskián různý od nuly na intervalu $I$.


# Homogenní LDE 2. řádu (obecné řešení)

$$y''+p(x)y'+q(x)y=f(x) \tag{LDE0}$$

> **Věta (obecné řešení homogenní LDE)** Jsou-li $y_1$ a $y_2$ dvě
> netriviální lineárně nezávislá řešení rovnice (LDE0) na intervalu
> $I$, pak funkce $y$ definovaná vztahem
> $$    y(x, C_1, C_2)=C_1y_1(x)+C_2y_2(x),$$
> kde $C_{1,2}\in\mathbb{R}$, je obecným řešením rovnice (LDE0) na intervalu
> $I$.

<def>

> **Definice (fundamentální systém řešení).** Dvojici funkcí $y_1$ a $y_2$ z\ předchozí
> věty nazýváme *fundamentální systém řešení rovnice (LDE0)*.

</def>

# Homogenní LDE 2. řádu s\ konstantními koeficienty


Budeme studovat rovnici tvaru
$$y''+py'+qy=0,$$
kde $p,q\in \mathbb{R}$. Všimněme si nejprve následujícího faktu: Dosadíme-li do
levé strany rovnice $y=e^{zx}$, kde $z$ je reálné číslo, po výpočtu
derivací a po vytknutí faktoru $e^{zx}$ získáváme
$$y''+py'+qy=e^{zx}(z^2+pz+q).$$
Protože exponenciální faktor na pravé straně je vždy nenulový, bude
výraz na pravé straně roven nule pokud bude splněna podmínka
$$z^2+pz+q=0.$$
Pouze v\ tomto případě bude uvažovaná funkce řešením rovnice (1).


<def>

> **Definice (charakteristická rovnice).** Kvadratická rovnice
> $$z^2+pz+q=0$$ s\ neznámou $z$ se nazývá *charakteristická rovnice*
> pro rovnici $$y''+py'+qy=0.$$

</def>

# Homogenní LDE 2. řádu s\ konstantními koeficienty

> **Věta o obecném řešení LDE s\ konstantními koeficienty.**
>  Uvažujme LDE $$y''+py'+qy=0,\tag{1}$$ a její charakteristickou rovnici
>  $$z^2+pz+q=0.$$
> 
> -   Jsou-li $z_1,z_2\in\mathbb{R}$ dva různé reálné kořeny charakteristické
>     rovnice, definujme $${y_1=e^{z_1 x}}, \qquad{y_2=e^{z_2 x}}.$$
> 
> -   Je-li $z_1\in\mathbb{R}$ dvojnásobným kořenem charakteristické
>     rovnice, definujme $${y_1=e^{z_1 x}}, \qquad{y_2=xe^{z_1 x}}.$$
> 
> -   Jsou-li $z_{1,2}=\alpha\pm i\beta\not\in\mathbb{R}$ dva komplexně sdružené
>     kořeny charakteristické rovnice, definujme $${y_1(x)=e^{\alpha x}\cos(\beta x)}, \qquad
>     {y_2(x)=e^{\alpha x}\sin(\beta x)}.$$
> 
> Potom obecné řešení rovnice (1) je
> $$y(x,C_1,C_2)=C_1y_1(x)+C_2y_2(x),\qquad C_1\in\mathbb{R},\ C_2\in\mathbb{R}.$$


# Nehomogenní LDE 2. řádu


> **Věta o obecném řešní nehomogenní LDE.** Součet libovolného partikulárního řešení
> nehomogenní lineární diferenciální rovnice a obecného řešení asociované
> homogenní rovnice je obecným řešením původní nehomogenní rovnice


Následující věta udává jednu z\ metod nalezení partikulárního řešení,
pokud je diferenciální rovnice do jisté míry speciální: má konstantní
koeficienty a polynomiální pravou stranu.

> **Věta (metoda neurčitých koeficientů).** Uvažujme lineární diferenciální rovnici
> druhého řádu
> $$y''+py'+qy=P_n(x),$$
> kde $p\in\mathbb{R}$ je konstanta, $q\in\mathbb{R}\setminus\{0\}$ je nenulová konstanta
> a $P_n(x)$ je polynom stupně $n$. Existuje polynom stupně $n$, který je
> partikulárním řešením této diferenciální rovnice.

V\ praxi polynom který má být řešením napíšeme s\ neurčitými koeficienty a
dosazením do rovnice určíme potřebné hodnoty těchto koeficientů.


# Dirichletova okrajová úloha, vlastní čísla

Někdy je nutné řešit diferenciální rovnice druhého řádu s jinými než
počátečními podmínkami. Ukážeme si na jednoduchém příkladě odlišnost
od počáteční úlohy. Následující úloha má velké uplatnění při studiu
kmitavých pohybů.


Pro parametr $\lambda\in\mathbb{R}$ najděte řešení rovnice 
$$y''+\lambda y=0 \tag{*}$$
splňující podmínky
$$y(0)=0=y(1). \tag{**}$$

<def>

> **Definice (okrajová úloha).** Úloha najít řešení diferenciální
> rovnice (\*), které splňuje podmínky (\*\*) se nazývá (Dirichletova)
> *okrajová úloha*.

</def>

Odlišnost Dirichletovy úlohy od (Cauchyovy) počáteční úlohy je v tom,
že nezadáváme funkční hodnotu a derivaci v jednom bodě, ale funkční
hodnotu ve dvou různých bodech.


Jedno z\ řešení Dirichletovy úlohy je triviální řešení
$y(x)=0$. Ukazuje se, že netriviální řešení existuje jen pro některé
hodnoty parametru $\lambda$.  

<def>

> **Definice (vlastní funkce, vlastní hodnota).** Hodnota $\lambda$,
> pro kterou existuje netriviální řešení Dirichletovy okrajové úlohy
> se nazývá *vlastní hodnota okrajové úlohy* a příslušné řešení se
> nazývá *vlastní funkce okrajové úlohy*.

</def>

# Výpočet vlastních hodnot


Je-li $\lambda>0$, je řešením rovnice $$y''+\lambda y=0 \tag{*}$$
funkce
$$y(x)=C_1\sin(\sqrt \lambda x)+C_2\cos(\sqrt \lambda x).$$
Z\ podmínky $y(0)=0$ dostáváme $C_2=0$. Tedy
$$y(x)=C_1\sin(\sqrt\lambda x).$$

Z\ podmínky $y(1)=0$ dostáváme 
$$0=C_1\sin(\sqrt\lambda),$$
která je splněna pokud $C_1=0$, nebo $\sqrt\lambda=k\pi$, $k\in\mathbb{Z}$


Okrajová úloha $$y''+\lambda y=0, \quad y(0)=0=y(1)$$ má vlastní hodnoty 
$\lambda=(k\pi)^2$, $k\in\mathbb{Z}$


# Kmity struny

<div class='obtekat'>

![Kmitání jednorozměrných objektů je popsáno lineární diferenciální rovnicí druhého řádu. Zdroj: pixabay.com](housle.jpg)

</div>


Při kmitání struny délky $l$ upevněné na koncích se ukazuje, že proces
je možno modelovat okrajovou úlohou $$y''+\lambda^2 y=0,\quad
y(0)=0=y(l),$$
kde $y$ je amplituda kmitů v místě $x$ a $\lambda$ souvisí s frekvencí. (Jaká tato souvislost je a jak se v rovnici objeví uvidíme později při
řešení vlnové rovnice.) Rovnice má obecné řešení $$y(x)=C_1\sin(
\lambda x)+C_2\cos( \lambda x)$$ Z\ podmínky $y(0)=0$ dostáváme $C_2=0$ a z
podmínky $y(l)=0$ dostáváme $$y(x)=C_1\sin(\lambda x)$$ pokud
$$\lambda l=k\pi \tag{***}$$ a $y=0$ jinak. Při podrobnějším popisu
(jedna ze závěrečných přednášek semestru) se ukazuje, že $\lambda$
souvisí s hmotností struny, napětím ve struně a frekvencí, kterou
slyšíme. Podmínka (\*\*\*) určuje spektrum slyšitelných frekvencí, na
kterých může struna kmitat, výsledný pohyb (a zvuk) je díky linearitě složením
jednotlivých variant. Toho se dá s výhodou vyžívat a stejnou strunu je možné [rozeznívat více způsoby](https://www.youtube.com/watch?v=kn92TLYA4rE) a dosahovat různý výsledný zvuk. 

# Vzpěry

<div class='obtekat'>

![Nosníky, ať už samostatné vzpěry, nebo součásti příhradových konstrukcí, je nutné posuzovat i z hlediska axiálního namáhání. Ignorování tohoto způsobu namáhání vedlo v 19. století k pádu několika příhradových železničních mostů a následnému stržení řady [chybně dimenzovaných mostů](https://en.wikipedia.org/wiki/Cast-iron_architecture#Catastrophic_failures). Zdroj: pixabay.com](vzpera.jpg)

</div>

Předpokládejme, že máme nosník namáhaný na vzpěr. (U příhradových
konstrukcí může být dokonce kombinované namáhání, částečně na vzpěr,
tj. v osem a částečně kolmo na osu.) Osu $x$ zvolíme podélně v ose
vzpěry, osu $y$ kolmo. Při namáhání takového nosníku, který je pevně uchycen na dolním a horním konci, je výchylka dána okrajovou úlohou
([Podžgaj a kol., Štruktúra a vlastnosti dreva](https://katalog.mendelu.cz/documents/21654), str. 359)
$$\frac{\mathrm d^2 y}{\mathrm dx^2}+\alpha^2 y=0,\quad y(0)=y(l)=0,$$
kde $\alpha^2=\frac{F}{EI}$ je parametr závislý na působící síle,
materálu a momentu setrvačnosti průřezu nosníku. (Pro jiné způsoby uchycení se rovnice a okrajové podmínky mohou mírně lišit, rovnice může být například i nehomogenní, zásadní vlastnosti jsou však stejné.) Toto je stejná úloha jako u kmitání struny. Při síle, která se postupně zvětšuje, se nenulové řešení objeví v bodě, kde platí $$\alpha l=\pi,$$ (odpovídá základní frekvenci struny) tj.
$$\sqrt{\frac {F}{EI}}l=\pi$$
a
$$F=\frac{\pi^2 EI}{l^2}.$$
Toto je pro daný nosník kritická síla a ta je pro daný materiál nepřímo úměrná druhé mocnině délky a přímo úměrná tuhosti kvadratickému momentu $I$.



# Neumannova a smíšená okrajová úloha


\iffalse

<div class='obtekat'>


![Array mbira - [hudební nástroj](https://www.youtube.com/watch?v=5fAAGheYTFA) se smíšenou okrajovou úlohou](array_mbira.jpg) 

</div>

\fi



Při řešení Dirichletovy úlohy hledáme řešení diferenciální rovnice
druhého řádu s předepsanými hodnotami ve dvou různých bodech
$$y(a)=\alpha,\quad y(b)=\beta.$$
Tento požadavek se uplatní při studiu kmitů struny nebo tyče s pevnými
konci.

V praxi je možné si představit i jiné podmínky. Například v
termodynamice se používají podmínky na hodnotu derivací ve dvou
různých bodech $$y'(a)=\alpha, \quad y'(b)=\beta.$$ Takové podmínky se
nazývají Neumannovy podmínky a úloha najít řešení rovnice, které tyto
podmínky splňuje se nazývá **Neummannova okrajová úloha**, též
**Neumannova úloha**.


Existují i smíšené úlohy, například při kmitání tělesa s\ jedním
upevněným a jedním volným koncem je přirozené formulovat **smíšenou
okrajovou podmínku** $$y(a)=0,\quad y'(b)=0,$$ kde $a$ je upevněný konec a
$b$ volný konec.


