# A Generalized Differential Evolution Combined with EDA for Multi-objective Optimization Problems 

Wang Chen, Yan-jun Shi, and Hong-fei Teng<br>School of Mechanical Engineering, Dalian University of Technology, Dalian, P.R. China 116024<br>shiyj@dlut.edu.cn


#### Abstract

This paper proposed a multi-objective evolutionary algorithm (called by GDE-EDA hereinafter). The proposed algorithm combined a generalized differential evolution (DE) with an estimation of distribution algorithm (EDA). This combination can simultaneously use global information of population extracted by EDA and differential information by DE. Thus, GDE-EDA can obtain a better distribution of the solutions by EDA while keeping the fast convergence exhibited by DE. The experimental results of the proposed GDE-EDA algorithm were reported on a suit of widely used test functions, and compared with GDE and NSGA-II in the literature.


Keywords: Generalized differential evolution; estimation of distribution algorithm; multi-objective optimization.

## 1 Introduction

Many real-world problems in the engineering are multi-objective in nature, e.g., layout optimization of satellite module, mechanical component design, etc. Over the past decades, a large amount of studies had been focused on multi-objective optimization problems (MOOPs) and had obtained a lot of achievement. However, the complexity of some multi-objective optimization problems (e.g., very large search spaces, uncertainty, noises, disjoint Pareto curves, etc.) call for new or alternative approaches.

Differential Evolution (DE) is a stochastic, population-based evolutionary algorithm for global optimization proposed by Kenneth Price and Rainer Storn[1]. DE is capable of converging to the optimal by adopt the distance and direction information from the current population of solutions. Therefore, there have been a lot of the proposed extensions of DE for multi-objective optimization. Chang et al[2] gave the first reported attempt to extend differential evolution for multi-objective problems. Bergey[3] also reported a multi-objective evolutionary algorithm based on differential evolution (called by Pareto Differential Evolution, or PDE) at about the same time as Chang et al. Ref [4] introduced a new version of PDE (called by Self-Adaptive Pareto Differential Evolution, or SPDE).

Besides, there have been many literatures on multi-objective optimization problems with constraints. Iorio and $\mathrm{Li}[5]$ firstly proposed the Non-dominated Sorting Differential Evolution (NSDE) with a simple modification of the NSGA-II[6]. Then

they [7] proposed a variation of NSDE. Santana-Quintero and Coello Coello[8] proposed the $\epsilon$-MyDE. Additionally, Ref [9] provided a new generalized differential evolution (GDE) algorithm. To sum up, DE is a very powerful to act as search engine of multi-objective optimization. However, some issues still was raised for multiobjective version of DE. For example, multi-objective DE seemed to have a high convergence rate, but has difficulties to reach the true Pareto front (see for example [8]). The main reason is that DE has no mechanism to extract global information to guide the search for exploring promising areas and to maintain diversity.

To overcome the aforementioned shortcomings, we herein combined Estimation of distribution algorithms (EDA) [10] to spread solutions along the front. EDAs maintained and successively improved a population of candidate solutions and a probability model for promising solutions until some stopping condition was met. Sun et al. [11] had combined DE with EDA to solve some test problems. Zhou et al.[12] proposed a M-MOEA and MOEA can be regarded as a combination of EDA and NSGAII. The preliminary experimental results show that M-MOEA performs better than NSGA-II. Peter et al.[13] proposed a new algorithm(MIDEA) for evolutionary multiobjective optimization by learning and using probabilistic mixture distributions.

In this study, we combine the DE with EDAs for MOOPs, that is, Generalized Differential Evolution with Estimation Distribution Algorithm (called by GDE-EDA hereinafter). The following sections provide the details of GDE-EDA.

# 2 The Proposed GDE-EDA Algorithm 

Mathematically, constrained multi-objective optimization problem (MOOP) can be presented in the following form without loss of generality:

$$
\begin{aligned}
\min & F(\vec{X})=\left(f_{1}(\vec{X}), f_{2}(\vec{X}), \ldots, f_{k}(\vec{X})\right)^{T} \\
\text { s.t. } & H(\vec{X})=\left(h_{1}(\vec{X}), h_{2}(\vec{X}), \ldots, h_{p}(\vec{X})\right)^{T}=0 \\
& G(\vec{X})=\left(g_{1}(\vec{X}), g_{2}(\vec{X}), \ldots, g_{m}(\vec{X})\right)^{T} \leq 0
\end{aligned}
$$

where $k$ is the number of objectives to be optimized, $p$ and $m$ is the number of equality constraints and inequality constraint functions respectively. In Eq.1, $\vec{X}=\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ is decision vector and $F(\vec{x})$ is vector of objective functions. Unlike single-objective problem, there exists a set of Pareto-optimal solutions for $F(\vec{x})$. To provide an alternative solution, we proposed a new algorithm (GDE-EDA) detailed as follows.

### 2.1 Generalized Differential Evolution

The multi-objective version of DE algorithm used in this study was referenced as Generalized Differential Evolution (GDE)[9]. GDE was an extension of Differential Evolution (DE) for global optimization with an arbitrary number of objectives and constraints. Like DE, GDE also has the mutation, crossover and selection operations. The mutation and crossover operators of GDE are in the same manner as basic DE,

while GDE extends the selection operation of DE for constrained MOOP. In each generation, GDE uses the crossover and mutation operation of DE to generate offspring, and then uses the extension of select operation of DE to form a new population (the next generation).

However, GDE only made improvement on the selection scheme rather than improve the algorithm on the generate scheme of offspring which is the most important operation in EAs. Therefore, we improved this GDE using Estimation of Distribution Algorithm.

# 2.2 Estimation of Distribution Algorithm 

EDA explicitly extract global statistical information from the selected solutions (often called parents) and build a posterior probability distribution model of promising solutions, based on the extracted information. New solutions are sampled from the model thus built and fully or in part replace the old population. To employ EDA, we have to deal with two important issues: (1) how to select the parent solution. We employ the 2 -tournament selection for it is a typical selection method used in many applications; (2) how to build a probability distribution model $p(x)$. Since it is impractical to calculate the actual posterior distribution of the promising solutions, most of the existing EDA-like algorithms model the distribution functions by probabilistic graph models or Bayesian networks. We employ Gaussian model with diagonal covariance matrix (GM/DCM) ${ }^{[14]}$ here because it considers the correlation between random variables, where the joint density function of the $G$-th generation is written as

$$
p_{G}(x)=\prod_{i=1}^{n} N\left(x_{i} ; \mu_{i}^{G}, \sigma_{i}^{G}\right)
$$

where

$$
N\left(x_{i} ; \mu_{i}^{G}, \sigma_{i}^{G}\right)=\frac{1}{\sqrt{2 \pi \sigma_{i}}} \exp \left(-\frac{1}{2}\left(\frac{x_{i}-\mu_{i}}{\sigma_{i}}\right)^{2}\right)
$$

In Formula (2), the $n$-dimensional joint probability distribution is factorized as a product of $n$ univariate and independent normal distributions. There are two parameters for each variable required to be estimated in the $G$-th generation: the mean $\mu_{i}^{G}$, and the standard deviation $\sigma_{i}^{G}$. They can be estimated as

$$
\begin{gathered}
\hat{\mu}_{i}^{G}=\bar{x}_{i}^{G}=\frac{1}{M} \sum_{j=1}^{M} x_{j i}^{G} \\
\hat{\sigma}_{i}^{G}=\sqrt{\frac{1}{M} \sum_{j=1}^{M}\left(x_{j i}^{G}-\bar{x}_{i}^{G}\right)^{2}}
\end{gathered}
$$

where $\left(x_{1, i}^{G}, x_{2, i}^{G}, \ldots, x_{M, i}^{G}\right)$ are values of the $i$-th variable of the selected $M$ parent solutions in the $G$-th generation.

# 2.3 The GDE-EDA Algorithm 

Borrowing from the aforementioned GDE and EDA, we proposed a new multiobjective algorithm, namely GDE-EDA. As mentioned above, GDE used the distance and direction information from the current population to guide its further search, but had no mechanism to extract global information for exploring promising areas and to maintain diversity in solving MOOPs. EDA explicitly extract global statistical information from the selected solutions and can avoid trapping in local optimum. Therefore, we combine GDE with EDAs, attempting to obtain a better algorithm. Figure 1 illuminates the pseudo code of GDE-EDA, where parameter $\delta(C R<\delta \leq 1)$ is used to balance contributions of the global information and the differential information. $G$, $G_{\text {MAX }}$ denote the current generation and max generation of evolution process respectively. $r 1, r 2, r 3$ is random integer.

```
initialize \(G=0, m=0\)
while \(G<G_{\text {MAX }}\)
    select \(M\) solutions from \(S_{G}=\left\{\ddot{x}_{1, G}, \ddot{x}_{2, G}, \ldots, \ddot{x}_{N, G}\right\}\), construct \(p_{G}(x)=\prod_{i} N\left(x_{i} ; \mu_{i}^{G}, \sigma_{i}^{G}\right)\)
    for each: \(\ddot{x}_{i, G}, i=1,2, \ldots, N\)
        for each: \(x_{j, G}, j=1,2, \ldots, D\)
            if \(\operatorname{randb}(j)<C R\) or \(j=\operatorname{randr}(i)\)
                \(u_{j, G}=x_{j+1, G}+F\left(x_{j+2, G}-x_{j+3, G}\right)\)
            else if \(C R \leq \operatorname{randb}(j)<\delta\)
                \(u_{j, G}\) is sampled according to \(N\left(x_{i} ; \mu_{i}^{G}, \sigma_{i}^{G}\right)\)
            else
                \(u_{j, G}=x_{j, G}\)
            end
        end
        selection
            \(\ddot{x}_{i, G+1}=\left\{\begin{array}{l}\ddot{u}_{1, G} \text {; if } \ddot{u}_{1, G} \leq \ddot{x}_{i, G} \\ \ddot{x}_{1, G} \text { otherwise }\end{array}\right.\)
            if \(\left(\forall j: g_{j}\left(\ddot{x}_{i, G}^{\prime}\right) \leq 0\right.\) or \(\left(\ddot{x}_{i, G+1}==\ddot{x}_{1, G}\right.\) or \(\left(\ddot{x}_{1, G} \neq \ddot{x}_{1, G}^{\prime}\right.\) )
                \(m=m+1\)
                \(\ddot{x}_{N+m, G+1}=\ddot{x}_{1, G}^{\prime}\)
            end
    end
    while \(m>0\)
        for each: \(\bar{x} \in S_{G+1}=\left\{\ddot{x}_{1, G+1}, \ddot{x}_{2, G+1}, \ldots, \ddot{x}_{N+m, G+1}\right\}\)
            if \((\forall i \quad \bar{x} \neq \ddot{x}_{i, G+1} \text { or }\left(\forall\left(\ddot{x}_{1, G+1}: \ddot{x}_{i, G+1} \neq \ldots \bar{x}\right) \quad C D(\bar{x}) \leq C D\left(\ddot{x}_{i, G+1}\right)\right.\)
                remove \(\bar{x}\) from \(S_{G+1}\)
                \(m=m-1\)
            end
        end
    end
    \(G=G+1\)
end
```

Fig. 1. The pseudo code of GDE-EDA

## 3 Experiments

We employed a set of widely used test functions available from the literature $[6,15,16]$ to evaluate our proposed approach. The main objective of experiments was

attempted to better understand the strengths and weaknesses of GDE-EDA for different types of test problems.

We used the following metrics to measure the performance[6]: (1) convergence metric $\gamma$, which measure the convergence property of a algorithm by using distance to $P F_{\text {true }}$ which is determined by approximating as a combination of piecewise linear segments with the average of these distances defining the metric value. (2) diversity metric $\Delta$ [6], which measures distributed extent of a obtained Pareto-optimal solutions over a non-dominated region. The smaller the value $\Delta$, the better the spread extent, and $\Delta=0$ stand for ideal solution set. The diversity metric was formulated as

$$
\Delta=\frac{d_{f}+d_{i}+\sum_{i=1}^{N-1}\left|d_{i}-\bar{d}\right|}{d_{f}+d_{i}+(N-1) \bar{d}}
$$

where the parameter $d_{f}$ and $d_{i}$ are the Euclidean distance between the extreme solutions and the boundary solutions of the obtained non-dominated set. The parameter $\bar{d}$ is the average of all distances $d_{i}, i=1,2, \ldots, N-1$, assuming that there are $N$ Paretooptimal solutions.

The experimental results are compared with that of the state-of-the-art in the area, NSGA-II and GDE.

The size of the population of NSGA-II, GDE and GDE-EDA was 100 and all approaches are run for a maximum of 25000 function evaluations. We use the simulated binary crossover (SBX) operator and polynomial mutation for NSGA-II. Suitable control parameter values of three algorithms for each problem were found by trying out a list of different control parameter values.

# 3.1 Bi-objective Test Problems 

Firstly, GDE-EDA was used to solve the widely used bi-objective optimization problem[6]. All these problems have two objective functions and none of these problems have any constraint. Control parameters for three algorithms are shown in Table 1.

Table 1. Control parameters for the three algorithms
### 3.2 Constrained Bi-objective Test Problems

Then, some constrained bi-objective problems were used to test the constrainthandling ability of GDE-EDA. All these problems ${ }^{[15]}$ have two objective functions and two constraint functions. Control parameters for three algorithms are shown in Table 2.

Table 2. Control parameters for the three algorithms

# 3.3 Tri-objective Test Problems 

GDE-EDA was also used to solve the widely used tri-objective test problems, i.e., DTLZ1, DTLZ4 and DTLZ7[16], and compared with GDE3 and NSGA-II. All these problems have three objectives and none of these problems have any constraint. Control parameters for three algorithms are shown in Table 3.

Table 3. Control parameters for the three algorithms

### 3.4 Results and Discussion

We made experiments on the aforementioned test functions, including bi-objective with constrain or not, tri-Objective test Problems. The experimental results of GDEEDA were compared with that of GDE3 and that of EDA, and shown on Table 4 and Table 5 using two metrics measure the performance for comparative study. Table 4 showed the mean and variance of the convergence metric $\tau$ obtained from NSGA-II, GDE and GDE-EDA. We can see that on most of problems, GDE-EDA is able to find better convergence solutions than other two algorithms on metric $\tau$. These results indicated that GDE-EDA kept the fast convergence exhibited by DE. Table 5 showed the mean and variance of the diversity metric $\Delta$ obtained from all three approaches. Considering the results from the metric $\Delta$, we can believe that GDE-EDA was able to find better distribution solutions than other two algorithms except in ZDT3 problem.

Table 4. Statistic results of the convergence metric $\tau$
Table 5. Statistic results of the diversity metric $\Delta$
Therefore, it seemed that GDE-EDA outperformed GDE3 and EDA for most of experiments on two metrics measure from the results obtained so far. The reason may be that GDE-EDA combined the advantages of GDE and EDA, which can extract the global information of population for exploration and use the differential information by DE for exploitation, and control two parameters to balance the trade-off between exploration and exploitation.

# 4 Conclusion and Future Research 

In this study we proposed a multi-objective evolutionary algorithm (GDE-EDA) to tackle both unconstrained and constrained multi-objective problems. The proposed GDE-EDA algorithm employed EDA to extract the global information of search for producing better distribution solutions, and employed DE to obtain the fast convergence. The experimental results indicated that GDE-EDA can generate Pareto-optimal solution set with better convergence and better distribution than EDA and GDE3. Further studies on employing different variations of EDA and DE for better performance will be summarized in our next work.

## Acknowledgements

This work was supported by National High-tech R\&D program of P R China (Grant No. 2006AA04ZI09), National Natural Science Foundation of P R China (Grant Nos. 50575031) and National Defense Basic Scientific Research Project of P R China (Grant No. B0920060901).
