# Transmission Expansion Planning Based on Hybrid EDA/DE Algorithm Considering Wind Power Penetration 

Wenxia Liu IEEE Member ,He Li, Huiting Xu, Jianhua<br>Zhang IEE Fellow,<br>School of Electrical and Electronic Engineering<br>North China Electric Power University, NCEPU<br>Beijing, China<br>lealihe@hotmail.com


#### Abstract

It poses high requirements for the calculation speed and the precision of the solving method when we consider the large-scale transmission expansion planning (TEP) problems. Therefore, combined with the respective characteristics of EDA (Distribution of Estimation Algorithm) and DE (Differential Evolution algorithm), this paper puts forward a new hybrid EDA/DE algorithm for large-scale TEP problems. Meanwhile, it improves the updating mechanism of probabilistic model of EDA based on the characteristics of the TEP problems. Considering the investments of grid company, the new energy incentive politics and network security constraints, this paper proposes a multi-objective static planning model for the TEP considering wind power penetration, which takes the comprehensive cost, the wind curtailment and the risk value into consideration. Finally a specific example is applied in this paper to verify the applicability and effectiveness of the proposed model and algorithm.


## Index Terms- Differential Evolution, Estimation of Distribution

Algorithm, Transmission Expansion Planning, Wind Power Penetration

## I. INTRODUCTION

Transmission expansion planning (TEP) occupies an important place in the electric power system planning, and its crucial mission is to expand the transmission grid according to the load forecasting and generation development. Then the future grid can meet the power transport demand, ensuring the safety and economy as well as reliability of the target electric power grid. With the rapid development of wind power industry and rising injection for the grid, the fluctuant and intermittent output of wind plants has been a crucial challenge[1]. Recently, researches on TEP model coordinated with wind power penetration are mainly focused on objective functions, constraints and approaches for TEP solving. The economic benefit is still an important objective for TEP model to be concerned with, mainly including the investment cost, operation maintenance cost, social welfare, environmental benefit as well as power outage cost. Ref. [2] adds the cost of

Dehua Zheng, IEEE Member<br>State Wind Power Engineering Technology Research Center<br>Goldwind Beijing Etechwin Electric CO. LTD<br>Beijing, China<br>ZHENGDEHUA01@hotmail.com

load shedding up to the objective function by the help of penalty coefficient, while Ref. [3] adds the cost of dummy generators in a similar way to deal with the violating of power balance. And With the reformation of electric power market, congestion cost is concerned to ensure the economical transport of electric power [4]. Recently, Ref. [5] runs a transmission and generation planning program and Ref. [6] has concerned about the cost of reactive power equipments, running a TEP associated with reactive power planning.

As the reliability of the transmission grid is not ignorable, generally $\mathrm{N}-1$ criterion is applied to test the target transmission grid. As a deterministic criterion, $\mathrm{N}-1$ test mainly pays close attention to big probability events. Since some the above events may cause less loss, planning programs with $100 \%$ satisfactory for $\mathrm{N}-1$ criterion may result in high construction cost. Risk is defined as the product of the probability and consequence, not only the big probability events are concerned, but also the small probability events with grave consequences are reflected. Therefore, risk index is more suitable for TEP [7-9].

The TEP model possesses multi-objective, high dimension, non-convex solutions, complicated constrains and nonlinearity, as it concerns about multi factors. In order to solve the TEP model efficiently and obtain the global optimum, EDA and DE is combined to be a new hybrid algorithm [10-12], inhering the prominent searching ability of DE and the whole information for individuals of EDA.

When the wind power injects at multi locations in a weak power grid with high penetration level, the difference among the locations has a serious impact on the safety, operation cost and risk value of the weak power grid. In addition, the adopt capacity for wind power is effected as well, while the location optimization is rarely referred in existing researches. In order to make up the deficiency, a TEP coordinated with locations for wind power injection optimization is proposed in this paper. And it is a non-linear model with complicate constrains.

This paper is organized as following: the model of TEP associated with the optimal position for wind power penetration is formulated in Section II, the proposed solving approach as bybrid is introduced in Section III, case study and conclusion are given in Section IV and Section V respectively.

## II. THE MODEL OF TEP ASSOCIATED WITH THE OPTIMAL POSITION FOR WINDOWER PENETRATION

## A. Objective functions

The difference of the positions for wind integration has an impact on the grid power flow, especially in a regional power grid. That is because the wind power injection may be either consumed locally or transported to the remote load. The power loses changes and the overload of transmission lines may emerge then. Meanwhile, the construction of the transmission grid and the static stability constraints limit the wind integration as well. The interaction effect between the wind power injection and grid makes it necessary to combine the optimal position planning for wind injection with the transmission expansion planning, taking the investment and operation cost, risk value as well as the integration level of wind power and the transmission capacity constraints, etc into considerations. A multi-objective static model is proposed in this paper, containing the objectives of composite cost, risk value and wind power curtailment, in order to obtain the optimal plan for TEP coordinating with location of wind power injection.

Objective function 1, minimizing the composite cost

$$
\begin{gathered}
\min f_{1}=C_{1}+C_{2} \\
C_{1}=A \sum_{i=1}^{L N} C_{i} * L_{i} * K_{i}, i \in \Omega, i=1,2, \ldots, L N \\
C_{2}=C_{k o t} \sum_{i=1}^{N}\left(\sum_{j=1}^{N_{i}} P_{i j k o n s} * T_{i}\right) \lambda=1,2, \ldots, N \\
P_{i j k o n s}=\frac{P_{i j}^{2}}{\cos \varphi^{2}} R_{j}, i=1, \ldots, N ; j=1, \ldots, N_{L}
\end{gathered}
$$

where $C_{1}$ and $C_{2}$ are investment cost (cost of expansive transmission lines) and operating cost( cost of power loss), respectively. $A$ is annual value coefficient, $L N$ is the number of candidate lines, and $N_{L}$ is the total number of the lines, while $N$ is the number of scenarios. $L_{i}$ and $C_{i}$ are the length and average capital cost ( $\Upsilon 10 \mathrm{k} / \mathrm{km}$ ) of $i^{\text {th }}$ candidate line, respectively. $K_{i}$ is an integer as 1 or 0 , representing whether the $i^{\text {th }}$ candidate line will be constructed or not. Power loss cost is calculated by formula (3), $C_{\text {loss }}$ is average power loss price ( $\Upsilon 10 \mathrm{k} / \mathrm{MWh}$ ), and $P_{i j \text { loss }}$ is the power loss for the $j^{\text {th }}$ candidate line under the $i^{\text {th }}$ scenario as well as $T_{i}$ is the duration time for the $i^{\text {th }}$ scenario within that. $U_{i j}$ is set as 1 , and $\cos \varphi$ is set as 0.95 . Moreover, $P_{i j}$ is power of the $j^{\text {th }}$
transmission corridor under the $i^{\text {th }}$ scenario, and $R_{j}$ is the resistance of the $j^{\text {th }}$ transmission corridor. Based on the parameters above, $P_{i j k o n s}$ is calculated in formula (4).

Objective function 2, minimizing risk value

$$
f_{2}=\text { Risk }=C o * \sum_{i=1}^{N} S_{i} * p_{i} * T_{i}, i=1,2, . ., N
$$

where Risk is risk value of candidate plans, $i$ is the $i^{\text {th }}$ fault state and $N$ is the number of fault states. $S_{i}$ is the amount of load shedding under $i^{\text {th }}$ fault state. $p_{i}$ and $T_{i}$ are the probability and the duration time for the $i^{\text {th }}$ fault state, respectively. Co is the social composite electricity price set as $\Upsilon 1 \mathrm{k} / \mathrm{MWh}$.
Objective function 3, minimizing wind energy curtailment

$$
f_{3}=\min W=\sum_{i=1}^{N} w_{i} * T_{i}, i=1,2, \ldots, N
$$

where $W$ is the amount of wind energy curtailment within a whole year, $i$ is the $i^{\text {th }}$ scenario, $N$ and $T_{i}$ are still the amount of scenarios and the duration time of the $i^{\text {th }}$ scenario respectively. $w_{i}$ it the amount of wind power curtailment in the $i^{\text {th }}$ scenario.

## B. Constraits

Since DC power flow is applied in this paper, there are a few constraints of it as well as the constraint of transmission capacity should be complied with as below.

$$
\left\{\begin{array}{l}
A^{\dagger} P_{i}+G_{i}+R_{i}+w i n_{i}=D_{i} \\
P_{i j}=B_{j} \Delta \theta_{i j} \\
\left|P_{i j}\right| \leq P_{j \max } \\
0 \leq g_{i j} \leq g_{j \max }, 0 \leq r_{i j} \leq d_{i j}
\end{array}\right.
$$

where $\boldsymbol{A}$ is node-branch incident matrix, $\boldsymbol{P}_{i}$ is the power flow vector of branches in the $i^{\text {th }}$ scenario, $\boldsymbol{G}_{i}$ is the output vector of generators in the $i^{\text {th }}$ scenario and $\boldsymbol{D}_{i}$ is the load vector in the $i^{\text {th }}$ scenario, $\boldsymbol{R}_{i}$ is the load shed vector in the $i^{\text {th }}$ scenario, $\boldsymbol{w} \boldsymbol{i} \boldsymbol{n}_{i}$ is the vector of wind power curtailment in the $i^{\text {th }}$ scenario. $B_{j}$ is the equivalent admittance of the $j^{\text {th }}$ branch. If there are multi-lines in the $j^{\text {th }}$ branch, the equivalent admittance is obtained according to the amount of lines). $P_{i j}$ is the transferred power in the $j^{\text {th }}$ branch, $\Delta \theta_{i j}$ is the angle difference between the two sides of the $j^{\text {th }}$ branch in the $i^{\text {th }}$ scenario and $P_{j \text { max }}$ is the maximum transmission capacity of the $j^{\text {th }}$ branch. $g_{i j}$ is the output of $j^{\text {th }}$ generator in the $i^{\text {th }}$ scenario and $g_{j \max }$ is its upper bound. $r_{i j}$ and $d_{i j}$ are load shed and load for the $j^{\text {th }}$ node in the $i^{\text {th }}$ scenario, respectively. And when the failure of the components occurs, constraints in fault states should be obeyed as showed in formula (8).

$$
\left\{\begin{array}{l}
\left(\boldsymbol{A}^{\prime}\right)^{T} \boldsymbol{P}_{i}^{t}+\boldsymbol{G}_{i}^{\prime}+\boldsymbol{S}_{i}+\boldsymbol{w} \boldsymbol{i} \boldsymbol{n}_{i}^{\prime}=\boldsymbol{D}_{i} \\
P_{i j}^{\prime}=B_{j}^{\prime} \Delta \theta_{i j}^{\prime} \\
\left|P_{i j}\right| \leq P_{j \max } \\
0 \leq g_{i}^{\prime} \leq g_{j \max }, 0 \leq s_{i j} \leq d_{i j}
\end{array}\right.
$$

where the parameters above are referred in a certain fault state response to formula (7), $\boldsymbol{S}_{i}$ is the column vector of load shedding in the $i^{\text {th }}$ fault state, and $\mathrm{s}_{i j}$ is the load shedding in node $j$ under the $i^{\text {th }}$ fault state.

## C. Model of opimal location for wind power injection

The wind plant is treated as a generator. The minimum output is 0 and the maximum output is the predicted value of wind power, different from the conventional generator. The essence of optimal location for wind power is distributing the optimal node for the power injection of the equivalent generator in power flow calculation. The decision variables of optimal location is adaptive during the process of the optimal program, the optimal location for wind power injection is obtained afterwards.

## III. IMPROVED HYBRID EDA/DE ALGORITHM

In order to solve the model efficiently, a hybrid EDA/DE algorithm is proposed in this paper with better performance. EDA and DE is collaborated in sequence, the hybrid algorithm starts from EDA for earlier searching to reduce the solution space, end with DE for final solution. The theory of the two involved algorithms are briefly introduced in this section, and the updating mechanism of probabilistic model in EDA is improved according to the characteristic of transmission expansion planning is also introduced in details.

## A. Breif introdution of DE and EDA

DE evolves to obtain a best solution by the method of recording the best individual and best value as well as mutually exchanging information among the population iteratively. The basic calculation flow chart of DE is referred to Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. The calculation flow chart of DE
Furthermore, DE is coded by the real number, while the proposed TEP model is a discrete one. Binary coding is
applied after the crossover to turn the individual code a binary one as showed in formula (9).

$$
x_{i}= \begin{cases}0 & x_{i}^{*} \leq 0.5 \\ 1 & x_{i}^{*}>0.5\end{cases} \quad i=1,2, \ldots, L D
$$

where $x_{i}{ }^{*}$ is the value of the $i^{\text {th }}$ decision variable for a certain individual coded as a real number and $L D$ is the number of decision variables. After the binary coding, it turns to be binary number $x_{i}$ with the value either 1 or 0 , indicating whether the $i^{\text {th }}$ candidate line or injection location is chosen or not.

The core part in EDA is the probabilistic model for the individuals in a certain generation, showed as below and the calculation flow chart of EDA is referred to Figure 2.

$$
\boldsymbol{p}_{i}(x)=\left(p_{i}\left(x_{i}\right), p_{i}\left(x_{i j}\right), \cdots, p_{i}\left(x_{i}\right), \cdots, p_{i}\left(x_{n}\right)\right)
$$

where $n$ is the number of decision variables, $P_{i}\left(x_{i}\right)$ is the probability of obtaining a value of 1 in the $i^{\text {th }}$ component of the population of individuals in the $i^{\text {th }}$ generation. The steps and flow chart of PBIL are showed below.
(1)Obtain an initial probability vector $\boldsymbol{p}_{0}(x)$, and initiate the first generation with $M$ individuals based on $\boldsymbol{p}_{0}(x)$ as $x_{1, \ldots,}^{I}$, $x_{k, \ldots,}^{I} x_{k, i}^{I}$.
(2)Calculate the fitness value of $M$ individuals and rank them by the fitness value, select the $N$ better individuals as $x_{1, M}^{I}, \ldots, x_{k, M}^{I}, \ldots, x_{N, M}^{I}$.
(3)Update the probability vector $\boldsymbol{p}_{1 \cdot i}(x)$ based on the above $N$ individuals using formula (11).
(4) Obtain $M$ individuals based on updated $\boldsymbol{p}_{1 \cdot i}(x)$. When it comes to a terminal condition, run the step (5); otherwise run the step (2).
(5)Stop the process and output the result.

$$
\boldsymbol{p}_{i+1}(x)=(1-\alpha) \boldsymbol{p}_{i}(x)+\alpha \frac{1}{N} \sum_{k=1}^{N} x_{k: M}^{i}
$$

where $\alpha \in(0,1]$ is a coefficient set as the value 0.5 , it decides the proportion of $\boldsymbol{p}_{i}(\mathrm{x})$ taking in $\boldsymbol{p}_{i+1}(x)$.
![img-1.jpeg](img-1.jpeg)

Figure 2. The calculation flow chart of EDA

## B. Improved EDA

As it can be known and defined from formula (11), $P_{l}\left(x_{i}\right)$ is the probability of obtaining a value of 1 in the $i^{\text {th }}$ component of the population of individuals and its additional probability increment $\Delta p_{l}\left(x_{i}\right)=0 . r_{j}(j=1,2, \ldots, V)$ in formula (7) gives the load shed of each node after running economic dispatch, where $V$ is the number of nodes in the objective grid. Then the total load shed energy of each node in all scenarios can be obtained as $e_{f}$, as well as the total load shed energy of the whole grid as $E$. It is assumed that there are $m$ lines connected with node $j$, one of the lines is selected randomly to add the additional probability increment. It refers to formula (12).

$$
\Delta p_{l}\left(x_{i}\right)=\frac{e_{f}}{E}
$$

There are still another situations. If the two sides of the $i^{\text {th }}$ line occur load shed as $e_{l}$ and $e_{k}$ and the $\Delta p_{l}\left(x_{i}\right) \neq 0$, another line connected the node $k$ except the $i^{\text {th }}$ line is selected to add the additional probability increment. When it comes to only one single line between the node $j$ and $k$, the greater additional probability is applied. The additional probability increment vector of the $l^{\text {th }}$ generation is then obtained after running above process, as showed below. Plus, the initial additional probability increment vector is a 0 vector.

$$
\Delta p_{l}(x)=\left(\Delta p_{l}\left(x_{1}\right), \Delta p_{l}\left(x_{2}\right), \cdots, \Delta p_{l}\left(x_{l}\right), \cdots, \Delta p_{l}\left(x_{n}\right)\right)
$$

Then the improved updating mechanism of probabilistic model in EDA is obtained combining formula (11) with (13).

$$
\boldsymbol{p}_{l+1}(x)=(1-\alpha) \boldsymbol{p}_{l}(x)+a \frac{1}{N} \sum_{k=1}^{N} x_{k: k}^{j}+\beta \Delta \boldsymbol{p}_{l}(x)
$$

where $\beta$ is a constant in the interval $(0,1)$, and it is defined as weight factor of additional probability increment, decides the weight of additional probability increment in the offspring probabilistic model. The physical significance of $\beta$ is how much the weight of the mentioned experiential TEP measure affects the offspring plans when the overload in some lines occurs in normal state.

## C. Hybrid EDA/DE Algorithm

There are mainly two strategies for the two above algorithms cooperating. One is that the evolutionary operation is added into the mutation and crossover of DE to obtain offspring; the other one is that EDA and DE solves the model in sequence as the hybrid process runs EDA firstly and skips to DE until sort of conditions. A simple skipping strategy is put up in this paper. Assuming the maximal iteration is IterMax, EDA is run at the first $\omega$ IterMax times. Where $\omega$ is a constant in the interval $(0,1)$, and it is defined as proportion weight coefficient of hybrid algorithm, deciding the proportion of EDA and DE taking in the process of the
proposed hybrid algorithm. The flow chart of the hybrid EDA/DE algorithm is referred to Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. The flow chart of hy bridEDA/DE algorithm

## IV. CASE STUDY

IEEE24 RTS case is applied in this paper for testy. 5 different scenario in the planning year is concerned, the load and wind power output are respectively displayed in TABLE 1. Assuming no new corridors are built and expansion lines are implemented on existing corridors. The average construction price of 110 kV line and 220 kV line are 500 $\Upsilon 10 \mathrm{k} /$ kilometer and $800 \Upsilon 10 \mathrm{k} /$ kilometer, respectively. The annual value coefficient is set as 0.08 , and the price of electricity loss is $0.5 \Upsilon 10 \mathrm{k} / \mathrm{MWh}$, the candidate nodes for power injection of wind plant 1 , wind plant 2 and wind plant 3 are $(3,4),(3,4)$ and $(19,20)$ respectively.

TABLEL DATA OF LOAD AND WINDOWER INPLANNING YEAR

| scenarios | 1 | 2 | 3 | 4 | 5 |
| :-- | :--: | :--: | :--: | :--: | :--: |
| Load(MW) | 2850 | 2500 | 3000 | 3500 | 3100 |
| Wind 1 <br> (Mw) | 200 | 90 | 120 | 60 | 80 |
| Wind 2 <br> (Mw) | 100 | 50 | 70 | 40 | 40 |
| Wind 3 <br> (Mw) | 300 | 120 | 180 | 80 | 160 |
| Duration(h) | 1750 | 1730 | 1760 | 1720 | 1800 |

## A. Analysis of $\beta$ and $\omega$

As it can be drawn from section 3.3, the proportion weight coefficient $\omega$ controls the searching proportion of the combined two algorithms. The value of it has a remarkable impact on the performance of proposed hybrid algorithm and a reasonable one can take fully advantage of the local and global searching ability of DE and EDA respectively. Firstly, $\beta$ is assumed as 0.5 , and risk value is neglected for enhancing analysis efficiency and simplification. The tested model consisting of $f_{l}$ and $f_{k}$, is solved by the proposed hybrid algorithm separately when the value of $\omega$ is selected respectively from the set as $\{0.05,0.1,0.15,0.2\}$. The computation speed and results are displayed in table 2.

TABLE 2. THE RELATIONSHIP BETWEEN THE SEARCHING ABILITY OF HYBRIDEDADE AND THE VALUE OF $\omega$

| $\omega$ | 0.05 | 0.1 | 0.15 | 0.2 | 0.25 |
| :-- | :--: | :--: | :--: | :--: | :--: |
| $f_{l}(\mathrm{Y} 10 \mathrm{k})$ | 14302 | 14273 | 14295 | 14286 | 14283 |
| $f_{k}(\mathrm{MWh})$ | 206950 | 206950 | 206950 | 206950 | 206950 |
| time (s) | 3555 | 2933 | 3054 | 2967 | 3348 |

As it can be seen from Table II through analyzing the results in contrast, the value of $\omega$ that is in the interval [0.1, 0.2 ] leads to better solutions with less computing time. Thus $\omega$ is set as 0.1 in this paper.

In a similar way, $\omega$ is fixed as 0.1 , the same tested model is solved by the proposed hybrid algorithm separately when the value of $\beta$ is selected from the set as $\{0.1,0.2,0.3,0.4$, $0.5\}$ respectively. The computation speed and results are displayed in Table III.

TABLE III. THE RELATIONSHIP BETWWENTHE SEARCHING ABILIT Y OF THE HYBRID EDA/DE ANDTHE VALUE OF $\beta$

| $\beta$ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 |
| :-- | :--: | :--: | :--: | :--: | :--: |
| $f(\sqrt{\mathrm{~V} 10 \mathrm{k}})$ | 14289 | 14254 | 14247 | 14254 | 14257 |
| $f_{0}(\mathrm{MWh})$ | 206950 | 206950 | 206950 | 20695 | 20695 |
| time(s) | 2821 | 2792 | 2943 | 2941 | 2942 |

As it is drawn from Table III through the comparison of the different values of $\beta$ with unlike results and computing time, different values of $\beta$ have less impact on the solutions than different values of $\omega$, resulting in mainly impact on computation speed. In test and contrast, the hybrid algorithm has a better performance in both results and computation speed when the value of $\beta$ in the interval of $[0.1,0.3]$. Thus, $\beta$ is set as 0.2 in this paper.

## B. Planning Schemes and Analysis

IEEE RTS24 case system is modified by adding a wind power plant leaving the location of wind injection to be planned. Table IV shows the solutions by the means of proposed hybrid EDA/DE algorithm.

| TABLE IV. THE OPTIMAL PLANS |  |  |  |
| :--: | :--: | :--: | :--: |
|  | Plan 1 | Plan 2 | Plan 3 |
| Composite <br> cost( $\mathrm{V} 10 \mathrm{k})$ | $1.4696^{*} 10^{4}$ | $1.4686^{*} 10^{4}$ | $1.4844^{*} 10^{4}$ |
| Risk <br> value( $\mathrm{V} 10 \mathrm{k})$ | $5.70541^{*} 10^{4}$ | $5.70544^{*} 10^{4}$ | $5.70540^{*} 10^{4}$ |
| Wind energy <br> curtailment <br> (MWh) | $2.0695^{*} 10^{5}$ | $3.7190^{*} 10^{5}$ | $2.0695^{*} 10^{5}$ |
| TEP routes | $\begin{gathered} 1-2 .7-8 . \\ 14-16.16- \\ 19 \end{gathered}$ | $\begin{gathered} 7-8 .14-16 \\ 16-19 \end{gathered}$ | $\begin{gathered} 2-6 .7-8 . \\ 14-16.16- \\ 19 \end{gathered}$ |
| Location of wind injection | Node 3 | Node 4 | Node 3 |

As we can see from the above Table IV, the wind energy curtailment is relative with the location of its injection and the grid structure. There are slight difference in expansion routes between plan 1 and plan 3 with the same amount of wind energy curtailment and both plan 1 and plan 3 have the same location for wind power injection, differing from plan 2. Comparison among the above 3 plans indicates that node 3 is more suitable for wind power injection considering the
utilization of it and the wind energy curtailment in this paper is mainly effect by the injection location. Although plan 2 gets the minimal composite cost, but the wind energy curtailment is far larger than plan 1 and plan 3. In addition, plan 1 is more economical than plan 3. According to all the above truth, plan 1 is selected as the optimal planning program. The expansion routes and the optimal location of wind power injection are displayed in Figure 4. Where the solid lines are existing lines and imaginary lines are newly expanded ones. The risk value of this optimal program is $5.7054^{*} 10^{-3}$ yuan, which is extremely small. It verifies the selected program can safely deal with the $\mathrm{N}-1$ faults and certain $\mathrm{N}-2$ faults.
![img-3.jpeg](img-3.jpeg)

Figure 4 The optimal plan
C. The Comparison Among the Hybrid EDA/DE Algorithm and DE, EDA
DE and EDA are applied with the maximal iteration 200 in solving the proposed model to verify the feasibility and efficiency of the proposed hybrid EDA/DE algorithm. The optimal programs obtained by the two algorithms are displayed in Table V , respectively.

TABLE V. THE OPTMAL PLAN BY THE METHOD OF DE AND EDA

|  | DE(plan 4) | EDA(plan 5) |
| :--: | :--: | :--: |
| Composite <br> cost( $\mathrm{V} 10 \mathrm{k})$ | $1.4829^{*} 10^{4}$ | $1.5823^{*} 10^{4}$ |
| Risk Value( $\mathrm{V} 10 \mathrm{k})$ | $5.70540^{*} 10^{4}$ | $5.70540^{*} 10^{4}$ |
| Wind energy <br> curtailment <br> (MWh) | $2.0695^{*} 10^{5}$ | $2.0695^{*} 10^{5}$ |
| Expansion routes | $\begin{aligned} & 1-5.7-8.14- \\ & 16.16-19 \end{aligned}$ | $\begin{aligned} & 1-2 .1-3 .2-4 .2-6 .3-9 .4- \\ & 9.5-10 .7-8 .11-13 .16-19 \end{aligned}$ |
| Location of wind injection | Node 3 | Node 3 |

Compared with the optimal program in Table IV, the two best programs in Table V are remarkably inferior obtained by single EDA and DE respectively. The comparison

indicates that the proposed hybrid EDA/DE algorithm has better performance in solving the proposed model than the singe EDA and DE. It avoids the local convergence that may be caused by DE, and improve the unsatisfactory solutions obtained by EDA.

## V. CONCLUSION

The objective functions as composite cost, risk value and wind energy curtailment makes it possible to obtain an economic and reliable program, especially being helpful with the utilization of wind power. A hybrid EDA/DE algorithm is proposed. In order to apply the TEP issue, the updating mechanism of probabilistic model in EDA is improved according to the experience of TEP. Tests are run to analyze and select the parameters in hybrid algorithm to ensure a good convergence, and the results verify the validity and practicability of the proposed model and algorithm. Comparison is made to verify the better performance of hybrid algorithm than EDA and DE. However, the obtained program based on the proposed static TEP model under deterministic condition is not properly adaptive for the uncertain factors in the future.

## VI. REFERENCE

[1] G. Sansavini, R. Piccinelli, L. R. Golea, et al, "A stochastic framework for uncertainty analysis in electric power transmission systems with wind generation," Renewable Energy, Vol 64, pp. 71-84, 2014.
[2] H. Yu, C. Y. Chuang, K. P. Wong, et al, "A chance constrained transmission network expansion planning method with consideration of load and wind farm uncertainties," IEEE Transactions on Power Systems, Vol 24, pp. 1568-1576, 2009.
[3] H. Mori, H. Kakuta, "Multi-objective transmission network expansion planning in consideration of wind farms," in $2^{\text {nd }}$ IEEE PES international conference and Exhibition on digital object identifier, pp. 1-7.
[4] G. B. Shrestha, P. A. J. Fonseca, "Congestion-driven transmission expansion in competitive power market," IEEE Transactions on Power Systems, Vol 19, pp. 1658-1665, 2004.
[5] Y. Gu, J. D. Mccalley, M. NI, "Coordinating large-scale wind integration and transmission planning," IEEE Transactions on Sustainable Energy, Vol 3, pp. 652-659, 2012.
[6] R. Hemmati, R. Hooshmand, A. Khodabakhshian, "Market based transmission expansion and reactive power planning with consideration of wind and load uncertainties," Renewable and Sustainable Energy Reviews, Vol 29, pp. 1-10, 2014.
[7] Wenyuan Li, Jiping Lu. "Risk evaluation of combinative transmission network and substation configurations and its application in substation planning," IEEE Transactions on Power Systems, Vol 20, No. 2, pp. 1144-1150, 2005.
[8] D. Delgado, J. Claro, "Transmission network expansion planning under demand uncertainty and risk aversion," Electrical Power and Energy Systems, Vol 44, pp. 696-702, 2013.
[9] R. Hooshmand, R. Hemmati, M. Parastegari, "Combination of AC Transmission Expansion Planning and Reactive power in the restructured power system," Energy Conversion and Management, Vol. 55, pp. 26-35, 2012.
[10] W. Yu, L. Bin, T.Weise, "Estimation of distribution and differential evolution cooperation for large scale economic load dispatch optimization of power sy stems," Information Sciences, Vol.180, pp. 2405-2420, 2010.
[11] S. Jiangyong, Z. Qingfu, E. P. K. Tsang, "DE/EDA A new evolutionary algorithm for global optimization," Information Sciences, Vol. 169, pp. 249-262, 2005.
[12] S. Xiangman, T. Lisin, "A novel hybrid differential evolutionestimation of distribution algorithm for dynamic optimization proble," IEEE Congress on Evolutionary Computation , Cancun, Mexico: 2013.