# Exploring the probabilistic graphic model of a hybrid multi-objective Bayesian estimation of distribution algorithm 

Marcella S.R. Martins ${ }^{\text {a, }}$, Myriam Delgado ${ }^{\text {a }}$, Ricardo Lüders ${ }^{\text {a }}$, Roberto Santana ${ }^{\text {b }}$, Richard A. Gonçalves ${ }^{\text {c }}$, Carolina P. de Almeida ${ }^{\text {c }}$<br>${ }^{a}$ Federal University of Technology - Paraná, Curitiba PR, Brazil<br>${ }^{\text {b }}$ University of the Basque Country, San Sebastián, Spain<br>${ }^{\text {c State University of the Midwest of Paraná, Guarapuava PR, Brazil }}$

## H I G H L I G H T S

- An approach for multi and manyobjective combinatorial optimization is explored.
- It is based on a joint probabilistic model with local optimizers as an online tuning.
- Versions with different sampling are analyzed from a probabilistic point of view.
- The best version outperforms other approaches when the number of objectives increases.
- Information can be extracted from the models to learn and explore dependencies.


## ARTICLE INFO

## Article history:

Received 20 February 2018
Received in revised form 11 July 2018
Accepted 27 August 2018
Available online 1 September 2018

## Keywords:

Multi-objective optimization
Estimation of distribution algorithms
Automatic algorithm configuration

GRAPHICAL ABSTRACT
![img-0.jpeg](img-0.jpeg)

## A B S T R A C T

The Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm (HMOBEDA) has shown to be very competitive for Many Objective Optimization Problems (MaOPs). The Probabilistic Graphic Model (PGM) of HMOBEDA expands the possibilities for exploration as it provides the joint probability of decision variables, objectives, and configuration parameters of an embedded local search. This work investigates different sampling mechanisms of HMOBEDA, applying the considered approaches to two different combinatorial MaOPs. Moreover, the paper provides a broad set of statistical analyses on its PGM model. These analyses have been carried out to evaluate how the interactions among variables, objectives and local search parameters are captured by the model and how information collected from different runs can be aggregated and explored in a Probabilistic Pareto Front. In experiments, two variants of HMOBEDA are compared with the original version, each one with a different set of evidences fixed during the sampling process. Results for instances of multi-objective knapsack problem with 2-5 and 8 objectives show that the best variant outperforms the original HMOBEDA in terms of convergence and diversity in the solution set. This best variant is then compared with five state-of-the-art evolutionary algorithms using the knapsack problem instances as well as a set of MNK-landscape instances with 2, 3, 5 and 8 objectives. HMOBEDA outperforms all of them.

[^0]
[^0]:    * Corresponding author.

    E-mail address: marcella@utfpr.edu.br (M.S.R. Martins).

thus been established as an important field of research [2]. In the past few years, problems with more than three objectives are becoming usual. They are referred as Many Objective Optimization Problems (MaOPs) [3].

MOPs and especially MaOPs contain several, usually conflicting, objectives. This means, optimizing one objective does not necessarily optimize the others. Due to the objectives trade-off, a set called Pareto-optimal is generated at the decision variable space. Different approaches have been proposed to approximate the Pareto-optimal front (i.e. Pareto-optimal corresponding objectives) in the objective space in various scenarios [2].

Multi-objective evolutionary algorithms (MOEAs) are classical examples of these approaches. They have achieved good results on MOPs as they search multiple solutions in parallel with some advantages when compared with math programming-based approaches. Several MOEAs incorporating local search (LS) have been investigated on combinatorial optimization, and these hybrid approaches can often achieve good performance for many problems [4], [5], [6]. However, as discussed in [7] and [8], they still present challenges, such as the choice of suitable LS parameters e.g., the type, frequency and intensity of LS applied to a particular candidate solution.

Another strategy widely used in evolutionary optimization is the probabilistic modeling, which is the basis of Estimation of Distribution Algorithms (EDAs) [9]. EDAs are a class of Evolutionary Algorithms (EAs) that explores the search space by building a probabilistic model from a set with the current best candidate solutions [10]. Since new solutions are sampled from the probabilistic model, evolution is guided toward more promising areas of the search space.

Normally, Multi-objective Estimation of Distribution Algorithm (MOEDAs) [11] integrate both model building and sampling techniques into evolutionary multi-objective optimizers using special selection schemes [12]. Probabilistic Graphical Models (PGMs) combine graph and probability theory. They have been adopted to improve EDAs and MOEDAs performance [13]. Most of MOEDAs developed to deal with combinatorial MOPs adopt Bayesian Networks (BNs) as PGM. This way, these PGM-based MOEAs are able to properly modeling variables' dependencies, besides solving the optimization problem.

Furthermore, recently the role of the probabilistic model has been extended to model dependencies between variables and objectives [11]. In addition, MOEDAs for combinatorial optimization can be notably enhanced by adding a local optimizer that can refine solutions found by sampling the PGM [14], [15].

This paper investigates the approach firstly presented in [7], called Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm (HMOBEDA), which is based on a joint probabilistic modeling of decision variables, objectives, and parameters of the local optimizers. Some recent MOEDA-based approaches model variables and objectives in the same PGM in order to explore their relationship, which means investigating how objectives influence variables and vice versa [11]. However, HMOBEDA also includes a Local Search (LS) parameters in its BN-based PGM. It means that appropriate LS parameters for different configurations of decision variables and objective values are sampled from PGM, which acts like an online parameter tuning approach. This paper aims to extend the work presented in [7] and further expanded in [8] by investigating different sampling mechanisms and also the results presented in [16] by expanding the statistical analysis and applying the considered approaches on two combinatorial MaOPs.

The main objective here is to explore, from a probabilistic point of view, the approximated Pareto Front (PF) using the final PGM structure. Two variants of HMOBEDA which use different ways to fix evidences during the sampling and were not explored in [7], [8] are considered in this paper. However, differently from [16], we
provide a more profound investigation of the resulted probabilistic model. We evaluate how the interactions among variables, objectives and local search parameters are captured by the model for the considered MaOPs instances, by exploring the PGM structures learned during the evolutionary process. Besides Hypervolume [17], [18] and Inverted Generational Distance (IGD) [19] indicators adopted in [16], this paper also considers a capacity metric called Error Ratio (ER) [19] on the statistical analysis of the results.

In [16], the embedded PGM is evaluated on the Multi-objective Knapsack Problem (MOKP) - the multi-objective version of the well known knapsack problem, which has been recently explored in other works in the literature [20], [21]. MOEDAs that use different types of probabilistic models have already been applied to MOKP [14], [15], particularly those based on BN [12]. However, these works do not consider the objectives and parameters structured all together in the same BN, as proposed in HMOBEDA. Therefore, HMOBEDA was chosen to be investigated in this work using the same instances of MOKP addressed in [16]. In addition, we extend the analysis to the multi-objective NK-landscape (MNKlandscape) problem [22], [23]. This problem represents another combinatorial MOP that has been recently explored by [23], [24], [25], [26]. The mono-objective version has also been explored by using EDAs [27], [29]. However, these works do not consider objectives and LS parameters structured all together in the same BN.

In the MOKP case, many real-world applications are reported dealing with capital budgeting [30], selection of transportation investment alternatives [31], relocation issues arising in conservation biology [32], planning remediation of contaminated lightstation sites [33] and action plan in the social and medico-social sector [34]. The NK model has found application in several fields, ranging from evolutionary biology studies [35], [36] to complex systems, such as the representation of complexity in economics and organizational sciences [37]. Therefore, these problems have been chosen due to their combinatorial and multi-objective features and because they might model several other real-world problems.

This paper is organized as follows. The addressed MOPs are presented in Section 2. Section 3 provides a brief introduction to Bayesian Network and EDA PGM. Section 4 details the two variants of HMOBEDA. Results from numerical experiments are shown and discussed in Section 5 with conclusions and future directions presented in Section 6.

## 2. The multi and many-objective problems addressed in this paper

This section presents the problems addressed in this paper. First we investigate the MOKP, according to the multi-objective formulation proposed by [17], [20] and [21]. Then we explore the MNK-landscape problem proposed by [22].

### 2.1. The multi-objective knapsack problem

The binary version $0 / 1$ knapsack is a widely studied problem due to its practical importance. In the last years a general formulation has been well studied and a number of algorithms have been proposed. Evolutionary approaches for solving the multiobjective version (MOKP) are of great interest [38] with many works presented in the last years [17], [20], [21], [39], [40], [41], [42] and [43], many algorithms for solving the MOKP variant have been proposed using different techniques for real [30], [31], [32], [33], [34] and non-real world applications [38].

MOKP can be formulated as follows:
$\max _{\mathbf{x}} \mathbf{z}(\mathbf{x})=\left(z_{1}(\mathbf{x}), \ldots, z_{R}(\mathbf{x})\right)$
subject to $\sum_{q=1}^{Q} b_{r q} x_{q} \leq c_{r}, r=1, \ldots, R$
with $z_{i}(\mathbf{x})=\sum_{q=1}^{Q} a_{r q} x_{q}, \mathbf{x} \in\{0,1\}^{Q}$

where, $a_{r q}$ is the profit of item $q$, according to knapsack $r, b_{r q}$ denotes the weight of item $q$ according to knapsack $r$, and $c_{r}$ is the constraint capacity of knapsack $r$, given a total of $R$ objective functions (knapsacks) and $Q$ items. Decision variables are represented by $\mathbf{x}$, a $Q$-dimension binary vector, with $x_{q}=1$ indicating that item $q$ has been selected to be in $r$ th knapsack, and $x_{q}=0$, otherwise.

### 2.2. The multi-objective NK-landscape problem

The single NK fitness landscapes is a family of combinatorial problems proposed in [44] aiming to explore the way in which the neighborhood structure and the strength of the interactions between neighboring variables (subfunctions) are linked to the search space ruggedness.

Let $\mathbf{X}=\left(X_{1}, \ldots, X_{N}\right)$ denote a vector of discrete variables and $\mathbf{x}=\left(x_{1}, \ldots, x_{N}\right)$ an assignment to the variables.

An NK fitness landscape is defined by the following components [28]:

- Number of variables, $N$.
- Number of neighbors per variable, $K$.
- A set of neighbors, $\Pi\left(X_{q}\right) \in \mathbf{X}$, for $X_{q}, q \in\{1, \ldots, N\}$ where $\Pi\left(X_{q}\right)$ contains $K$ neighbors.
- A subfunction $f_{q}$ defining a real value for each combination of values of $X_{q}$ and $\Pi\left(X_{q}\right), q \in\{1, \ldots, N\}$.

Both the subfunction $f_{q}$ for each variable $X_{q}$ and the neighborhood structure $\Pi\left(X_{q}\right)$ are randomly set [28].

The mono-objective function $z_{N K}$ to be maximized is defined as:
$z_{N K}(\mathbf{X})=\sum_{q=1}^{N} f_{q}\left(x_{q}, \Pi\left(x_{q}\right)\right)$.
For a set of given parameters, the problem consists in finding the global maximum of the function $z_{N K}[45]$.

The MNK-landscape problem [22], [23] is a multi-objective version of the NK fitness landscape model with $R$ objectives, $\mathbf{z}(\mathbf{x})=$ $\left(z_{1}(\mathbf{x}), z_{2}(\mathbf{x}), \ldots, z_{R}(\mathbf{x})\right): \mathcal{B}^{N} \rightarrow \mathcal{R}^{R}$. Each objective function is determined by a different instance of an NK-landscape, over the same binary string $\mathbf{x}$, where $N$ is the number of variables, ${ }^{1} R$ is the number of objectives, $z_{r}(\mathbf{x})$ is the $r$-ith objective function, and $\mathcal{B}=\{0,1\} . \mathbf{K}=\left\{K_{1}, \ldots, K_{R}\right\}$ is a set of integers where $K_{r}$ is the neighborhood size in the $r$ th landscape.

MNK-landscape problem can be formulated as follows [23]:
$\max _{\mathbf{x}} \mathbf{z}(\mathbf{x})=\left(z_{1}(\mathbf{x}), \ldots, z_{R}(\mathbf{x})\right)$
subject to $\mathbf{x} \in\{0,1\}^{N}$,
with
$z_{r}(\mathbf{X})=\frac{1}{R} \sum_{q=1}^{N} f_{r, q}\left(x_{q}, \Pi_{r, q}\left(x_{q}\right)\right)$,
$r \in\{1, \ldots, R\}$,
$q \in\{1, \ldots, N\}$,
where the fitness contribution $f_{r, q}$ of variable $x_{q}$ is a real number in $\{0,1\}$ drawn from a uniform distribution.

### 2.3. Related approaches

There are many related approaches to solve the problems addressed in this paper. Several probabilistic models can be used to represent the solution set for both $0 / 1$ knapsack and NK-landscape problems. The main contributions of HMOBEDA are the inclusion of local search and the relationship between objectives, variables and local search parameters in the probabilistic model.

[^0]Considering the MOKP and starting with the approach presented in [46], we point out that in this work authors present a modified evaluation phase of the single BOA algorithm using the strength criterion concept adopted by the SPEA algorithm, and their experiments are for 2 objectives. The work proposed by [12] has been designed using a probabilistic model based on binary decision trees and a special selection scheme that uses $\epsilon$-archives, it was applied to 2, 3 and 4 objectives. Differently, HMOBEDA uses the non-dominated sorting scheme, tournament selection and crowding distance (CD), procedures also used in NSGA-II. Another difference, is that HMOBEDA adopts a local search, models the best solutions using a BN, considers objectives and local search parameters in addition to decision variables as nodes of the network, and can be applied to multi and many objective optimization.

In [14], for MOKP, the following techniques are used: random repair method; random neighborhood structure in local search; stochastic clustering method; a mixture-based UMDA, for 2, 3 and 4 objectives. The differences of this approach and HMOBEDA are the probabilistic model and the local search: in their work the local search is based on a weighted sum method, with weights calculated according to maximization and minimization functions of each objective. In our work the local search weights are uniformly distributed.

An EDA is proposed in [47] to find the solution of the Bounded Knapsack Problem using the same repair method we have used in our work. However their addressed problem considers a single objective, a vector as the probabilistic model (i.e., they assume no relationship among variables) and a mutation probability exchanging a bit from 0 to 1 or 1 to 0 is applied to the sampled solutions in order to overcome a local optimum.

The work presented in [6] proposed an EDA combining two local search strategies addressing the knapsack problem for a single objective. The main difference from this previous research is that HMOBEDA addresses the embedded local search parameters in an EDA framework for MOPs. In [6] the authors present a relevant EDA approach with local search that might be extended to the MOKP to be consider in our future research.

Regarding the MNK-landscape problem, the main difference is that none of the related works considers EDAs for the multiobjective NK-landscape problem and none of them includes LS parameters in PGM.

In [27] and [28] the authors analyze the performance of hBOA, UMDA, and a genetic algorithm (GA) on the mono-objective NKlandscape problem. In [29] the authors also study the behavior of EDAs using UMDA, BMDA and EBNA with different parameter settings. Although they use probabilistic models based on BN, they consider only mono-objective NK-landscape instances.

The work presented in [23] compares NSGA-II and SPEA2 on the generated landscapes using hypervolume indicator, similar to our work, and analyzes the influence of MNK-landscape parameters on several features of the fitness landscape. However, the main difference between that work and ours is that we aim to study a PGMbased MOEDA (HMOBEDA), and compare its variants analyzing the probabilistic model.

The works proposed by [26] and [48] study which (and how) problem features impact the search performance for a global EMO strategy (GSEMO) and a neighborhood-based local search heuristic (PLS) in the $\rho$ MNK-landscapes, a variant of MNK-landscape model. The differences of these works and ours are that we explore an online tuning of LS parameters, where these parameters are selfadapted as the optimization process evolves.

Table 1 summarizes the main characteristics of EDA-based approaches developed to solve knapsack and NK-landscape problems compared with HMOBEDA.

## 3. Bayesian networks: a brief introduction

One of the most general probabilistic models for discrete variables used in EDAs and MOEDAs is the Bayesian Network [49].


[^0]:    1 The number of variables $N$ is noted $Q$ in Sections 4 and 5.

Table 1
Summarizing EDA approaches for the knapsack and NK-landscape problems.
Bayesian Networks are directed acyclic graphs (DAG) whose nodes represent variables, and whose missing edges encode conditional independencies between variables. Each node is associated with a probability function that takes as input a particular set of values for the node's parent variables and gives the probability of the variable represented by the node [50,51].

Let $\mathbf{Y}=\left(Y_{1}, \ldots, Y_{M}\right)$ be a vector of $M$ random variables, and let $y_{m}$ be a value of $Y_{m}$, the $m$ th component of $\mathbf{Y}$. The representation of a Bayesian model is given by two components [13]: a structure and a set of local parameters. The set of local parameters $\Theta$ contains, for each variable, the conditional probability distribution of its values given different value settings for its parents, according to structure B.

The structure $B$ for $\mathbf{Y}$ is a DAG that describes a set of conditional dependencies of all variables in $\mathbf{Y} . \mathbf{P a}_{m}^{B}$ represents the set of parents (variables from which an arrow is coming out in $B$ ) of the variable $Y_{m}$ in the PGM whose structure is given by $B$ [52]. This structure assumes that $Y_{m}$ is independent from its non-descendants given $\mathbf{P a}_{m}^{B}, m=2, \ldots, M$, where $Y_{1}$ is the root node.

Therefore, for discrete random variables, a Bayesian Network encodes a factorization for the probability mass function (pmf) as follows:
$p(\mathbf{y})=p\left(y_{1}, y_{2}, \ldots, y_{M}\right)=\prod_{m=1}^{M} p\left(y_{m} \mid \mathbf{p a}_{m}^{B}\right)$
In discrete domains, we can assume that $Y_{m}$ has $s_{m}$ possible values (states), $y_{m}^{1}, \ldots, y_{m}^{s_{m}}$, therefore the particular conditional probability, $p\left(y_{m}^{k} \mid \mathbf{p a}_{m}^{j, B}\right)$, can be defined as:
$p\left(y_{m}^{k} \mid \mathbf{p a}_{m}^{j, B}\right)=\theta_{y_{m}^{k} \mid \mathbf{p a}_{m}^{j, B}}=\theta_{n g_{k}}$
where $\mathbf{p a}_{m}^{j, B} \in\left\{\mathbf{p a}_{m}^{j, B}, \ldots, \mathbf{p a}_{m}^{s_{m}, B}\right\}$ denotes a particular combination of values for $\mathbf{P a}_{m}^{B}, t_{m}$ is the total number of different possible instantiations of the parent variables of $Y_{m}$ given by $t_{m}=\prod_{Y_{v} \in \mathbf{P a}_{m}^{B}} s_{v}$, $s_{v}$ is the total of possible values (states) that $Y_{v}$ can assume. The parameter $\theta_{n g_{k}}$ represents the conditional probability that variable $Y_{m}$ takes its $k$-th value $\left(y_{m}^{k}\right)$, knowing that its parent variables have taken their $j$ th combination of values $\left(\mathbf{p a}_{m}^{j, B}\right)$. This way, the parameter set is given by $\Theta=\left\{\boldsymbol{\theta}_{1}, \ldots, \boldsymbol{\theta}_{m}, \ldots \boldsymbol{\theta}_{M}\right\}$, where $\boldsymbol{\theta}_{m}=$ $\left(\theta_{m 11}, \ldots, \theta_{m j k}, \ldots, \theta_{m, t_{m}, s_{m}}\right)$ and $M$ the total number of nodes in the BN.

BNs are often used for modeling multinomial data with discrete variables [53] and generate new solutions using the particular conditional probability described in Eq. (5)(probabilistic logic sampling [54]).

Generally, parameters in the whole set $\Theta$ and the BN structure $B$ are unknown. Two approaches to estimate the parameters are usually applied: Maximum Likelihood Estimate (MLE) and Bayesian Estimate [52], this last one is used in this work to estimate the parameters.

There are three main approaches to learn BN structures: score-based learning, constraint-based learning, and hybrid methods [55].
![img-1.jpeg](img-1.jpeg)

Fig. 1. An MBN classifier with 3 class variables and 4 feature variables.

The majority of the developed structure learning algorithms fall into the category of score-based approaches, which look for the network structure that maximizes the value of a scoring metric. Usual examples of such approaches are the simple greedy search algorithm, local hill-climbing, simulated annealing, tabu search and evolutionary computation [13], most of them use K2 as the scoring metric [50].

Constraint-based learning methods typically use statistical tests to identify conditional independence relations from data and build a BN structure that best fits those relations [53], such as Incremental Association Markov Blanket (IAMB) [56] and Semi-Interleaved Hiton-PC (SI-HITON-PC) [57]. Hybrid methods aim to integrate the two approaches, like Max-Min Hill Climbing (MMHC) [58].

### 3.1. Naive BN-based models

One of the most important fields of BN application is classification, when the BN nodes represent either classes or instance features. However, many application domains involve instances that are expected to be assigned to the most likely combination of classes [59]. A multidimensional BN (MBN) classifier is a Bayesian Network, with a restricted topology designed to address these applications, which includes one or more class variables and one or more feature variables in its PGM.

An MBN classifier has a set of random variables $\mathbf{Y}$ partitioned into a set of feature variables $\mathbf{Y}_{\mathbf{F}}=\left\{F_{1}, \ldots, F_{m}\right\}, m \geq 1$, and a set $\mathbf{Y}_{\mathbf{C}}=\left\{C_{1}, \ldots, C_{n}\right\}, n \geq 1$, with the class variables. Subgraph $B_{C} \subset \mathbf{Y}_{\mathbf{C}}$ is called class subgraph; and $B_{F} \subset \mathbf{Y}_{\mathbf{F}}$ is called feature subgraph. Subgraph $B_{C F}$, which includes arcs from class to feature variables, is called feature selection subgraph, since it represents the selection of features that are deemed relevant for classification in view of class variables [60]. Fig. 1 illustrates an example of an MBN with $n=3$ and $m=4$.

![img-2.jpeg](img-2.jpeg)

Fig. 2. A naive MBN classifier with 3 class variables and 4 feature variables.

According to [11], an MBN can infer the classes of given feature variables, the most probable feature values for a given combination of classes, and the most probable values for a subset of features or classes given the value of the others.

Different types of MBN classifiers can be distinguished based on their graphical structures. An example is the naive multidimensional classifier in which both the class subgraph and the feature subgraph are empty [59] (i.e. there are edges only in feature selection subgraph, as presented in Fig. 2). This structure is the base of HMOBEDA, therefore the structure learning process consists in finding, for root notes defined as multiple objectives, a feature selection subgraph (encompassing decision variables and local search parameters in our case) that better fits the data.

Our interest in this work is to apply MBN concepts to MOPs, aiming to answer ((i) mainly (ii) possibly) the following questions: (i) what is the most probable solution resulting in a specific valuesetting for the objectives? (ii) what are the estimated objectives values of a given solution?

MBN classifiers use different estimation methods or search algorithms to find out the optimal way to represent data [59], and most of them are score-based [61]. The presence of several classes adds complexity and increases the number of network parameters [62]. Therefore, some authors have suggested methods to overcome these shortcomings such as: K2 algorithms [50,61,63], the Greedy Search [61,64], the Greedy Hill Climber (BN-HC) and the Repeated Hill Climber (BN-RHC) [61,65].

The choice of the K2 algorithm is based on previous studies. In [61], K2 was compared with BN-HC and BN-RHC and again, it achieved a better trade-off between accuracy and computational cost.

The K2 algorithm, introduced by [50], is a score-based greedy local search technique which uses the K2 metric to select the next arc between $B_{C}$ and $B_{F}$. It starts by assuming that a node, in an ordered list, does not have any parent, then it processes each node in turn, gradually adding edges from previously processed nodes to the current one. In each step it adds the edge that increases the K2 scoring metric the most. When no edge increases the metric anymore, it turns attention to the next node.

In this work we apply the K2 structure learning algorithm for all variants of HMOBEDA, which will be discussed in the next section.

## 4. Comparing HMOBEDA versions

HMOBEDA is a hybrid EDA approach introduced in [7]. The term hybrid concerns a local search (LS) mechanism included into its PGM-based framework to improve the performance. This way, LS can be combined with sorting and selection techniques usually adopted in MOEAs and also be configured with suitable parameters during the search. The general scheme of the HMOBEDA is presented in Fig. 3.

As can be noticed, HMOBEDA uses a probabilistic model (based on BN) of objectives, variables and local search parameters to sample new individuals. Every solution is thus represented by a joint
vector with $Q+R+L$ elements, $\mathbf{y}=(\mathbf{x}, \mathbf{z}, \mathbf{p})=\left(X_{1}, \ldots, X_{Q}, Z_{1}, \ldots\right.$, $\left.Z_{R}, P_{1}, \ldots, P_{L}\right)$, denoting the decision variables $\left(X_{1}, \ldots, X_{Q}\right)$, objectives $\left(Z_{1}, \ldots, Z_{R}\right)$ and LS parameters $\left(P_{1}, \ldots, P_{L}\right)$.

At the first iteration, solutions are randomly generated in the Initialization process and the corresponding objectives are calculated through the objective functions of the addressed problem. A Local Search based on Hill Climbing procedure (HCLS) [66]) generates a neighbor for each solution, then HMOBEDA calculates its fitness and updates the original solution in case the neighbor has a better fitness.

In order to select a total of $N_{P G M}$ individuals from the current population, the Non-dominated Sorting (ND) [67] technique is applied. The Selection procedure randomly selects two solutions and the one positioned in the best front is chosen. If they lie on the same front, it chooses that solution with the greatest Crowding Distance (CD) [68].

Aiming to learn the probabilistic model, the BN structure and parameters are estimated in the PGM Learning block. Different algorithms can be considered for the PGM Learning block: in this work we use the K2 algorithm with K2 metric running over a set of $N_{P G M}$ best individuals each one composed of $Q$ decision variables, $R$ objectives and $L$ local search parameters, (i.e. $\mathbf{Y}=\left(Y_{1}, \ldots, Y_{M}\right)=\left(Z_{1}, \ldots, Z_{R}, X_{1}, \ldots, X_{Q}, P_{1}, \ldots, P_{L}\right)$ ). In [69] some experiments were conducted and we concluded that K2-algorithm was a good option for the structure prediction of HMOBEDA, as well CD for tie-breaker criteria. This way the BN structure encodes a factorization of the joint probability distributions or the probability mass function (pmf) given by:
$p(\mathbf{y})=\prod_{t=1}^{R} p\left(z_{t} \mid \mathbf{p a}_{t}^{R}\right) \cdot \prod_{\mathrm{q}=1}^{\mathrm{Q}} p\left(\mathrm{x}_{\mathrm{q}} \mid \mathbf{p a}_{\mathrm{q}}^{R}\right) \cdot \prod_{l=1}^{L} p\left(p_{l} \mid \mathbf{p a}_{l}^{R}\right)$
where $\mathbf{p a}_{t}^{R}, \mathbf{p a}_{\mathrm{q}}^{R}$ and $\mathbf{p a}_{l}^{R}$ represent combinations of values for the parents of objective, decision variable and LS parameter nodes respectively, with $\mathbf{P a}_{\mathrm{q}}^{R} \subseteq\left\{Z_{1}, \ldots, Z_{R}\right\}, \mathbf{P a}_{\mathrm{l}}^{R} \subseteq\left\{Z_{1}, \ldots, Z_{R}\right\}, \mathbf{P a}_{\mathrm{l}}^{R}=\emptyset$, which means $p\left(z_{t} \mid \mathbf{p a}_{t}^{R}\right)=p\left(z_{t}\right)$ for $r=1, \ldots, R$.

In the Sampling block, the obtained PGM is used to sample the set of new individuals. As discussed in [16], the main advantage of using the HMOBEDA framework, is that not only decision variables, but also LS parameters can be obtained through the Sampling block. This naive Bayesian model (see Fig. 3) is adopted to facilitate the sampling process: fixing objective values as target evidences enables the estimation of their associated decision variables and LS parameters. Therefore, after sampling, decision variables $\left(X_{1}, \ldots, X_{Q}\right)$ and LS parameters $\left(P_{1}, \ldots, P_{L}\right)$ more related to the objectives fixed as evidences can be drawn for each new individual, and this paper aims at exploring different ways of fixing evidences.

Finally, objectives $\left(Z_{1}, \ldots, Z_{R}\right)$ are calculated based on the fitness function (in the case of surrogate assisted approaches, PGM can also be used to sample the objective values or the least squares method can provide objective value approximations). The union of the sampled and the current populations in the Survival block is used to create the new population for the next generation $g+1$, and the main loop continues until the stop condition is achieved.

In this paper, we explore two variants of HMOBEDA named $\mathrm{HMOBEDA}_{\text {EXT }}$ and $\mathrm{HMOBEDA}_{\text {CPT }}$ which were proposed in [16] and represent different possibilities to guide the search.

As shown in Fig. 4(b), HMOBEDA $_{\text {CPT }}$ uses priori probabilities of $Z_{1}, \ldots, Z_{R}$ described in the Conditional Probability Table (CPT) to draw and further fix evidences. Fig. 4(c) shows that HMOBEDA $_{\text {EXT }}$, besides considering $Z^{*}$ like the HMOBEDA version, it also includes the extreme points of the approximated Pareto Front (PF) as candidates for the evidences in the root nodes. In HMOBEDA $_{\text {EXT }}$, these values are fixed at each generation considering the same probabilities for all candidates: $Z^{*}$ and the total number of objectives (each in every extreme of the current approximation Pareto Front).

![img-3.jpeg](img-3.jpeg)

Fig. 3. The HMOBEDA Framework.
![img-4.jpeg](img-4.jpeg)

Fig. 4. Evidences (gray circles) from the approximated Pareto Front with 2 objectives for (a) HMOBEDA, (b) HMOBEDA ${ }_{\text {OT }}$ and (c) HMOBEDA ${ }_{\text {OT }}$.

## 5. Experiments and results

First we compare the original version of HMOBEDA with the two considered variants over MOKP instances through the Hypervolume $\left(\mathrm{HV}^{-}\right)[17,18]$ and Inverted Generational Distance (IGD) [19], which are usually adopted for measuring the quality of the optimal solution set for multi and many-objective optimization [70].

After that, we compare the best version of HMOBEDA with cutting edge approaches, over MOKP and MNK-landscape instances. In this case besides $\mathrm{HV}^{-}$and IGD we also consider a capacity metric called Error Ratio (ER) [19].

Hypervolume considers the difference $\left(\mathrm{HV}^{-}\right)$between the hypervolume of the corresponding objectives from both the solution set of an algorithm and the reference set. The IGD metric is the average distance from point in the PF associated with the reference set to the nearest point in the approximated PF. So, smaller values of $\mathrm{HV}^{-}$and IGD correspond to higher quality solutions in non-dominated sets indicating both better convergence and good coverage of the reference set. The Error Ratio considers the ratio of solutions from the approximated set that are not in the reference set, so smaller values also indicate better performances. We use the PISA framework [71] to compute $\mathrm{HV}^{-}$and Matlab to compute the remaining metrics.

The optimal Pareto Front (PF) for each instance of the addressed problem is not known. Therefore, we use a reference set which is constructed by gathering all non-dominated solutions from all approaches addressed in [7] in addition to those obtained by the HMOBEDA versions over all executions.

In the conducted experiments concerning MOKP $a_{n}^{\prime}$ and $b_{n}^{\prime}$ are specified as integers in the interval $[10,100]$. The capacity $c_{r}$ is defined as $50 \%$ of the sum of all weights related to each knapsack $r$ as in [17]. The set of instances (characterized as $R-Q$ ) is the union of those considered in [17,20,21]. We use thus instances with 100 and 250 items, 2 to 5 and 8 objectives. If an infeasible solution is generated, we apply the same greedy repair method used in [7,17]. This method repairs a solution by removing items in an ascending
order of the relation profit/weight until the constraints are satisfied.

We also considered MNK-landscape instances with $K \in$ $\{2,4,6,8,10\}$, objective space dimension $R \in\{2,3,5,8\}$ and size $N=Q \in\{20,50,100\}, 60$ instances (one for each combination of $R, K$ and $Q$ ).

As in previous works [7,8,16,69], we estimate the parameters through Bayesian Estimate, using the Dirichlet prior, and we adopt K2 metric as score-based technique, although any other method could be used as well. In a preliminary study on the HMOBEDA framework, constraint-based learning methods such as IAMB [56], SI-HITON-PC [57] and hybrid methods like MMHC [58] were also investigated. However, the experiments have shown that K2 metric as score-based technique is a good compromise between accuracy and computational cost.

The K2 algorithm is used here by setting parent nodes as objectives in the network. Therefore, fixing objective values as target evidences enables a straightforward estimation of their associated decision variables and LS parameters.

The parameters for all the HMOBEDA versions considered in this section are: population size $(N=100)$, number of selected individuals for PGM building $N_{\text {PGM }}=N / 2$, Number of sampled individuals $N_{\text {imp }}=10 * N$. The LS online configuration adopted by HMOBEDA versions during the evolution assumes the following elements in the vector $\mathbf{p}$ : the number of LS iterations $N_{\text {iter }} \in$ $\{5,6 \ldots, 20\}$; the type of neighbor fitness calculation $T_{\text {fribh }} \in\{1,2\}$ : with (1) representing Linear Combination of objectives and (2) Alternation of objectives (i.e., one by one for each LS iteration); the neighborhood type $T_{\text {hibh }} \in\{1,2\}$ : with (1) defining double bit-flip operator and (2) single bit-flip from 0 to 1 . These parameters have been defined experimentally in previous work [7,8,16,69].

Due to heterogeneous computer hardware and to be fair enough, we define a stop condition based on maximum number of fitness evaluations (Max ${ }_{\text {evol }}$ ), which includes repair procedures and LSiterations. Then, all algorithms stop when the total number of fitness computations achieves 200,000 evaluations. A total of 30

independent executions are conducted for each algorithm to get average performance metrics.

We use the Shapiro-Wilk normality test [72] to verify whether performance metric results are normally distributed. In case of non-normal distribution, Kruskal-Wallis [73] and Dunn-Sidak's post-hoc tests are applied for statistical analysis considering all approaches being compared. For normal distributions the analyses of variance test (ANOVA) can be applied [73]. All tests have been executed with a confidence level of $95 \%(\alpha=5 \%)$.

### 5.1. Comparing HMOBEDA alternative versions

In this section, we compare the original HMOBEDA with two modified versions: HMOBEDA ${ }_{\text {CPT }}$ and HMOBEDA ${ }_{\text {EXT }}$. As discussed in Section 4, the differences among them are mainly in the sampling step.

Based on the assumptions of each variant, we aim to investigate how the evidences may influence the distribution of nondominated solutions along the approximated PF.

In addition to HMOBEDA performance in terms of $\mathrm{HV}^{-}$and IGD indicators, this section aims to evaluate the quality of the final approximation of the PF through the analysis of the final achieved PGM. This way, we want to explore one of the main advantages of using EDA: the possibility of scrutinizing its probabilistic model which encompasses relationship among variables encoded in the nodes.

Table 2 shows the statistical analysis of pairwise comparisons between HMOBEDA, HMOBEDA ${ }_{\text {EXT }}$ and HMOBEDA ${ }_{\text {CPT }}$ for each instance with respect to $\mathrm{HV}^{-}$and IGD values, respectively. The first number shows how many algorithms are better than the algorithm listed in the corresponding line, and the second number shows how many algorithms are worse. When entries present no statistically significant difference the background is emphasized in light blue. The entry related to the algorithm with the lowest (best) average metric is highlighted in bold.

Although Table 2 shows that there is no statistically significant differences between HMOBEDA, HMOBEDA ${ }_{\text {CPT }}$ and HMOBEDA ${ }_{\text {EXT }}$ regarding $\mathrm{HV}^{-}$indicator for all instances, there are statistically significant differences regarding the IGD metric for 5-100, 5-250, 8-100 and 8-250 instances. HMOBEDA and HMOBEDA ${ }_{\text {EXT }}$ present better results than HMOBEDA ${ }_{\text {CPT }}$ for 2-250, 3-100, 3-250, 5-100 and 5-250 with some advantage for HMOBEDA ${ }_{\text {EXT }}$. Besides, HMOBEDA ${ }_{\text {EXT }}$ is the best approach for 8-100 and 8-250 instances.

The average run time for each algorithm is presented in Table 3, with the respective post-hoc test showed in Table 4. We can observe that the computational efforts for all algorithms are similar, as expected, keeping the run time at practical levels. However, increasing the number of objectives and variables severely impacts the average computational time of all approaches. The run times range from approximately 3 min (instance 2-100) to 66 min (instance 8-250) for the three HMOBEDA versions, with no statistically significant differences between them for the same instance.

In order to analyze the final approximated PF achieved by each HMOBEDA version taking into account the information available in the final PGM, we calculate, for each possible solution in the approximated PF, the pmf $P(\mathbf{y})$, defined by Eq. (6), from the final set (dominated and non-dominated solutions) achieved at the end of each execution. After that, the mean of pmf values along all executions is obtained for further calculating the marginal distribution $P\left(Z_{1}=z_{1}, \ldots, Z_{R}=z_{R}\right)$. The probabilistic view of the Pareto front is then defined by gathering all non-dominated solutions obtained over all 30 executions. Each non-dominated solution is represented by a circle, which is proportional to the corresponding marginal probability $P\left(Z_{1}=z_{1}, \ldots, Z_{R}=z_{R}\right)$.
![img-5.jpeg](img-5.jpeg)

Fig. 5. A probabilistic view of the approximated PF for 2 objectives $\left(z_{1}, z_{2}\right)$ and 100 items for HMOBEDA, HMOBEDA ${ }_{\text {EXT }}$ and HMOBEDA ${ }_{\text {CPT }}$.

Fig. 5 presents the analysis of the approximated PF of all HMOBEDA versions for the instance 2-100 considering the probabilistic information of the PGM. Although PFs seem similar in terms of convergence, we can observe that HMOBEDA and HMOBEDA ${ }_{\text {CPT }}$ provide solutions concentrated on a particular region of the PF (around the ideal point), region named Pareto Front knee. However, for HMOBEDA ${ }_{\text {EXT }}$ solutions are better distributed, as points located near the extreme point associated with objective $Z_{1}$ present higher probabilities than those obtained by HMOBEDA and $\mathrm{HMOBEDA}_{\text {CPT }}$.

Since it is difficult to visualize the PF for more than two objectives, Figs. 6(a) and 6(b) illustrate a simplified way to view the approximation: the ordered Euclidean distance between each point from the approximated PF and the ideal point. We note that all the approaches present similar Euclidean distances in Fig. 6(a) for instance 2-100, indicating similar convergence for all the approaches, however, for instance 8-100, HMOBEDA presents the smoothest distance fluctuation in Fig. 6(b). This observation, associated with the IGD values in Table 5, indicates that HMOBEDA provides an approximation of the PF with a slightly high concentration around the ideal point.

Notice that in Fig. 6(a), it is easy to see that each solution/circle in the graph is proportional to its marginal probability $P\left(z_{1}, z_{2}\right)$. Therefore, in Fig. 6(a), we can conclude that for 2 objectives the solutions present different probabilities along the PF, with some points concentrated around the ideal point, as also noticeable in Fig. 5.

We note, in Fig. 6(b), that for 8 objectives, the solutions present similar probabilities since there are few large points plotted in the PF. However, HMOBEDA ${ }_{\text {EXT }}$ and HMOBEDA ${ }_{\text {CPT }}$ produce solutions with higher diversity and smaller mean distances from ideal point than HMOBEDA: some solutions might be close to the ideal point but others (near the extreme points) can be far away.

With these experiments, we can conclude that, examining BN structures to provide (after some additional calculations) the marginal distribution of the corresponding objectives values taken over all the algorithm executions, enables the analysis of the influence of fixing evidences in the HMOBEDA approach.

According to the results we note that fixing evidences along the evolutionary process can guide the search through specific regions of the PF, providing different convergence and diversity. HMOBEDA has fixed the highest values for objectives as evidences in the network, providing solutions concentrated around the ideal point. On the other hand, when the evidences are chosen based on a uniform distribution of ideal and extreme points (i.e. with

Table 2
Results for pairwise comparisons between HMOBEDA, HMOBEDA ${ }_{E X T}$ and HMOBEDA ${ }_{C P T}$ using Kruskal--Wallis and Dunn--Sidak's post-hoc tests with $\alpha=5 \%$ for each problem instance.

Table 3
Average run time (min) for each algorithm and instance.
Table 4
Results for pairwise run time comparisons between HMOBEDA, HMOBEDA ${ }_{C P T}$ and HMOBEDA ${ }_{E X T}$ versions using Kruskal--Wallis and Dunn--Sidak's post-hoc tests with $\alpha=5 \%$ for each problem instance.
![img-6.jpeg](img-6.jpeg)

Fig. 6. The Euclidean distance between each solution and the ideal point for (a) 2 objectives and (b) 8 objectives.
equally likely chances of occurrence for each of them), like in HMOBEDA $_{E X T}$, the solutions are better distributed along the front.

These observations are based on the probability of the solutions along the PF and Euclidean distance fluctuations to the ideal point presented in Figs. 6(a) and 6(b), and support the results presented in Table 2, which show that HMOBEDA $_{E X T}$ provides higher diversity (lowest IGD values) especially when the number of objectives increases. Therefore, in the next section we compare HMOBEDA $_{E X T}$ with cutting edges approaches on both MOKP and MNK-landscape instances.

### 5.2. Comparing HMOBEDA $_{E X T}$ with cutting edge approaches

In this section we compare the HMOBEDA $_{E X T}$ version with MBNEDA [11], NSGA-II [68], S-MOGLS [74] (NSGA-II with local search), MOEA/D [75] and NSGA-III [76].

All algorithms used in the comparison are the original ones found in the literature. The exception is NSGA-III that has been
adapted for combinatorial optimization. As discussed by [74], for S-MOGLS we set the probabilities $P_{b}$ and bit-flip operation in LS as 0.1 and $4 / 500$, respectively; the number of neighbors $\left(N_{b}\right)$ to be examined as 20. For NSGA-III, we adopt the same configuration used by [76], i.e., the number of reference points $(H)$ defines the population size $N: H=C_{R+P-1}^{0}$. In MOEA/D, the number of subproblems equals the population size $N$ and the weight vectors $\lambda^{1}, \ldots, \lambda^{N}$ are controlled by the configuration parameter $W$, calculated as proposed by [75]. As discussed by [76], the size of the neighborhood for each weight vector is $T=10$. MOEA/D considers the weighted sum approach. ${ }^{2}$

All algorithms are run on an AMD Opteron Processor 6378 server, CPU 2.40 GHz machine with 125 GB of RAM, running Linux.

In the tables, the best values are highlighted in bold and results with no statistically significant differences with the best values

[^0]
[^0]:    2 This approach is usual for MOKP [75], and can be downloaded from http://http: //dces.essex.ac.uk/staff/zhang/webofmorad.htm. It is also suggested by [20].

Table 5
Average HV ${ }^{-}$and IGD over 30 executions.

Table 6
Capacity metrics over 30 executions for each algorithm. The best values are in bold.

Table 7
Average Run time (min) for each algorithm and instance.

are emphasized in light blue for each instance, using KruskalWallis and Dunn-Sidak's post-hoc tests with a significance level of $\alpha=5 \%$.

### 5.2.1. Experiments with MOKP

Table 5 shows the hypervolume difference ( $\mathrm{HV}^{-}$) and IGD metric, both averaged over 30 executions for HMOBEDA ${ }_{E X T}$ and cutting edge evolutionary approaches.

We note that there is no statistically significant differences between HMOBEDA ${ }_{\text {EXT }}$, NSGA-III and MOEA/D regarding both $\mathrm{HV}^{-}$ indicator and IGD metric for the $2-100,3-100$ and $3-250$ instances. However, HMOBEDA ${ }_{E X T}$ presents the lowest values among all other approaches for $4-250,5-100,5-250,8-100$ and $8-250$ instances.

Table 6 presents the capacity metric ER, which used an approximated front of each algorithm calculated over 30 executions and the reference defined as all non-dominated solutions obtained by all algorithms over all executions.

We can observe that HMOBEDA $_{\text {EXT }}$ is better than the other approaches for almost all instances regarding ER (lowest values), except for $2-100$ and $2-250$ instance. Therefore, we can affirm that HMOBEDA $_{\text {EXT }}$ is a competitive approach for the MOKP particularly for many-objective instances and can be considered a state-of-theart algorithm for the instances considered here.

Fig. 7 presents the approximated PFs for 2-100 instances for HMOBEDA ${ }_{\text {EXT }}$, MBN-EDA, NSGA-II, S-MOGLS, MOEA/D and NSGAIII. Each approximated PF is composed gathering all non-dominated solutions over the 30 executions. Note that this representation is different from the corresponding $\mathrm{HV}^{-}$and IGD metrics which are averaged over 30 executions.
![img-7.jpeg](img-7.jpeg)

Fig. 7. The approximated PFs for 2 objectives $\left(z_{1}, z_{2}\right)$ and 100 items for HMOBEDA ${ }_{\text {EXT }}$, MBN-EDA, NSGA-II, S-MOGLS, MOEA/D and NSGA-III.

We can observe that, for 2-100 instance, HMOBEDA ${ }_{\text {EXT }}$, MOEA/D and NSGA-III present the solutions well distributed along the entire front.

The average run time for each algorithm is presented in Table 7 only as guidance of the corresponding computational effort.

We can observe from Table 7 that the computational efforts required by each algorithm for the same instance are similar to

Table 8
Average HV ${ }^{-}$over 30 independent executions.
each other, keeping the run time at practical levels. However, increasing the number of objectives and variables severely impacts the average computational time of all approaches.

The results also show that NSGA-II presents the lowest computational time for all instances with 2,3 and 4 objectives. However, HMOBEDA $_{\text {EST }}$ presents competitive results in comparison with other approaches for instances with 5 and 8 objectives.

### 5.2.2. Experiments with MNK-landscape problem

In this section we aim to compare the results of HMOBEDA $_{\text {EST }}$, MBN-EDA, NSGA-II, S-MOGLS, MOEA/D and NSGA-III for solving MNK-landscape instances.

Tables 8 and 9 show the hypervolume difference ( $\mathrm{HV}^{-}$), IGD metric respectively, both averaged over 30 executions of each
algorithm. There is no statistically significant differences between HMOBEDA ${ }_{\text {EST }}$, NSGA-III and MOEA/D regarding both $\mathrm{HV}^{-}$indicator and IGD metric for several instances with 2 and 3 objectives. However, there are statistically significant differences for all the remaining instances for both $\mathrm{HV}^{-}$indicator and IGD metric, where HMOBEDA ${ }_{\text {EST }}$ presents the best values in comparison with all other approaches.

Table 10 presents the capacity metrics which, as in the previous case, uses the approximated front of each algorithm calculated over 30 executions and the reference defined as all non-dominated solutions obtained by all algorithms over all executions.

We can observe that HMOBEDA ${ }_{\text {EST }}$ is better than the other approaches for all instances regarding ER. Another important observation is that all solutions from the reference set of M5N20K6,

Table 9
Average IGD over 30 executions landscapes.
M5N20K10 and M5N50K2 instances have been generated using $\mathrm{HMOBEDA}_{\text {EST }}$, as shown by $E R=0$ for this approach on these instances.

Table 11 shows that the run time required by each algorithm for the same instance are similar to each other. In addition, the run times do not present statistically significant differences, except for instances with 2 and 3 objectives, where NSGA-II has the lowest computational time. However, as in MOKP, increasing the number of objectives and variables severely impacts the average computational time of all approaches.

### 5.3. Analyzing the final bayesian network

Aiming to proceed with the exploratory analysis of the PGM structures, Fig. 8 presents three hypothetical examples for $R=2$
objectives, $Q=6$ decision variables and $L=2$ LS parameters, illustrating how the analysis of the graphical structure of the BN can unearth specific characteristics of the MOPs.

In the first example, Fig. 8(a), we can observe that from each objective $\left(Z_{1}\right.$ and $\left.Z_{2}\right)$ there are three related decision variables and each one of the LS parameter $\left(P_{1}\right.$ or $P_{2}$ ) depend on a single objective; however in Fig. 8(b), the two LS parameters ( $P_{1}$ and $P_{2}$ ) depend on the two objectives ( $Z_{1}$ and $Z_{2}$ ). Another different scenario can be shown in 8(c), where the six decision variables depend on the two objectives and the LS parameters ( $P_{1}$ and $P_{2}$ ) depend on a single objective $\left(Z_{2}\right)$. These graphs analysis can help us to understand about the characteristics of the MOP. The comparison between the graphical structures can be used to characterize or classify the MOPs according to the patterns of interactions between variables, objectives and LS parameters.

Table 10
Error Ratio over 30 executions for each algorithm. The best values are in bold.

![img-8.jpeg](img-8.jpeg)

Fig. 8. Three different situations of the relationships that can be captured by the BN for $R=2$ objectives, $Q=6$ decision variables and $L=2$ LS parameters.

Table 11
Average run time (min) for each algorithm and instance.
In this section we provide an interpretation of the probabilistic model learned during the evolutionary process for some MOKP and MNK-landscape instances (examples of easy bi-objective and difficult many objective optimization instances) achieved by the $\mathrm{HMOBEDA}_{\text {EST }}$ version.

The arcs captured by the BN model represent the interactions learned from the data from the beginning until the end of the evolutionary process. For instance, an arc between objective $z_{1}$ and variable $x_{1}$ can indicate that the relationship between them is stronger than the relationship between objective $z_{1}$ and another variable $x_{2}$ that is not linked to $z_{1}$ in the network. Similarly, arcs between objectives and parameters of the local optimizers reveal the existence of relationships between the behavior of local optimizers and the changes in the objectives. By computing the frequencies of the arcs learned by the Bayesian Networks we can determine
which are the most stable interactions and extract other useful information about the particular effect of the objectives on the different local optimizers.

Fig. 9 shows the interactions (circles) between each decision variable $X_{q}, q \in\{1, \ldots, 100\}$, and the objectives $Z_{1}$ and $Z_{2}$, learned by the BN for the MOKP instance 2-100. Each circle has coordinates indicating the number of times an arc $\left(Z_{1}, X_{q}\right)$ has been captured along the evolutionary process for all executions versus a similar measure for $\operatorname{arc}\left(Z_{2}, X_{q}\right)$. Note that the interaction is quite similar for the two objectives, since most of the points are located nearby the +1 slope line. In other words, based on Fig. 9, we can conclude that variables (especially if the number of interactions for a given variable is either very low or very high) are equally affected by both objectives.

![img-9.jpeg](img-9.jpeg)

Fig. 9. For instance 2-100, number of times $\operatorname{arc}\left(Z_{1}, X_{4}\right)$ has been captured in the BN versus a similar measure for $\operatorname{arc}\left(Z_{2}, X_{8}\right)$. Each circle corresponds to one decision variable $X_{8}, q \in\{1, \ldots, 100\}$.
![img-10.jpeg](img-10.jpeg)

Fig. 10. Glyph representation of the three LS parameters (spokes) for each objective $Z_{1}$ to $Z_{8}$ of instance $8-100$.

Fig. 10 focuses on the analysis of BN structure concerning the relations between objectives and LS parameters for the MOKP instance $8-100$. The relations between each objective and the three LS parameters considered in this paper are illustrated by star glyphs. In such representation, each spoke represents one parameter $P_{i}$ and it is proportional to the number of times the $\operatorname{arc}\left(Z_{i}, P_{i}\right), l \in\{1,2,3\}, r \in\{1, \ldots, 8\}$, has been captured along the evolutionary process for all executions. The glyphs allow us to visualize which is the relative strength of the relations. For example, it can be seen in Fig. 10 that objectives $Z_{2}$ and $Z_{5}$ have small influence on the way the parameters are instantiated. On the other hand, $Z_{1}, Z_{3}$ and $Z_{6}$ have great influence, although $Z_{3}$ and $Z_{6}$ seem to have similar balance among the parameters.

We extend this analysis for the MNK-landscape problem. Fig. 11 shows the interactions between each decision variable $X_{8}, q \in$ $\{1, \ldots, 20\}$, and the objectives $Z_{1}$ and $Z_{2}$, learned by the BN for the M2N20K2 instance. The analysis of Fig. 11 reveals that different from 2-100 MOKP, for the M2N20K2 instance of the MNK landscape problem, variables are differently affected by each objective. Notice that some variables are almost exclusively affected by objective $Z_{1}$ and others by objective $Z_{2}$ (as in the extreme points depicted in Fig. 11 for example).

Figs. 12 and 13 present the relations between objectives and LS parameters for M3N50K6 and MBN100K10 instances, respectively.

We can observe, in Fig. 12, that objective $Z_{1}$ has great influence on the parameters and it is better balanced among them. From Fig. 13 we can conclude that $Z_{4}$ has the least influence on the parameters.
![img-11.jpeg](img-11.jpeg)

Fig. 11. For M2N20K2 instance, number of times $\operatorname{arc}\left(Z_{1}, X_{4}\right)$ has been captured in the BN versus a similar measure for $\operatorname{arc}\left(Z_{2}, X_{8}\right)$. Each circle corresponds to one decision variable $X_{8}, q \in\{1, \ldots, 20\}$.
![img-12.jpeg](img-12.jpeg)

Fig. 12. Glyph representation of the three LS parameters (spokes) for each objective $Z_{1}$ to $Z_{3}$ of M3N50K6 instance.
![img-13.jpeg](img-13.jpeg)

Fig. 13. Glyph representation of the three LS parameters (spokes) for each objective $Z_{1}$ to $Z_{8}$ of M8N100K10 instance.

We have shown with these examples that the $\mathrm{HMOBEDA}_{\text {EXT }}$ approach allows a step forward. First, it is possible to estimate the relation between variables and objectives from the analysis of how frequent objective-variable interactions are. Second, it is possible to determine how strong the interaction between objective and LS parameter is from the analysis of objective-parameters interactions in the PGM along the evolution.

## 6. Conclusion

In this paper we have explored, from a probabilistic point of view, the approximated Pareto-front, using the final PGM structure, for a hybrid EDA named Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm (HMOBEDA). We have investigated the influence of using different types of evidence in the behavior of this algorithm. For this, we have extended the original

HMOBEDA to build two other versions with different sample techniques: $\mathrm{HMOBEDA}_{\mathrm{CPT}}$, which considers priori probabilities for the objectives nodes available in the PGM conditional probability table (CPT); and $\mathrm{HMOBEDA}_{\mathrm{EXT}}$, with extreme or ideal points considered as evidences values.

These versions are considered in the context of multi and manyobjective combinatorial optimization in order to analyze how using evidences in the sampling process during the evolution can influence both convergence and diversity along the approximated Pareto Front. This analysis can be useful from a general point of view, defining which strategy is better than other. In addition, we aimed to explore one of the main advantages of using EDA: the possibility of analyzing its probabilistic model which in this work encompasses relationship among objectives, decision variables and configuration parameters of the local search procedure.

We have evaluated the quality of the final Pareto Front approximations of HMOBEDA, HMOBEDA ${ }_{\text {CPT }}$ and HMOBEDA ${ }_{\text {EXT }}$ through the analysis of the final achieved PGM. The Pareto Front as well as the probability of each solution captured by the PGM for all executions have been shown in a single plot. For more than two objectives, the Euclidean distance from each solution to the ideal point has been shown. It is important to point out that this is an important contribution research since it enables to join in a single graphic average information of PFs resulting from its different executions.

In addition, we have analyzed the performance of HMOBEDA versions considering $\mathrm{HV}^{-}$and IGD, concluding that uniformly distributing the evidences among ideal and extreme points of the Pareto Front (HMOBEDA ${ }_{\text {EXT }}$ ) in the sampling process is beneficial for HMOBEDA. Further we compared HMOBEDA ${ }_{\text {EXT }}$ with other techniques on the two addressed problems: MOKP and MNKlandscape. We concluded that, for the instances considered in this work, $\mathrm{HMOBEDA}_{\text {EXT }}$ is a competitive approach for small number of objectives and outperformed the others when the number of objectives increases. In addition, the average run times for all algorithms have been kept in practical levels. These conclusions are based on the statistical analysis made on hypervolume indicator, IGD and a capacity (ER) metrics. Finally, an analysis of the resulting BN structures has been presented in order to evaluate how the interactions among variables, objectives and local search parameters are captured by this type of PGM. Aiming to illustrate the types of information that can be extracted from the models, we have shown that the frequency of arcs in the BNs can indicate how the variables and local search parameters are influenced by the objectives.

Based on the results we concluded that probabilistic modeling arises as a sensitive and feasible way to learn and explore dependencies between variables and objectives and it can be also used for controlling the application of local search operators, as in a parameter tuning approach. Another important conclusion is that $\mathrm{HMOBEDA}_{\text {EXT }}$ is less sensitive to the increasing number of objectives, figuring as a good candidate for many objective optimization.

In the future, MOEA techniques other than Pareto-based approaches should be investigated, such as aggregative/ decomposition based approaches, for example. These new approaches will be investigated with more than eight objectives and applied to other problems. Additionally, an interesting research direction is the use of other types of PGM that can learn and explore dependencies between variables, objectives and automatically control the application of local search operators. Moreover, the BN used to model parameters of the local search, can be extended to model other parameters (especially those associated with individual solutions) as well as those relevant to other search strategies.

## Acknowledgments

M. Delgado acknowledges CNPq, Brazil grant 309935/2017-2. M. Martins acknowledges CAPES/Brazil. R. Santana acknowledges
support from the IT-609-13 program (Basque Government, Spain) and TIN2016-78365-R (Spanish Ministry of Economy, Industry and Competitiveness, Spain).
