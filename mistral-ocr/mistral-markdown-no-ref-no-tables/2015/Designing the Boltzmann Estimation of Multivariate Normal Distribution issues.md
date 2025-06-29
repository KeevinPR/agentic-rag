# Designing the Boltzmann Estimation of Multivariate Normal Distribution: issues, goals and solutions 

Ignacio Segovia-Domínguez<br>Center for Research in Mathematics Guanajuato, México ijsegoviad@cimat.mx

Arturo Hernández-Aguirre<br>Center for Research in Mathematics Guanajuato, México artha@cimat.mx


#### Abstract

This paper introduces a new Estimation of Distribution Algorithm (EDA) based on the multivariate Boltzmann distribution. In this work, the design variables and the energy function of the Boltzmann distribution are continuous. Note that since the population has finite size, it can only approximate a continuous Boltzmann distribution with some error. In order to tackle this issue, the parameter estimators for the mean vector and covariance matrix of a Multivariate Normal Density that approximate the Boltzmann density, are derived by minimizing the Kullback-Leibler divergence. The algorithm introduced here uses one energy function for the mean estimator and another for the covariance matrix estimator. The first function places the probability mass around the most promising regions by assigning larger weights to individuals with higher fitness. However, the second function orients the covariance matrix along improving directions by assigning larger weights to individuals with lower fitness. Our proposal combines the conveniences of linear weights with a simple annealing schedule to regulate the exploration and exploitation of the search process. The resulting algorithm is named the Boltzmann Estimation of Multivariate Normal Algorithm (BEMNA). By applying the developed formulae the BEMNA is capable of adapting the structure of a density model to the promisory search directions. BEMNA is tested with a benchmark of 16 functions and contrasted with the AMaLGaM algorithm, a state of the art EDA. Statistical tests of the experimental data show the competitiveness of the proposed algorithm.


Keywords-Estimation of Distribution Algorithm, Boltzmann distribution, Real valued optimization, Evolutionary computation, Kullback-Leibler divergence

## I. INTRODUCTION

The Estimation of Distribution Algorithms [1] EDAs are optimization methods based on estimating and sampling a probability distribution of some set of individuals chosen after a quality criteria. The most promising regions are unknown and have to be discovered during the optimization process. The EDA must favor such regions by assigning to them the highest probability values. Hence, the main goal of the EDA is to pose the probability mass around the optima. The common strategy, without loss of generality for a maximization process, is to reinforce the sampling of regions where the higher fitness function values have been sampled, and to disregard the regions with the lower values. The most common EDA scheme for continuous optimization is to use a multivariate or univariate Normal distribution [2]-[6]. The parameters of the Normal density are estimated by using maximum likelihood estimators
(MLEs) over the selected set, which is usually determined by a selection operator: truncation selection, tournament selection, et cetera. Although these approaches have proven competitive up to some extent, some issues are worth to notice here:

- It is a well-known issue that the variance in estimation of distribution algorithms is often less than required, hence, the MLE variance estimator is not the most adequate technique of searching for the optimum vector [7], [8].
- Not only is it possible that the variance could be less than required, but in addition, the orientation of the variance could be inadequate for sampling better solutions than those already known. Take into consideration the case when the population is not around the optimum region, hence, estimating the structure of the search density from the population will not guide the search to new promising regions. In this case, the structure of the search density must be oriented according to the improving directions instead of reproducing the population density structure.

Our purpose is to circumvent the mentioned issues by proposing weighted estimators for a parametric distribution which approximate the Boltzmann. The Boltzmann distribution has been largely used in optimization. For instance, in the context of Estimation of Distribution Algorithms (EDAs), researchers have proposed different approaches, such as the BEDA [9]-[11]. This is a general EDA framework based on the Boltzmann distribution, from which practical EDAs have been derived. For example: the FDA [12] which considers a factorization of the energy function, the Yun Peng et al. [13] and Valdez et al. works [14] which propose different approximations in continuous search spaces by minimizing the Kullbak-Leibler divergence. The unifying characteristic of these approaches is that they intend to set the highest probability on the most promising regions, considering a promising region as the region where the best fitness values have been sampled. This is to say, the better the fitness function is in a region, the more intense the sampling must be.

The Gibbs or Boltzmann distribution of an energy function $\mathrm{g}(\mathrm{x})$ is defined by

$$
p(x):=\int \frac{\exp (\beta g(\vec{x}))}{Z} d \vec{x}
$$

As can be noticed in Equation (1), the objective function can be used directly as an energy function. In practical approaches, the Boltzmann distribution cannot be used directly for sampling because it is necessary to determine the objective function in the whole domain. For this reason, the parameters of a density function are computed by minimizing a measure between the parametric distribution and the Boltzmann distribution; for instance, the Kullback-Leibler divergence [13][15].

There are remarkable challenges to consider when designing EDAs based on the Boltzmann distribution:

- To choose an adequate $\beta$ parameter in Equation (1). Usually $\beta$ depends on the time or is dynamic during the optimization process. The process which controls the $\beta$ updating each generation is called the annealing schedule. The annealing schedule can be used to manage the exploration and convergence of the algorithm.
- To derive robust parameter estimators for the approximated distribution. Some approaches [13], [16] have derived formulae for estimating parameters of a probability function which approximate the Boltzmann, by weighting the population or selected set by exponential functions, similar to Equation (1). Even though competitive results are obtained, these proposals often suffer from premature convergence because the exponential function drastically leads the probability mass to suboptimal positions. This behavior can be avoided by manipulating the $\beta$ value, but it is not simple to determine a competent manner to do so. A second option is to obtain formulae with an auto-adapted $\beta$ which do not drastically impact the estimators from one generation to the next.
- The last two issues are also related with the aforementioned variance reduction, which is a common issue in EDAs [7]. In the same vein, the structure of the probability function is related to the orientation of the density, which is defined by the covariance matrix. The structure by itself could be a determinant factor in the covariance reduction. Consider the case of two covariance matrices with the same eigenvalues, the same variance magnitude. They could perform completely differently if they had different eigenvectors; if the eigenvectors are not oriented in an improvement direction the algorithm could get trapped in the region currently covered by the population, even if there is no a local or global optimum inside.

Our proposal intends to tackle the aforementioned challenges by introducing the following features:

- A proposal of annealing schedule to update the $\beta$ value.
- Robust formulae for the estimators computation, in the sense that they are not impacted as drastically as the exponential function used in other approaches.
- The novel annealing schedules tackle the variance reduction problem, hence, these are mechanisms to avoid the premature convergence of the algorithm.
- A different energy function for the Bolztmann approximation, which induces an adequate orientation in the covariance matrix, favoring the improving directions.

The paper is organized as follows: Section II presents the derivation of parameter estimators, it is to say the mean vector and covariance matrix of a Multivariate Normal, which approximates the Boltzmann Density. Section III introduces a remarkable concept regarding the estimation of the covariance matrix, which significantly benefits the search by estimating an adequate structure of the probability search distribution.

Section IV introduces the Boltzmann Estimation of Multivariate Normal Algorithm (BEMNA). Then, Section V is devoted to test the proposed EDA on well-known Benchmark problems versus another state of the art algorithm. Finally, Section VI provides some concluding remarks.

## II. APPROXIMATING THE BOLTZMANN DISTRIBUTION BY THE NORMAL MULTIVARIATE DISTRIBUTION

This section introduces the formulae to estimate the mean vector $\vec{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$ of a Normal multivariate density $Q_{x}$, which approximates the multivariate Boltzmann density $P_{x}$.

Consider the multivariate Normal density, $Q_{x}=$ $Q(x ; \mu, \Sigma)$, as shown in Equation (2). The corresponding Boltzmann density, defined in the same domain as $Q_{x}$, is in Equation (3).

$$
\begin{gathered}
Q_{x}=\frac{1}{\sqrt{(2 \pi)^{d}|\boldsymbol{\Sigma}|}} \exp \left\{-\frac{1}{2}(\vec{x}-\vec{\mu})^{\t}\boldsymbol{\Sigma}^{-1}(\vec{x}-\vec{\mu})\right\} \\
P_{x}=\frac{\exp (\beta g(\vec{x}))}{Z}
\end{gathered}
$$

The procedure to find the parameters of $Q_{x}$, which best approximate $P_{x}$, consist in minimizing a measure of dissimilarity between density functions. Similar to previous works [13] [14], the Kullback-Leibler Divergence presented in Equation (4), $K_{Q P}=D_{K L}\left(Q_{x} \| P_{x}\right)$, is used for this purpose.

$$
K_{Q P}=\int Q_{x} \log \frac{Q_{x}}{P_{x}} d \vec{x}
$$

The minimization of $K_{Q P}$ for finding the optimal parameters $\left[\vec{\mu}_{*}, \boldsymbol{\Sigma}_{*}\right]$ can be stated as shown in Equation (5).

$$
[\vec{\mu}, \boldsymbol{\Sigma}]=\arg \min \left\{K_{Q P}\right\}
$$

Notice that $K_{Q P}$ can be rewritten as

$$
\begin{aligned}
K_{Q P} & =\int Q_{x} \log Q_{x} d \vec{x}-\int Q_{x} \log P_{x} d \vec{x} \\
& =-H\left(Q_{x}\right)-\int Q_{x} \log P_{x} d \vec{x} \\
& =-\frac{1}{2} \log \left((2 \pi e)^{d}|\Sigma|\right)-\int Q_{x} \log P_{x} d \vec{x}
\end{aligned}
$$

where the term $H\left(Q_{x}\right)$ stands for the entropy of the multivariate Normal density [17]. In order to get the parameters which minimize the Kulback-Leibler Divergence, the partial derivatives are calculated in Equations (7) and (8).

$$
\begin{aligned}
\frac{\delta K_{Q P}}{\delta \vec{\mu}} & =-\int \frac{\delta Q_{x}}{\delta \vec{\mu}} \log P_{x} d \vec{x} \\
& =-\int Q_{x}\left[\boldsymbol{\Sigma}^{-1}(\vec{x}-\vec{\mu})\right] \log P_{x} d \vec{x} \\
\frac{\delta K_{Q P}}{\delta \boldsymbol{\Sigma}}= & -\frac{1}{2} \frac{\delta \log (|\boldsymbol{\Sigma}|)}{\delta \boldsymbol{\Sigma}}-\int \frac{\delta Q_{x}}{\delta \boldsymbol{\Sigma}} \log P_{x} d \vec{x} \\
= & -\frac{1}{2} \int Q_{x}\left[\boldsymbol{\Sigma}^{-1}(\vec{x}-\vec{\mu})(\vec{x}-\vec{\mu})^{t} \boldsymbol{\Sigma}^{-1}\right] \log P_{x} d \vec{x} \\
& +\frac{1}{2} \int Q_{x} \boldsymbol{\Sigma}^{-1} \log P_{x} d \vec{x}-\frac{1}{2} \boldsymbol{\Sigma}^{-1}
\end{aligned}
$$

The optimal estimates for the mean vector and covariance matrix are obtained by forcing the derivatives equal to 0 , as in Equations (9) and (10), and solving for $\vec{\mu}$ and $\boldsymbol{\Sigma}$ respectively.

$$
\begin{aligned}
0 & =\frac{\delta K_{Q P}}{\delta \vec{\mu}} \\
0 & =\vec{\mu} \int_{x} Q_{x} \log P_{x} d \vec{x}-\int Q_{x} \vec{x} \log P_{x} d \vec{x} \\
0 & =\vec{\mu} \beta E_{Q}[g(\vec{X})]-\vec{\mu} \log Z-E_{Q}[g(\vec{X}) \vec{X}] \beta+E_{Q}[\vec{X}] \log Z \\
\vec{\mu} & =\frac{E_{Q}[g(\vec{X}) \vec{X}]}{E_{Q}[g(\vec{X})]}
\end{aligned}
$$

The following equivalences were used to obtain Equations (9) and (10):

- $\log P_{x}=\beta g(\vec{x})-\log Z$,
- $\int Q_{x} \vec{x} d \vec{x}=E_{Q}[\vec{X}], \int Q_{x}(\vec{x}-\vec{\mu})(\vec{x}-\vec{\mu})^{t} d \vec{x}=$ $E_{Q}[(\vec{X}-\vec{\mu})(\vec{X}-\vec{\mu})^{t}]$, and other similar equations.
- As $\vec{X} \sim Q_{x}$ then $E_{Q}[\vec{X}]=\vec{\mu}$ and $E_{Q}[(\vec{X}-\vec{\mu})(\vec{X}-$ $\vec{\mu})^{t}]=\boldsymbol{\Sigma}$.

$$
\begin{aligned}
0 & =\frac{\delta K_{Q P}}{\delta \boldsymbol{\Sigma}} \\
0= & \int Q_{x}(\vec{x}-\vec{\mu})(\vec{x}-\vec{\mu})^{t} \log P_{x} d \vec{x} \\
& -\int Q_{x} \log P_{x} d \vec{x} \boldsymbol{\Sigma}+\boldsymbol{\Sigma} \\
\boldsymbol{\Sigma}= & \frac{E_{Q}[g(\vec{X})(\vec{X}-\vec{\mu})(\vec{X}-\vec{\mu})^{t}]}{E_{Q}[g(\vec{X})]-1 / \beta}
\end{aligned}
$$

Finally, for estimating the parameters using the observations $\vec{x}^{(1)}, \vec{x}^{(2)}, \ldots, \vec{x}^{(N)}$ of the random variable $\vec{X} \sim Q_{x}$, a numerical stochastic approximation by the Monte Carlo method is computed, as shown in Equations (11) and (12).

These two equations are the estimators that approximate the parameters of the search distribution.

$$
\begin{gathered}
\vec{\mu}_{*}=\frac{\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right) \vec{x}^{(i)}}{\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)} \\
\boldsymbol{\Sigma}_{*}=r_{\mathrm{e}} \cdot \sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)\left(\vec{x}^{(i)}-\vec{\mu}\right)\left(\vec{x}^{(i)}-\vec{\mu}\right)^{t}
\end{gathered}
$$

where

$$
r_{\mathrm{e}}=\left(\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)-\frac{N}{\beta}\right)^{-1}
$$

## A. A note about the derived formulae

The estimators in Equations (11) and (12) use weights defined by $\frac{g\left(\vec{x}^{(i)}\right)}{\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)}$. In other words, the weighted estimators are computed by using weights proportional to the objective function value of each individual in the selected set. In contrast to similar approaches [13], [16], there are some advantages of these derivations:

- A proportional weight of the estimators avoids drastic changes when the individuals considerably differ in the objective function value. It is to say, if a new individual with a large objective value is sampled, the exponential weights could concentrate the probability mass around this single individual, leading the algorithm to premature convergence [13]. This effect is diminished when using proportional weights.
- A second advantage is that the minimum variance, which is bounded by a $\beta=\infty$, is not 0 for our approach, which is a significant advantage considering that EDAs naturally suffer from premature convergence and variance reduction [13], [16].
The energy function $g(\vec{x})$ must be positive or equal to zero in the domain. However, the objective function $\mathcal{F}(\vec{x})$ might be negative, considering that this is a maximization/minimization problem, in order to construct a valid energy function. Throughout this paper, the $g\left(\vec{x}^{(i)}\right)$ value is computed as $g\left(\vec{x}^{(i)}\right)=-\mathcal{F}\left(\vec{x}^{(i)}\right)-\min _{i}\left(-\mathcal{F}\left(\vec{x}^{(i)}\right)\right)$. The next section analyzes the importance of the energy function and other topics related to evolutionary computation.


## B. The annealing schedule

As seen in Equations (11), (12) and (13), the $\beta$ value only affects the covariance matrix computation. The grade of impact of $\beta$ over the covariance is highly related with $\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)$. On one hand, $N / \beta<\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)$ must hold in order to maintain a positive variance in the diagonal of the covariance matrix. On the other hand, if $N / \beta<<\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)$ then its effect is diminished. As a consequence, the estimator reaches the minimum variance when $\beta \rightarrow \infty$ because $N / \beta \rightarrow 0$. An interesting remark about this last setting is that the Normal distribution with such a minimum variance is not similar to a Dirac $\delta$, while the corresponding Boltzmann distribution actually is.

Notice that a method to control the $\beta$ value is needed, but it is not straightforward since $\beta$ might increase indefinitely. However, from the previous discussion: $\beta$ is highly related with $\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)$. Hence, it could be written as factor multiplying $\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)$. As a consequence, $r_{e}$ must be a reciprocal portion of $\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)$. In agreement with the arguments stated above, assume a parametrization of the $\beta$ value as follows:

$$
\beta=N /\left((1-\gamma) \sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)\right)
$$

where $0<\gamma<1$, then the scale factor $r_{e}$ is

$$
r_{e}=\left(\gamma \sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)\right)^{-1}
$$

According to this proposal the covariance estimator is rewritten as in Equation (16).

$$
\boldsymbol{\Sigma}_{*}=\frac{\sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)\left(\vec{x}^{(i)}-\vec{\mu}\right)\left(\vec{x}^{(i)}-\vec{\mu}\right)^{t}}{\gamma \cdot \sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)}
$$

This new equation for $\boldsymbol{\Sigma}_{*}$ is more convenient than the one presented in Equation (12) because the scale factor $\gamma$ is easier to control than the original $\beta$ parameter. Also $\gamma$ is more intuitive since it is basically a scaling factor, which can help to regulate the size of the covariance matrix. Additionally, notice that the individual with the highest $g\left(\vec{x}^{(i)}\right)$ has the greatest impact in the covariance computation.

## III. USING A DIFFERENT ENERGY FUNCTION FOR THE COVARIANCE MATRIX COMPUTATION

Every individual contribute to compute the mean vector $\vec{\mu}_{*}$ and the covariance matrix $\boldsymbol{\Sigma}_{*}$. Notice that the information of fitness function is introduced via $g\left(\vec{x}^{(i)}\right)$. The way this information modifies the estimates is worth to analyze. First let us study the mean vector estimator, Equation (11). Most of the probability mass is around the mean vector, which means that this position is crucial to produce samples on promissory regions. In Equation (11) each individual is weighted by $g\left(\vec{x}^{(i)}\right) / \sum_{i=1}^{S} g\left(\vec{x}^{(i)}\right)$, and the sum of these weights is equal to one. So, any mean vector computed in this way is a linear combination of the individuals and is inside the convex hull of the actual population [18].

In addition, Figure 1-(a) shows several differences between this proposal and Maximum Likelihood Estimation (MLE). The location of the mean vector via MLE only depends on the density of population whilst the location of $\vec{\mu}_{*}$ is biased according to the fitness function. Hence, our proposal usually situates the center of the density on promissory regions according to the location of the best individuals. Also, Figure 1-(a) shows a smaller covariance matrix in our proposal compared to the computed one via MLE, when using the fitness function as the energy function. This behaviour could be undesirable
![img-0.jpeg](img-0.jpeg)

Fig. 1. Comparison of normal densities. The symbol + shows the position of mean vector via maximum likelihood estimation while the asterisk symbol shows the location of $\vec{\mu}_{*}$. (a) Maximum likelihood estimators (dashed line) versus our proposal (solid line), computed using Equations (11) and (16). (b) Covariance matrix computed with weights using $g\left(\vec{x}^{(i)}\right)$ in Equation (16) (dashed line), versus computation using $h\left(\vec{x}^{(i)}\right)$ in Equation (17) (solid line).
because it might lead to the collapse of the population in a suboptimal point after some generations.

The proposed estimator in Equation (16) multiplies each term $\left(\vec{x}^{(i)}-\vec{\mu}\right)\left(\vec{x}^{(i)}-\vec{\mu}\right)^{t}$ by the weight $g\left(\vec{x}^{(i)}\right) / \sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)$. Since $\vec{\mu}_{*}$ is close to the best individuals, the vector $\vec{x}^{(i)}-\vec{\mu}_{*}$ has a shorter length for the best individuals than the worst ones. Then, summation of matrices $\left(g\left(\vec{x}^{(i)}\right) / \sum_{i=1}^{N} g\left(\vec{x}^{(i)}\right)\right.$. $\left(\vec{x}^{(i)}-\vec{\mu}\right)\left(\vec{x}^{(i)}-\vec{\mu}\right)^{t}$ induces structures with a smaller variance than the MLE estimator. In order to overcome this issue, we propose to change the energy function $g\left(\vec{x}^{(i)}\right)$ as shown in Equation (17).

$$
\boldsymbol{\Sigma}_{*}=\frac{\sum_{i=1}^{N} h\left(\vec{x}^{(i)}\right)\left(\vec{x}^{(i)}-\vec{\mu}\right)\left(\vec{x}^{(i)}-\vec{\mu}\right)^{t}}{\gamma \cdot \sum_{i=1}^{N} h\left(\vec{x}^{(i)}\right)}
$$

This proposal uses an energy function $h\left(x^{\overrightarrow{(i)}}\right)$, which returns a value between 0.01 and 1 according to the rank of the individual $x^{\overrightarrow{(i)}}$. Here, the values are taken from partitions on $[0.01,1]$. Let $j^{t h}$ denote the rank of individual $\vec{x}^{(i)}$ in the population sorted by fitness values, such that if $\vec{x}^{(i)}$ is the

best individual then $j^{t h}=1$, otherwise if $\vec{x}^{(k)}$ is the worst individual then $j^{t h}=N$. Thus, the energy function $h(\cdot)$, for the covariance matrix computation, is defined as follows

$$
h\left(x^{\vec{i}}\right)=\frac{1}{N}+\frac{99\left(j^{t h}-1\right)}{100(N-1)}
$$

where the first term ensures a non-zero weight for the best individual.

Equations (17) and (18) cause the differences $\vec{x}^{(i)}-\vec{\mu}_{*}$ of the worst individuals to be multiplied by higher weights than the other individuals. Hence, the proposed formulae for the mean $\vec{\mu}_{*}$ and covariance $\boldsymbol{\Sigma}_{*}$ estimators equip the algorithm with the following features:

- The proposed mean estimator poses the maximum probability mass around the best known region.
- The covariance matrix estimator enlarges the probability density, because usually the farthest an individual is from the mean the greater its weight is.
- Additionally, the enlargement of the covariance matrix aligns the normal multivariate distribution through the direction of maximum improvement; it goes from the worst to the best individuals.

A visual comparison between covariance estimates (16) and (17) is presented in Figure 1-(b). As can be observed our proposal is more prone to avoiding premature convergence than the MLE estimator.

## A. Updating the scale factor $\gamma$

In order to effectively apply the developed equations into the EDA context, the $\gamma$ factor must be adapted through the optimization process. Here, the annealing schedule modifies $\gamma$ in a linear fashion based on the improvements of the fitness values from the parents to the children. Notice that updating $\beta$ of Equations $(12,13)$ is equivalent to updating $\gamma$ in Equation (16). Most of the similar previous proposals adapt the $\beta$ or $\gamma$ parameter in an exponential manner [13], with a consequent drastic impact from one generation to the next one.

As mentioned $\gamma=1$ corresponds to the minimum variance (i.e. $\beta=\infty$ ), thus the limits for this parameter are well defined as $0<\gamma \leq 1$. The updating of $\gamma$ proceeds as follows

$$
\gamma^{t+1}=\gamma^{t}-\frac{2}{N}\left(\frac{12 M_{s}}{N}-1\right)
$$

where $M_{s}$ is the number of new simulations that are preserved from the current generation to the next one, throughout this paper known as the survivor individuals. Note that the maximum number of survivor individuals is the sample size $S_{*}$. Additionally, two conditions must be added to ensure $0<\gamma \leq 1$ : if $\gamma \leq 0$ then $\gamma=0.01$, also if $\gamma>1$ then $\gamma=1$.

If there are several survivor individuals this rule increases the covariance matrix values; which means that there is still a chance to find better individuals in the vicinity. Otherwise, the
covariance is reduced in order to focus on a smaller area. As a consequence, this annealing schedule controls the exploration and exploitation according to the gathered information.

## IV. The Boltzmann Estimation of Mutivariate Normal Algorithm

This section introduces our proposal named Boltzmann Estimation of Normal Multivariate Algorithm (BEMNA), which is presented in Figure 2. The algorithm exploits the developed parameter estimators $\vec{\mu}_{*}$ and $\boldsymbol{\Sigma}_{*}$, which allow to model the uncertainty of the optimum location.

The BEMNA starts with a random population, it is evaluated using the fitness function, then the values $g\left(\vec{x}^{(i)}\right)$ are computed in order to turn the minimization problem to a maximization one. The whole set of individuals $\mathcal{P}^{(t)}$ is used to compute the estimates $\vec{\mu}_{*}$ and $\boldsymbol{\Sigma}_{*}$. Next, new individuals are simulated from the multivariate normal density. The set $\mathcal{P}_{S}^{(t)}$ could have better fitness values than the current population. The next population $\mathcal{P}^{(t+1)}$ is created by selecting the best individuals between $\mathcal{P}^{(t)}$ and $\mathcal{P}_{S}^{(t)}$. The number of survivor individuals $M_{s}$ is used to adapt the scale factor $\gamma$ according to the gathered information. Finally, the best individual in the population is returned as the best approximation to the global optimum.

```
Initialize \(t \leftarrow 0, N_{s}, S_{s}\) and \(\gamma^{0}\)
\(\mathcal{P}^{(t)} \leftarrow \mathcal{U} \text { (Domain) } \quad \triangleright\) First population
Evaluate \(\mathcal{F}\left(\vec{x}^{(i)}\right)\)
Compute \(g\left(\vec{x}^{(i)}\right)=-\mathcal{F}\left(\vec{x}^{(i)}\right)-\min \left(-\mathcal{F}\left(\vec{x}^{(i)}\right)\right)\)
while (Stop condition is not reached) do
    Estimate \(\vec{\mu}_{*}\) and \(\boldsymbol{\Sigma}_{*}\) of \(\mathcal{P}^{(t)} \), Eq. (11) and (17)
    \(\mathcal{P}_{S}^{(t)} \leftarrow\) Simulate \(S_{s}\) individuals from \(Q\left(x ; \vec{\mu}_{*} ; \boldsymbol{\Sigma}_{*}\right)\)
    \(\mathcal{P}_{S}^{(t)} \leftarrow \operatorname{Reinsertion}\left(\mathcal{P}_{S}^{(t)}\right)\)
    Evaluate \(\mathcal{F}\left(\vec{x}^{(j)}\right)\) and \(g\left(\vec{x}^{(j)}\right)\) of \(\mathcal{P}_{S}^{(t)}\)
    \(\mathcal{P}^{(t+1)} \leftarrow\) Best \(N_{s}\) individuals of \(\mathcal{P}^{(t)} \cup \mathcal{P}_{S}^{(t)}\)
    \(M_{s} \leftarrow\left|\mathcal{P}^{(t+1)} \cap \mathcal{P}_{S}^{(t)}\right|\)
    Compute \(\gamma^{t+1}\) by Eq. (19)
    if \(\gamma \leq 0\) then \(\gamma \leftarrow 0.01\) end if
    if \(\gamma>1\) then \(\gamma \leftarrow 1\) end if
        \(t \leftarrow t+1\)
    end while
    Return the elite individual in \(\mathcal{P}^{(t)}\)
```

Fig. 2. Pseudocode of the proposed EDA: Boltzmann Estimation of Multivariate Normal Algorithm (BEMNA).

## A. Recommendations about the parameters

The only parameters of the BEMNA are the number of partitions $n_{p}$, population size $N_{s}$ and sample size $S_{s}$. After an empirical study on several benchmark problems, some comments/recommendations about the parameters can be provided:

- The factor $2 / N$ in Eq. (19) controls the velocity of parameter adaptation. A factor close to 1 speeds up convergence whilst a higher value reduces the convergence velocity. As a consequence the best value for this parameter depends on the problem. However, our

empirical observations suggest that the proposed value $2 / N_{s}$ performs adequately for most of the problems.

- An adequate population size $N_{s}$ is essential for the BEMNA. If there are too few samples the population collapses, leading to premature convergence. On the contrary, a large sample increases the number of function evaluations and reduces the convergence velocity. Our empirical study suggests that the minimum recommended population size is $N_{s}=$ $\left\lfloor 19.92+1.35 \cdot d^{1.44}\right\rfloor$ where $d$ is the number of dimensions. The previous equation was calculated by a regression method applied to the minimum population sizes which delivers successful results in most of the benchmark problems.
- The sample size $S_{s}$ affects the convergence velocity. If a few samples are simulated then there is less of a chance of intensively exploring the search space, while favoring a fast convergence to a local optimum. On the contrary, a large number of simulations have a greater chance of intensively exploring the search space, avoiding getting trapped in a local optimum; however it takes a larger number of fitness evaluations. According to our experiments, the BEMNA shows a competitive performance with a sample size $S_{s}=N_{s} / 6$ for most of the problems.

A well known issue in Normal multivariate EDAs is that the covariance matrix could present negative eigenvalues (due to numerical errors [5]). In order to avoid this issue we apply the repairing scheme stated in Figure 3. This repairing method is not utilized most of the time, and it just needs a few iterations to fix the covariance matrix.

1: Let $\boldsymbol{L}$ be the matrix of eigenvectors of covariance matrix $\boldsymbol{\Sigma}$ by columns, $d$ the number of dimensions and $\boldsymbol{\Lambda}$ a diagonal matrix with the corresponding eigenvalues, in decreasing order.
2: $i \leftarrow d$, flag $\leftarrow 0$
3: while $i>0$ do
4: if $\boldsymbol{\Lambda}_{i, i}<1 e-100$ then
$\boldsymbol{\Lambda}_{i, i} \leftarrow 1 e-100$
$f l a g \leftarrow 1$
else
break
end if
$i \leftarrow i-1$
end while
if flag $==1$ then
$\boldsymbol{\Sigma}=\boldsymbol{L} \boldsymbol{\Lambda} \boldsymbol{L}^{t}$
end if
Fig. 3. Repairing scheme for non-positive definite covariance matrix $\boldsymbol{\Sigma}$.
The parameter $\gamma$ controls the spread of simulated individuals based on the survivors from the current generation to the next one. Since no a priori knowledge is considered to choose an initial value for $\gamma$ (e.g. the type of problem, survivors individuals, etcetera), a value in the middle of the domain of $\gamma$ is chosen, it is to say $\gamma^{0}=0.5$. In addition, since the simulation method might generate samples outside
the search domain, a re-insertion technique is added in line 8. Let $\zeta_{k}=l_{k}^{\text {upper }}-l_{k}^{\text {lower }}$ be the domain length in dimension $k$, where $l_{k}^{\text {upper }}$ and $l_{k}^{\text {lower }}$ are the upper bound and lower bound in dimension $k$. For each dimension, the new sample $\tilde{g}^{(i)}=\left(y_{1}^{(i)}, \cdots, y_{k}^{(i)}, \cdots, y_{D}^{(i)}\right)$ is tested/replaced by the following rules:

- $\quad$ if $y_{k}^{(i)}>\underset{l_{k}^{\text {upper }}}{l_{k}^{\text {upper }}}$ then $a=\left(y_{k}^{(i)}-l_{k}^{\text {upper }}\right) / \zeta_{k}$ and $y_{k}^{(i)}=$ $\underset{l_{k}^{\text {upper }}}{l_{k}^{\text {upper }}}-\zeta_{k}(a-\lfloor a\rfloor)$
- if $y_{k}^{(i)}<l_{k}^{\text {lower }}$ then $a=\left(l_{k}^{\text {lower }}-y_{k}^{(i)}\right) / \zeta_{k}$ and $y_{k}^{(i)}=$ $l_{k}^{\text {lower }}+\zeta_{k}(a-\lfloor a\rfloor)$
which ensures that any new individual is inside the domain.


## V. EXPERIMENTS

This section is dedicated to test our algorithm versus another state of the art EDA: The Adapted Maximum Likelihood Gaussian Model Iterated Density-Estimation Evolutionary Algorithm (AMaLGaM-IDEA) [19]. It is capable of modeling dependencies among variables by using a Multivariate Normal Density. In addition, it adds at least three different rules to avoid premature convergence.

TABLE I. BENCHMARK MINIMIZATION PROBLEMS [2], [4], [14]. LEFT: UNIMODAL FUNCTIONS. RIGHT: MULTIMODAL FUNCTIONS. FURTHER DETAILS IN SECTION V.


In order to perform an adequate comparison between both algorithms, a suitable set of problems is chosen as shown in Table I. All of these are minimization problems. For applying the BEMNA these are converted to maximization and translated to positive as follows: $g(\vec{x})=-\mathcal{F}(\vec{x})-\min (-\mathcal{F}(\vec{x}))$. Where $\mathcal{F}(\vec{x})$ is the objective function and $g(\vec{x})$ is the energy function used in Figure 2. The minimum fitness value of all problems is 0 except for $\mathcal{F}_{4}$ and $\mathcal{F}_{15}$; where $\mathcal{F}_{4}^{*}=-d(d+4)(d-1) / 6$ and $\mathcal{F}_{15}^{*}=-1$.

The experiments contrast the error $\mathcal{F}-\mathcal{F}^{*}$ reached for each algorithm, where $\mathcal{F}^{*}$ represents the best fitness value returned by an algorithm. Also this section provides the mean, standard deviation and a non-parametric bootstrap hypothesis test, which elucidates if there is statistical difference between the mean of best objective function values delivered by the algorithms, and the mean of number of function evaluations used to reach the desired precision.

Since there are several variants of the AMaLGaM algorithm, we have chosen the parameter-free version which does not need extra parameter tuning. On the other hand, the parameters of the BEMNA (i.e. population size, number of samples, etcetera) were discussed in the previous section. Both algorithms are stopped when either: a maximum number

of $10000-d$ evaluations or a precision to the optimum value of $\mathcal{F}-\mathcal{F}^{*}<1 \times 10^{-8}$ is reached.

The comparison is summarized in Table II. It contrasts the error $\mathcal{F}-\mathcal{F}^{*}$ reached for each algorithm in 30 dimensions. Each algorithm is executed 50 times for each benchmark function. For each problem there are three measures: 1) the first row is the percentage of success rate, 2) the second is the mean and standard deviation of the best fitness value reached by the algorithms and 3) the third row is the mean and standard deviation of the number of evaluations of function.

In addition, the difference of the algorithms performance is verified by a non-parametric bootstrap hypothesis test with precision of $\alpha=0.05$. We test the hypothesis that the BEMNA returns a different mean of the best fitness value than the AMaLGaM as well as a different number of function evaluations. So, if the null hypothesis $H_{0}: \mu_{1}=\mu_{2}$ is rejected there is statistical evidence to accept differences between both algorithms. This case is marked in bold, as well as the winner of each problem. Observe that the hypothesis test about the fitness value is significant only if the desired precision is not reached, otherwise it might be meaningless because the algorithm is stopped as soon as it reaches the desired precision. In the same vein, the number of function evaluations only is significant if the algorithm does find the optimum.

Table II-top presents the results of 50 independent executions in 8 unimodal benchmark problems. According to these results we can observe the following evidence:

- Both algorithms reached the precision requested for all test problems. But there is statistical evidence to say that the BEMNA requires less number of function evaluations than AMaLGaM to reach the desired precision.
- In 6 out of 8 problems the AMaLGaM has slightly better distance to the optimum fitness than the BEMNA. However this might not be of great importance because both algorithms have already reached the desired precision.
- The BEMNA requires a smaller population size than the AMaLGaM.

50 independent executions in the other 8 benchmark multimodal problems, are shown in Table II-bottom. These present the following evidence:

- Both algorithms resulted in 3 out of 8 problems remaining unsolved: Rastrigin, Drop Wave and Salomon.
- Considering the 5 solved problems, the AMaLGaM has a slightly better success rate in 2 of them, presenting a considerable difference only in one of the problems: Bohachevsky.
- The BEMNA reaches slightly better fitness values in 3 out of 5 unsolved problems.
- The BEMNA requires fewer evaluations than the AMaLGaM in 4 out of 5 solved problems.

TABLE II. COMPARISON BETWEEN BEMNA AND AMALGAM METHODS IN 30 DIMENSIONS. THE WINNER IS MARKED IN BOLOFACE ACCORDING TO A NON-PARAMETRIC BODTSTRAP TEST. FURTHER DETAILS IN SECTION V.


This comparison at fixed 50 dimension problems shows that BEMNA have a better performance than the AMaLGaM in most of the benchmark functions. Despite the differences between both methods, we can conclude that the BENMA does not present any inconvenience to adequately adapt the covariance matrix as demanded by the problem.

## VI. CONCLUSIONS

This paper proposes to approximate the Multivariate Normal Density to the Boltzmann density by minimizing the Kullback-Leibler divergence. The first contribution is the derivation of parameter estimators, extending previous related work in one dimension to multidimensional problems [14]. The derived formulae for computing the search distribution use the

objective function as well as a ranking value as linear factors for estimating weighted parameters.

The linear weights avoid prematurely collapsing the probability mass around a single solution, preventing premature convergence. In addition, this fashion of parameter estimation produces a softer change in the structure of the covariance matrix between consecutive generations, in contrast to the exponential weights used in similar approaches [13]. The advantage of using linear weights, even with a fixed $\beta$ value, is well documented in [14].

We propose a change of variable in order to use a parameter $\gamma$, instead of the usual $\beta$ variable, which is easier to control than the first one. Also, it permits the development of a simple but powerful annealing schedule to control the exploration and exploitation.

One of the most important contributions of this work is the formula in Equation (17). Usually EDAs intend to estimate a parametric probability distribution which best fits the data. Our proposal is conceptually different, in the sense that it poses the probability mass in the most promising region by using a mean estimator weighted by the objective function, while the structure of the probability function is oriented to the maximum improvement direction. The conclusions elucidated from this different point of view are the following:

- While the current population or selected set indicates where the most promising regions are, the difference between the worst individuals to the best ones indicates the direction where the population must move to.
- Most other EDAs are conceptually built on the basis that the structure of the adequate distribution must be the same as that in the current population. We propose that the structure of the adequate distribution could be inferred from the current population but it does not follow the same structure. The conceptual basis of our proposal is that the best structure must be oriented in agreement with the maximum improvement direction.

Statistical results support that BEMNA is competitive with state of the art algorithms, considering that AMaLGaM has been contrasted with other competitive algorithms as well. Furthermore, the results demonstrate that the BEMNA effectively tackles the Rosenbrock problem, which is not solved by similar algorithms [13] and [14].

Future work will contemplate the proposal of additional enhancement techniques to be applied over the current BEMNA for reducing the population size, as well as the number of function evaluations. Moreover, we will explore new ways to use the ideas developed in this article in other evolutionary algorithms.
