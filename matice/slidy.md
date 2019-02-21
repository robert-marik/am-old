% Lineární algebra
% Robert Mařík
% 2019

Sčítání, násobení

# Vektory a operace s nimi

# Vektory ve 2D a 3D -- geometrie

# Sčítání vektorů a integrace cesty u migrujících živočichů

# Lineární závislost a nezávislost vektorů

# Lineární závislost a nezávislost vektorů (stechiomerické matice)

# Matice a jejich lineární kombinace

# Maticový součin

# Migrace mezi městem a venkovem


\iffalse 

<div class='obtekat'>

![Markovovy řetězce umožňují modelování migrace mezi městem a venkovem. Zdroj: pixabay.com](city.jpg)

</div>

\fi

Každý rok měříme velikosti populací ve městě a na
venkově. Procentuální složení zaznamenáváme ve formě
vektoru. Například vektor $$ X_0=
\begin{pmatrix}
  0.6 \\ 0.4
\end{pmatrix}
$$
znamená, že $60\%$ populace žije ve městě a $40\%$ na venkově. Každý
rok zůstane $95\%$ městské populace ve městě a $5\%$ se stěhuje na
venkov. Podobně $97\%$ obyvatelstva venkova zůstává a $3\%$ se stěhuje
do města. Po jednom roce je tedy rozložení populace dáno vektorem
$$ X_1=0.6
\begin{pmatrix}
  0.95 \\ 0.05 
\end{pmatrix}
+0.4
\begin{pmatrix}
  0.03 \\ 0.97
\end{pmatrix}.
$$
Koeficienty vektoru $X_0$ jsou koeficienty v této lineární
kombinaci. Podobně, rozložení po dvou letech bude dáno lineární
kombinací s koeficienty, danými vektorem $X_1$. Je výhodné tuto
lineární kombinaci zapsat pomocí maticového násobení. Pro matici $A=\begin{pmatrix}   0.95 & 0.03 \\ 0.05 & 0.97 \end{pmatrix}$
platí $$X_1=AX_0$$ a dále
$$X_2=AX_1=A(A X_0)=(AA)X_0=A^2 X_0.$$
Po $k$ letech je rozložení populace dáno vektorem $$X_k=A^k X_0$$


Další informace:

* Linear algebra, Lay

# Leslieho matice

\iffalse 

<div class='obtekat'>

![Patrick Holt Leslie (1900-1972) roku 1945 publikoval v časopisu
Biometrika On the use of matrices in certain population mathematics. V
něm sestavil a analyzoval model růstu počtu samic v populaci potkanů
(Rattus norvegicus); jeho model ovšem může být stejně dobře použit pro
lidskou nebo jinou populaci. Zdroj: pixabay.com](potkan.jpg)

</div>

\fi

Leslieho model růstu populace zohledňuje věkovou strukturu
populace. Původně byl odvozen pro modelování populace samic, dá se
však adaptovat na populaci obecně. Model předpokládá, že populace je
rozdělena do několika věkových kategoriií a v každé kategorii je dána
pravděpodobnost dožití se do další kategorie a průměrný počet potomků. 

Příslušný model například pro populaci rozdělenou do tří věkových kategorií by byl dán rovnicí
$$\begin{pmatrix} x_1(k+1) \\ x_2(k+1) \\ x_3 (k+1)
\end{pmatrix}
=
\begin{pmatrix}
  f_1 & f_2 & f_3 \\ p_1 & 0 & 0\\ 0 & p_2 & 0
\end{pmatrix} \begin{pmatrix} x_1(k) \\ x_2(k) \\ x_3 (k)
\end{pmatrix}
$$

Další informace:

* [Z. Pospíšil, Maticové populační modely](http://portal.matematickabiologie.cz/index.php?pg=analyza-a-modelovani-dynamickych-biologickych-dat--maticove-populacni-modely--prolog--leslieho-model-rustu-populace#pro14)

# Rozložení teploty na tepelně vodivé desce


\iffalse 

<div class='obtekat'>

![Rozložení teploty na tepelně vodivé desce je možné přibližně zkoumat metodami lineární algebry. Zdroj: pixabay.com](teplomer.jpg)

</div>

\fi

