# A Hybrid Estimation-of-Distribution Algorithm for Scheduling Flexible Job Shop With Limited Buffers Based on Petri Nets 

ZHENXIN GAO*, YANXIANG FENG*, AND KEYI XING*<br>State Key Laboratory for Manufacturing Systems Engineering, Xi’an Jiaotong University, Xi’an 710049, China<br>Systems Engineering Institute, Xi'an Jiaotong University, Xi'an 710049, China<br>Corresponding authors: Yanxiang Feng (fengyxss@stu.xjtu.edu.cn) and Keyi Xing (kyxing@xjtu.edu.cn)

This work was supported in part by the National Natural Science Foundation of China under Grant 61573278 and in part by the National Science Foundation for Post-Doctoral Scientists of China under Grant 2018M643660.


#### Abstract

This article focuses on the production scheduling problem in the flexible job shop (FJS) environment with limited buffers. Limited manufacturing resources and buffers may lead to blockage and deadlock phenomenon. In order to establish production scheduling with minimum makespan, the timed Petri net (PN) model of a production process is established. Based on this PN model, a novel Hybrid Estimation-of-Distribution Algorithm (HEDA) is proposed for solving the considered scheduling problem. A candidate solution for the problem is coded as an individual that consists of a route sequence for processing jobs and a permutation with repetition of jobs. A deadlock prevention policy is used to check the feasibility of individuals, such that it can be decoded into a feasible sequence of transitions, i.e., a feasible schedule. By using an effective voting procedure of elite individuals, two probability models in HEDA corresponding to different subsections of individuals are constructed. Based on the probability models, offspring individuals are then produced. As an improvement strategy, simulated-annealing-based local search is designed and incorporated into HEDA to enhance the entire algorithm's search ability. The proposed hybrid HEDA is tested on FJS examples. The results show its feasibility and effectiveness.


#### Abstract

INDEX TERMS Flexible job shop (FJS), limited buffers, scheduling, hybrid estimation-of-distribution algorithm (HEDA), petri net (PN).


## I. INTRODUCTION

In the classical scheduling problems, whether job-shop or flow-shop scheduling problems (JSSP or FSSP), infinite sizes of buffers for storing jobs are usually assumed [1], [2]. While, in many real production systems, the buffer space for storing jobs is usually limited, such as in flow shop [3]-[8], job-shop [1], [9]-[19], and automated manufacturing systems [20]. In these manufacturing systems, the total resources (machines, transportation equipment, buffers, etc.) to hold the jobs are limited, and hence in the process of system operation, if the resources are not allocated properly, it often encounters blocking and/or even deadlock [11]-[13], [16], [20]-[24], [42]-[44]. Therefore, in order to run such manufacturing systems effectively, we need to consider two problems: liveness control and optimal scheduling. The goal of control is to ensure the normal operation of a system without deadlock,

[^0]so as to complete all production tasks, while scheduling is to allocate resources to tasks reasonably, so as to optimize the (some) performance of the system on the basis of liveness control. These problems create a relatively new and more significant research direction, and have attracted many researchers [11], [12], [20]-[25].

Papadimitriou and Kanellakis [6] studied the complexity of FSSP with limited buffers and shown that even the simplest two machine flow-shop problem with a limited buffer between two machines is strongly NP-hard. Hence, to solve scheduling problems of manufacturing system with limited buffer capacities, especially, deadlock-prone manufacturing system, in reasonable time, heuristics and metaheuristics have to be applied. So far, many approximate algorithms have been developed in the literature for solving such complex manufacturing system scheduling problems.

On FSSP with limited buffers, many studies have been done and most works concern the problem with makespan objective [4], [5], [7], [8], [26], [27]. Compared to the


[^0]:    The associate editor coordinating the review of this manuscript and approving it for publication was Xiaoou Li ${ }^{\text {® }}$.

FSSP with limited buffer constraints in the literature, JSSP with limited buffer has received much less attention [9], [11]-[14], [19], and in these existing studies, it is focused on the special cases, where all buffers have capacity 0 , called the blocking job-shop problem [28]-[31]. In the literature, one of the main reasons for neglecting the impact of finite buffers is that compared with flexible job shop (FJS) scheduling problem, FJS scheduling problem with finite buffer, although both are NP-hard, is more complex and contains more constraints; while the other and most important reason is that the limited capacity buffer constraints in the job-shop environment leads to so-called deadlocks, and the detection and resolution of such deadlocks is also NP-hard. Mascis and Pacciarelli [30] studied JSSP with blocking and no-wait constraints, and established the complexity results of the problem. Brucker et al. [9] and Heitmann [14] investigated several types of JSSPs with limited buffer constraints by classifying buffers into three classes: (i) machine-dependent output buffers, (ii) machine-dependent input buffers, and (iii) job-dependent buffers. Based on the alternative and disjunctive graph models, representations of feasible solutions for job shop with limited buffers are investigated in [9] and a constructive heuristic to find feasible solutions is presented. Fahmy et al. [11], [12] presented an insertion heuristic based on matrices and Latin rectangles. This heuristic is capable to take into account limited buffer capacities and to avoid deadlocks, and hence, can obtain a feasible schedule. However, the computation time is longer, especially when applying the procedure within metaheuristics. Pranzo and Pacciarelli [16] proposed an iterative greedy algorithm to solve two types of blocking job shop scheduling problems, one with swap allowed and the other with no swap allowed. The need to swap jobs between machines (and buffers) arises whenever there is a circular set of blocking or deadlock jobs in which each job is waiting for a machine (or a buffer space) occupied by other jobs in the same set, that is, this set of jobs are in deadlock state. By swapping jobs, deadlock is resolved. But this swapping actually requires additional equipment to complete. For JSSP with buffer constraints and jobs consuming variable buffer space, Witt and Vo $\beta$ [19] presented a heuristic to find feasible solutions. Gomes et al. [13] investigated the scheduling problem of flexible job shop (FJS) with groups of parallel homogeneous machines and limited intermediate buffers, discrete parts manufacturing industries that operate on a make-to-order basis. Under the assumption that after the job is processed on the machine, there must be buffer space to store it, the integer linear programming model of the scheduling problem is developed, and by solving this integer linear programming, an optimal schedule is obtained.

Automated manufacturing systems, especially flexible manufacturing systems (FMS) can be considered as a generalization of the FJSs with limited capacity buffers. Both of them are faced with deadlock and have the same deadlock characteristics. The deadlock problem of FMSs has been widely studied, and many deadlock control policies are presented [20]-[24]. Deadlocks in FJSs with limited capacity
buffers can be handled according to deadlock control methods in FMSs. These methods provide a necessary and feasible control basis for solving the scheduling problem of FJSs with limited buffers.

This article focuses on the production scheduling problem of flexible job shop manufacturing environment with limited capacity buffers, where buffers are machine-dependent, that is, a machine and its buffer form a manufacturing cell or workstation, and the buffer is used to store the jobs that need to be processed or have been finished on the machine. This kind of buffers is widely used in automatic production line [9], [12], [14], [18], [28], railway network [10], [29], aircraft traffic control [17], and so on. The shop manufactures medium-volume discrete jobs (or, parts, products) of different types in a make-to-order basis as in Gomes et al. [13]. An order or a type of jobs, consists of a number of jobs to be produced and their processing routes. The re-circulation of jobs in the considered flexible job shops is permitted, that is, jobs can visit some machines more than once, as in FMSs. Furthermore, as in the classical job-shop problem, we assume that all jobs are available at the beginning time, and each job leaves the system directly after the finishing of its last operation, i.e. that sufficient buffer space is available to store all completed jobs. For such a manufacturing shop, the scheduling problem with the completion time as the optimization goal is investigated in this study. From the above literature review, the scheduling problem of such FJS with limited capacity buffers is rarely studied. In fact, to our best knowledge, no work has provided a systematic study and a feasible solution to this scheduling problem.

Note that FJS scheduling problem (with infinite buffers) and FJS scheduling problem with limited buffers have essential differences. To solve flow shop and flexible job shop scheduling problems, many algorithms have been proposed, such as particle swarm optimization [4], discrete differential evolution algorithm [5], artificial bee colony algorithm [27], estimation of distribution algorithm [33], and genetic algorithm [35]. In these algorithms, the individual's feasibility is determined by the individual's encoding, that is to say, each candidate individual can be decoded into a feasible schedule. For FJSs with limited buffers, the feasibility of an individual cannot be guaranteed by encoding, that is to say, a candidate individual may not be able to decode into a feasible schedule. Therefore, it is necessary to detect the feasibility of individuals and correct the infeasible individuals into the feasible individuals. From this point, we can know that the FJS scheduling problem with infinite buffers is totally different from that with limited buffers, and the evolutionary algorithms for the former has no deadlock avoidance mechanism, and hence, cannot be directly used for the latter.

This article uses place-timed Petri nets (PNs) to model FJSs with limited buffers. Petri net is an effective tool for modeling discrete event systems [37]-[41]. In view of the complexity of the considered scheduling problem, the estimation of distribution algorithm (EDA) is used to solve it. EDA is an evolutionary algorithm that has received much

attentions of many researchers [32]. It uses neither crossover nor mutation operator, but reproduces offsprings based on a probabilistic model learned from a population of parents. This model-based approach to optimization allows EDA to successively solve many complex and large problems [32], [33]. In this article, a candidate solution for the scheduling problem is denoted as an individual. Because of route flexibility, a feasible solution not only specifies a processing route for each job, but also determines a processing sequence of operations of all jobs. Hence, an individual designed in this article consists of two parts. The first part is a sequence of routes for jobs and the second one is a permutation with repetition of jobs. By letting the $i$-th occurrence of a job in the permutation of an individual correspond to the $i$-th operation of the job and using route information in the first part, the individual can be decoded as a candidate solution. Note that such a candidate solution may be not feasible, and can cause deadlock. In this article, by embedding a deadlock detection and avoidance policy into a decoding process, the feasibility of a candidate solution obtained by decoding an individual can be guaranteed.

Corresponding to the structure of individuals, two probabilistic models, route and operation probabilistic models, are generated by a simple vote of elite individuals and taking into account their weights. Based on these probabilistic models, offspring individuals are then produced. Moreover, to balance the global and local searches and to further improve the performance of EDA, the simulated annealing based local search is designed and incorporated into EDA. The proposed hybrid EDA is tested on a set of FJS examples, showing its feasibility and effectiveness.

The rest of this article is organized as follows. Section II introduces the considered FJSs with limited buffers and batch production, and develops their PN models. A novel hybrid estimation of distribution algorithm for the considered FJS is described in Section III. An example is given to show the effectiveness of the proposed scheduling method in Section IV. Section V concludes this article.

## II. PRELIMINARY

In this section, we first introduce the considered FJSs and then establish their Petri net models. For concepts and notations of Petri nets, a reader is referred to [34].

## A. BASIC DEFINITIONS AND NOTATIONS OF PNS

A PN is a three-tuple $N=(P, T, F)$, where $P$ and $T$ are are finite sets of places and transitions, respectively., respectively, $F \subseteq(P \times T) \cup(T \times P)$ is the set of directed arcs. Given a node $x \in P \cup T$, the preset and post-set of $x$ are defined as ${ }^{\bullet} x=\{y \in P \cup T \mid(y, x) \in F\}$ and $x^{\bullet}=\{y \in P \cup T \mid(x, y) \in$ $F\}$, respectively. These notations can be extended to a set, for example, let $S \subseteq P \cup T$, then ${ }^{\bullet} S=\cup_{x \in S}^{\bullet} x$ and $S^{\bullet}=\cup_{x \in S} x^{\bullet}$.

A marking of $N$ is a mapping $M: P \rightarrow Z$ where $Z \equiv$ $\{0,1,2, \ldots\}$. Given a place $p \in P$ and a marking $M, M(p)$ denotes the number of tokens in $p$ at $M$. Let $S \subseteq P$ be a set of places; the total number of tokens in all places of $S$ at $M$ is
denoted by $M(S)$, i.e., $M(S)=\sum_{p \in S} M(p)$. A PN $N$ with an initial marking $M_{0}$ is called a marked PN, denoted as $\left(N, M_{0}\right)$.

A transition $t \in T$ is enabled at marking $M$, denoted by $M[t>$, if $\forall p \in{ }^{\bullet} t, M(p) \geq 1$. An enabled transition $t$ at $M$ can be fired, resulting in a new marking $M_{1}$, denoted by $M\left[t>M_{1}\right.$, where $M_{1}(p)=M(p)-1, \forall p \in{ }^{\bullet} t \backslash t^{\bullet}, M_{1}(p)=$ $M(p)+1, \forall p \in t^{\bullet} \backslash^{\bullet} t$, and, otherwise, $M_{1}(p)=M(p)$.

A sequence of transitions $\alpha=t_{1} t_{2} \ldots t_{k}$ is feasible from marking $M$ if there exists $M_{i}\left[t_{i}>M_{i+1}, \forall i \in Z_{k} \equiv\right.$ $\{1,2, \ldots, k\}$, where $M_{1}=M$. We state that $M_{i}$ is a reachable marking from $M$. Let $R\left(N, M_{0}\right)$ denote the set of all reachable markings of $N$ from $M_{0}$.

A path is a string $\tau=x_{1} x_{2} \ldots x_{k}$, where $x_{i} \in P \cup T$ and $\left(x_{i}, x_{i+1}\right) \in F, \forall i \in Z_{k-1}$. A path $\tau=x_{1} x_{2} \ldots x_{k}$ is a circuit if $x_{1}=x_{k}$.

## B. FJS WITH LIMITED BUFFERS

The FJS considered in this article consists of $u$ workstations, $w_{1}-w_{u}$, and can process $v$ types of jobs, $q_{1}-q_{v}$. A workstation is a machine with a finite buffer. The machine is used to process jobs, while the buffer is for staging and storing jobs.

Let $W=\left\{w_{i}, i \in Z_{u}\right\}$ and $Q=\left\{q_{i}, i \in Z_{v}\right\}$. Suppose that workstation $w_{i}$ has machine $m_{i}$ and its buffer capacity is $C\left(w_{i}\right)$, i.e., it can simultaneously hold at most $C\left(w_{i}\right)$ jobs. Each job only occupies a unit buffer space at any time and the machine is not idle as long as there are unprocessed jobs in its buffer.

The considered FJS supports batch processing and route flexibility. That is, there are multiple jobs of the same type to be processed, and a job may have multiple processing routes. A processing route of a job is an ordered sequence of operations to be processed on machines with specified processing time. The same type of jobs has the same set of processing routes. Let $\varphi(q)$ be the number of type- $q$ jobs to be processed, and $n=\sum_{q \in Q} \varphi(q)$, the total number of jobs.

Suppose that type- $q$ jobs have $\mu(q)$ processing routes $\pi_{1}-\pi_{p(q)}$. Route $\pi_{i}$ can be expressed as $\pi_{i}=o_{i 1} o_{i 2} \ldots o_{i l i}$, where $o_{i j}$ is the $j$-th operation in $\pi_{i}$ and $l_{i} \equiv \lambda\left(\pi_{i}\right)$ is the length of route $\pi_{i}$. In this article, suppose that each operation requires only one predetermined machine for processing, and the processing time of operation $o_{i j}$ is $d\left(o_{i j}\right)$. Therefore, a processing route corresponds to a sequence of machine or workstations. Let $w\left(o_{i j}\right)$ denote the workstation with the machine required for processing operation $o_{i j}$. Then, $\pi_{i}$ is determined by the sequence of workstations $w\left(\pi_{i}\right)=$ $w\left(o_{i 1}\right) w\left(o_{i 2}\right) \ldots w\left(o_{i l i}\right)$. Let $\chi(q)=\max \left\{\lambda\left(\pi_{i}\right) \mid \pi_{i}\right.$ is a processing route for type- $q$ jobs $\}$. Since the same type of jobs has the same set of processing routes, we also use $\chi(J)$ to denote the maximum length of processing routes for job $J$, that is, if $J$ is a type- $q$ job, then $\chi(J)=\chi(q)$.

For convenience's sake, to type- $q$ jobs, two fictitious operations, $o_{q s}$ and $o_{q e}$, are added, while $w\left(o_{q s}\right) \equiv b_{q s}$ and $w\left(o_{q e}\right) \equiv b_{q e}$ are two fictional infinite buffers used to store raw and processed type- $q$ jobs, respectively. Then, route $\pi_{i}$ is extended and still denoted as $\pi_{i}$, i.e., $\pi_{i}=o_{q s} o_{i 1} o_{i 2} \ldots o_{i l i} o_{q e}$, or $w\left(\pi_{i}\right)=w\left(o_{q s}\right) w\left(o_{i 1}\right) w\left(o_{i 2}\right) \ldots w\left(o_{i l i}\right) w\left(o_{q e}\right)$.

To perform its operation $o_{i j}$, a type- $q$ job $J_{i}$ first enters the buffer of workstation $w\left(o_{i j}\right)$, and then, when the machine in $w\left(o_{i j}\right)$ is available, it is processed for $d\left(o_{i j}\right)$ time units without preemption. During the time in workstations, no matter what state a job is in (waiting to be processed, being processed, or has been processed), it always occupies a unit buffer space.

The scheduling objective is to minimize the completion time of the last job to leave the system or makespan.

## C. PN MODEL OF FJS WITH LIMITED BUFFERS

In this article, Petri nets are used to model the considered FJSs. To establish the PN model of such an FJS with limited buffers, we first model processing routes of jobs, and then the request, utilization, and release of resources (machine and buffers) by jobs in workstations.

For a type- $q$ job $J$, one of its routes, $\pi_{i}=o_{q s} o_{i 1} o_{i 2} \ldots o_{i l}$ $o_{q e}$, is modeled by a path of transitions and operation places, denoted as $O\left(\pi_{i}\right)=p_{q s} t_{i 1} p_{i 11} t_{i 11} p_{i 12} t_{i 12} p_{i 13} t_{i 2} p_{i 21} t_{i 21} p_{i 22}$ $t_{i 22} p_{i 23} t_{i 3} \ldots t_{i l} p_{i l 1} t_{i l 1} p_{i l 2} t_{i l 2} p_{i l 3} t_{i l+1} p_{q e}$, and called as an operation path (O-path), where operation places $p_{q s}$ and $p_{q e}$ represent fictitious operations $o_{q s}$ and $o_{q e}$, respectively. Operation $o_{i j}$ of job $J$ is processed in workstation $w\left(o_{i j}\right)$. Its activities in $w\left(o_{i j}\right)$ are simulated by path $t_{i j} p_{i j 1} t_{i j 1} p_{i j 2} t_{i j 2} p_{i j 3} t_{i i j+1)}$. The firing of transition $t_{i j}$ implies that job $J$ leaves the current workstation $w\left(o_{i(j-1)}\right)$ or $b_{q s}$ and enters the buffer of the next workstation $w\left(o_{i j}\right)$ or $b_{q e}$ if $o_{i(j-1)}$ is the last operation of the job. To make it clear that the relationship between transition $t_{k l}$ and operation $o_{i j}$, the notation $t_{i j}\left[o_{i j}\right]$ will be used, and $t_{k l}$ is called the preparatory transition of operation $o_{i j}$. The firings of transitions $t_{i j 1}$ and $t_{i j 2}$ represent the processing beginning and end of operation $o_{i j}$, respectively. Places $p_{i j 1}$ and $p_{i j 3}$ are used to store the jobs whose operation $o_{i j}$ has not started and has completed, respectively, so they are non-timed, that is, the sojourn time of tokens in them is 0 and can leave at any time. Place $p_{i j 2}$ represents that operation $o_{i j}$ is being processed by machine, and hence it is timed, and the sojourn time of the token in place $p_{i j 2}$ is the processing time of operation $o_{i j}$, that is, the sojourn time is $d\left(o_{i j}\right)$.

Hence, the PN model of routes for type- $q$ jobs can be denoted as

$$
\left(N_{q}, M_{q 0}\right)=\left(P_{O q} \cup\left\{p_{q s}, p_{q e}\right\}, T_{q}, F_{q}, M_{q 0}\right)
$$

where $P_{O q}$ is the set of operation places, $p_{i j 1}, p_{i j 2}, p_{i j 3}$, corresponding to various states of jobs in the workstations. $T_{q}$ and $F_{q}$ are the sets of all transitions and arcs in all O-paths for type- $q$ jobs. $M_{q 0}$ is the initial marking, $M_{q 0}\left(p_{q s}\right)=\varphi(q)$ and $M_{q 0}(p)=0, \forall p \in P_{O q} \cup\left\{p_{q e}\right\}$.

In $N_{q}, \forall t \in T_{q},\left\lvert\, \begin{aligned} & \bullet t \\ & \bullet \end{aligned}\right|=|t \bullet|=1$, that is, $N_{q}$ is a state machine, and consists of all O-paths from $p_{q s}$ to $p_{q e}$. Such a path corresponds to a processing route of type- $q$ jobs. A place $p \in P_{q}$ is called a split place if $\left|p^{\bullet}\right|>1$. From a split place, jobs can choose their future processing routes.

In order to model the request and release of resources (buffers or machines) in Petri net, assign two places corresponding to workstation $w_{k}$ and its machine $m_{k}$ respectively, denoted also by $w_{k}$ and $m_{k}$ for simplicity.

A token in $w_{k}$ represents an available unit buffer space. The initial marking of $w_{k}$ is $C\left(w_{k}\right)$. Let $P_{W}=\left\{w_{1}, \ldots, w_{n}\right\}$, the set of all workstation places. Similarly, let $P_{M}=$ $\left\{m_{1}, \ldots, m_{n}\right\}$ the set of all machine places.

A token in $m_{k}$ indicates that machine $m_{k}$ is idle and available. Since we assume that buffers are machine-dependent in this article, there is only one machine per workstation. That is, the initial marking of place $m_{k}$ is 1 .

Now consider the request and release of resources. Let $O\left(\pi_{i}\right)=p_{q s} t_{i 1} p_{i 11} t_{i 11} p_{i 12} t_{i 12} p_{i 13} t_{i 2} p_{i 21} t_{i 21} p_{i 22} t_{i 22} p_{i 23} t_{i 3} \ldots$ $t_{i l} p_{i l 1} t_{i l 1} p_{i l 2} t_{i l 2} p_{i l 3} t_{i l l+1} p_{q e}$ be an O-path of type- $q$ jobs. If the operation corresponding to $p_{i j 2}$ is processed by machine $m_{k}$ in workstation $w_{k}$, then add arcs $\left(w_{k}, t_{i j}\right)$ and $\left(t_{i j+1}\right), w_{k}$, representing the job entering and leaving $w_{k}$ respectively. At the same time, $\operatorname{arcs}\left(m_{k}, t_{i j 1}\right)$ and $\left(t_{i j 2}, m_{k}\right)$ are added to simulate the start and end of the operation processing on $m_{k}$ respectively.

Let $P_{W}$ denote the set of all arcs related with workstation and machine places. Then, the activities of all jobs among workstations can be modeled by the following Petri net, called as PN for scheduling (PNS).

$$
\left(N, M_{0}\right)=\left(P_{O} \cup P_{S} \cup P_{E} \cup P_{W} \cup P_{M}, T, F, M_{0}\right)
$$

where $P_{O}=\cup_{q \in Q} P_{O q}, P_{S}=\left\{p_{q s} \mid q \in Q\right\}, P_{E}=\left\{p_{q e} \mid q\right.$ $\in Q\}, T=\cup_{q \in Q} T_{q}, F=F_{Q} \cup F_{W}$, and $F_{Q}=\cup_{q \in Q} F_{q}$. The initial marking $M_{0}$ is defined as $M_{0}\left(p_{q s}\right)=\varphi(q), \forall p_{q s} \in P_{S}$, $M_{0}(p)=0, \forall p \in P_{O} \cup P_{E}$, and $M_{0}(w)=C(w), \forall w \in P_{W}$.

Let us use the following example to illustrate the modeling method.

Example 1: Consider an FJS with five workstations $w_{1}-w_{5}$. The buffer capacities of workstations are $1,1,1$, 2 , and 2 , respectively, i.e., $C\left(w_{1}\right)=C\left(w_{2}\right)=C\left(w_{3}\right)=1$ and $C\left(w_{4}\right)=C\left(w_{5}\right)=2$. The system can process two job types, types- $A$ and $B$, with 3 and 2 jobs to be processed, respectively, i.e., $\varphi(A)=3$ and $\varphi(B)=2$. Type$A$ jobs can be processed through $w_{1} w_{2} w_{3}$ or $w_{1} w_{4} w_{5} w_{3}$, while type- $B$ jobs through $w_{3} w_{5} w_{1}$. Then the PN model of jobs through workstations is shown in Figure 1, where three processing routes $\pi_{1}, \pi_{2}$, and $\pi_{3}$ are modeled by O-paths $\mathrm{O}\left(\pi_{1}\right)=p_{A s} t_{11} p_{111} t_{111} p_{112} t_{112} p_{113} t_{12} p_{121} t_{121} p_{122}$ $t_{122} p_{123} t_{13} p_{131} t_{131} p_{132} t_{132} p_{133} t_{14} p_{A e}, \mathrm{O}\left(\pi_{2}\right)=p_{A s} t_{11} p_{111}$ $t_{111} p_{112} t_{112} p_{113} t_{22} p_{221} t_{221} p_{222} t_{222} p_{223} t_{23} p_{231} t_{231} p_{232} t_{232}$ $p_{233} t_{24} p_{131} t_{131} p_{132} t_{132} p_{133} t_{14} p_{A e}$, and $\mathrm{O}\left(\pi_{3}\right)=p_{B s}$ $t_{31} p_{311} t_{311} p_{312} t_{312} p_{313} t_{32} p_{321} t_{321} p_{322} t_{322} p_{323} t_{33} p_{331} t_{331} p_{332}$ $t_{332} p_{333} t_{34} p_{B e}$, respectively.

When all the jobs have been processed, the system reaches the final state where no job is in the system and all resources are available or idle, or $\left(N, M_{0}\right)$ reaches the final marking $M_{f}$, where $M_{f}(p)=0, \forall p \in P_{O} \cup P_{S} ; M_{f}(p)=M_{0}(p), \forall p \in$ $P_{W} \cup P_{M} ; M_{f}\left(p_{q e}\right)=M_{0}\left(p_{q s}\right), \forall p_{q e} \in P_{E}$.

Let $\alpha$ be a sequence of transitions of $\left(N, M_{0}\right)$. If $\alpha$ can lead $\left(N, M_{0}\right)$ from $M_{0}$ to $M_{f}$, i.e., $M_{0}\left[\alpha>M_{f}\right.$, it is called to be feasible. Under the assumption that all transitions on $\alpha$ are fired as early as possible, $\alpha$ is a (feasible) schedule of the system, and in this case, the firing time of the last transition in $\alpha$ is the makespan of schedule $\alpha$. The scheduling problem considered

![img-0.jpeg](img-0.jpeg)

FIGURE 1. The PNS model of an FJS.
in this article is to find one with minimum makespan among all feasible sequences.

## III. PROPOSED ALGORITHM

Papadimitriou and Kanellakis have proved in [6] that the two machines FSSP with limited buffers, as a particular case of our problem, is strongly NP-hard. So when the problem size increases, it becomes impractical to obtain the optimum solution of the considered scheduling problem within a reasonable time. Thus intelligent optimization methods [35] are widely used. In this article, we introduce a new HEDA to solve our scheduling problem. The proposed HEDA is the combination of basic EDA, local search, and DAPs. Its main components are as follows.

- Representation and amending of individuals;
- Fitness function;
- Initialization;
- Probabilistic model and generating new individuals;
- Local search.

In the rest part of the paper, we use $J=\left(J_{1}, J_{2}, \ldots, J_{n}\right)$ to denote a permutation with a given order of all jobs, and suppose that there are a total of $K$ job processing routes. Then $\pi=\left(\pi_{1}, \pi_{2}, \ldots, \pi_{K}\right)$ is used to denote a route permutation with a fixed order. For example, in Example 1, there are five jobs to be processed through three routes $\pi_{1}-\pi_{3}$, three type$A$ jobs, denoted as $J_{1}-J_{3}$, and two type- $B$ jobs, $J_{4}$ and $J_{5}$.

Then $J=\left(J_{1}, J_{2}, J_{3}, J_{4}, J_{5}\right)$ and $\pi=\left(\pi_{1}, \pi_{2}, \pi_{3}\right)$ are given job and route permutations, respectively.

## A. REPRESENTATION AND AMENDING OF INDIVIDUALS

1) INDIVIDUAL REPRESENTATION

In our HEDA, a permutation with repetition of jobs is used to represent operation information of jobs and as a part of individual coding. On the other hand, a job may have different processing routes, and hence, the route information of jobs is also included in individual coding. Because the route of a job is unique within a workstation, in order to simplify the individual coding, the coding used in this article is only limited to the operation level or the corresponding workstation level, and the activities of jobs in workstations will be arranged according to the principle of first arrival and first processing. That is, an individual $I$ contains two parts: operation part $S_{o}$ and route part $S_{r}$, i.e., $I=\left(S_{o} ; S_{r}\right)$, where each type- $q$ job appears $\chi(q)$ times in $S_{o}$, and $S_{r}=\left(\sigma_{1}, \sigma_{2}, \ldots, \sigma_{n}\right)$ is an $n$-dimension vector and $\sigma_{k}$ is a processing route of job $J_{k}$ specified by $I$. Note that elements of $S_{r}$ and $J$ form one-to-one correspondence relation.

For a given individual $I=\left(S_{o} ; S_{r}\right)$, let the $i$-th appearance of type- $q$ job $J_{k}$ in $S_{o}$ represent the $i$-th operation of $J_{k}$ in route $\pi_{k}$, omitting redundant $J_{k}$ if the length of $\pi_{k}$ is less than $\chi(q)$, i.e., $\lambda\left(\pi_{k}\right)<\chi(q)$. In such a way, $S_{o}$ is translated into a sequence of operations, denoted as $\Delta\left(S_{o}\right)$. Then, according to the given route for each job in $S_{r}$, and matching each operation with its preparatory transition in $\left(N, M_{0}\right), \Delta\left(S_{o}\right)$ or $I$ is interpreted as a sequence of transitions in Petri net model, denoted as $\alpha^{\prime}(I)$. Thus, any individual can be decoded into a sequence of transitions in $\left(N, M_{0}\right)$.

For a given individual $I=\left(S_{o} ; S_{r}\right)$, although $\Delta\left(S_{o}\right)$ contains all operations of jobs to be processed, $\alpha^{\prime}(I)$ is not a complete sequence of firing transitions from $M_{0}$ to $M_{I}$. In $\alpha^{\prime}(I)$, there is a lack of transitions that represent the activities of jobs in workstations, as well as the last transition of the processing route to each job.

Note that the activity sequence or route of jobs in each workstation is uniquely determined, taking the form of $t_{i j} p_{i j 1} t_{i j 1} p_{i j 2} t_{i j 2} p_{i j 3}$, and as long as a job enters a workstation, its corresponding operation can always be completed, that is, jobs in $p_{i j 1}$ and $p_{i j 2}$ always reach $p_{i j 3}$ as time goes on. This kind of token transfer only takes up the processing time of the machine, and has no effect on the liveness of the system. Therefore, it can be considered that the token generated by $t_{i j}$-firing directly reaches $p_{i j 3}$, and for simplicity, transitions $t_{i j 1}$ and $t_{i j 2}$ are omitted in the transition sequence of coding $\alpha^{\prime}(I)$.

On the other hand, the processing order of jobs in the same workstation can be arranged in many ways, such as in first come first processing, or the same type of jobs can be put together for continuous processing as much as possible if the set-up time of machines is considered. Therefore, in order to reduce the encoding length, this article does not code the activity order of jobs in the workstations, but leaves it in

the simulation algorithm, and the principle of "first come first process" is adopted in the simulation of the proposed algorithm.

Therefore, in order to make $\alpha^{\prime}(I)$ complete, we only need to add the last transition of the processing route of each job to the back of $\alpha^{\prime}(I)$, and denote the resulting transition sequence as $\alpha(I)$.

Example 2: Consider the FJS in Example 1. Its PNS model is shown in Figure 1. There are five jobs to be processed: three type- $A$ jobs, denoted as $J_{1}-J_{3}$, and two type- $B$ jobs, denoted as $J_{4}$ and $J_{5}$. Type- $A$ jobs have two processing routes $\pi_{1}$ and $\pi_{2}$, while type- $B$ jobs have only one route $\pi_{3}$. Then, $S_{r 1}=\left(\pi_{2}, \pi_{2}, \pi_{1}, \pi_{3}, \pi_{3}\right)$ is the route part of an individual, where the routes of $J_{1}, J_{2}, J_{3}, J_{4}$, and $J_{5}$ are set to $\pi_{2}, \pi_{2}$, $\pi_{1}, \pi_{3}$, and $\pi_{3}$, respectively. Since $\lambda\left(\pi_{1}\right)=3, \lambda\left(\pi_{2}\right)=4$, $\lambda\left(\pi_{3}\right)=3$, we know that $\chi(A)=\max \left\{\lambda\left(\pi_{1}\right), \lambda\left(\pi_{2}\right)\right\}=4$, and $\chi(B)=\lambda\left(\pi_{3}\right)=3$. Then the numbers of type- $A$ and $B$ jobs that are contained in the operation section of an individual should be 4 and 3 , respectively. For example, $S_{o 1}=\left(J_{2}, J_{2}\right.$, $\left.J_{2}, J_{1}, J_{4}, J_{1}, J_{1}, J_{3}, J_{3}, J_{4}, J_{5}, J_{1}, J_{5}, J_{4}, J_{2}, J_{3}, J_{5}, J_{3}\right)$ can be regarded as the operation part of an individual. Then, $I_{1}=\left(S_{o 1} ; S_{r 1}\right)=\left(J_{2}, J_{2}, J_{2}, J_{1}, J_{4}, J_{1}, J_{1}, J_{3}, J_{3}\right.$, $\left.J_{4}, J_{5}, J_{1}, J_{5}, J_{4}, J_{2}, J_{3}, J_{5}, J_{3} ; \pi_{2}, \pi_{2}, \pi_{1}, \pi_{3}, \pi_{3}\right)$ represents an individual. According to the given route in $S_{r}$, we can obtain the sequence of operations corresponding to $S_{o 1}$, $\Delta\left(S_{o 1}\right)=\left(o_{21}, o_{22}, o_{23}, o_{11}, o_{41}, o_{12}, o_{13}, o_{31}, o_{32}, o_{42}, o_{51}\right.$, $\left.o_{14}, o_{52}, o_{43}, o_{24}, o_{33}, o_{53}\right)$, where $o_{k i}$ is the $i$-th operation of job $J_{k}$. Then by matching an operation with its preparatory transition, we have the sequence of transitions corresponding to $I_{1}, \alpha^{\prime}\left(I_{1}\right)=\left(t_{11}, t_{22}, t_{23}, t_{11}, t_{31}, t_{22}, t_{23}, t_{11}, t_{12}, t_{32}, t_{31}\right.$, $\left.t_{24}, t_{32}, t_{33}, t_{24}, t_{13}, t_{33}\right)$, where commas are added just for clarity.

Note that $\chi(A)=4$, and each of $J_{1}, J_{2}$, and $J_{3}$ appears 4 times in $S_{o 1}$. The route for $J_{3}$ specified in $S_{r 1}$ is $\pi_{1}$ and has 3 operations, and hence, the 4 -th $J_{3}$ in $S_{o 1}$ is redundant in converting $S_{o 1}$ to $\Delta\left(S_{o 1}\right)$. On the other hand, the second operation of $J_{3}, o_{32}$, is processed in $w_{2}$, and its preparatory transition is $t_{12}$, that is we have $t_{12}\left[o_{32}\right]$; while the routes for $J_{1}$ and $J_{2}$ given by $S_{r 1}$ are $\pi_{2}$. Then their second operations $o_{12}$ and $o_{22}$ are processed in $w_{4}$, and hence their preparatory transitions are $t_{22}$, and $t_{22}\left[o_{12}\right]$ and $t_{22}\left[o_{22}\right]$ is hold. Then the complete transition sequence for individual $I_{1}$ is $\alpha\left(I_{1}\right)=$ $\left(t_{11}, t_{22}, t_{23}, t_{11}, t_{31}, t_{22}, t_{23}, t_{11}, t_{12}, t_{32}, t_{31}, t_{24}, t_{32}, t_{33}, t_{24}\right.$, $\left.t_{13}, t_{33}, t_{14}, t_{14}, t_{14}, t_{34}, t_{34}\right)$.

## 2) AMENDING

According to the above encoding and decoding method, individual $I$ corresponds to the unique transition sequence $\alpha(I)$. Although $\alpha(I)$ includes the number of transitions required from $M_{0}$ to $M_{f}$, but $\alpha(I)$ itself may not be feasible. It may not be fired in order, and/or cause deadlock. Thus, the modification of such $I$ or $\alpha(I)$ is necessary. For example, consider individual $I_{1}$ and its corresponding transition sequence $\alpha\left(I_{1}\right)$ in Example 2. Let $\alpha\left(I_{1}\right)=\sigma_{1} \sigma_{2}$ where $\sigma_{1}=$ $t_{11} t_{22} t_{23} t_{11} t_{31} t_{22} t_{23} t_{11} t_{12}$, and $M_{0}\left[\sigma_{1}>M_{1}\right.$. Then $M_{1} \neq$ $M_{f}$, and under $M_{1}$, all transitions are dead. Thus $\alpha\left(I_{1}\right)$ is
not feasible. Thus, the feasibility of each individual should be checked and the infeasible individuals are translated into feasible ones. In this article, the detection and amending algorithm (Algorithm DA) proposed in [25] is embedded in a decoding process to obtain the feasible sequence of firing transitions from $M_{0}$ to $M_{f}$. The reader can refer to [25] for more details.

## B. FITNESS FUNCTION

The fitness function could be used to guide the EDA. In this article, it is the makespan, i.e., the completion time of the last job.

For an individual and its complete and feasible sequence of transitions $\alpha(I)=t_{0} t_{1} t_{2} \ldots t_{L-1}$, let $M_{k}\left[t_{k}>M_{k+1}\right.$, $k=0,1, \ldots, L-1$, and $\left.f\left(t_{k} \mid o_{i j}\right]\right)$ denote the firing time of $t_{k}$, i.e., when job $J_{i}$ enters workstation $w\left(o_{i j}\right)$. Since there is only one machine that can process jobs in $w\left(o_{i j}\right)$, job $J_{i}$ cannot be processed immediately after transition $t_{k}$ fires when the machine is busy.

Let $s\left(o_{i j}\right)$ denote the start time of operation $o_{i j}$, the $j$-th operation of $J_{i}$, that is, for example, the firing time of transitions $t_{111}$ or $t_{331}$ in Figure 1. Then, $f\left(t_{k} \mid o_{i j}\right]) \leq s(o i j)$, and $s\left(o_{i j}\right)=f\left(t_{k} \mid o_{i j}\right]$ ) only if the machine is idle when job $J_{i}$ enters workstation $w\left(o_{i j}\right)$.

For $J_{i}, t_{k}\left[o_{i j}\right]$ can be fired only after operation $o_{i(j-1)}$ is finished. Hence, $f\left(t_{k}\left[o_{i j}\right]\right) \geq s\left(o_{i(j-1)}\right)+d\left(o_{i(j-1)}\right)$. On the other hand, the transitions in $\alpha(I)$ are sequentially fired, and the firing time of $t_{k}\left[o_{i j}\right]$ should be after the firing of $t_{k-1}$, i.e., $f\left(t_{k}\left[o_{i j}\right]\right) \geq f\left(t_{k-1}\right)$. Then, we have

$$
f\left(t_{k}\left[o_{i j}\right]\right)=\max \left\{s\left(o_{i(j-1)}\right)+d\left(o_{i(j-1)}\right), f\left(t_{k-1}\right)\right\}
$$

If there are no other jobs in workstation $w\left(o_{i j}\right)$ when job $J_{i}$ enters it for its operation $o_{i j}$, job $J_{i}$ can start its operation $o_{i j}$, i.e., the start time of $o_{i j}$ is

$$
s\left(o_{i j}\right)=f\left(t_{k}\left[o_{i j}\right]\right)
$$

If there exist other jobs in $w\left(o_{i j}\right)$ that arrive earlier than job $J_{i}$, then the start time of $o_{i j}$ is not earlier than the completion time of any of their operations that have already been started at $f\left(t_{k}\left[o_{i j}\right]\right)$ or before. That is, the start time of $o_{i j}$ is

$$
\begin{aligned}
s\left(o_{i j}\right) & =\max \left\{s\left(o_{m n}\right)+d\left(o_{m n}\right), f\left(t_{k}\left[o_{i j}\right]\right) \mid w\left(o_{m n}\right)\right. \\
& =w\left(o_{i j}\right) \text { and } f\left(t_{l}\left[o_{m n}\right]\right) \leq f\left(t_{k}\left[o_{i j}\right]\right)\right\}
\end{aligned}
$$

By (1)-(3), the firing time of every transition and the start time of every operation can be computed recursively. The fitness function of individual $I$ is obtained

$$
f(I)=f\left(t_{L-1}\right)
$$

## C. INITIALIZATION

The initial population can be randomly generated. For generating an individual $I=\left(S_{o} ; S_{r}\right)$, first randomly create a permutation with repetition of jobs in which each type- $q$ job appears $\chi(q)$ times, and then, randomly select a route for each job from its route set. Through Algorithm DA, the infeasible

individuals are amended into feasible ones. Let $\Omega$ denote the current population of feasible individuals.

Decoding each individual in $\Omega$ and calculating their fitness values. Sort all individuals in $\Omega$ according to the ascending order of their fitness values, and select the best $\rho \times|\Omega|(\rho \in$ $(0,1])$ individuals as the elite set, denoted as $\Omega_{e}$. In the simulation of this example, the $\rho$ value is obtained by using an experimental optimization approach, and $\rho=0.3$.

## D. PROBABILISTIC MODEL AND GENERATING NEW INDIVIDUALS

The probabilistic model represents a main issue for EDA and its performance is closely related to it [32]. The best choice of a model is crucial. On the other hand, the efficiencies of model constructing and information sampling are closely related to the performance of the algorithm. Hence, the choice of the probabilistic model plays an important role in EDA's success.

In this article, the probability model is designed as a dominance matrix. It is based on the global statistic information from the elite set. Since an individual contains two parts: operation and route, two kinds of probability sub-models are constructed, i.e., the operation probability model $\Pi$, and the route probability model $\Xi$. They are used together to construct a new individual. Such two probability models are first constructed as follows.

Let $\Pi_{1}=\left(a_{i j}\right)$ be an $n \times L$ matrix where $n$ is the number of jobs to be processed and $L$ is the length of $S_{o}$. Let $\gamma_{i j}$ denote the number of individuals in $\Omega_{e}$, in which job $J_{i}$ is at position $j$ of their operation parts, and $a_{i j}=\gamma_{i j} /\left|\Omega_{e}\right|$.

In $\Pi_{1}=\left(a_{i j}\right)$ defined above, each individual in $\Omega_{e}$ is treated equally. In order to distinguish their importance, in this article, we set a weight for each individual according to their fitness values.

Let $I_{w}$ and $I_{b}$ be the worst and best individuals in current elite set $\Omega_{e}$. The weight of individual $I \in \Omega_{e}$ is defined as $g(I)=\left(f\left(I_{w}\right)-f(I)+1\right) / f\left(I_{b}\right)$. It is obvious that individuals with smaller fitness values or makespans are given larger weights. With this weight function $g(I)$ and $\Pi_{1}=\left(a_{i j}\right)$ defined above, we can design our operation probability matrix $\Pi$ and route probability matrix $\Xi . \Pi$ has the same dimension as $\Pi_{1}$ and can be obtained by modifying $\Pi_{1}$, and $\Xi$ is an $n \times K$ matrix, where $K$ is the total number of all different processing routes for all jobs.

The detailed algorithm for constructing probability Models $\Pi$ and $\Xi$ is given in algorithm CPM.

In the above Algorithm CPM, the operation probability matrix $\Pi$ and route probability matrix $\Xi$ are determined by the voting method of elite individuals in $\Omega_{e}$. Although each elite individual in $\Omega_{e}$ participates in voting, the better the individual is, the greater the contribution to $\Pi$ and $\Xi$.

With probability models $\Pi$ and $\Xi$, we can construct new individuals. Two methods for constructing new individuals are proposed in this article. In them, element $a_{i j}$ in $\Pi$ is considered as the probability of selection of job $J_{i}$ in the $j$-th position. In the first one, we first extend $n \times L$ matrix $\Pi$

```
Algorithm CPM //Constructing Probabilistic Models
Input: \(\Omega_{e}\);
Output: \(\Pi\) and \(\Xi\); Begin
    1: At the beginning, set \(\Pi \equiv\left(a_{i j}\right)_{n \times L}=\mathbf{0} ; B \equiv\left(b_{i j}\right)_{n \times L}=
    \(\mathbf{0} ; \Xi \equiv\left(c_{i k}\right)_{n \times K}=\mathbf{0} ; D \equiv\left(d_{i k}\right)_{n \times K}=\mathbf{0}\);
    2: for \((i=1 ; i \leq n ; i++)\{/ / J=\left(J_{1}, J_{2}, \ldots, J_{n}\right)\) is given.
    3: for (each \(I \in \Omega_{e}\) ) \(\} / / I=\left(S_{o}, S_{r}\right)\) where \(S_{o}=\) $\left(p_{0}, \ldots, p_{L-1}\right)$ and \(\left.S_{r}=\left(\sigma_{1}, \sigma_{2}, \ldots, \sigma_{n}\right)\right.\)
    \(4: g(I)=\left[f\left(I_{w}\right)-f(I)+1\right] /\left(I_{b}\right)\)
    5: for \((l=1 ; l \leq L ; l++)\{ ;\)
    \(6: \quad\) if \(\left(p_{l}=J_{l}\right)\left\{a_{i l}:=a_{i l}+1 ; b_{i l}:=b_{i l}+g(I) ;\right\}\)
    7: \(\}\) end for \((I)\);
    8: for \((k=1 ; k \leq K ; k++)\{/ /\) for \(\pi_{j}\) and \(\pi=\) $\left(\pi_{1}, \pi_{2}, \ldots, \pi_{K}\right)$ is given;
    \(9: \quad\) if \(\left(\sigma_{i}=\pi_{k}\right)\left\{c_{i k}:=c_{i k}+1 ; d_{i k}:=d_{i k}+g(I) ;\right\}\)
    10: \(\}\) end for \((k)\)
    11: \(\}\) end for (each \(I\) )
    12: \(\}\) end for \((i)\)
    13:for \((j=1 ; j \leq L ; j++)\{\)
    14: \(\Pi_{j}:=\Pi_{j} /\left|\Omega_{e}\right| ; / / \Pi\) normalization; \(\Pi_{j}\) is the \(j\)-th
    column of \(\Pi\).
    15: Let \(b_{j}=\sum_{i} b_{i j} ; B_{j}:=B_{j} / b_{j} ; / / B_{j}\) is the \(j\)-th column
    of \(B\).
    16: \(\Pi:=(\Pi+B) / 2 ; / / \Pi\) operation probability matrix.
    17: \(\}\) end for \((j)\)
    18: for \((i=1 ; i \leq n ; i++)\{\)
    19: Let \(c_{i}=\sum_{j} c_{i j} ; \Xi_{i}:=\Xi_{i} / c_{i} ; / / \Xi\) normalization; \(\Xi_{i}\)
    is the \(i\)-th row of \(\Xi\).
    20: Let \(d_{i}=\sum_{j} d_{i j} ; D_{i}:=D_{i} / d_{i} ; / / D\) normalization; \(D_{i}\)
    is the \(i\)-th row of \(D\).
    21: \(\Xi:=(\Xi+D) / 2 ; / / \Xi\) route probability matrix.
    22: \}end for \((i)\)
    23:Output \(\Pi\) and \(\Xi\);
End
```

to $L \times L$ matrix $\Pi_{e x t}$ so that a row of $\Pi$ corresponding to job $J_{i}$ is $\chi\left(J_{i}\right)$ rows of $\Pi_{e x t}$ in succession. Then, according to the descending order of elements in $\Pi_{e x t}$ and for maximum element $a_{i j}$, set job $i$ to position $j$ in the sequence of a new individual, and then set all elements on the row and column in which $a_{i j}$ is into -1 . Repeat until all the elements of $\Pi_{e x t}$ are -1 .

In the second method, selecting job for each position and a route for a job in the new individual is done by roulette based on $\Pi$ and $\Xi$. The details of algorithms called CNI1 and CNI2 where CN represents Constructing New-individuals are as follows.

## E. LOCAL SEARCH

To balance the global and local searches and to further improve the performance, a simplified simulated annealing (SSA) algorithm is employed as the local search. Note that simulated annealing has been successfully combined with other intelligent optimization methods. SSA is acted on new

Algorithm CNI1 // Constructing a New Individual $I=$ $\left(S_{o} ; S_{r}\right)$ Through $\Pi$ and $\Xi$
Input: $\Pi$ and $\Xi$;
Output: $I=\left(S_{o} ; S_{r}\right)$; Begin
1: Let $S_{o}$ and $S_{r}$ be $1 \times L$ and $1 \times n$ empty arrays;
2: Let $\Pi_{\text {ext }}$ be the extended matrix of $\Pi$; Let $\Xi_{1}=\Xi$;
3: for (count $=0$; count $<L$; count $++$ )\{ // Constructing $S_{o}$ through $\Pi_{\text {ext }}$.
4: 1.1) Find an element $e_{n j}$ with the maximum value in $\Pi_{\text {ext }} ; / /$ (select the first one if there is more than one such element);
5: 1.2) If the row, in which $e_{n j}$ is located, corresponds to job $J_{i}$, add job $J_{i}$ at position $j$ in $S_{o}$;
6: 1.3) Set all elements in row $u$ and column $j$ of $\Pi_{\text {ext }}$ as $-1 ;$
7: $\}$ end for $/ / S_{o}$ is constructed;
8: for (count $=0$; count $<n$; count $++$ ) $\{/ /$ Constructing route $S_{r}$ for $S_{o}$ through $\Xi$
9: 2.1) find an element $c_{i j}$ with the maximum value in $\Xi$; 10: 2.2) add route $\pi_{j}$ at position $i$ in $S_{r}$, that is, set $\pi_{j}$ as the route of job $J_{i}$ in $S_{r}$;
11: 2.3) Set all elements in row $i$ of $\Xi$ as -1 ;
12:|end for // $S_{r}$ is constructed;
Output: $I=D A\left(S_{o} ; S_{r}\right)$; // A new feasible individual $I$ is constructed.
End
individual with a probability $p_{u}\left(p_{u} \in(0,1]\right)$. Its parameter temperature, Temp, is supposed to be constant. If individual $I$ is selected to execute local search, Temp $=f(I) /(U \times n)$ where $U$ is a constant. Its termination condition is that the maximum number of iterations, $i_{\max }$, is reached or $I$ has been improved for $x$ times. In the simulation, we set $i_{\max }=30$ and $x=3$. A new individual is produced by the so-called Neighbor Search (NS), in which three operations, job-insert, job-swap, and route-change, are executed sequentially. These three operations are defined as follows.

Job-insert: Randomly choose two different jobs from the operation part $S_{o}$ of $I$, and then insert the back one before the front one.

Job-swap: Randomly select two different jobs $J_{u}$ and $J_{v}$ from the operation part $S_{o}$ of $I$, and then swap them.

Route-change: Randomly select a job with multiple routes, and then change its current route in route part $S_{r}$ of $I$ to any one of its other routes.

Algorithm SSA is shown as follows.

## F. PROPOSED HYBRID ESTIMATION OF DISTRIBUTION ALGORITHM

With the above design, we can propose the HEDA procedure for solving flexible job shop manufacturing environment with limited capacity buffers as follows. It contains two main parts in every generation. At global exploration, a probability model is built with the elite individuals of an entire population

Algorithm CNI2 // Constructing a New Individuals Through $\Pi$ and $\Xi$
// constructing $S_{o}$ through $\Pi \equiv\left(a_{i j}\right)$;
1: Let $S_{o}$ and $S_{r}$ be $1 \times L$ and $1 \times n$ empty arrays;
2: Let $\Pi_{1}=\Pi$; Let $\Xi_{1}=\Xi$;
3: Let $\mathrm{A}[n]=(0,0, \ldots, 0) ; / / \mathrm{A}[j]$ is the number of $J_{j}$ appearing in $S_{o}$;
4: for $(i=0 ; i<L ; i++)\{$
5: $\mu=\operatorname{rand}(0,1)$;
6: for $(j=1 ; j \leq n ; j++)\{$
7: if $\left(\mu \leq \sum_{k=1, \ldots, j} a_{i k} \& \& \mathrm{~A}[j]<\chi\left(J_{j}\right)\right)\{ / /$ Select a job for position $i$ by Roulette;
8: add job $J_{j}$ at position $i$ in $S_{o} ; \mathrm{A}[j] \leftarrow \mathrm{A}[j]+1$; break; 9: \}
10: $\}$ end for $(j)$
11: $\}$ end for $(i)$
// Constructing route $S_{r}$ for $S_{o}$ through $\Xi$.
12:for $(i=0 ; i<n ; i++)\{$
13: $\mu=\operatorname{rand}(0,1) ; / /$ generating a random number.
14: for $(j=0 ; j<K ; j++)\{$
15: if $\left(\mu \leq \sum_{s=1, \ldots, j} c_{i s}\right)\{/ /$ Select a route for job $i$ by Roulette.
16: add route $\pi_{j}$ at position $i$ in $S_{r}$, i.e., set $\pi_{j}$ as the route of job $J_{i}$ in $S_{r}$; break; $\}$
17: $\}$ end for $(j)$
18: $\}$ end for $(i) / / S_{r}$ is constructed;
19:Output $I=D A\left(S_{o} ; S_{r}\right)$; //A new feasible individual $I$ is constructed.
End
to generate new individuals. At local search, the newly generated individuals adopt in probability $p_{u}$ multiple local search operators based on the problem characteristics for further exploitation. The algorithm stops when the maximum number of generations $G_{\max }$ is reached.

If $p_{u}$ is set to 0 , the local search SSA is not called in every generation, and the algorithm is simplified into so-called basic EDA.

## IV. EXPERIMENTAL RESULTS AND ANALYSIS

FJS with limited buffers is a new scheduling problem that is first attempted to be studied in this article. In current literature, there are no any algorithms and benchmarks to be developed for it. As a result, except for the algorithms proposed in this article, it is unrealistic to carry out a wider comparison. In this section, the proposed HEDA is tested by a simple FJS with limited buffers, which consists of nine workstations $w_{1}-w_{9}$. Each of $w_{2}, w_{3}, w_{4}, w_{6}$, and $w_{7}$ has a buffer with capacity 2 while $w_{1}, w_{5}, w_{8}$ and $w_{9}$ each have a buffer with capacity 1 . The considered FJS can process three types of jobs, types- $q_{1}, q_{2}$, and $q_{3}$. Its PN model is shown in Figure 2. There are $\varphi\left(q_{i}\right)=n_{i}, i \in Z_{3}$, type- $q_{i}$ jobs to be processed, and $n=n_{1}+n_{2}+n_{3} . \mathrm{O}\left(\pi_{1}\right)=p_{1 s}$ $t_{11} p_{111} t_{111} p_{112} t_{112} p_{113} t_{12} p_{121} t_{121} p_{122} t_{122} p_{123} t_{13} p_{131} t_{131} p_{132}$ $t_{132} p_{133} t_{14} p_{141} t_{141} p_{142} t_{142} p_{143} t_{15} p_{151} t_{151} p_{152} t_{152} p_{153} t_{16} p_{1 e}$,

## Algorithm SSA( $I$ )

Input: $I, I_{0} / / I$ and $I_{0}$ are individuals and $I_{0}$ is the best one in the current population $\Omega$;
Output: Ind ${ }_{0}$; Begin
$1: \operatorname{Ind}_{0} \leftarrow I ; \operatorname{Ind}_{1} \leftarrow I$
2:Temp $=f(I) /(U \times n) ; u=v=0$;
3: While (the termination condition is not satisfied) $\{$
4: $\operatorname{Ind}_{1} \leftarrow N S\left(\operatorname{Ind}_{1}\right), \operatorname{Ind}_{1} \leftarrow D A\left(\operatorname{Ind}_{1}\right)$;
5: If $\left(f\left(\operatorname{Ind}_{1}\right)<f\left(\operatorname{Ind}_{0}\right)\right)\{$
6: $\operatorname{Ind}_{0} \leftarrow \operatorname{Ind}_{1} ; v \leftarrow v+1$;
7: $\}$ Else $\{$
8: If $\left((\operatorname{rand}(0,1) \leq \exp \left(-\left(f\left(\operatorname{Ind}_{1}\right)-\left(f\left(\operatorname{Ind}_{0}\right)\right) / \operatorname{Temp}\right)\right\}\right.$
9: $\operatorname{Ind}_{0} \leftarrow \operatorname{Ind}_{1} ; / /$ accept worse individual;
10: $\}$ Else $\{$
11: $\operatorname{Ind}_{2} \leftarrow N S\left(I_{0}\right), \operatorname{Ind}_{2} \leftarrow D A\left(\operatorname{Ind}_{2}\right)$;
12: If $\left(f\left(\operatorname{Ind}_{2}\right)<f\left(\operatorname{Ind}_{0}\right)\right)\left\{\operatorname{Ind}_{0} \leftarrow \operatorname{Ind}_{2}\right\}\}$
13: $\} / /$ end Else
14: $\operatorname{Ind}_{1} \leftarrow \operatorname{Ind}_{0}$
15: $u \leftarrow u+1 ; / /$ end Else
16: $\}$ end while
17:Return $D A\left(\operatorname{Ind}_{0}\right)$; // Return an feasible individual. End
![img-1.jpeg](img-1.jpeg)

FIGURE 2. PNS of the FIS.
and $\mathrm{O}\left(\pi_{4}\right)=p_{4 s} t_{41} p_{411} t_{411} p_{412} t_{412} p_{413} t_{42} p_{421} t_{421} p_{422} t_{422}$ $p_{423} t_{43} p_{431} t_{431} p_{432} t_{432} p_{433} t_{44} p_{441} t_{441} p_{442} t_{442} p_{443} t_{45} p_{451} t_{451}$ $p_{452} t_{452} p_{453} t_{46} p_{4 e}$, respectively. Type- $q_{2}$ jobs have two

## Algorithm HEDA

1:Initial parameters $G_{\text {max }}, N_{\text {pop }}, N_{\text {esc }}, N_{\text {New }}$, and $p_{\alpha}$; 2:Randomly generate initial population $\Omega$;
3: Sorting $\Omega / /$ according to in ascending order of individual fitness values, and denote $\Omega$ as $\Omega=\left\{I_{0}, I_{1}, \ldots, I_{N_{\text {pop }}}\right\}$;
4: select $\Omega_{e}=\left\{I_{0}, I_{1}, \ldots, I_{N e s c-1}\right\} ; / / I_{0}$ is the best individual in $\Omega$;
5: For $(g=0 ; g<G_{\max } ; g++)\{$
6: $\operatorname{Let}(\Pi, \Xi)=\operatorname{CPM}\left(\Omega_{e}\right) ; / /$ establish $\Pi$ and $\Xi$ from $\Omega_{e}$.
7: $\operatorname{Ind}_{0}=\operatorname{CNI1}(\Pi, \Xi)$;
8: $\operatorname{For}(i=1 ; i<N_{\text {new }} ; i++)\{$
9: $\quad \operatorname{Ind}_{i}=\operatorname{CNI} 2(\Pi, \Xi)$
10: If $\left(\operatorname{rand}(0,1)<p_{\alpha}\right)\{$
11: $\quad \operatorname{Ind}_{i}=\operatorname{SSA}\left(\operatorname{Ind}_{i}\right)$; \}
12: $\quad$ Add $\operatorname{Ind}_{i}$ to $\Omega_{1}$;
13: $\} / /$ end $\operatorname{For}(i)$
14: Sorting $\Omega \cup \Omega_{1}$; select the first $N_{\text {esc }}$ best individuals as $\Omega_{e}, \Omega_{e}=\left\{I_{0}, I_{1}, \ldots, I_{N e s c-1}\right\} ; / /$ the best individual is denoted as $I_{0}$.
15: $\}$ end $\operatorname{For}(g)$
16:output $I_{0}$;
End
TABLE 1. Job numbers in different instances.


processing routes, $\mathrm{O}\left(\pi_{2}\right)=p_{2 s} t_{21} p_{211} t_{211} p_{212} t_{212} p_{213} t_{22} p_{221}$ $t_{221} p_{222} t_{222} p_{223} t_{23} p_{233} t_{231} p_{232} t_{232} p_{233} t_{24} p_{241} t_{241} p_{242} t_{242} p_{243}$ $t_{25} p_{251} t_{251} p_{252} t_{252} p_{253} t_{26} p_{2 e}$ or $\mathrm{O}\left(\pi_{3}\right)=p_{2 s} t_{21} p_{211} t_{211} p_{212}$ $t_{212} p_{213} t_{32} p_{321} t_{321} p_{322} t_{322} p_{323} t_{33} p_{331} t_{331} p_{332} t_{332} p_{333} t_{34} p_{341}$ $t_{341} p_{342} t_{342} p_{343} t_{35} p_{251} t_{251} p_{252} t_{252} p_{253} t_{26} p_{2 e}$. Sixteen instances with different numbers of jobs, $\left(n_{1}, n_{2}, n_{3}\right)$, are designed to evaluate the performance of the proposed HEDA, and they are shown in Table 1. In these instances, we suppose that job processing time is randomly distributed in the range [4, 40], and the detailed values are shown in Table 2.

TABLE 2. Processing time for operations.


TABLE 3. Parameter values of different factor level.

## A. PARAMETER DETERMINATION

In the simulation calculation, the first two parameters of Algorithm HEDA, population size $|\Omega|$ and maximum number of generations $G_{\max }$, are set as $|\Omega|=100$ and $G_{\max }=50 \times n$, respectively. The other four parameters, the elite individual percentage $\rho$, the number of new individuals $N_{\text {new }}$, the probability of acting SSA on a new individual $p_{\alpha}$, and temperature constant $U$, will be determined by using the Taguchi method [36].

Parameter $\rho$ determines directly the size of the elite set that provides information for the probability model. If it is too large, some poor individuals are included and have bad effect on the probability model; while if it is too small, the population may mature too early. Parameter $N_{\text {new }}$ determines the size of the seed set. A small $N_{\text {new }}$ leads to obtain only a few good genes and has a too fast convergence speed while a large value implies that poor individuals could be involved in. Parameter $p_{\alpha}$ is the probability of local search conducted on new individuals, which balances the global search and the local search. Temperature Temp in SSA has influence on the probability accepting a worse solution. It is proportional to a constant $U$, i.e., Temp $=f(I) /(U \times n)$. The value domains these four parameters are set as $\rho \in\{0.1,0.3,0.5\}, N_{\text {new }} \in$ $\{10,20,30\}, p_{\alpha} \in\{0.02,0.04,0.08\}$, and $U \in\{14,16,18\}$, respectively. For each parameter, three factor levels are used and listed in Table 3, and hence, the orthogonal array $\mathrm{L}_{\theta}\left(3^{4}\right)$ is chosen. For each parameter combination of $\mathrm{L}_{\theta}\left(3^{4}\right)$, HEDA is run 10 times independently regarding instance In03. The makespan average in 10 run times is used as the response variables (RV). The orthogonal array and the values of response variables are listed in Table 4, and then the statistic results are summarized in Table 5.

TABLE 4. Orthogonal array $L_{\theta}\left(3^{4}\right)$ and response variable values.


TABLE 5. Statistic results.


![img-2.jpeg](img-2.jpeg)

FIGURE 5. The convergence tendency of EDA and HEDA with makespan on In03 and In08.

From Table 5, it can be seen that $p_{\alpha}$ has the most significant impact on HEDA performance. $N_{\text {new }}$ ranks the second, $U$ the third, and $\rho$ the last. According to their corresponding factor levels (the bold face), the suggested parameter set-up for HEDA are determined as $\rho=0.3, N_{\text {new }}=30, p_{\alpha}=0.04$, and $U=14$.

## B. EXPERIMENTAL RESULTS

In order to test the effectiveness of our proposed algorithms and explain the improvement effect of SSA on EDA, Algorithms EDA and HEDA are run 10 times independently on

TABLE 6. Comparison of simulation results and runtime of EDA and HEDA.

all 16 instances and their experimental results are compared. Their average and best (or minimum) makespan values are listed in Table 6, where BST denotes the best makespan among 10 trials, TIME/B denotes the runtime of a trial through which the best makespan is obtained, and AVG and TIME/A denote the average makespan and average runtime of 10 trials, respectively.

From Table 6, we know that two algorithms can give feasible solutions for each instance in a relatively short time. The shortest time is only a few seconds, and the longest average time is 2993.3 seconds of HEDA for In16. For each instance, the makespan results obtained by HEDA are superior to those obtained by the basic EDA. This shows that the embedding SSA has greatly improved the performance of EDA. The larger the scale of the problem, the greater the improvement. For example, the performance improvement for average makespans of In01, In08, In09, and In16 are $(124.5-109.2) / 124.5=12.3 \%, 20.8 \%, 22 \%$, and $20.3 \%$, respectively. Of course, these improvements are timeconsuming. Thus, it is better to run algorithm HEDA in order to obtain at the better schedules at the expense of more time.

The convergence tendency of EDA and HEDA of In03 and In08 with makespan is shown in Figure 3. It can be seen that EDA is easy to mature early, and converges faster than HEDA. It also shows that SSA plays a certain role in overcoming the early maturing phenomenon and HEDA owns better global searching ability. HEDA's makespan is improving globally and constantly, especially for In08 and hence, it is reasonable and necessary to increase the maximum iteration times as the scale of the problem increases, i.e., $G_{\max }=50 \times n$. For In08, an optimal or suboptimal schedule with makespan 491 is obtained by HEDA.

## V. CONCLUSION

In this article, the production scheduling problem of FJS with limited buffers is studied. Based on the place-timed Petri net model of the considered system, a novel hybrid estimation of distribution algorithm (HEDA) is proposed to minimize the makespan. A candidate solution is coded as an individual that consists of two sections. In the first section, a processing route is set for each job; and the second part is a possible sequence of operations. Under the monitoring of a deadlock controller, such an individual can be decoded as a feasible schedule. Corresponding to different sections of an individual, two probability models, route and operation probability models, are established via a voting procedure in which individual weighted differences are considered. Based on these models, an effective procedure for constructing offspring individuals is proposed. For each new individual, a simple local search, SSA, is performed with a certain probability in order to improve the performance of EDA. Simulation results show the effectiveness of the proposed method over EDA.

This work is of important practice significance for job-shop scheduling with limited buffers. Since no existing comparable results are available, more studies for establishing more effective methods are needed in the future. On the other hand, there are many evolutionary algorithms that may be used to solve the problem considered here. But for each different algorithm, as done in this article, we need to establish the corresponding encoding and decoding scheme, the relevant operators, and the parameter setting scheme, and how to improve the performance of the algorithm by embedding appropriate local searches. All these are worthy of further study.
