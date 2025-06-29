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

| Tested parameter |  |  | P values |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Parameter | Settings | flat300_28_0 | le450_15c | le450_15d | DSJC500.5 | flat1000_50_0 | flat1000_76_0 |  |  |  |  |
| $n p$ | $(4,6,8,10,12)$ | 0.162 | 0.548 | 0.404 | $\mathbf{0 . 0 0 4}$ | $\mathbf{0 . 0 0 1}$ | $\mathbf{0 . 0 0 1}$ |  |  |  |  |
| $\alpha$ | $(0.1,0.15,0.2,0.25,0.3)$ | 0.622 | 0.643 | 0.357 | $\mathbf{0 . 0 0 3}$ | 0.268 | $\mathbf{0 . 0 0 0}$ |  |  |  |  |
| iter $_{\text {max }}$ | $(0.5,1,1.5,2.0,2.5) \times 10^{4}$ | 0.025 | 0.146 | $\mathbf{0 . 0 0 0}$ | $\mathbf{0 . 0 4 0}$ | $\mathbf{0 . 0 0 0}$ | $\mathbf{0 . 0 0 0}$ |  |  |  |  |

Table 2
Candidate parameter settings of DEA-PPM.

| Parameter | Setting |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | $S_{1}$ | $S_{2}$ | $S_{3}$ | $S_{4}$ | $S_{5}$ | $S_{6}$ | $S_{7}$ | $S_{8}$ | $S_{9}$ | $S_{10}$ | $S_{11}$ |
| $n p$ | 4 | 4 | 4 | 4 | 4 | 8 | 8 | 8 | 8 | 8 | 8 |
| $\alpha$ | 0.1 | 0.1 | 0.1 | 0.2 | 0.2 | 0.1 | 0.1 | 0.1 | 0.2 | 0.2 | 0.2 |
| Iter $_{\text {max }}$ | 5000 | 10000 | 20000 | 5000 | 10000 | 20000 | 5000 | 10000 | 20000 | 5000 | 10000 | 20000 |

Table 3
Parameter setting of the DEA-PPM for numerical experiments.

| Parameter | Setting | Description |
| :-- | :-- | :-- |
| $n p$ | 8 | Population size of $\mathbf{Q}(t)$ and $\mathbf{P}(t)$; |
| $\alpha$ | 0.2 | Regulation parameter in Eq. (7); |
| iter $_{\text {max }}$ | $5 \times 10^{3}$ | Iteration budget for the TX; |
| $p_{0}$ | 0.98 | Parameter for update of $\mathbf{Q}(t)$; |
| $\Delta R_{i}$ | 0.05 e | Parameter in Eq. (8); |
| $\lambda$ | 0.5 | Parameter in Eq. (9); |
| $r$ | Randomly selected from $(0.2,0.8)$ | Parameter in Algorithm 5; |
| $P_{i}$ | 0.4 | Parameter in Algorithm 7; |

for $k$-coloring of the easy benchmark problems (DSJC500.1 ( $k=12$ ), le450_15c $(k=15)$, led450_15d $(k=15))$ and the hard benchmark problems(DSJC500.5 $(k=48)$, DSJC1000.1 $(k=20)$, DSJC1000.9 $(k=$ 226)). The box plots imply that with the employment of the orthogonal exploration strategy, DEA-PPM-O performs generally better than DEA-PPM-N, resulting in smaller values of the median value, the quantiles and the standard deviations of running time.

The positive impact of exploitation strategy is verified by comparing the DEA-PPM with exploitation (DEA-PPM-E) with the variant without exploitation (DEA-PPM-W), and the box plots of running time are included in Fig. 5. It is demonstrated that DEA-PPM-E generally outperforms DEA-PPM-W in terms of the median value, the quantiles and the standard deviation of running time.

Besides the statistical comparison regarding the exact values of running time, we perform a further comparison by the Wilcoxon rank sum test with a significance level of 0.05 , where the statistical test is based on the sorted rank of running time instead of its exact values. The results are included in Table 4, where "P" is the $p$-value of hypothesis test. For the test conclusion "R", " + ", " - " and " - " indicate that the performance of DEA-PPM is better than, worse than and incomparable to that of the compared variant, respectively. The results demonstrate that DEA-PPM outperforms DEA-PPM-N and DEA-PPM-W on two instances, and is not inferior to them for all benchmark problems. It

Table 4
Wilcoxon rank-sum test for the evolution strategies of distribution population.

| Instance | DEA-PPM-N |  |  | DEA-PPM-W |  |
| :-- | :-- | :-- | :-- | :-- | :-- |
|  | P | R | P | R |  |
| DSJC500.1 | $1.08 \mathrm{E}-01$ | - | $9.25 \mathrm{E}-01$ | - |
| le450_15c | $6.36 \mathrm{E}-01$ | - | $4.99 \mathrm{E}-02$ | + |
| le450_15d | $2.50 \mathrm{E}-01$ | - | $7.76 \mathrm{E}-01$ | - |
| DSJC500.5 | $4.97 \mathrm{E}-02$ | + | $5.29 \mathrm{E}-02$ | - |
| DSJC1000.1 | $6.56 \mathrm{E}-03$ | + | $4.57 \mathrm{E}-01$ | - |
| DSJC1000.9 | $7.15 \mathrm{E}-01$ | - | $4.68 \mathrm{E}-05$ | + |
| $+/-1-$ | $2 / 4 / 0$ |  | $2 / 4 / 0$ |  |

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

| Algorithms | Parameters | Description | Values |
| :--: | :--: | :--: | :--: |
| SDGC | $i t$ | The number of iterations; | $1 \times 10^{5}$ |
| MACOL | $\begin{aligned} & p \\ & \alpha \\ & p_{s} \\ & \lambda \end{aligned}$ | Size of population; <br> Depth of TS; <br> Number of parents for crossover; <br> Probability for accepting worse offspring; <br> Parameter for goodness score function; | $\begin{aligned} & 20 \\ & 1 \times 10^{3} \\ & \text { A random number in }\{2 \ldots, 6\} \\ & 0.2 \\ & 0.08 \end{aligned}$ |
| SDMA | $\begin{aligned} & \beta \\ & \sigma_{\omega} \\ & \sigma \end{aligned}$ | Search depth of weight tabu coloring; <br> Tabu tenure of weight tabu coloring; <br> Tabu tenure of perturbation; <br> Level limit of coarsening phase; <br> Unimproved consecutive rounds for best solution; | $\begin{aligned} & 1 \times 10^{6} \\ & \operatorname{rand}(10)=f^{r} \\ & \operatorname{rand}(1000)=f^{r} \\ & 5 \\ & 10 \end{aligned}$ |
| PLSCOL | $\begin{aligned} & \omega \\ & \alpha \\ & \beta \\ & \gamma \\ & p \end{aligned}$ | Noise probability; <br> Reward factor for correct group; <br> Penalization factor for incorrect group; <br> Compensation factor for expected group; <br> Smoothing coefficient; <br> Smoothing threshold; | $\begin{aligned} & 0.2 \\ & 0.1 \\ & {[0.05,0.45]} \\ & 0.3 \\ & 0.5 \\ & 0.995 \end{aligned}$ |
| HEAD | $\begin{aligned} & \text { Iter }_{T C} \\ & \text { Iter }_{c, c, t} \end{aligned}$ | Depth of TS; <br> The number of generations into one cycle; | $\begin{aligned} & 1 \times 10^{5} \\ & 10 \end{aligned}$ |

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

| Instance | $\chi(G)$ | Algorithm | $k_{\text {min }}$ | $k_{\text {max }}$ | $k_{\text {max }}$ | $k_{\text {std }}$ | Instance | $\chi(G)$ | Algorithm | $k_{\text {min }}$ | $k_{\text {max }}$ | $k_{\text {max }}$ | $k_{\text {std }}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| fpool2_i_2 | 30 | SDGC | 85.4 | 79 | 91 | 3.71 | le450_15c | 15 | SDGC | 29.07 | 28 | 32 | 1.46 |
|  |  | MACOL | 88.3 | 88 | 89 | 0.46 |  |  | MACOL | 19.4 | 18 | 21 | 1.2 |
|  |  | SDMA | 59.41 | 53 | 73 | 6.22 |  |  | SDMA | 30.93 | 28 | 38 | 3.12 |
|  |  | PLSCOL | 73 | 71 | 77 | 1.75 |  |  | PLSCOL | 16.1 | 15 | 17 | 0.4 |
|  |  | HEAD | 74.7 | 71 | 78 | 1.97 |  |  | HEAD | 15.87 | 15 | 16 | 0.34 |
|  |  | DEA-PPM | 30 | 30 | 30 | 0 |  |  | DEA-PPM | 15 | 15 | 15 | 0 |
| fpool2_i_3 | 30 | SDGC | 85.5 | 79 | 95 | 4.35 | le450_15d | 15 | SDGC | 30.27 | 27 | 34 | 2.24 |
|  |  | MACOL | 88 | 87 | 89 | 0.45 |  |  | MACOL | 18.7 | 17 | 21 | 1.35 |
|  |  | SDMA | 57.86 | 51 | 65 | 5.28 |  |  | SDMA | 32.72 | 31 | 38 | 2.17 |
|  |  | PLSCOL | 71.67 | 66 | 77 | 3.47 |  |  | PLSCOL | 16.33 | 16 | 17 | 0.47 |
|  |  | HEAD | 75.57 | 73 | 78 | 1.54 |  |  | HEAD | 15.93 | 15 | 16 | 0.25 |
|  |  | DEA-PPM | 30 | 30 | 30 | 0 |  |  | DEA-PPM | 15 | 15 | 15 | 0 |
| flat300_26_0 | 26 | SDGC | 40.5 | 38 | 44 | 1.5 | DSJC500_1 | 12 | SDGC | 16.67 | 16 | 18 | 0.79 |
|  |  | MACOL | 31.8 | 31 | 32 | 0.4 |  |  | MACOL | 13 | 13 | 13 | 0 |
|  |  | SDMA | 44.83 | 43 | 51 | 3.12 |  |  | SDMA | 20.76 | 17 | 29 | 3.39 |
|  |  | PLSCOL | 26 | 26 | 26 | 0 |  |  | PLSCOL | 12.77 | 12 | 13 | 0.42 |
|  |  | HEAD | 26 | 26 | 26 | 0 |  |  | HEAD | 13 | 13 | 13 | 0 |
|  |  | DEA-PPM | 26 | 26 | 26 | 0 |  |  | DEA-PPM | 12 | 12 | 12 | 0 |
| flat300_28_0 | 28 | SDGC | 40.83 | 40 | 42 | 0.58 | DSJC1000_1 | 20 | SDGC | 31.63 | 31 | 32 | 0.48 |
|  |  | MACOL | 32 | 32 | 32 | 0 |  |  | MACOL | 80.37 | 76 | 82 | 2.79 |
|  |  | SDMA | 45.72 | 43 | 54 | 3.64 |  |  | SDMA | 86.21 | 73 | 94 | 5.55 |
|  |  | PLSCOL | 31 | 30 | 32 | 0.73 |  |  | PLSCOL | 21 | 21 | 21 | 0 |
|  |  | HEAD | 31 | 31 | 31 | 0 |  |  | HEAD | 21 | 21 | 21 | 0 |
|  |  | DEA-PPM | 31 | 31 | 31 | 0 |  |  | DEA-PPM | 21 | 21 | 21 | 0 |

Table 7
Wilcoxon rank sum test for the comparison of performance on the chromatic number problem.

| Instance | SDGC |  | MACOL |  | SDMA |  | PLSCOL |  | HEAD |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | P | R | P | R | P | R | P | R | P | R |  |
| fpool2_i_2 | 1.09E-12 | $+$ | 2.90E-13 | $+$ | 1.13E-12 | $+$ | 9.96E-13 | $+$ | 1.11E-12 | $+$ |  |
| fpool2_i_3 | 1.17E-12 | $+$ | 1.59E-13 | $+$ | 1.13E-12 | $+$ | 1.12E-12 | $+$ | 1.03E-12 | $+$ |  |
| flat300_26_0 | 7.98E-13 | $+$ | 1.55E-13 | $+$ | 1.11E-12 | $+$ | 4.81E-11 | - | 6.73E-01 | - |  |
| flat300_28_0 | 4.27E-13 | $+$ | 1.69E-14 | $+$ | 1.05E-12 | $+$ | 6.31E-01 | - | 0.028 | $+$ |  |
| le450_15c | 8.93E-13 | $+$ | 7.31E-13 | $+$ | 1.13E-12 | $+$ | 2.05E-10 | $+$ | 1.97E-11 | $+$ |  |
| le450_15d | 1.05E-12 | $+$ | 5.16E-13 | $+$ | 9.63E-13 | $+$ | 3.37E-13 | $+$ | 7.15E-13 | $+$ |  |
| DSJC500_1 | 6.21E-13 | $+$ | 1.69E-14 | $+$ | 9.31E-13 | $+$ | 1.47E-09 | $+$ | 1.69E-14 | $+$ |  |
| DSJC1000_1 | 3.80E-13 | $+$ | 1.09E-12 | $+$ | 1.15E-12 | $+$ | 2.74E-11 | - | 3.73E-09 | - |  |
| $+/-1$ | 8/0/0 |  | 8/0/0 |  | 8/0/0 |  | 5/1/2 |  | 6/1/1 |  |  |

Table 8
Numerical results of DEA-PPM, HEAD and PLSCOL for the $k$-coloring problem.

| Instance | $k$ | PLSCOL |  | HEAD |  | DEA-PPM |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | SR | T(s) | SR | T(s) | SR | T(s) |
| DSJC125.5 | 17 | 30/30 | 0.31 | 30/30 | 0.55 | 30/30 | 0.65 |
| DSJC125.9 | 44 | 30/30 | 0.08 | 30/30 | 0.12 | 30/30 | 0.39 |
| DSJC250.5 | 28 | 30/30 | 17.60 | 30/30 | 37.03 | 30/30 | 23.93 |
| DSJC250.9 | 72 | 30/30 | 6.22 | 30/30 | 7.20 | 30/30 | 42.97 |
| DSJC500.1 | 12 | 9/30 | 3140.21 | 29/30 | 1655.11 | 30/30 | 226.14 |
| DSJC500.5 | 48 | 0/30 | 3600 | 30/30 | 1176.30 | 30/30 | 771.39 |
| DSJC500.9 | 126 | 0/30 | 3600 | 1/30 | 3504.49 | 3/30 | 3346.64 |
| DSJC1000.1 | 20 | 0/30 | 3600 | 0/30 | 3600 | 30/30 | 902.53 |
| DSJC1000.5 | 85 | 0/30 | 3600 | 30/30 | 2575.73 | 23/30 | 2271.70 |
| DSJC1000.9 | 225 | 0/30 | 3600 | 19/30 | 2784.67 | 12/30 | 3240.40 |
| le450_15c | 15 | 0/30 | 3600 | 30/30 | 400.85 | 30/30 | 9.34 |
| le450_15d | 15 | 0/30 | 3600 | 27/30 | 1121.86 | 30/30 | 24.60 |
| flat300_20_0 | 20 | 30/30 | 0.11 | 30/30 | 0.20 | 30/30 | 0.81 |
| flat300_26_0 | 26 | 30/30 | 3.47 | 30/30 | 8.81 | 30/30 | 15.46 |
| flat300_28_0 | 30 | 5/30 | 3196.66 | 0/30 | 3600 | 0/30 | 3600 |
| flat1000_50_0 | 50 | 30/30 | 159.32 | 30/30 | 433.27 | 30/30 | 636.96 |
| flat1000_60_0 | 60 | 30/30 | 347.74 | 30/30 | 580.71 | 30/30 | 843.81 |
| flat1000_76_0 | 84 | 0/30 | 3600 | 23/30 | 2834.23 | 30/30 | 2139.33 |
| Average rank |  | 1.94 | 2 | 1.38 | 2.05 | 1.16 | 1.83 |

problems except for DSJC1000.9 and flag_300_28_0. Accordingly, the average rank of DEA-PPM is 1.16, better than 1.94 of PLSCOL and 1.38 of HEAD. The global exploration improved by the population-based distribution strategy and the IVR contributes to faster convergence of

DEA-PPM for the complicated benchmark problems, however, increases the generational complexity of DEA-PPM, which leads to its slightly increased running time in some small-scale problems. Consequently, DEA-PPM gets the first place with the average running-time rank 1.83.

Further investigation of the performance is conducted by the Wilcoxon rank sum test of running time. With a significance level of 0.05 , the results are presented in Table 9 , where " P " is the $p$-value of hypothesis test. While both HEAD and DEA-PPM cannot get legal color assignments for flat300_28_0, the Wilcoxon rank sum test is conducted by the conflict numbers of 30 independent runs.

It is shown that DEA-PPM performs better than PLSCOL for 2 of 9 selected instances with vertex number less than 500, and better than HEAD for 3 of 9 problems, but performs a bit worse than PLSCOL and HEAD for most of small-scale instances. However, It outperforms PLSCOL and HEAD on the vast majority of instances with vertex number greater than or equal to 500. Therefore, we can conclude that DEA-PPM is competitive to PLSCOL and HEAD on large-scale GCPs, which is attributed to the composite function of the population-based distribution evolution mechanism and the IVR strategy.

## 6. Conclusion and future work

To address the graph coloring problems efficiently, this paper develops a distribution evolutionary algorithm based on a population of probability model (DEA-PPM). Incorporating the merits of the respective probability models in EDAs and QEAs, we introduce a novel distribution model, for which an orthogonal exploration strategy is

Table 9
Results of Wilcoxon rank-sum test for performance comparison.

| Instance $(n<500)$ | PLSCOL |  | HEAD |  | Instance $(n \geq 500)$ | PLSCOL |  | HEAD |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | P | R | P | R |  | P | R | P | R |
| DSJC125.5 | 4.00E-03 | - | 0.46 | - | DSJC500.1 | 1.96E-10 | $+$ | 1.10E-11 | $+$ |
| DSJC125.9 | 3.01E-11 | - | 3.00E-03 | - | DSJC500.5 | 1.21E-12 | $+$ | 2.00E-03 | $+$ |
| DSJC250.5 | 0.22 | - | 0.38 | - | DSJC500.9 | 0.08 | - | 0.34 | - |
| DSJC250.9 | 6.01E-08 | - | 6.53E-08 | - | DSJC1000.1 | 1.21E-12 | $+$ | 1.21E-12 | $+$ |
| le450_15c | 5.05E-13 | $+$ | 1.40E-11 | $+$ | DSJC1000.5 | 5.85E-09 | $+$ | 0.06 | - |
| le450_15d | 5.05E-13 | $+$ | 1.40E-11 | $+$ | DSJC1000.9 | 1.53E-04 | $+$ | 0.03 | $+$ |
| flat300_20_0 | 3.01E-11 | - | 3.01E-11 | - | flat1000_50_0 | 3.02E-11 | - | 1.75E-05 | - |
| flat300_26_0 | 8.15E-11 | - | 1.39E-06 | - | flat1000_60_0 | 8.99E-11 | - | 6.36E-05 | - |
| flat300_28_0 | 0.02 | - | 4.62E-05 | $+$ | flat1000_76_0 | 3.45E-07 | $+$ | 0.02 | $+$ |
| $+/-$ | $2 / 1 / 6$ |  | $3 / 2 / 4$ |  | $+/-$ | $6 / 1 / 2$ |  | $5 / 2 / 2$ |  |

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

## References

[1] G.W. Greenwood, Using differential evolution for a subclass of graph theory problems, IEEE Trans. Evol. Comput. 13 (2009) 1190-1192.
[2] F.J.A. Artacho, R. Campoy, V. Elser, An enhanced formulation for solving graph coloring problems with the douglas-rachford algorithm, J. Global Optim. 77 (2020) 383-403.
[3] O. Goudet, B. Duval, J.-K. Hao, Population-based gradient descent weight learning for graph coloring problems, Knowl.-Based Syst. 212 (2021) 106581.
[4] T. Mostafais, F. Modarros Khiyabani, N.J. Navimipour, A systematic study on meta-heuristic approaches for solving the graph coloring problem, Comput. Oper. Res. 120 (2020) 104850.
[5] P. Galinier, A. Hertz, A survey of local search methods for graph coloring, Comput. Oper. Res. 33 (9) (2006) 2547-2562.
[6] M. Dorigo, M. Birattari, T. Snietzle, Ant colony optimization - artificial ants as a computational intelligence technique, IEEE Computat. Intell. Mag. 1 (4) (2006) $28-39$.
[7] M. Hauschild, M. Pelikan, An introduction and survey of estimation of distribution algorithms, Swarm Evol. Comput. 1 (3) (2011) 111-128.
[8] H. Xiong, Z. Wu, H. Fan, G. Li, G. Jiang, Quantum rotation gate in quantumimpired evolutionary algorithm: A review, analysis and comparison study, Swarm Evol. Comput. 42 (2018) 43-57.
[9] O. Titlioye, A. Crispin, Quantum annealing of the graph coloring problem, Discrete Optim. 8 (2) (2011) 376-384.
[10] A.J. Pal, B. Ray, N. Zakaria, S.S. Sarma, Comparative performance of modified simulated annealing with simple simulated annealing for graph coloring problem, Procedia Comput. Sci. 9 (2012) 321-327.
[11] C. Avanthay, A. Hertz, N. Zufferey, A variable neighborhood search for graph coloring, European J. Oper. Res. 151 (2) (2003) 379-388.
[12] A. Hertz, D. de Werra, Using tabu search techniques for graph coloring, Computing 39 (1987) 345-351.
[13] D.C. Porumbel, J.-K. Hao, P. Kuntz, Informed reactive tabu search for graph coloring, Asia-Pac. J. Oper. Res. 30 (04) (2013) 1350010.
[14] I. Blöchliger, N. Zufferey, A graph coloring heuristic using partial solutions and a reactive tabu scheme, Comput. Oper. Res. 35 (3) (2008) 960-975.
[15] D.C. Porumbel, J.-K. Hao, P. Kuntz, A search space "cartography" for guiding graph coloring heuristics, Comput. Oper. Res. 37 (4) (2010) 769-778.
[16] S.F. Galán, Simple decentralized graph coloring, Comput. Optim. Appl. 66 (2017) $163-185$.
[17] W. Sun, J.-K. Hao, Y. Zang, X. Lai, A solution-driven multilevel approach for graph coloring, Appl. Soft Comput. 104 (2021) 107174.
[18] Y. Peng, X. Lin, B. Choi, B. He, Vcolor*: a practical approach for coloring large graphs, Front. Comput. Sci. 15 (4) (2021) 1-17.
[19] Y. Zhou, J.-K. Hao, B. Duval, Reinforcement learning based local search for grouping problems: A case study on graph coloring, Expert Syst. Appl. 64 (2016) $412-422$.
[20] Y. Zhou, R. Duval, J.-K. Hao, Improving probability learning based local search for graph coloring, Appl. Soft Comput. 65 (2018) 542-553.
[21] L.-Y. Hsu, S.-J. Horng, P. Fan, M.K. Khan, Y.-R. Wang, R.-S. Run, J.-L. Lai, R.-J. Chen, MTPSO algorithm for solving planar graph coloring problem, Expert Syst. Appl. 38 (5) (2011) 5525-5531.
[22] H. Hernández, C. Blum, Distributed graph coloring: an approach based on the calling behavior of Japanese tree frogs, Swarm Intell. 6 (2) (2012) 117-150.
[23] I. Rebollo-Ruiz, M. Grada, An empirical evaluation of gravitational swarm intelligence for graph coloring algorithm, Neurocomputing 132 (2014) 79-84.
[24] R. Zhao, Y. Wang, C. Liu, P. Hu, H. Jelodar, M. Rabbani, H. Li, Discrete selfish herd optimizer for solving graph coloring problem, Appl. Intell. 50 (2020) 1633-1656.
[25] D. Chalupa, P. Nielsen, Parameter-free and cooperative local search algorithms for graph colouring, Soft Comput. 25 (24) (2021) 15035-15050.
[26] L. Zhong, Y. Zhou, G. Zhou, Q. Luo, Enhanced discrete dragonfly algorithm for solving four-color map problems, Appl. Intell. 53 (2023) 6372-6400.

[27] T.N. Bui, T. Nguyen, C.M. Patel, K.-A.T. Phan, An ant-based algorithm for coloring graphs, Discret Appl. Math. 156 (2008) 190-200.
[28] H. Djelloul, A. Layeb, S. Chikhi, Quantum inspired cuckoo search algorithm for graph colouring problem, Int. J. Bio-Inspired Comput. 7 (2015) 183-194.
[29] Z. Lü, J.-K. Hao, A memetic algorithm for graph coloring, European J. Oper. Res. 203 (1) (2010) 241-250.
[30] D.C. Porumbel, J.-K. Hao, P. Kuntz, An evolutionary approach with diversity guarantee and well-informed grouping recombination for graph coloring, Comput. Oper. Res. 37 (10) (2010) 1822-1832.
[31] S. Mahmoudi, S. Lotfi, Modified cuckoo optimization algorithm (MCOA) to solve graph coloring problem, Appl. Soft Comput. 33 (2015) 48-64.
[32] Q. Wu, J.-K. Hao, Coloring large graphs based on independent set extraction, Comput. Oper. Res. 39 (2) (2012) 283-290.
[33] S.M. Douiri, S. Elbernounsi, Solving the graph coloring problem via hybrid genetic algorithms, J. King Saud Univ.: Eng. Sci. 27 (2015) 114-118.
[34] M. Bessedik, B. Toufik, H. Drias, How can bees colour graphs, Int. J. Bio-Inspired Comput. 3 (2011) 67-76.
[35] M.R. Mirsaleh, M.R. Meybodi, A michigan memetic algorithm for solving the vertex coloring problem, J. Comput. Sci. 24 (2018) 389-401.
[36] L. Moalic, A. Gondran, Variations on memetic algorithms for graph coloring problems, J. Heuristics 24 (1) (2018) 1-24.
[37] A.F.d. Silva, L.G.A. Rodriguez, J.F. Filho, The improved ColourAnt algorithm: a hybrid algorithm for solving the graph colouring problem, Int. J. Bio-Inspired Comput. 16 (1) (2020) 1-12.
[38] V.A. Shim, K.C. Tan, C.Y. Cheong, J.Y. Chia, Enhancing the scalability of multiobjective optimization via restricted Boltzmann machine-based estimation of distribution algorithm, Inform. Sci. 248 (2013) 191-213.
[39] S. Ivvan Valdez, A. Hernandez, S. Botello, A Boltzmann based estimation of distribution algorithm, Inform. Sci. 236 (2013) 126-137.
[40] L. PourMohammadhagher, M.M. Ebadzadeh, R. Safabakhsh, Graphical model based continuous estimation of distribution algorithm, Appl. Soft Comput. 58 (2017) $388-400$.
[41] W. Dong, Y. Wang, M. Zhou, A latent space-based estimation of distribution algorithm for large-scale global optimization, Soft Comput. 23 (13) (2019) $4593-4615$.
[42] A. Zhou, J. Sun, Q. Zhang, An estimation of distribution algorithm with cheap and expensive local search methods, IEEE Trans. Evol. Comput. 19 (6) (2015) $807-822$.
[43] Q. Dang, W. Gao, M. Gong, An efficient mixture sampling model for gaussian estimation of distribution algorithm, Inform. Sci. 608 (2022) 1157-1182.
[44] J. Péna, J. Lozano, P. Larrahaga, Globally multimodal problem optimization via an estimation of distribution algorithm based on unsupervised learning of Bayesian networks, Evol. Comput. 13 (1) (2005) 43-66.
[45] P. Yang, K. Tang, X. Lu, Improving estimation of distribution algorithm on multimodal problems by Detecting Promising Areas, IEEE Trans. Cybern. 45 (8) (2015) 1438-1449.
[46] Z. Ren, Y. Liang, L. Wang, A. Zhang, B. Pang, B. Li, Anisotropic adaptive variance scaling for Gaussian estimation of distribution algorithm, Knowl.-Based Syst. 146 (2018) 142-151.
[47] Y. Liang, Z. Ren, X. Yao, Z. Feng, A. Chon, W. Guo, Enhancing Gaussian estimation of distribution algorithm by exploiting evolution direction with archive, IEEE Trans. Cybern. 50 (1) (2020) 140-152.
[48] F. Wang, Y. Li, A. Zhou, K. Tang, An estimation of distribution algorithm for mixed-variable newsvendor problems, IEEE Trans. Evol. Comput. 24 (3) (2020) $479-493$.
[49] T. Liu, X. Li, L. Tan, S. Song, An incremental-learning model-based multiobjective estimation of distribution algorithm, Inform. Sci. 569 (2021) 430-449.
[50] K.-H. Han, J.-H. Kim, Quantum-inspired evolutionary algorithm for a class of combinatorial optimization, IEEE Trans. Evol. Comput. 6 (2002) 580-593.
[51] B. Yu, K. Yuan, B. Zhang, D. Ding, D.Z. Pan, Layout decomposition for triple patterning lithography, in: 2011 IEEE/ACM International Conference on Computer-Aided Design (ICCAD), 2011, pp. 1-8.
[52] S.T. Hedetniemi, D.P. Jacobs, P.K. Srimani, Linear time self-stabilizing colorings, Inform. Process. Lett. 87 (2003) 251-255.
[53] W. Greub, Linear Algebra, Springer, 1975.
[54] R. Kress, Numerical Analysis, Springer, 1998.
[55] P. Galinier, J.-K. Hao, Hybrid evolutionary algorithms for graph coloring, J. Comb. Optim. 3 (1999) 379-397.