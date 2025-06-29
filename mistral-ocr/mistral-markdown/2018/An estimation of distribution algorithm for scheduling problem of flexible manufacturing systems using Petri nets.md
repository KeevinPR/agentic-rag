# Accepted Manuscript 

An estimation of distribution algorithm for scheduling problem of flexible manufacturing systems using Petri nets

XinNian Wang, KeYi Xing, XiaoLing Li, JianChao Luo

| PII: | S0307-904X(17)30709-6 |
| :-- | :-- |
| DOI: | 10.1016/j.apm.2017.11.018 |
| Reference: | APM 12060 |

To appear in: Applied Mathematical Modelling

Received date: 3 June 2016
Revised date: 10 October 2017
Accepted date: 20 November 2017
Please cite this article as: XinNian Wang, KeYi Xing, XiaoLing Li, JianChao Luo, An estimation of distribution algorithm for scheduling problem of flexible manufacturing systems using Petri nets, Applied Mathematical Modelling (2017), doi: 10.1016/j.apm.2017.11.018

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Highlights 

- This is the first report on applying estimation of distribution algorithm (EDA) to the studied problem.
- A kind of PN-based deadlock controllers for FMSs is imbedded to exclude infeasible individuals.
- An effective voting procedure is adopted to construct the probabilistic model of EDA.
- The longest common subsequence is also embedded in the model for mining excellent genes.
- A new modified variable neighborhood search is developed as an efficiency enhancement of EDA.

# An estimation of distribution algorithm for scheduling problem of flexible manufacturing systems using Petri nets 

XinNian Wang ${ }^{1}$, KeYi Xing ${ }^{1, *}$, XiaoLing $\mathrm{Li}^{1}$, JianChao Luo ${ }^{1}$


#### Abstract

Based on the place-timed Petri net models of flexible manufacturing systems (FMSs), this paper proposes a novel effective estimation of distribution algorithm (EDA) for solving the scheduling problem of FMSs. A candidate solution is represented as an individual with two sections. The first contains the route information while the second is a permutation with repetition for parts. The feasibility of individuals is checked and geocontroled by a highly permissiveness deadlock controller. A feasible individual is interpreted into a deadlock-free schedule while the infeasible ones are amended. The probabilistic model in EDA is constructed via a voting procedure. An offspring individual is then produced based on the model from a seed individual, and the set of seed individuals is extracted by a roulette method from the current population. The longest common subsequence is also embedded into the probabilistic model for mining good genes. A modified variable neighborhood search is applied on offspring individuals to obtain better solutions in their neighbors and hence to improve EDA's performance. Computational results show that our proposed algorithm outperforms all the existing ones on benchmark examples for the studied problem. It is an important practice significance for the manufacturing of time-critical and multi-type products.

[^0]
[^0]:    *Corresponding author

    Email address: kyxingmail.xjtu.edu.cn (KeYi Xing )
    ${ }^{1}$ The State Key Laboratory for Manufacturing Systems Engineering and Systems Engineering Institute, Xi'an Jiaotong University, Xi'an 710049, P. R. China.

Keywords: flexible manufacturing system, timed Petri net, scheduling, estimation of distribution algorithm, variable neighborhood search

# 1. Introduction 

A flexible manufacturing system (FMS) is a computer controlled manufa turing system which consists of a limited set of resources and is capable to process multi-types of parts. Typical applications in real-life include eacogues 5 productions, industrial stamping systems, and semiconductor manufacturing industries [1-4]. These systems generally exhibit high degrees of resource sharing and route flexibility. The competitions for limited shared resources by concurrent processes of various parts may result in deadlocks, if no proper control or scheduling method is applied. Once a deadlock appears, the whole system or a part of it remains indefinitely blocked and cannot finish the task. Thus, it is of paramount importance to develop effective control and scheduling methods to prevent deadlocks while optimize the system performance.

The deadlock problem has been widely researched from the control viewpoint, and many control methods have been proposed [5-10]. Although the deadlock-free operation in FMS is guaranteed via the above deadlock control methods, the system performance is not considered. Scheduling is an integral part for various types of manufacturing systems [11-15], and the scheduling of FMSs involves not only the handling of deadlocks but the optimization of a certain objective function, and therefore is more difficult than a pure deadlock control problem. There are quite a few works on this area [4, 16-25]. Scthi at al. 16] dean with the problem of sequencing parts and robot moves in a robotic cell. The cycle time formulas are developed and analyzed for cells producing a single part, type, ising, two or three machines, and optimal sequences of robot moves are obtained. Ramaswamy and Joshi [17] proposed a mathematical model for automated manufacturing systems (AMSs) with material handling devices and limited buffers. A Lagrangian relaxation heuristic was used to simplify the model for searching the optimized average flow time. To search for the optimal

or near-optimal schedule of the semiconductor test facility, Xiong and Zhou [4] proposed two hybrid heuristic strategies by combining the best-first with the controlled backtracking based on the execution of Petri nets (PNs). Abdallah, Elmaraghy, and Elmekkawy [18] used timed PNs to model FMSs and proposed a scheduling algorithm to minimize the mean flow time. Their algorithm is based on a depth-first strategy and the branch and bound principle together with a siphon truncation technique. Dashora et al. [19] used extended colored timed PN to model the dynamic behavior of the system of simple sequential processes with resources ( $\mathrm{S}^{3} \mathrm{PR}$ ) and presented a deadlock-free scheduling method based on an evolutionary endosymbiotic learning automata algorithm. Xing et al. [20] embedded a deadlock avoidance policy (DAP) into a genetic algorithm and developed a deadlock-free genetic algorithm for AMSs. A one-step look-ahead method is used to guarantee the feasibilities of chromosomes and the deadlockfree schedule is then obtained by amending the infeasible ones. Han et al. [21] proposed a new deadlock-free genetic algorithm with different kinds of crossover and mutation operations. The effects of different deadlock controllers were also discussed and compared. Luo et al. [22] developed new scheduling approaches by combining DAPs and hybrid heuristic searches. Based on a PN reachability graph and minimum processing time matrix, new heuristic and selection functions are designed to guide the search. Baruwa et al. [23] proposed an Anytime Layered search algorithm based on the reachability analysis of timed colored PX. They combines breadth-first iterative deepening A* with suboptimal breadth-first heuristic search and backtracking. Lei et al. [24] proposed an effective hybrid discrete differential evolution algorithm based on the timed PN models of FMSs, where sequence-dependent setup time is considered. A variable neighborhood search is adopted to improve the solutions' qualities. Han et al. [25] proposed a hybrid particle swarm optimization algorithm by incorporating particle normalization and simulated annealing based local search into the algorithm. A random-key based solution representation is designed to encode the schedule into a particle.

Estimation of distribution algorithm (EDA) [26, 27] is an evolutionary algo-

rithm proposed in recent years and has received increasing attentions of many
researchers. It uses neither crossover nor mutation operator, but reproduces offsprings based on a probabilistic model learned from a population of parents. This model-based approach to optimization allows EDA to successively solve many complex and large problems [28-31]. However, to the best of our knowledge, no work has been done for the scheduling problem of FMSs using EDA Can EDA be used to solve this problem and obtain more promising results than existing methods?

This work intends to answer the question by proposing a new EDA. A candidate solution of the scheduling problem is represented as an individual of two sections, route information and operation sequence. This first section contains the route information of parts and the second is a permutation with repetition for all the parts. To exclude infeasible individuals, a kind of PN-based deadlock controllers for FMSs is imbedded. Since the probabilistic model of EDA constitutes the main issue and the performance of the algorithm is closely related to it [32], in this work, an effective setting procedure is adopted to construct the model. The longest common subsequence (LCS) that finds the common elements of two individuals is also embedded in the model for mining excellent genes. Then, an effective individual is produced based on the model from a seed individual, which is selected from the current population by a roulette method. Furthermore, to achieve a better result, a modified variable neighborhood search (MVNS) is developed as an efficiency enhancement of EDA. The local searches in MVNS are modified to accommodate the PN models of FMSs. To the author's knowledge, only a few research works [20-25] study the scheduling problem considered in this paper. Hence, we test and compare our proposed algorithm with all existing comparable examples and works. Experimental results and comparisons show that the proposed scheduling algorithm outperforms the existing ones, as it provides the best known solutions for 13 of 16 benchmark instances among the five compared approaches. Our proposed scheduling algorithm can be also applied to industrial problems such as flexible manufacturing cells and flexible job-shop production systems.

The rest of the paper is organized as follows. Sect. 2 reviews the PN modeling of FMSs and PN-based deadlock controllers. Sect. 3 develops a scheduling method via PN and EDA, together with the MVNS. The experimental results and comparisons are shown in Sect. 4. Sect. 5 concludes this paper.

# 2. Petri net modeling of FMSs 

This section first briefly reviews the basics of Petri nets (PNs), then the PN model of FMS for scheduling and the deadlock controller. For more details, the readers are referred to $[7,20,33-35]$.

### 2.1. Basics of $P N s$

A PN is a three-tuple $N=(P, T, F)$, where $P$ is a finite set of places, $T$ is a finite set of transitions, and $F \subseteq P \times T) \cup(P \times P)$ is the set of directed arcs. For a given node $x \in P \cup T$, its preset is defined as ${ }^{*} x=\{y \in P \cup T \mid(y, x) \in F\}$, and the postset $x^{\bullet}=\{y \in P \cup T \mid(x, y) \in P\}$.

Let $Z_{0}=\{0,1,2, \ldots\}$ and $Z_{k}=1, \ldots, k$. A path is a string $\alpha=x_{1} x_{2} \ldots x_{k}$, where $x_{i} \in P \cup T$ and $\left(x_{i}, x_{i+1}\right) \in Z_{i} \in Z_{k-1}$. A marking or state of $N$ is a mapping $M: P \rightarrow Z_{0}$. For a given marking $M$ and a place $p \in P$, denote $M(p)$ as the number of points in $p$ at $M$. A PN $N$ with an initial marking $M_{0}$, denoted as $(N, M_{0})$, is called a marked PN.

For a given transition $t \in T$, if $\forall p \in \bullet t, M(p)>0, t$ is enabled at $M$, denoted by $M \mid t$. An enabled transition $t$ at $M$ can fire, yielding $M^{\prime}$, denoted by $M \mid t \geq M$, where $M^{\prime}(p)=M(p)-1, \forall p \in \bullet t \backslash t \bullet, M^{\prime}(p)=M(p)+1, \forall p \in t \bullet \backslash \bullet t$, and otherwise, $M(p)=M^{\prime}(p)$. A sequence of transitions $\alpha=t_{1} t_{2} \ldots t_{k}$ is feasible from $M$ if $M_{i} \mid t_{i}>M_{i+1}, i \in Z_{k}$, where $M_{1}=M$.

A P-timed PN $[34,35]$ is defined as a three-tuple $\left(N, M_{0}, d\right)=\left(P, T, F, M_{0}, d\right)$, where $\left(N, M_{0}\right)=\left(P, T, F, M_{0}\right)$ is a marked PN, $d: P \rightarrow R^{+}$is the delay function, and $R^{+}$is the set of nonnegative real numbers. In a P-timed PN, tokens at a marking $M$ are divided into two classes, available and unavailable. A token in place $p \in P$ becomes available if it has stayed in $p$ for at least $d(p)$ time units;

otherwise, it is unavailable. For a given marking $M$ and a place $p \in P$, denote $M^{a}(p)$ and $M^{u}(p)$ as the number of available and unavailable tokens in $p$ at $M$,
respectively. In P-timed PNs, a transition $t \in T$ is enabled at any time instance if $\forall p \in \bullet t, M^{a}(p)>0$. The firing of transition $t$ at $M$ yields a new marking $M^{\prime}$ by removing one available token from each $t$ 's input place, and deposits one token into each $t$ 's output place.

# 2.2. FMSs and their P-Timed PN models 

In this paper, the studied FMS contains $m$ types of resources $R=\left\{\tau_{k}, k \in Z_{m}\right\}$ and is able to process $n$ types of parts $Q=\left\{q_{i}, i \in Z_{n}\right\}$. A resource type may be a robot, buffer or machine. The capacity of a resource type $r_{k}$ is a positive integer, denoted as $C\left(r_{k}\right)$, indicating the maximum number of parts that $r_{k}$ can simultaneously process.

The lot size of type- $q_{i}$ parts is $\phi\left(q_{i}\right)$. A processing route of a part $w_{j}=$ $o_{j 1} o_{j 2} \ldots o_{j k} \ldots o_{j L_{j}}$ is an ordered sequence of operations, where $o_{j k}$ is the $k$ th operation in $w_{j}$ and $L_{j}$ is the total number of operations for type- $q_{i}$ part. For each type- $q_{i}$ parts, let $o_{i s}$ and $o_{i c}$ be two fictitious operations that represent the loading and the unloading of type- $q_{i}$ parts, respectively. Then, route $w_{j}$ is redefined as $w_{j}=o_{i s} o_{s 1} o_{i s} \ldots o_{j L_{j}} o_{i c}$. A part may have more than one route and can choose the routes when processing. Let $\Omega=\left\{w_{j} \mid 1 \leq j \leq|\Omega|\right\}$ be the set of all processing routes, and $\Omega_{i} \subseteq \Omega$ be the route set of type- $q_{i}$ parts.

In our PN model, a processing route $w_{j}$ of a type- $q_{i}$ part is modeled by a path of transitions and places $\alpha_{j}=p_{i s} t_{j 1} p_{j 1} t_{j 2} p_{j 2} \ldots t_{j k} p_{j k} \ldots t_{j L_{j}} p_{j L_{j}} t_{j\left(L_{j}+1\right)} p_{i c}$, where $p_{i s}$ and $p_{i c}$ represent operations $o_{i s}$ and $o_{i c}$, respectively, operation place $p_{j k}$ represents operation $o_{j k}$, transition $t_{j k}$ represents the start of $o_{j k}$ and the completion of $o_{j(k-1)}$. Then, for type- $q_{i}$ parts' processing routes, the marked PN model is defined as

$$
\left(N_{i}, M_{i 0}\right)=\left(P_{i} \cup\left\{p_{i s}, p_{i c}\right\}, T_{i}, F_{i}, M_{i 0}\right), i \in Z_{h}
$$

where $P_{i}=\bigcup_{1 \leq j \leq\left|\Omega_{i}\right|}\left\{p_{j 1}, p_{j 2}, \ldots, p_{j L_{j}}\right\}, T_{i}=\bigcup_{1 \leq j \leq\left|\Omega_{i}\right|}\left\{t_{j 1}, t_{j 2}, \ldots, t_{j\left(L_{j}+1\right)}\right\}$, and $F_{i}=\bigcup_{1 \leq j \leq\left|\Omega_{i}\right|}\left\{\left(p_{i s}, t_{j 1}\right),\left(t_{j 1}, p_{j 1}\right),\left(p_{j 1}, t_{j 2}\right), \ldots,\left(p_{j L_{j}}, t_{j\left(L_{j}+1\right)}\right),\left(t_{j\left(L_{j}+1\right)}\right.\right.$,

$p_{i e} \mid \ldots . M_{i 0}$ is the initial marking, $M_{i 0}(p)=0, \forall p \in P_{i} \cup\left\{p_{i e}\right\}$, and $M_{i 0}\left(p_{i s}\right)=$ $\phi\left(q_{i}\right)$. In $N_{i}, \forall t \in T_{i},\left|* t\right|=\left|t^{*}\right|=1$. A place $p \in P_{i}$ is called a split place if $\left|p^{*}\right|>1$. At split places, parts can choose their processing routes.

For each resource type $r_{k}$, assign a resource place and denoted also by $r_{k}$. The initial marking of $r_{k}$ is $C\left(r_{k}\right)$. Tokens in $r_{k}$ indicate available type $r_{k}$ resources. Let $P_{R}$ and $R(p)$ denote the set of all resource places and the resource required by operation place $p$, respectively. Suppose that each operation requires only one resource and any two successive operations require different types of resources. Then, add arcs from $R(p)$ to each transition in $p$ denoting the 10 occupying of $R(p)$, and arcs from each transition in $p^{*}(0, R(p)$ denoting the releasing of $R(p)$. Let $F_{R}$ be the set of arcs related with resource places. The marked PN that models the FMS is defined as:

$$
\left(N, M_{0}\right)=\left(P \cup P_{s} \cup P_{f} \cup P_{R}, T, F, M_{0}\right)
$$

where $P=\bigcup_{i \in Z_{k}} P_{i}, P_{s}=\left\{p_{i s} \mid i \in Z_{k}\right\}, P_{r_{k}}=\left\{p_{i e} \mid i \in Z_{k}\right\}, T=\bigcup_{i \in Z_{k}} T_{i}, F=$ $F_{Q} \cup F_{R}$, and $F_{Q}=\cup_{i \in Z_{k}} F_{i}$. The initial marking $M_{0}$ is defined as $M_{0}\left(p_{i s}\right)=$ $\phi\left(q_{i}\right), \forall p_{i s} \in P_{s} ; M_{0}(p)=0, \forall p \in \mathcal{K}, P_{f} ;$ and $M_{0}\left(r_{k}\right)=C\left(r_{k}\right), \forall r_{k} \in P_{R}$.

In this work, the P-timed $\mathrm{PN}\left(N, M_{0}, d\right)$ is used to describe the processing time needed by an operation. A time delay $d(p)$ is assigned to each operation place $p$ to denotodis processing time. Note that $d(p)=0, \forall p \in P_{s} \cup P_{f} \cup P_{R}$. Such PN is called as Pefro Net for Scheduling (PNS) [20].

When all operations of all parts are completed, the system reaches its final marking $M_{f}$, where $M_{f}\left(p_{i e}\right)=M_{0}\left(p_{i s}\right), \forall p_{i e} \in P_{f} ; M_{f}\left(r_{k}\right)=C\left(r_{k}\right), \forall r_{k} \in P_{R}$; and $M_{f}(p) \neq 0, \forall p \in P \cup P_{s}$. A feasible sequence of transitions $\alpha$ from $M_{0}$ is completely if $M_{0}\left[\alpha>M_{f}\right.$. Then, a schedule is a feasible and complete sequence of transitions $\alpha$ in the PNS, and the scheduling problem of FMSs is to find a feasible and complete sequence of transitions $\alpha^{*}$ so that its makespan is as small as possible.

Example 1: Consider an FMS that contains five types of resources, $r_{1}-r_{5}$, and can process two types of parts, $q_{1}$ and $q_{2}$. Type- $r_{1}$ and $r_{5}$ resources are robots with $C\left(r_{1}\right)=C\left(r_{5}\right)=1$, and type- $r_{2}, r_{3}$, and $r_{4}$ resources are machines

![img-0.jpeg](img-0.jpeg)

Figure 1: PNS model of the FMS in Example 1.
175 with $C\left(r_{2}\right)=C\left(r_{3}\right)=C\left(r_{4}\right)=2$. Type- $q_{1}$ parts can be processed orderly on $r_{1}, r_{2}, r_{3}$, and $r_{5}$, or on $r_{1}$, $r_{2}$, $r_{3}$, and $r_{5}$. Type- $q_{2}$ parts are processed orderly on $r_{5}, r_{4}$, and $r_{1}$. Thus, type- $q_{1}$ parts have two processing routes, $w_{1}=$ $p_{1 e} t_{11} p_{11} t_{12} p_{12} t_{13} p_{13} t_{13} p_{14} t_{15} p_{15}$ and $w_{2}=p_{1 e} t_{11} p_{11} t_{22} p_{22} t_{23} p_{23} t_{24} p_{14} t_{15} p_{1 e}$, while type- $q_{2}$ parts have only one $w_{3}=p_{2 e} t_{31} p_{31} t_{32} p_{32} t_{33} p_{33} t_{34} p_{2 e}$. The PN 100 model of the FMS is shown in Fig. 1, where the required processing parts of type $q_{1}$ and $q_{2}$ are both 2 .

# 2.3. deadlock controllers of PNS 

In our PNS, a given marking $M$ is a deadlock, if $M \neq M_{f}$ and no transition is enabled at $M$. According to the structures of PNSs and $\mathrm{S}^{3} \mathrm{PRs}$ for FMSs in $/ 5$, it can be known that deadlock controllers for $\mathrm{S}^{3} \mathrm{PR}$ and PNS of the same FMS are the same. Thus, deadlock controllers in [5-9] can directly be used for PNSs. For the purpose of obtaining desirable scheduling results, the deadlock controller in [7] with high permissiveness is used to avoid deadlocks in the proposed scheduling algorithm.

# 3. Scheduling algorithm based on EDA 

In this work, EDA is used for solving the scheduling problem of FMSs with respect to the makespan minimization. DAPs are embedded so that all individuals can be interpreted to feasible schedules. Some constraints of our studied FMS are also the best of interest.

1. A resources may be a risk of over-matching. The capacity of a system type is a positive integer and indicates the maximum number of jobs that this resource type can simultaneously handle.
2. A process that ceites a system to a level directly, quickly or sometimes. A job may be processed on more than one route and can choose the routes during its processline.
3. Each one of four requires one child's volume and the security. It is a required for the two successive operations of a job are different.
4. The processing times for operations are prescribed in advance.
5. No prescription is allowed.

Estimation of distribution algorithm (EDA) is an evolutionary algorithm that extracts the global statistical information by constructing an explicit probabilistic model from selected solutions [36]. An EDA works with a population of candidate solutions (individuals) to the problem. The population is evaluated by a fitness function and the initial population is generated randomly. A set of fitter solutions are selected and a probabilistic model that tries to estimate the probability distribution of the selected individuals is then constructed. A new individual is generated by sampling the distribution of the probabilistic model. These new individuals are incorporated back to the old population, replacing it partly or entirely. The process is repeated until some termination criteria are met, with each iteration of this procedure usually referred to as one generation of EDA [36].

The various elements of the proposed EDA are detailed as follows.

# 3.1. Representation, interpretation and reparation 

In this paper, permutations with repetitions are used to represent the in-
20 dividuals in EDA. An individual $\pi$ is rewritten as two sections $\pi=\left(S_{r} ; S_{o}\right)$, where $S_{r}$ contains the route information for parts and $S_{o}$ is a permutation with repetition for all the parts. Each part $J_{i}$ appears $l\left(J_{i}\right)$ times in So, where $l\left(J_{i}\right)$ $=\max \left\{l\left(w_{s}\right) \mid w_{s}\right.$ is a route of $\left.J_{i}\right\}$ and $l\left(w_{s}\right)$ is the length of $w_{s}$. In the initial population, both sections, $S_{r}$ and $S_{o}$, are generated randomly for each individual.

Since the $i$ th $J_{s}$ in $S_{o}$ represents $J_{s}$ 's $i$ th operation, $S_{r}$ can be uniquely decoded as a sequence of operations $o\left(S_{o}\right)$, and $\pi$ can also be rewritten as $\pi=\left(S_{r} ; o\left(S_{o}\right)\right)$. By associating all the operations to the corresponding transitions, $\pi$ is interpreted as a sequence of transitions $o(\pi) \mid t_{1} t_{2} \ldots t_{L}$, which is regarded as a schedule in PNS. Let $O_{i j}$ be the the $j$ th operation of part $J_{i}$ and $f\left(t_{k}\left[O_{i j}\right]\right)$ be the firing time of transition $t_{k}$ that corresponds to operation $O_{i j}$. Considering the prescribed operation sequence in PNS and the firing order in $\alpha(\pi), t_{k}\left[O_{i j}\right]$ can be fired only after (1) operation $O_{i(j-1)}$ is finished, and (2) $t_{k-1}$ is fired. Let $t_{k-1}$ and $t_{s}$ correspond to operations $O_{u v}$ and $O_{i(j-1)}$, respectively. Then, $f\left(t_{k}\left[O_{i j}\right]\right) \leq \max \left\{f\left(t_{s}\left[O_{i(j-1)}\right]\right)+d\left(O_{i(j-1)}\right), f\left(t_{k-1}\left[O_{u v}\right]\right)\right\}$, and the makespan of $\alpha(\pi)$ is

$$
\left.\lambda(\alpha(\pi))=\max \left\{f\left(t_{k}\left[O_{i j}\right]\right)+d\left(O_{i j}\right)\right\}\right)
$$

Example 2: Consider the PNS in Fig. 1. There are four parts to be processed: two type- $q_{1}$ parts, $J_{1}$ and $J_{2}$, and two type- $q_{2}$ parts, $J_{3}$ and $J_{4}$. The type- $q_{1}$ parts have two routes, $w_{1}$ and $w_{2}$, while type- $q_{2}$ parts have only one, $w_{3}$. Assume that $J_{1}$ and $J_{2}$ are processed on routes $w_{1}$ and $w_{2}$, respectively. Then, $S_{r}=$ $\left(w_{3}, w_{2}, w_{3}, w_{3}\right)$ can be used as the first section of an individual $\pi$. Since the route lengths $l\left(J_{i}\right)=5,5,4$, and 4 , the second section $S_{o}$ can be represented as a permutation with repetition which contains five $J_{1}$ 's, five $J_{2}$ 's, four $J_{3}$ 's, and four $J_{4}$ 's. For example, $S_{o}=\left(J_{1}, J_{1}, J_{3}, J_{2}, J_{3}, J_{2}, J_{4}, J_{1}, J_{2}, J_{3}, J_{4}, J_{1}, J_{3}, J_{4}, J_{1}, J_{2}\right.$, $J_{2}, J_{4}$ ). Then $\pi$ is represented as $\pi=\left(S_{r} ; S_{o}\right)=\left(w_{1}, w_{2}, w_{3}, w_{3} ; J_{1}, J_{1}, J_{3}, J_{2}, J_{3}\right.$,

$J_{2}, J_{4}, J_{1}, J_{2}, J_{3}, J_{4}, J_{1}, J_{3}, J_{4}, J_{1}, J_{2}, J_{2}, J_{4}$ ). On the other hand, $S_{o}$ can be interpreted as a sequence of operations $o\left(S_{o}\right)=\left(O_{11}, O_{12}, O_{31}, O_{21}, O_{32}, O_{22}, O_{41}\right.$, $\left.O_{13}, O_{23}, O_{33}, O_{42}, O_{14}, O_{34}, O_{43}, O_{15}, O_{24}, O_{25}, O_{44}\right)$, and $\pi$ can be interpreted as a sequence of transitions $\alpha(\pi)=\left(t_{11}, t_{12}, t_{31}, t_{11}, t_{32}, t_{22}, t_{31}, t_{13}, t_{23}, t_{33}, t_{32}\right.$,
$t_{14}, t_{34}, t_{33}, t_{15}, t_{24}, t_{15}, t_{34}$ ), or for the details, $\alpha(\pi)=\left(t_{11}\left[O_{11}\right], t_{12}\left[O_{12}\right], t_{31}\left[O_{31}\right]\right.$, $\left.t_{11}\left[O_{21}\right], t_{32}\left[O_{32}\right], t_{22}\left[O_{22}\right], t_{31}\left[O_{41}\right], t_{13}\left[O_{13}\right], t_{23}\left[O_{23}\right], t_{33}\left[O_{33}\right], t_{32}\left[O_{42}\right], t_{14}\left[O_{14}\right]\right)$, $\left.t_{34}\left[O_{34}\right], t_{33}\left[O_{43}\right], t_{15}\left[O_{15}\right], t_{24}\left[O_{24}\right], t_{15}\left[O_{25}\right], t_{34}\left[O_{44}\right]\right)$, where $t_{i j}$ in $t_{i j}\left(O_{i j}\right)$, is the start of operation $O_{u v}$.

Note that the sequence of transitions generated from an individual by the 20 interpretation aforementioned may be infeasible and lead to deadlocks. Thus, the feasibility of each individual should be checked and the infeasible individuals are translated into feasible ones. In this paper, the amending algorithm proposed in [20] is incorporated to obtain the feasible sequence of transitions from $M_{0}$ to $M_{f}$. The amending algorithm is based on the deadlock controller proposed in [7]. This deadlock controller is of highly permiseiveness and has simple structures. The readers can refer to $[7,20]$ for many details.

# 3.2. Probabilistic model 

The construction of a probabilistic model is an important procedure that differentiates EDA from other meta-heuristics. This model does not aim to 25 perfectly represent the set of selected individuals but to reveal a general distribution that captures the features of these individuals that make them better than other ones [36]. On the other hand, the efficiencies of the model constructing and information sampling are closely related to the performance of the algorithm. Hence, the choice of the probabilistic model plays a decisive role in EDA's success.

In this paper, a dominance matrix $D$ is used as the probabilistic model. Let $\Pi_{e}$ denote the elite set that contains the best $n_{e}$ individuals in the current population. To extract the global statistical information about parts and positions from $\Pi_{e}$ and thereby construct the probabilistic model, the voting procedure 25 used in $[29,37]$ is adopted in this paper.

Given $\pi=\left(S_{r} ; S_{o}\right) \in \Pi_{e}$. We know that $S_{o}$ is a permutation with repetition for parts and each part $J_{k}$ appears $l\left(J_{k}\right)$ times in $S_{o}$. To identify the repetitive parts in different positions in $S_{o}$, the sequence of operations $o\left(S_{o}\right)=O_{1} O_{2} \ldots O_{L}$ is used in the voting procedure. Define a reference sequence of operations $\Theta=$ $\theta_{1} \theta_{2} \ldots \theta_{L}$, which remains unchanged during the procedure. Note that all the elements in $o\left(S_{o}\right)$ are different from each other and an operation $O_{j}$ in $o\left(S_{o}\right)$ also appears in $\Theta$. Thus, we can assign a unique index $i$ to $O_{j}$ if $O_{j}=\theta_{i} \theta_{j} \in O_{j}$. Let $\delta_{\pi}(i, j)$ be the indicator function for $\pi$, where $\delta_{\pi}(i, j)=1$ if $O_{j} \neq \theta_{i}$ or $O_{j}$ has index $i$; otherwise $\delta_{\pi}(i, j)=0$.

Now an $L \times L$ dominance matrix $D$ can be constructed and its $(i, j)$-entry $D_{i j}$, which denotes the times (weighted) that operation $O_{j} \in \Theta$ appears at the $j$ th positions in $o\left(S_{o}\right)$ s of all the individuals in $\Pi_{e}$ is formally defined as follows.

$$
D_{i j}=\sum_{\pi \in \Pi_{e}} \delta_{\pi}(i, j) \times\left(\lambda\left(\alpha\left(\pi_{w}\right)\right)-\lambda\left(\alpha(\pi)\right)+\mathrm{I} \lambda\left(\lambda\left(\alpha\left(\pi_{w}\right)\right)-\lambda\left(\alpha\left(\pi_{b}\right)\right)+1\right)\right.
$$

where $\pi_{b}$ and $\pi_{w}$ are the best and worst individuals in the current population, respectively.

Example 3: Consider the PNS in Fig. 1. For simplicity, the required processing parts of type $q_{1}$ and $q_{2}$ are both set to 1 . The processing time of operations is randomly taken, with $d\left(p_{11}\right)=4, d\left(p_{12}\right)=32, d\left(p_{13}\right)=38, d\left(p_{14}\right)=5$, $d\left(p_{22}\right)=23, d\left(p_{23}\right)=20, d\left(p_{31}\right)=5, d\left(p_{32}\right)=22, d\left(p_{33}\right)=6$. Given a population of 5 individuals:
$\pi_{1}=\left(w_{1}, w_{3} ; J_{1}, J_{2}, J_{2}, J_{1}, J_{1}, J_{2}, J_{1}, J_{2}, J_{1}\right), \lambda\left(\alpha\left(\pi_{1}\right)\right)=53 ;$
$\pi_{2}=\left(w_{2}, w_{3} ; J_{1}, J_{2}, J_{2}, J_{1}, J_{2}, J_{2}, J_{1}, J_{1}, J_{1}\right), \lambda\left(\alpha\left(\pi_{2}\right)\right)=58 ;$
$\pi_{3}=\left(w_{3}, w_{3} ; J_{1}, J_{2}, J_{1}, J_{1}, J_{2}, J_{2}, J_{2}, J_{1}, J_{1}\right), \lambda\left(\alpha\left(\pi_{3}\right)\right)=60 ;$
$\pi_{4}=\left(w_{1}, w_{3} ; J_{1}, J_{1}, J_{2}, J_{1}, J_{2}, J_{1}, J_{1}, J_{2}, J_{2}\right), \lambda\left(\alpha\left(\pi_{4}\right)\right)=85 ;$
$\pi_{5}=\left(w_{1}, w_{3} ; J_{1}, J_{1}, J_{1}, J_{1}, J_{1}, J_{2}, J_{2}, J_{2}, J_{2}\right), \lambda\left(\alpha\left(\pi_{5}\right)\right)=112 ;$
Assume that the elite set $\Pi_{e}$ contains 4 individuals, $\pi_{1}-\pi_{4}$. It can be known that the sequence of operations corresponding to $\pi_{2} \in \Pi_{e}$ is $o\left(S_{o 2}\right)=$ $\left(O_{11}, O_{21}, O_{22}, O_{12}, O_{23}, O_{24}, O_{13}, O_{14}, O_{15}\right)$. Then, set the reference sequence of operations as $\Theta=\left(\mathrm{O}_{11}, \mathrm{O}_{12}, \mathrm{O}_{13}, \mathrm{O}_{14}, \mathrm{O}_{15}, \mathrm{O}_{21}, \mathrm{O}_{22}, \mathrm{O}_{23}, \mathrm{O}_{24}\right)$, and $\delta_{\pi_{1}}(i, j)$ can be calculated. For example, $\delta_{\pi_{1}}(3,7)=1$ since the 3 rd operation $O_{13}$ in $\Theta$

appears at the 7 th position in $o\left(S_{o 2}\right)$. Note that for $\pi_{2}$, its weight $\left(\lambda\left(\alpha\left(\pi_{w}\right)\right)-\right.$ $\left.\lambda\left(\alpha\left(\pi_{2}\right)+1\right) /\left(\lambda\left(\alpha\left(\pi_{w}\right)\right)-\lambda\left(\alpha\left(\pi_{b}\right)\right)+1\right)=0.92\right.$, hence, $\pi_{2}$ 's votes for $D_{37}$ is also 0.92 and the value of $D_{37}$ is increased by 0.92 . After all the individuals in the elite set $\Pi_{e}$ have voted, the final dominance matrix is obtained as follows:

$$
\left[\begin{array}{cccccccccc}
3.27 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0.47 & 0.88 & 1.92 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1.35 & 1 & 0 & 0.92 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0.47 & 1 & 1.8 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1.47 & 0 & 2.8 \\
0 & 2.8 & 0.47 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1.92 & 0 & 1.35 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0.92 & 1.88 & 0 & 0.47 & 0 \\
0 & 0 & 0 & 0 & 0 & 0.92 & 0.88 & 1 & 0.47
\end{array}\right]
$$

Inspired by [29], the longest common subsequence (LCS) is also embedded in the model to find good genes of two individuals.

A subsequence of a given sequence $X$ is the sequence $X$ with zero or more elements deleted. Given two sequences $X$ and $Y, Z$ is their common subsequence if $Z$ is a subsequence of both $X$ and $Y$. Let $\Gamma_{X Y}$ denote the set of all common subsequences of $X$ and $Y$. Then, the longest one in $\Gamma_{X Y}$ is called their longest common subsequence (LCS) [38].

The brutetorce procedure to solve the LCS problem is obviously of exponential complexity. A basic idea to simplify the procedure is using dynamic programming, which reduces its complexity to $O\left(L_{a} L_{b}\right)$, where $L_{a}$ and $L_{b}$ are the length of two given sequences, respectively. The readers can refer to [38] for details. Note that we also use the sequence of operations in the procedure to identify the repetitive parts.

# 3.3. Offspring reproduction and replacement 

In our EDA, each offspring is reproduced from the seed, while the set of seeds, denoted by $\Pi_{s}\left(\left|\Pi_{s}\right|=n_{s}\right)$, is extracted by the roulette method from

the current population. Let $\pi_{b}=\left(S_{r b}, S_{o b}\right)$ be the best individual found so far, and $\pi=\left(S_{r}, S_{o}\right) \in \Pi_{s}$ be a seed. The LCS of $o\left(S_{o}\right)$ and $o\left(S_{o b}\right)$ is considered as good genes, denoted as $\sigma_{L}$. Let $\pi_{f}=\left(S_{r f}, S_{o f}\right)$ be the offspring individual reproduced from $\pi$. It is reproduced as follows.

First, if $O_{i j} \in \sigma_{L}, t_{k}\left[O_{i j}\right]$ in $\alpha(\pi)$ is scheduled to the $k$ th position in $\alpha(\pi)$, 100 with a probability $p_{l}$ that depends on the length of $\sigma_{L}$. In this work, we define $p_{l}=\exp \left(\mu L\left(\sigma_{L}\right) / L_{o}\right)$, where $\mu=\log (0.8)$ is a constant, $L\left(\sigma_{L}\right)$ is the length of $\sigma_{L}$, and $L_{o}$ is the length of the sequence of operations. Let $\Psi_{u}$ be the set of unscheduled transitions in $\alpha(\pi)$.

Then, for each unassigned $q$ th position in $\alpha\left(\pi_{f}\right)$, select a transition $t_{p}\left[O_{u v}\right]$ randomly from $\Psi_{u}$ with probability $D_{p q} / \sum_{t_{k} \in \Psi_{u}} D_{k q}$, where $D_{i j}$ is the $(i, j)$ entry of $D$. At last, set the route information in $S_{o f}$ and the parts in $S_{o f}$ accordingly. When an offspring individual is reproduced, if it is better than the worst one and different from the others in the current population, replace the worst one with it. This replacement procedure apparently keeps the population 300 diversity while improving the popularity quality.

# 3.4. Local search 

To further improve the EDAs performance and prevent it from being stuck in local optima, a local search method, variable neighbourhood search (VNS), is employed. Once a new individual $\pi_{f}$ is produced, VNS is applied on it 30 with a probability $p_{v}=\min \{\max \{\exp (H / \gamma), \epsilon\}, 1\}$, where $\gamma$ and $\epsilon$ are constants with $\gamma=$ $0.2 \epsilon(\omega / 0.02)$ and $\epsilon=0.01, H=\left(\lambda\left(\alpha\left(\pi_{f}\right)\right)-\lambda\left(\alpha\left(\pi_{b}\right)\right)\right) / \lambda\left(\alpha\left(\pi_{b}\right)\right)$, and $\pi_{b}$ is the best solution found so far.

In this paper, two neighborhood structures, swap_local _search and insert_ local_search [28], are used in VNS. For a given individual, the former leads to some possible swapping pairs of parts, while the latter consists of some operations of inserting one part in front of another part. Since they both change the sequence of processing parts, the individuals generated by them may not be feasible. Amending infeasible individuals into feasible ones is a very time-

105 consuming procedure. Thus, to improve the search efficiency and ensure the feasibility of generated individuals at the same time, this work develops two new local searches based on the following Remarks.

Remark 1: Let $\pi=\left(S_{r} ; S_{o}\right)$ be a feasible individual and $\alpha(\pi)$ be the corresponding sequence of transitions. Each part $J_{i}$ appears $l\left(J_{i}\right)$ times in $S_{o}$ and each transition $t_{j k} \in T$ appears $g\left(w_{s}\right)$ times in $\alpha(\pi)$, where $g\left(w_{s}\right)$ is the number of parts processed by route $w_{s}$. Then, the swapping pairs of the same part $J_{i}$ at different positions in $S_{o}$, or the same transition $t_{j k}$ at different positions in $\alpha(\pi)$ do not change $\pi=\left(S_{r} ; S_{o}\right)$ and $\alpha(\pi)$.

Remark 2: Let $\pi=\left(S_{r} ; S_{o}\right)$ be a feasible individual and $\alpha(\pi)=t_{1} t_{2} \ldots t_{n}$. Let ${ }^{(p)} t$ and $t^{(p)}$ denote the sets of input and output operation places of transition $t$, respectively. For a transition $t_{k}$ in $\alpha(\pi k$, let $a_{\pi}(t)$ ) and $b_{\pi}\left(t_{k}\right)$ denote the minimum and maximum subscripts of transitions in ${ }^{\bullet}\left({ }^{(p)} t_{k}\right)$ and $\left(t_{k}^{(p)}\right)^{\bullet}$, respectively. Then, $t_{k}$ cannot fire before the firing of the transition with subscript $a_{\pi}\left(t_{k}\right)$ or after the firing of the transition with subscript $b_{\pi}\left(t_{k}\right)$ in $\alpha(\pi)$.

In swap_local_search, a pair of transitions $t_{i}\left[O_{p q}\right]$ and $t_{j}\left[O_{u v}\right]$ to be swapped must satisfy two constraints: $J_{p} \neq \mathcal{J}_{q}, t_{i} \neq t_{j}$ and $a_{\pi}\left(t_{j}\left[O_{u v}\right]\right)<i<b_{\pi}\left(t_{j}\left[O_{u v}\right]\right)$, $a_{\pi}\left(t_{i}\left[O_{p q}\right]\right)<j<b_{\pi}\left(t_{i}\left[O_{p q}\right]\right)$. The search stops if no better local optimum is found. The first new local search deadlock-free swap_local _search (DSLS) is stated as follows.

Example 4: Consider the PNS in Fig. 1. Let $\pi=\left(S_{r} ; S_{o}\right)=\left(w_{1}, w_{2}, w_{3} ; J_{1}, J_{1}\right.$, $\left.J_{3}, J_{2}, J_{5}, J_{3}, J_{1}, J_{2}, J_{1}, J_{2}, J_{2}, J_{1}, J_{2}, J_{3}\right)$ be an individual that is inputted to algorithm DSLS. Then $\alpha(\pi)=\left(t_{11}, t_{12}, t_{31}, t_{11}, t_{32}, t_{33}, t_{13}, t_{22}, t_{14}, t_{23}, t_{24}, t_{15}, t_{15}\right.$, $t_{34}$ ). At the beginning of DSLS, $i=1$ and $j=i+1 . J_{i}=J_{j}=J_{1}$. No operation swap $\Lambda(\pi ; i, j)$ is done.

For $i=9, j=13$, suppose that no better individual has been obtained, i.e., the swap moves will still be performed on $\pi$, with respect to $J_{1}$ in the $i$ th position and $J_{2}$ in the $j$ th position. Since $a_{\pi}\left(t_{i}\right)=7$ and $b_{\pi}\left(t_{i}\right)=13$, this swap move is unpermitted under the second condition of DSLS. In fact, this move will turn the individual into $\pi^{\prime}=\left(w_{1}, w_{2}, w_{3} ; J_{1}, J_{1}, J_{3}, J_{2}, J_{3}, J_{3}, J_{1}, J_{2}, \boldsymbol{J}_{2}, J_{2}, J_{2}, J_{1}, \boldsymbol{J}_{1}, J_{3}\right)$ (differences are shown in bold), which is not feasible and must be amended. Af-

# Algorithm 1 DSLS 

Input: a feasible individual $\pi_{c}$ and $\alpha\left(\pi_{c}\right)$;
set $\pi_{l}=\pi_{c} ; \alpha\left(\pi_{l}\right)=\alpha\left(\pi_{c}\right) ; i=1 ; / / \pi_{l}$ is the best individual found in DSLS
while termination criterion is not satisfied do
$j=i+1$; compute $a_{\pi_{l}}\left(t_{i}\left[O_{p q}\right]\right), b_{\pi_{l}}\left(t_{i}\left[O_{p q}\right]\right), a_{\pi_{l}}\left(t_{j}\left[O_{u v}\right]\right)$, and $b_{\pi_{l}}\left(t_{j}\left[O_{u v}\right]\right) ; / / t_{i}$ is the $i$ th transition in $\alpha\left(\pi_{l}\right)$
while $a_{\pi_{l}}\left(t_{i}\left[O_{p q}\right]\right)<j<b_{\pi_{l}}\left(t_{i}\left[O_{p q}\right]\right)$ do
if $J_{p} \neq J_{u}, t_{i} \neq t_{j}$, and $a_{\pi_{l}}\left(t_{j}\left[O_{u v}\right]\right)<i<b_{\pi_{l}}\left(t_{j}\left[O_{u v}\right]\right)$ then
$\pi_{t}=\Lambda\left(\pi_{l} ; i, j\right) ; / / \Lambda$ permutes the parts in positions $j$ and $j$ in $\pi_{l}$
amend $\pi_{t}$ and $\alpha\left(\pi_{t}\right)$;
if $\lambda\left(\alpha\left(\pi_{t}\right)<\lambda\left(\alpha\left(\pi_{l}\right)\right.\right.$ then
$\pi_{l}=\pi_{t} ; \alpha\left(\pi_{l}\right)=\alpha\left(\pi_{t}\right) ; i=1 ; 2 \neq i \neq 1 ;$
else
$j=j+1 ;$
end if
else
$j=j+1 ;$
end if
end while
Output: $\pi_{l}$ and $\alpha\left(\pi_{l}\right)$;

ter that, we have the amended individual $\pi^{\prime \prime}=\left(w_{1}, w_{2}, w_{3} ; J_{1}, J_{1}, J_{3}, J_{2}, J_{3}, J_{3}\right.$, $\left.J_{1}, J_{2}, J_{1}, J_{2}, J_{2}, \boldsymbol{J}_{2}, \boldsymbol{J}_{1}, J_{3}\right)$ and its corresponding sequence of transitions is the same as $\alpha(\pi)=\left(t_{11}, t_{12}, t_{31}, t_{11}, t_{32}, t_{33}, t_{13}, t_{22}, t_{14}, t_{23}, t_{24}, t_{15}, t_{15}, t_{34}\right)$. Such situations are apparently invalid and hence must be prevented by DSLS.

In insert_local_search, for the transition $t_{i}\left[O_{p q}\right]$ that is to be inserted to the front of $t_{j}\left[O_{u v}\right]$ in $\alpha(\pi)$, only one constraint is required: $a_{\pi}\left(t_{i}\left[O_{p q}\right]\right)$ $b_{\pi}\left(t_{i}\left[O_{p q}\right]\right)$. The search stops if no better local optimum is found. The second new local search deadlock-free insert_local_search (DILS) can be established as follows.

# Algorithm 2 DILS 

Input: a feasible individual $\pi_{c}$ and $\alpha\left(\pi_{c}\right)$;
set $\pi_{l}=\pi_{c} ; \alpha\left(\pi_{l}\right)=\alpha\left(\pi_{c}\right) ; i=1 ; / / \pi_{l}$ is the best-individual/ found in DILS
while termination criterion is not satisfied do
$j=1$; compute $a_{\pi_{l}}\left(t_{i}\left[O_{p q}\right]\right)$ and $b_{\pi_{l}}\left(t_{i}\left[O_{p q}\right]\right) ; / / \pi_{l}$ is the $i$ th transition in $\alpha\left(\pi_{l}\right)$
while $a_{\pi_{l}}\left(t_{i}\left[O_{p q}\right]\right)<j<b_{\pi_{l}}\left(t_{i}\left[O_{p q}\right]\right)$ do
$\pi_{i}=\Delta\left(\pi_{l} ; i, j\right) ; / /$ operator $\Delta$ inserts the $i$ th part to position $j$ in $\pi_{l}$
amend $\pi_{l}$ and $\alpha\left(\pi_{l}\right)$;
if $\lambda\left(\alpha\left(\pi_{i}\right)<\lambda\left(\alpha\left(\pi_{l}\right)\right.\right.$ then
$\pi_{l}=\pi_{t} ; \alpha\left(\pi_{l}\right)=\alpha\left(\pi_{l}\right) ; j=i-1 ; j=1 ;$
else
$j=j+i-1$
end if
end while
$i=1 ; j=2 ;$
end if
end while
Output: $\pi_{l}$ and $\alpha\left(\pi_{l}\right)$;
According to these two new local searches, the swap and insert operations are performed within proper domains that are determined by the characteristics

(Remarks 1 and 2) of the concerned system. Thus, a number of invalid operations are avoided and the local search efficiency is therefore improved. In the following, a new Modified VNS (MVNS) is developed based on DSLS and DILS.

# Algorithm 3 MVNS 

Input: an offspring individual $\pi_{f}$ and $\alpha\left(\pi_{f}\right)$;
set $\pi_{v}=\pi_{c}=\pi_{f} ; \alpha\left(\pi_{v}\right)=\alpha\left(\pi_{c}\right)=\alpha\left(\pi_{f}\right) ; / / \pi_{v}$ is the best individual found in MVNS
while termination criterion is not satisfied do
repeat
$\lambda_{1}=\lambda\left(\alpha\left(\pi_{c}\right)\right) ;\left(\pi_{d}, \alpha\left(\pi_{d}\right)\right)=\operatorname{DSLS}\left(\pi_{c}, \alpha\left(\pi_{c}\right)\right)$;
$\left(\pi_{c}, \alpha\left(\pi_{c}\right)\right)=\operatorname{DILS}\left(\pi_{d}, \alpha\left(\pi_{d}\right)\right) ; \lambda_{2}=\lambda\left(\alpha\left(\pi_{d}\right)\right)$;
until $\lambda_{1} \geq \lambda_{2}$
if $\lambda\left(\alpha\left(\pi_{c}\right)\right)<\lambda\left(\alpha\left(\pi_{v}\right)\right)$ then
$\pi_{v}=\pi_{c}, \alpha\left(\pi_{v}\right)=\alpha\left(\pi_{c}\right)$;
end if
choose two different positions randomly in $\pi_{c}$ and permute the parts in these two positions;
amend $\pi_{c}$ and $\alpha\left(\pi_{c}\right)$;
end while
Output: $\pi_{v}$ and $\alpha\left(\pi_{v}\right)$
In MVNS, DSLS and DILS are used alternately starting from $\pi_{f}$ until no better solution is found. If the so-obtained solution is better than the best solution $\pi_{v}$ found so far, the former replaces the latter and the number of iterations is needed. 0 . Otherwise, the number of iterations increases by one. Next, choose two different parts in $\pi_{v}$ randomly and permute them. The whole procedure is repeated until the maximal number of iterations $I_{m}$ is reached. Here, the deadlock controller is embedded such that the solutions obtained by MVNS are feasible.

# 3.5. The hybrid scheduling algorithm 

By embedding MVNS and the deadlock controller into EDA, a novel hybrid scheduling algorithm DEDA_MVNS is developed. The algorithm terminates when a given time for computation is reached. Let $K$ denote the population size, the proposed scheduling algorithm is described as follows.

## Algorithm 4 DEDA_MVNS

Input: parameters $K, n_{e}, n_{s}$;
generate an initial population $\Pi_{c}$ with $K$ individuals randomly; select the best $n_{e}$ individuals as $\Pi_{e}$; let $\pi_{b}$ be the best individual in $\Pi_{c}$; while termination criteria are not met do
construct $D$ from $\Pi_{e}$;
let $\Pi_{s}$ be the set of $n_{s}$ individuals selected by redo the method from $\Pi_{c}$;
for each $\pi \in \Pi_{s}$ do
construct LCS of $\pi$ and $\pi_{b}$;
reproduce offspring individual $\pi_{f}$ based on $\pi_{f}$ and $D$;
perform MVNS on $\pi_{f}$ with probability $p_{c}$;
if $\lambda\left(\alpha\left(\pi_{f}\right)\right)<\lambda\left(\alpha\left(\pi_{w}\right)\right)$ and $\pi_{f}$ does not exist in $\Pi_{c}$ then replace $\pi_{w}$ with $\pi_{f} ; / / \pi_{w}$ is the worst individual in $\Pi_{c}$;
end if
end for
update $\Pi_{c}$ and $\pi_{f}$
end while
Output: $\pi_{f}$ and $\alpha\left(\pi_{f}\right)$;
4. Computational results

In this paper, a widely researched FMS [5-9, 20-25] is used to test the performance of the proposed algorithms. As seen in Fig. 2, this FMS contains 4 machines $m_{1}-m_{4}$ and 3 robots $r_{1}-r_{3}$, and is able to process 3 types of parts $J_{1}-J_{3}$. Its PNS is shown in Fig. 3. The processing time of parts is taken from [20] and shown in Table 1. 16 benchmark instances from [21] based on the PN

![img-1.jpeg](img-1.jpeg)

Figure 2: An example of FMS
model of this FMS are tested. According to the resource capacities $\left(C\left(m_{i}\right)\right.$, $i=1,2,3,4$, and $\left.C\left(r_{i}\right)\right)$ , $i=1,2,3$ ), these 16 instances are divided into 4 groups. Each group contains 4 instances with the numbers of type- $J_{1}, J_{2}$, and $J_{3}$ parts $(8,12,8),(10,20,10),(15,20,15)$, and $(20,20,20)$, respectively.

1. In01-In04: $C\left(m_{i}\right)=2$ and $C\left(r_{i}\right)=1$;
2. In01-In04: $C\left(m_{i}\right)=2$ and $C\left(r_{i}\right)=2$;
3. In04-In12: $C\left(m_{i}\right)=3$ and $C\left(r_{i}\right)=2$;
4. In13-In16: $C\left(m_{i}\right)=3$ and $C\left(r_{i}\right)=3$.

In the following, we first test the proposed hybrid algorithm and stand-alone ones, then compare the hybrid one with other existing works. All the algorithms are coded in $\mathrm{C}++$ and run on a desktop PC with 3.2 GHz processor and 8 GB memory.

Table 1: Processing time for the FMS in Fig. 2

| Type- $J_{1}$ | Type- $J_{2}$ |  | Type- $J_{3}$ |
| :--: | :--: | :--: | :--: |
| $w_{1}$ | $w_{2}$ | $w_{3}$ | $w_{4}$ |
| $O_{11}: 8$ | $O_{21}: 4$ | $O_{21}: 4$ | $O_{41}: 5$ |
| $O_{12}: 34$ | $O_{22}: 32$ | $O_{32}: 23$ | $O_{12}: 22$ |
| $O_{13}: 5$ | $O_{23}: 8$ | $O_{33}: 6$ | $O_{43}: 4$ |
|  | $O_{24}: 38$ | $O_{34}: 20$ | $O_{44}: 17$ |
|  | $O_{25}: 5$ | $O_{25}: 5$ | $O_{25}: 6$ |

![img-2.jpeg](img-2.jpeg)

Figure 3: PNS of the FMS in Fig. 2

Table 2: Scheduling results of hybrid algorithms and stand-alone ones

|  | DEDA |  | VNS |  | MVNS |  | DEDA_VNS |  | DEDA_MVNS |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Instance | Best | Average | Best | Average | Best | Average | Best | Average | Best | Average |
| Iso01 | 348 | 385.8 | 298 | 307.45 | 296 | 303.45 | 287 | 287.5 | 280 | 287.45 |
| Iso02 | 490 | 554.5 | 434 | 450.0 | 422 | 436.55 | 398 | 411.05 | 377 | 397.35 |
| Iso03 | 621 | 691.85 | 549 | 586.95 | 533 | 568.6 | 488 | 522.3 | 483 | 517.6 |
| Iso04 | 772 | 852.9 | 663 | 705.9 | 653 | 692.95 | 609 | 634.4 | 587 | 619.95 |
| Iso05 | 299 | 321.0 | 252 | 261.75 | 249 | 258.2 | 224 | 233.75 | 225 | 231.45 |
| Iso06 | 411 | 470.25 | 370 | 392.85 | 358 | 376.15 | 340 | 355.65 | 321 | 332.35 |
| Iso07 | 510 | 579.3 | 442 | 476.5 | 420 | 458.05 | 412 | 429.3 | 395 | 412.75 |
| Iso08 | 643 | 720.65 | 558 | 584.65 | 544 | 570.2 | 517 | 538.85 | 493 | 519.65 |
| Iso09 | 247 | 275.4 | 197 | 208.6 | 198 | 206.5 | 174 | 185.3 | 168 | 178.3 |
| Iso10 | 340 | 389.45 | 286 | 307.25 | 287 | 306.15 | 252 | 260.4 | 242 | 252.95 |
| Iso11 | 349 | 385.8 | 298 | 307.45 | 296 | 303.45 | 287 | 297.45 | 280 | 287.45 |
| Iso12 | 452 | 521.05 | 356 | 375.2 | 348 | 365.35 | 323 | 337.75 | 309 | 319.0 |
| Iso13 | 232 | 256.2 | 183 | 194.8 | 184 | 193.2 | 163 | 193.2 | 163 | 169.1 |
| Iso14 | 319 | 355.3 | 259 | 280.75 | 250 | 269.75 | 242 | 250.85 | 224 | 233.55 |
| Iso15 | 424 | 478.45 | 332 | 358.35 | 319 | 338.8 | 289 | 304.75 | 276 | 291.7 |
| Iso16 | 523 | 584.0 | 411 | 426.2 | 399 | 425.5 | 363 | 411.5 | 346 | 361.8 |

# 4.1. Scheduling results of hybrid algorithms and stand-alone ones 

To demonstrate the effectiveness of our proposed algorithms, DEDA, VNS, MVNS, DEDA_VNS, and DEDA_MVNS are tested and compared. The population sizes for instances with $28,40,50$, and 60 parts are $K=100,200,200$, 448 and 300, respectively. For each instance, the elite and seed sets both have sizes $0.1 \times K$, i.e., $n_{e}=n_{s}=0.1 \times K$. The maximal iteration number $I_{m}$ for VNS or MVNS is set as 50 . To guarantee the comparisons fairness, the termination criterion of different algorithms are all set as a maximum execution time of $40 \times N_{j}$ seconds, for the same instance, where $N_{j}$ is the number of total parts.
440 The simulation results are shown in Table 2, where Best and Average are the best and average makespans among 20 random trials, respectively.

The results show that the hybrid algorithms DEDA_VNS and DEDA_MVNS outperform the stand-alone ones, DEDA, VNS, and MVNS, for all 16 instances. Most significantly improved results of the hybrid algorithms appear in instances with larger lot sizes. The effects of the modification on the local search methods can be demonstrated by the comparison between the results of VNS and MVNS. According to Table 2, MVNS finds better results for 13 instances out of 16, while VNS is preferable for only 3 instances. The similar situation also occurs

![img-3.jpeg](img-3.jpeg)

Figure 4: Standard deviations of a floating results in Table 2.
in the comparison among the hybrid algorithms. DEDA_MVNS provides the best results for 15 instances out of 16 , while DEDA_VNS provides only 2. These improvements may be attributed to our modified MVNS that constrain the swap and insert operations in the proper domains to improve the search efficiencies.

The standard deviations of five algorithms for these 16 instances are shown in Fig. 4. It can be seen that DEDA_VNS and DEDA_MVNS significantly 405 outperforms DEDA, VNS, and MVNS with respect to the standard deviation. This means the stand-alone algorithms become more robust if combining with others.
4.7. Comparing with other works

In this subsection, the proposed DEDA_MVNS is compared with four existing approaches, $\mathrm{D}^{2}$ WS [22], ALS [23], DDE_VNS [24], and HPSO [25], for the 16 instances in Sect. 4.1. The computational results of $\mathrm{D}^{2} \mathrm{WS}$, ALS, DDE_VNS, and HPSO are directly from the respective papers. The computational results

Table 3: Scheduling results of DEDA_MVNS and existing approaches.

|  | DEDA_MVNS |  | HPSO |  | DDE_VNS |  | ALS |  | $\mathrm{D}^{2} \mathrm{WS}$ |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Instance | Best | Average | Best | Average | Best | Average | Best | Average | Best | Average |
| Iso01 | 280 | 287.45 | 283 | 291.5 | 288 | 295.5 | 293 | $/$ | 303 | 334.2 |
| Iso02 | 377 | 397.35 | 384 | 406.65 | 389 | 403.4 | 397 | $/$ | 426 | 454.9 |
| Iso03 | 483 | 517.3 | 485 | 525.05 | 483 | 521.55 | 490 | $/$ | 539 | 581.4 |
| Iso04 | 587 | 619.9 | 617 | 650.7 | 605 | 639.05 | 587 | $/$ | 672 | 702.9 |
| Iso05 | 225 | 231.65 | 224 | 231.5 | 226 | 232.7 | 266 | $/$ | 252 | 272.9 |
| Iso06 | 321 | 332.3 | 323 | 333.7 | 365 | 379.2 | 368 | $/$ | 369 | 397.6 |
| Iso07 | 396 | 412.7 | 404 | 420.9 | 416 | 431.75 | 450 | $/$ | 449 | 483.1 |
| Iso08 | 494 | 515.65 | 499 | 523.25 | 548 | 566.05 | 569 | $/$ | 570 | 609.9 |
| Iso09 | 168 | 178.3 | 168 | 177.6 | 188 | 192.1 | 196 | $/$ | 194 | 207.6 |
| Iso10 | 242 | 252.95 | 245 | 254.15 | 252 | 261.4 | 269 | $/$ | 269 | 286.5 |
| Iso11 | 309 | 319.0 | 313 | 323.4 | 346 | 365.45 | 332 | $/$ | 343 | 367.1 |
| Iso12 | 373 | 398.05 | 380 | 401.1 | 394 | 412.5 | 409 | $/$ | 397 | 440.2 |
| Iso13 | 163 | 169.1 | 158 | 162.3 | 158 | 162.3 | 186 | $/$ | 182 | 193.0 |
| Iso14 | 224 | 233.55 | 221 | 232.0 | 251 | 267.5 | 272 | $/$ | 246 | 261.5 |
| Iso15 | 276 | 291.7 | 281 | 295.25 | 287 | 308.25 | 327 | $/$ | 305 | 330.6 |
| Iso16 | 346 | 361.8 | 346 | 363.4 | 355 | 382.15 | 369 | $/$ | 359 | 385.5 |

are summarized in Table 3. Note that only the best makespans of ALS are provided.

As seen in Table 3, the proposed DEDA_MVNS provides the best solutions for 13 of 16 instances among the five approaches while HPSO, DDE_VNS, and ALS provide 5, 2, and 1, respectively. Moreover, DEDA_MVNS outperforms $\mathrm{D}^{2} \mathrm{WS}$ for all the instances. It appears that DEDA_MVNS outperforms these existing approaches especially for the instances with larger lot sizes and stricter resource constraints.

A non-parametric Friedman's test is also applied to the BSTs of the five different approaches (DEDA_MVNS, HPSO, DDE_VNS, ALS and $\mathrm{D}^{2} \mathrm{WS}$ ) to clarify whether there are statistical differences among the results. A level $\alpha=0.05$ of significance is set. The statistical test shows that significant differences exist among the results of these approaches. Therefore, a multiple comparison proposed by [39] is carried out to decide which approach is better. The significance level is also set to $\alpha=0.05$. The comparisons show that DEDA_MVNS and HPSO outperforms ALS and $\mathrm{D}^{2} \mathrm{WS}$ significantly while DEDA_MVNS outperforms DDE_VNS. No statistical differences are found between other pairs.

The computational cost comparison is shown in Table 4. Note that only

Table 4: Execution time of DEDA_MVNS, HPSO and ALS.

| Instance | Execution time (seconds) |  |  |
| :--: | :--: | :--: | :--: |
|  | DEDA_MVNS | HPSO | ALS |
| In01 | 1120 | 1400 | 2436 |
| In02 | 1600 | 2000 | 1637 |
| In03 | 2000 | 2500 | 587 |
| In04 | 2400 | 3000 | 3058 |
| In05 | 1120 | 1400 | 403 |
| In06 | 1600 | 2000 | 5506 |
| In07 | 2000 | 2500 | 853 |
| In08 | 2400 | 3000 | 292 |
| In09 | 1120 | 1400 | 876 |
| In10 | 1600 | 2000 | 1931 |
| In11 | 2000 | 2500 | 1024 |
| In12 | 2400 | 3000 | 1889 |
| In13 | 1120 | 1400 | 3237 |
| In14 | 1600 | 2000 | 1742 |
| In15 | 2000 | 2500 | 1399 |
| In16 | 2400 | 3000 | 1353 |

the shortest ( 178 seconds for In14) and longest ( 1900 seconds for In 16) execution time of $\mathrm{D}^{2} \mathrm{WS}$ were specifically given, and the execution time of DDE_VNS were not reported in [24]. Hence, only the execution time (in seconds) of three scheduling approaches, DEDA_MVNS, HPSO and ALS, are listed in Table 4.
${ }_{45}$ Note that DEDA_MVNS and HPSO terminate when some given maximum execution time reaches a while ALS terminates when its two upper bounds converge or some given maximum execution time reaches [23, 25]. The comparison shows that ALS and DEDA_MVNS cost the least time for 10 and 6 instances out of 16 , respectively. Non-parametric Friedman's test $(\alpha=0.05)$ shows that significant differences exist among the execution time of three approaches. Multiple comparisons [39] $(\alpha=0.05)$ show that DEDA_MVNS and ALS cost less time than HPSO significantly while no statistical difference is found between DEDA_MVNS and ALS. Additionally, the execution time of $\mathrm{D}^{2} \mathrm{WS}$ in most instances are less than 800 seconds [22]. Thus, it can be concluded that $\mathrm{D}^{2} \mathrm{WS}$ performs the best in the computational efficiency, followed by two algorithms at

the same level, ALS and DEDA_MVNS, while HPSO performs the worst among the four.

# 5. Conclusions 

In this paper, a novel scheduling algorithm DEDA_MVNS using PNs and 501 EDA is developed for the FMSs. Permutations with repetitions for parts are used to represent the individuals and the feasibility of each individual is guaranteed by a highly permissiveness deadlock controller. The probabilistic model in DEDA_MVNS is constructed by the voting procedure and the LCS is incorporated in the model for mining excellent genes. The LCS of the sequences of 501 operations of the seed individual that is selected from the current population by the roulette method, and the best individual found so far, are treated as excellent genes. A local search method MVNS, in which the domains of the swap and insert operations are constrained, is also introduced as an efficiency enhancement for improving the performance.

Experimental results show that the proposed scheduling algorithm outperforms all the existing ones on the benchmark examples. It may be owing to the use of the probability distribution model that can mine desired genes, and the modified local search method MVNS that prevents the algorithm from trapping into local optimum. More studies about the practical effects of these two 515 procedures are required in the future.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China under Grants 61573278.

## References

[1] Narciso ME, Piera MA, Guasch A, A time stamp reduction method for state space exploration using colored Petri nets. Simulation 88(5) (2012) 592-616

[2] Pang CK, Cao VL, Optimization of total energy consumption in flexible manufacturing systems using weighted p-timed Petri nets and dynamic programming. IEEE T Autom Sci Eng 11(4) (2014) 1083-1096
[3] Li XL, Xing KY, Wu YC, Wang XN, Luo JC, Total Energy Consumption Optimization via Genetic Algorithm in Flexible Manufacturing Systems, Comput Ind Eng 104 (2017) 188-200
[4] Xiong HH, Zhou MC, Scheduling of Semiconductor Test Facility via Petri Nets and Hybrid Heuristic Search. IEEE T Semiconduct M 41(3) (1998) 384393
[5] Ezpeleta J, Colom J, Martinez J A, Petri-Net-Based Deadlock Prevention Policy for Flexible Manufacturing Systems. IEEE T Robot Autom 11(2) (1995) $173-184$
[6] Huang YS, Jeng MD, Xie XL, Chung SL, Deadlock prevention policy based on Petri nets and siphons. Int J Prot Res 39(2) (2001) 283-305
[7] Piroddi L, Cordone R, Furnagalli J, Selective Siphon Control for Deadlock Prevention in Petri Nets. IEEE T Syst Man Cy A 38(6) (2008) 1337-1348
[8] Xing KY, Zhou MC, Liu HX, Tian F, Optimal Petri-Net-Based PolynomialComplexity Deadlock Avoidance Policies for Automated Manufacturing Systems. IEEE T Syst Man Cy A 39(1) (2009) 188-199
[9] Lin HX, Xing KY, Zhou MC, Han LB, Wang F, Transition Cover-Based Design of Petri Net Controllers for Automated Manufacturing Systems. IEEE T Syst Man Cy-S 44(2) (2014) 196-208
[10] Feng YX, Xing KY, Gao ZX, Wu YC, Transition Cover-Based Robust Petri Net Controllers for Automated Manufacturing Systems With a Type of Unreliable Resources. IEEE T Syst Man Cy-S 10.1109/TSMC.2016.2558106
[11] Sakhaii M, Tavakkoli-Moghaddam R, Bagheri M, Vatani B, A robust optimization approach for an integrated dynamic cellular manufacturing system

and production planning with unreliable machines. Appl Math Model 40(1) (2016) $169-191$
[12] Azadeh A, Ravanbakhsh M, Rezaei-Malek M, Sheikhalishahi M, TaheriMoghaddam A, Unique NSGA-II and MOPSO algorithms for improved dynamic cellular manufacturing systems considering human factors. Appl Math Model 48 (2017) 655-672
[13] Allahverdi A, Aydilek H, Aydilek A, Two-stage assembly scheduling problem for minimizing total tardiness with setup times. Appl Math Model 40(1718) (2016) $7796-7815$
[14] Karimi S, Ardalan Z, Naderi B, Mohammadi M, Scheduling flexible jobshops with transportation times: Mathematical models and a hybrid imperialist competitive algorithm. Appl Math Model 41 (2016) 667-682
[15] Ham A, Flexible job shop scheduling problem for parallel batch processing machine with compatible job families. Appl Math Model 45 (2017) 551-562
[16] Sethi SP, Sriskandarajah C, Sorger G, Blazewicz J, Kubiak W, Sequencing of parts and robot moves in a robotic cell. Int J Flex Manuf Sys 4(3) (1992) $331-358$.
[17] Ramaswamy SE, Joshi SB, Deadlock-free schedules for automated manufacturing workstations. IEEE T Robot Autom 12(3) (1996) 391-400
[18] Abdallah B, Elmaraghy HA, Elmekkawy T, Deadlock-free Scheduling in Flexible Manufacturing Systems Using Petri Nets. Int J Prod Res 40(12) (2002) $2733-2756$
[19] Dashora Y, Kumar S, Tiwari MK, Newman ST, Deadlock-free scheduling of an automated manufacturing system using an enhanced colored time resource Petri-net model-based Evolutionary Endosymbiotic Learning Automata approach. Int J Flex Manuf Sys 19(4) (2007) 486-515

[20] Xing KY, Han LB, Zhou MC, Wang F, Deadlock-Free Genetic Scheduling Algorithm for Automated Manufacturing Systems Based on Deadlock Control Policy. IEEE T Syst Man Cy B 42(3) (2012) 603-615
[21] Han LB, Xing KY, Chen X, Lei H, Wang F, Deadlock-free Genetic Scheduling for Flexible Manufacturing Systems using Petri Nets and Deadlock Controllers. Int J Prod Res 52(5) (2014) 1557-1572
[22] Luo JC, Xing KY, Zhou MC, Li XL, Wang XN, Deadlock-Free Scheduling of Automated Manufacturing Systems Using Petri Nets and Hybrid Heuristic Search. IEEE T Syst Man Cy-S 45(3) (2015) 530-541
[23] Baruwa OT, Piera MA, Guasch A, Deadlock-Free Scheduling Method for Flexible Manufacturing Systems Based on the Tuned Colored Petri nets and Anytime Heuristic Search. IEEE T Syst Man Cy-S 45(5) (2015) 831-846
[24] Lei H, Xing KY, Gao ZX, Xiong FL, Hybrid Discrete Differential Evolution Algorithm for Deadlock-free Scheduling with Setup Times of Flexible Manufacturing Systems. T I Mise Control 38(10) (2016) 1270-1280
[25] Han, L. B., K. Y. Xing, X. Chen and F. L. Xiong, A Petri Net-based Particle Swarm Optimization Approach for Scheduling Deadlock-prone Flexible Manufacturing Systems. J Intell Manuf doi:10.1007/s 10845-015-1161-2
[26] Mühlenbein H, Baaß G, From Recombination of Genes to the Estimation of Distributions I. Binary Parameters. in: Parallel Problem Solving from Nature Springer, New York, (1998) 178-187
[27] Larianaga P, Lozano JA, Estimation of Distribution Algorithms: a new tool for evolutionary computation. Kluwer Academic Publishers, Boston, (2002)
[28] Jarboui B, Eddaly M, Siarry P, An Estimation of Distribution Algorithm for Minimizing the Total Flowtime in Permutation Flowshop Scheduling Problems. Comput Oper Res 36(9) (2009) 2638-2646

[29] Zhang Y, Li XP, Estimation of Distribution Algorithm for Permutation Flowshops with Total Flowtime Minimization. Comput Ind Eng 60(4) (2011) $706-718$
[30] Ceberio J, Irurozki E, Mendiburu A, Lozano JA, A Distance-based Ranking Model Estimation of Distribution Algorithm for the Flowshop Scheduling Problem. IEEE T Evolut Comput 18(2) (2014) 286-300
[31] Liang XL, Chen HP, Lozano JA, A Boltzmann-based Estimation of Distribution Algorithm for a General Resource Scheduling Model. IEEE T Evolut Comput 19(6) (2015) 793-806
[32] Lozano JA, Larranaga P, Inza I, Bengoetxea E, Tswards a New Evolutionary Computation: Advances on Estimation of Distribution Algorithms. Springer, New York, (2006)
[33] Murata T, Petri Nets: Properties, Analysis, and Applications. In Proc IEEE 77 (1989) 541-580
[34] Zurawski R, Zhou MC, Petri nets and industrial applications: A tutorial. IEEE T Ind Electron, 41(6) (1994) 567-583
[35] Popova-Zeugmann J, Turic and Petri Nets. Springer, Berlin Heidelberg, (2013)
[36] Hauschild M, Pelikan M, An Introduction and Survey of Estimation of Distribution Algorithms. Swarm Evolut Comput 1(3) (2011) 111-128
[37] Chang PC, Chen SH, Liu CH, Sub-population Genetic Algorithm with Mining Gene Structures for Multiobjective Flowshop Scheduling Problems. Expert Syst Appl 33(3) (2007) 762-771
[38] Cormen TH, Leiserson CE, Rivest RL, Stein C, Introduction to Algorithms, 3rd edition. MIT Press, Massachusetts, (2009)
[39] Hollander M, Wolfe DA, Nonparametric Statistical Methods. Wiley, New York, (1973)