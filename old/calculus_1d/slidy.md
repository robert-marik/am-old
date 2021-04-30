% Diferenciální počet funkcí jedné proměnné z ptačí perspektivy
% Robert Mařík
% 2017–2019


## Od funkčního předpisu k rychlosti změny

> Derivace je okamžitá rychlost změny.

\iffalse 

<div class='obtekat'>

![Derivace teploty je rychlost změny teploty. Zdroj: pixabay.com](coffee.jpg)

</div>

\fi

Hrnek kávy v místnosti o teplotě $20^\circ\mathrm{C}$ se ochladí z
teploty $95^\circ\mathrm{C}$ na $25^\circ\mathrm{C}$ například za $40$
minut. To znamená, že nápoj chládne rychlostí
$$\frac{95-25}{40} \,{}^\circ\mathrm{C}\, \mathrm{min}^{-1}=1.75^\circ\mathrm{C}\, \mathrm{min}^{-1},$$
tj. každou minutu se nápoj ochladí průměrně o necelé dva stupně
Celsia. Toto však není příliš realistický model. Horký nápoj chládne
rychleji, protože je tepelná výměna internzivnější díky většímu
rozdílu teploty nápoje a místnosti. Realističtejším modelem popisujícím závislost teploty na čase je funkce $$T(t)=20+75 e^{-0.0677t}.$$ Derivace této funkce
$$\frac {\mathrm dT}{\mathrm dt}=-75\cdot 0.0677 e^{-0.0677t}$$
udává rychlost změny teploty v libovolném čase. Pro $t=0$ a $t=40$ [dostáváme](https://sagecell.sagemath.org/?z=eJxL06jQtDU31UqtKNDQNdAzMDM316rQ1DYy4OUqKMrMK1FI0zDQ1EnTMDHQhIlogHm6IAlNfROEQr2UzLQ0DU2wehgbqBAA0VoY-g==&lang=sage&interacts=eJyLjgUAARUAuQ==)
$$\frac {\mathrm dT}{\mathrm dt}(0)=-5.08 ^\circ\mathrm{C}\, \mathrm{min}^{-1},\qquad
\frac {\mathrm dT}{\mathrm dt}(40)=-0.34 ^\circ\mathrm{C}\, \mathrm{min}^{-1},
$$ tedy na počátku chládne rychostí pět stupňů Celsia za minutu, na konci už jenom rychlostí necelého půl stupně za minutu.


---------------------

## Od rychlosti změny k funkčnímu předpisu

> Ze známé rychlosti změny veličiny je možné zrekonstruovat změnu této veličiny.


\iffalse 

<div class='obtekat'>

![Pokud dírou ve dně vytéká voda ze sudu, rychlost je na počátku větší (u dna je při větší hloubce větší tlak) a snižuje se. Klasický přístup hledání celkové změny pomocí násobení rychlosti s délkou časového intervalu selhává vinou nekonstantní rychlosti. Zdroj: pixabay.com](barrel.jpg)

</div>

\fi

V nádrži je metr vody a voda vytéká tak, že hladina klesá rychlostí $20\mathrm{cm}\,\mathrm{h}^{-1}$. Touto rychlostí by voda vytekla za pět hodin. Protože však s objemem vody klesá tlak u dna, výtoková rychlost se snižuje. V případě nádrže se svislými stěnami by byl realistický model popisující závislost rychlosti snižování hladiny na čase
$$\frac{\mathrm dh}{\mathrm dt}=(-0.2 + 0.02 t)\,\mathrm{m}\,\mathrm{hod}^{-1}.$$
Za prvních pět hodin [vyteče](https://sagecell.sagemath.org/?z=eJxL06jQtNU10DPSNtAzMNKq4OVK08vMK0lNL0osSdWo0DHQMTTQBAC0jwnX&lang=sage&interacts=eJyLjgUAARUAuQ==)
$$h(5)-h(0)=\int_0^5 \frac{\mathrm dh}{\mathrm dt} \,\mathrm dt=
\int_0^5 (-0.2 + 0.02 t) \,\mathrm dt=\left[-0.2 t + 0.01 t^2\right]_0^5
=
-0.75\,\mathrm m
$$
a voda tedy klesne o třičtvrtě metru. Po pěti hodinách nádrž ještě není prázná, ale je v ní pořád čtvrtina vody. Ta bude vytékat ještě dalších pět hodin, protože 
$$h(10)-h(5)=
\int_5^{10} (-0.2 + 0.02 t) \,\mathrm dt=
-0.25\,\mathrm m
$$

--------------

# Derivace

$$f'(x)=\frac{\mathrm{d}f}{\mathrm{d}x}=\lim_{\Delta x\to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$$

* Derivace funkce $f$ vzhledem k $x$ je okamžitá rychlost s jakou se
mění veličina $f$ při změnách veličiny $x$. 
* Jednotkou derivace funkce
$f(x)$ je jednotka $f$ dělená jednotkou $x$.
* Derivaci funkce $f(x)$ označujeme $f'$ nebo $\frac{\mathrm df}{\mathrm dx}$. 
* Derivaci derivace (druhou derivaci) funkce $f(x)$ označujeme $f''$ nebo $\frac{\mathrm d^2 f}{\mathrm dx^2}$.

# Kde ji potkám?


<style>
table, th, td {
   border: 2px solid green;
} 
table {width:97%;}
td {padding:10px}
tr td:first-child {color:green; background: #E9E9E9;}
table {
    border-collapse: collapse;
}
</style>

<style>
table, th, td {
   border: 2px solid green;
} 
table {width:97%;}
td {padding:10px}
tr td:first-child {color:green; background: #E9E9E9;}
table {
    border-collapse: collapse;
}

th {
    background-color: green;
    color: white;
    border-color: gray;
}

th {text-align: center;}
</style>

Vlastně všude, kde se něco mění a zajímá mne jak rychle.


Závislá proměnná|Nezávislá proměnná|Derivace|
|------------------------|-----------------------|------------------------|
|veličina $x$|čas|rychlost růstu veličiny $x$|
|dráha při pohybu při pohybu po přímce i vzdálenost od referečního bodu|čas doba od začátku pohybu nebo od referečního okamžiku|rychlost|
|rychlost|čas|zrychlení|
|teplota v místě tyče (např. stěna, což je v podstatě extrémně krátká a široká tyč)|poloha|gradient teploty, veličina udávající intenzitu toku tepla tyčí resp. stěnou|
|všeobecná cenová hladina (cca náklady na živobytí)|čas|inflace|
|náklady na výrobu zboží|množství zboží|mezní náklady|
|nadmořská výška na trase treku|poloha|stoupání trasy|
|graf funkce $f(x)$|$x$|růst grafu (směrnice tečny)|
|hmotnost části tyče (např od zvoleného bodu doleva)|poloha na tyči (např. vzdálenost od levého konce)|lineární hustota tyče|
|výška stromu|čas|rychlost růstu do výšky|
|objem kmene stromu (smrk)|čas|rychlost růstu ve smyslu přírůstu dřevní hmoty|
|potenciální energie tělesa v radiálním silovém poli|vzdálenost od středu|působící síla vynásobená faktorem $-1$|




--------------------

## Derivace ve fyzikálních zákonech 1


Derivace nejčastěji ve fyzikálních zákonech vystupuje jako rychlost
změny v čase, často vyjádřená slovy "časová změna"

> Newtonův zákon síly (pohyb hmotného tělesa na které působí vnější
síla): *Časová změna hybnosti je rovna výsledné působící síle.*
$$\frac{\mathrm d p}{\mathrm dt}=F$$

\iffalse 

<div class='obtekat'>

![Newtonův pohybový zákon, založený na derivaci, umožňuje kvantifikovat účinky všech sil na pohyb. Na Zemi i ve vesmíru. Zdroj: pixabay.com](druzice.jpg)

</div>

\fi

Tj. derivace hybnosti podle času je rovna výsledné síle. Hybnost je součinem hmotnosti a rychlosti 
$$p=mv$$
a její derivace 
je pro tělesa s konstantní hmotností součinem hmotnosti a derivace rychlosti, tj. zrychlení.
$$\frac{\mathrm d p}{\mathrm dt}=m \frac{\mathrm d v}{\mathrm dt}
= m a
$$
Zrychlení je druhá derivace polohy. Nejčastěji proto tento
zákon píšeme ve tvaru $$m\frac{\mathrm{d}^2 x}{\mathrm{d}t^2}=F.$$

Speciální případy dobře známé ze střední školy jsou zákon setrvačnosti
($F$ nulová), rovnoměrně zrychlený pohyb ($F$ nenulová konstantní) a
kmitavý pohyb na pružině ($F=-kx$).

----------------

## Derivace ve fyzikálních zákonech 2

> Faradayův zákon elmg. indukce (indukované napětí podél uzavřené
smyčky v proměnném magnetickém poli): *Hodnota indukovaného
elektromotorického napětí je rovna záporně vzaté časové změně
celkového magnetického toku, který prochází elektrickým obvodem*.


\iffalse 

<div class='obtekat'>

![Větší rychlost znamená větší derivaci a větší svit žárovky. Zdroj: pixabay.com](dynamo.jpg)

</div>

\fi

$$\mathcal E = -\frac{\mathrm d\Psi}{\mathrm dt}$$ Speciálním
případem známým ze střední školy je přímý vodič pohybující se v
homogenním magnetickém poli po rovnoběžných vodičích.


---------------------

## Rozšířené pojetí rychlosti růstu

> Rychlost změny nemusí být změna vztažená na jednotku času, ale i míra změny prostorového uspořádání (gradient) nebo změna vztažená na jinou vhodnou jednotku.

\iffalse 

<div class='obtekat'>

![Dlouhé kosti mají stavební materiál po obvodu. Příroda a evoluce optimalizovaly jejich strukturu. Zdroj: pixabay.com](skeletons.jpg)

</div>

\fi


Hmotnost a tuhost tyče (odolnost tyče vůči namáhání) kruhového průřezu o poloměru $r$ jsou úměrné druhé a čtvrté mocnině poloměru, $$m=k_1r^2,\qquad I=k_2r^4.$$
Platí
$$\frac {\mathrm dm}{\mathrm dr}=2k_1r,\qquad \frac {\mathrm dI}{\mathrm dr}=4k_2r^3.$$
Vidíme, že při zvýšení poloměru hmotnost i tuhost podle očekávání rostou (derivace je kladná), při větších
poloměrech však tuhost roste mnohem rychleji než hmotnost (třetí versus první mocnina). Při hledání
vhodného poměru mezi tuhostí a hmotností se proto jeví jako vhodná
myšlenka využít tento rozdíl a naopak šetřit materiálem (a snižovat
hmotnost) tam, kde úbytek materiál ovlivní tuhost relativně
málo. Proto se při konstrukcích s požadovanou
odolností vůči namáhání běžně používají trubky namísto tyčí.

---------------------

## Rychlosti změn vzájemně souvisejících veličin

> Často se setkáme s tím, že dvě nebo více veličin jsou svázány vzájemně jednoznačným vztahem a změna jedná veličiny vyvolává změnu veličiny další. Pomocí derivace a pomocí pravidla pro derivaci složené funkce je možné najít vztah mezi rychlostmi změn těchto veličin.


\iffalse 

<div class='obtekat'>

![Pokud koule taje tak, že se poloměr zmenšuje konstantní rychlostí, objem se zmenšuje stále pomaleji a pomaleji. Zdroj: pixabay.com](ball.jpg)

</div>

\fi


*Příklad:* Ledová koule taje tak, že se poloměr zmenšuje rychlostí $3$cm/hod. Jak rychle se zmenšuje objem v okamžiku, kdy je poloměr $10$cm?

*Řešení:*
Zadání vlastně říká následující: $V=\frac 43 \pi r^3$, $r=10$cm, $\frac {\mathrm{d}r}{\mathrm{d}t}=-3$cm/hod, $\frac {\mathrm{d}V}{\mathrm{d}t}=?$

Derivací získáváme
$$\frac {\mathrm{d}V}{\mathrm{d}t}=  4\pi r^2 \frac {\mathrm{d}r}{\mathrm{d}t}$$
a po dosazení
$$\frac {\mathrm{d}V}{\mathrm{d}t}=  4 \cdot \pi \cdot (10\mathrm{cm})^2\cdot (-3)\mathrm{cm}/\mathrm{hod}=-3800 \mathrm{cm}^3/\mathrm{hod}.$$

Objem koule se zmenšuje rychlostí 3800 krychlových centimetrů za
hodinu. To je zdánlivě vysoké číslo vzhledem k objemu celé koule (4100
krychlových centimetrů), ale všimněme si, že rychle klesá s klesajícím
poloměrem.

---------------------

## Lineární aproximace

> Je-li známa současná hodnota veličiny $f$ a rychlost změny této veličiny, je možno budoucí nebo minulou hodnotu veličiny $f$ odhadnout extrapolací za předpokladu, že rychlost změny bude resp. byla stále stejná.

$$f(x)\approx f(a)+f'(a)(x-a)$$

Toto je základní vztah pro lokální lineární aproximaci, pro nahrazení komplikovaných vztahů jejich lineárními přiblíženími.

Příkladem jsou vztahy pro umocňování a odmocňování čísel blízkých jedniččce
$$(1\pm x)^n\approx 1\pm nx
,\quad \text{pro malé }x.$$

Dvě základní aplikace tohoto vztahu vedou na vzorce známé ze středoškolské
fyziky: středoškolské vztahy pro energii pohybujícího se tělesa a pro potenciální
energii pro malé výšky nad povrchem Země jsou aproximací přesných vztahů plyoucích z Einsteinovy teorie relativity a z Newtonovy gravitační teorie.


$$E=\frac{m_0c^2}{\sqrt{1-\frac {v^2}{c^2}}}
=m_0 c^2 \left(1-\frac {v^2}{c^2}\right)^{-1/2}
\approx m_0c^2+\frac 12 m_0v^2 \quad \text{pro $v$ mnohem menší než $c$}$$

$$V=-\kappa \frac{mM}{R}\left (1+\frac hR\right)^{-1}
= -\kappa \frac{mM}{R+h}\approx -\kappa \frac{mM}{R} + \kappa \frac{mM}{R^2} h=E_0+m g h,\quad \text{kde $g=\kappa \frac{M}{R^2}$}$$

---------------------

## Lineární aproximace při řešení rovnic

\iffalse 

<div class='obtekat'>

![Některé úlohy je nutné řešit numericky. I v takovém případě je linearizace vhodným nástrojem pro zjednodušení problému. Zdroj: pixabay.com](binary.jpg)

</div>

\fi



Z lineární aproximace 
$$f(x)\approx f(a)+f'(a)(x-a)$$
pro $a=x_n$, $x=x_{n+1}$, $f(x_{n+1})=0$ dostáváme
$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}.$$
Tímto způsobem můžeme numericky řešit i velmi obtížné rovnice. Například pro rovnici $$x=\cos x$$ a počáteční odhad $x_0=1$ dostáváme $f(x)=x-\cos x$, $f'(x)=1+\sin x$, $$x_{n+1}=x_n-\frac{x_n-\cos x_n}{1+\sin x_n}$$ a jednotlivé iterace s aproximací na 80 desetinných míst [dávají postupně](https://sagecell.sagemath.org/?z=eJyrsDXk5UrLL1LIVMjMUyhKzEtP1TDXtOLlUgCCCluNCl0gSs4v1qjQ1NTXMNQuzswDMTX18jRSMtMzS4ptLQw0IaoLijLzShQqAJbBFls=&lang=sage&interacts=eJyLjgUAARUAuQ==)

~~~
0.75036386784024389303494230668217685324699306585535903096658315202443061372724844
0.73911289091136167036058529090489023400289283673565690732340797067262734474030949
0.73908513338528396976012512085680433288953312317018897963123060924114905347788420
0.73908513321516064166170262568502637232522326252964269151340253531790167136371866
0.73908513321516064165531208767387340401342077636703525840515904303894688001184009
0.73908513321516064165531208767387340401341175890075746496568063577328465488354759
0.73908513321516064165531208767387340401341175890075746496568063577328465488354759
~~~

Vidíme, že proces neuvěřitelně rychle konverguje k řešení rovnice. Každým krokem se přibližně zdvojnásobí počet desetinných míst, která jsou správně.



# Integrál

Derivace umožní přechod od hodnoty veličiny v čase k okamžité
rychlosti její změny. Opak derivace, integrál, umožní zjistit, jaká je
celková změna veličiny, která se mění zadanou rychlostí. (Má smysl
provádět v případě nekonstantních rychlostí, jinak je problém
triviální.) Kromě toho integrál poslouží, pokud potřebujeme zobecnit
průměr na případ, kdy průměrujeme nekonečně mnoho hodnot spojitě
rozložených na nějakém intervalu.

* Změnu polohy pohybujícího se tělesa je možno vypočítat pomocí vztahu 
$$\Delta s=\int_a^b v(t)\,\mathrm{d}t.$$
Ze střední školy jsou známy speciální případy, kdy rychlost je
konstantní (dráha rovnoměrného pohybu, $s=s_0+vt$) nebo lineární (dráha rovnoměrně zrychleného pohybu, $s=s_0+v_0t+\frac 12 at^2$ )
* Energie a práce jsou integrály síly jako funkce polohy. Ze střední
školy známe speciální případ pro práci konstantní síly ($W=Fs$) a síly
úměrné posunutí (pro pružinu platí Hookův zákon a proto $W=\frac 12
kx^2$.)


---------------------

## Střední hodnota

Střední hodnota funkce $f$ na intervalu $[a,b]$ je $\frac1{b-a}\int_a^b f(x)\,\mathrm{d}x$.

Speciálním případem známým ze střední školy je efektivní hodnota střídavého napětí a proudu,
kdy $U_{\text{ef}}^2$ je střední hodnota $U^2$. (Druhá mocnina,
protože práce el. napětí je úměrná druhé mocnině napětí.)
 

*Příklad:* Teplota $T$ ve °C zaznamenaná během dne odpovídala funkci $$T = 0.001 t^4 − 0.280 t^2 + 25$$

kde $t$ je počet hodin po poledni ($-12 \leq t \leq  12$). Jaká je průměrná denní teplota?

*Řešení:*
$$\frac 1{24}\int_{-12}^{12} 0.001 t^4 − 0.280 t^2 + 25 \,\mathrm dt \approx 15.7$$
Průměrná denní teplota je 15.7 °C.

# Diferenciální rovnice

Někdy rychlost změny veličiny souvisí s numerickou hodnotou této
veličiny a proto nestačí k výpočtu změny této veličiny integrální
počet. Nástrojem pro studium jsou diferenciální rovnice.

* Rychlost tepelné výměny je úměrná rozdílu teplot.
* Rychlost s jakou dřevo při sušení ztrácí vodu je úměrná množství vody,
kterou má dřevo navíc oproti rovnovážnému stavu.
* Speciálním případem diferenciální rovnice, známým ze střední školy, je radioaktivní rozpad
$$\frac {\mathrm{d}y}{\mathrm{d}t}=-ky$$
(rychlost radioaktivního rozpadu je úměrná množství nerozpadlého
materiálu) s poklesem aktivity geometrickou řadou (poločas
rozpadu).
* Typickým příkladem v biologických vědách je růst populace, kdy rychlost růstu
populace je určena velikostí této populace (větší populace má více
narozených jedinců za jednotku času, příliš velká populace nemusí mít
dostatek obživy v dané lokalitě apod.)  Například základní rovnice pro studium populací
v biologii je logistická rovnice $$\frac
{\mathrm{d}y}{\mathrm{d}t}=ry\left(1-\frac yK\right).$$
	
