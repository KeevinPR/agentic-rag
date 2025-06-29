# Pareto-Based Multi-objective Estimation of Distribution Algorithm with Gaussian Copulas and Application in RFID Network Planning 

Ying Gao, Lingxi Peng, Fufang Li, Miao Liu and Xiao Hu


#### Abstract

A Pareto-based multi-objective estimation of distribution algorithm with Gaussian copulas is proposed and applied to RFID network planning. The algorithm employs Pareto-based approach and multivariate Gaussian copulas to construct probability distribution model. By estimating Kendall's tau and using the relationship of Kendall's tau and correlation matrix, Gaussian copula parameters are firstly estimated, thus, joint distribution is estimated. Afterwards, the Monte Carte simulation is used to generate new individuals. An archive with maximum capacity is used to maintain the non-dominated solutions. The Pareto optimal solutions are selected from the archive on the basis of the diversity of the solutions, and the crowding-distance measure is used for the diversity measurement. The archive gets updated with the inclusion of the non-dominated solutions from the combined population and current archive, and the archive which exceeds the maximum capacity is cut using the diversity consideration. The proposed algorithm is applied to some benchmark and RFID network planning. The relative experimental results show that the algorithm has better performance and is effective.


## I. INTRODUCTION

MULTI-OBJECTIVE optimization problems(MOOPs) are widely encountered in various fields of science and technology. The solution of a multi-objective optimization problem is usually a set of acceptable trade-off optimal solutions. This solution set is called a Pareto set[1]. Multi-objective optimization algorithms, especially those based on evolutionary principles, have seen wide acceptability because most engineering problems are NP-hard and therefore a quick computation of approximate solutions is often desirable. In recent years, a considerable amount of interest has been shown in multi-objective evolutionary algorithm (MOEA) and a number of different MOEAs have been suggested, such as Strength Pareto Evolutionary Algorithm (SPEA2)[2], Non-dominated Sorting Genetic Algorithm (NSGA-II) [3], and Fast Pareto Genetic Algorithm (FastPGA)[4].

Estimation of distribution algorithms(EDAs)[5] are a class of evolutionary algorithms based on probability distribution model. It has been proven that EDA has some

Manuscript received May 28, 2012. This work was supported in part by the Scientific and Technological Innovation Projects of Department of Education of Guangdong Province, P.R.C. and Guangzhou Science and Technology Projects under Grant No. 12C42011563, 11A11020499.

Y Gao is with the Department of Computer Science and Technology, Guangzhou University, Guangzhou, 510006, P.R. of China (phone: 86-020-39366631; fax: 86-020-39366375; e-mail: falcongao@sina.com.cn).
L Peng is with the Department of Computer Science and Technology, Guangzhou University, Guangzhou, 510006, P.R. of China (e-mail: lingxipeng@163.com).

F Li is with the Department of Computer Science and Technology, Guangzhou University, Guangzhou, 510006, P.R. of China (e-mail: lifufang@21en.com).
special characteristics of good convergence, high efficiency, concise concept and been successfully extended to multi-objective optimization problems. The performance of an EDA highly depends on how well it estimates and samples the probability distribution. Copula[6] is a recently developed mathematical theory and a power tool for multivariate probability analysis. It separates joint probability distribution function into the product of marginal distributions and a copula function which represents the dependency structure of random variables. Through copula, we can clearly represent the dependent relation of variables and analysis multivariate distribution of the underlying components. It has beed applied to constitute the probabilistic model in EDAs[7].

In this paper, EDA is extended to multi-objective optimization problems by using a Pareto-based approach and Gaussian copulas. The extended multi-objective EDA employs multivariate Gaussian copulas to construct probability distribution model. Gaussian copula parameters are firstly estimated, thus, joint distribution is estimated by estimating Kendall's tau and using the relationship of Kendall's tau and correlation matrix. Afterwards, the Monte Carte simulation is used to generate new individuals. An archive is used to maintain the non-dominated solutions. The Pareto optimal solutions are selected from the archive on the basis of the diversity of the solutions, and the crowding-distance measure is used for the diversity measurement. The archive gets updated with the inclusion of the non-dominated solutions from the combined population and current archive, and the archive which exceeds the maximum capacity is cut using the diversity consideration. The proposed algorithm is applied to some benchmark and RFID network planning. The experimental results show that the algorithm has better performance and is effective.

## II. Multi-Objective Optimization Problems

The general MOOPs can be defined as follows:

$$
\begin{gathered}
\min F(\mathbf{x})=\left\{f_{1}(\mathbf{x}), f_{2}(\mathbf{x}), \cdots, f_{k}(\mathbf{x})\right\} \\
\text { s.t. } g_{i}(\mathbf{x}) \leq 0, \quad i=1,2, \ldots, m \\
h_{i}(\mathbf{x})=0, \quad i=1,2, \ldots, p
\end{gathered}
$$

$g_{i}(\mathbf{x}) \leq 0$ and $h_{i}(\mathbf{x})=0$ define the feasible region $\Omega$ and any point in $\Omega$ defines a feasible solution.

The concept of optimum commonly adopted in MOOPs is Pareto optimality. Pareto optimality is defined as:

A point $\mathbf{x}^{*} \in \Omega$ is Pareto optimal if $\forall \mathbf{x} \in \Omega$ and $\mathrm{I}=\{1,2, \cdots, k\}$
either: $\forall i \in \mathrm{I} f_{i}\left(\mathbf{x}^{*}\right) \leq f_{i}(\mathbf{x})$
and, there is at least one $i \in \mathrm{I}$ such that $f_{i}\left(\mathbf{x}^{*}\right)<f_{i}(\mathbf{x})$

Other important definitions associated with Pareto optimality are Pareto dominance.

A vector $\mathbf{x}=\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ is said to dominate $\mathbf{y}=\left(y_{1}, y_{2}, \cdots, y_{n}\right)$, denoted by $\mathbf{x} \prec \mathbf{y}$, if and only if $\mathbf{x}$ is partially less than $\mathbf{y}$, i.e., $\forall i \in\{1,2, \cdots, k\} \quad x_{i} \leq y_{i}$ and, at least for one $i, x_{i}<y_{i}$.

For a given multi-objective problem $F(\mathbf{x})$, Pareto optimal set $P^{*}$ is defined as:

$$
P^{*}=\left\{\mathbf{x} \in \Omega \mid-\exists \mathbf{x}^{\prime} \in \Omega \quad F\left(\mathbf{x}^{\prime}\right) \prec F(\mathbf{x})\right\}
$$

Pareto front $P F^{*}$ is defined as:
$P F^{*}=\left\{F(\mathbf{x})=\left(f_{1}(\mathbf{x}), f_{2}(\mathbf{x}), \cdots, f_{k}(\mathbf{x})\right) \mid \mathbf{x} \in P^{*}\right\}$

## III. GAUSSIAN COPULAS

A copula[6] is a distribution function with known marginals. Any continuous Multivariate joint distribution of $n$ random variables $x_{1}, x_{2}, \ldots, x_{n}$
$F\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\operatorname{Pr}_{n} b\left(X_{1} \leq x_{1}, X_{2} \leq x_{2}, \ldots, X_{n} \leq x_{n}\right\}$, can be represented by a copula $C$ as a function of the marginal distribution $F_{X_{i}}\left(x_{i}\right)=\operatorname{Pr}_{n} b\left\{X_{i} \leq x_{i}\right\}, i=1,2, \cdots, n$; i.e.

$$
\begin{aligned}
F\left(x_{1}, x_{2}, \ldots, x_{n}\right) & =C\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \ldots, F_{n}\left(x_{n}\right)\right) \\
& =C\left(u_{1}, u_{2}, \ldots, u_{n}\right)
\end{aligned}
$$

Where $u_{i}=F_{X_{i}}\left(x_{i}\right), i=1,2, \cdots, n$ and $C\left(u_{1}, u_{2}, \ldots, u_{n}\right)$ is the associated copula function. Furthermore, application of the chain rule shows that the corresponding density function $f\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ can be decomposed as

$$
\begin{aligned}
f\left(x_{1}, x_{2}, \ldots, x_{n}\right) & =\frac{\partial^{n} C\left(u_{1}, u_{2}, \ldots, u_{n}\right)}{\partial u_{i} \partial u_{2} \ldots \partial u_{n}} \\
& =c\left(u_{1}, u_{2}, \ldots, u_{n}\right) \cdot f_{1}\left(x_{1}\right) \cdot f_{2}\left(x_{2}\right) \cdot \ldots \cdot f_{n}\left(x_{n}\right)
\end{aligned}
$$

From the above it may be seen that the joint density function is the product of the marginals $f_{i}\left(x_{i}\right), i=1,2, \cdots, n$ and copula densities function $c\left(u_{1}, u_{2}, \ldots, u_{n}\right)$.

Let $\mathbf{R}=\left(r_{i, j}\right), i=1,2, \cdots, n, j=1,2, \cdots, n$ be a symmetric, positive definite matrix with unit diagonal entries. The multivariate Gaussian copula is defined as

$$
C\left(u_{1}, u_{2}, \ldots, u_{n} ; \mathbf{R}\right)=\boldsymbol{\Phi}_{\mathbf{R}}\left(\varphi^{-1}\left(u_{1}\right), \varphi^{-1}\left(u_{2}\right), \cdots, \varphi^{-1}\left(u_{n}\right)\right)
$$

Where $\boldsymbol{\Phi}_{\mathbf{R}}$ denotes the standardized multivariate normal distribution with correlation matrix $\mathbf{R}=\left(r_{i, j}\right), i=1,2, \cdots, n, j=1,2, \cdots, n . \varphi^{-1}(x)$ denotes the inverse of the univariate standard normal distribution $\varphi(x)$.

The corresponding density is
$c\left(u_{1}, u_{2}, \ldots, u_{n} ; \mathbf{R}\right)=\frac{1}{|\mathbf{R}|^{1 / 2}} \exp \left(-\frac{1}{2} \boldsymbol{\omega}^{T}\left(\mathbf{R}^{-1}-\mathbf{I}\right) \boldsymbol{\omega}\right)$
with $\boldsymbol{\omega}=\left(\varphi^{-1}\left(u_{1}\right), \varphi^{-1}\left(u_{2}\right), \cdots, \varphi^{-1}\left(u_{n}\right)\right)^{T}$

## IV. Pareto-Based Multi-Objective EDA with GAUSSIAN COPULAS

The algorithm steps of pareto-based multi-objective EDA with Gaussian copulas for solving MOOPs is as follows:
$t=0$, initialize a population
$\mathrm{S}(0) \leftarrow$ Initialization ( $)$;
Evaluate(S(0))
$\mathrm{A}(0) \leftarrow$ Non_Dominated(S(0))
WHILE $t<\mathrm{T}$ DO
Estimate_Marginals_Distribution();
Estimate_Correlation_Matrix();
$\mathrm{S}^{\prime}(t) \leftarrow$ Sample( $)$;
$\mathrm{S}(t+1) \leftarrow$ Selection $(\mathrm{S}(\mathrm{t}) \cup \mathrm{S}^{\prime}(\mathrm{t}))$
Evaluate(S(t+1))
$\mathrm{A}(t+1) \leftarrow$ Non_Dominated(S(t+1) $\cup \mathrm{A}(\mathrm{t}))$
IF $|\mathrm{A}(t+1)|>\mathrm{M}$ THEN Cut_Archive(A $(t+1))$
$t \leftarrow \mathrm{t}+1$
END WHILE
Output the obtained Pareto optimal front
Initialization() is used to initialize a population $S(0)$ with size N. The initial population $S(0)$ is chosen randomly and should uniformly cover the entire solution space based on the consideration of the requirement of population diversity.

Evaluate() is used to evaluate individual in population.
$A(0)$ has been initialized to contain the non-dominated solutions from $\mathrm{S}(0)$.

Non_Dominated() returns the non-dominated solutions from a population.

Estimate_Marginals_Distribution() is used to estimate the marginals distribution from population.

Estimate_Correlation_Matrix() is used to estimate the correlation matrix $\mathbf{R}$ in Gaussian copulas.

A simple method[7] based on Kendall's tau is applied for estimating the correlation matrix $\mathbf{R}$. The method consists of constructing an empirical estimate of Kendall's tau for each bivariate margin of the copula and then using relationship (5)

$$
\tau\left(\mathbf{X}_{k}, \mathbf{X}_{m}\right)=\frac{2}{\pi} \arcsin \left(r_{k, m}\right)
$$

To infer an estimate of the relevant element of $\mathbf{R}$. More specifically we estimate $\tau\left(\mathbf{X}_{k}, \mathbf{X}_{m}\right)$ by calculating the standard sample c coefficient
$\hat{\tau}\left(\mathbf{X}_{k}, \mathbf{X}_{m}\right)=\frac{2}{n(n+1)} \sum_{i, i, i \leq k, n} \operatorname{sign}\left[\left(X_{i, k}-X_{j, k}\right)\left(X_{i, m}-X_{j, m}\right)\right]$
From the original data vectors $\mathbf{X}_{1}, \mathbf{X}_{2}, \ldots, \mathbf{X}_{N}$, and write the $j$ th component of the $i$ th vector as $X_{i, j}$; this yields an unbiased and consistent. An estimator of $r_{k, m}$ is then given by $\hat{r}_{k, m}=\sin \left(\frac{\pi}{2} \hat{\tau}\left(\mathbf{X}_{k}, \mathbf{X}_{m}\right)\right)$. In order to obtain an estimator of the entire matrix $\mathbf{R}$ we can collect all pairwise estimates $\hat{r}_{k, m}$ and then construct the estimator

$$
\hat{\mathbf{R}}=\left(\sin \left(\frac{\pi}{2} \hat{\tau}\left(\mathbf{X}_{k}, \mathbf{X}_{m}\right)\right)\right), k=1, \cdots N, m=1, \cdots, N
$$

Sample() is used to generate offspring population $\mathrm{S}^{\prime}(\mathrm{I})$ by sampling Gaussian copulas with correlation matrix $\mathbf{R}$ and the univariate standard normal distribution $\varphi(x)$ according to the following algorithm[7].

1) Find the Cholesky decomposition of $\mathbf{R}$, so that $\mathbf{A} \hat{\boldsymbol{X}}=\mathbf{R}$, with $\mathbf{A}$ lower triangular;
2) Generate a sample of $n$ independent random variables $\left(Z_{1}, Z_{2}, \ldots, Z_{n}\right)$ from $N(0,1)$;
3) Set $\mathbf{Y}=\mathbf{A Z}$ with $\mathbf{Z}=\left(Z_{1}, Z_{2}, \ldots, Z_{n}\right)^{T}$ and $\mathbf{Y}=\left(Y_{1}, Y_{2}, \ldots, Y_{n}\right)^{T}$
4) Return
$\mathbf{X}=\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\left(F_{1}^{-1}\left(\varphi\left(Y_{1}\right)\right), F_{2}^{-1}\left(\varphi\left(Y_{2}\right)\right), \ldots F_{n}^{-1}\left(\varphi\left(Y_{n}\right)\right)\right)$.
Selection() is used to evaluate individual in the current population $\mathrm{S}_{(t)}$ and the offspring population $\mathrm{S}^{\prime}(\mathrm{I})$ and carry out the non-dominated sorting and ranking selection, developed by Deb et al. in [3] to select non-dominated individuals to constitute the next generation population $\mathrm{S}(t+1)$.

The proposed algorithm maintains an archive $A(t)$ with maximum capacity M . The archive gets updated with the inclusion of the non-dominated solutions from the next generation population $\mathrm{S}(t+1)$ and $A(t)$. If the size of the archive exceeds the maximum capacity M , it is cut using the diversity consideration. Cut_Archive() is used to cut the archive.

## V. RFID Network Planning

The goal of RFID systems is to establish a wireless network, including: select a reasonable reader antenna position so that the wireless network can have the required coverage, ensure that RFID systems can provide effective communication performance and capacity, and control equipment costs within an acceptable range. RFID network planning[8][9] is to set a proper reader to ensure that the communications between electronic tags and readers. The reader has a limit on its interrogation range, within which the tags can be read by the reader. The placement of readers in RFID network is modeled in the following way. Assume we have a $\mathrm{X} \times \mathrm{Y}$ room. A number of RFID tags are evenly distributed in the area that needs signal coverage. For a RFID reader $I$, its detection range Ri is a function proportional to its emitting power Pi. That is $\mathrm{Ri}=\mathrm{f}(\mathrm{Pi})$. We simplify the model by claiming that if the distance between a tag and a reader $I$ is smaller than $R^{R}$ and there is no obstacle between them, then the tag can receive the signal sent by the reader. If a tag can receive the signal sent by exactly one reader, we say that the tag is detected by the reader. However, if a tag can receive the signal sent by more than one reader, it usually cannot respond to either of the readers because of the nature of passive RFID tags. We say that the tag is interfered. For each of the readers to be deployed in a placement, we need to consider following parameters:
$(x, y)$ : The position of the reader in the room, where
$\mathrm{x}[0 ; \mathrm{X}]$ and $\mathrm{y}[0 ; \mathrm{Y}]$.
P : The emitting power of the reader which directly affect the detection range R of the reader. Depends on the model of the reader, emitting power could be adjusted but limited in a range.

Multi-Objective Functions: The cost, the ratio of covered area and the ratio of the interfered area are the major factors need to be considered.

The cost function can be expressed as:

$$
f_{1}(\mathbf{x})=\mathrm{C}-\mathrm{N}^{*} \mathrm{p}
$$

Where C is the maximum cost or the budget, N is the number of readers, p is the unit price of reader. This function measures how much we can gain by deploying fewer readers.

The cover rate function is:

$$
f_{2}(\mathbf{x})=\frac{\text { DetectedTa gs }}{\text { TotalTags }}
$$

The interference rate function is:

$$
f_{1}(\mathbf{x})=\frac{\text { Interfered Tags }}{\text { TotalTags }}
$$

Encoding: A placement of readers needs to be encoded so that it can be used in the proposed algorithm. A RFID network planning $\mathbf{x}$ with n readers can be expressed as a vector $\mathbf{x}=\left(x_{1}, \cdots, x_{n}, y_{1}, \cdots, y_{n}, \mathrm{P}_{1}, \cdots, \mathrm{P}_{n}\right)$ where $\mathrm{x} 1, \mathrm{y} 1$ and Pl are the x-coordinate, y-coordinate, emitting power.

The overall optimal solution for RFID network planning is represented by $\min F(\mathbf{x})=\left\{f_{1}(\mathbf{x}), f_{2}(\mathbf{x}), f_{3}(\mathbf{x})\right\}$. The Pareto-based multi-objective estimation of distribution algorithm with Gaussian copulas is used to solve the MOOP.

## VI. EXPERIMENTAL RESULTS

In order to test efficiency of the proposed algorithm, the performance of the proposed algorithm is compared with that of some multi-objective optimization algorithms. The following benchmark functions[10] have been used to test.

1) ZDT1: $f_{1}(\mathbf{x})=x_{1}$

$$
\begin{aligned}
f_{2}(\mathbf{x})= & g(\mathbf{x})(1-\sqrt{x_{1} / g(\mathbf{x})}) \quad x_{1} \in[0,1] \\
& g(\mathbf{x})=1+9\left(\sum_{i=2}^{D} x_{i}\right) /(D-1)
\end{aligned}
$$

2) ZDT2: $f_{1}(\mathbf{x})=x_{1}$

$$
\begin{aligned}
f_{2}(\mathbf{x})= & g(\mathbf{x})\left(1-\left(x_{1} / g(\mathbf{x})\right)^{2}\right) \quad x_{1} \in[0,1] \\
& g(\mathbf{x})=1+9\left(\sum_{i=2}^{D} x_{i}\right) /(D-1)
\end{aligned}
$$

3) ZDT3: $f_{1}(\mathbf{x})=x_{1}$

$$
\begin{aligned}
& f_{2}(\mathbf{x})=g(\mathbf{x})\left(1-\sqrt{\frac{x_{1}}{g(\mathbf{x})}} \cdot \frac{x_{1}}{g(\mathbf{x})} \sin \left(10 \pi x_{1}\right)}\right) \quad x_{1} \in[0,1] \\
& g(\mathbf{x})=1+9\left(\sum_{i=2}^{D} x_{i}\right) /(D-1)
\end{aligned}
$$

4) ZDT4: $f_{1}(\mathbf{x})=x_{1}$

$$
\begin{gathered}
f_{2}(\mathbf{x})=g(\mathbf{x})\left(1-\sqrt{x_{1} / g(\mathbf{x})}\right) \quad x_{1} \in[0,1], x_{1} \in[-5,5], \\
g(\mathbf{x})=1+10(D-1)+\sum_{i=1}^{D}\left(x_{i}^{2}-10 \cos \left(4 \pi x_{1}\right)\right)
\end{gathered}
$$

5) ZDT6: $f_{1}(\mathbf{x})=1-\exp \left(-4 x_{1}\right) \sin ^{6}\left(6 \pi x_{1}\right)$

$$
\begin{gathered}
f_{2}(\mathbf{x})=g(\mathbf{x})\left(1-\left(f_{1}(x) / g(\mathbf{x})\right)^{2}\right) \quad x_{1} \in[0,1] \\
g(\mathbf{x})=1+9\left(\sum_{i=2}^{D} x_{i} /(D-1)\right)^{0.25}
\end{gathered}
$$

Convergence metric $\gamma[3]$ and Diversity metric $\Delta[3]$ were used. The smaller the value of these metrics is, the better the performance of the algorithm is. The initial population was generated from a uniform distribution in the ranges specified below. Population size $N=100$. All experiments were repeated for 20 runs. The maximum number of iterations is set to 2000 in each running. TABLE 1 listed the mean and variances of the convergence and diversity metrics obtained using SPEA2[2], NSGA-II[3], FastPGA[4] and the proposed algorithm (PMOEDAGC) on ZDT1, ZDT2, ZDT3, ZDT4 and ZDT6. It can be known from TABLE 1, in both aspects of convergence and distribution of solutions, PMOEDAGC outperforms SPEA2, NSGA-II and FastPGA on the benchmark functions.

The algorithm is also applied RFID network planning problem. A simplified $30 \mathrm{~m} \times 30 \mathrm{~m}$ square working area with 60 tags is used for the simulation. 20 RFID readers, whose radiated power is adjustable in the range from 0 to 30 dBm , are considered to serve this area. $\min F(\mathbf{x})=\left\{f_{1}(\mathbf{x}), f_{2}(\mathbf{x}), f_{3}(\mathbf{x})\right\}$ is used as the multi-objective function. The population size in the algorithm is set to 200 . The algorithm runs to a maximum number of 4000 iterations. A sample of Pareto optimal solution for network planning is listed in TABLE 2.

TABLE I
Mean and Variances of Convergence and Diversity Metrics for Multi-Objective Benchmark Functions


## VII. CONCLUSIONS

The proposed algorithm employs the multivariate Gaussian copulas to construct probability distribution model, and the new individuals are generated according to the model. An archive is used to maintain the non-dominated solutions. The Pareto optimal solutions are selected from the archive. The archive gets updated with the inclusion of the non-dominated solutions from the combined population and current archive.

The algorithm is applied to some benchmarks and RFID Network planning. The results show that the algorithm has better performance than SPEA2[2], NSGA-II[3], FastPGA[4] on the benchmarks and is effective in RFID networks planning.

TABLE II
a Sample of Pareto Optimal Solution for Network Planning

