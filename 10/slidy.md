% Autonomní systémy
% Robert Mařík
% 2020

# Opakování

* Maticový součin
* Řešitelnost homogenní soustavy lineárních rovnic
* Vlastní hodnoty a vlastní vektory
* Chování exponenciální funkce $e^{kt}$ v nekonečnu

# Autonnomní systém $X'=AX$

# Autonomní systém $X'=f(X)$

# Autonomní systém v jedné dimenzi

Rovnice $$\frac{\mathrm dy}{\mathrm dx}=f(y)\tag{♣}$$ je autonomní
systém v jedné dimenzi. Je speciálním případem rovnice se separovanými
proměnnými, která je uvedena na dalším slidu a umíme ji řešit
analytickou cestou. Proto se nyní nebudeme zaměřovat na hledání
obecného řešení, ale pokusíme se popsat chování řešení, aniž bychom
tato řešení znali. Pokusíme se s\ co nejmenší námahou říct, jak se
budou řešení chovat.

Všechna konstantní řešení rovnice (♣) jsou nulové body pravé strany. Kromě toho musíme poosudit stabilitu.

> Věta (stabilita konstantních řešení). Jestliže platí $f(y_0)=0$, je
  konstantní funkce $y(x)=y_0$ konstantním řešením rovnice
  $$\frac{\mathrm dy}{\mathrm dx}=f(y).$$ Toto řešení je stabilní
  pokud $f'(y_0)<0$ a nestabilní pokud $f'(y_0)>0$.

Pro grafickou intepretaci je vhodné připomenout, že funkce s kladnou
derivací jsou rostoucí a funkce se zápornou derivací klesající. Pokud
má tedy pravá strana derivaci různou od nuly, poznáme stabilitu z\ monotonie pravé strany.

**Příklad.** Logistická diferenciální rovnice s konstantním lovem
  $h$, tj. rovnice
  $$\frac{\mathrm dy}{\mathrm dt}=ry\left(1-\frac yK\right)-h,$$
  má pro malé $h$ dva stacionární body. Funkce $ry\left(1-\frac
  yK\right)$ je parabola otočená vrcholem
  nahoru a s nulovými body $y=0$ a $y=K$. V prvním stacionárním bodě
  je funkce rostoucí a tento stacionární bod je nestabilní. Ve druhém
  stacionárním bodě je funkce klesající a tento stacionární bod je
  stabilní. Jak se zvyšuje faktor $h$, graf paraboly se posouvá směrem
  dolů a oba stacionární body se posouvají směrem k sobě a k\  vrcholu. Jejich stabilita zůstává neporušena. To znamená, že sice
  pořád existuje stabilní stav, ale se zvyšující se intenzitou lovu se
  tento stacionární stav dostává stále blíže ke stavu nestacionárnímu a
  rovnováha je tedy poněkud křehká. 

# Autonomní systém ve dvou dimenzích

# Vícerozměrné autonomní systémy, kompartmentové modely

