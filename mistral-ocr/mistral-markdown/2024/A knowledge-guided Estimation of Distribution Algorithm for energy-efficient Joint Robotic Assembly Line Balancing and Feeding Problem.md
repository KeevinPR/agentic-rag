# A knowledge-guided Estimation of Distribution Algorithm for energy-efficient Joint Robotic Assembly Line Balancing and Feeding Problem 

Chu-ge $\mathrm{Wu}^{*}$, Ruochen Zhang, Yuanqing Xia<br>School of Automation, Beijing Institute of Technology, Beijing, 100081, China

## A R TICLE INFO

Keywords:
Robotic assembly line balancing
Part feeding
Estimation of distribution algorithm
Production
Optimization

## A B STR A C T

The assembly line serves as a fundamental system in discrete production. To address the challenges in balancing robotic assembly lines, timely part feeding, and the need for sustainable manufacturing, this paper studies an energy-efficient Joint Robotic Assembly Line Balancing and Feeding Problem (JRALB-FP) with the criteria of minimizing both cycle time and total fuel consumption cost. Considering the complexity of the multi-problem and multi-objective optimization, a knowledge-guided Estimation of Distribution Algorithm (KEDA) is proposed to solve energy-efficient JRALB-FP. First, a probability model of EDA for task-workstation allocation paired with a heuristic method-based sampling mechanism is created. Using this probability model, a specific encoding mechanism is designed for part-trailer allocation, and good initial solutions are produced. Second, several properties of the bi-objective problem are analyzed to guide the design of local search operators for both objectives optimization. Third, the updating mechanism of the probability model is designed to learn from the elite solutions. Fourth, two knowledge-guided local search operators are designed and implemented to exploit better non-dominated solutions sufficiently. A design of experiment is carried out to determine the parameters. Extensive computational tests and comparisons with the state-of-the-art multi-objective algorithms are carried out, which verify the effectiveness of the knowledge-guided local search operators, the problem-oriented heuristic-based sampling mechanism, and the special designs of the KEDA in solving the energy-efficient JRALB-FP.

## 1. Introduction

The assembly line is a typical manufacturing system, as the floworiented assembly processes play a crucial role for producers across various discrete manufacturing industries [1], notably the automotive and electronic industries [2]. Recent years have seen an increment in the consumption of electronic products, such as smartphones, which has greatly amplified the demand for the high productivity of the corresponding assembly lines. In addition, in response to the climate change crisis, many countries have initiated low-carbon projects. Energy conservation and energy harvesting [3,4] have gained significant importance across various domains. Especially, it is important to implement energy-efficient manufacturing strategies as approximately onefifth of greenhouse gas emissions originate from the manufacturing industry [5].

To gain the efficiency of the assembly line, the Assembly Line Balancing Problem (ALBP) is of critical importance [6,7]. ALBP aims to effectively allocate assembly tasks with precedence constraints to workstations along the assembly line, which ensures the uninterrupted operation at each workstation and minimizes the cycle time [8]. The
use of industrial assembly robots is widespread in efforts to increase assembly line productivity. Considering this situation, the ALB problem is connected to a robot selection problem as Robotic ALBP [9,10], where each workstation is equipped with a single robot selected from a set of different robot types. A robotic two-sided assembly line balancing problem with setup times is provided in [11]. Furthermore, timely parts feeding is crucial for the assembly process, as optimal positioning of parts containers at workstations can reduce the considerable unproductive walking involved in fetching parts [12]. To reduce the impact of unproductive walking on assembly line efficiency and consume less space, the Assembly Line Feeding Problem (ALFP) addresses the selection of appropriate part storage, feeding, and transportation strategies [13].

Considering the decisive impact of both ALBP and ALFP on the performance of the assembly system in terms of time, costs, and ergonomics [14], and in alignment with the energy efficiency objective of green manufacturing, we propose a combined problem involving RALBP and ALFP called the Joint Robotic Assembly Line Balancing and Feeding Problem (JRALB-FP). Type-II ALBP is addressed, where

[^0]
[^0]:    * Corresponding author.

    E-mail address: wucg@bit.edu.cn (C.-g. Wu).

the cycle time is minimized under a fixed number of workstations. In addition, a set of in-house trailers can be enabled to fetch the parts for different assembly tasks from the supermarket. In this way, both the cycle time and fuel consumption associated with part transportation trailers are minimized to ensure efficient and effective production. The assignment of robots to workstations, tasks to workstations, and parts to trailers is considered simultaneously in this paper, to achieve a collaborative optimization solution for the part feeding and assembly line balancing problems.

Given the NP-hard nature of ALBP and ALFP, exact solving methods, construction heuristics, and evolutionary algorithms are widely employed to provide a solution within the given period. In the case of ALBP, an integer programming-based optimization approach [15] is utilized for the dynamic resource reconfiguration problem in automatic assembly lines, which is used to enable reconfigurable production, reduce costs, and promote sustainability in automatic assembly lines. Genetic Algorithms (GA) [16-18], and Simulated Annealing (SA) [19, 20] are extensively adopted to provide solutions for ALBP. A hybrid GA is presented in [16] on the assembly line balancing problem with collaborative robots. RALBP with a focus on sequence-dependent setup times and various assumptions regarding robot assignment is considered in [21], where a polynomial optimal algorithm is incorporated within a meta-heuristic framework to explore the space of giant sequences. Assembly line balancing problem involving human-robot collaboration and a diverse range of operators optimizing the cycle time is investigated in [17] and a customized GA is constructed for the problem. An improved hybrid GA is proposed in [18], incorporating penalty function adjustment and adaptive weighting mechanisms, which provide an optimization scheme for the allocation of multiposition tasks in a robot assembly line, aiming to enhance efficiency and optimize energy consumption. A neighborhood-search enhanced SA is conducted on the assembly line balancing problem with humanrobot collaboration in advanced manufacturing systems [19], featuring an adaptive selection mechanism for dynamic neighborhood search.

Furthermore, a list of works explores in-house part feeding and material feeding issues to guarantee the just-in-time part delivery and the assembly process efficiency. A comprehensive survey [22] categorizes related works on the ALFP based on feeding problem design, feeding policies, assembly line, and product characteristics, as well as optimization problem objectives and constraints. Line feeding policies such as line stocking, boxed supply, sequenced parts delivery, stationery kits, and travel kits are defined. The optimization objectives encompass cost considerations, ergonomic factors, transportation costs, shop floor costs, holding costs, and logistical handling costs. Based on ALFP, several works are proposed to study the joint assembly line balancing and feeding problem. The problem is formulated in [23], taking into account both line balancing and material supply to minimize production time while considering container space, supply area constraints, and cycle time constraints. An enhanced multi-Hoffmann heuristic method is embedded with a CPLEX solver. The total operational annual costs of the system are optimized in [14], while the assembly line, supermarket, and parts handling system are synchronized to the cycle time. Its proposed joint approach is compared with the hierarchical approach in terms of the number of assembly stations, number of parts fed with different policies, assembly station volume utilization, and total operational costs, and the results dominate those of the comparison strategies.

In addition to time performance, many other metrics, including energy efficient metrics, are considered. The energy consumption for executing material delivery tasks in the mix-model assembly lines is minimized in [24]. A Taboo enhanced Particle Swarm Optimization algorithm is developed to solve the multi-objective problem. The operational cost and workload imbalance are considered in [25], where the Pareto optimal solutions are generated via the augmented $c$-constrained method using CPLEX. The population-based evolutionary algorithms
are commonly employed to address the multi-objective joint line balancing and part feeding problem due to their inherent parallelism characteristics. Production cycle time and part consumption balance are minimized in [26], which builds a multi-objective mathematical model and utilizes a multi-objective GA to obtain the solutions. Flexsim software was used for simulation. The total energy consumption is considered in [27], as well as the number of workstations and supermarkets. A modified GA with mixed encoding and repair strategy is adopted to solve the joint problem. The total energy consumption of part feeding mobile robots is considered in [28]. A multi-objective disturbance and repair strategy enhanced cohort intelligence algorithm is established to deal with the multi-objective problem.

Considering the NP-hard nature of the considered problem, the evolutionary algorithm is adopted in this paper. Estimation of Distribution Algorithm (EDA) [29] is a data-driven swarm intelligence optimization algorithm, which has been widely adopted to solve complex optimization problems [30], especially scheduling problems [31-33]. An EDA-based hyper-heuristic approach is adopted by [32] to solve the distributed assembly mixed no-idle permutation flowshop scheduling problem. An EDA enhanced by the path relinking mechanism is proposed by [33] to minimize makespan in the directed acyclic graph task scheduling problem, integrating list scheduling heuristics and a probability model for improved performance compared to existing heuristics and evolutionary algorithms. A matrix-cube-based EDA is designed in [34] to solve the distributed assembly permutation flowshop scheduling problem. Branch-and-bound guided EDA is adopted to solve RALBP by [9,10], where the cycle time and total energy consumption are minimized.

Inspired by the effectiveness of EDA in solving complex multiobjective optimization problems, a knowledge-guided EDA (KEDA) is adopted to solve the energy-efficient JRALB-FP. The main contributions of our work can be summarized as follows:

- The fuel consumption cost is reasonably quantified. A Mixed Integer Programming (MIP) model is constructed to formalize the energy-efficient JRALB-FP, considering two objectives: cycle time and trailer fuel consumption, to find the trade-off between assembly efficiency and energy costs.
- Several properties of the energy-efficient JRALB-FP are provided. The correlation between these two objectives is analyzed, and the lower bound of different variables is presented, which guides the design of local search operators.
- To enhance the effectiveness of KEDA, we designed and incorporated a specific sampling mechanism and two knowledge-guided local search operators within the basic EDA. Experimental results validate the effectiveness of KEDA in solving this problem compared to other multi-objective algorithms.

The remaining contents are organized as follows. We define the multi-objective optimization problem and introduce and formulate the JRALB-FP in Section 2. The details of the knowledge-based EDA tailored for the proposed problem are explained in Section 3, where the encoding and decoding mechanism, initialization method, problem properties, and the details of the algorithm are provided. The numerical experimental results are provided in Section 4, and the paper is concluded in Section 5.

## 2. Energy-efficient joint robotic assembly line balancing and feeding problem

### 2.1. Basic concepts of multi-objective optimization problem

A multi-objective optimization problem generally involves more than one contradictory objective simultaneously and requires the identification of a desired trade-off between such objectives. The problem can usually be defined by (1).
$\min y=f(x)=\left(f_{1}(x), f_{2}(x), \ldots, f_{q}(x)\right)$

where $x \in R^{p}$ is a $p$-dimensional decision vector and $y \in R^{q}$ is the objective vector that contains $q$ individual objectives. In this paper, the non-dominated sorting method is adopted to compare and rank the solutions for optimization problems considering more than one objective. The essential knowledge of optimal Pareto solutions is provided below.

Pareto dominance: A solution $x_{1}$ is considered to dominate solution $x_{2}$ (denoted as $x_{1}>x_{2}$ ) if and only if:
$f_{i}\left(x_{1}\right) \leq f_{i}\left(x_{2}\right), \quad \forall i \in 1,2, \ldots, q$
$f_{i}\left(x_{1}\right)<f_{i}\left(x_{2}\right), \quad \exists i \in 1,2, \ldots, q$
Optimal Pareto solution: A solution $x$ is called an optimal Pareto solution if it is not dominated by any other solution.

Optimal Pareto set/Pareto Front: The solution set containing all optimal Pareto solutions is defined as the optimal Pareto set/Pareto Front. The optimal Pareto set obtained by a certain algorithm is defined as a non-dominated solution set/archive set $(A S)$. Besides, $C$ metric used to estimate multi-objective algorithms is introduced. $C M$ is used to compare the archive sets $A S_{1}$ and $A S_{2}$ which reflects the dominance relationship between the solutions in these two sets. $C$ metric is computed as (3).
$C\left(A S_{1}, A S_{2}\right)=\frac{\left|x_{1} \in A S_{1}\right| \exists x_{1} \in A S_{1}, x_{1}>x_{2} \text { or } x_{1}=x_{2} \mid}{\left|A S_{2}\right|}$
where $C\left(A S_{1}, A S_{2}\right)$ reflects the percentage of the solutions in $A S_{2}$ that are dominated by or are the same as the solutions in $A S_{1}$. In principle, $C\left(A S_{1}, A S_{2}\right)$ and $C\left(A S_{2}, A S_{1}\right)$ are both calculated to compare the Pareto dominance of the archive sets and its algorithm. The larger $C\left(A S_{1}, A S_{2}\right)$ and smaller $C\left(A S_{2}, A S_{1}\right)$ means $A S_{1}$ is better than $A S_{2}$ under the Pareto optimal metric.

Another indicator, Inversed Generation Distance (IGD) [35], is also widely used to compare archive sets. IGD estimates the distance from the obtained Pareto front to the true Pareto front. For each solution, the minimum Euclidean distance between the solution and the true Pareto front is calculated. A set of distances are calculated and the average value of them is IGD, which gives a measure of both diversity and convergence.

### 2.2. $J R A L B-F P$

### 2.2.1. Problem description

The JRALB-FP is a combination of the RALBP and ALFP. It is proposed to provide an optimal assignment for tasks and their parts to both workstations and in-house trailers, as well as an efficient assignment of manufacturing robots. This paper focus on a single-model assembly line with a one-sided straight layout as Fig. 1 shows. In addition, this paper considers Type-II assembly line balancing problem, aiming to minimize the cycle time given the number of workstations. Additionally, ALFP ensures that various parts are distributed to each workstation according to the assembly line's requirements. To achieve energy efficiency in part feeding, this paper introduces total fuel consumption of the enabled trailers as another objective.

The problem is depicted in Fig. 1, which includes the assembling of products, in-house part transportation, and part feeding. For product assembling, the assembly task is the smallest unit within the process, where the assembly process is divided into a set of tasks with precedence constraints. Workstations are the equipment used for assembling, which is located alongside the assembly line. The tasks are assigned to these workstations for their assembly in accordance with their precedence constraints. Heterogeneous manufacturing robots are allocated to the workstations for task assembling, resulting in varying processing times. Trailers are used to transport the required raw parts to specific workstations for task assembling. Containers are equipped for the workstations to store the required parts. Each trailer follows a fixed route, which starts from the supermarket where the parts are prepared, pauses at its responsible workstations to feed the parts, and then returns to the supermarket. Fig. 1 illustrates that the
![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of JRALB-FP.
trailer takes a fixed path time $\left(t t_{0}\right)$, loading and unloading time $\left(t u l_{i}\right)$, and starting and stopping time ( $t s s$ ) during the each transport. $t t_{0}$ represents the time needed to travel across a fixed single route, $t s s$ represents the time needed for the trailer to stop and start at each workstation, and $t u l_{i}$ represents the time taken for the loading and unloading of parts for task $i$. Cycle time is defined as the interval time between the assembly of two consecutive finished products, and it is affected by both the assembly time of tasks and the transportation time of parts in this paper. Fuel consumption cost is defined as the total fuel consumption cost for part transportation.

### 2.2.2. Problem formulation

To increase the efficiency of the assembly line and reduce overall energy consumption, it is important to optimize both the cycle time and the total fuel consumption cost. A shorter cycle time allows for the completion of more products within a given period, and a smaller fuel consumption helps to save energy. To formulate the problem, the notations are explained in Table 1, and the MIP model is provided in (4)-(15).
$\min \{c, f$ cost $\}$
subject to:
$\sum_{k=1}^{N_{W}} x_{i, k}=1, \quad \forall i \in \boldsymbol{T}$
$\sum_{r=1}^{N_{R}} y_{r, k}=1, \quad \forall k \in \boldsymbol{W}$
$\sum_{g=1}^{N_{D}} z_{i, g}=1, \quad \forall i \in \boldsymbol{T}$
$u_{g, k}=\max _{1 \leqslant i \leqslant N_{T}} x_{i, k} \cdot z_{i, g}, \quad \forall g \in \boldsymbol{G}, k \in \boldsymbol{W}$
$\sum_{k=1}^{N_{W}} k \cdot x_{i, k}-\sum_{k=1}^{N_{W}} k \cdot x_{j, k} \leqslant 0, \quad \forall i \in \boldsymbol{P}_{j}, j \in \boldsymbol{T}$
$\sum_{r=1}^{N_{T}} m_{i} \cdot x_{i, k} \leqslant c w, \quad \forall k \in \boldsymbol{W}$
$\sum_{r=1}^{N_{T}} m_{i} \cdot z_{i, g} \leqslant c t, \quad \forall g \in \boldsymbol{G}$
$z_{i, g} \leqslant z z_{g}, \quad \forall g \in \boldsymbol{G}, i \in \boldsymbol{T}$
$c \geqslant \max _{1 \leqslant k \leqslant N_{W}} \sum_{r=1}^{N_{T}} \sum_{r=1}^{N_{R}} t_{r, r} \cdot x_{i, k} \cdot y_{r, k}$
$c \geqslant \sum_{r=1}^{N_{T}} t u l_{i} \cdot z_{i, g}+\sum_{k=1}^{N_{W}} t s s \cdot u_{g, k}+t t_{0}, \quad \forall g \in \boldsymbol{G}$

Table 1
Symbol definitions.

| Notation | Explanation |
| :--: | :--: |
| Sets and the corresponding indices: |  |
| $T$ | The set of assembly tasks, where $T=\left\{i \mid x_{0}\right\}$ |
| $W$ | The set of workstations, where $W=\left\{k \mid x_{0}\right\}$ |
| $R$ | The set of robots, where $R=\left\{r \mid x_{0}\right\}$ |
| $G$ | The set of trailers, where $G=\left\{g \mid x_{0}\right\}$ |
| $P_{i}$ | The set of the predecessors of task $i$; |
| $S_{i}$ | The set of the successors of task $i$; |
| Decision variables: |  |
| $x_{i, k}$ | $x_{i, k} \in\{0,1\}$, if task $i$ is assigned to workstation $k, x_{i, k}=1$; otherwise, $x_{i, k}=0$; |
| $y_{i, k}$ | $y_{i, k} \in\{0,1\}$, if robot $r$ is assigned to workstation $k, y_{i, k}=1$; otherwise, $y_{i, k}=0$; |
| $z_{i, k}$ | $z_{i, k} \in\{0,1\}$, if the necessary parts of task $i$ are assigned to trailer $g, z_{i, k}=1$; otherwise, $z_{i, k}=0$; |
| $z z_{g}$ | $z z_{g} \in\{0,1\}$, if trailer $g$ is enabled, $z z_{g}=1$; otherwise, $z z_{g}=0$; |
| $u_{g, k}$ | $u_{g, k} \in\{0,1\}$, if trailer $g$ needs to unload parts at workstation $k, u_{g, k}=1$; otherwise, $u_{g, k}=0$; |
| Intermediate variables: |  |
| $c$ | Cycle time; |
| $n t$ | Number of the enabled trailers; |
| $f$ cost | Fuel consumption cost; |
| Problem parameters: |  |
| $m_{i}$ | The number of parts required for assembling task $i$; |
| $t_{i, i}$ | The duration time of task $i$ processed by the robot $r$; |
| $t u l_{i}$ | Loading and uploading time for the parts of task $i$; |
| $t t_{0}$ | The fixed path time; |
| $t s s$ | Starting and stopping time; |
| $c w$ | The capacity of the container of each workstation; |
| $c t$ | The capacity of each trailer; |
| $f_{0}$ | The fuel consumption of an unloaded trailer; |
| $f_{c}$ | The fuel consumption per unit weight of the trailer load per unit distance traveled; |
| $l w$ | The distance between the adjacent workstations; |

$f \operatorname{cost}=\sum_{g=1}^{N_{G}}\left(\max _{1 \leq k \in N_{W}} k \cdot u_{g, k} \cdot l w \cdot f_{c}+f_{0}\right) \cdot z z_{g}$
where the multi objectives of this paper are stated in (4), encompass the minimization of both the cycle time and total fuel cost. Constraint (5) indicates that each task must be assigned to a workstation once and only once, while constraint (6) indicates that the robot must be assigned to a workstation once and only once. Constraint (7) indicates for each task $i$, its parts must be assigned to a trailer for transportation once and only once. Constraint (8) shows the necessity for trailer $g$ to serve workstation $k$ is established, based on the allocation of necessary parts from workstation $k$ to trailer $g$. Constraint (9) ensures the precedence constraints between the tasks are satisfied, where each task's predecessors must be processed in the prior or the same workstations. Constraint (10) and (11) enforce the capacity constraints of the containers and trailers are satisfied correspondingly. Constraint (12) indicates that if parts are allocated to a trailer $g$, then the trailer is enabled. Two objectives are defined in Eqs. (13), (14), and (15). Constraint (13) defines that the cycle time is the maximum workstation time. Constraint (14) ensures the parts' traveling duration time is shorter than the cycle time, guaranteeing continuous part feeding for task assembling. Eq. (15) gives the calculation of the total fuel cost, encompassing both loaded and unloaded fuel consumption. The term for loaded fuel consumption is related to the last workstation the trailer visited.

### 2.3. Problem encoding and decoding

For the JRALB-FP, a solution contains four parts, i.e., the task assignment to workstations, the robot assignment to workstations, the

Table 2
Illustration of encoding mechanism.

|  | $k=1$ | $k=2$ | $k=3$ | $f_{c}$ | $f_{0}$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $g=1$ | 1,3,5 | 2 |  | 2 | 1 |
| $g=2$ |  | 6 | 4,7,8 |  |  |
|  | $r=1$ | $r=2$ | $r=3$ | $t u l_{i}$ | $m_{i}$ |
| $i=1$ | 1 | 2 | 4 | 1 | 1 |
| $i=2$ | 3 | 1 | 5 | 2 | 1 |
| $i=3$ | 1 | 2 | 6 | 2 | 1 |
| $i=4$ | 6 | 3 | 1 | 1 | 1 |
| $i=5$ | 1 | 2 | 4 | 1 | 1 |
| $i=6$ | 3 | 1 | 5 | 2 | 1 |
| $i=7$ | 4 | 5 | 1 | 1 | 1 |
| $i=8$ | 3 | 2 | 1 | 1 | 1 |

number of enabled trailers, and the part assignment to trailers of all tasks. In this paper, we adopt a heuristic approach to assign the robots to each workstation to ensure the shortest possible time to complete tasks according to the task to workstation assignment. Then, the following scheme is used to encode the solution. Let $\Pi$ denote the task assignment to workstations, $n t$ denote the number of enabled trailers, and $\Phi$ denote assignment of parts to trailers. To ensure the feasibility of a solution, the task assignment must satisfy the precedence constraints. A solution is encoded as:
$[\Pi, n t, \Phi]=\left[\pi^{1}, \pi^{2}, \ldots, \pi^{N_{W}} ; n t ; \phi^{1}, \phi^{2}, \ldots, \phi^{m}\right]$
An example with eight tasks, three workstations, two trailers is adopted to illustrate the encoding and decoding mechanism. Three types of robots, and the task processing periods are shown in Table 2. In accordance to the precedence constraints in Fig. 2, a feasible solution can be encoded as:
$[(1,3,5 ; 2,6 ; 4,7,8), 2,(1,2,3,5 ; 4,6,7,8)]$
Based on it, the fastest robot to complete the tasks within a certain workstation is allocated to the workstation following the assumption of [36]. Additionally, trailer 1 is responsible for workstation 1 and 2, trailer 2 is responsible for workstation 2 and 3 as Table 2 shows.

For decoding phase, let $k_{m}^{k}$ represent the last workstation for which trailer $g$ is responsible. Trailer 1 completes the delivery of all loaded parts after workstation 2 and becomes unloaded, trailer 2 completes the delivery of all loaded parts after workstation 3 and becomes unloaded, so we have $k_{m}^{k}=2$ and $k_{m}^{k}=3$. The fuel consumption of trailer 1 can be calculated as $2 \times l w \times f_{c}+f_{0}$, and for trailer 2 , it can be calculated as $3 \times l w \times f_{c}+f_{0}$. We use $w t_{k}$ to denote the workstation time, representing the completion time of the last task assigned to workstation $k$, and $t t_{g}$ to denote the transportation time of trailer $g$. In addition, to calculate the cycle time, for the transportation time, we have $t s s=1, t t_{0}=1, l w=1$, $c w=5, c t=5$, and then the transportation time of these two trailers can be achieved as: $t t_{1}=9$, and $t t_{2}=7$. For the workstation time, we have $w t_{1}=3, w t_{2}=2$, and $w t_{3}=3$. Thus, $c=9$ and $f \operatorname{cost}=12$ according to (13)-(15).

## 3. KEDA for JRALB-FP

### 3.1. Properties of JRALB-FP

In this section, several properties of the JRALB-FP are analyzed, which can guide the design of optimization operators of our proposed algorithm.

Property 1. Two objectives considered in this paper, namely $c$ and $f$ cost, are conflicting.

Proof. The cycle time of an assembly factory is influenced by both task assembling and part transporting, expressed as $c=\max \left(w t_{\max }, t t_{\max }\right)$,

![img-1.jpeg](img-1.jpeg)

Fig. 2. Illustration of the example and its decoding mechanism.
where $w t_{\max }=\max _{k} w t_{k}$, and $t t_{\max }=\max _{g} t t_{g}$. We define the set of enabled trailers as $|E T|$ and $E T=n t$, the set of tasks allocated to trailer $g$ as $T_{g}$, and the set of workstations served by the trailer $g$ as $W_{g}$. Then, $t t_{g}$ can be calculated as:
$t t_{g}=\sum_{i \in T_{g}} t u l_{i}+\sum_{k \in W_{g}} t s s+t t_{0} \cdot \forall g \in E T$
Based on (14), we have $c \geqslant \max T_{g}$. Considering a given schedule, let us focus on the trailer $g_{1}$ with the highest transportation time, denoted as $g_{1}=\operatorname{argmax}_{g \in E T} t t_{g}$. If we introduce another trailer $g^{\prime}$ into $E T$ and move one task from $T_{g}$ to trailer $g^{\prime}$, then the uploading time $\sum_{i \in T_{g_{1}}} t u l_{i}$ will decrease. Furthermore, the starting and stopping time $\sum_{k \in W_{g_{1}}} t s s$ will not increase. As a result, $t t_{g_{1}}$ will decrease, subsequently leading to a decrease in the lower bound of $c$. Enabling more trailers has the potential to reduce $c$.

On the contrary, the calculation of $f$ cost can be derived from (15), as shown in (18):
$f \operatorname{cost}=\sum_{g \in E T} \max _{k \in W_{g}} k \cdot l w \cdot f_{c}+f_{0} \cdot n t$
It can be seen from (18) that, enabling more trailers results in an increase in the unloading fuel consumption, represented by $f_{0} \cdot n t$. Meanwhile, it is difficult to decrease the first term of (18) by enabling more trailers. Therefore, it can be inferred that having more enabled trailers leads to a higher $f$ cost and a lower $c$, while having fewer enabled trailers reduces $f$ cost and may increase $c$. These two objectives are conflicting.

Property 2. When given the maximum workstation time ( $w t_{\max }$ ), the minimum number of enabled trailers ( $n t$ ) can be determined using (19) without extending the cycle time. The equation for determining the lower bound for $n t$ is:
$n t \geqslant \frac{\sum_{i=1}^{N_{T}} t u l_{i}}{w t_{\max }-t s s-t t_{0}}$
Proof. To ensure that the transportation time does not affect the cycle time $c$, it is necessary to maintain $t t_{\max } \leqslant w t_{\max }$. Additionally, the total transportation time $t t_{\text {total }}$ under a given $n t$ is determined by (20).
$t t_{\text {total }}=\sum_{i=1}^{N_{T}} t u l_{i}+\sum_{g=1}^{n t}\left|W_{g}\right| \cdot t s s+t t_{0} \cdot n t$
where $t t_{0}$ denotes the fixed path time for each trailer, $\sum_{i=1}^{N_{T}} t u l_{i}$ denotes the total uploading and loading time for the trailers to transport parts of $N_{T}$ tasks, and $t s s$ is the implicit starting and stopping time for serving workstations. Since each trailer serves at least one workstation, it holds that $\left|W_{g}\right| \geqslant 1$. The average transportation time $t t_{\text {avg }}$ under $n t$ trailers can be expressed at $t t_{\text {avg }}=t t_{\text {total }} / n t$. The lower bound for $t t_{\text {avg }}$ is given by (21) as follows:
$t t_{\text {avg }}=\frac{\sum_{i=1}^{N_{T}} t u l_{i}}{n t}+t s s+t t_{0}$
It is a known fact that $t t_{\max } \geqslant t t_{\text {avg }}$. Considering the assumption $t t_{\max } \leqslant w t_{\max }$, the conclusion can be drawn as shown in (19), which provides a reference for the number of necessary enabled trailers.

Property 3. To guarantee that all the parts of the tasks are transported to the workstation during the assembly cycle time, the lower bound of $n t$ can be calculated using (22).
$n t \geqslant\left\lceil\frac{\sum_{i=1}^{N_{T}} m_{i}}{c t}\right\rceil$
Proof. If all the parts are transported by the trailers on average, the number of trailers will be minimized and the lower bound is held.

Property 4. The upper bound of $n t$ is $N_{T}$. When $n t=N_{T}$, the transportation time $t t_{g}$ of each trailer $g$ can be calculated as (23):
$t t_{g}=t u l_{i} \cdot z_{i, g}+t s s+t t_{0}$
Proof. Since the parts of a particular task cannot be divided and transported by different trailers, the upper bound of $n t$ is $N_{T}$. Under this scenario, $t t_{\min }$ is achieved, which can be expressed as $\min _{i} t u l_{i}+t s s+t t_{0}$.

Property 5. For all enabled trailers $g_{c}$ if $\left|W_{g}\right| \geqslant 2$, the fuel cost $f$ cost can be reduced by transferring the parts prepared for $k_{2}$ from trailer $g$ to other trailers, provided that its transportation time does not exceed the current cycle time $c$, whereas $k_{2}$ satisfies:
$k_{2}=\underset{k \in W_{g}}{\arg \max } k, \quad$ and $\exists g^{*} \neq g, k_{2} \in W_{g}$.
Proof. Let $T(g, k)$ be the task set of tasks assigned to the workstation $k$ and their parts are transported by trailer $g$. Simultaneously, we have $g^{*} \neq g, k_{2} \in W_{g^{*}}$. If $t t_{g^{*}}+\sum_{i \in T(g, k_{2})} t u l_{i} \leqslant c$ holds, then inserting $T\left(g, k_{2}\right)$ into $T_{g^{*}}$. After the adjustment, the updated transportation time $t t^{\prime}$ and the updated fuel cost $f \cos t^{\prime}$ can be calculated as:
$T_{g^{\prime}}^{*}=T_{g^{*}} \cup T\left(g, k_{2}\right)$
$T_{g}^{\prime}=T_{g} \backslash T\left(g, k_{2}\right)$
$t t_{g^{*}}^{\prime}=t t_{g^{*}}+\sum_{i \in T\left(g, k_{2}\right)} t u l_{i} \leqslant c$
$t t_{g}^{\prime}=t t_{g}-\sum_{i \in T\left(g, k_{2}\right)} t u l_{i}<t t_{g} \leqslant c$
$f \cos t^{\prime}=f \cos t-\left(k_{2}-k_{1}\right) \cdot l w \cdot f_{c} \cdot k_{1}=\underset{k \in W_{g}^{*}}{\arg \max } k$
where it is clear that $k_{1}<k_{2}$, leading to $f \cos t^{\prime}<f \cos t$. This property enables us to develop an operator optimizing the assignment of parts to trailers based on the allocation of tasks to workstations.

### 3.2. The probability model, and its sampling and updating schemes

### 3.2.1. The probability model

In this paper, a probability model is adopted to generate taskworkstation allocations, wherein each value $p_{i, k}$ represents the probability of a particular task being allocated to a workstation. This

probability matrix is sized $N_{T} \times N_{W}$, where $N_{T}$ refers to the number of tasks, and $N_{W}$ to the number of workstations. Obviously, the sum of the elements in each row of the matrix is 1 . The probability model can be represented as (30), where $g$ represents the $g$ th iteration of evolution:
$P(g)=\left[\begin{array}{cccc}p_{1,1}(g) & p_{1,2}(g) & \ldots & p_{1, N_{W}}(g) \\ p_{2,1}(g) & p_{2,2}(g) & \ldots & p_{2, N_{W}}(g) \\ \vdots & \vdots & \ddots & \vdots \\ p_{N_{T}, 1}(g) & p_{N_{T}, 2}(g) & \ldots & p_{N_{T}, N_{W}}(g)\end{array}\right]$

### 3.2.2. Initialization and sampling

To initialize individuals with diversity, the probability model is initialized uniformly, i.e., $p_{i, k}(0)=\frac{1}{N_{W}}$. During the $g$ th iteration, task-to-workstation assignment: $\Pi$ is sampled based on $P(g)$. First, the number of tasks allocated to a certain workstation $k$ is estimated. Let $\widetilde{w}_{k}(g)$ represent the estimated number of tasks assigned to a specific workstation $k$ at the $g$ th iteration, which can be calculated according to the probability values within the probability model as follows:
$\widetilde{w}_{k}(g)=\left\{\begin{array}{l}\left\{\sum_{i} p_{i, k}(g)\right\}+1, \text { if } q \leq \sum_{i} p_{i, k}(g)-\left\{\sum_{i} p_{i, k}(g)\right\} \\ {\left\{\sum_{i} p_{i, k}(g)\right\}, \text { otherwise }\end{array}\right.$
where $q \in(0,1)$ is a random number. For example, the sum of the first column of the probability model is 3.4 , indicating that there is a 0.4 probability that 4 tasks will be allocated to the first workstation and a 0.6 probability of allocating 3 tasks. Additionally, the estimated number of tasks allocated to the last workstation is as follows:
$\widetilde{w}_{N_{W}}(g)=N_{T}-\sum_{k=1}^{N_{W}-1} \widetilde{w}_{k}(g)$
Second, task-to-workstation assignment, denoted as $\Pi$, is generated in accordance with $P(g)$ and $\widetilde{w}(g)$. A task is defined as available if all its predecessor tasks have already been allocated to workstations. An available task set $A T$ a is maintained and updated during the sampling of the probability model, where $A T:=\{i\}, P_{i} \in \mathcal{}^{+} ; i \notin \mathcal{}^{+}$, and $\mathcal{}^{+}$ represents the set of tasks that have been allocated. A tabu set $T a b u$ is used to collect the tasks violating capacity constraints during the phase of allocation. For each workstation $k$, a task $i$ is chosen from $A T$ based on a roulette-wheel method [37] with the probability array $p_{i, k}(g)$. If the assigned task $i$ exceeds the capacity of the workstation $k$, it will be pushed back to $A T$. The selection continues until a certain task is assigned to the workstation $k$, or all tasks in $A T$ are traversed. Finally, the fastest robot is assigned to each workstation.

Based on $\Pi$, the number of enabled trailers, denoted as $n t$, and the corresponding task-to-trailer allocation, denoted as $\Phi$, are generated. The minimum value of $n t$ is given by Property 3. To optimize trailer capacity utilization, the average load of each trailer is set to exceed $60 \%$ of its maximum capacity in this paper. Consequently, the permissible range of $n t$ is defined in Eq. (33), within which $n t$ is randomly selected.

$$
\frac{\sum_{i=1}^{N_{T}} m_{i}}{c t}\left\lvert\, \leqslant n t \leqslant\left\lvert\, \frac{\sum_{i=1}^{N_{T}} m_{i}}{0.6 \times c t}\right.\right.
$$

The next consideration is the part-to-trailer assignment, denoted as $\Phi$. To minimize both transportation time ( $t s s$ ) and energy consumption, each trailer should serve fewer workstations near one another following Property 5. To avoid disperse part feeding, the task-to-workstation allocation scheme is adopted to guide the part-to-trailer assignment. A load ratio (act) is generated randomly in the range of $60 \%$ to $100 \%$. For each newly enabled trailer $g$, its load limit can be calculated as $a c t \times c t$, then the parts are allocated to the trailer $g$ following the task sequence until the load limit is reached. If the capacity constraint is not satisfied, a new trailer is enabled and the remained parts are assigned to the new trailer. The pseudo-code can be referred to as Algorithm 1, where $w m_{g}$ is defined as the sum of the part quantities corresponding to the tasks that have been assigned to the $k$ th workstation, and $t m_{g}$
is defined as the sum of the part quantities corresponding to the tasks that have been assigned to the $g$ th trailer.

Thus, $\{\Pi, n t, \Phi\}$ is sampled based on the heuristic-oriented sampling mechanism as Algorithm 1 shows. To make the pseudo code clearer, some functions are defined as follows.

- Update $(X)$ : Update the set $X$.
- $x=\operatorname{Select}(Y, z)$ : Select task $x$ from set $Y$ based on the probability matrix $z$.
- Calculate $(x)$ : Calculate the value of $x$.
- Remove $(x, y)$ : Remove task $x$ from workstation $y$.
- Swap $(x, y)$ : Swap task $x$ and task $y$.
- Insert $(x, y)$ : Insert task $x$ to workstation $y$.
- Determine $(x)$ : Determine the value of $x$ based on the corresponding information.


## Algorithm 1: Sampling

Input: $P(g)$
Output: $(n d):\{\Pi, n t, \Phi\}$
Calculate $\widetilde{\boldsymbol{\Omega}}(\boldsymbol{g})=\left\{\widetilde{w}_{1}(g), \widetilde{w}_{2}(g), \ldots, \widetilde{w}_{N_{W}}(g)\right\}$ from ((31), (32))
for $k \in\left\{1, N_{W}\right\}$ do
$\omega_{k}(g)=0 ;$
while $\omega_{k}(g)<\widetilde{w}_{k}(g)$ do
Update $(A T)$;
Update $(T a b u)$;
$i=\operatorname{Select}(A T \backslash T a b u, P(g))$;
$\mathcal{+}$append $(i)$;
Assign the fastest robot $r$ to workstation $k$;
Calculate $\left(w t_{k}\right)$;
Update $\left(w m_{k}\right)$;
$\omega_{k}(g)+=1$;
end
end
$\Pi=\left\{\mathcal{+} ^ { 1 } \mathcal{+} ^ { 2 } \ldots \mathcal{+} ^ { k } \ldots\right\} ;$
Initialize $n t=1, g=1$, and $t m_{1}=0$;
for $\mathcal{+} \in \Pi$ do
for $i \in \mathcal{}^{k}$ do
if $t m_{g}+m_{i} \leqslant a c t \times c t$ then
$\phi^{k}$.append $(i)$;
Update $\left(t m_{g}\right)$;
end
else
$n t+=1 ;$
$g \rightarrow n e x t(g)$;
end
end
end
$\Phi=\left\{\phi^{1}, \phi^{2}, . ., \phi^{g}, . .\right\}$;
return $(n d)=\{\Pi, n t, \Phi\}$

### 3.2.3. Fitness calculation and probability matrix updating

After the population is initialized, each individual is evaluated according to (14) and (15). The corresponding pseudo-code is given in Algorithm 2. Then, the individuals are non-dominated sorted, and the first $N_{P} \times \beta$ individuals are chosen as the elite population, where $N_{P}$ denotes the size of the population and $\beta \in(0,1)$ denotes the ratio of the elite population. The probability values are updated with the elite population based on the incremental learning method [38]. Specifically,
$p_{i, k}(g+1)=(1-\alpha) \times p_{i, k}(g)+\alpha \times \Sigma_{g} I_{i, k}^{g}(g) /|Q|$
where $\alpha \in(0,1)$ represents the learning rate, $Q$ represents the elite population, whereas $|Q|=N_{P} \times \beta$ denotes the number of elite individuals,

and $I_{i, k}^{q}(g)$ is the indicator corresponding to the $q$ th elite individual.
$I_{i, k}^{q}(g)= \begin{cases}1, \text { Task } i \text { is assigned to workstation } k \\ \text { in indi } d \text { during the } g \text { th generation } \\ 0, \text { otherwise }\end{cases}$
### 3.3. Knowledge-guided local search operators

To enhance the exploitation capability, two local search operators are designed under the guidance of the problem properties, which are used to optimize the cycle time and fuel consumption cost respectively. Local search operations are performed in turn on each elite individual in each iteration. The pseudo-code of both local search operators are shown in Algorithm 3-6.

### 3.3.1. Local search operator for cycle time

As cycle time is influenced by both workstation time and transportation time, task-to-workstation and part-to-trailer both make sense.

## Algorithm 2: Evaluation

Input: indi
Output: fitness
for $k \in N_{W}$ do
Calculate $\left(w t_{k}\right)$;
end
for $g \in N_{G}$ do
Calculate $\left(t_{g}\right)$;
end
$c=\max \left(\max \left(t_{g}\right), \max \left(w t_{k}\right)\right)$;
Calculate(fcost);
Fitness transformation.
return fitness

## Algorithm 3: Local search for cycle time

Input: indi
Output: indi_optimized
Calculate $\left(w t_{\max }, t t_{\max }\right)$;
if $w t_{\max } \geqslant t t_{\max }$ then
Algorithm 4;
end
else
Algorithm 5;
end
return indi_optimized
First, if $w t_{\max }>t t_{\max }$, it indicates that the allocation of tasks to the workstation limits the cycle time. The workstation with $w t_{\max }$ is noted as the bottleneck workstation $W S B$, and we aim to insert the tasks in $W S B$ to other workstations. If there are no predecessors of task $i$ allocated in $W S B$, then it can be inserted into the previous workstation (WSP). If there are no successors of task $i$ in $W S B$, then it can be inserted into the next workstation ( $W S N$ ). If $w t_{\max }$ is reduced and the capacity constraints are satisfied, then the insertion operator is implemented.

In addition, swap operators are implemented to reduce $w t_{\max }$ as well. The tasks in $W S B$ are swapped to the previous or next workstations, if the precedence constraints and container capacity are satisfied and $w t_{\max }$ is reduced. The operators are illustrated in Fig. 3.

On the other hand, if the $w t_{\max }<t t_{\max }$, then transportation time is needed to be optimized. First, the trailer corresponding to the $t t_{\max }$ is identified, referred to as the bottleneck trailer $T B$. The first task $T B_{f}$ in the $T B$ is inserted into the previous trailer $T B P$ or the last task $T B_{l}$ in the $T B$ is inserted into the next trailer $T B N$ as the part inserted into adjacent trailers can minimize the impact on trailer fuel consumption. The operator is implemented if container capacity is satisfied and $t t_{\max }$ is reduced. The operators are illustrated in Fig. 4.

## Algorithm 4: Local search for workstation time

Input: indi
Output: indi_optimized
Calculate $\left(w t_{\max }\right)$;
for $i \in W S B$ do
Determine $\left(P_{i}\left(S_{i}\right)\right)$;
if $P_{i}\left(S_{i}\right) \notin W S B$ then
$\operatorname{Insert}\left(i, W S P(W S N)\right)$;
Calculate $\left(w t_{W S P}\left(w t_{W S N}\right), w m_{W S P}\left(w m_{W S N}\right)\right)$;
if $w t_{W S P}\left(w t_{W S N}\right)<w t_{\max }$ and $w m_{W S P}\left(w m_{W S N}\right) \leqslant c w$
then
Remove $(i, W S B)$;
end
else
Remove $(i, W S P(W S N))$
end
end
Update $(W S B)$;
Calculate $\left(w t_{\max }\right)$;
for $i \in W S B$ do
$\operatorname{Determine}\left(P_{i}\left(S_{i}\right)\right)$;
if $P_{i}\left(S_{i}\right) \notin W S B$ then
for $j \in W S P(W S N)$ do
$\operatorname{Determine}\left(S_{j}\left(P_{j}\right)\right)$;
if $S_{j}\left(P_{j}\right) \notin W S P(W S N)$ and $j \notin P_{i}\left(S_{i}\right)$ then
Swap $(i, j)$;
Calculate $\left(w t_{W S P}\left(w t_{W S N}\right), w t_{W S B}\right.$,
$\left.w m_{W S P}\left(w m_{W S N}\right), w m_{W S B}\right)$;
if $w t_{W S P}\left(w t_{W S N}\right)>w t_{\max }$ or $w t_{W S B}>w t_{\max }$ or
$\left.w m_{W S P}\left(w m_{W S N}\right)>c w\right.$ or $\left.w m_{W S B}>c w\right.$ then
$\operatorname{Swap}(i, j)$;
end
end
end
end
return indi_optimized
![img-2.jpeg](img-2.jpeg)

Fig. 3. Local search for workstation time.

### 3.3.2. Local search operator for fuel consumption cost

The fuel consumption of trailers is determined by the last workstation served, which can be lowered as Property 5. For each trailer

![img-3.jpeg](img-3.jpeg)

Fig. 4. Local search for trailer time.
$g$, the number of workstations it serves without violating the capacity constraints or raising $t t_{g}$. This strategy can effectively reduce trailer fuel consumption. The operators are depicted in Fig. 5. $k_{m}^{g}$ represent the last workstation for which trailer $g$ is responsible. According to the initial allocation in the figure, we have $k_{m}^{1}=2, k_{m}^{2}=3$. After transferring the materials of task 2 from trailer 1 to trailer 2, we have $k_{m}^{1}=1$, $k_{m}^{2}=3$. The load running distance of trailer 1 has been reduced, thereby reducing fuel consumption.

## Algorithm 5: Local search for trailer time

Input: indi
Output: indi_optimized
Calculate( $t_{T B P}, t_{T B N}$ );
Determine $\left(m_{f}\right.$ of $T B$ 's first task $T B_{f}$ );
Determine $\left(m_{l}\right.$ of $T B$ 's last task $\left.T B_{l}\right)$;
if $t_{T B P} \leqslant t_{T B N}$ then
if $t m_{T B P}+m_{f} \leqslant c t$ then
Insert(first task of $T B, T B P$ );
Calculate $\left(t_{T B P}\right)$;
if $t_{T B P} \leqslant t t_{m o}$, then
$\mid$ Remove $\left(T B_{f}, T B\right)$;
end
end
else
Remove $\left(T B_{f}, T B P\right)$
end
end
else
if $t m_{T B N}+m_{l} \leqslant c t$ then
Insert(last task in $T B, T B N)$;
Calculate $\left(t_{T B N}\right)$;
if $t_{T B N} \leqslant t t_{m o}$, then
$\mid$ Remove $\left(T B_{l}, T B\right)$;
end
end
else
Remove $\left(T B_{l}, T B N\right)$
end
end
return indi_optimized

### 3.4. Flowchart and complexity analysis

To solve the JRALB-FP with the criteria of minimizing both cycle time and fuel consumption cost, we develop a knowledge-guided EDA, where two knowledge-guided local search operators are embedded in the EDA. The flowchart of KEDA is shown in Fig. 6, and the main steps are concluded as follows.

- Step 1: Uniformly initialize the probability matrix. Set the Pareto set as an empty set. Then, for each evaluation generation $g$ :
- Step 2: Generate $N_{P}$ individuals by sampling the probability matrix through problem-oriented heuristic based methods.

Algorithm 6: Local search for fuel cost
Input: indi
Output: indi_optimized
for $g \in E T$ do
Calculate $\left(W_{g}\right)$;
if $W_{g} \geqslant 2$ then
Calculate $\left(k_{2}\right.$ of $\left.g\right)$;
if $3 g^{*} \neq g, k_{2} \in W_{g^{*}}$ then
if $t t_{g^{*}}+\sum_{i \in T(g, k_{2})} t u l_{i} \leqslant c$ then
if $t m_{g^{*}}+m_{i} \leqslant c t$ then
$\mid$ Insert $\left(i, T_{g^{*}}\right)$;
end
end
end
end
Update $\left(T_{g^{*}}, T_{g^{*}}, t t_{g^{*}}, t t_{g}\right)$;
Calculate $\left(f \cos ^{t}\right)$;
return indi_optimized
![img-4.jpeg](img-4.jpeg)

Fig. 5. Local search for fuel cost.

- Step 3: Calculate the values of cycle time and total fuel cost for each individual.
- Step 4: Perform non-dominated sorting for all individuals and select the first $\beta \times 100 \%$ individuals as the elite population.
- Step 5: Perform two local search operators in turn for each elite individual.
- Step 6: Update the Pareto set and the probability matrix with a learning rate of $\alpha$ based on the elite individuals.
- Step 7: If the stopping condition is met, output the Pareto set; otherwise, return to Step 2.

According to the flowchart, the time complexity of our proposed algorithm is analyzed as follows:

- Sampling: The sampling of the 'task-workstation' assignment has an $O\left(N_{T}{ }^{2}\right)$ complexity, and the sampling of the 'task-trailer' assignment has an $O\left(N_{T} \times N_{G}\right)$ complexity. It can be summarized that the complexity of the sampling mechanism is of $O\left(N_{T}{ }^{2}\right)$ as we have $N_{T}>N_{G}$;
- Fitness Calculation: For each individual, the fitness calculation has an $O\left(N_{W}+N_{G}\right)$ complexity. The total complexity for the population can be concluded as $O\left(\left(N_{W}+N_{G}\right) \times N_{P}\right)$ with the population size of $N_{P}$;
- Non-dominated sorting and elite solution selection: It is known that the complexity of non-dominated sorting is $O\left(N_{P}{ }^{2}\right)$, and the complexity of the elite individual selection is $O\left(N_{p}\right)$;
- Local search: For each elite individual, we have: (1) For the local search operator designed to optimize the cycle time, the complexity can be summarized as $O\left(N_{T}{ }^{2}\right)$; (2) For the local search

![img-5.jpeg](img-5.jpeg)

Fig. 6. Framework of KEDA.
operator designed to optimize the fuel cost, the complexity can be summarized as $O(2)$;

Thus, the complexity of the proposed algorithm is $O\left(\right.$ iter $\times\left(N_{T}{ }^{2}+\right.$ $\left.\left(N_{W}+N_{G}\right) \times N_{P}+N_{P}{ }^{2}+N_{P} \times \beta \times N_{T}{ }^{2}\right)$ ), where iter denotes the number of iteration, and $\beta \in(0,1)$ denotes the ratio of the elite population selected from the population. Considering $N_{P} \times \beta>1$, the total algorithm complexity is of the order $O\left(\right.$ iter $\left.\cdot N_{p} \cdot\left(N_{W}+N_{G}+N_{p}+\beta \cdot N_{T}^{2}\right)\right)$.

## 4. Numerical experimental results

### 4.1. Experimental settings

To verify the effectiveness of the KEDA in solving the energy efficient JRALB-FP, test cases adopted from https://assembly-line-balancing.de/ is used, where $N_{T}=\{20,50,70,83,100,148,220,297\}$. These data are used for cycle optimization of the basic assembly line scheduling problem. To verify the effectiveness of our multiobjective problem, the dataset has been improved by incorporating energy related data. The fuel costs of the trailers are added to the benchmark cases. On the other hand, different scales of workstation numbers are considered for each scale of tasks. For $N_{T}=20, N_{W}$ is set $\{4,5\} ; N_{T}=\{50,70,83\}, N_{W}$ is set $\{8,10\} ; N_{T}=\{100,148\}, N_{W}$ is set $\{10,12\}$, and for $N_{T}=\{220,297\}, N_{W}$ is set $\{10,15\}$. For each scale of $N_{T}, 10$ independent cases are adopted, and each case is run 10 times respectively. The computing environment is 13th Gen Intel(R) Core(TM) i7-13790F running at 2.10 GHz with 32 GB of RAM, and the operating system is Windows 11.

Four parameters are considered in our proposed algorithm: learning rate $(\alpha)$, the ratio of elite population $(\beta)$, the maximum number of iterations (iter), and the size of the population $\left(N_{P}\right)$. To determine the aforementioned parameters, the Taguchi method of the design-ofexperiment method (DOE) is used to investigate how the change of parameters affects the performance of the proposed algorithm. In this paper, $\alpha$ is chosen and set at these three levels: $0.05,0.1$, and $0.15 ; \beta$ is set at three levels: $5 \%, 10 \%$, and $15 \%$; iter is set at three levels: 60 , 80 , and $100 ; N_{P}$ is set at three levels: 60,80 , and $100.3^{4}$ full-factorial experiments are employed in a randomly chosen test case.

Table 3
The response value.

| $\alpha$ | $\beta$ | iter | $N_{P}$ | $C O N$ |
| :-- | :-- | :-- | --: | :-- |
| 0.05 | 0.05 | 60 | 60 | 0.042614 |
| 0.05 | 0.10 | 80 | 80 | 0.157440 |
| 0.05 | 0.15 | 100 | 100 | 0.038352 |
| 0.10 | 0.05 | 80 | 100 | 0.154126 |
| 0.10 | 0.10 | 100 | 60 | 0.161323 |
| 0.10 | 0.15 | 60 | 80 | 0.070887 |
| 0.15 | 0.05 | 100 | 80 | 0.184429 |
| 0.15 | 0.10 | 60 | 100 | 0.110471 |
| 0.15 | 0.15 | 80 | 60 | 0.080357 |

Table 4
Rank of KEDA parameters.

| Level | $\alpha$ | $\beta$ | iter | $N_{P}$ |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 0.07947 | 0.12706 | 0.07466 | 0.09476 |
| 2 | 0.12878 | 0.14308 | 0.13064 | 0.13759 |
| 3 | 0.12509 | 0.06320 | 0.12803 | 0.10098 |
| Delta | 0.04931 | 0.07988 | 0.05598 | 0.04282 |
| Rank | 3 | 1 | 2 | 4 |

For each instance, 9 combinations of are tested independently and the obtained $A S_{c i}(c i=1,2, \ldots, 9)$ are stored. The final $A S(F A S)$ are obtained by integrating $A S_{1}, A S_{2}, \ldots, A S_{9}$. Then, the contribution of a certain combination (CON) is counted as $\operatorname{CON}(c i)=\left|A S_{c i}^{t}\right| /|F E|$, where $A S_{c i}^{t}=\left\{X_{l} \in A S_{c i} \mid \exists X_{l^{\prime}} \in F A S, X_{l}=X_{l^{\prime}}\right\}$. The average $C O N$ of each combination is used as the response value (RV), and the RVs are shown in Table 3. The ranks of parameters are shown in Table 4, and the main effect plot is generated in Fig. 7. It can be seen that $N_{P}=80$, iter $=80, \alpha=0.1$, and $\beta=10 \%$ are suggested as the parameters in the simulation experiments, and the parameter settings are presented in Table 5.

### 4.2. Comparison to Gurobi

In this section, the proposed MIP model is solved using Gurobi (version 10.0.3) to validate its correctness. The results are compared with

![img-6.jpeg](img-6.jpeg)

Fig. 7. Main effect plot.

Table 5
Parameter settings.

| Parameter | Settings |
| :--: | :--: |
| $\sigma \sigma$ | 80 |
| $N_{P}$ | 80 |
| $n$ | 0.1 |
| $\beta$ | $10 \%$ |

Table 6
Comparison results of IGD, time, and $C$ metric between KEDA and gurobi.

| $N_{T}$ | No. | IGD |  | C. metric |  | Time(s) |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | KEDA | Gurobi | $C_{1, g}$ | $C_{2,5}$ | KEDA | Gurobi |
| 20 | 1 | 16.02 | 0.00 | 0.00 | 1.00 | 58.8 | 3168 |
|  | 2 | 73.19 | 0.00 | 0.00 | 1.00 | 58.3 | 1986 |
|  | 3 | 38.55 | 0.00 | 0.00 | 1.00 | 58.1 | 5400 |
|  | 4 | 31.08 | 0.00 | 0.00 | 1.00 | 58.6 | 2922 |
|  | 5 | 18.26 | 0.00 | 0.00 | 0.67 | 59.1 | 3756 |
| 50 | 1 | 230.89 | 0.00 | 0.00 | 1.00 | 195.7 | 5400 |
|  | 2 | 138.19 | 0.00 | 0.00 | 0.45 | 207.4 | 5400 |
|  | 3 | 175.56 | 0.00 | 0.00 | 1.00 | 196.0 | 5400 |
|  | 4 | 117.07 | 0.00 | 0.00 | 0.80 | 190.8 | 5400 |
|  | 5 | 139.60 | 15.22 | 0.33 | 0.67 | 204.5 | 5400 |
| 70 | 1 | 76.82 | 6.73 | 0.00 | 0.00 | 276.2 | 5400 |
|  | 2 | 0.86 | 0.00 | 0.00 | 0.00 | 278.2 | 5400 |
|  | 3 | 21.82 | 0.00 | 0.00 | 0.20 | 387.3 | 5400 |
|  | 4 | 4.10 | 35.01 | 0.50 | 0.00 | 279.7 | 5400 |
|  | 5 | 167.32 | 0.00 | 0.00 | 0.88 | 276.6 | 5400 |
| 83 | 1 | 85.00 | 641.72 | 0.67 | 0.00 | 393.0 | 5400 |
|  | 2 | 95.83 | 128.10 | 0.50 | 0.00 | 743.9 | 5400 |
|  | 3 | 108.16 | 641.90 | 0.50 | 0.20 | 740.0 | 5400 |
|  | 4 | 42.05 | 20.40 | 1.00 | 0.00 | 757.7 | 5400 |
|  | 5 | 7.67 | 260.90 | 0.50 | 1.00 | 747.8 | 5400 |
| 100 | 1 | 302.28 | 0.00 | 0.00 | 1.00 | 487.6 | 10800 |
| 148 | 1 | 93.89 | 0.00 | 0.00 | 0.73 | 1081.7 | 10800 |
| 220 | 1 | 0.00 | 17071.83 | 1.00 | 0.00 | 3106.5 | 10800 |
| 297 | 1 | 37.83 | 40844.31 | 1.00 | 0.00 | 4832.6 | 10800 |

those obtained from KEDA. Both $C$ metrics and IGD are calculated, and the CPU time are recorded and listed in Table 6, where C$($ KEDA, gurobi) and C(gurobi,KEDA) are denoted as $C_{k, g}$ and $C_{g, k}$ respectively for simplification.

For gurobi, we normalize the objectives and set three weights $\left(W_{o 1}, W_{o 2}\right)=[(0.2,0.8),(0.5,0.5),(0.8,0.2)],\left(W_{o 1}, W_{o 2}\right)$ represents the weights of the two objectives, respectively, and each weight is run once to obtain three solutions. For KEDA, run it independently ten times to obtain the Pareto front combinations. The actual Pareto front used is the combination obtained by all the algorithms used in the experiment.

It can be seen from Table 6 that, for the small scale instances ( $N_{T} \leqslant$ 70), KEDA are dominated by the Gurobi solutions. When $N_{T}=83$, the scale of decision variables increases, and our solutions dominate
![img-7.jpeg](img-7.jpeg)

Fig. 8. Boxplot of $C$ metric between KEDA and A1.
$50 \%-100 \%$ of Gurobi solutions produced within 5400 s time limit. In addition, for the larger scale instances ( $N_{T} \leqslant 70$ ), the time limit is extended to 10800 s to enhance the performance of Gurobi solutions. As a results, it can be seen that Gurobi solutions dominate most KEDA solutions in two random cases in the $N_{T}=100,148$ scales, while KEDA solutions dominate all Gurobi solutions in two random cases in the $N_{T}=220,297$ scales. It can be seen from IGD values that KEDA solutions are nearer to the Pareto front.

### 4.3. Effect of local intensification

To demonstrate the effectiveness of two knowledge-guided local search operators, we compare the KEDA to the algorithms without local search for cycle time (denoted as A1) and local search for fuel cost (denoted as A2) respectively. For each case, the average $C$ metric of ten independent runs is summarized in Tables 7 and 8. Additionally, the boxplots of the comparison between all $C$ metrics of KEDA and the other algorithm are shown in Figs. 8 and 9. The T-hypothesis test with a $95 \%$ confidence level is carried out, setting alternative hypothesis H 1 such that the $C$ metric achieved by KEDA is greater than the $C$ metric achieved by the other algorithms. If H 1 is implemented significantly ( $p<0.05$ ), then the flag is labeled as Y, otherwise it is labeled as N. C metric C(KEDA,A1) and C(A1,KEDA) are denoted as $C_{k, 1}$ and $C_{1, k}$ respectively for simplification in the tables. C(KEDA,A2) and C(A2,KEDA) are denoted as $C_{k, 2}$ and $C_{2, k}$.

From Table 7, it can be seen that C(KEDA, A1) is larger than C(A1, KEDA) on most instances. Especially, for the large-scale instances ( $N_{T} \geq 200$ ), the difference is statistically significant with $p<0.05$. Fig. 8 shows that KEDA is significantly better than A1. Therefore, the local search operator designed for cycle time optimization is effective in solving this problem. Similarly, it can be seen that C(KEDA, A2) is larger than C(A2, KEDA) on most instances from Table 8. Fig. 8 demonstrates that KEDA performs better than A2, confirming the effectiveness of the local search operator designed for fuel consumption cost optimization.

### 4.4. Effect of heuristic-based sampling mechanism

To demonstrate the effectiveness of the heuristic-based sampling mechanism, we compare it with the proposed EDA with a random sampling mechanism (denoted as A3), i.e., the assembly tasks and their parts are randomly assigned to the workstations and trailers. For each case, the average $C$ metric of ten independent runs is summarized in Table 9. Additionally, the boxplot of the comparison between all $C$ metrics of KEDA and A3 is shown in Fig. 10. The T-hypothesis test with a $95 \%$ confidence level is carried out, setting alternative hypothesis H 1 such that the $C$ metric achieved by KEDA is greater than the $C$ metric achieved by the EDA with a random sampling mechanism. If H 1 is implemented significantly ( $p<0.05$ ), then the flag is labeled as

Table 7
Comparison results of $C$ metric between KEDA and A1.

| $\left(N_{T}, N_{W}\right)$ | $(20,4)$ |  |  | $(50,8)$ |  |  | $(70,8)$ |  |  | $(83,8)$ |  |  | $(100,10)$ |  |  | $(148,10)$ |  |  | $(220,10)$ |  |  | $(297,10)$ |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| No. | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig |
| 1 | 0.50 | 0.33 | N | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.86 | 0.20 | Y | 0.86 | 0.18 | Y | 0.75 | 0.00 | Y | 1.00 | 0.00 | Y |
| 2 | 0.67 | 0.33 | Y | 0.75 | 0.20 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.86 | 0.13 | Y | 0.50 | 0.25 | N | 1.00 | 0.00 | Y |
| 3 | 1.00 | 0.67 | Y | 0.50 | 0.60 | N | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.86 | 0.00 | Y | 0.80 | 0.20 | Y | 0.80 | 0.14 | Y | 1.00 | 0.00 | Y |
| 4 | 0.67 | 0.00 | Y | 0.83 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.80 | 0.25 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 5 | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.80 | 0.16 | Y | 0.57 | 0.42 | N | 0.86 | 0.16 | Y | 1.00 | 0.00 | Y |
| 6 | 0.67 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.75 | 0.00 | Y | 0.88 | 0.13 | Y | 0.86 | 0.11 | Y | 1.00 | 0.14 | Y | 1.00 | 0.00 | Y |
| 7 | 0.50 | 1.00 | N | 0.88 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.14 | Y | 1.00 | 0.00 | Y | 0.67 | 0.00 | Y | 1.00 | 0.00 | Y |
| 8 | 1.00 | 0.00 | Y | 0.60 | 0.25 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.57 | 0.50 | N | 1.00 | 0.00 | Y | 0.80 | 0.20 | Y | 1.00 | 0.00 | Y |
| 9 | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.50 | 0.00 | Y | 0.75 | 0.25 | Y | 0.80 | 0.16 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 10 | 0.67 | 0.50 | N | 0.80 | 0.25 | Y | 1.00 | 0.00 | Y | 0.83 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| $\left(N_{T}, N_{W}\right)$ | $(20,5)$ |  |  | $(50,10)$ |  |  | $(70,10)$ |  |  | $(83,10)$ |  |  | $(100,12)$ |  |  | $(148,12)$ |  |  | $(220,15)$ |  |  | $(297,15)$ |  |  |
| No. | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig |
| 1 | 0.60 | 0.00 | Y | 0.88 | 0.11 | Y | 0.86 | 0.20 | Y | 0.75 | 0.25 | Y | 0.75 | 0.20 | Y | 0.70 | 0.27 | Y | 0.63 | 0.33 | Y | 1.00 | 0.00 | Y |
| 2 | 1.00 | 0.00 | Y | 0.71 | 0.18 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.80 | 0.13 | Y | 0.40 | 0.47 | N | 0.67 | 0.08 | N | 1.00 | 0.00 | Y |
| 3 | 0.67 | 0.25 | Y | 1.00 | 0.00 | Y | 0.83 | 0.00 | Y | 1.00 | 0.00 | Y | 0.88 | 0.09 | Y | 0.50 | 0.38 | N | 0.67 | 0.29 | Y | 0.83 | 0.00 | Y |
| 4 | 0.50 | 0.25 | N | 0.89 | 0.00 | Y | 0.88 | 0.00 | Y | 1.00 | 0.00 | Y | 0.89 | 0.20 | Y | 0.70 | 0.31 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 5 | 0.50 | 0.33 | Y | 1.00 | 0.00 | Y | 0.92 | 0.00 | Y | 0.80 | 0.00 | Y | 0.78 | 0.13 | Y | 0.46 | 0.55 | N | 0.60 | 0.38 | N | 1.00 | 0.00 | Y |
| 6 | 0.83 | 0.20 | Y | 0.71 | 0.00 | Y | 0.83 | 0.00 | Y | 0.75 | 0.00 | Y | 0.88 | 0.10 | Y | 0.92 | 0.13 | Y | 0.83 | 0.00 | Y | 1.00 | 0.00 | Y |
| 7 | 0.67 | 0.50 | N | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.80 | 0.00 | Y | 0.80 | 0.33 | Y | 0.25 | 0.60 | N | 0.86 | 0.00 | Y | 1.00 | 0.00 | Y |
| 8 | 1.00 | 0.00 | Y | 0.50 | 0.50 | N | 1.00 | 0.00 | Y | 0.83 | 0.00 | Y | 0.43 | 0.27 | N | 0.89 | 0.08 | Y | 0.86 | 0.20 | Y | 0.75 | 0.50 | N |
| 9 | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.83 | 0.25 | Y | 1.00 | 0.00 | Y | 0.71 | 0.17 | Y | 0.33 | 0.57 | N | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 10 | 1.00 | 0.00 | Y | 0.88 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.86 | 0.00 | Y | 0.40 | 0.33 | N | 0.71 | 0.25 | Y | 0.50 | 0.00 | Y |

Table 8
Comparison results of $C$ metric between KEDA and A2.

| $\left(N_{T}, N_{W}\right)$ | $(20,4)$ |  |  | $(50,8)$ |  |  | $(70,8)$ |  |  | $(83,8)$ |  |  | $(100,10)$ |  |  | $(148,10)$ |  |  | $(220,10)$ |  |  | $(297,10)$ |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| No. | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig |
| 1 | 0.00 | 0.67 | N | 0.56 | 0.44 | N | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.50 | 0.60 | N | 0.43 | 0.36 | N | 1.00 | 0.00 | Y | 1.00 | 0.33 | Y |
| 2 | 0.75 | 0.33 | Y | 0.78 | 0.00 | Y | 0.50 | 0.25 | Y | 0.75 | 0.25 | Y | 0.75 | 0.50 | Y | 0.50 | 0.62 | N | 0.40 | 0.50 | N | 0.50 | 0.33 | N |
| 3 | 1.00 | 0.00 | Y | 0.67 | 0.20 | Y | 0.75 | 0.00 | Y | 0.75 | 0.40 | Y | 0.33 | 0.50 | N | 1.00 | 0.00 | Y | 0.43 | 0.57 | N | 0.50 | 0.20 | Y |
| 4 | 0.00 | 0.50 | N | 0.50 | 0.71 | N | 0.33 | 0.75 | N | 1.00 | 0.00 | Y | 0.63 | 0.12 | Y | 0.75 | 0.37 | Y | 0.75 | 0.00 | Y | 1.00 | 0.00 | Y |
| 5 | 1.00 | 0.00 | Y | 0.33 | 0.60 | N | 0.33 | 0.00 | Y | 1.00 | 0.00 | Y | 0.73 | 0.16 | Y | 0.25 | 0.28 | N | 0.67 | 0.16 | Y | 0.50 | 0.00 | Y |
| 6 | 0.67 | 0.00 | Y | 0.57 | 0.29 | Y | 0.67 | 0.33 | N | 0.80 | 0.00 | Y | 0.67 | 0.50 | Y | 0.38 | 0.44 | N | 0.13 | 0.37 | N | 0.67 | 0.00 | Y |
| 7 | 0.67 | 0.50 | N | 0.80 | 0.17 | Y | 1.00 | 0.00 | Y | 0.25 | 0.29 | N | 0.58 | 0.42 | N | 0.55 | 0.22 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 8 | 1.00 | 0.25 | Y | 1.00 | 0.00 | Y | 1.00 | 0.25 | Y | 0.67 | 0.25 | Y | 0.43 | 0.33 | N | 0.38 | 0.16 | Y | 0.40 | 0.60 | N | 0.67 | 0.60 | N |
| 9 | 0.75 | 0.00 | Y | 0.50 | 0.33 | Y | 1.00 | 0.25 | Y | 0.60 | 0.00 | Y | 0.60 | 0.50 | N | 0.38 | 0.25 | N | 0.85 | 0.00 | Y | 1.00 | 0.00 | Y |
| 10 | 0.75 | 0.25 | Y | 1.00 | 0.00 | Y | 0.67 | 0.43 | Y | 0.50 | 0.57 | N | 0.57 | 0.40 | Y | 0.80 | 0.33 | Y | 0.75 | 0.25 | Y | 0.75 | 0.20 | Y |
| $\left(N_{T}, N_{W}\right)$ | $(20,5)$ |  |  | $(50,10)$ |  |  | $(70,10)$ |  |  | $(83,10)$ |  |  | $(100,12)$ |  |  | $(148,12)$ |  |  | $(220,15)$ |  |  | $(297,15)$ |  |  |
| No. | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig | $C_{\mathrm{L} 1}$ | $C_{\mathrm{L} 2}$ | Sig |
| 1 | 0.67 | 0.33 | Y | 0.33 | 0.33 | N | 0.38 | 0.40 | N | 1.00 | 0.25 | Y | 0.80 | 0.20 | Y | 0.73 | 0.08 | Y | 0.71 | 0.11 | Y | 0.17 | 0.60 | N |
| 2 | 1.00 | 0.00 | Y | 0.63 | 0.45 | N | 0.82 | 0.14 | Y | 0.43 | 0.33 | N | 0.90 | 0.13 | Y | 0.28 | 0.73 | N | 0.29 | 0.33 | N | 1.00 | 0.00 | Y |
| 3 | 0.60 | 0.25 | N | 0.63 | 0.44 | N | 0.67 | 0.20 | Y | 0.91 | 0.20 | Y | 0.50 | 0.27 | Y | 0.25 | 0.54 | N | 0.67 | 0.43 | Y | 1.00 | 0.00 | Y |
| 4 | 1.00 | 0.00 | Y | 0.63 | 0.40 | Y | 0.33 | 0.40 | N | 0.80 | 0.20 | Y | 0.91 | 0.00 | Y | 0.43 | 0.62 | N | 0.29 | 0.38 | N | 1.00 | 0.00 | Y |
| 5 | 1.00 | 0.00 | Y | 0.78 | 0.33 | Y | 0.50 | 0.37 | N | 0.60 | 0.60 | N | 0.43 | 0.63 | N | 0.82 | 0.00 | Y | 0.57 | 0.38 | Y | 1.00 | 0.00 | Y |
| 6 | 0.50 | 0.60 | N | 0.71 | 0.50 | Y | 0.70 | 0.33 | Y | 0.67 | 0.00 | Y | 0.50 | 0.60 | N | 0.30 | 0.47 | N | 0.43 | 0.29 | Y | 1.00 | 0.00 | Y |
| 7 | 1.00 | 0.00 | Y | 0.44 | 0.33 | N | 0.83 | 0.37 | Y | 0.67 | 0.33 | N | 0.75 | 0.00 | Y | 0.20 | 0.60 | N | 0.71 | 0.29 | Y | 1.00 | 0.00 | Y |
| 8 | 0.50 | 0.33 | Y | 0.85 | 0.16 | Y | 1.00 | 0.00 | Y | 0.80 | 0.33 | Y | 0.88 | 0.36 | Y | 0.27 | 0.38 | N | 0.83 | 0.20 | Y | 0.67 | 0.00 | Y |
| 9 | 0.83 | 0.00 | Y | 0.50 | 0.50 | N | 0.25 | 0.25 | N | 0.50 | 0.50 | N | 0.78 | 0.00 | Y | 0.18 | 0.64 | N | 0.83 | 0.13 | Y | 1.00 | 0.00 | Y |
| 10 | 0.50 | 0.25 | N | 0.25 | 0.40 | N | 0.80 | 0.00 | Y | 0.67 | 0.50 | Y | 0.88 | 0.00 | Y | 0.75 | 0.50 | Y | 0.60 | 0.13 | Y | 0.29 | 0.25 | N |

![img-8.jpeg](img-8.jpeg)

Y, otherwise it is labeled as N. C metrics: C(KEDA,A3) and C(A3,KEDA) are denoted as $C_{L, 3}$ and $C_{L, 6}$ respectively for simplification in the table.

From Table 9, it can be seen that $C_{L, 3}$ is larger than $C_{L, 6}$ in most instances. Fig. 10 shows that the heuristic sampling mechanism is significantly better than the random sampling mechanism in terms of the $C$ metric. The reason is that the problem-oriented heuristic-based sampling mechanism can locate the promising solution space efficiently and then produce better solutions.

### 4.5. Comparison to other algorithms

In this section, two commonly used multi-objective optimization algorithms: A Multi-objective Evolutionary Algorithm Based on Decomposition (MOEA/D) [39] and Non-dominated Sorting Genetic AlgorithmII (NSGA-II) [40], are adopted as the comparison algorithms to verify the effectiveness of KEDA in solving the energy efficient JRALB-FP. For

Table 9
Comparison results of $C$ metric between KEDA and A3.

| $\left(N_{T}, N_{W}\right)$ | $(20,4)$ |  |  | $(50,8)$ |  |  | $(70,8)$ |  |  | $(83,8)$ |  |  | $(100,10)$ |  |  | $(148,10)$ |  |  | $(220,10)$ |  |  | $(297,10)$ |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| No. | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig |
| 1 | 0.40 | 0.33 | N | 0.40 | 0.00 | Y | 0.18 | 0.00 | Y | 0.35 | 0.00 | Y | 0.28 | 0.00 | Y | 0.25 | 0.09 | Y | 0.33 | 0.00 | Y | 0.13 | 0.00 | Y |
| 2 | 0.83 | 0.33 | Y | 0.56 | 0.00 | Y | 0.27 | 0.00 | Y | 0.33 | 0.00 | Y | 0.27 | 0.00 | Y | 0.27 | 0.00 | Y | 0.22 | 0.00 | Y | 0.27 | 0.00 | Y |
| 3 | 0.25 | 0.67 | N | 0.40 | 0.00 | Y | 0.30 | 0.00 | Y | 0.41 | 0.00 | Y | 0.29 | 0.00 | Y | 0.17 | 0.00 | Y | 0.20 | 0.00 | Y | 0.30 | 0.00 | Y |
| 4 | 0.00 | 0.50 | N | 0.42 | 0.00 | Y | 0.29 | 0.00 | Y | 0.35 | 0.00 | Y | 0.25 | 0.00 | Y | 0.28 | 0.00 | Y | 0.12 | 0.00 | Y | 0.13 | 0.00 | Y |
| 5 | 0.67 | 0.00 | Y | 0.30 | 0.00 | Y | 0.46 | 0.00 | Y | 0.25 | 0.00 | Y | 0.47 | 0.00 | Y | 0.24 | 0.00 | Y | 0.29 | 0.00 | Y | 0.25 | 0.00 | Y |
| 6 | 0.33 | 0.00 | Y | 0.50 | 0.00 | Y | 0.38 | 0.00 | Y | 0.33 | 0.00 | Y | 0.29 | 0.00 | Y | 0.26 | 0.00 | Y | 0.08 | 0.00 | Y | 0.00 | 0.00 | N |
| 7 | 0.57 | 0.25 | Y | 0.40 | 0.00 | Y | 0.17 | 0.00 | Y | 0.23 | 0.00 | Y | 0.20 | 0.00 | Y | 0.25 | 0.00 | Y | 0.19 | 0.00 | Y | 0.13 | 0.00 | Y |
| 8 | 0.40 | 0.50 | N | 0.33 | 0.13 | Y | 0.40 | 0.00 | Y | 0.31 | 0.00 | Y | 0.30 | 0.00 | Y | 0.21 | 0.00 | Y | 0.21 | 0.00 | Y | 0.30 | 0.00 | Y |
| 9 | 0.80 | 0.00 | Y | 0.47 | 0.00 | Y | 0.23 | 0.00 | Y | 0.20 | 0.00 | Y | 0.25 | 0.00 | Y | 0.30 | 0.00 | Y | 0.23 | 0.00 | Y | 0.08 | 0.00 | Y |
| 10 | 0.80 | 0.00 | Y | 0.43 | 0.00 | Y | 0.53 | 0.00 | Y | 0.42 | 0.00 | Y | 0.40 | 0.00 | Y | 0.07 | 0.00 | Y | 0.14 | 0.00 | Y | 0.00 | 0.00 | N |
| $\left(N_{T}, N_{W}\right)$ | $(20,5)$ |  |  | $(50,10)$ |  |  | $(70,10)$ |  |  | $(83,10)$ |  |  | $(100,12)$ |  |  | $(148,12)$ |  |  | $(220,15)$ |  |  | $(297,15)$ |  |  |
| No. | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig | $C_{\mathrm{L}, 3}$ | $C_{3,4}$ | Sig |
| 1 | 0.29 | 0.00 | Y | 0.45 | 0.00 | Y | 0.31 | 0.00 | Y | 0.47 | 0.00 | Y | 0.25 | 0.00 | Y | 0.17 | 0.00 | Y | 0.13 | 0.00 | Y | 0.13 | 0.00 | Y |
| 2 | 0.40 | 0.25 | Y | 0.42 | 0.00 | Y | 0.40 | 0.00 | Y | 0.36 | 0.00 | Y | 0.27 | 0.00 | Y | 0.31 | 0.00 | Y | 0.29 | 0.00 | Y | 0.47 | 0.00 | Y |
| 3 | 0.75 | 0.00 | Y | 0.56 | 0.00 | Y | 0.40 | 0.00 | Y | 0.45 | 0.00 | Y | 0.31 | 0.00 | Y | 0.28 | 0.00 | Y | 0.33 | 0.00 | Y | 0.23 | 0.00 | Y |
| 4 | 0.57 | 0.25 | Y | 0.40 | 0.00 | Y | 0.50 | 0.00 | Y | 0.33 | 0.00 | Y | 0.40 | 0.00 | Y | 0.08 | 0.00 | N | 0.15 | 0.00 | Y | 0.25 | 0.00 | Y |
| 5 | 0.71 | 0.00 | Y | 0.55 | 0.00 | Y | 0.39 | 0.00 | Y | 0.25 | 0.00 | Y | 0.21 | 0.00 | Y | 0.25 | 0.00 | Y | 0.06 | 0.00 | N | 0.11 | 0.00 | Y |
| 6 | 0.57 | 0.20 | Y | 0.50 | 0.00 | Y | 0.26 | 0.00 | Y | 0.29 | 0.00 | Y | 0.28 | 0.00 | Y | 0.36 | 0.00 | Y | 0.11 | 0.00 | Y | 0.25 | 0.00 | Y |
| 7 | 0.63 | 0.25 | Y | 0.64 | 0.00 | Y | 0.42 | 0.00 | Y | 0.21 | 0.00 | Y | 0.30 | 0.00 | Y | 0.31 | 0.00 | Y | 0.19 | 0.00 | Y | 0.19 | 0.00 | Y |
| 8 | 0.20 | 0.50 | N | 0.40 | 0.00 | Y | 0.47 | 0.00 | Y | 0.33 | 0.00 | Y | 0.12 | 0.00 | Y | 0.29 | 0.00 | Y | 0.18 | 0.00 | Y | 0.11 | 0.00 | N |
| 9 | 0.50 | 0.00 | Y | 0.30 | 0.00 | Y | 0.53 | 0.00 | Y | 0.33 | 0.00 | Y | 0.17 | 0.00 | Y | 0.23 | 0.00 | Y | 0.14 | 0.00 | Y | 0.20 | 0.00 | Y |
| 10 | 0.67 | 0.00 | Y | 0.46 | 0.00 | Y | 0.25 | 0.00 | Y | 0.23 | 0.00 | Y | 0.40 | 0.00 | Y | 0.25 | 0.00 | Y | 0.41 | 0.00 | Y | 0.25 | 0.00 | Y |

![img-9.jpeg](img-9.jpeg)

Fig. 10. Boxplot of $C$ metric between KEDA and A3.
each case, the average $C$ metric of ten independent runs is summarized in Tables 10 and 11. The boxplots of the comparison between all $C$ metrics of KEDA and the comparison algorithm are shown in Figs. 11 and 12. The T-hypothesis test with a $95 \%$ confidence level is carried out, setting alternative hypothesis H1 such that the $C$ metric achieved by KEDA is greater than the $C$ metric achieved by the comparison algorithms. If H1 is implemented significantly ( $p<0.05$ ), then the flag is labeled as Y, otherwise it is labeled as N. C metric C(KEDA,NAGAII) and C(NAGA-II,KEDA) are denoted as $C_{L, n}$ and $C_{n, k}$ respectively for simplification in the tables. C(KEDA, MOEA/D) and C(MOEA/D, KEDA) are denoted as $C_{\mathrm{L}, m}$ and $C_{m, k}$.

In addition, the IGD of the proposed algorithm and two comparative algorithms, and presented them in the Table 12. The true Pareto front is composed of the common Pareto front obtained by all algorithms. KEDA, NSGA-II and MOEA/D are denoted as $A k, A n$ and $A m$ respectively for simplification. The Pareto fronts obtained by KEDA, NSGA-II, and MOEA/D are illustrated in Figs. 13-16.

It can be seen from the results that C(KEDA, NSGA-II) are larger than C(NSGA-II, KEDA) in most cases, which implies that KEDA performs better than NSGA-II in solving this problem. The average value of C(KEDA, NSGA-II) is 0.770 and the average value of C(NSGA-II, KEDA) is 0.066 , which implies that about $77.0 \%$ NSGA-II solutions are dominated by the KEDA solutions, while about $6.6 \%$ KEDA solutions are dominated by NSGA-II solutions.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Boxplot of $C$ metric for KEDA and NSGA-II.
![img-11.jpeg](img-11.jpeg)

Fig. 12. Boxplot of $C$ metric for KEDA and MOEA/D.

Similarly, it can be seen from the results that C(KEDA, MOEA/D) are larger than C(MOEA/D), KEDA) in most cases, which implies that KEDA performs better than MOEA/D in solving this problem. The average value of C(KEDA, NSGA-II) is 0.881 and the average value of C(NSGAII, KEDA) is 0.002 . About $88.1 \%$ MOEA/D solutions are dominated by the KEDA solutions, while about $0.2 \%$ KEDA solutions are dominated

Table 10
Comparison results of $C$ metric between KEDA and NSGA-II.

| $\left(N_{T}, N_{W}\right)$ | $(20,4)$ |  |  | $(50,8)$ |  |  | $(70,8)$ |  |  | $(83,8)$ |  |  | $(100,10)$ |  |  | $(148,10)$ |  |  | $(220,10)$ |  |  | $(297,10)$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| No. | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig |
| 1 | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.92 | 0.00 | Y | 0.78 | 0.00 | Y | 0.45 | 0.20 | Y | 0.90 | 0.00 | Y | 0.89 | 0.00 | Y | 0.43 | 0.33 | N |
| 2 | 0.75 | 0.17 | Y | 0.90 | 0.00 | Y | 1.00 | 0.00 | Y | 0.94 | 0.00 | Y | 0.83 | 0.00 | Y | 0.89 | 0.00 | Y | 1.00 | 0.00 | Y | 0.50 | 0.33 | Y |
| 3 | 0.90 | 0.00 | Y | 0.94 | 0.00 | Y | 0.83 | 0.00 | Y | 0.94 | 0.20 | Y | 0.43 | 0.00 | Y | 0.89 | 0.00 | Y | 1.00 | 0.00 | Y | 0.67 | 0.00 | Y |
| 4 | 0.71 | 0.00 | Y | 0.88 | 0.14 | Y | 0.94 | 0.00 | Y | 1.00 | 0.00 | Y | 0.43 | 0.12 | Y | 0.83 | 0.00 | Y | 0.63 | 0.25 | Y | 0.60 | 0.00 | Y |
| 5 | 0.83 | 0.00 | Y | 1.00 | 0.00 | Y | 0.78 | 0.00 | Y | 0.89 | 0.00 | Y | 0.62 | 0.00 | Y | 0.90 | 0.00 | Y | 0.73 | 0.00 | Y | 0.43 | 0.00 | Y |
| 6 | 0.71 | 0.00 | Y | 0.94 | 0.00 | Y | 0.93 | 0.17 | Y | 0.80 | 0.25 | Y | 0.60 | 0.00 | Y | 0.91 | 0.00 | Y | 1.00 | 0.00 | Y | 0.40 | 0.00 | Y |
| 7 | 0.63 | 0.50 | N | 1.00 | 0.00 | Y | 0.90 | 0.20 | Y | 1.00 | 0.00 | Y | 0.29 | 0.14 | Y | 0.73 | 0.00 | Y | 0.50 | 0.00 | Y | 0.56 | 0.00 | Y |
| 8 | 0.88 | 0.13 | Y | 0.94 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.75 | 0.16 | Y | 0.92 | 0.00 | Y | 0.90 | 0.00 | Y | 0.50 | 0.33 | N |
| 9 | 0.50 | 0.25 | Y | 1.00 | 0.00 | Y | 0.88 | 0.00 | Y | 0.82 | 0.00 | Y | 0.43 | 0.25 | Y | 1.00 | 0.00 | Y | 0.88 | 0.25 | Y | 0.20 | 0.33 | N |
| 10 | 0.75 | 0.13 | Y | 1.00 | 0.00 | Y | 0.95 | 0.07 | Y | 1.00 | 0.00 | Y | 0.43 | 0.60 | N | 0.44 | 0.33 | N | 0.75 | 0.00 | Y | 0.40 | 0.80 | N |
| $\left(N_{T}, N_{W}\right)$ | $(20,5)$ |  |  | $(50,10)$ |  |  | $(70,10)$ |  |  | $(83,10)$ |  |  | $(100,12)$ |  |  | $(148,12)$ |  |  | $(220,15)$ |  |  | $(297,15)$ |  |  |  |
| No. | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig |
| 1 | 0.86 | 0.00 | Y | 0.44 | 0.33 | Y | 0.46 | 0.20 | Y | 0.55 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.66 | 0.40 | N |
| 2 | 1.00 | 0.00 | Y | 0.56 | 0.09 | Y | 0.75 | 0.00 | Y | 0.43 | 0.16 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.82 | 0.00 | Y |
| 3 | 1.00 | 0.00 | Y | 0.67 | 0.33 | N | 0.40 | 0.00 | Y | 0.44 | 0.00 | Y | 0.90 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.80 | 0.00 | Y |
| 4 | 1.00 | 0.00 | Y | 0.25 | 0.20 | Y | 0.75 | 0.00 | Y | 0.43 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.96 | 0.00 | Y | 0.64 | 0.00 | Y |
| 5 | 1.00 | 0.00 | Y | 0.47 | 0.25 | Y | 0.56 | 0.12 | Y | 0.36 | 0.00 | Y | 0.79 | 0.19 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.82 | 0.00 | Y |
| 6 | 1.00 | 0.00 | Y | 0.63 | 0.00 | Y | 0.63 | 0.16 | N | 0.63 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.75 | 0.00 | Y |
| 7 | 1.00 | 0.00 | Y | 0.20 | 0.33 | N | 0.53 | 0.12 | Y | 0.43 | 0.33 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.81 | 0.00 | Y |
| 8 | 1.00 | 0.00 | Y | 0.38 | 0.33 | Y | 0.60 | 0.00 | Y | 0.67 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.78 | 0.00 | Y |
| 9 | 0.80 | 0.00 | Y | 0.29 | 0.25 | Y | 0.64 | 0.25 | Y | 0.14 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.71 | 0.00 | Y |
| 10 | 0.75 | 0.00 | Y | 0.50 | 0.20 | Y | 0.30 | 0.00 | Y | 0.50 | 0.00 | Y | 1.00 | 0.00 | Y | 0.94 | 0.00 | Y | 1.00 | 0.00 | Y | 0.69 | 0.25 | Y |

Table 11
Comparison results of $C$ metric between KEDA and MOEA/D.

| $\left(N_{T}, N_{W}\right)$ | $(20,4)$ |  |  | $(50,8)$ |  |  | $(70,8)$ |  |  | $(83,8)$ |  |  | $(100,10)$ |  |  | $(148,10)$ |  |  | $(220,10)$ |  |  | $(297,10)$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| No. | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig |
| 1 | 0.25 | 0.33 | N | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.86 | 0.00 | Y | 0.90 | 0.00 | Y | 1.00 | 0.00 | Y | 0.57 | 0.00 | Y |
| 2 | 0.75 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.75 | 0.00 | Y | 0.93 | 0.00 | Y | 0.57 | 0.00 | Y |
| 3 | 0.33 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.50 | 0.14 | Y | 0.56 | 0.00 | Y | 0.78 | 0.00 | Y | 1.00 | 0.00 | Y |
| 4 | 0.43 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.89 | 0.00 | Y | 0.57 | 0.00 | Y | 0.91 | 0.00 | Y | 0.50 | 0.12 | Y |
| 5 | 0.67 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.56 | 0.00 | Y | 0.78 | 0.00 | Y | 0.88 | 0.00 | Y |
| 6 | 0.38 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.89 | 0.00 | Y | 0.75 | 0.00 | Y | 0.90 | 0.00 | Y |
| 7 | 0.40 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.86 | 0.00 | Y | 0.89 | 0.00 | Y | 0.73 | 0.00 | Y | 1.00 | 0.00 | Y |
| 8 | 0.44 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.88 | 0.00 | Y | 0.75 | 0.00 | Y | 0.89 | 0.00 | Y | 0.82 | 0.00 | Y |
| 9 | 0.29 | 0.12 | N | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.88 | 0.00 | Y | 0.78 | 0.00 | Y | 0.78 | 0.00 | Y | 0.83 | 0.00 | Y |
| 10 | 0.44 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.93 | 0.00 | Y | 0.80 | 0.00 | Y | 0.69 | 0.00 | Y | 0.60 | 0.00 | Y |
| $\left(N_{T}, N_{W}\right)$ | $(20,5)$ |  |  | $(50,10)$ |  |  | $(70,10)$ |  |  | $(83,10)$ |  |  | $(100,12)$ |  |  | $(148,12)$ |  |  | $(220,15)$ |  |  | $(297,15)$ |  |  |  |
| No. | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig | $C_{\mathrm{L} \mathrm{c}}$ | $C_{\mathrm{L} \mathrm{L}}$ | Sig |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 0.75 | 0.00 | Y | 0.86 | 0.00 | Y | 0.80 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 2 | 0.91 | 0.00 | Y | 0.89 | 0.00 | Y | 0.89 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 3 | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 0.82 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 4 | 0.88 | 0.00 | Y | 1.00 | 0.00 | Y | 0.92 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 5 | 0.71 | 0.00 | Y | 0.80 | 0.00 | Y | 0.83 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 6 | 0.83 | 0.00 | Y | 1.00 | 0.00 | Y | 0.67 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 7 | 0.91 | 0.00 | Y | 0.75 | 0.00 | Y | 0.56 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 8 | 1.00 | 0.00 | Y | 0.89 | 0.00 | Y | 0.75 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 9 | 0.80 | 0.00 | Y | 0.64 | 0.00 | Y | 0.63 | 0.00 | Y | 0.60 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
| 10 | 0.80 | 0.00 | Y | 0.79 | 0.00 | Y | 0.75 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y | 1.00 | 0.00 | Y |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

![img-12.jpeg](img-12.jpeg)

Fig. 13. Pareto fronts obtained by KEDA and the comparison algorithms for a task size of $20 / 50$.

Fig. 14. Pareto fronts obtained by KEDA and the comparison algorithms for a task size of $70 / 83$.

![img-13.jpeg](img-13.jpeg)

![img-14.jpeg](img-14.jpeg)

Fig. 15. Pareto fronts obtained by KEDA and the comparison algorithms for a task size of $100 / 148$.
![img-15.jpeg](img-15.jpeg)

Fig. 16. Pareto fronts obtained by KEDA and the comparison algorithms for a task size of $220 / 297$.
by MOEA/D solutions. It can be observed that the performance of KEDA improves as the scale of workstation increases. The possible reason is that our proposed KEDA is more likely to identify better solutions within a larger solution space.

In addition, the Pareto fronts obtained by KEDA under different scales of instances are better than the fronts obtained by the other two algorithms. The IGD results show that the KEDA solutions are much nearer to the Pareto fronts achieved by all the algorithms. Specially, $\mathrm{IGD}=0$ denotes that all the KEDA solutions denominate other solutions and none of them are dominated by others.

## 5. Conclusion

This paper addresses the energy-efficient JRALB-FP with the minimization of both cycle time and fuel consumption cost. An knowledgeguided EDA is presented to solve the energy-efficient JRALB-FP. From numerical experimental results, it shows that our proposed algorithm performs better than the existing algorithms in terms of both time and energy consumption index. The superior performances of the algorithm mainly owe to the following aspects.
(1) The hybrid individual generation method, which combines both probability sampling and the knowledge-based heuristic method.
(2) The cooperation of search operators and probability model updating.
(3) Two problem knowledge guided local search operators, which enhances exploitation capability.

The future work will involve studying various other types of assembly line balancing and part feeding problems, including the mixmodel assembly, other feeding strategies, and other objectives, such as addressing the assembly imbalance between different workstations. In-time assembly task assignment will be also considered through learning-enhanced methods [41]. We will also focus on the research about the analysis of problem and the utilization of the problem-specific knowledge to improve the effectiveness of the proposed algorithm. Moreover, it is also very important to apply the algorithms to real production cases.

## CRediT authorship contribution statement

Chu-ge Wu: Validation, Project administration, Methodology, Investigation, Funding acquisition, Formal analysis, Conceptualization, Writing - original draft, Writing - review \& editing. Ruochen Zhang: Writing - review \& editing, Data curation, Investigation, Methodology, Writing - original draft. Yuanqing Xia: Validation, Project administration.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This work was funded in part by the National Key R\&D Program of China (No. 2021YFB3300400) and the National Natural Science Foundation of China (No. 62203049).

## References

[1] N. Boysen, P. Schulze, A. Scholl, Assembly line balancing: What happened in the last fifteen years? European J. Oper. Res. 301 (3) (2022) 797-814, http://dx.doi.org/10.1016/j.ejor.2021.11.043.
[2] J. Sternatz, Enhanced multi-Hoffmann heuristic for efficiently solving real-world assembly line balancing problems in automotive industry, European J. Oper. Res. 235 (3) (2014) 740-754, http://dx.doi.org/10.1016/j.ejor.2013.11.005.
[3] Z. Fang, J. Wang, Y. Ren, Z. Han, H.V. Poor, L. Hanzo, Age of information in energy harvesting aided massive multiple access networks, IEEE J. Sel. Areas Commun. 40 (5) (2022) 1441-1456.
[4] H. Feng, J. Wang, Z. Fang, J. Chen, D.-T. Do, Evaluating Aid-Centric HARQ protocols for UAV networks, IEEE Trans. Commun. (2023).
[5] United States Environmental Protection Agency, Sources of greenhouse gas emissions, 2017, https://www.epa.gov/ghgemissions/sources-greenhouse-gas-emissions.
[6] N. Boysen, M. Fliedner, A. Scholl, Assembly line balancing: Which model to use when? Int. J. Prod. Econ. 111 (2) (2008) 509-528.
[7] N. Boysen, M. Fliedner, A. Scholl, A classification of assembly line balancing problems, European J. Oper. Res. 183 (2) (2007) 674-693, http://dx.doi.org/ 10.1016/j.ejor.2006.10.010.
[8] Y.-l. Jiao, H.-q. Jin, X.-c. Xing, M.-j. Li, X.-r. Liu, Assembly line balance research methods, literature and development review, Concurr. Eng. 29 (2) (2021) 183-194, http://dx.doi.org/10.1177/1063293X20987910.
[9] B. qi Sun, L. Wang, Z. ping Peng, Bound-guided hybrid estimation of distribution algorithm for energy-efficient robotic assembly line balancing, Comput. Ind. Eng. 146 (2020) 106604, http://dx.doi.org/10.1016/j.cie.2020.106604.
[10] L.W. Roup Sun, An estimation of distribution algorithm with branch-and-bound based knowledge for robotic assembly line balancing, Complex Intell. Syst. 7 (2021) 1125-1138.
[11] Z. Li, M.N. Janardhanan, Q. Tang, S.G. Ponnambalam, Model and metaheuristics for robotic two-sided assembly line balancing problems with setup times, Swarm Evol. Comput. 50 (2019) 100567.
[12] H.A. Sedding, Line side placement for shorter assembly line worker paths, IBR Trans. 52 (2) (2020) 181-198, http://dx.doi.org/10.1080/24725854.2018. 1508929, arXiv:https://doi.org/10.1080/24725854.2018.1508929.
[13] D. Battini, M. Faccio, A. Persona, F. Sgarbossa, Design of the optimal feeding policy in an assembly system, Int. J. Prod. Econ. 121 (1) (2009) 233-254, http: //dx.doi.org/10.1016/j.ijpe.2009.05.016, Modelling and Control of Productive Systems: Concepts and Applications.
[14] M. Calzavara, S. Finco, D. Battini, F. Sgarbossa, A. Persona, A joint assembly line balancing and feeding problem (JALBFP) considering direct and indirect supply strategies, Int. J. Prod. Res. 60 (19) (2022) 5727-5745, http://dx.doi.org/10. 1080/00207543.2021.1968527.
[15] M. Albus, M.F. Huber, Resource reconfiguration and optimization in brownfield constrained robotic assembly line balancing problems, J. Manuf. Syst. (2023) 132-142.
[16] C. Weckenborg, K. Kieckhäfer, C. Müller, M. Grunewald, T.S. Spengler, Balancing of assembly lines with collaborative robots, Bus. Res. (2020) 93-132.

[17] A. Nourmohammadi, M. Fathi, A.H.C. Ng, E. Mahmoodi, A genetic algorithm for heterogenous human-robot collaboration assembly line balancing problems, Procedia CIRP (2022) 1444-1448.
[18] F. Haotian, W. Hongjun, Research on robot assembly line balancing considering energy consumption, Mech. Mach. Sci. (2021) 869-881.
[19] A. Nourmohammadi, M. Fathi, A.H.C. Ng, Balancing and scheduling assembly lines with human-robot collaboration tasks, Comput. Oper. Res. (2022) 105674.
[20] Z. Mao, J. Zhang, K. Fang, D. Huang, Y. Sun, Balancing U-type assembly lines with human-robot collaboration, Comput. Oper. Res. (2023) 106359.
[21] Y. Labrichi, D. Damand, L. Denouni, N. Grangeon, S. Norre, Investigating two variants of the sequence-dependent robotic assembly line balancing problem by means of a split-based approach, Int. J. Prod. Res. (2023) 2322-2338.
[22] N.A. Schmid, V. Lintire, A classification of tactical assembly line feeding problems, Int. J. Prod. Res. 57 (24) (2019) 7586-7609, http://dx.doi.org/10. 1080/00207543.2019.1581957.
[23] J. Sternatz, The joint line balancing and material supply problem, Int. J. Prod. Econ. 159 (2015) 304-318, http://dx.doi.org/10.1016/j.ijpe.2014.07.022.
[24] R.-H. Zhou, C.-Y. Shen, Multi-objective optimization of material delivery for mixed model assembly lines with energy consideration, J. Clean. Prod. 192 (2018) 293-305.
[25] Ö.F. Yilmaz, An integrated bi-objective U-shaped assembly line balancing and parts feeding problem: Optimization model and exact solution method, Ann. Math. Artil. Intell. 90 (7-9) (2022) 679-696, http://dx.doi.org/10.1007/s10472-020-09718-y.
[26] H. Zhang, X. Li, Z. Kan, X. Zhang, Z. Li, Research on optimization of assembly line based on product scheduling and just-in-time feeding of parts, Assem. Autom. 41 (5) (2021) 577-588, http://dx.doi.org/10.1108/AA-12-2020-0196.
[27] J. Chen, X. Jia, Energy-efficient integration of assembly line balancing and part feeding with a modified genetic algorithm, Int. J. Adv. Manuf. Technol. 121 (3-4) (2022) 2257-2278.
[28] R. Zhou, Z. Zhu, Multi-objective optimization of greening scheduling problems of part feeding for mixed model assembly lines based on the robotic mobile fulfillment system, Neural Comput. Appl. 33 (2021) 9913-9937.
[29] P. Larranaga, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation (Genetic Algorithms and Evolutionary Computation), Kluwer Academic, 2002.
[30] N. Zhu, F. Zhao, L. Wang, C. Dong, An enhanced Kalman filtering and historical learning mechanism driven estimation of distribution algorithm, Swarm Evol. Comput. 86 (2024) 101502.
[31] Y. Du, J. qing Li, C. Luo, L. lei Meng, A hybrid estimation of distribution algorithm for distributed flexible job shop scheduling with crane transportations, Swarm Evol. Comput. 62 (2021) 100861.
[32] F. Zhao, B. Zhu, L. Wang, An estimation of distribution algorithm-based hyperheuristic for the distributed assembly mixed no-idle permutation flowshop scheduling problem, IEEE Trans. Syst. Man Cybern. Syst. (2023) 1-12.
[33] C.G. Wu, L. Wang, J.J. Wang, A path relinking enhanced estimation of distribution algorithm for direct acyclic graph task scheduling problem, Knowl.-Based Syst. (2021) 107255.
[34] Z.-Q. Zhang, B. Qian, R. Hu, H.-F. Jin, L. Wang, A matrix-cube-based estimation of distribution algorithm for the distributed assembly permutation flow-shop scheduling problem, Swarm Evol. Comput. 60 (2021) 100785.
[35] M.R. Sierra, C.A. Coello Coello, Improving PSO-based multi-objective optimization using crowding, mutation and $\varepsilon$-dominance, Lecture Notes in Comput. Sci. 3410 (2005) 505-519, http://dx.doi.org/10.1007/978-3-540-31880-4_35.
[36] J. Mukund Nilakantan, S.G. Ponnambalam, N. Jawahar, G. Kanagaraj, Biotospired search algorithms to solve robotic assembly line balancing problems, Neural Comput. Appl. 26 (2015) 1379-1393.
[37] A. Lipowski, D. Lipowska, Roulette-wheel selection via stochastic acceptance, Phys. A 391 (6) (2012) 2193-2196.
[38] S. Baluja, Population-Based Incremental Learning. A Method for Integrating Genetic Search Based Function Optimization and Competitive Learning, Technical Report, Carnegie Mellon University, 1994.
[39] Q. Zhang, H. Li, MOEA/D: a multiobjective evolutionary algorithm based on decomposition, IEEE Trans. Evol. Comput. 11 (6) (2007) 712-731, http://dx. doi.org/10.1109/TEVC.2007.892759.
[40] K. Deb, A. Pratap, S. Agarwal, T. Meyarivan, A fast and elitist multiobjective genetic algorithm: NSGA-II, IEEE Trans. Evol. Comput. 6 (2) (2002) 182-197, http://dx.doi.org/10.1109/4235.996017.
[41] J.-F. Chen, L. Wang, H. Ren, J. Pan, S. Wang, J. Zheng, X. Wang, An imitation learning-enhanced iterated matching algorithm for on-demand food delivery, IEEE Transactions on Intelligent Transportation Systems 23 (10) (2022) $18603-18619$.