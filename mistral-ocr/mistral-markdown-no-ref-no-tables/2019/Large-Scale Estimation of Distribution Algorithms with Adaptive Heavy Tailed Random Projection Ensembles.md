# Large-Scale Estimation of Distribution Algorithms with Adaptive Heavy Tailed Random Projection Ensembles 

Momodou L. Sanyang ${ }^{1,2}$ and Ata Kabán ${ }^{1}$, Member, IEEE<br>${ }^{1}$ School of Computer Science, University of Birmingham, Edgbaston, Birmingham B15 2TT, U.K.<br>${ }^{2}$ School of Information Technology and Communication, University of The Gambia, Serekunda, The Gambia<br>E-mail: MLSanyang@utg.edu.gm, A.Kaban@cs.bham.ac.uk

Received September 6, 2018; revised September 13, 2019.


#### Abstract

We present new variants of Estimation of Distribution Algorithms (EDA) for large-scale continuous optimisation that extend and enhance a recently proposed random projection (RP) ensemble based approach. The main novelty here is to depart from the theory of RPs that require (sub-)Gaussian random matrices for norm-preservation, and instead for the purposes of high-dimensional search we propose to employ random matrices with independent and identically distributed entries drawn from a $t$-distribution. We analytically show that the implicitly resulting high-dimensional covariance of the search distribution is enlarged as a result. Moreover, the extent of this enlargement is controlled by a single parameter, the degree of freedom. For this reason, in the context of optimisation, such heavy tailed random matrices turn out to be preferable over the previously employed (sub-)Gaussians. Based on this observation, we then propose novel covariance adaptation schemes that are able to adapt the degree of freedom parameter during the search, and give rise to a flexible approach to balance exploration versus exploitation. We perform a thorough experimental study on high-dimensional benchmark functions, and provide statistical analyses that demonstrate the state-of-the-art performance of our approach when compared with existing alternatives in problems with 1000 search variables.


Keywords covariance adaptation, estimation of distribution algorithm, random projection ensemble, $t$-distribution

## 1 Introduction

Optimisation over high-dimensional search spaces is a key task in many modern applications, including scientific, engineering and management problems. Estimation of Distribution Algorithms (EDAs) are black-box optimisation methods based on probabilistic modelling, which are becoming increasingly important in the evolutionary computation (EC) community ${ }^{[1]}$. EDAs avoid the usage of arbitrary operators of traditional EC approaches; instead they estimate a probabilistic model from the fittest individuals, and advance the search for the global optimum by sampling the estimated model. In this way, EDAs will not only simplify the design of an optimisation method, but also allow the algorithms to learn the structure of the search space and guide the search in further promising directions ${ }^{[2]}$.

However, the performance of most existing EDAs deteriorates significantly in high-dimensional search spaces. This is because EDA requires model building from empirical data, which is susceptible to the curse of dimensionality ${ }^{[3]}$. Unless an enormous budget of fitness evaluations is available, the sample size is insufficient for reliable model estimation. Consequently the structure of the problem is often severely mis-estimated from limited samples (see $[4,5]$ for examples). In turn, a badly estimated model typically results in premature convergence ${ }^{[5]}$.

To mitigate the curse of dimensionality, simplified models such as univariate models, or limited dependency models are often preferred instead of a full multivariate model in practice. The simplest of such approach is described in [6], called UMDAc. The

[^0]
[^0]:    Regular Paper
    The work of Momodou L. Sanyang was partly funded by a Ph.D. scholarship from the Islamic Development Bank. The work of Ata Kabán is funded by the Engineering and Physical Sciences Research Council of UK under Fellowship Grant EP/P004245/1.
    (C) 2019 Springer Science + Business Media, LLC \& Science Press, China

model building in this univariate approach is simply done under the independence assumption ${ }^{[6]}: P(\boldsymbol{x})=$ $\prod_{i=1}^{d} P\left(x_{i}\right)$, where $d$ is the dimensionality of the search space. More refined approaches such as the sep-CMA$\mathrm{ES}^{[7]}$ and the univariate AMaLGaM ${ }^{[8]}$ use only diagonal elements of a rotated full covariance matrix. However, the univariate models assume that all the variables are independent in some coordinate basis; hence they may be expected to perform well on problems that have no dependency between variables (i.e., separable) in that basis.

Non-separable problems are those in which the above assumption does not hold, that is, the design variables have multiple inter-dependencies. The approach known as MIMIC, proposed by De Bonet et al. ${ }^{[9]}$ sets out to capture bivariate interactions between decision variables by sampling from the pairwise joint distribution between variables. Despite that MIMIC is able to outperform univariate models, the majority of optimisation problems will have larger groups of interacting design variables. Several proposals have been put forth to explicitly capture multivariate dependencies by building graphical dependency networks, for example Bayesian Networks ${ }^{[10]}$. But, from statistical, computational and memory points of view, learning probabilistic graphical models from the sample of fit individuals is highly expensive and requires a large sample ${ }^{[11]}$. Thus, the scaling-up of these model building processes to highdimensional problems remains challenging.

### 1.1 Related Work in Large-Scale Black-Box Optimisation

There have been many efforts to alleviate the problems of high-dimensional search, resulting in several algorithms being proposed recently, including EDA-type methods. Here we limit ourselves to a few that are most relevant to the present work. Approaches can be grouped into cooperative co-evolution based methods, evolutionary strategies, latent variable models, hybrid methods, and compression based divide and conquer.

One of the first cooperative co-evolution (CC) methods is CC with Variable Interaction Learning (CCVIL) proposed by Weicker and Weicker in [12]. It is a deterministic method to uncover dependencies between decision variables. A more recent model-based formulation of a similar idea is EDA with Model Complexity Control (EDA-MCC) ${ }^{[13]}$, which also employs a deterministic algorithm; it groups variables into two disjoint subsets, those that are weakly correlated with other variables,
and those that are strongly correlated. The strength of correlations is estimated relative to a threshold.

Multilevel cooperative co-evolution (MLCC) proposed in [14] groups the decision variables of a problem randomly to tackle problems in high-dimensional optimisation. The groups are then optimised jointly, but separately from other groups.

MA-SW-Chain ${ }^{[15]}$ is a hybrid algorithm that assigns local search intensity to each individual by chaining dissimilar local search applications. It is an extension of the MA-CMA-Chain algorithm for high-dimensional regime, and was the winner of the CEC2010-2012 largescale global optimisation competition on 1000 dimensional benchmark problems.

Another related method employs latent variable models to sample new individuals with low-dimensional latent vectors. Shin et al. ${ }^{[16]}$ proposed a latent variable model such as the Helmholtz machine and probabilistic principal component analysis to estimate the probability distribution of given data. The model considers latent variables which have a much lower dimension than input variables for optimising a high-dimensional function. In doing so, the method will mitigate the curse of dimensionality. A different way to exploit hidden low-dimensional structure was proposed in [17], suggesting that a notion of the intrinsic dimension of a function can replace the ambient dimension of the inputs to the function, provided that the function has a special structure. However, in the absence of this structure this method is unsuitable.

A recent approach is the random matrix theory based EDA in [4], which devises a compression-based divide and conquer strategy. The idea is to project the high-dimensional selected individuals to many independent low-dimensional random subspaces, carry out the costly sampling and estimation operations concurrently in these subspaces, and combine the new samples to form the next generation. Such ensemble can exhibit a strong smoothing effect that facilitates the estimation from small samples.

### 1.2 Contributions

In this paper, we further enhance the random projection (RP) ensemble approach of [4], by employing a parameterised family of heavy-tailed random matrices to replace the more conventional sub-Gaussian ones. Although this results in a minor change in the implementation, as we shall see, it allows for a better exploration of high-dimensional search spaces. An early version with promising empirical results of this idea ap-

peared in $[18]^{\text {® }}$.

The increased exploration abilities of heavy tailed distributions are well known in evolutionary search, starting from pioneering work by Yao et al. ${ }^{[19]}$ in the univariate setting, and more recent work in the multivariate EDA framework (see, e.g., [20-22] and references therein). However, in the regime of large search spaces of dimensionality well beyond 100 variables, the use of such heavy tailed distributions in EDA is not straightforward - as demonstrated in [22], a heavy tailed search distribution becomes increasingly counterproductive as it loses sight of the direction of the search. Here we avoid these problems as we employ heavy tailed distributions in a combination of RPs rather than directly in the role of a search distribution.

Our approach is based on a detailed analysis of the effect of the distribution of entries of random matrices used in the algorithm in terms of the resulting aggregated covariance of the multivariate search distribution (which is not heavy tailed but Gaussian, as we shall see later). We should also note that this type of analysis is entirely different, and complementary with analyses of the dynamics or the running time, as the latter is currently feasible only in univariate models on some very specific problems ${ }^{[23]}$. The purpose of our analysis in this work is 1) to shed light on some limitations of borrowing existing tools from the area of RPs as done in previous work, and 2) to construct novel algorithm variants that bypass these limitations.

In particular, our analysis reveals that, while the use of RPs is useful for dealing with high-dimensional optimisation problems, the existing RP theory is not well aligned with the needs of optimisation. More precisely, the use of sub-Gaussian RP matrices has been originally borrowed from a literature that aims at approximately preserving Euclidean geometry. This goal is different from ours and, as we shall see, adopting the same approach falls short of exploration ability for search. In turn, the use of heavy tailed random matrices is very unusual in the context of the RP literature, as they do not have good distance preservation properties, but they will turn out to have advantages for high-dimensional search.

The specific contributions of this paper are as follows.

- We analytically show that the excess kurtosis of the entries of the RP matrices in the ensemble has a precise role in the aggregated covariance of the ensemble. The latter is the covariance of the high-dimensional
search distribution; therefore this analysis reveals the following: a distribution with negative excess kurtosis will shrink the aggregated covariance in comparison with that obtained when using the Gaussian distribution, and a distribution with positive excess kurtosis will enlarge it.
- We then propose to employ random matrices with i.i.d. $t$-distributed entries - this subsumes the Gaussian ensemble of [4] as a special case, when the degree of freedom is infinite. However, the degree of freedom parameter offers a means to enlarge the aggregated covariance in favour of better exploration in high dimensions. In particular, we show that the extent of this enlargement is a decreasing function of the degree of freedom parameter.
- Based on this, we then develop simple methods to adapt the degree of freedom parameter during the search, which essentially implement novel covariance adaptation schemes specifically for high-dimensional search.
- We present a thorough experimental study on 1000 -dimensional multi-modal test functions from the CEC2010-2012 large-scale global optimisation competition benchmark, and demonstrate the superior or state-of-the-art performance in statistical comparisons with a number of existing alternatives.


## 2 Heavy-Tailed Random Matrices for Continuous EDA Optimisation

Random projections (RP) have already been used with success in large-scale continuous EDA ${ }^{[4]}$. However the theory of RP in the literature is aimed at the preservation of the Euclidean distances and norms. The goal in optimisation is different: it is more important to have a good exploration-exploitation trade-off.

With this goal in mind, in this section we shall present an RP ensemble based large-scale multivariate Gaussian EDA that employs random matrices with heavy tailed entries drawn i.i.d. from the family of $t$ distributions. We shall present this algorithm first, to fix ideas, so that we see how these random matrices enter into the search algorithm. We will then analytically justify our choice for the family of $t$-distributions afterwards in the subsequent subsection.

### 2.1 tRP-Ens-EDA Algorithm: A Basic Variant

Our algorithm is a modification of the random projection ensemble based EDA (RP-Ens-EDA) of [4], and

[^0]
[^0]:    (1) Received a Runner-Up Student Paper Award of the CEC2015 Conference.

we refer to our new variant as tRP-Ens-EDA. The pseudo-code of tRP-Ens-EDA is given in Algorithm 1.

```
Algorithm 1. Algorithm with Entries of \(\boldsymbol{R}_{\boldsymbol{i}}\) from \(t\)-Distr-
    ibution (tRP-Ens-EDA)
    Input: \(k, M, N\), MaxFE
    Output: best individual \(\boldsymbol{x}^{*}\) : best fitness \(f^{*}\)
    \(\mathcal{P} \leftarrow\) Initialize a population uniformly at random in the
    search space
    \(\nu \leftarrow\) Initialize a degree of freedom
    while \(\operatorname{MaxFE}>0\) do
        MaxFE \(\leftarrow\) MaxFE \(-\mathrm{N}\)
        \(\boldsymbol{f} \leftarrow\) Evaluate the fitnesses of \(\mathcal{P}\)
        \(\mathcal{P}^{\mathrm{fit}} \leftarrow\) Select the \(T\) individuals of \(\mathcal{P}\) with best fitness
        using truncation selection
        \(\boldsymbol{x}^{*} \leftarrow\) the individual with the optimal fitness so far
        \(f^{*} \leftarrow\) the optimal fitness value so far
        \(\nu \leftarrow\) Decide a new \(\nu\) with an adaptive method
        \(\mu \leftarrow\) Estimate the mean of \(\mathcal{P}^{\mathrm{fit}}\) using maximum
        likelihood estimation (MLE)
        \(\mathcal{P}^{\mathrm{fit}} \leftarrow \mathcal{P}^{\mathrm{fit}}-\boldsymbol{\mu}\)
        \(\left\{\boldsymbol{R}_{i}\right\}_{i=1: M} \leftarrow\) Generate \(M\) independent random
        matrices with entries drawn i.i.d. from a
        \(t\)-distribution with mean 0 and variance \(\frac{1}{d}\)
        foreach \(i \in\{1,2, \ldots, M\}\) do
            \(\frac{\boldsymbol{\gamma}^{\boldsymbol{R}_{i}}}{\boldsymbol{\gamma}^{\boldsymbol{R}_{i}}} \leftarrow \boldsymbol{R}_{i} \mathcal{P}^{\mathrm{fit}}\) projects \(\mathcal{P}^{\mathrm{fit}}\) to a random
            \(k\)-dimensional subspace
            \(\boldsymbol{\Sigma}^{\boldsymbol{R}_{i}} \leftarrow\) Estimate the \(k \times k\) covariance matrix of
            \(\boldsymbol{\gamma}^{\boldsymbol{R}_{i}}\) using MLE
            Sample \(N\) new points \(\boldsymbol{y}_{1}^{\boldsymbol{R}_{i}}, \ldots, \boldsymbol{y}_{N}^{\boldsymbol{R}_{i}}\) i.i.d. from
            \(N\left(\mathbf{0}, \boldsymbol{\Sigma}^{\boldsymbol{R}_{i}}\right)\)
        \(\mathcal{P}^{\text {norm }} \leftarrow\)
        \(\sqrt{\frac{d M}{k}}\left[\frac{1}{M} \Sigma_{i=1}^{M} \boldsymbol{R}_{i}^{T} \boldsymbol{y}_{1}^{\boldsymbol{R}_{i}}, \ldots, \frac{1}{M} \Sigma_{i=1}^{M} \boldsymbol{R}_{i}^{T} \boldsymbol{y}_{N}^{\boldsymbol{R}_{i}}\right]+\boldsymbol{\mu}\)
        \(\mathcal{P} \leftarrow \mathcal{P}^{\text {norm }}\)
    Replace an individual in \(\mathcal{P}\) with \(\boldsymbol{x}^{*}\) (elitism)
```

The tRP-Ens-EDA proceeds by initially generating a population of individuals randomly everywhere in the search space, and selects the $T$ fittest ones based on their fitness values. This is the set $\mathcal{P}^{\text {fit }}$ in Algorithm 1. $M$ independent random projection (RP) matrices $\boldsymbol{R}_{i}$ are then generated, and each defines a random subspace of dimension $k \ll d$, where $d$ is the dimension of the search space. These are created in order to project the fittest individuals onto low-dimensional subspaces defined by them.

The number of such subspaces, $M$, and their dimension, $k$, are parameters of the method along with the population size $N$. For all of these parameters we will use the default values determined in [4], i.e., $M=\left\lceil\frac{3 d}{k}\right\rceil$, $k=3, N=300$, and $\left|\mathcal{P}^{\text {fit }}\right|=N / 4$, as the context and meaning of these parameters is the same as in [4]. Another input parameter is the maximum fitness evaluations allowed, MaxFE, which will be varied depending on the goal of the experiments.

Once the set $\mathcal{P}^{\text {fit }}$ is determined, its sample mean is estimated in step 10 and used to center the points in
step 11. The entries of the RP matrices $\boldsymbol{R}_{i}$ are drawn i.i.d. from a $t$-distribution with mean 0 and variance $\frac{1}{d}$. This is the only difference from the original RP-EnsEDA ${ }^{[4]}$. It is implemented by sampling from $t(0,1, \nu)$ first, and then multiplying the samples by $\sqrt{\frac{\nu-d}{\nu d}}$ so that their variance becomes $1 / d$. This choice for the variance is to ensure that we recover the original scale in step 17 without having to modify the scaling factor of the original RP-Ens-EDA. When $d$ is large, $\boldsymbol{R}_{i}$ has nearly orthonormal rows, as a result of the concentration of norms in high dimensions, since the coordinates in each row are independent - this is a very generic property of high-dimensional probability spaces that both [4] and our method exploit. Therefore, premultiplying with $\boldsymbol{R}_{i}$ is almost like orthogonally projecting the points from the $d$-dimensional space to a $k$-dimensional subspace, which shortens the lengths of vectors by a factor of $\sqrt{\frac{k}{d}}$, and the standard deviation gets reduced by a factor of $\sqrt{M}$ after averaging. Therefore, the scaling factor needed to recover the original scale is $\sqrt{\frac{d M}{k}}$.

Step 14 projects the good samples, $\mathcal{Y}^{\boldsymbol{R}_{i}}$ down to the subspaces of dimension $k$, and then estimates the $k \times k$ covariance matrices in each subspace and samples $N$ new points in each subspace using $k$-dimensional multivariate Gaussian distributions. Step 17 averages the obtained points from these subspaces to produce the new population $\mathcal{P}$. In addition, we will use elitism in practice, thereby the best fitness individual always survives to the next generation.

### 2.2 Why $t$-Distributed Random Projections

Let us restrict our attention to the procedure by which the new generation is created, as this is what distinguishes our algorithm from the vanilla multivariate EDA. We want to analyze the aggregated covariance that the ensemble of RP creates implicitly, which is in fact the covariance of the high-dimensional search distribution that the new generation follows.

Our analysis will allow quite general RP matrices, and only require their entries to be drawn i.i.d. from a 0 -mean symmetric distribution having finite first four moments. This includes the Gaussian, all subGaussians, and the family of $t$-distributions with the degree of freedom at least 5 . We take advantage of this generality to develop our arguments and explain our choice for the $t$-distributions, which, for readers familiar with the random projection literature, may seem very unusual.

We start by computing the covariance of the new population in step 17 of Algorithm 1, conditional on fixing the random projection matrices $\boldsymbol{R}_{i}, i=1: M$. We will then condition on the sample of fit individuals and look at the effect of $\boldsymbol{R}_{i}, i=1: M$ by computing the expectation of this ensemble covariance with respect to $\boldsymbol{R}_{i}, i=1: M$. If $M$ is large enough, this expectation approximates well the finite $M$ case. Moreover, although not pursued here, tools from [24] may be used to determine the sufficient ensemble size.

Proposition 1. Conditionally on $\boldsymbol{R}_{i}, i=1: M$, the new generation produced at step 17 of Algorithm 1 is i.i.d. Gaussian with mean $\boldsymbol{\mu}$ and $d \times d$ covariance of the following form:

$$
\boldsymbol{\Sigma}_{r p}=\frac{d}{k M} \sum_{i=1}^{M} \boldsymbol{R}_{i}^{\mathrm{T}} \boldsymbol{R}_{i} \boldsymbol{\Sigma} \boldsymbol{R}_{i}^{\mathrm{T}} \boldsymbol{R}_{i}
$$

where $\boldsymbol{\Sigma}$ is the maximum likelihood sample covariance of the original selected individuals in $\mathcal{P}^{\mathrm{fit}}$.

The proof is given in Appendix A1.
Next, we want to see the effect of the random $\boldsymbol{R}_{i}$ 's on $\boldsymbol{\Sigma}_{r p}$. To this end, we condition on $\boldsymbol{\Sigma}$, and look at the expectation $E_{\boldsymbol{R}}\left[\boldsymbol{\Sigma}_{r p}\right]$.

We require the following definition.
Definition 1. The excess kurtosis of a random variable $x$ is defined as:

$$
K=\frac{E\left[x^{4}\right]}{E\left[x^{2}\right]^{2}}-3
$$

We have the following result.
Theorem 1. Let $\boldsymbol{R}$ be a $k \times d$ random matrix, $k<d$, with entries drawn i.i.d. from a symmetric distribution with 0 -mean, finite first four moments, and excess kurtosis $K$. Let $\boldsymbol{\Sigma}$ be a $d \times d$ fixed positive semidefinite matrix with eigenvalues $\lambda_{1}, \ldots, \lambda_{d}$.

$$
\begin{aligned}
& E_{\boldsymbol{R}}\left[\boldsymbol{\Sigma}_{r p}\right] \\
= & \frac{1}{d}\left[(k+1) \boldsymbol{\Sigma}+\operatorname{Tr}(\boldsymbol{\Sigma}) \boldsymbol{I}_{d}+K \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}\right]
\end{aligned}
$$

where $\boldsymbol{A}_{i}$ is $d \times d$ diagonal matrices with their $j$-th diagonal elements being $\sum_{a=1}^{d} U_{a i}^{2} U_{a j}^{2}$ and $U_{a i}$ is the $a$-th entry of the $i$-th eigenvector of $\boldsymbol{\Sigma}$.

Proof. From (1), the expectation of $\boldsymbol{\Sigma}_{r p}$ is $\frac{d}{k} E_{\boldsymbol{R}}\left[\boldsymbol{R}^{\mathrm{T}} \boldsymbol{R} \boldsymbol{\Sigma} \boldsymbol{R}^{\mathrm{T}} \boldsymbol{R}\right]$, which we compute using a result from [25], originally derived in a very different context (namely to analyze compressive least square regression).

Under the condition on $\boldsymbol{R}$ stated in Theorem 2, Lemma 2 from [25] proved that

$$
\begin{aligned}
& E\left[\boldsymbol{R}^{\mathrm{T}} \boldsymbol{R} \boldsymbol{\Sigma} \boldsymbol{R}^{\mathrm{T}} \boldsymbol{R}\right] \\
= & k \times E\left[R_{i, j}^{2}\right]^{2}\left[(k+1) \boldsymbol{\Sigma}+\operatorname{Tr}(\boldsymbol{\Sigma}) I_{d}+K \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}\right]
\end{aligned}
$$

where $\boldsymbol{A}_{i}$ is the diagonal matrices defined as in Theorem 1 , and $R_{i j}$ is a generic entry of matrix $\boldsymbol{R}$.

Now, by design, we have $E\left[R_{i j}^{2}\right]=\frac{1}{d}$. Replacing (3) into (1) completes the proof.

Observe that from the definition of the matrices $\boldsymbol{A}_{i}$, and since $\boldsymbol{\Sigma}$ is positive semi-definite, $\lambda_{i}$ is non-negative - consequently the sum in the last term in the brackets in (2), that is, $\sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}$, is always a diagonal matrix with non-negative diagonal entries.

Now, let us look at the multiplier of this term, $K$. In previous work ${ }^{[4]}$ the entries of $\boldsymbol{R}$ were Gaussian or sub-Gaussian. In the Gaussian case, $K=0$. Hence in that case the last term cancels out: $K \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}=0$. Nevertheless, what remains is a regularised version of the sample covariance estimate $\boldsymbol{\Sigma}$. This is always nonsingular, thereby the search does not get stuck in a subspace of the search space.

However, if the entries of $\boldsymbol{R}$ are drawn from a subGaussian distribution, we find that certain choices may be a bad idea - it depends on the excess kurtosis of the distribution.

Indeed, take the Rademacher distribution below, and note this is sub-Gaussian:

$$
R_{i j} \sim_{\text {i.i.d. }} \begin{cases}1, & \text { with probability } 1 / 2 \\ -1, & \text { with probability } 1 / 2\end{cases}
$$

Random matrices with i.i.d. entries from this distribution have been originally proposed by [26] as an implementation-friendly alternative to the Gaussian RP, and it was subsequently considered for RP-EDAEnsemble optimisation in [4].

It is easy to check that for this distribution we have $E\left[R_{i j}^{4}\right]=1$, and $E\left[R_{i j}^{2}\right]=1$. Therefore, the excess kurtosis is $K=1-3=-2$. Consequently, $K \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}=-2 \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}$. This is a diagonal matrix with all non-positive diagonal entries. Therefore this term diminishes the regularisation effect of the term $\operatorname{Tr}(\boldsymbol{\Sigma}) \boldsymbol{I}_{d}$ in (2). It also shrinks the ensemble covariance matrix in comparison with that of a Gaussian RP ensemble.

We can go even further, and construct a simple example where the term $K \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}$ cancels out the effect of $\operatorname{Tr}(\boldsymbol{\Sigma}) \boldsymbol{I}_{d}$ completely in some directions of the

search space, thereby we are left with maximum likelihood estimates in those directions that may be not sufficiently accurate due to the small number of highfitness individuals relative to the high-dimensionality of the search space. We give such an example in Appendix A2.

Although such examples may seem contrived, the shrinking effect of distributions with negative kurtosis is undesirable for search, and instead we would like to use the insights of this analysis to come up with a better alternative.

If $K>0$, then the term, $K \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}$, is a diagonal positive semi-definite matrix; hence it always adds a non-negative quantity to the diagonals of the ensemble covariance. Hence, our idea is to use a family of distributions with positive kurtosis, and moreover, adapt $K$ during the search. Based on the discussion above, this would enlarge the covariance $E_{\boldsymbol{R}}\left[\boldsymbol{\Sigma}_{r p}\right]$ adaptively to the necessary extent. Covariance adaptation has been a successful technique in the EDA literature ${ }^{[27]}$, and our idea makes it feasible to implement it in new ways, specifically for large-scale EDA search through a more suitable random projection ensemble.

To achieve this, we have chosen the family of $t$ distributions with degree of freedom at least 5. Indeed, for this family of distributions the following holds.

Proposition 2. The excess kurtosis of $t(0,1, \nu)$ distribution with the degree of freedom $\nu$ is:

$$
K=\frac{6}{\nu-4}, \quad \text { provided } \nu>4
$$

The proof is given in Appendix A3.
Corollary 1 (to Proposition 2). Changing the variance leaves the excess kurtosis unchanged.

The proof is immediate and given in Appendix A3 for completeness.

We replace this into Theorem 1, and obtain the following.

Theorem 2. If $\boldsymbol{R}$ is sampled i.i.d. from a $t$ distribution with degree of freedom $\nu \geqslant 5$, mean 0 and variance $1 / d$, then the ensemble covariance for the highdimensional search distribution is:

$$
\begin{aligned}
& E_{\boldsymbol{R}}\left[\boldsymbol{\Sigma}_{r p}\right] \\
= & \frac{1}{d}\left[(k+1) \boldsymbol{\Sigma}+\operatorname{Tr}(\boldsymbol{\Sigma}) \boldsymbol{I}_{d}+\frac{6}{\nu-4} \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}\right]
\end{aligned}
$$

where the matrices $\boldsymbol{A}_{i}$ are the same as defined in Theorem 1.

The Gaussian RP corresponds to $\nu \rightarrow \infty$, in which case the last term in the bracket in (4) vanishes:
$\lim _{\nu \rightarrow \infty} \frac{6}{\nu-4} \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}=0$. In turn, by any finite choice of the degree of freedom parameter for the $t$ distribution we will be adding a positive semi-definite matrix to this covariance - this makes it larger and gives it more chance to explore the search space.

## 3 Adaptive Degree of Freedom Parameter

In this section we devise methods to adapt the parameter $\nu$ during the search.

Parameter setting methods are dichotomised into tuning and controlling ${ }^{[28]}$. Tuning means finding a good value by trial and error before running the algorithm and then fixing this value throughout the evolutionary process. While it may seem convenient, the trial-and-error phase consumes part of the budget of function evaluations. On the other hand, parameter control starts with an initial value which is then updated during the search, based on partial outcomes of the algorithm ${ }^{[28]}$. In other words, controlling tries to adapt the control parameters automatically in order to adjust the algorithm to the problem during the search ${ }^{[29]}$. Hence controlling methods need us to devise an algorithm that acts as an adaptation strategy. This is what we pursue in the remainder of this section.

In the sequel we present three different adaptation schemes. In each of these, the parameter we try to control is the degree of freedom of the $t$-distributed entries of our random projection matrices $\left(\boldsymbol{R}_{i}, i=1: M\right)$.

To simplify the computations we shall approximate $\boldsymbol{\Sigma}_{r p}$ by an upper bound on it in positive semi-definite ordering, which is independent of the eigenvectors of $\boldsymbol{\Sigma}$. Observing that $\sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i} \preceq \operatorname{Tr}(\boldsymbol{\Sigma}) \cdot I_{d}$, we have:

$$
E_{\boldsymbol{R}}\left[\boldsymbol{\Sigma}_{r p}\right] \preccurlyeq \frac{1}{d}\left[(k+1) \boldsymbol{\Sigma}+\operatorname{Tr}(\boldsymbol{\Sigma}) \boldsymbol{I}_{d}\left(1+\frac{6}{\nu-4}\right) \boldsymbol{I}_{d}\right]
$$

### 3.1 Adaptive Variance Scaling (AVS) Based Method

An adaptive variance scaling (AVS) method was originally proposed for EDA by Grahl et al. ${ }^{[27]}$ In each generation, it decides how to update a parameter for the next generation based on the "difference in the best fitness" between the latest two consecutive generations. The original approach ${ }^{[27]}$ is to scale the sample covariance matrix $\boldsymbol{\Sigma}$ multiplicatively, by a value $c \in[1,10]$, where $c$ is adapted (i.e., either increased or decreased) by a coefficient $\eta \in(0,1)$ as follows. If the best fitness improved then $c$ is increased as $c / \eta$ in order to explore; otherwise $c$ is decreased as $c \eta$ for exploitation. The authors of [27] put $c$ to 10 if it becomes greater than 10 or

smaller than 1, in order to stimulate exploration while preventing a blow-up of the covariance.

Note in our context of RP ensemble based algorithm, we do not need to artificially introduce the $c$ parameter as the original AVS does, as we can use the degree of freedom parameter $\nu$ to emulate the updating heuristic of the original AVS. The pseudo-code of this adaptation scheme is given in Algorithm 2.

```
Algorithm 2. Adaptive Variance Based Method (AVS)
    Input: index of current generation \(t\); degree of freedom
        \(\nu^{t}\) : best fitness \(b^{t}, b^{t-1}\); coefficient \(\eta\)
    Output: degree of freedom \(\nu^{t+1}\)
    \(c \leftarrow 1+\frac{b}{\nu^{t}-4}\)
    if \(b^{t}\) is no better than \(b^{t-1}\) then
    \(\quad c \leftarrow c \eta / / c\) gets smaller, \(\nu\) gets larger
    else
    \(\leftarrow \quad c \leftarrow c / \eta / / c\) gets larger, \(\nu\) gets smaller
    \(\nu^{t+1} \leftarrow \frac{b}{\nu-1}+4\)
    if \(\nu^{t+1}<5\) or \(\nu^{t+1}>124\) then
    \(\leftarrow \quad \nu^{t+1} \leftarrow 5 / /\) to stimulate exploration
```

From (4) we have seen that smaller values for $\nu$ allow for exploration and larger $\nu$-values encourage exploitation in tRP-Ens-EDA. We also observe that $\nu$ has a non-linear effect on the extent of enlarging the covariance of the new population. We set:

$$
c=1+6 /(\nu-4)
$$

which ensures that $\nu \geqslant 5$ as required so that we can directly apply the same adaptation rules as the original AVS approach of [27] as follows. Suppose the tRP-Ens-EDA is at its $t$-th generation, and we denote by $b^{t}$ and $b^{t-1}$ the best fitness values of the latest two generations respectively. Recall, tRP-Ens-EDA uses the elitism, thereby we will never observe a worse-than previous value of the best fitness. Therefore, our AVS will decrease $c$ (hence increase $\nu$ ) for exploitation if $b^{t}$ is no better than $b^{t-1}$ before the elitism is applied, and increase $c$ (hence decrease $\nu$ ) for exploration if $b^{t}$ is strictly better than $b^{t-1}$. This adaptation strategy is exactly the same as that originally proposed in [27], and the only difference is that it is now built into our RP-ensemble based EDA for large-scale searches.

Finally, from (5) we have:

$$
\nu=6 /(c-1)+4
$$

and as in the original method of [27], we will also constrain the range of $\nu \in[5,124]$, which corresponds to
$c \in[1.05,7]$. If $\nu$ goes beyond this range, then it is put to 5 to trigger exploration, which is the same strategy as in [27].

### 3.2 1/5-Success Rule Based Method

A classic alternative adaptation scheme is the wellknown $1 / 5$-success rule (or $1 / 5$ rule). It is one of the oldest adaptation heuristics, and it is widely used in evolutionary strategies (ES) ${ }^{[30]}$. The $1 / 5$ rule does not look at the improvement in the best fitness, but instead it looks at the overall fitness improvement of the population. It measures this as the following success probability:

$$
P_{s}=\frac{\text { number of individuals with improved fitness }}{\text { population size }}
$$

If $P_{s}>1 / 5$ then it is said that an improvement is detected. In our case, if such improvement is detected then we decrease $\nu$ for exploration; otherwise we increase $\nu$ in order to exploit - in the same manner as we did in AVS in Subsection 3.1.

However, in ESs it is easy to compute $P_{s}$, because the individuals can be compared with their parents after a mutation; but in EDA there is no explicit connection between a particular individual and its descendant in the next generation, as the new individuals are sampled from a probability distribution that the whole previous generation contributed to. To apply the $1 / 5$ rule in EDAs we use the following heuristic. At the $t$ th generation, given the fitness values of the population with $N$ individuals $\boldsymbol{f}^{t}$, and the fitness values of the individuals of the previous generation $\boldsymbol{f}^{t-1}$, we sort both $\boldsymbol{f}^{t}$ and $\boldsymbol{f}^{t-1}$, and compare between the corresponding elements $f_{i}^{t}$ and $f_{i}^{t-1}$, where $i \in\{1, \ldots, N\}$. This way we count the number of fitness values $f_{i}^{t}$ that are better than the corresponding $f_{i}^{t-1}$, and use this number in the expression of $P_{s}$.

The pseudo-code of this adapted $1 / 5$ rule for tRP-Ens-EDA is given in Algorithm 3. The algorithm first counts the number of improved individuals between the sorted fitness vectors of the two latest generations, and then calculates the success probability $P_{s}$. If $P_{s} \leqslant 1 / 5$, then the adaptive method decreases the value of $c$ (defined as before in (5)) and thus increases $\nu$ (defined in (6)) for the purpose of exploitation. Otherwise $c$ is increased, and thus $\nu$ is decreased, for exploration. This method shares with AVS the schemes of updating $c$ and thresholding $\nu$, namely it increases or decreases $c$ with a coefficient $\eta \in(0,1)$, keeps $\nu \in[5,124]$ and resets $\nu$

to 5 if it goes beyond the range in order to stimulate exploration.

```
Algorithm 3. 1/5-Success Rule Based Adaptive Method
    Input: population size N; index of current generation t;
        degree of freedom }\mp@subsup{}{t}{t}\mathrm{ , sorted fitnesses of the latest
        2 populations }\mp@subsup{f}{}{t} \& \mp@subsup{f}{}{t-1}\mathrm{ ; coefficient }\eta
    Output: degree of freedom }\mp@subsup{\nu}{t+1}\mathrm{
    \(c \leftarrow 1+\frac{n}{c \leftarrow t}\)
    \(N_{p} \leftarrow 0 / /\) counter of improved individuals
    for \(i=1: N\) do
        if \(f_{i}^{t}\) is better than \(f_{i}^{t-1}\) then
        \(N_{p} \leftarrow N_{p}+1\)
    \(P_{s} \leftarrow N_{p} / N / /\) success probability
    if \(P_{s} \leqslant 1 / 5\) then
        \(c \leftarrow c \eta / / c\) gets smaller, }\nu\mathrm{ gets larger
    else
        \(c \leftarrow c / \eta / / c\) gets larger, }\nu\mathrm{ gets smaller
    \(\nu^{t+1} \leftarrow \frac{n}{c \cdot t}+4\)
    if \(\nu^{t+1} \leqslant 5\) or \(\nu^{t+1}>124\) then
    \(\nu^{t+1} \leftarrow 5 / /\) to stimulate exploration
```


### 3.3 Adaptive Degree of Freedom (ADF)

Our third adaptation method will be a scheme where some backtracking is possible. The parameter updating decisions are made after trying out a list of alternative choices and observing their effects on the best fitness within each generation. We drew inspiration from [29] initially, and devise our own adaptation rules to fit the problem, bearing in mind that our parameter of interest must obey $\nu \geqslant 5$. The pseudo-code of our proposed adaptive method is given in Algorithm 4.

The adaptive method given in Algorithm 4 maintains a list of $L$ different alternative values of $\nu$ in ascending order, and in each generation it creates a separate trial (mock) new-generation using tRP-Ens-EDA with each of the $L$ different $\nu$ values on the current list. The list $L$ is initialised by taking the first $\nu$ values to be $6,7, \ldots, 6+L-1$ (all close to the smallest allowable value). The list is then updated based on the current best value, to be tried in the next generation. If the current list of $\nu$-values produces no difference to the fitness, then the list of values is spread out more (by decreasing the smallest and increasing all other $\nu$-values). Otherwise the algorithm updates the list of values to be tried in the next generation by bringing them closer to the current best $\nu$-value.

This adaptation scheme is direct and generic; however it has a tuning parameter that presents a trade-off: the length of the list of the $\nu$-values to try. Obviously, the longer the list, the higher the chance to find a good value within the generation, but the price is a quicker
drainage of the budget of fitness evaluations. We experimented with list lengths of $L=2$ and $L=5$ as representatives of this algorithm in our early work ${ }^{[18]}$, and had found $L=2$ to be a good value. Therefore we employ this in the experiments reported here, and will refer to our adaptation scheme as $\operatorname{ADF}(2 \mathrm{df})$.

```
Algorithm 4. Adaptive Degree of Freedom (ADF)
    Input: \(\vartheta\) (initial list of \(\nu\)-values in ascending order)
    Output: \(\nu\)
    \(L \leftarrow|\vartheta|\)
    for \(i=1: L\) do
        Run steps \(11-17\) and 5 of Algorithm 1 with \(\nu_{i}\)
        \(f_{i} \leftarrow\) best fitness from step 5 of Algorithm 1
    if \(\min (f)==\max (f)\) then
        \(\vartheta_{1} \leftarrow \max \left(5, \operatorname{round}\left(\vartheta_{1} / 2\right)\right)\)
        for \(j=2: L\) do
            \(\vartheta_{j} \leftarrow \vartheta_{j} \times 2\)
    else
        \(\ell \leftarrow \arg \min (f) ; \nu \leftarrow \vartheta_{\ell}\)
        if \(\ell==1\) then
            \(\vartheta_{1} \leftarrow \max \left(5, \operatorname{round}\left(\vartheta_{1} / 2\right)\right)\)
            for \(j=2: L\) do
            \(\vartheta_{j} \leftarrow \max \left(5, \operatorname{round}\left(\left(\vartheta_{j-1}+\vartheta_{j}\right) / 2\right)\right)\)
        else
            for \(j=1: \ell-1\) do
            \(\vartheta_{j} \leftarrow \max \left(5, \operatorname{round}\left(\left(\vartheta_{j}+\vartheta_{j+1}\right) / 2\right)\right)\)
            \(\vartheta_{\ell} \leftarrow \vartheta_{\ell}+\max \left(5, \operatorname{round}\left(\vartheta_{\ell} / 2\right)\right)\)
            for \(j=\ell+1: L\) do
            \(\vartheta_{j} \leftarrow \max \left(5, \operatorname{round}\left(\left(\vartheta_{j-1}+\vartheta_{j}\right) / 2\right)\right)\)
```

It follows from the construction of this method that ADF uses $L$ times as many fitness evaluations per generation as a fixed choice of $\nu$ would do, while the two adaptation heuristics presented in the previous subsections keep the same per-generation budget of fitness evaluations, since they make adaptation decisions sequentially, without the possibility of backtracking a parameter value after observing its effect on the fitness. Therefore we expect ADF to be more advantageous in terms of reaching a better fitness value when a sufficiently large budget is available, whereas the sequential heuristics may be preferable when the budget is relatively small. This will be assessed in more detail in Section 4.

## 4 Experiments

Initial experiments have indicated that the best choice of degree of freedom parameter is problemdependent ${ }^{[18]}$. Therefore we turn our attention to the adaptation approaches. We conduct a thorough set of experiments to assess our tRP-Ens-EDA with adaptation schemes on a battery of large-scale multi-modal benchmark problems, from the 1000 -

dimensional CEC2010-2012 competition test suite, as described in [31]. All problems are minimisations. Table 1 lists the test functions used in our experiments.

Table 1. 1000-Dimensional Multi-Modal Test Functions from the CEC2010-2012 Collection
In each experiment we initialize the population randomly in the search space. All the results in comparative experiments are obtained through fresh runs of the methods, except MA-SW-Chains whose results were obtained from the literature.

### 4.1 Results and Analysis

### 4.1.1 Comparative Assessment of Our Adaptation Schemes

In the first set of experiments we are interested in finding out whether our adaptive schemes can outperform the existing RP-Ens-EDA, and to learn about their respective advantages and disadvantages.

Table 2 provides a statistical analysis of comparisons on the 1000 -dimensional benchmarks. For each function, we compare our three different adaptive methods and the existing RP-Ens-EDA of [4] $(\nu=\infty)$. We report the average and the standard deviation (Std) of the best fitness achieved with the evaluation budget of $6 \times 10^{5}$ fitness evaluations, which is considered as medium budget in the benchmark problem description.

We perform a two-tailed $t$-test for each pair of methods involved in this comparison, and the symbols in the rightmost column of the table record statistically significant differences detected at the 0.05 level as follows. A symbol " + " indicates that the method in the corresponding row performed significantly better
than the method in the corresponding column. Likewise, "-" means that the method in the corresponding row performed significantly worse than the method in the corresponding column. Recall that all the test problems are minimisation problems, thereby lower fitness means better performance. The symbol $\varnothing$ appears where statistical comparison is not applicable. Positions left blank in the last column mean that no statistically significant difference was detected between the pair of methods tested.

Table 2. Statistical comparison of Our Adaptation Schemes and the Existing RP-Ens-EDA ${ }^{[4]}(\nu=\infty)$ on 1000-Dimensional Test Functions, with a Budget of $6 \times 10^{5}$ Function Evaluations
From the results listed in Table 2 we observe the followings.

- In nine (out of 11) of the test problems, no statistically significant difference is detected between the AVS and the $1 / 5$ adaptation heuristics.
- In the remaining two problems, AVS is statistically superior to $1 / 5$. On further investigation we observe that the $1 / 5$ approach has periods of stagnation where AVS is able to progress. This is most likely because the definition of $1 / 5$ in the context of EDA is rather ad hoc.
- AVS wins with statistical significance against the existing RP-Ens-EDA in seven (out of 11) test problems, and only loses in one (F4). The remaining three cases are ties.
- ADF performs on-par with AVS at this budget size: four wins and three losses against AVS, and it outperforms the existing RP-Ens-EDA in seven of the functions; it is outperformed by RP-Ens-EDA in two functions (F4 and F3), and two ties.

We then run the two most successful adaptation methods, $\operatorname{ADF}(2 \mathrm{df})$ and AVS, versus the existing RP-Ens-EDA for a larger budget size of $3 \times 10^{6}$. Fig. 1 shows the detailed trajectories, in order to visualize the behaviour of these methods and gain insight into the reasons for the observed differences. In Fig. 1 the best fitness is plotted against the elapsed number of function evaluations, averaged over 25 independent restarts. For clarity of visual inspection, these are zoomed into the interesting ranges of the axes: the fitness values of the first few generations are not shown, and the plotting halts when no more interesting change occurs.

We see from the trajectory plots on Fig. 1 that, given a sufficient budget, the direct adaptation method $\operatorname{ADF}(2 \mathrm{df})$ often reaches a better fitness value with a slight delay. This makes good sense intuitively too, based on the construction of the algorithm that spends part of its resources on exploring. Interestingly, it often goes through a period of stagnation before it wins over. For instance, on F3, with the medium budget size reported in Table 2 it was outperformed by all the other methods, including the previously existing RP-Ens-EDA, while from the trajectory plot we see that it does win eventually, given a larger budget, whereas the Gaussian variant makes no further progress. Indeed, we see from the trajectories in Fig. 1 that the Gaussian RP-Ens-EDA is more prone to premature convergence than our adaptive tRP-Ens-EDA variants. More differences between ADF and AVS will be seen in multi-comparison tests in the presence of other competing state-of-the-art
algorithms in Subsection 4.1.2.

### 4.1.2 Comparison with State-of-the-Art Methods on 1000-Dimensional Problems

We compare our best performing adaptive degree of freedom methods tRP-Ens-EDA(ADF) and tRP-Ens-EDA(AVS) with the existing state-of-the-art on the 1000-dimensional CEC2010-2012 competition multimodal benchmark problems.

Tables 3 and 4 and Tables 5 and 6 summarize the results from experiments with two different budged sizes respectively, from 25 repeated independent runs each. The average and the standard deviation of the best fitness values achieved are reported. By the Friedman's test and a subsequent multi-comparison, the means and the standard deviations of the best performing algorithms are marked in bold. The two budget sizes tested are $6 \times 10^{5}$ and $3 \times 10^{6}$, that is, a medium size budget and a large budget, according to the definitions in the benchmark suite.

The results are summarized in Tables 3-6. We see from these tables and Fig. 1 that our tRP-Ens-$\operatorname{EDA}(\mathrm{ADF})$ is most competitive in the high budget setting.

- In the medium budget setting $\left(0.6 \times 10^{6}\right.$ function evaluations), tRP-Ens-EDA(ADF) wins with statistical significance over all competitors tested in two of the test functions in the medium budget setting. AVS wins over all competitors tested in one function. In fact, tRP-Ens-EDA(AVS) does better than tRP-Ens-EDA(ADF) in terms of achieving lower fitness on a larger number of functions, but statistically significant out-performance is not observed in most of these cases in the multicomparison test.
- In the large budget setting $\left(3 \times 10^{6}\right.$ function evaluations), tRP-Ens-EDA(ADF) wins over all the other methods tested, including the winner of the CEC20102012 competitions ${ }^{[15]}$, in four test functions (out of 11 tested).

We can therefore conclude that a direct adaptation scheme like ADF turns most beneficial when we allow slightly larger budget sizes. In medium or limited budget settings we can recommend the AVS method.

Naturally, one cannot expect any method to perform best on all problems in the light of well known "no free lunch" theorems. However, the observed empirical results together with their statistical significance analysis support the conclusion that the methods presented in this paper are competitive with state-of-theart large-scale optimisation heuristics, and therefore

![img-0.jpeg](img-0.jpeg)

Fig. 1. Fitness trajectories of the RP-Ens-EDA, tRP-Ens-EDA(AVS) and tRP-Ens-EDA(2df) for a maximum of $3 \times 10^{6}$ function evaluations. For a statistical analysis of significance of the differences observed halfway through the budget, i.e., after $6 \times 10^{5}$ function evaluations (see Table 3 and Table 4). (a) Function F1. (b) Function F2. (c) Function F3. (d) Function F4. (e) Function F5. (f) Function F6. (g) Function F7. (h) Function F8. (i) Function F9. (j) Function F10. (k) Function F11.

Table 3. Mean of Best Fitness Values from 25 Independent Runs in Comparison with State-of-the-Art Under Equal Budget of $0.6 \times 10^{6}$ Function Evaluations
Table 4. Standard Deviation of Best Fitness Values from 25 Independent Runs in Comparison with State-of-the-Art under Equal Budget of $0.6 \times 10^{6}$ Function Evaluations
Table 5. Mean of Best Fitness Values from 25 Independent Runs in Comparison with State-of-the-Art under Equal Budget of $3 \times 10^{6}$ Function Evaluations
make a worthwhile addition to the practitioner's toolbox for use in difficult high-dimensional problems that no specialised algorithm is known to be able to solve. Moreover, our algorithm construction comes with a good intuition of its working strategy, which consists in a controlled increase of exploration in a similar spirit as the adaptive variance scaling idea previously pursued in [27], but now supporting much larger-scale problems
through an ensemble of RPs.

### 4.1.3 Scalability of ADF(2df)

Since our $\operatorname{ADF}(2 \mathrm{df})$ is the most expensive in terms of function evaluations per generation, our final set of experiments is to assess its scalability. We measure the number of function evaluations needed (search cost) to reach a specified distance from the global optimum

Table 6. Standard Deviation of Best Fitness Values from 25 Independent Runs in Comparison with State-of-the-Art under Equal Budget of $3 \times 10^{6}$ Function Evaluations
as the problem dimension varies. We fix the value to reach (VTR) to $10^{-3}$, and vary the dimensionality of the problem $d \in[50,1000]$. We repeat the same experiment with three other choices of VTR: $10^{-2}, 10^{2}$ and $10^{3}$ to avoid biasing the conclusions towards a particu-
lar choice of the VTR. Throughout, the budget was fixed to $3 \times 10^{6}$ thereby the algorithm stops either when the budget is exhausted or upon reaching the VTR. All other parameters are kept at their default values.
![img-1.jpeg](img-1.jpeg)

Fig.2. Number of function evaluations taken by successful runs of our tRP-Ens-EDA with ADF to reach a pre-specified "value to reach (VTR)" as the problem dimensionality is varied in $d \in[50,1000]$. The markers represent averages computed from 25 independent repetitions. The black dotted line corresponds to linear scaling (slope $=1$ ). (a) Shifted sphere function. (b) Shifted elliptic function. (c) Shifted Ackley function.

Fig. 2 displays the average number of function evaluations as computed from the successful runs out of 25 independent repetitions for each problem, for each dimension tested. That is, runs terminated by exhausting the budget do not contribute to these plots.

From Fig. 2 we observe a linear shape on the scalability measurements (dashed lines on the log-log plots). The black dotted line corresponds to the slope of 1 (that is, linear scaling) for reference. This means that our tRP-Ens-EDA with ADF scheme scales at most polynomially (with a degree indicated by the slope of lines) in the dimension of the problem, which matches the best scaling known for sep-CMA-ES ${ }^{[7]}$ and the original RP-Ens-EDA ${ }^{[4]}$.

## 5 Conclusions

We devised new adaptive approaches for highdimensional continuous black-box optimisation which extend and generalize the random projection ensemble based EDA by means of using unconventional random matrices. We analytically showed that this results in enlarging the covariance of the high-dimensional search distribution, which then increases exploration. Hence our adaptive schemes in fact implement novel means of covariance adaptation. We demonstrated superior performance against the original version RP-Ens-EDA on both large and medium budget instances, and with a state-of-the-art performance in comparison with a number of existing methods on 1000-dimensional problems. Future work remains to investigate other aggregation schemes, and to extend the method to multi-objective problems. A very interesting question for future work would be to analyze the dynamics and the running time of such high-dimensional EDA optimisation algorithms.

Acknowledgments The authors would like to thank Qi Xu (M.Sc. student at Birmingham) for implementing the AVS method and carrying out part of the experiments for Table 5 and Table 6.

## Appendix

## A. 1

Proof of Proposition 1. Recall from step 14 of Algorithm 1 that the set of projected points in the $i$-th subspace is:

$$
\boldsymbol{\mathcal { Y } ^ { R } _ { i } = \left\{\boldsymbol{R}_{i}\left(\boldsymbol{x}_{1}-\boldsymbol{\mu}\right), \boldsymbol{R}_{i}\left(\boldsymbol{x}_{2}-\boldsymbol{\mu}\right), \ldots, \boldsymbol{R}_{i}\left(\boldsymbol{x}_{N}-\boldsymbol{\mu}\right)\right\}}
$$

Conditionally on $\boldsymbol{R}_{i}$, the sample covariance matrix of $\mathcal{Y}^{\boldsymbol{R}_{i}}$ is:

$$
\boldsymbol{\Sigma}^{\boldsymbol{R}_{i}}=\frac{1}{N} \sum_{n=1}^{N} \boldsymbol{R}_{i}\left(\boldsymbol{x}_{n}-\boldsymbol{\mu}\right)\left(\boldsymbol{R}_{i}\left(\boldsymbol{x}_{n}-\boldsymbol{\mu}\right)\right)^{\mathrm{T}}=\boldsymbol{R}_{i} \boldsymbol{\Sigma} \boldsymbol{R}_{i}^{\mathrm{T}}
$$

Thereby the samples in step 16 are $\boldsymbol{y}_{1}^{\boldsymbol{R}_{i}}, \ldots, \boldsymbol{y}_{N}^{\boldsymbol{R}_{i}} \sim$ $\mathcal{N}\left(\mathbf{0}, \boldsymbol{\Sigma}^{\boldsymbol{R}_{i}}\right)$

To find the distribution of the individuals in $\mathcal{P}^{\text {new }}$ at step 17 , we look at the $n$-th individual:

$$
\boldsymbol{x}_{n}:=\sqrt{\frac{d M}{k}}\left[\frac{1}{M} \sum_{i=1}^{M} \boldsymbol{R}_{i}^{\mathrm{T}} \boldsymbol{y}_{n}^{\boldsymbol{R}_{i}}\right]+\boldsymbol{\mu}
$$

Conditionally on $\boldsymbol{R}_{i}, i=1: M$, this is a linear combination of independent Gaussian random variables, which is again a Gaussian ${ }^{(2)}$. Hence, $\boldsymbol{x}_{n}$ is Gaussian distributed, with mean $\boldsymbol{\mu}$ (since $\boldsymbol{y}_{n}^{\boldsymbol{R}_{i}}$ has zero mean), and we compute its covariance below.

In (7), denote $\boldsymbol{A}_{i}:=\sqrt{\frac{d M}{k}} \frac{1}{M} \boldsymbol{R}_{i}^{\mathrm{T}}$, then we have that $\boldsymbol{y}_{n}^{\boldsymbol{R}_{i}} \sim \mathcal{N}\left(\mathbf{0}, \boldsymbol{R}_{i} \boldsymbol{\Sigma} \boldsymbol{R}_{i}^{\mathrm{T}}\right)$. Therefore,

$$
\boldsymbol{A}_{i} \boldsymbol{y}_{n}^{\boldsymbol{R}_{i}} \sim \mathcal{N}\left(\mathbf{0}, \boldsymbol{A}_{i} \boldsymbol{R}_{i} \boldsymbol{\Sigma} \boldsymbol{R}_{i}^{\mathrm{T}} \boldsymbol{A}_{i}^{\mathrm{T}}\right)
$$

for all $n=1, \ldots N$. Replacing $\boldsymbol{A}_{i}$ in (A2), we have the $i$-th summand in (A1):

$$
\boldsymbol{A} \boldsymbol{y}_{n}^{\boldsymbol{R}_{i}} \sim \mathcal{N}\left(\mathbf{0}, \sqrt{\frac{d M}{k}} \frac{1}{M} \boldsymbol{R}_{i}^{\mathrm{T}} \boldsymbol{R}_{i} \boldsymbol{\Sigma} \boldsymbol{R}_{i}^{\mathrm{T}} \sqrt{\frac{d M}{k}} \frac{1}{M} \boldsymbol{R}_{i}\right)
$$

which simplifies to

$$
\mathcal{N}\left(\mathbf{0}, \frac{d}{k M} \boldsymbol{R}_{i}^{\mathrm{T}} \boldsymbol{R}_{i} \boldsymbol{\Sigma} \boldsymbol{R}_{i}^{\mathrm{T}} \boldsymbol{R}_{i}\right)
$$

Finally, the summation operation yields the ensemble covariance in the $d$-dimensional search space as stated in (1).

## A. 2

Here we give an example to demonstrate that random matrices with negative excess kurtosis can cancel the regularisation effect of the ensemble in some directions of the search space.

Let $R_{i j} \sim\{-1,+1\}$ with a probability of $1 / 2$ each. Hence we have $E\left[R_{i j}^{4}\right]=1, E\left[R_{i j}^{2}\right]=1$, and therefore the excess kurtosis is $K=1-3=-2$.

For the sake of this example, suppose that $\operatorname{rank}(\boldsymbol{\Sigma})=2$, thereby $\lambda_{1} \geqslant \lambda_{2}>0, \lambda_{3}=\ldots \lambda_{d}=0$, and suppose the first two eigenvectors of $\boldsymbol{\Sigma}$ are

$$
\begin{aligned}
& \boldsymbol{u}_{1}=(1 / \sqrt{2}, 1 / \sqrt{2}, 0, \ldots, 0) \\
& \boldsymbol{u}_{2}=(-1 / \sqrt{2}, 1 / \sqrt{2}, 0, \ldots, 0)
\end{aligned}
$$

and the remaining eigenvectors have their first two coordinates 0 . This is well defined, since one can easily verify that $\boldsymbol{u}_{1} \perp \boldsymbol{u}_{2},\left\|\boldsymbol{u}_{1}\right\|=\left\|\boldsymbol{u}_{2}\right\|=1$. Denote by $\boldsymbol{U}$ the matrix having $\boldsymbol{u}_{i}$ in its rows, with entries $U_{a i}$, where $a, i=1, \ldots, d$.

Now, we have:

$$
\begin{aligned}
& \boldsymbol{A}_{1}
\end{aligned}
$$

Then, for this example we get:

$$
\begin{aligned}
& K \sum_{i=1}^{d} \lambda_{i} \boldsymbol{A}_{i}=-2\left(\lambda_{1} \boldsymbol{A}_{1}+\lambda_{2} \boldsymbol{A}_{2}\right) \\
& =-\operatorname{Tr}(\boldsymbol{\Sigma})\left(\begin{array}{ccccc}
1 & 0 & 0 & \ldots & 0 \\
0 & 1 & 0 & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & \ldots & 0
\end{array}\right)
\end{aligned}
$$

This cancels the effect of the term $\operatorname{Tr}(\boldsymbol{\Sigma}) \boldsymbol{I}_{d}$ in the first two coordinate directions, leaving $E_{\boldsymbol{R}}\left[\boldsymbol{\Sigma}_{i \nu}\right]$ to be a multiple of maximum likelihood covariance estimates in those directions.

## A. 3

Proof of Proposition 2. Let $k \in\{2,4\}$ and $x \sim$ $t(0,1, \nu)$ a $t$-distributed random variable, then by definition,

$$
E\left[x^{k}\right]=\int_{-\infty}^{\infty} x^{k} f(x) \mathrm{d} x
$$

where $f(x)$ is the pdf of the $t$-distribution,

$$
f(x)=c\left(1+\frac{x^{2}}{\nu}\right)^{\frac{\omega k}{2}(\nu+1)}
$$

where

$$
c=\frac{1}{\sqrt{\nu} B\left(\frac{\nu}{2}, \frac{1}{2}\right)}=\frac{\Gamma(\nu / 2+1 / 2)}{\sqrt{\nu} \Gamma(\nu / 2) \Gamma(1 / 2)}
$$

and $B(\cdot, \cdot)$ is the beta function ${ }^{[32]}$. Observing that $f(x)=f(-x)$, we can re-write the integral as:

$$
E\left[x^{k}\right]=2 \int_{0}^{\infty} x^{k} f(x) \mathrm{d} x
$$

[^0]
[^0]:    (2) Assume $\boldsymbol{x} \sim \mathcal{N}\left(\boldsymbol{m}_{x}, \boldsymbol{\Sigma}_{\boldsymbol{x}}\right)$ and $\boldsymbol{y} \sim \mathcal{N}\left(\boldsymbol{m}_{\boldsymbol{y}}, \boldsymbol{\Sigma}_{\boldsymbol{y}}\right)$, then $\boldsymbol{A} \boldsymbol{x}+\boldsymbol{B} \boldsymbol{y}+\boldsymbol{c} \sim \mathcal{N}\left(\boldsymbol{A} \boldsymbol{m}_{\boldsymbol{x}}+\boldsymbol{B} \boldsymbol{m}_{\boldsymbol{y}}+\boldsymbol{c}, \boldsymbol{A} \boldsymbol{\Sigma}_{\boldsymbol{x}} \boldsymbol{A}^{\mathrm{T}}+\boldsymbol{B} \boldsymbol{\Sigma}_{\boldsymbol{y}} \boldsymbol{B}^{\mathrm{T}}\right)$.

Writing out the expression of $f$ as defined in (A3), we have that (A5) equals

$$
E\left[x^{k}\right]=2 c \int_{0}^{\infty} x^{k}\left(1+\frac{x^{2}}{\nu}\right)^{\frac{-1}{2}(\nu+1)} \mathrm{d} x
$$

Now, we make the change of variable: $t=\frac{x^{2}}{\nu}$. Hence $x=(\nu t)^{\frac{1}{2}}$, and we get:

$$
\begin{aligned}
E\left[x^{4}\right] & =c \nu^{\frac{k+1}{2}} \int_{0}^{\infty} t^{\frac{k+1}{2}-1}(1+t)^{-\frac{1}{2}-\frac{\nu}{2}} \mathrm{~d} t \\
& =c \nu^{\frac{k+1}{2}} \int_{0}^{\infty} t^{\frac{k+1}{2}-1}(1+t)^{-\left(\frac{k+1}{2}\right)-\left(\frac{\nu-k}{2}\right)} \mathrm{d} t
\end{aligned}
$$

where we added and subtracted $k / 2$ in the exponent of the last term so that the integral represents a beta function ${ }^{[32]}$ :

$$
B(m+1, n+1)=\int_{0}^{\infty} u^{m}(1+u)^{-(m+n)-2} \mathrm{~d} u
$$

with $m:=\frac{k}{2}-\frac{1}{2}$ and $n:=\frac{\nu}{2}-3$. Therefore we can write:

$$
\begin{aligned}
E\left[x^{k}\right] & =c \nu^{\frac{k+1}{2}} B\left(\frac{k+1}{2}, \frac{\nu-k}{2}\right) \\
& =c \nu^{\frac{k+1}{2}} \frac{\Gamma\left(\frac{k+1}{2}\right) \Gamma\left(\frac{\nu-k}{2}\right)}{\Gamma\left(\frac{1+n}{2}\right)}
\end{aligned}
$$

We need to evaluate this for $k=4$ and $k=2$. Replacing the expression of $c$ from (A4), we get for $k=4$ the following:

$$
E\left[x^{4}\right]=\nu^{2} \frac{\Gamma\left(\frac{5}{2}\right) \Gamma\left(\frac{\nu-4}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right) \Gamma\left(\frac{1}{2}\right)}
$$

which is finite provided that $\nu-4>0$ (since $\Gamma(0)=\infty$ ).
To simplify, we use the identities $\Gamma\left(\frac{5}{2}\right)=\frac{3}{4} \sqrt{\pi}$ and $\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}^{[32]}$. Therefore,

$$
E\left[x^{4}\right]=\frac{3 \nu^{2}}{4} \frac{\Gamma\left(\frac{\nu-4}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)}
$$

Furthermore, by a property of the Gamma function, $\Gamma(x)=(x-1) \Gamma(x-1)^{[32]}$, we have after substitution and simplification:

$$
E\left[x^{4}\right]=\frac{3 \nu^{2}}{(\nu-2)(\nu-4)}
$$

Analogously, for $k=2$, we arrive at

$$
E\left[x^{2}\right]=\frac{\nu}{\nu-2}
$$

Therefore, the excess kurtosis is:

$$
K=\frac{E\left[x^{4}\right]}{\left(E\left[x^{2}\right]\right)^{2}}-3=\frac{6}{\nu-4}
$$

Proof of Corollary 1. Let $c>0$ be a constant. Then $c \cdot x$ has variance $c^{2} \operatorname{var}(x)$. The excess kurtosis of $c \cdot x$ is

$$
\frac{E\left[(c \cdot x)^{4}\right]}{\left(E\left[(c \cdot x)^{2}\right]\right)^{2}}-3
$$

Taking the constant out, we have

$$
\frac{c^{4} E\left[x^{4}\right]}{c^{4} E\left[x^{2}\right]^{2}}-3=\frac{E\left[x^{4}\right]}{E\left[x^{2}\right]^{2}}-3
$$

thus the excess kurtosis did not change.