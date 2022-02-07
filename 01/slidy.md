% Derivace funkce více proměnných
% Robert Mařík
% 2020

> Anotace.
>
> * Naučíme se sledovat rychlost, s jakou se mění veličina, která je objektem našeho zájmu.
> * Budeme schopni sledovat rekci sledované veličiny na současné změny více parametrů. Například u teploty můžeme sledovat jak se v daném místě mění teplota v čase, nebo jak se v daný okamžik mění teplota s polohou.
> * Aparát využijeme k tomu, že z fyzikálních zákonů sestavíme rovnici vedení tepla. To bude matematický model umožňující jednak modelování přenosu tepla a jednak kontrolu toho, že fyzikální zákony vedoucí k formulaci této rovnice jsou správné.

> Prerekvizity.
>
> * Navážeme na znalosti z diferenciálního počtu funkcí jedné proměnných. Zejména definice, využití a výpočet derivace.
> * Zopakujte si fyzikální (praktický) význam derivace a pro osahání si konkrétních příkladů také základní metody výpočtu.


# Funkce jedné proměnné

https://youtu.be/zhaebxHbqhs


\iffalse 


<div class='obtekat'>

![2d graf funkce jedné proměnné.](2D_graf.png)

</div>

\fi


Základní informace o funkci jedné proměnné a její derivaci si můžete osvěžit v materiálech k předmětu [Matematika](http://user.mendelu.cz/marik/mtk/mat-slidy/derivace_I/).

* Zobrazení $f: \mathbb{R}\to \mathbb{R}$ se nazývá funkce jedné proměnné. 
* V kartézské rovině píšeme též $y=f(x)$, kreslíme uspořádané dvojice bodů $[x,y]$ a výstupem je zpravidla křivka v rovině ([Nakreslit online.](https://sagecell.sagemath.org/?z=eJxL06jQtK3QSq0o0NCt0OTlKsjJL9FQSAOKKugoaFTo6BrqmGgqaAIA3aEKBw==&lang=sage))
* Rychlost změny je derivace:
$$f'(x):=\lim_{h\to 0}\frac{f(x+h)-f(x)}h$$
* Podle kontextu a oborových zvyklostí zapisujeme derivaci pomocí čárky (někdy tečky) nebo jako podíl diferenciálů
$$y', \quad \frac{\mathrm dy}{\mathrm dx}, \quad \frac{\mathrm d}{\mathrm dx}y$$
* rychlost změny změny je druhá derivace: $$y'',\quad  \frac{\mathrm d^2y}{\mathrm dx^2}, \quad\frac{\mathrm d^2}{\mathrm dx^2}y$$

> Poznámka (Newtonův zákon tepelné výměny). Je-li $T(t)$ teplota tělesa v čase $t$, je $\frac{\mathrm dT}{\mathrm dt}$ změna této teploty za jednotku času, tj. rychlost s jakou roste teplota. Například hodnota derivace $$\frac{\mathrm dT}{\mathrm dt}(6)=2 ^\circ \mathrm {C}/\mathrm{min},$$ kdy teplotu ve stupních Celsia sledujeme jako funkci času v minutách, nás informuje o tom, že v čase $6$ minut roste teplota okamžitou rychlostí $2$ stupně Celsila za minutu. Pokud tento růst vydrží celou minutu, bude v čase $7$ miunt teplota o dva stupně Celsia vyšší. Pokud tato rychlost růstu vydrží deset minut, jsme schopni podobně určit změnu teploty i za delší časový úsek.
>
>V reálných dějích však konstantní rychlosti vídáme zřídka. Například u tepelné výměny se dynamika procesu zastavuje tím, jak se teploty postupně vyrovnávají. Častým modelem reálné situace je předpoklad, že rychlost s jakou roste teplota chladného tělesa při tepelné výměně s teplejším tělesem konstantní teploty je úměrná rozdílu teplot. Roli teplejšího tělesa hraje většinou okolí. Pokud je tedy teplota okolí konstantní a rovna $T_0$, je kvantitativním modelem procesu tepelné výměny rovnice $$\frac{\mathrm dT}{\mathrm dt}= k(T_0-T).$$ To platí pro ohřev (teplota okolí je vyšší a teplota tělesa roste). Analogicky můžeme naformulovat model $$\frac{\mathrm dT}{\mathrm dt}= -k(T-T_0)$$ pro ochlazování (teplota okolí je nižší, těleso se ochlazuje a má zápornou derivaci podle času).
>
> Tento model se naučíme časem vyřešit. Pro složitější děje bude ve většině případů modelování vývoje probíhat na počítači. K dispozici je celá řada nástrojů, kde si může zájemce daný matematický model naskriptovat a spustit, například [Sage](https://sagecell.sagemath.org/?z=eJxlU02L2zAQvRv8HwZySbZJmhYKpeBjT4WlFN-WZdFak0aRPGP0tWv_-o7sZDdtdbKsN-89vRmt4D716E1nFQTTJ6c6hMEz3ONLZEoZJmWZgLuTUxNnRQZ0-1FHaGAHFu5g3e7aw6auVvDTm95EkwUycJrkE-KU96B58KgJ4Xty6DmP0GNkPS41DKQ8d4Tn8F6HrybEdDYQ-Ch7W4RnwFK5lZrBG-uUhl-JfuPuR4pR1VVdtc3XA8haQcTBcVQ31vHE8tdhEGRsZpjgJtWpiFaoPYr1ToVUV1rO95_KseyLZevZzsFcUjJ1ZQXyZaawjEfTGaQI4uDQfD787cCyE_zAHcanQpQEsUCSVlmSH9ihRAABNDrLaZZLV21DEX1W7h_9PAaHGm3z8HDYto-Pha8QbSVxsFJS7vucNPYIqWSlopxLrgONkMfM54vDsQR3ZA9GpMArCXR9Y3bzbc5htC6Fuiqhle5H-AAyBu-riIdEkIttXIC6LXNi75YhuSv4FfhROiI-YJILqSy3jqI5gowGGRm_PJLc-xlJzTFgLzoLXWFrRZfWut3c6Mr8xtK7qUfhsYVRYj1LS-DEmjhe7Py3VnOkEqSM1pstGS1-Nf38ErhnIdEYMBoiQUBnArrrwTGRFRgt9NeG7NUwIOn1Q5S2bC4OBz4Xi5ovMJnp0p_SsKW6jBFhtwS9_KqrcOKXtZPH8FQatb4qbKFsz2wIddP6hJvt2BtqDpuZKI_WoyBFjy7PG9-e9x9WM0on&lang=sage&interacts=eJyLjgUAARUAuQ==) je založen na široce rozšířeném jazyce Python, případně [Octave](https://sagecell.sagemath.org/?z=eJwtj81qwzAQhO8CvcNeAlKTFLtQCDY59g18Kz2o1oYK_ayR1wbn6SvZEQjEzsy3I8twh-a97aGeE1gM3oDP5Bcpdq2z3H00fRVX9EwZZhjNTOsWHTyTGb2J7gLeIvwuFiPCRKNjw8A4BSqYoWCemGlWs3uiYq0P2sYrZUzuxV1gynSEeCsp1eoSvB2rZzaZaTWjgz-yidgUR1P0vVp1HEED5Ck4Kfz-r8-XOJlsInKuLgwJy_KIaQMppDjB1xJKvdVAsZA1Zfoo33T3tktLxKAGfW2lqKRBufNeqzw0nMEyvIEvVw3Ntc50LwUmW7m1juLLoKXYgovquwGXHj_6H6tibEk=&lang=octave&interacts=eJyLjgUAARUAuQ==) jako opensource alternativa programu Matlab.

> Poznámka (lineární aproximace, materiálové vztahy). Změna $\Delta x$ v proměnné $x$ vyvolá změnu $\Delta y\approx f'(x) \Delta x$. Proto je možné používat lineární aproximaci funkce $$f(x)\approx f(x_0)+f'(x_0)(x-x_0).  $$       Například naprostá většina materiálových vztahů je takovou aproximací pro $x_0=0$ (relativně malé podněty) a $f(x_0)=0$ (bez podnětu není odezva). Lineární aproximace má poté tvar $$f(x)\approx f'(0)x=kx.$$ Proto jsou zákony jako Fourierův, Fickův nebo Darcyho formulovány ve tvaru přímé úměrnosti. S těmito zákony jste se pravděpodobně seznámili v naukách o materiálu, blíže se jim budeme věnovat později. Podobně je možno chápat Newtonův zákon tepelné výměny z předchozí poznámky jako lineární aproximaci případného obecného vztahu
$$\frac{\mathrm dT}{\mathrm dt}= \Phi(T_0-T), \quad \Phi(0)=0$$
s obecnou a složitě identifikovatelnou funkcí $\Phi$ na tvar
$$\frac{\mathrm dT}{\mathrm dt}= k(T_0-T), \quad k=\Phi'(0),$$
s celkem jednoduše naměřitelnou číselnou konstantou $k$.


> Poznámka (logistický růst populace). Je-li $x(t)$ velikost populace živočichů, je $\frac{\mathrm dx}{\mathrm dt}$ změna této velikosti za jednotku času. Častým modelem reálné situace je modelování pomocí logistické rovnice       $$\frac{\mathrm dx}{\mathrm dt}=r x \left(1-\frac xK\right)$$       kdy předpokládáme, že rychlost růstu je úměrná velikosti populace a volné kapacitě prostředí. Konstanta $K$ je celková kapacita prostředí. 

> Poznámka (pohybová rovnice). Při pohybu po přímce je $x=f(t)$ poloha v čase $t$, rychlost je       $\frac{\mathrm dx}{\mathrm dt}$ a zrychlení je $\frac{\mathrm d^2x}{\mathrm dt^2}$. Podle       Newtonova pohybového zákona platí $$m\frac{\mathrm d^2x}{\mathrm dt^2} =F,$$ kde       $F$ je výsledná síla působící na objekt.




# Funkce dvou proměnných, graf

<div class='obtekat'>

![3d graf funkce dvou proměnných](3D_graf_b.png)

</div>

* Zobrazení $f: \mathbb{R}^2\to \mathbb{R}$ se nazývá funkce dvou proměnných.
* Grafem funkce $f$ je množina uspořádaných trojic  $[x,y,z]$, které splňují $z=f(x,y)$ . Graf kreslíme zpravidla jako body v 3D prostoru.
     * [Nakreslit online.](https://sagecell.sagemath.org/?z=eJxTVkgvSkxTyEpVyM0_ui8vXyG_5PDCI72pJQqJCgVHZ2Ym5WQe3ZdflliikFt5dOHhtbxclbZliUUa6pXqmrxcBTn5JcYpGhVxRrqVcUY6ChoVOrqGOoaaQFYlhKUJAGE3Igs=&lang=sage&interacts=eJyLjgUAARUAuQ==) (Sage),
     * [Nakreslit online.](https://sagecell.sagemath.org/?z=eJxNzc0OwiAQBOA7Ce-wN34CPbTxyM34HqhUm4AQQN19e1tTEy-Tb-YyL1-lIKE4m2tO0CgVGkrMvS-PGyyp5Nph69OVM87as87-EqYjuH2VB42adMAiLWo9WlpDGZBo7Gi-op8w-nOITqAwQLtpdbvntzv52IL6uxi2WaoP-CUxIw==&lang=sage&interacts=eJyLjgUAARUAuQ==) (matplotlib),

<br style="clear:both">

\iffalse 

<div class='obtekat'>

![Kvalita života ve městech souvisí s hospodařením s teplem a tzv. tepelnými ostrovy. Zdroj: pixabay.com](park.jpg)

</div>

\fi


Příkladem skalární funkce dvou prostorových proměnných je teplota v určitém okamžiku na dvourozměrném povrchu. Aparát funkcí dvou proměnných se tedy jistě uplatní při studiu tepelných ostrovů souvisejících s urbanizací a kvalitou života ve městech.

Příkladem skalární funkce dvou proměnných, kdy každá z proměnných má
jiný charakter, je teplota ve stěně budovy. Tato teplota se mění s
časem (studená stěna, na kterou začalo svítit slunce, se ohřívá) a s
polohou (vnější a vnitřní okraj stěny mají teplotu přibližně podle
teploty venku a teploty uvnitř budovy, uvnitř stěny se teplota spojitě
mění).



# Parciální derivace


https://youtu.be/Vw7OF5Fj8G4


Pokud sledujeme například ve stěně měnící se teplotní profil, zajímá nás, jak se teplota v jednotlivých místech stěny mění v čase a jak se teplota mění v řezu stěnou. Zdá se býti rozumné oddělit obě změny. Buď v daném bodě fixovat polohu a sledovat časový vývoj v tomto bodě, nebo v daném čase udělat něco jako teplotní snímek a srovnávat teplotu ve vybraném bodě s okolními teplotami ve stejném čase. To vede k následujícímu přístupu, kdy u funkce více proměnných sledujeme reakci na změnu jedné jediné veličiny. 

> Definice (parciální derivace). Buď $f\colon \mathbb R^2\to\mathbb R$ funkce dvou proměnných,  $x$ a $y$, tj. $f(x,y)$. Výraz
$$\frac{\partial f}{\partial x}:=\lim_{h\to 0}\frac{f(x+h,y)-f(x,y)}h$$ se nazývá *parciální derivace funkce $f$ podle $x$*. Podobně,
$$\frac{\partial f}{\partial y}:=\lim_{h\to 0}\frac{f(x,y+h)-f(x,y)}h$$ je *parciální derivace funkce $f$ podle $y$*.

Podobně můžeme definovat parciální derivaci pro funkce libovolného
konečného počtu proměnných. V těchto parciálních derivacích vlastně
sledujeme, jak reaguje veličina $f$ na změny jenom v jedné
proměnné. Proměnná, přes kterou se nederivuje, má vlastně roli
parametru a nijak se nemění.

> Poznámka (rozšifrování definice derivace).
>
* Výraz z čitatele, tj. $f(x+h,y)-f(x,y)$, je změna veličiny $f$ na intervalu $[x,x+h]$ při konstantní veličině $y$. Často označujeme též $\Delta f$.
* Podíl, tj. $\frac{f(x+h,y)-f(x,y)}h$ je změna veličiny $f$ na intervalu $[x,x+h]$  při konstantní veličině $y$, přičemž tato změna je přepočítaná na jednotku veličiny $x$, tj. v jistém smyslu průměrná rychlost změny vzhledem k $x$ na intervalu $[x,x+h]$. Často označujeme též $\frac{\Delta f}{\Delta x}$.
* Limita v definici derivace stahuje délku intervalu, na kterém počítáme průměrnou rychlost, k nule. Tím se z průměrné rychlosti stane okamžitá rychlost. Parciální derivace je tedy okamžitá rychlost s jakou se mění funkce $f$ při změnách jedné proměnné.

Jednotka derivace $\frac{\partial f}{\partial x}$ je stejná, jako jednotka podílu $\frac {f}x$. Jednotka derivace $\frac{\partial f}{\partial y}$ je stejná, jako jednotka podílu $\frac {f}y$.

Derivace $\frac{\partial f}{\partial x}$ udává, jak se mění veličina
$f$ při změnách veličiny $x$ a předpokladu konstantní veličiny
$y$. Interpretace derivace v nematematických disciplínách je okamžitá
rychlost s jakou veličina $f$ reaguje na změny veličiny $x$.

Pokud sledujeme vývoj a rozložení teploty na dvourozměrné tepelně vodivé desce, je teplota (udávaná například ve stupních Celsia) funkcí tří proměnných: jedna proměnná je čas $t$ a dvě proměnné $x$ a $y$ jsou souřadnice v rovině.  Tedy $T=T(t,x,y).$ Parciální derivace $\frac{\partial T}{\partial t}$ udává je rychle (například ve stupních Celsia za hodinu) roste v daném místě teplota. V různých částech desky může být tato veličina jiná a vždy se vztahuje k danému bodu. Může se měnit i v čase, například deska v prostředí s konstantní teplotou postupně dospěje do stavu se stacionárním rozložením teploty, kdy se teplota v žádném místě ani neroste ani neklesá a parciální derivace podle času je nulová. Derivace $\frac{\partial T}{\partial x}$ udává jak prudce (například ve stupních Celsia na centimetr) roste teplota ve směru osy $x$. 


# Interpretace parciálních derivací - brzdná dráha

https://youtu.be/UE_nkyDe7bw

<div class='obtekat'>

\iffalse 

![Brzdy v autě musí absorbovat kinetickou energii, která je lineární funkcí hmotnosti a kvadratickou funkcí rychlosti. Zdroj: pixabay.com](car.jpg)

\fi

</div>

*Příklad:* Brzdná dráha $L$ (v metrech) auta o hmotnosti $m$ (v kilogramech) brzdícího z rychlosti $v$ (v kilometrech za hodinu) je dána vzorcem
$$L=k m v^2, $$ kde $k= 3.45 \times 10 ^{-6}\,(\mathrm{m}\,\mathrm{hod}^2)/(\mathrm{kg}\,\mathrm{km}^2)$. Pro $m=1100\,\mathrm{kg}$ a $v=100\,\mathrm{km}/\mathrm{hod}$ je brzdná dráha $37.95\,\mathrm{m}$.

* Parciální derivace podle $m$ je $\frac{\partial L}{\partial m}=kv^2$
  a pro zadané hodnoty vychází
  $$\frac{\partial L}{\partial m}=0.0345\, \mathrm{m}/\mathrm{kg}.$$
  Každý kilogram hmotnosti nad $1100\,\mathrm{kg}$ auta jedoucího
  rychlostí $100\,\mathrm{km}/\mathrm{hod}$ prodlouží brzdnou dráhu o
  cca $3.5\,\mathrm{cm}$.
* Parciální derivace podle $v$ je $\frac{\partial L}{\partial v}=2kmv$
  a pro zadané hodnoty vychází
  $$\frac{\partial L}{\partial v}=0.759\,\mathrm{m}/(\mathrm{km}/\mathrm{hod})=7.59\times 10^{-4}\,\mathrm{hod}.$$
  Každý kilometr za hodinu nad $100\,\mathrm{km}/\mathrm{hod}$ u auta
  vážícího $1100\,\mathrm{kg}$ prodlouží brzdnou dráhu o cca
  $76\,\mathrm{cm}$.
* Zjednodušený vzorec pro brzdnou dráhu auta s hmotností blízkou
  $1100\,\mathrm{kg}$ a rychlostí blízkou
  $100\,\mathrm{km}/\mathrm{hod}$ je
$$L\approx 37.95+0.0345(m-1100)+0.759(v-100),$$
kde hmotnost a rychlost se dosazují v kilogramech a kilometrech za hodinu a brzdná
dráha vychází v metrech.
 
\iffalse

[Online výpočet.](https://sagecell.sagemath.org/?z=eJwrSyzSUM9VKFPIVtfk5cpWsFUw1jMx1TI0iNPQNQOK-ABFsrVytcrijHi5cg2APENDAwNerjIwE8QqKMrMK1HQ8NHItc010CmzLTPQ1ESI6qVkpqVplGnik81FkQUABtslGg==&lang=sage&interacts=eJyLjgUAARUAuQ==)

\fi



# Interpretace parciálních derivací - pohyb ještěrky


https://youtu.be/lk-LRBKth3Q


\iffalse

<div class='obtekat'>

![Energie potřebná pro překonání pevné vzdálenosti závisí na hmotnosti jedince a na rychlosti, kterou vyvíjí. Zdroj: pixabay.com](lizard.jpg)

</div>

\fi

Energie $E$ (v kcal), kterou spotřebuje ještěrka o hmotnosti $m$ (v
gramech) na překonání vzdálenosti jednoho kilometru rychlostí $v$ (v
kilometrech za hodinu) se dá odhadnout vzorcem
$$E(m,v)=2.65 m^{0.66} + \frac{3.5 m^{0.75}}{v}.$$
Přímým výpočtem je možné určit
$$\frac{\partial E}{\partial v}=-\frac{3.5 m^{0.75}}{v^2}.$$ Pro $m=400\,\mathrm{g}$ a $v=8\,\mathrm{km}\,\mathrm{h}^{-1}$ dostáváme
$$\frac{\partial E}{\partial v}(400,8)=-4.9\,\mathrm{kcal}\,\mathrm{km}^{-1}\mathrm{h}.$$ Zvýšení rychlosti o kilometr za hodinu vede ke snížení energetického výdeje ještěrky o $4.9\,\mathrm{kcal}$. Podobně, platí
\dm $$\frac{\partial E}{\partial m}={2.65}\times 0.66 {m^{-0.34}} + \frac{3.5\times 0.75 m^{-0.25}}{v}= \frac{1.749}{m^{0.34}} + \frac{2.625}{m^{0.25} v} $$
a pro výše uvažované hodnoty dostáváme
$$\frac{\partial E}{\partial m}(400,8)=
0.30\,\mathrm{kcal}\,\mathrm{g}^{-1}.
$$
Každý gram, který má ještěrka navíc oproti hmotnosti $400$ gramů, zvedne energetický výdej přibližně o $0.30\,\mathrm{kcal}$.

[Online výpočet.](https://sagecell.sagemath.org/?z=eJwrSyzSUM9VKFPX5OVytTXSMzPVyo0z0DMzU9BWMNYzVQDzzE31y3i5Cooy80oUNFw1cm1NDAx0ymwtNDURonopmWlpGmWa-GRzUWQBdPEfhw==&lang=sage&interacts=eJyLjgUAARUAuQ==)

(Zpracováno podle Stewart: Biocalculus)


ww:problems/parcialni_derivace/povrch_tela.pg

# Linearita parciální derivace

Následující poznámka je nenápadná a přirozená, protože je analogií stejného tvrzení pro obyčejné derivace. Má však mimořádnou důležitost, protože udává vlastnost, které se můžeme držet při studiu rovnic obsahujících derivace. Stejné věty zformulujeme i u dalších operací s funkcemi a později se je naučíme využívat.

> Poznámka (linearita parciální derivace). Parciální derivace zachovává součet a násobení konstantou, tj. pro libovolné funkce $f$ a $g$ a konstantu $c$ platí
> $$\frac{\partial (f+g)}{\partial x}=\frac{\partial f}{\partial x}+\frac{\partial g}{\partial x}, \qquad \frac{\partial (cf)}{\partial x}=c\frac{\partial f}{\partial x}$$ a analogicky pro libovolnou jinou proměnnou.


# Rovnice vedení tepla  v 1D

<!-- https://youtu.be/tZDKXyomaJE -->

https://youtu.be/1tbe5YUvoqg

https://youtu.be/ilAaBQNoySI


Studujme vedení tepla v jednorozměrné tyči. Teplota je funkcí dvou
proměnných, polohy a času. Tedy $T=T(t,x).$ Parciální derivace $\frac{\partial T}{\partial t}$ udává je rychle (například ve stupních Celsia za hodinu) roste v daném místě teplota. V různých částech desky může být tato veličina jiná a vždy se vztahuje k danému bodu. Přirozeně se mění i v čase, například  v prostředí s konstantní teplotou postupně systém dospěje do stavu se stacionárním rozložením teploty, kdy se teplota v žádném místě ani neroste ani neklesá a parciální derivace podle času je nulová. Derivace $\frac{\partial T}{\partial x}$ udává jak prudce (například ve stupních Celsia na centimetr) roste teplota ve směru osy $x$. 


> Poznámka. Potřebujeme fyzikální zákony řídící vedení tepla.  Bez nich matematika
model vedení tepla nemá jak naformulovat. Tyto zákony je potřeba matematice dodat "z venku", z aplikované vědy. Tou je v tomto případě fyzika, jindy může být biologie nebo geologie. Jakmile jsou potřebné zákony a případně materiálové vztahy k dispozici, stavé se problém čistě matematickým a fyzika přijde ke slovu při závěrečné interpretaci. Použijeme následující fyzikální fakta. 
>
* Rozdílem teplot je způsoben tok tepla. Velikost toku tepla je úměrná
teplotnímu rozdílu a teplo teče z místa v větší teplotou do místa s menší teplotou.
* Teplota se zvyšuje dodáním tepla. Změna teploty je úměrná dodanému teplu.

\iffalse

<div class='obtekat'>

![Jednorozměrná je například úloha, kde tok v jednom směru je dominantní a toky jiným směrem zanedbatelné. Například okno nebo stěna domu. Zdroj: Cengel, Ghajar: Heat and Mass Transfer.](domek.png)

![Ukázka možného výstupu z rovnice vedení tepla. Vodorovně je poloha v tyči, svisle čas, barva označuje teplotu. Dole je počáteční stav, nulová teplota podél celé tyče. Po ohřátí pravého konce na 100 stupňů a udržování levého konce na nulové teplotě se postupně nastolí rovnováha s lineárním teplotním profilem (teplota rovnoměrně roste doprava). Časový průběh toho, jak se od pravého konce postupně ohřívají jednotlivé části tyče, získáme řešením rovnice vedení tepla. Teplotní profily pro jednotlivé časy získáme na vodorovných řezech v obrázku. Vývoj teploty v pevně sledovaných bodech získáme na svislých řezech.](octave.png)


</div>

\fi

V dalším už nastupuje matematický popis a ve vhodných chvílích vždy
použijeme výše uvedené fyzikální zákony. Mluvíme o teple, ale jako
mechanický model si můžeme představit proudění tekutiny (pro
jednoduchou představu) nebo proudění vlhkosti (pro odvození rovnice
difuze namísto rovnice vedení tepla). Budeme uvažovat libovolné místo materiálu a budeme matematicky vyjadřovat děje, které přispívají ke změně teploty.

* Rychlost s jakou s daném místě roste teplota (v čase) je $$\frac{\partial T}{\partial t}$$ a měříme ji například ve stupních Celsia za minutu. Tato rychlost je úměrná rychlosti s jakou do daného místa dodáváme teplo. Proto v dalším budeme hledat rychlost dodávání tepla a daného místa a poté se sem vrátíme a dáme tuto rychlost do souvislosti s rychlostí růstu teploty.
* Rychlost s jakou s daném místě roste teplota jako funkce polohy je $\frac{\partial T}{\partial x}$ a měříme ji například ve stupních Celsia na centimetr. Tato rychlost musíme vzít záporně, abychom dostali pokles teploty a vynásobit konstantou, která převede spád teploty na tok tepla. Tuto konstantu označíme $k$ (nazývá se součinitel teplné vodivosti a dodá nám ji fyzika, přesněji Fourierův zákon) a tok tepla $q$ ve směru osy $x$ je $$q=-k\frac{\partial T}{\partial x}.$$ To je veličina, která udává, kolik joulů tepla proteče průřezem za jednotku času.
* Pokud do daného místa přitéká teplo stejnou rychlostí jako odtéká, teplota se nemění a dané místo se ani neohřívá ani neochlazuje. Intenzita ochazování je dána bilancí mezi přítokem a odtokem. Můžeme si to představit tak, že z tepla které do daného bodu přiteče, se část "oddělí" a přispěje k navýšení teploty a zbytek teče dál. Pro zjištění, kolik tepla se z toku "oddělí" a způsobí v daném místě navýšení teploty potřebujeme vědět, jak rychle v daném místě tok klesá jako funkce proměnné $x$. Nárůst určíme derivací podle $x$ a pokles z nárůstu uděláme změnou znaménka. Pokles toku tepla je tedy $$-\frac{\partial q}{\partial x}=
-\frac{\partial }{\partial x}\left(-k\frac{\partial T}{\partial x}\right)=
\frac{\partial }{\partial x}\left(k\frac{\partial T}{\partial x}\right).
$$
* Pokles toku vypočtený v předchozím bodě je úměrný rychlosti růstu teploty. Příslušné konstanty úměrnosti dodá fyzika a platí
$$\frac{\partial}{\partial x}\left(k\frac{\partial T}{\partial x}\right)=\rho c\frac{\partial T}{\partial t},$$
kde $c$ je měrná tepelná kapacita a $\rho$ je hustota. (V tomto případě jsou hustota i měrná tepelná kapacita vztaženy ne k jednotce objemu, jak jsme zvyklí, ale k jednotce délky. Například $\rho$ je lineární hustota, tj. v gramech na centimetr).
* Rovnice odvozená v předchozím kroku se nazývá **rovnice vedení tepla** a dokáže modelovat například prostup tepla stěnou domu.

**Shrnutí.** V odvození vidíme, že rovnice vedení tepla je vlastně
bilance toku tepla. Rozdíl o kolik se v daném místě snižuje tok tepla
udává, kolik tepla se v daném místě spotřebovalo. Tato spotřeba tepla
se projeví zvýšením teploty v daném bodě.

ww:problems/parcialni_derivace/rovnice_vedeni_tepla_interpretace.pg 

**Numerické modelování.**
Rovnici je možno použít k simulaci časového vývoje teploty například [takto.](https://sagecell.sagemath.org/?z=eJx1U0tv2zAMvgfIf-CliNw6bRTslELA0nMxDEOxFdgLis00ah0pkyjD9q8fJTtrMWw-WB_f_CjqAj651poKocUarQHCU6Ph5B08Y22dd8MRvXURqK8gwN50rtW2P46ejjQjq-HF2cpUB8gokLbEuU6u0oSVPfu6eD2fXcDDGAiBi6a0BrhK44Z0ttalegiiMRa1T1m825umeBP6R8kH1lC7oAfu_TjGt0k4OOAu2piZ-DhwxkqHHgYTXvQRYci-f_PONT6YAZk8aA7tzFGzj8eAmc_RcbfMkEn1zLY2e_TIzOez-exeyVvaq9X1u9v5TKv3ggpYMdyNUK6S8MRCN-prYt-VTKg7I92cDlrVdFN3P9Ys207dM06IFO1vamJIUq02NW1oz0KXhW5zzziqAb0LwtKVLG13JYukFJtSFkoLkouzjLYu1O5VI8tNoZ5ElwN4Bsv_fGz6guB2AX2LQAcE_BU1GWdByAJMAGNh7_zxJ2wvo6CyK9SSz6VkxMHb5CJSZ2N7ENKsA-fwyFtE3nTz2VZhj-LcPmcDo9YbyxbgbytMaZZyY9isvuZ5wVIu15cjzP_vHMcUMxUY20iFayRerWh5ZQL3jZaMbpr-TQ2e21jlLrXNZXgui9tRldXMUrGhzK29avM8kz6BPMKzLUpQYvvtjtPAqE1uiU4BKkqRUTLlfv89eNZ_5K0nY5_yzHkbY0PhOtV5lOrFOyt4Jad7l0U53uPDW9M08HK68so1fEv6BAdH89kpi-JRlg-yjEXKGw66TvWM5ZmdpoCd9rx9hhoUi8996575dcUdHuL0vvvpPS84RdfoHTZi0SWhnwRKwjAJcVH8Bv3_UjQ=&lang=octave&interacts=eJyLjgUAARUAuQ==) (Pokud si rozkliknete odkaz, neuvidíte rovnici s počátečními podmínkami a příkaz k jejímu vyřešení, ale poměrně dlouhý kód převadějící řešení rovnice vedení tepla na řešení vhodné soustavy lineárních rovnic. V tomto případě se čtyřicetkrát řeší soustava 100 rovnic o 100 neznámých. V inženýrsky zajímavých aplikacích bývají takových rovnic tisíce.)

# Druhá derivace

https://youtu.be/vJVRrik3EAw

Druhá derivace je derivace první derivace. U funkce dvou proměnných připadají v úvahu čtyři kombinace. Buď derivujeme pokaždé podle stejné proměnné, tj. 
  $$
\frac{\partial^2 f}{\partial x^2}:=\frac{\partial}{\partial x}\frac{\partial f}{\partial x},\quad 
\frac{\partial^2 f}{\partial y^2}:=\frac{\partial}{\partial y}\frac{\partial f}{\partial y},
$$
nebo pokaždé podle jiné proměnné. Tady existují teoreticky dvě možnosti
$$\frac{\partial }{\partial x}\frac{\partial f}{\partial y},
\frac{\partial}{\partial y}\frac{\partial f}{\partial x}$$
Poději si ukážeme, že tyto dvě možnosti jsou v praxi zpravidla vždy totožné.

Je-li tepelná vodivost $k$ v rovnici vedení tepla 
$$\rho c\frac{\partial T}{\partial t} = \frac{\partial}{\partial x}\left(k\frac{\partial T}{\partial x}\right)$$
konstantní, redukuje se rovnice na rovnici
$$\rho c\frac{\partial T}{\partial t} = k \frac{\partial^2 T}{\partial x^2},$$
ve které figuruje druhá derivace podle polohy.

# Numerická aproximace derivací: konečné diference 

Instrukce: Z podkapitoly věnované numerickým aproximacím si odneste hlavně vzorce pro aproximaci parciálních derivací. Seznamte se s jejich použitím a s metodou, jak je možno přepsat rovnici obsahující paricální derivace neznámé funkce na soustavu lineárních rovnic. Dle svého zájmu zběžně či důkladněji. Zdůvodnění proč tyto aproximační vzorce fungují a jak jsou odvozeny také přispěje k lepšímu pochopení, ale není zcela nezbytné a seznamte se s ním pdle hloubky svého zájmu.


https://youtu.be/iGohx4i95FI


## Dopředná diference

Základním přístupem při numerickém odhadu derivace je vynechání limitního přechodu v definici derivace. Pro funkci jedné proměnné a její derivaci
$$\frac{\mathrm df}{\mathrm dx}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$
tedy dostáváme
 $$\frac{\mathrm df}{\mathrm dx}\approx\frac{f(x+h)-f(x)}{h}.$$ Okamžitá rychlost je nahrazena
průměrnou rychlostí na intervalu $(x,x+h).$ Tento podíl se nazývá
*dopředná poměrná diference* nebo zkráceně *dopředná diference*. Pokud
 použijeme tento postup pro parciální derivace, dostáváme
 $$\frac{\partial f}{\partial x}\approx\frac{f(x+\Delta x,y)-f(x,y)}{\Delta x}$$
 a
  $$\frac{\partial f}{\partial y}\approx\frac{f(x,y+\Delta y)-f(x,y)}{\Delta y}$$


## Centrální diference

> Poznámka (Taylorův polynom). V diferenciálním počtu funkcí jedné proměnné se zabýváme otázkou hledání nejlepší polynomiální aproximace nějaké funkce. Odpovědí je [Taylorův polynom](http://user.mendelu.cz/marik/mtk/mat-slidy/derivace_II/#taylor%C5%AFv-polynom-a-polynomi%C3%A1ln%C3%AD-aproximace-v-1d) jako nejlepší polynomiální aproximace funkce. S jeho využitím platí $$f(x+h)=f(x)+\frac {\mathrm df(x)}{\mathrm dx}h+\frac{1}{2!} \frac {\mathrm d^2f(x)}{\mathrm dx^2} h^2+O(h^3),$$ kde $O(h^3)$ je funkce, která v okolí nuly konverguje k nule alespoň tak rychle, jako konstantní násobek funkce $h^3$.

Přesnější aproximace derivace vychází z Taylorova polynomu druhého řádu napsaného pro $f(x+h)$ a $f(x-h)$, tj. ze vztahů
$$\begin{aligned}
f(x+h)&\approx f(x)+f'(x)h+\frac 12 f''(x)h^2,\\
f(x-h)&\approx f(x)-f'(x)h+\frac 12 f''(x)h^2.
\end{aligned}$$
Pokud tyto vztahy sečteme a odečteme, dostaneme 
$$\begin{aligned}
f(x+h)+f(x-h)&\approx2f(x)+ f''(x)h^2,\\
f(x+h)-f(x-h)&\approx2f'(x)h.
\end{aligned}$$
Odsud dostáváme aproximace první a druhé derivace
$$ f'(x)=\frac{\mathrm d f}{\mathrm dx}\approx  \frac{f(x+h)-f(x-h)}{2h}  $$
a
$$ f''(x)=\frac{\mathrm d^2f}{\mathrm dx^2}\approx  \frac{f(x-h)-2f(x)+f(x+h)}{h^2}.  $$
Analogicky pro parciální derivaci podle $x$
$$ \frac{\partial f}{\partial x}\approx  \frac{f(x+h,y)-f(x-h,y)}{2h}  $$
a
$$ \frac{\partial^2f}{\partial x^2}\approx  \frac{f(x-h,y)-2f(x,y)+f(x+h,y)}{h^2}.  $$
Tato aproximace první derivace se nazývá *centrální diference* a je přesnější, než dopředná diference, protože je založena na přesnější aproximaci funkce $f$. Používá totiž polynom druhého stupně, kdežto dopředná diference je založena pouze na lineární aproximaci.

Uvedené závěry shrneme do následující věty, kterou vyslovíme pro parciální derivaci podle $x$ i $y$. Aproximace uvedeme ve tvaru, ze kterého je možno současně vidět i chybu při použití dané aproximace. Dva vzorce pro každou parciální derivaci prvního řádu a jeden vzorec pro parciální derivaci druhého řádu.

> Věta (aproximace parciálních derivací pomocí konečných diferencí).
> Platí následující aproximace derivace podle $x$.
> $$\begin{aligned} \frac{\partial f}{\partial x}&=  \frac{f(x+h,y)-f(x,y)}{h}+O(h) \\ \frac{\partial f}{\partial x}&=  \frac{f(x+h,y)-f(x-h,y)}{2h}+O(h^2)\\\frac{\partial^2 f}{\partial x^2}&=  \frac{f(x-h,y)-2f(x,y)+f(x+h,y)}{h^2}+O(h^2)\end{aligned}$$
> Platí následující aproximace derivace podle $y$.
> $$\begin{aligned} \frac{\partial f}{\partial y}&=  \frac{f(x,y+h)-f(x,y)}{h}+O(h) \\ \frac{\partial f}{\partial y}&=  \frac{f(x,y+h)-f(x,y-h)}{2h}+O(h^2)\\\frac{\partial^2 f}{\partial y^2}&=  \frac{f(x,y-h)-2f(x,y)+f(x,y+h)}{h^2}+O(h^2)\end{aligned}$$	
>

ww:problems/parcialni_derivace/centralni_diference.pg

## Diskerizace diferenciálních rovnic pomocí konečných diferencí

Rovnice obsahující parciální derivace jsou přirozeným jazykem, kterým modelujeme fyzikální děje. To jsme viděli na rovnici vedení tepla výše a setkáme se s tím i dále. Bohužel tyto rovnice umíme ručně vyřešit jenom v poměrně speciálních případech a i v těchto případech to není snadná práce. Proto v inženýrské praxi dáváme přednost numerickému řešení rovnice. To je založeno na numerické aproximace derivací a převádí řešení rovnic s parciálními derivacemi na řešení lineárních rovnic. Možnosti si naznačíme v následující poznámce, která je čistě informativní a není toho typu, že byste měli umět výpočty v ní uvedené reprodukovat. Je však důležitá pro pochopení, co nám z rovnic vlastně může vyplývat a jeké jsou zhruba požadavky na výpočetní prostředky..

> Poznámka (explicitní metoda řešení rovnice vedení tepla).
> Po převedení derivací z rovnice vedení tepla $$\rho c\frac{\partial T}{\partial t}=k \frac{\partial ^2 T}{\partial x^2}$$ bychom dostali
> $$\rho c\frac{T(x,t+\Delta t)-T(x,t)}{\Delta t}= k\frac{T(x-\Delta x,t)-2T(x,t)+T(x+\Delta x,t)}{\Delta x^2},$$
kde $\Delta x$ a $\Delta t$ jsou intervaly oddělující body a časy, ve kterých aproximujeme teplotu. Odsud
> $$T(x,t+\Delta t)=T(x,t)+\frac{k\Delta t}{\rho c (\Delta x)^2}\Bigl[T(x-\Delta x,t)-2T(x,t)+T(x+\Delta x,t)\Bigr]$$ a teplotu $T(x,t+\Delta t)$ v následujícím časovém okamžiku v libovolném bodě $x$ dokážeme vypočítat ze současné teploty v tomto bodě a z teploty v sousedních bodech $x+\Delta x$ a $x-\Delta x$. Toto je vzorec pro takzvanou explicitní metodu řešení rovnice vedení tepla a tuto metodu je snadné implementovat [programovým kódem](https://sagecell.sagemath.org/?z=eJyVVUGO4zYQvBvwH_pijOzR7NoD5DKGf7DIIRgsAgTJghY5a1oUKUikIOlPeUU-lmqKsjUzhyA-WKJEVldXV7c29JvrrC4UdUoqq8mr2giqG0dXJa1r3FipxrpAfiiopTfdu07YoZp2Oi9wZwWVzha6uFC8a72wHli1K4RXhZ33uvBlvdrQ63SQWgRlWE2IYtzI1846jqcoM9oq0TBK49602S6O3h7ioiRJ14oR3KvpfMeLiyOw6ELMpAkjEAvRDjTqthSVojHu_Zh3jPGrHhWSJ4Gjva4E9jSqVTGfyoEtMkRSA7KV-k01CpmT6mujC83UKuWdhGBPk4IyFBfBEumqNqpS1otC5ySMIqvA8ayNxbp2ZZB4AgAQdd1AZeNKpOajhIoqYYb1CgQjR8HZYXNcr1ff6ESHI02_DUllSsHSqvXKx1frle1x88v-mLagNsrTGfRSEXIoQaVXDSd2DhJUeZNG_FS-ABAfQSaUGYSJMgp4I57kON--2v44bWmQAmyUEqKsGyVyt3hKsoNMrQstdDqze5jOFhAc5ct-v-eUNks9ctIWFDth4MWrKIdqptqRFFZVDKGoNUrCB55gXjsk-lCPlr93wFSFVtN58PRB8pyu2gq8B66Z6jMXjYUPYDoq5JhZ_3jIbf942B5nfA2DaWH0yB6CECBjVY4IUWc1Uw-lEfKmcizy648OZeCWONF-B7-12R18Azel8t9bDOpdHOzmF4czZeWWy58KNrH6r8MoT8txbzDHhWTLlGL-4HV4icw-H9lQQFtzpPR47ko-mZz8fZhMhIYrhtKENp9MSKFy421ysL3QdmWjPPd5LLKIF1BPDuIsuiGM2sem7xLwTdUNMJA7rBGuSKKayg_LOEyEUZdxODGvN9fQ9YSs_D3v2MreaO4R2GW42T2aKomWHban_b0LeSaiurIZw5XrbJfDEWTTAC0u7zC4ZqdUsf-F8cHeS6NHS9t__p7FmMTxAIyHOGF9ekYZP529gcomXMQPqRrdsZtPlN1tplH9p-fd4sH2cbF4Omy39JVk_9fzlNRisjIs_hPsLdoshn7nKl4-fmSyI-mPn3hvZmWiFyZLp3ZP5Y6xIHYSP4U4pcj3KkapMAWh_AzJfUv40GB6zW06f-AiWsiumAUv4P4JbW4IZlW7Uapry90BY8OY00iZON3aY36FXezdMiSX_vH7IX89_Al9KtVefjZaZvsX2aOIO9nnuPUw8E76LWZ_4YxrKlGjy9HidVxm8XzO83a9ai9Cavtzmq51OnAWDT4f2huVPXwfOncF63BWl3C3UfxyPACiN-KsTPbQ82JIC_-w_ReYO7Kb&lang=octave&interacts=eJyLjgUAARUAuQ==). Dokonce, pokud teploty v čase $t$ uspořádáme do sloupcového vektoru $\vec T(t)$, je možno předchozí vztah zapsat pro všechny body současně jedinou maticovou rovnicí $$\vec T(t+\Delta t)=\vec T(t)+\frac{k \Delta t}{\rho c (\Delta x)^2} A \vec T(t),$$ kde $A$ je matice, která má v hlavní diagonále čísla $-2$, podél diagonály má čísla $1$ a jinak nuly s výjimkou prvního a posledního řádku, které jsou nulové. Viz [výsledný kód](https://sagecell.sagemath.org/?z=eJyFVMFu2zgQvRvwP8zFsJworR1gLwn2kHvRw8IIFii6AC2OY1oUKUgUYekf9gMWe9oP2E_YvbT5r76hZCcpCtRBbFEk37x582YW9JuPzhRMkTU7Q4Frq6huPB1ZO9_4oeLG-Y5CX1BLe3PyUbm-Gk_6oPDkFJXeFaY4UHpqg3IBWLUvVODCnc_67t18tqDteJFaBBVYQ4hi_SC_0XmJx5RZ41g1gtL4vbGrV1cvL_HDmrRv1QDu1Xg_yuLgCSxilzJpugGIhWp7GkxbqoppSGe_zzvF-GgGRvKkcPVkKoUzDbec8qk82CJDJNUjW2323DAyJz7V1hRGqFUcvIZgN6OCuisOSiQyVW25YhdUYXJSlskxOO6MdVjXvuw03gAARH3sqWx8KbmFpCFTpWw_n8nfguSfPipJETewktcf6Ffa3NP4WZBmWyrRl2XTnbD7y_p-2kRpONAO7KYa5BCCysCN5LXrNJjKIYPoU_U6gIQEMqKcQYSnoIA2ImmJ8-G9O92PRxokABed88nioJG6w1vSESq1vmsh007MI3RWgJAo79brtSSzeC1HTsaBYlQWVjyqcqjOVCNp5bgSCKbWsoYNAsG7rh_pz2f0-vMGlqquNbTrw_dy53Q0TmEfqHYszrliomkHngMjw8yF603uTteb1f0Z38BdRlkziIEgA6g4zhEhqcxn4l1plb5onAq8Bez6CiZrsxfQBSw0lfulr6DZwcNjISfXWY8KTjAUW8BLcgjhxH6pQYGdsdMrMcpUxZ8jT30uNy6dnrIHu81d4ge87eSJCP9IKwuinHrAXvCAMGHIPt3c5pt8lExSu9msPo_JxT5E3wiFSgUzKkYGQimx7wNO360uar-V-qWksU8qqDQf0N0YAo3SMOeE-SBIyP9nWG-RvNjph2CpF1MrPlpI6L78S_HLf7X_-ifaQhEQnv9neYui16r6-nc4t-reN3QEh9s7tNQlapoXwZqYKlf2l6bCrphiS9ekw_tMn_64XdEVZQ_42i5XyyThqBYYxwFKFiDeDSYqtJkqG3FYo1xbozYFbAh5gx9EZlV0RzFim9JDS1SYBCV6lqtxSqV8xVuwid9Jifade8KlVKPW-q5O2-OtPrHtsuP1j9wBSQYexzf4DZqPaLzYlxiwNg0yVAcAF2Efz1sQ8fkvfv5HniYNP_2-ybebz0CvuD08NUZn6zt9QswrfcrxGCDulQ6r-_ms8NY3laph6jCf1WmZpfu5TJz5rD0obdzTOF_q6cJONfNZMMFytnzsoz-Cd7fjQ_fSZml2LgFxsmrHNlueZNFPi7BcfQPOnGh8&lang=octave&interacts=eJyLjgUAARUAuQ==), kde je jenom jeden cyklus pro posun v čase a namísto cyklu přes všechny body v tyči je zde maticové násobení. 
>
>
> Ještě existuje implicitní metoda založená na zpětné diferenci v čase namísto dopředné, tj. 
> $$\frac{\partial T(x,t)}{\partial t}=\frac{T(x,t)-T(x,t-\Delta t)}{\Delta t}$$ a odsud $$T(x,t) = T(x,t-\Delta t) +\frac{k\Delta t}{\rho c (\Delta x)^2}\Bigl[T(x-\Delta x,t)-2T(x,t)+T(x+\Delta x,t)\Bigr].$$ Toto vztah umožňující výpočet teplot v čase $t$ z teplot v čase $t-\Delta t$. Bohužel však v každém tomto vztahu figurují tři teploty v čase $t$, které ještě neznáme. Úloha vede na řešení soustavy lineárních rovnic, kterých je stejně jako je uvažovaný počet bodů v tyči, tj. v prakticky využitelných úlohách počty začínají řádově stovkami či tisíci a omezeny jsou jenom pamětí počítačů. Každá rovnice v soustavě má sice jenom tři neznámé, ale jako celek je postup komplikovanější na naprogramování i na výpočet. Přesto se ukazuje jako výhodnější, protože je stabilnější a dovoluje řešení počítat po větších časových skocích, než metoda předchozí. Programová relizace je založena na řešení rovnice a v programech Octave nebo Matlab může vypadat [následovně.](https://sagecell.sagemath.org/?z=eJx1U01v2zAMvQfIf-CliNw6bVTslELA0nMxDEOxFWi3QbGZRq0jZRJl2P71o2RnLYbNB-vxm4-izuCLa62pEFqs0RogPDYajt7BC9bWeTcc0FsXgfoKAuxM51pt-8Po6Ugzshpena1MtYeMAmlLnOvoKk1Y2ZOvi5fz2Rncj4EQuGhKa4CrNG5IZ2tdqocgGmNR-5TFu51pinehf5R8YA21C3rg3g9jfJuEvQPuoo2ZiY8DZ6x06GEw4VUfEIbs-zfvXOOTGZDJg-bQzhw0-3gMmPkcHHfLDJlUz2xrs0OPzHw-m8_ulLyhnVpdfriZz7T6KKiAFcPtCOUqCc8sdKO-JvZdyYS6E9LNca9VTVd19-OaZdupO8YJkaLdVU0MSarVuqY17VjostCt7xhHNaB3QVi6kKXtLmSRlGJdykJpQXJxktHWhdq-aWS5LtSz6HIAz2D5n49N3xDcNqBvEWiPgL-iJuMsCFmACWAs7Jw__ITNeRRUdoVa8rmUjDh4k1xE6mxsD0KadeAcHnmLyJtuPtso7FGc2udsYNT12rIF-NsIU5qlXBs2q8c8L1jK5fX5CPP_O8cxxUwFxjZS4RqJVytaXpnAfaMlo5umf1eD5zZWuU1tcxmey-JmVGU1s1RsKHNrb9o8z6RPII_wZIsSlNg8Pd1yHhjVyS_xKUBFKTJKptzwvyfP-s-89mTscx46r2NsKFymQg9SvXpnBe_kdPGyKMeLvH9vmiZeTndeuYavSR9h72g-O2ZRPMjyXpaxSHnDXtepnrE8tOMUsNWe189Qg2LxtW_dCz-vuMV9nB54Pz3oBafoGr3FRiy6JPSTQEkYJiEuit9lQlKQ&lang=octave&interacts=eJyLjgUAARUAuQ==) Tento přístup se nazývá [implicitní metoda řešení](https://en.wikipedia.org/wiki/Finite_difference_method#Example:_The_heat_equation). 


<!--

% Rovnice vedeni tepla pro jednorozmernou tyc s fixovanymi teplotami na koncich a konstantni pocatecni teplotou.
% Teplota se v tyci rozlozi rovnomerne (linearni profil).
% Teplotni profil pred dosazenim rovnovazenho stavu pro ruzne casy ziskame z rovnice vedeni tepla.
% Nize je aproximace reseni pomoci konecnych diferenci explicitni metodou - jednoducha na implementaci, ale nestabilni, pokud neni casovy krok dostatecne maly


% 
%  Nastaveni
%

L = 1;       % delka tyce

nx = 50;     % pocet bodu v tyci, ve kterych budeme pocitat teplotu
nt = 500;    % pocet kroku v case
dx = L/nx;   % prostorovy krok (vzdalenost dvou sousednbich bodu)
dt = .0001;  % casovy krok, interval s jakzm budeme v danem bode sledovat zmeny teplo
             % casovy krok musi byt dostatecne maly, jinak model neni stabilni

u = zeros(nt+1,nx+1);      % inicializace promenne, do ktere budeme ukladat teploty

T = 0*ones(1,nx+1);  % nastaveni pocatecnich hodnot, nulove teploty vsude krome na nakonci
T(end) = 100;      % nastaveni pocatecnich hodnot, teplota 100 na konci

u(1,1:nx+1) = T;    % vychozi stav

A = toeplitz([-2,1,zeros(1,nx-1)]);  % vytvoreni matice pro iterace
A(1,:) = zeros(1,nx+1);              % vynulovani prvniho radku matice A
A(end,:) = zeros(1,nx+1);            % vynulovani posledniho radku matice A


%
%  Vlastní výpočet a uložení do paměti
%

for j = 2:nt        % jednotlive kroky v case
   T = T + dt/(dx^2) * (A * T')';  % iteracni vzorec pouziva dvakrat transpozice, protoze pracujeme s radkovym vektorem, ale maticove nasobeni funguje pro sloupcove vektory
   u(j+1,1:nx+1) = T;    % ulozeni pro pozdejsi vykresleni
end
 

%
% Vykreslení řešení
%

[X1,T1] = meshgrid(0:dx:nx*dx,0:dt:nt*dt);
colormap hot
pcolor(X1,T1,u)

shading interp
colorbar
title('Vyvoj prubehu teploty v tyci')
xlabel('x')
ylabel('t')

-->


<!--

% Rovnice vedeni tepla pro jednorozmernou tyc s fixovanymi teplotami na koncich a konstantni pocatecni teplotou.
% Teplota se v tyci rozlozi rovnomerne (linearni profil).
% Teplotni profil pred dosazenim rovnovazenho stavu pro ruzne casy ziskame z rovnice vedeni tepla.
% Nize je aproximace reseni pomoci konecnych diferenci explicitni metodou - jednoducha na implementaci, ale nestabilni, pokud neni casovy krok dostatecne maly


% 
%  Nastaveni
%

L = 1;       % delka tyce

nx = 50;     % pocet bodu v tyci, ve kterych budeme pocitat teplotu
nt = 500;    % pocet kroku v case
dx = L/nx;   % prostorovy krok (vzdalenost dvou sousednbich bodu)
dt = .0001;  % casovy krok, interval s jakzm budeme v danem bode sledovat zmeny teplo
             % casovy krok musi byt dostatecne maly, jinak model neni stabilni

u = zeros(nt+1,nx+1);      % inicializace promenne, do ktere budeme ukladat teploty

T = 0*ones(1,nx+1);  % nastaveni pocatecnich hodnot, nulove teploty vsude krome na nakonci
T(end) = 100;      % nastaveni pocatecnich hodnot, teplota 100 na konci

u(1,1:nx+1) = T;    % vychozi stav

A = toeplitz([-2,1,zeros(1,nx-1)]);  % vytvoreni matice pro iterace
A(1,:) = zeros(1,nx+1);              % vynulovani prvniho radku matice A
A(end,:) = zeros(1,nx+1);            % vynulovani posledniho radku matice A


%
%  Vlastní výpočet a uložení do paměti
%

for j = 2:nt        % jednotlive kroky v case
   T = T + dt/(dx^2) * (A * T')';  % iteracni vzorec pouziva dvakrat transpozice, protoze pracujeme s radkovym vektorem, ale maticove nasobeni funguje pro sloupcove vektory
   u(j+1,1:nx+1) = T;    % ulozeni pro pozdejsi vykresleni
end
 

%
% Vykreslení řešení
%

[X1,T1] = meshgrid(0:dx:nx*dx,0:dt:nt*dt);
colormap hot
pcolor(X1,T1,u)

shading interp
colorbar
title('Vyvoj prubehu teploty v tyci')
xlabel('x')
ylabel('t')

-->

# Vzdálenost a pojmy s ní související

Instrukce: V podkapitole věnované popisu bodů, množin a jejich vlastností v euklidovském prostoru se ujistíme, že dokážeme dát přesný obsah tak běžným pojmům jako vzdálenost nebo hranice množiny. Protože tyto pojmy nejdou nijak proti intuici, není nutné se učit jednotlivé definice. Jenom si rámcově odneste přehled, jak jsou tyto pojmy definovány a jaké pojmy vlastně používáme. V případě nutnosti se k těmto definicím můýžete kdykoliv vrátit. 

https://youtu.be/owfHzLBonRA

\iffalse 

<div class='obtekat'>

![Názvosloví a terminologie jsou nejnudnější pasáže. Prolétneme pro rychlé seznámení a můžeme se se vrátit, kdykoliv bude potřeba. Zdroj: pixabay.com, chudamay](bored_cat.jpg)

</div>

\fi


V dalším budeme pracovat s pojmy jako množina a její hranice, množina
obsahující hranici, množina neobsahující hranici, spojitá funkce
apod. Ač v technicky nejvýznamnějších aplikacích často můžeme tyto
pojmy chápat intuitivně, historie ukázala, že přesná formální definice
je nezbytná.

V dalším nastane jedna z nejnebezpečnějších situací v matematice, kdy přesně definovanému pojmu dáme název, který lidé znají z prostého života. Například hranice, oblast, spojitost, uzávěr, okolí, ... Podrobný rozbor ukazuje, že tyto definice jsou v jednoduchých případech v souladu s intuicí. 


## Euklidovský metrický prostor


> Definice (metrický prostor, metrika).
  Množina $\mathbb{E}^3$ prvků z $\mathbb{R}^3$ s metrikou $\rho$ definovanou pro
  $A=(a_x,a_y,a_z)\in\mathbb{R}^3$ a $B=(b_x, b_y, b_z)\in\mathbb{R}^3$
  vztahem
  $$
    \rho(A,B)=\sqrt{(a_x-b_x)^2+(a_y-b_y)^2+(a_z-b_z)^2}
  $$
  se nazývá *Euklidovský metrický prostor*. Prvky prostoru
  $\mathbb{E}^3$ budeme nazývat *body*. Funkce $\rho$ se nazývá
  *Euklidovská metrika*. Číslo $\rho(A,B)$ se nazývá
  *Euklidovská vzdálenost* bodů $A$, $B$.

Analogicky je možno definovat metriku v prostoru libovolné konečné dimenze.

> Definice (okolí).
  Buď $A\in \mathbb{E}^n$ bod z $\mathbb{E}^n$ a $\varepsilon>0$ kladné reálné
  číslo. *Epsilonovým okolím bodu $X$* rozumíme množinu
  označenou $O_\varepsilon(A)$ skládající se z bodů, jejichž vzdálenost od
  bodu $A$ je menší než $\varepsilon$, tj.
$$
    O_\varepsilon(A)=\{X\in\mathbb{E}^n:\rho(A,X)<\varepsilon\}.
$$
  *Ryzím epsilonovým okolím bodu $A$* rozumíme množinu
  $\overline O_\varepsilon(A)$ definovanou
  $$
    \overline O_\varepsilon(A)=O_\varepsilon(A)\setminus\{A\},
  $$
  tj. $\varepsilon$-okolí bodu $A$, s vyloučením bodu $A$.

## Významné vlastnosti množin v Euklidovském prostoru


V následujících definicích je $X\in\mathbb{E}^n$ bod a $M\subseteq
\mathbb{E}^n$ podmnožina v Euklidovském prostoru $\mathbb{E}^n$ ($n=2$
nebo $3$). Abstraktně je možno s těmito pojmy pracovat i v prostorech
libovolné konečné dimenze.


**Ohraničená množina**:
  Množina $M$ se nazývá *ohraničená*, jestliže leží
  v (dostatečně velkém) okolí nějakého bodu $Y\in\mathbb{E}^n$.



**Vnitřní bod, vnitřek,  otevřená množina**:
  Bod $X$ se nazývá *vnitřním bodem množiny $M$*, jestliže
  $X\in M$ a existuje nějaké okolí $O(X)$ bodu $X$ ležící celé
  v množině $M$, tj. $O(X)\subseteq M$. Množina všech vnitřních
  bodů množiny $M$ se nazývá \textit{vnitřek množiny $M$} a
  označuje $M^o$. Je-li množina $M$ totožná se svým vnitřkem, tj.
  je-li každý bod množiny $M$ vnitřní, říkáme, že množina $M$ je
  *otevřená*.


**Hraniční bod,  hranice**:
  Bod $X$ se nazývá *hraničním bodem množiny $M$*, jestliže
  každé okolí bodu $X$ obsahuje alespoň jeden bod ležící v množině $M$
  a současně alespoň jeden bod neležící v množině $M$. Množina všech
  hraničních bodů množiny $M$ se nazývá *hranice množiny $M$*
  a označuje $\partial M$.


**Uzávěr,  uzavřená množina**:
  *Uzávěrem množiny $M$* rozumíme množinu $\overline M$
  definovanou jako sjednocení vnitřku a hranice množiny $M$,
  tj. $\overline M=M^o\cup\partial M$. Je-li množina totožná se svým
  uzávěrem (tj. obsahuje-li všechny své hraniční body), nazývá se
  *uzavřená*.

**Souvislá množina**:
  Množina $M$ se nazývá souvislá, jestliže každé dva body, ležící
  v množině $M$ lze spojit lomenou čarou, ležící v $M$.

**Oblast, uzavřená oblast,  kompaktní množina**:
   Otevřená souvislá množina se nazývá *oblast*. Uzavřená
  souvislá množina se nazývá *uzavřená oblast*. Uzavřená
    ohraničená  množina se nazývá *kompaktní*.


# Spojitost funkce

\iffalse 

<div class='obtekat'>

![Spojitost dokáže potrápit i u funkce jedné proměnné. Například Weistrassova funkce je spojitá, ale její graf není možné nakreslit ani jedním tahem, ani nijak jinak. To rozhodně jde proti intuitivnímu chápání spojitosti ze střední školy či běžného života. Zdroj: pixabay.com](epmty.jpg)

</div>

\fi



**Spojitost skalární funkce**:
  Nechť $f:\mathbb{R}^n\to \mathbb{R}$ je skalární funkce $n$ proměnných definovaná
  v nějakém okolí bodu $A\in\mathbb{R}^n$. Řekneme, že funkce $f$ je v bodě
  $A$ *spojitá*, pokud pro každé okolí $O(f(A))$ bodu $f(A)$ existuje
  okolí $\overline O(A)$ bodu $A$ takové, že obrazy všech bodů
  z tohoto okolí bodu $A$ leží v okolí bodu $O(f(A))$, tj.  pro
  všechna $X\in \overline O(A)$ platí $f(X)\in O(f(A))$.

**Spojitost vektorové funkce**:
  Nechť $f:\mathbb{R}^n\to \mathbb{R}^m$ je vektorová funkce $n$ proměnných definovaná
  v nějakém okolí bodu $A\in\mathbb{R}^n$. Řekneme, že funkce $f$ je v bodě
  $A$ *spojitá*, jestliže je v tomto bodě spojitá každá její komponenta.


**Elementární funkce**: 
  Všechny mnohočleny, goniometrické, cyklometrické, exponenciální a
  logaritmické funkce a obecná mocnina se nazývají *základní
    elementární funkce* 
  Všechny funkce, které ze základních
  elementárních funkcí získáme konečným počtem operací sčítání,
  odečítání, násobení, dělení a skládání těchto funkcí navzájem se
  nazývají *elementární funkce*.

\iffalse

Elementární funkce jsou tedy všechny funkce, které umíme v konečném
  tvaru vyjádřit explicitním vzorcem za použití funkcí známých ze
  střední školy a cyklometrických funkcí.

Elementární neznamená jednoduchý. 
Funkce $$f(x,y)=\frac{x^2+\sin(x^2-y^2)}{\ln(x^2+y^2-1)},\quad g(x,y)=\frac{1}{1+\frac x{1+\frac {y}{x^2}}} $$ jsou elementárními funkcemi ve smyslu výše uvedené definice. Funkce $$h(x,y)=\begin{cases} 1 & x=0 \text{ nebo }y=0\\0 &\text{jinak}\end{cases}$$ není elementární funkce.

Následující věta ukazuje, že u elementárních funkcí je spojitost v
libovolném bodě zaručena již tím, že je funkce v tomto bodě
definována.

\fi

> Věta (spojitost elementárních funkcí). Všechny [elementární funkce](http://cs.wikipedia.org/wiki/Elementární_funkce}) jsou spojité v každém vnitřním bodě svého definičního oboru.




# Schwarzova věta


> Věta (Schwarzova). Jsou-li smíšené derivace spojité na otevřené množině, jsou zde stejné, tj. platí  $$ \frac{\partial }{\partial x}   \frac{\partial f}{\partial y}= \frac{\partial }{\partial y}   \frac{\partial f}{\partial x}.$$


\iffalse 

<div class='obtekat'>

![Smíšené derivace jsou (za určitých nepříliš omezujících podmínek) nerozlišitelná dvojčata. Zdroj: pixabay.com](ducks.jpg)

</div>

\fi

Vzhledem k této větě existují jenom tři druhé parciální derivace. Je tedy bezpečné psát
  $$
\frac{\partial^2 f}{\partial x^2},\quad 
\frac{\partial^2 f}{\partial x \partial y},\quad 
\frac{\partial^2 f}{\partial y^2},
$$
nebo
$$f''_{xx},\quad f''_{xy},\quad f''_{yy}.$$



# Z ptačí perspektivy

\iffalse

<div class='obtekat'>

![Ještě pohled s trochou nadhledu. Zdroj: pixabay.com](../falcon.jpg)

</div>


\fi


* U měnících se veličin běžně udáváme, o kolik se změní za jednotku času nebo o kolik se změní na jednotce délky. Například o kolik vzroste teplota za hodinu. Pomocí parciálních derivací můžeme tyto změny sledovat a popsat jejich okamžité rychlosti. To je nutné pro představu, jak fungují vztahy mezi veličinami.
* Parciální derivace udává okamžitou rychlost s jakou se mění funkce více proměnných při změně vybrané nezávislé proměnné. Tedy změna funkčních hodnot při změně jedné nezávislé proměnné o jednotku a zafixování ostatních proměnných. Tato změna se počítá na nekonečně malém intervalu a jedná se tedy o okamžitou rychlost.
* Příroda funguje tak, že děj v daném okamžiku probíhá rychlostí související s aktuálními hodnotami veličin, které mají na děj vliv. Potřebujeme tedy nástroj pro měření rychlosti. Tím je derivace. V případě, kdy výsledek je ovlivněn více vstupními daty, máme funkci více proměnných a parciální derivace, kdy sledujeme vliv každé vstupní veličiny samostatně.
* Přírodní zákony jsou formulovány buď přibližně, pomocí součinů, podílů a průměrných rychlostí, nebo přesně pomocí derivací a okamžitých rychlostí. Nám jde o detailní popis, tj. o přesnou fomrulaci.
* Kvalitativní představa může být, že teplo teče do studenějšího místa a v místě, kam se dodává teplo, roste teplota. Toto je pouze hrubý model. Pomocí parciálních derivací tento děj umíme namodelovat kvantitativně.
* V praxi často derivace počítáme pro funkce dané tabulkou. V tomto případě používáme numerickou aproximaci derivace. Nejčastěji pomocí centrální diference.

