# RM-MEDA: A Regularity Model-Based Multiobjective Estimation of Distribution Algorithm 

Qingfu Zhang, Senior Member, IEEE, Aimin Zhou, and Yaochu Jin, Senior Member, IEEE


#### Abstract

Under mild conditions, it can be induced from the Karush-Kuhn-Tucker condition that the Pareto set, in the decision space, of a continuous multiobjective optimization problem is a piecewise continuous ( $m-1$ )-D manifold, where $m$ is the number of objectives. Based on this regularity property, we propose a regularity model-based multiobjective estimation of distribution algorithm (RM-MEDA) for continuous multiobjective optimization problems with variable linkages. At each generation, the proposed algorithm models a promising area in the decision space by a probability distribution whose centroid is a ( $m-1$ )-D piecewise continuous manifold. The local principal component analysis algorithm is used for building such a model. New trial solutions are sampled from the model thus built. A nondominated sorting-based selection is used for choosing solutions for the next generation. Systematic experiments have shown that, overall, RM-MEDA outperforms three other state-of-the-art algorithms, namely, GDE3, PCX-NSGA-II, and MIDEA, on a set of test instances with variable linkages. We have demonstrated that, compared with GDE3, RM-MEDA is not sensitive to algorithmic parameters, and has good scalability to the number of decision variables in the case of nonlinear variable linkages. A few shortcomings of RM-MEDA have also been identified and discussed in this paper.


Index Terms—Estimation of distribution algorithm, local principal component analysis, multiobjective optimization, regularity, scalability, sensitivity, the Karush-Kuhn-Tucker condition, variable linkages.

## I. INTRODUCTION

MULTIOBJECTIVE OPTIMIZATION PROBLEMS (MOPs) arise in many engineering areas. Very often, the objectives in a MOP conflict with each other, and no single solution can optimize all the objectives at the same time. The Pareto set/front is the set of all the optimal tradeoffs in the decision/objective space. When the preference of a decision maker is unavailable or very difficult to specify mathematically as it is in many applications, the decision maker usually requires an approximation to the Pareto set and/or Pareto front for making their final choice. Such an approximation can be a finite set of Pareto optimal solutions or a mathematical approximation model of the Pareto set/front.

Since the publication of Schaffer's seminal work [1], a number of evolutionary algorithms (EAs) have been developed

[^0]for multiobjective optimization problems [2]-[5]. The major advantage of these multiobjective evolutionary algorithms (MOEAs) over other methods are that they work with a population of candidate solutions and thus can produce a set of Pareto optimal solutions to approximate the Pareto front and/or Pareto set in a single run. The current MOEA research mainly focuses on the following highly related issues.

- Fitness assignment and diversity maintenance: Like their counterparts for scalar optimization, most MOEAs employ a selection operator to direct its search into promising areas in the decision space. Since Pareto domination is not a complete ordering, conventional selection operators, which were originally developed for scalar objective optimization, cannot be directly applied to multiobjective optimization. Furthermore, the task of most MOEAs is to produce a set of solutions which are evenly distributed on the Pareto front. Thus, selection operators in MOEAs should not encourage the search to converge to a single point. Therefore, it is not a trivial job to assign a relative fitness value to each individual solution for reflecting its utility in selection in MOEAs. Fitness assignment has been subject to much research over the last two decades [6]-[8]. Some techniques such as fitness sharing and crowding have been frequently used within fitness assignment for maintaining the diversity of search [9]-[11]. Very recently, a method based on decomposition for fitness assignment and diversity maintenance has been proposed in [12].
- External population: It is usually very hard to balance diversity and convergence with a single online population in current MOEAs. The online population may be unable to store some representative solutions found during the search due to its limited size. To overcome this shortcoming, an external population (archive) is often used in MOEAs for recording nondominated solutions found during the search. Some effort has been made to study how to maintain and utilize such an external population [13], [14].
- Combination of MOEA and local search: Combinations of EAs and local search heuristics, often called memetic algorithms, have been shown to outperform traditional evolutionary algorithms in a wide variety of scalar objective optimization problems. A few multiobjective memetic algorithms (MOMAs) have been developed over the past decade [15]. MOMAs need to consider how to evaluate solution quality for their local search operators. In multiobjective genetic local search (MOGLS) [16], [17], a scalarizing function with random weights is used as its evaluation function in both its local search and selection.


[^0]:    Manuscript received July 27, 2006; revised November 2, 2006.
    Q. Zhang and A. Zhou are with Department of Computer Science, University of Essex, Wivenhoe Park, Colchester, CO4 3SQ, U.K. (e-mail: qzhang@essex.ac.uk; azhou@essex.ac.uk).
    Y. Jin is with Honda Research Institute Europe, 63073 Offenbach, Germany (e-mail: YaochuJin@honda-ri.de).

Memetic Pareto archived evolution strategy (M-PAES) evaluates solutions by using domination ranks [18]. Multiobjective evolutionary algorithm based on decomposition (MOEA/D) provides a general framework for using scalar optimization methods in multiobjective optimization [12].
Surprisingly, not much work has been done on how to generate new solutions in MOEAs. The implementations of most current MOEAs directly adopt traditional genetic recombination operators such as crossover and mutation. The characteristics of MOPs have not been well utilized in generating new solutions in current MOEAs. Very recently, Deb et al. have compared the performance of several recombination operators on some test problems with variable linkages [19]. Their experimental results suggest that variable linkages could cause difficulties for MOEAs and recombination operators are crucial to the performance of a MOEA.

It has been observed that under mild smoothness conditions, the Pareto set (in the decision space) of a continuous MOP is a piecewise continuous $(m-1)$-dimensional manifold, where $m$ is the number of the objectives. This observation has been used in several mathematical programming methods for approximating the Pareto front or Pareto set [20]-[22]. However, as suggested in [23], such regularity has not been exploited explicitly by most current MOEAs except for those combining local search that take advantage of the regularity implicitly, such as the dynamic weighted aggregation method [24]. The work in this paper will show that reproduction of new trial solutions based on this regularity property can effectively cope with the variable linkages in continuous MOPs.

Estimation of distribution algorithms (EDAs) are a new computing paradigm in evolutionary computation [25]. There is no crossover or mutation in EDAs. Instead, they explicitly extract globally statistical information from the selected solutions and build a posterior probability distribution model of promising solutions, based on the extracted information. New solutions are sampled from the model thus built and, fully or in part, replace the old population. Several EDAs have been developed for continuous MOPs [26]-[28]. However, these EDAs do not take the regularity into consideration in building probability models. Since probability modeling techniques under regularity have been widely investigated in the area of statistical learning [29], [30], it is suitable to take advantage of the regularity in the design of EDAs for a continuous MOP.

As one of the first attempts to capture and utilize the regularity of the Pareto set in the decision space, we have recently proposed using local principal component analysis for extracting regularity patterns of the Pareto set from the previous search. We have studied two naive hybrid MOEAs in which some trial solutions are generated by traditional genetic operators and others by sampling from probability models built based on regularity patterns [31], [32]. Our preliminary experimental results are very encouraging. This paper conducts a further and thorough investigation along this line. In comparison with our work presented in [31] and [32], the main new contributions of this paper include the following.

- Based on the regularity property of continuous MOPs, an estimation of distribution algorithm for continuous multiobjective optimization has been developed. Unlike our pre-
vious algorithms, it does not use crossover or mutation operators for producing new offspring. Besides, the parameter estimation for model building in this paper is more statistically sound and yet simpler than that used in [31] and [32]. Our experimental studies have shown that the algorithm presented in this paper performs similarly to its predecessors. ${ }^{1}$
- Systematic experiments have been conducted to compare the proposed algorithm with three other state-of-the art algorithms on a set of biobjective or triobjective test instances with linear or nonlinear variable linkages. Only the original NSGA-II with SBX [6] was compared on a few test instances in [31] and [32].
- The sensitivity to algorithmic parameters, the scalability to the number of decision variables and the CPU-time costs of the proposed algorithm and generalized differential evolution (GDE3) [33] have been experimentally investigated.
The rest of this paper is organized as follows. Section II introduces continuous multiobjective optimization problems, Pareto optimality, and the regularity property induced from the Karush-Kuhn-Tucker condition. Section III presents the motivation and the details of the proposed algorithm. Section IV briefly describes the three other algorithms used in comparison. Section V presents and analyzes the experimental results. Section VI experimentally studies the sensitivity and scalability, and presents CPU-time costs of the proposed algorithm and GDE3. Section VII concludes this paper and outlines future research work.


## II. Problem Definition

In this paper, we consider the following continuous multiobjective optimization problem (continuous MOP):

$$
\begin{aligned}
& \operatorname{minimize} \vec{F}(x)=\left(f_{1}(x), f_{2}(x), \ldots, f_{m}(x)\right)^{T} \\
& \text { subject to } \quad x \in X
\end{aligned}
$$

where $X \subset R^{n}$ is the decision space and $x=\left(x_{1}, \ldots, x_{n}\right)^{T} \in$ $R^{n}$ is the decision variable vector. $\vec{F}: X \rightarrow R^{m}$ consists of $m$ real-valued continuous objective functions $f_{i}(x)(i=$ $1,2, \ldots, m) . R^{m}$ is the objective space. In the case of $m=2$, this problem is referred to as a continuous biobjective optimization problem.

Let $a=\left(a_{1}, \ldots, a_{m}\right)^{T}, b=\left(b_{1}, \ldots, b_{m}\right)^{T} \in R^{m}$ be two vectors, $a$ is said to dominate $b$, denoted by $a \prec b$, if $a_{i} \leq b_{i}$ for all $i=1, \ldots, n$, and $a \neq b$. A point $x^{\star} \in X$ is called (globally) Pareto optimal if there is no $x \in X$ such that $\vec{F}(x) \prec \vec{F}\left(x^{\star}\right)$. The set of all the Pareto optimal points, denoted by $P S$, is called the Pareto set. The set of all the Pareto objective vectors, $P F=$ $\left\{y \in R^{m} \mid y=\vec{F}(x), x \in P S\right\}$, is called the Pareto front [2], [20].

Under certain smoothness assumptions, it can be induced from the Karush-Kuhn-Tucker condition that the PS of a continuous MOP defines a piecewise continuous $(m-1)$-dimensional manifold in the decision space [20], [22]. Therefore,

[^0]
[^0]:    ${ }^{1}$ Due to the page limit of this paper, the experimental comparison between this algorithm and its predecessors will be presented in a forthcoming working report, but not in this paper.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of the basic idea. Individual solutions should be scattered around the $P S$ in the decision space in a successful MOEA.
the $P S$ of a continuous biobjective optimization problem is a piecewise continuous curve in $R^{n}$, while the $P S$ of a continuous MOP with three objectives is a piecewise continuous surface. In fact, the PSs of the ZDT test problems [23], [34], [35], the widely used test instances for continuous biobjective optimization problems in the evolutionary computation community, are line segments in the decision space.

## III. AlGORITHM

## A. Basic Idea

EDAs build a probability model for characterizing promising solutions in the search space based on statistical information extracted from the previous search and then sample new trial solutions from the model thus built. A very essential issue is what kind of model one should use for such a task. A good model should be easy to build and sample, and be able to describe promising areas with good fidelity [36]-[38].
The population in the decision space in an EA for (1) will hopefully approximate the $P S$ and be uniformly scattered around the $P S$ as the search goes on. Therefore, we can envisage the points in the population as independent observations of a random vector $\xi \in R^{n}$ whose centroid is the $P S$ of (1). Since the $P S$ is an $(m-1)$-dimensional piecewise continuous manifold, $\xi$ can be naturally described by

$$
\xi=\zeta+\varepsilon
$$

where $\zeta$ is uniformly distributed over a piecewise continuous ( $m-1$ )-dimensional manifold, and $\varepsilon$ is an $n$-dimensional zeromean noise vector.
Fig. 1 illustrates our basic idea.

## B. Algorithm Framework

At each generation $t$, the proposed algorithm for (1), called regularity model-based multiobjective estimation of distribution algorithm (RM-MEDA) hereafter, maintains:

- a population of $N$ solutions (i. e. points in $X$ )

$$
\operatorname{Pop}(t)=\left\{x^{1}, x^{2}, \ldots, x^{N}\right\}
$$

- their $\vec{F}$-values: $\vec{F}\left(x^{1}\right), \vec{F}\left(x^{2}\right), \ldots, \vec{F}\left(x^{N}\right)$.

The algorithm works as follows.

## RM-MEDA

Step 0) Initialization: Set $t:=0$. Generate an initial population $\operatorname{Pop}(0)$ and compute the $\vec{F}$-value of each individual solution in $\operatorname{Pop}(0)$.

Step 1) Stopping Condition: If stopping condition is met, stop and return the nondominated solutions in $\operatorname{Pop}(t)$ and their corresponding $\vec{F}$ vectors. All these $\vec{F}$ vectors constitute an approximation to the $P F$.
Step 2) Modeling: Build the probability model (2) for modeling the distribution of the solutions in $\operatorname{Pop}(t)$.
Step 3) Reproduction: Generate a new solution set $Q$ from the model (2). Evaluate the $\vec{F}$-value of each solution in $Q$.
Step 4) Selection: Select $N$ individuals from $Q \bigcup \operatorname{Pop}(t)$ to create $\operatorname{Pop}(t+1)$.
Step 5) Set $t:=t+1$ and go to Step 1.
In the following, we discuss the implementation of modeling, reproduction, and selection in the above algorithm.

## C. Modeling

Fitting the model (2) to the points in $\operatorname{Pop}(t)$ is highly related to principal curve or surface analysis, which aims at finding a central curve or surface of a set of points in $R^{n}$ [39]. However, most current algorithms for principal curve or surface analysis are rather expensive due to the intrinsic complexity of their models. Since modeling needs to be conducted at each generation of RM-MEDA, a too complicated model is not affordable in RM-MEDA. On the other hand, a complicated model is not necessary since the actual distribution of the points in $\operatorname{Pop}(t)$ could hardly be exactly described by (2).

In our implementation, we assume, for the sake of simplicity, that the centroid of $\xi$ consists of $K$ manifolds $\Psi^{1}, \ldots, \Psi^{K}$ (i.e., $\zeta$ in (2) is uniformly distributed on these manifolds), each $\Psi^{j}$ is a $(m-1)$-dimensional hyper-rectangle. Particularly,

- in the case of two objectives (i.e., $m=2$ ): each $\Psi^{j}$ is a line segment in $R^{n}$.
- in the case of three objectives (i.e., $m=3$ ): each $\Psi^{j}$ is a 2-D rectangle in $R^{n}$.
Let $A^{j}$ denote the event that $\zeta$ is from $\Psi^{j}$. Then

$$
\sum_{j=1}^{K} \operatorname{Prob}\left(A^{j}\right)=1
$$

We make the following assumptions that under the condition that the event $A^{j}$ happens.

- $\zeta$ is uniformly randomly generated over $\Psi^{j}$.
- $\varepsilon \sim N\left(0, \sigma_{j} I\right)$, where $I$ is the $n \times n$ identity matrix and $\sigma_{j}>0$. In other words, all the components in $\varepsilon$ are independent and identically distributed (i.i.d.).
The modeling problem, under the above assumptions, becomes estimating $\Psi^{j}, \sigma_{j}$ and $\operatorname{Prob}\left(A^{j}\right)(j=1,2, \ldots, K)$. To solve it, we need to first partition $\operatorname{Pop}(t)$ into $K$ disjoint clusters $S^{1}, \ldots, S^{K}$ such that the points in $S^{j}$ can be regarded as being sampled under the condition of $A^{j}$. Then, we can estimate the parameters.

In this paper, we use the $(m-1)$-dimensional local principal component analysis ( $(m-1)$-D Local PCA) algorithm [40] for partitioning $\operatorname{Pop}(t)$. Let $S$ be a finite subset of $R^{n}$, the (sample) mean of $S$ is

$$
\bar{x}=\frac{1}{|S|} \sum_{s \in S} x
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. Illustration of extension: The number of clusters $(K)$ is 3 in this illustrative example. $\Phi^{4}, \Phi^{2}$, and $\Phi^{3}$ could not approximate the $P S$ very well, their extensions $\Psi^{1}, \Psi^{2}$, and $\Psi^{3}$, however, can provide a better approximation.
where $|S|$ is the cardinality of $S$. The (sample) covariance matrix of the points in $S$ is

$$
\operatorname{Cov}=\frac{1}{|S|-1} \sum_{x \in S}(x-\bar{x})(x-\bar{x})^{T}
$$

The $i$ th principal component $U^{i}$ is a unity eigenvector associated with the $i$ th largest eigenvalue of the matrix Cov. Then, the affine $(m-1)$-dimensional principal subspace of the points in $S$ is defined as

$$
\left\{x \in R^{n} \mid x=\bar{x}+\sum_{i=1}^{m-1} \theta_{i} U^{i}, \theta_{i} \in R, i=1, \ldots, m-1\right\}
$$

The partition $S^{1}, \ldots, S^{K}$ obtained by the ( $m-1$ )-D Local PCA algorithm minimizes the following error function:

$$
\sum_{j=1}^{K} \sum_{x \in S^{j}} \operatorname{dist}\left(x, \mathcal{L}_{j}^{m-1}\right)^{2}
$$

where $\mathcal{L}_{j}^{m-1}$ is the affine $(m-1)$-dimensional principal subspace of the points in $S^{j}$, $\operatorname{dist}\left(x, \mathcal{L}_{j}^{m-1}\right)$ is the Euclidean distance from $x$ to its projection in $\mathcal{L}_{j}^{m-1}$.

The $(m-1)$-D Local PCA [40] partitions $\operatorname{Pop}(t)=$ $\left\{x^{1}, \ldots, x^{N}\right\}$ into $S^{1}, \ldots, S^{K}$ in the following iterative way.
Step 1) Randomly initialize $\mathcal{L}_{i}^{m-1}$ to be an affine ( $m-$ 1)-dimensional space containing a point randomly chosen from $\operatorname{Pop}(t)$.
Step 2) Partition the points in $\operatorname{Pop}(t)$ into $K$ disjoint clusters $S^{1}, \ldots, S^{K}$,

$$
\begin{aligned}
S^{j}=\{x \mid x \in \operatorname{Pop}(t), \text { and } & \operatorname{dist}\left(x, \mathcal{L}_{j}^{m-1}\right) \\
& \leq \operatorname{dist}\left(x, \mathcal{L}_{k}^{m-1}\right) \text { for all } k \neq j\}
\end{aligned}
$$

Step 3) Set $\mathcal{L}_{j}^{m-1}, j=1, \ldots, K$, to be the affine $(m-$ 1)-dimensional principal subspace of the points in $S^{j}$.
Step 4) Iterate Steps 2 and 3 until no change in partition is made.
The Local PCA algorithm is more suitable for partitioning $\operatorname{Pop}(t)$ for building the model (2) than the widely used $K$-means clustering method in which a cluster centroid is a point [30], since we assume that the centroid of each cluster should be a $(m-1)$-D hyper-rectangle instead of a point.

Schematically, modeling (i.e., estimating $\Psi_{k}$ and $\sigma_{k}$ ) in RM-MEDA works as follows.

Modeling by the $(m-1)$-D Local PCA
Step 2.1) Partition $\operatorname{Pop}(t)$ into $K$ disjoint clusters $S^{1}, \ldots, S^{K}$ by the $(m-1)$-D Local PCA algorithm.
Step 2.2) For each cluster $S^{j}$. Let $\bar{x}^{j}$ be its mean and $U_{i}^{j}$ be its $i$ th principal component. Compute

$$
a_{i}^{j}=\min _{x \in S^{j}}\left(x-\bar{x}^{j}\right)^{T} U_{i}^{j}
$$

and

$$
b_{i}^{j}=\max _{x \in S^{j}}\left(x-\bar{x}^{j}\right)^{T} U_{i}^{j}
$$

for $i=1,2, \ldots, m-1$. Then, set

$$
\begin{aligned}
\Psi^{j}= & \left\{x \in R^{n} \mid x=\bar{x}^{j}\right. \\
& \left.+\sum_{i=1}^{m-1} \alpha_{i} U_{i}^{j}, a_{i}^{j}-0.25\left(b_{i}^{j}-a_{i}^{j}\right) \leq \alpha_{i} \leq b_{i}^{j}+0.25\left(b_{i}^{j}-a_{i}^{j}\right)\right. \\
& \left.i=1, \ldots, m-1.\right\}
\end{aligned}
$$

Let $\lambda_{i}^{j}$ be the $i$ th largest eigenvalue of the covariance matrix of the points in $S^{j}$, set

$$
\sigma_{j}=\frac{1}{n-m+1} \sum_{i=m}^{n} \lambda_{i}^{j}
$$

We would like to make the following comments on the above modeling method.

- The smallest hyper-rectangle containing the projections of all the points of $S^{j}$ in the affine $(m-1)$-dimensional principal subspace of $S^{j}$ is

$$
\begin{aligned}
\Phi^{j}=\{ & x \in R^{n} \mid x=\bar{x} \\
& \left.+\sum_{i=1}^{m-1} \alpha_{i} U_{i}^{j}, a_{i}^{j} \leq \alpha_{i} \leq b_{i}^{j}, i=1, \ldots, m-1\right\}
\end{aligned}
$$

$\Psi^{j}$ in Step 2.2 extends $\Phi^{j}$ by $50 \%$ along each of the directions $U_{1}^{j}, \ldots, U_{m-1}^{j}$. The motivation behind this extension is that $\operatorname{Pop}(t)$ often could not cover the whole $P S$, and thus the union of all these smallest hyper-rectangles $\Phi^{1}, \ldots, \Phi^{K}$ can only approximate part of the $P S$, while the union of all the $\Psi^{1}, \ldots, \Psi^{K}$ may provide a good approximation to the $P S$. Fig. 2 illustrates this motivation.

- $\lambda_{0 i}^{j}, \lambda_{m+1}^{j}, \ldots, \lambda_{n}^{j}$ characterize the deviation of the points in $S^{j}$ from its centroid. It is ideal to model $\varepsilon$ as

$$
\varepsilon=\sum_{i=m}^{n} \lambda_{i}^{j} U_{i}^{j} \varepsilon^{i}
$$

when $\varepsilon^{m}, \ldots, \varepsilon^{n}$ are $n-m+1$ independent $N(0,1)$ noises. Since it is often the case that $m \ll n$ and $\lambda_{i}^{j}, i=m, \ldots, n$ is very small compared with the first $(m-1)$ largest eigenvalues, the difference, in terms of distribution between the noise sampled from $N\left(0, \sigma_{j} I\right)$ and that in (6) is tiny when $\sigma_{j}$ is defined as in (5). Moreover, sampling from (6) is

more complicated than from $N\left(0, \sigma_{j} I\right)$. This is why we use $N\left(0, \sigma_{j} I\right)$ for facilitating the sampling procedure. $\sigma_{j}$ also controls the degree of the exploration of the search in the reproduction step.

- Since both the Local PCA and the noise model $N\left(0, \sigma_{j} I\right)$ are rotationally invariant, so is the above modeling method. Therefore, RM-MEDA is invariant of any orthogonal coordinate rotation, which is a property not shared by other algorithms using crossover and mutation.


## D. Reproduction

In our implementation of reproduction in this paper, $N$ new solutions are generated. The first issue we need to consider is how many new trial solutions are generated around each $\Psi^{i}$. Since it is desirable that final solutions are uniformly distributed on the $P S$, we set

$$
\operatorname{Prob}\left(A^{j}\right)=\frac{\operatorname{vol}\left(\Psi^{j}\right)}{\sum_{i=1}^{K} \operatorname{vol}\left(\Psi^{i}\right)}
$$

where $\operatorname{vol}\left(\Psi^{j}\right)$ is the $(m-1)$-D volume of $\Psi^{j}$. Therefore, the probability that a new solution is generated around $\Psi^{j}$ is proportional to $\operatorname{vol}\left(\Psi^{j}\right)$.

A simple reproduction scheme for generating a new solution $x$, used in our experimental studies, works as follows.

## Reproduction by Sampling (Reproduction/S)

Step 1) Randomly generate an integer $\tau \in\{1,2, \ldots, K\}$ with

$$
\operatorname{Prob}(\tau=k)=\frac{\operatorname{vol}\left(\Psi^{k}\right)}{\sum_{j=1}^{K} \operatorname{vol}\left(\Psi^{j}\right)}
$$

Step 2) Uniformly randomly generate a point $x^{\prime}$ from $\Psi^{\tau}$. Generate a noise vector $\varepsilon^{\prime}$ from $N\left(0, \sigma_{\tau} I\right)$.
Step 3) Return $x=x^{\prime}+\varepsilon^{\prime}$.
In Step 3 of RM-MEDA, $N$ new solutions can be produced by repeating Reproduction/S $N$ times.

In Reproduction/S, $x^{\prime}$, the main part of $x$ is from $\Psi^{\tau}$, which is the extension of $\Phi^{\tau}$. Therefore, the search will, hopefully, perform exploitation around the $P F$. Such exploitation, guided by the extension, is mainly along the first $m-1$ principal components. $\varepsilon^{\prime}$, the noise part of $x$ is necessary since $\Psi^{\tau}$ is just an approximation to part of the $P F$. Moreover, it provides diversity for the further search.

## E. Selection

In principle, any selection operators for MOEAs can be used in RM-MEDA. The selection procedure used in the experimental studies of this paper is based on the nondominated sorting of NSGA-II [6]. It is called NDS-selection in the following.

NDS-Selection partitions $Q \cup \operatorname{Pop}(t)$ into different fronts $F_{1}, \ldots, F_{l}$ such that the $j$ th front $F_{j}$ contains all the nondominated solutions in $\{Q \cup \operatorname{Pop}(t)\} \backslash\left(\cup_{i=1}^{l-1} F_{i}\right)$. Therefore, there is no solution in $\{Q \cup \operatorname{Pop}(t)\} \backslash\left(\cup_{i=1}^{l-l} F_{i}\right)$ that could dominate a
solution in $F_{j}$. Roughly speaking, $F_{1}$ is the best nondominated front in $Q \cup \operatorname{Pop}(t), F_{2}$ is the second best nondominated front, and so on.

The crowding distance $d_{c}(x, S)$ of point $x$ in set $S$ is defined as the average side length of the largest $m$-D rectangle in the objective space subject to the two constraints: a) each of its sides is parallel to a coordinate axis and b) $\vec{F}(x)$ is the only point in $\vec{F}(S)=\{\vec{F}(y) \mid y \in S\}$ that is an interior point in the rectangle. A solution with larger crowding distance should be given priority to enter $\operatorname{Pop}(t+1)$ since it could increase the diversity of $\operatorname{Pop}(t+1)$.

The details of the selection procedure is given as follows.

## NDS-Selection

Step 1) Partition $Q \cup \operatorname{Pop}(t)$ into different fronts $F_{1}, \ldots, F_{l}$ by using the fast nondominated sorting approach. Set $\operatorname{Pop}(t+1)=\emptyset$ and $k=0$.

Do

$$
\begin{gathered}
k=k+1 \\
\operatorname{Pop}(t+1)=\operatorname{Pop}(t+1) \cup F_{k} \\
\text { Until }|\operatorname{Pop}(t+1)| \geq N
\end{gathered}
$$

Step 2) While $|\operatorname{Pop}(t+1)|>N$, Do
For all the members in $F_{k} \cap \operatorname{Pop}(t+1)$, compute their crowding distances in $F_{k} \cap \operatorname{Pop}(t+1)$.
Remove the element in $F_{k} \cap \operatorname{Pop}(t+1)$ with the smallest crowding distance from $\operatorname{Pop}(t+1)$. In the case when there are more than one members with the smallest crowding distance, randomly choose one and remove it.
This selection operator selects $N$ members from $Q \cup \operatorname{Pop}(t)$ for forming $\operatorname{Pop}(t+1)$. Step 1 implements an elitism mechanism. The best fronts in $Q \cup \operatorname{Pop}(t)$ are added to $\operatorname{Pop}(t+1)$. After Step 1

$$
\operatorname{Pop}(t+1)=\bigcup_{j=1}^{k} F_{j}
$$

the last front in $\operatorname{Pop}(t+1)$ is $F_{k}$, the $k$ th front, which contains the "worst" solutions in $\operatorname{Pop}(t+1)$. When $|\operatorname{Pop}(t+1)|$ is larger than $N,\left|F_{k}\right|$ will be larger than $|\operatorname{Pop}(t+1)|-N$. Step 2 removes $|\operatorname{Pop}(t+1)|-N$ worst solutions from $\operatorname{Pop}(t+1)$ to reduce its size to $N$. The crowding distance is used to compare the quality of solutions in Step 2.

This selection procedure is the same as that used in NSGA-II except that we remove solutions from $\operatorname{Pop}(t+1)$ one by one and we recalculate the crowding distances before deciding which solution should be deleted from $\operatorname{Pop}(t+1)$, which can increase the diversity of $\operatorname{Pop}(t+1)$ at extra computational cost. We noticed that GDE3 [33] uses a very similar selection.

## IV. Three Other Algorithms in Comparison

The major purpose of this work is to tackle variable linkages in continuous MOPs. The studies conducted in [19] show that PCX-NSGA-II and GDE3 [33] perform better than other algorithms for continuous MOPs with variable linkages. In this paper, we compare RM-MEDA with these two algorithms. Since RM-MEDA is an EDA based on regularity, we also compare it with MIDEA [27], which is an EDA without using

TABLE 1
TEST INSTANCES


regularity, to investigate whether or not using regularity can improve the performance of EDAs.

## A. Generalized Differential Evolution (GDE3) [33]

Let $x=\left(x_{1}, \ldots, x_{n}\right)^{T}$ be a solution in the current population, its offspring $y=\left(y_{1}, \ldots, y_{n}\right)^{T}$ in GDE3 is generated as follows.

1) Randomly select from the current population three distinct solutions $x^{r 1}, x^{r 2}, x^{r 3}$, and randomly choose index $\in\{1,2, \ldots, n\}$.
2) Set $z=x^{r 1}+F \times\left(x^{r 2}-x^{r 3}\right)$.
3) Set the $i$ th element of $y$

$$
y_{i}= \begin{cases}z_{i} & \text { if } \operatorname{rand}<C R \text { or } i=\text { index } \\ x_{i}^{r 1} & \text { otherwise }\end{cases}
$$

where rand is a random number uniformly generated from $[0,1], F$ and $C R$ are two control parameters.

In GDE3, all the solutions in the current population first generate their offspring, these offspring and their parents undergo a selection operator similar to the one used in RM-MEDA and then the selected solutions form a new population for the next generation. The details of GDE3 can be found in [33]. The code of GDE3 used in comparison is written in C by ourselves.

## B. PCX-NSGA-II [19]

Parent-centric recombination (PCX) [41] generates a trial solution $y$ from $\mu$ parent solutions $x^{1}, \ldots, x^{\mu}$ as follows.

1) Select a solution $x^{p}$ from $x^{1}, \ldots, x^{\mu}$ and let it be the "index parent".
2) Compute the direction vector $d^{p}$ to $x^{p}$ from the center of these $\mu$ parent solutions, i.e., $d^{p}=x^{p}-(1 / \mu) \sum_{i=1}^{p} x^{i}$, and $\mu$ orthogonal directions $e^{1}, \ldots, e^{\mu}$ to $d^{p}$. Compute average perpendicular distance, $\bar{D}$, of the other $\mu-1$ parents to the line passing $x^{p}$ and the center.

3) Set

$$
y=x^{p}+\omega_{\zeta} d^{p}+\sum_{i=1, i \neq p}^{\mu} \omega_{\eta} \bar{D} e^{i}
$$

where $\omega_{\zeta}$ and $\omega_{\eta}$ are two zero-mean normally distributed random variables with variance $\sigma_{\zeta}^{2}$ and $\sigma_{\eta}^{2}$, respectively.
In PCX-NSGA-II [19], PCX with $\mu=3$ is used to generate a set of new trial solutions. All of these new solutions are mutated by a polynomial mutation operator. The PCX-NSGA-II used in comparison is implemented in C by modifying the code of SBX-NSGA-II from KanGAL's webpage (http://www.iitk.ac.in/kangal/). In our implementation of PCX-NSGA-II, the NDS-selection operator described in Section III-E is used for selecting from the old solutions and new solutions for creating a new population for the next generation, this is the only difference from the implementation of Deb et al. in [19]. Our first experiments show that our implementation is slightly better in terms of solution quality. The motivation that we use the NDS-selection in the implementation of PCX-NSGA-II is to have a fair comparison with RM-MEDA.

## C. MIDEA [27]

MIDEA is an EDA for MOPs. It has been applied to continuous MOPs. Its major difference from RM-MEDA is that it uses a mixture of Gaussians. It does not take the regularity of the $P S$ into consideration and, thus it does not impose any constraints on distribution of the centers of the Gaussians. A specialized diversity preserving selection is used in MIDEA. The number of Gaussians is determined by an adaptive clustering method. The C code of MIDEA written by its authors is used in our experimental studies.

## V. COMPARISON STUDIES

## A. Performance Metric

The inverted generational distance (IGD) is used in assessing the performance of the algorithms in our experimental studies.
Let $P^{*}$ be a set of uniformly distributed points in the objective space along the $P F$. Let $P$ be an approximation to the $P F$, the inverted generational distance from $P^{*}$ to $P$ is defined as

$$
D\left(P^{*}, P\right)=\frac{\sum_{v \in P^{*}} d(v, P)}{\left|P^{*}\right|}
$$

where $d(v, P)$ is the minimum Euclidean distance between $v$ and the points in $P$. If $\left|P^{*}\right|$ is large enough to represent the $P F$ very well, $D\left(P^{*}, P\right)$ could measure both the diversity and convergence of $P$ in a sense. To have a low value of $D\left(P^{*}, P\right)$, $P$ must be very close to the $P F$ and cannot miss any part of the $P F$.
In our experiments, we select 500 evenly distributed points in $P F$ and let these points be $P^{*}$ for each test instance with two objectives, and 1000 points for each test instance with three objectives.
IGD has been recently used by some other researchers (e.g., [42]). As its name suggests, it is an inverted variation of the
widely-used generational distance (GD) performance metric [43]. The GD represents the average distance of the points in an approximation to the true $P F$, which cannot effectively measure the diversity of the approximation. There are several different ways of computing and averaging the distances in the GD performance metrics (e.g., [43] and [6]), the version of IGD used in this paper inverts the $\Upsilon$ version of GD in [6].

## B. General Experimental Setting

RM-MEDA is implemented in C. The machine used in our experiments is Pentium(R) 4 (3.40 GHz, 1.00 GB RAM). In this section, the experimental setting is as follows.

- The number of new trial solutions generated at each generation: The number of new solutions generated at each generation in all the four algorithms is set to be 100 for all the test instances with two objectives, and 200 for the test instances with three objectives. Since in RM-MEDA, GDE3, and PCX-NSGA-II, the population size is the same as the number of new trial solutions generated at each generation, these three algorithms have the same population size for each test instance in our experiments.
- The number of decision variables: It is set to be 30 for all the test instances.
- Parameter setting in RM-MEDA: In Local PCA algorithm, $K$, the number of clusters, is set to be 5 .
- Parameter setting in GDE3: Both $C R$ and $F$ in the DE operator is set to be 1 , which was the best setting for most test instances in the simulation studies in [19].
- Parameter setting in PCX-NSGA-II: $\sigma$ in PCX is set to be 0.4 , which worked very well for most test instances in the simulation studies in [19].
- Parameter setting in MIDEA: $\tau$ is set to be 0.3 , therefore, the population size is $\lceil 100 / 0.3\rceil=334$ in the case of two objectives and $\lceil 200 / 0.3\rceil=667$ in the case of three objectives. In [27], large populations were used in simulation studies. Our first experiments show that a large population does not improve the performance of MIDEA on the test instances with variable linkages significantly. Following [27], we set $\delta=1.5$.
- Number of runs and stopping condition: We run each algorithm independently 20 times for each test instance. The algorithms stop after a given number of $\widehat{F}$-function evaluations. The maximal number of function evaluations in each algorithm is 10000 for F1, F2, F5, and F6, 40000 for F4 and F8, and 100000 for F3, F7, F9, and F10.
- Dealing with boundary in RM-MEDA: In all the test instances, the feasible decision space is a hyper-rectangle. If an element of a solution $x$, sampled from a model in RM-MEDA is out of boundary, we simply reset its value to be a randomly selected value inside the boundary. This method is very similar to that used in GDE3.
- Initialization: Initial populations in all the algorithms are randomly generated.


## C. Test Instances With Linear Variable Linkages

We first compare RM-MEDA with the three other algorithms on four continuous MOPs with linear variable linkages. The test instances F1-F4 in Table I are used for this purpose.

![img-4.jpeg](img-4.jpeg)

Fig. 3. The evolution of the average $D$-metric of the nondominated solutions in the current populations among 20 independent runs with the number of 10000 function evaluations in four algorithms for F1.
![img-5.jpeg](img-5.jpeg)

Fig. 4. The evolution of the average $D$-metric of the nondominated solutions in the current populations among 20 independent runs with the number of 10000 function evaluations in four algorithms for F2.

F1-F4 are variants of ZDT1, ZDT2, ZDT6 [34], and DTLZ2 [44], respectively. Due to $g(x)$ used in these instances, F1-F3 have the same $P S$. Their $P S$ is a line segment

$$
x_{1}=\cdots=x_{n}, 0 \leq x_{i} \leq 1,1 \leq i \leq n
$$

The $P S$ of F4 is a 2-D rectangle

$$
x_{1}=x_{3}=\cdots=x_{n}, 0 \leq x_{i} \leq 1,1 \leq i \leq n
$$

There are linear variable linkages in these test instances. The variable linkages in these instances [45] are obtained by performing the following linear mapping on the variables in the original ZDT and DTLZ instances:

$$
x_{1} \rightarrow x_{1}, \quad x_{i} \rightarrow x_{i}-x_{1}, i=2, \ldots, n
$$

![img-4.jpeg](img-4.jpeg)

Fig. 5. The evolution of the average $D$-metric of the nondominated solutions in the current populations among 20 independent runs with the number of 100000 function evaluations in four algorithms for F3.
![img-5.jpeg](img-5.jpeg)

Fig. 6. The evolution of the average $D$-metric of the nondominated solutions in the current populations among 20 independent runs with the number of 40000 function evaluations in four algorithms for F4.

Therefore, our scheme for introducing variable linkages can be regarded as a special implementation of the general strategy proposed in [19], which is based on variable linear or nonlinear mappings.

Figs. 3-6 show the evolution of the average $D$-metric of the nondominated solutions in the current populations among 20 independent runs with the number of function evaluations in four algorithms. As many researchers pointed out [13], no single metric is always able to rank different algorithms appropriately. For this reason, Figs. 7-10 plot the nondominated front with the lowest $D$-metric obtained in 20 runs of each algorithm on each test instance. All the 20 fronts found are also plotted together for showing their distribution ranges in the objective space in Figs. 7-10.

It is clear from the above experimental results that both RM-MEDA and GDE3 perform significantly better than PCX-NSGA-II and MIDEA on these four test instances. Since $C R=1$ is set in GDE3, an offspring $y$ is a linear combination of three old solutions $x^{c 1}, x^{c 2}, x^{c 3}$, and the $P S s$ of these

![img-6.jpeg](img-6.jpeg)

Fig. 7. The final nondominated fronts found by each algorithm on F1. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm.
four test instances are line segments or a 2-D rectangle. If $x^{r 1}, x^{r 2}, x^{r 3}$ are close to the $P S$, so is $y$. Therefore, GDE3 exploits the regularity of these $P S s$ as RM-MEDA does in a sense. In contrast, PCX-NSGA-II and MIDEA have no efficient
mechanism for using the regularity. This could be a major reason why RM-MEDA and GDE3 are winners.

GDE3 slightly outperforms RM-MEDA on F1, F2, and F4 in terms of $D$-metric. The reason might be that RM-MEDA, like

![img-7.jpeg](img-7.jpeg)

Fig. 8. The final nondominated fronts found by each algorithm on F2. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm.
many other EDAs, does not directly use the location information of previous solutions in generating new solutions, which makes it poorer than GDE3 at refining a solution, particularly, when it is close to the PS. A possible way to overcome this shortcoming is to hybridize location information and globally statistical in-
formation, which has proved to be successful in the guided mutation for scalar optimization in [46] and [47].

F3 is the hardest among these four test instances. The distribution of the Pareto optimal solutions in the objective space in this instance is very different from that in the other three. If we

![img-8.jpeg](img-8.jpeg)

Fig. 9. The final nondominated fronts found by each algorithm on F3. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm (some solutions found by MIDEA fall out of the figure range).
uniformly sample a number of points in the $P S$ of F3 in the decision space, most of the corresponding Pareto optimal vectors in the objective space will be more likely to be in the left part of the $P F$. This makes it very difficult for an algorithm to approximate
the whole $P F$. RM-MEDA performs much better than GDE3 on F3. This could be attributed to the fact that RM-MEDA does extend along the principal directions so that it has a good chance of approximating the whole $P F$.

![img-9.jpeg](img-9.jpeg)

Fig. 10. The final nondominated fronts found by each algorithm on F4. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm.

## D. Test Instances With Nonlinear Variable Linkages

F5-F8 in Table I are test instances with nonlinear variable linkages. The $P S$ of F5-F7 is a bounded continuous curve defined by

$$
x_{1}=x_{i}^{2}, \quad i=2, \ldots, n . \quad 0 \leq x_{1} \leq 1
$$

The $P S$ of F8 is a 2-D bounded continuous surface defined by

$$
x_{1}=x_{i}^{2}, \quad i=3, \ldots, n . \quad 0 \leq x_{1}, x_{2} \leq 1
$$

The variable linkages in these instances [45] are obtained by performing the following nonlinear mapping on the variables in the original ZDT and DTLZ instances:

$$
x_{1} \rightarrow x_{1}, \quad x_{i} \rightarrow x_{i}^{2}-x_{1}, i=2, \ldots, n
$$

Figs. 11-14 present the evolution of the average $D$-metric of the nondominated solutions in the current population and Figs. 15-18 plot the final nondominated fronts found by each algorithm for each instance.

The experimental results show that RM-MEDA outperforms the three other algorithms on these four instances. In fact, only RM-MEDA is able to produce nondominated solutions which

![img-10.jpeg](img-10.jpeg)

Fig. 11. The evolution of the average $D$-metric of the nondominated solutions in the current populations among 20 independent runs with the number of 10000 -function evaluations in four algorithms on F5.
![img-11.jpeg](img-11.jpeg)

Fig. 12. The evolution of the average $D$-metric of the nondominated solutions in the current populations among 20 independent runs with the number of 10000 -function evaluations in four algorithms on F6.
approximate the whole $P F$ well, in all or some runs for all the test instances. These results are not surprising since only RM-MEDA considers modeling nonlinear variable linkages. In the three other algorithms, even if all the parent solutions are Pareto optimal, it is possible that their offspring is far from the $P S$.

It is evident from Figs. 11-14 that PCX-NSGA-II and MIDEA are stuck in terms of $D$-metric after a number of generations, which implies that these two algorithms may not be able to make any more improvement on their solution quality even if more computational time is used. This observation, in conjunction with the results of Deb et al. [19], suggests that reproduction operators are crucial in MOEAs. One should carefully design these operators for dealing with nonlinear variable linkages.

Fig. 17 suggests that F7 is the hardest instance for RM-MEDA. This might be due to the fact that the Pareto optimal solutions of F7 are not uniformly distributed as in its linear linkage counterpart F3 and RM-MEDA samples points uniformly around the $P S$ in the decision variable space. To improve the performance of RM-MEDA on problems like F3
![img-12.jpeg](img-12.jpeg)

Fig. 13. The evolution of the average $D$-metric of the nondominated solutions in the current populations among 20 independent runs with the number of 100000 -function evaluations in four algorithms on F7.
![img-13.jpeg](img-13.jpeg)

Fig. 14. The evolution of the average $D$-metric of the nondominated solutions in the current populations among 20 independent runs with the number of 40000 -function evaluations in four algorithms on F8.
and F7, one may need to consider the distribution of solutions in the objective space when sampling solutions from the models.

## E. Test Instances With Many Local Pareto Fronts

There are nonlinear variable linkages in F9 and F10. Furthermore, these two instances have many local Pareto fronts since their $g(x)$ has many locally minimal points. The experimental results presented in Fig. 19 show that RM-MEDA can approximate the $P F$ very well in each run and significantly outperforms the three other algorithms on F9. It is also evident that all the four algorithms fail in converging to the global Pareto front of F10 in Fig. 20. The failure could be because, as Deb et al. have noticed on the ability of their NSGA-II [6], it is not an easy task for these evolutionary algorithms to find the globally minimal point of $g(x)$. To tackle MOPs with many local Pareto optimal fronts, efficient mechanisms for global optimization of a scalar objective may be worthwhile tailored and used in MOEAs.

## VI. SENSitivity, Scalability, and CPU-Time Costs

The experimental results in Section V have shown that, overall, RM-MEDA outperforms the three other algorithms,

![img-14.jpeg](img-14.jpeg)

Fig. 15. The final nondominated fronts found by each algorithm on F5. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm.
and GDE3 comes second on these continuous MOP test instances with variable linkages.

We have compared the sensitivity of population size in RM-MEDA and GDE3 and investigated the effect of the number of clusters on the performance of RM-MEDA on sev-
eral test instances. We have studied how the computational cost, in terms of the number of $I^{2}$-function evaluations, increases as the number of decision variables increases in both RM-MEDA and GDE3. We have also recorded the CPU time used by each algorithm. Due to the limit of the paper length, however, only

![img-15.jpeg](img-15.jpeg)

Fig. 16. The final nondominated fronts found by each algorithm on F6. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm.
the experimental results on F5 with nonlinear variable linkages are presented in this section. The parameter settings in the experiments are presented in Tables II and III. Twenty independent runs have been conducted for each parameter setting.

## A. Sensitivity to Population Size in RM-MEDA and GDE3

To study how the performances of RM-MEDA and GDE3 are sensitive to the population size, we have tried different values of

![img-16.jpeg](img-16.jpeg)

Fig. 17. The final nondominated fronts found by each algorithm on F7. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm.
population size: $20,30,40,50,60,80,100,150,200,250,300$, 350,400 in both algorithms for F5.

Fig. 21 shows the average $D$-metrics versus the numbers of $F$-function evaluations under different population size set-
tings in RM-MEDA and GDE3, respectively. It is clear that RM-MEDA is much less sensitive to the setting of population size than GDE3 on F5. In fact, RM-MEDA can, with the population sizes from 20 to 200, lower the $D$-metric value

![img-17.jpeg](img-17.jpeg)

Fig. 18. The final nondominated fronts found by each algorithm on F8. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm.
below 0.05 within 10000 function evaluations. Its convergence speed does not change much over this range. In contrast, the performance of GDE3 worsens considerably for small or large population sizes, and GDE3 could not lower the $D$-metric value below 0.05 within 10000 function evaluations with any population sizes.

## B. Sensitivity to the Number of Clusters in RM-MEDA

We have tested all the different cluster numbers from 1 to 15 in RM-MEDA. Fig. 22 presents the average $D$-metric values versus the numbers of $\vec{F}$-function evaluations with
different cluster numbers on F5. As clearly shown in this figure, RM-MEDA is able to reduce the $D$-metric below 0.002 with 15000 function evaluations when the cluster number is from 2 to 13 . It is also evident from this figure that the convergence speed does not change dramatically over this range. Thus, we could claim that RM-MEDA is not very sensitive to the setting of the cluster number for MOP instances which are somehow similar to F5. We should point out that the range of appropriate cluster numbers in RM-MEDA is still problem-dependent.

The experimental results in Fig. 22 reveal that RM-MEDA performs poorly when the cluster number is 1 or larger than

![img-18.jpeg](img-18.jpeg)

Fig. 19. The final nondominated fronts found by each algorithm on F9. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm.
13. Part of the reason could be that the Local PCA reduces to classic PCA, and consequently, underfits the population when the cluster number is 1 , and it could overfit in the case when the cluster number is larger than 13.

## C. Scalability of RM-MEDA and GDE3

We have tried RM-MEDA and GDE3 on different numbers of decision variables. Fig. 23 presents the number of the successful runs in which each algorithm has reached each of four

![img-19.jpeg](img-19.jpeg)

Fig. 20. The final nondominated fronts found by each algorithm on F10. The left panels show the nondominated fronts with the lowest $D$-metric obtained by each algorithm, while the right panels plot all the 20 fronts together found by each algorithm.
given levels of the $D$-metric within 20000 function evaluations for F5 with different numbers of decisions variables. The average numbers of function evaluations among the successful runs in each algorithm are also plotted in this figure. It can be
seen that RM-MEDA succeeds in every run for all the numbers of decision variables. It is also clear that the number of function evaluations, for lowering the $D$-metric below each of four levels, linearly scales up with the number of decision variables

TABLE II
The Parameter Settings of RM-MEDA for F5 in Section VI


TABLE III
The Parameter Settings of GDE3 for F5 in Section VI

![img-20.jpeg](img-20.jpeg)

Fig. 21. The average $D$-metric value versus the number of $\hat{F}$-function evaluations under the different settings of population sizes in RM-MEDA and GDE3 for F5.
in RM-MEDA. Although the average numbers of function evaluations among the successful runs in GDE3 also linearly scale up, its successful rate deceases substantially as the number of decision variables increases. In fact, GDE3 cannot reduce the $D$-metric value below 0.05 in any single run when the number of the decision variables is 100 .

The linear scalability of RM-MEDA in this test instance should be due to two facts: a) the $P S$ of F5 is always a 1-D continuous curve no matter how large its number of the decision variables is, which may explain why the hardness of F5 does not exponentially increase as its number of the decision variables increases and b) in RM-MEDA, only 1-D Local PCA is needed for F5 and sampling is always performed along a 1-D curve, then the curse of dimensionality may not exist in this test instance. Note that many real-world continuous MOPs should meet the regularity condition. These results imply that
![img-21.jpeg](img-21.jpeg)

Fig. 22. The average $D$-metric value versus the numbers of $\hat{F}$-function evaluations with different cluster numbers in RM-MEDA for F5.

RM-MEDA could be more suitable for solving large-scale MOPs.

## D. CPU-Time Cost

The good performance of RM-MEDA does not come without a price. Modeling and reproduction in RM-MEDA is more complicated than genetic operators such as crossover and mutation used in other MOEAs. RM-MEDA needs extra CPU time for running Local PCA at each generation. The CPU time used by RM-MEDA and GDE3 for F5 with different numbers of decision variables are given in Table IV.

Since we use the setting in Section VI-C, the total number of the function evaluations is 20000 and the number of generations is 200 in both algorithms. Therefore, the Local PCA was run 200 times in RM-MEDA. From the above experimental results, we can conclude that although RM-MEDA is more time consuming than GDE3, it is still affordable in many applications, where the CPU time of each function evaluation is under half an hour and a cluster of (say, 100) computers is available. To significantly reduce the number of function evaluations in RM-MEDA and make it more applicable for MOPs with very expensive function evaluations, one may need to incorporate metamodeling techniques into RM-MEDA.

## VII. CONCLUSION

It has not been well studied how to generate new trial solutions in multiobjective evolutionary optimization. Reproduction operators such as crossover and mutation, which were originally developed for scalar optimization, are directly used in most of current MOEAs. This could be one of the major reasons why these algorithms did not perform well on MOPs with variable linkages. In this paper, the regularity property of continuous MOPs is used as a basis for an estimation of distribution algorithm for dealing with variable linkages. RM-MEDA, the proposed algorithm, models a promising area in the search space by a probability model whose centroid is a piecewise continuous manifold. The Local PCA algorithm was employed for building such a model. New trial solutions are sampled from the model thus built.

![img-22.jpeg](img-22.jpeg)

Fig. 23. The average number of function evaluations among the successful runs for reaching each of four given levels of $D$-metric versus the number of decision variables in two algorithms for F5. The marked number is the number of successful runs. The solid line is for RM-MEDA while dash line for GDE3.

TABLE IV
The CPU Time (in Seconds) Used by RM-MEDA and GDE3 for $F 5$ With Different Numbers of Decision Variables

Experimental studies have shown that overall, RM-MEDA performs better than GDE3, PCX-NSGA-II, and MIDEA on a set of test instances with variable linkages. The sensitivity and scalability of RM-MEDA and GDE3 have also been experimentally studied.

We have found that RM-MEDA could perform slightly poorer than GDE3 on some test instances with linear variable linkages. We argued that it could be because RM-MEDA did not directly use the location information of individual solutions for
generating new trial solutions. The experimental results also reveal that RM-MEDA may fail in test instances with many local Pareto fronts.

The future research topics along this line should include the following.

- Combination of location information of individual solutions and globally statistical information for improving the ability of RM-MEDA to refine a solution. Guided mutation [46], [47] could be worthwhile studying for this purpose.
- Incorporating other techniques into RM-MEDA in order to improve its ability for global search. Effective global search techniques for scalar optimization should be considered.
- Combination of RM-MEDA with metamodeling techniques [48] for reducing the number of function evaluations.

- Use of other machine learning techniques, particularly, generative model learning for building distribution models such as mixtures of probabilistic principal component analyzers [49], for building models in RM-MEDA.
- Use of experimental design techniques for improving sampling quality. Experimental design techniques have been used in the design of genetic operators (e.g., [50]).
- Extension of RM-MEDA to constrained and/or dynamic MOPs. We should exploit properties of these MOPs in modifying or designing algorithms.


## ACKNOWLEDGMENT

The authors would like to acknowledge the help of H. Li, Dr. T. Okabe, Dr. B. Sendhoff, and Prof. E. Tsang on this work. They also thank Prof. X. Yao, the anonymous reviewers, and the anonymous associate editor for their insightful comments and suggestions.
