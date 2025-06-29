# Research Article 

## An Integrated Method Based on PSO and EDA for the Max-Cut Problem

Geng Lin ${ }^{1}$ and Jian Guan ${ }^{2}$<br>${ }^{1}$ Department of Mathematics, Minjiang University, Fuzhou 350108, China<br>${ }^{2}$ Modern Educational Technology Center, Minjiang University, Fuzhou 350108, China<br>Correspondence should be addressed to Geng Lin; lingeng413@163.com

Received 20 November 2015; Revised 12 January 2016; Accepted 26 January 2016
Academic Editor: Dominic Heger
Copyright © 2016 G. Lin and J. Guan. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

The max-cut problem is NP-hard combinatorial optimization problem with many real world applications. In this paper, we propose an integrated method based on particle swarm optimization and estimation of distribution algorithm (PSO-EDA) for solving the max-cut problem. The integrated algorithm overcomes the shortcomings of particle swarm optimization and estimation of distribution algorithm. To enhance the performance of the PSO-EDA, a fast local search procedure is applied. In addition, a path relinking procedure is developed to intensify the search. To evaluate the performance of PSO-EDA, extensive experiments were carried out on two sets of benchmark instances with 800 to 20000 vertices from the literature. Computational results and comparisons show that PSO-EDA significantly outperforms the existing PSO-based and EDA-based algorithms for the max-cut problem. Compared with other best performing algorithms, PSO-EDA is able to find very competitive results in terms of solution quality.

## 1. Introduction

The max-cut problem is one of the most classical combinatorial optimization problems. It is formally defined as follows. Given an undirected graph $G(V, E)$, with vertices set $V=$ $\{1, \ldots, n\}$ and edges set $E$, each edge $(i, j) \in E$ being associated with a weight $w_{i j}$, the max-cut problem is to find a partition $\left(V_{1}, V_{2}\right)$ of $V$, so as to maximize the sum of the weights of the edges between vertices in the different subsets.

Let $x=\left(x_{1}, \ldots, x_{n}\right)^{T} \in\{1,-1\}^{n}$ denote a solution of the max-cut problem. $x_{i}=1\left(x_{i}=-1\right)$ indicates that vertex $i$ is partitioned into $V_{1}\left(V_{2}\right)$. Let $W=\left(w_{i j}\right)_{\text {tren }}$ be the symmetric weighted adjacency matrix of $G$. The max-cut problem can be formulated as the following discrete quadratic optimization problem $[1]$ :

$$
\begin{aligned}
& \text { (MC) } \\
& \max f(x)=x^{T} \bar{L} x \\
& \text { s.t. } x_{i} \in\{1,-1\}, \quad i \in\{1, \ldots, n\}
\end{aligned}
$$

where $\bar{L}=\operatorname{Diag}(W e)-W$ is the Laplace matrix of $G$.

The max-cut problem has long served as a challenging test for researchers testing new methods for combinatorial algorithms [2] and has a wide range of practical applications such as numerics, scientific computing, circuit layout design, and statistical physics. It is one of the Karp's original NP-complete problems [3].

Due to the significance of the max-cut problem in academic research and real applications, it has gained much attention over the last decade. Because of the NP-hardness of the max-cut problem, heuristics have a crucial role for the solution of large scale instances in acceptable computing time. Various heuristic methods have been proposed including rank-two relaxation heuristic [4], GRASP [5, 6], scatter search [7], filled function method [1], dynamic convexized method [8], tabu Hopfield network and estimation of distribution [9], tabu search [2], particle swarm optimization [10], path relinking [11], breakout local search [12], and tabu search based hybrid evolutionary algorithm [13]. Among the above heuristic algorithms, breakout local search, path relinking, and tabu search based hybrid evolutionary algorithm are the best heuristics for solving challenging max-cut problems.

```
Require: A graph \(G\).
Ensure: A solution \(x^{\prime \prime}\).
(1) Set \(g=1, \operatorname{Pop}(g)=\left\{x^{1}, \ldots, x^{s}\right\}\) is generated randomly.
(2) for each \(x^{i} \in \operatorname{Pop}(g)\) do
(3) \(\quad x^{i}=L S\left(x^{i}\right)\).
(4) end for
(5) Let \(\bar{x}^{i}=x^{i}\), and \(x^{*}=\arg \max \left\{f\left(x^{i}\right), i=1, \ldots, s\right\}\).
(6) Initialize the probability vector \(p^{g-1}=(0.5, \ldots, 0.5)\).
(7) while \(g \leq\) Maxcount do
(8) if \(g\) can be divided by 2 then
(9) PSO procedure is executed to generate a new population \(\operatorname{Pop}^{t}(g)\).
(10) else
(11) EDA procedure is performed to generate a new population \(\operatorname{Pop}^{t}(g)\).
(12) end if
(13) Let \(\operatorname{Pop}(g+1)=\operatorname{Pop}^{t}(g)\).
(14) if \(x^{*}\) is not improved after \(G_{\mathrm{no}}\) continuous generations then
(15) for each \(\bar{x}^{i}(i=1, \ldots, s)\) do
(16) \(\bar{x}^{i}=\) mutation \(\left(\bar{x}^{i}\right)\).
(17) \(\bar{x}^{i}=L S\left(\bar{x}^{i}\right)\).
(18) end for
(19) end if
(20) Let \(g=g+1\).
(21) end while
(22) return \(x^{\prime \prime}\)
```

Algorithm 1: General structure of PSO-EDA.

Particle swarm optimization (PSO) [14] is one of the most popular population-based algorithms. In this technique, all particles search for food in the search space based on their positions and velocities. Every particle can adjust its flying direction by learning from its own experience and the performance of its peers [15]. Different variants of PSO have been shown to offer good performance in a variety of continuous and discrete optimization problems [16, 17]. Although information between particles is shared with each other to some extent, it is performed in a strictly limited fashion, and the global information about the search space is not utilized.

Estimation of distribution algorithm (EDA) [18] is a new paradigm in the field of evolutionary computation and has been applied to solve many optimization problems [19-21]. It uses a probability model, which gathers the global information of the search space, to generate promising offsprings. The probability model is updated at each generation using the global statistical information. However, the local information of the solutions found so far is not utilized. The algorithm may get stuck at local optima due to lack of diversity.

Blum et al. [22] observed that complementary characteristics of different optimization heuristics benefit from hybridization; for example, see [23, 24]. In this work, we focus on developing an integrated algorithm (PSO-EDA) based on PSO and EDA to benefit from the advantages of PSO and EDA. The integrated algorithm PSO-EDA consists of hybridization of PSO, EDA, local search procedure, path relinking, and mutation procedure. PSO is utilized to find local information of the search space quickly, while EDA is used to guide the search by the global information. Local search procedure and path relinking are applied to further improve the solution
quality. To maintain the diversity, mutation procedure is adopted. The integrated algorithm overcomes the shortcomings of PSO and EDA and keeps a proper balance between diversification and intensification during the search. We use two sets of 91 benchmark instances from the literature to test the performances of the PSO-EDA. The comparisons of PSOEDA with the existing PSO-based and EDA-based algorithms for the max-cut problem show that PSO-EDA significantly outperforms these algorithms in terms of solution quality and solution time. Compared with other metaheuristic algorithms, including GRASP, breakout local search, path relinking, and tabu search based hybrid evolutionary algorithm, PSO-EDA can find very competitive results in terms of solution quality. Moreover, PSO-EDA finds the best known solutions on 62 instances out of total 91 instances. In addition, its deviations range from $0.01 \%$ to $0.47 \%$. It shows that the proposed algorithm is able to find high quality solutions of the max-cut problem.

The remainder of this paper is organized as follows. Section 2 describes a detailed explanation of the PSO-EDA. The computational results and comparisons are given in Section 3. The conclusion remarks are made in Section 4.

## 2. The Proposed Algorithm

2.1. The Framework of PSO-EDA. The general structure of the PSO-EDA is given in Algorithm 1. Essentially, PSOEDA alternates between PSO procedure and EDA procedure. PSO procedure and EDA procedure play different roles in PSO-EDA. PSO procedure is used to gather the local information. The obtained local information is then used to

update the probability vector while EDA procedure is used to guide the search by the global information. It generates new promising solutions. These two complementary procedures are iteratively performed to obtain high quality solutions.

In the PSO-EDA, $(n-1)$-dimensional probability vector $p=\left(p_{2}, \ldots, p_{n}\right) \in[0,1]^{n-1}$ is used to represent the probability model of the solution space, where $p_{j}(j=$ $2, \ldots, n)$ is the probability of $x_{j}=x_{1}$. Let $g$ be the current generation. At the beginning of PSO-EDA, a population $\operatorname{Pop}(g)$ consisting of $s$ particles is generated randomly, and each particle is further improved by a local search procedure. Let $\tilde{x}^{i}$ be the personal best position of particle $i$, and let $x^{*}$ be the best solution found so far. We initialize $\tilde{x}^{i}=x^{i}$ and $x^{*}=\arg \max \left\{f\left(x^{i}\right), i=1, \ldots, s\right\}$. The probability vector is initialized as $p=(0.5, \ldots, 0.5)$. Then, PSO procedure and EDA procedure are executed alternately. If $g$ can be divided by 2, EDA procedure is performed; otherwise, PSO procedure is executed. After that, a new population $\operatorname{Pop}^{l}(g)$ is generated and is used to form the next population $\operatorname{Pop}(g+1)$. If the current best solution $x^{*}$ is not improved after $G_{m}$, continuous generations, the current personal best solutions can not guide the search efficiently. Each $\tilde{x}^{i}$ is perturbed by a mutation procedure and improved by the local search procedure. The obtained solution is used to replace the personal best solution of particle $i$. The above process is repeated until Maxcount of generations is reached.

The PSO-EDA consists of five main components: PSO procedure, EDA procedure, local search procedure, path relinking procedure, and mutation procedure. These procedures are described in detail in the following subsections.
2.2. PSO Procedure. The standard PSO is introduced for solving continuous optimization problems. To deal with discrete optimization problems, Kennedy and Eberhart [26] developed a binary version of PSO. After that, many discrete versions of PSO [27-29] have been proposed. Recently, Qin et al. [28] proposed an algorithmic framework of discrete PSO (denoted by DPSO for short), and the application of DPSO to number partitioning problem has demonstrated the effectiveness of the proposed algorithm.

The basic idea of canonical PSO is that any particle moves close to the best of its neighbors and returns to the best position of itself so far. The DPSO follows the basic idea of canonical PSO. It uses one of the following equations to generate a new position for particle $i$ in the swarm:

$$
\begin{aligned}
& x^{i}=x^{i} \oplus\left(r_{1} \bullet\left(\tilde{x}^{i} \sim x^{i}\right)\right) \\
& x^{i}=x^{i} \oplus\left(r_{2} \bullet\left(\tilde{x}^{i N} \sim x^{i}\right)\right) \\
& x^{i}=x^{i} \oplus\left(r_{3} \bullet\left(x^{*} \sim x^{i}\right)\right)
\end{aligned}
$$

where $\tilde{x}^{i}$ and $\tilde{x}^{i N}$ are personal best position of particle $i$ and the neighborhood best position, respectively; $r_{1}, r_{2}$, and $r_{3}$ are three random numbers in $[0,1] ; x^{i}$ is chosen at random from the current swarm; and $\sim, \bullet$, and $\oplus$ are three operators, and their definitions are as follows.

Difference operator $(\sim)$ : given any positions $x$ and $y$, the difference of them, denoted by $x \sim y$, is a sequence of
least number of consecutive flip operators. Difference of two positions is used to act as velocity in the DPSO; that is, $v=$ $x \sim y$.

Product operator $(\bullet)$ : supposing that $\sigma$ is a real number and $v$ is a velocity (i.e., the difference of two positions), the product of them, denoted by $\sigma \bullet v$, is a subsequence of $v$ such that the length of this subsequence is $[\sigma[v)]$, where $|v|$ is the length of $v$.

Sum operator $(\oplus)$ : given a position $x$ and a velocity $v, x \oplus v$ starts with $x$ and flips all the variables in $v$ to obtain a new position.

Equations (2) and (3) try to make particle moves close to the best position of itself so far and the best of its neighbors, respectively. Equation (4) introduces a stochastic factor to avoid premature convergence of DPSO. In each iteration, exactly one of the three equations is employed to update a particle.

Inspired by the idea in [28], our PSO procedure employs the basic structure of DPSO [28] and redefines the operators of DPSO based on the specific structure of the max-cut problem. Supposing that $x=\left(x_{1}, \ldots, x_{n}\right)$ and $y=\left(y_{1}, \ldots, y_{n}\right)$ are two solutions of max-cut problem, we define $x \sim y=\{j \mid$ $\left.x_{j} \neq y_{j}, j \in\{1, \ldots, n\}\right\}$. It is used to determine the differences between $x$ and $y$. In our PSO procedure, the velocity $v$ is denoted as a set of variables, that is, $x \sim y$. Different from the definition of operator $\bullet$ in DPSO, our operation $\sigma \bullet v$ generates a variable subset of $v$ by removing each variable $j \in v$ from $v$ with a probability $\sigma$. This operator increases the exploration ability of our PSO procedure. The operation $x \oplus v$ generates a new solution. It starts from $x$ and flips all the variables in $v$.

In (3), particle $i$ tries to reduce the distance to the best of its neighbors $\tilde{x}^{i N}$. It is time consuming to update $\tilde{x}^{i N}$ for each particle $i$ in each generation, especially for large scale problems. In addition, the landscape analysis of max-bisection problem [30] shows that, in most cases, the distances between high quality solutions are very small. Their research result [30] indicates that the degree of similarity between $\tilde{x}^{i N}$ and the current best solution $x^{*}$ is very large. To speed up the search, each particle tries to move close to $x^{*}$. The search can concentrate fast around $x^{*}$. In our PSO procedure, (3) is replaced by

$$
x^{i}=x^{i} \oplus\left(r_{2} \bullet\left(x^{*} \sim x^{i}\right)\right)
$$

The pseudocode of our PSO procedure is given in Algorithm 2. For each solution $x^{i}$ in the population $\operatorname{Pop}(g)$, a new position is updated by (2), (5), and (4) with probabilities $\operatorname{prob}_{p}, \operatorname{prob}_{n}$, and $\operatorname{prob}_{r}$, respectively (lines (1)-(11)). We have $\operatorname{prob}_{p}+\operatorname{prob}_{n}+\operatorname{prob}_{r}=1$; that is, updating of a particle is influenced by exactly one of (2), (5), and (4). Then, the newly obtained position is further improved by a local search procedure (line (12)). We use a path relinking procedure, which will be described in Section 2.5, to intensify the search. And $\tilde{x}^{i}$ and $x^{*}$ are updated (line (13)).
2.3. EDA Procedure. EDAs produce offsprings through sampling according to a probability model. Probability models

```
Require: A population \(\operatorname{Pop}(g)=\left\{x^{1}, \ldots, x^{s}\right\}\).
Ensure: A new population \(\operatorname{Pop}^{\prime}(g)\).
(1) for each \(x^{i} \in \operatorname{Pop}(g)\) do
(2) Generate a random number \(\delta \in[0,1)\).
(3) if \(0 \leq \delta<\operatorname{prob}_{p}\) then
(4) Use (2) to generate a new position \(x^{i}\).
(5) end if
(6) if \(\operatorname{prob}_{p} \leq \delta<\operatorname{prob}_{p}+\) prob \(_{n}\) then
(7) Use (5) to generate a new position \(x^{i}\).
(8) end if
(9) if \(\operatorname{prob}_{p}+\) prob \(_{n} \leq \delta<1\) then
(10) Use (4) to generate a new position \(x^{i}\).
(11) end if
(12) \(x^{i}=L S\left(x^{i}\right)\).
(13) A path relinking procedure is executed to intensify the search.
(14) Update \(\bar{x}\) and \(x^{*}\).
(15) end for
(16) \(\operatorname{Pop}^{\prime}(g)=\operatorname{Pop}(g)\).
(17) return \(\operatorname{Pop}^{\prime}(g)\).
```

Algorithm 2: PSO procedure.
identify the remarkable features of promising candidate solutions from the population. A probability model has a great effect on the performance of EDA.

Notice that $x=\left(x_{1}, \ldots, x_{n}\right)$ and its symmetric solution $\bar{x}=\left(-x_{1}, \ldots,-x_{n}\right)$ correspond to the same partition of $V$. Since the solution space of the max-cut problem is symmetric, the traditional probability models used in other binary optimization problems can not be directly applied.

We propose a probability model according to the symmetric solution space of the max-cut problem. Our EDA procedure uses $(n-1)$-dimensional vector $p=\left(p_{2}, \ldots, p_{n}\right)$ to characterize the distribution of promising solutions in the search space, where $p_{j}(j \neq 1)$ is the probability of $x_{j}=x_{1}$.

At the beginning of the PSO-EDA, vector $p$ is initialized as $p=(0.5, \ldots, 0.5)$. The PSO-EDA performs the PSO procedure and EDA procedure alternately. After the PSO procedure, a new population $\operatorname{Pop}(g)$, which contains $s$ new local optimal solutions, is obtained. The EDA procedure identifies the best $N$ solutions in $\operatorname{Pop}(g)$, and the probability vector $p^{g-1}$ is updated according to the following equation:

$$
p_{j}^{g}=(1-\alpha) p_{j}^{g-1}+\alpha \frac{1}{N} \sum_{k=1}^{N}\left|\frac{x_{j}^{k}+x_{1}^{k}}{2}\right|, \quad j=2, \ldots, n
$$

where $p^{g}$ is the probability vector in the $g$ th generation, $x^{k}=$ $\left(x_{1}^{k}, \ldots, x_{n}^{k}\right)$ is the $k$ th individual of the best $N$ solutions in $\operatorname{Pop}(g)$, and $\alpha \in(0,1)$ is the learning speed. Since $x_{j}^{k} \in$ $\{1,-1\},\left|\left(x_{j}^{k}+x_{1}^{k}\right) / 2\right|$ is binary. If $x_{j}^{k}=x_{1}^{k}$, it holds $\mid\left(x_{j}^{k}+\right.$ $\left.x_{1}^{k}\right) / 2 \mid=1$; otherwise, we have $\left|\left(x_{j}^{k}+x_{1}^{k}\right) / 2\right|=0$.

Wu and Hao [30] concluded from their experimental tests that the degrees of similarity between high quality solutions are very large. The best $N$ solutions, which are selected to update $p^{g}$, may be very similar. It leads the EDA procedure to produce very similar new solutions. The range of the value
of probability $p_{j}^{g}$ is limited to an interval $\left\{p_{\min }, p_{\max }\right\}$ with the aim of avoiding search stagnation. More formally, the probability vector $p^{g}$ is reset as follows:

$$
p_{j}^{g}= \begin{cases}p_{\min } & \text { if } p_{j}^{g}<p_{\min } \\ p_{j}^{g} & \text { if } p_{\min } \leq p_{j}^{g} \leq p_{\max } \quad j=2, \ldots, n \\ p_{\max } & \text { if } p_{j}^{g}>p_{\max }\end{cases}
$$

In each generation of the PSO-EDA, EDA procedure generates new solutions via sampling according to the probability vector $p^{g}$. A new solution $x=\left(x_{1}, \ldots, x_{n}\right)$ is generated as follows. First, EDA procedure randomly generates $x_{1} \in$ $\{1,-1\}$. Then, for every $x_{j}, j \neq 1$, to be determined, a random number $\mu \in(0,1)$ is generated. Let $x_{j}=x_{1}$ if $\mu<p_{j}^{g}$; otherwise, let $x_{j}=-x_{1}$.

The pseudocode of EDA procedure is given in Algorithm 3. In the procedure, firstly we identify $N$ best solutions in population $\operatorname{Pop}(g)$ (line (1)). The probability vector $p^{g}$ is generated according to (6), as well as (7) in line (2). Then, $s$ new solutions are generated by the probability vector $p^{g}$, and they are further improved by local search procedure (lines (3)-(13)). A path relinking procedure is employed to intensify the search. Line (14) updates $\bar{x}^{i}$ and $x^{*}$ if a new better solution is found.
2.4. Local Search Procedure. Local search has been proven to be very helpful when incorporated in PSO and EDA [29, 31]. To enhance the exploitation ability, a local search procedure is adopted. It is a simple modification of the local search method (denoted by FMMB) [32] for the max-bisection problem. Experimental results show that the FMMB is very effective. The max-bisection problem consists in partitioning the vertices into two equally sized subsets so as to maximize

```
Require: A population \(\operatorname{Pop}(g)=\left\{x^{1}, \ldots, x^{s}\right\}\) a probability vector \(p^{g-1}=\left(p_{2}^{g-1}, \ldots, p_{n}^{g-1}\right)\).
Ensure: A new population \(\operatorname{Pop}^{\prime}(g)\).
(1) The \(N\) best solutions in \(\operatorname{Pop}(g)\) are identified.
(2) Use (6) and (7) to obtain the probability vector \(p^{g}\).
(3) for \(i=\{1, \ldots, s\}\) do
(4) Generate \(x_{1}^{i} \in\{1,-1\}\) at random.
(5) for \(j=\{2, \ldots, n\}\) do
(6) Generate \(\mu \in(0,1)\) at random.
\((7) \quad\) if \(\mu<p_{j}^{g}\) then
\((8) \quad\) Let \(x_{j}^{i}=x_{1}^{i}\).
(9) else
\(\begin{array}{ll}\text { Let } x_{j}^{i}=-x_{1}^{i} \\ (11) & \text { end if }\end{array}\)
(12) end for
(13) \(x^{i}=L S\left(x^{i}\right)\).
(14) A path relinking procedure is executed to intensify the search.
(15) Update \(\tilde{x}^{i}\) and \(x^{n}\).
(16) end for
(17) \(\operatorname{Pop}^{\prime}(g)=\operatorname{Pop}(g)\).
(18) return \(\operatorname{Pop}^{\prime}(g)\).
```

Algorithm 3: EDA procedure.

```
Require: An initial solution \(x^{0}\).
Ensure: An improved solution \(x^{\text {best }}\).
(1) \(x^{\text {best }}=x^{0}\), flag \(=1\).
(2) while flag \(=1\) do
(3) Let flag \(=0\), and \(F=\{1, \ldots, n\}\).
(4) Calculate gains \(g_{j}, j \in V\), according to (8).
(5) for \(k=\{0, \ldots, n / 10\}\) do
(6) Let \(g_{a}=\max \left\{g_{j}, j \in F\right\}\).
(7) Move vertex \(a\) from its current belonged subset \(V_{a}\) to the other subset \(V_{a}\). Let \(x^{i}=\left(x_{1}^{k}, \ldots,-x_{n}^{k}, \ldots, x_{n}^{k}\right)\).
(8) Let \(F=F-\{a\}\), and update the gains of the affected vertices.
(9) if \(f\left(x^{i}\right)>f\left(x^{\text {best }}\right)\) then
(10) Let \(x^{\text {best }}=x^{i}\), flag \(=1\).
(11) end if
(12) Let \(g_{b}=\max \left\{g_{j}, j \in F \cap V_{a}\right\}\).
(13) Move vertex \(b\) from its current belonged subset \(V_{a}\) to the other subset \(V_{c}\). Let \(x^{k+1}=\left(x_{1}^{t}, \ldots,-x_{b}^{t}, \ldots, x_{n}^{t}\right)\).
(14) Let \(F=F-\{b\}\), and update the gains of the affected vertices.
(15) if \(f\left(x^{k+1}\right)>f\left(x^{\text {best }}\right)\) then
(16) Let \(x^{\text {best }}=x^{k+1}\), flag \(=1\).
(17) end if
(18) end for
(19) end while
(20) return \(x^{\text {best }}\).
```

Algorithm 4: Local search procedure.
the sum of the weights of crossing edges. It is a special case of the max-cut problem.

The steps for our local search procedure are presented in Algorithm 4. The local search procedure performs passes repeatedly until a pass fails to generate a better solution. Each pass is described between lines (2) and (19). Let $x^{\text {best }}$ be the
current best solution found in a pass and let $F$ be the set of unlocked vertices. Suppose that $x^{0}$ is a starting solution and its corresponding partition is $\left(V_{1}, V_{2}\right)$. A pass progresses in epochs. At the beginning of a pass, all vertices are unlocked (i.e., are free to be moved). We move free vertices according to their gains. The gain $g_{j}$ of a vertex $j$ is the objective function

```
Require: An initiating solution \(x\) and the current best solution \(x^{+}\).
Ensure: \(x^{+}\).
(1) Calculate the distance \(d\left(x, x^{+}\right)\)according to (10).
(2) if \(d\left(x, x^{+}\right)>n / 2\) then
(3) Let \(x=\bar{x}\).
(4) end if
(5) Calculate gains \(g_{j}, j \in V\), according to (8).
(6) The difference set \(\Delta\left(x, x^{+}\right)\)is determined according to (9).
(7) while \(\Delta\left(x, x^{+}\right) \neq \varnothing\) do
(8) Let \(a=\max \left\{g_{j}, j \in V\right\}, x^{\prime}=\left(x_{1}, \ldots,-x_{a}, \ldots, x_{a}\right)\).
(9) if \(f\left(x^{\prime}\right)>f\left(x^{+}\right)\)then
(10) Let \(x^{*}=x^{\prime}\). Return \(x^{+}\).
(11) else
(12) Let \(b=\max \left\{g_{j}, j \in \Delta\left(x, x^{+}\right)\right\}\left(\right.\) Assume that \(\left.b \in V_{c}\right)\).
(13) Set \(x_{b}=-x_{b}, \Delta\left(x, x^{+}\right)=\Delta\left(x, x^{+}\right)-\{b\}\), and update the gains of affected vertices.
(14) if \(\Delta\left(x, x^{+}\right) \neq \varnothing\) then
(15) Let \(c=\max \left\{g_{j}, j \in \Delta\left(x, x^{+}\right) \cap V_{a}\right\}\).
(16) Set \(x_{c}=-x_{c}, \Delta\left(x, x^{+}\right)=\Delta\left(x, x^{+}\right)-\{c\}\), and update the gains of affected vertices.
(17) end if
(18) end if
(19) end while
(20) return \(x^{*}\).
```

Algorithm 5: Path relinking procedure.
value and would increase if vertex $j$ is moved from its current belonged subset to the other. More formally,

$$
g_{j}=\left\{\begin{array}{cl}
\sum_{\{j, k\} \in E, k \in V_{1}} w_{j k}-\sum_{\{j, k\} \in E, k \in V_{2}} w_{j k}, & j \in V_{1} \\
\sum_{\{j, k\} \in E, k \in V_{2}} w_{j k}-\sum_{\{j, k\} \in E, k \in V_{1}} w_{j k}, & j \in V_{2}
\end{array}\right.
$$

Line (4) calculates the gains of all free vertices according to (8). There are two steps in each epoch. An epoch consists of lines (6)-(17). Firstly, the local search procedure moves an unlocked vertex with the highest gain in $F$ from its current belonged subset (denoted by $V_{c}$ ) to the other subset (denoted by $V_{a}$ ). And the current moved vertex is not allowed to be moved again during this pass. Line (8) updates the gains of the affected vertices. Then, an unlocked vertex with the highest gain in $V_{a}$ is moved to $V_{c}$. It is locked in this pass. The gains of the affected vertices are updated. To speed up our local search procedure, a pass ends if $n / 10$ epochs have been performed. The best partition $x^{\text {best }}$ observed during the pass is returned. Then, another pass starts with $x^{0}=x^{\text {best }}$. The local search procedure terminates when a pass fails to find a better solution.
2.5. Path Relinking Procedure. Path relinking is originally introduced in [33]. It explores trajectories that connect initiating solutions and guiding solutions to find better solutions. Our path relinking procedure uses the current best solution $x^{*}$ as the guiding solution. Algorithm 5 presents the path relinking procedure in detail. Suppose that $x$ is an initiating solution, which is generated by the PSO procedure or the

EDA procedure. Given two solutions $x^{1}$ and $x^{2}$, the difference set $\Delta\left(x^{1}, x^{2}\right)$ between $x^{1}$ and $x^{2}$ is defined as

$$
\Delta\left(x^{1}, x^{2}\right)=\left\{j: x_{j}^{1} \neq x_{j}^{2}\right\}
$$

The distance $d\left(x^{1}, x^{2}\right)$ between $x^{1}$ and $x^{2}$ is defined as the number of flipping variables for transforming $x^{1}$ to $x^{2}$. More formally,

$$
d\left(x^{1}, x^{2}\right)=\sum_{j=1}^{n} \frac{\left|x_{j}^{1}-x_{j}^{2}\right|}{2}
$$

Notice that the solution space of the max-cut problem is symmetric; that is, $x$ and $\bar{x}=-\left(x_{1}, \ldots,-x_{a}\right)$ represent the same partition. In order to reduce the difference set and speed up the path relinking procedure, we set $x=\bar{x}$ when $d\left(x, x^{+}\right)>n / 2$. The gains of all vertices are calculated according to (8) in line (5). The difference set $\Delta\left(x, x^{+}\right)$is determined (line (6)). In each iteration, a vertex $a$ with the highest gain in $V$ is identified (line (8)). If flipping $x_{a}$ will result in finding a better solution than $x^{*}$, we let $x_{a}=-x_{a}$ and stop the path relinking procedure (line (10)). Otherwise, a vertex $b$ with the highest gain in $\Delta\left(x, x^{+}\right)$is identified (line (12)), and the vertex $b$ is moved from its current belonged subset $V_{c}$ to the other subset $V_{a}$; that is, $x_{b}$ is flipped. The gains of the affected vertices are then updated, and $b$ is deleted from $\Delta\left(x, x^{+}\right)$(line (13)). After that, vertex $c$ with the highest gain in $\Delta\left(x, x^{+}\right) \cap V_{a}$ is determined (line (15)). The gains of the affected vertices are updated, and $c$ is deleted from $\Delta\left(x, x^{+}\right)$(line (16)). The above process is repeated until a better solution is found or $\Delta\left(x, x^{+}\right)=\varnothing$.

Table I: Combinations of parameter values.
Table 2: Orthogonal array and average cut values.
2.6. Mutation Procedure. The PSO-EDA uses the personal best position $\tilde{x}^{i}(i=1, \ldots, s)$ and the current best solution $x^{*}$ found so far to guide the search. At the beginning of the search, the degrees of the similarity between $\tilde{x}^{i}$ and $x^{*}$ are relatively small, which guides the search to find good solutions quickly. However, with progress of the search, the degrees of the similarity between $\tilde{x}^{i}$ and $x^{*}$ become large. It makes the search to find a better solution hard.

To make the search retain in a long term, we apply a simple mutation procedure to $\tilde{x}^{i}$. It diversifies the search. The mutation procedure flips a variable with a probability $\kappa=0.2$. In other words, for every $\tilde{x}_{j}^{i}$, a random number $\mu \in(0,1)$ is generated. The mutation procedure set $\tilde{x}_{j}^{i}=-\tilde{x}_{j}^{i}$ if $\mu<\kappa$.

## 3. Computational Results and Analysis

In this section, we report the computational experiments to show the efficiency and effectiveness of the PSO-EDA. The PSO-EDA was programmed in C and the experiments were run on PC with AMD processor ( 3.4 GHz CPU and 4 GB RAM).
3.1. Test Instances and Parameter Settings. We use two sets of benchmark instances to test the PSO-EDA. They have been
used to test many algorithms for the max-cut problem and max-bisection problem in the last two decades. The first set is G-set graphs [34]. The second set is from [4]. The instances of the second set arise from Ising Spin glasses cubic lattice graphs.

There are several parameters in our proposed PSO-EDA. The values of the population size $s$ and the learning speed $\alpha$ and $N$ and $p_{\min }$ and $p_{\max }$ highly affect the performance of PSO-EDA. To investigate the influence of those parameters on the performance of PSO-EDA, we fixed Maxcount $=100$, $G_{\text {no }}=6, \operatorname{prob}_{p}=0.25, \operatorname{prob}_{n}=0.05$, and $\operatorname{prob}_{r}=0.7$ and implemented the Taguchi method of design of experiment (DOE) [31, 35] by using problem G59. Combinations of different values of those parameters are given in Table 1.

For each parameter combination, we run PSO-EDA 5 times independently. We use the orthogonal array $L_{16}\left(4^{4}\right)$ and the orthogonal array and the obtained average cut values and average CPU time (time) are listed in Table 2.

From Table 2, one can observe that the PSO-EDA with the third parameter combination (i.e., $s=10, \alpha=0.3, N=$ $3, p_{\min }=0.2$, and $p_{\max }=0.8$ ) performed better than other parameter combinations in terms of average solution quality and solution time. In the following experiments, the values of parameters in PSO-EDA are given in Table 3.

Table 3: Settings of parameters.

Table 4: Comparison of the results obtained by the GPSO-CDHNN, DHNN-EDA, THNN-EDA, and PSO-EDA on instances from the first set.
3.2. Comparison of the PSO-EDA with Existing PSO-Based and EDA-Based Algorithms. In this subsection, we compared PSO-EDA with three PSO-based and EDA-based algorithms, that is, a memetic algorithm with genetic particle swarm optimization and neural network (GPSO-CDHNN) [10], a discrete Hopfield network with estimation of distribution
algorithm (DHNN-EDA) [25], and tabu Hopfield neural network with estimation of distribution algorithm (THNNEDA) [9].

We have run PSO-EDA 10 times with parameters listed in Table 3 on some instances used in [9, 25]. Tables 4 and 5 list the best objective function value ( $f_{\text {best }}$ ), the average

Table 5: Comparison of the results obtained by the DHNN-EDA, THNN-EDA, and PSO-EDA on instances from the second set.
objective function value ( $f_{\text {avg }}$ ), standard deviation values (Std.), and average time (time) in seconds produced by the GPSO-CDHNN, DHNN-EDA, THNN-EDA, and PSO-EDA, respectively. The mark "-" means that the experimental result is not reported. The best objective function value for each selected instance obtained by these algorithms has been indicated in boldface in Tables 4 and 5. The average objective function value with italic indicates the best average objective function value obtained by all algorithms.

The detailed results of GPSO-CDHNN shown in Table 4 are taken from [10]. The data of DHNN-EDA and THNNEDA is from [9]. Both DHNN-EDA and THNN-EDA were terminated within the same run time, which is shown in the subcolumn "time" under the column "THNN-EDA." Note that GPSO-CDHNN was tested on DELL-PC (Pentium 4 2.80 GHz ), and DHNN-EDA and THNN-EDA were run on a PC (Pentium 42.9 GHz with 2.0 G of RAM). According to the CPU speed data from http://www.cpubenchmark.net/, their computers are 6.15 times slower than our computer. Considering the difference between their computers and our computer, we normalize the CPU times of GPSO-CDHNN, DHNN-EDA, and THNN-EDA by dividing them by 6.15 .

From Table 4, we observe that PSO-EDA is able to find better solutions compared to GPSO-CDHNN for 14 instances out of 15 selected instances from the first set. In addition, the average objective function values of PSO-EDA are better compared to GPSO-CDHNN for all tested instances from the first set. The CPU time of PSO-EDA is smaller than that of GPSO-CDHNN. These mean that PSO-EDA has a better performance than GPSO-CDHNN.

From Tables 4 and 5, we can see that the best objective function value and the average objective function value of PSO-EDA are much better than those of DHNN-EDA for all 24 considered instances from the first set, as well as 20 instances from the second set. The PSO-EDA takes less CPU time compared to DHNN-EDA for all tested instances, expect for G1, G2, and G3. Therefore, PSO-EDA significantly outperforms DHNN-EDA for these instances.

THNN-EDA and PSO-EDA found the best objective function values on 23 and 40 out of the total 44 tested instances, respectively. The average objective function value of PSOEDA is better compared to THNN-EDA for 13 instances from the first set, while it fails to match the average results of THNN-EDA for 6 instances from the first set. PSO-EDA is able to find better average results than THNN-EDA for all instances from the second set. The PSO-EDA takes less CPU time compared to THNN-EDA for all tested instances, expect for G1, G2, and G3. These observations reveal that PSO-EDA performs better than THNN-EDA.

From all the results mentioned above, we can conclude that the performance of PSO-EDA is much better than the existing PSO-based and EDA-based algorithms for the maxcut problem.
3.3. Comparison of the PSO-EDA with Other Metaheuristic Algorithms. In this subsection, the PSO-EDA is compared with several metaheuristic algorithms for the max-cut problem, including grasp based heuristic (GRASP-TS/PM) [6], path relinking based heuristic (PR2) [11], breakout local

Table 6: Comparison of the results obtained by the GRASP-TS/PM, PR2, BLS, TSHEA, and PSO-EDA on instances from the first set.

Table 6: Continued.

search (BLS) [12], and tabu search based hybrid evolutionary algorithm (TSHEA) [13]. To compare PSO-EDA with these state-of-the-art algorithms, the maximum generation Maxcount is increased to 2000. We run PSO-EDA 10 times. Tables 6 and 7 report the best known solutions (Best), the best values ( $f_{\text {best }}$ ), and average solution values ( $f_{\text {avg }}$ ) obtained by GRASP-TS/PM, PR2, BLS, TSHEA, and PSOEDA, respectively. Since GRASP-TS/PM and BLS do not report their results on the instances of the second set, we do not include comparisons with GRASP-TS/PM and BLS on the instances of the second set. The mark "-" in Tables 6 and 7 means that the experimental result is not reported. The subcolumn "gap" under the column "PSO-EDA" lists the deviation of the best solution value obtained by PSOEDA with respect to the best known solution value Best. The deviation is calculated as follows: $\left((\right.$ Best $\left.-f_{\text {best }}) / \mathrm{Best}) \times 100$.

Since GRASP-TS/PM, PR2, BLS, TSHEA, and PSO-EDA were coded on different programming languages and run on different hardware platforms, it is very difficult to make a completely fair comparison of the computing time. Therefore, similar to [13], we only compare algorithms based on the solution quality.

We can make the following observations on the results in Tables 6 and 7:
(1) Table 6 shows that GRASP-TS/PM, PR2, BLS, TSHEA, and PSO-EDA find the best known solutions on $25,36,48,54$, and 43 instances out of the first 54 small or medium instances from the first set, respectively. For 17 large instances from the first set, BLS and TSHEA find the best known solutions on

5 and 13 instances, respectively. The experimental results in Tables 6 and 7 show that BLS and TSHEA are the best performing algorithms.
(2) Compared with GRASP-TS/PM and PR2, PSO-EDA finds very competitive results on the first 54 small or medium instances from the first set. In terms of best solution quality and average solution quality, PSOEDA is better than PR2 on 15 large instances from the first set.

For 20 instances from the second set, in terms of best solution quality, PSO-EDA is better than PR2 on 9 instances and same as PR2 on 11 instances. In terms of average solution quality, PSO-EDA is better than PR2 on 15 instances, same as PR2 on 3 instances, and worse than PR on 2 instances.
(3) PSO-EDA finds the best known solutions on 62 instances out of total 91 instances. In addition to the other 29 instances, PSO-EDA can obtain the best solution with very small deviations to the best known solutions. The range of deviations is only from $0.01 \%$ to $0.47 \%$.
(4) For the large scale instances, the performance of PSOEDA is not stable. Two main reasons are as follows: (I) with the increase of the instance size, the number of the local optima increases rapidly and (II) the degree of similarity between high quality solutions is generally very large [30].

The above computational results show that the proposed algorithm is very effective for solving the max-cut problem.

Table 7: Comparison of the results obtained by the PR2, TSHEA, and PSO-EDA on instances from the second set.
## 4. Conclusions

We have presented an integrated method based on particle swarm optimization and estimation of distribution algorithm (PSO-EDA) for the max-cut problem. It utilized both the global information and local information. A fast local search procedure was employed to enhance the performance of PSO-EDA. In addition, a path relinking procedure was developed to intensify the search. These strategies achieve a good balance between intensification and diversification.

Two sets of benchmark instances were used to test the performance of PSO-EDA. The comparison of PSO-EDA with the counterpart algorithms in the literatures, including GPSO-CDHNN, DHNN-EDA, and THNN-EDA, shows that PSO-EDA significantly outperforms these algorithms in terms of solution quality and solution time. We also compared our PSO-EDA with other existing metaheuristic algorithms, including GRASP-TS/PM, PR2, BLS, and TSHEA. The computational results showed that the PSO-EDA is able to find high quality solutions on these tested instances. In future work, we look forward to apply this approach to other combinatorial optimization problems.

## Conflict of Interests

The authors declare that there is no conflict of interests regarding the publication of this paper.

## Acknowledgments

This research was supported partially by the National Natural Science Foundation of China under Grant 11301255 and the

Science and Technology Project of Minjiang University, China, under Grant MYK15005.

## Kindawi

Submit your manuscripts at http://www.hindawi.com
![img-3.jpeg](img-3.jpeg)

Advanced Computer
![img-4.jpeg](img-4.jpeg)

## Hindawi

Submit your manuscripts at http://www.hindawi.com
![img-5.jpeg](img-5.jpeg)

Hematoma Journal
Computer Games
![img-6.jpeg](img-6.jpeg)

Computational
![img-7.jpeg](img-7.jpeg)

Computational Intelligence and Neuroscience
![img-8.jpeg](img-8.jpeg)

Computational
![img-9.jpeg](img-9.jpeg)

Computational
![img-10.jpeg](img-10.jpeg)

Electrical and Computer Engineering