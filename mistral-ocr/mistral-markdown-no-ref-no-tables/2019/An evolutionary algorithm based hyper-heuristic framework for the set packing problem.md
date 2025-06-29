# An evolutionary algorithm based hyper-heuristic framework for the set packing problem 

Sachchida Nand Chaurasia ${ }^{a, b}$, Joong Hoon Kim ${ }^{c, *}$<br>${ }^{a}$ Research Center for Disaster Prevention Science and Technology, Korea University, Seoul, 02841, South Korea<br>${ }^{b}$ Operational Research Lab, School of Electronic Engineering and Computer Science, Queen Mary University of London, London E1 4FZ,<br>United Kingdom<br>${ }^{c}$ School of Civil, Environmental and Architectural Engineering, Korea University, Seoul, 02841, South Korea

## A R T I C L E I N F O

Article history:
Received 13 June 2018
Revised 17 July 2019
Accepted 19 July 2019
Available online 19 July 2019

Keywords:
Set packing problem
Estimation of distribution algorithm
Guided-mutation
Heuristic
Hyper-heuristic
Minimum weight dominating set problem

## A B S T R A C T

In recent years, hyper-heuristics have received massive attention from the research community as an alternative of meta-heuristics. In a hyper-heuristic, generation or selection of an effective heuristic among a pool of heuristics is an important and challenging task in the search process. At each iteration, a suitable heuristic can take the search process toward the global optimal solution. Moreover, some additional factors such as quality and the number of heuristics also affect the performance. In this paper, we propose an evolutionary algorithm based hyper-heuristic framework that incorporates dynamic selection of parameters. To test its generality, effectiveness and robustness, we apply this approach on two different $\mathcal{N} \mathcal{P}$-hard problems - set packing problem (SPP) and minimum weight dominating set (MWDS) problem. The proposed approach for the SPP and the MWDS problem has been evaluated respectively on their respective set of benchmark instances. Computational results show that the proposed approach for the SPP and MWDS problem perform much better than their respective state-of-the-art approaches in terms of the solution quality and computational time.
(c) 2019 Elsevier Inc. All rights reserved.

## 1. Introduction

The set packing problem (SPP), considered to closely resemble a set covering problem [20,37], is a classical combinatorial optimization problem and has been proven to be $\mathcal{N} \mathcal{P}$-hard [18] in nature. We followed the same notational representation as in [14] to represent the SPP and is defined as follows: Consider a finite set $\mathcal{I}=\{1, \ldots, \mathbf{N}\}$ of $\mathbf{N}$ objects, $\mathcal{T}_{j}, j \in \mathcal{J}=\{1, \ldots, \mathbf{M}\}$ a list of $\mathbf{M}$ subsets of $\mathcal{I}$, and a packing $\mathcal{P} \subseteq \mathcal{I}$ is a subset of set $\mathcal{I}$ such that $\left|\mathcal{T}_{j} \cap \mathcal{P}\right| \leqslant 1, \forall j \in \mathcal{J}$. i.e., at most one object of set $\mathcal{T}_{j}$ can be in packing $\mathcal{P}$. Each set $\mathcal{T}_{j}, j \in \mathcal{J}=\{1, \ldots, \mathbf{M}\}$ is considered as an exclusive constraint between some objects of set $\mathcal{I}$. A weight function assigns a positive integer weight, $c_{i}$, to each object $i$ in set $\mathcal{I}$. The objective of the SPP is to find a subset $\mathcal{P} \subseteq \mathcal{I}$ that maximizes the sum of the weights of the objects in set $\mathcal{P}$. Mathematical model of the SPP is given as follows:

$$
\operatorname{Max} \mathbf{Z}=\sum_{i \in \mathcal{I}} c_{i} x_{i}
$$

[^0]
[^0]:    * Corresponding author.

    E-mail address: jaykim@korea.ac.kr (J.H. Kim).

$$
\begin{aligned}
& \sum_{i \in \mathcal{I}} t_{i, j} x_{i} \leqslant 1, \forall j \in \mathcal{J} \\
& x_{i} \in\{0,1\}, \forall i \in \mathcal{I} \\
& t_{i, j} \in\{0,1\}, \forall i \in \mathcal{I}, \forall j \in \mathcal{J}
\end{aligned}
$$

- a vector $\mathcal{X}=\left(x_{i}\right)$, where $x_{i}= \begin{cases}1, & \text { if } i \in \mathcal{P} \\ 0, & \text { otherwise }\end{cases}$
- a vector $\mathcal{C}=\left(c_{i}\right)$, where $c_{i}=$ weight of object $i, \forall i \in \mathcal{I}$
- a matrix $\mathcal{T}=\left(t_{i, j}\right)$, where $t_{i, j}= \begin{cases}1, & \text { if } i \in \mathcal{T}_{j} \\ 0, & \text { otherwise }\end{cases}$

Eq. (1) is the objective function that calculates the sum of the weights of the objects in packing $\mathcal{P}$. Eq. (2) ensures that at most one object from set $\mathcal{T}_{j}$ can be packed in packing $\mathcal{P}$. In Eq. (3), $x_{i}$ is a binary variable. If object $i$ is in packing $\mathcal{P}$, then $x_{i}=1$; otherwise, $x_{i}=0$. In Eq. (4), $t_{i, j}$ is a binary variable and its value is 1 if object $i$ belongs to set $\mathcal{T}_{j}$; otherwise, it is 0 .

A special case of the SPP is a node packing problem represented in Eq. (5), where constraints are defined between a pair of items.

$$
\left[\begin{array}{l}
\operatorname{Max} \mathbf{Z}=\sum_{i \in \mathcal{I}} c_{i} x_{i} \\
x_{i}+x_{j} \leqslant 1, \forall \text { pair }(i, j) \text { of incompatible items, } \\
x_{i} \in\{0,1\}, \forall i \in \mathcal{I}
\end{array}\right]
$$

# 1.1. Survey on the set packing problem and related problems 

The SPP is an $\mathcal{N} \mathcal{P}$-hard problem and its hardness is explained in detail in [20,37]. The Branch-and-cut algorithm, uses polyhedral theory [39], was the best exact approach for solving the SPP. However, owing to the solving limitation of an exact approach, only small instances are solved to optimality. For large instances, other approaches such as meta-heuristic approaches should be considered, which play an important role in determining the solution of acceptable quality in a reasonable amount of computational time. Considering the limitations of the exact approaches, Delorme et al. [14] proposed a greedy randomized adaptive search procedure (GRASP) which operates in two main phases. In the first phase, called a construction phase, an initial solution is generated using a greedy randomized procedure in which randomness allows to explore different search areas. In the second phase, a local search is applied to each solution generated in the first phase to further improve it. Further, an intensification phase based on the path relinking method [41] was applied. In the study reported in [14], two different types of instances were used: real railway problem and random instances. In [17], an ant colony optimization (ACO) was proposed for solving the SPP, and only random instances were used for investigating the performance of the ACO. Further, in [16] and [34], two different versions of ACO were proposed for the SPP, and both were tested on the railway problem instances. The state-of-the-art approach for solving the SPP is an evolutionary algorithm (EA) with guided mutation (GM) (i.e., EA/G) [11]. The EA/G approach is considered as a cross between traditional genetic algorithm and estimation of distribution algorithm. The GM operator uses the cross information to generate offspring. The solutions generated by the EA/G approach are subjected to a local search algorithm to further improve the solution quality. The EA/G with local search was applied to unit-cost and multi-cost random instances.

Many real-world applications of the SPP have been reported in the literature. In [42], Rönnqvist presented the use of a SPP to formulate the cutting stock problem and solved it using a combination of the Lagrangian relaxation method and sub-gradient optimization. In [30], Kim and Lee mapped a ship scheduling problem as the SPP and solved it using LINDO software. In [35], a SPP formulation was used to obtain the bounds for a resource-constrained project scheduling problem using the greedy method. In [47], Tajima and Misono formulated an airline seat allocation/reallocation problem as a SPP and solved it using the IBM optimization subroutine library. In [43], Rossi and Smriglio described the development of a SPP-based model for a ground holding problem and solved it using a Branch-and-cut method. In [15], Delorme et al. used a unit-cost SPP to model the railway infrastructure saturation problem and solved it using a GRASP meta-heuristic.

In [33], Lusby et al. formulated a routing of trains through junctions problem as a SPP and solved it using a branch-andprice algorithm. In the given problem, the tracks and time are divided into sections and time periods, respectively. Further, pairs of track sections and time periods are mapped as objects into a SPP with the objective to maximize the number of trains that can be assigned to pairs of track sections and time periods. It ensures that at any particular time period at most one train can be assigned to a pair of track section and time period. It also ensures that at any particular time period only one train can be assigned to any particular track section. Pairs of track sections and time periods are considered as objects in the SPP. The constraints of the SPP are the conflicts among different pairs of track sections and time periods that cannot be put together in the solution. A set of trains without any priority or with equal priority will address a unit-cost SPP, whereas with different priority will address multi-cost SPP. In [49], Xu and Zhang proposed a path set packing problem, is

a variant of a SPP, with the goal is to find a maximum number of edge-disjoint paths in a given graph, and the goal was achieved using a polynomial time optimal algorithm.

Several other versions of SPP are reported in the literature. In [27], Jia et al. studied a m-set packing problem, which is an extension of SPP, where the size of the set is bounded by $m$, and was solved using an efficient parametrized algorithm. In [38], Nguyen studied a complete set packing problem (CSPP). The CSPP has applications in combinatorial auctions and cooperative game theory. A winner determination problem in spectrum auctions and the coalition structure generation problem in coalition skill games is modeled as the CSPP and solved it using a fast approximation algorithm. In [23], Gulek and Toroslu studied a tree-like weighted set packing problem and solved it using a dynamic programming algorithm. This problem has been proven to be $\mathcal{P}$ and the complexity is $\mathcal{O}\left(k^{2} n\right)$. This problem has application in the task assignment of hierarchical organizations. In [45], Sviridenko and Ward studied a maximum un-weighted set packing problem in which set cardinality is upper bounded by a constant $k$. The goal of the problem is to find a packing with maximum cardinality. A large neighborhood local search algorithm is proposed to solve this problem. In [21], Gottlob and Greco presented a maximum-weight set packing problem which mapped a winner determination problem in combinatorial auctions in which it determines the allocation of items to the bidders such that the sum of the accepted bid prices is maximum. In [25], Heismann and Borndrfer proposed a generalization of odd set inequalities for a SPP for hyper-graph by employing cliques and odd set inequalities. In the context of hyper-graph, a SPP becomes an edge packing problem.

In this paper, we present an evolutionary algorithm (EA) based hyper-heuristic (EA-HH) framework to solve the SPP. The EA is inspired by the EA/G approach proposed in [50]. In the EA-HH approach, the concept of estimation of the distribution of the solutions in the solution space is used to estimate the distribution of heuristics in the search space of heuristics. Hyper-heuristics [5] are recently developed methods that operate directly on the search space of the heuristics and are independent of the problem structure. In general, almost, all meta-heuristics operate directly on the solution space of the problem under consideration and their performance may change on different problems in the same domain, and it may outperform/under-perform with a small change in the same problem. A hyper-heuristic is considered as an automated heuristic search method that provides sufficient flexibility to the process of selection, generating, combining or adapting several simple or problem specific heuristics to efficiently solve the computationally hard problem. Other important aspects of any heuristic are the scalability, stability, robustness, and generality. A well-designed approach can have the ability to perform well irrespective of problem domains. The novelty of the proposed approach is that it uses univariate marginal distribution model and population based incremental learning model to initialize and update, respectively, the probability vector which estimates the distribution of heuristics in the search space of the heuristics. Further, to investigate the scalability and stability of the EA-HH approach, the minimum weight dominating set (MWDS) problem is considered which is also a class of subset selection problem but has opposite objective than the SPP. The EA-HH approach is applied to solve the MWDS problem with the purpose to investigate the scalability and generality capability.

The remainder of this paper is organized as follows. Sections 2 and 3 present an overview of the EA/G approach and hyper-heuristics, respectively. Section 4 explains hyper-heuristics method. Section 5 describes the proposed EA-HH approach for the SPP. The computational results are reported in Section 6. Section 7 presents the MWDS problem, its components, and the computational results. Section 8 concludes the paper.

# 2. Overview of evolutionary algorithm with guided mutation (EA/G) 

The EA/G [50] is a recent addition to the class of evolutionary algorithms. It was developed by Zhang et al. [50] in 2005 with the intention of overcoming the shortcomings of traditional GAs [19] and (EDAs) [4,31]. In other words, the purpose was to take advantage of the features of GAs and EDAs together. GAs use the current location information of the solutions found so far in the solution space to generate a new offspring through standard operators such as crossover and mutation. GAs do not use, directly, the global statistical information in the process of generating an offspring. On the other hand, EDAs use the global statistical information, which is stored in the form of probability, to generate a new offspring. A new offspring is generated by sampling the probability vector. In contrast to GAs, EDAs do not directly use location information in the process of generating a new offspring.

In the EA/G, the guided mutation (GM) operator uses the features of both GAs and EDAs to generate a new offspring. The GM operator generates a new offspring either directly copying from the best solution or randomly sampling the probability vector.

More recently, several modified and improved versions of EA/G were developed and tested on a different domain of combinatorial optimization problems. In the study in [11], an improved version of EA/G was proposed to solve the SPP. The problem domain knowledge is used to initialize the probability of objects in the set. In the study in [8], the size of the parent was modified, whereas, in the study in [9], both the size of the parent and the number of solutions to update the probability vector were modified. In [10], the authors modified the original EA/G and applied it to an order acceptance and scheduling problem, which is a subset and permutation problem. For detailed study, please refer to [8-11,24].

## 3. Overview of hyper-heuristic

A hyper-heuristic is a heuristic search technique that automates the search process and also allows to combine or generate a suitable problem solver in each generation [5]. Generally, hyper-heuristic consists of two levels, namely; higher level

and lower level [5]. A High-level search strategy and a set of low-level heuristics reside at the higher level and lower level, respectively. The high-level search strategy directly operates on the search space of the heuristics. In each iteration, highlevel strategy applies a heuristic selection or heuristic generation method to select/generate a heuristic from the lower level and subsequently, this heuristic is applied to generate a new solution. The lower level consists of problem-specific/generic heuristics, called low-level heuristics that directly operate on the solution space of the problem under consideration. But the major challenge in hyper-heuristics is the selection of a heuristic from the heuristics pool. In the literature, several strategies have been developed to select/generate a heuristic from the heuristics pool such as simple random selection [13], greedy selection [13] and a choice function [13].

Several other versions of hyper-heuristic are presented in the literature. In [3], a tensor-based machine learning technique is proposed for selection hyper-heuristic. Further, a random heuristic selection with the naive, improving and equal move acceptance method are combined in a selection of low-level heuristic. In the study in [44], a Monte Carlo tree search method is proposed to generate a sequence of low-level heuristics. Further, the Monte Carlo is coupled with a population of solutions to improve the effectiveness of the search tree. In [22], Jacomine et al. put an effort to investigate the concept of heuristic space diversity and management of it under various strategies under meta-hyper-heuristic approach. In [2], Asta et al. applied hyper-heuristic with the combination of Monte-Carlo to solve the multi-mode resource-constrained multi-project scheduling problem. The hybrid version of the proposed approach is a combination of Monte-Carlo tree search, neighborhood moves, memetic algorithms, and hyper-heuristic. In [1], Almutairi et al. investigated six different existing selection hyper-heuristics namely: Sequence-based selection hyper-heuristic, Dominance-based and random descent hyperheuristic, Robinhood (round-robin neighbourhood) hyper-heuristic, Modified choice function, Fuzzy late acceptance-based hyper-heuristic [26], and Simple Random-Great Deluge in HyFlex problem domains such as 0-1 Knapsack, Quadratic Assignment, and Max-Cut problem. In [29], Ahmed and Ender proposed an iterated multi-stage selection hyper-heuristic and investigated on one-dimensional bin-packing, personal scheduling, permutation flow-shop, travelling salesman problem, and vehicle routing problem. In [12], a reinforcement learning technique is incorporated in hyper-heuristic and the performance is evaluated on six different problem domains. Several state-of-the-art hyper-heuristics [6], [12] are also developed for other domain problems.

# 4. Proposed evolutionary algorithm based hyper-heuristic 

This paper presents a novel evolutionary algorithm based hyper-heuristic inspired by the EA/G approach proposed by Zhang et al. [50]. As mentioned in Section 2, EDAs work on the concept of the estimation of the distribution of the promising solutions in the solution space. In each generation, it estimates the distribution of the promising solutions in the solution space and subsequently stores their distribution in the form of probability. On the other side, the higher level strategy of EAHH estimates the distribution of promising heuristics in the search space. The main components of the EA-HH are discussed below.

### 4.1. Higher level of the hyper-heuristic

An evolutionary algorithm is employed as a high-level strategy at the higher level of the hyper-heuristic. The main components of the higher level are explained in the following subsections:

### 4.1.1. High-level search strategy

The high-level of a hyper-heuristic is a search strategy that operates on the search space of the heuristics and selects or generates a heuristic by combining two or more heuristics from the heuristics pool. This section presents search strategy that is adopted at the higher level of the hyper-heuristic. Matrix in 6 is a heuristics population matrix of $\mathbf{N}_{\mathbf{p}} \times \mathbf{N}_{\mathbf{H}}$, where $\mathbf{N}_{\mathbf{p}}$ is the heuristics population size and $\mathbf{N}_{\mathbf{H}}$ is the number of low-level heuristics. The value of $f_{i N_{j}}, i=1,2, \ldots, \mathbf{N}_{\mathbf{p}}, j=1,2, \ldots \mathbf{N}_{\mathbf{H}}$, $\mathcal{H}_{j} \in\left\{\mathrm{LH}_{-} 1, \mathrm{LH}_{-} 2, \ldots, \mathrm{LH}_{-} \mathbf{N}_{\mathbf{H}}\right\}$ is determined by using Eq. (7).

$$
\mathcal{F}_{\text {Credit }}=\left[\begin{array}{cccc}
f_{1 N_{1}} & f_{1 N_{2}} & \cdots & f_{1 N_{N_{\mathbf{H}}}} \\
f_{2 N_{1}} & f_{2 N_{2}} & \cdots & f_{2 N_{N_{\mathbf{H}}}} \\
\vdots & \vdots & \ddots & \vdots \\
f_{\mathbf{N}_{\mathbf{p}} N_{1}} & f_{\mathbf{N}_{\mathbf{p}} N_{2}} & \cdots & f_{\mathbf{N}_{\mathbf{p}} N_{N_{\mathbf{H}}}}
\end{array}\right]
$$

$\mathcal{F}_{\text {Credit }}$ is a credit matrix that stores the fitness difference between the new solution and the current solution generated by each low-level heuristic in each generation in the search process. The difference is calculated as follows:

$$
f_{i N_{j}}= \begin{cases}f_{\text {New }}-f_{\text {Current }}, & \text { if }\left(f_{\text {New }}-f_{\text {Current }}\right)>0 \\ 0, & \text { otherwise }\end{cases}
$$

where $f_{\text {Current }}$ and $f_{\text {New }}$ are the fitness of the current solution and the fitness of the solution generated in the neighbourhood of the current solution, respectively.

# 4.1.2. Initialization and update of probability vector $\mathcal{P}_{\text {Heuristic }}$ 

In [36,50], the univariate marginal distribution (UMD) model was used to estimate the distribution of the candidate solutions in the population. In the UMD model, each decision variable is treated as an independent variable and the conditional probability of a variable does not depend on the probability of other variables. In the context of heuristics, the UMD model estimates the distribution of heuristics in the search space of the heuristics. Each heuristic is treated as an independent variable and probability vector $\mathcal{P}_{\text {Heuristic }}=\left\{\mathcal{P}_{N_{1}}, \mathcal{P}_{N_{2}}, \ldots, \mathcal{P}_{N_{p}}\right\} \in\left[0,1\right]^{N_{H}}$ characterizes the distribution of the promising heuristics in the search space, where $\mathcal{P}_{N_{k}}$ is the probability of $\mathcal{H}_{k}{ }^{\text {th }}$ heuristic in the heuristics pool. Eq. (8) is used to assign a probability to each heuristic $\mathcal{H}_{i}$.

$$
\mathcal{P}_{N_{i}}=\frac{\sum_{j=1}^{N_{p}} f_{j N_{i}}}{\sum_{k=1}^{N_{H}} \sum_{j=1}^{N_{p}} f_{j N_{k}}}, \quad i=1,2, \ldots \mathbf{N}_{\mathbf{H}}
$$

After the probability vector $\mathcal{P}_{N_{i}}$ has been initialized, at each generation $g$ the probability distribution of each heuristic $\mathcal{H}_{i}$ is updated using the best $\frac{\mathbf{N}_{\mathbf{p}}}{\mathbf{g}}$ fitness values from Eq. (6). A population-based incremental learning algorithm (PBILA) [4] is used to update the probability vector. Eq. (9) updates the probability vector at each generation. In Eq. (9), $\zeta$ is a learning variable that learns from the past statistical information stored in the form of the probability vector in the current population. The larger the value of $\zeta$, the greater is the contribution from the current population, whereas the smaller the value of $\zeta$, the greater is the contribution from the probability vector.

$$
\mathcal{P}_{N_{i}}=(1-\zeta) \times \mathcal{P}_{N_{i}}+\zeta \times \frac{\sum_{k=1}^{N_{p}} f_{k N_{i}}}{\sum_{k=1}^{N_{H}} \sum_{j=1}^{N_{p}} f_{j N_{k}}}, i=1,2, \ldots \mathbf{N}_{\mathbf{H}}
$$

The worst case time complexity of both the initialization and update of the probability vector is $\mathcal{O}\left(\mathbf{N}_{\mathbf{p}}{ }^{2} \mathbf{N}_{\mathbf{H}}\right)$.

### 4.1.3. Heuristic selection rule

Heuristic selection is an important component of any hyper-heuristic. It determines the direction of the search process in the search space. An intelligent heuristic selection method can take the search process toward the global best solution, whereas random selection may lead the search process toward the local best solution or may require a greater number of generations to reach the global best. Several heuristic selection rules have been developed such as random selection, choice function, and greedy selection. In this paper, we propose roulette wheel selection (RWS) method based heuristic selection rule. However, we tried all the mentioned methods but the RWS has, overall, the best performance. Therefore, we choose the RWS method as a heuristic selection rule.

Eq. (8) estimates the distribution of the heuristics in terms of their performance in each generation and stores the distribution in the form of probability in the probability vector $\mathcal{P}_{\text {Heuristic }}$. The probability $\mathcal{P}_{N_{i}}$ of heuristic $\mathcal{H}_{i}$ is directly proportional to its performance. The RWS method, also called the fitness proportionate selection method, considers the probability of each heuristic as a fitness of heuristic $\mathcal{H}_{i}$ and its probability of being selected is calculated as

$$
\varepsilon_{i}=\frac{\mathcal{P}_{N_{i}}}{\sum_{j=1}^{N_{H}} \mathcal{P}_{N_{j}}}, i=1,2, \ldots, \mathbf{N}_{\mathbf{H}}
$$

The selection of a heuristic is determined by the RWS method. The pseudo-code of the RWS method is presented in Algorithm 1.

```
Algorithm 1 Roulette wheel selection method.
    : heu \(\leftarrow 0 ;\)
    : \(t \leftarrow \operatorname{rand}(0,1)\);
    while \(\left(\varepsilon_{\text {heu }} \leqslant t\right)\) do
        heu \(\leftarrow\) heu +1
    end while
    return \(\mathcal{H}_{\text {heu }}\)
```


### 4.2. Lower level of the hyper-heuristic

The lower level of the hyper-heuristic is a set of low-level, can be standard or problem specific, heuristics that directly operates on the search space of the solution of the problem under consideration. Table 1 presents six low-level heuristics.

Table 1
Low-level heuristics.
# 4.2.1. Crossover heuristics 

Three versions of uniform crossover operator (UXO) [46] are developed to generate an offspring. In the first version, called Crossover1 (LH_1), the global best solution and the current solution are used as two parents and a child solution is generated by applying UXO. In UXO, for each location a random number is generated uniformly in the interval $[0,1]$. If the number is smaller than the predefined value $\mathbf{C}_{\mathbf{p}}$, then the corresponding object from the best solution is added to the child solution; otherwise, the corresponding object from the current solution is added.

In the second version of UXO, called Crossover2 (LH_2), the current solution and a solution different from the current solution is chosen using binary tournament selection (BTS) method and subsequently, as in Crossover1, a new child solution is generated. In the third version of UXO, Crossover3 (LH_3), two parents are selected randomly using BTS method and subsequently, similar to Crossover1, a new child is generated. Each UXO version has an advantage and also helps to maintain diversification in the solution population. Crossover1 and Crossover2 have both exploration and exploitation features, whereas Crossover3 has only exploration ability.

### 4.2.2. Construction heuristic (LH_4)

The purpose of the construction heuristic is to maintain diversity in the population. It performs exploration. At each iteration, an object, $i \in \mathcal{I}$, is added to partial solution, say $\mathcal{S}_{p}$, with the probability 0.50 . Subsequently, the solution is passed through the repair operator (Section 5.3) to make it feasible if not and thereafter through the improvement operator (Section 5.4) for the possible improvement. The pseudo-code of the Construction heuristic is presented in Algorithm 2 .

```
Algorithm 2 Construction heuristic (LH_4).
    \(\mathcal{S}_{p} \leftarrow \phi\);
    for each object \(i \in \mathcal{I}\) in some random order do
        \(r_{1} \leftarrow \operatorname{rand}(0,1)\);
        if \(\left(r_{1} \leqslant 0.50\right)\) then
            \(\mathcal{S}_{p} \leftarrow \mathcal{S}_{p} \cup\{i\}\);
        end if
    end for
    return \(\mathcal{S}_{p}\);
```


### 4.2.3. Guided mutation (LH_5)

In any heuristic, it is always good to take advantages of problem domain knowledge to improve their performance. The proposed guided mutation (GM) heuristic uses the cost and the cardinality of conflict set of objects to give more weight to an object whose conflict size is smaller. For each object $i \in \mathcal{I}, \mathbb{W}_{i}$ and $\left|\mathbb{W}_{i}\right|$ are the conflict set and the conflict count (number of objects conflicting with object $i$ ), respectively. An empty set indicates that the particular object has no conflicting objects. The pseudo-code of determining the conflict set of objects is presented in Algorithm 3.

```
Algorithm 3 Determination of the conflict set of each object \(i \in \mathcal{I}\).
    for (Each object \(i \in \mathcal{I}\) ) do
        \(\mathbb{W}_{i} \leftarrow \phi\);
        for \((j=1\) to \(\mathbf{M})\) do
            if \(\left(\left|\{i\} \cap \mathcal{T}_{j}\right|>0\right)\) then
                \(\mathbb{W}_{i} \leftarrow\left\{\mathbb{W}_{i} \cup \mathcal{T}_{j}\right\} \backslash\{i\} ;\)
            end if
        end for
    end for
```

For initialization of the probability vector, an UMD model is used to estimate the distribution of the candidate solutions in the solution space of the problem. A ratio, say $v_{i}$, of cost, say $c_{i}$, and $\left|\mathbb{W}_{i}\right|$ of an object $i$ is added to increase the probability. A probability vector, say $\mathcal{P}_{\text {Mutation }}=\left\{p_{1}, p_{2}, \ldots, p_{|\mathcal{I}|}\right\} \in[0,1]^{[2]}$, is initialized where $p_{i}$ is the probability of the $i^{\text {th }}$ object

in set $\mathcal{I}$ and $|\mathcal{I}|$ is the cardinality of set $\mathcal{I}$. The pseudo-code of the initialization of the probability vector using the UMD model is given in Algorithm 4.

```
Algorithm 4 Probability vector initialization.
    Compute \(v_{i} \leftarrow \frac{\sum_{i}\left[M_{i}\right]}{\sum_{i} v_{i}} \forall i \in \mathcal{I}\);
    Compute \(y_{i} \leftarrow\) number of initial solutions containing object \(\mathrm{i}, \forall \mathrm{i} \in \mathcal{I}\);
    Compute \(p_{i} \leftarrow \frac{\left(y_{i}+y_{i}\right)}{\left(\mathbf{N}_{\mathbf{p}}+y_{i}\right)}, \forall i \in \mathcal{I}\);
```

Further, the population-based incremental learning (PBIL) model [4] is used to update the probability vector. At each generation $g$, a parent set, say Parent $(g)$, is formed by selecting the best $\frac{N_{p}}{}$ candidate solutions from the current population $\operatorname{Pop}(g)$. Variable $\zeta$ is the learning rate, which changes dynamically with the generation. As $\zeta$ controls the contributions of location and global information and helps to maintain a balance between exploitation and exploration. The pseudo-code of the probability update vector using the PBIL model is given in Algorithm 5.

```
Algorithm 5 Probability vector update.
    Compute \(z_{i} \leftarrow\) number of solutions in Parent \((g)\) containing object \(\mathrm{i}, \forall i \in \mathcal{I}\);
    Compute \(p_{i} \leftarrow(1-\zeta) \times p_{i}+\zeta \times \frac{\zeta}{\sum_{j}} \forall i \in \mathcal{I}\);
```

After the probability vector $\mathcal{P}_{\text {Mutation }}$ is updated, the GM operator is applied to generate a new solution. Set $\mathcal{S}_{p}$, initially empty, is a partial solution in which objects are added either by sampling the probability vector $\mathcal{P}_{\text {Mutation }}$ or directly copying from the global best solution, say $\mathcal{B}_{s}$. Variable $\beta \in(0,1]$ is a control parameter that controls the contribution from probability vector $\mathcal{P}_{\text {Mutation }}$ and the global best solution $\mathcal{B}_{s}$. The large the value of $\beta$, the greater is the number of objects included by sampling the probability vector $\mathcal{P}_{\text {Mutation }}$, whereas the smaller the value of $\beta$, the greater is the number of objects copied from $\mathcal{B}_{s}$. The pseudo-code of the GM operator is presented in Algorithm 6.

```
Algorithm 6 Guided mutation.
    \(\mathcal{S}_{p} \leftarrow \phi\);
    for each object \(i \in \mathcal{I}\) in some random order do
        \(r_{1} \leftarrow \operatorname{rand}(0,-1)\);
        if \(\left(r_{1}<\beta\right)\) then
            \(r_{2} \leftarrow \operatorname{rand}(0,-1)\);
            if \(\left(r_{2}<p_{i}\right)\) then
                \(\mathcal{S}_{p} \leftarrow \mathcal{S}_{p} \cup\{i\}\);
            end if
        else
            if \(\left(i \in \mathcal{B}_{s}\right)\) then
                \(\mathcal{S}_{p} \leftarrow \mathcal{S}_{p} \cup\{i\}\);
            end if
        end if
    end for
    return \(\mathcal{S}_{p}\);
```


# 4.2.4. One_one swap heuristic (LH_6) 

One_one swap heuristic is a modified version of the 1-1 exchange local search presented in [11]. It also operates on the first improvement strategy. In each iteration, it swaps one object from solution $\mathcal{S}_{p}$ with an object not in the solution $\left(\mathcal{I}^{*}=\mathcal{I} \backslash \mathcal{S}_{p}\right)$ if it improves the solution. A function, say Find $_{1,1}\left(\mathcal{S}_{p}\right)$, identifies an object, say $j$, that does not violate the feasibility constraint. Swap $_{1,1}\left(\mathcal{S}_{p}, i, j\right)$ is a function that replaces object $i$ with objects $j$, i.e., $\mathcal{S}_{p}^{*}=\left(\mathcal{S}_{p} \cup\{j\}\right) \backslash\{i\}$. Fitness() is a function that calculates the sum of the weights of the objects in solution $\mathcal{S}_{p}^{*}$. If the new solution $\mathcal{S}_{p}^{*}$ is better than $\mathcal{S}_{p}$, then the solution is updated; otherwise, it moves to the next object in $\mathcal{S}_{p}$. This process continues until all objects in solution $\mathcal{S}_{p}$ are attempted. The 1-1 exchange local search is applied at most 4 successful exchanges, whereas the One_one swap exchanges objects until all objects in set $\mathcal{S}_{p}$ are attempted. The pseudo-code of the One_one swap heuristic (LH_6) is presented in Algorithm 7.

### 4.2.5. One_two swap heuristic (LH_6)

One_two swap heuristic is a modified version of the 1-2 exchange local search presented in [11]. Similar to One_one swap heuristic, function Find $_{1,2}\left(\mathcal{I}^{*}\right)$ identifies two objects, say $i$ and $j$, in set $\mathcal{I}^{*}$ that are not in solution $\mathcal{S}_{p}$ and do not violate

# Algorithm 7 One_one swap heuristic. 

```
    \mathcal{F} \leftarrow \operatorname{Fitness}\left(\mathcal{S}_{p}\right)\;
    \(\mathcal{I}^{*} \leftarrow \mathcal{I} \backslash \mathcal{S}_{p}\);
    \(\mathcal{C}_{s} \leftarrow\left|\mathcal{S}_{p}\right|\);
    \(i \leftarrow 1\);
    while \(\left\{i \leqslant \mathcal{C}_{s}\right\}\) do
        \(j \leftarrow \operatorname{Find}_{1,1}\left(\mathcal{I}^{*}\right)\);
        \(\mathcal{S}_{p}^{*} \leftarrow \operatorname{Swap}_{1,1}\left(\mathcal{S}_{p_{1}}, j\right)\);
        \(\mathcal{F}^{*} \leftarrow \operatorname{Fitness}\left(\mathcal{S}_{p}^{*}\right)\);
        if \(\left(\mathcal{F}^{*}>\mathcal{F}\right)\) then
            \(\mathcal{S}_{p} \leftarrow \mathcal{S}_{p}^{*} ;\)
            \(\mathcal{F} \leftarrow \mathcal{F}^{i} ;\)
            \(i \leftarrow 1\);
        else
            \(i \leftarrow i+1\);
        end if
    end while
```

the feasibility constraint. Function $\operatorname{Swap}_{1,2}\left(\mathcal{S}_{p}, \mathcal{S}_{p_{1}}, j, k\right)$ replaces object $\mathcal{S}_{p_{1}}$ with objects $j$ and $k$, i.e., $\mathcal{S}_{p}^{*}=\left(\mathcal{S}_{p} \cup\{j, k\}\right)$. If the new solution $\mathcal{S}_{p}^{*}$ is better than $\mathcal{S}_{p}$, then the solution is updated; otherwise, it moves to the next object in $\mathcal{S}_{p}$. This process continues until all the objects in $\mathcal{S}_{p}$ are attempted. The 1-2 exchange local search exchanges at most 6 objects, whereas the One_two swap exchanges objects until all objects in set $\mathcal{S}_{p}$ are tried. The pseudo-code of the One_two swap heuristic (LH_6) is presented in Algorithm 8.

```
Algorithm 8 One_two swap heuristic.
    \(\mathcal{F} \leftarrow \operatorname{Fitness}\left(\mathcal{S}_{p}\right)\);
    \(\mathcal{I}^{*} \leftarrow \mathcal{I} \backslash \mathcal{S}_{p}\);
    \(\mathcal{C}_{s} \leftarrow\left|\mathcal{S}_{p}\right|\);
    \(i \leftarrow 1\);
    while \(\left\{i \leqslant \mathcal{C}_{s}\right\}\) do
        \((j, k) \leftarrow \operatorname{Find}_{1,2}\left(\mathcal{I}^{*}\right)\);
        \(\mathcal{S}_{p}^{*} \leftarrow \operatorname{Swap}_{1,2}\left(\mathcal{S}_{p}, \mathcal{S}_{p_{1}}, j, k\right)\);
        \(\mathcal{F}^{*} \leftarrow \operatorname{Fitness}\left(\mathcal{S}_{p}^{*}\right)\);
        if \(\left(\mathcal{F}^{*}>\mathcal{F}\right)\) then
            \(\mathcal{S}_{p} \leftarrow \mathcal{S}_{p}^{*} ;\)
            \(\mathcal{F} \leftarrow \mathcal{F}^{i} ;\)
            \(i \leftarrow 1\);
        else
            \(i \leftarrow i+1\);
        end if
    end while
```


## 5. EA-HH approach for the SPP

The proposed EA-HH approach for the SPP was inspired by the approaches presented in [50] for the maximum clique problem and classification of hyper-heuristics [5]. The pseudo-code and flowchart of the EA-HH approach are presented in Algorithm 9 and Fig. 1, respectively. The main components of the EA-HH approach are presented below.

### 5.1. Solution encoding

Solution encoding is an important part of any meta-heuristic algorithm and it directly affects the computational performance. As the SPP is a class of subset selection problems; therefore, a subset encoding is adopted to represent a solution. Each solution, say $\mathcal{S}_{p}$, is represented directly by the objects it contains, i.e., $\mathcal{S}_{p}=\left\{o_{1}, o_{2}, \ldots, o_{\left|\mathcal{S}_{p}\right|}\right\}$, where $\left|\mathcal{S}_{p}\right|$ is the cardinality of the solution $\mathcal{S}_{p}$.

### 5.2. Initial solution

An initial population is generated randomly. Each object is included randomly in the partial solution, say $\mathcal{S}_{p}$, with equal probability. However, only those objects that satisfy the feasibility criteria are included in $\mathcal{S}_{p}$.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Flowchart of the EA-HH approach.

# Algorithm 9 Evolutionary algorithm based hyper-heuristic. 

1: At generation $\mathrm{g} \leftarrow 0$, an initial population $\operatorname{Pop}(0)$ consisting of $\mathbf{N}_{\mathbf{p}}$ solutions is generated randomly;
2: Apply each low-level heuristic $\mathcal{H}_{i} \in\left\{\mathrm{LH}_{-} 1, \mathrm{LH}_{-} 2 \ldots, \mathrm{LH}_{-} \mathbf{N}_{\mathbf{H}}\right\} \mathbf{N}_{\mathbf{p}}$ number of times to form $\mathbf{N}_{\mathbf{p}} \times \mathbf{N}_{\mathbf{H}}$ fitness matrix $\mathcal{F}_{\text {Credit }}$ (Equation (6);
3: Select the best $\mathbf{N}_{\mathbf{p}}$ number of solutions from $(\operatorname{Pop}(\mathrm{g})+\mathbf{N}_{\mathbf{p}} \times \mathbf{N}_{\mathbf{H}})$ solutions to form population $\operatorname{Pop}(0)$;
4: Initialize the probability vector $\mathcal{P}_{\text {Mutation }}$ (Algorithm 4) and $\mathcal{P}_{\text {Heuristic }}$ (Eq. (8));
5: while $(g<\mathbf{G E N})$ do
6: Select the best $\frac{\mathbf{N}_{\mathbf{p}}}{\mathbf{T}}$ solution from $\operatorname{Pop}(\mathrm{g})$ to form a Parent $(\mathrm{g})$;
7: Update $\zeta(\mathrm{g})$ (Equation (11)), $\beta(\mathrm{g})$ (Eq. (12)), $\mathcal{P}_{\text {Mutation }}$ (Algorithm 5), and $\mathcal{P}_{\text {Heuristic }}$ (Eq. (9));
for ( $i=1$ to $\frac{\mathbf{N}_{\mathbf{p}}}{\mathbf{T}}$ ) do
Select a heuristic $\mathcal{H}_{i} \in\left\{\mathrm{LH}_{-} 1, \mathrm{LH}_{-} 2 \ldots, \mathrm{LH}_{-} \mathbf{N}_{\mathbf{H}}\right\}$ by applying the RWS method on the probability vector $\mathcal{P}_{\text {Heuristic }}$;
10: Apply heuristic $\mathcal{H}_{i}$ to generate a new solution;
11: Update the fitness matrix $\mathcal{F}_{\text {Credit }}$ using First in first out scheme;
12: end for
13: Add $\frac{\mathbf{N}_{\mathbf{p}}}{\mathbf{T}}$ newly generated solutions to Parent $(\mathrm{g})$ to form $\operatorname{Pop}(\mathrm{g}+1)$;
$14: \mathrm{g} \leftarrow \mathrm{g}+1$;
15: end while
16: return Best solution;

### 5.3. Repair operator

The proposed repair operator is a modified version of the Repair Operator presented in [11]. A solution $\Gamma=$ $\left\{\Gamma_{1}, \Gamma_{2}, \ldots, \Gamma_{|\Gamma|}\right\}$ is infeasible if $\sum_{i=1}^{|\Gamma|}\left|\mathcal{H}_{\Gamma_{i}} \cap \Gamma\right|>0$, where $\mathcal{H}_{\Gamma_{i}}$ is the conflict set of an object $\Gamma_{i}$. Each infeasible solution $\Gamma$ generated through heuristic $\mathcal{H}_{i}$ is passed through the repair operator to make it feasible. In the Repair Operator of [11], the conflicting objects are deleted with the help of roulette wheel selection method where the probability of selection of an object is proportional to the ratio of $\left|\aleph_{i}\right|$ to the weight of object $i$, i.e., $c_{i}$, whereas in the modified repair operator conflicting objects are selected in the order in which they are presented in the solution. The pseudo-code of the repair operator is presented in Algorithm 10.

```
Algorithm 10 Repair operator.
\(i \leftarrow 1\);
while \((i \leqslant|\Gamma|)\) do
    \(\delta \leftarrow \aleph_{\Gamma_{i}} \cap \Gamma ;\)
    if \((|\delta|>0)\) then \(\quad \triangleright|\delta|\) will be greater than zero if there is at least one object conflicting with object \(\Gamma_{i}\) in \(\Gamma\)
        \(\Gamma \leftarrow \Gamma-\delta ; \quad \triangleright\) Remove the conflicting objects from \(\Gamma\)
        \(|\Gamma| \leftarrow|\Gamma|\);
        end if
        \(i \leftarrow i+1\);
    end while
```


### 5.4. Improvement operator

Each feasible solution is passed through the improvement operator to further improve the solution quality. The proposed improvement operator is the modified version of the Improvement Operator presented in [11]. Suppose $\delta$ is a set of objects which are not in solution $\Gamma$ and $\mathcal{H}_{\Gamma_{i}}$ is the conflict set of an object $\Gamma_{i}$. In [11], roulette wheel selection method is used to add unpacked object to the solution, where the probability of selection of object $\delta_{i}$ is directly proportional to the ratio of the weight of object $i$ to $\left|\aleph_{i}\right|$, whereas the proposed improvement operator selects an object in the same order as they presented in $\delta$. The improvement operator iteratively attempts to add an unpacked object without violating the feasibility criteria. The pseudo-code of the improvement operator is presented in Algorithm 11.

## 6. Computational results for the SPP

The proposed EA-HH approach was implemented in C language and executed on a Core 2 Duo system with 2 GB RAM under Ubuntu operating system in a 3.0 GHz environment. A gcc 4.4.4-10 compiler with -D3 flag was used to compile the C program. For the fair comparison, the same system is used as that of used in the study in [11]. The EA-HH parameters and their values are listed in Table 2, and all these values were fixed empirically after numerous trials. In this study, two types of random test instances: unit-cost and multi-cost are used to investigate the performance of the proposed approach.

```
Algorithm 11 Improvement operator.
    \(\delta \leftarrow(\mathcal{I}-\Gamma)\);
    for (For each object \(\delta_{i} \in \delta\) ) do
        if \(\left\{\left|\aleph_{\delta_{i}} \cap \Gamma\right|=0\right\}\) then
            \(\Gamma \leftarrow \Gamma \cup \delta_{i}\)
            \(\delta \leftarrow\left(\delta \backslash \aleph_{\delta_{i}}\right) \backslash\{i\} ;\)
        end if
    end for
```

Table 2
Parameters and their values for the EA-HH approach.

The characteristics of the test instances are reported in Tables 7-9. In these three tables, for each instance, the columns with the headings Var, Cnst, Density, Max_One, and Weight show the number of objects $(|\mathcal{I}|)$, number of constraints $(|\mathcal{J}|)$, percentage of non-null elements in the constraint matrix, size of the largest set $\left|\mathcal{T}_{j}\right|$ over all $j \in\{1,2, \ldots, \mathbf{M}\}$, and weight $c_{i} \in\{1-1\}$ or $\{1-20\}$ of object $i \in \mathcal{I}$, respectively. All the test instances can be downloaded from http://www3.inrets. $\mathrm{fr} /$ delorme/Instances-fr.html. In Table 7, the column with the heading Opt lists the optimal values returned by the CPLEX 6.0 solver and in Tables 8 and 9, the column with the heading BKV shows the best known value (BKV) obtained by CPLEX 6.0 solver indicated with an asterisk ("*"). For the GRASP [14], ACO [17], EA/G [11], and the proposed EA-HH approach, the columns with the headings Best, Avrg, and ATET show the best solution, average solution, and average execution time in seconds, respectively. For the EA-HH approach, we report also the number of objects in the best solution and the average number of objects in the average solution.

# 6.1. Effect of dynamic selection of $\beta$ and $\zeta$ parameters 

Parameter tuning is one of the most challenging and difficult tasks in any meta-heuristic approach. Therefore, an intelligent meta-heuristic always attempts to be as independent of parameters as possible.

$$
\begin{aligned}
& \zeta(g)=\zeta_{\min }+\frac{\zeta_{\max }-\zeta_{\min }}{\text { GEN }} \times g \\
& \beta(g)=\beta_{\min }+\frac{\beta_{\max }-\beta_{\min }}{\text { GEN }} \times g
\end{aligned}
$$

The values of $\zeta$ and $\beta$ change dynamically with generation $g$. It also helps to maintain a balance between exploration and exploitation. In the beginning of the generation, the search process performs the exploration whereas at the end of the generation performs exploitation. Dynamic nature of parameter $\zeta$ allows to learn from the global statistical information, whereas at the end of the generation, it allows to learn from the current location in the population. Similarly, a smaller value of $\beta$ forces a contribution from the global best solution, whereas a larger value forces a contribution from the current population. In Eqs. (11)and (12), $g, \zeta_{\min }$ and $\zeta_{\max }$, and GEN are the current generation, minimum and maximum values of $\zeta$, and the maximum number of generations, respectively.

In Figs. 2 and 3, instances pb500rnd09 and pb1000rnd07 are used to show the influence of the dynamic selection of parameters $\zeta$ and $\beta$ on the solution quality. These figures show the convergence speed of each combination of parameter values. The values of $\zeta, \beta \in\{0.40,0.60,0.80,0.99\}$, and other combinations, where the values change dynamically according to Eqs. (11) and (12) are plotted. In Fig. 2(a) to (d), and Fig. 3(a) to (d) the values of $\beta$ are $0.40,0.60,0.80$, and 0.99 , respectively and for each value of $\beta$ four different values of $\zeta \in\{0.01,0.40,0.60,0.80,0.99\}$ are passed. The figures show that the dynamic selection of parameters $\beta$ and $\zeta$ yields a better convergence speed and these values reach the BKV faster than the fixed values.

One of the reasons of success is that the dynamic selection of parameters allows the search process to explore different areas of search space at the beginning of the generation, and then end of the generation it allows to exploit the search area. On the other side, fixed parameter value restricts the search process to explore in the fixed direction. In these figures, we can see that plots with larger values of parameters unable to converge to the BKV, and the reason is that the search process started exploiting the search area from the beginning of generation and got stuck on local optima. Similarly, When one

![img-1.jpeg](img-1.jpeg)

Fig. 2. Convergence behavior of the EA-HH approach with different values of $\beta$ and $\zeta$ on instancepb500rnd09.
parameter has smaller value and other has a larger value, then the search process got stuck on local optima. Furthermore, if the parameters values are close to each other, then the search process is able to perform both exploration and exploitation. Based on experimental results and analysis it can be concluded that a proper trade-off among parameters values can take the search process towards global optimum in reasonable amount of computational time.

# 6.2. Behavior of the EA-HH approach in the search space of the heuristics 

In this section, we investigate the behavior of the components of the EA-HH approach. In Fig. 4(a), the portions of the probability shared by low-level heuristics LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6 in each generation for instance pb1000rnd07 are plotted. In the figure, the Generation axis represents generations from 1 to 100 and the Probability axis represents the percentage share of the probability by each heuristic in each generation. The probability value of each heuristic is directly proportional to the performance of the particular heuristic in any generation. The probability values help in the selection of a low-level heuristic in the next generation. In the figure, it can be observed that the probability share changes with the generation and this directly affects the heuristic selection rule. The larger its probability value, the greater is the chance of the heuristic being selected in the next generation. The average probability shares of heuristics LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6 are $0.160,0.162,0.160,0.184,0.174$, and 0.159 , respectively.

Fig. 4(b) shows the distribution of heuristics in each generation. In the figure, the Generation axis represents the generations from 1 to 100 and the Heuristic axis represents the percentage share of frequencies of each heuristic in each generation. The average number of times heuristics LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6 were selected was 242, 240, 255, 265, 281, and 217, respectively. The average number of frequencies of the heuristics shows that the search process is not dependent on any one of the heuristics and each heuristic contributed to the search process.

From Fig. 4(a) and (b), it can be observed that the $\%$ frequency of each heuristic in each generation is directly affected by the $\%$ probability share of each heuristic in the corresponding generation. However, the average probability of the heuristics does not have direct influence on the corresponding average frequency of heuristic. The reason of this is randomness in the RWS method.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Convergence behavior of the EA-HH approach with different values of $\beta$ and $\zeta$ on instance pb1000rnd07.
![img-3.jpeg](img-3.jpeg)
(a) Changes in probability of heuristics with generations (b) Changes in frequency of heuristics with generations

Fig. 4. Changes in probability and heuristic frequency with generation on instance pb1000rnd07.

# 6.3. Analysis of exploration and exploitation nature of the heuristics 

Exploration and exploitation are the important features of any heuristic. Exploratory heuristic searches new space of the search space, whereas exploitative heuristic searches in the neighborhood of the current location of the search space. Exploration tries to take the search process towards the new space, whereas exploitation exploits the current location of the search space. A delicate balance between exploration and exploitation is an important factor of any heuristic to get a satisfactory solution in a reasonable amount of computational time. On the other hand, an improper balance may take the search process towards a local optimum. Furthermore, more exploration may need more number of iterations to reach the global optimum, whereas more exploitation, may be stuck into local optimum. In the EA-HH, Crossover1, Crossover2, Crossover3, and Construction are exploratory heuristics, whereas One_one and One_two are exploitative heuristics. Crossover1 heuristic explores a new space in the neighbor of the current global best solution, Crossover2 heuristic explores a new space

![img-4.jpeg](img-4.jpeg)

Fig. 5. Population evolution of the EA-HH approach with generations on instance pb1000rnd07.
in the neighbor of one of the best $\frac{N_{p}}{T}$ solutions, whereas Crossover3 heuristic explores a new space in the neighbor of one of the worst $\frac{N_{p}}{T}$ solutions in the population. The advantage of these heuristics is that they explore diverse new space simultaneously. Construction heuristic explores the search space randomly and it helps to maintain diversity in the solution population. In the case of Guided mutation heuristic, it doses both exploration and exploitation together. It explores the search space using the global statistical information which is stored in the form of probability, on the other hand, it exploits the search space in the neighbor of the current global best solution.

# 6.4. Population evolution with generations 

Fig. 5 presents the evolution of the solution population with the generations. In the figure, all the generated solutions are plotted. It can be observed that the solution population evolves with the generations and converges toward the BKV. As in the EA-HH approach, $\operatorname{Pop}(g+1)$ is composed of the best $\frac{N_{p}}{T}$ solutions from $\operatorname{Pop}(g)$ and $\frac{N_{p}}{T}$ new solutions. In the figure, the solutions generated in each generation are represented by black dots. Each blue and red dot represents the best solution and the best $\frac{\mathrm{N}_{\mathrm{p}}}{\mathrm{T}} \mathrm{th}$ solution, respectively, in the corresponding generation. In the figure, it can be observed that the search procedure maintains diversification in the solution population throughout the generations, and this helps in avoiding a situation where the search becomes trapped in local optima as the other heuristics are trapped in a local optimum. It can also be observed that the best $\frac{N_{p}}{T}$ solutions move toward the global best solution and this helps in exploiting the neighborhood space of the global best solution, as the low-level heuristics use the best $\frac{\mathrm{N}_{\mathrm{p}}}{\mathrm{T}}$ and the worst $\frac{\mathrm{N}_{\mathrm{p}}}{\mathrm{T}}$ solutions to generate a new solution. The reason for considering the worst $\frac{\mathrm{N}_{\mathrm{p}}}{\mathrm{T}}$ solutions is the nature of the problem: the SPP problem is a subset selection problem and the number of objects in solution is very small compared to the size of the problem. Furthermore, it is also quite evident that the set of best solutions will have many common objects and will force the operator to generate a solution similar to the best solution. In resultant, it will take the search procedure toward a local optimum.

### 6.5. Comparison of the convergence speed and success rate

In Fig. 6, we compare the convergence speed and success rate to reaching the BKV of the EA-HH approach, with heuristics LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6 on instances pb1000rnd07, pb500rnd15, and pb500rnd09. In these figures, the convergence behavior of the best run and the average of runs are presented. In the figure, the vertical axis represents the fitness returned by each heuristic and the horizontal axis represents generations. In Fig. 6(a), (c) and (e) the best solution of each generation returned by each approach are plotted, whereas in Fig. 6(b), (d) and (f) the average of 16 runs are plotted. The purpose of plotting the best run and the average of runs is to show that, even for a particular run other approaches can outperform the EA-HH approach in terms of the average performance, the EA-HH approach is always superior. From the figures, it is evident that the convergence speed of the EA-HH approach is higher and it reaches the BKV, whereas other heuristics are slower and they are unable to reach the BKV.

In Fig. 6(a) and (b), it is also evident that the convergence speed of the EA-HH approach is higher than that of the other approaches. Similarly, Fig. 6(c)-(f) shows that the convergence speed of the EA-HH approach is higher than that of the other approaches. In Figs. 6(f), heuristics LH_1, LH_2, LH_3 are not plotted, because their convergence speed are far inferior than EE-HH, LH_4 and LH_5. If we compare the success rate in terms of reaching the BKV, EA-HH approach has higher than that of the other approaches.

![img-10.jpeg](img-10.jpeg)
(a) Convergence speed of the best run on instance pb1000rnd07
![img-6.jpeg](img-6.jpeg)
(c) Convergence speed of the best run on instance pb500rnd15
![img-7.jpeg](img-7.jpeg)
(b) Convergence speed of the average of runs on instance pb1000rnd07
![img-8.jpeg](img-8.jpeg)
(d) Convergence speed of the average of runs on instance pb500rnd15
![img-9.jpeg](img-9.jpeg)
(e) Convergence speed of the best run on instance pb500rnd09
![img-10.jpeg](img-10.jpeg)
(f) Convergence speed of the average runs on instance pb500rnd09

Fig. 6. Convergence speed of EA-HH, LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6 approaches on instances pb1000rnd07, pb500rnd15, and pb500rnd09.

# 6.6. Performance comparison of the individual heuristic with the EA-HH approach 

This section presents the performance comparison of heuristics LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6 when they are applied individually. Each individual heuristic has its own advantage and limitation: some of them have exploration ability and others have exploitation ability. Exploration may take the search process away from the global optima, whereas exploitation may takes the search process toward the local optima. Therefore, it is necessary to achieve a balanced tradeoff between exploration and exploitation in the search process to get a satisfactory solution in a reasonable amount of computational time. Tables 4-6 present the results of individual heuristics; the results show that each individual heuristic underperformed because of skewed nature of either exploration or exploitation, whereas the EA-HH approach utilized the exploitative and exploratory features of the individual heuristic to reach the best-known solutions.

Table 3
Wilcoxon-signed-rank test for the EA-HH with the other heuristics for the SPP.
Tables 4-6 present the standard deviation (SD), average solution (Avrg), and average total execution time (ATET) in seconds for heuristics LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6 under the same conditions as those adopted for the EA-HH approach. The percentage (\%) difference between the EA-HH approach and each individual heuristic is reported in the last six columns. The results with positive values indicate the EA-HH approach has better than that of a particular heuristic, whereas with the negative values indicate that the EA-HH has inferior performance. The results with zero values indicate that the performances of both the approaches are the same. In Tables 4-6, it can be observed that the EA-HH approach outperformed all the other heuristics under the same conditions. From the results, it can be concluded that the individual heuristics could not perform well owing to their limitation, whereas the EA-HH approach could determine a good solution owing to the better utilization of the individual heuristics with each generation. In other words, it can be stated that an appropriate balance in the selection of the heuristic in each generation increases the search ability. From these tables, it is clear that heuristics LH_4 and LH_5 outperformed the other heuristics in terms of the average and standard deviation. The two-tailed Wilcoxon signed-ranked test with the significance criterion $1 \%$ ( $p-$ value $\leqslant 0.01$ ) is used to investigate the significance level with the EA-HH approach. An online calculator ${ }^{1}$ was used to perform this test. Table 3, presents the results of the Wilcoxon-signed-ranked test and from the outcomes, it is evident that the EA-HH approach is significant than the heuristics when they are used individually. The mean rank of heuristics LH_1, LH_2, LH_3, LH_4, LH_5 and LH_6 are 2.70, $2.55,2.34,5.69,5.53$ and 3.56 , respectively. In the mean rank values, smaller value indicates smaller rank and higher value indicates higher rank. From the mean rank value, it is clear that LH_4 has the best performance among the heuristics. If we compare the robustness of the heuristics, the standard deviation shows that these heuristics have no robustness. In terms of computational time, the mean rank test of heuristics LH_1, LH_2, LH_3, LH_4, LH_5 and LH_6 are 4.27, 4.20, 3.97, 1.87, $4.02,3.87$, respectively. Whereas, in terms of standard variation, the mean rank test of the heuristics LH_1, LH_2, LH_3, LH_4, LH_5 and LH_6 are $4.25,4.14,4.03,2.22,3.42,4.45$, respectively. In the case of computation time and standard deviation, small mean rank value and large mean rank value indicate the higher rank and the lower rank, respectively.

# 6.7. Comparison analysis of computational results of the GRASP, ACO, EA/g and EA-HH 

This section presents a comparative analysis of the combinational results of the exact approach, GRASP [14], ACO [17], EA/G [11], and the EA-HH approach that are presented in Tables 7-9. The results in these tables show the superiority of the EA-HH approach over GRASP, ACO, and EA/G in terms of the computational results and time. Table 7 presents the computational results of the instances with 100 and 200 objects. The EA-HH approach achieved the optimal values on all 30 instances in terms of the best solution and on 28 instances in terms of the average solution. As compared with GRASP, the EA-HH approach is better on 13 instances, poorer on 2 instances, and the same on the remaining 15 instances in terms of the best solution. In terms of the average solution, the EA-HH approach is better on 10 instances, poorer on 1 instance, and the same on 19 instances. In terms of computational time, the EA-HH approach achieved the optimal as well as a better average solution in computationally less time than GRASP approach. In comparison with ACO, the EA-HH approach is better on 2 instances and the same on 28 instances in terms of the optimal solution. In terms of the average solution, the EA-HH approach is better on 17 instances, poorer on 1 instance, and the same on 12 instances. In terms of computational time, the EA-HH approach is always faster than ACO.

EA/G is the state-of-the-art approach for the SPP and the EA-HH approach outperformed in terms of both the average solution and the computational time. Out of 30 instances, the EA-HH approach is better on 10 instances, poorer on 1 instance, and the same on 19 instances in terms of the average solution. Here, notably, the EA-HH approach achieved the optimal solution in all the runs on all the 30 instances, whereas the EA/G could achieve the optimal solution on 19 instances only. Therefore, the computational results show that the EA-HH approach outperformed the EA/G approach.

Table 8 presents the computational results on the instances with 500 and 1000 objects. The exact approach failed to determine the optimal solution within the specified computational time on most of the instances, and therefore, the solution is the BKV and is indicated by "*". Out of 26 instances, the exact approach determined the optimal solution on 9 instances and on the remaining 17 instances, it achieved solution is the BKV. The EA-HH approach achieved the optimal value on eight

[^0]
[^0]:    ${ }^{1}$ https://mathcracker.com/wilcoxon-signed-ranks.php.

Table 4
Comparison on instances with up to 200 variables.
${ }^{(32)}$ Avrg ${ }_{(4) 32)}$ : SD, Avrg, and ATET are standard deviation, average solution, and average total execution time, respectively

Table 5
Comparison on instances with up to 500 and 1000 variables.
${ }^{(32)}$ Avrg ${ }_{(a) 37)}$ : SD, Avrg, and ATET are standard deviation, average solution, and average total execution time, respectively

Table 6
Comparison on instances with up to 2000 variables.

${ }^{(30)}$ Avrg $_{0}(\mathrm{OT})$. SD, Avrg, and ATET are standard deviation, average solution and average total execution time, respectively

Table 7
Comparison of the EA-HH approach with GRASP [14], ACO [17], and EA/G [11] on instances with up to 200 variables.
(a) indicates number of objects in the best solution (b) indicates average number of objects over 16 runs

Table 8
Comparison of the EA-HH approach with GRASP [14], ACO [17], and EA/G [11] on instances with 500 and 1000 variables.
(a) indicates number of objects in the best solution (b) indicates average number of objects over 16 runs

Table 9
Comparison of the EA-HH approach with GRASP [14], and EA/G [11] on instances with 2000 variables.
(a) indicates number of objects in the best solution (b) indicates average number of objects over 16 runs

out of nine instances, whereas in terms of the BKV, out of 17 instances, the EA-HH approach achieved the same results as the BKV on 13 instances, poorer than the BKV on 1 instance, and better than the BKV on 3 instances. As compared with GRASP, the EA-HH approach is better on 9 instances and the same on 17 instances in terms of the best solution. In terms of the average solution, the EA-HH approach is better on 21 instances, poorer on 1 instance, and the same on 4 instances. As compared with ACO approach, the EA-HH approach outperformed this approach. Out of 26 instances, the EAHH approach is superior on 5 instances and inferior on 2 instances in terms of the best solution. In terms of the average solution, the EA-HH approach is superior on 25 instances and inferior on 1 instance. In terms of the computational time, the EA-HH approach achieved a better solution in computationally less time than ACO approach. The EA-HH approach also outperformed the EA/G, which outperformed GRASP and ACO approaches. In terms of the best solution, the EA-HH approach determined the same solution on all the instances, whereas in terms of the average solution, the EA-HH approach is better on 21 instances, poorer on 4 instances, and the same on 1 instance. At the beginning of the computational section, it was mentioned that the EA-HH approach was executed on the same system as that used for the EA/G approach. Therefore, from Table 8, it can be observed that wherever the EA-HH approach has the same solution fitness, it took less computational time and on some instances, it achieved a better solution in computationally less time than the EA/G approach. Out of 26 instances, on 15 instances, the EA-HH approach returned a better solution than the EA/G approach. On 11 instances, the EA-HH approach achieved a better solution fitness at the cost of extra computational time. As already mentioned, both the EA-HH and EA/G approaches generated the same number of solutions and also the same number of fitness evolutions. However, EA/G approach could not achieve a better solution than the EA-HH approach. The reason is that EA/G approach converged to the local optima and could not explore the other areas of the solution space, whereas the EA-HH approach could explore many areas of the solution space. It is evident in Section 6.4 that the solution population always maintains diversity.

Table 9 presents the computational results for the instances with 2000 objects. For the large instances, the exact approach and GRASP could achieve the optimal solution on only 2 out of 8 instances. The EA-HH approach found the new BKV for the instances pb2000rnd0700 and pb2000rnd0800. GRASP approach reported only the best solution out of 16 runs and it could achieve BKV on 5 instances. As compared with GRASP, the EA-HH approach is better on 2 instances, poorer on 1 instance, and the same on the remaining 4 instances in terms of the best solution. As compared with EA/G, the EA-HH approach is better on 2 instances, poorer on 2 instances, and the same on the remaining 4 instances in terms of the best solution. In terms of the average solution, the EA-HH approach is better on 4 instances, poorer on 1 instance, and the same on the remaining 3 instances. Notably, the EA-HH approach achieved a better solution at the cost of extra computational time on 3 instances. This shows that the EA-HH approach has the ability to explore a different area of the solution space of the problem under consideration.

The superiority of the EA-HH approach over other approaches such as GRASP, ACO, and EA/G can be attributed to the utilization of the evolutionary algorithm in the hyper-heuristic framework which allows to take advantage of low-level heuristics to explore/exploit the solution space of the problem under consideration. However, the computational results show that on the some instances the EA-HH approach failed to achieve the same solution achieved by the other approaches and this asserts the "no free lunch theory" [48]. Another observation that can be made concerning computational time is the number of objects in the solution which is directly affected by the density of objects. Number of object is inversely proportional to the density. As a result of the higher density, the conflict size of objects becomes higher, whereas as the result of low density, the conflict size becomes smaller. And also, the number of objects in the solution directly affects the computational time. As the number of objects increases, the computational time also increases. The reason for the increase in the computational time is that the search procedure spends more time in eliminating the conflicting objects from the infeasible solution. For example, the characteristics of instances pb1000rnd05 and pb1000rnd07 are (Var $=1000$, Cnst $=1000$, Density $=2.60 \%$ ) and (Var $=1000$, Cnst $=1000$, Density $=0.58 \%$ ), respectively. The analysis of the computational results of these instances reveals that the number of objects is 14 and 163, respectively, and the computational time (ATET) is 12.50 s and 49.83 s , respectively. Therefore, it is evident that the computational time for the instances with higher density is less than that of an instance with lower density. Similarly, the computational time of the groups of instances reveals that all the groups show a similar trend of change in computational time.

# 6.8. The wilcoxon signed-rank test 

The two-tailed Wilcoxon signed-ranked test with the significance criterion of $1 \%$ ( $p$-value $\leqslant 0.01$ ). Table 10 presents the results of the Wilcoxon-signed-ranked test. The results in the table show that the EA-HH approach is significant compared to the other approaches. The Friedman mean ranks of the EA-HH, EA/G, GRASP, and ACO approaches are 3.3, 2.5, 2.3 and 1.8, respectively. A larger value indicates better performance. The mean ranks show that the EA-HH exhibits better performance than the other approaches.

### 6.9. Box plot analysis

This section examines the dispersion of fitness values from the median for the EA-HH, LH_1, LH_2, LH_3, LH_4, LH_5 and LH_6 approaches. The purpose of this analysis is to observe the capabilities of the approaches in terms of searching for a good solution in the solution space. The boxplots are used to show the robustness of the proposed approach. In

Table 10
Wilcoxon-signed-rank test of the EA-HH approach with the other approaches for the SPP.

![img-11.jpeg](img-11.jpeg)

Fig. 7. Boxplots of the approaches EA-HH, LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6.

Fig. 7(a) to (d) and Fig. 8(a) to (d), the boxplots of the fitness values returned by the EA-HH, LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6 approaches are shown. For the sake of a better representation, the fitness values are scaled between 0 and 1. In the figures, the "Fitness" axis represents the scaled fitness value and the "Instance" axis represents instances. The analysis is focused on the instances for which the standard deviation of the approaches is not zero. The reason for this is to determine the dispersion of fitness values. In Tables 4-6, it can be observed that the performances of heuristics LH_4 and LH_5 are better than those of LH_1, LH_2, and LH_3. In the boxplots in Fig. 7(a) to (d) and Fig. 8(a) to (d), it can be observed

![img-12.jpeg](img-12.jpeg)

Fig. 8. Boxplots of the approaches EA-HH, LH_1, LH_2, LH_3, LH_4, LH_5, and LH_6.
that, on most of the instances, all the heuristics, except EA-HH, have more dispersion from the median. This shows that the other heuristics determined the best solution among 16 runs randomly and they are not robust.

# 7. Minimum weight dominating set problem 

In this section, we consider the minimum weight dominating set (MWDS) problem which is also an $\mathcal{N} \mathcal{P}$-hard [18]. The purpose of considering the MWDS problem in this paper is to show the scalability and generality of the proposed EA-HH approach. Both the SPP and MWDS problems are subset selection problem but have opposite objectives. The SPP has the maximization objective whereas the MWDS problem has the minimization objective. As mentioned in Section 4.2, the lowlevel heuristics are standard operators and are independent of the nature of the problem. Most of the low-level heuristics do not use the problem domain knowledge in the process of generating a new solution. Therefore, the proposed approach is applied to the MWDS problem to investigate the scalability and generality.

### 7.1. Problem description

Consider a node weighted undirected graph $\mathcal{G}=(\mathcal{V}, \mathcal{E})$, where $\mathcal{V}$ is the set of nodes and $\mathcal{E}$ is the set of edges. Any pair, say $(v, u)$, of nodes $v$ and $u$ is considered as a pair of adjacent nodes or neighbor iff, there exists an edge between them, i.e., $(v, u) \in \mathcal{E}$. A dominating set $\mathcal{D} \subseteq \mathcal{V}$ is a set of nodes such that each node in $\mathcal{V}$ either belongs to subset $\mathcal{D}$ or is adjacent to at least one node in $\mathcal{D}$, i.e., node in $\mathcal{V} \backslash \mathcal{D}$ has at least one adjacent node in $\mathcal{D}$. Any node that belongs to subset $\mathcal{D}$ is called a dominating node or dominator, and a node not in subset $\mathcal{D}$ is called a non-dominating or dominatee node. The objective

of the minimum dominating set problem (MDS) is to find a dominating set with minimum cardinality from all possible dominating sets in $\mathcal{G}$.

In the MWDS problem, a non-negative weight, assigned through a weight function $w: \mathcal{V} \rightarrow \Re^{+}$, is associated with each node in $\mathcal{V}$, and the objective is to find a dominating set whose sum of weights of nodes is minimum among all the possible dominating sets in $\mathcal{G}$. Both the MDS and MWDS problems have been proven to be $\Lambda^{\prime} \mathcal{P}$-hard [18]. The object function of the MWDS can be defined as
$\underset{\mathcal{D} \in \mathcal{D}^{\prime}}{\arg \min } \sum_{\mathcal{D} \in \mathcal{D}^{\prime}} w(\nu)$, where $\mathcal{D}^{\prime}$ is the set of all possible dominating sets in $\mathcal{G}$.

# 7.2. The EA-HH approach for the MWDS problem 

This section presents the EA-HH approach for the MWDS problem under similar condition as of the SPP. The main components of the EA-HH approach for the MWDS problem are as follows:

### 7.2.1. Solution encoding

As both SPP and MWDS problem are subset selection problem, a subset encoding has been used to represent a solution. The same solution encoding is followed as that used for the SPP.

### 7.2.2. Initial solution representation

As both SPP and MWDS are subset selection problem; therefore, the initial population is generated in the same manner as for the SPP.

Each infeasible solution is passed through the repair operator to make the solution feasible and subsequently, the feasible solution is passed through the improvement operator. The same repair and improvement operators are used as those used in [8].

### 7.2.3. Solution generation in generation of the EA-HH approach

In each generation, similar to the SPP, a new solution is generated by applying the hyper-heuristic. Only LH_1, LH_2, LH_3, LH_5 heuristics are used at the lower level of the hyper-heuristic. As heuristic LH_6 is the problem specific and cannot directly be applied for the MWDS problem. All the above mentioned low-level heuristics are applied in the same manner as for the SPP, except the guided mutation. In the guided mutation, the probability initialization method does not use the problem domain knowledge to initialize the probability vector. Each infeasible solution is passed through the repair to make it feasible and then through the improvement operator to improve the solution quality. The repair and improvement operators are explained in the subsequent section.

### 7.2.4. Repair and improvement operators

Similar to the SPP, after the application of low-level heuristic, each solution is passed through the repair operator to make the solution feasible, and the feasible solution is passed through the improvement operator further to improve the solution quality.

The same repair operator is used as used in [8] to make the infeasible solution feasible. Only the infeasible solution is passed through the repair operator. The repair operator attempts to add uncovered nodes one after another. Uncovered nodes are those nodes that are either not dominating nodes or not the neighbor(s) of at least one dominating node. Iteratively, an uncovered node whose ratio between the sum of weights of uncovered nodes and the weight of the node itself is the highest is chosen.

The improvement operator is used to remove the redundant nodes without violating the feasibility criteria. A redundant node, say $v$, is a dominating node whose neighborhood nodes and node itself are covered by at least one dominating node other than node $v$ in the dominating set. Iteratively, a node whose ratio between the weight of node and number of neighborhood nodes among the set of redundant nodes is highest is removed. For a detailed description of the repair and improvement operators, please, refer to Sections 5.5 and 5.6 of [8].

### 7.3. Computational results for the MWDS problem

This section presents the computational results for the MWDS problem. In [8], two types of instances with different weight ranges are used. For Type I instances, weights of nodes in the network are randomly distributed in the closed interval [20,70], whereas for Type II instances, weights are randomly distributed in the closed interval $\left[1, \mathrm{dc}(v)^{2}\right]$, where $\mathrm{dc}(v)^{2}$ is square of the degree of the node $v$. In this study, instances with network sizes $300,500,800$, and 1000 and the number of edges varies from 300 to 20,000 for both Type I and Type II instances are considered. Ten instances were generated for each combination of the number of nodes $(|\mathcal{V}|)$ and the number of edges $(|\mathcal{E}|)$. A total of $420(210 \times 2$ instances are considered for Type I $(21 \times 10)$ and Type II $(21 \times 10))$.

The same system and the same parameters are used as those used in [8] to compile the C code for the MWDS problem. Furthermore, the parametric values for the MWDS in EA-HH are listed in Table 2. We have compared the EA-HH approach for the MWDS problem with Raka-ACO [28], HGA [40], ACO-LS [40], ACO-PP-LS [40], EA/G-IR [8], HMA [32], and MSRLS ${ }_{9}$ [7] for Type I and Type II instances.

Table 11
Results of Raka-ACO [28], HGA [40], ACO-LS [40], ACO-PP-LS [40], EA/G-IR [8], HMA [32], MSRLS ${ }_{n}$ [7] and EA-HH for large Type I instances.
Table 12
Results of Raka-ACO [28], HGA [40], ACO-LS [40], ACO-PP-LS [40], EA/G-IR [8], HMA [32], MSRLS ${ }_{n}$ [7] and EA-HH for large Type II instances.
The average value 2210.63 ${ }^{c}$ indicates that the average of, excluding mean of instances with number of nodes 1000 and the number of edges 15,000 and 20,000, the mean value of the EA-HH is better than the mean value of MSRLS $_{n}$.

Table 13
Wilcoxon-signed-rank test for the EA-HH with the other approaches for the MWDS problem .

In Table 2, it can be observed that all the low-level heuristics are problem independent, except LH_6, and do not use any problem domain knowledge. However, in [7,8,28,32,40], all of them have problem-dependent operators and they used problem domain knowledge to generate a new solution. The advantage of having a generic operator is that it can be applied on any type of problem in the same domain. However, both the SPP and MWDS problem belong to the domain of subset selection problem, but having opposite objectives. But the same low-level heuristics are used for both the SPP and MWDS problem even though the former one has a maximization objective whereas later one has a minimization objective.

Tables 11 and 12 present the computational results of the state-of-the-art approaches Raka-ACO [28], HGA [40], ACO-LS [40], ACO-PP-LS [40], EA/G-IR [8], HMA [32], and MSRLS ${ }_{6}$ [7] and the proposed EA-HH approach for the MWDS problem on Type I and Type II instances. These tables present mean value (Mean), standard deviation (SD) and average total execution time (ATET) for instance groups of ten instances with the same numbers of nodes $(|\mathcal{V}|)$ and edges $(|\mathcal{E}|)$. However, the SD values for Raka-ACO, HMA and MSRLS ${ }_{6}$ approaches were not reported in the original paper. Moreover, HMA and MSRLS ${ }_{6}$ did not report the ATET. Therefore, we did not report the SD and ATET for the respective approaches as well. The reason is that the MSRLS ${ }_{6}$ approach was run until a fixed time limit of 3600 s, which is much larger than that of any other approaches which are reported in these tables.

Out of 42 instance groups, EA-HH is better than HGA on all 42 instance groups. In comparison with ACO-LS, EA-HH is better on 40 instance groups and worse on two instance groups. In comparison with ACO-PP-LS, EA-HH is better on 39 instance groups and worse on 3 instance groups. In comparison with EA/G-IR, EA-HH is better on 30 instance groups and worse on 12 instance groups. EA-HH is better on 28 instance groups than HMA and worse than HMA on 14 instance groups. In comparison with MSRLS $_{6}$, EA-HH is better on 34 instance groups and worse on 4 instance groups. In [28], Javanovic et al. did not report computational results on the instance groups on the network with 300 nodes for both Type I and Type II. Therefore, we compared the performance on the reported instance groups only. On all 28 instance groups, the EAHH outperformed the Raka-ACO approach. The average performance also indicates that the EA-HH approach exhibits better performance than all the other state-of-the-art approaches presented in the tables.

In terms of computational time, from Tables 11 and 12, it is evident that EA-HH has taken less computational time than HGA, ACO-LS, ACO-PP-LS, and EA/G-IR. For HMA and MSRLS ${ }_{6}$, we did not report the computational times because their stopping criteria are different from those of other approaches. However, the EA-HH approach is bit slower than HMA but is computationally more significant than HMA. In the case of MSRLS $_{6}$, the stopping criterion is fixed at 3600 s. Therefore, EA-HH is faster than the MSRLS ${ }_{6}$ approach.

Table 13 presents the Wilcoxon-signed-rank test for the EA-HH approach with Raka-ACO, HGA, ACO-LS, ACO-PP-LS, HMA and MSRLS ${ }_{6}$ for the MWDS problem. Similar to the SPP, a two-tail Wilcoxon-signed-rank test is performed to investigate the significance level of the EA-HH approach with other approaches by setting the significance criterion to $1 \%$ ( $p$-value $\leq 0.01$ ). From Table 13, it can be observed that the EA-HH approach is significantly better than the other approaches.

Similar to the SPP, a mean ranked test is performed over Raka-ACO, HGA, ACO-LS, ACO-PP-LS, HMA, MSRLS ${ }_{6}$, and the EA-HH approaches and their ranks are $7.76,5.55,5.50,5.05,2.19,3.00,5.05,1.88$, respectively. A smaller value indicates better performance. From the mean ranked test, it is evident that the EA-HH outperformed all the other approaches.

# 8. Conclusions 

In this paper, we proposed an evolutionary algorithm based hyper-heuristic (EA-HH) framework for the SPP and MWDS problem. In the EA-HH, at the higher level of hyper-heuristic, an evolutionary algorithm is employed as a search methodology and at the lower level exploratory and exploitative heuristics are used in the heuristics pool. In the evolutionary algorithm, an online-learning mechanism is employed to learn the performance of each heuristic at each generation. The online-learning mechanism was inspired by the UMD algorithm, which at each iteration estimates the performance of each heuristic and stores their performance in the form of a probability vector. Further, this probability vector is used to select a heuristic using the RWS method. Another contribution is the dynamic selection of parameters. Instead of fixing the parameters, the EA-HH allowed making changes in their values with generations. The computational results show the effectiveness of dynamic selection of parametric. The EA-HH was compared with the state-of-the-art approaches for the SPP: GRASP [14], ACO [17], and EA/G [11]. Further, the MWDS problem is used, mainly, to investigate the generality, effectiveness and robust-

ness of the proposed EA-HH approach. In the case of the MWDS problem, [7], [28], [32], [40] are the state-of-the-art-approaches used to compare with the EA-HH approach. This can be evident from the computational results in Tables 7-9 as well as Tables 11 and 12 that the same operators and same high-level search heuristic are used to solve the problems with opposite objectives.

As a future work, we intend to explore the capabilities of other search heuristics such as taboo search, genetic programming, artificial bee colony, and genetic algorithm, etc. at the higher level of hyper-heuristics. Further, we will explore the heuristic selection methodology and rigorously analyses the performance for new problems in different domains such as permutation and grouping problems.

# Conflict of interest 

None

## Acknowledgments

This research work was supported by a grant from the National Research Foundation (NRF) of Korea, funded bythe Korean government (MSIP) (No. 2016R1A2A1A05005306). Authors are also grateful to four anonymous reviewers and the Editor-inChief for their valuable comments and suggestions which has helped in improving the quality of this paper.
