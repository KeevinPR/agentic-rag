# Equality Constraint-handling Technique with Various Mapping Points: The Case of Portfolio Replication Problem 

Yukiko Orito<br>Department of Economics, Hiroshima University, Hiroshima 739-8525, Japan<br>Email: orito@hiroshima-u.ac.jp


#### Abstract

For solving an equality constrained optimization problem, it is difficult to find an optimal solution by using any evolutionary algorithms. We propose a new technique that handles an equality constraint in this paper. The technique transforms variables of solution on equality constrained search space to them on unconstrained search space through trigonometrical functions. Thus, this paper presents the contribution that an evolutionary algorithm effectively finds good feasible solutions without evolutionary stagnation because an unconstrained space consists only of feasible solutions. However, our technique searches mapping points only on the part of constrained space because it cannot transform the constrained space to fully unconstrained space. Therefore, we expand such a space consisting of various mapping points by exchanging trigonometrical functions on EDA (Estimation of Distribution Algorithm). In numerical experiments, for portfolio replication problems, we demonstrate the effectiveness of our technique.


## I. InTRODUCTION

In a constrained optimization problem, we have to find an optimal solution on a search space consisting of many feasible solutions and many infeasible solutions. It is difficult to find an optimal solution by using evolutionary algorithms because the algorithms need to search for only feasible solutions. For optimizing such a problem, many researchers have proposed their own techniques in evolutionary algorithms that search efficiently for feasible solutions. Coello[1] provided a survey of popular constraint-handling techniques used with evolutionary algorithms: the techniques are classified into five categories; penalty functions, special representations and operators, repair algorithms, separation of objectives and constraints, and hybrid methods. Almost all of evolutionary algorithms employing these techniques search for optimal solutions on constrained search spaces. It is well known that, however, any evolutionary algorithms work better on unconstrained search spaces than do on constrained search spaces. In this paper, we focus on such an efficient search of evolutionary algorithms on unconstrained search space.

For handling constraints, Koziel and Michalewicz[2] proposed a homomorphous mapping technique. Their technique is categorized as special representations and operators for constraint-handling techniques[1] and has contribution that a constrained search space itself is partially transformed to an unconstrained search space. In this paper, we propose a new technique, one of homomorphous mappings, which

Yoshiko Hanada<br>Faculty of Engineering Science, Kansai University, Osaka 564-8680, Japan<br>Email: hanada@kansai-u.ac.jp

handle an equality constraint. Our technique partially transforms variables of solution on equality constrained search space to them on unconstrained search space through trigonometrical functions. Thus, this paper presents the contribution that an evolutionary algorithm effectively finds good feasible solutions without evolutionary stagnation because an unconstrained space consists only of feasible solutions. However, our technique cannot transform the constrained space to fully unconstrained space. This technique searches mapping points only on the part of constrained space. In this paper, we expand such a space consisting of various mapping points by exchanging trigonometrical functions on EDA (Estimation of Distribution Algorithm). Although we show that our technique works very well for a portfolio replication problem; a wellknown application of an equality constrained optimization problem, our basic idea can be adapted to other equality constrained optimization problems.

This paper is organized as follows: We propose a new constraint-handling technique with various mapping points in Section II. Section III describes the EDA with fixed width histogram as our optimization method. Our EDA has the special representations for employing the equality constraint-handling technique. Section IV describes a portfolio replication problem as a real world application of equality constrained problem. Section V presents the results of numerical experiments, and we conclude our discussion in Section VI.

## II. Equality Constraint-handling Technique WITH Various MapPing Points

We consider the following equality constrained minimization problem.

$$
\begin{aligned}
\min f(\boldsymbol{x}) \\
\text { s.t. } g(\boldsymbol{x}) & =\sum_{i=1}^{N} x_{i} \\
& =1
\end{aligned}
$$

where $x_{i}$ is the $i$ th variable of solution $\boldsymbol{x}$.
The function $f(\boldsymbol{x})$ is an objective function and $g(\boldsymbol{x})$ is an equality constraint. This is one of general allocation problems where a constraint is denoted by the sum total of variables.

While an evolutionary algorithm is applied to the optimization problem given by the equation (1), infeasible solutions

generated by the algorithm are removed, evolved into or repaired to feasible solutions satisfying the equality constraint. Therefore, a construction of feasible solution brings about evolutionary stagnation.

In order to overcome such a problem, we propose a new constraint-handling technique with various mapping points in this paper. Our technique transforms the part of a given constrained search space to an unconstrained search space. It is expected that an evolutionary algorithm effectively finds good feasible solutions without evolutionary stagnation because an unconstrained search space consists only of feasible solutions.

Let $M$ be the length of binary digits. The number of variables is defined as $N=2^{M}(M=1,2, \cdots)$. When the $j$-th value of the binary number which converted from the decimal number $i-1(i=1, \cdots, N)$ is expressed as $a_{j} \in\{0,1\}(j=1, \cdots, M)$, the solution $\boldsymbol{x}^{*}$ is defined as follows.

$$
\begin{aligned}
\boldsymbol{x}^{*} & =\left(x_{1}, \cdots, x_{N}\right), \quad\left(\boldsymbol{x}^{*} \subset \boldsymbol{x}\right) \\
x_{i} & \equiv \prod_{j=1}^{M}\left(\cos ^{2} \theta_{j}\right)^{a_{j}}\left(\sin ^{2} \theta_{j}\right)^{1-a_{j}}, \quad(i=1, \cdots, N)
\end{aligned}
$$

From the Pythagorean theorem, that is,

$$
\sin ^{2} \theta_{j}+\cos ^{2} \theta_{j}=1 \quad(j=1, \cdots, M)
$$

the following equation is satisfied for any value of $\boldsymbol{\theta}=$ $\left(\theta_{1}, \cdots, \theta_{M}\right)$.

$$
\begin{aligned}
\sum_{i=1}^{N} x_{i} & =\prod_{j=1}^{M}\left(\sin ^{2} \theta_{j}+\cos ^{2} \theta_{j}\right) \\
& =1
\end{aligned}
$$

Therefore, our technique can transform the part of equality constrained search space to unconstrained search space through trigonometrical functions. In a word, $\boldsymbol{x}^{*}$ is the partial space on the constrained space $\boldsymbol{x}$ mapped from the unconstrained space $\boldsymbol{\theta}$. We re-define the equality constrained minimization problem given by the equation (1) as the following unconstrained minimization problem.

$$
\begin{aligned}
& \min f\left(\boldsymbol{x}^{*}\right), \quad\left(\boldsymbol{x}^{*} \subset \boldsymbol{x}\right) \\
& x_{i} \equiv \prod_{j=1}^{M}\left(\cos ^{2} \theta_{j}\right)^{a_{j}}\left(\sin ^{2} \theta_{j}\right)^{1-a_{j}}, \quad(i=1, \cdots, N)
\end{aligned}
$$

It is expected that an evolutionary algorithm effectively finds good feasible solutions $\boldsymbol{x}^{*}$ because the unconstrained search space $\boldsymbol{\theta}$ consists only of feasible solutions.

For example, for $M=2$ and $N=2^{2}=4$, the decimal number $0,1,2$, or 3 is expressed as binary number $00_{(2)}$, $01_{(2)}, 10_{(2)}$, or $11_{(2)}$, respectively. The search space $\boldsymbol{x}^{*}=$ $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$ is expressed as follows.

$$
\begin{gathered}
\boldsymbol{x}^{*}=\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \\
x_{1}=\sin ^{2} \theta_{1} \sin ^{2} \theta_{2} \\
x_{2}=\sin ^{2} \theta_{1} \cos ^{2} \theta_{2} \\
x_{3}=\cos ^{2} \theta_{1} \sin ^{2} \theta_{2} \\
x_{4}=\cos ^{2} \theta_{1} \cos ^{2} \theta_{2}
\end{gathered}
$$

![img-0.jpeg](img-0.jpeg)
![img-1.jpeg](img-1.jpeg)

Fig. 1. Search Space $\boldsymbol{x}^{*}$ mapped from $\boldsymbol{\theta}$

Based on the Pythagorean theorem, the following equation is satisfied for any value of $\theta_{1}$ and $\theta_{2}$.

$$
\begin{aligned}
\sum_{i=1}^{4} x_{i} & =\left(\sin ^{2} \theta_{1}+\cos ^{2} \theta_{1}\right)\left(\sin ^{2} \theta_{2}+\cos ^{2} \theta_{2}\right) \\
& =1
\end{aligned}
$$

The search space $\boldsymbol{x}^{*}=\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$ mapped from $\boldsymbol{\theta}=$ $\left(\theta_{1}, \theta_{2}\right)$ on the range of $[0, \pi]$ is shown in Fig. 1.

The equations (7) $\sim(10)$ say that the mapping points of each variable $x_{i}$ depend on them of other variables $x_{j} \mathrm{~s}(i \neq j)$ and are limited as shown in Fig. 1. In order to expand the search space $\boldsymbol{x}^{*}=\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$, we generate other mapping points by exchanging these equations to each variable. Here, we reexpress the four functions from the equation (7) to (10) as follows.

$$
\begin{aligned}
& y_{1}=\sin ^{2} \theta_{1} \sin ^{2} \theta_{2} \\
& y_{2}=\sin ^{2} \theta_{1} \cos ^{2} \theta_{2} \\
& y_{3}=\cos ^{2} \theta_{1} \sin ^{2} \theta_{2} \\
& y_{4}=\cos ^{2} \theta_{1} \cos ^{2} \theta_{2}
\end{aligned}
$$

From the equations (12) (15), of course, the equality constraint $x_{1}+\cdots+x_{4}=1$ is satisfied in any cases of the search spaces from the equation (16) to (39).

$$
\begin{aligned}
\boldsymbol{x}_{1}^{*} & =\left(x_{1}=y_{1}, x_{2}=y_{2}, x_{3}=y_{3}, x_{4}=y_{4}\right) \\
\boldsymbol{x}_{2}^{*} & =\left(x_{1}=y_{1}, x_{2}=y_{2}, x_{3}=y_{4}, x_{4}=y_{3}\right) \\
\boldsymbol{x}_{3}^{*} & =\left(x_{1}=y_{1}, x_{2}=y_{3}, x_{3}=y_{2}, x_{4}=y_{4}\right) \\
\boldsymbol{x}_{4}^{*} & =\left(x_{1}=y_{1}, x_{2}=y_{3}, x_{3}=y_{4}, x_{4}=y_{2}\right) \\
\boldsymbol{x}_{5}^{*} & =\left(x_{1}=y_{1}, x_{2}=y_{4}, x_{3}=y_{2}, x_{4}=y_{3}\right) \\
\boldsymbol{x}_{6}^{*} & =\left(x_{1}=y_{1}, x_{2}=y_{4}, x_{3}=y_{3}, x_{4}=y_{2}\right) \\
\boldsymbol{x}_{7}^{*} & =\left(x_{1}=y_{2}, x_{2}=y_{1}, x_{3}=y_{3}, x_{4}=y_{4}\right) \\
\boldsymbol{x}_{8}^{*} & =\left(x_{1}=y_{2}, x_{2}=y_{1}, x_{3}=y_{4}, x_{4}=y_{3}\right) \\
\boldsymbol{x}_{9}^{*} & =\left(x_{1}=y_{2}, x_{2}=y_{3}, x_{3}=y_{1}, x_{4}=y_{4}\right) \\
\boldsymbol{x}_{10}^{*} & =\left(x_{1}=y_{2}, x_{2}=y_{3}, x_{3}=y_{4}, x_{4}=y_{1}\right) \\
\boldsymbol{x}_{11}^{*} & =\left(x_{1}=y_{2}, x_{2}=y_{4}, x_{3}=y_{1}, x_{4}=y_{3}\right)
\end{aligned}
$$

$$
\begin{aligned}
\boldsymbol{x}_{12}^{*} & =\left(x_{1}=y_{2}, x_{2}=y_{4}, x_{3}=y_{3}, x_{4}=y_{1}\right) \\
\boldsymbol{x}_{13}^{*} & =\left(x_{1}=y_{3}, x_{2}=y_{2}, x_{3}=y_{1}, x_{4}=y_{4}\right) \\
\boldsymbol{x}_{14}^{*} & =\left(x_{1}=y_{3}, x_{2}=y_{2}, x_{3}=y_{4}, x_{4}=y_{1}\right) \\
\boldsymbol{x}_{15}^{*} & =\left(x_{1}=y_{3}, x_{2}=y_{1}, x_{3}=y_{2}, x_{4}=y_{4}\right) \\
\boldsymbol{x}_{16}^{*} & =\left(x_{1}=y_{3}, x_{2}=y_{1}, x_{3}=y_{4}, x_{4}=y_{2}\right) \\
\boldsymbol{x}_{17}^{*} & =\left(x_{1}=y_{3}, x_{2}=y_{4}, x_{3}=y_{2}, x_{4}=y_{1}\right) \\
\boldsymbol{x}_{18}^{*} & =\left(x_{1}=y_{3}, x_{2}=y_{4}, x_{3}=y_{1}, x_{4}=y_{2}\right) \\
\boldsymbol{x}_{19}^{*} & =\left(x_{1}=y_{4}, x_{2}=y_{2}, x_{3}=y_{3}, x_{4}=y_{1}\right) \\
\boldsymbol{x}_{20}^{*} & =\left(x_{1}=y_{4}, x_{2}=y_{2}, x_{3}=y_{1}, x_{4}=y_{3}\right) \\
\boldsymbol{x}_{21}^{*} & =\left(x_{1}=y_{4}, x_{2}=y_{3}, x_{3}=y_{2}, x_{4}=y_{1}\right) \\
\boldsymbol{x}_{22}^{*} & =\left(x_{1}=y_{4}, x_{2}=y_{3}, x_{3}=y_{1}, x_{4}=y_{2}\right) \\
\boldsymbol{x}_{23}^{*} & =\left(x_{1}=y_{4}, x_{2}=y_{1}, x_{3}=y_{2}, x_{4}=y_{3}\right) \\
\boldsymbol{x}_{24}^{*} & =\left(x_{1}=y_{4}, x_{2}=y_{1}, x_{3}=y_{3}, x_{4}=y_{2}\right)
\end{aligned}
$$

We adopt all various mapping points as the search space from the equation (16) to (39) in our EDA.

## III. Evolutionary Algorithm: EDA with Fixed Width Histogram

Among the current evolutionary algorithms to the optimization problems, we find: PBIL (Population-Based Incremental Learning)[3], Compact GA (Compact Genetic Algorithm)[4], EDA with histograms[5]. These algorithms are effective to a problem without dependency between variables included in a solution. Our EDA is based on the EDA with fixed width histogram which proposed by Tsutsui et al. [5].

For the unconstrained search space, as a genetic representation, the $k$-th individual on the $l$-th generation's population is represented as

$$
\boldsymbol{\theta}^{(l, k)}=\left(\theta_{1}^{(l, k)}, \cdots, \theta_{M}^{(l, k)}\right)
$$

The function $f\left(\boldsymbol{x}^{*(l, k)}\right)$ given by the equation (5) is employed as an evaluation function in the EDA. The details of the function are described in Section IV as a real world application.

As described in Section II, our technique has various mapping points by exchanging the definition of each $x_{i}$. For example, for $M=2$ and $N=2^{2}=4$, there were 24 search spaces from $\boldsymbol{x}_{1}^{*}$ to $\boldsymbol{x}_{24}^{*}$, given by the equations (16) $\sim(39)$, mapped from $\boldsymbol{\theta}$. Applying the EDA to the unconstrained space $\boldsymbol{\theta}$, we have to determine the search space $\boldsymbol{x}^{*}$ defined as one of all spaces between $\boldsymbol{x}_{1}^{*}$ and $\boldsymbol{x}_{24}^{*}$. In this paper, we apply the following EDA to all spaces, and then select one solution that has the best evaluation value of all.

For each of all spaces between $\boldsymbol{x}_{1}^{*}$ and $\boldsymbol{x}_{24}^{*}$, the procedure of the EDA consists of processes from Step 1 to Step 5.

1) Initial State

At an initial generation of $l=0, N_{p}$ individuals are randomly generated in an initial parents' population. Here, it is defined as

$$
\left(\boldsymbol{\theta}^{(0,1)}, \cdots, \boldsymbol{\theta}^{\left(0, N_{p}\right)}\right)
$$

Each variable is determined by a value on the range of $[0, \pi]$.
2) Histograms from Parents' Population

For the parents' population $\boldsymbol{\theta}^{(l, k)}$ on the $l$-th generation, the interval of a variable on the range of $[0, \pi]$ is divided into $H$ discrete intervals. A histogram consists of $N_{p}$ individuals in the parents' population. Thereby, Bin $h(h=1, \cdots, H)$ is a bin of the discrete interval on the range of $[\pi(h-1) / H, \pi h / H]$. The histogram with frequencies to the bin $h$ is defined as

$$
\begin{gathered}
v_{j}^{(l)}[h]=\#\left\{k \left\lvert\, \frac{\pi(h-1)}{H} \leq \theta_{j}^{(l, k)}<\frac{\pi h}{H}\right.\right\} \\
\left(k \in\left\{1, \cdots, N_{p}\right\}, j=1, \cdots, M\right. \\
h=1, \cdots, H)
\end{gathered}
$$

where $\#$ means the frequencies at the bin $h$.
3) Probability Distribution for Offspring Population An offspring population consisting of $N_{o}$ individuals are generated from the current parents' population. We assume that the histogram of $j$-th variable defined by the equation (42) is the probability distribution of $j$-th variable for producing an offspring population. Let $p_{j}^{(l)}[h]$ be the probability of $j$-variable to $h$ on the $l$-th generation. The probability distribution of $j$ th variable is defined as

$$
\begin{aligned}
p_{j}^{(l)}[h] & =\frac{1}{N_{p}} v_{j}^{(l)}[h] \\
(j & =1, \cdots, M, h=1, \cdots, H)
\end{aligned}
$$

For producing offspring population, the $h^{*}$ of each variable is randomly selected according to the distributions given by the equation (43) and then a new variable is randomly determined from the range of $\left[\pi\left(h^{*}-1\right) / H, \pi h^{*} / H\right]$.
4) Selection

When the individual $\left(\theta_{1}^{(l, k)}, \cdots, \theta_{M}^{(l, k)}\right)$ is given, the solution $\left(x_{1}^{(l, k)}, \cdots, x_{N}^{(l, k)}\right)$ is mapped from the individual, and then the value of the evaluation function is obtained by the equation (5).
Based on the values of the evaluation function, $N_{p}$ individuals are selected by the elitism selection and the roulette wheel selection from the current parents' and offspring populations for the next generation.
5) Terminate Criterion

The operations of producing the parents' population, making the probability distribution, producing the offspring population, and performing the selection are repeated until the maximal number of the repetitions is satisfied.

From the last generation, we select one solution that has the lowest evaluation value of all. This solution is the optimum or quasi-optimum solution obtained by the EDA for each of all spaces between $\boldsymbol{x}_{1}^{*}$ and $\boldsymbol{x}_{24}^{*}$.

## IV. Application: Portfolio Replication Problem

As described in Section II, our equality constrainedhandling technique was proposed in order to optimize a problem like the equation (1). The function $f\left(\boldsymbol{x}^{*}\right)$ is employed as the evaluation function of the EDA instead of $f(\boldsymbol{x})$.

In this paper, we deal with a long-only portfolio replication problem, one of allocation problems, as a real world

application. A portfolio consists of assets with long positions in which they have bought and been held. Many researchers have used various evolutionary algorithms to optimize their portfolios (for this, see. e.g. [6], [7], [8], [9], [10], [11]).

The portfolio, represented as the solution $\boldsymbol{x}$, is defined as follows.

$$
\begin{aligned}
\boldsymbol{x}= & \left(x_{1}, \cdots, x_{N}\right) \\
& \text { s.t. } \sum_{i=1}^{N} x_{i}=1, \quad\left(x_{i} \geq 0\right)
\end{aligned}
$$

From a practical viewpoint, an asset management firm (Company A) desires to make a replication portfolio to a portfolio of another firm (Company B) when the portfolio of Company B has delivered better performances than the portfolio of Company A. However, Company B opens only the total return of portfolio to the public but other information such as the proportion-weighted combination is closed to the public. Hence, it is difficult for Company A to replicate the portfolio of Company B.

In this paper, we optimize a replication portfolio to a given benchmark portfolio. Let $r_{i}(t)$ be the return of Asset $i(i=$ $1, \cdots, N)$ at $t$. The returns of replication portfolio consisting of $N$ assets over a period between $t=1$ and $t=T$ are represented as

$$
\left(\begin{array}{c}
r_{x}(1) \\
\vdots \\
r_{x}(T)
\end{array}\right)=\left(\begin{array}{ccc}
r_{1}(1) & \cdots & r_{N}(1) \\
& \vdots & \\
r_{1}(T) & \cdots & r_{N}(T)
\end{array}\right)\left(\begin{array}{c}
x_{1} \\
\vdots \\
x_{N}
\end{array}\right)
$$

In the equation (45), the returns of the replication portfolio $\left(r_{x}(1), \cdots, r_{x}(T)\right)$ are already given because the replication portfolio has the same returns as a benchmark portfolio. The returns of individual assets $\left(r_{i}(1), \cdots, r_{i}(T)\right)(i=1, \cdots, N)$ are also given. Therefore, if the number of days data $T$ is equal to the number of assets $N$, we can obtain an optimal solution $\boldsymbol{x}$ by solving the simultaneous equations. However, a proportion-weighted combination of benchmark portfolio changes on its rebalancing to keep track of the performances in the future periods. A benchmark portfolio is fixed only in a short period, so $T$ might be very less than $N$. In case studies of $T<N$, it is difficult to find the real optimal solution. In order to avoid this problem, we try to optimize a replication portfolio such that its return mimics a return of benchmark portfolio. Let $r_{x^{D}}(t)$ be the return of benchmark portfolio $x^{D}$ at $t$. For evaluating replication portfolios, we employ the following function consisting of the errors of returns and the rates of changes of returns between replication and benchmark portfolios as an objective function.

$$
\begin{aligned}
f(\boldsymbol{x})= & \sum_{t=1}^{T}\left(r_{x}(t)-r_{x^{D}}(t)\right)^{2} \\
& +\rho \sum_{t=1}^{T-1}\left(1-\frac{r_{x}(t+1)-r_{x}(t)}{r_{x^{D}}(t+1)-r_{x^{D}}(t)}\right)^{2}
\end{aligned}
$$

where $\rho$ is a parameter given in the experiments.

Based on the equations (5) and (46), the proposed equality constrained-handling technique is applied to optimize the replication portfolio. The equation (46) is employed as the evaluation function of EDA.

## V. NUMERICAL EXPERIMENTS

Our technique can transform the part of equality constrained search space to the unconstrained search space. The $\boldsymbol{x}^{*}$ is the partial space on the constrained space $\boldsymbol{x}$ mapped from the unconstrained space $\boldsymbol{\theta}$. In a word, our technique cannot find an optimal solution if the optimal solutuion is located on the space $\boldsymbol{x} \backslash \boldsymbol{x}^{*}$. To investigate the power of our technique, we compare some case studies that the optimal solution is located on the different space of $\boldsymbol{x}$.

## A. Experimental Setting

As described in Section IV, the real optimal solution is the benchmark portfolio for the portfolio replication problem. The benchmark portfolio consists of the proportion-weighted combination of $N$ assets (variables). In the numerical experiments, we employ $N$ assets with high turnover on the Tokyo Stock Exchange. Each training phase consists of $T=20$ days data from 2005 to 2010. We call them Phase 1 through Phase 14, respectively.

The setting of the optimization problem was as follows.

- The number of variables for individual $\boldsymbol{\theta}: M=2$
- $\quad$ The number of variables for solution $\boldsymbol{x}: N=2^{M}=4$
- Parameter of the equation (46): $\rho=1.0 E-08$

When the number of variables of solution is $N=4$, we have 24 kinds of different search spaces between $\boldsymbol{x}_{1}^{*}$ and $\boldsymbol{x}_{24}^{*}$ given by the equations (16) $\sim(39)$ for our EDA. For each of 24 spaces, the parameters of the EDA were set as follows.

- Parents' population size: $N_{p}=100$
- Offspring population size: $N_{o}=200$
- Elitist rate: 0.1
- The number of bins: $H=100$ (The width of bin is set to $\pi / H$.)
- Generation size: 100
- Algorithm run: 10

We adopt the following 11 kinds of benchmark portfolios as the optimal solutions located on the different spaces of $\boldsymbol{x}$. In this paper, we call them BP1 through BP11, respectively. The proportion-weighted combination of from BP1 to BP11 are shown in Table I and Fig. 2.

## B. Main Results

For each of all phases from Phase 1 to Phase 14, we optimized the replication portfolios by performing the EDA to each of the 11 benchmark portfolios from BP1 to BP11, respectively. In order to demonstrate the power of our technique, we compare the following two techniques.

TABLE I. BENCHMARK PORTFOLIO (OPTIMAL SOLUTION)

|  | $x_{1}$ | $x_{2}$ | $x_{3}$ | $x_{4}$ |
| :-- | :--: | :--: | :--: | :--: |
| BP1 | 0.4 | 0.3 | 0.2 | 0.1 |
| BP2 | 0.1 | 0.2 | 0.3 | 0.4 |
| BP3 | 0.2 | 0.5 | 0.2 | 0.1 |
| BP4 | 0.2 | 0.1 | 0.2 | 0.5 |
| BP5 | 0.1 | 0.2 | 0.5 | 0.2 |
| BP6 | 0.5 | 0.2 | 0.1 | 0.2 |
| BP7 | 0.1 | 0.4 | 0.1 | 0.4 |
| BP8 | 0.4 | 0.1 | 0.4 | 0.1 |
| BP9 | 0.4 | 0.1 | 0.1 | 0.4 |
| BP10 | 0.1 | 0.4 | 0.4 | 0.1 |
| BP11 | 0.25 | 0.25 | 0.25 | 0.25 |

![img-2.jpeg](img-2.jpeg)

Fig. 2. Benchmark portfolio (optimal solution)

- VMP: Equality Constraint-handling Technique with Various Mapping Points
This is our technique proposed in this paper. The EDA searches for all various mapping points as the search space from the equation (16) to (39). We call this technique VMP in this section.
- FMP: Technique with Fixed Mapping Points This is our technique without various mapping points. The EDA searches only for the fixed search space from the equation (16). We call this technique FMP in this section.

For all benchmark portfolios on all phases, the value of evaluation function (EF) and the mean squared error (MSE) of values of variables between replication and benchmark portfolios are shown in Table II.

Table II says that, for all benchmark portfolios on all phases, the values of evaluation function (EF) and the mean squared error (MSE) of solutions obtained by VMP are better than those of FMP. In particular, the results of VMP are very better than those of FMP for BP3, BP4, BP5, BP6, BP9, and BP10.

As described in Section II, in our technique, the mapping points of each variable $x_{i}$ depend on them of other variables $x_{j} \mathrm{~s}(i \neq j)$ and are limited as shown in Fig. 1. However, our technique can expand the search space by exchanging the equations (7) $\sim(10)$. To generate the various mapping points
by exchanging the definition of variable $x_{i}$ are very useful for the equality constrained optimization problem.

## C. Comparison of Our Technique and Traditional Repair Technique

We compare our technique VMP and the traditional repair technique. We call this traditional repair technique TRT in this section. The differences between VMP and TRT are explained bellow.

- VMP: Equality Constraint-handling Technique with Various Mapping Points
This is our technique proposed in this paper. For the EDA of VMP, the search space is the partial space $x^{*}$ on the constrained space $\boldsymbol{x}$ mapped from the unconstrained space $\boldsymbol{\theta}$. The VMP cannot transform the constrained space $\boldsymbol{x}$ to fully unconstrained space $\boldsymbol{\theta}$, but the EDA can search only on the unconstrained space $\boldsymbol{\theta}$ consisting of feasible individuals.
- TRT: Traditional Repair Technique

In the portfolio replication problems, many researchers proposed their own evolutionary algorithms[6], [7], [8], [9], [10], [11]. On the other hand, all their equality constraint-handling techniques are the same. In their reports, the evolutionary algorithms make the infeasible solution $\left(x_{1}^{\prime}, \cdots, x_{N}^{\prime}\right)$ as an offspring. The infeasible solution is repaired to the following feasible solution $\left(x_{1}, \cdots, x_{N}\right)$.

$$
\begin{gathered}
\left(x_{1}, \cdots, x_{N}\right)=\left(\frac{x_{1}^{\prime}}{S}, \cdots, \frac{x_{N}^{\prime}}{S}\right) \\
S=\sum_{i=1}^{N} x_{i}^{\prime}
\end{gathered}
$$

This repair technique restores the feasible solution from the infeasible solution. It means that the infeasible individual searched by evolutionary algorithms is changed to the different individual. Therefore, the construction of feasible solution may bring about evolutionary stagnation.
For the EDA of TRT, the search space is the constrained space $\boldsymbol{x}$. The TRT can search on the original constrained space $\boldsymbol{x}$, but the EDA needs to change the solution to feasible individual from infeasible one searched by the EDA.

We optimized the replication portfolios by performing VMP and TRT, respectively. For the EDA of VMP, the range of search space for each variable was set as $[0, \pi]$. On the other hand, for the EDA of TRT, it is set as $[0,1]$. In this context, for the EDA of TRT, the number of bin of histogram is set as $H / \pi$, not $H$ in the experiments below.

We apply the VMP and the TRT to optimize the replication portfolios when the number of variables of the solution is set to $N=2^{M}=4,8,16,32$, and 64 , respectively. For the benchmark portfolio BP1 on all phases, the value of evaluation function (EF) and the mean squared error (MSE) of values of variables between replication and benchmark portfolios are shown in Table III. In the table, the better result of VMP and TRT is written by boldface.

Table III says that, for BP1 on all phases, the values of evaluation function (EF) and the mean squared error (MSE) of solutions obtained by TRT are better than those of VMP when the number of variables of solution $N$ is small. When the number of the variables increases, however, the effectiveness of TRT becomes bad. In a word, our technique VMP is more effective for large scale problems than TRT is though it cannot search the whole original space $x$. For other benchmark portfolios from BP2 to BP11, we have obtained similar results to those for this BP1.

## VI. CONCLUSION

In this paper, we proposed a new equality constrainthandling technique that transforms variables of solution on equality constrained search space to them on unconstrained search space through trigonometrical functions. The technique gives various mapping points only on the partial space on the original constrained space mapped from the unconstrained space. The evolutionary algorithms can search only on the unconstrained space consisting of feasible individuals when employing our technique.

In the numerical experiments, we showed that our technique is more effective for large scale problems than the traditional repair technique is though it cannot search the whole original space. In addition, to generate the various mapping points by exchanging the definition of variables in our technique are very useful for the equality constrained optimization problem.

However, our technique cannot find an optimal solution if the real optimal solution is not located in the search possible mapping points. We need to estimate the location of optimal solution on the search space and quantify the distance between the optimum solution and the search possible mapping point. This is our future work.

## ACKNOWLEDGMENT

This work was supported by JSPS KAKENHI Grant Numbers \#25730148 and \#26330290.

## REFERENCES

[1] C. A. C. Coello, "Theoretical and Numerical Constraint-handling Techniques Used with Evolutionary Algorithms: A Survey of the State of the Art", Computer Methods in Applied Mechanics and Engineering, 191, $1245-1287$ (2002)
[2] S. Koziel, and Z. Michalewicz, "Evolutionary Algorithms, Homomorphous Mappings, and Constrained Parameter Optimization", Evolutionary Computation, 7, 1, 19-44 (1999)
[3] S. Baluja, "Population-based Incremental Learning: A Method for Integrating Genetic Search Based Function Optimization and Competitive Learning", Technical Report, CMU-CS-94-163, Carnegie Mellon University (1994)
[4] G. R. Harik, F. G. Lobo, and D. E. Goldberg, "The Compact Genetic Algorithm", Technical Report, 97006, IlliGAL Report (1997)
[5] S. Tsutsui, M. Pelikan, and D. E. Goldberg, "Probabilistic Modelbuilding Genetic Algorithms Using Marginal Histograms in Continuous Domain" Proceedings of the International Conference on KnowledgeBased and Intelligent Information \& Engineering Systems 2001, 112-121 (2001)
[6] Y. Xia, B. Liu, S. Wang, and K. K. Lai, "A Model for Portfolio Selection with Order of Expected Returns", Computers \& Operations Research, 27, $409-422(2000)$
[7] C. C. Lin and Y. T. Liu, "Genetic Algorithms for Portfolio Selection Problems with Minimum Transaction Lots", European Journal of Operational Research, 85, 1, 393-404 (2008)
[8] T. J. Chang, N. Meade, J. E. Beasley, and Y. M. Sharaiha, "Heuristics for Cardinality Constrained Portfolio Optimization", Computers \& Operations Research, 27, 1271-1302 (2000)
[9] Y. Crama and M. Schyns, "Simulated Annealing for Complex Portfolio Selection Problems", European Journal of Operational Research, 150, 546-571 (2003)
[10] K. J. Oh, T. Y. Kim, and S. Min, "Using Genetic Algorithm to Support Portfolio Optimization for Index Fund Management", Expert Systems with Applications, 28, 371-379 (2005)
[11] Y. Orito, H. Yamamoto, and Y. Tsujimura, "Equality Constrained LongShort Portfolio Replication by Using Probabilistic Model-building GA", Proceedings of WCCI 2012 IEEE World Congress on Computational Intelligence, IEEE Congress on Evolutionary Computation, 513-520 (2011)

TABLE II. RESULTS OF VMP AND FMP: THE VALUE OF EVALUATION FUNCTION (EF) AND THE MEAN SQUARED ERROR (MSE) OF SOLUTIONS BETWEEN REPLICATION AND BENCHMARK PORTFOLIOS

| Phase | BP1 |  |  |  | BP2 |  |  |  | BP3 |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | VMP |  | FMP |  | VMP |  | FMP |  | VMP |  | FMP |  |
|  | EF | MSE | EF | MSE | EF | MSE | EF | MSE | EF | MSE | EF | MSE |
| 1 | 1.917E-06 | 4.754E-04 | 1.917E-06 | 4.754E-04 | 1.409E-06 | 6.043E-04 | 1.409E-06 | 6.043E-04 | 4.845E-07 | 8.773E-05 | 1.846E-05 | 6.297E-03 |
| 2 | 2.022E-06 | 5.945E-04 | 2.022E-06 | 5.945E-04 | 9.962E-07 | 3.527E-04 | 9.962E-07 | 3.527E-04 | 8.331E-07 | 1.438E-04 | 1.766E-05 | 6.893E-03 |
| 3 | 7.391E-06 | 5.963E-04 | 7.391E-06 | 5.963E-04 | 3.998E-06 | 3.974E-04 | 3.998E-06 | 3.974E-04 | 3.460E-06 | 8.326E-05 | 7.490E-05 | 7.024E-03 |
| 4 | 2.075E-06 | 3.593E-04 | 2.075E-06 | 3.593E-04 | 2.310E-06 | 4.287E-04 | 2.310E-06 | 4.287E-04 | 4.798E-07 | 7.678E-05 | 2.791E-05 | 5.130E-03 |
| 5 | 1.173E-06 | 5.088E-04 | 1.173E-06 | 5.088E-04 | 2.326E-06 | 1.113E-03 | 2.326E-06 | 1.113E-03 | 4.871E-07 | 1.282E-04 | 3.835E-05 | 9.010E-03 |
| 6 | 1.775E-06 | 3.609E-04 | 1.775E-06 | 3.609E-04 | 4.319E-06 | 5.148E-04 | 4.319E-06 | 5.148E-04 | 4.254E-07 | 8.392E-05 | 3.138E-05 | 5.853E-03 |
| 7 | 5.684E-07 | 3.810E-04 | 5.684E-07 | 3.810E-04 | 6.164E-07 | 3.600E-04 | 6.164E-07 | 3.600E-04 | 1.652E-07 | 9.073E-05 | 1.229E-05 | 7.890E-03 |
| 8 | 4.552E-06 | 4.620E-04 | 4.552E-06 | 4.620E-04 | 2.745E-06 | 3.730E-04 | 2.745E-06 | 3.730E-04 | 7.410E-07 | 1.046E-04 | 9.751E-05 | 8.229E-03 |
| 9 | 6.659E-06 | 5.043E-04 | 6.659E-06 | 5.043E-04 | 6.343E-06 | 3.431E-04 | 6.343E-06 | 3.431E-04 | 2.131E-06 | 1.914E-04 | 5.362E-05 | 7.102E-03 |
| 10 | 7.902E-06 | 1.172E-03 | 7.902E-06 | 1.172E-03 | 2.855E-06 | 4.654E-04 | 2.855E-06 | 4.654E-04 | 4.004E-06 | 1.755E-04 | 4.538E-05 | 1.014E-02 |
| 11 | 1.429E-05 | 3.904E-04 | 1.429E-05 | 3.904E-04 | 8.946E-06 | 6.580E-04 | 8.946E-06 | 6.580E-04 | 1.907E-06 | 1.115E-04 | 1.415E-04 | 6.740E-03 |
| 12 | 2.659E-06 | 3.840E-04 | 2.659E-06 | 3.840E-04 | 5.445E-06 | 4.716E-04 | 5.445E-06 | 4.716E-04 | 5.490E-07 | 7.868E-05 | 4.128E-05 | 5.515E-03 |
| 13 | 5.114E-06 | 3.679E-04 | 5.114E-06 | 3.679E-04 | 6.982E-06 | 3.656E-04 | 6.982E-06 | 3.656E-04 | 9.563E-07 | 7.551E-05 | 7.745E-05 | 5.273E-03 |
| 14 | 1.870E-06 | 4.731E-04 | 1.870E-06 | 4.731E-04 | 1.148E-06 | 3.541E-04 | 1.148E-06 | 3.541E-04 | 9.021E-07 | 7.732E-05 | 3.322E-05 | 8.631E-03 |
| Phase | BP4 |  |  |  |  |  |  |  |  |  |  |  |
|  | VMP |  |  |  | VMP |  |  |  |  |  |  |  |
|  | EF | MSE | EF | MSE | EF | MSE | EF | MSE | EF | MSE | EF | MSE |
| 1 | 7.225E-06 | 3.770E-04 | 2.116E-05 | 9.284E-03 | 3.724E-07 | 1.415E-04 | 4.652E-05 | 1.612E-02 | 4.720E-07 | 1.403E-04 | 3.518E-05 | 6.934E-03 |
| 2 | 2.474E-07 | 7.727E-05 | 1.459E-05 | 5.216E-03 | 3.198E-07 | 9.736E-05 | 1.870E-05 | 5.585E-03 | 2.642E-07 | 9.759E-05 | 3.106E-05 | 1.014E-02 |
| 3 | 3.463E-06 | 1.187E-04 | 5.595E-05 | 5.903E-03 | 1.296E-06 | 1.190E-04 | 1.033E-04 | 9.396E-03 | 2.356E-06 | 1.435E-04 | 1.173E-04 | 1.050E-02 |
| 4 | 1.669E-06 | 1.563E-04 | 3.474E-05 | 6.355E-03 | 5.468E-07 | 9.198E-05 | 5.547E-05 | 9.366E-03 | 6.599E-07 | 1.014E-04 | 3.491E-05 | 5.549E-03 |
| 5 | 2.687E-07 | 1.255E-04 | 4.021E-05 | 1.647E-02 | 1.842E-06 | 2.813E-04 | 1.564E-05 | 7.713E-03 | 4.758E-07 | 9.512E-05 | 1.785E-05 | 6.995E-03 |
| 6 | 1.911E-06 | 1.614E-04 | 6.960E-05 | 8.615E-03 | 1.009E-06 | 1.147E-04 | 7.049E-05 | 9.635E-03 | 5.955E-07 | 1.119E-04 | 2.624E-05 | 5.394E-03 |
| 7 | 2.528E-07 | 1.197E-04 | 1.007E-05 | 5.621E-03 | 1.839E-07 | 7.889E-05 | 2.324E-05 | 5.583E-03 | 5.011E-07 | 1.571E-04 | 8.459E-06 | 5.694E-03 |
| 8 | 7.124E-07 | 8.743E-05 | 3.848E-05 | 5.663E-03 | 5.031E-07 | 7.878E-05 | 4.224E-05 | 5.175E-03 | 1.629E-06 | 1.122E-04 | 6.728E-05 | 7.138E-03 |
| 9 | 6.752E-07 | 9.500E-05 | 9.890E-05 | 5.335E-03 | 2.010E-06 | 1.330E-04 | 7.203E-05 | 7.171E-03 | 5.918E-07 | 9.138E-05 | 1.166E-04 | 6.617E-03 |
| 10 | 7.909E-07 | 9.350E-05 | 4.047E-05 | 6.340E-03 | 9.136E-07 | 1.235E-04 | 6.730E-05 | 5.816E-03 | 6.751E-07 | 1.411E-04 | 1.091E-04 | 1.577E-02 |
| 11 | 6.927E-06 | 1.043E-04 | 1.104E-04 | 9.503E-03 | 1.466E-06 | 1.262E-04 | 3.371E-04 | 1.225E-02 | 2.966E-06 | 1.117E-04 | 1.987E-04 | 6.775E-03 |
| 12 | 2.188E-06 | 2.201E-04 | 8.972E-05 | 6.460E-03 | 1.003E-06 | 9.938E-05 | 1.094E-04 | 1.103E-02 | 7.135E-07 | 1.031E-04 | 4.078E-05 | 5.985E-03 |
| 13 | 2.182E-06 | 1.229E-04 | 1.027E-04 | 5.358E-03 | 1.223E-06 | 8.096E-05 | 1.434E-04 | 7.158E-03 | 1.260E-06 | 9.238E-05 | 7.793E-05 | 5.745E-03 |
| 14 | 3.861E-07 | 1.080E-04 | 1.861E-05 | 5.669E-03 | 3.994E-07 | 1.026E-04 | 1.701E-05 | 5.242E-03 | 1.192E-06 | 1.031E-04 | 3.084E-05 | 7.517E-03 |
|  | BP7 |  |  |  |  |  |  |  |  |  |  |  |
| Phase | VMP |  |  |  |  |  |  |  |  |  |  |  |
|  | EF | MSE | EF | MSE |  |  |  |  |  |  |  |  |
| 1 | 4.260E-11 | 1.704E-09 | 4.260E-11 | 1.704E-09 | 1.593E-11 | 1.379E-09 | 1.593E-11 | 1.379E-09 | 2.919E-12 | 7.031E-10 | 1.139E-04 | 4.927E-02 |
| 2 | 1.032E-11 | 3.275E-09 | 1.032E-11 | 3.275E-09 | 2.669E-12 | 3.271E-10 | 2.669E-12 | 3.271E-10 | 2.841E-12 | 3.271E-10 | 7.056E-05 | 2.551E-02 |
| 3 | 2.610E-11 | 5.241E-10 | 2.610E-11 | 5.241E-10 | 2.774E-11 | 5.895E-10 | 2.774E-11 | 5.895E-10 | 2.857E-11 | 5.895E-10 | 2.702E-04 | 2.841E-02 |
| 4 | 5.407E-11 | 1.426E-09 | 5.407E-11 | 1.426E-09 | 1.531E-10 | 7.712E-09 | 1.531E-10 | 7.712E-09 | 3.334E-12 | 5.326E-10 | 1.646E-04 | 2.842E-02 |
| 5 | 6.434E-12 | 9.653E-10 | 6.434E-12 | 9.653E-10 | 1.218E-11 | 6.899E-10 | 1.218E-11 | 6.899E-10 | 2.853E-12 | 6.312E-10 | 8.687E-05 | 3.319E-02 |
| 6 | 3.953E-11 | 1.867E-10 | 3.953E-11 | 1.867E-10 | 1.357E-11 | 7.142E-10 | 1.357E-11 | 7.142E-10 | 3.930E-12 | 3.628E-10 | 1.468E-04 | 2.902E-02 |
| 7 | 1.460E-12 | 7.372E-10 | 1.460E-12 | 7.372E-10 | 9.835E-13 | 3.393E-10 | 9.835E-13 | 3.393E-10 | 2.883E-12 | 9.108E-10 | 3.779E-05 | 2.539E-02 |
| 8 | 3.952E-13 | 4.095E-11 | 3.952E-13 | 4.095E-11 | 2.773E-13 | 4.095E-11 | 2.773E-13 | 4.095E-11 | 2.052E-11 | 2.630E-09 | 2.196E-04 | 3.115E-02 |
| 9 | 2.150E-11 | 6.990E-10 | 2.150E-11 | 6.990E-10 | 6.159E-12 | 5.910E-10 | 6.159E-12 | 5.910E-10 | 3.766E-12 | 9.349E-11 | 4.099E-04 | 2.322E-02 |
| 10 | 1.408E-11 | 1.148E-09 | 1.408E-11 | 1.148E-09 | 2.077E-11 | 1.098E-09 | 2.077E-11 | 1.098E-09 | 6.400E-12 | 3.164E-10 | 2.027E-04 | 3.114E-02 |
| 11 | 2.602E-11 | 2.513E-10 | 2.602E-11 | 2.513E-10 | 2.429E-11 | 1.582E-09 | 2.429E-11 | 1.582E-09 | 1.061E-11 | 2.513E-10 | 5.959E-04 | 5.054E-02 |
| 12 | 6.014E-12 | 2.596E-10 | 6.014E-12 | 2.596E-10 | 1.120E-11 | 6.475E-10 | 1.120E-11 | 6.475E-10 | 3.985E-11 | 2.699E-09 | 2.534E-04 | 3.506E-02 |
| 13 | 5.529E-11 | 4.109E-09 | 5.529E-11 | 4.109E-09 | 2.636E-10 | 8.861E-09 | 2.636E-10 | 8.861E-09 | 3.740E-11 | 1.478E-09 | 4.375E-04 | 2.669E-02 |
| 14 | 1.365E-11 | 1.090E-09 | 1.365E-11 | 1.090E-09 | 3.214E-12 | 1.960E-10 | 3.214E-12 | 1.960E-10 | 1.304E-12 | 1.960E-10 | 9.119E-05 | 2.667E-02 |
|  | BP10 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
| Phase |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | 5.105E-11 | 5.973E-09 | 9.053E-05 | 3.054E-02 | 7.651E-12 | 2.077E-10 | 8.802E-12 | 2.077E-10 |  |  |  |  |
| 2 | 1.191E-12 | 2.217E-10 | 8.890E-05 | 3.231E-02 | 3.399E-12 | 7.559E-10 | 5.721E-12 | 1.961E-09 |  |  |  |  |
| 3 | 7.073E-12 | 1.161E-10 | 3.313E-04 | 3.077E-02 | 1.767E-13 | 4.594E-12 | 8.779E-12 | 1.779E-10 |  |  |  |  |
| 4 | 5.100E-12 | 9.555E-10 | 1.321E-04 | 2.449E-02 | 2.587E-11 | 4.143E-09 | 3.110E-11 | 3.764E-09 |  |  |  |  |
| 5 | 2.412E-13 | 2.791E-11 | 7.923E-05 | 4.118E-02 | 1.107E-11 | 5.082E-09 | 5.064E-11 | 1.058E-08 |  |  |  |  |
| 6 | 3.866E-12 | 1.867E-10 | 1.682E-04 | 2.795E-02 | 1.720E-11 | 1.359E-09 | 1.942E-11 | 1.541E-09 |  |  |  |  |
| 7 | 5.639E-13 | 3.519E-10 | 3.588E-05 | 2.366E-02 | 1.014E-12 | 4.634E-10 | 1.014E-12 | 4.634E-10 |  |  |  |  |
| 8 | 2.593E-11 | 2.714E-09 | 2.156E-04 | 2.595E-02 | 1.453E-11 | 1.730E-09 | 2.719E-11 | 1.374E-09 |  |  |  |  |
| 9 | 1.093E-11 | 1.435E-09 | 2.928E-04 | 3.846E-02 | 3.437E-12 | 1.745E-10 | 4.396E-12 | 1.745E-10 |  |  |  |  |
| 10 | 4.877E-12 | 1.631E-10 | 2.491E-04 | 5.403E-02 | 2.587E-12 | 1.803E-10 | 2.587E-12 | 1.803E-10 |  |  |  |  |
| 11 | 3.725E-11 | 1.375E-09 | 7.064E-04 | 3.216E-02 | 3.286E-11 | 1.083E-09 | 4.341E-11 | 7.880E-10 |  |  |  |  |
| 12 | 5.168E-12 | 2.596E-10 | 2.233E-04 | 2.695E-02 | 7.216E-11 | 5.221E-09 | 7.216E-11 | 5.221E-09 |  |  |  |  |
| 13 | 6.493E-12 | 3.065E-10 | 3.898E-04 | 2.434E-02 | 2.056E-11 | 4.496E-10 | 2.247E-11 | 4.964E-10 |  |  |  |  |
| 14 | 2.313E-11 | 1.021E-09 | 8.292E-05 | 2.482E-02 | 1.988E-11 | 1.473E-09 | 7.323E-11 | 6.411E-09 |  |  |  |  |

TABLE III. Results of VMP and TRT: The value of evaluation function (EF) and the mean squared error (MSE) of solutions

| Phase | The number of variables of solution: $N=4$ |  |  |  | The number of variables of solution: $N=8$ |  |  |  | The number of variables of solution: $N=16$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | VMP |  | TRT |  | VMP |  | TRT |  | VMP |  | TRT |  |
|  | EF | MSE | EF | MSE | EF | MSE | EF | MSE | EF | MSE | EF | MSE |
| 1 | 1.917E-06 | 4.754E-04 | 7.105E-11 | 1.852E-08 | 1.987E-04 | 8.534E-03 | 1.762E-04 | 6.751E-03 | 3.339E-04 | 3.906E-03 | 3.727E-04 | 4.865E-03 |
| 2 | 2.022E-06 | 5.945E-04 | 1.846E-10 | 3.389E-08 | 2.228E-04 | 9.245E-03 | 8.510E-05 | 1.364E-02 | 6.387E-04 | 9.501E-03 | 1.408E-04 | 1.623E-02 |
| 3 | 7.391E-06 | 5.963E-04 | 6.584E-10 | 3.890E-08 | 4.095E-03 | 4.396E-02 | 1.009E-03 | 1.312E-02 | 1.831E-03 | 1.641E-02 | 1.080E-03 | 7.824E-03 |
| 4 | 2.075E-06 | 3.593E-04 | 1.218E-10 | 2.027E-08 | 3.160E-04 | 9.254E-03 | 2.083E-04 | 1.307E-02 | 5.073E-04 | 4.288E-03 | 3.887E-04 | 6.743E-03 |
| 5 | 1.173E-06 | 5.088E-04 | 4.528E-10 | 1.617E-08 | 2.643E-04 | 3.131E-02 | 1.491E-04 | 1.564E-02 | 1.059E-03 | 8.786E-03 | 3.885E-04 | 1.137E-02 |
| 6 | 1.775E-06 | 3.609E-04 | 4.968E-10 | 3.206E-08 | 2.644E-04 | 1.070E-02 | 1.623E-04 | 5.900E-03 | 1.334E-03 | 1.026E-02 | 3.684E-04 | 1.184E-02 |
| 7 | 5.684E-07 | 3.810E-04 | 6.558E-11 | 3.369E-08 | 3.069E-04 | 1.837E-02 | 1.281E-04 | 9.551E-03 | 1.068E-03 | 9.678E-03 | 3.389E-04 | 9.174E-03 |
| 8 | 4.552E-06 | 4.620E-04 | 6.629E-11 | 3.149E-09 | 1.392E-03 | 5.118E-02 | 1.183E-03 | 2.717E-02 | 2.919E-03 | 2.552E-02 | 3.219E-03 | 1.154E-02 |
| 9 | 6.659E-06 | 5.043E-04 | 3.427E-10 | 1.942E-08 | 1.169E-03 | 2.695E-02 | 7.742E-04 | 1.635E-02 | 4.046E-03 | 2.283E-02 | 4.311E-03 | 7.438E-03 |
| 10 | 7.902E-06 | 1.172E-03 | 5.574E-10 | 1.181E-07 | 4.480E-03 | 4.034E-02 | 3.498E-03 | 2.966E-02 | 1.260E-02 | 4.151E-02 | 1.243E-02 | 1.575E-02 |
| 11 | 1.429E-05 | 3.904E-04 | 2.811E-10 | 4.535E-09 | 2.103E-03 | 2.519E-02 | 1.099E-03 | 2.202E-02 | 4.187E-03 | 1.603E-02 | 2.812E-03 | 1.272E-02 |
| 12 | 2.659E-06 | 3.840E-04 | 1.999E-10 | 1.126E-08 | 3.624E-03 | 2.570E-02 | 6.941E-04 | 2.401E-02 | 4.147E-03 | 8.024E-03 | 9.900E-04 | 2.200E-02 |
| 13 | 5.114E-06 | 3.679E-04 | 3.644E-10 | 1.348E-08 | 1.742E-03 | 1.446E-02 | 1.020E-03 | 1.145E-02 | 4.386E-03 | 6.354E-03 | 2.977E-03 | 1.338E-02 |
| 14 | 1.870E-06 | 4.731E-04 | 4.796E-10 | 2.747E-08 | 1.144E-03 | 1.726E-02 | 8.786E-04 | 1.552E-02 | 2.974E-03 | 8.055E-03 | 2.413E-03 | 1.287E-02 |
| Phase | The number of variables of solution: $N=32$ |  |  |  | The number of variables of solution: $N=64$ |  |  |  |  |  |  |  |
|  | VMP |  | TRT |  | VMP |  | TRT |  |  |  |  |  |
|  | EF | MSE | EF | MSE | EF | MSE | EF | MSE |  |  |  |  |
| 1 | 5.328E-04 | 2.278E-03 | 6.326E-04 | 5.973E-03 | 7.021E-04 | 5.057E-04 | 1.648E-03 | 3.441E-03 |  |  |  |  |
| 2 | 7.430E-04 | 1.826E-03 | 2.583E-04 | 8.460E-03 | 5.892E-04 | 5.019E-04 | 3.341E-04 | 4.449E-03 |  |  |  |  |
| 3 | 1.874E-03 | 3.368E-03 | 2.006E-03 | 5.111E-03 | 1.942E-03 | 1.535E-03 | 3.679E-03 | 4.105E-03 |  |  |  |  |
| 4 | 8.582E-04 | 1.269E-02 | 1.163E-03 | 6.080E-03 | 1.151E-03 | 4.856E-03 | 2.245E-03 | 3.796E-03 |  |  |  |  |
| 5 | 1.243E-03 | 5.269E-03 | 5.335E-04 | 5.022E-03 | 1.292E-03 | 2.857E-03 | 2.553E-03 | 2.991E-03 |  |  |  |  |
| 6 | 1.344E-03 | 3.390E-03 | 5.248E-04 | 7.649E-03 | 1.358E-03 | 1.187E-03 | 1.167E-03 | 4.465E-03 |  |  |  |  |
| 7 | 1.312E-03 | 2.667E-03 | 3.974E-04 | 8.144E-03 | 1.019E-03 | 6.917E-04 | 4.841E-04 | 4.898E-03 |  |  |  |  |
| 8 | 3.892E-03 | 1.121E-02 | 5.476E-03 | 3.877E-03 | 4.623E-03 | 3.555E-03 | 1.003E-02 | 3.687E-03 |  |  |  |  |
| 9 | 4.681E-03 | 9.539E-03 | 6.237E-03 | 5.574E-03 | 3.907E-03 | 4.493E-03 | 1.220E-02 | 3.865E-03 |  |  |  |  |
| 10 | 9.778E-03 | 2.081E-02 | 1.734E-02 | 6.847E-03 | 1.002E-02 | 1.021E-02 | 3.253E-02 | 4.562E-03 |  |  |  |  |
| 11 | 2.946E-03 | 4.808E-03 | 3.172E-03 | 5.866E-03 | 3.647E-03 | 3.062E-03 | 9.528E-03 | 3.623E-03 |  |  |  |  |
| 12 | 3.304E-03 | 2.831E-03 | 1.348E-03 | 1.101E-02 | 4.163E-03 | 1.166E-03 | 4.977E-03 | 4.219E-03 |  |  |  |  |
| 13 | 5.434E-03 | 1.453E-03 | 5.133E-03 | 5.090E-03 | 5.237E-03 | 4.842E-04 | 9.008E-03 | 3.384E-03 |  |  |  |  |
| 14 | 4.410E-03 | 6.639E-03 | 2.745E-03 | 8.921E-03 | 5.081E-03 | 2.256E-03 | 3.687E-03 | 4.597E-03 |  |  |  |  |