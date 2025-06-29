# Article 

## Estimation of Distribution Algorithms with Fuzzy Sampling for Stochastic Programming Problems

Abdel-Rahman Hedar ${ }^{1,2,+\circ}$, Amira A. Allam ${ }^{3}$ and Alaa Fahim ${ }^{3}$ (C)<br>1 Department of Computer Science in Jamoum, Umm Al-Qura University, Makkah 25371, Saudi Arabia<br>2 Department of Computer Science, Faculty of Computers \& Information, Assiut University, Assiut 71526, Egypt<br>3 Department of Mathematics, Faculty of Science, Assiut University, Assiut 71516, Egypt; amirahm@science.aun.edu.eg (A.A.A.); alaa@aun.edu.eg (A.F.)<br>* Correspondence: ahahmed@uqu.edu.sa or hedar@aun.edu.eg; Tel.: +966-55-0086-411 or +20-10-0070-4940

Received: 25 August 2020; Accepted: 28 September 2020; Published: 3 October 2020


#### Abstract

Generating practical methods for simulation-based optimization has attracted a great deal of attention recently. In this paper, the estimation of distribution algorithms are used to solve nonlinear continuous optimization problems that contain noise. One common approach to dealing with these problems is to combine sampling methods with optimal search methods. Sampling techniques have a serious problem when the sample size is small, so estimating the objective function values with noise is not accurate in this case. In this research, a new sampling technique is proposed based on fuzzy logic to deal with small sample sizes. Then, simulation-based optimization methods are designed by combining the estimation of distribution algorithms with the proposed sampling technique and other sampling techniques to solve the stochastic programming problems. Moreover, additive versions of the proposed methods are developed to optimize functions without noise in order to evaluate different efficiency levels of the proposed methods. In order to test the performance of the proposed methods, different numerical experiments were carried out using several benchmark test functions. Finally, three real-world applications are considered to assess the performance of the proposed methods.


Keywords: estimation of distribution algorithms; stochastic programming; simulation-based optimization; fuzzy sampling; variable sample path

## 1. Introduction

Several real-world applications can be formulated as continuous optimization problems in a wide range of scientific domains, such as engineering design, medical treatment, supply chain management, finance, and manufacturing [1-9]. Many of these optimization formulations have some sort of uncertainty and their objective functions contain noise [10-13]. Moreover, it is sometimes necessary to deal with complex problems with high nonlinearity and/or dimensionality, and occasionally there is no analytical form for the objective function [14]. Even if the objective functions associated with these types of problems are expressed mathematically, in most cases they are not differentiable. Therefore, classical optimization methods fail to adapt them, and it is impossible to compute their gradient. The situation is much worse when these functions contain high noise levels.

Simulation and optimization has attracted much interest recently, since the output response evaluation of such real-world problems need simulation techniques. Moreover, optimization problems in stochastic environments are realized by combining simulation-based estimation with an optimization process. Therefore, the title "simulation-based optimization" is commonly used instead of "stochastic optimization" $[15,16]$.

Simulation-based optimization is used with certain types of uncertainties to optimize the real-world problem. There are four types of uncertainties discussed in [14]: noise in objective function evaluations; approximation of computationally expensive objective functions with surrogate models; changes or disturbance of design parameters after determining the optimal solution; problems with time-varying objective functions. We consider the first type of uncertainty, where the problem is defined mathematically as follows [17]:

$$
\min _{x \in X}\{f(x)=\mathbb{E}[\hat{\boldsymbol{\alpha}}(x, \omega)]\}
$$

where $f$ is a real-valued function defined on search space $X \subseteq R^{n}$ with objective variables $x \in X$, and $\omega$ is a random variable whose probability density function is $\hat{\alpha}$. Problem (1) is also referred to as the stochastic programming problem in which random variables appear in the formulation of the objective functions.

In spite of the importance of the choice of optimal simulation parameters in improving operation, configuring them well still remains a challenge. Because of the complicated simulation process, the objective function is subjected to different noise levels followed by expensive computational evaluation. These problems are restricted by the following characterizations:

- The complexity and time necessary to compute the objective function values;
- The difficulty of computing the exact gradient of the objective function, as well as its numerical approximation being very expensive;
- The noise values in the objective function.

To deal with these characterizations, global search methods should be invoked to avoid using classical nonlinear programming that fails to solve such problems with multiple local optima.

Recently, the use of artificial intelligence methods in optimization has been of great interest. Metaheuristics play a significant role in both real-life simulations and invoking smart methods [18,19,20,21,22,23,24]. Metaheuristics show strong validity rates across a wide variety of applications. These methods, however, suffer from slow convergence, especially in cases of complex applications, which lead to high computational costs. This slow convergence may be a result of the exploration structures of such methods, while exploring the search space depends on the random structures. On another hand, metaheuristics cannot utilize local information to deduce promising search directions. The estimation of Distribution Algorithms (EDAs) comprise a class of evolutionary computation [25] and has been widely studied in the global optimization field [26,27,28,29]. Compared with traditional Evolutionary Algorithms (EAs), such as Genetic Algorithms (GAs), this type of algorithm has neither crossover nor mutation operators. Instead, an EDA explicitly builds a probabilistic model by learning and sampling the probability distribution of promising solutions in each generation. While building the probabilistic model presents statistical information from the search space, it is used as the guidance of reproduction to find better solutions.

On the other hand, several optimal search techniques have been designed to tackle the stochastic programming problem. Some of these techniques are known as variable-sample methods [30]. The key aspect of the variable-sample approach is to reformulate the stochastic optimization problem in the form of a deterministic one. A differential evolution variant is proposed in [12] equipped with three new algorithmic components, including a central tendency-based mutation, adopted blending crossover, and a new distance-based selection mechanism. To deal with the noise, their algorithm uses non-conventional mutation strategies. In [31], an extension of multi-objective optimization is proposed, based on an differential evolution algorithm to manage the effect of noise in objective functions. Their method applies an adaptive range of the sample size for estimating the fitness values. In [32], instead of using averages, the search policy considers the distribution of noisy samples during the fitness evaluation process. A number of different approaches to deal with noise are presented in [33]. Most sampling methods are based on the use of averages, and this motivates us to use different

sampling techniques. One possible sampling alternative is the use of fuzzy logic, which is an important pillar of computational intelligence. The idea of the fuzzy set was first introduced in [34]; this enabled a member to belong to a set in a partitioned way, as opposed to in a definite way, as stated by classical set theory. In other words, membership can be assigned a value within the $[0,1]$ interval instead of the $\{0,1\}$ set. Over the past four decades, the theory of fuzzy random variables [35] has been developed via a large number of studies in the area of fuzzy stochastic optimization [36,37]. The noisy part of our problem can be considered to be randomness or fuzziness, and it can be understood as a fuzzy stochastic problem, which can be found in the literature [38-42].

In this paper, EDAs are used to solve nonlinear optimization problems that contain noise. The proposed EDA-based methods follow the class of EDAs proposed in [43]. The designed EDA-model is firstly combined with variable-sample methods (SPRS) [30]. Sampling techniques have a serious problem when the sample size is small, so estimating the objective function values with noise is accurate in these cases. Therefore, we propose a new sampling technique based on fuzzy systems to deal with small sample sizes. Another EDA-based method uses the proposed fuzzy sampling technique. Moreover, additive versions of the proposed methods are developed to optimize functions without noise in order to evaluate different efficiency levels of the proposed methods. In order to test the performance of the proposed methods, different numerical experiments were carried out using several benchmark test functions. Moreover, three real-world applications are considered to assess the performance of the proposed methods.

The rest of the paper is structured as follows. In Section 2, we highlight the main structure and techniques for EDAs. The design elements and proposed methods are stated in Section 3. In Section 4, algorithmic implementations of the proposed methods and numerical experiments are discussed. The results for three stochastic programming applications are presented in Section 5. Finally, the paper is concluded in Section 6.

# 2. Estimation of Distribution Algorithms 

EDAs were firstly introduced in [44] as a new population-based method, and have been extensively studied in the field of global optimization [26,44]. Despite the fact that EDAs were firstly proposed for combinatorial optimization, many studies have been performed applying them to continuous optimization. The primary difference between EDAs is the aspect of building the probabilistic model. Generally, in continuous optimization there are two considerable branches: one is based on the Gaussian distribution model [25,26,45-51], and the other on the histogram model [47,52-58]. The first is the most widely used and has been studied extensively. The main steps of general EDAs are stated in Algorithm 1.

## Algorithm 1 Pseudo-code for EDA approach

$1: g \leftarrow 0$
2: $P_{g} \leftarrow$ Generate and evaluate $M$ random individuals (the initial population).
3: repeat
4: $\quad P_{g}^{s} \leftarrow$ Select $m(\leq M)$ individuals from $P_{g}$ according to a selection method.
5: $\quad D_{g}(x)=p_{g}\left(x \mid P_{g}^{s}\right) \leftarrow$ Estimate the joint probability distribution of the selected individuals.
6: $\quad P_{g+1} \leftarrow$ Generate $M$ individuals using $D_{g}(x)$, and evaluate them.
7: $\quad g \leftarrow g+1$.
8: until a stopping criterion is met.

In the case of adapting a Gaussian distribution model $D_{g}(x)$ in Algorithm 1, it has the form of a normal density with a mean $\hat{\mu}$ and a covariance matrix $\Sigma$. The earliest proposed EDAs were based on simple univariate Gaussian distributions, such as the Marginal Distribution Algorithm for continuous domains $\left(U M D A_{c}^{G}\right)$ and Population-Based Incremental Learning for continuous domains

$\left(P B I L_{c}\right)[26,45]$. In these, all variables are taken to be completely independent of each other, and the joint density function is

$$
f_{l}\left(\mathbf{x} ; \boldsymbol{\Theta}^{l}\right)=\prod_{i=1}^{n} f_{l}\left(\mathbf{x}_{i} ; \boldsymbol{\Theta}_{i}^{l}\right)
$$

where $\Theta^{l}$ is a set of local parameters. Such models are simple and easy to implement with a low computational cost, but they fail with high dependent variable problems. For this problem, many EDAs based on multivariate Gaussian models have been proposed, which adapt the conventional maximum likelihood-estimated multivariate Gaussian distribution, such as Normal IDEA [46,47], EMNA $_{\text {global }}$ [26], and EGNA [25,26]. These methods have the same performance, since they are based on the same multivariate Gaussian distribution, and there is no significant difference between them [26]. However, in these methods the dependence between variables is taken, so they have a poor exploitative ability and the computational cost increases exponentially with the problem size [59]. To address this problem, various extensions of these methods have been introduced, which depend on scaling $\Sigma$ after estimating the maximum likelihood according to certain criteria to improve the exploration quality. This has been done in methods such as EEDA [48], SDR-AVS-IDEA [50], and CT-AVS-IDEA [49].

The EDA with Model Complexity Control (EDA-MCC) method was introduced to control the high complexity of the multivariate Gaussian model without losing the dependence between variables [43]. Since the univariate Gaussian model has a simple structure and limited computational cost, it has difficulty solving nonseparable problems. On other hand, the multivariate Gaussian model can solve nonseparable problems, but it usually has difficulty as a result of its complexity and cost. In the EDA-MCC method, the advantages of the univariate and multivariate Gaussian models are combined according to certain criterion and by applying two main strategies:

- Weakly Dependent Variable Identification (WI). In this strategy, the correlation coefficients between variables are calculated to measure how much they are dependent. This means that the observed linear dependencies are measured by their correlation coefficient with each other, as follows:

$$
\operatorname{corr}\left(x_{i}, x_{j}\right)=\frac{\operatorname{cov}\left(x_{i}, x_{j}\right)}{\sigma_{i} \sigma_{j}}
$$

where $\operatorname{corr}\left(x_{i}, x_{j}\right)$ is the linear correlation coefficient between $x_{i}$ and $x_{j}, \operatorname{cov}\left(x_{i}, x_{j}\right)$ is their covariance, $\sigma_{i}$ and $\sigma_{j}$ are their standard deviations, respectively, and $i, j=1, \ldots, n$. Briefly, all variables are divided into two sets: $W$ and $S$, where $W$ is the set of weakly dependence variables, and $S$ is the set of strong dependent variables. These variable sets are defined as follows:

$$
\begin{aligned}
W & =\left\{x_{i}:\left|\operatorname{corr}\left(x_{i}, x_{j}\right)\right| \leq \theta, \quad \forall j=1, \ldots, n, j \neq i, i=1, \ldots, n\right\} \\
S & =\left\{x_{i}: x_{i} \notin W, i=1, \ldots, n\right\}
\end{aligned}
$$

where $\theta$ is a threshold $(0 \leq \theta \leq 1)$, and this reflects how much the user trusts the univariate model in the problem. Algorithm 2 shows the main flow of the WI strategy.

# Algorithm 2 Pseudo-code for WI 

1: Use $m$ individuals to calculate the correlation matrix $C=\left(c_{i j}\right)$, where $c_{i j}=\operatorname{corr}\left(x_{i}, x_{j}\right), i, j=1, \ldots, n$.
2: Use $C$ to construct $W$ and $S$ as defined in Equations (4) and (5), respectively.
3: Estimate a univariate model for $W$ based on the $m$ selected individuals.

- Subspace Modeling (SM). This strategy is applied on the $S$ set. The performance of the multivariate model needs a large population size and the complexity of computations increases frequently. The SM strategy is applied on the variables set in $S$, which preferably has a limited number of variables. If the size $|S|$ of set $S$ is not limited, then the population points are projected to several subspaces of the $n$ dimensional search space. Then, a multivariate model can be built for each subspace, which means that the dependence is considered only between variables in the same subspace. The main steps of the SM strategy are explained in Algorithm 3.

Algorithm 3 Pseudo-code for SM

1: Construct $S$ as in Equation (5).
2: Randomly partition $S$ into $\lceil|S| / c\rceil$ nonintersected subsets: $S_{1}, S_{2}, \ldots S_{\lceil|S| / c\rceil}$.
3: Estimate a multivariate model for each subset based on $m$ selected individuals.

Parameter $c$ is a predefined one that controls the number of the subspaces, where $(1 \leq c \leq n)$.
After carrying out the WI and SM strategies, the final joint probability distribution function (pdf) has the following form:

$$
f\left(\mathbf{x}_{i}\right)=\prod_{x_{i} \in W} \phi_{i}\left(\mathbf{x}_{\mathbf{i}}\right) \cdot \prod_{k=1}^{\lceil|S| / c\rceil} \psi_{k}\left(\mathbf{s}_{\mathbf{k}}\right)
$$

where $\phi_{i}(\cdot)$ is the univariate pdf of variable $x_{i} \in W$, and $\psi_{k}(\cdot)$ is the multivariate pdf of the variables in $S_{k}$. The main steps of the EDA-MCC method are illustrated in Algorithm 4.

# Algorithm 4 Pseudo-code for EDA-MCC 

1: Generate an initial population $P$ of $M$ individuals.
2: repeat
3: Select $m \leq M$ individuals from $P$.
4: Call Algorithms 2 and 3 sequentially to build a model, as in Equation (6).
5: Generate new individuals $P^{\prime}$ : Variable values of an individual are generated independently from $\phi_{i}(\cdot)$ and $\psi_{k}(\cdot)$. Then, combine all generated variable values together to produce an individual.
6: $P \leftarrow P+P^{\prime}$.
7: until a stopping criterion is met.

## 3. Estimation of Distribution Algorithms for Simulation-Based Optimization

In this section, new EDA-based methods are proposed in order to deal with nonlinear and stochastic programming problems. Moreover, a new sampling technique is introduced based on fuzzy logic. Before presenting the proposed EDA-based methods, we illustrate the sampling techniques used to deal with noise.

### 3.1. Sampling Techniques

Two different sampling techniques were used to build two EDA-based methods for stochastic programming problems. The first sampling technique is the variable sampling path [30], while the other is the proposed fuzzy sampling technique. The details of these sampling techniques are illustrated in the following sections.

### 3.1.1. Variable Sampling Path

The variable-sample (VS) method [30] is defined as a class of methods that uses the Monte Carlo simulation to solve the stochastic programming problem. This sampling technique invokes several simulations to estimate the objective function value at a single solution. Search methods can gain benefits from such sampling to convert the stochastic programming problem into a nonlinear

programming one. Sampling Pure Random Search (SPRS) [30] is a random search algorithm that uses the VS process. The average of variable-size samples replaces the objective function value of the SPRS algorithm in each objective function evaluation call. The SPRS algorithm can converge, under certain conditions, to an optimal local solution. The formal SPRS algorithm is shown in Algorithm 5.

# Algorithm 5 Sampling Pure Random Search (SPRS) Algorithm 

1: Generate a point $x_{0} \in X$ at random, set an initial sample size $N_{0}$, and $k:=0$.
2: Generate a point $y \in X$ at random.
3: Generate a sample $\omega_{1}^{k}, \ldots, \omega_{N_{k}}^{k}$.
4: Compute $\hat{f}\left(x_{k}\right), \hat{f}(y)$ using the following formula: $\hat{f}(x)=\frac{\tilde{\alpha}\left(x, \omega_{1}^{k}\right)+\ldots+\tilde{\alpha}\left(x, \omega_{N_{k}}^{k}\right)}{N_{k}}$.
5: If $\hat{f}(y)<\tilde{f}\left(x_{k}\right)$, then set $x_{k+1}:=y$. Otherwise, set $x_{k+1}:=x_{k}$.
6: If the stopping criteria is satisfied, stop. Otherwise, update $N_{k}$, set $k:=k+1$ and go to Step 2.

### 3.1.2. Fuzzy Sampling

The basic study of possible definitions of a fuzzy number is proposed in [60]. In the case of a valuation (Boolean) set, the membership of any element $x \in X$ to the subset $A(\subseteq X)$ is given by

$$
\mu_{A}(x)= \begin{cases}1 & \text { iff } x \in A \\ 0 & \text { iff } x \notin A\end{cases}
$$

In the fuzzy set, the membership values fall in the real interval $[0,1]$, as in [34], and $\mu_{A}$ measures the degree of membership of an element $x$ in $X$-i.e., $\mu_{A}(x): X \rightarrow[0,1]$. Many definitions have been introduced for the membership function $\mu$ depending on the problem's properties [39,61].

The average sampling in Algorithm 5 works well whenever the sample size $N$ is sufficiently large. However, it fails to estimate the objective function values with small sample sizes, especially in the early stages of the search process, and promising solutions may be lost. Because of this, we proposed a new sampling technique based on fuzzy sets for the better estimation of function values even with relatively small sample sizes. Specifically, if our target is to estimate $\hat{f}(x)$ using a sample of size $N$; $\tilde{\alpha}\left(x, \omega_{1}\right), \ldots, \tilde{\alpha}\left(x, \omega_{N}\right)$. The proposed fuzzy sampling technique defines that estimation as

$$
\hat{f}(x)=\frac{\mu_{1} \tilde{\alpha}\left(x, \omega_{1}\right)+\ldots+\mu_{N} \tilde{\alpha}\left(x, \omega_{N}\right)}{\sum_{i=1}^{N} \mu_{i}}
$$

where $\mu_{i}$ is the associated membership function for every simulated value $\tilde{\alpha}\left(x, \omega_{i}\right)$, and $i=1, \ldots, N$.
In order to compute the membership values, three featured sample values are stored. The first two are the maximum value $\tilde{\alpha}_{\max }$ and the minimum value $\tilde{\alpha}_{\min }$ among the current sample values; $\tilde{\alpha}\left(x, \omega_{1}\right), \ldots, \tilde{\alpha}\left(x, \omega_{N}\right)$. The last feature value is called the guide value $\tilde{\alpha}_{G}$ and is selected within the interval $\left[\tilde{\alpha}_{\min }, \tilde{\alpha}_{\max }\right]$. Then, the membership values $\mu_{i}, i=1, \ldots, N$, can be defined as in the following formula:

$$
\mu_{i}= \begin{cases}1-\frac{\tilde{\alpha}_{G}-\tilde{\alpha}_{i}}{\rho}, & \tilde{\alpha}_{G}-\rho \leq \tilde{\alpha}_{i} \leq \tilde{\alpha}_{G} \\ 1-\frac{\tilde{\alpha}_{i}-\tilde{\alpha}_{G}}{\rho}, & \tilde{\alpha}_{G}<\tilde{\alpha}_{i} \leq \tilde{\alpha}_{G}+\rho \\ 0, & \tilde{\alpha}_{i} \leq \tilde{\alpha}_{G}-\rho, \text { or } \tilde{\alpha}_{i} \geq \tilde{\alpha}_{G}+\rho\end{cases}
$$

where $\rho$ is a radius value set based on the sample size $N$. The calculation of the membership values takes into consideration two main points:

- $\mu_{i}$ is set to take values between 0 and 1 : its value is near to 1 when the sample values are close to $\tilde{\alpha}_{G}$, and it is reduced and reaches 0 when it is far from this value at the end of the radius $\rho$, which is initialized to be $\ll\left(\tilde{\alpha}_{\max }-\tilde{\alpha}_{\min }\right)$ if the sample size is small;
- While the sample size $N$ is increased during the search process, the values of $\mu_{i}$ become close to 1 since the radius $\rho$ is expanded to cover the whole interval $\left[\tilde{\alpha}_{\min }, \tilde{\alpha}_{\max }\right]$.

Algorithm 6 contains the main steps of the proposed Fuzzy Sampling Random Search (FSRS) method to deal with the objective function noise.

```
Algorithm 6 Fuzzy Sampling Random Search (FSRS)
    Generate a point \(x_{0} \in X\) at random; set an initial sample size \(N_{0}\), and \(k:=0\).
    Generate a point \(y \in X\) at random.
    Generate a sample \(\omega_{1}^{k}, \ldots, \omega_{N_{k}}^{k}\).
    for \(i=1, \ldots, N_{k}\), do
        Compute \(\mathfrak{F}\left(x_{k}, \omega_{i}^{k}\right)\), and \(\mathfrak{F}\left(y, \omega_{i}^{k}\right)\).
    end for
    Sort the sample values to set \(\mathfrak{F}_{\text {max }}\) and \(\mathfrak{F}_{\text {min }}\).
    Set \(\rho=\alpha\left(\mathfrak{F}_{\max }-\mathfrak{F}_{\min }\right)\), where \(\alpha\) is a control parameter depends on \(N_{k}\).
    Choose a guide value \(\mathfrak{F}_{G} \in\left[\mathfrak{F}_{\min }, \mathfrak{F}_{\max }\right]\).
    for \(i=1, \ldots, N_{k}\), do
        Compute \(\mu_{i}\) according to Equation (8).
    end for
    Evaluate \(\hat{f}\left(x_{k}\right)\) and \(\hat{f}(y)\) using Equation (7).
    If \(\hat{f}(y)<\hat{f}\left(x_{k}\right)\), then set \(x_{k+1}:=y\). Otherwise, set \(x_{k+1}:=x_{k}\).
    If the stopping criteria is satisfied, stop. Otherwise, update \(N_{k}\), set \(k:=k+1\) and go to Step 2.

It is worth mentioning that several alternatives have been tested in our experiments to find the best choice for the $\mathfrak{F}_{G}$. The conclusion of those experiments is that the median value of $\mathfrak{F}\left(x, \omega_{1}\right), \ldots, \mathfrak{F}\left(x, \omega_{N}\right)$ gives the best algorithmic results.

# 3.2. EDA-Based Methods for Simulation-Based Optimization 

The proposed EDA-based methods are a combination of the EDA-MCC method, which is stated in Algorithm 4, and different sampling techniques for nonlinear and stochastic programming problems. In our proposal to build the EDA model (6), we used the UMDA ${ }_{c}^{G}$ model as a univariate Gaussian model [26], in which the joint density function is defined as

$$
\phi(x)=\prod_{i=1}^{n} \phi_{N}\left(\mathbf{x}_{\mathbf{i}} ; \mu_{i}, \sigma_{i}^{2}\right)=\prod_{i=1}^{n} \frac{1}{\sigma_{i} \sqrt{2 \pi}} e^{-\left(x_{i}-\mu_{i}\right)^{2} / 2 \sigma_{i}^{2}}
$$

where $\mu=\left(\mu_{1}, \ldots, \mu_{n}\right)$ is the mean and $\sigma^{2}=\left(\sigma_{1}^{2}, \ldots, \sigma_{n}^{2}\right)$ is the variance. Furthermore, the EEDA model [48] was used as a multivariate Gaussian model which is an extension of the EMNA global model [26]. The multivariate joint density function is defined as

$$
\psi(x)=\psi_{N}\left(\overline{\mathbf{x}}_{\mathbf{i}} ; \bar{\mu}, \Sigma\right)=\frac{1}{(2 \pi)^{N / 2}|\Sigma|^{1 / 2}} e^{-(\bar{x}-\bar{\mu})^{T} \Sigma^{-1}(\bar{x}-\bar{\mu}) / 2}
$$

where $\Sigma$ is the covariance matrix. In the EEDA method, the covariance matrix is redefined in each iteration by expanding the original matrix in the direction of the eigenvector corresponding to the smallest eigenvalue. In other words, the minimum eigenvalue is reset to the value of the maximum eigenvalue. Algorithm 7 illustrates the main steps of the proposed EDA-based method.

```
Algorithm 7 EDA for Simulation-Based Optimization
    Create an initial population \(P_{0}\) of \(M\) individuals.
    Estimate the objective function values at \(P_{0}\) individuals.
    Set the generation counter \(g:=0\).
    repeat
        Select the best \(m \leq M\) individuals \(P_{g}^{s}\).
        Compute the variable sets \(W\) and \(S\) using the WI strategy in Algorithm 2.
        Estimate joint density function of \(W\) variables using Equation (9).
        Apply the SM strategy using set \(S\) as in Algorithm 3.
        Estimate the multivariate joint density function for each variable subset using Equation (10).
        Generate new \((M-L)\) individuals \(P_{g}^{C}\) by using Equations (9) and (10) independently.
        Estimate the objective function values at \(P_{g}^{C}\) individuals.
        Set \(P_{g+1}=P_{g}^{C} \cup P_{g}^{s}\).
        Apply a local search to each individual in \(P_{g+1}\).
        Set \(g:=g+1\).
    until the stopping criterion is met.
```

Different EDA-based methods can be generated from Algorithm 7 according to the technique used to estimate the objective function values in Steps 2 and 11. Therefore, we have three versions:

- ASEDA: The Average Sampling EDA if the average sampling is used to estimate the objective function values, as in Algorithm 5;
- FSEDA: The Fuzzy Sampling EDA if the fuzzy sampling is used to estimate the objective function values, as in Algorithm 6;
- DEDA: The deterministic EDA if the objective function has no noise and its value can be directly calculated without simulation.


# 4. Numerical Experiments 

The proposed methods were programmed in MATLAB (see the Supplementary Materials), and tested using different benchmark test functions to prove their efficiency. Four test sets are used to discuss the proposed method results:

- Set A: Contains 14 classical test functions with different dimensions from 2 to $30[10,62]$, shown in Appendix A;
- Set B: Contains 40 classical test functions with different dimensions from 2 to $30[10,62]$, shown in Appendix B;
- Set C: Contains seven test functions $\left(f_{1}-f_{7}\right)$ with Gaussian noise $(\mu=0, \sigma=10)$, except $f_{6}$ which contains uniform random noise $U(-17.32,17.32)$. The function dimensions vary from 2 to 50 , shown in Appendix C;
- Set D: Contains 13 test functions $\left(g_{1}-g_{13}\right)$ with Gaussian noise $(\mu=0, \sigma=0.2)$. Each function is used with two dimensions- 30 and 100 -shown in Appendix D.

The versions of the main proposed method were tested using these test sets. Specifically, the DEDA method was tested with Test Sets A and B, while the ASEDA and FSEDA methods were tested with Test Sets C and D. Beside these test sets, we discuss three real-world applications in the next section. To assess the statistical differences between the compared results, the nonparametric Wilcoxon rank-sum test [63-67] was used. This test obtained the following statistical measures:

- The associated $p$-value;
- The ranks $R^{+}$and $R^{-}$which are computed as follows:

$$
\begin{aligned}
R^{+} & =\sum_{d_{i}>0} \operatorname{rank}\left(d_{i}\right)+\frac{1}{2} \sum_{d_{i}=0} \operatorname{rank}\left(d_{i}\right) \\
R^{-} & =\sum_{d_{i}<0} \operatorname{rank}\left(d_{i}\right)+\frac{1}{2} \sum_{d_{i}=0} \operatorname{rank}\left(d_{i}\right)
\end{aligned}
$$

where $d_{i}$ is the difference between the $i$-th out of $r$ results of the compared methods. Before discussing the main results, we illustrate the parameter tuning and setting.

# 4.1. Parameter Tuning and Setting 

In order to complete the description of our algorithms, the parameters are discussed in this section. Table 1 contains the definitions of all parameters and their best values. Some numerical experiments were tested to find the suitable values of these parameters. Parameter values were set to be as independent from the problem as possible. Despite the the theoretical part of EDAs parameters being studied before-for example, in [27]-the number of population size $R$ values is still a main factor that varies from problem to problem. In fact, trading off between the population size and the number of generation is a main issue.

Before choosing a suitable value for parameter $R$, a comparison between different values of $R=100, R=200$, and $R=500$ was applied for both types of problems (global optimization, simulation-based optimization). The number of function evaluations was set to be fixed at 500,000 in all of these experiments. Table 2 shows that for the global optimization problem, increasing the population size does not have a positive effect on most problems. This means that the search process is more qualified with an extra number of generations. For the simulation-based optimization problem, Figure 1 shows an almost identical performance when applying different values of $R=100, R=200$, $R=500$, and $R=1000$. Some functions need more exploration of the search space (increase $R$ ), such as $f_{3}$ and $f_{5}$, but $R=100$ is still the best choice for rest of the functions.

For parameters $m$ and $L$, which follow parameter $R$, setting higher values yields higher computational times without any significant improvement. For sample size parameters, the settings follow the recommended values in $[10,13]$.

Table 1. Parameters definition and values.

Table 2. Average errors using different settings of parameter $R$ for global optimization problems using Test Set A.

![img-0.jpeg](img-0.jpeg)

Figure 1. Average errors using different settings of parameter $R$ for simulation-based optimization problems using Test Set C.

# 4.2. Global Optimization Results 

The proposed DEDA algorithm was tested to solve nonlinear programming problems using the test functions in Set A and Set B. These test functions have diverse characteristics to assess various difficulties that occur in global optimization problems. For all test results for global optimizations, the records were obtained over 100 independent runs with a maximum function evaluation of 20,000. First, Table 3 shows average errors (Av.) and standard deviation (Std.) obtained by the DEDA method using Test Set B. It reached the global optima within error gaps less than $10^{-3}$ for 25 out of 40 test functions.

Table 3. The deterministic Estimation of Distribution Algorithm (DEDA) results using Test Set B.

The DEDA results were compared with those of the scatter search methods introduced in [10]:

- Scatter Search (SS): The standard scatter search method.
- Directed Scatter Search (DSS): An SS-based method directed by a memory-based element called gene matrix in order to increase the search diversity.

Table 4 shows the average errors (Av.), standard deviation (Std.) and success rates (Suc.) obtained by each method using Test Set A. In general, the DEDA obtained lower average errors and higher success rates than the other two methods, as can be seen in the ranks $R^{+}$and $R^{-}$in Table 5. However, there was no significant difference between these methods according to the $p$-values obtained by the Wilcoxon rank-sum test, as shown in Table 5.

Table 4. Compared results of the DEDA, SS, and DSS methods using Test Set A.
Table 5. Wilcoxon rank-sum test for the results of Table 4.

# 4.3. Fuzzy Sampling Performance 

The FSRS (Algorithm 6) results were compared with those of the standard SPRS (Algorithm 5) in high noise-i.e., $N\left(0,10^{2}\right)$. These results are illustrated in Figure 2 which shows the average $\hat{f}(x)$ of the best obtained solutions by each method for every test function. Tested functions with different dimensions were selected from Test Set C. The sample size varies from 10 to 1000. The results shown in Figure 2 reveal that the performance of the FSRS algorithm is consistently better than that of the SPRS algorithm for small number values $N$. There is no significant difference between them with higher sample sizes. Therefore, the proposed fuzzy sampling could efficiently deal with a wide range of noise, especially with small sample sizes.
![img-1.jpeg](img-1.jpeg)

Figure 2. The performance of Fuzzy Sampling Random Search (FSRS) and SPRA with different sample sizes.

### 4.4. Simulation-Based Optimization Results

In this section, we give more details about the experimental results of the comparison between the proposed FSEDA and ASEDA algorithms. Then, the results of the best method are compared with other benchmark methods. Table 6 shows the best and average errors obtained by the two methods using the seven test functions in Set C. The FSEDA method could obtain better solutions than the other

method for six out of seven test functions, and its average solutions are better in five out of seven test functions. Therefore, we used the FSEDA results to compare with the other benchmark methods.

Table 6. The best and average errors of the the Average Sampling Estimation of Distribution Algorithm (ASEDA) and FSDEA methods using Test Set C.

Two main comparison experiments are presented to test the FSEDA performance against some benchmark methods. The first experiment used Test Set C to make the comparisons with methods in $[10,68]$, while the other experiment used Test Set D with methods in $[12,13]$.

Table 7 shows the best and the average errors obtained by the proposed FSEDA method and the following evolutionary-based methods:

- DESSP: Directed evolution strategies for stochastic programming [10].
- DSSSP: Directed scatter search for stochastic programming $[10,68]$.

The results were obtained over 25 independent runs with maximum function evaluations equal to 500,000 . Moreover, Table 8 shows the statistical measures of the results compared in Table 7. These statistical measures reveal that there is no significant difference between the proposed method and the other two methods in terms of the best solution found or the average errors. However, for high dimensional function $f_{7}$, the proposed method demonstrated the best performance.

Table 7. The best and average errors of the FSDEA method compared with the DESSP and DSSSP methods.

Table 8. Wilcoxon rank-sum test for the results of Table 7.

The other comparison experiment compared the FSEDA results with those of the following benchmark methods [12,13] using Test Set D with dimensions 30 and 100.

- EDA-MMSS: An EDA-based method with a modified sampling search mechanism called min-max sampling [13].
- DE/rand/1: A modified version of the standard differential evolution of DE/rand/1/bin algorithm [12].
- jDE: An adaptive differential evolution method [69].
- GADS: Genetic algorithm with duration sizing [70].
- DERSFTS: Differential evolution with randomized scale factor and threshold-based selection [71].
- OBDE: Opposition-based differential evolution [72].
- NADE: Noise analysis differential evolution [73].
- MUDE: Memetic differential evolution for noisy optimization [74].
- MDE-DS: Modified differential evolution with a distance-based selection [12].
- NRDE: Noise resilient differential evolution [75].

The average errors over 30 independent runs are reported in the following tables, with computational budgets of 100,000 and 300,000 function evaluations for dimensions 30 and 100, respectively. Table 9 displays the average errors for test functions with $n=30$, and the statistical measures of these results are presented in Table 10. The FSEDA outperforms seven out of nine methods in terms of obtaining better average solutions.

Table 9. Average errors obtained by the compared methods for Test Set D with $n=30$, and 100,000 maximum function evaluations.

Table 10. Wilcoxon rank-sum test for the results of Table 9.
The results of test functions with $n=100$ are shown in Table 11. Their statistical measures are reported in Table 12. The FSEDA method outperformed six out of nine methods used in this comparison in terms of average solution quality.

Table 11. Average errors obtained by the compared methods for Test Set D with $n=100$, and 300,000 maximum function evaluations.
Table 12. Wilcoxon rank-sum test for the results of Table 11.
# 5. Stochastic Programming Applications 

In this section, we investigate the strength of the proposed methods in solving real-world problems. Therefore, the FSEDA and ASEDA methods attempted to find the best solutions for three different real stochastic programming applications:

- The product mix (PROD-MIX) problem [76,77];
- The modified production planning Kall and Wallace (KANDW3) problem [77,78];
- The two-stage optimal capacity investment Louveaux and Smeers (LANDS) problem [77,79].

These applications are constrained stochastic programming problems. Therefore, the penalty methodology [80] was used to transform these constrained problems into a series of unconstrained ones. These unconstrained solutions are assumed to converge to the solutions of the corresponding constrained problem.

To solve these problems, the proposed EDA-based methods were used with the parameters in Table 1, except the population size, which was adjusted to $R=300$. The penalty parameter was set to $\lambda=1000$. The algorithms were terminated when they reached 30,000 function evaluations.

### 5.1. PROD-MIX Problem

This problem assumes that a furniture shop has two workstations $(j=1,2)$; the first workstation is for carpentry and the other for finishing. The furniture shop has four products $(i=1, \ldots, 4)$. Each product $i$ consumes a certain number of man-hours $t_{i j}$ at $j$ a workstation, with man-hours $h_{j}$ being limited at each workstation $j$. The shop should purchase man-hours $v_{j}$ from outside the workstation $j$ if the man-hours exceed the limit. Each product earns a certain profit $c_{i}$. The most important aspect is to maximize the total profit of our shop and minimize the cost of purchased man-hours.

### 5.1.1. The Mathematical Formulation of the PROD-MIX Problem

The formal description of the PROD-MIX Problem can be defined as follows [76,77]. The required values for parameters and constants are also expressed.
$i \quad$ The product class $(i=1, \ldots, 4)$.
$j \quad$ The workstation $(j=1,2)$.
$x_{i} \quad$ The quantities of product (decision variables).
$v_{j} \quad$ The outside purchased man-hours for workstation $j$.
$c_{i} \quad$ The profit per product unit at class $i, c=[12.0,20.0,18.0,40.0]$.
$q_{j} \quad$ The man-hour cost for workstation $j, q=[5.0,10.0]$.
$t_{i j} \quad$ Random man-hours at workstation $j$ per unit of product class $i$,
$t=\left[\begin{array}{llll}U(3.5,4.5) & U(8.0,10.0) & U(6.0,8.0) & U(9.0,11.0) \\ U(0.8,1.2) & U(0.8,1.2) & U(2.5,3.5) & U(36.0,44.0)\end{array}\right]$.
$h_{i} \quad$ Random available man-hours at $j$ workstation,
$h=[N(6000,100), N(4000,50)]$.
Therefore, the object function for the PROD-MIX Problem can be expressed as

$$
\begin{gathered}
f(x, v)=\max \left(\sum_{i} c_{i} x_{i}-\mathbb{E}\left[\sum_{j} q_{j} v_{j}\right]\right) \\
\text { s.t. } \begin{aligned}
\sum_{i} t_{i j} x_{i} & <h_{j}+v_{j}, \forall j \\
x_{i}, v_{i} & \geq 0, \forall i, j
\end{aligned}
\end{gathered}
$$

# 5.1.2. Results of the PROD-MIX Problem 

The FSEDA method found a new solution with value $f_{\max }=20,580.99$, and the decision variable values $x_{\max }=(1356.2,17.4,88.1,38.1)$. The best known value for this problem is $f^{*}=17,730.3,[76,77]$. Figure 3 shows the comparison between the performance of the ASEDA and FSEDA methods. This figure shows that the FSEDA method demonstrated the best performance in terms of reaching the optimal solution.
![img-2.jpeg](img-2.jpeg)

Figure 3. The FSEDA and ASEDA performance for the product mix (PROD-MIX) Problem.

### 5.2. The KANDW3 Problem

In the KANDW3 Problem [77,78], a refinery makes J different products by blending I raw materials. The refinery produces the quantities $x_{i t}$ of the raw material $i$ in period $t$ with cost $c_{i}$ to meet the demands $d_{j t}$. Each product $j$ requires the raw material $i$ to be stored in $a_{i j}$. If the refinery does not satisfy the demands in period $t$, it should outsource $y$ the product with cost $h$. The main objective is to satisfy the demand completely with a minimum cost.

### 5.2.1. The Mathematical Formulation of the KANDW3 Problem

The formal description of the KANDW3 Problem can be defined as follows [77,78]. The required values for parameters and constants are also expressed.
$i \quad$ The materials $(i=1, \ldots, I)$.
$j \quad$ The products $(j=1, \ldots, J)$.
$t \quad$ The time periods $(t=1, \ldots, T)$.
$x_{i t} \quad$ The quantity of material $i$ in the period $t$ (decision variables).
$y_{j t} \quad$ The quantity of outsourced product $j$ in period $t$.
$c_{i} \quad$ The cost of raw material $i, c=[2.0,3.0]$.
$a_{i j} \quad$ The amount of raw material $i$ to a unit of product $j$,
$a=\left[\begin{array}{cc}2.0 & 6.0 \\ 3.0 & 3.4\end{array}\right]$.
$h_{j t} \quad$ The cost of outsourced product $j$ in period time $t$,
$h=\left[\begin{array}{cc}7.0 & 10.0 \\ 12.0 & 15.0\end{array}\right]$.
$b \quad$ The capacity of the inventory, $b=50$.
$d_{j t} \quad$ Random demands of product $j$ in period $t$.

The values for demands can be obtained from the Figure 4. The object function for the KANDW3 Problem $[77,78]$ can be expressed as

$$
f(x, v)=\min \left(\sum_{i, j} c_{i} x_{i t}+\mathbb{E}\left[\sum_{j, i} h_{j t} y_{j t}\right]\right)
$$

s.t.

$$
\begin{aligned}
\sum_{i, t} x_{i t} & \leq b \\
v \sum_{i} a_{i j} x_{i t}+y_{j t} & \geq d_{j t}, \forall j, t \\
x_{i t}, y_{j t} & \geq 0, \forall i, j, t
\end{aligned}
$$

stage 1
![img-3.jpeg](img-3.jpeg)

Figure 4. Demand values in the The modified production planning Kall and Wallace (KANDW3) Problem.

# 5.2.2. Results of KANDW3 Problem 

The FSEDA method found the objective function value $f_{\min }=1558.9$, with the decision variable values $x_{\min }=(2,13,10,20)$. The best known value for the KANDW3 Problem is $f^{*}=2613$, as mentioned in [78]. Therefore, the proposed method found a new minimal value for the KANDW3 Problem. The comparison between the ASEDA and FSEDA methods is shown in Figure 5. In this figure, the FSEDA method provided better solutions as compared to the ASEDA method.

![img-4.jpeg](img-4.jpeg)

Figure 5. The FSEDA and ASEDA performance for the KANDW3 Problem.

# 5.3. The LANDS Problem 

Power plants are the key issue in the LANDS Problem [77,79]. Assume that there are four types of power plants which can be operated by three different modes to meet the electricity demands; the operating level $y_{i j}$ of power plant $i$ in mode $j$ to satisfy the demands $d_{j}$ with the cost $h_{i j}$. The budget $b$ is considered as a constraint which limits the total cost. The main objective is to determine the optimal capacity investment $x_{i}$ in the power plant $i$.

### 5.3.1. The Mathematical Formulation of the LANDS Problem

The formal description of the LANDS Problem can be defined as follows [77,79]. The required values for parameters and constants are also expressed.
$i \quad$ The power plant type $(i=1, \ldots, 4)$.
$j \quad$ The operating mode $(j=1, \ldots, 3)$.
$x_{i} \quad$ The capacity of power plant $i$ (decision variable).
$y_{i j} \quad$ The operating level of power plant $i$ in mode $j$.
$c_{i} \quad$ The unit cost of capacity installed for plant type $i, c=[10.0,7.0,16.0,6.0]$.
$h_{i j} \quad$ The unit cost of operating level of power plant $i$ in mode $j$,
$h=\left[\begin{array}{lll}40.0 & 24.0 & 4.0 \\ 45.0 & 27.0 & 4.5 \\ 32.0 & 19.2 & 3.2 \\ 55.0 & 33.0 & 5.5\end{array}\right]$.
$m \quad$ The minimum total installed capacity $m=12.0$.
$b \quad$ The available budget for capacity installment, $b=120.0$.
$d_{j} \quad$ Random power demands in mode $j, d=[c, 3.0,2.0]$, where $c$ has values $3.0,5.0$, or 7.0 with probability $0.3,0.4$, and 0.3 , respectively.

Therefore, the object function for the LANDS Problem [77,79] can be expressed as

$$
f(x, v)=\min \left(\sum_{i, l} c_{i} x_{i}+\mathbb{E}\left[\sum_{i, j} h_{i j} y_{i j}\right]\right)
$$

$$
\begin{aligned}
\text { s.t. } \quad \sum_{i} x_{i} & \geq m \\
\sum_{i} c_{i} x_{i} & \leq b \\
\sum_{j} y_{i j} & \leq x_{i}, \forall i \\
\sum_{i} y_{i j} & \geq \bar{d}_{j}, \forall j \\
x_{i}, y_{i j} & \geq 0 . \forall i, j
\end{aligned}
$$

# 5.3.2. Results of the LANDS Problem 

The objective function value $f_{\min }=413.616$ was obtained by the FSEDA method with the decision variables $x_{\min }=(2.6,2.7,2.6,4.3)$. The best known function value for this problem is $f^{*}=381.85$, which is presented in [79]. Figure 6 presents the comparison between the FSEDA and ASEDA performance for the LANDS Problem. In Figure 6, the FSEDA method reached the best solution faster than the ASEDA method.
![img-5.jpeg](img-5.jpeg)

Figure 6. The FSEDA and ASEDA performance for the two-stage optimal capacity investment Louveaux and Smeers (LANDS) Problem.

## 6. Conclusions

In this paper, four new algorithms are presented to deal with various problems and applications. The first method is called Fuzzy Sampling Random Search (FSRS), which is a new sampling search technique. The other three methods are EDA-based methods which are denoted by DEDA, ASEDA, and FSEDA. The DEDA method is proposed to deal with deterministic nonlinear programming problems. While the ASEDA and FSEDA methods are designed with average and fuzzy sampling techniques, respectively, to deal with stochastic programming problems. Several sets of benchmark tests involving nonlinear and stochastic programming problems were tested, and the results demonstrate the promising performance of the novel methods. In fact, using a fuzzy membership function is very efficient in containing the anomalous function simulations resulting from small sample sizes. The numerical simulations show that the ASEDA and FSEDA methods are promising simulation-based optimization tools. Moreover, the FSEDA method obtained new optimal solutions for two out of three real-world applications. Finally, the experimental analysis of the proposed methods has enabled us to suggest extending the present work using different metaheuristics to solve simulation-based optimization problems in both continuous and combinatorial domains.

Supplementary Materials: The following are available at http://www.mdpi.com/2076-3417/10/19/6937/s1: MATLAB codes for the FSEDA method.

Author Contributions: Conceptualization, A.-R.H. and A.A.A.; methodology, A.-R.H., A.A.A., and A.F.; software, A.A.A.; validation, A.-R.H. and A.A.A.; formal analysis, A.-R.H., A.A.A., and A.F.; investigation, A.-R.H. and A.A.A.; resources, A.-R.H., A.A.A., and A.F.; data creation, A.-R.H. and A.A.A.; writing-original draft preparation, A.-R.H. and A.A.A.; writing-review and editing, A.-R.H. and A.F.; visualization, A.-R.H., A.A.A., and A.F.; project administration, A.-R.H.; funding acquisition, A.-R.H. All authors have read and agreed to the published version of the manuscript.
Funding: This work was funded by the National Plan for Science, Technology, and Innovation (MAARIFAH)—King Abdulaziz City for Science and Technology-the Kingdom of Saudi Arabia, award number (13-INF544-10).
Acknowledgments: The authors would like to thank King Abdulaziz City for Science and Technology, the Kingdom of Saudi Arabia, for supporting project number (13-INF544-10).
Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A. Classical Test Functions-Set A 

Set A contains 14 test functions listed in Table A1 $[10,62]$.
Table A1. Test functions for global optimization: Set A.
## Appendix B. Classical Test Functions-Set B

Set B contains 40 test functions listed in Table A2 [10,62].
Table A2. Test functions for global optimization: Set B.

# Appendix C. Test Functions with Noise-Set C 

Set C contains seven test functions $\left(f_{1}-f_{7}\right)$, and Gaussian noise with $(\mu=0, \sigma=10)$ was added to each function except $f_{6}$, which contains uniform random noise $U(-17.32,17.32)$.

## Appendix C.1. Goldstein and Price Function

Definition: $f_{1}(\mathbf{x})=\left[1+\left(x_{1}+x_{2}+1\right)^{2}\left(19-14 x_{1}+13 x_{1}^{2}-14 x_{2}+6 x_{1} x_{2}+3 x_{2}^{2}\right)\right]\left[30+\left(2 x_{1}-3 x_{2}\right)^{2}(18-\right.$ $\left.\left.32 x_{1}+12 x_{1}^{2}-48 x_{2}-36 x_{1} x_{2}+27 x_{2}^{2}\right)\right]$.
Search space: $-2 \leq x_{i} \leq 2, i=1,2$.
Global minimum: $\mathbf{x}^{*}=(0,-1) ; f_{1}\left(\mathbf{x}^{*}\right)=3$.
Appendix C.2. Rosenbrock Function
Definition: $f_{2}(\mathbf{x})=\sum_{i=1}^{4}\left(100\left(x_{i}^{2}-x_{i+1}\right)\right)^{2}+\left(\left(x_{i}-1\right)^{2}\right)+1$.
Search space: $-10 \leq x_{i} \leq 10, i=1,2, \ldots, 5$.
Global minimum: $\mathbf{x}^{*}=(1, \ldots, 1), f_{2}\left(\mathbf{x}^{*}\right)=1$.
Appendix C.3. Griewank Function
Definition: $f_{3}(\mathbf{x})=\frac{1}{40} \sum_{i=1}^{n} x_{i}^{2}-\prod_{i=1}^{n} \cos \left(\frac{x_{i}}{\sqrt{i}}\right)+2$.
Search space: $-10 \leq x_{i} \leq 10, i=1,2$.
Global minimum: $\mathbf{x}^{*}=(0,0), f_{3}\left(\mathbf{x}^{*}\right)=1$.
Appendix C.4. Pinter Function
Definition: $f_{4}(\mathbf{x})=\sum_{i=1}^{n} i x_{i}^{2}+\sum_{i=1}^{n} 20 i \sin ^{2}\left(x_{i-1} \sin x_{i}-x_{i}+\sin x_{i+1}\right)+\sum_{i=1}^{n} i \log _{10}\left[1+i\left(x_{i-1}^{2}-2 x_{i}+\right.\right.$ $\left.\left.3 x_{i+1}-\cos x_{i}+1\right)^{2}\right]$, where $x_{0}=x_{n}$ and $x_{n+1}=x_{1}$.
Search space: $-10 \leq x_{i} \leq 10, i=i=1,2, \ldots, 5$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0), f_{4}\left(\mathbf{x}^{*}\right)=1$.
Appendix C.5. Modified Griewank Function
Definition: $f_{5}(\mathbf{x})=\frac{1}{40} \sum_{i=1}^{n} x_{i}^{2}-\prod_{i=1}^{n} \cos \left(\frac{x_{i}}{\sqrt{i}}\right)-\prod_{i=1}^{n} e^{-x_{i}^{2}}+2$.
Search space: $-10 \leq x_{i} \leq 10, i=1,2$.
Global minimum: $\mathbf{x}^{*}=(0,0), f_{5}\left(\mathbf{x}^{*}\right)=1$.
Appendix C.6. Griewank Function with Non-Gaussian Noise
Definition: $f_{6}(\mathbf{x})=\frac{1}{40} \sum_{i=1}^{n} x_{i}^{2}-\prod_{i=1}^{n} \cos \left(\frac{x_{i}}{\sqrt{i}}\right)+2$.
The simulation noise was changed to the uniform distribution $U(-17.32,17.32)$
Search space: $-10 \leq x_{i} \leq 10, i=1,2$.
Global minimum: $\mathbf{x}^{*}=(0,0), s f_{6}\left(\mathbf{x}^{*}\right)=1$.
Appendix C.7. Griewank Function with (50D)
Definition: $f_{7}(\mathbf{x})=\frac{1}{40} \sum_{i=1}^{n} x_{i}^{2}-\prod_{i=1}^{n} \cos \left(\frac{x_{i}}{\sqrt{i}}\right)+2$.
Search space: $-10 \leq x_{i} \leq 10, i=1,2, \ldots, 50$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0),, f_{7}\left(\mathbf{x}^{*}\right)=1$.
Appendix D. Test Functions with Noise-Set D
Set D contains 13 test functions $\left(g_{1}-g_{13}\right)$, and Gaussian noise with $(\mu=0, \sigma=0.2)$ was added to each function.

# Appendix D.1. Ackley Function 

Definition: $g_{1}(\mathbf{x})=20+e-20 e^{-\frac{1}{3} \sqrt{\frac{1}{6} \sum_{i=1}^{n} x_{i}^{2}}}-e^{-\frac{1}{6} \sum_{i=1}^{n} \cos \left(2 \pi x_{i}\right)}$.
Search space: $-15 \leq x_{i} \leq 30, i=1,2, \ldots, n$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0) ; g_{1}\left(\mathbf{x}^{*}\right)=0$.
Appendix D.2. Alpine Function
Definition: $g_{2}(\mathbf{x})=\sum_{i=1}^{n}\left|x_{i} \sin x_{i}+0.1 x_{i}\right|$.
Search space: $-10 \leq x_{i} \leq 10, i=1,2, \ldots, n$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0) ; g_{2}\left(\mathbf{x}^{*}\right)=0$.
Appendix D.3. Axis Parallel Function
Definition: $g_{3}(\mathbf{x})=\sum_{i=1}^{n} i x_{i}^{2}$.
Search space: $-5.12 \leq x_{i} \leq 5.12, i=1,2, \ldots, n$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0) ; g_{3}\left(\mathbf{x}^{*}\right)=0$.
Appendix D.4. DeJong Function
Definition: $g_{4}(\mathbf{x})=\|\mathbf{x}\|^{2}$.
Search space: $-5.12 \leq x_{i} \leq 5.12, i=1,2, \ldots, n$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0) ; g_{4}\left(\mathbf{x}^{*}\right)=0$.
Appendix D.5. Drop Wave Function
Definition: $g_{5}(\mathbf{x})=-\frac{1+\cos 12 \sqrt{\|\mathbf{x}\|^{2}}}{\frac{1}{2}\left\|\mathbf{x}\right\|^{2}+2}$.
Search space: $-5.12 \leq x_{i} \leq 5.12, i=1,2, \ldots, n$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0) ; g_{5}\left(\mathbf{x}^{*}\right)=0$.
Appendix D.6. Griewank Function
Definition: $g_{6}(\mathbf{x})=\frac{1}{40} \sum_{i=1}^{n} x_{i}^{2}-\prod_{i=1}^{n} \cos \left(\frac{x_{i}}{x_{i}^{*}}\right)+2$.
Search space: $-600 \leq x_{i} \leq 600, i=1,2, \ldots, 50$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0), g_{6}\left(\mathbf{x}^{*}\right)=1$.
Appendix D.7. Michalewicz Function
Definition: $g_{7}(\mathbf{x})=-\sum_{i=1}^{2} \sin \left(x_{i}\right) \sin ^{2 m}\left(\frac{x_{i}^{2}}{\pi}\right) ; m=10$.
Search space: $0 \leq x_{i} \leq \pi, i=1,2, \ldots, n$.
Global minima: $g_{7}\left(\mathbf{x}^{*}\right)=-29.6309 ; n=30$.
Appendix D.8. Moved Axis Function
Definition: $g_{8}(\mathbf{x})=\sum_{i=1}^{n} 5 i x_{i}^{2}$.
Search space: $-5.12 \leq x_{i} \leq 5.12, i=1,2, \ldots, n$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0) ; g_{8}\left(\mathbf{x}^{*}\right)=0$.
Appendix D.9. Pathological Function
Definition: $g_{9}(\mathbf{x})=\sum_{i=1}^{n-1}\left[\frac{1}{2}+\frac{\sin ^{2}\left(\sqrt{100 x_{i}^{2}+x_{i+1}^{2}}-0.5\right)}{1+10^{-3}\left(x_{i}^{2}-2 x_{i} x_{i+1}+x_{i+1}^{2}\right)^{2}}\right]$.
Search space: $-100 \leq x_{i} \leq 100, i=1,2, \ldots, n$.

# Appendix D.10. Rastrigin Function 

Definition: $g_{10}(\mathbf{x})=10 n+\sum_{i=1}^{n}\left(x_{i}^{2}-10 \cos \left(2 \pi x_{i}\right)\right)$.
Search space: $-2.56 \leq x_{i} \leq 5.12, i=1, \ldots, n$.
Global minimum: $\mathbf{x}^{*}=(0, \ldots, 0), g_{10}\left(\mathbf{x}^{*}\right)=0$.
Appendix D.11. Rosenbrock Function
Definition: $g_{11}(\mathbf{x})=\sum_{i=1}^{4}\left(100\left(x_{i}^{2}-x_{i+1}\right)\right)^{2}+\left(\left(x_{i}-1\right)^{2}\right)+1$.
Search space: $-10 \leq x_{i} \leq 10, i=1,2, \ldots, 5$.
Global minimum: $\mathbf{x}^{*}=(1, \ldots, 1), g_{11}\left(\mathbf{x}^{*}\right)=1$.
Appendix D.12. Schwefel Function
Definition: $g_{12}(\mathbf{x})=-\sum_{i=1}^{n}\left(x_{i} \sin \sqrt{\left|x_{i}\right|}\right)$.
Search space: $-500 \leq x_{i} \leq 500, i=1,2, \ldots, n$.
Global minimum: $\mathbf{x}^{*}=(1, \ldots, 1), g_{12}\left(\mathbf{x}^{*}\right)=-418.9829 n$.
Appendix D.13. Tirronen Function
Definition: $g_{13}(\mathbf{x})=3 e^{-\frac{1+1^{2}}{10 n}}-10 e^{-8\left\|x\right\|^{2}}+\frac{5}{2 n} \sum_{i=1}^{n} \cos \left[5\left(x_{i}+(1+i \bmod 2) \cos \|x\|^{2}\right)\right]$.
Search space: $-10 \leq x_{i} \leq 5, i=1,2, \ldots, n$.
