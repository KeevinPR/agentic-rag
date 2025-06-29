# Perspective 

## A novel strategy for power sources management in connected plug-in hybrid electric vehicles based on mobile edge computation framework

Yuanjian Zhang ${ }^{\mathrm{a}}$, Chong Guo ${ }^{\mathrm{a}}$, Yonggang Liu ${ }^{\mathrm{b}}$, Fei Ding ${ }^{\mathrm{c}}$, Zheng Chen ${ }^{\mathrm{d}, \mathrm{e}, \mathrm{c}}$, , Wanming Hao ${ }^{\mathrm{f}, * *}$<br>${ }^{a}$ State Key Laboratory of Automotive Dynamic Simulation and Control, College of Automotive Engineering, Jilin University, Changchun, 130022, China<br>${ }^{\mathrm{b}}$ State Key Laboratory of Mechanical Transmission \& School of Automotive Engineering, Chongqing University, Chongqing, 400044, China<br>${ }^{c}$ State Key Laboratory of Advanced Design and Manufacturing for Vehicle Body, College of Mechanical and Vehicle Engineering, Hunan University, China<br>${ }^{\mathrm{d}}$ Faculty of Transportation Engineering, Kunming University of Science and Technology, Kunming, 650500, China<br>${ }^{\mathrm{e}}$ School of Engineering and Materials Science, Queen Mary University of London, London, E1 4NS, UK<br>${ }^{1}$ Henan Institute of Advanced Technology, Zhengzhou University, Zhengzhou, 450003, China

## H I G H L I G H T S

- A novel power sources management strategy is proposed for cPHEVs.
- The mobile edge computing framework is built for the developing the strategy.
- Energy consumption is properly planed by EDA in each route segment.
- BP-NN and IDP are employed to actively adjust manners of energy consumption plan.

A R T I C L E I N F O

Keywords:
Power sources management
Mobile edge computation (MEC)
Estimation of distribution algorithm (EDA)
Machine learning based method
Connected plug-in hybrid electric vehicles (cPHEVs)

## A B S T R A C T

This paper proposes a novel control framework and the corresponding strategy for power sources management in connected plug-in hybrid electric vehicles (cPHEVs). A mobile edge computation (MEC) based control framework is developed first, evolving the conventional on-board vehicle control unit (VCU) into the hierarchically asynchronous controller that is partly located in cloud. Elaborately contrastive analysis on the performance of processing capacity, communication frequency and communication delay manifests dramatic potential of the proposed framework in sustaining development of the cooperative control strategy for cPHEVs. On the basis of MEC based control framework, a specific cooperative strategy is constructed. The novel strategy accomplishes energy flow management between different power sources with incorporation of the active energy consumption plan and adaptive energy consumption management. The method to generate the reference battery state-ofcharge (SOC) trajectories in energy consumption plan stage is emphatically investigated, fast outputting reference trajectories that are tightly close to results by global optimization methods. The estimation of distribution algorithm (EDA) is employed to output reference control policies under the specific terminal conditions assigned via the machine learning based method. Finally, simulation results highlight that the novel strategy attains superior performance in real-time application that is close to the offline global optimization solutions.

## 1. Introduction

### 1.1. Background and motivation

In recent years, society has witnessed rapid development in economy, culture and technologies. Nonetheless, pungent social conflicts
including energy dilemma, environmental pollution and global warming have drawn extensive attention [1,2]. Researchers and engineers have devoted to lighting the beacons for alleviating the social contradiction. For automobile industry, electrification brings a promising response. Amongst all the existing choices, connected plug-in hybrid electric vehicles (cPHEVs) have been regarded as one of effective solutions which

[^0]
[^0]:    ${ }^{a}$ Corresponding author. Faculty of Transportation Engineering, Kunming University of Science and Technology, Kunming, 650500, China.
    ${ }^{* *}$ Corresponding author.
    E-mail addresses: chen@kust.edu.cn (Z. Chen), wmhao@hotmail.com (W. Hao).

are equipped with high efficient internal combustion engines (ICEs) and large capacity batteries [3,4]. cPHEVs, one type of evolved PHEVs, are equipped with vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communication, holding larger potential in fuel economy improvement. However, integration of multiple power sources within PHEVs, pervasively, incurs the additional controlling degree of freedom in energy management, potentially empowering PHEVs with better fuel economy and more decrement of harmful gas emission [5,6]. Therefore, reasonable and even optimal allocation of power from different sources on the basis of internet of things is vital to fully exert the economy potential of cPHEVs. Consequently, designing an effective strategy by virtue of internet of things to intelligently manage the energy distribution between power sources of cPHEVs becomes the main research topic in this work.

### 1.2. Related works on power sources management strategies

A number of typical methods, referred to as power sources management strategies (PSMSs) or energy management strategies (EMSs), have been successfully proposed, including rule based strategies [7,8], optimization theory based strategies [9,10], and machine learning based strategies [11,12]. The rule-based strategies, holding relatively simple algorithm framework, have gained a great number of advocators in engineering practice. The simple candidates, such as threshold value strategies [13] and fuzzy logic strategies [14], control powertrain operation according to the preset logic derived from expert knowledge and experience, and often lead to non-optimal solution. Although some parameter optimization methods like genetic algorithms (GAs) [15] and particle swarm optimization (PSO) [16] have been successfully employed to improve control effect of rule based methods, the driving cycle dependent optimization still cannot guarantee adaptive application when faced with different driving conditions. Additionally, the optimization-based methods, such as dynamic programming (DP) [17], Pontryagin's minimum principle (PMP) [18], and quadratic programming (QP) [19], can attain the global optimal solutions, usually with the price of high computational complexity. Nonetheless, dependence on the prior knowledge of future driving conditions prevents the global optimization-based PSMSs from real-time implementation. In the premise of neglecting the validated minor difference with the global optimization-based PSMSs [20], the instantaneous optimization-based PSMSs have been progressively accepted for their potential of real-time implementation. Typical methods, i.e., equivalent minimization consumption strategy (ECMS) [21], and model predictive control (MPC) algorithms [22], have been widely researched. In spite of the preferable capability in real-time application, implementation effect of instantaneous optimization-based methods is still constrained by driving cycle information. Some inner parameters of strategies, e.g., the equivalent factor in ECMS [23], need to be dynamically adjusted in the light of the identified driving conditions. Machine learning based methods, such as the heuristic dynamic programming based methods [24] and reinforcement learning based methods [25], declare to achieve the rational controlling performance based on one or several historical driving cycle data. However, adaptability to variation of driving conditions should be further investigated.

Actually, flexibility of different driving conditions has been a critical factor that impedes optimal PSMSs implemented in real time, and expedites inspiration of some novel methods by integrating the vehicleenvironment cooperative control, such as adaptive ECMSs [26,27] and stochastic DP (SDP) [28,29]. By incorporating classification of driving conditions and/or prediction of future velocity into PSMSs, adaptive energy management responding to different conditions is therefore fulfilled prominently; whereas the onboard ability in self-adaptation of driving conditions imposes heavy computation burden on vehicle control unit (VCU), thus indirectly lowering the system efficiency. In addition, methods to identify driving conditions or forecast future driving behaviors, i.e. Markov Chain (MC) [30,31], demand a variety of
data for adaptive application in different driving conditions, and elevate the application cost significantly.

### 1.3. Related works on workload offloading optimization

Emergency of cPHEVs seems to be an ideal solution for the incurred tricky issues. cPHEVs, benefit from V2V and V2I communication, can acquire more environmental information and attain advanced vehicleenvironment cooperative control [32]. With the built predictive framework, which assimilates assistance from intelligent transportation systems (ITS), trip planning and energy management can be conducted successively in different layers, achieving the optimal real-time application [33]. As exhaustively described in former research, the raised PSMSs for cPHEVs can be divided into the route view based methods, eco-driving based algorithms, and predictive EMSs [10]. In most of them, energy flow between ICEs and battery packs is managed based on a multi-stage work, where velocity profiles or battery state-of-charge (SOC) trajectories need to be macroscopically planed by global optimization-based methods on account of the collected traffic status data, followed by the microcosmically optimal energy management based on the devised reference trajectories [34]. The combination of the long-term and short-term optimization prompts the performance of instant PSMSs. Despite the laudable merits, some work can be further performed to gain better performance:

1) The predictive framework can be rationally refined to enable each local controller to share computation burden evenly with zero-lag communication.
2) The calculation speed of planning reference trajectories can be accelerated while keeping the effect that is tightly close, or equal, to global optimization.

### 1.4. Contribution

In this context, we hereby presented a novel cooperative PSMS for cPHEVs based on the evolutional control framework, and the main contributions of this study can be attributed to the following two aspects:

1) A brand-new hierarchical control framework is designed. The twolayer control framework moves the computation task from the original on-board controller to the partial cloud based controller with several asynchronous units, thereby relieving heavy computation intensity originally imposed on the on-board hardware. The comparative analysis is performed to elaborately investigate the performance in general computation, communication speed and communication delay.
2) A cooperative control strategy is developed to conduct active energy consumption plan and adaptive energy management successively. The active plan module programs the energy consumption globally, while the adaptive management module achieves the immediate control by tracking the optimally planned results. The global energy consumption plan by estimation of distribution algorithm (EDA) is limited within each route segment to accelerate computation speed. To narrow the gap of global optimization planned in route segment and in the whole trip, the terminal constraints (ending battery SOC) is actively adjusted by the back-propagation neural network (BP-NN) and iterative DP (IDP) according to the shared traffic information.

The remainder of this paper is organized as follows. The cPHEV model is described in Section II. The designed control framework is detailed in Section III. Section IV presents the proposed cooperative strategy, and Section V discusses the simulation results and evaluates the performance of raised method. The main conclusions are made in Section VI.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The schematic of the cPHEV configuration.

Table 1
Specifications of components.

| Components | Variable | Values |
| :--: | :--: | :--: |
| Engine | Type | In-line four-cylinder petrol engine |
|  | Displacement | 2.0 L |
|  | Maximum Power | 103 kW @6200 rpm |
|  | Maximum Torque | 270 Nm @2500-6000 rpm |
| Motor | Maximum Power | 124 kW |
|  | Maximum Torque | 305 Nm |
|  | Maximum Speed | 12480 rpm |
| Battery | Type | Lithium-ion battery |
|  | Capacity | $21 \mathrm{~Ah} / 6.7 \mathrm{kWh}$ |
|  | Nominal Voltage | 300 V |
| Generator (Starter) | Maximum Power | 8.5 kW |
|  | Maximum Torque | 45 Nm |
| Gearbox | Type | 6-Speed AT |

## 2. Modeling of cPHEVS

As shown in Fig. 1, a single-axle parallel PHEV is employed for investigating the control framework and strategy. In it, the fuel energy and electric energy paths cooperatively exist. A 2.0 L Atkinson internal combustion engine (ICE) and a 6.7 kWh lithium-ion battery pack, considered as the power sources, provide the energy for vehicle driving. A 124 kW electric motor is responsible for propelling the vehicle and recycling the braking energy that is stored in the battery pack. The tractive torque from ICE and motor is transmitted to wheels through a 6speed automatic transmission. The detailed parameters of each component in powertrain are listed in Table 1. From Fig. 1, four operation modes exist in the studied PHEV, including the electric driving (EV) mode, hybrid driving assist (HDA) mode, hybrid driving charging (HDC) mode and engine driving modes.

At wheels, the tractive torque from ICE and motor is applied to overcome the driving resistance. The power balance equation can be formulated, as:
$P_{r e q}=\frac{v}{\eta_{i}}\left(\frac{G f \cos \alpha}{3600}+\frac{G \sin \alpha}{3600}+\frac{C_{D} A v^{2}}{76140}+\frac{\xi m a}{3600}\right)$
where $P_{\text {req }}$ is the required tractive power; $G, \alpha$ and $f$ denotes the gravity, gradient and rolling resistance factor, respectively; $C_{D}, A$ and $v$ is the aerodynamic drag factor, frontal area and vehicle speed, respectively; $a$ denotes the acceleration; and $\xi, \eta_{i}$ and $m$ expresses the correction coefficient of rotating mass, transmission efficiency, vehicle mass, respectively.

The relationship between the tractive torque at wheels and acceleration can be written as:

$$
\begin{aligned}
a=v(k)= & \frac{1}{m}\binom{T_{\text {reac }}(k)-\frac{1}{2} C_{D} A v(k)^{2}-m g f \cos \theta(k)-}{m g \sin \theta(k)} \\
& =\frac{1}{m} T_{\text {reac }} k-P_{1} v(t)^{2}-P_{2}
\end{aligned}
$$

where $P_{1}=\frac{1}{2} C_{D} A v(k)^{2}, P_{2}=m g f \cos \theta(k)+m g \sin \theta(k)$, and $g$ denotes the gravity acceleration. The tractive torque at wheels comes from the ICE and motor, of which the relationship can be expressed as:
$T_{\text {req }}=T_{\text {fuel_path }}+T_{\text {ele_path }}$
where $T_{\text {req }}$ is the required tractive torque; $T_{\text {fuel_path }}$ and $T_{\text {ele_path }}$ is the tractive torque provided by the fuel path and electric path, respectively. In different operating modes, the tractive force transmitted to wheels can be calculated as:
$F_{i}=\left\{\begin{array}{cc}\frac{\left(T_{\text {req }}+T_{\text {em }}\right) i_{g b}\left(n_{g}\right) i_{b t} \eta_{i}}{R_{w h}} & S_{i h}=1 \\ \frac{T_{\text {em }} i_{g b}\left(n_{g}\right) i_{b t} \eta_{i}}{R_{w h}} & S_{i h}=1\end{array}\right.$
where $T_{\text {req }}$ and $T_{\text {em }}$ denotes the engine and motor torque, respectively; $i_{g b}$ and $i_{b t}$ denotes the gear and final drive ratio; $n_{g}$ is the gear number; and $R_{\text {wh }}$ is the wheel radius. In (4), $S_{\text {iht }}=1$ means the clutch is engaged, and in contrast $S_{\text {iht }}=0$ denotes the clutch is disengaged. Based on the static engine model, in which the efficiency map can be acquired from a benchmark calibration, the engine efficiency can be described as:
$\eta_{\text {req }}\left(T_{\text {req }}, n_{\text {req }}\right)=\frac{T_{\text {req }} \omega_{\text {req }}}{Q_{\text {fin }} \dot{m}_{2}}$
where $\eta_{\text {req }}$ denotes the engine net efficiency, $\omega_{\text {req }}$ means the rotating speed of engine, $Q_{\text {fin }}$ represents the fuel lower heating value, and $\dot{m}_{2}$ expresses the fuel consumption rate. Due to the fast transient response, the dynamic behaviors of electric motor are neglected. In the parallel PHEV, the electric motor can operate as the tractive motor or generator, and the relationship between the motor torque and power can be expressed as:
$P_{e m}= \begin{cases}\frac{T_{\text {em }} \omega_{\text {em }}}{\eta_{\text {mex }}} & T_{\text {em }}>0 \\ T_{\text {em }} \omega_{\text {em }} \eta_{\text {gen }} & T_{\text {em }} \leq 0\end{cases}$
where $\omega_{\text {em }}$ is the angular speed of electric motor; $P_{\text {em }}$ is the power of electric motor; and $\eta_{\text {mex }}$ and $\eta_{\text {gen }}$ denotes the efficiency in tractive mode

![img-1.jpeg](img-1.jpeg)

Fig. 2. Illustration on designed control framework and methods. (a) The illustration of the proposed framework. (b) MEC-based IoV system. (c) The time frame for the MEC-based IoV. (d) Delay versus transmit power at the vehicle. (e) Transmit rate versus transmit power at the vehicle. (f) The control process of the proposed strategy.

and generator mode, respectively. For easing of modeling the battery, the influence of operating temperature and degradation is neglected, and a simple equivalent circuit model is employed to characterize the battery electrical performance. The variation of SOC can be calculated as:
$S O ̈ C=-\frac{V_{o s}-\sqrt{V_{o s}-4 R_{n t} P_{b u t}}}{2 R_{n t} Q_{b u t}}$
where $V_{o s}$ is the open circuit voltage of battery, $R_{n t}$ is the internal resistance of battery, $P_{\text {butt }}$ is the battery power, and $Q_{\text {butt }}$ is the battery capacity.

## 3. The proposed control framework

### 3.1. The novel MEC based control framework

Generally, conventional vehicle controllers are installed in vehicle bodies. After recognizing driving requirement from drivers, high level control units in controllers will rationally choose the suitable operation modes and properly manage the energy flow successively. Energy distribution orders will be sent to the lower control units for driving operation of powertrain components. In the single-framework based controllers, control orders are executed through multiple stage operations. After integrating complex optimal control algorithms to the singleframework based controller, the computation burden will be undoubtedly increased.

To lessen the computation burden imposed on the VCU, a novel control framework is therefore developed. In the brand-new control framework, partial control tasks are shifted to the mobile edge computation units (MECUs) [35-38] at roadside, thereby fully exploiting merits of mobile edge computation (MEC) with the support of advanced communication technologies. In general, for the fog computation in intelligent transport systems, the static scheduling scheme is usually adopted, where the incoming tasks are allocated to their destinations with a fixed probability, namely "Static Scheduling" [39]. In addition, to improve the scheduling flexibility, dynamic scheduling schemes are adopted that can adaptively alter scheduling process based on the varying queue length [40]. For example, when a server is longer than other servers, the new incoming arrivals will be scheduled to other servers with relatively shorter queues. In the proposed algorithm, a probabilistic function $P_{L t}$ is defined in the dynamic scheduling mechanism, and it represents the probability of sending a job $j$ to server $s$. The birth of MEC has contributed to wide improvement on the vehicle-environment control. More traffic status data shared from the volunteered vehicles on route segments, such as global position system (GPS) coordinates, vehicle speeds, distances to forward vehicles and travel destination, can be collected and processed by MECUs, thereby integrating more environmental information into vehicle control. With the benefits from the powerful computation capability in MECUs and limited supervision scope, the processing ability in MECUs can be remarkably prompted.

The vehicle controller includes two parts, which is denoted as powertrain control unit (PCU) in Fig. 2 (a). The master level control units are located in the MECUs, mainly responsible for sensing, collecting and processing the predominant traffic information. The reference optimal control schemes can be generated in PCU-Part 1. In PCUPart 2, the high-level control unit optimally decides the powertrain operation modes and allocates the energy distribution in powertrain by tracking the reference control scheme sent from PCU-Part 1. Then, the control decisions from PCU will be executed finally. The PCU-Part 1, as a matter of fact, mainly deals with the macroscopically long-term control process, while PCU-Part 2 takes charge of the microcosmically shortterm management. The synergetic work in the asynchronous controller refines the control effect. To validate the performance of raised control framework, some comparable evaluation is made in the
following section.

### 3.2. Evaluation on the novel MEC based control framework

We consider a MEC-based internet of vehicle (IoV) system, as shown in Fig. 2 (b), where the MECU is mounted at the base station (BS) and owns enough computational capability. We assume that the computing capacity of MEC server as $F$ Giga CPU cycles/s, and the number of antennas at the BS as $N$. Moreover, we suppose the cooperative collision avoidance (CCA) [41] communication protocol is adopted, which is an emerging vehicular safety application using IEEE- and ASTM-adopted dedicated short-range communication (DSRC) standard. The vehicle is equipped with a single antenna. On this basis, the MEC-based time frame can be expressed in Fig. 2 (c).

For the channel estimation, the vehicle needs to transmit a small number of pilot signals to BS, and then BS estimates the channel. Subsequently, the vehicle offloads the input data to BS, and the MEC server performs calculations. Finally, BS sends back the computing results (controlling information) to the vehicle. Since the transmitted data both at the channel estimation and return control information phases are very small, the transmission time is extremely short and can be ignored. Here, we only consider the offloading and computing time.

We assume that the perfect channel estimation can be obtained at BS by the advanced channel estimation algorithm. The received signal by BS can be expressed as:
$y=\operatorname{vh} \sqrt{p} x+n$
where $\mathrm{h} \in \mathbb{C}^{N+1}$ denotes the channel coefficient between BS and the vehicle, $\mathrm{v} \in \mathbb{C}^{N+1}$ is the detection vector at the BS, $p$ and $x$ are the transmitted power and signal by the vehicle with $E\left(\left|x\right|^{2}\right)=1$, respectively. $N$ expresses the independent and identically distributed additive white Gaussian noise with zero mean value, i.e., $\mathbb{C} N\left(0, \delta^{2}\right)$. Then, the rate can be written as:
$R=B \log _{2}\left(1+\frac{\operatorname{vh}^{2} p}{\delta^{2}}\right)$
where $B$ is the transmission bandwidth. Generally, BS can adopt the maximal-ratio combiner (MRC) technique, and thusv $=\mathrm{h}^{\mathrm{T}} /\|\mathrm{h}\| \mid$. On this basis, the transmit rate can be rewritten as:
$R=B \log _{2}\left(1+\frac{\left|\mathrm{h}^{\mathrm{H}} \mathrm{h}\right|^{2} p}{\|\mathrm{~h}\| \delta^{2}}\right)$
And the transmission delay can be calculated as
$T_{3}=\frac{C}{R}$
where $C$ denotes the input data from the vehicle to BS. Additionally, we assume $W$ as the number of the required computation, and the computing time can be expressed as:
$T_{3}=\frac{W}{F}$
Finally, the total delay can be expressed as $T=T_{2}+T_{3}$. To minimize the delay, we formulate the following optimization problem:
Maximize: $T_{2}+T_{3}$. Subject to: $p \leq p_{\max }$
where $\mathrm{p}_{\max }$ denotes the maximum transmit power of vehicle. The above optimization problem can be directly solved by setting the maximum transmit rate. We set the following simulation parameters to calculate the delay. As a comparison, we assume that the computing capacity at the vehicle is 10 or 20 Giga CPU cycles/s. $B=10 \mathrm{MHz}, \delta^{2}=-144 \mathrm{dBm}$, the distance between the vehicle and BS is 20 m , the antennas number is $N=8$, and the computing capacity at the MEC server is $F=50$ Giga CPU

![img-2.jpeg](img-2.jpeg)

Fig. 3. Illustration on results by EDA. (a) The implementation process of EDA. (b) Calculation results by EDA. (c) Battery SOC decreasing slopes by EDA.
cycles/s. The data length is $C=0.1$ Mbits, and computing number $W=$ 0.1 Giga CPU cycles.

From Fig. 2 (d), we find that the delay is lower than 4 ms when the edge computing is performed. Meanwhile, the delay decreases with the increment of transmit power of the vehicle. In addition, from Fig. 2 (e), one can observe that the transmit rate can reach $5.6 \times 10^{8} \mathrm{bit} / \mathrm{s}$ when the transmit power of vehicle is 20 dBm , which is enough to guarantee the data transmission.

## 4. Cooperative power sources management strategy

### 4.1. Two-step cooperative control strategy for cPHEVs

As shown in Fig. 2 (f), a two-stage process is imperative to realize the energy management in the proposed cooperative control strategy for cPHEVs. According to the shared traffic information, the future velocity profile in each segment will be predicted by the method that was proposed in our former work [42]. Based on the forecasted velocity profile, the reference battery SOC trajectory in each route segment will be globally calculated in the master level control unit installed in the MECU. The generated battery SOC trajectories and predicted velocity profiles in different route segments will be sent to the high-level control unit installed in the vehicle. The tracking algorithm in the high level
control unit can regulate the energy flow between the engine and battery according to the optimal SOC trajectories and velocity profiles.

In this study, EDA is employed to generate the reference SOC trajectories in master level control units, and MPC is in charge of tracking the reference control policies in high level control unit. The velocity profile in each route segment is predicted with the full consideration of traffic macroscopic behaviours and security. It is worth pointing out that the reference control policies should be generated in each route segment for reducing the computation burden. However, the narrowed scope in global optimization will deteriorate the optimization effect, given that the terminal states of former route segment will be sent to the MECU that is responsible for the latter route segment. This means that the planned reference control policies in each route segment cannot delegate the optimal solutions to ensure the global optimal fuel economy in the whole trip. To bridge the gap when applying global optimization in route segment and in whole trip, active adjustment in energy consumption in each route segment is indispensable to improve the performance of raised cooperative control strategy. The detailed method for active adjustment of planning reasonable energy consumption will be introduced in the following section.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Illustration on the raised strategy. (a) Process to plan terminal battery SOC. (b) Velocity profiles for generating training data. (c) Generated slope data by IDP.

### 4.2. Fundamental energy consumption plan

The energy consumption in each route segment is fundamentally planned by EDA, which is one of the validated evolution algorithms in parameter estimation and global optimal control [43,44]. By virtue of the probabilistic models, priori information in terms of problem structure is integrated into the optimizing process, contributing to generation of the ideal performance of EDA [45]. EDA tries to obtain the solution by evaluating the general performance in each iteration, rather than digging out the personally optimum in each iteration from the perspective of individual performance solved by GA or PSO. In addition, the unknown information of optimization space can be detected by the probabilistic model, so as to increase the probability of obtaining the optimal solutions [46]. The execution process of EDA is shown in Fig. 3 (a).

In the implementation process of EDA, the fitness value function of evaluating the macroscopic performance can be expressed as:
$F_{c}=\int \omega_{i}\left(x_{k}, u_{k}\right)+\omega_{i} \frac{P_{\text {turi }}}{Q_{\text {inc }}} d_{i}$,
where $\omega_{k}$ is the weight on electric energy consumption. The inequality constraints can be expressed as:

$$
\left\{\begin{array}{l}
S O C_{\min } \leq S O C \leq S O C_{\max } \\
P_{\text {turi, } \min } \leq P_{\text {turi }} \leq P_{\text {turi, max }} \\
T_{\text {con, } \min } \leq T_{\text {con }} \leq T_{\text {con, max }} \\
T_{\text {req, } \min } \leq T_{\text {req }} \leq T_{\text {req, max }} \\
\omega_{\text {con, } \min } \leq \omega_{\text {con }} \leq \omega_{\text {con, max }} \\
\omega_{\text {req, } \min } \leq \omega_{\text {req }} \leq \omega_{\text {req, max }}
\end{array}\right.
$$

where the subscripts min and max denotes the minimum and maximum value of each variable, respectively. The optimization control by EDA is performed in distance domain for better satisfying the local constraints. In the distance domain calculation, velocity at next location can be described as:
$v(k+1)=v(k)+\bar{v}(k) \frac{2 \Delta s}{v(k)+v(k+1)}$
where $\Delta s$ is the calculation step in distance, and $k$ and $k+1$ denote the location at current and next step. The probabilistic model in EDA is the Gaussian network model [47], and each continuous variable $X_{i} \in X$ in the local density function can be written as:
$f\left(x_{i} \mid p a_{i}^{\prime}, \theta_{i}\right) \equiv N\left(x_{i} ; m_{i}+\sum_{x_{i} \in m_{i}} b_{i j}\left(x_{i}-m_{j}\right), \frac{1}{v_{i}}\right)$
where $N\left(x ; \mu, \sigma^{2}\right)$ is the univariate normal distribution with mean value $\mu$ and variance $\sigma^{2} ; b_{i}$ is the local parameter which includes $m_{i}, b_{i}$ and $v_{i} . m_{i}$ denotes the unconditional mean of $X_{i} ; b_{i}$ is a column vector; $v_{i}$ is the conditional variance of $X_{i}$ under assigned $p a_{i}^{\prime}$; and $b_{i j}$ is the linear coefficient reflecting the dependence between $X_{i}$ and $X_{i}$. The adopted sampling and learning methods in EDA are the univariate Gaussian model based method and greedy score method, respectively [48,49].

To fast complete the optimization process in EDA with preferable performance, it is recommended that the iteration and population number should be carefully determined by trail-and-error. Given the WLTC driving cycle [50], the computation intensity, terminal battery SOC deviation, and fuel consumption by EDA with different populations and iterations are compared, and the results are presented in Fig. 3 (b). As can be observed, it looks closer to the set terminal SOC constraint with larger population and iteration. Likewise, the fuel consumption will be certainly lower. However, the increase of population and iteration will incur more computation labor, which is not applicable in real-time implementation. By comprehensively trading off accuracy, optimization effect, and computation burden, the number of iteration and population are set to 800 and 200, respectively.

### 4.3. Active adjustment in energy management plan

As requested, some active adjustment should be performed to narrow the distance between applying global optimization in route segment and in the whole trip. The difference is attributed to the running global optimization in route segment without chance of previewing the driving conditions in the whole trip. This may lead to the local optimal in each route segment rather than global optimum. Furthermore, the global optimization integrally considers the effect of driving condition variation in each route segment, imposed on the total fuel economy, by intelligently governing more electric energy to be consumed in some route segments. Consequently, the performance of applying global optimization in route segment might be much closer to that by running global optimization in the whole trip through certain adjustment according to different driving conditions. To be specific, in the conditions of favoring the EV and HAD mode, more electric energy consumption will be encouraged. The HDC mode should be the prior choice in the conditions of enlarge the engine power to charge the battery.

Fig. 3 (c) illustrates the SOC declining slopes by the EDA under different driving conditions with different initial SOC values. Clearly, the difference in declining slopes reveals diverse electric energy consumption level under different driving conditions. After carefully analyzing the interrelation between the SOC declining slope and driving conditions, an adjustment function could be derived, as:
$S O C_{s c c}=T_{f} k_{c o s} s+S O C_{i n t}$
where $S O C_{\text {opt }}$ and $S O C_{\text {int }}$ denotes the initial and terminal SOC value in each route segment, respectively; $k_{\text {opt }}$ is originally battery SOC declining slope acquired from offline calculation; and $T_{f}$ is the traffic factor which can be expressed as:
$T_{f}=\frac{v_{\text {opt }}}{v_{\text {inf }}}$
where $v_{\text {opt }}$ is the average speed in a certain route segment, and $v_{\text {inf }}$ is the velocity standard deviation. $v_{\text {opt }}$ and $v_{\text {inf }}$ can be calculated according to the predicted velocity profile in each route segment. According to (17), the terminal SOC is actively adjusted in terms of the traffic conditions, thereby subjectively regulating the electric energy consumption in each route segment. $k_{\text {opt }}$, as described, is acquired through the offline calculation. The conventional manner of enabling $k_{\text {opt }}$ in real time is to generate look-up tables and program them into the controller. Despite the simple implementation process shown in (17), the method may occupy much memory with different initial SOC values. As such, an efficient method is preferred in this paper, of which the process is illustrated in Fig. 4 (a). As can be found, $k_{\text {opt }}$ will be the output directly derived from a pre-trained NN with the premise of acquiring the initial battery SOC and the estimated electric energy consumption. The latter can be calculated by:
$E_{v, k_{\text {sOC }}}=\int P_{r e q}(v(s))-\eta_{c} P_{r e q, \text { opt }}(v(s)) d_{i}$
where $P_{\text {eng, opt }}$ denotes the engine power corresponding to the optimal operation points in the best fuel rate line with the deterministic velocity, $s$ is the simulation step in distance domain. According to $k_{\text {opt }}, T_{f}$ and adjusted terminal SOC could be calculated by (17) and (18).

In this study, a three-layer BP-NN is adopted. The discussion in Ref. [51] justified that a three-layer BP-NN with a Sigmoid function based hidden layer can infinitely approximate to any nonlinear correlation. The Sigmoid function describes the interaction between the nodes in the hidden layer and output layer. In the preferred BP-NN, the number of nodes in input layer, hidden layer, and output layer are set to $n_{i} l_{i}$ and $m_{i}$ respectively. The output of the input layer, hidden layer, and output layer are expressed by $x_{i}(p) \quad(i=1,2, \ldots, n)_{i} y_{i}(p) \quad(i=1,2, \ldots, l)$ and $o_{i}(p) \quad(i=1,2, \ldots, m)$, respectively. The weights in the input and hidden layer and in between are $\omega_{i j} \quad(j=1,2, \ldots, l)$ and $v_{k j} \quad(k=1,2, \ldots$,

![img-4.jpeg](img-4.jpeg)

Fig. 5. General analysis results in energy consumption plan. (a) Predicted velocity profile in two travel routes. (b) Energy consumption comparison by different methods. (c) Engine torque by different methods in whole travel route. (d) Motor torque by different methods in whole travel route.
$m$ ); and the threshold values of hidden and output layer are $\theta_{f}$ and $\phi_{k}$. The training process of the three-layer BP-NN are described as follows:

Step 1: Initialize the number of nodes in the input layer, hidden layer, and output layer; their corresponding weights as well as the threshold values of hidden and output layer.
Step 2: Input the training data to proceed the forward propagation, and obtain the output from the nodes in output layer, as:

$$
\left\{\begin{array}{l}
u_{j}=\sum_{i} v_{k i} y_{j}+\phi_{k} \\
y_{j}=f\left(u_{j}\right) \\
x_{k}=\sum_{j} v_{k j} y_{j}+\theta_{j} \\
o_{i}=f\left(x_{k}\right)
\end{array}\right.
$$

Step 3: Calculate the error $\psi_{i}$ between the output $o_{i}$ of the forward propagation and real output $t_{i}$ of the trained data, as:
$\psi_{i}=\left(o_{i}-t_{i}\right) t_{i}\left(1-o_{i}\right)$

Step 4: Proceed the backward propagation with $\psi_{i}$, and calculated the error signal $\sigma_{f}$ caused by nodes in the hidden layer, as:
$\sigma_{i}=\left(\sum_{k} \psi_{i} v_{k i}\right) y_{i}\left(1-y_{i}\right)$

Step 5: Adjust the weight and threshold values by:

$$
\left\{\begin{array}{l}
v_{k i}^{\prime}=v_{k j}+\tau \psi_{i} y_{j} \\
\omega_{j i}^{\prime}=\omega_{j i}+\tau \psi_{i} x_{i} \\
\theta_{j}^{\prime}=\theta_{j}+\tau \psi_{j} \\
\phi_{k}^{\prime}=\phi_{k}+\tau \psi_{k}
\end{array}\right.
$$

where ris the learning rate.
Step 6: Repeat steps 1 to 6 and calculate the mean square error between the output of the BP-NN and real value by:
$E=\frac{1}{2 N} \sum_{k=1}^{N} \sum_{k=1}^{N}\left(o_{k}-t_{k}\right)^{2}$
The training process will be repeated untilEis lower than the pre-set value. The data for training the specific BP-NN is prepared offline by IDP [52] based on the collected driving cycle data. The length of each driving cycle, gathered in real route segment with different driving conditions, is 1500 m . The velocity profiles of partial chosen driving cycles are shown in Fig. 4(b). The IDP algorithm, as a numerical method, can save the calculation time while attain the quasi-optimal effect, compared with the optimal solutions provided by the deterministic DP

Table 2
Experimental setup.

| Experimental Setup | Detailed Information/Values |
| :-- | :-- |
| Operation platform | Matlab/Simulink |
| Operation hardware | Workstation with Intel Xeon E3-1270@ 3.4 GHz with |
|  | 32 Gb memory |
| Population in EDA | 200 |
| algorithm |  |
| Iteration in EDA | 800 |
| algorithm |  |
| Sample step in EDA | 10 m |
| algorithm |  |
| Prediction length in MPC | 10 m |
| Sample step in MPC | 2 m |
| Vehicle Mass | 1700 kg |
| Rolling resistance ratio | 0.0015 |
| Aero dynamic drag ratio | 0.31 |
| Vehicle frontal area | 2 m $^{2}$ |

(DDP) with smaller amount of state and control variables. In each iteration, the grid size of state and control variable will be adjusted to endeavour the lowest request on processor memory [45]. To constrain the electric energy, the stage cost function in IDP to calculate the cost-to-go values of each discrete state can be expressed as:
$h_{1}=\dot{m}_{l}\left(x_{k}, u_{1}\right)+\omega_{1} \frac{P_{t o s}}{Q_{h v}}$
where $\omega_{1}$ denotes the weight on electric energy consumption, and can be calculated as:

$$
\begin{aligned}
& \omega_{1} q+1\left(=\omega_{1} q\right)+\operatorname{sign} E_{c_{-} \text {rest }} q\left(-E_{c_{-} \text {target }} q\right)\left(\times \delta E_{c_{-} \text {rest }} q\right) \\
& \quad-E_{c_{-} \text {target }}(q))^{\frac{1}{2}}
\end{aligned}
$$

where $q$ is the iteration time, $E_{c_{-} \text {rest }}$ is the real electric energy consumption in qth iteration, $E_{c_{-} \text {target }}$ is the target electric energy consumption, and $\delta$ is a constant parameter. In each iteration, $\omega_{1}$ is recalculated according to the attained electric energy consumption, trying to approximate the target value. In the IDP based optimization, the inequality constraints are the same with that in EDA optimization. The offline generated battery SOC decreasing slopes, based on the velocity profiles displayed in Fig. 4 (b), is demonstrated in Fig. 4 (c).

## 5. Simulation and evaluation

In this study, we perform a comprehensive evaluation for the proposed cooperative strategy based on the novel asynchronous control framework. The performance in active energy consumption plan by the raised strategy is emphatically analyzed. The general behaviors of the adaptive energy management are also discussed based on the MPC algorithm. All the simulation was executed on a workstation with an Intel Xeon E3-1270 @ 3.4 GHz with 32-Gigabyte memory. Two driving routes are chosen with the total length of 4.5 km . Each MECU is responsible for the workload within 1.5 km . The selected driving routes stem from the urban center, of which the complex driving conditions are well suited for the validation of the MEC based cooperative control strategy. The real velocity profiles of the two driving routes are sketched in Fig. 5 (a), along with the predicted velocity. The predicted velocity profiles show high accuracy in contrast with the real driving data. The difference between the predicted velocity profiles and real driving data is caused by the data deficiency in some route segments. With respect to the simulation results, the EDA-W refers to the application of EDA on the whole route. The EDA-Seg indicates application of EDA in each route segment without any energy consumption adjustment. The AEDA-Seg represents applying EDA in each route segment with the corresponding active adjustment. The calculation step in the EDA based

Table 3
Energy consumption in whole trips by different EDA methods.

| Trip | Control <br> Strategy | Fuel Consumption |  | Electric Energy Consumption <br> (kWh) |
| :--: | :--: | :--: | :--: | :--: |
|  |  | (g) | (L/100 <br> km ) |  |
| 1 | EDA-W | 72.88 | 2.23 | 1.39 |
|  | EDA-Seg | 102.36 | 3.14 | 1.24 |
|  | AEDA-Seg | 93.47 | 2.87 | 1.26 |
| 2 | EDA-W | 78.09 | 2.39 | 1.34 |
|  | EDA-Seg | 112.05 | 3.43 | 1.16 |
|  | AEDA-Seg | 80.51 | 2.46 | 1.31 |

Table 4
Energy consumption in whole trips by different strategies.

| Trip | Control <br> Strategy | Fuel Consumption |  | Electric Energy Consumption <br> (kWh) |
| :--: | :--: | :--: | :--: | :--: |
|  |  | (g) | (L/100 <br> km ) |  |
| 1 | EDA-W | 72.88 | 2.23 | 1.39 |
|  | DP | 72.19 | 2.22 | 1.40 |
|  | IDP | 95.21 | 2.91 | 1.24 |
|  | AEDA-Seg | 93.47 | 2.87 | 1.26 |
| 2 | EDA-W | 78.09 | 2.39 | 1.34 |
|  | DP | 77.43 | 2.37 | 1.35 |
|  | IDP | 82.12 | 2.51 | 1.29 |
|  | AEDA-Seg | 80.51 | 2.46 | 1.31 |

optimization process in MEC-Us is 10 m . The details of the experimental setup information are listed in Table 2.

### 5.1. General analysis on the raised control strategies in energy consumption plan

Fig. 5 (b) and Table 3 compare the results in energy consumption according to different strategies when planning the energy consumption for the whole trip. The visual results shown in Fig. 5 (b) and the detailed statistical indexes in energy consumption roughly justify the reasonable performance of proposed method. The active adjustment in energy consumption plan contributes to the approximate optimal fuel economy, compared with that gained by EDA in whole trip, thus narrowing the performance gap of the two algorithms. Compared with the results based on EDA-Seg, the fuel consumption in two driving cycles is saved by up to $28.3 \%$. The fuel consumption by AEDA-Seg in two driving cycles has reached $97.2 \%$ savings of EDA-W. The electric energy consumption by AEDA-Seg, comparing with that by EDA-Seg, is closer to that by EDA-W. From the engine and motor operation results shown in Fig. 5 (c) and (d), the percentage of different operation modes, including the EV, HAD, and HDC mode, are quite approaching between EDA-W and AEDA-Seg, revealing that the traffic-information-based active adjustment in energy consumption plan prompts the fuel economy with the resemble manners from EDA-W. To further evaluate the general performance of the raised method, we also compare the energy consumption by the raised method with other methods including DP, IDP and EDA-W. IDP is an adaptive managing method that can adjust the energy allocation considering given constraints [53]. IDP has been applied in our previous work to narrow the distance between the global optimization within whole trip in each route segment [53]. According to the numerical results listed in Table 4, the raised method in this paper outperforms the IDP in adjusting energy consumption in each route segment and achieves the near-optimal energy consumption that is close to that by EDA-W and DP. Compared with the IDP, the fuel consumption by AEDA-Seg is reduced by up to $1.99 \%$ in two driving cycles shown in Fig. 5 (a), and it is a remarkable improvement, compared with our previous work. The fuel consumption by the AEDA-Seg in two driving conditions reaches $96.2 \%$ savings of DP. The electric energy

Table 5
Computation time in whole trips by different strategies.

| Driving <br> Cycle | Control <br> Strategy | Travel <br> Distance (m) | Travel <br> Time (s) | Computation <br> Time (s) |
| :-- | :-- | :-- | :-- | :-- |
| 1 | EDA-W | 4500 | 473 | 447.13 |
|  | EDA-Seg | 4500 | 473 | 396.45 |
|  | AEDA-Seg | 4500 | 473 | 399.69 |
| 2 | EDA-W | 4500 | 654 | 431.49 |
|  | EDA-Seg | 4500 | 654 | 382.46 |
|  | AEDA-Seg | 4500 | 654 | 383.67 |

consumption by the AEDA-Seg is also closer to that by DP when compared with the EDA-Seg. The further evaluation on several existing methods manifests the enhanced performance of the raised AEDA-Seg method.

In addition to the general evaluation on the energy consumption resulted from different methods, the complexity analysis of algorithms is also performed, which is reflected by computation duration of algorithms listed in Table 5. It is necessary to note that the results in Table 4 are the total computation time in whole trips, and results by EDA-Seg and AEDA-Seg are the sum of computation duration in all the route segments. Besides, the travel times are calculated based on the predicted velocity profiles shown in Fig. 5 (a). According to the results in Table 4, all EDA methods can accomplish the computation within travel time,
![img-5.jpeg](img-5.jpeg)

Fig. 6. Analysis results of further evaluation. (a) Battery SOC trajectories planned by different methods. (b) Engine torque comparison by different strategies. (c) Motor torque comparison by different strategies. (d) The engine operation points by different methods. (e) The engine operation points by different methods. (f) Engine and motor power probability distribution.

Table 6
Energy consumption in each segment by different strategies.

| Drive <br> Cycle | Control <br> Strategy | Route <br> Segment | Traffic <br> Factor <br> Value | Fuel <br> Consumption <br> (g) | Electric Energy <br> Consumption <br> (kWh) |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | EDA-Seg | R1 | 1.223 | 48.56 | 0.48 |
|  |  | R2 | 0.955 | 23.84 | 0.42 |
|  |  | R3 | 0.989 | 29.96 | 0.34 |
|  | AEDA- | R1 | 1.223 | 36.53 | 0.53 |
|  | Seg | R2 | 0.955 | 27.91 | 0.41 |
|  |  | R3 | 0.989 | 29.03 | 0.32 |
| 2 | EDA-Seg | R1 | 1.031 | 34.87 | 0.35 |
|  |  | R2 | 0.931 | 35.44 | 0.32 |
|  |  | R3 | 1.226 | 41.74 | 0.49 |
|  | AEDA- | R1 | 1.031 | 25.72 | 0.41 |
|  | Seg | R2 | 0.931 | 38.16 | 0.29 |
|  |  | R3 | 1.226 | 16.63 | 0.61 |

proving reasonable capability in real-time application. The EDA-Seg and AEDA-Seg narrow the optimization scopes with route segments, reducing computation time and pressure on hardware. With the existing adjustment in AEDA-Seg, the computation times are slightly longer than those by EDA-Seg in two trips.

### 5.2. Further evaluation on the simulation results

To understand the manner in performance improvement by the proposed method, more analysis is conducted. As can be seen in Fig. 6 (a), there are three arresting change caused by the active adjustment of energy consuming manners in each driving cycles, labelled as AD1s, AD2s, and AD3s, respectively. The active adjustments, generally, are triggered in three different route segments of the two travel routes. By the raised method, the battery SOC declining slopes become actively smaller (labelled as AD1), compared with those by EDA-Seg, thereby leading to more electric energy consumption (listed in Table 6) in the first route segment of the two driving cycles. In the first route segments of two routes, the traffic conditions contribute to electric energy consumption with larger traffic factor values (shown in Table 6), thus regulating the terminal battery SOC lower consequently. Under the adjusted terminal constraints, the EDA encourages the HDC mode at the beginning of the two trips essentially. The ICE and motor, respectively shown in Fig. 6 (b) and (c), are coordinately governed to operate more in the HDC mode, compared with that by EDA-Seg, resulting in the initial increase of battery SOC. With the initially higher SOC and lower constraints on the terminal battery SOC, the battery SOC decreasing slopes can be therefore reduced further.

In the second route segment of the first driving cycle, the traffic condition seems to be modest, also shown in Fig. 6 (a). However, some minor adjustment in terminal constraints is offered. The ending SOC is tuned to a slight smaller value, causing initial SOCs are lifted somewhat by urging more HDC mode compared with that by EDA-Seg. The marked results (AD2s) depicted in Fig. 6 (b) and (c) manifest that more appearance of the HDC mode is required by AEDA-Seg than by EDA-Seg. In the second route segment of the second driving cycle, the battery SOC decreasing rate is adjusted even though the terminal constraints on the battery SOC are almost the same. This active adjustment is dominated by the tuned terminal battery SOC in the first route segment of the second driving route. After transferring the terminal constraint from the first MECU to the second as the initial constraint for optimization in the second route segment, the EDA increases the battery SOC to reach the preset terminal constraining target by selecting more HDC modes. In the third route segment of the first driving cycle, active adjustment is made in the similar manner as that in the second route segment. In the third route segment of the second driving cycle, the terminal battery SOC is pared down obviously according to the specific traffic conditions, facilitating more electric energy to be consumed by choosing more EV

Table 7
Energy consumption in various driving conditions by different strategies.

| Drive Cycle | Control <br> Strategy | Fuel Consumption <br> $(\mathrm{g})$ | Electric Energy <br> Consumption $(\mathrm{kWh})$ |
| :-- | :-- | :-- | :-- |
| City Urban | EDA-W | 23.69 | 0.78 |
|  | EDA-Seg | 35.43 | 0.64 |
|  | AEDA-Seg | 24.31 | 0.73 |
| City | EDA-W | 31.61 | 0.59 |
| Suburban | EDA-Seg | 41.87 | 0.49 |
|  | AEDA-Seg | 32.72 | 0.57 |
| Highway | EDA-W | 49.04 | 0.27 |
|  | EDA-Seg | 55.43 | 0.25 |
|  | AEDA-Seg | 49.72 | 0.28 |

and HDA modes. The marked AD3s in Fig. 6 (b) and (c) validate that more favorable EV and HDA modes are preferred in the third route segment of the second route. Table 6 lists the detailed comparison in energy consumption solved by EDA-Seg and AEDA-Seg. As can be found, less fuel consumption and more electric energy utilization are reached by AEDA-Seg with larger traffic factor values. On the basis of detailed comparison between AEDA-Seg and EDA-Seg, it can be adequately summarized that the proposed AEDA-Seg achieves more similar performance to EDA-W. The active energy adjustment adapted to variation of traffic information offers flexible terminal conditions for EDA based solution, thus effectively narrowing the difference with that by EDA-W.

To further investigate the superiority of proposed algorithm, more evaluation is performed with detailed results illustrated in Fig. 6 (d)-(f). Fig. 6 (d) and (e) show the operation points of engine and motor by different methods. With the adaptive adjustment, engine operation points by AEDA-Seg locate intensively in the fields with larger power that are similar with those by EDA-W, contributing to better fuel economy. On the contrary, EDA-Seg leads to more disperse engine operation in lower power fields, deteriorating the fuel economy. The similar performances also appear in motor operation points distribution. Adaptive adjustment in AEDA-Seg, compared with no adjustment in EDA-Seg, brings operation points into concentrated field with higher efficiencies in both tractive and braking mode, improving total efficiencies of powertrain.

Fig. 6 (f) compares the engine and motor power distribution probability by different methods in each route segment of route 2. The power distribution probability can reveal the operation trends of powertrain that are determined by strategies. As shown in Fig. 6 (a), the adjustment by AEDA-Seg requests more engine power to charge battery in the beginning and more electric energy to accelerate the battery SOC decline frequency. Therefore, the engine powers locating in large value sections by AEDA-Seg are more than those by EDA-Seg. In addition, smaller negative motor power demanded by AEDA-Seg becomes more frequent to charge the battery in the beginning. In other parts of route segments, larger positive motor powers are preferred by AEDA-Seg to fasten the consumption of electricity.

To justify the robustness of the raised method to different scenarios, we compare the energy consumption by the EDA-W, EDA-Seg, and AEDA-Seg in different driving conditions. Three driving cycles, corresponding to city urban, city suburban and highway conditions, are extracted from the open available database [54]. The length of the chosen cycles is also around 1500 m . Generally, the energy consumption listed in Table 7 reveals that the fuel consumption is undoubtedly consumed more in highway than in city urban condition as highway condition entails more engine operation. On the contrary, the city urban condition turns to request more electric energy. Among these three methods, the proposed AEDA-Seg can adjust energy consumption within each route segment in each driving cycle, enabling that total performance is close to that by the global EDA-W. The compare results highlight that the raised AEDA-Seg can reduce the energy consumption with fast calculation speed in different driving conditions and certain

![img-6.jpeg](img-6.jpeg)

Fig. 7. Components performance by MPC. (a) Battery SOC trajectory tracking results. (b) Components performance by MPC.
robustness.

### 5.3. General evaluation on adaptive energy management

In the simulation evaluation, we also conducted some simulation test for the adaptive energy management realized by MPC. In the context, the nonlinear MPC based instantaneous optimization method is still in a distance domain. Different from the optimization process in MECUs, the calculation step in the nonlinear MPC is reduced to 2 m and the horizon length for the receding optimization is set to 10 m . In addition to following the reference battery SOC trajectories, the MPC algorithm in the on-board controllers are also requested to track the predicted velocity profiles acquired from MECU to safely satisfy the traffic conditions. The optimization target of control algorithm is the fuel economy, and as such, the energy consumption optimization is presented and compared. In Fig. 7 (a), it is clear that the MPC algorithm can track the reference battery SOC trajectories tightly in most of the time, guaranteeing that the optimal control policies generated in MECUs as the reference can be precisely explained by the vehicle powertrain. As can be seen in Fig. 7 (b), the ignorable difference existing in the engine and motor torque, is caused by the errors incurred in the nonlinear solving process.

## 6. Conclusion

This paper proposes a novel control framework for the connected plug-in hybrid electric vehicles. The novel control framework based on the mobile edge computation, well balances the computation burden in each control unit of the vehicle controller. With the novel control framework, the original on-board controllers are extended to the hierarchically asynchronous controller with enhanced capability supplied by cloud computation. The raised cooperative control strategy can dramatically govern the energy flow within powertrains by active energy adjustment and adaptive management. The active energy adjustment method is particularly and widely investigated. The estimation of distribution algorithm with active adjustment on terminal constraints achieves the optimal energy consumption plan in narrowed scope.

In the future work, communication optimization for the built framework will be further investigated carefully for realization of fast, inexpensive and zero-lag communication. Additionally, fast global optimization method will also be explored to achieve better performance in real-time application.

## CRediT authorship contribution statement

Yuanjian Zhang: Conceptualization, Investigation. Chong Guo:

Investigation. Yonggang Liu: Writing - review \& editing. Fei Ding: Writing - review \& editing. Zheng Chen: Supervision, Methodology, Writing - review \& editing. Wanming Hao: Supervision, Investigation, Writing - review \& editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgement

This work was supported in part by the National Natural Science Foundation of China (No. 61763021 and No. 51775063), in part by the National Key R\&D Program of China (No. 2018YF80104900), and in part by the EU-funded Marie Skłodowska-Curie Individual Fellowships Project under Grant 845102-HOEMEV-H2020-MSCA-IF-2018.

## References

[1] J. Gao, et al., 'Fuel consumption and exhaust emissions of diesel vehicles in worldwide harmonized light vehicles test cycles and their sensitivities to exo-driving factors, Energy Convers. Manag. 196 (2019) 9.
[2] Soumeur, Mohammed Amine, et al., Comparative study of energy management strategies for hybrid proton exchange membrane fuel cell four wheel drive electric vehicle, J. Power Sources 462 (2020) 228167.
[3] P.K. Gujarathi, V.A. Shah, M.M. Lokhande, Grey wolf algorithm for multidimensional engine optimization of converted plug-in hybrid electric vehicle, Transport. Res. Transport Environ. 63 (2018) 632-648.
[4] Likang Fan, et al., Design of an integrated energy management strategy for a plug-in hybrid electric bus, J. Power Sources 446 (2020) 227391.
[5] F. Wang, J. Zhang, X. Xu, Y.F. Cai, Z.G. Zhou, X.Q. Sun, A comprehensive dynamic efficiency-enhanced energy management strategy for plug-in hybrid electric vehicles, Appl. Energy 247 (Aug 1 2019) 657-669 (in English).
[6] Shaobo Xie, et al., Aging-aware co-optimization of battery size, depth of discharge, and energy management for plug-in hybrid electric vehicles, J. Power Sources 450 (2020) 227638.
[7] Y. Huang, et al., A review of power management strategies and component sizing methods for hybrid vehicles 96 (2018) 132-144. Renewable and Sustainable Energy Reviews.
[8] M.F. Mohd Safei, K.A. Danapalasingam, M. F. a Rahmat, Improved fuel economy of through-the-road hybrid electric vehicle with fuzzy logic-based energy management strategy, International Journal of Fuzzy Systems, vol. 20, no 8 (2018) 2677-2692.
[9] S. Moura, HW 5: optimal PHEV energy management via dynamic programming, University of California, Berkeley (2018).
[10] F. Zhang, X. Hu, R. Langari, D. Cao, Energy management strategies of connected HEVs and PHEVs: recent progress and outlook, Prog. Energy Combust. Sci. 73 (2019) 235-256.
[11] C. Song, et al., A power management strategy for parallel PHEV using deep Qnetworks.pdf, in: IEEE Vehicle Power and Propulsion Conference (VPPC), 2018.

[12] T. Liu, X. Hu, W. Hu, Y. Zou, A heuristic planning reinforcement learning-based energy management for power-split plug-in hybrid electric vehicles, IEEE Transactions on Industrial Informatics 15 (12) (2019) 6436-6445.
[13] E. Taberzadeh, M. Dabbaghjamaneeb, M. Gützadeh, A. Rahideh, A new efficient fuel optimization in blended charge depletion/charge sustenance control strategy for plug-in hybrid electric vehicles, IEEE Transactions on Intelligent Vehicles 3 (3) (2018) 374-383.
[14] Q. Xu, X. Luo, X. Jiang, M. Zhao, Research on double fuzzy control strategy for parallel hybrid electric vehicle based on GA and DP optimization, IET Electr. Syst. Transp. 8 (2) (2018) 144-151.
[15] Y. Zeng, Parameter optimization of plug-in hybrid electric vehicle based on quantum genetic algorithm, Cluster Comput. 22 (6) (2019) 14835-14843.
[16] S.-T. Chen, C.-H. Wu, Y.-H. Hung, C.-T. Chung, Optimal strategies of energy management integrated with transmission control for a hybrid electric vehicle using dynamic particle swarm optimization, Energy 160 (2018) 154-170.
[17] N. Ruma, H. Wang, J. Orlando, D. Robinette, B. Chen, Route-Optimized Energy Management of Connected and Automated Multi-Mode Plug-In Hybrid Electric Vehicle Using Dynamic Programming, 2019. SAE Technical Paper0148-7191.
[18] S. Xie, X. Hu, Z. Xin, J. Brighton, Pontryagin's Minimum Principle based model predictive control of energy management for a plug-in hybrid electric bus, Appl. Energy 236 (2019) 893-905.
[19] M. Shidari, H. Kebriani, Mean field optimal energy management of plug-in hybrid electric vehicles, IEEE Trans. Veh. Technol. 68 (1) (2019) 113-120.
[20] P. Pisu, G. Rizzoni, A comparative study of supervisory control strategies for hybrid electric vehicles, IEEE Trans. Contr. Syst. Technol. 15 (3) (2007) 506-518.
[21] F. Zhang, F. Yang, D. Xue, Y. Cai, Optimization of compound power split configurations in PHEV bus for fuel consumption and battery degradation decreasing, Energy 169 (2019) 937-957.
[22] G. Jinquan, H. Hongwen, P. Jiankun, Z. Nana, A novel MPC-based adaptive energy management strategy in plug-in hybrid electric vehicles, Energy 175 (2019) $378-392$.
[23] Y. Zhang, et al., An improved adaptive equivalent consumption minimization strategy for parallel plug-in hybrid electric vehicle, Proc. Inst. Mech. Eng. - Part D J. Automob. Eng. 233 (6) (2018) 1649-1663.
[24] J. Liu, Y. Chen, J. Zhan, F. Shang, Heuristic dynamic programming based online energy management strategy for plug-in hybrid electric vehicles, IEEE Trans. Veh. Technol. 68 (5) (2019) 4479-4493.
[25] R. Xiong, J. Cao, Q. Yu, Reinforcement learning-based real-time power management for hybrid energy storage system in the plug-in hybrid electric vehicle, Appl. Energy 211 (2018) 538-548.
[26] S. Yang, W. Wang, F. Zhang, Y. Hu, J. Xi, Driving-style-Oriented adaptive equivalent consumption minimization strategies for HEVs, IEEE Trans. Veh. Technol. 67 (10) (2018) 9249-9261.
[27] Likang Fan, et al., Design of an integrated energy management strategy for a plugin hybrid electric bus, J. Power Sources 448 (2020) 227391.
[28] Y. Du, Y. Zhao, Q. Wang, Y. Zhang, H. Xia, Trip-oriented stochastic optimal energy management strategy for plug-in hybrid electric bus, Energy 115 (2016) 1259-1271.
[29] Younes Nosrollahi, Armin Aligholian, Aminabbas Golshanfard, Stochastic energy modeling with consideration of electrical vehicles and renewable energy resourcesA review, Journal of Energy Management and Technology 4.1 (2020) 13-26.
[30] L. Li, S. You, C. Yang, B. Yan, J. Song, Z. Chen, Driving-behavior-aware stochastic model predictive control for plug-in hybrid electric buses, Appl. Energy 162 (2016) 868-879.
[31] Xiyun Li, et al., Adaptive energy management strategy for fuel cell/battery hybrid vehicles using Pontryagin's Minimal Principle, J. Power Sources 440 (2019) 227105.
[32] Y. Ni, J. He, L. Cai, Y. Bo, Data uploading in hybrid V2V/V2I vehicular networks: modeling and cooperative strategy, IEEE Trans. Veh. Technol. 67 (5) (2018) 4602-4614.
[33] C.M. Martinez, D. Cao, (Horizon-Enabled Energy Management for Electrified Vehicles, Butterworth-Heinemann, 2018.
[34] A. Pitanos, T. Jokela, M. Hancock, Predictive energy optimization for connected and automated HEVs, SAE Technical Paper 1 (2018).
[35] J. Zhao, Q. Li, Y. Gong, K. Zhang, Computation offloading and resource allocation for cloud assisted mobile edge computing in vehicular networks, IEEE Trans. Veh. Technol. 68 (8) (Aug. 2019) 7944-7956.
[36] M. Li, P. Si, Y. Zhang, Delay-tolerant data traffic to software-defined vehicular networks with mobile edge computing in smart city, IEEE Trans. Veh. Technol. 67 (10) (Oct. 2018) 9073-9086.
[37] H. Zhong, L. Pan, Q. Zhang, J. Cui, A new message authentication scheme for multiple devices in intelligent connected vehicles based on edge computing,", in IEEE Access 7 (2019) 108211-108222.
[38] Z. Haitao, D. Yi, Z. Mengkang, W. Qin, S. Xinyue and Z. Hongbo, "Multipath transmission workload balancing optimization scheme based on mobile edge computing in vehicular heterogeneous network," in IEEE Access, vol. 7, pp. 116047.
[39] X. Hou, Y. Li, M. Chen, D. Wu, D. Jin, S. Chen, Vehicular fog computing: a viewpoint of vehicles as the infrastructures, IEEE Trans. Veh. Technol. 65 (6) (Jun. 2016) 3860-3873.
[40] X. Chen, L. Wang, Exploring fog computing-based adaptive vehicular data scheduling policies through a compositional formal method-PEPA, IEEE Commun. Lett. 21 (4) (April 2017) 745-748.
[41] S. Bisons, R. Tatchikou, F. Dion, Vehicle-to-vehicle wireless communication protocols for enhancing highway traffic safety, IEEE Commun. Mag. 44 (1) (Jan. 2006) $74-82$.
[42] N. Xu, et al., Towards a smarter energy management system for hybrid vehicles: a comprehensive review of control strategies, Appl. Sci. 9 (10) (2019) 2026.
[43] T. Jo, H. Murakami, R. Masuda, M.K. Sakata, S. Yamamoto, T. Minamoto, Rapid degradation of longer DNA fragments enables the improved estimation of distribution and biomass using environmental DNA, Mol Ecol Resour 17 (6) (Nov 2017) e25-e33.
[44] Y. Qiang, C. Wei-Neng, L. Yun, C.L.P. Chen, X. Xiang-Min, J. Zhang, Multimodal estimation of distribution algorithms, IEEE Trans Cybern 47 (3) (Mar 2017) $636-650$.
[45] M. Germain, et al., Made Masked autoencoder for distribution estimation.pdf, in: International Conference on Machine Learning, 2015.
[46] D. Ding, Z. Wang, B. Shen, H. Dong, Hae state estimation with fading measurements, randomly varying nonlinearities and probabilistic distributed delays, Int. J. Robust Nonlinear Control 25 (13) (2015) 2180-2195.
[47] K. Xia, K. Opson, G.W. Wei, Multiscale Gaussian network model (mGNM) and multiscale anisotropic network model (mANM), J. Chem. Phys. 143 (20) (Nov 28 2015) 204106.
[48] L.F. Chamon, Alejandro Ribeiro, ,"Greedy sampling of graph signals.pdf:", IEEE Trans. Signal Process. 66 (1) (2017) 14.
[49] D. Holland, et al., Beyond SNP heritability: polygenicity and discoverability of phenotypes estimated with a univariate Gaussian mixture model, BioRxiv (2019) 133132.
[50] R. Suarez-Bertos, A.A. Zardini, H. Keoken, C. Astorga, Impact of ethanol containing gasoline blends on emissions from a flex-fuel vehicle tested over the Worldwide Harmonized Light duty Test Cycle (WLTC), Fuel 143 (2015) 173-182.
[51] S. Chao, H. Xianoung, S.J. Moura, S. Fengchun, Velocity predictors for predictive energy management in hybrid electric vehicles, IEEE Trans. Contr. Syst. Technol. 23 (3) (2015) 1197-1204.
[52] C. Zhu, F. Lu, H. Zhang, J. Sun, C.C. Mi, A real-time battery thermal management strategy for connected and automated hybrid electric vehicles (CAHEVs) based on iterative dynamic programming, IEEE Trans. Veh. Technol. 67 (9) (2018) 8077-8084.
[53] Yuanjian Zhang, et al., Cooperative control strategy for plug-in hybrid electric vehicles based on a hierarchical framework with fast calculation, J. Clean. Prod. 251 (2020) 119627.
[54] Vincent W. Zheng, et al., Towards mobile intelligence: learning from GPS history data for collaborative recommendation, Artif. Intell. 184 (2012) 17-37.