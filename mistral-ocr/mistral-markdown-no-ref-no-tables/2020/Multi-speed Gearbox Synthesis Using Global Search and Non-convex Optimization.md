# Multi-speed Gearbox Synthesis Using Global Search and Non-convex Optimization 

Chiara Piacentini ${ }^{2(\boxtimes)}\left(\mathbb{D}\right.$, Hyunmin Cheong ${ }^{1(\boxtimes)}$, Mehran Ebrahimi ${ }^{1}$, and Adrian Butscher ${ }^{1}$<br>${ }^{1}$ Autodesk Research, 661 University Avenue, Toronto, ON M5G 1M1, Canada<br>\{hyunmin.cheong, mehran.ebrahimi, adrian.butscher\}@autodesk.com<br>2 Augmenta Inc., 106 Front St E, Toronto, ON M5A 1E1, Canada<br>chiara@augmenta.ai


#### Abstract

We consider the synthesis problem of a multi-speed gearbox, a mechanical system that receives an input speed and transmits it to an outlet through a series of connected gears, decreasing or increasing the speed according to predetermined transmission ratios. Here we formulate this as a bi-level optimization problem, where the inner problem involves non-convex optimization over continuous parameters of the components, and the outer task explores different configurations of the system. The outer problem is decomposed into sub-tasks and optimized by a variety of global search methods, namely simulated annealing, best-first search and estimation of distribution algorithm. Our experiments show that a three-stage decomposition coupled with a best-first search performs well on small-size problems, and it outmatches other techniques on larger problems when coupled with an estimation of distribution algorithm.


Keywords: Global search $\cdot$ Best-first search $\cdot$ Stochastic search $\cdot$ Evolutionary algorithms $\cdot$ Non-convex optimization.

## 1 Introduction

As demonstrated by the rich literature available [7,13,23,25,33,40], the ability to generate optimal designs is of crucial importance in various engineering applications, since it can lead to significant cost reduction or increased quality of the designed product. In this paper, we focus on the configuration optimization of a specific type of multi-component mechanical system, namely a multi-speed gearbox, which is particularly challenging due to its discrete and bi-level nature.

A gearbox is a mechanical system that transmits and converts an input speed to one or multiple output speeds by means of a series of rotating elements such as shafts and gears. Depending on the arrangements of the gears, we have two different models: the planetary gearbox, used to achieve automatic transmission, and the gear-pairs model, used in manual transmission. Here we only consider the manual transmission, often used in heavy-duty systems due to its higher

durability. A power source rotates the input shaft with an input velocity, which in turn rotates the next connected shaft, propagating the speed throughout the gearbox and towards the output. Pairs of shafts are connected through gear-pairs with different radii. The size of the gears' radii determines the speed change between the connected shafts. Typically, a gearbox is designed to convert the input speed into multiple output speeds according to several transmission ratios. This is achieved by having multiple shafts and multiple gear-pairs connecting those shafts. When a desired transmission ratio is selected, the associated gearpairs are activated via clutches. Objectives considered for gearbox design can be the deviation of the transmission ratios from the nominal values, the power capacity, and the volume or the mass of the gearbox. The gearbox synthesis involves choosing the optimal configuration of shafts and gear-pairs, as well as their parameters such as gears' radii, with respect to the objectives.

The current work formalizes the gearbox synthesis as a bi-level optimization problem. The inner problem (or parameter optimization) takes a gearbox configuration as input and finds the position and size of the gears and shafts within given boundaries. This problem can be cast onto a non-convex continuous optimization problem and solved using state-of-the-art solvers. The outer optimization generates different configurations and we can solve it as a single step or as a decomposed set of sub-tasks. For both these approaches, we implement a variety of algorithms: simulated annealing (SA) and best-first search (BFS), which exploit a formulation of the configuration problem as a state transition system, and an estimation of distribution algorithm (EDA), from the evolutionary algorithms family. While in literature the gearbox synthesis is often modelled as a state transition system, in this paper we explore novel models and adapt them to better suit the search algorithms used. In summary, the contributions of this paper are:

1. formalization of multi-speed gearbox synthesis as a bi-level optimization problem;
2. presentation of two different decomposition approaches of the problem;
3. modelling of different sub-problems as state transition models;
4. application of BFS for multi-speed gearbox synthesis considering both lower and upper bounds;
5. development of an EDA for multi-speed gearbox synthesis.

The paper is organized as follows. Section 2 provides a literature review on gearbox synthesis, while Sect. 3 presents the notation and the problem definition. In Sect. 4 we describe two ways in which we can decompose the problem and we summarize each sub-problems. In Sect. 5 we formulate the sub-problems as state transmission models. Global search algorithms used in this work are described in Sect.6. The experimental evaluation of our approach is shown in Sect. 7. Section 8 concludes our paper.

# 2 Literature Review 

Gearbox design has been extensively studied in the mechanical engineering literature and different variations of the problem have been considered. A large body

of work deals with the parameter optimization problem, with the assumption that a fixed configuration is given as input. The problem can be formulated as a constraint satisfaction problem [26], and many works attempt to solve it using heuristic and meta-heuristic methods, such as local search [29,44], simulated annealing [17], genetic algorithms $[4,11,30,43]$ and particle swarm optimization [31]. Multi-objective versions of the problem can also be found [10,15,27,41].

Gearbox configurations are often represented using graphs [42] and configuration synthesis is typically performed using formal grammars, i.e. a sets of rules that combine a finite set of elements to obtain a potentially infinite set of entities $[9,24]$. In the context of design synthesis, grammar rules offer a way to define how a design can be modified [6] and they have been widely used for gearbox generation $[20,21,32,34,36]$. Tsai et al. consider the configuration optimization of a planetary gearbox, where configurations are generated manually and duplicates are detected using graph isomorphism [36]. Schmidt \& Chase developed a set of grammar rules that can be applied to generate several configurations of a planetary gearbox [32], while Li et al. propose a software that generates sketches of planetary gearboxes by modifying an initial design [20]. The set of rules developed by Lin et al. act on a graph representing the configuration of a manual transmission gearbox [21]. The graph is labelled to capture the relative position of gears and SA is used to generate candidate configurations and to fix some of the components' parameters. When a candidate is generated, collisions between elements are checked according to a set of constraints. The constraints identified by the authors, however, do not guarantee to avoid all possible collisions. Swantner \& Campbell use an exhaustive tree search algorithm to generate a gearbox that can have a single transmission ratio, resulting in a fairly small system. The parameter optimization problem includes bending and stress constraints [34]. In the context of computational design synthesis, a complete search is used to study the quality of grammar rules [18]. Departing from this approach, Pomrehn \& Papalambros consider the optimization of a gear train that outputs a single velocity as a mixed-integer non-linear programming model [28]. Berx et al. study a manual multi-speed gearbox and generate different configurations using constraint programming. A clustering procedure identifies promising candidate configurations, for which feasibility and objective value are calculated [2].

# 3 Problem Description 

We consider the generation of manual multi-speed gearboxes and impose geometric constraints on gears and shafts, as proposed by Berx et al. [2].

### 3.1 Notation

Consider a gearbox consisting of a set of shafts $\mathbf{S}$ and a set of gear-pairs, i.e. gears connected with each other, $\mathbf{P}$. Each pair $p \in \mathbf{P}$ is comprised of an input gear $g_{p}^{i}$ and an output gear $g_{p}^{o}$. We call $\mathbf{G}$ the union of all the input and output gears and we denote with $s_{g}$ the shaft in which a gear $g$ is situated, and $s_{p}^{i}$

and $s_{p}^{o}$ the input and the output shafts of a gear-pair $p$, respectively. We call $\mathbf{C}$ the union of all the shafts and gears. We assume that all the shafts and gears are cylinders aligned along the $z$-axis. Each component $c \in \mathbf{C}$ is defined by the coordinates of the center of the bottom face of the cylinder $\left(x_{c}, y_{c}, z_{c}\right)$, a radius $\rho_{c}$ and a length (or thickness) $l_{c}$. We have set of transmission ratios $\Omega$, where a transmission ratio $\omega$ is a real number indicating the desired ratio of the input and output speed.

A gearbox layout can be represented as an $s-t$ multi-graph $\mathcal{G}=\langle\mathbf{S}, \mathbf{P}\rangle$ where the nodes $\mathbf{S}$ are the shafts and edges $\mathbf{P}$ are the gear-pairs. A source node $s$ is identified as the input shaft, while a sink $t$ is the output shaft of the system.

The graph is required to contain at least $k=|\Omega|$ simple paths from $s$ to $t$. Each simple path $\pi$ is a sequence of edges $\pi=\left(p_{1}, \ldots, p_{n}\right)$, with $p_{i} \in \mathbf{P}$ and all the vertices are distinct, producing a transmission ratio:

$$
\omega_{\pi}=\prod_{j=1}^{n} \frac{\rho_{g_{p_{j}}^{i}}}{\rho_{g_{p_{j}}^{o}}}
$$

where $\rho_{g_{p_{j}}^{i}}$ and $\rho_{g_{p_{j}}^{o}}$ are the radii of the input and output gears for gear-pair $p_{j}$.
Given the set of transmission ratios $\Omega$, we call assignment $\Pi^{\Omega}$ the set of 2-tuples, containing a transmission ratio and a path $\Pi^{\Omega}=\{(\omega, \pi), \forall \omega \in \Omega\}$. We call configuration $\mathcal{C}=\left(\mathcal{G}, \Pi^{\Omega}\right)$ of a gearbox the 2-tuple consisting of the gearbox layout $\mathcal{G}$ and an assignment $\Pi^{\Omega}$.

Figure 1 shows an example of a gearbox with an input shaft $s^{i}$, an output shaft $s^{o}$ and an intermediate shaft $s$. Two gear-pairs are connected between $s^{i}$ and $s\left(p_{1}\right.$ and $\left.p_{2}\right)$ and two between $s$ and $s^{o}\left(p_{3}\right.$ and $\left.p_{4}\right)$. There are four possible paths between $s^{i}$ and $s^{o}: \pi_{1}=\left(p_{1}, p_{3}\right), \pi_{2}=\left(p_{1}, p_{4}\right), \pi_{3}=\left(p_{2}, p_{3}\right)$, and $\pi_{4}=$ $\left(p_{2}, p_{4}\right)$, corresponding to four different transmission ratios $\Omega=\left\{\omega_{1}, \omega_{2}, \omega_{3}, \omega_{4}\right\}$. An example of assignment can be $\Pi^{\Omega}=\left\{\left(\omega_{i}, \pi_{i}\right), \forall i=1, \ldots, 4\right\}$.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Graph representation of the gearbox

# 3.2 Parameter Optimization 

Let $\mathcal{C}=\left(\mathcal{G}, \Pi^{\Omega}\right)$ be a given configuration, where shafts, gear-pairs and their input and the output are known. We want to find the components' parameters $\left(x_{c}, y_{c}, z_{c}, \rho_{c}, l_{c}\right)$ that minimize the total mass of the gears and produce the desired transmission ratios. If we assume that all the gears have a constant thickness $\left(l_{g}\right)$ and are made of same material, the objective function is:

$$
J_{\mathcal{C}}(\rho)=\sum_{g \in \mathbf{G}} \rho_{g}^{2}
$$

The system must satisfy several constraints based on design requirements and physical feasibility. For each pair in the assignment $(\omega, \pi) \in \Pi^{\Omega}$ the transmission ratio produced by $\pi=\left(p_{1}, \ldots, p_{n}\right)$ is within a given $\epsilon$ to the desired value $\omega$ :

$$
\left|\prod_{j=1}^{n} \frac{\rho_{g_{p_{j}}^{i}}}{\rho_{g_{p_{j}}^{o}}}-\omega\right| \leq \epsilon \quad \forall(\omega, \pi) \in \Pi^{\Omega}
$$

Every component $c \in \mathbf{C}$ must be contained inside a parallelepiped with maximum sizes $\left(x_{\max }, y_{\max }, z_{\max }\right)$ and its radius has $\rho_{\min , c}, \rho_{\max , c}$ as limits:

$$
\begin{array}{ll}
\rho_{c} \leq x_{c} \leq x_{\max }-\rho_{c} & \forall c \in \mathbf{C} \\
\rho_{c} \leq y_{c} \leq y_{\max }-\rho_{c} & \forall c \in \mathbf{C} \\
0 \leq z_{c} \leq z_{\max }-l_{c} & \forall c \in \mathbf{C} \\
\rho_{\min , c} \leq \rho_{c} \leq \rho_{\max , c} & \forall c \in \mathbf{C}
\end{array}
$$

A gear $g$ must be placed on its connected shaft $s_{g}$ :

$$
\begin{array}{ll}
x_{g}=x_{s_{g}} & \forall g \in \mathbf{G} \\
y_{g}=y_{s_{g}} & \forall g \in \mathbf{G} \\
z_{g} \leq z_{s_{g}} & \forall g \in \mathbf{G} \\
z_{g}+l_{g} \leq z_{s_{g}}+l_{s_{g}} & \forall g \in \mathbf{G}
\end{array}
$$

In addition, we impose that the gears of each gear-pair must touch:

$$
\begin{array}{ll}
z_{g_{p}^{i}}=z_{g_{p}^{o}} & \forall p \in \mathbf{P} \\
\rho_{g_{p}^{i}}+\rho_{g_{p}^{o}}=\sqrt{\left(x_{s_{g}^{i}}-x_{s_{g}^{o}}\right)^{2}+\left(y_{s_{g}^{i}}-y_{s_{g}^{o}}\right)^{2}} & \forall p \in \mathbf{P}
\end{array}
$$

Finally, we require that two elements cannot occupy the same position in space. For two components $c, d \in \mathbf{C}$ that are not a gear and the shaft in which the gear is placed on, there exist two parameters $\lambda_{c, d}$ and $\alpha_{c, d}$, such that:

$$
\begin{aligned}
& \lambda_{c, d}\left(z_{c}-z_{d}-l_{d}\right)+\left(\alpha_{c, d}-\lambda_{c, d}\right)\left(z_{d}-z_{c}-l_{c}\right)+ \\
& \quad\left(1-\alpha_{c, d}\right)\left[\left(x_{c}-x_{d}\right)^{2}+\left(y_{c}-y_{d}\right)^{2}-\left(\rho_{c}+\rho_{d}\right)^{2}\right]>0 \\
& 0 \leq \lambda_{c, d} \leq \alpha_{c, d} \leq 1
\end{aligned}
$$

This is the continuous formulation of the non-overlapping constraint obtained from the Lagrange duality applied to the distance determination problem $[2,3]$.

Given a configuration $\mathcal{C}$, we define the parametric optimization problem as:

$$
\begin{aligned}
& \min _{\rho} J_{\mathcal{C}}(\rho) \\
& \text { s.t. Constraints (3)-(15) }
\end{aligned}
$$

# 3.3 Configuration Optimization 

When designing a gearbox configuration, we can impose a maximum limit on the number of shafts and the number of gears connecting any two shafts, $N_{\mathbf{S}}$ and $N_{\mathbf{P}}$, respectively. The configuration optimization problem is then:

$$
\begin{aligned}
& \min _{\mathcal{C}} \mathcal{I}(\mathcal{C}) \\
& \text { s.t. }|\mathbf{S}| \leq N_{\mathbf{S}} \\
& \left|\mathbf{P}_{s_{i}, s_{j}}\right| \leq N_{\mathbf{P}} \quad \forall s_{i}, s_{j} \in \mathbf{S}
\end{aligned}
$$

where $\mathbf{P}_{s_{i}, s_{j}}$ is the set of gear-pairs connecting shafts $s_{i}$ and $s_{j}$. Similarly, we define $\mathbf{P}_{s}$ as the set of gear-pairs connected to $s$.

## 4 Problem Decomposition

This section shows two decomposition approaches. In the two-stage decomposition approach, the problem is divided into two sub-tasks:

A1. Transmission ratio path assignment: given a complete multi-graph $\mathcal{G}^{N_{s}, N_{p}}=(\mathbf{S}, \mathbf{P})$ with $N_{s}$ shafts and $N_{p}$ gear-pairs between every two shafts, and a set of transmission ratios $\Omega$, generate an assignment $\Pi^{\Omega}$ using the $s$ - $t$ simple paths in $\mathcal{G}^{N_{s}, N_{p}}$. The layout $\mathcal{G}$ is the union of paths in the $\Pi^{\Omega}$;
A2. Parameter optimization: given the layout $\mathcal{G}$ and the assignment $\Pi^{\Omega}$, solve $\mathcal{I}\left(\mathcal{G}, \Pi^{\Omega}\right)$.

Since working with the complete multi-graph $\mathcal{G}^{N_{\mathbf{S}}, N_{\mathbf{P}}}$ may result in a prohibitive large number of possible assignments, we consider an alternative threestage decomposition approach, where we first select a sub-graph of $\mathcal{G}^{N_{s}, N_{p}}$ with at least $k$ distinct $s-t$ simple paths:

B1. Graph generation: generate a $s-t$ multi-graph $\mathcal{G}=(\mathbf{S}, \mathbf{P})$ with at least $k$ distinct simple paths from the input and output shafts;
B2. Transmission ratio path assignment: given a graph $\mathcal{G}$, find an assignment $\Pi^{\Omega}$ using the $s-t$ simple paths in $\mathcal{G}$;
B3. Parameter optimization: given a graph $\mathcal{G}$ and an assignment $\Pi^{\Omega}$, solve problem $\mathcal{I}\left(\mathcal{G}, \Pi^{\Omega}\right)$.

# 4.1 Graph Generation 

Graph generation entails finding a sub-graph $\mathcal{G}$ of $\tilde{\mathcal{G}}$ with at least $k s-t$ simple paths. Given an edge-weighted graph $\tilde{\mathcal{G}}=(V, E)$, a source node $s \in V$, a sink node $t \in V$ and a positive number $k$, we call min-k-simple paths (mkSP) the problem of finding the minimum weighted edges $E^{\prime} \subseteq E$, such that there exists $k$ distinct simple paths $\pi_{i}$ from $s$ to $t$, whose edges belong to $E^{\prime}: \pi_{i} \subseteq E^{\prime}$ for $i=1, \ldots, k$. In the gearbox synthesis, the input is a complete multi-graph with $\mathcal{G}^{N_{\mathbf{S}}, N_{\mathbf{P}}}$ and the solution can provide a lower bound on the number of gears necessary to add to the system.

The problem can be seen as a particular type of coverage problem, namely min-k-union (mkU) [38]: given a set $\mathcal{U}$, a collection $\mathcal{S}$ of subsets of $\mathcal{U}$, and an integer number $k$, select $k$ subsets of $\mathcal{S}$ to minimize the number of covered elements in $\mathcal{U}$. Min-k-union is the minimization version of the classical maximum coverage problem. While for maximum coverage, a greedy solution has a $(1-1 / e)$ approximation guarantee, mkU is harder to approximate [8].

The reduction of mkSP to mkU is trivial: the set of all the edges $E$ in mkSP is $\mathcal{U}$ in mkU and the set of all paths corresponds to $\mathcal{S}$. This, however, requires the identification of all the $s-t$ simple paths in $\mathcal{G}$, which is a \#P-COMPLETE task in the general case [37].

When generating graphs, we can leverage graph isomorphism to avoid the repeated evaluation of equivalent graphs. While it is not known if the detection of isomorphic graphs can be solved in polynomial time or if it is a NP-COMPLETE problem, efficient solvers are available [22].

### 4.2 Transmission Ratio Path Assignment

Given a graph $\mathcal{G}$ with $n s-t$ simple paths and a set of transmission ratios $\Omega$, the task requires to find an assignment $\Pi^{\omega}$. If we have $k$ transmission ratios, with $k \leq n$, we have $\frac{n!}{(n-k)!}$ assignments. To reduce the number of assignments that we need to check, we can identify those that lead to the same parameter optimization problem.

Consider the example in Fig. 2 with three transmission ratios $\omega_{1}, \omega_{2}, \omega_{3}$. The configuration contains three simple paths: $\pi_{1}=\left(p_{1}, p_{4}\right), \pi_{2}=\left(p_{2}, p_{4}\right), \pi_{1}=$ $\left(p_{3}\right)$ and six assignments can be made: $\left\{\left(\omega_{1}, \pi_{1}\right),\left(\omega_{2}, \pi_{2}\right),\left(\omega_{3}, \pi_{3}\right)\right\},\left\{\left(\omega_{1}, \pi_{1}\right)\right.$,
![img-1.jpeg](img-1.jpeg)


Fig. 2. Example of transmission ratio path assignments and their labeling

$\left.\left(\omega_{2}, \pi_{3}\right),\left(\omega_{3}, \pi_{2}\right)\right\},\left\{\left(\omega_{1}, \pi_{2}\right),\left(\omega_{2}, \pi_{1}\right),\left(\omega_{3}, \pi_{3}\right)\right\},\left\{\left(\omega_{1}, \pi_{2}\right),\left(\omega_{2}, \pi_{3}\right),\left(\omega_{3}, \pi_{1}\right)\right\}$, $\left\{\left(\omega_{1}, \pi_{3}\right),\left(\omega_{2}, \pi_{2}\right),\left(\omega_{3}, \pi_{1}\right)\right\}$, and $\left\{\left(\omega_{1}, \pi_{3}\right),\left(\omega_{2}, \pi_{1}\right),\left(\omega_{3}, \pi_{2}\right)\right\}$. If we have only a single transmission ratio, paths with the same lengths will lead to the same parameters. In our particular example, this allows us to check only three assignments: $\left\{\left(\omega_{1}, \pi_{1}\right),\left(\omega_{2}, \pi_{2}\right),\left(\omega_{3}, \pi_{3}\right)\right\},\left\{\left(\omega_{1}, \pi_{1}\right),\left(\omega_{2}, \pi_{3}\right),\left(\omega_{3}, \pi_{2}\right)\right\}$, and $\left\{\left(\omega_{1}, \pi_{3}\right),\right.$ $\left.\left(\omega_{2}, \pi_{2}\right),\left(\omega_{3}, \pi_{1}\right)\right\}$

Formally, given a gearbox problem, a layout $\mathcal{G}$ and two assignments $\Pi^{\Omega}$ and $\Pi^{\prime \Omega}$ over a set of $s-t$ simple paths in $\mathcal{G}$, we say that the two assignments are equivalent $\Pi^{\Omega} \equiv \Pi^{\prime \Omega}$ if problems $\mathcal{I}\left(\left(\mathcal{G}, \Pi^{\Omega}\right)\right)$ and $\mathcal{I}\left(\left(\mathcal{G}, \Pi^{\prime \Omega}\right)\right)$ produce the same optimal solution. To detect equivalent assignments, we fix an arbitrary order of the transmission ratios and label the edges of the associated paths in their order of appearance. Thus, two assignments with the same labeling are equivalent.

# 4.3 Parameter Optimization 

The parameter optimization $\mathcal{I}(\mathcal{C})$ is a non-convex optimization problem. We solve it using the solver IPOPt [39]. IPOPt is a software specialized in large scale continuous non-linear optimization problems, based on primal-dual interior point method. For non-convex problems, it does not guarantee that the solution found is globally optimal nor that the problem is globally infeasible. As shown in previous work [2], Constraints (14)-(15) are hard to enforce and can cause the solver to get stuck in a region of local infeasibility. To alleviate this problem, we first consider a relaxation of the problem containing only Constraint (3). If the relaxation is infeasible, we also consider the original problem to be infeasible. Otherwise, we use its solution to initialize the values of the radii of the gears. If the solver finds that $\mathcal{I}(\mathcal{C})$ is infeasible, we restart the solver with a different random initialization of the parameters, up to a fixed maximum number of times, or until a feasible solution is found.

## 5 State Transmission Models

In this section, we present different transition systems that can be used to solve the sub-tasks of our problem. Similar to grammar rules [18,21], a transition system can be used to describe how an algorithm moves from one partial solution (a state) to another, using applicable actions.

More formally, a state transition system is defined by a set of states $\mathcal{S}$, a set of possible actions $\mathcal{A}$ and a transition function $\mathcal{T}: \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S}$. An action can be applied to a state if the state satisfies some preconditions. Each transition is characterized by a cost function $\mathcal{Q}_{\mathcal{T}}: \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$. Given an initial state $\sigma_{i} \in \mathcal{S}$ and a set of goal states $\mathcal{S}_{g} \subseteq \mathcal{S}$, we want to find a sequence of applicable actions $\pi=\left(\alpha_{1}, \ldots, \alpha_{n}\right)$, such that after applying the actions from $\sigma_{i}$, we obtain a goal state $\sigma_{g}=\mathcal{T}\left(\mathcal{T}\left(\mathcal{T}\left(\sigma_{i}, \alpha_{1}\right), \ldots\right), \alpha_{n}\right) \in \mathcal{S}_{g}$, using a sequence of actions with minimal cost. In all the sub-tasks considered, the cost does not depend on the transition, but only on the state.

# 5.1 Graph Generation 

A state is an $s$-t multi-graph $\mathcal{G}=(\mathbf{S}, \mathbf{P})$ with nodes $\mathbf{S}$ and edges $\mathbf{P}$. The source of the graph is the input shaft $s^{i} \in \mathbf{S}$ while the sink is the output shaft $s^{o} \in \mathbf{S}$. A goal state is defined as a graph containing $k=|\Omega|$ simple paths from $s_{i}$ to $s_{o}$. We assign cost 0 to non-goal states, while the cost of a goal state is determined by the solution of the nested problem. We report here the primitive actions for this task. However, depending on the algorithm, we use a subset of such actions, or we define new actions as a sequence of these primitive actions. In the following, every action is identified by a name, where the subscript indicates the involved objects (gears, shafts, paths), its preconditions $\Phi$, and the transition function $\mathcal{T}$ from a state $\mathcal{G}=(\mathbf{S}, \mathbf{P})$ :
$-a_{p, s_{j}, s_{k}}$ : add a gear-pair $p$ between shafts $s_{j}, s_{k} \in \mathbf{S} . \Phi:\left|\mathbf{P}_{s_{j}, s_{k}}\right|<N_{p}$, $\mathcal{T}:(\mathbf{S}, \mathbf{P} \cup\{p\})$
$-a_{s}:$ add a new shaft $s . \Phi:|\mathbf{S}|<N_{s} . \mathcal{T}:(\mathbf{S} \cup\{s\}, \mathbf{P})$
$-d_{p}:$ delete edge $p \in \mathbf{P} . \Phi: p \in \mathbf{P} . \mathcal{T}:(\mathbf{S}, \mathbf{P} /\{p\})$
$-d_{s}:$ delete shaft $s \in \mathbf{S} . \Phi: s \in \mathbf{S}, s \neq s^{i}, s \neq s^{o}, \mathcal{T}:(\mathbf{S} /\{s\}, \mathbf{P} / \mathbf{P}_{s})$

### 5.2 Transmission Ratio Path Assignment

We consider two distinct models for the transmission ratio path assignment task. The first model, called paths generation model, incrementally builds paths adding edges, while the second, assignment model, finds all the $s$ - $t$ simple paths in a graph and tries to assign each transmission ratio to one of them.

Paths Generation Model. In path generation, a state is defined as a tuple $\left(\pi_{1}, \ldots, \pi_{k}\right)$, where $\pi_{i}=\left(p_{1}, \ldots, p_{n_{i}}\right)$ is the sequence of gear-pairs associated with the transmission ratio $\omega_{i}$, starting with shaft $s^{i}$. The sequence requires the gearpairs to be connected: i.e. $s_{p_{j}}^{i}=s_{p_{j-1}}^{o}, \forall j=2, \ldots, n_{i}$. A sequence may be empty. We say that a sequence is a complete path if it terminates with shaft $s^{o}$. A goal state is a state where all the sequences of gear-pairs are complete, distinct paths. A goal state uniquely identifies a transmission ratio path assignment. For this task, we only add or delete gear-pairs from a state $\left(\pi_{1}, \ldots, \pi_{k}\right)$ (shafts are automatically added if they are the input or the output of the gear-pair added):

- $a_{p, \pi_{i}}$ : add gear-pair $p$ at the end of $\pi_{i} . \Phi: s_{p}^{i}=s_{p_{n_{i}}}^{o},\left|\mathbf{P}_{s_{p}^{i}, s_{p}^{o}}\right|<N_{p},|\mathbf{S}|<N_{s}$, $\pi_{i} \cup p$ is a simple path. $\mathcal{T}:\left(\pi_{1}, \ldots, \pi_{i} \cup p, \ldots, \pi_{k}\right)$
$-d_{\pi_{i}}:$ delete the last element of $\pi_{i} . \Phi: \pi_{i}$ is not empty. $\mathcal{T}:\left(\pi_{1}, \ldots, \pi_{i} / p_{n_{i}}, \ldots, \pi_{k}\right)$

The cost of a non-goal state is determined by the solution of the relaxed version of the parameter optimization problem, which considers only the transmission ratios associated with complete paths. The cost of goal states is the cost of the full parameter optimization problem.

Assignment Model. For this model, given a graph $\mathcal{G}$ containing $n$ simple paths from $s^{i}$ to $s^{o}$, a state is a partial assignment $\tilde{\Pi}^{\Omega}$, i.e. a subset of $\Pi^{\Omega}$. Actions assign a simple path to a transmission ratio, i.e. add an element $(\omega, \pi)$ to the partial assignment. A goal state is defined as a state where all the transmission ratios are assigned. The cost of a non-goal state is determined by the solution of the relaxed version of the parameter optimization problem over the partial assignment, while for goal states, the cost is the objective value of the full parameter optimization problem.

# 6 Global Search 

This section describes three search algorithms used to solve the gearbox synthesis problem. For each search, both the two-stage and three-stage decomposition approaches are considered (see Fig. 3). Each sub-task is solved using transition systems described in the previous section and its solution is the input of the next sub-task. The first algorithm presented, our baseline, is SA [16]. Next, we consider a BFS [12] that keeps track of both the upper bound and lower bound of solutions, similarly to branch-and-bound [19]. Finally, an EDA, a populationbased meta-heuristics approach is used.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Flowchart of the decomposition approaches

### 6.1 Simulated Annealing

In SA, states are feasible solutions and their cost corresponds to the cost of a solution. A new state is generated by randomly selecting one transition of the transition model and solving the subsequent sub-tasks. If this results in a non-feasible solution, the state is automatically rejected.

Two-Stage Decomposition. The search is initialized with randomly generated paths and the neighborhood is defined by the paths generation model in Sect.5.2. We consider the following actions, obtained by concatenating the actions in Sect.5.2:

- delete gear-pair $p$ at position $i$ in $\pi: d_{p, i, \pi}=d_{p_{n}, \pi}, d_{p_{n-1}, \pi}, \ldots, d_{p_{i-1}, \pi}$,
$a_{\left(s_{p_{i-1}}^{i}, s_{p_{i+1}}^{i}\right), \pi}, a_{p_{i+2}, \pi}, \ldots, a_{p_{n}, \pi}$
- add gear-pair $p$ at position $i$ in $\pi: a_{p, i, \pi}=d_{p_{n}, \pi}, d_{p_{n-1}, \pi}, \ldots, d_{p_{i-1}, \pi}$,
$a_{\left(s_{p_{i-1}}^{i}, s_{p}^{i}\right), \pi}, a_{p, \pi}, a_{\left(s_{p}^{o}, s_{p_{i}}^{o}\right), \pi}, a_{p_{i}, \pi}, \ldots, a_{p_{n}, \pi}$
- replace gear-pair $p_{j}$ with $p_{k}$ in $\pi: r_{p_{j}, p_{k}, i, \pi}=d_{p_{j}, i, \pi}, a_{p_{k}, i, \pi}$

Three-Stage Decomposition. For this approach, we first generate a graph using the graph generation model in Sect.5.1 with the actions devised by Konigseder et al. [18], which are a combination of actions in Sect.5.1:

- create a new gear-pair between two existing shafts: $a_{p, s_{j}, s_{k}}$
- delete an existing gear-pair $p: d_{p}$
- create a new shaft and connect to two existing ones: $a_{s}, a_{p_{i}, s_{p_{j}}^{i}, s}, a_{p_{j}, s, s_{p_{j}}^{o}}$
- delete a shaft: $d_{s}$
- replace a gear-pair: $d_{p}, a_{s}, a_{p_{j}, s_{p}^{i}, s}, a_{p_{k}, s, s_{p}^{o}}$

Starting from a randomly generated graph, the SA randomly selects one of the actions and finds a new graph. The transmission ratio-path assignment problem is solved heuristically by selecting a limited number of assignments, which are then used to solve the parameter optimization problem. The cost of the graph is the best objective value found among the sub-problems considered.

# 6.2 Best-First Search 

In BFS, starting from the initial state, the algorithm selects a node for expansion based on an evaluation function $f$, which represents an estimation of the cost of the best solution. During expansion all the possible successor states are generated, evaluated and inserted into a priority queue. The process is repeated, selecting each time the state in the queue with the lowest $f$, until a goal state is retrieved from the queue. We consider here a tweaked version of BFS that also keeps track of an upper bound [5], which is simply the cost of the best incumbent solution found during the evaluation stage of the algorithm. This allows us to return the such feasible solution when we limit the running time of the algorithm. Our evaluation function $f$ is defined as a lower bound of the cheapest configuration that can be achieved from a state $\sigma$ and it is set to 0 at initialization. The optimality of the algorithm cannot be guaranteed because our parameter optimization problem is not solved to (global) optimality.

Two-Stage Decomposition. Similarly to SA, we solve the transmission ratio path assignment problem using the path generation model in Sect. 5.2. We start a search with a state with empty paths and incrementally add all possible edges to create the first path. When the path is complete, we solve the inner optimization problem to determine the cost of the state and we can start adding edges to create the next path. Notice that the only action that we need is the addition of a gear-pair. The evaluation function is calculated by running the relaxed solver on paths that are completed. In addition, we add a lower bound related to the number of gear-pairs that we need to add to the graph to have $k$ paths. This is calculated by building the graph representing the gearbox layout as the union of the paths and estimating the number of edges necessary to have $k s-t$ simple paths: if the graph has $k s-t$ simple paths, this is the number of edges in the graph, otherwise, we take the number of edges plus one. We calculate the lower bound on the cost by multiplying such number by two (every edge is a pair of gears) and the square of the minimum radius of the gears.

Three-Stage Decomposition. We set the initial state to be a graph containing only the input $s^{i}$ and the output $s^{o}$ shafts and consider the actions in Sect.5.1:

- create a new gear-pair between two existing shafts: $a_{p, s_{j}, s_{k}}$
- create a new gear-pair $p$ between an existing and a new shafts $s: a_{s}, a_{p, s_{j}, s}$

Since we insert all the states explored in the queue and we start with an empty graph, we do not need actions that delete gear-pairs or shafts. We use graph isomorphism to detect duplicated states. When a goal state (a graph with $k$ simple paths from $s^{i}$ to $s^{o}$ ) is generated, we calculate the minimal cost of the graph. This cost is calculated by solving the transmission ratio path assignment problem. The evaluation function is calculated by estimating the minimum number of edges that we need to have a graph with at least $k$ simple paths, similarly to the 2 -stage decomposition approach. Since the cost of a graph is defined by $\mathcal{I}$, which is a non-convex problem, adding a gear-pair does not necessarily increase the cost of a configuration. For this reason, the evaluation function of a goal state is not the cost of the configuration but is the lower bound defined above. Our algorithm does not terminate when a goal state is found, but when the gap between lower and upper bound is 0 or all the states have been explored.

To solve the transmission ratio path assignment problem, we run another BFS using the assignment model in Sect. 5.2, where we start from a state where none of the transmission ratios is assigned and actions correspond to the assignment of a simple path to a transmission ratio.

# 6.3 Estimation of Distribution Algorithm 

The last type of global search method is EDA, a class of meta-heuristic approaches based on the evolution of populations [14]. While typical evolutionary algorithms, such as genetic algorithms, use variation operators such as cross-over and mutation, EDAs use an explicit probability model to generate new solutions,

showing advantages in terms of performance, theoretical convergence, and capturing the structure of the problem space [14]. The probabilities are computed by directly using the frequency statistics of the selected top individuals from a population and indicate the likelihood of a particular solution being included in a set of top quality solutions based on prior observations. EDA has also been successfully applied to the configuration design of vehicle suspension systems [7]. As with the other algorithms, both two and three-stage decomposition approaches are implemented and EDA is used to solve the top-level task. The overall framework for the both approaches is the same except for the details in each of the steps, as detailed below.
i) Generation of Initial Population: As a first step, an initial population of individuals $\mathcal{P}$ is randomly generated.

In the two-stage decomposition approach, an individual is a tuple of $k$ simple paths, each corresponding to a transmission ratio path assignment. Each path is constructed by randomly choosing an edge at a given node from a uniform distribution defined over all possible outgoing edges of the node, starting from the input shaft node $s^{i}$ and ending at the output shaft node $s^{o}$.

In the three-stage decomposition approach, an individual is a graph $\mathcal{G}$. An individual is generated by randomly selecting an edge from a uniform distribution defined over all possible edges, and incrementally adding the selected edge to a null graph until the number of simple paths $n$ is such that $k \leq n \leq n_{\max }$. We impose an upper bound on the number of paths to limit the number of transmission ratio path assignments. If the last edge added results in $n>n_{\max }$, we backtrack one step and add another edge until $k \leq n \leq n_{\max }$.
ii) Evaluation and Selection: Each individual in the population is evaluated by solving the parameter optimization problem. For the three-stage decomposition approach, several transmission ratio path assignments are created exhaustively before parameter optimization. A subset of the population, $\mathcal{P}^{\prime} \subseteq \mathcal{P}$, representing top $t$ individuals, is selected. $\left|\mathcal{P}^{\prime}\right| /|\mathcal{P}|$ is called truncation rate.
iii) Estimation of Probability Distribution: From $\mathcal{P}^{\prime}$, the probability distributions of the edges in the individuals are estimated.

The probability model used for the two-stage decomposition approach is:

$$
\mathbb{P}_{\text {path }, \pi_{j}}(\mathbf{P})=\prod_{p \in \mathbf{P}} \mathbb{P}_{\text {path }, \pi_{j}}\left(p \mid s_{p}^{i}\right) \quad \forall j=1, \ldots, k
$$

Here, a conditional probability distribution is assumed and the probability of a gear-pair $p$ is dependent on its input shaft, $s_{p}^{i}$.

The probability model used for the three-stage decomposition approach is:

$$
\mathbb{P}_{\text {graph }}(\mathbf{P})=\prod_{p \in \mathbf{P}} \mathbb{P}_{\text {graph }}(p)
$$

In other words, a univariate probability distribution is assumed and the probability of an edge $p$ is determined independently from other edges.
iv) New Population Generation: A new population of individuals is generated using the same techniques as in Step i) with probability distributions estimated in Step iii). That is, instead of randomly selecting edges from uniform distributions to construct a graph or a path, the edges are sampled from the probability distributions in Eq. (19) or Eq. (18), depending on the approach.
v) Iterate Steps ii)-iv): Steps ii) to iv) are repeated with the newly generated population until an allocated number of iterations is reached.

# 7 Experimental Evaluation 

Experiments are run on a single desktop computer with two Intel Xeon CPUs E5-2650 v2 2.60 GHz and 32 G of RAM.

### 7.1 Experimental Setup

Datasets. We generate a first dataset with 45 synthetic problem instances (synthetic dataset). Instances have 4,7 and 10 transmission ratios. We fix the minimum transmission ratio to 1 , and the maximum to 2,6 and 10 , respectively. The values of the transmission ratios are generated randomly between the minimum and the maximum. The second dataset (tremec dataset) contains nine realistic problems, five with five transmission ratios and four with ten transmission ratios. The transmission ratios and the size of the gearbox are taken from the specifications found on the TREMEC website [35].

Implementation Details. The inner problem $\mathcal{I}(\mathcal{C})$ is solved with IPOPT [39], using the modeling language CASADI [1]. Isomorphic graphs are detected using the NAUTY library [22]. For EDAs, evaluations are run in parallel across 32 CPU threads available in the computer used. For the two-stage decomposition approach, we use population sizes of 192 for the five-ratio problems and 384 for the ten-ratio problems in the tremec dataset. For the three-stage decomposition approach, we use population size of 64 , while using different time limits for evaluating each individual: three minutes for the five-ratio problems and six minutes for the ten-ratio problems. For all EDAs, the truncation rate and the number of iterations are set to 0.2 and 10, respectively. Both SA and BFS are run on a single thread. The temperature parameter in SA is set to 2000 and decremented every 1000 evaluations with a step size of 5 . Time limits vary depending on the size of the problem and are reported in the next section. They are assumed to be tolerable waiting times from a design process perspective.

Table 1. Results on the synthetic dataset. We report the average and the standard deviation of objective value for problems that are solved by all algorithms (excluding those that cannot solve any problem). We report also the number of problems solved by each algorithm.

Table 2. Results on the tremec dataset. We report the average and the standard deviation of the objective value of each problem. The value marked with * is the objective value of the only solution found in all runs of the algorithm.

# 7.2 Results 

We use the synthetic dataset to test the behaviour of the algorithms running on a single thread: BFS and SA. In Table 1 we report the average solution qualities and the number of problems solved for different groups of problems, using a time-limit of 1 h . The name of the algorithm is followed by 2 or 3 , indicating the two-stage or three-stage decomposition approach, respectively. Every algorithm is run 3 times to account for the randomization in the algorithms. Both SA and BFS perform better when using the three-stage decomposition approach. The two-stage approach fails to find feasible solutions to medium-size problems. In terms of solution quality, BFS outperforms SA for small size problems, while SA generally performs better on problems with more transmission ratios.

All algorithms are tested on the tremec dataset and results are in Table 2. The time limit is 1 and 2 h for problems with 5 and 10 transmission ratios, respectively. Each algorithm is run 10 times for each problem. Results on this dataset confirms that the three-stage decomposition generally outperforms the two-stage. Among the algorithms, EDA is the best performing, mainly attributed to the larger number of solutions that can be evaluated in parallel.

# 8 Conclusion 

In this paper, we consider the multi-speed gearbox synthesis problem formulated as a bi-level optimization problem. The inner task, or parameter optimization, is a non-convex continuous optimization problem, solved with a state-of-the-art solver. For the outer problem, we used two approaches to search over gearbox configurations: the two-stage decomposition approach searches over transmission ratio path assignments, while the three-stage decomposition approach first selects a sub-graph, and then performs the transmission ratio path assignment. We found that the latter consistently outperforms the first in all test problems and search algorithms. We investigated a variety of global search algorithms for solving the sub-tasks of the outer problem. While best-first-search usually performs well on small-size problems, the estimation of distribution algorithm produces better quality solutions for realistic instances. This work demonstrates the value of integrating methods from both the artificial intelligence and optimization fields applied to configuration design problems in mechanical engineering.
