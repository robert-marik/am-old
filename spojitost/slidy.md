% Spojitost funkcí více proměnných
% Robert Mařík
% jaro 2018


# Euklidovský metrický prostor

\iffalse 

<div class='obtekat'>

![Vzdálenost se dá měřit spoustou způsobů. My použijeme ten, který je známý z běžného života. Ne že by to vedlo k nejjednodušším formulacím, ale je to nejnázornější. Zdroj: pixabay.com](distance.jpg)

</div>

\fi


**Metrický prostor, metrika**:
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

**Okolí**:
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

# Významné vlastnosti množin v Euklidovském prostoru

\iffalse 

<div class='obtekat'>

![Jedna z nejnebezpečnějších situací v matematice nastává, pokud přesně definovanému pojmu dáme název, který lidé znají z prostého života. Například hranice, oblast, spojitost, uzávěr, elementární, okolí, ... Zdroj: pixabay.com](hranice.jpg)

</div>

\fi


V následujících definicích je $X\in\mathbb{E}^n$ bod a $M\subseteq
\mathbb{E}^n$ podmnožina v Euklidovském prostoru $\mathbb{E}^n$ ($n=2$
nebo $3$). Abstraktně je možno s těmtito pojmy pracovat i v prostorech
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

![Spojitost mimo jiné zakazuje funkcím skoky. I ty sebenepatrnější. Ač se skoky řádově třeba v nanometrech zdají bezvýznamné, u pěkných (spojitých) funkcí nepřipustíme ani toto. Zdroj: pixabay.com](jump.jpg)

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

<i><small>Elementární neznamená jednoduchý. 
Funkce $$f(x,y)=\frac{x^2+\sin(x^2-y^2)}{\ln(x^2+y^2-1)},\quad g(x,y)=\frac{1}{1+\frac x{1+\frac {y}{x^2}}} $$ jsou elemenárními funkcemi ve smyslu výše uvedené definice. Funkce $$h(x,y)=\begin{cases} 1 & x=0 \text{ nebo }y=0\\0 &\text{jinak}\end{cases}$$ není elementární funkce.
</small>
</i>

Následující věta ukazuje, že u elementárních funkcí je spojitost v
libovolném bodě zaručena již tím, že je funkce v tomto bodě
definována.

\fi

> **Věta:** Všechny [elementární funkce](http://cs.wikipedia.org/wiki/Elementární_funkce}) jsou spojité v každém vnitřním bodě svého definičního oboru.


