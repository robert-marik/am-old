% Parciální derivace 
% Robert Mařík
% jaro 2019

# Derivace

Derivace je matematický prostředek, který umožňuje sledovat, měřit a
porovnávat rychlosti změn fyzikálních veličin. Přirozeně se tak
objevuje při formulaci a popisu téměř všech dynamicky probíhajících
fyzikálních jevů. (Fyzikální popis světa tak je prezentovaný
středoškolskou fyzikou je častou pouze jakousi aproximací ve které
jevy probíhají konstantní rychlostí - například bez derivací umíme
studovat pouze rovnoměrný nebo rovnoměrně zrychlený pohyb).

**Poznámka.** Všude v následujícím textu budeme předpokládat, že
funkce a derivace které zde vystupují jsou dostatečně hladké a
rovnosti platí na dostatečně pěkných množinách. V praktických
aplikacích bývají tyto předpoklady zpravidla triviálně splněny, proto
je pro úsporu místa nebudeme vypisovat. Zájemce najde poučení v
odborné literatuře.

# Obyčejná derivace

<div class='sloupce'>
<div>
* <span class='red'>Derivace</span> funkce $y=f(x)$ je definována vztahem $$\boxed{\displaystyle f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}h}$$
* Jedná se o veličinu udávající, jak rychle se mění funkční hodnoty
  funkce při změnách vstupních dat. 
* Alternativní označení je $\frac{\mathrm{d}f}{\mathrm{d}x}$.
* Derivace $f'(x)$ je směrnice tečny ke grafu funkce $y=f(x)$ v bodě $[x,f(x)]$.
* Lineární aproximací funkce $y=f(x)$ v bodě $x_0$ je $$f(x)\approx f(x_0)+f'(x_0)(x-x_0)$$ Slovy: funkční hodnota teď (v $x$) je funkční hodnota před chvílí (v $x_0$) plus celková změna, která je součinem rychlosti změny ($f'(x_0)$) a času, za který se změna udála ($x-x_0$).

</div>

\iffalse

![Derivace a tečna (lineární aproximace)](derivace.png)

\fi

</div>


\iffalse

# Motivace pro rozšíření pojmu derivace

\iffalse 

<div class='obtekat'>

![Mnoho procesů se řídí zákony zachování. Pokud proudící látka může vznikat a zanikat nebo měnit hustotu, není situace tak jednoduchá, jak to známe z rovnice kontinuity ve středoškolské fyzice. Zdroj: pixabay.com](river.jpg)

</div>

\fi



Derivace je vhodná ke studiu fyzikálních procesů na makroskopické úrovni
těles. Takovým fyzikálním zákonům říkáme zákony v integrálním
tvaru. Ty jsou často odvozeny ze zákonů zachování.

* Tepelná energie tělesa (a teplota) se mění tak, že v tělese vzniká
nebo zaniká (chemické reakce, el. proud apod.) anebo tepelnou výměnou
(teplo odtéká nebo přitéká kontaktem s tělesem o jiné teplotě).
* Kapaliny a plyny proudí tak, že změna v definovaném místě prostoru
je dána rozdílem, kolik do prostoru přiteče a vyteče. Pokud bereme v
úvahu i zdroje nebo spotřebiče tak i rozdílem kolik v daném místě
vznikne a kolik zanikne (například při proudění podzemní vody mezi
dvěma geologickými vrstvami dojde k částečnému průsaku mimo tyto
vrstvy).

Pro vyjadřování procesů jako jsou rychlost změny teploty tělesa nebo
množství tekutiny v daném objemu jsou vhodné (obyčejné) derivace.

Někdy však požadujeme detailnější informace o celém procesu, abychom
měli přesnější popis a dokázali odhalit vliv všech relevantních
parametrů. U tepelné výměny bychom například sledovali, jak se teplo
předává z jednoho místa tělesa do druhého místa a jak prostupuje
tělesem. Takový pohled je nutný například při studiu procesu, který
není stacionární v čase. Při tomto pohledu již musíme znát teplotu
nejen jako funkci času, ale i jako funkci prostorových
souřadnic. Výsledkem tohoto přístupu je formulace zákonů v
diferenciálním tvaru. Tento tvar říká, co se děje v konkrétním místě a
dává lepší náhled na fyzikální podstatu. Proto tomuto přístupu často
dáváme přednost a používáme jej jako výchozí bod pro studium a popis
konkrétních situací. Musíme tedy pracovat s funkcemi více proměnných a
studovat, jak se mění vzhledem k jednotlivým proměnným. To je přesně
úkol pro diferenciální počet funkcí více proměnných a *parciální derivace*.

\fi

# Parciální derivace

<div class='sloupce'>

* Pro funkce dvou proměnných rozlišujeme <span class='red'>parciální derivace</span> podle jednotlivých proměnných. 
  $$\begin{aligned}\frac{\partial f(x,y)}{\partial x}&=\lim_{h\to 0}\frac{f(x+h,y)-f(x,y)}h\\
	  \frac{\partial f(x,y)}{\partial y}&=\lim_{h\to 0}\frac{f(x,y+h)-f(x,y)}h\end{aligned}$$
* Jedná se o stejnou veličinu jako u obyčejné derivace, ale vždy jenom
  vzhledem k jedné proměnné. Parciální derivace $\frac
  {\partial}{\partial x}f$ tedy udává, jak rychle se mění $f$ při
  změnách veličiny $x$.
* V definici a při výpočtu parciální derivace podle $x$ je proměnná
  $y$ konstantní. Geometricky to je možno interpretovat tak, že
  studujeme křivku, která vznikne na řezu grafu funkce $z=f(x,y)$
  rovinou $y=\text{konst}$.
* Alternativní označení: $f'_x(x,y)$, $f'_y(x,y)$.

![Parciální derivace funkce $f$ v bodě $[2,-2]$ jsou derivace křivek vzniklých na řezech rovinami $x=2$ a $y=-2$.](parcialni_derivace_1.png)

</div>

# Aplikace parciálních derivací - základní myšlenky

* Parciální derivace $\frac {\partial f}{\partial x}$ je rychlost
  změny funkce $f(x,y)$ při změnách veličiny $x$.
    * Pokud se veličina $x$ změní o $\Delta x$, funkční hodnota se změní o přibližně $\frac {\partial f}{\partial x}\Delta x$.
    * Pokud je veličina $x$ známa s chybou $\Delta x$, veličina $f$ je vypočítána s chybou $\frac {\partial f}{\partial x}\Delta x$.
    * Pokud je $u$ celková vnitřní energie v jednotkovém objemu tělesa (hustota tepelné energie), je $\frac{\partial u}{\partial t}$ rychlost, s jakou se tato energie mění v čase. Pokud ke změně dochází pomocí vedení tepla, je tato derivace rovna tepelnému toku přes hranice. Pokud dochází ke generování tepla v tělese (chemická reakce, elektrický proud), je tato derivace  rovna tepelnému výkonu zdroje. V obecném případě se oba faktory sčítají, což vede k odvození rovnice vedení tepla ze zákona zachování.
* Jednotkou derivace $\frac{\partial f}{\partial x}$ je jednotka veličiny $f$ dělená jednotkou veličiny $x$.
* Analogická tvrzení jako pro veličinu $x$ platí pro veličinu $y$.
* Ve fyzice často pracujeme s funkcemi, které mají spojité parciální derivace. Takové funkce se nazývají *hladké funkce*.


\iffalse 


# Interpretace parciálních derivací - pohyb ještěrky



<div class='obtekat'>

![Energie potřebná pro překonání pevné vzdálenosti závisí na hmotnosti jedince a na rychlosti, kterou vyvíjí. Zdroj: pixabay.com](lizard.jpg)

</div>

Energie $E$ (v kcal), kterou spotřebuje ještěrka o hmotnosti $m$ (v
gramech) na překonání vzdálenosti jednoho kilometru rychlostí $v$ (v
kilometrech za hodinu) se dá odhadnout vzorcem
$$E(m,v)=2.65 m^{0.66} + \frac{3.5 m^{0.75}}{v}.$$
Přímým výpočtem je možné určit
$$\frac{\partial E}{\partial v}=-\frac{3.5 m^{0.75}}{v^2}.$$ Pro $m=400\,\mathrm{g}$ a $v=8\,\mathrm{km}\,\mathrm{h}^{-1}$ dostáváme
$$\frac{\partial E}{\partial v}(400,8)=-4.9\,\mathrm{kcal}\,\mathrm{km}^{-1}\mathrm{h}.$$ Zvýšení rychlosti o kilometr za hodinu vede ke snížení energetického výdeje ještěrky o $4.9\,\mathrm{kcal}$. Podobně, platí
$$\frac{\partial E}{\partial m}=
{2.65}\times 0.66 {m^{-0.34}} + \frac{3.5\times 0.75 m^{-0.25}}{v}=
\frac{1.749}{m^{0.34}} + \frac{2.625}{m^{0.25} v}
$$
a pro výše uvažované hodnoty dostáváme
$$\frac{\partial E}{\partial m}(400,8)=
0.30\,\mathrm{kcal}\,\mathrm{g}^{-1}.
$$
Každý gram, který má ještěrka navíc oproti hmotnosti $400$ gramů, zvedne energetický výdej přibližně o $0.30\,\mathrm{kcal}$.

[Online výpočet.](https://sagecell.sagemath.org/?z=eJwrSyzSUM9VKFPX5OVytTXSMzPVyo0z0DMzU9BWMNYzVQDzzE31y3i5Cooy80oUXDVybU0MDHTKbC004WJ6KZlpaRplmrjlcpHlANRDHpQ=&lang=sage)

(Zpracováno podle Stewart: Biocalculus)
\fi



# Aplikace parciálních derivací - brzdná dráha


\iffalse 

<div class='obtekat'>

![Brzdy v autě musí absorbovat kinetickou energii, která je lineární funkcí hmotnosti a kvadratickou funkcí rychlosti. Zdroj: pixabay.com](car.jpg)

</div>

\fi

*Příklad:* Brzdná dráha $L$ (v metrech) auta o hmotnosti $m$ (v kilogramech) brzdícího z rychlosti $v$ (v kilometrech za hodinu) je dána vzorcem
$$L=k m v^2, $$ kde $k= 3.45 \times 10 ^{-6}\,(\mathrm{m}\,\mathrm{hod}^2)/(\mathrm{kg}\,\mathrm{km}^2)$. Pro $m=1100\,\mathrm{kg}$ a $v=100\,\mathrm{km}/\mathrm{hod}$ je brzdná dráha $37.95\,\mathrm{m}$.

* Parciální derivace podle $m$ je $\frac{\partial L}{\partial m}=kv^2$
  a pro zadané hodnoty vychází
  $$\frac{\partial L}{\partial m}=0.0345 \mathrm{m}/\mathrm{kg}.$$
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
* Z parciální derivace podle $v$ víme, že změna rychlosti o $\Delta v$
  změní brzdnou dráhu přibližně o $\Delta L\approx 2kmv\Delta v$. Nabízí se
  otázka, proč s touto přibližnou informací pracovat, když změnu umíme
  určit i přesně, $\Delta L=k m(v+\Delta v)^2 - k m v^2=2kmv\Delta v+ k m (\Delta v)^2$. *Překvapivě, přibližný
  vzorec založený na derivacích je skoro vždy jednodušší, než přesný výpočet
  změny.* Tento efekt je možné vidět u druhé mocniny, je výraznější u
  vyšších mocnin a stane se fatálním u obecných neceločíslených mocnin
  nebo obecnějších funkcí. Pokud náš výpočet vstupuje do
  komplexnějších inženýrských modelů, staly by se neřešitelnými. Že
  s derivací jde jenom o aproximaci vůbec nevadí, protože zapojením důmyslných
  matematických postupů zapracovaných přímo v definici (limita) srážíme chybu na nulu.
 
\iffalse

[Online výpočet.](https://sagecell.sagemath.org/?z=eJzL1lHI1SmzLUss0lDPVshVKFPX5OXKyE_Jyy-ptNWozrYy1jMx1TI0iNPQNdPUybUyNDQw0CmzApK1QIU-ttlauVplcUZApgZUl6ZecUZ-uQZQFkxH--ilZKalaeRq6sBZcKWx6KrK4KrKUFUBAMMQMSg=&lang=sage)

\fi


# Zákon šíření chyb  (chyba nepřímo měřené veličiny)

\iffalse 

<div class='obtekat'>

![Každá chyba má své důsledky. Důsledky chyb ve vstupních datech kvantifikujeme pomocí zákona šíření chyb. Zdroj: pixabay.com](mistake.jpg)

</div>

\fi



* V praxi často měříme nepřímo veličinu $f$ tak, že měříme veličiny
$x_1$, $x_2$, $\dots$, $x_n$ a hodnotu veličiny $f$ určíme pomocí vzorce
$f(x_1, x_2, \dots, x_n)$. 
* Měření každé z veličin je zatíženo
chybou. Je-li chyba veličiny $x_i$ rovna $\Delta x_i$, způsobí tato
odchylka to, že chyba veličiny $f$ bude (v souladu se vzorcem pro lineární aproximaci)
přibližně
$$
  \Delta f\approx \left|\frac{\partial f}{\partial x_i}\Delta x_i\right|
$$
* Celkovou chybu veličiny $f$ můžeme určit sečtením chyb způsobených
jednotlivými veličinami $x_i$. Častěji se však používá následující vzorec
$$
  \Delta f(x_1,x_2,\dots x_n)\approx\sqrt{\left(\frac{\partial f}{\partial x_1}\Delta x_1\right)^2+\left(\frac{\partial f}{\partial x_2}\Delta x_2\right)^2+\cdots+\left(\frac{\partial f}{\partial x_n}\Delta x_n\right)^2}
$$
označovaný **zákon šíření chyb**.


# Zákon šíření chyb  - příklad

\iffalse 

<div class='obtekat'>

![Pocitová teplota v zimě závisí na skutečné teplotě a na síle větru. Zdroj: pixabay.com](zima.jpg)

</div>

\fi



Kanadský empirický vzorec pro pocitovou teplotu v zimě ([wind-chill
factor](https://en.wikipedia.org/wiki/Wind_chill)) je $$W(T,v) =
13.12+0.6215 T-11.37 v^{0.16}+0.3965 T v^{0.16},$$ kde $T$ je teplota
(ve stupních Celsia) a $v$ je rychlost větru (v km/hod). Teplota byla
změřena $-11.0\,{}^\circ\!\text{C}$ s chybou $0.2\,{}^\circ\!\text{C}$ a rychlost $26
\,\text{km/hod}$ s chybou $5\,\text{km/hod}$. S využítím zákona šíření
chyb určíme, jaký vliv mají nepřesnosti v měření na nepřesnost
vypočítané veličiny.

Dosazením do vzorce dostáváme $W(-11,26)=-20.212\,{}^\circ\!\text{C}$. Derivováním dostáváme
$$\begin{aligned}\frac{\partial W}{\partial T}(T,v)&=0.6215+0.3965 v^{0.16},\\
\frac{\partial W}{\partial v}(T,v)&=-11.37\times 0.16 v^{-0.84}+0.3965 \times 0.16 Tv^{-0.84}
\end{aligned}
$$
a po dosazení 
$$\begin{aligned}\frac{\partial W}{\partial T}(-11,26)&=1.289,\\
\frac{\partial W}{\partial v}(-11,26)&=-0.163 \,{}^\circ\!\text{C}\, \text{hod}/\mathrm{km}.
\end{aligned}
$$
Za dané teploty a rychlosti větru způsobí nárůst teploty o jeden
stupeň nárůst pocitové teploty přibližně o $1.3$ stupně. Podobně,
zesílení větru o jeden kilometr za hodinu způsobí snížení pocitové
teploty přibližně o $0.16$ stupně.
Ze zákona šíření chyb dostáváme pro chybu pocitové teploty (dosazováno bez jednotek)
$$\Delta W=\sqrt{\left(1.289\times 0.2\right)^2+\left(-0.163\times 5\right)^2}=0.85\,{}^\circ\!\text{C}.$$
Pocitová teplota je tedy $W=-20.2\,{}^\circ\!\text{C}\pm 0.9\,{}^\circ\!\text{C}$.

\iffalse

[Online výpočet.](https://sagecell.sagemath.org/?z=eJxdi0EKgzAQRfeCdxA3TmIanISmdJFbDGRThEIQ3EhNZc5vJFiwu__e4_M7QUeKO1FXAfIQHq1G0w_aGbxLuiFq-5A8wqDRiezt02X_M3UVyQcd52kCEsDeOEU-347CZ-G_8knzsjWhyKZY1b6W9kyRrsgX_K5pA4gkRtNDZGnyKP8d3o01SQ==&lang=sage)

\fi 

\iffalse

# Motivace pro zavedení diferenciálních operátorů

\iffalse 

<div class='obtekat'>

![Při proudění tekutin nesledujeme jednotlivé molekuly, ale vektor rychlosti. Díky tomu můžeme stejným aparátem sledovat tok tekutiny, tok tepla nebo tok jiné veličiny. Zdroj: pixabay.com](water.jpg)

</div>

\fi

Parciální derivace se vyskytují ve většině důležitých rovnic
popisujících fyzikální svět okolo nás. 

Parciální derivace umožňují sledovat závislost stavových veličin v
závislosti na souřadnicích nebo čase, a to pro každou souřadnici
samostatně. Nicméně souřadný systém je něco, co do popisu vnášíme
uměle a proto by fyzikální proce neměl být na tomto souřadném systému
závislý. *Proto často spojujeme parciální derivace do složitějších
výrazů -- diferenciálních operátorů. Zde teprve vynikne síla
parciálních derivací.*

Jedno z uplatnění je v mechanice kontinua při popisu proudění
tekutin. Pomocí Newtonova zákona můžeme napsat pohybovou rovnici pro
každou molekulu tekutiny a ze znalosti počáteční rychlosti a polohy
všech molekul zjistit, jak bude vypadat pohyb molekul v libovolném
čase. V praxi však nedokážeme ani přesně určit počet molekul, ne tak
jejich počáteční polohu a rychlost. Jedním z přístupů odstraňujících
tyto problémy je statistický přístup používaný ve statistické
fyzice. Jiný přístup je, že nesledujeme pohyb jednotlivých molekul,
ale v jednotlivých místech prostoru sledujeme důležité
charakteristiky, jako například rychlost proudění nebo tlak v
kapalině. To je přesně úloha pro diferenciální operátory sestavené z
parciálních derivací.

Výhodou použití univerzálního nástroje parciálních derivací je, že
získáme podobné rovnice pro studium řady rozdílných problémů. Při
popisu proudění vycházíme ze zákona zachování: přírůstek proudící
veličiny v uvažovaném místě tělesa je dán součtem vydatnosti všech
zdrojů v tomto místě sníženém o množství veličiny, které vyteče přes
hranice. Přitom spotřebiče uvažujeme jako zdroje se zápornou
vydatností a tok dovnitř jako záporný tok. Na fyzikálním charakteru
proudící veličiny nezáleží. Podobnými rovnicemi proto popisujeme
proudění vody v potrubí (proudění homogenním prostředím, které neklade
odpor), proudění vody ve dřevě (tj. proudění ortotropním materiálem),
proudění vody nebo ropy v půdě (proudění anizotropním materiálem),
proudění tepla v tepelně vodivém prostředí (proudění veličiny, která
není spojena přímo s látkou) nebo například difuzi.

\fi


# Gradient

<div class='sloupce'>
* <span class='red'>Gradient</span> je definován pro skalární funkce
* Gradient funkce dvou proměnných $f(x,y)$:
  $$\mathop{\mathrm{grad}}f=\left(\frac{\partial f}{\partial
  x}, \frac{\partial f}{\partial y}\right)$$
* Gradient funkce tří proměnných $f(x,y,z)$:
  $$\mathop{\mathrm{grad}}f=\left(\frac{\partial
  f}{\partial x}, \frac{\partial f}{\partial y},
  \frac{\partial f}{\partial z}\right)$$
* Formálně většinou zapisujeme gradient $\nabla f,$ kde vystupuje
  operátor nabla definovaný vztahem
  $$\nabla=\left(\frac{\partial}{\partial x}, \frac{\partial}{\partial
  y}, \frac{\partial}{\partial z}\right)$$ nebo
  $$\nabla=\left(\frac{\partial}{\partial x}, \frac{\partial}{\partial
  y}\right)$$ (v závislosti na počtu proměnných funkce $f$). "Násobení"
  $\frac{\partial }{\partial x}$ s funkcí $f$ přitom chápeme jako
  parciální derivaci $\frac{\partial f}{\partial x}$.
* Gradient je v každém bodě kolmý k vrstevnici. [Nakreslit online.](https://sagecell.sagemath.org/?z=eJxlj71uwyAUhfdIfgcU2TKk5Mdupip0TFdPnapY1IaYFoMFJDV5-hLbUVKVAbjncr_D4bDHHpH-kC_8sl_4w3M0a9mF9SQ0MrxFY-kJ9HiZ4TzUjaS1UJ5sN9HMNvoHNq6VcL5r8td3Yx07K1ExQMHRhHdMud06dMD-pL4r9gJiwEdLkFgQzxMgqWM9HMWwotkj1aRvEyVMfij6KeltHiYWJxbFaQIfEata8HBDCIP_8uAwWBSk0srpkyk7qR3keAg97B6DqWfJlDUoLe1I-sVcigEXUpI9lZahK6h4uiLKM6ucNiUXTNaQr27pIVorbdo_SvjbaDcc_p65uMKPVlwYyTYYUNsFaGmoE5pk6BegT4aw&lang=sage)


\iffalse
![Gradient je kolmý na vrstevnice](gradient.svg)
\fi

</div>


# Gradient v přírodě a přírodních zákonech 

\iffalse 

<div class='obtekat'>

![U teplokrevných živočichů vystavených chladu vzniká velký gradient teploty. Pro snížení tohoto gradientu a lepší ochranu před mrazem je výhodné mít silnou vrstvu chlupů. Ptáci se v zimě zase umí proměnit v načepýřené koule. Zdroj: pixabay.com](ovce.jpg)

</div>

\fi

* V jednorozměrném případě je gradient totéž co derivace. Přesto se někdy z tradičních důvodů respektujících zvyklosti oboru nemluví o derivaci, ale o gradientu. Například mluvíme o gradientu teploty při studiu *tepelně izolačních vlastností* izolačních materiálů. Pokud máme na mysli vrstvu z jednoho materiálu (a ne například sendvičovou stěnu), je rozložení teploty lineární a dokonce v tomto případě pojmem gradient vlastně označujeme směrnici přímky.
* S gradientem souvisí *majáková navigace* při migraci živočichů. Ti sledují určitý chemický podnět a pohybují se ve směru největšího růstu tohoto podnětu (tj. ve směru gradientu). Například žralok ve vodě takto sleduje koncentraci krve. Pokud je mezi žralokem a zdrojem krve proud, který krev unáší, nepopluje žralok rovnou čarou ke zdroji krve, ale koncentrace krve ho povede po delší trase.
* Pokud se zajímáme nejenom o směr, ale i velikost gradientu, pomůže to k posouzení jak rychle se mění veličina v prostoru (gradient je velký, jsou-li vrstevnice nahusto). 
* *Síla* ($\vec F$) působící na těleso v silovém poli ve kterém je možno zavést potenciální energii ($V$) je gradientem potenciální energie vynásobeným faktorem $-1$ (záporně vzatý gradient).
$$\vec F=-\nabla V$$
Pro jednorozměrnou úlohu a těleso v potenciálové jámě (tj. v rovnovážném stavu, kdy je minimum potenciální energie) můžeme potenciál v okolí minima aproximovat pomocí Taylorova rozvoje $$V(x)\approx V_0+\frac 12 V''(0)x^2+\cdots $$ (souřadnice volíme tak, že toto minimum je pro $x=0$) a je-li $|xV'''(0)|\ll V''(0)$, potom
$$\vec F=-\nabla V=-V''(0)x=-kx.$$ To znamená, že síla je úměrná výchylce, stejně jako u tělesa na pružině. Podobně ve vícerozměnrném případě.
* V homogenním tíhovém poli s osou $z$ svisle nahoru je gravitační potenciál (potenciální energie tělesa o jednotkové hmotnosti) dán vztahem $\phi(x,y,z)=gz$ a gradient je konstantní vektor $\nabla \phi=(0,0,g)$. Proto je práce přímo úměrná potenciálu a má smysl práci (změnu potenciální energie) považovat jenom za jiné vyjádření výškového rozdílu (změnu souřadnice $z$) Dokonce je to možné interpretovat jako změnu jednotek. Při proudění vody v půdě nebo v rostlinách hraje roli celá řada různých příspěvků k potenciální energii, jako gravitace, vnější tlak, osmóza, kapilarita. Pro pohodlnou práci někdy všechny tyto faktory přepočítáváme na odpovídající rozdíl výšek vodního sloupce, čímž je dána *piezometrická hladina*. Je to vlastně celková potenciální energie přepočtená na výšku vodního sloupce.
* Většina proudění v přírodě je způsobena gradientem veličiny, která je hybatelnou silou tohoto proudění. Například vítr vznikne rozdílem v prostorovém rozložení tlaku (nenulovým gradientem). Často je intenzita  proudění úměrná tomuto gradientu (*Fickův zákon*). Například hustota toku $\vec j$ při difúzi vody ve dřevě je dána vztahem $$\vec j=-D\nabla c,$$ kde $c$ je koncentrace vody a $D$ je difúzní konstanta. 


# Lineární aproximace funkce

* Lineární aproximací funkce $z=f(x,y)$ v bodě $(x_0, y_0)$ je
$$      f(x,y)\approx f(x_0, y_0)+\frac{\partial f (x_0,y_0)}{\partial x}(x-x_0)+\frac{\partial f (x_0,y_0)}{\partial y}(y-y_0)$$
nebo (pomocí gradientu)
$$      f(x,y)\approx f(x_0, y_0)+ \nabla f(x_0,y_0)\cdot (x-x_0,y-y_0).$$
* Tečná rovina ke grafu funkce $z=f(x,y)$ vedená bodem
  $[x_0,y_0,z_0]$, kde $z_0=f(x_0,y_0)$ má rovnici
  $$z=z_0+\frac{\partial f (x_0,y_0)}{\partial x}(x-x_0)+\frac{\partial f (x_0,y_0)}{\partial y}(y-y_0),$$
nebo (pomocí gradientu)
$$      z= z_0+ \nabla f(x_0,y_0)\cdot (x-x_0,y-y_0).$$

# Lineární aproximace funkce  - příklad

Kanadský empirický vzorec pro pocitovou teplotu v zimě ([wind-chill
factor](https://en.wikipedia.org/wiki/Wind_chill)) je $$W(T,v) =
13.12+0.6215 T-11.37 v^{0.16}+0.3965 T v^{0.16},$$ kde $T$ je teplota
(ve stupních Celsia) a $v$ je rychlost větru (v km/hod). Teplota byla
změřena $-11.0\,{}^\circ\!\text{C}$ s chybou $0.2\,{}^\circ\!\text{C}$ a rychlost $26
\,\text{km/hod}$ s chybou $5\,\text{km/hod}$. S využítím zákona šíření
chyb určíme, jaký vliv mají nepřesnosti v měření na nepřesnost
vypočítané veličiny.

Na předchozích slidech jsme vypočítali 
$$\begin{aligned}W(-11,26)&=-20.212\,{}^\circ\!\text{C}\\\frac{\partial W}{\partial T}(-11,26)&=1.289,\\
\frac{\partial W}{\partial v}(-11,26)&=-0.163 \,{}^\circ\!\text{C}\, \text{hod}/\mathrm{km}.
\end{aligned}
$$
Za dané teploty a rychlosti větru způsobí nárůst teploty o jeden
stupeň nárůst pocitové teploty přibližně o $1.3$ stupně. Podobně,
zesílení větru o jeden kilometr za hodinu způsobí snížení pocitové
teploty přibližně o $0.16$ stupně.

Přibližný vzorec pro pocitovou teplotu platný pro teploty blízké $-11.0\,{}^\circ\!\text{C}$ a rychlosti větru blízké $26
\,\text{km/hod}$ je
$$W\approx -20.12 +1.289 (T+11) -0.163(v-26).$$

# Tečna k vrstevnici

<div class='sloupce'>

Pro $z=0=z_0$ dostáváme z tečné roviny následující: Nechť
  $f(x_0,y_0)=0$. Tečna k vrstevnici funkce $f(x,y)$ na úrovni nula,
  tj. ke křivce $0=f(x,y)$, vedená bodem $[x_0,y_0]$ má rovnici
  $$0=\nabla f(x_0,y_0)\cdot (x-x_0,y-y_0).$$
  
\iffalse

[Nakreslit online](https://sagecell.sagemath.org/?z=eJxtkc1ygyAUhffO-A7MZBFIrtafdMk7ZNFdp3EIYqRRcBAN9umL5qeLujtw7v0u97BB1aCuXCCGrOCKoRGddSnQp0tgSr7CoMIOJkLdKdtNkdtNpzzKwmBxaQZpGGycF_HBC39TSVUWRmuLfZ-vIZBASsIgDO50iqr4YlgphbKYLCUJiUtti87ocuAWj4JbbTB20WxG3iaE0mRGbJA-G_Yjrmg0vRWjkhz-pECePxjtNVJDw2BZaPKLPQcOYXCkXCurB1N0zfxI8NulkBPAk39pRgA17Cyann6YQQB6FPfUMHURODrAwa8DvGUd3X4LuyUz8riXbddILu2d-khyZicvdv5sq_tx68dIJW6ytDXN1xn33BGlKPlPWmlnxugbfiQKrxSXI9mvpP6mtGnxikGW_zrGfe2BrO88qjDMSk1TcK1UNI3fYWqZmwX5BYh4r2w=&lang=sage)

![Tečna k vrstevnici](tecna.png)	
\fi

</div>



# Implicitně definovaná funkce 


<div class='sloupce'>

Mějme funkci $f(x,y)$ dvou proměnných a její vrstevnici na úrovni $C$
$$f(x,y)=C. \tag{1}$$ Tato rovnice za jistých okolností může definovat $y$
jako funkci proměnné $x$. \iffalse Pokusíme se najít derivaci této funkce. K
tomu uvažujme bod $(x_0,y_0)$ ležící na této vrstevnici,
tj. $f(x_0,y_0)=C$.

* Rovnice tečné roviny v bodě $(x_0,y_0)$ je
  $$ z=f(x_0,y_0)+\nabla f(x_0,y_0)\cdot (x-x_0,y-y_0).$$
* Řez grafu rovinou $z=f(x_0,y_0)$ je vrstevnice na úrovni $C$, řez tečné roviny je tečna k vrstevnici v rovině $z=C$. Rovnice této tečny je 
  $$ C=f(x_0,y_0)+\nabla f(x_0,y_0)\cdot (x-x_0,y-y_0),$$
  tj.
  $$ 0=\nabla f(x_0,y_0)\cdot (x-x_0,y-y_0).$$


![Tečna k vrstevnici](implicitni_1.png) 


<a href="animation.gif" rel="facebox" alt="Nahrava se ...">Animace</a>

</div>

# Implicitně definovaná funkce  (pokračování)


<div class='sloupce'>

* Normálový vektor tečny je 
  $$ \nabla f(x_0,y_0)=\left(\frac{\partial f (x_0,y_0)} {\partial x}, \frac{\partial f (x_0,y_0)}{\partial y}\right),$$
  k němu kolmý je vektor
  $$ \left(-\frac{\partial f (x_0,y_0)}{\partial y}, \frac{\partial f (x_0,y_0)}{\partial x}\right)$$
  a po znormování první komponenty dostáváme směrový vektor tečny ve tvaru 
  $$ \left(1, -\frac{\frac{\partial f (x_0,y_0)}{\partial x}}{\frac{\partial f (x_0,y_0)}{\partial y}}\right).$$
  Druhá komponenta tohoto vektoru je derivací funkce, která je dána implicitně rovnicí (1).
  To vše za podmínky, že první komponenta normálového vektoru je nenulová.
* Poznámka: bez újmy na obecnosti většinou při definici implicitní funkce bereme $C=0$. Vskutku,
  pokud definujeme $g(x,y)=f(x,y)-C$, potom je možno rovnici
  vrstevnice funkce $f$ na úrovni $C$ přepsat do tvaru $$g(x,y)=0. $$

![Tečna k vrstevnici](implicitni_2.png) 

</div>

# Implicitně definovaná funkce  (závěr)

\fi

<div class='sloupce'>

>  **Věta o implicitní funkci**: Uvažujme funkci $f(x,y)$ dvou proměnných, splňující v nějakém bodě
>  $(x_0, y_0)$ podmínku $f(x_0, y_0)=0$ a mající v okolí bodu $(x_0,
>  y_0)$ spojité parciální derivace.
>  Rovnice $$f(x,y)=0$$ vrstevnice na úrovni $0$ popisuje křivku
>   procházející bodem $(x_0, y_0)$.
>
> * Platí-li $$\frac{\partial f (x_0,y_0)}{\partial y}\neq 0,$$ je rovnicí
>    $f(x,y)=0$ v okolí bodu $(x_0, y_0)$ implicitně určena
>    **právě jedna spojitá funkce** $y=g(x)$ (tj. vrstevnice je
>    v okolí bodu $(x_0, y_0)$ grafem nějaké spojité funkce $g$).
> * Funkce $g$ z předchozího bodu **má v $x_0$ derivaci**
>   $$
>      g'(x_0)=-\frac{\frac{\partial f (x_0,y_0)}{\partial x}}{\frac{\partial f (x_0,y_0)}{\partial y}}.
>   $$


\iffalse
![Tečna k vrstevnici](implicitni_3.png) 
\fi

</div>



# Lokální extrémy funkce více proměnných

<div class='sloupce'>

Podobně jako pro funkce jedné proměnné definujeme i pro funkce více
proměnných **lokální extrémy** následovně: funkce má v daném
bodě **lokální minimum**, pokud v nějakém okolí tohoto bodu
neexistuje bod s menší funkční hodnotou a podobně, funkce má v bodě
**lokální maximum**, pokud v okolí tohoto bodu neexistuje bod
s vyšší funkční hodnotou. 

\iffalse

Funkce jedné proměnné určitě nemá v bodě lokální extrém, pokud má v
tomto bodě kladnou derivaci (protože potom funkce roste), nebo pokud
má v tomto bodě zápornou derivaci (protože potom funkce
klesá). Derivace v bodě kde nastává lokální extrém tedy musí být buď
nulová nebo nesmí existovat. Stejná myšlenková úvaha se dá provést pro
křivky vzniklé na řezech funkce dvou proměnných a proto platí
následující věta.

\fi

>  **Věta (Fermatova nutná podmínka pro lokální extrémy)**:
>  Jestliže funkce více proměnných má v nějakém bodě svůj lokální
>  extrém, pak každá parciální derivace, která v tomto bodě existuje,
>  je nulová.

*V bodě lokálního extrému hladké funkce je tedy nulový gradient.*


\iffalse 

![Pokud je některá z parciálních derivací nenulová, extrém nenastává](extrem_1.png) 

</div>

-----

#### Lokální extrémy funkce více proměnných (pokračování)

<div class='sloupce'>

![V bodě kde nastává extrém je každá parciální derivace která existuje nulová, tj. křivka na řezu má vodorovnou tečnu](extrem_2.png) 

![Nulovost parciálních derivací nemusí stačit k existenci lokálního extrému - funkce může mít sedlový bod](extrem_3.png) 

</div>

\fi

# Složené funkce

* Derivace složené funkce $f(x,y)$, kde $x=x(u,v)$, $y=y(u,v)$ je
  $$\frac {\partial f}{\partial u}=\frac{\partial f}{\partial x} \frac{\partial x}{\partial u}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial u}=  \nabla f \cdot \left( \frac{\partial x}{\partial u}, \frac{\partial y}{\partial u}\right).$$
* Derivace složené funkce $f(x,y,z)$, kde $x=x(t)$, $y=y(t)$, $z=z(t)$ (derivace podél křivky):
$$  \frac{\mathrm{d} f}{\mathrm{d} t}=\frac{\partial f}{\partial x}\frac{\mathrm{d} x}{\mathrm{d} t}+\frac{\partial f}{\partial y}\frac{\mathrm{d} y}{\mathrm{d} t}+\frac{\partial f}{\partial z}\frac{\mathrm{d} z}{\mathrm{d} t}
=
   \nabla f \cdot \left(\frac{\mathrm{d} x}{\mathrm{d} t}, \frac{\mathrm{d} y}{\mathrm{d} t}, \frac{\mathrm{d} z}{\mathrm{d} t}\right).
$$
 Je-li křivkou vrstevnice, je $f$ konstantní podél křivky, derivace je nulová, protože funkční hodnoty se nemění. Skalární součin je nulový a gradient $\nabla f$ je kolmý na tečný vektor 
k vrstevnici, tj. na vektor $\left(\frac{\mathrm{d} x}{\mathrm{d} t}, \frac{\mathrm{d} y}{\mathrm{d} t}, \frac{\mathrm{d} z}{\mathrm{d} t}\right)$.




# Druhá derivace

* Druhá derivace je derivace první derivace. U funkce dvou proměnných připadají v úvahu čtyři kombinace.
  $$
\frac{\partial}{\partial x}\frac{\partial}{\partial x}f,\quad 
\frac{\partial}{\partial x}\frac{\partial}{\partial y}f,\quad 
\frac{\partial}{\partial y}\frac{\partial}{\partial x}f,\quad 
\frac{\partial}{\partial y}\frac{\partial}{\partial y}f.
$$

> **Věta (Schwarzova).** Jsou-li smíšené derivace hladké na otevřené množině, jsou zde stejné, tj. platí  $$ \frac{\partial }{\partial x}
  \frac{\partial f}{\partial y}= \frac{\partial }{\partial y}
  \frac{\partial f}{\partial x}.$$

Vzhledem k této větě existují jenom tři druhé parciální derivace. Je tedy bezpečné psát
  $$
\frac{\partial^2}{\partial x^2}f,\quad 
\frac{\partial^2}{\partial x \partial y}f,\quad 
\frac{\partial^2}{\partial y^2}f,
$$
nebo
$$f''_{xx},\quad f''_{xy},\quad f''_{yy}.$$


\iffalse

# Separace proměnných



Některé funkce dvou proměnných je možno zapsat jako součin dvou funkcí
jedné proměnné, například $\varphi(x,y)=\sin(x^2+1)\frac{\ln y}{y}$. U některých funkcí toto možné není, například funkce
$\varphi(x,y)=x^2-y^2$. Pomocí parciálních derivací je možno podat
jednoduchou charakterizaci všech funkcí, majících výše uvedenou
vlastnost.

<div class='sloupce'>

>  **Věta**: Nechť funkce dvou proměnných $\varphi(x,y)$ je nenulová na konvexní
>  oblasti $G$ a má zde spojité všechny parciální derivace do řádu dva,
>  včetně.  Funkci $\varphi(x,y)$ je možno zapsat ve tvaru
>  $\varphi(x,y)=f(x)g(y)$, kde $f$ a $g$ jsou vhodné funkce jedné
>  proměnné právě tehdy, když je na množině $G$ nulový výraz 
>  $$
>    \varphi(x,y)\frac{\partial^2 \varphi (x,y)}{\partial y\partial x}-\frac{\partial \varphi (x,y)}{\partial x\vphantom{y}}\frac{\partial \varphi (x,y)}{\partial y}
>  $$
>   tj. pokud na množině $G$ platí $$\begin{vmatrix}\varphi & \frac {\partial \varphi}{\partial x}\\ \frac {\partial \varphi}{\partial y} &
> \frac {\partial^2 \varphi}{\partial x\partial y}\end{vmatrix}=0$$


 Naznačíme část důkazu. Pokud platí $$\varphi(x,y)=f(x)g(y),$$ je
  $$\ln \varphi(x,y)=\ln(f(x))+\ln(g(y)).$$ Derivací podle $x$ dostáváme
$$
    \frac {\frac{\partial }{\partial x}\varphi(x,y)}{\varphi (x,y)}=
    \frac{f'(x)}{f(x)}.
$$
  Protože pravá strana nezávisí na $y$, dostáváme derivováním podle $y$
$$
    \frac {\left(\frac{\partial^2 \varphi (x,y)}{\partial y\partial x}\right)\varphi(x,y)-\left(\frac{\partial \varphi (x,y)}{\partial x\vphantom{y}}\right)\left(\frac{\partial \varphi (x,y)}{\partial y}\right)}{\varphi^2(x,y)}=
    0
$$
  Výraz v čitateli je uveden v tvrzení věty.

</div>

\fi

# Totální diferenciál
* **Totálním diferenciálem** funkce $z=f(x,y)$ v bodě $(x_0, y_0)$ nazýváme výraz
$$      \mathrm{d}f=
\nabla f (x_0,y_0) \cdot (\mathrm{d}x,\mathrm{d}y)=\frac{\partial f (x_0,y_0)}{\partial x}\mathrm{d}x+\frac{\partial f (x_0,y_0)}{\partial y}\mathrm{d}y.
$$
* Máme-li vektorové pole $$\vec F(x,y)=(M(x,y),N(x,y)),$$ resp. máme-li výraz 
  $$      M(x,y)\mathrm{d}x+N(x,y)\mathrm{d}y,$$
  může nastat otázka, zda k tomuto výrazu existuje totální diferenciál, tj. zda existuje skalární funkce $f$, jejímž gradientem je vektorové pole  $\vec F$. Toto je důležitá otázka ve fyzice, protože umožňuje rozhodnout, ke kterému silovém poli je možno zavést potenciální energii.
Funkce $f$ se v tomto kontextu nazývá **skalární potenciál** vektorového pole nebo **kmenová funkce** diferenciálu.

>  **Věta**  (platí za předpokladu dostatečně hladkých funkcí na otevřené množině):  Vektor   $$\vec F(x,y) = \left(   M(x,y) , N(x,y)\right)$$ je gradientem nějaké funkce $f(x,y)$ právě tehdy když platí   $$      \frac{\partial }{\partial y}M(x,y)=\frac{\partial}{\partial x}N(x,y).$$ 

\iffalse

# Darcyho zákon a skalární potenciál

<div class='obtekat'>

![Tok vody v půdě je jedním ze základních předpokladů existence života. Zdroj: pixabay.com](darcy.jpg)

</div>

Darcyho zákon experimentálně prokázal, že při proudění tekutiny
pórovitým prostředím je pro mnoho látek za běžných situací tok úměrný
rozdílu tlaků. Proto se tento zákon používá například při studiu
proudění podzemní vody propustnými vrstvami půdy, vody dřevem, vzduchu
půdou, vody rostlinou a jejími částmi, ropy půdou a podobně. Rozdíl
tlaků může mít různý původ (jiná výška, jiný tlak vrstev z nadloží,
osmóza, kapilarita, koncentrace rozpuštěných látek apod) a tyto
faktory se sčítají. Pro pohodlí je někdy rozdíl tlaků přepočítáván v
některých oborech na ekvivalentní výškový rozdíl, což však činí tuto
veličinu poměrně těžko představitelnou, protože není spojena s jedním
konkrétním fyzikálním jevem. My se budeme držet tlaku.

Je-li $p$ tlak, je změna tlaku na jednotku délky ve směru osy $x$
rovna $\frac{\partial p}{\partial x}$ a tento rozdíl tlaků vyvolá
proudění ve směru osy $x$ o velikosti $$q_{xx}=-K_{xx}\frac{\partial
p}{\partial x},$$ kde $K_{xx}$ je konstanta úměrnosti z Darcyho zákona
a znaménko vyjadřuje, že tekutina teče z místa s vyšším tlakem do
místa s nižším tlakem.

Změna tlaku ve směru osy $x$ může v obecném *anizotropním* prostředí vyvolat
proudění i ve směru osy $y$ nebo $z$, opět existují konstanty $K_{xy}$
a $K_{xz}$ takové, že
$$q_{yx}=-K_{yx}\frac{\partial
p}{\partial x},\qquad q_{zx}=-K_{zx}\frac{\partial
p}{\partial x}.$$

Analogické vztahy platí i pro další směry a celkový tok ve směru osy
$x$ je dán součtem příspěvků, které vznikly tlakovým gradientem ve
směru jednotlivých os, tj.
$$q_x=-K_{xx}\frac{\partial
p}{\partial x}-K_{xy}\frac{\partial
p}{\partial y}-K_{xz}\frac{\partial
p}{\partial z}.$$
Proudění ve všech třech směrech je možné zapsat pomocí maticové rovnice
$$\begin{pmatrix}
q_x\\q_y\\q_z
\end{pmatrix}
=-\begin{pmatrix}
K_{xx} & K_{xy} & K_{xz}\\
K_{yx} & K_{yy} & K_{yz}\\
K_{zx} & K_{zy} & K_{zz}
\end{pmatrix}
\begin{pmatrix}
\frac{\partial p}{\partial x}\\
\frac{\partial p}{\partial y}\\
\frac{\partial p}{\partial z}
\end{pmatrix}.
$$
Matice $(K_{ij})$ má kladná vlastní čísla a je symetrická. To není
zcela snadné vidět, ale symetrie plyne z termodynamiky a z předpokladu
vratnosti procesů, pozitivní definitnost plyne z toho, že kapalina
teče do míst s nižším tlakem.  Díky těmto vlastnostem je možné pro
vhodně zvolenou soustavu souřadnic dosáhnout toho, že matice
$(K_{ij})$ je diagonální, tj.
$$\begin{pmatrix}
q_x\\q_y\\q_z
\end{pmatrix}
=-\begin{pmatrix}
K_{xx} & 0 & 0\\
0 & K_{yy} & 0\\
0 & 0 & K_{zz}
\end{pmatrix}
\begin{pmatrix}
\frac{\partial p}{\partial x}\\
\frac{\partial p}{\partial y}\\
\frac{\partial p}{\partial z}
\end{pmatrix}.
$$
V některých případech jsou vhodné souřadnice dány geometrií, například
díky vláknům dřeva můžeme psát Darcyho zákon ve tvaru s diagonální
maticí.  Je-li prostředí dokonce *izotropní* (stejné vlastnosti ve
všech směrech), platí $K_{xx}=K_{yy}=K_{zz}=K$ a rovnice má tvar
$$\begin{pmatrix}
q_x\\q_y\\q_z
\end{pmatrix}
=-K
\begin{pmatrix}
\frac{\partial p}{\partial x}\\
\frac{\partial p}{\partial y}\\
\frac{\partial p}{\partial z}
\end{pmatrix}.
$$
Je-li prostředí kromě izotropie i *homogenní* a $K$ nezávisí na prostorových souřadnicích, má Darcyho zákon tvar ještě o něco jednodušší
$$\begin{pmatrix}
q_x\\q_y\\q_z
\end{pmatrix}
=-
\begin{pmatrix}
\frac{\partial Kp}{\partial x}\\
\frac{\partial Kp}{\partial y}\\
\frac{\partial Kp}{\partial z}
\end{pmatrix}.
$$
Vidíme, že tok je záporně vzatým gradientem jisté fyzikální veličiny, která se v anglické literatuře nazývá *specific discharge potential*.
Matematicky je veličina $-Kp$ kmenovou funkcí toku $\vec q$.


\fi

# Laplaceův operátor


* <span class='red'>Laplaceův operátor</span> $\Delta$, je definován v\ kartézských souřadnicích a trojrozměrném prostoru vztahem
  $$
  \Delta f=\frac{\partial^2 }{(\partial x)^2}f+\frac{\partial^2 }{(\partial y)^2}f+\frac{\partial^2 }{(\partial z)^2}f.
  $$
  V prostorech jiné dimenze postupujeme analogicky, jenom vynecháme nebo přidáme derivace podle dalších proměnných.
* Označení symbolem $\Delta$ je stejné jako změna funkce $f$ a je nutné tyto dva významy symbolu $\Delta$
  nezaměňovat. Chceme-li se vyhnout nedorozumění, je možno pro
  označení Laplaceova operátoru používat $\nabla^2$ namísto $\Delta$.
* Laplaceův operátor vystupuje v problémech týkajících se
  elektrického nebo gravitačního potenciálu, difuze, nebo kmitů a
  šíření vln.
    * Vlnová rovnice popisující vlnění resp. chvění je rovnice
      $$\frac{1}{c^2} \frac{\partial ^2 u}{\partial t^2} = \nabla^2
      u.$$ Například u kmitání struny nebo membrány je v odvození této
      rovnice i lineární aproximace $\sin x\approx x$.
    * Vedení tepla v prostředí bez zdrojů nebo spotřebičů tepla je
      popsáno rovnicí $$\frac{\partial u}{\partial t}=D\nabla^2 u.$$
    * Při ustáleném vedení tepla je derivace podle času nulová a
      takové vedení tepla je popsáno rovnicí $$0=\nabla^2 u.$$ Stejná
      rovnice popisuje proudění obecně. Například proudění [podzemní
      vody](http://www.soilmanagementindia.com/soil/seepage-analysis/laplace-equation/laplace-equation-for-two-dimensional-flow-soil-engineering/137580)
      propustnými vrstvami půdy.


\iffalse

# Shrnutí vzorců pro výpočty



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
}

th {text-align: center;}
</style>

|Úloha                                                          |Postup                                                                              |
|---------------------------------------------------------------|------------------------------------------------------------------------------------|
|Najdi směr kolmý na vrstevnice funkce $f(x,y)$ v bodě $(x_0,y_0)$.| $\nabla f(x_0,y_0)$ |
|Najdi tečnu k vrstevnici funkce $f(x,y)$ v bodě $(x_0,y_0)$.| $\nabla f(x_0,y_0)\cdot(x-x_0,y-y_0)=0$ <br> (Přímka v rovině $z=f(x_0,y_0)$.)|
|Najdi tečnu k funkci dané implicitně rovnicí $f(x,y)=0$ v bodě $(x_0,y_0)$.| Totéž co předchozí případ. Musí navíc platit $f(x_0,y_0)=0$.|
|Najdi tečnou rovinu ke grafu funkce $f(x,y)$ v bodě $(x_0,y_0)$.| $z=f(x_0,y_0)+\nabla f(x_0,y_0)\cdot(x-x_0,y-y_0)$ |
|Najdi lineární aproximaci funkce $f(x,y)$ v okolí bodu $(x_0,y_0)$.| $f(x,y)\approx f(x_0,y_0)+\nabla f(x_0,y_0)\cdot(x-x_0,y-y_0)$ |
|Je $M\mathrm{d}x+N\mathrm{d}y$ totální diferenciál?<br> Existuje funkce $\varphi$ taková, že $\nabla\varphi=(M,N)$?| Platí následujíci vztah? $\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$|
|Je možno psát funkci $\varphi(x,y)$ ve tvaru $f(x)g(y)$ pro vhodné funkce $f$ a $g$?|Platí následujíci vztah? $\varphi \frac{\partial^2 \varphi}{\partial x \partial y}-\frac{\partial \varphi}{\partial x}\frac{\partial \varphi}{\partial y}=0$|

Použité označení:

* Výraz $\nabla f(x_0,y_0)$ je gradient v bodě $(x_0, y_0)$. Je nutno zderivovat funkci $f$, sestavit gradient v bodě $(x,y)$ a dosadit $x=x_0$ a $y=y_0$.
* Operace $(a,b)\cdot (c,d)=ac+bd$ je skalární součin vektorů.

\fi

<!--




# Lineární aproximace podruhé

* Lineární aproximací funkce $z=f(x,y)$ v bodě $(x_0, y_0)$ je 
  $$      f(x,y)\approx f(x_0, y_0)+\frac{\partial f (x_0,y_0)}{\partial x}(x-x_0)+\frac{\partial f (x_0,y_0)}{\partial y}(y-y_0)$$
  Pomocí gradientu:
  $$      f(x,y)\approx f(x_0, y_0)+\nabla f (x_0,y_0)(x-x_0,y-y_0)$$
* Tečná rovina:
  $$      z= f(x_0, y_0)+\nabla f (x_0,y_0)(x-x_0,y-y_0)$$
* Tečna k vrstevnici funkce $f(x,y)$ v bodě $(x_0,y_0)$
  $$      0= \nabla f (x_0,y_0)(x-x_0,y-y_0)$$
* Zobecnění předchozího pro funkci tří proměnných  $f(x,y,z)$ v bodě $(x_0,y_0,z_0)$
  $$      0= \nabla f (x_0,y_0,z_0)(x-x_0,y-y_0,z-z_0)$$
  Toto je možné použít k nalezení rovnice tečné roviny ke grafu funkce dvou proměnných, pokud funkci $z=g(x,y)$ přepíšeme do tvaru $$z-g(x,y)=0$$ a chápeme ji jako "vrstevnici" funkce 
  tří proměnných $f(x,y,z)=z-g(x,y)$ na úrovni $0$. (Ve skutečnosti se používá pojem ekvipotenciální plocha.)


# Proč je gradient kolmý na vrstevnice?

<div class='sloupce'>

Buď $z=f(x,y)$ funkce dvou proměnných a $\nabla f(x,y)$ její
gradient. Odvodíme vztah mezi vrstevnicemi a gradientem.

* Uvažujme bod $[x_0,y_0, f(x_0,y_0)]$ na grafu funkce $f(x,y)$ a vrstevnici
  procházející bodem $[x_0,y_0]$. Tuto vrstevnici napíšeme jako parametrickou
  křivku $$\begin{aligned}x&=x(t)\\y&=y(t)\end{aligned}$$
* Složená funkce $$F(t)=f(x(t),y(t))$$ je podél naší křivky konstantní
  (křivka je vrstevnicí a podél vrstevnice jsou konstantní funkční
  hodnoty)
* Platí $$\frac{\mathrm{d}F}{\mathrm{d}t}=0$$
  (derivace konstantní funkce je nula)
* Platí $$\frac{\mathrm{d}F}{\mathrm{d}t}= \frac{\partial f}{\partial x}\frac{\mathrm{d}
  x}{\mathrm{d} t}+\frac{\partial f}{\partial y}\frac{\mathrm{d}
  y}{\mathrm{d} t} $$ (derivace složené funkce více proměnných)
* Platí 
  $$\begin{aligned}0=\frac{\mathrm{d}F}{\mathrm{d}t}&=
  \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial
  y}\right)\cdot\left(\frac{\mathrm{d} x}{\mathrm{d} t},
  \frac{\mathrm{d} x}{\mathrm{d} t}\right) \\&= \nabla
  f(x,y)\cdot(x'(t),y'(t))\end{aligned}$$ (derivace konstanty z
   předešlého bodu, definice sklárního součinu, definice gradientu,
   zkrácené označení pro derivace funkce
  jedné proměnné)
* Vektory $\nabla f(x,y)$ a $(x'(t),y'(t))$ jsou kolmé (jejich
  skalární součin je nula). Zbývá zjistit, jak vypadá vektor
  $(x'(t),y'(t))$.


</div>

-----

### Vztah mezi gradientem a vrstevnicemi

<div class='sloupce'>
Z přechozího plyne

* Gradient je kolmý na vektor $(x'(t),y'(t))$
* Vektor $(x'(t),y'(t))$ je tečný k vrstevnici

Tedy gradient v daném bodě je kolmý na vrstevnici procházející tímto
bodem.

![Gradient je kolmý k vrstevnicím](../derivace/gradient.svg)

</div>


-->