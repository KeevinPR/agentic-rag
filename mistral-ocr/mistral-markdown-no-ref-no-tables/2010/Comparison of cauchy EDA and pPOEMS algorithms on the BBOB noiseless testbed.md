# Comparison of Cauchy EDA and pPOEMS algorithms on the BBOB Noiseless Testbed 

Petr Pošík<br>Czech Technical University in Prague<br>Faculty of Electrical Eng., Dept. of Cybernetics Technická 2, 16627 Prague 6, Czech Republic posik@labe.felk.cvut.cz


#### Abstract

Estimation-of-distribution algorithm using Cauchy sampling distribution is compared with the iterative prototype optimization algorithm with evolved improvement steps. While Cauchy EDA is better on unimodal functions, iterative prototype optimization is more suitable for multimodal functions. This paper compares the results for both algorithms in more detail and adds to the understanding of their key features and differences.


## Categories and Subject Descriptors

G.1.6 [Numerical Analysis]: Optimization—global optimization, unconstrained optimization; F.2.1 [Analysis of Algorithms and Problem Complexity]: Numerical Algorithms and Problems

## General Terms

Algorithms

## Keywords

Benchmarking, Black-box optimization, Estimation-of-distribution algorithm, Cauchy distribution, POEMS, Iterative prototype optimization with evolved improvement steps

## 1. INTRODUCTION

The black-box optimization benchmarking (BBOB) workshop in 2009 introduced well-prepared set of benchmark functions suitable for a systematic comparison of black-box optimization algorithms. As an important part of the workshop framework, the whole comparison methodology was created. The 2010 issue of the BBOB methodology [2] allows for a detailed comparison of 2 algorithms on the BBOB functions testbed.

The two algorithms selected for the comparison in this article are:

[^0]
## Jiři Kubalík <br> Czech Technical University in Prague <br> Faculty of Electrical Eng., Dept. of Cybernetics Technická 2, 16627 Prague 6, Czech Republic kubalík@labe.felk.cvut.cz

- The estimation-of-distribution algorithm (EDA) with Cauchy sampling distribution (Cauchy EDA) [7]. The data for this algorithm are taken from the 2009 benchmarking.
- The iterative prototype optimization with evolved improvement steps (POEMS) [4], particularly, one of its variants: POEMS with a pool of candidate prototypes (pPOEMS) described in Sec. 2.1. The data for this algorithm were generated using the 2010 framework. ${ }^{1}$

The comparison is made using the new BBOB 2010 postprocessing scripts and templates. Both algorithms fall into the class of evolutionary optimization algorithms, yet they perform in some sense a kind of local search. Their underlying principles are, however, different and it is valueable to look for the effect of their similarities and differences.

In the next section, both algorithms are shortly described and their differences are emphasized. Sec. 3 contains all the results used to compare the algorithms and their discussions. After the presentation of the time demands of both algorithms in Sec. 4, Sec. 5 concludes the paper.

## 2. ALGORITHM PRESENTATION

The exact description of the Cauchy EDA algorithm along with the parameter settings can be found in [7]. The pPOEMS algorithm is described in the next section.

### 2.1 pPOEMS

Prototype Optimization with Evolved Improvement Steps (POEMS) optimization algorithm is a stochastic local search algorithm that uses an evolutionary algorithm for searching the neighborhood of the current best solution. The moves in the search space can be thought of as so-called evolved hypermutations. The concept of the evolved hypermutations has been shown to outperform other mutation-based evolutionary algorithms that use pure random hypermutations for generating new points in the search space on several combinatorial optimization problems $[5,6]$.

A description of the original version of the POEMS algorithm for real-valued optimization can be found in [4]. The inner EA evolves hypermutations which are composed
${ }^{1}$ Despite the fact that the algorithms used different versions of the BBOB framework, the results are still comparable. The set of benchmark functions is the same, the only difference is that in 2009 the algorithms were run on 5 instances of each function with 3 repetitions, while in 2010 the algorithms were tested using 15 different instances of the functions.


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. To copy otherwise, to republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee.
    GECCO'10, July 7-11, 2010, Portland, Oregon, USA.
    Copyright 2010 ACM 978-1-4503-0073-5/10/07 ...\$10.00.

of simple actions of adding a normally distributed real number to each of the coordinates of the prototypes (the length of the action sequence is the same as the search-space dimensionality). The distribution of each single modification is $N\left(0, \sigma_{i}^{2}\right)$, i.e. the expected step length in each direction is different.

The variant, denoted as pPOEMS, uses a pool of candidate prototypes of size PoolSize from which one prototype is chosen in each iteration. Each candidate prototype maintains its own $\sigma_{i}^{2}$ values. Thus, the size of the neighborhood to be searched is different for each candidate prototype. The best modification of the current prototype is sought by an evolutionary algorithm and the resulting solution replaces one of the candidate prototypes in the pool according to the following rules:

1. If the modified prototype is better than the current prototype then the modified prototype replaces the current prototype in the pool of prototypes (option A in 1). The values of $\sigma_{i}^{2}$ of the current prototype are adapted as weighted average of their old values and of the differences between the modified and the current prototype variable values. Finally, this prototype remains the current prototype for the next iteration.
2. If the modified prototype is equally good as the current prototype then it replaces the current prototype in the pool of prototypes (option B in 1) and the values of $\sigma_{i}^{2}$ of the current prototype are adapted in the same way as in the rule nb. 1. However, since no improvement to the current prototype has been achieved in this iteration the next prototype from the prototype pool (meaning the prototype with index $(i+1) \%$ PoolSize, where $i$ is the index of the current prototype) becomes the current prototype for the next iteration.
3. If the modified prototype is worse than the current prototype then the most similar (according to the Euclidean distance) candidate prototype out of the prototypes that have worse fitness than the modified prototype is sought in the pool. If such a prototype exists then it is replaced (option C in 1) by the modified prototype. The values of $\sigma_{i}^{2}$ of the replacement prototype are adapted according to differences between the modified and the replacement prototype variable values.
If such a replacement does not exist then the modified prototype is thrown away and the values of $\sigma_{i}^{2}$ of the current prototype are shrinked as if the differences between the modified and the replacement prototypes were zero. Thus, the values of $\sigma_{i}^{2}$ are maximally decreased.
In both cases next prototype from the pool of prototypes becomes the current prototype for the next iteration.

In all cases 1-3, if for some candidate prototype all its $\sigma_{i}^{2}$ values drop below $10^{-11}$ then they are reinitialized to $0.25 \pi$ (ubound-lbound). The prototype itself remains unchanged.

### 2.2 Algorithm Differences

As already stated, we can look at both algorithms as on quite different instances of local search. The algorithms differ foremost in the following aspects:
![img-0.jpeg](img-0.jpeg)

Figure 1: Schema of the pool of prototypes used in pPOEMS.

- In Cauchy EDA, the neighborhood is given by the shape of the Cauchy distribution, which is used to sample new candidate solutions. In pPOEMS, the search is conducted in the neighborhood of the prototype; the neighborhood is given implicitely by the sequence of actions that are evolved to modify the prototype.
- The Cauchy EDA uses population of tens or hundreds of individuals; after its evaluation, the best solution found so far is updated (and the Cauchy-distribution parameters as well). In pPOEMS, the prototype is updated after certain number of generations spent in the inner EA which evolves the improving sequence of actions. The inner EA run is longer (it runs for $200 \times D$ fitness evaluations) and the updates of prototypes are therefore less frequent, especially for higher dimensions.
- Both algorithms can get stuck in local optima. The Cauchy EDA prevents this situation by independent restarts, as suggested in the BBOB methodology. The pPOEMS algorithm is not restarted; instead it maintains a pool of candidate prototypes which can be used in situations when the inner EA is not able to evolve an improving sequence from the current prototype.
For both algorithms, the crafting effort $\mathrm{CrE}=0$.


## 3. RESULTS

Results from experiments according to [2] on the benchmark functions given in $[1,3]$ are presented in Figures 2, 3 and 4 and in Table 1. The expected running time (ERT), used in the figures and table, depends on a given target function value, $f_{\mathrm{t}}=f_{\text {opt }}+\Delta f$, and is computed over all relevant trials as the number of function evaluations executed during each trial while the best function value did not reach $f_{\mathrm{t}}$, summed over all trials and divided by the number of trials that actually reached $f_{\mathrm{t}}[2,8]$. Statistical significance is tested with the rank-sum test for a given target $\Delta f_{\mathrm{t}}\left(10^{-8}\right.$ in Figure 2) using, for each trial, either the number of needed function evaluations to reach $\Delta f_{\mathrm{t}}$ (inverted and multiplied by -1 ), or, if the target was not reached, the best $\Delta f$-value achieved, measured only up to the smallest number of overall function evaluations for any unsuccessful trial under consideration.

Cauchy EDA outperforms the pPOEMS algorithm on functions $1,2,5,7,9,10,11,12,13,14,17,18$ for the tight target

![img-1.jpeg](img-1.jpeg)

Figure 2: ERT ratio of CauchyEDA divided by pPOEMS versus $\log _{10}(\Delta f)$ for $f_{1}-f_{21}$ in $2,3,5,10,20,40-\mathrm{D}$. Ratios $<10^{6}$ indicate an advantage of CauchyEDA, smaller values are always better. The line gets dashed when for any algorithm the ERT exceeds thrice the median of the trial-wise overall number of $f$-evaluations for the same algorithm on this function. Symbols indicate the best achieved $\Delta f$-value of one algorithm (ERT gets undefined to the right). The dashed line continues as the fraction of successful trials of the other algorithm, where 0 means $0 \%$ and the y -axis limits mean $100 \%$, values below zero for CauchyEDA. The line ends when no algorithm reaches $\Delta f$ anymore. The number of successful trials is given, only if it was in $\{1 \ldots 9\}$ for CauchyEDA (1st number) and non-zero for pPOEMS (2nd number). Results are significant with $p=0.05$ for one star and $p=10^{- \# s}$ otherwise, with Bonferroni correction within each figure.

![img-2.jpeg](img-2.jpeg)

Figure 3: Expected running time (ERT in $\log 10$ of number of function evaluations) of CauchyEDA versus pPOEMS for 46 target values $\Delta f \in\left[10^{-8}, 10\right]$ in each dimension for functions $f_{1}-f_{24}$. Markers on the upper or right egde indicate that the target value was never reached by CauchyEDA or pPOEMS respectively. Markers represent dimension: $2:+, 3: \nabla, 5: \times, 10: \circ, 20: \square, 40: \diamond$.

![img-3.jpeg](img-3.jpeg)

Figure 4: Empirical cumulative distributions (ECDF) of run lengths and speed-up ratios in 5-D (left) and 20D (right). Left sub-columns: ECDF of the number of function evaluations divided by dimension $D$ (FEvals/D) to reach a target value $f_{\text {opt }}+\Delta f$ with $\Delta f=10^{k}$, where $k \in\{1,-1,-4,-8\}$ is given by the first value in the legend, for CauchyEDA (solid) and pPOEMS (dashed). Light beige lines show the ECDF of FEvals for target value $\Delta f=10^{-8}$ of algorithms benchmarked during BBOB-2009. Right sub-columns: ECDF of FEval ratios of CauchyEDA divided by pPOEMS, all trial pairs for each function. Pairs where both trials failed are disregarded, pairs where one trial failed are visible in the limits being $>0$ or $<1$. The legends indicate the number of functions that were solved in at least one trial (CauchyEDA first).

![img-4.jpeg](img-4.jpeg)

Table 1: Expected running time (ERT in number of function evaluations) divided by the best ERT measured during BBOB-2009 (given in the respective first row) for different $\Delta f$ values for functions $f_{1}-f_{24}$. The median number of conducted function evaluations is additionally given in italics, if $\operatorname{ERT}\left(10^{-7}\right)=\infty$. \#succ is the number of trials that reached the final target $f_{\text {opt }}+10^{-8}$. 0: pPO is pPOEMS and 1: Cau is CauchyEDA. Bold entries are statistically significantly better compared to the other algorithm, with $p=0.05$ or $p=10^{-k}$ where $k>1$ is the number following the $*$ symbol, with Bonferroni correction of 48.

Table 2: The average time demands per function evaluation (in microseconds) of the two compared algorithms.

values, while pPOEMS beats Cauchy EDA on functions 3, $4,15,16,19,20,22$. (The results on the other functions are mixed, or neither algorithm solved the problem successfully.) In this small competition the Cauchy EDA wins 12:7. It can be stated that Cauchy EDA beats pPOEMS mainly on the unimodal functions, while pPOEMS is better on multimodal ones.

The pPOEMS algorithm is not invariant with respect to the rotation of the search space. The evolved actions operate on 1 dimension only (making axis-parallel modifications only), nevertheless, the whole action sequences (hypermutations) result in non-axis-paralel steps. However, it is easier for this algorithm to optimize separable functions. As an example, we can look at function pair 2-10 in Fig. 2: the non-rotated version of the ellipsoid function is much easier for pPOEMS, while it cannot solve the rotated version in higher dimensions at all. And even though the Rosenbrock function (8) is not separable, its rotated version (9) is for pPOEMS much harder as well.

In lower dimensions, Cauchy EDA is often orders of magnitude faster than pPOEMS. With increasing dimensionality this gap reduces, and the speed of both algorithms becomes almost equal (e.g. for 20D versions of sphere and ellipsoid functions). It may be anticipated that for larger dimensions pPOEMS would overtake the Cauchy EDA.

Looking at Fig. 4, it can be stated that pPOEMS beats CauchyEDA clearly on separable functions. It is better also for multimodal and weak-structure functions, but neither algorithm is really successful on these (especially in 20D). Cauchy EDA is a clear winner for ill-conditioned functions and for moderate functions in lower dimensions.

## 4. CPU TIMING EXPERIMENTS

The time requirements of Cauchy EDA are taken from [7]. The multistart algorithm was run with the maximal number of evaluations set to $10^{5}$, the basic algorithm was restarted for at least 30 seconds. These experiments have been conducted on Intel Core 2 CPU, T5600, 1.83 GHz, 1 GB RAM with Windows XP SP3 in MATLAB R2007b for Cauchy EDA and on Intel Pentium-M 1400 MHz with Windows XP SP3 using the implementation in C for pPOEMS. The comparison of the average time demands per function evaluation are shown in Table 2.

The differences in the average time needed for function evaluation are caused by the fact that CauchyEDA was implemented in MATLAB while pPOEMS in C. The MATLAB implementation becomes more efficient for larger populations.

## 5. CONCLUSIONS

Cauchy EDA and POEMS algorithm with a pool of candidate prototypes were compared using the BBOB 2010 methodology. The results confirm that pPOEMS searches much
broader neighborhood than Cauchy EDA. The pPOEMS algorithm is able to solve certain percentage of multimodal functions, while the performace of Cauchy EDA is for them rather weak (and the restarting does not help much).

The pPOEMS algorithm is rather slow (compared to Cauchy EDA and other algorithms taking part in BBOB 2009) which showed up especially on unimodal functions. The pPOEMS greatly suffers from the fact that the individual actions in the improving sequence operate over axis-parallel directions. For non-separable functions, this renders the crossover operator used in the inner EA of POEMS rather useless since the individual actions are correlated. To incorporate a method that would decorrelate the actions between the individual inner-EA launches remains as future work.

## Acknowledgements

Petr Pošík is supported by the Grant Agency of the Czech Republic with the grant no. 102/08/P094 entitled "Machine learning methods for solution construction in evolutionary algorithms". Jiří Kubalík is supported by the Ministry of Education, Youth and Sport of the Czech Republic with the grant No. MSM6840770012 entitled "Transdisciplinary Research in Biomedical Engineering II".
