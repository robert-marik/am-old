% Lineární operátory a lineární diferenciální rovnice
% Robert Mařík
% 2014–2020

# Lineární operátor


**Operátorem** rozumíme zobrazení, které má na vstupu i na výstupu
funkci. Například pro funkce jedné proměnné mohou být operátory
derivace, druhá derivace, vynásobení funkce funkcí $\ln x$ anebo vnoření zadané funkce do funkce $\ln x$. Tj. pro $y=y(x)$ můžeme uvažovat operátory
$F_1[y]=\frac{\mathrm dy}{\mathrm dx}$, $F_2[y]=\frac{d^2y}{dx^2}$, $F_3[y](x)=y(x)\ln(x)$, $F_4[y](x)=\ln(y(x)).$

\iffalse 

<div class='obtekat'>

![Lineární zobrazení zachovávají některé vlastnosti. V geometrii například rovnoběžnost, v matematické analýze zachovávají lineární zobrazení lineární kombinaci. Rovnice s lineárním operátorem jsou díky tomu velmi předvídatelné. Proto je (lineární operátory i rovnice) v matematice máme tak rádi. Zdroj: pixabay.com](rails.jpg)

</div>

\fi

**Lineárním operátorem** rozumíme zobrazení, které zachovává součet
funkcí a násobek konstantou, tj. platí $$L[y_1+y_2]=L[y_1]+L[y_2]$$ a
$$L[C y_1]=C L[y_1]$$ pro libovolné reálné číslo $C$ a libovolné
funkce $y_1$ a $y_2$ z definičního oboru operátoru $L$.

# Příklady lineárních operátorů

Linearitu se naučíme využívat k tomu, abychom úlohu najít řešení
rovnice rozkouskovali na řešení jednodušších úloh. Například je možné
zkombinovat úlohu na stacionární proudění podzemní vody a úlohu na radiální proudění ke studni. Každou z těchto úloh umíme redukovat na separovatelnou diferenciální rovnici a vyřešit. Zkombinováním těchto úloh je možné modelovat chování studny v rovinném toku. Používá se například k zachycení kontaminace spodní vody.

\iffalse 

<div class='obtekat'>

![Rovinný tok podzemní vody se studnou. Podle šipek je možno určit oblast zachytáváni. Řeší se samostatně rovinný tok (kartézské souřadnice) a tok ke studni (polární souřadnice) a obě úlohy se zkombinují pomocí linearity.](snizeni_toku_se_studnou_03_001.png)

</div>

\fi


* Operátor derivace, tj. operátor definovaný vztahem $L[y]=\frac{\mathrm dy}{\mathrm dx}$ je lineární. Toto plyne ze vzorců pro derivaci součtu a konstantního násobku.
* Buď dána funkce $a(x)$. Operátor násobení funkcí $a(x)$, tj. $L[y](x)=a(x)y(x)$ je lineární. To plyne z komutativity násobení a z distributivního zákona (roznásobování závorek).
* Složení (postupná aplikace) lineárních operátorů je lineární operátor. Například tedy
$$\frac{\mathrm d^2 y}{\mathrm dx^2}$$ je lineární operátor.
* Součet lineárních operátorů je lineární operátor. 
* Buď pevně dána funkce $a(x)$. Lineární operátor
$$L[y]=\frac{\mathrm dy}{\mathrm dx}+a(x)y$$
se nazývá *lineární diferenciální operátor prvního řádu*.
* Buďte pevně dány funkce $p(x)$ a $q(x)$. Lineární operátor
$$L[y]=\frac{\mathrm d^2y}{\mathrm dx^2}+p(x)\frac{\mathrm dy}{\mathrm dx}+q(x)y$$
se nazývá *lineární diferenciální operátor druhého řádu*.
* Buď dána $n\times n$ matice reálných čísel $A$ a $n$-vektorová funkce $\vec F(x)$. Zobrazení, které funkci $\vec F(x)$ přiřadí součin $A\vec F(x)$ je lineární. To plyne z distributivnosti násobení vzhledem ke sčítání matic a z toho, že součin matice a reálného čísla komutuje.
* Operátor z levé strany difuzní rovnice
$$
      {\frac{\partial u}{\partial t}-\nabla\cdot \bigl(D\nabla u\bigr)=\sigma, }$$
      tj. operátor $$L[u]=\frac{\partial u}{\partial t}-\nabla\cdot \bigl(D\nabla u\bigr)$$ je lineární. Po rozepsání divergence a gradientu pomocí parciálních derivací (které jsou lineární) jenom kombinujeme lineární operátory a tedy zachováváme linearitu.
* Rovnice podzemní vody pro proudění s napjatou hladinou
$$ {S_S\frac{\partial h}{\partial t} - \nabla\cdot \bigl(T\nabla h\bigr)=  \sigma }$$
je speciálním případem difuzní rovnice a operátor definovaný levou stranou je lineární. Rovnice podzemní vody pro proudění s volnou hladinou
$$ {S_S\frac{\partial h}{\partial t} - \nabla\cdot \bigl(kh\nabla h\bigr)=  \sigma }$$
      definuje operátor
      $$F[h]={S_S\frac{\partial h}{\partial t} - \nabla\cdot \bigl(kh\nabla h\bigr)}$$
      a není lineární. Pokud však využijeme rovnost
      $$h\frac{\partial h}{\partial x}=\frac 12 \frac{\partial h^2}{\partial x}$$ a analogickou rovnost i pro další parciální derivace, je ve stacionárním případě (derivace podle času je nulová) rovnici možno přepsat do tvaru 
$$ - \frac 12 \nabla\cdot \bigl(k\nabla (h^2)\bigr)= \sigma $$
a levá strana definuje lineární operátor v proměnné $h^2$.




# Princip superpozice

> Věta (princip superpozice). Každý lineární operátor zachovává lineární kombinaci funkcí, tj. platí
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

# Operátorové rovnice s lineárním operátorem

Operátorovou rovnicí budeme rozumět rovnici $$L[y]=b(x),$$ kde $b(x)$
je funkce a $L$ operátor. Například pro $b(x)=0$ a $L[y]=y'-y$ má
rovnice tvar
$$y'-y=0,$$
tj.
$$y'=y.$$

Operátorovými rovnicemi (na množině konstantních vektorových funkcí) jsou i soustavy lineárních rovnic $$AX=B.$$ Pokud pracujeme s nekonstantními vektorovými funkcemi tak, že při derivaci derivujeme každou komponentu samostatně, je rovnice 
$$\frac{\mathrm dX}{\mathrm dt}-AX= B$$ operátorová rovnice s lineárním operátorem. Tyto rovnicím se v případě, kdy matice $A$ a $B$ nezávisí na čase, nazývají autonomní systémy a budeme se jim věnovat v příští přednášce.

Následující věta vlastně vyjadřuje totéž co princip superpozice z minulého slidu, pouze v jiných pojmech: v pojmech řešení rovnice s lineárním operátorem. 

> Věta (princip superpozice při řešení rovnic). Jsou-li funkce $y_1(x)$ a $y_2(x)$ po řadě řešeními rovnic $$L[y]=b_1(x),\quad L[y]=b_2(x),$$
> Je funkce $$y(x)=C_1 y_1(x)+C_2 y_2(x)$$ řešením rovnice $$L[y]=C_1 b_1(x)+C_2 b_2(x).$$


Pro $b_1(x)=b_2(x)=0$ všechny tři výše uvedené rovnice splynou a lineární kombinace dvou řešení homogenní lineární rovnice je také řešením. Toto je možné pochopitelně rozšířit na libovolný konečný počet funkcí. 

Pro $b_1(x)=0$ a $C_2=1$ jsou obě nehomogenní rovnice stejné a pokud k řešení rovnie přičteme řešení asociované homogenní rovnice (se stejným operátorem na levé straně, ale nulou na pravé straně), dostaneme řešení stejné rovnice.

Z těchto jednoduchých tvrzení plyne několik zásadních pozorování.

* Pokud máme k dispozici několik řešení homogenní rovnice, libovolná jejich lineární kombinace je také řešením. 
* Za určitých okolností lineární kombinace z předchozího bodu umožní splnit libovolnou počáteční podmínku a vzhledem k jednoznačnosti řešení, která lineární rovnice zpravidla provází, je jistota, že žádné další řešení neexistuje. Nalezení těchto funkcí je tedy zásadní krok při řešení rovnice. 
* U nehomogenní rovnice stačí najít jedno řešení. Obecné řešení (zahrnující všechna řešení) potom dostaneme tak, že k tomuto řešení přičteme obecné řešení homogenní rovnice, která má stejný lineární operátor, ale pravá strana je nahrazena nulou. Že dostaneme řešení stejné nehomogenní rovnice zajišťuje linearita, že žádné další řešení neexistuje zajišťuje jednoznačnost řešení.


# Příklady využití linearity 

Pro konkrétnost specifikujeme myšlenky z předchozího slidu na příkladech.

* V další části této přednášky se seznámíme se skalárními lineárními diferenciálními rovnicemi
  prvního řádu. Pro jednu funkci lineární kombinace degenerují na
  násobky. Proto je obecné řešení rovnice součtem jednoho řešení
  rovnice a obecného řešení asociované homogenní rovnice. Toto řešení
  asociované homogenní rovnice je násobkem jednoho nenulového řešení. Například  funkce $y=e^x$ splňuje rovnici $$y'-y=0$$ a funkce $y=-\pi$ splňuje rovnici $$y'-y=\pi.$$ Všechna řešení této rovnice jsou tvaru $y=Ce^x-\pi$
* Pro skalární lineární diferenciální rovnice druhého řádu je situace
  obdobná, pouze pro řešení asociované homogenní diferenciální rovnice
  potřebujeme dvě lineárně nezávislé řešení (jedno není násobkem
  druhého).   
Například  $y_1(x)=e^x$ a $y_2(x)=e^{-x}$ nejsou jedna násobkem druhé a obě splňují rovnici $$y''-y=0.$$ Proto všechna řešení jsou tvaru 
$$y(x)=C_1 e^x+C_2 e^{-x},$$
kde $C_{1,2}\in\mathbb{R}.$ Funkce $y=-x$ splňuje rovnici $$y''-y=x$$ a všechna řešení této rovnice jsou $$y(x)=C_1 e^x+C_2 e^{-x}-x.$$
* Pro vektorové diferenciální rovnice prvního řádu $$\frac{\mathrm dX}{\mathrm dt}-AX= B$$  je souvislost mezi
  homogenní a nehomogenní rovnicí obdobná jako v minulých
  případech. Pouze pro řešení homogenní rovnice ($B=0$) potřebujeme tolik
  nezávislých řešení, kolik je dimenze vektoru. (Lineární závislost a
  nezávislost je definována stejně jako u algebraických vektorů.) Z
  nich lineárními kombinacemi dostaneme řešení libovolné počáteční podmínky a proto jsou v obecné lineární kombinaci zahrnuta všechna řešení. Pro nalezení obecného řešení nehomogenní úlohy stačí najít jedno řešení a všechna další řešení dostaneme sečtením s obecným řešením homogenní rovnice se stejnou levou stranou. Úloha už je složitější na provedení, ale můžeme pracovat kvalitativně. Pokud například máme tolik nezávislých řešení, kolik je dimenze úlohy, a všechna řešení konvergují k nule, potom i všechny jejich lineární kombinace konvergují k nule. Všechna řešení rovnice v takovém případě konvergují k nule. Řešení nehomogenní rovnice by byla součtem jednoho pevného řešení a řešení jdoucích k nule. Všechny by tady konvergovaly ke stejnému řešení nehomogenní úlohy. To odpovídá systému, který po čase přejde do rovnovážného stavu.

# Lineární diferenciální rovnice prvního řádu

> Definice (Lineární diferenciální rovnice prvního řádu). Nechť funkce $a$, $b$ jsou spojité na intervalu $I$.
> Rovnice
> $$  y'+a(x)y=b(x) \tag{LDE}$$
> se nazývá *obyčejná lineární diferenciální rovnice prvního řádu*
> (zkráceně píšeme LDE). Je-li navíc $b(x)\equiv 0$ na $I$, nazývá se
> rovnice *homogenní*, v opačném případě *nehomogenní*.

> Věta (o řešitelnosti LDE prvního řádu). Jsou-li funkce $a$, $b$ spojité na
> intervalu $I$, $x_0\in I$ a $y_0\in\mathbb{R}$ libovolné, má každá počáteční
> úloha právě jedno řešení definované na celém
> intervalu $I$.

> Definice (asociovaná homogenní rovnice). Buď dána lineární diferenciální rovnice. Homogenní rovnice, která
> vznikne z\ rovnice nahrazením pravé strany nulovou funkcí, tj.
> rovnice
> $$    y'+a(x)y=0$$
> se nazývá *homogenní rovnice, asociovaná s nehomogenní rovnicí (LDE)*

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
  \dm$$L[y]=L[Cy_{p0}+y_p]=CL[y_{p0}]+L[y_p]=C\cdot 0+b(x)=b(x).$$
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

> Příklad. Rovnice $$y'+y=3 \tag{*}$$ má partikulární řešení $y=3$ (vidíme
  hned po dosazení). Asociovaná homogenní rovnice $$y'+y=0$$ má obecné
  řešení $y=Ce^{-x}$. Obecné řešení rovnice (*) tedy je 
	  $$y=3+Ce^{-x}.$$

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

