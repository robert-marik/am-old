% LaTeXové snippety
% Robert Mařík
% 2018–2021

# Snippety

<style>

li code{
background-color: #E4E5E7;
}

.menu-obalka {display:none;}
</style>



* V tomto dokumenty jsou snippety pro LaTeX. Můžete si je vykopírovat
  do svého dokumentu a upravit dle potřeby. Fungují pro
  [LaTeX](https://www.latex-project.org/) a
  [MathJax](https://www.mathjax.org/) a
  [KaTeX](https://katex.org/). Tedy fungují i v systémech WeBWorK a Markdown.

* Jednořádkové fungují i pro [MS Word](https://support.office.com/cs-cz/article/rovnice-v-line%C3%A1rn%C3%ADm-form%C3%A1tu-pomoc%C3%AD-unicodemath-a-latex%C5%AF-ve-wordu-2e00618d-b1fd-49d8-8cb4-8d17f25754f8), ale je někdy nutné kód doladit podle požadavků software, například `\sin{x}` místo úspornějšího `\sin x`. Značka napravo od výrazu na samostatném řádku se do Wordu nevkládá jako `rovnice \tag{znacka}` ale `rovnice # (znacka)`

* Obecně v matematickém prostředí nezáleží na mezerách, ale některé
  interpretace toto pravidlo mohou porušovat. Například pro matematiku
  v textu na [https://stackedit.io/](https://stackedit.io/) nesmí být
  mezera za prvním a před druhým dolarem.

* Obecně v LaTeXu nezáleží na koncích řádku, ale některé interpretace
  toto pravidlo mohou porušovat. Například v textu na
  [https://stackedit.io/](https://stackedit.io/) způsobí konec řádku
  na vstupu ukončení řádku na výstupu (což zpravidla nechceme).

* LaTeXový příkaz k ručně nakreslenému symbolu najde služba
  [Detexify](http://detexify.kirelabs.org/classify.html)

* LaTeX slouží matematikům více než 30 let. Je tedy na síti spousta
  návodů nebo dotazů a odpovědí. Jsou i [nástroje](https://www.codecogs.com/latex/eqneditor.php), kde si naklikáte
  vzorec interaktivně a poté zkopírujete LaTeX kód. Odpadá tím
  rychlost, jedna z hlavních výhod zápisu v LaTeXu, ale pro
  začátečníka se to může hodit.

# Zásady pro LaTeX

* LaTeX je vlastně programovací jazyk pro texty. Ale běžný text v něm
  vypadá běžně. Něco jiného než běžný text se dělá pomocí příkazů.
* Příkazy v LaTeXu začínají lomítkem. Například `\frac` je příkaz pro zlomek.
* Kromě příkazů máme aktivní znaky. Nejčastější jsou následující.
    * Dolar. Mezi dolary píšeme matematický text. Bude jiným fontem, se speciálním mezerováním a spousta dalšího. Ve WeBWorK používejte zpětné lomítko a kulaté závorky.
    * Dvojdolar. Jako dolar, ale matematický text bude navíc na samostatném řádku, centrovaný na osu. Pořád ale bude pokračovat jeden odstavec. Ve WeBWorK používejte zpětné lomítko a hranaté závorky.
    * Složené závorky. Závorky ohraničují působení příkazu. Dají se vynechat, pokud je argumentem jeden znak. Například `$\sqrt 2$` a `$\sqrt {121}$` vede na $\sqrt 2$ a $\sqrt{121}$. Špatně by bylo `$\sqrt 121$`, které vede na $\sqrt 121$.
    Podobně jednu polovinu můžu zapsat jako `$\frac 12$`, ale jednu desetinu už jako `$\frac 1{10}$`
* Mezera se v matematickém prostředí ignoruje, protože zde platí speciální pravidla. Pokud potřebujeme vložit mezeru, děláme to speciálním příkazem. Krátká mezera je `\,`, normální mezera je `\␣` (zpětné lomítko a mezera), dlouhá mezera je `\quad`.
* LaTeX je typografický systém. My využijeme jenom jeho schopnost sázet matematiku. Nenechte se proto odradit tlustými návody. Nic takového nepotřebujete.

# Zásady pro WeBWorK

* WeBWorK je napsaný v jazyce PERL, kde má symbol dolaru speciální postavení. Proto používejte pro matematické prostředí dvojici `\(` a `\)`. Pro matematické prostředí naformátované na samostatný řádek potom `\[` a `\]`. Na dolary a dvojdolary raději zapomeňte.

# Zásady pro Markdown

* LaTeX je nejjednodušší způsob, jak psát matematiku. Nejjednodušší způsob jak psát formátovaný text je jazyk Markdown. I v něm běžný text vypadá běžně a něco jiného než běžný text se dělá pomocí značek. Proto se oba systémy vhodně doplňují.
* Nový odstavec v Markdownu začíná prázdným řádkem.


# Základní výrazy


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


Vykopírujte text z prostředního sloupce mezi značky `$ $` pro matematiku v textu, mezi `$$ $$` pro matematiku na samostatném řádku. 

|název| TeX | výstup |
|-----|----------------------------------------------------|--------------------|
|mocnina| `x^2 y^{10}` | $x^2 y^{10}$|
|index| `x_0 y_{10}^3` | $x_0 y_{10}^3$|
|zlomek| `\frac {A} {B+C}` | $\frac {A}{B+C}$|
|funkce|`f\colon \mathbb R^n \to \mathbb R^m`|$f\colon\mathbb R^n\to\mathbb R^m$|
|vektor|`\vec F(x,y)`|$\vec F(x,y)$|
|přibližná rovnost|`f(x,y)\approx \text{formula}`|$f(x,y)\approx \text{formula}$|
|řecká písmena| `\alpha \beta \varepsilon \varphi \dots`| $\alpha \beta \varepsilon \varphi \dots$|
|funkce| `\sin x\cos x\arctan x`| $\sin x\cos x\arctan x$|
|nepředdefinované funkce| `\mathop{\text{grad}} f`| $\mathop{\text{grad}} f$|

# Derivace

|název| TeX | výstup |
|-----|----------------------------------------------------|--------------------|
|derivace| `y',\ y'',\ y''',\ y^{(n)}` | $y',\ y'',\ y''',\ y^{(n)}$|
|derivace| `\frac {\mathrm dy} {\mathrm dx}` | $\displaystyle\frac {\mathrm dy} {\mathrm dx}$|
|parciální derivace| `\frac {\partial f} {\partial x}` | $\displaystyle\frac {\partial f}{\partial x}$|
|druhá derivace| `\frac {\mathrm d^2y} {\mathrm dx^2}` | $\displaystyle\frac {\mathrm d^2y} {\mathrm dx^2}$|
|druhá derivace| `\frac {\mathrm d^2} {\mathrm dx^2}y` | $\displaystyle\frac {\mathrm d^2} {\mathrm dx^2}y$|
|smíšená parciální derivace druhého řádu| `\frac {\partial^2 f} {\partial x\partial y}` | $\displaystyle\frac {\partial^2 f}{\partial x\partial y}$|
|parciální derivace druhého řádu| `\frac {\partial^2 f} {\partial x^2}` | $\displaystyle\frac {\partial^2 f}{\partial x^2}$|
|parciální derivace z difuzní rovnice| `\frac {\partial} {\partial x}\left( D_x \frac {\partial} {\partial y} T \right)` | $\displaystyle\frac {\partial} {\partial x}\left( D_x \frac {\partial} {\partial y} T \right)$|
|gradient| `\nabla u` | $\nabla u$|
|divergence| `\nabla \cdot \vec j` | $\nabla \cdot \vec j$|
|rotace| `\nabla \times \vec j` | $\nabla \times \vec j$|

# Integrály

|název| TeX | výstup |
|-----|----------------------------------------------------|--------------------|
|neurčitý integrál| `\int (x^2-\arctan x)^{\sin x} \,\mathrm dx` | $\int (x^2-\arctan x)^{\sin x} \,\mathrm dx$|
|určitý integrál| `\int_a^b \ln x \,\mathrm dx` | $\int_a^b \ln x \,\mathrm dx$|
|dvojný integrál| `\iint_M \frac 1{\sqrt{x^2+y^2}} \,\mathrm dx\mathrm dy` | $\iint_M \frac 1{\sqrt{x^2+y^2}} \,\mathrm dx\mathrm dy$|
dvojný integrál| `\iint_M \frac 1{\sqrt{x^2+y^2}} \,\mathrm dS` | $\iint_M \frac 1{\sqrt{x^2+y^2}} \,\mathrm dS$|
křivkový integrál| `\oint_C \frac 1{\sqrt{x^2+y^2}} \,\mathrm ds` | $\oint_C \frac 1{\sqrt{x^2+y^2}} \,\mathrm ds$|
křivkový integrál| `\int_C \vec F \,\mathrm d\vec r` | $\int_C \vec F \,\mathrm d\vec r$|
|dosazení mezí| `\left[ \frac {x^4}{4} \right]_{0}^{\sqrt 2}` | $\left[ \frac {x^4}{4} \right]_{0}^{\sqrt 2}$|


# Matice

|název| TeX | výstup |
|-----|------------------------------------------------------------|---------|
|matice| `\begin{pmatrix} A & B \\ C & D \end{pmatrix}` | $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ |
|matice s hranatými závorkami| `\begin{bmatrix} A & B \\ C & D \end{bmatrix}` | $\begin{bmatrix} A & B \\ C & D \end{bmatrix}$ |
|sloupcový vektor| `\begin{pmatrix} A  \\ B \end{pmatrix}` | $\begin{pmatrix} A \\ B \end{pmatrix}$ |
|determinant| `\begin{vmatrix} A & B \\ C & D \end{vmatrix}` | $\begin{vmatrix} A & B \\ C & D \end{vmatrix}$ |
|maticový součin| `\begin{pmatrix} A & B \\ C & D \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}` | $\begin{pmatrix} A & B \\ C & D \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}$ |


# Elipsy

|název| TeX | výstup |
|-----|------------------------------------------------------------|---------|
|cdots| `A+B+\cdots+Z` | $A+B+\cdots+Z$ |
|vdots| `\begin{pmatrix} x_0 \\ \vdots \\ x_n\end{pmatrix}` | $\begin{pmatrix} x_0 \\ \vdots \\ x_n\end{pmatrix}$ |
|dots| `i\in\{1,2,\dots,n\}` | $i\in\{1,2,\dots,n\}$ |
|ddots| `\begin{pmatrix}1&&\\&\ddots&\\&&1\end{pmatrix}` | $\begin{pmatrix}1&&\\&\ddots&\\&&1\end{pmatrix}$ |

# Závorky

|název| TeX | výstup |
|-----|------------------------------------------------------------|---------|
|big| `\bigl( x+y \bigr)` | $\bigl( x+y \bigr)$ |
|Big| `\Bigl[ x+y \Bigr]^5` | $\Bigl[ x+y \Bigr]^5$ |
|bigg| `\biggl( x+y \biggr)` | $\biggl( x+y \biggr)$ |
|Bigg| `\Biggl( x+y \Biggr)^{\sin x}` | $\Biggl( x+y \Biggr)^{\sin x}$ |
|natahovací| `\left( x+y \right)` | $\left( x+y \right)$ |
|natahovací| `\left( x+\frac{y^{e^{x^{14}}}}{1-x^{12}} \right)` | $\left( x+\frac{y^{e^{x^{14}}}}{1-x^{12}} \right)$ |


# Víceřádkové výrazy a výrazy na samostatný řádek

* Nezáleží na koncích řádků, ty slouží pouze pro přehlednost.
* Pro vynechání značky nepoužívete řádek s příkazem `\tag`.

## Zarovnávání podle rovnítek

~~~
$$
\begin{aligned}
 a + b &= c\\
 e &= x + y
\end{aligned}
\tag{N}
$$
~~~

$$
\begin{aligned}
 a + b &= c\\
 e &= x + y
\end{aligned}
\tag{N}
$$

## Jiné zarovnávání

~~~
$$
\begin{aligned}
 a = b & + c\\
 & + y
\end{aligned}
\tag{M}
$$
~~~

$$
\begin{aligned}
 a = b & + c\\
 & + y
\end{aligned}
\tag{M}
$$


# Komentované ukázky chybných zápisů

|Číslo|Špatně|Správně|Vysvětlení|
|-|----|----|----|
|1|Derivace rychlosti dinosaura podle délky kroku je $$\frac{\mathrm dv}{\mathrm dl}=1.336*l^{0.67}.$$|Derivace rychlosti dinosaura podle délky kroku je $$\frac{\mathrm dv}{\mathrm dl}=1.336 l^{0.67}.$$|Špatně je zápis násobení. Násobení zapisujeme hvězdičkou jenom ve vstupech pro počítač. Pro texty určené lidem **hvězdičku nepoužíváme**. Nepíšeme buď nic, nebo `\times` nebo `\cdot`, tj. $1.336\times l^{0.67}$ nebo $1.336\cdot l^{0.67}$.|
|2|Derivace rychlosti dinosaura podle délky kroku je $$\frac{\mathrm dv}{\mathrm dl}=1.336 \mathrm l^{0.67}.$$|Derivace rychlosti dinosaura podle délky kroku je $$\frac{\mathrm dv}{\mathrm dl}=1.336 l^{0.67}.$$|Špatně je font pro proměnnou označující délku kroku. Matematické proměnné zapisujeme matematickou kurzívou. To je defaultní font v matematickém prostředí, tedy v praxi to znamená, že **nic ručně nepřepínáme**, pokud si opravdu nejsme jisti, že to je potřeba (jako například u jednotek).|
|3|Derivace rychlosti dinosaura podle délky kroku je $$\frac{\mathrm dv}{\mathrm dl}=1.336 l^{0.67}$$|Derivace rychlosti dinosaura podle délky kroku je $$\frac{\mathrm dv}{\mathrm dl}=1.336 l^{0.67}.$$|Špatně je chybějící konec věty. Na konci věty píšeme **tečku**. (Pozor, toto pravidlo nemusí platit v anglickém textu, tam záleží na typografovi publikace.)|
|4|Jednotka derivace rychlosti dinosaura podle délky kroku je $s^{-1}.$|Jednotka derivace rychlosti dinosaura podle délky kroku je $\mathrm s^{-1}.$|Špatně je font pro zápis jednotky. Úmysl byl zapsat převrácenou hodnotu sekundy, ale zapsána je převrácená hodnota dráhy. Fyzikální jednotky se nepíšou matematickou kurzívou, ta je vyhrazena pro proměnné. Přepínáme do **textového fontu** příkazem `\mathrm`.| 
|5|Jednotka derivace rychlosti dinosaura podle délky kroku je $$\mathrm s^{-1}.$$|Jednotka derivace rychlosti dinosaura podle délky kroku je $\mathrm s^{-1}.$|Špatně je umístění vzorce s jednotkou na samostatný řádek. Velmi krátké vzorce si umístění na **samostatný řádek** zaslouží jenom vyjímečně. Napříkad pokud vzorec potřebujeme očíslovat. Krátké matematické výrazy píšeme do textu odstavce.| 
|6|Derivace rychlosti dinosaura podle délky kroku je: $$\frac{\mathrm dv}{\mathrm dl}=1.336 l^{0.67}.$$|Derivace rychlosti dinosaura podle délky kroku je $$\frac{\mathrm dv}{\mathrm dl}=1.336 l^{0.67}.$$|Špatně je použití dvojtečky. Snažíme se o co nejhladší začlenění matematických výrazů do textu. Kdyby místo vzorce bylo slovo, tak taky žádnou **dvojtečku nepoužíváme**. Proto není potřeba ji psát ani v situaci, kdy je místo slova vzorec. Co není potřeba psát a nepřispívá k čitelnosti, to ani nepíšeme. (Podobně jako tečka za větou, pravidlo nemusí platit v jiných jazycích a při speciálních požadavcích typografa.)|
|7|Z Buckinghamova II teorému vyplývá pro kužel s daným úhlem u vrcholu vztah mezi objemem $V$ a výškou $h$ ve tvaru $$V = kh^3.$$|Pro kužel s daným úhlem u vrcholu je objem $V$ úměrný třetí mocnině výšky $h$, tj. platí $$V = kh^3$$ pro vhodnou konstantu $k$.|Špatně je název věty, v názvu není římská dvojka, ale velké řecké písmeno "pí". Obecně platí, že **ve vlastních textech používáme jenom takové informace, o kterých jsme stoprocentně přesvědčeni, že jsou správně.** Pokud si například nejsme jisti názvem věty, v naprosté většině textů je možné se mu vyhnout.|
|8|$k$ je konstanta úměrnosti.|Veličina $k$ je konstanta úměrnosti.|Není vhodné začínat větu matematickým výrazem. Vždy je možné použít formulaci, kdy **věta začíná běžným slovem**. Poté je možné toto slovo napsat s velkým písmenem na začátku a je zcela zřejmé, že zde začíná nová věta.|
