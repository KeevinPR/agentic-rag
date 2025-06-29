# Multi-task Allocation of Multi-UAV Coalition Based on Improved Quantum Genetic Algorithm 

Pengfei Liu ${ }^{1}$, Bing Wang ${ }^{2}$, Wenjie Liu ${ }^{1}$, Lan Zhang ${ }^{1}$<br>1. University of Science \& Technology Beijing, Beijing 100083<br>E-mail: zhanglan2013@ustb.edu.cn<br>2. Tianjin Aerospace Zhongwei Date System Technology Co.,LTD, Tianjin 300345, China<br>E-mail: wangbing0001@126.com


#### Abstract

In the multi-UAV task allocation problem, one task may need several UAVs with specific capabilities to form a coalition to execute cooperatively. In this paper, considering the UAV coalition loss cost and time cost, an improved quantum genetic algorithm is proposed to solve the task allocation problem of multi-UAV coalition. On the basis of quantum genetic algorithm, the historical optimal solution retention mechanism and estimation of distribution algorithm are introduced to speed up the convergence speed and reduce the probability falling into the local optimum of the algorithm, respectively. Then, a gene repair strategy is used to improve the efficiency of the algorithm according to the problem background. Finally, the simulation results show that the proposed algorithm has more advantages than other comparison algorithms in terms of search ability and convergence speed in solving the task allocation problem of multi-UAV coalition.


Key Words: Unmanned aerial vehicle, Task allocation, Combinatorial optimization, Quantum genetic algorithm

## 1 Introduction

Unmanned aerial vehicles (UAVs) have found an increasingly wide utilization in military and civilian fields, such as target reconnaissance, disaster rescue and precision agriculture, etc [1]. Due to the limitation of single UAV, it is usually difficult to complete a complex task independently. Therefore, the task allocation system must integrate UAVs with different capabilities and resources according to the characteristics of task attributes to form UAV coalitions to perform tasks cooperatively [2]. To solve this task allocation problem, various optimization algorithms have been proposed, which are mainly divided into distributed task allocation and centralized task allocation [3].

Distributed task allocation means that there is no central controller to grasp the global information. Each UAV in the system, as an independent agent with certain intelligence, shares information and negotiates among agents, and then obtains the task allocation scheme. It has the advantages of good timeliness, flexibility and robustness. Common distributed task allocation methods include contract network protocol algorithms, distributed auction algorithms and game theory methods $[4,5]$. However, the distributed task allocation methods fail to consider global factors, so they can not provide an optimal allocation scheme.

Centralized task allocation has a central processing unit to integrate the global information and formulate a reasonable assignment plan. Since it can be considered from a global perspective, it has the advantages of good globalization and high solution quality [6]. With the rapid developments of metaheuristic optimization algorithms, they have been widely applied to solve centralized task allocation problems. Li et al. [7] accomplished the allocation of multi-task to multi-agent through a novel quantum particle swarm optimization algorithm (QPSO) method. It is aimed at assigning the best possible agent coalition for each task. Guo et al. [8] proposed an efficient genetic algorithm with heuristic initialization and repair strategy (GAHIR), which can handle various task allocation models in a uniform algo-
rithm framework.
Quantum genetic algorithm (QGA) $[9,10]$ is also a metaheuristic optimization algorithm, which has the characteristics of fast convergence speed and strong global search ability with small population size. With the advantages of the QGA, it has been widely used to solve combinatorial optimization problems such as task allocation and path planning. Mousavi et al. [11] used QGA in a large scale UAV network to allocate the optimal UAV coalitions to perform the detected tasks in an unknown environment. Gao et al. [12] designed QGA to solve the robot path planning problem. The algorithm worked in the discretized environment and approximated the optimal robot planning path in a highly computationally effcient fashion. Tian et al. [13] presented an improved QGA to solve the vehicle routing problem. It combined route selection with quantum chromosome coding and quantum updating and used the high parallel computing characteristics of a quantum computer to obtain the best solution. However, QGA only uses the current generation optimal solution to guide population evolution, which makes the population diversity to shrink rapidly in the later stage of the optimization process and the algorithm easy to fall into a local optimum.

Different from the evolution of QGA, estimation of distribution algorithm (EDA) adopts statistical learning methods to construct a macroscopic probability model describing the solution distribution, and then randomly samples the probability model to generate a new population [14, 15]. It is often used in combination with other algorithms to reduce the probability of the algorithm falling into the local optimum $[16,17]$.

The main contributions of this paper are as follows: (1) QGA is used to solve task allocation problem of multi-UAV coalition by encoding UAV and task information in quantum chromosome. (2) EDA is introduced into the QGA to reduce the probability of the QGA falling into the local optimum. Then the convergence speed of the algorithm is further accelerated by using the historical optimal solution retention

mechanism. And finally, the gene repair strategy is used to modify the solutions to improve the efficiency of the algorithm.

The rest of the paper is organized as follows: Section 2 formulates mathematical model for task allocation problem of multi-UAV coalition. Section 3 describes the proposed distributed estimation quantum genetic algorithm (DE-QGA) in detail. Section 4 presents and discusses the simulation results. Finally, Section 5 concludes the paper and notes the directions of future work.

## 2 Problem description and formulation

### 2.1 Problem description

As shown in Fig. 1, the problem in this paper is to allocate an optimal coalition of several UAVs for each task. The UAV, task and UAV coalition are described firstly.
![img-0.jpeg](img-0.jpeg)

Fig. 1: Task allocation diagram
UAV: $U=\left\{U_{1}, U_{2}, \ldots, U_{N_{u}}\right\}$ is the set of $N_{u}$ UAVs. The information of $U_{i}$ can be represented by a vector $A_{U_{i}}=$ $\left\{V_{U_{i}}, F T \max _{U_{i}}, v_{U_{i}}, P_{U_{i}}\right\}$, which is made up of the value, maximum flight time, flight speed and coordinates of $U_{i}$. $R_{U_{i}}=\left[r_{U_{i}}^{1}, r_{U_{i}}^{2}, \ldots, r_{U_{i}}^{N_{r}}\right]$ denotes the vector of resources carried by $U_{i}$, where $r_{U_{i}}^{k}$ is the amount of $k^{t h}$ resource carried by $U_{i}$ and $N_{r}$ is the number of resource types.

Task: There exists $N_{t}$ tasks $T=\left\{T_{1}, T_{2}, \ldots, T_{N_{t}}\right\}$. The information vector of $T_{j}$ is $A_{T_{j}}=\left\{Q_{T_{j}}, E x c T_{T_{j}}, P_{T_{j}}\right\}$, including the danger level, execution time and coordinates of $T_{j}$. The resource vector required by $T_{j}$ is defined as $R_{T_{j}}=\left[r_{T_{j}}^{1}, r_{T_{j}}^{2}, \ldots, r_{T_{j}}^{N_{r}}\right]$, where $r_{T_{j}}^{k}$ represents the number of $k^{t h}$ resources required by task $T_{j}$. Finally, there are sequential logic relationships between tasks. As shown in Fig. 2, $T_{1}$ is the synchronization task of $T_{2}$, defined as $T_{1}=\operatorname{Syn}\left(T_{2}\right)$, which means that the two tasks must be executed synchronously; $T_{1}$ is the predecessor task of $T_{2}$, defined as $T_{1}=\operatorname{Pr}\left(T_{3}\right)$, which means that $T_{3}$ must be executed after $T_{1}$.
![img-1.jpeg](img-1.jpeg)

Fig. 2: The sequential logic relationship between tasks
UAV Coalition: The UAV coalition set is $C=$ $\left\{C_{1}, C_{2}, \ldots, C_{N_{t}}\right\}$, and each coalition corresponds to a task. The resource vector carried by $C_{j}$ is defined as $R_{C_{j}}=$ $\left[r_{C_{j}}^{1}, r_{C_{j}}^{2}, \ldots, r_{C_{j}}^{N_{r}}\right]$, where $r_{C_{j}}^{k}=\sum r_{U_{i}}^{k}, U_{i} \in C_{j}$. The same UAV can participate in multiple coalitions at different times, but only can participate in one coalition at a time.

### 2.2 Problem Formulation

Task allocation of multi-UAV coalition can be formulated as a complex combinatorial optimization problem.

$$
\min J=\alpha_{1} \cdot f_{1}+\alpha_{2} \cdot f_{2}
$$

s.t.

$$
\begin{gathered}
r_{C_{j}}^{k} \geq r_{T_{j}}^{k}\left(\forall k=1,2, \ldots, N_{r}, j=1,2, \ldots, N_{t}\right) \\
F T_{U_{i}} \leq F T \max _{U_{i}}\left(\forall i=1,2, \ldots, N_{u}\right) \\
C_{j} \cap \operatorname{Syn}\left(C_{j}\right)=\emptyset\left(\forall j=1,2, \ldots, N_{t}\right) \\
\left.S t\left(T_{j}\right) \geq E t\left(\operatorname{Pr}\left(T_{j}\right)\right)\left(\forall j=1,2, \ldots, N_{t}\right)\right) \\
\left.S t\left(T_{j}\right)=S t\left(\operatorname{Syn}\left(T_{j}\right)\right)\left(\forall j=1,2, \ldots, N_{t}\right)\right. \\
\left.S t\left(T_{j}\right) \geq E t\left(T_{j i}\right)+\frac{\left|P_{T_{j}}, P_{T_{j i}}\right|}{v_{U_{i}}}\right. \\
\left(\forall j=1,2, \ldots, N_{t}, \forall U_{i} \in C_{j}\right)
\end{gathered}
$$

The objective function (1) to minimize the weighted cost includes two main components: coalition loss cost and time cost, which will be described below. Constraint (2) ensures that the resource vector component required by each task should be less than that carried by corresponding UAV coalition. Constraint (3) ensures that the total time for each UAV to perform its tasks shall not exceed its maximum flight time. Where $F T_{U_{i}}$ is the total time taken by $U_{i}$ to perform tasks. Constraint (4) ensures that the same UAV can only participate in one coalition at a time. Where $\operatorname{Syn}\left(C_{j}\right)$ is the UAV coalition corresponding to synchronization task $\operatorname{Syn}\left(T_{j}\right)$ of task $T_{j}$. Constraint (5) ensures that task $T_{j}$ can not start to be executed until all the predecessor tasks have been executed. Where $\operatorname{St}\left(T_{j}\right)$ and $\operatorname{Et}\left(T_{j}\right)$ are the start time and end time of task $T_{j}$, respectively. Constraint (6) ensures that task $T_{j}$ must start to be executed at the same time as its synchronization task. Constraint (7) means that if the UAV $U_{i} \in C_{j}$ performing task $T_{j}$ participates in task $T_{j i}$ before, the start time of task $T_{j}$ is greater than the end time of task $T_{j i}$ plus the transfer time of UAV $U_{i}$ at two tasks. Where $\left|P_{T_{j}}, P_{T_{j i}}\right|$ is the distance between task $T_{j}$ and $T_{j i}$.

The detailed description of the objective function (1) is as follows:

$$
\begin{gathered}
\min J=\alpha_{1} \cdot f_{1}+\alpha_{2} \cdot f_{2} \\
f_{2}=\sum_{j=1}^{N_{t}} Q_{T_{j}} \cdot \sum_{U_{i} \in C_{j}} V_{U_{i}} / \delta_{1} \\
\delta_{1}=V_{U \max } \\
f_{2}=\left(E t\left(T_{N_{t}}\right)-S t\left(T_{1}\right)\right) / \delta_{2} \\
\delta_{2}=\operatorname{Exc} T_{\max }
\end{gathered}
$$

Formula (9) is the coalition loss cost function which refers to the expected total cost of the members of coalitions being damaged when the coalitions are executing tasks. Formula (11) is the time cost function that can be calculated after the task allocation plan is determined. In order to unify the order of magnitude of the two parts of the objective function, the UAV value and task execution time are normalized in Formula (10) and Formula (12). Where $V_{U \max }$ represents the maximum value of single UAV and $E x c T_{\max }$ represents the maximum execution time of single task.

## 3 Proposed algorithm

The flowchart of the DE-QGA is presented in Fig. 3, and the key steps of the algorithm will be described below.
![img-2.jpeg](img-2.jpeg)

Fig. 3: The flowchart of the DE-QGA

### 3.1 Quantum genetic algorithm

### 3.1.1 Quantum encoding

QGA maintains a population of quantum chromosomes in the iterative process, $Q=\left\{q_{1}, q_{2}, \ldots, q_{N}\right\}$, where $N$ is population size, and quantum chromosome of the task allocation problem of multi-UAV coalition $q_{l}$ is coded as:

$$
q_{l}=\left[\begin{array}{c}
{\left[\begin{array}{c}
\alpha_{11} \\
\beta_{11} \\
\alpha_{21} \\
\beta_{21}
\end{array}\right]} \\
{\left[\begin{array}{c}
\alpha_{12} \\
\beta_{12} \\
\alpha_{22} \\
\beta_{22}
\end{array}\right]} \\
\cdots \\
{\left[\begin{array}{c}
\alpha_{N_{n} 1} \\
\beta_{N_{n} 1}
\end{array}\right]}\left[\begin{array}{c}
\alpha_{N_{n} 2} \\
\beta_{N_{n} 2}
\end{array}\right] \cdots\left[\begin{array}{c}
\alpha_{1 N_{i}} \\
\beta_{1 N_{i}} \\
\alpha_{2 N_{i}} \\
\beta_{2 N_{i}}
\end{array}\right] \\
\cdots \\
{\left[\begin{array}{c}
\alpha_{N_{n} N_{i}} \\
\beta_{N_{n} N_{i}}
\end{array}\right]}
\end{array}\right]
$$

where $\left[\alpha_{i j}, \beta_{i j}\right]^{T}$ is a qubit. $\alpha_{i j}^{2}$ and $\beta_{i j}^{2}$ respectively represent the probability of $U_{i}$ not joining or joining $C_{j}$, and satisfy the constraint:

$$
\alpha_{i j}^{2}+\beta_{i j}^{2}=1
$$

In (15), $p_{l} \in P$ is a binary solution, which can be obtained by observing $q_{l}$ [11]. Where $b_{i j} \in\{0,1\}$. If $b_{i j}=1$, then $U_{i}$ will join coalition $C_{j}$, otherwise it will not join.

$$
p_{l}=\left[\begin{array}{cccc}
b_{11} & b_{12} & \cdots & b_{1 N_{i}} \\
b_{21} & b_{22} & \cdots & b_{2 N_{i}} \\
\cdots & \cdots & \cdots & \cdots \\
b_{N_{n} 1} & b_{N_{n} 2} & \cdots & b_{N_{n} N_{i}}
\end{array}\right]
$$

### 3.1.2 Quantum gate

In QGA, quantum gate is used to act on qubit to change the distribution of the probability amplitude. Taking the first quadrant as an example, the quantum gate update is shown as Fig. 4.
![img-3.jpeg](img-3.jpeg)

Fig. 4: Schematic diagram of quantum gate update
The update operation of quantum gate is as follows:

$$
\begin{gathered}
{\left[\begin{array}{c}
\alpha_{i j}^{\prime} \\
\beta_{i j}^{\prime}
\end{array}\right]=U\left(\Delta \theta_{i j}\right)\left[\begin{array}{c}
\alpha_{i j} \\
\beta_{i j}
\end{array}\right]} \\
U\left(\Delta \theta_{i j}\right)=\left[\begin{array}{cc}
\cos \Delta \theta_{i j} & -\sin \Delta \theta_{i j} \\
\sin \Delta \theta_{i j} & \cos \Delta \theta_{i j}
\end{array}\right] \\
\Delta \theta_{i j}=\left|\Delta \theta_{i j}\right| s\left(\alpha_{i j}, \beta_{i j}\right)
\end{gathered}
$$

where $U\left(\Delta \theta_{i j}\right)$ is quantum gate, $\Delta \theta_{i j}$ is rotation angle. $\left|\Delta \theta_{i j}\right|$ and $s\left(\alpha_{i j}, \beta_{i j}\right)$ are the size and sign of $\Delta \theta_{i j}$.

### 3.2 Improvement of QGA

Constraint (19) is used to confine the qubit to the first quadrant as the basis of the subsequent improved method.

$$
\left\{\begin{array}{c}
\alpha_{i j}^{2}+\beta_{i j}^{2}=1 \\
0 \leq \alpha_{i j} \leq 1 \\
0 \leq \beta_{i j} \leq 1
\end{array}\right.
$$

### 3.2.1 Historical optimal solution retention mechanism

In DE-QGA, the population uses the historical optimal solution $H b e s t$ to update the quantum gate instead of the current generation optimal solution, so as to improve the probability of population updating to the optimal direction and accelerate the convergence speed of the algorithm. The rotation angle based on $H b e s t$ table is shown in Table 1.

Table 1: Rotation Angle Based on $H b e s t$

Where $J(\cdot)$ is the objective function, and $b_{i j}$ and $H b e s t_{i j}$ are the $i j^{\text {th }}$ bits of $p_{l}$ and $H b e s t$, respectively.

### 3.2.2 Estimation of distribution algorithm

The EDA is introduced to predict the evolution direction of the population by using the weighted average of the dominant individuals of the population, so that the population can

be updated according to the evolution direction of the population with a certain probability and reduce the probability of the algorithm falling into the local optimum.

As can be seen from Fig. 4, each qubit corresponds to an angle [18], so each angle chromosome $\varphi_{l}$ can be defined as:

$$
\begin{gathered}
\varphi_{l}=\left[\begin{array}{cccc}
\theta_{11} & \theta_{12} & \cdots & \theta_{1 N_{t}} \\
\theta_{21} & \theta_{22} & \cdots & \theta_{2 N_{t}} \\
\cdots & \cdots & \cdots & \\
\theta_{N_{u} 1} & \theta_{N_{u} 1} & \cdots & \theta_{N_{u} N_{t}}
\end{array}\right] \\
\theta_{i j}=\arccos \alpha_{i j}
\end{gathered}
$$

The weighted average of the dominant individuals of the population D better is calculated as the following:

$$
\begin{gathered}
\text { D better }=\sum_{l=1}^{m} \omega_{l} \cdot \varphi_{l} \\
\omega_{l}=(\ln (m+1)-\ln (l)) / \sum_{l=1}^{m}(\ln (m+1)-\ln (l))
\end{gathered}
$$

The half of population with lower objective function value is chosen as the dominant population. In (22), $m=N / 2$, and $\varphi_{1}, \varphi_{2}, \ldots, \varphi_{m}$ are the $m$ dominant individuals with the objective function values of the corresponding binary solutions ranked from low to high. Formula (23) means that the higher the ranking, the greater the weight coefficient. The rotation angle based on D better table is shown in Table 2.

Table 2: Rotation Angle Based on D better
Where $\theta_{i j}$ and $D$ better $_{i j}$ are the $i j^{\text {th }}$ bits of $\varphi_{l}$ and D better, respectively.

### 3.2.3 Adaptive probability parameter

In Fig. 3, $P v=\left\{p v_{1}, p v_{2}, \ldots, p v_{N}\right\}$ is adaptive probability parameter, which is adopted to choose the quantum gate update strategies. After each iteration, $P v$ is adaptively updated based on evolution information. If quantum gate based on $H$ best is selected to generate the offspring and the objective function value is reduced, or quantum gate based on D better is selected to generate the offspring and the objective function value is increased, $p v_{l}$ is updated as follows:

$$
p v_{l}^{\prime}=p v_{l}-0.1 \cdot p v_{l} \cdot\left(1-t / t_{\max }\right)
$$

If not, $p v_{l}$ is updated as follows:

$$
p v_{l}^{\prime}=p v_{l}+0.1 \cdot\left(1-p v_{l}\right) \cdot t / t_{\max }
$$

where $t$ is current iteration time, $t_{\max }$ is maximum iteration time.

### 3.2.4 Gene repair strategy

In order to make $p_{l}$ as feasible as possible, $p_{l}$ is repaired according to the constraint (4). Firstly, $p_{l}$ is checked row by row. If the same UAV participates in $n$ synchronous tasks at
a time, the $n-1$ genes with a value of 1 in the synchronous task genes are randomly selected to become 0 .

Fig. 5 depicts an example of gene repair process. The two yellow genes represent two tasks in synchronous relationship. And they are assigned to the same UAV, so the UAV abandons one of the synchronization tasks at random.
![img-4.jpeg](img-4.jpeg)

Fig. 5: Gene repair strategy

## 4 Simulation results and analysis

To evaluate the performance of DE-QGA algorithm, three scenarios with different number of UAVs and tasks were simulated, namely 4 tasks allocated to 8 UAVs, 8 tasks allocated to 16 UAVs, and 16 tasks allocated to 32 UAVs. It is assumed that the task sequence has been planned in advance.

### 4.1 Scenario I

In an area of 50 km * 50 km , there are 8 UAVs which need to perform 4 tasks. The task sequence is shown as Fig. 6. And scenario I provides detailed tasks and UAVs information, which are shown in Table 3 and Table 4, respectively.
![img-5.jpeg](img-5.jpeg)

Fig. 6: Scenario I task sequence diagram
Table 3: Tasks Information Table

Table 4: UAVs Information Table

![img-6.jpeg](img-6.jpeg)

Fig. 7: Algorithm convergence comparison graph

Fig. 7 displays the convergence curves of the objective function values of the three algorithms with the same iteration time, which are original QGA [9], Multiple Operators Based Adaptive Parallel Quantum Genetic Algorithm (MOP-AQGA) [19] and proposed DE-QGA, respectively. All the three algorithms converge to the same objective function value of 1.808 , but the convergence time of the three algorithms are $12.66 \mathrm{~s}, 9.52 \mathrm{~s}$ and 4.41 s , which demonstrates that the proposed algorithm has a faster convergence speed when dealing with scenario I.
![img-7.jpeg](img-7.jpeg)

Fig. 8: UAV task and allocation timing diagram
Fig. 8 shows the task assignment results and execution time of multi-UAV coalition obtained by the DE-QGA algorithm in Scenario I. Different colors represent different tasks, and the numbers in the figure represent the serial number of UAVs. As seen in the figure, each task is completed by a coalition of several UAVs, and the resources of the coalition are greater than or equal to the resources required by the corresponding task to ensure that each task is successfully executed. The result indicates the feasibility of the task allocation scheme obtained by the proposed algorithm.

### 4.2 Scenario II and Scenario III

In order to further verify the impact of problem scale expansion on the proposed algorithm, scenario II and scenario III are set for simulation experiments, which have higher dimension and wider search range.

Scenario II: In an area of $100 \mathrm{~km} * 100 \mathrm{~km}$, there are 16 UAVs which need to perform 8 tasks. The task sequence is shown as Fig. 9(a).

Scenario III: In an area of $200 \mathrm{~km} * 200 \mathrm{~km}$, there are 32 UAVs which need to perform 16 tasks. The task sequence is shown as Fig. 9(b).
![img-8.jpeg](img-8.jpeg)

Fig. 9: Task sequence diagram
Fig. 10 displays the objective function value convergence curves of the three algorithms in two scenarios. As the problem scale expands, the three algorithms no longer converge to the same objective function value, and the convergence time also increases. However, the DE-QGA obtains a
![img-9.jpeg](img-9.jpeg)

Fig. 10: Algorithm convergence comparison graph
lower objective function value than the other two algorithms in both scenarios, and the convergence speed is also faster, which is consistent with the theoretical analysis.
![img-10.jpeg](img-10.jpeg)

Fig. 11: Algorithm statistical comparison diagram
In scenario II, the three algorithms are run independently for 50 times with each iteration lasting for 2 minutes, and the statistical data box diagram obtained is shown in Fig. 11(a). Similarly, in scenario III, the three algorithms are run independently for 30 times with each iteration lasting for 8 minutes, and the statistical data box diagram obtained is shown in Fig. 11(b). It can be observed that not only DE-QGA box body is evidently lower than QGA and MOP-AQGA algorithms, but also the results of DE-QGA are more concen-

trated, which prove that DE-QGA has better solving ability and stability no matter which scenario to deal with. Moreover, the larger the problem dimension is, the more obvious the advantage of DE-QGA has.
![img-11.jpeg](img-11.jpeg)

Fig. 12: UAV task and allocation timing diagram
Fig. 12 shows the allocation result of DE-QGA algorithm in two scenarios. Each task is assigned a corresponding UAV coalition, which proves that DE-QGA algorithm can complete task allocation in complex scenarios. And there is no intersection between the coalitions executing synchronous tasks, which indicates that the proposed algorithm obtains the global optimal solution under the constraint conditions. In addition, there are intersections between the coalitions executing sequential tasks, because after the coalition completes the current task, if the UAVs in the coalition have any remaining resources, they can continue to join the subsequent coalition.

## 5 Conclusion

In this paper, the multi-task allocation of multi-UAV coalition is solved based on the DE-QGA. In the solution process, historical optimal solution retention mechanism, EDA and gene repair strategy are introduced to improve the performance of the algorithm. The simulation results show that the proposed algorithm has good convergence and optimization under different scale scenarios.

However, as the proposed algorithm is time-consuming, it is not suitable for handling dynamic situations during task execution. In the future, we will introduce the distributed control methods to study the dynamic adjustment strategy of task assignment scheme in response to uncertain emergencies.
