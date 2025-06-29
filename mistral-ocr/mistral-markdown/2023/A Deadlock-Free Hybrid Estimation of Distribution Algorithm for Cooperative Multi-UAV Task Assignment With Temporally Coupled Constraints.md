## A Deadlock-Free Hybrid Estimation of Distribution Algorithm for Cooperative Multi-UAV Task Assignment With Temporally Coupled Constraints

## RUIPENG ZHANG

YANXIANG FENG
YIKANG YANG
Xi'an Jiaotong University, Xi'an, China

## XIAOLING LI

Chang'an University, Xi'an, China

This article addresses the cooperative multianmanned aerial vehicles task assignment problem (CMTAP) with temporally coupled constraints and aims to find a feasible assignment to minimize the equivalent distances of all tasks. We first present a mixed-integer linear programming model of CMTAP. To solve the undesirable deadlocks of CMTAP, a Petri net amender is constructed based on a candidate solution, and a deadlock-free solution is equivalent to a feasible transition sequence that can be fired sequentially in the corresponding amender. With this amender, we present a Petri net-based deadlock amending method (PDAM) with polynomial time complexity to convert a deadlocked solution into a deadlock-free solution. Also, a deadlock-free hybrid estimation of distribution algorithm (DHEDA) is developed for CMTAP by embedding PDAM into the original EDA. To further improve the solution quality, we establish a local exploitation method, and an adaptive operational probability is used

Manuscript received 6 May 2022; revised 30 August 2022; accepted 20 November 2022. Date of publication 25 November 2022; date of current version 9 June 2023.

DOI. No. 10.1109/TAES.2022.3224694
Refereeing of this contribution was handled by H. Xu.
This work was supported in part by the Science and Technology Innovation 2030-Key Project of "New Generation Artificial Intelligence" under Grant 2020AAA0108203 and in part by the National Natural Science Foundation of China under Grant 62003258 and Grant 62103062.

Authors' addresses: Ruipeng Zhang, Yanxiang Feng, and Yikang Yang are with the School of Automation Science and Engineering, Xi'an Jiaotong University, Xi'an 710049, China, E-mail: (zrprepeal@stu.xjtu.edu.cn; fengyanxiang@xjtu.edu.cn; yangyk74@mail.xjtu.edu.cn); Xiaoling Li is with the School of Electronics and Control Engineering, Chang'an University, Xi'an 710064, China, E-mail: (xiaolingli@chd.edu.cn). (Corresponding author: Yikang Yang.)

[^0]to balance the computational burden and local exploitation ability. Then, a match-up-based reassignment method is proposed to cope with time-sensitive targets. Finally, extensive computational experiments demonstrate that PDAM is more effective at solving deadlocks than graph-based methods, particularly for large-scale CMTAP, and DHEDA outperforms existing algorithms when solving CMTAP.

## NOMENCLATURE

$N_{\alpha}$
Total number of unmanned aerial vehicles (UAVs).
$N_{t}$
Total number of targets.
$U$
Set of UAVs.
$D$
Set of tasks.
$\theta_{k}$
Task sequence of $k$-UAV.
$\boldsymbol{\theta}=\left\{\theta_{k} \mid k \in U\right\}$
Task assignment solution for cooperative multi-UAV task assignment problem.
$\Delta=\{\lambda ; \mu\}$
Individual of deadlock-free hybrid estimation of distribution algorithm, where $\lambda$ implies the execution sequence of tasks and $\mu$ represents the assignment information of UAVs.
$\left(N, M_{0}\right) \| \Delta \quad$ Petri net amender based on individual $\Delta$. Transition sequence extracted from $\Delta$.
$\Omega_{\text {all }}$
Set of all individuals.
$\Omega_{x}$
Number of individuals in a population.
$F(\Delta)$
Fitness of individual $\Delta$.
$P_{\text {swap }}$
Probability of swap operations.
$P_{\text {insert }}$
Probability of insert operation.
$P_{\text {reorg }}$
Probability of reorganization operation.
$\pi_{s}$
Detection time of time-sensitive target.
$\pi_{d}{ }^{i}$
Deadline of the $i$ th time-sensitive target.
$\left[\pi_{\text {start }}, \pi_{\text {end }}\right]$
Reassignment horizon.
$\partial$
Replanning time.
$\theta^{r}$
Reassignment solution.

## I. INTRODUCTION

Unmanned aerial vehicles (UAVs) are widely used in the civilian and military fields, such as search and rescue [1], [2], mineral exploration [3], transportation [4], and military attacks [5], [6], [7]. However, it is difficult for a single UAV to complete complex tasks alone. Thus, multi-UAV systems are being developed to overcome the shortcomings of a single UAV because they can perform tasks cooperatively and in parallel. Task allocation is a critical factor for multi-UAV systems since it determines, which UAVs are assigned to specific targets or tasks. But due to the large solution space or temporal relations among tasks, it is challenging to obtain an effective and feasible task assignment for multi-UAV systems [7].

The cooperative multi-UAV task assignment problem (CMTAP) has recently received increasing attention. Essentially, CMTAP is a nondeterministic polynomial combinatorial optimization problem [9]. Various researchers have proposed a number of mathematical models to solve CMTAP [10], [11], [12], [13], [14]. In particular, Schumacher et al. [10] proposed a mixed-integer linear programming model (MILP) that considers UAV constraints. Evers et al. [11]


[^0]:    0018-9251 © 2022 IEEE

presented an orienteering problem model and then extended it to fit the dynamics and complexity of UAV missions. Zhao et al. [12] developed a multiagent task assignment model and obtained task assignment results using a $Q$-learning network. The resulting dynamic programming model is described in [13] and [14].

Existing approaches to solve CMTAP fall into the following two categories: centralized and distributed. The former consists of some optimization algorithms, such as genetic algorithms [15], [16], [17], ant colony algorithms [18], [19], particle swarm optimization algorithms [20], and wolf pack search algorithms [8]. However, these algorithms may easily fall into local optima. For distributed approaches, Choi et al. [23] presented a consensus-based bundle algorithm (CBBA) that uses a market-based decision strategy and uses a consensus routine to produce conflict-free solutions. Wu et al. [24] proposed their method based on the consensus algorithm and the online cooperative strategy, and the Bayesian theorem was used to estimate a target. Kim et al. [25] presented an extension of CBBA and provided a systematic way of grouping the UAVs based on their task preference. These distributed methods achieve a better robustness than centralized methods but struggle with complex constraints.

There is typically complex task precedence when considering multiple tasks. For example, the before relation of tasks refers to that a task must be completed before another begins. If tasks are assigned inappropriately, an undesirable phenomenon called deadlock will occur in the solution. In a deadlock, several UAVs performing tasks fall into a circular-waiting pattern, and all tasks cannot be executed in the worst case [26]. To solve this problem, several studies have investigated deadlock-free task assignments [8], [27], [28], [29], [30], [31]. Specifically, Lemaire et al. [27] dealt with deadlocks by swapping the order of two tasks that violate task precedence constraints. Deng et al. [28] developed a graph theory-based method that detects deadlocks by monitoring the strongly connected components in the task-precedence graph (TPG) and amends them just by matrix transposition. However, too many matrix operations and loops may lead to poor algorithm efficiency. Chen et al. [8] improved the method used in [28] to solve deadlocks by reversing edges instead of using complex matrix operations. Xu et al. [29] proposed a target-bundled genetic algorithm in which deadlocks are avoided using a special encoding method. Customized crossover and mutation operators are used to generate deadlock-free offspring. This approach was enhanced in [30] and [31]. Ye et al. [30] presented a mutation operator with a state-transition scheme to enhance the stochastic searching ability. Tian et al. [31] used a clustering method to sort the targets, through which the computational complexity of the CMTAP was reduced. As a graphical and mathematical modeling tool of discrete-event systems (DESs), Petri nets (PNs) can build state equations, algebraic equations, and other mathematical models of system behavior [33]. These characteristics make PN an efficient mathematical tool that can accurately describe the coupling relation between tasks and UAVs.

However, no studies have modeled CMTAP solutions using PNs.

Considering the advantages of PNs in modeling different problems, this study presents a PN amender to resolve the deadlock problem of CMTAP. In this amender, task execution is represented by the firing of corresponding transition, and all tasks are assigned to specific UAVs, but their execution order is not fixed. A deadlock-free solution is equivalent to a feasible transition sequence that contains all transitions and can be fired sequentially in the amender. According to this modeling formalism, we also develop a PN-based deadlock amending method (PDAM) to convert a deadlock individual into a deadlock-free individual. Compared with existing deadlock resolution methods [8], [27], [28], [29], [30], [31], the proposed PDAM provides the following advantages.

1) PDAM has polynomial computational complexity, which means that it can solve deadlocks effectively and quickly, particularly for large-scale CMTAP (see the experiments in Section IV-B).
2) Unlike the graph-based method [8] and [28], PDAM does not need to iterate repeatedly such that no new deadlocks are created during the amending process.
3) PDAM imposes no restrictions on the search mechanism, and the quality of the solutions is not affected, while the methods used in [29], [30], and [31] may fail to do so.

By embedding PDAM into the estimation of distribution algorithm (EDA), we propose an algorithm called the deadlock-free hybrid estimation of distribution algorithm (DHEDA) to solve CMTAP by minimizing the total equivalent distance. EDA is an evolutionary algorithm that reproduces offspring using a probabilistic model instead of individual variation. A potential solution is represented as an individual with two sections: a permutation of tasks and a UAV assignment. To further improve the solution quality, we propose a local exploitation method containing three dedicated operations. Then, an adaptive operational probability is used to balance the computational cost and local exploitation ability. Finally, computational experiments are conducted, and experimental results show that DHEDA outperforms existing algorithms because it provides the best assignment for 32 of 36 instances among the four compared algorithms.

We also extend DHEDA to address the unexpected time-sensitive targets and propose a match-up-based reassignment method, which is confirmed to provide not only good feasible solutions but also advantages in reducing computation time and improving system stability. It also verifies the effectiveness of PDAM on the reassignment problems.

The primary contributions of this study are as follows. First, this article establishes an MILP model for CMTAP with temporally coupled constraints. Second, PDAM is proposed, and its effectiveness and computational complexity in solving deadlocks are demonstrated. Third, based on PDAM, we design DHEDA to solve CMTAP. A dedicated

local exploitation method is used to obtain higher quality solutions. Fourth, a match-up-based reassignment method is presented to cope with time-sensitive targets. Last, an experimental scheme is performed to validate the algorithmic capabilities.

The rest of this article is organized as follows. Section II describes the CMTAP model. Section III describes the proposed PDAM method and demonstrates its ability to resolve deadlocks. By embedding PDAM into EDA, we develop the DHEDA. Section IV describes extensive numerical experiments and analyzes their results. Finally, Section V concludes this article.

## II. PROBLEM DESCRIPTION AND FORMULATION

This article investigates a CMTAP that consists of a team of UAVs performing different predefined tasks on known targets. Multiple tasks on a target must satisfy temporally coupled constraints. This section presents the details of UAVs, targets, and tasks involved in a CMTAP and yields the mathematical formulation of the considered CMTAP.

## A. Unmanned Aerial vehicles

We let $U \equiv\left\{1, \ldots, N_{u}\right\}$ denote a set of $N_{u}$ UAVs that are initially located at different positions. Each UAV, which is denoted as $k$-UAV, $k \in U$, has a flying distance limitation $L_{\text {lim }}{ }^{k}$. The number of tasks that $k$-UAV performs cannot exceed $N_{\text {lim }}{ }^{k}$ due to its capacity limitation, and we let $v_{k}$ be the speed of $k$-UAV.

## B. Targets and Tasks

We assume that there are $N_{t}$ ground targets whose positions are known in advance. Each target must be assigned three types of tasks (classification, attack, and verification); thus, there are $3 N_{t}$ tasks in total. For a specific target, the precedence of its three tasks must be satisfied; thus, before a target is attacked by UAVs, classification must be performed, and after the attack is completed, verification is required. To distinguish from the UAVs in $U$, we denote all tasks by numbers in $D \equiv\left\{N_{u}+1, \ldots, 3 N_{t}+N_{u}\right\}$.

For a task $j \in D$, let $l=\operatorname{div}\left(j-N_{u}-1,3\right)+1$ and $h=\operatorname{mod}\left(j-N_{u}-1,3\right)+1$, where $\operatorname{div}(a, b)$ takes the quotient when $a$ is divided by $b$, and the remainder is obtained by $\operatorname{mod}(a, b)$. Then, the $j$-task belongs to the $l$ th target, and $h=1,2,3$ implies that the $j$-task is a classification, attack, and verification task, respectively.

We also let $\boldsymbol{\theta}=\left\{\theta_{1}, \theta_{2}, \ldots, \theta_{N u}\right\}$ denote a task assignment solution, where $\theta_{k}, k \in U$, is a task sequence containing all tasks that must be performed sequentially by $k$-UAV.

## C. Mathematical Model of CMTAP

CMTAP can be considered a multitravel salesman problem (m-TSP) [32], denoted $\mathcal{G}=(\mathcal{V}, \mathcal{E})$, where $\mathcal{V} \equiv U \cup D$ collects all depot or task nodes and $\mathcal{E}$ contains all edges that represent the shortest traveling path between any two nodes. The $k$-UAV (or a salesman) is initially located in its depot node $k \in U$, and all nodes in $D$ can be considered
![img-0.jpeg](img-0.jpeg)

Fig. 1. Timeline of the $j$-task node.
to be cities. To solve such an m-TSP, we must determine routes for salesmen with the goal of minimizing their total journey cost, and all cities must be visited exactly once. We assume that each UAV leaves a task node immediately after finishing the corresponding task, and it must return to its original depot node after completing the tour.

For a $j$-task, $j \in D$, some critical time parameters are defined as follows:

1) $S_{j}$ : the departure time when a UAV flies to the $j$-task node, which is equal to zero or the time when the UAV leaves the previous node.
2) $A_{j}$ : the time a UAV arrives at $j$-task node.
3) $E_{j}$ : the time when a UAV executes $j$-task.
4) $C_{j}$ : the completion time of $j$-task.
5) $H_{j}$ : the time required to perform $j$-task.

The relationship between $S_{j}, A_{j}, E_{j}$, and $C_{j}$ is shown in Fig. 1. The interval between $S_{j}$ and $A_{j}$ is the flying time, and the waiting time is equal to $E_{j}-A_{j}$. Therefore, time interval $E_{j}-S_{j}$ is the time consumed before $j$-task is executed. If the $j$-task is assigned to $k$-UAV, we use $\left(E_{j}-S_{j}\right) \times v_{k}$ to represent the corresponding equivalent distance.

The mathematical model of the studied CMTAP is presented as follows:

$$
\begin{aligned}
& \min \sum_{i \in v} \sum_{j \in D} \sum_{k \in U}\left(E_{j}-S_{j}\right) v_{k} x_{i j}^{k} \\
& \text { s.t. } \sum_{j \in D} x_{k j}^{k}=1, k \in U \\
& \sum_{j \in D} x_{j k}^{k}=1, k \in U \\
& \sum_{k \in U} x_{k j}^{k}+\sum_{k \in U} \sum_{i \in D} x_{i j}^{k}=1, j \in D \\
& x_{k j}^{k}+\sum_{i \in D} x_{i j}^{k}-x_{j k}^{k}-\sum_{j \in D} x_{j i}^{k}=0, k \in U, j \in D \\
& u_{j}+\left(3 N_{t}-2\right) \sum_{k \in U} x_{k j}^{k}-\sum_{k \in U} x_{j k}^{k} \leq 3 N_{t}-1 \quad \forall j \in D \\
& u_{i}-u_{j}+3 N_{t} \sum_{k \in U} \\
& x_{i j}^{k}+\left(3 N_{t}-2\right) \sum_{k \in U} x_{j i}^{k} \leq 3 N_{t}-1 \quad \forall i, j \in D, i \neq j \\
& \sum_{i \in D} \sum_{j \in v} x_{i j}^{k} \leq N_{\mathrm{Lim}}^{k}, k \in U \\
& \sum_{j \in D} x_{k j}^{k} L(k, j)+\sum_{i \in D} \\
& \sum_{j \in D} x_{i j}^{k} L(i, j)+\sum_{j \in D} x_{j k}^{k} L(k, j) \leq L_{\mathrm{Lim}}^{k}, k \in U
\end{aligned}
$$

$\sum_{k \in U}\left(S_{j}-E_{i}-H_{i}\right) x_{i j}^{k}=0 \quad \forall i, j \in D$
$\sum_{k \in U} S_{j} x_{k j}^{k}=0 \quad \forall j \in D$
$A_{j}-S_{j}=\frac{\sum_{k \in U} \sum_{i \in v} L(i, j) x_{i j}^{k}}{v_{k}} \quad \forall j \in D$
$E_{3 s+1+N_{n}}+H_{3 s+1+N_{n}} \leq E_{3 s+2+N_{n}} \quad \forall s=\left\{0, \ldots, N_{t}-1\right\}$
$E_{3 s+2+N_{n}}+H_{3 s+2+N_{n}} \leq E_{3 s+3+N_{n}} \quad \forall s=\left\{0, \ldots, N_{t}-1\right\}$
where $x_{i j}{ }^{k}$ is a binary decision variable that describes the task assignment solution $\boldsymbol{\theta} ; x_{i j}{ }^{k}=1$ if $k$-UAV flies from $i$-node to $j$-node, and otherwise, $x_{i j}{ }^{k}=0 ; L(i, j)$ represents the shortest distance between the $i$-node and $j$-node, which can be calculated using the Euclidean distance between node coordinates; and $u_{j}$ is the number of nodes that the UAV has visited until node $j$. Equation (1) is the objective function, which aims to minimize the total equivalent distances of all tasks; Equations (2) and (3) indicate that each UAV takes off from the corresponding depot node and returns after finishing its tour; Equations (4) and (5) indicate that only one specific UAV arrives and then departs at each task node; Equations (6) and (7) are the traditional subtour elimination constraints (SECs); Equation (8) [resp. (9)] implies the capacity (resp. flying distance) constraint for UAVs; Equation (10) indicates that the departure time of the $j$-task equals the completion time of the $i$-task if a UAV is flying from $i$ to $j$; Equation (11) implies that all UAVs start from their corresponding deports concurrently (i.e., time zero); Equation (12) shows the constraints on flight time for all tasks; and (13) and (14) represent the temporal relationship between classification, attack, and verification tasks on the same target.

## III. DEADLOCK-FREE HYBRID ESTIMATION OF DISTRIBUTION ALGORITHM

This article develops a DHEDA to solve CMTAP to minimize the total equivalent distance. The candidate solutions of DHEDA are evaluated by the fitness value, and the probabilistic model is used to extract the features of superior individuals. In each iteration, new individuals are generated to replace some old individuals with the poor performance. A dedicated local exploitation method is used to enhance the solution quality. The primary components of DHEDA are described in the following.

## A. Encoder and Initialization

We let $\Delta=\{\lambda ; \mu\}$ be an individual representing a solution $\boldsymbol{\theta}$ for CMTAP, where $\lambda=\left(\lambda[1], \lambda[2], \ldots, \lambda\left[3 N_{t}\right]\right)$ is a permutation of all tasks in which each task appears exactly once, and $\mu=\left(\mu[1], \mu[2], \ldots, \mu\left[3 N_{t}\right]\right)$ is a sequence of UAVs. For example, we consider an individual $\Delta=\{\lambda$; $\mu\}$ shown in Fig. 2, where $\lambda=(6,8,3,5,4,7)$ implies the execution sequence of tasks and $\mu=(1,2,1,1,2,1)$ represents the assignment information of UAVs. We assume

| $\lambda$ | 6 | 8 | 3 | 5 | 4 | 7 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $\mu$ | 1 | 2 | 1 | 1 | 2 | 1 |

Fig. 2. Individual for CMTAP with $U=\{1,2\}$ and $D=\{3,4, \ldots, 8\}$.
![img-1.jpeg](img-1.jpeg)

Fig. 3. Digraph representation of a deadlocked solution.
that the initial population consists of $N_{p}$ randomly generated individuals.

## B. Decoder

Given an individual $\Delta=\{\lambda ; \mu\}$, after applying Algorithm BD, we can obtain a solution $\boldsymbol{\theta}$. However, if tasks are assigned inappropriately, constraints (8) or (9) cannot be satisfied, and deadlocks could arise in solution $\boldsymbol{\theta}$.

## Algorithm: BD (Basic Decoding Method).

Input: an individual $\Delta=\{\lambda ; \mu\}$;
Output: a candidate solution $\boldsymbol{\theta}=\left\{\theta_{k} \mid k \in U\right\}$;
1: Let each $\theta_{k}=\varnothing, k \in U$;
2: for $m \in\left\{1,2, \ldots, 3 N_{t}\right\}$
3: Insert $\lambda[m]$-task to the end of task sequence $\theta_{p_{[m]}}$.
4: end
5: Output candidate solution $\boldsymbol{\theta}$

EXAMPLE 1 Considering $\Delta=\{\lambda ; \mu\}$ in Fig. 2, the corresponding solution $\boldsymbol{\theta}=\left\{\theta_{1}, \theta_{2}\right\}$ is obtained by Algorithm BD, where $\theta_{1}=<6,3,5,7>$ and $\theta_{2}=<8,4>$. We use a digraph $\mathcal{G}=(\aleph, \xi)$ to represent $\boldsymbol{\theta}$, as shown in Fig. 3, where $\aleph=U \cup D$, the dotted arcs imply the consecutive tasks on the same target, and the task-executing order of UAVs is indicated by solid arcs. Fig. 3 shows that the 8 -task is performed before the 4 -task, the 7 -task is before the 8 -task, and the 5 -task is before the 7 -task; thus, the 5 -task must be performed prior to the 4 -task, leading to a contradiction with the premise that the 4 -task should be completed before performing the 5 -task. Thus, a deadlock occurs in $\boldsymbol{\theta}$. Generally, that deadlock can be characterized by a cycle composed of nodes in $\{4,5,7,8\}$.

1) Constraint Amending Method: Algorithm CD modifies individual $\Delta=\{\lambda ; \mu\}$ so that it can meet constraints (8) and (9). We let $\operatorname{dis}\left(\theta_{k}\right)$ be the flight distance of $k$-UAV to finish all its tasks and let $\left|\theta_{k}\right|$ denote the number of tasks assigned to $k$-UAV in $\boldsymbol{\theta}$.

Algorithm: CD (Constraint Decoding Method).
Input: an individual $\Delta=\{\lambda ; \mu\}$;
Output: the modified individual $\Delta^{\prime}=\left\{\lambda^{\prime} ; \mu^{\prime}\right\}$, where (8) and (9) are met.
1: Obtain solution $\boldsymbol{\theta}$ from $\Delta$ by Algorithm BD;
2: Let $G=\left\{u \in U \mid\left|\theta_{u}\right|<N_{\lim }{ }^{n}\right\}$ and $X=\{x \in U$ $\left.\left|\left|\theta_{u}\right|>N_{\lim }{ }^{x}\right\}\right)$
3: while $(X \neq \varnothing)$
4: Choose $x \in X$ and a $d$-task $\in \theta_{u}$, let $p$ be the index of the $d$-task in $\lambda$, i.e., $\lambda[p]=d$;
5: Let $u_{u}=\operatorname{argmin}_{u \in G} L(d, u), u_{u} \in G$, the initial position of $u_{u}$ is closest to $d$;
6: Set $\mu[p]=u_{u}$;
7: Update $\boldsymbol{\theta}, G$, and $X$;
8: end
9: Let $Y=\left\{y \in U \mid \operatorname{dis}\left(\theta_{y}\right)>L_{\lim }{ }^{y}\right\}$;
10: while $(Y \neq \varnothing)$
11: Choose $y \in Y$ and $d^{\prime}$-task $\in \theta_{y}$, Let $p^{\prime}$ be the index of the $d^{\prime}$-task in $\lambda, \lambda\left[p^{\prime}\right]=d^{\prime}$;
12: Let $u_{u^{\prime}}=\operatorname{argmin}_{u \in G} L\left(d^{\prime}, u\right)$;
13: Set $\mu\left[p^{\prime}\right]=u_{u^{\prime}}$;
14: Update $\boldsymbol{\theta}, G$, and $Y$;
15: end
16: Let $\lambda^{\prime}=\lambda$ and $\mu^{\prime}=\mu$;
17: Output generated individual $\Delta^{\prime}=\left\{\lambda^{\prime} ; \mu^{\prime}\right\}$;

In Algorithm CD, $X=\left\{x \in U \mid\left|\theta_{x}\right|>N_{\lim }{ }^{x}\right\}$ and $Y=\left\{y \in U \mid \operatorname{dis}\left(\theta_{y}\right)>L_{\lim }{ }^{y}\right\}$ denote the set of UAVs whose assigned task sequence violates constraints (8) and (9), respectively. If $X \neq \varnothing$, we choose $x \in X$ and $d \in \theta_{x}$, we let $u_{u}$ be the UAV in $G=\left\{u \in U \mid\left|\theta_{u}\right|<N_{\lim }{ }^{u}\right\}$ whose initial position is closest to the $d$-task, and then, we reassign $d$ to $u_{u}$. If $Y \neq \varnothing$, we take a similar action on $Y$. The output individual $\Delta^{\prime}$ satisfies (8) and (9).
2) Deadlock-Free Amending Method: We introduce a PN-based method to resolve deadlocks in CMTAP effectively. PN is a modeling formalism for DESs, and readers are assumed to be familiar with definitions and notations about PNs; for more details, see [33] and the supplemental file [39]. We start by giving a deadlock amender based on an assignment solution of CMTAP.

DEFINITION 1 Given an individual $\Delta=\{\lambda ; \mu\}$ for CMTAP, let $\boldsymbol{\theta}=\left\{\theta_{1}, \theta_{2}, \ldots, \theta_{N u}\right\}$ be the corresponding solution by Algorithm BD. Then, PN deadlock amender $\left(N, M_{0}\right) \| \Delta$ is established by the following steps.

Step 1: For the $l$ th target, we define $\mathrm{PN}\left(\alpha_{l}, M_{l}\right)=\left(P_{l}\right.$, $\left.T_{l}, F_{l}, M_{l}\right)$, where $P_{l}=\left\{p_{l s}, p_{l 1}, p_{l 2}, p_{l c}\right\}, T_{l}=\left\{t_{l 1}\right.$, $\left.t_{l 2}, t_{l 3}\right\}, F_{l}=\left\{\left(p_{l s}, t_{l 1}\right),\left(t_{l 3}, p_{l c}\right)\right\} \cup\left\{\left(t_{l h}, p_{l h}\right)\left(p_{l h}\right.\right.$, $\left.\left.t_{l, h+1}\right)\right\|h \in\{1,2\}\}, M_{l}\left(p_{l s}\right)=1$, and $M_{l}(p)=0, \forall p$ $\in P_{l} \backslash\left\{p_{l s}\right\}$.
Step 2: For $k$-UAV, we define a $\mathrm{PN}\left(\beta_{k}, M_{k}\right)=\left(\left\{u_{k}\right\}\right.$, $\left.T_{k}, F_{k}, M_{k}\right)$, where $u_{k}$ is the resource place corresponding to $k$-UAV, $T_{k}=\left\{t_{l h} \mid, l=\operatorname{div}\left(j-N_{u}-1\right.\right.$,

$$
\begin{aligned}
& \text { 3) }+1, h=\bmod \left(j-N_{u}-1,3\right)+1, \forall j \in \theta_{k}\}, F_{k} \\
& =\left\{\left(t, u_{k}\right),\left(u_{k}, t\right) \mid t \in T_{k}\right\}, M_{k}\left(u_{k}\right)=1
\end{aligned}
$$

Step 3: The amender $\left(N, M_{0}\right) \| \Delta$ is obtained by composing all $\left(\alpha_{l}, M_{l}\right)$ and $\left(\beta_{k}, M_{k}\right)$ :
$\left(N, M_{0}\right) \| \Delta=\otimes_{l \in\{1, \ldots, N t\}}\left(\alpha_{l}, M_{l}\right) \otimes_{k \in\{1, \ldots, N u\}}\left(\beta_{k}\right.$, $\left.M_{k}\right)$
where operator $\otimes$ represents the composition of two PNs via their common places and transitions.

The subnet $\left(\alpha_{l}, M_{l}\right)$ established in Step 1 represents the execution procedure of tasks on the $l$ th target. Transitions $t_{l 1}, t_{l 2}$, and $t_{l 3}$ represent the classification, attack, and verification tasks, respectively, assigned for the $l$ th target. $p_{l s}$ and $p_{l c}$ are the source and sink places, respectively, and $p_{l 1}$ and $p_{l 2}$ represent the intermediate states. Initially, $p_{l s}$ is marked by a unique token, which moves in the ordering $p_{l s} \rightarrow p_{l 1} \rightarrow p_{l 2} \rightarrow p_{l c}$. When the token arrives in $p_{l c}$, all tasks in the $l$ th target are finished.

The subnet $\left(\beta_{k}, M_{k}\right)$ established in Step 2 indicates the task assignment of $k$-UAV. Then, each transition $t_{l h}$ $\in T_{k}$ in $\left(\beta_{k}, M_{k}\right)$, which connects resource place $u_{k}$ by a pair of directed arcs $\left(t_{l h}, u_{k}\right)$ and $\left(u_{k}, t_{l h}\right)$, denotes that the corresponding task is assigned to $k$-UAV (i.e., $T_{k}$ denotes the set of transitions (or tasks) assigned to $k$-UAV). $u_{k}$ always contains one token.

EXAMPLE 2 We reconsider the individual $\Delta=\{\lambda ; \mu\}$ in Fig. 2; the corresponding solution is $\boldsymbol{\theta}=\left\{\theta_{1}, \theta_{2}\right\}$, where $\theta_{1}=<6,3,5,7>$ and $\theta_{2}=<8,4>$. By Definition 1, PNs $\left(\alpha_{l}, M_{l}\right), l \in\{1,2\}$ are shown in Fig. 4(a). We let $u_{k}$ be the resource place for $k$-UAV, $k \in\{1,2\}$, with a token in it. According to $\boldsymbol{\theta}$, we have $T_{1}=\left\{t_{21}, t_{11}, t_{13}, t_{22}\right\}$ and $T_{2}=$ $\left\{t_{23}, t_{12}\right\}$. The corresponding $\mathrm{PN}\left(\beta_{k}, M_{k}\right)$ for the $k$-UAV is shown in Fig. 4(b). Finally, the composition of all $\left(\alpha_{l}\right.$, $M_{l}$ ) and $\left(\beta_{k}, M_{k}\right)$ is the PN deadlock amender $\left(N, M_{0}\right) \| \Delta$, which is shown in Fig. 4(c).

Next, we present some properties of the PN amender $\left(N, M_{0}\right) \| \Delta$.

PROPOSITION 1 We let $\Delta=\{\lambda ; \mu\}$ be an individual of the studied CMTAP. The PN amender $\left(N, M_{0}\right) \| \Delta$ is safe and strictly $L_{1}$-live.

Proof (1-bounded safe) There is precisely one token in each place $p_{l s}$ and $u_{k}$ under the initial marking $M_{0}$. Thus, $M_{0}$ is 1 -bounded safe. We let $M$ be a safe reachable marking of $\left(N, M_{0}\right) \| \Delta$ and $t$ be an enabled transition under $M$. We assume that $M\left[t>M^{\prime}\right.$. Due to the safety of $M$, tokens in each place are no more than one. All arcs in $\left(N, M_{0}\right) \| \Delta$ have a weight of one, and the firing of $t$ adds a token into an empty place or removes a token from a place. Thus, tokens in each place under $M^{\prime}$ are no more than one, and $M^{\prime}$ is also 1-bounded safe. Then, using the induction method, all reachable markings of $\left(N, M_{0}\right) \| \Delta$ are found to be safe.
( $L_{1}$-live) We let $u_{k}$ and $p$ be the input places of $t_{l h}$, i.e., ${ }^{\star} t_{l h}$ $=\left\{u_{k}, p\right\}$. According to Definition 1, $u_{k}$ is always marked by one token. Thus, if $t_{l h}$ is enabled, there must exist a token in $p$. The token flow in $\left(\alpha_{l}, M_{l}\right)$ is unidirectional, and $p$ will

![img-2.jpeg](img-2.jpeg)

Fig. 4. (a) $\operatorname{PNs}\left(\alpha_{1}, M_{1}\right)$ and $\left(\alpha_{2}, M_{2}\right)$. (b) $\operatorname{PNs}\left(\beta_{1}, M_{1}\right)$ and $\left(\beta_{2}, M_{2}\right)$. (c) Corresponding PN deadlock amender $\left(N, M_{0}\right) \| \Delta$.
eventually gain a token under a reachable marking, in which $t_{l h}$ can be fired. Conversely, if $t_{l h}$ is fired, $p$ will no longer gain tokens. Therefore, each $t_{l h}$ can be fired exactly once, and $\left(N, M_{0}\right) \| \Delta$ is $L_{1}$-live.

According to [33], the safeness and strictly $L_{1}$-liveness of $\left(N, M_{0}\right) \| \Delta$ imply that each transition in $\left(N, M_{0}\right) \| \Delta$ can be fired exactly once under initial marking $M_{0}$ or under a state $M$ reached from $M_{0}$. We let $M_{E}$ be a state of $\left(N, M_{0}\right) \| \Delta$ satisfying $M_{E}\left(p_{l e}\right)=1, \forall l \in\left\{1, \ldots, N_{t}\right\}$, and $M_{E}\left(u_{k}\right)=1$, $\forall k \in\left\{1, \ldots, N_{u}\right\}$. To reach $M_{E}$ from $M_{0}$, each transition in $\left(N, M_{0}\right) \| \Delta$ must be fired once all tasks can be performed.

Given an individual $\Delta=\{\lambda ; \mu\}$, after obtaining the corresponding solution $\boldsymbol{\theta}$ by algorithm BD , we let $t_{l h}$ be the transition in $\left(N, M_{0}\right) \| \Delta$, which corresponds to $j$-task, as described in Definition 1. Then, a transition sequence $\tau_{\Delta}=\left(\tau_{\Delta}[1], \ldots, \tau_{\Delta}\left[3 N_{t}\right]\right)$ is obtained by replacing each $j$-task in $\lambda$ with transition $t_{l h}$. For example, we consider
individual $\Delta=\{\lambda ; \mu\}$ in Fig. 2, and its corresponding transition sequence $\tau_{\Delta}=t_{21} t_{23} t_{11} t_{13} t_{12} t_{22}$. If $\tau_{\Delta}$ is feasible under $M_{0}$ (i.e., $M_{E}$ can be reached from $M_{0}$ through $\tau_{\Delta}$, which is denoted as $M_{0}\left[\tau_{\Delta}>M_{E}\right)$, then all underlying tasks can be finished through firing transitions in $\tau_{\Delta}$ sequentially, and the corresponding solution $\boldsymbol{\theta}$ is deadlock-free. Thus, the deadlock in $\Delta$ equivalents is detected to determine whether its corresponding transition sequence $\tau_{\Delta}$ is feasible under $M_{0}$.

Based on the abovementioned analysis, we develop PDAM to resolve the deadlock problem in an individual $\Delta=\{\lambda ; \mu\}$ based on the amender $\left(N, M_{0}\right) \| \Delta$.

## Algorithm: PDAM (PN-Based Deadlock Amending Method).

Input: an individual $\Delta=\{\lambda ; \mu\}$;
Output: a deadlock-free solution $\Delta^{*}$;
1: Generate PN amender $\left(N, M_{0}\right) \| \Delta$ based on $\Delta$;
2: Generate the transition sequence $\tau_{\Delta}$;
3: for $n=1$ to $3 N_{t}$
4: while $\left(\tau_{\Delta}[n]\right.$ is disabled under $\left.M_{n-1}\right)$
5: $\quad$ Remove $\tau_{\Delta}[n]$ to the end of $\tau_{\Delta}$;
6: $\quad$ Remove $\mu[n]$ to the end of $\mu$;
7: end
8: Let $M_{n-1}\left[\tau_{\Delta}[n]>M_{n}\right.$;
9: end
10: Let $\tau_{\Delta}{ }^{*}=\tau_{\Delta}$ and $\mu^{*}=\mu$;
11: Generate a task permutation $\lambda^{*}$ according to $\tau_{\Delta}{ }^{*}$;
12: Output $\Delta^{*}=\left(\lambda^{*} ; \mu^{*}\right)$;

Given an individual $\Delta$, PDAM first generates its amender $\left(N, M_{0}\right) \| \Delta$ and transition sequence $\tau_{\Delta}$, as shown in Lines $1-2$. Then, in the loop of Lines $4-7$, we detect whether $\tau_{\Delta}[n]$ is enabled under marking $M_{n-1}$ or not; if it is enabled, we fire it and generate a new marking $M_{n}$ (i.e., $M_{n-1}\left[\tau_{\Delta}[n]>M_{n}\right)$. Otherwise, $\tau_{\Delta}[n]$ (resp. $\mu[n]$ ) is moved to the end of $\tau_{\Delta}$ (resp. $\mu$ ), and the loop is continued until finding an enabled transition under $M_{n-1}$. When the iteration in Lines 3-9 ends, a transition sequence $\tau_{\Delta}{ }^{*}$ is generated such that $M_{0}\left[\tau_{\Delta}{ }^{*}>M_{E}\right.$, as well as a new permutation $\mu^{*}$. We can generate a task permutation $\lambda^{*}$ from $\tau_{\Delta}{ }^{*}$. Then, the new individual $\Delta^{*}=\left(\lambda^{*}, \mu^{*}\right)$ corresponds to a deadlock-free solution. The following result establishes the computational complexity of PDAM.

PROPOSITION 2 PDAM has polynomial time complexity and can obtain a deadlock-free task allocation solution.

Proof By Proposition 1, amender $\left(N, M_{0}\right) \| \Delta$ is strictly $L_{1}$-live, and each transition $t_{i h}$ can be fired exactly once under some marking $M_{h}$ before reaching $M_{E}$. This fact means that there is at least one enabled transition under $M_{h}$. Such an enabled transition is found through the iteration in PDAM. Finally, $M_{E}$ is reached, and a feasible transition sequence $\tau_{\Delta}{ }^{\prime}$ is obtained. Thus, the corresponding solution $\Delta^{\prime}$ generated from $\tau_{\Delta}{ }^{\prime}$ is deadlock-free.

![img-3.jpeg](img-3.jpeg)

Fig. 5. Processing of PDAM. (a) Initial marking $M_{0}$ in $\left(N, M_{0}\right) \| \Delta$. (b) $t_{21}$ is fired, $M_{0} \mid t_{21}>M_{1}$. (c) $t_{23}$ is disabled under marking $M_{1}$. (d) $t_{11}$ is fired, $M_{1} \mid t_{11}>M_{2}$. (e) $t_{13}$ is disabled under marking $M_{2}$. (f) Final marking $M_{E}$.

The entire method repeats $3 N_{t}$ times. In the $n$th iteration, at most $\left(3 N_{t}-n\right)$ transitions are checked. Thus, the complexity of the PDAM is $O\left(N_{t}^{2}\right)$, i.e., PDAM is polynomial.

EXAMPLE 3 The process of applying PDAM to the individual $\Delta=\{\lambda ; \mu\}$ in Fig. 2 is shown in Fig. 5. The corresponding $\tau_{\Delta}=t_{21} t_{23} t_{11} t_{13} t_{12} t_{22}$ and amender $\left(N, M_{0}\right) \| \Delta$ are shown in Fig. 5(a). Transition $t_{21}$, the first transition in $\tau_{\Delta}$, is enabled under $M_{0}$. After firing $t_{21}$ in $\left(N, M_{0}\right) \| \Delta$, a new marking $M_{1}$ is reached from $M_{0}$ (i.e., $M_{0}\left[t_{21}>M_{1}\right)$, as shown in Fig. 5(b). However, the second transition $\tau_{\Delta}[2]$ $=t_{23}$ is disabled under $M_{1}$, as shown in Fig. 5(c). Then, we move $t_{23}$ (resp. 2) to the end of $\tau_{\Delta}$ (resp. $\mu$ ), and a new transition sequence $\tau_{\Delta}{ }^{\prime}=t_{21} t_{11} t_{13} t_{12} t_{22} t_{23}$ and $\mu^{\prime}=$ $(1,1,1,2,1,2)$ are obtained. For the second transition $\tau_{\Delta}{ }^{\prime}[2]=t_{11}$, because it is enabled under $M_{1}$, we have $M_{1}\left[t_{11}>M_{2}\right.$, as shown in Fig. 5(d). Because $\tau_{\Delta}{ }^{\prime}[3]=t_{13}$ is disabled under $M_{2}$, we take a similar action and obtain $\tau_{\Delta}{ }^{\prime \prime}=t_{21} t_{11} t_{12} t_{22} t_{23} t_{13}$ and $\mu^{\prime \prime}=(1,1,2,1,2,1)$. After sequentially firing transitions $t_{12}, t_{22}, t_{23}$, and $t_{13}$ from $M_{2}$, the marking $M_{E}$ is reached (i.e., $M_{2}\left[t_{12} t_{22} t_{23} t_{13}>M_{E}\right)$, as shown in Fig. 5(e). Thus, $M_{E}$ can be reached from $M_{0}$ through $\tau_{\Delta}{ }^{\prime \prime}$, i.e., $M_{0}\left[\tau_{\Delta}{ }^{\prime \prime}>M_{E}\right.$. Based on $\tau_{\Delta}{ }^{\prime \prime}$ and $\mu^{\prime \prime}$, we
finally obtain a new deadlock-free individual $\Delta^{*}=\left\{\lambda^{*}\right.$; $\left.\mu^{*}\right\}$, where $\lambda^{*}=(6,3,4,7,8,5)$ and $\mu^{*}=(1,1,2$, $1,2,1)$.
3) Individual Amending Method: An individual amending method is shown in Algorithm IAD by synthesizing the above two amending algorithms.

```
Algorithm: IAD (Individual Amending Method).
    Input: an individual \(\Delta\);
    Output: a feasible individual \(\Delta^{\prime}\);
    while (8) or (9) is not met in \(\Delta\) or \(\Delta\) is
        deadlocked)
        Let \(\Delta\) be the input of Algorithm CD and \(\Delta_{1}\)
        be the result;
        Let \(\Delta_{1}\) be the input of PDAM and \(\Delta_{2}\) be the
        result;
        Let \(\Delta=\Delta_{2}\);
    end
    Let \(\Delta^{\prime}=\Delta\);
    Output feasible individual \(\Delta^{\prime}\);
```

In Algorithm IAD, after running Algorithm CD on $\Delta$, a new $\Delta_{1}$ meeting (8) and (9) is obtained. Then, the PDAM

is executed to obtain the deadlock-free individual $\Delta_{2}$. The resulting $\Delta_{2}$ may violate (9), and thus, a loop (Lines 1-5) is used. The output $\Delta^{\prime}$ satisfies all constraints and has no deadlocks.

## C. Computation of Objection Function

For a deadlock-free individual $\Delta=\{\lambda ; \mu\}$, we let $\boldsymbol{\theta}$ $=\left\{\theta_{k}, k \in U\right\}$ be the corresponding solution by Algorithm BD. Then, the parameters associated with any $j$-task, $j \in \theta_{k}$, can be calculated by the method described in this section.

First, we let $\chi(j) \in D$ be the preceding task of the $j$-task according to the task orders in $\theta_{k}$. If $j$-task is the first element of $\theta_{k}$, set $\chi(j)=0$; otherwise, $k$-UAV begins flying to the location of $j$-task immediately upon the completion of task $\chi(j)$. Thus, we have

$$
S_{j}= \begin{cases}0, & \text { if } \chi(j)=0 \\ C_{\chi(j)}, & \text { otherwise }\end{cases}
$$

The time that $k$-UAV arrives at the location of $j$-task can be calculated as follows:

$$
A_{j}= \begin{cases}S_{j}+\frac{\mu_{k, j}}{\nu_{k}}, & \text { if } \chi(j)=0 \\ S_{j}+\frac{\mu_{k+j}^{\prime}}{\nu_{k}}, & \text { otherwise }\end{cases}
$$

We let $\gamma(j)$ be the previous task of $j$ according to the temporal relation. Considering CMTAP in Example 1, tasks 3, 4 , and 5 represent the classification, attack, and verification tasks for the first target, respectively. We have $\gamma(4)=3$ and $\gamma(5)=4$. Tasks $\gamma(j)$ and $j$ are performed on the same target, but the latter begins only after the former is finished. Therefore, we have

$$
E_{j} \geq E_{\gamma(j)}+H_{\gamma(j)}
$$

where $H_{\gamma(j)}$ is the performing time of task $\gamma(j)$.
For $\Delta=\{\lambda ; \mu\}$, let $\omega(j) \in D$ be the preceding task of $j$-task in $\lambda$. If the $j$-task is the first element of $\lambda$, we set $\omega(j)$ $=0$. Considering $\lambda=(6,8,3,5,4,7)$ in Fig. 2, we have $\omega(8)$ $=6, \omega(3)=8$, and $\omega(6)=0$. We assume that the execution time of $j$-task is no less than $\omega(j)$-task, which is consistent with the firing rule of the corresponding transition sequence in a PN amender. Thus, we have

$$
E_{j} \geq E_{\omega(j)}
$$

It is clear that $E_{j} \geq A_{j}$. Based on the abovementioned inequalities, we can give the calculation formula of $E_{j}$, as shown in (19)

$$
E_{j}=\max \left\{A_{j}, E_{\gamma(j)}+H_{\gamma(j)}, E_{\omega(j)}\right\}
$$

The completion time $C_{j}$ of $j$-task is

$$
C_{j}=E_{j}+H_{j}
$$

For a deadlock-free individual $\Delta=\{\lambda ; \mu\}$, we can calculate $S_{j}, A_{j}, E_{j}$, and $C_{j}$ for each $j$-task in $\lambda$ sequentially using (15), (16), (19), and (20), respectively. We let the fitness of individual $\Delta$ be equal to the value of objective function (1), which is the sum of equivalent distances of all
tasks, is denoted by $F(\Delta)$, and can be computed by

$$
F(\Delta)=\sum_{u=1}^{3 N_{t}}\left(E_{\lambda[u]}-S_{\lambda[u]}\right) v_{|u| u]}
$$

## D. Probabilistic Model

The probabilistic model is an essential component of determining the performance of EDA that describes the distribution of superior individuals and captures the features that make them better than others.

We let $\Omega_{\text {all }}$ denote the population in EDA, which consists of $N_{p}$ individuals. Let $\Omega_{c}$ be the elite set containing the best $\left[N_{p} \times \delta\right]$ individuals, where $\delta$ is a proportion parameter and $\left[N_{p} \times \delta\right]$ indicates the maximum integer less than $N_{p} \times \delta$.

The voting procedure in [35] is used to construct the probability model from each elite individual $\Delta_{q}=\left\{\lambda_{q}\right.$; $\left.\mu_{q}\right\} \in \Omega_{c}$. Specifically, we construct a $3 N_{t}$-dimensional square $\Psi_{\lambda q}$ for $\lambda_{q}$ : for $i \in\left[1,3 N_{t}\right]$, set $\Psi_{\lambda q}\left(k-N_{u}, i\right)=$ 1 , where $k=\lambda_{q}[i]$, and other elements in $\Psi_{\lambda q}$ are set to zero. In this study, $\Psi_{\lambda q}(m, n)=1$ represents that $(m+$ $N_{u}$ )-task is in the $n$th position of $\lambda_{q}$. Similarly, another $N_{u}$ $\times 3 N_{t}$ matrix $\Psi_{\mu q}$ is established: for each $i \in\left[1, N_{u}\right]$, we set $\Psi_{\mu q}(k, i)=1$, where $k=\mu_{q}[i]$, and other elements in $\Psi_{\mu q}$ are zero. $\Psi_{\mu q}(m, n)=1$ represents that $m$-UAV is in the $n$th position of $\mu_{q}$.

Also, the dominance matrix $Q_{c}$ (resp. $Q_{\mu}$ ) can be calculated from $\Psi_{\lambda q}$ (resp. $\Psi_{\mu q}$ ) as follows:

$$
\begin{aligned}
Q_{c}(m, n)= & \sum_{\Delta q \in \Omega_{c}} \Psi_{\lambda_{q}}(m, n) \\
& \times\left(\exp \left(\frac{F\left(\Delta_{w}\right)-F\left(\Delta_{q}\right)}{F\left(\Delta_{w}\right)-F\left(\Delta_{b}\right)}\right)-1\right) \\
Q_{\mu}(m, n)= & \sum_{\Delta q \in \Omega_{c}} \Psi_{\mu_{q}}(m, n) \\
& \times\left(\exp \left(\frac{F\left(\Delta_{w}\right)-F\left(\Delta_{q}\right)}{F\left(\Delta_{w}\right)-F\left(\Delta_{b}\right)}\right)-1\right)
\end{aligned}
$$

where $\Delta_{w}$ (resp. $\Delta_{k}$ ) represents the worst (resp. best) individual, and the entry $Q_{c}(m, n)\left(\right.$ resp. $\left.Q_{\mu}(m, n)\right)$ denotes the weighted times that $\left(m+N_{u}\right)$-task (resp. $m$-UAV) appears at the $n$th position in $\lambda_{p}\left(\right.$ resp. $\left.\mu_{q}\right)$ of all elite individuals.

Example 6 We consider the CMTAP in Example 1. Given a population $\Omega_{\text {all }}=\left\{\Delta_{1}, \ldots, \Delta_{5}\right\}$ containing five individuals, their details are as follows:

$$
\begin{gathered}
\Delta_{1}=\left\{\lambda_{1} ; \mu_{1}\right\}=\{(6,7,8,3,4,5) ;(2,1,2,1,2,1)\} \\
F\left(\Delta_{1}\right)=187.89 \\
\Delta_{2}=\left\{\lambda_{2} ; \mu_{2}\right\}=\{(6,7,3,8,4,5) ;(1,2,2,1,2,1)\} \\
F\left(\Delta_{2}\right)=206.94 \\
\Delta_{3}=\left\{\lambda_{3} ; \mu_{3}\right\}=\{(8,6,5,3,4,7) ;(2,1,1,2,1,2)\} \\
F\left(\Delta_{3}\right)=212.77 \\
\Delta_{4}=\left\{\lambda_{4} ; \mu_{4}\right\}=\{(6,7,3,4,5,8) ;(2,1,2,2,1,1)\} \\
F\left(\Delta_{4}\right)=216.94
\end{gathered}
$$

$$
\begin{aligned}
\Delta_{5}= & \left\{\lambda_{5} ; \mu_{5}\right\}=\{(3,6,4,7,8,5) ;(2,1,1,2,2,1)\} \\
& F\left(\Delta_{5}\right)=228.67
\end{aligned}
$$

We assume that $\delta=0.4$; then, the elite set $\Omega_{\varepsilon}$ contains the 2 best individuals $\Delta_{1}$ and $\Delta_{2}$ (i.e., $\Omega_{\varepsilon}=\left\{\Delta_{1}, \Delta_{2}\right\}$ ). For $\Delta_{1} \in \Omega_{\varepsilon}$, because $\lambda_{1}[1]=6$ and $N_{u}=2$, we can obtain $\Psi_{\lambda 1}(4,1)=1 . \Psi_{\lambda 1}(5,2)=\Psi_{\lambda 1}(6,3)=\Psi_{\lambda 1}(1,4)=\Psi_{\lambda 1}(2$, $5)=\Psi_{\lambda 1}(3,6)=1$, and the other elements in $\Psi_{\lambda 1}$ are zero. Similarly, $\Psi_{\mu 1}$ can also be obtained

$$
\begin{aligned}
& \Psi_{\mu_{1}}=\left[\begin{array}{cccccc}
0 & 1 & 0 & 1 & 0 & 1 \\
0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0
\end{array}\right] \\
& \Psi_{\mu_{2}}=\left[\begin{array}{cccccc}
0 & 1 & 0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 & 1 & 0
\end{array}\right]
\end{aligned}
$$

$\Delta_{b}=\Delta_{1}$ and $\Delta_{w}=\Delta_{5}$, and we set all elements in $Q_{\lambda}$ and $Q_{\mu}$ to zero at first. We then consider individual $\Delta_{1}$. Because $\Psi_{\lambda 1}(4,1)=1$, its weight $\exp \left(\frac{F\left(\Delta_{1}\right)-F\left(\Delta_{1}\right)}{F\left(\Delta_{1}\right)-F\left(\Delta_{1}\right)}\right)-1$ $=1.72$. Thus, $\Delta_{1} \mathrm{~s}$ votes for $Q_{\lambda}(4,1)$ are 1.72 , and $Q_{\lambda}(4$, 1) increases accordingly. After all individuals in $\Omega_{\varepsilon}$ have voted, the final dominance matrices $Q_{\lambda}$ and $Q_{\mu}$ are described by follows:

$$
\begin{aligned}
Q_{\lambda} & =\left[\begin{array}{cccccc}
0 & 0 & 0.7 & 1.72 & 0 & 0 \\
0 & 0 & 0 & 0 & 2.42 & 0 \\
0 & 0 & 0 & 0 & 0 & 2.42 \\
2.44 & 0 & 0 & 0 & 0 & 0 \\
0 & 2.44 & 0 & 0 & 0 & 0 \\
0 & 0 & 1.72 & 0.7 & 0 & 0
\end{array}\right] \\
Q_{\mu} & =\left[\begin{array}{cccccc}
0.70 & 1.72 & 0 & 2.42 & 0 & 2.42 \\
1.72 & 0.70 & 2.42 & 0 & 2.42 & 0
\end{array}\right]
\end{aligned}
$$

## E. Offspring Reproduction and Replacement

This section extracts $\zeta$ individuals from the current population to construct a set of seeds $\Omega_{\text {new }}$ by the roulette method. Each offspring $\Delta=\{\lambda ; \mu\}$ is reproduced from each seed $\Delta_{n}=\left\{\lambda_{n} ; \mu_{n}\right\} \in \Omega_{\text {new }}$ as follows.

First, element $\lambda_{n}[l]$ is scheduled to the $l$ th position of $\lambda$ with a probability $p_{l}=\alpha \times \beta \times \exp \left\{\left(F\left(\Delta_{b}\right)-F\left(\Delta_{n}\right)\right)\right.$ $\left./\left(F\left(\Delta_{w}\right)-F\left(\Delta_{b}\right)\right)\right\}$, where $\alpha=1 /(e-1)$ is a constant, and parameter $\beta=\exp \left\{\left(F\left(\Delta_{b^{\prime}}\right)-F\left(\Delta_{b}\right)\right) / F\left(\Delta_{b^{\prime}}\right)\right\}$ is associated with the best individual $\Delta_{b^{\prime}}$ of the previous generation. Then, we let $\Lambda_{n}$ be the set of tasks that are not assigned to $\lambda$, thus far. For each unassigned $q$ th position in $\lambda$, we randomly select $j$-task $\in \Lambda_{n}$ with probability $p_{\lambda}=Q_{\lambda}\left(j-N_{u}\right.$, $\left.q) / \Sigma_{p \in \Delta} Q_{\lambda}\left(p-N_{u}, q\right)\right.$, where $Q_{\lambda}(m, n)$ is the $(m, n)$-entry of $Q_{\lambda}$. This process is repeated until $\Lambda_{n}=\varnothing$ and all elements in $\lambda$ have been assigned a task. Finally, for each $r$ th position in $\mu$, we randomly select $k$-UAV $\in U$ with probability $P_{\mu}=Q_{\mu}(k, r) / \Sigma_{p \in U} Q_{\mu}(p, r)$ and set $\mu[r]=k$. The obtained offspring $\Delta$ is amended with Algorithm IAD, and if this $\Delta$ is better than the worst $\zeta$ individuals of the current population and different from others, this offspring
is reserved. This replacement preserves superior genes and ensures the diversity of the population.

## F. Local Exploitation Method

This section proposes a dedicated local exploitation method to further improve the solution quality. We first define $r_{z}$ as the probability of performing local exploitation at the $z$ th iteration

$$
r_{z}= \begin{cases}0.01, & \text { when } R_{z} \leq 0.01 \\ R_{z}, & \text { when } 0.01<R_{z} \leq 1\end{cases}
$$

where $R_{z}=\exp (\beta / \alpha), \alpha=\frac{F_{z}-F_{z}-1}{F_{z}}$, and $\beta=\frac{F_{z-1}-F_{z}}{F_{z}}$. In this study, $F_{1}, F_{z}$, and $F_{z-1}$ represent the fitness values of the best individuals in the initial, current, and previous populations, respectively. If there is a better individual in the $z$ th generation population, $F_{z}<F_{z-1}$; otherwise, $F_{z}$ $=F_{z-1}$. Also, we obtain $F_{1} \geq \cdots \geq F_{z-1} \geq F_{z}$, and $\alpha$ is definitely negative. Thus, the smaller $\beta$ is, the more the algorithm needs to perform local exploitation, and therefore, the larger $R_{z}$ and probability indicator $r_{z}$ are. In addition, if $R_{z}$ is small, we set $r_{z}=0.01$ to strengthen the exploitation ability.

The introduction of $r_{z}$ can bring a reasonable balance between local exploitation ability and computational cost. When the algorithm fails to achieve a better solution, the dedicated local exploitation method is always called. The method is introduced in the following.

We start by selecting $\zeta$ individuals from the population $\Omega_{\text {all }}$ to create a set $\Omega_{a}$ by the roulette method. Three operations (swap, insert, and reorganization) are then performed on each individual $\Delta \in \Omega_{a}$ with probability $P_{\text {swap }}, P_{\text {insert }}$, and $P_{\text {reorg }}$, respectively. The supplemental file [39] details all operations.

Swap operation: For an individual $\Delta=\{\lambda ; \mu\} \in \Omega_{a}$, we choose two different $h$-task and $j$-task from $\lambda$ and then swap them. Because the results may be infeasible, we perform Algorithm IAD to ensure that the obtained individual is deadlock-free and satisfies constraints.

Insert operation: Given an individual $\Delta=\{\lambda ; \mu\} \in \Omega_{a}$, two different $h$-task and $j$-task are selected from $\lambda, h$-task is inserted into the position of $j$-task, while the elements after $j$-task in $\lambda$ are shifted backward. Algorithm IAD is also performed on the generated individual.

Reorganization operation: Given an individual $\Delta=$ $\{\lambda ; \mu\} \in \Omega_{a}$, we choose another individual $\Delta_{g}=\left\{\lambda_{g} ; \mu_{g}\right\}$ from $\Omega_{a}$. Then, individual $\Delta$ is reorganized by replacing $\mu$ with $\mu_{g}$ (i.e., $\Delta=\left\{\lambda ; \mu_{g}\right\}$ ). We also perform Algorithm IAD on it.

All individuals obtained by performing the above three operations are collected in $\Omega_{a}{ }^{\prime}$. The worst $\zeta$ individuals in $\Omega_{\text {all }}$ are replaced by the best $\zeta$ ones in $\Omega_{a} \cup \Omega_{a}{ }^{\prime}$.

## G. Overall DHEDA

By embedding PDAM and the local exploitation method into EDA, we obtain DHEDA, as detailed in the following.

Algorithm: DHEDA (Deadlock-Free Hybrid Estimation of Distribution Algorithm).

Input: Parameters $N, \delta, P_{\text {swap }}, P_{\text {insert }}, P_{\text {rearg }}, \zeta$, and the iteration number $T_{\text {max }}$.
Output: the optimal solution $\boldsymbol{\theta}$.
1: Generate initial population $\Omega_{\text {all }}$ with $N$ individuals and set $z=1$;
2: Perform Algorithm IAD on each individual in $\Omega_{\text {all }}$;
3: while $z<T_{\max }$
4: Obtain elite set $\Omega_{e} \subseteq \Omega_{\text {all }}$ based on fitness value with ratio $\delta$;
5: Obtain dominance matrices $Q_{k}$ and $Q_{\mu}$ according to $\Omega_{e}$;
6: Update the population $\Omega_{\text {all }}$ according to $Q_{k}$ and $Q_{\mu}$;
7: Compute the probability $r_{z}$ for the current $z$-th iteration;
8: if rand $(0,1)<r_{z} / /$ performing local exploitation
9: Obtain antibody set $\Omega_{a}$ with $\zeta$ individuals from $\Omega_{\text {all }}$ by the roulette method;
10: Perform Algorithm SO, IO, RO on each individual in $\Omega_{a}$. Let $\Omega_{a}{ }^{\prime}$ be the set of all obtained individuals;
11: The worst $\zeta$ individuals in $\Omega_{\text {all }}$ are replaced by the best $\zeta$ ones in $\Omega_{a} \cup \Omega_{a}{ }^{\prime}$;
12: end
13: $z=z+1$;
14: end
15: Let $\Delta_{\text {best }}$ be the optimal individual in $\Omega_{\text {all }}$, and generate a solution $\boldsymbol{\theta}$ from $\Delta_{\text {best }}$;
16: Output solution $\boldsymbol{\theta}$;

## H. Uncertainty Problem in CMTAP

The time-sensitive targets with time window constraints are unpredictable disturbances in the dynamic environment, and their appearance will make the original assignment infeasible. To solve this problem, we propose a match-up [36] based reassignment method, which consists of the following three steps: setting the reassignment horizon, performing the reassignment, and integrating the result into the original solution.

Assume that at time $\pi_{s}, N_{u}$ new targets are detected, each requiring three tasks described in Section II, and the tasks of the $i$ th target should be completed within $\left[\pi_{s}, \pi_{a}{ }^{i}\right]$. All these new tasks are denoted as $D_{u} \equiv\left\{3 N_{t}+N_{u}+1, \ldots\right.$, $\left.3 N_{t}+N_{u}+3 N_{u}\right\}$. Let the replanning time $\partial$ be a smaller value, and the reassignment horizon is $\left[\pi_{\text {start }}, \pi_{\text {end }}\right]$, where $\pi_{\text {start }}=\pi_{s}+\partial$ and $\pi_{\text {end }}=\max \left\{\pi_{a}{ }^{i} \mid i \in\left\{1, \ldots, N_{u}\right\}\right\}$. The assignment of tasks in $D_{u}$ within $\left[\pi_{\text {start }}, \pi_{\text {end }}\right]$ will affect some originally assigned tasks in the same horizon, denoted by $D_{o}=\left\{j \in D \mid E_{j} \in\left(\pi_{\text {start }}, \pi_{\text {end }}\right)\right\}$. Hence, tasks in $D_{v}=D_{o} \cup D_{u}$ need to be reassigned.

Before reassignment, we need to compute the "initial location" of each UAV as well as the maximal number of
tasks and flying distances that an UAV can perform within [ $\pi_{\text {start }}, \pi_{\text {end }}$ ]. Specifically, if $k$-UAV is performing $j$-task at $\pi_{\text {start }}$, it is available only after this task is completed, and its initial location is exactly $j$-task's point. Otherwise, since $v_{k}$ remains constant, $k$-UAV's location can be calculated based on the task points and the flight time before $\pi_{\text {start }}$, and then the remaining flying distance is updated accordingly. Moreover, $k$-UAV can perform up to $N^{k}$ tasks, where $N^{k}=$ $N_{\lim }^{k}-N_{s}{ }^{k}-N_{v}{ }^{k}$ and $N_{s}{ }^{k}$ (resp. $N_{v}{ }^{k}$ ) denotes the number of tasks assigned to $k$-UAV before $\pi_{\text {start }}$ (resp. after $\pi_{\text {end }}$ ).

Next, all tasks in $D_{v}$ are reassigned by DHEDA, in which individuals that do not satisfy time windows are regenerated. After time $\partial$ is passed, the optimal individual $\Delta^{r}$ is adopted, then each $k$-UAV can be assigned a corresponding task sequence $\theta_{k}{ }^{r}$. The original assignment of $k$-UAV after $\pi_{\text {end }}$ is retained and denoted by $\theta_{k}{ }^{e}$, so the reassignment task sequence $\theta_{k}{ }^{r}$ is

$$
\theta_{k}^{r}=\theta_{k}^{r} \oplus \theta_{k}^{e}
$$

where $\oplus$ means combining two sequences. Hence, the reassignment solution $\boldsymbol{\theta}^{r}=\left\{\theta_{k}{ }^{r} \mid k \in U\right\}$ is available.

Proposition 3 The obtained solution $\boldsymbol{\theta}^{r}$ according to (25) is deadlock-free.

Proof Let $\Delta$ be the original assignment's individual and its transition sequence is $\tau_{\Delta}$. We have $\tau_{\Delta}{ }^{e} \subseteq \tau_{\Delta}$ and $\Delta^{e}$ $\subseteq \Delta$, which correspond to the tasks after $\pi_{\text {end }}$ in the original assignment. For solution $\boldsymbol{\theta}^{r}$ with individual $\Delta^{r}$ $=\Delta^{v} \oplus \Delta^{e}$, we construct the amender $\left(N, M_{0}\right) \| \Delta^{r}$ by removing some transitions and places whose corresponding tasks do not exist in $\Delta^{r}$. According to $\Delta^{v}$, marking $M_{v}$ indicating that all tasks before $\pi_{\text {end }}$ are completed can be reached from $M_{0}$ through $\tau_{\Delta}{ }^{v}$ (i.e., $M_{0}\left[\tau_{\Delta}{ }^{v}>M_{v}\right)$. As the remaining transitions can be fired along $\tau_{\Delta}{ }^{e}, M_{E}$ is reached (i.e., $M_{v}\left[\tau_{\Delta}{ }^{e}>M_{E}\right)$. Since individual $\Delta^{r}$ whose transition sequence $\tau_{\Delta}{ }^{r}=\tau_{\Delta}{ }^{v} \oplus \tau_{\Delta}{ }^{e}$ satisfies $M_{0}\left[\tau_{\Delta}{ }^{r}>M_{E}, \boldsymbol{\theta}^{r}\right.$ is deadlock-free.

Fig. 6(a) shows the original assignment $\boldsymbol{\theta}=\left\{\theta_{1}, \theta_{2}\right\}$, where $\theta_{1}=<6,3,7,5>$ and $\theta_{2}=<4,8>$, task execution process is marked in blue. A time-sensitive target with time window $[3,27]$ is detected and the new tasks $D_{u}=\{9,10$, 11$\}$ is marked in red. Then, the disturbed tasks is $D_{o}=\{3$, $4,7\}$ and $D_{v}=D_{o} \cup D_{u}=\{3,4,7,9,10,11\}$. For 1-UAV, we get $\theta_{1}{ }^{v}=<7,9,10,11>$ after performing DHEDA, the original assignment after $\pi_{\text {end }}=27$ is $\theta_{1}{ }^{e}=<5>$, then $\theta_{1}{ }^{r}$ $=\theta_{1}{ }^{v} \oplus \theta_{1}{ }^{e}=<7,9,10,11,5>$. Similarly, we have $\theta_{2}{ }^{r}=$ $<3,4,8>$. Hence, the reassignment result $\boldsymbol{\theta}^{r}=\left\{\theta_{1}{ }^{r}, \theta_{2}{ }^{r}\right\}$ is obtained, as shown in Fig. 6(b).

## IV. COMPUTATIONAL EXPERIMENTS

Extensive computational experiments are conducted to describe the performance of the proposed DHEDA.

## A. Experimental Setup

For a more comprehensive evaluation, we perform all experiments based on the following three groups of testing instances: small, medium, and large. The number of UAVs,

![img-4.jpeg](img-4.jpeg)

Fig. 6. Gantt chart for task assignment. (a) Original assignment. (b) Reassignment result.

TABLE I
Parameter Size for Each Instance Type

| Instance <br> type | $u$ | $t$ | $a$ | $u \times t \times a$ |
| :--: | :--: | :--: | :--: | :--: |
| Small | 3, 4, 5 | 2, 3 | $(200,3),(400,4)$ | $3 \times 2 \times 2=12$ |
| Medium | $10,12,14$ | 10,12 | $(300,4),(500,5)$ | $3 \times 2 \times 2=12$ |
| Large | $30,40,50$ | 30,40 | $(400,5),(600,6)$ | $3 \times 2 \times 2=12$ |

the number of targets, and the ability limits $\left(L_{\text {lim }}{ }^{k}\right.$ and $\left.N_{\text {lim }}{ }^{k}\right)$ of $k$-UAV are represented by $u, t$, and $a$, respectively. Table I shows the size of parameters $u, t$, and $a$ for each instance type, and there are $3 \times(3 \times 2 \times 2)=36$ combinations. Each combination consists of ten different instances. The positions of UAVs and targets are randomly generated in the range $[1,100]$, and the $j$-task's performing time $H_{j}$ (resp. $k$-UAV's flying speed $v_{k}$ ) is randomly generated within [1, $3]$ (resp. $[4,6]$ ).

A comparison is performed with three existing algorithms, which are MTWPS [8], GA [28], and classical EDA (using PDAM to solve deadlocks but without the dedicated local exploitation method). Two graph-based deadlock amending methods, the novel digraph-based method (NDM) and TPG, are used in MTWPS and GA, respectively. These algorithms are measured by the relative percentage value (RPV)

$$
\mathrm{PV}=\left(\mathrm{FV}_{a}-\mathrm{FV}_{b}\right) / \mathrm{FV}_{b}
$$

where $\mathrm{FV}_{a}$ is the fitness of an algorithm for a test instance, and $\mathrm{FV}_{b}$ is the best fitness obtained by all algorithms for the same instance.

To reduce randomness, each algorithm is run 20 times independently, and then, the best RPV (bRPV) and average RPV (aRPV) are used as the performance metrics to evaluate each algorithm. The maximum number of iterations is

TABLE II
Deadlock Detection and Amending Results of PDAM

| Scale <br> $u \times t$ | Solution <br> amount | Deadlock <br> solution <br> amount | Success <br> rate | running <br> time | Single <br> solution <br> amending <br> time |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $[4 \times 2]$ | 250 | 139 | $100 \%$ | 0.04 | $3.13 \mathrm{e}-4$ |
|  | 500 | 299 | $100 \%$ | 0.07 | $2.34 \mathrm{e}-4$ |
|  | 1000 | 605 | $100 \%$ | 0.13 | $2.30 \mathrm{e}-4$ |
|  | 2000 | 1171 | $100 \%$ | 0.27 | $2.37 \mathrm{e}-4$ |
| $[12 \times 10]$ | 250 | 225 | $100 \%$ | 0.12 | $5.70 \mathrm{e}-4$ |
|  | 500 | 453 | $100 \%$ | 0.22 | $5.07 \mathrm{e}-4$ |
|  | 1000 | 882 | $100 \%$ | 0.37 | $4.30 \mathrm{e}-4$ |
|  | 2000 | 1770 | $100 \%$ | 0.90 | $5.13 \mathrm{e}-4$ |
| $[40 \times 30]$ | 250 | 224 | $100 \%$ | 0.32 | 0.0015 |
|  | 500 | 451 | $100 \%$ | 0.72 | 0.0016 |
|  | 1000 | 901 | $100 \%$ | 1.44 | 0.0016 |
|  | 2000 | 1830 | $100 \%$ | 2.82 | 0.0015 |
| $[200 \times 200]$ | 250 | 249 | $100 \%$ | 7.84 | 0.0315 |
|  | 500 | 500 | $100 \%$ | 28.08 | 0.0562 |
|  | 1000 | 999 | $100 \%$ | 43.15 | 0.0432 |
|  | 2000 | 1998 | $100 \%$ | 93.39 | 0.0467 |

set as $T_{\max }=2000$. All algorithms are coded in MATLAB 2021a and run on a PC with an Intel Core i9-9900K CPU @3.60 GHz and 32 GB of RAM in the 64-bit Windows 10 operating system.

## B. Deadlock Amending Verification

Two experiments are conducted to verify the progressiveness of PDAM on deadlock amending. First, we apply PDAM to the individual CMTAP of different scales and compare its performance with NDM and TPG methods. PDAM is established based on PNs, but NDM and TPG resolve deadlocks using the graph formed by CMTAP solutions.

Four combinations of $u \times t$ (i.e., $4 \times 2,12 \times 10,40 \times$ $30,200 \times 200$ ) are considered in the first experiment, and $250,500,1000,2000$ solutions are randomly generated for each combination. We perform PDAM on each individual and record the success rate as well as the running time. Table II shows that as the solution size grows, the probability of deadlock increases accordingly, which can be described by the ratio of deadlock solutions. For large-scale CMTAP, deadlocks arise in nearly all generated individuals. The success rate of PDAM in obtaining deadlock-free solutions is $100 \%$ for each instance type, and the running time increases marginally with the problem scale. Even for the solutions of CMTAP with the size $u \times t=200 \times 200$, PDAM can resolve deadlocks in less than 0.06 s . This result verifies that the computational complexity of PDAM is polynomial from the experimental viewpoint.

In the second experiment, PDAM is compared with NDM and TPG, and six combinations of $u \times t=4 \times 2$, $12 \times 10,40 \times 30,100 \times 100,200 \times 200$, and $400 \times 400$ are used. We randomly generate 500 individuals for each combination and run three methods on each of them 20 times independently.

TABLE III
Deadlock Detection and Amending Results of PDAM

| Scale$u \times t$ | Amount | Deadlock solution | PDAM |  | NDM |  | TPG |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  | Average success rate | Average amending time | Average success rate | Average amending time | Average success rate | Average amending time |
| $\{4 \times 2\}$ | 500 | 303 | $100 \%$ | 0.048 | $100 \%$ | 0.605 | $100 \%$ | 0.276 |
| $\{12 \times 10\}$ | 500 | 451 | $100 \%$ | 0.173 | $100 \%$ | 3.654 | $100 \%$ | 1.321 |
| $\{40 \times 30\}$ | 500 | 460 | $100 \%$ | 0.608 | $100 \%$ | 15.229 | $100 \%$ | 4.384 |
| $\{100 \times 100\}$ | 500 | 499 | $100 \%$ | 2.897 | $100 \%$ | 201.576 | $100 \%$ | 48.671 |
| $\{200 \times 200\}$ | 500 | 499 | $100 \%$ | 24.502 | $100 \%$ | 981.621 | $100 \%$ | 209.982 |
| $\{400 \times 400\}$ | 500 | 500 | $100 \%$ | 81.218 | $100 \%$ | 4599.698 | $100 \%$ | 468.798 |

![img-5.jpeg](img-5.jpeg)

Fig. 7. Variance plots of the amending time for PDAM, NDM, and TPG.

Table III shows that these three methods can successfully solve all deadlock solutions. However, from the perspective of running time, PDAM performs the best, followed by TPG, and the worst is NDM. Also, as shown in Fig. 7, PDAM has a negligible growth in amending time as the scale grows, while the other two methods exhibit a marked ascending trend. Importantly, PDAM performs well for large-scale CMTAP. For example, when applied to the solutions with $u \times t=400 \times 400$, the running time of PDAM is decreased by $98.23 \%$ ((4599.69-81.21)/4599.69) and $82.67 \%$ ((468.79-81.21)/468.79) compared with NDM and TPG, respectively.

## C. Parameter Calibration

Six relevant parameters ( $N, \delta, P_{\text {trans }}, P_{\text {shift }}, P_{\text {reorg }}$, and $\zeta$ ) in DHEDA are calibrated by the design of experiment (DOE) [37]. Unlike the traditional approach [38], we perform DOE in the following two steps: we first pick the appropriate factor levels for each parameter by experiments and then execute DOE to obtain the most suitable parameters for each CMTAP instance type. The aRPV is used as the performance metric.

We obtain candidate factor levels for a parameter as follows: ten values of the parameter are tested on a given instance, while all other parameters are fixed. Then, four

TABLE IV
Factor Levels for Each Parameter

| Factor level | $\boldsymbol{N}$ | $\boldsymbol{\delta}$ | $\boldsymbol{P}_{\text {trans }}$ | $\boldsymbol{P}_{\text {shift }}$ | $\boldsymbol{P}_{\text {reorg }}$ | $\boldsymbol{\zeta}$ |
| --: | --: | --: | --: | --: | --: | --: |
| $\mathbf{1}$ | 20 | 0.2 | 0.4 | 0.2 | 0.4 | 7 |
| $\mathbf{2}$ | 30 | 0.3 | 0.6 | 0.3 | 0.5 | 9 |
| $\mathbf{3}$ | 40 | 0.4 | 0.7 | 0.4 | 0.6 | 10 |
| $\mathbf{4}$ | 50 | 0.5 | 0.9 | 0.5 | 0.7 | 12 |

TABLE V
Orthogonal Array $L_{10}\left(4^{6}\right)$ and aRPV Results or Response Value

| Trial | Factor Level |  |  |  | Response Value $(\boldsymbol{a R P V})$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | N | $\delta$ | $P_{\text {trans }}$ | $P_{\text {shift }}$ | $P_{\text {reorg }}$ | $\zeta$ | Small | Medium | Large |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0.5192 | 0.2686 | 0.1966 |
| 2 | 1 | 2 | 2 | 2 | 2 | 1.0591 | 0.1545 | 0.2144 |  |
| 3 | 1 | 3 | 3 | 3 | 3 | 2.0027 | 0.2606 | 0.2632 |  |
| 4 | 1 | 4 | 4 | 4 | 4 | 1.3085 | 0.5509 | 0.5616 |  |
| 5 | 2 | 1 | 1 | 2 | 2 | 3 | 0.9472 | 0.2042 | 0.2369 |
| 6 | 2 | 2 | 2 | 1 | 1 | 4 | 0.1015 | 0.3776 | 0.2857 |
| 7 | 2 | 3 | 3 | 4 | 4 | 1 | 0.6963 | 0.4770 | 0.4409 |
| 8 | 2 | 4 | 4 | 3 | 3 | 2 | 0.2607 | 0.3989 | 0.3804 |
| 9 | 3 | 1 | 2 | 3 | 4 | 1 | 0.1416 | 0.4824 | 0.4203 |
| 10 | 3 | 2 | 1 | 4 | 3 | 2 | 0.1015 | 0.5731 | 0.4355 |
| 11 | 3 | 3 | 4 | 1 | 2 | 3 | 0.2704 | 0.2633 | 0.4948 |
| 12 | 3 | 4 | 3 | 2 | 1 | 4 | 0.0657 | 0.5679 | 0.5752 |
| 13 | 4 | 1 | 2 | 4 | 3 | 3 | 0.1140 | 0.2020 | 0.3678 |
| 14 | 4 | 2 | 1 | 3 | 4 | 4 | 0.3545 | 0.5131 | 0.5587 |
| 15 | 4 | 3 | 4 | 2 | 1 | 1 | 0.1647 | 0.5781 | 0.5820 |
| 16 | 4 | 4 | 3 | 1 | 2 | 2 | 0.0807 | 0.6055 | 0.5629 |

values that lead to the minimum aRPV are selected as the sought factor levels, and the results are shown in Table IV.

Based on the number of parameters and the factor levels of each parameter, the orthogonal array $L_{10}\left(4^{6}\right)$ is used. Because there are three CMTAP instance types, DOE is executed three times for instances with combinations $u \times$ $t \times a=\{3 \times 2 \times(200,3)\},\{10 \times 10 \times(300,4)\}$, and $\{30 \times 30 \times(400,5)\}$, respectively. Table V shows $L_{10}\left(4^{6}\right)$, which consists of 16 different combinations of parameter factor levels. For each combination, DHEDA is performed 10 times independently, and aRPV is used as the response value.

Table VI shows the statistical analysis of the aRPV results obtained in the test. The significance priority of

TABLE VI
Statistical Analysis and Suggested Parameter Values (SPV)

| Factor level |  | N | $\delta$ | $P_{\text {max }}$ | $P_{\text {min }}$ | $P_{\text {max }}$ | $\zeta$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 1.2224 | 0.4305 | 0.4806 | 0.2430 | 0.2128 | 0.3805 |
|  | 2 | 0.5064 | 0.4041 | 0.3541 | 0.5592 | 0.5894 | 0.3805 |
| Small | 3 | 0.1448 | 0.7835 | 0.7113 | 0.6949 | 0.6247 | 0.8336 |
|  | 4 | 0.1785 | 0.4339 | 0.5061 | 0.5551 | 0.6252 | 0.4576 |
|  | Delta | 1.0776 | 0.3794 | 0.3573 | 0.4519 | 0.4125 | 0.4531 |
|  | Rank | 1 | 5 | 6 | 3 | 4 | 2 |
|  | SPV | 40 | 0.3 | 0.6 | 0.2 | 0.4 | 7 |
| Medium | 1 | 0.3087 | 0.2893 | 0.3898 | 0.3788 | 0.4480 | 0.4515 |
|  | 2 | 0.3624 | 0.4046 | 0.3041 | 0.3762 | 0.3069 | 0.4310 |
|  | 3 | 0.4717 | 0.3948 | 0.4778 | 0.4117 | 0.3567 | 0.2325 |
|  | 4 | 0.4747 | 0.5288 | 0.4458 | 0.4508 | 0.5058 | 0.5024 |
|  | Delta | 0.1660 | 0.2395 | 0.1763 | 0.0746 | 0.1990 | 0.2698 |
|  | Rank | 5 | 2 | 4 | 6 | 3 | 1 |
|  | SPV | 20 | 0.2 | 0.6 | 0.3 | 0.5 | 10 |
| Large | 1 | 0.3090 | 0.3054 | 0.3569 | 0.3850 | 0.4099 | 0.4099 |
|  | 2 | 0.3360 | 0.3736 | 0.3221 | 0.4021 | 0.3773 | 0.3983 |
|  | 3 | 0.4815 | 0.4452 | 0.4606 | 0.4056 | 0.3617 | 0.3407 |
|  | 4 | 0.5178 | 0.5200 | 0.5047 | 0.4515 | 0.4954 | 0.4953 |
|  | Delta | 0.2089 | 0.2146 | 0.1827 | 0.0665 | 0.1337 | 0.1546 |
|  | Rank | 2 | 1 | 3 | 6 | 5 | 4 |
|  | SPV | 20 | 0.2 | 0.6 | 0.2 | 0.6 | 10 |

parameters for DHEDA is different for the three CMTAP instance types. Specifically, for small-type instances, $N$ is the most important parameter, $\zeta$ ranks second, $P_{\text {shift }}$ ranks third, $P_{\text {reorg }}$ ranks fourth, $\delta$ ranks fifth, and $P_{\text {trans }}$ ranks last. For medium-type instances, $\zeta$ is the most important parameter, followed by $\delta, P_{\text {reorg }}, P_{\text {trans }}, N$, and $P_{\text {shift }}$. For large-type instances, $\delta$ ranks first, followed by $N, P_{\text {trans }}, \zeta$, $P_{\text {reorg }}$, and $P_{\text {shift }}$. Thus, the parameter sets for the remaining experiments are selected as follows: $\left\{N, \delta, P_{\text {trans }}, P_{\text {shift }}\right.$, $\left.P_{\text {reorg }}\right\}=\{40,0.3,0.6,0.2,0.4,7\},\{20,0.2,0.6,0.3,0.5$, 10$\}$, and $\{20,0.2,0.6,0.2,0.6,10\}$ for small, medium, and large type instances, respectively.

## D. Comparison With Existing Algorithms

The proposed DHEDA is compared with MTWPS, GA, and EDA and the CMTAP instances described in Section IVA are used in the comparison.

The comparison results are shown in Table VII, where the performances of the four algorithms vary markedly in terms of aRPV, bRPV, and running time; the optimal values are bolded in black. Fig. 8 plots a set of comparison results and shows that DHEDA obtains the best bRPV and aRPV in nearly all instances, and only in a few cases does MTWPS perform the best.

Fig. 8(c) shows the running time of all algorithms. For small-type instances, deadlocks arise with a low probability, and the GA has the shortest running time due to its simplicity. For large-scale instances, the proportion of deadlock solutions increases, as shown in the experiments in Section IV-B; thus, if the graph-based TPG or NDM is used, it takes a lot of time to resolve deadlocks. Thus, GA (using TPG) and MTWPS (using NDM) take much more time than EDA and DHEDA, which use the proposed PDAM to amend deadlocks. Although DHEDA takes marginally more time than EDA, DHEDA always obtains a better solution because DHEDA uses a dedicated local exploitation method to improve the solution quality, but EDA does not. In general, adding a small additional time cost to achieve
![img-6.jpeg](img-6.jpeg)

Fig. 8. Plots for GA (use TPG), MTWPS (use NDM), EDA, DHEDA. (a) Variance plot of RPV. (b) Line chart of bRPV. (c) Variance plot of running time.
a better solution is worthwhile. Therefore, we conclude that DHEDA outperforms existing methods when solving CMTAP, particularly for large instances.

## E. Validation of the Reassignment Method

We verify the proposed match-up-based reassignment method by comparing it with the traditional approach of reassigning all tasks [40]. There are six types of instances with size $u \times t \in\{3 \times 2,5 \times 3,10 \times 10,14 \times 12,30 \times 30$, $50 \times 40\}$ and $a$ is $(400,4)$. For each instance type, after obtaining the solution by DHEDA, 10 reassignments are performed for a randomly generated time-sensitive target with a time window $\left[\pi_{s}, \pi_{d}\right]$ such that $\pi_{d}-\pi_{s} \in[20,25]$. The replanning time $\partial$ is set to one-third of $\pi_{d}-\pi_{s}$. We record the reassignment results of two methods.

Stability is another crucial factor to assess the reassignment results, because it indicates the time difference between the new assignment and the original one. We can denote the stability parameter as

$$
\operatorname{stability}\left(\theta^{\mathrm{re}}, \theta^{\mathrm{uti}}\right)=\frac{\sum_{j \in D^{\mathrm{ori}}}\left|E_{j}^{\mathrm{re}}-E_{j}^{\mathrm{ori}}\right|}{\left|D^{\mathrm{ori}}\right|}
$$

where $\boldsymbol{\theta}^{\text {ori }}$ and $\boldsymbol{\theta}^{\text {re }}$ are the original and new assignments, respectively, $D^{\text {ori }}$ is the original task set, $E_{j}^{\text {ori }}\left(\right.$ resp. $E_{j}^{\text {re }}$ ) is the $j$-task's execution time in the original (resp. new) assignments.

TABLE VII
Comparison Results of Different Algorithms

| Instance type | Scale |  | GA (see TPG) |  |  | MTWPS (see NDM) |  |  | EDA |  |  |  | DHEDA |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $\mu \mathrm{ct}$ | $\alpha$ | MPV | sBPV | Time | MPV | sBPV | Time | MPV | sBPV | Time | MPV | sBPV | Time |
| Small | (3, 2) | (290,3) | 0.3591 | 0.5768 | 151.83 | 0 | 0.1069 | 169.14 | 0 | 0.2675 | 163.85 | 0 | 0 | 170.99 |
|  | (3, 2) | (400,4) | 0.3591 | 0.4285 | 91.00 | 0 | 0.1692 | 110.41 | 0 | 0.3201 | 121.86 | 0 | 0 | 184.26 |
|  | (3, 3) | (200,3) | 0.0174 | 0.1714 | 181.35 | 0.0174 | 0.0737 | 200.75 | 0.0174 | 0.1437 | 193.32 | 0 | 0.0728 | 197.99 |
|  | (3, 3) | (400,4) | 0.1250 | 0.2107 | 126.67 | 0 | 0.1033 | 155.87 | 0.0902 | 0.1475 | 176.11 | 0 | 0.0665 | 202.59 |
|  | (4, 2) | (200,3) | 1.0912 | 1.5910 | 100.20 | 0.5025 | 1.4592 | 137.95 | 0.7683 | 1.9125 | 136.53 | 0 | 0.4359 | 148.86 |
|  | (4, 2) | (400,4) | 3.0912 | 4.6780 | 94.23 | 0 | 2.1643 | 111.977 | 0.3954 | 2.1863 | 150.48 | 0 | 0.2180 | 190.91 |
|  | (4, 3) | (200,3) | 0.5935 | 0.9660 | 121.47 | 0.1473 | 0.4065 | 152.75 | 0.5643 | 0.7742 | 143.75 | 0 | 0.3716 | 163.78 |
|  | (4, 3) | (400,4) | 0.6097 | 0.9301 | 127.37 | 0.3168 | 0.6167 | 166.38 | 0.3462 | 0.8053 | 190.44 | 0 | 0.4593 | 213.19 |
|  | (5, 2) | (200,3) | 1.8627 | 2.1357 | 103.52 | 0.5025 | 2.4044 | 131.92 | 1.2938 | 2.5410 | 130.70 | 0 | 0.7203 | 145.19 |
|  | (5, 2) | (400,4) | 7.1357 | 7.3389 | 96.58 | 0 | 1.8761 | 127.41 | 1.1669 | 3.0174 | 148.35 | 0 | 1.4738 | 183.55 |
|  | (5, 3) | (200,3) | 1.1165 | 1.4780 | 125.15 | 0.6328 | 1.3321 | 154.70 | 1.0874 | 1.4371 | 149.53 | 0 | 0.6012 | 162.73 |
|  | (5, 3) | (400,4) | 1.1476 | 1.4894 | 120.70 | 0.0702 | 0.4563 | 156.27 | 1.1311 | 1.4429 | 203.60 | 0 | 0.3525 | 226.23 |
| Medium | (10, 10) | (390,4) | 0.1969 | 0.5517 | 1430.37 | 0.1674 | 0.3191 | 2179.63 | 0.1828 | 0.4085 | 1498.45 | 0 | 0.0591 | 1562.93 |
|  | (10, 10) | (500,5) | 0.2930 | 0.7028 | 758.96 | 0.1099 | 0.2915 | 2206.2 | 0.2125 | 0.4843 | 797.22 | 0 | 0.0427 | 1148.1 |
|  | (10, 12) | (300,4) | 0.4143 | 0.7473 | 2230.79 | 0.2093 | 0.3021 | 2626.91 | 0.3463 | 0.6324 | 1768.45 | 0 | 0.1154 | 1837.65 |
|  | (10, 12) | (500,5) | 0.4907 | 0.7290 | 1197.81 | 0.1798 | 0.3852 | 2659.3 | 0.2814 | 0.4967 | 969.91 | 0 | 0.0889 | 1227.7 |
|  | (12, 10) | (300,4) | 0.3264 | 0.4020 | 1390.58 | 0.0095 | 0.3659 | 2141.73 | 0.1596 | 0.3668 | 1381.83 | 0 | 0.0920 | 1425.57 |
| Medium | (12, 10) | (500,5) | 0.3922 | 0.9872 | 763.68 | 0.3364 | 0.4973 | 2116.2 | 0.3909 | 0.6807 | 797.55 | 0 | 0.1184 | 1072.9 |
|  | (12, 12) | (300,4) | 0.5880 | 1.1841 | 2722.92 | 0.3062 | 0.4691 | 3573.29 | 0.3233 | 0.5256 | 2598.01 | 0 | 0.3633 | 2682.03 |
|  | (12, 12) | (500,5) | 0.4583 | 0.6198 | 1265.14 | 0.0168 | 0.1239 | 3412.8 | 0.1668 | 0.4099 | 1256.8 | 0 | 0.0326 | 1541.6 |
|  | (14, 10) | (300,4) | 0.3785 | 0.6293 | 1997.27 | 0.1214 | 0.3411 | 2832.07 | 0.2135 | 0.3712 | 1936.45 | 0 | 0.0615 | 2029.73 |
|  | (14, 10) | (500,5) | 0.7512 | 0.9404 | 1320.10 | 0.1162 | 0.1795 | 2773.0 | 0.4534 | 0.6804 | 1076.7 | 0 | 0.0520 | 1390.4 |
|  | (14, 12) | (300,4) | 0.4243 | 0.9984 | 2813.03 | 0.0573 | 0.1808 | 3468.75 | 0.1267 | 0.2436 | 2538.46 | 0 | 0.0764 | 2735.14 |
|  | (14, 12) | (500,5) | 0.4837 | 0.8966 | 1539.04 | 0.1501 | 0.2601 | 3286.0 | 0.4374 | 0.7523 | 1259.2 | 0 | 0.0993 | 1666.5 |
| Large | (30, 30) | (400,5) | 1.3910 | 1.5795 | 7177.31 | 0 | 0.1864 | 8704.87 | 0.5094 | 0.7868 | 3228.14 | 0.0367 | 0.1312 | 3576.97 |
|  | (30, 30) | (600,6) | 1.0486 | 1.4643 | 5235.3 | 0.0840 | 0.1466 | 7654.5 | 0.7378 | 1.0325 | 2753.6 | 0 | 0.0624 | 3210.7 |
|  | (30, 40) | (400,5) | 1.5048 | 1.6202 | 9181.38 | 0.1185 | 0.2102 | 12404.97 | 0.9573 | 1.3276 | 4215.67 | 0 | 0.1218 | 4721.52 |
|  | (30, 40) | (600,6) | 1.4984 | 1.5981 | 6030.4 | 0 | 0.1123 | 10693.1 | 1.0300 | 1.4891 | 3486.2 | 0.0423 | 0.0911 | 3867.6 |
|  | (40, 30) | (400,5) | 1.1429 | 1.3309 | 6158.57 | 0 | 0.1575 | 8401.13 | 0.5737 | 1.1524 | 3206.14 | 0.0557 | 0.1337 | 3815.59 |
|  | (40, 30) | (600,6) | 0.9217 | 1.3665 | 4975.6 | 0.0980 | 0.1704 | 7438.9 | 0.6496 | 0.8659 | 2747.5 | 0 | 0.0827 | 3077.8 |
|  | (40, 40) | (400,5) | 1.2260 | 1.5019 | 9173.62 | 0.2546 | 0.2921 | 11465.92 | 0.8634 | 1.0916 | 4484.36 | 0 | 0.1149 | 5034.21 |
|  | (40, 40) | (600,6) | 1.6546 | 1.9669 | 6067.8 | 0.2041 | 0.2280 | 9673.8 | 0.9340 | 1.6492 | 3448.5 | 0 | 0.0728 | 3985.3 |
|  | (50, 30) | (400,5) | 1.0182 | 1.5894 | 7767.95 | 0.1429 | 0.1808 | 8925.73 | 0.7618 | 1.0298 | 3051.64 | 0 | 0.0621 | 3714.02 |
|  | (50, 30) | (600,6) | 1.1646 | 1.2594 | 4618.1 | 0 | 0.1027 | 7049.4 | 0.6322 | 0.7750 | 2696.8 | 0.0328 | 0.1095 | 3135.1 |
|  | (50, 40) | (400,5) | 1.8405 | 1.9030 | 9119.69 | 0.1337 | 0.1912 | 10809.72 | 0.7559 | 1.0230 | 4436.70 | 0 | 0.0644 | 4964.68 |
|  | (50, 40) | (600,6) | 1.9751 | 2.1413 | 5806.1 | 0.1357 | 0.1892 | 9194.3 | 0.7499 | 1.0057 | 3365.4 | 0 | 0.0413 | 3875.6 |

![img-7.jpeg](img-7.jpeg)

Fig. 9. Comparison of reassignment results. (a) Average running time. (b) Average fitness value. (c) Average stability.

Fig. 9 shows the statistical results of three metrics, including the running time, fitness, and stability. Our method
takes significantly less time than traditional one in Fig. 9(a) and, thus, can better cope with dynamic environments. Despite the minimal running time, we still obtain deadlock-free solutions with the good performance [see Fig. 9(b)] because the match-up method reduces the number of reassigned tasks, shortens iteration process, and preserves part of the original optimal assignment. This also leads to better stability of our reassignments [see Fig. 9(c)], especially for the large-scale problems of size $u \times t \in\{30 \times 30,50 \times 40\}$, with an improvement of nearly $40 \%$.

## V. CONCLUSION

This study focuses on CMTAP with temporally coupled constraints for minimizing the total equivalent distance of all tasks. Based on the MILP model of CMTAP, we present a PN amender to resolve the arising deadlocks. This amender is constructed based on a candidate solution, and the corresponding deadlock-free solution is equivalent to a feasible transition sequence that can be fired sequentially in the amender. Then, based on these amenders, the PDAM with polynomial computational complexity is proposed to convert a deadlocked solution to a deadlock-free solution.

The resulting PDAM is effective and fast at solving deadlocks. Then, PDAM is embedded into EDA, creating a new algorithm called DHEDA, which can successfully solve the considered CMTAP. To further improve the solution quality, we establish a dedicated local exploitation method. An adaptive operational probability is explored to preserve the local exploitation ability without markedly increasing the computational burden. To deal with the time-sensitive tasks, a match-up-based reassignment method is proposed. Finally, extensive experiments are performed, and results show that:

1) for large-scale CMTAP, PDAM solves deadlocks in candidate solutions significantly faster than the existing graph-based methods;
2) the proposed DHEDA outperforms existing algorithms in [8] and [28] when solving CMTAP and obtains the best results with only a small additional time cost;
3) the match-up-based reassignment method achieves higher stability and efficiency than traditional method [40].
Extending PDAM to manage more realistic scenarios with simultaneous strikes is planned to be investigated in future work.

## REFERENCES

[1] J. Scherer, S. Yahyanejad, and S. Hayat, "An autonomous multi-UAV system for search and rescue," in Proc. 1st Workshop Micro Aerial Veh. Netw., Syst., Appl. Civilian Use, 2015, pp. 33-38.
[2] E. P. de Freitas, M. Basso, and A. A. S. da Silva, "A distributed task allocation protocol for cooperative multi-UAV search and rescue systems," in Proc. Int. Conf. Unmanned Aircr. Syst., 2021, pp. 909-917.
[3] S. Park and Y. Choi, "Applications of unmanned aerial vehicles in mining from exploration to reclamation: A review," Minerals, vol. 10, no. 8, p. 663, 2020, doi:10.3390/min10080663.
[4] H. Menouar, I. Guvenc, and K. Akkaya, "UAV-enabled intelligent transportation systems for the smart city: Applications and challenges," IEEE Commun. Mag., vol. 55, no. 3, pp. 22-28, Mar. 2017.
[5] M. Suresh and D. Ghose, "UAV grouping and coordination tactics for ground attack missions," IEEE Trans. Aerosp. Electron. Syst., vol. 48, no. 1, pp. 673-692, Jan. 2012.
[6] T. W. McLain and R. W. Beard, "Coordination variables, coordination functions, and cooperative timing missions," J. Guid., Control, Dyn., vol. 28, no. 1, pp. 150-161, 2005.
[7] Z. Zhen, D. Xing, and C. Gao, "Cooperative search-attack mission planning for multi-UAV based on intelligent self-organized algorithm," Aerosp. Sci. Technol., vol. 76, pp. 402-411, 2018.
[8] Y. Chen, D. Yang, and J. Yu, "Multi-UAV task assignment with parameter and time-sensitive uncertainties using modified two-part wolf pack search algorithm," IEEE Trans. Aerosp. Electron. Syst., vol. 54, no. 6, pp. 2853-2872, Dec. 2018.
[9] G. A. Korsah, A. Stentz, and M. B. Dias, "A comprehensive taxonomy for multi-robot task allocation," Int. J. Robot. Res., vol. 32, no. 12, pp. 1495-1512, 2013.
[10] C. Schumacher, P. Chandler, and M. Pachter, "UAV task assignment with timing constraints via mixed-integer linear programming," in Proc. AIAA 3rd Unmanned Unlimited Tech. Conf., Workshop Exhibit., 2004, p. 6410.
[11] L. Evers, A. I. Barros, and H. Monsuur, "Online stochastic UAV mission planning with time windows and time-sensitive targets," Eur. J. Oper. Res., vol. 238, no. 1, pp. 348-362, 2014.
[12] X. Zhao, Q. Zong, B. Tian, B. Zhang, and M. You, "Fast task allocation for heterogeneous unmanned aerial vehicles through reinforcement learning," Aerosp. Sci. Technol., vol. 92, pp. 588-594, 2019.
[13] J. S. McGrew, J. P. How, B. Williams, and N. Roy, "Air-combat strategy using approximate dynamic programming," J. Guid., Control, Dyn., vol. 33, no. 5, pp. 1641-1654, 2010.
[14] Z. Zhou et al., "When mobile crowd sensing meets UAV: Energyefficient task assignment and route planning," IEEE Trans. Commun., vol. 66, no. 11, pp. 5526-5538, Nov. 2018.
[15] Y. Eun and H. Bang, "Cooperative task assignment/path planning of multiple unmanned aerial vehicles using genetic algorithm," J. Aircr., vol. 46, no. 1, pp. 338-343, 2009.
[16] Z. Jia, J. Yu, X. Ai, X. Xu, and D. Yang, "Cooperative multiple task assignment problem with stochastic velocities and time windows for heterogeneous unmanned aerial vehicles using a genetic algorithm," Aerosp. Sci. Technol., vol. 76, pp. 112-125, 2018.
[17] F. Ye, J. Chen, Y. Tian, and T. Jiang, "Cooperative multiple task assignment of heterogeneous uavs using a modified genetic algorithm with multi-type-gene chromosome encoding strategy," J. Intell. Robot. Syst., vol. 100, no. 2, pp. 615-627, 2020.
[18] S. Fei, C. Yan, and S. Lin-Cheng, "UAV cooperative multitask assignment based on ant colony algorithm," Acta Aeronautica et Astronautica Sinica, vol. 29, no. 5, pp. 188-189, 2008.
[19] S. Gao, J. Wu, and J. Ai, "Multi-UAV reconnaissance task allocation for heterogeneous targets using grouping ant colony optimization algorithm," Soft Comput., vol. 25, no. 10, pp. 7155-7167, 2021.
[20] K. A. Ghamry, M. A. Kamel, and Y. Zhang, "Multiple UAVs in forest fire fighting mission using particle swarm optimization," in Proc. Int. Conf. Unmanned Aircr. Syst., 2017, pp. 1404-1409.
[21] V. Gonzalez, C. A. Monje, S. Garrido, L. Moreno, and C. Balaguer, "Coverage mission for UAVs using differential evolution and fast marching square methods," IEEE Aerosp. Electron. Syst. Mag., vol. 35, no. 2, pp. 18-29, Feb. 2020.
[22] X. Liang, H. Chen, and J. A. Lozano, "A Boltzmann-based estimation of distribution algorithm for a general resource scheduling model," IEEE Trans. Evol. Comput., vol. 19, no. 6, pp. 793-806, Dec. 2015.
[23] H. L. Choi, L. Brunet, and J. P. How, "Consensus-based decentralized auctions for robust task allocation," IEEE Trans. Robot., vol. 25, no. 4, pp. 912-926, Aug. 2009.
[24] W. Wu, N. Cui, W. Shan, and X. Wang, "Distributed task allocation for multiple heterogeneous UAVs based on consensus algorithm and online cooperative strategy," Aircr. Eng. Aerosp. Technol., Vol. 90, no. 9, pp. 1464-1473, 2018.
[25] K. S. Kim, H. Y. Kim, and H. L. Choi, "A bid-based grouping method for communication-efficient decentralized multi-UAV task allocation," Int. J. Aeronautical Space Sci., vol. 21, no. 1, pp. 290-302, 2020.
[26] Z. Jia, J. Yu, X. Ai, X. Xu, and D. Yang, "Cooperative multiple task assignment problem with stochastic velocities and time windows for heterogeneous unmanned aerial vehicles using a genetic algorithm," Aerosp. Sci. Technol., vol. 76, pp. 112-125, 2018.
[27] T. Lemaire, R. Alami, and S. Lacroix, "A distributed tasks allocation scheme in multi-UAV context," in Proc. IEEE Int. Conf. Robot. Autom., 2004, vol. 4, pp. 3622-3627.
[28] Q. Deng, J. Yu, and Y. Mei, "Deadlock-free consecutive task assignment of multiple heterogeneous unmanned aerial vehicles," J. Aircr., vol. 51, no. 2, pp. 596-605, 2014.
[29] G. Xu, T. Long, Z. Wang, and L. Liu, "Target-bundled genetic algorithm for multi-unmanned aerial vehicle cooperative task assignment considering precedence constraints," Proc. Inst. Mech. Engineers, Part G: J. Aerosp. Eng., vol. 234, no. 3, pp. 760-773, 2020.
[30] F. Ye, J. Chen, Y. Tian, and T. Jiang, "Cooperative task assignment of a heterogeneous multi-UAV system using an adaptive genetic algorithm," Electronics, vol. 9, no. 4, p. 687, 2020, doi: 10.3390/electronics 9040687 .

[31] W. Tian, L. Liu, Q. Wang, and H. Mu, "Cooperative multiple task assignment using cluster method and bidirectional particle swarm optimization," in Proc. IEEE 4th Adv. Inf. Manage., Communicates, Electron. Autom. Control Conf., vol. 4, 2021, pp. 797-802.
[32] C. Schumacher, P. Chandler, M. Pachter, and L. Pachter, "UAV task assignment with timing constraints," in Proc. AIAA Guid., Navigat., Control Conf. Exhibit, 2003, Art. no. 5664.
[33] T. Murata, "Petri nets: Properties, analysis and applications," Proc. IEEE, vol. 77, no. 4, pp. 541-580, Apr. 1989.
[34] M. Hauschild and M. Pelikan, "An introduction and survey of estimation of distribution algorithms," Swarm Evol. Comput., vol. 1, no. 3, pp. 111-128, 2011.
[35] Y. Zhang and X. Li, "Estimation of distribution algorithm for permutation flow shops with total flowtime minimization," Comput. Ind. Eng., vol. 60, no. 4, pp. 706-718, 2011.
[36] F. Qiao, Y. Ma, M. Zhou, and Q. Wu, "A novel rescheduling method for dynamic semiconductor manufacturing systems," IEEE Trans. Syst., Man, Cybern.: Syst., vol. 50, no. 5, pp. 1679-1689, May 2020.
[37] J. Antony, Design of Experiments for Engineers and Scientists. Amsterdam, The Netherlands: Elsevier, 2014.
[38] S. Kapsalis, P. Panagiotou, and K. Yakinthos, "CFD-aided optimization of a tactical blended-wing-body UAV platform using the Taguchi method," Aerosp. Sci. Technol., vol. 108, 2021, Art. no. 106395.
[39] [Online]. Available: https://github.com/ZhangRuiPeng94/TAES-2022-A-Deadlock-free
[40] Y. Wei, M. B. Blake, and G. R. Madey, "An operation-time simulation framework for UAV swarm configuration and mission planning," Procedia Comput. Sci., vol. 18, pp. 1949-1958, 2013.
![img-8.jpeg](img-8.jpeg)

Ruipeng Zhang received the B.S. degree in electrical engineering and automation in 2016 from Xi'an Jiaotong University, Xi'an, China, where he is currently working toward the Ph.D. degree in automation science and technology with the School of Automation Science and Engineering.

His research interests include UAV task assignment, decision making for intelligent systems, and satellite edge computing.
![img-9.jpeg](img-9.jpeg)

Yanxiang Feng received the B.S. and Ph.D. degrees in automation science and technology from Xi'an Jiaotong University, Xi'an, China, in 2010 and 2017, respectively.

He is currently an Associate Professor with the Systems Engineering Institute, School of Automation Science and Engineering, Faculty of Electronic and Information Engineering, Xi'an Jiaotong University. His research interests include Petri net, discrete-event systems, multiUAV task assignment, and robust control.
![img-10.jpeg](img-10.jpeg)

Yikang Yang received the B.S., M.S., and Ph.D. degrees in electronic engineering from Xi'an Jiaotong University, Xi'an, China, in 1996, 1999, and 2003, respectively.

He is currently a Professor with the School of Electronic and Information Engineering, Xi'an Jiaotong University. His research interests include satellite navigation, intersatellite link, spacecraft telemetry, tracking, and command (TT\&C), and signal processing.
![img-11.jpeg](img-11.jpeg)

Xiaoling Li received the B.S. degree in electronic science and technology and the Ph.D. degree in control science and engineering from Xi'an Jiaotong University, Xi'an, China, in 2012 and 2019, respectively.

She is currently an Assistant Professor with the School of Electronic and Control Engineering, Chang'an University, Xi'an, China. Her research interests include scheduling of flexible manufacturing systems and discrete event systems.