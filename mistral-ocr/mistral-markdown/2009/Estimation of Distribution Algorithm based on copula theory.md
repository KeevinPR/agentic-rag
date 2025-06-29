# Estimation of Distribution Algorithm Based on Copula Theory 

Li-Fang Wang, Jian-Chao Zeng, and Yi Hong, Member, IEEE


#### Abstract

Estimation of Distribution Algorithm (EDA) is a novel evolutionary computation, which mainly depends on learning and sampling mechanisms to manipulate the evolutionary search, and has been proved a potential technique for complex problems. However, EDA generally spend too much time on the learning about the probability distribution of the promising individuals. The paper propose an improved EDA based on copula theory (copula-EDA) to enhance the learning efficiency, which models and samples the joint probability function by selecting a proper copula and learning the marginal probability distributions of the promising population. The simulating results prove the approach is easy to implement and is validated on several problems. ${ }^{1}$


## I. INTRODUCTION

ESTIMATION of Distribution Algorithm (EDA) has caught many researchers' eyes since proposed in 1996[1]. There are two important steps in EDAs which are explicitly modeling the probability distribution of the good solutions found so far and sampling new solutions by use of the constructed model. Many kinds of EDAs are proposed such as first order EDAs (PBIL[2], UMDA[3], $\mathrm{cGA}[4]$ ) who take the variables as independent with each other, second order EDAs (MIMIC[5], KFMIMIC[6], BMDA[7]) who only consider the relationship between pairs of variables, high order EDAs(ECGA[8], FDA[9], BOA[10]) and EDAs in continuous search spaces(PBILc[11], UMDAc[12], PPCA[13], ENGA[14]).

EDAs are extended into continuous optimization problems recently. Gaussian distribution $N(\boldsymbol{\mu}, \boldsymbol{\sigma})$ is used mainly for the estimation of the selected population in those continuous EDAs. The ways of setting parameters of Gaussian distribution are approximately the following.

[^0]1. The combination of the sample average or the sample variance [11], [13], [15], [16];
2. Linearly changing the parameters according to the distribution of the selected population [11], [17];
3. Using a constant value [11];
4. Using a self-adjust way [11], [18].

It has been proved in theory that EDAs are global converged if the population size is infinite and the constructed probability model can reflect exactly the probability distribution of the selected population, no matter which selection operator is used such as proportional selection, truncation selection or 2 -agents tournament selection [19], [20]. However, both infinite population size and exact probability model are hard to realize, especially when the optimization problem is very large. For example, the algorithms proposed in [10] and [15] need to find the optimal network, and the finding work for a given dataset is a NP-complete problem. In other words, enormous time is required for the modeling work when the optimization problem size is large.

Copula theory proposed in 1960's [21] is developed quickly until recent years. The research productions on copula theory are available mainly in statistics [21]-[23], [26] and finance [24], [25] at present, we cannot find its available results in evolutionary computations. According to copula theory, a joint probability distribution can be decomposed into $n$ marginal probability distributions and a copula function. So the marginal distributions and their dependency can be studied separately. The probability distribution of the selected population will be modeled in EDAs. Some available EDAs considered the variables are independent; others considered the relations between variables which need more time and spaces. Furthermore, the spent on learning the probability distribution increases quickly as the problem is more and more complex. It is easier to model the probability distribution of univariate compared with the joint probability distribution of multivariate. According to copula theory, the joint probability distribution of multivariate can be constructed utilizing a copula function and the marginal probability distributions of every variable. Therefore, an Estimation of Distribution Algorithms based on copula theory (copula-EDA) is proposed in this paper. This algorithm learns the probability distribution of promising population and samples agents on the ground of copula theory. This algorithm is simple and easy to realize.

The paper is organized as follows. In section II, the copula theory is introduced briefly firstly, and then the copula-EDA is produced, finally 2-D Gaussian copula-EDA is


[^0]:    Manuscript received November 16, 2008. This work was supported in part by the Youth Research Fund of Taiyuan University of Science and Technology (No.2007130), the Chinese Nature Science Fund (No. 60674104) and the Youth Research Fund of ShanXi province(No. 2006021019).
    L. F. Wang is with College of Electrical and Information Engineering, Lanzhou University of Technology, Lanzhou, 730050, China. She is now with Complex System and Computational Intelligence Laboratory, Taiyuan University of Science \& Technology, Taiyuan, 030024, China(phone: 86-0351-6962106; fax: 86-0351-6998486; e-mail: wlf1001@163.com)
    J. C. Zeng is with Complex System and Computational Intelligence Laboratory, Taiyuan University of Science \& Technology, Taiyuan, 030024, China. (e-mail: zengjianchao@263.net)
    Y. Hong is with College of Electrical and Information Engineering, Lanzhou University of Technology, Lanzhou, 730050, China. (e-mail: yudongmei@china-netcom.com)

implemented as an example. In section III, the experimental results are presented. The conclusions are provided in section IV.

## II. COPULA-EDA

## A. A brief introduction to copula theory

Researchers have not attached the importance to copula theory when it was proposed. The global economy developed quickly in recent years, and the financial risk analysis become very important. As one of the useful tools of the financial risk analysis, copula theory arouses the interest of global researchers. The copula theory is briefly introduced in the following, the details can be found in [21].

1) Definition 1: If a two-dimensional function $C:[0,1]^{2} \rightarrow[0,1]$, meet
2. $\forall t \in[0,1]$, then $C(t, 0)=C(0, t)=0$
3. $\forall t \in[0,1]$, then $C(t, 1)=C(1, t)=1$
4. $\forall u_{1}, u_{2}, v_{1}, v_{2} \in[0,1]$, and $u_{1} \leq u_{2}, v_{1} \leq v_{2}$, then $C\left(u_{2}, v_{2}\right)-C\left(u_{2}, v_{1}\right)-C\left(u_{1}, v_{2}\right)+C\left(u_{1}, v_{1}\right) \geq 0$,
the function $C$ is called two-dimensional copula or 2-copula.
5) Sklar's theorem: Let $H(x, y)$ be a joint distribution function with margins $F(x)$ and $G(y)$. Then there exists a copula $C$ such that for all $(x, y)$ in $\boldsymbol{R}$,

$$
H(x, y)=C(F(x), G(y))
$$

If $F(x)$ and $G(y)$ are continuous, then $C$ is unique; otherwise, $C$ is uniquely determined on $\operatorname{Ran} F \times \operatorname{Ran} G$. Conversely, if $C$ is a copula and $F(x)$ and $G(y)$ are distribution functions, then the function $H(x, y)$ defined by (1) is a joint distribution function with margins $F(x)$ and $G(y)$.

Sklar's theorem is the foundation of copula theory. It elucidates the role that copulas play in the relationship between multivariate distribution functions and their univariate margins[21].
3) The classes of copulas: There are two classes of copulas: ellipse copulas and Archimedean copulas. Ellipse copulas include Gauss-copula and t-copula. Archimedean copulas are produced from different generators according to the definition of Archimedean copula.

Gaussian copula: $C_{R}^{G a}$ is a Gaussian copula if the random vector $(X, Y)$ meets the following conditions:

1. The marginal distributions $u$ and $v$ obey Gaussian distribution;
2. The copula to connect the marginal distributions is also normal, i.e.

$$
C_{R}^{G a}(u, v)=\phi_{R}\left(\phi^{-1}(u), \phi^{-1}(v)\right)
$$

Where, $\phi_{R}$ is a multivariate standardized normal distribution whose correlation matrix is $\boldsymbol{R}$, its inverse
function is $\phi^{-1}$.
t-copula Random vector $(X, Y)$ obeys t-distribution whose freedom is $\gamma$, and the marginal distribution of each random variable is $u$ and $v$ separately, $C_{\gamma, R}^{j}$ is a t-copula if

$$
C_{\gamma, R}^{j}(u, v)=t_{\gamma, R}^{n}\left(t_{\gamma}^{-1}(u), t_{\gamma}^{-1}(v)\right)
$$

where, $t_{\gamma}^{-1}$ denotes the inverse function of univariate standard t-distribution whose freedom is $\gamma, t_{\gamma, R}^{n}$ denotes n-dimensional standard t-distribution whose freedom is $\gamma$ and linear correlation matrix is $\boldsymbol{R}$.

Archimedean copulas: Copulas of the form

$$
C(u, v)=\phi^{(-1)}(\phi(u)+\phi(v))
$$

are called Archimedean copulas, where, $\phi$ is a continuous, strictly decreasing function from $[0,1]$ to $[0, \infty]$ such that $\phi(1)=0$, and $\phi^{(-1)}$ is the pseudo-inverse of $\phi$ defined by

$$
\phi^{(-1)}(t)=\left\{\begin{array}{cc}
\phi^{-1}(t) & 0 \leq t \leq \phi(0) \\
0 & \phi(0) \leq t<\infty
\end{array}\right.
$$

The function $\phi$ is called a generator of the copula.

## B. The frame of copula-EDA

Sklar's theorem plays an important role in copula theory. It is got from Sklar's theorem that copula correlates the marginal distribution functions and the joint distribution function. If the marginal distribution functions and a copula are available, then the joint distribution function is easy to construct. In EDAs, the distribution of promising population must be estimated in every generation. In the light of copula theory, only the marginal distributions are needed to be estimated. The joint distribution function can be constructed by the marginal distribution functions and a well-selected copula. The next generation can be sampled using the joint distribution function.

Suppose that the optimization problem is

$$
\min f(X)=f\left(x_{1}, x_{2}, \ldots x_{n}\right), \quad x_{i} \in\left[a_{i}, b_{i}\right] \quad(i=1,2, \ldots n)
$$

Denote the promising population with size $s$ as $\mathbf{x} \triangleq\left\{x^{\prime}=\left(x_{1}^{\prime}, x_{2}^{\prime}, \ldots, x_{n}^{\prime}\right), i=1,2, \ldots, s\right)\}$, then $\mathbf{x}$ is the $s$ observed values of random vector $\left(X_{1}, X_{2}, \ldots, X_{n}\right)$. The marginal distribution of each random variable $X_{i}(i=1,2, \ldots n)$ can be Gaussian distribution, t-distribution or some others. On the ground of Sklar's theorem, the joint distribution function can be constructed with a selected copula and the marginal distributions. The modeling of the distribution of the selected population is finished.

Next step is to generate new population by Monte Carlo method [21], [25]. The definition of quasi-inverse is introduced firstly.

Definition 2 [21]: Let $F$ be a distribution function. Then a quasi-inverse of $F$ is any function $F^{(-1)}$ with domain $[0,1]$ such that

1. If $t$ is in Ran $F$, then $F^{(-1)}(t)$ is any number $x$ in $\boldsymbol{R}$

such that $F(x) \quad t$, i.e., for all $t$ in RanF, $F\left(F^{(1)}(t)\right) \quad t$
2. If $t$ is not in RanF, then

$$
F^{(1)}(t) \quad \inf \{x \mid F(x) \quad t\} \quad \sup \{x \mid F(x) \quad t\}
$$

2-copula is considered in the following, in other words, the random samples of two-dimensional random vector $\left(X_{1}, X_{2}\right)$ will be produced. Given that the marginal distribution functions are $u \quad F\left(x_{1}\right)$ and $v \quad G\left(x_{2}\right)$, obviously $u \sim U[0,1]$ and $v \sim U[0,1]$, then the random vector sequences can be sampled from $u$ and $v$. According to the properties of copulas, the condition distribution function $C_{u}(v) \quad \partial C(u, v) / \partial u$ is monotony non-decreasing in $v[0,1]$ when $u[0,1]$ is given. Denote $\omega \quad C_{u}(v) \quad \partial C(u, v) / \partial u$, then $\omega$ is uniform in interval $[0,1]$. Thus, generate $u$ and $\omega$ by Monte Carlo method in interval $[0,1]$ firstly. And then get $v \quad C_{u}^{(1)}(\omega)$ from the quasi-inverse function of $C_{u}(v)$. Finally, from $x_{1} \quad F^{(1)}(u)$ and $x_{2} \quad G^{(1)}(v)$, the random vector $\left(x_{1}, x_{2}\right)$ is obtained. The pseudo code of the generating process is showed in Fig. 1.

$$
\begin{aligned}
& \text { generation }(C ; F, G) \\
& \text { - Generate two independent uniform }(0,1) \text { variates } u \text { and } \\
& \omega ; \\
& \text {-Set } v \quad C_{u}^{(1)}(\omega) \text {, where } C_{u}^{(1)} \text { denotes a quasi-inverse } \\
& \text { of } C_{u} \text {; } \\
& \text {-set } x_{1} \quad F^{(1)}(u) \text { and } x_{2} \quad G^{(1)}(v) \text {; } \\
& \text {-The desired pair is }\left(x_{1}, x_{2}\right) \text {. } \\
& 1
\end{aligned}
$$

Fig. 1. The pseudo code of generating an agent

## C. Two dimensional Gaussian copula-EDA

A two-dimensional optimization problem is considered. Accordind to copula theory, the marginal distribution of each variable and a copula are required. The marginal distributions of $X_{1}, X_{2}$ ) is easy to estimate because the observed values are given. The only thing is to evaluate sample mean and sample variance. 2-D Gauss-copula is selected which is

$$
C(u, v ; \rho) \quad{ }_{\rho}\left({ }^{1}(u), \quad{ }^{1}(v)\right), u, v \quad[0,1]
$$

where, ${ }_{\rho}$ is a binary standard Gaussian distribution with correlation coefficient $\rho$. Determining $\rho$ is the key to construct copula.

If the Maximum Likelihood Estimation is used, then the logarithm likelihood function is

$$
\begin{aligned}
& l(\rho) \sum_{i=1}^{n} \frac{1}{2} \ln 2 \pi \frac{1}{2} \ln \left(1 \quad \rho^{2}\right) \frac{z_{x_{i}}^{2} \quad z_{y_{i}}^{2} \quad \frac{2 \rho z_{1 i} z_{2 i}}{2\left(1 \quad \rho^{2}\right)} \\
& \sum_{i=1}^{n}\left[\ln f\left(x_{i}^{1}\right) \quad \ln g\left(x_{i}^{2}\right)\right]
\end{aligned}
$$

where,

$$
z_{1 i} \quad{ }^{1}\left(F\left(x_{i}^{1}\right)\right), z_{2 i} \quad{ }^{1}\left(G\left(x_{i}^{2}\right)\right)
$$

If Moment Estimation is used, then

$$
\hat{\rho} \frac{\frac{1}{2} \sum_{i=1}^{n} x_{i}^{2} x_{i}^{3} \quad \hat{X}_{i} \hat{X}_{2}}{\hat{S_{x_{i}}^{2}} \hat{S_{x_{i}}^{2}}}
$$

where,

$$
\hat{X}_{i} \quad \frac{1}{s} \sum_{i=1}^{n} x_{i}^{2} \quad \hat{S_{x_{i}}^{2}} \sqrt{\frac{1}{s} \sum_{i=1}^{s}\left(x_{i}^{1}\right)^{2}},(\text { k } 1,2)
$$

Next, sampling from the distribution function is discussed. Since

$$
\begin{aligned}
& C(u, v ; \rho) \\
& { }_{\rho}\left({ }^{1}(u), \quad{ }^{1}(v)\right) \\
& \int^{\alpha} \int^{\alpha} \frac{1}{2 \pi \sqrt{1} \rho^{2}} \\
& \exp \left[\frac{\left[{ }^{1}(s)\right]^{2} \quad\left[^{1}(t)\right]^{2}}{2\left(1 \quad \rho^{2}\right)} \frac{2 \rho}{ \rho^{2}}\right] d t d s
\end{aligned}
$$

then

$$
\begin{aligned}
& \omega \quad C_{u}(v) \\
& \quad \partial C(u, v) / \partial u \\
& \quad e^{\left[\frac{{ }^{1}(u)\right]^{2}}{2}} \int^{\alpha} \frac{1}{2 \pi \sqrt{1} \rho^{2}} \exp \left[\frac{\left[{ }^{1}(t) \rho \quad{ }^{1}(u)\right]^{2}}{2\left(1 \quad \rho^{2}\right)}\right] d t
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& v \quad \sqrt{1 \quad \rho^{2}} \quad{ }^{1}\left(e^{\left[\frac{{ }^{1}(u)\right]^{2}}{2}} \omega\right) \quad \rho \quad{ }^{1}(u) \\
& \sqrt{1 \quad \rho^{2}} \quad{ }^{1}\left(\omega^{1}\right) \quad \rho \quad{ }^{1}(u)
\end{aligned}
$$

So randomly generate vector $\left(u, \omega^{1}\right) \sim U[0,1]^{2}$, and then the other random number $v$ was calculated by using (9). The vector $\left(x_{1}, x_{2}\right)$ can be calculated by using (10).

$$
\begin{array}{llllll}
x_{1} & \hat{\sigma}_{1} & { }^{1}(u) & \hat{\mu}_{1}, x_{2} & \hat{\sigma}_{2} & { }^{1}(v) & \hat{\mu}_{2}
\end{array}
$$

where,
$\hat{\mu}_{k} \quad \hat{X}_{k}, \hat{\sigma}_{k} \quad S_{x_{k}}^{x},(k \quad 1,2)$.
Conclusively, the process for implementing 2-D copula-EDA is as follows:

Step 1: Initialize (pop, $N$ ). Randomly generate initial population pop with size $N$. set generation count $g \leftarrow 0$.

Step 2: Selection (pop, spop, select-rate). Select the best select-rate $N$ agents form pop to spop according to the agents' fitness.

Step 3: copula-generator (pop, spop, mutate-rate).
S3.1: Construct the distribution model of spop:

1. calculate the sample average and the sample variance for each variable according to (6), then the marginal

distributions are $F \quad N\left(X_{1}, S_{x_{i}}^{\prime}\right)$ and $G \quad N\left(X_{2}, S_{x_{i}}^{\prime}\right)$;
2. calculate the estimation value of parameter according to (3) or (5), then the copula $C$ is the same as (7);

S3.2: Generate a new population by iterative using proceed generation( $C, F, G)$, where

$$
v \quad C_{S}^{i-1}(\quad) \sqrt{1^{2}} \quad{ }^{1}(\quad)^{1}(u)
$$

S3.3: randomly generate some agents by the rate mutate-rate.

Step 4: Stop if the termination criteria is met.
Step 5: Set $g \quad g \quad 1$ and go to Step 2.

## III. VALIDATION

The following 9 test functions are used to show the behavior of the proposed algorithm. The test functions $F_{1} \sim F_{3}$ and $F_{8} \sim F_{8}$ are also used in [11].

$$
F_{1}(x) \quad \frac{100}{10^{5} \quad\left|y_{i}\right|}
$$

where $y_{1} \quad x_{1}, y_{i} \quad x_{i} \quad y_{i}(i 2), x_{i}[3,3]$, the optimal result is $F_{i} *(0,0, \ldots 0) \quad 10^{7}$.

$$
F_{2}(x) \quad \frac{100}{10^{5} \quad\left|y_{i}\right|}
$$

Where $y_{1} \quad x_{1}, y_{i} \quad x_{i} \quad \sin y_{i}(i 2), x_{i}[3,3]$, the optimal result is $F_{2} *(0,0, \ldots 0) \quad 10^{7}$

$$
F_{3}(x) \quad \frac{100}{10^{5} \quad\left|y_{i}\right|}
$$

where $y_{i} \quad 0.024 \times(i 1) \quad x_{i}, x_{i}[3,3]$, the optimal result is $F_{3} *(0.024 \times 2, \ldots, 0.024 \times(n 1)) \quad 10^{7}$
$F_{4}(x) \quad x_{i}^{2}$, where $x_{i}[500,500]$, the optimal result is $F_{4} *(0,0, \ldots 0) \quad 0$
$F_{5}(x) \quad 1 \quad{ }_{1}\left(\sin x_{i}\right)^{2} \quad 0.1 \exp \left({ }_{1} x_{i}^{2}\right)$, where $x_{i}[10,10]$, the optimal result is $F_{5} *(0,0, \ldots 0) \quad 0.9$
$F_{6}(x) \quad{ }_{1}\left(x_{i}^{2} \quad A \cos \left(2 x_{i}\right)\right) \quad A$ ), where $x_{i}[5,5]$, the optimal result is $F_{6} *(0,0, \ldots 0) \quad 0$
$F_{7}(x) \quad{ }_{1}\left(418.9829 \quad x_{i} \sin \sqrt{\left|x_{i}\right|}\right)$,
where $x_{i}[500,500]$, the optimal result is $F_{7} *(-420.9687, \ldots,-420.9687) \quad 0$

$$
F_{8}(x) \quad x_{i}^{2} \quad \prod_{1} \cos \left(\frac{x_{i}}{\sqrt{i}} \frac{x_{i}}{1}\right)
$$

where $x_{i}[100,100]$, the optimal result is $F_{8} *(0,0, \ldots 0) \quad 1$

$$
\begin{aligned}
& F_{9}(x) \quad[1 \\
& \left(x_{1} \quad x_{2} \quad 1\right)^{2}\left(19 \quad 14 x_{1} \quad 3 x_{1}^{2} \quad 14 x_{2} \quad 6 x_{1} x_{2} \quad 3 x_{2}{ }^{2}\right)\} \\
& \times[30 \\
& \left(2 x_{1} \quad 3 x_{2}\right)^{2}\left(18 \quad 32 x_{1} \quad 12 x_{1}^{2} \quad 48 x_{2} \quad 36 x_{1} x_{2} \quad 27 x_{2}{ }^{2}\right)\}
\end{aligned}
$$

$\times[30$
$\left(2 x_{1} \quad 3 x_{2}\right)^{2}\left(18 \quad 32 x_{1} \quad 12 x_{1}^{2} \quad 48 x_{2} \quad 36 x_{1} x_{2} \quad 27 x_{2}{ }^{2}\right)\}$
where $x_{1}, x_{2}[2,2]$, the optimal result is $F_{9} *(0,1) \quad 3$

TABLE I
THE CONVERGENCE OF COPULA-EDA AND PBILC, THE MAXIMAL GENERATION IS 1000

|  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  |  |  |  |
| $F_{1}$ | cEDA | 500 | 0.2 | 0.05 | $10^{d}$ | 50:50 | 50.700 |
|  | PBILc | 500 | 0.2 | 0 | $10^{d}$ | 50:50 | 405.660 |
| $F_{2}$ | cEDA | 500 | 0.2 | 0.05 | $10^{d}$ | 46:50 | 43.369 |
|  | PBILc | 500 | 0.2 | 0 | $10^{d}$ | 50:50 | 421.120 |
| $F_{3}$ | cEDA | 500 | 0.2 | 0.05 | $10^{d}$ | 50:50 | 17.600 |
|  | PBILc | 500 | 0.2 | 0 | $10^{d}$ | 50:50 | 396.420 |
| $F_{4}$ | cEDA | 100 | 0.2 | 0.05 | $10^{d}$ | 50:50 | 28.791 |
|  | PBILc | 100 | 0.2 | 0 | $10^{d}$ | 50:50 | 841.400 |
| $F_{5}$ | cEDA | 100 | 0.2 | 0.05 | $10^{d}$ | 50:50 | 222.760 |
|  | PBILc | 100 | 0.2 | 0 | $10^{d}$ | 50:50 | 560.860 |
| $F_{6}$ | cEDA | 100 | 0.2 | 0.05 | $10^{d}$ | 50:50 | 76.800 |
|  | PBILc | 100 | 0.2 | 0 | $10^{d}$ | 50:50 | 493.600 |
| $F_{7}$ | cEDA | 100 | 0.2 | 0.05 | $10^{d}$ | 44:50 | 69.386 |
|  | PBILc | 100 | 0.2 | 0 | $10^{d}$ | 32:50 | 905.593 |
| $F_{8}$ | cEDA | 100 | 0.2 | 0.05 | $10^{d}$ | 50:50 | 25.250 |
|  | PBILc | 100 | 0.2 | 0 | $10^{d}$ | 50:50 | 664.300 |
| $F_{9}$ | cEDA | 100 | 0.2 | 0.05 | $10^{d}$ | 50:50 | 21.306 |
|  | PBILc | 100 | 0.2 | 0 | $10^{d}$ | 41:50 | 644.195 |

TABLE II
THE STATICS OF DIFFERENT ALGORITHM AFTER 50 RUNS

|  | copula_EDA | PBILc | PBILcM |
| :--: | :--: | :--: | :--: |
|  | Mean $\pm$ Std | Mean $\pm$ Std | Mean $\pm$ Std |
| $F_{1}$ | $-9.7229 \mathrm{e}+006 \pm$ | $-9.9473 \mathrm{e}+006 \pm$ | $-4.4996 \mathrm{e}+005 \pm$ |
|  | $1.5966 \mathrm{e}+004$ | $3.1487 \mathrm{e}+004$ | $4.4091 \mathrm{e}+005$ |
| $F_{2}$ | $-9.4549 \mathrm{e}+006 \pm$ | $-9.9403 \mathrm{e}+006 \pm$ | $-3.8927 \mathrm{e}+005 \pm$ |
|  | $1.3826 \mathrm{e}+003$ | $3.1134 \mathrm{e}+004$ | $3.7505 \mathrm{e}+005$ |
| $F_{3}$ | $-9.8119 \mathrm{e}+006 \pm$ | $-9.9519 \mathrm{e}+006 \pm$ | $-9.4466 \mathrm{e}+004 \pm$ |
|  | $1.1698 \mathrm{e}+003$ | $2.0524 \mathrm{e}+004$ | $6.6105 \mathrm{e}+004$ |
| $F_{4}$ | $3.6721 \mathrm{e}-012 \pm$ | $7.8393 \mathrm{e}-012 \pm$ | $0.2069 \pm$ |
|  | $2.6923 \mathrm{e}-012$ | $8.4951 \mathrm{e}-012$ | 0.8377 |
| $F_{5}$ | $0.9000 \pm$ | $0.9000 \pm$ | $0.9000 \pm$ |
|  | $3.0600 \mathrm{e}-011$ | $3.3826 \mathrm{e}-014$ | $2.0910 \mathrm{e}-005$ |
| $F_{6}$ | $8.3590 \mathrm{e}-014 \pm$ | $2.2464 \mathrm{e}-012 \pm$ | $5.8463 \mathrm{e}-004 \pm$ |
|  | $5.7045 \mathrm{e}-014$ | $2.6022 \mathrm{e}-012$ | $6.0017 \mathrm{e}-004$ |
| $F_{7}$ | $0.1596 \pm$ | $35.1368 \pm$ | $0.3105 \pm$ |
|  | 0.7787 | 58.5155 | 0.2903 |
| $F_{8}$ | $-1.0000 \pm$ | $-1.0000 \pm$ | $-0.9907 \pm$ |
|  | $4.4546 \mathrm{e}-014$ | $3.6992 \mathrm{e}-013$ | 0.0388 |
| $F_{9}$ | $3.0000 \pm$ | $7.8600 \pm$ | $3.0116 \pm$ |
|  | $9.9700 \mathrm{e}-009$ | 10.4784 | 0.0206 |

![img-0.jpeg](img-0.jpeg)

Fig. 2. The performance on test function $F_{t}$
![img-1.jpeg](img-1.jpeg)

Fig. 3. The performance on test function $F_{2}$
![img-2.jpeg](img-2.jpeg)

Fig. 4. The performance on test function $F_{3}$
![img-3.jpeg](img-3.jpeg)

Fig. 5. The performance on test function $F_{4}$
![img-4.jpeg](img-4.jpeg)

Fig. 6. The performance on test function $F_{5}$
![img-5.jpeg](img-5.jpeg)

Fig. 7. The performance on test function $F_{6}$

![img-6.jpeg](img-6.jpeg)

Fig. 8. The performance on test function $F_{7}$
![img-7.jpeg](img-7.jpeg)

Fig. 9. The performance on test function $F_{8}$
![img-8.jpeg](img-8.jpeg)

Fig. 10. The performance on test function $F_{9}$
All test functions are optimized in 2-dimensional spaces, the maximal generation $g$ is set to 1000 . The search terminates if the distance between the best solution found so far and the optimum is less than the predefined precision. Table I and Table II display the experimental results.
copula-EDA is abbreviated to cEDA in Table I and Fig. 2 - Fig.10. PBILcM is performed based on PBILc with the mutation rate as 0.05 for the sake of comparing the performance of copula-EDA and PBILc with the same
parameters. But the experimental results show that the convergence rate of PBILcM is 0 in each function with the parameters in Table I. The convergence rate and the convergence generations are the average results of 50 runs. The experimental results show that copula-EDA converges to the global optimum quickly in the test functions.

The mean fitness and the standard variance of each algorithm after 50 runs are showed in Table II. Obviously, copula-EDA performs better than the other two algorithms. It is found through further experiments that Copula-EDA converges faster than PBILc, but it needs more agents in the population than PBILc.

The evolution processes of the above three algorithms is compared begin with the same population in Fig. 2 - Fig. 10. The population in the first generation is same for each algorithm. Error in Fig. 2 - Fig. 10 is the fitness difference. Copula-EDA converges to the best solution quickly in almost all tested functions especially for the function $F_{3}-F_{3}$ whose variables are strongly correlative with each other. It is also can be seen from the figure of $F_{5}, F_{6}$ and $F_{7}$ that copula-EDA is premature in some cases.

## IV. CONCLUSION

Copula theory provides a good basis for studying multivariate distribution functions. The marginal distributions and the dependence between variables can be researched separately which make the operation easier. Copula-EDA constructs the distribution model based on copula theory. The constructed model reflects the distribution of promising population well, and the computation cost is less than PPCA or BOA. Moreover, different joint distribution functions can be made by selecting different copulas if the marginal distribution functions are given. The experimental results validate this algorithm. The next targets to study is extending this algorithm to high dimensional optimization problems and keeping the algorithm away from prematurity.

## REFERENCES

[1] P. Larranaga, and J. A. Lozano, Estimation of Distribution Algorithms. A New Tool for Evolutionary Computation. Boston: Kluwer Academic Publishers, 2002.
[2] S. Baluja, "Population-Based Incremental Learning: A Method for Integrating Genetic Search Based Function Optimization and Competitive Learning," Technical Rep. CMU-CS-94-163, Pittsburgh, PA: Carnegie Mellon University, 1994.
[3] H. Muhlenbein, and G.Paass, "From recombination of genes to the estimation of distributions I. Binary Parameters," in Proc. PPSN IV, Berlin, 1996, pp. 178-187.
[4] G. R. Harik, F. G. Lobo, and D. E. Goldberg, "The compact genetic algorithm," in Proc. IEEE Conf. Evolutionary Computation., Indianapolis, USA, 1998. pp. 523-528.
[5] J. S. De Bonet, C. L. Isbell , P. Viola, "MIMIC: Finding optima by estimation probability densities," Advances in Neural Information Processing Systems, Cambridge: MIT Press, 1997, pp. 424-430.
[6] W. Zhong, J.Liu, F.Liu, and L. Jiao, "Second order estimation of distribution algorithms based on kalman filter," Chinese Journal of Computers, vol. 27, no. 9, pp. 1272-1277, Sept. 2004. (in Chinese)

[7] M. Pelican, and H.Muhlenbein, "The bivariate marginal distribution algorithm," Advances in Soft Computing-Engineering Design and Manufacturing, London, Springer-Verlag, 1999, pp. 521-535.
[8] G.Harik, "Linkage Learning via Probabilistic Modeling in the ECGA," Illigal Rep. No.99010, Illinois Genetic Algorithms Lab., University of Illinois, Urbana-Champaign, Illinois, 1999.
[9] H. Muhlenbein, and T.Mahnig, "FDA- a scalable evolutionary algorithm for the optimization of additively decomposed functions," Evolutionary Computation, vol. 7, no. 4, pp. 353-376, Winter 1999.
[10] M, Pelikan, D. E. Goldberg, and E.Cantu-Paz, "BOA: the Bayesian optimization algorithm," in Proc. Genetic and Evolutionary Computation Conference (GECCO-99), Orlando, FL, 1999, pp. 525-532.
[11] M. Sebag, and A. Ducoulombier, "Extending population-based incremental learning to continuous search spaces," in Proc. PPSN V, Amsterdam, 1998, pp. 418-427.
[12] P. Larranaga, R. Etxeberria, J. A. Lozano, and J. M. Pena, "Optimization in continuous domains by learning and simulation of Gaussian networks," in Proc. 2000 Genetic and Evolutionary Computation Conf. Workshop Program, Las Vegas, Nevada, 2000, pp. 201-204.
[13] D. Y. Cho, and B T. Zhang, "Continuous estimation of distribution algorithms with probabilistic principal component analysis," in Proc. IEEE Conf. Evolutionary Computation, Seoul, Korea, 2001, pp. 521-526.
[14] P. Larranga, R. Etxeberria, J. A. Lozano, and J. M. Pena. "Optimization by Learning and Simulation of Bayesian and Gaussian Networks," Technical Rep. EHU-KZAA-IK-4/99, University of the Basque Country, Spain, 1999.
[15] P. Larranaga, R. Etxeberria, J. A. Lozano, and J. M. Pena, "Optimization in Continuous Domains by Learning and Simulation of Gaussian Networks," in Proc. GECCO-2000, San Francisco, USA, 2001, pp. 201-204.
[16] P. Bosman, D. Thierens. (2008, December 1). IDEAs based on the normal kernels probability density function. [Online]. Available: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.36.1984.
[17] M. Gallagher, and M. Frean, "Population-based continuous optimization, probabilistic modelling and mean shift," Evolutionary Computation, vol. 13, no. 1, pp. 29-42, Spring 2005.
[18] J. Ocenasek, S. Kern, N. Hansen, S. Muller, and P. Koumoutsakos. "A Mixed Bayesian Optimization Algorithm with Variance Adaptation," in Proc. PPSN VIII, Birmingham, UK, 2004, pp. 352 - 361.
[19] Q. Zhang, and H.Muhlenbein, "On the convergence of a class of estimation of distribution algorithms," IEEE Trans. Evolutionary Computation, vol. 8, no.2, pp. 127-136, Apr. 2004.
[20] Q. Zhang. (2008, October 1). On the convergence of a factorized distribution algorithm with truncation selection. [Online]. Available: http://cswww.essex.ac.uk/staff/zhang/EDAWEB/.
[21] R. B.Nelsen, An Introduction to copula. Springer-Verlag, New York, 1998.
[22] J. Wu, C. Liu, and X. Qiu, "Dependence measure based on copula theory," Journal of Shanxi University(Nat. Sci. Ed.) , vol. 31, no. 3, pp. 299-302, 2008. in Chinese)
[23] D. Shi, and Q. Yao, "A method of improving copula fitted to data," System Engineering - Theory \& Practice, no.4, pp. 49-54, Apr. 2004. (in Chinese)
[24] Y. Zhang, "copula technique and financial risk analysis," Statistical Research, no.4, pp. 48-51, Apr. 2004. in Chinese)
[25] M. Bai, L. Sun, "The comparison between three copula-VaR approaches and traditional VaR methods," The Journal of Quantitative \& Technical Economics, no. 2 pp. 154-160, Feb. 2007. (in Chinese)
[26] S. Demarta, and A. J. McNeil. (2008, October 1). The t copula and Related copulas [Online]. Available: http://www.math.ethz.ch/ mcneil/ftp/tcopula.pdf.