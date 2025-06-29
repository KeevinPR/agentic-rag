# Optimal Stabilizing Gain Selection for Networked Control Systems With Time Delays and Packet Losses 

Hongbo Li, Mo-Yuen Chow, Fellow, IEEE, and Zengqi Sun, Senior Member, IEEE


#### Abstract

This brief addresses the optimal-stabilization problem for networked control systems (NCSs) with time delays and packet losses. The closed-loop NCS is modeled as a discrete-time switched system, and the stability conditions are derived in terms of linear matrix inequality. A controller design method with both system stability and control performance taken into account is proposed, and estimation of distribution algorithm is used to select the optimal stabilizing gain. The proposed method can be easily implemented to various applications, since it has simple structure and has no assumptions on time-delay and packet-loss models. Simulation and experimental results are given to demonstrate the effectiveness of the proposed approach.


Index Terms-Estimation of distribution algorithm (EDA), networked control systems (NCSs), packet loss, time delay.

## I. INTRODUCTION

NETWORKED control systems (NCSs) of which data networks are used for the connections between spatially distributed system components have recently attracted much attention from research communities. Issues such as time delays [1]-[5], packet losses [6], [7], network constraints [8], [9], signal quantization [10], [11], and scheduling [13] have been investigated, with results reported in the literature. In addition, due to the advantages of reduced system wiring, simple installation, increased system flexibility, and resources sharing, NCSs have been finding applications in dc motors [3], robots [4], vehicles [14], car suspension system [15], ball maglev system [16], industrial fish-processing machine [17], etc.

Time delay in NCSs is a major cause for system-performance deterioration and potential system instability. In the literature, time delays have been modeled by using various formulations such as constant delay [6], independently random delays [1], [2], and random delays governed by Markov chains [5]. Another important issue in NCSs is packet loss. There are two

Manuscript received March 24, 2008; revised June 13, 2008. Manuscript received in final form August 03, 2008. First published April 14, 2009; current version published August 26, 2009. Recommended by Associate Editor C. N. Hadjicostis. This work was supported in part by the National Science Foundation of China under Grant 60574035 and Grant 60674053, by the National Key Project for Basic Research of China under Grant 2002ch312205, and by the National Science Foundation under Grant IIS-0426852.
H. Li is with the Department of Electrical and Computer Engineering, North Carolina State University, Raleigh, NC 27606 USA, and also with the Department of Computer Science and Technology, State Key Laboratory of Intelligent Technology and Systems, Tsinghua University, Beijing 100084, China (e-mail: hli7@ncsu.edu; hb-l04@mails.tsinghua.edu.cn).
M.-Y. Chow is with the Department of Electrical and Computer Engineering, North Carolina State University, Raleigh, NC 27606 USA (e-mail: chow@ncsu. edu).
Z. Sun is with Department of Computer Science and Technology, State Key Laboratory of Intelligent Technology and Systems, Tsinghua University, Beijing 100084, China (e-mail: szq-dcs@mail.tsinghua.edu.cn).

Color versions of one or more of the figures in this brief are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TCST.2008.2004346
typical approaches to describe packet losses in the literature. The first approach assumes that packet losses follow certain probability distributions such as Markov chains. The second one is the deterministic approach, which specifies the packet losses in a time-averaged sense or in terms of bounds on max-imum-allowed consecutive packet losses. Note that the packets in NCSs usually suffer time delays and packet losses simultaneously during network transmission. Therefore, the analysis and synthesis of NCSs with time delays and packet losses is a challenge but practical problem. In the literature, some important methodologies, such as queuing methodology, stochastic optimal control, and predictive control, are proposed to address packet-loss and/or time-delay issues. However, these methods require large controller memory to store a large amount of past information, and the dynamic model of the plant has to be very precise [18]. Moreover, as pointed out in [1] and [18], for stochastic optimal control of NCSs, the probability distributions of time delays must be known a priori.

Memoryless state-feedback control is a simple and effective control method. It has a simple structure and does not require controller memory to store past information. Moreover, it has no assumptions on time-delay and packet-loss models. Therefore, memoryless state-feedback control for NCSs with time delays and packet losses, either in the continuous-time domain [18]-[20] or in the discrete-time domain [7], [21]-[25], has received considerable attention in the past few years. It was noticed that, for the controller design methods in the aforementioned results, most of them are derived directly from the stability conditions, and none of them considered the control performance during the controller design stage. As a result, the designed controller can only guarantee NCSs to be asymptotically stable while the control performance of NCSs may not be satisfied. However, control practices not only require an NCS to be asymptotically stable but also require the NCS to meet some performance specifications. Therefore, the memoryless state-feedback controller design method with both system stability and control performance taken into account is much needed, which motivates this brief.

In this brief, we investigate the optimal-stabilization problem for NCSs with time delays and packet losses. In this brief, the closed-loop NCS is modeled as a discrete-time switched system, and the stability conditions are derived in terms of linear matrix inequality. Based on the obtained stability conditions, estimation of distribution algorithm (EDA) is adopted to select the optimal gain for the corresponding stabilizing controller. In comparison with the existing stabilizing controllers, the proposed method takes both system stability and control performance into account during the controller design stage. Moreover, the proposed method can be easily implemented to various applications, since it is simple and has no assumptions

![img-0.jpeg](img-0.jpeg)

Fig. 1. Structure of the concerned NCSs.
on time-delay and packet-loss models. Simulation and experimental results are given to demonstrate the effectiveness of the proposed approaches.

Notation: Throughout this brief, $\mathbb{R}^{n}$ and $\mathbb{R}^{n \times m}$ denote the $n$-dimensional Euclidean space and the set of all $n \times m$ real matrices, respectively. $\|\cdot\|$ refers to the Euclidean norm for vectors and induced 2-norm for matrices. The superscript "T" denotes matrix transposition; and for symmetric matrices $X$ and $Y$, the notation $X>Y$ means that $X \sim Y$ is positive definite. $I$ is the identity matrix with appropriate dimensions, and the notation $\mathbb{Z}^{+}$stands for the set of nonnegative integers.

## II. Problem Formulation

As shown in Fig. 1, the considered NCS can be grouped into four modules: 1) the plant and the sensor; 2) the data network; 3) the networked controller; and 4) the actuator. Each module is described in the following sections.

## A. Controlled Plant and Sensor

The dynamics of the remote-controlled plant is given by the following linear discrete-time model:

$$
\boldsymbol{x}(k+1)=\boldsymbol{F} \boldsymbol{x}(k)+\boldsymbol{G} \boldsymbol{u}(k)
$$

where $\boldsymbol{x}(k) \in \mathbb{R}^{n}$ is the plant state and $\boldsymbol{u}(k) \in \mathbb{R}^{m}$ is the control input. $\boldsymbol{F}$ and $\boldsymbol{G}$ are known matrices with appropriate dimensions. Note that (1) can be considered as discretized from a continuous-time system given by

$$
\dot{\boldsymbol{x}}_{\mathrm{p}}(t)=\boldsymbol{A} \boldsymbol{x}_{\mathrm{p}}(t)+\boldsymbol{B} \boldsymbol{u}(t)
$$

with sampling period $h$ and

$$
\boldsymbol{F}=\mathrm{e}^{\boldsymbol{A} h} \quad \boldsymbol{G}=\int_{0}^{h} \mathrm{e}^{\boldsymbol{A} \tau} \mathrm{d} \tau \boldsymbol{B}
$$

The sensor is time-driven. At each sampling period, the sampled plant state and its timestamp (i.e., the time the plant state is sampled) are encapsulated into a packet and sent to the controller via the network.

## B. Data Network

In practice, the data packets in NCSs usually suffer time delays and packet losses during network transmissions. As shown in Fig. 1, sensor-to-controller delay and controller-to-actuator delay are denoted by $\tau_{\mathrm{sc}}$ and $\tau_{\mathrm{cs}}$, respectively, and two switches $S_{1}$ and $S_{2}$ are used to model the packet losses in the backward and the forward networks. For example, when $S_{1}$ is open,
the sensor packet is lost during network transmission from the sensor to the controller, whereas when $S_{1}$ is closed, the packet is successfully transmitted to the controller with a sensor-tocontroller delay $\tau_{\mathrm{sc}}$. Similar arrangements are for the forward network.

## C. Networked Controller

The networked controller is a memoryless state-feedback controller with the following form:

$$
\boldsymbol{u}=\boldsymbol{K} \tilde{\boldsymbol{x}}
$$

where $\boldsymbol{K} \in \mathbb{R}^{m \times n}$ is the feedback gain to be designed and $\tilde{\boldsymbol{x}}$ is the plant state from the arriving sensor packet. The controller is event-driven. Whenever there is a sensor packet that reaches the controller, the controller starts calculating the control signal. Immediately after the calculation, the new control signal and the timestamp of the used plant state are encapsulated into a packet and sent to the actuator via the network.

## D. Actuator

The actuator is time-driven. It is assumed that the actuator and the sensor have the same sampling period $h$, and they are synchronized. Note that the actuator and the sensor are at the same location, and theretofore, the synchronization between them can be easily achieved by hardware synchronization, for instance, using special wiring to distribute a global clock signal to the sensor and the actuator. The actuator has a buffer size of one, which means that the latest control packet is used to control the plant. Let $\tau_{k} \triangleq \tau_{\mathrm{sc}}(k)+\tau_{\mathrm{cs}}(k)$ express the round-trip-time (RTT) delay encountered by the $k$ th sampling time packet from the sensor, i.e., $\tau_{k}$ is from the time instant when the sensor samples the plant state to the time instant when the control signal based on this packet reaches the actuator. To simplify the analysis, we only use the control packets with $\tau_{k} \leq 2 h$ to control the plant (i.e., when a control packet reaches the actuator, it is used to update the buffer if its RTT delay is no longer than $2 h$ and its timestamp is newer than that of the control signal in buffer; otherwise, it will be discarded), but the idea behind this brief can be easily extended to the case $\tau_{k}>2 h$. The actuator uses a zeroth-order hold ( ZOH$)$. At each sampling period, the ZOH reads the control signal from buffer and uses it to control the plant.

## III. Discrete-Time Switched Model For NCSs

This section will present a discrete-time switched model for NCSs. To address this problem, we introduce the definition of an effective sensor packet, and it will be used throughout this brief. A packet from the sensor is called an effective sensor packet for controller (4), if its RTT delay is no longer than $2 h$. Let $S \triangleq\left\{i_{1}, i_{2}, \ldots\right\}$, a subsequence of $\{0,1,2, \ldots\}$, denotes the sequence of time index of effective sensor packets. Since only effective sensor packets are used to control the plant, the sensor packets between two effective sensor packets can all be considered as dropped packets. To avoid confusion, we used the following illustration to explain and demonstrate the used nota-

![img-2.jpeg](img-2.jpeg)

Fig. 2. Illustration of effective packets in NCSs.
tions. Let us assume that $S \triangleq\left\{i_{1}, i_{2}, i_{3}, i_{4}, \ldots\right\}$ in an NCS is $\{2,4,8,11, \ldots\}$ (see Fig. 2). It means that the 2 nd, 4 th, 8 th, and 11th sensor packets are effective sensor packets, while the $i$ th sensor packets $(i=3,5,6,7,9,10)$ are not used to control the plant, and they are considered as dropped packets.

Based on the earlier notations, the packet-loss process in the NCSs can be defined as

$$
\left\{\eta\left(i_{m}\right) \triangleq i_{m+1}-i_{m}, \quad i_{m} \in S\right\}
$$

which means that, from $i_{m}$ to $i_{m+1}$, the number of dropped packets is $\eta\left(i_{m}\right)-1$. For the sake of analysis, we define $\boldsymbol{N}_{\text {drop }} \triangleq \max _{i_{m} \in S}\left\{\eta\left(i_{m}\right)\right\}$. Then, we can conclude that $\eta\left(i_{m}\right)$ takes values in a finite set $\Omega \triangleq\left\{1,2, \ldots, \boldsymbol{N}_{\text {drop }}\right\}$.

Let $\tau_{i_{m}}$ express the RTT delay encountered by the $m$ th effective sensor packet. As shown in Fig. 3, for NCSs during the time interval between two effective packets, i.e., $\left[i_{m} h, i_{m+1} h\right]$, four cases may arise and are discussed as follows.
Case 1) $\tau_{i_{m}}=0$, i.e., the RTT delay encountered by the $m$ th effective sensor packet is zero. Since the sensor packets between two effective sensor packets are lost, the control input for $l \in\left[i_{m}, i_{m+1}\right)$ will be $\boldsymbol{u}(l)=\boldsymbol{K} \boldsymbol{x}\left(i_{m}\right)$ because of ZOH . Therefore, the dynamics of the NCS can be described as follows:

$$
\begin{aligned}
\boldsymbol{x}\left(i_{m}+1\right) & =\boldsymbol{F} \boldsymbol{x}\left(i_{m}\right)+\boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m}\right) \\
\boldsymbol{x}\left(i_{m}+2\right) & =\boldsymbol{F}^{2} \boldsymbol{x}\left(i_{m}\right)+\boldsymbol{F} \boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m}\right)+\boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m}\right) \\
& \vdots
\end{aligned}
$$

Correspondingly, for the time instant $i_{m+1} h$, we have

$$
\boldsymbol{x}\left(i_{m+1}\right)=\boldsymbol{F}^{\eta\left(i_{m}\right)} \boldsymbol{x}\left(i_{m}\right)+\sum_{j=0}^{\eta\left(i_{m}\right)-1} \boldsymbol{F}^{j} \boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m}\right)
$$

Case 2) $\tau_{i_{m}} \in(0, h]$, i.e., the RTT delay encountered by the $m$ th effective sensor packet ranges within $(0, h]$. In this case, the last control signal $\boldsymbol{K} \boldsymbol{x}\left(i_{m-1}\right)$ and the new control signal $\boldsymbol{K} \boldsymbol{x}\left(i_{m}\right)$ are used to control the plant during $\left[i_{m} h,\left(i_{m}+1\right) h\right)$ and $\left[\left(i_{m}+\right.\right.$ $1) h, i_{m+1} h)$, respectively. Therefore, the dynamics of the NCS can be described as follows:

$$
\begin{aligned}
\boldsymbol{x}\left(i_{m}+1\right) & =\boldsymbol{F} \boldsymbol{x}\left(i_{m}\right)+\boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m-1}\right) \\
\boldsymbol{x}\left(i_{m}+2\right) & =\boldsymbol{F}^{2} \boldsymbol{x}\left(i_{m}\right)+\boldsymbol{F} \boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m-1}\right)+\boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m}\right) \\
& \vdots
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)

Fig. 3. Illustration of time delays and packet losses in NCS.

Correspondingly, for the time instant $i_{m+1} h$, we have

$$
\begin{aligned}
\boldsymbol{x}\left(i_{m+1}\right)=\boldsymbol{F}^{\eta\left(i_{m}\right)} \boldsymbol{x}\left(i_{m}\right)+\sum_{j=0}^{\eta\left(i_{m}\right)-2} & \boldsymbol{F}^{j} \boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m}\right) \\
& +\boldsymbol{F}^{\eta\left(i_{m}\right)-1} \boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m-1}\right)
\end{aligned}
$$

where the notation $\sum_{j=a}^{b} \boldsymbol{F}^{j}$ satisfies the following property:

$$
\left\{\begin{array}{l}
\sum_{j=a}^{b} \boldsymbol{F}^{j}=0, \quad b<a \\
\boldsymbol{F}^{j}=0, \quad j<0
\end{array}\right.
$$

Note that property (10) is used to ensure that (9) is a general expression. For example, when $\eta\left(i_{m}\right)$ is one, (9) can be reduced to the first equation in (8) with property (10).
Case 3) $\tau_{i_{m}} \in(h, 2 h]$ and $\tau_{i_{m-1}}<\eta\left(i_{m-1}\right) h$, i.e., the RTT delay encountered by the $m$ th effective sensor packet ranges within $(h, 2 h]$, and the control signal based on the $(m-1)$ th effective sensor packet arrives at the actuator before the time instant $i_{m} h$. In this case, the new and the last control signals, i.e., $\boldsymbol{K} \boldsymbol{x}\left(i_{m}\right)$ and $\boldsymbol{K} \boldsymbol{x}\left(i_{m-1}\right)$, are used to control the plant during $\left[\left(i_{m}+2\right) h, i_{m+1} h\right)$ and $\left[i_{m} h,\left(i_{m}+\right.\right.$ 2) $h$ ), respectively. Based on the similar analysis in cases 1) and 2), the dynamics of the NCS in this situation can be described as follows:

$$
\begin{aligned}
\boldsymbol{x}\left(i_{m+1}\right)=\boldsymbol{F}^{\eta\left(i_{m}\right)} \boldsymbol{x}\left(i_{m}\right) & +\sum_{j=0}^{\eta\left(i_{m}\right)-3} \boldsymbol{F}^{j} \boldsymbol{G} \boldsymbol{K} x\left(i_{m}\right) \\
& +\sum_{j=\eta\left(i_{m}\right)-2}^{\eta\left(i_{m}\right)-1} \boldsymbol{F}^{j} \boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m-1}\right)
\end{aligned}
$$

Case 4) $\tau_{i_{m-1}} \in\left(\eta\left(i_{m-1}\right) h,\left(\eta\left(i_{m-1}\right)+1\right) h\right]$ and $\tau_{i_{m}} \in$ $(h, 2 h]$, i.e., the RTT delay encountered by the $m$ th effective sensor packet ranges within $(h, 2 h]$, and the control signal based on the $(m-1)$ th effective sensor packet arrives at the actuator during the time interval $\left(i_{m} h,\left(i_{m}+1\right) h\right]$. In this case, the new control signal $\boldsymbol{K} \boldsymbol{x}\left(i_{m}\right)$ is also used to control the plant during $\left[\left(i_{m}+2\right) h, i_{m+1} h\right)$. However, the last two

control signals, i.e., $\boldsymbol{K} \boldsymbol{x}\left(i_{m-2}\right)$ and $\boldsymbol{K} \boldsymbol{x}\left(i_{m+1}\right)$, are used to control the plant during $\left[i_{m} h,\left(i_{m}+1\right) h\right)$ and $\left[\left(i_{m}+1\right) h,\left(i_{m}+2\right) h\right)$, respectively. The dynamics of the NCS in this situation is described as

$$
\begin{aligned}
\boldsymbol{x}\left(i_{m+1}\right)= & \boldsymbol{F}^{\eta\left(i_{m}\right)} \boldsymbol{x}\left(i_{m}\right)+\sum_{j=0}^{\eta\left(i_{m}\right)-3} \boldsymbol{F}^{i} \boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m}\right) \\
& +\boldsymbol{F}^{\eta\left(i_{m}\right)-2} \boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m-1}\right)+\boldsymbol{F}^{\eta\left(i_{m}\right)-1} \boldsymbol{G} \boldsymbol{K} \boldsymbol{x}\left(i_{m-2}\right)
\end{aligned}
$$

From the earlier analysis, we can be seen that, during $\left[i_{m} h, i_{m+1} h\right]$, there are four different cases that may arise, and the corresponding dynamics of NCSs are described as four different subsystems (7), (9), (11), and (12). Now, taking all the subsystems into consideration, we introduce the augmented state $\boldsymbol{z}\left(i_{m}\right)=\left[\boldsymbol{x}_{i_{m-1}}^{\mathrm{T}} \boldsymbol{x}_{i_{m-2}}^{\mathrm{T}}, \boldsymbol{x}_{i_{m-2}}^{\mathrm{T}}\right]^{\mathrm{T}}$ into (7), (9), (11), and (12). Then, the four subsystems can be lumped into a general framework, which is described by the following discrete-time switched system:

$$
\boldsymbol{z}\left(i_{m+1}\right)=\boldsymbol{M}_{r\left(i_{m}\right)} \boldsymbol{z}\left(i_{m}\right)
$$

where $r\left(i_{m}\right)$ is a piecewise constant function called a switch signal, which takes values in a finite set $\mathbb{S} \triangleq\{1,2,3,4\}$. Noting that the switch state $r=1, r=2, r=3$, and $r=4$ are corresponding to (7), (9), (11), and (12), respectively, $\boldsymbol{M}_{r\left(i_{m}\right)}$ is in the form of (15), shown at the bottom of the page. Moreover, for $i_{m}<l<i_{m+1}$, the dynamics of NCSs can be expressed by

$$
\boldsymbol{z}(l)=\overline{\boldsymbol{M}}_{l, r\left(i_{m}\right)} \boldsymbol{z}\left(i_{m}\right)
$$

where $\boldsymbol{z}(l) \triangleq\left[\begin{array}{lll}\boldsymbol{x}_{l}^{\mathrm{T}} & \boldsymbol{x}_{i_{m-1}}^{\mathrm{T}} & \boldsymbol{x}_{i_{m-2}}^{\mathrm{T}}\end{array}\right]^{\mathrm{T}}, \overline{\boldsymbol{M}}_{l, r\left(i_{m}\right)}$ is similar to (15) but with $\eta\left(i_{m}\right)$ replaced by $l-i_{m}$.

Note that, in the NCS model (13), both time delays and packet losses are taken into account, and there is no assumption on the time-delay model or packet-loss model (i.e., the time delay can be constant, independently random, or random but governed by a Markov chain, and the packet losses can be independently random or random but governed by a Markov chain). Therefore, the NCS model (13) and the following proposed methods are quite general and can be applied to various applications. In the following theorem, the stability conditions are derived for NCSs via a state-dependent Lyapunov approach. This theorem will play an instrumental role in the controller design stage.

Theorem 1: NCS (13) in the presence of time delays and packet losses is asymptotically stable, if for $i, j \in \mathbb{S}$, there exist positive-definite matrices $\boldsymbol{P}_{i}$ and $\boldsymbol{P}_{j}$ satisfying

$$
\boldsymbol{M}_{i}^{\mathrm{T}} \boldsymbol{P}_{j} \boldsymbol{M}_{i}-\boldsymbol{P}_{i}<0
$$

where $\boldsymbol{M}_{i}$ is of form (15) with a given gain matrix $\boldsymbol{K}$.
Proof: For NCS (13), let a state-dependent Lyapunov function candidate be

$$
V\left(i_{m}\right)=\boldsymbol{z}^{\mathrm{T}}\left(i_{m}\right) \boldsymbol{P}_{r} \boldsymbol{z}\left(i_{m}\right)
$$

where $\boldsymbol{P}_{r}$ are matrices upon the switch state $r$ in the NCSs model (13). Let the switch signal $r$ at time instants $i_{m} h$ and $i_{m+1} h$ be $i$ and $j$, where $i, j \in \mathbb{S}$. The difference of Lyapunov function is given by

$$
\begin{aligned}
\Delta V(k) & =V(k+1)-V(k) \\
& =\boldsymbol{z}^{\mathrm{T}}\left(i_{m+1}\right) \boldsymbol{P}_{j} \boldsymbol{z}\left(i_{m+1}\right)-\boldsymbol{z}^{\mathrm{T}}\left(i_{m}\right) \boldsymbol{P}_{i} \boldsymbol{z}\left(i_{m}\right)
\end{aligned}
$$

Then, along the solution of the closed-loop system (13), we have

$$
\Delta V(k)=\boldsymbol{z}^{\mathrm{T}}\left(i_{m}\right)\left(\boldsymbol{M}_{i}^{\mathrm{T}} \boldsymbol{P}_{j} \boldsymbol{M}_{i}-\boldsymbol{P}_{i}\right) \boldsymbol{z}\left(i_{m}\right)<0
$$

for any $\boldsymbol{z}\left(i_{m}\right) \neq 0$. Moreover, for $i_{m}<l<i_{m+1}$, we have $V(l)=\boldsymbol{z}^{\mathrm{T}}\left(i_{m}\right) \overline{\boldsymbol{M}}_{l, i}^{\mathrm{T}} \boldsymbol{P}_{j} \overline{\boldsymbol{M}}_{l, i} \boldsymbol{z}\left(i_{m}\right)$. From the modeling process, we know that $\eta\left(i_{m}\right)$ in $\boldsymbol{M}_{i}$ takes values in $\Omega$, while $l-i_{m}$ in $\overline{\boldsymbol{M}}_{l, i}$ takes values in $\Omega-\left\{\boldsymbol{N}_{\text {drop }}\right\}$. Thus, if the condition (16) holds, we have

$$
V(l)-V\left(i_{m}\right)=\boldsymbol{z}^{\mathrm{T}}(l)\left(\overline{\boldsymbol{M}}_{l, i}^{\mathrm{T}} \boldsymbol{P}_{j} \overline{\boldsymbol{M}}_{l, i}-\boldsymbol{P}_{i}\right) \boldsymbol{z}(l)<0
$$

for any $\boldsymbol{z}(l) \neq 0$, where $i_{m}<l<i_{m+1}$.
From (19), we have $\lim _{i_{m} \rightarrow \infty} V\left(i_{m}\right)=0$. From (20), we get $\lim _{l \rightarrow \infty} V(l)=0$ for $l \neq i_{m}$. Summarizing the discussed two cases, we can conclude that $\lim _{l \rightarrow \infty} V(l)=0$ for $l \in \mathbb{Z}^{+}$, which implies that system (13) is asymptotically stable.

## IV. OPTIMAL STABILIZING CONTROLLER DESIGN

This section is concerned with the optimal stabilizing controller design problem. We will transform the controller design problem into an optimization problem and then solve the optimization problem.

$$
\begin{aligned}
& \boldsymbol{M}_{1}=\left[\begin{array}{cccc}
\boldsymbol{F}^{\eta\left(i_{m}\right)}+\sum_{j=0}^{\eta\left(i_{m}\right)-1} \boldsymbol{F}^{r} \boldsymbol{G} \boldsymbol{K} & 0 & 0 \\
\boldsymbol{I} & 0 & 0 \\
0 & I & 0
\end{array}\right] \quad \boldsymbol{M}_{4}=\left[\begin{array}{cccc}
\boldsymbol{F}^{\eta\left(i_{m}\right)}+\sum_{j=0}^{\eta\left(i_{m}\right)-3} \boldsymbol{F}^{r} \boldsymbol{G} \boldsymbol{K} & \boldsymbol{F}^{\eta\left(i_{m}\right)-2} \boldsymbol{G} \boldsymbol{K} & \boldsymbol{F}^{\eta\left(i_{m}\right)-1} \boldsymbol{G} \boldsymbol{K} \\
\boldsymbol{I} & 0 & 0 \\
0 & I & 0
\end{array}\right] \\
& \boldsymbol{M}_{2}=\left[\begin{array}{cccc}
\boldsymbol{F}^{\eta\left(i_{m}\right)}+\sum_{j=0}^{\eta\left(i_{m}\right)-2} \boldsymbol{F}^{r} \boldsymbol{G} \boldsymbol{K} & \sum_{j=\eta\left(i_{m}\right)-1}^{\eta\left(i_{m}\right)-2} \boldsymbol{G} \boldsymbol{F}^{r} \boldsymbol{G} \boldsymbol{K} & 0 \\
\boldsymbol{I} & 0 & 0 \\
0 & I & 0
\end{array}\right]
\end{aligned}
$$

## A. Optimization Variables

In the optimization problem, the optimization variables are the elements of the controller gain matrix $\boldsymbol{K} \in \mathbb{R}^{m \times n}$. For future use, we transform the optimization variables into a vector

$$
\tilde{\boldsymbol{K}}=\left(\tilde{K}_{1}, \tilde{K}_{2}, \ldots, \tilde{K}_{\tilde{S}}\right)
$$

where $\tilde{S}=m n$ is the dimension of $\tilde{\boldsymbol{K}}$.

## B. Cost Function

Different engineering applications have their performance measures, which can be used to construct their cost functions. In this brief, the mean square error, the overshoot, and the settling time are used to evaluate the NCSs' performance. The corresponding cost function is defined as follows:

$$
\begin{aligned}
\boldsymbol{J} & =\lambda_{1} \boldsymbol{J}_{1}+\lambda_{2} \boldsymbol{J}_{2}+\lambda_{3} \boldsymbol{J}_{3} \\
\boldsymbol{J}_{1} & = \begin{cases}0, & \mathrm{MSE} \leq \mathrm{MSE}_{\mathrm{n}} \\
\left(\mathrm{MSE}-\mathrm{MSE}_{\mathrm{n}}\right) / \mathrm{MSE}_{\mathrm{n}}, & \mathrm{MSE}<\mathrm{MSE}_{\mathrm{n}}\end{cases} \\
\boldsymbol{J}_{2} & = \begin{cases}0, & \left\|\mathrm{O} . \mathrm{S} .\right\| \leq\left\|\mathrm{O} . \mathrm{S} ._{\mathrm{n}}\right\| \\
\left(\mathrm{O} . \mathrm{S} .-\mathrm{O} . \mathrm{S} ._{\mathrm{n}}\right) / \mathrm{O} . \mathrm{S} ._{\mathrm{n}}, & \left\|\mathrm{O} . \mathrm{S} .\right\|<\left\|\mathrm{O} . \mathrm{S} ._{\mathrm{n}}\right\| \\
\boldsymbol{J}_{3} & = \begin{cases}0, & \mathrm{~S} . \mathrm{T} . \leq \mathrm{S} . \mathrm{T} ._{\mathrm{n}} \\
\left(\mathrm{~S} . \mathrm{T} .-\mathrm{S} . \mathrm{T} ._{\mathrm{n}}\right) / \mathrm{S} . \mathrm{T} ._{\mathrm{n}}, & \mathrm{~S} . \mathrm{T} .<\mathrm{S} . \mathrm{T} ._{\mathrm{n}}\end{cases}
\end{aligned}
$$

where

$$
\mathrm{MSE}=\frac{1}{N} \sum_{k=0}^{N}(\boldsymbol{r}(k)-\boldsymbol{y}(k))^{2}
$$

is the mean square error, $\mathrm{MSE}_{\mathrm{n}}$ is the nominal mean square error, O.S. is the overshoot, $\mathrm{O} . \mathrm{S}_{\mathrm{n}}$ is the nominal overshoot, S.T. is the settling time, and S.T. ${ }_{\mathrm{n}}$ is the nominal settling time. $\mathrm{MSE}_{\mathrm{n}}, \mathrm{O} . \mathrm{S}_{\mathrm{n}}$, and $\mathrm{S} . \mathrm{T}_{\mathrm{n}}$ are nominal performance measures that the system should achieve without network in the loop. If the NCS performance meets the nominal performance specifications, we have $\boldsymbol{J}=0$ because $\boldsymbol{J}_{i}=0, i=1,2,3$. In (23), $\boldsymbol{N}$ is the appropriate time index such that the tracking has arrived at the steady state; $\boldsymbol{r}(k)$ and $\boldsymbol{y}(k)$ are the reference input and plant output at time index $k$. The cost $\boldsymbol{J}_{1}$ penalizes poor response time and convergence, the cost $\boldsymbol{J}_{2}$ penalizes high value of the overshoot, and the cost $\boldsymbol{J}_{3}$ penalizes long settling time. The problem-dependent weights $\lambda_{1}, \lambda_{2}$, and $\lambda_{3}$ are used to specify the relative significance of $\boldsymbol{J}_{1}, \boldsymbol{J}_{2}$, and $\boldsymbol{J}_{3}$, respectively, on the overall system performance.

## C. SRC

A vector set $\Psi \subset \mathbb{R}^{1 \times \tilde{S}}$ is called the stable region of NCSs, if any vector $\tilde{\boldsymbol{K}} \in \Psi$ can satisfy the stability conditions described in (16), i.e., $\Psi$ is composed of $\tilde{\boldsymbol{K}}$ that can guarantee the NCSs to be asymptotically stable. Obviously, the controller gains that can provide satisfactory control performance for NCSs must be within the stable region (see Fig. 4), since satisfactory performance not only requires an NCS to be asymptotically stable but also require the NCS to meet some performance specifications. Therefore, it is sufficient to search the optimal controller gain within the stable region, which can effectively reduce the
![img-3.jpeg](img-3.jpeg)

Fig. 4. Graphical representation of the regions used in this brief.
search space and guarantee the stability of NCSs from a theoretical point of view. Based on this idea, stable region constraint (SRC) is introduced as follows:

$$
\text { SRC : } \quad \tilde{\boldsymbol{K}} \in \Psi \quad \forall \tilde{\boldsymbol{K}}
$$

which means that the optimization variables are constrained to the stable region throughout the optimization procedure.

In summary, the optimization problem can be expressed as

$$
\begin{aligned}
& \text { OP : } \min \quad \boldsymbol{J}(\mathrm{NCS}, \tilde{\boldsymbol{K}}) \\
& \text { s.t. } \mathrm{SRC}: \quad \tilde{\boldsymbol{K}} \in \Psi \quad \forall \tilde{\boldsymbol{K}}
\end{aligned}
$$

Equation (25) asks for $\tilde{\boldsymbol{K}}$ that minimizes the value of the cost function within the defined stable region. Obviously, the SRC can guarantee the stability of NCSs during the optimization procedure. On the other hand, by minimizing the cost function, the control performance of NCSs is optimized. Therefore, solving the optimization problem (25) offers a substantial advantage in that both stability and control performance can be guaranteed in the controller design stage.

For the optimization problem (25), heuristic-search algorithms such as genetic algorithm can be adopted to solve it. However, the behavior of these heuristic-search algorithms depends on many parameters. For researcher without associated experiences, the choice of suitable values for so many parameters is difficult. Unlike other evolutionary algorithms (EAs), EDA does not use crossover or mutation. Instead, EDA uses probability distribution model derived from the promising solutions to generate new population. Thus, one of the most appealing advantages of EDA over classical EAs is the reduction in the number of parameters to be tuned by the user. Moreover, it is noted that the optimization problem (25) is subjected to SRC. Therefore, to accelerate the search speed, a generic characteristic expected for the heuristic-search algorithm is that it can search the optimal solution within the defined stable region with high probability. As mentioned before, EDA adopts probability distribution model derived from the promising solutions to generate new population, which enables EDA to possess the required characteristic. Motivated by the earlier analyses, we adopt EDA to solve the optimization problem (25) in this brief. The optimization variables in the search space are modeled as a multivariate normal distribution $p(\tilde{\boldsymbol{K}})=\prod_{i=1}^{S} p\left(\tilde{K}_{i}\right)=\prod_{i=1}^{S}\left(\mu_{i}, \sigma_{i}\right)$, which is a product of $\tilde{S}$-independent univariate normal distributions $p\left(\tilde{K}_{i}\right)=\left(\mu_{i}, \sigma_{i}\right)$. The EDA algorithm used in this brief can be summarized as follows.

TABLE I
Statistical Measures (Minimum, Median, Mean and Maximum Delay, and Maximum Consecutive Packet Loss) of the RTT DelaYS and Packet LosSES From the ADAC Laboratory at NCSU to Different Destinations

Rule 1) Initialization: Generate $n_{1}$ gain candidates meeting SRC randomly to form an initial population.
Rule 2) Repeat the following steps until the termination criterion is met.
a) Selection: Select the best $n_{2}\left(n_{2}<n_{1}\right)$ gain candidates from the parent generation.
b) Updating: Update $p(\boldsymbol{K})$ using the selected $n_{2}$ promising gain candidates.
c) Sampling: Generate $n_{1}-1$ gain candidates meeting SRC based on the updated $p(\boldsymbol{K})$; copy the best gain candidate in the current population to the next population.
For more details on EDA, please refer to [26], [27], and the reference therein. It is noticed that, although we do not know the exact stable region of an NCS, we can realize the SRC based on the stability conditions described in (16). Taking step 1) for example, we can generate a gain candidate in the search space randomly and, then, check whether the gain candidate satisfies the stability conditions described in (16). If it does, the gain candidate will be selected as an individual of the population. Otherwise, we discard it and repeat the earlier steps until we obtain one satisfying the stability conditions (16). Similar arrangements are for step 2)-c).

## V. ILLUSTRATIVE EXAMPLES

This section provides a comprehensive study of proposed method. As a practical application, we apply the proposed method to a networked dc-motor system. Let $\boldsymbol{x}_{p}=[\theta, \omega]^{\mathrm{T}}$, where $\theta$ and $\omega$ are the motor angular position and the motor angular speed, respectively. The dc motor used in this brief can be expressed as

$$
\dot{\boldsymbol{x}}_{p}(t)=\left[\begin{array}{cc}
0 & 1 \\
1 & -217.4
\end{array}\right] \boldsymbol{x}_{p}(t)+\left[\begin{array}{c}
0 \\
1669.5
\end{array}\right] \boldsymbol{u}(t)
$$

The networked dc-motor system is designed to drive the dc motor to a preset angle of $40^{\circ}$. The performance specifications are given as follows.

1) Mean square error: $\mathrm{MSE} \leq 220^{\circ 2}$.
2) Overshoot: O.S. $\leq 0.1^{\circ}$.
3) Settling time: S.T. $\leq 8 \mathrm{~s}$.

Typical RTT delay and packet-loss information of packets between the Advanced Diagnosis And Control (ADAC) Laboratory at North Carolina State University (NCSU), Raleigh, U.S., and the destinations listed in Table I are measured for a 24-h period ( $0000-2400$ ). The statistical information on the experimental measures are listed in Table I, and the RTT delay histograms of 60000 packets are shown in Fig. 5. Those experimental measured data are used in numerical simulations and experimental verifications as follows: Each value of these RTT delays is divided by two and is utilized as $\tau_{\mathrm{sc}}$ and $\tau_{\mathrm{ca}}$; the packet loss is simulated either by the switch $S_{1}$ or by the switch $S_{2}$.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Histograms of RTT delays measured from ADAC Laboratory at NCSU to (a) www.utexas.edu, (b) www.ku.ac.th, and (c) www.tsinghua.edu.cn, where the $x$-axis is RTT delay (in milliseconds) and the $y$-axis is the number of packets.

## Numerical Simulations:

Case 1) NCS with network from the ADAC Laboratory at NCSU to www.utexas.edu.
We first consider the networked dc-motor system with network from the ADAC Laboratory at NCSU to www.utexas.edu. Table I shows that, in the used network, the RTT time delays range from 0.037 to 0.069 s , and the maximum consecutive packet losses is two. For the simulation study, we set the sampling period to 0.05 s . Noting that the networked system is designed to drive the dc motor to a preset angle, we introduce the reference input $\boldsymbol{r}$ into networked controller (4) and modify it into $\boldsymbol{u}=\boldsymbol{K} \ddot{\boldsymbol{x}}-\boldsymbol{K}(1,1) \boldsymbol{r}$. For the proposed controller design method, we set $n_{1}$ and $n_{2}$ in EDA to 50 and 20, and set $\mathrm{MSE}_{\mathrm{m}}, \mathrm{O}, \mathrm{S}_{\mathrm{m}}$, $\mathrm{S}, \mathrm{T}_{\mathrm{u}}, \lambda_{1}, \lambda_{2}$, and $\lambda_{3}$ in the cost function to $20,0.03$, $1,1,1$, and 1 , respectively. By applying the proposed controller design method to the networked system, we obtain the optimal gain $\boldsymbol{K}=[-0.4216,0.0102]$. With the initial state $\boldsymbol{x}_{0}=[3.65,0]^{\mathrm{T}}$, a typical step response of networked dc motor is shown in Fig. 6(a), where the corresponding network condition is shown in Fig. 6(d), which is selected from the experimental measures. The MSE, O.S., and S.T. corresponding to Fig. 6(a) are $28.27^{\circ 2}, 0^{\circ}$, and 1.15 s . Apparently, the

![img-5.jpeg](img-5.jpeg)

Fig. 6. Typical simulation results of the networked dc-motor control system with different network conditions.
system performance meets the given specifications very well, which demonstrates that the proposed controller provides a satisfactory performance.
Case 2) NCS with network from the ADAC Laboratory at NCSU to www.ku.ac.th.
We then consider the networked dc-motor system with network from the ADAC Laboratory at NCSU to www.ku.ac.th. To include as much data packets within $2 h$ as possible, we set the sampling period to 0.3 s . By considering the packets with $\tau_{k}>2 h$ as lost packets, the maximum consecutive packet losses becomes three, which is obtained based on the statistics of experimental measures of RTT delays and packet losses. We apply the proposed controller design method to the earlier networked system and obtain $\boldsymbol{K}=[-0.1202,-0.0139]$. A typical step response of networked dc motor is shown in Fig. 6(b), where the corresponding network condition is shown in Fig. 6(e). The MSE, O.S., and S.T. corresponding to Fig. 6(b) are $122.23^{\circ 2}, 0^{\circ}$, and 3.85 s . Apparently, the system performance meets the given specifications very well, which demonstrates that the proposed controller still provides a satisfactory performance even though worse network condition is considered.
Case 3) NCS with network from the ADAC Laboratory at NCSU to www.tsinghua.edu.cn
In fact, the proposed method can still stabilize the networked system with even more worse network condition. To illustrate this point, let us consider the networked dc-motor system with network from the ADAC Laboratory at NCSU to www.tsinghua.edu.cn. To include as much data
![img-6.jpeg](img-6.jpeg)

Fig. 7. Actual networked dc-motor system setup.
packets within $2 h$ as possible, we set the sampling period to 0.5 s . By considering the packets with $\tau_{k}>2 h$ as lost packets, the maximum consecutive packet losses becomes four, which is obtained based on the statistics of experimental network measures. We apply the proposed controller design method to the earlier networked system and obtain $\boldsymbol{K}=[-0.0691,-0.0169]$. A typical step response of networked dc motor is shown in Fig. 6(c), where the corresponding network condition is shown in Fig. 6(f). The MSE, O.S., and S.T. corresponding to Fig. 6(c) are $203.96^{\circ 2}, 0^{\circ}$, and 6.0 s . Apparently, the system performance still meets the given specifications, which demonstrates that the proposed controller can still provide a satisfactory performance even though more worse network condition is considered.
Experimental Verifications: To further illustrate the effectiveness and applicability of the proposed method, a networked dc-motor platform is constructed. The actual system setup is shown in Fig. 7, where the experimental apparatus consists of a PC controller, a local board, and a dc motor with sensors. The PC controller is used to implement the networked controller.

![img-7.jpeg](img-7.jpeg)

Fig. 8. Typical experimental results of the networked dc-motor control system with different network conditions.

The local board is on the plant side and used for two functions. The first function is to convert the control signal read from the buffer into a pulsewidth-modulation (PWM) signal and, then, send the PWM signal to drive the dc motor. The second function is to encapsulate the plant state and its timestamp into a packet and send it to the PC controller via the network. Both the local board and the sensor are time-driven, and they are synchronized by using the same clock signal.

In the experimental verifications, the PC controller and the dc motor were linked by a simulated network. Using real-time software and a hardware timer, the simulated network creates time delays by delaying the packets transmitted between the PC controller and the dc motor and creates packet losses by discarding the transmitted packets. The reasons for using the simulated network rather than using the actual network are as follows: 1) The experimental results can be compared with the simulation results under the same network condition and 2) the experiment is ensured to be repeatable for various investigations.
Case 4) NCS with network from the ADAC Laboratory at NCSU to www.utexas.edu.
Consider the network condition shown in Fig. 6(d). With the same initial state and controller gain as used in case 1), the experimental result of the networked dc motor is shown in Fig. 8(a). Apparently, the experimental result is consistent with the simulation result in case 1).
Case 5) NCS with network from the ADAC Laboratory at NCSU to www.ku.ac.th.
Consider the network condition shown in Fig. 6(e). With the same initial state and controller gain as used in case 2), the experimental result of the networked dc motor is shown in Fig. 8(b). Apparently, the experimental result is consistent with the simulation result in case 2).
Case 6) NCS with network from the ADAC Laboratory at NCSU to www.tsinghua.edu.cn.
Finally, consider the network condition shown in Fig. 6(f). With the same initial state and controller gain as used in case 3), the experimental result of the networked dc motor is shown in Fig. 8(c). Apparently, the experimental result is consistent with the simulation result in case 3).

The simulation and experimental results demonstrate the effectiveness of the proposed method for real-world application. Figs. 6 and 8 show that the control performance of networked system degrades when network conditions become worse. This phenomenon is reasonable, since NCS performance worsens with longer time delays and more packet losses. Note that the sampling period of the networked system increases from cases 1) to 3) and from cases 4) to 6). This demonstrates that larger sampling period is allowable in the NCSs design stage.

## VI. CONCLUSION

This brief presents a controller design method for a class of NCSs with time delays and packet losses. The most appealing advantage of the proposed method is that both system stability and control performance are considered during the controller design stage. The proposed method can be easily implemented to various applications, since it has simple structure and has no assumptions on time-delay and packet-loss models. Simulation and experimental results are given to demonstrate the effectiveness of the proposed approach.

## ACKNOWLEDGMENT

The authors would like to thank Associate Editor Prof. C. Hadjicostis and the anonymous reviewers for their constructive comments and suggestions, which have lead to important enhancements of the original manuscript.
