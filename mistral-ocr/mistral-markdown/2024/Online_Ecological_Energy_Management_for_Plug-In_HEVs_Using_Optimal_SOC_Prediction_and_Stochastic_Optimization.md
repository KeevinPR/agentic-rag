# Online Ecological Energy Management for Plug-In HEVs Using Optimal SOC Prediction and Stochastic Optimization 

Hansang Lim ${ }^{\oplus}$, Senior Member, IEEE


#### Abstract

Optimizing power demand and distribution in real time is the primary challenge in the energy management of plug-in hybrid electric vehicles. To address this challenge, this study proposes an online ecological energy management strategy using the optimal state of charge (SOC) prediction and stochastic optimization. Future energy-consumption features at each location are computed from the traffic and route information of the entire remaining trip and the optimal SOC value at the next location is predicted from the computed features using a recurrent neural network. By considering the predicted optimal SOC and average speed as references, the speed and SOC values at the next location are optimized using a modified estimation of distribution algorithm (EDA). The process of generating initial and new populations in EDA is modified for fast and reliable convergence. The optimal SOC prediction considering the energy consumption for the entire remaining trip from the current to final locations ensures long-term optimality. Stochastic aspects of the modified EDA can compensate for potential neural-network errors. The prediction and optimization of driving only up to the next location enables to adapt to the changes in traffic conditions. Moreover, the energy efficiency is further improved by optimizing power demand based on the characteristics of the drivetrain, as well as traffic and route conditions. Because the traffic and route information are provided on a location basis, management is performed in a distance domain. The proposed management strategy is evaluated in diverse driving scenarios, and it exhibits good performance, comparable to that of the offline optimization.


Index Terms-Estimation of distribution algorithm, feedforward neural network, long-term optimality, online ecological energy management, optimal speed and state-of-charge, recurrent neural network.

## I. InTRODUCTION

PLUG-IN hybrid electric vehicles (PHEVs) provide high energy efficiency owing to two or more propulsive sources and large battery capacities. The energy efficiency of PHEVs primarily depends on the power distribution between the propulsive sources, which is determined by the energy management strategy. Therefore, an energy management strategy that is appropriate for the driving conditions and characteristics of drivetrains is essential. Energy management strategies in

[^0]PHEVs are broadly divided into two categories based on the method of distributing power demand to propulsive sources: rule- and optimization-based strategies.

Rule-based strategies control the power distribution using rules determined by human expertise [1], fuzzy logic [2], [3], genetic algorithms [4], and deep learning [5]. Generally, these strategies are robust, easy to implement, and sufficiently fast to allow real-time management; however, their optimality is limited under diverse driving conditions.

Optimization-based strategies are further divided into global and real-time optimization strategies. Global optimization strategies provide a globally optimal management solution using optimization algorithms, such as dynamic programming (DP) [6], [7], [8], with full knowledge of the driving conditions, which can be obtained via a global positioning system (GPS), intelligent transportation system (ITS), and communications [9], [10], [11]. However, the long computational time required to optimize the entire driving cycle hinders their real-time applications essential for coping with dynamic changes in traffic conditions. Generally, real-time optimization strategies optimize energy consumption over part of the driving cycle rather than the entire driving cycle for a faster computation, resulting in locally optimal performance. A common approach to real-time optimization is the equivalent consumption minimization strategy (ECMS), which minimizes the instantaneous sum of fuel and electric energy consumption weighted by an equivalence factor [12], [13], [14]. The Pontryagin's minimum principle (PMP) is another approach, which converts the power distribution problem into an instantaneous optimization based on specific assumptions [15], [16]. However, its optimality largely depends on the equivalence factor in the ECMS or the costate in the PMP, and it is difficult to determine the best equivalence factor or costate in real time, as they vary with the future driving condition.

Recently, learning-based strategies have been explored to overcome the aforementioned limitations, which are categorized into two groups. One group uses machine-learning or deep-learning algorithms for estimating the parameters or variables needed to optimize the energy management. The optimal battery current and equivalence factor in the ECMS were estimated from traffic data using neural networks (NNs) [7] and deep Q-networks [17]. Vehicle speeds were predicted using artificial NNs [18], recurrent neural networks (RNNs) and long short-term memory (LSTM) [19], Markov chains and


[^0]:    Manuscript received 24 March 2023; revised 6 December 2023 and 23 January 2024; accepted 18 March 2024. Date of publication 4 April 2024; date of current version 29 August 2024. This work was supported by the Basic Science Research Program through the National Research Foundation of Korea under Grant NRF-2019R1F1A1058029. The Associate Editor for this article was R. Arghandeh.

    The author is with the Department of Electronics Convergence Engineering, Kwangwoon University, Seoul 01897, South Korea (e-mail: lhs@kw.ac.kr).
    Digital Object Identifier 10.1109/TITS.2024.3379991

RNN [20], and LSTM and radar data [21], [22]. NNs and convolutional NNs have been adopted to select the operating mode of HEVs [23] and recognize the types of driving cycles [24]. The other group handles the optimal power distribution using diverse learning algorithms. Road types, driving trends, optimal battery power, and engine speed were estimated using a NN [25]. Q-learning with and without speed prediction [26], [27] and Q-learning based on neurodynamic programming [28] have been used for optimal control actions. Deep Q-learning (DQL) using a new optimization method [29], deep deterministic policy gradient (DDPG) embedding expert knowledge [5], and artificial-NN-based deep learning combined with genetic algorithms [30] have been employed in management strategies. DQL- and DDPG-based management methods that integrate multiple traffic information, such as traffic lights, were compared in [31]. However, NN-based learning heavily relies on pretrained NN models that produce inevitable errors in complex problems such as energy managements, restricting its performance. Moreover, model-free reinforcement learning requires enormous driving data and, if not, may not achieve near-global optimality for new driving conditions.

With the development of GPS and ITS, traffic and route information such as the average traffic speed and density on road segments can be obtained in real time [9], [10], [11]. As the knowledge of future driving conditions contributes to optimality, traffic and route information is employed in energy management strategies. The costate of the PMP is updated from the average power predicted from the average speed and its standard deviation [16]. As the battery electricity is efficiently consumed for optimal power distribution, SOC reference is generated with traffic data using the linear model [32], [33], PMP [15], fast DP [34], [35], replanned linear model [36], NN [37], and adaptive rolling planning method [38]. The SOC references are simplified as linear functions of driving distance or can be estimated from only partial traffic and route information; although the simplified functions can be easily implemented, they cannot ensure nearglobal optimality.

The energy efficiency of PHEVs depends on power demand and distribution. As power demand is adjusted using vehicle speed, energy efficiency can be further improved by optimizing vehicle speed, considering the characteristics of the drivetrain and traffic conditions, instead of simply following traffic conditions. This is known as ecological driving. An optimal speed trajectory for short-term future driving was generated, and the power distribution was optimized under this trajectory [39], [40]. Owing to the dependency of the optimality on the length of the finite horizon, the speed trajectory may be locally optimal. To reduce this dependence, a distancebased approach with a two-stage hierarchy was developed [41]. Before departure, the optimal speed and SOC trajectories for the entire driving cycle were established in the distance domain. During driving, short-term control variables were adapted to changes in local traffic conditions. However, entire trajectory optimization is time-consuming and is not practical even if the optimization is performed before departure. Moreover, it is difficult to maintain the optimality if traffic conditions significantly change.

To overcome these limitations, this study proposes an online ecological energy management strategy that uses optimal SOC prediction and the stochastic approach of the modified estimation of distributed algorithm (EDA). This energy management is performed in the distance domain because traffic and route information is provided based on location through the ITS. At each location, the optimal SOC value at the next location is predicted using an RNN. To fulfill globally near-optimal SOC prediction in real time, comprehensive features characterizing energy consumption in the entire future driving rather than a partial future driving are calculated from traffic and route information. Using the calculated energy consumption features, the RNN predicts the optimal SOC value at the next location. Then, the vehicle speed and battery power consumption are optimized with constraints on the predicted optimal SOC value and traffic conditions, which optimize the power demand as well as its distribution. An EDA-based algorithm is used as the optimization algorithm because its stochastic aspects can compensate for the RNN model errors. As this optimization should be performed in real time, EDA is modified for improving the computational time, which includes initial populations based on feed-forward NNs and new populations generated by combining a typical probability distribution model with a grid-based area searching model. This prediction and optimization are repeatedly performed at each location as the vehicle travels, which allows immediate adaptation to changing traffic conditions.

The main contributions of this study are as follows:

1) An online ecological energy management scheme that uses RNN-based optimal SOC prediction and modified EDA-based real-time optimization is proposed.
2) Energy consumption features over the entire future driving are calculated and used to predict the optimal SOC at the next location using an RNN, which facilitates globally near-optimal power distribution.
3) Vehicle speed and battery consumption up to the next location are optimized using the modified EDA with constraints on the predicted SOC value, traffic information, and the characteristic of the drivetrain, which can facilitate ecological driving, feature rapid real-time management, and compensate for involved NN model errors.

The remainder of this paper is organized as follows: Section II presents the modeling of the systems for vehicle propulsion in a PHEV. Section III presents an online ecological energy management scheme based on the optimal SOC prediction. In Section IV, the performance of the proposed strategy is evaluated. Finally, Section V presents the conclusions.

## II. Vehicle Dynamics

A power-split PHEV involves two propulsion sources, an engine and a motor, which are combined via a planetary gear set, as illustrated in Fig. 1. The engine, motor, and generator are connected to the planet carrier, ring gear, and sun gear of the planetary gear set, respectively. The ring gear output is connected to the wheel via the final drive.

To reduce model complexity, the inertial losses of the engine, motor, and generator were disregarded, and steady-state operation was assumed [34]. Therefore, the

![img-0.jpeg](img-0.jpeg)

Fig. 1. Drivetrain of a power-split PHEV.
drivetrain output torque $T_{\text {out }}$ can be calculated as

$$
T_{\text {out }}=f_{r} \eta_{p g}\left(T_{\text {eng }}+T_{\text {gen }}+G_{T C} \eta_{T C} T_{\text {mot }}\right)
$$

where $T_{\text {eng }}, T_{\text {gen }}$, and $T_{\text {mot }}$ are the torques of the engine, generator, and motor, respectively [41]. $T_{\text {gen }}$ has the following relationship with $T_{\text {eng }}$ :

$$
T_{\text {gen }}=-T_{\text {eng }} \frac{Z}{Z+1}
$$

$T_{\text {out }}$ in (1) can be expressed as

$$
T_{\text {out }}=f_{r} \eta_{p g}\left(\frac{1}{Z+1} T_{\text {eng }}+G_{T C} \eta_{T C} T_{\text {mot }}\right)
$$

where $\mathrm{Z}=\frac{N_{s}}{N_{r}}$ and $N_{s}$ and $N_{r}$ represent the radii of the sun and ring gears, respectively. Additionally, $\eta_{p g}$ and $\eta_{T C}$ are the efficiencies of the planetary gear set and the torque coupler, respectively, and are modeled as constants, specifically, 0.98 and 0.97 , respectively. Other parameters and their corresponding values are listed in Table 1 and were obtained from Autonomie, which is a simulation software for vehicle performance analysis [42], [43].

Accordingly, a propelling force $F_{w}$ at a wheel is expressed as

$$
\begin{aligned}
F_{w}(t)= & \frac{T_{\text {out }}(t)}{R_{w}}=m \dot{v}(t)+\frac{1}{2} \rho C_{d} A_{d} v(t)^{2} \\
& +m g C_{r} \cos \theta(t)+m g \sin \theta(t)
\end{aligned}
$$

where $v(t)$ and $\theta(t)$ represent the vehicle speed $(\mathrm{m} / \mathrm{s})$ and the road gradient (rad), respectively. Using the acceleration of the vehicle in (4), the vehicle speed $v\left(t_{k+1}\right)$ at the $(k+1)^{\text {th }}$ time step can be expressed as

$$
\begin{aligned}
v\left(t_{k+1}\right)= & v\left(t_{k}\right)+\dot{v}\left(t_{k}\right) \Delta t_{k} \\
= & \left(1-\frac{1}{2 m} \rho C_{d} A_{d} v\left(t_{k}\right) \Delta t_{k}\right) v\left(t_{k}\right)+\frac{\Delta t_{k}}{m} F_{w}\left(t_{k}\right) \\
& -g\left(C_{r} \cos \theta\left(t_{k}\right)+\sin \theta\left(t_{k}\right)\right) \Delta t_{k}
\end{aligned}
$$

where $\Delta t_{k}$ is the time interval between adjacent time steps $\left(=t_{k+1}-t_{k}\right)$. The acceleration within each time interval was assumed constant.

Engine operation consumes fuel energy, and according to the Willans line approximation, fuel consumption rate, $\dot{m_{f}}$ can be modeled as

$$
\dot{m_{f}}=\left(\alpha_{1} \omega_{\text {eng }}+\beta_{1}\right) T_{\text {eng }}+\left(\alpha_{2} \omega_{\text {eng }}+\beta_{2}\right)
$$

TABLE I
ParameTers of The Vehicle Model

| Symbol | Quantity | Value |
| :-- | :-- | :-- |
| $f_{r}$ | Gear ratio of the final drive | 4.06 |
| $G_{T C}$ | Gear ratio of the torque coupler | 2.5 |
| $R_{v}$ | Wheel radius | 0.317 m |
| $m$ | mass | 1470 kg |
| $\rho$ | Air density | $1.19854 \mathrm{~kg} / \mathrm{m}^{3}$ |
| $C_{d}$ | Air drag coefficient | 0.3 |
| $A_{d}$ | Frontal area | $2.2508 \mathrm{~m}^{2}$ |
| g | Gravity | $9.81 \mathrm{~m} / \mathrm{s}^{2}$ |
| C | Rolling resistance coefficient | - |

![img-1.jpeg](img-1.jpeg)

Fig. 2. Fuel efficiency map and battery parameters.
where $\omega_{\text {eng }}$ denotes the engine speed. Additionally, $\alpha_{1}, \alpha_{2}$, $\beta_{1}$, and $\beta_{2}$ represent coefficients that depend on engine torque [41].

The motor and generator charge or discharge electrical energy, which changes the battery SOC. By modeling a battery as a series combination of the open-circuit voltage $V_{o c}$ and internal resistance $R_{\text {batt }}, S \dot{O} C$ can be expressed as

$$
S \dot{O} C=\frac{d S O C}{d t}=-\frac{V_{o c}-\sqrt{V_{o c}^{2}-4 R_{\text {batt }} P_{\text {batt }}}}{2 Q_{\text {batt }} R_{\text {batt }}}
$$

where $Q_{\text {batt }}$ represents the battery capacity, and $P_{\text {batt }}$ indicates the battery power, which can be expressed as

$$
P_{\text {batt }}=T_{\text {mot }} \omega_{\text {mot }}\left(\eta_{\text {mot }} \eta_{\text {inv }}\right)^{l}+T_{\text {gen }} \omega_{\text {gen }}\left(\eta_{\text {gen }} \eta_{\text {inv }}\right)^{l}
$$

where $\omega_{\text {mot }}$ and $\omega_{\text {gen }}$ are the speeds of the motor and generator, respectively. Additionally, $\eta_{\text {mot }}, \eta_{\text {gen }}$, and $\eta_{\text {inv }}$ denote the efficiencies of the motor, generator, and power converter, respectively. Superscript $l$ indicates the status of the motor (or generator), which is ' 1 ' during charging and ' -1 ' during discharging.

Fig. 2 illustrates the dependence of the fuel consumption rate and battery parameters on the operating conditions and battery state. The performance data were obtained from Autonomie. In the left panel, the solid and dashed lines correspond to the fuel map and its estimation, respectively, which were obtained using the linear model given by (6). The blue and red solid lines in the right panel correspond to the open-circuit voltage and internal resistance of the battery, respectively. The blue and red circles represent their estimations using a linear SOC model and a combined model of two quadratic functions for SOC values smaller or larger

than 0.6 , respectively [41]. The models for $m_{f}^{\prime}, V_{o c}$, and $R_{\text {batt }}$ provide reasonable estimations, which are used to optimize the proposed energy management strategy.

For distance-based management, the vehicle dynamics are transformed into the distance domain. The driving route is divided into segments with a fixed distance step size $\Delta s$. The vehicle speed and driving distance at location $k \Delta s$ are denoted by $v(k)$ and $S(k)$, respectively. Subsequently, the relationship between the distance step and time interval is derived as

$$
\Delta s=S(k+1)-S(k)=\frac{v(k)+v(k+1)}{2} \Delta t_{k}
$$

By inserting (9) into (5), the vehicle speed at the $(k+1)^{\text {th }}$ location is given by

$$
\begin{aligned}
v(k+1)^{2}= & \left(1-\frac{1}{m} \rho C_{d} A_{d} \Delta s\right) v(k)^{2}+\frac{2 \Delta s}{m} F_{w}(k) \\
& -2 g\left(C_{r} \cos \theta(k)+\sin \theta(k)\right) \Delta s
\end{aligned}
$$

The propelling force $F_{w}(k)$ at the $k^{\text {th }}$ location to drive to the $(k+1)^{\text {th }}$ location is expressed as

$$
\begin{aligned}
F_{w}(k)= & \frac{m}{2 \Delta s} v(k+1)^{2}+\left(\frac{1}{2} \rho C_{d} A_{d}-\frac{m}{2 \Delta s}\right) v(k)^{2} \\
& +m 2 g\left(C_{r} \cos \theta(k)+\sin \theta(k)\right)
\end{aligned}
$$

Additional details on vehicle dynamics can be found in our previous studies [41], [44]. From (7) and (9), the SOC at the $(k+1)^{\text {th }}$ location is given by

$$
\begin{aligned}
S O C(k+1)= & S O C(k)+\Delta S O C(k)=S O C(k) \\
& -\frac{V_{o c}(k)-\sqrt{V_{o c}(k)^{2}-4 R_{\text {batt }}(k) P_{\text {batt }}(k)}}{2 Q_{\text {batt }} R_{\text {batt }}(k)} \\
& \times \frac{2 \Delta s}{v(k)+v(k+1)}
\end{aligned}
$$

## III. ONLINE ECOLOGICAL ENERGY MANAGEMENT BASED ON OPTIMAL SOC PREDICTION StOCHASTIC OPTIMIZATION

For real-time energy-efficient driving, an online ecological energy management strategy with the prediction of the long-term optimal SOC and a stochastic approach was proposed.

## A. Fundamental Concept

The primary objective of online ecological energy management is to secure long-term optimal power demand and distribution considering drivetrain characteristics under given traffic and route conditions in real time. The framework of the proposed energy management strategy is shown in Fig. 3(a), which consists of two stages: optimal SOC prediction and online optimization.

Two tasks were performed for optimal SOC prediction. First, features that characterize the energy consumption in the entire future driving cycle were produced from traffic and route information, which were assumed to be obtained via ITS and GPS. The driving cycle was divided into segments of fixed size. The average speed and road slope at each segment and the length of the remaining driving cycle were used as
![img-2.jpeg](img-2.jpeg)

Fig. 3. (a) Framework of the proposed online ecological energy management strategy (b) operation during driving.
traffic and route information, respectively. Subsequently, the optimal SOC value at the next location was predicted from the computed energy consumption features and the traffic and route information at the previous, current, and subsequent locations. As a new SOC value is determined based on the previous value, it is necessary to store information on the previous inputs; therefore, an NN with recurrent connections is suitable for processing such sequential data. As RNNs involve less number of parameters, it is simple in structure and can be trained rapidly, whereas it has a limited memory capacity and cannot retain long-term dependencies due to vanishing gradients. However, the next SOC value mainly depends on a few previous values, and its prediction does not require handling long sequences. Therefore, an RNN was used for prediction and it is sufficiently fast for real-time applications. The energy-consumption features for the entire future driving cycle ensure that the predicted SOC value is optimal in the long term and provide a good reference for power splits in online optimization. Furthermore, the prediction of only the next SOC value allows for immediate adaptation to changes in traffic conditions.

In online optimization, the vehicle speed and SOC value at the next location were optimized using a modified EDA, based on the predicted SOC value, average speed at the next location, and characteristics of the drivetrain. First, the control variables yielding the predicted SOC value after driving to the next location, such as engine torque $T_{\text {eng }}$, engine speed $\omega_{\text {eng }}$, and motor torque $T_{\text {mot }}$, were estimated using feed-forward

![img-3.jpeg](img-3.jpeg)

Fig. 4. Flowchart of the proposed online ecological energy management strategy.
neural networks (FFNNs). These estimated values were used to generate the initial populations for an EDA. Second, new populations in an EDA were generated by combining the usual statistical populations and gridded populations centered at the best population in the previous iteration. These two modifications accelerate optimization, and the stochastic aspect of an EDA compensates for errors in neural-network-based estimation.

As a vehicle travels, the remaining driving is reduced, and the traffic may change. Therefore, when departing, the driving cycle from 0 to $n \Delta s$ was considered, and when traveling at the $k^{\text {th }}$ location, the driving cycle from $k \Delta s$ to $n \Delta s$ was considered. At each location, the optimal SOC prediction and online optimization were repeated for the remaining future driving, as shown in Fig. 3(b).

## B. Proposed Online Ecological Energy Management

Fig. 4 shows the operations of the proposed online ecological energy management strategy for each location. The upper four blocks encircled by the dotted rectangle represent the optimal SOC prediction based on the RNN, and the lower blocks represent the online optimization of driving to the next location, that is, the $k+1^{\text {th }}$ location. As the vehicle travels, this process is repeated by increasing $k$ to $k+1$ by one. The operations of each stage are described in detail.

1) Prediction of the Long-Term Optimal SOC: In (3), (4), and (8), $T_{\text {eng }}, \omega_{\text {eng }}$, and $T_{\text {mot }}$ determine the vehicle speed and SOC at the next location, namely, the power demand and its distribution. Therefore, from the average speed and road slope at each segment of the remaining driving cycle, features that characterize the energy consumption in future driving were generated and input into an RNN that predicted the optimal SOC at the next location.

Fig. 5 illustrates the RNN-based optimal SOC prediction structure. The RNN inputs comprised five groups of data. The first group indicates the status of a vehicle at the current $k^{\text {th }}$ location, that is, vehicle speed $v(k)$ and $\operatorname{SOC}(k)$. The second group indicates traffic information in the next two locations,
![img-4.jpeg](img-4.jpeg)

Fig. 5. RNN-based optimal SOC prediction structure.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Modified EDA-based online optimization structure.
that is, the average speeds $v_{\text {avg }}(k+1)$ and $v_{\text {avg }}(k+2)$. The third group is the driving route information, such as the length of the remaining route $L_{\text {remain }}(k)$ and the road slope-related term $f(\theta(k))(=g\left(C_{r} \cos \theta(k)+\sin \theta(k)\right) \Delta \mathrm{s})$. The fourth group characterizes the energy consumption for the future driving cycle, which includes the propelling force $F_{w}(k)$, the sum of the propelling forces $\Sigma F_{w}(l)$ from $l=k$ to $n-1$ (that is, the end of the cycle), the maximum and minimum values $\left(\operatorname{Max}\left(F_{w}(l)\right), \operatorname{Min}\left(F_{w}(l)\right)\right)$, and the sums of positive and negative propelling forces $\left(\Sigma \operatorname{Por}\left(F_{w}(l)\right), \Sigma \operatorname{Neg}\left(F_{w}(l)\right)\right)$. Here, $n$ denotes the end location. Moreover, from $l=k$ to $n-1, F_{w}(l)$ covers the propelling forces at all segments of the remaining driving cycle and is calculated from (11) using the average speed of each segment. The fifth represents the past SOC values, such as $\operatorname{SOC}(k-1), \cdots, \operatorname{SOC}(k-m)$. These input data were selected based on an analysis of vehicle dynamics and a series of simulations. From these inputs characterizing future energy consumption in the entire future driving, the RNN predicts the optimal SOC value $\operatorname{SOC}(k+1)_{\text {predict }}$ at the next location, which can provide good guidance on longterm optimality.
2) Online Optimization of Driving to the Next Location: Based on the predicted optimal SOC value, driving to the next location was optimized in real time by considering the drivetrain characteristics, traffic, and route information. The optimization of driving only to the next location guarantees a sufficiently short computational time for real-time implementation.

The online optimization structure is shown in Fig. 6. Four groups of data were used as inputs. The first included speed data, such as the current vehicle speed, $v(k)$, and the average speed at the next location, $v_{\text {avg }}(k+1)$. The second included SOC data such as the current SOC, $\operatorname{SOC}(k)$, and the predicted SOC value at the next location, $\operatorname{SOC}(k+1)_{\text {predict }}$. The third and fourth groups were the route information and features that characterize future energy consumption, respectively. The

![img-6.jpeg](img-6.jpeg)
![img-7.jpeg](img-7.jpeg)

Fig. 7. Generation of new populations.
output included the optimal vehicle speed $v(k+1)_{\text {opt }}$, optimal SOC value at the next location, $\operatorname{SOC}(k+1)_{\text {opt }}$, and the optimal control variables that lead to the optimal vehicle speed and SOC value, $T_{\text {mot }}(k)_{\text {opt }}, T_{\text {eng }}(k)_{\text {opt }}$, and $\omega_{\text {eng }}(k)_{\text {opt }}$.

NN model errors are inevitable in complex function approximations such as optimal battery consumptions and the predicted optimal SOC value has potential inaccuracy owing to RNN errors. Therefore, an EDA that uses stochastic approaches was used as the optimization algorithm for robustness against RNN model limitations and to compensate for prediction inaccuracy. An EDA generates a predefined number of samples of control inputs at each iteration, which are called populations. Generally, an EDA starts searching for the optimal solution with random initial populations. Then, it explicitly extracts statistical information from populations with good performance, which builds a probability distribution model of a promising solution. Next, new populations are generated using the built probability distribution model, and the entire process is iterated until stopping criteria are satisfied. This online optimization uses the number of iterations as a stopping criterion, which was set to five. The proposed EDA-based optimization modified an EDA to improve the optimization speed and obtain reliable results within a limited number of iterations. First, the promising control variables such as $T_{\text {eng }}(k)_{\text {init }}, \omega_{\text {eng }}(k)_{\text {init }}$, and $T_{\text {mot }}(k)_{\text {init }}$ were estimated using FFNNs, and the initial populations were generated from the estimated values instead of random generation. Second, new populations were generated using partly the probability distribution model and partly the grid-based area searching model, as shown in Fig. 7.

In Fig. 7(a), the red star indicates the best control variables in the previous iteration. In the first iteration, the promising control variables estimated using FFNNs become the red star. The blue circles represent new population generated by the grid-based model, which are given by $\mathrm{X}+(-2 \Delta X,-\Delta X, 0, \Delta X, 2 \Delta X)$, where X represents each control variable, that is, $T_{\text {eng }}, \omega_{\text {eng }}$, and $T_{\text {mot }}$, of the best population in the previous iteration. The step size $\Delta X$ was initially $5 \%$ of the entire range of each control variable and decreased by $1 \%$ with each iteration. This means that the first iteration searched for $\pm 10 \%$ of the entire range with a step size of $5 \%$, and the last iteration for a $\pm 2 \%$ range with a step size of $1 \%$. The yellow triangles represent the populations generated by the probability distribution model built on the
averages and standard deviations of the good populations in the previous iteration.

For clarity, these three-dimensionally distributed populations were projected onto a $T_{\text {eng }}-T_{\text {mot }}$ plane, as shown in Fig. 7(b). The blue circles of the grid-based model search for relatively wide areas of control variables to prevent a premature result, where the interval of each control variable, such as $\Delta T_{\text {eng }}, \Delta \omega_{\text {eng }}$, and $\Delta T_{\text {mot }}$, decreases with iterations for a more efficient search. The yellow triangles of the probability distribution model tend to finely search for a promising area around the current good populations and randomly explore distant regions. These combined populations, along with the promising initial population estimation, can balance the search area, number of iterations, and tolerance, and yield near-optimal results within a small number of iterations, which is a prerequisite for real-time applications.

The cost function for online optimization at each location is expressed as follows:

$$
\begin{aligned}
J_{\text {online }}(k)= & \left(\omega_{1} \dot{m}_{f}(k)+\omega_{2} P_{\text {batt }}(k)\right) \frac{2 \Delta s}{v(k)+v(k+1)} \\
& +\omega_{3} \text { sigmoid }\left(\left(\frac{v(k+1)-v_{\text {avg }}(k+1)}{v_{\text {avg }}(k+1)}\right)^{2}\right)
\end{aligned}
$$

subject to

$$
\begin{aligned}
& |v(k+1)-v_{\text {avg }}(k+1)| \leq \Delta v \\
& \left|S O C(k+1)-S O C_{\text {predict }}(k+1)\right| \leq \Delta S O C \\
& T_{\mathrm{X}(\min )} \leq T_{X}(k) \leq T_{X(\max )} \\
& \omega_{X(\min )} \leq \omega_{X}(k) \leq \omega_{X(\max )} \\
& P_{\mathrm{Y}(\min )} \leq P_{Y}(k) \leq P_{Y(\max )}
\end{aligned}
$$

where $\operatorname{sigmoid}(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}$. $\omega_{1}$ and $\omega_{2}$ are the weights to balance the fuel and electricity consumption and are set to their unit prices, that is, $0.795 \mathrm{US} \$ / \mathrm{kg}$ and 0.137 US $\$ / \mathrm{kWh}$, respectively, as given in [17]. Moreover, $\omega_{3}$ is the weight of the deviation from the average speed and was set to $4.5 \times 10^{-1}$ by trial and error. The allowable speed deviation $\Delta v$ was set to $0.05 v_{\text {avg }}(k+1)$ to provide a margin for ecological driving. $\Delta S O C$ is set to be a larger value between 0.05 times the predicted SOC value and the constant of 0.03 , which allows compensation for the potential SOC prediction inaccuracy owing to the RNN model errors. The subscript X represents the engine, motor, or generator. $P_{\mathrm{Y}}$ represents the motor power $P_{\text {mot }}$ and the generator power $P_{\text {gen }}$.

In (13), the first term represents the cost of restoring the energy consumption while driving to the next location, where $\dot{m}_{f}(k)$ and $P_{\text {batt }}(k)$ are calculated using (6) and (8), respectively. The second term represents the weighted deviation from the average speed, which balances the energy consumption and driving time. If the second term is excluded, the optimized speed tends to follow the lower limit of $0.95 v_{\text {avg }}(k+1)$ to minimize energy consumption, which results in the longest driving time. The speed deviation is squared and applied to the sigmoid function to impose a larger penalty for a large deviation close to the upper or lower speed limit, and to minimize the effects of small deviations.

## C. Training Neural Networks

To train the RNN for SOC prediction and the FFNNs to estimate the promising control variables, 47 driving cycles were prepared in a distance domain. Commonly used driving cycles, such as the urban dynamometer driving schedule (UDDS), highway fuel economy test (HWFET), worldwide harmonized light-duty test cycle (WLTC), and Artemis motorway, were obtained from Autonomie. As the cycles were given in the time domain, they were transformed into the distance domain under the assumption that the vehicle speed was constant within a time step. Then, the transformed driving cycle was divided into segments with an identical distance step size $\Delta s$ of approximately 50 m , which means that the generated distance-based driving cycles list speeds at locations approximately 50 m apart. Two or more short cycles were combined to generate additional training data.

By using EDA, optimal vehicle speed and SOC trajectories were generated for the distance-based driving cycles in different initial SOC conditions from 0.4 to 0.9 at intervals of 0.1 . The speed at the corresponding $k^{\text {th }}$ location in the driving cycle was considered as the average traffic speed $v_{a v g}(k)$. The cost function for this offline optimization is as follows:

$$
J_{\text {offline }}=\sum_{k=0}^{n-1}\left(\omega_{1} \dot{m}_{f}(k)+\omega_{2} P_{\text {batt }}(k)\right) \frac{2 \Delta s}{v(k)+v(k+1)}
$$

subject to

$$
\begin{aligned}
& \left|v(k+1)-v_{a v g}(k+1)\right| \leq \Delta v \\
& S O C_{\min } \leq S O C(k+1) \leq S O C_{\max } \\
& T_{X(\min )} \leq T_{X}(k) \leq T_{X(\max )} \\
& \omega_{X(\min )} \leq \omega_{X}(k) \leq \omega_{X(\max )} \\
& P_{\mathrm{Y}(\min )} \leq P_{Y}(k) \leq P_{Y(\max )} \\
& v(n)=0
\end{aligned}
$$

where constants $\omega_{1}$ and $\omega_{2}$ are weights to balance the fuel and battery consumptions and are set the same as in (13). The subscript X represents the engine, motor, or generator, and the subscript Y represents the motor or generator. The minimum and maximum limits of SOC, that is, $S O C_{\min }$ and $S O C_{\text {max }}$, in a battery were set as 0.3 and 1 , respectively. The engine speed while the engine ran was in the range of $100-500 \mathrm{rad} / \mathrm{s}$, whereas it was zero in the switched-off engine condition. In addition, $k=0$ and $k=n$ indicate the initial and final locations of the driving cycle, respectively, indicating that the driving cycle is divided into $n$ segments. The online optimization in Section III-C covers driving up to the next location, whereas the offline optimization is performed for the entire driving cycle. Therefore, the cost function in (14) does not include a term for the weighted deviation from the average speed in (13).

An EDA randomly generates the predefined number, $n_{\text {pop }}$, of populations covering the entire driving. Therefore, each population comprises $n$ pairs of control variables ( $T_{\text {eng }}, \omega_{\text {eng }}$, $T_{\text {mot }}$ ) at all $n$ locations from 0 to $(n-1) \Delta s$. The values of the cost function given in (14) are computed for all populations,
![img-8.jpeg](img-8.jpeg)

Fig. 8. Comparison of SOC trajectories for HWFET-U506 cycle.
and populations with smaller costs are chosen. Statistical information, such as the average and the standard deviation of the chosen populations, are extracted and a probability distribution model of the promising solution is constructed. Based on the probability distribution model, new populations are randomly generated and the unchosen populations are replaced. This process is repeated for a predefined number of iteration, $n_{\text {iter }}$. In the offline optimization, $n_{\text {pop }}$ and $n_{\text {iter }}$ are set to 1500 and 5000 , respectively, and the optimal speed and SOC trajectories, and control variables generating these trajectories were obtained for each driving cycle. Because the optimization was performed for the entire route of each driving cycle, its outputs could be near-optimal in the long term.

The offline optimization results were used as a benchmark for examining the feasibility of the proposed online strategy. In addition, most of the offline optimization results were used to train RNN and FFNNs. The optimization data for 47 driving cycles with six initial SOC conditions were used to train RNN to predict the long-term optimal SOC value at the next location, $S O C_{\text {predict }}(k+1)$, from the input data described in Section III-B. RNN included two hidden layers, and four past SOC outputs were inputted in addition to the current SOC datum. Subsequently, three FFNNs, including two hidden layers, were trained to estimate the promising control variables of $T_{\text {eng }}, \omega_{\text {eng }}$, and $T_{\text {mot }}$, respectively, which were then used to generate the initial EDA populations and yield near-optimal results within a small number of iterations. The three control variables were consecutively estimated, considering their relationships and inputs. First, $T_{\text {mot }}$ was estimated from the predicted SOC value. Then, $T_{\text {eng }}$ was estimated using $T_{\text {mot }}$ and the inputs used in the estimation of $T_{\text {mot }}$ because the target speed at the next location is determined by $T_{\text {mot }}$ and $T_{\text {eng }}$. Finally, $\omega_{\text {eng }}$ was estimated using $T_{\text {mot }}$ and $T_{\text {eng }}$.

## IV. Evaluation of The Proposed Energy Management Strategy

The proposed online ecological energy management strategy was implemented in MATLAB and evaluated using diverse trained and untrained driving cycles.

## A. Tests on Trained Driving Cycles

The feasibility of the proposed online ecological energy management strategy was tested on the diverse driving cycles used for training. Figs. 8 and 9 compare the results of the

![img-9.jpeg](img-9.jpeg)

Fig. 9. Comparison of speed trajectories for HWFET-US06 cycle.
proposed management strategy and the off-line optimized trajectories for the driving cycle that combines the HWFET and US06. The initial SOC, $S O C_{\text {init }}$, was 0.7 . The red and blue lines represent the real-time results of the proposed strategy and offline optimization results, respectively.

SOC trajectories are compared in Fig. 8. The SOC trajectory generated by the proposed strategy matches the off-line optimized trajectory, indicating that the proposed strategy can provide near-optimal management. The final SOC values of the proposed strategy and offline optimization were 0.316 and 0.304 , respectively.

In Fig. 9, the upper and lower panels display the speed trajectories in the distance and time domains, respectively. The speed trajectory of the proposed online strategy is consistent with that of the offline optimization. Both the online and offline results are almost the same at lower speeds; however, the online results tend to be slower than the offline results at higher speeds. This is reasonable because energy consumption significantly increases at higher speeds. The amount of the tradeoff between energy consumption and driving time depends on the characteristics of driving cycles and can be controlled by the weight $\omega_{3}$ and the formulation of the speed deviation in (13). Consequently, as illustrated in the lower panel, the driving time increases by $1.2 \%$ from 1300 to 1315 s , whereas the total cost calculated by (14) decreases by $5.2 \%$ from 1.048 to 0.993 . Under a given driving condition, the decreasing rate of energy consumption is slightly larger than the increasing rate of the driving time. Considering the tradeoff between energy consumption and driving time, it was observed that the performance of the proposed strategy is comparable to that of the offline optimization.

The computational time at each location is crucial for realtime applications. The simulations were performed using an Intel i7-8700K core at a frequency of 3.7 GHz . The average and standard deviations of the computational time were 0.034 and 0.034 s , respectively. The maximum computational

TABLE II
Results for Diverse Trained Driving Cycles

| Driving cycles | Initial SOC | Results | Off-line optimized | Proposed strategy |
| :--: | :--: | :--: | :--: | :--: |
| HWFET- <br> 2TIMES | 0.6 | Total cost (\$) | 1.1717 | 1.1299 |
|  |  | Driving time (s) | 1544.6 | 1560.5 |
| ARTEMIS | 0.6 | Total cost (\$) | 1.3231 | 1.2612 |
| Motorway |  | Driving time (s) | 1075.7 | 1088.3 |
| UDDS- <br> 2TIMES | 0.6 | Total cost (\$) | 0.6326 | 0.5838 |
|  |  | Driving time (s) | 2027.6 | 2044.6 |
| US06 | 0.7 | Total cost (\$) | 0.3267 | 0.3254 |
| HWY |  | Driving time (s) | 371.0 | 372.2 |
| UDDS | 0.7 | Total cost (\$) | 0.2541 | 0.2620 |
|  |  | Driving time (s) | 1051.8 | 1051.8 |
| HWFET- <br> US06 | 0.7 | Total cost (\$) | 1.0128 | 0.9927 |
|  |  | Driving time (s) | 1308.1 | 1314.5 |
| US06 | 0.8 | Total cost (\$) | 0.4004 | 0.4089 |
|  |  | Driving time (s) | 537.2 | 527.1 |
| HWFET- <br> UDDS | 0.8 | Total cost (\$) | 0.8585 | 0.7822 |
|  |  | Driving time (s) | 1775.0 | 1798.2 |
| WLTC | 0.8 | Total cost (\$) | 0.6845 | 0.6628 |
|  |  | Driving time (s) | 1509.8 | 1523.1 |

time was 0.206 s , which is sufficiently short for real-time application.

The proposed strategy was tested over diverse driving cycles with different initial SOC conditions, which were also used to train the NNs. The results are listed in Table II. The dashed $(-)$ mark in the driving cycle name indicates that the driving cycle was generated by combining two cycles. In comparison with the offline optimization results, the proposed strategy resulted in a longer driving time by $0.5 \%$ and lower total cost to restore the consumed fuel and electricity by $2.7 \%$ on average. Considering the tradeoff between the cost and driving time, which can be adjusted by the weight $\omega_{3}$ in (13), the performance of the proposed strategy was comparable to that of the offline optimization.

Subsequently, the speed-up of the modified EDA was tested. The results listed in Table II were obtained using the modified EDA with five iterations. For the HWFET-US06 driving cycle with an initial SOC of 0.7 , a comparison of the total cost of the modified EDA with that of EDA with different numbers of iterations from 5 to 50 is shown in Fig. 10, wherein the blue circles represent the total cost resulting from an EDA and the red dashed line represents that of the modified EDA with five iterations. Evidently, the modified EDA with five iterations is comparable to the EDA with more than forty iterations.

## B. Tests on Untrained Driving Cycles

The feasibility of the proposed online ecological energy management strategy was evaluated on twelve driving scenarios, with four driving cycles and three initial SOC conditions that were not used to train the NNs. For comparison, the optimal trajectory in each scenario was obtained by off-line optimizing (14) using EDA and used as references.

Fig. 11 illustrates SOC trajectories for the driving cycle of US06-SC03 under an initial SOC condition of 0.7 . The red line represents the real-time results using the proposed online strategy and the blue line represents the offline optimization results. The SOC trajectory obtained using the proposed online

![img-10.jpeg](img-10.jpeg)

Fig. 10. Comparison of the modified EDA with an EDA.
![img-11.jpeg](img-11.jpeg)

Fig. 11. Comparison of SOC trajectories for US06-SC03 cycle.
![img-12.jpeg](img-12.jpeg)

Fig. 12. Comparison of speed trajectories for US06-SC03 cycle.
strategy is consistent with offline optimization, where the final SOC values were 0.315 and 0.300 , respectively. This implies that the power distribution in the proposed strategy can be optimal in the long term for untrained driving scenarios.

Fig. 12 presents a comparison of the vehicle speed trajectories in distance and time domains. The vehicle speed controlled by the proposed strategy conformed to the reference;
FIGLE III
RESULTS FOR UNTRAINED DRIVING CYCLES

| Driving cycles | Initial SOC | Results | Off-line optimized | Proposed strategy |
| :--: | :--: | :--: | :--: | :--: |
| UDDS- <br> HWFET | 0.6 | Total cost (\$) | 0.9180 | 0.8597 |
|  |  | Driving time (s) | 1803.9 | 1823.0 |
|  | 0.7 | Total cost (\$) | 0.8702 | 0.8293 |
|  |  | Driving time (s) | 1810.7 | 1823.9 |
|  | 0.8 | Total cost (\$) | 0.8299 | 0.7974 |
|  |  | Driving time (s) | 1812.3 | 1825.1 |
| $\begin{aligned} & \text { US06- } \\ & \text { SC03 } \end{aligned}$ | 0.6 | Total cost (\$) | 0.6090 | 0.5770 |
|  |  | Driving time (s) | 983.1 | 997.1 |
|  | 0.7 | Total cost (\$) | 0.5791 | 0.5493 |
|  |  | Driving time (s) | 983.3 | 997.8 |
|  | 0.8 | Total cost (\$) | 0.5290 | 0.5303 |
|  |  | Driving time (s) | 986.1 | 996.1 |
| FU505- <br> US06 | 0.6 | Total cost (\$) | 0.6425 | 0.6010 |
|  |  | Driving time (s) | 918.4 | 933.2 |
|  | 0.7 | Total cost (\$) | 0.5987 | 0.5751 |
|  |  | Driving time (s) | 923.2 | 933.2 |
|  | 0.8 | Total cost (\$) | 0.5530 | 0.5564 |
|  |  | Driving time (s) | 924.6 | 929.5 |
| $\begin{aligned} & \text { SC03- } \\ & \text { UDDS } \end{aligned}$ | 0.6 | Total cost (\$) | 0.4408 | 0.4051 |
|  |  | Driving time (s) | 1470.8 | 1495.2 |
|  | 0.7 | Total cost (\$) | 0.3847 | 0.3969 |
|  |  | Driving time (s) | 1464.5 | 1465.6 |
|  | 0.8 | Total cost (\$) | 0.3851 | 0.3867 |
|  |  | Driving time (s) | 1466.8 | 1496.4 |

however, at high speeds, it tended to be slightly lower than that of the offline optimization in the upper panel, which resulted in a longer driving time, as indicated in the lower panel. The resulting driving time of the proposed strategy was 997.8 seconds, which was $1.5 \%$ longer than that of the reference. The total cost of the proposed strategy was $5 \%$ lower than that of the reference. The average computational time at each location was 0.033 s with a standard deviation of 0.032 s . The maximum computation time was 0.190 s , which was sufficiently short for online management.

Table III lists the simulation results for twelve different driving scenarios, including four driving cycles of UDDSHWFET, US06-SC03, FU505-US06, and SC03-UDDS with three initial SOC conditions. These scenarios were not used in training. In comparison with the offline optimization results, the proposed strategy achieved a longer driving time by $1.1 \%$ and lower total cost by $3.3 \%$ on average.

## C. Tests on Changes in Traffic Conditions

The proposed strategy was applied to a situation in which the traffic conditions changed while driving. It was assumed that when departing, the driving cycle given via ITS and GPS was the US06-SC03 cycle and, when the vehicle passed the location at 10 km , parts of the future driving cycle were changed owing to heavy traffic.

In the upper panel of Fig. 14, the dashed line indicates the driving cycle without traffic, which corresponds to the driving cycle given when departing, and the solid line indicates the changed driving cycle owing to heavy traffic over areas from 15.1 km to 18.2 km . The average speed in the areas with heavy traffic was reduced by $20 \%$. For comparison, the changed driving cycle indicated by the solid line was optimized offline,

![img-13.jpeg](img-13.jpeg)

Fig. 13. Comparison of SOC trajectories for changes in traffic conditions during driving.
![img-14.jpeg](img-14.jpeg)

Fig. 14. Comparison of speed trajectories for changes in traffic conditions during driving.
which was hypothetically done on the assumption that future changes in traffic were known when departing, which could not be achieved in reality because the driving cycle was changed while driving.

Fig. 13 shows a comparison of the resulting SOC trajectory of the proposed strategy with that of the off-line optimized SOC trajectory. The initial SOC value was 0.7 . The red line is higher than the blue one, which means that the battery in the proposed strategy was less consumed because the strategy expected more energy consumption over the areas from 15.1 km to 18.2 km and kept more electric energy until the vehicle traveled 10 km . The final SOC values of the offline optimization and proposed strategy were 0.301 and 0.322 , respectively, which means that the proposed strategy consumed less electric energy by approximately $5.2 \%$.

The lower panel of Fig. 14 shows a comparison of the speed trajectories. It is shown that the proposed strategy could adapt to changes in traffic conditions during driving. The driving times for the offline optimization and proposed online strategy
were 1044 and 1049, respectively, and the corresponding total costs were 0.5507 and 0.5468 .

Simulations over diverse trained and untrained driving scenarios and unexpected changes in traffic revealed that the proposed online ecological energy management strategy can provide good performance, comparable to that of EDA offline optimization. The computational time was sufficiently short to be suitable for online management. Therefore, the proposed energy management strategy using RNN-based prediction and modified EDA-based optimization can produce near-optimal performance in real time.

## V. CONCLUSION

This study proposed a distance-based online ecological management strategy using optimal SOC prediction and stochastic optimization to optimize the power demand and distribution in real time and to adapt to the changes in traffic conditions. The optimal SOC value at the next location was predicted using an RNN from the computed energy-consumption features of the remaining driving cycle, which offered good guidance for long-term optimal power distribution. Driving to the next location was ecologically optimized using a modified EDA with a constraint on the predicted SOC value by considering the characteristics of the drivetrain, traffic, and route conditions. To accelerate the optimization, EDA was modified in two ways: initial populations were estimated using NNs and new populations were generated by combining the probability distribution and grid-based area searching models. The stochastic approach of the EDA can compensate for potential prediction errors in NNs. Simulations over multiple driving scenarios demonstrated that the proposed strategy could produce good performance comparable to that of offline optimization and its computational time is sufficiently short for real-time applications. Diverse prediction approaches, including deep learning, for more accurate SOC prediction, and fast stochastic optimization methods for finestep management, will be the subject of our future work.

## ACKNOWLEDGMENT

This work was conducted during the sabbatical year of Kwangwoon University in 2020.

## REFERENCES

[1] N. Jalil, N. A. Kheir, and M. Salman, "A rule-based energy management strategy for a series hybrid vehicle," in Proc. Amer. Control Conf., Albuquerque, NM, USA, 1997, pp. 689-693.
[2] Y. Zhu, Y. Chen, G. Tian, H. Wu, and Q. Chen, "A four-step method to design an energy management strategy for hybrid vehicles," in Proc. Amer. Control Conf., Boston, MA, USA, 2004, pp. 156-161.
[3] N. J. Schouten, M. A. Salman, and N. A. Kheir, "Fuzzy logic control for parallel hybrid vehicles," IEEE Trans. Control Syst. Technol., vol. 10, no. 3, pp. 460-468, May 2002.
[4] Y. Li, X. Lu, and N. C. Kar, "Rule-based control strategy with novel parameters optimization using NSGA-II for power-split PHEV operation cost minimization," IEEE Trans. Veh. Technol., vol. 63, no. 7, pp. 3051-3061, Sep. 2014.
[5] R. Lian, J. Peng, Y. Wu, H. Tan, and H. Zhang, "Rule-interposing deep reinforcement learning based energy management strategy for power-split hybrid electric vehicle," Energy, vol. 197, Apr. 2020, Art. no. 117297.

[6] J. Liu and H. Peng, "Modeling and control of a power-split hybrid vehicle," IEEE Trans. Control Syst. Technol., vol. 16, no. 6, pp. 1242-1251, Nov. 2008.
[7] Z. Chen, C. C. Mi, J. Xu, X. Gong, and C. You, "Energy management for a power-split plug-in hybrid electric vehicle based on dynamic programming and neural networks," IEEE Trans. Veh. Technol., vol. 63, no. 4, pp. 1567-1580, May 2014.
[8] Q. Gong, Y. Li, and Z.-R. Peng, "Trip-based optimal power management of plug-in hybrid electric vehicles," IEEE Trans. Veh. Technol., vol. 57, no. 6, pp. 3393-3401, Nov. 2008.
[9] T. Choe, A. Skabardonis, and P. Varaiya, "Freeway performance measurement system: Operational analysis tool," Transp. Res. Rec., J. Transp. Res. Board, vol. 1811, no. 1, pp. 67-75, Jan. 2002.
[10] California Dept. Transp., Sacramento, CA, USA. PeMS. [Online]. Available: http://pems.dot.ca.gov
[11] Wisconsin Traffic Operations and Safety Laboratory. Accessed: Mar. 17, 2020. [Online]. Available: http://transportal.cee.wisc.edu
[12] C. Musardo, G. Rizzoni, and B. Staccia, "A-ECMS: An adaptive algorithm for hybrid electric vehicle energy management," in Proc. 44th IEEE Conf. Decis. Control, Seville, Spain, Sep. 2005, pp. 1816-1823.
[13] D. Karbowski, J. Kwon, N. Kim, and A. Rousseau, "Instantaneously optimized controller for a multimode hybrid electric vehicle," in Proc. SAE, Detroit, MI, USA, Apr. 2010, pp. 1-22.
[14] D. Zhao, R. Stobart, G. Dong, and E. Winward, "Real-time energy management for diesel heavy duty hybrid electric vehicles," IEEE Trans. Control Syst. Technol., vol. 23, no. 3, pp. 829-841, May 2015.
[15] M. Montazeri-Gh and Z. Pourbafarani, "Near-optimal SOC trajectory for traffic-based adaptive PHEV control strategy," IEEE Trans. Veh. Technol., vol. 66, no. 11, pp. 9753-9760, Nov. 2017.
[16] D. Shi, S. Liy, Y. Cai, S. Wang, H. Li, and L. Chen, "Pontryagin's minimum principle based fuzzy adaptive energy management for hybrid electric vehicle using real-time traffic information," Appl. Energy, vol. 286, pp. 1-15, Jun. 2021.
[17] W. Lee, H. Jeoung, D. Park, T. Kim, H. Lee, and N. Kim, "A real-time intelligent energy management strategy for hybrid electric vehicles using reinforcement learning," IEEE Access, vol. 9, pp. 72759-72768, 2021.
[18] C. Sun, X. Hu, S. J. Moura, and F. Sun, "Velocity predictors for predictive energy management in hybrid electric vehicles," IEEE Trans. Control Syst. Technol., vol. 23, no. 3, pp. 1197-1204, May 2015.
[19] Y. Du et al., "The vehicle's velocity prediction methods based on RNN and LSTM neural network," in Proc. Chin. Control Decis. Conf. (CCDC), Hefei, China, Aug. 2020, pp. 99-102.
[20] J. Shin, K. Yeon, S. Kim, M. Sunwoo, and M. Han, "Comparative study of Markov chain with recurrent neural network for short term velocity prediction implemented on an embedded system," IEEE Access, vol. 9, pp. 24755-24767, 2021.
[21] X. Ma, Z. Tao, Y. Wang, H. Yu, and Y. Wang, "Long short-term memory neural network for traffic speed prediction using remote microwave sensor data," Transp. Res. C, Emerg. Technol., vol. 54, pp. 187-197, May 2015.
[22] K. Yeon, K. Min, J. Shin, M. Sunwoo, and M. Han, "Ego-vehicle speed prediction using a long short-term memory based recurrent neural network," Int. J. Automot. Technol., vol. 20, no. 4, pp. 713-722, Aug. 2019.
[23] P. G. Anselma, Y. Huo, J. Roeleveld, G. Belingardi, and A. Emadi, "Integration of on-line control in optimal design of multimode powersplit hybrid electric vehicle powertrains," IEEE Trans. Veh. Technol., vol. 68, no. 4, pp. 3436-3445, Apr. 2019.
[24] Z. Chen, C. Yang, and S. Fang, "A convolutional neural network-based driving cycle prediction method for plug-in hybrid electric vehicles with bus route," IEEE Access, vol. 8, pp. 3255-3264, 2020.
[25] J. Park, Z. Chen, and Y. L. Murphey, "Intelligent vehicle power management through neural learning," in Proc. Int. Joint Conf. Neural Netw. (IJCNN), Barcelona, Spain, Jul. 2010, pp. 1-7.
[26] T. Liu, X. Hu, S. E. Li, and D. Cao, "Reinforcement learning optimized look-ahead energy management of a parallel hybrid electric vehicle," IEEE/ASME Trans. Mechatronics, vol. 22, no. 4, pp. 1497-1507, Aug. 2017.
[27] A. Biswas, P. G. Anselma, and A. Emadi, "Real-time optimal energy management of electrified powertrains with reinforcement learning," in Proc. IEEE Transp. Electrific. Conf. Expo (ITEC), Detroit, MI, USA, Jun. 2019, pp. 1-6.
[28] C. Liu and Y. L. Murphey, "Optimal power management based on Q-learning and neuro-dynamic programming for plug-in hybrid electric vehicles," IEEE Trans. Neural Netw. Learn. Syst., vol. 31, no. 6, pp. 1942-1954, Jun. 2020.
[29] G. Du, Y. Zou, X. Zhang, T. Liu, J. Wu, and D. He, "Deep reinforcement learning based energy management for a hybrid electric vehicle," Energy, vol. 201, Jun. 2020, Art. no. 117591.
[30] T. Liu, X. Tang, H. Wang, H. Yu, and X. Hu, "Adaptive hierarchical energy management design for a plug-in hybrid electric vehicle," IEEE Trans. Veh. Technol., vol. 68, no. 12, pp. 11513-11522, Dec. 2019.
[31] H. He, Y. Wang, J. Li, J. Dou, R. Lian, and Y. Li, "An improved energy management strategy for hybrid electric vehicles integrating multistates of vehicle-traffic information," IEEE Trans. Transport. Electrific., vol. 7, no. 3, pp. 1161-1172, Sep. 2021.
[32] G. Li, J. Zhang, and H. He, "Battery SOC constraint comparison for predictive energy management of plug-in hybrid electric bus," Appl. Energy, vol. 194, pp. 578-587, May 2017.
[33] Y. Liu, J. Li, Z. Chen, D. Qin, and Y. Zhang, "Research on a multiobjective hierarchical prediction energy management strategy for range extended fuel cell vehicles," J. Power Sources, vol. 429, pp. 55-66, Jul. 2019.
[34] C. Sun, S. J. Moura, X. Hu, J. K. Hedrick, and F. Sun, "Dynamic traffic feedback data enabled energy management in plug-in hybrid electric vehicles," IEEE Trans. Control Syst. Technol., vol. 23, no. 3, pp. 1075-1086, May 2015.
[35] Z. Lei, D. Sun, J. Liu, D. Chen, Y. Liu, and Z. Chen, "Trip-oriented model predictive energy management strategy for plug-in hybrid electric vehicles," IEEE Access, vol. 7, pp. 113771-113785, 2019.
[36] H.-Q. Guo, G. Wei, F. Wang, C. Wang, and S. Du, "Self-learning enhanced energy management for plug-in hybrid electric bus with a target preview based SOC plan method," IEEE Access, vol. 7, pp. 103153-103166, 2019.
[37] H. Tian, X. Wang, Z. Lu, Y. Huang, and G. Tian, "Adaptive fuzzy logic energy management strategy based on reasonable SOC reference curve for online control of plug-in hybrid electric city bus," IEEE Trans. Intell. Transp. Syst., vol. 19, no. 5, pp. 1607-1617, May 2018.
[38] D. Hu, S. Cheng, J. Zhou, and L. Hu, "Energy management optimization method of plug-in hybrid-electric bus based on incremental learning," IEEE J. Emerg. Sel. Topics Power Electron., vol. 11, no. 1, pp. 7-18, Feb. 2023.
[39] C. Zheng, G. Xu, K. Xu, Z. Pan, and Q. Liang, "An energy management approach of hybrid vehicles using traffic preview information for energy saving," Energy Convers. Manage., vol. 105, pp. 462-470, Nov. 2015.
[40] L. Guo, B. Gao, Y. Gao, and H. Chen, "Optimal energy management for HEVs in eco-driving applications using bi-level MPC," IEEE Trans. Intell. Transp. Syst., vol. 18, no. 8, pp. 2153-2162, Aug. 2017.
[41] H. Lim and W. Su, "Hierarchical energy management for power-split plug-in HEVs using distance-based optimized speed and SOC profiles," IEEE Trans. Veh. Technol., vol. 67, no. 10, pp. 9312-9323, Oct. 2018.
[42] Argonne Nat. Lab., Lemont, IL, USA. (2017). Autonomie. [Online]. Available: http://www.autonomie.net
[43] N. Kim, M. Duoba, N. Kim, and A. Rousseau, "Validating volt PHEV model with dynamometer test data using autonomie," SAE Int. J. Passenger Cars-Mech. Syst., vol. 6, no. 2, pp. 985-992, Apr. 2013.
[44] H. Lim, W. Su, and C. C. Mi, "Distance-based ecological driving scheme using a two-stage hierarchy for long-term optimization and short-term adaptation," IEEE Trans. Veh. Technol., vol. 66, no. 3, pp. 1940-1949, Mar. 2017.
![img-15.jpeg](img-15.jpeg)

Hansang Lim (Senior Member, IEEE) received the B.S., M.S., and Ph.D. degrees from the School of Electrical Engineering, Seoul National University, Seoul, South Korea, in 1996, 1998, and 2004, respectively. He was with the Telecommunications Research and Development Center, Samsung Electronics Company Ltd., from 2004 to 2007. He is currently a Professor with the Department of Electronics Convergence Engineering, Kwangwoon University, Seoul. His research interests include low-noise, high-speed signal conditioning circuits, precise time measurements, electrical power distribution, in-vehicle network designs, and energy management in electrified vehicles.