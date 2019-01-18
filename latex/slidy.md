% LaTeXové snippety
% Robert Mařík
% podzim 2018

# Snippety

<style>

li code{
background-color: #E4E5E7;
}
</style>



* V tomto dokumenty jsou snippety pro LaTeX. Můžete si je vykopírovat
do svého dokumentu a upravit dle potřeby. Fungují pro [LaTeX](https://www.latex-project.org/) a [MathJax](https://www.mathjax.org/)
a [KaTeX](https://katex.org/). Tedy fungují i v Markdown, například v [online Mardown
editoru](https://stackedit.io/app#).


* Jednořádkové fungují i pro [MS Word](https://support.office.com/cs-cz/article/rovnice-v-line%C3%A1rn%C3%ADm-form%C3%A1tu-pomoc%C3%AD-unicodemath-a-latex%C5%AF-ve-wordu-2e00618d-b1fd-49d8-8cb4-8d17f25754f8), ale je někdy nutné kód doladit podle požadavků software, například `\sin{x}` místo úspornějšího `\sin x`. Značka napravo od výrazu na samostaném řádku se do Wordu nevkládá jako `rovnice \tag{znacka}` ale `rovnice # (znacka)`

* Obecně v matematickém prostředí nezáleží na mezerách, ale některé interpretace toto pravidlo mohou porušovat. Například pro matematiku v textu na [https://stackedit.io/](https://stackedit.io/) nesmí být  mezera za prvním a před druhým dolarem.

# Jednořádkové výrazy 1


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
|parciální derivace| `\frac {\partial f} {\partial x}` | $\frac {\partial f}{\partial x}$|
|funkce|`f\colon \mathbb R^n \to \mathbb R^m`|$f\colon\mathbb R^n\to\mathbb R^m$|
|vektor|`\vec F(x,y)`|$\vec F(x,y)$|
|přibližná rovnost|`f(x,y)\approx \text{formula}`|$f(x,y)\approx \text{formula}$|
|řecká písmena| `\alpha \beta \varepsilon \varphi \dots`| $\alpha \beta \varepsilon \varphi \dots$|
|funkce| `\sin x\cos x\arctan x`| $\sin x\cos x\arctan x$|
|nepředdefinované funkce| `\mathop{\text{grad}} f`| $\mathop{\text{grad}} f$|


# Jednořádkové výrazy 2 (matice)

|název| TeX | výstup |
|-----|------------------------------------------------------------|---------|
|matice| `\begin{pmatrix} A & B \\ C & D \end{pmatrix}` | $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ |
|sloupcový vektor| `\begin{pmatrix} A  \\ B \end{pmatrix}` | $\begin{pmatrix} A \\ B \end{pmatrix}$ |
|determinant| `\begin{vmatrix} A & B \\ C & D \end{vmatrix}` | $\begin{vmatrix} A & B \\ C & D \end{vmatrix}$ |


# Jednořádkové výrazy 3 (elipsy)

|název| TeX | výstup |
|-----|------------------------------------------------------------|---------|
|cdots| `A+B+\cdots+Z` | $A+B+\cdots+Z$ |
|vdots| `\begin{pmatrix} x_0 \\ \vdots \\ x_n\end{pmatrix}` | $\begin{pmatrix} x_0 \\ \vdots \\ x_n\end{pmatrix}$ |

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
