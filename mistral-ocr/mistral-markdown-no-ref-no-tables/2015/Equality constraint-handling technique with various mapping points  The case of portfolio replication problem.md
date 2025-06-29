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
