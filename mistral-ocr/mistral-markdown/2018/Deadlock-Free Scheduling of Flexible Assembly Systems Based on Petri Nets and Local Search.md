# Deadlock-Free Scheduling of Flexible Assembly Systems Based on Petri Nets and Local Search 

JianChao Luo, ZhiQiang Liu, MengChu Zhou ${ }^{\circledR}$, Fellow, IEEE, and KeYi Xing


#### Abstract

Deadlock-free scheduling and control is critical for optimizing the performance of flexible assembly systems (FASs). Based on the Petri net models of FASs, this paper integrates a deadlock prevention policy with local search and develops a novel deadlock-free scheduling algorithm. A solution of the scheduling problem is coded as a chromosome representation that is a permutation with repetition of parts. By using the deadlock prevention policy, a repairing algorithm (RA) is developed to repair unfeasible chromosomes. A perturbation strategy based on estimation of distribution algorithm is developed to escape from local optima. Moreover, to improve population diversity, an acceptance criterion (AC) based on Pareto dominance is proposed. The chromosome representation, RA, perturbation strategy, and AC together support the cooperative aspect of local search for scheduling problems strongly.


Index Terms—Deadlock prevention policy, flexible assembly system (FAS), local search, Petri net (PN), scheduling.

## NOMENCLATURE

$N \quad\left(P \cup P_{s} \cup P_{e} \cup P_{R}, T, F\right)$, an assembly PN.
$P \quad$ Set of activity (operation) places.
$P_{s} \quad$ Set of start activity places.
$P_{e} \quad$ Set of end activity places.
$P_{R} \quad$ Set of resource places.
$[N] \quad$ Incidence matrix of $N$.
$\mathbb{R}(N, M)$ Set of all reachable markings of $N$ from $M$.
$M(S) \quad \Sigma_{p \in S} M(p)$, where $S$ is a set of places.
$\mathbb{Z} \quad$ Set of integers.
$\mathbb{N} \quad\{0,1,2, \ldots\}$.
Manuscript received February 25, 2018; revised April 13, 2018; accepted June 28, 2018. This work was supported in part by the Fundamental Research Funds for the Central Universities under Grant 3102017OQD110, in part by the Aviation Science Foundation of China under Grant 2015ZD53050, in part by the National Defense Basic Scientific Research Program under Grant N2016KD0003, and in part by the National Natural Science Foundation of China under Grant 61573278. This paper was recommended by Associate Editor M. K. Tiwari. (Corresponding authors: ZhiQiang Liu; MengChu Zhou.)
J. Luo and Z. Liu are with the School of Software and Microelectronics, Northwestern Polytechnical University, Xi’an 710072, China (e-mail: luojianchao@nwpu.edu.cn; zqluo@nwpu.edu.cn).
M. Zhou is with the Department of Electrical and Computer Engineering, New Jersey Institute of Technology, Newark, NJ 07102 USA and also with the Institute of Systems Engineering, Macau University of Science and Technology, Macau 999078, China (e-mail: zhou@njit.edu).
K. Xing is with the State Key Laboratory for Manufacturing Systems Engineering, Xi'an Jiaotong University, Xi'an 710049, China, and also with the Systems Engineering Institute, Xi'an Jiaotong University, Xi'an 710049, China (e-mail: kysing@sei.xjtu.edu.cn).
Digital Object Identifier 10.1109/TSMC.2018.2855685

| $\mathbb{N}^{+}$ | $\{1,2,3, \ldots\}$ |
| :-- | :-- |
| $\mathbb{N}_{k}$ | $\{1,2, \ldots, k\}$ |
| $\|\Delta\|$ | Support of a P-vector $\Delta$ in N. |
| $N^{-1}$ | $\left(P \cup P_{s} \cup P_{e} \cup P_{R}, T, F^{-1}\right)$, reverse of $N$. |
| $F^{-1}$ | $\{(x, y) \mid(y, x) \in F\}$, the set of arcs in $N^{-1}$. |
| $f(x)$ | A vertex $x \in P \cup P_{s} \cup P_{e} \cup P_{R} \cup T$ in $N^{-1}$. |
| $d(p)$ | Processing time of the activity modeled by $p$. |
| $\wp(\pi)$ | Set of places in A-chain $\pi$. |
| $\mathfrak{J}(\pi)$ | Set of transitions in A-chain $\pi$. |
| $R(\pi)$ | Set of all resource types required by places |
|  | in $\wp(\pi)$. |
| span $(s)$ | Makespan of schedule $s$. |
| $o(\Gamma)$ | Sequence of activities corresponding to chromo- |
|  | some $\Gamma$. |
| $\alpha(\Gamma)$ | Sequence of transitions corresponds to $\Gamma$. |

## I. INTRODUCTION

AN AUTOMATED manufacturing system (AMS) is a computer-controlled system that exhibits a high degree of resource sharing. It consists of a finite set of resources and can process different kinds of parts based on a prescribed sequence of operations. Its interacting parts and shared resources may lead to deadlock states under which the system remains indefinitely blocked and cannot terminate its tasks. Therefore, developing efficient control and scheduling algorithms to avoid deadlocks while optimizing system performance is significant.

The deadlock control problem of AMSs without assembly processes has been extensively studied, and many deadlock control policies have been proposed [3], [4], [7], [9], [10], [17], [19], [20], [22], [29], [31], [32], [36], [38], [40], [42], [45]-[47], [60]. More detailed review can be found in [48]. These policies can ensure the deadlock-free operation of AMSs. As they do not take the processing time into consideration, their operational performance is not guaranteed. Thus, deadlock-free scheduling of such systems is still an open field. Because of its NP-hard nature [2], [41], only a few researchers address it [1], [2], [11], [21], [24], [33]-[35], [37], [41], [61]. Ramasway and Joshi [24] provide a mathematical model for deadlock-free scheduling problems of AMSs with material handing devices and limited buffers and use a Lagrangian relaxation heuristic to simplify the model to search for the optimized average flow time. Abdallah et al. [1] use timed Petri nets (PNs) to model AMSs and propose a deadlockfree scheduling algorithm. It generates a partial reachability

graph to find the optimal or near-optimal deadlock-free schedule. Gang and Wu [37] develop a genetic algorithm based on PN with infinity buffers to find a schedule, analyze deadlocks that may occur with the schedule, and add some necessary buffers to avoid the deadlocks. Wu and Zhou [33] develop colored-timed resource-oriented PNs to model AMSs that are failure-prone. Based on the developed model and a deadlock control policy, heuristic rules are proposed to schedule the system in real time. Xing et al. [41] embed a deadlock avoidance policy into a genetic algorithm and develop a deadlock-free genetic algorithm for AMSs. Based on the deadlock search algorithm in [40], a one-step look-ahead method is developed to amend infeasible solutions into feasible ones. The latest scheduling algorithms for AMSs can be found in [62]-[66].
In contrast, few researchers have addressed the deadlock control problems in flexible assembly systems (FASs) [8], [12]-[16], [26], [30], [39]. Assembly is an important process of many manufacturing systems, which puts together two or more parts to produce an intermediate or final product. Fanti et al. [8] address deadlock avoidance problems in FASs from a supervisory control point of view. Two supervisors characterized by easy implementation, efficiency, and flexibility in resource management are proposed. Roszkowska [26] contribute a method for deadlock avoidance in AMSs with assembly/disassembly processes. A supervisor is proposed for a subclass of realizable systems to avoid deadlocks. Hsieh [12]-[14] studies FASs with unreliable resources. He first analyzes the fault tolerant properties of the systems and presents the conditions under which the operation of the system can be maintained in the presence of resource failures [12], [14]. Then, he studies the deadlock avoidance problem for FASs with alternative routes, proposes a deadlock avoidance algorithm with polynomial complexity, and accesses its robustness with respect to resource failures. Wu et al. [30] studies the deadlock avoidance problem for FASs with assembly/disassembly material flow and resourceoriented PNs. A deadlock control policy is proposed and proved to be computationally efficient and less conservative than existing ones [26]. Xing et al. [39] focus on the deadlock prevention problem for FASs. Two kinds of structural objects that can lead to an empty siphon and cause deadlocks are proposed. By preventing such structural objects from causing FAS deadlocks, a PN controller is proposed. An illustrative example shows that it is more permissive than those in [26] and [30].
Although several control policies for FASs have been proposed, to the authors' best knowledge, no existing scheduling algorithm dealing with the deadlock-free scheduling problem of FASs has been proposed. This may be because:

1) the scheduling problem of AMSs with assembly processes is more difficult than that without them since parts waiting for the assembly with other parts may also lead to deadlocks, and hence it is also NP-hard;
2) combining control policies with scheduling algorithms poses a new challenge since deadlock control of FASs is not addressed widely.

Metaheuristic algorithms, e.g., genetic algorithm [58] and local search algorithm [49], have received extensive research. Genetic algorithms have been well applied in scheduling of flexible manufacturing systems [11], [41]. Detailed review can be found in [59]. They use a crossover operation to obtain better chromosomes (solutions) by exchanging information in parent chromosomes and a mutation operation to enhance the biodiversity of the population. Local search algorithms use a local search operation to search the neighbors of incumbent chromosomes to find better ones and a perturbation operation perturbs locally optimal solutions to escape from local optima. Thus, a genetic algorithm and local search algorithm are different. The latter has solved many complex and large problems successful [5], [23], [51]-[53]. However, no work has been done for the deadlock-free scheduling problem of FASs using it.

This paper intends to fill this gap by proposing a local search algorithm for the scheduling problem of deadlock-prone FASs. We assume that each part in our system has only one processing route. The reason why we make such an assumption is twofold. First, the deadlock-free scheduling problem of FAS with or without flexible routing has not been studied before. Beginning a problem from FAS without flexible routing still represents an important step in this area. Second, existing deadlock control policies for FAS with flexible routing constrain the system too much. Integrating them with scheduling algorithms tends to affect the scheduling performance greatly. Thus, research on scheduling FAS with flexible routing is delayed to the future. We use place-timed PNs to model the systems. The optimization objective is to minimize the total completion time or makespan. To embed an existing deadlock prevention policy into a scheduling algorithm, the policy is redefined in a concise way that is analogous to the original one, but can be easily embedded into a scheduling algorithm. Based on the built PN model and redefined deadlock prevention policy, a deadlock-free local search scheduling algorithm is developed. In order to enhance the global search ability and keep the population diversity of local search, a perturbation policy based on the estimation of distribution algorithm (EDA) and an acceptance criterion (AC) based on Pareto dominance for selection are proposed. Our proposed deadlock-free local search scheduling algorithm is suitable for deadlock-prone FASs with shared resources, lot size, and concurrency.

The rest of this paper is organized as follows. Section II introduces the PN modeling of FASs. A PN-based deadlock prevention policy is reviewed and redefined in Section III. Section IV establishes a deadlock-free scheduling algorithm by integrating the redefined policy with local search. The effectiveness of the proposed algorithm is illustrated in Section V. Section VI concludes this paper.

## II. BASIC PN DEFINITIONS AND FAS SCHEDULing MODELS

First, we review the basics of PNs. More details can be found in [28], [43], [44], and [55]-[57]. Next, we describe the PN model of FAS for scheduling.

## A. Basic Definitions of PNs

A PN is a 4-tuple $N=(P, T, F, W)$, where $P$ and $T$ are finite and disjoint sets. $P$ is a set of places, and $T$ is a set of transitions with $P \cap T=\varnothing, P \neq \varnothing$, and $T \neq \varnothing . F \subseteq$ $(P \times T) \cup(T \times P)$ is a set of directed arcs. $W: F \rightarrow \mathbb{N}^{+}$is a mapping that assigns to each arc a positive integer or weight. $N$ is ordinary if $\forall(x, y) \in F, W(x, y)=1$, and in this case, $W$ can be omitted.

Given a vertex $x \in P \cup T$, its preset and postset are defined as ${ }^{*} x=\{y \in P \cup T \mid(y, x) \in F\}$ and $x^{*}=\{y \in P \cup T \mid(x, y)$ $\in F\}$, respectively. Given $X \subseteq P \cup T$, we define ${ }^{\bullet} X=\cup_{x \in X}$ ${ }^{\bullet} x$ and $X^{\bullet}=\cup_{x \in X} x^{\bullet}$. A path in $N$ is a sequence of vertices $\alpha=x_{1} x_{2} \ldots x_{k}$, where $x_{i} \in P \cup T$ and $\left(x_{i}, x_{i+1}\right) \in F \forall i \in$ $\mathbb{N}_{k-1}$.

A marking of $N$ is a mapping $M: P \rightarrow \mathbb{N}$. Given a place $p$ $\in P$ and a marking $M, M(p)$ denotes the number of tokens in $p$ at $M . N$ with an initial marking $M_{0}$ is called a marked PN, denoted as $\left(N, M_{0}\right)$.

A transition $t \in T$ is enabled at a marking $M$, denoted as $M[t>$, if $\forall p \in{ }^{\bullet} t, M(p) \geq W(p, t)$. An enabled transition $t$ at $M$ can fire, generating a new marking $M^{\prime}$, denoted as $M[t>$ $M^{\prime}$, where $M^{\prime}(p)=M(p)-W(p, t) \forall p \in{ }^{\bullet} t \backslash t^{\bullet}, M^{\prime}(p)=M(p)$ $+W(t, p) \forall p \in t^{\bullet} t^{\bullet} t$, and otherwise, $M^{\prime}(p)=M(p)-W(p, t)$ $+W(t, p)$. A sequence of transitions $\alpha=t_{1} t_{2} \ldots t_{k}$ is feasible from a marking $M$ if there exists $M_{i}\left[t_{i}>M_{t+1}, i \in \mathbb{N}_{k}\right.$, where $M_{1}=M$. We call that $M_{i}$ is reachable from $M$. Let $\mathbb{R}(N, M)$ denote the set of all reachable markings of $N$ from $M$.

The incidence matrix of $N$ is a mapping $[N]: P \times T \rightarrow \mathbb{Z}$ such that $[N](p, t)=-W(p, t) \forall p \in{ }^{\bullet} t \backslash t^{\bullet} ;[N](p, t)=W(t, p)$ $\forall p \in t^{\bullet} \backslash^{\bullet} t$; otherwise $[N](p, t)=W(t, p)-W(p, t)$. A nonzero $\mid P t$-vector $\Delta: P \rightarrow N$ is a $P$-invariant if $\Delta^{T} \cdot[N]=0$. The support of a $P$-invariant is the set of places $\|\Delta\|=\{p \in P$ $|\Delta(p) \neq 0\}$. Let $\Delta$ be a $P$-invariant and $M \in \mathbb{R}\left(N, M_{0}\right)$, then $\Delta^{T} \cdot M=\Delta^{T} \cdot M_{0}$.

A nonempty set of places $S \subseteq P$ is a siphon if ${ }^{\bullet} S \subseteq S^{\bullet}$. Let $S$ be a siphon and $M \in \mathbb{R}\left(N, M_{0}\right)$. If $M(S)=0$, then $\mathbb{R}^{\prime}(S)=0 \forall M^{\prime} \in \mathbb{R}(N, M)$. A transition $t$ is live if $\forall M \in$ $\mathbb{R}\left(N, M_{0}\right)$, there exists a marking $M^{\prime} \in \mathbb{R}(N, M)$ such that $t$ is enabled at $M^{\prime}$. A transition $t$ is dead at $M \in \mathbb{R}\left(N, M_{0}\right)$ if there exists no marking $M^{\prime} \in \mathbb{R}(N, M)$ such that $t$ is enabled at $M^{\prime}$. A marked PN is live if all transitions are live.

Let $\left(N_{1}, M_{10}\right)=\left(P_{1}, T_{1}, F_{1}, W_{1}, M_{10}\right)$ and $\left(N_{2}\right.$, $\left.M_{20}\right)=\left(P_{2}, T_{2}, F_{2}, W_{2}, M_{20}\right)$ be two marked PNs. $\left(N_{1}\right.$, $M_{10}$ ) and $\left(N_{2}, M_{20}\right)$ are compatible if $\forall p \in P_{1} \cap P_{2}$, $M_{10}(p)=M_{20}(p)$ and $\forall(x, y) \in F_{1} \cap F_{2}, W_{1}(x, y)=W_{2}(x, y)$. In this case, they can be composed and their composition is a marked net $\left(N_{1}, M_{10}\right) \otimes\left(N_{2}, M_{20}\right)=\left(N_{1} \otimes N_{2}, M_{0}\right)$, where $N_{1} \otimes N_{2}=\left(P_{1} \cup P_{2}, T_{1} \cup T_{2}, F_{1} \cup F_{2}, W\right)$ where $\forall(x, y) \in F_{i}$, $W(x, y)=W_{i}(x, y), i \in\{1,2\}$ and $\forall p \in P_{i}, M_{0}(p)=M_{i 0}(p)$, $i \in\{1,2\}$.

The reverse of $N=(P, T, F, W)$ is a PN, denoted as $N^{-1}=\left(P, T, F^{-1}, W^{-1}\right)$, where $F^{-1}=\{(x, y) \mid(y, x) \in$ $F\}$ and $W^{-1}(x, y)=W(y, x)$. To distinguish a vertex $x \in P \cup$ $T$ in $N$ and $N^{-1}$, it is denoted as $f(x)$ in $N^{-1}$.

## B. Place-Timed PN Scheduling Models of FASs

The FAS studied in this paper consists of $m$ type of resources and can manufacture and assemble $l$ types
of products. Let $R=\left\{r_{i} \mid i \in \mathbb{N}_{i e}\right\}$ be the set of resource types. Each type of resources may be a kind of workstations, buffers, or robots. The capacity of $r_{i}$ is a positive integer, denoted as $C_{i}$. A product is obtained from some raw parts through a series of manufacturing and assembly operations or activities. In a manufacturing activity, parts are only processed, while in an assembly, two or more parts are assembled into a new (intermediate or final) part. The same raw parts can only be used to assemble a type of products. Let $n$ be the number of part types, and $J=\left\{J_{i} \mid i \in \mathbb{N}_{n}\right\}$ be the sets of part types, and $\Psi_{i}$ be the number of type- $i$ parts to be processed.

A processing route of a part is a sequence of manufacturing and assembly activities. A part of $J_{i}$ has only one processing route, denoted as $w_{i}$. Route $w_{i}$ can be expressed as $w_{i}=o_{i s} o_{i 1} o_{i 2} \ldots o_{i L_{i}} o_{i e}$, where $o_{i j}$ is the $j$ th manufacturing or assembly activity in $w_{i}, L_{i}$ is the total number of manufacturing and assembly activities in $w_{i}$, and $o_{i s}\left(o_{i e}\right)$ denote the start (end) activity of $J_{i}$.

In our PN model, the processing route of part $J_{i}$, i.e., $w_{i}$ is modeled by a path $\alpha_{i}=p_{i s} t_{i 1} p_{i 1} t_{i 2} p_{i 2} t_{i 3} \ldots p_{i L i} t_{i\left(L_{i}+1\right)} p_{i e}$, where $p_{i s}$ and $p_{i e}$ represent the activities $o_{i s}$ and $o_{i e}$, respectively, $p_{i j}$ is an activity place representing activity $o_{i j}, t_{i j}$ represents the start of $o_{i j}$, and $t_{i(j+1)}$ represents the completion of $o_{i j}$. Hence, the marked PN model of $w_{i}$ can be denoted as

$$
N_{i}=\left(P_{i} \cup\left\{p_{i s}, p_{i e}\right\}, T_{i}, F_{i}, M_{i 0}\right), i \in \mathbb{N}_{n}
$$

where $P_{i}=\left\{p_{i 1}, \ldots, p_{i L_{i}}\right\}, T_{i}=\left\{t_{i 1}, t_{i 2}, \ldots, t_{i\left(L_{i}+1\right)}\right\}$, and $F_{i}=\left\{\left(p_{i s}, t_{i 1}\right),\left(t_{i 1}, p_{i 1}\right), \ldots,\left(p_{i L_{i}}, t_{i\left(L_{i}+1\right)}\right),\left(t_{i\left(L_{i}+1\right)}, p_{i e}\right)\right\}$. $M_{i 0}$ is the initial marking, $M_{i 0}(p)=0 \forall p \in P_{i} \cup\left\{p_{i e}\right\}$, and $M_{i 0}\left(p_{i s}\right)=\Psi_{i}$.

The processing routes of different parts may share some identical activities. For simplicity, the identical activities are merged as one, i.e., they have the same activity place, start and completion transition.

To each resource type $r_{i} \in R$, we assign a place, called a resource place and denoted also by $r_{i}$, for simplicity. Tokens in $r_{i}$ indicate the number of available type- $i$ resources. The initial marking of $r_{i}$ is $C_{i}$. Let $P_{R}$ denote the set of all resource places.

In this paper, suppose that each activity requires only one resource. Let $R(p)$ denote the resource required by activity place $p$. Then, add arcs from $R(p)$ to each transition in ${ }^{\bullet} p$, denoting the allocation of $R(p)$, and arcs from each transition in $p^{\bullet}$ to $R(p)$, denoting the release of $R(p)$. Let $F_{R}$ denote the set of arcs related with resource places. The whole system can be modeled by the following marked PN:

$$
\left(N, M_{0}\right)=\left(P \cup P_{s} \cup P_{e} \cup P_{R}, T, F, M_{0}\right)
$$

where $P=\left\{P_{i} \mid i \in \mathbb{N}_{n}\right\}, P_{s}=\left\{p_{i s} \mid i \in \mathbb{N}_{n}\right\}, P_{e}=\left\{p_{i e} \mid i \in\right.$ $\left.\mathbb{N}_{n}\right\}, T=\left\{T_{i} \mid i \in \mathbb{N}_{n}\right\}, F=F_{Q} \cup F_{R}$, and $F_{Q}=\left\{F_{i} \mid i \in \mathbb{N}_{n}\right\}$. $P_{s}, P_{e}$, and $P_{R}$ are finite and disjoint sets, i.e., $P_{s} \neq \varnothing, P_{e} \neq \varnothing$, $P_{R} \neq \varnothing$, and $P_{s} \cap P_{e} \cap P_{R}=\varnothing$. The initial marking $M_{0}$ is defined as $M_{0}\left(p_{i s}\right)=\Psi_{i} \forall p_{i s} \in P_{s}, M_{0}(p)=0 \forall p \in P \cup P_{e}$, and $M_{0}\left(r_{i}\right)=C_{i} \forall r_{i} \in P_{R}$.

When all activities of all parts are finished, $N$ reaches a final marking, denoted as $M_{f}$, which is defined as follows. $M_{f}\left(p_{i e}\right)=M_{0}\left(p_{i s}\right) \forall p_{i e} \in P_{e}, M_{f}(p)=0 \forall p \in P \cup P_{s}$, and $M_{f}\left(r_{i}\right)=C_{i} \forall r_{i} \in P_{R}$. For a marking $M \in \mathbb{R}\left(N, M_{0}\right), M$ is safe

![img-0.jpeg](img-0.jpeg)

Fig. 1. APNS of the FAS in Example 1.
if $M_{f} \in \mathbb{R}(N, M)$; and otherwise, $M$ is unsafe. In this paper, we suppose that $M_{0}$ is safe.

For $p \in P$, let $d(p)$ denote the processing or assembly time of the activity modeled by $p$, and particularly, for $p \in P_{s} \cup P_{e} \cup$ $P_{R}, d(p)=0$. In the following, we refer to the above placetimed PN model as an assembly PN for scheduling (APNS). Let us illustrate the modeling method with the following example.

Example 1: Consider an FAS with seven types of resources $r_{1}-r_{7}$, i.e., $R=\left\{r_{i} \mid i \in \mathbb{N}_{7}\right\} . C_{i}=2 \forall i \in Z_{7}$. The system can manufacture four types of parts and assemble two types of products. The part type set is $J=\left\{J_{i} \mid i \in \mathbb{N}_{4}\right\}$. Type-1 parts are manufactured on $r_{1}, r_{2}$, and $r_{3}$ and type-2 parts on $r_{4}$ and $r_{6}$ sequentially. Then type-1 and type-2 parts are assembled on $r_{2}$. Type-3 parts are manufactured on $r_{5}$ and $r_{6}$ and type-4 parts on $r_{1}, r_{5}$, and $r_{7}$ sequentially. Then type-3 and type-4 parts are assembled on $r_{4}$. The processing routes of type-1 4 parts are $w_{1}=o_{1 s} o_{11} o_{12} o_{13} o_{14} o_{1 e}$, $w_{2}=o_{2 s} o_{21} o_{22} o_{23} o_{2 e}, w_{3}=o_{3 s} o_{31} o_{32} o_{33} o_{3 e}$, and $w_{4}=o_{4 s} o_{41} o_{42} o_{43} o_{44} o_{4 e}$, respectively. The processing routes of type-1 4 are modeled by $p_{1 s} t_{11} p_{11} t_{12} p_{12} t_{13} p_{13} t_{14} p_{14} t_{15} p_{1 e}$, $p_{2 s} t_{21} p_{21} t_{22} p_{22} t_{14} p_{14} t_{15} p_{1 e}, p_{3 s} t_{31} p_{31} t_{32} p_{32} t_{33} p_{33} t_{34} p_{3 e}$, and $p_{4 s} t_{41} p_{41} t_{42} p_{42} t_{43} p_{43} t_{33} p_{33} t_{34} p_{3 e}$, respectively. Since $o_{14}$ and $o_{23}$ represent the same activity, their activity places and start and completion transitions are the same. So are $o_{1 e}$ and $o_{2 e}, o_{33}$ and $o_{44}, o_{3 e}$ and $o_{4 e}$. Then, $P=\left\{p_{11}, p_{12}, p_{13}\right.$, $\left.p_{14}, p_{21}, p_{22}, p_{31}, p_{32}, p_{33}, p_{41}, p_{42}, p_{43}\right\}, P_{s}=\left\{p_{1 s}, p_{2 s}\right.$, $\left.p_{3 s}, p_{4 s}\right\}, P_{e}=\left\{p_{1 e}, p_{3 e}\right\}$, and $P_{R}=\left\{r_{1}, r_{2}, r_{3}, r_{4}, r_{5}\right.$, $\left.r_{6}, r_{7}\right\}$. The APNS model of the whole system is shown in Fig. 1, where the numbers of raw parts to be processed are not given.

For a transition $t \in T,{ }^{(r)} t$ and $t^{(r)}$ denote its input and output resource place sets, respectively, and ${ }^{(a)} t$ and $t^{(a)}$ denote its input and output activity place sets, respectively. For a set with a single element, e.g., ${ }^{(a)} t=\{p\}$, we use ${ }^{(a)} t=p$ for simplicity. In APNS $\forall p \in P \cup P_{s} \cup P_{e},{ }^{\bullet} p\}=\left|p^{\bullet}\right|=1$ and $\forall t \in T, \mid t^{(a)} \mid \leq 1 . t \in T$ is an assembly transition if $\left|{ }^{(a)} t\right|>1$. Let $T_{s}$ denote the set of all transitions whose input activity
places are in $P_{s}$, i.e., $T_{s}=\left\{t \in T \mid{ }^{(a)} t \in P_{s}\right\}$. For the APNS in Fig. 1, $T_{s}=\left\{t_{11}, t_{21}, t_{31}, t_{41}\right\}$.

For a given marking $M \in \mathbb{R}\left(N, M_{0}\right), t \in T$ is activity-enabled at $M$ if $M(p)>0 \forall p \in{ }^{(a)} t, t$ is resource-enabled at $M$ if ${ }^{(r)} t=\varnothing$ or $M\left({ }^{(r)} t\right)>0$. In an APNS, only transitions, which are activity- and resource-enabled at the same time, can fire. For a resource $r \in P_{R}$, let $H(r)$ denote the set of places whose activities require resource $r$, i.e., $H(r)=\{p \in P \mid R(p)=r\}$. These notations can be extended to a set. For example, $R^{\prime} \subseteq$ $P_{R}, H\left(R^{\prime}\right)=\left\{p \in P \mid R(p) \in R^{\prime}\right\}$. For any marking $M \in \mathbb{R}(N$, $\left.M_{0}\right), M\left(H\left(R^{\prime}\right) \cup R^{\prime}\right)=M_{0}\left(R^{\prime}\right)$. That means, $H\left(R^{\prime}\right) \cup R^{\prime}$ is the support of a $P$-invariant of $N$.

Given an APNS ( $N, M_{0}$ ), a sequence of transitions $s$ is named as a schedule if $M_{0}\left[s>M_{f}\right.$. Let $S\left(N, M_{0}\right)=\{s$ $\left.\mid M_{0}\left[s>M_{f}\right\}\right.$ denote the set of all schedules of $\left(N, M_{0}\right)$. Let $s=r_{1} t_{2} \ldots t_{k}$ be a schedule in $S\left(N, M_{0}\right)$ and $f\left(t_{i}\left[o_{i j}\right]\right)$ denote the firing time of $t_{i}$ that is the start time of activity $o_{i j}$. In APNS, $t_{i}\left[o_{i j}\right]$ can fire only after activity $o_{i(j-1)}$ is finished (according to the prescribed activity sequence) and $t_{(l-1)}$ fires (according to the order in $s$ ). Suppose that $t_{(l-1)}$ corresponds to $o_{u v}$ and $t_{q}$ corresponds to $o_{i(j-1)}$. Then $f\left(t_{i}\left[o_{i j}\right]\right)=\max \left\{f\left(t_{q}\left[o_{i(j-1)}\right]\right)+d\left(t_{q}^{(a)}\right), f\left(t_{(l-1)}\left[o_{u v}\right]\right)\right\}$ and the makespan of $s$ is $\operatorname{span}(s)=\max _{i, j, l}\left\{f\left(t_{i}\left[o_{i j}\right]\right)+d\left(t_{i}^{(a)}\right)\right\}$. The scheduling problem of $\left(N, M_{0}\right)$ is to find a schedule in $S\left(N\right.$, $M_{0}$ ) such that its makespan is as small as possible.

## III. Deadlock Prevention Policies OF MARKED APNSs

According to the structures of APNS and the assembly PN (APN) models [39] for FASs, we know that deadlock prevention policies for APN are available for APNS of the same FAS. Hence, the deadlock prevention policy for APN proposed in [39] can be used for APNS.

The deadlock prevention policy in [39] has not considered the integration with any scheduling algorithms. To integrate it with a scheduling algorithm, we have to redefine it. The deadlock prevention policy in [39] contains the controllers for all A-circuits and closed $\Omega$-structures. To redefine it, we have to introduce the definitions and theorems related with A-circuits and closed $\Omega$-structures first. Then, we redefine the controllers for A-circuits and closed $\Omega$-structures and give the proofs on their correctness.

## A. Structural Characteristics and Deadlock

Analysis of APNSs
Xing et al. [39] present two kinds of structural objects that may cause deadlocks in APNS, i.e., A-circuit and $\Omega$-structure. Their definitions are as follows. Let $\left(N, M_{0}\right)=\left(P \cup P_{s} \cup P_{e}\right.$ $\cup P_{R}, T, F, M_{0}$ ) be an APNS.

Definition 1 [39]: An activity path (A-path) is a path $\pi=p_{1} t_{1} \ldots p_{k} t_{k}$ where $p_{i} \in P$ and $t_{i} \in T, i \in \mathbb{N}_{k}$.

Definition 2 [39]: An A-chain is recursively defined as follows.

1) An A-path is an A-chain.
2) Let $\pi_{1}=p_{11} t_{11} \ldots p_{1 k} t_{1 k}$ and $\pi_{2}=p_{21} t_{21} \ldots p_{2 j} t_{2 j}$ be two A-chains. If ${ }^{(r)} t_{1 k}=R\left(p_{21}\right)$, then $\pi_{1}$ and

$\pi_{2}$ are said to be compatible, and $\pi=\pi_{1} \pi_{2}=$ $p_{11} t_{11} \ldots p_{1 k} t_{1 k} p_{21} t_{21} \ldots p_{2 j} t_{2 j}$ is an A-chain.
An A-path is an activity subroute of a path and starts from an activity place and ends with a transition. An A-chain is a sequence of A-paths, $\pi=\pi_{1} \pi_{2} \ldots \pi_{k-1} \pi_{k}$ such that $\pi_{i}$ and $\pi_{i+1}, i \in \mathbb{N}_{k-1}$ are compatible.

Let $\pi=p_{1} t_{1} \ldots p_{k} t_{k}$ be an A-chain in $N, \wp(\pi)=\left\{p_{1}, \ldots\right.$, $p_{k}$ ) and $\Im(\pi)=\left\{t_{1}, \ldots, t_{k}\right\}$ denote the sets of places and transitions in $\pi$, respectively, $R(\pi)=R(\wp(\pi))$ denote the set of all resource types required by the activities in $\pi$.

Definition 3 [39]: Let $\theta=\pi_{1} \pi_{2} \ldots \pi_{k-1} \pi_{k}=p_{1} t_{1} \ldots p_{q} t_{q}$ be an A-chain and $M \in \mathbb{R}\left(N, M_{0}\right)$. $\theta$ is closed if $\pi_{1}$ and $\pi_{k}$ are compatible, i.e., ${ }^{(r)} t_{q}=R\left(p_{1}\right)$. A closed A-chain is called as an A-circuit. An A-circuit $\theta$ is saturated under $M$ if $M(\wp(\theta))=M_{0}(R(\theta))$.

If two A-circuits $\theta_{1}$ and $\theta_{2}$ have the same set of resources, then they can be written as $\theta_{1}=p_{11} t_{11} \ldots p_{1 k} t_{1 k}$ and $\theta_{2}=p_{21} t_{21} \ldots p_{2 j} t_{2 j}$ with ${ }^{(r)} t_{1 k}=R\left(p_{11}\right)=R\left(p_{21}\right)={ }^{(r)} t_{2 j}$, and $\theta=\theta_{1} \theta_{2}$ is also an A-circuit. Thus, for any A-circuit $\theta$, there is a unique maximal A-circuit, denoted as $\Lambda(\theta)$, such that $\theta$ is a subcircuit of $\Lambda(\theta), \wp(\theta) \subseteq \wp(\Lambda(\theta))$ and $R(\theta)=R(\Lambda(\theta))$. Let $O(N)$ denote the set of all maximal A-circuits in $N$.

Definition 4 [39]: Let $\pi_{1}=p_{11} t_{11} \ldots p_{1 k} t_{1 k}$ be an A-chain and $\pi_{2}=p_{21} t_{21} \ldots p_{2 j} t_{2 j}$ be an A-path. If $\wp\left(\pi_{1}\right) \cap \wp\left(\pi_{2}\right)=\varnothing$ and $t_{1 k}=t_{2 j}$ (an assembly transition), then $\pi_{1}$ and $\pi_{2}$ are said to be a $v$-structure, denoted as $v=\left(\pi_{1}, \pi_{2}\right)$. Furthermore, $v$-structure $v=\left(\pi_{1}, \pi_{2}\right)$ is closed if $R\left(p_{11}\right)=R\left(p_{21}\right)$; and $R\left(p_{11}\right)$ is called a seal-resource of $v$.

Note that a $v$-structure is not symmetrical, i.e., $v=\left(\pi_{1}, \pi_{2}\right)$ is a $v$-structure, while $v^{T}=\left(\pi_{2}, \pi_{1}\right)$ may be not a $v$-structure.

Definition 5 [39]: An $\Omega$-structure is a sequence of alternating A-chains and A-paths $w=\pi_{11} \pi_{21} \ldots \pi_{1 k} \pi_{2 k}$ such that $\left(\pi_{1 i}, \pi_{2 i}\right), i \in \mathbb{N}_{k}$, is a $v$-structure and $R\left({ }^{*} \pi_{2 i}\right)=R\left({ }^{*} \pi_{1(i+1)}\right)$, $i \in \mathbb{N}_{k-1}$, where ${ }^{*} \pi$ denotes the first place of $\pi$.

Let $w=\pi_{11} \pi_{21} \ldots \pi_{1 k} \pi_{2 k}$ be an $\Omega$-structure, $\prod_{1}=\left\{\pi_{1 i}\right.$, $\left.i \in \mathbb{N}_{k}\right\}$, and $\prod_{2}=\left\{\pi_{2 i}, i \in \mathbb{N}_{k}\right\}$. Then $w$ can be written as $\left(\prod_{1}, \prod_{2}\right)$ for simplicity. Let $\wp\left(\prod_{i}\right)=\left\{\wp(\pi) \mid \pi \in \prod_{i}\right\}$ and $R\left(\prod_{i}\right)=R\left(\wp\left(\prod_{i}\right)\right), i \in\{1,2\}$. $w$ is closed if $\wp\left(\prod_{1}\right) \cap$ $\wp\left(\prod_{2}\right)=\varnothing$ and $R\left({ }^{*} \pi_{11}\right)=R\left({ }^{*} \pi_{2 k}\right)$; and $R\left({ }^{*} \pi_{11}\right)$ is called a seal-resource of $w$.

Note that a closed $v$-structure is a closed $\Omega$-structure. Let $w_{1}=\left(\prod_{11}, \prod_{12}\right)$ and $w_{2}=\left(\prod_{21}, \prod_{22}\right)$ be two closed $\Omega$-structures such that $R\left(\prod_{11}\right)=R\left(\prod_{21}\right), \prod_{1}=\prod_{11} \cup$ $\left.\prod_{21}, \prod_{2}=\prod_{12} \cup \prod_{22}\right.$. If $\prod_{1} \cap \prod_{2}=\varnothing$, then $w_{1}$ and $w_{2}$ form a closed $\Omega$-structure $w=\left(\prod_{1}, \prod_{2}\right)$. Thus, for a closed $\Omega$-structure $w=\left(\prod_{1}, \prod_{2}\right)$, there is a unique maximal closed $\Omega$-structure, or $\pi r$-structure for short, $\Lambda(w)=\left(\prod_{10}, \prod_{20}\right)$, such that $w$ is an $\Omega$-substructure of $\Lambda(w)$, and $R\left(\prod_{1}\right)=R\left(\prod_{10}\right)$. Let $W(N)$ denote the set of all $\pi r$-structures in $N$.

Definition 6 [39]: Let $M \in \mathbb{R}\left(N, M_{0}\right)$ and $w=\left(\prod_{1}, \prod_{2}\right)$ be a closed $\Omega$-structure. $w$ is semi-saturated and semi-empty at $M$ if $M\left(\wp\left(\prod_{1}\right)\right)=M_{0}\left(R\left(\prod_{1}\right)\right)$ and $M\left(\wp\left(\prod_{2}\right)\right)=0$.

Example 2: Consider the APNS in Fig. 1. Let

$$
\begin{aligned}
& \theta_{1}=p_{12} t_{13} p_{13} t_{14}, \quad \theta_{2}=p_{21} t_{22} p_{32} t_{33}, \quad \pi_{1}=p_{31} t_{32} p_{32} t_{33} \\
& \pi_{2}=p_{42} t_{43} p_{43} t_{53}, \quad \pi_{3}=p_{11} t_{12} p_{12} t_{13} p_{13} t_{14} \\
& \pi_{4}=p_{41} t_{42} p_{31} t_{32} p_{32} t_{33} p_{21} t_{22} p_{22} t_{14}, \quad \pi_{5}=p_{22} t_{14}
\end{aligned}
$$

$\pi_{6}=p_{32} t_{33}, \quad \pi_{7}=p_{41} t_{42} p_{42} t_{43} p_{43} t_{33}, \quad \pi_{8}=p_{31} t_{32} p_{22} t_{14}$
$\pi_{9}=p_{41} t_{42} p_{31} t_{32} p_{32} t_{33}, \quad \pi_{10}=p_{41} t_{42} p_{31} t_{32} p_{22} t_{14}$, and
$\pi_{11}=p_{41} t_{42} p_{42} t_{43} p_{43} t_{33} p_{21} t_{22} p_{22} t_{14}$.
Then $\theta_{1}, \pi_{1}-\pi_{3}, \pi_{5}-\pi_{7}$ are A-paths, while $\theta_{2}, \pi_{4}$, and $\pi_{8}-\pi_{11}$ are A-chains. $\theta_{1}$ and $\theta_{2}$ are both A-circuits and maximal too, and $O(N)=\left\{\theta_{1}, \theta_{2}\right\} . w_{1}=\left(\pi_{1}, \pi_{2}\right), w_{2}=\left(\pi_{2}\right.$, $\pi_{1}$ ), $w_{3}=\left(\pi_{4}, \pi_{3}\right)$, and $w_{4}=\left(\pi_{11}, \pi_{3}\right)$ are $v$-structures. Since $R\left(p_{31}\right)=R\left(p_{42}\right)$ and $R\left(p_{11}\right)=R\left(p_{41}\right), w_{1}-w_{4}$ are closed $v$-structures.

Let $w_{5}=\pi_{3} \pi_{5} \pi_{6} \pi_{7}, w_{6}=\pi_{5} \pi_{3} \pi_{7} \pi_{6}, w_{7}=\pi_{8} \pi_{3} \pi_{9} \pi_{2}$, and $w_{8}=\pi_{7} \pi_{6} \pi_{5} \pi_{3} \pi_{10} \pi_{3}$. Since $\left(\pi_{3}, \pi_{5}\right)$ and $\left(\pi_{6}, \pi_{7}\right)$ are $v$-structures, $R\left({ }^{*} \pi_{5}\right)=R\left({ }^{*} \pi_{6}\right)=r_{6}$ and $R\left({ }^{*} \pi_{3}\right)=R\left({ }^{*} \pi_{7}\right)=r_{1}$, $w_{5}=\pi_{3} \pi_{5} \pi_{6} \pi_{7}$ is a closed $\Omega$-structure. Similar, $w_{6}-w_{8}$ are closed $\Omega$-structures, too. $w_{1}-w_{8}$ are all $\pi r$-structures, and $W(N)=\left\{w_{1}, \ldots, w_{8}\right\}$.

The following lemmas show that each A-circuit or closed $\Omega$-structure can induce a siphon that may be emptied and hence lead to a deadlock. Their proofs can be referred to [39].

Lemma 1 [39]: Let $\theta$ be an A-circuit in APNS $\left(N, M_{0}\right)$, and $M \in \mathbb{R}\left(N, M_{0}\right)$. Then $\phi(\theta)=R(\theta) \cup\{H(R(\theta)) \backslash \wp(\theta)\}$ is a siphon of $N$ (induced by $\theta$ ), and $\theta$ is saturated at $M$ if and only if $\phi(\theta)$ is empty at $M$.

Lemma 2 [39]: Let $w=\left(\prod_{1}, \prod_{2}\right)=\pi_{11} \pi_{21} \ldots \pi_{1 k} \pi_{2 k}$ be a closed $\Omega$-structure in APNS $\left(N, M_{0}\right)$, and $M \in \mathbb{R}(N$, $\left.M_{0}\right)$. Then $\phi(w)=R\left(\prod_{1}\right) \cup\left\{H\left(R\left(\prod_{1}\right)\right) \backslash \wp\left(\prod_{1}\right)\right\} \cup \wp\left(\prod_{2}\right)$ is a siphon of $N$ (induced by $w$ ), and $w$ is semi-saturated and semi-empty at $M$ if and only if $\phi(w)$ is empty at $M$.

Let $N$ be an APNS, $\aleph(N)=O(N) \cup W(N)$ be the set of maximal A-circuits and $\pi r$-structures, and $\mathrm{S}(N)=\{\phi(\alpha) \mid$ $\alpha \in \aleph(N)\}$ be the set of siphons induced by A-circuits or $\pi r$-structures in $\aleph(N)$.

Example 3: For the APNS in Fig. 1, from Example 1, we know that $\theta_{1}=p_{12} t_{13} p_{13} t_{14}$ is an A-circuit. By Lemma 1, the siphon induced by $\theta_{1}$ is

$$
\phi\left(\theta_{1}\right)=R\left(\theta_{1}\right) \cup\left\{H\left(R\left(\theta_{1}\right)\right) \backslash \wp\left(\theta_{1}\right)\right\}=\left\{r_{2}, r_{3}, p_{14}\right\}
$$

$w_{1}=\left(\pi_{1}, \pi_{2}\right)$ is a closed $\Omega$-structure. By Lemma 2, the siphon induced by $w_{1}$ is

$$
\begin{aligned}
\phi\left(w_{1}\right) & =R\left(\pi_{1}\right) \cup\left\{H\left(R\left(\pi_{1}\right)\right) \backslash \wp\left(\pi_{1}\right)\right\} \cup \wp\left(\pi_{2}\right) \\
& =\left\{r_{5}, r_{6}, p_{22}, p_{42}, p_{43}\right\}
\end{aligned}
$$

Let $M_{0}=5\left(p_{1 s}+p_{2 s}+p_{3 s}+p_{4 s}\right)+$ $2\left(r_{1}+r_{2}+r_{3}+r_{4}+r_{5}+r_{6}+r_{7}\right)$ be the initial marking of $N$, and $M=p_{1 s}+5 p_{2 s}+p_{3 s}+5 p_{4 s}+$ $2\left(p_{12}+p_{13}+p_{31}+p_{32}+r_{1}+r_{4}+r_{7}\right) \in \mathbb{R}\left(N, M_{0}\right)$. $M\left(\wp\left(\theta_{1}\right)\right)=M_{0}\left(R\left(\theta_{1}\right)\right)=4$. Hence $\theta_{1}$ is saturated at $M$, and $M\left(\phi\left(\theta_{1}\right)\right)=0 . M\left(\wp\left(\pi_{1}\right)\right)=M_{0}\left(R\left(\pi_{1}\right)\right)=4$ and $M\left(\wp\left(\pi_{2}\right)\right)=0$, hence $w_{1}$ is semi-saturated and semi-empty at $M$, and $M\left(\phi\left(w_{1}\right)\right)=0$.

Theorem 1 [39]: An APNS $\left(N, M_{0}\right)$ is live if and only if none of A-circuits is saturated and none of closed $\Omega$-structures is semi-saturated and semi-empty at $V M \in \mathbb{R}\left(N, M_{0}\right)$.

Its proof is given in [39]. Please refer to [39] for the details.

## B. Deadlock Prevention Policies for APNSs

By Theorem 1, we know that only A-circuits and closed $\Omega$-structures can lead an APNS to deadlocks. The system is

![img-2.jpeg](img-2.jpeg)
(a)
(b)

Fig. 2. Controller for $\theta_{1}$ and $w_{2}$ by [39].
live if and only if all siphons induced by A-circuits and closed $\Omega$-structures are not emptied at any reachable marking. To avoid deadlock, it is necessary to guarantee that all siphons are not empty. The deadlock prevention policy in [39] is to add a PN controller to each A-circuit and closed $\Omega$-structure such that their corresponding siphons cannot be emptied at any reachable marking. To make it easy to be integrated with a scheduling algorithm, we redefine it as follows.

Let $\pi$ be an A-chain in APNS ( $N, M_{0}$ ). A transition $t$ is called an input or output transition of $\pi$ if firing $t$ increases or decreases the number of tokens in $\wp(\pi)$. Let $I(\pi)$ and $O(\pi)$ denote the sets of input and output transitions of $\pi$, respectively.

Let $T(\pi)$ denote the set of transitions in $T_{s}$ from which there is an A-path to $I(\pi)$, i.e., $T(\pi)=\left\{t \in T_{s} \mid\right.$ An A-path from $t^{(a)}$ to $I(\pi)$ exists or $\left.t \in I(\pi)\right\}$.

Definition 7: Let $\theta$ be an A-circuit in APNS $\left(N, M_{0}\right)$. Define a weighted PN controller for $\theta$

$$
\left(C[\theta], M_{\theta}\right)=\left(P_{\theta}, T_{\theta}, F_{\theta}, W_{\theta}, M_{\theta}\right)
$$

where $P_{\theta}=\left\{p_{\theta}\right\}$ and $p_{\theta}$ is the control place corresponding to $\theta$ with $M_{\theta}\left(p_{\theta}\right)=M_{0}(R(\theta))-1, T_{\theta}=T(\theta) \cup O(\theta)$, and $F_{\theta}=$ $\left\{\left(p_{\theta}, t\right) \mid t \in T(\theta)\right\} \cup\left\{\left(t, p_{\theta}\right) \mid t \in O(\theta)\right\}$, and $W_{\theta}\left(t, p_{\theta}\right)=\left[{ }^{(a)} t\right.$ $\cap \wp(\theta)\left|-\mid t^{(a)} \cap \wp(\theta)\right|$ for $\left(t, p_{\theta}\right) \in F_{\theta}$, and $W_{\theta}\left(p_{\theta}, t\right)=1$ for $\left(p_{\theta}, t\right) \in F_{\theta}$.

Lemma 3: Let $\theta$ be an A-circuit in APNS $\left(N, M_{0}\right)$, and $\left(C[\theta], M_{\theta}\right)$ be a PN controller for $\theta$ given in Definition 7. Then $\left(C[\theta], M_{\theta}\right)$ can avoid siphon $\phi(\theta)$ from being emptied. Let $\left(\underline{C}[\theta], \underline{M}_{\theta}\right)$ be the controller in [39] for $\theta$. Then, $\left(C[\theta]\right.$, $M_{\theta}$ ) is analogous to $\left(\underline{C}[\theta], \underline{M}_{\theta}\right)$.

Its proof is available at https://github.com/luojianchao/ ILS4FAS.

Note that the controllers for A-circuits in this paper have some difference from those in [39]. Consider the APNS in Fig. 1. From Example 1, we know that $\theta_{1}=p_{12} t_{13} p_{13} t_{14}$ is a maximal A-circuit. $T\left(\theta_{1}\right)=\left\{t_{11}\right\}$, and $O(\theta)=\left\{t_{14}\right\}$. The controller for $\theta_{1}$ by Definition 7, $\left(C\left[\theta_{1}\right], M_{\theta}\right)$, is shown in Fig. 3(a), and that for $\theta_{1}$ by [39], $\left(\underline{C}\left[\theta_{1}\right], \underline{M}_{\theta}\right)$, is shown in Fig. 2(a). Obviously, $\left(C\left[\theta_{1}\right], M_{\theta}\right)$ does not contain places and transitions in $N^{-1}$ and hence is more concise than $\left(\underline{C}\left[\theta_{1}\right]\right.$, $\underline{M}_{\theta 1}$ ). Although their structures are different, their function is the same. The function of $\left(C\left[\theta_{1}\right], M_{\theta 1}\right)$ is to constrain $M\left(p_{11}\right)+M\left(p_{12}\right)+M\left(p_{13}\right)+M\left(p_{\theta 1}\right)=3$, and $\left(\underline{C}\left[\theta_{1}\right], \underline{M}_{\theta 1}\right)$ is to constrain $M\left(p_{11}\right)+M\left(p_{12}\right)+M\left(p_{13}\right)+M\left(f\left(p_{11}\right)\right)+$ $M\left(p_{\theta 1}\right)=3$. Since $M\left(f\left(p_{11}\right)\right) \geq 0$ and $M\left(p_{\theta 1}\right) \geq 0,\left(C\left[\theta_{1}\right], M_{\theta}\right)$ and $\left(\underline{C}\left[\theta_{1}\right], \underline{M}_{\theta 1}\right)$ are both to constrain $M\left(p_{11}\right)+M\left(p_{12}\right)+$ $M\left(p_{13}\right) \leq 3$. Hence, they are analogous.

Let $w=\pi_{11} \pi_{21} \ldots \pi_{1 k} \pi_{2 k}=(\prod_{1}, \prod_{2})$ be a closed $\Omega$-structure, where $\prod_{1}=\left\{\pi_{1 i}, i \in \mathbb{N}_{k}\right\}$ and $\prod_{2}=\left\{\pi_{2 i}, i\right.$ $\in \mathbb{N}_{k}$, and $\wp\left(\prod_{1}\right)=\left\{\wp\left(\pi_{1 i}\right) \mid \pi_{1 i} \in \prod_{1}\right\}$. A transition $t$ is called an input or output of $\prod_{1}$ if firing $t$ increases or decreases
![img-2.jpeg](img-2.jpeg)

Fig. 3. PN controllers for maximal A-circuits and $\varpi$-structures.
the number of tokens in $\wp\left(\prod_{1}\right)$. Let $I\left(\prod_{1}\right)$ and $O\left(\prod_{1}\right)$ denote the sets of input and output transitions of $\prod_{1}$, respectively.

Let $T(w)$ denote the set of transitions in $T_{s}$ from which there is an A-path to $I\left(\prod_{1}\right)$, i.e., $T(w)=\left\{t \in T_{s} \mid\right.$ An A-path from $t^{(a)}$ to $I\left(\prod_{1}\right)$ exists or $t \in I\left(\prod_{1}\right)\right\}$.

Definition 8: Let $w=\left(\prod_{1}, \prod_{2}\right)$ be a closed $\Omega$-structure in APNS $\left(N, M_{0}\right)$, define a weighted PN controller for $w$

$$
\left(C[w], M_{w}\right)=\left(P_{w}, T_{w}, F_{w}, W_{w}, M_{w}\right)
$$

where $P_{w}=\left\{p_{w}\right\}$ and $p_{w}$ is a control place corresponding to $w$, the initial marking is $M_{w}\left(p_{w}\right)=M_{0}\left(R\left(\prod_{1}\right)\right)-1, T_{w}=T(w) \cup$ $O\left(\prod_{1}\right)$, and $F_{w}=\left\{\left(p_{w}, t\right) \mid t \in T(w)\right\} \cup\left\{\left(t, p_{w}\right) \mid t \in O(w)\right\}$, and $W_{w}\left(t, p_{w}\right)=\left|{ }^{(a)} t \cap \wp\left(\prod_{1}\right)\right|-\left|{ }^{(a)} \cap \wp\left(\prod_{1}\right)\right|$ for $\left(t, p_{w}\right)$ $\in F_{w}$, and $W_{w}\left(p_{w}, t\right)=1$ for $\left(p_{w}, t\right) \in F_{w}$.

Lemma 4: Let $w$ be a closed $\Omega$-structure in APNS $\left(N, M_{0}\right)$, and $\left(C[w], M_{w}\right)$ be a PN controller for $w$ given in Definition 8. Then $\left(C[w], M_{w}\right)$ can avoid siphon $\phi(w)$ from being emptied. Let $\left(\underline{C}[w], \underline{M}_{w}\right)$ be the controller in [39] for $w$. Then, $\left(C[w], M_{w}\right)$ is analogous to $\left(\underline{C}[w], \underline{M}_{w}\right)$.

Its proof is available at https://github.com/luojianchao/ ILS4FAS.

Note that the controllers for closed $\Omega$-structures in this paper have some difference from those in [39]. Consider the APNS in Fig. 1. From Example 1, we know that $w_{2}=\left(\prod_{1}\right.$, $\left.\prod_{2}\right)=\left(\pi_{2}, \pi_{1}\right)=\left(\left\{p_{42} t_{43} p_{43} t_{33}\right\},\left\{p_{31} t_{32} p_{32} t_{33}\right\}\right)$ is a closed $\Omega$-structure. $T\left(w_{2}\right)=\left\{t_{41}\right\}, O\left(\prod_{1}\right)=\left\{t_{33}\right\}$. The controller for $w_{2}$ by Definition 8, $\left(C\left[w_{2}\right], M_{w 2}\right)$, is shown in Fig. 3(d), and that for $w_{2}$ by [39], $\left(\underline{C}\left[w_{2}\right], \underline{M}_{w 2}\right)$, is shown in Fig. 2(b). Obviously, $\left(C\left[w_{2}\right], M_{w 2}\right)$ does not contain places and transitions in $N^{-1}$ and hence is more concise than $\left(\underline{C}\left[w_{2}\right]\right.$, $\underline{M}_{w 2}$ ). Although their structures are different, their function is the same. The function of $\left(C\left[w_{2}\right], M_{w 2}\right)$ is to ensure $M\left(p_{41}\right)+M\left(p_{42}\right)+M\left(p_{43}\right)+M\left(p_{w 2}\right)=3$, and $\left(\underline{C}\left[w_{2}\right]\right.$, $\underline{M}_{w 2}$ ) is to ensure $M\left(p_{41}\right)+M\left(p_{42}\right)+M\left(p_{43}\right)+M\left(f\left(p_{41}\right)\right)+$ $M\left(p_{w 2}\right)=3$. Since $M\left(f\left(p_{41}\right)\right) \geq 0$ and $M\left(p_{w 2}\right) \geq 0,\left(C\left[w_{2}\right]\right.$, $M_{w 2}$ ) and $\left(\underline{C}\left[w_{2}\right], \underline{M}_{w 2}\right)$ are both to ensure $M\left(p_{41}\right)+M\left(p_{42}\right)+$ $M\left(p_{43}\right) \leq 3$. Hence, they are analogous.

Definition 9: A PN controller for APNS $\left(N, M_{0}\right),\left(C, M_{C}\right)$, is the composition of all controllers for all maximal A-circuits and all $\varpi$-structures in $\aleph(N)$, i.e.,

$$
\left(C, M_{C}\right)=\otimes_{\tau \in \aleph(N)}\left(C[\tau], M_{\tau}\right)
$$

Then the controlled system can be modeled by the composition of $\left(N, M_{0}\right)$ and $\left(C, M_{C}\right)$ as follows. $\left(C N, M_{C 0}\right)=\left(N, M_{0}\right)$ $\otimes\left(C, M_{C}\right)=\left(P \cup P_{s} \cup P_{e} \cup P_{R} \cup P_{C}, T \cup T_{C}, F \cup F_{C}\right.$, $M_{C 0}$ ), where $M_{C 0}(p)=M_{0}(p) \forall p \in P \cup P_{s} \cup P_{e} \cup P_{R}$, and $M_{C 0}(p)=M_{C}(p) \forall p \in P_{C}$. When all activities of all

parts are finished, $C N$ reaches a final marking, denoted as $M_{C f}$, which is defined as follows. $M_{C f}(p)=0 \forall p \in P \cup P_{s}$, $M_{C f}\left(p_{i e}\right)=M_{C 0}\left(p_{i s}\right) \forall p_{i e} \in P_{e}, M_{C f}\left(r_{i}\right)=C_{i} \forall r_{i} \in P_{R}$, and $M_{C f}(p)=M_{C 0}(p) \forall p \in P_{C}$.

Example 4: Consider the APNS $N$ in Fig. 1, from Example 2, we know that $\aleph(N)=O(N) \cup W(N)=\left\{\theta_{1}, \theta_{2}\right.$, $\left.w_{1}, \ldots, w_{8}\right\}$. The controller for $\theta_{1}, \theta_{2}$, and $w_{1}-w_{8}$ are shown in Fig. 3(a)-(j), respectively.

Theorem 2: Let $\left(N, M_{0}\right)$ be an APNS. Then the PN controller $\left(C, M_{C}\right)$ for $\left(N, M_{0}\right)$ in Definition 9 makes the controlled net deadlock-free.

Its proof is available at https://github.com/luojianchao/ ILS4FAS.

The controller in [39] contains some places and transitions in $N^{-1}$, but that in this paper does not. Thus, our controller is more concise. Besides, our controller has another advantage over that in [39], i.e., if it allows an activity and resourcenabled transition to fire at a making, then the transition can fire in the controlled system. However, the controller in [39] may allow such a firing only after some transitions in $N^{-1}$ fire. Take the controllers for $\theta_{1}$, i.e., $\left(C\left[\theta_{1}\right], M_{\theta 1}\right)$ in Fig. 3(a) and (C[ $\left.\theta_{1}\right], \underline{M}_{\theta 1}$ ) in Fig. 2(a) as an example. Both ( $\left.C\left[\theta_{1}\right], M_{\theta 1}\right)$ and (C[ $\left.\theta_{1}\right], \underline{M}_{\theta 1}$ ) allow $t_{11}$ to fire in $N$ at $M_{0}=5\left(p_{1 s}+p_{2 s}+\right.$ $\left.p_{3 s}+p_{4 s}\right)+2\left(r_{1}+r_{2}+r_{3}+r_{4}+r_{5}+r_{6}+r_{7}\right)$. However, $t_{11}$ is not enabled in (C[ $\left.\theta_{1}\right], \underline{M}_{\theta 1}$ ) $\otimes\left(N, M_{0}\right)$ since $M\left(f\left(p_{11}\right)\right)=0$, and $t_{11}$ is allowed to fire only after $f\left(t_{42}\right)$ fires.

To illustrate the benefits of two above advantages, some notations are introduced. Let $\left(C, M_{C}\right)$ and (C, $\underline{M_{C}}$ ) denote our controller and the one in [39], respectively, $\left(C N, M_{C 0}\right)=\left(C\right.$, $\left.M_{C}\right) \otimes\left(N, M_{0}\right)$, and $\left(\underline{C N}, \underline{M_{C 0}}\right)=\left(\underline{C}, \underline{M_{C}}\right) \otimes\left(N, M_{0}\right)$. Usually, a deadlock-free scheduling algorithm integrates with a controller by taking it as a constraint for the original system. It means that a deadlock-free scheduling algorithm finds a schedule in the controlled net, e.g., $\left(C N, M_{C 0}\right)$ or $(\underline{C N}$, $\underline{M_{C 0}})$. By the first advantage, we know that $(\underline{C N}, \underline{M_{C 0}})$ has transitions and places in $N^{-1}$, while $\left(C N, M_{C 0}\right)$ does not. The search space of ( $\underline{C N}, \underline{M_{C 0}}$ ) is larger than that of $\left(C N, M_{C 0}\right)$. Thus, scheduling FMS with $\left(C, M_{C}\right)$ can achieve higher search efficiency for an optimal schedule than doing it with ( $\underline{C}, \underline{M_{C}}$ ). By the second advantage, we know that the schedule obtained in $(\underline{C N}, \underline{M_{C 0}})$ cannot be executed in $\left(N, M_{0}\right)$ directly since it may contain some transitions in $N^{-1}$, while the schedule obtained in $\left(C N, M_{C 0}\right)$ can be executed in $\left(N, M_{0}\right)$ directly. Thus, scheduling the system with $\left(C, M_{C}\right)$ is easier than doing so with ( $\underline{C}, \underline{M_{C}}$ ).

## IV. DeADlock-Free LOCAL SEARCH

ALGORITHM FOR FASS

In order to obtain the optimal or suboptimal schedule to minimize the makespan and to avoid deadlock, a deadlockfree local search algorithm is proposed, which is an iterative algorithm in which the deadlock prevention policy is embedded. It is based on the following two main components with its flow chart in Fig. 4: 1) preliminaries of local search (coding, decoding, repairing, population generation, and termination
![img-3.jpeg](img-3.jpeg)

Fig. 4. Flow chart of a deadlock-free local search scheduling algorithm.
condition) and 2) local search operations (perturbation, local search, and selection).

## A. Preliminaries of Local Search

1) Coding: In this paper, a solution for our scheduling problem is a sequence of the elements of a set of coded parts. The set of coded parts consists of a sequence of consecutive positive integers starting from 1 , in which each integer corresponds to a part. Consider a system with $n$ types of parts to be processed. The total number of parts to be processed is denoted as $\vartheta=\Psi_{1}+\cdots+\Psi_{n}$, where $\Psi_{i}\left(i \in \mathbb{N}_{n}\right)$ is the number of type- $i$ parts to be processed. Let $\vartheta_{k}=\sum_{j=1}^{k} \Psi_{j}$ denote the sum of first $k\left(k \in \mathbb{N}_{n}\right)$ types of parts to be processed. Specially, let $\vartheta_{0}=0$. Then, the set of type- $i$ parts is coded as $\left\{\vartheta_{(i-1)}+1, \vartheta_{(i-1)}+2, \ldots, \vartheta_{i}\right\}$, and the set of all parts is coded as $\mathrm{N}_{\vartheta}$. Given a code $k \in \mathrm{~N}_{\vartheta}$, let $\mu(k)$ denote the type of the part which is coded by $k$, i.e., $\mu(k)=i$ if $k \in$ $\left\{\vartheta_{(i-1)}+1, \vartheta_{(i-1)}+2, \ldots, \vartheta_{i}\right\}$.

A permutation is defined as an order of the elements of a finite set. An order in which elements may appear more than once is called a permutation with repetition. A solution code of the scheduling problem is named as a chromosome. A chromosome is a permutation with repetition of elements in $\mathrm{N}_{\vartheta}$. Each code in a chromosome is named as a gene. For code $k \in \mathrm{~N}_{\vartheta}$, it appears $\left(L_{\mu(k)}+1\right)$ times in a chromosome, where $L_{\mu(k)}$ is the total number of manufacturing and assembly activities of a type- $\mu(k)$ part. The $j$ th $k$ represents the start of the part's $j$ th activity, where $j \leq L_{\mu(k)}$, and the last $k$ represents the part's end activity. Different types of parts may share some identical activities. For simplicity, the codes of two identical activities are merged as one.

Example 5: Consider the APNS $N$ in Fig. 1, and suppose that two type-1 parts and two type-2 parts are to be processed, i.e., $\Psi_{1}=\Psi_{2}=2$. Then, $\vartheta_{0}=0, \vartheta_{1}=\Psi_{1}=2$, $\vartheta_{2}=\Psi_{1}+\Psi_{2}=4$. The set of codes for type-1 parts is $\left\{\vartheta_{0}+1, \ldots, \vartheta_{1}\right\}=\{1,2\}$, and that for type- 2 parts is $\left\{\vartheta_{1}+1, \ldots, \vartheta_{2}\right\}=\{3,4\}$. Thus, the set of all codes is $\mathbb{N}_{4}=\{1,2,3,4\}$. Since the fourth activity of a type-1 part and the third activity of a type-2 part are the same, their corresponding codes are merged as one. Similarly, the codes corresponding to end activities of a type-1 part and a type- 2 part are merged as one. For simplicity, let the codes

## Algorithm 1 RA

Input: chromosome $\Gamma$ and the controlled APNS (CN, $M_{C 0})=\left(N, M_{0}\right) \otimes\left(C, M_{C}\right)$;
Output: $\Gamma_{1} ; /^{*} \Gamma_{1}$ is the repaired chromosome */
$1: M=M_{C 0} ; /^{*}$ initialization*/
2: for all $(i=0 ; i<|\Gamma| ; i++)$ do
3: let $j=0$;
4: while $(\alpha(\Gamma)[i]$ is not enabled at $M)$ do
5: $j++$;
6: $\quad \operatorname{swap}(\Gamma[i], \Gamma[i+j])$;
7: end while
8: $M[\alpha(\Gamma)[i]>M_{1}$;
9: $M=M_{1}$;
10: end for
11: $\Gamma_{1}=\Gamma$;
12: return $\Gamma_{1}$
of type-1 parts denote the merged ones. The total number of manufacturing and assembly activities of a type-1 parts is four, thus codes 1 and 2 appear $5=4+1$ times in a chromosome, where the first four codes 1 (or 2 ) represent the starts of a type-1 part's four activities, and the last one represents the part's end activity. The total number of manufacturing and assembly activities of a type-2 part is 3 . Since the third and end activities of type-2 parts are denoted by the codes of type1 parts, thus codes 3 and 4 appear $2=3+1-2$ times in a chromosome. Then, a chromosome can be expressed as $\Gamma_{1}=$ $(1,2,3,1,3,2,4,2,4,1,2,1,2,1)$.
2) Decoding: In order to convert a chromosome into a sequence of codes that can be recognized by PN, the decoding technology is designed. Since a gene in a chromosome $\Gamma$ represents a unique activity, $\Gamma$ can be interpreted uniquely as a sequence of activities denoted as $o(\Gamma)$. By mapping each activity in $o(\Gamma)$ to its start transition, a chromosome $\Gamma$ can be interpreted as a sequence of transitions, denoted as $\alpha(\Gamma)$.

Example 6: Consider chromosome $\Gamma_{1}$ in Example 5. The first 1 (or 2 ) in $\Gamma_{1}$ represents the start of a type-1 part's first activity, i.e., $o_{11}$, the second 1 (or 2 ) represents the start of a type-1 part's second activity, i.e., $o_{12}$, and the last 1 (or 2) represents a type-1 part's end activity, i.e., $o_{1 e}$. Similarly, the first 3 (or 4) represents the start of a type-2 part's first activity, i.e., $o_{21}$, and the second 3 (or 4) represents for the start of a type-2 part's second activity, i.e., $o_{22}$. Thus, $\Gamma_{1}$ can be interpreted as $o\left(\Gamma_{1}\right)=\left(o_{11}, o_{11}, o_{21}, o_{12}, o_{22}, o_{12}, o_{21}, o_{13}\right.$, $\left.o_{22}, o_{13}, o_{14}, o_{14}, o_{1 e}, o_{1 e}\right)$. By mapping each activity in $o(\Gamma)$ to its start transition, $\Gamma$ can be interpreted as $\alpha\left(\Gamma_{1}\right)=\left(t_{11}\right.$, $\left.t_{11}, t_{21}, t_{12}, t_{22}, t_{12}, t_{21}, t_{13}, t_{22}, t_{13}, t_{14}, t_{14}, t_{15}, t_{15}\right)$.
3) Repairing: The proposed repairing algorithm (RA) is a recursive procedure. Let $\left(C N, M_{C 0}\right)$ be a controlled APNS and $\Gamma$ be a chromosome. At each step, select a gene in $\Gamma$, which can be interpreted as a transition that is enabled at the current marking $M$ in $C N$, from unselected genes of $\Gamma$. This process corresponds to Lines 3-7 of RA. Then, update the current marking $M$ by firing the transition corresponding to the selected gene from it. This process corresponds to Lines 8 and 9 of RA. Repeat this procedure till the set of unselected genes of $\Gamma=\varnothing$. This process corresponds to the for-loop in RA. We have the following result.

Theorem 3: RA is correct.

Its proof is available at https://github.com/luojianchao/ ILS4FAS.
4) Initial Population Generation: A chromosome is generated in two steps: 1) generate a permutation with repetition of elements in $\mathrm{N}_{\vartheta}$, where $k \in \mathrm{~N}_{\vartheta}$ appears $\left(L_{\mu(k)}+1\right)$ times and 2) merge the codes in the permutation, which represent two identical activities of different types of parts as the one with smaller integer value.
5) Termination Condition: The maximum number of generations is used as a termination condition to stop the proposed algorithm.

## B. Local Search Operations

Local search operations are used to create a child population from parent one. They include perturbation, local search, and selection.

1) Perturbation: This operation perturbs locally optimal solutions to escape from local optima and explore a new region of the search space. The EDA [18] is a population evolution algorithm based on a probability model, which owns strong global search ability. To take such advantage of EDA, a novel EDA-based perturbation policy (EDA-P) is presented.

Let $L$ be the length of a chromosome, and $\beta$ be the size of a population. In this paper, we choose $\varepsilon=\left\lceil\zeta_{p} \cdot \beta\right\rceil$ best chromosomes to establish the excellent population, where $\zeta_{p}$ $\in(0,1]$ is the parameter for EDA-P. The set of best chromosomes is denoted as $\left\{\Gamma_{1}, \ldots, \Gamma_{e}\right\}$. The probability model $\mathbb{P}$ is an $L \times L$ matrix where $\mathbb{P}(i, j)$ is the probability that activity $j$ is in the front of activity $i$. Formally, $\mathbb{P}(i, j)=\left(\sum_{k=1}^{e} I_{i j}\left(\Gamma_{k}\right)\right)$ $l(i, \varepsilon)$, where $I_{i j}\left(\Gamma_{k}\right)$ is a two-valued function defined as follows. If activity $j$ is in or in the front of the $i$ th position of a chromosome $\Gamma_{k}$, then $I_{i j}\left(\Gamma_{k}\right)=1$; otherwise, $I_{i j}\left(\Gamma_{k}\right)=0$.

A new chromosome $\Gamma$ is generated based on $\mathbb{P}$ as follows. For the $i$ th position of $\Gamma$, we select an activity by the roulette wheel method [25]. The selection probability of activity $j$ is $\mathbb{P}(i, j)$. Once activity $j$ is selected in position $i$, then it cannot be selected any more. So, we set $\mathbb{P}(k, j)=0 \forall k \in \mathbb{N}_{L}$ and $k>$ $i$. Iteratively execute this procedure until a new chromosome is completed.
2) Local Search: This operation searches the neighbors of incumbent chromosomes to find better ones. Different local search operators have been proposed in [5] and [23]. They make contribution to the field in which they are used. However, they cannot be used in the problem studied in this paper. To take the size of a neighborhood into account, we define $\zeta_{l}$ to denote as the maximum ratio of the number of different genes between two chromosomes to $L$ (the length of a chromosome). The number of neighbors of a chromosome increases with the value of $\zeta_{l}$. According to [49], we know that the number of neighbors of an incumbent chromosome should not be too large. Otherwise, it is difficult to find any local optimum. When $\zeta_{l}$ is larger than 0.1 , the number of neighbors of an incumbent chromosome is large enough. Thus, we roughly set the range of $\zeta_{l}$ as ( 0 , 0.1]. A neighborhood chromosome is generated by randomly

choosing $L . \zeta_{l}$ genes from an incumbent chromosome, and then randomly putting them in the places where they are chosen.

Let $\chi$ be the maximum number of times of local search allowed to perform consecutively on an incumbent chromosome, which does not reduce its makespan. Given a chromosome $\Gamma$, let $\gamma(\Gamma)=\operatorname{span}(\alpha(\Gamma))$ denote its makespan, and $\delta(\Gamma)$ record the number of times of consecutive local search on it which does not reduce its makespan. A local search operator starts from $\Gamma$. It iteratively performs the following process: find $\Gamma_{1}$ in the neighborhood of $\Gamma$; perform RA to repair $\Gamma_{1}$ to a feasible chromosome $\Gamma_{2}$; compare $\Gamma_{2}$ with $\Gamma$. If $\gamma\left(\Gamma_{2}\right)$ is less than $\gamma(\Gamma), \Gamma$ is replaced by $\Gamma_{2}$ and $\delta(\Gamma)=0$; otherwise, $\delta(\Gamma)=\delta(\Gamma)+1$. If $\delta(\Gamma)$ is equal to $\chi$, local search is stopped. Generally speaking, the bigger $\chi$ is, the better the local search's performance. However, if $\chi$ is too big, the CPU time is too long. Thus, the effectiveness of $\chi$ is certain. In the following test, it is fixed as 10 .
3) Selection: This operation selects a child population from incumbent population and newly generated population via local search. An acceptance criterion (AC) plays a crucial role in a local search algorithm [27]. It directly affects the intensification and diversification of a population. In order to keep high-quality and low-similarity chromosomes, we develop a novel Pareto dominance-based AC (PD-AC) [6]. Let $\Gamma_{b}$ be the best chromosome found by now. A chromosome $\Gamma$ is associated with two indicators $\gamma(\Gamma)$ and $S\left(\Gamma, \Gamma_{b}\right)$ representing the quality and similarity, respectively, where $S(\Gamma$, $\Gamma_{b}$ ) is the number of positions in which $\Gamma$ and $\Gamma_{b}$ have the same genes.

A chromosome $\Gamma$ is said to dominate another chromosome $\Gamma_{1}$, if $\gamma(\Gamma) \leq \gamma\left(\Gamma_{1}\right)$ and $S\left(\Gamma, \Gamma_{b}\right)<S\left(\Gamma_{1}, \Gamma_{b}\right)$, or $\gamma(\Gamma)<$ $\gamma\left(\Gamma_{1}\right)$ and $S\left(\Gamma, \Gamma_{b}\right) \leq S\left(\Gamma_{1}, \Gamma_{b}\right)$. A chromosome is said to be nondominated if no other chromosome dominates it. The crowding distance of a chromosome $\Gamma$, denoted as $c(\Gamma)$, is defined as follows. If $\Gamma$ is a boundary chromosome (chromosomes with smallest or largest indicators), then an infinite distance value is assigned to $c(\Gamma)$. Otherwise, $c(\Gamma)$ is assigned the sum of two values equal to the absolute normalized differences in the $\gamma(\Gamma)$ and $S\left(\Gamma, \Gamma_{b}\right)$ values of two adjacent chromosomes.

PD-AC is used to select child population from incumbent population and newly generated population by local search in three steps. First, PD-AC ranks each chromosome to be selected according to its dominance relationship. The nondominated solutions are in the first rank, the chromosomes that are only dominated by the nondominated chromosomes are in the second rank, and so on. Then, PD-AC computes the crowding distance of each chromosome. In the end, PD-AC selects $\beta$ (the size of a population) chromosomes according to the rank and crowing distances by the following rule. PD-AC selects chromosomes with smaller rank. For the chromosomes in the same rank, the chromosome with biggest crowing distances is selected. The selecting process goes on until $\beta$ chromosomes are selected. Since the current best solution is a nondominated solution with an infinite distance, it must be selected to the next generation.

TABLE I
Processing Times of Activities of the APNS in Fig. 1

| $d\left(p_{1}\right): 27$ | $d\left(p_{2}\right): 29$ | $d\left(p_{3}\right): 31$ | $d\left(p_{4}\right): 25$ |
| :--: | :--: | :--: | :--: |
| $d\left(p_{1}\right): 16$ | $d\left(p_{2}\right): 18$ | $d\left(p_{3}\right): 23$ | $d\left(p_{4}\right): 19$ |
| $d\left(p_{1}\right): 34$ |  | $d\left(p_{3}\right): 24$ | $d\left(p_{4}\right): 38$ |
| $d\left(p_{1}\right): 22$ |  |  |  |

TABLE II
Parameter LeVels

| $\begin{aligned} & \text { factors } \\ & \text { levels } \end{aligned}$ | $\zeta_{e}$ | $\zeta_{l}$ | AC |
| :--: | :--: | :--: | :--: |
| 1 | 0.2 | 0.02 | RW-AC |
| $\frac{3}{4}$ | 0.4 | 0.05 | B-AC |
| 3 | 0.6 | 0.08 | PD-AC |

## V. ILLUSTRATIVE EXAMPLE

The proposed deadlock-free local search algorithm is implemented in $\mathrm{C}++$. The size of the code file is 26 KB . It is compiled by MSBuild 4.0 and run on a $1.7-\mathrm{GHz}$ personal computer with 8 GB RAM. The operating system of the computer is Windows 7 Ultimate. The APNS in Fig. 1 is used to test the performance of the proposed algorithm. Suppose that the numbers of type-1 4 parts are all 10. Let $[1,10],[11,20],[21,30]$, and $[31,40]$ denote the codes of type-1 4 parts, respectively. The processing time is randomly distributed in the range of $[15,40]$ for all manufacturing and assembly activities, as shown in Table I. The experimental data and main bodies of the code are available at https://github.com/luojianchao/ILS4FAS. The performance of the proposed deadlock-free local search algorithm may be affected by the size of the population, the maximum number of generations, $\zeta_{p}, \zeta_{l}, \mathrm{AC}$, and perturbation policy. Generally speaking, the larger the population size or the maximum number of generations is, the better the algorithm's performance. Thus, the effectiveness of the population size and the maximum number of generations is certain. They are fixed as 20 and 2000, respectively. To test the effectiveness of the other factors, the following experiments are conducted.

In order to compare PD-AC with existing ACs, we implement another two ACs, i.e., roulette wheel-based AC (RWAC) [25] and the better AC (B-AC) [49]. Let $\left\{\Gamma_{j} \mid j \in \mathbb{N}_{2 \beta}\right\}$ be the set of all chromosomes in the incumbent population and newly generated one. In RW-AC, the selection probability of a chromosome $\Gamma_{j}\left(j \in \mathbb{N}_{2 \beta}\right)$ is $P\left(\Gamma_{j}\right)=f\left(\Gamma_{j}\right) / \sum_{i=1}^{2 \beta} f\left(\Gamma_{i}\right)$, where $f\left(\Gamma_{j}\right)=\left(\max \left\{\gamma\left(\Gamma_{k}\right) \mid k \in \mathbb{N}_{2 \beta}\right\}-\gamma\left(\Gamma_{j}\right)+1\right) /\left(\max \left\{\gamma\left(\Gamma_{k}\right) \mid\right.\right.$ $\left.k \in \mathbb{N}_{2 \beta}\right\}-\min \left\{\gamma\left(\Gamma_{k}\right) \mid k \in \mathbb{N}_{2 \beta}\right\}+1$ ).

To test effectiveness of $\zeta_{p}, \zeta_{l}$, and AC , a design-ofexperiment (DOE) [54] method is used. They all have three levels, as shown in Table II. Thus, a DOE with size $L_{9}\left(3^{4}\right)$ is selected. The proposed algorithm runs ten times at each factor combination. The average makespan is taken as an evaluation index. The final orthogonal experiment table is shown in Table III, and the range and rank of $\zeta_{p}, \zeta_{l}$, and AC are given in Table IV.

Since $\zeta_{p}$ owns the biggest range, it affects the performance of the proposed algorithm most. If it is too small, all chromosomes search toward the best chromosomes. The algorithm is easy to premature. If it is too big, the search direction is

TABLE III
Orthogonal Table and Average MAKEsPan

| columns <br> experiments | $\zeta_{c}$ | $\zeta_{l}$ | AC |  | Average <br> makespan |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1 | 2 | 3 | 4 |  |
| 2 | 1 | 1 | 1 | 1 | 580.8 |
| 3 | 1 | 2 | 2 | 2 | 578.9 |
| 4 | 2 | 1 | 2 | 3 | 574.2 |
| 5 | 2 | 2 | 3 | 1 | 568.0 |
| 6 | 2 | 3 | 1 | 2 | 568.8 |
| 7 | 3 | 1 | 3 | 2 | 576.4 |
| 8 | 3 | 2 | 1 | 3 | 570.7 |
| 9 | 3 | 3 | 2 | 1 | 581.9 |

TABLE IV
Response Table

| $\begin{aligned} & \text { factors } \\ & \text { levels } \end{aligned}$ | $\zeta_{c}$ | $\zeta_{l}$ | AC |
| :--: | :--: | :--: | :--: |
| 1 | 1733.9 | 1732 | 1720.3 |
| 2 | 1711.6 | 1717.6 | 1735.6 |
| 3 | 1729 | 1724.9 | 1718.6 |
| range | 22.3 | 14.4 | 17 |
| rank | 1 | 3 | 2 |

TABLE V
Simulation Results Under Different Perturbation Policy

| EDA-P |  | R-P (0.1) |  | R-P (0,2) |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Makespan | RT(s) | Makespan | RT(s) | Makespan | RT(s) |
| 570 | 81 | 558 | 83 | 590 | 82 |
| 585 | 79 | 578 | 76 | 581 | 78 |
| 572 | 76 | 573 | 75 | 588 | 71 |
| 562 | 79 | 561 | 78 | 580 | 81 |
| 575 | 74 | 586 | 79 | 587 | 76 |
| 585 | 73 | 538 | 77 | 563 | 79 |
| 598 | 79 | 567 | 81 | 573 | 74 |
| 578 | 78 | 575 | 78 | 596 | 76 |
| 558 | 75 | 566 | 79 | 574 | 73 |
| 575 | 79 | 578 | 78 | 547 | 77 |

too random. The algorithm performs like a random search. AC ranks second. Since PD-AC accepts chromosomes with both diversity and optimality, it can avoid repeated search to some extent, and thus achieves high search efficiency. Comparing with $\zeta_{p}$ and $\mathrm{AC}, \zeta_{l}$ affects the performance of the algorithm least. However, a reasonable factor selection can help the algorithm perform better. Based on the previous analysis, they are selected as: $\zeta_{p}=0.4, \zeta_{l}=0.05$, and $\mathrm{AC}=\mathrm{PD}-\mathrm{AC}$.

To test the effectiveness of EDA-P, a random perturbation (R-P) policy is developed. The R-P policy is the same as the local search operation proposed in the last section besides that the range of $\zeta_{l}$ is different. According to [49], we know that the strength of a perturbation policy should not be weaker than a local search. Otherwise, the algorithm can fall back into the local optimum just visited. Because the maximum $\zeta_{l}$ in the local search is set to be 0.1 , let $\zeta_{l} \in[0.1,1]$ in R-P. Two R-P policies with $\zeta_{l}=0.1$ and 0.2 , respectively, are implemented. The proposed algorithm under EDA-P ( $\zeta_{p}=0.4$ ), R-P (0.1), and R-P (0.2) all run ten times. Simulation results are shown in Table V, where RT means run time (in seconds).

The average makespan under EDA-P, R-P (0.1), and R-P (0.2) is 568, 575.8, and 577.9, respectively, and the average run time under EDA-P, R-P (0.1), and R-P (0.2) is 78.4, 77.3,
![img-4.jpeg](img-4.jpeg)

Fig. 5. Changing trend of the current best solution.
and 76.7 s , respectively. The best solutions found under EDAP, R-P (0.1), and R-P (0.2) have makespan 538, 558, and 547, respectively. Although the best solution found under R-P (0.2) is better than that under R-P (0.1), the average makespan under R-P (0.2) is larger than that under R-P (0.1). It means that the search under R-P (0.2) likes a random restart search. It may obtain some excellent solutions. However, the average performance of the found solutions is not so good. EDA-P performs the best among them. That means EDA-P owns stronger global search ability than both R-P (0.1) and R-P (0.2).

Our algorithm has two characteristics: 1) its optimization objective is to minimize the total completion time or makespan and 2) the solution with minimum makespan is kept for the next generation. Theoretically, if every solution can be searched, then it converges to the global optimum. Besides, we can analyze its convergence by the tested results. The process of finding the solution with makespan 538 is tracked in Fig. 5. From Fig. 5, we find that the makespan of the current best solution decreases with the number of generations. That means our algorithm converges toward the optimal solution as the search goes on. It is suitable for the studied NP-hard scheduling problem since it can generate better solutions as more time is given.

## VI. CONCLUSION

This work studies the scheduling problem of deadlock-prone FASs. As far as we know, such a problem has never been reported in the existing literature. To solve it, a deadlock-free local search scheduling algorithm is proposed. It finds optimal or near-optimal deadlock-free schedules at given initial marking. To avoid deadlocks, an existing deadlock prevention policy is redefined in a concise way. The redefined one is analogous to the original one, but can be easily embedded in a scheduling algorithm. Then, the redefined deadlock prevention policy is embedded into an RA by which all chromosomes are amended into feasible ones that can be decoded into deadlock-free schedules. To enhance the global search ability of the proposed local search algorithm, a perturbation policy based on the EDA is proposed. Moreover, a novel PD-AC is developed to keep high-quality and high-diversity chromosomes. Experimental results show the effectiveness of the proposed scheduling algorithm. The proposed local search algorithm can be improved by proposing different local search

operations. Improving deadlock prevention policies in terms of their optimality and computation complexity and their usage in scheduling requires future research.

## ACKNOWLEDGMENT

The authors would like to thank the Editor, Associate Editor, and all anonymous reviewers for their thoughtful comments and suggestions that have greatly helped improve the presentation and technical quality of this paper.

## REFERENCES

[1] I. B. Abdallah, H. A. Elmaraghy, and T. Elmekkawy, "Deadlock-free scheduling in flexible manufacturing systems using Petri nets," Int. J. Prod. Res., vol. 40, no. 12, pp. 2733-2756, Feb. 2002.
[2] O. T. Baruwa, M. A. Piera, and A. Guasch, "Deadlock-free scheduling method for flexible manufacturing systems based on timed colored Petri nets and anytime heuristic search," IEEE Trans. Syst., Man, Cybern., Syst., vol. 45, no. 5, pp. 831-846, May 2015.
[3] Y. F. Chen and Z. W. Li, "Design of a maximally permissive livenessenforcing supervisor with a compressed supervisory structure for flexible manufacturing systems," Automatica, vol. 47, no. 5, pp. 1028-1034, May 2011.
[4] S. F. Chew and M. A. Lawley, "Robust supervisory control for production systems with multiple resource failure," IEEE Trans. Autom. Sci. Eng., vol. 3, no. 3, pp. 309-323, Jul. 2006.
[5] R. K. Congram, C. N. Potts, and S. L. Van De Velde, "An iterated dynasearch algorithm for the single-machine total weighted tardiness scheduling problem," INFORMS J. Comput., vol. 14, no. 1, pp. 52-67, Jan. 2002.
[6] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, "A fast and elitist multiobjective genetic algorithm: NSGA-II," IEEE Trans. Evol. Comput., vol. 6, no. 2, pp. 182-197, Apr. 2002.
[7] J. Ezpeleta, J. M. Colom, and J. Martinez, "A Petri net based deadlock prevention policy for flexible manufacturing systems," IEEE Trans. Robot. Autom., vol. 11, no. 2, pp. 173-184, Apr. 1995.
[8] M. P. Fanti, G. Maione, and B. Turchiano, "Design of supervisors to avoid deadlock in flexible assembly systems," Int. J. Flexible Manuf. Syst., vol. 14, no. 2, pp. 157-175, Apr. 2002.
[9] H. X. Liu, W. Wu, H. Su, and Z. Zhang, "Design of optimal Petrimet controllers for a class of flexible manufacturing systems with key resources," Inf. Sci., vol. 363, pp. 221-234, Oct. 2015.
[10] L. B. Han, K. Y. Xing, M. C. Zhou, X. Chen, and Z. X. Gao, "Efficient optimal deadlock control of flexible manufacturing systems," IET Control Theory Appl., vol. 10, no. 10, pp. 1181-1186, Jun. 2016.
[11] L. B. Han, K. Y. Xing, X. Chen, H. Lei, and F. Wang, "Deadlockfree genetic scheduling for flexible manufacturing systems using Petri nets and deadlock controllers," Int. J. Prod. Res., vol. 52, no. 5, pp. 1557-1572, Oct. 2013.
[12] F.-S. Hsieh, "Robustness analysis of Petri nets for assembly/disassembly processes with unreliable resources," Automatica, vol. 42, no. 7, pp. 1159-1166, Jul. 2006.
[13] F.-S. Hsieh, "Analysis of flexible assembly processes based on structural decomposition of Petri nets," IEEE Trans. Syst., Man, Cybern. A. Syst., Humans, vol. 37, no. 5, pp. 792-803, Sep. 2007.
[14] F.-S. Hsieh, "Robustness analysis of holonic assembly/disassembly processes with Petri nets," Automatica, vol. 44, no. 10, pp. 2538-2548, Oct. 2008.
[15] H. Hu, M. C. Zhou, Z. W. Li, and Y. Tang, "Deadlock-free control of automated manufacturing systems with flexible routes and assembly operations using Petri nets," IEEE Trans. Ind. Informat., vol. 9, no. 1, pp. 109-121, Feb. 2013.
[16] H. Hu and M. C. Zhou, "A Petri net-based discrete-event control of automated manufacturing systems with assembly operations," IEEE Trans. Control Syst. Technol., vol. 23, no. 2, pp. 513-524, Mar. 2015.
[17] Y. S. Huang, M. D. Jeng, X. L. Xie, and S. L. Chung, "Deadlock prevention policy based on Petri nets and siphons," Int. J. Prod. Res., vol. 39, no. 2, pp. 283-305, Jan. 2001.
[18] P. Larrahaga and J. A. Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Boston, MA, USA: Kluwer, 2001.
[19] Z. W. Li and M. C. Zhou, "Control of elementary and dependent siphons in Petri nets and their application," IEEE Trans. Syst., Man, Cybern. A, Syst., Humans, vol. 38, no. 1, pp. 133-148, Jan. 2008.
[20] H. X. Liu, K. Y. Xing, M. C. Zhou, L. B. Han, and F. Wang, "Transition cover-based design of Petri net controllers for automated manufacturing systems," IEEE Trans. Syst., Man, Cybern., Syst., vol. 44, no. 2, pp. 196-208, Feb. 2014.
[21] J. C. Luo, K. Y. Xing, M. C. Zhou, X. L. Li, and X. N. Wang, "Deadlockfree scheduling of automated manufacturing systems using Petri nets and hybrid heuristic search," IEEE Trans. Syst., Man, Cybern., Syst., vol. 45, no. 3, pp. 530-541, Mar. 2015.
[22] L. Prroddi, R. Cordone, and I. Fumagalli, "Selective siphon control for deadlock prevention in Petri nets," IEEE Trans. Syst., Man, Cybern. A, Syst., Humans, vol. 38, no. 6, pp. 1337-1348, Nov. 2008.
[23] A.-S. Pepin, G. Desaulniers, A. Hertz, and D. Huisman, "A comparison of five heuristics for the multiple depot vehicle scheduling problem," $J$. Sched., vol. 12, pp. 17-30, Feb. 2009.
[24] S. E. Ramaswamy and S. B. Joshi, "Deadlock-free schedules for automated manufacturing workstations," IEEE Trans. Robot. Autom., vol. 12, no. 3, pp. 391-400, Jun. 1996.
[25] C. R. Reeves and J. E. Rowe, Genetic Algorithms-Principles and Perspectives: A Guide to GA Theory. Norwell, MA, USA: Kluwer, 2003.
[26] E. Roszkowska, "Supervisory control for deadlock avoidance in compound processes," IEEE Trans. Syst., Man, Cybern. A, Syst., Humans, vol. 34, no. 1, pp. 52-64, Jan. 2004.
[27] T. Stützte, "Iterated local search for the quadratic assignment problem," Eur. J. Oper. Res., vol. 174, no. 3, pp. 1519-1539, Nov. 2006.
[28] T. Murata, "Petri nets: Properties, analysis and applications," Proc. IEEE, vol. 77, no. 4, pp. 541-580, Apr. 1989.
[29] N. Viswanadham, Y. Narahari, and T. L. Johnson, "Deadlock prevention and deadlock avoidance in flexible manufacturing systems using Petri net models," IEEE Trans. Robot. Autom. Mag., vol. 6, no. 6, pp. 713-723, Dec. 1990.
[30] N. Q. Wu, M. C. Zhou, and Z. W. Li, "Resource-oriented Petri net for deadlock avoidance in flexible assembly systems," IEEE Trans. Syst., Man, Cybern. A, Syst., Humans, vol. 38, no. 1, pp. 56-69, Jan. 2008.
[31] N. Q. Wu and M. C. Zhou, "Avoiding deadlock and reducing starvation and blocking in automated manufacturing systems based on a Petri net model," IEEE Trans. Robot. Autom., vol. 17, no. 5, pp. 658-669, Oct. 2001.
[32] N. Q. Wu, M. C. Zhou, and G. Hu, "Petri net modeling and one-step look-ahead maximally permissive deadlock control of automated manufacturing systems," ACM Trans. Embedded Comput. Syst., vol. 12, no. 1, pp. 1-10, Jan. 2013.
[33] N. Q. Wu and M. C. Zhou, "Real-time deadlock-free scheduling for semiconductor track systems based on colored timed Petri nets," OR Spectr., vol. 29, no. 3, pp. 421-443, Jul. 2007.
[34] N. Q. Wu and M. C. Zhou, "Modeling, analysis and control of dual-arm cluster tools with residency time constraint and activity time variation based on Petri nets," IEEE Trans. Autom. Sci. Eng., vol. 9, no. 2, pp. 446-454, Apr. 2012.
[35] N. Q. Wu, M. C. Zhou, F. Chu, and C. Chu, "A Petri-net-based scheduling strategy for dual-arm cluster tools with wafer revisiting," IEEE Trans. Syst., Man, Cybern., Syst., vol. 43, no. 5, pp. 1182-1194, Sep. 2013.
[36] Y. C. Wu, K. Y. Xing, J. C. Luo, and Y. X. Feng, "Robust deadlock control for automated manufacturing systems with an unreliable resource," Inf. Sci., vols. 346-347, pp. 17-28, Jun. 2016.
[37] X. Gang and Z. M. Wu, "Deadlock-free scheduling strategy for automated production cell," IEEE Trans. Syst., Man, Cybern. A, Syst., Humans, vol. 34, no. 1, pp. 113-122, Jan. 2004.
[38] K. Y. Xing, B.-S. Hu, and H.-X. Chen, "Deadlock avoidance policy for Petri-net modeling of flexible manufacturing systems with shared resources," IEEE Trans. Autom. Control, vol. 41, no. 2, pp. 289-296, Feb. 1996.
[39] K. Y. Xing, F. Wang, M. C. Zhou, H. Lei, and J. C. Luo, "Deadlock characterization and control of flexible assembly systems with Petri nets," Automatica, vol. 87, pp. 358-364, Jan. 2018.
[40] K. Y. Xing, M. C. Zhou, H. X. Liu, and F. Tian, "Optimal Petri-net-based polynomial-complexity deadlock-avoidance policies for automated manufacturing systems," IEEE Trans. Syst., Man, Cybern. A, Syst., Humans, vol. 39, no. 1, pp. 188-199, Jan. 2009.
[41] K. Y. Xing, L. B. Han, M. C. Zhou, and F. Wang, "Deadlock-free genetic scheduling algorithm for automated manufacturing systems based on deadlock control policy," IEEE Trans. Syst., Man, Cybern. B, Cybern., vol. 42, no. 3, pp. 603-615, Jun. 2012.

[42] H. Yue, K. Xing, and Z. Hu, "Robust supervisory control policy for avoiding deadlock in automated manufacturing systems with unreliable resources," Int. J. Prod. Res., vol. 52, no. 6, pp. 1573-1591, Aug. 2013.
[43] M. C. Zhou and K. Venkatesh, Modeling, Simulation, and Control of Flexible Manufacturing Systems: A Petri Net Approach. Singapore: World Sci., 1998.
[44] M. C. Zhou and M. P. Fanti, Deadlock Resolution in ComputerIntegrated System. New York, NY, USA: Marcel Dekker, 2005.
[45] Y. Zhou, H. Hu, Y. Liu, and Z. Ding, "Collision and deadlock avoidance in multirobot systems: A distributed approach," IEEE Trans. Syst., Man, Cybern., Syst., vol. 47, no. 7, pp. 1712-1726, Jul. 2017.
[46] F. Lu, Q. Zeng, M. C. Zhou, Y. Bao, and H. Duan, "Complex reachability trees and their application to deadlock detection for unbounded Petri nets," IEEE Trans. Syst., Man, Cybern., Syst., to be published, doi: 10.1109/TSMC.2017.2692262.
[47] Y. Feng, K. Xing, Z. Gao, and Y. Wu, "Transition cover-based robust Petri net controllers for automated manufacturing systems with a type of unreliable resources," IEEE Trans. Syst., Man, Cybern., Syst., vol. 47, no. 11, pp. 3019-3029, Nov. 2017.
[48] Z. W. Li, M. C. Zhou, and N. Q. Wu, "A survey and comparison of Petri net-based deadlock prevention policies for flexible manufacturing systems," IEEE Trans. Syst., Man, Cybern. C, Appl. Rev., vol. 38, no. 2, pp. 173-188, Mar. 2008.
[49] H. Lourenço, O. C. Martin, and T. Stützle, "Iterated local search: Framework and applications," in Handbook of Metaheuristics, M. Gendreau and J.-Y. Potvin, Eds. Boston, MA, USA: Springer, 2010, pp. 363-397.
[50] S. Nguyen, M. Zhang, M. Johnston, and K. C. Tan, "Automatic programming via iterated local search for dynamic job shop scheduling," IEEE Trans. Cybern., vol. 45, no. 1, pp. 1-14, Jan. 2015.
[51] P. Li et al., "Iterated local search for distributed multiple assembly nowait flowshop scheduling," in Proc. IEEE Evol. Comput., San Sebastián, Spain, 2017, pp. 1565-1571.
[52] A. Subramanian, M. Battarra, and C. N. Potts, "An Iterated Local Search heuristic for the single machine total weighted tardiness scheduling problem with sequence-dependent setup times," Int. J. Prod. Res., vol. 52, no. 9, pp. 2729-2742, Feb. 2014.
[53] J. Xu, C.-C. Wu, Y. Yin, and W.-C. Lin, "An iterated local search for the multi-objective permutation flowshop scheduling problem with sequence-dependent setup times," Appl. Soft Comput., vol. 52, pp. 39-47, Mar. 2017.
[54] D. C. Montgomery, Design and Analysis of Experiments. New York, NY, USA: Wiley, 1984.
[55] X. Lu, M. C. Zhou, A. C. Ammari, and J. Ji, "Hybrid Petri nets for modeling and analysis of microgrid systems," IEEE/CAA J. Automatica Sinica, vol. 3, no. 4, pp. 349-356, Oct. 2016.
[56] N. Ran, H. Su, and S. Wang, "An improved approach to test diagnosability of bounded Petri nets," IEEE/CAA J. Automatica Sinica, vol. 4, no. 2, pp. 297-303, Apr. 2017.
[57] F. J. Yang, N. Q. Wu, Y. Qiao, and R. Su, "Polynomial approach to optimal one-wafer cyclic scheduling of treelike hybrid multi-cluster tools via Petri nets," IEEE/CAA J. Automatica Sinica, vol. 5, no. 1, pp. 270-280, Jan. 2018.
[58] G. Mitsuo and R. W. Cheng, Genetic Algorithms and Engineering Optimization. New York, NY, USA: Wiley, 2000.
[59] M. G. Filho, C. F. Barco, and R. F. T. Neto, "Using Genetic Algorithms to solve scheduling problems on flexible manufacturing systems (FMS): A literature survey, classification and analysis," Flexible Services Manuf. J., vol. 26, no. 3, pp. 408-431, 2014.
[60] J. C. Luo, K. Y. Xing, and M. C. Zhou, "Deadlock and blockage control of automated manufacturing systems with an unreliable resource," Asian J. Control, to be published, doi: 10.1002/asjc. 1856.
[61] J. C. Luo, K. Y. Xing, M. C. Zhou, X. L. Li, and X. N. Wang, "Scheduling of deadlock and failure-prone automated manufacturing systems via hybrid heuristic search," Int. J. Prod. Res., vol. 55, no. 11, pp. 3283-3293, 2017.
[62] F. J. Yang, N. Q. Wu, Y. Qao, M. C. Zhou, and Z. W. Li, "Scheduling of single-arm cluster tools for an atomic layer deposition process with residency time constraints," IEEE Trans. Syst., Man, Cybern., Syst., vol. 47, no. 3, pp. 502-516, Mar. 2017.
[63] Y. Hou, N. Q. Wu, M. C. Zhou, and Z. W. Li, "Pareto-optimization for scheduling of crude oil operations in refinery via genetic algorithm," IEEE Trans. Syst., Man, Cybern., Syst., vol. 47, no. 3, pp. 517-530, Mar. 2017.
[64] J. C. Luo, Z. Q. Liu, and K. Y. Xing, "Hybrid branch and bound algorithms for the two-stage assembly scheduling problem with separated setup times," Int. J. Prod. Res., to be published, doi: $10.1080/00207543.2018 .1489156$.
[65] C. Pan, M. C. Zhou, Y. Qiao, and N. Q. Wu, "Scheduling cluster tools in semiconductor manufacturing: Recent advances and challenges," IEEE Trans. Autom. Sci. Eng., vol. 15, no. 2, pp. 896-899, Apr. 2018.
[66] F. Yang, N. Wu, Y. Qiao, and M. C. Zhou, "Optimal one-wafer cyclic scheduling of time-constrained hybrid multicluster tools via Petri nets," IEEE Trans. Syst., Man, Cybern., Syst., vol. 47, no. 11, pp. 2920-2932, Nov. 2017.
![img-5.jpeg](img-5.jpeg)

JianChao Luo received the Ph.D. degree in control science and engineering from Xi'an Jiaotong University, Xi'an, China, in 2016.

He joined the Northwestern Polytechnical University, Xi'an, in 2017, where he is currently an Assistant Professor of Software Engineering. His current research interests include deadlock-free scheduling and control of AMS.
![img-6.jpeg](img-6.jpeg)

ZhiQiang Liu received the Ph.D. degree in computer science and engineering from Northwestern Polytechnical University, Xi'an, China, in 2007.

He is currently an Associate Professor of Software Engineering with Northwestern Polytechnical University. His current research interests include safety critical software, data analysis, and deadlock-free scheduling and control of AMSs.
![img-7.jpeg](img-7.jpeg)

MengChu Zhou (S'88-M'90-SM'93-F'03) received the Ph.D. degree in computer and systems engineering from Retoselaer Polytechnic Institute, Troy, NY, USA, in 1990.

He joined the New Jersey Institute of Technology, Newark, NJ, USA, in 1990, and currently a Distinguished Professor of Electrical and Computer Engineering. He has over 700 publications including 12 books, over 400 journal papers ( $300+$ in IEEE Transactions), 11 patents, and 28 book-chapters. His current research interests include Petri nets, intelligent automation, Internet of Things, big data, Web services, and intelligent transportation.

Dr. Zhou is the Founding Editor of IEEE Press Book Series on Systems Science and Engineering. He is a fellow of the International Federation of Automatic Control, American Association for the Advancement of Science, and Chinese Association of Automation.
![img-8.jpeg](img-8.jpeg)

KeYi Xing received the Ph.D. degree in systems engineering from Xi'an Jiaotong University, Xi'an, China, in 1994.

He is currently a Professor of Systems Engineering with the State Key Laboratory for Manufacturing Systems Engineering and the Systems Engineering Institute, Xi'an Jiaotong University. His current research interest includes control and scheduling of AMSs.