# Comparison of Cauchy EDA and Rosenbrock's Algorithms on the BBOB Noiseless Testbed 

Petr Pošík<br>Czech Technical University in Prague<br>Faculty of Electrical Engineering, Department of Cybernetics<br>Technická 2, 16627 Prague 6, Czech Republic<br>posik@labe.felk.cvut.cz


#### Abstract

Estimation-of-distribution algorithm equipped with Cauchy distribution (Cauchy EDA) is compared with Rosenbrock's local search algorithm. Both algorithms were already presented at the 2009 black-box optimization benchmarking workshop where Cauchy EDA usually ranked better than Rosenbrock's algorithm. This paper compares them in more detail and adds to the understanding of their key differences.


## Categories and Subject Descriptors

G.1.6 [Numerical Analysis]: Optimization—global optimization, unconstrained optimization; F.2.1 [Analysis of Algorithms and Problem Complexity]: Numerical Algorithms and Problems

## General Terms

Algorithms

## Keywords

Benchmarking, Black-box optimization, Estimation-of-distribution algorithm, Cauchy distribution, Rosenbrock's algorithm

## 1. INTRODUCTION

During the black-box optimization benchmarking (BBOB) workshop in 2009 many diverse algorithm were benchmarked on a well-prepared set of functions using common conditions. The BBOB 2010 methodology [2] provides additional means to compare two algorithms in more detail. In this paper, two algorithms which took part in the BBOB 2009 workshop are further compared. Data for both algorithms were taken from the 2009 benchmarking, but the comparison is made using the new post-processing scripts and templates for BBOB 2010.

The two algorithms chosen for the comparison are:

[^0]- Rosenbrock's algorithm introduced in [8]. It could be described as an adaptive pattern search. Its performance on the BBOB 2009 noiseless test suite was reported in [6].
- The estimation-of-distribution algorithm (EDA) with Cauchy sampling distribution (Cauchy EDA) [5]. It represents the class of evolutionary optimization algorithms.
Despite their different origins, both algorithms maintain the model of local neighborhood. It is interesting to see if there exists any systematic difference resulting from the different adaptation mechanisms and other differences between the algorithms, or if the similar principle of maintaining the model of the local neighborhood also unifies the performance of both algorithms.
In the next section, both algorithms are shortly described and their differences are emphasized. Sec. 3 contains all the results used to compare the algorithms and their discussions. After the presentation of the time demands of both algorithms in Sec. 4, Sec. 5 concludes the paper.


## 2. ALGORITHM PRESENTATION

The exact descriptions of the algorithms along with the parameter settings can be found in [6] and [5], respectively. The main differences between the algorithms are:

- The Cauchy EDA is a population based algorithm, while Rosenbrock's algorithm maintains the best-sofar solution only.
- The Cauchy EDA updates the model of the local neighborhood on the basis of (a relatively large set of) selected individuals each generation. Rosenbrock's algorithm updates the model (orthonormal basis) only in strictly defined situations; the time periods which use the same model may last varying number of iterations.
- The Cauchy EDA uses the Cauchy distribution to sample new candidate solutions. Rosenbrock's algorithm uses strictly defined pattern to sample new candidates; it iterates over all axes of the orthonormal basis and generates one solution in the respective direction in a particular iteration.
- To fight the premature convergence, it uses a constant multiplier to enlarge the variance of the distribution (as suggested in [4]). Rosenbrock's algorithm needs no such modification.
For both algorithms, the crafting effort $\mathrm{CrE}=0$.


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. To copy otherwise, to republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee.
    GECCO'10, July 7-11, 2010, Portland, Oregon, USA.
    Copyright 2010 ACM 978-1-4503-0073-5/10/07 ...S10.00.

## 3. RESULTS

Results from experiments according to [2] on the benchmark functions given in $[1,3]$ are presented in Figures 1, 2 and 3 and in Table 1. The expected running time (ERT), used in the figures and table, depends on a given target function value, $f_{\mathrm{t}}=f_{\text {opt }}+\Delta f$, and is computed over all relevant trials as the number of function evaluations executed during each trial while the best function value did not reach $f_{\mathrm{t}}$, summed over all trials and divided by the number of trials that actually reached $f_{\mathrm{t}}[2,7]$. Statistical significance is tested with the rank-sum test for a given target $\Delta f_{\mathrm{t}}\left(10^{-8}\right.$ in Figure 1) using, for each trial, either the number of needed function evaluations to reach $\Delta f_{\mathrm{t}}$ (inverted and multiplied by -1 ), or, if the target was not reached, the best $\Delta f$-value achieved, measured only up to the smallest number of overall function evaluations for any unsuccessful trial under consideration.

Rosenbrock's algorithm ouperforms Cauchy EDA on functions $1,2,5,6,20,21,22$, and 23 (it is often faster, but Cauchy EDA can solve many of these functions as well), while Cauchy EDA beats G3PCX on functions $7,10,11,13$, 17, and 18 (where Rosenbrock's often fails to find the target level), i.e. in this small competition Rosenbrock's algorithm wins 8:6. (The results on the other functions are mixed, or neither algorithm solved the problem successfully.)

In Fig. 1, we can sometimes see a peak (upward or downward) at the beginning of the ERT ratio lines (functions 1, 5, 13, 14). In the beginning of the evolution, both algorithms need to adapt their models to the fitness landscape. The peak means that Cauchy EDA (upward) or Rosenbrock's algorithm (downward) probably needs more time for this adaptation.

Interesting situation can be seen when comparing results for functions 2 and 10 (separable and non-separable version of the ellipsoid function). In the first case, the model of Rosenbrock's algorithm is actually initialized to the correct one, and it does not need to be adapted (however, it is not clear if any adaptation takes place or not). Thanks to this correct initialization, Rosenbrock's algorithm is faster for the separable problem. The picture for non-separable ellipsoid is, however, completely different. For 2- and 3-dimensional version, Rosebrock's algorithm is still about 2 times faster than Cauchy EDA, but for dimensions 5 and higher Rosenbrock's adaptation mechanism loses its efficiency and the algorithm becomes very slow.

Rosenbrock's algorithm failed on functions 7 (Step-ellipsoid) and on both Schaffer's functions 17 and 18. It seems that for these functions the batch model adaptation using tens or hundreds samples is a better approach than sequential adaptation after each sampled point.

Interesting results may be found for functions 13 (sharp ridge problem) and 14 (sum of different powers): Rosenbrock's algorithm is orders of magnitude faster than Cauchy EDA for a broad range of target levels. But for target levels at about $10^{-5}$ and tighter, Cauchy EDA takes over and its results are much better. It seems that Rosenbrock's algorithm is not even able to find some of the tighter target levels.

Another note can be made on the variance enlargment constant used by Cauchy EDA. It was set to be approximately optimal for Rosenbrock's function. However, such setting may be too large for other functions. The ERT ratio for sphere function shows that with increasing problem

Table 2: The average time demands per function evaluation (in microseconds) of the two compared algorithms.

dimensionality the gap between the algorithms gets larger. Also the results for function 21 and 22 (and possibly for function 23) suggest, that the slow convergence of Cauchy EDA prevents it to be restarted more often which is the key to solve these problems; on the contrary, Rosenbrock's algorithm converges probably much faster and is thus restarted more often which gives it a chance to have higher success rate.

Looking at Fig. 3, it can be stated that Rosenbrock's algorithm beats CauchyEDA mainly on the separable functions and on weak structure functions. On the other hand, Cauchy EDA wins on moderate, ill-conditioned and multimodal functions. It can be stated that if Rosenbrock's algorithm solves a problem, it solves it very quickly, while Cauchy EDA is usually much slower but more robust (is able to solve broader range of problems).

## 4. CPU TIMING EXPERIMENTS

The time requirements of both algorithms are taken from the respective articles, [6] and [5]. The multistart algorithm was run with the maximal number of evaluations set to $10^{5}$, the basic algorithm was restarted for at least 30 seconds. The experiment was conducted on Intel Core 2 CPU, T5600, 1.83 GHz, 1 GB RAM with Windows XP SP3 in MATLAB R2007b. The comparison of the average time demands per function evaluation are shown in Table 2.

The differences in the average time needed for function evaluation are caused by the frequency of calling the evaluation function and by the size of the solution set to be evaluated. While Rosenbrock's algorithm evaluates the solutions one by one, Cauchy EDA uses batches of tens or hundreds of solutions which means that the evaluation routine is called less often and can take advantage of the MATLAB matrix processing capabilities to much larger extent.

## 5. CONCLUSIONS

The results indicate that neither algorithm dominates the other. In cases when Rosenbrock's algorithm is able to find the solution, it finds it quickly. The Cauchy EDA is slower, but can find the solution for a broader set of functions. Of course, this can be attributed to the fact that Cauchy EDA uses a population, while Rosenbrock's algorithm maintains only single point. This observation can be expected for many comparisons of single-point vs. population-based methodsthe fact that both algorithms use a model of the local neighborhood does not change this expectation

## Acknowledgements

The author is supported by the Grant Agency of the Czech Republic with the grant no. 102/08/P094 entitled "Machine learning methods for solution construction in evolutionary algorithms".

![img-0.jpeg](img-0.jpeg)

Figure 1: ERT ratio of CauchyEDA divided by Rosenbrock versus $\log _{10}(\Delta f)$ for $f_{1}-f_{24}$ in $2,3,5,10,20$, 40-D. Ratios $<10^{0}$ indicate an advantage of CauchyEDA, smaller values are always better. The line gets dashed when for any algorithm the ERT exceeds thrice the median of the trial-wise overall number of $f$ evaluations for the same algorithm on this function. Symbols indicate the best achieved $\Delta f$-value of one algorithm (ERT gets undefined to the right). The dashed line continues as the fraction of successful trials of the other algorithm, where 0 means $0 \%$ and the $y$-axis limits mean $100 \%$, values below zero for CauchyEDA. The line ends when no algorithm reaches $\Delta f$ anymore. The number of successful trials is given, only if it was in $\{1 \ldots 9\}$ for CauchyEDA (1st number) and non-zero for Rosenbrock (2nd number). Results are significant with $p=0.05$ for one star and $p=10^{-\# *}$ otherwise, with Bonferroni correction within each figure.

![img-1.jpeg](img-1.jpeg)

Figure 2: Expected running time (ERT in $\log 10$ of number of function evaluations) of CauchyEDA versus Rosenbrock for 46 target values $\Delta f \in\left[10^{-8}, 10\right]$ in each dimension for functions $f_{1}-f_{24}$. Markers on the upper or right egde indicate that the target value was never reached by CauchyEDA or Rosenbrock respectively. Markers represent dimension: $2:+, 3: \nabla, 5: \mathrm{s}, 10: \circ, 20: \square, 40: \diamond$.

![img-2.jpeg](img-2.jpeg)

Figure 3: Empirical cumulative distributions (ECDF) of run lengths and speed-up ratios in 5-D (left) and 20D (right). Left sub-columns: ECDF of the number of function evaluations divided by dimension $D$ (FEvals/D) to reach a target value $f_{\text {opt }}+\Delta f$ with $\Delta f=10^{k}$, where $k \in\{1,-1,-4,-8\}$ is given by the first value in the legend, for CauchyEDA (solid) and Rosenbrock (dashed). Light beige lines show the ECDF of FEvals for target value $\Delta f=10^{-8}$ of algorithms benchmarked during BBOB-2009. Right sub-columns: ECDF of FEval ratios of CauchyEDA divided by Rosenbrock, all trial pairs for each function. Pairs where both trials failed are disregarded, pairs where one trial failed are visible in the limits being $>0$ or $<1$. The legends indicate the number of functions that were solved in at least one trial (CauchyEDA first).

![img-3.jpeg](img-3.jpeg)

Table 1: Expected running time (ERT in number of function evaluations) divided by the best ERT measured during BBOB-2009 (given in the respective first row) for different $\Delta f$ values for functions $f_{1}-f_{24}$. The median number of conducted function evaluations is additionally given in italics, if $\operatorname{ERT}\left(10^{-7}\right)=\infty$. \#succ is the number of trials that reached the final target $f_{\text {opt }}+10^{-8}$. 0: Ros is Rosenbrock and 1: Cau is CauchyEDA. Bold entries are statistically significantly better compared to the other algorithm, with $p=0.05$ or $p=10^{-k}$ where $k>1$ is the number following the $*$ symbol, with Bonferroni correction of 48.
