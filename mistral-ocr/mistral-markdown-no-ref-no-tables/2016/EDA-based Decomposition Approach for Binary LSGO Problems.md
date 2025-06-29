# EDA-based Decomposition Approach for Binary LSGO Problems 

Evgenii Sopov<br>Department of Systems Analysis and Operations Research, Siberian State Aerospace University, Krasnoyarsk, Russia

Keywords: Large-Scale Global Optimization, Problem Decomposition, Estimation of Distribution Algorithm, Binary Genetic Algorithm.


#### Abstract

In recent years many real-world optimization problems have had to deal with growing dimensionality. Optimization problems with many hundreds or thousands of variables are called large-scale global optimization (LSGO) problems. Many well-known real-world LSGO problems are not separable and are complex for detailed analysis, thus they are viewed as the black-box optimization problems. The most advanced algorithms for LSGO are based on cooperative coevolution schemes using the problem decomposition. These algorithms are mainly proposed for the real-valued search space and cannot be applied for problems with discrete or mixed variables. In this paper a novel technique is proposed, that uses a binary genetic algorithm as the core technique. The estimation of distribution algorithm (EDA) is used for collecting statistical data based on the past search experience to provide the problem decomposition by fixing genes in chromosomes. Such an EDA-based decomposition technique has the benefits of the random grouping methods and the dynamic learning methods. The EDA-based decomposition, GA using the island model is also discussed. The results of numerical experiments for benchmark problems from the CEC competition are presented and discussed. The experiments show that the approach demonstrates efficiency comparable to other advanced techniques.


## 1 INTRODUCTION

Evolutionary algorithms (EAs) have proved their efficiency at solving many complex real-world optimization problems. However, their performance usually decreases when the dimensionality of the search space increases. This effect is called the "curse of dimensionality". Optimization problems with many hundreds or thousands of objective variables are called large-scale global optimization (LSGO) problems.

There exist some classes of optimization problems that are not hard for either classical mathematical approaches or more advanced search techniques (for example, linear programming). At the same time, real-world optimization problems are usually complex and not well-studied, so they are viewed as black-box optimization problems even the objective has analytical representation (mathematical formula). Black-box LSGO problems have become a great challenge even for EAs as we have no information about the search space to include it into a certain algorithm. Another challenge is nonseparability that excludes a straightforward
variable-based decomposition. Nevertheless, some assumption can be done, and there exist many efficient LSGO techniques for the continuous search space (Mahdavi et al., 2015).

Many real-world optimization problems encode different complex structures and contain variables of many different types, which cannot be represented only by real values. In this case binary genetic algorithms (GAs) can be used. As we can see from papers, there is a lack of LSGO approaches using the GA as the core technique.

In this paper a novel LSGO technique using a GA with a decomposition based on the estimation of distribution algorithm (EDA) is proposed. The binary EDA is used to present a statistic of the past search experience of the GA and to predict the values of problem subcomponents that are being fixed to decrease the problem dimensionality.

The rest of the paper is organized as follows. Section 2 describes related work. Section 3 describes the proposed approach. In Section 4 the results of numerical experiments are discussed. In the Conclusion the results and further research are discussed.

## 2 RELATED WORK

There exist a great variety of different LSGO techniques that can be combined in two main groups: non-decomposition methods and cooperative coevolution (CC) algorithms. The first group of methods are mostly based on improving standard evolutionary and genetic operations. But the best results and the majority of approaches are presented by the second group. The CC methods decompose LSGO problems into low dimensional sub-problems by grouping the problem subcomponents. CC consists of three general steps: problem decomposition, subcomponent optimization and subcomponent coadaptation (merging solutions of all subcomponents to construct the complete solution). The problem decomposition is a critical step. There are many subcomponent grouping methods, including: static grouping (Potter and De Jong, 2000), random dynamic grouping (Yang et al., 2008) and learning dynamic grouping (Liu and Tang, 2013; Omidvar et al., 2014). A good survey on LSGO and methods is proposed in (Mahdavi et al., 2015). As we can observe in papers, almost all studies are focused on continuous LSGO, and there is a lack of techniques for binary (or other discrete) representations.

The EDA is a stochastic optimization technique that explores a space of potential solutions by building and sampling explicit probabilistic models. The estimated distribution can be used for improving standard search techniques. There exist some hybrid EDA-EA approaches for LSGO (Dong et al., 2013; Wang and Li, 2008). These hybrid EDA-EA techniques are also designed for continuous LSGO.

The most widely known competition on LSGO has been held within the IEEE Congress on Evolutionary Computation (CEC) since 2008. As we can see from the last competition, the majority of proposed methods are based on the random dynamic grouping and continuous search techniques.

## 3 PROPOSED APPROACH

### 3.1 EDA-based Decomposition

The main idea of the LSGO problem decomposition methods is based on the divide-and-conquer approach which decomposes the problem into single-variable or multiple-variable low dimensional problems. In this case, only part of the variables are used in the search process; the rest are fixed and their values are
defined using some strategy (for example, values from the best-found solution are used).

The finding of an appropriate decomposition is part of the general search process. It is obvious and has been presented in many studies that the best performance is achieved with separable LSGO problems. In the case of non-separable problems, the performance strongly depends on the decomposition strategy.

In this work, we will formulate the following requirements for the proposed decomposition method:

- The grouping should be dynamic to realize the "exploration and exploitation" strategy.
- The grouping should be random to avoid the greedy search and the local convergence.
- The grouping should be based on the past search experience of the whole population (to provide the global search options).
- The grouping should be adaptively scalable to provide efficient decomposition at every stage of the search process.
As is known, GAs do not collect a statistic of the past generations in an explicit form, but it is contained in the genes of individuals in the population. One of the ways to present the statistic is to evaluate the distribution of binary values as in the binary EDA. The following probability vector can be used (1):

$$
\begin{gathered}
P(t)=\left(p_{1}(t), p_{2}(t), \ldots, p_{n}(t)\right) \\
p_{i}(t)=P\left(x_{i}=1\right)=\frac{1}{N} \sum_{j=1}^{N} x_{i}^{j}, i=\overline{1, n}
\end{gathered}
$$

where $t$ is the number of the current generation, $p_{i}$ is the probability of a one-value for the $i$-th position in chromosomes of individuals in the last population, $x_{i}^{j}$ is the value of the $i$-th gene of the $j$-th individual, $n$ is the chromosome length, and $N$ is the size of the population.

The distribution calculated at the $t$-th generation describes the generalized statistic collected by the GA in the population. We can also analyse the dynamic of the statistic over a series of generations. In (Sopov and Sopov, 2011) a convergence property of the probability vector components is discussed. Experiments have shown that for a GA that converges to the global optima, the probability vector values converge to one if the corresponding position of the optimal solution contains a one, and converge to zero otherwise.

We will use this convergence property to define the values for fixed genes at the grouping stage. If the $i$-th position in a chromosome at the $t$-th generation is

![img-0.jpeg](img-0.jpeg)

Figure 1: The dynamic of the probability vector component (the vertical axis is the value of the probability vector component, the horizontal axis is generation number).
fixed, its value is defined by the corresponding value of the probability vector (2):

$$
x_{i}^{j}(t)==\left\{\begin{array}{cc}
0, & \text { if } p_{i}(t)<(0.5-\delta) \\
r n d, & \text { if } p_{i}(t) \epsilon(0.5-\delta, 0.5+\delta) \\
1, & \text { if } p_{i}(t)>(0.5+\delta)
\end{array}\right.
$$

where $\delta$ is a threshold (a confidence level), $\delta \in$ $(0,0.5)$.

We will explain the proposed approach using Figure 1. The diagram visualizes an arbitrary component of the probability vector for an arbitrary run of a GA on the Rastrigin function. For the chosen gene the corresponding value of the optimal solution is equal to zero. As we can see from Figure 1, the GA starts with random initialization, thus the value of the probability vector is equal to 0.5 . At the first generations the GA actively explores the search space and number of 1's and 0's genes are almost equal, thus the value of the probability vector is still about 0.5 . After that, the GA locates a promising region in the search space and increases the number of 0 's in this position, thus the value of the probability vector decreases towards zero.

The confidence level $\delta$ is a parameter that defines a threshold for the probability value around 0.5 , when we cannot make a decision about the gene value.

Although a decision about fixed variables is made by stand-alone components, the estimated distribution contains information about the problem solving in general. Thus the method is not focused only on separable LSGO problems.

Next we need to define the number of variables that will be fixed. There exist many strategies. For example, the splitting-in-half method divides an $n$ -
dimensional problem into two $n / 2$ subcomponents. In general, we will define the number of fixed variables as a percentage of the chromosome length and will denote it as $\alpha$. The value of $\alpha$ can be constant or can change during the run of the algorithm. The variables and corresponding components of the probability vector are fixed for some predefined number of generations, which is called an adaptation period (denoted as $t_{\text {adapt }}$ ). The list of fixed components is randomly defined.

In this paper, the straight-forward approach is used, $\alpha$ and $t_{\text {adapt }}$ are predefined and constant.

The main advantage of such EDA-based decomposition is that we do not lose the previously collected statistic as we fix components of the probability vector. The GA solves the problem of reduced dimensionality and updates the probability only for active components. After each adaptation period we will randomly fix other components, and the previously fixed components will continue updating their saved values.

### 3.2 The GA with EDA-based Decomposition for LSGO

We will describe the proposed LSGO algorithm in detail.

First, we need to encode the initial problem into a binary representation. The standard binary or Grey code can be used. A chromosome length $n$ is defined. Next, specific parameters of the EDA-based decomposition and the chosen GA, maximum number of fitness evaluations ( $\operatorname{MaxFE}$ ) or maximum number of generations ( $\operatorname{MaxGEN}$ ) are defined. The maximum

number of generations can be substituted with any other stop condition (for example, time-based condition).

Finally, the following algorithm is used:
Input: $n, N, \alpha, \delta, t_{\text {adapt }}$, MaxFE, the GA operators' parameters.

Initialization:
Randomly generate a population of $N$ individuals of the length $n$.

Calculate $P(0)$ using formula (1).

Main loop.
Until MaxFE is reached:

1. Problem decomposition stage: Start new adaptation period. Fix random $\alpha$ components in chromosomes and in the probability vector.
2. Subcomponent optimization stage: Run the GA for $t_{\text {adapt }}$ generations:
a. Fitness evaluation. Set values in fixed positions of chromosomes according to $P(t)$ using formula (2).
b. Perform selection, crossover and mutation operations.
c. Create next generation, update the probability vector $P(t)$ for active components.

Output: the best-found solution.

### 3.3 Parallel Modification with Self-Configuration

Many proposed LSGO approaches with the subcomponent grouping are based on cooperative coevolution. In this case, many populations are used, which evolve different groups of subcomponents. The cooperation is used on the fitness evaluation step to define the values of components that were fixed during the algorithm run. Usually, components of the best individuals from other populations are used.

We will introduce many parallel populations using the following scheme. At the main loop, the total population of size $N$ is divided into $K$ populations of size $M$, where $N=K \cdot M$. For each population the problem decomposition and the subcomponent optimization steps are independently performed. Thus each population can be viewed as an island with its own decomposition strategy. When the adaptation period is over, all individuals from all populations are collected back into the total population and the summary statistic is updated. This step can be viewed as the cooperation.

As is known, the island model GA can outperform the standard single-population GA for many complex
optimization problems (Gonga et al., 2015). We can also decrease the computational time by implementing the GA with a parallel multi-core or multi-processor computer.

We will use the following approach for selfconfiguration of the GA parameters. First, we define a list of different genetic operators: selection types, crossover types and values of mutation intensity. Next, we set probabilities for each operator to be chosen. All probabilities are initialized with equal values. During the GA run, we define a combination of genetic operators, which is used for producing offspring according to the given probabilities distribution. Finally, after each generation we redistribute the probabilities in order to increase probabilities of operators that have produced offspring with better fitness values. More detailed information about the approach can be found in (Semenkin and Semenkina, 2012).

Also we will provide additional interaction of subpopulation in the island model using concept proposed in (Sopov, 2015). We will increase the size of island with the best performance over some predefined number of generations (adaptation period). The migration operation will copy the current best-found solution to each island to equate the start positions of all population for the next adaptation period.

## 4 EXPERIMENTAL RESULTS

To estimate the proposed approach performance, we have used 15 large-scale benchmark problems from the CEC'2013 Special Session and Competition on Large-Scale Global Optimization (Li et al., 2013a). These problems represent a wider range of real-world large-scale optimization problems and provide convenience and flexibility for comparing various evolutionary algorithms specifically designed for large-scale global optimization. There are 3 fullyseparable problems (denoted as $f 1-f 3$ ), 8 partially separable problems ( $f 4-f 7$ with a separable subcomponent and $f 8-f 11$ with no separable subcomponents), 3 problems with overlapping subcomponents (f12-f14), and 1 non-separable problem (f15).

The experiment settings are:

- Dimensions for all problem are $\mathrm{D}=1000$;
- The standard binary encoding is used with accuracies: $\varepsilon=0.1$ for $\mathrm{f} 1, \mathrm{f} 4, \mathrm{f} 7, \mathrm{f} 8$ and $\mathrm{f} 11-15$, $\varepsilon=0.05$ for f 3 , f 6 and f 10 , and $\varepsilon=0.01$ for $\mathrm{f} 2, \mathrm{f} 5$ and f9;

Table 1: Experimental results for the f1 problem and the EDA-based decomposition with the single-population GA.

Table 2: Experimental results for the f1 problem and the EDA-based decomposition with the island GA.

- For each problem the best, mean, and standard deviation of the 25 independent runs are evaluated;
- Maximum number of fitness evaluations is $\operatorname{MaxFE}=3.0 \mathrm{e}+6$
- The performance estimation is performed for the number of fitness evaluations equal to $1.2 \mathrm{e}+5,6.0 \mathrm{e}+5$ and $3.0 \mathrm{e}+6$.
The EDA-based decomposition GA settings are:
- Population sizes are $\mathrm{N}=1000$ for the singlepopulation version, $\mathrm{N}=500$ for the island version with 3 islands, and $\mathrm{N}=400$ for 5 islands;
- The adaptation period is $t_{\text {adapt }}=100$;
- The probability threshold is $\delta=0.05,0.15$ and 0.25 ;
- Numbers of fixed components are $\alpha=25 \%$, $50 \%$ and $75 \%$ of the chromosome length.
All algorithms have been implemented in Visual Studio C++ using the OpenMP for parallel computing with multi-core PC. Free C++ source codes of the benchmark problems are taken from (http://goanna.cs.rmit.edu.au/ xiaodong/cec13-lsgo/ competition/lsgo_2013_benchmarks.zip, 2013).

We have carried out the above-mentioned experiments and have established the following. In the case of single population, the best performance on
average is achieved with $50 \%$ fixed components and $\delta=0.15$. In the case of the island model, the best results are obtained by the 5 island model with $75 \%$ fixed components and $\delta=0.15$. Almost for every considered value of parameters, the island model outperforms the single population version of the algorithm.

Let's discuss it in detail. We have estimated the algorithm performance for each benchmark problem varying the percentage of fixed components $(\alpha)$ and the confidence level value $(\delta)$. The results for the f1 problem are presented in Table 1 and 2. Table 1 contains the results obtained with the singlepopulation algorithm, and. Table 2 contains results obtained with the 5 island GA. As we can see from Tables, the island model version outperforms the single-population version almost for all combinations of parameters.

We have visualized the best-found value depending on the $\alpha$ and the $\delta$ parameters for each of 3 numbers of fitness evaluations. The best-found value has been normalized to $[0,1]$ interval and averaged over all benchmark problems. The dependences are presented in Figures 2 and 3. As we can see from Figures, the best performance on average is obtained with high percentage of fixed components. In the case of single population, the best

![img-2.jpeg](img-2.jpeg)

Figure 2: Performance of the single-population algorithm via the $\alpha$ and the $\delta$ parameters change for $\operatorname{MaxFE}=\{1.2 \mathrm{e}+5,6.0 \mathrm{e}+5$, $3.0 \mathrm{e}+6\}$.
![img-2.jpeg](img-2.jpeg)

Figure 3: The Performance of the 5 island algorithm via the $\alpha$ and the $\delta$ parameters change for $\operatorname{MaxFE}=\{1.2 \mathrm{e}+5,6.0 \mathrm{e}+5$, $3.0 \mathrm{e}+6\}$.
components. In the case of single population, the best combination is $(\alpha=50 \%, \delta=0.15)$ for the $\operatorname{MaxFE}=1.2 \mathrm{e}+5$, but it shifts to $(\alpha=50 \%, \delta=0.25)$ for the $\operatorname{MaxFE}=6.0 \mathrm{e}+5$ and $3.0 \mathrm{e}+6$. In the case of the island model, the best combinations are $(\alpha=75 \%,$ $\delta=0.25)$ for the $\operatorname{MaxFE}=1.2 \mathrm{e}+5$ and $(\alpha=75 \%$, $\delta=0.15)$ for the $\operatorname{MaxFE}=6.0 \mathrm{e}+5$ and $3.0 \mathrm{e}+6$. Our hypothesis is that the algorithm requires different parameters settings for different stages of the search process. In further work, an adaptive parameters tuning will be introduces and investigated.

The experimental results for the best found settings are presented in Table 3. The summary results are compared with other techniques presented at the CEC'13 competition. The algorithms are DECC-G (differential evolution (DE) based cooperative coevolution (CC) with random dynamic grouping) (Yang et al., 2008), VMO-DE (variable mesh optimization using differential evolution) ( Li et al., 2013b), CC-CMA-ES (Covariance Matrix Adaptation Evolution Strategy using Cooperative Coevolution) (Liu and Tang, 2013), MOS (Multiple Offspring Sampling (MOS) based hybrid algorithm) (LaTorre et al., 2013), and SACC (smoothing and auxiliary function based cooperative coevolution)
(Wei et al., 2013). We have averaged the performance estimates of all algorithms over all problems and have ranked algorithms by the Best and the Mean values. The results are in Table 4.

As we can see from Table 4, the proposed approach has taken 4th place by the Best criterion and 5th place by the Mean value. We should note that all algorithms except the proposed are specially designed for continuous LSGO problems. The EDA-based decomposition GA does not use any knowledge about search space. Moreover, the chromosome length in the binary algorithm is greater than in the case of the continuous space. Nevertheless, the EDA-based decomposition GA outperforms the CC-CMA-ES by two measures and the DECC-G by the Best value on average.

Our hypothesis is that the proposed approach will be a good tool for solving complex real-world LSGO problems, which usually contain not only continuous variables, but mixed-type variables and can represent arbitrary complex structures. Further investigations of the algorithm structure and parameters can probably improve its performance. In particular, the $\alpha$ value can be adjusted adaptively during the algorithm run using information about the probability vector convergence.

Table 3: Experimental results for the EDA-based decomposition GA with 5 islands and $\square=75 \%$.
Table 4: LSGO approaches comparison.
Table 4: LSGO approaches comparison.
# 5 CONCLUSIONS 

In this paper a novel technique for LSGO that uses a binary GA with EDA-based decomposition is proposed. The EDA is used for collecting statistical data based on the past search experience to predict the convergence of subcomponents and to decrease the problem dimensionality by fixing some genes in chromosomes. We have compared a single population and the island model implementations of the algorithm. The best results have been obtained with the island model version. It yields state-of-the-art LSGO techniques, but the performance is comparable. The advantage of the proposed approach is that it can be applied to problems with arbitrary representations and it needs no a priori information about the search space.

In further work, more detailed analysis of the EDA-based decomposition GA parameters will be provided. A self-configuration will be introduced into the algorithm.

## ACKNOWLEDGEMENTS

The research was supported by the President of the Russian Federation grant (MK-3285.2015.9).
