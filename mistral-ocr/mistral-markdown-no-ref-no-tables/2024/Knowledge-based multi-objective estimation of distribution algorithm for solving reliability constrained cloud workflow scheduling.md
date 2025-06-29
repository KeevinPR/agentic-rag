# Knowledge-based multi-objective estimation of distribution algorithm for solving reliability constrained cloud workflow scheduling 

Ming $\mathrm{Li}^{1} \cdot$ Dechang $\mathrm{Pi}^{1} \cdot$ Shuo Qin ${ }^{1}$<br>Received: 25 January 2023 / Revised: 10 April 2023 / Accepted: 30 April 2023 / Published online: 14 May 2023<br>(c) The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2023


#### Abstract

With the rapid development of cloud computing, numerous large-scale workflow are executed in the cloud environment. Therefore, the workflow scheduling in cloud environment has become an emerging topic. This paper focuses on a reliability constrained multi-objective workflow scheduling problem (RCMOWSP) with the objectives of minimum execution cost and time. To solve the RCMOWSP, this paper proposes a knowledge-based multi-objective estimation of distribution algorithm (KMOEDA) with several problem-specific operators. First, an idle time-based decoding scheme is applied to sort the permutation of tasks greedily. In the global search strategy, a probability model is constructed to improve the diversity of population. Based on the problem-specific knowledge, a reliability-aware local search strategy is designed to performs local search around the solutions that violate reliability constraint. An elite enhancement strategy with a task perturbation operator and a resource perturbation operator is introduced to further improve the elite nondominated solutions in the external archive. A comprehensive experiment is conducted to verify the performance of KMOEDA. The comparative results show that the KMOEDA significantly outperforms several relative multi-objective workflow scheduling approaches in solving the RCMOWSP.


Keywords Cloud computing $\cdot$ Workflow scheduling $\cdot$ Multi-objective optimization $\cdot$ Estimation of distribution algorithm $\cdot$ Reliability constraint

## 1 Introduction

Complex scientific computing programs are frequently described as workflows in several scientific domains, i.e., physics, biology, and astronomy [1, 2]. Directed acyclic graphs (DAGs) are applied to define the common workflow model [3]. In a DAG, the nodes represent computational tasks in a workflow, and the edges denote the relationships in data and control flow among various tasks. Due to the complex dependency relationships between tasks and the

[^0]high amount of computation and transmission, it is a significant challenge to execute the workflow with reasonable time and cost [4].

As a prevalent computing paradigm, cloud computing can offer computing services on demand in a pay-as-you-go manner [5, 6]. Cloud service providers deploy numerous virtual machines on the servers to satisfy the requirements of widely dispersed users, which can effectively reduce the operational cost of services providers and the rental charges of users [7, 8]. Large-scale workflows are frequently deployed on the cloud computing platforms for execution because of the low cost, flexible application mode, and high availability. During the workflow execution process, the tasks must satisfy the dependency with other tasks and the available of virtual machines $[9,10]$. Therefore, the tasks may be delayed because of the unsatisfied data and control dependencies or the occupied virtual machines, which increases total execution cost (TEC) and total execution time (TET). It is clear that the effective and efficient workflow scheduling algorithm can significantly reduce TET and TEC [11-13].


[^0]:    $\boxtimes$ Shuo Qin
    qinshuo@nuaa.edu.cn
    Ming Li
    li_ming_nuaa@163.com
    Dechang Pi
    dc.pi@nuaa.edu.cn
    1 School of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Shengtai West Road, Nanjing 211100, China

Existing workflow scheduling algorithms can be roughly divided into two categories, called real-time scheduling algorithms [14, 15] and predictive scheduling algorithms [16, 17]. Real-time scheduling algorithms focus on optimizing a single objective such as time and cost when meeting the desired constraints, i.e., budget and deadline. In addition, the real-time scheduling algorithms can fully utilize the transient resources in cloud environment when the resources requirement for tasks increase sharply. The computational complexity of a real-time scheduling algorithm is low, and then the real-time requirement can be satisfied. Predictive scheduling algorithms produce predictive schedules based on the estimated computational and transmission time. The running time of the predictive scheduling algorithm is long, and it is unable for real-time scheduling. The predictive scheduling algorithm obtains schedules and resources leasing scheme before workflow execution. Therefore, the predictive scheduling algorithms do not utilize transient resources. However, most of the real-time scheduling algorithms are heuristic approaches, which mainly depend on greedy search and are restricted by some predefined rules. Thus, the performance of the heuristic approaches is poor when addressing complex large-scale workflow scheduling problems. Therefore, the predictive scheduling algorithms, which are based on the intelligence optimization algorithms with strong global search technique, are superior to the realtime scheduling algorithms for the large-scale workflow scheduling problems [18-20].

Furthermore, multi-objective predictive workflow scheduling algorithms usually take numerous requirements of users into account and provide a set of trade-off schedules from which users can choose their favorite alternatives. This paper studies the multi-objective predictive workflow scheduling algorithm for the large-scale scientific workflow scheduling problem.

Most of the existing multi-objective predictive workflow scheduling algorithms focus on scheduling workflows with minimization TET and TEC. However, virtual machines in a cloud computing environment frequently experience momentary issues that prevent task execution [21]. To be specific, although some schedules achieves the low execution cost or fast execution time, their reliability may be extremely low. The low-reliability schedule results in a small probability to execute the workflow successfully. Additionally, the high reliability of the predictive schedules cannot guarantee the schedule seamless implementation, and requires expensive costs. Therefore, this paper focuses on the reliability-constrained multi-objective predictive workflow scheduling problem (RCMOWSP) in the cloud computing environment.

RCMOWSP involves three aspects, i.e., resource rental scheme, task allocation scheme, and task permutation. Moreover, the schedules should satisfy the predefined
reliability constraints. However, there are too many schedules which do not meet the reliability constraint. Therefore, the existing algorithm cannot address this problem effectively because they will produce too many unfeasible solutions. In addition, the multi-objective cloud workflow scheduling problem typically requires high diversity of population, which can ensure the distribution of the final schedules. Thus, it is necessary to improve the global search ability of the algorithms. For these reasons, this paper proposes a knowledge-based multi-objective estimation of distribution algorithm (KMOEDA) to address the considered problem. KMOEDA apply the estimation of distribution algorithm (EDA), which is suitable for solving the large-scale optimization problem, to be the global search strategy. Besides, the core component of KMOEDA is the reliability-aware local search strategy, which can guide the search direction of algorithm and improve the search efficiency. The contributions of this paper can be summarized as follows.

- Formulate the reliability-constrained multi-objective workflow scheduling problem with the objectives of minimizing TET and TEC.
- A knowledge-based estimation of distribution algorithm with several problem-specific strategies is proposed to solve RCMOWSP.
- A reliability-aware local search strategy is designed to handle the schedules that violate the reliability constraint.
- The effectiveness and efficiency of KMOEDA are investigated by a set of experiments.

The remainder of this paper is structured as follows. Section 2 introduces the related work of the workflow scheduling algorithms in cloud environment. Section 3 describes the considered problem and related definitions. Section 4 details the proposed algorithm. Section 5 presents the parameter calibration, ablation analysis, and comparative experiments. In Sect. 6, the conclusion and several promising future directions are provided.

## 2 Literature review

The workflow scheduling algorithms consist of real-time workflow scheduling algorithms and predictive workflow scheduling algorithms. Efficiency is the most significant performance metric for real-time workflow scheduling algorithms. As a result, the real-time workflow scheduling problems can be effectively solved by the heuristic approach with low time complexity. The traditional heuristics for the real-time workflow scheduling problem are the HEFT algorithm [22], Max-Min algorithm [23], and CPOP algorithm [24]. Additionally, there are numerous

heuristics for the workflow scheduling problems that take into account various factors, i.e., scalability [25], data localization [26], data transmission delay[27], bandwidth restriction [28], security[29], price[30], resource utilization [31], uncertainty [14], and fault tolerance [15].

Predictive workflow scheduling algorithms includes the deadline-constrained workflow scheduling algorithms, the budget-constrained workflow scheduling algorithms, and the multi-objective workflow scheduling algorithms. For the elastic and heterogeneous resources in cloud environment, a resource allocation and scheduling algorithm based on particle swarm optimization (PSO) was proposed by Rodriguez et al. [32] to address the deadline-constrained workflow scheduling problem with the objective of minimizing cost. Wang et al. [33] developed a distributed particle swarm optimization algorithm (DGLDPSO) based on the dynamic group learning strategy to minimize the execution cost with the deadline constraint for the large-scale workflow scheduling problem. Based on the virtual machines configurations in the actual public cloud and the execution data from the actual scientific workflow, Jia et al. [18] designed a novel task execution time estimation model and proposed an adaptive ant colony optimization algorithm (A-ACO) for workflow scheduling problem. To reduce the workflow execution cost under deadline constraint, Wu et al. [34] presented a meta-heuristic L-ACO and a heuristic ProLiS, where L-ACO is employed to optimize cost, and ProList is response for assigning the deadline constraint to each task. Faragardi et al. [17] suggested the resource supply and workflow scheduling algorithm GRP-HEFT to optimize the execution time when meeting the budget constraint. GRPHEFT constructs the resource leasing scheme based on the resource execution efficiency using the greedy strategy, and applies the improved HEFT algorithm to schedule the tasks in the workflow.

To offer a set of trade-off Pareto solutions for users, Durillo et al. [35] developed a multi-objective HEFT algorithm (MOHEFT) to optimize the execution time and cost simultaneously. Then, users can select one of the schedules based on their preferences. However, MOHEFT requires an excessively high time and space complexity because it is an exhaustive-based approach. Therefore, MOHEFT is not appropriate for the large-scale workflow scheduling problem. Wu et al. [36] designed a multi-objective evolutionary list scheduling algorithm (MOELS) to address the multi-objective workflow scheduling problem. In MOELS, the schedule is encoded as the permutation in which tasks are executed, and the decoding procedure makes use of the HEFT algorithm. For resource management methods and payment strategies in the cloud computing environment, Zhu et al. [16] proposed a workflow scheduling strategy based on an evolutionary multi-objective optimization algorithm (EMS-C). Based on the
problem-specific knowledge, EMS-C proposes a novel coding method, an initialization strategy, a fitness evaluation function, and genetic operators. According to the weight aggregation approach described in the literature [37], the execution cost and time are aggregated as an optimization objective. Then, the HEFT algorithm and gravitational search algorithm are combined to schedule the workflow. For optimizing the execution time, cost, and virtual machine energy efficiency, Paknejad et al. [38] developed an enhanced multi-objective co-evolution algorithm (ch-PICEA-g) based on chaotic systems. To minimize execution time, cost, and energy consumption and maximize reliability, an improved multi-objective particle swarm optimization algorithm (I_MaOPSO) is proposed by Saeedi et al. [39] for multi-objective workflow scheduling.

As above review, the classic multi-objective workflow scheduling problem with the objectives of minimizing cost and time has been successfully solved with the existing algorithms. However, the reliability of schedule has been ignored in the most of the previous researches. To be specific, the low reliability of schedule represents that the implementation of this schedule would fail with large probability. Then, the low execution cost and fast execution time of this schedule are meaningless. Moreover, a few existing approaches focus on maximizing the reliability when minimizing the time and cost. However, the high reliability often results in expensive cost and slow execution time. Considering the execution time and cost are the most concerned metrics of users, this paper tends to formulate a reliabilityconstrained multi-objective optimization problem to provide users with relatively reliable schedules. Then, the users can select one of the reliable schedules to execute the workflow on the cloud environment.

## 3 Problem statement

This section describes the considered problem from three aspects: the workflow model, the cloud resource model, and the reliability-constrained multi-objective cloud workflow scheduling model. The notations used in this section are displayed in Table 1.

### 3.1 Workflow model

Workflow model is denoted by the directed acyclic graph (DAG), $G=\langle T, E, W, D\rangle . T=\left\{t_{1}, t_{2}, \cdots, t_{n}\right\}$ indicates the set of tasks. $E=\left\{\left\langle t_{i}, t_{j}\right| \mid t_{i}, t_{j} \in T\right\}$ denotes the dependency relationships between tasks. $W=$ $\left\{w\left(t_{1}\right), w\left(t_{2}\right), \cdots, w\left(t_{n}\right)\right\}$ is the computational load of tasks. $D=\left\{d\left(t_{i}, t_{j}\right) \mid\left(t_{i}, t_{j}\right) \in E\right\}$ is the communication load between tasks. From above definitions, the predecessor

Table 1 The notations and descriptions

tasks set and the successor tasks set can be defined as $P\left(t_{i}\right)=\left\{t_{p} \mid\left(t_{p}, t_{i}\right) \in E\right\}$ and $C\left(t_{i}\right)=\left\{t_{c} \mid\left(t_{i}, t_{c}\right) \in E\right\}$. Figure 1 depicts a workflow model made up of 10 tasks.

From Fig. 1, it can be observed that the predecessor tasks set of task $t_{5}$ is $P\left(t_{5}\right)=\left\{t_{1}, t_{4}\right\}$, the successor tasks set of task $t_{5}$ is $C\left(t_{5}\right)=\left\{t_{7}, t_{9}\right\}$. The computational load $w\left(t_{5}\right)$ is 5 , and the communication load $d\left(t_{5}, t_{7}\right)$ is 4 .
![img-0.jpeg](img-0.jpeg)

Fig. 1 A workflow model with 10 tasks

### 3.2 Cloud resource model

Cloud computing provides computational services in the form of virtual machines. The users can rent any number of any kind of heterogeneous virtual machines at any time. To be specific, there is an enormous number of virtual machine configurations in a cloud environment, but the cost to rent a virtual machine increases with computational efficiency. Moreover, the users must pay for a full-time unit even if the virtual machine is used for a short time. For any resource $r_{j}, L S T\left(r_{j}\right)$ represents the start time, $L E T\left(r_{j}\right)$ denotes the end time, and $L D T\left(r_{j}\right)$ means the holding time. Let $\operatorname{Pr}\left(r_{j}\right)$ represents the unit rental price of $r_{j}$, the total rent cost of resource $r_{j}$ can be calculated as follows.
$\operatorname{Cost}\left(r_{j}\right)=\operatorname{Pr}\left(r_{j}\right) \times\left\lceil L D T\left(r_{j}\right) / u\right\rceil$
where $u$ is the rent time unit. In this paper, the hourly billing mechanism is used, which means $u$ is set to $1 h$.

### 3.3 Reliability-constrained multi-objective workflow scheduling model

We assume that task $t_{i}$ is deployed on resource $r_{j}$, and the processing capacity of $r_{j}$ is $C U\left(r_{j}\right)$, the execution time $E T\left(t_{i}, r_{j}\right)$ of task $t_{i}$ on resource $r_{j}$ is defined as follow.
$E T\left(t_{i}, r_{j}\right)=w\left(t_{i}\right) / C U\left(r_{j}\right)$
Furthermore, the data transmission time $\operatorname{tr}\left(t_{p}, t_{i}\right)$ from any predecessor task $t_{p}$ to task $t_{i}$ can be calculated as below.
$\operatorname{tr}\left(t_{p}, t_{i}\right)=\left\{\begin{array}{cc}\frac{d\left(t_{p}, t_{i}\right)}{\beta}, & \text { if } r\left(t_{p}\right) \neq r\left(t_{i}\right) \\ 0, & \text { otherwise }\end{array}\right.$
where $r\left(t_{p}\right)$ and $r\left(t_{i}\right)$ are the resources which execute task $t_{p}$ and $t_{i} . \beta$ is the bandwidth between resources $r\left(t_{p}\right)$ and $r\left(t_{i}\right)$. Furthermore, The start time of task $t_{i}$ is constrained by two factors, (1) the task must delay until all of the communication data from its immediate predecessor tasks

has been received; (2) the task can be executed when the corresponding resource is free. As a result, the task start time $S T\left(t_{i}\right)$ can be calculated as follow.

$$
S T\left(t_{i}\right)=\max \left\{\max \left\{F T\left(t_{p}\right)+\operatorname{tr}\left(t_{p}, t_{i}\right)\right\}, L E T\left(r\left(t_{i}\right)\right)\right\}, \quad t_{p} \in P\left(t_{i}\right)
$$

where $F T\left(t_{p}\right)$ denotes the finish time of task $t_{p}$, $\max \left\{F T\left(t_{p}\right)+\operatorname{tr}\left(t_{p}, t_{i}\right)\right\}$ indicates that the task $t_{i}$ have received all communication data from its predecessor tasks. $L E T\left(r\left(t_{i}\right)\right)$ is the finish time of the previous task on the same resource. Then, the finish time $F T\left(t_{i}\right)$ can be calculated as follow.
$F T\left(t_{i}\right)=S T\left(t_{i}\right)+E T\left(t_{i}\right)$
Furthermore, the resource start time $L S T\left(r_{j}\right)$ is equal to the start time of the first task executed on $r_{j}$, and the resource end time $L E T\left(r_{j}\right)$ is equal to the finish time of the last task executed on $r_{j}$.

$$
\begin{aligned}
L S T\left(r_{j}\right) & =\min \left\{S T\left(t_{i}\right) \mid r\left(t_{i}\right)=r_{j}\right\} \\
L E T\left(r_{j}\right) & =\max \left\{F T\left(t_{i}\right) \mid r\left(t_{i}\right)=r_{j}\right\} \\
L D T\left(r_{j}\right) & =L E T\left(r_{j}\right)-L S T\left(r_{j}\right)
\end{aligned}
$$

Since RCMOWSP is a predictive scheduling problem which generates schedules before the workflow is executed, there is no scheduling consuming in the workflow execution process. Then, the total execution time (TET) and total execution time (TEC) can be calculated as follows.

$$
\begin{aligned}
& T E T=\max \left\{E T\left(t_{i} \mid t_{i} \in T\right)\right\} \\
& T E C=\sum_{j=1}^{m} \operatorname{Cost}\left(r_{j}\right)
\end{aligned}
$$

In the cloud environment, the transient failure caused by virtual machine crashes and software defects will interrupt the workflow execution, and then the schedules cannot be implemented as expected. In this paper, we assume that the failure of virtual machines follows Poisson distribution. Let $\lambda\left(r_{j}\right)$ denotes the failure rate of resource $r_{j}$, the reliability of task $t_{i}$ on resource $r_{j}$ can be defined as follow.
$\operatorname{rel}\left(t_{i}, r_{j}\right)=e^{-\lambda\left(r_{j}\right) \times E T\left(t_{i}, r_{j}\right)}$
Then, the reliability of the whole workflow can be calculated as

$$
\operatorname{Rel}=\prod_{i=1}^{n} \operatorname{rel}\left(t_{i}, r\left(t_{i}\right)\right)
$$

Therefore, the optimization objective of the considered problem is to minimize $T E T$ and $T E C . \delta_{\text {Rel }}$ is a user-defined reliability threshold, which means that a feasible schedule must meet the constraint $\operatorname{Rel}>\delta_{\text {Rel }}$.

## 4 Proposed algorithm

Due to the RCMOWSP not being solved by the previous research, this paper proposes a knowledge-based multiobjective estimation of distribution algorithm (KMOEDA) to solve the considered problem. Considering the elastic and heterogeneous resources, the resource pool is constructed based on the maximum number of parallel tasks in KMOEDA. A decoding technique focused on idle time is designed throughout the decoding process to greedily sort the order of the tasks on the same virtual machine. Based on the above strategies, the problem space of RCMOWSP is reduced to the mapping relationships between tasks and virtual machines. Then, an effective initial strategy is designed to construct promising solutions. To prevent premature convergence and ensure the diversity of the population, a global search strategy is designed based on the estimation of distribution algorithm. Estimation of distribution algorithm can be classified as univariate, bivariate, and mutivariate due to variations in statistics. As the probability model in KMOEDA is a univariate model, the proposed KMOEDA is univariate. In addition, a rela-bility-aware local search strategy is proposed to handle the solutions that violate reliability constraints. Furthermore, an elite enhancement strategy for the elite solution in the external archive is developed based on the critical task and resource perturbation operators. The details of all components are explained below.

### 4.1 Encoding and decoding strategy

Because of the elasticity and Heterogeneity of virtual machines, the construction of a resource pool has a significant impact on the schedules. Due to each task in the workflow is only executed once, and the task can only be executed by one resource at the same time, a workflow of size $n$ can occupy up to $n$ resources. Obviously, the maximum size of the resource pool is $n$. In the previous research, there are two popular strategies for constructing the resource pools during the optimization process. The first one is to set the maximum size of the resource pool to $n$, and the type of each resource is dynamically optimized during the search process, which is the dynamic resource pool [16]. The second one is to preset the resource pool based on the maximum number of parallel tasks, and the resource type remains unchanged during the search process, called static resource pool [40]. Compared to the dynamic resource pool, the static resource pool can effectively reduce the complexity of problem space. Since only one resource can execute a task at a time, the following problem-specific knowledge can be discovered. For a given workflow with $n$ tasks, the maximum number of leasing

virtual machines is $n$. We assume that the cloud environment provides $k$ configurations of virtual machines. Then, the maximum number of virtual machines in the resources pool is $n \times k$. However, not all tasks can be executed at the same time because of the topology constraints between tasks. Therefore, we construct a resource pool by using the maximum number of parallel resources. We assume that the given contains $n$ tasks, and each resource only executes one task. Then, the maximum number of parallel resources $M P T$ can be calculated based on the start time and finish time of each task. Therefore, the number of virtual machines in the resources pool is $M P T \times k$, where the instance of $\left\{r_{1}, r_{2}, \cdots, r_{M P T}\right\}$ is $p_{1}$, the instance of $\left\{r_{M P T+1}, r_{M P T+2}, \cdots, r_{2 \times M P T}\right\}$ is $p_{2}$, and so on.

Figure 2 depicts the encoding strategy that the workflow in Fig. 1 is scheduled to the resources pool $R$. In Fig. 2, the first row demonstrates the tasks in the workflow, and the second row indicates the deployment of tasks on resources. For example, the first position of the second row is 1 , which means that the task $t_{1}$ is assigned to the resource with index 1 . For any task, the start time is limited by the resource release time and the time that all direct predecessor tasks transfer data are received. When the time of receiving data is later than the resource releasing time, the idle time slot will appear. Because the resources are leased on the hourly billing mechanism, using the idle time slots can effectively reduce the execution time without raising the resource leasing cost. Therefore, this paper designs an idle time-based decoding strategy to construct the execution order of tasks. The decoding strategy consists of two

Fig. 2 An example of the encoding strategy
phases. In the first phase, the tasks are ordered according to the average execution time and data transmission time of tasks. The task priority can be calculated as follow.
$\operatorname{pri}\left(t_{i}\right)=\overline{E T\left(t_{i}\right)}+\max _{t_{i} \in C\left(t_{i}\right)}\left(\overline{i r\left(t_{i}, t_{c}\right)}+\operatorname{pri}\left(t_{c}\right)\right)$
where $\overline{E T\left(t_{i}\right)}$ is the average execution time of $t_{i}$ on all available instances, and $\overline{i r\left(t_{i}, t_{c}\right)}$ is the average transmission time between $t_{i}$ and $t_{c}$. In the second phase, the tasks without predecessors in $T$ are firstly added to the ready tasks set $R S$, and the task permutation $O$ is an empty set. Then, the task with the highest priority is chosen and the earliest start time $E S T\left(t_{k}\right)$ is calculated. When $E S T\left(t_{k}\right)$ is larger than $L E T\left(r\left(t_{k}\right)\right)$, an idle time slot will appear on $r\left(t_{k}\right)$ if the task $t_{k}$ is directly executed. Therefore, all ready tasks which are deployed on $r\left(t_{k}\right)$ are carried out to construct a set $T S$ in the order of task priority. Then, the earliest finish time $E F T\left(t_{i}\right)$ of each task is calculated. When $E F T\left(t_{i}\right)$ is smaller than $E S T\left(t_{k}\right)$, the task $t_{i}$ can be executed in the idle time slot. Therefore, $t_{i}$ is appended to the tail of $O$. If the earliest finish time of all tasks is larger than $E S T\left(t_{k}\right), t_{k}$ is directly appended to the tail of $O$. Next, the edges between $t_{k}$ and other tasks are removed, and the tasks in $T$ without predecessors are added to $R S$. The above procedure is repeated until $R S$ is an empty set. The decoding strategy is described in Algorithm 1.

```
Algorithm 1 Decoding strategy
    Sort the tasks according to task priority
    Init ready tasks set \(R S \leftarrow\left\{t_{i} \mid P\left(t_{i}\right)=\emptyset\right\} \cap T, O \leftarrow \emptyset\)
    while \(R S \neq \emptyset\) do
        \(t_{k} \leftarrow \operatorname{argmax}(\operatorname{pri})\), Calculate \(E S T\left(t_{k}\right)\)
        if \(E S T\left(t_{k}\right) \geq L E T\left(r\left(t_{k}\right)\right)\) then
            \(T S \leftarrow\left\{t_{i} \mid r\left(t_{i}\right) \wedge t_{i} \in R S\right\}\)
            Sort \(T S\) according to task priority
            for \(t_{i} \in T S\) do
                Calculate \(E F T\left(t_{i}\right)\)
                if \(E F T\left(t_{i}\right)<E S T\left(t_{k}\right)\) then
                    \(t_{k} \leftarrow t_{i}\), break
                end if
            end for
        end if
        Append \(t_{k}\) to the tail of \(O\)
        for \(t_{i} \in C\left(t_{k}\right)\) do
            Remove edge \(\left(t_{k}, t_{i}\right)\)
            if \(P\left(t_{i}\right)=\emptyset\) then
                \(R S=R S \cup\left\{t_{i}\right\}\)
            end if
        end for
    end while
```

Suppose that the processing capacity of all resources are 1 and the bandwidth between resources are 1 , the priority of tasks in the workflow shown in Fig. 1 is $\{48,41,16,37,24,29,15,12,7,2\}$. Therefore, the task $t_{1}$ with the largest priority is chosen. Due to task $t_{1}$ has no predecessors and the assigned resource $r_{1}$ can be used immediately, the task $t_{1}$ is executed on the first position of resource $r_{1}, F T\left(t_{1}\right)$ and $L E T\left(r_{1}\right)$ are 3 . Then, the task $t_{2}$ has the largest priority among the residual tasks, and the $\operatorname{EST}\left(t_{2}\right)$ is 3 because $t_{1}$ is the predecessor of $t_{2}$. As $\operatorname{EST}\left(t_{2}\right) \geq L E T\left(r_{1}\right)$, the remaining tasks assigned to $r_{1}$ form a set $T S=\left\{t_{2}\right\}$. Since there are no other tasks on $r_{1}$, the task $r_{2}$ is directly assigned to the second position of $r_{1}$. Thus, $F T\left(t_{2}\right)$ is 12, $\operatorname{LET}\left(r_{1}\right)$ is updated to 12 , and $t_{4}$ becomes the task with the largest priority. As the resource $r_{7}$ can be used immediately, the start time of $t_{4}$ is 4 because it can receive the data from its predecessor $t_{1}$ at time 4 . Then, $F T\left(t_{4}\right)$ is 14, $\operatorname{LET}\left(r_{7}\right)$ is 14 , and the task $t_{3}$ becomes the task with the largest priority. The above procedure is repeated until all tasks have been assigned.

### 4.2 Global search strategy

The estimation of distribution algorithm (EDA) [41] constructs and updates the probability model by sampling the elite solutions in the population, and then the trial population is generated based on the probability model. The conventional EDA consists of the following steps: (1) Construct the probability model; (2) Generate the new population based on the probability model; (3) Evaluate the solutions in the new population; (4) Update the probability model based on the elite solutions. The above steps are repeated until the termination condition is satisfied.

### 4.2.1 Construction of probability model

Based on the above encoding and decoding scheme, this paper only considers the mapping relationships between tasks and virtual machines. Therefore, this paper constructs a univariate probability model $P$ to reflect the probability that each task $t_{i}$ is deployed to each resource $r_{j}$. We assume that the number of tasks is $n$ and the number of virtual machines is $m, p_{i, j}$ represents the probability that task $t_{i}$ is deployed to the resource $r_{j}$. Due to $P$ is constructed based on the average probability of tasks being assigned to a resource among multiple candidate solutions, and the average probability is a first-order statistic, the probability model $P$ is a univariate probability model. The probability model is shown as follows.
$P=\left[\begin{array}{cccc}p_{1,1} & p_{2,1} & \cdots & p_{n, 1} \\ p_{1,2} & p_{2,2} & \cdots & p_{n, 2} \\ \vdots & \vdots & \ddots & \vdots \\ p_{1, m} & p_{2, m} & \cdots & p_{n, m}\end{array}\right]$
In the initial phase, the probability $p_{i, j}$ is set to $1 / m$.

### 4.2.2 Update strategy of probability model

In KMOEDA, the external archive $\mathbb{L}$ is carried out to store the found non-dominated solutions. Therefore, the probability model is updated based on the elite solutions in $\mathbb{L}$. To make the probability model balance the historical information and the information of current elite solutions, the population-based incremental learning technique (PBIL) is applied for updating the probability model as shown in Eq. 15.
$p_{i, j}(t+1)=(1-\alpha) \times p_{i, j}(t)+\alpha \times I_{i, j}(t) /|\mathbb{L}|$
where $\alpha \in[0,1]$ denotes the learning rate, $I_{i, j}(t)$ represents the frequency that task $t_{i}$ is deployed to resource $r_{j}$. According to the previous literature [42], the PBIL is also a univariate method.

### 4.2.3 Construction of trial population

One of the essential elements of EDA is the creation of the trial population. Although the mapping relationships between tasks and resources can be well reflected by the probability model, solutions obtained by direct sampling will lose the structural information between tasks. Therefore, this paper introduces the reference template-based sampling approach [43] to construct the trial population. A random solution $\pi_{i}$ is first chosen from the external archive $\mathbb{L}$, and then $d \times n$ tasks mapping are randomly eliminated from $s_{i}$. Next, the removed tasks are re-deployed on the virtual machines in the resources pool using the probability model $P$ and roulette wheel selection technique. The procedure of global search strategy is described in Algorithm 1 .

```
Algorithm 2 Global search strategy
for \(\pi_{k} \in \mathbb{L}\) do
    \(P(t+1) \leftarrow\) Update \(P(t+1)\) according to \(\pi_{k}\) and \(P(t)\)
    end for
    for \(\pi_{k} \in T P\) do
        \(\pi_{\text {temp }} \leftarrow\) Choose reference template from \(\mathbb{L}\)
        \(\sigma \leftarrow\) Move \(d \times n\) task from \(\pi_{\text {temp }}\) to \(\sigma\).
        \(\pi_{k} \leftarrow \pi_{\text {temp }}\)
        for \(t_{i} \in \sigma\) do
            \(r_{\text {new }} \leftarrow\) Choose resource for \(t_{i}\) according to \(P(t+1)\)
            \(\pi_{k}\left(t_{i}\right) \leftarrow r_{\text {new }}\)
        end for
    end for
```

For example, suppose that $m$ is $7, n$ is 10, $\alpha$ is $0.5, d$ is 0.2 , and there are two solutions $s_{1}=\{1,1,4,7,6,3$, $2,4,6,2\}$ and $s_{2}=\{1,2,6,3,4,5,2,7,1,4\}$ in the external archive $\mathbb{L}$, each element of the probability model $P$ in the initial phase is $\frac{1}{7}$. The matrix $I$ can be constructed as follows.
$I=\left[\begin{array}{llllllllll}2 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0\end{array}\right]$
Then, the probability model $P$ can be updated as follows.
$P=\left[\begin{array}{cccccccccc}4 & 9 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 9 & 1 \\ 7 & 28 & 7 & 7 & 7 & 7 & 7 & 7 & 28 & 7 \\ 1 & 9 & 1 & 1 & 1 & 1 & 4 & 1 & 1 & 9 \\ 7 & 28 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 28 \\ 1 & 1 & 1 & 9 & 1 & 9 & 1 & 1 & 1 & 1 \\ 7 & 7 & 7 & 28 & 7 & 28 & 7 & 7 & 7 & 7 \\ 1 & 1 & 9 & 1 & 9 & 1 & 1 & 9 & 1 & 9 \\ 7 & 7 & 28 & 7 & 28 & 7 & 7 & 28 & 7 & 28 \\ 1 & 1 & 1 & 1 & 1 & 9 & 1 & 1 & 1 & 1 \\ 7 & 7 & 7 & 7 & 7 & 28 & 7 & 7 & 7 & 7 \\ 1 & 1 & 9 & 1 & 9 & 1 & 1 & 1 & 9 & 1 \\ 7 & 7 & 28 & 7 & 28 & 7 & 7 & 7 & 28 & 7 \\ 1 & 1 & 1 & 9 & 1 & 1 & 1 & 9 & 1 & 1 \\ 7 & 7 & 7 & 28 & 7 & 7 & 7 & 28 & 7 & 7\end{array}\right]$

Thus, the solution $s_{1}$ is chosen from $\mathbb{L}$ to be reference template, and 3 tasks $\sigma=\left\{t_{3}, t_{5}, t_{7}\right\}$ are randomly removed from $s_{1}$. Then, based on the roulette wheel selection technique, $t_{3}$ is re-deployed to $r_{6}, t_{5}$ is re-deployed to $r_{3}$, and $t_{7}$ is re-deployed to $r_{4}$. Thus, a new solution is generated. The above procedure should be performed on all solutions in the trial population.

### 4.3 Reliability-aware local search strategy

Since the reliability of task follows the Poison distribution, it can be concluded that the reliability of task is only related to the failure rate of virtual machines and the execution time of task. Then, the total reliability can be formulated as follow.
$R e l=\prod_{i=1}^{n} r e l\left(t_{i}\right)=e^{-\sum_{i=1}^{n} \lambda\left(r_{i} t_{i}\right) E T\left(t_{i}, r\left(t_{i}\right)\right)}$
Suppose that $\operatorname{Rel} \geq \delta_{\text {Rel }}$, then

$$
\sum_{i=1}^{n} \lambda\left(r_{i} t_{i}\right) E T\left(t_{i}, r\left(t_{i}\right)\right) \leq-\log \left(\delta_{\text {Rel }}\right)
$$

Therefore, the reliability constraint can be converted to a weighted execution time constraint. Since the failure rate of virtual machines is constant in a specified period, the reliability of a task decreases as the execution time increases. Therefore, a reliability-aware local search strategy is designed to search for feasible solutions near infeasible ones. The procedure of the local search strategy is described in Algorithm 3. First, the reliability constraint is converted to a weighted execution time constraint, and then the weighted execution time constraint is assigned to each task. The weighted execution time constraint $\delta_{w t\left(t_{i}\right)}$ of task $t_{i}$ can be calculated as follow.
$\delta_{w t\left(t_{i}\right)}=-w\left(t_{i}\right) / \sum_{i=1}^{n} w\left(t_{i}\right) \times \log \left(\delta_{R e l}\right)$
Second, the task list $T S\left(r_{j}\right)$ of each resource $r_{j}$ is constructed. Then, the total weighted execution time $w t\left(r_{j}\right)$ of each resource and the total weighted execution time constraint $\delta_{w t\left(r_{j}\right)}$ are obtained as follow.
$w t\left(r_{j}\right)=\sum_{i=1}^{|T S|} w t\left(t_{i}\right), T S=\left\{t_{i} \mid r\left(t_{i}\right)=r_{j}\right\}$

$$
\delta_{w t\left(r_{j}\right)}=\sum_{i=1}^{|T S|} \delta_{w t\left(t_{i}\right)}, T S=\left\{t_{i} \mid r\left(t_{i}\right)=r_{j}\right\}
$$

Then, the resources are sorted according to $\Delta w t\left(r_{j}\right)=\delta_{w t\left(r_{j}\right)}-w t\left(r_{j}\right)$. The resources with maximum $\Delta w t\left(r_{j}\right)$ are iteratively chosen to modify the instance until the weighted execution time satisfies the constraint. The procedure of the local search strategy is shown in Algorithm 3.
another resource with the instance of $p_{5}$. Then, the reliability of the schedule is calculated again. This procedure is repeated until the reliability of the schedule meets the userdefined reliability constraint.

### 4.4 Elite enhancement strategy

To further explore the problem space deeply, this paper applies an elite enhancement strategy to improve the

```
Algorithm 3 Reliability-aware local search strategy
    Calculate \(\delta_{w t\left(t_{i}\right)}\) of each task
    for \(t_{i} \in T\) do
        Add \(t_{i}\) into \(T S\left(r\left(t_{i}\right)\right)\)
    end for
    for \(r_{j} \in R\) do
        Calculate \(\Delta w t\left(r_{j}\right)\) of each resource
    end for
    Sort resources according to \(\Delta w t\left(r_{j}\right)\)
    for \(r_{j} \in R\) do
        for \(p_{k} \in P\) do
            Calculate \(\Delta w t\left(r_{j}\right)\) when \(p\left(r_{j}\right)=p_{k}\)
            if \(\Delta w t\left(r_{j}\right) \leq 0\) then
                Move \(T S\left(r_{j}\right)\) from \(r_{j}\) to another resource with \(p_{k}\)
                Break
            end if
        end for
        if \(\operatorname{Rel} \geq \delta_{\text {Rel }}\) then
            Break
        end if
    end for
```

Suppose that the user-defined reliability threshold $\delta_{\text {Rel }}$ is $50 \%$, and the failure rate $\lambda$ of the resources are $\{0.1,0.07,0.03,0.02,0.008,0.006,0.001\}$. According to Eq. 20, the weighted execution time constraints of tasks are $\{0.0352,0.1057,0.0117,0.1175,0.0587,0.0940,0.1292$, $0.0822,0.0352,0.0235\}$. For solution $s_{1}$ shown in section 4.2.3, the actual weighted execution time of the tasks are $\{0.3,0.9,0.02,0.01,0.03,0.24,0.77,0.14,0.018,0.14\}$. Furthermore, the weighted execution times of resources and the weighted execution time constraint are $\{1.2,0.91$, $0.24,0.16,0,0.048,0.01\}$ and $\{0.1409,0.1527,0.094$, $0.0939,0,0.0939,0.1175\}$. Then, it can be obtained that $\Delta_{w t\left(r_{j}\right)}=\{-1.0591,-0.7573,-0.1460,-0.0661,0,0.0459$, $0.1075\}$. Due to $\Delta_{w t\left(r_{1}\right)}$ is the smallest, the $r_{1}$ is firstly chosen to change the instance of the resource. For the tasks $t_{1}$ and $t_{2}$ on resource $r_{1}$, it can be calculated that the weighted execution times on all instances are $\{1.2000$, $0.8400,0.3600,0.2400,0.0960,0.0720,0.0120\}$. Obviously, when the instance of $r_{1}$ is $p_{5}, \Delta_{w t\left(r_{1}\right)}$ is larger than zero. Therefore, the tasks $t_{1}$ and $t_{2}$ are moved from $r_{1}$ to
quality of non-dominated solutions in $\mathbb{L}$. The elite enhancement strategy consists of two perturbation operators, i.e., task perturbation and resource perturbation.

- Task perturbation first calculates the critical path of the solution, and then a random task on the critical path is moved to a random resource. This operator can effectively disturb the total execution time with constant total execution cost.
- Resource perturbation first chooses a random resource on which at least one task is deployed, and then move all tasks deployed on this resource to another virtual machine. This operator can effectively disturb the total execution cost.
In each iteration, two random solutions in $L$ are carried out to perform the elite enhancement strategy. The task perturbation is performed on the first solution, and the resource perturbation is executed on the second solution. Suppose that the solutions $s_{1}$ and $s_{2}$ shown in section 4.2.3 are chosen to perform the elite enhancement strategy. The critical path of $s_{1}$ is $\left\{t_{1}, t_{2}, t_{6}, t_{7}, t_{1} 0\right\}$, and a random task $t_{6}$

is moved from $r_{3}$ to $r_{2}$. Therefore, the data communication between $t_{6}$ and $t_{7}$ becomes zero, and the total execution time of $s_{1}$ is reduced. Then, it can be observed that there are seven resources used in $s_{2}$. First, a random resource $r_{2}$ is chosen. The tasks assigned to $r_{2}$ are $\left\{t_{2}, t_{7}\right\}$. Second, tasks $t_{2}$ and $t_{7}$ are moved from $r_{2}$ to a random resource $r_{7}$. Thus, there is no task on $r_{2}$.

### 4.5 External archive

The output of the KMOEDA algorithm is a set of nondominated solutions, that is, there is no solution that the execution time, cost, and reliability are superior to the other solutions at the same time. Therefore, the external archive $\mathbb{L}$ is applied to preserve the non-dominated solutions found during the iterations.

### 4.5.1 Initialization of external archive

Numerous previous studies have demonstrated that solid initial solutions can significantly accelerate the convergence speed and increase the quality of solution [44, 45]. Therefore, this paper applies two heuristics to initialize the external archive. First, all tasks are deployed to the same resource for execution. For $k$ available instances, we can obtain $k$ init solutions. Second, a solution is constructed based on the popular HEFT algorithm. Therefore, the initial external archive contains $k+1$ solutions.

### 4.5.2 Update strategy of external archive

In each iteration, we can obtain $p s+2$ solutions after the global search strategy and the local search strategy. First, the trial population $T P$ and the external archive $\mathbb{L}$ are emerged, then the non-dominated fast sorting technique [46] is performed to generate the non-dominated solutions set. When the number of solutions in the non-dominated solutions set is larger than $r s$, the crowding distance [46] is employed to sort the solutions, and then the $r s$ solutions with larger distance are remained in external archive $\mathbb{L}$.

### 4.6 Framework of KMOEDA

Based on the above components, this paper proposes a knowledge-based multi-objective distributed estimation algorithm (KMOEDA). The flowchart of KMOEDA is shown in Fig. 3. First, the external archive is constructed based on the heuristics, and the probability model is initialized. Second, the mapping relationship between tasks and virtual machines in the external archive is counted, and then the probability model is updated. Based on the
![img-1.jpeg](img-1.jpeg)

Fig. 3 The flowchart of KMOEDA
probability model and the reference templates, the trial population is constructed. Moreover, the elite enhancement strategy is performed to generate two improved elite solutions. For the solutions which violate the reliability in the trial population, the reliability-aware local search strategy is applied to search for feasible solutions. Next, the external archive is updated. The above procedure is repeated until the termination criterion is met.

### 4.7 Computational complexity

Suppose that the workflow $G$ is made up of $n$ tasks, the resources pool contains $m$ virtual machines, and there are $p$ instances in the cloud environment. Let $s$ denotes the size of the external archive, and $k$ represents the size of the trial population. In the initialize phase, the computational complexity of the init external archive is $O\left(p n+m n^{2}\right)$, and the computational complexity of the init probability model is $O(m n)$. Therefore, the total computational complexity of initializing phase is $O\left(p n+m n^{2}+m n\right)$. In each iteration, the computational complexity of updating the probability model is $O(s n)$, and the computational complexity of constructing the trial population is $O(k m n)$. In the elite enhancement strategy, the computational complexity of searching critical path is $O(n)$. Therefore, the computational complexity of the elite enhancement strategy is

$O(n+2)$. The computational complexity of the reliabilityaware local search strategy is $O(p n)$, and the computational complexity of the decoding strategy is $O\left(n^{2}\right)$. The computational complexity of the fitness function is $O\left(n^{2}\right)$, and the computational complexity of the non-dominated sorting approach is $O\left(2 s^{2}\right)$. Therefore, the computational complexity of KMOEDA in $g$ iterations is as follows.

$$
\begin{aligned}
O(W) & =O\left(p n+m n^{2}+m n\right) \\
& +O(g(s n+m n+n+2)) \\
& +O\left(g\left((k+2)\left(p n+2 n^{2}\right)+2 s^{2}\right)\right)
\end{aligned}
$$

In the worst case, the number of virtual machines $m$ is equal to $p n$. For the large-scale workflows, $n$ is over larger than $p$. Therefore, the computational complexity of KMOEDA is

Table 2 Configurations of the instances

$$
\begin{aligned}
O(W) & =O\left(p n+p n^{3}+p n^{2}\right) \\
& +O\left(g\left(s n+p n^{2}+n+2\right)\right) \\
& +O\left(g\left((k+2)\left(p n+2 n^{2}\right)+2 s^{2}\right)\right) \\
& \approx O\left(p n^{2}+g p n^{2}+(2 k+4) g n^{2}\right) \\
& \approx O\left((2 k+p+4) g n^{2}\right)
\end{aligned}
$$

## 5 Experimental study

### 5.1 Experimental setup

To evaluate the effectiveness of the proposed KMOEDA, we compared the proposed KMOEDA with several related algorithms in the same experimental environment. The configurations of instances in the experiment is simulated with reference to six virtual machines on Amazon EC2 cloud platform. The billing time unit is set to $1 h$. The details of the configurations of virtual machines are described in Table 2.

Four scientific workflows, i.e., CyberShake, Montage, Inspiral, and Sipht, were employed in this experiment as workflow cases. These workflows are frequently utilized in the assessment of workflow scheduling algorithms [47]. Figure 4 depicts the topology structures of these workflows. The workflowSim is utilized to simulate the scheduling environment in the cloud environment. To

Fig. 4 The structures of the four workflows
![img-2.jpeg](img-2.jpeg)

make a fair comparison, all algorithms are coded by Java 1.8 and run on the server with two Intel(R) Xeon(R) E5-2650-V3@2.30GHz processors and 128 G of RAM under Linux CentOS release 6.5.

The experiment is made up of three aspects: (1) Parameter calibration of KMOEDA; (2) Ablation analysis of the components; (3) Comparison of KMOEDA and related multi-objective algorithms. Since RCMOWSP was not considered in previous research, the reliability constraint is established as follows.
$\delta_{\text {Rel }}=\prod_{i=1}^{n} \max \left(\left\{\left.\left(e l\left(t_{i}, p_{k}\right) \right\rvert\, p_{k} \in I\right\}\right) \times 75 \%\right.$
where $\operatorname{rel}\left(t_{i}, p_{k}\right)$ represents the reliability of task $t_{i}$ on the virtual machines with the type of $p_{k}$. We set the reliability constraint as the $75 \%$ of maximum reliability. Moreover, because KMOEDA and the compared algorithms are stochastic approaches, all algorithms run independently for 30 times. Considering that the scale of problem space increases with the increase of workflow size, the termination criterion of each run is set to $100 n$.

### 5.2 Performance metrics

Due to the considered RCMOWSP is essentially a multiobjective optimization problem, It is difficult to evaluate the performance of algorithms based on a comparison of isolate schedules. hypervolume and set coverage [48] are two popular performance metrics for evaluating the multiobjective optimization algorithms. Therefore, this paper applies hypervolume and set coverage to measure the nondominated solutions obtained by the implemented algorithms.
(1) Hypervolume. It measures quality of a given Pareto set $S$ by calculating the hypervolume of points. A reference point $(1.2,1.2)$ is employed to close the volume. Therefore, the closer the hypervolume value is to 1.44 , the better $S$ is. Then, TET and TEC are
normalized to a number within [0, 1]. Next, the hypervolume is calculated as follows.
hypervolume $(S)=\sum_{i=1}^{2} \sum_{j=1}^{|S|} \frac{f_{i}\left(s_{j}\right)-f_{i}^{\min }}{f_{i}^{\max }-f_{i}^{\min }}$
where $s_{j}$ is the $j$ th solution in $S . f_{1}\left(s_{j}\right)$ and $f_{2}\left(s_{j}\right)$ are TET and TEC of the solution $s_{j} . f_{i}^{\min }$ and $f_{i}^{\max }$ are the minimum and maximum values of $i$ th objective.
(2) Set Coverage $(C(A, B))$. It reflects the dominance relationship between the two Pareto set $A$ and $B$. The set coverage is calculated as follows.
$C(A, B)=\frac{|\{b \in B \mid \exists a \in A, a \preceq b\}|}{|B|}$
where $A$ and $B$ are two Pareto sets. The closer $C$ $(A, B)$ is to 1 , the better the quality of $A$.

### 5.3 Parameter calibration

The parameters of the KMOEDA are calibrated using the full factorial design of the experiment. The levels of the parameters of KMOEDA are the population size $p s=\{5,10,15,20,25,30\}, \quad r s=\{10,20,30,40,50,60\}$, $d=\{0.1,0.2,0.3,0.4,0.5,0.6\}, \quad$ and $\quad \alpha=\{0.3,0.4,0.5$, $0.6,0.7,0.8\}$. It would result in $6 \times 6 \times 6 \times 6=1296$ configurations. All configurations are run on the Montage workflow with 25 tasks, and each configuration run 5 times independently. Table 3 provides the analysis of variance (ANOVA) results of hypervolume. The $p$-values $<0.05$ are marked bold to demonsrate that the corresponding parameter is significant to the KMOEDA.

As shown in Table 3, $p s, r s$, and $d$ have a significant effect on the performance of KMOEDA. The size of the external archive $r s$ has the largest impact on the performance of KMOEDA because it has the highest F-Ratio. From the main effect plot of $r s$, it can be seen that the best value of $r s$ is 30 , and the worst value of $r s$ is 10 . The small

Table 3 ANOVA Results for parameters calibration

Fig. 5 Main effect plots of parameters
![img-3.jpeg](img-3.jpeg)

Fig. 6 Interaction effect plots between parameters
![img-4.jpeg](img-4.jpeg)

Table 4 Average hypervolume of ablation analysis

external archive results in insufficient distribution of the non-dominated solution set, and then the probability model cannot reflect the objective space. Additionally, the small external archive will lead to insufficient reference templates, which will significantly reduce the diversity of the population. The over large external archive can accommodate more non-dominated solutions with the reduced convergence speed. As seen from Table 3, the interactions between $r s$ and $d$ have a significantly impact on the performance of KMOEDA because the corresponding $p$-value
is smaller than 0.05 . Therefore, the value of $r s$ is set to 40 according to the interaction effect plot.

From Table 3, the $p$-value of $d$ is also smaller than 0.05 , and its F-Ratio is only smaller than that of $r s$. Therefore, $d$ has a significant effect on the performance of KMOEDA. To be specific, the over large value of $d$ means that more tasks should be re-deployed according to the probability model, and then reduce the convergence speed. Therefore, it can be seen from Fig. 5 that the best value of $d$ is 0.1 . From Table 3, the interaction relationships between $d$ and $r s, d$ and $p s$ have significant impact on the performance of KMOEDA. Since the interaction between $r s$ and $d$ has a larger F-Ratio, the value of $d$ is set to 0.1 according to the interaction effect plot.

From Table 3, the impact of $p s$ on the performance of KMOEDA ranks third. The large size of the population will result in fewer probability model updates, which will lower the accuracy of the probability model. As depicted in Fig. 5, KMOEDA performs best with a small $p s$ of 5.

![img-5.jpeg](img-5.jpeg)

Fig. 7 Pareto fronts of KMOEDA and its variants on Sipht with 100 tasks

Additionally, the value of $p s$ is determined by the interaction relationship between $p s$ and $d$ because it significantly affects the performance of KMOEDA. As seen from Fig. 6, the best value of $p s$ is 10 . Moreover, the learning rate $\alpha$ has no significant effect on the performance of KMOEDA, and it has no interaction effect with other parameters. Therefore, the value of $\alpha$ is set to 0.4 according to Fig. 5. As above results and analysis, the parameters are set as follows: $p s=10, r s=40, d=0.1$, and $\alpha=0.4$.

### 5.4 Ablation analysis

The impact of the core components on the performance of KMOEDA is further compared and examined in this section. The core components of KMOEDA include the initialization strategy, global search strategy, reliability-aware local search strategy, and elite enhancement strategy. Therefore, four variants of KMOEDA are constructed based on the above four components to be compared with KMOEDA. To verify the effect of the initialization strategy, a variant KNI replaces the initialization strategy with a random initialization approach. KNG removes the global search strategy to evaluate the effect of the global search strategy on performance. KNL removes the elite enhancement strategy to test the effect of the elite enhancement strategy on the performance of KMOEDA. KNR removes the reliability-aware local search strategy to confirm the effectiveness of the local search strategy. The above variants and KMOEDA are run 30 times independently with the same experimental environment and termination criterion. The CyberShake, Inspiral, Montage, and Sipht with 100 tasks are carried out to be the benchmark. The experimental results are reported in Table 4. The maximum values of hypervolume in each row are marked bold.

It can be seen from Table 4 that the average hypervolume of KMOEDA is superior to the other variants. Therefore, all of the components contribute to the performance of KMOEDA. To be specific, KNG performs the poorest, which demonstrates that the global search strategy significantly enhances the performance of KMOEDA. The performance of KNI is marginally better than KNG but poorer than KNR and KNL. The reason is that the distribution of the initialization solutions within the problem space has a significant effect on the probability model, and then the poor initialization solutions will reduce the effectiveness of the global search strategy. The performance of KNR and KNL are similar, but both are inferior to KMOEDA. This demonstrates the reliability-aware local search strategy and the elite enhancement strategy can effectively enhance the performance of KMOEDA.

As the above experimental results and analysis, KMOEDA can balance diversity and convergence well by using the components. The Pareto front obtained by KMOEDA and other variants on the Sipht workflow with 100 tasks is depicted in Fig. 7.

### 5.5 Comparison of other related algorithms

This section compares the proposed KMOEDA with five multi-objective optimization algorithms: EMS-C [16], NSGA-II [46], MOHEFT [35] ch-PICEA-g [38], and L_MaOPSO [39] to verify the effectiveness of KMOEDA on RCMOWSP. MOHEFT is a heuristic for solving the biobjective workflow scheduling problem in the cloud environment. EMS-C, ch-PICEA-g, and L_MaOPSO are metaheuristics for solving the multi-objective workflow scheduling problem in the cloud environment. NSGA-II is a popular multi-objective optimization algorithm. Therefore, the effectiveness of KMOEDA for solving the RCMOWSP can be adequately verified when compared to the above algorithms.

The benchmark is made up of below workflows: (1) CyberShake workflow with 30, 50, 100, and 1,000 tasks; (2) Inspiral workflow with 30, 50, 100, and 1,000 tasks; (3) Montage workflow with 25, 50, 100, 1,000 tasks; (4) Sipht workflow with 30, 60, 100, and 1,000 tasks. The aforementioned workflows are frequently carried out to test the performance of workflow scheduling algorithms. To make a fair comparison, all algorithms share the same termination criterion, which is the maximum number of function evaluations. Additionally, all algorithms were run 30 times independently. The average hypervolume and set coverage are displayed in Tables 5, 6, 7. The maximum values of hypervolume and set coverage are marked bold. In Tables 6 and $7, C(-, A)$ represents the coverage of KMOEDA to the compared algorithm $A$, and $C(A,-)$ denotes the coverage of the compared algorithm $A$ to

Table 5 Average hypervolume of KMOEDA and compared algorithms

Table 6 Average set coverage between KMOEDA and compared algorithms

KMOEDA. Due to the high space complexity and memory requirement of MOHEFT, the experimental results of MOHEFT on the extra large-scale workflows are not provided.

It can be observed from Table 5 that the average hypervolume obtained by KMOEDA is superior to that of the other compared algorithms on most of the instances. However, the hypervolume of KMOEDA is slightly smaller than that of EMS-C on the Montage workflow with 100 tasks. On the Montage with 1000 tasks, the hypervolume of KMOEDA is marginally lower than that of I_MaOPSO. Table 5 further shows that the gap between the hypervolume of KMOEDA and that of other algorithms
rapidly widens with the size of workflow increases. The influence of reliability constraints on the problem space increases as the size of workflow increases. The problemspecific strategies of KMOEDA can effectively enhance performance of KMOEDA. Table 5 further demonstrates that the hypervolume of KMOEDA is higher than that of compared algorithms EMS-C, NSGA-II, MOHEFT, chPICEA-g, and I_MaOPSO by $4.34,38.93,6.65,29.76$, and $7.33 \%$, respectively. The mean values of hypervolume with $95 \%$ LSD interval are shown in Fig. 8.

The average set coverage between KMOEDA and other compared algorithms is reported in Tables 6 and 7. From Tables 6 and 7, it can be observed that the KMOEDA has

Table 7 Average set coverage between compared algorithms and KMOEDA

Fig. 8 Mean value of hypervolume with $95 \%$ LSD interval


![img-6.jpeg](img-6.jpeg)

Fig. 9 Pareto fronts of KMOEDA and other algorithms on CyberShake
![img-7.jpeg](img-7.jpeg)

Table 8 Statistical results of Wilcoxon's test
more set coverage on other compared algorithms than the compared algorithms do non most test instances. On the Montage with 100 and 1,000 tasks, the set coverage of KMOEDA is lower than less than EMS-C and chi-PIECAg , respectively. On the Montage with 100 tasks and the Sipht with 30 tasks instances, the set coverage of KMOEDA is smaller than MOHEFT. However, the experimental results in most of the instances still demonstrate the superior performance of KMOEDA. The Pareto fronts obtained by KMOEDA and other compared algorithms are shown in Fig. 9.

To further investigate the performance disparity between KMOEDA and the compared algorithms, we apply Wilcoxon's test to verify the significant difference between the comparison algorithms. The results of Wilcoxon's test are displayed in Table 8. The $p$-values $<0.05$ are marked bold to demonstrate that the KMODEA is significantly superior to the compared algorithms. Since the $p$-values between KMOEDA and other compared algorithms are less than 0.05 , it can be concluded that

KMOEDA is significantly superior to EMS-C, NSGA-II, MOHEFT, ch-PICEA-g, and I_MaOPSO with $95 \%$ confidence level.

Based on the experimental results and analysis, it can be observed that the proposed KMOEDA can effectively solve the RCMOWSP. In fact, the proposed KMOEDA still follows the current universal framework of meta-heuristics, which includes initialization strategy, global search strategy, and local search strategy. However, in KMOEDA, the global and local strategies are design based on the characteristics of the problem, especially for reliability-aware local search strategies. The collaboration of these problem-specific strategies can effectively contribute to improving the convergence and diversity of non-dominated solutions when compared to the other existing algorithms for the related problems.

## 6 Conclusions and future work

This paper proposes a knowledge-based multi-objective estimation of distribution algorithm (KMOEDA) to solve a novel workflow scheduling problem, i.e., reliability-constrained multi-objective workflow scheduling problem (RCMOWSP) with the objectives of minimizing execution time and cost subject to reliability constraint. The computational experiments and comparative results with several related algorithms demonstrate that KMOEDA is more effective in solving RCMOWSP whether on small-scale or large-scale workflows. The superior performance of

KMOEDA is attributed to the aspects below: 1) The initialization strategy constructs the initial solutions in a promising area. 2) The global search strategy uses the probability model to maintain the diversity of the population well. 3) The reli-ability-aware search strategy can effectively handle unfeasible solutions. 4) The elite enhancement strategy performs well based on the elite solutions in the external archive.

The following three directions will be investigated in subsequent studies. First, the multi-objective workflow scheduling problem with multi-billing mechanism will be deeply studied. Second, the real-time fault-tolerant largescale workflow scheduling problem should be further researched. Additionally, it is necessary to apply machine learning approaches to solve the multi-objective workflow scheduling problem in a cloud environment.

Author contributions ML and SQ wrote the main manuscript text and prepared all figures. All authors reviewed the manuscript.

Funding Not applicable.
Data availability The data presented in this study are available on request from the corresponding author.

## Declarations

Conflict of interest The authors declare that they have no conflict of interest.
