# A scheduling algorithm for heterogeneous computing systems by edge cover queue 

Yu-meng Chen, Song-lin Liu, Yan-jun Chen, Xiang Ling*<br>National Key Laboratory of Science and Technology on Communications, University of Electronic Science and Technology of China, Chengdu, 611731, Sichuan, China

## A R T I C L E I N F O

Article history:
Received 13 December 2022
Received in revised form 2 February 2023
Accepted 3 February 2023
Available online 10 February 2023

Keywords:
Heterogeneous computing system
Edge cover queue
Estimation of distribution algorithm
Graph random walk algorithm

## A B S T R A C T

In heterogeneous computing systems, excellent task scheduling algorithms can shorten the task completion time and improve system parallelism. With the large-scale deployment of edge computing, the task scheduling algorithm in heterogeneous edge computing servers has become a critical factor in improving the overall system performance. This paper proposes a new task scheduling algorithm called the edge cover scheduling algorithm (ECSA), which schedules tasks based on the edge cover queue of the directed acyclic graph (DAG) for heterogeneous computing systems. Based on the estimation of distribution algorithm (EDA) and the graph random walk algorithm, the ECSA generates an edge cover queue from DAG. Then, the ECSA uses the heuristics greedy method with low time and computational complexity to allocate the edge cover queue to processors. Theoretical analysis and simulation results on random DAGs and real-world DAGs show that the ECSA can achieve better scheduling results in terms of makespan, the schedule length ratio (SLR), efficiency, and frequency of best results with low time and computational complexity.
(c) 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license
(http://creativecommons.org/licenses/by/4.0/).

## 1. Introduction

A heterogeneous computing system (HCS) refers to a group of interconnected processors with different computing and storage capabilities [1-3]. Due to the diversity of tasks and the difference in processor architecture, HCS widely exists in various computing scenarios [1-3]. Applications are usually modeled as DAGs for scheduling in practice. An efficient DAG task scheduling algorithm can improve the heterogeneous computing system's performance and user experience quality. With a suitable scheduling algorithm, an excellent computing system can fully exert its computing capability [4-7]. Because of the heterogeneity of the HCS, the priority constraints between tasks, and the NP-H characteristics of DAGs, it is challenging to achieve efficient scheduling [8].

The existing scheduling algorithms are divided into list scheduling algorithms and evolutionary algorithms [3]. List scheduling algorithms have low time and computational complexity, but the scheduling results are not ideal in many scenarios, and they easily fall into the local optimal solution [9,10]. Evolutionary algorithms are global optimization algorithms [11,12]. Due to high time and computational complexity, it can obtain excellent scheduling results only with sufficient computation [11,12].

The list scheduling algorithms have two phases: the prioritizing phase for giving priority to each task and the processor

[^0]selection phase for selecting a suitable processor that minimizes the heuristic greedy cost function [13,14]. The task scheduling queue is obtained by sorting the tasks according to the task priority weight. Early scheduling algorithms were designed for homogeneous computing systems, such as the earliest start time (EST) and earliest finish time (EFT) [1], which are the simplest greedy algorithms. To adapt to heterogeneous environments, two well-known heuristic methods, heterogeneous earliest finish time (HEFT) and critical path on a processor (CPOP), are proposed in [1]. In the HEFT algorithm, tasks are sorted by the length of the longest path from the task node to the bottom of the DAG. The task on top of the scheduling queue is greedily assigned to the processor, which allows for the earliest finish time. Furthermore, the HEFT algorithm uses an insertion policy that tries to insert a task in the earliest idle time between two already scheduled tasks on a processor if the slot is large enough to accommodate the task [1]. In the CPOP algorithm, the critical path of the DAG is calculated first, and then the critical path is allocated to the same processor that has the shortest completion time, and the other tasks are allocated in turn [1]. The predictive list scheduling algorithm performs scheduling by estimating the impact of task allocation on its subsequent tasks. The most famous predictive list scheduling algorithm, predict earliest finish time (PEFT), constructs an optimistic cost table (OCT) by listing the shortest path from its child node to the exit node for each combination of tasks and processors [2]. PEFT uses the average OCT value of each task to sort tasks from high to low. The task is


[^0]:    * Corresponding author.

    E-mail address: xiangling@uestc.edu.cn (X. Ling).

assigned to the processor with the shortest EFT+OCT or inserting the available idle time slot of the processor [2]. The lookahead scheduling algorithm (LO) is a special list scheduling algorithm. When scheduling, each task is assigned to the processor that has the shortest completion time for all its subtasks [10]. It has a good effect in medium-scale DAG scheduling, Gaussian elimination (GE) programs, and Fast Fourier Transform (FFT) programs, but it is also a type of list scheduling algorithm with the highest time and computational complexity [10].

Evolutionary algorithms are global optimization algorithms that can provide satisfactory solutions to complex problems [12], [15]. For the DAG scheduling problem (DAG-SP), evolutionary algorithms have been attempted, including the genetic algorithm (GA) [9], ant colony optimization (ACO) [16], moth search algorithm (MSA) [17], differential evolution (DE) [17], chemical reaction optimization (CRO) [18], and particle swarm optimization (PSO) [19], [20]. In addition to giving the task-processor scheduling scheme, the evolutionary algorithm for the priority of the scheduling queue also has research work. In the multiple priority queues genetic algorithm (MPQGA), an evolutionary algorithm is proposed to guide the iteration of the scheduling queue to solve DAG-SP [9]. After initialization, crossover and mutation operators evolve the scheduling queue. Better scheduling results can be obtained by obtaining a better scheduling queue [9]. However, the evolutionary algorithm's large number of iterations also limits its application scope.

In recent research, the scheduling algorithm collects and memorizes the information from the DAG-SP and further explores better scheduling within the acceptable time and computational complexity to achieve a better solution [21], [22]. For this point, the estimation of distribution algorithm (EDA) is suitable. The EDA establishes a probability model and extracts information in the iterative process to guide the algorithm to explore new scheduling solutions further [23]. To date, the EDA has performed well in combinatorial optimization problems, including scheduling problems [21], [22], [23], [24], [25], [26], [27]. However, the EDA has high time and computational complexity similar to the evolutionary algorithm.

In this paper, to improve the current DAG-SP scheduling results with less complexity and fewer iterations, we present a new task scheduling algorithm called ECSA. Unlike previous work using a vertex queue in the prioritizing phase and processor selection phase, the ECSA uses an edge cover queue for task scheduling. Furthermore, we propose a method using a simplified EDA and graph random walk algorithm to generate the edge cover queue. The tasks in an edge as a whole use the heuristic greedy cost function for processors' task assignments. Theoretical analysis and experimental results show that the ECSA can effectively improve the performance of task scheduling solutions and be closer to the optimal solution in fewer iterations and with low time complexity.

The major contributions of this paper are as follows:

1. This paper first proposes the idea of using an edge cover queue instead of a vertex queue for scheduling. In the scheduling process, the edge cover queue explores a hybrid scheduling strategy of vertex greed and edge greed.
2. Based on the EDA and the graph random walk algorithm, a method of generating an edge cover queue is designed. We adopted the strategy of a single population to simplify the EDA, avoiding the significant time and computational complexity of the EDA.

The content of this paper is organized as follows. Section 2 describes the relevant theoretical basis and preliminaries of the article. Section 3 introduces the relevant work. Section 4 introduces the proposed algorithm and analyzes its advantages. Section 5 introduces the experimental results and discusses them. Section 6 summarizes the article and introduces the content that can be expanded upon in the future.

## 2. Theoretical basis and preliminaries

In this section, we first introduce both the hardware and software DAG-SP system model and related definitions. Then, we introduce the EDA and graph random walk algorithm, which will be used later.

### 2.1. DAG-SP

DAG-SP means DAG scheduling problem. An application program can be modeled as a directed acyclic graph, $D A G=(V, E)$, where $V$ is the set of $v$ nodes and each node $n_{i} \in V$ represents an independent application task that must execute on the same processor. $E$ is the set of edges between tasks. Each $e_{i j} \in E$ represents the task-dependence constraint such that task $n_{i}$ can be started after task $n_{i}$ completes its computation. The DAG is complemented by a matrix $W$, which is a $v \times p$ computation cost matrix, where $v$ is the number of tasks and $p$ is the number of processors in the system. Each $\omega_{i j} \in W$ means the computation cost for task $n_{i}$ on processor $p_{j}$. A matrix $C$ consists of $c_{i j}$ called the communication cost matrix. $c_{i j}$ is the communication cost for the corresponding edge $e_{i j}$. Note that when tasks $n_{i}$ and $n_{j}$ are assigned to the same processor, the actual communication cost $c_{i j}$ can be considered to be zero because it is negligible compared with inter-processor communication costs.

In most models, processors connect in a fully connected topology [1], [2], [3]. Moreover, the execution of tasks and communications with other processors can be achieved for each processor without contention. Additionally, the execution of any task is considered non-preemptive. These models are standard in this scheduling problem because these simplifications correspond to natural systems [2].

Then, some terms related to DAG are introduced to characterize the topology of DAG. $\operatorname{pred}\left(n_{i}\right)$ refers to the set of immediate predecessors of task $n_{i} . \operatorname{succ}\left(n_{i}\right)$ refers to the set of immediate successors of task $n_{i} . n_{\text {entry }}$ is a task with no immediate predecessors. If a DAG has more than one $n_{\text {entry }}$, a dummy entry node without influence on actual computation will be added to the graph. $n_{\text {exit }}$ is a task with no immediate successors. Similarly, if a DAG has more than one $n_{\text {exit }}$, a dummy entry node will also be added to the graph. makespan is the maximum finish time of $n_{\text {exit }}$, so makespan is the scheduling length of the application program represented by the DAG.

The critical path (CP) of a DAG is the longest path from the entry node to the exit node in the graph. The lower bound of makespan is the minimum critical path length $\left(C P_{\min }\right)$, which is computed by considering the minimum computational costs of each node in the critical path. CCR is the communication-tocomputation ratio that is designed to measure the impact of communication latency on computing performance. For an application program, high CCR refers to communication-intensive, and low CCR refers to computation-intensive. CCR can be computed by Eq. (1) as follows:
$C C R=\frac{\sum_{i j} c_{i j} /|E|}{\sum_{i} \tilde{\omega}_{i} /|V|}$
$\tilde{\omega}_{i}$ denotes the average computation cost which can be computed by Eq. (2) as follows:
$\tilde{\omega}_{i}=\left(\sum_{j \in P} \omega_{i j}\right) / p$
The range percentage of computation costs $\beta$ on processors refers to the heterogeneity factor for processor speeds. A high $\beta$ value implies higher heterogeneity and different computation

![img-0.jpeg](img-0.jpeg)

Fig. 1. DAG-SP (a) a HCS with three processors (b) a DAG with ten tasks (c) computation cost matrix $W$.
costs among processors. The computation cost $\omega_{i j}$ of each task $n_{i}$ on each processor $p_{j}$ is randomly set from the range of Eq. (3):
$\tilde{\omega}_{i}(1-\beta / 2) \leq \omega_{i j} \leq \tilde{\omega}_{i}(1+\beta / 2)$
Fig. 1(a) shows a fully connected computing system with three heterogeneous processors. The DAG task diagram shown in Fig. 1(b) must be assigned to the HCS. The computation time of every task on different processors is different in the computation cost matrix $W$ in Fig. 1(c) [2].

### 2.2. Scheduling queue

In the list scheduling algorithm [1-3] or evolutionary algorithms [9], it is necessary to generate a scheduling queue. Different algorithms will give different scheduling orders and obtain different vertex scheduling queues. For example, in PEFT, vertex scheduling queues are sorted according to the average OCT value.

Definition 1 (Topology Feasible Queue), A topology feasible queue means that sequential scheduling will not result in violating the topology of the DAG, that is, the succ of every task is behind them in the topology feasible queue.

Definition 2 (Edge Cover Queue), An edge cover queue is a queue that arranges edge cover in topological order. In graph theory, an edge cover is a subset of the edges of a graph, so that each node in the graph is associated with an edge in the subset of edges. The queue of all edges in the DAG graph arranged in topological order is called the max edge cover queue.

Taking Fig. 1(b) as an example, the number of edges is fifteen, and the max edge cover queue is $[(1,2),(1,3),(1,4),(1,5),(1,6)$, $(3,7),(2,8),(2,9),(4,8),(4,9),(6,8),(5,9),(7,10),(8,10),(9,10)]$. An example of an edge cover queue is $[(1,2),(1,3),(1,4),(1,5),(1,6)$, $(3,7),(2,8),(2,9),(9,10)]$.

### 2.3. Estimation of distribution algorithm

The main idea of the EDA is to combine the evolutionary algorithm with the constructive mathematical analysis method to guide the effective search of the problem space [24-26]. Essentially, the EDA is an algorithm based on a probability model. It guides the following search range of the algorithm by updating the probability model from the currently found excellent individuals and generates new individuals from the probability distribution function of the obtained better solution for iteration. Combining genetic algorithms with statistical learning allows search iteration to be completed faster.

### 2.4. Graph random walk algorithm

The graph random walk algorithm traverses a graph from one or a series of vertices. At any vertex, the traverser of the random walk will walk to the neighbor vertex of this vertex with probability $(1-a)$ and jump to a non-neighbor vertex in the graph with probability $a$. After each walk, a probability distribution is obtained. The probability distribution depicts the probability that each vertex in the graph is visited. This probability distribution is used as the input of the next walk, and the process is iterated repeatedly. Over time, the probability distribution will tend to converge.

## 3. Related work

In this section, we present a concise survey of frequently used task scheduling algorithms including list scheduling algorithms and the EDA. We introduce the main ideas of these algorithms. Over the past few years, research on DAG-SP has focused on finding suboptimal solutions to obtain a good solution in an acceptable time. List scheduling algorithms can generate highquality suboptimal solutions at a reasonable cost without a high processor workload.

### 3.1. List scheduling algorithm

Research on the list scheduling algorithm for DAGs focuses on obtaining an acceptable solution in a short time. Compared with the evolutionary algorithm, the list scheduling algorithm has a low time complexity [1-3]. Therefore, this kind of algorithm is widely used in various HCSs. Here, we introduce several common list scheduling algorithms, most importantly HEFT and PEFT.

### 3.1.1. Earliest finish time

The EFT algorithm has two phases: a task prioritizing phase and a processor selection phase [2]. In the first phase, task priorities are defined as $\operatorname{rank}_{u}$, as shown in Eq. (4).
$\operatorname{rank}_{u}\left(n_{i}\right)=\tilde{\omega}_{i}+\max _{n_{j} \in \operatorname{succ}\left(n_{i}\right)}\left(\tilde{c}_{i j}+\operatorname{rank}_{u}\left(n_{j}\right)\right)$
$\operatorname{rank}_{u}$ represents the length of the longest path from task $n_{i}$ to the exit node, including the computational cost of $n_{i}$. The task list is ordered by decreasing value of $\operatorname{rank}_{u}$.

In the processor selection phase, the task on top of the list is assigned to the processor $p_{j}$ that allows for the earliest finish time of task $n_{i}: p_{n_{i}}=\arg \min _{p_{j}}\left(E F T\left(n_{i}, p_{j}\right)\right), E F T\left(n_{i}, p_{j}\right)$ denotes the finish time of task $n_{i}$ on processor $p_{j}$.

### 3.1.2. Heterogeneous earliest finish time

The HEFT algorithm is highly competitive and widely used since it was proposed [1]. In the task prioritizing phase, it is the same as the EFT algorithm with $\operatorname{rank}_{n}$. In the processor selection phase, the task on top of the task list is assigned to processor $p_{i}$, which allows for the EFT of task $n_{i}$. However, the HEFT algorithm uses an insertion policy that tries to insert a task in the earliest idle time between two already scheduled tasks on a processor if the slot is large enough to accommodate the task.

### 3.1.3. Predict earliest finish time

The novelty of the PEFT algorithm is its ability to forecast by computing OCT [2]. The OCT is a matrix in which the rows indicate the number of tasks and the columns indicate the number of processors, where each element $\operatorname{OCT}\left(n_{i}, p_{i}\right)$ indicates the maximum of the shortest paths of $n_{i}$ children tasks to the exit node considering that processor $p_{i}$ is selected for task $n_{i}$.

In the task prioritizing phase, PEFT computes the average OCT for each task that is defined by Eq. (5) as follows:
$\operatorname{rank}_{\text {OCT }}\left(n_{i}\right)=\frac{\sum_{i=1}^{p} O C T\left(n_{i}, p_{i}\right)}{p}$
In the processor selection phase, with an insertion policy, the processor that gives the minimum $O_{\text {EFT }}$ for a task is selected to execute that task. $O_{\text {EFT }}\left(n_{i}, p_{i}\right)$ equals $\operatorname{EFT}\left(n_{i}, p_{i}\right)+O C T\left(n_{i}, p_{i}\right)$.

In this way, PEFT is looking forward in the processor selection phase. Perhaps PEFT is not selecting the processor that achieves the EFT for the current task, but it expects to achieve a shorter finish time for the tasks in the next steps. In general, PEFT is still an effective heuristic greedy algorithm. Unlike EFT or HEFT, it is not greedy for time but greedy for $O_{\text {EFT }}$.

### 3.1.4. Lookahead scheduling algorithm

The LO algorithm is based on the HEFT algorithm, whose main feature is its processor selection policy [10]. To select a processor for the current task, it iterates over all available processors and computes the EFT for the child tasks on all processors. The processor selected for the current task is the one that minimizes the maximum EFT from all children of it. This procedure can be repeated for each child of task by increasing the number of levels analyzed. However, the LO algorithm has high time and computational complexity, even if only one level of children's tasks is considered. The LO algorithm performs well in some DAGs with regular structures, such as FFT and GE.

### 3.2. Estimation of distribution algorithm

The EDA is an appropriate algorithm to solve scheduling problems since its probability model can represent the precedence constraints between tasks and simulate the distribution of search space [24], [25], [26].

In multi-objective flexible job-shop scheduling problem with sequence-dependent setups problem, to minimize the completion time and installation cost, the relevant work uses the EDA to guide the machine learning strategy, learn valuable information from the nondominated solution of the main population, and establish a probability model to obtain better scheduling [26]. In resource scheduling for energy-efficient fog-enhanced Internet of Things, some papers use EDA and partition operators to partition the graph to determine task processing arrangement and processor allocation. It has similar performance to other algorithms in terms of fog node energy consumption and is superior to other algorithms in terms of maximum completion time [21], [22]. Furthermore, there are articles that apply some mathematical skills to speed up the EDA. The path relinking enhanced in the control field is used to speed up the EDA iterative solution process [3]. The scheduling solution obtained is better than the list scheduling algorithm in terms of completion time.

## 4. The proposed algorithm

In this section, we introduce a new scheduling algorithm for HCS, called the ECSA, which aims to achieve a better solution within acceptable time and computational complexity. The ECSA uses a designed structure's edge cover queue for task scheduling. The ECSA mainly includes two programs: Init-S and Iteration-of-S. Init-S completes the heuristic generation of the initial edge cover queue and probability model matrix $S$. Iteration-of-S completes the iteration of $S$ and the edge cover queue. The Init-S and Iteration-of-S programs use more basic methods, including the generation for edge cover queue, scheduling for edge cover queue, graph random walk algorithm, and simplified EDA. This section starts with introducing these basic methods in Sections 4.1, 4.2, 4.3, and 4.4, then two programs based on these basic methods are constructed in Sections 4.5 and 4.6, and the ECSA is constructed in Section 4.7. Finally, we introduce the overall process and theoretical advantages of the algorithm.

### 4.1. Generation for edge cover queue

In a DAG, the number of edges is generally considered to be at the $\pi^{2}$ level, so the edge cover queue has a huge number of permutations and combinations. Generating the edge cover queue through traversal will lead to massive time and computational complexity and may not have a good scheduling performance. This section introduces how to generate an edge cover queue based on a vertex queue and vertex sets with low time and computational complexity. Specifically, it includes two steps, the vertex-to-line step and loss-continuity step. Below, we will elaborate on this processing.

In the vertex-to-line step, the algorithm converts the input vertex queue $\pi$ and vertex set $V_{1}$ to an edge cover queue. The vertices in vertex queue $\pi$ are successively converted into corresponding edges under the guidance of vertex set $V_{1}$, and an edge cover queue line ${ }_{1}$ is obtained. In the loss-continuity step, the algorithm deletes some edges of line ${ }_{1}$ under the guidance of vertex set $V_{2}$ on the premise that the edge cover queue without topology errors. The pseudo code is as follows in Method 1. It is evident that the scheduling result of line ${ }_{1}$ generated by the vertex-to-line step is consistent with the vertex queue $\pi$. The scheduling result of line ${ }_{2}$ may be different from the original vertex queue. How to obtain vertex set $V_{1}$ and vertex set $V_{2}$ will be introduced in Sections 4.3 and 4.4.

Taking the DAG in Fig. 1(b) as an example, if the vertex queue is $[0,1,2,3,4,5,6,7,8,9,10,11]$, the vertex sets $V_{1}$ and $V_{2}$ are vertex 1 . Vertices 0 and 11 are dummy entry nodes without influence on the actual computation introduced in Section 2. The edge cover queue line ${ }_{1}$ obtained by the vertex-to-line step is $\{(0,1),(1,2),(1,3),(1,4),(1,5),(1,6),(3,7),(4,8),(5,9),(8,10)$, $(10,11)\}$. The output edge cover queue line ${ }_{2}$ obtained by the losscontinuity step is $[(1,2),(1,3),(1,4),(1,5),(1,6),(3,7),(4,8),(5,9)$, $(8,10),(10,11)]$.

### 4.2. Scheduling for edge cover queue

Unlike the vertex task queue, the edge cover queue takes the edge as the minimum unit in the scheduling process. In $e_{i j}$, if task $n_{i}$ has been scheduled, task $n_{j}$ will be scheduled according to a greedy cost function. Under this circumstance, task $n_{j}$ is vertex greedy scheduled. We call task $n_{i}$ a continuous vertex. If task $n_{i}$ has not been scheduled, task $n_{i}$ and task $n_{j}$ will be scheduled together to minimize the overall greedy cost function. Under this circumstance, task $n_{i}$ and task $n_{j}$ are edge greedy scheduled. We call task $n_{i}$ and task $n_{j}$ an un-continuous vertex. EFT and $O_{\text {EFT }}$ with

## Method 1 Generate edge cover queue

Input: vertex task queue $\pi$, vertex set $V_{1}, V_{2}$
1: vertex-to-line step:
2: for each task $\pi_{i}$ in $\pi$ do
3: if $\operatorname{pred}\left(\pi_{i}\right) \cap V_{1}=Y \neq \emptyset$ then
for each task $Y_{j}$ in $Y$ do
Put $\left(Y_{j}, \pi_{i}\right)$ in edge cover queue line ${ }_{1}$
end for
else
Put one of $\left(\operatorname{pred}\left(\pi_{i}\right), \pi_{i}\right)$ in line ${ }_{1}$
end if
end for
11: loss-continuity step:
for each task $n_{i}$ in $V_{2}$ do
Delete $\left(\operatorname{pred}\left(n_{i}\right), n_{i}\right)$ in line ${ }_{1}$
14: if line ${ }_{1}$ get topology error then
15: Cancel deletion
end if
17: end for
Output: line ${ }_{2}$

## Method 2 Schedule edge cover queue

Input: edge cover queue line ${ }_{3}$, label
if label $=0$ then
for each edge $\left(\operatorname{pred}\left(n_{i}\right), n_{i}\right)$ in line ${ }_{3}$ do
if task pred $\left(n_{i}\right)$ has been scheduled then
Schedule $n_{i}$ by $O_{E F T}$ with insert policy
else
Schedule pred $\left(n_{i}\right)$ and $n_{i}$ with minimum $O_{E F T}$ for $n_{i}$ with insert policy
end if
end for
end if
if label $=1$ then
for each edge $\left(\operatorname{pred}\left(n_{i}\right), n_{i}\right)$ in line ${ }_{3}$ do
if task pred $\left(n_{i}\right)$ has been scheduled then
Schedule $n_{i}$ by EFT with insert policy
else
Schedule pred $\left(n_{i}\right)$ and $n_{i}$ with EFT for $n_{i}$ with insert
policy
end if
end for
end if
Output: makespan of line ${ }_{3}$
the insert policy are chosen as greedy methods. The pseudo code is as follows in Method 2.

In this method, label indicates which greedy cost function to be used. Edge cover queue line ${ }_{3}$ is obtained from the after method. As mentioned earlier, each max edge cover queue may be very long. However, the scheduling of the edge cover queue line ${ }_{3}$ relative to the vertex queue does not have additional redundancy. This means that the edge cover queue's scheduling process has a similar time complexity as the scheduling process of the vertex queue.

### 4.3. Graph random walk algorithm

In the ECSA, the graph random walk algorithm generates vertex set $V_{1}$ under the guidance of the imaginary part of the diagonal element of probability model matrix $S$. How to obtain complex matrix $S$ will be introduced in Section 4.5. In the graph
random walk algorithm, first, random $(0,1 / n)$, the vertex whose imaginary part of the diagonal element $\operatorname{Im}\left(S_{i i}\right)$ is larger than this value, is put into vertex set $V_{1}$. The imaginary part of the diagonal element is updated according to the scheduling result $\Delta t$. The specific pseudo code is as follows in Method 3.

## Method 3 Graph random walk

Input: complex matrix $S, \Delta t$
random step:
$e=\operatorname{Random}(0,1 / n)$
if $\operatorname{Im}\left(S_{i i}\right) \geqslant e$ then
Put task $i$ to $V_{1}$
end if
update step:
for each task $n_{i}$ in $V_{1}$ do
$I m\left(S_{n_{i}, n_{i}}\right)=k \operatorname{Im}\left(S_{n_{i}, n_{i}}\right)+(1-k) \Delta t$
end for
Normalization $\left(\operatorname{Im}\left(S_{i i}\right)\right)$
Output: $V_{1}$

### 4.4. Local EDA in the ECSA

EDA establishes a probability model to simulate the distribution of the solution space. The standard EDA steps are as follows: First, the probability model matrix $S$ is established. The population in the subsequent iteration is generated by $S$. Then, under the guidance of $S$, a new population is generated, and $S$ is updated according to the results of the new population. The above steps are repeated until the stop criteria are met [2426]. However, when the standard EDA is used to generate a vertex queue in the scheduling algorithm, it leads to a high time complexity $O\left(G N n^{3}\right)$, where $n$ is the total number of tasks, $N$ is the size of the population, and $G$ is the number of iterations [3].

In some research, it is feasible to simplify the EDA to improve the solution speed according to the scenario requirements [28]. In the ECSA, to reduce complexity, we use a single individual instead of a population to update $S$ and generate new solutions. The updated formula of $S$ is also changed to adapt to this change, and the specific form will be introduced later. The edges $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ with the same front vertex $\left(n_{i}\right)$ in the edge cover queue have high parallelism between each other. Then, the real part between $\operatorname{succ}\left(n_{i}\right)$ in the matrix $S$ is updated by taking advantage of the influence of the topological structure change of these edges. In this way, the EDA plays a role only on local edges with the same front vertex, so we call this the local EDA in the ECSA. A single individual updating strategy and local EDA strategy will significantly reduce the complexity of the EDA in the ECSA. In this section, we divide the local EDA in the ECSA into the EDA-sample step, EDA-produce step and EDA-update step, for a total of three steps.

The EDA-produce step uses EDA to obtain a subset of the input vertex set $V_{1}$. The output vertex subset $V_{2}$ guides the losscontinuity step in Method 1 to generate un-continuous vertices in the edge cover queue.

The EDA-sample step changes topology between $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ in line ${ }_{2}$ guided by $V_{1}, S$. To produce individuals, a sampling method is designed for the relative position probability model between $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$. For task $n_{i}$, find all the positions of topological sorting $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ and place them in a backfill queue $B$. The order of the edges in $B$ is determined by the roulette method with reference to the probability distribution value between the corresponding real part of $\operatorname{succ}\left(n_{i}\right)$ in the matrix $S$. Then $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ is backfilled to line ${ }_{2}$ in order. Because the EDA is performed only for the topological relationship of $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$, the backfilling process only needs to check the topology of the partial edge cover

## Method 4 local-EDA

Input: vertex set $V_{1}$, matrix $S$, edge cover queue line ${ }_{2}, \Delta t$
EDA-produce step:
for each task $n_{i}$ in $V_{1}$ do
Put $n_{i}$ to $V_{2}$ with roulette method by $\operatorname{Re}\left(S_{n_{i}, n_{i}}\right)$
end for
EDA-sample step:
for each task $n_{i}$ in $V_{1}$ do
Put all $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ in backfill queue $B$ and topological sort
$B$ with roulette method by $S$
end for
for each edge $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ in $B$ do
Backfill $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ to line ${ }_{2}$ in order
if topology error in edge cover queue then
Place $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ at the top of $B$
end if
end for
if $B$ not empty then
Put them back, re-backfilling
end if
Get edge cover queue line ${ }_{3}$
EDA-update step:
for each task $n_{i}$ in $V_{1}$ do
Update $S_{n_{i}, n_{i}}$ by Eq. (6)
for each task in $\operatorname{succ}\left(n_{i}\right)$ do
if task $i$ is before task $j$ then
Update $S_{i j}$ by Eq. (6)
Update $S_{i j}$ by Eq. (7)
end if
end for
end for
Output: vertex set $V_{2}$, edge cover queue line ${ }_{3}$, matrix $S$
queue containing $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right.$ ). Suppose a topology error occurs after backfilling, placing it at the beginning of $B$ and selecting the next edge. Using the described method, the permutations produced by the EDA probability model can be guaranteed to be valid and satisfy the topological order of the DAG. If B is not empty after backfilling, ECSA backfills the remaining edges in B to the original position and then backfills the other edges. Finally, the EDA-sample step outputs the edge cover queue line ${ }_{3}$.

The EDA-update step updates $S$ according to the edge cover queue line ${ }_{3}$ and vertex set $V_{1}, V_{2}$. In ECSA, $S$ is designed as a $n \times n$ matrix to reduce the complexity of operation and storage. In the edge cover queue, the existing topological relationship between two vertices in the directed edge makes it impossible to update the probability model matrix $S$ directly by using the edge topological relationship. Thanks to the idea of local in the EDA-sample step, we only need to use the topological relationship between $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ to update the real part between $\operatorname{succ}\left(n_{i}\right)$ in S. Furthermore, the probability model matrix $S$ also avoids being designed as a vast $n^{2} \times n^{2}$ matrix.

Moreover, the EDA-sample step generates a single individual. We need to introduce a weighting term into the updated formula to adapt to this change. In ECSA, the weighted item is designed as the difference between the scheduling length makespan of the old and new queues: $\Delta t$. If task $i$ is before task $j$ in $\operatorname{succ}\left(n_{i}\right)$, the offdiagonal element $\operatorname{Re}\left(S_{i j}\right)$ and $\operatorname{Re}\left(S_{j i}\right)$ update formulas are as shown in Eqs. (6) and (7).
$\operatorname{Re}\left(S_{i j}\right)=k \operatorname{Re}\left(S_{i j}\right)+(1-k) \Delta t$
$\operatorname{Re}\left(S_{j i}\right)=1-\operatorname{Re}\left(S_{i j}\right)$

## Program 1 Init-S

1: Schedule DAG with HEFT and PEFT
2: if makespan $_{\text {HEFT }} \leq$ makespan $_{\text {PEFT }}$ then
$\pi=\pi_{\text {HEFT }}, t=$ makespan $_{\text {HEFT }}$, label $=1$
else
$\pi=\pi_{\text {PEFT }}, t=$ makespan $_{\text {PEFT }}$, label $=0$
end if
for each task $n_{i}$ in $V$ do
Calculate $P L$ of $n_{i}$, put max to $\lfloor\sqrt{n}\rfloor P L$ of $n_{i}$ to $P L S$
end for
for $\mathrm{i}=1$ :n do
for $\mathrm{j}=1$ :n do
if i=j then $\operatorname{Re}\left(S_{i j}\right)=0.5, \operatorname{Im}\left(S_{i j}\right)=1 / n$
else
if $P_{i j}=0$ then $\operatorname{Re}\left(S_{i j}\right)=0.5$
else
$\operatorname{Re}\left(S_{i j}\right)=0$
end if
end if
end for
end for
for each task $n_{i}$ in PLS do
$V_{1}=V_{2}=n_{i}$
Get line ${ }_{2}$ by Method 1
Get line ${ }_{3}$ by EDA-sample step and schedule line ${ }_{3}$
Calculate $\Delta t=t-t_{\text {line }_{3}}$
Update $S$ by EDA-update step and update step in Method
3
end for

### 4.5. Heuristic updating of $S$

In this section, we design the initialization and heuristic update method of the probability model matrix $S$. HEFT and PEFT are the most commonly used task scheduling algorithms due to their simplicity and performance [1,2]. Therefore, ECSA will heuristically update $S$ based on HEFT and PEFT.

First, HEFT and PEFT are performed on DAG to obtain the vertex queue of the HEFT, PEFT, OCT table and the label of which heuristic greedy cost function is better. Then, the prediction lookahead value ( $P L$ ) of tasks is sorted. PL is calculated by $P L=\sum_{n_{j} \leq n_{i} \leq n_{j}}\sigma\left(\omega_{j}\right) . \sigma\left(\omega_{j}\right)$ is variance. The $P L$ is considered as the potential of a vertex. Selecting vertices by decreasing the value of $P L$ total $\lfloor\sqrt{n}\rfloor$ nodes to form vertex set $P L S$.

Next, the ECSA initializes the complex matrix $S$ and assigns values to the elements in matrix $S$. The real and imaginary parts of the matrix $S$ are given initial values under the guidance of the matrix $P$, which is the topological matrix of the DAG graph. The initialized matrix $S$ is an equal probability matrix. The assignment method can be found in the pseudo code.

It is worth remembering that the real part of the matrix $S$ is used for the EDA, and the imaginary part is used for the graph random walk algorithm. In this part of the program, the algorithm puts the first vertex in PLS into vertex set $V_{1}, V_{2}$, and then moves it out from the top of the PLS. $V_{1}$ and a better vertex queue from HEFT or PEFT are transferred to Method 1 to obtain line ${ }_{2}$. The EDA-sample step further samples line ${ }_{2}$ with probability matrix $S$ and $V_{1}$. Calling the EDA-update step and graph random walk update algorithm update $S$. Thus far, the initialization of the matrix $S$ has been completed. The specific pseudo code is as shown in Program 1.

### 4.6. Iteration of $S$

In the previous Section 4.5, we used the heuristic queue PLS to heuristically update the probability matrix. This section introduces the iterative process of generating a new edge cover queue guided by $S$. Using the graph random walk algorithm, random $(0,1 /(n))$, the vertices whose imaginary part of the diagonal is greater than this value are placed in $V_{1}$. If the selected vertices can form an edge, the vertex with the larger PL value is selected. The length of $V_{1}$ shall not exceed $\lfloor\sqrt{n}\rfloor$. The following steps are similar to the Init-S algorithm, except that $V_{1}$ replaces a single vertex in the PLS, iterating $\lfloor\sqrt{n}\rfloor$ times and outputting the last edge coverage queue, that is, the ECSA output. The specific steps are as shown in Program 2.

## Program 2 Iteration-of-S

```
for num \(=1:\lfloor\sqrt{n}\rfloor\) do
    \(\quad\) Num \(=\) num \(++\)
    Get \(V_{1}\) by Graph random walk
    Get \(V_{2}\) by EDA-produce step
    Get Line \(_{1}\) by vertex-to-line step
    Get Line \(_{2}\) by loss-continuity step
    Get Line \(_{3}\) by EDA-sample step and schedule line \(_{3}\)
    Calculate \(\Delta t=t-t_{\text {line }_{3}}\)
    Update \(S\) by EDA-update step and update step in Method
    3
end for
```


### 4.7. ECSA

## Program 3 ECSA

```
Convert \(E\) to 01-matrix \(A\)
Compute longest path \(s\) in \(A\)
Compute \(P=A^{1}+A^{2}+\cdots+A^{s}\)
Init-S
Iteration-of-S
```

With the knowledge of graph theory, the power of the adjacency matrix of a graph contains the path information of the graph. ECSA can quickly obtain the topological matrix $P$ by using this property. First, ECSA converts $E$ to 01-matrix $A$ and finds the longest path $s$ in matrix $A$ through dynamic programming. Then,topological matrix $P$ calculate by $P=A^{1}+A^{2}+\cdots+A^{s} . P_{i j}>$ 0 that is, task $i$ is the pre-topological node of task $j . P_{i j}=0$, that is, task $i$ and task $j$ can be exchanged freely without topological relationship. Afterward, the ECSA uses the Program 1 to obtain the heuristic matrix $S$. Finally, the ECSA, as shown in Program 3 calls the Program 2 to iterate and output the final result.

### 4.8. Analysis for ECSA

### 4.8.1. Time complexity

The time complexity of our proposed algorithm is analyzed as follows. For Method 1, the generation for the edge cover queue is $O\left(n^{2}\right)$. For Method 2, scheduling for the edge cover queue method is near $O\left(n^{2} p\right)$. In the EDA-sample step, not all vertices are involved in sampling. Second, the EDA-sample step is sampling the topological relationship between $\left(n_{i}, \operatorname{succ}\left(n_{i}\right)\right)$ with the same front vertex. Moreover, the use of a single population further reduces the time complexity. Therefore, the EDA-sample step has a complexity near $O\left(n^{2.5}\right)$, and other operators in the local-EDA are $O\left(n^{2}\right)$ instead of the total $O\left(G N n^{3}\right)$ in the standard EDA.

For program Init-S, the time complexity comes from single vertex sampling and scheduling of the edge cover with $\lfloor\sqrt{n}\rfloor$ times iterations. The total time complexity is $O\left(n^{2.5}+n^{2.5} p\right)$.

For program Iteration-of-S, the calculation for the topological matrix $P$ is $O\left(n^{2}\right)$. In one iteration, the time complexity is $O\left(n^{2.5}+n^{2} p\right)$. There are $\lfloor\sqrt{n}\rfloor$ times iterations as well. Thus, the complexity of the proposed ECSA is $O\left(n^{3}+n^{2.5} p\right)$. This is an acceptable time complexity compared to $\operatorname{HEFT}\left(n^{2} p\right), \operatorname{PEFT}\left(n^{2} p\right)$, and $L O\left(n^{4} p^{3}\right)$.

### 4.8.2. Summary

The ECSA proposes using an edge cover queue for scheduling and proposes a method to generate an edge cover queue. It can be seen from the generation process of the edge cover queue that it is still similar in length to the initial vertex queue, avoiding additional redundancy. In addition, the edge cover queue can include the scheduling results of the vertex queue and reasonably explore more solution spaces on the basis of the excellent vertex queue to jump out of the greedy trap.

Furthermore, in the edge cover queue, if $n_{i}$ in $e_{i j}$ is not scheduled, the directed edge will be scheduled as a whole. Therefore, the loss-continuity step brings local greed to the scheduling process. For the ECSA, compared with the vertex queue, the final edge cover queue is a mixture of vertex greed and local greed in scheduling.

The ECSA is a memory algorithm. The complex matrix $S$ guides the EDA and graph random walk algorithm to generate the edge coverage queue. The single individual updating strategy and the local EDA strategy not only greatly reduce the complexity of the EDA but also make the ECSA have fewer iterations. Compared with the exponential iteration number of the genetic algorithm, the ECSA iteration number is lower, only $2\lfloor\sqrt{n}\rfloor$ times.

Taking the DAG in Fig. 1 as an example, the edge cover queue given by ECSA is $\{(1,3),(1,2),(1,4),(1,6),(1,5),(4,8),(3,7),(5,9)$, $(8,10)\}$. As shown in Fig. 2, compared with the PEFT, LO, and HEFT algorithms, the ECSA has a shorter scheduling length.

## 5. Experimental results

In this section, we compare the performance of the ECSA with that of the list scheduling algorithms presented above. We consider random DAGs and graphs that represent some real-world applications. We first introduce the evaluation metrics used for the scheduling algorithm. Then we show the performance of different algorithms for different types of DAGs.

### 5.1. Scheduling algorithm evaluation metrics

The evaluation metrics for the scheduling algorithm include makespan, efficiency, the ratio of better solutions and the scheduling length ratio(SLR). It is worth mentioning that the SLR is a parameter that considers the lower bound of the algorithm. It reflects the improvement by the algorithm better than makespan. Efficiency can reflect the improvement of HCS parallelism by the algorithm.

Makespan as shown in Eq. (8) is the most intuitive parameter. The smaller makespan is, the faster the execution of programs on the HCS is.
makespan $=\max F T\left(v_{\text {real }}\right)$
Efficiency is defined as Speedup $/ m$. Speedup as shown in Eq. (9) is defined as the ratio of the sequential execution time to the makespan of the algorithm. The calculation of sequential execution time assigns all tasks to a single processor to minimize the calculation time of DAG.
Speedup $=\frac{\min _{p_{i} \in V}\left\{\sum_{n_{i} \in V} \omega_{i j}\right\}}{\text { makespan }}$
The ratio of better solutions is well understood. This comparison is presented as a pairwise table, where the percentage of

![img-1.jpeg](img-1.jpeg)

Fig. 2. ECSA and other algorithm (PEFT, lookahead and HEFT) scheduling results.
better, equal, and worse solutions produced by ECSA is compared to other algorithms.

The scheduling length ratio is the ratio of the scheduling solution to an impossible lower bound. Here, we want to use a metric that compares DAGs with very different topologies. The metric most commonly used to do so is the normalized schedule length (NSL). It is also called SLR. For a given DAG, both represent the makespan normalized to the lower bound. SLR is defined in Eq. (10) as follows.
$S L R=\frac{\text { makespan }}{\sum_{v_{i} \in C P_{500}} \min _{P_{i} \in P}\left[\omega_{0}\right]}$
The denominator in SLR is the minimum computation cost of the critical path tasks $\left(C P_{\text {min }}\right)$. There is no makespan less than the denominator of the SLR equation. Therefore, the algorithm with the lowest SLR is the best algorithm.

### 5.2. Random DAGs

To evaluate the relative performance of the ECSA, we randomly generated DAGs. For this purpose, we used a DAG generation program TGFF [29]. The TGFF, as a general DAG generation tool, ensures the universality of the original data. For TGFF, there are a number of parameters relevant to the task graph structure: the average ( x ) and multiplier ( y ) for the lower bound on the number of nodes in a graph and the maximum in-degree (id) and out-degree (od) of graph nodes. A value for the lower bound of nodes is selected at random from the uniform range $[x-y, x+y]$. The upper bound of id and od for a DAG will relate to $\alpha$. Every node will obtain id and od randomly from the uniform range $[0, \alpha\lfloor\sqrt{n}\rfloor]$. For random DAG generation, we considered the following parameters:
$n=[20,30,40,50,60,70,80,90,100,200,300,400,500]$
$\alpha=[0.4,0.6,0.8,1]$
$C C R=[0.1,0.5,1,5]$
$p=[2,4,8,16]$
$\beta=[0.8,1]$

Generally, we think that 20 nodes' DAGs are small-scale and 500 nodes are large-scale, so we set $n$ from 20 to 500. $\alpha$ determines the upper bound of the in-degree and out-degree and further affects the number of DAG layers. Therefore, DAGs with large $\alpha$ look fat and DAGs with small $\alpha$ look thin, so we set the above $\alpha$ to make the test data evenly contain thin and fat DAGs. The $C C R$ of 0.1 is very low communication traffic and 5.0 is very high. Therefore, we set CCR from 0.1 to 5 so that the test data will gradually change from computation-intensive to communicationintensive. In the HCS, the number of computing cores varies greatly. Those with strong performance have 16 or more cores, while those with low performance have fewer cores (2-4) due to power consumption and cost considerations. Therefore, we choose 2 to 16 processors. Because our algorithm is for the HCS, our default system has strong heterogeneity. Therefore, we select $\beta$ as 0.8 and 1 to represent medium and high heterogeneity, respectively. These combinations produce 1920 groups of different DAGs. In each DAG, 20 different random graphs were generated for different communication cost edge and computation cost tasks. Thus, 38400 random DAGs were used in the research.

In the ECSA, in local-EDA and graph random walk update, the learning rate $k$ is 0.995 . To evaluate the performance of the ECSA, we compare it with four algorithms: EFT, HEFT, PEFT, and LO. For a fair comparison, the algorithms are all coded in C++ and run on the same computer with AMD 5800x 3.8 GHz and 32 GB RAM.

Fig. 3 shows the makespan as a function of the DAG size $n$, processor number $p$ and CCR. From Fig. 3(a), with the gradual increase of the DAG size, the ECSA can effectively reduce the makespan of the DAGs. The greater the task quantity is, the more makespan decreases. The HEFT and PEFT algorithms maintain similar performance in random DAGs. EFT is the simplest greedy algorithm and has the worst performance. The LO algorithm is designed and used in DAGs with specific structures. Although it has high complexity, it performs similarly to HEFT and PEFT when the DAG size is small or medium and performs worse than HEFT and PEFT when the DAG size is large, which is consistent with the result of the PEFT algorithm [2]. In general, the ECSA shows good optimization performance on makespan for various DAG sizes. More numerically, considering all random graphs as a whole, the reduction percentage of the ECSA compared with

![img-2.jpeg](img-2.jpeg)

Fig. 3. (a) n-makespan of random DAGs (b) p-makespan of random DAGs (c) CCR-makespan of random DAGs.
that of EFT on makespan is $8 \%$. This number for HEFT is $5 \%$, for PEFT is $4.3 \%$, and for LO is $6.2 \%$. The ECSA brings considerable reduction to the scheduling of random DAGs, and this reduction does not require any upgrading of the HCS. From Fig. 3(b), the ECSA can reduce the makespan of the DAGs on the HCS for a different number of processors. It can effectively improve the computing performance in HCSs at various scales. From Fig. 3(c), we have verified the reduction of makespan by various algorithms on different CCR random DAGs. The ECSA can effectively reduce the makespan of the DAG in both communication-intensive and computation-intensive tasks.

Low makespan is the most direct target in task scheduling, but the SLR is a parameter that can better reflect the performance of the scheduling algorithm. Because SLR reflects the approximation ratio between the current scheduling scheme and the optimal solution. To further compare ECSA with other algorithms, we then calculate the SLR of the scheduling results of the ECSA and other algorithms for DAGs with different sizes. From Fig. 4, the scheduling solution given by the ECSA has a lower SLR than other
scheduling algorithms. We can clearly see that as the DAG size increases, the SLR increases, and the ECSA reduces the SLR more. Under different DAGs, the scheduling results obtained by the ECSA can obtain a lower SLR.

Efficiency measures the utilization of scheduling algorithms for parallel computing systems. In Fig. 5, whether it is a small number of processors or a large number of processors, the ECSA can better improve the system efficiency, that is, enhance the parallelism of the system.

Table 1 shows the percentage of better, equal, and worse results for the ECSA when compared with other algorithms based on makespan. We can conclude that the ECSA can obtain better scheduling results in most situations.

Finally, we compare the execution time and memory usage of the above algorithms. We randomly selected five groups of random DAGs. Each group contains 1920 DAGs corresponding to the 1920 types of random DAGs mentioned above and calculates the average execution time of each DAG as the completion time and average memory usage. From Fig. 6(a), EFT is the simplest

![img-3.jpeg](img-3.jpeg)

Fig. 4. n-SLR average of random DAGs.
![img-4.jpeg](img-4.jpeg)

Fig. 5. p-efficiency of random DAGs.

Table 1
Better-equal-worse ratio.
list scheduling algorithm, so it has the lowest completion time. As algorithms with the same time complexity $\left(n^{2} p\right)$, HEFT and PEFT also have low completion times in general, but PEFT is approximately three times higher than HEFT. The LO algorithm is a list scheduling algorithm with high time complexity, but because we use LO with one step to greatly reduce the amount of computation, the completion time is also low. The ECSA is an iterative algorithm, but it also has a low completion time, which is close to the list scheduling algorithm of only 1.3 s . The ECSA is a memory-intensive algorithm that requires additional memory. From Fig. 6(b), however, the ECSA does not require too much memory usage. Therefore, we can conclude that the ECSA finds
suboptimal solutions to obtain a good solution in an acceptable time.

From the experimental results, for random DAGs, in general, the ECSA is a reliable algorithm that can bring considerable improvement to the scheduling process. The ECSA improves the efficiency of the system and makes the scheduling result closer to the optimal solution.

### 5.3. Real-world program

In addition to the random DAGs, we evaluated the performance of the algorithms with respect to the real-world program, Gaussian Elimination(GE) [30], and Fast Fourier Transform (FFT) [1]. All of these applications are well-known and used in real-world problems.

The FFT algorithm can be separated into two parts: recursive calls and the butterfly operation [1]. The input points $x$ determine the number of tasks [1]. The specific formula is $n=(x+2) 2^{x}-1$. In our experiment, the values for $x$ are $[3,4,5,6]$.

The GE algorithm is a common method for solving matrix [30]. For GE, the matrix size $x$ determines the number of tasks. The number of tasks $n$ in a Gaussian Elimination DAG is equal to $\frac{x^{2}+x-2}{2}$. In our experiment, the values for $x$ are $[20,21,22,23,24$, $25,26,27,28,29]$.

Because of the fixed structure of these applications, we simply used different values for CCR, heterogeneity, and CPU number. The range of values that we used in our simulation was $[0.1,0.5,1,5]$ for CCR, $[0.6,1]$ for heterogeneity, and $[2,4,8,16]$ for CPU number. Moreover, we will use the boxplot to analyze the SLR of scheduling results of different algorithms instead of the average SLR, which is different from random DAGs.

### 5.3.1. Fast Fourier Transform

The FFT algorithm is one of the most commonly used algorithms in the communication field and can help researchers analyze the spectrum of signals [1]. Almost every engineering researcher has learned the FFT algorithm. From Fig. 7, compared with the comparison algorithms, the ECSA performs better in terms of efficiency and SLR in FFT DAGs. Similar to the results of in the PEFT algorithm, HEFT seems to be the most appropriate algorithm among these comparison algorithms [2]. However, the ECSA has shown better performance in FFT programs. It can not only improve the efficiency of a variety of systems but also

![img-5.jpeg](img-5.jpeg)

Fig. 6. (a) average completion time (b) average memory usage.
![img-6.jpeg](img-6.jpeg)

Fig. 7. (a) p-efficiency of FFT (b) n-SLR boxplot of FFT.
![img-7.jpeg](img-7.jpeg)

Fig. 8. (a) p-efficiency of GE (b) n-SLR boxplot of GE.
effectively reduce the SLR. In total, numerically, the ECSA brings about a $3.2 \%$ reduction in makespan and a $3.1 \%$ reduction in average SLR compared to HEFT.

### 5.3.2. Gaussian elimination

The GE algorithm is an algorithm in linear algebraic programming that can be used to solve linear equations. It is used to find
the rank of a matrix and the inverse matrix of a reversible square matrix. From Fig. 8, the results obtained from ECSA were similar to HEFT and PEFT with only minor advantages, and the LO algorithm shows the best performance. This is not surprising. The LO algorithm often performs very well in the Gaussian elimination method DAG with a high time complexity $O\left(n^{4} p^{3}\right)$. Therefore, the ECSA is also an optional algorithm for GE programs.

## 6. Conclusions and future work

In this paper, we design a new algorithm, the ECSA, for the DAG-SP. An efficient DAG task scheduling algorithm can benefit the performance of loT and cloud computing to improve the quality of user experience. In addition, an appropriate task scheduling algorithm can upgrade the resource balancing in a single processor with multiple cores and multiple virtual machines. The experimental results of a vast number of random DAG and real-world DAG data prove the theoretical advantages of the ECSA algorithm. The ECSA can benefit the DAG-SP in terms of makespan, efficiency, and SLR. It can be claimed that the ECSA can obtain a solution closer to the optimal, achieving better performance solutions in an acceptable time.

In the future, we will study two aspects. First is nondeterministic task scheduling model. In this model, the computing resources and completion time required by a single task vertex are no longer known or can accurately predict such as in a D2D network [31,32]. The existing task scheduling algorithm will cause a significant decline in system performance when applied to such scheduling problems. Second, a lighter edge cover queue scheduling algorithm for the DAG-SP model. We want to further reduce the time and computational complexity for edge cover queue generation.

## CRediT authorship contribution statement

Yu-meng Chen: Conceptualization, Methodology, Software, Writing - review \& editing. Song-lin Liu: Data curation, Software. Yan-jun Chen: Visualization, Investigation. Xiang Ling: Project administration.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Appendix A. Supplementary data

Supplementary material related to this article can be found online at https://doi.org/10.1016/j.knosys.2023.110369.
