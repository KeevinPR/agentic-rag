# Intelligent PHEV Charging and Discharging Strategy in Smart Grid 

Jie Yu, Member IEEE, Wei Gu, Member IEEE and Zaijun Wu, Member IEEE


#### Abstract

The anticipation of a large penetration of Plug-in Hybrid Electric Vehicles (PHEVs) and Plug-in Electric Vehicles (PEVs) into the market brings up many new technical problems that need to be addressed. In the near future, a large number of PHEVs/PEVs connected to power grids will add a large-scale energy load, as well as add substantial energy resources that can be utilized. Vehicle-toGrid (V2G) technology is a most promising opportunity in PHEV/PEV adoption. In this paper, the authors propose an intelligent method for optimally managing a large number of PHEVs/PEVs (e.g., 3,000) charging/discharging at a municipal parking deck. The authors used the Estimation of Distribution Algorithm (EDA) to determine the optimal charging/discharging times and patterns over a period of 24 hours. A mathematical framework for the objective function (i.e., maximizing the overall profit on a vehicle fleet base) is also given in detail. The authors characterized the performance of EDA-based energy management using a Matlab simulation, and compared it with other optimization techniques.


## I. INTRODUCTION

$\mathrm{E}=$CONOMIC and environmental incentives, as well as advances in technology, are reshaping the traditional view of power systems. PHEVs and PEVs have received increasing attention because of their low pollution emissions and high fuel economy. The US government puts a lot of effort into accelerating the introduction and penetration of advanced electric drive vehicles into the market. The US Department of Energy projects that approximately 1 million PHEVs/PEVs will be on the road by 2015 and $425,000 \mathrm{PHEVs} / \mathrm{PEVs}$ will be sold in 2015 alone. At this penetration rate, PHEVs would account for $2.5 \%$ of all new vehicle sales in 2015 [1]. The Electric Power Research Institute (EPRI) projects that $62 \%$ of the entire U.S. vehicle fleet will consist of PHEVs by 2050 using a moderate penetration scenario [2].

In [3], the authors provided a comprehensive survey on the electrification of transportation in a Smart Grid environment. In [4]-[6], the authors proposed computational intelligence-based centralized charging algorithms to achieve the optimal power allocation at a large-scale public PHEV/PEV charging facility. The authors evaluated the impact of the integration of PHEVs/PEVs into power grids under a variety of charging scenarios in [7]-[9]. In [10], the authors analyzed the optimal performance of the proposed charging algorithms under certain operating conditions and various types of

[^0]battery models. The authors further developed a digital testbed in order to evaluate a variety of charging algorithms and demonstrate the communications capabilities for a PHEV/PEV enabled charging facility [11]. The research work [12]-[14] consolidates the modeling and simulation of power distribution system and transportation network in order to assess the emerging electric vehicle technologies in Microgrid. To accommodate the high demand of renewable energy and the environment policy, the planning and operation of Micro-source generators has been studied using HOMER [15]. In [16], the authors proposed a detailed simulation model for flywheel energy storage. Simulation results show the accurate dynamic behavior of flywheel unit during charge and discharge modes.

Accordingly, there is a growing need to address the implications of this emerging technology on the power grid. A large market penetration of PHEVs/PEVs imposes additional stress on the power systems. Large numbers of PHEVs/PEVs have the potential to threaten the stability of the existing power grids. Moreover, due to variations in the needs of the PHEVs/PEVs connected to the power grids at any given time, the demand pattern will also have a significant impact on the electricity market.

There are approximately 250 million cars in the United States. By the year 2020, if $10 \%$ of US vehicles will be some form of PHEV or PEV and each vehicle has a storage capacity of $20 \mathrm{KWh}, 500 \mathrm{GWh}$ is both a threat to today's utility and an opportunity. If used wisely, these vehicles can become a distributed energy storage device (DESD) for the utility and hence can be dispatched to lower the peak demand, delay the construction of new power plants. In other words, PHEVs/PEVs also have the potential to transfer power to the grid to alleviate peak power demand and provide ancillary services to the grid [17]. Vehicle-to-Grid (V2G) technology is a most promising opportunity in PHEV/PEV adoption. The aggregated PHEV/PEV load can offer ancillary services such as voltage control, frequency regulation, regulation reserve, spinning reserve, and non-spinning reserve [18].

This paper addresses the optimal energy management for a real-world PHEV/PEV parking deck with V2G capability under various energy constraints. The remainder of this paper is organized as follows: Section II will describe the V2G problem solved in mathematical term. The overall objective is to maximize the profit on a vehicle fleet base. The authors will provide the optimization objective and certain system constraints, as well as the simulated data. According to the nature of the optimization problems considered in this paper, the authors proposed the Estimation of Distribution Algorithm (EDA) to regulate multiple battery charging/discharging from a cluster of PHEVs/PEVs appropriately. Section III will review the EDA-based method, as well as describe how the algorithm works for the proposed optimization problems. The results of the simulation, as well as further analysis of


[^0]:    This work is supported by Project 2011sd116018 from Nanjing Committee of Science and Technology, and project E070402 National Natural Science Foundation of China.
    J Yu (corresponding author) is with School of Electrical Engineering, Southeast University, Nanjing, Jiangsu Province, 210096, China. (Email:jxijx@seu.edu.cn)
    W Gu is with School of Electrical Engineering, Southeast University, Nanjing, Jiangsu Province, 210096, China. (Email:wgu@seu.edu.cn)
    Z Wu is with School of Electrical Engineering, Southeast University, Nanjing, Jiangsu Province, 210096, China. (Email:zjwu@seu.edu.cn)

the V2G challenge, are presented in Section IV. Finally, authors will summarize this paper in Section V.

## II. Problem Formulation

## A. Objective Function

This section formulates V2G problem in mathematical terms. In V2G mode, there is multiple buying (charging) and selling (discharging) transactions at any step $k$. Since EDA is a population-based optimization method, the problem can be represented as a 3-D matrix representation of an individual $X_{i d}$ in the population $X=\left[X_{1}, X_{2}, \ldots, X_{L}\right]$, as shown in Fig 1. $X_{i d}$ is the energy scheduling for all the vehicles over a period of time. The population is a threedimension matrix with the dimension equal to $N \times T \times L . N$ is the number of vehicles; $T$ is the maximum time step; $L$ is population size. The row/column information can be used to solve the optimal energy scheduling on a vehicle fleet base and judge whether the energy scheduling at any time step meets certain constraints.

The objective function being considered in this paper is to determine the feasible combinations of energy transaction in V2G mode that maximize the net profit of all vehicles over a period of 24 hours. In this paper, all the vehicles are assumed to have V2G capability. In other words, all the vehicles are equipped with advanced power electronic device supporting two-way power flow. All the vehicles also have two-way communication capabilities once they are plugged-in. Without loss of generality, the authors assume all the PHEVs/PEVs are charged/discharged within a certain time period (e.g., 24 hours). On a vehicle fleet base, the proposed objective function allows the system aggregator (e.g., parking deck operator) to maximize the profit by taking full advantage of V2G capability.
![img-0.jpeg](img-0.jpeg)

Fig. 1 A 3-D Matrix Representation of V2G Problem
The V2G revenue includes, but is not limit to, the net revenue by selling/buying electricity $R_{e}$, the regulation incentives from the utilities $R_{\text {reg }}$, and other incentives $R_{\text {other }}$ for the participation of V2G (e.g., extended battery warranty).

$$
R=R_{e}+R_{\text {reg }}+R_{\text {other }}
$$

The net revenue of energy transaction by charging/discharging PHEV/PEV battery is defined as:

$$
R_{e}=-\sum_{i=1}^{T} \sum_{k=1}^{T} x_{i}(k) \cdot \Delta t \cdot p(k)
$$

Where $p(k)$ is the real-time energy price at time step $k$; $x_{i}(k)$ is the energy transaction (e.g., charging and discharging process) for the $i$-th vehicle at time step $k$; Positive value of $x_{i}(k)$ indicates a charging process while negative value of $x_{i}(k)$ indicates a discharging process. $T$ is the total number of time steps. $\Delta t$ is the user-defined time step. $N$ is the total number of vehicles.

For spinning reserves and regulation services, the revenue for regulation service includes: 1) the capacity payment $R_{\text {reg_capacity }}$ for providing regulation capacity; 2) the energy payment $R_{\text {reg_electricity }}$ for providing regulation electricity.

$$
\begin{gathered}
R_{\text {reg }}=R_{\text {reg_electricity }}+R_{\text {reg_capacity }} \\
R_{\text {reg_electricity }}=\sum_{i=1}^{N} p_{\text {reg_electricity }} \cdot E_{i-F 2 G} \\
R_{\text {reg_capacity }}=\sum_{i=1}^{N} p_{\text {reg_capacity }} \cdot P_{i-F 2 G} \cdot T_{i-\text {park }} \\
E_{i-F 2 G}=-\sum_{k=1}^{T} \min \left[0, x_{i}(k)\right] \cdot \Delta t
\end{gathered}
$$

$E_{i-F 2 G}$ is the amount of energy delivered by the $i$-th vehicle for providing regulation electricity in V2G mode. $P_{i-F 2 G}$ is the amount of the contracted power capacity available by the $i$-th vehicle in V2G mode. Since the regulation dispatch is typically during a short period of time, $P_{i-F 2 G}$ is mainly determined by the power line limit (i.e., battery charging limit). $T_{\text {vpark }}$ is the time that the $i$-th vehicle is plugged-in; $R_{\text {reg_electricity }}$ is the price for regulation electricity ( $\$ / \mathrm{kWh})$; $R_{\text {reg_capacity }}$ is the price for regulation capacity ( $\$ / \mathrm{kW}-\mathrm{h})$.

The V2G cost includes, but is not limit to, the initial capital cost $C_{\text {capital }}$ (e.g., additional equipment supporting V2G), the cost of purchasing electricity which has been incorporated into $R_{e}$, the battery degradation cost $C_{\text {Degradation }}$ (e.g., battery temperature/aging effect), the additional operating cost $C_{\text {Operating }}$ (e.g., communication cost).

The initial capital cost $C_{\text {capital }}$ (e.g., additional equipment supporting V2G and additional operating cost $C_{\text {Operating }}$ (e.g., communication cost) can be taken into account as:

$$
C_{\text {fixed }}=C_{\text {capital }} \cdot \frac{d}{1-(1+d)^{-n}}+C_{\text {operating }}
$$

where $d$ is the daily rate of interest; $n$ is the lifespan; $\frac{d}{1-(1+d)^{-n}}$ is the capital recovery factor.

Frequent charging/discharging switch may significantly affect the PHEV/PEV battery life. It is important to consider and formulate the additional battery wear cost $C_{\text {wear }}$ in V2G mode. The battery lifetime published by manufactures usually assumes that the battery is fully charged and discharged each cycle at an ideal reference condition [19]. However, the frequent charging/discharging switch in V2G mode results in rapid battery wear. The battery degradation cost due to the participation of V2G can be expressed as a function of the actual battery cycle life.

Depth of Discharging (DoD) of the $i$-th vehicle battery in V2G mode is defined as:

$$
D o D_{i}=\frac{E_{i-F 2 G}}{\eta_{i n v} E_{i}}
$$

$\eta_{i n v}$ denotes the overall efficiency of the battery charger. In this paper, all the battery chargers are assumed to be identical with the same efficiency. $E_{i}$ is the stored energy

of the $i$-th vehicle battery in DC kwh; $E_{i-1 / 2 G}$ is the amount of energy delivered by the $i$-th vehicle in V2G mode.

According to the published literature [19], the relationship between battery cycle life $(L)$ can be formulated as a function of and $D o D$ depending on the type of battery (e.g., Lead-Acid, Lithium-Ion, and NiMH).

$$
L=f(D o D)
$$

The actual battery life in DC kwh is defined as: $L_{E-D o D}=E_{s} \cdot L$
$L$ is the actual battery cycle life, which is defined as a function of $D o D ; E_{s}$ is the stored energy in DC kwh.

The battery degradation cost $C_{\text {Degradation }}(\$ / \mathrm{kwh})$ can be defined as:

$$
C_{\text {Degradation }}=C_{\text {Battery }} / L_{E-D o D}
$$

Where $C_{\text {Battery }}$ is the battery capital cost.
Therefore, the battery degradation cost (\$) for the $i$-th EV battery due to the participation of V2G is formulated as:

$$
C_{i-\text { wear }}=2 \cdot E_{i-1 / 2 G} \cdot C_{\text {Degradation }, i}
$$

Then the additional battery cost $C_{\text {wear }}$ of a fleet of $\mathrm{PHEVs} / \mathrm{PEVs}$ in V2G mode is expressed as:

$$
C_{\text {wear }}=\sum_{i=1}^{N} C_{\text {Degradation }, i}
$$

Finally, the objective function becomes: $\max (J)$

$$
J=R_{s}+R_{\text {reg }}+R_{\text {other }}-C_{\text {wear }}-C_{\text {fixed }}
$$

## B. System Constraints

The primary energy constraints being considered include the power available from the utility ( $P_{\text {utility }}$ ) and the two-way power line capacity ( $x_{i, \min } x_{i, \max }$ ) for all EVs. The overall charging efficiency of the parking deck is described by $\eta$. From the system point of view, $\eta$ is assumed to be constant at any time step. So $C_{i, \text { min }}$ and $S o C_{i, \text { max }}$ is the userdefined battery State-Of-Charge (SOC) requirement for the $i$-th vehicle in order to reduce the risk of overcharging or over-discharging in V2G mode. The SOC ramp rate is limited by the constraint $\Delta S o C_{i, \text { max }}$. So $C_{i-\text { int }}$ is the initial SOC of the $i$-th vehicle. So $C_{i \text {-desired }}$ is the desired departure SOC for the $i$-th vehicle.

$$
\begin{gathered}
\sum_{i} x_{i}(k) \leq P_{\text {utity }}(k) \cdot \eta \\
x_{i, \text { thh }}(k) \leq x(k) \leq x_{i, \text { thh }}(k) \\
S o C_{i, \text { thh }} \leq S o C_{i}(k) \leq S o C_{i, \text { thh }} \\
0 \leq S o C_{i}(k+1)-S o C_{i}(k) \leq \Delta S o C_{\max } \\
S o C_{i}(T) \geq S o C_{i \text {-desired }}
\end{gathered}
$$

Where SOC is defined as:

$$
S o C_{i}(k)=\frac{\sum_{k=1}^{k} x_{i}(k) \cdot \Delta t+E_{i} \cdot S o C_{i-\text { int }}}{E_{i}}
$$

## C. Simulated Data

Many factors contributed to the energy management for large numbers of $\mathrm{PHEVs} / \mathrm{PEVs}$ in V2G mode. Due to the lack of real market data, some of parameters are estimated or simulated according to published work and public data.

Battery chargers fall into three categories by voltage and power level. Level 2 is typically described as the primary or standard method for both private and public charging, and specifies a single-phase branch circuit with typical voltage ratings from 208 VAC to 240 VAC. In this paper, all the battery chargers are assumed to be Level 2. Hence, $x_{i, \min }=-6.7 \mathrm{kWh}$ and $x_{i, \max }=6.7 \mathrm{kWh}$. The overall system efficiency is $90 \%$ all the time; the scheduling period is 24 hours; $n(k)$ is the number of EVs connected at any given sample time, $P_{\text {utity }}(k)=90 \% \times n(k) \times P_{i, \max }(k)$.

In this paper, the vehicle owners are assumed to sign contract with the parking deck operator in order to get some incentives in participation of V2G (e.g., capacity payment). According to the analysis on the historical data, the expected plug-in/out can be estimated. The detailed simulated data can be found in [4]-[6].

Battery is the most expensive component of $\mathrm{PHEVs} / \mathrm{PEVs}$. A number of battery technologies have been developed, namely, Lead-Acid, Nickel-Cadmium, Nickelmetal hydride (NiMH), ZEBRA, and Li-Ion. Lead-Acid is the cheapest and most common battery technology. Traditionally, most electric vehicles have used lead-acid batteries due to their mature technology, high availability, and low cost. But they have low energy density and short life cycle. Lead-Acid batteries power early-modern EVs such as the original versions of General Motors EV1. Due to the high power density and charge/discharge efficiency, Li-Ion batteries dominate the most recent group of EVs in development. NiMH batteries are now considered a relatively mature technology. They boast an energy density of $30-80 \mathrm{~Wh} / \mathrm{kg}$, far higher than the other two batteries. However, the disadvantages include the poor efficiency, high self-discharge, finicky charge cycles, and poor performance in cold weather. This paper is based on three types of battery technologies, namely, Lead-Acid, Li-Ion, and NiMH.

TABLE II
Characteristics of Three Battery Technologies [17]

For Lead-Acid battery, the relationship between battery cycle life and DoD can be expressed as a linear function:

$$
L=a \cdot D o D+b
$$

For Li-Ion battery, the relationship between battery cycle life and DoD can be expressed as a logarithmic function:

$$
L=a \cdot D o D^{-b}
$$

For NiMH battery, the relationship between battery cycle life and DoD can be expressed as a exponential function:

$$
L=\beta_{0}\left(\frac{D o D_{R}}{D o D}\right)^{\beta_{1}} \exp \left(\beta_{2} \cdot\left(1-\frac{D o D}{D o D_{R}}\right)\right)
$$

According to PJM market data [20-21], the price for regulation capacity $p_{\text {reg_capacity }}$ is $\$ 38.2 / \mathrm{MW}-\mathrm{h}$. The price

for regulation electricity $p_{\text {reg_electricity }}$ is assumed to be the average spot energy price $\$ 0.1 / \mathrm{kWh}$. The participated vehicles are awarded "free charging" when providing regulation services. In this paper, the Time-of-Use (TOU) pricing schedule provides two-tiered pricing for $\mathrm{PHEVs} / \mathrm{PEVs}$ with a dedicated meter for On- and Off-Peak time. Generally speaking, the electricity price will be cheaper during the low load period, and will be higher in the peak period. According to PJM recent study [20], OnPeak hours are 12:00-21:00 daily (including weekends) and Off-Peak hours are all other hours. Off-Peak prices are approximately $\$ 0.06017 / \mathrm{kWh}$ and On-Peak prices from summer and winter seasons were averaged to $\$ 0.14345 / \mathrm{kWh}$. Due to the lack of the operational data, the invariable component $R_{\text {value }}$ is assumed to be zero in this paper. In order to reduce the risk of overcharging or overdischarging battery in V2G mode, $S o C_{s, \max }$ and $S o C_{s, \max }$ is defined as $5 \%$ and $95 \%$ for all the vehicles, respectively. Since the overall objective is to take full advantage of the energy storage in $\mathrm{PHEVs} / \mathrm{PEVs}$, the desired departure $\mathrm{SOC} S o C_{s-d e i r a k}$ is set as a moderate level $50 \%$ for all the participated vehicles.

## III. Estimation of Distribution Algorithm

EDAs are evolutionary algorithms based on global statistical information extracted from promising solutions [22-23]. For most real-world problems, there is a reasonable assumption that good solutions have a similar structure in some sense. In brief, an EDA is mainly based on the global information. EDAs estimate the probability distribution of the most successful solutions and generate offspring by sampling the statistical model. Authors selected an EDA for solving this problem because it is robust for solving complex, large-scale, non-linear optimization problems (e.g. large-scale energy management for a PHEV/PEV enabled charging facility with V2G capability).

Generally speaking, the principal steps of an EDA in solving this problem can be summarized as follows.

1) As illustrated in Fig 1, generate a group of random solutions $X=\left[X_{1}, X_{2}, \ldots, X_{L}\right]$, ( $L$ is the size of population; $X_{j}$ is a possible energy scheduling in the feasible region. $X_{j}$ is a $N \times T$ matrix in which $N$ is the number of vehicles and $T$ is the maximum time instance. Since normally there is very little information about the global optima, these elements in $X_{j}$ (i.e., the amount of energy transaction for the $i$-th vehicle at time step $k$ ) are scattered over the search space as uniformly as possible.
2) Convert the constrained optimization problem into a simple unconstrained one by assigning a proper penalty to the constraint violation. Such a way can easily handle the constraints, eliminating the need for additional computation costs. Also, there is no limit to the number or format of the constraints.
3) One of the major issues in EDAs is how to select most successful ones from parents. A widely-used selection method is the truncation selection. Individuals are sorted according to their fitness values in Step (2).

Then select the best $n_{s}\left(n_{s}<L\right)$ candidates using a truncation selection.
4) Another major issue in EDAs is how to build up a statistical model (probability distribution model) to extract the global information from promising solutions. In this paper, a continuous Gaussian model with diagonal covariance matrix (GM/DCM) is used. Then update the probability distribution model using the selected $n_{s}$ solutions. The joint density function of the $l$-th generation is written as follow:
$p_{l}(x)=\prod_{i=1}^{n} g\left(x_{i} ; \mu_{i}^{l} ; \sigma_{i}^{l}\right)=\prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi} \sigma_{i}} e^{\frac{1}{2} \frac{n_{s}-n_{s}}{n_{s}} \frac{1}{n_{s}}}$
The joint probability distribution is a factorized as product of $N$ univariate and independent normal distributions. The two parameters mean $\mu_{i}^{l}$ and standard deviation $\sigma_{i}^{l}$ can be estimated.
5) Generate new solutions which have gene values $x_{i}$ with the probability $p_{l}\left(x_{i}\right)$ from step 4. The V2G energy management problem being considered in this paper is also subject to different constraints that limit the search space to a certain feasible region. Reset the individual value (i.e., the amount of power allocated to or absorbed from a specific vehicle) to the boundary if the constraints do not hold true.
6) Replace some members from the current population with offspring generated in previous step.
7) Repeat steps 2-6 until the maximum number of iterations or the minimum error criteria is met. Save the near-optimal solution (i.e., the feasible combinations of energy transaction in V2G mode that maximize the net profit of all vehicles over a period of 24 hours).
![img-1.jpeg](img-1.jpeg)

Fig. 2 EDA Framework
IV. Simulation Results and Analysis

The authors first simulated the optimal energy management program with a small-scale vehicle fleet. The optimization performance of EDA and Genetic Algorithm (GA) is compared in Table III. The energy schedule of is discretized into multiple sample time $\Delta t$ (i.e., 1 hour). In both EDA and GA, the maximum number of generations is limited to 100 ; the population size is 200 ; the initial population is the same; the simulation is repeated for 30 times.

In term of the average CPU time, EDA is almost half of GA. EDA is less time-consuming than GA because it does not perform selection and crossover operations. In general, the optimization performance mainly relies on the parameter settings, which is a big challenge for a researcher who has less experience. EDA requires few parameters to be tuned by users. Instead, EDAs extract

global statistical information from the promising solutions in order to generate offspring. In terms of the fitness values, as shown in Table III, EDA is also better than GA.

TABLE III
COMPARISON ON EDA AND GA WITH 240 Variables


Population-based optimization method is a stochastic method and the maximum number of internal iterations was limited, there existed the chance of generating different solutions at each run. Despite this potential for variation, the standard deviation of the fitness value in EDA was found to be less than $1.26 \%$ of the average, showing the accuracy and consistency of the final solutions.

The variation of fitness values with respect to the number of iterations in a typical run of EDA or GA is shown in Fig 2.

The blue and black markers represent the best fitness value and the mean value achieved by EDAs while the black line represents the best fitness value achieved by GA. Gradually, the entire population reached the nearoptima region, but the diversity of the population was still maintained. Eventually, they converged on the global nearoptima. An optimal fitness value of 97.1 was achieved at the $100^{\text {th }}$ generation. Fig 3 also concludes that the proposed EDA-based algorithm has high efficiency in solving V2G energy management.
![img-4.jpeg](img-4.jpeg)

Fig. 3 Variations of Fitness Values in EDA and GA with 240 Variables
To further analyze the simulation results, the authors increase the vehicle fleet size by a factor of 5 . In both EDA and GA, the maximum number of generations is limited to 100 ; the population size is 300 ; the initial population is still the same. The authors found that GA can't handle a large problem to some extent. By contrast, EDAs are fairly immune to the local minima and non-linear nature of the problems being considered in this paper. EDAs can reach the near-optimal solution at a reasonable convergence rate. Since the V2G problem incorporates multiple energy scheduling for a large number of $\mathrm{PHEVs} / \mathrm{PEVs}$, EDAs are particularly suitable for solving this problem with low computation costs when compared to other approaches (e.g., Genetic Algorithms).

Fig 4 shows the deep discharge effect on the battery cycle life in V2G mode. Fig 5 shows the battery
degradation cost ( $\$ / \mathrm{kWh}$ ) of different types of batteries with respect to DoD. Fig 6 compares the overall cost/profit with 3 types of PHEV/PEV batteries in V2G mode.
![img-5.jpeg](img-5.jpeg)

Fig. 4 Battery Cycle Life in V2G Mode
![img-4.jpeg](img-4.jpeg)

Fig. 5 Battery Degradation Cost in V2G Mode
![img-5.jpeg](img-5.jpeg)

Fig. 6 Variation of Cost/Profit with Different Types of Batteries in V2G Mode (Case 1 and 2)
The profit-to-cost ratio is defined as $\lambda=\frac{C_{\text {total }}}{R_{e}+R_{\text {reg }}}$
The comparison listed in Table III is also in favor of LiIon battery in V2G application.

TABLE III
Profit-cost Ratio with Different Types of Batteries


According to the simulation results, Li-Ion battery technology is the best candidate among three major battery technologies for V2G application. EV battery technology is not fully ready for a frequent switch between charging/discharging modes. The high opportunity cost of

batteries still prevents V2G from becoming a reality in near-term. At the current stage, the V2G economics are in favor of Li-Ion battery technology.

The issues with the commercially available batteries in the vehicle application include, but are not limit to: 1) Battery energy and power densities need to be further improved; 2) Battery life is an issue; 3) Battery safety must be assured, especially during fast charging and in hot weather; 4) Battery cost needs to be significantly reduced; 5) The power electronics technologies that interface the battery with the grid and the motor must be further improved to increase efficiency and reduce weight.

To the authors' best knowledge, most published work related to V2G concept mainly focus on the demonstration of the V2G capability. The mathematical framework and simulation results presented in this paper can be used as a reference for the policy maker and utilities to further access the cost and benefits of the commercial deployment of V2G in the near future.

## V. CONCLUSION

In this paper, the authors described the optimal energy management for a real-world PHEV/PEV parking deck with V2G capability from a mathematical perspective. In this model, the authors also considered the constraints imposed by the battery charging limit, the power line capacity, the desired departure SOC, certain battery requirements. In order to enable the smooth integration of PHEVs/PEVs into the power grid, the authors have applied an EDA-based approach to handle a large-scale V2G enabled energy scheduling.

In this paper, the authors used a PC to perform the calculations for algorithm testing. The simulation results were given to demonstrate the effectiveness of the proposed EDA-based approach in solving V2G problems at a municipal PHEV/PEV parking deck. Since an EDA explicitly extract global statistical information from promising solutions, it is immune to the potential local minimum and the non-linear nature of the problem. The simulation results also demonstrated that the algorithm converged to a better solution than some of the more traditional methods. In the future work, the temperature condition will be also taken into account to further model the battery degradation cost.

However, it is important to mention that V2G technology is still in the early deployment stage due to certain technical and economical issues. Although V2G is a promising concept, the following two major issues might delay its real-world implementation in the short term: 1) a two-way power/communication enabled system infrastructure; and 2) an unproven business model and economic justification.
