# Research Article 

## Decentralized Optimization Algorithms for Variable Speed Pumps Operation Based on Local Interaction Game

Shi-Qiang Wang (1) ${ }^{1}$ Jian-Chun Xing (1) ${ }^{1}$ Zi-Yan Jiang, ${ }^{2}$ and Yun-Chuang Dai ${ }^{2}$<br>${ }^{1}$ College of Defense Engineering, Army Engineering University of PLA, Nanjing, Jiangsu 210001, China<br>${ }^{2}$ Building Energy Research Center of Tsinghua University, Beijing 100084, China<br>Correspondence should be addressed to Jian-Chun Xing; xjc@893.com.cn

Received 28 November 2017; Accepted 17 June 2018; Published 9 July 2018
Academic Editor: Benoit Iung
Copyright © 2018 Shi-Qiang Wang et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

A fully distributed optimal control strategy for the parallel variable speed pumps in heating, ventilation, and air-conditioning (HVAC) systems is proposed. Compared with the traditional centralized method, the efficient control and coordination are scattered to every updated smart pump without the need for a monitoring host. Similar to the structure, mechanism, and characteristics of biological communities, a smart pump can communicate with adjacent nodes and operate collaboratively to complete pumps group operation with the least total power consumption under load demand and system constraints. And a decentralized optimization method that is decentralized estimation of distribution algorithm (DEDA) under local interaction games framework has been transplanted to the proposed structure to optimize the pumps working in parallel mode. Besides, convergence property of the two novel mechanisms is analyzed theoretically. Finally, simulation studies have been conducted based on the models of a physical pumps system, and the performance of the proposed algorithm is compared with centralized algorithms in terms of both effectiveness and stability. The results provide support for the validity of the proposed algorithms and control structure.

## 1. Introduction

A pumping system, which generally consists of several circulation pumps, is one of the main energy consuming parts in a chilled water based HVAC system. According to the International Energy Agency, electrical motors have consumed $46 \%$ of global electricity demand by end-use [1]. Furthermore, this rate is somewhat higher in the industrial area: up to almost $65 \%$ of generated electrical power [2]. And for the HVAC system, $60-70 \%$ of the power consumption is attributed to the water pumps and fan-based energy transmission in the water distribution system. These data has reflected the fact that there exists huge potential for energy conserving. And energy efficiency of a pumping system depends not only on the design but also, even more, on its operation. Thus an effective optimization should be proposed to improve the operating efficiency.

Currently, frequency converters are widely used with induction motor-driven pumps, enabling the pumps speed variation to control the head and flow rate of pumps under different working conditions in an energy-efficient way, that
is, variable speed pumps (VSPs). However, it makes the moderating process more complicated in that not only the combination of pumps but also the frequency of each pump needs to be determined compared to the nonvariable-speed pumps.

On the one hand, the physical models of pumps operation are difficult to be designed accurately and the pumps unit commitment is always a mixed integer programming problem, which leads to conventional optimization methods difficult to be used. In this case, the majority of existing researches focus on adopting different kinds of heuristic algorithms to solve such problems. Kecebas et al. utilized the artificial neural network to optimize the geothermal district heating systems [3]. Edson Bortoni had used the dynamic programming algorithm for optimizing a complex pumping system with a set of parallel centrifugal pumps and the efficiency of the method is verified through experiment[4]. Wang et al. introduced an enhanced evolutionary algorithm for biobjective pump scheduling in water supply [5]. Arun Shankar has conducted a comprehensive review of different methods for energy efficiency enhancement initiatives in

![img-0.jpeg](img-0.jpeg)

Figure 1: Structure of the centralized control system of a typical HVAC system.
centrifugal pumping system in recent years, and several practical evolutionary methods were also introduced [6]. However, the theory analysis of heuristic algorithms is not easy so that its convergence characteristic has not been studied well. Therefore, a more valid solving method needs to be applied to the pumps control in some critical application.

On the other hand, in most recent studies, the keynote has been put on updating the existing optimization methods or developing more effective ones[7, 8]. However, most of the current algorithms are developed based on a centralized structure, in which all the sensors and actuators are connected to one master controller and the field bus technology is usually used to handle the communication. Figure 1 has shown a typical physical structure of an HVAC system (Figure 1(a)) and a corresponding centralized control system (Figure 1(b))[9]. The sensors and actuators of each separate equipment are gathered to the master controller level by level through the linkers (RS485/Ethernet $<->$ analog quantities) on the field bus.

From the engineering perspective, the centralized control structure is not consistent with the physical system, so a mapping mechanism between the two systems is needed, such as configuring and commissioning. Therefore, the development incurs high maintenance and labor costs and somehow diminishes the flexibility and universality of a construction.

After that the key procedure is to write the control model and algorithm into the monitoring center. The mathematical model for the total system is always complex and difficult to be obtained. In the algorithm writing process, a lot of work is needed such as system recognizing, software developing, and operating debugging. Moreover, traditional centralized methods require information transmission to the supervising computer during operations, which can cause severe link congestion and operational lag. Besides, since all the devices are managed by the master controller, malfunctions in one device will also bring about influence on other devices which
will cause the entire control system running abnormally or even paralysis.

Recently, distributed multiagent control systems which are being focused on by many learners have provided a possible solution to this problem [10]. And Andrew Windham has analyzed the application prospects of the multiagent in HVAC control system[11]. However, the structures still require several local central nodes which are not fully distributed in our sense. And, in fact, the challenge is how to achieve the same performance as in a centralized manner where only local state information is available via each smart unit and is not considered in the above studies[12].

In this paper, a novel distributed control structure where each pump and chiller are updated to a smart unit by an embedded controller is proposed. These independent units can work independently and cooperate together to fulfill the global optimizing task.

To achieve the global optimization in a fully distributed way, a local interaction game is introduced into cognitive ratio networks in [13]. And using the log-linear algorithm[14-18], the network throughput is maximized. However, the log-linear algorithm is not applicable to the pumps optimal load distribution. Therefore, learning from the local state interaction games concept, a decentralized estimation of distribution algorithm (DEDA) is proposed in this paper. Simulation studies have been conducted based on physical models of the chilled water pumps system in a refrigeration station. The performance of DEDA is validated through comparison with centralized manner.

The rest of this paper is outlined as follows: In Section 2 the pumps system model is presented. Besides, potential game is introduced. Then a decentralized optimization model adaption is formulated in Section 3. And a decentralized algorithm is derived to solve the adapted mathematical model in this section. Section 4 focuses on performance assessment through simulations and experiments. Conclusions are drawn in Section 5.

## 2. System Model and Problem Formulation

2.1. Pumps Model and Its Decentralized Control System. The pump head and flow rate of a single VSP $i(i=1,2, \ldots, N)$ running at nonrated speed can be scaled from those of the pump running at the rated speed. According to the affinity laws of centrifugal pumps, the similarity working conditions of a VSP can be determined as

$$
\begin{aligned}
& \frac{Q_{i}(n)}{Q_{i}\left(n_{0}\right)}=\frac{n}{n_{0}} \\
& \frac{H_{i}(n)}{H_{i}\left(n_{0}\right)}=\left(\frac{n}{n_{0}}\right)^{2} \\
& \frac{\eta_{i}(n)}{\eta_{i}\left(n_{0}\right)}=1
\end{aligned}
$$

where $n_{0}$ is the rated pump speed and $n$ is the pump speed under nonrated conditions. $Q_{i}$ is the flow rate, $H_{i}$ is the pump head of each branch, and $\eta_{i}$ is the efficiency.

The speed ratio $w_{i}$ for each pump $i$ is described in (2) and $w_{0}$ is the lower limitation of the speed ratio.

$$
w_{i}=\frac{n}{n_{0}} \quad\left(w_{0}<w_{i}<1\right)
$$

And, the fitting formulas of pumps running at nonrated speed can be expressed as

$$
\begin{aligned}
H_{\text {set }} & =H_{i}=a_{i} Q_{i}^{2}+b_{i} w_{i} Q_{i}+c_{i} w_{i}^{2}, \quad i=1,2, \ldots, N \\
\eta_{i} & =j_{i}\left(\frac{Q_{i}}{w_{i}}\right)^{2}+k_{i}\left(\frac{Q_{i}}{w_{i}}\right)+l_{i}, \quad i=1,2, \ldots, N \\
W & =\sum_{i=1}^{N} W_{i}=\sum_{i=1}^{N} \frac{\rho g H_{i} Q_{i}}{\eta_{i}}
\end{aligned}
$$

where $H_{\text {set }}$ is the demanded pressure difference on the main pipe. $W$ is the total energy consumption of the pumps and $W_{i}=\rho g H_{i} Q_{i} / \eta_{i} \cdot \rho$ is the density of water, $g$ is the gravitational acceleration, $N$ is the quantity of pumps. $a_{i}, b_{i}, c_{i}$ and $j_{i}, k_{i}$, $l_{i}$ are static physical characteristics of different branches for pump $i(i=1,2, \ldots, N)$.

If the detected pressure difference $H_{o}$ is not equal to $H_{\text {set }}$, the control system will calculate the demanded total flow rate $Q_{p}$ as shown in (6). After that the moderating process will be conducted to ensure the pressure difference by moderating $w_{i}$ and make the calibration of each $Q_{i}$ satisfy $Q_{p}$.

$$
\begin{aligned}
H_{o} & =S Q_{o} \\
H_{\text {set }} & =S\left(\sum Q_{i}\right)^{2}=S Q_{p}^{2}
\end{aligned}
$$

where $S$ is the resistance of the current pipe net and $H_{o}$ and $Q_{o}$ are the current pressure difference and flow rate detected by the sensors.

In the largest pump systems, the pump groups are composed by several identical big pumps and one or two small pumps for energy saving. As shown in Figure 2, the
![img-1.jpeg](img-1.jpeg)

Figure 2: Decentralized control structure of a parallel pump system.
decentralized control system consists of $N$ smart updated pump by embedded microprocessors. A flow meter and a pressure meter will be connected to one of the smart units to detect the current state of the pipe net.

Each smart pump is connected hand to hand with its neighbor building up a chain-like form which corresponds to its actual engineering installation layout as shown in Figure 2. The model of each pump is stored in its smart unit as local variables and there is no need to model for the entire system as that in the centralized structure. And the control algorithm and instructions will be written into each smart pump and are identical. The load difference between supply and demand will be transmitted back and forth from one smart unit to another on the chain. And the operating state of each smart pump will be updated with the load difference between supply and demand transmitted from its neighbors. In such way, each smart device can be removed or substituted with little configuration making the system convenient to update and extend.
2.2. Problem Formulation. The operation object can be described as finding a combination of the running pumps and different pump can adopt a number of speed ratio strategies that can satisfy $Q_{p}$ with the least energy consumption. Thus, it can be built up as

$$
\begin{aligned}
\min & W \\
\text { s.t. } & Q_{i}^{\text {donon }}<Q_{i}<Q_{i}^{\text {sp }} \\
& \sum_{i=1}^{N} Q_{i}=Q_{p} \\
& i=1,2, \ldots, N
\end{aligned}
$$

where $Q_{d o n e n}^{i}$ and $Q_{n p}^{i}$ denote the power outputs limit of pump $i$.

Implementation of the centralized model (8) requires a central processor with the total system information. The fully distributed approaches remove the requirement of monitoring host and enable each updated smart DG to complete optimal load distribution task only based on local

and neighboring information. In this case, the centralized model (8) is split on each smart pump to be executed in a fully distributed and parallel manner across every processor core in each pump. Each part $i(i=1,2, \ldots, N)$ is a suboptimization problem of (8) as decentralized optimization.

Definition 1 (decentralized optimization for pumps load distribution). The decentralized optimization problem for each node $i(i=1,2, \ldots, N)$ is defined as

$$
\begin{aligned}
\min & W_{i} \\
\text { s.t. } & Q_{i}^{\text {down }}<Q_{i}<Q_{i}^{\text {up }} \\
& \sum_{i=1}^{N} Q_{i}=Q_{p} \\
& i=1,2, \ldots, N
\end{aligned}
$$

Indeed, (9) corresponds to part of the objective function (5). Note that each energy consumption $W_{i}$ of the pump $i(i=1$, $2, \ldots, N)$ is locally known by smart pump $i$ only. The penalty term is constructed by load difference and added to the utility function as (11) for pump $i(i=1,2, \ldots, N)$.

$$
\begin{aligned}
\min & U_{i}=W_{i}+P_{i}=W_{i}+\beta_{i}\left(\sum_{i=1}^{N} Q_{i}-Q_{p}\right)^{2} \\
& =W_{i}+\beta_{i}(\Delta Q)^{2}
\end{aligned}
$$

where $\beta$ is the penalty coefficient. The parameter $\beta$ balances the tradeoff between exploration and exploitation. Smaller $\beta$ implies that the smart pumps are more willing to choose a suboptimal action to explore, whereas higher $\beta$ implies that they are prone to choose the best response action. Therefore, it is advisable that, at the beginning phase, the value of $\beta$ is set to small number and it keeps increasing as the optimization iterates[19, 20]. $\Delta Q$ is the supply-demand difference. Then, (11) means that each pump $i$ should select a certain speed ratio strategy from its speed space to satisfy $Q_{p}$ with the least energy consumption.

Thus, the key problem lies in designing the mechanism to achieve global optimization via local interaction among nodes (the terms of agent, node, and smart pump refer to the same concept in this paper) only with direct communication links. As we all know, it is local interaction game. In this manner, optimal load distribution can be completed on the field level. In this paper, any method that solves (9)(10) without using a central node aggregating data is called decentralized algorithm.
2.3. Potential Game. Coordination and combinatorial optimization, when viewed from a game theory perspective, can form a subset of the class of potential games.

Definition 2 (potential games, [21]). Player action sets $\left\{S_{i}\right\}_{i=1}^{N}$, and $\bigcup_{i=1}^{N} S_{i}=S$, with player objective functions; $\left\{U_{i}: S \longrightarrow\right.$ $\left.R\right\}_{i=1}^{N}$ is a potential game if, for some potential function $\Phi$ : $S \longrightarrow R$,

$$
\begin{gathered}
U_{i}\left(s_{i}, s_{-i}\right)-U_{i}\left(s_{i}^{\prime}, s_{-i}\right)=\phi\left(s_{i}, s_{-i}\right)-\phi\left(s_{i}^{\prime}, s_{-i}\right) \\
\forall s_{i}^{\prime}, s_{-i} \in S_{i} \forall i \in\{1,2, \ldots, N\}
\end{gathered}
$$

for every player $P_{i} \in P$ where $\mathrm{P}=\left\{\mathrm{P}_{1}, \ldots, \mathrm{P}_{N}\right\}$ is a group of players (or agents) and $s_{-i}$ is the complimentary set of $s_{i}$.

And a number of learning algorithms can be found for the potential game. Most of the learning algorithms for potential games guarantee convergence to a (pure) Nash equilibrium.

Definition 3 (Nash equilibrium). A joint strategy profile, $s^{*}$, such that no individual agent has an incentive to change to a different strategy, that is,

$$
\begin{aligned}
U_{i}\left(s_{i}^{*}, s_{-i}^{*}\right)-U_{i}\left(s_{i}, s_{-i}^{*}\right) \geq & 0 \\
& \forall s_{i} \in S_{i} \forall i \in\{1,2, \ldots, N\}
\end{aligned}
$$

is a Nash equilibrium.
It is easy to see that, in potential games, any action profile maximizing the potential function is a pure Nash equilibrium. Hence, every potential game possesses at least one such equilibrium.

Consequently, each smart pump can be treated as a player and the energy consumption (11) is the utility function in potential game. And a potential game, as previously defined, requires perfect alignment between the global objective and the players' local objective functions in the following sense: if a player unilaterally changed its action, the change in its objective function would be equal to the change in the potential function. The pumps total cost function (7) is taken as the potential function in the optimization. Obviously, (9) subjected to (10) is a potential game.

However, there may also exist suboptimal pure Nash equilibrium that do not maximize the potential function[22]. Therefore, the key problem lies in how to design the mechanism to achieve the global optimization in a fully distributed way for the VSPs.

## 3. Decentralized Optimization Based on Probability Parallel Variable-Frequency Speed Pumps

In fact, there exist many evolutionary and swarm intelligent algorithms for coordination and combinatorial optimization in engineering[23, 24], but they might not be applicable to decentralized pumps control system due to a number of reasons. Firstly, the existing evolutionary or swarm intelligent algorithm refers to quite identical individualities. That is, every population in swarm intelligent algorithm or chromosomes in evolutionary algorithm involves a global variable, but only local information is available in the decentralized control structure of a parallel pump system. As an exploration, an example of multiple autonomous robots following simple local rules and collectively provided by [25] is quite

![img-2.jpeg](img-2.jpeg)

Figure 3: Comparison between EDA and decentralized optimization algorithm.
similar to the principles of the decentralized control system in this paper. However, the challenge is how to achieve the same performance as in a centralized manner where only local information is available.
3.1. Decentralized Estimation of Distribution Algorithm. Estimation of distribution algorithm (EDA) is an evolutionary optimization method that guides the search for the optimum by building and sampling explicit probabilistic models of promising candidate solutions[26]. Provided that a solution $\boldsymbol{x}$ has $N$ factors $\boldsymbol{x}_{i}, i=1,2, \ldots, N$, the probability distribution of observing $\boldsymbol{x}$ is estimated by the product of density for each factor as follows:

$$
P(\boldsymbol{x})=\prod_{i=1}^{N} P_{\theta_{i}}\left(\boldsymbol{x}_{i}\right)
$$

where $\theta_{i}$ is the vector of parameters for the probability density of factor $\boldsymbol{x}_{i}$.

The EDA is adapted into decentralized fashion in this study. DEDA is different from traditional evolutionary or swarm intelligent algorithms, where the populations of each smart pump only cover its own variable as shown in Figure 3.

And the detailed description of DEDA is illustrated in Figure 4. Further, from the potential game theory perspective, an adjustment mechanism can typically produce sequential or parallel actions by agents (smart pump). Observed by the characteristic of decentralized parallel pumps control structure, sequential random schedule with local interaction is adopted in the present study. And an arbitrary agent can be picked as the indicator in the pumps optimal load distribution.
3.2. Convergence Proof. The convergence proof of the DEDA is presented in Proposition 4 and illustrated in the following paragraph.

Proposition 4. The solution $x^{d e}=\left\{x_{1}^{d e}, \ldots, x_{i}^{d e}, \ldots, x_{N}^{d e}\right\}$ for the decentralized optimization (II) generated by DEDA can converge to the optimal Nash equilibrium with a probability of 1.

Proof. Assume the global solution space is defined as $\Omega$ $=\Omega_{1} \cap \Omega_{2} \cap \ldots \cap \Omega_{N}$, where $\Omega_{i}, i=1,2, \ldots, N$, is the space of the ith agent and its corresponding variable $x_{i}$. An elite-preserving operator is used in the presented algorithm. This operator favors the $g$ elites of a population by giving them an opportunity to be directly carried over to the next generation. Thus, the new population consists of $(L-g)$ new chromosomes, with $g<L$.

Firstly, the optimality convergence of each agent $i(i=1,2$, $\ldots, N)$ is discussed. The present study assumes that the search space $\Omega_{i}$ of problem (14) is a closed and bounded region. The objective function is taken as the fitness function $J_{i}\left(x_{i}\right)$, and the optimal solution set is expressed as

$$
D_{0}=\left\{x_{i} \in \Omega_{i} \mid\left|J_{i}\left(x_{i}\right)-J_{i}^{*}\right|<\varepsilon\right\}
$$

where $J_{i}^{*}=\min \left\{J_{i}\left(x_{i}\right): x_{i} \in \Omega_{i}\right\}$.
For agent $i(i=1,2, \ldots, N)$, the $L$ chromosomes of EDA can be divided into the following properties:
(I) At least one chromosome belongs to $D_{0}$, which is written as $S_{0}$.
(II) All $L$ chromosomes belong to $D_{1}$, which is written as $S_{1}$, where

$$
D_{1}=\Omega \backslash D_{0}
$$

![img-3.jpeg](img-3.jpeg)

Figure 4: Flow chart of the DEDA in each smart pump and executed in serial mode.

And if $q_{i j}(i, j=0,1)$ represents the probability that the $(k+1)$ th generation $x_{i}(k+1)$ transfers to $S_{i}$ when the $k$-th generation $x_{i}(k)$ keeps the state of $S_{i}$, then the following conditions hold:
(I) $x_{i}(k)$ at $S_{0}$ and $q_{i 0 i}=1$.

Condition (I) is obviously valid because the elitepreserving operator is used in this paper.
(II) $x_{i}(k)$ at $S_{1}$ and $q_{11} \leq c$, where $c \in(0,1)$.

Conditions (II) is analyzed as follows: For any $\varepsilon>0$, if $x_{i 0} \in\left\{x_{i} \in \Omega_{i} \mid\left|J_{i}\left(x_{i}\right)-J_{i}^{*}\right|<\varepsilon / 2\right\}$, there exists $r>0$ satisfying

$$
\left|J_{i}\left(x_{i}\right)-J_{i}\left(x_{i 0}\right)\right|<\frac{\varepsilon}{2}
$$

when

$$
\left\|x_{i}-x_{i 0}\right\|_{\infty a}=\max \left|x_{i}-x_{i 0}\right| \leq r
$$

Define

$$
Q_{x_{i 0}, r}=\left\{x_{i} \in \Omega_{i} \mid\left\|x_{i}-x_{i 0}\right\|_{\infty a} \leq r\right\}
$$

so that

$$
Q_{x_{i 0}, r} \subset D_{0}
$$

due to

$$
\begin{aligned}
\left|J_{i}\left(x_{i}\right)-J_{i}^{*}\right| & \leq\left|J_{i}\left(x_{i}\right)-J_{i}\left(x_{i 0}\right)\right|+\left|J_{i}\left(x_{i 0}\right)-J_{i}^{*}\right| \\
& <\frac{\varepsilon}{2} \leq \frac{\varepsilon}{2}=\varepsilon
\end{aligned}
$$

The probability that $x_{i}$ transfers to $S_{0}$ can be defined by

$$
P\left\{x_{i+} \in Q_{x_{i 0}, r}\right\}=P\left\{\left|x_{i+}-x_{i 0}\right| \leq r\right\}
$$

where $x_{i+}$ is the chromosome of a new generation and $i=1$, $2, \ldots, N$. Given that the evolutionary computation of EDA is based on probability, each element of the chromosome generates a series of the probability function $g\left(x_{i}\right)$, with $i=1$, $2, \ldots, N$.

For $x_{i+}$,

$$
x_{i+} \sim g\left(x_{i}\right)
$$

and thus

$$
P\left\{x_{i+} \in Q_{x_{i 0}, r}\right\}=\int_{x_{i 0}-r}^{x_{i 0}+r} g\left(x_{i}\right) d x_{i}
$$

For simplicity, $P\left\{x_{i+} \in Q_{x i 0, r}\right\}$ can be denoted by

$$
P_{1}\left(x_{i+}\right)=P\left\{x_{i+} \in Q_{x_{i 0}, r}\right\}
$$

and then

$$
0<P_{1}\left(x_{i+}\right)<1
$$

Define

$$
P_{1}\left(y_{i 0}\right)=\min P_{1}\left(x_{i+}\right)
$$

so that

$$
P_{1}\left(y_{i 0}\right) \leq P_{1}\left(x_{i+}\right) \leq q_{10}
$$

As

$$
q_{11}+q_{10}=1
$$

the following result can be achieved:

$$
q_{11}=1-q_{10} \leq c \quad(0<c<1)
$$

where the constant $c$ is

$$
c=1-P_{1}\left(y_{i 0}\right)
$$

Further, for any $\varepsilon>0$, set

$$
p_{k}=P\left\{\left|J_{i}\left(x_{i}^{*}(k)\right)-J_{i}^{*}\right| \geq \varepsilon\right\}
$$

and

$$
p_{k}= \begin{cases}0 & \exists T \in\{0,1,2, \ldots, k\}, x_{i}^{*}(T) \in D_{0} \\ \overline{p_{k}}, & x_{i}^{*}(m) \notin D_{0} m=0,1,2, \ldots, k\end{cases}
$$

Table 1: Pumps parameters.

| PAR | PUMP |  |  |  |
| :-- | :--: | :--: | :--: | :--: |
|  | 1.KP1020-3 406 | 2.KP1020-3 406 | 3.KP1020-3 457 | 4.KP1020-3 457 |
| $a$ | $-6.07 \mathrm{e}-6$ | $-5.36 \mathrm{e}-6$ | $-8.54 \mathrm{e}-6$ | $-8.41 \mathrm{e}-6$ |
| $b$ | $-0.00822$ | -0.00949 | -0.00048 | -0.00046 |
| $c$ | $60.41767$ | 60.61789 | 74.54932 | 73.55836 |
| $j$ | $-4.08 \mathrm{e}-7$ | $-3.96 \mathrm{e}-7$ | $-3.87 \mathrm{e}-7$ | $-3.82 \mathrm{e}-7$ |
| $k$ | 0.000940 | 0.000911 | 0.000999 | 0.000985 |
| $l$ | 0.316357 | 0.328377 | 0.249898 | 0.259137 |

and, thus, the following equation is obtained:

$$
\widetilde{p_{k}}=P\left\{x_{i}^{*}(m) \notin D_{0}, m=0,1,2, \ldots, k\right\}=q_{11}^{k} \leq c^{k}
$$

so that

$$
\sum_{k=1}^{\infty} \widetilde{p_{k}} \leq \sum_{k=1}^{\infty} c^{k}=\frac{c}{1-c}<\infty
$$

Then the following theorem is introduced to complete the proof process.

Theorem 5 (Borel-Cantelli theorem). The present study assumes that $A_{1}, A_{2}, \ldots$ is the event sequence based on probability and defines $p_{k}=P\left\{A_{k}\right\}$. If

$$
\sum_{k=1}^{\infty} p_{k}<\infty
$$

then

$$
P\left\{\prod_{m=1}^{\infty} \bigcup_{k \geq m} A_{k}\right\}=0
$$

If

$$
\sum_{k=1}^{\infty} p_{k}=\infty
$$

and $A_{k}$ are independent of one another, then

$$
P\left\{\prod_{m=1}^{\infty} \bigcup_{k \geq m} A_{k}\right\}=1
$$

According to Theorem 5,

$$
P\left\{\prod_{m=1}^{\infty} \bigcup_{k \geq m}\left\{\left|J_{i}\left(x_{i}^{*}(k)\right)-J_{i}^{*}\right| \geq \varepsilon\right\}\right\}=0
$$

is true. Therefore, $x_{i}^{\prime}(m)$, where $t=1,2, \ldots, L$, is the population of the $m$ th generation of EDA for agent $i(i=1,2, \ldots, N)$, which consists of $L$ chromosomes. If the fitness function $J_{i}\left(x_{i}\right)$ is continuous on the bounded region $\Omega_{i}$, the optimal solution $x_{i}^{*}(m)$ converges to the optimum for agent $i$ with a probability of 1 , and

$$
x_{i}^{*}(m)=\arg \min _{1 \leq t \leq L} J_{i}\left(x_{i}^{t}(m)\right)
$$

Then, the validity of the global optimization is deduced in the subsequent paragraphs.

According to the above analysis, the solution $x_{i}^{d e}$ can converge to the optimum $x_{i}^{* d e}$ for agent $i$ with a probability of 1 . Define the probability as $p_{i}$, that is,

$$
x_{i}^{d e} \xrightarrow{p_{i}} x_{i}^{* d e}
$$

and

$$
p_{i}=P\left\{\prod_{m=1}^{\infty} \bigcup_{k \geq m}\left\{\left|J\left(x_{i}^{d e}(k)\right)-J_{i}^{*}\right|<\varepsilon\right\}\right\}=1
$$

According to (24), the global combined probability density can be described as

$$
P=\prod_{i=1}^{N} p_{i}=1
$$

For the coupled variables, a similar result is also obtained:

$$
P=\frac{\left(\prod_{i=1}^{N} p_{i}\right)}{p_{i j}}=1
$$

Then the present study directly obtains

$$
x^{d e} \xrightarrow{P} x^{* d e}
$$

where $x^{* d e}=\left\{x_{1}^{* d e}, \ldots, x_{i}^{* d e}, \ldots, x_{N}^{* d e}\right\}$ is a Nash equilibrium of problem (11). In conclusion, $x^{d e}$ converges to an optimal solution of the centralized optimization problem with a probability of 1 as the iteration step $m \longrightarrow \infty$. Then Proposition 4 can be obtained as follows.

## 4. Case Study

4.1. Experimental Setup. This case study is carried out to validate the performance of DOABP by applying it to the model of a physical pump system under different load demands. The physical parameters (PAR) corresponding to performance curves of the pumps are shown in Table 1, and these parameters are recognized from the practical operating data of a district freezing station. As seen from Table 1, the performances of pumps of the same type are close to each other. The pump system is composed of four pumps working

Table 2: Pumps discreted strategy space.

| SR | PUMP |  |  |  |
| :-- | :--: | :--: | :--: | :--: |
|  | 1.KP1020-3 406 | 2.KP1020-3 406 | 3.KP1020-3 457 | 4.KP1020-3 457 |
| 1 | 0 | 0 | 0 | 0 |
| 2 | 0.93 | 0.94 | 0.825 | 0.825 |
| 3 | 0.94 | 0.945 | 0.85 | 0.85 |
| 4 | 0.945 | 0.95 | 0.875 | 0.875 |
| 5 | 0.95 | 0.955 | 0.9 | 0.9 |
| 6 | 0.96 | 0.96 | 0.915 | 0.915 |
| 7 | 0.97 | 0.97 | 0.925 | 0.925 |
| 8 | 0.98 | 0.98 | 0.95 | 0.95 |
| 9 | 0.99 | 0.99 | 0.975 | 0.975 |
| 10 | 1 | 1 | 1 | 1 |

Note. The speed ratio of 0 means that the pump is off.
in parallel mode including two big pumps (KP1020-3 457mm in impeller diameter) and two smaller pumps (KP1020-3 406 mm in impeller diameter) manufactured by Grundfos. A determined pressure difference control is applied here where the designed pressure difference and flow rate demand for the entire system are 45 m and $3234 \mathrm{~m}^{3} / \mathrm{h}$, respectively.
4.2. Simulation Result. The strategy space is discretized, and it becomes a limited strategy space to ensure that the potential game is a finite game. And, the speed ratio (SR) of each pump, as selected action set, is shown in Table 2.

In the case study, the proposed algorithms will be triggered as follows: when the pipe net has been changed, the smart unit will detect that the pressure difference $H_{u}$ is not equal to $H_{u d}$ and $Q_{u}$ which can be got through the flow meter on the trunk; thus $Q_{i}$ can be solved in (3).

DEDA can be downloaded to microprocessor chip in each smart pump $i(i=1,2,3,4)$, and then each smart pump can be active. And, each smart pump can communicate and cooperate with other smart pump nodes in serial mode. The corresponding results by the proposed DEDA are shown in Figure 5.

As shown in Figure 5, the probability distribution (PD) on each pump is dynamic during the iterative process in DEDA. And the optimal solution of each pump fluctuates and finally reaches a new equilibrium state under mutual negotiation and adjustment. By about 60 iteration steps, the pumps optimal load distribution task can be achieved. It can be seen that the probability of the optimal output flow rate tends to approach 1 . Conversely, the probability of the other solution space approaches 0 .

The iterative process of each pump $i(i=1,2,3,4)$ cost is illustrated in Figure 6. Further, the iterative process of total energy cost is shown in Figure 7.

Comparing Figure 6 and Figure 7, we find that although not all the costs of the four pumps decrease, the total cost decreases during the iterative process. This can validate the effectiveness of DEDA. For a comparison, the iterative process of EDA in centralized method is also illustrated in Figure 8. As shown in Figures 5 and 8, the DEDA can achieve
the actual optima which are equivalent to that obtained with the centralized algorithm.

Further, a more detailed calculation result is shown in Table 3, where EDA and DEDA are adopted, respectively.

## 5. Conclusion

respectivelyMost of the optimizing methods for parallel pump systems in HVAC system are based on a centralized structure under which all the management tasks have to be settled with one master controller. In this structure, the computation efficiency and stability are relatively low in that all the data and inspection have to be processed by one controller and that one malfunctioning device will influence the whole system. Besides, the control strategy is a case-by-case one which cannot be transplanted easily to other systems.

In this study, a decentralized control strategy has been applied to the parallel pump systems in which the traditional master controllers have been substituted by a list of independent smart units embedded in each pump.
(i) A new fully distributed mathematical model for pumps optimal distribution and decentralized flat architecture are presented. With the rapid development of the electronic industry, smart hardware has been widely utilized in different fields. According to the vision of the decentralized method, traditional units can be upgraded to smart agents by incorporating a microcontroller chip inside. The decentralized algorithm can be written into the chip. The smart unit communicates with neighboring nodes such that they can work collaboratively to achieve the optimal load distribution task. In this case, the complicated onsite modeling, configuration, commissioning, and other secondary developing work can be simplified to the wiring of communication connection among different nodes because the smart unit can selforganize and plug-and-play.
(ii) Decentralized optimization is used to solve pumps optimal load distribution under potential game framework. And, to achieve effectiveness of global goals, DEDA using local interaction is introduced. The convergence property of the novel method is also analyzed theoretically. Simulation

![img-8.jpeg](img-8.jpeg)

Pump 38:
![img-5.jpeg](img-5.jpeg)

Pump 28:
![img-6.jpeg](img-6.jpeg)

Pump 48:
![img-7.jpeg](img-7.jpeg)

Figure 5: Iterative process in decentralized optimization.
![img-8.jpeg](img-8.jpeg)

Figure 6: Iterative process of cost on each pump in decentralized optimization.

![img-9.jpeg](img-9.jpeg)

Figure 7: Iterative process of total cost in decentralized optimization.
![img-10.jpeg](img-10.jpeg)

Figure 8: Iterative process in centralized optimization.
results presented in the preceding paragraph indicate that the proposed method can achieve optimal load distribution.

This scenario is extremely motivating for further investigation in the field of distributed networked control in other large-scale interconnected nonlinear systems. And, there are still several potential issues of the presented method that needed to be emphasized here. Firstly, the proposed
mechanism is executed in sequence. Therefore, the proposed distributed algorithms should in principle be applicable to chain-like networks. Each smart pump is connected hand to hand with its neighbor, but the meshed network should also be considered. Secondly, future work will consider the hardware test and implementation on practical engineering.

Table 3: Comparison between centralized and decentralized results.

| \#Working condition |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Demand: $1496.9 \mathrm{~m}^{3} / \mathrm{h}$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ |
| Pump 1 | 47.00 | 700.17 | 0.79 | 47.00 | 700.17 | 0.79 |
| Pump 2 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Pump 3 | 41.25 | 796.71 | 0.85 | 41.25 | 796.71 | 0.85 |
| Pump 4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Power/kW |  | 227.4804 |  |  | 227.4804 |  |
| Difference |  | 0.0169 |  |  | 0.0169 |  |
| Demand: $2583.4 \mathrm{~m}^{3} / \mathrm{h}$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ |
| Pump 1 | 48.50 | 886.98 | 0.83 | 48.50 | 886.98 | 0.83 |
| Pump 2 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Pump 3 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Pump 4 | 48.75 | 1695.44 | 0.82 | 48.75 | 1695.44 | 0.82 |
| Power/kW |  | 392.2045 |  |  | 392.2045 |  |
| Difference |  | 0.9772 |  |  | 0.9772 |  |
| Demand: $2952.9 \mathrm{~m}^{3} / \mathrm{h}$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ |
| Pump 1 | 47.25 | 733.01 | 0.80 | 48.00 | 827.24 | 0.82 |
| Pump 2 | 49.00 | 926.41 | 0.84 | 47.50 | 745.89 | 0.80 |
| Pump 3 | 0.00 | 0.00 | 0 | 40.00 | 0.00 | 0 |
| Pump 4 | 45.00 | 1292.65 | 0.89 | 45.75 | 1579.76 | 0.88 |
| Power/kW |  | 435.5667 |  |  | 439.1761 |  |
| Difference |  | 0.8373 |  |  | 0.0181 |  |
| Demand: $3234.7 \mathrm{~m}^{3} / \mathrm{h}$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ |
| Pump 1 | 50.00 | 1054.53 | 0.85 | 48.50 | 886.98 | 0.83 |
| Pump 2 | 47.75 | 777.35 | 0.81 | 47.70 | 777.34 | 0.81 |
| Pump 3 | 45.75 | 1402.09 | 0.87 | 0.00 | 0.00 | 0.00 |
| Pump 4 | 40.00 | 0.00 | 0.00 | 47.50 | 1569.19 | 0.84 |
| Power/kW |  | 475.8191 |  |  | 485.6048 |  |
| Difference |  | 0.7344 |  |  | 1.1869 |  |
| Demand: $3858.3 \mathrm{~m}^{3} / \mathrm{h}$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ |
| Pump 1 | 47.00 | 700.17 | 0.79 | 48.50 | 886.98 | 0.83 |
| Pump 2 | 49.00 | 926.41 | 0.84 | 50.00 | 1037.53 | 0.85 |
| Pump 3 | 41.25 | 796.71 | 0.85 | 41.25 | 796.71 | 0.85 |
| Pump 4 | 46.25 | 1435.66 | 0.87 | 43.75 | 1136.63 | 0.89 |
| Power/kW |  | 572.8274 |  |  | 561.5738 |  |
| Difference |  | 0.6517 |  |  | 0.4537 |  |
| Demand: $4901.2 \mathrm{~m}^{3} / \mathrm{h}$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ | $n(\mathrm{~Hz})$ | $Q\left(m^{3} / h\right)$ | $\eta$ |
| Pump 1 | 49.00 | 944.62 | 0.84 | 48.00 | 827.24 | 0.82 |
| Pump 2 | 49.00 | 926.41 | 0.84 | 50.00 | 1037.51 | 0.85 |
| Pump 3 | 50.00 | 1831.72 | 0.78 | 46.25 | 1456.97 | 0.86 |
| Pump 4 | 46.25 | 1435.66 | 0.87 | 50.00 | 1815.93 | 0.79 |
| Power/kW |  | 778.3465 |  |  | 777.4647 |  |
| Difference |  | 0.4889 |  |  | 1.2384 |  |

## Conflicts of Interest

The authors declare that there are no conflicts of interest regarding the publication of this paper.

## Acknowledgments

This work is supported by National Key Research and Development Program of China No. 2017YFC0704100 (entitled

New Generation Intelligent Building Platform Techniques). And the authors are grateful for the support provided by the Tsinghua University-UTC Research Center for Integrated Building Energy, Safety, and Control Systems.

## References

[1] P. Waide and C. U. Brunner, Energy-efficiency policy opportunities for electric motor-driven systems, lea Energy Papers, 2011.

[2] P. Olszewski, "Genetic optimization and experimental verification of complex parallel pumping station with centrifugal pumps," Applied Energy, vol. 178, pp. 527-539, 2016.
[3] A. Keçebaş and I. Yabanova, "Thermal monitoring and optimization of geothermal district heating systems using artificial neural network: A case study," Energy and Buildings, vol. 50, pp. 339-346, 2012.
[4] E. da Costa Bortoni, R. A. Almeida, and A. N. C. Viana, "Optimization of parallel variable-speed-driven centrifugal pumps operation," Energy Efficiency, vol. 1, no. 3, pp. 167-173, 2008.
[5] J.-Y. Wang, T.-P. Chang, and J.-S. Chen, "An enhanced genetic algorithm for bi-objective pump scheduling in water supply," Expert Systems with Applications, vol. 36, no. 7, pp. 10249-10258, 2009.
[6] V. K. Arun Shankar, S. Umashankar, S. Paramasivam, and N. Hanigovszki, "A comprehensive review on energy efficiency enhancement initiatives in centrifugal pumping system," Applied Energy, vol. 181, pp. 495-513, 2016.
[7] Y.-F. Wang and Q. Chen, "A direct optimal control strategy of variable speed pumps in heat exchanger networks and experimental validations," Energy, vol. 85, pp. 609-619, 2015.
[8] Z. Tianyi, Z. Jili, and M. Liangdong, "On-line optimization control method based on extreme value analysis for parallel variable-frequency hydraulic pumps in central air-conditioning systems," Building and Environment, vol. 47, no. 1, pp. 330-338, 2012.
[9] H. Yu, T. Zhao, and J. Zhang, "Development of a distributed artificial fish swarm algorithm to optimize pumps working in parallel mode," Science and Technology for the Built Environment, pp. 1-11, 2017.
[10] A. Viehweider and S. Chakraborty, "Multi-Agent based Distributed Optimization Architecture for Energy-Management Systems with Physically Coupled Dynamic Subsystems," IFACPapersOnLine, vol. 48, no. 30, pp. 251-256, 2015.
[11] A. Windham and S. Treado, "A review of multi-agent systems concepts and research related to building HVAC control," Science and Technology for the Built Environment, vol. 22, no. 1, pp. 50-66, 2015.
[12] Y. C. Dai, Z. Y. Jiang, Q. Shen et al., "A decentralized algorithm for optimal distribution in HVAC systems," Building \& Environment, vol. 95, no. 2016, pp. 21-31, 2016.
[13] Y. Xu, J. Wang, Q. Wu, A. Anpalagan, and Y.-D. Yao, "Opportunistic spectrum access in cognitive radio networks: global optimization using local interaction games," IEEE Journal of Selected Topics in Signal Processing, vol. 6, no. 2, pp. 180-194, 2012.
[14] J. R. Marden, G. Arslan, and J. S. Shamma, "Regret based dynamics: Convergence in weakly acyclic games," in Proceedings of the the 6th international joint conference, pp. 194-201, Honolulu, Hawaii, May 2007.
[15] J. R. Marden, G. Arslan, and J. S. Shamma, "Joint strategy fictitious play with inertia for potential games," Institute of Electrical and Electronics Engineers Transactions on Automatic Control, vol. 54, no. 2, pp. 208-220, 2009.
[16] H. P. Young, Individual Strategy and Social Structure, Princeton University Press, Princeton, NJ, USA, 1998.
[17] C. H. Sun and H. B. Duan, "An evolutionary potential game theoretic approach for the K-cover problem in multi-UAV sensor networks," Scientia sinica Technologica, vol. 46, no. 10, pp. 1016-1023, 2016 (Chinese).
[18] Q. Zhang and H. Mühlenbein, "On the convergence of a class of estimation of distribution algorithms," IEEE Transactions on Evolutionary Computation, vol. 8, no. 2, pp. 127-136, 2004.
[19] Y. Song, C. Zhang, and Y. Fang, "Joint channel and power allocation in wireless mesh networks: A game theoretical perspective," IEEE Journal on Selected Areas in Communications, vol. 26, no. 7, pp. 1149-1159, 2008.
[20] M. V. Dolgopolik, "Smooth exact penalty functions: a general approach," Optimization Letters, vol. 10, no. 3, pp. 635-648, 2016.
[21] D. Monderer and L. S. Shapley, "Potential games," Games and Economic Behavior, vol. 14, no. 1, pp. 124-143, 1996.
[22] J. R. Marden, G. Arslan, and J. S. Shamma, "Cooperative control and potential games," IEEE Transactions on Systems, Man, and Cybernetics, Part B: Cybernetics, vol. 39, no. 6, pp. 1393-1407, 2009.
[23] G. Chen, L. Liu, P. Song, and Y. Du, "Chaotic improved PSObased multi-objective optimization for minimization of power losses and $L$ index in power systems," Energy Conversion and Management, vol. 86, pp. 548-560, 2014.
[24] N. Radhakrishnan, S. Srinivasan, R. Su, and K. Poolla, "Lear-ning-Based Hierarchical Distributed HVAC Scheduling With Operational Constraints," IEEE Transactions on Control Systems Technology, 2017.
[25] J. Werfel, K. Petersen, and R. Nagpal, "Designing collective behavior in a termite-inspired robot construction team," Science, vol. 343, no. 6172, pp. 754-758, 2014.
[26] P.-Y. Yin and H.-L. Wu, "Cyber-EDA: estimation of distribution algorithms with adaptive memory programming," Mathematical Problems in Engineering, vol. 2013, Article ID 132697, 11 pages, 2013.

![img-22.jpeg](img-22.jpeg)

The Scientific World Journal
![img-23.jpeg](img-23.jpeg)

Journal of
Sensors
![img-24.jpeg](img-24.jpeg)

Journal of
![img-25.jpeg](img-25.jpeg)

Civil Engineering
![img-26.jpeg](img-26.jpeg)

Journal of
Robotics
![img-27.jpeg](img-27.jpeg)

## Hindawi

Submit your manuscripts at www.hindawi.com
![img-28.jpeg](img-28.jpeg)

## Hindawi

Submit your manuscripts
![img-29.jpeg](img-29.jpeg)

Advances in OptoElectronics
![img-19.jpeg](img-19.jpeg)

International Journal of
![img-20.jpeg](img-20.jpeg)

International Journal of
Navigation
![img-21.jpeg](img-21.jpeg)

International Journal of
![img-22.jpeg](img-22.jpeg)

Molelling \& Simulation in Engineering
![img-23.jpeg](img-23.jpeg)

Actives and Passive Electronic Components
![img-24.jpeg](img-24.jpeg)

Shock and Vibration
![img-25.jpeg](img-25.jpeg)

Control Science and Engineering
![img-26.jpeg](img-26.jpeg)

Electrical and Computer Engineering
![img-27.jpeg](img-27.jpeg)

Electrical and Computer Engineering
![img-28.jpeg](img-28.jpeg)

Aerospace Engineering
![img-29.jpeg](img-29.jpeg)