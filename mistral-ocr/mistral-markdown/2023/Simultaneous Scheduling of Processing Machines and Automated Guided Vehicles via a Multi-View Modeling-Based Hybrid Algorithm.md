# Simultaneous Scheduling of Processing Machines and Automated Guided Vehicles via a Multi-View Modeling-Based Hybrid Algorithm 

Bin Xin ${ }^{\odot}$, Member, IEEE, Sai Lu ${ }^{\odot}$, Qing Wang ${ }^{\odot}$, Fang Deng ${ }^{\odot}$, Senior Member, IEEE, Xiang Shi ${ }^{\odot}$, Jun Cheng ${ }^{\odot}$, Member, IEEE, and Yuhang Kang ${ }^{\odot}$


#### Abstract

The flexible job-shop co-scheduling problem (FJCSP) for processing machines and automated guided vehicles (AGVs) in a flexible manufacturing system (FMS) has attracted more attention with the aim of improving production efficiency. In FMS, AGVs in charge of transporting jobs realize the flexible linkage of operations between different processing machines. The added interdependence between transporting and processing tasks brings more difficulties than the traditional flexible job-shop scheduling problem (FJSP). In this paper, the mathematical model of FJCSP is formulated to minimize the makespan. Considering the feature similarity of FJCSP with FJSP and AGV-routing problem in different cases, a multi-view modelingbased hybrid algorithm consisting of an estimation of distribution algorithm (EDA) and an ant colony optimization (ACO) is proposed. In EDA, a probability model abstracts the information in superior solutions about the operation sequencing and the rule selection for scheduling machines and AGVs. In ACO, a jobpath pheromone model and an AGV-path pheromone model are designed to jointly select the job-machine-AGV combination with shorter processing time and transportation time. In the proposed hybrid algorithm, EDA and ACO generate solutions indepen-


Manuscript received 26 May 2023; accepted 23 July 2023. This article was recommended for publication by Associate Editor Z. Pei and Editor T. Nishi upon evaluation of the reviewers' comments. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1308000, in part by the National Outstanding Youth Talents Support Program under Grant 61822304, in part by the Basic Science Center Programs of NSFC under Grant 62088101, in part by the Beijing Advanced Innovation Center for Intelligent Robots and Systems, in part by the Shanghai Municipal Science and Technology Major Project under Grant 2021SHZDZX0100, in part by the Shanghai Municipal Commission of Science and Technology Project under Grant 19511132101, in part by the National Natural Science Fund of China under Grant 62003044, and in part by the National Science Fund for Distinguished Young Scholars of China under Grant 62025301. (Corresponding author: Bin Xin.)

Bin Xin, Sai Lu, Qing Wang, and Xiang Shi are with the National Key Laboratory of Autonomous Intelligent Unmanned Systems, School of Automation, Beijing Institute of Technology, Beijing 100081, China (e-mail: brucebin@bit.edu.cn; 292243532@qq.com; wangqing1020@bit. edu.cn; bit_shixiang@163.com).
Fang Deng is with the National Key Laboratory of Autonomous Intelligent Unmanned Systems, School of Automation, Beijing Institute of Technology, Beijing 100081, China, and also with the Beijing Institute of Technology Chongqing Innovation Center, Chongqing 401120, China (e-mail: dengfang@ bit.edu.cn).
Jun Cheng and Yuhang Kang are with the Key Laboratory of Human-Machine Intelligence-Synergy Systems, Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, Shenzhen 518055, China (e-mail: jun.cheng@siat.ac.cn; yh.kang1@siat.ac.cn).
This article has supplementary material provided by the authors and color versions of one or more figures available at https://doi.org/10.1109/TASE.2023.3301656.

Digital Object Identifier 10.1109/TASE.2023.3301656
dently and achieve cooperation by sharing elites. An adaptive parameter is designed to regulate the use of the two methods to adapt to the varying demands of multi-view modeling in different cases and search stages. Furthermore, a local search with a three-layer operator based on the critical path method is proposed to balance exploration and exploitation in solution space. Finally, computational experiments involving a case study verified the advantage of the multi-view modeling-based hybrid algorithm in comparison with the state-of-the-art approaches.

Note to Practitioners-This paper was motivated by the optimization problem of scheduling machines and automated guided vehicles (AGVs) in flexible manufacturing system (FMS). In FMS with AGVs, the transportation stages for jobs by AGVs significantly impact the overall production efficiency of the FMS and cannot be overlooked. This paper suggested a hybrid evolutionary algorithm using an estimation of distribution algorithm (EDA), an ant colony optimization (ACO) and a local search algorithm based on the critical path method. In the proposed hybrid algorithm, an adaptive parameter is introduced to regulate the utilization of EDA and ACO in generating a new population. This paper presents a mathematical characterization of the scheduling problem and subsequently outlines the step-bystep design of the hybrid algorithm. Computational experiments, including a case study, demonstrate that the hybrid algorithm exhibits adaptability to various instances and outperforms state-of-the-art approaches.

Index Terms-Simultaneous scheduling, Flexible manufacturing system, Automated guided vehicle, Modeling-based method, Multi-view.

## I. INTRODUCTION

WITH the continuous development of user needs and the flexibility of manufacturing, the manufacturing mode has gradually changed from the product-driven mode to the user-driven mode. In order to meet these demands, the flexible manufacturing system (FMS) has become an important development direction of the industry in the future because of its high automation, fast response speed and low-cost line change. The flexible job-shop scheduling problem (FJSP) is always a research hotspot that has been proven to be an NP-hard problem [1], [2]. With the development of production automation and information integration, modern industrial production puts forward higher requirements for logistics systems. As a kind of automatic equipment, automated guided vehicle (AGV) can complete specified transportation tasks in a given path or environment layout. AGVs accomplish the flexible

operation linkages between various processing machines and play an important role in the logistics system of FMS. This paper focuses on the flexible job-shop co-scheduling problem (FJCSP) for machines and AGVs to improve system flexibility and production efficiency. From a practical perspective, FJCSP is widely present in industries such as intelligent manufacturing of hardware products [3] and automated container terminals [4]. From a theoretical perspective, although FJCSP can be regarded as a variant of FJSP, it becomes more complex due to the increase in scheduling entities. Therefore, FJCSP is a practically urgent and theoretically valuable optimization problem.

In FJCSP, the completion time of jobs consists of processing time and no-load/load time, which is affected by the processing sequence on machines and the transportation sequence of AGVs together. The sequential-logic constraint between the transportation stage and processing stage of each operation makes it difficult to decouple the problem. The difficulty of FJCSP increases obviously in contrast with FJSP, which is mainly reflected in the following aspects:

1) In addition to the scheduling problem of processing machines under the operation constraints, the task allocation problem of the AGVs also needs to be solved, which will commonly expand the solution space;
2) The transport behaviors of AGVs including no-load and load phases are significantly different from the processing behaviors of machines. These two types of behaviors are executed alternately, and necessary waiting phases may occur during execution. This brings a more complex cascading effect for calculating the completion time of jobs;
3) The interdependence between processing tasks and transportation tasks is difficult to decouple, which means layering or decoupling mechanisms are likely to lose the optimal solution.
The practical urgency of simultaneous scheduling in FMS with AGVs and the difficulty have attracted some scholars to study this problem. Recently, Li conducted a review on integrated flexible job shop scheduling problems, in which the co-scheduling problem with AGV was mentioned [5]. The early research on FJCSP dates back to the 1990s. Doo et al. set two AGV models based on Petri nets for the material handling and a model for the processing stage. These models were integrated into a single coherent model and a scheduling method that employed Petri nets, and a heuristic search was used for a better solution [6]. Bilge and Ulusoy established a nonlinear mixed-integer programming model and proposed a heuristic algorithm to generate machine schedules and a sliding time windows heuristic for the vehicle scheduling [7]. Later, more and more scholars began to pay attention to this problem. Lacomme et al. researched the simultaneous job input sequencing and vehicle dispatching problem in FMS with a single AGV [8]. Then, they proposed a branch-andbound coupled with a discrete event simulation model to evaluate the job sequence under the given vehicle and machine dispatching rules [9].

As a popular evolutionary algorithm, genetic algorithm (GA) has been designed into many variants to solve
similar problems. Ulusoy et al. adopted a genetic algorithm with a special uniform crossover operator and two mutation operators, and lots of instances were solved to evaluate the proposed algorithm [10]. Chaudhry et al. proposed a spreadsheet-based GA approach to solving the co-scheduling problem. An adaptation of the proprietary GA software was demonstrated to minimize the total completion time or makespan in FMS [11]. Badakhshian et al. adopted a fuzzy controller to control the behavior of the GA during solving the scheduling problem [12]. Nouri et al. proposed a hybrid metaheuristic approach based on clustered holonic multiagent model. A neighborhood-based GA for global exploration was adopted and a set of cluster agents used tabu search for promising regions [13]. Meng et al. designed a diversity check method into GA to prevent the decline of population diversity [14].

Some other evolutionary algorithms were also employed to solve FJCSP. Gnanavel Babu et al. proposed a new meta-heuristic differential evolution algorithm to minimize the makespan [15]. Tatsushi et al. addressed a bilevel decomposition algorithm for solving the simultaneous scheduling and conflict-free routing problems for AGVs to minimize the total weighted tardiness. A mixed-integer formulation was decomposed into task assignment and routing subproblems which were solved by using Lagrangian relaxation [16]. Zheng et al. established a mixed-integer linear programming model and proposed heuristic algorithm based on tabu search, which included a novel two-dimensional solution representation and the generating operation of two neighbor solutions [17]. Wen et al. designed a harmony search algorithm with a neighborhood search incorporating problem knowledge to guide the search [18].

More hybrid or multi-stage algorithms were proposed to solve the complex problem. Saidi Mehrabad et al. considered the scheduling problem containing the conflict-free routing problem for AGVs and the basic job-shop scheduling problem, and proposed a two-stage ant colony algorithm to solve it [19]. Considering real situations such as deadlock or blockage, Lin et al. proposed a hybrid algorithm based on GA and optimal computing budget allocation to reduce simulation replications [20]. Nageswararao et al. proposed a new meta-heuristic gravitational search algorithm to solve the simultaneous scheduling problem and the adequacy of the algorithm was demonstrated by comparing it with existing results [21]. Lyu et al. adopted a hybrid consisting of GA and Dijkstra algorithm to solve the scheduling problem with the objectives of minimizing the makespan and the transportation time [22].

Despite the above research, the problem is still worth studying further. As most scholars have stated, FJCSP is an expansion of the traditional FJSP [23]. However, on the other hand, due to the AGVs introduced into the problem, the routing issue of AGVs arises and may even become dominant in some cases. Therefore, the approach to solving this problem needs to be designed from the above two views. As we know, the estimation of distribution algorithm (EDA) is a novel evolutionary algorithm based on statistical learning theory and has been applied widely to similar scheduling problems [2].

EDA estimates the probability distribution of elite individuals and builds a probability model of the most promising area by statistical information according to the historical search experience. In addition, the ant colony algorithm (ACO) has been widely applied to path-related scheduling problems such as the path planning problem [24] and vehicle routing problem [25], [26]. EDA and ACO are both based on statistical models, namely the probability model and the pheromone model, respectively. Compared with the other methods like GAs, EDA and ACO are conducive to absorbing various problem knowledge. For a complex problem, reasonable heuristics designed by fully using the problem knowledge can commonly achieve better performance.
This paper intends to use the two modeling-based methods to extract and utilize the statistical information of the elite solutions for global exploration through their complementation and collaboration from different views. The main innovations and contributions of this paper include the following issues:

1) To the best of our knowledge, this is the first attempt to solve FJCSP by the cooperation of two modeling-based methods described different features of elites, i.e., EDA and ACO. The two methods generate new solutions independently and share elites to update respective models. The use of them is adjusted adaptively to adapt to the varying demands of multi-view modeling in different cases or different search stages;
2) Inspired by successful application of EDA to the traditional FJSP, a probability model in EDA is designed to abstract the information in superior solutions about the operation positions and the rule selection for scheduling machines and AGVs is designed for generating a solution;
3) Considering the AGVs introduced into the problem and the path issue arising, a job-path pheromone model and an AGV-path pheromone model in ACO are designed to jointly determine the selection of the job-machine-AGV combinations to generate a solution;
4) In view of the three types of path segments in the critical path, a local search with a targeted three-layer operator is designed to improve elites. The hybrid algorithm combining two modeling-based methods for global exploration and the local search for local exploitation shows advantages in different cases.
The remainder of this paper is organized as follows. The problem model and the objective function are described in Section II and the details about the proposed hybrid algorithm are displayed in Section III. Finally, the experiment results are shown and analyzed to verify the proposed algorithm in Section IV and the conclusions are presented in Section V.

## II. Problem Formulation

## A. Problem Description

In an FMS with AGVs as illustrated in Fig.1, there are three kinds of entities to be considered: jobs, machines and AGVs. Each job contains a series of operations to be processed sequentially by different machines. Each machine has the ability to process more than one operation, and each AGV can carry different jobs between any two machines for the
![img-0.jpeg](img-0.jpeg)

Fig. 1. Flexible manufacturing system with AGVs.
![img-1.jpeg](img-1.jpeg)

Fig. 2. A simple handling procedure of two jobs.
next operations along the planned or given path. In particular, the different operations of a job can be transported by different AGVs. FJCSP can be divided into four sub-problems:

1) The assignment problem of processing tasks: assign a processing machine for each operation;
2) The assignment problem for transportation tasks: assign a transport AGV for each operation;
3) The sequencing problem of processing tasks: plan a processing sequence for each machine;
4) The sequencing problem of transportation tasks: plan a transporting sequence for each AGV.
In this paper, the objective of the problem is to minimize the makespan, i.e., the time when all the jobs have been processed. The notations are listed in Table I. The decision variables are $X_{j i m}, Y_{j i i, j j i}^{m}, Z_{j i k}$ and $W_{j i i, j j i}^{k}$, corresponding to the four sub-problems aforementioned.

The handling procedure for two jobs is shown in Fig. 2, where (1)-(4) represents the routing sequence of AGVs. A complete operation-handled duration contains the no-load moving stage of the AGV, the load transportation stage for the job and the processing stage on the machine. For $O_{22}$-handled duration in Fig. 2, AGV $A_{2}$ will move from the machine $M_{1}$ to $M_{2}$ to take job $J_{2}$ (no-load stage). Then, it will deliver $J_{2}$ from $M_{2}$ to the target machine $M_{1}$ for processing $O_{22}$ (load stage). The processing stage of $O_{22}$ on $M_{1}$ is the same as in FJSP (processing stage). The interaction phase between different entities, e.g. the phase when jobs are taken from machines to AGVs, will cause some waiting time, such as the waiting time for $O_{11}$ and the waiting time for $M_{2}$.

Remark 1: From Fig. 2, it can be found that the added no-load/load stages and more waiting stages in FJCSP in

TABLE I
DESCRIPTION OF KEY SYMBOLS

| Symbol | Description |
| :--: | :--: |
| $N_{J}$ | The number of jobs to be processed. |
| $N_{M}$ | The number of machines in FMS. |
| $N_{A}$ | The number of AGVs in FMS. |
| $J$ | The index set of jobs, $J=\{1,2, \ldots, N_{J}\}$. |
| $J_{j}$ | The $j$-th job, $j \in J$. |
| $M$ | The index set of machines, $M=\{1,2, \ldots, N_{M}\}$. |
| $M_{m}$ | The $m$-th machine, $m \in M$. |
| $A$ | The index set of AGVs, $A=\left\{1,2, \ldots, N_{A}\right\}$. |
| $A_{k}$ | The $k$-th AGV, $k \in A$. |
| $N_{j}^{o p r}$ | The total number of the operations of $J_{j}, j \in J$. |
| $N_{O}$ | The total number of all the operations, $N_{O}=\sum_{i=1}^{N_{J}} N_{j}^{\text {opr }}$. |
| $O_{j}^{\text {opr }}$ | The index set of the operations of $J_{j}, O_{j}^{\text {opr }}=\left\{1,2, \ldots, N_{j}^{\text {opr }}\right\}, j \in J$. |
| $O_{j}^{C}$ | The $i$-th operation of $J_{j}, i \in O_{j}^{\text {opr }}$. |
| $S_{j}^{D}$ | The processing stage of $O_{j i}$. |
| $S_{j}^{D}$ | The loaded transportation stage of $O_{j i}$. |
| $S_{j}^{D}$ | The no-load moving stage of $O_{j i}$. |
| $\Omega_{j i}$ | The index set of machines which can handle $O_{j i}$. |
| $t_{j i m}^{D}$ | The processing time of $O_{j i}$ on $M_{m}, m \in \Omega_{j i}$. |
| $D$ | The position index set of the raw material area and machines, $D=\left\{0,1, \ldots, N_{M}\right\}$. |
| $D_{d}$ | The position set of the raw material area and machines, $d \in D, D_{0}$. means the position of raw material and $M_{m}$ is located at $D_{m}, m \in M$. |
| $t_{d_{1} d_{2}}^{r}$ | The no-load time between two positions, $\forall d_{1}, d_{2} \in D$. |
| $t_{d_{1} d_{2}}^{r}$ | The transportation time between two positions, $\forall d_{1}, d_{2} \in D$. |
| $T s t_{j_{1}}^{r}$ | The starting time of the no-load stage $S_{j_{1}}^{D}$ for $O_{j i}$. |
| $T s t_{j_{2}}^{r}$ | The ending time of the no-load stage $S_{j_{2}}^{D}$ for $O_{j i}$. |
| $T s t_{j_{3}}^{r}$ | The starting time of the transportation stage $S_{j_{3}}^{T}$ for $O_{j i}$. |
| $T s t_{j_{3}}$ | The ending time of the transportation stage $S_{j_{3}}^{T}$ for $O_{j i}$. |
| $T s p_{j i}$ | The starting time of the processing stage $S_{j_{3}}^{P}$ of $O_{j i}$. |
| $T s p_{j k}$ | The ending time of the processing stage $S_{j_{3}}^{P}$ of $O_{j i}$. |
| $X_{j i m}$ | If $O_{j i}$ is processed on $M_{m}, X_{j i m}=1$; otherwise, $X_{j i m}=0$. |
| $Y_{j i}^{m}$ | If $O_{j_{1} i_{1}}$ is processed on $M_{m}$ before $O_{j_{2} i_{2}}, Y_{j_{1} i_{1}, j_{2} i_{2}}^{m}=1$; otherwise, $Y_{j_{1} i_{1}, j_{2} i_{2}}^{m}=0$. |
| $Z_{j i k}$ | If $A_{k}$ takes $O_{j i}, Z_{j i k}=1$; otherwise, $Z_{j i k}=0$. |
| $W_{j_{1} i_{1}, j_{2} i_{2}}^{k}$ | If $A_{k}$ takes $O_{j_{1} i_{1}}$ before $O_{j_{2} i_{2}}, W_{j_{1} i_{1}, j_{2} i_{2}}^{k}=1$; otherwise, $W_{j_{1} i_{1}, j_{2} i_{2}}^{k}=0$. |

contrast with FJSP bring more obvious coupling relations, which increases the difficulty of solving this problem.

In order to grasp the problem backbone and simplify redundancy, some assumptions are necessary and are shown as follows:

1) Each machine has sufficient input/output buffer space for storing the jobs;
2) Each machine is allowed to process at most one operation at any time;
3) Each operation is not preemptive;
4) The processing time of each operation on different machines are available and deterministic;
5) All AGVs are identical and cost the same and predetermined transportation time on the same path;
6) Each AGV will start its first task at the material area;
7) Each AGV is allowed to transport at most one job at any time;
8) The traffic congestion and path conflict of AGVs are not taken into account;
9) When completing a transportation task, the AGV will move to the next transportation task and wait until the task can be executable.

## B. Constraints

According to the above descriptions, the following constraints must be satisfied.

$$
\sum_{m \in \Omega_{j i}} X_{j i m}=1, \forall j \in J, \forall i \in O_{j}^{o p r}
$$

$$
\begin{aligned}
& \sum_{k \in A} Z_{j i k}=1, \quad \forall j \in J, \forall i \in O_{j}^{o p r} \\
& \sum_{j_{1}=1}^{N_{J}} \sum_{i_{1}=1}^{N_{J}^{o p r}} Y_{j_{1} i_{1}, j_{2} i_{2}}^{m} \cdot X_{j_{2} i_{2} m} \leq 1, \forall j_{2} \in J, \\
& \forall i_{2} \in O_{j_{2}}^{o p r}, \forall m \in M \\
& \sum_{j_{1}=1}^{N_{J}} \sum_{i_{1}=1}^{N_{J}^{o p r}} \sum_{j_{2}=1}^{N_{J}} \sum_{i_{2}=1}^{N_{J}^{o p r}} Y_{j_{1} i_{1}, j_{2} i_{2}}^{m} \cdot X_{j_{1} i_{1} m} \cdot X_{j_{2} i_{2} m} \\
& =Q_{m}-1, \forall m \in M \\
& \sum_{j_{1}=1}^{N_{J}} \sum_{i_{1}=1}^{N_{J}^{o p r}} W_{j_{1} i_{1}, j_{2} i_{2}}^{k} \cdot Z_{j_{2} i_{2} k} \leq 1, \forall j_{2} \in J, \\
& \forall i_{2} \in O_{j_{2}}^{o p r}, \forall k \in A \\
& \sum_{j_{1}=1}^{N_{J}} \sum_{i_{1}=1}^{N_{J}^{o p r}} \sum_{j_{2}=1}^{N_{J}^{o p r}} W_{j_{1} i_{1}, j_{2} i_{2}}^{k} \cdot Z_{j_{1} i_{1} k} \cdot Z_{j_{2} i_{2} k} \\
& =H_{k}-1, \forall k \in A
\end{aligned}
$$

where $Q_{m}=\sum_{j_{1}=1}^{N_{J}} \sum_{i_{1}=1}^{N_{J}^{o p r}} X_{j_{2} i_{1} m}$ means the total number of processing tasks of the $M_{m}(m \in M)$ and $H_{k}=$ $\sum_{j_{1}=1}^{N_{J}} \sum_{i_{1}=1}^{N_{J}^{o p r}} Z_{j_{1} i_{1} k}$ means the total number of transportation tasks of the $A_{k}(k \in A)$.

Eq. (1) means that each operation can be processed by only one machine. Eq. (2) means that each operation can be transported by only one AGV. Eqs. (3)-(4) imply that each machine will handle all of its assigned operations sequentially. Eqs. (5)-(6) imply that each AGV will perform its transportation tasks sequentially.

## C. Objective

The optimization objective is to minimize the makespan which means the time when all the jobs have been processed and is defined as follows:

$$
C \max =\max \left\{T e p_{j N_{j}^{o p r}} \mid j \in J\right\}
$$

where $C \max$ is the maximum completion time of all jobs and $T e p_{j N_{j}^{o p r}}$ can be calculated according to Eq. (8)-(13).

$$
T e p_{j_{2} i_{2}}=T s p_{j_{1} i_{1}}+t_{j_{2} i_{2} m_{3}}^{P}
$$

where $X_{j_{2} i_{2} m_{3}}=1, j_{2} \in J, i_{2} \in O_{j_{2}}^{o p r}$ and $m_{3} \in M$.

$$
T s p_{j_{2} i_{2}}=\max \left\{T e t_{j_{2} i_{2}}, T e p_{j_{2} i_{3}}\right\}
$$

where $Y_{j_{2} i_{1}, j_{2} i_{2}}^{m_{3}}=1, j_{2}, j_{3} \in J, i_{2} \in O_{j_{2}}^{o p r}$ and $i_{3} \in O_{j_{3}}^{o p r}$.

$$
T e t_{j_{2} i_{2}}=T s t_{j_{2} i_{2}}+t_{d_{2} d_{3}}
$$

where $d_{2}, d_{3}$ are the position indexes of $M_{m_{2}}$ and $M_{m_{3}}$, $X_{j_{2}\left(i_{2}-1\right) m_{2}}=1, X_{j_{2} i_{2} m_{3}}=1, Z_{j_{3} i_{3} k}=1, j_{2} \in J, i_{2} \in O_{j_{3}}^{o p r}$ and $m_{2}, m_{3} \in M$.

$$
T s t_{j_{2} i_{2}}=\max \left\{T e p_{j_{1}\left(i_{2}-1\right)}, T e t_{j_{2} i_{2}}^{\prime}\right\}
$$

where $j_{2} \in J$ and $i_{2} \in O_{j_{2}}^{o p r}$.

$$
T e t_{j_{2} i_{2}}^{\prime}=T s t_{j_{2} i_{2}}^{\prime}+t_{d_{1} d_{2}}^{\prime}
$$

![img-2.jpeg](img-2.jpeg)

Fig. 3. A chromosome example of FJCSP.
where $d_{1}, d_{2}$ are the position indexes of $M_{m_{1}}$ and $M_{m_{2}}$, $W_{j_{1} i_{1}, j_{2} i_{2}}^{k}=1, X_{j_{2}\left(i_{2}-1\right) m_{2}}=1, X_{j_{1} i_{1} m_{1}}=1, Z_{j_{2} i_{2} k}=1$, $Z_{j_{1} i_{1} k}=1, j_{1}, j_{2} \in J, i_{1} \in O_{j_{1}}^{o p r}, i_{2} \in O_{j_{2}}^{o p r}$ and $m_{1}, m_{2} \in M$.

$$
T s t_{j_{2} i_{2}}^{i_{2}}=T e t_{j_{1} i_{1}}
$$

where $Z_{j_{1} i_{1} k}=1, Z_{j_{2} i_{2} k}=1, W_{j_{1} i_{1}, j_{2} i_{2}}^{k}=1, j_{1}, j_{2} \in J, i_{1} \in$ $O_{j_{1}}^{o p r}, i_{2} \in O_{j_{2}}^{o p r}$ and $k \in A$.

Eq. (8) means that the ending time of the processing stage consists of the starting time and the processing time of the operation. Eq. (9) implies that the operation will begin to be processed after the job is transported to the machine and the previous processing task in the machine is completed. Eq. (10) means that the ending time of the transportation stage consists of the starting time and the transportation time on the AGV. Eq. (11) means that the job needs to be transported after the previous operation of the job is processed and the AGV reaches the machine processing the previous operation. Eq. (12) is the constraint of the ending time of the noload stage. Eq. (13) implies that the AGV must complete the previous transportation task before taking the current operation.

## D. Model of FJCSP

On the basis of the above analysis, the mathematical model can be summarized as follows:

$$
\begin{aligned}
& \min C \max =\max \left\{\operatorname{Te}_{j N_{j}^{\text {opr }}} \mid j \in J\right\} \\
& \text { s.t. Eqs. }(1)-(6)
\end{aligned}
$$

Remark 2: The scale of an FJCSP can be described as a tuple $\left\langle N_{J}, N_{O}, N_{M}, N_{A}\right\rangle$ consisting of the numbers of jobs, machines, operations and AGVs.

## E. Encoding Method

In this section, a three-layer representation of the solution is adopted. The genes in the first layer (operation layer) are responsible for the expression of the processing and transportation sequence of all operations. The genes in the second layer (machine layer) are the indexes of machines to process the operations at corresponding positions in the operation layer. The genes in the third layer (AGV layer) are the indexes of AGVs that transport the corresponding jobs. The encoding example of an instance with the scale of $\langle 3,9,4,3\rangle$ is shown in Fig.3. The complete scheduling scheme of this example can be described as a sequence of combinations about
the operations and the assignment of machines and AGVs $\left(O_{j i}, m, k\right)$. Each $\left(O_{j i}, m, k\right)$ means that $O_{j i}$ is assigned to the $M_{m}$ and is transported by the $A_{k}$. Therefore, the scheduling scheme can be described as follows: $\left(O_{11}, 2,1\right),\left(O_{21}, 4,2\right)$, $\left(O_{12}, 1,3\right),\left(O_{31}, 3,1\right),\left(O_{22}, 1,3\right),\left(O_{23}, 2,2\right),\left(O_{32}, 4,1\right)$, $\left(O_{13}, 1,3\right),\left(O_{33}, 2,1\right)$.

## F. Decoding Method

According to the three-layer chromosome, the decision variables can be determined. $X_{j i m}$ and $Z_{j i k}$ can be determined through the combination $\left(O_{j i}, m, k\right)$ in the chromosome. In addition, $Y_{j_{1} i_{1}, j_{2} i_{2}}^{m}$ and $W_{j_{1} i_{1}, j_{2} i_{2}}^{k}$ can be assigned by the sequential relationship between combinations. For the solution in Fig. 3, the decision variables which will be set to 1 are shown below the chromosome. According to the combination $\left(O_{21}, 4,2\right)$ of the 2 nd operation in the chromosome, $X_{214}=1$ and $Z_{212}=1$. Because the operation to be processed next by $M_{4}$ is $O_{32}, Y_{21,32}^{4}=1$. Because the operation to be transported next by $A_{2}$ is $O_{23}, W_{21,23}^{2}=1$. The more direct decoding procedures are shown in Algorithm 1.

## Algorithm 1 Decoding Process

1: Input: The chromosome of a solution $x$;
2: Output: The makespan of $x$;
3: $T e j_{j} \Leftarrow 0, \forall j \in J ; \%$ Set the initial time on jobs;
4: $D e j_{j} \Leftarrow 0, \forall j \in J ; \%$ Set the position index of each job;
5: $T e m_{m} \Leftarrow 0, \forall m \in M ; \%$ Set the initial time on machines;
6: $T e a_{k} \Leftarrow 0, \forall k \in A ; \%$ Set the initial time on AGVs;
7: $D e a_{k} \Leftarrow 0, \forall k \in A ; \%$ Set the position index of each AGV;
8: for $g=1$ to $N_{O}$ do:
9: Extract the combination $\left(O_{j i}, m, k\right)$ of the $g$-th column in the chromosome;
10: $\quad$ Tst $t_{j i}^{\prime}=T e a_{k}$ according to Eq.(13);
11: $\quad$ Tet $_{j i}^{\prime}=$ Tst $t_{j i}^{\prime}+t^{\prime}{ }_{D e a_{k} D e j_{j}}$ according to Eq.(12);
12: $\quad$ Tst $t_{j i}=\max \left\{T e j_{j}, T e t_{j i}^{\prime}\right\}$ according to Eq.(11);
13: $\quad$ Tet $_{j i}=T e t_{j i}^{\prime}+t_{D e j_{j} m}$ according to Eq.(10);
14: $\quad$ Tsp $_{j i}=\max \left\{T e t_{j i}, T e m_{m}\right\}$ according to Eq.(9);
15: $\quad$ Tep $_{j i}=T s p_{j i}+t_{j i m}^{p}$ according to Eq.(8);
16: $\quad$ Update $T e j_{j} \Leftarrow T e p_{j i}, D e j_{j} \Leftarrow m, T e m_{m} \Leftarrow T e p_{j i}$, $T e a_{k} \Leftarrow T e t_{j i}, D e a_{k} \Leftarrow m$;
17: end for
18: Calculate the makespan according to Eq. (7).

## III. Hybrid Algorithm for FJCSP

In this paper, we propose a multi-view modeling-based hybrid algorithm, in which EDA with a probability model and ACO with a pheromone model are designed to conduct the global exploration cooperatively. In addition, a local search based on the critical path method is used for local exploitation.

## A. Optimization Methods Based on Statistical Model

The model mentioned in the proposed algorithm refers to statistical model that attempts to estimate some kind of characteristics of the optimal solution. The statistical model

![img-3.jpeg](img-3.jpeg)

Fig. 4. The two views of FJCSP.
can help to interpret the results of previous optimization steps and to plan the next ones [27]. The feature selection of the solution is closely related to the establishment of the statistical model. Therefore, the feature selection is important and only the models reflecting key features of the optimal solution are necessary.

For complex problems, a single model may be weak because it does not reflect completely or accurately the key features. Compared with a single model, multiple models with different key features can bring the following benefits:

1) Multiple models can characterize the solution more comprehensively and reduce dependence on a single model;
2) Multiple models can improve population diversity and reduce the possibility of premature convergence.
The modeling method from multiple views (perspectives) can be applied to FJCSP as shown in Fig. 4. On the one hand (machine-dominating view), FJCSP can be regarded as an extension of FJSP and most scholars designed their algorithms from this view. On the other hand (AGV-dominating view), the routing problem of AGVs may be the main issue in some cases when the transportation stages take more time than the processing stages. It can be found that the algorithms designed from any single view may be weak for these instances due to the difference of key features. Therefore, we introduced EDA and ACO for the two features to solve FJCSP. In this paper, we design a novel probability model in EDA and a joint pheromone model in ACO to grasp the key features of elite solutions from the two views, respectively. In the proposed hybrid algorithm, EDA and ACO generate solutions independently and achieve cooperation by sharing elites. Compared with previously proposed algorithms such as GAs, the modeling-based method establishes a statistical model for the distribution of the entire population, describing the direction of evolution through this model. It represents a macroscopic level simulation. Furthermore, the modeling-based method enables more convenient utilization of problem knowledge.

## B. Probability Model in EDA

The probability model can be described as three matrixes, i.e., operation-related probability matrix (OPM, $P^{\text {opr }}$ ), machine-related probability matrix (MPM, $P^{\text {mac }}$ ) and AGV-related probability matrix (APM, $P^{\text {agv }}$ ) to generate the three-layer representation of a solution in Section II-E. The

TABLE II
Selection Rules of AGVs and Machines for Processing $O_{j(i \times 1)}$

| Rule | Description |
| :-- | :-- |
| ASR1 | Select the AGV that reaches the material area the earliest. |
| ASR2 | Select the AGV that is available the earliest. |
| ASR3 | Select the AGV that reaches the current machine the latest before <br> $O_{j i}$ is finished, if one exists. Otherwise, select the AGV that <br> reaches the machine the earliest. |
| ASR4 | Select the AGV that reaches the current machine the earliest after <br> $O_{j i}$ is finished, if one exists. Otherwise, select the AGV that <br> reaches the machine the latest. |
| ASR5 | Select the AGV that minimizes waiting time for each other. |
| ASR6 | Select the AGV that reaches the machine the earliest. |
| ASR7 | Select the AGV that is available the earliest. |
| MSR1 | Select the machine that finishes the operation the earliest. |
| MSR2 | Select the machine that is available the earliest. |
| MSR3 | Select the machine that is available the latest before $J_{j}$ reaches it, <br> if one exists. Otherwise, select the machine that is available the <br> earliest. |
| MSR4 | Select the machine that is available the earliest after $J_{j}$ reaches it, <br> if one exists. Otherwise, select the machine that is available the <br> latest. |
| MSR5 | Select the machine that minimizes waiting time for each other. |
| MSR6 | Select the machine that finishes processing $O_{i j}$ the earliest. |
| MSR7 | Select the machine that is available the earliest. |

operation layer can be generated from the first position to the last by sampling the OPM directly. However, the machine layer and the AGV layer need to be generated according to the heuristic rule selected by the MPM and the APM. These heuristic rules for machines and AGVs which can obtain good-quality solutions are introduced, and the heuristic rules including 7 machine selection rules (MSR) and 7 AGV selection rules (ASR) can be referred to the recent research [28] as shown in Table II. ASR1, ASR2, MSR1 and MSR2 are the selection rules for $O_{j 1}(j \in J)$.

The probability matrixes can be described as follows:

$$
\begin{aligned}
P^{\text {opr }}(l) & =\left[p_{i j}^{\text {opr }}(l)\right]_{N_{i i} \times N_{j}} \\
P^{\text {mac }}(l) & =\left[p_{j}^{\text {mac }}(l)\right]_{N_{R M} \times 1} \\
P^{\text {agv }}(l) & =\left[p_{j}^{\text {agv }}(l)\right]_{N_{R A} \times 1}
\end{aligned}
$$

where $N_{R M}$ is the number of the machine scheduling rules and $N_{R A}$ is the number of the AGV scheduling rules; the element $p_{i j}^{\text {opr }}(l)$ of $P^{\text {opr }}$ means the probability that $J_{j}$ appears at position $i$ in the first layer at generation $l$. The element $p_{j}^{\text {mac }}(l)$ of $P^{\text {mac }}$ represents the probability that the genes in the second layer for processing operations are selected by the $j$-th MSR at generation $l$. The element $p_{j}^{\text {agv }}(l)$ of $P^{\text {agv }}$ represents the probability that the genes in the third layer for processing operations are selected by the $j$-th ASR at generation $l$.

Without prior knowledge, these probability matrices are uniformly initialized, and the update mechanisms of the three probability matrixes are as follows:

$$
\begin{aligned}
& p_{i j}^{\text {opr }}(l+1)=\left(1-\lambda^{e d a}\right) p_{i j}^{\text {opr }}(l)+\frac{\lambda^{e d a}}{N_{s}} \sum_{s=1}^{N_{s}} I_{s i j}^{\text {opr }} \\
& p_{j}^{\text {mac }}(l+1)=\left(1-\lambda^{e d a}\right) p_{j}^{\text {mac }}(l)+\frac{\lambda^{e d a}}{N_{s}} \sum_{s=1}^{N_{s}} I_{s j}^{\text {mac }} \\
& p_{j}^{\text {agv }}(l+1)=\left(1-\lambda^{e d a}\right) p_{j}^{\text {agv }}(l)+\frac{\lambda^{e d a}}{N_{s}} \sum_{s=1}^{N_{s}} I_{s j}^{\text {agv }}
\end{aligned}
$$

where $N_{s}$ represents the number of superior individuals and $\lambda^{e d a}$ is the learning rate. $I_{s j j}^{o p r}, I_{s j}^{m a c}$ and $I_{s j}^{a g v}$ are the indicators as follows:

$$
\begin{aligned}
I_{s j j}^{o p r} & =\left\{\begin{array}{cl}
1, & \text { if the } j \text {-th job appears at position } i \\
& \text { in the } s \text {-th solution, } \\
0, & \text { else. }
\end{array}\right. \\
I_{s j}^{m a c} & =\left\{\begin{array}{cl}
1, & \text { if the } j \text {-th MSR is applied in the } \\
& s \text {-th solution, } \\
0, & \text { else. }
\end{array}\right. \\
I_{s j}^{a g v} & =\left\{\begin{array}{cl}
1, & \text { if the } j \text {-th ASR is applied in the } \\
& s \text {-th solution, } \\
0, & \text { else. }
\end{array}\right.
\end{aligned}
$$

The pseudo-code of sampling a solution by EDA is shown in Algorithm 2.

## Algorithm 2 Sampling a Solution by EDA

1: Input: $P^{o p r}, P^{a g v}, P^{m a c}$;
2: Output: A solution $x$;
3: Set $g \Leftarrow 1$;
4: for $l=1$ to $N_{J}$ do:
5: $\quad \varepsilon_{l}=0 \%$ Initialize the operation index of each job;
6: end for
7: while $g \leq N_{O}$ do: \% Obtain the operation sequence;
8: for $l=1$ to $N_{J}$ do:
9: $\quad R(l)=\left\{\begin{array}{l}p_{g l}^{o p r}, \text { if } \varepsilon_{l}<N_{l}^{o p r}, \\ 0, \text { else. }\end{array}\right.$ $\%$ Build roulette;
10: end for
11: $\quad$ Normalize $(R) \%$ Normalize the roulette;
12: Obtain a job index $j$ on the $g$-th position in operation layer by wheeling $R$;
13: Set $\varepsilon_{j} \Leftarrow \varepsilon_{j}+1, g \Leftarrow g+1$;
14: end while
15: Obtain an ASR by sampling $P^{a g v}$ in roulette wheel;
16: Obtain an MSR by sampling $P^{m a c}$ in roulette wheel;
17: Set $G \Leftarrow\left\{O_{j i} \mid j \in J, i \in N_{j}^{o p r}\right\}, g \Leftarrow 1$;
18: while $G \neq \emptyset$ do:
19: Retrieve the $g$-th operation $O_{j i}$ to be assigned next in the operation layer;
20: Assign $A_{k}$ for $O_{j i}$ using ASR shown in Table II;
21: Assign $M_{m}$ for $O_{j i}$ using MSR shown in Table II;
22: Update $T s t_{j i}^{\prime}, T e t_{j i}^{\prime}, T s t_{j i}, T e t_{j i}, T s p_{j i}$ and $T e p_{j i}$ of $O_{j i}$ for $J_{j}, M_{m}$ and $A_{k}$ as shown in Algorithm 1;
23: Set $G \Leftarrow G /\left\{O_{j i}\right\}, g \Leftarrow g+1$.
24: end while

## C. Pheromone Model in ACO

ACO was originally proposed by Dorigo, Maniezzo and Colorni in the 1990s. In the process of studying ant foraging, they found that ant colony as a whole can reflect swarm intelligence for optimizing by simple behaviors of each ant, including laying pheromone to the environment and deciding the next step based on the pheromone.

1) Pheromone Design: As the key element of ACO for solving the problem in this paper, the pheromone needs to be redesigned to fit the problem feature. Considering the operation flows of jobs and the paths of AGVs in FMS, two kinds of pheromones are designed: job-related pheromone $\tau_{j i d_{i} m}^{j o b}(l)$ and AGV-related pheromone $\tau_{d_{i} d_{2}}^{a g v}(l)$. The element in job-related pheromone $\tau_{j i d_{i} m}^{j o b}(l)$ represents the pheromone amount deposited for $J_{j}$ from the current position $D_{d_{i}}$ to the target position $D_{m}$ to process $O_{j_{i}}$ at generation $l$. The element in AGV-related pheromone $\tau_{d_{i} d_{2}}^{a g v}(l)$ represents the total pheromone deposited for AGVs from the current position $D_{d_{i}}$ to $D_{d_{2}}$ at generation $l$. They can be initialized as follows:

$$
\begin{aligned}
\tau_{j i d_{i} m}^{j o b}(0) & =\frac{1}{|D|}, \quad j \in J, \quad i \in N_{j}^{o p r}, \quad d_{1} \in D, m \in M \\
\tau_{d_{1} d_{2}}^{a g v}(0) & =\frac{1}{|D|}, \quad d_{1}, d_{2} \in D
\end{aligned}
$$

where the initial pheromone value on each path is set as $1 /|D|$ uniformly.
2) Transition Strategy: According to the two pheromone models, a set of combinations of job-machine-AGV are selected step by step until all the operations are assigned. In this way, each ant will select one machine and one AGV for one operation in each step.

The selection of the combination $\left(O_{j i}, m, k\right)$ depends on the joint factor of the two pheromones. Define the joint pheromone factor as follows:

$$
\tau_{j i m k}^{j o i n t}(l)=\left(\tau_{d_{k} d_{1}}^{a g v}(l)+\tau_{d_{1} m}^{a g v}(l)\right) \times \tau_{j i d_{i} m}^{j o b}(l)
$$

where $d_{k}$ is the current position index of $A_{k}$ when $A_{k}$ starts to transport $O_{j i}, d_{1}$ is the current position index of $J_{j}$ and $m$ is the position index of the target machine for processing $O_{j i}$.

The probability for selecting the combination $\left(O_{j i}, m, k\right)$ by roulette wheel is

$$
p_{j i m k}=\frac{\tau_{j i m k}^{j o i n t}}{\sum_{O_{j i} \in G} \sum_{m \in \Omega_{i j}} \sum_{k \in A} \tau_{j i m k}^{j o i n t}}
$$

where $p_{j i m k}$ is the probability of selecting $A_{k}$ to transport $O_{j i}$ to $M_{m}$, and $G$ is the set of operations to be processed next. The pseudo-code of sampling a solution by ACO is shown in Algorithm 3.

Remark 3: All the optional combinations about all the operations to be processed, the available machines and AGVs are considered in Eq. (27). For example, if $O_{12}$ and $O_{32}$ need to be processed and the number of the available AGVs is $N_{A}$, then the total number of all the optional combinations are $\left|\Omega_{12}\right| \times N_{A}+\left|\Omega_{32}\right| \times N_{A}$.
3) Pheromone Trail Update Rule: The pheromone trail update rule of the two matrixes for route selection is shown as follows:

$$
\tau_{j i d_{i} m}^{j o b}(l+1)=\xi^{a c o} \tau_{j i d_{i} m}^{j o b}(l)+\left(1-\xi^{a c o}\right) \Delta \tau_{j i d_{i} m}^{j o b}(l)
$$

where $\Delta \tau_{j i d_{i} m}^{j o b}(l)=\sum_{s=1}^{N_{s}} I_{s j i d_{i} m}^{j o b} / N_{s}$ is the pheromone amount added by $N_{s}$ superior individuals for $J_{j}$ from $D_{d_{1}}$ to $D_{m}$ for processing $O_{j i}$, and $\xi^{a c o}$ is the volatilization rate of ACO.

$$
\tau_{d_{1} d_{2}}^{a g v}(l+1)=\xi^{a c o} \tau_{d_{1} d_{2}}^{a g v}(l)+\left(1-\xi^{a c o}\right) \Delta \tau_{d_{1} d_{2}}^{a g v}(l)
$$

![img-4.jpeg](img-4.jpeg)

Fig. 5. An Illustration for generating a solution by EDA/ACO.
where $\Delta \tau_{d_{1} d_{2}}^{o g v}(l)=\sum_{s=1}^{N_{s}} I_{o d_{1} d_{2}}^{o g v} / N_{s}$ is the pheromone amount added by $N_{s}$ superior individuals for AGVs from $D_{d_{1}}$ to $D_{d_{2}}$.

```
Algorithm 3 Sampling a Solution by ACO
    Input: \(\tau_{j: d_{1} m}^{j o b}: \tau_{d_{1} d_{2}}^{o g v}\).
    Output: A solution \(x\);
    Set \(G \Leftarrow\left\{O_{j 1} \mid j \in J\right\}\);
    while \(G \neq \emptyset\) do:
        for \(O_{j i}\) in \(G\) do:
            for \(k\) in \(A\) do:
                for \(m\) in \(\Omega_{j i}\) do:
                    Calculate the joint factor \(\tau_{j: m k}^{j o t o t}\) about trans-
        porting \(O_{j i}\) to \(M_{m}\) by \(A_{k}\) according to (26);
        Select the combination of \(\left(O_{j i}, m, k\right)\) by roulette
        wheel according to the probability matrix in (27);
            \(G \Leftarrow G /\left\{O_{j i}\right\}\)
            If \(i \neq N_{j}^{j p r}\), then \(G \Leftarrow G \cup\left\{O_{j(i+1)}\right\}\).
    end while
```

In proposed hybrid algorithm, both EDA and ACO can sample a complete solution independently. However, they generate solutions from different aspects. The detailed illustration in Fig. 5 shows the sampling procedures of EDA and ACO. For EDA, the operation sequence in the first layer of the chromosome, MSR and ASR are obtained by sampling by OPM, MPM and APM, respectively. And then the schemes for machines and AGVs are determined according to MSR, ASR and the operation sequence step by step. For ACO, the ant will select an operation to be processed next, an optional machine and an AGV simultaneously in each step according to the pheromones.

## D. EDA/ACO Selection Ratio

The use proportion of EDA and ACO needs to be adjusted dynamically according to their performance. The reason can be summarized into two points:

1) Their performance may be different for various cases;
2) Their performance may be varying with search stages.

Therefore, we define $\lambda(l) \in[0.1,0.9]$ as the selection ratio of EDA and ACO in the $l$-th iteration. Initially, set $\lambda(0)=0.5$ without prior knowledge, which means an equal chance of
selecting EDA and ACO. The update rule of $\lambda(l)$ is shown as follows:

$$
\lambda(l+1)=(1-\omega) \cdot \lambda(l)+\omega \cdot \frac{N_{E}}{N_{B}}
$$

where $\omega$ denotes the learning rate, $N_{E}$ is the number of individuals generated by EDA in elite individuals and $N_{B}$ is the number of elite individuals.

## E. Selection Mechanism

In order to maintain the population diversity and keep the best individuals in the population, a multi-strategy selection operation needs to be designed. Firstly, the elite reservation is embedded into the selection mechanism. The individual with the best performance will always be selected for the next generation. Secondly, a survival ratio parameter $P_{s}$ means the proportion of the individuals selected from the population into the next generation in the whole population. According to the parameter, the binary tournament selection strategy is adopted to select a specified number of individuals for the next generation. In order to supplement the population diversity, a reproduction strategy is adopted to maintain the previous population size and improve the population diversity.

## F. Local Search Based on Critical Path Method

Although EDA and ACO can pay more attention to the characteristics of problems for global exploration, the local exploitation in solution space still needs to be implemented by a local search [29]. In the traditional research for job shop scheduling problems, many local search methods based on the critical path method (CPM) have been studied widely and have good performance [30]. There are no idle time and no possible overlap time between any two adjacent processes in the critical path. No idle time means no time can be compressed and no possible overlap time means there is a strict logical relationship about the task sequence. The length of the critical path is equal to the makespan.

For the simultaneous scheduling problem, a critical path may include the processing and transportation blocks, called machine-blocks and $A G V$-blocks, respectively [31]. For example in Fig. 6, three machine-blocks and three AGV-blocks make up of the critical path $P^{C}, S_{11}^{T} \Rightarrow S_{11}^{P} \Rightarrow S_{12}^{T} S_{22}^{T} S_{22}^{T} \Rightarrow$ $S_{22}^{P} \Rightarrow S_{23}^{T} \Rightarrow S_{23}^{P} S_{33}^{P}$. From the perspective of the operation,

![img-5.jpeg](img-5.jpeg)

Fig. 6. An example of a critical path in gantt chart.
$S_{11}^{T}$ and $S_{11}^{P}$ of $O_{11}, S_{12}^{T}$ of $O_{12}, S_{22}^{T} S_{22}^{T}$ and $S_{22}^{P}$ of $O_{22}, S_{23}^{T}$ and $S_{23}^{P}$ of $O_{23}, S_{23}^{T}$ of $O_{33}$ make up the critical path $P^{C}$. Thus, for $O_{j i}$ in the critical path, there may be the following three kinds of cases:
Case1: $S_{j i}^{T} \in P^{C} \& S_{j i}^{P} \in P^{C}$ means both the transportation stage and processing stage of $O_{j i}$ are in the critical path;
Case2: $S_{j i}^{T} \notin P^{C} \& S_{j i}^{P} \in P^{C}$ means only the processing stage of $O_{j i}$ is in the critical path;
Case3: $S_{j i}^{T} \in P^{C} \& S_{j i}^{P} \notin P^{C}$ means only the transportation stage of $O_{j i}$ is in the critical path.
In order to reduce the length of the critical path (to minimize makespan), three operators for the above three cases of an $O_{j i}$ selected randomly on critical path are proposed to define the neighborhood structures for local search:
Opr1 for case1: Exchange three-layer genes with a random adjacent operation of $O_{j i}$;
Opr2 for case2: Replace randomly the gene in the machine layer of $O_{j i}$ with another optional machine;
Opr3 for case3: Replace randomly the gene in the AGV layer of $O_{j i}$ with another optional AGV.

## Algorithm 4 Local Search Based on CPM

1: Input: a solution $x$ and the number of iteration Iter $\operatorname{Max}_{\max }^{L S}$;
2: Output: An improved solution $x^{\prime}$;
3: Set $g=0$;
4: while $g<$ Iter $_{\text {max }}^{L S}$ do
5: Find the critical path $P_{C}$ of $x$;
6: Select an operation $O_{j i}$ in $P_{C}$ randomly;
7: if $S_{j i}^{T} \in P^{C}$ and $S_{j i}^{P} \in P^{C}$ then
8: $\quad$ Execute Opr1 for $x$ to generate $x^{\prime}$;
9: if $S_{j i}^{P} \in P^{C}$ and $S_{j i}^{T} \notin P^{C}$ then
10: Execute $O p r 2$ for $x$ to generate $x^{\prime}$;
11: if $S_{j i}^{T} \in P^{C}$ and $S_{j i}^{P} \notin P^{C}$ then
12: Execute $O p r 3$ for $x$ to generate $x^{\prime}$;
13: Calculate the makespan value $C_{\max }^{\prime}$ for $x^{\prime}$;
if $C_{\max }^{\prime}<C_{\max }$ then
$x \Leftarrow x^{\prime}$
$C_{\max } \Leftarrow C_{\max }^{\prime}$
15: $g \Leftarrow g+1$;
16: end while
19: $x^{\prime} \Leftarrow x$.

TABLE III
Time COMPLEXITY ANALYSIS

| Procedure | Time complexity |
| :-- | :-- |
| Generating a new population | $O\left(N \cdot N_{J}^{S}\right)$ |
| Selecting elite individuals | $O\left(N_{x}\right)$ |
| Updating models of EDA and ACO | $O\left(N_{x} \cdot N_{J}^{S}\right)$ |
| Improving a solution by local search | $O\left(\right.$ Iter $\left._{\max }^{\text {LSS }}\right)$ |
| Updating ratio of selecting EDA/ACO | $O\left(N_{x}\right)$ |

The pseudo-code of CPM-based local search is shown in Algorithm 4. In every generation, the local search will be applied Iter $_{\text {max }}^{L S}=200$ times on the best individual of the current population, and the better solution found by local search will replace the old one. Although only a few genes in the new solution are changed by local search, the solution still needs to be re-evaluated completely, which costs the same time as evaluating a solution generated by EDA or ACO.

## G. Procedure of Proposed Algorithm

In the first stage, the search space is sampled according to the selection ratio $\lambda$ of EDA and ACO to generate a new population by Algorithm 2 and Algorithm 3. Then, the elite group is selected for the following updating process of probability matrixes and pheromone matrixes. Then, the CPM-based local search is carried out to improve the best individuals by Algorithm 4. The probability model of EDA and the pheromone model of ACO are updated by the information of the elite group. In addition, $\lambda$ is also updated by the performance of EDA and ACO according to (30). Finally, whether the evolutionary loop is stopped is determined by the termination criterion.

## H. Computational Complexity Analysis

At each generation of the proposed algorithm, the time complexity analysis is presented in Table III.

The time complexity of generating a new population by ACO or EDA is $O\left(N \cdot N_{J}^{S}\right)$. For the binary tournament selection of the proposed algorithm, there is a computational complexity of $O\left(N_{x}\right)$. Then, about the update process for the probability model of EDA and pheromone in ACO, it has a computational complexity of $O\left(N_{x} \cdot N_{J}^{S}\right)$. For the local search based on CPM, the computational complexity is $O\left(\right.$ Iter $_{\text {max }}^{L S}$ ). Therefore, the main time complexity is introduced by generating a new population and updating the models of EDA and ACO.

## IV. NUMERICAL RESULTS AND COMPARISONS

## A. Design of Experiments

In this section, we design three experiments for analyzing the proposed algorithm. In the first experiment, the Taguchi method is carried out for setting key parameters of the proposed algorithm (namely EDA_ACO_LS) for the different instances. In the second experiment, the following algorithms are run 30 times for solving different instances to verify the effectiveness and advantages of the proposed algorithm:

1) sEDA: The single EDA which uses the same probability model and parameter values in EDA_ACO_LS;

2) sACO: The single ACO which uses the same pheromone model and parameter values in EDA_ACO_LS;
3) EDA_ACO: The hybrid algorithm combining probability model and pheromone model without the local search in EDA_ACO_LS;
4) RGA [32]: A multi-objective hybrid genetic algorithm combining a selection strategy for AGVs, in which probability of crossover $C R=0.8$ and probability of mutation $M R=0.4$
5) PDE [33]: A differential evolution with a machine selection heuristic and a vehicle assignment heuristic in which $C R=0.5$ and scaling factor $F=0.8$
6) GATS [34]: A hierarchical procedure that combines a genetic algorithm and a tabu search procedure, whose $C R=1$ and $M R=1$
7) BRKGA [28]: An operation-based multi-start biased random key genetic algorithm coupled with greedy heuristics to select the machine processing each operation and the vehicles transporting the jobs to operations, whose selection proportion of elites $P_{S}=0.2, M R=0.1$ and elite inheritance probability $P_{E}=0.7$.
The above comparison algorithms proposed in previous literature are calibrated for the benchmark reported in Bilge and Ulusoy [7] and BRKGA can also be calibrated according to the percentage gaps. All the calibration results are shown in the attachment. Finally, a case study in a real-world intelligent hardware factory is carried out for the actual production.
Three benchmarks are carried out for discussion and analysis, including small-sized instances by Deroussi and Norre [35], small-sized instances by Kumar et.al [33] and small-medium-large-sized instances by Homayouni et.al [28]. All of these instances are collected from https://fastma nufacturingproject.wordpress.com/2019/04/11/fjspt-instances/. These instances are named by a set of strings. For example, Deroussi_6_15_8_2 means the instance proposed by Deroussi has 6 jobs, 15 operations, 8 machines and 2 AGVs.
In this paper, each instance for the following experiments will be run 30 times independently. All of the following experiments for different algorithms are carried out with AMD Ryzen 74800 H (2.90GHz) with Radeon Graphics (RAM_32G). All algorithms will be terminated after evaluating solutions the maximum number $N S E$ times shown in Eq. (31) to keep fairness. In addition, the number of evaluations during the local search in EDA_ACO_LS is also considered into $N S E$.

$$
N S E=100 \times N_{O} \times N_{M} \times N_{A}
$$

## B. Parameter Setting

The proposed algorithm has the following key parameters: 1) population size $(N)$; 2) selection ratio of the elite group $\left(P_{s}\right)$; 3) the learning rate of probability model in EDA $\left(\lambda^{e d a}\right)$; 4) the evaporation factor of pheromone in ACO ( $\xi^{a c o}$ ); 5) the learning rate of the selection ratio ( $\omega$ ). In this paper, the Taguchi method of design-of-experiment is applied to discuss the influence of the five parameters [36]. Among all the parameters of the problem, $t / p$ is important to represent the relative size between transportation time and

TABLE IV
Orthogonal Array and RV Values

| Experiment | Factor Level |  |  |  | Makespan |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Number | N | $P_{s}$ | $\lambda^{\text {e } d a}$ | $\xi^{\text {aco }}$ | $\omega$ | Exp1 | Exp2 |
| 1 | 100 | 0.1 | 0.2 | 0.2 | 0.2 | 1156.3 | 192.5 |
| 2 | 100 | 0.2 | 0.4 | 0.4 | 0.4 | 1158.2 | 192.1 |
| 3 | 100 | 0.3 | 0.6 | 0.6 | 0.6 | 1156.7 | 192.8 |
| 4 | 100 | 0.4 | 0.8 | 0.8 | 0.8 | 1166.0 | 195.3 |
| 5 | 200 | 0.1 | 0.4 | 0.6 | 0.8 | 1143.4 | 191.8 |
| 6 | 200 | 0.2 | 0.2 | 0.8 | 0.6 | 1142.4 | 194.6 |
| 7 | 200 | 0.3 | 0.8 | 0.2 | 0.4 | 1131.5 | 190.5 |
| 8 | 200 | 0.4 | 0.6 | 0.4 | 0.2 | 1144.7 | 192.6 |
| 9 | 300 | 0.1 | 0.6 | 0.8 | 0.4 | 1141.2 | 190.6 |
| 10 | 300 | 0.2 | 0.8 | 0.6 | 0.2 | 1132.3 | 190.3 |
| 11 | 300 | 0.3 | 0.2 | 0.4 | 0.8 | 1130.5 | 192.7 |
| 12 | 300 | 0.4 | 0.4 | 0.2 | 0.6 | 1137.1 | 193.0 |
| 13 | 400 | 0.1 | 0.8 | 0.4 | 0.6 | 1122.2 | 190.0 |
| 14 | 400 | 0.2 | 0.6 | 0.2 | 0.8 | 1133.7 | 191.3 |
| 15 | 400 | 0.3 | 0.2 | 0.8 | 0.2 | 1135.0 | 191.9 |
| 16 | 400 | 0.4 | 0.2 | 0.6 | 0.4 | 1135.0 | 192.5 |

TABLE V
Response Table For ExPI

| Factor Level | N | $P_{s}$ | $\lambda^{\text {e } d a}$ | $\xi^{\text {aco }}$ | $\omega$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1159 | 1141 | 1141 | 1140 | 1142 |
| 2 | 1140 | 1142 | 1143 | $\mathbf{1 1 3 9}$ | 1141 |
| 3 | 1135 | $\mathbf{1 1 3 8}$ | 1144 | 1142 | $\mathbf{1 1 4 0}$ |
| 4 | $\mathbf{1 1 3 1}$ | 1146 | $\mathbf{1 1 3 8}$ | 1146 | 1143 |
| Delta | 29 | 8 | 6 | 7 | 4 |
| Rank | 1 | 2 | 4 | 3 | 5 |

processing time in an instance [7]. Four levels of each parameter are set, i.e., $N \in\{100,200,300,400\}, P_{s} \in$ $\{0.1,0.2,0.3,0.4\}, \lambda^{e d a} \in\{0.2,0.4,0.6,0.8\}, \xi^{a c o} \in\{0.2,0.4$, $0.6,0.8\}, \omega \in\{0.2,0.4,0.6,0.8\}$. Two instances, Homayouni_11_44_8_2(Exp1) and Homayouni_10_55_6_2(Exp2), are selected to test these parameters, whose $t / p$ are equal to 0.04 and 2.25 , respectively.

According to the Taguchi method, a set of tests with different parameter values are carried out to establish the orthogonal array $L_{16}\left(4^{5}\right)$. For each test, the proposed algorithm is run 30 times independently and the average fitness value (makespan) is calculated and filled into Table IV. Then, the response average values of each factor level for different instances are shown in Table V and Table VI. It can be found that the major differences between instances with different $t / p$ are the $P_{s}$ and $\omega$. From the Rank vectors in Table V and Table VI, it is obvious that the population size $(N)$ and the selection ratio of the elite group $\left(P_{s}\right)$ are more important than the other parameters. Considering the different $t / p$ levels of different instances, the two combinations of the five parameters for different instances are introduced and shown in Table VII according to the factor levels in Table V and Table VI. In general, the difference in parameter selection of the algorithm under different calculation examples is acceptable.

## C. Experimental Analysis

First of all, a comparisons criterion under significant differences needs to be stated: if Alg 1 performs better than $A l g 2$, one of the following conditions needs to be met: 1) $\operatorname{Mean}(A l g 1)<\operatorname{Mean}(A l g 2)$; 2) Mean $(A l g 1)=\operatorname{Mean}(A l g 2)$ and $\operatorname{Std}(A l g 1)<\operatorname{Std}(A l g 2)$,

![img-6.jpeg](img-6.jpeg)

Fig. 7. The radio map of the gaps with best results $(\rho=1.0)$ of different algorithms for all instances.

TABLE VI
RESPONSE TABLE FOR EXP2

| Factor Level | $N$ | $P_{x}$ | $\lambda^{\text {cdo }}$ | $\xi^{\text {inco }}$ | $\omega$ |
| :--: | --: | --: | --: | --: | --: |
| 1 | 193.2 | $\mathbf{1 9 1 . 3}$ | 193.1 | $\mathbf{1 9 1 . 8}$ | 191.8 |
| 2 | 192.4 | 192.1 | 192.2 | $\mathbf{1 9 1 . 8}$ | $\mathbf{1 9 1 . 4}$ |
| 3 | 191.7 | 192.0 | 191.8 | 191.9 | 192.6 |
| 4 | $\mathbf{1 9 1 . 4}$ | 193.3 | $\mathbf{1 9 1 . 5}$ | 193.1 | 192.8 |
| Delta | 1.7 | 2.1 | 1.5 | 1.3 | 1.3 |
| Rank | 2 | 1 | 3 | 5 | 4 |

TABLE VII
Suggested COMBinaTION OF PARAMETERS

| Instance | $N$ | $P_{x}$ | $\lambda^{\text {cdo }}$ | $\xi^{\text {inco }}$ | $\omega$ |
| :--: | --: | --: | --: | --: | --: |
| $t / p \leq 0.5$ | 400 | 0.3 | 0.8 | 0.4 | 0.6 |
| $t / p>0.5$ | 400 | 0.1 | 0.8 | 0.4 | 0.4 |

where $A l g 1$ and $A l g 2$ means two different algorithms, $\operatorname{Min}(A l g 1), \operatorname{Mean}(A l g 1)$ and $\operatorname{Std}(A l g 1)$ indicate the minimum value, the mean value and the standard deviation of the vector of the best makespan found by $A l g 1$ in the runs of 30 times. Then, the rank of an algorithm for an instance is defined as the number of other comparison algorithms which the algorithm performs worse than. For example, the rank of EDA_ACO_LS among all comparison algorithms for an instance is Rank5 means that 5 algorithms outperforms EDA_ACO_LS. Obviously, the higher rank of an algorithm, the better its performance.

Due to space constraints, the experiment results for various instances with different scales and $t / p$ are briefly shown in a radio map as Fig. 7 and more details are listed in the attachment. In the radio map of Fig. 7, a data point can be represented as $(\theta, \rho)$. The angular coordinate $\theta$ indicates the instance index and the radial coordinate $\rho$ is a measure on the
![img-7.jpeg](img-7.jpeg)

Fig. 8. The distribution of performance levels among sEDA, sACO and EDA_ACO (The average $t / p$ of the instances in different ranks are shown above histograms).
![img-8.jpeg](img-8.jpeg)

Fig. 9. Change of the selection ratio $\lambda$.
tending to the best makespan $M k b$ for an algorithm $A l g$, which is calculated by $\rho=1-G a p$, where $G a p=[\operatorname{Mean}(A l g)-$ $M k b] / M k b \times 100 \%$. The more detail analysis will be shown in the following sections. A non-parameter statistical significance test method, i.e., the Mann-Whitney U test (Rank Sum Test, Rst) [37] at a significance level of 0.05 was used to analyze

![img-9.jpeg](img-9.jpeg)

Fig. 10. The distribution of performance ranks of all comparison algorithms for all instances.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Makespan distribution of different algorithms in classical instances.
the statistical significance of the results. The test results are also shown in attachment. In addition, we find new bounds of three instances including Ins85, Ins86 and Ins88, and the solutions are listed in Table IX of Appendix.

1) Effect of the Combination of EDA and ACO: In order to verify the effectiveness of the combination of the two models, EDA_ACO is compared with sEDA and sACO for solving all the instances. The statistical information about the performance ranks among the three algorithms and the number of instances on the corresponding ranks of each algorithm is shown in Fig. 8. In addition, the average values of $t / p$ in different ranks are also shown above the corresponding blocks to analyze the influence of $t / p$ on these algorithms. For example, the blue block of EDA_ACO indicates that the number of instances on which EDA_ACO performs the best is 57 and the average $t / p$ of these instances is equal to 0.32 . From the figure, the following points can be summarized:
2) EDA_ACO performs the best in most of the instances, which means that the method combining EDA and ACO is more effective than any single-model method;
3) The average $t / p$ values of sEDA in Rank1 and Rank2 are significantly less than sACO, which means sEDA performs better than sACO if $t / p$ is small, and otherwise, sACO performs better than sEDA.
These conclusions become another basis for setting the algorithm parameters according to the problem parameter $t / p$. Despite the above points, we still cannot clearly define which
model performs better than the other one in a certain instance. In the analysis for the selection ratio, it can be found the combination of EDA and ACO is still necessary. In addition, EDA_ACO, sEDA and sACO still need to be improved due to the lack of a local exploration mechanism.
4) Effect of Local Search: To verify the effectiveness of the local search proposed, EDA_ACO and EDA_ACO_LS are compared for solving all the instances. From Fig.7, it can be found that EDA_ACO_LS performs better than EDA_ACO in more than 50 instances at least. The obvious advantage indicates that the proposed local search can greatly improve the solution under global search by EDA and ACO.
5) Effect of Selection Ratio: Fig. 9 shows the change curves of the selection ratio $\lambda$ with iterations for different instances including Ins84, Ins85, Ins86, Ins87 and Ins88. For Ins88, it can be found that EDA was mainly used to generate individuals in the early iterations, but the ACO performed better than EDA in the late iteration. The diversified trend of these curves indicates that this parameter can be adjusted adaptively according to different instances and search stages to ensure the performance of the proposed algorithm. This adaptive adjustment, coupled with innovative and effective modeling-based methods, has brought about a significant improvement in solution efficiency. In summary, the hybrid mechanisms in EDA_ACO_LS, including hybrid modeling and local search operator, all contribute to the advantages of the hybrid algorithm.
6) Comparison With State-of-the-Art Algorithms: The statistics of comparison experiments are visually displayed in Figs. 7 and 10. From Fig. 7, EDA_ACO_LS is closer to the edge of radar image, which means the average performance in 30 runs of EDA_ACO_LS is better than the other algorithms. From Fig. 10, it obvious that the proposed algorithm performs the best among all the algorithms in 50 instances and performs the second best in 30 instances. It should be noted that the comparison algorithms such as PDE and BRKGA can find the same best solution as EDA_ACO_LS during the 30 runs, and they outperform the other algorithms in 20 and 18 instances, respectively. In order to explore the stability of the solution results of each algorithm, the distribution of optimization results for 4 classical instances is shown in Fig. 11. From the box graphs, it can be found that the proposed algorithm performs more stable for better results.

![img-11.jpeg](img-11.jpeg)

Fig. 12. The hardware factory.

TABLE VIII
Results of the Case Study in a Hardware Factory

| $1 / p$ | EDA_ACO_LS |  |  | RGA |  |  | PDE |  |  | GATS |  |  | BRKGA |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Best(min) | Aver(min) | Die | Best(min) | Aver(min) | Die | Best(min) | Aver(min) | Die | Best(min) | Aver(min) | Die | Best(min) | Aver(min) | Die |
| 0.11 | 403.7 | 411.2 | 7.40e-02 | 422.4 (-) | 432.7 | 2.27e-01 | 418.9 (-) | 427.9 | 6.82e-02 | 411 (-) | 426.5 | 1.57e-01 | 457 (-) | 466.0 | 1.34e-01 |

TABLE IX
The Information on the New Upper Bounds

| Ins85 | Hom_11_44_8_2 | Best makespan $=1113.0$ |
| :-- | :-- | :-- | :-- |
| job layer: | 946203514472103659411038262917958101300710588670 |  |
| machine layer: | 31202010453614225712314674657426453367345467 |  |
| AGV layer: | 10011011111111001011111100000111010001100010101 |  |
| Ins86 | Hom_12_48_8_2 | Best makespan $=1233.0$ |
| job layer: | 24071132148403985204178112697111100387656310951110169105 |  |
| machine layer: | 102310604256432346715427154641735623452647674653 |  |
| AGV layer: | 10011110010011100101001101110111101111011101001001010 |  |
| Ins88 | Hom_10_58_6_2 | Best makespan= 147.0 |
| job layer: | 5335831068527326180499721009264978254615307948150926441773 |  |
| machine layer: | 5115114515501144455134144014441545413411145541154544111552 |  |
| AGV layer: | 011100101111001011110010000111010101100000000100010111110011 |  |

5) Discussion of Experimental Results: The better performance of the proposed algorithm is mainly attributed to the following reasons:
1) Considering the similarity of FJCSP with FJSP and AGV-routing problem in different cases, a modelingbased method combining EDA and ACO for describing different features of the two problems is innovated;
2) EDA and ACO generate solutions independently and cooperate by sharing elites. The use of the EDA and ACO is dynamically adjusted to make the algorithm adapt to different problems and search stages for global exploration;
3) The local search with a three-layer operator based on critical path method is proposed to improve local exploitation.

## D. A Case Study

Supported by the demonstration project we participated in, we cooperated with the hardware factory in the project and completed a case study. Due to the complexity and diversity of hardware workpieces, the flexible intelligent factory covers a series of processes including lathing, planing, milling, cutting, bending, polishing, drilling and spraying. In addition, the factory has introduced AGVs for transporting semi-finished products under the control of centralized dispatching system.

The aerial view of the factory and the layout of the area for our case study are shown in Fig. 12. The demonstration area mainly consists of four functional areas, namely, the processing area, the standby area, the storage area and the transport track area. In the processing area, different kinds of machines are arranged modularly. In the standby area, 5 AGVs with quick response code navigation are initially placed for transporting materials as also shown in Fig. 12. After the materials are processed along the given routes, they will be temporarily stored in the storage area. For the example of machining bend pipe for a chair, a raw pipe will be processed by cutting, bending, punching, and painting in turn, and finally packaged with other types of finished products for sale.

With the data collected from the factory and the AGV website, the case study is carried out practically. The experiment result of the case study is shown in Table VIII. From this table, it can be found that EDA_ACO_LS can find a better solution than the other four algorithms.

## V. CONCLUSION

In this paper, a multi-view modeling-based hybrid algorithm combining EDA with a novel probability model and ACO with a pheromone model is proposed to minimize the makespan of the scheduling problem for machines and AGVs. A novel EDA whose probability model is designed to describe the

information of the operation position and the rule selection for scheduling machines and AGVs is proposed. Simultaneously, a joint model with the job-related and the AGV-related pheromone in ACO is proposed to generate new individuals. In addition, a local search based on a critical path is customized to apply to this problem. An adaptive parameter is designed to regulate the use of the two methods to adapt to the varying demands of multi-view modeling in different cases and search stages. The parameter experiment and comparison experiment are carried out and the advantage of the proposed algorithm is proved by the statistical analysis. Three new upper bounds are found by the proposed algorithm. Finally, we conducted a case study in a hardware factory to finish the actual verification. In the future, the dynamic or multi-objective simultaneous scheduling problem needs to be studied.

## APPENDIX

New bounds of three instances including Ins85, Ins86 and Ins88 are found, and the solutions are listed in Table IX.

## REFERENCES

[1] J.-Q. Li et al., "A hybrid iterated greedy algorithm for a crane transportation flexible job shop problem," IEEE Trans. Autom. Sci. Eng., vol. 19, no. 3, pp. 2153-2170, Jul. 2022.
[2] W. Shao, D. Pi, and Z. Shao, "A Pareto-based estimation of distribution algorithm for solving multiobjective distributed no-wait flow-shop scheduling problem with sequence-dependent setup time," IEEE Trans. Autom. Sci. Eng., vol. 16, no. 3, pp. 1344-1360, Jul. 2019.
[3] Y. Liu, Y. Zhao, K. Li, S. Yu, and S. Li, "Design and application research of a digitized intelligent factory in a discrete manufacturing industry," Intell. Autom. Soft Comput., vol. 26, no. 5, pp. 1081-1096, 2020.
[4] Y. Yang, M. Zhong, Y. Dessouky, and O. Postolache, "An integrated scheduling method for AGV routing in automated container terminals," Comput. Ind. Eng., vol. 126, pp. 482-493, Dec. 2018.
[5] X. Li et al., "Survey of integrated flexible job shop scheduling problems," Comput. Ind. Eng., vol. 174, Dec. 2022, Art. no. 108786.
[6] D. Y. Lee and F. DiCesare, "Integrated scheduling of flexible manufacturing systems employing automated guided vehicles," IEEE Trans. Ind. Electron., vol. 41, no. 6, pp. 602-610, Dec. 1994.
[7] Ü. Bilge and G. Ulusoy, "A time window approach to simultaneous scheduling of machines and material handling system in an FMS," Oper. Res., vol. 43, no. 6, pp. 1058-1070, Dec. 1995.
[8] P. Lacomme, A. Moukrim, and N. Tchernev, "A new lower bound for scheduling of FMS based on AGV material handling," IFAC Proc. Volumes, vol. 35, no. 1, pp. 217-222, 2002.
[9] P. Lacomme, A. Moukrim, and N. Tchernev, "Simultaneous job input sequencing and vehicle dispatching in a single-vehicle automated guided vehicle system: A heuristic branch-and-bound approach coupled with a discrete events simulation model," Int. J. Prod. Res., vol. 43, no. 9, pp. 1911-1942, May 2005.
[10] G. Ulusoy, F. Sivrikaya-Šerifoğlu, and Ü. Bilge, "A genetic algorithm approach to the simultaneous scheduling of machines and automated guided vehicles," Comput. Oper. Res., vol. 24, no. 4, pp. 335-351, Apr. 1997.
[11] I. A. Chandlery, S. Mahmood, and M. Shami, "Simultaneous scheduling of machines and automated guided vehicles in flexible manufacturing systems using genetic algorithms," J. Central South Univ., vol. 18, no. 5, pp. 1473-1486, Oct. 2011.
[12] M. Badakhshian, "Performance optimization of simultaneous machine and automated guided vehicle scheduling using fuzzy logic controller based genetic algorithm," Int. J. Phys. Sci., vol. 7, no. 9, pp. 1461-1471, Feb. 2012.
[13] H. E. Nouri, O. B. Driss, and K. Ghédira, "Hybrid metaheuristics for scheduling of machines and transport robots in job shop environment," Int. J. Speech Technol., vol. 45, no. 3, pp. 808-828, Oct. 2016.
[14] L. Meng, W. Cheng, B. Zhang, W. Zou, W. Fang, and P. Duan, "An improved genetic algorithm for solving the multi-AGV flexible job shop scheduling problem," Sensors, vol. 23, no. 8, p. 3815, Apr. 2023.
[15] A. G. Babu, J. Jerald, A. N. Haq, V. M. Luxmi, and T. P. Vigneswaralu, "Scheduling of machines and automated guided vehicles in FMS using differential evolution," Int. J. Prod. Res., vol. 48, no. 16, pp. 4683-4699, Aug. 2010.
[16] T. Nishi, Y. Hiranaka, and I. E. Grossmann, "A bilevel decomposition algorithm for simultaneous production scheduling and conflict-free routing for automated guided vehicles," Comput. Oper. Res., vol. 38, no. 5, pp. 876-888, May 2011.
[17] Y. Zheng, Y. Xiao, and Y. Seo, "A Tabu search algorithm for simultaneous machine/AGV scheduling problem," Int. J. Prod. Res., vol. 52, no. 19, pp. 5748-5763, Oct. 2014.
[18] X. Wen, Y. Fu, W. Yang, H. Wang, Y. Zhang, and C. Sun, "An effective hybrid algorithm for joint scheduling of machines and AGVs in flexible job shop," Meas. Control, May 2023. [Online]. Available: https://journals.sagepub.com/doi/full/10.1177/00202940231173750
[19] M. Saidi-Mehrabad, S. Dehnavi-Arani, F. Evazabadian, and V. Mahmoodian, "An ant colony algorithm (ACA) for solving the new integrated model of job shop scheduling and conflictfree routing of AGVs," Comput. Ind. Eng., vol. 86, pp. 2-13, Aug. 2015.
[20] J. T. Lin, C.-C. Chiu, Y.-H. Chang, and H. M. Chen, "A hybrid genetic algorithm for simultaneous scheduling of machines and AGVs in FMS," in Industrial Engineering, Management Science and Applications, M. Gen, K. J. Kim, X. Huang, and Y. Hiroshi, Eds. Berlin, Heidelberg: Springer, 2015, pp. 277-286.
[21] M. Nageswararao, K. Narayanarao, and G. Rangajanardhana, "Scheduling of machines and automated guided vehicles in FMS using gravitational search algorithm," Appl. Mech. Mater., vol. 867, pp. 307-313, Jul. 2017.
[22] X. Lyu, Y. Song, C. He, Q. Lei, and W. Guo, "Approach to integrated scheduling problems considering optimal number of automated guided vehicles and conflict-free routing in flexible manufacturing systems," IEEE Access, vol. 7, pp. 74909-74924, 2019.
[23] S. M. Homayouni and D. B. M. M. Fontes, "Production and transport scheduling in flexible job shop manufacturing systems," J. Global Optim., vol. 79, no. 2, pp. 463-502, Feb. 2021.
[24] D. Li, L. Wang, J. Cai, K. Ma, and T. Tan, "Research on terminal distance index-based multi-step ant colony optimization for mobile robot path planning," IEEE Trans. Autom. Sci. Eng., Oct. 2022. [Online]. Available: https://ieeexplore.ieee.org/abstract/document/9919849
[25] S.-H. Huang, Y.-H. Huang, C. A. Blazquez, and C.-Y. Chen, "Solving the vehicle routing problem with drone for delivery services using an ant colony optimization algorithm," Adv. Eng. Informat., vol. 51, Jan. 2022, Art. no. 101536.
[26] Y. Ding, B. Xin, and J. Chen, "A review of recent advances in coordination between unmanned aerial and ground vehicles," Unmanned Syst., vol. 9, no. 2, pp. 97-117, Apr. 2021.
[27] A. Žilinskas, "A review of statistical models for global optimization," J. Global Optim., vol. 2, no. 2, pp. 145-153, Jun. 1992.
[28] S. M. Homayouni, D. B. M. M. Fontes, and J. F. Gonçalves, "A multistart biased random key genetic algorithm for the flexible job shop scheduling problem with transportation," Int. Trans. Oper. Res., vol. 30, no. 2, pp. 688-716, Mar. 2023.
[29] F. Neri and C. Cotta, "Memetic algorithms and memetic computing optimization: A literature review," Swarm Evol. Comput., vol. 2, pp. 1-14, Feb. 2012.
[30] S.-Y. Wang and L. Wang, "An estimation of distribution algorithm-based memetic algorithm for the distributed assembly permutation flow-shop scheduling problem," IEEE Trans. Syst., Man, Cybern. Syst., vol. 46, no. 1, pp. 139-149, Jan. 2016.
[31] J. Hurink and S. Knust, "Tabu search algorithms for job-shop problems with a single transport robot," Eur. J. Oper. Res., vol. 162, no. 1, pp. 99-111, Apr. 2005.
[32] B. S. P. Reddy and C. S. P. Rao, "A hybrid multi-objective GA for simultaneous scheduling of machines and AGVs in FMS," Int. J. Adv. Manuf. Technol., vol. 31, nos. 5-6, pp. 602-613, Nov. 2006.
[33] M. V. S. Kumar, R. Janardhana, and C. S. P. Rao, "Simultaneous scheduling of machines and vehicles in an FMS environment with alternative routing," Int. J. Adv. Manuf. Technol., vol. 53, nos. 1-4, pp. 339-351, Mar. 2011.

[34] Q. Zhang, H. Manier, and M.-A. Manier, "A genetic algorithm with tabu search procedure for flexible job shop scheduling with transportation constraints and bounded processing times," Comput. Oper. Res., vol. 39, no. 7, pp. 1713-1723, Jul. 2012.
[35] L. Deroussi and S. Norre, "Simultaneous scheduling of machines and vehicles for the flexible job shop problem," in Proc. Int. Conf. Metaheuristics Nature Inspired Comput., 2010, pp. 1-2.
[36] D. C. Montgomery, Design and Analysis of Experiments. Hoboken, NJ, USA: Wiley, 2019.
[37] H. B. Mann and D. R. Whitney, "On a test of whether one of two random variables is stochastically larger than the other," Ann. Math. Statist., vol. 18, no. 1, pp. 50-60, Mar. 1947.
![img-12.jpeg](img-12.jpeg)

Bin Xin (Member, IEEE) received the B.S. degree in information engineering and the Ph.D. degree in control science and engineering from the Beijing Institute of Technology, Beijing, China, in 2004 and 2012, respectively. He was an Academic Visitor at the Decision and Cognitive Sciences Research Centre, The University of Manchester, from 2011 to 2012. He is currently a Professor at the School of Automation, Beijing Institute of Technology. His current research interests include search and optimization, evolutionary computation, unmanned systems, and multi-agent systems. He serves as an Associate Editor for many journals, such as Unmanned Systems, Advanced Control for Applications, Engineering and Industrial Systems, and the Journal of Systems Science and Complexity.
![img-13.jpeg](img-13.jpeg)

Sai Lu received the B.E. degree from Harbin Engineering University in 2017 and the M.E. degree from the Beijing Institute of Technology in 2019, where he is currently pursuing the Ph.D. degree in control science and engineering. His current interests include multi-agent systems and combinatorial optimization.
![img-14.jpeg](img-14.jpeg)

Qing Wang received the B.Eng. and Ph.D. degrees from the University of Science and Technology Beijing, Beijing, China, in 2013 and 2018, respectively. She was a Post-Doctoral Researcher with the School of Automation, Beijing Institute of Technology, Beijing, from 2018 to 2020. She is currently working at the Beijing Institute of Technology. Her current research interests include multiagent systems, nonlinear systems, and distributed optimization.
![img-15.jpeg](img-15.jpeg)

Fang Deng (Senior Member, IEEE) received the B.E. and Ph.D. degrees in control science and engineering from the Beijing Institute of Technology, Beijing, China, in 2004 and 2009, respectively. He is currently a Professor with the School of Automation, Beijing Institute of Technology. His research interests include intelligent fire control, intelligent information processing, and smart wearable devices.

Xiang Shi received the B.E. degree in automation from Qingdao University, Qingdao, China, in 2015, and the M.E. degree in control theory and control engineering from Northeastern University, Shenyang, China, in 2018. He is currently pursuing the Ph.D. degree in control science and engineering with the Beijing Institute of Technology. His current research interests include emergent systems, combinatorial optimization, and reinforcement learning.

Jun Cheng (Member, IEEE) received the B.Eng. and M.Eng. degrees from the University of Science and Technology of China, Hefei, China, in 1999 and 2002, respectively, and the Ph.D. degree from the Chinese University of Hong Kong, Hong Kong, in 2006. He is currently with the Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, Shenzhen, China, as a Professor, and the Director of the Laboratory for Human Machine Control. His current research interests include computer vision, robotics, machine intelligence, and control.

Yuhang Kang received the B.S. degree in measurement and control engineering, the M.S. degree in control science and engineering, and the Ph.D. degree in control science and engineering from Naval Aeronautical and Astronautical University, China, in 2011, 2013, and 2017, respectively. Since 2018, he has been with the Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, where he is currently an Assistant Researcher with the Human Machine Control Laboratory. His research interests include cooperative control of multi-agent systems and consensus problem.