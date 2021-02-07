% Divergence vektorového pole, rovnice kontinuity
% Robert Mařík
% 2020, 2021


> Anotace.
>
> * Představíme si univerzální nástroj umožňující popsat libovolný transportní děj v přírodě. Tedy transport energie (vedení tepla), transport vody (sušení dřeva, proudění podzemní vody, proudění tzv. mělké vody) a transport látky obecně (pohyb sedimentů, pohyb tektonických vrstev).
> * Aparát představený v této přednášce se věnuje základním principům transportních dějů. Naučíme se základní představu o fungování těchto dějů naformulovat matematicky. Vzniklé rovnice řešit nebudeme, což vůbec nevadí. Řešení za nás zvládnou počítače, role člověka je však nezastupitelná právě při formulaci modelu, což bude naším hlavním úkolem.
> * Během analýzy transportních jevů si představíme nový diferenciální operátor, operátor divergence. Vyjadřuje, zda tok zesiluje a nabírá na intenzitě (tj. z daného místa více vytéká, než teče dovnitř) nebo naopak.


> Prerekvizity.
>
> * Navážeme na využití vektorových funkcí a gradientu k popisu proudění látky nebo energie prostředím.
> * Ukážeme si, jak se matematicky odrazí v popisu izotropie nebo homogenita materiálu, jak se liší popis stacionárních a nestacionárních jevů, jak se liší popis materiálů s lineárními a nelineárními materiálovými vlastnostmi. Pod těmito pojmy je vždy vhodné si představovat konkrétní situace a pokud se budete při používání těchto pojmů cítit zaskočeni, můžete si oživit znalosti například na Wikipedii.
> * Zobecníme si rovnici vedení tepla v jedné dimenzi, kterou jsme si odvodili v úvodní přednášce. Je proto vhodné si základní fakta o této rovnici zopakovat.



# Transportní jevy

https://youtu.be/p1Qu89EKc94

  Pochopení a modelování transportních dějů je
  důležité pro většinu technických oborů. Podstata těchto dějů je často
  odlišná, přesto mají navenek podobné chování a tím je umožněn
  jednotný přístup při matematickém modelování.

Příklady transportních dějů

* povrchová voda
* podzemní voda
* teplo
* voda ve dřevě

Obecná bilance veličiny, která má zdroje a spotřebiče a je přenášena tokem vypadá následovně.

* Existuje veličina, spojitě rozložená v prostoru, charakterizující stav systému. Tuto veličinu budeme nazývat
    *stavovou veličinou* a její hustotu označíme $u$.
* Stavová veličina se může v prostoru přemisťovat *tokem* $\vec
    \jmath$.
* Stavová veličina může vznikat a zanikat.
    *Zdroje* i *spotřebiče* budeme
    uvažovat společně a jejich vydatnost rozlišíme
    znaménkem: spotřebiče budou zdroje se zápornou vydatností. Celkovou vydatnost zdrojů a spotřebičů v daném místě, tj.
    množství veličiny vygenerované na jednotku objemu (nebo plochy,
    nebo délky, podle počtu dimenzí v úloze) za jednotku času,
    označíme $\sigma$.


Zákon zachování (se zohledněním toku a zdrojů) je vlastně celková
bilance stavové veličiny. Přirozeným jazykem je možno tuto bilanci
formulovat následovně.  

> Přírůstek množství veličiny je součtem přírůstku způsobeného tokem a přírůstku ze zdrojů. Akumulace je přítok plus zisk z interních zdrojů.

Toto je jednoduchý, ale přitom neuvěřitelně silný nástroj, který
umožní popsat řadu zcela odlišných dějů. Pro použití v matematickém
modelu ale musíme jednotlivé pojmy kvantifikovat. Měřit rychlost, s
jakou se mění množství veličiny v daném místě umíme pomocí derivace
podle času. Měřit změny v toku přenášejícím sledovanou veličinu jsme se naučili jako jednu z prvních aplikací parciálních derivací: jedná se o záporně vzatou derivaci podle prostorové proměnné vynásobenou fyzikální materiálovou konstantou. Ještě se musíme naučit měřit změny v toku ve dvou nebo třech dimenzích.




# Změna toku vektorového pole

https://youtu.be/cXT6ULeZFJs

\iffalse 

<div class='obtekat'>

![Divergence a tok pole $\vec q=(0,Q, R)$ tělesem nenulového objemu. Tok je zobrazen vždy ve středu stěny. Červené vektory vstupují do krychle a příslušné toky se počítají záporně. Modré vystupují ven a počítají se kladně. V tomto případě je celková bilance kladná, z objemu více vyteče, než vteče dovnitř. Divergence je kladná. Pokud v krychli množství veličiny neubývá, musí tam být zdroj této veličiny.](divergence_kostka.png)

</div>

\fi

Budeme sledovat tok vektorového pole a bude nás zajímat, o kolik se tok v daném místě mění.

* Pro jednoduchost rozdělíme tok na tři nezávislé části ve směru jednotlivých os a vztáhneme vše k jednotkám času a průřezu, tj. budeme uvažovat hustotu toku nějaké fyzikální veličiny.
* Je-li tato hustota toku popsána vektorovým polem  $\vec q=(P,Q,R)$ v jednotkách kilogram na metr čtvereční za sekundu, znamená to, že kolmým průřezem jednotkového obsahu projde za jednotku času $P$ kilogramů sledované látky, jejíž tok popisujeme. Často se pracuje i s objemovým tokem, kdy množství neměříme v kilogramech ale v metrech krychlových a například při ustáleném proudění v trubici (hydrodynamika) je tok roven vektoru rychlosti a při proudění porézním materiálem (proudění podzemní vody) je roven filtrační rychlosti.
* Uvažování toku v souřadnicích nám umožní tok rozdělit na nezávislé toky ve směru os. Můžeme si pro jednoduchost představit tři trubky, ve směru každé osy jednu. Funkce $P$ udává tok v trubce mířící směrem v ose $x$ (v kladném směru kladný tok a naopak) a potřebujeme zjistit, jestli tento tok narůstá nebo slábne. To jsme již řešili v případě toku tepla u rovnice vedení tepla v úvodní přednášce. Derivace $\frac{\partial P}{\partial x}$ udává, o kolik studovaná komponenta toku v daném místě vzroste a tento nárůst je vztažený na jednotku délky.
* Ve směru osy $y$ máme tok vyjádřený veličinou $Q$ a proto nás pro popis zesilování či zeslabování zajímá $\frac{\partial Q}{\partial y}$.
* Analogicky $\frac{\partial R}{\partial z}$ ve směru osy $z$.
* Celková změna toku bude součtem všech tří příspěvků. Pokud je kladná, znamená to, že tok zesiluje. Z daného místa více veličiny vytéká, než kolik teče dovnitř. Pokud je záporná, je tomu naopak. Jestli se v případě nerovnováhy v daném místě může proudící veličina tvořit nebo spotřebovávat nebo akumulovat nebo jestli v daném místě může ubývat již z čisté matematiky nezjistíme. Záleží na charakteru proudící veličiny a na okolnostech s tímto prouděním spojených. Tuto informaci nám pro další popis musí dodat externí věda (obecná fyzika, fyzika materiálu, fyzika životního prostředí, hydrologie, pedologie, ...).
* Při preciznější argumentaci dávající do souvislosti parciální derivace jednotlivých komponent toku s tím, co se reálně s vektorovým polem děje, je nutné si pomoci stejně jako u derivací, tj. uvažovat ne dané místo, ale jistý konečně velký objem (viz obrázek), vztáhnout dané veličiny na jednotku objemu a rozměry tohoto objemu limitně stáhnout k nule. Toto však již přesahuje ambice v našem kurzu a jedná se o formalismus, kterému se vyhneme přímým představením hotového výsledku.

<!--
Budeme sledovat tok vektorového pole ze zvoleného 
místa. Vyjádříme bilanci, o kolik je větší tok vektorového pole z daného místa ven ve srovnání s tokem tohoto pole dovnitř (viz krychlička na obrázku). Protože
záleží na objemu, ve kterém tok sledujeme, je  vztáhneme tento tok na
jednotku objemu.

Fyzikálně tok ven uvažujeme jako kladný a tok dovnitř jako záporný. Velikost toku rovinnou plochou určíme jako součin vektorového pole v tomto místě a  obsahu plochy.
Celkový tok $\vec q=(0,q_y,q_z)$ do krychle na obrázku je součtem toků levou boční stěnou a dolní stěnou, tj. 
$$Q_{in}=-q _y\Delta x \Delta z - q _z\Delta x \Delta y.$$
Podobně tok ven z krychle je  $$Q_{out}=\left(q_z+\frac {\partial q_z}{\partial z}\Delta z\right)\Delta x\Delta y + \left(q_y+\frac {\partial q_y}{\partial y}\Delta y\right)\Delta x\Delta z$$
a celková bilance je 
$$Q_{in}+Q_{out}=
\left(\frac {\partial q_y}{\partial y}+\frac {\partial q_z}{\partial z}\right)\Delta x\Delta y\Delta z.
$$
V případě proudění i v ose $x$ bude přítomen ještě další analogický člen charakterizující tuto dodatečnou položku. 

-->

# Divergence

https://youtu.be/ejDQx3QjgfI

Výše uvedenými úvahami je motivována následující definice a věta. (Definice je maličko nepřesná, protože nemáme nástroje pro pečlivější formulaci.)

> Definice (divergence). *Divergence* vektorového pole $\vec F$ v daném bodě je převis toku vektorového pole z tohoto místa nad tokem do tohoto místa. Tento tok se počítá přes hranici infinitezimálně malého referenčního tělesa a je vztažený na jednotku objemu. Divergenci vektorového pole $\vec F$ označujeme $\mathop{\mathrm{div}}\vec F$ nebo $\nabla \cdot \vec F$.


> Věta (výpočet divergence).
> Pro vektorovou funkci $$\vec F=(P,Q,R)=P\vec i + Q\vec j + R\vec k,$$ kde $P$, $Q$ a $R$ jsou funkce tří proměnných $x$, $y$ a $z$ vypočteme divergenci vztahem 	  $$\mathop{\mathrm {div}}\vec F=\nabla\cdot\vec F=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}.$$
> Pro vektorovou funkci dvou proměnných vypočteme divergenci analogicky, pouze chybí třetí člen. 

> Poznámka (linearita divergence). Divergence zachovává součet a násobení konstantou, tj. pro libovolné vektorové funkce $\vec F$ a $\vec G$ a konstantu $c$ platí
> $$\nabla \cdot (\vec F+\vec G)=\nabla \cdot \vec F +\nabla \cdot \vec G, \qquad \nabla \cdot (c\vec F)=c\nabla \cdot \vec F.$$


> Poznámka (fyzikální interpretace divergence). Vektorové pole používáme k modelování toku veličin, které nás zajímají (teplo v materiálu, tekutina nebo chemická látka v materiálu, voda nebo plyn v půdě a podobně). Divergence vektorového pole udává tok z jednotkového objemu látky v daném místě. Udává, jestli se v daném místě a čase tok nabývá na intenzitě (kladná divergence) nebo ustává (záporná divergence). Tento efekt může být způsoben tím, že veličina přenášená tímto polem se v daném místě buď kumuluje, nebo ubývá a také tím, že daná veličina v bodě může vznikat nebo zanikat.

Divergence je lokální veličina. Udává informaci o daném bodě. Pro měření však je nutné mít konečný objem a pro stanovení toku konečně velkou hranici. Vzájemný vztah mezi lokální veličinou a konečným objemem je založený na předpokladu, že podmínky se nemění skokem a okolí každého bodu jsou nepříliš odlišné od podmínek v okolních bodech.

> Poznámka (fyzikální interpretace divergence v měřitelných pojmech). Protože tok přes hranici umíme měřit u těles, představíme si okolo bodu který nás zajímá, těleso. Například kouli nebo krychli. Poté určíme tok přes hranici. Tok hranicí ven počítáme kladně a dovnitř záporně. Celkový tok hranicí určíme jako součet přes všechny části hranice. Podíl celkového toku přes hranici tělesa a objemu tohoto tělesa je odhad pro divergenci v daném bodě. Naopak, ze známé divergence je možno odhadnout zesílení toku v malé oblasti okolo studovaného bodu jako součin divergence a objemu (nebo obsahu ve 2D) oblasti.

Přesnou divergenci získáme postupem uvedeným v předchozí poznámce, pokud limitním přechodem stáhneme rozměry tělesa k nule. 

Pokud se daném místě množství veličiny nemění s časem, tj. žádná veličina se tam neakumuluje ani neubývá, mluvíme o stacionárním proudění a stacionárním poli. Situace se zjednoduší, protože potom divergence souvisí jenom s přítomností zdrojů a spotřebičů.

> Poznámka (praktická interpretace divergence stacionárního pole). Pokud při ustáleném proudění je v některém místě divergence kladná, znamená to, že v tomto místě musí být zdroj této veličiny. Pokud je záporná, je v daném místě spotřebič. Pro pohodlí při popisu toku bereme spotřebiče jako záporné zdroje. Vektorové pole, jehož divergence je rovna nule, se nazývá **nezřídlové pole**. To proto, že pokud toto pole popisuje ustálený tok, tak se jedná o tok v prostředí bez zdrojů a spotřebičů.

Ze střední školy z fyziky umíme modelovat vektorové pole pomocí siločar. Ty začínají ve zdrojích a končí ve spotřebičích. Siločáry stacionárního nezřídlového pole nikde nezačínají ani nekončí a jsou to uzavřené křivky.  Například stacionární magnetické pole je nezřídlové. Absence zdrojů magnetického pole se projevuje tak, že rozříznutím tyčového magnetu vzniknou dva menší plnohodnotné magnety. Nevznikne samostatný jižní pól a samostatný severní pól magnetu. To je rozdíl oproti poli elektrickému, kdy rozdělením tyče s opačně nabitými konci vznikne jedna kladně nabitá a jedna záporně nabitá tyč poloviční délky.

# Výpočet divergence

Viz [cvičení](http://user.mendelu.cz/marik/am/slidy/cviceni/cviceni03.md.html). Jedná se o prosté derivování se následným sečtením derivací.


# Rovnice kontinuity

https://youtu.be/HiOmERpTdV0

\iffalse 

<div class='obtekat'>

![V celkové bilanci se nemusí nutně uplatnit všechny tři členy. Například při studiu tepelné vodivosti dřevěných panelů se měří tok tepla po dosažení rovnovážného ustáleného stavu, tj. derivace podle času je nulová. Na obrázku měřící zařízení ve VCJR v Útěchově.](stacionarni_vedeni_tepla_Utechov.jpg)

</div>

\fi 


* Přírůstek stavové veličiny za jednotku času v jednotkovém objemu
  (nebo ploše, nebo délce, podle dimenzionality úlohy) je derivace
  hustoty $u$ podle času.
  $$\text{Přírůstek}=\frac{\partial u}{\partial t}$$
*  Přírůstek veličiny v jednotkovém objemu (nebo ploše, nebo délce) za
  jednotku času způsobený tokem $\vec \jmath$ je záporně vzatá divergence
  vektorového pole $\vec \jmath$. Tento přírůstek je způsobený snížením
  toku, proto má předřazeno záporné znaménko.
$$    \text{
        Přírůstek způsobený tokem
}=-\nabla\cdot \vec \jmath$$

Matematickou formulací celkové bilance  je **rovnice kontinuity**.
$$
      {\frac{\partial u}{\partial t}=\sigma -\nabla\cdot \vec \jmath}   $$

    

>Poznámka (fyzikální interpretace členů rovnice kontinuity).
>
>* Člen $\frac{\partial u}{\partial t}$ udává, jak rychle se roste hustota stavové veličiny $u$ v daném místě a čase.
>* Člen $\sigma$ udává vydatnost zdrojů stavové veličiny, přičemž spotřebiče jsou uvažovány jako zdroje záporné vydatnosti. Tento člen tedy udává, kolik stavové veličiny v tomto místě vzniká v jednotkovém objemu za jednotku času.
>* Člen $\nabla\cdot \vec j$ udává v daném bodě změnu ve velikosti proudění přenášejícím stavovou veličinu. Přesněji, udává, o kolik více veličiny z daného místa vyteče ve srovnání s množstvím veličiny, které do tohoto místa vteče. Jinak řečeno, udává, o kolik zesílí v daném místě tok $\vec \jmath$. My potřebujeme mít zachyceno zeslabení (množství které chybí v toku se "použije" na akumulaci veličiny v daném místě) a proto uvažujeme záporně vzatou divergenci, tj. $-\nabla\cdot \vec j$.
>* Pokud zdroje stavové veličiny neexistují, jedná se o *bezzdrojovou rovnici* a klademe $\sigma=0$.
>* Pokud studujeme systém v ustáleném stavu, kdy se stavová veličina nemění v čase, je člen $\frac{\partial u}{\partial t}$ na levé straně nulový. V tomto případě mluvíme o *stacionárním stavu* a *stacionární rovnici kontinuity*. Stacionární rovnice kontinuity typicky popisuje systémy, které byly dostatečně dlouhou dobu ve stabilních podmínkách a dosáhly rovnovážného stavu.
>* Viděli jsme, že za určitých podmínek mohou některé členy v rovnici kontinuty chybět. Naopak člen $\nabla\cdot \vec j$ charakterizující změny v toku je v rovnici kontinuity přítomen vždy. Bez něj by rovnice kontinuity ztratila smysl (resp. redukovala by se na triviální případ, kdy veličina v daném místě vzniká danou rychlostí a zůstává zde, tj. problém řešitelný čistě integrováním).


V matematice často rovnici kontinuity uvažujeme ve výše uvedeném tvaru.  Při
praktickém použití většinou preferujeme názornou interpretaci
jednotlivých veličin a proto se v rovnici mohou objevit další
konstanty úměrnosti, které umožní sladit jednotky a fyzikální
interpretaci členů. Někdy se naopak snažíme konstanty co nejvíce
redukovat metodami transformace popsanými v přednášce o diferenciálních rovnicích. Proto volíme vhodné násobky veličin
vystupujících v matematické formulaci tak, aby se co nejvíce konstant
eliminovalo, případně shluklo do jediné veličiny. Zkušenosti ukazují,
že je vhodné volit veličiny bezrozměrné. Například v publikaci
P. Horáček, Fyzikální a mechanické vlastnosti dřeva I je zavedena
[bezrozměrná vlhkost, bezrozměrný čas a bezrozměrná
vzdálenost](https://is.mendelu.cz/eknihovna/opory/zobraz_cast.pl?cast=9180;lang=cz)
na straně 61 pro rovnici popisující difuzi a [charakteristická délka,
Biotovo číslo (bezrozměrná tepelná vodivost) a bezrozměrná teplota,
bezrozměrný čas a bezrozměrná
vzdálenost](https://is.mendelu.cz/eknihovna/opory/zobraz_cast.pl?cast=9182;lang=cz)
pro rovnici popisující vedení tepla na stranách 88 a 89.

V této rovnici není zahrnut případ, kdy se veličina přenáší ještě i prouděním hmotného prostředí (konvekce).


# Rovnice mělké vody

<div class='obtekat'>

\iffalse 

![Rovnici kontiuity známe ze středoškolské fyziky pro ustálené proudění. Naše obecnější formulace umí zachytit i nestacionární stav. Zdroj: pixabay.](ricka.jpg)

\fi

</div>



Rovnici kontinuity můžeme použít pro popis vody v řečišti. Úloha je jednodimenzionální a tok $Q$ je skalární veličina. Divergence toku se díky jednodimenzionálnosti redukuje na derivaci podle prostorové proměnné $\frac{\partial Q}{\partial x}$. Zachovávající se veličinou je množství vody. Hustota zachovávající se veličiny je množství vody na metr délky toku, tj. \textit{průtočný průřez} $A$ (obsah průřezu říčního toku  v daném místě). Zdroje zpravidla neuvažujeme, tj. $\sigma=0$. Rovnice kontinuity má potom tvar 
$$
      {\frac{\partial A}{\partial t}= - {\frac{\partial Q}{\partial x}}}
$$
a nazývá se Saint-Venantova rovnice nebo též *rovnice mělké vody*. Tato rovnice se používá při popisu *proudění v korytě* nebo při modelování *vln tsunami*.



# Difuzní rovnice

https://youtu.be/p2FTgyAWzA4

Difuzní rovnice je rovnice kontiuity s dosazeným konstitučním vztahem
pro tok.  Použijeme-li pro kvantifikaci souvislosti toku a gradientu
lineární aproximaci, je možné psát
$$      \vec \jmath=-D\nabla u,$$
kde $D$ konstanta
úměrnosti. Pokud tok $\vec \jmath$ a gradient $\nabla u$ leží v jedné přímce,
je $D$ reálné číslo, jinak je $D$ matice. Například při
studiu pohybu vody ve dřevě se voda řídí nejen směrem maximálního
poklesu vlhkosti, ale stáčí se současně do podélného směru, ve kterém dřevo
vede vlhkost nejlépe. V takovém případě je $D$ matice. 
Spojením rovnice kontinuity
$$
      {\frac{\partial u}{\partial t}=\sigma -\nabla\cdot \vec \jmath}   $$
a vztahu  pro tok stavové veličiny dostáváme rovnici
$$
      {\frac{\partial u}{\partial t}=\sigma - \nabla\cdot \bigl(-D\nabla u\bigr)}.$$
      Tuto rovnici je možno upravit na tvar
$$
      {\frac{\partial u}{\partial t}=\sigma + \nabla\cdot \bigl(D\nabla u\bigr)},$$
který se nazývá *difuzní rovnice*.

>Poznámka (fyzikální interpretace difuzní rovnice).
>
>* Člen $\frac{\partial u}{\partial t}$ udává, jak rychle se mění
   hustota stavové veličiny $u$. Je stejný jako v rovnici kontinuity.
>* Člen $\sigma$ udává vydatnost zdrojů stavové veličiny. Je stejný jako v rovnici kontinuity.
>* Člen $\nabla u$ udává nerovnoměrnost v prostorovém rozložení stavové veličiny. Pomocí difuzní matice $D$ a konstitutivního zákona tuto nerovnoměrnost přepočítáme na tok, který se snaží uvažovanou nerovnoměrnost vyrovnat. Tento tok je reprezentován výrazem $-D\nabla u$.
>* Záporně vzatá divergence toku udává, jak tok v daném místě ztrácí na intenzitě. Vzhledem k zápornému znaménku v konstitutivním zákoně má záporně vzatá divergence tvar $$\nabla\cdot \bigl(D\nabla u\bigr).$$ Představuje přírůstek hustoty stavové veličiny v daném místě za jednotku času, způsobený zeslábnutím toku.
>* Rovnice jako celek vyjadřuje, že navýšení hustoty stavové veličiny (tj. množství stavové veličiny v jednotkovém objemu) je součtem navýšení díky zdrojům a navýšení díky zeslabení toku v daném místě.

V jednorozměrném případě (proudění jedním směrem) gradient splývá s parciální derivací a má jenom jednu komponentu. Ztrácí tedy vektorový charakter a proto nemá smysl $D$ uvažovat maticově, prostředí je automaticky izotropní. Divergence se v takovém případě také redukuje na parciální derivaci a rovnice difuze v jedné dimenzi má tvar
$$
      {\frac{\partial u}{\partial t}=\sigma + \frac{\partial }{\partial x} \left(D\frac{\partial u}{\partial x}\right)}.$$
To jsme viděli již v první přednášce.

ww:problems/difuzni_rce/interpretace_clenu.pg

# Vedení tepla

\iffalse

<div class='obtekat'>

![Stromy umí ochlazovat své okolí. Ulice v Melbourne vyfocená termokamerou to dokazuje. A difuzní rovnice toto dokáže modelovat. Photograph: City of Melbourne. Zdroj: theguardian.com.](teplo.jpg)

</div>

\fi

Důležitým speciálním případem difuzní rovnice je rovnice vedení tepla.
Stavovou veličinou, která se zachovává v úlohách s vedením tepla, je vnitřní energie ve
formě tepla. Zpravidla nemá smysl uvažovat členy vyjadřující
zdroje, tj. $\sigma =0$. Protože teplo neměříme přímo, je vhodnější
model formulovat pro teplotu $T$. Jsou-li $\varrho$ a $c$ po řadě hustota a měrná tepelná kapacita materiálu, má člen vyjadřující změnu hustoty
energie v daném místě tvar
$\varrho c\frac{\partial T}{\partial t}.$ Úměrnost mezi gradientem
teploty a tokem tepla  zprostředkovává
*Fourierův zákon*. Difuzní rovnice má v tomto případě tvar
$${\varrho c\frac{\partial T}{\partial t}=  \nabla\cdot\bigl(k\nabla T\bigr)}$$

> Poznámka (interpretace rovnice vedení tepla).
>
>* Veličina $\frac{\partial T}{\partial t}$ udává rychlost růstu teploty tělesa a koeficient $\rho c$ tuto hodnotu přepočítává na údaj, jak rychle roste vnitřní energie tělesa (kinetická energie molekul.)
>* Výraz $k\nabla T$ udává (až na znaménko), jak se nerovnoměrnost v rozložení teploty vyrovnává tokem tepla. Přesněji, tok tepla je $-k\nabla T$.
>* Člen $\nabla\cdot(k\nabla T)$ udává, kolik tepla z celkového toku v daném místě zůstává a podílí se na zvýšení teploty. Vzhledem k absenci zdrojů je to také jediný mechanismus, jak v daném místě může vnitřní energie přibývat či ubývat.
>* Rovnice jako celek vyjadřuje to, že pokud z daného místa více energie odtéká, než kolik do místa proudí, dojde v tomto místě k odpovídajícímu snížení teploty. V tomto bodě je totiž divergence toku $\nabla\cdot (-k\nabla T)$ kladná a výraz z rovnice $\nabla\cdot (k\nabla T)$ je proto záporný.

\iffalse

<div class='obtekat'>

![Na rozhraní vrstev ve vrstveném materiálu je spojité teplotní pole a tok tepla.  Zdroj: Cengel, Ghajar: Heat and Mass Transfer.](vrstvy.png)

</div>

\fi


Tato rovnice je zobecnění rovnice vedení tepla v jedné dimenzi, kterou jsme
odvodili primitivními prostředky (jenom pomocí parciálních derivací, bez gradientu a divergence) ve tvaru
$$\rho c\frac{\partial T}{\partial t}=\frac{\partial}{\partial x}\left(k\frac{\partial T}{\partial x}\right)$$
v úvodní přednášce.

Rovnice vedení tepla se používá například při *tepelné ochraně budov*, při modelování *tepelných ostrovů* v krajině, při *tepelné modifikaci dřeva*, nebo při studiu *permafrostu*. 

V literatuře věnované problematice dřeva se rovnice vedení tepla ve dřevě označuje jako Druhý Fourierův zákon (P. Horáček, Fyzikální a mechanické vlastnosti dřeva I, str. 88).

V některých případech nemusí být člen charakterizující zdroje
nulový. Teplo může vznikat například při tření nebo při průchodu
elektrického proudu transformací z jiného druhu energie. Dále teplo vzniká například při betonování po [přidání vody do cementu](http://www.ebeton.cz/pojmy/hydratacni-teplo), známý je problém jak [uchladit Hooverovu přehradu](http://www.ebeton.cz/encyklopedie/hooverova-prehrada) při stavbě.



# Rovnice vedení tepla ve 2D v různých podmínkách

\iffalse

<div class='obtekat'>

![Teplotní modifikace dřeva ve VCJR v Útěchově. Díky jednoduché geometrii vzorků je možno provést i přesný analytický výpočet teplotního pole. Výřez ukazuje detail čtyř vzorků. Jeden z nich je nařezán šikmo. V takovém případě je výpočet mnohem obtížnější než u vzorků, jejichž tvar respektuje anatomické směry ve dřevě. Zdroj: J. Dömény.](VCJR_modifikace_pravidelne.jpg)

![Teplotní modifikace šindele ve VCJR v Útěchově. Řídí se stejnou rovnicí jako hranoly na obrázku výše. Vinou komplikovaného tvaru je však matematické modelování teplotního pole možné jenom numerickou cestou. Skutečně, v podobných úlohách hraje geometrie úlohy důležitou roli a netriviální geometrie zpravidla znemožní efektivní řešení analytickou cestou. Zdroj: J. Dömény.](VCJR_sindel.jpg)

![Nestacionární rovnice vedení tepla. Měření teplotních charakteristik pomocí sledování odezvy na teplotní impuls na ÚNOD LDF MENDELU. Zdroj: R. Slávik.](rtb.png)



</div>

\fi

Uvažujme rovnici vedení tepla ve dvou rozměrech a v prostředí bez zdrojů.
$$\rho c\frac{\partial T}{\partial t}=\nabla \cdot (k\nabla T)\tag{***}$$

## Stacionární stav

Stacionární stav znamená, že stavové veličiny nezávisí na čase. Derivace podle času je v takovém případě nulová. Rovnice (***) se redukuje na 
$$\nabla \cdot (k\nabla T)=0.$$


## Homogenní izotropní materiál a lineární materiálové vztahy

Materiál má ve všech místech (homogenní) a ve všech směrech (izotropní) stejné vlastnosti.
Veličina $k$ je reálná skalární veličina (konstanta).

Podle pravidla derivace konstantního násobku se rovnice (***) redukuje na  
$$\rho c\frac{\partial T}{\partial t}=k\nabla \cdot (\nabla T)$$
a ve složkách
$$\rho c\frac{\partial T}{\partial t}=k\left(\frac{\partial^2 T}{\partial x^2}+\frac{\partial^2 T}{\partial y^2}\right).$$

\iffalse

Pro $\tau=\frac{kt}{\rho c}$ (změna jednotky času) dostáváme
$$\frac{\partial T}{\partial \tau}=\frac{\partial^2 T}{\partial x^2}+\frac{\partial^2 T}{\partial y^2}.$$

\fi

## Ortotropní materiál, nehomogenní nebo nelineární

Materiál má dva charakteristické směry související s rovinami
symetrie. Zvolíme soustavu souřadnic tak, aby osy byly orientovány ve
směru vlastních vektorů.

Veličina $k$ je diagonální matice. Pro $$k=\begin{pmatrix}k_x & 0\\ 0& k_y\end{pmatrix}$$ je tvar rovnice (***) ve složkách
$$\rho c\frac{\partial T}{\partial t}=\frac{\partial }{\partial x}\left(k_x\frac{\partial T}{\partial x}\right)
+\frac{\partial }{\partial y}\left(k_y\frac{\partial T}{\partial y}\right).$$



## Homogenní ortotropní materiál a lineární materiálové vztahy

Materiál má dva charakteristické směry související s rovinami symetrie a materiálové charakteristiky jsou ve všech místech stejné a nezávislá na $T$.
Stejné jako předchozí případ, ale $k_x$ a $k_y$ jsou konstanty. Podle pravidla pro derivaci konstantního násobku se rovnice (***) redukuje na 
$$\rho c\frac{\partial T}{\partial t}=k_x\frac{\partial^2 T}{\partial x^2}+k_y\frac{\partial^2 T}{\partial y^2}.$$


# Voda v porézním materiálu 

\iffalse

<div class='obtekat'>

![Difuzní rovnice se používá k modelování sušení dřeva. Zdroj: pixabay.com.](drevo.jpg)

</div>

\fi



V porézním materiálu voda prostupuje materiálem a zachovává se její
množství, což bude stavová veličina. Hustotu tohoto množství, tj. obsah vody v jednotce
objemu, označíme $c$ a pro tuto veličinu formulujeme matematický
model. Zdroje neuvažujeme. Úměrnost mezi gradientem koncentrace vody a
jejím tokem zprostředkovává *Fickův
zákon*. Modelem je potom  difuzní rovnice bez zdrojů.
$$
      {\frac{\partial c}{\partial t}= \nabla\cdot \bigl(k\nabla c\bigr)}
	  $$
  Tato rovnice se používá například při modelování procesu
  *sušení dřeva* v sušárnách nebo při modelování *dřeva
    ve vlhkém prostředí*. Stejná rovnice napsaná pro vzduch se používá
  k modelování proudění v atmosféře při *předpovídání počasí*.

V literatuře věnované problematice dřeva se rovnice difuze použitá na modelování vlhkosti ve dřevě označuje jako Druhý Fickův zákon (A. Požgaj a kol., Štruktúra a vlastnosti dreva, str. 202, P. Horáček, Fyzikální a mechanické vlastnosti dřeva I, str. 60).

V praxi je dřevo často s jistou přesností homogenní, ale difuzní
koeficient dřeva závisí na vlhkosti, tedy vztah mezi gradientem
vlhkosti a difuzním tokem není lineární. Přesto i v tomto případě
používáme Fickův zákon, ovšem složky difuzního koeficientu
nepovažujeme za konstanty, jsou závislé na $c$ a jejím prostřednictvím
i na $x$.


# Rovnice podzemní vody

\iffalse

<div class='obtekat'>

![Difuzní rovnice umí popsat proudění podzemní vody. Díky tomu dokážeme zabránit kontaminacím pitné vody z chemických provozů. Zdroj: pixabay.com.](voda.jpg)

</div>

\fi


Proudění podzemní vody je vlastně úloha s řekou se zasypaným
korytem. Taková voda teče ve srovnání s povrchovou vodou velmi pomalu,
protože prosakuje půdou. Prostor, kde se podzemní voda nachází, se
nazývá *zvodeň*. Stejně jako řeka v korytě na povrchu, i voda
v podzemní zvodni teče v jistém smyslu "z kopce". V tomto případě
však kromě nadmořské výšky může hrát roli i rozdíl tlaků nebo další
efekty. Vliv všech těchto efektů shrnujeme do jediného pojmu
*piezometrická výška*. Směr "z kopce" pro podzemní vodu je
poté směr poklesu piezometrické výšky. V daném místě se může voda
hromadit, to poznáme nárůstem hladiny spodní vody. Také může
z hlediska zvodně část vody zanikat, například pokud je zde čerpaná
studna nebo průsak do jiné zvodně. Voda může ve zvodni i vznikat,
například zasakovacím vrtem nebo průsakem dešťových srážek. Pokud do
celkové bilance započteme rozdíl mezi přítokem a odtokem a všechny
zdroje a spotřebiče, množství vody se zachovává.

Podzemní zvodeň je typickým porézním materiálem, přesto k modelování
vody v tomto prostředí přistupujeme speciálním způsobem. Úloha se většinou uvažuje ve dvou dimenzích, protože
horizontální rozměry zvodně jsou mnohem větší než její
hloubka. Zachovává se množství vody, ale stejně
jako u vedení tepla je výhodné formulovat model pro lépe
měřitelnou veličinu, *piezometrickou výšku*
$h$. Přírůstek množství podzemní vody za časovou jednotku na jednotkové ploše v daném
místě zvodně má tvar $S_S \frac{\partial h}{\partial t}$, kde $S_S$ je
*specifická zásobnost*.  Úměrnost mezi gradientem piezometrické výšky a
filtračním tokem byla prokázána experimentálně a je známa jako *Darcyho
zákon*. Difuzní rovnice  má (s konstantou úměrnosti $T$, *transmisivitou*) tvar
$$ {S_S\frac{\partial h}{\partial t}=  \sigma + \nabla\cdot \bigl(T\nabla h\bigr).}$$ Tato rovnice se nazývá *rovnice podzemní vody*. Zdroje jsou nejčastěji zasakovací nebo odvodňovací vrty, dále studny, poldry, výkopy nebo zářezy. Informace získané z rovnice podzemní vody se využívají například
  k ochraně lomů, dolů a stavebních jam před *zaplavením*, k hospodaření s *pitnou vodou*,  k ochraně před šířením *kontaminace z chemických
  provozů*. Aplikace jsou dále v detekci zdroje kontaminace pitné vody a odhadu rychlosti  šíření kontaminace, včetně 
*kontaminace slanou mořskou vodou* v přímořských oblastech.

U proudění s napjatou hladinou (mezi dvěma nepropustnými vrstvami, angl. *confined aquifer*) transmisitiva závisí pouze na fyzikálních vlastnostech zvodně. Například pro homogenní izotropní materiál je konstantní. U proudění s volnou hladinou (bez horní nepropustné vrstvy, angl. *unconfined aquifer*) je transmisivita úměrná tloušťce vrstvy obsahující vodu. Zpravidla nulovou hodnotu piezometrické hladiny volíme na dolní nepropustné vrstvě a potom platí $T=kh$, kde $k$ závisí pouze na fyzikálních vlastnostech půdy. Proto se často rovnice podzemní vody pro proudění s volnou hladinou zapisuje ve tvaru
$$ {S_S\frac{\partial h}{\partial t}=  \sigma + \nabla\cdot \bigl(kh\nabla h\bigr).}$$

# Laplaceův operátor

> Definice (Laplaceův operátor). Laplaceovým operátorem $\nabla ^2$ rozumíme divergenci gradientu, tj. $$\nabla^2 f=\nabla\cdot(\nabla f).$$

* V\ kartézských souřadnicích a trojrozměrném prostoru je Laplaceův operátor $\nabla^2$ dán  vztahem
  $$
  \nabla^2 f=\frac{\partial^2 }{\partial x^2}f+\frac{\partial^2 }{\partial y^2}f+\frac{\partial^2 }{\partial z^2}f.
  $$
  V prostorech jiné dimenze postupujeme analogicky, jenom vynecháme nebo přidáme derivace podle dalších proměnných.
* Jiné běžné označení Laplaceova operátoru je $\Delta f$. Toto je bohužel je stejné jako změna funkce $f$ a je nutné tyto dva významy symbolu $\Delta$
  nezaměňovat. 
* Laplaceův operátor vystupuje například v problémech popsaných
  difuzní rovnicí a lineárním konstitučním vztahem s konstantním
  skalárním difuzním koeficientem (homogenní izotropní prostředí s
  lineární materiálovou odezvou).
