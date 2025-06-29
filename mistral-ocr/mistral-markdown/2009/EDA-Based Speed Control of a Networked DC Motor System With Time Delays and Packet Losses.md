# EDA-Based Speed Control of a Networked DC Motor System With Time Delays and Packet Losses 

Hongbo Li, Mo-Yuen Chow, Fellow, IEEE, and Zengqi Sun, Senior Member, IEEE


#### Abstract

This paper presents a new controller design method for networked dc motor system in the presence of time delays and packet losses. The sufficient condition under which the closed-loop system is asymptotically stable and the necessary condition under which the networked dc motor has zero steady-state tracking error are derived. Based on the obtained conditions, an output tracking controller design method is proposed, where the Estimation of Distribution Algorithm is used to optimize the control parameters to improve the system control performance. The proposed method can be easily applied to various applications, since it is simple and has no assumptions on time delay and packet loss models. Simulation and experimental results are given to demonstrate the effectiveness of the proposed approach.


Index Terms-Estimation of Distribution Algorithm (EDA), networked control systems (NCSs), packet loss, time delay.

## I. INTRODUCTION

THE control of dc motors has been an attractive subject of research during the past several decades since dc motors have been widely utilized in various fields. In traditional dc motor control, system components are located in the same place and connected by point-to-point wiring. However, in many practical systems, dc motor and controller are difficult to be located in the same place, and thus, signals are required to be transmitted from one place to another. To reduce the cost of installation and offer the ease of maintenance, communication networks are used to connect those system components, which gives rise to the so-called networked control systems (NCSs). Recently, NCSs have attracted much attention from research communities. Issues such as time delays [1]-[4], packet losses [8], scheduling [9], and security [10] have been investigated with results reported in the literature. In addition, due to their

Manuscript received June 10, 2008; revised January 5, 2009. First published February 6, 2009; current version published April 29, 2009. This work was supported in part by the National Science Foundation of China under Grants 60574035 and 60674053, in part by the National Key Project for Basic Research of China under Grant 2002cb312205, and in part by the U.S. National Science Foundation under Grant IIS-0426852.
H. Li is with the Electrical and Computer Engineering Department, North Carolina State University, Raleigh, NC 27606 USA, and also with the Department of Computer Science and Technology, State Key Laboratory of Intelligent Technology and Systems, Tsinghua University, Beijing 100084, China (e-mail: hli7@ncsu.edu; hb-li04@mails.tsinghua.edu.cn).
M.-Y. Chow is with the Electrical and Computer Engineering Department, North Carolina State University, Raleigh, NC 27606 USA (e-mail: chow@ncsu.edu).
Z. Sun is with the Department of Computer Science and Technology, State Key Laboratory of Intelligent Technology and Systems, Tsinghua University, Beijing 100084, China (e-mail: szq-dcs@mail.tsinghua.edu.cn).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TIE.2009.2013749
great advantages, NCSs have been finding applications in a broad range of areas such as dc motors [1]-[3], robots [4], vehicles [5], car suspension system [6], ball maglev system [7], rotary manipulator [17], and process control [18].

Time delay in NCSs is a major cause for system performance deterioration and potential system instability. In the literature, time delays have been modeled by using various formulations, such as constant delay, independently random delay [11], or random delay governed by a Markov chain. Another important issue in NCSs is the packet loss phenomenon. There are two typical approaches to describe packet losses in the literature. The first approach assumes that packet losses follow certain probability distributions such as Markov chain. The second one is the deterministic method, which specifies the packet losses in a time average sense or places bound on the number of consecutive packet losses. Note that the packets in NCSs usually suffer time delays and packet losses simultaneously during network transmissions. Therefore, the analysis and synthesis of NCSs with time delays and packet losses are a challenge but a practical problem. In the literature, some important methodologies, such as stochastic control [11], robust control [5], fuzzy control [4], predictive control [3], and memoryless state-feedback control (MSFC) [12]-[15], are proposed to compensate the time delays and/or packet losses. For more details on this topic, we refer the reader to [3]-[5], [11]-[15], and the references therein.

MSFC is a simple and effective control method. It has a simple structure and does not require controller memory to store past information. Therefore, the MSFC of NCSs with time delays and packet losses has received considerable attention in the past few years. Among the reported results in the literature, to mention a few, the stability issue is addressed in [12], the stabilization problem is investigated in [13] and [14], and the optimal stabilizing controller is designed in [15]. Note that the MSFC controllers in the aforementioned results are all regulators and none of them takes output tracking problem into account. However, it is well known that output tracking control has been widely used in various fields, and it has been well recognized that output tracking controller design is more general than regulator design, which motivates this paper.

In this paper, we address the optimal output tracking problem for a networked dc motor system with time delays and packet losses. The sufficient condition under which the closed-loop system is asymptotically stable and the necessary condition under which the networked dc motor has zero steady-state tracking error for a step reference speed are derived. An output tracking controller design method is proposed, where the Estimation of Distribution Algorithm (EDA) is used to optimize the

![img-0.jpeg](img-0.jpeg)

Fig. 1. Structure of networked dc motor system.
control parameters to improve the system control performance. Note that our previous works [15] and [16] have shown the advantages of using EDA to optimize the control parameter for networked system, and there are at least two significant improvements of this paper over our previous works [15] and [16]. The first is that the framework of this paper is more general. Reference [15] assumes that time delays are less than two sampling periods, and [16] allows the network from sensor to controller only. This paper eliminates those assumptions and constraints. The second is that this paper studies output tracking controller design while [15] and [16] address the regulator design only.

The remainder of this paper is organized as follows. The problem formulation is given in Section II. Some preliminary results for networked dc motor system are derived in Section III. The controller design problem is solved in Section IV. Numerical and experimental results are provided in Section V. Finally, we conclude this paper in Section VI.

## II. Problem Formulation

As shown in Fig. 1, the networked dc motor system considered in this paper can be grouped into the following four modules: 1) the dc motor and the sensor; 2) the communication network; 3) the networked controller; and 4) the actuator. Each module is described in the following sections.

## A. DC Motor and the Sensor

The electromechanical dynamics of the dc motor can be described as

$$
\begin{aligned}
\frac{d i_{a}}{d t} & =-\frac{R}{L} i_{a}-\frac{K_{b}}{L} \omega+\frac{1}{L} u \\
\frac{\omega}{d t} & =\frac{K}{J} i_{a}-\frac{B}{J} \omega
\end{aligned}
$$

where $i_{a}$ is the armature winding current, $\omega$ is the rotor angular speed, $R$ is the armature winding resistance, $L$ is the armature winding inductance, $K_{b}$ is the back electromotive force constant, $u$ is the armature winding input voltage, $K$ is the torque constant, $J$ is the system moment of inertia, and $B$ is the system damping coefficient.

By letting $\boldsymbol{x} \stackrel{\Delta}{=}\left[i_{a}, \omega\right]^{\mathrm{T}}$, the dc motor can be expressed as

$$
\left\{\begin{array}{l}
\dot{\boldsymbol{x}}(t)=\boldsymbol{A} \boldsymbol{x}(t)+\boldsymbol{B} \boldsymbol{u}(t) \\
\boldsymbol{y}(t)=\boldsymbol{C} \boldsymbol{x}(t)+\boldsymbol{D} \boldsymbol{u}(t)
\end{array}\right.
$$

with $\boldsymbol{y}(t)$ being the rotor angular speed and

$$
\begin{array}{ll}
\boldsymbol{A}=\left[\begin{array}{cc}
-\frac{B}{L} & -\frac{K_{b}}{L} \\
\frac{K}{J} & -\frac{B}{J}
\end{array}\right] & \boldsymbol{B}=\left[\begin{array}{l}
\frac{1}{L} \\
0
\end{array}\right] \\
\boldsymbol{C}=\left[\begin{array}{ll}
0 & 1
\end{array}\right] & \boldsymbol{D}=0
\end{array}
$$

When the sampling period is specified to $h$, the dc motor can be discretized as

$$
\left\{\begin{array}{l}
\boldsymbol{x}(k+1)=\boldsymbol{F} \boldsymbol{x}(k)+\boldsymbol{G} \boldsymbol{u}(k) \\
\boldsymbol{y}(k)=\boldsymbol{C} \boldsymbol{x}(k)+\boldsymbol{D} \boldsymbol{u}(k)
\end{array}\right.
$$

with

$$
\boldsymbol{F}=e^{\boldsymbol{A} h} \quad \boldsymbol{G}=\int_{0}^{h} e^{\boldsymbol{A} \tau} d \tau \boldsymbol{B}
$$

It is assumed that the full-state variables are available in the networked system. At each sampling period, the sampled dc motor state and its time stamp (i.e., the time the motor state is sampled) are encapsulated into a packet and sent to the controller via the network.

## B. Data Network

In practice, the packets in NCSs usually suffer time delays and packet losses during network transmissions. As shown in Fig. 1, sensor-to-controller and controller-to-actuator delays are denoted by $\tau_{\mathrm{sc}}$ and $\tau_{\mathrm{ca}}$, respectively, and two switches $S_{1}$ and $S_{2}$ are used to model the packet losses in the backward and forward networks. When $S_{1}$ is open, the sensor packet is lost during network transmission from the sensor to the controller, whereas when $S_{1}$ is closed, the packet is successfully transmitted to the controller with a sensor-to-controller delay $\tau_{\mathrm{sc}}$. Similar arrangements are made for the forward network.

## C. Networked Controller

The networked controller takes the following form:

$$
\boldsymbol{u}=\boldsymbol{K} x+\boldsymbol{N} r
$$

where $\boldsymbol{x}$ is the motor state in the arriving sensor packet, $\boldsymbol{r}$ is the reference input, and $\boldsymbol{K}$ and $\boldsymbol{N}$ are the control parameters to be designed. Networked controller (7) is event driven. Whenever there is a sensor packet arriving at controller, the controller starts calculating the control signal. Immediately after the calculation, the new control signal and the time stamp of the used motor state are encapsulated into a packet and sent to the actuator via the network. The time stamp in the control packet will ensure the actuator to select the appropriate control signal to control the dc motor.

## D. Actuator

The actuator is time driven. It is assumed that the actuator and the sensor have the same sampling period $h$ and they are synchronized. Note that the actuator and the sensor are at the same location, and therefore, the synchronization between

them can be easily achieved by hardware synchronization, for instance, using special wiring to distribute a global clock signal to the sensor and the actuator. The actuator has a buffer size of one, which means that the latest control packet is used to control the dc motor. When a control packet arrives at the actuator, it will be used to update the buffer if its time stamp is newer than that of the control signal in Buffer. Otherwise, it will be discarded. The actuator uses a zero-order hold ( ZOH ) circuit. At each sampling period, the ZOH circuit reads the control signal from buffer and uses it to control the dc motor.

The objective of this paper is to provide a synthesis method to design optimal stabilizing gain $\boldsymbol{K}$ and coefficient $\boldsymbol{N}$ for networked controller (7), such that the networked system is asymptotically stable, meets specified control performance, and tracks the reference speed without steady-state error.

## III. Preliminary Results

This section is devoted to present some preliminary results for the concerned networked system. Those preliminary results will play a significant role in the controller design stage.

## A. Sufficient Stability Condition

The sufficient condition under which the gain matrix $\boldsymbol{K}$ of networked controller (7) can guarantee the networked system to be asymptotically stable is presented in this section.

In the considered networked system, a sensor packet is called effective sensor packet for networked controller (7), if it is successfully transmitted from the sensor to the controller and to the actuator, and the corresponding control packet is used to control the dc motor. Let $S \triangleq\left\{i_{1}, i_{2}, \ldots\right\}$, which is a subsequence of $\{0,1,2, \ldots\}$, denote the sequence of time indexes of the effective sensor packets. Note that only effective sensor packets are used to control the dc motor, and therefore, the sensor packets between two effective sensor packets can all be considered as dropped packets.

Based on the aforementioned notations, the packet loss in the networked dc motor system can be defined as

$$
\left\{\eta\left(i_{m}\right) \triangleq i_{m+1}-i_{m}, \quad i_{m} \in S\right\}
$$

which means that, from $i_{m}$ to $i_{m+1}$, the number of dropped packets is $\eta\left(i_{m}\right)-1$. Without loss of generality, we assume that the maximum number of consecutive packet losses is $\boldsymbol{N}_{\text {drop }}$.

Let $\tau_{i_{m}} \triangleq \tau_{\mathrm{sc}, i_{m}}+\tau_{\mathrm{ca}, i_{m}}$ express the round-trip time (RTT) delay encountered by the $m$ th effective sensor packet. A nature assumption on RTT delay $\tau_{i_{m}}$ can be made that $\tau_{i_{m}} \leq \tau_{\max }$, where $\tau_{\max }$ denotes the upper bound of $\tau_{i_{m}}$.

Let $N_{\text {delay }} \triangleq\left\lceil\tau_{\max } / h\right\rceil$, where $\lceil\cdot\rceil$ is the ceiling operator, which returns the smallest integer that is greater than or equal to a specified number. Introduce the augmented state $\boldsymbol{z}\left(i_{m}\right)=$ $\left[\begin{array}{llll}x_{i_{m}}^{\mathrm{T}} & \boldsymbol{x}_{i_{m-1}}^{\mathrm{T}} & \cdots & \boldsymbol{x}_{i_{m-n_{\text {delay }}}}^{\mathrm{T}}\end{array}\right]^{\mathrm{T}}$ into the aforementioned networked dc motor system; the closed-loop system can be described by the following discrete-time switched model:

$$
\boldsymbol{z}\left(i_{m+1}\right)=\boldsymbol{M}_{\left\lceil\tau_{i_{m}} / h\right\rceil} \boldsymbol{z}\left(i_{m}\right)
$$

where $\left\lceil\tau_{i_{m}} / h\right\rceil$ is a piecewise constant function called a switch signal, which takes values in a finite set $\mathbb{S} \triangleq\left\{0,1, \ldots, N_{\text {delay }}\right\}$. For $i \in \mathbb{S}, \boldsymbol{M}_{i}$ takes the following form:

$$
\boldsymbol{M}_{i}=\left[\begin{array}{cccc}
\boldsymbol{F}^{\eta\left(i_{m}\right)}+\Pi_{1}^{i} & \Pi_{2}^{i} & \cdots & \Pi_{\boldsymbol{N}_{\text {delay }}^{i}} \\
I & 0 & \cdots & 0 \\
0 & I & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & I
\end{array}\right]
$$

where

$$
\begin{aligned}
& \Pi_{1}^{i}=\sum_{r=0}^{\eta\left(i_{m}\right)-i} \mathbf{F}^{r} \mathbf{G} \boldsymbol{K} \\
& \Pi_{j}^{i}=\sum_{r=0}^{\nu_{r}^{i}} \mathbf{F}^{\eta\left(i_{m}\right)-i+r+1} \boldsymbol{G} \boldsymbol{K}(j \in[2, \ldots, i+1]) \\
& \Pi_{j}^{i}=0, \quad j \in\left[i+2, \ldots, N_{\text {delay }}+1\right]
\end{aligned}
$$

For more details of the modeling process and the used notations, please refer to our previous work [14]. Reference [14] has also shown that networked dc motor system (9) in the presence of time delays and packet losses is asymptotically stable, if, for $i, j \in \mathbb{S}$, there exist positive definite matrices $\boldsymbol{P}_{i}$ and $\boldsymbol{P}_{j}$ satisfying

$$
\boldsymbol{M}_{i}^{\mathrm{T}} \boldsymbol{P}_{j} \boldsymbol{M}_{i}-\boldsymbol{P}_{i}<0
$$

where $\boldsymbol{M}_{i}$ is of form (10) with a given gain matrix $\boldsymbol{K}$.
Noted that, in the considered networked system, there is no assumption on the time delay or packet loss model (i.e., the time delay can be constant, independently random, or random governed by a Markov chain, and the packet losses can be independently random or random governed by a Markov chain). Therefore, the NCS model (9), the stability condition (12), and the methods proposed in the following sections are quite general and can be applied to various applications.

## B. Necessary Condition for Zero Steady-State Tracking Error

The necessary condition under which the networked dc motor has zero steady-state tracking error for a step reference speed is presented in this section.

The basic idea of addressing the concerned problem is to compute the steady-state values of the motor state and the control input (denoted as $\boldsymbol{x}_{\mathrm{ss}}$ and $\boldsymbol{u}_{\mathrm{ss}}$ ) that result in zero steady-state tracking error, and then, let them take these values. Following this idea, we consider the networked controller

$$
\boldsymbol{u}=\boldsymbol{u}_{\mathrm{ss}}-\boldsymbol{K}\left(\boldsymbol{x}-\boldsymbol{x}_{\mathrm{ss}}\right)
$$

The rest of the problem is to determine the values of $\boldsymbol{x}_{\mathrm{ss}}$ and $\boldsymbol{u}_{\mathrm{ss}}$ such that the networked system has no steady-state error for any step reference input $\boldsymbol{r}$. To address this problem,

let $\boldsymbol{x}_{\mathrm{ss}}=\boldsymbol{N}_{x} \boldsymbol{r}$ and $\boldsymbol{u}_{\mathrm{ss}}=\boldsymbol{N}_{u} \boldsymbol{r}$. With those substitutions, (13) is equivalent to

$$
\boldsymbol{u}=-\boldsymbol{K} \boldsymbol{x}+\left(\boldsymbol{N}_{\mathrm{u}}+\boldsymbol{K} \boldsymbol{N}_{x}\right) \boldsymbol{r}
$$

When the networked system is at steady state, the dynamics of the dc motor (3) can be rewritten as

$$
\begin{aligned}
0 & =\boldsymbol{A} \boldsymbol{x}_{\mathrm{ss}}+\boldsymbol{B} \boldsymbol{u}_{\mathrm{ss}} \\
\boldsymbol{y}_{\mathrm{ss}} & =\boldsymbol{C} \boldsymbol{x}_{\mathrm{ss}}+\boldsymbol{D} \boldsymbol{u}_{\mathrm{ss}}
\end{aligned}
$$

where $\boldsymbol{y}_{\mathrm{ss}}$ is the steady-state output of the dc motor.
Letting $\boldsymbol{y}_{\mathrm{ss}}=\boldsymbol{r}$ and substituting $\boldsymbol{x}_{\mathrm{ss}}=\boldsymbol{N}_{x} \boldsymbol{r}$ and $\boldsymbol{u}_{\mathrm{ss}}=$ $\boldsymbol{N}_{u} \boldsymbol{r}$ into (15) lead to

$$
\left[\begin{array}{ll}
\boldsymbol{A} & \boldsymbol{B} \\
\boldsymbol{C} & \boldsymbol{D}
\end{array}\right]\left[\begin{array}{l}
\boldsymbol{N}_{x} \\
\boldsymbol{N}_{u}
\end{array}\right]=\left[\begin{array}{l}
0 \\
1
\end{array}\right]
$$

By solving (16), $\boldsymbol{N}_{x}$ and $\boldsymbol{N}_{u}$ can be easily obtained as

$$
\left[\begin{array}{l}
\boldsymbol{N}_{x} \\
\boldsymbol{N}_{u}
\end{array}\right]=\left[\begin{array}{ll}
\boldsymbol{A} & \boldsymbol{B} \\
\boldsymbol{C} & \boldsymbol{D}
\end{array}\right]^{-1}\left[\begin{array}{l}
0 \\
1
\end{array}\right]
$$

Apparently, if $\boldsymbol{N}_{x}$ and $\boldsymbol{N}_{u}$ in (14) take the values obtained from (17), the networked system will have zero steady-state tracking error for any step reference speed. By noting the difference between (7) and (14), we obtain

$$
\boldsymbol{N}=\boldsymbol{N}_{u}+\boldsymbol{K} \boldsymbol{N}_{x}
$$

Therefore, the necessary condition under which the networked dc motor has zero steady-state tracking error for any step reference speed is that the gain matrix $\boldsymbol{K}$ and the coefficient $\boldsymbol{N}$ satisfy (18).

## IV. Controller Design

This section is devoted to design the optimal stabilizing gain $\boldsymbol{K}$ and the coefficient $\boldsymbol{N}$ for networked controller (7). We will transform the controller design problem into an optimization problem and then solve the optimization problem.

Optimization Variables: In networked controller (7), the gain matrix $\boldsymbol{K}$ and the coefficient $\boldsymbol{N}$ are two parameters to be designed. Note that the coefficient $\boldsymbol{N}$ can be determined according to (18), which is a function of $\boldsymbol{K}$. Therefore, the optimization variables in the optimization problem are in fact only the state-feedback gain matrix $\boldsymbol{K}$, which takes the following form:

$$
\boldsymbol{K}=\left[K_{1}, K_{2}\right]
$$

Cost Function: The percent overshoot and the settling time are used to evaluate the networked dc motor system performance. The corresponding cost function is defined as follows:

$$
\begin{aligned}
J & =\lambda_{1} J_{1}+\lambda_{2} J_{2} \\
J_{1} & = \begin{cases}0, & P . O . \leq P . O, n \\
\left(P . O .-P . O, n\right) / P . O, n, & P . O .>P . O, n\end{cases} \\
J_{2} & = \begin{cases}0, & S . T . \leq S . T, n \\
\left(S . T .-S . T, n\right) / S . T, n, & S . T .>S . T, n\end{cases}
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. Graphical representation of the regions used in this paper.
where $P . O$. is the percent overshoot, $P . O . n_{n}$ is the nominal percent overshoot, S.T. is the settling time, and S.T. ${ }_{n}$ is the nominal settling time. P.O. ${ }_{n}$, and S.T. ${ }_{n}$ are nominal performance measures that the system should achieve without network in the loop. If the NCS performance meets the nominal performance specifications, we have $J=0$ because $J_{i}=0$, where $i=1,2$. The cost $J_{1}$ penalizes high value of the percentage overshoot, and the cost $J_{2}$ penalizes long settling time. The problem dependent weights $\lambda_{1}$ and $\lambda_{2}$ are used to specify the relative significance of $J_{1}$ and $J_{2}$ on the overall system performance.

SRC: A vector set $\Psi \subset \mathbb{R}^{1 \times 2}$ is called the stable region (Fig. 2) of the networked dc motor system, if any $\boldsymbol{K} \in \Psi$ satisfies the stability conditions described in (12), i.e., $\Psi$ is composed of $\boldsymbol{K}$ that guarantees the networked system to be asymptotically stable. Obviously, the controller gains that can provide satisfactory control performance must be within the defined stable region, since satisfactory control performance not only requires a system to be asymptotically stable but also requires the system to meet given performance specifications. Therefore, it is sufficient to search the optimal controller gain within the stable region, which can effectively reduce the search space and guarantee the stability of NCSs during the optimization procedure. Based on this idea, stable region constraint (SRC) is introduced as follows:

$$
S R C: \boldsymbol{V} \in \Psi \quad \forall \boldsymbol{V}
$$

which means that the optimization variables are constrained to the stable region throughout the optimization procedure.

OTC: To enable the networked dc motor track a reference speed with zero steady-state error, output tracking constraint (OTC) is introduced as follows:

$$
O T C: \boldsymbol{N}=\boldsymbol{N}_{u}+\boldsymbol{K} N_{x}
$$

which means that the gain matrix $\boldsymbol{K}$ and the coefficient $\boldsymbol{N}$ satisfy (18) during the optimization procedure.

In summary, the optimization problem can be expressed as

$$
\begin{aligned}
& \text { OP : } \min \boldsymbol{J}(\mathrm{NCS}, \boldsymbol{K}) \\
& \text { s.t. SRC : } \boldsymbol{K} \in \Psi \quad \forall \boldsymbol{K} \\
& \text { OTC : } \boldsymbol{N}=\boldsymbol{N}_{u}+\boldsymbol{K} \boldsymbol{N}_{x} \text {. }
\end{aligned}
$$

Equation (23) asks for $\boldsymbol{K}$ that minimizes the value of the cost function. Obviously, SRC can guarantee the stability of the networked system during the optimization procedure. On the other hand, by minimizing the cost function, the system control performance is optimized. Therefore, solving the optimization

problem (23) offers a substantial advantage in that both stability and control performance can be guaranteed in the controller design stage.

For the optimization problem (23), heuristic search algorithms such as a genetic algorithm can be adopted to solve it. However, the behavior of these heuristic search algorithms depends on many parameters. For a researcher without associated experiences, the choice of suitable values for so many parameters is difficult. Unlike other evolutionary algorithms (EAs), EDA does not use crossover or mutation. Instead, EDA uses a probability distribution model derived from the promising solutions to generate new population. Thus, one of the most appealing advantages of EDA over classical EAs is the reduction in the number of parameters to be tuned by the user. Moreover, it is noted that the optimization problem (23) is subjected to SRC. Therefore, to accelerate the search speed, a generic characteristic expected for the heuristic search algorithm is that it can search the optimal solution within the defined stable region with high probability. As mentioned before, EDA adopts a probability distribution model derived from the promising solutions to generate new population, which enables EDA to possess the required characteristic. Motivated by the aforementioned analyses, we adopt EDA to solve the optimization problem (23) in this paper. The optimization variables in the search space are modeled as a multivariate normal distribution $p(\boldsymbol{K})=\prod_{i=1}^{g} p\left(K_{i}\right)$, which is a product of two independent univariate normal distributions $p\left(K_{i}\right)=\left(\mu_{i}, \sigma_{i}\right)$. The EDA-based MSFC (E_MSFC) algorithm proposed in this paper can be summarized as follows.

1) Initialization. Generate $n_{1}$ gain candidates $\boldsymbol{K}^{i}=$ $\left[K_{1}^{i}, K_{2}^{i}\right](i=1, \ldots, n_{1})$ meeting SRC in the initial search space randomly; for each $\boldsymbol{K}^{i}$, compute the corresponding coefficient $\boldsymbol{N}^{i}$ according to (18).
2) Selection. Compute the cost value $J^{i}$ for each pair $\left(\boldsymbol{K}^{i}, \boldsymbol{N}^{i}\right)$; select the best $n_{2}\left(n_{2}<n_{1}\right)$ gain candidates $\boldsymbol{K}^{i}$ from the parent generation according to the cost values $J^{i}$.
3) Updating. Update the probability distribution model $p(\boldsymbol{K})$ using the selected $n_{2}$ promising gain candidates.
4) Sampling. Select the best gain candidate in the current population as $\boldsymbol{K}^{1}=\left[K_{1}^{1}, K_{2}^{1}\right]$, generate $n_{1}-1$ gain candidates $\boldsymbol{K}^{i}=\left[K_{1}^{i}, K_{2}^{i}\right](i=2, \ldots, n_{1})$ meeting SRC based on the updated $p(\boldsymbol{K})$, and, for each $\boldsymbol{K}^{i}$, compute the corresponding coefficients $\boldsymbol{N}^{i}$ according to (18).
5) If the termination criterion is met, EXIT; otherwise, go back to step 2).

For more details on EDA, please refer to [19] and the references therein. Note that, although we do not know the exact stable region of an NCS, we can realize SRC based on the stability conditions described in (12). Taking step 1), for example, we can generate a gain candidate in the search space randomly and then check whether the gain candidate satisfies the stability conditions described in (12). If it does, the gain candidate will be selected as an individual of the population. Otherwise, we discard it and repeat the aforementioned steps until we obtain one satisfying the stability conditions described in (12). Similar arrangements are made for step 4).

TABLE I
PARAMETERS OF THE DC MOTOR

| $J$ | Inertia | $1.6511 \times 10^{-4} \mathrm{~kg} \bullet \mathrm{~m}^{g}$ |
| :-- | :-- | :-- |
| $L$ | Inductance | $3.14 \times 10^{-3} \mathrm{H}$ |
| $R$ | Resistance | $4.961 \Omega$ |
| $K$ | Torque Constant | $7.105 \times 10^{-2} \mathrm{~N} \bullet \mathrm{~m} / \mathrm{A}$ |
| $B$ | Damping coefficient | $23.64 \times \mathrm{e}^{-6} \mathrm{~N} \bullet \mathrm{~m} \bullet \mathrm{sec} / \mathrm{rad}$ |
| $K_{b}$ | Back-EMF Constant | $1.276 \times 10^{-3} \mathrm{Vs} / \mathrm{rad}$ |

![img-2.jpeg](img-2.jpeg)

Fig. 3. Typical evolution process of EDA in solving the optimization problem.

## V. ILLUSTRATIVE EXAMPLE

To show the effectiveness of $\mathrm{E}_{\mathrm{n}} \mathrm{MSFC}$ for networked dc motor speed control, it is applied to a networked dc motor system. A comparative study of E_MSFC with two existing approaches is constructed, where both numerical simulations and experimental verifications are provided.

The parameters of the dc motor used in this paper are listed in Table I. The sampling period of the networked system is specified to 0.1 s . To carry out the comparative study, it is assumed that $\tau_{i_{\mathrm{in}}} \in(0 \mathrm{~s}, 0.25 \mathrm{~s}]$ and $\boldsymbol{N}_{\mathrm{drop}}=4$, which means that up to four consecutive packets can be lost during network transmissions. The performance specifications for the networked dc motor system are developed as follows:

1) percent overshoot: P.O. $\leq 3 \%$
2) settling time: S.T. $\leq 2 \mathrm{~s}$.

## A. Networked Controller Design

First, let us consider the state-feedback controller (SFC) proposed by Yue et al. in [13]. By using [13, Th. 1] to the aforementioned networked system, we obtain an SFC $\boldsymbol{u}(t)=$ $10^{-4}[0.4043,-0.0417] \boldsymbol{x}\left(t-\tau_{k}\right)$.

Then, we apply the state-feedback stabilizing controller (SFSC) in our previous work [14] to the aforementioned networked system and obtain an SFSC $\boldsymbol{u}=[-0.0031,-0.0056] \boldsymbol{x}$.

Finally, let us consider the proposed E_MSFC method. This example uses $n_{1}=50$ and $n_{2}=20$ for the EDA algorithm, with $P . O_{\cdot n}, S . T_{\cdot n}, \lambda_{1}$, and $\lambda_{2}$, in the cost function (20) specified to $1 \%, 1 \mathrm{~s}, 1$, and 1 , respectively. Fig. 3 shows the typical evolution process of EDA in solving the optimization problem (23), which clearly shows that the system control performance is improved from generation to generation by

![img-3.jpeg](img-3.jpeg)

Fig. 4. Population distribution of EDA at the (a) first, (b) fifth, (c) tenth, and (d) fortieth generations.
using EDA. The population distribution of EDA at different generations is shown in Fig. 4, where the circles represent the individuals of population and the crosses represent the discarded gain candidates based on the SRC criteria. From Fig. 4(a), we can approximate the boundary of the stable region of the networked dc motor system. Fig. 4 also shows that EDA can generate a new population in the stable region for the next generation with high probability, and from generation to generation, the search space gets smaller and smaller, which can accelerate the search speed. That demonstrates the advantage of using EDA in solving the optimization problem (23). As shown in Fig. 3, the optimal cost of 0.31 has been achieved at the forty-second generation, where the designed controller is $\boldsymbol{u}=[-0.1588,-0.0190] \boldsymbol{x}+0.0311 \boldsymbol{r}$.

Note that the networked system is designed to drive the dc motor to a preset speed. However, the SFC and SFSC are regulators, and therefore, they cannot drive the dc motor to a nonzero speed. For comparison purposes, we modify the two comparative controllers by further introducing the reference
input. We use the same feedback gain matrices but further apply (17) and (18) to them. As a result, the two comparative controllers are modified as $\boldsymbol{u}(t)=10^{-4}[0.4043,-0.0417] \boldsymbol{x}(t-$ $\left.\tau_{k}\right)+0.0196 \boldsymbol{r} \quad$ and $\quad \boldsymbol{u}=[-0.0031,-0.0056] \boldsymbol{x}+0.0140 \boldsymbol{r}$, respectively.

It is worth noting that our previous works [15] and [16] cannot be applied to the aforementioned networked system since both-sides network is considered in the networked system and the RTT delays are larger than two sampling periods. Therefore, [15] and [16] are not considered in the comparative study. This remark also demonstrates the significant improvement of this paper over our previous works [15] and [16].

## B. Numerical Simulations

In the numerical simulation scenario, the networked dc motor system is simulated using MATLAB under fully controlled environments. With the initial state $\boldsymbol{x}_{0}=[0,0]^{\mathrm{T}}, 40$ paired simulation results are shown in Fig. 5, where Fig. 5(a) shows the

![img-4.jpeg](img-4.jpeg)

Fig. 5. Typical simulation results using different networked controllers.
TABLE II
Statistics of Networked DC Motor Performance

|  | SFC | SFSC | E_MSFC |
| :--: | :--: | :--: | :--: |
| Mean value | 2.7979 | 1.4437 | 0.3134 |
| Standard deviation | 0.0883 | 0.0809 | 0.1550 |

system cost values, Fig. 5(b) shows the system performances, and Fig. 5(c) shows the corresponding box-and-whisker diagram over the 40 runs. The statistics of the 40 simulation results are listed in Table II. By paired simulation results, we mean that the same network condition is used in the simulation of networked system using the SFC, the SFSC, and the E_MSFC controller. Note that the 40 paired runs used 40 different network conditions and they were generated randomly under the given network constraints $\tau_{t_{\mathrm{tn}}} \in(0 \mathrm{~s}, 0.25 \mathrm{~s}]$ and $N_{\text {drop }}=4$.

Two-sample tests of hypothesis are also performed on the aforementioned simulation results. First, we use the hypothesis test to determine whether the E_MSFC controller provides higher control performance statistically than the SFC does. For this purpose, the null hypothesis

$$
H_{0}^{1}: J_{\mathrm{E} \_ \mathrm{MSFC}} \geq J_{\mathrm{SFC}}
$$

is tested against the alternative hypothesis

$$
H_{a}^{1}: J_{\mathrm{E} \_ \mathrm{MSFC}}<J_{\mathrm{SFC}}
$$

The decision is made based on the $P$-values of the tests that show the probability of obtaining the existing experimental data given the null hypothesis; thus, a low $P$-value leads to the rejection of the null hypothesis. Let $J_{\mathrm{dif}} \triangleq J_{\mathrm{E} \_ \mathrm{MSFC}}-J_{\mathrm{SFC}}$, where $J_{\mathrm{E} \_ \mathrm{MSFC}}$ and $J_{\mathrm{SFC}}$ denote the system cost using the E_MSFC controller and the SFC, respectively. Corresponding to the 40 paired simulation results shown in Fig. 5(a), the mean and standard deviation of $J_{\mathrm{dif}}$ are given as follows:

$$
\bar{d}=-2.5500 \quad s_{d}=0.1397
$$

Substituting $\bar{d}$ and $s_{d}$ into the test statistic $t$, we have

$$
t=\frac{\bar{d}}{s_{d} / \sqrt{n}}=\frac{-2.55}{0.1397 / \sqrt{39}}=-113.9924
$$

Corresponding to $t=-113.9924$, the level of significance is $p$-value $<0.0001$. Thus, we reject the null hypothesis $H_{0}^{1}$ and conclude that there is significant evidence ( $p$-value $<$ 0.0001 ) that E_MSFC controller provides smaller cost value than SFC does. Moreover, based on the mean value of system cost using SFC and E_MSFC controller (denoted as $\bar{J}_{\mathrm{SFC}}$ and $\bar{J}_{E \_ \text { MSFC }}$, respectively), as listed in Table II, we can further conclude that, in comparison with SFSC on the average, E_MSFC controller reduces the system cost by $88.8 \%$ $\left[\left(\bar{J}_{\mathrm{SFC}}-\bar{J}_{E \_ \text { MSFC }}\right) 100 \% / \bar{J}_{\mathrm{SFC}}\right]$.

![img-5.jpeg](img-5.jpeg)

Fig. 6. (a) Block diagram of networked dc motor system. (b) Actual networked dc motor system setup.

For the two-sample tests of E_MSFC controller and SFSC, the null and alternative hypotheses are given by

$$
\begin{array}{ll}
H_{0}^{2}: & J_{E_{-} \text {MSFC }} \geq J_{\text {SFSC }} \\
H_{n}^{2}: & J_{E_{-} \text {MSFC }}<J_{\text {SFSC }}
\end{array}
$$

By following a similar procedure as described in the first hypothesis test, we obtain $t=-112.9102$ for this case. Corresponding to $t=-112.9102$, the level of significance is $p$ value $<0.0001$. Thus, we reject the null hypothesis $H_{0}^{2}$ and conclude that there is significant evidence ( $p$-value $<0.0001$ ) that E_MSFC controller provides smaller cost value than SFSC does. Moreover, based on the mean value of system cost using SFSC and E_MSFC controller (denoted as $\bar{J}_{\text {SFSC }}$ and $\bar{J}_{E_{-} \text {MSFC }}$, respectively), as listed in Table II, we can further conclude that, comparing with SFC on the average, E_MSFC controller reduces the system cost by $78.25 \%$ ( $\left(\bar{J}_{\text {SFSC }}-\right.$ $\left.\bar{J}_{E_{-} \text {MSFC }}\right) 100 \% / \bar{J}_{\text {SFSC }}$ ).
From the simulation results and aforementioned analysis, we can see that, comparing with SFC and SFSC, E_MSFC controller reduces the system cost by $88.8 \%$ and $78.25 \%$, respectively. The substantial performance improvement of E_MSFC controller comes as no surprise since the performance optimization is considered in the E_MSFC controller design.

## C. Experimental Verifications

To further illustrate the effectiveness and applicability of E_MSFC, a networked dc motor platform is constructed. The block diagram of networked dc motor system is shown Fig. 6(a), and the actual system setup is shown in Fig. 6(b).

As shown in Fig. 6, the experimental apparatus consists of a PC, a local board, and a dc motor with sensors. The networked controller was implemented in Labview 8.2 on a PC running Windows XP. The local board is on the dc motor side and is used for two functions. The first function is to convert the control signal read from the buffer into a pulsewidth-
![img-6.jpeg](img-6.jpeg)

Fig. 7. Typical experimental results using different networked controllers.
modulation (PWM) signal and then send the PWM signal to drive the dc motor. The second function is to encapsulate the motor state into a packet and send it to the PC controller via the network. The local board and the sensor are time driven, and they are synchronized by using the same clock signal. In the experimental verifications, the PC controller and the dc motor were linked by a simulated network. The simulated network creates time delays by delaying the packets transmitted between the PC controller and the dc motor and creates packet losses by discarding the transmitted packets. The reasons for using the simulated network rather than using the actual network are as follows. 1) The experimental results can be compared with the simulation results under the same network condition. 2) The experiment is ensured to be repeatable for various investigations.

With the same initial state and control parameters as used in numerical simulations (see Section V-B), four typical paired experimental results are shown in Fig. 7, where the system responses with SFC, SFSC, and E_MSFC controller are depicted by cross-solid, dashed, and solid lines, respectively. Apparently, the experimental results shown in Fig. 7 are consistent with the simulation results shown in Fig. 5(b), except that there are small steady-state errors in the experimental results. Note that the steady-state errors in the experimental results come as no surprise, since there is an inevitably modeling error, and most importantly, there are inevitably some nonlinearities such as dead zone and fabrication in the experimental apparatus.

From the simulation results shown in Fig. 5(b) and experimental results shown in Fig. 7, we can also see that the system control performance using E_MSFC controller meets the given performance specifications (i.e., P.O. $\leq 3 \%$, and S.T. $\leq$ 2 s) very well, which demonstrates that E_MSFC controller provides a satisfactory performance. However, as shown in Figs. 5(b) and 7, the S.T. of networked system using SFC and SFSC does not satisfy the given specification $S . T . \leq 2 \mathrm{~s}$. This phenomenon demonstrates the fact that a stabilizing controller can only guarantee the system to be asymptotically stable while the system control performance may be not satisfied. Note

that both system stability and control performance are taken into account in the design stage of E_MSFC. This substantial advantage enables E_MSFC to overcome the aforementioned shortcoming of stabilizing controller.

In summary, the aforementioned simulation and experimental results have demonstrated the effectiveness of the proposed E_MSFC method for real-world application. It has been shown that the E_MSFC method is more general than the ones in [13] and [14] at the application scope, since E_MSFC controller is an output tracking controller while the ones in [13] and [14] are regulators. Furthermore, the E_MSFC method can reduce the system cost, substantially comparing with the methods in [13] and [14], and in the examples used, the E_MSFC method reduces the system cost by more than $78.25 \%$.

## VI. CONCLUSION

This paper has presented an E_MSFC method for networked dc motor system with time delays and packet losses. The proposed E_MSFC controller is an output tracking controller, and therefore, it is more general than the regulator at the application scope. One advantage of E_MSFC method is that both system stability and control performance are considered during the controller design stage; another is that it can be easily implemented to various applications since it has simple structure and has no assumptions on time delay and packet loss models. Simulation and experimental results are given to demonstrate the effectiveness of the proposed approaches.

In future work, we will consider more performance requirements such as $\mathrm{H}_{\infty}$ specification during the controller design stage. Moreover, we will also extend the results to the case where full state measurement is not available.

## REFERENCES

[1] M.-Y. Chow and Y. Tipsuwan, "Gain adaptation of networked DC motor controllers based on QoS variations," IEEE Trans. Ind. Electron., vol. 50, no. 5, pp. 936-943, Oct. 2003.
[2] K. C. Lee, S. Lee, and M. H. Lee, "QoS-based remote control of networked control systems via Profibus token passing protocol," IEEE Trans. Ind. Informat., vol. 1, no. 3, pp. 183-191, Aug. 2005.
[3] G.-P. Liu, Y. Xia, J. Chen, D. Rees, and W. Wu, "Networked predictive control of systems with random network delays in both forward and feedback channels," IEEE Trans. Ind. Electron., vol. 54, no. 3, pp. 12821297, Jun. 2007.
[4] C.-L. Hwang, L.-J. Chang, and Y.-S. Yu, "Network-based fuzzy decentralized sliding-mode control for car-like mobile robots," IEEE Trans. Ind. Electron., vol. 54, no. 1, pp. 574-585, Feb. 2007.
[5] P. Seiler and R. Sengupta, "An $\mathrm{H}_{\infty}$ approach to networked control," IEEE Trans. Autom. Control, vol. 50, no. 3, pp. 356-364, Mar. 2005.
[6] M. Gaid, A. Cela, and Y. Hamam, "Optimal integrated control and scheduling of networked control systems with communication constraints: Application to a car suspension system," IEEE Trans. Control Syst. Technol., vol. 14, no. 4, pp. 776-787, Jul. 2006.
[7] W. J. Kim, K. Ji, and A. Srivastava, "Network-based control with realtime prediction of delayed/lost sensor data," IEEE Trans. Control Syst. Technol., vol. 14, no. 1, pp. 182-185, Jan. 2006.
[8] J. Xiong and J. Lama, "Stabilization of linear systems over networks with bounded packet loss," Automatica, vol. 43, no. 1, pp. 80-87, Jan. 2007.
[9] P. Martí, J. Yépez, M. Velasco, R. Villà, and J. M. Fuertes, "Managing quality-of-control in network-based control systems by controller and message scheduling co-design," IEEE Trans. Ind. Electron., vol. 5, no. 6, pp. 1159-1167, Dec. 2004.
[10] M. Long, C.-H. Wu, and J. Y. Hung, "Denial of service attacks on network-based control systems: Impact and mitigation," IEEE Trans. Ind. Informat., vol. 1, no. 2, pp. 85-96, May 2005.
[11] S. Hu and Q. Zhu, "Stochastic optimal control and analysis of stability of networked control systems with long delay," Automatica, vol. 39, no. 11, pp. 1877-1884, Nov. 2003.
[12] M. Garcia-Rivera and A. Barreiro, "Analysis of networked control systems with drops and variable delays," Automatica, vol. 43, no. 12, pp. 2054-2059, Dec. 2007.
[13] D. Yue, Q.-L. Han, and C. Peng, "State feedback controller design of networked control systems," IEEE Trans. Circuits Syst. II, Exp. Briefs, vol. 51, no. 11, pp. 640-644, Nov. 2004.
[14] H. Li, M.-Y. Chow, and Z. Sun, "State feedback stabilization of networked control systems," IET Control Theory Appl., to be published.
[15] H. Li, M.-Y. Chow, and Z. Sun, "Optimal stabilizing gain selection for networked control systems with time delays and packet losses," IEEE Trans. Control Syst. Technol., to be published.
[16] H. Li, Z. Sun, B. Chen, and H. Liu, "Intelligent scheduling control of networked control systems with networked-induced delay and packet dropout," Int. J. Control, Autom. Syst., vol. 6, no. 6, pp. 915-927, 2008.
[17] K. Natori and K. Ohnishi, "A design method of communication disturbance observer for time-delay compensation, taking the dynamic property of network disturbance into account," IEEE Trans. Ind. Electron., vol. 55, no. 5, pp. 2152-2168, May 2008.
[18] C. Lazar and S. Carari, "A remote-control engineering laboratory," IEEE Trans. Ind. Electron., vol. 55, no. 6, pp. 2368-2375, Jun. 2008.
[19] P. A. Bosman and J. Grahl, "Matching inductive search bias and problem structure in continuous estimation-of-distribution algorithms," Eur. J. Oper. Res., vol. 185, no. 3, pp. 1246-1264, Mar. 2008.
![img-7.jpeg](img-7.jpeg)

Hongbo Li received the B.S. degree from Northeastern University, Shenyang, China, in 2004. He is currently working toward the Ph.D. degree in the Department of Computer Science and Technology, Tsinghua University, Beijing, China.
He is also with the Electrical and Computer Engineering Department, North Carolina State University, Raleigh. His current research interests include networked control systems and intelligent control.
![img-8.jpeg](img-8.jpeg)

Mo-Yuen Chow (S'81-M'82-SM'93-F'07) received the B.S. degree in electrical and computer engineering from the University of Wisconsin, Madison, in 1982, and the M.Eng. and Ph.D. degrees from Cornell University, Ithaca, NY, in 1983 and 1987, respectively.
He is currently a Professor with the Electrical and Computer Engineering Department, North Carolina State University, Raleigh. His core technology is diagnosis and control, artificial neural networks, and fuzzy logic with applications to areas including motors, power systems, networked control systems, and unmanned vehicles.
![img-9.jpeg](img-9.jpeg)

Zengqi Sun (SM'93) received the Ph.D. degree in control engineering from Chalmers University of Technology, Goteborg, Sweden, in 1981.
He is currently a Professor with the Department of Computer Science and Technology, Tsinghua University, Beijing, China. His current research interests include intelligent control, robotics, fuzzy systems, neural networks, and evolutionary computing.