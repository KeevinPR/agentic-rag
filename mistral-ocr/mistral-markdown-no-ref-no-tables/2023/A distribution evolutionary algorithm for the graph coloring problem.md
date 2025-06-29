# A distribution evolutionary algorithm for the graph coloring problem ${ }^{\ominus}$ 

Yongjian Xu*, Huabin Cheng ${ }^{\text {b }}$, Ning Xu ${ }^{\mathrm{c}}$, Yu Chen ${ }^{\mathrm{a}, *}$, Chengwang Xie ${ }^{\mathrm{d}, *}$<br>${ }^{a}$ School of Science, Wuhan University of Technology, Wuhan, 430070, China<br>${ }^{\text {b }}$ Department of Basic Science, Wuchang Shouyi University, Wuhan, 430064, China<br>${ }^{c}$ School of Information Engineering, Wuhan University of Technology, Wuhan, 430070, China<br>${ }^{d}$ School of Data Science and Engineering, South China Normal University, Guangdong, 516600, China

## A R TICLE INFO

Keywords:
Distribution evolutionary algorithm
Orthogonal exploration
Inherited initialization
Graph coloring
Estimation of distribution algorithm

## A B STRAC T

Graph coloring is a challenging combinatorial optimization problem with a wide range of applications. In this paper, a distribution evolutionary algorithm based on a population of probability model (DEA-PPM) is developed to address it efficiently. Unlike existing estimation of distribution algorithms where a probability model is updated by generated solutions, DEA-PPM employs a distribution population based on a novel probability model, and an orthogonal exploration strategy is introduced to search the distribution space with the assistance of an refinement strategy. By sampling the distribution population, efficient search in the solution space is realized based on a tabu search process. Meanwhile, DEA-PPM introduces an iterative vertex removal strategy to improve the efficiency of $k$-coloring, and an inherited initialization strategy is implemented to address the chromatic number problem well. The cooperative evolution of the distribution population and the solution population leads to a good balance between exploration and exploitation. Numerical results demonstrate that the DEA-PPM of small population size is competitive to the state-of-the-art metaheuristics.

## 1. Introduction

Given an undirected graph $G=(V, E)$ with a vertex set $V$ and a edge set $E$, the (vertex) graph coloring problem (GCP) assigns colors to vertexes such that no adjacent vertexes share the same color. If $G$ can be colored by $k$ different colors without color conflicts, it is $k$-colorable. The smallest value of color number $k$ such that $G$ is $k$-colorable is its chromatic number, denoted by $\chi(G)$. There are two instances of the GCP, the $k$-coloring problem attempting to color a graph with $k$ colors and the chromatic number problem trying to get the chromatic number of $G$, both of which are extensively applied in scientific and engineering fields. Due to the NP-completeness of GCPs, some relaxation methods were proposed to transform the combinatorial GCPs to continuous optimization problems [1-3]. However, the transformation will lead to continuous problems with distinct landscapes, and global optimal solutions of the original GCPs could be quite different from those of the relaxed problems.

Accordingly, a variety of metaheuristics have been developed to address the original GCPs efficiently [4]. Individual-based metaheuristics search the solution space by single-point iteration schemes, contributing to their fast convergence and low complexity [5]. However, their performance relies heavily on the initial solution and the definition of
neighborhood, which makes it challenging to balance exploration and exploitation. Population-based metaheuristics perform cooperative multipoint search in the solution space, but a comparatively large population is usually necessary for the efficient search in the solution space, which makes it inapplicable to large-scale GCPs [4].

Recently, metaheuristics based on probability models have been widely employed to solve complicated optimization problems [6-8]. As two popular instances, the ant colony optimization (ACO) [6] and the estimation of distribution algorithm (EDA) [7] employ a single probability model that is gradually updated during the iteration process, which makes it difficult to balance the global exploration and the local exploitation in the distribution space. The quantum-inspired evolutionary algorithm (QEA) performs an active update of probability model by the Q-gate rotation, whereas it is a kind of local exploitation that cannot explore the distribution space efficiently [8]. To remedy the aforementioned issues, we propose a distribution evolutionary algorithm based on a population of probability model (DEA-PPM), where a balance between the convergence performance and the computational complexity could be kept by evolution of small populations. Contributions of this work are as follows.

[^0]
[^0]:    ${ }^{\ominus}$ Y. Xu and H. Cheng contributed equally to this research.

    * Corresponding authors.

    E-mail addresses: xyjchl88888@163.com (Y. Xu), 2020111132@weyu.edu.cn (H. Cheng), xuning@whut.edu.cn (N. Xu), ychen@whut.edu.cn (Y. Chen), chengwangxie@m.scnu.edu.cn (C. Xie).

- We propose a novel distribution model that incorporates the advantages of EDAs and QEAs.
- Based on the proposed distribution model, an orthogonal exploration strategy is introduced to search the probability space with the assistance of a tailored refinement strategy.
- For the chromatic number problem, an inherited initialization is presented to accelerate the convergence process.

Rest of this paper is organized as follows. Section 2 presents a brief review on related works. The proposed distribution model is presented in Section 3, and Section 4 elaborates details of DEA-PPM. Section 5 investigates the influence of parameter and the distribution evolution strategies, and the competitiveness of DEA-PPM is verified by numerical experiments. Finally, we summarize the work in Section 6.

## 2. Literature review

### 2.1. Individual-based metaheuristics for GCPs

Besides the simulated annealing [9,10] and the variable neighborhood search [11], the tabu search (TS) is one of the most popular individual-based metaheuristics applied to solve the GCPs [12]. Porumbel et al. [13] improved the performance of TS by evaluation functions that incorporates the structural or dynamic information in addition to the number of conflicting edges. Blöchliger and Zufferey [14] proposed a TS-based constructive strategy, which constructs feasible but partial solutions and gradually increases its size to get the optimal color assignment of a GCP. Hypothesizing that high quality solutions of GCPs could be grouped in clusters within spheres of a specific diameter, Porumbel et al. [15] proposed two improved TS variants using a learning process and a tree-like structure of the connected spheres. Assuming that each vertex only interacts with a limited number of components, Galán [16] developed a decentralized coloring algorithm, where colors of vertexes are modified according to those of the adjacent vertexes to iteratively reduce the number of edge conflicts. Sun et al. [17] established a solution-driven multilevel optimization framework for GCP, where an innovative coarsening strategy that merges vertexes based on the solution provided by the TS, and the uncoarsening phase is performed on obtained coarsened results to get the coloring results of the original graph. To color vertexes with a given color number $k$, Peng et al. [18] partitioned a graph into a set of connected components and a vertex cut component, and combined the separately local colors by an optimized maximum matching based method.

Since a probability model can provide a bird's-eye view for the landscape of optimization problem, Zhou et al. [19,20] proposed to enhance the global exploration of individual-based metaheuristics by the introduction of probability models. They deployed a probabilistic model for the colors of vertexes, which is updated with the assistance of a reinforcement learning technology based on discovered local optimal solutions [19]. Moreover, they improved the learning strategy of probability model to develop a three-phase local search, that is, a starting coloring generation phase based on a probability matrix, a heuristic coloring improvement phase and a learning based probability updating phase [20].

### 2.2. Population-based metaheuristics for GCPs

Population-based iteration mechanisms are incorporated to the improve exploration abilities of metaheuristics as well. Hsu et al. [21] proposed a modified turbulent particle swarm optimization algorithm for the planar graph coloring problem, where a three-stage turbulent model is employed to strike a balance between exploration and exploitation. Hernández and Blum [22] dealt with the problem of finding valid graphs colorings in a distributed way, and the assignment of different colors to neighboring nodes is asynchronously implemented by simulating the calling behavior of Japanese tree frogs. RebolloRuiz and M. Graña [23] addressed the GCP by a gravitational swarm
intelligence algorithm, where nodes of a graph are mapped to agents, and its connectivity is mapped into a repulsive force between the agents corresponding to adjacent nodes. Based on the conflict matrices of candidate solutions, Zhao et al. [24] developed a dimension-bydimension update method, by which a discrete selfish herd optimizer was proposed to address GCPs efficiently. Aiming to develop an efficient parameter-free algorithm, Chalupa and Nielsen [25] proposed to improve the global exploration by a multiple cooperative searching strategy. For the four-colormap problem, Zhong et al. [26] proposed an enhanced discrete dragonfly algorithm that performs a global search and a local search alternately to color maps efficiently.

The incorporation of probability models are likewise employed to improve the performance of population-based metaheuristics. Bui et al. [27] developed a constructive strategy of coloring scheme based on an ant colony, where an ant colors just a portion of the graph unsing only local information. Djelloul et al. [28] took a collection of quantum matrices as the population of the cuckoo search algorithm, and an adapted hybrid quantum mutation operation was introduced to get enhanced performance of the cuckoo search algorithm.

### 2.3. Hybrid metaheuristics for GCPs

The population-based metaheuristics can be further improved by hybrid search strategies. Paying particular attention to ensuring the population diversity, Lü and Hao [29] proposed an adaptive multiparent crossover operator and a diversity-preserving strategy to improve the searching efficiency of evolutionary algorithms, and proposed a memetic algorithm that takes the TS as a local search engine. Porumbel et al. [30] developed a population management strategy that decides whether an offspring should be accepted in the population, which individual needs to be replaced and when mutation is applied. Mahmoudi and Lotfi [31] proposed a discrete cuckoo optimization algorithm for the GCP, where a neighborhood search in radius of the lay egg causes the algorithm hardly trapped in local minimum and producing new eggs. Accordingly, it provides a good balance between diversification and centralizing.

Wu and Hao [32] proposed a preprocessing method that extracts large independent sets by the TS, and the memetic algorithm proposed by Lü and Hao [29] was employed to color the residual graph. For the chromatic number problem, Douiri and Elbernoussi [33] initialized the color number by the coloring result of a heuristic algorithm and generated the initial population of genetic algorithm (GA) by finding a maximal independent set approximation of the investigated graph.

Bessedik et al. [34] addressed the GCPs within the framework of the honey bees optimization, where a local search, a tabu search and an ant colony system are implemented as workers and queens are randomly generated. Mirsaleh and Meybodi [35] proposed a Michigan memetic algorithm for GCPs, where each chromosome is associated to a vertex of the input graph. Accordingly, each chromosome is a part of the solution and represents a color for its corresponding vertex, and each chromosome locally evolves by evolutionary operators and improves by a learning automata based local search. Moalic and Gondran [36] integrated a TS procedure with an evolutionary algorithm equipped with the greedy partition crossover, by which the hybrid algorithm can performs well with a population consisting of two individuals. Silva et al. [37] developed a hybrid algorithm ColourAnt, which addresses the GCP using an ant colony optimization procedure with assistance of a local search performed by the reactive TS.

### 2.4. Related work on the estimation of distribution algorithm

A large number of works have been reported to improve the general performance of EDAs. To improve the general precision of a distribution model, Shim et al. [38] modeled the restricted Boltzmann machine as a novel EDA, where the probabilistic model is constructed using its energy function, and the $k$-means clustering was employed to group

the population into small clusters. Approximating the Boltzmann distribution by a Gaussian model, Valdez et al. [39] proposed a Boltzmann univariate marginal distribution algorithm, where the Gaussian distribution obtains a better bias to sample intensively the most promising regions. Considering the multivariate dependencies between continuous random variables, PourMohammadBagher et al. [40] proposed a parallel model of some subgraphs with a smaller number of variables to avoid complex approximations of learning a probabilistic graphical model. Dong et al. [41] proposed a latent space-based EDA, which transforms the multivariate probabilistic model of Gaussian-based EDA into its principal component latent subspace of lower dimensionality to improve its performance on large-scale optimization problems.

To enhance the local exploitation of an EDA, Zhou et al. [42] suggested to combine an estimation of distribution algorithm with cheap and expensive local search methods for making use of both global statistical information and individual location information. Considering that the random sampling of Gaussian EDA usually suffers from the poor diversity and the premature convergence, Dang et al. [43] developed an efficient mixture sampling model to achieve a good tradeoff between the diversity and the convergence, by which it can explore more promising regions and utilize the unsuccessful mutation vectors.

The performance of EDA can be further improved by designing tailored update strategies of the probability model. To address the multiple global optima of multimodal problem optimizations, Pèna et al. [44] introduced the unsupervised learning of Bayesian networks in EDA, which makes it able to model simultaneously the different basins represented by the selected individuals, whereas preventing genetic drift as much as possible. Peng et al. [45] developed an explicit detection mechanism of the promising areas, by which function evaluations for exploration can be significantly reduced. To prevent the Gaussian EDAs from premature convergence, Ren et al. [46] proposed to tune the main search direction by the anisotropic adaptive variance that is scaled along different eigendirections based on the landscape characteristics captured by a simple topology-based detection method. Liang et al. [47] proposed to archive a certain number of high-quality solutions generated in the previous generations, by which fewer individuals are needed in the current population for model estimation. In order to address the mixed-variable newsvendor problem, Wang et al. [48] developed a histogram model-based estimation of distribution algorithm, where an adaptive-width histogram model is used to deal with the continuous variables and a learning-based histogram model is applied to deal with the discrete variables. Liu et al. [49] embedded within the search procedure a learning mechanism based on an incremental Gaussian mixture model, by which all new solutions generated during the evolution are fed incrementally into the learning model to adaptively discover the structure of the Pareto set of an MOP.

## 3. The distribution model for the graph coloring problem

### 3.1. The graph coloring problem

Let $n=|V|$ be the vertex number of a graph $G=(V, E)$. An assignment of vertexes with $k$ colors can be represented by an integer vector $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)$, where $x_{j}$ denotes the assigned color of vertex $v_{j}$. Then, the $k$-coloring problem can be modeled as a minimization problem
$\min \quad f_{k}(\mathbf{x})=\sum_{j_{1}=1}^{n} \sum_{j_{2}=1}^{n} \delta\left(j_{1}, j_{2}\right)$
s.t. $\left\{\begin{array}{l}\delta\left(j_{1}, j_{2}\right)=\left\{\begin{array}{l}1, \quad \text { if }\left(v_{j_{1}}, v_{j_{2}}\right) \in E \wedge x_{j_{1}}=x_{j_{2}} \\ 0, \quad \text { otherwise } \\ \mathbf{x}=\left(x_{1}, \ldots, x_{n}\right), x_{j} \in\{1, \ldots, k\}, j=1, \ldots, n,\end{array}\right. \\ j_{i} \in\{1,2, \ldots, n\}, i=1,2 .\end{array}\right.$
While $\delta\left(j_{1}, j_{2}\right)=1$, the adjacent vertexes $v_{j_{1}}$ and $v_{j_{2}}$ are assigned with the same color, and $\left(v_{j_{1}}, v_{j_{2}}\right)$ is called a conflicting edge. Accordingly, the objective values $f_{k}(\mathbf{x})$ represents the total conflicting number of the color assignment $\mathbf{x}$. While $G$ is $k$-colorable, there exists an optimal partition $\mathbf{x}^{*}$ such that $f_{k}\left(\mathbf{x}^{*}\right)=0$, and $\mathbf{x}^{*}$ is called a legal $k$-color assignment of $G$. Thus, the chromatic number problem is modeled as
$\min \quad k$
s.t. $f_{k}\left(\mathbf{x}^{*}\right)=0$
where $\mathbf{x}^{*}$ represents a legal $k$-color assignment that is an optimal color assignment of problem (1).

### 3.2. The Q-bit model and the Q-gate transformation

Different from the ACO and the EDA, the QEA employs a quantum matrix for probabilistic modeling of the solution space, modeling the probability distribution of a binary variable $b x$ by a Q-bit $(a, \beta)^{T}$ satisfying $|a|^{2}+|\beta|^{2}=1$ [50]. That is, $|a|^{2}$ and $|\beta|^{2}$ give the probabilities of $b x=1$ and $b x=0$, respectively. Accordingly, the probability distribution of an $n$-dimensional binary vector $\mathbf{b x}=\left(b x_{1}, \ldots, b x_{n}\right)$ is represented by
$\mathbf{q}=\left(\vec{q}_{1}, \vec{q}_{2}, \ldots, \vec{q}_{n}\right)=\left[\begin{array}{cccc}a_{1} & a_{2} & \cdots & a_{n} \\ \vec{p}_{1} & \vec{p}_{2} & \cdots & \vec{p}_{n}\end{array}\right]$,
where $|a|_{1}^{2}+|\beta|_{1}^{2}=1, j=1, \ldots, n$. Then, the value of $b x_{j}$ can be obtained by sampling the probability distribution $\left(|a|_{j}^{2},|\beta|_{j}^{2}\right)$.

The probability distribution of binary variable is modified in the QEA by the Q-gate, a $2 \times 2$ orthogonal matrix
$U(\Delta \theta)=\left[\begin{array}{cc}\cos (\Delta \theta) & -\sin (\Delta \theta) \\ \sin (\Delta \theta) & \cos (\Delta \theta)\end{array}\right]$.
Premultiplying $\vec{q}_{j}$ by $U(\Delta \theta)$, the probability distribution of $b x_{j}$ is modified as
$\vec{q}_{j}^{\prime}=U(\Delta \theta) \cdot \vec{q}_{j}, \quad i=j, \ldots, n$.
To coloring a graph of $n$ vertexes by $k$ colors, Djelloul et al. [28] modeled the probability distribution of color assignment by a quantum matrix
$\mathbf{q}=\left(\vec{q}_{1}, \vec{q}_{2}, \ldots, \vec{q}_{n}\right)=\left[\begin{array}{cccc}q_{1,1} & q_{1,2} & \cdots & q_{1, n} \\ q_{2,1} & q_{2,2} & \cdots & q_{2, n} \\ \cdots & \cdots & \cdots & \vdots \\ q_{2 k-1,1} & q_{2 k-1,2} & \cdots & q_{2 k-1, n} \\ q_{2 k, 1} & q_{2 k, 2} & \cdots & q_{2 k, n}\end{array}\right]$,
where
$\left(q_{2 i-1, j}\right)^{2}+\left(q_{2 i, j}\right)^{2}=1, \quad \forall i \in\{1, \ldots, k\}, j \in\{1, \ldots, n\}$.
In this way, the Q-gate can be deployed for each unit vector $\left(q_{2 i-1, j}\right.$, $\left.q_{2 i, j}\right)^{T}$ to regulate the distribution of color assignment.

### 3.3. The proposed distribution model of color assignment

Since the unit vector $\left(q_{2 i-1, j}, q_{2 i, j}\right)^{T}$ models each candidate color $i$ of vertex $j$ independently, the sampling process would lead to multiple assignments for vertex $j$, and an additional repair strategy is needed to get a feasible $k$-coloring assignment [28]. To address this defect, we propose to model the color distribution of vertex $j$ by a $k$-dimensional unit vector $\vec{q}_{j}$, and present the color distribution of $n$ vertexes as
$\mathbf{q}=\left(\vec{q}_{1}, \ldots, \vec{q}_{n}\right)=\left[\begin{array}{cccc}q_{11} & q_{12} & \cdots & q_{1 n} \\ q_{21} & q_{22} & \cdots & q_{2 n} \\ \vdots & \vdots & \vdots & \vdots\end{array}\right]$,
where $\vec{q}_{j}$ satisfies
$\left\|\vec{q}_{j}\right\|_{2}^{2}=\sum_{i=1}^{k} q_{i j}^{2}=1, \quad \forall j=1, \ldots, n$.

The distribution model confirmed by (3) and (4) incorporates the advantages of models in EDAs and QEAs.

- An feasible $k$-coloring of $n$ vertexes can be achieved by successively sampling $n$ columns of $\mathbf{q}$.
- The update of probability distribution can be implemented by both orthogonal transformations performed on column vectors of $\mathbf{q}$ and direct manipulations of components that do not change the norms of columns vectors. ${ }^{1}$


## 4. A distribution evolutionary algorithm based on a population of probability model

The proposed DEA-PPM solves the GCP based on a distribution population and a solution population. The distribution population consists of individuals representing distribution models of graph coloring, which are updated by an orthogonal exploration strategy and an composite exploitation strategy. Meanwhile, an associated solution population is deployed to exploit the solution space by the TS-based local search. Moreover, an iterative vertex removal strategy and a tailored inherited initialization strategy are introduced to accelerate the procedure of $k$-coloring, which in turn contributes to its high efficiency of addressing the chromatic number problem. Thanks to the cooperative interplay between the distribution population and the solution population, the DEA-PPM with small populations is expected to achieve competitive results of GCPs.

### 4.1. The framework of DEA-PPM

As presented in Algorithm 1, DEA-PPM is implemented as two nested loopc the inner loop addressing the $k$-coloring problem and the outer loop decreasing $k$ to get the chromatic number $\chi(G)$. Based on a distribution population $\mathbf{Q}(t)=\left(\mathbf{q}^{111}(t), \ldots, \mathbf{q}^{1 n p l}(t)\right)$ and the corresponding solution population $\mathbf{P}(t)=\left(\mathbf{x}^{111}(t), \ldots, \mathbf{x}^{1 n p l}(t)\right)$, it starts with the initialization of the color number $k$, which is then minimized by the outer loop to get the chromatic number $\chi(G)$.

Each iteration of the outer loop begins with the iterative vertex removal (IVR) strategy [51], by which the investigated graph $G$ could be transformed into a reduced graph $G^{\prime}=\left(V^{\prime}, E^{\prime}\right)$, and the complexity of the coloring process could be reduced as well. Then, Lines 511 of Algorithm 1 initialize a distribution population $\mathbf{Q}(0)$ and the corresponding solution population $\mathbf{P}(0)$ for $G^{\prime}$. Once $G^{\prime}$ is colored by Lines 12-20 of Algorithm 1, DEA-PPM recovers the obtained color assignment $\mathbf{x}_{G^{\prime}}^{*}$ to get an color assignment $\mathbf{x}_{G}^{*}$ of $G$, and $\mathbf{Q}(t)$ as well as $\mathbf{P}(t)$ is archived for the inherited initialization performed at the next generation. Repeating the aforementioned process until the terminationcondition 1 is satisfied, DEA-PPM returns a color number $k$ and the corresponding color assignment $\mathbf{x}_{G}^{*}$.

After the initialization of $\mathbf{x}_{G^{\prime}}^{*}, \mathbf{p}_{1}, \mathbf{p}_{2}$ and $t$, the inner loop tries to get a legal $k$-coloring assignment for the reduced graph $G^{\prime}$ by evolving both the distribution population $\mathbf{Q}(t)$ and the solution population $\mathbf{P}(t)$. It first performs the orthogonal exploration on $\mathbf{Q}(t)$ to generate $\mathbf{Q}^{\prime}(t)$, and then, generates an intermediate solution population $\mathbf{P}^{\prime}(t)$, which is further refined to get $\mathbf{P}(t+1)$. Meanwhile, $\mathbf{Q}(t+1)$ is generated by refining $\mathbf{Q}^{\prime}(t)$. The inner loop repeats until the termination-condition 2 is satisfied.

The outer loop of DEA-PPM is implemented only once for the $k$-coloring problem. To address the chromatic number problem, the termination condition 1 is satisfied if the chromatic number has been identified or the inner loop fails to get a legal $k$-coloring assignment for a given iteration budget. The termination condition 2 is met while a legal $k$-coloring assignment is obtained or the maximum iteration number is reached.

[^0]
## Algorithm 1: The framework of DEA-PPM

Input: an undirected graph $G=(V, E)$;
Output: the color number $k$, the obtained color assignment $\mathbf{x}_{G}^{*}$;
$1 \operatorname{gen} \leftarrow 0$;
initialize the color number $k$;
while termination-condition 1 is not satisfied do
reduce $G=(V, E)$ to $G^{\prime}=\left(V^{\prime}, E^{\prime}\right)$ by the IVR strategy ;
if gen $=0$ then
initialize $\mathbf{Q}(0)$ by (5);
sample $\mathbf{Q}(0)$ to generate $\mathbf{P}(0) ; / *$ unform initialization $* /$
else
$\left(\mathbf{Q}(0), \mathbf{P}(0)\right)=\operatorname{InherInit}(\mathbf{Q}, \mathbf{P}, k) ; / *$ inherited initialization $* /$
$k=k-1$;
end
set $\mathbf{x}_{G^{\prime}}^{*}$ as the best solution in $\mathbf{P}(0)$;
$\mathbf{p}_{1}=\mathbf{x}_{G^{\prime}}^{*}, \mathbf{p}_{2}=\mathbf{x}_{G^{\prime}}^{*}$
$t \leftarrow 1$;
while termination-condition 2 is not satisfied do
$\mathbf{Q}^{\prime}(t)=\operatorname{OrthExpQ}(\mathbf{Q}(t-1), \mathbf{P}(t-1)) ; / *$ orthogonal exploration $* /$
$\mathbf{P}^{\prime}(t)=\operatorname{SampleP}(\mathbf{Q}^{\prime}(t), \mathbf{P}(t-1)) ; / *$ sampling with inheritance $* /$
$\left(\mathbf{P}(t), \mathbf{p}_{1}, \mathbf{p}_{2}, \mathbf{x}_{G^{\prime}}^{*}\right)=\operatorname{RefineP}\left(\mathbf{P}^{\prime}(t), \mathbf{p}_{1}, \mathbf{p}_{2}, \mathbf{x}_{G^{\prime}}^{*}\right) / *$
refinement of the solution population $* /$
$\mathbf{Q}(t)=\operatorname{RefineQ}\left(\mathbf{P}^{\prime}(t), \mathbf{P}(t), \mathbf{Q}^{\prime}(t)\right) ; / *$ refinement of the distribution population $* /$
$t \leftarrow t+1$;
end
recover $\mathbf{x}_{G^{\prime}}^{*}$ by the IR strategy to get $\mathbf{x}_{G}^{*}$;
$\mathbf{Q}=\mathbf{Q}(t), \mathbf{P}=\mathbf{P}(t)$;
gen $\leftarrow$ gen +1
end

For the $k$-coloring problem, DEA-PPM initializes the color number $k$ by a given positive integer. While it is employed to address the chromatic number problem, we set $k=\Delta G+1^{2}$ because an undirected graph $G$ is sure to be $(\Delta G+1)$-colorable [52].

### 4.2. The iterative vertex removal strategy and the inverse recovery strategy

To reduce the time complexity of the $k$-coloring algorithm, Yu et al. [51] proposed an iterative vertex removal (IVR) strategy to reduce the size of the investigated graph. By successively removing vertexes with degrees less than $k$, IVR generates a reduced graph $G^{\prime}=\left(V^{\prime}, E^{\prime}\right)$, and put the removed vertexes into a stack $S$. In this way, one could get a graph $G^{\prime}$ where degrees of vertexes are greater than or equal to $k$, and its size could be significantly smaller than that of $G$.

While a $k$-coloring assignment $\mathbf{x}_{G^{\prime}}^{*}$ is obtained for the reduced graph $G^{\prime}$, the inverse recovery (IR) operation is implemented by recovering vertexes in the stack $S$. The IR process is initialized by assigning any legal color to the vertex at the top of $S$. Because the IVR process removes vertexes with degree less than $k$, the IR process can get all recovered vertexes colored without conflicting. An illustration for the implement of the IVR and the IR is presented in Fig. 1.

### 4.3. Population initialization

Depending on the iteration stage of DEA-PPM, the initialization of populations is implemented by the uniform initialization or the inherited initialization.

[^1]
[^0]:    ${ }^{1}$ Details for the update process are presented in Section 4.4.

[^1]:    ${ }^{2}$ Here $\Delta G$ is the maximum vertex degree of graph $G$.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The iterative vertex removal and the inverse recovery process for the 3-coloring of $G=(V, E)$. (a) Graph $G=(V, E)$ consisting of 8 vertexes and 14 edges. (b)(c) Vertexes $B$ and $A$ are successively removed from $G$ to get the reduced graph $G^{\prime}=\left(V^{\prime}, E^{\prime}\right)$. (d) A legal 3-color assignment of $G^{\prime}$. (e)(f) Recover vertexes $A$ and $B$ to get a legal 3-color assignment of $G$.

At the beginning, the uniform initialization generates $n p$ individuals of $\mathbf{Q}(0)$ as
$\mathbf{q}^{(0)}=\left[\begin{array}{cccc}\frac{1}{\sqrt{k}} & \frac{1}{\sqrt{k}} & \cdots & \frac{1}{\sqrt{k}} \\ \frac{1}{\sqrt{k}} & \frac{1}{\sqrt{k}} & \cdots & \frac{1}{\sqrt{k}} \\ \frac{1}{\sqrt{k}} & \frac{1}{\sqrt{k}} & \cdots & \frac{1}{\sqrt{k}}\end{array}\right]$.
$\mathbf{P}(0)$ is generated by sampling model (5) $n p$ times.
While gen $>0$, the inherited initialization gets $\mathbf{Q}(0)$ and $\mathbf{P}(0)$ with the assistance of the distribution populations $\mathbf{Q}$ and the solution population $\mathbf{P}$ archived at the last generation. The graph $G$ has been colored with $k$ colors, and it is anticipated to get a legal $k-1$-color assignment. To get an initial color assignment of $k-1$ colors, a color index $l_{m}$ that corresponds to the minimum vertex independent set is identified for $\mathbf{x}^{[i]}=\left(x_{1}^{[i]}, \ldots, x_{n}^{[i]}\right) \in \mathbf{P}$. Then, we get the initial color assignment $\mathbf{y}^{[i]}=\left(y_{1}^{[i]}, \ldots, y_{n}^{[i]}\right)$ by
$y^{[i]}=\left\{\begin{array}{ll}x^{[i]}-1, & \text { if } x^{[i]} \geq l_{m}, \\ x^{[i]}, & \text { otherwise. }\end{array}\right.$
Meanwhile, delete the $l_{m}$-th row of $\mathbf{q}^{[i]}$, and normalize its columns to get an initial distribution $\mathbf{r}^{[i]}$ corresponding to $k-1$ colors. Details of the inherited initialization are presented in Algorithm 2.

### 4.4. Evolution of the distribution population

Based on the distribution model defined by (3) and (4), DEA-PPM performs the orthogonal exploration on individuals of $\mathbf{Q}(i)$ to explore the probability space. Moreover, distribution individuals of $\mathbf{Q}(i)$ are refined by an exploitation strategy or a disturbance strategy.

### 4.4.1. Orthogonal transformation

An orthogonal transformation on a column vector is performed by premultiplying an orthogonal matrix $M$, a square matrix satisfying
$M^{T} \cdot M=M \cdot M^{T}=I$,
where $I$ is the identity matrix. Because an orthogonal transformation preserves the 2-norm [53], we know
$\|M \vec{v}\|_{2}=\|\vec{v}\|_{2}, \quad \forall \vec{v} \in \mathbb{R}^{n}$.

Algorithm 2: $\left(\mathbf{Q}^{T}, \mathbf{P}^{T}\right)=I$ nherIm $(\mathbf{Q}, \mathbf{P}, k)$
Input: a distribution population $\mathbf{Q}$, a solution population $\mathbf{P}$, a color number $k$;
Output: the initialized distribution population $\mathbf{Q}^{t}$, the initialized solution population $\mathbf{P}^{t}$;
for $i=1, \ldots, n p$ do
$\mathbf{x}^{[i]} \in \mathbf{P}, \mathbf{q}^{[i]} \in \mathbf{Q}$
transform $\mathbf{x}^{[i]}=\left(x_{1}^{[i]}, \ldots, x_{n}^{[i]}\right)$ to a vertex partition $z=\left\{V_{1}, \ldots, V_{k}\right\} ;$
$l_{m} \leftarrow \arg \min \left\{\left|V_{j}\right|\right\} ;$
for $j=1, \ldots, n$ do
if $x_{j}^{[i]} \geq l_{m}$ then
$x_{j}^{[i]}=x_{j}^{[i]}-1$;
end
end
$y^{[i]}=\mathbf{x}^{[i]}$
delete the $l_{m}$-th row of $\mathbf{q}^{[i]}$ and normalize $\mathbf{q}^{[i]}$ to get $\mathbf{r}^{[i]}$;
end
$\mathbf{Q}^{t}=\bigcup_{i=1}^{n p} \mathbf{r}^{[i]}, \mathbf{P}^{t}=\bigcup_{i=1}^{n p} \mathbf{y}^{[i]}$;
Then, by performing orthogonal transformations on columns of the distribution individuals, DEA-PPM can explore the distribution space flexibly.

Since columns of an orthogonal matrix are orthonormal [53], one can get an orthogonal matrix by performing the QR decomposition on an invertible matrix [54].

### 4.4.2. Orthogonal exploration in the distribution space

To perform the orthogonal exploration in the distribution space, DEA-PPM generates an orthogonal matrix by performing the QR decomposition on an invertible matrix that is generated randomly. As presented in Algorithm 3, $m$ worst individuals of $\mathbf{Q}$ are modified by random orthogonal transformations performed on $c$ randomly selected columns. As an initial study, $m$ is set as a random integer in $[1, n p / 2]$, and $c$ is an integer randomly sampled in $[1, n / 10]$.

### 4.4.3. Refinement of the distribution population

As presented in Algorithm 4, the distribution population $\mathbf{Q}^{t}$ is refined to generate $\mathbf{Q}, \forall \mathbf{q}^{[i]}=\left(q_{i, j}^{[i]}\right)_{k \leq a} \in \mathbf{Q}^{t}$, DEA-PPM refines its

## Algorithm 3: $\mathbf{Q}^{t}=\operatorname{OrthExpQ}(\mathbf{Q} \cdot \mathbf{P})$

Input: a distribution population $\mathbf{Q}$, a solution population $\mathbf{P}$;
Output: the updated distribution population $\mathbf{Q}^{t}$;
1 sorting $\mathbf{Q}$ by fitness values of corresponding individuals in $\mathbf{P}$;
2 take $\mathbf{Q}_{w}$ as the collection of $m$ worst individuals of $\mathbf{Q}$;
$3 \mathbf{Q}^{t}=\mathbf{Q} \backslash \mathbf{Q}_{m}$;
4 for $\mathbf{q} \in \mathbf{Q}_{w}$ do
5 $\mathbf{q}^{t} \sim \mathbf{q}$;
6 randomly select $c$ columns $\vec{q}_{i j}^{*}(l=1, \ldots, c)$ from $\mathbf{q}^{t}$;
7 for $l=1, \ldots, c$ do
8 generate a random orthogonal matrix $M_{l}$;
$q_{i j}^{t-1}=M_{l} q_{i j}^{t-1}$;
9 end
10
$\mathbf{Q}^{t}=\mathbf{Q}^{t} \cup \mathbf{q}^{t}$
12 end

## Algorithm 4: $\mathbf{Q}=\operatorname{RefineQ}\left(\mathbf{P}^{t}, \mathbf{P}, \mathbf{Q}^{t}\right)$

Input: two solution populations $\mathbf{P}$ and $\mathbf{P}^{t}$, a distribution population $\mathbf{Q}$;
Output: the refined distribution population $\mathbf{Q}^{t}$;
for $i=1, \ldots, n p$ do
$\mathbf{q}^{[i]} \in \mathbf{Q}^{t}, \mathbf{x}^{[i]} \in \mathbf{P}^{t}, \mathbf{y}^{[i]} \in \mathbf{P}$;
for $j=1, \ldots, n$ do
set $r n d_{j} \sim U(0,1)$;
if $r n d_{j} \leq p_{0}$ then
$\vec{r}_{j}^{[i]}$ is generated by the exploitation strategy confirmed by Eqs. (7) and (8);
else
$\vec{r}_{j}^{[i]}$ is generated by the exploitation strategy defined by Eq. (9);
end
end
$\mathbf{r}^{[i]}=\left(\vec{r}_{1}^{[i]}, \ldots, \vec{r}_{n}^{[i]}\right)$;
12 end
$13 \mathbf{Q}=\bigcup_{i=1}^{i p} \mathbf{r}^{[i]}$.
$j$ th column $\vec{q}_{j}^{[i]}$ with the assistance of the $j$ th components of $\mathbf{x}^{[i]}=$ $\left(x_{1}^{[i]}, \ldots, x_{n}^{[i]}\right) \in \mathbf{P}^{t}$ and $\mathbf{y}^{[i]}=\left(y_{1}^{[i]}, \ldots, y_{n}^{[i]}\right) \in \mathbf{P}$. With probability $p_{0}$, $\vec{q}_{j}^{[i]}$ is refined by an exploitation strategy; otherwise, its refinement is implemented by a disturbance strategy.

The exploitation strategy. Similar to the probability learning procedure proposed in [20], the first phase of the exploitation strategy is implemented by
$r_{i, j}^{[i]}=\left\{\begin{array}{ll}\sqrt{a+(1-\alpha)\left(q_{i, j}^{[i]}\right)^{2}} & \text { if } l=y_{j}^{[i]} \\ \sqrt{(1-\alpha)\left(q_{i, j}^{[i]}\right)^{2}} & \text { if } l \neq y_{j}^{[i]}\end{array} \quad l=1, \ldots, k\right.$,
where $y_{j}^{[i]}$ is the $j$ th component of $\mathbf{y}^{[i]}$. Then, an local orthogonal transformation is performed as
$\left[\begin{array}{l}r_{1, j}^{[i]} \\ \vec{r}_{1, j}^{[i]} \\ \vec{r}_{2, j}^{[i]}\end{array}\right]=U\left(\Delta \theta_{j}\right) \times\left[\begin{array}{l}r_{1, j}^{[i]} \\ \vec{r}_{2, j}^{[i]} \\ \vec{r}_{3, j}^{[i]}\end{array}\right]$.
where
$U\left(\Delta \theta_{j}\right)=\left[\begin{array}{ll} \cos \left(\Delta \theta_{j}\right) & -\sin \left(\Delta \theta_{j}\right) \\ \sin \left(\Delta \theta_{j}\right) & \cos \left(\Delta \theta_{j}\right)\end{array}\right]$.
$l_{1}=x_{j}^{[i]}, l_{2}=y_{j}^{[i]}$. Eq. (7) conducts an overall regulation controlled by the parameter $\alpha$, and Eq. (8) rotates the subvector $\left(r_{l_{1}, j}^{[i]}, r_{l_{2}, j}^{[i]}\right)^{T}$ counterclockwise by $\Delta \theta_{j}$ to regulate it slightly.

The disturbance strategy. $\forall j \in\{1,2, \ldots, n\}, \vec{r}_{j}^{[i]}=\left(r_{1, j}^{[i]}, \ldots, r_{k, j}^{[i]}\right)$ is generated by
$r_{i, j}^{[i]}=\left\{\begin{array}{ll}\sqrt{\frac{\varepsilon_{n}^{[i]}, s^{2}}{1-\left(1-\varepsilon_{n}^{[i]}\right)^{2}} & \text { if } l=l_{0}, \\ \sqrt{\frac{\varepsilon_{n}^{[i]}, s^{2}}{1-\left(1-\varepsilon_{n}^{[i]}\right)^{2}} & \text { if } l \neq l_{0},\end{array}\right.$
$l=1, \ldots, k$. For $0<\lambda<1$, the $l_{0}$-th components of $\vec{r}_{j}^{[i]}$ is smaller than that of $\vec{q}_{j}^{[i]}$, and others are greater. Thus, we set $l_{0}=y_{j}^{[i]}$ to prevent DEA-PPM from premature convergence.

### 4.5. Efficient search in the solution space

To search the solution space efficiently, DEA-PPM generates a solution population by sampling with inheritance, and then, refines it using a multi-parent crossover operation followed by the TS search proposed in Ref. [55].

### 4.5.1. The strategy of sampling with inheritance

Inspired by the group selection strategy [19], components of new solution $\mathbf{y}^{[i]}=\left(y_{1}^{[i]}, \ldots, y_{n}^{[i]}\right)$ are either generated by sampling the distribution $\mathbf{q}^{[i]}=\left(\vec{q}_{1}^{[i]}, \ldots, \vec{q}_{n}^{[i]}\right)$ or inheriting from the corresponding solution $\mathbf{x}^{[i]}=\left(x_{1}^{[i]}, \ldots, x_{n}^{[i]}\right)$. The strategy of sampling with inheritance is presented in Algorithm 5, where $r$ is the probability of generating $y_{j}^{[i]}$ by sampling $\vec{q}_{j}^{[i]}$.

## Algorithm 5: $\mathbf{P}^{t}=\operatorname{SampleP}(\mathbf{Q}, \mathbf{P})$

Input: a distribution population $\mathbf{Q}$, a solution population $\mathbf{P}$;
Output: the generated solution population $\mathbf{P}^{t}$;
for $i=1, \ldots, n p$ do
$\mathbf{q}^{[i]} \in \mathbf{Q}, \mathbf{x}^{[i]} \in \mathbf{P}$;
for $j=1, \ldots, n$ do
set $r n d_{j} \sim U(0,1)$;
if $r n d_{j}<r$ then
sampling $\vec{q}_{1}^{[i]}$ to get $y_{j}^{[i]}$;
else
$y_{j}^{[i]}=x_{j}^{[i]}$;
end
end
$\mathbf{y}^{[i]}=\left(y_{1}^{[i]}, \ldots, y_{n}^{[i]}\right)$;
12 end
$13 \mathbf{P}^{t}=\bigcup_{i=1}^{n p} \mathbf{y}^{[i]}$.

### 4.5.2. Refinement of the solution population

The quality of generated solutions is further improved by a refinement strategy presented in Algorithm 6, which is an iterative process consisting of a multi-parent greedy partition crossover guided by two promising solutions $\mathbf{p}_{1}$ and $\mathbf{p}_{2}$ as well as the TS process presented in Ref. [55]. Meanwhile, two promising solutions $\mathbf{p}_{1}$ and $\mathbf{p}_{2}$ are updated. The refinement process ceases once it stagnates for 20 consecutive iterations.

Multi-parent greedy partition crossover (MGPX). Inspired by the motivation of greedy partition crossover (GPX) for graph coloring [55], we propose the multi-parent greedy partition crossover (MGPX) presented in Algorithm 7. For $\mathbf{x}_{1} \in \mathbf{P}$, two mutually different solutions $\mathbf{x}_{2}$ and $\mathbf{x}_{3}$ are selected from $\mathbf{P} \backslash\left\{\mathbf{x}_{1}\right\} \cup\left\{\mathbf{p}_{1}, \mathbf{p}_{2}\right\}$. Then, the MGPX is performed on $\mathbf{x}_{1}, \mathbf{x}_{2}$ and $\mathbf{x}_{3}$ to generate a new solution $\mathbf{y}$. After the traversal of the solution population $\mathbf{P}$, all generated solutions construct the intermediate solution population $\mathbf{P}^{t}$.

Update of the promising solutions. The promising solution $\mathbf{p}_{1}$ is updated if a better solution $\mathbf{b}$ is obtained. Then, $\mathbf{p}_{2}$ is set as the original values of $\mathbf{p}_{1}$. To fully exploits the promising information incorporated by $\mathbf{p}_{2}$, it is updated once every 10 iterations.

```
Algorithm 6: \(\left(\mathbf{P}, \mathbf{p}_{1}, \mathbf{p}_{2}, \mathbf{x}_{G^{\prime}}^{*}\right)=\operatorname{Refine} P\left(\mathbf{P}^{\prime}, \mathbf{p}_{1}, \mathbf{p}_{2}, \mathbf{x}_{G^{\prime}}^{*}\right)\)
    Input: a solution population \(P^{\prime}\), two reference solutions \(\mathbf{p}_{1}\) and
        \(\mathbf{p}_{2}\), the best color assignment \(\mathbf{x}_{G^{\prime}}^{*}\);
    Output: the updated solution population \(P\), two updated
        reference solutions \(\mathbf{p}_{1}\) and \(\mathbf{p}_{2}\), the updated best color
        assignment \(\mathbf{x}_{G^{\prime}}^{*}\);
    iter \(\leftarrow 0\), iter_stag \(\leftarrow 0\);
    \(\mathbf{c}_{1}=\mathbf{x}_{G^{\prime}}^{*}\)
    while iter_stag \(<20\) do
        \(\mathbf{P}=M G P X\left(\mathbf{P}^{\prime}, \mathbf{p}_{1}, \mathbf{p}_{2}\right)\)
        \(\mathbf{P}=\) Tabs \((\mathbf{P})\)
        record the best solution in \(\mathbf{P}\) as \(\mathbf{b}\)
        if \(f(\mathbf{b})<f\left(\mathbf{p}_{1}\right)\) then
            iter_stag \(=0\)
            \(\mathbf{c}_{1}=\mathbf{p}_{1}, \mathbf{p}_{1}=\mathbf{b}\)
        else
            iter_stag \(=\) iter_stag +1
            end
        if \(f(\mathbf{b})<f\left(\mathbf{x}_{G^{\prime}}^{*}\right)\) then
            \(\mathbf{x}_{G^{\prime}}^{*}=\mathbf{b}\)
        end
        if \(\operatorname{mod}(\) iter, 10 \()=0\) then
            \(\mathbf{p}_{2}=\mathbf{c}_{1}\)
        end
        \(\mathbf{P}^{\prime}=\mathbf{P}\)
        iter \(=\) iter +1
    end
```

```
Algorithm 7: \(\mathbf{P}^{\prime}=M G P X\left(\mathbf{P}, \mathbf{p}_{1}, \mathbf{p}_{2}\right)\)
    Input: a solution population \(\mathbf{P}\), two reference solutions \(\mathbf{p}_{1}\) and
        \(\mathbf{p}_{2}\)
    Output: the updated solution population \(\mathbf{P}^{\prime}\)
    \(\mathbf{P}^{\prime}=0\)
    for \(\mathbf{x} \in \mathbf{P}\) do
        let \(\mathbf{x}_{1}=\mathbf{x}, \mathbf{x}_{2}\) and \(\mathbf{x}_{3}\) be two different solutions selected
        from \(\mathbf{P} \backslash\{\mathbf{x}\} \cup\left\{\mathbf{p}_{1}, \mathbf{p}_{2}\right\}\)
        transform \(\mathbf{x}_{i}\) to the corresponding vertex partition
        \(s_{i}=\left\{V_{1}^{i}, \ldots, V_{k}^{i}\right\}, i=1,2,3\)
        for \(i=1, \ldots, k\) do
            randomly select an index \(i_{0} \in\{1,2,3\}\) according to the
                probability distribution \(\left\{P_{i},\left(1-P_{i}\right) / 2,\left(1-P_{i}\right) / 2\right\}\)
                choose \(l_{0}\) such that \(V_{i_{0}}^{i_{0}}\) has a maximum cardinality;
                \(V_{i}:=V_{i_{0}}^{i_{0}}\)
                remove the vertices of \(V_{i}\) from \(s_{1}, s_{2}\) and \(s_{3}\)
            end
        assign the vertices of \(V^{\prime} \backslash \bigcup_{i=1}^{k} V_{i}\) by \(s_{3}\)
        transform \(s=\left(V_{1}, \ldots, V_{k}\right)\) to a solution \(\mathbf{y}\)
        \(\mathbf{P}^{\prime}=\mathbf{P}^{\prime} \cup\{\mathbf{y}\}\)
    end
```


# 5. Numerical experiments 

The investigated algorithms are evaluated on the benchmark instances from the second DIMACS competition ${ }^{5}$ that were used to test graph coloring algorithms in recent studies [16,17,20,29,36]. All tested algorithms are developed in $\mathrm{C}++$ programming language, and run in

[^0]Microsoft Windows 7 on a laptop equipped with the Intel(R) Core(TM) i7 CPU 860 @ 2.80 GHz and 8 GB system memory. We first perform a parameter study to get appropriate parameter settings of DEA-PPM, and then, the proposed evolution strategies of distribution population are investigated to demonstrate their impacts on its efficiency. Finally, numerical comparisons for both the chromatic number problem and the $k$-coloring problem are performed with the state-of-the-art algorithms. For numerical experiments, time budgets of all algorithms are consistently set as 3600 s (one hour). Because performance of the investigated algorithms varies for the selected benchmark problems, we perform the numerical comparison in two different ways. If two compared algorithms achieve inconsistent coloring results for the chromatic number problem, numerical comparison is performed by the obtained color numbers; otherwise, we take the running time as the evaluation metric while they get the same coloring results.

### 5.1. Parameter study

By setting $k$ as the best known color numbers of the benchmark problems, preliminary experiments for the $k$-coloring problem show that the performance of DEA-PPM is significantly influenced by the population size $n p$, the regulation parameter $\alpha$ and the maximum iteration budget $I t e r_{\max }$ of the TS. Then, we first demonstrate the univariate influence of parameters by the one-way analysis of variance (ANOVA), and then, perform a descriptive comparison to get a set of parameter for further numerical investigations. The benchmark instances selected for the parameter study are the $k$-coloring problems of DSJC500.5, flat300_28_0, flat1000_50_0, flat1000_76_0, le450_15c, le450_15d.

### 5.1.1. Analysis of variance on the impacts of parameters

Our preliminary experiments show that DEA-PPM achieves promising results with $n p=8, \alpha=0.2$ and iter $_{\max }=5000$, which is taken as the baseline parameter setting of the one-side ANOVA test of running time. With the significance level of 0.05 , the significant influences are highlighted in Table 1 by bold P-values.

Generally, the univariate changes of $n p, \alpha$ and iter $_{\max }$ do not have significant influence on performance of DEA-PPM for instances flat300_28_0, le450_15c and le450_15d, except that values of iter $_{\max }$ has great impact on the results of le450_15d. But for instances DSJC500.5, flat1000_50_0 and flat1000_76_0, the influence is significant, except that $\alpha$ does not significantly influence the performance of DEA-PPM on flat1000_50_0. To illustrate the results, we included the curves of expected running time in Fig. 2. The univariate analysis shows that the best results could be achieved by setting $n p=8, \alpha=0.2$ and iter $_{\max }=5000$.

### 5.1.2. Descriptive statistics on the composite impacts of parameters

Besides the one-way ANOVA test, we also present a descriptive comparison for the composite impact of several parameter settings. With the parameter combinations presented in Table 2, statistical results for running time of 30 independent runs are included in Fig. 3.

It indicates that the parameter setting $S_{10}$ leads to the most promising results of DEA-PPM. Combining it with the setting of other parameters, we get the parameter setting of DEA-PPM presented in Table 3, which is adopted in the following experiments.

### 5.2. Experiments on the evolution strategies of probability distribution

In DEA-PPM, the evolution of distribution population is implemented by the orthogonal exploration strategy and the exploitation strategy. We try to validate the positive effects of these strategies in this section.

To validate the efficiency of the orthogonal exploration strategy, we compare two variants, the DEA-PPM with orthogonal exploration (DEA-PPM-O) and the DEA-PPM without orthogonal exploration (DEA-PPM-N), and show in Fig. 4 the statistical results of running time


[^0]:    ${ }^{5}$ Publicly available at ftp://dimacs.rutgers.edu/pub/challenge/graph/ benchmarks/color/.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Influence of parameters on expected running time of DEA-PPM.

Table 1
Results of the one-way ANOVA test.

Table 2
Candidate parameter settings of DEA-PPM.

Table 3
Parameter setting of the DEA-PPM for numerical experiments.

for $k$-coloring of the easy benchmark problems (DSJC500.1 ( $k=12$ ), le450_15c $(k=15)$, led450_15d $(k=15))$ and the hard benchmark problems(DSJC500.5 $(k=48)$, DSJC1000.1 $(k=20)$, DSJC1000.9 $(k=$ 226)). The box plots imply that with the employment of the orthogonal exploration strategy, DEA-PPM-O performs generally better than DEA-PPM-N, resulting in smaller values of the median value, the quantiles and the standard deviations of running time.

The positive impact of exploitation strategy is verified by comparing the DEA-PPM with exploitation (DEA-PPM-E) with the variant without exploitation (DEA-PPM-W), and the box plots of running time are included in Fig. 5. It is demonstrated that DEA-PPM-E generally outperforms DEA-PPM-W in terms of the median value, the quantiles and the standard deviation of running time.

Besides the statistical comparison regarding the exact values of running time, we perform a further comparison by the Wilcoxon rank sum test with a significance level of 0.05 , where the statistical test is based on the sorted rank of running time instead of its exact values. The results are included in Table 4, where "P" is the $p$-value of hypothesis test. For the test conclusion "R", " + ", " - " and " - " indicate that the performance of DEA-PPM is better than, worse than and incomparable to that of the compared variant, respectively. The results demonstrate that DEA-PPM outperforms DEA-PPM-N and DEA-PPM-W on two instances, and is not inferior to them for all benchmark problems. It

Table 4
Wilcoxon rank-sum test for the evolution strategies of distribution population.

further validates the conclusion that both the exploration strategy and the exploitation strategy significantly improve the performance of DEA-PPM.

### 5.3. Numerical comparison with the state-of-the-art algorithms

To demonstrate the competitiveness of DEA-PPM, we perform numerical comparison for the chromatic number problem and the $k$ coloring problem with SDGC [16], MACOL [29], SDMA [17], PLSCOL [20], and HEAD [36], the parameter settings of which are presented in Table 5. If an algorithm cannot address the chromatic number problem or the $k$-coloring problem in 3600 s , a failed run is recorded by the running time of 3600 s .

### 5.3.1. Comparison for the chromatic number problem

In order to verify the competitiveness of DEA-PPM on the chromatic number problem, we compare it with SDGC, MACOL, SDMA, PLSCOL and HEAD by 8 selected benchmark problems, and the statistical results of 30 independent runs are collected in Table 6, where $k_{\text {min }}, k_{\text {max }}$, $k_{\text {max }}$ and $k_{\text {std }}$ represent the average color number, the maximum color number, the minimum color number and the standard deviation of

![img-2.jpeg](img-2.jpeg)

Fig. 3. Statistical results for running time of the DEA-PPM that addresses the $k$-coloring problem of selected benchmark problems. (a) DSJC500.5( $k=48$ ). (b) flat300_28_0( $k=31$ ). (c) flat1000_50_0( $k=50$ ). (d) flat1000_76_0( $k=96$ ). (e) le450_15c( $k=15$ ). (f) le450_15d( $k=15$ ).
![img-3.jpeg](img-3.jpeg)

Fig. 4. Comparison of running time between the DEA-PPM-O and the DEA-PPM-N by selected benchmark problems.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Comparison of running time between the DEA-PPM-E and the DEA-PPM-W by selected benchmark problems.

Table 5
Parameter settings of the compared algorithms.
color numbers, respectively. The best results are highlighted by bold texts.

It is shown that DEA-PPM generally outperforms the other five state-of-the-art algorithms in terms of $k_{\text {occ }}, k_{\text {min }}, k_{\text {max }}$ and $k_{\text {std }}$ of 30 independent runs. Attributed to the population-based distribution evolution strategy, the global exploration ability of DEA-PPM is enhanced significantly. Moreover, the inherited initialization strategy improve the searching efficiency of the inner loop for search of $k$-coloring assignment. As a result, it can address these problems efficiently and obtain $\chi(G)$ with a $100 \%$ success rate for all of eight selected problems.

It is noteworthy that the competitiveness is partially attributed to the IVR strategy introduced by DEA-PPM, especially for the sparse benchmark graphs fpsol2.i.2 and fpsol2.i.3. Numerical implementation shows that when $k=30$, introduction of the IVR strategy reduces the vertex number of fpsol2.i. 2 and fpsol2.i. 3 from 451 and 425 to 90 and 88 , respectively. Thus, the scale of the reduced graph $G^{\prime}$ is significantly cut down for fpsol2.i. 2 and fpsol2.i.3, which greatly improves the efficiency of the $k$-coloring process validated by the inner loop of DEA-PPM.

However, it demonstrates that DEA-PPM, PLSCOL and HEAD get consistent results on the instances flag300_26_0 and DSJC1000_1, and the best results of DEA-PPM and HEAD is a bit worse than that of PLSOCL. Accordingly, we further compare their performance by the Wilcoxon rand sum test. If the compared algorithms obtain different results of color number, the sorted rank is calculated according to
the color number; while they get consistent results of color number, the rank sum test is performed according to the running time of 30 independent runs (see Table 7).

The test results demonstrate that DEA-PPM does outperform SDGC, MACOL and SDMA on the selected benchmark problems. For the instance flat300_26_0, it is shown in Table 6 that DEA-PPM, PLSCOL and HEAD can address the chromatic number in 3600s. While the running time is compared by the rank sum test, we get the conclusion that PLSCOL runs faster than DEA-PPM. Considering the instance DSJC1000_1, DEA-PPM, PLSCOL and HEAD stagnate at the assignment of 21 colors. However, the rank sum test shows that DEA-PPM is inferior to PLSCOL and HEAD in terms of the running time.

### 5.3.2. Comparison for the $k$-coloring problem

Numerical results on the chromatic number problem imply that DEA-PPM, PLSCOL and HEAD outperform SDGC, MACOL and SDMA, but the superiority of DEA-PPM over PLSCOL and HEAD is dependent on the benchmark instances. To further compare DEA-PPM with PLSCOL and HEAD, we investigate their performance for the $k$-coloring problem, where $k$ is set as the chromatic number of the investigate instance. For 18 selected benchmark problems collected in Table 8, we present the success rate (SR) and average runtime ( $T$ ) of 30 independent runs, and the best results are highlighted by bold texts.

Thanks to the incorporation of the population-based distribution evolution strategy, the global exploration of DEA-PPM has been significantly improved, resulting in better success rate for most of the selected

Table 6
Comparison of DEA-PPM with SDGC, MACOL, SDMA, PLSCOL and HEAD for the chromatic number problem.

Table 7
Wilcoxon rank sum test for the comparison of performance on the chromatic number problem.

Table 8
Numerical results of DEA-PPM, HEAD and PLSCOL for the $k$-coloring problem.

problems except for DSJC1000.9 and flag_300_28_0. Accordingly, the average rank of DEA-PPM is 1.16, better than 1.94 of PLSCOL and 1.38 of HEAD. The global exploration improved by the population-based distribution strategy and the IVR contributes to faster convergence of

DEA-PPM for the complicated benchmark problems, however, increases the generational complexity of DEA-PPM, which leads to its slightly increased running time in some small-scale problems. Consequently, DEA-PPM gets the first place with the average running-time rank 1.83.

Further investigation of the performance is conducted by the Wilcoxon rank sum test of running time. With a significance level of 0.05 , the results are presented in Table 9 , where " P " is the $p$-value of hypothesis test. While both HEAD and DEA-PPM cannot get legal color assignments for flat300_28_0, the Wilcoxon rank sum test is conducted by the conflict numbers of 30 independent runs.

It is shown that DEA-PPM performs better than PLSCOL for 2 of 9 selected instances with vertex number less than 500, and better than HEAD for 3 of 9 problems, but performs a bit worse than PLSCOL and HEAD for most of small-scale instances. However, It outperforms PLSCOL and HEAD on the vast majority of instances with vertex number greater than or equal to 500. Therefore, we can conclude that DEA-PPM is competitive to PLSCOL and HEAD on large-scale GCPs, which is attributed to the composite function of the population-based distribution evolution mechanism and the IVR strategy.

## 6. Conclusion and future work

To address the graph coloring problems efficiently, this paper develops a distribution evolutionary algorithm based on a population of probability model (DEA-PPM). Incorporating the merits of the respective probability models in EDAs and QEAs, we introduce a novel distribution model, for which an orthogonal exploration strategy is

Table 9
Results of Wilcoxon rank-sum test for performance comparison.
proposed to explore the probability space efficiently. Meanwhile, an inherited initialization is employed to accelerate the process of color assignment.

- Assisted by an iterative vertex removing strategy and a TS-based local search process, DEA-PPM can achieve excellent performance with small populations, which contributes to its competitiveness on the chromatic number problem.
- Since the population-based evolution leads to slightly increased generational time complexity of DEA-PPM, its running time for the small-scale $k$-coloring problems is a bit higher than that of the individual-based PLSCOL and HEAD.
- DEA-PPM achieves overall outperformance on benchmark problems with vertex numbers greater than 500, because its enhanced global exploration improves the ability of escaping from the local optimal solutions.
- The iterative vertex removal strategy reduces sizes of the graphs to be colored, which likewise improves the coloring performance of DEA-PPM.

The proposed DEA-PPM could be extended to other complex problems. To further improve the efficiency of DEA-PPM, our future work will focus on the adaptive regulation of population size, and the local exploitation is anticipated to be enhanced by utilizing the mathematical characteristics of graph instance. Moreover, we will try to develop a general framework of DEA-PPM to address a variety of combinatorial optimization problems.

# CRediT authorship contribution statement 

Yongjian Xu: Writing - original draft, Software. Huabin Cheng: Formal analysis, Writing - original draft. Ning Xu: Conceptualization, Funding acquisition. Yu Chen: Supervision, Writing - review \& editing, Funding acquisition. Chengwang Xie: Supervision, Funding acquisition.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request

## Acknowledgments

This research was supported in part by the National Key R \& D Program of China [grant number 2021ZD0114600], in part by the Fundamental Research Funds for the Central Universities [grant number WUT:2020IB006], and in part by the National Nature Science Foundation of China [grant number 61763010] as well as the Natural Science Foundation of Guangxi [grant number 2021GXNSFAA075011].
