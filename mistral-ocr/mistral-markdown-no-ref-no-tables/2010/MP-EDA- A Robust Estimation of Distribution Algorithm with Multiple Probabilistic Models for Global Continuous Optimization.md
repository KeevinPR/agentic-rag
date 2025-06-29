# MP-EDA: A Robust Estimation of Distribution Algorithm with Multiple Probabilistic Models for Global Continuous Optimization* 

Jing-hui Zhong ${ }^{1}$, Jun Zhang ${ }^{1, * *}$, and Zhun Fan ${ }^{2}$<br>${ }^{1}$ Dept. of Computer Science, SUN yat-sen University<br>Key Laboratory of Digital Life (Sun Yat-Sen University), Ministry of Education<br>Key Laboratory of Software Technology, Education Department of Guangdong<br>Province, P.R. China<br>junzhang@ieee.org<br>${ }^{2}$ Denmark Technical University


#### Abstract

Extending Estimation of distribution algorithms (EDAs) to the continuous field is a promising and challenging task. With a single probabilistic model, most existing continuous EDAs usually suffer from the local stagnation or a low convergence speed. This paper presents an enhanced continuous EDA with multiple probabilistic models (MP-EDA). In the MP-EDA, the population is divided into two subpopulations. The one involved by histogram model is used to roughly capture the global optima, whereas the other involved by Gaussian model is aimed at finding highly accurate solutions. During the evolution, a migration operation is periodically carried out to exchange some best individuals of the two subpopulations. Besides, the MP-EDA adaptively adjusts the offspring size of each subpopulation to improve the searching efficiency. The effectiveness of the MP-EDA is investigated by testing ten benchmark functions. Compared with several state-of-the-art evolutionary computations, the proposed algorithm can obtain better results in most test cases.


Keywords: Estimation of Distribution Algorithm, Evolutionary Computation, Histogram, Multivariate Gaussian Distribution, Global Optimization.

## 1 Introduction

The estimation of distribution algorithms (EDAs) are a new class of evolutionary computation algorithms [1] [2]. They generate new individuals by sampling a probabilistic model, which is estimated based on the current promising solutions. As the probabilistic model can capture promising areas in a statistically sound manner and can explicitly express the interactions among variables, EDAs usually can outperform traditional EAs on a number of complex problems .

[^0]
[^0]:    * This work was supported in part by the National Natural Science Foundation of China No. U0835002 and No. 61070004, by the National High-Technology Research and Development Program ("863" Program) of China No. 2009AA01Z208.
    ** Corresponding author.

The EDAs are first proposed to solve discrete problems with binary representation. For the last few years, various efforts have been made on extending them to the continuous optimization [3] - [11]. Most existing continuous EDAs use the Gaussian model or the histogram model to estimate the distribution of promising areas. The marginal Gaussian probabilistic model was used to guide the search in early continuous EDAs, such as the PBILc [3] and the UMDAc [4]. Lately, the multivariate Gaussian models also appeared in continuous EDAs [5] [6]. EDAs with a single Gaussian model are excellent in finding the global optima for unimodal optimization. However, for multimodal problems, they usually suffer from a slow convergence speed or even a local stagnation. Though clustering techniques have been utilized to address some of these issues [7], more efficient methods are greatly desirable.

Meanwhile, the histogram has multimodal density and can capture multiple local optima at the same time. Hence the histogram-based EDAs (HEDAs) are less likely to get trapped in local optima [8]. However, the HEDAs usually need a heavy computational cost to search for a highly accurate solution. To tackle this problem, the local search techniques [9], the shrink strategy [10], and the sub-divided method [11], have been proposed in recent few years. Nevertheless, since the histogram ignores interactions among variables, the HEDAs are not efficient enough to solve problems containing variable dependency.

In this paper, we present an enhanced EDA with multiple probabilistic models (named MP-EDA) for the global continuous optimization. The proposed MP-EDA has made two major improvements as below. First, the robustness to find a highly accurate solution is guaranteed by adopting two different types of probabilistic models: the multivariate Gaussian model and the fixed-height histogram (FHH) model. Second, the efficiency of the search is improved by utilizing an adaptive control strategy. In the MP-EDA, the population is initially divided into two subpopulations, with each involved by a probabilistic model. The one involved by the FHH is used to roughly capture the global optima, and the other involved by the multivariate Gaussian model is aimed at finding highly accurate solutions. During the evolution, a migration operation is carried out periodically to exchange some best individuals between the two subpopulations. By sharing information of better individuals, both subpopulations can converge faster. Besides, in order to improve the search efficiency, an adaptive strategy is used to adjust the offspring sizes of the two subpopulations. The performance of a probabilistic model is measured by the average fitness of new individuals generated by it during recent generations. The better probabilistic model is allowed to generate more offspring individuals, and vice versa. We investigate the effectiveness of the proposed MP-EDA by solving ten test functions with different characteristics. Several state-of-the-art EAs (i.e PLSO [12], DE [13], FEP [14] and CMA-ES [15]) are used for the comparison. Experimental results show that the proposed MP-EDA can achieve better results in most test cases.

The rest of the paper is organized as follows. Section 2 briefly describes the EDAs' general framework and two classical continuous EDAs. Section 3 illustrates the detailed implementations of the MP-EDA. The experimental studies on the MP-EDA are presented in Section 4. At last, Section 5 draws the conclusions.

# 2 Estimation of Distribution Algorithms 

### 2.1 Framework of EDAs

The general framework of EDAs is similar to that of the GA. However, there is neither crossover nor mutation in EDAs. Instead, they use a probabilistic model to generate new individuals. Specifically, the common outline of EDAs consists of the following four steps.

Step 1: Initialize the algorithm parameters and the initial population.
Step 2: Select a certain number of excellent individuals. There are several selection strategies, such as the truncation selection and the tournament selection.

Step 3: Construct probabilistic model by analyzing information of the selected individuals.

Step 4: Create new population by sampling new individuals from the constructed probabilistic model.

There is a repetition from Step2 to Step4 until the algorithm meets the termination condition.

### 2.2 Multivariate Gaussian Model

The multivariate Gaussian model is most commonly used in continuous EDAs. It characterizes the distribution of data points by two parameters $\mu$ and $\sum$. The former gives the mean vector of data points, while the latter describes the covariance information. In particular, given a set of data points $\boldsymbol{X}=\left\{x_{1}, x_{2}, \ldots, x_{\mathrm{Z}}\right\}$, the multivariate Gaussian model of $\boldsymbol{X}$ can be expressed by

$$
N(\mu, \Sigma)=\frac{1}{\sqrt{2 \pi \Sigma}} \cdot \exp \left(-\frac{1}{2} \cdot(x-\mu) \cdot \sum^{-1} \cdot(x-\mu)\right)
$$

where $\mu$ is the mean vector of $\boldsymbol{X}$, and $\sum$ is the covariance matrix of $\boldsymbol{X}$.
The multivariate Gaussian model is able to capture the interaction between variables, owing to the covariance matrix in the density function. However, it is not effective to estimate the distribution of multimodal data points, due to its unimodal density.

### 2.3 Histogram Model

There are usually two types of histograms, namely the fixed-width histogram (FWH) and the FHH. The FWH consists of bins with the same width, whereas the FHH contains bins with the same height. In this paper, we choose the FHH as one probabilistic model of the proposed method, because it has shown to perform better than the FWH. Given a set of data points $\boldsymbol{X}=\left\{x_{1}, x_{2}, \ldots, x_{\mathrm{Z}}\right\}$ within an interval $\Omega=\left[x_{\min }, x_{\max }\right\}$. The FHH of $\boldsymbol{X}$ consists of $n$ bins, with each bin $\boldsymbol{B}_{i}(i=1,2, \ldots, n)$ containing the same number of data points. Hypothesizing that the data points in each bin are uniformly

distributed, the estimated density $\hat{f}_{H}(x)$ of the underlying probability density at any point $x$ can be computed by

$$
\hat{f}_{H}(x)=\frac{1}{w_{\mathrm{k}} \cdot n}
$$

where $w_{\mathrm{k}}$ is the width of the bin $\boldsymbol{B}_{\mathrm{k}}$ that contains $x$. According to the definition of the FHH, bins in the dense regions would have a narrower width than those in the sparse regions. As the population of an evolutionary algorithm evolves, individuals will gradually gather around promising areas. By giving more bins to these regions, the FHH is able to capture multiple peaks at the same time. Nevertheless, one drawback of the FHH based EDA is that it may get stuck when the population converges. It this case, a heavy computational cost is usually required to sample a highly accurate solution.

# 3 MP-EDA for Multimodal Continous Optimization 

### 3.1 Algorithm Framework

There are two subpopulations $\left(P O P_{\mathrm{thh}}\right.$ and $\left.P O P_{\mathrm{gm}}\right)$ involved by two probabilistic models in the MP-EDA. The $P O P_{\mathrm{thh}}$ is involved by the FHH model, whereas the $P O P_{\mathrm{gm}}$ is involved by the Gaussian model. Specifically, the framework of the proposed MP-EDA contains following six steps.

## 1) Step 1 - Initialization

This step initializes parameters of the algorithm, such as the size of the population $N$, the number of excellent individuals $S$, the migration cycle $T$ and the number of bins $n$. Besides, new individuals of $P O P_{\mathrm{thh}}$ and $P O P_{\mathrm{gm}}$ are randomly generated in the search space, with their offspring sizes respectively set as $N_{\mathrm{thh}}=N$ and $N_{\mathrm{gm}}=N$.

## 2) Step 2 - Constructing probabilistic models

This step aims at constructing two different probabilistic models for the two subpopulations in parallel. For the $P O P_{\mathrm{thh}}, S$ best individuals are firstly selected. Then the marginal histogram for all variables is updated. Let $X=\left\{x_{0}, x_{1}, \ldots, x_{\mathrm{S}}\right\}$ with $x_{0} \leq x_{1} \leq \ldots \leq x_{\mathrm{S}}$, be the $i$-th variable values of these selected individuals, then the lower bound and the upper bound of each bins is updated by

$$
\begin{aligned}
& l_{j, i}=\left\{\begin{array}{l}
\text { lower bound of the } i \text {-th variable, if } j=1 \\
\left(x_{\lfloor(j-1) \cdot \Delta x\rfloor}+x_{\lfloor(j-1) \cdot \Delta x\rfloor+1}\right) / 2, \text { otherwise }
\end{array}\right. \\
& u_{j, i}=\left\{\begin{array}{l}
\text { upper bound of the } i \text {-th variable, if } j=n \\
l_{j+1, i}, \text { otherwise }
\end{array}\right.
\end{aligned}
$$

where $\Delta x=S / n$ is the average number of data points in each bin.
As for the multivariate Gaussian model, the constructing process aims to update values of two parameters: the mean $\mu$ and the covariance matrix $\sum$. Firstly, S promising

individuals are selected in $P O P_{\mathrm{gm}}$, and then the mean and the covariance of these $S$ individuals are computed and set as the values of $\mu$ and $\sum$.

# 3) Step 3 - Sampling new population 

The sampling process of the FHH consists of two sub-steps. Firstly, a bin is randomly selected according to the constructed marginal histogram. Then a random value uniformly distributed in the interval of the selected bin is generated.

As for the multivariate Gaussian model, the sampling process contains three substeps.

Sub-step1: Use the Cholesky decomposition to generate a lower triangular matrix S, with

$$
\sum=S \cdot S^{T}
$$

Sub-step2: obtain a 1-by-D matrix Z with random elements sampled from a standard Normal distribution $\mathrm{N}(0,1)$.
Sub-step3: generate a individual $P$ by

$$
P=\mu+S \cdot Z
$$

In order to maintain higher population diversity, a scale parameter $\delta>1$ is suggested to add in (6) [16] and expressed as

$$
P=\mu+\delta \cdot S \cdot Z
$$

Note that the parameter $\delta$ should be set appropriate, for a trade-off between the diversity and the convergence of the population.

## 4) Step 4 -Evaluation and Replacement

This step aims to evaluate the fitness values of all new individuals and replace some worst individuals of the current population by better new individuals. For example, let $\boldsymbol{C}=\left\{C_{1}, C_{1}, \ldots, C_{N}\right\}$ be the current subpopulation $P O P_{\mathrm{fhh}}, \boldsymbol{C}^{*}=\left\{C^{*}{ }_{1}, C^{*}{ }_{2}, \ldots, C^{*}{ }_{N}\right\}$ be the newly generated individuals by the FHH and $\boldsymbol{C}^{\#}=\boldsymbol{C} \cup \boldsymbol{C}^{*}$. Then the best $N$ individuals in $\boldsymbol{C}^{\#}$ are selected as the new $P O P_{\mathrm{fhh}}$. The similar process can be done to generate the new $P O P_{\mathrm{gm}}$.

## 5) Step 5 -Migration

During the evolution, a migration operation is carried out every $T$ generations. In the migration, the best $M$ individuals in one subpopulation are migrated to the other. By sharing the best individuals of two subpopulations, the algorithm can utilize the advantages of both probabilistic models, which makes the algorithm less likely to be trapped into local optima and more efficient to find highly accurate solutions.

## 6) Step 6 - Adaptive control operation

This step aims to adjust the size of new offspring for each subpopulation, so as to save the computational cost. The key idea is to make the better probabilistic model generate more new individuals in each generation. Specifically, $F_{\mathrm{fhh}}$ and $F_{\mathrm{gm}}$ are supposed to be the average fitness of new individuals generated by the FHH and the GM respectively during the recent $T$ generations. If $F_{\mathrm{fhh}}$ is better than $F_{\mathrm{gm}}$, the value of $N_{\mathrm{fhh}}$ would be enlarged by a small step $\Delta$, whereas the value of $N_{\mathrm{gm}}$ would be reduced

by $\Delta$. Otherwise, the reverse operation can be done. The maximum and the minimum of $N_{\mathrm{thh}}$ and $N_{\mathrm{gm}}$ are both set as $P_{\min }$ and $P_{\max }$.

There is a repetition from Step2 to Step6 and the evolution processes iteratively until reaching the maximum number of evaluations.

# 4 Experiments and Comparisons 

### 4.1 Test Functions and Parameter Settings

Ten benchmark functions are contained in the experimental study, as listed in Table 1. These functions are chosen in the literature [17] and [18]. Parameter settings of all comparison algorithms are listed in Table 2. The parameter settings of the DE, the CLPSO and the CMA-ES are set as those in the reference papers. The dimension of all test functions is 30 and the maximum evaluation number for each function is $3 \times 10^{5}$. In order to make fair comparisons, 30 independent runs are performed on each algorithm.

Table 1. Test functions

Table 2. Parameter Settings

Table 3. Experimental Results. ' $a$ ' stands for the average best values, ' $s$ ' stands for the standard deviations and ' $r$ ' stands for the performance ranking of the corresponding algorithm.

# 4.2 Experimental Results 

The comparison results are summarized in Table 3. Firstly, we investigate the performance of the FHH-EDA, GM-EDA and the MP-EDA. Results of f1 show that, among these three algorithms, the MP-EDA performs the best, while the FHH-EDA performs the worst. The GM-EDA can obtain very highly accurate solutions, but it gets stuck near the global optima. This is because the eigenvectors of the covariate matrix in the GM-EDA has dropped to zero when the mean vector was still a bit distant from the global optimum. However, the MP-EDA can overcome this drawback, owing to the diversity provided by the histogram. Results of f2 and f3 indicate that, the FHH-EDA is not suitable to solve these kinds of problems, since it contains no mechanism to deal with variable interactions. However, the GM-EDA is very effective to solve these problems, and the proposed MP-EDA can also give competitive performance. As for multimodal functions, the MP-EDA performs much better than the GM-EDA and the FHH-EDA in all test cases except for the shift rosenbrock function. It can be observed that the Gaussian-based EDA can find satisfying solutions for multimodal functions with a big-valley structure (such as f8 and f9), but it performs
![img-0.jpeg](img-0.jpeg)

Fig. 1. Convergence graphs of the MP-EDA

very badly for those with local optima scattering in the search space. Meanwhile, the FHH-EDA can only find roughly accurate solutions for separable-multimodal functions (such as f5 and f6), but it performs badly for those containing variable interactions (such as f4). By combining two different probabilistic models, the MP-EDA performs better and more stable.

Results in table 3 indicate that the proposed MP-EDA performs the best in six test functions, and it can also give competitive performance on other test functions. According to the average rank value, the MP-EDA performs averagely much better than the other comparison EAs.

The convergence graphs of the MP-EDA and the comparison algorithms are shown in Fig. 1. It can be observed that the proposed algorithm can not only search a highly accurate solution, but also has a very fast convergence speed. Besides, the proposed MP-EDA can give good performance on both unimodal functions and multimodal functions.

# 5 Conclusions 

This paper has proposed an enhanced EDA with multiple probabilistic models for the global continuous optimization. The proposed MP-EDA adopts a histogram and a multivariate Gaussian model to involve two subpopulations. During the evolution, a migration strategy is used to exchange some best individuals of the two subpopulations. Besides, the offspring size of each subpopulation is adaptively adjusted to reduce the computational cost. The effectiveness of the proposed MP-EDA has been investigated by testing ten benchmark functions. Compared with several state-of-theart evolutionary algorithms, the proposed MP-EDA can obtain better results in most test cases.

This study has shown that, EDAs with multiple probabilistic models usually can work more effectively and efficiently than those with a single probabilistic model. As for future work, we will further extent the framework by hybridizing more probabilistic models. Besides, applying the proposed algorithm framework to solve real application is another promising research topic.
