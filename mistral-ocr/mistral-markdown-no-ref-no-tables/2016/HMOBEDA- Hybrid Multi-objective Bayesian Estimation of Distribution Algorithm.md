# HMOBEDA: Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm 

Marcella S. R. Martins<br>Federal University of<br>Technology - Paraná (UTFPR)<br>Av. Sete de Setembro, 3165<br>Curitiba PR, Brazil<br>marcella@utfpr.com.br<br>Ricardo Lüders<br>Federal University of<br>Technology - Paraná (UTFPR)<br>Av. Sete de Setembro, 3165<br>Curitiba PR, Brazil<br>luders@utfpr.edu.br

## Myriam R. B. S. Delgado Federal University of Technology - Paraná (UTFPR) <br> Av. Sete de Setembro, 3165 <br> Curitiba PR, Brazil myriamdelg@utfpr.edu.br

Richard Aderbal Gonçalves<br>Midwest State University of<br>Parana (UNICENTRO)<br>Guarapuava, PR, Brazil<br>richard@unicentro.br

Roberto Santana<br>University of the Basque Country (UPV/EHU)<br>20018 Donostia<br>San Sebastián, Spain<br>roberto.santana@ehu.es

Carolina Paula de Almeida<br>Midwest State University of<br>Parana (UNICENTRO)<br>Guarapuava, PR, Brazil<br>carol@unicentro.br


#### Abstract

Probabilistic modeling of selected solutions and incorporation of local search methods are approaches that can notably improve the results of multi-objective evolutionary algorithms (MOEAs). In the past, these approaches have been jointly applied to multi-objective problems (MOPs) with excellent results. In this paper, we introduce for the first time a joint probabilistic modeling of (1) local search methods with (2) decision variables and (3) the objectives in a framework named HMOBEDA. The proposed approach is compared with six evolutionary methods (including a modified version of NSGA-III, adapted to solve combinatorial optimization) on instances of the multi-objective knapsack problem with 3,4 , and 5 objectives. Results show that HMOBEDA is a competitive approach. It outperforms the other methods according to the hypervolume indicator.


## 1. INTRODUCTION

Nowadays, a number of metaheuristics have been developed for efficiently solving multi-objective optimization problems. Among these techniques, evolutionary algorithms are particularly popular, due to their promise of using a population to move towards an entire set of good solutions in a single run. However, for many combinatorial problems, multiobjective optimization evolutionary algorithms (MOEAs), by themselves, are not able to successfully find good solutions. Two strategies have shown to be particularly suited to improve results from MOEAs: local optimizers and probabilistic modeling to capture and exploit the potential regularities that arise in the promising solutions.

[^0]Hybrid algorithms that combine traditional evolutionary operators with local search (LS) procedures have attracted considerable attention from the MOEA community [19]. As pointed out by [9], a number of researchers have acknowledged that these hybrid approaches can often achieve good performance for many MOPs. However, they still present challenges regarding local optimizers, like the choice of the right parameters (e.g., the type, frequency and intensity of LS applied on a specific candidate solution).

Frequency and intensity directly define the degree of evolution (exploration) versus exploitation (performed by LS) in these hybrid approaches [20]. Clearly, a more intense procedure provides greater chances of convergence to the local optima but limits the amount of exploration that could be performed without incurring in an excessive computational cost. Therefore, for a fixed computational budget, care should be taken when setting these two parameters. Moreover, when only a subset of individuals undergo local optimization, the issue of which will be chosen must also be considered. Finally, the type of LS performed favors different neighborhood structures. All previous discussed parameters greatly affect the algorithm's performance.

The other strategy is probabilistic modelling, widely used in Estimation of distribution algorithms (EDAs) [24] a computational approach that, instead of applying genetic operators, learn a probabilistic model from a set of promising solutions, and sample new candidate solutions from the model. The probabilistic model can capture relevant statistics about problem variables and important dependencies existing among these variables.

EDAs developed to solve multi-objective problems [16] are usually called Multi-objective Estimation of Distribution Algorithm (MOEDAs). Although in MOEDAs the probabilistic model generally represents only the relationships between decision variables, the work proposed in [16] shows the effectiveness of also modelling objectives.

At the same time, hybrid approaches have been developed by integrating LS methods as part of a MOEDA [23, 43]. Although hybrid MOEDAs which incorporate LS methods represent a powerful class of algorithms to deal with MOPs, they inherit from hybrid MOEAs the challenge of finding out


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
    GECCO '16, July 20-24, 2016, Denver, CO, USA
    (C) 2016 ACM. ISBN 978-1-4503-4206-5/16/07... $\$ 15.00$

    DOI: http://dx.doi.org/10.1145/2908812.2908826

an optimal setting of LS parameters. This question is particularly relevant because at different phases of the search the requirements for the application of LS can be very different. Furthermore, in an ideal setting we would tune the parameters of the local optimizer according to the characteristics of the solution to which the local optimizer is applied (e.g. the current values of the different objectives provided by those variables). One alternative to deal with this question is to encode the LS parameters as part of the representation of problem solution as done in previous EAs $[1,39]$.

In this paper we propose a different approach aiming to benefit from a probabilistic modeling-based approach. The proposal is a joint probabilistic modeling of decision variables, objectives, and parameters of the local optimizer. The rationale is that the probabilistic model could learn which is the appropriate choice of the local optimization parameters for different configurations of decision variables and objective values.

The introduced approach is evaluated on a combinatorial MOP - the multi-objective version of the well known knapsack problem named Multi-objective Knapsack Problem (MOKP). The performance of MOEAs for this problem has been extensively investigated [12, 37, 44]. In particular, MOEDAs that use different types of probabilistic models have already been applied to MOKP. In [23], a hybrid MOEDA based on an univariate probabilistic model is used to solve the $0 / 1$ MOKP. In [39], a hybrid EDA that uses an adaptive local search (HEDA) is proposed to enhance the exploitation ability of the EDA to solve the multidimensional knapsack problem. MOEDAs based on Bayesian networks have also been applied to MOKP in [22, 32].

Our work is built on previous results that investigate the application of LS to MOEDAs [30, 42]. It is also linked to the work presented in [16] in which a joint probabilistic model of objectives and variables is proposed, and related to [23] by considering a LS based on the weighted sum method. However, none of these previous works consider a joint probabilistic model of objectives, variables and LS parameters.

This paper is organized as follows. Section 2 presents the principles of the theory used in the paper. Section 3 details our proposed approach. Results from numerical experiments are shown and discussed in Section 4, with the conclusions and future directions presented in Section 5.

## 2. BACKGROUND

This section presents a background on multi-objective optimization, with a special attention dedicated to the multiobjective knapsack problem, and the basic concepts associated to EDAs.

### 2.1 Multi-objective optimization

A general multi-objective optimization problem (MOP) includes decision variables, objective functions, and constraints where objective functions and constraints are functions of the decision variables [33, 44]. Mathematically, a maximization MOP can be defined as:

$$
\begin{aligned}
& \max _{\mathbf{x}} \mathbf{y}=\mathbf{f}(\mathbf{x})=\left(f_{1}(\mathbf{x}), f_{2}(\mathbf{x}), \ldots, f_{m}(\mathbf{x})\right) \\
& \text { subject to } \mathbf{h}(\mathbf{x})=\left(h_{1}(\mathbf{x}), h_{2}(\mathbf{x}), \ldots, h_{k}(\mathbf{x})\right) \leq 0 \\
& \mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right) \in X \\
& \mathbf{y}=\left(y_{1}, y_{2}, \ldots, y_{m}\right) \in Y
\end{aligned}
$$

where $\mathbf{x}$ is the decision vector, $X$ is the variable space, $\mathbf{y}$ is
the objective vector, $Y$ is the objective space and $\mathbf{h}(\mathbf{x}) \leq 0$ is the set of constraints which determines a set of feasible solutions $X_{f}$.

The set of solutions of MOP includes decision vectors for which the corresponding objective vectors cannot be improved in any dimension without degradation in another - these vectors are called Pareto optimal set. The idea of Pareto optimality is based on the Pareto dominance. A decision vector $\mathbf{u}$ dominates a decision vector $\mathbf{v}$ iff $f_{i}(\mathbf{u}) \geq f_{i}(\mathbf{v})$ for $i=1,2, . ., m$ with $f_{i}(\mathbf{u})>f_{i}(\mathbf{v})$ for at least one $i$. The vector $\mathbf{u}$ is called Pareto optimal if there is no vector $\mathbf{v}$ which dominates vector $\mathbf{u}$ in the decision space $X$. In the objective space the set of nondominated solutions lies on a surface known as Pareto optimal front. The goal of the optimization is to find a representative sampling of solutions along the Pareto optimal front.

The $0 / 1$ knapsack problem is a widely studied problem due to its practical importance. Recently, the multi-objective generalization of this problem has been well studied and many algorithms for solving it have been proposed [12, 37].

In this work we use the multi-objective formulation proposed in [12, 37, 44]. Given a total of $R$ objective functions (knapsacks) and $Q$ items, $a_{r q}$ is the profit of item $q=1, \ldots, Q$, according to knapsack $r=1, \ldots, R, b_{r q}$ denotes the weight of item $q$ according to knapsack $r$, and $c_{r}$ is the constraint capacity of knapsack $r$. The multi-objective knapsack problem can be formulated as follows:

$$
\begin{aligned}
& \max _{\mathbf{x}} \mathbf{z}(\mathbf{x})=\left(z_{1}(\mathbf{x}), \ldots, z_{R}(\mathbf{x})\right) \\
& \text { subject to } \sum_{q=1}^{Q} b_{r q} x_{q} \leq c_{r}, r=1, \ldots, R \\
& \text { with } z_{r}(\mathbf{x})=\sum_{q=1}^{Q} a_{r q} x_{q}, \mathbf{x} \in\{0,1\}^{Q}
\end{aligned}
$$

where $\mathbf{x}$ is a $Q$-dimension binary vector, $a_{r q}, b_{r q}$ and $c_{r}$ are nonnegative coefficients, such that $x_{q}=1$ means that item $q$ is selected to be in all knapsacks.

### 2.2 Estimation of Distribution Algorithms

The main idea of EDAs [24, 27] is to extract and represent, using a probabilistic graphical model (PGM), the regularities shared by a subset of high-valued problem solutions. The PGM then samples new solutions biasing the search to areas where optimal solutions are more likely to be found.

Usually, an EDA starts by generating a random set of solutions. Solutions are then evaluated using one or more objective functions and a subset of them is selected according to a pre-defined criterion. The selected solutions are used to learn a PGM which is then applied to sample new solutions and the cycle of evaluation, selection, modeling, and sampling is repeated until a stop condition is fulfilled.

EDAs have also been applied to solve multi-objective problems. Normally they integrate both, the model building and sampling techniques, into evolutionary multi-objective optimizers using special selection schemes [17, 22]. However, recently the role of the probabilistic model has been extended to model the dependencies between variables and objectives [16]. In addition, MOEDAs can be notably enhanced by adding a local optimizer that can refine the solutions found by sampling from the PGM [23, 39, 43]. In this paper, we use this type of enhancement in the context of multi-objective optimization.

### 2.3 Bayesian Networks as Probabilistic Graphical Model

Bayesian networks (BN) are directed acyclic graphs whose nodes represent variables, and whose missing edges encode conditional independencies between variables. Random variables represented by nodes may be observable quantities, latent variables, unknown parameters or hypotheses. Each node is associated with a probability function that takes as input a particular set of values for the node's parent variables and gives the probability of the variable represented by the node $[6,18]$. Mathematically, an acyclic BN with directed edges encodes a joint probability distribution. This can be written as in 3 :

$$
p(X)=\prod_{i=0}^{n-1} p\left(X_{i} \mid P a_{X_{i}}\right)
$$

where $X=\left(X_{0}, \ldots, X_{n-1}\right)$ is the vector of variables, $P a X_{i}$ is the set of parents of $X_{i}$ in the network (the set of nodes from which there exists an arc to $X_{i}$ ) and $p\left(X_{i} \mid P a_{X_{i}}\right)$ is the conditional probability of $X_{i}$ given $P a_{X_{i}}$. This distribution can be used to generate new instances using the marginal and conditional probabilities in a modeled data set. Therefore, BN's are considered the most prominent Probabilistic Graphical Models (PGMs) [21] and often are used for modeling multinomial data with discrete variables [25].

There are three main approaches to learn these PGMs structures: score-based learning, constraint-based learning, and hybrid methods [40]. Score-based learning methods evaluate the quality of Bayesian network structures using a scoring function and selects the best one, like BD-metric [10] and K2-metric [6]. Constraint-based learning methods typically use statistical testing to identify conditional independence relations from the data and build a Bayesian network structure that best fits those relations [25]. Hybrid methods aim to integrate the previous two approaches, like what was done in $[26,38]$.The authors used constraint-based learning to create a skeleton graph and then used score-based learning to find a high-scoring network structure that is a subgraph of the skeleton.

In our implementation, we have used a simple greedy algorithm with only arc additions allowed in order to maximize the value of K2-metric and we also assume a causal relation between objectives and variables/parameters, but different assumptions can be made in the HMOBEDA framework. In the implemented concept, objectives are parents in the network, and variables and parameters are child nodes with no inter-relation among each other.

## 3. THE PROPOSAL: HMOBEDA

In the proposed approach, the goal is to include as part of the probabilistic model not only decision variables, but also objectives and parameters that control the embedded LS. In this section we explain how this strategy can be implemented detailing the proposed algorithm named HMOBEDA.

### 3.1 Encoding scheme

In the EDA population, every individual is represented by a joint vector $(\mathbf{x}, \mathbf{z}, \mathbf{p})=\left(x_{1}, \ldots, x_{Q}, z_{1}, \ldots, z_{R}, p_{1} \ldots p_{L}\right)$, of size $Q+R+L$, denoting the decision variables (i.e. the solution of the addressed problem instance), objectives, and

LS parameters, respectively. The components $\mathbf{x}, \mathbf{z}$ an $\mathbf{p}$ can be specified as:

- $\mathbf{x}$ is a binary vector of items, with element $x_{q} \in\{0,1\}$, $q=1 \ldots Q$, indicating the presence or absence of the associated item;
- $\mathbf{z}$ is a vector of objectives, with element $z_{r}, r=1 \ldots R$, representing the discrete value of $r^{\text {th }}$ objective.
- $\mathbf{p}$ is a vector of elements regarding local search, with element $p_{l}, l=1 \ldots L$, indicating the $l^{\text {th }}$ discrete value associated with the LS procedure - see Section 3.2.3. In this work we assume the following elements: (i) $N_{\text {iter }} \in\{5,6 \ldots, 20\}$ : maximum number of iterations of LS; (ii) $T_{\text {Fcal }} \in\{1,2\}$ : the type of fitness calculation: (1) Linear Combination or (2) Alternation of included objectives in both cases; (iii) $N_{D A d / I n s} \in$ $\{1,2\}$ : neighborhood type: drop-add (1) or insertion (2); (iv) $\left.\mathbf{O b}_{\mathbf{b}}\right|_{\mathbf{0 s}}=\left(b_{1}, \ldots, b_{m}\right)$, where $b_{i} \in\{0,1\}$ : binary vector indicating whether objectives are included or not in the fitness computation of LS neighbors.


### 3.2 HMOBEDA Algorithm

The main steps performed by HMOBEDA are described in Algorithm 1. The proposed algorithm makes use of specific strategies described in the next subsections.

### 3.2.1 Initialization

The Initialization process randomly generates every vector $\mathbf{x}$ and $\mathbf{p}$ of the initial population $P o p^{1}$, a total of $N$ vector solutions are generated. For each solution in Pop ${ }^{1}$ the values of all objectives are calculated based on the objective functions and further discretized to form vector $\mathbf{z}$. Therefore, $N$ joint vectors $(\mathbf{x}, \mathbf{z}, \mathbf{p})$ are obtained to compose the population in the first generation.

### 3.2.2 Non-dominated Sorting

In order to sort individuals of the current population, the proposed approach uses Non-dominated Sorting [35]. This technique sorts the population according to the dominance relationships established among solutions, producing a total of $T o t_{F}$ sub-populations or fronts, $F_{1}, F_{2}, \ldots, F_{T o t_{F}}$. Front $F_{1}$ corresponds to the set of non-dominated solutions (the best front). Sets $F_{i}, i=2, \ldots, T o t_{F}$ contain the nondominated solutions when sets $F_{1}, \ldots, F_{i-1}$ are removed from the whole population. After dominance calculation, a diversity criterion named crowding distance (CD) is computed. Within each $F_{i}$, CD estimates the density of solutions surrounding a particular point $\mathbf{z} \in F_{i}$. For this, the method considers each of the $R$ objectives independently, and sums the distances between the nearest points that have respectively smaller and greater value for the objective [8]. Individuals are sorted taking at first the dominance criterion and secondly, the CD criterion. Finally truncation selection is applied, i.e. the best $N$ solutions are selected ${ }^{1}$.

### 3.2.3 Local search

In this work we implement the hill climbing (HC) local search $[28,36]$ at each generation, aiming to improve a set of solutions selected by the truncation procedure.

[^0]
[^0]:    ${ }^{1}$ This implementation was adapted from [34].

Algorithm 1 HMOBEDA framework
INPUT: $N$, population size;
$N_{P G M}$, number of individuals selected to learn the probabilistic model;
$N_{\text {smp }}$, number of individuals sampled from the probabilistic model;
$\beta$, window of occurrence for the local search;
$M a x_{\text {ger }}$, maximum number of generations of EDA;
OUTPUT: $N D$, the final set of non-dominated solutions; \{Initialization\}
1: $\operatorname{Pop}^{1}(\mathbf{x})=$ RandomVector $(N, Q) ;$ \{repair if necessary \}
2: $\operatorname{Pop}^{1}(\mathbf{z})=$ Fitness $\left(\operatorname{Pop}^{1}(\mathbf{x})\right)$;
3: $\operatorname{Pop}^{1}(\mathbf{p})=$ RandomVector $(N, L)$;
4: $g=1$;
$\{$ EDA: main loop \}
5: while $g \leq$ Max $_{\text {ger }}$ do
6: if $g>1$ \{EDA sampling\} then
7: $\quad \operatorname{Pop}_{\text {smp }}=$ Sampling $(B N P M) ;$ \{repair if necessary \}
8: $\quad \operatorname{Pop}_{\text {smp }}(\mathbf{z})=$ Fitness $\left(\operatorname{Pop}_{\text {smp }}(\mathbf{x})\right) ;$ \{not surrogate assisted \}
9: $\quad \operatorname{Pop}^{\beta}=\left\{\operatorname{Pop}^{\beta-1} \cup \operatorname{Pop}_{\text {smp }}\right\} ;\{$ EDA survival $\}$
10: end if
\{Non-dominated Sorting \}
\{Defines $k$ Pareto fronts from the best $(i=1)$ to the worst, and assigns a crowding distance \}
11: $F_{1} \ldots F_{k}=$ ParetoDominance $\left(\operatorname{Pop}^{\beta}\right)$;
12: $\quad \operatorname{Pop}^{\beta}=$ Select $\left(N, F_{1} \cup \ldots \cup F_{k}\right)$; $\{$ Truncation Selection \}
\{Local search: performed at every $\beta$ generations \}
13: if $((g=1)$ or $(g \bmod \beta=\mathbf{0}))$ then
14: $\quad \operatorname{Pop}_{I}=\left(\operatorname{LS}\left(\operatorname{Pop}^{\beta}\right)\right) ;\{$ repair if necessary $\}$
15: $\quad \operatorname{Pop}^{\beta}=$ ParetoDominance $\left(\operatorname{Pop}_{I}\right)$;
16: else
17: $\quad \operatorname{Pop}_{I}=\emptyset$;
18: end if
\{EDA: learning the probabilistic model \}
19: $\quad \operatorname{Pop}_{P G M}^{g}=\operatorname{Selection}\left(N_{P G M}, \operatorname{Pop}^{\beta}\right)$; $\{$ binary tournament $\}$
20: $\quad B N P M=$ ProbabilisticModelEstimation $\left(\operatorname{Pop}_{P G M}^{\beta}\right)$;
21: $g=g+1$;
22: end while
23: $N D=\operatorname{Pop}^{\beta-1}(\mathbf{x})$;

For every solution in $\operatorname{Pop}^{\beta}$ (population at generation $g$ ), the HC-based local search (HCLS) generates a neighbor, calculates its fitness and compares it with the original solution fitness. If the neighbor is better it takes the original solution's place in $\operatorname{Pop}^{\beta}$. In this work HCLS is applied at every $\beta$ generations (steps 13 to 18 in Algorithm 1).

Neighbors are generated by swapping (drop-add) or inserting an item at a random position of the sequence depending on the $N_{D A d / i_{i k}}$ element of $\mathbf{p}$.

When LS compares the original solution with its neighbor, the fitness computation is based on $\mathbf{O b j}_{\mathbf{i k}}$ and $T_{F c a l}$. It uses a linear combination (aggregation or one objective at a time for all active objectives in the corresponding neighbor and original solution (i.e., $\forall$ objective $i \mid b_{i}=1, b_{i} \in \mathbf{O b j}_{\mathbf{i k}}$ ). The decision between the two types of fitness calculation is set by the $\mathbf{p}$ element $T_{F c a l}$. In the second case, at each iteration (of a total of $N_{\text {iter }}$ performed by HCLS at the current generation
g) a different objective is chosen for the fitness calculation. This method of fitness calculation is based on $[1,23,29,39]$.

### 3.2.4 Probabilistic Modeling

After local search, HMOBEDA starts the PGM construction phase. First, $N / 2$ individuals of $\operatorname{Pop}^{\beta}$ are selected through a binary tournament in the same way used by NSGAII [8]. The procedure randomly selects two solutions from Pop ${ }^{\beta}$. If both solutions belong to front $F_{i}$, the solution with greatest crowding distance is chosen. Otherwise, the solution that lies in the best front is selected. Then, $\operatorname{Pop}_{P G M}^{g}$ is obtained encompassing $N / 2$ good individuals.

In order to learn the probabilistic model, the objective values are discretized providing $t$ discrete values. The discretization process converts objective value into $t$ discrete states considering the maximum possible value for each objective $\left(M a x^{t}\right)$. For each objective $i$, its discrete value is calculated as $\left\lceil\text { objective }^{i} /\left(\text { Max }^{i} / t\right)\right\rceil$. In the experiments, we set $t=10$. BN is modeled using K2-metric and $\mathbf{z}$ data collected from $\operatorname{Pop}_{P G M}^{g}$. BN structure (encompassing local search parameters and objectives, in addition to decision variables) and BN parameters (joint probability distributions) are estimated based on [16].

Figure 1 presents an example of a PGM obtained. The model encodes the joint probabilistic model of $Q$ decision variables, $R$ objectives and $L$ local search parameters. In this figure, $Z$ represents the objectives, $P$ the parameters and $X$ the decision variables. The advantage of HMOBEDA over traditional EDA-based approaches is that besides providing good decision variables (based on the model captured from good solutions present in $\operatorname{Pop}_{P G M}^{g}$ ) it can also provide variables and LS parameters more related with good values of objectives fixed as evidence. This naive Bayesian model is conceived to facilitate the sampling process: fixing objective values enables the estimation of their associated decision variables and LS parameters.
![img-0.jpeg](img-0.jpeg)

Figure 1: An example of a PGM used by HMOBEDA.

The probabilistic model (BNPM) is used to sample the set of new individuals (Pop $p_{\text {smp }}$ ). In this case, not only decision variables $\mathbf{x}$, but also, local search parameters $\mathbf{p}$ can be sampled. Vector $\mathbf{z}$ is calculated based on the fitness function (in the case of surrogate assisted approaches, BNPM can also be used to sample the objective values). New individuals are generated from the joint distribution encoded by the network using probabilistic logic sampling. In this process, vector $\mathbf{z}$ can be fixed as evidence, set with high values (for maximization problems). Therefore, it is possible to obtain a set of solutions and parameters associated with high objective values.

A union of the sampled population (Pop $p_{\text {smp }}$ ) and $\operatorname{Pop}^{\beta}$ is used to create the new population for the next generation $g$, and the main loop HMOBEDA continues until the stop condition is fulfilled. At any stage of the evolutionary process, if

an infeasible solution is generated, HMOBEDA applies the same greedy repair method as in [44]. This method repairs a solution by removing items in an ascending order of the relation profit/weight until the constraints are satisfied.

## 4. EXPERIMENTS AND RESULTS

To analyze the performance of the proposed approach in multi-objective combinatorial optimization, HMOBEDA is evaluated in a set of MOKP instances with different sizes and number of objectives. These instances are considered because they are well explored in many works in the literature and have been previously addressed in [44]. We use six different instances, with 100 and 250 items, for 3,4 and 5 objectives. We characterize each instance as $R-Q$, where $R$ is the number of objectives and $Q$ the number of items.

In this section, we compare HMOBEDAwith HMOBEDA $_{f}$ (i.e., HMOBEDA with fixed parameters), MBN-EDA [16], NSGA-II [8], S-MOGLS (a NSGA-II with local search) [13, 14], MOEA/D [41], and NSGA-III [7, 15]. HMOBEDA $_{f}$ has no LS parameter encoded as a node in the Bayesian network model. It has been included in the comparison to evaluate the benefits of incorporating LS parameters into the probabilistic model. The difference between MBN-EDA and $\mathrm{HMOBEDA}_{f}$ is the LS applied to $\mathrm{HMOBEDA}_{f}$. All algorithms have run in the same computer using MatLab, excepted MOEA/D and NSGA-III which have been adapted from [41] and [4, 7], respectively, using C++.
As commented in Section 2.1, we use the same problem formulation used in [12, 37, 44]. The values of $a_{a}^{r}$ and $b_{a}^{r}$ are specified as integers in the interval $[10,100]$. Like in [44], the capacity $c_{r}$ is specified as $50 \%$ of the sum of all weights related to each knapsack $r$.

### 4.1 Algorithms Settings

The parameters for each algorithm are shown in Table 1.
Table 1: Parameters of algorithms.

HMOBEDA $_{f}$ assumes $T_{F c a l}=0, N_{\text {iter }}=20$ and $N_{D A d / I n s}$ $=0$ (these parameters have been empirically defined). For S-MOGLS we set the probability of LS $\left(P_{t s}\right)$ as 0.1 , the probability of Bit-Flip operation in LS as $4 / 500$, and $N_{t s}=20$, where $N_{t s}$ is the number of neighbors to be examined [13].
For NSGA-III, we use the same configuration used in [7], i.e., the number of reference points $(H)$ defines the population size $N$. For an $R$-objective problem, if $p$ divisions are considered along each objective, [7] defines $H=C_{R+p-1}^{p}$. (e.g., $H=N=126$, for 5 objectives and $p=5$ ).

In MOEA/D, the number of the subproblems equals the population size $N$ and the weight vectors $\boldsymbol{\lambda}^{1}, \ldots, \boldsymbol{\lambda}^{N}$ is con-
trolled by the $W$ configuration parameter, calculated as proposed in [41], which is same procedure used to generate the reference points in NSGA-III. The size of the neighborhood of each weight vector is $T=10$ [7]. The weighted sum approach was used for the MOEA/D experiments ${ }^{2}$.

All the algorithms run a total of $M a z_{g e r}=100$ generations (LS iterations are not considered as generations); 20 independent executions are conducted for each algorithm and then the performance indicators are computed.

### 4.2 Performance Metrics

Since for the addressed problem the optimal Pareto front for each instance is not known, we use a reference set which is constructed by gathering all non-dominated solutions obtained by all algorithms over all executions. The reference set (the best known Pareto front) is denoted by Ref. The performance of an algorithm is measured by the difference $\mathrm{HV}^{-}$between the hypervolume of its solutions set and the hypervolume of the reference set. So, smaller values correspond to higher quality solutions in non-dominated sets and it indicates both a better convergence as well as a good coverage of the reference set [2].

### 4.3 Numerical results

In this section, we aim to compare HMOBEDA with HMOBEDA $_{f}$, MBN-EDA, NSGA-II, S-MOGLS, NSGA-III and MOEA/D. The sets provided by these algorithms will denote the non-dominated solutions found among all the executions (the reference set). Table 2 presents the percentage of non-dominated solutions of each algorithm that composes the reference set (cardinality).

Table 2: Percentage of $|\operatorname{Ref}|$ corresponding to each algorithm.

Note that some non-dominated solutions are found by more than one algorithm. We conclude that for all instances HMOBEDA finds the greatest number of solutions in the reference of the reference set. For instances $3-250$ and $5-250$ more than half of the solutions in the reference set are originated from solutions produced by HMOBEDA.

Average run times are presented in Table 3.
We observed that for smaller search spaces, NSGA-II presents better results (an average of total runs). However, increasing the number of objectives and variables severely impacts the computational time of all approaches, mainly for NSGA-II. Also, HMOBEDA, NSGA-III and MOEA/D execution times are similar for all instances.

Table 4 shows the hypervolume difference $\left(\mathrm{HV}^{-}\right)$averaged over 20 executions of each algorithm. We use PISA framework [31] to calculate $\mathrm{HV}^{-}$. Due to the normality of the

[^0]
[^0]:    ${ }^{2}$ This approach is used in [41] implementation for MOKP, which can be downloaded from http://http://dces.essex.ac.uk/staff/zhang/webofmoead.htm.

Table 3: Average run time (min) of each algorithm.
$\mathrm{HV}^{-}$values, which has been verified through the ShapiroWilk normality test [5], the Anova test is applied to perform a statistical analysis on the results [3]. All tests have been executed with a confidence level of $95 \%(\alpha=0.05)$ and 20 replications (executions of each algorithm).

Table 4: Average hypervolume differences $\left(\mathrm{HV}^{-}\right)$.

Table 5 shows the statistical analysis of the results for the algorithms for each instance, with respect to $\mathrm{HV}^{-}$values. The null hypothesis that all the algorithms have $\mathrm{HV}^{-}$ values with no statistical difference can be rejected for all instances. A post-hoc analysis is performed to evaluate which algorithms present statistical difference. The entry related to the algorithm with the best average $\mathrm{HV}^{-}$is shown in bold. The numbers in parentheses show the results of pairwise comparisons using Tukey's posthoc test [11] with a significance level of $\alpha=0.05$. The first number shows how many algorithms are significantly worse than the algorithm listed in the corresponding line, and the second number shows how many algorithms are significantly better.

Table 5: Results of post-hoc statistical test.
Figures 2 and 3 illustrate the Tukey's post-hoc test for HMOBEDA in comparison with other approaches: (a) instances with 3 , (b) instances with 4 and (c) instances with 5 objectives. The continuous bold line represents the $\mathrm{HV}^{-}$values obtained by HMOBEDA; the continuous line identifies the $\mathrm{HV}^{-}$values obtained by algorithms with no significant difference from HMOBEDA; and the dashed line represents $\mathrm{HV}^{-}$values with significant difference from HMOBEDA.

As we can see from these graphical results, the proposed approach presents statistical difference in comparison with almost all other algorithms. For Tukey's post-hoc test, when confidence intervals do not overlap, $\mathrm{HV}^{-}$values can be compared (and thus algorithms), otherwise they have similar
performances. An example can be seen in Figures 2 (a) and (b): for instances $3-100$ the performances of $\mathrm{HMOBEDA}_{f}$, MBN-EDA, NSGA-II and S-MOGLS are not statistically different and all of them are worse than HMOBEDA (which has similar performance to NSGA-III and MOEA/D); also, for instances $4-100$ the performances of HMOBEDA, NSGAIII and MOEA/D are not statistically different; NSGA-III and HMOBEDA are better than $\mathrm{HMOBEDA}_{f}$, MBN-EDA, NSGA-II and S-MOGLS. For the remaining instances we clearly see that confidence intervals do not overlap, so we can conclude that, based on $\mathrm{HV}^{-}$, HMOBEDA has the best performance among the algorithms compared.

Therefore, we can affirm that HMOBEDA is a competitive approach for the instances considered in this work. We have observed that it is statistically superior to the compared approaches, except for instances of small size where HMOBEDA, NSGA-III and MOEA/D are not statistically different. Also, HMOBEDA is better than $\mathrm{HMOBEDA}_{f}$, which evidences that the proposed approach is capable of setting good values for the LS parameters.

## 5. CONCLUSIONS AND FUTURE WORK

In this paper we have proposed a new approach for integrating local search methods and probabilistic modeling in the context of multi-objective optimization. The backbone of our proposal is a MOEDA-based approach that uses a Bayesian Network as its probabilistic model. Additionally, it is embedded with a hill climbing procedure as local optimizer. The distinguished characteristic of HMOBEDA is that it adopts joint probabilistic model of objectives, variables and LS parameters to generate new individuals through the sample process. The Bayesian network is learned using the K-2 method and individuals selected by non-dominated sort. Current solutions are exploited by the LS procedure according to the encoded LS parameters. Thus, the algorithm can explore in a proper way other solutions in the decision space, contributing to the diversity of the non-dominated final set. As the LS parameters are part of the network, they are adapted as the algorithm evolves.

Local search is commonly applied as a method to improve the results of evolutionary optimization methods as the ones analyzed in our paper. The main question for us was to determine whether using auto-adapted LS parameters, and letting the Bayesian network represent and set these parameters, would improve the search which can be be answered in an affirmative way based on the experimental results. The algorithm was tested in six instances of the multi-objective knapsack problem. We concluded that the proposed hybrid EDA provides better performance when compared with the other evolutionary algorithms investigated. The explanation is based on the fact that since the LS parameters are in the same probabilistic model, HMOBEDA provides an automatic and informed decision at the time of setting these parameters, thus a variety of non-dominated solutions could be found attending different stages of the evolutionary process. We showed that the better performance of the proposed approach is more related with the probabilistic model than with LS: $\mathrm{HMOBEDA}_{f}$ did not provide the same tradeoff even using LS with tuned parameters.

In the future, different repair methods and LS procedures can also be tested. Finally, we intend to compare HMOBEDA with a baseline method commonly used in hyperheuristics contexts which randomly generates LS parameters.

![img-2.jpeg](img-2.jpeg)

Figure 2: Graphical results of post-hoc test for HMOBEDA versus other approaches - MOKP with 100 items
![img-2.jpeg](img-2.jpeg)

Figure 3: Graphical results of post-hoc test for HMOBEDA versus other approaches - MOKP with 250 items

## 6. ACKNOWLEDGEMENTS

R. Santana acknowledges support by: IT-609-13 program (Basque Government), TIN2013-41272P (Spanish Ministry of Science and Innovation) and CNPq Program Science Without Borders Nos.: 400125/2014-5 (Brazil Government).
M.Martins acknowledges CAPES/Brazil.
