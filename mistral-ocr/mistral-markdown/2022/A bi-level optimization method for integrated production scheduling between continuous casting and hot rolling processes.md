# A bi-level optimization method for integrated production scheduling between continuous casting and hot rolling processes* 

Wei Tang, Lingling Cao, Yaomin Wen, and Sheng-Long Jiang, Member, IEEE


#### Abstract

To improve production efficiency and reduce energy costs in steel manufacturing, this paper investigates the integrated production scheduling problem between continuous casting and hot rolling (IPSP-CCHR) and formulates it as a bi-level optimization model. The upper-level one is the production planning match problem (PPMP) between continuous casting and hot rolling processes, which aims to maximize productivity. The lower-level one is the reheating furnace scheduling problem (RFSP), which aims to minimize the total residence time. Next, we propose a stratified sampling bi-level optimization (SSBLO) algorithm to solve the IPSP-CCHR, which applies Latin Hypercube sampling (LHS) for solving the upper-level problem and estimation of distribution algorithm (EDA) for solving the lower-level problem. In the experiments, computational results via well-synthetic data show the bi-level optimization model and the proposed algorithm is effective and is expected to apply in realistic industrial cases.


## I. INTRODUCTION

Continuous casting-hot rolling (CC-HR) section is the key component in a steel manufacturing system, which includes CC, HR, reheating stage (as shown in Figure 1). In the CC stage, high-temperature molten steel is casted into slabs after steelmaking, the basic production unit is a cast (molten steel continuous casted in a tundish). Then the output slabs from CC stage are transported to reheating furnaces, soaking pit, or slab yard, which results in three linkage modes between CC and HR respectively, namely direct hot charging rolling (DHCR), hot charge rolling (HCR), and cold charging rolling (CCR). No matter which linkage mode is selected, each slab needs to be heated to the rolling temperature in the reheating furnace before HR. In the HR stage, the slabs are rolled into coils. The basic production unit in the HR stage is a rolling unit (slabs continuously rolled between replacement of two adjacent work rollers).

To select appropriate linkage modes between CC and HR can improve production efficiency. The most ideal scheme is to adopt DHCR linkage mode for all slabs, but it may exceed the heating capacity of the reheating furnace and destroy the matching relationship. If all slabs adopt CCR linkage mode, it will increase energy cost because the CCR linkage mode slab need more heating time. The integrated production scheduling mainly includes two parts: one is the optimal CC-HR production planning matching based the selection of linkage mode, and the other one is the optimal reheating furnace

[^0]scheduling. Therefore, the integrated production scheduling of CC and HR is of great significance to the energy saving and efficiency increase of production.

In past decades, most practitioners studied scheduling problems across CC to HR stages in a disintegrative way because of their significant difference in production mode. In the CC stage, most studies focused on CC scheduling problems related with the steelmaking process, which were modelled via mixed-integer linear programming (MILP) problem and solved it by heuristic methods or evolutionary algorithms[1-3]. In HR stage, most studies mainly focus on seeking optimal sequence of slabs and minimizing the technological change of slabs. The HR scheduling problems were commonly modelled via traveling salesman problem (TSP), vehicle routing problem (VRP) and their variants, and were commonly solved by heuristic methods[4]. In reheating furnace stage, related works were devoting to solve the machine scheduling problem minimizing the residence time of slabs in reheating furnaces[5-7].

As the integrated production scheduling of CC-HR becoming more and more important, some scholars moved attentions to the IPSP-CCHR. Zhu et al. [8] established a integrated scheduling model including steelmaking, CC, and HR and proposed Lagrangian relaxation-based algorithm to solve it. Mattik et al. [9] addressed the joint scheduling of continuous caster and hot strip mill processes by formulating a MILP model based on the block planning principle. Pan et al. [10] proposed a novel modified extremal optimization algorithm combining an exact mathematical programming on the CC stage and a heuristic algorithm on the HR stage. Tan et al. [11] studied the scheduling problem containing CC, reheating, and HR processes by modeling it as a combination of a CC-HR scheduling subproblem and an reheating scheduling subproblem, then developed a hybrid MIP/CP algorithm to solve each subproblem based on Benders decomposition strategy. Wang et al. [12] proposed a two-stage optimization algorithm combined a genetic algorithm and a linear programming to solve the integrated scheduling problem of steelmaking, CC, and HR aiming at minimizing the energy consumption.

Although the IPSP-CCHR were investigated as mentioned above, existing studies still have an obvious limitation. They always assumed that the capacity of reheating furnaces is infinite and ignored its impacts on feasibility of scheduling in other stages. This assumption is Utopian and may cause most theories to be ineffective. To fill this research gap, we study the IPSP-CCHR which considers reheating stage as the intermediate process, and consider it as a bi-level optimization problem involving a PPMP sub-problem and an RFSP sub-problem. In the upper level, the PPMP sub-problem is to coordinate the production planning by using flexible linkage


[^0]:    *Research supported by the National Natural Science Foundation of China (No. 61873042).
    W. Tang, L. Cao , Y Wen, and S-L Jiang are with the School of materials science and engineering, Chongqing University, Chongqing, China (wei.tang@cqu.edu.cn; 20172943@cqu.edu.cn; wymwh@cqu.edu.cn, jiang_shli@cqu.edu.cn).

modes. In the lower level, the RFSP sub-problem is to determine the processing time and the processing machine in the reheating stage under the production planning given by the
![img-0.jpeg](img-0.jpeg)

Figure 1. Flowsheet of steel manufacturing
upper-level model. Then, we propose a stratified sampling bi-level optimization (SSBLO) algorithm to solve it.
![img-1.jpeg](img-1.jpeg)

Figure 1. Flowsheet of steel manufacturing

# II. Problem Formulation 

In this section, we build mathematical models for the two sub-problems respectively and then combine them into a bi-level optimization model.

## A. PPMP Model

Indices:
$m \quad$ index of continuous casting machines (CCMs), and $M$ is the number of CCMs.
$b, d \quad$ index of casts, and $n^{C}$ is the number of casts.
$i, j \quad$ index of slabs, and $n$ is the number of slabs.
$p, q \quad$ index of rolling units, and $n^{R}$ is the number of rolling units.
Parameters:
$a_{i, b} \quad$ position of slab $i$ in cast $b$.
$a_{i, p} \quad$ position of slab $i$ in rolling unit $p$.
$t^{C} \quad$ processing time of each slab in CC stage.
$t^{R} \quad$ processing time of each slab in HR stage.
$T_{b}^{C} \quad$ processing time of cast $b$ in CC stage.
$T_{p}^{R} \quad$ processing time of rolling $p$ in HR stage.
$U^{C} \quad$ setup time between two successive casts in a machine.
$U^{R} \quad$ setup time between two successive rolling units.
$k \quad$ linkage mode, 1 for DHCR, 2 for HCR, 3 for CCR.
$T_{b}^{\min } \quad$ minimum time interval for slabs in a process assigned with linkage mode $k$.
$T_{b}^{\max } \quad$ maximum time interval for slabs in a process assigned with linkage mode $k$.
$\lambda_{1} \quad$ objective weight coefficient, determined according to manual experience.
$\operatorname{big} M$ a large number.
Decision Variables:
$\alpha_{p} \quad$ weight coefficient of linkage mode for rolling unit $p$.
$X_{b, m} \quad$ if cast $b$ is arranged on $\mathrm{CCM} m, X_{b, m}=1$, otherwise $X_{b, m}=0$.
$Y_{b, d, m}$ if cast $b$ and cast $d$ are processed by CCM $m$, and $b$ directly precedes $d$, then $Y_{b, d, m}=1$, otherwise $Y_{b, d, m}=0$.
$Y_{p, q} \quad$ if rolling unit $p$ directly precedes $q, Y_{p, q}=1$, otherwise $Y_{p, q}=0$.
$Z_{i, k} \quad$ if linkage mode $k$ is assigned with slab $i, Z_{i, k}=1$, otherwise $Z_{i, k}=0$.
$s_{b}^{C} \quad$ starting time of cast $b$ at CC stage.
$s_{b, i}^{C} \quad$ starting time of slab $i$ in cast $b$ at CC stage.
$s_{p}^{R} \quad$ starting time of rolling unit $p$ at HR stage.
$s_{p, i}^{R} \quad$ starting time of slab $i$ in rolling unit $p$ at HR stage.
$v_{i} \quad$ interval between CC-HR of slab $i$.
The mathematical model is formulated as follows.

$$
\min F=\left(\lambda_{1} \sum_{i=1}^{n} k \cdot z_{i, k}+\sum_{i=1}^{n}\left(s_{p, i}^{R}-s_{b, i}^{C}-t^{C}\right)\right)
$$

Subject to

$$
\begin{gathered}
\sum_{m=1}^{M} X_{b, m}=1 \\
\sum_{d=1, j=n}^{n^{C}-1} Y_{b, d, m}=\sum_{d=0, j=n}^{n^{C}-1} Y_{b, d, m}=X_{b, m} \\
s_{b}^{C}+T_{b}^{C}+U^{C}-b i g M\left(3-X_{b, m}-X_{d, m}-Y_{b, d, m}\right) \leq s_{d}^{C} \\
s_{b, i}^{C}=s_{b}^{C}+\left(a_{b, i}^{C}-1\right) t^{C} \\
\sum_{p=1, j=q}^{n^{C}-1} Y_{p, q}=\sum_{p=0, j=q}^{n^{C}-1} Y_{q, p}=1 \\
s_{p}^{R}+T_{p}^{R}+U^{R}-b i g M\left(1-Y_{p, q}\right) \leq s_{q}^{R} \\
s_{p, i}^{R}=s_{p}^{R}+\left(a_{p, i}^{R}-1\right) t^{R} \\
\sum_{k=1}^{1} Z_{i, k}=1 \\
v_{i}=s_{p, i}^{R}-s_{b, i}^{C}-t^{C} \\
\sum_{k=2}^{3}\left(1+\alpha_{p}\right) T_{k}^{\min } Z_{i, k} \leq v_{i} \leq \sum_{k=2}^{3}\left(1+\alpha_{p}\right) T_{k}^{\max } Z_{i, k}
\end{gathered}
$$

The objective function (1) minimizes CCR mode and the interval of all slabs between CC and HR. Constraint (2) ensures each cast is allocated to one CCM. Constraint (3) ensures there is only one predecessor and only one successor for casts processed on the same CCM. Constraint (4) ensures enough setup time between two adjacent casts on one CCM. Constraint (5) shows the CC is continuously processed and the start of each slab can be calculated. Constraint (6) ensures there is only one predecessor and only one successor for rolling units. Constraint (7) ensures enough setup time between two consecutive rolling units. Constraint (8) shows the rolling process is continuous and then the start rolling time of each slab can be calculated. Constraint (9) ensures each slab is processed by one linkage mode. Constraint (10) shows the interval of the slab between the CC stage and HR stage can be calculated. Constraint (11) ensures the interval between CC and HR must be in the specified linkage mode range.

It is worth noting that we proposed a flexible coefficient $\alpha_{p}$ to adjust the linkage mode interval of each rolling unit, which can reduce the CCR mode slabs, reduce energy consumption and improve production efficiency.

## B. RFSP Model

Indices:
$g \quad$ index of reheating furnaces, and $G$ is the number of reheating furnaces.
Parameters:
$h_{i}^{\min } \quad$ minimum residence time of slab $i$.
$h_{i}^{\max } \quad$ maximum residence time of slab $i$.
$a_{i, b} \quad$ position of slab $i$ in cast $b$.
$U^{H} \quad$ setup time between two successive slabs in or out reheating furnace.
$w \quad$ maximum wait time for roll after slab out from reheating furnace.
$s_{b, i}^{C} \quad$ starting time of slab $i$ in cast $b$ at CC stage.
$s_{p, i}^{R} \quad$ starting time of slab $i$ in rolling unit $p$ at HR stage.
$L_{g} \quad$ capacity of reheating furnace $g$.
$\operatorname{big} M$ a large number.
Decision Variables:
$b_{i} \quad$ feed-in time of slab $i$ in reheating stage.
$e_{i} \quad$ drop-out time of slab $i$ in reheating stage.
$x_{i, g} \quad$ if slab $i$ heating in reheating furnace $g$, then $x_{i, g}=1$, otherwise $x_{i, g}=0$.
$y_{i, j, g}$ if slab $i$ and slab $j$ are processed by reheating furnace $g$, and $i$ directly precedes $j$, then $y_{i, j, g}=1$, otherwise $y_{i, j, g}=0$.
$z_{i, j, g}$ if slab $j$ is in the $L_{g}-t h$ position after slab $i$ in the reheating furnace $g$, then $z_{i, j, g}=1$, otherwise $z_{i, j, g}=0$.
The mathematical model is formulated as follows.

$$
\min f=\sum_{i=1}^{n}\left(e_{i}-b_{i}\right)
$$

Subject to

$$
\begin{gathered}
\sum_{g=1}^{G} x_{i, g}=1 \\
\sum_{i=i, j=j}^{n} y_{i, j, g}=\sum_{a=b, i=j}^{n} y_{i, j, g}=x_{i, g} \\
b_{i}+U^{H}-\operatorname{big} M\left(3-x_{i, g}-x_{j, g}-y_{i, j, g}\right)<b_{j} \\
e_{i}+U^{H}-\operatorname{big} M\left(3-x_{i, g}-x_{j, g}-y_{i, j, g}\right)<e_{j} \\
b_{i}+h_{i}^{\min }<e_{i}<b_{i}+h_{i}^{\max } \\
b_{i}>s_{b, i}^{E}+t^{C} \\
s_{p, i}^{R}-e_{i} \leq w \\
\left(b_{i}-e_{j}\right)+\operatorname{big} M\left(3-x_{i, g}-x_{j, g}-z_{i, j, g}\right) \geq 0
\end{gathered}
$$

The objective function (12) minimizes the residence time of all slabs. Constraint (13) ensures each slab is heated in one reheating furnace. Constraint (14) ensures there is only one predecessor and only one successor for slabs processed on the same reheating furnace. Constraint (15) and (16) ensure the first in first out principle of reheating furnace. Constraint (17) indicates the residence time in a reheating furnace must in the specified range. Constraint (18) ensures the feed-in time of the reheating stage is after the CC stage. Constraint (19) shows that the slab should be rolled after drop-out from reheating furnace, and the interval should be less than a certain value. Constraint (20) guarantees the number of slabs in a reheating furnace should not exceed its capacity.

## C. Bi-level Model

![img-2.jpeg](img-2.jpeg)

Figure 2. Bi-level model of CC-HR integrated production scheduling
In the IPSP-CCHR, the residence time of slab in RFSP is determined by the linkage mode in the PPMP model. The interval between the reheating stage and the HR stage in RFSP should be less than a specific value, causing the slab due to roll immediately after drop-out from reheating furnace, so the

drop-out time in RFSP is also determined by the PPMP. Therefore, the IPSP-CCHR can be formulated as a bi-level optimization problem, in which the PPMP is the upper-level optimization problem and the RFSP is the lower-level problem (as shown in Figure 2).

For the relationship of the upper-level model and the lower-level model, $s_{b, i}^{T}$ and $s_{p, i}^{R}$ are not only the parameters of the lower model, but also the decision variables of the upper model. So the solution time window of the RFSP is given by the PPMP, but the solution time window given by the upper-level may be infeasible to solve the lower-level model. Considering this relationship, we integrate two models to establish a bi-level model by introducing a penalty parameter $d_{i}$, which is the delay time of slab $i$ in HR stage. When the upper-level model pursues production efficiency, it should ensure the feasibility of solving the lower-level model. Then $d_{i}$ becomes the Nash equilibrium point between the upper-level and the lower-level. The bi-level model is formulated as follows.

$$
\operatorname{Min}\left(F+\sum_{i=1}^{N} \lambda_{i} d_{i}\right)
$$

Subject to (2) $\sim(11)$ and

$$
\left\{\begin{array}{l}
d_{i} \in \arg \min f+\sum_{i=1}^{N} \lambda_{i} d_{i} \\
\text { subject to }(13) \sim(20) \\
d_{i} \geq e_{i}-s_{p, i}^{R}
\end{array}\right.
$$

Where $\lambda_{i}$, is the weight coefficient of $d_{i}$, usually set to a large value to avoid delay in the HR stage.

As mentioned above, this problem is a bi-level optimization problem, in which a PPMP and an RFSP are dealt with in an integrated manner. The RFSP is at the lower
![img-3.jpeg](img-3.jpeg)

Figure 3. The flowchart of the SSBLO algorithm

## B. Upper-level Optimization Algorithm

LHS[13] method belongs to the stratified sampling, which could reflect the integral distribution effectively. Assuming that we want to take $m$ samples from an n-dimensional vector space. Here are the steps of taking $m$ samples in the upper-level problem:

Step 1: Divide $m$ dimension of $n^{R}$ into m intervals from 0 to 1 that do not overlap each other so that each interval has the same probability.

Step 2: Pick a random point in each interval in each dimension.

Step 3: Then the points selected in step 2 are randomly selected from each dimension and formed into vector $\alpha$, then the vectors are the samples.

After the flexible coefficients are determined by LHS, the upper-level model is supposed to be a MILP and can be solved by mathematical solvers, like GUROBI, CPLEX, etc.

## C. Lower-level Optimization Algorithm

After the upper-level model parameters are determined, the lower-level optimization process is an evolutionary optimization process which uses EDA, the specific flow of the algorithm can be found in paper[14].

In the algorithm, we encode the furnace assignment and sequence of slabs. The chromosome length is the slab number $N$, the value of gene is furnace number assignment, and the value of the $i-t h$ gene is $g$, which means slab $i$ is assigned to reheating furnace $g$. After encoding, we designed a heuristic method to decode and determine the feed-in time and drop-out time of slabs:
(1) If the slab is the first slab to feed-in a reheating furnace, $b_{i}=s_{b, i}^{C}+t^{C}, e_{i}=b_{i}+h_{i}^{\min } ;$
(2) If the slab feed-in a furnace and does not exceed its capacity, $b_{i}=s_{b, i}^{C}+t^{C}, e_{i}=\max \left\{b_{i}+h_{i}^{\min }, e_{i-1}\right\}$.
(3) If the slab feed-in a furnace and exceed its capacity, $b_{i}=e_{i-1_{i}}, e_{i}=\max \left\{b_{i}+h_{i}^{\min }, e_{i-1}\right\}$.

When all time variables are determined, we push back all times to ensure that the drop-out times and start times of hot rolling are less than the specified range.

## IV. COMPUTATIONAL EXPERIMENTS

In this section, we conduct a number of experiments to evaluate the bi-level optimization model and the proposed SSBLO algorithm. The algorithms were coded in Python 3.9 and Gurobi 9.1.0 was used for solving the MILP in the model. The programs were conducted via a 64-bit personal computer with a 1.00 GHz Core(TM) i5-1035G1 CPU and 16 GB RAM.

## A. Instance Generation

We randomly generated test instances, in which the input data is collected from a large steel company located in China. The following are the parameter settings used in the experiments. The number of CC machines $M=2$, and the number of reheating furnaces $G=3$, the setup time for CC machines $S^{C}=20 \mathrm{~min}$, and for HR machine $S^{R}=10 \mathrm{~min}$, the processing time for one slab in CC stage $t^{C}=6 \mathrm{~min}$, and in HR stage $t^{R}=4 \mathrm{~min}$. The capacity of each reheating furnace $L_{g}=10$, the interval for each linkage mode are as follows: $\left[T_{1}^{\min }, T_{1}^{\max }\right]=[40,80],\left[T_{2}^{\min }, T_{2}^{\max }\right]=[81,160],\left[T_{3}^{\min }, T_{3}^{\max }\right]$ $=[161,600]$ with minutes being the time unit. As for the range of standard reheating time, DHCR, HCR and CCR mode are respectively $[30,60],[70,120]$ and $[140,180]$. The weight coefficients $\lambda_{i}=99, \lambda_{2}=100$. The maximum interval between the drop-out time in reheating stage and the start time in HR stage $w=5$.

The proposed approach was implemented based on the following settings: the sample size from LHS is 15 . And for EDA, the population size is 50 , the maximum iteration number is 100 , the learning rate $\theta=0.2$.

## B. Experimental Results

The computational results of the test instances are given in Table I. It reports the best flexible coefficient, the linkage mode, total interval between CC and HR stage, and the total residence time in reheating furnaces, and we have made a detailed analysis of instance 03 by randomly, which shows the Latin Hypercube samples, and the results in both upper-level model and lower-level model in Table II.

Based on the results shown in the tables and figures, we observe the following:
(1) In all instances, the proportions of the DHCR and the HCR mode slabs exceeded $80 \%$, and the instance 01 and 07 even reached $100 \%$. The mean interval between CC-HR of each slab is 159 minutes, and the mean residence time of each slab is 65 minute.
(2) From the result of instance 3 , we can see that the whole production planning works well and there is no delay in the HR stage.
(3) As the results shown in table II, it can be verified that the upper-level problem and lower-level problem are in a co-operative relationship. The objective values of the upper-level and lower-level models are linearly positively correlated. It is worth noting that the sample 8 has the optimal solution both in upper-level model and lower-level model.

TABLE I. COMPutational Results of Proposed Algorithm

| instances | $\boldsymbol{n}^{C}$ | $\boldsymbol{n}^{R}$ | $\boldsymbol{n}$ | $\boldsymbol{\alpha}$ | $\begin{gathered} \text { DHCR } \\ \text { slabs } \end{gathered}$ | HCR <br> slabs | CCR <br> slabs | Interval between CC-HR | residence time | $\mathbf{T} /(\mathbf{s})$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\# 01$ | 4 | 3 | 88 | $[0.97,0.90,0.88]$ | 25 | 63 | 0 | 9232 | 4715 | 131 |
| $\# 02$ | 4 | 3 | 90 | $[0.50,0.43,0.37]$ | 30 | 45 | 15 | 10940 | 4657 | 167 |
| $\# 03$ | 4 | 3 | 97 | $[0.70,0.50,0.77]$ | 34 | 58 | 5 | 10235 | 4798 | 281 |
| $\# 04$ | 5 | 3 | 108 | $[0.90,0.70,0.76]$ | 38 | 52 | 18 | 11249 | 5365 | 288 |
| $\# 05$ | 5 | 4 | 115 | $[0.77,0.97,0.70,0.90]$ | 50 | 50 | 15 | 11976 | 6572 | 227 |
| $\# 06$ | 5 | 3 | 120 | $[0.70,0.50,0.77]$ | 50 | 55 | 15 | 12854 | 5700 | 234 |
| $\# 07$ | 5 | 4 | 130 | $[0.57,0.50,0.50,0.43]$ | 60 | 70 | 0 | 13894 | 6016 | 271 |
| $\# 08$ | 6 | 4 | 134 | $[0.70,0.70,0.77,0.57]$ | 70 | 54 | 10 | 13921 | 6083 | 315 |
| $\# 09$ | 5 | 4 | 140 | $[0.97,0.70,0.57,0.03]$ | 50 | 74 | 26 | 14746 | 6795 | 300 |
| $\# 10$ | 6 | 4 | 147 | $[0.57,0.37,0.83,0.10]$ | 50 | 77 | 20 | 14080 | 8321 | 324 |

TABLE II. COMPUTATIONAL RESULTS OF INSTANCE 03

| No. | $\boldsymbol{\alpha}$ | upper-level <br> value | lower-level <br> value |
| :--: | :-- | :-- | :-- |
| 1 | $[0.35,0.63,0.73]$ | 46323 | 26771 |
| 2 | $[0.43,0.19,0.65]$ | 38805 | 12099 |
| 3 | $[0.68,0.45,0.43]$ | 64212 | 24656 |
| 4 | $[0.48,0.57,0.91]$ | 54990 | 38802 |
| 5 | $[0.73,0.90,0.26]$ | 32338 | 14898 |
| $\mathbf{6}$ | $[0.78,0.15,0.47]$ | 41297 | 24227 |
| 7 | $[0.54,0.35,0.98]$ | 28965 | 6358 |
| $\mathbf{8}$ | $[0.70,0.50,0.77]$ | $\mathbf{2 6 5 7 0}$ | $\mathbf{4 7 9 8}$ |
| 9 | $[0.94,0.46,0.83]$ | 30327 | 8698 |
| 10 | $[0.24,0.51,0.08]$ | 36771 | 9611 |
| 11 | $[0.88,0.96,0.15]$ | 50024 | 35661 |
| 12 | $[0.27,0.70,0.31]$ | 32968 | 5873 |
| 13 | $[0.83,0.26,0.02]$ | 44260 | 19942 |
| 14 | $[0.07,0.10,0.86]$ | 29801 | 10197 |
| 15 | $[0.97,0.82,0.21]$ | 37882 | 6812 |

## C. Comparative Experiments

In order to verify the superiority of the proposed bi-level optimization method, we conducted research on the IPSP-CCHR by using sequential decision-making method, that is we first studied the PPMP, and then the RFSP. Then we compare the experimental results of the two methods. Due to the small sample size, we use the Mann Whitney U test in the nonparametric test and draw a box diagram (as shown in Figure 4).
![img-4.jpeg](img-4.jpeg)

Figure 4. Comparison between sequential decision-making method and bi-level method

The calculation results show that when $a<0.12$, the interval of bi-level optimization is significantly less than that of sequential decision-making method. When $\alpha<0.03$, the residence time of the bi-level optimization is significantly less than that of the sequential decision-making method.

Through the Mann Whitney U test and Figure 4, we find that the results of the bi-level optimization method are better than those of the sequential decision-making method, regardless of PPMP or RFSP. Therefore, the bi-level optimization method can obtain a better scheduling solution than the sequential decision-making method.

## V. CONCLUSION

In this paper, we study the IPSP-CCHR by developing a bi-level optimization model and propose an SSBLO algorithm to solve it. In the proposed model, we apply a flexible coefficient to parameterize the linkage interval
between CC and HR and select the optimal linkage parameters for each rolling unit. To evaluate the efficacy of the proposed approach, we conduct experimental comparisons based on randomly synthetic instances. The experimental results demonstrated that the proposed bi-level optimization model with the SSBLO algorithm was capable of tackling the IPSP-CCHR effectively.

In order to improve the solving efficiency, we adopted the Latin hypercube sampling and the heuristic methods, but the results may not reach the global optimization. A direct extension for future research should aim to find other methods to obtain the global optimal solution and ensure the solving efficiency. Besides, we will apply the proposed model and algorithm in practice.

## REFERENCES

[1] K. Mao, Q.-k. Pan, X. Pang, and T. Chai, "A novel Lagrangian relaxation approach for a hybrid flowshop scheduling problem in the steelmaking-continuous casting process," European Journal of Operational Research, vol. 236, no. 1, pp. 51-60, 2014.
[2] J. Long, Z. Zheng, and X. Gao, "Dynamic scheduling in steelmaking-continuous casting production for continuous caster breakdown," International Journal of Production Research, vol. 55, no. 11, pp. 3197-3216, 2016.
[3] L. Tang, Y. Zhao, and J. Liu, "An Improved Differential Evolution Algorithm for Practical Dynamic Scheduling in Steelmaking-Continuous Casting Production," IEEE Transactions on Evolutionary Computation, vol. 18, no. 2, pp. 209-225, 2014.
[4] A. Özgür, Y. Uygun, and M.-T. Hütt, "A review of planning and scheduling methods for hot rolling mills in steel production," Computers \& Industrial Engineering, 2020.
[5] X. Wang and L. Tang, "Scheduling a single machine with multiple job processing ability to minimize makespan," Journal of the Operational Research Society, vol. 62, no. 8, pp. 1555-1565, Aug 2011.
[6] R. Hu, S. X. Yang, X. C. Luo, and leee, "Ant Colony Optimization for Scheduling Walking Beam Reheating Furnaces," in 2014 11th World Congress on Intelligent Control and Automation, 2014, pp. 621-626.
[7] L. X. Tang, H. Z. Ren, and Y. Yang, "Reheat furnace scheduling with energy consideration," International Journal of Production Research, vol. 53, no. 6, pp. 1642-1660, Mar 2015.
[8] B. L. Zhu and S. F. Ji, "Steelmaking-Hot Rolling Scheduling Model and Method for Integrated Management in Iron and Steel Enterprises," Advanced Materials Research, vol. 860-863, pp. 3094-3099, 2013.
[9] I. Mattik, P. Amorim, and H.-O. Günther, "Hierarchical scheduling of continuous casters and hot strip mills in the steel industry: a block planning application," International Journal of Production Research, vol. 52, no. 9, pp. 2576-2591, 2014.
[10] Z. Pan, T. Wang, X. Zhou, and P. Chen, "Application of extremal optimization approach to the integrated scheduling problem of continuous casting and hot rolling process," in Control \& Decision Conference, 2017.
[11] Y. Y. Tan, M. C. Zhou, Y. Y. Wang, X. W. Guo, and L. Qi, "A Hybrid MIP-CP Approach to Multistage Scheduling Problem in Continuous Casting and Hot-Rolling Processes," IEEE Transactions on Automation Science and Engineering, vol. 16, no. 4, pp. 1860-1869, Oct 2019.
[12] S. Wang, Y. Shi, and S. Liu, "Integrated Scheduling for Steelmaking Continuous Casting- Hot Rolling Processes considering Hot Chain Logistics," Mathematical Problems in Engineering, vol. 2020, pp. 1-10, 2020.
[13] J. Yin, W. Lu, X. Xin, and L. Zhang, "Application of Monte Carlo sampling and Latin Hypercube sampling methods in pumping schedule design during establishing surrogate model," 2011 International Symposium on Water Resource and Environmental Protection, 2011, vol. 1, pp. 212-215.
[14] L. Tang, X. Song, J. Liu, and C. Liu, "An Estimation of Distribution Algorithm with Filtering and Learning," IEEE Transactions on Automation Science and Engineering, vol. 18, no. 3, pp. 1478-1491, 2021.