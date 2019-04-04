% Diferenciální rovnice a konečné diference
% Robert Mařík
% 2019


# Rozložení teploty na tepelně vodivé desce


Rovnici vedení tepla jsme odvodili ve tvaru 
$$
\frac{\partial u}{\partial t}-  \mathop{\mathrm{div}} (D \nabla u)=\sigma.
$$

Uvažujeme čtvercovou desku bez zdrojů tepla ($\sigma=0$), okraje desky
udržujeme na konstantní teplotě a deska je v rovnovážném stavu
(teplota se nemění v čase, $\frac{\partial u}{\partial t}=0$). Deska
je homogenní izotropní a koeficient tepelné vodivosti je konstantní skalární veličina ($D\in\mathbb R$).  Úloha se tedy redukuje na
$$\mathop{\mathrm{div}} (\nabla u) =0$$
tj.
$$\frac {\partial^2 u}{\partial x^2} + \frac {\partial^2 u}{\partial y^2} =0.$$

To je pořád dost komplikovaná úloha, zkusíme tedy něco jednoduchého.

# Rozložení teploty na tepelně vodivé desce přibližně


<div class='obtekat'>

![Rozložení teploty na tepelně vodivé desce je možné přibližně zkoumat metodami lineární algebry.](deska.png)

</div>


Desku rozdělíme sítí na $12$ uzlových bodů
(rohy zanedbáme) jak je uvedeno na obrázku.  V uzlových bodech na
okraji desky je teplota zadána (okrajová podmínka), zajímá nás
rozložení teploty v ostatních uzlových bodech.

Učiníme (poměrně realistický) předpoklad, že teplota v každém uzlovém
bodě je díky tepelné vodivosti desky ovlivněna sousedními uzlovými
body. Každý sousední bod má stejný vliv, proto teplota v uzlovém bodě
bude přibližně rovna aritmetickému průměru teplot v sousedních
bodech. Kvantitativně zformulováno, platí 
$$
\begin{aligned}
  x_1&=\frac 14(30+x_2+x_4)\\
  x_2&=\frac 14(60+x_1+x_3)\\
  x_3&=\frac 14(70+x_2+x_4)\\
  x_4&=\frac 14(40+x_1+x_3)
\end{aligned}
$$
anebo po úpravě
$$
\begin{aligned}
  4x_1-x_2-\qquad x_4&=30\\
  -x_1+4x_2-x_3\qquad&=60\\
  \qquad-x_2+4x_3-x_4&=70\\
  -x_1\qquad-x_3+4x_4&=40
\end{aligned}
$$
Dostali jsme soustavu lineárních rovnic o čtyřech neznámých.
Tuto úlohu je možno zformulovat pomocí  maticového násobení (s vynechanými nulami uvnitř matice)
$$
\begin{pmatrix}
 \phantom{-}4&-1&&-1\\
 -1& \phantom{-}4&-1&\\
 &-1& \phantom{-}4&-1\\
 -1&&-1& \phantom{-}4
\end{pmatrix}
\begin{pmatrix}
  x_1\\x_2\\x_3\\x_4
\end{pmatrix}
=
\begin{pmatrix}
  30\\60\\70\\40
\end{pmatrix}.
$$
Úloha je tedy převoditelná na úlohu řešení soustavy lineárních
rovnic. Pro podrobnější popis použijeme stejnou myšlenku, ale mnohem
více uzlových bodů. Postup je stejný, pouze vznikne soustava s více
neznámými a více rovnicemi. 


**Poznámka.** Rovnice popisující vedení tepla na základě fyzikálních
principů je poměrně komplikovaně řešitelná a proto se zpravidla
převádí na problém lineární algebry. Může to znít překvapivě, ale
skončíme u něčeho podobného jako v našem jednoduchoučkém modelu. Výše
uvedený postup se nazývá metoda konečných diferencí, ale jsou i další
metody, například metoda konečných prvků. Společným znakem je
rozdělení oblasti našeho zájmu na velké množství bodů a aproximace
fyzikálních zákonů pro sledovaný jev v každém bodě pomocí lineární
rovnice. Tím vznikne úloha na řešení soustavy rovnic. Používá se k
modelování proudění tepla nebo vody, k modelování mechanického
namáhání od jednoduchých nosníků po komplikované konstrukce nebo stromy.
Soustava vytvořená pomocí takových modelů je velmi řídká, má hodně
nul. Je proto možné ji rychle vyřešit i v případě tisíců rovnic.

# Konečné diference


<div class='obtekat'>

![Tramvajový most v Brně Pisárkách z předpjatého betonu. Vede do zatáčky a ve stoupání. Analyticky vyřešit namáhání takového mostu je nereálné, podobné úlohy se řeší převodem na úlohy lineární algebry. Podobné síly mohou vznikat i v\ dřevěných konstrukcích a to i v\ případě, že  nosníky primárně nekonstruujeme jako předpjaté. Zdroj: www.moravskyturista.cz.](pisarky.jpg)

</div>


Při přibližném modelování vynecháváme to nejsložitější, limitní
přechod v definici derivace
$$\frac{\mathrm df}{\mathrm dx}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$
Tedy $$\frac{\mathrm df}{\mathrm dx}\approx\frac{f(x+h)-f(x)}{h}.$$
Okamžitá rychlost je nahrazena průměrnou rychlostí na intervalu
$(x,x+h).$

Kromě dopředné diference někdy používáme zpětnou diferenci
$$\frac{\mathrm df}{\mathrm dx}\approx\frac{f(x)-f(x-h)}{h}$$
nebo jejich průměr, centrální diferenci
$$\frac{\mathrm df}{\mathrm dx}\approx\frac{f(x+h)-f(x-h)}{2h}.\tag{1}$$

Pro druhou derivaci dostáváme podobně pomocí diferencí aproximaci
druhé derivace pomocí funkční hodnoty funkce $f$ v daném bodě a v
bodech o $h$ doprava a doleva ve tvaru
$$ \frac{\mathrm d^2f}{\mathrm dx^2}= \frac{\frac{f(x+h)-f(x)}{h} - \frac{f(x)-f(x-h)}{h}}{h} =\frac{f(x-h)-2f(x)+f(x+h)}{h^2}. \tag{2} $$

Ke stejným výsledkům jako je (1) a (2) můžeme dospět pomocí aproximace Taylorovým polynomem druhého řádu
$$
\begin{gathered}
  f(x+h)\approx f(x)+\frac {\mathrm df}{\mathrm dx}h + \frac 12 \frac {\mathrm d^2f}{\mathrm dx^2}{h^2}\\
  f(x-h)\approx f(x)-\frac {\mathrm df}{\mathrm dx}h + \frac 12 \frac {\mathrm d^2f}{\mathrm dx^2}{h^2}  
\end{gathered}
$$
tak, že výše uvedené vztahy odečteme a vyjádříme první derivaci, nebo
odečteme a vyjádříme druhou derivaci.

Pro parciální derivace analogicky
$$
\begin{aligned}
\frac{\partial f}{\partial x}&\approx\frac{f(x+h,y)-f(x-h,y)}{2h},\\
\frac{\partial f}{\partial y}&\approx\frac{f(x,y+h)-f(x,y-h)}{2h},\\
\frac{\partial^2 f}{\partial x^2}&\approx\frac{f(x-h,y)-2f(x,y)+f(x+h,y)}{h^2},\\
\frac{\partial^2 f}{\partial y^2}&\approx\frac{f(x,y-h)-2f(x,y)+f(x,y+h)}{h^2}.
\end{aligned}
$$
Laplaceův operátor je například možné aproximovat pomocí vztahu
$$\frac{\partial^2 f}{\partial x^2}+\frac{\partial^2 f}{\partial y^2}\approx\frac{f(x-h,y)+f(x,y-h)-4f(x,y)+f(x+h,y)+f(x,y+h)}{h^2}$$
a Laplaceova rovnice popisující rozložení tepla na tepelně vodivé desce bez zdrojů a v ustáleném stavu 
$$\frac{\partial^2 f}{\partial x^2}+\frac{\partial^2 f}{\partial y^2}=0$$
má tvar
$$f(x-h,y)+f(x,y-h)-4f(x,y)+f(x+h,y)+f(x,y+h)=0,$$
tj.
$$f(x,y)=\frac 14 \Bigl(f(x-h,y)+f(x,y-h)+f(x+h,y)+f(x,y+h)\Bigr).$$
Jinými slovy, teplota v uzlovém bodu desky z předchozího slidu je
opravdu průměrem teplot v okolních uzlových bodech desky.

Proto byl náš postup korektní a zjednodušení, spočívající v nahrazení
složité parciální diferenciální rovnice jednoduchou soustavou rovnic,
bylo správné. O co víc: podobně je možné postupovat i tam, kde je naše
intuice nejistá anebo nedokážeme fyzikálně argumentovat při záměně
derivací za algebraické operace. Stačí se řídit odvozenými vztahy.


# Nosník 


<div class='obtekat'>

![Příhradový nosník. Vzpěry jsou namáhány v ose. Teorii vybudoval v 18. století L. Euler, ale začala se dále rozvíjet a využívat až po [sérii pádů](https://en.wikipedia.org/wiki/Cast-iron_architecture#Catastrophic_failures) příhradových železničních mostů v 19. století. Zdroj: www.ceskestavby.cz.](nosnik.jpg)

</div>

**Příklad** (podle Autar Kaw et al.: [Finite Difference Method for
Ordinary Differential
Equations](http://nm.mathforcollege.com/topics/finite_difference_method.html).)
Deformace $y$ nosníku délky $L$ podepřeného na koncích, vystaveného
vertikálnímu zatížení $q$ a axiálnímu namáhání $T$ je dána rovnicí
$$\frac{d^2 y}{dx^2}-\frac {T}{EI} y=\frac{qx(L-x)}{2EI},$$ kde $E$ je
materiálová charakteristika a $I$ je veličina související s\ průřezem
nosníku (kvadratický moment průřezu, souvisí s\ velikostí i\ s\ tvarem). Okrajové podmínky jsou $y(0)=0$ a $y(L)=0$. 
Po aproximace druhé derivace výrazem s konečnými diferencemi dostáváme
$$\frac{y(x-h)-2y(x)+y(x+h)}{h^2}-\frac {T}{EI}
y(x)=\frac{qx(L-x)}{2EI}.$$ Pokud délku nosníku $L$ rozdělíme na $n$
částí délky $h$ a pokud označíme $x_i=ni$, $y_i=y(x_i)$, rovnice se
redukuje na rovnici $$\frac{y_{i-1}-2y_i+y_{i+1}}{h^2}-\frac {T}{EI}
y_i=\frac{qx_i(L-x_i)}{2EI}.$$ To je pro $i$ od $i=1$ po $i=n-1$
celkem $n-1$ lineárních rovnic. K tomu přidáváme rovnice na koncích
podepřeného nosníku, kdy platí $y_0=0$ a $y_n=0$. Celkem tedy máme
soustavu $n+1$ lineárních rovnic o $n+1$ neznámých. Soustava je
řešitelná. Protože pro jemné dělení je rovnic obrovské množství, není
vhodné se problém snažit zdolat metodami řešení rovnic známými ze
střední školy. Existují velmi rychlé iterační metody, které umožní
najít řešení pomocí operací, které se dají v počítači realizovat velmi
levně.


# Vylepšení?

Metoda konečných diferencí má někdy potíže způsobené tím, že mříž je v celém studovaném problému rovnoměrná. To někdy nemusí být optimální, bylo by vhodné vlit jemnější dělení tam, kde očekáváme dramatické změny a hrubší dělení tam, kde neočekáváme velké změny v řešení. Jedna z možností, jak se s tímto vyrovnat je metoda konečných prvků. Přesný matematický popis je nepoměrně náročnější, než u metody konečných diferencí, co je však podstatné je

* že metoda konečných prvků redukuje úlohu modelovanou pomocí diferenciální rovnice na úlohu lineární algebry (soustava rovnic),
* a že metoda konečných prvků je upravena do tvaru, kdy ji po určitém zaškolení může používat v řadě případů s úspěchem i člověk, který do podstaty úlohy nevidí.

Z výše uvedených důvodů a hlavně proto, že tato metoda poskytuje
perfektní výsledky, je metoda konečných prvků jedna z
nejpoužívanějších metod v matematickém modelování. O alanytické
řešení, jak jsme to dělali při separaci proměnných Fourierovou metodou
se zpravidla snažíme jenom v nejjednodušších případech, abychom
porozuměli problematice a získali zkušenosti a jistý vhled do
problematiky. Reálné úlohy řešící statiku mostů či budov nebo
komplexní tepelnou výmenu mezi budovou a okolím řešíme numericky,
metodou konečných diferencí, konečných prvků nebo dalšími podobnými
metodami.



