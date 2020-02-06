% Autonomní systémy
% Robert Mařík
% 2020

# Opakování

* Maticový součin
* Řešitelnost homogenní soustavy lineárních rovnic
* Vlastní hodnoty a vlastní vektory
* Chování exponenciální funkce $e^{kt}$ v nekonečnu

# Úmluva

V celé přednášce budeme jako nezávislou proměnnou uvažovat čas
$t$. Autonomní znamená v tomto kontextu nezávislý na čase. Budeme
studovat rovnice mající tuto vlastnost.

# Autonomní systém v jedné dimenzi


Rovnice $$\frac{\mathrm dy}{\mathrm dt}=f(y)\tag{1}$$ je autonomní
systém v jedné dimenzi. Je speciálním případem rovnice se separovanými
proměnnými a umíme ji řešit
analytickou cestou. Proto se nyní nebudeme zaměřovat na hledání
obecného řešení, ale pokusíme se popsat chování řešení, aniž bychom
tato řešení znali. Pokusíme se s\ co nejmenší námahou říct, jak se
budou řešení chovat.

Všechna konstantní řešení rovnice (1) jsou nulové body pravé strany. Kromě toho musíme posoudit stabilitu, což umožní následující věta.

> Věta (stabilita konstantních řešení). Jestliže platí $f(y_0)=0$, je
  konstantní funkce $y(x)=y_0$ konstantním řešením rovnice
  $$\frac{\mathrm dy}{\mathrm dt}=f(y).$$ Toto řešení je stabilní
  pokud $f'(y_0)<0$ a nestabilní pokud $f'(y_0)>0$.

Pro grafickou intepretaci je vhodné připomenout, že funkce s kladnou
derivací jsou rostoucí a funkce se zápornou derivací klesající. Pokud
má tedy pravá strana derivaci různou od nuly, poznáme stabilitu z\ monotonie pravé strany.

Věta je odvozena z pozorování, že rovnice $y'=ky$ má řešení $y(t)=Ce^{kt}$ a toto řešení se pro velká $t$ blíží k nule nebo roste neohraničeně, v závislosti na znaménku hodnoty $k$. Pravou stranu rovnice, funkci $f(y)$, je možné aproximovat vztahem $f(y)\approx f'(y_0)(y-y_0)$ a odsud a z poznatku, že malá změna rovnice vetšinou nemění dramaticky chování řešení (přesněji, existuje spojitá závislost na parametrech) a proto rovnice $y'=f(y)$ kopíruje v okolí bodu $y_0$ chování rovnice $(y-y_0)'=f'(y_0)(y-y_0)$, pokud vynecháme patologické případy, což je zde $f'(y_0)=0$. Řešení je tedy $y\approx y_0+Ce^{f'(y_0)t}$ a tato funkce buď konverguje k $y_0$ nebo roste neohraničeně, v závislosti na znaménku derivace $f'(y_0)$.

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


# Logistická diferenciální rovnice s predátory

<div class='obtekat'>

\iffalse

![Model obaleče byl publikován v D. Ludwig, D.D. Jones and C.S. Holling, Qualitative analysis of insect outbreak systems: the spruce budworm and forest, Journal of Animal Ecology 47(1): 315–332, February 1978 a v tomto odstavci je zpracován podle knihy [Brauer, Kribs, Dynamical systems for biological modelling](https://katalog.mendelu.cz/documents/223086?back=https%3A%2F%2Fkatalog.mendelu.cz%2Fsearch%3Ftype%3Dglobal%26q%3DDYNAMICAL%2BSYSTEMS%2BFOR%2BBIOLOGICAL%2BMODELING&group=223086,175427,175821), plný text je pro uživatele MENDELU zdarma. zdroj: Wikimedia.org](obalec.jpg)

\fi

![Pravá strana diferenciální rovnice modelu obaleče jako funkce proměnné $y$.](budworm.png)

</div>

Následující model je model obaleče *Choristoneura fumiferana*, který periodicky atakuje lesy severní Ameriky. Jeho populace je relativně malá, ale některé roky (historicky cca po
40 letech) se velikost populace zvýší tisícinásobně a dokáže zahubit
$80\%$ stromů v lese a prakticky zničit les. Populaci je možno modelovat logistickou rovnicí $$y'=ry\left(1-\frac yK\right)-H\frac{y^2}{y^2+A^2},$$
kde druhý člen na pravé straně charakterizuje vliv predátorů. Jedná se o funkci, která zpomaluje růst, podobně jako lov. Protože však predátoři mají určitou hodnotu, nad kterou jsou saturovaní a nestačí brzdit růst populace, je tato funkce ohraničená. Platí $$H\frac{y^2}{y^2+A^2}  \leq H.$$ To má dalekosáhlé důsledky.
Pro určité hodnoty parametrů může mít pravá strana rovnice dva nebo čtyři nulové body. Nakreslíme si [druhou variantu](https://sagecell.sagemath.org/?z=eJwrSyzSUK9U1-TlKrI10DPl5fK2NTTg5fKwNeTlcgQRaRqVmrZFWpVaGoa6lfremroeWpVxRvoaQELbMc4IqLEgJ79EA6RMR6NSx0DH0EBTR6EyNzPPVtdAz1ATAENFFxg=&lang=sage&interacts=eJyLjgUAARUAuQ==). 

Vidíme dva průsečíky, kde je funkce rostoucí, to odpovídá nestabilním
stavům. Vidíme i dva stabilní stavy, přibližně pro hodnoty $0.6$ a
$7.3$. Malé populace, které se rozvíjejí od nuly, dospějí do nižšího
stabilního stavu. Pokud se nějakým způsobem změní velikost populace o
malé množství, systém se po čase díky stabilitě vrátí do původního
stavu. Pokud však skok je velký a systém populace se dostane nad
hodnotu nestabilního stavu, růst pokračuje a systém spěje ke
stabilitě, ale s vyšším výskytem škůdce odpovídající stacionárnímu
bodu $7.3$.

Brauer a Kirbs vysvětlují situaci tak, že s růstem lesa se mění
parametry modelu, stacionární body se posunují a populace obaleče se
tomu přizpůsobuje. Více stromů znamená vyšší nosnou kapacitu prostředí
pro obaleče a predátoři svou činností populaci obaleče udržují na
rozumné míře. Pokud však nosná kapacita prostředí dosáhne takové
hodnoty, že predátoři jsou nasycení a nestačí populaci redukovat,
odpovídá to posunu nestabilního stacinárního bodu pod hodnotu
velikosti populace a dojde k přemnožení. Toto přemnožení má
devastující účinky pro les.





# Model soupeření jestřábí a holubičí povahy

\iffalse 

<div class='obtekat'>

![V modelu jestřáb-holubice (hawk-dove) nejde o skutečné živočišné druhy, ale o strategii chování. Předmětem modelu je jestřábí a holubičí povaha u jedinců téhož druhu. Zdroj: pixabay.com](harris-hawk.jpg)

![Pravá strana modelu v závislosti na hodnotě parametrů.](chovani.png)

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
$$f=x(1-x)\left(\frac V2-\frac D2 x\right).$$ Stacionární body rovnice jsou nulové body funkce $f$ a to jsou $x=0$, $x=1$ a $x=\frac VD$. Poslední stacionární bod v závislosti na hodnotě paraemtrů [může a nemusí](https://sagecell.sagemath.org/?z=eJxL06jQCdNx0bSt0NIw1K3Q1NII0zfSddE30qrQ5OUqyMkv0YhOA6ox1DHQM9LUATEN9Ex0DDVjdUBMIEMnJzU9NS8lPicxKTXHNrpIXSXMzkVFXQfEsAEyYjUBCOEZ8g==&lang=sage&interacts=eJyLjgUAARUAuQ==) ležet v intervalu $[0,1]$

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



# Autonomní systém ve dvou dimenzích, vektorový zápis

\iffalse 

<div class='obtekat'>

![Vajíčko je vhodný model pro zprostředkování přenosu tepla a tím i pro popis změny teploty pomocí systému dvou diferenciálních rovnic. Zdroj: pixabay.com](vajicko.jpg)


</div>

\fi



Následující příklad je mírně modifikovaný příklad z [kurzu MIT o diferenciálních rovnicích](https://youtu.be/MCrDzhpu3-s?t=671). Budeme modelovat ohřívání vejce ve vodě o konstantní teplotě $T_0$. Na počátku mají bílek a žloutek teplotu $T_1$ a $T_2$. Žloutek přebírá teplo od bílku rychlostí úměrnou rozdílu teplot žloutku a bílku. Bílek přebírá teplo od vodní lázně rychlostí úměrnou rozdílu teplot a předává teplo žloutku procesem popsaným v předchozí větě. Vody je hodně a její teplota se nemění. Proces můžeme modelovat soustavou diferenciálních rovnic $$\begin{aligned}T_1^\prime &= k_1(T_0-T_1)-k_2(T_1-T_2) \\ T_2^\prime&=k_2(T_1-T_2)\end{aligned}$$
Tento systém je možno přepsat do tvaru
$$\begin{aligned}T_1^\prime &= -(k_1+k_2)T_1+k_2T_2+T_0k_1 \\ T_2^\prime&=k_2T_1-k_2T_2\end{aligned}$$
a zapsat maticově $$\begin{pmatrix}T_1\\T_2\end{pmatrix}'=
\begin{pmatrix}-(k_1+k_2) & k_2 \\ k_2 & -k_2\end{pmatrix}
\begin{pmatrix}T_1\\T_2\end{pmatrix}
+
\begin{pmatrix}k_1T_0\\0\end{pmatrix}.
$$
Pokud zvolíme teplotní stupnici tak, že teplotě vroucí vody je v naší nové stupnici nula, můžeme dokonce eliminovat druhý člen a dostáváme
$$\begin{pmatrix}T_1\\T_2\end{pmatrix}'=
\begin{pmatrix}-(k_1+k_2) & k_2 \\ k_2 & -k_2\end{pmatrix}
\begin{pmatrix}T_1\\T_2\end{pmatrix}
$$
tj. symbolicky $X'=AX$, kde $X=(T_1,T_2)^T$ je vektorová funkce (sloupcový vektor) a $A$ je $2\times 2$ matice.

# Autonomní systém $X'=AX$

Je-li determinant matice nenulový, má soustava $AX=0$ pouze nulové řešení a systém $$X'=AX$$ má jediné konstantní řešení, kterým je počátek. Konstantní řešení bude nazývat stacionární bod.

Autonomní systém $$X'=AX$$ je lineární, protože díky distributivnímu zákonu pro matice pro operátor $L[X]=X'-AX$ platí
\dm$$L[X_1+X_2]=(X_1+X_2)'-A(X_1+X_2)=X_1^\prime+X_2^\prime-AX_1 -AX_2=(X_1^\prime -AX_1)+(X_2^\prime-AX_2)=L[X_1]+L[X_2]$$
a díky komutativitě při násobení s konstantou $C\in\mathbb R$ také
\dm$$L[CX]=(CX)'-A(CX)=CX'-CAX=C(X'-AX)=CL[X].$$

Je možné ukázat, že každá počáteční úloha je jednoznačně řešitelná a pro obecné řešení stačí najít tolik nezávislých řešení, kolik komponent má neznámá vektorová funkce $X$. Platí následující věta, kterou je možno ověřit přímo dosazením.

> Věta (souvislost vlastních čísel matice a řešení autonomního systému). Má-li matice $A$ vlastní číslo $\lambda$ a příslušný vlastní vektor je $v$, tj. platí $A v =\lambda v$, je funkce $X(t)=v e^{\lambda t}$ řešením systému $AX'=X.$ Jsou-li $\lambda$ a $v$ komplexní, je řešením i samostatně reálná část a imaginární část.

Autonomní systém $$X'=AX+B\tag{1}$$ je možno na předchozí případ převést po přepsání do tvaru $(X-X_0)'=A(X-X_0)$, kde $X_0$ je řešením soustavy $AX+B=0$, což odpovídá posunu stacionárního bodu do počátku.

> Poznámka (vlastní hodnoty a řešení). Následující poznatky jsou shrnutím a specifikací výše uvedeného a klasifikují stabilitu někerých řešení systému (1), tj. $$X'=AX+B.$$ 
>
> * Jakmile má systém reálnou kladnou vlastní hodnotu, existuje řešení, které se vzdaluje od stacionárního bodu směrem daným příslušným vlastním vektorem.
> * Jakmile má systém reálnou zápornou vlastní hodnotu, existuje řešení, které se přibližuje ke stacionárnímu bodu ze směru daného příslušným vlastním vektorem.
> * Jakmile má systém komplexní hodnotu s kladnou reálnou částí, existuje řešení, které se v oscilacích vzdaluje od stacionárního bodu.
> * Jakmile má systém komplexní hodnotu se zápornou reálnou částí, existuje řešení, které se v oscilacích přibližuje ke stacionárnímu bodu.

Pokud jsou například všecha vlastní čísla v daném bodě záporná, poté takto čísla generují řešení konvergující do stacionárního bodu. Díky linearitě, jednoznačnosti řešení a tomu, že máme tolik řešení, kolik je nutno pro splnění libovolné podmínky, je možné pomocí těchto dílčích řešení zapsat i libovolné jiné řešení. Tím pádem ale všechna řešení konvergují do stacinárního bodu. Podobně, pokud všechny vlastní hodnoty jsou kladné, všechna řešení se od stacionárního bodu vzdalují. 


**Příklad.** Model ohřívání vajíčka má stacionární bod $(0,0)$. Zkusíme li bovolně zvolit parametry a určit chování trajektorií v okolí tohoto bodu. Pro $k_1=1$ a $k_2=2$ dostáváme
$$\begin{pmatrix}T_1\\T_2\end{pmatrix}'=
\begin{pmatrix}-3 & 2 \\ 2 & -2\end{pmatrix}
\begin{pmatrix}T_1\\T_2\end{pmatrix}.
$$
Charakteristická rovnice je 
$$\lambda^2+5\lambda+2=0$$
se dvěma zápornými kořeny $\lambda_{1,2}=\frac{-5\pm\sqrt{25-8}}{2}=\cdots$. Budou tedy existovat dvě nezávislá řešení konvergující do počátku a všechna další řešení dostaneme jako jejich lineární kombinaci. Proto všechna řešení knvergují k počátku tj. $T_1=T_2=0$. Obě teploty v naší posunuté stpunici se tedy ustálí na teplotě vodní lázně. Nic jiného jsme ani nečekali, ať mají žloutek a bílek ba začátku jakoukoliv teplotu, po čase se teplota ustálí na teplotě vodní lázně.



# Autonomní systém $X'=f(X)$

Obecný autonomní systém nemusí být lineární.

**Doplnit příklad**

Ukážeme si, jak studovat nelineární systém pomocí lineárního a pomocí vlastních čísel. Půjde o lineární paroximaci. V tomto případě o lineární aproximaci vektrorové funkce definující pravé strany rovnic.

Je-li $f(X_0)=0$, je možno systém $$X'=f(X)$$ v okolí bodu $X_0$ aproximovat lineárním systémem $$X'=J(X_0)(X-X_0),$$
kde $J(X_0)$ je Jacobiho matice funkce $f(X)$ v bodě $X_0$, tj. pro $f(X)=(f_1(X),\dots,f_n(X))^T$ je
$$J(X)=\left(\frac{\partial f_i(X_0)}{\partial x_j}\right).$$
O stabilitě tedy rozhodnou vlastní čísla Jacobiho matice. Toto platí
za předpokladu, že Jacobiho matice je regulární, tj. její determinant
je nenulový nula není jejím vlastním číslem. Nelineární systém v
jistém smyslu "zdědí" chování řešení od své lineární aproximace pomocí
Jacobiho matice. Je však nutno připomenout, že aproximace pomocí Jacobiho matice je jenom lokální a můžeme takto posoudit jenom řešení z nějakého okolí stacionárního bodu. Zejména tedy, pokud má Jacobiho matice všechny vlastní hodnoty záporné, tak všechna řešení z nějakého okolí stacionárního bodu konvergují do tohoto  bodu. Pokud má všechny vlastní hodnoty kladné, všechna řešení z nějakého okolí se naopak od stacionárního bodu vzdalují. To platí i pro vlastní komplexní vlastní hodnoty, pouze se mezi konvergencí a vzdalování přepíná podle znaménka reálné části vlastních hodnot a řešení oscilují směrem ke stacionárnímu bodu nebo od něj.



# Bruselátor

\iffalse 

<div class='obtekat'>

![Belousova-Zabotinskeho reakce vytváří periodicky se měnící obrazce. Autor: Stephen Morris, flickr.com](bz-reakce.jpg)

![Fázový portrét brusselátoru. Zdroj: Wikipedia](Bruesselator.png)

</div>

\fi

Systém chemických reakcí
$$\begin{aligned}A &\rightarrow X\\2X + Y &\rightarrow 3X\\B + X &\rightarrow Y + D\\X &\rightarrow E\end{aligned}$$
má pozoruhodnou minulost. Jeho objevitelé (reakci objevil Belousov, jeho výsledky přezkoumal a potvrdil Zabotinski) zaznamenali překvapivé chování, kdy se periodicky mění koncentrace. Protože to bylo v roce 1951 mimo chápání chemiků, měli potíže s publikováním tohoto převratného jevu. Všeobecně panoval názor, že chemická reakce rychle spěje ke stavu termodynamické rovnováhy a oscilující reakce byla něco jako chemické perpetum mobile. Později matematikové (Prigogine) sestavili teoretický model periodicky probíhající reakce a po čase několik takových reakcí i našli. Dnes toto chápeme jako jakési chemické hodiny. Název bruselátor je spojení slova Brusel (pracoviště Prigogina) a oscilátor.

Pokud je dostatek složek $A$ a $B$, modeluje po zjednodušení (viz Wikipedie, konstanty úměrnosti klademe rovny jedné) chemické reakce soustava
$$
\begin{aligned}
\frac {\mathrm d X}{\mathrm dt}&= A  +  X ^2 Y  - B X - X,\\
\frac {\mathrm d Y}{\mathrm dt}&= BX-X^2Y,
\end{aligned}
$$
kde $X$ pro jednoduchost znamená koncentraci látky $X$ a totéž platí i pro další veličiny vystupující v rovnici.

Stacionárním bodem je bod $X=A$, $Y=\frac BA$. Pro $A=1$ a $B=4$ má systém tvar
$$
\begin{aligned}
\frac {\mathrm d X}{\mathrm dt}&=    X ^2 Y  - 5 X,\\
\frac {\mathrm d Y}{\mathrm dt}&= 4X-X^2Y,
\end{aligned}
$$

Jacobiho matice je $$J(X,Y)=\begin{pmatrix}2XY-5 & X^2 \\ 4-2XY & -X^2\end{pmatrix}$$
a $$J(1,4)=\begin{pmatrix}3& 1\\-4 & -1\end{pmatrix}.$$
Vlastní čísla jsou řešením rovnice
$$0=\begin{vmatrix}3-\lambda & 1\\-4 & -1-\lambda\end{vmatrix}
=\lambda^2- 2\lambda+4=(\lambda-1)^2+3.$$
Taková rovnice nemá řešení v množině reálných čísel a vlastní čísla jsou komplexně sdružená $$\lambda_{1,2}=1\pm \sqrt {3}i.$$ Protože reálná část $\Re(\lambda_i)=1>0$, řešení se v oscilacích vzdalují od rovnovážného bodu. Protože systém je druhého řádu a tímto postupem je možno získat dvě nezávislá řešení, lineárními kombinacemi vygenerujeme všechna řešení. Proto se v oscilacích budou od stacionárního bodu vzdalovat všecha řešení. Další stacionární bod neexistuje a koncentrace určitě zůstanou ohraničené z fyzikálních důvodů. Proto neexistuje stabilní stav, a systém je nestabilní. Je možné ukázat, že systém není chaotický, ale oscilacemi se přibližuje k periodickému řešení. Taková analýza je však již nad rámec základního seznámení se s aparátem autonomních systémů. 

# Autonomní systém ve dvou dimenzích

Autonomní systémy prozkoumáme ve cvičení. 


# Vícerozměrné autonomní systémy, kompartmentové modely

