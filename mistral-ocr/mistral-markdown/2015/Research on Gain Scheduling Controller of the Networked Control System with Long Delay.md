# Research on Gain Scheduling Controller of the Networked Control System with Long Delay 

Jian-Qiu Deng*, Hong-Bo Li, Cui Hao, and Zeng-Qi Sun


#### Abstract

This paper addresses the stabilization and optimization problem of networked control systems (NCSs) with long time delays and parameter scheduling. According to the actual network conditions, the network time delay is divided into the fixed time delay and the random time delay. Then, the stabilization controller and the gain scheduling controller are constructed, where the stabilizing control parameters are obtained with cone complementary linearization (CCL) approach and the optimizing control parameters are solved with estimation of distribution algorithm (EDA). Simulation results demonstrate the effectiveness of the proposed methods.


Keywords: CCL, EDA, gain scheduling, long time delay, NCSs.

## 1. INTRODUCTION

NCSs are the extension and application of computer network in the control field, whose study is an interdisciplinary research area, combining both network and control theory. Time delays and packet losses are the two major causes for NCSs performance deterioration and potential system instability. Recently, NCSs have been extensively investigated. The research area includes tele-surgery [1-6], networked DC motor control [7-9], aerodynamic missile and torpedo [10], and tele-robot [11-14].

There are many research results in the NCSs field already. The NCSs model with multiple time delays was established by Gao, and Lyapunov-Krasovskii function was used to analyze the stability of the system [15]. The maximum allowable delay was solved by Kim based on Lyapunov-Krasovskii function [16]. The time delay between controller and sensor and the time delay between controller and actuator are considered in this method. So, it has a broader application range than the perturbation method.

In the discrete NCSs with clock-driven, the stochastic

[^0]optimal control method is proposed. Nilsson turned the NCSs with random time delay into the LQG(Linear Quadratic Gaussian) problem [17]. The stochastic optimal control problem of NCSs with linear quadratic cost function was researched by Zhu [18]. Besides, there are stochastic stabilization methods [19-21], stochastic $H_{\infty}$ control method [22], stochastic $\mathrm{H}_{2}$ control method [23].

Fuzzy control theory can be used in NCSs too. The fuzzy control theory was used by Almutairin to adjust the PI parameters of the NCSs [24]. The time delay of the network can be compensated by this method. A fuzzy stabilization controller design method in NCSs was proposed by Jiang [25]. A fuzzy switching method depends on the time delay of the network was proposed by Jia [26]. The nonlinear NCSs can be considered as a stable subsystem and a potentially unstable subsystem.

However, there are still some open problems to be addressed. To improve the universality of the networked method, the problems of analysis and design of NCSs with long time delay are studied.

The remainder of this paper is organized as follows: Section 2 describes the network conditions of the NCSs, and establishes the NCSs model based on that. Section 3 drives out the mathematics model of the NCSs, discusses the stability of the system, calculates and optimizes the scheduled gains of the controller. Section 4 takes servo motor NCSs as an example to simulate the control performance of the method proposed in this paper. Finally, Section 5 concludes the results of this study.

## 2. PROBLEM FORMULATION

In order to make the research close to the reality, the round-trip-delay of the network between Tsinghua University and Yahoo is measured by sending and receiving data packet every five seconds from Tsinghua side. The Fig. 1 shows the continuous ten thousand times of time delay on the network between Tsinghua and Yahoo. The test date is September 7th, 2010. Yahoo server's IP address is 66.94.230.34.


[^0]:    Manuscript received July 1, 2013; revised March 4, 2014; accepted May 29, 2014. Recommended by Associate Editor Yingmin Jia under the direction of Editor-in-Chief Young-Hoon Joo.

    The work was supported in part by the National Basic Research Program of China (973 Program) under Grant 2012CB821206, by the National Natural Science Foundation of China under Grant 61004021, 61174069, and by the Beijing Natural Science Foundation under Grant 4122037.

    Jian-Qiu Deng is with Naval Aeronautical and Astronautical University, Qingdao, China (e-mail: djq06@mails.tsinghua.edu.cn).

    Hong-Bo Li and Zeng-Qi Sun are with the Department of Computer Science and Technology, Tsinghua University, Beijing, China (e-mails: hb-li04@mails.tsinghua.edu.cn, szq-dcs@tsinghua. edu.cn).

    Cui Hao is with Beijing Information Science and Technology University, Beijing, China (e-mail: haocui0433234@163.com). * Corresponding author.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Continuous ten thousand times of time delay on the network between Tsinghua and Yahoo.

The sensor and the actuator are time driven. The controller is event driven. The results in Fig. 1 shows that time delay is varying in a small range near the average time delay in a certain period of time, and it is so long that we can't make them in one sampling period because of the poor control performance. It is more suitable to make the sampling period small, so the time delay is a few times of sampling period plus a time within a sampling period (i.e., the time delay $\tau$ is 320 ms , and the sampling period $h$ is 60 ms . So, the time delay is $\tau$ $=5 h+20)$.

## 3. DESIGN OF GAIN SCHEDULING CONTROLLER

### 3.1. System modeling and controller design

3.1.1 Network status division and monitor design

There are many kinds of standards to evaluate the quality of the network service (QoS). The packet loss rate is taken as QoS parameter of the network in this paper for its stability in a period of time, and the status of the network is divided into many grades on the base of the packet loss rate. The packet loss rate is defined as the ratio between the loss packets and the total packets in a period of time. The loss packet includes the packet whose time delay is longer than $(N+1) h$. N can be any number in the natural numbers set.

Suppose that the packet loss rate of the network in a period of time is $f_{\text {drop }}$, and the biggest packet loss rate is $f_{\text {drop }}^{\text {max }}$. So, the packet loss rate $f_{\text {drop }} \in\left[0, f_{\text {drop }}^{\text {max }}\right]$. Define that $Q o S \triangleq\left[0, f_{\text {drop }}^{\text {max }}\right] . Q o S$ is divided into $N_{Q o S}$ different sections, and the $q^{\prime}$ th section is defined as follow:

$$
Q o S_{q} \triangleq\left[f_{q}^{\min }, f_{q}^{\max }\right]
$$

where q is switch signal who has dividing ability, and it can take values in the set $W \triangleq\left\{1,2, \cdots, N_{Q o S}\right\} . \quad f_{q}^{\min }$ and $f_{q}^{\max }$ are the minimum and maximum of $Q o S_{q}$ respectively. The division of $Q o S$ satisfies the conditions described below:

$$
\begin{aligned}
& Q o S_{i} \cap Q o S_{j}=\Phi, \quad i, j \in W, \quad i \neq j \\
& Q o S_{1} \cup Q o S_{2} \cup \cdots \cup Q o S_{N_{Q o S}}=Q o S
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. The structure of the network controller with long time delay based on states feedback gain scheduling.
where $\Phi$ is the empty set.
The $Q o S$ of the network is changed all the time. So the monitor is monitoring the status of the network all the time and calculating the loss packet rate to estimate the network status level currently. Then the controller can schedule different parameters based on different $Q o S$.

### 3.1.2 Controller design

The structure of the network controller with long time delay based on states feedback gain scheduling is shown in Fig. 2. The QoS Monitor is used to monitor the quality of the network service. The controller will call different parameters based on different QoS of the network.

Suppose that the current $Q o S$ is $Q o S_{q}$. Because the effective packet has to delay $(N+1) h$ before effecting on the plant. If the packet sampled at the $k-N-1$ 'th instant is effective packet, the input value effecting on the actuator in the $k^{\prime}$ th instant is $\mathbf{u}(k)=\mathbf{u}_{c}(k-N-1)$ $=-\mathbf{L}_{q} \mathbf{x}(k-N-1)$. Thereinto, $\mathbf{u}(k)$ is the input of actuator, and $\mathbf{u}_{c}(k)$ is the output of controller.

Suppose that the augmented vectors are shown as below:

$$
\begin{aligned}
& \mathbf{z}\left(i_{m}\right)=\left[\begin{array}{lll}
\mathbf{x}\left(i_{m}\right)^{T} & \cdots & \mathbf{x}\left(i_{m-k+j}\right)^{T} \quad \cdots \\
\mathbf{x}\left(i_{m-k+n}\right)^{T} & \cdots & \mathbf{x}\left(i_{m-k}\right)^{T} \quad \cdots \quad \mathbf{x}\left(i_{m-N-1}\right)^{T}
\end{array}\right]^{T} \\
& \mathbf{z}\left(i_{m+1}\right)=\left[\begin{array}{lll}
\mathbf{x}\left(i_{m+1}\right)^{T} & \cdots & \mathbf{x}\left(i_{m-k+j+1}\right)^{T} \quad \cdots \\
\mathbf{x}\left(i_{m-k+n+1}\right)^{T} & \cdots & \mathbf{x}\left(i_{m-k+1}\right)^{T} \quad \cdots \quad \mathbf{x}\left(i_{m-N}\right)^{T}
\end{array}\right]^{T}
\end{aligned}
$$

1) If there is no new input effecting on the actuator, the transformational relationship from $\mathbf{x}\left(i_{m}\right)$ to $\mathbf{x}\left(i_{m+1}\right)$ is

$$
\begin{aligned}
& {\left[\begin{array}{c}
\mathbf{x}\left(i_{m+1}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-k+1}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-N}\right)
\end{array}\right]=\left[\begin{array}{lll}
\prod_{0} & \delta(1, k) \prod_{1} & \delta(2, k) \prod_{1} \\
1 & \ddots & \ddots \\
0 & & \ddots
\end{array}\right]} \\
& \left.\begin{array}{l}
\cdots \delta(N+1, k) \prod_{1} \\
0 \\
1
\end{array} \quad\left[\begin{array}{c}
\mathbf{x}\left(i_{m}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-k}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-N-1}\right)
\end{array}\right] .\right.
\end{aligned}
$$

For simplicity,
$\mathbf{z}\left(i_{m+1}\right)=\mathbf{M}_{i, j, k, q} \mathbf{z}\left(i_{m}\right)$,
$\mathbf{M}_{i, j, k, q}=$
$\left[\begin{array}{cccccc}\Pi_{0} & \delta(1, k) \Pi_{1} & \delta(2, k) \Pi_{1} & \cdots & \delta(N+1, k) \Pi_{1} \\ 1 & & & & & \\ & \ddots & & & & \\ & & & \ddots & & \\ 0 & & & & 1 & 0\end{array}\right]$
$\Pi_{0}=\mathbf{F}^{i_{m+1}-i_{m}} \quad \Pi_{1}=\sum_{i=0}^{i_{m+1}-i_{m}-1} \mathbf{F}^{i} \mathbf{G L}_{q}$,
$i \in\left\{1,2, \cdots, N_{\text {drop }}+1\right\}, \quad q \in W, \quad j=0$,
$k=\{1,2, \cdots, N+1\}, \quad \delta(n, k)=\left\{\begin{array}{ll}1, & n=k \\ 0, & n \neq k .\end{array}\right.$
2) If there is new input effecting on the actuator, the transformational relationship from $\mathbf{x}\left(i_{m}\right)$ to $\mathbf{x}\left(i_{m+1}\right)$ is shown in (5) which is listed in the previous page.
$\left[\begin{array}{c}\mathbf{x}\left(i_{m+1}\right) \\ \vdots \\ \vdots \\ \mathbf{x}\left(i_{m-k+j+1}\right) \\ \vdots \\ \mathbf{x}\left(i_{m-k+1+1}\right) \\ \vdots \\ \mathbf{x}\left(i_{m-k+1}\right) \\ \vdots \\ \mathbf{x}\left(i_{m-k+1}\right) \\ \vdots \\ \mathbf{x}\left(i_{m-k+1}\right) \\ \vdots \\ \mathbf{x}\left(i_{m-N}\right)\end{array}\right]=\left[\begin{array}{cccccc}\Pi_{0} & \frac{k-j-1}{0} & \Pi_{k-j} & \cdots & \Pi_{k-n} \\ 1 & & & 0 & & 0 \\ 0 & 1 & & \vdots & & \vdots \\ \vdots & \ddots & & \vdots & & \vdots \\ \vdots & & 1 & 0 & & \vdots \\ \vdots & & & 1 & & \vdots \\ \vdots & & & 0 & \ddots & 0 \\ \vdots & & & \vdots & & 1 \\ \vdots & & & \vdots & & 0 \\ \vdots & & & \vdots & & \vdots \\ \vdots & & & \vdots & & \vdots \\ 0 & & & 0 & & 0\end{array}\right]$
$\left[\begin{array}{cccccc}\Pi_{k} & \frac{N+1-k}{0} & \Pi_{k-j} & \cdots & \Pi_{k-n} & \cdots & \Pi_{k} \\ 0 & & & & \vdots \\ & \vdots & & & \vdots \\ & \vdots & & & \vdots \\ & \vdots & & & \vdots \\ & \vdots & & & \vdots \\ & \vdots & & & \vdots \\ & \vdots & & & \vdots \\ & \vdots & & & \vdots \\ & \vdots & & & \vdots \\ 0 & & & 1 & 0\end{array}\right]\left[\begin{array}{c}\mathbf{x}\left(i_{m}\right) \\ \vdots \\ \vdots \\ \vdots \\ \mathbf{x}\left(i_{m-k+j}\right) \\ \vdots \\ \mathbf{x}\left(i_{m-k+1}\right) \\ \vdots \\ \mathbf{x}\left(i_{m-k}\right) \\ \vdots \\ \vdots \\ \mathbf{x}\left(i_{m-N-1}\right)\end{array}\right]$
$\mathbf{z}\left(i_{m+1}\right)=\mathbf{M}_{i, j, k, q} \mathbf{z}\left(i_{m}\right)$,
$\mathbf{M}_{i, j, k, q}=$
$\left[\begin{array}{cccccc}\Pi_{0} & \frac{k-j-1}{0} & \Pi_{k-j} & \cdots & \Pi_{k-n} & \cdots & \Pi_{k} \\ 1 & & & 0 & & 0 & \cdots & 0 \\ 0 & 1 & & \vdots & & \vdots & & \vdots \\ \vdots & & \ddots & & \vdots & & \vdots & & \vdots \\ \vdots & & 1 & 0 & & \vdots & & \vdots \\ \vdots & & & 1 & & \vdots & & \vdots \\ \vdots & & & 0 & \ddots & 0 & & \vdots \\ \vdots & & & \vdots & & 1 & & \vdots \\ \vdots & & & \vdots & & 0 & \ddots & 0 \\ \vdots & & & \vdots & & \vdots & & 1 \\ \vdots & & & \vdots & & \vdots & & 0 \\ 0 & & 0 & & 0 & & 0 \\ & 1 & 0\end{array}\right]$
$\Pi_{0}=\mathbf{F}^{i_{m+1}-i_{m}}, \quad \Pi_{k-j}=-\sum_{j=0}^{i_{m+1}-i_{m-k+j}-N-2} \mathbf{F}^{j} \mathbf{G L}_{q}$,
$\Pi_{k-n}=-\mathbf{F}^{i_{m+1}-i_{m-k+n+1}-N-1} \sum_{j=0}^{i_{m-k+n+1}-i_{m-k+n-1}} \mathbf{F}^{j} \mathbf{G L}_{q}$,
$\Pi_{k}=-\mathbf{F}^{i_{m+1}-i_{m-k+1}-N-1} \sum_{j=0}^{i_{m-k+1}+N-i_{m}} \mathbf{F}^{j} \mathbf{G L}_{q}$,
$i \in\left\{1,2, \cdots, N_{\text {drop }}+1\right\}, q \in W, 1 \leq k \leq N+1,0<j \leq k$.
In the same way, the transformational relationship from $\mathbf{x}\left(i_{m}\right)$ to $\mathbf{x}\left(i_{m}^{p}\right)\left(i_{m}<i_{m}^{p}<i_{m+1}\right)$ is shown as follows:

1) If there is no new input effecting on the actuator, the transformational relationship from $\mathbf{x}\left(i_{m}\right)$ to $\mathbf{x}\left(i_{m}^{p}\right)$ is

$$
\begin{aligned}
& {\left[\begin{array}{c}
\mathbf{x}\left(i_{m}^{p}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-k+1}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-N}\right)
\end{array}\right]=\left[\begin{array}{cccc}
\Pi_{0} & \delta(1, k) \Pi_{1} & \delta(2, k) \Pi_{1} \\
1 & & \ddots & \\
& & & \ddots \\
0 & & & \ddots
\end{array}\right.} \\
& \left.\begin{array}{cccc}
\cdots & \delta(N+1, k) \Pi_{1} \\
0 & & \\
1 & 0 & \\
\cdots
\end{array}\right]\left[\begin{array}{c}
\mathbf{x}\left(i_{m}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-k}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-N-1}\right)
\end{array}\right]
\end{aligned}
$$

For simplicity,
$\mathbf{z}\left(i_{m}^{p}\right)=\tilde{\mathbf{M}}_{p, j, k, q} \mathbf{z}\left(i_{m}\right)$,
$\tilde{\mathbf{M}}_{p, j, k, q}=\left[\begin{array}{cccc}\Pi_{0} & \delta(1, k) \Pi_{1} & \delta(2, k) \Pi_{1} & \cdots & \delta(N+1, k) \Pi_{1} \\ 1 & & & 0 \\ & \ddots & & \\ & & \ddots & \\ 0 & & & 1 & 0\end{array}\right]$,
$\Pi_{0}=\mathbf{F}^{i_{m}^{p}-i_{m}} \quad \Pi_{1}=\sum_{j=0}^{i_{m}^{p}-i_{m}-1} \mathbf{F}^{j} \mathbf{G L}_{q} \quad i_{m}<i_{m}^{p}<i_{m+1}$.
Thereinto,

$$
\begin{aligned}
& i \in\{1,2, \cdots, N_{\text {drop }}\}, q \in W, j=0, k=\{1,2, \cdots, N+1\} \\
& \delta(n, k)= \begin{cases}1, & n=k \\
0, & n \neq k\end{cases}
\end{aligned}
$$

2) If there is new input effecting on the actuator, the transformational relationship from $\mathbf{x}\left(i_{m}\right)$ to $\mathbf{x}\left(i_{m}^{p}\right)$ is

$$
\left[\begin{array}{c}
\mathbf{x}\left(i_{m}^{p}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-k+j+1}\right) \\
\mathbf{x}\left(i_{m-k+j+1}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-k+1}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-k+1}\right) \\
\vdots \\
\vdots \\
\mathbf{x}\left(i_{m-N}\right)
\end{array}\right]=\left[\begin{array}{cccccc}
\Pi_{0} & \frac{k-j-1}{0} & \Pi_{k-j} & \cdots & \Pi_{k-n} \\
1 & & & 0 & & 0 \\
0 & 1 & & \vdots & & \vdots \\
\vdots & \ddots & & \vdots & & \vdots \\
\vdots & & 1 & 0 & & \vdots \\
\vdots & & & & 1 & & \vdots \\
\vdots & & & & 0 & \ddots & 0 \\
\vdots & & & & \vdots & & 1 \\
\vdots & & & & \vdots & & 0 \\
\vdots & & & & \vdots & & \vdots \\
\vdots & & & & \vdots & & \vdots \\
\mathbf{x}\left(i_{m-N}\right)
\end{array}\right] \left[\begin{array}{c}
\mathbf{x}\left(i_{m}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-k+j}\right) \\
\mathbf{x}\left(i_{m-k+1}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-k}\right) \\
\vdots \\
\mathbf{x}\left(i_{m-N-1}\right)
\end{array}\right]
$$

For simplicity,
$\mathbf{z}\left(i_{m}^{p}\right)=\widehat{\mathbf{M}}_{p, j, k, q} \mathbf{z}\left(i_{m}\right)$,
$\widehat{\mathbf{M}}_{p, j, k, q}=$
$\left[\begin{array}{cccccc}\Pi_{0} & \frac{k-j-1}{0} & \Pi_{k-j} & \cdots & \Pi_{k-n} & \cdots & \Pi_{k} & \frac{N+k-k}{0} \\ 1 & & 0 & & 0 & & 0 \\ 0 & 1 & & \vdots & & \vdots & & \vdots \\ & \vdots & \ddots & \vdots & & \vdots & & \vdots \\ \vdots & & 1 & 0 & & \vdots & & \vdots \\ \vdots & & & & 1 & & \vdots \\ \vdots & & & & 0 & \ddots & 0 \\ \vdots & & & \vdots & & & \vdots \\ \vdots & & & \vdots & & & \vdots \\ 0 & & 0 & & 0 & & 0 & 1 & 0\end{array}\right]$

$$
\begin{aligned}
& \Pi_{0}=\mathbf{F}^{p} \\
& \Pi_{k-j}=-\sum_{l=0}^{i_{m}^{p}-i_{m-k+j}-N-2} \mathbf{F}^{l} \mathbf{G} \mathbf{L}_{q} \\
& \Pi_{k-n}=-\mathbf{F}^{i_{m}^{p}-i_{m-k+n+1}-N-1} \sum_{l=0}^{i_{m-k+n+1}-i_{m-k+n-1}} \mathbf{F}^{l} \mathbf{G} \mathbf{L}_{q} \\
& \Pi_{k}=-\mathbf{F}^{i_{m}^{p}-i_{m-k+1}-N-1} \sum_{l=0}^{i_{m-k+1}+N-i_{m-k+1}} \mathbf{F}^{l} \mathbf{G} \mathbf{L}_{q}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& i \in\{1,2, \cdots, N_{\text {drop }}\}, \quad q \in W, \quad 1 \leq k \leq N+1 \\
& 0<j \leq k, \quad i_{m}<i_{m}^{p}<i_{m+1}
\end{aligned}
$$

### 3.2. Stability analysis

Theorem 1: Suppose that $\mathbf{L}_{q}$ is the state feedback gain of the controller which is scheduled right now. If there are positive matrixes $\mathbf{P}_{i} \in R^{(N+2) \mathrm{re}(N+2) \mathrm{n}}$ and $\mathbf{P}_{j} \in$ $R^{(N+2) \mathrm{re}(N+2) \mathrm{n}}$ which satisfy inequation (8), the NCSs is stable under the network condition $\Omega$.

$$
\widehat{\mathbf{M}}_{i}^{T} \mathbf{P}_{j} \widehat{\mathbf{M}}_{i}-\mathbf{P}_{i}<0 \quad \widehat{\mathbf{M}}_{i} \in \boldsymbol{\Xi}
$$

Thereinto, the set of parameter $\mathbf{M}_{i, j, k, q}$ is represented by $\boldsymbol{\Xi}$, so one element of the set is $\widehat{\mathbf{M}}_{i} \in \boldsymbol{\Xi}$.

Proof: The Lyapunov function of the NCSs is defined as:

$$
\mathbf{V}\left(i_{m}\right)=\mathbf{z}^{T}\left(i_{m}\right) \mathbf{P}_{i} \mathbf{z}\left(i_{m}\right)
$$

Based on (4), (5), and (9), equation (10) can be obtained.

$$
\begin{aligned}
\mathbf{V}\left(i_{m+1}\right) & =\mathbf{z}^{T}\left(i_{m}\right) \mathbf{M}_{i}^{T} \mathbf{P}_{j} \mathbf{M}_{i} \mathbf{z}\left(i_{m}\right) \\
\Delta \mathbf{V} & =\mathbf{V}\left(i_{m+1}\right)-\mathbf{V}\left(i_{m}\right) \\
& =\mathbf{z}^{T}\left(i_{m}\right)\left(\mathbf{M}_{i}^{T} \mathbf{P}_{j} \mathbf{M}_{i}-\mathbf{P}_{i}\right) \mathbf{z}\left(i_{m}\right)<0
\end{aligned}
$$

Thereinto, $\mathbf{z}\left(i_{m}\right) \neq 0$.
We can infer that $\lim _{i_{m} \rightarrow \infty} \mathbf{z}\left(i_{m}\right)=0$ based on (11). When $i_{m}<l<i_{m+1},\|\mathbf{z}(l)\|=\left\|\widehat{\mathbf{M}}_{i} \mathbf{z}\left(i_{m}\right)\right\| \leq \alpha\left\|\mathbf{z}\left(i_{m}\right)\right\|, \lim _{l \rightarrow \infty}\|\mathbf{z}(l)\|=0$ (thereinto, $l \neq i_{m}$ ). Summing up the above two kinds of case, we can infer that $\lim _{l \rightarrow \infty}\|\mathbf{z}(l)\|=0(l \in N)$.

Based on the NCSs' stable theorem, the NCSs is stable.
Corollary 1: Suppose that $\mathbf{L}_{q}$ is the state feedback gain of the controller which is scheduled right now. If there is a positive matrix $\mathbf{P} \in R^{(N+2) \mathrm{re}(N+2) \mathrm{n}}$ which satisfies inequation (12), the NCSs is stable under the network condition $\Omega$.

$$
\widehat{\mathbf{M}}_{i}^{T} \mathbf{P} \widehat{\mathbf{M}}_{i}-\mathbf{P}<0 \quad \widehat{\mathbf{M}}_{i} \in \boldsymbol{\Xi}
$$

Thereinto, the set of parameter $\mathbf{M}_{i, j, k, q}$ is represented by $\boldsymbol{\Xi}$, so one element of the set is $\widehat{\mathbf{M}}_{i} \in \boldsymbol{\Xi}$.

In the Feedback gain design process, the CCL algo-

rithm can be used to calculate the feedback gain $\mathbf{L}_{q}$, and the EDA algorithm can be used to solve the optimization problem.

## 4. SIMULATION EXAMPLE

The servo motor NCSs can be taken as an illustrative example to demonstrate the effectiveness of the controller design method mentioned in this paper. The state of the system is $\mathbf{x}_{p}=[\theta, \omega]^{T}$, where $\theta$ and $\omega$ are the angular and angular velocity of the system respectively. The dynamic equation of the servo motor is shown as below:

$$
\dot{\mathbf{x}}_{p}(t)=\left[\begin{array}{cc}
0 & 1 \\
0 & -217.4
\end{array}\right] \mathbf{x}_{p}(t)+\left[\begin{array}{c}
0 \\
1669.5
\end{array}\right] \mathbf{u}(t)
$$

Owing to the transmission medium and heavy network load, there are time delay and packet loss in the transmission. Suppose that the sampling period of the NCSs is 50 ms . When the packet loss ratio is in the set $[0,15 \%)$, the $Q \circ S$ level is $Q \circ S_{1}$, and when the packet loss ratio is in the set $(15 \%, 30 \%)$, the $Q \circ S$ level is $Q \circ S_{2}$.

Fig. 3 shows the simulation results of three different controllers: stabilization controller without parameters scheduling, stabilization controller with parameters scheduling, and optimized controller with parameters scheduling. The feedback gain of the stabilization controller without parameters scheduling is $\mathbf{L}_{1}=[0.1530$ 0.0120]. The feedback gain is obtained by CCL approach. The feedback gains of the stabilization controller with parameters scheduling are $\mathbf{L}_{2}^{*}=[0.15300 .0120]$ under the network condition $Q \circ S_{1}$, and $\mathbf{L}_{2}^{*}=[0.2040 \quad 0.0230]$ under the network condition $Q \circ S_{2}$ respectively. The feedback gains of the optimized controller with parameters scheduling are $\mathbf{L}_{3}^{*}=[0.46890 .0427]$ under the network condition $Q \circ S_{1}$, and $\mathbf{L}_{3}^{*}=[0.1471 \quad 0.0640]$ under the network condition $Q \circ S_{2}$ respectively.

Fig. 4 shows the network condition of the simulation. The circle represents the lost packet. Most time delay is
![img-2.jpeg](img-2.jpeg)

Fig. 3. The simulation results of three different controllers.
![img-3.jpeg](img-3.jpeg)

Fig. 4. The network condition of the simulation.
varying in the period [ 50 ms 100 ms ]. So, we can conclude that $N=1$ and the packet is lost when the time delay is more than 100 ms .

The simulation results show that the performance of the NCSs is prompted after parameters adjusting, and the performance of the NCSs is prompted a lot after parameters optimizing.

## 5. CONCLUSION

The modeling of the NCSs, stability analysis, feedback gain scheduling controller design and controller parameter optimizing are investigated in this paper in the situation of network with long time delay. The network state $Q \circ S$ is divided into $N$ grades and there are corresponding control parameter $L_{q}$ for every network grade $Q \circ S_{q}$. So, when the state of the network is different, different parameter is selected. In the end, for improving the performance of the system, the EDA algorithm is adopt to optimize the control parameter. The simulation results show that adopting different feedback gain of the system based on the different packet loss ratio can improve the performance of the NCSs, and the performance can be improved further after the parameters were optimized.

## REFERENCES

[1] M. Anvari, C. McKinley, and H. Stein, "Establishment of the World's first telerobotic remote surgical service for provision of advanced laparoscopic surgery in a rural community," Annals of Surgery, vol. 241, no. 3, pp. 460-464, 2005.
[2] M. Anvari and Remote, "Telepresence surgery: the Canadian experience surgical endoscopy," Annals of Surgery, vol. 21, no. 4, pp. 537-541, 2007.
[3] M. Anvari, "Telesurgery: remote knowledge translation in clinical surgery," World Journal of Surgery, vol. 31, no. 8, pp. 1545-1550, 2007.
[4] K. Kazuya and K. Yo, "Fujie Masakatsu G. Pilot study on verification of effectiveness on operability of assistance system for robotictele-surgery using simulation," Proc. of 32nd Annual International Conference of the IEEE Engineering-in-Medicine-and-Biology-Society, pp. 2308-2312, 2010.
[5] S. Seung, B. Kang, and H. Je, "Tele-operation mas-ter-slave system for minimal invasive brain surgery," Proc. of IEEE International Conference on Robotics and Biomimetics, pp. 177-182, 2009.
[6] N. Sriram and G. Aura, "Efficient force feedback transmission system for tele surgery," Proc. of 30th Annual International Conference of the IEEE-

Engineering-in-Medicine-and-Biology-Society, pp. 3245-3248, 2008.
[7] M. Y. Chow and Y. Tipsuwan, "Gain adaptation of networked DC motor controllers based on QoS variations," IEEE Trans. on Industrial Electronics, vol. 50, no. 5, pp. 936-943, 2003.
[8] G. P. Liu, Y. Xia, J. Chen, D. Rees, and W. Hu, "Networked predictive control of systems with random network delays in both forward and feedback channels," IEEE Trans. on Industrial Electronics, vol. 54, no. 3, pp. 1282-1297, 2007.
[9] Y. B. Zhao, G. P. Liu, and D. Rees, "Networked predictive control systems based on the Hammerstein model," IEEE Trans. on Circuits and Systems II, vol. 55, no. 5, pp. 469-473, 2008.
[10] J. A. Sparks, "Low cost technologies for aerospace applications," Microprocessors and Microsystems, vol. 20, no. 8, pp. 449-454, 1997.
[11] Y. Tipsuwan and M. Y. Chow, "Gain adaptation of networked mobile robot to compensate QoS deterioration," Proc. of the 28th Annual Conference of the IEEE industrial electronics society, Sevilla, Spain, pp. 3146-3151, 2002.
[12] Z. Yao and K. Gupta, "Distributed roadmaps for robot navigation in sensor networks," IEEE Trans. on Robotics, vol. 27, no. 5, pp. 997-1004, 2011.
[13] M. R. Stein, "Interactive internet artistry," IEEE Robotics and Automation Magazine, vol. 7, no. 2, pp. 28-32, 2000.
[14] S. H. Yang, X. Chen, and J. L. Alty, "Design issues and implementation of internet-based process control systems," Control Engineering Practice, vol. 11, no. 6, pp. 709-720, 2003.
[15] H. Gao, T. Chen, and J. Lain, "An new delay system approach to network-based control," Automatica, vol. 44, no. 1, pp. 39-52, 2008.
[16] D. S. Kim, Y. S. Lee, W. H. Kwon, and H. S. Park, "Maximum allowable delay bounds of networked control systems," Control Engineering Practice, vol. 11, no. 11, pp. 1301-1313, 2003.
[17] J. Nilsson, B. Bernhardsson, and B. Wittenmark, "Stochastic analysis and control of real-time systems with random time delays," Automatica, vol. 34, no. 1, pp. 57-64, 1998.
[18] Z. Qixin, H. Shousong, and L. Ya, "Infinite time stochastic optimal control of networked control systems with long delay," Control Theory and Applications, vol. 21, no. 3, pp. 321-326, 2004.
[19] L. Leiming, T. Chaonan, and W. Yankun, "Markovian jump model of networked control systems with dynamic output feedback controllers," Acta Automatica Sinica, vol. 5, pp. 627-631, 2009.
[20] F. Yang, Z. Wang, D. W. C. Ho, and M. Gani, "Robust $H_{\infty}$ control with missing measurements and time delays," IEEE Trans. on Automatic Control, vol. 52, no. 9, pp. 1666-1672, 2007.
[21] M. Weiguo and S. Cheng, "Stochastic stability for networked control systems," Acta Automatica Sinica, vol. 33, no. 8, pp. 878-882, 2007.
[22] J. Wu and T. Chen, "Design of networked control
systems with packet dropouts," IEEE Trans. on Automatic Control, vol. 52, no. 7, pp. 1314-1319, 2007.
[23] W. Wang, Y. Zhan, and F. Yang, "An $\mathrm{H}_{2}$ approach to networked control system," Acta Automatica Sinica, vol. 4, no. 2, pp. 219-224, 2008.
[24] B. Almutairin, Adaptive Fuzzy Modulation for Networked PI Control Systems, North Carolina State University, Carolina, 2002.
[25] X. Jiang and Q. L. Han, "On designing fuzzy controllers for a class of nonlinear networked control systems," IEEE Trans. on Fuzzy Systems, vol. 16, no. 4, pp. 1050-1060, 2008.
[26] X. Jia, L. Zheng, X. Chi, and D. Zhang, "A new approach to stabilization of a class of nonlinear networked control systems," Acta Automatica Sinica, vol. 11, pp. 1476-1480, 2009.
![img-4.jpeg](img-4.jpeg)

Jian-Qiu Deng received his Ph.D. degree in Computer Science and Technology from Tsinghua University in 2011. He is now an associate professor of Naval Aeronautical and Astronautical University. His research interests include networked control system, adaptive control, and optimum control.
![img-5.jpeg](img-5.jpeg)

Hong-Bo Li received his Ph.D. degree in Computer Science and Technology from Tsinghua University in 2009. He is now an assistant professor in the Department of Computer Science and Technology, Tsinghua University, Beijing, China. His current research interests include networked control systems and intelligent control.
![img-6.jpeg](img-6.jpeg)

Cui Hao received her B.S. degree from Beijing Information Science and Technology University, Beijing, China in 2008. She is now pursuing her Ph.D. degree in the School of Electronics and Information Engineering, Beijing Jiaotong University, Beijing, China. Her current research interests include networked control systems and intelligent control.
![img-7.jpeg](img-7.jpeg)

Zeng-Qi Sun received his Ph.D. degree in Control Engineering in 1981 from the Chalmas University of Technology in Sweden. He is currently a Professor in the Department of Computer Science and Technology, Tsinghua University, China. His current research interests include intelligent control, robotics, fuzzy systems, neural networks and evolution computing etc.