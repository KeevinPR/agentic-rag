# Modelling the Population Distribution in Multi-objective Optimization by Generative Topographic Mapping 

Aimin Zhou ${ }^{1}$, Qingfu Zhang ${ }^{1}$, Yaochu Jin ${ }^{2}$, Bernhard Sendhoff ${ }^{2}$, and Edward Tsang ${ }^{1}$<br>${ }^{1}$ Department of Computer Science, University of Essex, Colchester, CO4 3SQ, U.K.<br>${ }^{2}$ Honda Research Institute Europe, Carl-Legien-Str. 30, 63073, Offenbach, Germany


#### Abstract

Under mild conditions, the Pareto set of a continuous multi-objective optimization problem exhibits certain regularity. We have recently advocated taking into consideration such regularity in designing multi-objective evolutionary algorithms. Following our previous work on using Local Principal Component Analysis for capturing the regularity, this paper presents a new approach for acquiring and using the regularity of the Pareto set in evolutionary algorithms. The approach is based on the Generative Topographic Mapping and can be regarded as an Estimation of Distribution Algorithm. It builds models of the distribution of promising solutions based on regularity patterns extracted from the previous search, and samples new solutions from the models thus built. The proposed algorithm has been compared with two other state-of-the-art algorithms, NSGA-II and SPEA2 on a set of test problems.


## 1 Introduction

Multi-objective optimization problems (MOP) arise from many practical applications where several objectives have to be optimized. In this paper, we consider the following continuous MOP:

$$
\begin{array}{cc}
\operatorname{minimize} F(x)=\left(f_{1}(x), f_{2}(x), \ldots, f_{m}(x)\right)^{T} \\
\text { subject to } & x \in X
\end{array}
$$

where $X \in R^{n}$ is the decision (variable) space, $F: X \rightarrow R^{m}$ consists of $m$ continuous objective functions and $R^{m}$ is called the objective space. Very often, no point in $X$ minimizes all the objectives simultaneously. The best tradeoffs among these objectives can be defined in terms of Pareto optimality.

Let $u, v \in R^{m}, u$ is said to dominate $v$ if and only if $u_{i} \leq v_{i}$ for every $i \in$ $\{1,2, \ldots, m\}$ and $u_{j}<v_{j}$ for at least one index $j \in\{1,2, \ldots, m\}$. A point $x^{*} \in S$ is Pareto optimal to (1) if there is no point $x$ such that $F(x)$ dominates $F\left(x^{*}\right) . F\left(x^{*}\right)$ is then called a Pareto optimal (objective) vector. The set of all the Pareto optimal points is called the Pareto set (PS) and the set of all the Pareto optimal objective vectors is the Pareto front $(P F)$.

A number of evolutionary algorithms (EA) for dealing with multi-objective optimization problems, have been suggested over the past two decades [12]. These multiobjective evolutionary algorithms (MOEA) work with a population of candidate solutions and are able to produce a set of Pareto optimal vectors for approximating the PF. Most of these algorithms can be regarded as extensions of EAs for scalar optimization

problems. Selection, crossover and mutation are major operators in EAs. Conventional crossover and mutation operators can be used without any modification in MOEAs (although these operators may not lead to satisfactory performances in MOEAs), while the selection operators in scalar optimization EAs cannot be directly applied to MOPs. A major research issue in the area of MOEAs is the so-called fitness assignment [3], which assigns a relative fitness to each individual in a population for facilitating selection.

Estimation Distribution Algorithms (EDA) are a new class of EAs [4,5,6]. There is no traditional crossover or mutation in EDAs. Instead they explicitly extract global statistical information from the previous search and build a posterior probability distribution model of promising solutions, based on the extracted information. New trial solutions are sampled from the model thus built. Several EDAs for continuous MOPs have been proposed, among them are Mixture-based Iterated Density Estimation Evolutionary Algorithms (MIEDA) [7], EDAs based on Bayesian networks [8] and Voronoibased Estimation of Distribution Algorithm (VEDA) [9].

Under mild conditions, the PS (or PF) of a continuous MOP is a piecewise continuous $(m-1)$ dimensional manifold where $m$ is the number of the objectives. This property has been used in several mathematical programming methods for approximating the PF [10]. In fact, it has also been found that, for the most widely-used test problems of continuous multi-objective optimization in the evolutionary computations, their PS are $(m-1)$ dimensional linear or piecewise linear manifolds [11,12]. This regularity has been ignored in most current MOEAs.

Recently, we suggested that such regularity should be used in MOEAs for improving the algorithms' performances. We have proposed three EDAs [13,14,15] which employ Local Principal Component Analysis algorithms [16] for capturing and modeling the regularity of the Pareto set in a continuous MOP. The experimental results are very encouraging, the algorithms outperform NSGA-II [17] and SPEA2 [3] on several test problems with high interactions among the decision variables. Bueche et al [18] also attempted to use self-organizing mapping to learn the shape of the Pareto set of a MOP, although they have not explicitly discussed their method in the context of the regularity.

The Generative Topographic Mapping (GTM) [19] is a tool for extracting regularity from data. This paper continues our work on improving MOEAs by utilizing the regularity. We propose to use GTM in EDAs for extracting the regularity of the PS of (1). GTM can provide a probability model of promising solutions in terms of latent variables. Such a model is very easy for sampling new trial solutions.

The remainder of this paper is organized as follows: Section 2 gives a brief introduction to GTM. Section 3 presents the details of the model building and sampling techniques. The framework of the proposed algorithm is given in Section 4. Section 5 compares our proposed algorithm with NSGA-II and SPEA2 on a set of test problems. The final section provides concluding remarks.

# 2 The Generative Topographic Mapping 

GTM can discover some underlying regularity of a set of unlabeled data in a high dimensional space. It considers a nonlinear transformation mapping from a latent-variable space with lower dimensionality $L$ to the data space:

$$
x=y(v, W)=W \phi(v)
$$

where $x$ is a point in the data space, $v$ is the latent variable. $W$ is a parameter matrix and $\phi(v)$ is a vector of prefixed basis functions.

GTM models the distribution of data $x$, for given value of $W$ and $v$, to be a radiallysymmetric Gaussian centered on $y(v, W)$ with variance $\beta^{-1}$ :

$$
p(x \mid v, W, \beta)=\left(\frac{\beta}{2 \pi}\right)^{-n / 2} \exp \left\{-\frac{\beta}{2}\left\|W \phi(v)-x\right\|^{2}\right\}
$$

Therefore, $x=W \phi(v)$ can be envisaged as a central $L$-D manifold of the data, as illustrated in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Generative Topographic Mapping from 1-D latent space (left) to data space (right)

Given a number of points $x^{1}, x^{2}, \ldots, x^{N}$ in the data space, GTM estimates the values of $W$ and $\beta$ by maximizing the following log likelihood:

$$
L(W, \beta)=\ln \prod_{i=1}^{N} \int p\left(x^{i} \mid v, W, \beta\right) p(v) d v
$$

where $p(v)$ is the distribution of $v$. In our experiments, we use the GTM code developed by NCRG group at Aston University ${ }^{1}$. The details of GTM can be found in [19].

# 3 Model Building Based on GTM 

### 3.1 Basic Idea

The population in a MOEA for (1) will hopefully approximate to the PS and be uniformly distributed around the PS as the search goes on. Therefore, we can envisage the solutions in the population as independent observations of a random vector whose center is an approximation of the PS of (1). Since the PS is a piecewise continuous $(m-1)$

[^0]
[^0]:    ${ }^{1}$ The source codes are from http://www.ncrg.aston.ac.uk/GTM

dimensional manifold, a promising solution $x$ can be regarded as an observation of the following $n$-D random vector:

$$
\xi=\xi_{1}+\xi_{2}
$$

where $\xi_{1}$ is uniformly distributed along a $(m-1)$ dimensional manifold $\Phi . \xi_{2}$ is a random noise vector. $\Phi$ is called the central manifold of $\xi$ in this paper. For simplicity, we assume that $\xi_{1}$ and $\xi_{2}$ are independent of each other.

Under the above assumption, the modeling of promising solutions consists of two tasks: the modeling of the central manifold $\Phi$ and noise $\xi_{2}$.

# 3.2 Modeling and Sampling 

Given a population, which is a data set in $R^{n}$, we apply the GTM with $(m-1)$ latent variables to it (where $m$ is the number of objectives) and obtain the values of $W$ and $\beta$. In GTM training procedure, we set the range of the latent variable $v=\left(v_{1}, \ldots, v_{m-1}\right)$ as:

$$
-1 \leq v_{i} \leq 1 \quad i=1,2, \ldots, m-1
$$

Since the population often can not cover the whole PS thus the central manifold found can only approximate part of the PS. To overcome this problem and explore more ranges, in [13], [14] and [15], the search range is extended along the center manifold when we do sampling. In this paper, this idea is implemented by extending the range of the latent variables by $20 \%$.

Sampling a new point $x$ from the model built by the GTM is quite straightforward. We can do it in the following way:

Step 1: Uniformly and randomly select a $v$ from $[-1.1,1.1]^{m-1}$. Set $x^{1}=y(v, W)$.
Step 2: Sample $x^{2}$ from $N\left(0, \frac{1}{\beta} I\right)$.
Step 3: Set $x=x^{1}+x^{2}$.
where $m$ is the objective number, $I$ is a $n \times n$ identity matrix and $n$ is the variable dimension.

## 4 Algorithm Framework

Our proposed modeling and sampling approach can be adopted as operators for producing new solutions in most current MOEAs. In this paper, we use the following algorithm framework:

Step 0 Initialization: Randomly generate a population $P$ of $N$ solutions, $N$ is the population size.

## Step 1 Reproduction:

Step 1.1 Modeling: Build a probability model based on statistical information extracted from $P$;
Step 1.2 Sampling: Sample $N$ new solutions from the model and store them in $Q$.

Step 2 Selection: Select $N$ solutions from $P \cup Q$. Let these selected solutions to replace all the solutions in $P$.
Step 3 Stopping Condition: If the stopping condition is met, stop; otherwise, go to Step 1.

In our implementation, we use the selection scheme of NSGA-II in Step 2. We call our algorithm the model-based evolutionary algorithm with GTM (MEA/GTM).

# 5 Experimental Results 

We use five test problems shown in Table 1 in our simulation studies.

Table 1. Test problems
$Z D T 1.2, Z D T 2.2$ and $D T L Z 2.2^{2}$ are a respective modified version of $Z D T 1$ [1], ZDT2 [1] and DTLZ2 [21]. In their original versions, the Pareto set is parallel to a coordinate axis which makes the problems easy to tackle.

We compared the performances of MEA/GTM, NSGA-II ${ }^{3}$ and SPEA2 ${ }^{4}$ on the test problems in Table 1. The parameter setting of these algorithms are as follows: The

[^0]
[^0]:    ${ }^{2}$ ZDT 1.2, ZDT 2.2 and DTLZ2.2 are provided by Hui Li.
    ${ }^{3}$ The source codes are from http://www.iitk.ac.in/kangal/codes.shtml
    ${ }^{4}$ The source codes are from http://www.tik.ee.ethz.ch/pisa

population size for all the algorithms is set to 100 for 2-objective test instances and 200 for the 3-objective test instances. To have a fair comparison, the other parameters in NSGA-II and SPEA2 are set as in the default setting in their source codes. In GTM, the number of training steps is 15 , the latent points number is $1 \times 25$ for 2-objective test instances and $5 \times 5$ in case of 3 objective, the basis function number is 2 for 2objective problems and $2 \times 2$ in case of 3-objective and other parameters take their default values in their source codes. All the algorithms stops after 200 generations. We run each algorithm for each test instances 20 times.

To measure the performances of the algorithms, we use $\Upsilon$ [17] metric to measure the convergence of a population to the $P F$, and $\Delta$ [17] metric to measure the diversity of a population.
$\Upsilon[17]$ metric is defined as:

$$
\Upsilon\left(S, S^{*}\right)=\frac{1}{|S|} \sum_{x \in S} d\left(x, S^{*}\right)
$$

where

$$
d\left(x, S^{*}\right)=\min _{y \in S^{*}}\|F(x)-F(y)\|^{2}
$$

$S$ is an obtained non-dominated set by an algorithm, $S^{*}$ is a set which is uniformly distributed in Pareto Front.
$\Delta[17]^{5}$ metric is defined as:

$$
\Delta\left(S, S^{*}\right)=\frac{\sum_{i=1}^{m} d\left(e_{i}, S\right)+\sum_{x \in S}|d(x, S)-\bar{d}|}{\sum_{i=1}^{m} d\left(e_{i}, S\right)+|S| \bar{d}}
$$

where $\left\{e_{1}, \ldots, e_{m}\right\}$ are $m$ extreme solutions in $S^{*}$ and

$$
\begin{gathered}
d(x, S)=\min _{y \in S, y \neq x}| | F(x)-F(y) \mid \|^{2} \\
\bar{d}=\frac{1}{|S|} \sum_{y \in S} d(y, S)
\end{gathered}
$$

It should be noticed that $d(x, S)$ measures the distance between point $x$ and its nearest neighbor which is different from the original definition.

Table 2 gives the means and standard derivations of $\Upsilon$ and $\Delta$ on 20 runs at different stages, generation $40,80,120,160$ and 200, of the algorithms for each problem. Fig. 2 shows the distributions of nondominated solutions generated in 20 runs in the objective space for each algorithm for each problem.

From the values of $\Delta$ in Table 2 it is clear that MEA/GTM outperforms NSGA-II and SPEA2 in terms of the diversity of the nondominated solutions found. Fig. 2 also supports this claim. For all five test problems, MEA/GTM can cover the whole Pareto Fronts, while NSGA-II can only cover the Pareto Fronts of OKA4 and DTLZ2.2 and

[^0]
[^0]:    ${ }^{5}$ We notice this metric is only fit in the case of small $m$.

![img-3.jpeg](img-3.jpeg)
(c) ZDT1.2
![img-3.jpeg](img-3.jpeg)
(d) ZDT2.2
![img-3.jpeg](img-3.jpeg)
(e) DTLZ2.2

Fig. 2. Pareto fronts produced by MEA/GTM, NSGA-II and SPEA2

Table 2. Experimental results
SPEA2 can not cover any of the Pareto Fronts. The reason may be: (1) MEA/GTM can cover the whole Pareto Fronts by extension and (2) MEA/GTM uniformly samples new solutions from the model.

In terms of $\gamma$ metric, MEA/GTM performances much better than NSGA-II and SPEA2 on FON2 and DTLZ2.2. $\gamma$ values in MEA/GTM is slightly higher than in SPEA2 on ZDT1.2 and ZDT2.2, it does not imply that MEA/GTM is worse. Since NSGA-II and SPEA2, as shown in Fig.2, cannot cover the whole Pareto Front as MEA/ GTM does. Only on OKA4, MEA/GTM performs worse than NSGA-II and SPEA2. From Fig.2, however, EA/GTM can also approximate the Pareto Front very well.

These algorithms have been run in a desktop computer (Pentium(R) 43.40 GHz CPU, 1.00 GB of RAM). The average run time (in seconds) are listed in Table 3. Although

Table 3. Average run time(in seconds)
MEA/GTM needs more time to optimize each test problem than NSGA-II and SPEA2, it is still affordable especially when the fitness evaluation is much time consuming.

# 6 Conclusions 

Incorporating problem-specific knowledge into evolutionary algorithms is a basic strategy for enhancing their performances [22]. The Pareto set of a continuous MOP is usually a piecewise continuous $(m-1)$-D manifold. Most current MOEAs ignore this regularity. Our recent work has showed that such regularity could be beneficial for modeling the population distribution in estimation of distribution algorithms for continuous multi-objective optimization. This paper demonstrated that GTM can be used for capturing and modeling the regularity and proposed an estimation of distribution algorithms with GTM for multi-objective optimization. The preliminary experiments show that our proposed method outperforms NSGA-II and SPEA2.

Our previous work in [13], [14] and [15] and this paper are on the design of EDAs by making the use of the regularity property. In the future, we plan to study how to incorporate such regularity and other properties of MOPs into other evolutionary algorithms.
