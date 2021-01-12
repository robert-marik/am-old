% Autonomní rovnice a systémy

![Zdroj: vlastní](pokros.jpg)


# Stavebniny vedle čebínského nádraží: model

Hromada sypkého
materiálu má tvar kužele. Úhel u vrcholu je konstantní, daný
mechanickými vlastnostmi materiálu a je nezávislý na
objemu. Předpokládejme, že personál stavebnin přisypává na hromadu
materiál konstantní rychlostí (v jednotkách objemu za jednotku
času). Tato hromada je však v poměrně otevřené krajině a vítr
rozfoukává materiál po okolí. Je rozumné předpokládat, že rozfoukávání (opět v jednotkách objemu za jednotku
času)
se děje rychlostí úměrnou povrchu návětrné strany pláště.

1. Napište rovnici pro derivaci objemu hromady podle času. 
1. Existuje konstantní řešení? Pokud ano, je stabilní nebo nestabilní? Zdůvodněte.
1. Může hromada skončit i při neustálém přisypávání celá rozfoukaná?
1. Mohou pracovníci navršit hromadu do libovolné výšky anebo pro velkou hromadu je již rozfoukávání rychlejší než přisypávání?

<div class=reseni>
Rychlost s jakou se mění objem je $\frac{\mathrm dV}{\mathrm dt}$, rychlost přisypávání označme $R$, povrch návětrné strany $S$.
Podle zadání platí
$$  \frac{\mathrm dV}{\mathrm dt} = R - k_0S.$$
Protože kužel má stále stejný tvar, objem jednoznačně determinuje rozměry, povrch kužele, nebo i povrch poloviny pláště, tj. povrch návětrné strany. Z podobnosti víme, že plochy rostou s druhou mocninnou a objemy se třetí mocninou délkových rozměrů. Proto je zřejmé, že musí platit úměrnost mezi takovými mocninami těchto veličin, pro které jednotky ``pasují'', Existuje tedy konstanta taková, že $$S=k_1V^{\frac 23}.$$ Spojením těchto dvou vztahů dostáváme
$$  \frac{\mathrm dV}{\mathrm dt} = R - k V^{\frac 23},$$
kde $r$ a $k=k_0k_1$ jsou konstanty.

Označme $f(V)=R-kV^{\frac 23}$.
Konstantní řešení je řešením rovnice $f(V)=0$, tj. $$R-kV^{\frac 23}=0.$$ Odsud
$$V_0=\left(\frac{R}{k}\right)^{3/2}.$$ Protože $f$ klesá v bodě $V_0$, je toto řešení stabilní.

Protože $f(0)>0$, malá hromada vždy roste a proto nemůže skončit celá rozfoukaná. Pro malý objem je přisypávání intenzivnější než rozfoukávání.

Protože $f$ je pro velké $V$ záporná, pro velkou hromadu objem ubývá (více se rozfouká než přisype) a hromadu není možné navršit libovolně velkou. 

</div>



![Zdroj: vlastní](trolejbus.jpg)

# Časový rozestup mezi trolejbusy

Uvažujme dva trolejbusy jedoucí za sebou po stejné trati. Označme
$x(t)$ jejich časový odstup. Pokud první trolejbus zastaví na určité
zastávce v čase $t$, druhý trolejbus na tuto zastávku dorazí v čase
$x(t)$. Naším úkolem je zjistit, jak se $x(t)$ mění s\ rostoucím $t$.

Předpokládejme, že **(1)** pokud žádní pasažéři nečekají na druhý vůz, druhý vůz se
  pohybuje rychleji než první vůz a oba vozy se "sjedou", tj. $x(t)$
  klesá konstantní rychlostí, pokud na druhý vůz nečekají žádní pasažéři
**(2)** rychlost druhého vozu klesá (a rozestup roste) s rostoucím počtem pasažérů, kteří
  čekají na zastávce 
**(3)** počet pasažérů kteří čekají na zastávce roste s rostoucím
  intervalem mezi oběma vozy.

Navrhněte model pro rozestup trolejbusů, najděte stacionární řešení a posuďte jeho stabilitu.


<div class=reseni>

Situaci je možno modelovat diferenciální rovnicí
$$ 
  \frac{\mathrm dx}{\mathrm  dt}=\beta x-\alpha,
$$
kde $\alpha$ a $\beta$ jsou kladné reálné konstanty. Tato rovnice má konstantní řešení $x=\frac \alpha\beta$. Toto řešení je nestabilní, protože 
$$\frac{\mathrm d}{\mathrm dx}(\beta x-\alpha)=\beta>0.$$ Žádné jiné
konstantní řešení neexistuje a proto všechna řešení klesají na nulu
nebo neohraničeně rostou.

Vzhledem k nestabilitě stacionárního řešení nemůžeme nechat řidiče
veřejné dopravy jezdit "jak jim to vyjde". Situace by směřovala k
tomu, že cestující budou nejprve dlouho čekat na trolejbus a nakonec
přijede několik trolejbusů těsně za sebou. (Podle knihy P.  Blanchard,
R. L. Devaney, G.  R. Hall: Differential equations, Cengage Learning
(2006), 828 pp.)

</div>


![pixabay.com](kost.jpg)

# Propeptid kolagenu

Kolagen je klíčový protein pojivových tkání. Jeden z kroků při syntéze
kolagenu spočívá v reakci tří molekul propeptidu kolagenu, zkráceně
propeptidu. Tento propeptid se formuje konstantní rychlostí a kromě
toho, že je surovinou pro produkci kolagenu, se ještě rozpadá
rychlostí úměrnou koncentraci. Napište matematický model pro množství
(koncentraci) propeptidu kolagenu.

_Podle Alan Garfinkel, Jane Shevtsov, Yina Guo: Modeling Life_

<div class=reseni>

$$\frac{\mathrm dP}{\mathrm dt}=-k_1 P^3 +k_2-k_3 P$$

</div>


![Jelen a los](moose.jpg)

# Jelen a los

Uvažujme populaci jelenů a losů. Tyto populace spolu soupeří o potravu. \textbf{(1)} Bez konkurence by populace jelena rostla rychlostí $3$ a  populace losa rychlostí $2$ na jeden kus. \textbf{(2)} Vnitrodruhová konkurence se projevuje v obou populacích stejně a je rovna druhé mocnině příslušné velikosti populace. \textbf{(3)} Mezidruhová konkurence je vyjádřena členem rovným součinu velikosti populací a tato konkurence se projeví s koeficientem 0.5 v populaci losa a s koeficientem 1 v populaci jelena.

Sestavte matematický model a otestujte jej numerickým experimentem na stabilitu stacionárních bodů. Poté zdvojnásobte parametry mezidruhové konkurence a sledujte změnu odezvy. 



<div class=reseni>

$$
\begin{aligned}
  \frac{\mathrm dx}{\mathrm dt}&=3x-xy-x^2\\
    \frac{\mathrm dy}{\mathrm dt}&=2y-0.5xy-y^2
\end{aligned}
$$

[Sage](https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=3*x%20-%20x%5E2%20-%20x*y&dydt=2*y%20-%20y%5E2%20-%200.5%20*%20x%20*%20y&x=0,4,20&y=0,3,15&method=rk4&h=0.1&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B0.3,0.28328571428571436%5D,%5B0.20714285714285716,0.6434928229665071%5D,%5B2.664285714285714,2.158851674641148%5D,%5B3.1714285714285713,0.7533014354066987%5D,%5B1.7785714285714285,0.2115789473684213%5D)

</div>

<!--

% \obrazek{les.jpg}

% ## Model konkurence

% Konkurence je častý jev v přírodě. Například v lese si konkurují listnaté a jehličnaté stormy z hlediska prostoru, slunečního světla a vody. Stromy se liší rychlostí růstu, nosnou kapacitou prostředí a tím, jak ovlivňují své konkurenty. Předpokládejte logistický růst v obou konkurujících si populacích, předpokládejte člen vyjadřující zbrždění vlivem konkurenta přímo úměrný velikosti obou populací  a namodelujte čtyři možné východiska modelu ()


% %https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=0.1*x*(1-x/10000)-5*0.00001*x*y&dydt=0.25*y*(1-y/6000)-3*0.00001*x*y&x=0,10000,20&y=0,6000,15&method=rk4&h=0.1&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B4907.407407407408,5229.428571428572%5D,%5B7444.444444444444,3746.6985645933014%5D,%5B8407.407407407407,2633.9712918660284%5D,%5B9259.25925925926,1111.2918660287078%5D,%5B9648.148148148148,423.1578947368416%5D,%5B3240.740740740741,306.0287081339711%5D,%5B1407.4074074074074,935.5980861244016%5D,%5B4611.111111111111,203.5406698564584%5D,%5B5518.518518518518,57.129186602870504%5D
-->

![wikimedia](pustik.jpg)

# Puštík obecný

Puštík obecný se téměř výhradně živí malými hlodavci. Předpokládejme následující vztahy.
\textbf{(1)} Populace hlodavců má porodnost 0.1 na jedince a úmrtnost 0.025 na jedince za jednotku času.
\textbf{(2)} Rychlost s jakou jeden puštík konzumuje hlodavce je úměrná počtu hlodavců s kostantou úměrnosti 0.01.
\textbf{(3)} Porodnost v populaci puštíka je úměrná množství zkonzumované potravy s konstantou úměrnosti 0.05.
\textbf{(4)} Úmrtnost v populaci puštíka je 0.1 na jedince za jednotku času.

Vyjádřete tyto vztahy matematickým modelem.

_Podle Alan Garfinkel, Jane Shevtsov, Yina Guo: Modeling Life. Doslova přeloženo. Porodnost je ve skutečnosti společný efekt zvýšené porodnosti a snižené úmrtnosti v případě, že puštík má přístup k potravě._


<div class=reseni>

$$
\begin{aligned}
  \frac{\mathrm dx}{\mathrm dt}&=0.1 x-0.025x-0.01xy\\
  \frac{\mathrm dy}{\mathrm dt}&=-0.1y+0.05xy  
\end{aligned}
$$

[Sage](https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=0.1*x%20-%200.025*x-0.01*x*y&dydt=-0.1*y+0.05*x*y&x=0,10,20&y=0,40,15&method=rk4&h=0.1&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B0.7894736842105263,10.577142857142857%5D,%5B1.795774647887324,12.09377990430622%5D,%5B0.7394366197183099,22.830622009569378%5D)

</div>


![Kůň Převalského](prevalski.jpg)

# Kůň Převalského

Kůň Převalského je divoký kůň ze střední Asie, jediný druh koně, který nebyl domestikován. V divočině jsou tyto koně loveni vlky. Napište matematický model založený na následujících předpokladech.
\textbf{(1)} Porodnost v populaci koní je  0.15 na jedince. \textbf{(2)} Úmrtnost v populaci koní je  0.01 na jedince.
\textbf{(3)} Vlci se živí i jinou potravou, mají tedy kladnou porodnost. Ta je 0.1 na jedince.
\textbf{(4)} Vlci mají konstantní úmrtnost 0.05 na jedince.
\textbf{(5)} Pravděpodobnost s jakou je kůň uloven vlkem je úměrná počtu vlků s konstantou úměrnosti 0.02.

_Podle Alan Garfinkel, Jane Shevtsov, Yina Guo: Modeling Life_

_Podle Wikipedie kůň Převalského přežil jenom díky péči zoologických zahrad a z rodokmenu je zřejmé, že 70 procent jedinců tohoto druhu má původní předky ze zoologické zahrady v Praze._

<div class=reseni>

$$
\begin{aligned}
  \frac{\mathrm dx}{\mathrm dt}&=0.15 x-0.01x-0.05xy\\
  \frac{\mathrm dy}{\mathrm dt}&=0.1y-0.05y  
\end{aligned}
$$


[Sage](https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=x-x*y&dydt=-y+x*y&x=0,4,20&y=0,3,15&method=rk4&h=0.1&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B0.6714285714285717,0.6442105263157893%5D,%5B1.1571428571428575,0.6002870813397125%5D,%5B0.9857142857142858,1.155933014354067%5D,%5B0.7142857142857143,2.1442105263157893%5D,%5B2.992857142857143,2.01244019138756%5D,%5B2.7,1.382870813397129%5D)

</div>

<!--

% Holling
% https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=x*(1-x/2)-y*%20x/(1+x)&dydt=-0.2*y%20+%200.7%20*%20y%20*%20x/(1+x)&x=0,1.5,15&y=0,2,15&method=rk4&h=0.05&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B0.19553571428571428,0.7085714285714286%5D,%5B0.23839285714285716,0.8731100478468901%5D,%5B0.38571428571428573,0.477799043062201%5D

%
% Jezera
% https://homepages.bluffton.edu/~nesterd/apps/compartmentalanalysis.html?O&S,29,F,80,10;H,0,T,290,100;M,0,T,130,200;R,0,T,325,280;O,0,T,490,230&S,H,S*15/2900;M,H,M*38/1180;H,R,H*68/850;R,O,R*85/116;O,s,O*99/393&The%20compartments%20represent%20levels%20of%20some%20pollutant%20in%20the%20Great%20Lakes.%20%28R%20%3D%20Erie%2C%20because%20E%20is%20not%20an%20allowed%20variable%20name.%29%20The%20model%20assumes%20that%20the%20initial%20concentration%20of%20the%20pollutant%20is%20the%20same%20in%20all%20the%20lakes%2C%20so%20the%20initial%20value%20is%20proportional%20to%20the%20lake%27s%20volume.%20No%20more%20of%20that%20pollutant%20is%20being%20introduced%2C%20and%20pure%20%28rain%29%20water%20flows%20in%20to%20the%20lakes%2C%20with%20the%20resulting%20mixture%20flowing%20from%20each%20lake%20into%20the%20next%2C%20and%20eventually%20to%20the%20ocean.%20From%20Fundamentals%20of%20Differential%20Equations%20%28Nagle%20and%20Saff%2C%201996%29%2C%20page%20317.

-->


# Analýza pomocí vlastních čísel

Autonomní systém
$$
\begin{aligned}
  \frac{\mathrm dx}{\mathrm dt}&= 4x^2y+y^3-5\\
  \frac{\mathrm dy}{\mathrm dt}&= 3xy^2-3y
\end{aligned}
$$
má stacionární bod $(1,1)$. Najděte Jacobiho matici v tomto bodě, vlastní čísla této matice a určete typ stacioárního bodu.

<div class=reseni>

Platí
$$
\begin{aligned}
  \frac{\partial }{\partial x}(4x^2y+y^3-5)&=8xy\\
  \frac{\partial }{\partial y}(4x^2y+y^3-5)&=4x^2+3y^2\\
  \frac{\partial }{\partial x}(3xy^2-3y)&=3y^2\\
  \frac{\partial }{\partial y}(3xy^2-3y)&=6xy-3\\
\end{aligned}
$$
a odsud
$$J(x,y)=
\begin{pmatrix}
  8xy& 4x^2+3y^2 \\ 3y^2 & 6xy-3
\end{pmatrix}.
$$
Ve stacionárním bodě dostáváme $$J(1,1)=
\begin{pmatrix}
  8 & 7\\3&3
\end{pmatrix}.
$$
Výpočtem determinantu dostáváme
$$|J-\lambda I|=
\begin{vmatrix}
  8-\lambda & 7 \\ 3 & 3-\lambda
\end{vmatrix}
=(8-\lambda)(3-\lambda)-21=\lambda^2-11\lambda +3.
$$
Kořeny jsou
$$\lambda_{1,2}=\frac{11\pm\sqrt{121-12}}{2}$$
 a oba jsou kladné. Ve stacionárním bodě proto je nestabilní uzel.

</div>

