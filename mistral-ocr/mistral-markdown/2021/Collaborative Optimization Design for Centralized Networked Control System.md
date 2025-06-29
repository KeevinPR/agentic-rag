# Collaborative Optimization Design for Centralized Networked Control System 

XIANG YAN ${ }^{(1)}$, (Member, IEEE), JUN LI ${ }^{1}$, AND BIZHOU MEI ${ }^{2}$<br>${ }^{1}$ School of Information and Intelligence Engineering, Zhejiang Wands University, Ningbo 315000, China<br>${ }^{2}$ Zhejiang Yi Duan Machinery Company, Ningbo 315000, China<br>Corresponding author: Xiang Yan (yanxiang@zwu.edu.cn)


#### Abstract

This work was supported in part by the Natural Science Foundation of Ningbo City of China under Grant 2019A610121, in part by the General Project of Zhejiang Provincial Department of Education under Grant Y201942596, and in part by the Public Welfare Project of Ningbo City of China under Grant 2017C50028.


#### Abstract

This paper proposes a collaborative optimization design for a kind of centralized networked control system based on jitter. After the analysis of the network delay and jitter on the performance of the Train Networked Control System (TNCS) based on the MVB (Multifunction Vehicle Bus) network, the proposed strategy modifies the media allocating model of MVB directly related to the performance of the control system. Under the premise of ensuring the stability of the control system, and taking into account the impact of transmission jitter on the dynamic performance of the closed-loop control, this collaborative design method can minimize the network resource occupancy rate of the subsystem. Thus, it can overcome schedule failure in the traditional algorithm that excessively occupies network resources in order to reduce jitter. Finally, the authors present an algorithm based on EDA to find the optimal solution of the proposed strategy and illustrate the effectiveness of the strategy through numerical simulation and experimental tests.


#### Abstract

INDEX TERMS Train networked control system, jitter, estimation of distribution algorithm.


## I. INTRODUCTION

The networked control system (NCS) is a distributed control system that forms closed-loop feedback through network, integrates communication network and control system. Compared with conventional point-to-point interconnected control systems, NCS has the advantages of strong interaction, less wiring, and convenient expansion. Therefore, it is widely used in the fields of national defense, aerospace, equipment manufacturing, intelligent transportation, process control and economic management [1]-[3]. Train Networked Control System (TNCS) is the key technology of intelligent high-speed rail [4], and it is also a typical and important application of NCS in the railway field. Furthermore, the core network protocol of TNCS adopts the master-slave network MVB (Multifunction Vehicle Bus), thus TNCS belongs to centralized control NCS.

In centralized control NCS, each network control loop shares the same transmission channel with other closed loops. When multiple network nodes need to send data at the same time, a sharing conflict occurs. Therefore, the performance of the control system depends not only on the

The associate editor coordinating the review of this manuscript and approving it for publication was Haipeng Yao ${ }^{\text {® }}$.
control algorithm but also on the scheduling of shared network resources [5], [6]. Especially under the condition of limited network resources, how to share the network time allocation among sensors, controllers and actuators is one of the key factors to determine the performance of NCS. Therefore, it is very essential to design an appropriate real-time scheduling algorithm to ensure the quality of service of a communication network.

In recent years, the main research direction of NCS is to reduce the influence of delay [7], [8], packet loss [9], [10], and packet disorder [11] on control performance by studying control strategies under the premise of known network conditions. However, ignoring the complex dynamic behavior of the network and studying TNCS only from the perspective of control will be difficult to apply to complex practical systems. With the deepening of the research on NCS, the integrated design strategy of both control and scheduling has attracted more attention. The design idea of this collaborative design strategy is to use the results of the real-time scheduling theory to combine the effective sharing of network resources with control design.

The collaborative design of scheduling and control can be divided into two categories: one is the real-time calculation method based on real-time feedback theory, the other

is to maximize the performance of the control system during the collaborative design. Concerning the first catagory, Martí et al. [12] proposed a cooperative design method combining adaptive controller and feedback scheduling strategy, which overcomes some limitations of the execution platform and can dynamically adjust the control system performance through message scheduling. Xia et al. [13] proposed a neural network scheduling method based on a feedback schedule. By dynamically adjusting the control task cycle, the system can still obtain suitable control performance under the conditions of resource constraints and load uncertainty. Gao and Fan [14] proposed a hierarchical scheduling strategy based on fuzzy feedback, which comprehensively considered the control performance requirements of the control loop and the network service quality requirements of non-real-time nodes.
As for the second type, Otanez et al. [15] proposed a cooperative design method of NCS considering both network utilization and tracking performance for the proposed dead zone dynamic scheduling strategy, and discussed the transmission dead zone threshold optimization problem. Under the dual constraints of schedulability and system stability, Zhang et al. [16] proposed a cooperative design algorithm based on RM to determine the sampling period offline. Based on MADB collaborative design algorithm, Kim et al. [17] simplifies the complexity of control and scheduling problems by transforming the stability constraints in NCS design into controlling the transmission interval in MADB. For the given network (Token, CAN), Bai [18] proposed a cooperative design method based on jitter. In this method, the bandwidth allocation problem in NCS is described as a multi-objective optimization problem. The objective function is the weighted sum of network occupancy and transmission jitter. Both of them are functions of the sampling period. The constraints are network bandwidth resource constraints and control performance constraints. The optimal solution of the sampling period is obtained when the objective function is very small and can be obtained by a genetic algorithm. However, this design method is limited to a specific distributed control network. Thus, it is not suitable for the research object of this paper.
To sum up, the collaborative design strategy that takes into account the control performance and network service quality has attracted more attention. To optimize the control performance of the TNCS based on MVB, this article mainly discusses a collaborative optimization design based on jitter. However, the traditional algorithm by Hong [19], [20] may cause excessive occupation of bandwidth resources, leading to scheduling failures. For seeking a trade-off between the performance of the control system and the occupation of the network resource, the media allocation of MVB is modified and a jitter-based collaborative design optimization model is proposed. Furthermore, one kind of estimation of distribution algorithm (EDA) is given to solve the optimal solution.
The remainder of this paper is organized as follows: Section 2 analysis the stability of the TNCS and gives the transmission jitter model. Section 3 explains the proposed
scheme. Simulation results are provided in Section 4 and the paper concludes in Section 5.

## II. PROBLEM FORMULATION

## A. STABILITY ANALYSIS OF TNCS

For networked control systems, stability refers to the certainty and anti-interference ability of network control system behavior characteristics. Its stability is determined by the control network and control system. This paper mainly considers the influence of network scheduling in the control network on the stability of the whole system. As for the stability analysis of the controlled object, refer to the relevant references [21], [22]. In order to explore the influence of network quality on control performance, several basic assumptions are added in this paper:
(1) TNCS based on MVB adopts topology structure of bus type and distributed frame. It has $M$ control loops. Since the actuator generally does not send data, each control loop has two data transmission nodes, sensor node and controller node, so the total network data transmission node is $N=2 M$, as shown in Figure 1. The actuator is event driven, while the sensor and controller are time driven. The sensors and controllers in the same control loop have the same sampling period and work synchronously.
(2) For the control loop $i$, the sampling period is $T_{i}$, and $T_{i} \leq T_{i+1}, \forall i$, the initial phase is $\varphi_{i}$, the closed-loop delay is $D_{i}$, the maximum allowable closed-loop delay is $\phi_{i}$, and $\phi_{i} \leq \phi_{i+1}, \forall i$, the data transmission rate is B , and the data length is fixed as $\overline{\mathrm{L}}$, then the data transmission time is $\mathrm{L}=\overline{\mathrm{L}} / B$. Moreover, the smaller the sampling period is, the higher the priority set. Because each control loop has two data sending nodes and the same sampling period, the control loop $i$ occupies two priority levels $\operatorname{im}(m=1,2)$ according to the sampling period, and the priority of the controller node is higher than the sensor in the same node. The network delay is defined as the time from the data reaches the sending node's sending queue to the data reaches the receiving node's receiving queue. Assuming that the sampling deviation and data processing time between the nodes are small enough to be negligible relative to the sampling period, $\theta_{i, 1}$ and $\theta_{i, 2}$ are defined as the delay from the sensor to the controller and the controller to the sensor in the $i$-th control loop, then the closed-loop delay $D_{i}$ can be calculated by formula (1). Figure 2 shows the closed-loop delay of the closed loop $i$.

$$
D_{i}=\left[\frac{\theta_{i, 1}}{T_{i}}\right] T_{i}+\theta_{i, 2}
$$

In terms of real-time periodic data, when the transmission delay is greater than the sampling period interval of the corresponding control closed-loop, multiple sampling data will arrive in a certain sampling period of the node. At this time, only the latest data is used, and other data will be discarded, resulting in "data filtering". However, in another sampling period, there may be no sampling data arriving, thus forming "empty sampling", as shown in Figure 2. "Data filtering" and "empty sampling" will cause distortion of the control signal

![img-0.jpeg](img-0.jpeg)

FIGURE 1. Schematic diagram of TNCS.
![img-1.jpeg](img-1.jpeg)

FIGURE 2. The closed-loop delay of the closed loop $i$.
and high-frequency noise, which will lead to unnecessary loss of actuator and degradation of the dynamic performance of control loop. Therefore, the transmission and scheduling of real-time periodic data must ensure that the network delay does not exceed one sampling period interval of the corresponding control loop. In order to avoid the phenomenon of data filtering and null sampling, the sampling data of sensor nodes must reach the corresponding controller nodes within the deadline, that is, before the next data sampling. At the same time, in order to ensure the stability of the control system, each control loop must satisfy the following two constraints [20]:

$$
\begin{gathered}
\theta_{i, m}<T_{i}, \quad m=1,2 \\
D_{i} \leq \phi_{i}
\end{gathered}
$$

For the closed loop $i$ with priority $i m$, when it is approaching to generate a data to be sent, there is no data with priority higher than $i m$ to be polled by the master in this basic cycle. The node of loop $i$ can send the data immediately, and the delay of the data is the minimum.

$$
\min \theta_{i, m}=L, \quad(m=1,2)
$$

![img-2.jpeg](img-2.jpeg)

FIGURE 3. Schematic diagram of the time-varying delay for loop $i$.
where $L$ refers to the transmission time of complete frame message, which is different according to different function code.

Otherwise, it needs to wait until all high-priority data has been sent and check whether the remaining cycle phase is enough to send the data. If it is not enough, then it needs to wait for the next basic cycle and continue to judge until there is no higher priority data to be sent and enough cycle phase. At this time, the time delay experienced is the largest:

$$
\begin{aligned}
\max \theta_{i, m} & =n_{i} T_{\mathrm{bp}}+r L \leq n_{i} T_{\mathrm{bp}}+\omega_{\mathrm{p}} T_{\mathrm{bp}} \\
& =\left(n_{i}+\omega_{\mathrm{p}}\right) T_{\mathrm{bp}}, \quad(m=1,2)
\end{aligned}
$$

where $n_{i}$ is the waiting number of the basic cycle, $r$ is the maximum time slice that can transmit data in a basic cycle, and $\omega_{\mathrm{p}}$ is the cycle proportion factor.

Reference [23] points out that the performance of feedback control system directly depends on the closed-loop delay. Since $\theta_{i, 2}$ is time-varying, the closed-loop delay $D_{i}$ is also time-varying. Simply replacing $\theta_{i, 2}$ with the upper bound $T_{i}$ of $\theta_{i, 2}$ is not conducive to the design of the control system. Therefore, reference [20], [23] provides an idea: assuming that $t_{k}$ is the time when the $k$-th control instruction arrives at the controlled object, then $t_{k+1}$ is the time when the $(k+1)$-thcontrol instruction arrives at the controlled object (regardless of packet loss and timing disorder). Due to the time-varying nature of $\theta_{i, 2}$, the time interval of $\left[t_{k}, t_{k+1}\right)$ is also time-varying, as shown in Figure 3. For the performance of the control system, the influence of the network delay is mainly reflected in the change of the time interval $\left[t_{k}, t_{k+1}\right)$, rather than the delay itself. If the $\theta_{i, 2}$ of $k$-th control instruction is the smallest while the $\theta_{i, 2}$ of $(k+1)$-th control instruction is the largest, then $\left[t_{k}, t_{k+1}\right)$ is the largest, which is $T_{i}+\left(\max \theta_{i, 2}-\min \theta_{i, 2}\right)$. Reference [23] also proves that if $\theta_{i, 2}$ is replaced with a fixed-length delay of $T_{i}+$ $\left(\max \theta_{i, 2}-\min \theta_{i, 2}\right)$, the stability requirements of the original time-varying delay system can still be met. Therefore, the closed-loop delay $D_{i}$ can be converted to the fixed-length delay $D_{i}^{\prime}$ :

$$
D_{i}^{\prime}=2 T_{i}+\left(\max \theta_{i, 2}-\min \theta_{i, 2}\right)
$$

## B. TRANSMISSION JITTER MODEL

The control variables of TNCS are usually transmitted periodically, which must meet certain design specifications and actual control requirements. In an independent closed-loop

control system, these transmission control requirements can be well met because there is no resource competition between nodes. However, in the networked control system, the introduction of network allows all nodes to share a limited bandwidth resource. One consequence of this is that it may not be able to ensure the invariability of the continuous transmission time interval between two nodes in the same closed-loop. Therefore, even if the network parameters are fixed, for a certain node, the network-induced delay is time-varying. The existence of varying sampling rate and delay can degrade the performance index of the original nominal system design, and even destroy the stability of the system. The main reason is that the control signal output time has changed, which is inconsistent with the controller design (synchronous control, sampling and execution without time delay). Ultimately, the instability of the control network may directly lead to the instability of the entire system.

This kind of unequal interval data transmission will cause fluctuation of data transmission, affect the real-time performance of the system and reduce the dynamic performance of the control system. In reference [24], this fluctuation is defined as the jitter of data transmission, which can be expressed as:

$$
j_{i, k}=t s_{i, k}-\left(k^{*} T_{i}+\varphi_{i}\right)
$$

where $t s_{i, k}$ and $\left(k^{*} T_{i}+\varphi_{i}\right)$ are the actual data transmission time and the generation time of the $k$-th data respectively

The jitter optimization scheduling problem of the TNCS can be described as the scheduling problem of the data transmission of each node in the $T$ period, and its mathematical model is:

$$
O S J=\sum_{i=1}^{N} \sum_{k=1}^{T f T_{i}} j_{i, k}=2 \sum_{i=1}^{M} \sum_{k=1}^{T f T_{i}} j_{i, k}
$$

The above model represents the sum of all data transmission jitter of all nodes in the macro period $T=$ $\operatorname{LCM}\left(T_{i}, i=1, \ldots, M\right)$. Since the above rules will be repeated in each $T$ period, thus, this paper only studies the transmission jitter problem caused by scheduling during the $T$ period.

## III. MAIN RESULT

## A. MVB MEDIA ALLOCATION METHOD

TCN standard, namely IEC61375-1 protocol [25], provides the media allocation mode of MVB, and defines the basic period $T_{\mathrm{bp}}$, characteristic period $T_{\mathrm{ip}}$ and macro period $T_{\mathrm{Mp}}$, where $T_{\mathrm{ip}}=2^{\mathrm{m}} T_{\mathrm{bp}}, \mathrm{m} \in\{0,1, \ldots, 10\}, T_{\mathrm{Mp}}=\max \left\{T_{\mathrm{ip}}\right\}$, $i \in\{1,2, \ldots, N\}$, which is consistent with the preset conditions in reference [19]. The bandwidth allocation and sampling period scheduling algorithm in reference [19] can be used to realize the non-jitter scheduling under ideal conditions. Although this method is simple and effective to avoid periodic jitter, it is at the cost of over using bandwidth resources. This will cause some closed loop cannot be served by network due to over-occupy resources of other network nodes. On the other hand, under the condition that the number of control loops (or network traffic) is fixed, more bandwidth resources are needed to make all control loops be served by the network, which increases the operation cost of the system. Therefore, by referring to reference [19], this paper proposes a scheduling optimization algorithm for centralized MVB network, which compromises bandwidth resource occupation and transmission jitter. By determining the optimal sampling period of each control loop in TNCS, the initial phase of each control loop is optimized to minimize the system jitter.

In order to implement the above scheduling optimization algorithm, the media allocation of MVB for period data needs to be modified as follows:
(1) The basic period $T_{\mathrm{bp}}$ is corrected to the minimum sampling period of the TNCS, i.e.,

$$
T_{\mathrm{bp}}=T_{1}
$$

According to the conditions (2) and (3), the data whose sampling period is $T_{1}$ must be completed within a basic period, then $n_{1}=0$. In addition, according to formulas (4), (5) and (6), as well as assuming $D_{1}^{\prime}=\phi_{1}, T_{1}$ can be determined:

$$
T_{1}=\frac{\phi_{1}+L}{2+\omega_{\mathrm{p}}}
$$

(2) The characteristic period of $T_{i}$ is modified as:

$$
\begin{aligned}
& T_{i}=k_{i} T_{\mathrm{bp}}=k_{i} T_{1} \leq T_{\mathrm{ip}} \\
& k_{i} \in\{1,2, \ldots, 1024\}, \quad i \in\{1,2, \ldots, N\}
\end{aligned}
$$

But the revised $T_{i}$ still needs to satisfy $T_{i} \leq T_{i+1}, \forall i$. Similarly, according to conditions (2) and (3), other sampling periods $T_{i}$ can be obtained:

$$
T_{i} \leq \frac{\phi_{i}-\left(\mathrm{n}_{i}+\omega_{\mathrm{p}}\right) \mathrm{T}_{1}+L}{2}
$$

then $k_{i}$ :

$$
k_{i}=\left\lfloor\frac{\phi_{i}-\left(\mathrm{n}_{i}+\omega_{\mathrm{p}}\right) T_{1}+L}{2 T_{1}}\right\rfloor
$$

where $n_{i} \in\left[0, k_{i}\right]$ satisfies conditions (2) and (3). In the above formula, $\lfloor\mathrm{X}\rfloor$ represents the largest integer whose value is not greater than X .
(3) Correspondingly, the macro period is no longer the maximum characteristic period, but:

$$
T_{\mathrm{Mp}}=\operatorname{LCM}_{i=1, \ldots, N}\left(T_{i}\right)=\min \left\{\psi\left|\frac{\psi}{T_{i}}=\left\lfloor\frac{\psi}{T_{i}}\right\rfloor\right\}\right.
$$

and for $\forall i \in[1, N], i$ and $\psi$ are all positive integers.
(4) In macro period $T_{\mathrm{Mp}}$, the total number of data to be transmitted is:

$$
\begin{aligned}
\sum_{i=1}^{N} \frac{T_{\mathrm{Mp}}}{T_{i}} & =\frac{T_{\mathrm{Mp}}}{T_{\mathrm{bp}}} \sum_{i=1}^{N} \frac{1}{k_{i}}=\zeta \frac{T_{\mathrm{Mp}}}{T_{\mathrm{bp}}} \\
\zeta & =\sum_{i=1}^{N} \frac{1}{k_{i}}
\end{aligned}
$$

Meanwhile, the number of time slices that the limited bandwidth can only produce is $r \frac{T_{\mathrm{Mp}}}{T_{\mathrm{bp}}}$. If the number of data to be transmitted is greater than the "windows" $r$ in $T_{\mathrm{Mp}}$, the network is overloaded and the real-time requirement of the system cannot be guaranteed, that means the network scheduling is failed. Only when $\zeta \leq r$, the system is schedulable, and the utilization ratio of network bandwidth resource is:

$$
U=\sum_{i=1}^{N} \frac{L}{T_{i}}=\frac{L}{T_{\mathrm{bp}}} \sum_{i=1}^{N} \frac{1}{k_{i}}=\zeta \frac{L}{T_{\mathrm{bp}}}
$$

## B. JITTER-BASED COLLABORATIVE DESIGN OPTIMIZATION MODEL

Transmission jitter is the fluctuation of the sampling period caused by the sharing of limited network resources by multiple nodes. Good control performance requires that the transmission jitter is as small as possible. However, the reduction of transmission jitter comes at the cost of consuming network resources. Therefore, the optimization problem to be solved in this paper is to determine the optimal sampling period and the optimal initial phase of each closed loop in the TNCS under the constraints of system dynamic performance and network schedulability. The expected result is to reduce the usage of the bandwidth resource by the subsystem as far as possible under the premise of ensuring the stability of the control system and considering the impact of transmission jitter on the dynamic performance of the control loop, so as to provide data transmission service for more control loops. Therefore, the bandwidth resource utilization of the whole system is improved. Based on the total transmission jitter $O S J$ of the system given above, the compromised bandwidth optimization scheduling problem can be described as the following mathematical form:

$$
\begin{aligned}
& \min J=\alpha_{1} U\left(T_{i}\right)+\alpha_{2} O \hat{S} J\left(T_{i}, \varphi_{i}\right) \\
& =\alpha_{1} \sum_{i=1}^{N} \frac{T_{\mathrm{mm}}^{i}}{T_{i}}+\alpha_{2} \sum_{i=1}^{N} \sum_{k=1}^{T_{\mathrm{M}} / T_{i}} \hat{j}_{i, k} \\
& \text { s.t } \max \theta_{i m} \leq T_{i}, \quad \forall i=1,2, \ldots, N \\
& T_{i} \leq T_{i+1}, \quad \forall i \\
& \alpha_{1}+\alpha_{2}=1
\end{aligned}
$$

where $\hat{j}_{i, k}=\left(t s_{i, k}-\left(k^{*} T_{i}+\varphi_{i}\right)\right) / T_{i}, T_{i}$, and $\varphi_{i}$ are variables needed to be optimized, $T_{\mathrm{mm}}^{i}$ is the length of the period data $T_{i}, \alpha_{1}$ and $\alpha_{2}$ are the weighting factors of the objective function, reflecting the needs of users for different performance of the system. When the multi-objective optimization requirements of bandwidth resource utilization and control system performance (transmission jitter) are met, load balance can be further considered.

The solution of problem (15) mainly involves two groups of optimization variables $\left\{T_{i}\right\}$ and $\left\{\varphi_{i}\right\}$, and there is a certain coupling relationship between these two groups, that is, $\varphi_{i}<$ $T_{i}, \forall i$, and $T_{i} \leq T_{i+1}, \forall i$. A new optimization model is needed to describe the relationship of variables under this constraint, so as to obtain the optimal solution of problem (15) more effectively.

## C. EDA ALGORITHM DESIGN

The estimation of distribution algorithms (EDA) is a new optimization algorithm [26]. Different from the traditional optimization algorithm based on individual population evolution (crossover, mutation, etc.) to realize population evolution, the EDA directly describes the evolutionary trend of the entire group, and uses a probability model for learning and sampling. As a new tool for solving complex optimization problems, EDA can describe the relationship between variables through probability model, which makes it more effective for solving nonlinear and variable coupling optimization problems. Therefore, this paper introduces EDA to solve the scheduling optimization problem of collaborative design based on jitter.

The $i$-th optimization vector in this paper can be designed as (19), shown at the bottom of the page, where $T_{j}^{i}$ represents the sampling period of the closed-loop $j, \varphi_{j, 1}^{i}$ and $\varphi_{j, 2}^{i}$ respectively represent the initial phase of data transmission of the controller and sensor of the closed-loop $j$.

There are coupling constraints between the sampling period and the initial phase of each closed loop. Thus, this paper obtains the optimal value by directly completing the evolution based on EDA for the population of vector $\mathbf{B}$. The algorithm is designed as follows:

Step 1: Initialize the first generation of effective population $\mathbf{B}_{0}$. The initial population is randomly generated in the solution space according to uniform distribution. Due to the need to meet $T_{i} \leq T_{i+1}, \forall i$ and schedulability constraints, each group of randomly generated vectors $\mathbf{B}_{0, i}$ should be tested for effectiveness first, and those that are not satisfied should be eliminated directly until the effective initial population $\mathbf{B}_{0}$ with population size P is obtained.

Step 2: Evaluate the group. Calculate the fitness value $J_{i}$ of each individual, and select the first half to form the dominant group $\mathrm{X}_{\mathrm{s}}$.

Step 3: Construct a probability model describing the solution space. Construct a probability model based on Gaussian distribution from this dominant group $\mathrm{X}_{\mathrm{s}}$.

Step 4: Generate a new generation of population from the probability model. The Monte Carlo method is used to estimate the mean vector and covariance matrix of the multivariate Gaussian distribution. Sampling by the probability model to obtain a new population, and judge the validity of the

$$
\mathbf{B}_{i}=\left[T_{1}^{i}, T_{2}^{i}, \ldots, T_{j}^{i}, \ldots, T_{M}^{i}, \varphi_{1,1}^{i}, \varphi_{1,2}^{i}, \ldots, \varphi_{j, 1}^{i}, \varphi_{j, 2}^{i}, \ldots, \varphi_{M, 1}^{i}, \varphi_{M, 2}^{i}\right]
$$

new individual, turn to Step 2 until the evolution conditions are satisfied.

## IV. EXPERIMENT AND RESULT ANALYSIS

## A. NUMERICAL SIMULATION

In order to verify the effectiveness of the algorithm, this paper uses MATLAB to realize the above optimization scheduling algorithm. Comparing with the algorithm provided in references [19], [20], a numerical simulation is carried out. Suppose that a TNCS based on MVB has five control loops. Each controller and sensor of the closed loop are equipped with one source port and one sink port, and the actuator is configured with one sink port. The maximum allowable closed-loop delay of each control loop is $\left[\phi_{1}, \phi_{2}, \phi_{3}, \phi_{4}, \phi_{5}\right]=[6,15,25,30,40] \mathrm{ms}$, the data transmission rate is $\mathrm{B}=1.5 \mathrm{Mbit} / \mathrm{s}$, the periodic phase scale factor is $\omega_{\mathrm{P}}=0.65$, and all source port data function codes are F_code $=4$, then the message transmission time is $L=$ 0.265 ms . According to the modified MVB medium allocation model, the minimum sampling period is $T_{1}=2 \mathrm{~ms}$, and the "window" $r=4$ with $T_{1}$ as the basic period can be obtained. According to equation (13), the maximum values of other closed-loop $k_{i}$ are $3,5,7$ and 9 , respectively.

Then, according to equation (11), the value range of other sampling periods can be calculated, and $T_{i} \leq T_{i+1}, \forall i$ should be satisfied at the same time. Furthermore, according to the given EDA design algorithm, the optimal combination of sampling period and initial phase of each control loop is obtained. And some simulation results are shown in Table 1, in which, the fitness function is $\mathrm{Fit}=100 /(O S J+1)$ and $O S J$ is the total transmission jitter caused by scheduling. If the scheduling cannot meet the real-time and jitter conditions, which means the constraint (3) is failed, then $O S J=$ 99. Therefore, the higher the fitness, the smaller the jitter value of the system. When the fitness is 100 , there is no transmission jitter in the system. When the fitness is between $(1,100)$, it indicates that the system can be scheduled with jitter.

From the simulation results, there are multiple scheduling optimization solutions without jitter in the given TNCS based on MVB. Taking the first group of simulation results as an example, the sampling period of each control loop is $\left[T_{1}, T_{2}, T_{3}, T_{4}, T_{5}\right]=[2,6,6,12,12] \mathrm{ms}$. And $\zeta=4 \leq r$, which satisfies the network schedulability condition. Besides, bandwidth utilization rate $U=53.00 \%$. And the maximum closed-loop delay for each control loop are $4 \mathrm{~ms}, 12 \mathrm{~ms}, 12 \mathrm{~ms}$, 24 ms and 24 ms respectively, which are less than the maximum allowable closed-loop delay $\phi_{t}$, and meet the stability conditions of the control system. At the same time, it can also be found that there is an optimal solution (bandwidth utilization rate $U=47.36 \%$ ) with the minimum bandwidth resource occupation. The sampling period of each control loop is $\left[T_{1}, T_{2}, T_{3}, T_{4}, T_{5}\right]=[2,6,10,14,18] \mathrm{ms}$. And $\zeta=3.57<r$, which satisfies the network schedulability condition. The maximum closed-loop delay for each control
loop are $4 \mathrm{~ms}, 12 \mathrm{~ms}, 20 \mathrm{~ms}, 28 \mathrm{~ms}$ and 36 ms respectively, which are all less than the maximum allowable closed-loop delay $\phi_{t}$, which satisfies the stability condition of the control system. However, there exists transmission jitter caused by scheduling. As for the given TNCS based on MVB, the selection of optimal solution also depends on the needs of users, which can be achieved by setting the weighting factors $\alpha_{1}$ and $\alpha_{2}$.

If using the scheduling algorithm of references [19, 20], the sampling period of each control loop is set as $2^{k}$ times the reference period, which means the sampling period is $\left[T_{1}, T_{2}, T_{3}, T_{4}, T_{5}\right]=[2,4,8,8,16] \mathrm{ms}$ and $\zeta=4.25>r$. Thus, the scheduling fails. It shows that under the same network parameter conditions, the scheduling algorithm cannot realize the scheduling of all control loops, so more bandwidth resources are needed. To realize the schedulability of this TNCS, the only way to change the system structure by reducing the number of transmission nodes or increasing bandwidth resources will inevitably lead to an increase in design and operating costs. By comparing with the scheduling algorithms in references [19], [20], the jitter-based MVB collaborative design optimization algorithm proposed in this paper can fully and reasonably allocate bandwidth resources under the condition of meeting the delay requirements of the control system. In addition, it can realize no jitter or minimum jitter optimized scheduling of real-time periodic data. Thereby, the dynamic performance requirements of the system are ensured.

## B. EXPERIMENTAL VERIFICATION

In order to verify the optimization algorithm proposed in this paper furthermore, an experimental platform for TNCS delay test is built based on MVB. The topology is shown in Figure 4, including a MPA protocol analyzer for monitoring network data. There are six VCUs (Vehicle Control Unite) developed independently as MVB network nodes, one of which is acted as the MVB bus master, five simulation nodes (consist of mvb2usb protocol conversion device + PC) called SimNode are acted as the other five MVB slave nodes. And each network node is configured with corresponding source and sink ports. Taking control loop 1 as an example, VCU1 is configured with a source port to send control information to the actuator, and a sink port is configured to receive sensor information. As the controlled object, SimNode1 includes both sensors and actuators. A source port is configured to send feedback information and a sink port is configured to receive controller information. Therefore, a closed-loop control system consists of two sending data nodes. The parameters of each closed loop are set according to the numerical simulation examples except the sampling period and initial phase using the following three groups of test data. The detailed configuration table of the equipment is shown in Table 2. At the same time, using MPA to capture all the MVB network data online, the delay and jitter of all control loops can be obtained according to the sampling period and time synchronization of each control loop. It should be noted

TABLE 1. The optimal solution of MVB sampling period and the initial phase.

| $\mathrm{T}_{1}, \varphi_{1,1}$ | $\mathrm{~T}_{1}, \varphi_{1,2}$ | $\mathrm{~T}_{2}, \varphi_{2,1}$ | $\mathrm{~T}_{2}, \varphi_{2,2}$ | $\mathrm{~T}_{3}, \varphi_{3,1}$ | $\mathrm{~T}_{3}, \varphi_{3,2}$ | $\mathrm{~T}_{4}, \varphi_{4,1}$ | $\mathrm{~T}_{4}, \varphi_{4,2}$ | $\mathrm{~T}_{5}, \varphi_{5,1}$ | $\mathrm{~T}_{5}, \varphi_{5,2}$ | Fitness | U\% |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 2,0 | 2,0 | 6,2 | 6,4 | 6,0 | 6,2 | 12,0 | 12,4 | 12,6 | 12,10 | 100 | 53.00 |
| 2,0 | 2,0 | 6,0 | 6,2 | 6,2 | 6,0 | 12,10 | 12,4 | 18,10 | 18,4 | 100 | 51.53 |
| 2,0 | 2,0 | 6,4 | 6,0 | 8,4 | 8,0 | 12,6 | 12,10 | 12,8 | 12,2 | 100 | 50.79 |
| 2,0 | 2,0 | 6,2 | 6,4 | 8,2 | 8,4 | 12,0 | 12,6 | 16,8 | 16,14 | 100 | 49.69 |
| 2,0 | 2,0 | 6,4 | 6,2 | 10,8 | 10,4 | 10,6 | 10,0 | 18,6 | 18,12 | 100 | 48.88 |
| 2,0 | 2,0 | 6,4 | 6,0 | 6,2 | 6,4 | 12,2 | 12,6 | 16,8 | 16,0 | 66.67 | 51.90 |
| 2,0 | 2,0 | 6,4 | 6,2 | 10,2 | 10,6 | 12,6 | 12,0 | 18,10 | 18,14 | 52.4 | 47.99 |
| 2,0 | 2,0 | 6,4 | 6,0 | 10,4 | 10,8 | 12,8 | 12,2 | 16,6 | 16,2 | 40.00 | 48.36 |
| 2,0 | 2,0 | 6,4 | 6,2 | 10,0 | 10,6 | 12,6 | 12,0 | 14,0 | 14,10 | 22.58 | 48.84 |
| 2,0 | 2,0 | 6,4 | 6,2 | 10,8 | 10,2 | 14,0 | 14,8 | 18,0 | 18,6 | 18.81 | 47.36 |

![img-3.jpeg](img-3.jpeg)

FIGURE 4. The topology of the TNCS delay test.

TABLE 2. Network device address and port allocation table.

| device | device address | source port | sink port |
| :--: | :--: | :--: | :--: |
| VCU1 | 0x01 | 0x4001 | 0x4002 |
| SimNode 1 | 0x02 | 0x4002 | 0x4001 |
| VCU2 | 0x03 | 0x4003 | 0x4004 |
| SimNode 2 | 0x04 | 0x4004 | 0x4003 |
| VCU3 | 0x05 | 0x4005 | 0x4006 |
| SimNode 3 | 0x06 | 0x4006 | 0x4005 |
| VCU4 | 0x07 | 0x4007 | 0x4008 |
| SimNode 4 | 0x08 | 0x4008 | 0x4007 |
| VCU5 | 0x09 | 0x4009 | 0x400A |
| SimNode 5 | 0x0A | 0x400A | 0x4009 |

that the measured delay is directly obtained from the MVB network data analysis, not the actual arrival delay of data in each control loop.
(1) Test data 1:

The first group of simulation results with no jitter in Table 1 obtained by using the jitter-based collaborative design optimization algorithm, thus, the closed-loop sampling period is:

$$
\left[T_{1}, T_{2}, T_{3}, T_{4}, T_{5}\right]=[2,6,6,12,12] \mathrm{ms}
$$

TABLE 3. Real-time performance of test data 1 (time unit: ms).

|  | min delay |  | max delay |  | average delay |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $\theta_{d 1}$ | $\theta_{d 2}$ | $\theta_{d 3}$ | $\theta_{d 2}$ | $\theta_{d 3}$ | $\theta_{d 2}$ |
| Loop 1 | 0.53 | 0.27 | 0.53 | 0.27 | 0.53 | 0.27 |
| Loop 2 | 0.80 | 0.80 | 0.80 | 0.80 | 0.80 | 0.80 |
| Loop 3 | 1.06 | 0.80 | 1.06 | 0.80 | 1.06 | 0.80 |
| Loop 4 | 1.06 | 1.06 | 1.06 | 1.06 | 1.06 | 1.06 |
| Loop 5 | 1.06 | 1.06 | 1.06 | 1.06 | 1.06 | 1.06 |

The initial phase is:

$$
\begin{aligned}
& {\left[\psi_{1,1}, \psi_{1,2}, \ldots, \psi_{i, 1}, \psi_{i, 2}, \ldots, \psi_{5,1}, \psi_{5,2}\right]} \\
& \quad=[0,0,2,4,0,2,0,4,6,10] \mathrm{ms}
\end{aligned}
$$

(2) Test data 2:

Using the same control closed-loop sampling period as test data 1, but without considering data jitter, the initial phase is:

$$
\begin{aligned}
& {\left[\psi_{1,1}, \psi_{1,2}, \ldots, \psi_{i, 1}, \psi_{i, 2}, \ldots, \psi_{5,1}, \psi_{5,2}\right]} \\
& \quad=[0,0,0,0,0,0,0,0,0,0] \mathrm{ms}
\end{aligned}
$$

(3) Test data 3:

The final group of simulation results with jitter in Table 1 obtained by using the jitter-based collaborative design optimization algorithm, thus, the closed-loop sampling period is:

$$
\left[T_{1}, T_{2}, T_{3}, T_{4}, T_{5}\right]=[2,6,10,14,18] \mathrm{ms}
$$

The initial phase is:

$$
\begin{aligned}
& {\left[\psi_{1,1}, \psi_{1,2}, \ldots, \psi_{i, 1}, \psi_{i, 2}, \ldots, \psi_{5,1}, \psi_{5,2}\right]} \\
& \quad=[0,0,4,2,8,2,0,8,0,6] \mathrm{ms}
\end{aligned}
$$

According to test data 1, the real-time data service performance of the system is obtained as shown in Table 3. Because the priority of the controller node in each control loop is higher than the sensor node, the delay of the real-time

TABLE 4. Real-time performance of test data 2 (time unit: ms).

|  | min delay |  | max delay |  | average delay |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | $\theta_{s 1}$ | $\theta_{s 2}$ | $\theta_{s 1}$ | $\theta_{s 2}$ | $\theta_{s 1}$ | $\theta_{s 2}$ |
| Loop 1 | 0.53 | 0.27 | 0.53 | 0.27 | 0.53 | 0.27 |
| Loop 2 | 1.06 | 0.80 | 1.06 | 0.80 | 1.06 | 0.80 |
| Loop 3 | 3.06 | 2.80 | 3.06 | 2.80 | 3.06 | 2.80 |
| Loop 4 | 5.06 | 4.80 | 5.06 | 4.80 | 5.06 | 4.80 |
| Loop 5 | 11.06 | 10.80 | 11.06 | 10.80 | 11.06 | 10.80 |

TABLE 5. Real-time performance of test data 3 (time unit: ms).

|  | min delay |  | max delay |  | average delay |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | $\theta_{s 1}$ | $\theta_{s 2}$ | $\theta_{s 1}$ | $\theta_{s 2}$ | $\theta_{s 1}$ | $\theta_{s 2}$ |
| Loop 1 | 0.53 | 0.27 | 0.53 | 0.27 | 0.53 | 0.27 |
| Loop 2 | 0.80 | 0.80 | 0.80 | 0.80 | 0.80 | 0.80 |
| Loop 3 | 0.80 | 0.80 | 1.06 | 1.06 | 0.90 | 0.90 |
| Loop 4 | 0.80 | 0.80 | 3.06 | 3.06 | 1.41 | 1.41 |
| Loop 5 | 0.80 | 0.80 | 3.06 | 3.06 | 1.20 | 1.20 |

![img-4.jpeg](img-4.jpeg)

FIGURE 5. The average delay of the sensor node.
periodic data of the controller node may be smaller than the sensor node. The closed-loop delay of each control loop are $2.27 \mathrm{~ms}, 6.80 \mathrm{~ms}, 6.80 \mathrm{~ms}, 13.06 \mathrm{~ms}$ and 13.06 ms respectively, which are less than the maximum allowable closed-loop delay bound, so the performance of the control system can be guaranteed, and the network load rate is about $53 \%$. According to the test data 2, the real-time data service performance of the system is obtained as shown in Table 4. The closed-loop delay of each control loop are $2.27 \mathrm{~ms}, 6.80 \mathrm{~ms}, 10.80 \mathrm{~ms}, 14.80 \mathrm{~ms}$ and 22.80 ms respectively, which are all less than the maximum allowable closed-loop delay bound, and the network load rate is about $53 \%$. According to the test data 3, the realtime data service performance of the system is obtained as shown in Table 5. The closed-loop delay of each control loop are $2.27 \mathrm{~ms}, 6.80 \mathrm{~ms}, 11.06 \mathrm{~ms}, 17.06 \mathrm{~ms}$ and 21.06 ms respectively, which are all less than the maximum allowable closed-loop delay bound, but its network load rate is about $47 \%$. The real-time data service performance average delay and closed-loop delay comparison results of test data 1, test data 2 and test data 3 are shown in Figure 5, Figure 6 and Figure 7, respectively. From the above test results, we can
![img-5.jpeg](img-5.jpeg)

FIGURE 6. The average delay of the controller node.
![img-6.jpeg](img-6.jpeg)

FIGURE 7. The delay of the closed loop.
see that, the optimized scheduling algorithm proposed in this paper can reasonably and fully utilize the network resources when the network resources are certain. On the premise of satisfying the control performance, by adjusting the sampling period, the bandwidth resource occupation of each control loop can be reduced as much as possible. In addition, it can also solve the problem that the scheduling algorithm in reference $[19,20]$ can't solve, that is, the network cannot serve all nodes due to excessive resource occupation by some nodes. On the other hand, a jitter scheduling is achieved while meeting the system delay requirements. The real-time data service performance of this method is better than that without considering jitter, so as to better ensure the dynamic performance requirements of the system.

## v. CONCLUSION

Aiming at the centralized network, the relationship between sampling period of control loop and control performance is studied, and the influence of network delay and jitter on the performance of networked control system is analyzed. The MVB media allocation model, which is directly related to the performance of the control system, is modified. A jitter based bandwidth scheduling algorithm for MVB collaborative design is proposed. Under the jitter constraints, a tradeoff between control performance and bandwidth consumption is achieved. Thus, the network resource occupancy rate of the subsystem is reduced, and the scheduling failure problem of the traditional algorithm is overcome. Finally, the optimal

solution of the proposed design is realized by the algorithm based on EDA, and the effectiveness and practicability of the method are verified by simulation and experimental tests.

## REFERENCES

[1] X. Ge, F. Yang, and Q. L. Han, "Distributed networked control systems: A brief overview," Inf. Sci., vol. 380, pp. 117-131, Feb. 2017.
[2] X.-M. Zhang, Q.-L. Han, X. Ge, D. Ding, L. Ding, D. Yue, and C. Peng, "Networked control systems: A survey of trends and techniques," IEEE/CAA J. Automatica Sinica, vol. 7, no. 1, pp. 1-17, Jan. 2020.
[3] X. Yan, Y. Sun, and B. Mei, "Dynamic bandwidth scheduling of software defined networked collaborative control system," IEEE Access, vol. 8, pp. 75968-75975, 2020, doi: 10.1109/ACCESS.2020.2989414.
[4] T. Zhang, C.-X. Li, and Z.-L. Li, "Generalized predictive control and delay compensation for high-Speed EMU network control system," in Proc. 6th Int. Conf. Comput. Sci. Netw. Technol. (ICCSNT), Oct. 2017, pp. 511-515.
[5] W. Zeng and M. Y. Chow, "Optimal tradeoff between performance and security in networked control systems based on coevolutionary algorithms," IEEE Trans. Ind. Electron., vol. 59, no. 7, pp. 3016-3025, Dec. 2011.
[6] H. Zhang, Y. Shi, J. Wang, and H. Chen, "A new delay-compensation scheme for networked control systems in controller area networks," IEEE Trans. Ind. Electron., vol. 65, no. 9, pp. 7239-7247, Jan. 2018.
[7] Y. Yuan, H. Yuan, Z. Wang, L. Guo, and H. Yang, "Optimal control for networked control systems with disturbances: A delta operator approach," IET Control Theory Appl., vol. 11, no. 9, pp. 1325-1332, 2017.
[8] A. A. Yaseen and M. Bayart, "A model-free approach to networked control system with time-varying communication delay," IFAC-Papers Line, vol. 51, no. 24, pp. 558-563, 2018.
[9] R. Lu, Y. Xu, and R. Zhang, "A new design of model predictive tracking control for networked control system under random packet loss and uncertainties," IEEE Trans. Ind. Electron., vol. 63, no. 11, pp. 6999-7007, Nov. 2016.
[10] Z. Wang, J. Sun, and Y. Bai, "Stability analysis of event-triggered networked control systems with time-varying delay and packet loss," J. Syst. Sci. Complex., pp. 1-16, Nov. 2020.
[11] B. P. Padhy, "Adaptive latency compensator considering packet drop and packet disorder for wide area damping control design," Int. J. Electr. Power Energy Syst., vol. 106, pp. 477-487, Mar. 2019.
[12] P. Martí, J. Yépez, M. Velasco, R. Villa, and J. M. Fuertes, "Managing quality-of-control in network-based control systems by controller and message scheduling co-design," IEEE Trans. Ind. Electron., vol. 51, no. 6, pp. 1159-1167, Nov. 2004.
[13] F. Xia, S. Li, and Y. Sun, "Neural network based feedback scheduler for networked control system with flexible workload," in Proc. Int. Conf. Natural Comput., 2005, pp. 242-251.
[14] Z. N. Gao and W. H. Fan, "Hierarchic scheduling policy based on fuzzy feedback in networked control systems," J. Nanjing Univ. Sci. Technol., Nature Sci., vol. 34, no. 4, pp. 496-502, 2010.
[15] P. G. Otanez, J. R. Moyne, and D. M. Tilbury, "Using deadbands to reduce communication in networked control systems," in Proc. Amer. Control Conf., vol. 4, May 2002, pp. 3015-3020.
[16] W. Zhang, M. S. Branicky, and S. M. Phillips, "Stability of networked control systems," IEEE Control Syst. Mag., vol. 21, no. 1, pp. 84-99, Feb. 2001.
[17] D. S. Kim, Y. S. Lee, W. H. Kwon, and H. S. Park, "Maximum allowable delay bounds of networked control systems," Control Eng. Pract., vol. 11, no. 11, pp. 1301-1313, 2003.
[18] T. Bai, Y. S. Lee, W. H. Kwon, and H. S. Park, "Optimal bandwidth scheduling of networked control systems (NCSs) in accordance with jitter," J. Zhejiang Univ. Sci. A, vol. 6, 6, pp. 535-542, Nov. 2005.
[19] S. H. Hong, "Scheduling algorithm of data sampling times in the integrated communication and control systems," IEEE Trans. Control Syst. Technol., vol. 3, no. 2, pp. 225-230, Sep. 1995.
[20] S. Ho Hong, "Bandwidth allocation scheme for cyclic-service fieldbus networks," IEEE/ASME Trans. Mechatronics, vol. 6, no. 2, pp. 197-204, Jun. 2001.
[21] K. Ramakrishnan and G. Ray, "Robust stability criteria for a class of uncertain discrete-time systems with time-varying delay," Appl. Math. Model., vol. 37, no. 3, pp. 1468-1479, 2013.
[22] H. Li, Z. Sun, and M. Y. Chow, "State feedback controller design of networked control systems with time delay and packet dropout," IFAC Proc., vol. 41, no. 2, pp. 6626-6631, 2008.
[23] Y. Halevi and A. Ray, "Integrated communication and control systems: Part I—Analysis," J. Dyn. Syst., Meas., Control, vol. 110, pp. 367-373, 1988.
[24] F. Coutinho, J. Fonseca, J. Barreiros, and E. Costa, "Using genetic algorithms to reduce jitter in control variables transmitted over CAN," in Proc. ICC, Amsterdam, The Netherlands, 2000. [Online]. Available: https://www.can-cia.de/fileadmin/resources/documents/proceedings/ 2000_coutin.pdf
[25] Y. Z. Wang, L. Wang, X. Yan, and P. Shen, "Fuzzy immune particle swarm optimization algorithm and its application in scheduling of MVB periodic information," J. Intell. Fuzzy Syst., vol. 32, no. 6, pp. 3797-3807, 2017.
[26] Y. Chen, X. Sun, D. Gong, Y. Zhang, J. Choi, and S. Klasky, "Personalized search inspired fast interactive estimation of distribution algorithm and its application," IEEE Trans. Evol. Comput., vol. 21, no. 4, pp. 588-600, Aug. 2017.
![img-7.jpeg](img-7.jpeg)

XIANG YAN (Member, IEEE) received the B.S. degree in electrical information engineering and the Ph.D. degree in electrical engineering from Beijing Jiaotong University, Beijing, China, in 2009 and 2015, respectively.

From 2015 to 2019, he was an Electrical Engineer with the China Academy of Railway Sciences. He is currently a Lecturer with Zhejiang Wanli University. His current research interests include intelligent optimization, future networks, and the Internet of Things. He is a member of Chinese Association for Artificial Intelligence.
![img-8.jpeg](img-8.jpeg)

JUN LI received bachelor's (Hons.) and master's degrees from Zhejiang University, in 1993 and 2001, respectively, and the Ph.D. degree in computer networks from the Nanjing University of Posts and Telecommunications, in 2010.

She is currently a Professor with the School of Information and Intelligence Engineering, Zhejiang Wanli University. Her current research interests include future networks, content centric networks, the Industrial Internet of Things, network traffic classification, and network management.
![img-9.jpeg](img-9.jpeg)

BIZHOU MEI received the B.S. degree in mechanical design and manufacturing from Jiangsu Ocean University, Jiangsu, China, in 1991, and the M.S. degree in industrial engineering from the China University of Mining and Technology, Jiangsu, China, in 2005.

He is currently a Chief Technology Officer of Zhejiang Yi Duan Machinery Company. His research interests include intelligent CNC metal forming machine, metal forming, and wheel equipment.