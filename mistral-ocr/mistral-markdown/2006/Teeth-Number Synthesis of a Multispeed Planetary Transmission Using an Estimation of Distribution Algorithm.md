## P. A. Simionescu

Department of Mechanical Engineering, The University of Tulsa, 600 S. College, Tulsa, OK 74104

## D. Beale

Department of Mechanical Engineering, Auburn University, 202 Ross Hall, Auburn, AL 36849

## G. V. Dozier

Department of Computer Science, Auburn University, 109 Dunstan Hall, Auburn, AL 36849

## Teeth-Number Synthesis of a Multispeed Planetary Transmission Using an Estimation of Distribution Algorithm

The gear-teeth number synthesis of an automatic planetary transmission used in automobiles is formulated as a constrained optimization problem that is solved with the aid of an Estimation of Distribution Algorithm. The design parameters are the teeth number of each gear, the number of multiple planets and gear module, while the objective function is defined as the departure between the imposed and the actual transmission ratios, constrained by teeth-undercut avoidance, limiting the maximum overall diameter of the transmission and ensuring proper spacing of multiple planets. For the actual case of a $3+1$ speed Ravigneaux planetary transmission, the design space of the problem is explored using a newly introduced hyperfunction visualization technique, and the effect of various constraints highlighted. Global optimum results are also presented.
[DOI: 10.1115/1.2114867]

## Introduction

The wide applicability of planetary gears in the aircraft, maritime, and mainly automotive industry (particularly as automatic multi-speed transmissions) has brought a great deal of attention to this topic. The literature on the design of planetary automatic transmissions covers conceptual design [1-9], kinematic analysis $[6,8,10-14]$, and power flow and efficiency analysis [15-18]. Less work has been done however on the design of multi-speed planetary gears for imposed transmission ratios-the available literature covers mostly fixed axles transmissions [19-23] and the design of single-ratio planetary units [20,24-26].

Specific to teeth number synthesis of multi-speed planetary transmissions are the design variables which must be integers (gear-teeth numbers and the number of multiple planets) and the numerous constraints. These constraints reduce significantly the feasible domain of the design space, making the synthesis problem quite difficult to solve. The work published on teeth number synthesis of multi-speed planetary transmissions is, for the most part, hand-calculation oriented [27-29], or in the case of computer implemented approaches, only some of the numerous constraints were actually considered [30-33].

The constraints imposed on multi-speed planetary transmissions derive from: (a) the minimum allowed number of teeth each gear can have so that undercut does not occur, (b) the maximum allowed diameter of the whole assembly, (c) the condition of central gears having coaxial axes, (d) the requirement of equally spacing multiple planets, and (e) the noninterference condition of neighboring gears.

Aspects like tooth geometry optimization [34] or bearing selection from the condition of volume and cost minimization and of satisfying a required design life can also be prescribed early in the design process. However, since these can be decoupled from the teeth-number selection problem, it is preferable to be solved as a subsequent multiobjective optimization problem once a satisfactory solution of the original problem becomes available [35].

Contributed by Power Transmission and Gearing Committee of ASME for publication in the Journal of Mechanical Design, Manuscript received: August 24, 2004; final manuscript received: April 1, 2005. Assoc. Editor: Teik C. Lim.

## The Ravigneaux 3+1 Gear Transmission

Figure 1 shows a planetary transmission of the Ravigneaux type with three forward and one reverse gears used in automobiles [36,37]. A kinematic diagram of the transmission is available in Fig. 2, where the broad planet gear is shown as two compound gears 2 and 3 . Based on the clutch/brake activation required in each gear (Table 1), it can be shown that in the first and reverse gears, the planet carrier is immobile and the equivalent transmission is a fixed-axle one with the following transmission ratios

$$
i_{1}=N_{0} / N_{4}
$$

and

$$
i_{R}=-\left(N_{2} N_{6}\right) /\left(N_{1} N_{3}\right)
$$

In the third gear, the planet carrier, sun gears, and ring gear rotate together as a whole

$$
i_{3}=1
$$

i.e., a direct drive, which ensures an increased mechanical efficiency of the transmission.

The second gear configuration is the only case when the transmission works as a planetary gear set. Considering the planet carrier $c$ immobile, three basic transmission ratios can be defined as follows

$$
i_{16}^{\prime}=-\frac{N_{0} N_{6}}{N_{1} N_{3}} \quad i_{46}^{\prime}=\frac{N_{0}}{N_{4}} \quad i_{14}^{\prime}=-\frac{N_{2} N_{4}}{N_{1} N_{3}}
$$

Through motion inversion, which converts the planetary gear into a fixed axle transmission, the following additional relations between the angular velocities of the sun gears 1 and 4 , ring gear 6 , and planet carrier $c$ can be written as

$$
i_{16}^{\prime}=\frac{\omega_{2}-\omega_{c}}{\omega_{6}-\omega_{c}} \quad i_{46}^{\prime}=\frac{\omega_{4}-\omega_{c}}{\omega_{6}-\omega_{c}} \quad i_{14}^{\prime}=\frac{\omega_{1}-\omega_{c}}{\omega_{4}-\omega_{c}}
$$

Eliminating $\omega_{c}$ between any two of the above equations and for $\omega_{4}=0$, the sought-for transmission ratio of the second gear can be obtained

$$
i_{2}=\frac{N_{0}\left(N_{1} N_{3}+N_{2} N_{4}\right)}{N_{1} N_{3}\left(N_{6}-N_{4}\right)}
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1 Ravigneaux planetary gear [36]: 1 small sun gear; 2-3 broad planet gear; 4 large sun gear; 5 narrow planet gear; 6 ring gear
![img-1.jpeg](img-1.jpeg)

Fig. 2 Kinematic diagram of a $3 \times 1$ transmission ratios Ravigneaux planetary transmission. Note that the broad planet 2-3 consists now of two distinct gears

|  | $C=$ clutch $/ B=$ brake |  |  |  |
| :-- | :-- | :-- | :-- | :-- |
| Speed | $C_{1}$ | $C_{2}$ | $B_{1}$ | $B_{2}$ |
| First | engage | engage | engage | engage |
| Second | engage | engage | engage | engage |
| Third |  | engage | engage |  |
| Reverse |  |  |  |  |

The expressions of the transmission ratios $i_{1}, i_{2}$, and $i_{R}$ previously derived will be further used in formulating the problem of finding the optimum number of gear teeth for which imposed transmission ratios are best fulfilled.

## The Optimization Problem

A general nonlinear programming problem requires finding the optimum point (minimum or maximum) of a function of $n$ real variables

$$
f\left(x_{1} \ldots x_{n}\right)
$$

subject to side constraints

$$
x_{j \min } \leqslant x_{j} \leqslant x_{j \max } \quad(1 \leqslant j \leqslant n)
$$

inequality constraints

$$
g_{j}\left(x_{1}, \ldots, x_{n}\right) \leqslant 0 \quad(1 \leqslant j \leqslant n 1)
$$

and equality constraints

$$
h_{j}\left(x_{1}, \ldots, x_{n}\right)=0 \quad(1 \leqslant j \leqslant n 2)
$$

When the design variables of an optimization problem are imposed integer values, they may be considered from the beginning integers [23], or additional equality constraints of the form

$$
\text { round }\left(x_{j}\right)-x_{j}=0 \quad(1 \leqslant j \leqslant n)
$$

can be imposed. Alternatively, a continuous optimization problem can be solved first and then a grid search performed in the neighborhood of the optima thus found, until a set of integers that satisfy all constraints are identified [38].

In this paper, the gear-teeth numbers were considered from the beginning integers, and the synthesis problem solved without significant implementation effort using an Estimation of Distribution Algorithm [39,40]. The $n$ design variables are the teeth numbers of gears 1 and 4 , ring gear 6 , and planet gear 2,3 , and 5 , together with the number of equally spaced, identical planets to be mounted on the planet carrier. Other possible design variables could be module $m_{1}=m_{2}$ and $m_{3}=m_{4}=m_{5}=m_{6}$ which can have only discrete values in accordance with gear standards.

A suitable objective function to be used for minimizing the departure between the actual $\left(i_{k}\right)$ and the imposed $\left(i_{0 k}\right)$ transmission ratios could be maximum-error based:

$$
f_{1}\left(N_{1}, \ldots, N_{n}, p, m_{j}\right)=\max _{k}\left(w_{k} \cdot\left|i_{k}-i_{0_{k}}\right|\right)
$$

or equal to the sum of squared residuals

$$
f_{2}\left(N_{1}, \ldots, N_{n}, p, m_{j}\right)=\sum_{k} w_{k}\left(i_{k}-i_{0_{k}}\right)^{2}
$$

where $k=\{1,2, R\}$ is the number of transmission ratios (less the direct drive) and $w_{k}$ are weighting coefficients, the values of which can be adjusted to differentiate the importance of these transmission ratios during the optimization process (for example, lowering the importance of the reverse gear which is engaged for shorter periods of time).

It can be easily checked that most constraints have meaning for both continuous and integer design variables (i.e., the gears inside the transmission can be considered ideal friction wheels), while

other constraints (like the condition of assembling multiple planet carriers) explicitly require the design variables to be integers. Because good solutions can be overlooked, seeking a continuous optimum first followed by a neighbor search for the integers satisfying all constraints it is likely to be less effective than imposing from the beginning the design variables to be integers.

Noting with $n s=2$ the number of sun gears, $n p=3$ the number of distinct planet gears (gears 2, 3, and 5), and $n r=1$ the number of ring gears, the lower side constraints have the following general expressions:

$$
N \min _{j} \leqslant N_{j} \quad(1 \leqslant j \leqslant n s+n p)
$$

where $N \min _{j}$ (the minimum number of teeth the sun or planet gears can have) are specified from the condition of undercut avoidance as 17 or if the use of nonstandard gears is acceptable, 14 even 12 teeth.

Limiting the maximum outer diameter of the transmission to a value $D_{\max }$ can be accounted for by imposing an upper value to the standard root diameter of the ring gear

$$
m_{3}\left(N_{6}+2.5\right) \leqslant D_{\max }
$$

and constraining to the same value the outside diameter of the workspace of planet 2 and idler 5

$$
\begin{aligned}
& 2\left[m_{1}\left(N_{1}+N_{2}\right) / 2+m_{1}\left(N_{2} / 2+1\right)\right] \leqslant D_{\max } \\
& 2\left[m_{3}\left(N_{4}+N_{5}\right) / 2+m_{3}\left(N_{5} / 2+1\right)\right] \leqslant D_{\max }
\end{aligned}
$$

Evidently, when nonstandard gears are accepted, the above constraints (15)-(17) can be satisfied only approximately, since hob withdrawal is accompanied by a diameter change of the addendum and dedendum circles of the respective gears.

The condition of the solar and ring gears having coaxial axes can be written either as equality constraints, or (if nonstandard gears are acceptable) as inequality constraints. The latter, commonly done in practice, is more advantageous to the searching process, and for the actual case of mating gears 1,2 and mating gears 3,6 it was translated into the following inequality

$$
\left|m_{1}\left(N_{1}+N_{2}\right) / 2-m_{3}\left(N_{6}-N_{3}\right) / 2\right| \leqslant\left(m_{1}+m_{3}\right) / 2
$$

which is equivalent to imposing the difference in the standard center-distances of gears 1 and 2 and gears 3 and 6 to be less than an average modulus $\left(m_{1}+m_{3}\right) / 2$.

The neighborhood condition refers to adjacent, non-meshing gears, the teeth of which are required to operate at a distance greater than a certain minimum value $d \min _{i j}$

$$
d_{i j} \geqslant d \min _{i j}
$$

In the above equation, $d_{i j}$ is the distance between the addendum circles of the respective neighboring wheels. For the broad planet 2-3 and idler 5 (Fig. 3) these distances can be approximated with

$$
\begin{aligned}
& d_{22}=2\left[m_{1}-\frac{N_{1}+N_{2}}{2} \sin \left(\frac{\pi}{p}\right)-m_{1}\left(\frac{N_{2}}{2}+1\right)\right] \\
& d_{33}=2\left[m_{3}-\frac{N_{6}-N_{3}}{2} \sin \left(\frac{\pi}{p}\right)-m_{3}\left(\frac{N_{2}}{2}+1\right)\right]
\end{aligned}
$$

and

$$
d_{55}=2\left[m_{3}-\frac{N_{4}+N_{5}}{2} \sin \left(\frac{\pi}{p}\right)-m_{3}\left(\frac{N_{2}}{2}+1\right)\right]
$$

When checking the interference of planets 3 and 5 the following distance must also be evaluated
![img-2.jpeg](img-2.jpeg)

Fig. 3 Schematic for calculating distances $d_{22}, d_{34}, d_{35}$, and $d_{55}$. Notice that one of the idler planets 5 has been removed for clarity.

$$
\begin{aligned}
d_{35}= & \sqrt{C_{36}^{2}+C_{45}^{2}-2 C_{36} C_{45} \cos \left(\frac{2 \pi}{p}-\beta\right)}-m_{3}\left(\frac{N_{5}}{2}+1\right) \\
& -m_{3}\left(\frac{N_{5}}{2}+1\right)
\end{aligned}
$$

with

$$
\begin{gathered}
\beta=\cos ^{-1}\left(\frac{C_{36}^{2}+C_{45}^{2}-C_{35}^{2}}{2 C_{36} \cdot C_{45}}\right) \quad C_{36}=m_{3} \frac{N_{6}-N_{3}}{2} \\
C_{45}=m_{3} \frac{N_{4}+N_{5}}{2} \text { and } C_{35}=m_{3} \frac{N_{5}+N_{5}}{2}
\end{gathered}
$$

In addition, the distances between the addendum circles of planet gear 3 and sun gear 4

$$
d_{34}=m_{3} \frac{N_{6}-N_{3}}{2}-m_{3}\left(\frac{N_{5}}{2}+1\right)-m_{3}\left(\frac{N_{4}}{2}+1\right)
$$

and between addendum circles of ring gear 6 and idler planet gear 5

$$
d_{56}=m_{3}\left(\frac{N_{6}}{2}-1\right)-m_{3} \frac{N_{4}+N_{5}}{2}-m_{3}\left(\frac{N_{5}}{2}+1\right)
$$

must also be kept larger than a certain value in order to allow for a satisfactory flow of lubricant.

When the minimum admissible values $d \min _{i j}$ in Eq. (19) are defined as a multiple of the modulus of the respective neighboring gears, the corresponding inequalities simplify to some extent (see the Appendix where the optimization problem has been summarized for conciseness and where $d \min _{i j}$ were considered equal to multiples $d_{i j}$ of either $m_{1}$ or $m_{3}$ ).

The most restrictive constraints of all are the conditions of assembling equally spaced planets, which are equality constraints in integer numbers. Based on the theory developed in Ref. [41], for the Ravigneaux planetary transmission under consideration, the condition of having equally spaced identical planets 2-3 writes

$$
\operatorname{Frac}\left(\frac{1}{p}\left|\frac{1}{i_{1-2}^{\prime}}-\frac{1}{i_{6-3}^{\prime}}\right|\right)=\left|\frac{A}{N_{2}} \pm \frac{B}{N_{3}}\right|
$$

where $\operatorname{Frac}(\ldots)$ is the factional part of the expression in parentheses, $A$ and $B$ are integers $A \leqslant N_{2} / p$ and $B \leqslant N_{3} / p$, while

$$
i_{1-2}^{\prime}=-N_{2} / N_{1} \text { and } i_{6-3}^{\prime}=N_{3} / N_{6}
$$

are called partial basic ratios of the planetary gear (the transmission ratios between the respective gears when the planet carrier is immobilized).

A second assembly condition requirement must be imposed to idler planets 5 . The equivalent expression in basic ratios applied to either gear $4,5,3$, or 6 (and without resorting to the Frac(..) operator so that simplifications can be made across the equal sign), reduces to [41]

$$
\left(N_{6}-N_{4}\right) / p=\text { integer }
$$

## The Search Algorithm

The optimization problem previously formulated has been solved with the aid of an elitist Estimation of Distribution Algorithm (EDA) of the Population Based Incremental Learning (PBIL) type [39,40], a very robust and easy to implement Evolutionary Algorithm. Following is the general structure of the elitist PBIL algorithm:

Step 1: Generate $M$ uniform random points within the imposed boundaries of the design variables $\left[x_{i \text { min }}, \ldots, x_{i \text { max }}\right](i=1, \ldots, n)$ or until at least one feasible individual has been generated (the population size $M$ is a constant specified by the user).
repeat Step 2 and Step 3 until a certain stopping criteria is met;
Step 2: Select the best $N$ individuals in the population and evaluate the average and standard deviation vectors

$$
\begin{gathered}
\left\{\mu_{i}\right\}=\left\{\frac{1}{N} \sum_{k=1}^{N}\left(x_{i}\right)_{k}\right\} \quad(i=1, \ldots, n) \\
\left\{\sigma_{i}\right\}=\left\{\sqrt{\frac{1}{N} \sum_{k=1}^{N}\left[\left(x_{i}\right)_{k}-\mu_{i}\right]^{2}}\right\} \quad(i=1, \ldots, n)
\end{gathered}
$$

In the above formulas $N$ is a specified integer restricted to $1<N<M$.

Step 3: Generate $M$ new points $\left\{x_{i}\right\},(i=1, \ldots, n, r=1, \ldots, M)$ to replace the current population, less the best-fit individual, using the standard deviations (31) and the following vector of corrected average values:

$$
\left\{\mu_{i}^{2}\right\}=\left\{(1-\alpha) \cdot \mu_{i}+\alpha \cdot\left(x_{i}\right)_{\text {best }}\right\}
$$

where $\mu_{i}$ are given by the above formula (30) and $\alpha$ is a variable parameter:

$$
\alpha=q \cdot\left(G_{c} / G_{\max }\right)^{n}
$$

with $G_{c}$ the number of the current generation and $q$ a chosen constant between 0 and 1 (in the numerical examples below, $q$ has been considered equal to 1 ).

In order to ensure that the newly generated individuals satisfy the imposed side constraints, the following corrections were performed

$$
\begin{aligned}
& \text { IF } x_{i}<x_{i \text { min }} \text { THEN } x_{i}=x_{i \text { min }} \\
& \text { IF } x_{i}>x_{i \text { max }} \text { THEN } x_{i}=x_{i \text { max }}
\end{aligned}
$$

More details about this algorithm together with some benchmark-problem results can be found in the referred paper [39] where the capabilities of EDAs to solve constrained problems have been investigated for the first time.

In the same paper [40] it was reported that when the design space is very fragmented or it is reduced to scattered points only (as is the case with discrete or integer optimization problems), repair-by-crossover can be a very effective constraint-handling technique. According to this technique, a given infeasible point in the population is replaced with a new point generated through the crossover between this current point and the closest feasible point in the population (a midpoint crossover has been considered in particular).

The numerical results reported in the paper were the best out of 500 runs of the above algorithm with $M=80$ and $N=40$. The stopping criteria considered was exceeding 15000 calls of the objective function.

## Numerical Results

The design problem presented earlier and summarized in the Appendix was solved for a maximum outer diameter of the transmission $D_{\max }=220 \mathrm{~mm}$ and for the following forward transmission ratios: $i_{01}=3.11, i_{02}=1.84, i_{03}=1.0$ corresponding to a Chevrolet Corvette manual transmission. The reverse transmission ratio was imposed equal to the first forward gear $i_{R}=-3.11$, although in the original transmission this was slightly higher, viz. -3.22 .

For simplicity, a maximum norm-based objective function $f_{1}$ [Eq. (12)] with all weightings $w_{k}$ equal to 1.0 has been considered.

To facilitate the searching process, the teeth number combinations for which only assembly condition (29) holds were not rejected, but rather assigned the objective function 40-50 times its current value. This is because according to Ref. [41] there are alternative solutions available for the cases when equally spaced multiple planets cannot be assembled together as follows:
(a) One possibility is to assemble identical planets at different spacing angles (this approach is more conveniently applicable to planetary units restricted by only one assembly-condition equation, which is not the case of the current problem).
(b) In case of the planetary transmission in Fig. 2, equally spaced $p$ nonidentical compound planets can be assembled, provided that gears 2 and 3 are manufactured rotated relative to each other by a certain angle. Following [41], one out of $p$ compound planets numbered 1 is considered as reference. The $k$ th planet (counting clockwise) must be manufactured with gears 2 and 3 rotated relative to each other by the angle

$$
\begin{aligned}
\delta \varphi_{k} & =2 \pi \cdot \operatorname{Frac}\left[\frac{k-1}{p} \cdot\left(\frac{1}{r_{12}^{\prime}}-\frac{1}{r_{03}^{\prime}}\right)\right] \\
& =2 \pi \cdot \operatorname{Frac}\left[\frac{k-1}{p} \cdot\left(-\frac{N_{1}}{N_{2}}-\frac{N_{0}}{N_{3}}\right)\right]
\end{aligned}
$$

Since gears 2 and 3 have periodic profiles, angles $\delta \varphi_{k}$ are actually equivalent to much smaller angles, which may allow identically manufactured planets to be plastically torsioned at the desired offset angle.

In order to facilitate the design process, a visualization of the objective function $f_{1}$ has been performed by projecting its hypersurface down to the three-dimensional (3D) space of $\left(m_{1}, m_{3}, f_{1}\right)$. According to Ref. [42], the lower envelope of the hypersurface of a single valued function of more than two variables $f\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ projects down to the 3 D space formed with the function value $f$ and two of the variables, say $x_{1}$ and $x_{2}$, as the partial global minima function

$$
f_{] 3, \ldots, n}\left(x_{1}, x_{2}\right)=\text { global } \min _{x_{2}, \ldots, x_{n}} f\left(x_{1}, \ldots, x_{n}\right)
$$

where $x_{1}$ and $x_{2}$ are called scan variables and $x_{3, \ldots, n}$ are called search variables [42]. In a similar manner, by considering only one scan variable, the lower envelope of the same hypersurface can be plotted as a two-dimensional (2D) graph

$$
f_{] 2, \ldots, n}\left(x_{1}\right)=\text { global } \min _{x_{2}, \ldots, x_{n}} f\left(x_{1}, \ldots, x_{n}\right)
$$

Choosing as scan variables the module $m_{1}$ and $m_{3}$ of the gears, the graph in Fig. $4(a)$ has been generated for the case of equally spaced planets with identical compound gears 2 and 3. Similar plots have been generated [Fig. 5(a)] for the cases when the compound planets must be manufactured with gears 2 and 3 rotated at

![img-3.jpeg](img-3.jpeg)

Fig. 4 Projection of the lower envelope of objective function $f_{1}=\operatorname{Err}$ max with $N_{2} \neq N_{3}$ on the $\left(m_{1}, m_{3}, f_{1}\right)$ space (a), and plot of the corresponding outer diameter of the transmission (b) for the case of equally spaced identical planets
different angles. These plots [Figs. 4(a) and 5(a)] allow the designer to select a suboptimum teeth-number combination based on additional criteria, like the availability or cost of gear cutting tools, or the requirement of all gears having the same modulus, i.e., $m_{1}=m_{3}$. The accompanying graphs [Figs. 4(b) and 5(b)] show the actual maximum diameter of the transmission $D_{\max }$ calculated with the left-hand side of Eqs. (15) and (16), and provide additional information to the designer, who can select the teeth number combination and module $m_{1}, m_{3}$ which ensure an outer diameter of the transmission smaller than the actual imposed value $D_{\max }$. They also indicate whether or not an increase of the maximum allowed diameter of the transmission can provide further reduction of the departure between the imposed and the actual transmission ratios.

Referring back to Fig. 1, it is evident that it is more advantageous to manufacture planetary transmission with planets $2-3$ having identical gears 2 and 3 . The corresponding optimum solution can be obtained by minimizing objective function $f_{1}$ subject to the same constraints and additionally imposing $N_{2}=N_{3}$ and $m_{1}=m_{3}$. Figures 6(a) and 7(a) show 2D projections ( $m_{1}$ is the only scan variable) of the lower envelope of the objective-function's hypersurface when subject to these additional constraints. Figure $6(a)$ was generated for the case of equally spaced identical planets while Fig. 7(a) corresponds to the $p$ compound planets having gears 2 and 3 manufactured rotated at different relative angles according to Eq. (36).

The global optimum solution corresponding to the variants studied through the graphs in Figs. 4-7 are gathered in Table 2.
![img-4.jpeg](img-4.jpeg)

Fig. 5 Projection of the lower envelope of objective function $f_{1}=\operatorname{Err}$ max with $N_{2} \neq N_{3}$ on the $\left(m_{1}, m_{3}, f_{1}\right)$ space (a), and plot of the corresponding outer diameter of the transmission (b) for the case of equally spaced nonidentical compound planets 2-3

Two of these solutions (numbers 3 and 7) are shown drawn at scale in Figs. 8 and 9. Solution number 3 requires the three out of four compound planets (counting clockwise) to have their gears rotated relative to each other by $\pm 37.693^{\circ}, \pm 18.091^{\circ}$, and $\pm 55.784^{\circ}$, respectively, equivalent to the much smaller angles: $\pm 0.1639^{\circ}, \pm 0.1997^{\circ}$, and $\pm 0.0708^{\circ}$.

The transmission schematized in Fig. 9, however, can be considered the most convenient to manufacture due to the use of identical, equally spaced broad planets.

## Conclusions

The gear-teeth number synthesis of an automatic planetary transmission of the Ravigneaux type was solved with the aid of an Estimation of Distribution Algorithm. All possible assembly and interference avoidance requirements were accounted for in the form of constraints.

By allowing nonstandard involute gears to be used, an increase of the feasible domain was obtained, favorable to the design process. Visualization of the design space through partial global minima plots adds insight to the synthesis problem in that it allows selecting the numerical solution based on additional requirements, like reduced overall diameter of the transmission or using unified gear cutting tools in the manufacturing process.

The presented approach can be easily extended to the teeth number synthesis of automatic planetary transmission with more than three forward gears that include a Ravigneaux gear-set: When only simple planetary units are associated in an automatic transmission, the number of geometric constraints will occur in

![img-5.jpeg](img-5.jpeg)

Fig. 6 Projection of the lower envelope of objective function $f_{1}=$ Err max with $m_{1}=m_{2}$ and $N_{2}=N_{3}$ on the $\left(m_{1}, f_{1}\right)$ plane (a), and plot of the corresponding outer diameter of the transmission (b) for the case of equally spaced identical planets
![img-6.jpeg](img-6.jpeg)

Fig. 7 Projection of the lower envelope of objective function $f_{1}=\operatorname{Err} \max$ with $m_{1}=m_{2}$ and $N_{2}=N_{3}$ on the $\left(m_{1}, f_{1}\right)$ plane (a), and plot of the corresponding outer diameter of the transmission (b) for the case of equally spaced nonidentical planets 2-3

Table 2 Numerical results obtained through the optimization process ( $N_{2}$ value given corresponds to the maximum number of teeth idler 5 can have)

| Variant | 1,2 | 3 | 4 | 5,6 | 7 |
| :-- | :--: | :--: | :--: | :--: | :--: |
| Max | 0.523 | 0.526 | 0.529 | 0.530 | 0.530 |
| error | $28.4 \%$ | $28.6 \%$ | $28.7 \%$ | $28.5 \%$ | $28.5 \%$ |
| $N_{1}$ | 40 | 34 | 46 | 35 | 35 |
| $N_{2}$ | 21 | 25 | 36 | 27 | 28 |
| $N_{3}$ | 14 | 33 | $=\mathrm{N}_{2}$ | $=\mathrm{N}_{2}$ | $=\mathrm{N}_{2}$ |
| $N_{4}$ | 19 | 32 | 33 | 25 | 25 |
| $N_{5}$ | 16 | 23 | 40 | 30 | 28 |
| $N_{6}$ | 69 | 116 | 120 | 91 | 91 |
| $m_{1}$ | $2.25 /$ | 2.50 | 1.75 | $1.75 /$ | 2.00 |
| $m_{2}$ | 2.50 |  |  | 2.25 |  |
| $m_{3}$ | $2.50 /$ | 1.75 | 1.75 | $1.75 /$ | 2.00 |
| $m_{4}$ | 2.75 |  |  | 2.25 |  |
| $P$ | 5 | 4 | 3 | 3 | 3 |
| $i_{1}$ | 3.632 | 3.225 | 3.636 | 3.640 | 3.640 |
| $i_{2}$ | 2.363 | 2.366 | 2.369 | 2.364 | 2.364 |
| $i_{\mathrm{R}}$ | -2.588 | -2.585 | -2.609 | -2.600 | -2.600 |
| $D_{\max }$ | 189.0 | 215.0 | 214.4 | 163.6 | 187.0 |
| $\min$ |  |  |  |  |  |
| Identical | No | No | No | Yes | Yes |
| planets |  |  |  |  |  |

Fig. 8 Front view of the transmission with $N_{1}=34, N_{2}=25, N_{3}$ $=33, N_{2}=32, N_{3}=23, N_{4}=116, p=4$ and $m_{1}=2.5$ and $m_{2}$ $=1.75 \mathrm{~mm}$ (variant number 3 in Table 2)

![img-7.jpeg](img-7.jpeg)

Fig. 9 Front view of the transmission with $N_{1}=35, N_{2}=N_{3}=28$, $N_{4}=25, N_{5}=28, N_{6}=91, m_{1}=m_{3}=2 \mathrm{~mm}$ (variant number 7 in Table 2)
lesser number, although there will be additional equally-spacedplanet assembly condition requirements that must be accounted for in the form of constraints.

## Acknowledgments

The comments and suggestions upon an early version of the paper of Dr. Ilie Talpasanu and of the anonymous reviewers are acknowledged.

## Appendix

The optimum synthesis problem of the $3+1$ speed Ravigneaux transmission in Fig. 2 has been summarized in the following.

Find the integers $N_{1, \ldots, 6}$, number of planets $p$ and module $m_{1}$ and $m_{3}$ that minimize the function

$$
f_{1}(\ldots)=\max \left|i_{k}-i_{0 k}\right|(k=\{1,2, R\})
$$

where

$$
\begin{gathered}
i_{1}=N_{6} / N_{4} \text { and } i_{01}=3.11 \\
i_{2}=\frac{N_{4}\left(N_{1} N_{3}+N_{3} N_{4}\right)}{N_{1} N_{3}\left(N_{6}-N_{4}\right)} \text { and } i_{02}=1.84 \\
i_{R}=-\left(N_{2} N_{6}\right) /\left(N_{1} N_{3}\right) \text { and } i_{0 R}=-3.11
\end{gathered}
$$

subject to the following constraints

$$
\begin{gathered}
N_{1,4} \geqslant N_{5 \text { min }}=17 \\
N_{2,3,5} \geqslant N_{P \text { min }}=14 \\
m_{3}\left(N_{6}+2.5\right) \leqslant D_{\max } \\
m_{1}\left(N_{1}+N_{2}\right)+m_{1}\left(N_{2}+2\right) \leqslant D_{\max } \\
m_{3}\left(N_{4}+N_{5}\right)+m_{3}\left(N_{5}+2\right) \leqslant D_{\max } \\
\left|m_{1}\left(N_{1}+N_{2}\right)-m_{3}\left(N_{6}-N_{3}\right)\right| \leqslant m_{1}+m_{3} \\
\left(N_{1}+N_{2}\right) \cdot \sin (\pi / p)-N_{2}-2-\delta_{22} \geqslant 0 \\
\left(N_{6}-N_{3}\right) \cdot \sin (\pi / p)-N_{3}-2-\delta_{33} \geqslant 0 \\
\left(N_{4}+N_{5}\right) \cdot \sin (\pi / p)-N_{5}-2-\delta_{55} \geqslant 0
\end{gathered}
$$

$$
\begin{gathered}
\left(N_{6}-N_{3}\right)^{2}+\left(N_{4}+N_{5}\right)^{2}-2\left(N_{6}-N_{3}\right)\left(N_{4}+N_{5}\right) \cos \left(\frac{2 \pi}{p}-\beta\right) \\
\geqslant\left(N_{3}+N_{5}+2+\delta_{55}\right)^{2}
\end{gathered}
$$

with

$$
\begin{gathered}
\beta=\arccos \frac{\left(N_{6}-N_{3}\right)^{2}+\left(N_{4}+N_{5}\right)^{2}-\left(N_{3}+N_{5}\right)^{2}}{2 \cdot\left(N_{6}-N_{3}\right)\left(N_{4}+N_{5}\right)} \\
N_{6}-2 N_{3}-N_{4}-4-2 \delta_{34} \geqslant 0 \\
N_{6}-N_{4}-2 N_{5}-4-2 \delta_{56} \geqslant 0
\end{gathered}
$$

and equality constraints

$$
\left(N_{6}-N_{4}\right) / p=\text { integer }
$$

and

$$
\operatorname{Frac}\left(\frac{1}{p}\left|\frac{N_{1}}{N_{2}}+\frac{N_{6}}{N_{3}}\right|\right)=\left|\frac{A}{N_{2}} \pm \frac{B}{N_{3}}\right|
$$

where $\operatorname{Frac}(\ldots)$ is the factional part of the expression in parentheses, $A$ and $B$ are integers within

$$
0 \leqslant A<N_{2} / p \text { and } 0 \leqslant B<N_{3} / p
$$

The lower limit of $N_{6}$ determined from Eqs. (A15) and (A16) is

$$
N_{6} \geqslant N_{5 \text { min }}+2 N_{P \text { min }}+2+2 \cdot \min \left(\delta_{34}, \delta_{56}\right)
$$

Additional upper side constraints can be obtained as follows:
From inequality (A6)

$$
N_{6} \leqslant D_{\max } / m_{3 \text { min }}-2.5
$$

From inequality (A7)

$$
\begin{aligned}
& N_{1} \leqslant D_{\max } / m_{1 \text { min }}-2 N_{P \text { min }}-2 \\
& N_{2} \leqslant\left(D_{\max } / m_{1 \text { min }}-N_{5 \text { min }}-2\right) / 2
\end{aligned}
$$

From inequalities (A15) and (A21)

$$
N_{3} \leqslant\left(D_{\max } / m_{3 \text { min }}-N_{5 \text { min }}-6.5-2 \delta_{34}\right) / 2
$$

From inequalities (A16) and (A21)

$$
\begin{gathered}
N_{4} \leqslant D_{\max } / m_{3 \text { min }}-2 N_{P \text { min }}-6.5-2 \delta_{56} \\
N_{5} \leqslant\left(D_{\max } / m_{3 \text { min }}-N_{5 \text { min }}-6.5-2 \delta_{56}\right) / 2
\end{gathered}
$$

In the above equations the maximum admissible outer diameter is $D_{\max }=220 \mathrm{~mm}$, the number of identical planets $p$ can be 3,4 , or 5 , while module $m_{1}$ and $m_{3}$ can have the following discrete values: $1.75,2.0,2.25,2.5,2.75$, or 3.0 mm . The relative clearances between adjacent wheels $\delta_{22}, \delta_{33}, \delta_{55}, \delta_{35}, \delta_{34}$, and $\delta_{56}$ were considered all equal 0.5 .

## References

[1] Chatterjee, G., and Tsai, L. W., 1995, "Enumeration of Epicyclic-Type Automatic Transmission Gear Trains," SAE Trans., J. of Passenger Cars, 103, pp. 1415-1426.
[2] Chatterjee, G., and Tsai, L. W., 1996, "Computer Aided Sketching of Epicyclic-Type Automatic Transmission Gear Trains," ASME J. Mech. Des., 118, pp. 405-411.
[3] Hsu, C.-H., and Hsu, J.-J., 2000, "Epicyclic Gear Trains for Automotive Automatic Transmission", " Proc. Inst. Mech. Eng., Part D (J. Automob. Eng.), 214D, pp. 523-532.
[4] Johnson, R. C., and Towlig, K., 1967, "Creative Design of Epicyclic Gear Trains Using Number Synthesis," ASME J. Eng. Ind., 89, pp. 309-314.
[5] Lloyd, R. A., 1983, "Triple Epicyclic Four-clutch Six-ratio Change Speed System," Proc. Inst. Mech. Eng., 197C, pp. 127-140.
[6] Love, P. P., 1936, "Epicyclic Gearing," Proc. Inst. Mech. Eng., 134, pp. 547568 .
[7] Molian, S., 1971, "Kinematics of Compound Differential Mechanisms," Proc. Inst. Mech. Eng., 185, pp. 733-739.
[8] Ravigneaux, P., 1930, "Théorie Nouvelle sur les Trains Épicycloidaux et les Mouvements Relatifs," La Technique Automobile et Aérienne, 21, pp. 97106.

[9] Yan, H.-S., and Hsieh, L.-C., 1994, "Conceptual Design of Gear Differentials for Automotive Vehicles," ASME J. Mech. Des., 116, pp. 565-570.
[10] Fogarasy, A. A., and Smith, M. R., 1995, "A New Simplified Approach to the Kinematic Analysis and Design of Epicyclic Gearboxes," Proc. Inst. Mech. Eng., Part A, J. of Mechanical Engineering Science, 209C, pp. 49-53.
[11] Hsieh, H.-I., and Tsai, L.-W., 1995, "Kinematic Analysis of Epicyclic-Type Transmission Mechanisms Using the Concept of Fundamental Geared Entities," Proceedings of the ASME-DETC 1995, Vol. 1, pp. 545-552.
[12] Macmillan, R. H., 1949, "Epicyclic Gear Trains," The Engineer, 25, pp. 318320 .
[13] Merritt, H. E., 1941, "Epicyclic Gear Trains," The Engineer, 21, pp. 190-215.
[14] Wilson, W. G., 1932, "Epicyclic Gearing," Automob. Eng., 26, pp. 216-257.
[15] Macmillan, R. H., 1961, "Power Flow Loss in Differential Mechanisms," J. Mech. Eng. Sci., 3, pp. 37-41.
[16] Macmillan, R. H., 1965, "Analytical Study of Systems for Bifurcated Power Transmission," J. Mech. Eng. Sci., 7, pp. 40-47.
[17] Pennestri, E., and Freudenstein, F., 1993, "A Systematic Approach to PowerFlow and Static Force Analysis in Epicyclic Spur-Gear Trains," ASME J. Mech. Des., 115, pp. 639-644.
[18] Pennestri, E., and Valentini, P. P., 2003, "A Review of Formulas for the Mechanical Efficiency Analysis of Two Degrees-of-Freedom Epicyclic Gear Trains," ASME J. Mech. Des., 125, pp. 602-608.
[19] Chong, T. H., and Lee, J. S., 2000, "Genetic Algorithm Based Design for Gear Trains," Proceedings of the ASME-DETC 2000.
[20] Cleghorn, W. L., Fenton, R. G., and Fu, J.-F., 1989, "A General Method for Optimum Design of Gear Boxes Through Nonlinear Programming," Proceedings of the ASME-DETC 1989, Vol. 19-2, pp. 153-160.
[21] Deb, K., and Jain, S., 2003, "Multi-Speed Gearbox Design Using MultiObjective Evolutionary Algorithms," ASME J. Mech. Des., 125, pp. 610-619.
[22] Golinski, J., 1970, "Optimal Synthesis Problem Solved by Means of Nonlinear Programming and Random Methods," J. Mech., 5, pp. 285-309.
[23] Sandgren, E., 1990, "Nonlinear Integer and Discrete Programming in Mechanical Design Optimization," ASME J. Mech. Des., 112, pp. 223-229.
[24] Brewer, R. C., 1960, "Synthesis of Epicyclic Gear Trains Using the Velocity Ratio Spectrum," ASME J. Eng. Ind., 82, pp. 173-178.
[25] Kim, S. S., and Newcombe, W. R., 1979, "Computer Aided Kinematic Design of Planetary Gear Trains," Proceedings of the 5th World Congress on the Theory of Machines and Mechanisms, Montreal, CA, pp. 148-152.
[26] Pennestri, E., 1992, "Kinematic Synthesis of Ordinary and Epicyclic Gear Trains for a Prescribed Velocity Ratio," Proceedings of the ASME-DETC 1992, Vol. 44, pp. 75-82.
[27] Fitzgeorge, D., 1971, "Synthesis of Single-ratio and Multi-ratio Epicyclic Gear

Trains," Proc. Inst. Mech. Eng., 13, pp. 404-415.
[28] Pazak, A., Chrobak, J., and Klimo, V., 1984, "Method of the Kinematic Synthesis of the Epicyclic Gear Trains," International Symposium on Design and Synthesis, Tokyo, Japan, pp. 307-310.
[29] Sanger, D. J., 1972, "Synthesis of Multiple-Speed Transmissions of the Planetary-Gear Type," Proc. Inst. Mech. Eng., J. of Mechanical Engineering Science, 14, pp. 353-362.
[30] Bagci, C., 1990, "Efficient Methods for the Synthesis of Compound Planetary Differential Gear Trains for Multiple Speed Ratio Generation," Gear Technol., 7, pp. 16.
[31] McCue, J. J., and Olson, D. G., 1990, "Optimization of Complex Planetary Gear Trains." Proceedings of the ASME-DETC 1990, Vol. 26, pp. 57-62.
[32] Meng, C.-F., Lu, X.-N., Cha, J.-Z., and Shi, Z.-C., 1990, "Optimal Synthesis of Planetary Chain-link Compound Mechanisms," Proceedings of the ASMEDETC 1990, Vol. 26, pp. 181-184.
[33] Kahraman, A., Ligata, H., Kienzle, K., and Zini, D. M., 2004, "A Kinematics and Power Flow Analysis Methodology for Automatic Transmission Planetary Gear Trains," ASME J. Mech. Des., 126, pp. 1071-1081.
[34] Hooser, D. R., Luscher, A., and Regalado, I., 1999, "The Multi-Objective Optimization of Non-standard Gears Including Robustness," Proceedings of the 1999 AGMA Technical Conference, Paper 99FTM16.
[35] Rogers, J. L., and Bloubaum, C. L., 1994, "Ordering Design Tasks Based on Coupling Strengths," Proceedings of the Fifth Symposium of Multidisciplinary Analysis and Optimization, Panama City, FL, pp. 708-717.
[36] Lechner, G., and Naunheimer, H., 1999, Automotive Transmissions. Fundamentals. Selection, Design and Application, Springer, New York.
[37] Hlíd, A., Post, J., and Pfeiffer, F., 2002, "Simulation of a Ravigneaux Planetary Gear of an Automatic Transmission," VDI-Ber., 1665, pp. 491-506.
[38] Prayoonrat, S., and Wlaton, D., 1988, "Practical Approach to Optimum Gear Train Design," Comput.-Aided Des., 20, pp. 83-92.
[39] Larrunaga, P., and Lozano, J. A., 2002, Estimation of Distribution Algorithms. A New Tool for Evolutionary Computation, Kluwer, Dordrecht.
[40] Simionescu, P. A., Beale, D., and Dozier, G., 2004, "Constrained Optimization Problem Solving Using Estimation of Distribution Algorithms," 2004 Congress on Evolutionary Computation, June 20-23, 2004, Portland, OR, pp. 296302.
[41] Simionescu, P. A., 1998, "A Unified Approach to the Assembly Condition of Epicyclic Gears," ASME J. Mech. Des., 120, pp. 448-452.
[42] Simionescu, P. A., and Beale, D., 2004, "Visualization of Multivariable (Objective) Functions by Partial Global Optimization," Visual Comput., 20, pp. $665-681$.