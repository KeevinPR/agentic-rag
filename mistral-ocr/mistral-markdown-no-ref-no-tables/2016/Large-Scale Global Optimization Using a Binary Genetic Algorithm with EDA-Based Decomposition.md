# Large-Scale Global Optimization Using a Binary Genetic Algorithm with EDA-Based Decomposition 

Evgenii Sopov ${ }^{(\square)}$<br>Department of Systems Analysis and Operations Research, Siberian State Aerospace University, Krasnoyarsk, Russia<br>evgenysopov@gmail.com


#### Abstract

In recent years many real-world optimization problems have had to deal with growing dimensionality. Optimization problems with many hundreds or thousands of variables are called large-scale global optimization (LGSO) problems. The most advanced algorithms for LSGO are proposed for continuous problems and are based on cooperative coevolution schemes using the problem decomposition. In this paper a novel technique is proposed. A genetic algorithm is used as the core technique. The estimation of distribution algorithm is used for collecting statistical data based on the past search experience to provide the problem decomposition by fixing genes in chromosomes. Such an EDA-based decomposition technique has the benefits of the random grouping methods and the dynamic learning methods. The results of numerical experiments for benchmark problems from the CEC'13 competition are presented. The experiments show that the approach demonstrates efficiency comparable to other advanced algorithms.


Keywords: Estimation of distribution algorithm $\cdot$ Genetic algorithm $\cdot$ Large-scale global optimization $\cdot$ Problem decomposition

## 1 Introduction

Evolutionary algorithms (EAs) have proved their efficiency at solving many complex real-world optimization problems. However, their performance usually decreases when the dimensionality of the search space increases. This effect is called the "curse of dimensionality". Optimization problems with many hundreds or thousands of objective variables are called large-scale global optimization (LGSO) problems.

There exist some classes of optimization problems that are not hard for either classical mathematical approaches or more advanced search techniques (for example, linear programming). At the same time, black-box LSGO problems have become a great challenge even for EAs as we have no information about the search space to include it into a certain algorithm. Nevertheless, some assumption can be done, and there exist many efficient LSGO techniques for the continuous search space [6].

Many real-world optimization problems encode different complex structures and contain variables of many different types, which cannot be represented only by real values. In this case binary genetic algorithms (GAs) can be used. As we can see from papers, there is a lack of LSGO approaches using the GA as the core technique.

In this paper a novel LSGO technique using a GA with a decomposition based on the estimation of distribution algorithm (EDA) is proposed. The binary EDA is used to present a statistic of the past search experience of the GA and to predict the values of problem subcomponents that are being fixed to decrease the problem dimensionality.

The rest of the paper is organized as follows. Section 2 describes related work. Section 3 describes the proposed approach. In Sect. 4 the results of numerical experiments are discussed. In the Conclusion the results and further research are discussed.

# 2 Related Work 

There exist a great variety of different LSGO techniques that can be combined in two main groups: non-decomposition methods and cooperative coevolution (CC) algorithms. The first group of methods are mostly based on improving standard evolutionary and genetic operations. But the best results and the majority of approaches are presented by the second group. The CC methods decompose LSGO problems into low dimensional sub-problems by grouping the problem subcomponents. CC consists of three general steps: problem decomposition, subcomponent optimization and subcomponent coadaptation (merging solutions of all subcomponents to construct the complete solution). The problem decomposition is a critical step. There are many subcomponent grouping methods, including: static grouping [8], random dynamic grouping [13] and learning dynamic grouping [5, 7]. A good survey on LSGO and methods is proposed in [6]. As we can observe in papers, almost all studies are focused on continuous LSGO, and there is a lack of techniques for binary (or other discrete) representations.

The EDA is a stochastic optimization technique that explores a space of potential solutions by building and sampling explicit probabilistic models. The estimated distribution can be used for improving standard search techniques. There exist some hybrid EDA-EA approaches for LSGO [1, 11]. These hybrid EDA-EA techniques are also designed for continuous LSGO.

The most widely known competition on LSGO has been held within the IEEE Congress on Evolutionary Computation (CEC) since 2008. As we can see from the last competition, the majority of proposed methods are based on the random dynamic grouping and continuous search techniques.

## 3 Proposed Approach

### 3.1 EDA-Based Decomposition

The main idea of the LSGO problem decomposition methods is based on the divide-and-conquer approach which decomposes the problem into single-variable or multiple-variable low dimensional problems. In this case, only part of the variables are used in the search process; the rest are fixed and their values are defined using some strategy (for example, values from the best-found solution are used).

The finding of an appropriate decomposition is part of the general search process. It is obvious and has been presented in many studies that the best performance is achieved with separable LSGO problems. In the case of non-separable problems, the performance strongly depends on the decomposition strategy.

In this work, we will formulate the following requirements for the proposed decomposition method. The grouping should be dynamic to realize the "exploration and exploitation" strategy. The grouping should be random to avoid the greedy search and the local convergence. The grouping should be based on the past search experience of the whole population (to provide the global search options). The grouping should be adaptively scalable to provide efficient decomposition at every stage of the search process.

As is known, GAs do not collect a statistic of the past generations in an explicit form, but it is contained in the genes of individuals in the population. One of the ways to present the statistic is to evaluate the distribution of binary values as in the binary EDA. The following probability vector can be used (1):

$$
P(t)=\left(p_{1}(t), p_{2}(t), \ldots, p_{n}(t)\right), p_{i}(t)=P\left(x_{i}=1\right)=\frac{1}{N} \sum_{j=1}^{N} x_{i}^{j}, i=\overline{1, n}
$$

where $t$ is the number of the current generation, $p_{i}$ is the probability of a one-value for the $i$-th position in chromosomes of individuals in the last population, $x_{i}^{j}$ is the value of the $i$-th gene of the $j$-th individual, $n$ is the chromosome length, and $N$ is the size of the population.

The distribution calculated at the $t$-th generation describes the generalized statistic collected by the GA in the population. We can also analyse the dynamic of the statistic over a series of generations. In [9] a convergence property of the probability vector components is discussed. Experiments have shown that for a GA that converges to the global optima, the probability vector values converge to one if the corresponding position of the optimal solution contains a one, and converge to zero otherwise.

We will use this convergence property to define the values for fixed genes at the grouping stage. If the $i$-th position in a chromosome at the $t$-th generation is fixed, its value is defined by the corresponding value of the probability vector (2):

$$
x_{i}^{j}(t)=\left\{\begin{array}{c}
0, \text { if } p_{i}(t)<(0.5-\delta) \\
\text { random, if }(0.5-\delta) \leq p_{i}(t) \leq(0.5+\delta) \\
1, \text { if } p_{i}(t)>(0.5+\delta)
\end{array}\right.
$$

where $\delta$ is a threshold (a confidence level), $\delta \in(0,0.5)$.
We will explain the proposed approach using Fig. 1. The diagram visualizes an arbitrary component of the probability vector for an arbitrary run of a GA on the Rastrigin function. For the chosen gene the corresponding value of the optimal solution is equal to zero. As we can see from Fig. 1, the GA starts with random initialization, thus the value of the probability vector is equal to 0.5 . At the first generations the GA actively explores the search space and number of 1's and 0's genes are almost equal, thus the value of the probability vector is still about 0.5 . After that, the GA locates a

![img-0.jpeg](img-0.jpeg)

Fig. 1. The dynamic of the probability vector component
promising region in the search space and increases the number of 0 's in this position, thus the value of the probability vector decreases towards zero.

The confidence level $\delta$ is a parameter that defines a threshold for the probability value around 0.5 , when we cannot make a decision about the gene value.

Although a decision about fixed variables is made by stand-alone components, the estimated distribution contains information about the problem solving in general. Thus the method is not focused only on separable LSGO problems.

Next we need to define the number of variables that will be fixed. There exist many strategies. For example, the splitting-in-half method divides an $n$-dimensional problem into two $n / 2$ subcomponents. In general, we will define the number of fixed variables as a percentage of the chromosome length and will denote it as $\alpha$. The value of $\alpha$ can be constant or can change during the run of the algorithm. The variables and corresponding components of the probability vector are fixed for some predefined number of generations, which is called an adaptation period (denoted as $t_{\text {adapt }}$ ). The list of fixed components is randomly defined.

In this paper, the straight-forward approach is used, $\alpha$ and $t_{\text {adapt }}$ are predefined and constant.

The main advantage of such EDA-based decomposition is that we do not lose the previously collected statistic as we fix components of the probability vector. The GA solves the problem of reduced dimensionality and updates the probability only for active components. After each adaptation period we will randomly fix other components, and the previously fixed components will continue updating their saved values.

# 3.2 The GA with EDA-Based Decomposition for LSGO 

We will describe the proposed LSGO algorithm in detail.
First, we need to encode the initial problem into a binary representation. The standard binary or Grey code can be used. A chromosome length $n$ is defined. Next, specific parameters of the EDA-based decomposition and the chosen GA, maximum

number of fitness evaluations (MaxFE) or maximum number of generations (MaxGEN) are defined.

Finally, the following algorithm is used:
Input: $n, N, \alpha, \delta, t_{\text {adapt }}$, MaxFE, the GA operators' parameters.
Initialization. Randomly generate a population of $N$ individuals of the length $n$. Calculate $P(0)$ using formula (1).

Main loop. Until MaxFE is reached:

1. Problem decomposition stage. Start new adaptation period. Fix random $\alpha$ components in chromosomes and in the probability vector.
2. Subcomponent optimization stage. Run the GA for $t_{\text {adapt }}$ generations:
(a) Fitness evaluation. Set values in fixed positions of chromosomes according to $P(t)$ using formula (2).
(b) Perform selection, crossover and mutation operations.
(c) Create next generation, update the probability vector $P(t)$ for active components.

Output: the best-found solution.

# 3.3 Parallel (The Island Model) Modification 

Many proposed LSGO approaches with the subcomponent grouping are based on cooperative coevolution. In this case, many populations are used, which evolve different groups of subcomponents. The cooperation is used on the fitness evaluation step to define the values of components that were fixed during the algorithm run. Usually, components of the best individuals from other populations are used.

We will introduce many parallel populations using the following scheme. At the main loop, the total population of size $N$ is divided into $K$ populations of size $M$, where $N=K \cdot M$. For each population the problem decomposition and the subcomponent optimization steps are independently performed. Thus each population can be viewed as an island with its own decomposition strategy. When the adaptation period is over, all individuals from all populations are collected back into the total population and the summary statistic is updated. This step can be viewed as the cooperation.

As is known, the island model GA can outperform the standard single-population GA for many complex optimization problems. We can also decrease the computational efforts by implementing the GA with a parallel multi-core or multi-processor computer.

## 4 Experimental Results

To estimate the proposed approach performance, we have used 15 large-scale benchmark problems from the CEC'2013 Special Session and Competition on Large-Scale Global Optimization [3]. These problems represent a wider range of real-world large-scale optimization problems and provide convenience and flexibility for comparing various evolutionary algorithms specifically designed for large-scale global

optimization. There are 3 fully-separable problems (denoted as $f 1-f 3$ ), 8 partially separable problems ( $f 4-f 7$ with a separable subcomponent and $f 8-f 11$ with no separable subcomponents), 3 problems with overlapping subcomponents ( $f 12-f 14$ ), and 1 non-separable problem ( $f 15$ ).

The experiment settings are:

- Dimensions for all problem are $D=1000$.
- The standard binary encoding is used with accuracies: $\varepsilon=0.1$ for $f 1, f 4, f 7, f 8$ and $f 11-15, \varepsilon=0.05$ for $f 3, f 6$ and $f 10$, and $\varepsilon=0.01$ for $f 2, f 5$ and $f 9$.
- For each problem the best, mean, and standard deviation of the 25 independent runs are evaluated.
- Maximum number of fitness evaluations is $\operatorname{MaxFE}=3.0 \mathrm{e}+6$.
- The performance estimation is performed when the number of fitness evaluations is $1.2 \mathrm{e}+5,6.0 \mathrm{e}+5$ and $3.0 \mathrm{e}+6$.

The EDA-based decomposition GA settings are:

- Population sizes are $N=1000$ for the single-population version, $N=500$ for the island version with 3 islands, and $N=400$ for 5 islands.
- The adaptation period is $t_{\text {adapt }}=100$.
- The probability threshold is $\delta=0.15$.
- Numbers of fixed components are $\alpha=25 \%, 50 \%$ and $75 \%$ of the chromosome length.

All algorithms have been implemented in Visual Studio C++ using the OpenMP for parallel computing with multi-core PC. Free C++ source codes of the benchmark problems are taken from [10].

We have carried out the above-mentioned experiments and have established the following. In the case of single population, the best performance is achieved with $50 \%$ fixed components. In the case of the island model, the best results are obtained by the 5 island model with $75 \%$ fixed components. Almost for every considered value of $\alpha$, the island model outperforms the single population version of the algorithm. The experimental results for the best found settings are presented in Table 1.

The summary results are compared with other techniques presented at the CEC'13 competition. The algorithms are DECC-G (differential evolution (DE) based cooperative coevolution (CC) with random dynamic grouping) [13], VMO-DE (variable mesh optimization using differential evolution) [4], CC-CMA-ES (Covariance Matrix Adaptation Evolution Strategy using Cooperative Coevolution) [5], MOS (Multiple Offspring Sampling (MOS) based hybrid algorithm) [2], and SACC (smoothing and auxiliary function based cooperative coevolution) [12]. We have averaged the performance estimates of all algorithms over all problems and have ranked algorithms by the Best and the Mean values. The results are in Table 2.

As we can see from Table 2, the proposed approach has taken 4th place by the Best criterion and 5th place by the Mean value. We should note that all algorithms except the proposed are specially designed for continuous LSGO problems. The EDA-based decomposition GA does not use any knowledge about search space. Moreover, the chromosome length in the binary algorithm is greater than in the case of the continuous

Table 1. Experimental results for the EDA-based decomposition GA with 5 islands and $\alpha=75 \%$

Table 2. LSGO approaches comparison

space. Nevertheless, the EDA-based decomposition GA outperforms the CC-CMA-ES by two measures and the DECC-G by the Best value on average.

Our hypothesis is that the proposed approach will be a good tool for solving complex real-world LSGO problems, which usually contain not only continuous variables, but can represent arbitrary complex structures. Further investigations of the algorithm structure and parameters can probably improve its performance. In particular, the $\alpha$ value can be adjusted adaptively during the algorithm run using information about the probability vector convergence.

# 5 Conclusions 

In this paper a novel technique for LSGO that uses a binary GA with EDA-based decomposition is proposed. The EDA is used for collecting statistical data based on the past search experience to predict the convergence of subcomponents and to decrease the problem dimensionality by fixing some genes in chromosomes. We have compared a single population and the island model implementations of the algorithm. The best

results have been obtained with the island model version. It yields state-of-the-art LSGO techniques, but the performance is comparable. The advantage of the proposed approach is that it can be applied to problems with arbitrary representations and it needs no a priori information about the search space.

In further work, more detailed analysis of the EDA-based decomposition GA parameters will be provided. A self-configuration will be introduced into the algorithm.

Acknowledgements. The research was supported by the President of the Russian Federation grant (MK-3285.2015.9).
