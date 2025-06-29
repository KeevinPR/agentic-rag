# Estimation of Distribution Algorithm Based on Copula Theory 

Li-Fang Wang and Jian-Chao Zeng


#### Abstract

Estimation of Distribution Algorithms (EDAs) is the hot topic of evolutionary computation currently. EDAs model the selected population using a distribution model, which is latter sampled to generate the population for the next generation. This chapter introduces a new way to estimate the distribution model and sample from it according to copula theory. The multivariate joint is decomposed into the univariate margins and a function called copula. In the EDAs based on copula theory (copula-EDAs), only the margins are estimated, and the next generation is sampled from the copula and the inverse function of the margins. The framework of the copula-EDAs is discussed in the chapter. Two 2-dimensional copula-EDAs and a high-dimensional copula-EDA are described in detail as the examples.


## 1 Introduction

Estimation of Distribution Algorithms (EDAs) are originated from Genetic Algorithms (GAs) [1]. While GAs generate a new population using crossover and mutation operators, EDAs estimate a distribution model of the selected population and sample from the estimated model. The comparison of the two algorithms is shown as Fig. 1.

As an example, the integer minimization problem $f(x)=x^{2}, x \in[0,15]$ is optimized with a kind of EDA. The value of $x$ is denoted as 4 -bit binary number, i.e. 5 is denoted as 0101,8 is denoted as 1000 . According to the flow chat of EDAs, the first step is to generate some random integers in $[0,15]$. Supposing, the following 5 binary numbers are generated. Their fitness are listed followed the numbers.

Li-Fang Wang $\cdot$ Jian-Chao Zeng Complex System and Computational Intelligence Laboratory, Taiyuan University of Science and Technology, China P.R. e-mail: wlf1001@163.com

Secondly, a promising population is selected according to the individual's fitness. If the truncation selection is used and the selection rate is 0.6 , then the $3^{\text {rd }}-5^{\text {th }}$ individuals are selected as the promising population.

Thirdly, the distribution model of the selected population is estimated. Denote $p_{i}$ as the probability of the $i^{\text {th }}$ bit being 1 . Thus the probability of each bit is the following: $p_{1}=0, p_{2}=2 / 3, p_{3}=1 / 3, p_{4}=2 / 3$.

Fourthly, the next generation is sampled according to the estimated model. The following individuals are generated supposing.

The loop is continued by going to the second step until the termination condition is met.
![img-0.jpeg](img-0.jpeg)

Fig. 1 The different flowchart of EDAs and GAs
Different kinds of EDAs have been developed since the idea of EDA is introduced in 1994 [1,2].

The early EDAs regard the relationship of the random variables as independent. PBIL(Population Based Incremental Learning) [2-5], UMDA(Unirvariate Marginal Distribution Algorithm) [6-8] and cGA(compact Genetic Algorithm) [9] are all the classical algorithms.

However, in practical problems variables of the optimization problems are not independent. Some algorithms consider the linear relationship of variables. The random variables are numbered according to a certain rule, and the random variable depends only on the previous random variable. The classical algorithms of this type include MIMIC(Mutual Information Maximization of Input Clustering) [10], COMIT(Combining Optimizers with Mutual Information Trees) [11] and BMDA(Binary Marginal Distribution Algorithm) [12,13].

Many EDAs considering the multivariate dependence are proposed in the last decade. For example, ECGA(Extended Compact Genetic Algorithm) [14], FDA(Factorized Distribution Algorithms) [15-19] and BOA(Bayesian Optimization Algorithm) [20-25].

Continuous EDAs were developed later than discrete EDAs. The classical algorithms include PBILc [26], UMDAc [27], SHCLVND(Stochastic Hill Climbing with Learning by Vectors of Normal Distributions) [28], EMNA(Estimation of Multivariate Normal Algorithm)[29], ENGA(Estimation of Gaussian Networks Algorithm) [30], IDEA [31], etc. The Gaussian distribution is used in most of these algorithms.

PBILc and UMDAc are extended from PBIL and UMDA respectively to the continuous form, and the Gaussian distributions are used in both of the two algorithms. The Gaussian distribution is also used in SHCLVND and the parameter mean is adjusted by Hebbian Learning.

The multivariate Gaussian distribution is used to estimate the distribution of the population in EMNA. The parameters mean and the covariance matrix are estimated by EML. The next generation is sampled from the joint distribution. It is a problem in EMNA that the runtime to estimate the covariance matrix increased exponentially if the number of random variables has increased.

EGNA is an algorithm based on the Gaussian network. The directed edges represent the relationship of the random variables and the distribution of each random variable is described with the Gaussian distribution. The Gaussian network is adjusted according to the current selected population.

IDEA is a kind of EDA based on the hybrid Gaussian distribution and the Gaussian kernel function. The shortage of EMNA and EGNA is conquered in IDEA. But the relationship of random variables is not reflected thoroughly in IDEA.

The chapter describes how copula theory can be used in an Estimation of Distribution Algorithm. The benefit of the copula approach is that only marginal distributions need to be estimated from the population of solutions, thus promising efficiency savings.

The remaining sections are organized as follows. Section 2 talks about the basic theorem and properties in copula theory. Section 3 explains why copula theory could be used in EDA and then gives the framework of copula-EDAs. Section 4 and section 5 illustrate the copula EDAs with two 2-dimensional algorithms and one high-dimensional algorithm respectively. Finally, section 6 concludes the paper, summarizing the main results and pointing further directions.

# 2 A Brief Introduction to Copula Theory 

Copula theory [32] is one of the hot topics in statistics. Its main idea is how to decompose the multivariate joint distribution into the univariate marginal distributions. A kind of function called copula ties the joint and the margins together. Thus the difficult work to estimate the joint distribution could be replaced by estimating the margins and constructing a copula. It also draws many scholars' attention to sample from copula. These are the two key steps in EDAs, i.e., to construct a distribution model to represent the selected population and to sample the constructed model, creating the next generation. The distribution of the population is reflected precisely and the runtime is shortened if the copula theory is introduced into the framework of EDAs. Copula theory is briefly introduced in the following section.

### 2.1 Definitions and Basic Properties

The definition of copula and the basic theorem are listed in this section. The symbol $\mathbf{I}$ denotes the domain $[0,1]$ in this chapter. The definitions and theorems are quoted from [32].

Definition 1. A two-dimensional subcopula (or 2-subcopula, or briefly, a subcopula) is a function $C^{\prime}$ with the following properties:

1) $\operatorname{Dom} C^{\prime}=S_{1} \times S_{2}$, where $S_{1}$ and $S_{2}$ are subsets of $\mathbf{I}$ containing 0 and 1 ;
2) $C^{\prime}$ is grounded and 2-increasing;
3) For every $u$ in $S_{1}$ and every $v$ in $S_{2}$,

$$
C^{\prime}(u, 1)=u \text { and } C^{\prime}(1, v)=v
$$

Definition 2. A two-dimensional copula( or 2-copula, or briefly, a copula) is a 2 -subcopula $C$ whose domain is $\mathbf{I}^{2}$.

Equivalently, a copula is function $C$ from $\mathbf{I}^{2}$ to $\mathbf{I}$ with the following properties:

1) For every $u, v$ in $\mathbf{I}$,

$$
C(u, 0)=0=C(0, v)
$$

and

$$
C(u, 1)=u \text { and } C(1, v)=v
$$

2) For every $u_{1}, u_{2}, v_{1}, v_{2}$ in $\mathbf{I}$ such that $u_{1} \leq u_{2}$ and $v_{1} \leq v_{2}$,

$$
C\left(u_{2}, v_{2}\right)-C\left(u_{2}, v_{1}\right)-C\left(u_{1}, v_{2}\right)+C\left(u_{1}, v_{1}\right) \geq 0
$$

The definition of $n$-copula is extended from the above definitions.
Definition 3. An n-copula is a function $C$ from $\boldsymbol{I}^{n}$ to $\boldsymbol{I}$ with the following properties:

1) For every $\boldsymbol{u}$ in $\boldsymbol{I}^{n}$,

$$
C(\boldsymbol{u})=0 \text { if at least one coordinate of } \boldsymbol{u} \text { is } 0
$$

and

$$
\text { if all coordinates of } \boldsymbol{u} \text { are } 1 \text { except } u_{k} \text {, then } C(\boldsymbol{u})=u_{k}
$$

2) For every $\boldsymbol{u}$ and $\boldsymbol{v}$ in $\boldsymbol{I}^{n}$ such that $\boldsymbol{u} \leq \boldsymbol{v}$, denote

$$
V_{C}\left([\boldsymbol{u}, \boldsymbol{v}]\right)=\sum_{\varepsilon 1, \ldots, \varepsilon n \in[0,1]}(-1)^{(\varepsilon 1 \times \ldots+\varepsilon n)} C\left(\left(\varepsilon_{1} u_{1}+\left(1-\varepsilon_{1}\right) v_{1}\right)+\ldots+\left(\varepsilon_{n} u_{n}+\left(1-\varepsilon_{n}\right) v_{n}\right)\right)
$$

then

$$
V_{C}([\boldsymbol{u}, \boldsymbol{v}]) \geq 0
$$

It can be derived from the definition of copula that the condition of copula is very easy to be satisfied. So many functions can be used as copulas. The copulas are divided into two classes that are elliptical copulas and Archimedean copulas. For example, normal copula and t-copula are all elliptical copulas. Archimedean copulas are generated from different generators such as Clayton copula, Gumbel copula and others. Each Archimedean copula has one or more parameters. More details see [32].

Sklar's theorem plays an important role in copula theory. It gives the theory basis to connect the multivariate distribution with one-dimensional marginal distribution.

Sklar's Theorem in $\boldsymbol{n}$-dimensions: Let $H$ be an $n$-dimensional distribution function with margins $F_{1}, F_{2}, \ldots, F_{n}$. Then there exists an $n$-copula $C$ such that for all $\boldsymbol{x}$ in $\boldsymbol{R}^{n}$,

$$
H\left(x_{1}, \ldots, x_{n}\right)=C\left(F_{1}\left(x_{1}\right), \ldots, F_{n}\left(x_{n}\right)\right)
$$

If $F_{1}, F_{2}, \ldots, F_{n}$ are all continuous, then $C$ is unique; otherwise, $C$ is uniquely determined on $\operatorname{Ran} F_{1} \times \ldots \times \operatorname{Ran} F_{n}$. Conversely, if $C$ is an n-copula and $F_{1}, F_{2}, \ldots, F_{n}$ are distribution functions, then the function $H$ defined by (8) is an n-dimensional distribution function with margins $F_{1}, F_{2}, \ldots, F_{n}$.

According to Sklar's theorem, the joint distribution of a random vector could be constructed by the one-dimensional distribution of each random variable through a copula. Therefore, the hard work to estimate the joint distribution is simplified to estimate the margins and to produce a copula.

# 2.2 Random Variable Generation 

As it will be demonstrated in section 4 and section 5, it is easy in EDAs to estimate the distribution model based on Sklar's theorem. And the next work is to sample from the distribution model that is composed by a copula and some margins. An example of sampling from 2 - copula is shown. Let $F(x)$ and $G(y)$ be the margins of the random vector $(X, Y)$, and the joint is $C(F(x), G(y))$, i.e. $C$ is the copula. Denote $U=F(x), V=G(y)$, then $U \in[0,1], V \in[0,1]$. According to Sklar's theorem, the sample of $(X, Y)$ can be generated by the following two steps. First, a sample value $(u, v)$ of the random vector $(U, V) \in[0,1]^{2}$ that obeys the joint $C$ is generated. Second, the sample value $(x, y)$ is generated according to the inverse of margins and $(u, v)$, i.e. $x=F^{-1}(u)$ and $y=G^{-1}(v)$.

Obviously, the first step need to be studied and it is actually one of the current hot topics for research. A method based on the conditional distribution of $C(u, v)$ is introduced as an example. The condition distribution $c_{u}(v)$ when

$U=u$ is $c_{u}(v)=P[V \leq v \mid U=u]=\lim _{\Delta u \rightarrow 0} \frac{C(u+\Delta u, v)-C(u, v)}{\Delta u}=\frac{\partial C(u, v)}{\partial u}$. So the steps are the following.

1) Generate two independent random numbers $u \sim U(0,1)$ and $t \sim U(0,1)$;
2) Let $v=c_{u}^{(-1)}(t)$, where, $c_{u}^{(-1)}(t)$ is the restricted inverse function of $c_{u}(v)$ in $[0,1]$;
3) $(u, v)$ is the sample that obeys $C$.

This is a way to sample from the 2 -copula based on the conditional distribution and it can be extended to $n$-copula. Furthermore, many ways to sample from the $n$-copula are studied by the scholars [33,34].

# 3 Motivation 

The main idea of EDAs is to analyze the distribution model of the promising population and to affect the next generation by use of the distribution model. Selection, modeling and sampling are the three main steps of EDAs. Selection is used to increase the average fitness of the population by eliminating low fitness individuals while increasing the number of copies of high fitness ones. Modeling is used to quantify the distribution of the selected population, i.e. by probability density function (pdf), cumulative distribution function (cdf) or some other ways. Sampling is used to generate the next generation according to the modeled distribution.

To reflect the entire relation of the random variables and the distribution model of selected population, the joint of all random variables is the best way. However, the computation cost to model the joint is very large when the problem involves a large number of variables. For instance, EMNA supposes that the joint is multivariate normal distribution, and the parameters (i.e. mathematical expectation and covariance matrix) are estimated by EML. Obviously, the size of covariance matrix is the square of the number of variables in the problem. The larger the problem we are trying to solve, the higher is the computational cost to estimate the necessary parameters.
![img-1.jpeg](img-1.jpeg)

Fig. 2 The schema of copula-EDA

On the grounds of Sklar's theorem, the joint of random variables could be represented by a copula and the margins of each random variable. Thus the relation of random variables could be denoted by a selected copula and the margins are also estimated as a certain distribution, and then the joint is obtained according to equation (8). Actually, the joint $H$ does not need to be calculated in copula-EDAs. The only two works are to select or to construct a copula $C$ and to estimate each one-dimensional margins $F_{i}, i=1, \ldots, N$.

Sampling from the estimated distribution model is the next work after the distribution model of selected population is estimated, that is the new individuals generated should obey the estimated distribution. To generate an individual, the first work is to generate a vector $\left\{u_{1}, u_{2}, \ldots, u_{N}\right\} \in[0,1]^{N}$ who obeys the joint $C$ according to copula theory. Subsequently, the values $x_{i}=F_{i}^{-1}\left(u_{i}\right)$ are calculated according to the inverse function of each margins, and the vector $\left\{x_{1}, x_{2}, \ldots, x_{N}\right\}$ is the sample who obeys the joint $H$, i.e. $\left\{x_{1}, x_{2}, \ldots, x_{N}\right\}$ is one generated individual. To sum up the above arguments, the schema of EDAs based on copula theory (cop-ula-EDA) is shown in Fig. 2. Copula-EDA generates random initial population firstly, then repeat the following 4 steps until certain terminate condition is met.

1. Select $m$ individuals from the current population as the promising population.
2. Estimate the margins. The $m$ individuals are the $m$ samples of the $N$ dimensional random vector. Each one-dimensional margin $F_{i}(i=1, . ., N)$ is estimated according to the $m$ samples. The margins could be empirical distribution, normal distribution or others.
3. Sample from the copula $C$. Generate $l$ vectors $\left\{u_{1}{ }^{(j)}, u_{2}{ }^{(j)}, \ldots, u_{N}{ }^{(j)}\right\}(j=1, \ldots, l)$ who obey the joint $C$.
4. Compose the next generation by the following 3 parts. 1) Reserve the best $k$ individuals of the current generation to the next generation. 2) Get the new $l$ individuals by calculate $x_{i}^{(j)}=F_{i}^{-1}\left(u_{i}^{(j)}\right)(i=1, . ., N, j=1, \ldots, l)$. 3) to generate some random individuals in the search space depending on certain mutation rate.

# 4 Two-Dimensional Copula-EDAs 

Suppose that the optimization problem is

$$
\min f(X)=f\left(x_{1}, x_{2}, \ldots, x_{n}\right), x_{i} \in\left[a_{i}, b_{i}\right](i=1,2, \ldots, n)
$$

Let $s$ denote the population size. Let $\mathbf{x}=\left\{x^{i}=\left(x_{1}^{i}, x_{2}^{i}, \ldots, x_{n}^{i}\right), i=1,2, \ldots, s\right\}$ denote the population. Then the population $\mathbf{x}$ is composed of $s$ observed samples from a random vector $\left(X_{1}, X_{2}, \ldots, X_{n}\right)$. The marginal distribution of each random variable $X_{i}(i=1,2, \ldots, n)$ can be Gaussian distribution, t-distribution or some other distribution. On the ground of Sklar's theorem, the joint distribution function can be constructed with a selected copula and the marginal distributions. The modeling for the distribution of the selected population is finished. Next step is to generate new population by the way introduced in Sect. 2.2.

# 4.1 Gaussion Copula-EDAs 

A two-dimensional optimization problem is considered. According to copula theory, the marginal distribution of each random variable and a copula are required. The marginal distributions of $\left(X_{1}, X_{2}\right)$ is easy to estimate because the observed values are given. The only thing is to evaluate sample mean and sample variance. 2-D Gauss-copula is selected which is

$$
C(u, v ; \rho)=\phi_{\rho}\left(\phi^{-1}(u), \phi^{-1}(v)\right), u, v \in[0,1]
$$

where, $\phi_{\rho}$ is a binary standard Gaussian distribution with correlation coefficient $\rho$. Determining $\rho$ is the key to construct copula.

If the Maximum Likelihood Estimation is used, then the log-likelihood function is

$$
l(\rho)=\sum_{i=1}^{s}\left\{-\ln 2 \pi-\frac{1}{2} \ln \left(1-\rho^{2}\right)-\frac{z_{1 i}^{2}+z_{2 i}^{2}-2 \rho z_{1 i} z_{2 i}}{2\left(1-\rho^{2}\right)}\right\}+\sum_{i=1}^{s}\left[\ln f\left(x_{1}^{i}\right)+\ln g\left(x_{2}^{i}\right)\right]
$$

where,

$$
z_{1 i}=\phi^{-1}\left(F\left(x_{1}^{i}\right)\right), z_{2 i}=\phi^{-1}\left(G\left(x_{2}^{i}\right)\right)
$$

If Moment Estimation is used, then

$$
\rho=\frac{\frac{1}{s} \sum_{i=1}^{s} x_{1}^{i} x_{2}^{i}-\bar{X}_{1} \bar{X}_{2}}{S_{X_{1}}^{s} S_{X_{2}}^{s}}
$$

where,

$$
\bar{X}_{k}=\frac{1}{s} \sum_{i=1}^{s} x_{k}^{i}, S_{X_{k}}^{s}=\sqrt{\frac{1}{s-1} \sum_{i=1}^{s}\left(x_{k}^{i}\right)^{2}},(k=1,2)
$$

Next, sampling from the distribution function is discussed. Since

$$
\begin{aligned}
& C(u, v ; \rho)=\phi_{\rho}\left(\phi^{-1}(u), \phi^{-1}(v)\right) \\
& =\int_{-\infty}^{u} \int_{-\infty}^{v} \frac{1}{2 \pi \sqrt{1-\rho^{2}}} \exp \left\{-\frac{\left[\phi^{-1}(s)\right]^{2}+\left[\phi^{-1}(t)\right]^{2}-2 \rho \phi^{-1}(s) \phi^{-1}(t)}{2\left(1-\rho^{2}\right)}\right\} d t d s
\end{aligned}
$$

then

$$
\begin{aligned}
& \omega=C_{u}(v)=\partial C(u, v) / \partial u \\
& =e^{\frac{\left[\phi^{-1}(u)\right]^{2}}{2}} \int_{-\infty}^{v} \frac{1}{2 \pi \sqrt{1-\rho^{2}}} \exp \left\{-\frac{\left[\phi^{-1}(t)-\rho \phi^{-1}(u)\right]^{2}}{2\left(1-\rho^{2}\right)}\right\} d t
\end{aligned}
$$

Therefore,

$$
v=\sqrt{1-\rho^{2}} \phi^{-1}\left(e^{\frac{\left[\phi^{-1}(u)\right]^{2}}{2}} \omega\right)+\rho \phi^{-1}(u)=\sqrt{1-\rho^{2}} \phi^{-1}\left(\omega^{\prime}\right)+\rho \phi^{-1}(u)
$$

So randomly generate vector $\left(u, \omega^{\prime}\right) \sim U[0,1]^{2}$, and then the other random number $v$ is calculated by using equation (16). The vector $\left(x_{1}, x_{2}\right)$ can be calculated by using equation (17).

$$
x_{1}=\sigma_{1} \phi^{-1}(u)+\mu_{1}, x_{2}=\sigma_{2} \phi^{-1}(u)+\mu_{2}
$$

where,

$$
\mu_{k}=\bar{X}_{k}, \sigma_{k}=S_{X_{k}}^{*},(k=1,2)
$$

Conclusively, the algorithm for implementing 2-D copula-EDA is as follows [35]:

1. Initialize (pop, $N$ ). Randomly generate initial population pop with size $N$. set generation count $g \leftarrow 0$.
2. Selection (pop, spop, select-rate). Select the best select-rate $\times N$ agents from pop to spop according to the agents' fitness.
3. copula-generator (pop, spop, mutate-rate).

- 3.1. Construct the distribution model of spop:

1) calculate the sample average and the sample variance for each random variable according to (13), then the marginal distributions are $F=N\left(\bar{X}_{1}, S_{X_{1}}^{*}\right)$ and $G=N\left(\bar{X}_{2}, S_{X_{2}}^{*}\right)$
2) calculate the estimation value of parameter $\rho$ according to equation (11) or (12), then the copula $C$ is the same as (14);

- 3.2. Generate a new population by iterative using procedure generation( $C$, $F, G)$, where
$-v=C_{u}^{(-1)}(\omega)=\sqrt{1-\rho^{2}} \phi^{-1}(\omega)+\rho \phi^{-1}(u)$.
- 3.3. Randomly generate some agents by the mutate-rate.

4. Stop if the termination criterion is met.
5. Set $g \leftarrow g+1$ and go to Step 2 .

The following 9 test functions are used to show the behavior of the proposed algorithm cEDA and to compare the cEDA with PBILc and other EDAs. The test functions $F_{1} \sim F_{3}$ and $F_{6} \sim F_{8}$ are also used in [26].

- $F_{1}(x)=-\frac{100}{10^{-5}+\sum_{i}\left|y_{i}\right|}$, where $y_{1}=x_{1}, y_{i}=x_{i}+y_{i-1}(i \geq 2), x_{i} \in[-3,3]$, the optimal result is $F_{1}^{*}(0,0, \ldots, 0)=-10^{7}$.
- $F_{2}(x)=-\frac{100}{10^{-5}+\sum_{i}\left|y_{i}\right|}$, where $y_{1}=x_{1}, y_{i}=x_{i}+\sin y_{i-1}(i \geq 2), x_{i} \in[-3,3]$, the optimal result is $F_{2}^{*}(0,0, \ldots, 0)=-10^{7}$.
- $F_{3}(x)=-\frac{100}{10^{-5}+\sum_{i}\left|y_{i}\right|}$, where $y_{i}=0.024 \times(i-1)-x_{i}, x_{i} \in[-3,3]$, the optimal result is $F_{3}^{*}(0.024 \times 2,0.024 \times 3, \ldots, 0.024 \times(n+1))=-10^{7}$.

- $F_{4}(x)=\sum_{i} x_{i}^{2}$, where $x_{i} \in[-500,500]$, the optimal result is $F_{4}^{*}(0,0, \ldots, 0)=0$.
- $F_{5}(x)=1+\sum_{i}\left(\sin x_{i}\right)^{2}-0.1 \exp \left(-\sum_{i} x_{i}^{2}\right)$, where $x_{i} \in[-10,10]$, the optimal result is $F_{5}^{*}(0,0, \ldots, 0)=0.9$.
- $F_{6}(x)=\sum_{i}\left(x_{i}^{2}-A \cos \left(2 \pi x_{i}\right)+A\right)$, where $x_{i} \in[-5,5]$, the optimal result is $F_{6}^{*}(0,0, \ldots, 0)=0$.
- $F_{7}(x)=\sum_{i}\left(418.9829+x_{i} \sin \sqrt{\left|x_{i}\right|}\right)$, where $x_{i} \in[-500,500]$, the optimal result is $F_{7}^{*}(-420.9687,-420.9687, \ldots,-420.9687)=0$.
- $F_{8}(x)=\sum_{i} x_{i}^{2}-\prod_{i} \cos \left(\frac{x_{i}}{\sqrt{i+1}}\right)$, where $x_{i} \in[-100,100]$, the optimal result is $F_{8}^{*}(0,0, \ldots, 0)=-1$.
- $F_{9}(x)=\left[1+\left(x_{1}+x_{2}+1\right)^{2} \times\left(19-14 x_{1}+3 x_{1}^{2}-14 x_{2}+6 x_{1} x_{2}+3 x_{2}^{2}\right)\right]$

$$
\times\left[30+\left(2 x_{1}-3 x_{2}\right)^{2} \times\left(18-32 x_{1}+12 x_{1}^{2}+48 x_{2}-36 x_{1} x_{2}+27 x_{2}^{2}\right)\right]
$$

$x_{1}, x_{2} \in[-2,2]$, the optimal result is $F_{9}^{*}(0,-1)=3$.
All test functions are optimized in 2-dimensional spaces, the maximal generation $g$ is set to 1000 . The search terminates if the distance between the best solution found so far and the optimum is less than the predefined precision. Table 1 and Table 2 display the experimental results.

Table 1 The convergence of copula-EDA and PBILc, the maximal generation is 1000

Table 2 The state of different algorithm after 50 runs

![img-4.jpeg](img-4.jpeg)

Fig. 3 The performance on test function $F_{1}$
![img-3.jpeg](img-3.jpeg)

Fig. 5 The performance on test function $F_{3}$
![img-4.jpeg](img-4.jpeg)

Fig. 6 The performance on test function $F_{4}$

![img-5.jpeg](img-5.jpeg)

Fig. 7 The performance on test function $F_{5}$
Fig. 8 The performance on test function $F_{6}$
![img-6.jpeg](img-6.jpeg)

Fig. 9 The performance on test function $F_{7}$ Fig. 10 The performance on test function $F_{8}$
![img-7.jpeg](img-7.jpeg)

Fig. 11 The performance on test function $F_{9}$

Copula-EDA is abbreviated to cEDA in Table 1 and Fig.3-11. PBILcM is performed based on PBILc with the mutation rate as 0.05 for the sake of comparing the performance of copula-EDA and PBILc with the same parameters. But the experimental results show that the convergence rate of PBILcM is 0 in each function with the parameters in Table 1. The convergence rate and the convergence

generations are the average results of 50 runs. The experimental results show that copula-EDA converges to the global optimum quickly in the test functions.

The mean fitness and the standard variance of each algorithm after 50 runs are showed in Table 2. Obviously, copula-EDA performs better than the other two algorithms. It is found through further experiments that Copula-EDA converges faster than PBILc, but it needs more agents in the population than PBILc.

The evolution processes of the above three algorithms is compared with the same population in Fig.3-11. The population in the first generation is same for each algorithm. Error in Fig.3-11 is the fitness difference. Copula-EDA converges to the best solution quickly in almost all tested functions especially for the function $F_{1}-F_{3}$ whose random variables are strongly correlative with each other. It is also can be seen from Fig.7-9 that copula-EDA is premature in some cases.

# 4.2 Archimedean Copula-EDAs 

According to Sklar's theorem, two steps are performed in order to construct the joint probability distribution function of a random vector. The first step is constructing the margins of each random variable separately. The second step is selecting a proper copula to construct the joint distribution. Therefore, the distribution character of each random variable and their relationship can be studied by themselves. This way can be used in EDAs to model the joint probability distribution function. And then samples are generated from the specified joint distribution by use of the copula.

The optimization problem is

$$
\min f(X)=f\left(x_{1}, x_{2}\right), x_{i} \in\left[a_{i}, b_{i}\right] \quad(i=1,2)
$$

Denote the selected population with size $s$ as

$$
\mathbf{x}=\left\{x^{i}=\left(x_{1}^{i}, x_{2}^{i}\right), i=1,2, \ldots, s\right)\}
$$

In other words, $\mathbf{x}$ are the $s$ observations of the random vector $\left(X_{1}, X_{2}\right)$. The marginal distribution function of each random variable $X_{i}$ can be estimated by normal distribution, t-distribution or empirical distribution, etc. Denote the marginal distribution function of $X_{i}$ as $u=F\left(x_{1}\right)$ and $v=G\left(x_{2}\right)$. The joint probability distribution function is constructed with a selected copula $C$ and the estimated margins in the light of Sklar's theorem.

The next step is to generate samples from the joint distribution using the copula as a tool. By virtue of Sklar's theorem, it is necessary only to generate a pair $(u, v)$ of observations of uniform $(0,1)$ random variables $(U, V)$ whose joint distribution function is $C$, and then transform those uniform random variables via the quasiinverse of the marginal distribution functions. One procedure for generating such of a pair $(u, v)$ of uniform $(0,1)$ random variables is the conditional distribution method. For this method, the conditional distribution function for $V$ given $U=u$ is need, which is denoted as $C_{u}(v)$ :

$$
C_{u}(v)=P(V \leq v \mid U=u)=\lim _{\Delta u \rightarrow 0} \frac{C(u+\Delta u, v)-C(u, v)}{\Delta u}=\frac{\partial C(u, v)}{\partial u}
$$

$C_{u}(v)$ exists and is non-decreasing almost everywhere in $\mathbf{I}$.
Conclusively, the generation of sample is performed as the following steps:

1. Generate two independent uniform $(0,1)$ random variables $u$ and $t$;
2. Set $v=C_{u}^{(-1)}(t)$, where $C_{u}^{(-1)}(t)$ denotes a quasi-inverse of $C_{u}(v)$.
3. The desired pair is $(u, v)$.
4. Set $x_{1}=F^{(-1)}(u), x_{2}=G^{(-1)}(v)$, then $\left(x_{1}, x_{2}\right)$ is a sample of the specified joint distribution.

To sum up, the process for implementing 2-D Copula-EDA is as follows [36]:

1. Initialize (pop, $N$ ). Randomly generate initial population pop with size $N$. set generation count $g \leftarrow 0$.
2. Selection (pop, spop, select-rate). Select the best select-rate $\times N$ agents from pop to spop according to the agents' fitness.
3. Copula-generator (pop, spop, mutate-rate).

- 3.1. Construct the distribution model of spop;
- 3.2. Generate a new population based on the specified joint distribution, and randomly generate some agents by the rate mutate-rate.

4. Stop if the termination criterion is met.
5. Set $g \leftarrow g+1$, and then go to step 2 .

The functions in Sect. 4.1 are used to test the effectiveness of the proposed algorithm. The following two Archimedean copulas are chosen.

- Clayton: $C_{1}(u, v)=\left(u^{-\theta}+v^{-\theta}-1\right)^{-1 / \theta}, \theta \geq-1, \theta \neq 0$

$$
C_{2}(u, v)=\frac{u v}{1-\theta(1-u)(1-v)},-1 \leq \theta<1
$$

- Ali-Mikhail-Haq:

All the one-dimensional marginal distributions are normal distributions. Table 3 displays the experimental results.

All test functions are optimized in 2-dimensional spaces, the maximal generation $g$ is set to 1000 . The search terminates if the distance between the best solution found so far and the optimum is less than the predefined precision $\left(10^{-5}\right.$ for other test functions in spite of $10^{-3}$ for $F_{7}$ ). Parameters are set to (select-rate $=0.2$, mutate-rate $=0.05$, population size $N=100$ ) for all experiments. The convergence rate and the convergence generations are the average results of 50 runs. The experimental results show that Copula-EDA converges to the global optimum quickly in the test functions. There is not much difference in performance between two copulas for other test functions despite $F_{3}$ and $F_{6}$. Both the algorithms proposed in this section perform better than the copula-EDA based on Gaussian copula (see Sect. 4.1) and PBILc [26].

Table 3 Experimental results of Archimedean copula-EDAs

# 5 High-Dimensional Copula-EDAs 

In fact, many optimization problems are high-dimensional. The 2-dimensional copula-EDAs only show the feasibility to apply copula theory to EDAs. The copula-EDA based on the empirical copula is discussed in this section.

### 5.1 High-Dimensional Copula Constructions

Let $F(\mathbf{x})$ be the joint of the $D$-dimensional random vector $\mathbf{x}$, the margins of each random variable are $F_{i}(x)(i=1,2, \ldots, D)$, and the copula, then the equation $C\left(u_{1}, u_{2}, \ldots, u_{D}\right)=F\left(F_{1}^{-1}\left(u_{1}\right), F_{2}^{-1}\left(u_{2}\right) \ldots, F_{D}^{-1}\left(u_{D}\right)\right)$ is gotten according to Sklar's theorem. A random vector $\left(u_{1}, u_{2}, \ldots, u_{D}\right)$ obeying $C(\mathbf{u})$ is generated firstly in order to generate a random vector obeying $F(\mathbf{x})$. Subsequently, the vector $\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ is

calculated according to the inverse function of the margins $F_{i}(x)(i=1,2, \ldots, D)$, i.e. $x_{i}=F_{i}^{-1}(x)(i=1,2, \ldots, D)$.

If the density of the copula $C(\mathbf{u})$ is $c(\mathbf{u})$, then the marginal probability density functions are

$$
c_{d}(u)=c_{d}\left(u_{1}, u_{2}, \ldots, u_{d}\right)=\int_{u_{d-1}=0}^{1} \ldots \int_{u_{D}=0}^{1} c(u) d u_{d+1} \ldots d u_{D}, d=1,2, \ldots, D-1
$$

Obviously, $c(\mathbf{u})=c_{D}(\mathbf{u})$. The condition distribution functions are

$$
C_{d}\left(u_{d} \mid u_{1}, \ldots, u_{d-1}\right)=P\left\{U_{d} \leq u_{d} \mid U_{1}=u_{1}, \ldots, U_{d-1}=u_{d-1}\right\}=\frac{\int_{u=0}^{u_{d}} c_{d}\left(u_{1}, \ldots, u_{d-1}, u\right) d u}{c_{d-1}\left(u_{1}, \ldots, u_{d-1}\right)}, d=1,2, \ldots D
$$

A method to construct a copula based on the empirical distribution and to sample from the empirical copula is proposed in [34] and it is briefly introduced in the following paragraphs.

Let the samples of the $D$-dimensional random vector $\mathbf{z}$ be $\mathbf{z}_{i}=\left(z_{i 1}, z_{i 2}, \ldots z_{i D}\right)(i=1,2, \ldots, n)$. The empirical distribution function of each dimension is constructed firstly according to the samples and then each sample $\mathbf{z}_{i}$ is mapped to a value $u_{i}$ belonging to $\mathbf{I}^{D}$. The values $\mathbf{u}_{i}(i=1,2, \ldots, n)$ are actually the samples of the random vector $\mathbf{u}$ obeying $\operatorname{cdf} C(\mathbf{u})$. In order to sample from the estimated $\operatorname{cdf}$ $C(\mathbf{u})$, the conditional distribution functions $c_{d}(\mathbf{u})$ are necessary to be estimated according to the samples $u_{i}(i=1,2, \ldots, n)$. the details are shown as follows.

The samples $\mathbf{z}_{i}=\left(z_{i 1}, z_{i 2}, \ldots z_{i D}\right)(i=1,2, \ldots, n)$ are sorted in each dimension. For example, the sorted sequence of the $d^{\text {th }}$ dimension is $z_{(1) d}, z_{(2) d}, \ldots, z_{(n) d}$, then the empirical distribution of the $d^{\text {th }}$ dimension is

$$
F_{d}(z)= \begin{cases}0 & z<z_{(1) d} \\ i / n & z_{(i) d} \leq z \leq z_{(i+1) d}, i=1,2, \ldots, n-1 \\ 1 & z_{(n) d} \leq z\end{cases}
$$

According to equation (24), the samples $\mathbf{z}_{i}=\left(z_{i 1}, z_{i 2}, \ldots z_{i D}\right)(i=1,2, \ldots, n)$ are mapped to the vectors $\mathbf{u}_{i}=\left(u_{i 1}, u_{i 2}, \ldots u_{i D}\right) \in\left\{1 / n, 2 / n, \ldots, 1\right\}^{D}(i=1,2, \ldots, n)$.

Denote $S_{1}, S_{2}, \ldots, S_{K}$ as the partition of the interval $\mathbf{I}=[0,1]$, where $S_{i}=((i-1) \delta, i \delta]$ $(\mathrm{i}=1,2, \ldots, \mathrm{~K}), \delta=1 / \mathrm{K}, \mathrm{K}$ is a positive integer. Thus the D -cube $\mathbf{I}^{D}$ is divided into $K^{D}$ subcubes $\Delta_{i}=S_{i} \times S_{i_{1}} \times \ldots \times S_{i_{m}} i=\left(i_{1}, i_{2}, \ldots, i_{D}\right) \subseteq\{1,2, \ldots, K\}^{D}$. denote $N_{i}$ as the number of points in ,i.e. $N_{i}=\left|\left\{\mathbf{u}_{j} \mid \mathbf{u}_{j} \in \Delta_{i}\right\}\right|$. The density of the copula is

$$
c(\mathbf{u})=f_{\mathbf{i}}=N_{\mathbf{i}} / n / \delta^{D}
$$

Let $\uparrow u=\max \left\{1,\lceil u K\rceil\right\}$, then $\mathbf{i}=\left(\uparrow u_{1}, \uparrow u_{2}, \ldots, \uparrow u_{D}\right) \in\{1,2, \ldots, K\}^{D}$, and

$$
c_{d}\left(u_{1}, \ldots, u_{d}\right)=\delta^{D-d} f_{\left|u_{1}, \ldots, u_{d}\right|}^{(d)}, d=1, \ldots, D-1
$$

where,

$$
f_{i_{1}, \ldots, i_{d}}^{(d)}=\sum_{\left(i_{d+1}, \ldots, i_{D}\right)=(1, \ldots, 1)}^{(K, \ldots, K)} f_{1}, \quad\left(i_{1}, \ldots, i_{d}\right)=\{1,2, \ldots, K\}^{d}
$$

The conditional distribution is

$$
\begin{gathered}
C_{2}\left(u_{2} \mid u_{1}\right)=\delta^{D-1} \sum_{i_{2}=1}^{\downarrow u_{2}} f_{\uparrow u_{1}, i_{2}}^{(2)}+\left(u_{2}-\downarrow u_{2} \delta\right) \delta^{D-2} f_{\uparrow u_{1}, \uparrow u_{2}}^{(2)} \\
C_{d}\left(u_{d} \mid u_{1}, \ldots, u_{d-1}\right)=\frac{\delta \sum_{i_{d}=1}^{\downarrow u_{d}} f_{\uparrow u_{1}, \ldots, \uparrow u_{d-1}, i_{d}}^{(d)}+\left(u_{d}-\downarrow u_{d} \delta\right) f_{\uparrow u_{1}, \ldots, \uparrow u_{d}}^{(d)}}{\delta f_{\uparrow u_{1}, \ldots, \uparrow u_{d-1}}^{(d-1)}}
\end{gathered}
$$

where, $\downarrow u=\uparrow u-1$.
The following algorithm (Algorithm 1) can be applied to calculate the arrays $f^{(d)}$ which we use for the calculation of the conditional distribution functions of the copula.

1. Calculate the empirical distribution functions of the marginal distributions of the sample with equation (24) and the image points $\mathbf{u}_{i}$ of the sample points $\mathbf{z}_{i}(i=1,2, \ldots, n)$.
2. Set all elements of the arrays $f^{(d)}$ to 0 .
3. for $i:=1$ to $n$ do

$$
\begin{aligned}
& \text { for } d:=1 \text { to } D \text { do } \\
& j_{d i}=\uparrow u_{d, i} \text {; } \\
& \text { end } \\
& \text { for } d:=2 \text { to } D \text { do } \\
& \quad f_{j_{1}, \ldots, j_{d}}^{(d)}:=f_{j_{1}, \ldots, j_{d}}^{(d)}+1 / n / \delta^{D} \\
& \text { end } \\
& \text { end }
\end{aligned}
$$

Let $\mathbf{f}=\left\{f_{i}^{d}\right\} .\left(i=\left(i_{1}, i_{2}, \ldots, i_{D}\right) \in\{1,2, \ldots, K\}^{D}, d=1,2, \ldots, D-1\right)$. The procedure generation $(\mathbf{f})$ can be used to generate random numbers $u_{1}, u_{2}, \ldots, u_{D}$ obeying the empirical copula.

1. Generate two independent random numbers $u_{1}$ and $u$;

$$
u-\delta^{D-1} \sum_{i_{2}=1}^{\downarrow u_{2}} f_{\uparrow u_{1}, i_{2}}^{(2)}
$$

2. Calculate $u_{2}=\downarrow u_{2} \delta+\frac{u-\delta^{D-1} \sum_{i_{2}=1}^{\downarrow u_{2}} f_{\uparrow u_{1}, i_{2}}^{(2)}}{\delta^{D-2} f_{\uparrow u_{1}, \uparrow u_{2}}^{(2)}}$, where $\downarrow u_{2}$ is the minimal number in
$\{0,1, \ldots, K-1\}$ satisfied with the condition $u K^{D-1} \leq \sum_{i_{2}=1}^{\downarrow u_{2}+1} f_{\uparrow u_{1}, i_{2}}^{(2)}$;

3. for $d:=3$ to $D$

- 3.1. Generate a random number $u$ in $\mathbf{I}$;
- 3.2. Calculate $u_{d}=\downarrow u_{d} \delta+\delta \frac{u f_{\uparrow_{n_{1}, \ldots, \uparrow} u_{d-1}}^{(d-1)}-\sum_{i_{d}=1}^{\downarrow u_{d}} f_{\uparrow_{n_{1}, \ldots, \uparrow} u_{d-1}, i_{d}}^{(d)}}{f_{\uparrow_{n_{1}, \ldots, \uparrow} u_{d}}^{(d)}}$, where $\downarrow u_{d}$ is the minimal number in $\{0,1, \ldots, \mathrm{~K}-1\}$ satisfied with the condition $u f_{\uparrow_{n_{1}, \ldots, \uparrow} u_{d-1}}^{(d-1)} \leq \sum_{i_{d}=1}^{\downarrow u_{d}+1} f_{\uparrow_{n_{1}, \ldots, \uparrow} u_{d-1}, i_{d}}^{(d)}$
end


# 5.2 Copula-EDA Based on Empirical Copula 

For the optimization problem $\min f\left(x_{1}, x_{2}, \ldots, x_{D}\right), x_{i} \in\left[a_{i}, b_{i}\right],(i=1,2, \ldots, D)$, the copula-EDA based on the above empirical copula is in the following [37].

1. Generate $N$ individuals in the search space randomly. Decide the selection rate $s$ and the mutation rate $t$;
2. Select $n=s \times N$ individuals $\left\{\mathbf{z}_{1}, \mathbf{z}_{2}, \ldots, \mathbf{z}_{n}\right\}$ among the $N$ individuals as the promising population, and reserve them in the next generation;
3. Calculate $\mathbf{f}=\mathrm{F}\left(\mathbf{z}_{1}, \mathbf{z}_{2}, \ldots, \mathbf{z}_{n}\right)$ by doing Algorithm 1
4. Repeat the following steps $m=(1-s-t) \times N$ times, add the new $m$ individuals into the population.

- $4.1\left(u_{1}, u_{2}, \ldots, u_{D}\right)=$ generation $(\mathbf{f})$
- 4.2 for $i:=1$ to $D$
$x_{i}=F_{\mathrm{i}}^{-1}\left(u_{i}\right)$, where $F_{\mathrm{i}}$ is the empirical distribution (24) or the normal distribution
end
$\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ is the new individual.

5. Generate $t \times N$ individuals in the search space randomly as the new individuals;
6. Stop if the terminate condition is met, and the best individual of the population is the optimal result.

The following 3 functions are used to test the proposed algorithm.

- Sumcan function: $f_{1}(x)=-\left\{10^{-5}+\sum_{i=1}^{D}\left|y_{i}\right|\right\}^{-1}$, where, $y_{1}=x_{1}, y_{i}=y_{i-1}+x_{i}$, $i=2, \ldots, d,-0.16 \leq x_{i} \leq 0.16$
- Schwefel function: $f_{2}(x)=\sum_{i=1}^{D}\left[\left(x_{1}-x_{i}^{2}\right)^{2}+\left(x_{i}-1\right)^{2}\right]$, where, $-10 \leq x_{i} \leq 10$

- Griewank function: $f_{3}(x)=1+\sum_{i=1}^{D} \frac{x_{i}^{2}}{4000}-\prod_{i=1}^{D} \cos \left(\frac{x_{i}}{\sqrt{i}}\right)$, where, $-600 \leq x_{i} \leq 600$

The above three functions are all minimal optimization problem. The empirical copula and the normal margins are used in the tested copula-EDA, and is denoted as $\mathrm{cEDA}_{\mathrm{PG}}$. The parameters are the same as in [30], i.e. the dimension of the problem is $\mathrm{D}=10$, the population size of the three problem are 2000,2000 and 750 respectively. The maximal fitness evaluation is 300,000 . The truncation selection is used. The mutation is used and the mutation rate is 0.05 . The search space is not divided when the empirical copula is constructed, i.e. $\mathrm{K}=1$. The variance for sampling is one of the following three strategies.
A. The variance is fixed.
B. The variance is set to the sample variance, i.e. $\sigma_{i}=\sqrt{\frac{\sum_{j=1}^{S}\left(x_{i j}-\overline{x_{i}}\right)^{2}}{S-1}}$, where, $\overline{x_{i}}=\frac{1}{S} \sum_{j=1}^{S} x_{i j}$.
C. The variance is linearly changed, i.e.

$$
\sigma_{i}^{t+1}=(1-\alpha) \sigma_{i}^{t}+\alpha \sqrt{\frac{\sum_{j=1}^{S}\left(x_{i j}-\overline{x_{i}}\right)^{2}}{S-1}}, \alpha=0.2
$$

Table 4 The comparison among cEDA and other algorithms on Sumcan function

Table 5 The comparison among cEDA and other algorithms on Schwefel function
Table 6 The comparison among cEDA and other algorithms on Griewank function
The experimental results in Table 4-6 indicate that the performance of $\mathrm{cEDA}_{\mathrm{PG}}$ is affected by the parameters. cEDA finds the better results than other compared algorithms in certain parameters. Especially for Griewank function, $\mathrm{cEDA}_{\mathrm{PG}}$ finds the optimal result after 68.7 generations when selection rate is 0.2 and the variance is changed in strategy B. It can be indicated from Fig. 12-13 that $\mathrm{cEDA}_{\mathrm{PG}}$ is good at exploration and is not good at exploitation.

![img-8.jpeg](img-8.jpeg)

Fig. 12 The performance of $\mathrm{cEDA}_{\mathrm{PG}}$ in Sumcan function
![img-9.jpeg](img-9.jpeg)

Fig. 13 The performance of $\mathrm{cEDA}_{\mathrm{PG}}$ in Schwefel function

# 6 Conclusion 

Estimation of Distribution Algorithms utilize the distribution characters of the selected population to guide the creation of the next generation. Therefore, the population evolves towards the optimal direction and finds the optimal solution quickly. Two key steps in EDAs are to estimate the distribution of the selected population and to sample from the distribution model.

Copula theory contributes to the estimation of the distribution model and sampling from the estimated model because copula theory provides a way to present the multivariate joint distribution with the univariate marginal distributions and a function called copula. How to construct copula and to sample from the copula are also the research topics of copula theory.

Copula theory is applied into the research of EDAs and three EDAs based on different copulas are introduced in this chapter. They are respectively copula-EDA based on Gaussian copula, copula-EDA based on Archimedean copula and cop-ula-EDA based on empirical copula. All of them can find the optimal results quick than the other algorithms used for comparison. But there are also shortages in them. For example, the copula-EDA based on empirical copula is not good at exploitation and the convergence speed in last generations is slow and the algorithm is affected by the selection of parameters.

Different copula is corresponded to different relationship of the random variables. So the performance of copula-EDAs based on different copula is different on optimization problems. The following questions need to be studied further.

- The expansion of copula-EDA based on Gaussian copula and Archimedean copula on high-dimensional optimization problems.
- How to select and construct copula.

- The comparison among the copula-EDAs based on different copulas.
- The relationship between the characters of the optimization problem and the optimal copula.

