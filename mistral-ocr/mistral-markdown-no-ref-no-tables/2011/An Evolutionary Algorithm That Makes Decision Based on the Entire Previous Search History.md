# An Evolutionary Algorithm That Makes Decision Based on the Entire Previous Search History 

Chi Kin Chow and Shiu Yin Yuen, Member, IEEE


#### Abstract

In this paper, we report a novel evolutionary algorithm that enhances its performance by utilizing the entire previous search history. The proposed algorithm, namely history driven evolutionary algorithm (HdEA), employs a binary space partitioning tree structure to memorize the positions and the fitness values of the evaluated solutions. Benefiting from the space partitioning scheme, a fast fitness function approximation using the archive is obtained. The approximation is used to improve the mutation strategy in HdEA. The resultant mutation operator is parameter-less, anisotropic, and adaptive. Moreover, the mutation operator naturally avoids the generation of out-of-bound solutions. The performance of HdEA is tested on 34 benchmark functions with dimensions ranging from 2 to 40. We also provide a performance comparison of HdEA with eight benchmark evolutionary algorithms, including a real coded genetic algorithm, differential evolution, two improved differential evolution, covariance matrix adaptation evolution strategy, two improved particle swarm optimization, and an estimation of distribution algorithm. Seen from the experimental results, HdEA outperforms the other algorithms for multimodal function optimization.


Index Terms-Benchmarking with other evolutionary algorithms, evolutionary algorithm using search history, fitness function approximation, parameter-less anisotropic adaptive mutation.

## I. INTRODUCTION

SEARCH HISTORY, including the performed operations, the positions of the evaluated solutions, and the fitness values of the solutions, is valuable information to enhance the performance of an evolutionary algorithm (EA). Intuitively, it can be used to maintain diversity. It can also guide the search direction or suggest promising regions of interest. In addition, when the same optimum reappears in the search history (i.e., a revisit occurs), it can warn that the search may have been trapped in a local optimum. In expensive objective function optimization, one may use the history to approximate the objective function and pre-evaluate the potential optimum on this approximated function, thus saving computation cost.

Several search algorithms [1]-[5], such as particle swarm optimization (PSO), genetic algorithm (GA), differential evolution (DE), and estimation of distribution algorithm (EDA), employ search history in the form of memory to

[^0]guide the search strategies. Search histories, in different EAs, are in different forms and contribute to search strategy in different manners. In PSO, each candidate solution is modeled as a particle that moves in a multidimensional search space. The corresponding search history is in terms of its best-visited position $\mathbf{l}$ and the best visited position $\mathbf{g}$ amongst the swarm. The search strategy of PSO, referred to as particle velocity, is adjusted according to the vector difference between its position $\mathbf{x}$ and $\mathbf{l}$, and the vector difference between $\mathbf{x}$ and $\mathbf{g}$.

Canonical GA and DE presume that fitter population contains more promising information about the position of global optimum. Thus, the search strategies of GA and DE refer to the offspring generation by the parent population based genetic operators, such as mutation, crossover, and selection. Comparing with PSO, the search strategies of GA and DE involve shorter search histories.

Recently, the non-revisiting genetic algorithm (NrGA) is proposed by Yuen and Chow [6], [7]. It memorizes all evaluated solutions by a binary partitioning tree (BSP) archive. The non-revisiting scheme of NrGA uses this archive to prevent solution re-evaluation. More importantly, this scheme acts as a parameter-less adaptive mutation operator. The adaptation of this scheme to other search methods is reported in [8], [9].

Owing to the fact that survived individuals have better fitness values, EDA presume that the distribution of the evaluated solutions (the survival individuals) correlates with the probability distribution of global optimum. The more survived individuals in a region, the higher probability the global optimum can be found in there. Thus, EDA memorizes the distribution of the evaluated solutions and obtains new candidate solution by sampling the distribution.

Tabu search (TS) [10] uses a short term memory, called Tabu list, to memorize the solutions that have been visited in the recent past. Different from PSO, GA, DE, and EDA of which their search histories infer promising regions for the prospective search, TS refuses to repeat the search history and prevents revisiting the solutions stored in the Tabu list.

Search history can also be used to build an empirical model that approximates the fitness function. The approximation is then used to predict promising candidate solutions at a smaller evaluation cost than the original problem. A comprehensive review of different approximation methods is provided in $[11]-[14]$.

Besides of mechanism and motivation, the discussed EAs are different in the sense that they use different memory archive structures to memorize search history. In PSO, GA,


[^0]:    Manuscript received April 15, 2009; revised August 21, 2009 and November 26, 2009; accepted December 9, 2009. Date of publication September 22, 2011; date of current version December 1, 2011. This work was supported by CityU under Grant 7002304.

    The authors are with the Department of Electronic Engineering, City University of Hong Kong, Kowloon Tong, Hong Kong, China (e-mail: chowchi@cityu.edu.hk; kelviny.ee@cityu.edu.hk).
    Digital Object Identifier 10.1109/TEVC.2010.2040180

DE, and TS, the search histories are stored in a list structure archive. For NrGA, the evaluated solutions are memorized by a tree-structure archive which can manage spatial data well. For EDA, the distribution of the evaluated solution is commonly represented by a parametric model [15]. Recently, Liou and Chen [16] presented a multidimensional space discretization method for encoding continuous decision variables with discrete codes by discretizing the continuous domain, which is named multidimensional split-on-demand ( mSod ). For the EAs that predict promising candidate solutions by the approximated fitness function, search histories are in terms of different approximation models such as low-order polynomial regression, radial basis function network (RBFN), extreme learning machine (ELM) [17], and Gaussian process model (GPM) [13]. A comparison of the models can be found in [12], [18], and [19].

Apart from the employed archive structure, these EAs are different in terms of the usage of search history. The Tabu list in TS is a negative search guidance as the list provides the positions of which TS should not visit. In contrast, the search histories of GA, PSO, DE, and EDA somehow represent the positions which the EAs should go to.

More importantly, they use different portions of search history to guide the search. GA, DE and PSO only use partial search histories-that is, only part of the information gained from the search is retained and the rest is discarded. TS stores only recently visited solutions in the Tabu list and discards solutions once the list is full. EDA abstracts the search history by a predefined parametric model and proceeds to discard the raw search data. On the other hand, NrGA advocates storing all visited solutions in memory, then organize them in some ways to guide the search. At first glance, there seems a tradeoff between the portion of search history and the corresponding contribution to the search. On the one hand, a larger portion of search history provides a more detailed description of the objective function. On the other hand, it needs a larger amount of memory to record the history. In fact, the amount of memory required is reasonable and acceptable. First, consider applications which have expensive and/or time consuming fitness evaluations; the fitness evaluation cost is significantly higher than the solution generation cost. There are many such applications in engineering, artificial intelligence, and robotics. For such problems, the total number of evaluations that can be made by an EA cannot be too large; and it is culpable to throw away any information gained from fitness evaluations. Second, currently, the memory that is becoming available due to advance in computer technology is increasing drastically (Moore's law [20]). Algorithms that are previously considered memory demanding, e.g., $z$ buffer in computer graphics, are now standard provisions. Third, even in applications whose solution generation costs are significant, it has recently been shown that using the entire search history may still give performance gains in spite of the memory overhead (see [21] for our study on a nondeterministic polynomial (NP) hard problem). Finally, EA are seldom used alone. Memetic algorithms [22], [23], the idea of hybridizing EA with another algorithm which encodes domain specific knowledge, often results in the best algorithm. In such a scenario, the total
number of evaluations that the EA is subject to is limited. In conclusion, in many cases, it is preferred to use the entire previous search history to adaptively guide the search strategy.

In this paper, we report a novel evolutionary algorithm, namely History driven Evolutionary Algorithm (HdEA). It is shown that when a BSP tree archive stores the positions and the fitness values of all evaluated solutions, this archive, namely fitness tree, can be treated as an approximation of the fitness function. Moreover, we incorporate the fitness tree to govern the EA search, through which a new parameter-less and adaptive mutation scheme, namely guided anisotropic search (GAS), is obtained.

HdEA is superior to the methods of [12], [18], and [19] in the sense that the fitness tree uses less computation to reapproximate the fitness function. Given an evaluated solution, the fitness tree rapidly responds to the update of the approximated fitness function by inserting a tree node. On the other hand, the ELM, RBFN, and GPM in [12], [18], and [19] respond to the update by model re-training, which is more computational expensive. This superiority is more obvious when the dimension of the search space increases. HdEA is also superior to EDA in terms of the robustness of their memory archive structures. EDA suffers from the problem of model parameter selection, but HdEA does not as the fitness tree is a nonparametric approximation model.

There are several conceptual differences between TS and HdEA: 1) TS only stores recently visited solutions while HdEA stores all visited solutions; that is, TS is not nonrevisiting but HdEA is (though revisit seldom occurs in continuous search space); 2) TS only passively uses the Tabu list to prevent revisits while HdEA organizes the entire previous search history and actively uses it to guide the search; 3) the BSP tree employed in HdEA is a more advanced data structure than the Tabu list; it encodes landscape information rather than local neighborhood information; and 4) HdEA does not introduce any additional control parameter whilst TS does.

Though HdEA and NrGA share the same nature in that they both memorize all evaluated solutions to perform adaptive mutation, HdEA and NrGA are quite different algorithms. As aforementioned, NrGA is applied on discrete search space where the precision of its optima depends on the axis resolution. On the other hand, HdEA deals with continuous search space to which the precision of its optima is up to the precision of the computer. Moreover, the usage of the memory archive in HdEA is different from that in NrGA. Though both use nonparametric representation, NrGA uses the archive to estimate the density of the evaluated solutions, while HdEA uses the archive to approximate the fitness landscape.

In summary, HdEA has the following remarkable features.

1) HdEA guides the search strategy using the entire search history.
2) HdEA naturally avoids generating any out-of-bound solutions and hence the extra solution-repair operator is not necessary.
3) HdEA uses a tree structure archive, which is nonparametric, to memorize the search history and hence no parametric model and its attendant model parameter selection is needed.

4) The fitness landscape re-approximation process in HdEA is achieved by a standard tree node insertion, which is viewed as an incremental learning.
5) GAS computes not only the mutation step size but also the mutation direction.
The rest of this paper is organized as follows. Section II presents the mechanism of HdEA. Section III reports the structure and the distinct features of the memory archive in HdEA. Section IV presents the details of GAS. Section V reports the experimental results and Section VI gives the conclusion.

## II. History Driven Evolutionary Algorithm

History driven evolutionary algorithm is a real coded evolutionary algorithm. For a $D$-dimensional search space $S \subset \Re^{\mathrm{D}}$, an individual $\mathbf{x}$ of HdEA is a 1 by $D$ real valued vector, i.e., $\mathbf{x} \in \Re^{\mathrm{D}}$. Evolutionary algorithm searches for the optimum by four main steps, namely population initialization, crossover, mutation, and selection. HdEA focuses on enhancing the mutation by GAS and the entire previous search history.

HdEA is considered as a generic EA module (EAM) cooperating with an adaptive mutation module (AMM). EAM consists of the standard EA operators such as population initialization, crossover operator, and selection operator; while AMM consists of the GAS module and the memory archive, namely fitness tree.

HdEA starts with initializing the population $\mathbf{P}=\left\{\mathbf{x}_{\mathbf{i}}\right\}$. Afterward, the offspring population $\mathbf{N}=\left\{\mathbf{n}_{\mathbf{i}}\right\}$ is generated by genetic operators such as crossover and mutation. The new population is then selected from the parent population and the offspring population. The reproduction process and the selection process are repeated until the number of iterations exceed a pre-determined value $N_{g}$. Fig. 1 shows the block diagram of HdEA. The circled numbers represent the step orders within a HdEA iteration. Algorithm A1 shows the pseudo code for HdEA. The code sections: steps $4-7$, steps $9-16$, and steps 19-21 in boldface indicate the newly added codes for HdEA, which will be explained in the following subsections.

## A. Fitness Tree Initialization and Update

In the beginning of EA evolution, the fitness tree is initialized to consist of the root node only (step 4 at Algorithm A1). During the evolution, once an individual is evaluated, knowledge to the fitness landscape is gained. Fitness tree responds to this gained knowledge by inserting the individual (its position and fitness value) to the tree. The insertion is performed after the population initialization (steps 5-7 at Algorithm A1) and the evaluations of offspring individuals (steps 19-21 at Algorithm A1).

## B. Reproduction Strategy of HdEA

In HdEA, offspring pool $\mathbf{N}=\left\{\mathbf{n}_{\mathbf{i}}\right\}$ is generated by two genetic operators: mutation and crossover. Given a population pool $\left\{\mathbf{x}_{\mathbf{i}}\right\}$, each individual $\mathbf{x}_{\mathbf{i}}$ is mutated by GAS, i.e., $\mathbf{x}_{\mathbf{i}} \xrightarrow{G A S}$ $\mathbf{m}_{\mathbf{i}}$ (The details of GAS will be discussed in Section IV. At the current stage, one can regard it as a black-box mutation operator which maps a solution $\mathbf{x} \in S$ to its mutant $\mathbf{m} \in S$ ).

```
Algorithm A1: History Driven Evolutionary Algorithm
(HdEA)
Input: 1) fitness function \(f(.) \), 2) search space \(S, 3)\) popu-
    lation size \(\mu, 4)\) number of generations \(N_{g}\)
1. Initialize the current population \(\mathbf{P}=\left\{\mathbf{x}_{\mathbf{i}}\right\}_{\mathbf{i}}=1,2, \ldots, \mu\)
where \(\mathbf{x}_{\mathbf{i}} \in S\)
2. Evaluate the population \(\mathbf{P}\)
3. Find the historical optimal solution \(\mathbf{x}_{\mathbf{0}}\)
    /* Fitness Tree Initialization */
4. Initialize fitness tree \(T\) to consist of a root node only
5. For \(\mathbf{i}:=1\) to \(\mu\)
6. \(\quad\) BSPTreeNodeInsert \(\left(\left[\boldsymbol{x}_{i}, \boldsymbol{f}\left(\boldsymbol{x}_{i}\right)\right], \boldsymbol{T}\right)\)
7. Next \(i\)
    /* End of Fitness Tree Initialization */
8. For \(g:=2\) to \(N_{g}\)
    /* Reproduction Strategy of HdEA */
9. For \(i:=1\) to \(\mu\)
10. $\quad \mathbf{m}_{\mathbf{i}}:=\boldsymbol{G A S}\left(\mathbf{x}_{\mathbf{i}}, \boldsymbol{T}\right)$
11. Next \(i\)
12. For \(i:=1\) to \(\mu\)
13. $\quad \mathbf{a}:=\operatorname{Random}\left(\left\{\mathbf{m}_{\mathbf{i}}\right\}\right)$
14. $\quad \mathbf{b}:=\operatorname{Random}\left(\left\{\mathbf{m}_{\mathbf{i}}\right\}\right)$ subject to \(\boldsymbol{b} \neq \boldsymbol{a}\).
15. $\quad \mathbf{n}_{\mathbf{i}}=\operatorname{Crossover}(\mathbf{a}, \mathbf{b})$
16. Next \(i\)
    /* End of Reproduction Strategy of HdEA */
17. Evaluate the population \(\mathbf{N}=\left\{\mathbf{n}_{\mathbf{i}}\right\}_{i=1,2, \ldots, \mu}\)
18. Update \(\mathbf{x}_{\mathbf{0}}\)
    /* Fitness Tree Update */
19. For \(i:=1\) to \(\mu\)
20. BSPTreeNodeInsert \(\left(\left[\mathbf{n}_{\mathbf{i}}, \boldsymbol{f}\left(\mathbf{n}_{\mathbf{i}}\right)\right], \boldsymbol{T}\right)\)
21. Next \(i\)
    /* End of Fitness Tree Update */
22. \(\mathbf{P}:=\operatorname{Selection}(\mathbf{P} \cup \mathbf{N})\)
23. Next \(g\)
```

Output: The optimal solution $\mathbf{x}_{\mathbf{o}}$ found by HdEA

Afterwards, every offspring individual $\mathbf{n}_{\mathbf{i}}$ is generated by the crossover of two mutants randomly picked from the set $\left\{\mathbf{m}_{\mathbf{i}}\right\}$. Steps 9-16 of Algorithm A1 list the implementation of the reproduction strategy of HdEA.

## III. Fitness Tree

HdEA uses a BSP tree as an archive which stores the positions and the fitness values of the evaluated solutions $\left\{\left\{\mathbf{s}_{\mathbf{i}}\right.\right.$, $\left.\left.f\left(\mathbf{x}_{i}\right)\right\}\right\}$. It partitions the whole search space $S$ according to the distribution of $\left\{\mathbf{s}_{\mathbf{i}}\right\}$. A tree node represents a partitioned sub-region of $S$. Suppose a parent node has two child nodes $\mathbf{l}$ and $\mathbf{r}$. The sub-regions represented by $\mathbf{l}$ and $\mathbf{r}$ are disjoint and their union is the sub-region of the parent, (i.e., the child nodes binary partitions the parent sub-region). As the tree construction depends on the sequence of solutions found by the EA, the BSP tree is a random tree and its topology is different from trial to trial.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Block diagram of HdEA.
The evaluated solutions in HdEA are recorded by the same procedure used in NrGA. Initially, the tree archive $T$ in HdEA consists of only the root node. Each node of the tree records a distinct previously visited solution $\mathbf{s}$ of the EA. It also represents a sub-region $X$ of the search space. Each subregion is a hyper-rectangular box of the search space. The tree is organized such that the nodes binary partition the search space using Euclidean metric. Two child nodes $\mathbf{a}$ and $\mathbf{b}$ binary partition the space of its parent node into two disjoint halves $A$ and $B, A \cap B=\phi$, by a hyper-plane at dimension $j$, chosen such that the difference of $x$ and $y$ along the dimension is the largest amongst all dimensions. In this way, each previous solution generated by the EA is recorded in a node of the tree, and the BSP tree serves as an efficient data structure to query the sub-region of $\mathbf{x}$. Algorithm A2 shows the pseudo code for BSP tree node insertion.

For more details on the tree construction as well as a working example, please refer to [7]. Note that since we are dealing with continuous search space, no node-pruning and backtracking is needed. Thus, the tree construction and management is simpler than that in NrGA [7].

## Definition 1: The Sub-Region of $\mathbf{x}$

Suppose $\mathbf{x}$ is a solution in the search space $S$, i.e., $\mathbf{x} \in S$, and $S$ is partitioned as the sub-region set $H=\cup_{i} h_{i}$ by the fitness tree, we define the sub-region $h \subseteq H$ as the "sub-region of $\mathbf{x}$ " if $\mathbf{x} \in h$ and $h$ is represented by a leaf node of the fitness tree.

Consider the situation when the fitness values of the evaluated solutions are also stored in the memory archive of HdEA;
the archive can be regarded as the approximation $\tilde{f}(\mathbf{x})$ of a fitness function $f(\mathbf{x})$. Given a tree which stores the evaluated solution set $\left\{\left[\mathbf{s}_{\mathbf{i}}, y_{i}=f\left(\mathbf{s}_{\mathbf{i}}\right)\right]\right\}_{i=1,2, \ldots}$ and partitions the search space as sub-region set $H=\cup_{i} h_{i}$, the fitness value of an unseen solution $\mathbf{x}$ can be approximated as $y_{k}$, i.e., $f(\mathbf{x}) \approx \tilde{f}(\mathbf{x})$ $=y_{k}$, if $\mathbf{x}$ is inside the sub-region $h_{k}$. Since the fitness of all solutions in the sub-region of a BSP tree node is approximated to the same value, i.e., $\tilde{f}(\mathbf{a})=\tilde{f}(\mathbf{b})=y_{k}$ for all $\mathbf{a}, \mathbf{b}, \mathbf{s}_{\mathbf{k}} \in h_{k}$, $\tilde{f}(\mathbf{x})$ is a step-wise function and the landscape of $\tilde{f}(\mathbf{x})$ is of the shape of a "terraced field". Because the tree archive is an approximation model of the fitness function, we call the tree a fitness tree.

As the approximation error of $\tilde{f}(x)$ monotonically decreases with a growing number of evaluated solutions, and the solutions are recorded one by one; this approximation process can be viewed as a simple incremental learning method in the field of machine learning.

Comparing between the fitness tree and mSoD, they are similar in the sense that both partition the search space into hyper-rectangular and nonoverlapping sub-regions. However, the fitness tree binary partitions the space whilst mSoD uses different partitioning schemes for different space dimensionalities, i.e., a quad-tree partitioning for 2-D space; an oct-tree partitioning for 3-D space, and so on. For a 30-dimensional fitness function (as those used in the experiment section), mSoD uses a $2^{30}$-tree to represent the space partitioning, and each node of the tree has $2^{30}$ child nodes. Thus, the structure of the fitness tree is much simpler than that of mSoD , and this simplicity in-

![img-3.jpeg](img-3.jpeg)
(a)
![img-3.jpeg](img-3.jpeg)
(b)

Fig. 2. Content of $S$ : (a) $S$ is partitioned by six evaluated solutions $\left\{\mathbf{s}_{1}, \ldots\right.$, $\mathbf{s}_{\mathbf{6}}$ \}. (b) Topology of the fitness tree: the leaf nodes labeled $\mathbf{s}_{1}, \ldots, \mathbf{s}_{\mathbf{6}}$ represent the sub-regions $\mathbf{s}_{1}, \ldots, \mathbf{s}_{\mathbf{6}}$, respectively, and the node labeled $\mathbf{r}$ represents the root node the fitness tree.
![img-3.jpeg](img-3.jpeg)

Fig. 3. Approximated fitness landscape by the fitness tree shown in Fig. 2(b). creases along with the space dimensionality. HdEA constantly partitions the search space during the whole evolution. In contrast, the split rate of mSoD increases along with iteration, so the corresponding space partitioning is much more frequent in the latter part of the evolution. The partitioning method is also different. In HdEA, the partition boundary is defined by a rule (aiming at reducing the maximum size of the hyper-rectangular regions), whilst the split point in mSoD is randomly picked. The search space partitioning of mSoD is

## Algorithm A2: BSP Tree Node Insertion

Input: 1) An individual $\mathbf{x}$ and it fitness value $f$, 2) BSP tree $T$

1. Curr_node $:=$ root node of $T$
2. While (Curr_node has two child nodes: a and b)
3. Comparing dimension $j:=\arg \max _{k \in[1, D]}|\mathbf{a}(k)-\mathbf{b}(k)|$
4. If $(|\mathbf{a}(j) \cdot \mathbf{x}(j)| \leq|\mathbf{b}(j) \cdot \mathbf{x}(j)|)$
5. Curr_node $:=$ child node a
6. Else
7. Curr_node $:=$ child node $\mathbf{b}$
8. End
9. Loop
10. Insert a child node to Curr_node that records $\mathbf{x}$ and $f$
different from trial to trial even when the sequence of solution generation is kept the same.

Comparing between HdEA and NrGA, the memory archives of HdEA and NrGA have four differences in terms of the represented information and the tree operation.

1) The memory archive of HdEA stores the fitness values of the evaluated solutions but the memory archive of NrGA does not.
2) The archive of HdEA approximates the fitness landscape; whilst the archive of NrGA represents the density of the evaluated solutions.
3) Since the search space of HdEA is continuous, the number of possible solutions in a sub-region is infinite and no node-pruning is performed.
4) The number of nodes in the fitness tree is exactly the same as the number of evaluated solutions, whilst this is in general not true in NrGA due to pruning.
Example: Suppose $S=[0,1]^{2}$ is the search space, and EA randomly generates the individual sequence $\left(\mathbf{s}_{1}, \mathbf{s}_{5}, \mathbf{s}_{3}, \mathbf{s}_{2}, \mathbf{s}_{\mathbf{6}}\right.$, $\mathbf{s}_{4}$ ). The corresponding space partitioning is shown in Fig. 2(a). $s_{i}$ are the real nodes and $n_{i}$ are the "virtual" nodes. For real nodes, $s_{i}$ represents both the solution $\mathbf{s}_{\mathbf{i}}$ and the corresponding sub-region $h_{i}$. Fig. 2(b) shows the topology of the fitness tree $T$, which is a BSP tree. Please refer to [7] for details on how this tree is constructed.

The leaf nodes labeled $\mathbf{s}_{1}, \mathbf{s}_{2}, . ., \mathbf{s}_{\mathbf{6}}$ represent the sub-regions $h_{1}, h_{2}, \ldots, h_{6}$, respectively; the sub-region of node $\mathbf{n}_{2}$ is $N_{2}=h_{1} \cup h_{2}$; the sub-region of node $\mathbf{n}_{1}$ is $N_{1}=h_{1} \cup h_{2} \cup h_{3}$; the sub-region of node $\mathbf{n}_{4}$ is $N_{4}=h_{4} \cup h_{5}$; the sub-region of node $\mathbf{n}_{3}$ is $N_{3}=h_{4} \cup h_{5} \cup h_{6}$; and node $\mathbf{r}$ represents the entire search space $S$.

Given the fitness values of the six individuals are: $f\left(\mathbf{s}_{\mathbf{1}}\right)=$ $1, f\left(\mathbf{s}_{5}\right)=2, f\left(\mathbf{s}_{3}\right)=5, f\left(\mathbf{s}_{2}\right)=7, f\left(\mathbf{s}_{6}\right)=3$, and $f\left(\mathbf{s}_{4}\right)=4$, the approximated function of $f(\mathbf{x})$ by $T$ is expressed as

$$
\tilde{f}(\mathbf{x})= \begin{cases}1 & {\left[x_{1}, x_{2}\right] \in[0,0.35) \times[0.3,1]} \\ 7 & {\left[x_{1}, x_{2}\right] \in[0.35,0.5) \times[0.3,1]} \\ 5 & {\left[x_{1}, x_{2}\right] \in[0,0.5) \times[0,0.3)} \\ 4 & {\left[x_{1}, x_{2}\right] \in[0.5,0.65) \times[0,0.6)} \\ 2 & {\left[x_{1}, x_{2}\right] \in[0.65,1] \times[0,0.6)} \\ 3 & {\left[x_{1}, x_{2}\right] \in[0.5,1] \times[0.6,1] .}\end{cases}
$$

Fig. 3 shows the output landscape of $\tilde{f}(x)$.

TABLE I
ACTIVE Neighborhoods of the Leaf NODEs for COMPUTING OPTIMAL Sub-REGIONS


## IV. GUIDED ANISOTROPIC SEARCH

In this section, we present a novel mutation operator GAS. GAS is a randomized gradient descent-like genetic operator. Its mutation step size is randomly assigned within an adaptively adjusted range, while its search direction is governed by the approximated fitness landscape from the fitness tree.

GAS is an adaptive, parameter-less and guided mutation operator. It has the same advantage as the parameterless adaptive mutation operator in NrGA, namely, the mutation step size is adaptively adjusted based on the search history. Moreover, the search direction of a mutant in GAS is guided by the fitness landscape instead of being a random walk as in the mutation of NrGA.

In GAS, an individual $\mathbf{x}$ moves in the direction that the fitness improvement of $\bar{f}(\mathbf{x})$ at $\mathbf{x}$ is locally maximal. This can be done by assigning the mutation direction $\mathbf{v}$ as the direction pointing to the nearest historical optimum $\mathbf{y}$ of $\mathbf{x}$, i.e., $\mathbf{v}=\mathbf{y}-\mathbf{x}$. Recall that $\bar{f}(x)$ is a step function; its optimum is in the form of a $D$-dimensional sub-region rather than a $D$-dimensional point. Also, the topology of the fitness tree represents the adjacencies amongst the steps (sub-regions). Therefore the procedure of finding the nearest optimum of $\mathbf{x}$ is equivalent to finding the nearest optimal sub-region of the sub-region of $\mathbf{x}$ in $\bar{f}(x)$.

To balance the exploitative effect of this gradient descentlike direction assignment, the mutation step size $\alpha$ is randomly selected in the interval $(0,1)$, in which the mutant $\mathbf{m}$ of $\mathbf{x}$ is a linear combination of $\mathbf{x}$ and $\mathbf{y}, \mathbf{m}=\mathbf{x}+\alpha \mathbf{v}=(1-\alpha) \mathbf{x}+$ $\alpha \mathbf{y}$. It may happen that $\mathbf{x}$ is a local optimum, i.e., $\mathbf{x}=\mathbf{y}$. For such cases, the mutant $\mathbf{m}$ will be randomly picked from the sub-region of $\mathbf{x}$. Algorithm A3 shows the procedure of GAS with the fitness landscape approximated by the fitness tree $T$. Note that GAS naturally avoids generating any out-of-bound solutions. This is an advantage over some other methods that may generate out-of-bound solutions and need to define an extra repair operator to change the solutions back to valid ones.

Seen from Algorithm A3, two types of information about $\bar{f}(x)$ should be provided to GAS: 1) the optimal sub-region set; and 2) distance metric amongst sub-regions for defining the term "nearest." In the following subsections, we present a method that uses the fitness tree to estimate the optimal subregion. Then we propose a metric to measure the distance between sub-regions, and hence define the nearest optimal sub-region of a sub-region. An illustrative example is provided. The example employs the same search space, fitness tree and terminologies used in the example in Section II. Finally, the strengths and the weaknesses of GAS are discussed.
![img-4.jpeg](img-4.jpeg)

Fig. 4. (a) Gray straight line between $\mathbf{x}$ and $\mathbf{s}_{\mathbf{1}}$ is the range of possible mutants of $\mathbf{x}$ by GAS and (b) mutation directions of $\mathbf{x}$ at different positions of $S$.

## A. Estimation of Optimal Sub-Region

In this subsection, we present a method that estimates the optimal sub-region based on the topology of the fitness tree. The sub-region $X$ of node $\mathbf{x}$ is optimal if the fitness value of $\mathbf{x}$ is the smallest amongst the neighborhood of $X$.

Definition 2: Neighborhood of a Sub-region
The sub-region $Y$ of node $\mathbf{y}$ is the neighborhood of the subregion $X$ of leaf node $\mathbf{x}$ if $X \subseteq Y$.

Remark: Because the BSP tree binary partitions the search space and hierarchically represents the partitioned sub-regions, node $\mathbf{x}$ must be the descendant of node $\mathbf{y}$. For example, the sub-region of node $\mathbf{n}_{2}$ and the sub-region of node $\mathbf{n}_{1}$ are the neighborhoods of the sub-region of node $\mathbf{s}_{\mathbf{1}}$.

Every sub-region can be regarded as an optimum up to a certain neighborhood size. For example, the sub-region $h_{1}$

![img-5.jpeg](img-5.jpeg)

Fig. 5. Sample fitness landscapes for illustrating the effectiveness of GAS. (a) $\Omega_{1}$. (b) $\Omega_{2}$. (c) $\Omega_{3}$.








Fig. 6. Indicators of the best test algorithm in the experiments. The cells with gray color represents that the corresponding test algorithm outperforms the others for a particular function and a particular function dimension.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Histograms of the ranks of HdEA, RCGA-UNDX, CMA-ES, DE, ODE, DEahcSPX, DPSO, SEPSO, and EDA on the 64 test cases.

## Algorithm A3: GAS

Input: 1) An individual $\mathbf{x}, 2$ ) fitness tree $T$

1. $\left\{\mathbf{s}_{\mathbf{i}}\right\}:=$ The evaluated solution set stored in $T$
2. $H=\cup_{i} h_{i}:=$ The partitioned sub-region set where $h_{i}$ is the sub-region of $\mathbf{s}_{\mathbf{i}}$
/* Search for the nearest optimal sub-region $\mathbf{y}$ of $\mathbf{x} * /$
3. Search for the sub-region $h \subseteq H$ of $\mathbf{x}$
4. Find the nearest optimal sub-region of $h$
5. $\mathbf{y}:=$ The evaluated solution inside $h$ /* End of Search for the nearest optimal sub-region $\mathbf{y}$ of $\mathbf{x} * /$
6. If $(\mathbf{x}=\mathbf{y})$
7. $\quad \mathbf{m}:=\operatorname{Random}(h)$
8. Else
9. $\alpha:=\operatorname{Random}((0,1))$
10. $\quad \mathbf{m}:=\alpha \mathbf{x}+(1-\alpha) \mathbf{y}$
11. End

Output: The mutated individual $\mathbf{m}$
shown in Fig. 2(a) is optimal when its neighborhood is the whole search space; the sub-region $h_{5}$ is an optimum if $h_{4}$ is the only neighbor of $h_{5}$; in the extreme case, $h_{2}$ is an optimum if the corresponding neighborhood is itself. Commonly, the
term "neighborhood size" refers to the number of neighbor points concerned. Due to the topology of the fitness tree, the number of neighbor points (evaluated solutions) of a node decreases with its node depth. For example, when comparing node $\mathbf{n}_{2}$ and its parent node $\mathbf{n}_{1}$, the corresponding neighbor point sets increase from $\left\{\mathbf{s}_{2}\right\}$ to $\left\{\mathbf{s}_{2}, \mathbf{s}_{3}\right\}$. Similarly, while considering node $\mathbf{n}_{1}$ and its parent node $\mathbf{r}$, the corresponding neighbor point set further increases from $\left\{\mathbf{s}_{2}, \mathbf{s}_{3}\right\}$ to $\left\{\mathbf{s}_{2}, \mathbf{s}_{3}\right.$, $\left.\mathbf{s}_{4}, \mathbf{s}_{5}, \mathbf{s}_{6}\right\}$. Therefore, we represent "neighborhood size" by the tree node depth difference:

Definition 3: Neighborhood Size of a Sub-region
Suppose the sub-region $Y$ of node $\mathbf{y}$ is the neighborhood of the sub-region $X$ of node $\mathbf{x}$, the neighborhood size of $Y$ related to $X$ is defined as the depth difference of $\mathbf{y}$ and $\mathbf{x}$.

We denote by $l$ the neighborhood size for estimating the optimal sub-region: Suppose the sub-region $Y$ of node $\mathbf{y}$ is the neighborhood of the sub-region $X$ of node $\mathbf{x}$; and the neighborhood size of $Y$ related to $X$ is $l ; X$ is estimated as an optimal sub-region if the fitness value of $\mathbf{x}$ is the smallest amongst all evaluated solutions in $Y$. When $l$ is chosen to be the depth of the fitness tree, it is assumed that the approximated fitness function consists of only one optimum. All individuals are enforced to approach to the best found optimum. On the other hand, if $l$ equals zero, every sub-region is regarded as a local optimum; the corresponding GAS is equivalent to

![img-7.jpeg](img-7.jpeg)

Fig. 7 (Continued)

TABLE II
DISTANCES $D(\mathbf{x}, \mathbf{y})$ OF THE SUB-REGIONS AS SHOWN IN FIG. 2(a)


The highlighted cell indicates the nearest optimal sub-region of a particular sub-region. For example, the nearest optimal sub-region of $h_{2}$ is $h_{1}$; and the nearest optimal sub-region of $h_{4}$ is $h_{5}$.
the adaptive mutation in NrGA, i.e., the UIS, in which an individual is randomly mutated within its sub-region. To make the approximated fitness function locally guide the search in GAS, $l$ should be slightly larger than zero but much smaller than the depth of the fitness tree. In this paper, $l$ is chosen to be 2 . In the special case that $\mathbf{x}$ is the immediate descendant of $\mathbf{r}$, then $l=1$.

Table I lists the active neighborhoods of all sub-regions that appear in Fig. 2. Seen from the table, the sub-regions of nodes $\mathbf{s}_{\mathbf{1}}$ and $\mathbf{s}_{\mathbf{2}}$ are regarded as the optimal sub-regions.

## B. The Nearest Optimal Sub-Region

After locating the optimal sub-regions of the approximated fitness landscape, the mutation direction of a sub-region $X$ is defined as the direction pointing to its nearest optimal subregion. Suppose $Z$ is the optimal sub-region set in $S$. The sub-region $Y \subseteq Z$ is the nearest optimal sub-region of the sub-region $X$ of node $\mathbf{x}$ if the metric $D($.$) from X$ to $Y$ is the minimum amongst the metrics from $X$ to all optimal sub-regions, i.e., $Y=\arg \min _{A \subseteq Z} D(X, A)$. The following metric measures the distance between sub-regions:

Definition 4: Sub-Region Distance $D(X, Y)$
Suppose $X$ and $Y$ are the sub-regions of nodes $\mathbf{x}$ and $\mathbf{y}$, respectively; let the sub-region $P$ of node $\mathbf{p}$ be the smallest sub-region which contains both $X$ and $Y$, i.e., $X, Y \subseteq P$, then the sub-region distance from $X$ to $Y$ is defined as the depth difference between $\mathbf{x}$ and $\mathbf{p}$.

Remark: Sub-region distance is not commutative; unless $\mathbf{x}$ and $\mathbf{y}$ are at the same tree level, the distance from $X$ to $Y$ may not be equivalent to that from $Y$ to $X$.

Remark 2: If node $\mathbf{x}$ is a sibling of node $\mathbf{y}$, the distance from $X$ to any partitioned sub-region $A$ except $X$ and $Y$ is equivalent to the distance from $Y$ to $A$, i.e., $D(X, A)=D(Y$, A) where $A \neq X, Y$.

Referring to the example in Fig. 2, the distances amongst the sub-regions $h_{1}-h_{6}$ and $N_{1}-N_{4}$ are listed in Table II. The highlighted cells indicate the nearest optimal sub-regions of the sub-regions. For example, the nearest optimal subregion of $h_{2}$ is $h_{1}$; and the nearest optimal sub-region of $h_{4}$ is $h_{5}$.
![img-8.jpeg](img-8.jpeg)

Fig. 8. Histogram of optimal population sizes for $f_{1}-f_{10}$ and $f_{15}-f_{34}$.
![img-9.jpeg](img-9.jpeg)

Fig. 9. Histogram of empirical optimal population sizes for $f_{11}-f_{14}$.

## C. Example

In this example, the search space $S$ and the individual sequence (i.e., hence the fitness tree) are the same as the example that appeared in Section III. Suppose $\mathbf{x}$ is an individual to be mutated by GAS, the corresponding mutation starts by searching the sub-region $\mathbf{x}$. In actual programming, the result is obtained by tree node search starting at the root node. Suppose the search is terminated at node $\mathbf{s}_{\mathbf{2}}$ and $h_{2}$ is the sub-region of $\mathbf{x}$. Afterwards, we compute the distances from $h_{2}$ to all optimal sub-regions. According to Table I, the search space consists of two optimal sub-regions: $h_{1}$ and $h_{5}$. The nearest optimal sub-region of $h_{2}$ is $h_{1}$ because $D\left(h_{2}, h_{1}\right)=1<D\left(h_{2}, h_{5}\right)=$ 3 (as listed in Table II). Thus, the mutant of $\mathbf{x}$ is suggested as one of the points lying on the straight line between $\mathbf{x}$ and $\mathbf{s}_{\mathbf{1}}$. The gray line shown in Fig. 4(a) indicates the range of possible mutants. Fig. 4(b) shows the mutation directions at different positions in $S$. Seen from the figure, the directions can be considered as a discrete approximation of the gradient flow of the fitness landscape. Thus, GAS is analogous to the steepest gradient descent with a random learning rate.

## D. Strengths and Weaknesses of GAS

In this section, we analyze the strengths and the weaknesses of GAS while minimizing three typical forms of fitness landscapes shown in Fig. 5. When searching the fitness landscape $\Omega_{1}$ with an unusual spike [Fig. 5(a)], since GAS mutates

TABLE III
AVERAGEd Difference of the COMPutation Time (in SECONDS) Between HdEA and RCGA-UNDX, DE, ODE, DEahCSPX, DPSO and SEPSO: $f_{1}-f_{14}$


individuals based on the local structure of the fitness function, the mutants always move toward the global optimum. Different from the traditional steepest gradient descent method which may either converge slowly when a small step size is used; or oscillates around the spike when a large step size is used; GAS adaptively computes the mutation step size and so HdEA preserves a fast convergence rate no matter how unusual the spike is.

In the case of fitness landscape $\Omega_{2}$ with dense and clustered optimums [Fig. 5(b)], such as the Shekel's Foxholes function [24], the crossover operator in HdEA diversifies individuals and helps them to escape from local optima.

For the fitness landscape $\Omega_{3}$ shown in Fig. 5(c), the success rate of HdEA depends on the selection scheme instead of GAS. Note that $\Omega_{3}$ is a mixture of $\Omega_{2}$ and $\Omega_{3}$. If the search space is divided into two sub-regions (the left and the right subregions), and two independent HdEAs are performed on each of the sub-regions, the global optima of $\Omega_{3}$ should be obtained. However, when only one HdEA is performed, the selection scheme enforces a large portion of population to search the left sub-region, and the search effort on the global optima basin located at the right sub-region is naturally weakened. To tackle this problem, increasing diversity is a possible solution. In other words, given prior knowledge that the structure of fitness function is known to be $\Omega_{3}$, GAS is still helpful to the search when a selection scheme with lower selection pressure is employed.

HdEA mainly derives benefit from the local structure of the approximated fitness function. GAS speeds up the convergence of HdEA as it rapidly reaches the nearest optimum. However, similar to the steepest gradient descent method, GAS sacrifices diversity to exchange for a faster convergence rate.

While dealing with the optimization of noisy and/or highly oscillated function landscapes that consists of densely and/or uniformly distributed local optimas, the corresponding search strategy should concern large-scale structures instead of local structures. Thus, the local optimas may interfere with GAS and occasionally traps the search in a local optimum.

## V. EXPERIMENTAL RESULTS

## A. Test Function Set

A real valued function set $\mathbf{F}=\left\{f_{1}(\mathbf{x}), f_{2}(\mathbf{x}), \ldots, \mathbf{f}_{34}(\mathbf{x})\right\}$ consisting of 34 well-known benchmark functions is employed to evaluate the performance of HdEA. These 34 test functions are as follows.

1. Sphere function [24].
2. Schwefel's problem 2.22 [24].
3. Schwefel's problem 1.2 [24].
4. Schwefel's problem 2.21 [24].
5. Generalized Rosenbrock function [24].
6. Quartic function [24].
7. Generalized Rastrigin function [24].
8. Generalized Griewank function [24].
9. Generalized Schwefel's problem 2.26 [24].
10. Ackley function [24].
11. Shekel's Foxholes function [24].
12. Six-Hump Camel-Back function [24].
13. Branin function [24].
14. Goldstein-Price function [24].
15. High conditioned elliptic function [25].
16. Weierstrass's function [25].
17. Hybrid composition function [25].

TABLE IV
AVERAGEd Difference of the COMPutation Time (in seconds) Between HdEA and RCGA-UNDX, DE, ODE, DEahCSPX, DPSO, and SEPSO: $f_{13}-f_{24}$


TABLE V
AVERAGEd Difference of the COMPutation Time (in seconds) Between HdEA and RCGA-UNDX, DE, ODE, DEahCSPX, DPSO, AND SEPSO: $f_{25}-f_{34}$


18. Levy function [1].
19. Zakharov function [1].
20. Alpine function [1].
21. Pathological function [1].
22. Inverted cosine wave function (Masters) [1].
23. Inverted cosine mixture problem [26].
24. Epistatic Michalewicz problem [26].
25. Levy and Montalvo 2 problem [26].
26. Neumaier 3 problem [26].
27. Odd square problem [26].
28. Paviani problem [26].
29. Periodic problem [26].
30. Salomon problem [26].
31. Shubert problem [26].
32. Sinusoidal problem [26].
33. Michalewicz function [1].
34. Whitely's function [24].

The mathematical forms of these functions are given in Appendix I.

Seven of them are uni-modal functions; the remaining 27 are multimodal functions designed with a considerable amount of local minima. Additionally, the function $f_{6}$ is a noisy function and the function $f_{17}$ is a hybrid composition function. The dimensions of the first ten and the last 20 functions are adjustable while the dimensions of $f_{11}-f_{14}$ are fixed at two, as they are 2-D functions as defined in the original references.

TABLE VI
Considered Combinations of Population Size and the Number of Generations for $f_{1}-f_{10}$ and $f_{15}-f_{34}$


TABLE VII
CONSIDERED COMBINATIONS OF POPULATION SIZE AND THE NUMBER
OF GENERATIONS FOR $f_{11}-f_{14}$

The optimal points of the functions $f_{24}, f_{27}, f_{28}, f_{31}, f_{33}$, and $f_{34}$ are not known. Simulations are carried out to find the global minimum of each function.

## B. Algorithms for Comparison

To evaluate the impact of the proposed algorithm, we compare the optimal fitness found by HdEA with eight benchmark evolutionary algorithms. The designs and settings of HdEA and the algorithms for comparison are summarized below. Simulation settings are given in Section C.

1) Test Algorithm 1-HdEA: HdEA, proposed in this paper, is an evolutionary algorithm that uses the entire search history to improve its mutation strategy. It uses the fitness function approximated from the search history to perform mutation. Since the proposed mutation operator is adaptive and parameter-less, HdEA has only three control parameters: neighborhood size, population size, and crossover rate. In this section, random population initialization, uniform crossover operator and $(\mu+\mu)$ elitism selection are used in EAM of HdEA. Note that HdEA is not limited to these operator settings. Other crossover operators such as arithmetic crossover and $n$-point crossover, and any selection scheme such as proportional selection and tournament selection are also applicable. The neighborhood size is constantly assigned to be two throughout this section. The source code of HdEA is available at http://www.ee.cityu.edu.hk/ syyuen/Public/Code.html
2) Test Algorithm 2—Real Coded GA With Uni-Modal Normal Distribution Crossover (RCGA-UNDX): RCGA-UNDX [27] is a real coded GA that deals with continuous search spaces. It applies the uni-modal normal distribution crossover (UNDX) to preserve the statistics of the population. UNDX
is a multiparent genetic operator in which the distribution of the corresponding offspring follows the distribution of the parents.
3) Test Algorithm 3-Covariance Matrix Adaptation Evolution Strategy (CMA-ES) [28]: CMA-ES is an evolution strategy that adapts the full covariance matrix of a normal search (mutation) distribution. An important property of CMAES is its invariance against linear transformations of the search space. The underlying idea is to gather information about successful search steps to modify the covariance matrix of the mutation distribution in a de-randomized, goal directed fashion. Changes to the covariance matrix are such that variances in directions of the search space that have previously been successful are increased, while those in other directions decrease passively. The accumulation of information over a number of search steps makes it possible to reliably adapt the covariance matrix even when using small populations. CMAES is designed with the emphasis that the same parameters are used in all applications in order to be "parameter-less." The source code of CMA-ES is taken from [28] (Aug. 2007 version).
4) Test Algorithm 4-DE: Differential evolution [4], [5] is a stochastic search algorithm. The basic idea behind DE is a scheme that generates trial parameter vectors. DE adds the weighted difference between two population vectors to a mutant vector, and the trial vector is the crossover between the mutant vector and the parent vector. By doing so, no separate probability distribution is used, which makes the scheme completely self-organizing.
5) Test Algorithm 5-Opposition-Based Differential Evolution (ODE) [29]: Opposition-based differential evolution utilizes the concept of opposition-based learning (OBL) [30] to accelerate the convergence rate of DE. The main idea behind OBL is the simultaneous considerations of a solution and its corresponding opposite solution. ODE considers the evaluations of the opposite solution in a generation depending on a jumping rate.
6) Test Algorithm 6-Differential Evolution With Adaptive Hill-Climbing Simplex Crossover (DEahcSPX): DEahcSPX [31] attempts to accelerate the classic DE by a local search strategy, named adaptive hill-climbing crossover-based local search. It adopts the simplex crossover operation (SPX) [32] to generate offspring individual for hill-climbing.
7) Test Algorithm 7-Dissipative Particle Swarm Optimization (DPSO): DPSO [2] is a modified PSO which introduces random mutation that helps particles to escape from local minima. Its formula is described as follows:

$$
\text { If } \eta_{3}<C_{v} \text { then } v_{i}=\eta_{4} \times V_{\max } / C_{m}
$$

where $\eta_{3}$ and $\eta_{4}$ are uniformly distributed random variables in the range $[0,1], C_{v}$ is the mutation rate to control the velocity, $C_{m}$ is a constant to control the extent of mutation, and $V_{\max }$ is the maximum velocity.
8) Test Algorithm 8-PSO With Spatial Particle Extension (SEPSO): SEPSO [33] is another modified PSO which introduces the spatial particle extension model to increase the diversity. When particles start to cluster and collide, they bounce off by adjusting their velocities.

9) Test Algorithm 9-EDA: The tested EDA is based on undirected graphical model and Bayesian network. The source code of the EDA is taken from [34] (Feb. 2009 version). The implementation is conceived to allow the user different combinations of selection, learning, sampling, and local search procedures [35].

## C. Simulation Settings

The parameter settings of the test algorithms for all conducted experiments are as follows.

For HdEA, the crossover rate is set to 0.1 . The population sizes are chosen to be 20 .

For the rest of the algorithms, we use the same parameter settings as that recommended in the original literature

For RCGA-UNDX, the crossover rate is set to 0.1 . The UNDX operator is in the three-parent mode. For uni-modal test functions (i.e., $f_{1}-f_{6}$ ), the population size is chosen to be 50. For multimodal test functions (i.e., $f_{7}-f_{34}$ ), the population size is chosen to be 300 . These parameters (i.e., the number of parents for UNDX and the population size of RCGA-UNDX) are suggested in [27].

For CMA-ES, the population size $\lambda$ is chosen by the suggested setting in [28] (i.e., $\lambda=4+\lfloor 3 \ln D\rfloor$ ). The remaining parameters used in CMA-ES are chosen to be the predefined values in [28].

For DE and ODE, the crossover rate and the differential amplification factor are set to 0.95 and 0.5 , respectively. These values have been used in literature [5], [36]-[38], [39]. The mutation strategy is DE/rand/1/bin (classic version of DE) [5], [38], [40], [41]. The jumping rate constant of ODE is chosen to be 0.3 [29]. The population sizes of DE and ODE are assigned as 100 [29] for all test functions.

For DEahcSPX, the crossover rate and the differential amplification factor are selected as 0.9 and 0.9 , respectively [31]. The population size $\lambda$ of DEahcSPX is assigned as the dimension of test function, i.e., $\lambda=D$. The number of parents participating in SPX, as suggested in [32], is chosen to be 3 .

For DPSO and SEPSO, the values of $c_{1}, c_{2}$ are set to 2 . The inertia $w$ is linearly decreasing from 0.9 to 0.4 . The swarm sizes are set to 20 . Suppose $S=\prod_{i=1}^{D}\left\{L_{i}, U_{i}\right\}$ is the search space of a $D$-dimensional test function, where $L_{i}$ and $U_{i}$ are the lower and upper limits in the $i$ th dimension, the maximum velocity $V_{\max }$ is set to $0.1 R$ where $R=\max _{i \in\{1, D\}}\left(U_{i}-L_{i}\right)$. The parameters $C_{v}$ and $C_{m}$ of DPSO are chosen to be 0.001 and 0.002 , respectively. For SEPSO, a simple velocity line bouncing with bouncing factor -1 is used. These parameter settings are recommended in the original works [2], [33].

For EDA, the selection scheme is $(\mu+\mu)$ elitism selection. The offspring population is sampled by probabilistic logic sampling. The parameters of these operators are chosen to be the values suggested in the source code.

To provide a fair comparison amongst the test algorithms, the total number of function evaluations of all algorithms is kept a constant: For functions $f_{1}-f_{10}$ and $f_{15}-f_{34}$, the total number of fitness evaluations of all test algorithms is fixed
at 40000 . For functions $f_{11}-f_{14}$, the total number of fitness evaluations is fixed at 1000 .

All test functions with the exception of $f_{11}-f_{14}$, which are 2-D, are tested with dimensions 30 and 40 . Since the test algorithms are stochastic, their performances on each test function are evaluated based on statistics obtained from 100 independent runs. All simulations are performed on a PC with 3.2 GHz central processing unit and 1 GB memory. All test algorithms except CMA-ES and EDA (HdEA, RCGA-UNDX, DE, ODE, DEahcSPX, DPSO, and SEPSO) are implemented in C language. CMA-ES uses source code in [28] and MATLAB version 6.1. EDA uses source code in [34] and MATLAB version 6.1.

## D. Simulation Results

In this section, we first observe the performance in terms of accuracy (quality of the averaged best found fitness) of HdEA in comparison with RCGA-UNDX, CMA-ES, DE, ODE, DEahcSPX, DPSO, SEPSO, and EDA. To be a practical solution to real world problems, the processing time of HdEA should be within a reasonable range. Thus, the average processing time is also observed. Finally, the influence of population size to the performance of HdEA is observed.

The average and the standard deviation (inside brackets) of the optimal fitness for 100 trials are presented in Tables VIIIXV. In Tables III-V, the averaged differences of the computation time between HdEA and RCGA-UNDX, DE, ODE, DEahcSPX, DPSO, and SEPSO are presented. In Fig. 10, the performance of HdEA with various population sizes is presented.

1) Accuracy: Fig. 6 presents a summary of the results. The shaded cells in Fig. 6 indicate that the corresponding test algorithm is the best algorithm on a particular test function at a particular function dimension. The values inside the table cells for HdEA indicate the ranking of HdEA on a particular test function at a particular function dimension when it is not the best algorithm. It can be observed that HdEA outperforms the other test algorithms: HdEA ranks first (or joint first) in 31 and is second in nine out of a total of 64 cases. Fig. 7 shows the histogram of the ranking amongst the test algorithms in the 64 test cases.

The detailed simulation results (mean and standard deviation) are listed in Tables VIII-XV in Appendix II. It lists the average and the standard deviation (inside brackets) of the optimal fitness for 100 independent trials. A value in boldface indicates that the corresponding algorithm is the best amongst the test algorithms on a particular test function at a particular function dimension. To illustrate the significance of the indicator in Fig. 6, the confidence levels $C$ (in terms of \%) for $t$-tests comparing the averaged optimal fitness values of HdEA with other algorithms are listed. In the tables, a larger confidence level infers a higher significance of a comparison result.

The significance of the rank of HdEA (i.e., HdEA ranks first (or joint first) in 31 and is second in nine out of a total of 64 cases) is summarized as follows. We are $99.95 \%$ confident that HdEA performs the best amongst all test algorithms in

21 test cases. For the remaining ten test cases that HdEA ranks or jointly ranks first, two out of them are with $99 \%$ confidence level, one out of them is with $97.5 \%$ confidence level, three out of them are with $95 \%$ confidence level, two out of them are with $80 \%$ confidence level, and the remaining two cases are with less than $50 \%$ confidence level. For the nine test cases that HdEA ranks second, eight out of them are with $99.95 \%$ confidence level and the remaining one is with $99.75 \%$ confidence level. From the above, we conclude that the comparisons of HdEA with other algorithms are statistically significant.

Fig. 7 shows the histograms of the ranks of the test algorithms on the 64 test cases. Seen from figure, nearly $80 \%$ of HdEA results are in the first four ranks. It shows the consistent and superior performance of HdEA amongst the test algorithms. For ODE, its performance is also consistent but not as good as HdEA. On the other hand, for CMA-ES which is the second best (in terms of the number of test cases with first rank) test algorithm, around $69 \%$ of CMA-ES results are ranked lower or equal to fourth. In addition, it performs the worst amongst the test algorithms in eight out 64 test cases. Thus, though the number of first ranked test cases of CMA-ES is just slightly lower than that of HdEA, the number of worst ranked test cases of CMA-ES is much more than that of HdEA (i.e., eight for CMA-ES and none for HdEA). We conclude that HdEA is superior to CM-ES in terms of consistency.
2) Processing Time: During the search process, an algorithm spends its computation resources on either solution generation or function evaluation. Different algorithms use different strategies to generate trial solutions, so the corresponding processing times are different. HdEA spends most computation on recording the evaluated solutions (i.e., BSP tree node insertion) and performing GAS. RGA-UNDX and DEahcSPX spend computations on their specific crossover operators. Comparing with DE that employs simple vector addition to generate trial vectors, ODE involves additional processes such as triggering the opposition-based learning and the generation of opposite solutions. CMA-ES generates new candidate solutions according to the covariance matrix of the multivariate normal mutation distribution. DPSO checks if any particle should be re-initialized. For SEPSO, path tracking is required for detecting the possible collisions amongst the swarm. EDA estimates the probability distribution of the evaluated solutions and generates new candidate solutions based on it. As a practical solution to real world applications, the processing time of HdEA should be within an acceptable range. In this section, the computation load of an algorithm, in terms of processing time, is studied.

Tables III-V list the averaged differences of the computation time (in second) between HdEA and RCGA-UNDX, DE, ODE, DEahcSPX, DPSO, and SEPSO for $f_{1}-f_{34}$. The comparisons with CMA-ES and EDA are not made since they are implemented in MATLAB. A negative value indicates that the corresponding test algorithm is slower than HdEA for a particular function at a particular dimension. Seen from the tables, HdEA is faster than RCGA-UNDX
for all test cases except that it is just 0.00312 seconds and 0.00015 seconds slower than RCGA-UNDX for $f_{11}$ and $f_{12}$, respectively. Comparing with SEPSO, HdEA is faster at all high-dimensional test cases (i.e., $D=30$ and 40) except for $f_{16}, f_{17}$, and $f_{34}$ which are relatively time consuming. For the low-dimensional test cases (i.e., $D=2$ ), the overheads of HdEA are in a small range from 0.0022 seconds to 0.01219 seconds. Though HdEA spends more computation time than DE ODE, DEahcSPX, and DPSO for all test cases; the corresponding overheads range from 0.00095 seconds to 7.3084 seconds; but its performance is better than those of DE, ODE, DEahcSPX, and DPSO in 60, 38, 43, and 52 out of 64 test cases, respectively. Moreover, it should be emphasized that, for real world applications involving expensive and/or time consuming fitness evaluations, such as surface registration [42], optimized design and energy management of heating, ventilating and air conditioning systems [43]-[45], function evaluations are much more expensive and/or time consuming than solution generation. For such applications, the overhead of HdEA, of maximum a few more seconds, is insignificant.
3) Influence of Population Size: In this experiment, we examine the performance of HdEA for different population sizes but fixed number of fitness evaluations. For the test functions $f_{1}-f_{10}$ and $f_{15}-f_{34}$, the population size is varied from 2 to 20000 . Table VI lists the combinations of population size $\mu$ and the number of generations $N_{g}$. The total numbers of fitness evaluations for these functions are fixed at 40000 .

For the test functions $f_{11}-f_{14}$, the population size is varied from 2 to 500 . Table VII lists the combinations of $\mu$ and $N_{g}$. The total numbers of fitness evaluations are 1000 .

The remaining parameter settings for this experiment are as follows.

1) Crossover operator $=$ uniform crossover.
2) Crossover rate $=0.1$.
3) Selection scheme $=(\mu+\mu)$ elitism selection.
4) Dimensions $D$ of the test functions: $D=30$ for $f_{1}-f_{10}$ and $f_{15}-f_{34}$, and $D=2$ for $f_{11}-f_{14}$.

Fig. 8 shows the frequencies of the empirical optimal population sizes for $f_{1}-f_{10}$ and $f_{15}-f_{34}$. Fig. 9 shows the frequencies of the optimal population sizes for $f_{11}-f_{14}$. Seen from the figures, we should employ a small population size ranging from for 2 to 100 for both low and high-dimensional fitness functions when the number of fitness evaluations is fixed.

Fig. 10 in Appendix III shows the averaged best fitness found by HdEA against population size for $f_{1}-f_{34}$. The $x$-axis is in log scale. Seen from the figure, the relation between population size and averaged best fitness can be divided into three cases. For the first case, the averaged best fitness monotonically increases along with population size. The corresponding curve vaguely resembles a sigmoid function. The averaged best fitness of HdEA is insensitive to the population size $\mu$ in the range between 2 and 100. When $\mu$ further increases beyond this range, the corresponding fitness value monotonically increases and converges to a certain value. Twenty seven out of the 34 test functions

$\left(f_{1}-f_{10}, f_{14}-f_{18}, f_{20}-f_{26}, f_{28}-f_{30}\right.$, and $\left.f_{33}-f_{34}\right)$ have similar scenarios.

For the second case, the relation between the averaged best fitness and population size is in the form of a convex function. Six test functions $\left(f_{11}-f_{13}, f_{27}, f_{31}\right.$, and $f_{32}$ ) belong to this scenario and the corresponding optimal population sizes are in a small range from 50 to 200.

For the remaining test function $f_{19}$, the proper selection of population size is critical to the accuracy of HdEA. The curve of $f_{19}$ shown in Fig. 10 is oscillating: it is neither monotonically increasing, monotonically decreasing, concave, nor convex.

## VI. CONCLUSION

In this paper, we propose a new evolutionary algorithm that adaptively guides mutation by the entire previous search history. This evolutionary search, namely HdEA, integrates an evolutionary algorithm with a binary space partitioning tree that encodes the search history. Moreover, we employ the tree to approximate the fitness function, and use the approximated function to derive a parameter-less, adaptive, and guided mutation. This mutation somewhat resembles the gradient descent in classical optimization methods, but the step size is random and interesting, the maximum step size is parameter-less and is a function of the entire search history. HdEA has the following properties.

1) Because of the partitioning scheme, the neighborhoods of the evaluated solutions follow the topology of fitness tree; a fast fitness function approximation is obtained.
2) The proposed adaptive mutation in HdEA suggests both the direction and the magnitude of the mutation vector in a parameter-less manner.
3) The adaptive mutation naturally avoids the out-of-bound solution problem in bounded real valued optimization algorithms.
4) It is empirically suggested that HdEA performs well with small population size (i.e., 40 to 100 individuals for a 40 -dimensional function).
In the experiment section, we examine HdEA on 34 benchmark problems, including both uni-modal and multimodal functions. The dimensions of the test functions are from 2 to 40 . We compare the performance of HdEA with eight benchmark real coded evolutionary algorithms. It is found that for multimodal functions, HdEA outperforms all the other algorithms, while it does not perform as well for uni-modal functions. This suggests that HdEA should be used in the optimization of multimodal functions, which represents the harder and more challenging application problems.

Possible directions for future work include applying other function approximation methods (e.g., parametric model fitting and neural network) and extending the usage of the whole search history (e.g., cooperative mutation strategy and parameter controls such as adaptive crossover rate and adaptive selection pressure).

## APPENDIX I

1. Sphere function [24]

$$
f_{1}(\mathbf{x})=\sum_{i=1}^{D} x_{i}^{2}
$$

where $\mathbf{x} \in[-100,100]^{D}$

$$
\min _{\mathbf{x}} f(\mathbf{x})=f_{1}([0,0, \cdots, 0])=0
$$

2. Schwefel's problem 2.22 [24]

$$
f_{2}(\mathbf{x})=\sum_{i=1}^{D}\left|x_{i}\right|+\prod_{i=1}^{D}\left|x_{i}\right|
$$

where $\mathbf{x} \in[-10,10]^{D}$

$$
\min _{\mathbf{x}} f_{2}(\mathbf{x})=f_{2}([0,0, \cdots, 0])=0
$$

3. Schwefel's problem 1.2 [24]

$$
f_{3}(\mathbf{x})=\sum_{i=1}^{D}\left(\sum_{j=1}^{i} x_{j}\right)^{\frac{1}{2}}
$$

where $\mathbf{x} \in[-100,100]^{D}$

$$
\min _{\mathbf{x}} f_{3}(\mathbf{x})=\mathbf{f}_{3}([\mathbf{0}, \mathbf{0}, \cdots, \mathbf{0}])=\mathbf{0}
$$

4. Schwefel's problem 2.21 [24]

$$
f_{4}(\mathbf{x})=\max _{i \in[1, D]}\left|x_{i}\right|
$$

where $\mathbf{x} \in[-100,100]^{D}$

$$
\min _{\mathbf{x}} f_{4}(\mathbf{x})=\mathbf{f}_{4}([\mathbf{0}, \mathbf{0}, \cdots, \mathbf{0}])=\mathbf{0}
$$

5. Generalized Rosenbrock function [24]

$$
f_{5}(\mathbf{x})=\sum_{i=1}^{D-1}\left[100\left(x_{i+1}-x_{i}^{2}\right)^{2}+\left(x_{i}-1\right)^{2}\right]
$$

where $\mathbf{x} \in[-29,31]^{D}$

$$
\min _{\mathbf{x}} f_{5}(\mathbf{x})=f_{5}([1,1, \cdots, 1])=0
$$

6. Quartic function [24]

$$
f_{6}(\mathbf{x})=\sum_{i=1}^{D} i x^{4}+\operatorname{random}[0,1]
$$

where $\mathbf{x} \in[-1.28,1.28]^{D}$

$$
\min _{\mathbf{x}} f_{6}(\mathbf{x})=f_{6}([0,0, \cdots, 0])=0
$$

Note: This is a noisy fitness function. There is a random measurement noise in each fitness evaluation.
7. Generalized Rastrigin function [24]

$$
f_{7}(\mathbf{x})=\sum_{i=1}^{D}\left[x_{i}^{2}-10 \cos \left(2 \pi x_{i}\right)+10\right]
$$

where $\mathbf{x} \in[-5.12,5.12]^{D}$

$$
\min _{\mathbf{x}} f_{7}(\mathbf{x})=f_{7}([0,0, \cdots, 0])=0
$$

8. Generalized Griewank function [24]

$$
f_{8}(\mathbf{x})=\frac{1}{4000} \sum_{i=1}^{D} x_{i}^{2}-\prod_{i=1}^{D} \cos \frac{x_{i}}{\sqrt{ }}+1
$$

where $\mathbf{x} \in[-600,600]^{D}$

$$
\min _{\mathbf{x}} f_{\mathbf{x}}(\bar{x})=f_{8}([0,0, \cdots, 0])=0
$$

9. Generalized Schwefel's problem 2.26 [24]

$$
f_{9}(\mathbf{x})=-\sum_{i=1}^{D} x_{i} \sin \sqrt{\left|x_{i}\right|}
$$

where $\mathbf{x} \in[-500,500)^{D}$

$$
\min _{\mathbf{x}} f_{9}(\mathbf{x})=f_{9}([420.9687, \cdots, 420.9687])=-418.9829 D
$$

10. Ackley function [24]

$$
\begin{aligned}
& f_{10}(x)=-20 \exp \left(-0.2 \sqrt{\frac{1}{D} \sum_{i=1}^{D} x_{i}^{2}}\right)- \\
& \exp \left(\frac{1}{D} \sum_{i=1}^{D} \cos 2 \pi x_{i}\right)+20+e
\end{aligned}
$$

where $\mathbf{x} \in[-32,32]^{D}$ and $\min _{\mathbf{x}} f_{10}(\mathbf{x})=f_{10}([0,0, \cdots, 0])=0$.
11. Shekel's Foxholes function [24]

$$
f_{11}(\mathbf{x})=\left[\begin{array}{c}
1 \\
\frac{1}{500}+\sum_{j=1}^{25} \frac{1}{j x \sum_{i=1}^{2}\left(x_{i}-a_{i, j}\right)^{p}} \\
-98,34
\end{array}\right]
$$

where $\mathbf{x} \in[-98,34]^{2}$ and

$$
\begin{gathered}
\left\{a_{i, j}\right\}=\left[\begin{array}{cccc}
-32-16 & 0 & 16 & 32-32 \cdots 01632 \\
-32-32-32-32-32-16 & \cdots & 323232
\end{array}\right] \\
\min _{\mathbf{x}} f_{11}(\mathbf{x})=f_{11}([-32,-32]) \approx 1
\end{gathered}
$$

12. Six-hump Camel-Back function [24]

$$
f_{12}(\mathbf{x})=4 x_{1}^{2}-2.1 x_{1}^{4}+\frac{1}{3} x_{1}^{6}+x_{1} x_{2}-4 x_{2}^{2}+4 x_{2}^{4}
$$

where $\mathbf{x} \in[-4.91017,5.0893] \times[-5.7126,4.2874]$ and

$$
\begin{aligned}
& \min _{x} f_{12}(\mathbf{x})=f_{12}([0.08983,-0.7126])= \\
& f_{12}([-0.08983,0.7126])=-1.0316285
\end{aligned}
$$

13. Branin function [24]

$$
f_{13}(\mathbf{x})=\left(x_{2}-\frac{5}{4 \pi^{2}} x_{1}^{2}+\frac{5}{\pi} x_{1}-6\right)^{2}+10\left(1-\frac{1}{8 \pi}\right) \cos x_{1}+10
$$

where $\mathbf{x} \in[-8.142,6.858] \times[-12.275,2.725]$ and

$$
\begin{gathered}
\min _{\mathbf{x}} f_{13}(\mathbf{x})=f_{13}([-3.142,12.275])=f_{13}([3.142,2.275])= \\
f_{13}([9.425,2.425])=0.398
\end{gathered}
$$

14. Goldstein-Price function [24]

$$
f_{14}(\mathbf{x})=g(\mathbf{x}) \times h(\mathbf{x})
$$

where
$g(\mathbf{x})=1+\left(x_{1}+x_{2}+1\right)^{2}\left(19-14 x_{1}+3 x_{1}^{2}-14 x_{2}+6 x_{1} x_{2}+3 x_{2}^{2}\right)$
$h(\mathbf{x})=30+\left(2 x_{1}-3 x_{2}\right)^{2}\left(18-32 x_{1}+12 x_{1}^{2}+48 x_{2}-36 x_{1} x_{2}+27 x_{2}^{2}\right)$
$\mathbf{x} \in[-2,2] \times[-3,1]$ and $\min _{x} f_{14}(\mathbf{x})=f_{14}([0,-1])=3$.
15. High conditioned elliptic function [25]

$$
f_{15}(\mathbf{x})=\sum_{i=1}^{D} 10^{\frac{(i-1)}{D-1}} z_{i}^{2}
$$

where $\mathbf{x} \in[-100,100]^{D}$ and

$$
\min _{\mathbf{x}} f_{15}(\mathbf{x})=f_{15}([-100,-100, \ldots,-100])=0
$$

16. Weierstrass's function [25]

$$
f_{16}(\mathbf{x})=\sum_{i=1}^{D} \sum_{k=0}^{D} a^{k} \cos \left(2 \pi b^{k}\left(z_{i}-0.5\right)\right)-D \sum_{i=1}^{D} a^{k} \cos \left(\pi b^{k}\right)
$$

where $\mathbf{x} \in[-0.5,0.5]^{D}$ and $\min _{\mathbf{x}} f_{16}(\mathbf{x})=f_{16}([0, \ldots, 0])=0$.
17. Hybrid composition function [25]

$$
f_{17}(\mathbf{x})=\sum_{i=1}^{10} w_{i}\left(g_{i}\left(\lambda_{i}\left(\mathbf{x}-\mathbf{o}_{\mathbf{i}}\right)\right)+b_{i}\right)
$$

where

$$
\begin{aligned}
& \mathbf{o}_{\mathbf{i}}=\left\{o_{i, j}\right\} \\
& g_{i}\left(\lambda_{i} \mathbf{x}\right)=C \times \frac{h_{i}\left(\lambda_{i} \mathbf{x}\right)}{h_{i}\left(\lambda_{i}[5,5, \ldots, 5]\right)} \\
& h_{1-2}(\mathbf{x})=f_{7}(\mathbf{x}) \\
& h_{3-4}(\mathbf{x})=f_{16}(\mathbf{x}) \\
& h_{5-6}(\mathbf{x})=f_{8}(\mathbf{x}) \\
& h_{7-8}(\mathbf{x})=f_{10}(\mathbf{x}) \\
& h_{9-10}(\mathbf{x})=f_{1}(\mathbf{x}) \\
& w_{i}=\exp \left(-\sum_{j=1}^{D} \frac{\left(x_{j}-o_{i, j}\right)^{2}}{2 D \sigma_{j}^{2}}\right)
\end{aligned}
$$

$\sigma_{j}=1$ for $j=1,2, \ldots, D$
$\lambda_{i}=\left[1,1,0.1,0.1,12,12,6.4,6.4,20,20\right]$
$b_{i}=\left[0,100,200,300,400,500,600,700,800,900\right]$
$\mathbf{o}_{\mathbf{i}}=\left[u_{i}, u_{i}, \ldots, u_{i}\right]$ where $u_{i}=0.5 \times \operatorname{floor}(i / 2)$
$C=2000$
$\mathbf{x} \in[-5,5]^{D}$ and $\min _{x} f_{17}(\mathbf{x})=f_{17}([0, \ldots, 0])=4500$.
18. Levy function [1]

$$
\begin{gathered}
f_{18}(\mathbf{x})=\sin ^{2}\left(\pi x_{1}\right)+\sum_{i=1}^{D-1}\left(x_{i}-1\right)^{2}\left(1+10 \sin ^{2}\left(\pi x_{i+1}\right)\right)+ \\
\left(x_{n}-1\right)^{2}\left(1+10 \sin ^{2}\left(2 \pi x_{n}\right)\right)
\end{gathered}
$$

where $y_{i}=1+\frac{x_{i}-1}{4}$ and $\mathbf{x} \in[-10,10]^{D}$ and $\min _{\mathbf{x}} f_{18}(\mathbf{x})=$ $f_{18}([1, \ldots, 1])=0$.
19. Zakharov function [1]

$$
f_{19}(\mathbf{x})=\sum_{i=1}^{D} x_{i}^{2}+\left(\sum_{i=1}^{D} 0.5 i x_{i}\right)^{2}+\left(\sum_{i=1}^{D} 0.5 i x_{i}\right)^{4}
$$

where $\mathbf{x} \in[-5,10]^{D}$ and $\min _{\mathbf{x}} f_{19}(\mathbf{x})=f_{19}([0, \ldots, 0])=0$.
20. Alpine function [1]

$$
f_{20}(\mathbf{x})=\sum_{i=1}^{D}\left|x_{i} \sin \left(x_{i}\right)+0.1 x_{i}\right|
$$

where $\mathbf{x} \in[-10,10]^{D}$ and $\min _{\mathbf{x}} f_{20}(\mathbf{x})=f_{20}([0, \ldots, 0])=0$.
21. Pathological function [1]

$$
f_{21}(\mathbf{x})=\sum_{i=1}^{D-1}\left(0.5+\frac{\sin ^{2} \sqrt{100 x_{i}^{2}+x_{i+1}^{2}}-0.5}{1+0.001\left(x_{i}^{2}-2 x_{i} x_{i+1}+x_{i+1}^{2}\right)^{2}}\right)
$$

where $\mathbf{x} \in[-100,100]^{D}$ and $\min _{x} f_{21}(\mathbf{x})=f_{21}([0, \ldots, 0])=0$.
22. Inverted cosine wave function (Masters) [1]

$$
\begin{aligned}
f_{22}(\mathbf{x})= & -\sum_{i=1}^{D-1}\left(\exp \left(\frac{-\left(x_{i}^{2}+x_{i+1}^{2}+0.5 x_{i} x_{i+1}\right)}{\mathrm{S}}\right) \times\right. \\
& \left.\cos \left(4 \sqrt{x_{i}^{2}+x_{i+1}^{2}+0.5 x_{i} x_{i+1}}\right)\right)
\end{aligned}
$$

where $\mathbf{x} \in[-5,5]^{D}$ and $\min _{x} f_{22}(\mathbf{x})=f_{22}([0, \ldots, 0])=-D+1$.
23. Inverted cosine mixture problem [26]

$$
f_{23}(\mathbf{x})=0.1 D-\left(0.1 \sum_{i=1}^{D} \cos \left(5 \pi x_{i}\right)-\sum_{i=1}^{D} x_{i}^{2}\right)
$$

where $\mathbf{x} \in[-1,1]^{D}$ and $\min _{x} f_{23}(\mathbf{x}) \approx f_{23}([0, \ldots, 0])=0$.
24. Epistatic Michalewicz problem [26]

$$
f_{24}(\mathbf{x})=-\sum_{i=1}^{D} \sin \left(y_{i}^{2}\right) \sin ^{2 m}\left(\frac{i y_{i}^{2}}{\pi}\right)
$$

where $y_{i}=\left\{\begin{array}{cl}x_{i} \cos \theta-x_{i+1} \sin \theta & i=1,3,5 \ldots<n \\ x_{i} \sin \theta+x_{i+1} \cos \theta & i=2,4,6 \ldots<n \\ x_{i} & i=n\end{array}\right.$
$m=10, \theta=\pi / 6$ and $\mathbf{x} \in[0, \pi]^{D}$.
25. Levy and Montalvo 2 problem [26]

$$
\begin{gathered}
f_{25}(\mathbf{x})=0.1\left(\sin ^{2}\left(3 \pi x_{1}\right)+\sum_{i=1}^{D-1}\left(x_{i}-1\right)^{2}\left(1+10 \sin ^{2}\left(3 \pi x_{i+1}\right)\right)+\right. \\
\left.\left(x_{n}-1\right)^{2}\left(1+10 \sin ^{2}\left(2 \pi x_{n}\right)\right)\right)
\end{gathered}
$$

where $\mathbf{x} \in[-5,5]^{D}$ and $\min _{x} f_{25}(\mathbf{x})=f_{25}([1, \ldots, 1])=0$.
26. Neumaier 3 problem [26]

$$
f_{26}(\mathbf{x})=\sum_{i=1}^{D}\left(x_{i}-1\right)^{2}-\sum_{i=2}^{D} x_{i} x_{i-1}
$$

where $\mathbf{x} \in\left[-\mathrm{D}^{2}, D^{2}\right] D^{2}$ and $\min _{\mathbf{x}} f_{26}(\mathbf{x})=f_{26}\left(\mathbf{x}_{0}\right)=$ $-\frac{(\ln D+1)(D-1)}{6}, x_{0, i}=i(D+1-i)$.
27. Odd square problem [26]

$$
f_{27}(\mathbf{x})=-\left(1+\frac{0.2 n}{N+0.1}\right) \cos (N \pi) e^{-\frac{N}{2 \pi}}
$$

where

$$
n=\sqrt{\sum_{i=1}^{D}\left(x_{i}-b_{i}\right)^{2}}, N=\sqrt{D} \max _{i \in[1, D]}\left|x_{i}-b_{i}\right|
$$

$\mathbf{b}=[1,1.3,0.8,-0.4,-1.3,1.6,-2,-6,0.5,1.4,1,1.3, \ldots]$
and $\mathbf{x} \in[-15,15]^{D}$.
28. Paviani problem [26]

$$
f_{28}(\mathbf{x})=\sum_{i=1}^{D}\left[\left(\ln \left(x_{i}-2\right)\right)^{2}+\left(\ln \left(10-x_{i}\right)\right)^{2}\right]-\left(\prod_{i=1}^{D} x_{i}\right)^{0.2}
$$

where $\mathbf{x} \in[2,10]^{D}$.
29. Periodic problem [26]

$$
f_{29}(\mathbf{x})=1+\sum_{i=1}^{D}\left(\sin x_{i}\right)^{2}-0.1 \prod_{i=1}^{D} \exp \left(-x_{i}^{2}\right)
$$

where $\mathbf{x} \in[-10,10]^{D}$ and $\min _{\mathbf{x}} f_{29}(x)=f_{29}([0, \ldots, 0])=0.9$.
30. Salomon problem [26]

$$
f_{30}(\mathbf{x})=1-\cos \left(2 \pi \sqrt{\sum_{i=1}^{D} x_{i}^{2}}\right)+0.1 \sqrt{\sum_{i=1}^{D} x_{i}^{2}}
$$

where $\mathbf{x} \in[-100,100]^{D}$ and $\min _{\mathbf{x}} f_{30}(\mathbf{x})=f_{30}([0, \ldots, 0])=0$.
31. Shubert problem [26]

$$
f_{31}(\mathbf{x})=\prod_{i=1}^{D}\left(\sum_{j=1}^{5} j \cos \left((j+1) x_{i}+j\right)\right)
$$

where $\mathbf{x} \in[-10,10]^{D}$ and $\min _{\mathbf{x}} f_{31}(\mathbf{x}) \approx-186.7309$.
32. Sinusoidal problem [26]

$$
f_{32}(\mathbf{x})=-\left[A \prod_{i=1}^{D} \sin \left(\frac{\left(x_{i}-z\right) \pi}{180}\right)+\prod_{i=1}^{D} \sin \left(\frac{B\left(x_{i}-z\right) \pi}{180}\right)\right]
$$

where $A=2.5, B=5, z=30, \mathbf{x} \in[0,180]^{D}$
and $\min _{\mathbf{x}} f_{32}(\mathbf{x})=f_{32}([90+z, \ldots, 90+z])=-(A+1)$.
33. Michalewicz function [1]

$$
f_{33}(\mathbf{x})=-\sum_{i=1}^{D}\left(\sin \left(x_{i}^{2}\right) \sin ^{2 m}\left(\frac{i x_{i}^{2}}{\pi}\right)\right)
$$

where $m=10$ and $\mathbf{x} \in[0, \pi]^{D}$.
34. Whitely's function [24]

$$
f_{34}(\mathbf{x})=\sum_{j=1}^{D} \sum_{i=1}^{D}\left(\frac{y_{i, j}}{4000}-\cos \left(y_{i, j}\right)+1\right)
$$

where $y_{i, j}=100\left(x_{j}-x_{i}^{2}\right)^{2}+\left(1-x_{i}\right)^{2}$ and $\mathbf{x} \in[-100$, 100$]^{D}$.

# APPENDIX II 

TABLE VIII
AVERAGE, STANDARD DEVIATION, AND CONFIDENCE LEVEL OF THE BEST FITNESS VALUES FOUND BY HdEA, RCGA-UNDX, CMA-ES, DE, ODE, DEAhCSPX, DPSO, SEPSO, AND EDA: $f_{3}-f_{4}$

TABLE IX
AVERAGE, STANDARD DEVIATION, AND CONFIDENCE LEVEL OF THE BEST FITNESS VALUES FOUND BY HdEA, RCGA-UNDX, CMA-ES, DE, ODE, DEAhCSPX, DPSO, SEPSO, AND EDA: $f_{5}-f_{8}$

TABLE X
AverAGE, Standard Deviation, and CONFIDENCE LeVEl of the Best Fitness Values Found by HdEA, RCGA-UNDX, CMA-ES, DE, ODE, DEahCSPX, DPSO, SEPSO AND EDA: $f_{9}-f_{14}$

TABLE XI
Average, Standard Deviation, and Confidence LeVEl of the Best Fitness Values Found by HdEA, RCGA-UNDX, CMA-ES, DE, ODE, DEahCSPX, DPSO, SEPSO, AND EDA: $f_{15}-f_{18}$

TABLE XII
AVERAGE, STANDARD DEVIATION, AND CONFIDENCE LEVEL OF THE BEST FITNESS VALUES FOUND BY HdEA, RCGA-UNDX, CMA-ES, DE, ODE, DEahCSPX, DPSO, SEPSO, AND EDA: $f_{19}-f_{22}$


TABLE XIII
AVERAGE, STANDARD DEVIATION, AND CONFIDENCE LEVEL OF THE BEST FITNESS VALUES FOUND BY HdEA, RCGA-UNDX, CMA-ES, DE, ODE, DEahCSPX, DPSO, SEPSO, AND EDA: $f_{23}-f_{26}$

TABLE XIV
Average, Standard Deviation, and CONFIDENCE LeVEl of the Best Fitness Values Found by HdEA, RCGA-UNDX, CMA-ES, DE, ODE, DEahCSPX, DPSO, SEPSO, and EDA: $f_{27}-f_{30}$

TABLE XV
Average, Standard Deviation, and CONFidence Level of the Best Fitness Values Found by HdEA, RCGA-UNDX, CMA-ES, DE, ODE, DEahCSPX, DPSO, SEPSO, and EDA: $f_{31}-f_{34}$

APPENDIX III
![img-10.jpeg](img-10.jpeg)

Fig. 10. Averaged best fitness values against population size for the test functions $f_{1}-f_{34}$.

![img-11.jpeg](img-11.jpeg)

Fig. 10 (Continued)

![img-12.jpeg](img-12.jpeg)

Fig. 10 (Continued)

![img-13.jpeg](img-13.jpeg)

Fig. 10 (Continued)

![img-14.jpeg](img-14.jpeg)

Fig. 10 (Continued)

![img-15.jpeg](img-15.jpeg)

Fig. 10 (Continued)

## ACKNOWLEDGMENT

The authors would like to thank S. W. Leung for proofreading the manuscript.
