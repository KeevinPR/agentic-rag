# A path relinking enhanced estimation of distribution algorithm for direct acyclic graph task scheduling problem 

Chu-ge Wu, Ling Wang *, Jing-jing Wang<br>Department of Automation, Tsinghua University, Beijing, 100084, China


#### Abstract

A R T I C L E I N F O

Article history: Received 22 November 2020 Received in revised form 22 June 2021 Accepted 24 June 2021 Available online 25 June 2021


Keywords:
Estimation of distribution algorithm
Direct acyclic graph task scheduling
Path relinking
Makespan
Workflow scheduling

## A B STR ACT

Superior task scheduling scheme is able to improve the performance in achieving shorter task completion time in multi-processor computing system. Large scale applications are generally modelled as direct acyclic graph (DAG) to be processed efficiently in parallel. To solve DAG task scheduling problem (DAG-SP) with the criterion of minimizing makespan, this paper proposes an estimation of distribution algorithm (EDA) enhanced by the path relinking. An efficient hybrid scheme integrating list scheduling heuristics is designed to take advantage of the knowledge of existing works. In addition, to describe the relative position relationships between the task pairs, a specific probability model is built and the task processing permutations are produced by sampling such a model. To enhance the exploitation of EDA, a path relinking based knowledge is used to design the local search method. Simulation experiments are carried out with both benchmark datasets and real-world graphs, where the comparative results show that the above designs can improve the performance effectively. Moreover, the numerical comparisons show that the proposed algorithm performs significantly better than the existing heuristics and evolutionary algorithms.
(c) 2021 Elsevier B.V. All rights reserved.

## 1. Introduction

Heterogeneous computing system (HCS) refers to a set of processors interconnected with a network, which are equipped with different computing and storage capacities. HPCs provide support for executing computationally intensive parallel applications. To facilitate scheduling decision, an application is generally modelled as a directed acyclic graph (DAG) [1], such as scientific workflows [2] and deep neural networks [3]. Efficient DAG task scheduling [4] is able to improve the application performance and the quality of user experience [5-7]. Considering both academic significance and practical value of DAG task scheduling problem (DAG-SP), this paper will address DAG-SP with the overall completion time minimization.

It is difficult to obtain efficient schedules because of the heterogeneity within the computing system and the precedence constraints between tasks, as well as the NP-hard nature of DAGSP [8]. To solve the problem more efficiently, some works are presented to describe, model and formulate the problem. A deterministic static model is given in [1] and two schedule strategies based on this model are proved that optimal solutions can be produced if there are only two processors, and the execution

[^0]periods are the same when the DAG structure is arbitrary or the execution periods are arbitrary when the DAG is an in-tree. For other situations, there does not exist a polynomial algorithm for DAG-SP due to its NP-hard nature. In addition, lower bound analysis and mixed integer linear programming (MILP) models are presented to provide a guideline for the optimization algorithms. Lower bounds of necessary number of processors, communication requests and makespan are considered in [9] and the tasks are merged and their earliest starting time (EST) are evaluated to calculate the lower bound of makespan. The above method is extended to solve the problem with total weighted completion time minimization via time-indexed linear programming relaxations in [10]. Furthermore, a knowledge-based heuristic called generalized earliest time first (GETF) is proposed where the gap between GETF solution and the optimal makespan is provided in [11]. Processors are grouped into clusters according to its speed and the task-processor assignments are suggested by the solutions of a MILP model. Similar with [11], a MILP enhanced heuristic method is proposed in [12] where an extended DAG scheduling model is given to formulate DAG-SP with deadline constraints in loT-fog system. A greedy individual time allowance approach based on MILP with binary relaxation is proposed.

Since it is difficult to obtain the optimal solution of DAG-SP within an acceptable duration under most practical cases, heuristic methods and evolutionary algorithms are widely applied to solve DAG-SP in the past few decades. Kwok and Ahmad [13] gives a detailed review on DAG scheduling heuristics and other


[^0]:    * Corresponding author.

    E-mail addresses: wucg15@mails.tsinghua.edu.cn (C. Wu), wangling@mail.tsinghua.edu.cn (L. Wang), wij18@mails.tsinghua.edu.cn (J. Wang).

algorithms, which are categorized by hybrid processor states and DAG structures. Heuristics provide approximate solutions within polynomial time periods. For DAG-SP, [14] summarizes heuristics into three categories: clustering, task duplication and list scheduling. In clustering heuristic, tasks are divided into groups, which are merged until its number equals to the number of processors. This approach performs poor in heterogeneous system [15]. Task duplication heuristic, such as duplication-based bottom-up scheduling algorithm (DBUS) [16], repeatedly allocates a set of tasks onto different processors to decrease data transfer time between processors. However, duplicated tasks increase the power consumption of processors, which is inacceptable for some computing system. Compared to these two heuristics, list heuristic provides better solutions with lower computing complexity under most situation by sorting tasks according to DAG properties. To ensure the valid topological order of tasks, this method contains two main phases: task prioritizing and processor selection.

Dynamic level scheduling [17] sorts tasks depending on an estimate of the availability of each processor and adopts EST to select the processor. The processor selection method cannot guarantee a minimum finish time when processors are not homogeneous. To fit heterogeneous environment, heterogeneous earliest finish time (HEFT) [18], a well-known heuristic is proposed, where tasks are sorted according to upward rank values (bottom-level values), i.e., the longest path length from the node to the bottom of DAG. Then, tasks are allocated to available idle time slot of the processors towards the earliest finish time (EFT). Considering the heterogeneity of computing system, the impact of different calculations, such as mean, median, worst, best values of DAG variables on different processors is studied in [19]. DAG is divided into a set of unlisted-parent trees and the task permutation is constructed according to the trees and average EST in [20], some heuristics forecast the impact of task assignment on its successive tasks. Based on HEFT, the task is assigned onto the processor minimizing the maximum EFT of its children tasks [21]. Inspired by this work, [15] builds an optimistic cost table (OCT) to list the maximum of shortest paths from its children nodes to the exit node for each combination of task and processor. For each task, average OCT value is considered and used to sort the tasks. At last, tasks are assigned to processors considering both EFT and OCT with insert-based policy. Inspired by the efficiency of existing list heuristics, task prioritizing and processor selection methods designed according to properties of DAG-SP can be abstracted as the knowledge for task scheduling.

Evolutionary algorithms are able to provide satisfactory solutions within acceptable time by data-driven search process for complex problems. Compared to heuristics, evolutionary algorithms aim to improve the quality of solutions by iteration-based search process. For DAG-SP, a variety of evolutionary techniques are reviewed in [22], where genetic algorithm (GA) [23], ant colony optimization (ACO) [24], differential evolution (DE) [25] and chemical reaction optimization (CRO) [26] are adopted. A double molecular structure-based CRO is proposed in [26] to generate and evolve task processing sequence as well as task-to-computing-node mapping sequence simultaneously. Similarly, a multiple priority queues leading GA is proposed in [23] to solve DAG-SP. The population is initialized with multiple task priority queues produced by list heuristics and its combinations and mutations. After this efficient initialization, crossover and mutation operators are adopted to evolve the solutions. Insert-based HEFT policy is as the task-processor mapping mechanism. A hybrid evolutionary algorithm is adopted in [27] to solve the data-intensive DAG-SP. Data file and computation tasks are both modelled as vertices of DAG, and data reading and writing procedures are considered. The chromosome of the proposed algorithm consists
of task and data assignment and the execution order of tasks. Local search procedures, path relinking and move-file heuristic are used to enhance the algorithm. A tailored BiogeographyBased Optimization (BBO) is adopted in [28] to solve DAG-SP, where the "task-processor" assignment array is used to encode the problem and heuristic strategy is applied to determine the task processing sequence. Migration and mutation operators are used to improve the individuals. A particle swarm optimization (PSO) algorithm is proposed in [29] for multi-objective DAG-SP to optimize makespan, load-balancing, resource utilization and speed up objectives. One task sequence is produced and kept and PSO evolves the processor selection sequence based on the task sequence. Furthermore, a deep reinforcement learning enhanced biased random-key genetic algorithm (BRKGA) is proposed in [30] to optimize both running time and peak memory usage. Taskprocessor affinities, task scheduling priorities and data transfer priorities are all considered as encoding chromosome. Deep reinforcement learning enhanced initialization observably improves the performance of BRKGA. In summary, task processing sequence and processor assignment rule are generally used to encode the problem; list heuristics can be adopted as the initial solutions of evolutionary algorithms; tasks are assigned to processors by heuristic-based policy.

From these existing research works, it is significant to achieve well-performance solutions within acceptable time by abstracting knowledge from DAG application properties and collecting information during data-driven search. Estimation of distribution algorithm (EDA) [31], [32], [33] is an appropriate algorithm to solve such a problem since its probability model can represent the precedence constraints between tasks, simulate the distribution of search space and record search information during evolution process. So far, EDA performs well on combinatorial optimization problems [34] including scheduling problems [35], [36]. With the above motivation, a tailored permutation-based EDA is adopted in this paper to generate task processing permutations. For permutationbased optimization problems, path relinking [37] is used to generate paths between two solutions, and the solutions on these paths are evaluated as a new combination of solutions. Thus, to enhance the exploitation of EDA, a path relinking [37], [38] enhanced local search mechanism is embedded into EDA to accelerate convergence. With the above special designs, DAG-SP is solved effectively by our proposed algorithm, which is demonstrated via simulation experiments with benchmark datasets and real-world graphs.

The remaining contents are organized as follows. Section 2 formulates the problems by providing DAG application and scheduling computational models. Then, four decoding methods and the proposed hybrid decoding mechanism are presented in Section 3. Section 4 introduces the proposed algorithm, including EDA and path relinking enhanced local intensification mechanism. In Section 5, numerical comparisons are given to demonstrate the effectiveness of our proposed algorithm. Some conclusions are presented in Section 6, and managerial implication and future work of this study are summarized in Section 7.

## 2. Problem statement and formulation

### 2.1. DAG application model

A four-tuple vector $<\boldsymbol{V}, \boldsymbol{E}, \boldsymbol{w}, \boldsymbol{D}>$ is used to model a DAG named $G$, where $\boldsymbol{V}(G)=\left\{V_{j} \mid j=0,1, \ldots, n-1\right\}$ denotes a set of noncommunication task vertexes and $\boldsymbol{w}(G)=\left\{w_{i}\right\}$ denotes the set of corresponding task workload. $\boldsymbol{E}(G)=\left\{e_{j} \mid i, j=0,1, \ldots, n-1\right\}$ represents a set of directed edges of $G$ where $e_{j}$ represents the directed edge between vertex $i$ and $j$, which means that there is a precedence constraint between task $i$ and $j$ and $D(G)=(D(i, j))$ denotes the transfer data size of corresponding edge.

![img-0.jpeg](img-0.jpeg)

Fig. 1. A DAG containing 14 tasks.

For task $j$, if there exists a direct path from vertex $k$ to $j$, then task $k$ is defined as a precedent task of task $j$ and $\operatorname{pred}(j)$ denotes the task set consisting of all its precedent tasks. Similarly, if vertex $j$ is reachable to $k$, then task $k$ is defined as a successive task of task $j$ and $\operatorname{succ}(j)$ denotes the task set consisting of all its successive tasks. For ease of description, a virtual entry vertex (node 0 ) and a virtual exit vertex (node $n-1$ ) are set in DAG as the virtual parent vertex of all tasks without precedent tasks and the virtual child vertex of all tasks without successive tasks correspondingly. An example of DAG is shown in Fig. 1.

In addition, to measure the impact of communication latency on computing performance, communication to computation ratio $(C C R)$ is introduced as (1). For an application, high CCR implies communication-intensive and low CCR implies computationintensive.
$C C R(G)=\frac{\sum_{i, j} D(i, j) /|E|}{\sum_{j} w_{j} / n}$

### 2.2. System model

Multi-processor system consists of a set of full connected $m$ heterogeneous processors. The processors are able to process at most one task during a certain time period. For each processor $i$, its processing speed is $v_{i}$. The computation time of task $j$ processed on processor $i$ is $w_{j} / v_{i}$. For each pair of processors $i_{1}$ and $i_{2}$, the bandwidth between each other is $B\left(i_{1}, i_{2}\right)$. The communication time between task $j_{1}$ and $j_{2}$ is $D\left(j_{1}, j_{2}\right) / B\left(i_{1}, i_{2}\right)$ where $i_{1}$ and $i_{2}$ denotes the processors of tasks $j_{1}$ and $j_{2}$. Specially, the communication time is 0 if the tasks are processed on the same processor as the transfer data can be read from memory. An example system is shown in Fig. 2.

### 2.3. Scheduling model and its notations

DAG-SP aims at optimizing the completion time by determining the task-processor assignment and task processing order. It is supposed that tasks are non-preemptive and any task can be processed only after all of its precedent tasks are finished and input data is received.

To formulate the MILP model for DAG-SP, a set of notations is given as Table 1.
$\min \max _{j} C_{j}$
![img-1.jpeg](img-1.jpeg)

Fig. 2. A fully connected computing system with 4 heterogeneous processors.

Subject to:

$$
\begin{aligned}
& \sum_{r=1}^{n} \sum_{i=1}^{m} x_{j, i, r}=1, \forall j \\
& \sum_{j=1}^{n} x_{j, i, r} \leq 1, \forall i, r \\
& \sum_{j_{1}=1}^{n} x_{j_{1}, i, r} \geq \sum_{j_{2}=1}^{n} x_{j_{2}, i, r+1}, \forall r \leq n-1, i \\
& C_{j_{1}}-C_{j_{2}}+M \cdot\left(2-x_{j_{1}, i, r+1}-x_{j_{2}, i, r}\right) \geq \frac{w_{j_{1}}}{v_{i}}, \forall j_{1}, j_{2}, r \leq n-1, i \\
& C_{j}+M \cdot\left(1-x_{j, i, 1}\right) \geq \frac{w_{j}}{v_{i}}, \forall j, i \\
& C_{j_{2}}-C_{j_{1}} \geq \sum_{r=1}^{n} \sum_{i_{2}=1}^{m} x_{j_{2}, i_{2}, r} \cdot \frac{w_{j_{2}}}{v_{i_{2}}} \\
& \quad+\sum_{i_{1}=1}^{m} \sum_{i_{2}=1}^{m} \sum_{r=1}^{n} \sum_{i=1}^{n} x_{j_{1}, i_{1}, r} \cdot x_{j_{2}, i_{2}, r} \cdot \frac{D\left(j_{1}, j_{2}\right)}{B\left(i_{1}, i_{2}\right)}, \forall j_{1} \rightarrow j_{2}
\end{aligned}
$$

where (2) defines the optimization objective, i.e., makespan; Constraints (3)-(8) guarantee feasible schedule. To be specific, (3) ensures that each task can be processed once and only once; (4) ensures that for a given position of a certain processor, no more than one task can be processed in case of avoiding the time conflict; To strictly meet the task queue, (5) means that $(r+1)$ th task does not exist in the queue if there is no the $r$-th task on the certain processor; For the tasks processed on the same machine, (6) ensures that the $(r+1)$-th task cannot be processed before the completion of the $r$-th task. In addition, (7) guarantees that the completion time of the first task on each processor is not less than its computation time. Considering the precedence constraints between the tasks, (8) ensures the tasks cannot be processed before receiving the data from its precedent tasks.

## 3. Encoding method and hybrid decoding mechanism

### 3.1. Encoding method

To represent the problem, the task processing permutation $\pi$ is adopted to encode a solution as Fig. 3, where $\pi_{i} \in$ $\{0,1, \ldots, n-1\}$ denotes the $i$ th task to be processed. As there is a virtual entry vertex and a virtual exit vertex, $\pi_{0}=0$ and $\pi_{n}=n-1$ is settled for the convenience of producing the permutations. Other tasks in DAG are ranked to generate the task processing permutation without violating the precedence constraints.

Table 1
Notations for the DAG-SP.

Fig. 3. Task processing permutation.

Definition 1 (Valid Permutation). For a permutation $\pi$, if there does not exist DAG precedence constraint between task pair ( $\pi_{j}$, $\pi_{i}$ ), $\forall i<j \in\{1, \ldots, n-1\}$, then $\pi$ is defined as a valid permutation of the certain DAG. As a consequence, when the tasks are scheduled according to this permutation, the schedule will satisfy the topological order of DAG. For DAG in Fig. 1, $\pi^{*}=$ $(0,2,1,3,4,8,7,5,6,9,11,10,13,12,14)$ is a valid permutation.

### 3.2. Decoding mechanism

Once a valid permutation $\pi$ is achieved, a feasible schedule can be obtained via decoding methods. In this work, four existing list scheduling methods, i.e., EFT, HEFT, OCT+EFT(OEFT) and OCT+HEFT(OHEFT) are used to form an efficient decoding mechanism. Firstly, these four decoding methods are illustrated respectively as Figs. 4-7 with $\pi^{*}=\{0,2,1,3,4,8,7,5,6,9,11,10$, $13,12,14$ ), where two processors are considered and the speed values are 1 and 1.25 .

EFT Tasks are assigned to the end of each processor to achieve to the earliest finish time. For task $j$, its processor is chosen as (11), where $F T(j, i)$ denotes the finish time of task $j$ on processor $i$ as (10). $\operatorname{EST}(j)$ denotes the earliest starting time of task $j$ as (9) shows, where $m_{k}$ denotes the processor assignment of task $k$ and $C_{i}$ denotes completion time of processor $i . \operatorname{EFT}(\pi)$ denotes the schedule decoded by EFT based on $\pi$.
$\operatorname{EST}(j)=\max _{k \in \operatorname{grad} j}\left(C_{j}+\frac{D(k, j)}{B\left(i, m_{k}\right)}\right)$
$F T(j, i)=\max \left\{\operatorname{EST}(j), C_{i}\right\}+\frac{w_{j}}{v_{i}}$
$m_{j}=\operatorname{argmin}_{i}\langle F T(j, i)\rangle$
HEFT: According to HEFT, tasks are assigned to any available idle time slot and the last period of processor $i$ defined as $\left(C_{i},+\infty\right\rangle$. For task $j$ and processor $i$, its available idle time slot set avidle contains idle periods satisfying (12), where $S T_{k}$ and $C T_{k}$ denotes the starting and ending time of the $k$ th idle. In this way, finish time of task $j$ on processor $i$ is calculated as (13) and the processor with minimum finish time is selected according to (14). $\operatorname{HEFT}(\pi)$ denotes the schedule decoded by HEFT based on $\pi$.
$\max \left(\operatorname{EST}(j), S T_{k}\right)+\frac{w_{j}}{v_{i}}<C T_{k}$
$H F T(j, i)=\min _{k \in \operatorname{avidle}}\left\{\max \left(\operatorname{EST}(j), S T_{k}\right)+\frac{w_{j}}{v_{i}}\right\}$
$m_{j}=\operatorname{argmin}(H F T(j, i))$
Compared to EFT, insert-based policy is adopted in HEFT. Suppose $S$ represents a schedule, we define $\boldsymbol{I}(\boldsymbol{S})$ as the set of tasks inserted forward into idle periods during HEFT decoding procedure. For each inserted task, define its following task as the first task after the idle period in the scheduling solution. In Fig. 8, $I\left(\operatorname{HEFT}\left(\pi^{*}\right)\right)=\{5,6,9,10\}$ and their following task are task 7 . Obviously, when $S=\operatorname{EFT}(\pi), S^{\prime}=\operatorname{HEFT}(\pi)$, if $\left(\left(S^{\prime}\right)=\varnothing\right.$, then all the tasks are assigned to the end of processors during the decoding procedure and for all $i$ and $j, H F T(j, i)=F T(j, i)$. Then, $S=S^{\prime}$ and $C_{\max }\left(S^{\prime}\right)=C_{\max }\left(S^{\prime}\right)$.

OEFT: OCT values [15] can be calculated iteratively as (15) shows. The processor assignment is determined as (16) shows, where $F T(j, i)$ can be calculated by (9)-(10).

$\operatorname{OEFT}(\pi)$ denotes the schedule decoded by OCT method with EFT policy based on $\pi$.

$$
\begin{aligned}
O C T(j, i) & =\max _{k \in \operatorname{OnC}(j)} \min _{i}\left\{\operatorname{OCT}(k, l)+\frac{w_{S}}{v_{i}}+\frac{D(j, k)}{B(i, l)}\right\} \\
m_{j} & =\operatorname{argmin}_{i}\langle F T(j, i)+\operatorname{OCT}(j, i)\rangle
\end{aligned}
$$

OHEFT: The processor selection is determined as (17) shows, where $H F T(j, i)$ can be calculated by (12)-(13). OHEFT $(\pi)$ denotes the schedule decoded by OCT method using HEFT policy based on $\pi$.
$m_{j}=\operatorname{argmin}(H F T(j, i)+O C T(j, i))$
It can be seen, for the same permutation, different decoding mechanisms lead to different schedules. HEFT and OHEFT are more efficient for the mentioned permutation because of its insert-based policy.

### 3.3. Hybrid decoding mechanism

Based on the above decoding methods, it can be seen that, the idle periods are shorten or removed by the insert-based policy. It is possible to decrease makespan through the insert-based policy. However, it is time consuming to traverse the idle periods when assigning each task. The efficient schedule produced by HEFT cannot be presented in the task processing permutations, which leads to the difficulty for our EDA in learning the effective structure of permutations.

Thus, to take advantage the high quality of HEFT schedule solution and low complexity of EFT, it is efficient adopting EFT to achieve same scheduling solution as HEFT, i.e., $\pi^{*}=\mathrm{EFT}^{-1}$ $(\operatorname{HEFT}(\pi))$ where the schedule solution encoded by EFT based on $\pi^{*}$ is the same with $\operatorname{HEFT}(\pi)$. $\operatorname{HEFTZEFT}(\pi)$ is designed to achieve the objective, which includes two methods: transfer $(\pi)$ is designed to achieve $\pi^{*}$ in permutation space and produce $(S)$ is

![img-6.jpeg](img-6.jpeg)

Fig. 4. Gantt graph of $\operatorname{EFT}\left(\pi^{+}\right), C_{\text {max }}=39.4$.
![img-5.jpeg](img-5.jpeg)

Fig. 5. Gantt graph of $\operatorname{HEFT}\left(\pi^{+}\right), C_{\text {max }}=29.4$.
![img-6.jpeg](img-6.jpeg)

Fig. 6. Gantt graph of $\operatorname{OEFT}\left(\pi^{+}\right), C_{\text {max }}=35.4$.
![img-5.jpeg](img-5.jpeg)

Fig. 7. Gantt graph of $\operatorname{OHEFT}\left(\pi^{+}\right), C_{\max }=31.4$.
![img-6.jpeg](img-6.jpeg)

I $I\left(\operatorname{HEFT}\left(\pi^{+}\right)\right)=[5,6,9,10], 7$ is immediate behind 10
Fig. 8. Illustration of $I(S)$.

![img-7.jpeg](img-7.jpeg)

Fig. 9. Illustration of produce $(S)$.
used to achieve $\pi^{\prime}$ from the schedule solution. When $I(S) \neq \varnothing$, transfer $(\pi)$ is adopted which transfers the permutation through swapping and moving tasks in $I(S)$ forward. The detailed pseudo code is presented as Method 1.

## Method 1: transfer $(\pi)$

Input: task permutation $\pi, S=\operatorname{HEFT}(\pi)$
For each task $\pi_{i}$ in $I(S)$ and its following task $\pi_{n}$ :
Insert $\pi_{i}$ between $\pi_{n}$ and $\pi_{n-1}$ to achieve $\pi^{\prime}$
If $\pi^{\prime}$ is valid:
If $C_{\max }\left(\operatorname{EFT}\left(\pi^{\prime}\right)\right)=C_{\max }(\operatorname{HEFT}(\pi))$ :
Return FALSE;
Else if $C_{\max }\left(\operatorname{EFT}\left(\pi^{\prime}\right)\right)=C_{\max }(\operatorname{HEFT}(\pi))$ :
Return TRUE, $\pi^{\prime}$;
Else
$S=\operatorname{HEFT}\left(\pi^{\prime}\right)$;
Update $I(S)$;
$\operatorname{transfer}\left(\pi^{\prime}\right)$;
End If
Else
Return FALSE;
End For
Output: $\pi^{\prime}$, if makespan of $\operatorname{EFT}(\pi)$ is not worse than $\operatorname{HEFT}(\pi)$
If transfer $(\pi)$ returns FALSE, produce $(S)$ is used to produce $\pi^{\prime}$ from the scheduling solution as Fig. 9 shows. For $S$, the task lists on each processor is recorded as $\operatorname{Tlist}(S)$, where $\operatorname{Tlist}(S)[i][r]$ represents the $r$-th task on the $i$ th processor of $S$. As produce $(S)$ is a mapping from $S$ to $\pi^{\prime}$, available task set $\mathbf{A}$ is defined as the tasks can be used to generate $\pi$. For example, $\mathbf{A}=\{1,2\}$ at the beginning of the procedure. If 2 is determined as the first element of $\pi^{\prime}$, then $\mathbf{A}=\{1,5\}$ as task 5 is the task scheduled next to task 2. The detailed pseudo code is listed as Method 2.

## Method 2: produce( $\boldsymbol{S}$ )

Input: $S, \mathbf{A}=\{0\}$ : available task set, $S^{\prime}$ : empty scheduling solution;
For the $i$-th valid task $j$ in $\mathbf{A}$ :
//valid task: its parent tasks have been scheduled;
Assign $j$ to processor $m_{j}$ by EFT in $S^{\prime}$;
If start time and end time of $j$ in $S^{\prime}$ are the same with $S$;
Append $j$ to the end of $\pi^{\prime}$;
Add the task assignment to $S^{\prime}$ and remove $j$ from $\mathbf{A}$;
Add the next task in $\operatorname{Tlist}\left[m_{j}\right]$ to $\mathbf{A}$;
$i=1$
End If
End For
If the length of $\pi^{\prime}$ is less than $n$ :
Return FALSE;
Else
Return TRUE;
End

HEFT2EFT is presented as Method 3, which is consisting of Method 1 and 2. During the local intensification, the individuals labelled 0 is decoded with EFT and ones labelled 1 is decoded with HEFT. The whole hybrid decoding mechanism consisting four heuristic-based decoding methods is listed as Procedure 1.

```
Method 3: HEFT2EFT(\pi, S)
Input: \(\pi, S=\operatorname{HEFT}(\pi), I(S)\)
If \(I(S)\) is empty:
    Label \(=0\);
    Return \(\pi^{\prime}=\pi\);
Else if transfer \((\pi)\) is TRUE:
    Label \(=0\);
    Return \(\pi^{\prime}\);
Else
    If produce \((S)\) is TRUE:
        Label \(=0\);
        Return \(\pi^{\prime}\);
    Else
        Label \(=1\);
    End If
End If
```

Procedure 1: Hybrid decoding mechanism $(\pi)$
Input: $\pi$
Result $=\left\{C_{\text {end }}\left(\operatorname{EFT}(\pi)\right), C_{\text {max }}\left(\operatorname{HEFT}(\pi)\right), C_{\text {min }}\left(\operatorname{OEFT}(\pi)\right), C_{\text {max }}\left(\operatorname{OHEFT}(\pi)\right)\right\}$
If Result[0] is the best:
Label $=0$;
Return $\pi$;
Else if Result[1] is the best:
HEFT2EFT $(\pi, \operatorname{HEFT}(\pi))$
Else if Result[2] is the best:
Label $=2$;
Return $\pi$;
Else:
Label $=3$;
Return $\pi$;
End If

## 4. The proposed algorithm

### 4.1. EDA for task processing sequence production

EDA builds a probability model to simulate the distribution of solution space, where its sampling and updating method are used to learn, evaluate and update the possibility model from the structure of elite individuals. Standard EDA procedure can be summarized as follows: Firstly, probability model $P$ is built. A population is generated by sampling $P$ and then $P$ is updated in accordance to the elite individuals selected from the population. Then, a new population is generated by sampling the updated $P$ until the stopping criterion is met.

## Probability model and its initialization

A problem knowledge driven probability model is designed which adopts the information of the problem and existing heuristic solutions. Since there exist precedence constraints between the tasks, a relative position probability is designed as (18) to produce task processing permutation, where $p_{i, j}(g)$ represents the probability that task $i$ is placed in front of task $j$ in the permutation at the $g$-th generation. Clearly, $p_{i, j}(g) \mapsto p_{j, i}(g)=1$. When $i=j, p_{i, j}(g)$ is set as 1.
$P(g)=\left\{p_{\mathrm{k}, j}(g)\right\}_{\mathrm{R}=\mathrm{R}}$

The probability model is initialized according to the following rule. If task $i$ is precedent of task $j, p_{i, j}=1$, else 0 as (19).
$p_{i, j}(0)=\left\{\begin{array}{l}1, i \rightarrow j \\ 0, j \rightarrow i\end{array}\right.$
For task pairs $(i, j)$ without precedent constraints, the probability value is initialized with the best existing list scheduling permutation. An indicative function (20) is used to represent the structure of a good solution and the probability is initialized as (21) where $\alpha \in(0,1)$ denotes the learning rate.
$l_{i, j}=\left\{\begin{array}{l}1, \text { task } i \text { is before task } j \text { in the best heuristic list } \\ -1, \text { otherwise }\end{array}\right.$
$p_{i, j}(0)=0.5+\alpha \times l_{i, j}$, there is no precedent constraint between $i$ and $j$

## Sampling and updating method

A sampling method is designed for the relative position probability model to produce individuals. The pseudo code is given as follows. For each position not determined in the permutation, a probability array is created which denotes the probabilities that tasks in available set should be assigned to the position. $s p(t)$ denotes the probability vector of task $t$ is set in front of all other available tasks. Then the array is normalized and sampled the next element of the permutation by the roulette wheel method. In addition, after a certain task is determined in the permutation, its child tasks are checked to update the available task set. If the parent tasks of a certain task have been determined in the processing permutation, then it is defined as an available task and pushed into the available task set. In this way, the permutations produced by EDA probability model can be guaranteed to be valid and schedules decoded from permutations by EDA satisfy the topological order of the DAG.

```
Method 4: EDA sampling
Input: A is a task set, A=\{0\}, P(g), k=0.
While A is not empty:
For each task \(t\) in \(A\)
    \(\operatorname{sp}(t):=\prod_{i \in A} p_{i, j}(g)\);
    End For
    Normalize probability array sp;
    \(\pi_{t}=\) RouletteWheel(sp)
    Check child tasks of \(\pi_{t}\), and if its parent tasks are determined in \(\pi\), push it into A;
    \(\mathrm{g}_{k=1}\);
End While
Output: \(\pi\)
```

After sampling $P$, all the individuals are sorted according the increasing order of makespan. The first $Q=N \times \eta \%$ individuals are considered as the elite population, where $N$ denotes the size of population and $\eta \%$ is the elite population proportion. The updating scheme is set as (22) and (23). For each elite individual, the permutation structure is recorded as $I_{i, j}^{k}(g)(k=1, \ldots, Q)$ as (23). Through this indicator, the frequency of a certain task pair is calculated and used to update the probability value based on population based incremental learning method (PBIL) [39].
$p_{i, j}(g+1)=(1-\alpha) \times p_{i, j}(g)+\alpha \times \sum_{k} I_{i, j}^{k}(g) / Q$
$I_{i, j}^{k}(g)=\left\{\begin{array}{l}1, \text { task } i \text { is before task } j \text { in the } k \text { th individual of the } \\ g \text { th generation } \\ 0, \text { otherwise }\end{array}\right.$

### 4.2. Path relinking enhanced local intensification

Path relinking is one of methods to explore the path between elite solutions, which aims at sharing the promising permutation structure [40]. Three essential elements: rules for building reference set, initial and guiding solutions and a neighbourhood structure for moving along the path, are necessary for path relinking procedure. Based on the neighbourhood structure, a path is built from the initial solution to the guiding solution based on neighbourhood structure. In this way, a set of temporary solutions are produced, and it is possible to achieve better solutions within the temporary solutions.

To take advantage of the knowledge of existing DAG-SP research works, solutions produced by EDA are chosen as the corresponding starting solution to learn from the guiding solution, which is set as the best heuristic solution or existing best solution till now. Path relinking insert and swap operators are defined and set as the neighbourhood structures. The whole procedure is illustrated as Fig. 10 where for all the elite solutions produced by EDA, "path relinking insert" operator is adopted to build the path and generate temporary solutions, and for the best solution of the current population, "path relinking swap" operator is adopted. In this section, these two neighbourhood structures as well as a corresponding property is presented at first. Then, the detailed pseudo code of the path relinking enhanced local intensification is introduced.

Definition 2 (Path Relinking Insert), $\boldsymbol{\pi}_{r s}^{\mathbf{1}}$ is defined as a set of temporary permutations generated from $\pi_{r}$ to $\pi_{s}$ by "path relinking insert" operator. For starting permutation $\pi_{r}$ and guiding permutation $\pi_{s}$, each element of permutations $\pi_{r}$ and $\pi_{s}$ is compared and if $\pi_{s, i} \neq \pi_{r, i}, \pi_{r}$ is traversed to locate $\pi_{s, i}$, and is inserted to the $i$ th position of $\pi_{r}$, as method 5: PRInsert $\left(\pi_{r}, \pi_{s}\right)$ and Fig. 11(a) present. In this way, a temporary permutation is generated and added to $\boldsymbol{\pi}_{r s}^{\mathbf{1}}$. The whole procedure is defined as "path relinking insert". Obviously, $\left|\boldsymbol{\pi}_{\boldsymbol{r}_{\boldsymbol{r}}}^{\mathbf{1}}\right| \leq n$ and when $\pi_{r}$ and $\pi_{s}$ are completely reversed, the equality holds.

```
Method 5: PRInsert \(\left(\pi_{r}, \pi_{s}\right)\)
Input: Starting permutation \(\pi_{r}\), guiding permutation \(\pi_{r}, \boldsymbol{I}_{\boldsymbol{r} s}^{\mathbf{1}}=\{ \}\)
For \(i=1\) to \(n\)
If \(\pi_{r, i} \neq \pi_{r, i}\)
    \(\pi^{i}=\pi_{r}\)
    For \(j=i\) to \(n+1\)
        If \(\pi_{r, j}=\pi_{s, j}\)
            \(\pi^{i},=\pi_{s, j}\)
            For \(k=i+1\) to \(j\)
            \(\pi^{i}{ }_{k}=\pi_{r, k-1}\)
            End For
            Add \(\pi^{i}\) into \(\Pi^{k}{ }_{r s}\)
            Break
        End if
        End For
End If
\(j++\)
End For
Output: \(\Pi_{r s}^{k}\)
```

Definition 3 (Path Relinking Swap), $\boldsymbol{\pi}_{\boldsymbol{r} \boldsymbol{s}}^{\mathbf{S}}$ is defined as a set of temporary permutations generated from $\pi_{r}$ to $\pi_{s}$ by "path relinking swap" operator. For starting permutation $\pi_{r}$ and guiding permutation $\pi_{s}$, each element of permutations $\pi_{r}$ and $\pi_{s}$ is compared and if $\pi_{s, i} \neq \pi_{r, i}, \pi_{r}$ is traversed to locate $\pi_{s, i}$, and then swap it with its prior element. In this way, a temporary permutation is generated and added to $\boldsymbol{\pi}_{\boldsymbol{r} \boldsymbol{s}}^{\mathbf{S}}$ until $\pi_{s, i}$ is moved to the $i$ th position

![img-8.jpeg](img-8.jpeg)

Fig. 10. Illustration of path relinking enhanced local intensification.
of $\pi_{r}$, as method 6: $\operatorname{PRSwap}\left(\pi_{r}, \pi_{s}\right)$ and Fig. 11(b) present. The whole procedure is defined as "path relinking swap". Obviously, $\left|\pi_{r_{r}}^{\mathbf{s}}\right|_{\mathbf{r s}}^{k}(\leq n(n+1) / 2$ and when $\pi_{r}$ and $\pi_{s}$ are completely reversed, the equality holds.

Method 6: PRSwap $\left(\pi_{r}, \pi_{s}\right)$
Input: Starting permutation $\pi_{r}$, guiding permutation $\pi_{s}, \boldsymbol{I}_{r}^{\mathbf{s}}{ }_{\mathbf{r s}}=\{ \}$
For $i=1$ to $n$
If $\pi_{r, i} \neq \pi_{r, i}$
$\pi^{\prime}=\pi_{r}$
For $j=i+1$ to $n$
If $\pi_{r, j}=\pi_{s, i}$
For $k=j$ to $i$
$\pi^{\prime}{ }_{k}=\pi_{r, k-1}$
$\pi^{\prime}{ }_{k-1}=\pi_{r, k}$
Add $\pi^{\prime}$ into $I_{r}^{\mathbf{s}}{ }_{r s}$
End For
break
End If
End For
End If
$j=\mathrm{s}$
End For
Output: $I_{r}^{\mathbf{s}}{ }_{r s}$

Property 1. If $\pi_{r}$ and $\pi_{s}$ are valid permutations, permutations in the defined sets: $\pi_{r_{r}}^{\mathbf{i}}{ }_{\mathbf{r s}}$ and $\pi_{\mathbf{r s}}^{\mathbf{s}}{ }_{\mathbf{r s}}$, are valid.

Proof. These permutations into three sets as Fig. 11 shows, where $\phi_{1}$ is the beginning set of same elements, which is green-coloured in Fig. 11. $\pi_{r, 1}$ and $\pi_{s, i}$ are the first different element of these two permutations and if $\pi_{r, j}=\pi_{r, h}$, then $\phi_{2}$ includes the $i$ th to the $(i+k)$-th elements of these permutations, which is yellow coloured in Fig. 11. At last, $\phi_{3}$ is consist of the rest elements, which is pink coloured.

As guiding permutation $\pi_{s}$ is valid, we have $\operatorname{prec}\left(\pi_{s, i}\right) \subseteq \phi_{1}$, and for starting permutation $\pi_{r}$, as the elements $\phi_{1}$ are the same, we have $\forall \beta \in \phi_{3}, \beta \notin \operatorname{prec}\left(\pi_{s, i}\right)$. Thus, inserting $\pi_{r, i+k}=\pi_{s, i}$ to the position between $\phi_{1}$ and $\phi_{2}$ will not violate the precedence constraints in DAG. For $\phi_{3}$, the topological order between $\phi_{1} \cup \phi_{2}$

Guiding solution $\pi_{g}: \phi_{1}$


Starting solution $\pi_{r}$ :

Temporary solution
(a)

Guiding solution $\pi_{g}: \quad \phi_{1}$


Starting solution $\pi_{r}$ :
![img-9.jpeg](img-9.jpeg)
(b)

Fig. 11. Illustration of path relinking neighbourhood structures (a) Path relinking insert; (b) Path relinking swap.
and $\phi_{3}$ does not be altered. In this way, it can be proved that permutations in $\pi_{\mathrm{rs}}^{1}$ are valid. The case of swap operator can be proved similarly.

Based on this property, all the permutations produced by path relinking insert and swap can be proved valid. Thus, there is

no need to check if the permutation is valid during the local intensification. The details of local intensification is introduced in Procedure 2 and detailed path relinking method is illustrated in Method 5, where $X=\{\mathrm{EFT}, \mathrm{HEFT}, \mathrm{OEFT}, \mathrm{OHEFT}\}$ denotes the selected decoding method by the above hybrid decoding mechanism. To improve the performance of elite solutions, insert operator is carried on elite individuals at first, and the individuals are updated with better solutions. Then, the path relinking swap operator is adopted for the best individual.

```
Method 7: pathrelinking \((Y, \pi_{i}, L)\)
Input: Path relinking operator \(Y\), guiding solution \(\pi_{i}\) and elite individual \(L\)
\(\pi_{i}:=L\).permutation; \(I:=L\);
Produce \(\Pi^{2}{ }_{\pi_{i}}\) based on Method 5 or 6
For each \(\pi\) in \(\left\langle\Pi^{2}{ }_{\pi}\right\rangle \mid \pi_{i}\) :
Choose decoding method \(X\) for \(\pi\) according to label of \(L\);
    If \(X(\pi)<L\).makespan
        1.permutation \(=\pi\)
        1.makespan \(=X(\pi)\)
    End If
End For
If 1.makespan < L.makespan
    Return \(I\);
Else
    Return null;
End If
Output: better solution \(I\)
```

```
Procedure 2: Local Intensification
Input: bledi := best individual till now;
    gblndi := elite individuals in this generation of population;
\(\pi_{i}:=\) bledi. permutation;
For each \(L\) in gblndi:
    \(I:=\) pathrelinking(Insert, \(\pi_{i}, L\) )
    If \(I!=\) null
        Replace \(L\) with \(I\);
    End If
End For
Update gblndi, bledi, \(\pi_{i}\)
\(I:=\) pathrelinking(Swap, \(\pi_{i}\), glndi[0])
If \(I!=\) null
        Replace gblndi with \(I\);
End If
```


### 4.3. Flowchart and complexity analysis

Based on above introduction, our proposed algorithm is summarized in Fig. 12. At first, HEFT and PEFT heuristics are carried out where the best one is chosen to initialize the probability model. After that, EDA is adopted to produce the task processing permutation as the right of Fig. 12. Please refer to the corresponding pseudo codes for the details of the related procedures.

According to the flowchart, the time complexity of our proposed algorithm is analysed as follows:

Hybrid decoding mechanism: transfer $(\pi)$ has an $O\left(n^{2}\right)$ complexity and the complexity of produce $(S)$ is the same as HEFT, where HEFT has an $O\left(n^{2} \cdot m\right)$ complexity. It could be summarized that hybrid decoding mechanism complexity is of $O\left(n^{2} \cdot m\right)$;

EDA evolution: EDA sampling has an $O\left(n^{3}\right)$ complexity and other operator complexity is $O\left(n^{2}\right)$;

Local intensification: Path relinking insert operator is carried on elite population, and its complexity turns to $O\left(n^{3} \cdot m \cdot Q\right)$. Path relinking swap operator is carried on the best individual, and the complexity is $O\left(n^{4} \cdot m\right)$. It is worth mentioned that if the
individual is labelled as 0 or 2 , EFT or OEFT is adopted to decode the permutation, its complexity decreases to $O\left(n^{2} \cdot m \cdot Q\right)$ and $O\left(n^{3} \cdot m\right)$.

Thus, the complexity of the proposed algorithm is $O\left(\left(N \cdot n^{3} \cdot\right.\right.$ $\left.m+n^{3} \cdot m \cdot Q+n^{4} \cdot m\right) G$ ) where $G$ denotes the number of iteration. Considering $N<n$, the total algorithm complexity is of the order $O\left(n^{4} \cdot m \cdot G\right)$.

## 5. Simulation

To evaluate the performance of our proposed algorithm, we compare it with several algorithms: two list scheduling heuristic methods and two evolutionary algorithms tailored for DAG-SP.

For fair comparison, the algorithms are all coded in C++ and run on the same computer with Intel Core i5 CPU/3.20 GHz and 16 GB RAM. For the evolutionary algorithms, the stopping criterions are set the same. In this section, the benchmark datasets, comparison algorithms and parameter settings are introduced at first. Then, the comparison with solutions of Gurobi solver are presented to review our proposed model. In addition, comparison results on randomly generated DAGs and real world instances with different scales of tasks, processors and different values of CCRs demonstrate the effectiveness of the proposed algorithm.

### 5.1. Benchmark datasets, comparison algorithms and parameter settings

Two benchmark datasets are adopted in this paper: A commonly used DAG dataset [41] (http://www.kasahara.elec.waseda. ac.jp/schedule/) and DAG applications from real world. To supplement the communication data information of [41], new datasets are produced in accordance to different CCR values. Data communication size is produced following normal distribution with the average value of a certain $C C R$ according to (1). In addition, the settings of $\{n, m, C C R\}$ can be referred to Table 2. For each combination of $\{n, m, C C R\}, 60$ independent cases are produced.

In addition, DAG applications from real world problems are carried out as the test instances: Gauss elimination algorithm (GE) [42] and Fast Fourier Transformation (FFT) [43] and scientific workflows [44]. The general structures of these DAGs are presented as Figs. 13 and 14.

The detailed datasets can be referred in https://www.research gate.net/publication/352697650_DAG-benchmark.

For the comparison algorithms, HEFT [18], PEFT [15], GA[23] and PSO[29] are selected as. HEFT is considered as the best DAG-SP list scheduling heuristic in terms of robustness and performance compared with around 20 heuristic methods [45]. In this simulation test, the minimum makespan among HEFT-t-level, HEFT-b-level and HEFT-tb-level is adopted as its result. Compared to HEFT, PEFT considers the impact of task assignment on its children nodes. Besides, GA is an efficient evolutionary algorithm designed for solving DAG-SP, which adopts existing heuristic permutations to initialize the population. Similar with GA, PSO is also an evolutionary algorithm tailored for DAG-SP, which considers more than one objectives simultaneously.

During the simulation, two parameters of our proposed EDA: population size $(N)$ and learning rate $(\alpha)$ are set as the parameters in the simulation experiments based on our previous works [35]. The population size and stopping criterion are set the same for EDA, GA and PSO. The detailed settings are listed as follows.

### 5.2. Comparison to Gurobi on small scale instances

To review the MILP model presented in Section 2.3 and evaluate the performance of our proposed algorithm on solving smallscale problems, math solver Gurobi (Version 9.0.0) is adopted to

![img-10.jpeg](img-10.jpeg)

Fig. 12. Flow chart of the proposed algorithm.
![img-11.jpeg](img-11.jpeg)

Fig. 13. DAGs from real world applications (a) Gauss elimination algorithm; (b) Fast Fourier transformation.
![img-12.jpeg](img-12.jpeg)

Fig. 14. DAGs from scientific workflows [44] (a) CyberShake workflow; (b) LIGO workflow.
solve the MILP model and construct an accurate algorithm on DAG-SP. Small-scale DAGs of GE with $n=14, C C R=(0.1,0.5,1.0$, 5.0) and $m=[2,4,8]$ are produced for the comparison.

For each instance, the proposed EDA is run 20 times independently and the best, average (Avg.) and deviation values (Std.) of EDA solutions are recorded and compared with the solutions

Table 2
Simulation settings.

Table 3
Comparative results with model on small scale instance.
${ }^{\text {a }} 2.50$ GHz Inter Core i5 CPU.
${ }^{\mathrm{b}} 3.50$ GHz Inter Core i5 CPU.

Table 4
Pair-wise comparison to different decoding mechanism/EDA without local search method.

and low bounds (LB) of Gurobi. Considering the problem scales, the time limit of solving the model is set as 3600 s . In addition, the CPU time of each algorithm is recorded where the average CPU time $(\overline{\mathbf{C P U}(\mathbf{s})})$ of 20 independent runs for each instance is presented for EDA.

It can be seen from Table 3 that for the small scale instances $(m<8)$, our proposed EDA achieves the Gurobi solutions within a relative short time period under most situations. When $m=8$, the scale of decision variables doubles and our solutions performs better than the Gurobi solutions produced within 3600 s time limit.

### 5.3. Effectiveness of hybrid decoding mechanism and local intensification

To verify the efficiency of our hybrid decoding mechanism, we use EFT, HEFT, OEFT and OHEFT as the decoding method to compare with our proposed algorithm. In addition, a naïve GA is implemented as a baseline to verify the efficiency of the scheme of EDA, where its population is initialized randomly and crossover and mutation operators are adopted for the evolution of the algorithm. The individuals of GA are encoded with task processing permutations and decoded by HEFT. Pair-wise comparison results are listed in Table 4 , where "EDA-X" denotes the EDA embedded with single decoding mechanism "X". In addition, "EDA-noLS" denotes simple EDA with hybrid decoding mechanism without
local intensification. 960 independent cases are randomly chosen as the test cases. Table 4 illustrates the percentage of cases where EDA and naïve GA are "worse" than, "equal" to, "better" than the corresponding comparison algorithm.

It can be seen from Table 4 that EDA-OHEFT performs well, which means that it is successful to take PEFT as a decoding method. In addition, compared to single OHEFT, hybrid decoding mechanism performs better on over $65 \%$ instances and for other single decoding methods, the superiority of our mechanism is much more obvious. The comparison between EDA-noLS and our proposed EDA shows that the local intensification improves its performance.

In addition, the comparison results between "EDA-HEFT" and "EDA-noLS" and naïve GA show that, the EDA scheme and the hybrid decoding mechanism are efficient in solving DAG-SP.

### 5.4. Comparisons to existing algorithms

Firstly, we compare our algorithm with list scheduling heuristics: HEFT [15] and PEFT [12], and evolutionary algorithms: GA [20] and PSO [25] based on datasets [41]. The average values of are listed according to $n, m$ and $C C R$ in Table 5 . Paired T-test is carried out to verify the significant superiority of our algorithm. For each scale groups of comparative results, the alternative hypothesis is set as "the makespan of EDA solution is less than

![img-13.jpeg](img-13.jpeg)
(a)
![img-14.jpeg](img-14.jpeg)
(b)
![img-15.jpeg](img-15.jpeg)
(c)

Fig. 15. Makespan plots of Gaussian elimination application. (a). "makespan-n" plot; "makespan -CCR" histogram (c) "makespan-m" histogram.

Table 5
Comparative results sorted by different parameters.
Note: The bold values mean the best results.
the other one under $95 \%$ confidence level" and Sig='Y' denotes that the alternative hypothesis is accepted.

From Table 5, it can be seen that the average makespan of EDA performs the best significantly. In addition, it can be seen that when $C C R=0.1$ and 0.5 , difference between EDA and other algorithms, especially GA, is small. The possible reason is that relatively small $C C R$ leads to less idle periods in scheduling solutions, and thus there is not much space left for optimization. As CCR increases, it can be seen that our superiority of EDA turns larger. The possible reason is that data transfer size increases, poor permutations and decoding method lead to a large amount of idle periods. Our hybrid decoding mechanism and local search method improve the solutions by altering the task processing sequence and choosing appropriate decoding method.

Table 6
Pair-wise comparison to existing algorithms.
In addition, it can be seen that EDA performs better when the processor number increases. Similar with a larger CCR, larger amount of processors increase the difficulty of searching for the best solution. As the encoding sequence of PSO is the processor assignment sequence, when processor number increases, the possibility of processor assignment increases, and it turns to be difficult to search for a good task-processor mapping sequence.

Table 6 illustrates the percentage of cases in which the performance of proposed EDA is "worse" than, "equal" to, "better" than the corresponding comparison algorithm respectively.

From Table 6, it is obvious that our EDA performs better than these comparison algorithms. Compared to the GA, EDA refreshes $82 \%$ of its solutions. Similar with GA, knowledge from existing list scheduling heuristics is applied in the evolution and it improves the performance of the proposed algorithm significantly.

Considering the real-world applications: GE and FFT, 10 different scales of DAGs of Gauss Elimination application ( $b=20-29$ ) are produced. For each scale of DAG, $C C R=\{0.1,0.5,1.0,5.0\}$ and $m=\{2,4,8,16\}$ are used to generate $10 \times 4 \times 4=160$ different instances. The average makespan value sorted according to $n, m$ and $C C R$ are shown in Fig. 15.

For these 160 instances, EDA overcomes $95.63 \%$ solutions produced by GA and $100 \%$ solutions from other three algorithms.

Table 7
Comparative results on GE DAGs.

![img-16.jpeg](img-16.jpeg)

Fig. 16. "makespan $-n$ " histogram of FFT application.

From Fig. 15(a), it can be seen that as the scale of DAG increases, EDA performs the best on average value of makespan.

Specially, for the cases of $n=434,20$ independent executions are run for each case and the relative percent deviation (RPD) is calculated as (24):
$R P D^{\text {sig }}=\frac{C_{\text {max }}{ }^{\text {sig }}-C_{\text {max }}{ }^{\text {best }}}{C_{\text {max }}{ }^{\text {best }}} \times 100$
The best, average RPD values and deviation of solutions are recorded as Table 7 and for each case, a two sample T-test is carried out and Sig='Y' denotes that our solutions are better than the others under $95 \%$ confidence level. From Table 7, it can be seen that our proposed algorithm perform better than other two algorithms significantly.

For FFT, $4 \times 4 \times 4=64$ cases are produced respectively. The average value of makespan sorted by $n$ is presented in Fig. 16 where it can be seen that, except for $n=40$, EDA performs the best. The results show that it is necessary to increase the capacity of local intensification in EDA to search for optimal solutions when the problem scale is not large.

Specially, for the cases of $n=512,20$ independent executions are run for each case and RPD is calculated are listed in Table 8. From Table 8, it can be seen that our proposed algorithm performs better when CCR and $m$ are relatively larger.

The results of comparison tests on instances from scientific workflows: Cybershake and LIGO, are listed as follows. For each instance, the problem scale, computation and communication data are determined, and different scales of processors ( $m=$ $\{2,4,8,16\}$ ) are carried out to test the proposed algorithm. The

RPD values are listed as Table 9 and it can be seen that our proposed algorithm provides a better and robust performance compared to other algorithms. The file of detailed schedules can be downloaded from https://www.researchgate.net/publication/3 52697650_DAG-benchmark.

## 6. Conclusions

In this paper, a path relinking enhanced EDA is designed for DAG-SP. The simulation results based on extensive benchmark datasets with different scales of tasks, processors as well as CCRs show that the tailored hybrid decoding mechanism and path relinking based local intensification are effective to improve the performance of EDA. Moreover, our proposed algorithm is superior to existing algorithms in solving DAG-SP. The main contributions of this work in designing the optimization algorithm are summarized as follows.

1. A hybrid decoding mechanism based on existing list heuristics is developed to adjust the produced permutations during the EDA-based search. With such a mechanism, appropriate decoding method can be chosen according to the structure of permutation.
2. A relative position based probability model is designed to describe the probability distribution of solutions. In addition, the probability model is initialized according to the DAG structure and heuristic solutions. Via sampling such a model, diverse and promising task processing permutations can be produced.
3. Two search operators based on problem-specific path relinking scheme are designed, and a path relinking enhanced local intensification procedure is presented. With the local intensification procedure, exploitation ability is enhanced.

## 7. Managerial implication and future work

Efficient DAG task scheduling algorithm can uplift the performance of IoT, fog or cloud computing applications. Due to the wide application of cloud and fog computing in our daily life, such a solution has significant impact on the optimization of the quality of user experience [46,47]. In addition, appropriate task assignment solution gives rise to the resource balancing within multi-processors, multi-cores and multi virtual machines (VMs) within a single processor. Therefore, DAG task scheduling techniques such as our proposed algorithm can be well applied in the related areas.

For the large and distributed cloud computing environment, it is essential to cut down the extra time generated by scheduling overhead, which results in a shorter execution time of the entire

Table 8
Comparative results on FFT DAGs.

Table 9
Comparative results on scientific workflow instances.
process. Efficient DAG task scheduling algorithm plays an important part in distributed workflow task balancing [5], offering a good solution to the assignment of the tasks within the workflow to the processors.

Similarly, resource consumption cost optimization within many-core processor is important because of the limited resource and high computation load of embedded systems [6]. Efficient DAG task scheduling algorithm is adopted to handle the task precedence constraints during the task scheduling process. In addition, DAG task scheduling algorithm increases the utilization of VMs and brings forth resource balancing in multi-vCPU VMs [7].

In the future, we will study DAG-SP with different metrics and constraints by considering the uncertainty in computing system and applications. In addition, we will develop effective task scheduling algorithms by fusing the evolutionary computing and the problem-specific search knowledge. It is also interesting to apply the proposed algorithm for the real-world applications.

## CRediT authorship contribution statement

Chu-ge Wu: Data curation, Analysis, Methodology, Writing draft. Ling Wang: Conceptualization, Analysis, Methodology, Review, Funding acquisition. Jing-jing Wang: Conceptualization, Methodology, Funding acquisition.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This research is supported by the National Science Fund for Distinguished Young Scholars of China [No. 61525304], the National Natural Science Foundation of China [No. 61873328].
