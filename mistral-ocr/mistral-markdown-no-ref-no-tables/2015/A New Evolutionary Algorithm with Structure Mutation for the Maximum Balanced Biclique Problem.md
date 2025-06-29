# A New Evolutionary Algorithm with Structure Mutation for the Maximum Balanced Biclique Problem 

Bo Yuan, Bin Li, Member, IEEE, Huanhuan Chen, Member, IEEE, and Xin Yao, Fellow, IEEE


#### Abstract

The maximum balanced biclique problem (MBBP), an NP-hard combinatorial optimization problem, has been attracting more attention in recent years. Existing node-deletion-based algorithms usually fail to find high-quality solutions due to their easy stagnation in local optima, especially when the scale of the problem grows large. In this paper, a new algorithm for the MBBP, evolutionary algorithm with structure mutation (EA/SM), is proposed. In the EA/SM framework, local search complemented with a repair-assisted restart process is adopted. A new mutation operator, SM, is proposed to enhance the exploration during the local search process. The SM can change the structure of solutions dynamically while keeping their size (fitness) and the feasibility unchanged. It implements a kind of large mutation in the structure space of MBBP to help the algorithm escape from local optima. An MBBP-specific local search operator is designed to improve the quality of solutions efficiently; besides, a new repair-assisted restart process is introduced, in which the Marchiori's heuristic repair is modified to repair every new solution reinitialized by an estimation of distribution algorithm (EDA)-like process. The proposed algorithm is evaluated on a large set of benchmark graphs with various scales and densities. Experimental results show that: 1) EA/SM produces significantly better results than the state-of-the-art heuristic algorithms; 2) it also outperforms a repair-based EDA and a repair-based genetic algorithm on all benchmark graphs; and 3) the advantages of EA/SM are mainly due to the introduction of the new SM operator and the new repair-assisted restart process.


Manuscript received January 17, 2014; revised May 13, 2014 and July 23, 2014; accepted July 24, 2014. Date of publication August 14, 2014; date of current version April 13, 2015. This work was supported in part by the National Natural Science Foundation of China under Grant 61071024, Grant 61331015, Grant 61329302, Grant 61175065, Grant 61203292, and Grant 61311130140, in part by the European Union 7th Framework Program under Grant 247619 and Grant 257906, in part by the National Natural Science Foundation of Anhui Province under Grant 1108085J16, and in part by EPSRC under Grant EP/I010297/J. The work of X. Yao was supported by a Royal Society Wolfson Research Merit Award. The work of H. Chen was supported by the One Thousand Young Talents Program. This paper was recommended by Associate Editor K. C. Tan.
B. Yuan is with the USTC-Birmingham Joint Research Institute in Intelligent Computation and Its Applications, University of Science and Technology of China, Hefei 230027, China (e-mail: yuanbo@ustc.edu.cn).
H. Chen and X. Yao are with the USTC-Birmingham Joint Research Institute in Intelligent Computation and Its Applications, University of Science and Technology of China, Hefei 230027, China, and also with the Centre of Excellence for Research in Computational Intelligence and Applications, School of Computer Science, University of Birmingham, Birmingham B15 2TT, U.K. (e-mail: hehen@ustc.edu.cn; x.yao@cs.bham.ac.uk).
B. Li is with the USTC-Birmingham Joint Research Institute in Intelligent Computation and Its Applications, University of Science and Technology of China, Hefei 230027, China, and also with the CAS Key Laboratory of Technology in Geo-spatial Information Processing and Application System, University of Science and Technology of China, Hefei 230027, China (e-mail: bidi@ustc.edu.cn).

Digital Object Identifier 10.1109/TCYB.2014.2343966

Index Terms-Estimation of distribution algorithm, evolutionary algorithms, local search, maximum balanced biclique problem (MBBP), structure mutation.

## I. INTRODUCTION

ABIPARTITE graph $G(U, V, E)$ is a graph whose nodes can be divided into two disjoint sets $U$ and $V$ such that every edge connects one node in $U$ to one in $V$, and $E$ denotes the edges of the graph. A balanced bipartite graph $G(U, V$, $E)$ is a bipartite graph in which the both disjoint node sets are of the same cardinality, having $|U|=|V|=n$. A biclique $B\left(U^{b}, V^{b}, E^{b}\right)$ is a subgraph of $G$ that for each pair of nodes $u \in U^{b}$ and $v \in V^{b}$, having $(u, v) \in E^{b}$. If $\left|U^{b}\right|=\left|V^{b}\right|=k$, we call $B$ a balanced biclique of size $k$. The maximum balanced biclique problem (MBBP) is defined as finding a balanced biclique with the largest size $k$ in a balanced bipartite graph, that is the cardinality of $U^{b}$ or $V^{b}\left(\left|U^{b}\right|=\left|V^{b}\right|\right)$ should be maximized.

The MBBP (also referred to as the maximum balanced complete bipartite subgraph) was stated to be NP-hard in [1] (problem GT24), while the other nice NP-hardness proofs for this problem were presented in [2] and [3]. It is one of the few problems for which we still have neither a hardness of approximation result, nor a good approximation algorithm. A theoretical estimation of the boundary of $k$ was given in [4], that is $k(n) \leq k \leq 2 k(n)$ with high probability (for sufficiently large $n$ ), where $k(n)=\log n / \log (1 / p), 0<p<1$ is the probability that a particular edge exists in $G$. Recently, the MBBP has been proven to be even hard to approximate within a factor of $2^{\theta}, \theta=(\log n)^{\delta}$ for some $\delta>0$ [5]. So it seems to be impossible to have an exact polynomial time algorithm for the MBBP, and approximation of large biclique is also hard.

Meanwhile, the MBBP is closely related to many important real-life applications, such as biclustering of gene expression data in computational biology [6], PLA-folding in VLSI theory [7], and newly emerged applications in nanoelectronic system design [8]-[11], where the MBBP problem is used to model a promising defect-tolerant design flow that extracts the maximum defect-free subcrossbar (balanced biclique) within the original defective nano-crossbar (balanced bipartite graph).

Although the MBBP has been attracting more and more attention in recent years, few effective algorithms have been presented for it due to its NP-hardness. Instead of finding the maximum balanced biclique in $G$, the problem can be

transformed into a decision (yes or no) problem: does $G$ have a biclique of size $k \times k$ ? Since it has been proven that it would also take exponential time for an exact algorithm [11] to solve such decision problem, the time for graphs of size $n=64$ or larger would be completely intractable. If the constraint of being balanced was removed, the MBBP problem would be solvable in polynomial time [12]. However, the results obtained in this way were poor [9], because most of the bicliques generated by the polynomial time algorithm without the balance constraint were highly unbalanced. Given a bipartite graph with $2 n$ nodes and $m$ edges, the size of the largest (maximum) balanced biclique that is theoretically guaranteed to exist is $\log 2 n / \log \left(8 m^{2} / m\right)$ [13]. An efficient algorithm was proposed in [13] to approach such a theoretical size. It can only find a subgraph of logarithmic size even in a dense graph, e.g., the graph models of crossbar nano-architectures [8].
Recently, a class of node-deletion-based heuristic algorithms get a lot of attention [8], [9], [14], [15], which convert the MBBP into the maximum balanced independent set problem in the complement graph, which is usually sparse because the original bipartite subgraph is dense, e.g., the graph models of crossbar nano-architectures. To guarantee the outputted biclique to be almost balanced $\left(-1 \leq\left|U^{b}\right|-\left|V^{b}\right| \leq 1\right)$, the algorithms remove the nodes alternately from $U$ and $V$. The heuristic in [8] was to remove nodes with the maximum degree. The heuristic in [9] (the most effective algorithm so far) was to remove the node in one partition that was adjacent to the maximum number of minimum degree nodes in the other partition. Therefore in brief, to achieve the maximum balanced biclique, the heuristic in [8] tried to reduce the number of edges in the graph, while the heuristic in [9] tried to reduce the degree of the least degree nodes in a partition. The heuristics in [14] and [15] tried to improve the performance of the node-deletion-based algorithms by combining the two heuristics in [8] and [9], which could obtain results as good as that of [9] while with much lower time complexity. The heuristic in [14] was to remove the node with the maximum degree in one partition that was adjacent to the given minimum degree node in the other partition, and it was speeded up significantly in [15] by considerably reducing the number of major loops. So far, no node-deletion-based heuristic algorithm is effective enough for the MBBP, new techniques have to be designed and investigated.

It has been shown by many works that the hybrids of evolutionary algorithms (EAs) and problem-specific local search operators are effective methods for combinatorial optimization problems [16]. Most of the previous hybrid EAs adopted the paradigm in which EAs played the role of the global search, while local search operators were introduced to enhance the efficiency of the hybrid algorithms. In [17], a different paradigm was proposed with the algorithm R-EVO, in which fine-grained local search strategy was complemented by an EA (EDA). The difference lies in that the local search operator provides the most contribution to the quality improvement of solutions, while the EDA plays a complementary role that reinitializes the solutions when the local search process stagnates. Experimental results on the maximum clique
problems (MCPs) [18], another NP-hard problem, showed that such paradigm could produce significantly better solutions than the conventional EAs [19], [20]. For other complex combinatorial optimization problems with more constraints, e.g., the MBBP, the effectiveness of the paradigm still need to be improved to meet the harsh challenges brought by real-world applications.

By going through the procedure of R-EVO [17], it can be seen that the most computation resource is consumed by the local search process, which is the main force for convergence. No technique is considered to keep, to some degree, the algorithm's capability of exploration during the search process. The exploration is performed via a reinitialization process only when the local search process is stagnated. We try to improve the performance of the algorithm by introducing better exploration techniques to complement the local search process. In more details, a problem-specific mutation operator, structure mutation (SM), is proposed to enhance the exploration of the algorithm during the search process. Besides, a new local search operator utilizing the domain knowledge is presented to accelerate the quality improvement of solutions, and a repair-assisted restart process is implemented to utilize the good knowledge gained from previous local search process. Consequently, an effective evolutionary algorithm with structure mutation (EA/SM) for the MBBP is proposed.

The main contributions of this paper can be summarized as follows.

1) Fast Local Search: The fast local search operator considers the given current solution (biclique) as a start point and modifies the solution step-by-step through alternating between expansion and corrosion on the biclique. Specifically, the local search operator adds/drops one node on/from the current solution while keeping the solution feasible.
2) Structure Mutation: Solutions got by the fast local search will be reprocessed by the SM, which changes the structure of the current biclique dynamically while keeping the size (fitness value) and feasibility of the biclique unchanged. The SM is expected to implement a kind of large mutation in the solution space, which increases the possibility of finding a new search area for the following local search process, therefore enhances the capability of EA/SM to jump out of local optima.
3) Repair-Assisted Restart:
a) Probability-Model-Based Sampling: Restart process will be invoked only when the local search process cannot improve the quality of the current solution for a number of iterations. To obtain good efficiency, each new solution is reinitialized by sampling the search space according to a probability model $P$ updated with better solutions in the previous local search process.
b) Modified Marchiori's Heuristic Repair: Since the reinitialized solution is prone to be infeasible, to repair it effectively, Marchiori's heuristic repair operator [19] (proposed for the MCP [18]) is modified and applied on every reinitialized solution to generate a feasible solution.

## Algorithm 1 EA/SM $(G)$

1: $B_{i} \leftarrow \operatorname{zeros}(1,2 n) ; t b_{i} \leftarrow 0 ; t r_{i} \leftarrow 0 ; k b e s t_{i} \leftarrow 0 ; i=1$, $2, \ldots, N$
2: $p_{i} \leftarrow 0.5 ; i=1,2, \ldots, 2 n$
3: $t \leftarrow 0$;
4: Repeat
5: $t \leftarrow t+1$;
6: $i=1: N$
7: $B_{i} \leftarrow$ Fast Local Search $\left(B_{i}\right)$;
8: $B_{i} \leftarrow$ Structure Mutation $\left(B_{i}\right)$;
9: If $k_{i}>k b e s t_{i}$
10: $k b e s t_{i}=k_{i} ; t b_{i}=t$;
11: end
12: If $t-\max \left\{t b_{i}, t r_{i}\right\}>A / /$ Restart
13: $B_{i} \leftarrow$ Sampling $(P)$;
14: If $B_{i}$ is infeasible
15: $B_{i} \leftarrow$ Heuristic Repair $\left(B_{i}\right)$;
16: end
17: $t r_{i}=t$;
18: end
19: end
20: Update $P$ according to (5);
21: until maximum iteration reached

The rest of this paper is organized as follows. The problem formulation is given in detail in Section II. Section III introduces the framework of EA/SM for the MBBP and its main components. Experimental studies and comparisons are given in Section IV. Section V concludes the paper.

## II. Problem Formulation

Refer to the description of the MBBP in Section I, we advance formulized definition of the MBBP for the first time. Given an balanced bipartite graph $G(U, V, E)$ as shown in Fig. 1, a subgraph $B\left(U^{b}, V^{b}, E^{b}\right)$ of $G$ (the dark dots) can be represented by a $2 n$-D 0-1 vector, $B=\left\{b_{1}, b_{2}, \ldots, b_{n} ; b_{n+1}\right.$, $\left.b_{n+2}, \ldots, b_{2 n}\right\} \in\left\{0,1\right\}^{2 n}$, where $b_{i}=1$ if and only if node $i$ is in $B, b_{i}=0$ otherwise, the first $n$ values represent the nodes in $U$, while the last $n$ values represent the nodes in $V$. Then, the MBBP can be defined as follows:

$$
\begin{aligned}
\max : k(B) & =\min \left(\left|U^{b}\right|,\left|V^{b}\right|\right) \\
\text { s.t.: } & \left|E^{b}\right|=\left|U^{b}\right| \cdot\left|V^{b}\right| \\
\text { where } & \left|U^{b}\right|=\Sigma b_{i}, 1 \leq i \leq n \quad \text { and } \\
& \left|V^{b}\right|=\Sigma b_{j}, n+1 \leq j \leq 2 n
\end{aligned}
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. Balanced bipartite graph $G(U, V, E)$ and its subgraph $B\left(U^{b}, V^{b}, E^{b}\right)$, where $B=\{0,1,1,0 ; 1,0,0,1\}$.

The object function (1) is to maximize the smaller cardinalities of the two node set $\left(U^{b}\right.$ and $\left.V^{b}\right)$. The constraint (2) is used to ensure that the subgraph $B$ to be a biclique (or a complete bipartite subgraph), that is, for every $u \in U^{b}$ and $v \in V^{b}$, the edge $(u, v) \in E^{b}$. It seems that a balanced biclique could possibly be obtained without considering balance constraint. But including the balance constraint in the quality evaluation of solutions definitely may help to improve the performance of the EAs. In order to obtain better performance, all the effective algorithms for the MBBP generally keep the constraint of being balanced at the same time
s.t.: $-1 \leq\left|U^{b}\right|-\left|V^{b}\right| \leq 1$.

The constraint (4) is used to ensure that the subgraph $B$ is almost balanced. In this paper, both constraints (2) and (4) are considered simultaneously.

## III. EA/SM FOR MBBP

## A. Representation and Fitness

Refer to the problem formulation at the beginning of Section II, a subgraph $B$ of $G$ can be encoded as a $2 n$-D 0-1 string $B=\left\{b_{1}, b_{2}, \ldots, b_{2 n}\right\} \in\{0,1\}^{2 n}$. The fitness of $B$ is defined as its size $k$ [objective function (1)] if $B$ represents an almost balanced biclique [(2) and (4) are satisfied simultaneously]. Since each initialized solution will be repaired, there is no need to define fitness values for infeasible solutions.

## B. EA/SM Algorithm

The framework of EA/SM algorithm is similar to that of R-EVO [17], where a fine-grained local search strategy is complemented by an EDA-like restart process. R-EVO was originally designed for the MCP, so it cannot be applied directly on the MBBP. New effective MBBP-specific operators need to be designed to tackle the MBBP. Besides, by investigating the procedure of R-EVO, one can find that there is still much room for improvement. Examples are as follows.

1) In R-EVO, the exploration capability of the algorithm is not seriously considered enough. During the local search process, separated greedy local searches of individuals take all the computational resource. The global search is conducted only when the local search process stagnates and the algorithm enters the restart process. An EDAlike restart process is used to reinitialize the solution

Algorithm 2 Fast Local Search $(B)$

```
    // Add a node
    If \(U P A \neq \phi\) and \(V P A \neq \phi\)
    If \(\left|U^{b}\right|<\left|V^{b}\right|\)
    pick \(k \in U P A\); return \(B \cup\{k\}\); end
    If \(\left|U^{b}\right|>\left|V^{b}\right|\)
    pick \(k \in V P A\); return \(B \cup\{k\}\); end
    If \(\left|U^{b}\right|=|V^{b}|\)
    pick \(k \in U P A\) or \(k \in V P A\); return \(B \cup\{k\}\); end
    end
    If \(U P A \neq \phi\) and \(V P A=\phi\) and \(\left|U^{b}\right| \leq\left|V^{b}\right|\)
    pick \(k \in U P A\); return \(B \cup\{k\}\); end
    If \(U P A=\phi\) and \(V P A \neq \phi\) and \(\left|U^{b}\right| \geq\left|V^{b}\right|\)
    pick \(k \in V P A\); return \(B \cup\{k\}\); end
    // or Drop a node
    If \(\left|U^{b}\right| \neq \phi\) and \(\left|V^{b}\right| \neq \phi\)
    If \(\left|U^{b}\right|>\left|V^{b}\right|\)
    pick \(k \in U^{b}\); return \(B /\{k\} ;\) end
    If \(\left|U^{b}\right|<\left|V^{b}\right|\)
    pick \(k \in V^{b}\); return \(B /\{k\} ;\) end
    If \(\left|U^{b}\right|=\left|V^{b}\right|\)
    pick \(k \in U^{b}\) or \(k \in V^{b}\); return \(B /\{k\} ;\) end
    end
    If \(\left|U^{b}\right| \neq \phi\) and \(\left|V^{b}\right|=\phi\)
    pick \(k \in U^{b}\); return \(B /\{k\} ;\) end
    If \(\left|U^{b}\right|= \phi\) and \(\left|V^{b}\right| \neq \phi\)
    pick \(k \in V^{b}\); return \(B /\{k\} ;\) end
```

according to a probability model. Since the probability model is trained with the better solutions obtained in the local search process, it is reasonable to expect that the probability model would converge quickly when the local search is effective. Therefore, good exploration ability of the algorithm could not be expected in the restart process.
2) In R-EVO, in the EDA-like restart process, each new solution is generated in a greedy and tough fashion, where candidate nodes at every step are selected not only with probability proportional to the probability model describing the promising area of solution space, but also checking the feasibility of the solution. That means if the feasibility checking of one node generated according the probability model is negative, the node has to be dropped to meet the feasibility constraint. This way of new solution reinitialization would limit the efficiency and effectiveness of the EDA-like process dramatically.
In EA/SM, a well-crafted structure mutation operator is proposed to accompany the local search operator to increase the exploration capability of the algorithm during the search process; a MBBP-specific fast local search operator is presented to accelerate the solution quality improvement (toward suboptima); a new repair-assisted restart process is proposed, in
which, each new solution is firstly generated by sampling the search space according to the knowledge (probability model) gained from previous search process, then it is repaired in whole if it violates the constraints. A modified Marchiori's heuristic repair [19] is presented to repair the new reinitialized solutions to be feasible ones. The pseudo-code of EA/SM for MBBP is shown in Algorithm 1.

At the initialization stage, step $1-3$, a pool of solutions $B$ is initialized with all variables set to be 0 , and the probability model $P$ is initialized with all variables set to be 0.5 , which expresses a uniform distribution of sampling probability in the solution space.

Each iteration consists of two processes: local search process and restart process. In the local search process, a fast local search is conducted on current solution $B_{i}$, which adds or drops nodes one by one from the current biclique represented by $B_{i}$. SM is conducted consequently, which changes the adjacency attributes of the nodes in the current biclique represented by $B_{i}$.

When the quality of $B_{i}$ cannot be improved for $A$ iterations (step 12), the restart process is invoked. First, new solution is sampled according to the probability model $P$, then, the modified Marchiori's heuristic repair operator is applied to the newly generated solution to guarantee the reinitialized one is feasible. At the end of each iteration, the probability model $P$ is updated [according to the formula (5) on Section III-F].

## C. Fast Local Search

The work on R-EVO [17] has shown that a simplification of the original heuristic local search complemented by a global search is effective on achieving state-of-the-art results of the MCP, where the reactive local search (RLS) heuristic [21], [22] is simplified. On the other hand, the heuristics which are excessively strong and frequent are often time-consuming, and may even weaken the stochastic nature of EAs.

With above understanding, a fast local search operator tailored for the MBBP is presented in EA/SM, which works in an alternative manner between expansion and corrosion phases. In each phase, the operator adds/drops one node to/from the current solution while ensuring its feasibility. The pseudo-code of the fast local search is presented in Algorithm 2. It can be seen in Algorithm 2 that the fast local search works via alternating between expansion and corrosion phases. It selects a node $k$ from $U P A$ or $V P A$ randomly and adds it (node $k$ ) to $B$ while keeping $B$ almost balanced (expansion phase), and then return $B$. If no such node is available, it removes a node from $U^{b}$ or $V^{b}$ randomly while keeping $B$ almost balanced (corrosion phase), and then return $B$. In order to keep the obtained biclique balanced, we add one node to the partition whose cardinality is less than that of the other partition, or drop one node from the partition whose cardinality is more than that of the other partition.

## D. SM

It has been testified by quite a number of instances that introducing large mutation operators into EAs will effectively improve the performance of EAs on complex optimization problems. Such large mutation can generate new solutions far

Algorithm 3 Structure Mutation (B)
$G(U, V, E)$ Bipartite graph
$B\left(U^{b}, V^{b}\right)$ Current biclique
$U P A \quad$ Set of nodes in $U$ connected to all nodes in $V^{b}$
$V P A \quad$ Set of nodes in $V$ connected to all nodes in $U^{b}$

```
If \(U P A \neq \phi\) and \(V P A \neq \phi\)
If \(\left|U^{b}\right| \neq \phi\)
pick \(k \in U P A ; B \leftarrow\{k\} ;\) pick \(k \in U^{b} ; B \leftarrow B /\{k\} ;\) end
Update \(V P A\);
If \(V P A \neq \phi\) and \(\left|V^{b}\right| \neq \phi\)
pick \(k \in V P A ; B \leftarrow\{k\} ;\) pick \(k \in V^{b} ; B \leftarrow B /\{k\} ;\) end
end
If \(U P A \neq \phi\) and \(V P A=\phi\) and \(\left|U^{b}\right| \neq \phi\)
pick \(k \in U P A ; B \leftarrow\{k\} ;\) pick \(k \in U^{b} ; B \leftarrow B /\{k\} ;\) end
If \(U P A=\phi\) and \(V P A \neq \phi\) and \(\left|V^{b}\right| \neq \phi\)
pick \(k \in V P A ; B \leftarrow\{k\} ;\) pick \(k \in V^{b} ; B \leftarrow B /\{k\} ;\) end
return \(B\)
```

away from the current one in the solution space with considerable probability. Successful examples include the three points swap-based mutation and four stock remove and insertbased mutation for cutting stock problems with and without contiguity [23], merge-split operator for capacitated arc routing problems [24], etc. It has been observed that EAs with large mutation operators are less likely to be trapped in local optima. Original idea of large mutation (referred to as extended neighborhoods) can be traced back to [25] and [26].
In this paper, a new mutation operator, named SM, is proposed to implement the idea of large mutation, it is expected to make large jump in the solution space of the MBBP to enhance the exploration of the algorithm during the search process. The proposed SM has three important characteristics: 1) it can adjust the search direction of the following local search process by changing UPA or/and VPA of the current solution, since the fast local search process starts with a random node selected from UPA or VPA (expansion phase in Algorithm 2); 2) it does not change the fitness value (size) of the solution, thus no extra fitness evaluation is needed after the mutation; and 3) compared to random mutation operators, the feasibility of the solution can be guaranteed [constraints (2) and (4) are satisfied simultaneously], thus no repair operation is needed after the mutation. With characteristics 2) and 3), the SM can be conducted with a very low computational cost.
The pseudo-code of the SM is presented in Algorithm 3. It is an exchange process that replaces the nodes in $U^{b}$ by nodes from $U P A$ and then replaces the nodes in $V^{b}$ by nodes from VPA, where UPA represents the set of nodes in $U$ connected to all nodes in $V^{b}$, while VPA represents the set of nodes in $U$ connected to all nodes in $V^{b}$. It looks like that the SM operator can be executed on the current solution more than once, but in practice the cardinality of VPA or UPA is very limited, especially in the later phase of the search, thus, in EA/SM, each solution is manipulated by the SM only once per iteration.
Fig. 2 is an example to illustrate the SM procedure for the MBBP, where the dark dots represent the current biclique
![img-1.jpeg](img-1.jpeg)

Fig. 2. Example to illustrate the structure mutation procedure. (a) Initial state. (b) Intermediate state. (c) Final state.
[Fig. 2(a)]. First, a random node from $U^{b}$ is replaced by a random node from UPA, then VPA is updated [Fig. 2(b)]; second, if VPA is not empty, a random node from $V^{b}$ is replaced by a random node from VPA [Fig. 2(c)]. The size of the resulting biclique $B$ [Fig. 2(c)] is unchanged, while its structure is different from the previous one dramatically [Fig. 2(a)]. The difference lies in that all nodes in $B$ [Fig. 2(c)] have new adjacency attributes in $G$. The SM can increase the possibility of finding a new search area for the following local search process, therefore enhances the capability of EA/SM to jump out of local optima. Furthermore, the new promising search space will be memorized by the probability model for the following EDA-based restart process, which will also enhance the contribution of the restart process for global optimization.

## E. Repair-Assisted Restart

One new solution will be generated when the restart process is invoked by a certain trigger condition. In R-EVO [17], the reinitialized solution is built in a greedy fashion, where candidate node at every step is selected firstly with probability proportional to model values in $P$. Then, the feasibility is checked. Only the node that can legally expand the solution will be accepted into the current solution under built, which causes the size of the reinitialized solution prone to be very small. It can be perceived that the greedy restart process does not take full advantage of the statistical knowledge learned from in previous search process.

In EA/SM, a new repair-assisted restart process is presented, where each new solution is reinitialized in whole by sampling the search space according to the probability model $P$ with the statistical knowledge of possible promising area in solution space extracted during the previous search process. Then, the feasibility of the whole solution is checked. If the new solution violates the constraints, it is repaired by the modified Marchiori's heuristic repair operator (Section III-G) to guarantee the feasibility of the solution.

## F. Probability Model for Restarts

Estimation of distribution algorithms (EDAs) [27]-[34] have been investigated in the framework of evolutionary computation for more than ten years. The feature of EDAs is to model promising areas in the search space in a probabilistic manner, then guide the exploration of the algorithm with the probabilistic model [35]. In this paper, the EDA-like technique is adopted to learn the knowledge/model of promising area

```
Algorithm 4 Heuristic Repair \((B)\)
    \(G(U, V, E)\) Bipartite graph
    \(B\left(U^{b}, V^{b}\right)\) Current solution (likely not a biclique)
    \(\alpha \quad\) A very small value \(\alpha \in(0,1)\)
    // Extraction (to be a small almost balanced biclique)
    \(C\left(U^{c}, V^{c}\right) \leftarrow B\);
    While \(C \neq \phi\)
    If \(\left|U^{b}\right|<\left|V^{b}\right|\)
    pick \(k \in U^{c} ; C \leftarrow C /\{k\}\); end
    If \(\left|U^{b}\right|>\left|V^{b}\right|\)
    pick \(k \in V^{c} ; C \leftarrow C /\{k\}\); end
    if \(\left|U^{b}\right|=\left|V^{b}\right|\)
    pick \(k \in U^{c}\) or \(k \in V^{c} ; C \leftarrow C /\{k\}\); end
    // Flip a coin with head probability \(\alpha\)
    If the head turns up
    \(B \leftarrow B /\{k\}\)
    else
    remove from \(B\) and \(C\) all the nodes in \(B\) that are
        not connected to \(k\); end
    end // Extraction
    // Extension (to be a larger almost balanced biclique)
    \(C\left(U^{c}, V^{c}\right) \leftarrow G / B\)
    While \(C \neq \phi\)
    If \(\left|U^{b}\right|<\left|V^{b}\right|\)
    pick \(k \in U^{c} ; C \leftarrow C /\{k\}\); end
    If \(\left|U^{b}\right|>\left|V^{b}\right|\)
    pick \(k \in V^{c} ; C \leftarrow C /\{k\}\); end
    If \(\left|U^{b}\right|=\left|V^{b}\right|\)
    pick \(k \in U^{c}\) or \(k \in V^{c} ; C \leftarrow C /\{k\}\); end
    If \(k\) is connected to all nodes in \(B\)
    \(B \leftarrow B \cup\{k\}\); end
    end // Extension
    return \(B\)
```

during the local search process, and then reinitialize the searching population according to the knowledge/model.

The probability model adopted in this paper is a simple univariate model, $P=\left\{p_{1}, p_{2}, \ldots, p_{2 n}\right\} \in[0,1]$, each of whose variable represents the probability that the correspondent binary variable $b$ in the solution $B$ should take the value 0 or 1 . At the beginning of the algorithm, the probability model is set to be uniform distribution, $p_{i}=0.5$ for $i=1,2, \ldots, 2 n$. That means each binary variable has the same probability of taking value 0 or 1 . At the end of each generation $t$ in EA/SM, the best $M$ solutions (binary strings) are selected from the current population to update the probability model $P$. In order to reduce noise, only solutions providing balanced bicliques whose size is comparable (within a tolerance depth $\Delta$ ) with the largest one are taken into account as suggested in [17]. Let the $M$ selected solutions are $C^{i}=\left\{c_{1}{ }^{j}\right.$, $\left.c_{2}{ }^{j}, \ldots, c_{2 n}{ }^{j}\right\}, j=1,2, \ldots, M$. The probability model $P$ is updated in the same way as that in the PBIL algorithm [27]

$$
p_{i}=(1-\lambda) p_{i}+\lambda \sum_{j=1}^{M} c_{i}^{j} / M
$$

For $i=1,2, \ldots, 2 n, \lambda \in(0,1]$ is the learning rate. The bigger $\lambda$ is the more contribution of the $M$ selected solutions to the updated probability model will be.

If the algorithm cannot improve the current biclique for $A$ iterations, the proposed repair-assisted restart process is invoked. The same restart counter mechanism as RLS [21] is used. The reinitialized individual, $B=\left\{b_{1}, b_{2}, \ldots, b_{2 n}\right\}$, $i=1,2, \ldots, 2 n$, is generated one-by-one by sampling the search space according to the probability model $P$. Since the reinitialized individual may be infeasible, a repair operation is conducted consequently to check and repair the solution.

## G. Modified Marchiori's Heuristic Repair

The Marchiori's heuristic repair operator [19] has been shown to be effective in EAs for the MCP, but it is not designed for the MBBP, and cannot be adopted directly in EA/SM. To utilize the merits of Marchiori's heuristic repair operator, it is modified for the MBBP in this paper. The pseudo-code of the modified Marchiori's heuristic repair is presented in Algorithm 4. It has two phases: phase 1 extracts the illegal solution to be a small almost balanced biclique (lines 1-15); phase 2 extends the small biclique obtained in phase 1 to be a larger one (lines 16-27).

The time complexity of the SM operator is of the same order of magnitude as that of the fast local search operator; the two operators only perform one or two node additions or removals. In contrast, the time complexity of the heuristic repair operator is pretty high; the operator requires a sequence of node additions and removals to repair an initialized solution. Since the restart process is invoked only when the quality of solutions cannot be improved in the local search process for $A$ iterations, the interval of restarts should be at least $A$ iterations and the total execution number of restart is very limited. Therefore, the heuristic repair operator is affordable in EA/SM. Experimental results in Section IV also show that the runtime consumed by the heuristic repair operator is very limited.

## IV. EXPERIMENTAL STUDIES

In this section, the performance of EA/SM is experimentally investigated and compared with the state-of-the-art heuristic algorithm [9]. The effectiveness of the SM operator and the repair-based restart process is verified. The performance of EA/SM is also compared with those of two other repair-based EAs: a repair-based EDA and a repair-based GA.

A large number (30) of benchmark testing instances (graphs) are randomly generated as done in previous works [8]-[11], [14] and [15]. The benchmark graphs have different sizes, $n=250,500$, and different probability that a particular edge exists in $G, p=95 \%, 90 \%, 85 \%$ with uniform edge distribution (which is most common in nano-electronics). For ease of recording and comparison, the following naming rule is introduced, $n \mathrm{~A} \_\mathrm{pB} \_\mathrm{C}$, where A is the size of the graph, B is the probability that a particular edge exists in $G$ and C is the sequence order in the benchmark set with the same attributes (both $n$ and $p$ ). For example, graph $n 250 \_p 90 \% \_3$ means that the graph is of size 250 , the probability that a particular edge exists is $90 \%$ and it is the third graph in the

benchmark set with the same attributes $n=250$ and $p=90 \%$. (All the benchmark graphs used in the simulation in this paper and EA/SM source codes with supporting documents are available at: http://staff.ustc.edu.cn/ yuanbo).

As suggested in [19], the parameter $\alpha$ in the repair operator should be very small, $\alpha$ value is set to be 0.001 as [20] recommended for the MCP. The other parameters of EA/SM are set as suggested in [17], [19], and [20]: population size $N=10$; tolerance depth $\Delta=2$; learning rate $\lambda=0.7$; restart parameter $A=10$-kbest. These values work well among other test values in our experiments. A rigorous theoretical analysis on how these parameters affect the results is very hard and out of the scope of this paper, but we can comment that: 1) in order to reduce the noise in the updated probability model, tolerance depth $\Delta$ shouldn't be too large; 2) the bigger $\lambda$ is, the more contribution of the $M$ selected solutions to the updated probability model will be, so the probability model would converge quickly; and 3) periodic restarts are needed to assure that the search is not confined in a limited portion of the search space, but frequent restarts are time-consuming and may even weaken the learning ability of the PBIL method.

The algorithm stops after 200000 calls (maximum times of fitness evaluation $F_{\max }=200000$ ) of the local search and SM operators when the algorithm is very likely to have converged to a good solution, and help us get sufficient data in the evolutionary process. All the experiments were performed on two quadruple nucleuses 2.33 GHz Intel Xeon processors platform with 12 G memory. However, all tested algorithms were implemented as monolithic processes and no CPU core parallelism has been exploited.

## A. Comparisons With State-of-the-Art Heuristic Algorithm

The heuristic algorithms in [8], [9], [14], and [15] are three representative deterministic algorithms for the MBBP, whose performances have been testified successfully. Among these three algorithms, the algorithm in [9] is the most effective in terms of the quality of solutions. It consistently outperforms the algorithm in [8] on the quality of best solutions on all test instances, and such advantages are directly proportional to the crossbar sizes $n$. The algorithms in [14] and [15] aims to reduce the runtime of the algorithm in [9], while the quality of solutions got by them is slightly lower. Since one of the main advantages of meta-heuristic algorithms over heuristic algorithms is their effectiveness (quality of solutions), the heuristic algorithm in [9] is chosen as a comparing algorithm on the effectiveness in this paper. The heuristic algorithm was reimplemented and the correctness of the implementation has been testified by comparing the simulation results with the original paper's [9] on hundreds randomly generated graphs. It is notable that the heuristic algorithm always starts with an empty initial solution and it is a deterministic algorithm, so it is impossible to make any random initial condition and the same results will be obtained in multiple runs. Therefore, for each benchmark graph, the heuristic algorithm needs to be run only once, while EA/SM is to be run independently for 30 times to get the statistical results as the measure of performance. The following terms of the results are recorded in the experiments.

```
Algorithm 5 Repair-Based EDA \((G)\)
    \(p_{i} \leftarrow 0.5 ; i=1,2, \ldots, 2 n\)
    \(B_{i} \leftarrow\) Sampling \((P) ; i=1,2, \ldots, N\)
    \(B_{i} \leftarrow\) Heuristic Repair \(\left(B_{i}\right) ; i=1,2, \ldots, N\)
    Repeat
    Update \(P\) according to (5);
    \(B_{i} \leftarrow\) Sampling \((P) ; i=1,2, \ldots, N\)
    \(B_{i} \leftarrow\) Heuristic Repair \(\left(B_{i}\right) ; i=1,2, \ldots, N\)
    until maximum iteration reached
Algorithm 6 Repair-Based GA \((G)\)
    \(p_{i} \leftarrow 0.5 ; i=1,2, \ldots, 2 n\)
    \(B_{i} \leftarrow\) Sampling \((P) ; i=1,2, \ldots, N\)
    \(B_{i} \leftarrow\) Heuristic Repair \(\left(B_{i}\right) ; i=1,2, \ldots, N\)
    4. Repeat
    \(B_{i}{ }^{\prime} \leftarrow\) Selection Crossover and Mutation \((B) ; i=1,2, \ldots\),
        \(N\)
    \(B_{i}{ }^{\prime} \leftarrow\) Heuristic Repair \(\left(B_{i}{ }^{\prime}\right) ; i=1,2, \ldots, N\)
    until maximum iteration reached
```

1) Heuristic: The size obtained by the state-of-the-art heuristic algorithm [9].
2) Avg: The average size of the balanced biclique obtained by each EA in 30 runs.
3) Std: The standard deviation of the sizes of the balanced biclique obtained by each EA in 30 runs.
4) Best: The size of the largest balanced biclique obtained by each EA in 30 runs.
5) Ftime: The average times of fitness evaluation that each EA needed to obtain a balanced biclique as large as the Heuristic in 30 runs.
6) Rtime: The average times of restart process of each EA in 30 runs.
7) Time: The average runtime (in seconds) of each EA in 30 runs.
Table I provides the comparison results between the state-of-the-art heuristic algorithm in [9] and the proposed EA/SM on the MBBP (statistical test results will be presented in a separate table). It can be seen that EA/SM produces significantly better results (lager $k$ ) than the Heuristic [9] on all benchmark graphs. In particular, EA/SM can achieve improvements of $5.12 \%-21.48 \%$ with very small standard deviations $(\leq 1)$, and the improvements are more than $10 \%$ in most cases (21/30). In addition, EA/SM can obtain a balanced biclique as large as the heuristic in very limited times of fitness evaluation; the value Ftime of EA/SM is $0.89 \%-27.11 \%$ of the $F_{\max }$ and less than $10 \%$ of the $F_{\max }$ in most cases $(26 / 30)$. The invoking times of restart process are also very limited in EA/SM; the average period between restarts is $698.6-3072.2$ times of fitness evaluation. Given fixed $n$, as $p$ decreases, the problem becomes more difficult. The following results are observed: 1) the sizes $k$ obtained by both the heuristic algorithm [9] and EA/SM decrease sharply according with the boundary theory [4]; 2) the values of Ftime decrease, indicating EA/SM prone to converge more quickly; 3) the values of Rtime increase, indicating the restart process is invoked more frequently

TABLE I
Comparison Results Between the State-of-the-Art Heuristic Algorithm [9] and EA/SM on the MBBP (Statistical Test Results are Presented in Table IV)

in EA/SM; and 4) the values of time decrease, indicating EA/SM becomes less time-consuming for sparser benchmark graphs.

## B. Effectiveness of Main Contributions: Structure Mutation and New Repair-Assisted Restart

In EA/SM, the structure mutation is proposed to improve the exploration capability of the algorithm during the local search process to escape from local optima, while the new repair-assisted restart process is introduced to make full use of the statistical information extracted from the good solutions during the local search process with probability model. A very natural question is whether the proposed SM operator and the new repair-assisted restart process have any positive contribution to the performance of the algorithm. To answer this question, the performance of EA/SM are compared with three other EAs.

1) Evolutionary algorithm with greedy restart (EA/GR), which has the same framework as EA/SM, but no SM and repair operator is adopted. EA/GR adopts the same restart process as that present in [17].
2) Evolutionary algorithm with the new repair-assisted restart (EA/RR), which has the same framework as

EA/SM, and the new repair-assisted restart process is adopted after local search process, but no SM is adopted.
3) Evolutionary algorithm with structure mutation and greedy restart (EA/SM/GR), which has the same framework as EA/SM, and the SM is adopted in local search process, but no repair operator is adopted. EA/SM/GR adopts the same restart process as that present in [17]. All the parameters of EA/GR, EA/RR, and EA/SM/GR are set as the same as EA/SM. The three algorithms are run independently for 30 times on each benchmark graph.
Table II provides the experiment results of the four algorithms on the MBBP (statistical test results will be presented in a separate table). It can be seen that the performance of ER/GR is much weaker than those of other EAs. EA/GR even cannot obtain a biclique as large as that got by the heuristic algorithm [9] in most case, so the values of Ftime are unfilled in Table II. In particular, it is observed that the restart process in EA/GR is invoked more frequently (2.5-4.2 times) than EA/SM to help algorithm jump out of the local optima, which results in much longer runtimes. It can also be observed in Table II that the performances of both EA/RR and EA/SM/GR are weaker than that of EA/SM, while they both outperform the heuristic algorithm significantly.

TABLE II
Experiment Results of EA/GR, EA/RR, and EA/SM/GR on the MBBP (Statistical Test Results are Presented in Table IV)

Without of SM, the performance of EA/RR can be summarized as follows: 1) the values of Ftime are $2-3.8$ times more than that of EA/SM; 2) the values of Rtime are 2.2-3.4 times more than that of EA/SM; and 3) the runtimes are $13.6 \%-24.7 \%$ longer than that of EA/SM. Making use of greedy restart process [17] in place of the proposed new repair-assisted restart process, the performance of EA/SM/GR can be summarized as follows: 1) the values of Rtime are $8.5 \%-34.6 \%$ more than that of EA/SM and 2) the runtimes are $3.3 \%-15.8 \%$ longer than that of EA/SM, although the greedy restart process itself is slightly faster than the new repair-assisted restart process.

## C. Comparisons With Repair-Based EAs

For comprehensively understanding the advantage of EA/SM, it is also compared with two other repair-based EAs, which are constructed by incorporating the modified Marchiori's heuristic repair operator into an EDA and a GA, respectively, as shown in Algorithms 5 and 6. In the two repaired-based EAs, every solution generated by evolutionary operators is to be repaired by the heuristic repair operator as did in [19] and [20]. The procedure of repair-based EDA is easy to understand, while the repair-based GA obeys the definition of basic GA which uses roulette wheel selection, single-point crossover and one-bit mutation. Since GAs are prone to be trapped in local optima for combinatorial optimization problems with strict constraints, so no elitist strategy is used in repair-based GA for the MBBP. The population size and learning rate adopted in the repair-based EDA are set as the same as EA/SM. The population size, crossover probability, and mutation probability adopted in the repair-based GA are 40, 0.8, and 0.1 , respectively. As mentioned before, the heuristic repair operator is more time-consuming than both local search and SM. In our simulation experiments conducted in this paper, it is observed that the local search and SM operators are approximately two orders of magnitude faster than the heuristic repair operator. Therefore, a direct comparison between EA/SM and repair-based EAs is unfair. In order to solve this problem, a fixed and large $F_{\max }$ is set as the termination condition for the three algorithms to guarantee them converging to optimum or suboptimum solutions before termination. Based on this setting, the repair-based EAs stop after 4000 calls of the heuristic repair operator while EA/SM still stops after 200000 calls of the local search and SM operators. In spite of above setting, EA/SM is still much faster than the repair-based EAs, especially for large $n$. The two repair-based EAs are run independently for 30 times on each benchmark graph.

Table III provides the comparison results between EA/SM and the other repair-based EAs (statistical test results will be presented in a separate table). It can be seen that the performance of both repair-based EDA and repair-based GA are weaker

TABLE III
Comparison Results Between EA/SM, Repair-Based EDA, and Repair-Based GA on the MBBP (Statistical Test Results are Presented in Table IV)

TABLE IV
Statistical Significance Win-Loss-Tie Summary of Two-Tailed $t$-Test BAsed on 30 Benchmark Graphs


than that of EA/SM, while both of them outperform the heuristic algorithm [9] in most case. As mentioned above, the heuristic repair operator is very time-consuming and its runtime increases sharply with $n$, therefore the runtimes of the repair-based EAs are much longer than that of EA/SM, especially for large-scale benchmark graphs $(n=500)$. It can also be observed that the performance of repair-based EDA is slightly weaker than that of repair-based GA in most case. A reasonable explanation is that EDA is prone to premature convergence by its nature, and the convergence is further accelerated by invoking the heuristic repair operator frequently. The performance of repair-based GA becomes poor as $p$ decreases, especially for $n 500 \_p 85 \% \_C$ problems, A reasonable explanation is that is more difficult to extract a large biclique from a sparser graph, and
the basic GA cannot jump out of the local optima for these hard problems although no elitist strategy is used.

## D. Statistical Comparisons on Single Benchmark Graph

In order to compare the EAs in this paper in a sound statistical context, statistical tests are performed for paired EAs, e.g., EA/SM versus EA/GR and EA/RR versus the repair-based EAs, on each single benchmark graph. Statistical tests are carried out on the size $k$ obtained by each EA and provide the win-loss-tie summary. A two-tailed $t$-test is conducted with a null hypothesis stating that there is no difference between two algorithms in comparison. The null hypothesis was rejected if the $p$-value is smaller than the significance level $\alpha=0.05$. Table IV gives the win-loss-tie summary that comparing the

![img-2.jpeg](img-2.jpeg)

Fig. 3. Values of $k$ on benchmark graphs with size $n=250$ (Graph No. 1-15) obtained by 1) Heuristic; 2) EA/SM; 3) EA/GR; 4) EA/RR; 5) EA/SM/GR; 6) repair-based EDA; and 7) repair-based GA, respectively. Box plots are used to illustrate the distribution of these values. In each box, the central mark is the median, the edges of the box are the 25 th and 75 th percentiles, the whiskers extend to the most extreme data points the algorithm considers to be not outliers, and the outliers are plotted by + individually.

EAs in the 1st column with the EAs in the 1st row based on 30 benchmark graphs. For example, the 2 nd row compares EA/SM with other five EAs, EA/SM gets 30-0-0 ( 30 wins, 0 loss, 0 ties) in each paired comparison. Another example, row 4 column 5 compares EA/RR with EA/SM/GR, EA/RR
gets 12-1-17 (12 wins, 1 loss, 17 ties) in the comparison. The significance tests show that EA/SM is statistically better than other EAs on all benchmark graphs ( 30 wins).

Visualized comparisons of all the algorithms in this paper are displayed by box-plot in Figs. 3 and 4, which show the

![img-3.jpeg](img-3.jpeg)

Fig. 4. Values of $k$ on benchmark graphs with size $n=500$ (Graph No. 16-30) obtained by 1) Heuristic; 2) EA/SM; 3) EA/GR; 4) EA/RR; 5) EA/SM/GR; 6) repair-based EDA; and 7) repair-based GA, respectively. Box plots are used to illustrate the distribution of these values. In each box, the central mark is the median, the edges of the box are the 25 th and 75 th percentiles, the whiskers extend to the most extreme data points the algorithm considers to be not outliers, and the outliers are plotted by + individually.
distribution of the values of $k$ on 30 benchmark graphs with size $n=250$ and $n=500$, respectively.

## V. CONCLUSION

This paper proposes an EA with SM and a new repair-assisted restart scheme for the MBBP. Experimental
investigation on a large set of benchmark graphs shows that: 1) effective heuristics (local search and SM) coupled with an EA (EDA) can produce significantly better results than the state-of-the-art algorithm for the MBBP; 2) for complex combinatorial optimization problems, such as the MBBP, the SM, designed for enhancing the exploration capability of the

algorithm, can effectively help to avoid stagnation in local optima; and 3) the new repair-assisted restart process can take full advantage of the statistical knowledge learned from good solutions obtained in previous search process, therefore can generate more promising reinitialized solutions for the following local search process.
The proposed SM operator is not limited to the MBBP. It can easily be generalized to other similar problems, such as the MCP [18], the maximum edge biclique problem [36], and the maximum edge-weighted clique problem [37]. We believe that the idea, i.e., efficient local search accompanied by a large mutation, is also applicable to other hard optimization problems.
