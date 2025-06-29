# Dynamic Bandwidth Scheduling of Software Defined Networked Collaborative Control System 

XIANG YAN ${ }^{(1)}$, (Member, IEEE), YANFEI SUN ${ }^{(2)}$, AND BIZHOU MEI ${ }^{3}$<br>${ }^{1}$ School of Information and Intelligence Engineering, Zhejiang Wanli University, Ningbo 315000, China<br>${ }^{2}$ School of Internet of Things, Nanjing University of Posts and Telecommunications, Nanjing 210003, China<br>${ }^{3}$ Zhejiang Yi Duan Machinery Company, Ningbo 315000, China<br>Corresponding author: Xiang Yan (yanxiang@zwu.edu.cn)

This work was supported in part by the Natural Science Foundation of Ningbo City of China under Grant 2019A610121, and in part by the Talent Project of Zhejiang Wanli University under Grant SZ1540509806.


#### Abstract

From the perspective of collaborative design of control and scheduling, a software-defined networked collaborative control system (SD-NCCS) is established. On this basis, the system performance of SD-NCCS is analyzed and the average sensitivities of reference are used in utility function to evaluate the effects of network-induced delays. Moreover, the network pricing mechanism and game theory are introduced and a dynamic bandwidth resource allocation model of the overall control system for optimal performance is obtained. Thus, the problem of the network resource allocation of the SD-NCCS has been converted to be the problem of solving the Nash equilibrium point under the non-cooperative game model. Furthermore, the Nash equilibrium solution under this frame is obtained using the estimation distributed algorithm (EDA). Finally, a simple example is included to illustrate the performance of our scheme.


#### Abstract

INDEX TERMS Estimation of distribution algorithm, game theory, network pricing, software-defined network.


## I. INTRODUCTION

The networked control system (NCS) is a distributed control system where the control loops are closed via a communication network. Compared with the traditional point-topoint control system, the most significant feature of NCS is that the sensors, controllers, and actuators within are interconnected through some communication network instead of direct point-to-point connections [1]. As a result, using NCS may increase system flexibility, reduce system wiring, break the space limitation, which can realize remote monitoring and control in complex environments. Software-Defined Network (SDN) is recognized as the next-generation network paradigm [2], which decouples the network control plane from the data forwarding plane to a logically centralized controller, enabling rapid network technology innovation for multiple users. Under the SDN architecture, it is feasible to provide flexible and efficient service slicing solutions for different QoS requirements of nodes at the application layer by utilizing the characteristics of OpenFlow (OF) switches and Network Virtualization (NV).

[^0]Due to the limited communication bandwidth of the network itself, many problems such as delay, packet loss and jitter of data transmission in the control system will affect the control performance of NCS [3]-[5]. Without additional network resources, how to allocate and utilize bandwidth reasonably in limited network resources, so that the entire control system has an optimal control performance is a problem worth studying.

Notably, most of the aforementioned research is focused on the control strategy to reduce the impact of delay, packet loss, and packet error on control performance. However, studying NCS from the perspective of the quality of control (QoC) ignores the complex dynamic behavior of the network and is difficult to apply to complex real systems. The integrated design strategy of both the QoC and the quality of service (QoS) has attracted a growing number of researchers' attention. The collaborative design of control and scheduling can be divided into two categories. One is a real-time calculation method using real-time feedback theory, see [6]-[7]. In [8] a collaborative design method combining adaptive controller and feedback scheduling strategy is proposed, which overcomes some limitations of application and execution platform. The other is to maximize the performance of the control system in collaborative design and see [9]-[11]


[^0]:    The associate editor coordinating the review of this manuscript and approving it for publication was Qiong Wu.

for a partial list of references. For example, in [12] joint optimization of information transmission and state estimation developed to reduce the influence of network inducing factors on the convergence and accuracy of estimation. However, a key research issue in the NCS over SDN is the lack of dynamic scheduling mechanisms for network resources [13].

Motivated by the above analyses and under the SDN framework, from the perspective of collaborative design of control and scheduling, a software-defined networked collaborative control system is proposed. Furthermore, under the framework of SD-NCCS, the non-cooperative game model and network pricing mechanism are introduced, and a dynamic bandwidth scheduling strategy suitable for SD-NCCS is proposed. The goal is to find a flexible bandwidth allocation strategy based on Nash equilibrium and network pricing. Thus, the dynamic performance requirements of individuals and the whole are simultaneously satisfied. The network pricing mechanism is implemented in a centralized control mode in the network controller, and the overall performance of the control system is evaluated by the cumulative amount of the output error of each control loop. Also, considering the complexity of the calculation of the exact solution of the network bandwidth scheduling problem in practical operation, this paper gives an EDA-based Nash equilibrium point solution method.

## II. PROBLEM FORMULATION

## A. SYSTEM STRUCTURE

Envisioning the advantages of a software-defined network, a general architecture of SD-NCCS is proposed as shown in Figure 1. First, the data plane and the control plane are decoupled. The data plane is mainly composed of a set of switches that support the OpenFlow protocol (referred to as the OF Switch). In addition to the packet matching and forwarding tasks according to the flow table, the OF switch provides a secure interface to the control plane according to the OpenFlow protocol for convenient control. The control plane queries and manages the flow table in the switch. Second, the control plane consists of a controller that supporting the OpenFlow protocol (referred to as the OF Controller) or a network operating system and a set of applications on top of it. Through the OpenFlow channel, the control plane can acquire the state of the data plane and program the data plane, and thereby achieving optimal management of network resources from a global perspective. The part responsible for bandwidth scheduling and allocation above the OF Controller in the control plane is called the policy center (one kind of control APPs with a bandwidth allocation algorithm). Also, the network control subsystem is no longer a closed-loop control of the straight-through structure, but an open-loop control using a hierarchical structure. Each control loop issues a control command by the main controller, and the execution agent receives the command and controls the output.

It is assumed that the SD-NCSS has M hierarchical network control loop subsystems, and each control loop subsystem includes a main controller and an execution agent. The
![img-0.jpeg](img-0.jpeg)

FIGURE 1. The general structure of SD-NCCS.
execution agent includes a local controller, a sensor, and an actuator. The main controller sends a control command to the execution agent through the network, and the local controller in the execution agent converts the control device into a control signal according to the received command, and the sensor feeds the output action state information to the local controller. Both the main controller and the execution agent are time-driven and have the same sampling period $h$. The main controller sends bandwidth requirements to the policy center through the OF switch and the OF controller according to the task information, and the policy center integrates the bandwidth requirements of each subsystem to perform bandwidth allocation. A complete bandwidth scheduling operation cycle is called $T_{\mathrm{O}}$, as shown in Figure 2. First, during the bandwidth polling period $T_{\mathrm{F}}$, each control loop controller submits a bandwidth requirement to the center. Then, in the allocation period $T_{\mathrm{A}}$, the center calculates and allocates the bandwidth according to the collected information, that is, updates the Flow Table in the corresponding OF Switch. Finally, in the remaining data transmission period $T_{\mathrm{T}}$, each control loop alternately transmits data according to the allocated time slice until the beginning of a new cycle. Through the state information feedback and bandwidth resource reallocation of each new cycle, it can adapt to the changes in data service requirements of each control ring. Therefore, in this layered software-defined network collaborative control system, flexible scheduling strategies can be conveniently implemented.

## B. PERFORMANCE ANALYSIS

Under the premise of ensuring the stability of each control loop, finding an optimal bandwidth allocation scheme is the problem to be solved in this paper. Therefore, it is necessary to further analyze the impact of time delays on control performance under the assumption that there is no packet loss and disorder.

First, assume that during a data transmission period $T_{\mathrm{T}}$, the main controller of the control loop $i$ will periodically send a reference control signal $r(t)$ to the corresponding execution

![img-2.jpeg](img-2.jpeg)

FIGURE 2. Timing diagram of bandwidth allocation.
![img-2.jpeg](img-2.jpeg)

FIGURE 3. Transmissions of the reference $r(t)$ during $T_{T}$.
agent with $h$ as the sampling period, as shown in Figure 3. The total number of reference transmissions during $T_{T}$ is $N=\left\lfloor T_{\mathrm{T}} / h\right\rfloor$. Next, define $t_{k}^{j}=k T_{\mathrm{T}}+j h, k=0,1,2, \ldots ; j=$ $0,1,2, \ldots, N$. At the time $t=t_{k}^{j}$, the control reference signal is being sent to the corresponding execution agent on the main controller side, and the latest reference control signal at this time is recorded as $r^{(n)}\left(t_{k}^{j}\right)$. However, at the same time, the reference control signal actually received by the actuator agent side is a previous reference control signal, denoted as $r^{(o)}\left(t_{k}^{j}\right)$, and $r^{(o)}\left(t_{k}^{j}\right) \in\left\{r\left(t_{k-p}^{j-q}\right)\right\}, p=0,1,2, \ldots ; q=$ $1,2, \ldots, N ; p \leq k, q \leq j . y^{(n)}\left(t_{k}^{j}\right)$ and $y^{(o)}\left(t_{k}^{j}\right)$ are defined as output values obtained according to the reference control signals $r^{(n)}\left(t_{k}^{j}\right)$ and $r^{(o)}\left(t_{k}^{j}\right)$, respectively. If the difference between $y^{(n)}\left(t_{k}^{j}\right)$ and $y^{(o)}\left(t_{k}^{j}\right)$ is significant compared to the difference between $r^{(n)}\left(t_{k}^{j}\right)$ and $r^{(o)}\left(t_{k}^{j}\right)$, the time delay has a great influence on the control output of the control loop. Conversely, if the difference between $y^{(n)}\left(t_{k}^{j}\right)$ and $y^{(o)}\left(t_{k}^{j}\right)$ is insignificant compared to $r^{(n)}\left(t_{k}^{j}\right)$ and $r^{(o)}\left(t_{k}^{j}\right)$, the time delay has small effect on the control output.

Based on the above analysis, the average sensitivity of the control output to the reference control signal due to network delay is defined as follows [14]:

$$
\begin{aligned}
\bar{P}_{n, o}\left(t_{k}\right) & =\frac{\sum_{j=0}^{N-1} P_{n, o}\left(t_{k}^{j}\right)}{N} \\
P_{n, o}\left(t_{k}^{j}\right) & =\frac{\left(y^{(o)}\left(t_{k}^{j}\right)-y^{(n)}\left(t_{k}^{j}\right)\right) / y^{(n)}\left(t_{k}^{j}\right)}{\left(r^{(o)}\left(t_{k}^{j}\right)-r^{(n)}\left(t_{k}^{j}\right)\right) / r^{(n)}\left(t_{k}^{j}\right)}
\end{aligned}
$$

In practical engineering applications, the average sensitivity of the reference control signal can be calculated in advance or determined by simulation experiments according to the control requirements and then obtained by table lookup.

Finally, the designed utility function must be an increasing function of the bandwidth $x$, which is also affected by the average sensitivity of the reference control signal. In addition, to satisfy the existence of the Nash equilibrium, it must also be quasi-concave and continuously differentiable. Based on the above conditions, the utility function of the control loop $i$ designed in this paper during a data transmission period $t \in\left[t_{k}^{0}, t_{k+1}^{0}\right)$ is as follows:

$$
U_{i}\left(x_{i}\right)=\ln \left(1+\frac{\bar{P}_{n, o}^{i}\left(t_{k}\right) x_{i}}{\sum_{j \neq i}^{M} \bar{P}_{n, o}^{i}\left(t_{k}\right) x_{j}}\right)
$$

where $\bar{P}_{n, o}^{i}\left(t_{k}\right)$ is the average sensitivity of the reference control signal change of the control loop $i$.

The optimization goal is to maximize the total utility of all control loops in the SD-NCCS as follows:

$$
\begin{aligned}
J= & \max \sum_{i=1}^{M} U_{i}\left(x_{i}\right) \\
& \text { s.t. } \sum_{i=1}^{M} x_{i} \leq 1-\omega g, \quad x_{i} \geq 0
\end{aligned}
$$

where $\omega_{R} \in(0,1)$ is a retention scale factor, which was introduced to retain part of the bandwidth for unexpected overload conditions. However, simply using $J$ as the optimization objective does not consider that each control loop should pay a corresponding price for bandwidth resources. Therefore, such bandwidth resource allocation without price mechanism constraints cannot prevent individual control loops from maximizing their private utility due to private interests. All bandwidth resources may be only assigned to one control loop and cause the overall system to crash.

## III. MAIN RESULT

## A. GAME MODELING BASED ON NETWORK PRICING

The game model based on network pricing mechanism is discussed in this section. Applying economic model and game theory to the field of computer networks becomes of high research. Utilizing a game-theoretical framework with the pricing mechanism is an effective way of resource allocation of arbitration. Especially in the field of wireless access networks. For example, in [15] a utility-based power control via convex pricing scheme is proposed to obtain an efficient power allocation in the uplink of CDMA wireless networks. In [16] a cooperative distributed interference pricing algorithm is proposed for power control in heterogeneous wireless networks. In [17] a Stackelberg game is formulated to study the price-based bandwidth allocation in multi-user Bluetooth low energy (BLE)-backscatter communication. In [18] a hierarchical auction-based mechanism is designed to reduce both global communication and unnecessary repeated computation in ad hoc networks. The pricing strategy mainly

includes two modes: Non-usage-Based Pricing (NBP) and Usage-Based Pricing (UBP) [19]. Although NBP is simple in pricing and convenient to operate, it cannot use price leverage to adjust user resource allocation, which affects resource utilization and easily leads to network congestion. However, the unit bandwidth price of UBP can be tracked and changed according to the consumption of network resources. This dynamic pricing mechanism aims at maximizing the overall satisfaction of users and can achieve high utilization and fairness of network resources.

Every control loop wants to maximize its final revenue under the framework of the SD-NCCS. In general, the revenue of a control loop depends on the pricing strategy of other control loops. Given the pricing strategy of other control loops, if no control loop has the motivation to choose other pricing strategies (the utility of this strategy is already the max ), then no control loop will break this equilibrium. This equilibrium is called the Nash equilibrium (NE) [20]. On the one hand, it needs to provide services for each control loop to improve its QoC. On the other hand, it needs to balance the bandwidth requirements of each control loop so that the QoC of each control loop can be guaranteed. Therefore, for the SD-NCCS with limited bandwidth resources, the optimal resource scheduling strategy that takes into account the best performance of individuals and the whole is to allocate bandwidth at the NE.

The OF controller plays the role of price maker and each control loop mentioned above is referred to as a user. Each user does not know the existence of other users and their current status. Each one submits its bidding strategy according to its QoC need, and then pays the corresponding amount for the actual bandwidth allocated. The entire bidding process is as follows:

Step 1: Each user has the same amount of funds g in the initial state of each round of bidding.
Step 2: Each user submits a bidding $y_{i}\left(y_{i} \in[0, \mathrm{~g}]\right)$.
Step 3: The price maker will develop a bandwidth allocation scheme based on the bidding and allocates bandwidth resources to each user.

Step 4: Each user pays the amount of bandwidth allocated.
The amount $y_{i}$ that user $i$ needs to pay can be calculated by the following formula.

$$
y_{i}=\lambda x_{i}
$$

where $\lambda$ is the unit bandwidth price, and the utility function of each user is as follows:

$$
S_{i}\left(x_{i}\right)= \begin{cases}U_{i}\left(x_{i}\right)-\lambda x_{i}, & \text { if } x_{i}>0 \\ U_{i}(0), & \text { if } x_{i}=0\end{cases}
$$

It can be seen that the benefit of a user is determined by the corresponding QoC obtained and the payment under the given QoS. Each user independently makes its bidding strategy based on its earnings. Each user will not offer the high price arbitrarily, because too much high bidding will only lower its final income. It should be noted that the amount, the user
ultimately pays is based on the bandwidth they have obtained, which may not match the initial offer.

The Nash equilibrium based on and non-cooperative game model can be described as follows:

A non-cooperative game model with $M$ users based on the network pricing can be described as $M G=$ $\left(\Gamma,\left\{x_{i}\right\},\left\{S_{i}(\cdot)\right\}\right), \Gamma=\{1,2, \ldots, M\}$ is the index set of users. If $x_{i}^{*}$ is the optimal strategy for user $i$ when other users choose $\boldsymbol{x}_{-i}^{*}=\left(x_{1}^{*}, \ldots, x_{i-1}^{*}, x_{i+1}^{*}, \ldots, x_{M}^{*}\right)$, that is:

$$
S_{i}\left(x_{i}^{*}, \boldsymbol{x}_{-i}^{*}\right) \geq S_{i}\left(x_{i}, \boldsymbol{x}_{-i}^{*}\right), \quad \forall x_{i} \in X_{i}, i \in \Gamma
$$

$X_{i}=\left[x_{i}^{\min }, x_{i}^{\max }\right],\left(x_{i}^{\min }>0\right)$, is the policy space of user $i$, and $S_{i}(\cdot)$ (shown in equation (6)) is the utility function set of the user $i$. Then, the bidding strategy $\boldsymbol{x}^{*}=$ $\left(x_{1}^{*}, \ldots, x_{i}^{*}, \ldots, x_{M}^{*}\right)$ is a Nash equilibrium based on the network pricing and non-cooperative game model.

However, each time a user submits status information, it is not practically a submission of a bidding, but the average sensitivity $\bar{P}_{n, o}^{i}\left(t_{k}\right)$ for a new task. The price maker runs the bandwidth allocation program according to the $\bar{P}_{n, o}^{i}\left(t_{k}\right)$ combined with the game model to calculate the Nash equilibrium point, and performs actual scheduling on each control loop.

The following theorem will be used to prove the existence and uniqueness of Nash equilibrium for $M G$.

Theorem 1: A Nash equilibrium exists in game $N G=$ $\left(\Psi,\left\{P_{j}\right\},\left\{u_{j}(\cdot)\right\}\right)$, if for all $j \in \Psi$ :
(1) The policy space $\left\{P_{j}\right\}$ is a non-empty compact convex subset of the Euclidean space $R^{n}$;
(2) Utility function $u_{j}(p)$ is continuous on $p$ and concave on $p_{j}$ :

Proof: Please refer to [21] for details of the certificate.
Theorem 2: A Nash equilibrium exists in SD-NCCS, $M G=\left(\Gamma,\left\{X_{i}\right\},\left\{S_{i}(\cdot)\right\}\right), i \in \Gamma$.

Proof: This theorem can be proved by verifying that $M G$ satisfies the two conditions of Theorem 1. Assuming that $x_{i}^{\min } \leq x_{i}^{\max }$ is always true, it is clear that the first condition is met. It remains to prove that the utility function $S_{i}(x)$ is quasi-concave on $x_{i}$ for all $i$.

The first-order differential of utility function $S_{i}(x)$ is:

$$
\frac{\partial S_{i}\left(x_{i}\right)}{\partial x_{i}}=\frac{\bar{P}_{n, o}^{i}\left(t_{k}\right)}{\sum_{j \neq i}^{M} \bar{P}_{n, o}^{j}\left(t_{k}\right) x_{j}+\bar{P}_{n, o}^{i}\left(t_{k}\right) x_{i}}-\lambda
$$

The second-order differential of utility function $S_{i}(x)$ is:

$$
\frac{\partial S_{i}^{2}\left(x_{i}\right)}{\partial x_{i}^{2}}=-\frac{\bar{P}_{n, o}^{i}\left(t_{k}\right)^{2}}{\left(\sum_{j \neq i}^{M} \bar{P}_{n, o}^{j}\left(t_{k}\right) x_{j}+\bar{P}_{n, o}^{i}\left(t_{k}\right) x_{i}\right)^{2}}<0
$$

Obviously, the utility function $S_{i}(x)$ is continuous and differentiable on $x$ and concave on $x_{i}$. A concave function $S_{i}(x)$ is also quasi concave, so the second condition is also satisfied, and the proof is completed.

Theorem 3: The SD-NCCS has a unique Nash equilibrium.
Proof: The proof of the uniqueness of Nash equilibrium is similar to Theorem 2. The specific proof process can be found in the reference [22]. To ensure the simplicity of the text, it will not be repeated here.

![img-3.jpeg](img-3.jpeg)

FIGURE 4. The SD-NCCS test platform.

So far, we have converted the SD-NCCS network bandwidth allocation problem into a Nash equilibrium calculation problem based on the network pricing non-cooperative game model.

## B. EDA ALGORITHM

Envisioning the Nash equilibrium point under the network pricing non-cooperative game model is a nonlinear optimization problem with multiple constraints. The traditional numerical calculation method is difficult to solve the Nash equilibrium, so this paper adopts the EDA-based optimization algorithm for calculation. Furthermore, the implementation steps are as follows [23]:

Step 1: Initialization: randomly generate a valid initial population $B_{0}$ meeting the bandwidth constraint.
Step 2: Select: select the first half of the best gain candidates from the parents.

Step 3: Update: reconstruct a probability model based on Gaussian distribution from the obtained dominant group.

Step 4: Sampling: a new generation of populations is sampled by a new probability model. Go to Step 2 until the termination criterion is met.

## IV. EXPERIMENT AND RESULT ANALYSIS

## A. SIMULATION SETUP

In this section, a simple example is given to illustrate the effectiveness of the proposed method. The topology of the SD-NCCS test platform is shown in Figure 4, including a controller as a policy center, a switch supporting the OpenFlow protocol, and three control loops. Each control loop consists of the main controller and a simulation execution agent. The simulation test platform includes three networked dc-motor subsystems with the same control parameters. The state-space description of the subsystem can be expressed by (10) [24], and the corresponding motor parameters are shown in Table 1.

$$
\left\{\begin{array}{l}
\dot{\boldsymbol{x}}(t)=\boldsymbol{A} \boldsymbol{x}(t)+\boldsymbol{B} u(t) \\
\boldsymbol{y}(t)=\boldsymbol{C} \boldsymbol{x}(t)
\end{array}\right.
$$

TABLE 1. The parameters of the dc-motor subsystem.

| Symbol | Description | Value |
| :--: | :--: | :--: |
| $R_{a}$ | Motor winding resistance | $4.961 \Omega$ |
| $L_{a}$ | Motor winding inductance | $3.14 \times 10^{-3} \mathrm{H}$ |
| $K_{b}$ | Back-EMF constant | $1.276 \times 10^{-2} \mathrm{Vs} / \mathrm{rad}$ |
| $K_{l}$ | Electric torque constant | $7.105 \times 10^{-2} \mathrm{~N} \cdot \mathrm{~m} / \mathrm{A}$ |
| $J$ | Motor moment of inertia | $1.6511 \times 10^{-4} \mathrm{~kg} \cdot \mathrm{~m}^{2}$ |
| $B$ | Damping coefficient | $\begin{gathered} 23.64 \times 10^{-6} \\ \mathrm{~N} \cdot \mathrm{~m} \cdot \mathrm{sec} / \mathrm{rad} \end{gathered}$ |

![img-4.jpeg](img-4.jpeg)

FIGURE 5. Reference signals input of three control loops.

TABLE 2. Average sensitivities of reference signals for three control loops.

|  | Average sensitivity |  |  |
| :-- | :-- | :-- | :-- |
|  | Period 1 | Period 2 | Period 3 |
| Loop 1 | 1.53 | 1.22 | 2.10 |
| Loop 2 | 1.22 | 1.00 | 1.22 |
| Loop 3 | 1.79 | 1.53 | 1.53 |

and
$\boldsymbol{A}=\left[\begin{array}{cc}-\frac{R_{a}}{L_{a}} & -\frac{K_{b}}{L_{b}} \\ \frac{K_{l}}{J} & -\frac{\boldsymbol{B}}{J}\end{array}\right], \quad \boldsymbol{B}=\left[\begin{array}{c}\frac{1}{L_{a}} \\ 0\end{array}\right], \boldsymbol{C}=\left[\begin{array}{lll}0 & 1\end{array}\right]$
The reference control signal inputs of the three control loops during three transmission periods are as shown in Figure 5, and the corresponding sensitivity of the control signals is as shown in Table 2. Substituting each group of data into equation (3) gives the utility function of the corresponding control loop at each stage. The remaining parameters are set as follows: $\omega_{R}=0.1, T_{\mathrm{O}}=0.5 \mathrm{~s}, T_{\mathrm{P}}=0.03 \mathrm{~s}$, and the remaining time is $T_{\mathrm{T}}$. Among them, the bandwidth allocation period $T_{\mathrm{A}}$ is very small relative to the polling period $T_{\mathrm{P}}$ and can be ignored.

![img-5.jpeg](img-5.jpeg)

FIGURE 6. A comparison of simulation results.

The evaluation of SD-NCCS system performance can be jointly described by all control loop subsystems. The performance of each control loop subsystem can be measured by the integrated absolute error (IAE) [25]. The IAE for the control loop $i$ can be expressed as

$$
\operatorname{IAE}_{i}=\sum_{k=0}^{\infty}|e(k)| h_{i}
$$

It can also be directly expressed by controlling the output instantaneous error, and (12) is corrected to:

$$
\operatorname{IAE}_{i}\left(t_{j}\right)=\frac{1}{D} \sum_{d=0}^{D-1}\left|y_{\text {nom }, j}\left(t_{d}\right)-y_{\text {act }, j}\left(t_{d}\right)\right|
$$

where $t_{d}=d \Delta t, t_{d} \in\left[t_{j}, t_{j+1}\right]$ is the sampling time of the output signal measurement, $d$ is the index of the sampling point, and $\Delta t$ is the sampling interval. $D$ represents the total number of sampling points and can be set to $D=100$. $y_{\text {nom }, j}\left(t_{d}\right)$ is the output of the control loop $i$ measured at $t_{d}$ without time delay. $y_{\text {act }, j}\left(t_{d}\right)$ is the output of the control loop $i$ measured at the $t_{d}$ after the scheduling policy is adopted in the case of time delay.

## B. RESULT ANALYSIS

The initial population of the Network Pricing-based Bandwidth Allocation (NPBA) method is 100. After 10 generations of evolution, the overall fitness is quickly converged and stabilized, and reaches the Nash equilibrium.

TABLE 3. Overall performance.

|  | Method | Bandwidth vector | IAE |
| :-- | :-- | :-- | :-- |
| Period 1 | NPBA | $[0.190 .280 .43]$ | 0.1021 |
|  | EBA | $[0.300 .300 .30$ | 0.1189 |
|  | NPBA | $[0.220 .390 .29]$ | 0.1148 |
|  | EBA | $[0.300 .300 .30]$ | 0.1280 |
|  | NPBA | $[0.040 .460 .40]$ | 0.0409 |
| Period 3 | EBA | $[0.300 .300 .30]$ | 0.0488 |

The equilibrium solutions of the three stages are $\mathbf{x}_{1}^{*}=$ $\left[\begin{array}{llll}0.19 & 0.28 & 0.43\end{array}\right]^{T}, \mathbf{x}_{2}^{*}=\left[\begin{array}{llll}0.22 & 0.39 & 0.29\end{array}\right]^{T}, \mathbf{x}_{3}^{*}=$ $\left[\begin{array}{llll}0.04 & 0.46 & 0.40\end{array}\right]^{T}$. Also, we use the Equal Bandwidth Allocation (EBA) method for comparative experiments. The given bandwidth of each subsystem can be quickly obtained by $x_{i}=(1-\omega_{\mathrm{R}}) / M$. The IAE results of two different strategies are shown in Figure 6. The detailed numerical results are shown in Table 3 and IV.

As shown in Figure 6, generally speaking for independent subsystems, the less bandwidth allocation, the worse the control performance will be. Since the EBA uses the average bandwidth method, each control loop maintains the same bandwidth allocation for different transmission periods, so there is a case of excess bandwidth in a certain period. Loop 2 during period 2 for example, the average sensitivity of the loop 2 is 1.00 , and only a small amount of bandwidth is required to maintain the stable output of this subsystem. However, the result of a large amount of bandwidth wasted

TABLE 4. Individual performance.

|  | Method | Period 1 | Period 2 | Period 3 |
| :-- | :-- | :-- | :-- | :-- |
| Loop 1 | NPBA | 0.0408 | 0.0217 | 0.0465 |
|  | EBA | 0.0385 | 0.0251 | 0.0684 |
| Loop 2 | NPBA | 0.0283 | 0.0009 | 0.0279 |
|  | EBA | 0.0241 | 0.0005 | 0.0246 |
| Loop 3 | NPBA | 0.0457 | 0.0183 | 0.0277 |
|  | EBA | 0.0654 | 0.0232 | 0.0259 |

by this control loop is the lack of bandwidth of other control loops, which ultimately leads to a decline in overall control performance. In contrast, although the individual subsystems using NPBA are inferior to the corresponding subsystems using EBA in a certain transmission period, such as the first transmission period, the IAE of the control loop 1 and 2 using NPBA are higher than EBA. However, the overall IAE of EBA is higher than that of NPBA, indicating that the SD-NCCS using the proposed strategy provides satisfactory performance.

## v. CONCLUSION

This paper presents a software-defined networked collaborative control system from the perspective of collaborative design of control and scheduling. Under the framework of the SD-NCCS, a dynamic bandwidth scheduling strategy based on the game theory and network pricing mechanism is proposed, which transforms the network resource allocation problem into the Nash equilibrium solving problem. The biggest difference from the existing research results is that the proposed method forces the control subsystems to work at the Nash equilibrium dynamically, and the overall performance of the SD-NCCS with limited resources is improved. The simulation results demonstrate the effectiveness and availability of the proposed method. In addition, as the control plane and data plane are separated in SD-NCCS, a centralized algorithm for reaching the NE can be handed over to the SD-NCCS controller, which can be realized by an application on it. Therefore, in terms of complexity, comparing to the decentralized methods aforementioned, it is simpler and more operational. As it comes to the cost, more spending may be saved supposedly. At last, further study and implementation of this research work in a realistic software-defined networking environment is practical importance and is part of our current and future work.

## REFERENCES

[1] C. Tan and H. Zhang, "Necessary and sufficient stabilizing conditions for networked control systems with simultaneous transmission delay and packet dropout," IEEE Trans. Autom. Control, vol. 62, no. 8, pp. 4011-4016, Aug. 2017.
[2] D. Kreutz, F. M. V. Ramos, P. Esteves Verissimo, C. Esteve Rothenberg, S. Azodolmolky, and S. Uhlig, "Software-defined networking: A comprehensive survey," Proc. IEEE, vol. 103, no. 1, pp. 14-76, Jan. 2015.
[3] Z. Wang, C. Hu, Y. Zhu, S. He, K. Yang, and M. Zhang, "Neural network learning adaptive robust control of an industrial linear motor-driven stage with disturbance rejection ability," IEEE Trans. Ind. Informat., vol. 13, no. 5, pp. 2172-2183, Oct. 2017.
[4] L. Zhang, H. Gao, and O. Kaynak, "Network-induced constraints in networked control Systems-A survey," IEEE Trans. Ind. Informat., vol. 9, no. 1, pp. 403-416, Feb. 2013.
[5] C. Yuan and F. Wu, "Delay scheduled impulsive control for networked control systems," IEEE Trans. Control Netw. Syst., vol. 4, no. 3, pp. 587-597, Sep. 2017.
[6] Y. Sadi and S. C. Ergen, "Joint optimization of wireless network energy consumption and control system performance in wireless networked control systems," IEEE Trans. Wireless Commun., vol. 16, no. 4, pp. 2235-2248, Apr. 2017.
[7] D. Simon, A. Seuret, and O. Sename, "On real-time feedback control systems: Requirements, achievements and perspectives," in Proc. 1st Int. Conf. Syst. Comput. Sci. (ICSCS), Lille, France, Aug. 2012, pp. 1-6.
[8] P. Marti, J. Yepez, M. Velasco, R. Villa, and J. M. Fuertes, "Managing Quality-of-Control in network-based control systems by controller and message scheduling co-design," IEEE Trans. Ind. Electron., vol. 51, no. 6, pp. 1159-1167, Dec. 2004.
[9] L. Huang, M. Chen, and Y. Liu, "Learning-aided stochastic network optimization with state prediction," IEEE/ACM Trans. Netw., vol. 26, no. 4, pp. 1810-1820, Aug. 2018.
[10] M. H. Mamduhi, M. Kneissl, and S. Hirche, "Decentralized eventtriggered medium access control for networked control systems," in Proc. IEEE 55th Conf. Decis. Control (CDC), Dec. 2016, pp. 513-519.
[11] S. C. Lokhande and H. Xu, "Optimal self-triggered control and network co-design for networked multi-agent system via adaptive dynamic programming," in Proc. IEEE Symp. Ser. Comput. Intell. (SSCI), Nov. 2017, pp. 1-8.
[12] L. Lyu, C. Chen, J. Yan, F. Lin, C. Hua, and X. Guan, "State estimation oriented wireless transmission for ubiquitous monitoring in industrial cyberphysical systems," IEEE Trans. Emerg. Topics Comput., vol. 7, no. 1, pp. 187-201, Jan. 2019.
[13] A. Lee, P. Wang, S.-C. Lin, I. F. Akyildiz, and M. Luo, "Dynamic bandwidth allocation in SDN based next generation virtual networks: A deterministic network calculus approach," in Proc. Conf. Res. Adapt. Convergent Syst. (RACS), 2018, pp. 80-87.
[14] Y. Tipsuwan, S. Kamonsantiroj, J. Srisabye, and P. Chongstitvattana, "An auction-based dynamic bandwidth allocation with sensitivity in a wireless networked control system," Comput. Ind. Eng., vol. 57, no. 1, pp. 114-124, Aug. 2009.
[15] E. E. Tsiropoulou, G. K. Katsinis, and S. Papavassiliou, "Utility-based power control via convex pricing for the uplink in CDMA wireless networks," in Proc. Eur. Wireless Conf. (EW), 2010, pp. 200-206.
[16] C. Chen, Pricing, Competition, and Resource Allocation in Heterogeneous Wireless Networks. Evanston, IL, USA: Northwestern Univ., 2016.
[17] D. Li and Y.-C. Liang, "Price-based bandwidth allocation for backscatter communication with bandwidth constraints," IEEE Trans. Wireless Commun., vol. 18, no. 11, pp. 5170-5180, Nov. 2019.
[18] L. Wang, M. Liu, and M. Q.-H. Meng, "A hierarchical auction-based mechanism for real-time resource allocation in cloud robotic systems," IEEE Trans. Cybern., vol. 47, no. 2, pp. 473-484, 2016.
[19] S. Stidham, "Pricing and congestion management in a network with heterogeneous users," IEEE Trans. Autom. Control, vol. 49, no. 6, pp. 976-981, Jun. 2004.
[20] RT. Maheswaran and T. Basar, "Equilibrium and negotiation in multiple resource auctions," in Proc. 42nd IEEE Int. Conf. Decision Control (CDC). Vol. 6, Dec. 2003, pp. 5939-5944.
[21] S.-P. Hsu, S.-L. Hsu, and A. S. Tsai, "A game-theoretic analysis of bandwidth allocation under a user-grouping constraint," J. Appl. Math., vol. 2013, pp. 1-9, Dec. 2013.
[22] C. U. Saraydar, N. B. Mandayam, and D. J. Goodman, "Efficient power control via pricing in wireless data networks," IEEE Trans. Commun., vol. 50, no. 2, pp. 291-303, 2002.
[23] H. Li, M.-Y. Chow, and Z. Sun, "EDA-based speed control of a networked DC motor system with time delays and packet losses," IEEE Trans. Ind. Electron., vol. 56, no. 5, pp. 1727-1735, May 2009.
[24] H. Li, F. Sun, Z. Sun, and J. Du, "Optimal state feedback integral control using network-based measurements," IEEE Trans. Instrum. Meas., vol. 61, no. 12, pp. 3127-3135, Dec. 2012.
[25] L. Xu and M. Fei, "A hybrid quantum clone evolutionary algorithm-based scheduling optimization in a networked learning control system," in Proc. Chin. Control Decis. Conf., Shanghai, China, May 2010, pp. 3632-3637.

![img-6.jpeg](img-6.jpeg)

XIANG YAN (Member, IEEE) received the B.S. degree in electrical information engineering and the Ph.D. degree in electrical engineering from Beijing Jiaotong University, Beijing, China, in 2009 and 2015, respectively.
From 2015 to 2019, he was an Electrical Engineer with the China Academy of Railway Sciences. He is currently a Lecturer with Zhejiang Wanli University. His current research interests include intelligent optimization, future networks, and the Internet of Things.
Dr. Yan is also a member of the Chinese Association for Artificial Intelligence.
![img-7.jpeg](img-7.jpeg)

YANFEI SUN received the Ph.D. degree in communication and information systems from the Nanjing University of Posts and Telecommunications, in 2006.
He is currently a Professor with the School of Internet of Things, Nanjing University of Posts and Telecommunications. He is also a Director of the Jiangsu Engineering Research Center of HPC and Intelligent Processing. His current research interests are mainly in the areas of future networks, industrial Internet, energy Internet, big data management and analysis, and intelligent optimization and control.
![img-8.jpeg](img-8.jpeg)

BIZHOU MEI received the B.S. degree in mechanical design and manufacturing from Jiangsu Ocean University, Jiangsu, China, in 1991, and the M.S. degree in industrial engineering from the China University of Mining and Technology, Jiangsu, in 2005.
He is currently a Chief Technology Officer with Zhejiang Yi Duan Machinery Company. His research interests include intelligent CNC metal forming machine, metal forming, and wheel equipment.