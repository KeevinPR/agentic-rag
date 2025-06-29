# Optimization of Contract Distribution Based on Multi-objective Estimation of Distribution Algorithm 

Laihong Hu<br>Xi'an Research Inst. of Hi-tech 710025 Xi'an<br>Shannxi, P.R. China $+86029-62651749$ guyue2028@163.com

Xiaogang Yang<br>Xi'an Research Inst. of Hi-tech<br>710025 Xi'an<br>Shannxi, P.R. China $+86029-62651741$<br>doctoryxg@163.com<br>Hongdong Fan<br>Xi'an Research Inst. of Hi-tech<br>710025 Xi'an<br>Shannxi, P.R. China $+86029-62651744$ fhd06@mails.tsinghua.edu.cn


#### Abstract

Contract distribution is widely exists in modern commercial society, which mainly depends on qualitative analysis, and there still lack studies of quantitative analysis. Based on multi-objective estimation of distribution algorithm (MOEDA), quantitative research idea on contract distribution is explored in this article. First of all, Multi-objective optimization model is built for contract distribution. Then, the algorithm flow base on MOEDA is designed. At last, simulations are carried out and compare with multi-objective genetic algorithm (MOGA). The simulation results show that the MOEDA performs better than MOGA, and verify the effectiveness and robustness of the proposed method in optimization of contract distribution.


## CCS Concepts

- Computing methodologies $\rightarrow$ Discrete space search


## Keywords

Contract distribution; Multi-objective optimization problem; Estimation of distribution algorithm; Genetic algorithm

## 1. INTRODUCTION

With the development of information technology and logistics industry in modern commercial society, large contracts are often assigned to several contractors, such as large project contract, government procurement contract, and so on. Now, contract distribution mainly depends on qualitative analysis, such as expert experience, which is lacking in quantitative methods of evaluation. In addition, contract distribution is affected by a variety of factors, such as total cost, quality of service, and it is difficult to analyze the influence of a single factor. Therefore, the problem of contract distribution is treated as a multi-objective optimization problem (MOOP). In this article, MOEDA is introduced to solve the optimization problem of contract distribution, which makes evaluation result more scientific and provides a quantitative basis for decision making.

[^0]Estimation of distribution algorithm (EDA) is a new class of evolutionary algorithms, which combine the statistical theory with evolutionary schemes [1], [2]. According to the information of some better individuals in the current population, the model of probability is built to describe the distribution of all the solutions. Then a new population can be obtained by sampling from this model of probability [3]. Compared with traditional evolutionary algorithms, such as genetic algorithm (GA), EDA is also population-based algorithm, but there are no crossover and mutation operators [4], [5].
The rest of the article is organized as follows. Section 2 provides an overview of MOOP. Next in Section 3, the multi-objective optimization for contract distribution is given. Section 4 is solving the problem using MOEDA, in which the algorithm flow is designed. In Section 5, simulations are performed and MOEDA is compared with MOGA. In Section 6, conclusions are put forward.

## 2. BRIEF OVERVIEW OF MOOP

The general formulation of deterministic MOOP is as follows [6]:

$$
\begin{gathered}
\text { Minimize } Y=f(x)=\left(f_{1}(x), f_{2}(x), \ldots, f_{m}(x)\right) \\
\text { S.t. } e(x)=\left(e_{1}(x), e_{2}(x), \ldots, e_{k}(x)\right) \geq 0
\end{gathered}
$$

where, $x=\left(x_{1}, x_{2}, \ldots, x_{n}\right) \in X$ is the $n$-th decision vector, $y=\left(y_{1}, y_{2}, \ldots, y_{m}\right) \in Y$ is the $m$-th objective vector, $e_{i}(x)$ is the $k$-th constrain.

The concept of "optimal" for MOOP was first proposed by Francis Ysidro Edgeworth, and was providing complete definition by Vilfredo Pareto, so it is usually called "Pareto optimal" [7].

Definition 1: Pareto dominate. Solution $x^{0}$ Pareto dominates solution $x^{1}$ (denoted $x^{0}>x^{1}$ ), if and only if

$$
\begin{aligned}
f_{i}\left(x^{0}\right) \geq f_{i}\left(x^{1}\right) \quad \forall i \in\{1,2, \ldots, M\} \wedge f_{i}\left(x^{0}\right) & >f_{i}\left(x^{1}\right) \\
\exists i \in\{1,2, \ldots, M\}
\end{aligned}
$$

Definition 2: Pareto optimal. Solution $x^{0}$ is Pareto optimal, if and only if

$$
-\exists x^{1}: x^{1}>x^{0}
$$

Definition 3: Pareto optimal set. The set of all Pareto optimal solutions.

$$
P_{X}=\left\{x^{0}:-\exists x^{1}>x^{0}\right\}
$$


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from Permissions@acm.org.
    ICCAI 2018, March 12-14, 2018, Chengdu, China
    (C) 2018 Association for Computing Machinery.

    ACM ISBN 978-1-4503-6419-5/18/03\$15.00
    https://doi.org/10.1145/3194452.3194455

The curve or surface, which composed of all solution vectors in the Pareto optimal set, is denoted Pareto front, as shown in Figure 1 .
![img-0.jpeg](img-0.jpeg)

Figure 1. Pareto front of two objectives.
It is difficult to find a satisfactory solution for MOOP because that the objectives mutually restricted and influenced with each other, and optimizing one of them must at the expense of the sacrifices of others. Traditional methods for solving MOOP are mainly attributed to multi-objective linear combination, such as weighted method, constraint method, min-max method [8], which has strict restrictions in mathematically, such as continuous, differentiable. Besides, optimization efficiency is low that it needs a huge amount of time and computation for comprehensive problems, which greatly limit their application scope. With the development of intelligent optimization methods, evolutionary algorithm has been applied widely to solve MOOP due to its robust and adaptive capacity [9], [10].

## 3. CONTRACT DISTRIBUTION MODEL

Generally, there are many factors which influence contract distribution. In order to simplify the model, only main factors are chose for establishing objective functions, such as total cost, quality of service and malicious competition index.
(1) Total cost. It is always hoped that the lower the better for total cost of the contract, so the objective function can be established as:

$$
\min f_{1}(x)=\sum_{i=1}^{N} a_{i} x_{i}
$$

where, $N$ is the number of contractors, $x_{i} \quad(i=1,2, \cdots, N)$ is the purchase quantity which distribution to the $i$ th contractor, $a_{i}$ is the purchase unit-price.
(2) Quality of service. It is included product quality, maintenance period, service response time, service level, and so on. Quality of service is always hoped better, so the objective function can be established as:

$$
\max f_{2}(x)=\sum_{i=1}^{N} b_{i} x_{i}
$$

where, $b_{i}$ denotes the weight of quality of service.
Eq. (2) can be rewritten as:

$$
\min f_{2}^{\prime}(x)=\gamma / \sum_{i=1}^{N} b_{i} x_{i}
$$

where, $\gamma$ is adjustment coefficient.
(3) Malicious competition index. In order to avoid malicious competition in the form of false price or false propaganda, malicious competition index is introduced to the model of contract distribution. It is hoped that the lower the better for malicious
competition index of contract, so the objective function can be established as:

$$
\min f_{3}(x)=\sum_{i=1}^{N} c_{i} x_{i}
$$

where, $c_{i}$ denotes the weight of malicious competition index.
In addition, the purchase quantity which distribution to the $i$-th contractor can't overstep its production capacity, so $0 \leq x_{i} \leq L_{S}$, where, $L_{S}$ denotes the production capacity of the $i$-th contractor.

Based on these requirements mentioned above, multi-objective functions for contract distribution are established as follows:

$$
\begin{gathered}
\min f_{1}(x)=\sum_{i=1}^{N} a_{i} x_{i} \\
\min f_{2}(x)=\gamma / \sum_{i=1}^{N} b_{i} x_{i} \\
\min f_{3}(x)=\sum_{i=1}^{N} c_{i} x_{i} \\
\text { s.t. } \sum_{i=1}^{N} x_{i}=J \\
0 \leq x_{i} \leq L_{S}
\end{gathered}
$$

## 4. ALGORITHM FLOW BASED ON MOEDA

(1) Generate initial population

According to characteristics of the discrete variable optimization, integer code is adopted. The $k$-th individual encodes as $x^{k}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$, where, $n$ is the number of contractors, $x_{i}$ $(i=1,2, \cdots, n)$ is the purchase quantity which distribution to the $i$-th contractor. The initial population is sampled random from the feasible region, which is the production capacity of the contractor.
(2) Calculate the fitness of every individual

The objective functions $f_{1} \sim f_{3}$ in Eq. (5) are chose to be fitness functions.
(3) Calculate dominated number and dominate number

Two vectors $P=\left(p_{1}, p_{2}, \ldots, p_{l}\right)$, $Q=\left(q_{1}, q_{2}, \ldots, q_{i}\right)$ are defined, where, $l$ is population size, $p_{i}$ denotes dominated number of the $i$-th individual, and $q_{i}$ denotes dominate number of the $i$-th individual. Calculate $P$ and $Q$ as follows:
a. Individual $x^{i}$ and $x^{j}$ don't dominate each other, there is no change of $p_{i}, q_{i}, p_{j}, q_{j}$.
b. There exists dominance relationship between individual $x^{i}$ and $x^{j}$, if $x^{i}<x^{j}$, then $q_{i}=q_{i}+1, p_{j}=p_{j}+1$; else if $x^{i}<x^{j}$, then $p_{i}=p_{i}+1, q_{j}=q_{j}+1$.

(4) Choose good individuals

Rank the individual as follow strategy:
a. Dominated numbers of individual $x^{i}$ and $x^{j}$ are compared first. If $p_{i}<p_{j}$, then the individual $x^{i}$ is in front of the individual $x^{j}$; otherwise, the individual $x^{j}$ is in front of the individual $x^{i}$.
b. When $p_{i}=p_{j}$, then compare dominate numbers of individual $x^{i}$ and $x^{j}$. If $q_{i}>q_{j}$, then the individual $x^{i}$ is in front of the individual $x^{j}$; otherwise, the individual $x^{j}$ is in front of the individual $x^{i}$.

Higher-ranking individuals are chosen to be good individuals, which number lies on the evolution pool size.
(5) Establish probabilistic model

The gaussian model is chosen for the probabilistic model, which mean $m_{p}$ and standard deviation $\sigma_{p}$ are calculated based on the chosen good individuals.
(6) Generate new population

New population generated via Gauss sampling based on the probabilistic model established in step (5). Meanwhile, strategy of elitist preservation chooses to copy better individuals for the next generation which ensures global convergence.

## 5. SIMULATION AND ANALYSIS

### 5.1 Initial Conditions

Contract object is to purchase 500 sets of equipment, and 4 contractors participate in the distribution of contract, so there are $N=4, J=500$ in Eq. (5). The weight of total cost, quality of service and malicious competition index for 4 contractors is shown in Table 1.

TABLE 1. Weight of contractors


According to the production capacity of each contractor, $L_{i}=(500,400,350,300)$ in Eq. (5). In order to make the orders of magnitude more close to the objective functions, the adjustment coefficient in the objective function $f_{2}$ is $\gamma=10000$.

### 5.2 Simulation Results and Analysis

For more objective comparison of MOEDA and MOGA, a variety of different population sizes, evolution pool sizes and
evolutionary generations are selected for comparison. The selected parameters are shown in Table 2.

Table 2. Parameters of multi-objective evolutionary algorithm
Take the three sets of parameters in Table 2 to MOEDA and MOGA, the average fitness evolution curve and Pareto optimal distribution map are obtained in Figure 2-7.
![img-3.jpeg](img-3.jpeg)

Figure 2. Average fitness evolution curve (Parameter 1).
![img-3.jpeg](img-3.jpeg)

Figure 3. Pareto optimal distribution map (Parameter 1).
![img-3.jpeg](img-3.jpeg)

Figure 4. Average fitness evolution curve (Parameter 2).

![img-4.jpeg](img-4.jpeg)

Figure 5. Pareto optimal distribution map (Parameter 2).
![img-5.jpeg](img-5.jpeg)

Figure 6. Average fitness evolution curve (Parameter3).
![img-6.jpeg](img-6.jpeg)

Figure 7. Pareto optimal distribution map (Parameter 3) .

The average time consumption of two algorithms is shown in Table 3.

Table 3. Average time consumption of the two algorithms

Comparing the application of MOEDA and MOGA in the contract distribution, the time consumption of the two algorithms is quite similar, and the algorithm parameters (population size, evolution pool size, etc.) have less influence on the results, so the algorithm has better robustness. On the whole, the effect of MOEDA is a little better than MOGA, which can find better solutions. But from the distribution of Pareto optimal solution, the spatial distribution
of MOGA is more evenly. The main reason is that MOEDA is calculated from the general population. As well MOGA is more focused on the individual operation.

## 6. CONCLUSIONS

The article established optimization model for contract distribution with three objectives of total cost, quality of service and malicious competition index, and designed the algorithm flow based on MOEDA. Simulation results show that the proposed method is able to obtain the Pareto front, which can reflect the results of each contract distribution plan intuitively and provide more effective support for the operating staff.

## 7. ACKNOWLEDGMENTS

This work is supported by the National Natural Science Foundation of China (Nos. 61203189, 61401470, 61503389), and by the Natural Science Foundation of Shaanxi Province of China (Nos. 2017JM6010).
