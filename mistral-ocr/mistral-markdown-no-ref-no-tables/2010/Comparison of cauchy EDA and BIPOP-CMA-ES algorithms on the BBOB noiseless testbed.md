# Comparison of Cauchy EDA and BIPOP-CMA-ES Algorithms on the BBOB Noiseless Testbed 

Petr Pošík<br>Czech Technical University in Prague<br>Faculty of Electrical Engineering, Department of Cybernetics<br>Technická 2, 16627 Prague 6, Czech Republic<br>posik@labe.felk.cvut.cz


#### Abstract

Estimation-of-distribution algorithm using Cauchy sampling distribution is compared with the bi-population CMA evolutionary strategy which was one of the best contenders in the black-box optimization benchmarking workshop in 2009. The results clearly indicate that the CMA evolutionary strategy is in all respects a better optimization algorithm than the Cauchy estimation-of-distribution algorithm. This paper compares both algorithms in more detail and adds to the understanding of their key features and differences.


## Categories and Subject Descriptors

G.1.6 [Numerical Analysis]: Optimization—global optimization, unconstrained optimization; F.2.1 [Analysis of Algorithms and Problem Complexity]: Numerical Algorithms and Problems

## General Terms

Algorithms

## Keywords

Benchmarking, Black-box optimization, Estimation-of-distribution algorithm, Cauchy distribution, Evolutionary strategy, Covariance matrix adaptation

## 1. INTRODUCTION

The 2010 issue of the black-box optimization benchmarking methodology (BBOB) [3] allows for a detailed comparison of 2 algorithms on the BBOB functions testbed. In this article, two algorithms benchmarked during the BBOB 2009 workshop are further compared. Data for both algorithms were taken from 2009 benchmarking, but the comparison is made using the new BBOB 2010 post-processing scripts and templates. Both algorithms fall into the class of evolutionary optimization algorithms and both algorithms use unimodal

[^0]distribution as a mean for generating new offspring; however, there are several important differences between them and this paper clearly shows which algorithm is better. The two algorithms selected for the comparison are:

- The bi-population variant of the evolutionary strategy with covariance matrix adaptation (BIPOP-CMA-ES) [2] which belongs to the best algorithms of the BBOB 2009 comparison in terms of speed and success ratio, and thus was selected as the reference algorithm.
- The estimation-of-distribution algorithm (EDA) with Cauchy sampling distribution (Cauchy EDA) [5]. In BBOB 2010, further comparisons of the Cauchy EDA with other algorithms (G3PCX [6] and Rosenbrock's algorithm [7]) are planned, and this article anchors the relative performances of the respective algorithm pairs to one of the best algorithms in BBOB 2009.
In the next section, both algorithms are shortly described and their differences are emphasized. Sec. 3 contains all the results used to compare the algorithms and their discussions. After the presentation of the time demands of both algorithms in Sec. 4, Sec. 5 concludes the paper.


## 2. ALGORITHM PRESENTATION

The exact descriptions of the algorithms along with the parameter settings can be found in [5] and [2], respectively. Apart of the unimodality of the sampling distribution, the algorithms differ foremost in the following aspects:

- The probabilistic model used in BIPOP-CMA-ES is Gaussian, while the EDA uses Cauchy distribution.
- In BIPOP-CMA-ES, each generation, the Gaussian distribution is updated (the recent model parameters explicitly take part in the process of creating new values of model parameters), while in Cauchy EDA all the distribution parameters are computed from scratch (and thus a larger population is needed).
- The restart strategy of BIPOP-CMA-ES allows the algorithm to use different population sizes for each restart. In Cauchy EDA, the population size depends only on the dimensionality of the problem being solved. Very often, the BIPOP-CMA-ES population size is much smaller when compared to the population size of Cauchy EDA, which allows the BIPOP-CMA-ES algorithm to converge faster and to be restarted more often.

For both algorithms, the crafting effort $\mathrm{CrE}=0$.


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. To copy otherwise, to republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee.
    GECCO'10, July 7-11, 2010, Portland, Oregon, USA.
    Copyright 2010 ACM 978-1-4503-0073-5/10/07 ...\$10.00.

Table 2: The average time demands per function evaluation (in microseconds) of the two compared algorithms.

## 3. RESULTS

Results from experiments according to [3] on the benchmark functions given in $[1,4]$ are presented in Figures 1, 2 and 3 and in Table 1. The expected running time (ERT), used in the figures and table, depends on a given target function value, $f_{\mathrm{t}}=f_{\text {opt }}+\Delta f$, and is computed over all relevant trials as the number of function evaluations executed during each trial while the best function value did not reach $f_{\mathrm{t}}$, summed over all trials and divided by the number of trials that actually reached $f_{\mathrm{t}}[3,8]$. Statistical significance is tested with the rank-sum test for a given target $\Delta f_{\mathrm{t}}\left(10^{-8}\right.$ in Figure 1) using, for each trial, either the number of needed function evaluations to reach $\Delta f_{\mathrm{t}}$ (inverted and multiplied by -1 ), or, if the target was not reached, the best $\Delta f$-value achieved, measured only up to the smallest number of overall function evaluations for any unsuccessful trial under consideration.

The most important observation that can be made from Figures 1, 2, and 3 and from Table 1 is that BIPOP-CMA$E S$ is simply more reliable (has higher success rates) and typically 1-2 orders of magnitude faster than Cauchy EDA! BIPOP-CMA-ES outperforms Cauchy EDA for all functions, (virtually) all dimensions and (virtually) all target levels. The few exceptions happen for low dimensional functions (2D or 3D) and for a very narrow range of target levels.

In Fig. 1, we can see rather regular behaviour of the ERT ratios for unimodal ${ }^{1}$ functions (1, 2, 5-14). The ERT ratio is often almost constant (between 1 and 100) for a broad range of the target levels.

For multimodal functions (3, 4, 15-24), the Cauchy EDA algorithm does not work well. The long running times allow for a limited number of restarts only, and it is able to solve only low-dimensional versions of some of the multimodal benchmark functions.

## 4. CPU TIMING EXPERIMENTS

The time requirements of both algorithms are taken from the respective articles, [2] and [5]. The multistart algorithm was run with the maximal number of evaluations set to $10^{5}$, the basic algorithm was restarted for at least 30 seconds. These experiments have been conducted with an Intel dual core T5600 processor with 1.8 GHz under Linux 2.6.27-11 using MATLAB R2008a for BIPOP-CMA-ES, and on Intel Core 2 CPU, T5600, 1.83 GHz, 1 GB RAM with Windows XP SP3 in MATLAB R2007b for Cauchy EDA. The comparison of the average time demands per function evaluation are shown in Table 2.

The differences in the average time needed for function evaluation are caused by the different population sizes. While BIPOP-CMA-ES often uses populations of a few (or a few

[^0]tens of) individuals, Cauchy EDA needs larger populations which means that the evaluation routine is called less often and can take advantage of the MATLAB matrix processing capabilities to a larger extent.

## 5. CONCLUSIONS

The results indicate that BIPOP-CMA-ES clearly dominates the Cauchy EDA algorithm regardless of the particular optimization conditions. The adaptation scheme used in CMA-ES needs lower population sizes, is thus faster, and allows for more algorithm restarts. For the functions in the testbed, it seems to be better to have fast local optimizer with the possibility to restart it often.

## Acknowledgements

The author is supported by the Grant Agency of the Czech Republic with the grant no. 102/08/P094 entitled "Machine learning methods for solution construction in evolutionary algorithms".
