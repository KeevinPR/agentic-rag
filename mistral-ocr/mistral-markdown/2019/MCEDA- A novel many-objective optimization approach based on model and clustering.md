# MCEDA: A novel many-objective optimization approach based on model and clustering 

Xiaoxu Duan<br>Central South University, Changsha, Hunan 410075, China

## H I G H L I G H T S

- Propose a new framework of estimation of distribution algorithms (EDAs), MCEDA.
- Propose a new promising estimation model, the bits model.
- Extend the application of EDAs to solve many-objective optimization problems.
- Combine clustering and decomposition strategy in evolutionary algorithms.


## ARTICLE INFO

## Article history:

Received 10 September 2017
Received in revised form 26 September 2018
Accepted 19 October 2018
Available online 24 October 2018

## Keywords:

Many-objective optimization
Estimation of distribution algorithm
Clustering
Evolutionary algorithm

## A B S T R A C T

To solve many-objective optimization problems (MaOPs) by evolutionary algorithms (EAs), the maintenance of convergence and diversity is essential and difficult. Improved multi-objective optimization evolutionary algorithms (MOEAs), usually based on the genetic algorithm (GA), have been applied to MaOPs, which use the crossover and mutation operators of GAs to generate new solutions. In this paper, a new approach, based on decomposition and the MOEA/D framework, is proposed: model and clustering based estimation of distribution algorithm (MCEDA). MOEA/D means the multi-objective evolutionary algorithm based on decomposition. The proposed MCEDA is a new estimation of distribution algorithm (EDA) framework, which is intended to extend the application of estimation of distribution algorithm to MaOPs. MCEDA was implemented by two similar algorithm, MCEDA/B (based on bits model) and MCEDA/RM (based on regular model) to deal with MaOPs. In MCEDA, the problem is decomposed into several subproblems. For each subproblem, clustering algorithm is applied to divide the population into several subgroups. On each subgroup, an estimation model is created to generate the new population. In this work, two kinds of models are adopted, the new proposed bits model and the regular model used in RM-MEDA (a regularity model based multi-objective estimation of distribution algorithm). The nondominated selection operator is applied to improve convergence. The proposed algorithms have been tested on the benchmark test suite for evolutionary algorithms (DTLZ). The comparison with several state-of-the-art algorithms indicates that the proposed MCEDA is a competitive and promising approach.
(c) 2018 Elsevier B.V. All rights reserved.

## 1. Introduction

Evolutionary multi-objective optimization (EMO) algorithms have performed very well in different two and three objective optimization problems, while the theory proof of its convergence and diversity is insufficient [1,2]. Many engineering optimization problems have been solved with the help of multi-objective optimization evolutionary algorithms (MOEAs) [3-6]. For example, during designing a certain construction, the civil engineer may

[^0]seek after the minimal total cost, the minimal danger coefficient, the maximal available space and the maximal stiffness.

However, when it comes to many-objective optimization problems (MaOPs), it is difficult to maintain the convergence and diversity. Most MOEAs are based on the selection directed by domination relation. As Kalyanmoy Deb et al. say, the proportion of nondominated solutions in the population tends to be very large which will slow down the search process considerably as the number of objectives increases [7]. This will make the non-domination based algorithms extremely confused where to go since most algorithms rely on the domination relation among solutions to guide the search process. Also many evolution algorithms cannot maintain


[^0]:    E-mail address: siaoxuduan@outlook.com.

enough diversity, faced with MaOPs, which may result in local optimal solutions or even wrong answer.

While most EAs simply adopt the traditional genetic operators (e.g., crossover and mutation), estimation of distribution algorithms (EDAs), trying to generate the new solutions more reasonably, direct the search process of the Pareto fronts by building explicit probabilistic models of the promising candidate solutions and generating new solutions from those estimation models [8]. Although EDAs have successfully solved many problems, they are mainly used to handle problems with discrete variables and low number of objectives [9]. As Luis Marti et al. point out, the traditional EDAs have several shortcomings: handling the data outliers in a wrong way, losing diversity and too complex to compute [10].

In this paper, a new approach (MCEDA), utilizing estimation models and clustering strategy, is proposed to deal with manyobjective optimization problems. MCEDA is based on decomposition and the MOEA/D framework [11], [12]. It mainly focuses on unconstrained MaOPs at present. In MCEDA, the problem is decomposed into several subproblems. To deal with each subproblem, the population is divided into several clusters and the estimation model is built for each cluster. Then new solutions are generated from the estimation models. Non-dominated selection, which has been used in non-dominated sorting genetic algorithm III (NSGAIII) [7], [13], is adopted to select the candidate solutions from all new solutions. The candidate solutions are compared with the solutions of the current population to determine whether the current solutions should be replaced or not so as to update the whole population. Since the search progress is directed by both decomposition and estimation models, the data outliers can be handled and the population diversity is maintained well.

The main new contributions of this paper are listed as follows.
(1) Propose a new EDA framework, MCEDA. The traditional EDA framework may be too ideal when it comes to complex problems, e.g. MaOPs.
(2) Propose a new estimation model, the bits model. It is a promising model according to the experiments.
(3) Extend the application of EDAs to MaOPs. A few attempts have been made to applied the EDAs to MaOPs. In this work, the new proposed EDAs prove to be qualified to solve the MaOPs.
(4) Combine clustering and decomposition strategy. In this paper, the new proposed EDA framework utilizes both the clustering and decomposition procedure, which has not been tried.

The remaining of this paper is organized as follows. In Section 2, the related work and some background concepts are described. Section 3 presents the MCEDA in detail. Experimental studies with parameter studies and comparison to other algorithms are reported in Section 4. And finally, Section 5 presents the conclusions.

## 2. Related work and preliminaries

In this section, current research about MaOPs, EDAs and decomposition are introduced. And for the sake of completeness, some background concepts are presented.

### 2.1. Many-objective optimization

An unconstrained multi-objective optimization problem (MOOP) can be defined as follows [14]. And many-objective optimization problems (MaOPs) are defined as problems with four or more objectives [7].

$$
\begin{array}{ll}
\text { Minimize } f_{i}(\boldsymbol{x}), & j=1,2, \ldots, m \\
\text { subject to } x_{i}^{(L)} \leq x_{i} \leq x_{i}^{(U)}, & i=1,2, \ldots, n
\end{array}
$$

A solution $\boldsymbol{x}$ is a vector of $n$ decision variables: $\boldsymbol{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)^{T}$. The corresponding objective value is $\boldsymbol{f}=\left(f_{1}(\boldsymbol{x}), f_{2}(\boldsymbol{x}), \ldots, f_{m}(\boldsymbol{x})\right)^{T}$. The last set of constraints are called variable bounds. The decision space is formed by all the variables constituted by the variable bounds.

A solution $\boldsymbol{x}^{(1)}$ is said to dominate the other solution $\boldsymbol{x}^{(2)}$, if both following conditions are true:
(1) $f_{i}\left(\boldsymbol{x}^{(1)}\right) \leq f_{j}\left(\boldsymbol{x}^{(2)}\right)$ for all $j=1,2, \ldots, m$.
(2) $f_{i}\left(\boldsymbol{x}^{(1)}\right)<f_{j}\left(\boldsymbol{x}^{(2)}\right)$ for at least one $j \in{1,2, \ldots, m}$.

Among a set of solutions $\boldsymbol{P}$, the non-dominated set of solution $\boldsymbol{P}$ are those that are not dominated by any member of the set $\boldsymbol{P}$.

MOEAs have been widely used in real-world applications [3], [6]. However, most domination based MOEAs find difficulties in solving many-objective optimization problems, since the selection ability is reduced considerably with rising number of objectives $[15], 7,16]$.

To deal with MaOPs, a number of many-objective evolutionary algorithms (MaOEAs) have been proposed. Bingdong Li et al., according to the key operator, categorized MaOEAs into seven classes [2]: relaxed dominance based, diversity-based, aggregationbased, indicator-based, reference set based, preference-based and dimensionality reduction approaches. Hernán Aguirre and Kiyoshi Tanaka proposed a method to search effectively on MaOPs by partitioning the objective space into subspaces and they used an adaptive $\epsilon$-ranking procedure to re-rank solution [17]. Convergence and diversity of the solutions can be improved remarkably on 4 to 10 objectives. Hisao Ishibuchi et al. examined two different algorithms: NSGA-II [1] and MOEA/D [11]. According to their computational experiments, when it comes to large populations, NSGA-II showed inefficient while MOEA/D performed well [18]. Xiaofang Guo et al. employed PAM clustering algorithm to identify redundant objectives [19]. Non-dominated sorting genetic algorithm III (NSGA-III), proposed by Kalyanmoy Deb et al., is a reference-point-based MaOEA based on NSGA-II framework, which uses reference points and clustering operator to maintain the population diversity and convergence [7]. And constrained non-dominated relation is applied in constrained MaOPs in their subsequent work [20]. Clustering-ranking evolutionary algorithm (crEA) implements clustering and ranking sequentially to improve convergence and diversity [21]. Xinye Cai et al. proposed a new variant of MOEA/D with sorting-and-selection (MOEA/D-SAS) in which decomposition-based-sorting (DBS) and angle-basedselection (ABS) was used to maintain the balance between convergence and diversity [22]. In their experiments, MOEA/D-SAS performed very well. Huanlai Xing et al. proposed a modified multi-objective evolutionary algorithm based on decomposition (MOEA/D-PBIL) [23], which is based on the multi-objective evolutionary algorithm based on decomposition (MOEA/D) and the population based incremental learning (PBIL) [24]. The MOEA/D-PBIL is intended to solve a specific multi-objective optimization problem in the context of multicasting with network coding and the problem have three objectives. Jing Bai et al. proposed a multi-objective artificial bee algorithm (MOABC) which is based on decomposition by PBI method [25]. They apply artificial bee colony algorithm to enhance the performance and the experimental results show that MOABC outperforms others. Yuyan Han et al. proposed an evolutionary multi-objective robust scheduling algorithm (REMO) to deal with the flow shop scheduling problems in the presence of machine breakdowns [26]. Their experimental results show that REMO can tackle the blocking lot-streaming flow shop scheduling problems very well. Xiangwei Zheng et al. proposed a novel multiobjective group search optimizer based on multiple producers and crossover operator of genetic algorithm (MCGSO) [27]. Experimental results show that MCGSO is effective and efficient. Junqing Li et al. proposed an energy-aware multi-objective optimization

algorithm (EA-MOA) to solve hybrid flow shop (HFS) scheduling problem when the setup energy consumptions are considered [28]. The experimental results show that EA-MOA is highly effective, compared with other efficient algorithms.

### 2.2. Estimation of distribution algorithms

As mentioned before, most MaOEAs are based on genetic algorithms (GAs). GAs are optimization methods based on the mechanics of artificial selection and genetic recombination operators [9], while estimation of distribution algorithms (EDAs) based optimization algorithms direct the search of the optimum by building and sampling explicit probabilistic models of promising candidate solutions [8]. The estimation model is used to capture the probability distribution of the promising, which is the most important feature of EDAs [29]. However, it is not intended to exactly represent the population, which could be very time consuming and almost impossible, but instead to build an estimation model that can generate better solutions. The basic procedure of traditional EDA is described in Algorithm 1 [8].

```
Algorithm 1. Basic procedure of traditional EDA
    \(\mathbf{t} t \leftarrow 0 ;\)
    2 Generate population \(P(0)\) of random solutions;
    3 while termination criteria not satisfied do
    4 Evaluate all candidate solutions in \(P(t)\);
    5 Select promising solutions \(S(t)\) from \(P(t)\);
    6 Build a probabilistic model \(M(t)\) for \(S(t)\);
    7 Generate new solutions \(O(t)\) by sampling \(M(t)\);
    8 Create \(P(t+1)\) by combining \(O(t)\) and \(P(t)\);
    \(t \leftarrow t+1 ;\)
    10 return
```

Many traditional EDAs are focus on solving problems with discrete variables (e.g., Bayesian network based EDAs [30-34,9, $35,36]$ ). However, solutions for many problems are represented by continuous variables. According to Mark Hauschild and Martin Pelikan's survey, there are two primary approaches to applying EDAs to problems with continuous variables: map the continuous variables into discrete domain and use a discrete EDA to solve it or use EDAs designed for continuous variables [29]. The selection method also has an important impact on the performance of EDAs. J.R. Caldwell et al. analyzed two different selection method used in EDAs: filter selection and constructive selection [37]. And the results show that constructive selection can significantly improve the EDAs' performance. Marcella S. R. Martins et al. proposed the heuristic selection based on estimation of distribution algorithm (HSEDA), which considers EDA as a heuristic selection technique [38]. The HSEDA performs well at the traveling thief problem in their experiments. Tudor Dan Mihoc proposed a new estimation of distribution algorithm, which is intended to detect a sample of Nash equilibria for games [39]. Murilo Zangari et al. proposed a multi-objective decomposition-based EDA using Kernels of Mallows models (MEDA/D-MK) to deal with multi-objective permutation-based optimization problems [40]. MEDA/D-MK outperforms others in their experiments. Fergal Lane et al. introduced a bivariate model for discrete EDAs, based on dichotomized Gaussian models (DICE) [41]. And DICE turns out to be competitive compared with other EDAs in their experiments.

Many EDAs have emerged in the past several decades [42,34, $9,43,35,36]$. RM-MEDA, a regularity model based multi-objective estimation of distribution algorithm, employs the local principal component analysis algorithm to build the estimation model at each generation [44]. A non-dominated sorting based selection is used for choosing solutions for the next generation [44]. Li Mo et al.
employed elitist strategy theory to improve RM-MEDA, using part of the parent population with better performance instead of the entire parent population to establish a more accurate manifold [45]. Yangyang Li et al. introduced local learning to improve the local search ability of RM-MEDA, which obtained much better convergence capability according to their experiments [46]. The Bayesian optimization algorithm (BOA), proposed by Martin Pelikan et al., estimates the distribution of promising solutions by Bayesian network to generate new candidate solutions, which mainly used to solve problems with discrete variables [47,34]. Other models have also been used. The naive MIDEA, proposed by Peter A.N. Bosman and Dirk Thierens, performed well in their experiments. C-Multi, a competent multi-swarm approach for many-objective problems, is based on a particle swarm optimization (PSO) algorithm and an EDA [48]. The PSO algorithm is applied to discover the Pareto front and divide different regions. The EDA used in C-Multi is the realcoded Bayesian optimization algorithm (rBOA) [43], focusing on convergence to its allocated region. It performed very well in their experiments. Yanan Sun et al. proposed a reference line-based estimation of distribution algorithm for many-objective optimization problems (MaOEDA/RL) /citeRN3270. MaOEDA/RL samples new solutions with the help of generated uniformly distributed reference points and performs well in their experiments. Luis Marti et al. proposed a scalable multi-objective optimization with a neural network-based estimation of distribution algorithm (MONEDA), which utilizes a modified growing neural gas network for modelbuilding (MB-GNG) [49,50]. MONEDA performs better than others in their experiments.

### 2.3. Decomposition

MOEA/D, proposed by Qingfu Zhang et al., uses decomposition strategy to decompose MOOPs [11]. In their paper, three approaches to decompose MOOPs are introduced: weighted sum approach, Tchebycheff approach and boundary intersection (BI) approach. In this paper, the proposed MCEDA is based on MOEA/D, in which the Tchebycheff approach is adopted. In the Tchebycheff approach, the original problem is decomposed into $N$ subproblems as follows [11].
$\operatorname{minimize} g\left(\boldsymbol{x} \mid \lambda^{j}, \boldsymbol{z}^{*}\right) ;$

$$
g\left(\boldsymbol{x} \mid \lambda^{j}, \boldsymbol{z}^{*}\right)=\max _{1 \leq i \leq m}\left(\lambda_{i}^{j}\left|f_{i}(x)-z_{i}^{*}\right|\right)
$$

subject to $\boldsymbol{x} \in \Omega$.
where $m$ is the number of objectives of the problem and $\boldsymbol{z}^{*}=$ $\left(z_{1}^{*}, \ldots, z_{m}^{*}\right)^{T}$ is the ideal point, i.e., $z_{i}^{*}=\min \left\{f_{i}(x) \mid x \in \Omega\right\}$ for each $i=1, \ldots, m . \lambda^{j}=\left(\lambda_{1}^{j}, \lambda_{2}^{j}, \ldots, \lambda_{m}^{j}\right)^{T}, j=1,2, \ldots, N$, is the weight vector. For each Pareto optimal solution $\boldsymbol{x}^{*}$ of Eq. (1), there is a corresponding weight vector $\lambda^{j}$ and vice versa. Therefore, different Pareto optimal solutions can be obtained by solving the single objective optimization problems generated by varying the weight vectors [12]. This is how the Tchebycheff approach works.

## 3. Proposed algorithm

### 3.1. Framework of the proposed algorithm

The framework of the proposed MCEDA is summarized in Algorithm 2, which is different from most other EDAs. To begin with, the problem is decomposed into several subproblems [11,12]. The initial population $P_{0}$, whose size is assigned with the number of the size of weights vector, are randomly generated and the ideal point $\boldsymbol{z}^{*}$ are initialized. Then the normalization is applied to the population. For a solution $\boldsymbol{x}$, the normalized objective value is defined as [21]
$\tilde{f}_{i}(\boldsymbol{x})=\frac{f_{i}(\boldsymbol{x})-z_{i}^{*}}{z_{j}^{\max }-z_{j}^{*}}, j=1,2, \ldots, m$

Table 1
Mean and standard deviation values of IGD, obtained by MCEDA/B on DTLZ instances.

| Crossover parameter | Obj. | 0.5 | 0.1 | 0.8 |
| :--: | :--: | :--: | :--: | :--: |
| DTLZ1 | 3 | $\begin{aligned} & 2.76 E-04_{8,30E-06} \\ & 2.63 E-03_{1,30E-06} \\ & 1.62 E-03_{5,30 E-05} \end{aligned}$ | $\begin{aligned} & 2.79 E-03_{8,30 E-05}(-) \\ & 2.11 E-02_{2,30 E-05}(-) \\ & 9.47 E-03_{4,30 E-05}(-) \\ & 2.97 E-03_{3,30 E-04}(+) \end{aligned}$ | $\begin{aligned} & 2.67 E-04_{1,30 E-05}(+) \\ & 2.63 E-03_{5,30 E-05}(-) \\ & 1.64 E-03_{6,40 E-05}(-) \end{aligned}$ |
|  | 10 | $\begin{aligned} & 3.05 E-03_{2,30 E-04} \\ & 6.45 E-03_{3,30 E-03} \end{aligned}$ | $\begin{aligned} & 2.97 E-03_{3,30 E-04}(+) \\ & 1.19 E-02_{6,40 E-05}(-) \end{aligned}$ | $\begin{aligned} & 3.58 E-03_{8,20 E-04}(-) \\ & 4.65 E-03_{1,50 E-03}(+) \end{aligned}$ |
|  | 3 | $\begin{aligned} & 4.12 E-04_{1,90 E-05} \\ & 1.49 E-03_{8,30 E-05} \end{aligned}$ | $\begin{aligned} & 4.28 E-04_{1,30 E-05}(-) \\ & 1.97 E-03_{4,30 E-04}(-) \end{aligned}$ | $\begin{aligned} & 4.22 E-04_{3,40 E-05}(-) \\ & 1.58 E-03_{1,50 E-04}(-) \end{aligned}$ |
|  | 8 | $\begin{aligned} & 4.63 E-03_{9,70 E-04} \\ & 5.45 E-03_{1,30 E-03} \end{aligned}$ | $\begin{aligned} & 4.65 E-03_{3,40 E-04}(-) \\ & 4.37 E-03_{9,30 E-04}(+) \end{aligned}$ | $\begin{aligned} & 4.09 E-03_{3,40 E-04}(+) \\ & 5.45 E-03_{1,30 E-03}(-) \end{aligned}$ |
|  | 15 | $\begin{aligned} & 2.58 E-03_{6,30 E-04} \\ & 8.65 E-04_{1,30 E-05}(-) \end{aligned}$ | $\begin{aligned} & 2.25 E-03_{4,30 E-04}(+) \\ & 2.14 E-02_{1,90 E-05}(-) \end{aligned}$ | $\begin{aligned} & 3.16 E-03_{7,80 E-04}(-) \\ & 8.99 E-04_{7,00 E-05}(-) \end{aligned}$ |
| DTLZ3 | 5 | $\begin{aligned} & 8.42 E-03_{4,30 E-03} \\ & 9.10 E-03_{1,30 E-03} \end{aligned}$ | $\begin{aligned} & 1.73 E-02_{6,20 E-03}(-) \\ & 5.72 E-03_{1,40 E-03}(+) \end{aligned}$ | $\begin{aligned} & 4.93 E-03_{3,70 E-05}(+) \\ & 9.45 E-03_{1,60 E-03}(-) \end{aligned}$ |
|  | 10 | $\begin{aligned} & 5.51 E-03_{2,80 E-03} \\ & 1.90 E-02_{6,80 E-03} \end{aligned}$ | $\begin{aligned} & 6.84 E-03_{4,30 E-05}(-) \\ & 2.46 E-02_{8,60 E-05}(-) \end{aligned}$ | $\begin{aligned} & 4.97 E-03_{3,00 E-05}(+) \\ & 2.76 E-02_{8,50 E-05}(-) \end{aligned}$ |
| DT1Z4 | 3 | $\begin{aligned} & 1.07 E-02_{3,00 E-03} \\ & 1.08 E-02_{3,80 E-03} \end{aligned}$ | $\begin{aligned} & 1.45 E-02_{3,60 E-05}(-) \\ & 1.11 E-02_{4,00 E-05}(-) \end{aligned}$ | $\begin{aligned} & 8.17 E-03_{7,90 E-05}(+) \\ & 8.26 E-03_{4,20 E-05}(+) \end{aligned}$ |
|  | 8 | $\begin{aligned} & 6.51 E-03_{1,70 E-03} \\ & 1.03 E-02_{6,60 E-04} \end{aligned}$ | $\begin{aligned} & 5.72 E-03_{1,40 E-05}(+) \\ & 8.06 E-03_{5,60 E-04}(+) \end{aligned}$ | $\begin{aligned} & 7.34 E-03_{9,50 E-04}(-) \\ & 1.23 E-02_{1,70 E-05}(-) \end{aligned}$ |
| DT1Z5 | 15 | $\begin{aligned} & 7.07 E-03_{4,60 E-04} \\ & 3.98 E-05_{3,90 E-05}(-) \end{aligned}$ | $\begin{aligned} & 6.36 E-03_{2,40 E-04}(-) \\ & 4.55 E-05_{3,50 E-05}(-) \end{aligned}$ | $\begin{aligned} & 8.10 E-03_{4,70 E-04}(-) \\ & 3.91 E-05_{2,40 E-05}(+) \end{aligned}$ |
| DT1Z6 | 3 | $\begin{aligned} & 2.22 E-03_{2,00 E-04} \\ & 2.79 E-03_{3,20 E-04}(-) \end{aligned}$ | $\begin{aligned} & 2.20 E-03_{1,30 E-04}(+) \\ & 2.97 E-03_{2,20 E-04}(-) \end{aligned}$ | $\begin{aligned} & 2.33 E-03_{2,00 E-04}(-) \\ & 3.06 E-03_{4,00 E-04}(-) \end{aligned}$ |
|  | 15 | $\begin{aligned} & 1.07 E-03_{1,10 E-04} \\ & 3.98 E-05_{3,90 E-05}(-) \end{aligned}$ | $\begin{aligned} & 1.02 E-03_{6,40 E-05}(+) \\ & 4.55 E-05_{3,50 E-05}(-) \end{aligned}$ | $\begin{aligned} & 1.20 E-03_{1,60 E-04}(-) \\ & 3.91 E-05_{2,40 E-05}(+) \end{aligned}$ |
| DT1Z7 | 3 | $\begin{aligned} & 2.14 E-03_{1,00 E-04} \\ & 3.43 E-03_{6,20 E-04} \end{aligned}$ | $\begin{aligned} & 2.66 E-03_{2,50 E-04}(-) \\ & 3.27 E-03_{6,00 E-04}(+) \end{aligned}$ | $\begin{aligned} & 2.23 E-03_{1,30 E-04}(-) \\ & 3.25 E-03_{5,80 E-04}(+) \end{aligned}$ |
|  | 10 | $\begin{aligned} & 5.11 E-03_{1,20 E-03} \\ & 3.44 E-03_{6,30 E-05} \end{aligned}$ | $\begin{aligned} & 4.70 E-03_{7,70 E-04}(+) \\ & 3.43 E-03_{6,00 E-05}(+) \end{aligned}$ | $\begin{aligned} & 5.80 E-03_{1,70 E-03}(-) \\ & 3.37 E-03_{2,70 E-04}(+) \end{aligned}$ |
| DT1Z8 | 3 | $\begin{aligned} & 1.65 E-03_{3,10 E-03} \\ & 7.95 E-03_{1,90 E-03} \end{aligned}$ | $\begin{aligned} & 4.64 E-03_{5,20 E-03}(-) \\ & 7.35 E-03_{4,10 E-03}(+) \end{aligned}$ | $\begin{aligned} & 1.65 E-03_{3,20 E-03}(-) \\ & 6.25 E-03_{3,60 E-03}(+) \end{aligned}$ |
|  | 8 | $\begin{aligned} & 7.74 E-03_{1,30 E-03} \\ & 1.30 E-02_{1,80 E-03} \end{aligned}$ | $\begin{aligned} & 5.22 E-03_{6,00 E-04}(+) \\ & 9.79 E-03_{3,50 E-04}(+) \end{aligned}$ | $\begin{aligned} & 1.03 E-02_{2,00 E-03}(-) \\ & 1.40 E-02_{1,20 E-03}(-) \end{aligned}$ |
|  | 15 | $\begin{aligned} & 1.08 E-02_{3,70 E-04} \end{aligned}$ | $\begin{aligned} & 7.99 E-03_{1,60 E-04}(+) \\ & 7.99 E-03_{1,60 E-04}(+) \end{aligned}$ | $\begin{aligned} & 1.20 E-02_{1,50 E-03}(-) \end{aligned}$ |

The symbol " + " and " - " denote whether the IGD results of the algorithm with the compared parameter are better than or worse than that of the algorithms with the first parameter value according to the mean value and standard deviation.
where $z_{i}^{\max }$ is the maximum value for every objective $f_{j}$ in the population. The weight vectors are created recursively under the conditions as follows.
$\lambda^{j}=\left(\lambda_{1}^{j}, \lambda_{2}^{j}, \ldots, \lambda_{m}^{j}\right)^{T}, j=1,2, \ldots, N$
$\sum_{i=1}^{m} \lambda_{i}^{j}=1, \lambda_{i}^{j} \in[0,1]$.
Each weight vector $\lambda^{j}$ is related to a subproblem and a solution $S$ which has the best fitness for the subproblem in terms of the solutions have been evaluated and compared.

The fitness is represented as follows [12].
fitness $(S)=\max _{1 \leq i \leq m}\left\{\lambda_{i}\left|f_{i}(x)-z_{i}^{*}\right|\right\}$
The solution with the smaller fitness value is better.
For each subproblem, the neighborhood type $N t$ is randomly chose from Neighbor and Public, which will be used in the updating population procedure. The neighborhood relationship among all the subproblems is defined based on the distances of their weight vectors which is developed by Zhang et al. [11]. The current solution set $P_{t}$ is normalized to generate $P n_{t}$. Then the nondominated solution set $P n_{t}$ is selected from $P n_{t}$. Then $P n_{t}$ is divided into $m$ clusters $C_{t}$ according to the Euclidean distances between the objective values of the solutions by k means. For each cluster, a estimation model is built to generate new solutions, used to form $Q_{t}$. Here, a new proposed bits model and the regular model from RM-MEDA [44] are used to estimate the new solutions Section 3.3. During the model procedure, the generated solutions, whose
variables exceed the variable bounds, will be dropped. And a new solution will be generated until the specified amount of new solutions is filled. To focus on the current subproblem, the new solutions $Q_{t}$ are crossed with the current solution which relates to the current subproblem to obtain $Q c_{t}$. The uniform crossover operator from differential evolution is adopted [51]. In order to explore more decision space, $Q c_{t}$ is mutated to get $Q c m_{t}$. The polynomial mutation is used here. And the non-dominated solutions $Q c m s_{t}$ are selected from the mutated solutions $Q c m_{t}$. For each solution in $Q c m s_{t}, z^{*}$ is updated according to following principle, which have been described in Section 2.3. $\boldsymbol{z}^{*}=\left(z_{1}^{*}, \ldots, z_{m}^{*}\right)^{T}$ is the ideal point, i.e., $z_{i}^{*}=\min \left\{f_{i}(x) \mid x \in \Omega\right\}$ for each $i=1, \ldots, m$. Then, compared with the fitness of the non-dominated solutions, the current population $P_{t}$ is updated to generate the next population $P_{t+1}$. Finally, the algorithm will terminate when the number of the evaluation reaches the max.

The reason why the normalization is used here is to make the algorithm more robust, i.e. 1) to avoid the too large or to small value of the objective function misleads the direction of the selection 2) and to avoid the too large value exceeds the scope the computer can hold. It would be better to add the normalization operator before line 21 in Algorithm 2 as well. However, thinking about the small amount of the new generated solutions and to make the algorithm more concise, the normalization operator is not added before line 21 in Algorithm 2.

The main difference between MCEDA and MOEA/D is the way to generate new solutions. While MOEA/D uses operators of the differential evaluation, MCEDA generate new solutions by clustering and modeling procedure.

## Algorithm 2. The framework of MCEDA

Input: $P_{t}$ : the problem; $N$ : the size of population and weight vectors; $m$ : the number of the objectives; $n$ : the number of the variables of the problem; MaxRSS: the max RSS in k means; MaxIterations: the max iterations in k means;
$1 P_{0} \leftarrow$ initializePopulation( $N$ );
$2 P_{0} \leftarrow$ evaluatePopulation $\left(P_{0}\right)$;
3 Update evaluation number;
$4 z^{*} \leftarrow$ initializeldealPoint();
$5 P_{0} \leftarrow$ normalize( $\left.P_{0}\right)$;
$6 \lambda \leftarrow$ generateWeight $(N)$;
$7 N b \leftarrow$ initialNeighborhood $(\lambda)$;
8 while termination criteria not satisfied do randomly permutate subproblem;
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25 return subproblems do
Id $\leftarrow$ subproblemId;
$N t \leftarrow$ RandomlyChooseNeighborType();
$P n_{t} \leftarrow$ normalize( $\left.P_{t}, z_{t}^{*}\right)$;
$P s_{t} \leftarrow$ nonDominatedSelect( $\left.P n_{t}\right)$;
$C_{t} \leftarrow$ generateClusters( $\left.P s_{t}, m\right.$, MaxIterations, MaxRSS);
$Q_{t} \leftarrow$ modeling $\left(C_{t}, m\left(C_{t}\right), n\right)$;
$Q c_{t} \leftarrow$ crossover $\left(Q_{t}, I d\right)$;
$Q c m_{t} \leftarrow$ mutate $\left(Q c_{t}\right)$;
$Q c m_{t} \leftarrow$ evaluatePopulation $\left(Q c m_{t}\right)$;
Update evaluation number;
Qcms $_{t} \leftarrow$ nonDominatedSelect $\left(Q c m_{t}\right)$;
foreach solution in Qcms, do
$z_{t+1}^{*} \leftarrow$ updateldealPoint(solution);
$P_{t+1} \leftarrow$
updatePopulation $\left(P_{t}\right.$, solution, Id, Nt, $\left.\lambda, z_{t+1}^{*}, N b\right)$;
// see Algorithm 3;
26 return

## Algorithm 3. Update population [11]

Input: $P_{t}$ : the previous population; $S$ : the new solution; Id: the subproblem number; Nt: the neighborhood type; $\lambda$ : the weight vectors; $z_{t+1}^{*}$ : the updated ideal point; Nb : the neighborhood;
Output: $P_{t+1}$ : the new population;
if $\mathrm{Nt} \Leftrightarrow$ "Neighbor" then
Update only the solutions which are the neighbor of the solution corresponding to the subproblem Id;
Compare the new solution with the neighbor solution, the one has a smaller fitness is retained;
And the max number of solutions to be updated is limited to two;
else
Update all the solutions in $P_{t}$;
Compare the new solution with each solution in $P_{t}$, the one has a smaller fitness is retained;
And the max number of solutions to be updated is limited to two;
return the updated population as $P_{t+1}$;

### 3.2. Clustering algorithm

Several clustering strategies have been used [21,52,19,53,36, 54-56] and comparison was conducted as well [57]. Castro et al. compared different clustering strategy for MaOPs: clustering in decision space, objective space or both [57]. After experimental

| $x_{1}^{1}$ | $\rightarrow 1$ | 0 | 1 | $\ldots 1$ |
| :--: | :--: | :--: | :--: | :--: |
| $x_{1}^{2}$ | $\rightarrow 0$ | 1 | 1 | $\ldots 0$ |
| $x_{1}^{3}$ | $\rightarrow 1$ | 0 | 0 | $\ldots 1$ |
| $\ldots$ |  |  |  |  |
| $x_{1}^{n}$ | $\rightarrow 1$ | 0 | 1 | $\ldots 1$ |
|  | $\downarrow$ | $\downarrow$ | $\downarrow$ | $\ldots \downarrow$ |
|  | $P_{1}$ | $P_{2}$ | $P_{3}$ | $\ldots P_{n b}$ |
|  | $\downarrow$ | $\downarrow$ | $\downarrow$ | $\ldots \downarrow$ |
|  | 0 | 1 | 1 | $\ldots 0$ |
|  |  | $\downarrow$ |  |  |
|  |  | $x_{\text {new }}^{1}$ |  |  |

Fig. 1. Generating a new variable in bits model.
study, they recommended clustering the solutions in the objective space although they concluded that the best choice of clustering space can be impacted by specific properties of the problem. Castro et al. also compared the results obtained when use different clustering metrics, after which they recommended to use the Euclidean distance since it was the most robust in their comparison.

Therefore, in this paper, $m$ (i.e., the objective number) clusters of solutions $C_{t}$ are created from $P s_{t}$ by the k means clustering algorithm as a result of comparing the Euclidean distance between solutions. The Euclidean distance between $\boldsymbol{x}$ and $\boldsymbol{y}$ can be defined by [58]
distance $=\left(\sum\left|x_{i}-y_{i}\right|^{p}\right)^{1 / r}$
where $p=r=2$.
The max iterations of $k$ means is set to $m$ and the residual sum of squares (RSS) is set to MaxRSS. Only if the iteration number is less than $m$, the residual sum of squares is greater than MaxRSS and the new generated mean vector is different from the previous one, will the k means iteration continue. Otherwise, it will terminate.

### 3.3. Estimation model

A too complicated model is not affordable and is not necessary, because modeling procedure needs to be conducted at each generation of the EAs [44]. And it is almost impossible to build a complete exact estimation model. In this paper, to deal with continuous MaOPs, two models are used to build estimation models for each cluster: a new estimation model based on bits probability (MCEDA/B) and the model adopted in RM-MEDA (MCEDA/RM).

### 3.3.1. Bits model

The principle of bits model is inspired by the Bayesian optimization algorithm (BOA) [34] which uses conditional probability and Bayesian network to estimate and that is mainly applied to problems with discrete variables. In bits model, the decision variables $\boldsymbol{X}=\left(X_{1}, \ldots, X_{n}\right)$ are assumed to be independent each other. Notes that the bits model is different from BOA since the BOA builds model based on the connection among the variables while the bits model simply assumes they are independent. That is to say
$P(\boldsymbol{X}=\boldsymbol{x})=P\left(X_{1}=x_{1}\right) P\left(X_{2}=x_{2}\right) \ldots P\left(X_{n}=x_{n}\right)$
The variables of each solution are transferred into a set of bits. Each bit is represented by ' 0 ' or ' 1 '. All the bits are assumed to be independent each other. Then the probability distribution of each bit is used to generate the new variable. The reason why make this transform is in the hope of exploring more information from the solution sets as BOA has done. Experiments have shown that the new solutions generated by the bits model is explosive which can

![img-0.jpeg](img-0.jpeg)

Fig. 2. Plots for the solution set in the best run obtained by MCEDA/B (first row) and MCEDA/RM (second row) on 3 objectives DTLZ problems.
cover enough decision space. In this section, a simple version of bits model is presented. The number of the bits of each variable is represented by $n b$.

In a solution set $P$, the $i$ th solution $S_{i}$ can be represented by its decision variables, $\left(x_{i}^{1}, x_{i}^{2}, \ldots, x_{i}^{n}\right)$. The formula transferring a double variable $x$ to the corresponding binary $x b$ is presented as follows.
$x b=\operatorname{toBinary}\left(\operatorname{round}\left(\frac{\left(x-\text { lowLimit }\right)\left(2^{n b}-1\right)}{\text { upperLimit }- \text { lowLimit }}\right)\right)$
where lowLimit and upperLimit are the variable bounds of the variable $x$, which depend on the specific problem, round $(d)$ obtains the closest integer of $d$ and toBinary $(t)$ transfers the integer $t$ to the corresponding binary.

And the formula transferring a binary $x b$ to the corresponding double variable $x$ is presented below.
$x=\frac{\operatorname{toInteger}(x b)(\text { upperLimit }- \text { lowLimit })}{\left(2^{n b}-1\right)}+\operatorname{lowLimit}$
where toInteger $(b)$ transfers the binary $b$ to the corresponding integer.

For example, the procedure of generating the first variable $x_{\text {new }}^{1}$ of the new solution $S_{\text {new }}$ from a solution set $P$ is illustrated in Fig. 1. In the figure, $x_{i}^{1}$ represents the first decision variable of the $i$ th solution of $P$. First, $x_{i}^{1}$ is mapped to binary according to Eq. (8). Then the probability of the occurrence of ' 1 ' of the $j$ th column $p_{j}$ is calculated. To generate new variable, the new bits are generated at the probability of $p$ and the new bits is mapped to the new variable $x_{\text {new }}^{1}$ by Eq. (9).

All the new generated variables $\left(x_{\text {new }}^{1}, x_{\text {new }}^{2}, \ldots, x_{\text {new }}^{n}\right)$ are combined together to construct a new solution $S_{\text {new }}$. The model procedure is introduced in Algorithm 4.

### 3.3.2. Regular model

The RM-MEDA showed prominent performance in their experiments and it has been improved by latter researches [46], [45].

In RM-MEDA, the model is built with the help of local principal component analysis (PCA) algorithm [59] under the assumption of Karush-Kuhn-Tucker condition. They assume that, with the search going on, the population in the decision space in an EA will approximate the Pareto Set (PS) (i.e., the decision variables of the corresponding Pareto Front) and be uniformly distribute around the PS, from which they make the assumption that the points in the population, whose centroid is the PS, are independent observations of a random vector $\xi \in R^{n}$.
$\xi=\zeta+\varepsilon$
where $\zeta$ is uniformly distributed over a piecewise continuous ( $\mathrm{m}-$ 1)-dimensional manifold. $\varepsilon \sim N\left(0, \sigma_{I}\right)$ is an $n$-dimensional zeromean noise vector, where $I$ is the $n \times n$ identity matrix and $\sigma_{I}>0$.

The modeling procedure is briefly described and the pseudocode is presented in Algorithm 5. Here is a detailed description of Algorithm 5. In this work, the regular model is applied to generate models for each cluster. For a certain solution cluster $C_{i}^{1}$, to begin with, it is partitioned into several sub clusters $S_{1}, S_{2}, \ldots, S_{n}$ by the local PCA algorithm [59], where the partition number $h$ is adaptively defined according to $C_{i}^{1}$. In this work, the partition number is simply set to one since the local PCA is time consuming. Then, each sub cluster is modeled by Eq. (10). Before generating new solutions, the mean of $S_{i}(\bar{x}(i, j))$, the covariance matrix of the points in $S_{i}(\operatorname{Cov}(i, j))$ should be calculated. Then, the sorted eigenvalue of $\operatorname{Cov}(i, j)(\lambda(i, j))$, i.e., $\lambda(i, j)(1,1) \geq \lambda(i, j)(2,2) \geq \cdots \geq \lambda(i, j)(n, n)$, is calculated. The eigenvector of $\operatorname{Cov}(i, j)(\mathrm{U}(\mathrm{i}, \mathrm{j}))$, corresponding to $\lambda(i, j)$, is calculated as well. Now it is ready to generate the new solutions. The total number of new solutions to be generated is $m\left(C_{i}\right)$, and for each cluster in $C_{i}\left(C_{i}^{1}\right) \cdot n_{i} \leftarrow\left(m\left(C_{i}\right)\right) \frac{\left(C_{i}^{1}\right)}{n_{i} n}$ solutions is generated. For each cluster in $S\left(S_{i}\right), n_{i} \frac{\left(S_{i}\right)}{(S_{i}^{1})}$ new solutions are generated. And here is how to generate one new solution based on the previous calculation.
$\boldsymbol{x}_{\text {new }}=\Psi(i, j)+\varepsilon_{j}^{\prime}$

![img-2.jpeg](img-2.jpeg)

Fig. 3. Variation of IGD metric value with MCEDA/B, MCEDA/RM, NSGA-III and MOEA/D on four DTLZ instances with 8 objectives.
![img-2.jpeg](img-2.jpeg)

Fig. 4. Variation of IGD metric value with RM-MEDA on four DTLZ instances with 8 objectives.
where $\Psi(i, j)=\overline{\boldsymbol{x}}(i, j)+\sum_{w=1}^{m-1} \alpha_{w} U(i, j)(:, w)$, in which $\overline{\boldsymbol{x}}(i, j)$ is the mean of $S_{j}$ and $\alpha_{w}$ is calculated in line 16 to line 18. $\varepsilon_{j}^{\prime}$ is a random value generated by normal distribution number where mean equals 0 and $\sigma_{j}$ is the standard deviation. $\sigma_{j}$ has been calculated in line 20.

The new population $Q_{i}$ is formed by all the new solutions. For more details of the regular model, readers are referred to the original papers [59], [44].

### 3.4. Computational complexity

Before analyzing the computational complexity of the proposed approach, some symbols are defined first. $N$ is the population size. $m$ is the number of the objectives of the problem. $n$ is the number of the variables of the problem. And, in order to simplify the analysis, the solutions in each cluster is assumed to be $N / m . N$ is usually greater than $m$ and $n$. In Algorithm 2, the initialization process from

![img-3.jpeg](img-3.jpeg)

Fig. 5. Parallel coordinate plots for the solution set in the best run obtained by MCEDA/B (first row), MCEDA/RM (second row), NSGA-III (third row) and MOEA/D (fourth row) on 10 objectives DTLZ problems.
line 1 to line 7 , requires $O\left(N+N+1+N m+N m+N+N^{2}\right)$ computations, i.e., $O\left(N^{2}\right)$. The while loop from line 8 to line 24 will stop when the maximum evaluations is reached. And line 9 requires $O(N)$ computations. The for loop from line 10 to line 24 will be executed $N$ times. Line 11 to line 15 requires $O(1+$
$1+m N+N^{2}+m^{2} N)$ computations, i.e., $O\left(N^{2}\right)$. Line 16 requires $O\left(N^{2} / m\right)$ computations for Algorithm 4 of MCEDA/B and $O(m N)$ computations for Algorithm 5 of MCEDA/RM. Line 17 to line 21 requires $O\left(m^{2} n+m^{2} n+m^{2}+1+m^{4}\right)$ computations, i.e., $O\left(2 m^{2} n+\right.$ $\left.m^{4}\right)$. The for loop from line 22 to line 24 will be executed less than or

![img-4.jpeg](img-4.jpeg)

Fig. 6. Parallel coordinate plots for the solution set in the best run obtained by RM-MEDA on 10 objectives DTLZ problems.

Table 2
Mean and standard deviation values of IGD, obtained by MCEDA/RM on DTLZ instances.

| Crossover parameter | Obj. | 0.5 | 0.1 | 0.8 |
| :--: | :--: | :--: | :--: | :--: |
| DTLZ1 | 3 | $\begin{aligned} & 5.97 E-03_{1.50 E-03} \\ & 2.93 E-03_{2.30 E-03} \\ & 4.81 E-03_{5.70 E-04} \\ & 4.38 E-03_{7.90 E-04}(+) \end{aligned}$ | $\begin{aligned} & 7.50 E-03_{2.80 E-03}(-) \\ & 1.75 E-03_{3.00 E-04}(+) \\ & 4.38 E-03_{7.90 E-04}(+) \\ & 4.49 E-03_{4.90 E-04}(-) \end{aligned}$ | $\begin{aligned} & 5.43 E-03_{1.40 E-03}(+) \\ & 1.84 E-03_{3.00 E-04}(+) \\ & 4.65 E-03_{6.20 E-04}(+) \\ & 4.63 E-03_{4.20 E-04}(-) \end{aligned}$ |
|  | 15 | 8.01E-03 $3_{7.20 E-04}$ | $7.56 E-03_{7.20 E-04}(+)$ | $8.07 E-03_{6.00 E-04}(-)$ |
|  | 3 | $\begin{aligned} & 3.36 E-04_{2.00 E-05} \\ & 3.47 E-03_{2.90 E-04} \\ & 5.41 E-03_{7.20 E-04} \\ & 10 \end{aligned}$ | $\begin{aligned} & 3.22 E-04_{1.10 E-05}(+) \\ & 3.22 E-03_{4.80 E-04}(+) \\ & 4.82 E-03_{5.90 E-04}(+) \end{aligned}$ | $\begin{aligned} & 3.37 E-04_{2.30 E-05}(-) \\ & 3.53 E-03_{4.20 E-04}(-) \\ & 5.08 E-03_{7.90 E-04}(+) \\ & 4.31 E-03_{8.00 E-04}(+) \end{aligned}$ |
|  | 15 | 4.19E-03 $3_{3.90 E-04}$ | $4.40 E-03_{5.50 E-04}(-)$ | $4.48 E-03_{5.00 E-04}(-)$ |
| DTLZ3 | 3 | $\begin{aligned} & 1.25 E-02_{4.10 E-03} \\ & 3.72 E-03_{1.00 E-04} \\ & 8 \end{aligned}$ | $\begin{aligned} & 1.23 E-02_{2.40 E-03}(+) \\ & 3.88 E-03_{3.90 E-04}(-) \\ & 9.30 E-03_{1.50 E-03}(+) \end{aligned}$ | $\begin{aligned} & 1.39 E-02_{2.10 E-03}(-) \\ & 3.79 E-03_{3.10 E-04}(-) \\ & 9.28 E-03_{2.30 E-03}(+) \end{aligned}$ |
|  | 10 | 9.55E-03 $3_{1.40 E-03}$ | $9.19 E-03_{4.00 E-04}(+)$ | $9.33 E-03_{1.50 E-03}(+)$ |
|  | 15 | $1.19 E-02_{8.10 E-04}$ | $1.16 E-02_{7.00 E-04}(+)$ | $1.17 E-02_{6.50 E-04}(+)$ |
|  | 3 | $\begin{aligned} & 4.73 E-03_{6.30 E-03} \\ & 2.80 E-03_{7.90 E-03} \\ & 7.06 E-03_{6.20 E-04} \end{aligned}$ | $\begin{aligned} & 4.54 E-03_{6.30 E-03}(+) \\ & 3.78 E-03_{3.90 E-03}(-) \\ & 6.86 E-03_{5.40 E-04}(+) \end{aligned}$ | $\begin{aligned} & 4.04 E-03_{5.00 E-03}(+) \\ & 3.15 E-03_{3.60 E-04}(-) \\ & 6.97 E-03_{4.60 E-04}(+) \end{aligned}$ |
|  | 10 | 8.96E-03 $3_{2.60 E-04}$ | $9.22 E-03_{4.30 E-04}(-)$ | $9.09 E-03_{4.40 E-04}(-)$ |
|  | 15 | $1.42 E-02_{3.40 E-04}$ | $1.43 E-02_{3.60 E-04}(-)$ | $1.41 E-02_{4.00 E-04}(+)$ |
| DTLZ5 | 3 | $\begin{aligned} & 2.01 E-05_{1.80 E-06} \\ & 2.27 E-03_{1.90 E-04} \\ & 8 \end{aligned}$ | $\begin{aligned} & 2.17 E-05_{7.60 E-06}(-) \\ & 2.21 E-03_{1.90 E-04}(+) \end{aligned}$ | $\begin{aligned} & 2.22 E-05_{8.30 E-06}(-) \\ & 2.16 E-03_{1.50 E-04}(+) \end{aligned}$ |
|  | 8 | 4.10E-03 $3_{4.20 E-04}$ | $3.99 E-03_{3.20 E-04}(+)$ | $4.10 E-03_{3.60 E-04}(-)$ |
|  | 10 | $5.35 E-03_{4.20 E-04}$ | $5.41 E-03_{5.50 E-04}(-)$ | $5.74 E-03_{7.80 E-04}(-)$ |
|  | 15 | $7.41 E-03_{4.00 E-04}$ | $7.63 E-03_{3.60 E-04}(-)$ | $7.32 E-03_{3.30 E-04}(+)$ |
|  | 3 | $9.14 E-03_{1.00 E-03}$ | $8.12 E-03_{1.50 E-03}(+)$ | $9.04 E-03_{1.50 E-03}(+)$ |
|  | 5 | $1.84 E-03_{3.50 E-04}$ | $1.66 E-03_{2.20 E-04}(+)$ | $1.77 E-03_{4.10 E-04}(+)$ |
|  | 8 | $3.51 E-03_{8.50 E-04}$ | $3.43 E-03_{4.60 E-04}(+)$ | $3.60 E-03_{5.40 E-04}(-)$ |
|  | 10 | $2.87 E-03_{3.50 E-04}$ | $3.38 E-03_{6.30 E-04}(-)$ | $3.08 E-03_{4.70 E-04}(-)$ |
|  | 15 | $3.62 E-03_{3.30 E-04}$ | $3.52 E-03_{2.90 E-04}(+)$ | $3.58 E-03_{6.60 E-04}(+)$ |
|  | 3 | $6.63 E-03_{4.10 E-03}$ | $3.79 E-03_{4.20 E-03}(+)$ | $6.15 E-03_{4.40 E-03}(+)$ |
|  | 5 | $3.89 E-03_{1.50 E-03}$ | $3.66 E-03_{5.40 E-04}(+)$ | $3.61 E-03_{6.00 E-04}(+)$ |
| DTLZ7 | 8 | $6.51 E-03_{1.90 E-04}$ | $6.64 E-03_{2.00 E-04}(-)$ | $6.54 E-03_{2.60 E-04}(-)$ |
|  | 10 | $7.98 E-03_{6.80 E-05}$ | $7.95 E-03_{1.10 E-04}(+)$ | $7.98 E-03_{1.60 E-04}(-)$ |
|  | 15 | $1.16 E-02_{2.20 E-04}$ | $1.14 E-02_{1.00 E-04}(+)$ | $1.16 E-02_{1.60 E-04}(-)$ |

The symbol " + " and "-" denote whether the IGD results of the algorithm with the compared parameter are better than or worse than that of the algorithms with the first parameter value according to the mean value and standard deviation.
equal to $m^{2}$ times. Line 23 requires $O(m)$ computations. And line 24 requires $O(N+N m)$ computations. The for loop from line 22 to line 24 requires $O\left(m^{3} N\right)$ computations. To execute the while loop from line 8 to line 24 once, the MCEDA/B requires $O\left(N\left(N^{2}+N^{2} / m+\right.\right.$ $\left.2 m^{2} n+m^{4}+m^{3} N\right)$ ) computations and the MCEDA/RM require $O\left(N\left(N^{2}+m N+2 m^{2} n+m^{4}+m^{3} N\right)\right)$ computations, so that both the MCEDA/B and the MCEDA/RM requires $O\left(N^{3}+m^{3} N\right)$ computations when calculating the while loop once. The number of times that the while loop will be executed is depended on the max evaluations of parameter setting.

## 4. Experimental study

In this section, some parameter studies are conducted to show the performance of the proposed approach at a wide range of parameters. And the proposed MCEDA/B and MCEDA/RM are applied to the benchmark test suite for evolutionary algorithms (DTLZ) [60]. All algorithms are coded in Java and the experiments is conducted in the jMetal ${ }^{1}$ platform [61-63]. The test results are compared with NSGA-III, MOEA/D and RM-MEDA.

[^0]
[^0]:    1 jMetal: https://jmetal.github.io/jMetal/.

Table 3
Mean and standard deviation values of IGD, obtained by MCEDA/B on DTLZ instances.

| Number of bits | Obj. | 16 | 8 | 30 |
| :--: | :--: | :--: | :--: | :--: |
|  | 3 | $4.37 \mathrm{E}-04_{1.10 E-05}$ | $4.78 \mathrm{E}-03_{1.98 E-03}(-)$ | $4.38 \mathrm{E}-04_{4.30 E-06}(-)$ |
|  | 5 | $3.79 \mathrm{E}-03_{1.98 E-03}$ | $1.15 \mathrm{E}-02_{1.60 E-03}(-)$ | $2.85 \mathrm{E}-03_{1.98 E-04}(+)$ |
| DTLZ1 | 8 | $2.40 \mathrm{E}-03_{1.98 E-04}$ | $6.87 \mathrm{E}-03_{1.20 E-03}(-)$ | $2.26 \mathrm{E}-03_{7.30 E-05}(+)$ |
|  | 10 | $4.93 \mathrm{E}-03_{1.86 E-04}$ | $8.21 \mathrm{E}-03_{1.30 E-03}(-)$ | $4.97 \mathrm{E}-03_{2.10 E-04}(-)$ |
|  | 15 | $5.99 \mathrm{E}-03_{1.98 E-03}$ | $8.93 \mathrm{E}-03_{1.40 E-03}(-)$ | $7.41 \mathrm{E}-03_{4.00 E-03}(-)$ |
|  | 3 | $3.41 \mathrm{E}-04_{3.30 E-05}$ | $3.75 \mathrm{E}-04_{3.10 E-05}(-)$ | $3.32 \mathrm{E}-04_{2.20 E-05}(+)$ |
|  | 5 | $1.76 \mathrm{E}-03_{2.10 E-04}$ | $1.77 \mathrm{E}-03_{2.60 E-04}(-)$ | $1.84 \mathrm{E}-03_{2.96 E-04}(-)$ |
| DTLZ2 | 8 | $4.80 \mathrm{E}-03_{1.20 E-03}$ | $4.32 \mathrm{E}-03_{8.10 E-04}(+)$ | $4.88 \mathrm{E}-03_{9.80 E-04}(-)$ |
|  | 10 | $7.08 \mathrm{E}-03_{1.10 E-03}$ | $6.29 \mathrm{E}-03_{9.50 E-04}(+)$ | $7.72 \mathrm{E}-03_{5.70 E-04}(-)$ |
|  | 15 | $3.02 \mathrm{E}-03_{5.30 E-04}$ | $2.68 \mathrm{E}-03_{3.70 E-04}(+)$ | $3.16 \mathrm{E}-03_{6.10 E-04}(-)$ |
|  | 3 | $1.56 \mathrm{E}-03_{1.20 E-06}$ | $2.29 \mathrm{E}-02_{2.20 E-03}(-)$ | $1.55 \mathrm{E}-03_{3.40 E-06}(+)$ |
|  | 5 | $2.16 \mathrm{E}-02_{3.10 E-03}$ | $3.61 \mathrm{E}-02_{2.00 E-03}(-)$ | $2.54 \mathrm{E}-02_{7.00 E-03}(-)$ |
| DTLZ3 | 8 | $1.35 \mathrm{E}-02_{2.00 E-03}$ | $1.37 \mathrm{E}-02_{1.10 E-03}(-)$ | $1.66 \mathrm{E}-02_{6.60 E-03}(-)$ |
|  | 10 | $9.80 \mathrm{E}-03_{5.40 E-04}$ | $1.30 \mathrm{E}-02_{1.30 E-03}(-)$ | $9.48 \mathrm{E}-03_{6.10 E-04}(+)$ |
|  | 15 | $6.63 \mathrm{E}-03_{5.40 E-04}$ | $8.10 \mathrm{E}-03_{5.00 E-03}(-)$ | $6.37 \mathrm{E}-03_{2.30 E-04}(+)$ |
|  | 3 | $8.53 \mathrm{E}-03_{3.10 E-03}$ | $8.98 \mathrm{E}-03_{5.70 E-03}(-)$ | $1.36 \mathrm{E}-02_{2.70 E-03}(-)$ |
|  | 5 | $1.13 \mathrm{E}-02_{3.10 E-03}$ | $1.08 \mathrm{E}-02_{3.60 E-03}(+)$ | $9.92 \mathrm{E}-03_{5.80 E-03}(+)$ |
| DTLZ4 | 8 | $6.06 \mathrm{E}-03_{1.60 E-03}$ | $6.49 \mathrm{E}-03_{1.00 E-03}(-)$ | $6.29 \mathrm{E}-03_{9.60 E-04}(-)$ |
|  | 10 | $1.21 \mathrm{E}-02_{1.10 E-03}$ | $1.18 \mathrm{E}-02_{4.40 E-04}(+)$ | $1.26 \mathrm{E}-02_{2.20 E-03}(-)$ |
|  | 15 | $8.39 \mathrm{E}-03_{5.70 E-04}$ | $8.71 \mathrm{E}-03_{4.00 E-04}(-)$ | $8.10 \mathrm{E}-03_{5.40 E-04}(+)$ |
|  | 3 | $1.99 \mathrm{E}-05_{1.00 E-05}$ | $2.55 \mathrm{E}-05_{7.40 E-06}(-)$ | $2.74 \mathrm{E}-05_{1.10 E-05}(-)$ |
|  | 5 | $2.35 \mathrm{E}-03_{4.50 E-04}$ | $2.11 \mathrm{E}-03_{5.40 E-04}(+)$ | $1.75 \mathrm{E}-03_{3.30 E-04}(+)$ |
| DTLZ5 | 8 | $1.93 \mathrm{E}-03_{1.80 E-04}$ | $2.01 \mathrm{E}-03_{2.70 E-04}(-)$ | $1.96 \mathrm{E}-03_{1.90 E-04}(-)$ |
|  | 10 | $2.49 \mathrm{E}-03_{2.40 E-04}$ | $2.64 \mathrm{E}-03_{3.20 E-04}(-)$ | $2.48 \mathrm{E}-03_{2.90 E-04}(+)$ |
|  | 15 | $1.15 \mathrm{E}-03_{6.40 E-05}$ | $1.15 \mathrm{E}-03_{7.10 E-05}(-)$ | $1.14 \mathrm{E}-03_{1.10 E-04}(+)$ |
|  | 3 | $2.66 \mathrm{E}-05_{1.00 E-05}$ | $2.96 \mathrm{E}-05_{1.30 E-05}(-)$ | $2.49 \mathrm{E}-05_{2.20 E-05}(+)$ |
|  | 5 | $2.06 \mathrm{E}-03_{1.90 E-04}$ | $2.04 \mathrm{E}-03_{2.50 E-04}(+)$ | $2.12 \mathrm{E}-03_{1.80 E-04}(-)$ |
| DTLZ6 | 8 | $2.83 \mathrm{E}-03_{4.00 E-04}$ | $3.08 \mathrm{E}-03_{6.70 E-04}(-)$ | $2.86 \mathrm{E}-03_{2.20 E-04}(-)$ |
|  | 10 | $5.33 \mathrm{E}-03_{1.80 E-03}$ | $5.16 \mathrm{E}-03_{9.20 E-04}(+)$ | $4.90 \mathrm{E}-03_{1.10 E-03}(+)$ |
|  | 15 | $2.19 \mathrm{E}-03_{2.50 E-04}$ | $2.17 \mathrm{E}-03_{3.10 E-04}(+)$ | $2.25 \mathrm{E}-03_{3.40 E-04}(-)$ |
|  | 3 | $2.77 \mathrm{E}-03_{4.50 E-03}$ | $1.70 \mathrm{E}-03_{3.30 E-03}(+)$ | $2.76 \mathrm{E}-03_{4.50 E-03}(+)$ |
|  | 5 | $7.30 \mathrm{E}-03_{2.80 E-03}$ | $8.41 \mathrm{E}-03_{2.20 E-03}(-)$ | $7.27 \mathrm{E}-03_{3.50 E-03}(+)$ |
| DTLZ7 | 8 | $8.44 \mathrm{E}-03_{1.40 E-03}$ | $1.02 \mathrm{E}-02_{1.50 E-03}(-)$ | $1.03 \mathrm{E}-02_{1.20 E-03}(-)$ |
|  | 10 | $1.42 \mathrm{E}-02_{1.30 E-03}$ | $1.40 \mathrm{E}-02_{1.60 E-03}(+)$ | $1.51 \mathrm{E}-02_{7.40 E-04}(-)$ |
|  | 15 | $1.02 \mathrm{E}-02_{3.30 E-04}$ | $1.05 \mathrm{E}-02_{5.70 E-04}(-)$ | $1.05 \mathrm{E}-02_{6.10 E-04}(-)$ |

The symbol " + " and "-" denote whether the IGD results of the algorithm with the compared parameter are better than or worse than that of the algorithms with the first parameter value according to the mean value and standard deviation.

### 4.1. Test sets

The scalable test problems DTLZ, proposed by Kalyanmoy Deb et al. [60], have been widely used to test MOEAs. In their paper, three test problem construction approaches are suggested and DTLZ1 $\sim$ DTLZ9 are proposed. Test problem DTLZ1 has a linear Pareto front (PF). And DTLZ3 has many local Pareto fronts and one global Pareto fronts in order to investigate an MOEA's ability to converge to the global PF. DTLZ4 is designed to investigate an MOEA's ability to maintain a good distribution of solutions. Both DTLZ5 and DTLZ6 have a curve PF. And DTLZ7 has a disconnected set of Pareto-optimal regions, which tests an algorithm's ability to maintain subpopulation in different Pareto-optimal regions. In this work, the 3 to 15 objectives DTLZ1, DTLZ2, DTLZ3, DTLZ4, DTLZ5, DTLZ6 and DTLZ7 are tested. The number of variables are set to $(m+k-1)$, where $m$ is the number of objectives and $k=5$ for DTLZ1, while $k=10$ for DTLZ2, DTLZ3, DTLZ4, DTLZ5 and DTLZ6, and $k=20$ for DTLZ7 [7]. Table 6 illustrates the test setting.

### 4.2. Performance metrics

The inverse generational distance (IGD) metric [7] is chosen as the performance metric, since it can provide a combined information about the convergence and diversity of the obtained solutions. It measures the distances between the optimal solution set, obtained by EAs, and the computed approximated Pareto front [61].

It can be defined as follows.
$I G D=\frac{\sqrt{\sum_{i=1}^{n} d_{i}^{2}}}{n}$
where $n$ is the number of solutions in the optimal solution set, obtained by EAs, and $d_{i}$ is the Euclidean distance (measured in objective space) between each point of the optimal solution set and the nearest member of approximated PF. A solution set with a smaller IGD value is better.

### 4.3. Parameter studies

Parameter studies of the proposed approach are conducted in this section. Parts of the results are presented in Tables 1, 2, 3, 4, 5. Note that When one parameter is changing, all other parameters are fixed. The results show that MCEDA/B and MCEDA/RM can work well at a wide range of parameters. It is a good choice to set crossover parameter as 0.5 for MCEDA/B and MCEDA/RM. And the number of bits used in MCEDA/B can be set to 16, which works better. Usually, the EDAs need more populations to produce a good results because the more the number of the populations, the more accurate of the model. The results of iterations number of $k$ means are shown in Tables 4 and 5 . Notes that the data from different tables should not be compared since other parameters may be different. However, the parameter setting would be related to the problem to be solved. It is recommended to choose the parameter for a specific problem.

Table 4
Mean and standard deviation values of IGD, obtained by MCEDA/RM on DTLZ instances.

| Number of k means iterations | Obj. | 200 | 50 | 500 |
| :--: | :--: | :--: | :--: | :--: |
|  | 3 | $5.84 \mathrm{E}-03_{4.20 E-03}$ | $5.44 \mathrm{E}-03_{3.30 E-03}(+)$ | $4.95 \mathrm{E}-03_{3.20 E-03}(+)$ |
|  | 5 | $2.37 \mathrm{E}-03_{2.70 E-04}$ | $2.27 \mathrm{E}-03_{1.80 E-04}(+)$ | $2.31 \mathrm{E}-03_{1.80 E-04}(+)$ |
| DTLZ1 | 8 | $4.73 \mathrm{E}-03_{6.80 E-04}$ | $4.33 \mathrm{E}-03_{3.90 E-04}(+)$ | $4.34 \mathrm{E}-03_{3.90 E-04}(+)$ |
|  | 10 | $5.01 \mathrm{E}-03_{4.00 E-04}$ | $5.04 \mathrm{E}-03_{5.20 E-04}(-)$ | $4.76 \mathrm{E}-03_{4.70 E-04}(+)$ |
|  | 15 | $5.23 \mathrm{E}-03_{2.00 E-04}$ | $5.53 \mathrm{E}-03_{4.90 E-04}(-)$ | $5.90 \mathrm{E}-03_{4.40 E-04}(-)$ |
|  | 3 | $3.21 \mathrm{E}-04_{1.30 E-05}$ | $3.32 \mathrm{E}-04_{1.70 E-05}(-)$ | $3.31 \mathrm{E}-04_{2.40 E-05}(-)$ |
|  | 5 | $2.75 \mathrm{E}-03_{3.80 E-04}$ | $3.10 \mathrm{E}-03_{5.30 E-04}(-)$ | $3.19 \mathrm{E}-03_{5.40 E-04}(-)$ |
| DTLZ2 | 8 | $4.86 \mathrm{E}-03_{4.20 E-04}$ | $4.97 \mathrm{E}-03_{8.10 E-04}(-)$ | $5.12 \mathrm{E}-03_{6.80 E-04}(-)$ |
|  | 10 | $4.36 \mathrm{E}-03_{4.80 E-04}$ | $4.42 \mathrm{E}-03_{4.50 E-04}(-)$ | $4.70 \mathrm{E}-03_{6.00 E-04}(-)$ |
|  | 15 | $4.41 \mathrm{E}-03_{7.90 E-04}$ | $4.57 \mathrm{E}-03_{5.50 E-04}(-)$ | $4.66 \mathrm{E}-03_{3.60 E-04}(-)$ |
|  | 3 | $1.34 \mathrm{E}-02_{1.70 E-03}$ | $1.20 \mathrm{E}-02_{3.10 E-03}(+)$ | $1.35 \mathrm{E}-02_{2.10 E-03}(-)$ |
|  | 5 | $5.40 \mathrm{E}-03_{2.70 E-03}$ | $4.52 \mathrm{E}-03_{3.60 E-04}(+)$ | $4.35 \mathrm{E}-03_{5.10 E-04}(+)$ |
| DTLZ3 | 8 | $7.01 \mathrm{E}-03_{8.60 E-04}$ | $6.71 \mathrm{E}-03_{6.70 E-04}(+)$ | $6.90 \mathrm{E}-03_{6.70 E-04}(+)$ |
|  | 10 | $1.27 \mathrm{E}-02_{2.80 E-03}$ | $1.23 \mathrm{E}-02_{1.30 E-03}(+)$ | $1.22 \mathrm{E}-02_{2.10 E-03}(+)$ |
|  | 15 | $9.71 \mathrm{E}-03_{8.40 E-04}$ | $9.70 \mathrm{E}-03_{8.20 E-04}(+)$ | $1.01 \mathrm{E}-02_{1.20 E-03}(-)$ |
|  | 3 | $3.57 \mathrm{E}-03_{5.50 E-03}$ | $7.35 \mathrm{E}-03_{6.80 E-03}(-)$ | $8.77 \mathrm{E}-03_{8.80 E-03}(-)$ |
|  | 5 | $2.81 \mathrm{E}-03_{1.10 E-03}$ | $3.50 \mathrm{E}-03_{2.80 E-03}(-)$ | $2.73 \mathrm{E}-03_{8.90 E-04}(+)$ |
| DTLZ4 | 8 | $6.70 \mathrm{E}-03_{3.00 E-04}$ | $6.67 \mathrm{E}-03_{2.70 E-04}(+)$ | $6.50 \mathrm{E}-03_{3.00 E-04}(+)$ |
|  | 10 | $8.78 \mathrm{E}-03_{1.20 E-04}$ | $9.10 \mathrm{E}-03_{3.50 E-04}(-)$ | $8.85 \mathrm{E}-03_{2.90 E-04}(-)$ |
|  | 15 | $1.33 \mathrm{E}-02_{4.30 E-04}$ | $1.34 \mathrm{E}-02_{2.90 E-04}(-)$ | $1.34 \mathrm{E}-02_{4.30 E-04}(-)$ |
|  | 3 | $1.61 \mathrm{E}-05_{2.60 E-06}$ | $1.53 \mathrm{E}-05_{3.00 E-07}(+)$ | $1.79 \mathrm{E}-05_{6.40 E-06}(-)$ |
|  | 5 | $2.11 \mathrm{E}-03_{1.70 E-04}$ | $2.09 \mathrm{E}-03_{2.00 E-04}(+)$ | $2.10 \mathrm{E}-03_{9.30 E-05}(+)$ |
| DTLZ5 | 8 | $3.78 \mathrm{E}-03_{2.40 E-04}$ | $3.89 \mathrm{E}-03_{3.60 E-04}(-)$ | $4.15 \mathrm{E}-03_{3.00 E-04}(-)$ |
|  | 10 | $4.56 \mathrm{E}-03_{4.60 E-04}$ | $4.72 \mathrm{E}-03_{6.20 E-04}(-)$ | $4.80 \mathrm{E}-03_{6.30 E-04}(-)$ |
|  | 15 | $6.85 \mathrm{E}-03_{2.80 E-04}$ | $7.02 \mathrm{E}-03_{4.90 E-04}(-)$ | $6.97 \mathrm{E}-03_{3.60 E-04}(-)$ |
|  | 3 | $9.25 \mathrm{E}-03_{1.50 E-03}$ | $9.13 \mathrm{E}-03_{2.30 E-03}(+)$ | $9.52 \mathrm{E}-03_{1.20 E-03}(-)$ |
|  | 5 | $1.72 \mathrm{E}-03_{2.90 E-04}$ | $1.61 \mathrm{E}-03_{1.70 E-04}(+)$ | $1.84 \mathrm{E}-03_{4.20 E-04}(-)$ |
| DTLZ6 | 8 | $3.36 \mathrm{E}-03_{1.20 E-03}$ | $2.66 \mathrm{E}-03_{5.00 E-04}(+)$ | $2.81 \mathrm{E}-03_{5.30 E-04}(+)$ |
|  | 10 | $3.23 \mathrm{E}-03_{5.00 E-04}$ | $2.90 \mathrm{E}-03_{4.80 E-04}(+)$ | $3.27 \mathrm{E}-03_{8.70 E-04}(-)$ |
|  | 15 | $3.28 \mathrm{E}-03_{2.90 E-04}$ | $3.44 \mathrm{E}-03_{5.60 E-04}(-)$ | $3.44 \mathrm{E}-03_{4.90 E-04}(-)$ |
|  | 3 | $4.68 \mathrm{E}-03_{3.70 E-03}$ | $5.60 \mathrm{E}-03_{3.70 E-03}(-)$ | $6.63 \mathrm{E}-03_{3.60 E-03}(-)$ |
|  | 5 | $3.44 \mathrm{E}-03_{6.70 E-04}$ | $3.57 \mathrm{E}-03_{8.40 E-04}(-)$ | $3.71 \mathrm{E}-03_{9.20 E-04}(-)$ |
| DTLZ7 | 8 | $6.41 \mathrm{E}-03_{1.80 E-04}$ | $6.45 \mathrm{E}-03_{2.50 E-04}(-)$ | $6.45 \mathrm{E}-03_{2.20 E-04}(-)$ |
|  | 10 | $7.80 \mathrm{E}-03_{1.60 E-04}$ | $7.89 \mathrm{E}-03_{9.80 E-05}(-)$ | $7.82 \mathrm{E}-03_{1.80 E-04}(-)$ |
|  | 15 | $1.15 \mathrm{E}-02_{2.10 E-04}$ | $1.15 \mathrm{E}-02_{1.90 E-04}(-)$ | $1.14 \mathrm{E}-02_{1.50 E-04}(+)$ |

The symbol " + " and " - " denote whether the IGD results of the algorithm with the compared parameter are better than or worse than that of the algorithms with the first parameter value according to the mean value and standard deviation.

### 4.4. Compared algorithms

The proposed algorithms, MCEDA/B and MCEDA/RM, are compared with three other MOEAs: NSGA-III, MOEA/D and RM-MEDA.

The NSGA-III [7] is a reference-point-based many-objective evolutionary algorithm following NSGA-II framework based on genetic algorithms. It emphasizes population members that are non-dominated and which are close to a set of supplied reference points. In their work, Das's method is adopted to create reference points [64], which has been widely used [21,7]. The NSGA-III has been applied to test problems with 3 to 15 objectives, which produced satisfactory results. And it has been extended to deal with constrained MaOPs [20]. The MOEA/D [11] is a multi-objective evolutionary algorithm based on decomposition and differential evolution (DE), which decomposes a MOOP into a number of scalar optimization subproblems and optimizes them simultaneously. It performs very well in multi-objective optimization problems as well as MaOPs [65,21]. In this experiment, the Tchebycheff approach is adopted to decompose problems. The RM-MEDA [44] is a multi-objective estimation of distribution algorithm, which uses a regularity model to generate new solutions from the previous populations. And it has only a few parameters. In the paper, describing RM-MEDA, the authors have conducted systematically experiments to compare RM-MEDA with other competitive algorithms, e.g. generalized differential evolution (GDE3), ParentCentric Recombination (PCX-NSGA-II) and a competitive EDA for MOPs, MIDEDA. The experimental results show that RM-MEDA performs better than others. Therefore, it should be proper to use RM-MEDA as a representation of EDAs in this paper.

### 4.5. Parameter setting

For all the competing algorithms, the same parameter setting of problems is used to ensure fair comparison, which is presented in Tables 6 and 7.

More parameter setting is presented in Table 8. The parameters of the algorithms compared is set according to the original papers. In NSGA-III, the simulated binary crossover (SBX) [66] probability $p_{\mathrm{c}}$ is set to 1 and the crossover parameter in SBX $\eta_{\mathrm{c}}$ is set to 30 according to the original paper [7]. In MOEDA/D, the differential crossover parameter $\sigma$ is assigned to 1.0 and $f$ is set to 0.5 [11,12]. The crossover parameter in MCEDA $c_{t}$ is set to 0.5 . The polynomial mutation probability $p_{m}$ of all algorithms is assigned as $1 / n$ where $n$ is the number of variables and the $\eta_{m}$ is set to 20. For MOEA/D and MCEDA, the neighborhood size is assigned with 20 [11]. The partition number used in RM-MEDA is set to 5 [44]. All algorithms will terminate when their evaluations reach 300,000 and all of them will be run 30 times independently.

### 4.6. Results

### 4.6.1. Three objectives problems

The Pareto fronts of problems with 3 objectives can be visualized in a Cartesian coordinate. There have been many graphs for NSGA-III and MOEA/D in terms of 3 objectives on DTLZ problems [7, 20,11,12]. Therefore, in this section, only the proposed MCEDA/B and MCEDA/RM on 3 objectives DTLZ problems are plotted in Fig. 2. It is not surprising that the distribution of the solution

Table 5
Mean and standard deviation values of IGD, obtained by MCEDA/B on DTLZ instances.

| Number of k means iterations | Obj. | 200 | 50 | 500 |
| :--: | :--: | :--: | :--: | :--: |
|  | 3 | $\begin{aligned} & 2.44 \mathrm{E}-04_{3,30 \mathrm{E}-05} \\ & 1.32 \mathrm{E}-03_{3,10 \mathrm{E}-04} \\ & 1.99 \mathrm{E}-03_{6,30 \mathrm{E}-04} \end{aligned}$ | $\begin{aligned} & 2.36 \mathrm{E}-04_{3,20 \mathrm{E}-05}(+) \\ & 1.23 \mathrm{E}-03_{3,70 \mathrm{E}-05}(+) \\ & 3.28 \mathrm{E}-03_{3,20 \mathrm{E}-03}(-) \end{aligned}$ | $\begin{aligned} & 2.32 \mathrm{E}-04_{3,50 \mathrm{E}-05}(+) \\ & 1.28 \mathrm{E}-03_{3,10 \mathrm{E}-04}(+) \end{aligned}$ |
| DTLZ1 | 8 |  | $5.43 \mathrm{E}-03_{3,40 \mathrm{E}-04}$ | $5.20 \mathrm{E}-03_{7,20 \mathrm{E}-04}(+)$ |
|  | 10 |  | $5.43 \mathrm{E}-03_{3,40 \mathrm{E}-04}$ | $5.20 \mathrm{E}-03_{7,20 \mathrm{E}-04}(+)$ |
|  | 15 |  | $1.07 \mathrm{E}-02_{3,30 \mathrm{E}-03}$ | $7.29 \mathrm{E}-03_{3,50 \mathrm{E}-03}(+)$ |
|  | 3 |  | $3.53 \mathrm{E}-04_{3,40 \mathrm{E}-05}$ | $3.44 \mathrm{E}-04_{3,70 \mathrm{E}-05}(+)$ |
|  | 5 |  | $2.24 \mathrm{E}-03_{3,30 \mathrm{E}-04}$ | $2.15 \mathrm{E}-03_{3,70 \mathrm{E}-04}(+)$ |
| DTLZ2 | 8 |  | $4.69 \mathrm{E}-03_{3,80 \mathrm{E}-04}$ | $4.85 \mathrm{E}-03_{4,40 \mathrm{E}-04}(-)$ |
|  | 10 |  | $5.64 \mathrm{E}-03_{8,70 \mathrm{E}-04}$ | $5.25 \mathrm{E}-03_{7,00 \mathrm{E}-04}(+)$ |
|  | 15 |  | $2.63 \mathrm{E}-03_{8,10 \mathrm{E}-04}$ | $2.66 \mathrm{E}-03_{2,20 \mathrm{E}-04}(-)$ |
|  | 3 |  | $8.41 \mathrm{E}-04_{8,90 \mathrm{E}-05}$ | $8.35 \mathrm{E}-04_{1,10 \mathrm{E}-04}(+)$ |
|  | 5 |  | $2.16 \mathrm{E}-02_{2,00 \mathrm{E}-02}$ | $1.56 \mathrm{E}-02_{9,70 \mathrm{E}-03}(+)$ |
| DTLZ3 | 8 |  | $1.07 \mathrm{E}-02_{4,20 \mathrm{E}-03}$ | $1.08 \mathrm{E}-02_{3,80 \mathrm{E}-03}(-)$ |
|  | 10 |  | $8.09 \mathrm{E}-03_{6,00 \mathrm{E}-03}$ | $6.64 \mathrm{E}-03_{3,80 \mathrm{E}-03}(+)$ |
|  | 15 |  | $1.11 \mathrm{E}-02_{2,90 \mathrm{E}-03}$ | $8.97 \mathrm{E}-03_{1,50 \mathrm{E}-03}(+)$ |
|  | 3 |  | $1.04 \mathrm{E}-02_{7,00 \mathrm{E}-03}$ | $1.25 \mathrm{E}-02_{6,70 \mathrm{E}-03}(-)$ |
|  | 5 |  | $1.37 \mathrm{E}-02_{3,80 \mathrm{E}-03}$ | $1.35 \mathrm{E}-02_{3,40 \mathrm{E}-03}(+)$ |
| DTLZ4 | 8 |  | $7.00 \mathrm{E}-03_{1,50 \mathrm{E}-03}$ | $6.57 \mathrm{E}-03_{8,80 \mathrm{E}-04}(+)$ |
|  | 10 |  | $1.21 \mathrm{E}-02_{1,10 \mathrm{E}-03}$ | $1.25 \mathrm{E}-02_{1,50 \mathrm{E}-03}(-)$ |
|  | 15 |  | $8.15 \mathrm{E}-03_{6,50 \mathrm{E}-04}$ | $8.15 \mathrm{E}-03_{3,00 \mathrm{E}-04}(-)$ |
|  | 3 |  | $1.89 \mathrm{E}-05_{9,30 \mathrm{E}-06}$ | $1.67 \mathrm{E}-05_{1,00 \mathrm{E}-05}(+)$ |
|  | 5 |  | $2.04 \mathrm{E}-03_{3,00 \mathrm{E}-04}$ | $1.86 \mathrm{E}-03_{3,10 \mathrm{E}-04}(+)$ |
|  | 8 |  | $2.18 \mathrm{E}-03_{2,80 \mathrm{E}-04}$ | $2.31 \mathrm{E}-03_{2,10 \mathrm{E}-04}(-)$ |
|  | 10 |  | $2.45 \mathrm{E}-03_{1,30 \mathrm{E}-04}$ | $2.58 \mathrm{E}-03_{4,20 \mathrm{E}-04}(-)$ |
|  | 15 |  | $1.68 \mathrm{E}-03_{8,80 \mathrm{E}-05}$ | $1.76 \mathrm{E}-03_{1,30 \mathrm{E}-04}(-)$ |
|  | 3 |  | $4.74 \mathrm{E}-05_{4,50 \mathrm{E}-05}$ | $5.75 \mathrm{E}-05_{9,00 \mathrm{E}-05}(-)$ |
|  | 5 |  | $2.08 \mathrm{E}-03_{2,50 \mathrm{E}-04}$ | $2.15 \mathrm{E}-03_{2,60 \mathrm{E}-04}(-)$ |
| DTLZ6 | 8 |  | $2.98 \mathrm{E}-03_{6,50 \mathrm{E}-04}$ | $2.84 \mathrm{E}-03_{5,10 \mathrm{E}-04}(+)$ |
|  | 10 |  | $5.30 \mathrm{E}-03_{9,60 \mathrm{E}-04}$ | $4.89 \mathrm{E}-03_{6,20 \mathrm{E}-04}(+)$ |
|  | 15 |  | $2.23 \mathrm{E}-03_{2,80 \mathrm{E}-04}$ | $2.13 \mathrm{E}-03_{9,60 \mathrm{E}-05}(+)$ |
|  | 3 |  | $6.41 \mathrm{E}-04_{2,70 \mathrm{E}-05}$ | $2.69 \mathrm{E}-03_{4,30 \mathrm{E}-03}(-)$ |
|  | 5 |  | $7.30 \mathrm{E}-03_{3,40 \mathrm{E}-03}$ | $6.12 \mathrm{E}-03_{3,00 \mathrm{E}-03}(+)$ |
|  | 8 |  | $8.37 \mathrm{E}-03_{2,40 \mathrm{E}-03}$ | $1.02 \mathrm{E}-02_{2,40 \mathrm{E}-03}(-)$ |
|  | 10 |  | $1.37 \mathrm{E}-02_{9,10 \mathrm{E}-04}$ | $1.45 \mathrm{E}-02_{8,90 \mathrm{E}-04}(-)$ |
|  | 15 |  | $1.08 \mathrm{E}-02_{5,00 \mathrm{E}-04}$ | $1.04 \mathrm{E}-02_{3,80 \mathrm{E}-04}(+)$ |

The symbol " + " and " - " denote whether the IGD results of the algorithm with the compared parameter are better than or worse than that of the algorithms with the first parameter value according to the mean value and standard deviation.
sets are similar to that of MOEA/D because MCEDA is based on MOEA/D framework. As the graphs show, the obtained solutions well distribute and converge to the Pareto fronts of DTLZ1, DTLZ3 and DTLZ5.

### 4.6.2. IGD values

The mean and standard deviation values of IGD, obtained by MCEDA/B, MCEDA/RM, NSGA-III and MOEA/D on DTLZ instances after 30 independent runs, is presented in Tables 9 and 10.

Here is how Tables 9 and 10 are produced. (1) Apply the MannWhitney rank test to justify the results of different algorithms to find whether they are statistically identical at the $5 \%$ significance level. (2) If they are statistically identical, their performance will be regarded as equal. (3) Otherwise, mean value and standard deviation are used to decide whether one result is better/worse than the other.

The data from Tables 9 and 10 can be compared together. According to the IGD values table, MCEDA/RM performs better in DTLZ6 and DTLZ7 while NSGA-III performs well in DTLZ1, DTLZ2 and DTLZ3. And it can be seen that MCEDA/RM has better results than MOEA/D and RM-MEDA on many problems, which should give the credit to the estimation model and the clustering strategy used in MCEDA/RM. MCEDA/B has better performance than MOEA/B and RM-MEDA in many problems although its results are worse than NSGA-III. It is noted that MCEDA/RM performs better than MCEDA/B, which may be due to the too ideal assumption of the bits model.
4.6.3. IGD variation with increasing number of function evaluations

Since the IGD value can represent the convergence and diversity of the obtained solutions at the same time, it is valuable to explore the change of IGD value with the increase of function evaluations. Variation of IGD metric value with MCEDA/B, MCEDA/RM, NSGAIII and MOEA/D on four DTLZ instances with 8 objectives is represented in Fig. 3. Variation of IGD metric value with RM-MEDA on four DTLZ instances with 8 objectives is represented in Fig. 4. These results are obtained after 300,000 function evaluations for each algorithm. And each experiment has been run 20 times to get the mean and standard deviation of the IGD value. And the Pareto fronts adopted here is generated by the MOEAFramework. ${ }^{2}$ As we can see, MCEDA/B and MCEDA/RM have better performance on DTLZ1 and DTLZ7 with 8 objectives, while NSGA-III performs better on DTLZ2. It seems that the regular model based MCEDA/RM is not so suitable for the DTLZ3 with 8 objectives, while the MCEDA/B has normal performance on it. MOEA/D shows unstable fluctuation on DTLZ2 while MCEDA/B and MCEDA/RM have intended to lower the IGD value. According to the graphs, MCEDA/B and MCEDA/RM have outperformed others on DTLZ7 with 8 objectives. As for RM-MEDA, it seems that it cannot handle problems like DTLZ1 and DTLZ3 and has intended to lower the IGD on DTLZ2 and DTLZ4. According to the graphs, RM-MEDA, the pure EDA, is not good at dealing with problems with many objectives.

[^0]
[^0]:    2 MOEAFramework: http://moeaframework.org/index.html.

## Algorithm 4. Bits model

Input: $C_{t}$ : the solution cluster set of current population, where $C_{t}=\left\{C_{t}^{1}, C_{t}^{2}, \ldots, C_{t}^{k}\right\} . C_{t}^{r}$ contains the ith solution cluster; $m\left|C_{t}\right|$ : the number of new solutions; $n$ : the number of the variables of the problem;
Output: $Q_{t}$ : new solutions;
size $\leftarrow$ the number of all solutions in $C_{t}$;
// Model each cluster;
for $i \leftarrow 1$ to $\left|C_{t}\right|$ do
$C s_{i}^{i} \leftarrow$ nonDominatedSelect $\left(C_{t}^{i}\right)$;
Probability; $\leftarrow \emptyset$;
for $j \leftarrow 1$ to $n$ do
singleVariableVector $\leftarrow \emptyset$;
for $v \leftarrow 1$ to $\left|C s_{i}^{v}\right|$ do
singleVariableVector $(v) \leftarrow$
the $j$ th variable of $\mathrm{Cs}_{v}^{j}(v)$;
variableBitsMatrix $\leftarrow$ getBitsMatrix(
singleVariableVector, low:Limit, upperLimit);
bitsProbability $\leftarrow$ calculateBitsProbability(
variableBitsMatrix);
Probability; $\leftarrow$ Probability; $\cup$ bitsProbability;
// $n_{i}$ is the number of the new solutions to be generated for the $i$ th cluster;
$n_{i} \leftarrow\left(m\left|C_{t}\right|\right) \frac{|c_{t}^{i \cdot 1}|}{u_{i t e}}$
counter $\leftarrow 0$;
while counter $<n_{i}$ do
new:Solution $\leftarrow$ createSolution();
for $v \leftarrow 1$ to $n$ do
newVariable $\leftarrow$ getNewVariable( Probability;(v), low:Limit, upperLimit);
if newVariable exceeds the variable bounds then
Regenerate the newVariable
Set the $v$ th variable of the newSolution to newVariable;
$Q_{t} \leftarrow Q_{t} \cup$ new:Solution;
counter $++$;
23 return $Q_{t}$;

Note that the time cost by the proposed algorithms and other EDAs are a little larger than non-EDAs. However the difference is not too large and the time cost by the proposed algorithms is acceptable. And many methods can be used to speed up the run of algorithms, e.g. parallelization, vectorization, using cache.

### 4.6.4. Parallel coordinates

While the results of problems withe 2 or 3 objectives can be plotted by scatter in Cartesian coordinates, the visualization of results of MaOPs remains a challenge. When it comes to MaOPs, there have been some researches in visualizing their results [67, 68]. Parallel coordinates are such a tool, which illustrate an $m$ dimensional space on a 2D figure by plotting points in the parallel vertical parallel axes [69]. The parallel coordinates with different order of parallel vertical parallel axes will present different information.

Fig. 5 shows the parallel coordinate plots for the solution set in the best run obtained by MCEDA/B (first row), MCEDA/RM (second row), NSGA-III (third row) and MOEA/D (fourth row) on 10 objectives DTLZ problems. Fig. 6 shows the parallel coordinate plots for the solution set in the best run obtained by RM-MEDA on 10 objectives DTLZ problems. As we can see from the graphs, as for DTLZ2, MCEDA/B, MCEDA/RM and MOEA/D do not converge to

## Algorithm 5. Regular model

Input: $C_{t}$ : the solution cluster set of current population, where $C_{t}=\left\{C_{t}^{1}, C_{t}^{2}, \ldots, C_{t}^{k}\right\} . C_{t}^{r}$ contains the ith solution cluster; $m\left|C_{t}\right|$ : the number of new solutions;
Output: $Q_{t}$ : new solutions;
$C_{t}^{r} \leftarrow \emptyset$;
size $\leftarrow$ the number of all solutions in $C_{t}$;
// Model each cluster;
for $i \leftarrow 1$ to $\left|C_{t}\right|$ do
// The partition number is set to 1 ;
$h \leftarrow 1$;
// $S=\left\{S_{1}, S_{2}, \ldots, S_{h}\right\}$
$S \leftarrow P C A$ partition $\left(C_{t}(i), h\right)$;
$S^{\prime} \leftarrow \emptyset$;
// Model each sub cluster;
for $j \leftarrow 1$ to $h$ do
$\widetilde{\boldsymbol{x}}(i, j) \leftarrow \operatorname{mean}\left(S_{j}\right)$
$C_{t}(i, j) \leftarrow \frac{1}{\left|S_{j}\right|-1} \sum_{\boldsymbol{x} \in S_{j}}(\boldsymbol{x}-\widetilde{\boldsymbol{x}})(\boldsymbol{x}-\widetilde{\boldsymbol{x}}(i, j))^{T}$;
// $\lambda(i, j)$ is the eigenvalue matrix, which is sorted (i.e.,
$\lambda(i, j)(1,1) \geq \lambda(i, j)(2,2) \geq \ldots \geq \lambda(i, j)(n, n))$;
$\lambda(i, j) \leftarrow$ Eigenvalue $(\operatorname{Cov}(i, j)) . \operatorname{sort}()$;
// $U(i, j)$ is the eigenvector matrix corresponding to $\lambda(i, j)$;
$U(i, j) \leftarrow$ Eigenvector $(\operatorname{Cov}(i, j)) . \operatorname{sort}()$;
// Generate new solutions;
// $n_{i}$ is the number of the new solutions to be generated for the $i$ th cluster;
$n_{i} \leftarrow\left(m\left|C_{t}\right|\right) \frac{|c_{t}^{i \cdot 1}|}{u_{i t e}}$
for $j \leftarrow 1$ to $h$ do
for $j i \leftarrow 1$ to $n_{i} \frac{\left|S_{j}\right|}{\left|s_{j}^{v}\right|}$; do
for $w \leftarrow 1$ to $m-1$ do
$a(i, j, w) \leftarrow \min _{\boldsymbol{x} \in S_{j}}(\boldsymbol{x}-\widetilde{\boldsymbol{x}})^{T} U(i, j)(:, w)$;
$b(i, j, w) \leftarrow \max _{\boldsymbol{x} \in S_{j}}(\boldsymbol{x}-\widetilde{\boldsymbol{x}})^{T} U(i, j)(:, w)$;
$\alpha_{w} \leftarrow$ uniformlyRandomlyGenerate(
$a(i, j, w)-0.25(b(i, j, w)-a(i, j, w))$,
$b(i, j, w)+0.25(b(i, j, w)-a(i, j, w)))$;
$\Psi(i, j) \leftarrow \widetilde{\boldsymbol{x}}(i, j)+\sum_{w=1}^{m-1} \alpha_{w} U(i, j)(:, w)$;
$\sigma_{j} \leftarrow \frac{1}{n-m+1} \sum_{w=m}^{n} \lambda(i, j)(w, w)$;
for $i i \leftarrow 1$ to $n_{i}$ do
// Generate normal distribution number where mean equals 0 and standard deviation equals $\sigma_{j}$;
$\varepsilon_{j}(i i, i i) \leftarrow$
generateNormalDistributionNumber $\left(0, \sigma_{j}\right)$;
$\varepsilon_{j}^{\prime}(i i) \leftarrow \varepsilon_{j}(i i, i i)$;
$S_{j}^{\prime}(j j) \leftarrow \Psi(i, j)+\varepsilon_{j}^{\prime} ;$
$C_{t}^{\prime}(i) \leftarrow C_{t}^{\prime}(i) \cup S_{j}^{\prime} ;$
$Q_{t} \leftarrow$ all solution in $C_{t}^{\prime}$;
return $Q_{t}$;
the Pareto fronts as fast as NSGA-III, which indicates that they may need more evaluations. According to the parallel coordinates, these algorithms has similar performance on DTLZ5 with 10 objectives. RM-MEDA shows large oscillation for DTLZ2 and DTLZ7. However, it is important to note that parallel coordinates may not be able to accurately represent those properties since the problem could be very complex [69].

Table 6
DTLZ setting.

| Problems | Objective number | Variable number |
| :--: | :--: | :--: |
|  | 3 | 7 |
|  | 5 | 9 |
| DTLZ1 | 8 | 12 |
|  | 10 | 14 |
|  | 15 | 19 |
|  | 3 | 12 |
|  | 5 | 14 |
| DTLZ2 | 8 | 17 |
|  | 10 | 19 |
|  | 15 | 24 |
|  | 3 | 12 |
|  | 5 | 14 |
| DTLZ3 | 8 | 17 |
|  | 10 | 19 |
|  | 15 | 24 |
|  | 3 | 12 |
|  | 5 | 14 |
| DTLZ4 | 8 | 17 |
|  | 10 | 19 |
|  | 15 | 24 |
|  | 3 | 12 |
|  | 5 | 14 |
| DTLZ5 | 8 | 17 |
|  | 10 | 19 |
|  | 15 | 24 |
|  | 3 | 12 |
|  | 5 | 14 |
| DTLZ6 | 8 | 17 |
|  | 10 | 19 |
|  | 15 | 24 |
|  | 3 | 22 |
|  | 5 | 24 |
| DTLZ7 | 8 | 27 |
|  | 10 | 29 |
|  | 15 | 34 |

Table 7
Population size.

| No. of objectives | NSGA-III divisions | Population size |
| :--: | :--: | :--: |
| 3 | 18 | 192 |
| 5 | 5 | 210 |
| 8 | 4 | 330 |
| 10 | 3 | 220 |
| 15 | 3 | 680 |

## 4.7. Discussion

The proposed approach has been applied to 3-objective to 15objective test problems of DTLZ. On those problems, the proposed
algorithms, MCEDA/B and MCEDA/RM, have been able to successfully find a well-converged and well-diversified set of points over multiple runs. MCEDA/RM have showed better results than MOEA/D and RM-MEDA in many problems and perform best in some problems. It is noted that MCEDA/B does not perform as good as MCEDA/RM, which may be because the assumption of the bits model adopted in the work is too ideal and it will be improved further. It can be expected that a better model incorporated with MCEDA will generate better results.

As a matter of fact, the best approach may be related to the specific problem to be solved and it may be useful to clearly define the class of problems an algorithm is designed for. However, how to choose the best approach will be the subsequent problem. It may be more difficult to choose a better algorithm than to apply a universe approach directly, since the choose of approaches could be very time consuming and a universe algorithm can also produce well distributed and converged results.

## 5. Conclusion

In this paper, a new approach to deal with many-objective optimization problems, utilizing estimation models and clustering strategy, is proposed, which is based on decomposition and the MOEA/D framework. And two algorithms, MCEDA/B and MCEDA/ RM, have been implemented. Most other EDAs try to build the estimation model for the all variables as a whole and are based on the traditional EDA framework Algorithm 1. It may work very well at low number of objectives and simple problems. However, when it comes to MaOPs and problems with complex Pareto fronts, it would be unimaginable to build such a complex model. Therefore, unlike the traditional EDAs, the proposed approach builds the model after the clustering strategy, which will enhance the precision and the reliability of the latter estimation.

The performance of MCEDA/B and MCEDA/RM have been compared with NSGA-III, MOEA/D and RM-MEDA. The NSGA-III is based on GA and the MOEA/D is based on differential evolution (DE), which do not use any prior knowledge. While the proposed MCEDA/B and MCEDA/RM try to build estimation model by the bits model and the regular model in order to find more explicit and promising solutions so as to speed up the convergence procedure. The results have shown that the proposed MCEDA is a competitive and promising approach to solve MaOPs.

In the future, more explicit and more efficient estimation model will be tested in the hope of enhancing the convergence and diversity of the algorithm and increasing its speed. More reliable performance metrics will be used to justify the algorithms as well, since the accurate Pareto fronts are difficult to find in MaOPs. Also MCEDA will be extended to handle constrained problems and it will be applied to real-word engineering problems.

Table 8
Parameter setting.

| Parameters | NSGA-III | MOEA/D | MCEDA/B | MCEDA/RM | RM-MEDA |
| :--: | :--: | :--: | :--: | :--: | :--: |
| SBX probability, $p_{s}$ | 1 |  |  |  |  |
| Crossover parameter in SBX, $\eta_{i}$ | 30 |  |  |  |  |
| Differential crossover, $c r$ |  | 1 |  |  |  |
| Differential crossover, $f$ |  | 0.5 |  |  |  |
| Crossover parameter in MCEDA |  |  | 0.5 | 0.5 |  |
| Max RSS in k means, MaxRSS |  |  | $1 e-5$ | $1 e-5$ |  |
| Max iterations in k means, Masterutions |  |  | 200 | 200 |  |
| Polynomial mutation probability, $p_{m}$ | $1 / n$ | $1 / n$ | $1 / n$ | $1 / n$ |  |
| Parameter in polynomial mutation, $\eta_{m}$ | 20 | 20 | 20 | 20 |  |
| Neighborhood size |  | 20 | 20 | 20 |  |
| Partition number |  |  |  |  | 5 |
| Max evaluations | 300,000 | 300,000 | 300,000 | 300,000 | 300,000 |
| Independent runs | 30 | 30 | 30 | 30 | 30 |

Table 9
Mean and standard deviation values of IGD, obtained by MCEDA/RM, NSGA-III, MOEA/D and RM-MEDA on DTLZ instances.

| Problem | Obj. | MCEDA/RM | NSGA-III | MOEA/D | RM-MEDA |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | 3 | $2.32 \mathrm{E}-04_{2.50E-05}$ | $1.40 \mathrm{E}-04_{1.70 E-04}(+)$ | $2.21 \mathrm{E}-04_{2.80 E-05}(+)$ | $5.37 \mathrm{E}-03_{2.80 E-03}(-)$ |
|  | 5 | $3.19 \mathrm{E}-04_{7.98 E-05}$ | $2.50 \mathrm{E}-04_{5.20 E-05}(+)$ | $1.72 \mathrm{E}-03_{2.50 E-03}(-)$ | $3.23 \mathrm{E}-03_{2.50 E-04}(-)$ |
| DTLZ1 | 8 | $1.40 \mathrm{E}-03_{1.50 E-04}$ | $2.44 \mathrm{E}-03_{1.50 E-03}(-)$ | $4.41 \mathrm{E}-03_{3.50 E-03}(-)$ | $1.70 \mathrm{E}-03_{4.70 E-05}(-)$ |
|  | 10 | $4.51 \mathrm{E}-03_{5.20 E-04}$ | $2.80 \mathrm{E}-03_{6.10 E-04}(+)$ | $1.92 \mathrm{E}-03_{4.00 E-04}(+)$ | $2.48 \mathrm{E}-03_{1.10 E-04}(+)$ |
|  | 15 | $1.34 \mathrm{E}-03_{4.00 E-04}$ | $8.71 \mathrm{E}-04_{1.80 E-04}(+)$ | $4.09 \mathrm{E}-03_{6.80 E-04}(-)$ | $1.62 \mathrm{E}-03_{1.30 E-04}(-)$ |
|  | 3 | $3.04 \mathrm{E}-04_{4.20 E-05}$ | $4.40 \mathrm{E}-05_{1.20 E-05}(+)$ | $3.99 \mathrm{E}-04_{1.90 E-05}(-)$ | $3.16 \mathrm{E}-03_{6.40 E-04}(-)$ |
|  | 5 | $7.01 \mathrm{E}-04_{1.70 E-04}$ | $1.82 \mathrm{E}-04_{1.20 E-05}(+)$ | $2.39 \mathrm{E}-03_{3.00 E-04}(-)$ | $3.31 \mathrm{E}-03_{3.31 E-03}(-)$ |
| DTLZ2 | 8 | $3.89 \mathrm{E}-03_{6.50 E-04}$ | $2.20 \mathrm{E}-03_{2.80 E-03}(+)$ | $5.04 \mathrm{E}-03_{4.50 E-04}(-)$ | $3.02 \mathrm{E}-03_{1.40 E-05}(+)$ |
|  | 10 | $7.64 \mathrm{E}-03_{8.00 E-04}$ | $5.20 \mathrm{E}-03_{1.50 E-03}(+)$ | $9.62 \mathrm{E}-03_{5.20 E-04}(-)$ | $4.36 \mathrm{E}-03_{1.50 E-04}(+)$ |
|  | 15 | $3.10 \mathrm{E}-03_{4.00 E-04}$ | $2.22 \mathrm{E}-03_{8.50 E-04}(+)$ | $6.54 \mathrm{E}-03_{1.10 E-04}(-)$ | $2.79 \mathrm{E}-03_{5.80 E-05}(+)$ |
|  | 3 | $6.60 \mathrm{E}-04_{6.70 E-05}$ | $1.18 \mathrm{E}-04_{2.20 E-05}(+)$ | $4.15 \mathrm{E}-04_{3.00 E-05}(+)$ | $5.46 \mathrm{E}-03_{1.50 E-05}(-)$ |
|  | 5 | $3.58 \mathrm{E}-02_{1.30 E-02}$ | $7.72 \mathrm{E}-04_{5.80 E-04}(+)$ | $8.43 \mathrm{E}-03_{3.20 E-02}(+)$ | $3.42 \mathrm{E}-03_{2.30 E-04}(+)$ |
| DTLZ3 | 8 | $5.31 \mathrm{E}-03_{5.70 E-04}$ | $2.75 \mathrm{E}-03_{2.80 E-03}(+)$ | $4.02 \mathrm{E}-03_{1.90 E-03}(+)$ | $2.94 \mathrm{E}-03_{7.70 E-05}(+)$ |
|  | 10 | $4.93 \mathrm{E}-03_{3.20 E-03}$ | $3.44 \mathrm{E}-03_{1.80 E-03}(+)$ | $2.16 \mathrm{E}-03_{2.70 E-04}(+)$ | $4.95 \mathrm{E}-03_{1.80 E-04}(-)$ |
|  | 15 | $9.58 \mathrm{E}-03_{7.90 E-04}$ | $8.90 \mathrm{E}-04_{8.50 E-05}(+)$ | $5.61 \mathrm{E}-03_{9.50 E-04}(+)$ | $2.86 \mathrm{E}-03_{6.60 E-05}(+)$ |
|  | 3 | $2.76 \mathrm{E}-03_{5.70 E-03}$ | $3.58 \mathrm{E}-04_{1.60 E-03}(+)$ | $1.64 \mathrm{E}-03_{2.00 E-03}(+)$ | $1.56 \mathrm{E}-02_{9.20 E-03}(-)$ |
|  | 5 | $6.88 \mathrm{E}-04_{1.30 E-04}$ | $1.53 \mathrm{E}-03_{2.40 E-03}(-)$ | $4.23 \mathrm{E}-03_{1.70 E-03}(-)$ | $2.46 \mathrm{E}-03_{2.00 E-04}(-)$ |
| DTLZ4 | 8 | $3.44 \mathrm{E}-03_{6.10 E-04}$ | $1.29 \mathrm{E}-04_{6.00 E-06}(+)$ | $8.76 \mathrm{E}-03_{6.30 E-04}(-)$ | $1.68 \mathrm{E}-03_{4.00 E-05}(+)$ |
|  | 10 | $7.22 \mathrm{E}-03_{8.70 E-04}$ | $7.49 \mathrm{E}-04_{1.50 E-04}(+)$ | $1.65 \mathrm{E}-02_{8.30 E-04}(-)$ | $2.61 \mathrm{E}-03_{5.50 E-05}(+)$ |
|  | 15 | $7.05 \mathrm{E}-03_{5.50 E-04}$ | $1.24 \mathrm{E}-04_{1.80 E-05}(+)$ | $7.45 \mathrm{E}-03_{7.90 E-04}(-)$ | $1.54 \mathrm{E}-03_{8.80 E-06}(+)$ |
|  | 3 | $1.85 \mathrm{E}-05_{1.30 E-05}$ | $1.58 \mathrm{E}-04_{2.30 E-05}(-)$ | $2.85 \mathrm{E}-05_{1.90 E-05}(-)$ | $1.84 \mathrm{E}-03_{1.10 E-03}(-)$ |
|  | 5 | $1.68 \mathrm{E}-03_{1.60 E-04}$ | $1.90 \mathrm{E}-03_{4.80 E-04}(-)$ | $2.36 \mathrm{E}-03_{4.70 E-04}(-)$ | $2.61 \mathrm{E}-03_{2.80 E-04}(-)$ |
| DTLZ5 | 8 | $1.81 \mathrm{E}-03_{1.60 E-04}$ | $1.20 \mathrm{E}-03_{3.70 E-05}(+)$ | $4.07 \mathrm{E}-03_{7.30 E-04}(-)$ | $2.46 \mathrm{E}-03_{2.50 E-04}(-)$ |
|  | 10 | $3.38 \mathrm{E}-03_{3.90 E-04}$ | $2.60 \mathrm{E}-03_{7.50 E-04}(+)$ | $6.98 \mathrm{E}-03_{5.70 E-04}(-)$ | $4.00 \mathrm{E}-03_{4.10 E-04}(-)$ |
|  | 15 | $1.29 \mathrm{E}-03_{8.90 E-05}$ | $1.43 \mathrm{E}-03_{3.60 E-04}(-)$ | $4.44 \mathrm{E}-03_{2.30 E-04}(-)$ | $1.77 \mathrm{E}-03_{9.50 E-05}(-)$ |
|  | 3 | $3.28 \mathrm{E}-04_{2.00 E-04}$ | $1.62 \mathrm{E}-03_{3.30 E-04}(-)$ | $2.09 \mathrm{E}-05_{1.80 E-05}(+)$ | $8.86 \mathrm{E}-03_{2.80 E-03}(-)$ |
|  | 5 | $1.99 \mathrm{E}-03_{2.80 E-04}$ | $3.02 \mathrm{E}-03_{1.50 E-04}(-)$ | $1.52 \mathrm{E}-03_{1.70 E-04}(+)$ | $2.80 \mathrm{E}-03_{1.30 E-04}(-)$ |
| DTLZ6 | 8 | $2.03 \mathrm{E}-03_{2.50 E-04}$ | $2.23 \mathrm{E}-03_{1.50 E-03}(-)$ | $3.47 \mathrm{E}-03_{5.90 E-04}(-)$ | $2.62 \mathrm{E}-03_{6.00 E-05}(-)$ |
|  | 10 | $2.91 \mathrm{E}-03_{3.50 E-04}$ | $6.25 \mathrm{E}-03_{1.20 E-03}(-)$ | $5.09 \mathrm{E}-03_{7.30 E-04}(-)$ | $3.93 \mathrm{E}-03_{7.50 E-05}(-)$ |
|  | 15 | $1.29 \mathrm{E}-03_{1.10 E-04}$ | $1.39 \mathrm{E}-03_{3.80 E-04}(-)$ | $2.71 \mathrm{E}-03_{2.20 E-04}(-)$ | $2.46 \mathrm{E}-03_{4.10 E-05}(-)$ |
|  | 3 | $1.31 \mathrm{E}-03_{1.10 E-03}$ | $3.17 \mathrm{E}-04_{6.20 E-06}(+)$ | $8.10 \mathrm{E}-04_{2.20 E-03}(+)$ | $2.60 \mathrm{E}-02_{4.90 E-03}(-)$ |
|  | 5 | $6.69 \mathrm{E}-04_{3.30 E-04}$ | $6.69 \mathrm{E}-03_{1.90 E-03}(-)$ | $2.85 \mathrm{E}-03_{7.10 E-04}(-)$ | $8.56 \mathrm{E}-03_{7.20 E-04}(-)$ |
| DTLZ7 | 8 | $3.17 \mathrm{E}-03_{3.60 E-04}$ | $5.60 \mathrm{E}-03_{1.00 E-04}(-)$ | $4.48 \mathrm{E}-03_{5.60 E-04}(-)$ | $5.78 \mathrm{E}-03_{2.20 E-04}(-)$ |
|  | 10 | $1.46 \mathrm{E}-03_{2.40 E-05}$ | $6.41 \mathrm{E}-03_{4.20 E-04}(-)$ | $7.43 \mathrm{E}-03_{1.10 E-03}(-)$ | $8.06 \mathrm{E}-03_{1.30 E-04}(-)$ |
|  | 15 | $4.92 \mathrm{E}-03_{5.30 E-05}$ | $2.70 \mathrm{E}-03_{1.80 E-04}(+)$ | $6.92 \mathrm{E}-03_{3.70 E-04}(-)$ | $5.74 \mathrm{E}-03_{2.50 E-05}(-)$ |

The symbol " $=$ " denote that the IGD results of the proposed algorithm and algorithms compared are statistically identical according to the Mann-Whitney rank test at the $5 \%$ significance level. The symbol " + " and " - " denote whether the IGD results of the compared algorithm are better or worse than that of the proposed algorithms according to the mean value and standard deviation.

Table 10
Mean and standard deviation values of IGD, obtained by MCEDA/B, NSGA-III, MOEA/D and RM-MEDA on DTLZ instances.

| Problem | Obj. | MCEDA/B | NSGA-III | MOEA/D | RM-MEDA |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | 3 | $1.85 \mathrm{E}-04_{1.50 E-05}$ | $1.40 \mathrm{E}-04_{1.70 E-04}(+)$ | $2.21 \mathrm{E}-04_{2.80 E-05}(-)$ | $5.37 \mathrm{E}-03_{2.80 E-03}(-)$ |
|  | 5 | $3.65 \mathrm{E}-04_{7.90 E-05}$ | $2.50 \mathrm{E}-04_{7.20 E-05}(+)$ | $1.72 \mathrm{E}-03_{2.50 E-03}(-)$ | $3.23 \mathrm{E}-03_{2.10 E-04}(-)$ |
| DTLZ1 | 8 | $2.67 \mathrm{E}-03_{4.20 E-04}$ | $2.44 \mathrm{E}-03_{1.50 E-03}(+)$ | $4.41 \mathrm{E}-03_{3.50 E-03}(-)$ | $1.70 \mathrm{E}-03_{4.70 E-05}(+)$ |
|  | 10 | $6.59 \mathrm{E}-03_{1.20 E-03}$ | $2.80 \mathrm{E}-03_{6.30 E-04}(+)$ | $1.92 \mathrm{E}-03_{4.00 E-04}(+)$ | $2.48 \mathrm{E}-03_{1.10 E-04}(+)$ |
|  | 15 | $2.21 \mathrm{E}-03_{3.00 E-04}$ | $8.71 \mathrm{E}-04_{1.80 E-04}(+)$ | $4.09 \mathrm{E}-03_{6.80 E-04}(-)$ | $1.62 \mathrm{E}-03_{1.30 E-04}(+)$ |
|  | 3 | $2.53 \mathrm{E}-04_{4.40 E-05}$ | $4.40 \mathrm{E}-05_{1.30 E-05}(+)$ | $3.99 \mathrm{E}-04_{3.90 E-05}(-)$ | $3.16 \mathrm{E}-03_{6.40 E-04}(-)$ |
|  | 5 | $6.69 \mathrm{E}-04_{1.20 E-04}$ | $1.82 \mathrm{E}-04_{1.20 E-05}(+)$ | $2.39 \mathrm{E}-03_{3.60 E-04}(-)$ | $3.31 \mathrm{E}-03_{3.31 E-03}(-)$ |
| DTLZ2 | 8 | $4.17 \mathrm{E}-03_{7.90 E-04}$ | $2.20 \mathrm{E}-03_{2.80 E-03}(+)$ | $5.04 \mathrm{E}-03_{4.70 E-04}(-)$ | $3.02 \mathrm{E}-03_{7.40 E-05}(+)$ |
|  | 10 | $7.02 \mathrm{E}-03_{1.30 E-03}$ | $5.20 \mathrm{E}-03_{1.50 E-03}(+)$ | $6.62 \mathrm{E}-03_{2.20 E-04}(-)$ | $4.36 \mathrm{E}-03_{1.50 E-04}(+)$ |
|  | 15 | $3.23 \mathrm{E}-03_{5.80 E-04}$ | $2.22 \mathrm{E}-03_{8.30 E-04}(+)$ | $6.54 \mathrm{E}-03_{1.10 E-04}(-)$ | $2.79 \mathrm{E}-03_{1.80 E-05}(+)$ |
|  | 3 | $4.71 \mathrm{E}-04_{5.20 E-05}$ | $1.18 \mathrm{E}-04_{2.20 E-05}(+)$ | $4.15 \mathrm{E}-04_{3.00 E-05}(+)$ | $5.46 \mathrm{E}-03_{1.10 E-03}(-)$ |
|  | 5 | $2.77 \mathrm{E}-03_{1.90 E-04}$ | $7.72 \mathrm{E}-04_{5.60 E-04}(+)$ | $8.43 \mathrm{E}-03_{1.20 E-03}(-)$ | $3.42 \mathrm{E}-03_{2.30 E-04}(-)$ |
| DTLZ3 | 8 | $4.17 \mathrm{E}-03_{7.90 E-04}$ | $2.75 \mathrm{E}-03_{2.00 E-03}(+)$ | $4.02 \mathrm{E}-03_{1.90 E-03}(+)$ | $2.94 \mathrm{E}-03_{7.70 E-05}(+)$ |
|  | 10 | $7.02 \mathrm{E}-03_{1.30 E-03}$ | $3.44 \mathrm{E}-03_{1.80 E-03}(+)$ | $2.16 \mathrm{E}-03_{2.70 E-04}(+)$ | $4.95 \mathrm{E}-03_{1.40 E-04}(+)$ |
|  | 15 | $1.13 \mathrm{E}-02_{2.20 E-03}$ | $8.90 \mathrm{E}-04_{8.50 E-05}(+)$ | $5.61 \mathrm{E}-03_{9.50 E-04}(+)$ | $2.86 \mathrm{E}-03_{6.60 E-05}(+)$ |
|  | 3 | $1.05 \mathrm{E}-02_{6.30 E-03}$ | $3.58 \mathrm{E}-04_{1.60 E-05}(+)$ | $1.64 \mathrm{E}-03_{2.00 E-03}(+)$ | $1.56 \mathrm{E}-02_{9.20 E-03}(-)$ |
|  | 5 | $1.08 \mathrm{E}-02_{4.40 E-03}$ | $1.53 \mathrm{E}-03_{2.40 E-03}(+)$ | $4.23 \mathrm{E}-03_{1.70 E-03}(+)$ | $2.46 \mathrm{E}-03_{2.00 E-04}(+)$ |
| DTLZ4 | 8 | $6.21 \mathrm{E}-03_{1.40 E-03}$ | $1.29 \mathrm{E}-04_{6.00 E-06}(+)$ | $8.76 \mathrm{E}-03_{6.30 E-04}(-)$ | $1.68 \mathrm{E}-03_{4.90 E-05}(+)$ |
|  | 10 | $1.13 \mathrm{E}-02_{2.20 E-03}$ | $7.49 \mathrm{E}-04_{1.10 E-05}(+)$ | $1.65 \mathrm{E}-02_{8.30 E-04}(-)$ | $2.61 \mathrm{E}-03_{5.50 E-05}(+)$ |
|  | 15 | $9.37 \mathrm{E}-03_{8.50 E-04}$ | $1.24 \mathrm{E}-04_{1.80 E-05}(+)$ | $7.45 \mathrm{E}-03_{7.90 E-04}(+)$ | $1.54 \mathrm{E}-03_{8.80 E-06}(+)$ |

(continued on next page)

Table 10 (continued).

| Problem | Obj. | MCEDA/B | NSGA-III | MOEA/D | RM-MEDA |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | 3 | $1.84 \mathrm{E}-05_{1.80E-05}$ | $1.58 \mathrm{E}-04_{2.30E-05}(-)$ | $2.85 \mathrm{E}-05_{1.90E-05}(-)$ | $1.84 \mathrm{E}-03_{1.10E-03}(-)$ |
|  | 5 | $1.68 \mathrm{E}-03_{4.70E-04}$ | $1.90 \mathrm{E}-03_{4.80E-04}(-)$ | $2.36 \mathrm{E}-03_{4.70E-04}(-)$ | $2.61 \mathrm{E}-03_{2.80E-04}(-)$ |
| DTLZ5 | 8 | $2.06 \mathrm{E}-03_{1.70E-04}$ | $1.20 \mathrm{E}-03_{3.70E-05}(+)$ | $4.07 \mathrm{E}-03_{1.30E-04}(-)$ | $2.46 \mathrm{E}-03_{2.50E-04}(-)$ |
|  | 10 | $2.88 \mathrm{E}-03_{2.00E-04}$ | $2.60 \mathrm{E}-03_{1.10E-04}(+)$ | $6.98 \mathrm{E}-03_{5.70E-04}(-)$ | $4.00 \mathrm{E}-03_{4.10E-04}(-)$ |
|  | 15 | $1.05 \mathrm{E}-03_{1.60E-04}$ | $1.43 \mathrm{E}-03_{3.60E-04}(-)$ | $4.44 \mathrm{E}-03_{2.30E-04}(-)$ | $1.77 \mathrm{E}-03_{5.50E-05}(-)$ |
|  | 3 | $5.31 \mathrm{E}-05_{5.30E-05}$ | $1.62 \mathrm{E}-03_{3.10E-04}(-)$ | $2.09 \mathrm{E}-05_{1.80E-05}(+)$ | $8.86 \mathrm{E}-03_{2.80E-03}(-)$ |
|  | 5 | $2.07 \mathrm{E}-03_{3.10E-04}$ | $3.02 \mathrm{E}-03_{1.50E-04}(-)$ | $1.52 \mathrm{E}-03_{1.70E-04}(+)$ | $2.80 \mathrm{E}-03_{1.30E-04}(-)$ |
| DTLZ6 | 8 | $3.22 \mathrm{E}-03_{6.00E-04}$ | $2.23 \mathrm{E}-03_{1.50E-03}(+)$ | $3.47 \mathrm{E}-03_{5.30E-04}(-)$ | $2.62 \mathrm{E}-03_{6.00E-05}(+)$ |
|  | 10 | $5.13 \mathrm{E}-03_{1.20E-03}$ | $6.25 \mathrm{E}-03_{1.20E-03}(-)$ | $5.09 \mathrm{E}-03_{7.30E-04}(+)$ | $3.93 \mathrm{E}-03_{7.50E-05}(+)$ |
|  | 15 | $2.88 \mathrm{E}-03_{2.50E-04}$ | $1.39 \mathrm{E}-03_{3.80E-04}(+)$ | $2.71 \mathrm{E}-03_{2.20E-04}(+)$ | $2.46 \mathrm{E}-03_{4.10E-05}(+)$ |
|  | 3 | $1.39 \mathrm{E}-03_{2.90E-03}$ | $3.17 \mathrm{E}-04_{6.20E-06}(+)$ | $8.10 \mathrm{E}-04_{2.20E-05}(+)$ | $2.60 \mathrm{E}-02_{4.90E-03}(-)$ |
|  | 5 | $5.28 \mathrm{E}-03_{2.80E-03}$ | $6.69 \mathrm{E}-03_{1.90E-03}(-)$ | $2.85 \mathrm{E}-03_{1.10E-04}(+)$ | $8.56 \mathrm{E}-03_{7.20E-04}(-)$ |
| DTLZ7 | 8 | $8.06 \mathrm{E}-03_{1.60E-03}$ | $5.60 \mathrm{E}-03_{1.00E-04}(+)$ | $4.48 \mathrm{E}-03_{5.60E-04}(+)$ | $5.78 \mathrm{E}-03_{2.20E-04}(+)$ |
|  | 10 | $1.33 \mathrm{E}-02_{1.60E-03}$ | $6.41 \mathrm{E}-03_{4.20E-04}(+)$ | $7.43 \mathrm{E}-03_{1.10E-03}(+)$ | $8.06 \mathrm{E}-03_{1.30E-04}(+)$ |
|  | 15 | $1.03 \mathrm{E}-02_{7.20E-04}$ | $2.70 \mathrm{E}-03_{1.80E-04}(+)$ | $6.92 \mathrm{E}-03_{3.70E-04}(+)$ | $5.74 \mathrm{E}-03_{2.50E-05}(+)$ |

The symbol " $=$ " denote that the IGD results of the proposed algorithm and algorithms compared are statistically identical according to the Mann-Whitney rank test at the 5% significance level. The symbol " + " and " - " denote whether the IGD results of the compared algorithms are better or worse than that of the proposed algorithms according to the mean value and standard deviation.

## References

[1] K. Deb, A. Pratap, S. Agarwal, T. Meyarivan, A fast and elitist multiobjective genetic algorithm: NSGA-II, IEEE Trans. Evol. Comput. 6 (2) (2002) 182-197, http://dx.doi.org/10.1109/4235.996017.
[2] B. Li, J. Li, K. Tang, X. Yao, Many-objective evolutionary algorithms: A survey, ACM Comput. Surv. 48 (1) (2015) 13.
[3] J.H. Zhu, W.H. Zhang, L. Xia, Topology optimization in aircraft and aerospace structures design, Arch. Comput. Methods Eng. 23 (4) (2016) 595-622, http: //dx.doi.org/10.1007/s11831-015-9151-2.
[4] R. Jafarkhani, S.F. Masri, Finite element model updating using evolutionary strategy for damage detection, Comput.-Aided Civil Infastruct. Eng. 26 (3) (2011) 207-224, http://dx.doi.org/10.1111/j.1467-8667.2010.00687.x.
[5] A.M. Raich, T.R. Liszkai, Multi-objective optimization of sensor and excitation layouts for frequency response function-based structural damage identification, Comput.-Aided Civil Infastruct. Eng. 27 (2) (2012) 95-117, http://dx.doi. org/10.1111/j.1467-8667.2011.00726.x.
[6] R.T. Marler, J.S. Arora, Survey of multi-objective optimization methods for engineering, Struct. Multidiscip. Optim. 26 (6) (2004) 369-395, http://dx.doi. org/10.1007/s00158-003-0368-6.
[7] K. Deb, H. Jain, An evolutionary many-objective optimization algorithm using reference-point-based nondominated sorting approach, part I: solving problems with box constraints, IEEE Trans. Evol. Comput. 18 (4) (2014) 577-601, http://dx.doi.org/10.1109/tevc.2013.2281535.
[8] M. Pelikan, M.W. Hauschild, F.G. Lobo, Introduction to estimation of distribution algorithms, MEDAI, Rep. (2012003) (2012).
[9] M. Pelikan, D.E. Goldberg, E.E. Cant, Linkage problem, distribution estimation, and bayesian networks, Evol. Comput. 8 (3) (2000) 311-340, http://dx.doi. org/10.1162/106365600750078808.
[10] L.Mart, J. Garcia, A. Berlanga, C. Coello, J.M. Molina. On current model-building methods for multi-objective estimation of distribution algorithms: shortcomings and directions for improvement, Department of Informatics of the Universidad Carlos III de Madrid, Madrid, Spain, Tech. Rep. GIAA2010E001, 2010.
[11] Q. Zhang, H. Li, MOEA/D: A multiobjective evolutionary algorithm based on decomposition, IEEE Trans. Evol. Comput. 11 (6) (2007) 712-731, http://dx. doi.org/10.1109/tevc.2007.892759.
[12] Q. Zhang, W. Liu, H. Li, The performance of a new version of MOEA/D on CEC09 unconstrained MOP test instances, in: 2009 IEEE Congress on Evolutionary Computation, pp. 203-208, http://dx.doi.org/10.1109/CEC.2009.4982949.
[13] A. Mukhopadhyay, U. Maulik, S. Bandyopadhyay, C.A.C. Coello, A survey of multiobjective evolutionary algorithms for data mining: part 1, IEEE Trans. Evol. Comput. 18 (1) (2014) 4-19, http://dx.doi.org/10.1109/tevc.2013. 2290086.
[14] K. Deb, Multi-objective Optimization using Evolutionary Algorithms, Vol. 16, Wiley, 2001.
[15] K. Deb, D.K. Saxena, Searching for pareto-optimal solutions through dimensionality reduction for certain large-dimensional multi-objective optimization problems, in: Proceedings of the World Congress on Computational Intelligence (WCCI-2006), pp. 3352-3360.
[16] H. Ishibuchi, N. Tsukamoto, Y. Nojima, leee, Evolutionary many-objective optimization: A short review, in: 2008 leee Congress on Evolutionary Computation, Vols 1-8, 2008, pp. 2419-2426.
[17] H. Aguirre, K. Tanaka, Many-objective optimization by space partitioning and adaptive epsilon-ranking on MNK-landscapes, in: M. Ehrgott, C.M. Fonseca, X. Gandibleux, J.K. Han, M. Sevaux (Eds.), Evolutionary Multi-Criterion Optimization: 5th International Conference, Emo 2009, in: Lecture Notes in Computer Science, vol. 5467, 2009, pp. 407-*.
[18] H. Ishibuchi, Y. Sakane, N. Tsukamoto, Y. Nojima, leee, Evolutionary manyobjective optimization by NSGA-II and MOEA/D with large populations, in: 2009 leee International Conference on Systems, Man and Cybernetics, in: IEEE International Conference on Systems Man and Cybernetics Conference Proceedings, 2009, pp. 1758-1763, http://dx.doi.org/10.1109/icsmc. 2009.5346628.
[19] X. Guo, Y. Wang, X. Wang, Using objective clustering for solving manyobjective optimization problems, Math. Probl. Eng. 2013 (2013).
[20] H. Jain, K. Deb, An evolutionary many-objective optimization algorithm using reference-point based nondominated sorting approach, part ii: handling constraints and extending to an adaptive approach, IEEE Trans. Evol. Comput. 18 (4) (2014) 602-622, http://dx.doi.org/10.1109/tevc.2013.2281534.
[21] L. Cai, S.R. Qu, Y. Yuan, X. Yao, A clustering-ranking method for manyobjective optimization, Appl. Soft Comput. 35 (2015) 681-694, http://dx.doi. org/10.1016/j.asoc.2015.06.020.
[22] X. Cai, Z. Yang, Z. Fan, Q. Zhang, Decomposition-based-sorting and angle-based-selection for evolutionary multiobjective and many-objective optimization, IEEE Trans. Cybern. PP (99) (2017) 1-14, http://dx.doi.org/10.1109/ TCYB. 2016.2586191.
[23] H. Xing, Z. Wang, T. Li, H. Li, R. Qu, An improved MOEA/D algorithm for multi-objective multicast routing with network coding, Appl. Soft Comput. 59 (2017) 88-103, http://dx.doi.org/10.1016/j.asoc.2017.05.033.
[24] X. Meng, J. Li, M. Zhou, X. Dai, J. Dou, Population-based incremental learning algorithm for a serial colored traveling salesman problem, IEEE Trans. Syst. Man Cybern.: Syst. 48 (2) (2018) 277-288, http://dx.doi.org/10.1109/TSMC. 2016.2591267.
[25] J. Bai, H. Liu, Multi-objective artificial bee algorithm based on decomposition by PBI method, Appl. Intell. 45 (4) (2016) 976-991.
[26] Y. Han, D. Gong, Y. Jin, Q. Pan, Evolutionary multiobjective blocking lotstreaming flow shop scheduling with machine breakdowns, IEEE Trans. Cybern. 42 (C) (2017) 229-245.
[27] X.-W. Zheng, X.-M. Yu, Y. Li, H. Liu, An enhanced multi-objective group search optimizer based on multi-producer and crossover operator, J. Inf. Sci. Eng. 33 (1) (2017) 37-50.
[28] J.-q. Li, H.-y. Sang, Y.-y. Han, C.-g. Wang, K.z. Gao, Efficient multi-objective optimization algorithm for hybrid flow shop scheduling problems with setup energy consumptions, J. Cleaner Prod. 181 (2018) 584-598.
[29] M. Hauschild, M. Pelikan, An introduction and survey of estimation of distribution algorithms, Swarm Evol. Comput. 1 (3) (2011) 111-128, http://dx.doi. org/10.1016/j.sweco.2011.08.003.
[30] M. Laumanns, J. Ocenasek, Bayesian Optimization Algorithms for Multiobjective Optimization, Springer Berlin Heidelberg, Berlin, Heidelberg, 2002, pp. 298-307, http://dx.doi.org/10.1007/3-540-45712-7_29.
[31] J. Ocenasek, S. Kern, N. Hansen, P. Koumoutsakos, A mixed bayesian optimization algorithm with variance adaptation, in: International Conference on Parallel Problem Solving from Nature, Springer, 2004, pp. 352-361.
[32] M. Pelikan, Bayesian optimization algorithm: from single level to hierarchy, Thesis, 2002.

[33] M. Pelikan, D.E. Goldberg, Escaping hierarchical traps with competent genetic algorithms, in: Proceedings of the 3rd Annual Conference on Genetic and Evolutionary Computation, Morgan Kaufmann Publishers Inc., 2001, pp. 511518
[34] M. Pelikan, D.E. Goldberg, E. Cant-Paz, BOA: the bayesian optimization algorithm, in: Proceedings of the 1st Annual Conference on Genetic and Evolu-tionary Computation-Volume 1, Morgan Kaufmann Publishers Inc., 1999, pp. 525-532.
[35] M. Pelikan, D.E. Goldberg, S. Tsutsui, Hierarchical bayesian optimization algorithm: toward a new generation of evolutionary algorithms, DBLP, 2003, pp. 2738-2743 Vol.3.
[36] M. Pelikan, K. Sastry, D.E. Goldberg, Multiobjective hBOA, clustering, and scalability, in: Proceedings of the 7th annual conference on Genetic and evolutionary computation, ACM, 2005, pp. 663-670.
[37] J.R. Caldwell, R.A. Watson, How to get more from your model: the role of constructive selection in estimation of distribution algorithms, 2017, http: //dx.doi.org/10.1145/3067695.3076049.
[38] M.S. Martins, M. El Yafrani, M.R. Delgado, M. Wagner, B. Ahiod, R. Lders, HSEDA: a heuristic selection approach based on estimation of distribution algorithm for the travelling thief problem, in: Proceedings of the Genetic and Evolutionary Computation Conference, ACM, 2017, pp. 361-368.
[39] T.D. Mihoc, A New Estimation of Distribution Algorithm for Nash Equilibria Detection, Springer, 2017, pp. 99-107.
[40] M. Zangari, A. Mendiburu, R. Santana, A. Pozo, Multiobjective decompositionbased mallows models estimation of distribution algorithm. a case of study for permutation flowshop scheduling problem, Inform. Sci. 397 (2017) 137-154.
[41] F. Lane, R.M.A. Azad, C. Ryan, DICE: a new family of bivariate estimation of distribution algorithms based on dichotomised multivariate Gaussian distributions, in: European Conference on the Applications of Evolutionary Computation, Springer, 2017, pp. 670-685.
[42] S. Baluja, Population-based Incremental Learning. A Method for Integrating Genetic Search Based Function Optimization and Competitive Learning, Report, Carnegie-Mellon Univ Pittsburgh Pa Dept Of Computer Science, 1994.
[43] C.W. Ahn, R.S. Ramakrishna, D.E. Goldberg, Real-coded Bayesian Optimization Algorithm, Springer Berlin Heidelberg, Berlin, Heidelberg, 2006, pp. 51-73, http://dx.doi.org/10.1007/3-540-32494-1_3.
[44] Q.F. Zhang, A.M. Zhou, Y.C. Jin, RM-MEDA: A regularity model-based multiobjective estimation of distribution algorithm, IEEE Trans. Evol. Comput. 12 (1) (2008) 41-63, http://dx.doi.org/10.1109/tevc.2007.894202.
[45] L. Mo, G. Dai, J. Zhu, The RM-MEDA based on elitist strategy, Adv. Comput. Intell. (2010) 229-239.
[46] Y. Li, X. Xu, P. Li, L Jian, Improved RM-MEDA with local learning, Soft Comput. 18 (7) (2014) 1383-1397.
[47] D. Heckerman, D. Geiger, D.M. Chickering, Learning bayesian networks: the combination of knowledge and statistical data, Mach. Learn. 20 (3) (1995) 197-243, http://dx.doi.org/10.1023/a:1022623210503.
[48] O.R. Castro, R. Santana, A. Pozo, C-Multi: A competent multi-swarm approach for many-objective problems, Neurocomputing 180 (2016) 68-78, http://dx. doi.org/10.1016/j.neucom.2015.06.097.
[49] L. Mart, J. Garca, A. Berlanga, J.M. Molina, MONEDA: scalable multi-objective optimization with a neural network-based estimation of distribution algorithm, J. Global Optim. 66 (4) (2016) 729-768, http://dx.doi.org/10.1007/ s10898-016-0415-7.
[50] L. Mart, J. Garca, A. Berlanga, C.A. Coello Coello, J.M. Molina, MB-GNG: Addressing drawbacks in multi-objective optimization estimation of distribution algorithms, Oper. Res. Lett. 39 (2) (2011) 150-154, http://dx.doi.org/10. 1016/j.otl.2011.01.002.
[51] S. Das, P.N. Suganthan, Differential evolution: a survey of the state-of-the-art, IEEE Trans. Evol. Comput. 15 (1) (2011) 4-31, http://dx.doi.org/10.1109/tevc. 2010.2059031.
[52] R. Denysiuk, L. Costa, I.E. Santo, Clustering-Based Selection for Evolutionary Many-Objective Optimization, in: Lecture Notes in Computer Science, vol. 8672, 2014, pp. 538-547.
[53] F. Lavinia, C. Corina, Multi-objective genetic algorithm with clustering-based ranking and direct control of diversity, in: 2013 17th International Conference on System Theory, Control and Computing, 2013, pp. 213-218.
[54] D. Pradhan, S. Wang, S. Ali, T. Yue, M. Liaaen, leee, CBCA-ES: A clusterbased genetic algorithm with elitist selection for supporting multi-objective test optimization, in: 2017 10th leee International Conference on Software Testing, Verification and Validation, in: IEEE International Conference on Software Testing Verification and Validation, 2017, pp. 367-378, http://dx. doi.org/10.1109/scst.2017.40.
[55] G.T. Pulido, C.A.C. Coello, Using clustering techniques to improve the performance of a multi-objective particle swarm optimizer, in: Genetic and Evolutionary Computation - Gecco 2004, Pt 1, Proceedings, in: Lecture Notes in Computer Science, vol. 3102, Springer-Verlag Berlin, Berlin, 2004, pp. 225237.
[56] C. von Lucken, C. Brizuela, B. Baran, Clustering Based Parallel Many-Objective Evolutionary Algorithms Using the Shape of the Objective Vectors, in: Lecture Notes in Computer Science, vol. 9019, 2015, pp. 50-64, http://dx.doi.org/10. 1007/978-3-319-15892-1_4.
[57] O.R. Castro, A. Pozo, J.A. Lozano, R. Santana, An investigation of clustering strategies in many-objective optimization: the i-Multi algorithm as a case study, Swarm Intell. 11 (2) (2017) 101-130, http://dx.doi.org/10.1007/ s11721-017-0134-9.
[58] M.M. Deza, E. Deza, Encyclopedia of distances, in: Encyclopedia of Distances, Springer, 2009, pp. 1-583.
[59] N. Kambhatla, T.K. Leen, Dimension reduction by local principal component analysis, Neural Comput. 9 (7) (1997) 1493-1516, http://dx.doi.org/10.1162/ neco.1997.9.7.1493.
[60] K. Deb, L. Thiele, M. Laumanns, E. Zitzler, Scalable Test Problems for Evolutionary Multiobjective Optimization, Springer London, London, 2005, pp. 105145, http://dx.doi.org/10.1007/1-84628-137-7_6.
[61] J.J. Durillo, A.J. Nebro, JMetal: A Java framework for multi-objective optimization, Adv. Eng. Softw. 42 (10) (2011) 760-771, http://dx.doi.org/10.1016/j. advengsoft.2011.05.014.
[62] J.J. Durillo, A.J. Nebro, E. Alba, The JMetal framework for multi-objective optimization: Design and architecture, in: Evolutionary Computation (CEC), 2010 IEEE Congress on, IEEE, 2010, pp. 1-8.
[63] A.J. Nebro, J.J. Durillo, M. Vergne, Redesigning the JMetal multi-objective optimization framework, in: Proceedings of the Companion Publication of the 2015 Annual Conference on Genetic and Evolutionary Computation, ACM, 2015, pp. 1093-1100.
[64] I. Das, J.E. Dennis, Normal-boundary intersection: a new method for generating the pareto surface in nonlinear multicriteria optimization problems, SIAM J. Optim. 8 (3) (1998) 631-657, http://dx.doi.org/10.1137/ s1052623496307510.
[65] H. Ishibuchi, Y. Sakane, N. Tsukamoto, Y. Nojima, Evolutionary manyobjective optimization by NSGA-II and MOEA/D with large populations, in: Systems, Man and Cybernetics, 2009. SMC 2009. IEEE International Conference on, IEEE, pp. 1758-1763.
[66] K. Deb, R.B. Agrawal, Simulated binary crossover for continuous search space, Complex Syst. 9 (3) (1994) 1-15.
[67] Z.A. He, G.G. Yen, Visualization and performance metric in many-objective optimization, IEEE Trans. Evol. Comput. 20 (3) (2016) 386-402, http://dx.doi. org/10.1109/tevc.2015.2472283.
[68] D.J. Walker, R.M. Everson, J.E. Fieldsend, Visualizing mutually nondominating solution sets in many-objective optimization, IEEE Trans. Evol. Comput. 17 (2) (2013) 165-184, http://dx.doi.org/10.1109/tevc.2012.2225064.
[69] M. Li, L. Zhen, X. Yao, How to read many-objective solution sets in parallel coordinates [educational forum], IEEE Comput. Intell. Mag. 12 (4) (2017) 88100 .