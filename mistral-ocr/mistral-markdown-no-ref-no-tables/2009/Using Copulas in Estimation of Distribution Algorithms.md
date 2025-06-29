# Using Copulas in Estimation of Distribution Algorithms 

Rogelio Salinas-Gutiérrez, Arturo Hernández-Aguirre, and Enrique R. Villa-Diharce<br>Centro de Investigación en Matemáticas, Guanajuato, México<br>\{rsalinas,artha, villadi\}@cimat.mx


#### Abstract

A new way of modeling probabilistic dependencies in Estimation of Distribution Algorithm (EDAs) is presented. By means of copulas it is possible to separate the structure of dependence from marginal distributions in a joint distribution. The use of copulas as a mechanism for modeling joint distributions and its application to EDAs is illustrated on several benchmark examples.


## 1 Introduction

Estimation of Distribution Algorithms (EDAs) 17] are recognized as a new paradigm in Evolutionary Computation to deal with optimization problems 15. EDAs are a class of Evolutionary Algorithms (EAs) based on probabilistic models instead of genetic operators such as crossover and mutation. The use of probabilistic models allow us to explicitly represent: 1) dependencies between the decision variables; and 2) their structure. EDAs populate the next generation by simulating individuals from the probabilistic model, therefore, the goal is to transfer both the data dependencies and the structure found in the best individuals into the next population. A pseudocode for EDAs is shown in Algorithm 1.

```
Algorithm 1. Pseudocode for EDAs
    assign \(t \longleftarrow 0\)
    generate the initial population \(P_{0}\) with \(M\) individuals at random
    select a collection of \(N\) solutions \(S_{t}\), with \(N<M\), from \(P_{t}\)
    estimate a probabilistic model \(\mathcal{M}_{t}\) from \(S_{t}\)
    generate the new population by sampling from the distribution of \(S_{t}\).
    assign \(t \longleftarrow t+1\)
    if stopping criterion is not reached go to step 2
```

As it can be seen in step 3, the interactions among the decision variables are taken into account through the estimated model. The possibility of incorporating the dependencies among the variables into the new population greatly modifies the performance of an EDA. Nowadays, several EDAs have been proposed for

optimization problems in discrete and continuous domains. They can be grouped by the complexity of the probabilistic model used to learn the interactions between the variables. For instance, the UMDA [18|1113] can be considered the most simple EDA because it does not take into account dependencies between the variables, while the BMDA [21] and MIMIC [6|1113] just take dependencies between pairs of variables into account. Probabilistic models such as Bayesian networks and multivariate Gaussian distributions have been used by EDAs for multiple dependencies. Some examples in discrete domain are PADA [24], EBNA [812] and BOA [20]. For continuous domain EMNA [14] and EGNA [1113] are EDAs based on multivariate and bivariate Gaussian distribution respectively. In this paper we deal with continuous optimization problems, and address the use of copulas in EDAs. One motivation of this work is to take advantage of the almost natural capacity of copulas to represent bivariate dependencies through concordance measures, such as Kendall's tau or Pearson's rho. The goal of the paper is to introduce copula functions and implement the copula-based MIMIC; to the best of our knowledge this paper would be one of the first studies on the performance of EDAs based on copulas. Related works have considered EDAs based on multidimensional Gaussian copula with nonparametric marginals [13] and EDAs based on two dimensional copulas with Gaussian marginals [27|26].

The structure of the paper is the following: Section 2 is a short introduction to copula functions, Sect. 3 describes the implementation of the MIMIC algorithm with copula functions. Section 4 presents the experimental setting to solve 5 test global optimization problems, and Sect. 5 resumes the conclusions.

# 2 Copula Functions 

The concept of copula was introduced by Sklar [23] to separate the effect of dependence from the effect of marginal distributions in a joint distribution. The separation between marginal distributions and a dependence structure explains the modeling flexibility given by copulas and, for this reason, they have been widely used in many research and application areas such as finance [425], climate [22], oceanography [7], hydrology [9], geodesy [2], and reliability [16].

Definition 1. A copula is a joint distribution function of standard uniform random variables. That is,

$$
C\left(u_{1}, \ldots, u_{n}\right)=\operatorname{Pr}\left[U_{1} \leq u_{1}, \ldots, U_{n} \leq u_{n}\right]
$$

where $U_{i} \sim U(0,1)$ for $i=1, \ldots, n$.
For a more formal definition of copulas, the reader is referred to [1019]. The following result, known as Sklar's theorem, connects marginal distributions and copula with a joint distribution.

Theorem 1 (Sklar). Let $F$ be a n-dimensional distribution function with marginals $F_{1}, F_{2}, \ldots, F_{n}$, then there exists a copula $C$ such that for all $x$ in $\overline{\mathbb{R}}^{n}$,

$$
F\left(x_{1}, x_{2}, \ldots, x_{n}\right)=C\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \ldots, F_{n}\left(x_{n}\right)\right)
$$

where $\overline{\mathbb{R}}$ denotes the extended real line $[-\infty, \infty]$. If $F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \ldots, F_{n}\left(x_{n}\right)$ are all continuous, then $C$ is unique. Otherwise, $C$ is uniquely determined on $\operatorname{Ran}\left(F_{1}\right) \times \operatorname{Ran}\left(F_{2}\right) \times \cdots \operatorname{Ran}\left(F_{n}\right)$, where Ran stands for the range.

According to Theorem 1, the $n$-dimensional density $f$ can be represented as

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=f_{1}\left(x_{1}\right) \cdot f_{2}\left(x_{2}\right) \cdots f_{n}\left(x_{n}\right) \cdot c\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \ldots, F_{n}\left(x_{n}\right)\right)
$$

where $f_{i}\left(x_{i}\right)$ is the density of variable $x_{i}$ and $c$ is the density of the copula $C$. This result allows us to choose different marginals and a dependence structure given by the copula and then merge them to build a multivariate distribution. This contrasts with the usual way to construct multivariate distributions, which suffers from the restriction that the margins are usually of the same type.

There are many families of copulas and each of them is characterized by a parameter or a vector of parameters. These parameters measure dependence between the marginals and are called dependence parameters $\boldsymbol{\theta}$. In this paper we use bivariate copulas with one dependence parameter $\theta$. The dependence parameter is related to Kendall's tau through the equation (see [19])

$$
\tau\left(X_{1}, X_{2}\right)=4 \int_{0}^{1} \int_{0}^{1} C\left(u_{1}, u_{2} ; \theta\right) d C\left(u_{1}, u_{2} ; \theta\right)-1
$$

Kendall's tau measures the concordance between two continuous random variables $X_{1}$ and $X_{2}$. Table 1 shows the defining equations of the Frank copula and the Gaussian copula. Observe how the dependence parameter in the copula function is related to the Kendall's tau. The dependence parameter of a bivariate copula can be estimated using the maximum likelihood method. To do so, we need to maximize the log-likelihood function given by

$$
l(\theta)=\sum_{t=1}^{T} \ln c\left(F\left(x_{1 t}\right), F\left(x_{2 t}\right) ; \theta\right)
$$

where $T$ is the sample size. The value $\theta$ which maximizes the log-likelihood is called maximum likelihood estimator $\widehat{\theta}_{\text {MLE }}$. Once the value of $\theta$ is estimated, the bivariate copula is well defined. For maximizing the likelihood function we use the nonparametric estimation of $\theta$ given by Kendall's tau in (1) as an initial approximation to $\widehat{\theta}_{\text {MLE }}$.

# 3 An EDA Based on Copula Functions 

In order to show how a probabilistic model based on copulas can be used in EDAs we proposed an adaptation of the $M I M I C_{C}^{G}[11,13]$ with no Gaussian

Table 1. Bivariate copulas used in this paper

assumption over univariate and bivariate density functions. Next, for completeness sake, we describe the principles of the $M I M I C_{C}^{G}$ learning algorithm.

Given a permutation of the numbers between 1 and $n, \pi=\left(i_{1}, i_{2}, \ldots, i_{n}\right)$ we define a class of density functions, $f_{\pi}(\boldsymbol{x})$ :

$$
f_{\pi}(\boldsymbol{x})=f\left(x_{i_{1}} \mid x_{i_{2}}\right) \cdot f\left(x_{i_{2}} \mid x_{i_{3}}\right) \cdots f\left(x_{i_{n-1}} \mid x_{i_{n}}\right) \cdot f\left(x_{i_{n}}\right)
$$

Our goal is to choose the permutation $\pi$ that minimizes the Kullback-Leibler divergence between the true density function $f(\boldsymbol{x})$ and the proposed density function $f_{\pi}(\boldsymbol{x})$ :

$$
D_{K L}(f(\boldsymbol{x}) \| f_{\pi}(\boldsymbol{x}))=E_{f(\boldsymbol{x})}\left[\log \frac{f(\boldsymbol{x})}{f_{\pi}(\boldsymbol{x})}\right]
$$

It is well known that conditional entropy $H(X \mid Y)$ and mutual information $I(X, Y)$ are related in the following way:

$$
H(X \mid Y)=-I(X, Y)+H(X)
$$

where $H(X)=-E_{f(x)}[\log f(x)]$ denotes the entropy of the continuous random variable $X$ with density $f(x)$. The Kullback-Liebler divergence can be written

as:

$$
\begin{aligned}
D_{K L}(f(\boldsymbol{x}) \| f_{\pi}(\boldsymbol{x})) & =-H(\boldsymbol{X})+\sum_{k=1}^{n-1} H\left(X_{i_{k}} \mid X_{i_{k+1}}\right)+H\left(X_{i_{n}}\right) \\
& =-H(\boldsymbol{X})+\sum_{k=1}^{n} H\left(X_{i_{k}}\right)-\sum_{k=1}^{n-1} I\left(X_{i_{k}}, X_{i_{k+1}}\right)
\end{aligned}
$$

The first two terms in the divergence do not depend on $\pi$. Therefore, minimize the Kullback-Leibler is equivalent to maximize

$$
J_{\pi}(\boldsymbol{X})=\sum_{k=1}^{n-1} I\left(X_{i_{k}}, X_{i_{k+1}}\right)
$$

where

$$
I\left(X_{i_{k}}, X_{i_{k+1}}\right)=E_{f\left(x_{i_{k}}, x_{i_{k+1}}\right)}\left[\log \frac{f\left(x_{i_{k}}, x_{i_{k+1}}\right)}{f\left(x_{i_{k}}\right) \cdot f\left(x_{i_{k+1}}\right)}\right]
$$

According to [6], the optimal permutation $\pi$ is the one that equivalently produces the highest pairwise mutual information with respect to the true distribution. But due to computational efficiency reasons we will employ the greedy algorithm originally proposed by [6] and adapted by [11]. Thus, the MIMIC learning algorithm is based on a dependence test, and this is measured through mutual information. In this paper we will use the following fact (see [5]) between copula entropy and mutual information:

$$
\begin{aligned}
-E_{c\left(u_{1}, u_{2}\right)}\left[\log c\left(u_{1}, u_{2}\right)\right] & =-E_{f\left(x_{1}, x_{2}\right)}\left[\log \frac{f\left(x_{1}, x_{2}\right)}{f\left(x_{1}\right) \cdot f\left(x_{2}\right)}\right] \\
H\left(U_{1}, U_{2}\right) & =-I\left(X_{1}, X_{2}\right)
\end{aligned}
$$

where $U_{1}=F\left(X_{1}\right)$ and $U_{2}=F\left(X_{2}\right)$.
Our proposed EDA uses two different dependence functions: a Frank copula and a Gaussian copula. These copulas are chosen because their dependence parameter have associated all range values of Kendall's tau. This means that negative and positive dependence between the marginals are considered in both copulas. However, they differ in the way they model extreme and centered values [25]. For instance, a Frank copula is mostly appropiate for data that exhibit weak dependence between extreme values and strong dependence between centered values. The proposed EDA estimates the copula entropy between each pair of variables in order to calculate the mutual information. The pair of variables with the largest mutual information are selected as the two first variables of the permutation $\pi$. The following variables of $\pi$ are chosen according to their mutual information with respect to the previous variable. Algorithm 2 shows a straightforward greedy algorithm to find a permutation $\pi$.

```
Algorithm 2. Greedy algorithm to pick a permutation \(\pi\)
    choose \(\left(i_{n}, i_{n-1}\right)=\arg \max _{j \neq k} \widetilde{I}\left(X_{j}, X_{k}\right)\), where \(\widetilde{I}()\) is an estimation of the mutual
    information between two variables.
    choose \(i_{k}=\arg \max _{j} \widetilde{I}\left(X_{i_{k+1}}, X_{j}\right)\), where \(j \neq i_{k+1}, \ldots, i_{n}\) and
    \(k=n-1, n-2, \ldots, 2,1\).
```

For a Gaussian copula there is a direct way to calculate its entropy and mutual information; for a Frank copula we estimate its entropy with a numerical approximation.

Once a permutation $\pi$ is found, generating samples follows the order established by (2). In order to do it, we first sample variable $U_{i_{n}} \sim U(0,1)$ and then we sample variables $U_{i_{k}} \sim C\left(U_{i_{k}} \mid U_{i_{k+1}}=u_{i_{k+1}}\right)$ from conditional copula of $U_{i_{k}}$ given the value of $U_{i_{k+1}}$ for $k=n-1, \ldots, 1$. After that, we use values of $U_{i}$ to find quantiles $X_{i}$ through expression $X_{i}=F_{X_{i}}^{-1}\left(U_{i}\right)$.

It is important to say that, by means of copulas, we can write (2) as

$$
f_{\pi}(\boldsymbol{x})=\prod_{i=1}^{n} f\left(x_{i}\right) \cdot \prod_{k=1}^{n-1} c\left(u_{i_{k}}, u_{i_{k+1}}\right)
$$

where $u_{i_{k}}=F\left(x_{i_{k}}\right)$ and $u_{i_{k+1}}=F\left(x_{i_{k+1}}\right)$. This means that $M I M I C_{C}^{G}$ is a particular copula based EDA with Gaussian copulas $C\left(u_{i_{k}}, u_{i_{k+1}}\right)$ and Gaussian marginals $F\left(x_{i}\right)$, for $k=n-1, \ldots, 1$ and $i=1, \ldots, n$.

In this work we use Beta distributions as marginals. In order to estimate the parameters of the probabilistic model (3), we use the Inference Function for Margins method (IFM) [4]. This method is based on maximum likelihood and estimates first the parameters of marginals and then use them to estimate parameters of copulas. The test problems used in this paper have bounded search space. Each value of variable $X_{i}$ from search space is transformed to a value in $(0,1)$ through a linear transformation. This explains why we use Beta distributions as marginals.

We summarize in Algorithm 3 the proposed approach. The main aspects, such as the estimation of the probabilistic model and the generation of the new population, are shown.

# 4 Experiments 

We use three algorithms in order to optimize five test problems. The algorithms are $M I M I C_{C}^{G}$, copula based EDA using Frank copulas, and copula based EDA using Gaussian copulas. Table 2 shows the definition of the test problems used in the experiments: Ackley, Griewangk, Rastrigin, Rosenbrock, and Sphere functions. We use test problems in 10 dimensions. Each algorithm is run 30 times for each problem. The population size is 100 . The maximum number of evaluations is 300,000 . However, when convergence to a local minimum is detected the run is stopped. Any improvement less than $1 \times 10^{-6}$ in 25 iterations is considered convergence. The goal is to reach the optimum with an error less than $1 \times 10^{-6}$.

```
Algorithm 3. Pseudocode for estimating model and generating new population
    calculate pairwise mutual information using copula entropy
    use greedy algorithm to pick a permutation (Algorithm 2)
    calculate concordance measure Kendall's tau between variables in permutation \(\pi\)
    obtain an initial approximation to the dependence parameter \(\theta_{\tau}\) using relationship
        with Kendall's tau (Table 1)
    estimate marginal and copula parameters using Inference Function for Margins
        Method with \(\theta_{\tau}\) as initial approximation
    simulate \(U_{i_{n}}\) from uniform distribution \(U(0,1)\)
    simulate \(U_{i_{k}}\) from conditional copula \(C\left(U_{i_{k}} \mid U_{i_{k+1}}\right), k=n-1, n-2, \ldots, 2,1\)
    determine \(X_{i}\) using quasi-inverse \(F_{X_{i}}^{-1}\left(U_{i}\right), i=1, \ldots, n\)
```

Table 2. Test functions

# 4.1 Numerical Results 

In Table 3 we report the fitness value reached by the algorithms in all test functions. The information about the number of evaluations required by each algorithm is reported in Table 4.

To properly compare the performance of the algorithms (using the optimum value reached), we conducted a hypothesis test based on a Bootstrap method for the differences between the means of the three comparison pairs, for all test problems. Table 5 shows the confidence interval for the means, and the corresponding p-value.

Table 3. Descriptive fitness results for all test functions

Table 4. Descriptive function evaluations for all test functions

Table 5. Results for the difference between fitness means in each problem. A $95 \%$ interval confidence and a p-value are obtained through a Bootstrap technique.

# 4.2 Discussion 

For the Ackley problem, intervals confidence show signicant differences between $M I M I C_{C}^{G}$ and Gaussian copula against Frank copula. This means that a dependence structure based on Gaussian copula is more adequate than a dependence structure based on Frank copula.

For the Griewangk problem, the algorithm that shows the best behaviour is $M I M I C_{C}^{G}$, closely followed by Frank copula algorithm. In this case, interval confidence between $M I M I C_{C}^{G}$ and Gaussian copula shows that better results are obtained using both Gaussian dependence structure and marginals.

The $M I M I C_{C}^{G}$ is the algorithm that performed best for the Rastrigin problem. For this problem there is statistically significant difference in the mean fitness between the $M I M I C_{C}^{G}$ and the Frank copula algorithms. Although results of Frank copula algorithm are not statistically different of Gaussian copula, is more suitable for this problem to choose a Gaussian structure than a Frank dependence. Respect to marginals distributions we can say something similar between Gaussian copula algorithm and $M I M I C_{C}^{G}$ in the sense that is more adequate to choose Gaussian marginals than Beta marginals.

For the Rosenbrock problem, the intervals confidence shows statistical differences between $M I M I C_{C}^{G}$ and Gaussian copula against Frank copula. In this case, a Frank dependence between marginals is more adecuate than a Gaussian strucuture between marginals. Fitness results between $M I M I C_{C}^{G}$ and Gaussian

copula algorithm show no difference between Gaussian or Beta marginals if structure dependence is modeled by a Gaussian copula.

Finally, the fitness results for Sphere problem indicate that $M I M I C_{C}^{G}$ obtained the global minimum in all the executions. The selection of Gaussian structure and Gaussian marginals is more adecuate for this problem.

Regarding the number of fitness function evaluations, Table 4 the three algorithms performed in a similar way.

# 5 Conclusions 

In this paper we introduce the use of copulas in EDAs. According to numerical experiments the selection of a copula for modeling structure dependence and the selection of marginals distributions can help achieving better fitness results. Although we use the same structure dependence and the same marginals for each algorithm, it is not necessary to do it. Fitness results are the result of the selected structure dependences and marginals.

The three algorithms performed very similar, however, more experiments are necessary with different probabilistic models in order to identify where the copula functions mean a clear advantage to EDAs.
