% LaTeXové snippety
% Robert Mařík
% 2018-2019

# Snippety

<style>

li code{
background-color: #E4E5E7;
}
</style>



* V tomto dokumenty jsou snippety pro LaTeX. Můžete si je vykopírovat
  do svého dokumentu a upravit dle potřeby. Fungují pro
  [LaTeX](https://www.latex-project.org/) a
  [MathJax](https://www.mathjax.org/) a
  [KaTeX](https://katex.org/). Tedy fungují i v Markdown, například v
  [online Markdown editoru](https://stackedit.io/app#).


* Jednořádkové fungují i pro [MS Word](https://support.office.com/cs-cz/article/rovnice-v-line%C3%A1rn%C3%ADm-form%C3%A1tu-pomoc%C3%AD-unicodemath-a-latex%C5%AF-ve-wordu-2e00618d-b1fd-49d8-8cb4-8d17f25754f8), ale je někdy nutné kód doladit podle požadavků software, například `\sin{x}` místo úspornějšího `\sin x`. Značka napravo od výrazu na samostaném řádku se do Wordu nevkládá jako `rovnice \tag{znacka}` ale `rovnice # (znacka)`

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
|derivace| `\frac {\mathrm dy} {\mathrm dx}` | $\frac {\mathrm dy} {\mathrm dx}$|
|parciální derivace| `\frac {\partial f} {\partial x}` | $\frac {\partial f}{\partial x}$|
|druhá derivace| `\frac {\mathrm d^2y} {\mathrm dx^2}` | $\frac {\mathrm d^2y} {\mathrm dx^2}$|
|derivace| `\frac {\mathrm d^2} {\mathrm dx^2}y` | $\frac {\mathrm d^2} {\mathrm dx^2}y$|
|parciální derivace| `\frac {\partial^2 f} {\partial x\partial y}` | $\frac {\partial^2 f}{\partial x\partial y}$|
|parciální derivace| `\frac {\partial} {\partial x}\left( D\frac {\partial} {\partial y} T \right)` | $\frac {\partial} {\partial x}\left( D\frac {\partial} {\partial y} T \right)$|

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
