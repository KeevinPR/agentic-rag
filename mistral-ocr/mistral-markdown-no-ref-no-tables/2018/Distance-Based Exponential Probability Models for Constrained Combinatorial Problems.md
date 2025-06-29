# Distance-Based Exponential Probability Models for Constrained Combinatorial Problems 

Josu Ceberio ${ }^{1(\boxtimes)}$, Alexander Mendiburu ${ }^{1}$, and Jose A. Lozano ${ }^{1,2}$<br>${ }^{1}$ University of the Basque Country UPV/EHU, Paseo Manuel Lardizabal 1, 20018 Donostia, Spain<br>josu.ceberio@ehu.eus<br>${ }^{2}$ Basque Center for Applied Mathematics (BCAM), Alameda Mazarredo 14, 48009 Bilbao, Spain


#### Abstract

Estimation of Distribution Algorithms (EDAs) have already demonstrated their utility when solving a broad range of combinatorial problems. However, there is still room for methodological improvement when approaching problems with constraints. The great majority of works in the literature implement repairing or penalty schemes, or use ad-hoc sampling methods in order to guarantee the feasibility of solutions. In any of the previous cases, the behavior of the EDA is somehow denaturalized, since the sampled set does not follow the probability distribution estimated at that step. In this work, we present a general method to approach constrained combinatorial optimization problems by means of EDAs. This consists of developing distance-based exponential probability models defined exclusively on the set of feasible solutions. In order to illustrate this procedure, we take the 2-partition balanced Graph Partitioning Problem as a case of study, and design efficient learning and sampling methods to use distance-based exponential probability models in EDAs.


Keywords: Constraint $\cdot$ Estimation of Distribution Algorithm
Distance-based exponential model $\cdot$ Graph Partitioning Problem

## 1 Introduction

A Combinatorial Optimization Problem (COP), $\mathbf{P}=(\Omega, f)$, consists of a domain of solutions $\Omega$ also known as search space (finite or infinite countable), and an objective function $f$ that is defined as

[^0]
[^0]:    This work has been partially supported by the Research Groups 2013-2018 (IT-60913) programs (Basque Government), and TIN2016-78365R and TIN2017-82626R (Spanish Ministry of Economy, Industry and Competitiveness). Jose A. Lozano is also supported by BERC 2014-2017 and Elkartek programs (Basque government) and Severo Ochoa Program SEV-2013-0323 (Spanish Ministry of Economy and Competitiveness).

$$
\begin{aligned}
f: \Omega & \rightarrow \mathbf{R} \\
x & \mapsto f(x)
\end{aligned}
$$

Given an instance of the problem, the aim is to find a solution $x \in \Omega$ such that $f$ is maximized (or minimized).

The work on computers and intractability by Garey and Johnson [6] showed that many COPs are NP-hard, denoting the difficulty of finding the optimum solution of a problem of this type (motivated principally by the size of $\Omega$ ). In this sense, literature on evolutionary computation has proposed a broad range of heuristic and metaheuristic algorithms that are able to provide acceptable solutions in reasonable computation times. Among those algorithms, Estimation of Distribution Algorithms (EDAs) $[11,16]$ have proved to be a powerful evolutionary algorithm for solving either artificial or real-world COPs $[3,13]$.

EDAs are a type of population-based evolutionary algorithm designed for solving combinatorial and numerical optimization problems. Based on machine learning techniques, at each iteration, EDAs learn a probabilistic model from a subset of the most promising solutions, trying to explicitly express the dependencies between the different variables of the problem. Then, by sampling the probabilistic model learnt in the previous step, a new population of solutions is created. The algorithm iterates until a certain stopping criterion is met, such as a maximum number of iterations, homogeneity of the population, or a lack of improvement in the solutions.

Among different types of COPs, there is one where there is room for methodological improvement in the design of EDAs. We refer to problems with constraints (also known as restrictions). In general, a $n$ dimensional constrained COP, or from now on, constrained problem [10] consists of (following the same notation as for COPs)

$$
\begin{aligned}
\operatorname{minimizing} & f(\mathbf{x}), \quad \mathbf{x}=\left(x_{1}, \ldots, x_{n}\right) \in \Omega \\
\text { subject to, } & g_{i}(\mathbf{x}) \leq 0, i=1, \ldots, r \\
& h_{j}(\mathbf{x})=0, j=r+1, \ldots, m
\end{aligned}
$$

where $g$ and $h$ are linear functions that are used to describe, respectively, inequality and equality constraints. Some relevant examples of constrained problems are the knapsack problem [12], capacitated arc routing problems [5] or graph partitioning problem [15].

Constrained problems introduce a challenging characteristic in the definition of the solutions in the search space: feasibility. A solution $\mathbf{x}$ is feasible if it holds all the constraints (functions $g$ and $h$ ), otherwise it is unfeasible. It must be noted that the codification used to describe the solutions may induce solutions that are unfeasible. For instance, if the codification used to formalize solutions of size $n$ is the binary coding, then the set of all solutions that fit in the codification are all the binary vectors of size $n\left(2^{n}\right.$ in total). Nonetheless, many of those solutions might be unfeasible, and thus, procedures that discriminate between feasible and unfeasible solutions are needed within the algorithms.

This point represents a serious drawback for EDAs, since these algorithms learn a probability distribution defined on the whole set of solutions induced

by the codification (either feasible or unfeasible solutions), and then the new solutions are sampled from that distribution. As a consequence, both type of solutions are usually generated. In this sense, in the case of EDAs, in order to hold the feasibility of the solutions, three trends have been followed: (1) repair unfeasible solutions, (2) use penalty functions to punish unfeasible solutions ${ }^{1}$, or (3) implement sampling procedures that update the probability distribution while constructing the solutions [18]. When following any of these trends, the behavior of EDAs is somehow denaturalized as the obtained sample of solutions does not follow the probability distribution defined at that iteration.

Works in the literature with regard to the design of EDAs for solving permutation problems have shown that introducing probability models defined exclusively on the space of feasible solutions (the set of all permutations of a given size) can be a step forward in terms of performance [2]. Inspired by that work, recently, Ceberio et al. [4] proposed a lattice-based probability model defined exclusively on the set of feasible solutions of the 2-partition balanced Graph Partitioning Problem (GPP). Despite its novelty, the proposed approach is adhoc for that problem, and can hardly be extended to other problems.

Based on the work of Irurozki [8] on probability models for permutation spaces, in this manuscript we address constrained problems in the framework of EDAs following a more general research line: design and implement new distancebased exponential probability models that define a probability distribution on the set of feasible solutions. In order to design such types of models, there are three key aspects related to the model to consider, and it is desirable to give computationally accurate, and efficient, implementations: (1) calculate the probability of any $x$ in $\Omega$ (feasible set), (2) given a set $\left\{\mathbf{x}^{1}, \ldots, \mathbf{x}^{n}\right\}$ of solutions, estimate the parameters of the probability model, and (3) sample solutions given the parameters of the probability model.

With illustrative purposes, we consider the GPP as a case of study (in Sect.2). Then, in Sect.3, one by one we address the three key-aspects enumerated above. In Sect. 4, we carried out a set of experiments to evaluate the performance of the proposed EDA. Lastly, conclusions and future works are listed in Sect. 5 .

# 2 Graph Partitioning Problem 

The Graph Partitioning Problem (GPP) is the problem of finding a $k$-partition of the vertices of a graph while minimizing the number (or sum of weights) of the edges between sets [15]. Among its many variants, in this paper we considered the balanced 2-partition case, i.e., a solution for the problem groups the vertices into two sets of equal size. So, any solution is encoded as a binary vector $\mathbf{x} \in\{0,1\}^{n}$, where $x_{i}$ indicates the set to which vertex $i$ is assigned, $n$ stands for the size of the problem, and is subject to the restriction of having the same number of zeros

[^0]
[^0]:    ${ }^{1}$ Trends (1) and (2) have been proposed for a broad range of algorithms that include EDAs.

and ones, i.e., $\sum_{i=1}^{n} x_{i}=n / 2$. Taking this restriction into account, the search space of solutions $\Omega$ is composed of $\binom{n}{n / 2}$ binary vectors.

Given a weighted undirected graph $G=(V, E)$ with $n=|V|$ vertices, and the weights $w_{i j}$ between each pair of vertices in $G$, the objective function is calculated as the total weight of the edges between the sets (sum of the weights of the edges in the cut), and it is denoted as

$$
f(\mathbf{x})=\sum_{i=1}^{n} \sum_{j=1}^{n} x_{i}\left(1-x_{j}\right) w_{i j}
$$

Figure 1 introduces a GPP instance of $n=8$, where two solutions are illustrated. As we can see, $\mathbf{x}^{1}$ is better than $\mathbf{x}^{2}$ since the sum of the weights of the edges of the cut (in bold) is lower: $f\left(\mathbf{x}^{1}\right)=1+3$ and $f\left(\mathbf{x}^{2}\right)=2+2+1$.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Example of $n=8$ instance of GPP with two different solutions $\mathbf{x}^{1}$ and $\mathbf{x}^{2}$.

The GPP is a very well-known constrained problem and has been studied extensively. When the problem is balanced (as in our case), the problem is NPhard [1]. This problem is present in many real world applications [14], in fields such as tracking areas in cellular networks [19] or image segmentation [7].

# 3 Distance-Based Exponential Model 

Let us consider a distance-based exponential probability model $P$ defined on a finite (or infinite countable) domain of solutions $\Omega$. Under this model, the probability value of every solution in the domain, $x \in \Omega$, is calculated as

$$
P(x)=\frac{e^{-\theta d(x, \bar{x})}}{\psi(\theta)}
$$

where $\psi(\theta)$ is the normalization constant, $\theta$ denotes the spread of the distribution, and $d(x, \bar{x})$ is the distance of $x$ to a reference solution $\bar{x}$.

This model assigns every solution $x$ a probability that decays exponentially with respect to its distance to $\bar{x}$. When $\theta$ equals 0 , the model assigns equal probability to every solution in $\Omega$. The larger the value of $\theta$, the more concentrated the distribution becomes around the reference solution.

As previously mentioned, in order to introduce a model of this type in EDAs to deal with constrained problems, there are three key aspects that are mandatory to be solved efficiently. First, we need to calculate the probability of any given solution in $\Omega$, i.e., compute Eq. 1, in closed form. Next, given a set of solutions, it is necessary to calculate the parameters of the model: $\theta$ and $\bar{x}$. In this work, we decided to calculate their maximum likelihood estimators (MLE). Finally, given the parameters of the model, we need to be able to obtain a sample of solutions that follows the inferred probability distribution.

It is worth remarking that, as EDAs are iterative algorithms, and learning/sampling procedures are repeated innumerable times in that framework, developing low complexity methods for each procedure is critical for the general feasibility of the algorithm. For the sake of illustrating the approach presented in this manuscript, we considered the balanced 2-partition GPP as a case of study, and we individually address each of the three key aspects described above.

# 3.1 A Case of Study: The Graph Partitioning Problem 

The first decision to make is the election of the distance-metric $d$, which directly depends on the codification of solutions. As described in Sec. 2, the solutions of the 2-balanced GPP are codified as binary vectors of size $n$ with an equal number of zeros as ones. Among binary vectors, the most natural distancemetric is the Hamming distance, i.e., given two solutions $x$ and $y$, the Hamming distance is calculated as $d_{H}(x, y)=\sum_{i=1}^{n} \mathbf{1}_{[x(i) \neq y(i)]}$. It is worth noting that the codification employed to describe the solutions is highly redundant. For instance, the solutions $x^{1}=(0,0,0,1,1,1)$ and $x^{2}=(1,1,1,0,0,0)$ are equal. One is a relabeling of the other, but in terms of the Hamming distance, they are at maximum distance from each other. Therefore, we define a new distance for this case that is based on the Hamming distance.

Definition 1. Let $x$ be a solution for a 2-balanced GPP problem, and $\neg x$ is the negated or complementary solution of $x$, then the distance-metric $d(x, \bar{x})$ is calculated as

$$
d(x, \bar{x})=\min \left\{d_{H}(x, \bar{x}), d_{H}(\neg x, \bar{x})\right\}
$$

Under this metric, the maximum distance $K$ to which a solution can be defined is $\lfloor n / 2\rfloor$. The minimum distance is 0 (when $x$ or $\neg x$, are equal to $\bar{x}$ ). Solutions can only be at paired distances in order to hold the constraint of the balanced 2-partition case. The number of solutions at distance $k$ (being $k$ even) is $\binom{n / 2}{k / 2}^{2}$. Note that each possible solution can be coded with two different binary vectors (one the negation of the other).

Computing the Probability Value. Given a solution $x$ and the parameters $\theta$ and $\bar{x}$, computing $P(x)$ is given by an efficient computation of the normalization constant $\psi(\theta)$. This function, which is roughly computed as

$$
\psi(\theta)=\sum_{y \in \Omega} e^{-\theta d(y, \bar{x})}
$$

considering the previous observations, can be reformulated as follows:

$$
\psi(\theta)=\sum_{l=0}^{K / 2}\binom{n / 2}{l}^{2} e^{-\theta 2 l}
$$

Learning. Given a set $\mathbf{x}=\left\{x^{1}, \ldots, x^{N}\right\}$ of solutions, the learning step consists of estimating the parameters of the proposed model: $\bar{x}$ and $\theta$. In this work, we decided to estimate the MLE of the parameters. To that end, we define the likelihood expression as

$$
L(\theta, \bar{x} \mid \mathbf{x})=\prod_{i=1}^{N} \frac{e^{-\theta d\left(x_{i}, \bar{x}\right)}}{\psi(\theta)}
$$

The aim is to find the parameters that maximize that function. To that end, we apply the logarithm, as calculus is more simple, but the MLE parameters are not affected. So we have the function

$$
\log L(\theta, \bar{x} \mid \mathbf{x})=-\theta N \bar{d}-N \log \left[\sum_{l=0}^{K / 2}\binom{n / 2}{l}^{2} e^{-\theta 2 l}\right]
$$

where $\bar{d}=\frac{1}{N} \sum_{i=1}^{N} d\left(x_{i}, \bar{x}\right)$.
The term related to the estimation of $\bar{x}$ is independent to that of $\theta$, so by minimizing $\sum_{i=1}^{N} d\left(x_{i}, \bar{x}\right)$, the likelihood is maximized. Thus, first we define the computation of $\bar{x}$ as

$$
\bar{x}=\arg \min _{x \in \Omega} \sum_{i=1}^{N} d\left(x_{i}, x\right)
$$

Such an estimation is an optimization task itself. Therefore, we propose estimating $\bar{x}$ as in [3]. First, we calculate the average values at each position individually in the $N$ solutions, and next, the $\mathrm{n} / 2$ positions with largest values in the resulting vector are assigned 1 , and the rest 0 .

Once the $\bar{x}$ is estimated, the MLE of the spread parameter $\theta$ is calculated. In order to find the maximum value of $\theta$ that maximizes Eq. 2, we compute its derivative and equate it to 0 :

$$
-N \bar{d}+N \frac{\sum_{l=0}^{K / 2}\binom{n / 2}{l}^{2} 2 l e^{-\theta 2 l}}{\sum_{l=0}^{K / 2}\binom{n / 2}{l}^{2} e^{-\theta 2 l}}=0
$$

and finally,

$$
\sum_{l=0}^{K / 2}\binom{n / 2}{l}^{2}(2 l-\bar{d}) e^{-\theta 2 l}=0
$$

$\theta$ cannot be calculated exactly from Eq. 3 and, thus, we propose using numerical methods, such as Newton-Raphson [3] to estimate it.

Sampling. Once the parameters of the model have been estimated, the next step in EDAs is to sample a set of solutions that follow the probability distribution defined by the parameters calculated in the previous step. In this case, we propose using a distance-based sampling algorithm based on the following two statements [8]: (1) every solution has the same number of solutions at each distance, and (2) every solution at same distance from $\bar{x}$ has same probability.

First, a distance $k=2 l$ at which generate a solution is sampled. The probability under the proposed model to generate a solution at distance $k$ is

$$
P(k)=\sum_{x \mid d(x, \bar{x})=k} P(x)=\binom{n / 2}{k / 2}^{2} \frac{e^{-\theta k}}{\psi(\theta)}
$$

Once $k$ has been decided, we generate uniformly at random one solution among those at distance $k$ from the reference solution $\bar{x}$. To that end, we choose u.a.r. $\mathrm{k} / 2$ zeros and $\mathrm{k} / 2$ ones, and the chosen items are bit-flipped.

# 4 Experiments 

The experimental study has been organized in two parts. First, the feasible ranges to estimate the $\theta$ parameter are calculated. Then, a performance evaluation of the EDA on a benchmark of instances of GPP is carried out.

### 4.1 Feasible Ranges for $\theta$

In order to incorporate the model to the framework of EDAs, and avoid scenarios in which the proposed model is not suitable for optimization, the spread parameter $\theta$ needs to be controlled in a range of feasible values. To that end, we calculate for different $n=\{124,250,500,1000\}$, in the range $[0,10]$ for $\theta$ with step size 0.1 , the probability assigned to the reference solution. Results are introduced in Fig. 2.

Without performing previous experiments, for each problem size, we set the lower and upper bounds that assign to $\bar{x}$ the probabilities $10^{-9}$ and 0.1 respectively. The values are presented in Table 1.

### 4.2 Performance Analysis

In order to obtain some hints about the performance of the proposed exponential probability model (abbreviated as Exp) for solving the GPP, we carried some experiments on the set of 22 GPP instances [9]. In addition, with comparison purposes, we included three EDAs in the analysis: the univariate marginal distribution algorithm (UMDA) [16], the tree EDA (Tree) [17] and the Lattice EDA [4] (Lattice). The UMDA assumes that the n-dimensional joint probability distribution factorizes as a product of n univariate and independent probability distributions ${ }^{2}$. The second EDA, Tree, estimates, at each iteration, a dependency-tree

[^0]
[^0]:    ${ }^{2}$ Despite this strong assumption, due to its good general performance and low time consumption it is appropriate to include UMDA as baseline in the experimentation.

![img-1.jpeg](img-1.jpeg)

Table 1. Lower and upper bounds for the estimation of $\theta$ parameters.

Fig. 2. Probability assigned to $\bar{x}$ for different $n$ and $\theta$.
which encodes conditional dependencies between the problem variables. Finally, in [4], the authors of the paper made the first attempt of developing EDAs for constrained COPs, and proposed a square lattice probability model to optimize the GPP.

As this is a preliminary work, we considered using the same parameter settings as in [4]:

- Population size is set to 10 n .
- 5 n solutions are selected to learn the probabilistic model.
- At each iteration, 10 n solutions are sampled.
- A maximum number of $100 \mathrm{n}^{2}$ evaluations are considered as the stopping criterion.

Equally, the initial population is generated uniformly at random.

Particular Settings of the Exponential EDA. A preliminary analysis of the quality of the reference solution estimated at the learning step pointed out that the proposed method, although it provides MLE of the reference solution $\bar{x}$, it is not competitive. In this sense, we decided to set the best solution of the population as $\bar{x}$.

In addition, as sampling at distance 0 provides the reference solution, we avoid sampling at this distance. Finally, due to convergence and diversity considerations, the solutions that do not exist in the population are only accepted when sampling.

Results. Results are presented in Table 2 as Average Relative Percentage Deviation (ARPD) and Average Execution Times (AET) of 10 executions of each algorithm-instance pair.

Looking at the results, we can conclude that with regard to the ARPD, Tree is the best performing algorithm followed by Lattice and Exp. Finally, UMDA

Table 2. ARPD and AET results for Johnson's benchmark instances. The results in bold denote the approach with the lowest ARPD and AET. $\left(^{*}\right)$ denotes the instances in which $10^{6}$ evaluations were used instead of $100 n^{2}$.
is the worst performing algorithm. Note that Exp obtained the best result in three of the largest instances while it is by far the fastest algorithm for all sizes considered.

# 5 Conclusions and Future Work 

In this work we proposed using distance-based exponential probability models defined exclusively on the set of feasible solutions. In this sense, we took as a case of study the 2-balanced Graph Partitioning Problem, and designed step by step a probability model to be used in the framework of EDAs. In addition, some experiments to fine-tune the probability model have also been carried out.

Finally, in order to evaluate the performance of the proposed algorithm, some benchmark experiments were carried out. Results revealed that the proposed methodology is a promising research line for future work.

In this work, we used an heuristic method to calculate the reference solution $\bar{x}$ as it is a cheap algorithm to approach the estimation problem. However, we have no intuition about its precision, in this sense, for the future, we should (1) perform experiments to estimate its accuracy, and (2) investigate other estimation methods for MLE of $\bar{x}$.

Regarding the experimental study, in future research, we aim to provide a more general experimental study in which the parameters of the compared algorithms are fined-tuned, and are evaluated on a larger benchmark of instances. We also consider to hybridize Exp in order to perform a fair comparison of the algorithms.
