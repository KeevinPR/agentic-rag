# A Novel Energy Management Strategy for Plug-in Hybrid Electric Buses Based on Model Predictive Control and Estimation of Distribution Algorithm 

Xiang Tian ${ }^{\ominus}$, Yingfeng Cai ${ }^{\ominus}$, Senior Member, IEEE, Xiaodong Sun ${ }^{\ominus}$, Senior Member, IEEE, Zhen Zhu ${ }^{\ominus}$, and Yiqiang Xu


#### Abstract

Energy management strategies determine how much energy is consumed by the engine and electric motor of plug-in hybrid electric buses (PHEBs), which represent critical fuel-saving technologies. In this study, a model predictive control (MPC) method with the estimation of distribution algorithm (EDA) as the solver is proposed to optimize the energy flow of PHEBs. Inspired by the recursive mechanism, short-term velocity prediction is achieved based on a Markov chain model with online updates to greatly improve prediction accuracy. Then, the energy-flow control problem of PHEBs is formulated as a discrete-time nonlinear optimization problem. Due to its strong nonlinear multivariable and constrained nature, the control algorithm is implemented by using MPC. To obtain an optimal solution efficiently, the EDA algorithm is incorporated into the MPC-based control framework, in which the Gaussian distribution is selected as a probabilistic model to characterize the candidate solutions and make full use of the statistical information extracted from the search experience. All performance verifications were conducted by theoretical simulation and hardware-in-the-loop. The verification results show that the proposed strategy can greatly improve the fuel economy and the shorten computational time over cycle-based driving.


Index Terms-Energy optimization, fuel consumption, Markov chain, model predictive control (MPC), plug-in hybrid electric bus.

[^0]
## I. INTRODUCTION

AN INCREASING amount of attention has been given to energy management design as the core technology for hybrid electric vehicles (HEVs), which provides a great hope for reducing carbon emissions, addressing the threat of climate change, improving fuel economy, and alleviating range anxiety in recent decades [1]. Among the various existing configurations of HEVs, plug-in hybrid electric buses (PHEBs) equipped with large capacity batteries are one of the most promising products and can achieve the optimal fuel economy only when the battery is depleted at the end of the trip [2], [3]. Accordingly, it is critical to design a practical energy management strategy (EMS) to take full advantage of PHEBs to reduce fuel consumption, especially in the domain of urban public transportation [4].

Charge-depleting and charge-sustaining (CDCS) is a representative rule-based EMS, and PHEBs with the CDCS strategy could significantly reduce fuel consumption [5]-[7]. However, its rule-based design relies on quantities of experiments or calibrations, leading to poor adaptability in real implementation. To address this issue, Lin et al. [8] proposed a stochastic dynamic programming (DP) control strategy for a hybrid powertrain. However, the control performance is closely associated with the prediction accuracy of driver behaviors. In the equivalent consumption minimization strategy (ECMS), the equivalent factor is an important variable that determines the performance in terms of fuel economy for PHEBs [9]-[11]. Considering the changeability and uncertainty of the future driving cycle, a constant equivalent factor does not guarantee sound fuel economy. In [12], particle swarm optimization was applied to regulate the equivalent factor in light of different driving cycles [12]. Although the aforementioned methods exhibit great potential in fuel savings, they do not take the future driving conditions or driver demand into consideration [13]-[16]. Model predictive control (MPC) appears to be suitable to handle this issue, and it can plan the power distribution by minimizing the energy consumption of the preview horizon according to the driver's power demand [17]. The whole process is performed over a moving finite horizon so that it requires the driver's velocity demand to be known beforehand [18]-[20]. Currently, several prediction methods of short-term velocity have already been


[^0]:    Manuscript received 29 November 2021; revised 14 January 2022; accepted 28 February 2022. Date of publication 18 March 2022; date of current version 14 December 2022. Recommended by Technical Editor J. Marshall and Senior Editor X. Chen. This work was supported in part by the National Natural Science Foundation of China under Grant U1764257, and in part by the Foundation for Jiangsu key Laboratory of Traffic and Transportation Security (TTS2021-02). (Corresponding authors: Yingfeng Cai; Xiaodong Sun.)
    Xiang Tian, Yingfeng Cai, Xiaodong Sun, and Zhen Zhu are with the Automotive Engineering Research Institute, Jiangsu University, Zhenjiang 212013, China (e-mail: auzn0009@163.com; caicaixiao0304@ 126.com; xdsun@ujs.edu.cn; zhuzhenjs@126.com).

    Yiqiang Xu is with the Nexteer Automotive (Suzhou) Company, Ltd., Suzhou 215000, China (e-mail: xuyq_cloud@126.com).

    Color versions of one or more figures in this article are available at https://doi.org/10.1109/TMECH.2022.3156150.
    Digital Object Identifier 10.1109/TMECH. 2022.3156150

proposed. For example, the exponential varying approach [21], fuzzy granulation technology [22], artificial neural networks [23], and Markov chain model [24] could be chosen to predict the future velocity. Among them, the Markov chain model with the nature of a "Markov process" is fit to depict discretely random processes, which exhibits great prediction performance. However, a stationary Markov chain cannot precisely capture the short-term dynamics of the velocity data, thus producing nonnegligible errors. Further improvement in the accuracy of short-term velocity prediction remains a challenge.

In addition, MPC also offers such a predictive method that trip information can be incorporated into multifarious energy management strategies. A stochastic MPC was proposed to optimize the energy flow of a parallel HEV, where the road grade preview was taken into consideration [25]. In [26], the Markov chain Monte Carlo method was used to predict the future velocity sequences to further improve the MPC performance. In addition, a two-level MPC framework was proposed for a power-split PHEV, and the results showed that this strategy incorporating traffic information can obtain $94 \%$ fuel economy of the DP benchmark [27]. Due to the limited computational resources on board in real-time applications, computational efficiency is critical to MPC applications. Borhan et al. [28] adopted quadratic programming to solve the MPC problem of energy management for a power-split HEV. In [29], Pontryagin's minimum principle-based MPC was proposed to optimize the energy flow of a PHEB, and the power distribution was determined by using the shooting method. Furthermore, a DP-based MPC was also proposed to obtain the power distribution efficiently for a coaxis PHEV [30]. Nonetheless, devising an efficient and practicality-oriented MPC for PHEBs would still be worthy of more in-depth research.

To further help enhance the performance of the energy management of PHEBs, an efficient instantaneous EMS based on MPC and estimation of distribution algorithm (EDA) as the solver method is proposed in this article. The improvement in both velocity prediction and control sequence solving leads to the adaptability and efficiency of the new methodology becoming stronger. First, short-term velocity prediction is achieved based on a Markov chain model with self-update, whose renewal mechanism is realized by using the improved recursive algorithm to modify the probability transition matrix of vehicle acceleration. Then, an MPC framework is established to formulate the PHEB energy management problem. The EDA method is used as the solver, in which the Gaussian distribution is selected as a probabilistic model to characterize the candidate solutions. Due to the outstanding global search ability of the algorithm, the predictive optimal control can be realized for energy management. Finally, a performance comparison with different strategies is conducted in the MATLAB/Simulink environment over the West Virginia City (WVCITY) driving cycle, and simulation results reveal the superior performance of the proposed strategy in achieving improved fuel economy and real-time applicability. In addition, the proposed strategy is also verified through a hardware-in-the-loop (HIL) experiment. The contributions of this research are summarized in the following:
![img-0.jpeg](img-0.jpeg)

Fig. 1. Configuration of the plug-in hybrid electric bus.

1) The design methodology of short-term velocity prediction is presented, and its performance is verified in different prediction horizons.
2) The EDA is incorporated into the MPC-based control framework to formulate the energy management strategy of PHEBs.
3) Both theoretical simulations and HIL experiments are performed to demonstrate the capability of the proposed strategy in fuel savings and its online computational efficiency.
The rest of this article is organized as follows. The hybrid powertrain model is presented in Section II. Then, the MPCbased EMS is introduced in Section III, and the EDA to realize the optimal solution of the MPC problem is also discussed. The results of the theoretical simulation and HIL test are illustrated in Section IV, and the performance of different strategies is compared. Finally, Section V concludes this article.

## II. HyBRID POWERTRAIN MODEL

This research uses the vehicle model with the parallel hybrid arrangement, which is the most popular hybrid powertrain in the city bus market. The configuration of this hybrid powertrain is shown in Fig. 1. A diesel engine is mechanically connected to an electric motor by using the clutch, and its output torque is coupled to the driveline through automated mechanical transmission (AMT). The main components are located on the same driving shaft without the utilization of the mechanical coupler, which can help compress the whole powertrain space [31]. The dominating benefit of this artful design in the powertrain is that it possesses multiple operating modes to deal with complex driving cycles and has great potential to improve fuel economy. The main parameters regarding the model are listed in Table I.

In this parallel hybrid powertrain, the nominal power of the diesel engine is 218 kW , and the peak torque reaches 1150 Nm . Since only the fuel economy is considered, the complicated dynamic characteristics of the engine are neglected. Then, a quasi-static model of the diesel engine can be set up as follows:

$$
Q_{\mathrm{f}}=T_{\mathrm{e}} \cdot \omega_{\mathrm{e}} \cdot \dot{m}_{\mathrm{f}} \cdot \Delta t /\left(3600 \cdot \rho_{\mathrm{f}}\right)
$$

where $Q_{\mathrm{f}}$ is the fuel consumption, $\dot{m}_{\mathrm{f}}$ is the fueling rate, $\omega_{\mathrm{e}}$ is the engine speed, $T_{\mathrm{e}}$ is the engine torque, $\triangle t$ is the time interval, and $\rho_{\mathrm{f}}$ is the diesel density. Fig. 2 illustrates the engine brake

TABLE I
Main PANAMETERS OF THE VEHICLE


![img-4.jpeg](img-4.jpeg)

Fig. 2. BSFC map of the engine.
specific fuel consumption (BSFC). The fueling rate is a function of $\omega_{\mathrm{e}}$ and $T_{\mathrm{e}}$, as shown in the following equation:

$$
\dot{m}_{\mathrm{f}}=f_{\mathrm{fuel}}\left(T_{\mathrm{e}}, \omega_{\mathrm{e}}\right)
$$

For the electric motor, its peak power is 95 kW , and its peak torque is up to 850 Nm . Neglecting the dynamic characteristics, a static model with efficiency maps is applied to model the performance of the electric motor. The electric motor efficiency is a function of its speed and torque, and its output power $P_{\mathrm{m}}$ can be expressed as follows:

$$
\begin{aligned}
\eta_{m} & =f\left(T_{m}, \omega_{m}\right) \\
P_{m} & =T_{m} \omega_{m} \\
P_{B} & =P_{m} \cdot \eta_{m}^{-\operatorname{sign}\left(T_{m}\right)}
\end{aligned}
$$

where $P_{\mathrm{B}}$ is the battery power, $T_{\mathrm{m}}$ is the electric motor torque, $\omega_{\mathrm{m}}$ is the electric motor speed, $\eta_{\mathrm{m}}$ is the efficiency of the electric motor, and $\operatorname{sign}\left(T_{m}\right)=\left\{\begin{array}{c}1, T_{m} \geq 0 \\ -1, T_{m}<0\end{array}\right.$ is a sign function. The electric motor efficiency map from bench testing is presented in Fig. 3. To improve the transmission efficiency, a 6-speed AMT with gear ratios of $6.71,3.77,2.26,1.44,1$, and 0.77 is equipped in this configuration. A modified gear-shifting schedule, for achieving a good tradeoff between the fuel economy and drivability performance, is executed in the AMT control unit [32].

In this article, a lithium iron phosphate battery pack with a capacity of 110 Ah and a nominal voltage of 483 V is used as the energy storage system. Neglecting the effect of operating temperature and aging, the Rint model is applied to simulate battery charging/discharging characteristics, as shown in Fig. 4.
![img-4.jpeg](img-4.jpeg)

Fig. 3. Efficiency map of the electric motor.
![img-4.jpeg](img-4.jpeg)

Fig. 4. Rint model.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Internal resistance and open circuit voltage.

Based on the Kirchhoff law, the battery voltage $V_{\mathrm{c}}$ can be calculated by

$$
V_{C}=V_{O C}-I_{B} R_{B}
$$

where $V_{O C}, I_{B}$, and $R_{\mathrm{B}}$ are the open circuit voltage, battery current, and internal resistance, respectively. The characteristic curve of the battery is shown in Fig. 5. The state of charge (SOC) of the battery can be further written as follows:

$$
\left\{\begin{array}{l}
I_{B}=\frac{V_{O C}-\sqrt{\left(V_{O C}\right)^{2}-4 P_{B} R_{B}}}{2 R_{B}} \\
S O C=\frac{Q_{0}-\int_{0}^{1} I_{B} d \tau}{Q_{B}}
\end{array}\right.
$$

where $S O C$ is the battery SOC and $Q_{0}$ and $Q_{\mathrm{B}}$ are the initial and nominal battery capacities, respectively.

For the parallel hybrid powertrain, the torque balance can be written as follows:

$$
T_{\mathrm{w}}=\left(T_{\mathrm{e}}+T_{\mathrm{m}}\right) i_{\mathrm{g}} i_{0}\left(\eta_{\mathrm{T}}\right)^{\operatorname{sign}\left(T_{\mathrm{w}}\right)}+T_{\mathrm{brk}}
$$

where $T_{\mathrm{w}}$ is the driving torque acting on the wheel and $T_{\mathrm{brk}}$ is the braking torque acting on the wheel, whose value is zero or negative. $i_{0}$ denotes the final gear ratio, $i_{\mathrm{g}}$ denotes the AMT gear ratio, and $\eta_{\mathrm{T}}$ denotes the transmission efficiency

![img-5.jpeg](img-5.jpeg)

Fig. 6. Framework of the proposed strategy.
of the whole powertrain. Based on the longitudinal dynamics equation, the vehicle driving torque can also be expressed as follows:

$$
\begin{aligned}
& T_{w}= \\
& \left(m_{v} g f_{r} \cos \theta+\frac{1}{2} C_{D} A \rho v^{2}+m_{v} g \sin \theta+\delta m_{v} \frac{d v}{d t}\right) \cdot r_{w}
\end{aligned}
$$

where $v$ is the vehicle velocity and $\theta$ is the road slope.

## III. ENERGY MANAGEMENT STRATEGY DEVELOPMENT

To achieve sound fuel economy, the critical problem is how to utilize chemical energy and electric energy properly among the hybrid powertrain [33], [34]. Although urban bus routes exhibit regular and repeatable characteristics, different traffic conditions may make a huge difference in fuel consumption. To solve this issue, a combination of MPC and EDA methods for the PHEB is proposed to optimize the energy flow, whose control framework is demonstrated in Fig. 6. The vehicle velocity over each moving horizon is predicted based on a Markov chain with a recursive update. SOC planning is subsequently conducted, and the equivalent fuel consumption index is evaluated by the different combinations of power distributions. Then, the optimal power distribution can be derived from the receding-horizon EDA optimization. A more detailed presentation is given in the following sections.

## A. Markov Chain-Based Forecaster Model for Vehicle Velocity

In general, the Markov chain is a probabilistic model that characterizes a stochastic process. Assuming that the demand torque for a driver can be modeled as a stochastic process, then the future velocity would be predicted accurately using the Markov chain. According to the samples of velocity profiles actually collected in the vehicle through sensors, the acceleration and velocity sequences can be acquired beforehand. By discretizing the acceleration and velocity, when the velocity $v_{m}$ and corresponding acceleration $a_{i}$ at the $k$ th time step are assumed, the transition probability of acceleration shifting from $a_{i}$ to $a_{j}$ can be expressed as follows:

$$
\begin{aligned}
p_{m, i j}(k) & =\operatorname{Pr}\left\{a(k+1)=a_{j} \mid v(k)=v_{m}, a(k)=a_{i}\right\} \\
\forall i, j & \in\{1,2, \cdots, n\}
\end{aligned}
$$

where $\operatorname{Pr}\{\cdot\} \cdot\}$ denotes the conditional probability. For a given velocity $v_{m}$, the transition probability $p_{m, i j}(k)$ can be combined as a matrix $\boldsymbol{P}_{m}$.

Here, the transition matrix $\boldsymbol{P}_{m}$ can be obtained from the frequency deduced from the corresponding acceleration sequence $\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, which has the form of

$$
\left[P_{m}\right]_{i j}=\frac{n_{i j}}{n_{i}}, \forall i, j \in\{1,2, \cdots n\}
$$

![img-6.jpeg](img-6.jpeg)

Fig. 7. Velocity and acceleration profiles for WVCITY cycle.
where $n_{i j}$ is the number of transitions from $a_{i}$ to $a_{j}$, and $n_{i}$ is the number of transitions for $a_{i}$. Given $U(k) \in \mathbb{R}^{n}$, where $[U(k)]_{i}=\operatorname{Pr}\left\{a(k)=a_{i}\right\}$ with the current velocity $v_{m}$, the probability distribution of $a(k+1)$ can be obtained by

$$
U(k+1)=P_{m} \cdot U(k)
$$

Searching $U(k+1)$ to find the maximum element, its corresponding acceleration is $a(k+1)$. Then, the predicted velocity $v_{p}$ at the $k+1$ time step can be expressed as follows:

$$
v_{p}(k+1)=v(k)+a(k+1)
$$

Hence, a sequence of future velocities can be obtained by repeating the above-mentioned calculation. However, driver behavior may be profoundly affected due to the complex and changeable urban traffic conditions. It changes over time so that the fixed transition probability matrix inevitably leads to prediction errors. To improve the prediction accuracy, an improved recursive algorithm is introduced to update the probability transition matrix online. The vector $\beta_{m, i}$ that represents which transition has occurred for the current velocity $v_{m}$ and acceleration $a_{i}$ can be defined as follows:

$$
\begin{aligned}
& {\left[\beta_{m, i}\right]_{j}=} \\
& \left\{\begin{array}{c}
1, \text { if } a(k)=a_{j} \text { and } a(k-1)=a_{i} \\
0, \text { else }
\end{array}, \forall j \in\{1,2, \cdots, n\}\right.
\end{aligned}
$$

The regulation parameter $\gamma_{i}(k)$ is associated with the actual transition result and can be obtained by

$$
\gamma_{i}(k)=\frac{\left.\sum_{j=1}^{n}\left[\beta_{m, i}\right]_{j}\right.}{n_{i}(k-1)+\sum_{j=1}^{n}\left[\beta_{m, i}\right]_{j}}
$$

Hence, the probability transition matrix can be recursively calculated by

$$
\begin{aligned}
{\left[P_{m}(k)\right]_{i j} } & =\left(1-\gamma_{i}(k)\right)\left[P_{m}(k-1)\right]_{i j}+\gamma_{i}(k)\left[\beta_{m, i}\right]_{j} \\
\forall j & \in\{1,2, \cdots n\}
\end{aligned}
$$

In this article, the WVCITY cycle is chosen as the test cycle to verify the reliability of the prediction method, whose velocity profile is demonstrated in Fig. 7. The maximum and minimum accelerations are $-3.2 \mathrm{~m} / \mathrm{s}^{2}$ and $1.1 \mathrm{~m} / \mathrm{s}^{2}$, respectively, so that the whole range is divided into 44 discrete points. Fig. 8 shows the acceleration transition probability matrix at a velocity of $20 \mathrm{~km} / \mathrm{h}$. The variation trend of the acceleration is consistent with that of the previous hypothesis. Different time horizons,
![img-7.jpeg](img-7.jpeg)

Fig. 8. Transition probability of the acceleration $\left(v_{m}=20 \mathrm{~km} / \mathrm{h}\right)$.
![img-8.jpeg](img-8.jpeg)

Fig. 9. Predicting velocity based on Markov chain model.

TABLE II
Predictive Performance Evaluation Indices Over WVCITY Cycle

such as 5,10 , and 15 s , are selected to further verify the prediction performance. To elucidate the prediction performance, both the prediction results and real values are plotted together in Fig. 9, and the predictive performance evaluation indices, such as root mean squared error (RMSE) and mean absolute error (MAE), are also listed in Table II. It is apparent that the predicted results of the velocity become less precise as the prediction horizon increases. Hence, the prediction horizon of 5 s is suitable to forecast velocity in this research, which can be incorporated into the MPC framework.

## B. Reference SOC Planning

As outlined earlier, a PHEB with a large battery capacity can provide a considerable portion of the total power demand to reduce fuel consumption. When the battery is depleted, it can be recharged from external electric power grids in a conductive charging manner. Given this feature, the optimal fuel economy can be achieved for the PHEB when the battery is depleted at the terminal stop on the urban bus route. Therefore, devising the optimal SOC trajectory is critical to the energy optimization

of the PHEB running on a fixed bus route. The optimal SOC trajectory can be used as the reference, which reflects the electric energy consumption over the whole bus route. In this research, the optimal SOC trajectory can be extracted by the DP method. Assuming that the bus drivers tend to have similar driving behaviors under the same road conditions, the allocation of reference SOC can be regarded to be only related to the remainder range of the whole trip, which can be expressed as follows:

$$
\begin{aligned}
S O C_{r}\left(k+N_{p}\right)= & S O C(k)-\frac{d_{p}\left(k+N_{p}\right)}{D-d(k)} \\
& \times S O C(k)-S O C_{o p t} \\
d_{p}\left(k+N_{p}\right)= & \int_{k T_{s}}^{\left(k+N_{p}\right) T_{s}} v_{p}(t) d t
\end{aligned}
$$

where $k$ denotes the time step, $N_{p}$ denotes the time span for the predictive horizon, $\mathrm{SOC}_{\text {opt }}$ denotes the preset battery SOC deduced from the optimal SOC trajectory, $S O C(k)$ denotes the battery SOC at the $k$ th time step, $S O C_{r}\left(k+N_{p}\right)$ denotes the reference value of the battery SOC at the end of the predicting horizon of the $k$ th time step, $D$ is the distance of the whole trip, $d(k)$ is the traveled distance after the $k$ th time step, $d_{p}\left(k+N_{p}\right)$ represents the driving distance of the prediction horizon at the $k$ th time step, $T_{s}$ is the sample time, and $v_{p}$ is the predicted velocity. The optimal SOC trajectory regarded as the reference is demonstrated in Fig. 6.

## C. MPC Formulation

The power distribution problem for the PHEB can be formulated as an MPC optimal control problem. Consider the linear time-varying discrete system

$$
\left\{\begin{aligned}
x(k+1)=A(k) x(k)+B(k) u(k)+G(k) d(k) \\
y(k)=C(k) x(k)+D(k) u(k)+H(k) d(k)
\end{aligned}\right.
$$

where $x, y$, and $u$ represent the vectors of the system state, output state, and input state, respectively, and $d$ is a disturbance state, whose probability distribution is a Markov distribution.

$$
\begin{aligned}
x(k) & =\left[v(k), T_{\mathrm{c}}(k-1), S O C(k)\right]^{\prime} \\
u(k) & =\left[\Delta T_{\mathrm{c}}(k), T_{\mathrm{bck}}(k)\right]^{\prime} \\
d(k) & =\left[T_{\mathrm{req}}(k), F_{\mathrm{f}}(k)\right]^{\prime} \\
y(k) & =P_{B}(k) \\
A(k) & =\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 \lambda(k) \cdot \Psi_{\mathrm{B}} & 1
\end{array}\right] \\
B(k) & =\left[\begin{array}{cc}
0 & 0 \\
1 & 0 \\
\lambda(k) \cdot \Psi_{\mathrm{B}} & \frac{\lambda(k)}{\eta_{T} i_{0} i_{g}} \cdot \Psi_{\mathrm{B}}
\end{array}\right] \\
G(k) & =\left[\begin{array}{cc}
\frac{1}{\delta m r_{\mathrm{m}}} & \frac{-1}{\delta m} \\
0 & 0 \\
\frac{-\lambda(k)}{\eta_{T} i_{0} i_{g}} \cdot \Psi_{\mathrm{B}} & 0
\end{array}\right]
\end{aligned}
$$

$$
\begin{aligned}
C(k) & =\left[0,-\lambda(k), 0\right], D(k)=\left[-\lambda(k), \frac{-\lambda(k)}{\eta_{T} i_{0} i_{g}}\right] \\
H(k) & =\left[\frac{\lambda(k)}{\eta_{T} i_{0} i_{g}}, 0\right]
\end{aligned}
$$

where $\Psi_{\mathrm{B}}=\frac{1}{\eta_{c} \cdot V_{\mathrm{oc}} \cdot Q_{\mathrm{B}}}$, and $\eta_{c}$ is the coulombic efficiency. $\lambda(k)=\omega_{\mathrm{m}}(k) \cdot \eta_{\mathrm{m}}^{\operatorname{sign}\left(T_{\mathrm{m}}\right)}$ is associated with the rotation speed of the electric motor at the $k$ th time step. $T_{\text {req }}(k)$ and $\Delta T_{\mathrm{c}}(k)$ denote the driver demand torque and difference of the engine torque at the $k$ th time step, respectively. $F_{\mathrm{f}}(k)$ represents the related resistance of the vehicle, including the rolling resistance, air resistance, and climbing resistance. Furthermore, some constraints must be set to limit the system states and control variables, which can be defined as follows:

$$
\left\{\begin{aligned}
S O C_{\min } & \leq S O C(k) \leq S O C_{\max } \\
& -\Delta T_{\mathrm{c}}^{\max } \leq \Delta T_{\mathrm{c}}(k) \leq \Delta T_{\mathrm{c}}^{\max } \\
T_{\mathrm{c}}^{\min } & \leq T_{\mathrm{c}}(k) \leq T_{\mathrm{c}}^{\max }, \omega_{\mathrm{m}}^{\min } \leq \omega_{\mathrm{c}}(k) \leq \omega_{\mathrm{m}}^{\max } \\
T_{\mathrm{m}}^{\min } & \leq T_{\mathrm{m}}(k) \leq T_{\mathrm{m}}^{\max }, \omega_{\mathrm{m}}^{\min } \leq \omega_{\mathrm{m}}(k) \leq \omega_{\mathrm{m}}^{\max }
\end{aligned}\right.
$$

where the indices min and max denote the lower and upper boundary values of the corresponding parameters, respectively.

In this research, the fuel economy performance corresponds to the equivalent fuel consumption that contains fuel consumption and electric consumption. Hence, the cost function of the MPC problem can be formulated as follows:

$$
\begin{aligned}
J= & \min \sum_{i=1}^{N_{p}} Q_{f}(k+i)+\gamma\left[S O C\left(k+N_{p}\right)\right. \\
& \left.-S O C_{r}\left(k+N_{p}\right)\right]
\end{aligned}
$$

s.t. Eq. (19) and (21)
where $\gamma$ is the penalty parameter regarding the battery SOC.

## D. EDA for Receding-Horizon Optimization

The aforementioned MPC problem exhibits a high dimensionality, strong nonlinearity, and uncertain nature. Compared with common typical methods, such as the shooting method and sequential quadratic programming, the EDA as a population-based and iterative algorithm is very powerful in solving such a PHEB energy management problem, which exhibits the outstanding ability of global search and faster convergence.

EDA can reproduce a new population using statistical information extracted from search experience instead of traditional evolutionary operators. In the search space, a probability model of the most promising solutions is constructed. Then, the new individuals can be generated from the aforementioned model, and this process is called sampling. Based on new individuals, a new probability model is estimated and reconstructed, which describes the distribution of the most promising solutions. Hence, the population can evolve toward the optimal solutions by repeating the above-mentioned steps. The EDA flowchart is also presented in Fig. 6.

To apply the EDA algorithm in the optimization problem of energy management for PHEBs, the cost function should be

TABLE III
RePRESENTATION OF THE POPULATION MATRIX M

reformulated by discretizing the engine power as follows:

$$
\begin{aligned}
J= & \min \sum_{i=1}^{N_{p}} \sum_{j=1}^{M} h(k+i, j) P_{c}(j) / \eta_{c}(j) \\
& +\gamma\left[S O C\left(k+N_{p}\right)-S O C_{r}\left(k+N_{p}\right)\right] \\
\text { s.t. } & \sum_{j=1}^{M} h(k+i, j)=1 \quad \forall j \\
& h(k+i, j)=\{0,1\} \quad \forall i, j \\
& \text { Eq. (19) and (21) }
\end{aligned}
$$

where $M$ is the number of discretized power levels, $j$ is the index of the power level, $P_{c}(j)$ is the $j$ th discretized power level for the engine, and $\eta_{c}(j)$ is the associated efficiency for the engine. Once the engine power is determined, the fuel consumption can also be calculated in (1). In this optimization problem, each individual consisting of an engine power sequence is a candidate solution, whose vector size is the length of the predictive horizon. Here, the Gaussian distribution is selected as a probabilistic model to characterize the candidate solutions. Assuming the size of the population is $L$, the population can be expressed as a matrix $\mathbf{M}=\left(m_{i j}\right)_{L \times N_{p}}$, whose representation is listed in Table III. Taking Individual_1 as an example, the engine power level at the second time step of the horizon is 0 kW , which implies that the engine is shut off and only the battery pack can supply power.

For each element of every individual in the population, the Gaussian probabilistic distribution can be formulated as follows:

$$
\begin{aligned}
g(m, u, \sigma) & =\frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(m-u)^{2}}{2 \sigma^{2}}}, u=m_{i j} \\
\sigma & =\frac{\rho_{1}}{\sqrt{L-1}} \sqrt{\sum_{l=1}^{L}\left(m_{l j}-m_{i j}\right)^{2}}
\end{aligned}
$$

where $\rho_{1}$ is a constant. Here, the number of Gaussian functions is $L \times N_{p}$. The mean and standard deviation values of each Gaussian function are different.

Subsequently, each individual is substituted into the cost function to obtain the cost value. According to the cost value in ascending order, the priority vector $\mathbf{R}=\left[r_{1}, r_{2}, \cdots, r_{h}, \cdots, r_{L}\right]^{\mathrm{T}}$ is generated. For example, $r_{l}=1$ when the $l$ th individual has the minimum value of the cost function. Then, the weight of each
individual can be calculated by the following expression:

$$
\omega_{i}=\frac{1}{\rho_{2} L \sqrt{2 \pi}} e^{-\frac{\left(r_{i}-r_{l}\right)^{2}}{2 \rho_{2} L)^{2}}}, i=1, \cdots, L
$$

where $\omega_{i}$ is the weight for the $i$ th individual and $\rho_{2}$ is a constant. For the dominant individual, its weight has a larger value.

To generate the new individual, the Gaussian distribution for the $j$ th element of the new individual should be selected from the group of Gaussian probabilistic distributions expressed in (24). The corresponding selection probability can be defined as follows:

$$
q_{i}=\frac{\omega_{i}}{\sum_{l=1}^{L} \omega_{l}}, i=1, \cdots, L
$$

where $q_{i}$ denotes the probability that the $i$ th group of Gaussian distributions is selected. When the value of $q_{i}$ is larger, the corresponding group will be selected. Then, the $j$ th element of the new individual $N E_{j}$ will be acquired by sampling the selected Gaussian distribution. Repeating $N_{p}$ times, the new individual is available.

Every $q_{\text {iter }}$ iteration, a new Gaussian function is constructed to replace the original function. Then, the new individual should be reproduced by sampling the new Gaussian function. This is beneficial to improving the dispersion of individuals. The formulation of the new Gaussian function can be expressed as follows:

$$
\begin{aligned}
& g_{\text {new }}(x, u, \sigma)=\frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(m-u)^{2}}{2 \sigma^{2}}}, j=1, \cdots, N_{p} \\
& u=m_{b s, j}, \sigma=\max \left[\left(m_{j}^{\max }-m_{b s, j}\right),\left(m_{b s, j}-m_{j}^{\min }\right)\right]
\end{aligned}
$$

where $m_{b s, j}$ is the optimal value of the $j$ th element of an individual among the current population. $m_{j}^{\min }$ and $m_{j}^{\max }$ are the lower and higher thresholds of the $j$ th element of the individual, respectively.

After each iteration, the dominant individuals with the least fuel consumption are chosen as the parents for reproducing the next generation of individuals by the process of estimation and sampling. It is beneficial to evolve the population toward the optimal solution. When the ending condition of the optimization problem is satisfied, the best-so-far solution can be regarded as the final result. The pseudocode for the EDA algorithm is shown in Table IV.

## IV. RESULTS AND DISCUSSION

In this section, the proposed strategy is evaluated on a simulation platform based on MATLAB/Simulink and the HIL test bench. Considering that one WVCITY cycle is too short, the testing time used is quadruple that of the WVCITY cycle. In addition, the battery capacity is set as half of the nominal value in both the simulation and HIL tests. The simulation platform, including the driver model, powertrain model, control model, and vehicle dynamics model, is presented in Fig. 10. The acceleration and braking commands are generated from the driver model. The powertrain model consists of the engine, clutch, electric motor, battery, and AMT, whose setting parameters are

TABLE IV
PSEUDOCODE FOR THE EDA ALGORITHM

```
1} \(t=0\)
2 Initialization Matrix \(\boldsymbol{M}_{0}: *\) Generate \(L\) individuals randomly */
3 while an ending criterion is not met do
4 for \(i=1\) to \(L\) do
5 for \(j=1\) to \(N_{0}\) do
6 Formulate Gaussian distribution for each element in the
    population \(\leftarrow\) Eq. (24)
    end for
    end for
    for \(i=1\) to \(L\) do
        Compute the priority vector \(\boldsymbol{R}\) and sort by ascending order
        end for
        for \(i=1\) to \(L\) do
            Compute the weight of each individual \(\omega_{i} \leftarrow\) Eq. (25)
        end for
        for \(i=1\) to \(L\) do
            Calculate the selection probability \(q_{i} \leftarrow\) Eq. (26)
        end for
        if \(t=q_{L D}\) then
            for \(j=1\) to \(N_{0}\) do
                Generate the \(j\)-th element \(N E_{j}\) using the selected Gaussian
                distribution
            end for
        else
        for \(j=1\) to \(N_{0}\) do
            Generate the \(j\)-th element \(N E_{j}\) using the new Gaussian
                distribution function \(\leftarrow\) Eq. (27)
            end for
        \(t=0\)
        end if
        \(t=t+1\)
29 end while
```

![img-9.jpeg](img-9.jpeg)

Fig. 10. Simulation platform for verifications.
determined as presented in Section II. The vehicle dynamics model is used to compute the tractive force so that the vehicle velocity is obtained.

## A. Simulation Case: WVCITY Cycle

To protect the battery pack, the initial electrical energy level must not be full in the actual running process. Hence, an initial battery SOC of $90 \%$ is set in the simulation. Fig. 11 demonstrates the vehicle performance over cycle-based driving. As shown, the proposed strategy can make the simulation velocity approximately consistent with the reference defined by the WVCITY cycle. The maximum velocity error is less than $2.0 \mathrm{~km} / \mathrm{h}$, which means that the velocity-following performance of the proposed strategy is considered to be good enough. Due to the configuration of the large-capacity battery, the electric motor is controlled to provide the most tractive force for running of the PHEB, especially when the battery SOC is high. Relatively, the engine has more opportunities to operate alone or together with the electric motor in a high-efficiency area for fuel savings. In
![img-10.jpeg](img-10.jpeg)

Fig. 11. Vehicle system performance over cycle-based driving (initial $\mathrm{SOC}=90 \%)$.

TABLE V
CONTROL PERFORMANCE COMPARISON OVER CYCLE-BASED DRIVING


*Battery capacity $Q_{\mathrm{D}}=55 \mathrm{Ah}$.
addition, the electric motor can operate as a generator during regenerative braking, which is beneficial to making full use of the excess kinetic energy of the vehicle.

## B. Comparison of Different Strategies

To evaluate the superiority of the proposed strategy, different energy management strategies, such as CDCS, ECMS, and DP, are applied to make a comparison regarding fuel consumption, electric consumption, total cost, etc. Among them, the CDCS method is used as the benchmark. For a fair comparison, the total cost is chosen as the evaluation indicator to assess the performance of different strategies. Based on market average prices, the prices of diesel fuel and electricity were 6.5 CNY/L and $0.8 \mathrm{CNY} / \mathrm{kWh}$, respectively.

Here, all simulation works are executed in the same simulation platform, whose results are summarized in Table V. As illustrated, the total cost of the CDCS method is 39.509 CNY and it is the highest among these methods. This is because the preset rules in the CDCS method do not guarantee optimality. For ECMS with an optimized equivalent factor, the reduction of total cost is up to $5.53 \%$ compared with that of the CDCS method. Once the driving cycle changes, the equivalent factor needs to be adjusted; otherwise, the ECMS performance will deteriorate. The DP method can achieve the lowest cost over the whole driving cycle, but it is impossible to implement it in real-world HEVs. Benefiting from the introduction of the velocity prediction information, the total cost of the proposed strategy is 35.623 CNY ,

![img-11.jpeg](img-11.jpeg)

Fig. 12. SOC trajectories of different strategies.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Distribution range of engine working points.
and the increment is only $8.06 \%$ compared with that of the DP method. Apparently, the performance difference between the proposed strategy and DP method is whether to use the global information of the driving cycle. However, the proposed strategy can achieve reductions of approximately $9.84 \%$ and $4.56 \%$ in total cost in comparison with the CDCS and ECMS strategies, respectively. On the whole, these results demonstrate that the proposed strategy exhibits outstanding capability in terms of energy savings, and its performance is second only to the DP method.

On the other hand, the battery SOC is an important parameter indicating the flow direction of electric energy, which can represent the electric consumption over the whole driving cycle. Fig. 12 illustrates the SOC trajectories based on different strategies over the driving cycle, in which the SOC trajectory obtained by the DP method is selected as the reference. As shown, the electric energy alone is not sufficient to satisfy the driver's power demand over the entire cycle, so the SOC under the CDCS strategy is consumed to the lower threshold at 2000 s . This phenomenon is bad for the improvement of fuel economy. In addition, the SOC under the ECMS method declines relatively quickly, and the battery is nearly depleted at 4000 s . As a result, the output of the motor is constrained after that moment, making it possible for the engine to operate in less efficient regions. For the proposed strategy, the SOC trajectory is close to the reference curve, which means that the electric energy stored in the battery is fully utilized to reduce fuel consumption.

To further explain why the proposed strategy exhibits better fuel economy, the distribution range of engine working points of different strategies is illustrated in Fig. 13. Because a great number of points are distributed in the high-efficiency region, the DP method can achieve optimal fuel economy. The energy distribution under the CDCS method relies on fixed rules so that the engine operating points are distributed dispersedly. The performance of the CDCS method in fuel economy is the worst
![img-13.jpeg](img-13.jpeg)

Fig. 14. RMSE and standard deviation of the velocity forecast results.

TABLE VI
EVALUATION RESULTS OF ALGORITHMIC PERFORMANCE


among these methods. Compared to the ECMS strategy, the proposed strategy allows the distribution of the engine working points to be more reasonable. Therefore, sound fuel economy is achieved by the proposed strategy.

## C. Algorithmic Performance Evaluation

To evaluate the algorithmic performance, the traditional MPC is selected to make a comparison with the proposed strategy. In the traditional MPC, velocity forecasting is realized by using the Markov chain model without self-update, and the shooting method is selected to obtain the candidate solutions. When the WVCITY cycle was repeated four times, the RMSE and standard deviation of the velocity forecast results are shown in Fig. 14. It is observed that as the prediction horizon increases from 5 to 15 s , the RMSE in the Markov chain model without self-update grows from 1.914 to $7.136 \mathrm{~km} / \mathrm{h}$, whereas the RMSE of the velocity forecast with the self-update mechanism only grows from 1.302 to $6.236 \mathrm{~km} / \mathrm{h}$. The standard deviations for these two forecasting methods in the 5 s forecasting situation are relatively small, approximately 0.51 and 0.29 , respectively. As the horizon increases, the prediction results become less precise for both methods. This is because under the Markov chain model, the causal link between predicted and current velocities is ambiguous, especially in the larger predictive horizon. Regardless, the proposed strategy obtains better prediction accuracy than the traditional MPC in the same horizon through the recursive mechanism.

The evaluation results between traditional MPC and the proposed strategy are summarized in Table VI. The total cost of the traditional MPC is 37.47 CNY over the $4 \times$ WVCITY cycle, whereas the total cost of the proposed strategy is reduced by $4.93 \%$ in comparison with that of traditional MPC. More importantly, the computational time that each method takes to obtain the optimal solution is critical, especially if targeting a real-time application where computational resources on board

![img-14.jpeg](img-14.jpeg)

Fig. 15. Framework of the HIL test bench.

TABLE VII
TECHNICAL DESCRIPTION OF THE MODULES


are limited. The computational time of traditional MPC is 421 s over the testing cycle, while the value of the proposed strategy is only up to 289 s . It can be noted that the elapsed time with the proposed strategy is shorter than that of traditional MPC, whose reduction is up to $31.35 \%$. The reasons for these achievements can be summarized as follows: first, more accurate short-term velocity prediction is the basis of the energy management of PHEBs based on MPC, and second, the EDA algorithm with global search capability is selected as the solver to guide the evolution toward the optimal solution by making full use of the statistical information of each individual. To summarize, the proposed strategy with the shorter computational time requirement exhibits outstanding fuel savings ability.

## D. HIL Implementation and Its Results

Since many unpredictable factors in real-time applications still exist, the HIL test bench is employed to evaluate the performance and effectiveness in this article. The bench consists of the NI real-time simulator, supervisor platform, vehicle control unit, and hybrid powertrain model, as shown in Fig. 15.

The NI real-time simulator comprises the processor card, CAN interface module, multifunctional RIO board, and programmable power supply. The technical description of the modules is listed in Table VII.

In the MATLAB/Simulink environment, the hybrid powertrain model can be compiled by the simulation interface toolkit and downloaded into the NI real-time simulator. Then, the control strategy is compiled and programmed into the vehicle control unit to execute by using a real-time workshop. During running of the program, the data link between the NI real-time simulator and vehicle control unit is realized by CAN communication. Finally, the test information and collected data are displayed on the supervisor platform by using the LAN interface.

Fig. 16 demonstrates the HIL experiment curves, including the actual velocity, fuel consumption, and battery SOC. Similar
![img-15.jpeg](img-15.jpeg)

Fig. 16. HIL experiment curves. (a) Velocity. (b) Fuel consumption and SOC.
![img-16.jpeg](img-16.jpeg)

Fig. 17. Output of two power sources in the HIL. (a) Engine. (b) Electric motor.
to the simulation results, the actual velocity accurately follows the reference. In addition, the output of the engine and electric motor over the whole trip is shown in Fig. 17. The electric motor features constant torque output characteristics in the low-speed region so that it can provide most of the tractive power to reduce the fuel consumption from the engine when the vehicle velocity is low. On that basis, the large capacity of the battery equipped makes the motor operate more flexibly together with the engine. It can also be discerned from Fig. 17 that the driver's torque demand is well-satisfied under the proposed strategy.

The performance comparison of different control strategies between the theoretical simulation and HIL tests in terms of the total cost is conducted to evaluate the effectiveness of the proposed strategy, as summarized in Table VIII. In the HIL tests, the total costs of the CDCS strategy, ECMS, and proposed strategy are 40.469 CNY, 39.007 CNY, and 37.266 CNY, respectively. Among them, the proposed strategy still achieves a lower total cost, which exhibits outstanding control performance. In addition, the deviations between the simulation and HIL tests under the CDCS strategy, ECMS, and proposed strategy are $2.5 \%, 4.5 \%$, and $4.6 \%$, respectively. This is because of the difference in signal transmission and processing between simulation and HIL tests. Especially, for both the proposed strategy and ECMS, the signal processing error and CAN communication

TABLE VIII
PerformAnCE COMPARISON BETWEEN SiMULATION AND HIL TESTS

![img-17.jpeg](img-17.jpeg)

Fig. 18. Operating point distribution maps of the engine and electric motor in the HIL. (a) CDCS strategy. (b) Proposed strategy.
delay further deteriorate the accuracy of the control problem solution in the HIL. Even then, the proposed strategy can obtain a better satisfactory control performance in view of the results of HIL, which is more in line with the original design purpose.

Furthermore, the operating point distribution maps of the engine and the electric motor under the CDCS method and proposed strategy are demonstrated in Fig. 18. As shown, the engine operating points under the CDCS method are distributed fairly in different ranges, while the operating points of the electric motor are relatively concentrated. Benefitting from the excellent global search ability, the proposed strategy distributes more engine operating points in the high-efficiency range. Similarly, the operation efficiency of the electric motor is also improved. These factors lead to the total cost of the proposed strategy being dramatically lower than that of the CDCS method. In summary, both theoretical simulation and HIL test results indicate that the proposed strategy can greatly improve fuel economy, showing that it is an efficient online EMS for PHEBs.

## V. CONCLUSION

PHEBs are equipped with a larger capacity battery than other structures of HEVs, so there is great potential to improve fuel economy. In this article, a predictive EMS based on MPC and

EDA methods is exploited, which exhibits excellent performance in fuel savings and online implementation. By introducing the improved recursive algorithm, a finite-state Markov chain model with a self-update mechanism is established to realize short-term velocity prediction. On this basis, an MPC-based control framework is designed, while the EDA with excellent ability of global search and faster convergence is applied to obtain the optimal control sequence in the receding horizon. Theoretical simulations are conducted, and the results demonstrate that the total cost of the proposed strategy is greatly decreased by nearly $5 \%$ compared to that of the traditional MPC method. The computational efficiency of the proposed strategy is improved impressively, whose elapsed time is only one-third of that of traditional MPC. Furthermore, the effectiveness is also validated by HIL experiments.

As advanced internet of vehicles technology develops, our research will focus on devising an application-oriented EMS for PHEBs by incorporating a large amount of traffic information to further reduce fuel consumption. In addition, the effect of the velocity prediction may be influenced by the driver's driving behaviors, and driving pattern recognition needs to be taken into consideration.
