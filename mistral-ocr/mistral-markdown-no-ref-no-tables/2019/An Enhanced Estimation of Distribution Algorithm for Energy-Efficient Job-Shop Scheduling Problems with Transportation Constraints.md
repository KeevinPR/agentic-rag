# Article 

## An Enhanced Estimation of Distribution Algorithm for Energy-Efficient Job-Shop Scheduling Problems with Transportation Constraints

Min Dai ${ }^{1, *}$, Ziwei Zhang ${ }^{1}$, Adriana Giret ${ }^{2}$ and Miguel A. Salido ${ }^{2}$<br>1 College of Mechanical Engineering, Yangzhou University, Yangzhou 225127, China; yzuzhangziwei@163.com<br>2 Departamento de Sistemas Informáticos y Computación/AI2, Universitat Politècnica de València, Camino de Vera s/n, 46022 Valencia, Spain; adjibog@upvnet.upv.es (A.G.); msalido@dsic.upv.es (M.A.S.)<br>* Correspondence: daimin@yzu.edu.cn

Received: 30 April 2019; Accepted: 29 May 2019; Published: 31 May 2019


#### Abstract

Nowadays, the manufacturing industry faces the challenge of reducing energy consumption and the associated environmental impacts. Production scheduling is an effective approach for energy-savings management. During the entire workshop production process, both the processing and transportation operations consume large amounts of energy. To reduce energy consumption, an energy-efficient job-shop scheduling problem (EJSP) with transportation constraints was proposed in this paper. First, a mixed-integer programming model was established to minimize both the comprehensive energy consumption and makespan in the EJSP. Then, an enhanced estimation of distribution algorithm (EEDA) was developed to solve the problem. In the proposed algorithm, an estimation of distribution algorithm was employed to perform the global search and an improved simulated annealing algorithm was designed to perform the local search. Finally, numerical experiments were implemented to analyze the performance of the EEDA. The results showed that the EEDA is a promising approach and that it can solve EJSP effectively and efficiently.


Keywords: job-shop scheduling; energy consumption; estimation of distribution algorithm; transportation time

## 1. Introduction

As is well known, reducing energy consumption and its associated environmental impacts is one of the most important challenges for manufacturing industries. In China, the energy efficiency of traditional manufacturing enterprises is low and the related pollution emissions are very high. According to relevant surveys, the average proportion of industrial GDP is obtained by consuming $67.9 \%$ of the national electricity energy and emits $83.1 \%$ of the national carbon dioxide [1]. Hence, one of the most effective ways to develop energy-savings mechanisms and methods is to optimize the energy efficiency of the production process for manufacturing enterprises [2,3].

Researchers have come to realize that workshop scheduling could play an important role in reducing energy consumption during manufacturing processes. In recent years, there has been an increasing number of studies on production scheduling integrated with energy efficiency in the literature [4-6]. Energy-related production scheduling can mainly be divided into three aspects: energy-aware single-machine scheduling, energy-aware flow-shop scheduling, and energy-aware job-shop scheduling.

Regarding energy optimization of single-machine scheduling, Che et al. [7] proposed an energy-efficient single-machine scheduling model regarding total energy consumption and maximum tardiness. In order to reduce the total penalty costs and total energy consumption costs, Lee et al. [8]

developed an efficient dynamic control algorithm to enable an energy-efficient single-machine scheduling problem. Rubaiee and Yildirim [9] addressed an energy-aware multi-objective ant colony algorithm for solving a single-machine pre-emptive scheduling problem with consideration of the total completion time and energy cost. In the aspect of energy optimization of flow-shop scheduling, Zhang et al. [10] proposed an improved strength Pareto evolutionary algorithm to study energy-efficient flexible flow-shop scheduling under time of use electricity tariffs. Li et al. [11] addressed the hybrid flow-shop scheduling problem with consideration of setup energy consumption and developed an efficient multi-objective optimization algorithm to solve it. Lu et al. [12] developed a multi-objective backtracking search algorithm for solving the energy-efficient scheduling problem with controllable transportation times. Fu et al. [13] proposed a stochastic energy-conscious distributed permutation flow-shop scheduling model with the aim of minimizing the makespan and total energy consumption. Schulz et al. [14] presented a new multiphase iterated local search algorithm to investigate the energy-aware hybrid flow-shop scheduling model with three objectives: makespan, total energy costs, and peak load.

In comparison, research on energy optimization of job-shop scheduling has attracted increasing attention. Liu et al. [15,16] investigated a bi-objective energy-aware job-shop scheduling problem that minimized both the total weighted tardiness and the total electricity consumption. May et al. [17] designed a green genetic algorithm to solve the job-shop scheduling problem with consideration of energy consumption and makespan. Zhang and Chiong [18] analyzed an energy-efficient job-shop scheduling problem with the total weighted tardiness as well as the comprehensive energy consumption in order to minimize the energy consumption and makespan, and Salido et al. [19] studied an extended energy-conscious job-shop scheduling problem with different processing speeds of machines. Moreover, Masmoudi et al. [20] established two integer linear programming models for the job-shop scheduling problem with consideration of energetic aspects. Afterward, Mokhtari and Hasani [21] studied an energy-efficient scheduling of both production and maintenance operations with the objective of total completion time, total availability of the system, and energy consumption in a flexible job-shop environment. Meng et al. [22] formulated new mixed-integer linear programming models to address the energy-aware flexible job-shop scheduling problem. In addition, Dai et al. [23] modeled a multi-objective energy-efficient flexible job-shop schedule with the aim of optimizing energy consumption and makespan.

In the abovementioned studies, the studies focused on optimizing the processing operations between tasks and machines. However, the transportation of tasks between machines is a non-negligible operation in a real-world production environment. In real production scheduling, after one task in the schedule finishes its processing operation on a machine, transportation equipment such as an Automated Guided Vehicle (AGV) transports the task to the next machine for processing. Due to the consideration of transportation constraints, the complexity of the workshop scheduling problem increases severely. Researchers have also investigated the impact of transportation resources on the workshop scheduling problem. Lacomme et al. [24] designed a framework for the joint scheduling problem regarding the simultaneous scheduling of machines and AGVs with the objective of minimizing the makespan. Nageswararao et al. [25] introduced integrated scheduling of machines and AGVs with minimization of mean tardiness and proposed a binary particle swarm vehicle heuristic algorithm to solve it. Saidi-Mehrabad et al. [26] established a new mathematical model regarding integrated job shop scheduling and conflict-free routing of AGVs, and developed a two-stage ant colony algorithm to study the problem. Guo et al. [27] analyzed the integrated production and transportation scheduling problem and developed a bi-level evolutionary optimization approach for solving the problem. Karimi et al. [28] formulated two mixed-integer linear programming models for the flexible job-shop problem with consideration of transportation times. In addition, to minimize both the comprehensive energy consumption and makespan, Liu et al. [29] proposed a mixed-integer programming model of the integrated flexible job-shop scheduling and crane transportation. Although scholars have studied the impact of transportation constraints on workshop scheduling, these studies have almost always

centered on the optimization of the production objectives like makespan. To the best of our knowledge, only three relatively related research articles considered energy-efficient scheduling optimization of integrated processing and transportation equipment [12,23,29].

There are strong interactions between processing and transportation operations in production scheduling [29]. When AGVs are required to transfer the jobs after finishing operations of the jobs, their transportation times may result in different waiting times for machines. Moreover, the different operation sequences of all tasks on each machine considers the different transportation routes of AGVs. In addition, in the production process, both machines and AGVs generate a certain amount of energy consumption. From the viewpoint of energy savings, the optimization of the integrated scheduling of machines and AGVs could be considered an efficient strategy for manufacturing enterprises to reduce energy consumption [23].

To summarize, different kinds of workshop scheduling problems have been discussed in the literature with regard to energy efficiency. During the entire workshop production process, both the processing and transportation operations consume large amounts of energy. On the other hand, transportation operations are an indispensable part of production scheduling, and an integrated optimization scheduling of machines and AGVs is needed for actual production. Therefore, on the basis of the studies mentioned above, an energy-efficient job-shop scheduling problem with transportation constraints is investigated for the following reasons. First, it fills a gap in the literature, since job-shop scheduling problems with transportation constraints (such as transportation time) have not been well investigated with regard to energy efficiency. Second, to evaluate different performance criteria in practical situations, the further improvement of optimization algorithms is conducted to make them more effective and efficient to search for better solutions. In this work, an enhanced estimation of distribution algorithm (EEDA) was developed for solving the energy-efficient job-shop scheduling problem (EJSP).

The remaining sections of this paper are organized as follows. Section 2 introduces the energy-efficient scheduling problem with transportation time and devises a meta-heuristic algorithm to solve the scheduling problem. Section 3 formulates a mixed-integer programming (MIP) model for the EJSP. Section 4 designs the comprehensive experiments to analyze the performance of the proposed model and algorithm. Section 5 reports the discussion, and Section 6 summaries the conclusions and future works.

# 2. Problem Description and Method 

### 2.1. Problem Description

An energy-efficient job-shop scheduling problem with transportation constraints can be described as follows. There are a set of $n$ tasks $T=\left\{T_{1}, T_{2}, \ldots, T_{n}\right\}$ and a set of $m$ machines $M=\left\{M_{1}, M_{2}, \ldots, M_{m}\right\}$. Each task $T_{i}$ consists of a sequence of $N_{i}$ operations $\left(O_{i 1}, O_{i 2}, \ldots, O_{i N_{i}}\right)$. All the operations must be executed by $m$ machines in a fixed order. Once one operation $O_{i j}$ of a task $T_{i}$ completes its processing operation on a machine $M_{\omega}$, an empty AGV transfers the task to the next machine $M_{\omega}$ for processing. In the entire production process, both machines and AGVs consume energy for supporting production activities. The challenge is to determine the operation sequence on each machine to satisfy schedule efficiency that is measured in terms of makespan and energy efficiency that is calculated by the comprehensive energy required for a schedule. It is calculated by the comprehensive energy required for a schedule. For instance, as shown in Figure 1, there are three tasks and three machines. Each task has three operations, and the processing routings for them are $M_{3}-M_{1}-M_{2}, M_{2}-M_{3}-M_{1}$, and $M_{3}-M_{2}-M_{1}$, respectively. At the same time, the corresponding transportation times are collected. During the production process, each machine will consume energy to process each operation of the tasks, and AGVs will also consume energy to move the tasks. The objective of the EJSP is to find an effective and efficient schedule that minimizes the makespan and energy consumption. The EJSP satisfies the following assumptions.

![img-0.jpeg](img-0.jpeg)

Figure 1. An example schedule.
(1) Each task is available at time zero.
(2) Each machine is available at time zero.
(3) The precedence relationships between operations for each task cannot be changed.
(4) Each machine can only process an operation of one task at a time.
(5) Once an operation begins, the operation cannot be interrupted until it is completed.
(6) There are enough AGVs responsible to move each task.
(7) Handling times of all tasks between machines and AGVs are ignored.

# 2.2. Enhanced Estimation of Distribution Algorithm (EEDA) 

Due to the strongly NP-hard nature of the job-shop scheduling problem (JSP), many optimization approaches such as meta-heuristic algorithms have been developed to obtain optimal and suboptimal solutions. It should be noted that although meta-heuristic approaches have been shown to be effective in solving the JSP with the consideration of energy efficiency [17,18,30], the solution quality will become less satisfactory, especially when transportation constraints are added to the scheduling model. The estimation of distribution algorithm (EDA), as an evolutionary algorithm, has received increasing interest in solving many complex optimization problems such as production scheduling problems [31-33].

In this section, an enhanced hybrid algorithm based on a combination of estimation of the distribution algorithm (EDA) and simulated annealing algorithm (SAA) is developed for solving the problem. In the literature, a variety of meta-heuristic algorithms have been used to solve JSP, including the genetic algorithm (GA), simulated annealing algorithm (SAA), estimation of distribution algorithm (EDA), particle swam optimization (PSO), etc. Among these algorithms, the EDA has the ability of global exploration and can quickly approach the optimization solution, but a fatal shortcoming is that its local exploitation ability is limited. Fortunately, SAA has a strong exploitation ability and can jump out of the local optimization to search for the best solution. Therefore, this paper proposes to incorporate the advantages of the SAA into the EDA. The EDA based on global information search is developed to rapidly obtain optimal or near-optimal solutions in the solution space, and then the SAA based on local information search is employed to seek better ones in terms of the solutions.

### 2.2.1. Representation

In this section, an encoding scheme based an operation representation is employed to study the EJSP with $n$ tasks and $m$ machines. For the EJSP, its encoding sequence consists of a series of tasks' numbers and its encoding length ( $l$ ) equals $n \times m$. In the encoding sequence, different appearances of the same task number denote different operations of the task, and the $j^{\text {th }}$ appearance represents the $j^{\text {th }}$ operation of the task.

Example 1: Consider that the tasks are to be processed on three machines and each task has three operations, as shown in Figure 1. An encoding sequence (1 32231132 ) is yielded randomly. Here, 1,2 , and 3 represent the task number of $T_{1}, T_{2}$, and $T_{3}$, respectively. Moreover, take task $T_{1}$ for an example, there are three different appearances (i.e., the 1st, 6th, and 7th position) in the sequence, which means $T_{1}$ has three operations. The 1st position of the encoding sequence represents the first operation $\left(O_{11}\right)$ of $T_{1}$; the 6th position of the encoding sequence represents the second operation $\left(O_{12}\right)$ of $T_{1}$; the 7th position of the encoding sequence represents the third operation $\left(O_{13}\right)$ of $T_{1}$. Thus, the corresponding operation sequence of the encoding sequence is $\left(O_{11}, O_{31}, O_{21}, O_{22}, O_{32}, O_{12}, O_{13}\right.$, $\left.O_{33}, O_{23}\right)$.

Since the continuous space based on the EDA cannot be directly used to describe the discrete solution space of the EJSP, the sequence mapping method was developed in this paper. Firstly, generate random numbers ranging from 0 to 1 according to the encoding length; secondly, sort the numbers from small to large and record their corresponding position index; finally, divide each number by the total number of machines, and then round up to an integer.

Example 2: According to the encoding length in Figure 1, nine random numbers are generated as $(0.104,0.517,0.618,0.336,0.988,0.203,0.380,0.902,0.151)$; then, the position indexes of the random numbers that are sorted from small to large are sequenced as $(1,9,6,4,7,2,3,8,5)$; next, each number in the integer sequence is divided by three to acquire a value and the value is rounded up to an integer. Thus, the mapping result is $(1,3,2,2,3,1,1,3,2)$.

# 2.2.2. Estimation of Distribution Algorithm 

The estimation of distribution algorithm (EDA) is a global searching technique that is based on the probabilistic model [34]. Algorithm 1 shows the general steps of the EDA. In the EDA, the probabilistic model and updating mechanism are two crucial parts aspects.

```
Algorithm 1. Estimation of distribution algorithm (EDA)
    Begin
    Randomly generate the initial population \(X(0)\)
    Set \(t=0\)
    While (the termination condition is not met) do
        Select a set of candidate individuals (solutions) \(D(t)\) to construct the current population \(X(t)\) according to the
        fitness values
        Construct the probability distribution model of the selected set \(D(t)\)
        Generate a set of new offspring individuals \(N(t)\) according to the probabilistic model
        Create a new population \(X(t+1)\) by replacing some individuals of \(X(t)\) by \(N(t)\) according to the updating
        mechanism
        \(T=t+1\)
    End while
    Report best results
    End
```

(1) Probabilistic model

The probabilistic model aims to reveal a general distribution by capturing the features of parent individuals. Moreover, the EDA generates new offspring individuals by sampling from the probabilistic model. Hence, constructing an effective probabilistic model is critical to studying the performance of the EDA. In this paper, according to the processing priorities of tasks, the probabilistic model was developed as an operation probabilistic matrix $Q(t)$ with $n$ rows and $l$ columns.

$$
Q(t)=\left[\begin{array}{cccc}
p_{11}(t) & p_{12}(t) & \cdots & p_{1 l}(t) \\
p_{21}(t) & p_{22}(t) & \cdots & p_{2 l}(t) \\
\vdots & \vdots & \ddots & \vdots \\
p_{n 1}(t) & p_{n 2}(t) & \cdots & p_{n l}(t)
\end{array}\right]
$$

where $p_{i q}(t)(1 \leq i \leq n, 1 \leq l \leq n \times m)$ stands for an element of the operation probabilistic matrix $Q(k)$, which represents the probability that task $T_{i}$ appears in the $q^{\text {th }}$ position of the operation sequence vector at generation $t$. Here, there exists $p_{i q}(t) \in[0,1]$ and $\sum_{i=1}^{n} p_{i q}(t)=1,(\forall q)$ at generation $t$. At the initial stage of the proposed algorithm, the value of each element in $Q(t)$ is initialized as $p_{i q}(0)=1 / n,(\forall i, q)$.
(2) Updating mechanism

In order to enhance the exploitation ability of the EDA, the probabilistic model should be adjusted well at each generation. Hence, an updating mechanism based on the incremental learning method was developed in this paper. First, according to the roulette wheel selection strategy, a promising sub-population that consists of Num_SP candidate solutions was determined. Then, the operation probabilistic matrix $Q(t)$ was updated based on the information of the promising sub-population and the historical information. The updating function of the probabilistic model is formally defined as:

$$
p_{i q}(t+1)=(1-\alpha) \cdot p_{i q}(t)+\frac{\alpha}{N u m \_S P} \sum_{s=1}^{N u m} \delta_{i q}^{S P} \cdot \forall i, q
$$

where $\alpha$ represents the learning rate of the operation probabilistic matrix $Q(t)$, and $\alpha \in(0,1) ; \delta_{i q}^{s}$ represents the following indicator function of the $s^{\text {th }}$ candidate individual in the promising sub-population.

$$
\delta_{i q}^{s}=\left\{\begin{array}{r}
1, \text { if task } T_{i} \text { appears in the } q^{\text {th }} \text { position } \\
0, \text { else }
\end{array}\right.
$$

# 2.2.3. Simulated Annealing Algorithm 

The simulated annealing algorithm (SAA) is a stochastic searching technique and its local search ability is promising. Algorithm 2 shows the general steps of the SAA. In the SAA, the neighborhood structure and annealing rate function have an important impact on performance.
(3) Neighborhood structure

To create a set of feasible solutions, neighborhood structures are needed. In general, the disjunctive graph is used to describe the neighborhood structure. In the neighborhood structures, the neighborhoods are generated in terms of neighborhood strategies. One of the most effective neighborhood strategies is based on the block structure of the critical path method, which is adapted in the SAA. A critical path, which is the longest path in the disjunctive graph, consists of a series of operations. It corresponds to a feasible solution. A maximal sequence of several operations that either is processed on the same machine or belongs to the same task is defined as a critical block. In this paper, the swap neighborhood structure based on the critical block is presented to generate the neighborhood.

(4) Annealing rate function

Annealing rate directly affects the speed and accuracy of the SAA. The general annealing rate function is given by Equation (4).

$$
T(t)=\beta \times T(t-1)
$$

where $\beta \in(0,1)$ represents an annealing rate coefficient; $T(t)$ and $T(t-1)$ represent current temperature and previous temperature, respectively; $t$ represents the iteration number.

```
Algorithm 2. Simulated annealing algorithm (SAA)
Begin
Generate the initial schedule \(S_{i}\)
Initialize the start temperature \(T_{s}\), the end temperature \(T_{e}\)
Set \(T=T_{s}\)
While \(\left(T>T_{e}\right)\) do
    Generate the temporary schedule \(S_{j}\) according to the neighborhood structure
    Evaluate the improvement of performance criterion function \(\Delta=f\left(S_{i}\right)-f\left(S_{i}\right)\)
    If \((\Delta \leq 0)\) then
        \(S_{i}=S_{j}\)
    Else if \(\left(\operatorname{random}(0,1)<e^{-\Delta / T}\right)\) then
\(S_{i}=S_{j}\)
End if
Update new annealing rate function
End while
Report best results
End
```

According to the characteristic of the annealing temperature function, it can be obtained that its decreased amplitude becomes faster at a high temperature level, while its decreased amplitude becomes slower at a low temperature level. It is likely to result in an insufficient search in the solution space. In order to enhance the exploitation ability of the SAA, an improved annealing rate function inspired by the Hill function is developed as

$$
T(t)=\beta \times \frac{T_{0}{ }^{n}}{T_{0}{ }^{n}+t^{n}}
$$

where $T_{0}$ represents a temperature threshold and it has a relationship with an initial temperature of the SAA; $n$ represents a Hill coefficient, and $n \geq 1 ; \beta \in(0,1)$ represents an annealing rate coefficient; $t$ represents the iteration number.

# 2.2.4. The Procedure of the EEDA 

By embedding SAA into EDA, an enhanced estimation of distribution algorithm (EEDA) was developed to solve the EJSP. To balance the global exploration and local exploitation of the EEDA, a decision-making factor $\lambda$ was designed with Equation (6). The procedure of the EEDA is described as shown in Algorithm 3.

$$
\lambda(t)=\exp (-t / \text { Maxgen })
$$

where $t$ represents the iteration number; Maxgen represents the maximal number of iteration.

```
Algorithm 3. Enhanced Estimation of distribution algorithm (EEDA)
    Begin
    Randomly generate the initial population \(X(0)\)
    Initialize the learning rate \(a\), the Hill coefficient \(n\), the start temperature \(T_{s}\), the end temperature \(T_{e}\)
    Set \(t=0, T=T_{s}\)
    While (the termination condition is not met) do
    Evaluate the fitness value of each individual in \(X(0)\)
    Select a set of candidate individuals (solutions) \(D(t)\) to construct the current population \(X(t)\)
    Construct the probability distribution model of the selected set \(D(t)\)
    If ( \(r a n d \leq \lambda\) ) then
        Generate a set of new offspring individuals \(N(t)\) according to the probabilistic model
        Create a new population \(X(t+1)\) by replacing some individuals of \(X(t)\) by \(N(t)\) according to the updating
    mechanism
        Else
    While \(\left(T>T_{e}\right)\) do
    Generate the temporary individuals \(N(t)\) according to the neighborhood structure
    Evaluate the improvement of the fitness value
    Update annealing rate function
    End while
    End if
        \(T=t+1\)
    End while
    Report best results
    End
```


# 3. Model of Energy-Efficient Job-Shop Scheduling Problem (EJSP) with Transportation Constraints 

### 3.1. Notations

Notations are defined as follows.



# 3.2. Energy Consumption Model 

According to energy-consuming behaviors of each task processed on machines [15,16], three important energy consumption modules were considered: energy consumption module for a cutting process ( $E c$ ), energy consumption module for an idle running process ( $E i$ ), and energy consumption module for an auxiliary process ( $E a$ ). In addition, AGVs are used to move each task that needs to be transported to the next machine after the completion of a task on a machine, which also consumes energy, i.e., energy consumption module for a transportation process (Et). Thus, the comprehensive energy consumption throughout the production process mainly consists of four modules, which are described as follows.

### 3.2.1. Energy Consumption Module for a Cutting Process (Ec)

Ec represents the energy required to execute all the operations. In general, Ec can be calculated approximately by using a secondary polynomial fitting curve [35]. Hence, the formulation of Ec is defined below.

$$
E c=\sum_{k=1}^{m} P_{k^{\prime}}\left(\sum_{i=1}^{n} \sum_{j=1}^{N_{i}} T_{i j k}\right)+\sum_{i=1}^{n} \sum_{j=1}^{N_{i}} \sum_{k=1}^{m}\left(1+\alpha_{1}\right) \cdot P_{i j k} \cdot T_{i j k}+\sum_{i=1}^{n} \sum_{j=1}^{N_{i}} \sum_{k=1}^{m} \alpha_{2} \cdot P_{i j k}{ }^{2} \cdot T_{i j k}
$$

where $\alpha_{1}$ and $\alpha_{2}$ are the coefficients of the secondary polynomial fitting curve.

### 3.2.2. Energy Consumption Module for an Idle Running Process (Ei)

$E i$ represents the energy required to wait for processing the next operation when a machine is in an idle running period. Ei can be calculated by multiplying the unload power consumption by the total idle time as:

$$
E i=\sum_{k=1}^{m} P_{k^{\prime}}\left(\max _{i, j} C_{i j k}-\sum_{i=1}^{n} \sum_{j=1}^{N_{i}}\left(C_{i j k}-S_{i j k}\right)\right)
$$

### 3.2.3. Energy Consumption Module for an Auxiliary Process (Ea)

Ea represents the energy required to support production equipment in the workshop, such as lighting, heating, and air-conditioning. Ea can be written as:

$$
E a=e \cdot \max _{1 \leq i \leq n}\left(C_{i}\right)
$$

### 3.2.4. Energy Consumption Module for a Transportation Process (Et)

$E t$ is the energy consumption of an AGV for moving a task whenever it requires transportation from one machine to another. Et is defined as:

$$
E t=\sum_{i=1}^{n} \sum_{j=2}^{N_{i}} \sum_{k=1}^{m} \sum_{w=1}^{m} P_{0} \cdot T_{i(j-1) w}^{i j k}
$$

# 3.2.5. Comprehensive Energy Consumption (E) 

$E$ is composed of $E c, E i, E a$, and $E t$. Hence, the comprehensive energy consumption is the sum of them, which is expressed as:

$$
E=E c+E i+E a+E t
$$

### 3.3. Formulation of the EJSP Optimization Model

The scheduling optimization objectives are to satisfy two efficiency criteria: schedule efficiency that is measured in terms of makespan and energy efficiency that is calculated by the comprehensive energy consumption for a schedule. The two objective functions can be written as:

$$
\begin{gathered}
\min f_{1}=C_{\max } \\
\min f_{2}=E
\end{gathered}
$$

subject to:

$$
\begin{aligned}
& C_{i j k}-C_{i(j-1) w} \geq T_{i j k} \\
& \forall i=1,2, \ldots, n, j=2,3, \ldots, N_{i}, k, w=1,2, \ldots, m \\
& S_{i j k} \geq \max \left(C_{i(j-1) w}++T_{i(j-1) w}^{i j k}, C_{i^{-} j^{-} k}\right) \\
& \forall i, i^{-}=1,2, \ldots, n, j=2,3, \ldots, N_{i}, j^{-}=1,2, \ldots, N_{i^{-}}, k, w=1,2, \ldots, m \\
& B_{k q} \leq T_{i j k}+L \cdot\left(1-Y_{i j k q}\right) \\
& \forall i=1,2, \ldots, n, j=1,2, \ldots, N_{i}, k=1,2, \ldots, m, q=1,2, \ldots, Q_{k} \\
& B_{k q} \geq T_{i j k}-L \cdot\left(1-Y_{i j k q}\right) \\
& \forall i=1,2, \ldots, n, j=1,2, \ldots, N_{i}, k=1,2, \ldots, m, q=1,2, \ldots, Q_{k} \\
& \sum_{i=1}^{n} \sum_{j=1}^{N_{i}} Y_{i j k q}=1 \\
& \forall k=1,2, \ldots, m, q=1,2, \ldots, Q_{k}
\end{gathered}
$$

The first objective (12) is to minimize the makespan and the second objective (13) is to minimize the comprehensive energy consumption. Constraint (14) ensures that the precedence constraints between the operations of each task are not changed. Constraint (15) establishes the relationship between the transportation constraint and the machine capacity constraint. Assume that two adjacent operations $\left(O_{i^{-} j^{-}}, O_{i j}\right)$ are to be executed on machine $M_{k}$ in Figure 2. The completion time of the preceding operation $O_{i^{-} j^{-}}$of operation $O_{i j}$ on machine $M_{k}$ is $C_{i^{-} j^{-} k}$, the completion time of the $(j-1)^{\text {th }}$ operation $O_{i(j-1)}$ of task $T_{i}$ on machine $M_{w}$ is $C_{i(j-1) w}$, and the transportation time of AGV between machine $M_{w}$ and machine $M_{k}$ is $T_{i(j-1) w}^{i j k}$. If $C_{i^{-} j^{-} k} \leq C_{i(j-1) w}+T_{i(j-1) w}^{i j k}$, then, the start time of operation $O_{i j}$ should be after the transportation time of operation $O_{i(j-1)}$. Otherwise, the start time of operation $O_{i j}$ should be after the completion time of operation $O_{i^{-} j^{-}}$. Constraints (16) and (17) establish linking constraints between start times $B_{k q}$ and $S_{i j k}$. It means that if operation $O_{i j}$ is processed in the $q^{\text {th }}$ position on machine $M_{k}$, then $B_{k q}=S_{i j k}$. Constraint (18) points out that an operation is only assigned to one position of one machine.

As the relationship between energy consumption and makespan is conflicting, no single optimal solution exists in the multi-objective optimization problem (MOP) [36]. There have been diverse techniques for solving MOP. One of the most popular approaches to studying MOP is the normalized weighted additive utility function (NWAUF). Owning to its simplicity and natural ability to explore

efficient solutions, the NWAUF has been successfully applied in the field of production scheduling. The NWAUF for alternative $k$ with $n$ objectives is defined as $U(k)$ :

$$
U(k)=w_{1} f_{1}^{\prime}(k)+w_{2} f_{2}^{\prime}(k)+\ldots+w_{n} f_{n}^{\prime}(k)
$$

where $w_{i}(i=1,2, \ldots, n)$ is a weight coefficient, and $\sum_{i=1}^{n} w_{i}=1, w_{i} \in[0,1] ; f_{i}^{\prime}(k)$ is the normalized value of the $i^{\text {th }}$ objective function $f_{i}(k)$ for $i=1,2, \ldots, n$. Note that each normalized objective $f_{i}^{\prime}(k)$ can be expressed by Equation (20).

$$
f_{i}^{\prime}(k)=\frac{f_{i, \max }-f_{i}(k)}{f_{i, \max }-f_{i, \min }}
$$

where $f_{i, \min }$ and $f_{i, \max }$ represent for the minimum and maximum values of the objective function $f_{i}$, respectively.

Using the utility function, MOP can be solved as a single objective optimization. Therefore, according to the objective functions (12) and (13), NWAUF is formulated as $F(k)$ :

$$
F(k)=w \cdot \frac{f_{1, \max }-f_{1}(k)}{f_{1, \max }-f_{1, \min }}+(1-w) \cdot \frac{f_{2, \max }-f_{2}(k)}{f_{2, \max }-f_{2, \min }}
$$

where $w$ is the weighted importance of the objective function makespan and $w \in[0,1] . f_{1, \min }$ and $f_{1, \max }$ are the minimum and maximum values of the objective function $f_{1}$, respectively. $f_{2, \min }$ and $f_{2, \max }$ are the minimum and maximum values of the objective function $f_{2}$, respectively.
![img-1.jpeg](img-1.jpeg)

Figure 2. Constraints of two successive operations for a task.

# 4. Experimental Results 

In this section, the proposed EEDA is employed to solve the EJSP. First, the analysis of the algorithm parameter settings was conducted to investigate their influence on the performance of the EEDA. Second, two classes of benchmark instances from the OR-Library were given to evaluate the performance of the proposed algorithm. Finally, the proposed algorithm was used to evaluate the effectiveness of the proposed model. The computational experiments were carried out utilizing MATLAB R2009a. The experimental tests were implemented on a personal computer with an Intel Pentium (R) with 4 GB memory and a 2.60 GHz processor, and the operating system was Windows 10.

### 4.1. Sensitivity Analysis of the Algorithm Parameters

The parameter settings could have significant influence on the performance of the EEDA. In the EEDA, four critical algorithm parameters should be considered: the population size (NIND), the maximum number of iterations (Maxgen), the learning rate ( $\alpha$ ), and the Hill coefficient ( $n$ ). In order to analyze the influence of these algorithm parameters on the performance of the EEDA, the Taguchi

design method was adopted to study the parametric sensitivity. An example of a $10 \times 10 \mathrm{JSP}$ is given in Table 1. There are 10 types of tasks to be processed on 10 machines, and each task contains 10 operations. An operation is assigned to a given machine and has the corresponding processing time. For example, in Table 1, the element $(4,6)$ in first row and fifth column means that the 5th operation of task $T_{1}$ is processed on machine $M_{4}$ and the processing time is 6 min . Here, for the convenience of analysis and comparison, the scheduling objective is to minimize the makespan which is used by many authors in the literature. Various values for the four parameters are listed Table 2. In addition, the average makespan value (AMV) and average running time (ART) were adopted as evaluation standards to analyze the parameters.

Table 1. Test instance with 10 tasks 10 machines.
Table 2. Various values of the algorithm parameters.
The experimental results on the combination situations of the four parameters are listed Table 3. Figure 3 describes the changing trend in the average makespan, such that each parameter for different setting values is considered.

Table 3. Combination situations of the algorithm parameters.

From Table 3 and Figure 3, it can be seen that four parameters had an impact on the performance of the EEDA. Concretely speaking, the average makespan value decreased as any of these parameter values (including NIND, Maxgen, $\alpha$ ) increased, as shown in Figure 3a-c. But a large parameter setting value could result in more computational time. In addition, when the Hill coefficient was set to 2, in Figure 3d, the better solution can be obtained by the EEDA. Therefore, according to the above analysis, the parameter values in the EEDA are set in Table 2 (in bold and italics).
![img-2.jpeg](img-2.jpeg)

Figure 3. Parameters' influence on the average makespan.

# 4.2. Performance Evaluation 

To validate the effectiveness of the proposed algorithm, the widely used benchmark instances from the OR-library were carried out [37]. Two classes of benchmarks instances are considered: one was the instance FT06, FT10, FT20 ( $n \times m=6 \times 6,10 \times 10,20 \times 5$ ) designed by Fisher and Thompson [38], the other was the instance LA01-LA40 ( $n \times m=10 \times 5,15 \times 5,20 \times 5,10 \times 10$, $15 \times 10,20 \times 10,30 \times 10,15 \times 15$ ) designed by Lawrence [39]. The proposed algorithm was compared with several existing algorithms, including estimation of distribution algorithm (EDA) presented by He et al. [40], hybrid differential evolution and estimation of distribution algorithm (DE-EDA) presented by Zhao et al. [41], simulated annealing (SA) presented by Laarhoven et al. [42], hybrid genetic and simulated annealing (GA-SA) presented by Wang and Zheng [43], genetic algorithm (GA: P-GA, SBGA-40, SBGA-60 ) presented by Dorndorf and Pesch [44], and hybrid genetic algorithm (HGA: HGA-Param, HGA-Non-delay, HGA-Active) presented by Goncalves et al. [45]. For each instance, we ran the algorithms 10 times independently. The experimental results are shown in Table 4. It lists the problem name, the problem size, the best-known solution $\left(S_{\text {best }}\right)$, the solution obtained by the proposed algorithm (EEDA), and the solution obtained by other algorithms reported in the literature. According to Table 4, it can be observed that the proposed algorithm obtained the best-known solution in 30 out of 43 instances. In other words, the EEDA found the best-known solution in $70 \%$ of problem instances. In addition, compared with EDA and SA, the EEDA was superior to them in solution quality. Hence, the combination of the EDA and SA is promising in solving the problems.

Table 4. Experimental results obtained by different algorithms.

Table 4. Cont.
"-" means inapplicable.

At the same time, average relative percentage deviation ( $A R P D$ ) is designed to evaluate the performance of the EEDA in the experimental test as below:

$$
A R P D=\left(\sum_{z=1}^{\mathrm{NIS}} \frac{f(z)-S_{b e s t}}{S_{b e s t}} \times 100\right) / \mathrm{NIS}
$$

where $f(z)$ represents the best result obtained by the algorithms, $S_{\text {best }}$ represents the best result known for each instance, NIS represents the number of instances solved by the algorithms.

In addition, improvement rate $(I R)$ of $A R P D$ obtained by the EEDA with regard to other algorithms is defined as follows:

$$
I R=\frac{A R P D \text { of some algorithm }-A R P D \text { of EEDA }}{A R P D \text { of some algorithm }}
$$

The comparisons of the experimental results among different algorithms are given in Table 5. It lists the different algorithms, the number of instances solved (NIS), the average relative percentage deviation $(A R P D)$ of all compared algorithms, and the corresponding improvement rate $(I R)$. From Table 5, we can find that the $A R R D$ of the EEDA was 0.60 in all 43 instances. Compared to the other algorithms, the EEDA had an improvement in solution quality.

In summary, it was realized that the proposed algorithm is a promising approach for the job shop scheduling problem by comparing it with other algorithms. Thus, the EEDA is employed to solve the EJSP in the next section.

Table 5. Experimental results of the EEDA compared with the other algorithms.
# 4.3. Case Study 

In order to evaluate the energy-savings potential of the proposed model, an experiment originating from a machining shop floor is illustrated: the experiment consists of ten tasks and ten machines. These tasks had similar processing operations, including rough/finish turning, rough/finish milling, drilling/tapping, rough/finish grinding, cleaning, and inspection. Their processing times are shown in Table 6. Moreover, there were five AGVs for transporting the tasks among machines, and the power demand of each AGV was set to 3.45 kW . In addition, the auxiliary average power required to support the production environment was set to 1 kW . The transportation times between different machines are listed in Table 7. The related power demand for all machines is given in Table 8.

Table 6. Processing times of tasks on machines (unit: s).
Table 7. Transportation times between different machines (unit: s).

Table 8. Unload power of each machine.

# 4.3.1. Energy-Efficient Scheduling Analysis 

To highlight the transportation impact over the scheduling objective, we analyzed energy consumptions with regard to different transportation speeds of AGVs. Three transportation speeds, i.e., low speed, medium speed, and high speed, were considered when the weighted importance $w$ was set as $0,0.5$, and 1 , respectively. The experimental results based on the proposed EEDA are shown in Figures 4-6.
![img-3.jpeg](img-3.jpeg)

Figure 4. Breakdown of energy consumption of different transportation speeds for $w=0$.

![img-4.jpeg](img-4.jpeg)

Figure 5. Breakdown of energy consumption of different transportation speeds for $w=0.5$.
![img-5.jpeg](img-5.jpeg)

Figure 6. Breakdown of energy consumption of different transportation speeds for $w=1$.
From the results shown in Figures 4-6, we can observe that the ratio of the transportation energy consumption to the comprehensive energy consumption became lower as the transportation speed increased for the given weighted importance. Moreover, the comprehensive energy consumption reduced as the transportation speed increased. It is also clear that the comprehensive energy consumption decreased as the weighted importance $w$ increased at the given transportation speed. Furthermore, the transportation speed had a significant effect on $E i$ and $E a$. For example, for the given weighted importance ( $w=0.5$ ), when the transportation speed increased from low speed to the high speed, the ratio of the idle energy consumption decreased to $36.9 \%$ and the ratio of the auxiliary energy consumption decreased to $14.29 \%$. Also, we calculated that the comprehensive energy consumption ratio decreased to $14.61 \%$. Therefore, it was concluded that the energy-efficient scheduling strategy could be considered by increasing the transportation speed for the decision makers.

# 4.3.2. Computational Results on EEDA versus EDA 

In order to demonstrate the optimization capability of the EEDA on the potential of the energy savings, the general EDA was also shown as a heuristic strategy. The parameters setting of the EDA was the same as that of the EEDA regarding the population size (NIND), the maximum number of iterations (Maxgen), and the learning rate ( $\alpha$ ). Due to the fact that the consideration of energy consumption

and makespan is different in different manufacturing environments, different weighted importance of energy consumption and makespan should be taken into account in the EJSP. In this section, this is done by changing the value of the weighted importance $w$ with a step size of 0.1 . Hence, the objective function is conducted with the weighted importance $w$ from 0 to 1 so that the optimal solutions are from energy-savings oriented to time-savings oriented. The experimental results are shown in Table 9.

As seen in Table 9, the comprehensive energy consumption decreased by 25.57 kWh and an optimal energy-efficient schedule result could be obtained by the EEDA. Moreover, the comprehensive energy consumption values obtained by the EEDA had better optimization than EDA, where the average comprehensive energy consumption by EEDA was $0.02 \%$ lower than EDA. Moreover, the makespan values from the EDA were larger than those obtained by the EEDA, where the related average gap was $1.62 \%$. Therefore, the optimization effects of the EEDA with regard to the energy consumption and makespan were better than those of the EDA. Meanwhile, the comparison results were given with regard to the makespan and energy consumption with the EEDA and EDA, as demonstrated in Figure 7. It can be observed that the quality of solutions obtained by the EEDA outperformed the quality of solutions obtained by the EDA.

Table 9. Optimization results with different weighted importance on EEDA versus EDA.

![img-6.jpeg](img-6.jpeg)

Figure 7. Distribution of solutions with different weighted importance on the EEDA versus EDA.

# 5. Discussion 

In summary, the reasonable settings of the parameters in the EEDA had an important impact on the algorithms' performance. For example, when the population size increased, better individuals could be selected to obtain an optimal solution. However, oversized population sizes will result in more computational time. It is a disadvantage for the EEDA to obtain the best result in a limited time. Hence, it is necessary to design the experiment to determine parameter values, which is shown in Table 2. Furthermore, to verify the effectiveness of the EEDA, experiments with the EEDA versus other algorithms were performed for benchmark problems. According to the results, the EEDA had improvements in solution quality compared to the other algorithms. The reason for this is that the EEDA had a better ability to achieve a balance with the proposed algorithm in both global and local searches.

In addition, the proposed EEDA is a promising method for solving energy-efficient job-shop scheduling problems with transportation constraints. On the one hand, by assessing the algorithm performance, it can be seen that EEDA had a better searching ability compared to other algorithms like the EDA. The reason for this is explained by the EDA being a global search method based on the probability model, but its local search ability is limited. The EEDA is the combination of the EDA and SA, and absorbs their advantages. At the same time, with regard to the local search ability of the SA, it is subject to the constraint of simulated annealing function. A novel annealing schedule method, which is inspired from the hormone modulation mechanism, is designed to achieve the balance of EEDA in both global and local search. On the other hand, through analyzing the optimization capability of the EEDA on the potential of the energy savings in the case study, the EEDA outperforms the EDA in obtaining the optimal solution regarding energy consumption and makespan on a fair basis. It also indicates that the EEDA had the comprehensive search ability.

## 6. Conclusions

In this study, an energy-efficient job-shop scheduling problem with consideration of AGV transportation was studied. First, a mixed-integer programming model was established to minimize both the comprehensive energy consumption and makespan. Due to the complexity of the problem, the EEDA was designed to explore its optimal solution. Comprehensive experiments were conducted to investigate the proposed model and algorithm. The experimental results indicated that the proposed algorithm was effective in solving the EJSP and it was capable of obtaining better solutions than the EDA. Furthermore, the results highlighted that the transportation energy consumption had a non-negligible impact on the comprehensive energy consumption.

With respect to future work, it will be interesting to study the following issues: (1) the EEDA shows the improvement of algorithm performance compared with other meta-heuristic algorithms, but further research on the model accuracy and computation time should be taken into account; (2) there are many unexpected events such as random machine breakdown, rush task, and task cancellation occurring in practical factories. They may have an influence on the energy consumption, which should be considered in the EJSP. Hence, research on a dynamic integrated scheduling problem for machines and AGVs with consideration of energy consumption should also be studied in the future.

Author Contributions: Conceptualization: M.D.; methodology: M.D. and Z.Z.; software, Z.Z.; formal analysis: Z.Z.; data curation, M.D. and Z.Z.; writing-original draft preparation, M.D. and Z.Z.; writing-review and editing, A.G. and M.A.S.; supervision: A.G. and M.A.S.
Funding: This work was supported by the Natural Science Foundation of the Jiangsu Higher Education Institutions of China (No. 17KJB460018), the Innovation Foundation for Science and Technology of Yangzhou University (No. 2016CXJ020 and No. 2017CXJ018), Science and Technology Project of Yangzhou under (No. YZ2017278), Research Topics of Teaching Reform of Yangzhou University under (No. YZUJX2018-28B), and the Spanish Government (No. TIN2016-80856-R and No. TIN2015-65515-C4-1-R).
Conflicts of Interest: The authors declare no conflict of interest.
