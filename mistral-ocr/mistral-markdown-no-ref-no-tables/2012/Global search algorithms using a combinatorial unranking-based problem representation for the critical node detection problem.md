# Global search algorithms using a combinatorial unranking-based problem representation for the critical node detection problem 

Mario Ventresca<br>Medical Operations Research Laboratory, Department of Mechanical and Industrial Engineering, University of Toronto, Toronto, Canada

## A R T I C L E I N F O

Available online 17 February 2012
Keywords:
Critical node detection
Complex networks
Random graph
Simulated annealing
Population-based incremental learning

## A B S T R A C T

In this paper the problem of critical node detection (CNDP) is approached using population-based incremental learning (an estimation of distribution algorithm) and simulated annealing optimization algorithms using a combinatorial unranking-based problem representation. This representation is space-efficient and alleviates the need for any repair mechanisms. CNDP is a very recently proposed problem that aims to identify a vertex set $V^{\prime} \subseteq V$ of $k>0$ nodes from a given graph $G=(V, E)$ such that $G\left(V \backslash V^{\prime}\right)$ has minimum pairwise connectivity. Numerous practical applications for this problem exist, including pandemic disease mitigation, computer security and anti-terrorism. In order to test the proposed heuristics 16 benchmark random graph structures are additionally proposed that utilize Erdos-Renyi, Watts-Strogatz, Forest Fire and Barabasi-Albert models. Each of these models presents different network characteristics, yielding variations in problem difficulty. The relative merits of the two proposed approaches are compared and it is found that the population-based incremental learning approach, using a windowed perturbation operator is able to outperform the proposed simulated annealing method.

## 1. Introduction

The critical node detection problem is $\Lambda 7^{3}$-complete and concerned with discovering a set of $k$ vertices $S \subseteq V$ of graph $G(V, E)$ whose removal will leave the graph with minimum pairwise connectivity [1]. As a consequence of sufficiently large $k$, the resulting graph $G^{\prime}=G\left(V^{\prime} S, E^{\prime}:\left\{\left(i, j\right): i, j j\left(V^{\prime} S\right)\right)\right.$ will have the maximum number of components, while simultaneously having the minimum variance in component sizes. In general, identification of critical nodes provide important information concerning the structural characteristics of the graph under consideration.

Let there exist a diffusive process acting upon the network, for instance pandemic disease spread or information transfer. Where an edge is present between two vertices $\left(i, j\right) \in E$, a path exists for the diffusive process to propagate through the network. By removing critical nodes we can limit the amount of spread over the entire network. Not surprisingly, CNDP has applications in network immunization where vaccination/quarantine of individuals is expensive. Existing approaches for vaccination in these circumstances focus on using properties of node centrality, however these are not optimal strategies [1]. Other applications include transportation engineering, protein-protein interaction networks [2], disease mitigation [3] and computer security [4,5], for example.

[^0]As stated above, the CNDP problem has only recently been proposed and therefore there does not exist a great variety of approaches to solving this problem. The original works [1,2,5] are based on heuristic algorithms and are shown to yield reasonable results. However, in [2] a simple genetic algorithm was proposed and shown to outperform the heuristic method with respect to solution quality. Another caveat of these approaches is the use of networks that contain less than 200 nodes; for networks with thousands of vertices the heuristic is too computationally expensive.

A further analysis of graph partitioning and critical node detection was performed in [6]. The work considers the concept of uncertain edges and describes the effects on community structure that result. Numerical experiments are performed to verify the theoretical analysis. The cardinality constrained critical node detection problem is proposed in [7]. This version extends CNDP by restricting the disconnected components to a given cardinality.

Most recently, Di Summa et al. [8] examined the case where $G$ is restricted to a tree structure and proved the $\Lambda 7^{3}$-completeness of the problem for non-unit edge costs. They also provide a polynomial time dynamic programming algorithm for solving the problem with unit edge costs. The dynamic programming solution is also applied to variants of the CNDP [9]. In [10] an integer linear programming model with non-polynomial number of constraints is given and branch and cut algorithms are proposed. This latter approach also requires significant computational resources for networks containing thousands of vertices.


[^0]:    E-mail address: mario.ventresca@utoronto.ca

In this paper we examine the efficacy of simulated annealing and population-based incremental learning for approximating solutions to the CNDP. Neither algorithm has been applied to this problem previously. Both approaches rely upon a perturbation operator for generating successive solutions, and we propose an efficient window-based procedure. Key to the relatively low computational cost of this approach is the proposed binary solution representation. By employing a combinatorial unranking algorithm as a mapping from the binary representation to a set of removed vertices, we eliminate the need for any repair mechanism. Often repairing solutions to enforce feasibility is computationally expensive and introduces undesirable bias into the results. Moreover, generation of binary strings is very efficient as are unranking algorithms. Fitness evaluation is accomplished via a depth-first search of $\mathcal{O}(|V|+|E|)$ and thus is also not a large burden on efficiency.

In order to test the results, 16 benchmark problems are additionally proposed. These problems have been generated based on Barabasi-Albert [11], Erdos-Renyi [12], Watts-Strogatz [13] and Forest Fire [14] complex network construction algorithms. Each type of graph presents different structural properties, leading to variations in problem difficulty. We present small (less than 1000 vertices) and medium-sized (less than 5000 vertices) graphs. Extremely large networks, with millions of nodes, will be considered in future works.

The remainder of this paper is organized as follows. Section 2 formally presents the critical node detection problem and a possible integer programming formulation. The algorithms and related implementation issues are then discussed in Section 3. Section 4 proposes 16 benchmark data instances which are subsequently used in Section 5 where experimental results are discussed. Conclusions are given in Section 6.

## 2. Critical node detection

In this section an integer program problem formulation for the critical node detection problem (CNDP) is given. We assume graph $G=(V, E)$ is undirected and unweighted, and has vertices $V$ and edges $E$. For subset $S \subseteq V$, the subgraph $G(S)$ has edge set $W=\{(i, j): i, j \in S\} \cap E$. A connected component of $G$ is a set of vertices such that all vertices in each set are mutually connected (reachable by some path), and no two vertices in different sets are connected. Given integer $k>0$, the goal of the CNDP is to determine
$\underset{S \subseteq V}{\operatorname{argmin}} \sum_{i, j \in(V, S)} u_{i j}(G(V, S))$
such that $|S| \leq k$, and where
$u_{i j}= \begin{cases}1 & \text { if } i, j \text { in same component of } G(V, S) \\ 0 & \text { otherwise. }\end{cases}$
The problem can be expressed as the following integer program [5]:
Minimize $\sum_{i, j \in V} u_{i j}$
subject to $\quad u_{i j}+v_{i}+v_{j} \geq 1 \quad \forall(i, j) \in E$

$$
\begin{aligned}
& u_{i j}+u_{j k}+u_{k i} \neq 2 \quad \forall(i, j, k) V \\
& \sum_{i \in V} v_{i} \leq k \\
& u_{i j} \in(0,1) \quad \forall i, j \in V \\
& v_{i} \in(0,1) \quad \forall i \in V
\end{aligned}
$$

Optimization of this objective function will result in a graph with minimum pair-wise connectivity. The first constraint (Eq. (4)) enforces the separation of vertices into different components. Eq. (5)
is concerned with a triangle inequality; if vertices $i, j$ and $j, k$ are in the same component, then $i$ and $k$ must also be in the same component. The final constraint, in Eq. (6), ensures the removal of no more than $k$ vertices.

Eq. (2) is a measure of the pairwise connectivity of a given (sub)graph, where $u_{i j}$ is a binary value equal to 1 iff $i$ and $j$ are in the same component of $G(V, S, W)$. Let $C$ be the set of all maximally connected components of $G(V, S, W)$, and $\sigma_{c}$ represent the size of component $c=\{1, \ldots,|C|\}$. Then, an alternative objective function to Eq. (3) is [5]:
$\frac{1}{2} \sum_{c \in C} \sigma_{c}\left(\sigma_{c}-1\right)$
Minimization of (9) will maximize the number of components while also minimizing the variance between components. Determining graph component sizes can be efficiently determined via a depthfirst search with complexity $\mathcal{O}(|V|+|E|)$ [15] and thus does not have great computational overhead.

As indicated in [1,5] the CNDP is related to the maximum $k$-cut problem (K-MAX-CUT) [16]. Specifically, K-MAX-CUT approximations would be useful if only the number of components is considered. However, this additional consideration increases the problem difficulty sufficiently that related approximations are not very useful. To the best of the author's knowledge, the application of stochastic search algorithms to this problem has not yet been investigated outside of preliminary work utilizing genetic algorithms [2].

## 3. Algorithms and methods

In this paper we employ an indirect binary problem representation that is mapped to a set of $k$ removed vertices. Specifically, we use an intermediate function $\phi:(0,1)^{m} \mapsto \mathbb{Z}^{*}$, to map an $m$ dimensional binary string to an integer, where a combinatorial unranking function will in turn map to a lexicographically ordered combination (i.e. $\psi: \mathbb{Z}^{*} \mapsto \mathbb{C}_{\langle V|, k}$, where $V$ is the vertex set and $k>0$ is user-defined). In this section the unranking function $\psi$ is described, followed by the solution representation and stochastic search algorithms.

### 3.1. Solution representation

The representation being searched is a straightforward binary string. This solution representation we have implemented completely alleviates the need for repair mechanisms or penalty functions, which are often computationally expensive. Our idea utilizes a combinatorial unranking method as an intermediate step between the binary problem representation (for the search) and a lexicographically ordered (i.e. ranked) set of solutions (i.e. unique sets of vertices). The entire decoding procedure has computational complexity $\mathcal{O}\left(\log _{2}|V|+|V|\right)=\mathcal{O}(|V|)$, as described below.

### 3.1.1. Unranking

An unranking algorithm will construct elements $a_{i}$ of the $\kappa$ th sequence $\left\langle a_{1}, \ldots, a_{i}, \ldots, a_{k}\right\rangle$, where $1 \leq a_{1}<\cdots<a_{i}<\cdots a_{k} \leq|V|$ and $1 \leq \kappa \leq \mathbb{C}_{\langle V|, k}$. That is, given a list of lexicographically ordered combinations and an integer $\kappa>0$, the algorithm will return the associated $\kappa$ th combination. Characterization of unranking algorithms is according to Refs. [17,18]:

1. linear ordering of elements and
2. algorithm applied to evaluate the binomial coefficient.

The linear ordering of elements used in this paper is simply according to the natural integer value. Computation of binomial

coefficients is described below. Further information on (un)ranking algorithms can be found in [18-25].

We implement a simple unranking algorithm from [23], although more complex algorithms exist (see above unranking references for examples). Firstly, a modified Pascal's Triangle is constructed ${ }^{1}$ as:
$P_{i, j}=\left[\begin{array}{cccccccc}0 & 0 & 0 & 0 & 0 & 0 & \cdots \\ 1 & 1 & 1 & 1 & 1 & \cdots & \\ 2 & 3 & 4 & 5 & \cdots & & \\ 3 & 6 & 10 & \cdots & & \\ 4 & 10 & \cdots & & & \\ 5 & \cdots & & & & \end{array}\right]$
The unranking method is presented in Algorithm 1, where ranks are assumed to be in decreasing lexicographic order. The $\kappa$-unranked combination, stored in object $R$, will be determined via a divide-and-conquer approach, where $|V|$ and $k$ are the number of vertices and subset size, respectively. At each iteration, line 6 is successful if $\kappa$ is within the current ranking bounds ( $q$ is the upper limit of this bound), and the $R_{k-m+1}$ element will have been determined. It has been proven that this approach requires $\mathcal{O}(|V|)$ time complexity and $\mathcal{O}(|V| k)$ space complexity [23].

Algorithm 1. The unranking algorithm.
Require: $0 \leq k<|V|, 0 \leq \kappa<\left(\begin{array}{l}V \\ k\end{array}\right)$
$1: t=|V|-k+1$
2: $m=k$
3: $R=$ empty list of size $k$
4: $q=P_{t, m}+P_{t+1, m-1}-\kappa-1$
5: repeat
6: if $P_{t, m} \leq q$ then
7: $\quad R_{k-m+1}=|V|-t-m+2$
8: $\quad q=q-P_{t, m}$
9: $\quad m=m-1$
10: else
11: $\quad t=t+1$
12: end if
13: until $m=0$
14: return $R$

It is important to note the existence of unranking algorithms having lower time and space complexity than the one utilized in this work (see $[23,18]$ for some examples). However, in this work we did not require more advanced methods and using doublevalued integer sizes allows for storage of maximum $\kappa$ value (i.e. number of combinations) of approximately $1.7977 \mathrm{e}+308$. If a larger number of combinations is required one can utilize cryptographic or other libraries capable of handling essentially arbitrarily large numbers.

### 3.1.2. Binary representation

Given the unranking approach defined above, we now reformulate the search problem to find the $\kappa^{*}$ that corresponds to the index of the optimal solution to (9). To motivate the decision of a binary problem representation, let us consider the lexicographically ordered list $L$ of combinations, as above, where $L(\kappa)$ is the $\kappa$ th element. Then due to the lexicographical ordering,

[^0](L( $\kappa-1), L(\kappa), L(\kappa+1)$ ) will have many elements in common. Thus, there exists sufficient information amongst adjacent elements to perform a search on $\kappa$. A binary representation is attractive because it allows for both small adjustments in the corresponding decimal value (through flipping right-side bits) as well as large jumps in the search space (by left-side bit flips), while preserving the solution structure. That is, both local and global search are possible, easily implemented and efficient operations.

With respect to critical node detection: CNDP will normally require the number of critical nodes to be significantly less than the number of vertices in the graph; i.e. $k \ll|V|$. Therefore, each $k$ subset will encode the vertices to be removed from graph $G$. That is, a solution represents the graph $G(V, S, W)$ for $|S| \leq k$. Each solution is composed of a bit string $Q=\left(0,1\right)^{m}$, where
$m=\left\lceil\log _{2}\left(\frac{n}{k}\right)\right\rceil$
It is likely that more integer values can be represented with this string than is required. This will occur when
$\max _{\kappa}<\left(\frac{n}{k}\right)$
Instead of computational overhead to check the non-existence of values greater than $\max _{\kappa}+1$, we simply perform a modulo operation where $ø$ returns the integer representation of the binary argument,
$\kappa=\phi(Q) \bmod \left(\frac{n}{k}\right)$
Consequently, each binary solution will be converted to an integer $\kappa$ that corresponds to some index
$0 \leq \kappa \leq\left(\frac{n}{k}\right)-1$
It must be noted that the modulo operation will potentially introduce some bias towards lower values of $\kappa$.

This binary representation also has the property of requiring less memory to store a solution since we require only sufficient bits to store a single number. Conversely, if utilizing a integer-based representation where $b$ bits are used to encode an integer, then $b k$ total bits are required to store $k$ vertices. So, if
$\left\lceil\log _{2}\left(\frac{|V|}{k}\right)\right\rceil<b k$
holds, then the binary representation is more efficient. For instance, using a 32-bit integer representation with $k=100$ and $|V|=1000$ we require $100 \times 32=3200$ bits using the integer-based representation, but only 465 bits for the binary-based version.

### 3.1.3. From binary solution to evaluation

Decoding a solution representation for subsequent evaluation is accomplished by the procedure outlined in Algorithm 2, and highlighted by the following order of operations:
$\underbrace{Q=(0,1)^{m}}_{\begin{array}{c}\text { Representation }\end{array}} \rightarrow \underbrace{\phi(Q)}_{\begin{array}{c}\text { Convert to index } \\ \text { Conver }\end{array}} \rightarrow \underbrace{\psi}_{\begin{array}{c}\text { Unranking: generate } S \\ \text { Evaluate G(V.S) }\end{array}} \rightarrow \underbrace{Z^{*}}_{\begin{array}{c}\text { Evaluate G(V.S) } \\ \text { Evaluate }\end{array}}$

In line 1 of Algorithm 2, $Q$ is converted from binary to integer value and represents the index $\kappa$ into the lexicographically ordered list of combinations. Using Algorithm 1 in line 2, the $\kappa$-combination is generated and stored as set $S \subseteq V$. The components of the graph $G(V, S)$ are subsequently determined in line 3 and the corresponding solution is evaluated in line 4 using Eq. (9).


[^0]:    ${ }^{1}$ More sophisticated methods exist that circumvent the need to store Pascal's Triangle. The method used here was chosen for simplicity. The choice of unranking method has no effect on the outcome of the proposed simulated annealing or population-based incremental learning approaches.

Algorithm 2. Decoding and evaluating a binary representation.
Require: $Q=\{0,1\}^{m}$, the binary representation
$: \kappa=\phi(Q)$
$: S=\operatorname{unrank}(\|V\|, k, \kappa)$
$: C=$ findComponents( $G: S)$
return $\frac{1}{2_{c=C}} \sigma_{c}\left(\sigma_{c}-1\right)$

### 3.2. Population-based incremental learning

Population-based incremental learning (PBIL) is an estimation of distribution algorithm [26] that combines elements from evolutionary computation and reinforcement learning [27]. At each iteration a number of samples is generated based on the current belief about the state of each variable in the solution where the global best found solution is used to update the belief of each variable. Values in the belief vector can be probabilistically mutated in order to promote exploration of the search space.

A $d \times c$-dimensional probability matrix $\mathbf{M} \simeq\left(m_{i j}\right)_{d \times c}$ is defined and corresponds to a probability distribution over possible values for each element ( $d$ is the problem dimensionality, each having $c$ variables). Learning in PBIL consists of utilizing the current $\mathbf{M}$ to generate a set $H_{1}$ of $k$ samples. These samples are evaluated according to the objective function for the given problem and the "best" sample $\mathbf{B}^{*} \simeq\left(b_{i j}\right)_{d \times c} \in\{0,1\}$ is maintained. Then, $\mathbf{M}$ is updated by increasing the probability of generating solutions similar to $\mathbf{B}^{*}$ according to
$\mathbf{M}_{t}=(1-\alpha) \mathbf{M}_{t-1}+\alpha \mathbf{B}^{*}$
where $0<\alpha<1$ represents the learning rate parameter and subscript $t \geq 1$ corresponds to the current iteration. Without prior information $\left(m_{i j}\right)=0.5$. Values in $\mathbf{M}$ can be perturbed once per iteration by adding or removing a small random value to a random subset of the values in $\mathbf{M}$.

The pseudocode for PBIL is presented in Algorithm 3. It assumes constants to control the maximum number of iterations and samples, $\omega$ and $k$, respectively. Additionally, in line 13 parameter $0<\gamma<1$ controls the amount that any $m_{i j}$ can be perturbed; according to constant $0<\beta<1$ in line 12 .

Algorithm 3. Population-based incremental learning.
1: \{Initialize probabilities \}
2: $\mathbf{M}_{0} \simeq\left(m_{i j}\right)=0.5$
3: for $t=1$ to $\omega$ do
4: \{Generate samples\}
5: $\quad H_{1}=$ generate_samples $\left(k, \mathbf{M}_{t-1}\right)$
6: \{Find best sample\}
7: $\mathbf{B}^{*}=$ select_best $\left(\left(\mathbf{B}^{*}\right) \cup H_{1}\right)$
8: Update $\mathbf{M}$
9: $\quad \mathbf{M}_{t}=(1-\alpha) \mathbf{M}_{t-1}+\alpha \mathbf{B}^{*}$
10: \{Mutate probability vector\}
11: for $i=0 \ldots d$ and $j=0 \ldots c$ do
12: if $\lambda i(0,1)<\beta$ then
13: $\quad m_{i j}=(1-\gamma) m_{i j}+\gamma \cdot \operatorname{random}(0$ or 1$)$
14: end if
15: end for
16: end for
In line $2, \mathbf{M} \simeq\left(m_{i j}\right)=0.5$ to reflect the lack of a priori information about the probability distribution of each variable. $k$ samples are generated using the using the current probability
matrix in line 5 and the best sample is retained in line 7. Matrix $\mathbf{M}$ is updated in line 9 using $\mathbf{B}^{*}$ to guide the direction of probability update. Finally, lines 11-15 probabilistically perform the mutation rule on elements of $\mathbf{M}$. Parameter settings used are $\alpha=0.05$, $\beta=0.25, \gamma=0.1$; determined by limited experimentation.

It has been shown in [28-30] that for a given discrete search space PBIL will converge to a local optima. Versions of PBIL for continuous spaces have also been explored [31-34], although only the discrete binary case is considered in this work.

### 3.3. Simulated annealing

Simulated annealing [35] is a popular Monte Carlo optimization algorithm used for discrete and continuous optimization. Inspiration for this approach was taken from the cooling/annealing properties of metals whereby a metal is heated and cooled into a low-energy stable state. The version of the algorithm used here is presented in Algorithm 4.

The function findBest() in line 6 will select the solution $\mathbf{H}$ having the best evaluation from those created by the generateNeighbors( $\mathbf{L}, k$ ) function, which generates $k>0$ neighbors of the local best solution $\mathbf{L}$. A neighbor is generated according to a heuristic that selects a subset of solution features and perturbs them slightly. We tested three different methods in this work, described in Section 5. At each iteration a number of neighbors are generated, and the global best solution found thus far is tracked in line 8 and the local solution is updated according to lines 12-15. Temperature update is performed in line 17. There exist a variety of cooling approaches, each decreasing the temperature according to a different schedule [36]. In this paper we use
$T_{t}=\alpha T_{t-1}$

Algorithm 4. Simulated annealing algorithm.
Require: $\omega>0, T_{0}>0, k>0$
$: \mathbf{B}^{*}=$ random solution
$: \mathbf{L}=\mathbf{B}^{*}$
$: T=T_{0}$
4: for $t=1$ to $\omega$ do
5: \{Generate $k$ neighbors\}
6: $\quad \mathbf{H}=$ findBest(generateNeighbors( $\mathbf{L}, k)$ )
7: \{Maintain global best solution\}
8: if (eval $(\mathbf{H})<$ eval $\left(\mathbf{B}^{*}\right)$ then
9: $\quad \mathbf{B}^{*}=\mathbf{H}$
10: end if
11: \{Update local best, or accept with probability\}
12: $\quad \Delta=$ eval $(\mathbf{H})-$ eval $(\mathbf{L})$
13: if $\Delta<0$ OR $e^{\Delta / T}>$ random $(0,1)$ then
14: $\quad \mathbf{L}=\mathbf{H}$
15: end if
16: \{Update temperature\}
17: $\quad T=$ updateTemperature $\left(T, T_{0}, t\right)$
18: end for

## 4. Benchmark problem instances

In order to evaluate the quality of the proposed approach, we propose 16 benchmark optimization instances based on ErdosRenyi, Barbasi-Albert, Watts-Strogatz and Forest Fire algorithms. Other graph generation algorithms could be used for future

instances, for example [37-41]. These data sets can be downloaded at http://individual.utoronto.ca/mventresca/cnd.html, or obtained via email from the author.

### 4.1. Edros-Renyi model

The general procedure for creating a random graph of this type is to start with $V$ vertices and $|E|=0$. Then, for every pair of vertices $i, j \in V$ an edge is added between them with probability $p$. This process defines a set of graphs $G_{V, p}$ having the same parameters $V, p$.

The degree distribution describes the probability of a vertex having degree $k$. For the Erdos-Renyi model [12] the Poisson distribution models this accurately
$p_{k}=\binom{|V|}{k} p^{k}(1-p)^{|V|-k} \approx \frac{z^{k} e^{-z}}{k!}$
where $z=p(|V|-1)$.
This random graph model has been of critical importance for the development of complex networks, but their structure has not been found to accurately model real world systems very well. The main difference lies in the Poisson degree distribution, whereas many real world networks follow a power law or lognormal degree distribution. Moreover, there is a lack of community structure that is often observed in real networks.

Fig. 1 shows an example Erdos-Renyi random graph with 176 vertices and 200 edges. While branches exist, the bulk of the edges are concentrated near the center of the graph where little discernible structure is observed. Another observation is the existence of multiple graph components. The Erdos-Renyi model does not enforce that the resultant graph structure have a path between all vertex pairs.

The benchmark, given in Table 1, includes four instances of the Erdos-Renyi model. They have been constructed with the properties given in Table 1. The smallest problem contains 235 vertices and 349 edges, while the largest has 2343 vertices and 3499 edges, respectively. Also given for each problem size is a set of three $k$-critical node values to search for.
![img-0.jpeg](img-0.jpeg)

Fig. 1. An Erdos-Renyi random graph with 235 vertices and 349 edges.

Table 1
The six Erdos-Renyi problems and associated $k$-critical nodes.

![img-1.jpeg](img-1.jpeg)

Fig. 2. An example Barabasi-Albert random graph with 1000 vertices.

### 4.2. Barabasi-Albert model

The Barabasi-Albert model [11] proposes that graph structure results from two processes, growth and preferential attachment. The former refers to the algorithm starting with a small set of $m_{0}$ vertices and grows the network as nodes and edges are added over time. The latter states that the probability of connecting to a node increases proportional to the current edge degree of the node; i.e. "the rich get richer".

The algorithm works as follows. The network starts with $m_{0}$ nodes and grows in stages. At each stage one vertex is added along with $m$ edges that link the new node to $m$ existing nodes according to the probability
$P\left(e_{\text {new, } v} \in E\right)=\frac{\operatorname{deg}(v)}{\sum_{w} \operatorname{deg}(w)}$
where $\operatorname{deg}(\cdot)$ returns the degree of a vertex and $v, w$ are the vertices already existing in the graph. As a result, nodes already having high degree will likely grow further. The degree distribution of this model [42] has been shown to have a power law tail with exponent 3
$p_{k} \approx k^{-3}$
for large $k$. The power law edge distribution has made this model an attractive basis for models of real networks.

Fig. 2 shows an example Barabasi-Albert graph with 1000 vertices. The "rich get richer" behavior is immediately obvious as a relatively small number of vertices act as hubs with higher connectivity. Contrasting with the Erdos-Renyi model, the entire graph forms a single component.

Table 2
The five Barabasi-Albert problems and associated $k$-critical nodes.

The benchmark suite contains five Barabasi-Albert networks, shown in Table 2. The smallest network contains 500 vertices and 499 edges, whereas the largest network contains 5000 vertices and 4999 edges. The $k$-critical node values are also given. Due to the "rich get richer" structure of these graphs, it is expected that they will prove easiest w.r.t. the CNDP.

### 4.3. Watts-Strogatz small world model

Small world networks were first popularized through Milgram's degrees of separation experiments [43]. These networks have path length $L \propto \log (|V|)$. That is, the graph has a low diameter and most nodes are reachable from any other in a relatively small number of hops. These networks also exhibit a high clustering coefficient, indicating the tendency of nodes to cluster together.

The Watts-Strogatz model [13] requires as input (a) the number of vertices, (b) the number of initial neighbors of each node, $b$ and (c) a probability $p$ of rewiring edges between nodes. The algorithm is straightforward. Initially start with a regular lattice and continually rewire edges randomly throughout the graph with probability $p$. During this graph generation process, the further apart the new edge ending is from its start the more reduction in graph diameter is observed. The best reduction ratio achievable is 0.5 at any step, and so after a small number of iterations the graph diameter will have been dramatically reduced. Except when the rewiring probability is zero, the degree distribution is Poissonian.

Fig. 3 shows an example Watts-Strogatz network with 250 vertices, initial neighborhood size of 5 and rewiring probability $p=0.05$. This particular model has a clustering coefficient of $\approx 0.47$ and a diameter of 6 . Given the density of connections and small-world property, these networks will require removal of a significant number of vertices in order to limit the size of the largest graph component.

Table 3 shows the four benchmark instances. Networks WS250 and WS1000 were generated using an initial neighbor value of 5 and 0.05 rewiring probability. Instance WS500 used an initial neighbor value of 3 and 0.05 rewiring probability, and WS1500 used a neighbor value of 3 and rewiring of 0.03 . The smallest network has 250 nodes and 1250 edges, and the largest graph has 1500 vertices and 4500 edges. The small-world property of these networks should result in a difficult optimization, or a very undesirable optimal solution (giant component is very large).

### 4.4. Forest Fire model

We also use the Forest Fire random graph model [14] to generate benchmark data. Like the Barabasi-Albert model, this is also a preferential attachment approach. However, this model reproduces heavy tailed degree distribution where the network diameter decreases over time. As a result, this model also follows a densification power-law whereby the network becomes dense according to a power-law rule. The name of the model is derived from the resemblance of its growth pattern to the manner in which forest fires spread.
![img-2.jpeg](img-2.jpeg)

Fig. 3. An example Watts-Strogatz small world model with 250 vertices.

Table 3
The four Watts-Strogatz problems and associated $k$-critical nodes.

![img-3.jpeg](img-3.jpeg)

Fig. 4. An example Forest Fire random graph model with forward probability $p=0.25$ and $r=0.2$ backward probability, respectively.

The algorithm to generate Forest Fire networks is also straightforward. The network starts with at random vertex $v \in V$ and uniformly selects some other vertex $w \in V$ and forms a connection

$(v, w)$. Then, select $x$ out-links and $y$ in-links of $w$, where $x$ and $y$ are the binomially distributed with means
$\frac{p}{1-p}$ and $\frac{r p}{1-r p}$
respectively, and $0<p, r<1$ are probabilities. Create links from $v$ to each of the $x+y$ edges and recursively repeat the process from the $x+y$ vertices.

An example Forest Fire graph with forward probability $p=0.25$ and backward probability $p=0.20$ is given in Fig. 4. This structure seems to be a mix of the Erdos-Renyi and Barabasi-Albert models. This model does have dense connection regions as well as long branches.

Table 4 gives the four Forest Fire problem instances in the benchmark. All networks were created with forward probability $p=0.25$ and backward probability 0.20 . The smallest network is made of only 250 vertices and 400 edges, and the largest is constructed of 2500 vertices and 4046 edges. The Forest Fire model should be harder for critical node detection than the Barabasi-Albert

Table 4
The five Forest-Fire problems and associated $k$-critical nodes.

Table 5
The average runtime (in seconds) of SA and PBIL for the 16 benchmark functions.

model as it contains more edges for the same sized graph (with the parameters used here).

## 5. Experimental results

In this section we explore the quality of the proposed algorithms on the 16 aforementioned problems. Both SA and PBIL will require a perturbation operator during the optimization. We experimented with three operators, and selected the best performing over all the 16 instances, without tuning parameters to work best for individual problems. The first subsection details these operators, but we do not show experimentation for them. Subsequent sections will utilize the operator that performed most admirably. In all cases, the algorithms were run for 30 trials with the number of samples per iteration, and run lengths determined by the number of vertices in the given graph, according to:
$\{$ samples, iterations $)(|V|)=\left\{\begin{array}{lll}(300,2500) & \text { if } & |V| \leq 500 \\ (400,4000) & \text { if } & |V| \in(500,1000) \\ (500,6000) & \text { if } & |V| \in(1000,2500) \\ (600,7500) & \text { if } & |V| \in(2500,5000)\end{array}\right.$
Other parameter settings for the algorithms are as follows: SA initial temperature $=\#$ iterations $\#|V|$ and temperature, $T$, update was performed every other iteration using $T_{1+1}=0.985 * T_{t}$. PBIL parameters were experimentally determined to be $\alpha=0.03$, $\beta=0.05$ and $\gamma=0.05$. All experiments were conducted on an Intel i7-2600 K (quad-core, eight threads 3.4 GHz ) machine with 8 GB RAM, with the algorithms being programmed using version 1.6 of Sun Java.

### 5.1. Sample generation and perturbation operator

We considered three types of perturbation/update operator, for SA and PBIL, respectively. The first method considers all dimensions of the solution representation and performs a perturbation with fixed probability $p$, which was tested to vary by 0.005 increments over the range $[0.005,0.10]$. This type of operator allows for maximum potential of search-space exploration at any given iteration. However, the number of dimensions could lead to longer convergence times, or difficulty escaping poor local optima.

Table 6
Summary results (mean, standard deviation, minimum and maximum) for SA and PBIL.
The second operator focuses on a contiguous subset $W \subseteq$ $(1, \ldots, m)$, i.e. an interval of indices in the representation, at each iteration. This tactic could allow for exploitation of the best known solution structure while exploring the best arrangement of a subset of the elements. The number of elements in $W$ is determined by
$|W|=\left\lfloor m^{-2.5}+\log _{2}(m)\right\rfloor$
where $m$ is according to Eq. (11). The SA algorithm uses a window size twice this size. During optimization this window is moved at each iteration from the lowermost bit towards the uppermost bit,
repeating once the uppermost bit is reached. The final operator is similar to the sliding window approach. Instead of the window, a random subset of size $|W|$ elements is selected. This approach is intended as a less biased version of the windowing technique. PBIL probabilities must always exist in the range $[0.5,0.95]$.

Generating solutions at each iteration has a significant impact on the solution quality as well. To fully utilize the search ability, we employ a strategy that uses the best known solution as a template background and only sample variations within $W$. Experimentation led to the use of the sliding window technique for the sampling phase of SA, with a probability $2 /|W|$ on each
![img-4.jpeg](img-4.jpeg)

Fig. 5. Box and whisker plots of results for the 16 benchmark problems.

element. That is, we expect two perturbations per sample. PBIL also utilized this windowed version, but the perturbation operator utilized the randomized window approach.

### 5.2. Running time

In this subsection we perform a comparison of the aforementioned SA and PBIL algorithms using the 16 benchmark graphs. The average runtime (in seconds) for each algorithm is given in Table 5. The overhead of PBIL's probability update step is evident, but as problem size increases the difference from SA is decreased. Given the size of the networks under consideration, the number of iterations and the number of samples per iteration, these are very promising results. For instance, solving the WS1500 problem will involve performing 6000 iterations each with 500 samples, thus 3,000,000 candidate solutions are generated. More traditional approaches have been limited to 1000s to determine a bounded solution to 50 or 100 node problems [10], or required many thousands of seconds to determine an optimal [1] for problems with less than 150 vertices. Moreover, the best existing heuristic [1] is also much less efficient than either the SA or PBIL approach presented here.

### 5.3. Comparing results

Unfortunately, comparison of our results to pre-existing approaches was not possible due to either limited RAM or exceptionally high computational demands, but we are hopeful that such a comparison will become feasible in the near future. A summary of our experimental results are presented in Table 6. We show the mean ( $\mu$ ), standard deviation ( $\sigma$ ), minimum and maximum obtained result for each algorithm, respectively. Corresponding box-and-whisker for each experiment, showing the distribution of results is given in Fig. 5.

For many of the proposed problems PBIL is more likely to yield a better quality outcome, although SA can produce reasonable results as well. Results obtained with PBIL tend to be more reliable, as indicated by the $\sigma$ values, than SA and the range of minimum/maximum values. The standard deviation also provides some minimal insight into the range of problem difficulty of the 16 benchmark instances. Problems with highly variable results may be more difficult to solve, whereas less variable results may indicate easier problems (or those with a difficult to discover optima). A full analysis of problem difficulty is beyond the scope of this paper, however, would form an interesting direction for future work.

Table 7
Comparing the effect size of the difference between SA and PBIL results.

The practical effect of the observed difference between SA and PBIL is estimated using Cohen's $d$-statistic, calculated as
$d=\frac{\bar{x}_{1}-\bar{x}_{2}}{s}$
where $\bar{x}_{1}$ and $\bar{x}_{2}$ are the means of two results with $n_{1}$ and $n_{2}$ observations in each group, respectively. The pooled standard deviation $s$ is calculated according to
$s=\sqrt{\frac{\left(n_{1}-1\right) s_{1}^{2}+\left(n_{2}-1\right) s_{2}^{2}}{n_{1}+n_{2}}}$
where $s_{1}$ and $s_{2}$ are the group 1 and group 2 standard deviations. Cohen's $d$-statistic can be interpreted using the following heuristic: the levels are $d>0.8,0.5<d<0.8,0.2<d<0.5$ and $<0.2$, which correspond to degrees of differences of large, medium, small and none, respectively. The results of this analysis are presented in Table 7. For all problems the PBIL approach significantly outperforms SA. A Kolmogorov-Smirnov test was also performed to determine whether the values could have been drawn from the same distribution. It was confirmed that this is

Table 8
Assessing the quality of the proposed algorithms versus a random sampling approach. Values for the $\mu$ and min columns are given as percentages.
Table 9
Summary results of the largest component achieved by the SA and PBIL algorithms.
highly unlikely as all $p$-values for this hypothesis were negligible $(<0.00001)$.

Given the lack of comparative algorithms, we will gauge the quality of the SA and PBIL algorithms versus the best result obtained by random sampling. While this is not a perfect measure, it provides insight into both the quality of the proposed methods, as well as the difficulty of the problems themselves. For each instance we generate the same number of random samples as one would have generated for all runs of SA or PBIL. For example, WS1500 generates 3,000,000 samples per run and thus we generate 30 times this number (recall, 30 trials are conducted for SA and PBIL). We retain the minimum, versus the mean, of the random sampling in order to be as critical as possible on the proposed algorithms.

Table 8 presents the results of our assessment. For each problem the minimum value found by random sampling is given, as well as the percentage difference of the mean and best results found by SA and PBIL (as given in Table 6). This difference is computed as a percentage according to
$100 \cdot \frac{\text { RANDOM }- \text { ALG }}{\text { RANDOM }}$
where $A L G$ is substituted for the mean or minimum result obtained by SA or PBIL. Negative values indicate the random sampler is more desirable. The larger this percentage the more desirable the outcome for the algorithm is.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Watts-Strogatz model (left) of 250 vertices, and after removal of 70 vertices (right). The high clustering coefficient and small diameter relate to very dense graphs that are difficult to compartmentalize.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Erdos-Reni random graph (left) with 235 vertices, and after removal of 50 vertices (right). The network has been segmented after removing critical nodes, but a very large component still remains.

The mean SA outcome turns out to be less desirable than the best RANDOM solution, for all but the Barabasi-Albert instances. These graphs are the simplest to solve, and as indicated above polynomial time algorithms exist to solve them optimally. Most instances the mean PBIL is more desirable than RANDOM, and cases where this is not true the difference is negligible. For both SA and PBIL the Forest Fire and Barabasi-Albert instances seem easiest to solve, whereas the Erdos-Renyi and Watts-Strogatz models seem significantly more difficult. As indicated previously, these graphs have characteristics such as small diameter or higher clustering coefficients that will likely make them more challenging to solve.

When comparing the best results obtained by each algorithm to the random approach we see that the pattern of problem difficulty noticed above remains. Also the results are, as expected,
more desirable than one would find using the purely random sampler.

### 5.4. Sample solution graphs

In this section sample graphs are shown to illustrate the type of solution represented by the above optimizations. This is done by presenting the graph before and after removal of the designated number of vertices. For space limitations, as well as visualization limitations we restrict the plots to networks having 250, 500 or 1000 vertices. Firstly, we present summary results concerning the size of the largest component in the graph.

Identification of the largest component is important in a number of practical applications. While not the explicit goal of the CNDP formulation, it is desirable to make the size of this
![img-7.jpeg](img-7.jpeg)

Fig. 8. Forest Fire network model of 250 vertices (left). Removal of 70 critical nodes leaves the network somewhat segmented (right).
![img-8.jpeg](img-8.jpeg)

Fig. 9. Barabasi-Albert preferential attachment model of 1000 vertices (left). After removing 75 critical nodes the network is significantly fragmented.

component as small as possible. Table 9 presents summary results for the largest component size for each problem instance and optimization algorithm. PBIL tends to yield the smaller component, which is expected from the above results. However, it is quite interesting to note the relatively small differences between the component size of these two approaches. Specifically, that even a largest component size difference of $5-10$ vertices ( $2-4 \mathrm{X}$ of a 250 vertex graph) can have such a large impact on the network as a whole.

Figs. 6-9 show typical results from optimization with PBIL. The WS250 problem before and after removal of 70 critical nodes is less dense, however, the network remains highly connected with the largest component size of 172 vertices. Significant reduction in this value will require a very large number of critical nodes, but nonetheless this is a very challenging problem to optimize. ER250 is also plotted (Fig. 7) before and after removal of 50 vertices. The network is characteristically random with respect to the connection structure and has a largest component size of 119, approximately half of the original network size. Fig. 8 shows the Forest Fire model with 250 vertices. Fifty critical nodes are identified and removed, with the remaining largest component having only 39 vertices. Finally, in Fig. 9 a Barabasi-Albert model with 1000 vertices and 75 critical nodes is shown. The high degree of segmentation is expected as these models are tree-like and shown to be simple to solve [9].

## 6. Conclusions and possible future work

This paper proposed simulated annealing and populationbased incremental learning approaches for attaining solutions to the critical node detection problem. Neither method had been previously applied in this context previously. A sliding windowbased perturbation operator was designed, which employed an efficient unranking-based problem representation and shown to yield quality results. An important additional benefit of this representation is the alleviation of any repair mechanism.

In order to assess the quality of the algorithms 16 benchmark problem instances were also proposed. These problems are created from Erdos-Renyi, Barabasi-Albert, Watts-Strogatz and Forest Fire complex network models and represent varying degrees of difficulty for an optimization algorithm. Additionally, their relatively large size (compared to previous problem instances of less than 250 vertices) make efficient computation necessary. Our statistical analyses reveals that the PBIL-based algorithm is superior to SA, for these problems.

Future works include creating larger benchmark problems, on the order of hundreds of thousands or millions of vertices. The representation presented here could be used for these extremely large problems as our representation scales logarithmically with respect to the number of vertices. That is, we use a compressed representation and this would therefore have a smaller search space at large networks than otherwise would be required. However, further theoretical and practical study of the solution representation is required. Other directions for future endeavors also include using other network models and heuristics.

## Acknowledgements

The author would like to thank the anonymous reviewers for their constructive input.
