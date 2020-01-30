% Autonomní systémy
% Robert Mařík
% 2020

# Opakování

* Maticový součin
* Řešitelnost homogenní soustavy lineárních rovnic
* Vlastní hodnoty a vlastní vektory
* Chování exponenciální funkce $e^{kt}$ v nekonečnu

# Autonomní systém $X'=AX$

# Autonomní systém $X'=f(X)$

# Autonomní systém v jedné dimenzi

Rovnice $$\frac{\mathrm dy}{\mathrm dx}=f(y)\tag{1}$$ je autonomní
systém v jedné dimenzi. Je speciálním případem rovnice se separovanými
proměnnými, která je uvedena na dalším slidu a umíme ji řešit
analytickou cestou. Proto se nyní nebudeme zaměřovat na hledání
obecného řešení, ale pokusíme se popsat chování řešení, aniž bychom
tato řešení znali. Pokusíme se s\ co nejmenší námahou říct, jak se
budou řešení chovat.

Všechna konstantní řešení rovnice (1) jsou nulové body pravé strany. Kromě toho musíme poosudit stabilitu.

> Věta (stabilita konstantních řešení). Jestliže platí $f(y_0)=0$, je
  konstantní funkce $y(x)=y_0$ konstantním řešením rovnice
  $$\frac{\mathrm dy}{\mathrm dx}=f(y).$$ Toto řešení je stabilní
  pokud $f'(y_0)<0$ a nestabilní pokud $f'(y_0)>0$.

Pro grafickou intepretaci je vhodné připomenout, že funkce s kladnou
derivací jsou rostoucí a funkce se zápornou derivací klesající. Pokud
má tedy pravá strana derivaci různou od nuly, poznáme stabilitu z\ monotonie pravé strany.

# Logistická diferenciální rovnice s konstantním lovem


<div class='obtekat'>

![Pravá strana k modelu lovu s konstantní intenzitou.](logisticka-lov.png)

</div>


Logistická diferenciální rovnice s konstantním lovem $h$, tj. rovnice
$$\frac{\mathrm dy}{\mathrm dt}=ry\left(1-\frac yK\right)-h,$$ má pro
malé $h$ dva stacionární body. Funkce $ry\left(1-\frac yK\right)$ je
parabola otočená vrcholem nahoru a s nulovými body $y=0$ a $y=K$. V
prvním stacionárním bodě je funkce rostoucí a tento stacionární bod je
nestabilní. Ve druhém stacionárním bodě je funkce klesající a tento
stacionární bod je stabilní. Jak se zvyšuje faktor $h$, graf paraboly
se posouvá směrem dolů a oba stacionární body se posouvají směrem k
sobě a k\ vrcholu. Jejich stabilita zůstává neporušena. To znamená, že
sice pořád existuje stabilní stav, ale se zvyšující se intenzitou lovu
se tento stacionární stav dostává stále blíže ke stavu nestacionárnímu
a rovnováha je tedy poněkud křehká.

[Nakreslit online](https://sagecell.sagemath.org/?z=eJx90D8OgjAYh-HdxDswkLRIIW3p2tm1NzAFChhqawpo8U6ewosJOPgvId_8Pr_kE4Sfte2h30GS-AhBjzAiEdKqVqY8aJkrzUHYcJxiHIJouxH0q0hwStYqMlWosNo6DpwqFyH7FeiaQD-E2illFoP9GWwVYW8k17JoZ2S-rrFXKEgsaCyyWDA0no6GTx4mqD_2WnGwd7IKuou8tUNQDaYtHvcgHLl_LTfTV577N1xo&lang=sage&interacts=eJyLjgUAARUAuQ==)

# Model soupeření jestřábí a holubičí povahy

\iffalse 

<div class='obtekat'>

![V modelu jestřáb-holubice (hawk-dove) nejde o skutečné živočišné druhy, ale o strategii chování. Předmětem modelu je jestřábí a holubičí povaha u jedinců téhož druhu. Zdroj: pixabay.com](harris-hawk.jpg)

</div>

\fi


Cílem tohoto modelu je studovat typy chování živočichů a rostlin a
zjistit, zda některý typ chování přináší jeho nositelům evoluční
výhodu.

Nechť se v populaci vyskytují dva vzorce chování -- jedince
používající první z nich budeme nazývat *jestřábi* a druhý
*holubice*. Chování se projeví, pokud se dva jedinci setkají
u téhož zdroje (potrava, hnízdistě, apod). 

* Jestřáb o zdroj bojuje a ustoupí pouze po prohraném boji.
* Holubice
  o zdroje nebojuje a zkonzumuje zdroj pouze pokud protivník ustoupí
  bez boje.
* Předpokládejme, že každý jedinec v populaci si zkonzumování
  zdroje si může svou evoluční zdatnost posílit o hodnotu $V$, pokud
  je nucen a ochoten o zdroj bojovat, je jeho evoluční zdatnost naopak
  snížena o hodnotu $D$. 
* Setkají-li se u zdroje dvě holubice, jedna z nich ustoupí bez boje
  a druhá zkonzumuje zdroj. Předpokládejme, že po častých setkáních
  tohoto typu každá holubice zkonzumuje průměrně polovinu zdrojů.
* Setká-li se u zdroje holubice s jestřábem, zkonzumuje celý zdroj
  jestřáb.
* Setkají-li se u zdroje dva jestřábi, ani jeden z nich neustoupí
  a bojují o zdroj. Předpokládejme, že všichni jestřábi jsou stejně
  silní a po boji je pravděpodobnost zkonzumování zdroje poloviční pro
  každého jestřába.  

Matematický rozbor (J. Kalas, Z. Pospíšil, Spojité modely v biologii) ukazuje, že četnost $x$ výskytu jestřábů v populaci
řídí diferenciální rovnicí
$$x'=x(1-x)\left(\frac V2-\frac D2 x\right).$$
Jediné realistické hodnoty $x$ jsou z intervalu $[0,1]$. Pro nalezení stacionárních bodů a posouzení jejich stability budeme studovat funkci
$$f=x(1-x)\left(\frac V2-\frac D2 x\right).$$ Stacionární body rovnice jsou nolové body funkce $f$ a to jsou $x=0$, $x=1$ a $x=\frac VD$.

* V bodě $x=0$ funkce $f$ nulová a rostoucí. Stacionární bod $x=0$ je vždy nestabilní. **Ať jsou tedy podmínky jakékoliv, vždy budou v populaci
    přítomni jestřábi.** Přitom právě jestřábi paradoxně plýtvají
  zdroji energie na boj, namísto, aby celou energii zaměřili na
  rozmnožování. Z hlediska efektivity při využívání zdrojů prostředí
  platí, že populace složená ze samých holubic využívá zdroje
  prostředí nejefektivnějším možným způsobem.  Přesto je taková
  populace evolučně nestabilní! Pronikne-li do populace samých holubic jeden jestřáb, má značnou evoluční výhodu, protože každý zdroj, u kterého se nachází,
  zkonzumuje. Tím poroste jeho evoluční zdatnost a jeho geny nebo vzorce chování (u druhů které mohou přepínat strategie chování) se budou
  v populaci rychle šířit.  
* Pokud jsou náklady na boj větší než užitek ze zdrojů, platí $V<D$.
  V intervalu $[0,1]$ leží stacionární bod $x=\frac VD$ a tento bod je
  stabilní. Poslední stacionární bod $x=1$ je nestabilní. V tomto
  případě všechna řešení konvergují ke stacionárnímu bodu $x=\frac
  VD$. V populaci tedy budou přítomni i jestřábi i holubice.
* Pokud platí $V>D$, všechna řešení konvergují ke stacionárnímu
  bodu $x=1$. Ať je počáteční rozložení vzorců chování v populaci
  jakékoliv, evolučně stabilní je pouze populace složená ze samých
  jestřábů.  Jsou-li náklady na boj o zdroje nižší než užitek ze
  zdrojů, nevyplatí se ustupovat při soupeření o zdroje. *Příkladem
  populace složené ze samých jestřábů je les. Náklady na boj spočívají
  ve vytvoření vyššího kmene, užitkem je světlo.*


# Autonomní systém ve dvou dimenzích


# Bruselátor

\iffalse 

<div class='obtekat'>

![Fázový portrét brusselátoru. Zdroj: Wikipedia](Bruesselator.png)

</div>

\fi


Systém chemických reakcí
$$\begin{aligned}A &\rightarrow X\\2X + Y &\rightarrow 3X\\B + X &\rightarrow Y + D\\X &\rightarrow E\end{aligned}$$
má pozoruhodnou minulost. Jeho objevitelé (reakci objevil Belousov, jeho výsledky přezkoumal a potrvrdil Zabotinski) zaznamenali překvapivé chování, kdy se periodicky mění koncentrace. Protože to bylo v roce 1951 mimo chápání chemiků, měli potíže s publikováním tohoto převratného jevu. Všeobecně panoval názor, že chemická reakce rychle spěje ke stavu termodynamické rovnováhy a oscilující reakce byla něco jako chemické perpetum mobile. Později matematikové (Prigogine) sestavili teoretický model periodicky probíhající reakce a po čase několik takových reakcí i našli. Dnes toto chápeme jako jakési chemické hodiny. Název bruselátor je spojení slova Brusel (pracoviště Prigogina) a oscilátor.

Pokud je dostatek složek $A$ a $B$, modeluje po zjednodušení (viz Wikipedie, konstanty úměrnosti klademe rovny jedné) chemické reakce soustava
$$
\begin{aligned}
\frac {\mathrm d X}{\mathrm dt}&= A  +  X ^2 Y  - B X - X,\\
\frac {\mathrm d Y}{\mathrm dt}&= BX-X^2Y,
\end{aligned}
$$
kde $X$ pro jednoduchost znamená koncentraci látky $X$ a totéž platí i pro další veličiny vystupující v rovnici.

# Vícerozměrné autonomní systémy, kompartmentové modely

