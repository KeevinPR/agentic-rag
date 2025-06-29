# Hierarchical Energy Management for Power-Split Plug-In HEVs Using Distance-Based Optimized Speed and SOC Profiles 

Hansang Lim ${ }^{\circledR}$, Member, IEEE, and Wencong Su ${ }^{\circledR}$, Member, IEEE


#### Abstract

This paper proposes a distance-based two-stage energy management strategy for power-split plug-in hybrid electric vehicles (PHEVs). One stage is for long-term optimization and the other is for short-term adaptation to actual traffic conditions. Energy consumption in PHEVs depends on the characteristics of the drivetrain as well as the operating conditions such as power demands and their split. Thus, prior to departure, the operating conditions for a whole trip are optimized for the drivetrain characteristics and trip information, which generates optimal speed and state-of-charge profiles. While driving, the operating conditions are adapted to current traffic conditions for a short horizon on the basis of long-term optimization results. In consideration of the changeability of traffic conditions, the proposed energy management strategy is performed in a distance domain, which localizes the effects of changes in traffic conditions on the long-term optimization results. Therefore, this distance-based two-stage strategy improves the balance between the optimality and the real-time computing time, which is suitable for online management. A model for the propulsion system in a PHEV and the energy management strategy were formulated in a distance domain. An estimation of distribution algorithm was used for long-term optimization and local adaptation.


Index Terms-Distance-based, long-term optimization, local adaptation, hierarchical scheme, estimation of distribution algorithm.

## I. INTRODUCTION

HYBRID electric vehicles (HEVs) have remarkable fuel economy owing to an additional degree-of-freedom provided by two or more propulsive sources [1]-[3], which enables engine down-sizing, regenerative braking and engine operation in more efficient regions. Among the possible three categories, namely, series [4], [5], parallel [6], [7], and power-split hybrids [3], [8]-[10], the power-split configuration takes advantage of both the series and parallel types under proper control, and have

Manuscript received December 22, 2017; revised April 27, 2018 and June 11, 2018; accepted August 1, 2018. Date of publication August 3, 2018; date of current version October 15, 2018. This work was supported in part by the research grant of Kwangwoon University in 2017 and in part by the Basic Science Research Program through the National Research Foundation of Korea (NRF-2016R1D1A1B03935190). The review of this paper was coordinated by Prof. M. Preindl. (Corresponding author: Hansang Lim.)
H. Lim is with the Department of Electronics Convergence Engineering, Kwangwoon University, Seoul 01897, South Korea (e-mail: lhs@kw.ac.kr).
W. Su is with the Department of Electrical and Computer Engineering, University of Michigan, Dearborn, MI 48128 USA (e-mail: wencong@umich.edu). Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TVT.2018.2862945
been produced by automobile manufacturers [11], [12]. The recent development in battery technology introduces plug-in hybrid electric vehicles (PHEVs) that have larger battery capacities and can be charged from an external power source. Thus, PHEVs can achieve a higher fuel economy compared to conventional HEVs, and appear to be a next step to reducing fuel consumption and exhaust emission.

Energy economy in HEVs and PHEVs is strongly dependent on the regulation of the power split between the propulsive sources for the power demand. This power split is determined by the energy management strategy, which is more essential to PHEVs owing to their larger battery capacity. Diverse energy management strategies in HEVs and PHEVs have been developed in the literature, which are broadly divided into three categories based on the methods of determination of the control parameters for the power split: rule-based, global optimizationbased, and real-time optimization strategies.

The rule-based strategies regulate the power split by the rules that are determined by heuristics and human expertise [13] or whose constituent parameters are obtained by fuzzy logic [14], [15] and genetic algorithm [16]. While this approach is straightforward and convenient to implement in a manner suitable for real-time energy management, there is no guarantee of its optimality under diverse driving conditions.

The global optimization-based strategies numerically determine the most optimal energy management solution over a predefined driving cycle. As the power-split problem in HEVs and PHEVs is a non-linear equation with complex constraints, dynamic programming (DP) has been widely used as an optimization algorithm [7], [10], [17] or a benchmark [3], [8]; this can guarantee a globally optimal solution. However, DP requires complete knowledge of the future driving conditions and excessively long computation time. As traffic conditions frequently change, the driving cycle followed by a vehicle is likely to deviate from the predefined driving cycle for which DP carries out the optimization. This unpredictability of traffic conditions requires real-time energy management that can cope with change in traffic conditions.

Real-time optimization strategies are based on optimization over a finite horizon, i.e., a part of the entire driving cycle, which utilizes limited knowledge of the future driving conditions and, consequently, results in rapid computation. A common approach is the equivalent consumption minimization strategy, which carries out the optimization by minimizing the instantaneous energy consumption at each step [18]-[21]. The Pontryagin's minimum principle (PMP) is another approach, which carries out the optimization by solving nonlinear secondorder differential equations and reduces the computation time

[21]-[23]. Those approaches could achieve near optimality, i.e., a local solution rather than a global solution.

As the reliable future driving conditions improves the optimization performance, model predictive control methods can be employed to predict driving conditions for the near future [9], [24]. Rule-based approaches with multiple objectives [25] and stochastic dynamic programming without requiring driving cycle knowledge a priori [26] have been proposed. Intelligent control techniques such machine-learning algorithms for predicting driving environments and optimizing the power split [27] or neural network modules trained with information on the trip length and duration [10] have been adopted for real-time optimization.

Owing to the development in global positioning systems (GPSs), communications, and sensors, reliable trip information such as the trip length and traffic data such as current and historical speed data can be obtained [28]-[30]. Therefore, research efforts to integrate energy management strategies with these have been made. Driving cycles are estimated using historical speed data [17] or by comparing the GPS trajectory with stored commuting routes [31]. The control parameters are adjusted by the future road terrain in the map and future velocity estimated from traffic speed data [32]. The future recuperable energies estimated by using the topographic profile and average speeds of the trip [33] and real-time traffic data gathered by traffic monitor systems [34] are used to synthesize the SOC reference trajectory. Accordingly, their performance exhibits large dependency on the length and accuracy of the estimated future driving cycle.

Therefore, energy management approaches based on hierarchical control scheme have been applied to manage the complexity of the optimization problem, reduce the computation time, and improve the performance from a global perspective [34]-[36]. The first level generates the optimal SOC profile for a driving cycle based on traffic data, and the second level performs the actual power management in the short-term [34]-[36]. The top layer generates optimal speed and battery energy trajectories, the middle layer determines the gear and engine switch on/off, and the lower layer distributes the acceleration request between the constituent power sources [37]. Certain approaches manage the problem in spatial domain to take advantage of the positioning function of GPS and/or carry out the computation efficiently [35]-[37].

However, SOC and vehicle speed trajectories obtained in time domain [34] cannot act as references after traffic conditions change, which frequently does. As energy consumption depends on the characteristics of the drivetrain as well as the operation conditions according to trip and traffic conditions and driving patterns [38]-[40], driving cycles following only current or historical traffic data [34]-[36] cannot guarantee the most efficient driving for vehicles with different drivetrains. Moreover, owing to the unpredictability of traffic conditions, effective realtime energy management is not available if it does not adapt to changes in traffic conditions [37], while driving.

In order to extend the advantages of hierarchical control and overcome these limitations of real-time energy management, this paper proposes a distance-based energy management strategy with a two-stage hierarchy for power-split PHEVs, which optimizes its driving cycle in a distance domain. Hierarchical control schemes which handle energy management in a time domain cannot maintain the optimality under changeable traffic conditions, while the proposed strategy overcomes this limit by
using distance-based managements. Existing spatial-domain hierarchical strategies don't take changes in traffic conditions and differences in drivetrain of a vehicle into account. The proposed strategy provides the adaptation scheme for traffic conditions and more energy efficient managements based on the characteristics of the drivetrain.

Before departure, the first stage of the proposed strategy optimizes the vehicle speed and SOC profiles in the long-term by taking the characteristics of the drivetrain and trip and traffic information into account. While driving, the second stage regulates the control variables such as engine and motor torques for a short horizon by using the optimized profiles as references and adapts the variables to changes in local traffic conditions. The proposed distance-based optimization benefits from localizing the effects of changes in traffic conditions and maintaining the effectiveness of optimized profiles, except in areas undergoing the changes.

The main contributions of this paper are as follows:

1) Optimize the long-term speed and SOC profiles in a distance domain by considering the characteristics of the drivetrain along with the trip and traffic information, which facilitates more energy-efficient driving by combining ecological driving with energy management;
2) Apply an en-route adaptation framework in a short distance domain to reliably respond to real-time traffic conditions on the basis of the long-term optimal speed and SOC profiles; this localizes the effects of the changes in traffic conditions;
3) Consequently, improve the balance between the optimality from a global perspective and the computing load for real-time implementation, by applying a hierarchical scheme with a local adaptation stage and long-term optimal reference profiles in a distance domain.
The remainder of this paper is organized as follows. In Section II, constituent systems of power-split PHEVs are modeled. Section III presents a distance-based, hierarchical energy management scheme. In Section IV, simulation results for each stage are analyzed, and discussions and conclusions are presented in Section V.

## II. Vehicle Model for Control

For the accurate estimation of energy consumption, models for constituent systems such as fuel consumption in an engine, efficiencies of a motor and a generator, etc. are constructed for a power-split midsize gasoline type PHEV. Their performance data are obtained from Autonomie, simulation software for vehicle energy consumption and performance analysis developed by Argonne National Laboratory in collaboration with automotive manufacturers [41], [42].

## A. Constituent System Models

Fig. 1 shows a drivetrain configuration of a power-split PHEV. A power-split PHEV is equipped with two propulsion sources such as an engine and a motor, which are combined through a planetary gear set. The engine and generator are connected to the planet carrier and the sun gear of the planetary gear set, respectively. The motor is connected through the torque coupler to the ring gear. The battery supplies the auxiliary power for electrical accessories, which is not taken into account.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Drivetrain of a power-split PHEV.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Comparison of fuel efficiency maps.

The fuel rate $\dot{m}_{f}$ in the engine exhibits a piecewise linear relationship with the engine torque $T_{e n g}$ for a fixed angular speed $\omega_{\text {eng }}$ and a linear relationship with the angular engine speed for a fixed engine torque. Therefore, based on the Willans line approximation [43], the fuel rate can be modeled by

$$
\dot{m}_{f}=\left\{\begin{array}{c}
\left(\alpha_{11} \omega_{e n g}+\alpha_{12}\right) T_{e n g}+\left(\alpha_{21} \omega_{e n g}+\alpha_{22}\right) \text { for } 0 \\
\leq T_{e n g} \leq T_{t h} \\
\left(\alpha_{31} \omega_{e n g}+\alpha_{32}\right) T_{e n g}+\left(\alpha_{41} \omega_{e n g}+\alpha_{42}\right) \text { for } T_{e n g} \\
\geq T_{t h}
\end{array}\right.
$$

where $\alpha_{11}=7.1043 \times 10^{-8}, \alpha_{12}=5.7935 \times 10^{-7}, \alpha_{21}=9.0764$ $\times 10^{-7}, \alpha_{22}=-5.6741 \times 10^{-5}, \alpha_{31}=4.3780 \times 10^{-8}, \alpha_{32}=$ $1.9087 \times 10^{-6}, \alpha_{41}=2.3818 \times 10^{-6}, \alpha_{42}=-2.1087 \times 10^{-4}$, and $T_{t h}=46.8573$.

Fig. 2 compares fuel rates estimated by the model with original data given by Autonomie for diverse engine torques and speeds. The solid and dashed lines represent the Autonomie and estimated data. This comparison shows that the model is acceptable for estimation of the fuel rate.

A state-of-charge (SOC) in a battery is the main parameter that determines the electrical power performance such as maximum charging and discharging power. If a battery is modeled as a series combination of an open-circuit voltage and an internal
![img-2.jpeg](img-2.jpeg)

Fig. 3. Open-circuit voltage and internal resistance of a battery.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Maximum charging and discharging power.
resistance, $S O ́ C$ can be represented by

$$
S O ́ C=\frac{d S O C}{d t}=-\frac{V_{o c}-\sqrt{V_{o c}^{2}-4 R_{\text {batt }} P_{\text {batt }}}}{2 Q_{\text {batt }} R_{\text {batt }}}
$$

where $\mathrm{V}_{\mathrm{oc}}, \mathrm{R}_{\text {batt }}$, and $\mathrm{Q}_{\text {batt }}$ are the battery open-circuit voltage, internal resistance, and capacity, respectively. $\mathrm{P}_{\text {batt }}$ is the battery power, which is the sum of the powers of the motor and generator and can be described by

$$
P_{\text {batt }}=T_{\text {mot }} \omega_{\text {mot }}\left(\eta_{\text {mot }} \eta_{\text {inv }}\right)^{l}+T_{\text {gen }} \omega_{\text {gen }}\left(\eta_{\text {gen }} \eta_{\text {inv }}\right)^{l}
$$

where $\mathrm{T}_{\text {mot }}, \mathrm{T}_{\text {gen }}, \omega_{\text {mot }}, \omega_{\text {gen }}, \eta_{\text {mot }}$, and $\eta_{\text {gen }}$, are the torques, speeds, and efficiencies, respectively, of the motor and generator. $\eta_{\text {inv }}$ is the efficiency of the power converter. The superscript $l$ indicates whether the motor (or generator) is charging or discharging. Its value becomes ' 1 ' on charging and ' -1 ' on discharging.

In (2), the derivative of an SOC is a function of $\mathrm{V}_{\text {oc }}$ and $\mathrm{R}_{\text {batt }}$, which are also dependent on the value of the SOC. The blue lines in Fig. 3 denote the dependencies of the battery open-circuit voltage and internal resistance on the SOC. The dependencies are modeled in a normal operating range of the SOC larger than 0.2. In the left panel, the open circuit voltage $\mathrm{V}_{\text {oc }}$ is modeled as a linear function of the SOC, which is indicated by red circles. In the right panel, the dependency of the internal resistance is modeled by two quadratic equations for two regions of the SOC value smaller or larger than 0.6 . The models for $\mathrm{V}_{\text {oc }}$ and $\mathrm{R}_{\text {batt }}$ exhibit reasonable agreement with the dependencies, which are similar with a non-linear static model [44].

The maximum charging and discharging power in a battery is also strongly dependent on the SOC value, as shown in Fig. 4. With respect to the battery, the charging power is represented by a negative value and the discharging power by a positive value.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Efficiencies of a motor and a generator.
The maximum charging and discharging powers are modeled as a quadratic function and a linear function, respectively, of the SOC value. The red circles indicate the values estimated using the models, which are in reasonable agreement with the original data.

The efficiencies of a motor, a generator, and a power converter which are represented by $\eta_{\text {mot }}, \eta_{\text {gen }}$, and $\eta_{\text {inv }}$ in (3) also depend on the speed and torque although those dependencies are smaller than that of an engine. The left and right panels of Fig. 5 show $\eta_{\text {mot }}$ and $\eta_{\text {gen }}$, respectively. $\eta_{\text {inv }}$ shows the similar dependency. As their shapes are difficult to model with simple equations, the efficiencies are listed in lookup tables for diverse speed and torques. The efficiencies of a final drive, a torque coupler, and a planetary gear set are modeled as constants, namely $0.97,0.97$, and 0.98 , respectively.

## B. Vehicle Propulsion Model

Based on a quasi-static approach, the drivetrain model of a power-split type PHEV has been developed. Omitting the inertial loss of the engine, motor, and generator, the relationship between the torques in the planetary gear set can be obtained as follows:

$$
\begin{aligned}
& 0=T_{g e n}+F \cdot N_{s} \\
& 0=T_{e n g}-F \cdot N_{s}-F \cdot N_{r} \\
& 0=T_{m o t(T C)}-\frac{T_{o u t}}{f_{r} \eta_{p g}}+F \cdot N_{r}
\end{aligned}
$$

where $F$ represents the interaction force between the different gears; and $N_{s}$ and $N_{r}$ are the radii of the sun gear and ring gear, respectively. $T_{\text {out }}$ is the drivetrain output torque, $f_{r}$ is the gear ratio of the final drive, and $\eta_{p g}$ is the efficiency of the planetary gear set. $T_{\text {mot }(P C)}$ is the torque that is transferred from the motor through the torque coupler and is expressed as

$$
T_{\text {mot }(P C)}=G R_{T C} \cdot \eta_{T C} \cdot T_{\text {mot }}
$$

where $G R_{T C}$ and $\eta_{T C}$ are the gear ratio and efficiency of the torque coupler, respectively.

From (4) and (5), the output torque $T_{\text {out }}$ is expressed as

$$
T_{\text {out }}=f_{r} \eta_{p g}\left(T_{\text {eng }}+T_{\text {gen }}+G R_{T C} \cdot \eta_{T C} \cdot T_{\text {mot }}\right)
$$

As the torque of the generator exhibits the following relationship with the torque of the engine

$$
T_{\text {gen }}(t)=-T_{\text {eng }}(t) \frac{N_{s}}{N_{s}+N_{r}}=-T_{\text {eng }}(t) \frac{Z}{Z+1}
$$

TABLE I
PARAMETERS OF THE VENICE MODEL

| Symbol | Quantity | Value | Unit |
| :--: | :--: | :--: | :--: |
| $\mathrm{R}_{w}$ | Wheel radius | 0.317 | m |
| m | Mass | 1470 | kg |
| $\rho$ | Air density | 1.19854 | $\mathrm{kg} / \mathrm{m}^{3}$ |
| $\mathrm{C}_{d}$ | Air drag coefficient | 0.3 | - |
| $\mathrm{A}_{d}$ | Frontal area | 2.2508 | $\mathrm{m}^{2}$ |
| g | Gravity | 9.81 | $\mathrm{m} / \mathrm{s}^{2}$ |

where $\mathrm{Z}=\frac{N_{s}}{N_{r}}, T_{\text {out }}$ can be expressed as

$$
T_{\text {out }}=f_{r} \eta_{p g}\left(\frac{1}{Z+1} T_{\text {eng }}+G R_{T C} \cdot \eta_{T C} \cdot T_{\text {mot }}\right)
$$

Then, a wheel force $F_{w}$ for propelling a vehicle is expressed as

$$
\begin{aligned}
F_{w}(t)= & \frac{T_{\text {out }}(t)}{R_{w}}=m \dot{v}(t)+\frac{1}{2} \rho C_{d} A_{d} v(t)^{2} \\
& +m g C_{r} \cos \theta(t)+m g \sin \theta(t)+F_{\text {brake }}(t) \\
\therefore \dot{v}(t)= & \frac{T_{\text {out }}(t)}{m R_{w}}-\frac{1}{m} F_{\text {brake }}(t)-\frac{1}{2 m} \rho C_{d} A_{d} v(t)^{2} \\
& -\mathrm{g} C_{r} \cos \theta(t)-g \sin \theta(t)
\end{aligned}
$$

where $v(t), \dot{v}(t), \theta(t)$, and $\mathrm{F}_{\text {brake }}(t)$ are the speed of the vehicle $(\mathrm{m} / \mathrm{s})$, its acceleration $\left(\mathrm{m} / \mathrm{s}^{2}\right)$, the road gradient (rad), and the brake force ( N ), respectively. The rolling resistance coefficient, $C_{r}$, is modeled as a linear function of the engine speed. The other parameters and their values are listed in Table I.

Let the time at the $k^{\text {th }}$ time step and the time interval between adjacent time steps be $\mathrm{t}_{\mathrm{k}}$ and $\Delta \mathrm{t}_{\mathrm{k}}$, respectively. Then, the speed at the $(k+1)^{\text {th }}$ time step is expressed as

$$
\begin{aligned}
v\left(t_{k+1}\right)= & v\left(t_{k}\right)+\dot{v}\left(t_{k}\right) \Delta t_{k} \\
= & \left(1-C_{1} v\left(t_{k}\right) \Delta t_{k}\right) v\left(t_{k}\right) \\
& +\frac{\Delta t_{k}}{m}\left(\frac{T_{\text {out }}\left(t_{k}\right)}{R_{w}}-F_{\text {brake }}\left(t_{k}\right)\right)-C_{2}\left(t_{k}\right) \Delta t_{k}
\end{aligned}
$$

where $C_{1}=\frac{1}{2 m} \quad \rho C_{d} A_{d}$, and $C_{2}\left(t_{k}\right)=g\left(C_{r} \cos \theta\left(t_{k}\right)+\right.$ $\left.\sin \theta\left(t_{k}\right)\right)$.

## III. Distance-BASEd Hierarchical Energy Management STRATEGY USING OptimIZED DRIVING CYCLES

For a reasonable balance between the optimality and real-time computing loads, a distance-based energy management strategy with two stages is proposed. The hierarchical structure of the proposed strategy and its constituent stages are described.

## A. Fundamental Concept

Vehicles with different drivetrain characteristics consume different energies although they are driven at an identical speed profile. Thus, a more effective energy management can be achieved by optimizing the power demands for the characteristics of the

![img-5.jpeg](img-5.jpeg)

Fig. 6. Hierarchical management structure based on the optimal driving cycle generation in a distance domain.
drivetrain and environmental conditions and managing the split of the optimized power demand. The proposed energy management strategy is composed of two stages: optimization of the speed and SOC profiles in the long horizon and their real-time adaptations for the short horizon, which are depicted in Fig. 6.

Prior to departure, the first stage generates the optimal speed profile and SOC profile for a whole trip or its sufficiently long part by considering the characteristics of the drivetrain and the trip and traffic conditions. The road gradient, trip length, and speed limits on the road segments are inputted as trip information. The average traffic speeds of the road segments, if available, are inputted as traffic conditions. Then, the speed profile and SOC profile are optimized to guarantee an optimal balance among fuel consumption, electric power consumption, and driving time. A vehicle will be regulated not to be driven at the given speed profile (such as average speeds) but at the generated optimal speed and SOC profiles, which are called reference profiles.

While driving, the second stage management adapts the vehicle to the reference profiles and change in traffic conditions. The reference speed and SOC profiles, which are the outputs of the first stage, provide target values for short horizon management. However, if the actual speeds for a short horizon, which are assumed to be available through communication or broadcasting, deviate considerably from the reference speeds at the current location, the second stage uses the actual speeds rather than the reference speeds as the target speeds and generates a locally optimal driving profile for the short horizon. The operations of a motor and generator are controlled by the reference SOC values.

As the traffic conditions change very frequently, this adaptation is made only for a horizon that is short enough for the computing time to be suitable for real-time implementation and long enough for energy-efficient driving control.

Moreover, although the first stage is performed before departure, the permitted time for optimization is still limited, and, consequently, the number of segments to be optimized is also limited. For a long trip, the distance step of each segment is likely to become too large to drive the vehicle reliably. Then, the second stage divides a segment in the long-term profile into
several fine segments with a smaller distance step; this results in a more efficient and reliable energy management.

In a time-based strategy, adaptation at any time changes the total driving time, and the reference profiles in the remaining trip route cannot be used as the target values at the corresponding times. Consequently, the reference profiles lose their effectiveness after that time. For optimal energy management, the speed and SOC profiles for the remaining route need to be optimized again; this requires a long computing time. As traffic conditions are changeable, this re-optimization may be repeated while driving; this is not suitable for real-time implementation.

The proposed energy management strategy regulates the vehicle in a distance domain. As the reference profiles are defined for each location of the trip route, adaptation at any location limits its effect in the nearby area, and the reference profiles except in the area can maintain their effectiveness and optimality. Therefore, the distance-based energy management is not required to compute the optimal profiles for the remaining route after the adaptation if the areas undergoing changes in traffic conditions are not large.

In a distance domain, the whole trip is divided into distance segments with a fixed step size of $\Delta \mathrm{s}$, and the control is updated at each location that is $\Delta \mathrm{s}$ distant from its adjacent locations. Let the time, speed and SOC value at the $k^{\text {th }}$ location of the trip $(=k \cdot \Delta s)$ be $t_{k}, v(\mathrm{k})$, and $\mathrm{SOC}(\mathrm{k})$. As the control is updated at each location, the acceleration from the $k^{\text {th }}$ to $(k+1)^{\text {th }}$ locations is constant, and the relationship between the time difference and the distance step can be expressed as

$$
\Delta t_{k}=t_{k+1}-t_{k}=\frac{2 \Delta s}{v(k)+v(k+1)}
$$

Then, by inserting (13) into (12) and multiplying ' $v(k+1)$ $+v(k)$ ' on both the sides, the speed at the $(k+1)^{\text {th }}$ location, $v(k+1)$, can be described by

$$
\begin{aligned}
v(k+1)^{2}= & \left(1-2 C_{1} \Delta s\right) v(k)^{2} \\
& +\frac{2 \Delta s}{m}\left(\frac{T_{\text {out }}(k)}{R_{w}}-F_{\text {brake }}(k)\right)-2 C_{2}(k) \Delta s
\end{aligned}
$$

By inserting (8) into (14),

$$
\begin{aligned}
v(k+1)^{2}= & \left(1-2 C_{1} \Delta s\right) v(k)^{2}+\frac{2 \Delta s}{m}\left(\frac{t_{k} \eta_{p g}}{R_{w}}\right. \\
& \left(\frac{1}{Z+1} T_{\text {eng }}(k)+G R_{T C} \eta_{T C} T_{\text {mot }}(k)\right) \\
& \left.-F_{\text {brake }}(k)\right)-2 C_{2}(k) \Delta s
\end{aligned}
$$

It implies that, for the specified speed at the current location, the speed at the subsequent location is determined by a function of the current speed $v(k)$; control inputs for propulsion such as $T_{\text {eng }}(k), T_{\text {mot }}(k)$, and $F_{\text {brake }}(\mathrm{k})$; and the road conditions $C_{2}(k)$.

As the energy consumption by a PHEV depends on the speeds as well as torques of the propulsion sources, the relationship involving the speeds of the vehicle, engine, generator, and motor is described. In the planetary gear set, the rotational speeds of

the sun gear $\omega_{\mathrm{s}}(k)$, ring gear $\omega_{\mathrm{r}}(k)$, and carrier gear $\omega_{\mathrm{c}}(k)$ at the $k^{\text {th }}$ location satisfy the following relationship:

$$
\omega_{s}(k) N_{s}+\omega_{r}(k) N_{r}=\omega_{c}(k)\left(N_{r}+N_{s}\right)
$$

The engine and generator are connected to the planet carrier and sun gears, that is, $\omega_{\text {eng }}(k)=\omega_{\mathrm{c}}(k)$ and $\omega_{\text {gen }}(k)=\omega_{\mathrm{s}}(k)$. The motor is connected to the ring gear through the torque coupler such that its rotational speed is expressed as

$$
\omega_{\text {mot }}(k)=G R_{T C} \omega_{r}(k)
$$

and can be determined using the following relationship

$$
\omega_{r}(k)=\frac{f_{r}}{R_{w}} v(k)
$$

If two rotational speeds in (16) are specified, the remaining speed can be determined. The motor speed is determined by the vehicle speed according to (17) and (18). In (15), the engine speed does not affect the subsequent speed control; however, it exerts a large effect on the fuel efficiency; therefore, it is selected as a control input. Then, the generator speed is derived by the engine speed and motor speed as follows;

$$
\omega_{\text {gen }}=\omega_{\text {eng }}\left(1+\frac{N_{r}}{N_{s}}\right)-\omega_{\text {mot }} \frac{1}{G R_{T C}} \frac{N_{r}}{N_{s}}
$$

In this study, the engine speed is allowed to be zero; this implies that the engine is turned off, and no fuel is consumed. In the case of zero engine speed, the engine torque is also set to be zero. Thus, a separate engine on/off control is not required.

Therefore, the control input $u(k)$ is set as

$$
u(k)=\left[T_{\text {eng }}(k), \omega_{\text {eng }}(k), T_{\text {mot }}(k), F_{\text {brake }}(k)\right]^{T}
$$

where the superscript T represents the transpose matrix. By replacing $v(k)^{2}$ and $v(k+1)^{2}$ with $X(k)$ and $X(k+1)$, (15) can be described by

$$
X(k+1)=A(k) X(k)+B(k) u(k)+D(k)
$$

where $A(k)=\left(1-2 \Delta s C_{1}\right), \mathrm{B}(\mathrm{k})=\frac{2 \Delta s}{m}\left[\frac{f_{r} \eta_{r s}}{R_{w}(Z+1)}, 0, \frac{f_{r} \eta_{r s}}{R_{w}}\right.$ $\left.G R_{T C} \eta_{T C},-1\right]$, and $D(k)=-2 \Delta s C_{2}(k)$.

## B. Optimal Speed and SOC Profiles in Long Horizon

The energy efficiency in a PHEV depends on the management of the two propulsion sources as well as the manner in which the vehicle is driven; this in turn determines the power demand. If the vehicle is driven in a manner that is optimal for its drivetrain under specified trip conditions, higher energy efficiency can be obtained. Thus, the optimal driving pattern for a whole trip is generated for the characteristics of drivetrain and trip conditions. The whole trip length, road gradients, speed limits, and average speeds, if available, at each location are used as trip conditions.

The resulting optimal driving pattern includes the speed profile and SOC profile, which list the speed and SOC values at each location of the trip. Driving at a low speed results in low energy consumption and long driving time, which is not desirable for actual driving. Therefore, the optimal speed profile should keep an adequate balance between the energy consumption and driving time. The energy consumption in a PHEV includes both fuel and battery energy consumption. The optimal SOC profile regulates effectively the split between fuel and battery powers while satisfying the power demand required by the optimal speed profile.

The whole trip is composed of $n$ segments, whose step size is $\Delta \mathrm{s}$. The cost function $J_{\text {long }}$ for optimizing the driving pattern is described by

$$
\begin{aligned}
J_{\text {long }}= & w_{1} \sum_{k=0}^{n-1} \dot{m}_{f}(k) \Delta t_{k}+w_{2} \sum_{k=0}^{n-1} P_{\text {batt }}(k) \Delta t_{k} \\
& +w_{3} \sum_{k=0}^{n-1}\left(v(k+1)^{2}-v_{\text {target }}(k+1)^{2}\right)^{2} \Delta t_{k} \\
= & \sum_{k=0}^{n-1}\left(w_{1} \dot{m}_{f}(k)+w_{2} P_{\text {batt }}(k)+w_{3}(v(k+1)^{2}\right. \\
& \left.-v_{\text {target }}(k+1)^{2}\right)^{2}\right) \frac{2 \Delta s}{v(k+1)+v(k)}
\end{aligned}
$$

where constants $w_{1}, w_{2}$, and $w_{3}$ are weights for balancing the three terms. On the right side of (22), the first and second terms represent the fuel and battery consumption, respectively. The third term represents the speed deviation from the target speed $V_{\text {target }}(\mathrm{k})$ at each location. An average speed, if available, or a speed limit is used as the target speed. The third term makes the vehicle speed close to the target speed and results in a balanced driving time.

This optimization is subject to inequality constraints caused by characteristics of the constituent systems:

$$
\begin{aligned}
T_{\text {eng }(\min )} & \leq T_{\text {eng }}(k) \leq T_{\text {eng }(\max )} \\
T_{\text {mot }(\min )} & \leq T_{\text {mot }}(k) \leq T_{\text {mot }(\max )} \\
F_{\text {brake }(\min )} & \leq F_{\text {brake }}(k) \leq F_{\text {brake }(\max )} \\
\omega_{\text {eng }(\min )} & \leq \omega_{\text {eng }}(k) \leq \omega_{\text {eng }(\max )} \\
\omega_{\text {mot }(\min )} & \leq \omega_{\text {mot }}(k) \leq \omega_{\text {mot }(\max )} \\
P_{\text {mot }(\min )} & \leq P_{\text {mot }}(k) \leq P_{\text {mot }(\max )} \\
P_{\text {batt_charge }(\max )}(S O C(k)) & \leq P_{\text {batt }}(k) \\
& \leq P_{\text {batt_dsicahra }(\max )} \\
(S O C(k)), S O C_{\min } & \leq \operatorname{SOC}(k) \leq S O C_{\max } \\
v(k) & \leq \text { speed limit }(k) \\
v(n) & =0
\end{aligned}
$$

where $\mathrm{P}_{\text {batt_charge(max) }}$ represents the maximum charging power, which is a negative number; and $\mathrm{P}_{\text {batt_discharge(max) }}$ represents the maximum discharging power, which is a positive number. Both are functions of the SOC value, as shown in Fig. 4.

As shown in (23) and (24), the cost function is nonlinear and imposes complex constraints. In addition, the allowable computing time is still limited, although this long-term optimization is performed before departure. Thus, an estimation of distribution algorithm (EDA) is used as an optimization algorithm, which builds a probability distribution from promising populations of the previous ones and generates new populations by using the probability distribution [45]-[48]. This probabilistic approach speeds up the optimization process such that it is suitable to solve the cost function for the energy management of PHEVs. An EDA has been applied to the ecological driving of a conventional vehicle and online energy management for plug-in HEVs and exhibits good optimization performance [49], [50].

![img-6.jpeg](img-6.jpeg)

Fig. 7. Flowchart of the long-term optimization stage.

An EDA randomly generates a predefined number of samples of control inputs, which are called populations and computes the values of the cost function for all the populations. Then, the populations with smaller values of the cost function are selected, whose number is determined by $n_{\text {pop }} \times t_{r}$ where $n_{\text {pop }}$ is the number of populations and $t_{r}$ is the predefined truncation ratio. The probability distribution features such as the average value and standard deviation are obtained from the selected populations. Based on the probability distribution features, new populations are randomly generated and replace the unselected previous populations. Among the selected and newly generated populations, those with smaller cost functions are selected again, and this process is repeated for a predefined number of iterations.

Because of the preferable rapid optimization, an approach for a shorter computing time based on promising initial populations and the combination of a small truncation ratio and a large number of populations, are adopted; this was proposed in [49].

The inequality constraints in (24) are implemented by selecting values of the control input variables when building the populations. Then, the constraints on the SOC and vehicle speed are implemented by assigning large penalties to the values that violate the constraint.

Fig. 7 shows the long-term optimization process by using an EDA. In this study, promising initial populations instead of random initial populations were generated by using the models of the drivetrain and a speed profile where speeds are linearly accelerated or decelerated at speed transient regions and speeds at other regions are set to the speed limits. Promising populations generated in the initial iteration obviate the requirement for iteration from randomly generated populations to the current promising ones and speed up the optimization.

As the truncation ratio becomes smaller, more populations are replaced by promising populations at each iteration and the value of the cost function tends to reduce rapidly if the probability distribution features obtained from the selected populations adequately reflect the features of the optimal solution. Thus, it is important to guarantee that promising populations are incorporated in generated populations at early iterations and that the selected populations reflect the features of the optimal solutions; this is more probable with a large number of populations.

As each iteration can be computed at a time by matrix calculation, the computing time is not linearly proportional to the number of population. However, it linearly increases with the
![img-7.jpeg](img-7.jpeg)

Fig. 8. Flowchart of the local adaptation stage.
number of iteration. In this study, the truncation ratio is set to be 0.2 and the number of populations is 800 . This small truncation ratio with a sufficiently large number of populations reduces the iteration number and speeds up the optimization.

The number of distance steps in a driving cycle is another parameter to determine the computing time, which is the ratio of the trip length to a step size. Since they are linearly proportional, a large step size is preferable from the viewpoint of the computing time. However, the operating condition within a segment with a large step size may deviate significantly from the initial one and a small step size is preferable to reliable results. Thus, the size and number of distance steps are set to balance them.

## C. Local Adaptation to Variations in Traffic Conditions

While driving, a vehicle will be constrained to follow the reference speed and SOC value at each location, which are obtained from the first stage. However, as traffic conditions are highly changeable, the optimal reference speeds occasionally need to be adapted to the changes in traffic conditions. It is preferable to make this adaptation locally as it may be repeated owing to frequent changes in traffic and should be made in real time. If the area under heavy traffic conditions is not too long, the distance-based SOC profile is still optimal in the long term. Thus, it regulates effectively the power split for the adapted target speeds, that is, the adapted power demands.

For a long trip, the length of a segment in the long-term optimal profiles, $\Delta \mathrm{s}$, becomes large, which may not reflect the variations in characteristics of the drivetrain and the constituent parts within the segment. For instance, the driving time of a 200 m long segment ranges up to 40 seconds and may be too long to cope with variations in real-time traffic conditions. Since the control is updated at each location, it is kept to be constant over the segment and the operating conditions within the segment may deviate from ones at the starting location of the segment.

Consequently, the resulting profiles result in suboptimal or practically unreliable driving, and more fine controls are required for shorter steps. Therefore, if necessary, the second stage divides each segment in the long-term optimal profile into several fine segments with a smaller step size and adapts them to changes in traffic conditions for a short horizon.

Fig. 8 describes the local adaptation process. The average speed is used as the real-time traffic condition at each location.

The reference speeds at the next several locations are compared with the actual average speeds. If the reference speeds are equal to or lower than the actual average speeds, the target speeds at the next locations are set to be the reference speeds. However, if the actual speeds are lower than the reference speeds, the target speeds are changed into the actual speeds.

Let the number of the long-term segments within the short horizon be $n_{s}$, the number of the fine segments for each longterm segment be $n_{\mathrm{f}}$, and the step size of the fine segment be $\Delta s_{f}\left(=\frac{\Delta s}{n_{f}}\right)$. The cost function for local adaptation $J_{\text {local }}$ at the $\mathrm{m}^{\text {th }}$ location in the long-term profile is defined by

$$
\begin{aligned}
& J_{\text {local }}(m)=\sum_{k=0}^{n_{s}-1}\left(\sum_{i=0}^{n_{f}-1}\left(w_{1} \dot{m}_{f}(m+k, i) \Delta t_{i}\right.\right. \\
& \left.\left.+w_{2}\left(S O C_{\text {fine }}(m+k, i)-S O C_{\text {target }}(m+k+1)\right)^{2} \Delta s_{f}\right.\right. \\
& \left.\left.+w_{3}\left(v_{\text {fine }}(m+k, i)^{2}-v_{\text {target }}(m+k+i)^{2}\right)^{2} \Delta s_{f}\right)\right)
\end{aligned}
$$

where $\dot{m}_{f}(l, i), v_{\text {fine }}(l, i), S O C_{\text {fine }}(l, i)$ are the fuel consumption, vehicle speed, and state-of-charge at the $\mathrm{i}^{\text {th }}$ fine location in the $f^{\text {th }}$ long-term segment, that is, at the $\left(l \times \Delta \mathrm{s}+\mathrm{i} \times \Delta s_{f}\right)^{\text {th }}$ location. $V_{\text {target }}(l)$ is the target speed at the $(l \times \Delta \mathrm{s})^{\text {th }}$ location in the whole trip. $\Delta t_{i}\left(=\frac{2 \Delta \mathrm{~S}_{i}}{v(l+1)+v(l)}\right)$ is the time interval between time steps adjacent to the $\mathrm{i}^{\text {th }}$ fine location. The first term represents the fuel consumption at each fine location, and the second and third terms represent the deviations from the SOC value and target speed, respectively.

This short horizon adaptation is also subject to inequality constraints caused by characteristics of the constituent systems:

$$
\begin{aligned}
T_{\text {eng(min) }} & \leq T_{\text {eng }}(i) \leq T_{\text {eng(max) }}, \\
T_{\text {mot(min) }} & \leq T_{\text {mot }}(i) \leq T_{\text {mot(max) }}, \\
F_{\text {brake(min) }} & \leq F_{\text {brake }}(i) \leq F_{\text {brake(max) }}, \\
\omega_{\text {eng(min) }} & \leq \omega_{\text {eng }}(i) \leq \omega_{\text {eng(max) }}, \\
\omega_{\text {mot(min) }} & \leq \omega_{\text {mot }}(i) \leq \omega_{\text {mot(max) }} \\
P_{\text {mot(min) }} & \leq P_{\text {mot }}(i) \leq P_{\text {mot(max) }}, \\
P_{\text {batt_charge(max) }}\left(S O C_{\text {fine }}(l, i)\right) & \leq P_{\text {batt }}(l, i) \\
& \leq P_{\text {batt_dsiccabrgc(max) }} \\
\left(S O C_{\text {fine }}(l, i)\right) S O C_{\text {min }} & \leq \mathrm{SOC}_{\text {fine }}(l, i) \leq S O C_{\text {max }}, \\
v_{\text {fine }}(m+k, i) & \leq \text { speed limit }(m+k+1) \\
v_{\text {fine }}\left(n-n_{s}, n_{s} \times n_{f}\right) & =0
\end{aligned}
$$

The cost function is also nonlinear with complex constraints such that the optimal adaptation is obtained by using an EDA.

## IV. SimULATIONS

The proposed distance-based energy management scheme with two-stages was implemented using MATLAB, and a series of simulations were conducted for the long-term optimization and local adaptation. The dependency of the three weight values, $\omega_{1}, \omega_{2}$, and $\omega_{3}$, was simulated, and the long-term driving profiles were optimized for the selected weight values. Then, the resulting energy consumption was compared with that of a

TABLE II
EFFECTS OF $\mathrm{W}_{1}$ VALUES

|  | $w_{i}=10^{7}$ | $w_{i}=3 \times 10^{7}$ | $w_{i}=5 \times 10^{7}$ | $w_{i}=7 \times 10^{7}$ |
| :--: | :--: | :--: | :--: | :--: |
| Fuel consumption (g) | 44 | 7 | 0 | 0 |
| SOC final value | 0.403 | 0.423 | 0.430 | 0.430 |
| Driving time (s) | 2013 | 2014 | 2014 | 2014 |

vehicle driven at the given speed profile. In local adaptation, smooth and heavy traffic conditions were simulated.

The parameter values used in the simulations are as follows: $T_{\text {eng }(\max )}=220(\mathrm{~N} \cdot \mathrm{~m}), T_{\text {mot }(\max )}=175.4(\mathrm{~N} \cdot \mathrm{~m})$, $T_{\text {mot }(\min )}=-175.4 \quad(\mathrm{~N} \cdot \mathrm{~m}), \mathrm{P}_{\text {brake }(\max )}=3120 \quad(\mathrm{~N} \cdot \mathrm{~m})$, $\omega_{\text {eng }(\max )}=500(\mathrm{rad} / \mathrm{s}), \omega_{\text {eng }(\min )}$ during operation $=$ $100 \quad(\mathrm{rad} / \mathrm{s}), \omega_{\text {eng }(\min )}=0 \quad(\mathrm{rad} / \mathrm{s}), \quad$ and $\quad \omega_{\text {mot }(\max )}=$ $1500(\mathrm{rad} / \mathrm{s}), \omega_{\text {eng }(\min )}$ during operation represents the minimum engine speed while the engine is operational, and ${ }^{\prime} \omega_{\text {eng }}=0^{\prime}$ represents the switched off engine condition.

## A. Generation of Optimal Speed and SOC Profiles in the Long Term

The optimization of the cost function in (23) is dependent on the values of its weight parameters, $w_{1}, w_{2}$, and $w_{3} . w_{1}$ and $w_{2}$ determine the relative priority between the engine and motor as a propulsion source. A widely used method to determine their values is based on the evaluation of the fuel equivalent to the consumed electricity according to their market prices [31]-[33]. In this study, the environmental effect of the exhaust gas is considered such that the motor takes priority over the engine unless the electric power of the battery is used up. That is, if the trip can be covered by the current battery capacity, a vehicle is driven by only the electric power without consuming fuel. The battery capacity is assumed to be 25 Ah , and its allowable minimum limit of the SOC is set to be 0.3 . In order to obtain this optimization priority, the initial state-of-charge is set to 0.9 ; moreover, the trip under test is 40 km long, shorter than allelectric range. Then, simulations for diverse values of $w_{1}$ were carried out with a fixed value of $w_{2}=1 . w_{3}$ is set to 1 , which guarantees that the resulting speeds follow the target speeds adequately.

Table II lists the important driving results such as fuel consumption, final SOC value, and driving time. The distance step is 200 m , and the total number of locations is 201 . It is demonstrated that for values of $w_{1}$ lower than $5 \times 10^{7}$, fuel was consumed although the SOC value did not attain the minimum limit, and the driving times are almost equal. Thus, the values of $w_{1}$ and $w_{2}$ are set to be $5 \times 10^{7}$ and 1 , respectively.

Then, $w_{3}$ determines how closely the target speed is to be followed at each location and, consequently, the balance between the driving time and the total energy consumption including both fuel and electric energies. The initial SOC value is set to be 0.6 , and a $40-\mathrm{km}$-long trip is tested. Simulations for diverse values of $w_{3}$ were carried out with fixed values of $w_{1}=5 \times 10^{7}$ and $w_{2}=1$ based on the previous simulation results. In all of the simulations, the final SOC values reached 0.3 , which is the allowable minimum limit.

Fig. 9 shows the driving results of the long-term speed profiles optimized for diverse $w_{3}$ values. The solid red and dotted blue lines represent the fuel consumption and driving time,

![img-8.jpeg](img-8.jpeg)

Fig. 9. Effects of $w_{3}$ values.
respectively. It is demonstrated that there is a trade-off between fuel consumption and driving time. As $w_{3}$ increases, the optimized speed profile becomes closer to the target speed, which results in larger fuel consumption and shorter driving time. The speed profile optimized using a lower value of $w_{3}$ consumes less fuel and requires a long driving time; this is not suitable as a vehicle driven at such low speeds hinders a smooth flow of traffic. In this study, the weight parameters, $w_{1}, w_{2}$, and $w_{3}$, are set to be $5 \times 10^{7}, 1$, and 2 , respectively, which makes the speed deviation less than $1 \%$.

In order to check the convergence tendency, simulations were carried out for diverse number of iterations which ranged from 100 to 10,000 . The values of the cost function at iterations more than 6,000 converge within $2 \%$ from the final value. Considering the decrease in the value of the cost function and the increase in the computing time, the number of iterations is set to be 6,000 for long-term optimization.

The proposed energy management strategy generates the optimal speed and SOC profiles and then controls the operation of two propulsion sources on the basis of the optimal profiles. In order to verify the advantage of these optimal profiles, a vehicle was regulated to be driven at the given speed profile without optimization, and the driving results were compared with those of the optimized speed profile. The optimal speed profile was generated from the target speed at each location by applying the set of the weight parameter selected above, and the target speeds were used as the given though not optimized speed profile. More precisely, for comparison by using an identical process, the speed profile that was obtained by a large value of $w_{3}$ to tie in closely with the target speeds was used as the given speed profile.

The upper and lower panels of Fig. 10 compare their speed profiles and SOC profiles, respectively, in a distance domain. In each panel of Fig. 10, the red solid and blue dotted lines represent the given and optimal profiles, respectively. The optimized speed profile does not exhibit large deviations from the given speed profile except in the last deceleration area of the trip. The initial SOC level is 0.6 . The battery is charged while driving at relatively low speeds of approximately $17 \mathrm{~m} / \mathrm{s}$ and deceleration, and discharged at relatively high speeds of approximately $22 \mathrm{~m} / \mathrm{s}$ and $28 \mathrm{~m} / \mathrm{s}$, attaining the lower limit towards the end of the trip. The computing time of this optimization was 473 s with an Intel i7-8700K core at a frequency of 3.7 GHz .
![img-9.jpeg](img-9.jpeg)

Fig. 10. Comparison of the given and optimized speed profiles.

TABLE III
COMPARISON OF THE DRIVING RESULTS

|  | Given speed profile | Optimized speed profile |
| :-- | :--: | :--: |
| Fuel consumption (g) | 751 | 623 |
| Final SOC value | 0.311 | 0.309 |
| Driving time (s) | 2054 | 2077 |

Table III presents the driving results: fuel consumption, final SOC levels, and driving times. Driving at the optimal speed profile consumes fuel of 623 g and takes 2077 s . On the other hand, fuel consumption and a driving time while driving at the given speed profile are 751 g and 2054 s , respectively. The driving based on the generated optimal speed profile consumes fuel less by $17.0 \%$, whereas its driving time increases by $1.1 \%$ in comparison with driving at the given speed profile. Therefore, a significantly better balance between fuel consumption and driving time is achieved by optimal-speed-based energy management.

The operation points from the given and optimal speed profiles are drawn on a fuel efficiency map in Fig. 11. The ' $x$ ' and ' $o$ ' marks represent the operation points while driving at the given and optimal speed profiles, respectively. The color bar on the right side represents fuel consumption in grams. Thus, the lower-left area corresponds to the fuel efficient-driving condition. It is revealed that almost all the operation points from the optimal speed profile were concentrated around the narrow range in the lower-left area. Although the operation points from the given speed profile were located in the left area, they were spread relatively widely, and more number of operations were carried out at higher engine speeds and larger engine torques.

## B. Local Adaptation to Variations in Traffic Conditions

The local adaption is carried out for speeds at fine segments within a short horizon to follow the reference speeds specified by the long-term speed profile and adapt to change in

![img-10.jpeg](img-10.jpeg)

Fig. 11. Engine operation points from the given and optimal speed profiles.
traffic conditions in an energy efficient manner. These adaptation results are also dependent on the values of $w_{1}, w_{2}$, and $w_{3}$ in (25), and similar to the long-term optimization, simulations with diverse weight values were conducted. The values of $w_{1}=5 \times 10^{6}, w_{2}=10^{7}$, and $w_{3}=1$ are selected, which guarantee that the locally adapted speeds and SOC values agree with the long-term profiles.

The number of the long-term segment within the short horizon, $n_{s}$, is set to be 2 , which implies that the short horizon is $400-\mathrm{m}$-long. The number of fine segments for each long-term segment, $n_{\mathrm{f}}$, is four, and, consequently, the step size of the fine segment $\Delta s_{f}$ becomes 50 m . It is assumed that the current average speed at each segment of the short horizon can be obtained in real time.

Fig. 12 shows an example of local adaptation results under smooth traffic conditions where there is no change in target speeds and a vehicle is regulated to follow the long-term optimal speed profile. The red dashed, blue solid, and black dotted lines represent the long-term speed profile, locally adapted speeds, and actual average speeds, respectively. The upper and middle panels represent the locally adapted speeds in a distance domain and a time domain, respectively. The lower panel represents the locally adapted SOC profile in a distance domain. It is revealed that the local vehicle speed and SOC values follow the long-term optimal speed and SOC profiles adequately. Its fuel consumption is 621 g and the driving time is 2078 s , which are consistent with the driving results of the long-term speed profile. The computing time for each short horizon ranged from 0.29 to 0.36 s , and was 0.31 s on average.

Fig. 13 shows another example of local adaptation results under partially heavy traffic conditions. The traffic conditions are represented by the black dotted lines. The two left panels are the locally adapted speeds under heavy traffic condition 1, where traffic is congested in an area between 7 km and 11 km where the engine is switched off. The two right panels are those under heavy traffic condition 2, where traffic is congested in an area between 15 km and 19 km where the engine is switched on. The fuel consumptions are 612 g and 592 g , respectively, and the driving times are 2099 s and 2115 s for heavy traffic conditions 1 and 2 .
![img-11.jpeg](img-11.jpeg)

Fig. 12. Local adaptation under smooth traffic conditions.
From the two upper panels showing the locally adapted speeds in a distance domain, a vehicle speed is adapted adequately to changes in traffic conditions. It is noteworthy that after the area undergoing traffic congestion, the locally adapted speeds follow the reference speed profile again; this implies that the long-term optimal speed profile can still act as a reference speed after the area. Thus, if traffic is changed in limited areas of the trip, a vehicle is driven in the optimal driving conditions for most areas of the trip, which is the reason why the proposed strategy manages the problem in a distance domain.

The two lower panels show the locally adapted speeds in a time domain. Owing to the lower speeds around the areas under heavy traffic conditions, the driving times are longer. After undergoing heavy traffic conditions, the locally adapted speeds do not match with the long-term optimal speed profile. It implies that the time-based optimal speed profile cannot act as the reference speeds after undergoing changes in traffic conditions.

Fig. 14 compares the engine and motor powers in the smooth and heavy traffic conditions 1 and 2, which are represented by the black solid, red dotted, and blue dashed lines. In the congested area under heavy traffic condition 1, between the distances 7 km and 11 km , the engine is off. Thus, the fuel consumption is almost similar to that under smooth traffic condition. It is demonstrated that the motor power decreases at deceleration of around 7 km in distance and increases at acceleration of around 11 km in comparison with that under traffic smooth condition. In the congested area under heavy traffic condition 2, between the distances 15 km and 19 km , the engine is operational. It is revealed that the engine power at the area is lower, and consequently, the fuel consumption is reduced by approximately $5 \%$. In the other areas, the engine and motor powers are consistent with each other.

![img-12.jpeg](img-12.jpeg)

Fig. 13. Local adaptation under heavy traffic conditions.
![img-13.jpeg](img-13.jpeg)

Fig. 14. Comparison of engine and motor powers.

## V. CONCLUSIONS

This study investigates a distance-based hierarchical energy management strategy for power-split PHEVs to balance the optimality, real-time computing load, and changeability of traffic conditions. The proposed strategy consists of two stages: generation of optimal management profiles in the long-term and their adaptation to actual traffic conditions in the short-term. The first stage, before departure, generates the globally optimal speed and SOC profiles for the whole trip in a distance domain by considering the characteristics of the drivetrain, trip information, and traffic conditions at that time, if available. While driving, the second stage utilizes the long-term profiles as references and adapts operating conditions to changes in traffic conditions for a short horizon.

Simulations demonstrate that the optimal-speed-profilebased strategy yields a $17 \%$ improvement in fuel consumption over the strategy without optimization of the given speed profile. In addition, although the traffic conditions in certain areas of the trip route change from those used for optimization,
![img-14.jpeg](img-14.jpeg)
this speed profile, optimized in a distance domain, continues to be optimal except in areas undergoing the changes. Thus, this distance-based strategy localizes the effects of changes in traffic conditions and enables near-optimal energy management with adaptation only for a short horizon; this makes the computing time sufficiently short for real-time implementation.

The effects of input parameters in the distance-based strategy, such as the step sizes of long-term and fine segments and the length of the short horizon and their optimal values, will be the subject of our future work.

## REFERENCES

[1] L. Guzzella and A. Sciarretta, Vehicle Propulsion Systems: Introduction to Modeling and Optimization. New York, NY, USA: Springer, 2010.
[2] X. Zhang and C. Mi, Vehicle Power Management: Modeling, Control and Optimization. London, U.K.: Springer, 2011.
[3] J. Liu and H. Peng, "Modeling and control of a power-split hybrid vehicle," IEEE Trans. Control Syst. Technol., vol. 16, no. 6, pp. 1242-1251, Nov. 2008.
[4] M. Sorrentino, G. Rizzo, and I. Arsie, "Analysis of a rule-based control strategy for on-board energy management of series hybrid vehicles," Control Eng. Pract., vol. 19, pp. 1433-1441, 2011.
[5] S. D. Cairano, W. Liang, I. V. Kolmanovsky, M. L. Kuang, and A. M. Philips, "Power smoothing energy management and its application to a series hybrid powertrain," IEEE Trans. Control Syst. Technol., vol. 21, no. 6, pp. 2091-2103, Nov. 2013.
[6] A. Sciarretta, M. Back, and L. Guzzella, "Optimal control of parallel hybrid electric vehicles," IEEE Trans. Control Syst. Technol., vol. 12, no. 3, pp. 352-363, May 2004.
[7] C. Lin, H. Peng, J. W. Grizzle, and J. Kang, "Power management strategy for a parallel hybrid electric truck," IEEE Trans. Control Syst. Technol., vol. 11, no. 6, pp. 839-849, Nov. 2003.
[8] J. Liu and H. Peng, "Control optimization for a power-split hybrid vehicle," in Proc. Amer. Control Conf., Minneapolis, MN, USA, 2006, pp. 466-471.
[9] H. Borhan, A. Vahidi, A. M. Philips, M. L. Kuang, I. V. Kolmanovsky, and S. D. Cairano, "MPC-based energy management of a power-split hybrid electric vehicle," IEEE Trans. Control Syst. Technol., vol. 20, no. 3, pp. 593-603, May 2012.
[10] Z. Chen, C. C. Mi, J. Xu, X. Gong, and C. You, "Energy management for a power-split plug-in hybrid electric vehicle based on dynamic programming and neural networks," IEEE Trans. Veh. Technol., vol. 63, no. 4, pp. 15671580, May 2014.
[11] J. Liu, H. Peng, and Z. Filipi, "Modeling and analysis of the toyota hybrid system," in Proc. IEEE/ASME Int. Conf. Adv. Intell. Mechatronics, Monterey, CA, USA, 2005, pp. 134-139.

[12] N. Kim, A. Rousseau, and E. Rask, "Autonomic model validation with test data for 2010 Toyota Prius," in Proc. SAE World Cong. Exhib., Detroit, MI, USA, 2012, pp. 1-14.
[13] N. Jalil, N. A. Kheir, and M. Salman, "A rule-based energy management strategy for a series hybrid vehicle," in Proc. Amer. Control Conf., Albuquerque, NM, USA, 1997, pp. 689-693.
[14] Y. Zhu, Y. Chen, G. Tian, H. Wu, and Q. Chen, "A four-step method to design an energy management strategy for hybrid vehicles," in Proc. Amer. Control Conf., Boston, MA, USA, 2004, pp. 156-161.
[15] N. J. Schouten, M. A. Salman, and N. A. Kheir, "Fuzzy logic control for parallel hybrid vehicles," IEEE Trans. Control Syst. Technol., vol. 10, no. 3, pp. 460-468, May 2002.
[16] Y. Li, X. Lu, and N. C. Kar, "Rule-based control strategy with novel parameters optimization using NSGA-II for power-split PHEV operation cost minimization," IEEE Trans. Veh. Technol., vol. 63, no. 7, pp. 30513061, Sep. 2014.
[17] Q. Gong, Y. Li, and Z. Peng, "Trip-based optimal power management of plug-in hybrid electric vehicles," IEEE Trans. Veh. Technol., vol. 57, no. 6, pp. 3393-3401, Nov. 2008.
[18] C. Musardo, G. Rizzoni, and B. Staccia, "A-ECMS: an adaptive algorithm for hybrid electric energy management," in Proc. IEEE Conf. Decis. Control Eur. Control Conf., Seville, Spain, 2005, pp. 1816-1823.
[19] D. Karbowski, J. Kwon, N. Kim, and A. Rousseau, "Instantaneously optimized controller for a multimode hybrid electric vehicle," in Proc. SAE World Congs. Exhib., Detroit, MI, USA, 2010, pp. 1-22.
[20] D. Zhao, R. Stobart, G. Dong, and E. Winward, "Real-time energy management for diesel heavy duty hybrid electric vehicles," IEEE Trans. Control Syst. Technol., vol. 23, no. 3, pp. 829-841, May 2015.
[21] L. Serrao, S. Onori, and G. Rizzoni, "ECMS as a realization of Pontryagin's minimum principle for HEV control," in Proc. Amer. Control Conf., 2009, St. Louis, MO, USA, pp. 3964-3969.
[22] N. Kim, S. Cha, and H. Peng, "Optimal control of hybrid electric vehicle based on Pontryagin's minimum principle," IEEE Trans. Control Syst. Technol., vol. 19, no. 5, pp. 1279-1287, Sep. 2011.
[23] N. Kim, S. W. Cha, and H. Peng, "Optimal equivalent fuel consumption for hybrid electric vehicles," IEEE Trans. Control Syst. Technol., vol. 20, no. 3, pp. 817-825, May 2012.
[24] H. A. Borhan, C. Zhang, A. Vahidi, A. M. Phillips, M. L. Kuang, and S. D. Cairano, "Nonlinear model predictive control for power split-hybrid electric vehicles," in Proc. IEEE Conf. Decis. Control, Atlanta, GA, USA, 2010, pp. 4890-4895.
[25] B. Moulik and D. Soffker, "Optimal rule-based power management for online, real-time applications in HEVs with multiple sources and objectives: A review," Energies, vol. 8, pp. 9049-9063, 2015.
[26] S. J. Moura, H. K. Fathy, D. S. Callaway, and J. L. Stein, "A stochastic optimal control approach for power management in plug-in hybrid electric vehicles," IEEE Trans. Control Syst. Technol., vol. 19, no. 3, pp. 545-555, May 2011.
[27] Y. L. Murphey et al., "Intelligent hybrid vehicle power control-part II. online intelligent energy management," IEEE Trans. Veh. Technol., vol. 62, no. 1, pp. 69-79, Jan. 2013.
[28] T. Choe, A. Skabardonis, and P. Varaiya, "Freeway performance measurement system (PeMS): An operational analysis tool," Univ. Calif., Berkeley, CA, USA, Transp. Res. Rec., 1811, Jan. 2001.
[29] "PeMS," California Dept. Transp., Sacramento, CA, USA. 2017. [Online]. Available: http://pems.dot.ca.gov
[30] Wisconsin Traffic Operations and Safety Laboratory. 2017. [Online]. Available: http://transportal.cee.wisc.edu
[31] V. Larsson, L. Johannesson, B. Egardi, and A. Lasson, "Benefit of route recognition in energy management of plug-in hybrid electric vehicles," in Proc. Amer. Control Conf., Montreal, QC, Canada, 2012, pp. 1314-1320.
[32] C. Zhang and A. Vahidi, "Real-time optimal control of plug-in hybrid vehicles with trip preview," in Proc. Amer. Control Conf., Baltimore, MD, USA, 2010, pp. 6917-6922.
[33] D. Ambafd and L. Guzzella, "Predictive reference signal generator for hybrid electric vehicles," IEEE Trans. Veh. Technol., vol. 58, no. 9, pp. 47304740, Nov. 2009.
[34] C. Sun, S. J. Moura, X. Hu, J. K. Hedrick, and F. Sun, "Dynamic traffic feedback data enabled energy management in plug-in hybrid electric vehicles," IEEE Trans. Control Syst. Technol., vol. 23, no. 3, pp. 1075-1086, May 2015.
[35] Q. Gong, Y. Li, and Z. Peng, "Computationally efficient optimal power management for plug-in hybrid electric vehicles based on spatial-domain two-scale dynamic programming," in Proc. IEEE Conf. Veh. Electron. Saf., Columbus, OH, USA, 2008, pp. 90-95.
[36] Q. Gong, Y. Li, and Z. Peng, "Trip based power management of plug-in hybrid electric vehicle with two-scale dynamic programming," in Proc. IEEE Veh. Power Propulsion Conf., Arlington, TX, USA, 2007, pp. 12-19.
[37] L. Johannesson, N. Murgovski, E. Jonasson, J. Hellgren, and B. Egardt, "Predictive energy management of hybrid long-haul trucks," Control Eng. Pract., vol. 41, pp. 83-97, 2015.
[38] F. Mensing, R. Trigui, and E. Bideaux, "Vehicle trajectory optimization for application in Eco-driving," in Proc. IEEE Veh. Power Propulsion Conf., Chicago, IL, USA, 2011, pp. 1-6.
[39] Q. Cheng, L. Nonveliere, and O. Orfila, "A new eco-driving assistance system for a light vehicle: energy management and speed optimization," in Proc. IEEE Intell. Veh. Symp., Gold Coast, Qld, Australia, 2013, pp. 14341439.
[40] F. Mensing, E. Bideaux, R. Trigui, and H. Tattegrain, "Trajectory optimization for eco-driving taking into account traffic constraints," Transp. Res. D Transp. Environ., vol. 18, pp. 55-61, 2013.
[41] "Autonomie," Argonne Nat. Lab., Lemont, IL, USA. 2017. [Online]. Available: http://www.autonomie.net
[42] N. Kim, M. Duoba, N. Kim, and A. Rousseau, "Validating volt PHEV model with dynamometer test data using Autonomie," SAE Int. J. Passenger Cars, vol. 6, no. 2, pp. 985-992, 2013.
[43] G. Rizzoni, L. Guzzella, and B. M. Baumann, "Unified modeling of hybrid electric vehicle drivetrains," IEEE Trans. Mechatronics, vol. 4, no. 3, pp. 246-257, Sep. 1999.
[44] C. Pinto, J. V. Barreras, R. D. Castro, and R. E. Araujo, "Study on the combined influence of battery models and sizing strategy for hybrid and battery-based electric vehicles," Energy, vol. 137, pp. 272-284, 2017.
[45] T. K. Paul and H. Iba, "Linear and combinatorial optimizations by estimation of distribution algorithms," in Proc. 9th MPS Symp. Evol. Comput., 2002, pp. 99-106.
[46] M. Hauschild and M. Pelikan, "An introduction and survey of estimation of distribution algorithms," Swarm Evol. Comput., vol. 1, pp. 111-128, 2011.
[47] P. Yang, K. Tang, and X. Lu, "Improving estimation of distribution algorithm on multimodal problems by detecting promising areas," IEEE Trans. Cybern., vol. 45, no. 8, pp. 1438-1448, Aug. 2015.
[48] W. Dong and X. Yao, "Unified eigen analysis on multivariate Gaussian based estimation of distribution algorithms," Inf. Sci., vol. 178, pp. 30003023, 2008.
[49] H. Lim, C. C. Mi, and W. Su, "A distance-based two-stage ecological driving system using an estimation of distribution algorithm and model predictive control," IEEE Trans. Veh. Technol., vol. 66, no. 8, pp. 66636675, Aug. 2017.
[50] X. Qi, G. Wu, K. Boriboonsomsin, and M. J. Barth, "Development and evaluation of an evolutionary algorithm-based online energy management system for plug-in hybrid electric vehicles," IEEE Trans. Intell. Transp. Syst., vol. 18, no. 8, pp. 2181-2191, Aug. 2017.
![img-15.jpeg](img-15.jpeg)

Hamsang Lim (M'09) received the B.S., M.S., and Ph.D. degrees from the School of Electrical Engineering, Seoul National University, Seoul, South Korea, in 1996, 1998, and 2004, respectively. He was with the Telecommunication R\&D Center, Samsung Electronics Co. Ltd., from 2004 to 2007. He is currently a Professor with the Department of Electronics Convergence Engineering, Kwangwoon University, Seoul, Korea. His research interests include instrumentation and measurement systems, power supply and distribution systems, and energy management in electrified vehicles.
![img-16.jpeg](img-16.jpeg)

Wensong Su (S'06-M'13) received the B.S. degree with distinction in electrical engineering from Clarkson University, Potsdam, NY, USA, in 2008, the M.S. degree in electrical engineering from Virginia Tech, Blacksburg, VA, USA, in 2009, and the Ph.D. degree in electrical engineering from North Carolina State University, Raleigh, NC, USA, in 2013. He is currently an Assistant Professor with the Department of Electrical and Computer Engineering, University of Michigan, Dearborn, MI, USA. His research interests include power and energy systems, electrified transportation systems, cyber-physical systems, and electricity market.