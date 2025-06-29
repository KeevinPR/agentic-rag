# Hybrid optimization for charge planning problem in twin strands continuous casting production 

Jian $\mathrm{Yi}^{1,2} \otimes \cdot$ Shu-jin Jia ${ }^{2} \cdot$ Bin $\mathrm{Du}^{1,2}$<br>Received: 21 January 2020 / Revised: 7 July 2020 / Accepted: 8 July 2020 / Published online: 21 April 2021<br>(c) China Iron and Steel Research Institute Group 2021


#### Abstract

Charge planning is one of batching problems for steelmaking and continuous casting production, and its optimization will be conducive to subsequent cast planning. Charge planning problem in the twin strands continuous casting production was studied, where casting width of the odd strand might be different from that of the even strand. Considering the different widths in the twin strands, the resulting counterweights and the constraints of steelmaking and continuous casting, a multiobjective optimization model was established to minimize the number of charges, the number of scale pairs, the surplus and the upgrading costs of steel grades. Furthermore, a hybrid optimization algorithm combined with heuristic and mutationbased estimation of distribution algorithm was proposed to solve the model. Experiments were conducted on several groups of test data collected from practical production orders of Baosteel. The computational results demonstrate that the proposed algorithm can generate better solutions than the manual method. The proposed model and algorithm proved to be effective and practical.


Keywords Steelmaking $\cdot$ Continuous casting $\cdot$ Production planning $\cdot$ Charge $\cdot$ Cast $\cdot$ Estimation of distribution algorithm

## 1 Introduction

Steelmaking and continuous casting (SCC) are two critical parts in steel manufacturing that are closely related [1, 2]. In the SCC production process, effective planning and scheduling are crucial to raise productivity and have been widely studied [3]. Tang and Wang [4] divided the SCC production into two types of decisions: scheduling decisions and batching decisions. The scheduling decisions are production scheduling problems, while the batching decisions are production planning problems, which include charge planning and cast planning. Charge planning refers to that orders are converted into dummy slabs by the production design, and then, dummy slabs are consolidated into charges according to the converter's capacity for

[^0]smelting. Cast planning refers to that charges are grouped into casts according to the rules of SCC.

There have been many studies on production scheduling problems [5-14] and production planning problems [15-24] for the SCC process. The methods to study the SCC production planning mainly include mathematical programming [15], exact algorithm [16, 17], heuristic algorithm [4, 18, 19], intelligence optimization [20-22] and hybrid optimization [23, 24].

As for mathematical programming, Bellabdaoui and Teghem [15] presented a mixed-integer linear programming model for the continuous casting planning and used standard software packages to solve it. As for exact algorithm, Tang et al. [16] studied an integrated charge batching and casting width selection problem and developed a column generationbased branch-and-price solution approach. Yi et al. [17] established a multi-objective model for the continuous casting production planning problem and presented a column generation-based optimization algorithm. As for heuristic algorithm, Tang and Wang [4] investigated two batching problems for steelmaking and continuous casting production, formulated them as integer programming models and then developed two heuristic algorithms for the corresponding batching


[^0]:    $\boxtimes$ Jian Yi
    yijian@baosteel.com
    1 College of Information Science and Engineering, Northeastern University, Shenyang 110819, Liaoning, China
    2 Institute of Intelligent Manufacturing, Baosteel Central Research Institute, Shanghai 201900, China

problems. Dong et al. [18] proposed a multi-objective model for the integrated tundish planning problem and then developed two improved variable neighborhood local search methods. Song [19] generated an integrated formulation for the cast design problem by introducing multilayer network representation and derived a heuristic algorithm. As for intelligence optimization, Liu et al. [20] formulated a multiobjective order-planning model for manufacturing steel sheets, transferred the multiple objectives into a single one by the weighted-sum approach and designed a specific particle swarm optimization algorithm. Li et al. [21] proposed an effective fruit fly optimization algorithm to solve the steelmaking casting problem. Lin et al. [22] constructed a multiobjective optimization model for the integrated production planning in the steel industry and then proposed a novel approach based on a modified interval multi-objective optimization evolutionary algorithm. As for hybrid optimization, Zhu et al. [23] proposed a novel optimization model combined with parallel-backward inferring algorithm and genetic algorithm to improve the efficiency and performance for production planning in steelmaking and continuous casting process. Sun et al. [24] proposed a three-level batching policy consisting of charge planning, tundish planning and cast planning and then developed a hybrid optimal strategy combined with the iterated local search, variable neighborhood search and ant colony optimization.

This paper focuses on charge planning problem and uses a hybrid optimization method to solve it. Charge planning problem is important in the SCC production, which should consider the requirements of converters and casters as well. For a converter, it is required that the ordered slabs combined in a charge have the same steel grade and the total mass of ordered slabs cannot exceed the upper bound of the converter's capacity. If the total mass of ordered slabs in a charge is less than the lower bound of the converter's capacity, the open ordered slabs are filled in the charge. The open ordered slabs are also called the surplus [17], with which there are no corresponding orders. For a caster, it is required that the thickness should be the same and the width range should be intersected if the ordered slabs are consolidated together into a charge. This paper extends the problem by considering the twin strands continuous casting production and allowing different casting widths between the odd strand and the even strand.

## 2 Charge planning problem in twin strands continuous casting production

### 2.1 Twin-strand caster

The caster can be classified as a single-strand caster and a multi-strand caster. One typical multi-strand caster is the twin-strand caster (Fig. 1), whose two strands are called the odd strand and the even strand. The two strands may have different casting widths denoted by $W^{\text {odd }}$ and $W^{\text {even }}$, but they must keep the balance of time in the continuous casting production. It means that the two strands should start and end simultaneously in the continuous casting production. In this case, the total mass of slabs in the odd strand and the total mass of slabs in the even strand in a charge are defined as the counterweights denoted by $G^{\text {odd }}$ and $G^{\text {even }}$.

Generally, a caster has many scales because its available casting widths are scaled by the multiple of 50 mm . For the odd strand and the even strand of a twin-strand caster, the number of scales is the same. The casters at Baosteel have 24 scales, and their casting widths vary from 900 to 2050 mm . For scale $r \in\{1, \ldots, 24\}$, the corresponding casting width is $(850+50 r) \mathrm{mm}$.

### 2.2 Counterweight calculation

It is assumed that $G$ is the capacity of converter, while $G^{\min }$ and $G^{\max }$ are the lower bound and the upper bound of converter's capacity, respectively. For each charge, the total mass of slabs in the odd strand and the one in the even strand are the same if the casting widths of two strands are the same. Otherwise, they are not the same. To maintain the balance of time between two strands, the counterweights need to be calculated. The counterweights are related not only to the casting widths of two strands, but also to the casting speeds. The casting speed relies on the casting width, and each casting width can correspond to a fixed casting speed. The counterweights are calculated as follows:

$$
\left\{\begin{array}{l}
G^{\text {odd }}=\frac{W^{\text {odd }} \cdot v^{\text {odd }}}{W^{\text {odd }} \cdot v^{\text {odd }}+W^{\text {even }} \cdot v^{\text {even }}} \cdot G \\
G^{\text {even }}=\frac{W^{\text {even }} \cdot v^{\text {even }}}{W^{\text {odd }} \cdot v^{\text {odd }}+W^{\text {even }} \cdot v^{\text {even }}} \cdot G
\end{array}\right.
$$

where $v^{\text {odd }}$ and $v^{\text {even }}$ are casting speeds of the odd strand and the even strand, respectively.

### 2.3 Problem description

The dummy slabs with the same thickness derived from $n$ orders are required to be consolidated into charges that are arranged to produce in the twin-strand caster. For order $i \in\{1, \ldots, n\}$, the set of its steel grades is marked as $S_{i}$, the casting wide range is $W_{\text {min }}^{\text {min }}-W_{\text {max }}^{\text {max }}$, the single slab mass is $G_{i}$, and the demand for slabs is $D_{i}$. For each charge, casting width of the odd strand may be different from that of the even strand; thus, it needs to determine in which charge, at which strand and on what width every dummy slab should

![img-0.jpeg](img-0.jpeg)

Fig. 1 Schematic of a twin-strand caster
be consolidated. The goal is to minimize the surplus, the number of casting widths and the upgrading costs of steel grades. Specifically, for the dummy slabs that are consolidated into the same charge, the requirements to be met are as follows:
(1) Steel grades must be the same;
(2) The total mass of slabs is not more than the upper bound of the converter's capacity;
(3) The width range should be intersected and can correspond to one scale of the caster at least if arranged on the same strand;
(4) The counterweights are required.

## 3 Mathematical modeling

### 3.1 Pattern

To facilitate modeling, a pattern is firstly defined which is the set of charges with the same steel grade, the same casting width of the odd strand, and the same casting width of the even strand. It is assumed that there are $m$ steel grades for these $n$ orders and $q$ scales for the twin-strand caster, and then, the number of patterns is $m q^{2}$, where $m=$ $\left|S^{\text {all }}\right|$ and $S^{\text {all }}=\bigcup_{i=1}^{n} S_{i}$. Because of the symmetry between the odd strand and the even strand, the number of patterns can be reduced to $m q(q+1) / 2$ and all patterns can be listed.

Each pattern has a unique steel grade, odd strand's casting width and even strand's casting width. For example, pattern $((u-1) \cdot q(q+1) / 2+r(r-1) / 2+r^{\prime})$ indicates that steel grade $S_{u}^{\text {all }}$ is used in this pattern, casting width of the odd strand is $(850+50 r)$ and casting width of the even strand is $\left(850+50 r^{\prime}\right)$, where $u=1,2, \ldots, m$, $r=1,2, \ldots, q$, and $r^{\prime}=1,2, \ldots, r$. For this pattern, the following data can be calculated in advance.
(i) According to Eq. (1), its counterweights can be predetermined:

$$
\left\{\begin{array}{l}
G_{(u-1) \cdot q(q+1) / 2+r(r-1) / 2+r^{\prime}}^{\text {old }}=\frac{(850+50 r) \cdot v_{r}^{\text {old }}}{\left(850+50 r\right) \cdot v_{r}^{\text {old }}+\left(850+50 r^{\prime}\right) \cdot v_{r}^{\text {even }}} \cdot G^{\text {max }} \\
G_{(u-1) \cdot q(q+1) / 2+r(r-1) / 2+r^{\prime}}^{\text {even }}=\frac{\left(850+50 r^{\prime}\right) \cdot v_{r}^{\text {even }}}{\left(850+50 r\right) \cdot v_{r}^{\text {old }}+\left(850+50 r^{\prime}\right) \cdot v_{r}^{\text {even }}} \cdot G^{\text {max }}
\end{array}\right.
$$

(ii) Let $E_{i,(u-1) \cdot q(q+1) / 2+r(r-1) / 2+r^{\prime}}^{\text {odd }}$ and $E_{i,(u-1) \cdot q(q+1) / 2+r(r-1) / 2+r^{\prime}}^{\text {even }}$ indicate whether order $i$ can be consolidated in the odd strand and the even strand of this pattern, respectively. They can be predetermined as follows:
$E_{i,(u-1) \cdot q(q+1) / 2+r(r-1) / 2+r^{\prime}}^{\text {odd }}=\left\{\begin{array}{r}1, \text { if } W_{i}^{\min } \leq 850+50 r \leq W_{i}^{\max } \\ 0, \text { otherwise }\end{array}\right.$
$E_{i,(u-1) \cdot q(q+1) / 2+r(r-1) / 2+r^{\prime}}^{\text {even }}=\left\{\begin{array}{r}1, \text { if } W_{i}^{\min } \leq 850+50 r^{\prime} \leq W_{i}^{\max } \\ 0, \text { otherwise }\end{array}\right.$
(iii) Let $C_{i,(u-1) \cdot q(q+1) / 2+r(r-1) / 2+r^{\prime}}$ denote the upgrading cost of steel grade if the order $i$ is consolidated in this pattern, which can be predetermined as follows:
$C_{i,(u-1) \cdot q(q+1) / 2+r(r-1) / 2+r^{\prime}}=\left\{\begin{array}{r}c, \text { if } S_{u}^{\text {all }} \in S_{i} \\ \infty, \text { if } S_{u}^{\text {all }} \notin S_{i}\end{array}\right.$
where $c$ is the index of $S_{u}^{\text {all }}$ in $S_{i}$ when $S_{u}^{\text {all }} \in S_{i}$.
Therefore, for each pattern $t \in\{1, \ldots, m q(q+1) / 2\}$ and each order $i \in\{1, \ldots, n\}, G_{i}^{\text {odd }}, G_{i}^{\text {even }}, E_{u}^{\text {odd }}, E_{u}^{\text {even }}$ and $C_{i t}$ can all be obtained according to Eqs. (2)-(5). $G_{i}^{\text {odd }}$ and $G_{i}^{\text {even }}$ are the counterweights of pattern $t$ in the odd strand and the even strand, respectively. $E_{u}^{\text {odd }}$ and $E_{u}^{\text {even }}$ are binary flags indicating whether order $i$ can be consolidated in the odd strand and the even strand of pattern $t$, respectively. $C_{i t}$ is the upgrading cost of steel grade when a slab of order $i$ is consolidated in pattern $t$.

### 3.2 Scale pair

Scales $r$ and $r^{\prime}$ are corresponding to casting widths of the odd strand and the even strand, respectively. It is assumed that casting width of the odd strand is always no less than

that of the even strand, i.e., $r \geq r^{\prime}$. And then, $\left(r, r^{\prime}\right)$ is called scale pair, where $r=1,2, \ldots, q$, and $r^{\prime}=1,2, \ldots, r$. It is obvious that the number of scale pairs is $q(q+1) / 2$. Suppose that $F_{i k}$ indicates whether scale pair $k$ is used in pattern $t$. If scale pair $k$ is used in pattern $t$, then $F_{i k}=1$; otherwise, $F_{i k}=0$. Therefore, $F_{i k}$ can be determined in advance for all patterns and all scale pairs, where $t=1,2, \ldots, m q(q+1) / 2$, and $k=1,2, \ldots, q(q+1) / 2$. It is expected that the least scale pairs should be used in this problem.

### 3.3 Mathematical model

The model can be described as follows:
$\min \sum_{t \in O} \alpha_{t}$
$\min \sum_{k \in H} \beta_{k}$
$\min \sum_{t \in O} \chi_{t}$
$\min \sum_{i \in N} \sum_{t \in O} C_{i t} \cdot\left(x_{i t}^{\text {odd }}+x_{i t}^{\text {even }}\right)$
s.t.
$\sum_{t \in O}\left(x_{i t}^{\text {odd }}+x_{i t}^{\text {even }}\right)=D_{i}, i \in N$
$x_{i t}^{\text {odd }} \leq M \cdot E_{i t}^{\text {odd }}, i \in N, t \in O$
$x_{i t}^{\text {even }} \leq M \cdot E_{i t}^{\text {even }}, i \in N, t \in O$
$y_{t} \leq \sum_{t \in N}\left(x_{t t}^{\text {odd }}+x_{i t}^{\text {even }}\right) \leq M \cdot y_{t}, t \in O$
$\beta_{k} \leq \sum_{t \in O} y_{t} \cdot F_{t k} \leq M \cdot \beta_{k}, k \in H$
$G_{t}^{\text {odd }} \cdot\left(\alpha_{t}^{\text {odd }}-1\right) \leq \sum_{i \in N} G_{i} \cdot x_{i t}^{\text {odd }} \leq G_{t}^{\text {odd }} \cdot \alpha_{t}^{\text {odd }}, t \in O$
$G_{t}^{\text {even }} \cdot\left(\alpha_{t}^{\text {even }}-1\right) \leq \sum_{i \in N} G_{i} \cdot x_{i t}^{\text {even }} \leq G_{t}^{\text {even }} \cdot \alpha_{t}^{\text {even }}, t \in O$
$\alpha_{t}^{\text {odd }}-\alpha_{t}^{\text {even }}=c_{t}^{\text {odd }}-c_{t}^{\text {even }}, t \in O$
$c_{t}^{\text {odd }}+\varepsilon_{t}^{\text {even }} \leq 1, t \in O$
$\alpha_{t} \geq \alpha_{t}^{\text {odd }}, t \in O$
$\alpha_{t} \geq \alpha_{t}^{\text {even }}, t \in O$
$G^{\min } \cdot \alpha_{t} \leq \chi_{t}+\sum_{i \in N} G_{i} \cdot\left(x_{i t}^{\text {odd }}+x_{i t}^{\text {even }}\right) \leq G^{\max } \cdot \alpha_{t}, t \in O$
where $O=\{1, \ldots, m q(q+1) / 2\}, H=\{1, \ldots, q(q+1) / 2\}$, $N=\{1, \ldots, n\}$, and $M$ is a very large number, while $x_{i t}^{\text {odd }}$,
$x_{i t}^{\text {even }}, y_{t}, \alpha_{t}^{\text {odd }}, \alpha_{t}^{\text {even }}, \alpha_{t}, c_{t}^{\text {odd }}, c_{t}^{\text {even }}, \beta_{k}$, and $\chi_{t}$ are the decision variables. $x_{i t}^{\text {odd }}$ and $x_{i t}^{\text {even }}$ are nonnegative integer variables representing the number of dummy slabs when order $i$ is consolidated in the odd strand and the even strand of pattern $t$, respectively. $y_{t}$ is a binary variable, which is equal to 1 if pattern $t$ is used, otherwise 0 . $\alpha_{t}^{\text {odd }}$ and $\alpha_{t}^{\text {even }}$ are nonnegative integer variables representing the number of charges in the odd strand and the even strand of pattern $t$, respectively. $\alpha_{t}$ is a nonnegative integer variable representing the number of charges in pattern $t . c_{t}^{\text {odd }}$ and $c_{t}^{\text {even }}$ are nonnegative integer variables. If $\alpha_{t}^{\text {odd }}>\alpha_{t}^{\text {even }}$, then $c_{t}^{\text {odd }}=$ $\alpha_{t}^{\text {odd }}-\alpha_{t}^{\text {even }}$ and $c_{t}^{\text {even }}=0$. If $\alpha_{t}^{\text {odd }}<\alpha_{t}^{\text {even }}$, then $c_{t}^{\text {odd }}=0$ and $c_{t}^{\text {even }}=\alpha_{t}^{\text {even }}-\alpha_{t}^{\text {odd }}$. If $\alpha_{t}^{\text {odd }}=\alpha_{t}^{\text {even }}$, then $c_{t}^{\text {odd }}=0$ and $c_{t}^{\text {even }}=0 . \beta_{k}$ is a binary variable, which is equal to 1 if scale pair $k$ is used, otherwise $0 . \chi_{t}$ is a nonnegative real variable indicating the surplus of pattern $t$.

Objectives (6)-(9) are to minimize the number of charges, the number of scale pairs, the surplus and the upgrading costs of steel grades, respectively. Constraint (10) is the demand for dummy slabs of each order. Constraints (11) and (12) indicate whether the dummy slab of order $i$ can be consolidated in the odd strand and the even strand of pattern $t$, respectively. Constraint (13) represents that a pattern is used if any dummy slab is consolidated in its odd strand or even strand. Constraint (14) indicates whether a scale pair is used. Constraints (15) and (16) calculate the number of charges in the odd strand and the number of charges in the even strand for each pattern, respectively, while constraint (17) is the difference between the two numbers, and constraint (18) ensures that the absolute value of the difference is not more than 1 . Constraints (19) and (20) guarantee that the number of charges for each pattern is the maximum between the two numbers. Constraint (21) calculates the surplus for each pattern.

## 4 Solution approach

The estimation of distribution algorithm (EDA) [25] is an evolutionary algorithm based on probabilistic statistics, which is very suitable for solving high-dimensional problems by using a probability model to describe the distribution information of candidate solutions in solution space. This paper uses a heuristic method to produce the set of patterns and then designs a mutation-based EDA to solve the model.

### 4.1 Heuristic

The number of patterns involved in the model is $m q(q+1) / 2$. However, for a specific batch of orders, the

number of patterns can be reduced on account of order structure. A heuristic method is proposed below.
(1) For each order $i$, the casting width range is converted:

$$
\left\{\begin{array}{l}
r_{i}^{\min }=\left[\frac{\left(W_{i}^{\min }-850\right)}{50}\right. \\
r_{i}^{\max }=\left[\frac{\left(W_{i}^{\max }-850\right)}{50}\right], i \in N
\end{array}\right.
$$

where the symbol $\lceil x\rceil$ represents the minimum integer that is no less than $x$; and $\lfloor x\rfloor$ represents the maximum integer that is no more than $x$.
(2) All the orders are grouped into the subsets according to their steel grades.
(3) For each subset of orders $N_{u}=\left\{i \mid S_{u}^{\text {all }} \in S_{i}, i \in N\right\}$ with identical steel grade $S_{u}^{\text {all }}$, the set of available scales is obtained: $R_{u}=\bigcup_{i^{\prime} \in N_{u}}\left\{r \mid r_{i^{\prime}}^{\min } \leq r \leq r_{i^{\prime}}^{\max }\right\}$. Set $R^{\text {all }}=\bigcup_{k=1}^{m} R_{u}$.
(4) The real number of patterns is calculated: $o=\sum_{u=1}^{m}\left|R_{u}\right|\left(\left|R_{u}\right|+1\right) / 2$. Set $O=\{1, \ldots, o\}$.
(5) The real number of scale pairs is calculated: $h=\left|R^{\text {all }}\right|\left(\left|R^{\text {all }}\right|+1\right) / 2$. Set $H=\{1, \ldots, h\}$.

### 4.2 Mutation-based EDA

### 4.2.1 Encoding

The chromosome is designed as $\boldsymbol{x}=\left(x_{i j}\right), i \in N, j \in D_{i}$, where $x_{i j} \in\{1, \ldots, 2 o\}$ contains the following gene information:
(1) If $1 \leq x_{i j} \leq o$, then slab $j$ of order $i$ is consolidated in the odd strand of pattern $x_{i j}$;
(2) If $o<x_{i j} \leq 2 o$, then slab $j$ of order $i$ is consolidated in the even strand of pattern $\left(x_{i j}-o\right)$.

Therefore, $x_{i j}$ represents the pattern and strand information when slab $j$ of order $i$ is consolidated.

### 4.2.2 Probability vector

The probability vector is the core of EDA. Through the probability vector and its updating, the spatial distribution of solution and the evolution trend of the population are described. According to the chromosome, a probability vector is established as below: $\boldsymbol{P}(\boldsymbol{x})=\left(P_{v}\left(x_{i j}\right)\right)$, where $P_{v}\left(x_{i j}\right)$ represents the probability of $x_{i j}=v, v \in\{1, \ldots, 2 o\}$.

Set $O^{\prime}=\{1, \ldots, 2 o\}$. For order $i$ and pattern $t$, if $E_{i t}^{\text {odd }}=$ 0 or $C_{i t}=\infty$, it means $x_{i j} \in O^{\prime} \backslash\{t\}$. Similarly, if $E_{i t}^{\text {even }}=0$ or $C_{i t}=\infty$, it means $x_{i j} \in O^{\prime} \backslash\{t+o\}$. Thus, the domain of $x_{i j}$ is $B_{i}=O^{\prime} \backslash\left\{t \mid E_{i t}^{\text {odd }}=0\right.$ or $\left.C_{i t}=\infty, t \in O\right\} \backslash\{t+o\}$

$E_{i t}^{\text {even }}=0$ or $C_{i t}=\infty, t \in O\} . \mathrm{It}$ is assumed that $b_{i}$ is the number of elements in $B_{i}$. The probability vector in generation $L$ is denoted by $\left(P_{v}^{L}\left(x_{i j}\right)\right)$. In generation $0, P_{v}^{0}\left(x_{i j}\right)$ is initialized as follows:
$P_{v}^{0}\left(x_{i j}\right)=\left\{\begin{array}{l}1 / b_{i}, \text { if } v \in B_{i} \\ 0, \text { if } v \notin B_{i}\end{array}, i \in N, j \in D_{i}, v \in O^{\prime}\right.$
In generation $L$, new individuals are generated by randomly sampling the probability vector based on roulette wheel selection method. The sampling process is listed below:
(1) For slab $j$ of order $i, P_{1}^{L}\left(x_{i j}\right), P_{2}^{L}\left(x_{i j}\right), \ldots, P_{v}^{L}\left(x_{i j}\right), \ldots$, $P_{2 o}^{L}\left(x_{i j}\right)$ make up of the proportions in roulette wheel.
(2) According to the roulette wheel selection, a random number between 0 and 1 is generated to determine the value of $x_{i j}$.
(3) For all slabs and all orders, repeat steps (1) to (2).

After new individuals are generated to form the new population, the probability vector in generation $L+1$ is constructed and updated by the following strategy:
$\left\{\begin{array}{l}P_{v}^{L+1}\left(x_{i j}\right)=(1-\lambda) \cdot P_{v}^{L}\left(x_{i j}\right)+\lambda \cdot \phi\left(v, x_{i j}\right) \\ P_{v}^{L+1}\left(x_{i j}\right)=P_{v}^{L+1}\left(x_{i j}\right) / \sum_{v^{\prime} \in O^{\prime}} P_{v^{\prime}}^{L+1}\left(x_{i j}\right) \quad, i \in N, j \in D_{i}, v \in O^{\prime}\end{array}\right.$
where $\lambda \in(0,1)$ is the learning rate, and $\phi\left(v, x_{i j}\right)$ represents the frequency of $x_{i j}=v$ in the new population.

### 4.2.3 Mutation

Mutation in evolutionary algorithms is to introduce new genetic material and maintain a certain level of diversity in a population. After a new individual is generated by sampling process, the following mutation strategy is used.
(1) Generate a random number between 1 and $n$ to pick a order, such as order $i^{\prime}$.
(2) Generate a random number between 1 and $D_{i^{\prime}}$ to pick a slab of order $i^{\prime}$, such as slab $j^{\prime}$.
(3) Randomly select an element from $B_{i^{\prime}}$ as the value of $x_{i^{\prime} j^{\prime}}$.

### 4.2.4 Fitness evaluation

For an individual, the value of its fitness is evaluated as below:
$f=-\left[f_{1} \cdot \sum_{i \in D} \chi_{i}+f_{2} \cdot \sum_{k \in H} \beta_{k}+f_{3} \cdot \sum_{i \in D} \chi_{k}+f_{4} \sum_{i \in N} \sum_{j \in D_{i}} C_{i, \phi\left\{v_{i j}\right\}}\right]$
where

$\psi\left(x_{i j}\right)= \begin{cases}x_{i j}, & \text { if } 1 \leq x_{i j} \leq o \\ x_{i j}-o, & \text { if } o<x_{i j} \leq 2 o\end{cases}$
$f_{1}, f_{2}, f_{3}$ and $f_{4}$ are the weights of four objectives; $\beta_{k}$ is given by constraint (10); and $\alpha_{t}$ and $\chi_{t}$ need to be calculated by Eqs. (26)-(29).

$$
\begin{aligned}
& \alpha_{t}^{\text {odd }}=\left[\frac{\sum_{i \in N} \sum_{j \in D_{i}} G_{i} \cdot \theta^{\text {odd }}\left(t, x_{i j}\right)}{G_{i}^{\text {odd }}}\right], t \in O \\
& \alpha_{t}^{\text {even }}=\left[\frac{\sum_{i \in N} \sum_{j \in D_{i}} G_{i} \cdot \theta^{\text {even }}\left(t, x_{i j}\right)}{G_{i}^{\text {even }}}\right], t \in O \\
& \alpha_{t}=\sigma\left(\alpha_{t}^{\text {odd }}, \alpha_{t}^{\text {even }}\right) \cdot \max \left\{\alpha_{t}^{\text {odd }}, \alpha_{t}^{\text {even }}\right\}, t \in O \\
& \chi_{t}=\max \left\{0,\left(\alpha_{t} \cdot G^{\min }-\sum_{i \in N} \sum_{j \in D_{i}} G_{i} \cdot \theta\left(t, x_{i j}\right)\right)\right\}, t \in O
\end{aligned}
$$

where
$\theta^{\text {odd }}\left(t, x_{i j}\right)= \begin{cases}1, & \text { if } x_{i j}=t \\ 0, & \text { otherwise }\end{cases}$
$\theta^{\text {even }}\left(t, x_{i j}\right)=\left\{\begin{array}{c}1, \text { if } x_{i j}=t+o \\ 0, \text { otherwise }\end{array}\right.$
$\theta\left(t, x_{i j}\right)=\left\{\begin{array}{c}1, \text { if } \psi\left(x_{i j}\right)=t \\ 0, \text { otherwise }\end{array}\right.$
$\sigma\left(\alpha_{t}^{\text {odd }}, \alpha_{t}^{\text {even }}\right)=\left\{\begin{array}{c}1, \text { if }\left|\alpha_{t}^{\text {odd }}-\alpha_{t}^{\text {even }}\right| \leq 1, \\ M, \text { otherwise }\end{array}\right.$
Note that the function $\sigma\left(\alpha_{t}^{\text {odd }}, \alpha_{t}^{\text {even }}\right)$ is the penalty to violate constraint (18).

### 4.3 Algorithm procedure

Algorithm 1 lists the procedure of hybrid optimization algorithm combined with heuristic and mutation-based EDA. The stopping criterion is specified in terms of a maximum number of generations (i.e., $L^{\max }$ ). $X^{\text {local }}$ is the local optimal individual, while $X^{\text {best }}$ is the global optimal individual. $a$ is the population size.

```
Algorithm 1
{
    Determine the set of patterns and the set of scale pairs by using the heuristic;
    Calculate the parameters \(G_{i}^{\text {odd }}, G_{i}^{\text {even }}, C_{i i}, E_{i i}^{\text {odd }}, E_{i i}^{\text {even }}, F_{i k}\) for each pattern;
    Initialize the probability vector \(\left(P_{v}^{i i}\left(x_{i j}\right)\right)\) and \(a\);
    \(L=0\);
    while \(\left(L \leq L^{\text {mes }}\right)\{\)
        Randomly sample the probability vector \(\left(P_{v}^{L}\left(x_{i j}\right)\right)\) to generate \(a\) individuals;
        Mutate \(a\) individuals according to the mutation strategy;
        Evaluate the fitness for \(2 a\) individuals;
        Sort \(2 a\) individuals by their fitness in descending order;
        Select the front \(a\) individuals as the new population;
        \(X^{\text {local }}=\mathrm{the}\) first individual of new population;
        \(X^{\text {best }}=\max _{\text {_fitness }}\left(X^{\text {best }}, X^{\text {local }}\right)\);
        Construct \(\hat{P}_{v}^{L+1}\left(x_{i j}\right)\) by the new population;
        \(L++\)
    \}
    Output the global optimal individual \(X^{\text {best }}\);
```

## 5 Experiment and analysis

Experiments are conducted on four groups of test data collected from practical production orders of Baosteel, which are shown in Table 1. The proposed algorithm is coded in Microsoft Visual C++, and the computational experiments are performed on a PC with Intel Pentium-4 2.8 GHz CPU and 2 GB RAM.

### 5.1 Parameter setting

The technological parameters are as follows: $G^{\min }=290$, $G^{\max }=310$, and $q=24$. With considering the importance of four objectives, the weighted parameters in the model are set as below: $f_{1}=100, f_{2}=10, f_{3}=0.1$, and $f_{4}=1$. As for the algorithm parameters, $L^{\max }$ is set to 1000 , while $\lambda$ and $a$ are undetermined. In order to analyze the influence of algorithm parameters, the following trials on Test1 are conducted:
(1) Learning rate is fixed as 0.1 and population size is set to $20,50,80$ and 110 , respectively.
(2) Population size is fixed as 80 and the learning rate is set to $0.004,0.02,0.1$ and 0.5 , respectively.

Test1 is computed 10 times with each type of parameters. Box plots based on these trials are shown in Fig. 2. Figure 2a is used to analyze the influence of population size on Test1 when learning rate is fixed, while Fig. 2b is used to analyze the influence of learning rate on Test1 when population size is fixed. Each rectangular box is a statistic for 10 computations on Test1 with determined $\lambda$ and $a$, displaying the dispersion of results.

As seen from Fig. 2, increasing the population size can improve the algorithm performance, because larger population is conducive to a more comprehensive search for solution space. However, large population will cause an increase in computational complexity. When the population reaches a certain size, the marginal improvement will be trivial. Moreover, the learning rate should not be too high or too low. If the learning rate is too high, the population will converge to local optimal solution, which turns out to be premature. If the learning rate is too low, the convergence speed tends to be slow and the ability of searching for the optimum gets worse. Therefore, population size and learning rate should be set appropriately considering the performance and efficiency. In the next computations on four groups of test data, the two parameters are set as follows: $\lambda=0.1$, and $a=80$.

### 5.2 Computational results

Each test datum is computed 10 times with the proposed algorithm, and the best result is kept. To demonstrate the proposed algorithm, the manual method is also used to produce the result. The manual method for charge planning is a greedy procedure. Firstly, all slabs are separated into subsets according to their first steel grades (it is not easy to think about the upgrading costs of steel grades in the manual method because the combinations of steel grades are very complex), and the statistics of their mass are displayed in a matrix in which rows represent steel grades and columns represent widths. Secondly, the planner analyzes the order structure by observing the matrix, selects a subset of slabs with the same steel grade into a pool and determines two sets of casting widths covering them,

Table 1 Four groups of order data

![img-1.jpeg](img-1.jpeg)

Fig. 2 Influence of algorithm parameters on Test1
corresponding to two strands. Finally, these selected slabs in the pool are consolidated into one or several charges (i.e., cast-lot) with determined casting widths of the odd strand and the even strand. Repeat these steps until all slabs are consolidated.

The computational results are reported in Table 2.
In Table 2, the column labelled Condition represents the limit condition for casting width of the odd strand and the even strand, which includes Sam. condition and Dif. condition. Sam. means the situation that does not make a distinction between the odd strand and the even strand when charge planning, i.e., for each charge, casting width of the odd strand is the same as that of the even strand. Dif. means another situation that makes a distinction between the odd strand and the even strand when charge planning, i.e., for each charge, casting width of the odd strand may be different from that of the even strand. Man_sam and Man_dif represent the manual method under the Sam. and Dif. conditions, respectively. Alg_sam and Alg_dif represent the proposed algorithm under the Sam. and Dif. conditions, respectively. Note that under the Sam. condition, the number of patterns in the model is $m q$ theoretically, not $m q(q+1) / 2$. In other words, the number of patterns under the Sam. condition is less than the one under the Dif. condition.

The following conclusions can be drawn from the results in Table 2:
(1) The objective values indicate that the proposed algorithm is obviously dominant compared to the manual method under an identical condition, whether it is the Sam. condition or Dif. condition. The number of charges and surplus obtained by the proposed algorithm are remarkably less than the ones obtained by the manual method. The number of scale pairs is also less than the one obtained by the manual method, which is helpful to reduce the width adjustment times when cast planning. Moreover, the
proposed algorithm has better control of steel grades' upgrading costs.
(2) Regardless of the proposed algorithm or the manual method, the values obtained under the Dif. condition are superior to the ones obtained under the Sam. condition. The reason lies in that those orders without intersection in width range can be consolidated together into a charge by distributing in the odd strand and the even strand, which will inevitably reduce the number of charges and the number of scale pairs.
(3) The proposed algorithm can achieve the desired solution for different test data. Especially when the problem size is bigger, the effect will be more obvious. Of course, the computing time will increase accordingly.

Figure 3a-d displays the curves with the fastest convergence speed and the best global optimal solution when four groups of test data are computed by the proposed algorithm. As shown in Fig. 3, the proposed algorithm has a good convergence performance. Meanwhile, the increase in problem size slows down the convergence because its solution set expands.

## 6 Conclusions

1. Charge planning is one of batching problems for steelmaking and continuous casting production, and its optimization will be conducive to subsequent cast planning. This paper studies the charge planning problem in the twin strands continuous casting production.
2. Considering the different widths in the twin strands, the resulting counterweights and the constraints of steelmaking, a multi-objective optimization model is established to minimize the number of charges, the

Table 2 Results of proposed algorithm and manual method

![img-2.jpeg](img-2.jpeg)

Fig. 3 Algorithm convergence curves. a Test1; b Test2; c Test3; d Test4
number of scale pairs, the surplus and the upgrading costs of steel grades.
3. A hybrid optimization algorithm combined with heuristic and mutation-based EDA is proposed to solve the model. Experiments are conducted on several groups of test data under the different conditions. The
results indicate that the proposed algorithm can generate better solutions than the manual method.

Acknowledgements This work was supported by the National Key Research and Development Program of China (No. 2017YFB0304100).
