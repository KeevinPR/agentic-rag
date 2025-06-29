# Estimation of Distribution Algorithm with Stochastic Local Search for Uncertain Capacitated Arc Routing Problems 

Juan Wang, Ke Tang, Senior Member, IEEE, Jose A. Lozano, and Xin Yao, Fellow, IEEE


#### Abstract

The Uncertain Capacitated Arc Routing Problem (UCARP) is a challenging problem where the demands of tasks, the costs of edges, and the presence of tasks and edges are uncertain. The objective of this problem is to find a robust optimal solution for a finite set of possible scenarios. In this paper, we propose a novel robust optimization approach, called an Estimation of Distribution Algorithm with Stochastic Local Search (EDASLS), to tackle this problem. The proposed method integrates an estimation of distribution algorithm with a novel two phase stochastic local search procedure to minimize the maximal total cost over a set of different scenarios. The stochastic local search procedure avoids excessive fitness evaluations of unpromising moves in local search. Our experimental results on two sets of benchmark problems (a total of 55 problem instances) showed that the proposed approach outperformed existing state-of-the-art algorithms.


Index Terms-Uncertain Capacitated Arc Routing Problem; Robust Optimization; Estimation of Distribution Algorithm; Local Search.

## I. INTRODUCTION

THE Capacitated Arc Routing Problem (CARP) [1] is a well-known combinatorial optimization problem. A CARP is defined over a directed graph $G=(V, E)$ with vertex set $V$ and edge set $E$. Each edge $e \in E$ has a traversal cost $c(e)$ and a demand $d(e)$. Both $c(e)$ and $d(e)$ are non-negative. The edges with positive demand constitute the task set $T$, i.e., $T=\{e \in$ $E \mid d(e)>0\}$. A fleet of vehicles, each of which is with capacity $Q$ and located in the depot $v_{0}$, are assigned to serve all the tasks. The aim of CARP is to determine a set of routes with minimal total costs and satisfying the following constraints: each route starts and ends at the depot; each task is served exactly once (but can be traveled more than once); the total load of a route, i.e., the total demand of tasks served by a route, cannot exceed the vehicle capacity $Q$.
CARP has been shown to be NP-hard [1]. Hence, exact methods are limited to small-scale instances and the

[^0]mainstream approaches for solving CARP are heuristics and meta-heuristics. In the past few decades, in addition to some exact algorithms [2-4], a number of heuristics and meta-heuristics have been proposed. For instance, augment-merge [1], path-scanning [5], construct-strike [6] and route-first, cluster-second [7] are constructive heuristics that can produce fairly good solutions. More recently, variants of famous meta-heuristic methods, such as Simulated Annealing [8], guided local search [9] and memetic algorithms [10-12], have also been developed for CARP and showed even better performance in comparison to classical constructive heuristics. Moreover, research on CARP is not restricted to new algorithms, but has also been advanced in terms of problem formulations. Quite a few extensions of CARP, such as CARP with multiple depots [8], time windows [13] and alternative objective functions [14], have arisen from practical applications and have all been studied.

So far, most investigations on CARP (or extensions of CARP) are formulated as deterministic problems. However, real-world applications of CARP are usually stochastic. For instance, in urban waste collection, a typical real-world application of CARP, the amount of garbage on a street may change every day. In street salting, the amount of desired salt of a road changes with the road surface temperature [15]. Therefore, the stochastic version of CARP would have more practical value. In [16] and [17], the robustness of a solution to CARP with respect to stochastic demands was considered. In [18], a stochastic version of CARP, namely Stochastic CARP (SCARP) was approached directly and tackled with a memetic algorithm. In SCARP, demands of tasks are assumed to be random variables that follow normal distributions. The objective is to seek a robust solution that minimizes the expected total cost. Since then, SCARP has received some attention. In [19], the authors provided a mathematical analysis of SCARP and proposed a Hybrid Genetic Algorithm (HGA) to solve it. In [20], a bi-objective approach, which is an extension of Non-dominated Sorting Genetic Algorithm (NSGA-II), was proposed to optimize both the total cost and the duration of the longest trip for SCARP. In [21], demands of tasks in SCARP are assumed to follow Poisson distribution and are revealed gradually as the vehicle progresses along the task. SCARP was formulated as a Set Partitioning Problem and a Branch-and-Price algorithm was proposed to solve it.

Although random variables in a robust optimization problem $[22,23]$ are usually assumed to follow specific distributions, this common practice might be inappropriate for CARP. In a real-world CARP, the distributions of the random variables (i.e., the demand on an edge) are usually unknown in advance, but can only be estimated using a number of different scenarios that


[^0]:    J. Wang, K. Tang (Corresponding Author) and X. Yao are with the USTC-Birmingham Joint Research Institute in Intelligent Computation and Its Applications, School of Computer Science and Technology, University of Science and Technology of China, Hefei, Anhui 230027, China (e-mail: jingze@mail.ustc.edu.cn; ketang@ustc.edu.cn).
    J.A. Lozano is with the Intelligent Systems Group, Department of Computer Science and Artificial Intelligence, University of the Basque Country UPV/EHU, Pasco Manuel de Lardizabal, 1, 20018 Donostia, Giugekoa, Spain (email: ja.lozano@ehu.eus).
    X. Yao is also with the Center of Excellence for Research in Computational Intelligence and Applications, School of Computer Science, University of Birmingham, Birmingham B15 2TT, U.K. (email: x.yao@cs.bham.ac.uk). Copyright (c) 2012 IEEE.

are collected in the real world. Hence, solving a CARP with the estimated (and error-prone) distribution of random variables may not be meaningful. Alternatively, a more direct way is to seek a robust solution for a sample of deterministic scenarios. In this way, the underlying distributions of stochastic variables do not need to be known a priori. Based on this consideration, the Uncertain CARP (UCARP) problem is proposed in [24]. Compared with SCARP, UCARP considers variability in more parameters and does not assume predefined distributions for these parameters. Concretely, four random factors are considered in UCARP: demands of tasks, costs of edges, presence of tasks, and presence of edges. The first two indicate that values of costs and demands in UCARP are stochastic. The latter two mean that the task set and edge set are not fixed. These stochastic factors all correspond to uncertainties in practical situations. For instance, in salting route optimization problem [25], the salting demand and traversal cost of a street vary with the road surface temperature. As the temperature increases, some of the streets may not require salting, i.e., the tasks corresponding to these streets will disappear. Likewise, if a road becomes inaccessible due to construction or traffic jams, the corresponding edges will be absent. The primary aim of UCARP is to find a solution that works satisfactorily when the problem parameters change. Such a solution is called a robust solution [26]. It has been shown that UCARP has quite different characteristics from CARP and cannot be well addressed by simply adapting some existing CARP solver [24]. However, to the best of our knowledge, only one approach has been designed for UCARP so far [27].
In this article, a new approach to UCARP, namely Estimation of Distribution Algorithm with Stochastic Local Search procedure (EDASLS), is proposed to seek robust solutions over a set of deterministic CARP instances. The EDASLS is designed based on Edge Histogram Based Sampling Algorithm (EHBSA) [28], a variant of the Estimation of Distribution Algorithm (EDA) and is equipped with a novel Stochastic Local Search (SLS) procedure tailored to manage the stochastic characteristics of UCARP. Since a solution of UCARP can be represented as a permutation of tasks, UCARP is also in nature a permutation optimization problem. Tasks with tight correlation in the graph have a high probability to be adjacent in the final robust solution sequence. EHBSA fits this characteristic well because it generates new offspring by sampling a probabilistic model that learns the adjacency of elements in permutations. Therefore, an intuitive idea is that EHBSA can generate high-quality solutions to UCARP. However, the original EHBSA does not handle uncertainties explicitly and thus is not efficient for UCARP. Inspired by the idea of Memetic Algorithms (MAs), the SLS procedure is developed to address this challenge.
The remainder of this paper is organized as follows: Section II introduces the problem definition of UCARP and the corresponding notations. In Section III, details of EDASLS are presented. Section IV presents the computational experiments on two benchmark sets adapted from the UCARP literature. The results are compared to those obtained by two other state-of-the-art MAs. Finally, conclusions and future work is presented in Section V.

## II. Problem DEFINITION AND NOTATIONS

Let $G(V, E)$ be a complete and undirected graph where $V$ and $E$ represent the sets of vertices and edges, respectively. Associated with each edge $e \in E$ there is a $\operatorname{cost} c(e)>0$ and a demand $d(e) \geq 0$. Both $c(e)$ and $d(e)$ are stochastic variables. The value of $c(e)$ could be infinite, which means that edge $e$ is missing. The edges with positive demands form the task set $T$, i.e., $T=\{\tau \in E \mid d(\tau)>0\}$. Note that tasks in $T$ are not fixed. A task will turn into a non-required edge when its demand changes to 0 . A fleet of vehicles with capacity $Q$ and located at the depot $v_{0} \in V$ is assigned to serve the task set. Similar to CARP, UCARP also involves three constraints: 1) each vehicle starts and ends at the depot; 2) each task is served by one and only one vehicle; 3) the total demand of the tasks served by each vehicle should not exceed the vehicle capacity. The objective of UCARP is to determine a set of vehicle routes that minimize the maximal total cost of the routes over a set of scenarios. That is, the UCARP in this article is a minimax optimization problem.

As mentioned in Section I, in this article, UCARP is approximated by a set of deterministic CARP instances. Concretely, an UCARP instance $\Theta$ is expressed as $\Theta=$ $\left\{I_{1}, I_{2}, \ldots, I_{N}\right\}$. For any $1 \leq j \leq N, I_{j}$ is a CARP instance. All $I_{j} \in \Theta$ are related but different from each other. Intuitively, $I_{j}$ can be regarded as a status of $\Theta$ in a specific scenario. The task sets of all the instances comprise of the union task set UT, i.e., $U T=\bigcup_{j=1}^{N} T_{j}$, where $T_{j}$ is the task set of instance $I_{j}$. Each $\tau \in U T$ is associated with two task IDs which are integers within the range 1 to $2[U T]$. Each ID represents one direction of the task.

The main issue to be addressed in UCARP is that a planned feasible solution might be inappropriate (or infeasible) for some instances because of the stochastic nature of UCARP. Therefore a recourse strategy $\Phi$, which guarantees the solution's feasibility and flexibility, is required. Particularly, $\Phi$ tackles the following three conditions that might occur when a solution is executed on an instance:

1) A travelled edge is missing;
2) An original task turns into a non-required edge;
3) A violation of vehicle capacity comes up.

For the first case, the missing edge is replaced by the shortest path connecting its two endpoints. For the second case, as a task becomes non-required, it is no longer necessary to serve it. The vehicle would ignore the "was-required" task and skip to the next task to continue service. For the last case, when the capacity of a vehicle is exceeded, which is commonly called a route failure in Stochastic Capacitated Vehicle Routing Problem (SCVRP) [29], the node counterpart of SCARP, the recourse strategy amends the routes by returning to the depot to get replenished before serving the next task. Since we are not aware of the distributions of demands on the tasks, it is intractable to determine where a route failure occurs if the actual demand of an edge is revealed only when the vehicle arrives. Hence, an assumption made in [30] for SCVRP is adopted in this work as well, that is, a task's actual demand is known before it is served. Under this assumption, when a task $\tau_{i}$ is served and the remaining capacity of the vehicle is not enough for the next task $\tau_{i+1}$, we consider that a route failure

occurs right after $\tau_{i}$ is served. It is worth mentioning that after replenishment, the vehicle heads directly to serve $\tau_{i+1}$ instead of going back to the vertex where the route failure occurs (which is an endpoint of task $\tau_{i}$ ).

A solution of UCARP can be represented by a set of routes $s=\left(R_{1}, \ldots, R_{m}\right)$ that partition the task set $U T$ into $m$ routes $R_{k}=\left(\tau_{k, 1}, \ldots, \tau_{k, l_{k}}\right)$, where $\tau_{k, t}$ and $l_{k}$ denote the $t$ th task and the number of tasks served in route $R_{k}$, respectively. The contiguous tasks are connected by implicit shortest paths which are not represented in the routes.

Let $\operatorname{head}(\tau)$ and $\operatorname{tail}(\tau)$ represent the two endpoints and $\operatorname{inv}(\tau)$ the reverse direction of task $\tau$, i.e., $\operatorname{head}(\operatorname{inv}(\tau))=$ $\operatorname{tail}(\tau), \operatorname{tail}(\operatorname{inv}(\tau))=\operatorname{head}(\tau)$, and vice versa, $d\left(\tau, l_{j}\right)$ represents the demand of $\tau$ in instance $l_{j}$, UCARP can be stated as follows:
minimize $R(s)$
s.t. : head $\left(\tau_{k, 1}\right)=\operatorname{tail}\left(\tau_{k, l_{k}}\right)=v_{0}, \forall k=1,2, \ldots, m$

$$
\begin{aligned}
& \sum_{k=1}^{m} l_{k}=|U T| \\
& \tau_{k_{1}, i_{1}} \neq \tau_{k_{2}, i_{2}}, \forall\left(k_{1}, i_{1}\right) \neq\left(k_{2}, i_{2}\right) \\
& \tau_{k_{1}, i_{1}} \neq \operatorname{inv}\left(\tau_{k_{2}, i_{2}}\right), \forall\left(k_{1}, i_{1}\right) \neq\left(k_{2}, i_{2}\right) \\
& \sum_{i=1}^{l_{k}} d\left(\tau_{k, i}, l_{j}\right) \leq Q \\
& \forall k=1,2, \ldots, m ; \forall l_{j} \in \Theta \\
& \tau_{k, i} \in U T
\end{aligned}
$$

In constraints (4) and (5), the inequality $\left(k_{1}, i_{1}\right) \neq\left(k_{2}, i_{2}\right)$ means that the two equalities $k_{1}=k_{2}$ and $i_{1}=i_{2}$ do not hold simultaneously. Eq. (1) requires minimizing the maximal total $\operatorname{cost} T C\left(s^{\prime}, l_{j}\right)$ for all $l_{j} \in \Theta$, i.e., $R(s)=\max _{l_{j} \in \Theta} T C\left(s^{\prime}, l_{j}\right)$. In other words, the optimal solution for UCARP is $s^{\prime}=$ $\arg \min _{s \in S}\left\{\max _{l_{j}} T C\left(s^{\prime}, l_{j}\right)\right\}$, where $s^{\prime}=\Phi\left(s, l_{j}\right)$ denotes the modified solution obtained by the recourse strategy $\Phi$ when executing $s$ on instance $l_{j}$ and $T C\left(s^{\prime}, l_{j}\right)$ is the total cost of $s^{\prime}$ on instance $l_{j}$ :

$$
T C\left(s^{\prime}, l_{j}\right)=\sum_{k=1}^{m} C\left(R_{k}\right)
$$

where $C\left(R_{k}\right)$ is the cost of route $R_{k}$ :
$C\left(R_{k}\right)=\sum_{i=1}^{l_{k}}\left(c\left(\tau_{k, i}\right)+\operatorname{dis}\left(\operatorname{tail}\left(\tau_{k, i-1}\right), \operatorname{head}\left(\tau_{k, i}\right)\right)\right)+$ $\operatorname{dis}\left(\operatorname{tail}\left(\tau_{k, l_{k}}\right), v_{0}\right)$
where $\operatorname{dis}(a, b)$ is the cost of the shortest path from vertex $a$ to vertex $b$. tail $\left(\tau_{k, i-1}\right)$ is set to $v_{0}$ when $i=1$.

Constraint (2) indicates the priority that each route starts and ends at the depot $v_{0}$. Constraints (3) to (5) make sure that all the tasks are served exactly once. Constraint (6) means that the total demand of each route should not exceed the capacity $Q$ on any instance. Constraint (7) defines the domain of variables.

## III. An EDA With Stochastic Local Search for UCARP

Most EDAs [31-33] focus on optimization problems based on integer or real domains. The EHBSA was proposed in 2002 for permutation optimization problems [28]. In each generation of EHBSA, an edge histogram matrix is calculated.

Subsequently, new offspring are generated based on the matrix. By learning the adjacency of the vertices in the parent population, EHBSA can produce new individuals in which the adjacent elements would have a stronger correlation.

A UCARP can be transformed to a permutation optimization problem and solved by EHBSA. However, the basic and simple EHBSA does not have particularly significant advantage over other well-established EAs for deterministic problems, not to mention stochastic problems. To enhance the performance of EHBSA, a natural idea is hybridizing it with local search. However, because of the stochastic characteristics, conventional local search is inappropriate when applying to UCARP. In UCARP, an intermediate solution should be evaluated on all the instances, which is computationally costly. Thus, we propose a novel stochastic local search for UCARP and couple it with EHBSA, forming a new approach named EDA with Stochastic Local Search (EDASLS).

The pseudo-code of EDASLS is presented in Fig. 1. Several main ingredients are described in detail in Sections III.A-III.D: chromosome structure and evaluation, edge histogram based sampling method, local search procedure, population structure, initialization and replacement.

## A. Chromosome structure and evaluation

Solving routing problems essentially involves determining a sequence of tasks (edges) or customers (nodes) with route delimiters partitioning the sequence into routes compatible with vehicle capacity. In 1983, Beasley [34] first introduced route-first cluster-second heuristics. This method first produces a giant route, also called chromosome, by temporarily ignoring the vehicle capacity. Then, the giant route is decomposed into feasible routes for vehicles. Subsequent to Beasley's work, a large amount of methods adopting the route-first split-second idea have been proposed for CARP [7, 10, 13, 18, 35, 36] as well as other routing problems [29, 37-41]. More related works can be found in a review [42]. Inspired by these literatures, our chromosome $c$ is a permutation of $|U T|$ tasks (each task is represented by its task ID), without route delimiters, and with implicit shortest paths between consecutive tasks. We adopt this kind of chromosome representation because: (1) EHBSA can be directly applied to this encoding scheme; (2) an optimal solution can be extracted from a chromosome by the split procedure proposed in [7] for the deterministic CARP; (3) since our approach is developed on a set of CARPs, this chromosome is more convenient for evolution than a solution (routes with route delimiters). Without the capacity constraint, we do not need to frequently execute the recourse operator to repair a chromosome.

To evaluate the performance of a chromosome $c$, its fitness needs to be defined. In EDASLS, the fitness of $c$ is defined as the maximum of its optimal (i.e., minimal) costs on all the instances and the lower fitness indicates the better performance:

$$
F(c)=\max _{l_{j} \in \Theta} T C\left(s_{l_{j}}, l_{j}\right)
$$

where $s_{l_{j}}$ is the solution obtained by partitioning chromosome $c$ on instance $l_{j}$ using Ulusoy's splitting procedure [7].

Ulusoy's splitting procedure is an exact method that seeks the optimal way to split a chromosome into several feasible

```
EDASLS \(\left(\Theta, U T, p_{i s}, s_{r}\right)\)
Input: a set of instances \(\Theta\), the task set \(U T\), the probability of local search \(p_{i s}\)
Output: A robust solution \(s_{r}\)
begin
    construct the initial population pop using heuristics and random generation.
    for each \(c_{i} \in\) pop do
        \(F\left(c_{i}\right) \leftarrow \mathrm{CEvaluate}\left(c_{i}, \Theta\right)\).
        update \(s_{r}\)
    end
    sort pop in non-descending order according to the fitness value.
    until stopping criterion is reached do
        develop the edge histogram matrix ehm based on the best half individuals of pop.
        randomly select an individual \(T[]\) from pop.
        \(c \leftarrow \operatorname{EHBSA}(T[], n)\).
        Sample a random number \(r\) from the uniform distribution between 0 and 1.
        if \(r<p_{i s}\) then
            \(c^{\prime} \leftarrow\) StochasticLS \(\left(c, e h m, U T, \Theta, s_{r}\right)\);
            if \(c^{\prime}\) is not a duplicate of any \(c_{i} \in\) pop then
                \(c \leftarrow c^{\prime}\)
            end
    end
    CEvaluate \((c, \Theta)\).
    update \(s_{r}\)
    if \(c\) is better than \(T[]\) and \(c\) is not a duplicate of any \(c_{i} \in\) pop then
        \(T[] \leftarrow c\)
    end
    sort pop in non-descending order according to the fitness value.
    end
    return \(s_{r}\).
end
```

Fig. 1. The pseudo-code of $\operatorname{EDASLS}\left(\Theta, U T, p_{i s}, s_{r}\right)$.
routes. For a given chromosome $\mathrm{c}=\left(\tau_{1}, \tau_{2}, \ldots, \tau_{|U T|}\right)$, it builds an auxiliary graph $G^{*}$ with $(|U T|+1)$ vertices indexed from 0 to $|U T|$. Each arc $(i, j)$ models a subsequence $\left(\tau_{i+1}, \tau_{i+2}, \ldots, \tau_{j}\right)$ corresponding to a feasible route and is weighted by the route cost. The shortest path from vertex 0 to vertex $t$ indicates an optimal partition of the chromosome $c$. Bellman's algorithm [43] can be used to compute the shortest path in $O\left(|U T|^{2}\right)$. Note that for the same chromosome, the solution $s_{l_{j}}$ obtained by Ulusoy's splitting procedure on different $l_{j}$ might be different, leading to different costs.

Fig. 2 shows the pseudo code of the procedure CEvaluate $(c, \Theta)$ which calculates the fitness value of chromosome $c$.

## B. Edge histogram based sampling algorithm

This section briefly explains the EHBSA [28], which is used to generate offspring in EDASLS. EHBSA comprises of two phases: (1) modeling promising individuals, and (2) generating new individuals by sampling the model.

In each generation, an edge histogram matrix ehm for the promising individuals in the population is calculated. Let $p^{*}=\left\{c_{1}, c_{2}, \ldots, c_{l}\right\}$ represent the $l$ promising individuals. The elements in ehm are defined as:

$$
e h m_{i, j}= \begin{cases}\sum_{k=1}^{i}\left(\delta_{i, j}\left(c_{k}\right)+\delta_{j, i}\left(c_{k}\right)\right)+\epsilon & \text { if } i \neq j \\ 0 & \text { if } i=j\end{cases}
$$

where $\delta_{i, j}\left(c_{k}\right)$ is a delta function defined as:

$$
\delta_{i, j}\left(c_{k}\right)= \begin{cases}1 & \text { if there is a subsequence }(i, j) \text { in } c_{k} \\ 0 & \text { otherwise }\end{cases}
$$

and $\epsilon$ is a bias to control the pressure in sampling elements and can be computed as:

$$
\epsilon=\frac{2 l}{L-1} B_{\text {ratio }}
$$

where $B_{\text {ratio }}$ is a bias ratio ( $B_{\text {ratio }}>0$ ) and $L$ is the length of each permutation (chromosome). Intuitively, $e h m_{i, j}$ counts the number of adjacent element pairs $(i, j)$ and $(j, i)$ in the promising individuals plus a bias. Thus, the matrix ehm is symmetrical.

When applying EHBSA to UCARP, there exist some issues to be addressed. First, the elements in a permutation are required edges (tasks) rather than nodes. Since ehm learns the adjacency of consecutive elements, subsequence $(i, j)$ is considered to be the same as $(\operatorname{inv}(j), \operatorname{inv}(i))$ rather than $(j, i)$. The reason is that in our permutation structure, the implicit shortest path between elements $i$ and $j$ is the same as that between $\operatorname{inv}(j)$ and $\operatorname{inv}(i)$ (both are from $\operatorname{tail}(i)$ to head $(j)$ or in the opposite direction). Since the edges in the path are undirected, a path can be traveled along either direction). Moreover, a task should be served only once and can be served in either direction of an undirected arc. Hence, task $\tau$ and $\operatorname{inv}(\tau)$ cannot appear in the same chromosome.

Based on the characteristics of UCARP described above, the definition of ehm matrix in our approach differs from (11):

$$
e h m_{i, j}= \begin{cases}\sum_{k=1}^{l}\left(\delta_{i, j}\left(c_{k}\right)+\delta_{\operatorname{inv}(j), \operatorname{inv}(i)}\left(c_{k}\right)\right)+\epsilon & \text { if } i \neq j \\ 0 & \text { if } i=j\end{cases}
$$

```
CEvaluate \((c, \Theta)\)
Input: a set of instances \(\Theta\), a chromosome \(c\)
Output: the fitness of the chromosome \(F(c)\)
begin
    \(F(c) \leftarrow 0\)
    for each \(I_{j} \in \Theta\) do
        \(x_{i j} \leftarrow\) partition \(c\) on \(I_{j}\) using Ulusoy's splitting procedure.
        if \(T C\left(s_{i j}, I_{j}\right)>F(c)\) then
            \(F(c) \leftarrow T C\left(s_{i j}, I_{j}\right)\)
        end
    end
    return \(F(c)\)
end
```

Fig. 2. The pseudo-code of CEvaluate $(c, \Theta)$.
where $\delta_{i, j}\left(c_{\mathrm{k}}\right)$ shares the same definition as that of the original EHBSA as defined in (12). $\epsilon$ is defined as:

$$
\epsilon=\frac{1}{|U T|-1} B_{\text {ratio }}
$$

With the edge histogram matrix ehm, EHBSA can generate a new chromosome (permutation) by sampling ehm. In [28], the author proposed two variants of EHBSA. One is without a template (EHBSA/WO) and the other with a template (EHBSA/WT). The latter is shown to have better performance [28] and thus is employed in this work.

To summarize, EHBSA works as follows: in each generation, a template chromosome $T[]$ is randomly chosen from the best half individuals of the current population and then randomly divided into $n$ sub-segments. Subsequently, one of the sub-segments is randomly selected. The elements of the selected sub-segment are resampled one by one based on ehm. Fig. 3 shows the pseudo-code of the EHBSA employed in this work.

## C. Stochastic local search procedure

A novel local search procedure, called Stochastic Local Search (SLS), is adopted with a predefined probability $p_{i s}$ in EDASLS to improve the chromosome $c$ obtained by EHBSA. Recall that in EDASLS, an individual is encoded as a sequence of task IDs. Hence, the local search is carried out with so-called move operators. In SLS, four traditional move operators are used:

Single insertion $(u, v)$ : Single insertion moves a task $u$ after another task $v$. In UCARP, the edges, both non-required and required edges (tasks) are undirected. Therefore, both directions of $u$ are considered when inserting it to another position. The direction leading to a better improvement is chosen.

Double insertion $(u, v)$ : Two consecutive tasks $(u, w)$ are moved instead of a single task. Likewise, both directions $(u, w)$ and $(\operatorname{inv}(w), \operatorname{inv}(u))$ are considered.

Swap $(u, v)$ : Two candidate tasks $u, v$ are selected and exchanged. Both directions of the tasks are considered.

2-opt $(u, v)$ : For a chromosome $c=\left(\tau_{1}, \tau_{2}, \ldots, \tau_{r}\right)$, a sub-route $\left(\tau_{u}, \tau_{u+1} \ldots, \tau_{v}\right)(u \leq v)$ is selected and reversed. That is, $\quad\left(\tau_{u}, \tau_{u+1} \ldots, \tau_{v}\right) \quad$ is replaced by $\left(\operatorname{inv}\left(\tau_{v}\right), \ldots, \operatorname{inv}\left(\tau_{u+1}\right), \operatorname{inv}\left(\tau_{u}\right)\right)$. Unlike the previous three operators, we do not need to consider the direction because the

2-opt operator itself is an operator changing the direction of tasks.

To determine whether an intermediate chromosome obtained by a move operator is better, its fitness should be evaluated. For deterministic problems such as CARP, this can be done in constant time. Because only the change in cost of a chromosome and (or) the capacity violation of demand caused by a move need to be calculated. In SLS, a perturbation to a chromosome would change the order of a subsequence of tasks, thus affecting the optimal solution obtained by Ulusoy's splitting procedure. Consequently, evaluating the impact of a move on the total cost can be rather time consuming. As defined in (10), to evaluate a chromosome's fitness, we need to partition it on all the instances and calculate the total costs of the corresponding solutions. That means, one fitness evaluation requires calling the splitting procedure $N$ times ( $N$ is the number of instances as defined in Section II). As the time complexity of Ulusoy's splitting is $O\left(|U T|^{2}\right)$, it would take $O\left(N|U T|^{2}\right)$ to evaluate one intermediate chromosome. To scan all the $|U T|^{2}$ pairs of tasks, the time complexity would be $O\left(N|U T|^{4}\right)$. This is obviously quite time consuming compared with that of a local search procedure in CARP, which is $O\left(|U T|^{2}\right)$. To tackle this problem, the SLS procedure is developed to avoid expensive evaluations of unpromising moves.

Recall that the value of $\operatorname{ehm}_{i, j}$ in the edge histogram matrix reflects the adjacency of task $i$ and $j$ in the promising individuals. Tasks $\tau_{i}$ and $\tau_{j}$ with a larger value of $\operatorname{ehm}_{i, j}$ are more likely to be adjacent in the individuals with high performance. Intuitively, an improving local search move should increase the ehm value of adjacent tasks in the individual sequence. SLS is based on this idea. If a move reduces the adjacency of tasks, it will be considered to be an

```
EHBSA \((T[] \cdot \operatorname{ehm}, n)\)
Input: a template chromosome \(T[]\), the edge histogram matrix
ehm, number of sub segments \(n\)
Output: a child chromosome \(C[]\)
begin
    randomly divide the template individual \(T[]\) into \(n\) sub
    segments \(T_{0}[], \ldots T_{n}[]\).
    randomly choose one sub segment \(T_{i}[]\).
    \(\Omega \leftarrow\) all the tasks in \(T_{i}[]\).
    \(c t \leftarrow\) the task before \(T_{i}[0]\).
    for \(p \leftarrow 0\) to length \(\left(T_{i}[]\right)-1\) do
    construct a roulette wheel vector \(r w[]\) as \(r w[k]=\) \(\operatorname{ehm}_{c t, k}(k=1,2, \ldots 2 t)\).
    for \(k \leftarrow 1\) to \(2 t\) do
        if \(k \notin \Omega \& \& \operatorname{inv}(k) \notin \Omega\) then
        \(r w[k] \leftarrow 0\)
        \(r w[\operatorname{inv}(k)] \leftarrow 0\)
        end
        end
        sample \(T_{i}[p]=x\) with probability \(r w[x] / \sum_{j=1}^{2 t} r w[j]\).
        \(c t \leftarrow T_{i}[p]\)
        \(p \leftarrow p+1\)
        \(\Omega \leftarrow \Omega-\{c t\}\)
    end
    \(C[] \leftarrow T[]\)
    return \(C[]\)
end
```

Fig. 3. The pseudo-code of our $\operatorname{EHBSA}(T[] \cdot \operatorname{ehm}, n)$.

un-improving move. Hence, it is unnecessary to evaluate the fitness of the intermediate chromosome obtained by this move.

The SLS procedure can be described as follows: Given a chromosome $c$ generated by EHBSA, the SLS scans each pair of tasks $(u, v)$ in $O\left(|U T|^{2}\right)$ time. The previously mentioned four move operators are separately applied to $c$. To avoid excessive computation, every move is pre-evaluated on the basis of the edge histogram matrix ehm in the first phase of SLS, which costs constant time. For instance, for the move single insertion $(u, v)$, SLS first computes the value of $\Delta e h m=e h m_{i, l}+e h m_{e, u}+e h m_{u l}-e h m_{i, u}-e h m_{u, l}-$ $e h m_{e, l}$, where $i$ and $j$ represent the tasks before and after $u$, respectively, and $l$ is the task after $v$. If $\Delta e h m$ is positive, this move is considered to be promising and the fitness of the corresponding chromosome will be evaluated with Eq. (10) in the second phase. Otherwise, the corresponding chromosome will be discarded directly. The first improved chromosome produced by each move operator is preserved. By this means, we will obtain four improved intermediate chromosomes $c_{s i}, c_{d i}, c_{\text {swap }}$ and $c_{2-o p t}$. The one with optimal fitness will be chosen to replace the current chromosome $c$. This process repeats until the current chromosome can no longer be improved. Fig. 4 gives the pseudo-code of SLS.

## D. Other components of EDASLS

Initialization: during the initialization phase, an initial population with popsize chromosomes is constructed. Chromosomes in the initial population are generated either by heuristics or at random. A constructive heuristic called path-scanning (PS) [5] is executed to generate five solutions (task sequences with route delimiters) according to the five rules in PS. The solutions are then concatenated into five chromosomes by removing the route delimiters from the solution sequences. Since PS is a well-known heuristic, we omit its details in this paper. Interested readers may refer to the original paper [5]. The remaining popsize -5 chromosomes are generated by a best-insertion heuristic (BIH). BIH starts with an empty route. In each iteration, the task satisfying the capacity constraint and with the minimal increased cost is inserted into the route. If no task satisfies the capacity constraint, a new empty route is initialized and the procedure repeats until all the tasks are inserted. The solution obtained is then also concatenated into a chromosome and inserted into the population. Note that both PS and BIH are deterministic algorithms and cannot be directly executed on UCARP instances. As our UCARP is approximated by a set of CARP instances, the aforementioned two heuristics are executed on randomly selected CARP instances. In order to increase the diversity of the population, no duplicates are allowed to appear in the population. The maximal trials for generating non-redundant initial individuals by using BIH are bounded to ubtrial. If the number of trials exceeds ubtrial, individuals are directly generated at random.

Stopping criterion: The EDASLS stops when a maximal number of fitness evaluations, $F E_{m}$, is met.

Update of robust solutions: As described in the previous sections, a population is composed of chromosomes (giant routes without route delimiters). However, the final solution is a sequence of tasks with route delimiters. Thus, a chromosome

```
StochasticLS \((c, e h m, U T, \Theta, s_{r,}\)
Input: a chromosome \(c\), the edge-histogram matrix \(e h m\), the
task set \(U T\), a set of instances \(\Theta\)
Output: an improved chromosome \(c^{\prime}\), a robust solution \(s_{r}\)
begin
    until \(c\) can no longer be improved do
        \(c_{s i} \leftarrow \operatorname{Sl}\left(c, e h m, U T, \Theta, s_{r}\right)\)
        \(c_{d i} \leftarrow \operatorname{DI}\left(c, e h m, U T, \Theta, s_{r}\right)\)
        \(c_{\text {swap }} \leftarrow \operatorname{Swap}\left(c, e h m, U T, \Theta, s_{r}\right)\)
        \(c_{2-\text { opt }} \leftarrow 2 \_\)opt \(\left(c, e h m, U T, \Theta, s_{r}\right)\)
        \(c \leftarrow\) the best one of \(c_{s i}, c_{d i}, c_{\text {swap }}\) and \(c_{2-\text { opt }}\)
    end
    return \(c^{\prime}\)
end
```

$\mathbf{S I}\left(c, e h m, U T, \Theta, s_{r}\right)$
Input: a chromosome $c$, the edge-histogram matrix ehm, the task set $U T$, a set of instances $\Theta$
Output: an improved chromosome $c^{\prime}$, a robust solution $s_{r}$ begin
$c_{s i} \leftarrow c$
for all the pair of tasks $(u, v)$ in the task set $U T$ do move task $u$ after task $v$ in $c_{s i}$

$$
\begin{aligned}
& \Delta e h m \leftarrow \sum_{i=1}^{i-1} e h m_{c_{s i} \mid\left(c_{s i} \mid+1\right)}-\sum_{i=1}^{i-1} e h m_{C[i], C[i+1]} \\
& \text { if } \Delta e h m>0 \text { then } \\
& \quad F\left(c_{s i}\right) \leftarrow \text { CEvaluate }\left(c_{s i}, \Theta\right) \\
& \quad \text { update } s_{r} \\
& \quad \text { if } F\left(c_{s i}\right)<F(c) \text { then } \\
& \quad \text { return } c_{s i} \\
& \quad \text { end } \\
& \quad \text { end } \\
& \quad \text { return } c_{s i} \\
& \text { end }
\end{aligned}
$$

Note: The procedures of DI, Swap and 2-opt are similar to that of SI except that the move operations are different. Hence we omit the presentation of these algorithms.

Fig. 4. The pseudo-code of StochasticLS(c, ehm, $U T, \Theta)$.
should be converted into a solution. A difficult issue to be addressed here is how to partition a chromosome $c$ into a solution $s$ with minimal $R(s)$ (defined in Section II). As the vehicle number is unfixed, the solution space of this problem is very large. To determine the optimal partition scheme with respect to $R(s)$ would be another hard optimization problem. To get around this problem, we follow the idea in Section III.A. A chromosome is first partitioned into $|\Theta|$ solutions on the $|\Theta|$ CARP instances in order to evaluate its fitness. The one with the minimal $R(s)$ among the $|\Theta|$ solutions is then compared to the current best robust solution. The one with minimal $R(s)$ will be retained. By this means, only a small part of the partition schemes will be checked. Assume the number of chromosome evaluations is $F E$, the number of solutions being checked is then $|\Theta| \cdot F E$. We do this for two reasons: (1) it saves much time to calculate $R$ of $|\Theta| \cdot F E$ solutions rather than all the solutions in the solution space; (2) different instances in $\Theta$ share a similar structure and hence may have approximate values of parameters.

## IV. EXPERIMENTAL STUDIES

## A. Benchmark instances

The UCARP test instances generated in [24], i.e., $u g d b$ and

TABLE I
THE PARAMETERS OF EDASLS

TABLE II
RESULTS ON THE ugdb BENCHMARK TEST SET IN TERMS OF THE WORST-CASE SOLUTION COSTS


Time: average execution time (in CPU seconds) over 20 independent executions;
Average: the average value over the 20 executions;
Std: standard deviation over the 20 executions;
$p$-value: $p$-values of ANOVA tests for comparing EDASLS, EDA/NoLS, MA1 and MA2.
The minimal average results are with "*". Bold (underlined) results indicate that the corresponding algorithm is better (worse) than EDASLS based on Wilcoxon rank-sum test with the level of significance $\alpha=0.05$.
\#. of 'w-d-1': the number of 'win-draw-lose' of EDASLS versus the other algorithms; mean: the average values on all test instances.
uval sets, are used in the experimental studies. The ugdb instances are small-scale instances with 7-27 vertices and 11-55 edges, and uval instances are medium-scale instances with $24-50$ vertices and $34-97$ edges. All the edges in the corresponding CARP instances are required edges (tasks). Each UCARP instance contains 30 CARP instances generated by extending the same CARP instance. Thus, the 30 CARP instances share a similar graph structure and have similar (but not the same) values of parameters.

When Mei et al. [24] proposed UCARP, they also provided a procedure to generate UCARP instances by extending the
well-known deterministic CARP instances. For each deterministic CARP instance, 30 UCARP instances are generated using the instance generator ${ }^{1}$, with the starting random seed of 0 . If necessary, more uncertain instances can be generated by the generator with other random seeds. The known random seeds enable us to re-produce the instances for our comparative studies.
${ }^{1}$ Available at http://staff.ustc.edu.cn/ ketang/codes/UCARPGen.zip

TABLE III
RESULTS ON THE uval BENCHMARK TEST SET IN TERMS OF THE WORST-CASE SOLUTION COSTS

Time: average execution time (in CPU seconds) over 20 independent executions;
Average: the average value over the 20 executions;
Std: standard deviation over the 20 executions;
$p$-value: $p$-values of ANOVA tests for comparing EDASLS, EDA/NoLS, MA1 and MA2.
The minimal average results are with " $*$ ". Bold (underlined) results indicate that the corresponding algorithm is better (worse) than EDASLS based on Wilcoxon rank-sum test with the level of significance $\alpha=0.05$.
\#. of 'w-d-l': the number of 'win-draw-lose' of EDASLS versus the other algorithms; mean: the average values on all test instances.

## B. Algorithms tested and parameter settings

To evaluate the efficacy of EDASLS, a series of experiments on the aforementioned benchmark test sets are conducted. In order to evaluate our algorithm, we compared it against the following baseline approach: solve all CARP instances using a state-of-the-art approach for CARP, and the most robust solution among them is selected as the final solution. One of such state-of-the-art algorithms is a recently proposed meta-heuristic, named memetic algorithm with iterated local search (MAILS) for CARP [44]. MAILS is executed on all the

CARP instances $I_{j} \in \Theta$ to obtain $|\Theta|$ solutions $S_{\text {dcarp }}=$ $\left\{S_{1}, S_{2}, \ldots S_{|\Theta|}\right\}$, each $S_{i} \in S_{\text {dcarp }}$ is executed on all $I_{j} \in \Theta$ to calculate $R\left(S_{i}\right)$, the one with the minimal $R\left(S_{i}\right)$ is selected as the final robust solution.

Other compared algorithms are the two variants of MA for UCARP proposed in [27] (MA1 and MA2). By replacing the expectation-based fitness function with the minimax fitness function defined in Section III.A, these approaches are modified to suit the minimax fitness function.

To investigate the contributions of the SLS to EDASLS, an

![img-0.jpeg](img-0.jpeg)

Fig. 5. The box plots on the ugdb benchmark test set in terms of the worst-case solution costs, where 1, 2, 3,4 in x-axis stand for EDASLS, EDA/NoLS, MA1, MA2, respectively.

EDA without SLS (EDA/NoLS), in which SLS is removed while all the other components of EDASLS is kept, was also involved in the comparison.

In order to ensure the fairness of the comparison, all algorithms except MAILS were assigned with the same number of fitness evaluation number $F E_{m}$. The termination conditions of MAILS, as well as all its other parameters, were set to the values presented in the original publication.

TABLE I summarizes the parameter settings of EDASLS, determined after some preliminary experiments. All the experiments were conducted for 20 independent executions, and the averages and standard deviations of the results are reported in this paper.

## C. Comparing EDASLS to existing algorithms

## 1) Performance metrics

TABLE II and TABLE III report the results on ugdb and uval benchmark sets, respectively. The columns 'Time', 'Average' and 'Std' stand for the average execution time, average cost and standard deviation of cost over 20 independent executions. Results marked with "*" indicate the minimal average cost. In our experiments, all the algorithms are coded in $\mathrm{C}++$ language using an Intel(R) Xeon(R) E5620 2.40GHz. Other algorithms are compared to EDASLS by using Wilcoxon rank-sum test with the level of significance $\alpha=0.05$ over 20 executions. For EDA/NoLS, MA1, MA2 and MAILS, the average results
highlighted in bold indicate that, statistically, the corresponding algorithm is significantly better than EDASLS. The underlined results indicate the corresponding algorithm is significantly worse than EDASLS. Results without any symbol indicate that the difference between EDASLS and the corresponding algorithm is statistically insignificant. Take TABLE II as an example, for ugdb1, the average result of EDA/NoLS (370.34) is underlined, indicating that EDASLS performed significantly better than EDA/NoLS on ugdb1. The average result of EDASLS (368.40) is marked with "*", indicating that EDASLS was the best-performing algorithm on ugdb1. For ugdb10, the average result of MA2 (302.05) is highlighted in bold, which means MA2 performed significantly better than EDASLS on ugdb10. The average result of MA1 (304.27) is not highlighted, meaning that statistically, there is no significant difference between EDASLS and MA1 on ugdb10.

For each table, two additional rows are included at the bottom. The first row represents the number of 'win-draw-lose' of EDASLS versus the other algorithms. The second row summarizes the average values for each algorithm on all the test instances.

Considering the columns headed 'Average' in TABLE II and TABLE III, we can observe that EDASLS outperforms the compared algorithms in almost all cases. Specifically, EDASLS outperforms MA1 on 18 out of 23 ugdb instances and 32 out of 34 uval instances. The gap between EDASLS and

![img-1.jpeg](img-1.jpeg)

Fig. 6. The box plots on the uval benchmark test set in terms of the worst-case solution costs, where 1, 2, 3,4 in x-axis stand for EDASLS, EDA/NoLS, MA1, MA2, respectively.

MA2 is also significant. On 12 out of 23 ugdb instances and 24 out of 34 uval instances, EDASLS is the winner. Only on four instances (ugdb 10, ugdb 22, uval1A and uval10A) EDASLS is inferior to MA2 with small gaps ( $0.9,0.47,1.72$ and 2.26). When compared to MAILS, EDASLS shows more significant advantage, outperforming MAILS on 21 of 23 ugdb instances and on all uval instances. The gaps between the average values are quite large ( 46.14 for $u g d b$ and 183.82 for $u v a l$ ). Compared with EDA/NoLS, EDASLS is also competitive, winning on 10 instances of the $u g d b$ set and 33 instances of the uval set.

In terms of the standard deviations, TABLE II shows that the average standard deviation of the results obtained by EDASLS over all the instances of $u g d b$ set is just 1.75 , while those obtained by EDA/NoLS, MA1, MA2 and MAILS are $2.08,2.87,2.15$ and 12.00 , respectively. The results on the uval set reported in TABLE III are similar. Although the average standard deviation obtained by EDASLS is not the lowest (3.54), it is quite close to the lowest value of 3.47 obtained by MA2. A closer look at TABLE II and TABLE III also shows that the largest standard deviation is 7.82 (uval $5 D$ ) for EDASLS, while for EDA/NoLS, MA1, MA2 and MAILS are 13.07 (uval 5D), 13.74 (uval 4D), 8.31 (uval 4D) and 165.77 (uval 4B), respectively. These observations highlight the advantage of EDASLS in terms of solution robustness and stability.

There are some particular phenomena that are worth noticing
in TABLE II and TABLE III. In ugdb15, the results show that solutions obtained by all the algorithms have the same performance over 20 executions. This is because the graph of ugdb15 is a very simple and complete one with only eight vertices. Despite the uncertainties, it is still quite easy to solve ugdb15. Another interesting observation is that in some of the uval instances, such as uval9A uval9C and uval10A uval10C, MAILS performs poorly. This phenomenon is due to the characteristics of the instances. On these instances, the values of demands vary greatly over tasks. And the absence of a task would affect the problem instance. Thus, an optimal solution for one instance (one scenario) might collapse on another instance in which a "was-required" task with a large demand disappears or an originally absent task emerges, leading to a large recourse cost.

Additionally, ANOVA tests were also conducted to compare the performance of EDASLS, EDA/NoLS, MA1 and MA2. MAILS was excluded because the previous analysis showed that MAILS was uncompetitive. The $p$-values of ANOVA tests are presented in the ' $p$-value' columns in TABLE II and TABLE III. It can be observed that the compared approaches are significantly different for the $95 \%$ confidence interval on all of the instances except for ugdb15, ugdb19 and ugdb20. To depict the performance of the tested approaches, the box plots of EDASLS, EDA/NoLS, MA1 and MA2 on all instances are presented in Fig. 5 and Fig. 6. Fig. 5 shows that solutions

![img-2.jpeg](img-2.jpeg)

Fig. 7. The convergence curves of EDASLS, MA1, MA2 and EDA/NoLS on instances ugdb3, ugdb23, uval1A and uval9C.
obtained by EDASLS are more stable than those obtained by other tested approaches on most of the ugdb test instances. For the uval test instances, EDASLS clearly performed better than EDA/NoLS. This indicates that the SLS procedure indeed greatly improved the algorithm's performance. When compared to MA1 and MA2, EDASLS also showed advantages.

With regard to the execution time, EDASLS is also very competitive, although it is not the most efficient one among all the tested algorithms. EDASLS is only inferior to MA1.

To study the convergence speed of the tested algorithms, the convergence curves of the compared algorithms are plotted on four typical instances in Fig. 7. Pictures on other instances are similar. MAILS is not included in the figure because of its different basic framework from other algorithms. It can be observed that EDASLS converged the fastest among the compared algorithms. However, due to its fast convergence, it could converge to a local optimum (e.g., on uval 1A). To avoid this situation, the diversity of individual population needs to be increased, which will be a topic of our future research.

The observation that EDASLS outperforms the other algorithms demonstrates the efficiency of EDASLS. The reasons of EDASLS's excellent performance can be summarized as follows: (1) the quality of a solution to UCARP heavily depends on the order of tasks being served. In a robust
solution, closely related tasks are more likely to be served adjacently to each other. In EDASLS, we build the edge histogram matrix to learn the adjacency information of tasks. New individuals are generated based on this information. By this means, the closely related fragments of solutions have a higher chance to be retained, making it easier to find the robust solution. (2) In the stochastic local search procedure, only the moves that put related tasks closer and produce chromosomes with better fitness are implemented. This strategy not only improves the quality of chromosomes but also avoids a large amount of excessive computations of fitness.
2) Structure metrics

Further analysis on the structures of the solutions obtained by EDASLS may deepen our understanding of UCARP. As mentioned in Section II, stochastic demands of tasks might incur route failures (violations of vehicle capacity constraints). When a route failure occurs, the recourse strategy amends the infeasible route by returning to the depot to get vehicle replenished before serving the next task. This "return-and-back" replenishment process would incur additional cost, which could be a large proportion of the total cost if the route failure occurs frequently. Since our goal is to minimize the total costs of solutions, it is meaningful to investigate the frequency of occurrence of route failure. Hence, a new structure metric $R f$ is defined. $R f$ is the route failure ratio of a solution in all

$$
\begin{aligned}
& Q=4 \\
& s=\left(R_{1}, R_{2}\right)=\left(0, \tau_{1}, \tau_{2}, \tau_{5}, 0, \tau_{3}, \tau_{4}, 0\right) \\
& R f=0.5 \\
& E x=1 \\
& \text { ![img-6.jpeg](img-6.jpeg) } \\
& \text { load }\left(R_{1}, I_{1}\right)=4 \\
& \text { load }\left(R_{2}, I_{1}\right)=4
\end{aligned}
$$

![img-7.jpeg](img-7.jpeg)
![img-8.jpeg](img-8.jpeg)
load $\left(R_{1}, I_{2}\right)=6$
$\operatorname{load}\left(R_{2}, I_{2}\right)=4$
![img-6.jpeg](img-6.jpeg)
![img-7.jpeg](img-7.jpeg)
load $\left(R_{1}, I_{3}\right)=7$
$\operatorname{load}\left(R_{2}, I_{3}\right)=5$

Fig. 8. An illustrative example of the structure metrics $R f$ and $E x$.
scenarios of scenario set $\Theta$. For solution $s=\left(R_{1}, R_{2}, \ldots, R_{\mathrm{m}}\right)$, $R f$ is defined as:

$$
R f=\frac{\sum_{j \in \Theta} \sum_{k=1}^{\mathrm{m}} \operatorname{sgn}\left(\max \left\{\operatorname{load}\left(R_{k}, I_{j}\right)-Q, 0\right\}\right)}{\mathrm{m} \cdot|\boldsymbol{\theta}|}
$$

where $\operatorname{sgn}(x)$ is the sign function defined as:

$$
\operatorname{sgn}(x)= \begin{cases}1 & \text { if } x>0 \\ 0 & \text { if } x=0 \\ -1 & \text { if } x<0\end{cases}
$$

and $\operatorname{load}\left(R_{k}, I_{j}\right)$ denotes the total demand of route $R_{k}$ in scenario $I_{j}$.

As can be seen from (16) and (17), $R f$ is concerned with the number of route failures while ignoring the quantity of capacity constraint violation. In real-world situations, when route failure is inevitable, one would hope the quantity of violation to be as small as possible. Thus, we also define another structure metric $E x$, which is the ratio of capacity violation. Similar to $R f, E x$ is defined as:

$$
E x=\frac{\sum_{j \in \Theta} \sum_{k=1}^{\mathrm{m}} \max \left\{\operatorname{load}\left(R_{k}, I_{j}\right)-Q, 0\right\}}{m \cdot|\boldsymbol{\theta}|}
$$

$R f$ and $E x$ are similar but are concerned with different aspects of a solution. The former measures the number of route failures while the latter is concerned with the quantity of capacity violation when a route failure occurs. Fig. 8 gives a simple example to illustrate the two metrics. Each graph corresponds to a scenario. The tasks (edges) are labeled as task IDs with demands in brackets. Assuming a solution $s=$ $\left(0, \tau_{1}, \tau_{2}, \tau_{5}, 0, \tau_{3}, \tau_{4}, 0\right)$ with two routes $R_{1}$ and $R_{2}$ and a capacity $Q=4$. Due to the uncertain demands of tasks, route failures occur in route $R_{1}$ (with a capacity violation of 2 ) in scenario $I_{2}$ and $R_{1}$ (with capacity violation 3 ) and $R_{2}$ (with capacity violation 1) in scenario $I_{3}$. The total number of route failures is 3 and the total violation of capacity is 6 . Hence, the values of $R f$ and $E x$ are $3 /(2 \times 3)=0.5$ and $6 /(2 \times 3)=1$, respectively.

Fig. 9 depicts the histograms of the $R f$ and $E x$ on instances uval $8 C$ and uval5D. For the convenience of cross-comparison,
the histograms of costs are also shown. All values are the averages of results of 20 independent executions. On both instances, EDASLS achieved the lowest average costs among the five algorithms. It can be observed that for EDASLS, the values of $R f$ and $E x$ generally coincide with the costs. To be specific, the solution obtained by EDASLS corresponds to the lowest $R f$ and $E x$ on uval $8 C$, and the second lowest $R f$ and $E x$ on uval5D. These observations support our conjecture that less route failures could save more additional replenishment cost and lead to lower total cost. Although the two structure metrics of the solution obtained by EDASLS are slightly higher than those achieved by EDA/NoLS, the differences between the two methods are relatively small, e.g., 0.14 to 0.12 in terms of $R f$. In this case, the additional cost induced by the slight increase in number of route failures may be insignificant in comparison to the total cost. Hence, EDASLS still managed to achieve a lower total cost.
3) Further investigation of SLS

To further investigate the influence of the first phase of SLS, i.e., the calculation of $e h m$ value to pre-evaluate intermediate
![img-8.jpeg](img-8.jpeg)

Fig. 9. The histograms of $R f, E x$ and cost on instances uval8C and uval5D.

![img-9.jpeg](img-9.jpeg)

Fig. 10. Average costs of the "after-local-search" individuals obtained by LS and SLS versus generations.
individuals, we removed it from SLS while keeping the other parts unchanged. By this means, SLS turns into traditional LS. The resultant LS was applied to the same individuals that undergo the SLS procedure. That is, in each local search process, LS and SLS were executed on the same offspring and two improved individuals were produced and compared with each other. Fig. 10 gives the results of average cost of the "after-local-search" individual versus generation on three typical instances. Results on other instances are not reported because of the page limit. Note that each pair of "after-local-search" individuals was generated from the same neighborhood of an individual to make a fair comparison.

The results on instance ugdb3 show that there is no apparent gap between the results obtained by EDASLS and those obtained by EDALS. This observation indicates that the pre-evaluation phase of SLS does not misjudge the intermediate individual, i.e., intermediate individuals with good fitness are not discarded in the first phase of SLS. Taking a closer look at the results on instance uval3A, we observe that in early generations, LS achieved solutions with lower costs than EDASLS. However, in later generations, EDASLS caught up with EDALS. The reason is that the quality of the edge histogram matrix could greatly affect the performance of SLS. In early generations, the population is not well evolved, thus the edge histogram matrix is not very reliable, leading to misjudgments in the pre-evaluation phase of SLS. In later generations, individuals in the population are generally of higher quality. In consequence, the pre-evaluation phase of SLS is more correct. Results on instance uval1A can be divided into three stages. The first two show the similar trend to that on uval3A. While in the last stage, the line of SLS is higher than that of LS, indicating a higher ratio of misjudgment in the pre-evaluation phase of SLS. This may be because the edge histogram matrix learned from the population overfitted the convergent population. Thus, new individuals (might have good performance) with different structures from those in the population are discarded because they cannot enhance the correlation of adjacent tasks.

TABLE IV summarizes the average execution time of EDAs

TABLE IV Average Runtime Over 20 Runs (In CPU Seconds) of the COMPARED Algorithms on the Test Sets.


with SLS and with LS on all tested instances over 20 independent runs. The results show that SLS is much faster than LS, especially on the medium-sized uval set.

## V. CONCLUSION AND FUTURE WORK

In this paper, we formulate UCARP as a minimax optimization problem. An EDA with a novel stochastic local search (EDASLS) is devised for solving UCARP. The EDASLS algorithm is featured with: (1) a problem-dependent chromosome structure and evaluation strategy, and (2) a two-phase stochastic local search procedure (SLS) to avoid redundant fitness evaluations in local search. From the experimental results, three conclusions can be drawn. First, EDASLS is capable of obtaining solutions with better "worst-case" performance. Second, the SLS plays an important role in EDASLS. It prevents excessive fitness evaluations of unpromising moves in traditional local search and hence accelerates the algorithm without reducing the performance. Third, although a UCARP can be approximated by a set of CARP instances, it is not a good choice to separately solve the CARP instances using existing CARP algorithms, because the optimal solution to one single CARP instance might have poor robust performance.

Despite its excellent performance in terms of both solution quality and efficiency, EDASLS is by no means perfect. The main disadvantage of EDASLS is that it is confined to a finite number of deterministic instances. Hence, a potential direction to be explored in the future is to develop approaches that can achieve robust solutions over an infinite set of CARP instances, e.g., representing the uncertainty of the demand of tasks using intervals. Since UCARP takes into account of the uncertainties that might occur in reality, it is much closer to real-world applications, than deterministic CARPs. Extending EDASLS to tackle relevant practical problems, such as path planning of mobile robot or unmanned aerial vehicles, is also an important and interesting future work.

## ACKNOWLEDGMENT

This work was supported in part by the 973 Program of China under Grant 2011CB707006, the National Natural Science Foundation of China under Grants 61175065 and 61329302, the Program for New Century Excellent Talents in University under Grant NCET-12-0512, the Science and Technological Fund of Anhui Province for Outstanding Youth under Grant 1108085J16, the European Union Seventh Framework Programme under Grant 247619, and an EPSRC grant (No. EP/I010297/1). Jose A. Lozano is partially supported by the Basque Government (IT609-13), and Spanish Ministry of Economy and Competitiveness MINECO (BCAM Severo Ochoa excellence accreditation SEV-2013-0323 and TIN2013-41272P). Xin Yao was support by a Royal Society Wolfson Research Merit Award.
