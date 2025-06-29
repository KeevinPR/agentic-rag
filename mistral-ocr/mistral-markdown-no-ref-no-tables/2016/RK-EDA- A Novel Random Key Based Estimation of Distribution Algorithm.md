# RK-EDA: A Novel Random Key Based Estimation of Distribution Algorithm 

Mayowa Ayodele ${ }^{(\boxtimes)}$, John McCall, and Olivier Regnier-Coudert<br>Robert Gordon University, Aberdeen, UK<br>\{m.m.ayodele,j.mccall, o.regnier-coudert\}@rgu.ac.uk


#### Abstract

The challenges of solving problems naturally represented as permutations by Estimation of Distribution Algorithms (EDAs) have been a recent focus of interest in the evolutionary computation community. One of the most common alternative representations for permutation based problems is the Random Key (RK), which enables the use of continuous approaches for this problem domain. However, the use of RK in EDAs have not produced competitive results to date and more recent research on permutation based EDAs have focused on creating superior algorithms with specially adapted representations. In this paper, we present RK-EDA; a novel RK based EDA that uses a cooling scheme to balance the exploration and exploitation of a search space by controlling the variance in its probabilistic model. Unlike the general performance of RK based EDAs, RK-EDA is actually competitive with the best EDAs on common permutation test problems: Flow Shop Scheduling, Linear Ordering, Quadratic Assignment, and Travelling Salesman Problems.


Keywords: Estimation of distribution algorithm $\cdot$ Random key $\cdot$ Permutation problems $\cdot$ Cooling scheme $\cdot$ Univariate model

## 1 Introduction

Estimation of Distribution Algorithms (EDAs) are Evolutionary Algorithms (EAs) that generate solutions by sampling a Probabilistic Model (PM) of promising solutions. The ability to model the features of more promising solutions is a major attribute that differentiates them from most other EAs [7]. They benefit from the use of machine learning techniques, which makes them better at solving certain categories of larger and more difficult problems [12]. Problems naturally represented as permutations have however been identified as challenging for EDAs. This is attributed to the fact that EDAs have not been extensively explored to solve this class of problems [3]. EDAs for permutation spaces have therefore been a focus of research in recent years.

EDAs applied to permutations have been categorised into ad hoc approaches with varying strategies, integer space based and continuous space based [3]. One of the common continuous representations for solving permutations in EAs is the well-known Random Key (RK). RKs have an advantage over most other permutation representations as they always produce permutation feasible solutions.

This is particularly not the case for integer based EDAs as they often require a procedure to handle the mutual exclusivity constraint.

RK based EDAs have however been considered the poorest [3] of the EDAs designed for permutation problems. RK representation has not been sufficiently adapted to benefit from the operation of EDA. It contains some inherent redundancy as a result of several RKs producing the same ordering thereby introducing plateaux to the search space $[2,3,13]$. Also, variability in the values that capture the same priority across solutions of a population limits the information captured by the probabilistic model. They therefore struggle to produce competitive results [7]. Models that are more specific to permutations such as histogram models $[16,17]$, permutation distribution models [4-6] and factoradics [14] have shown better performances.

Some classical examples of RK based EDAs are REDA [15], EGNA ${ }_{e e}$ $\& U M D A_{c}[10]$. REDA uses the triangulation of Bayesian network approach and focuses on model efficiency by modelling subset nodes of a problem. EGNA ${ }_{e e}$ builds a Gaussian network where the structure of a problem is learnt using edge exclusion tests [10]. The UMDA ${ }_{c}$ which is also a structure identification algorithm based on Gaussian network performs hypothesis tests to identify the density of its model's components. In addition, IDEA-ICE [2] can also be classified as a RK based EDA, although it uses a crossover operator to preserve building blocks in addition to its probabilistic model. Also, RKs associated with the building blocks are rescaled to improve the likelihood of them being properly combined. The IDEA-ICE shows better performance compared to the classical RK based EDAs.

The proposed Random Key Estimation of Distribution Algorithm (RK-EDA) attempts to capture some of the identified limitations of RKs as well as exploit their advantages.

The rest of this paper is described as follows. Section 2 motivates and describes the novel algorithm, RK-EDA. A discussion of problem sets and experimental design is presented in Sect. 3. Section 4 presents and discusses results while conclusions are presented in Sect. 5.

# 2 RK-EDA 

The proposed RK-EDA is a univariate EDA whose probabilistic model, similar to UMDA ${ }_{c}$, is based on mean values of genes in more promising solutions of a population. It exploits already found good genes by sampling a Gaussian distribution based on mean and variance values. Unlike UMDA ${ }_{c}$, RK-EDA imposes a user defined variance parameter rather than a population generated one. This is because we achieved better performance using a controlled variance value. Furthermore, we propose to use a cooling rate parameter to control exploration and exploitation. This controls the level of variance in solutions of a population such that there is more exploration at the start of the algorithm, which automatically cools as the search progresses.

In this section, we present the algorithmic details of RK-EDA.

```
Algorithm 1. RK-EDA
    1: Initialise \(\sigma, t_{s}\) and \(p_{s}\)
    Generate initial population \(P\) of size \(p_{s}\)
    for \(g=1\) to MaxGen do
        Evaluate and rescale individuals in \(P\)
        Select best \(t_{s}<p_{s}\) solutions to form \(S\)
        Calculate \(\mu_{S}\)
        \(c=1-\frac{g}{\text { MaxGen }}\)
        \(\sigma_{g}=\sigma * c\)
        \(M=N\left(\mu_{S}, \sigma_{g}\right)\)
        \(P_{\text {new }}=\emptyset\)
        repeat
            Sample \(M\) to generate offspring off
            Add off to \(P_{\text {new }}\)
        until \(\left|P_{\text {new }}\right|=p_{s}\)
        \(P=P_{\text {new }}\)
    end for
```

As shown in Algorithm 1, RK-EDA requires the initialisation of three parameters which are initial variance $\sigma$, truncation size $t_{s}$ and population size $p_{s}$. Since the stopping criteria is based on the number of fitness evaluations allowed $(F E s)$, the maximum number of generations $\operatorname{MaxGen}$ is estimated by dividing $F E s$ by $p_{s}$.

A population $P$ of RKs is randomly generated, evaluated and rescaled. The rescaling procedure requires the conversion of RKs to ranks e.g. $[0.12,0.57,0.23$, $0.25,0.99]$ becomes $[1,4,2,3,5]$. The ranks are then rescaled to values between 0 and 1 . This is done by setting $\operatorname{rescaled} R K_{i}=\frac{\operatorname{rank}_{i}-1}{n-1}$ where $\operatorname{rescaled} R K_{i}$ and $\operatorname{rank}_{i}$ are respectively the rescaled RK and rank of gene $i$, and $n$ is the problem size. The RK in the previous example therefore becomes $[0.00,0.75,0.25,0.50$, 1.00]. With this approach, another set of RKs $[0.01,0.06,0.03,0.04,0.2]$ which is the same solution as the previous example will have the same rescaled RK value $[0.00,0.75,0.25,0.50,1.00]$. With this approach, we are able to minimise redundancy and improve the information captured by the probabilistic model.

The best $t_{s}$ solutions of the population are selected to generate a population $S$. Also, $\mu_{S}$ in $\ln$. (6) is an array $\mu_{S_{1}}, \ldots, \mu_{S_{n}}$ that saves the mean of all RKs at indexes $\{1 \cdots n\}$ in the selected population $S$. Note that $\mu_{S_{n}}$ refers to the mean of all RKs in the $n^{\text {th }}$ index of each solution of $S$.

Cooling Rate $c$ is calculated with respect to the particular generation such that its value is higher for the first few iterations and lower at the last set of iterations. As shown in $\ln$. (8), $c$ is used to generate generational variance $\sigma_{g}$. Multiplying $c$ with $\sigma$ to form $\sigma_{g}$ makes it possible to achieve higher exploration at the start of the algorithm and more exploitation as $g$ increases.

Furthermore, $M$ is defined as a normal distribution $N\left(\mu_{S}, \sigma_{g}\right)$ and is updated for each generation $g$. Unlike $\mu_{S}$ which is an array of values, $\sigma_{g}$ is not an array but a single value. An offspring solution off is generated by sampling $M$. Each gene $i(1 \leq i \leq n)$ of off is generated based on $\sigma_{g}$ and $\mu_{S_{i}}$, off is repeatedly

added to the offspring population $P_{\text {new }}$ until its size equals $p_{s}$. At the end of each generation, $P_{\text {new }}$ completely replaces the parent population $P$.

# 3 Experimental Settings 

In this section we present the permutation problem instances as well as the parameter settings.

### 3.1 Permutation Problems

To assess the performance of RK-EDA, we apply it to a range of permutation benchmark problems. These problems include Flow Shop Scheduling Problem (FSSP), Linear Ordering Problem (LOP), Quadratic Assignment Problem (QAP) and Travelling Salesman Problem (TSP). These are formerly defined in [3], we have used the same objective functions as presented in the review paper and is summarised in Table 1. Note that we also consider the more recently used Total Flow Time (TFT) criteria for further experiments on the FSSP.

Table 1. Definition of the permutation problems

### 3.2 Problem Sets

We evaluate RK-EDA using the selected permutation problems in [14]. We acknowledge that many of the problems are small instances especially the FSSP. Also, results from running RK-EDA on the FSSP problem instances gives an intuition that the algorithm is more competitive on the FSSP. We therefore added four larger FSSP problems.

The problem sets used in this paper are listed below.

1. TSP: bays29, berlin52, dantzig42 and fri26
2. FSSP: tai20-5-0, tai20-5-1, tai20-10-0 and tai20-10-1 (smaller instances) tai50-10-0, tai50-10-1, tai100-20-0 and tai100-20-1 (larger instances)
3. QAP: tai15a, tai15b, tai40a and tai40b
4. LOP: t65b11, be75np and be75oi

These are commonly used problems and we consider them useful for comparing with other EDAs for permutation problems.

# 3.3 Parameter Setting 

To be able to understand the parameter settings that suit RK-EDA, we explored a range of values and found different parameters suitable for different problem classes and sizes. To be able to make a fair comparison between RK-EDA and the considered algorithms, we use a set of parameters across all problems as done in the review [3]. The set of parameters used for RK-EDA is shown in Table 2. Based on preliminary tests, these parameters produce relatively good quality solutions across all problem classes and instances.

Table 2. Parameter values for RK-EDA

## 4 Results and Discussion

In this section, we present the results of running RK-EDA on the aforementioned permutation problem sets. Table 3 shows the minimum, maximum, average and standard deviation based on 10 runs of RK-EDA using the parameters presented in Table 2. Results are compared based on averages and standard deviations. We have highlighted results where optimal solution was found (appended *). We also highlight results that are significantly better (appended $\checkmark$ ) or not significantly different (appended ${ }^{* *}$ ) from the best of the reviewed algorithms. We used the student t-test to measure statistical significance with a 0.05 significance level.

The results in Table 3 are presented according to problem classes. Note that $\mathrm{FSSP}_{s}$ and $\mathrm{FSSP}_{l}$ respectively denote the smaller and larger instances of the FSSP.

Table 3. Average performance of RK-EDA on benchmark problems
Table 4 shows the performance of each algorithm on the considered problems. The table is ordered according to the overall ranks shown in column "ALL". Columns TSP, FSSP $_{s}$, QAP, LOP and FSSP $_{l}$ show the average ranks of algorithms on instances of their respective problem classes. Column ALL is the average rank of algorithms on all instances of TSP, FSSP $_{s}$, QAP and LOP. Since one of the motivations for selecting the additional problems $\left(\mathrm{FSSP}_{l}\right)$ is that we ranked relatively high on $\mathrm{FSSP}_{s}, \mathrm{FSSP}_{l}$ was not used to create the overall rank so as to eliminate bias towards performance on FSSP. Also, since one of the reviewed algorithms was not applied to instances of $\mathrm{FSSP}_{l}$, it will be impossible to generate an overall rank for the algorithm. To generate the ranks shown in the table, we use the average fitness recorded by each algorithm as reported in [3] and [14] as well as that of RK-EDA shown in Table 3. All algorithms are ranked from best to worst for each problem.

We used "-" to denote missing results where authors have not applied their algorithm to the given problem class.

According to the review presented in [3], $\mathrm{EHBSA}_{W T}$ and $\mathrm{NHBSA}_{W T}$ were recognised as the best performing algorithms. A similar result is depicted by the overall rank of these algorithms in Table 4. EHBSA $_{W T}$ ranks $1^{s t}$ while RK-EDA ranks $2^{n d}$ with $\mathrm{NHBSA}_{W T}$.

Table 4. Average ranks of algorithms

We observed that the RK based EDAs such as $\mathrm{REDA}_{U M D A}, \mathrm{REDA}_{M I M I C}$, $\mathrm{EGNA}_{e e}, \mathrm{UMDA}_{c}$ as well as the RK based GA (OmeGA) are ranked least in Table 4 which is similar to the conclusion in the review Ceberio et al. [3]. OmeGA had been introduced in the review to compare with the performance of the EDAs in general. RK-EDA however shows a different trait outperforming all other RK based algorithms.

Furthermore, the performance of RK-EDA varies with different classes of problems. It produced competitive results on the FSSP, ranking $2^{n d}$ on FSSP $_{s}$ and $1^{\text {st }}$ on FSSP $_{l}$. RK-EDA produced statistically better results than the best of the reviewed algorithms on three FSSP $_{l}$ instances. It also produced competitive results for the TSP and LOP but much less competitive performance on the QAP. This may be attributed to the fact that parameters that suit other problem classes are not particularly suitable for the search space presented by the QAP.

In addition to the reviewed algorithms, other permutation based EDAs exist but were not included in the previous comparison because their results are not reported on the selected problems. GM-EDA [4] exhibits the best results on FSSP when hybridised with local search procedures such as variable neighbourhood search (VNS). We therefore compare RK-EDA with GM-EDA on a selected set of FSSP instances. In order to compare the two EDAs in a fair way, we use the reported results of GM-EDA without VNS.

We use the same set of parameters presented by the authors in [4] except that we do not consider elitism. This is because preliminary experiments show that

Table 5. Parameter values and stopping criteria for experiments on FSSP based on TFT

Table 6. Average TFT for FSSP

elitism does not improve the performance of RK-EDA. In addition, 0.15 initial variance value particularly produced competitive results for FSSP instances. Table 5 shows the parameters of RK-EDA, which are adapted for solving the FSSP.

In Table 6, we present the average fitness over 20 runs for RK-EDA as well as GM-EDA. The results are based on the Total Flow Time (TFT) objective function

and we compare using instances of $\mathrm{FSSP}_{s}$ and $\mathrm{FSSP}_{l}$. The results for GM-EDA have been extracted from [4]. Values that are significantly better are presented in bold. The results show that the GM-EDA is significantly better on two of the smallest problems (tai20-5-0 and tai20-10-1) while RK-EDA shows significant improvement on the largest problems (tai100-20-0 and tai100-20-1). There are however no significant difference between the performance of the algorithms on other instances.

Results from comparing RK-EDA with GM-EDA as shown in Table 6 also indicate that RK-EDA is competitive and should be further explored to solve bigger and more complex problems.

# 5 Conclusions 

EDAs based on RKs have previously been considered the poorest of permutation based EDAs [3]. One of the problems posed by RKs is attributed to the variety of ways of representing an ordering [13]. In this paper, we introduce a novel RK based EDA (RK-EDA) which addresses this by rescaling the RKs uniformly. This approach improves the information captured by the probabilistic model. Furthermore, RK-EDA uses a cooling scheme to manage the rate of exploration/exploitation of the search space such that there is better exploration at the start of the algorithm and better exploitation of already found good pattern as the search progresses.

Furthermore, learning a probability structure is considered the most expensive operation in EDAs [2], we present a simple model, which only saves the mean of solutions in a selected population. This is relatively computationally efficient. RK-EDA whose procedure is comparatively simple produces very competitive results. It outperforms other reviewed continuous EDAs. It is also competitive with the best permutation EDAs in general.

RK-EDA's most competitive performance is seen on FSSP and the least on QAP. It's performance on FSSP gets more competitive as the problem size increases presenting the best results on the largest of the considered FSSP instances. The performance of RK-EDA on larger problems is therefore recommended for further investigation.

In addition, the use of local search has been reported to improve the performance of the GM-EDA, hybridisation of the RK-EDA may also improve its performance.
