# Computational intelligence-based energy management for a large-scale PHEV/PEV enabled municipal parking deck 

Wencong Su*, Mo-Yuen Chow<br>Department of Electrical and Computer Engineering, North Carolina State University, Raleigh, NC 27606, USA

## A R T I C L E I N F O

Article history:
Received 29 June 2011
Received in revised form 5 November 2011
Accepted 30 November 2011
Available online 26 December 2011

Keywords:
Plug-in Hybrid Electric Vehicle (PHEV)
Plug-in Electric Vehicle (PEV)
Electric Vehicle (EV)
Smart Grid
Estimation of Distribution Algorithm (EDA)
Particle Swarm Optimization (PSO)


#### Abstract

There is a growing need to address the potential problems caused by the emergence of Plug-in Hybrid Electric Vehicles (PHEVs) and Plug-in Electric Vehicles (PEVs) within the next 10 years. In the near future, a large number of PHEVs/PEVs in our society will add a large-scale energy load to our power grids, as well as add substantial energy resources that can be utilized. The large penetration of these vehicles into the marketplace poses a potential threat to the existing power grid. The existing parking infrastructure is not ready for the large penetration of plug-in vehicles and the high demand of electricity. Nowadays, the advanced computational intelligence methods can be applied to solve large-scale optimization problems in a Smart Grid environment. In this paper, authors propose and implement a suite of computational intelligence-based algorithms (e.g., Estimation of Distribution Algorithm, Particle Swarm Optimization) for optimally managing a large number of PHEVs/PEVs charging at a municipal parking station. Authors characterize the performance of the proposed methods using a Matlab simulation, and compare it with other optimization techniques.


(c) 2011 Elsevier Ltd. All rights reserved.

## 1. Introduction

Economic and environmental incentives, as well as advances in technology, are reshaping the traditional view of power systems. Plug-in Hybrid Electric Vehicles (PHEVs) and Plug-in Electric Vehicles (PEVs) have received increasing attention because of their low pollution emissions and high fuel economy. In 2007, on a net basis, the United States imported $58 \%$ of the energy it consumed [1]. Most US imported oil comes from unstable regions, which is a potential threat to US national security. Ultimately, PHEVs/PEVs will transfer energy demands from crude oil to electricity for the personal transportation sector [2]. This shift will reduce pollution and alleviate security issues related to oil extraction, importation, and combustion. In the near future, not only do the PHEVs/PEVs utilize grid power for charging, they also have the potential to transfer power back to the grid in order to alleviate peak demand.

US government puts a lot of effort into accelerating the introduction and penetration of advanced electric drive vehicles into the market. The US Department of Energy (DOE) projects that approximately 1 million PHEVs will be on the road by 2015 and 425,000 PHEVs will be sold in 2015 alone. At this penetration rate, PHEVs would account for $2.5 \%$ of all new vehicle sales in 2015 [3]. The Electric Power Research Institute (EPRI) projects that $62 \%$ of the entire US vehicle fleet will consist of PHEVs by 2050 using a moderate penetration scenario [4]. There are approximately 250

[^0]million cars in the United States. By the year 2020, if $10 \%$ of US vehicles will be some form of PHEV or PEV and each vehicle has a storage capacity of $20 \mathrm{~kW} \mathrm{~h}, 500 \mathrm{GW} \mathrm{h}$ is both a threat to today's utility and an opportunity.

Accordingly, there is a growing need to address the implications of this emerging technology on the power grid. A large market penetration of PHEVs/PEVs imposes additional stress on the power systems. Large numbers of PHEVs/PEVs have the potential to threaten the stability of the existing power grids. For example, several thousand PHEVs/PEVs may be introduced into the system over a short period of time (e.g., during the early morning hours when people arrive at work). Moreover, due to variations in the needs of the PHEVs/PEVs connected to the power grids at any given time, the demand pattern will also have a significant impact on the electricity market.

In the future, electric-powered vehicles will be plugged into the grid, and their onboard energy storage systems will be recharged using clean, renewable electricity. If properly managed, plug-in vehicles could be charged during low demand periods when there is excess capacity on the grid, minimizing the strain on the grid and obviating major generation and transmission infrastructure additions. One of the key missions is to facilitate the smooth interaction between the vehicle and the grid. In order to maximize customer satisfaction and minimize disturbances to the grid, a sophisticated controller will need to be designed in order to regulate multiple battery loads from a cluster of PHEVs/PEVs appropriately. This controller must take into consideration real-world constraints (e.g., battery requirement, user preference, and energy price). The


[^0]:    * Corresponding author. Tel.: +13155283344.

    E-mail addresses: wsu2@ncsu.edu (W. Su), chow@ncsu.edu (M.-Y. Chow).

algorithm should also be robust to uncertainty, be capable of making decisions in real-time with limited communication bandwidth, and work seamlessly with existing utilities.

Computational intelligence is a set of nature-inspired computational methodologies and approaches to address complex problems of the real-world applications. Many computational intelligence based methods (e.g., fuzzy logic, neural networks and evolutionary computation) have been applied to solve a variety of problems in different application areas. According to the nature of the optimization problems considered in this paper, the computational intelligence based methods can achieve the optimal energy management at a large-scale PHEV/PEV enabled municipal parking deck in near real time.

In [5], the authors provided a comprehensive survey on the electrification of transportation in a Smart Grid environment. The authors evaluated the impact of the integration of PHEVs/PEVs into power grids under a variety of charging scenarios in [6]. A theoretical system of PHEV/PEV municipal parking deck was studied in [7]. In [8], the authors applied the Monte Carlo method to simulate the real-world scenarios possible at a municipal parking deck. In [9], the authors demonstrated that PHEVs/PEVs have the potential to provide a significant amount of demand response. In [10], the authors analyzed the optimal performance of the proposed charging algorithms under certain operating conditions and various types of battery models. In [11], [12], the authors proposed centralized charging algorithms to achieve the optimal power allocation at a large-scale public charging facility. The authors further developed a digital testbed in order to evaluate a variety of charging algorithms and demonstrate the communications capabilities for a PHEV/PEV enabled charging facility in [13]. In [14], the authors proposed the optimal energy scheduling at a municipal PHEV/ PEV parking deck via multi-objective optimizations (e.g., minimizing the peak demand, maximizing the customer preference, and minimizing the charging cost). Vehicle-to-Grid (V2G) technology is a most promising opportunity in PHEV/PEV adoption. In [15], the authors achieved the optimal energy management for PHEV/ PEV enabled charging facilities with V2G capability.

This paper addresses the performance evaluation of different online charging strategies in a PHEV/PEV enabled parking deck under various operating conditions and real-world energy constraints. This paper also evaluates and compares the optimal performance of the proposed computational intelligence-based large-scale charging algorithms.

The remainder of this paper is organized as follows: in Section 2, the authors describe the mathematical framework for the objective function (i.e., maximizing the average State-of-Charge at the next time step) on a vehicle fleet base. The authors propose an accurate modeling of PHEV/PEV battery and simulate the real-world scenarios at a municipal parking deck (e.g., plug-in time, initial SoC, expected charging time) according to the statistical analysis based on transportation data. The proposed optimization model considers real-world constraints such as energy price, remaining battery capacity, and remaining charging time. In Section 3, the authors review the proposed methods (e.g., EDA, PSO, IPM), as well as describe how the algorithm works for the proposed optimization problems. In Section 4, the authors investigate and compare the use of the proposed methods for developing real-time, large-scale optimizations for allocating power to PHEVs/PEVs at a municipal parking deck. Finally, the authors summarize this paper in Section 5.

## 2. Materials and methods

Fig. 1 illustrates an envisioned architecture of a large-scale PHEV/PEV enabled municipal parking deck in a Smart Grid environment. As shown in Fig. 1, the proposed system consists of three
![img-0.jpeg](img-0.jpeg)

Fig. 1. Envisioned large-scale PHEV/PEV charging/V2G infrastructure in a Smart Grid environment.
major subsystems: (1) The Traditional Power Utility and Local-scale Renewable Energy Resource (PHEV/PEV onboard energy storage systems are recharged using either renewable energy or traditional energy source); (2) An Intelligent Grid Aggregator/ Operator (online charging algorithms for large population of PHEV/PEV); (3) PHEV/PEV with On-board Battery Management System, Battery Chargers, and Customers. It is important to mention that the two-way electrical energy flow and communications network are represented by the black arrow. A reliable two-way communication network is needed to enable the successful integration of a large number of PHEVs/PEVs. Having effective communications technologies is critical to achieve the optimal results. In this paper, all the vehicles are assumed to have two-way communication capabilities once they are plugged-in. In addition, all the vehicles are equipped with advanced power electronic device supporting variable power flow.

The energy management is embedded in the second subsystem, which is in the solid red ${ }^{1}$ block in Fig. 1. Ideally, the energy management system needs to not only handle static optimization (e.g., single objective optimization given a certain constraints), but also handle multi-objective optimization (e.g., multi-objective energy scheduling: minimizing energy usage, minimizing peak demand, minimizing charging cost, maximizing customer preference, etc.), dynamic optimization (e.g., plug-and-play operation), and predictive optimization (e.g., $N$-time step ahead prediction).

### 2.1. Objective function

Depending on the locations of the charging facility, the control of PHEV charging can be categorized into two groups: (1) home charging and (2) public charging. The aggregate load in a public charging facility needs to be managed carefully in order to avoid interruptions when several thousand PHEVs/PEVs are introduced into the system over a short period of time. To achieve the intelligent energy management at public charging facilities, a number of objective functions can be formulated depending on user preference and interest. For example, Galus and Andersson [16] proposed the multi-agent-based energy hub system for PHEV integration and managed recharging behavior for a large number of PHEVs considering dynamic prices. Clement-Nyns et al. [17] formulated the objective function to minimize power losses and voltage deviations in distribution systems. Sortomme et al. [18] devised three

[^0]
[^0]:    ${ }^{1}$ For interpretation of color in Figs. 1 and 5-14, the reader is referred to the web version of this article.

objective functions, namely, minimizing losses, maximizing load factor, and minimizing load variance.

Without loss of generality, the authors assume all the PHEVs/ PEVs participate in the energy management within a certain time period (e.g., 24 h ). The energy management time is discretized into multiple time intervals $\Delta t$. The objective function considered in this paper is the maximization of the average State-of-Charge (SoC) for all vehicles at the next time step. The authors consider the energy price, charging time, and current SoC in this model to allow the vehicles to join the charging system dynamically. In order to make the system more robust, the proposed system will also allow vehicles to leave prior to their expected departure time (i.e., the vehicle is unplugged abruptly). This would result in a serious failure in terms of optimal power allocation, and the PHEV/PEV battery may not be adequately charged (even if it has been plugged-in for a long time) [19]. Therefore, the proposed function aims at ensuring some fairness in the SoC-distribution at each time step. This will help ensure that a reasonable level of battery power is attained, even in the event of an early departure.

Maximize the objective function $J$ at any given time $k$
$J(k)=\sum_{i} w_{i}(k) \cdot \operatorname{SoC}_{i}(k+1)$,
$w_{i}(k)=f\left(\operatorname{Cap}_{c j}(k), T_{c j}(k), D_{i}(k)\right)$,
$\operatorname{Cap}_{c j}(k)=\left(1-\operatorname{SoC}_{i}(k)\right) \cdot \operatorname{Cap}_{i}$,
where $\operatorname{Cap}_{c j}(k)$ is the remaining battery capacity needed to be filled for the $i$ th vehicle at time step $k ; \operatorname{Cap}_{i}$ is the rated battery capacity (A h) of the $i$ th vehicle. Fig. 2 illustrates the relationship between $\operatorname{Cap}_{i}$ and $\operatorname{SoC}_{i}(k), T_{c j}(k)$ is the remaining time for charging the $i$ th vehicle at time step $k ; D_{i}(k)$ is the price difference between the real-time energy price and the price that the specific customer at the $i$ th vehicle battery charger is willing to pay at time step $k$; $w_{i}(k)$ is the charge weighting term of the $i$ th vehicle at time step $k$ (this is a function of the energy price, the remaining charging time, and the present SoC); $\operatorname{SoC}_{i}(k+1)$ is the state of charge of the $i$ th vehicle at time step $k+1$.

The weighting term gives a reward proportional to the attributes of a specific vehicle. For example, if a vehicle has a lower initial SoC and less remaining charging time, but the driver is willing to pay a higher price, the controller allocates more power to this vehicle battery charger:
$w_{i}(k) \propto\left[\operatorname{Cap}_{c j}(k)+D_{i}(k)+1 / T_{c j}(k)\right]$.
Since the three terms $\operatorname{Cap}_{c j}(k), D_{i}(k), 1 / T_{c j}(k)$ are not on the same scale, all terms need to be normalized in order to assign reasonable importance to each other.

The parking deck operators may also have different interests and assign different importance factors to $c_{c j}(k), t_{i}(k)$, and $d_{i}(k)$ depending on their own preferences, $\alpha$ is this user-defined parameter. Thus,
$w_{i}(k)=\alpha_{1} c_{c j}(k)+\alpha_{2} t_{i}(k)+\alpha_{3} d_{i}(k)$,
![img-1.jpeg](img-1.jpeg)

Fig. 2. The illustration of the remaining battery capacity.
$\alpha_{1}+\alpha_{2}+\alpha_{3}=1$
$\alpha_{1}, \alpha_{2}, \alpha_{3} \geqslant 0$
The charging current is also assumed to be constant over $\Delta t$.
$\left[\operatorname{SoC}_{i}(k+1)-\operatorname{SoC}_{i}(k)\right] \cdot \operatorname{Cap}_{i}=Q_{i}=I_{i}(k) \Delta t$,
$\operatorname{SoC}_{i}(k+1)=\operatorname{SoC}_{i}(k)+I_{i}(k) \Delta t / \operatorname{Cap}_{i}$,
where $\Delta t$ is the sample time defined by the parking deck operators, and $I_{i}(k)$ is the charging current over $\Delta t$.

The battery model is considered to be a capacitor circuit, were $C_{i}$ is the battery capacitance (Farad). The model is described as
$C_{i} \cdot d V_{i} / d t=I_{i}$.
Therefore, over a short period of time, one can approximate the voltage change to be linear,
$C_{i} \cdot\left[V_{i}(k+1)-V_{i}(k)\right] / \Delta t=I_{i}$,
$V_{i}(k+1)-V_{i}(k)=I_{i} \Delta t / C_{i}$.
Since the decision variable is the power allocated to the vehicles, replace $I_{i}(k)$ with $P_{i}(k)$
$I_{i}(k)=\frac{P_{i}(k)}{0.5 \times\left[V_{i}(k+1)+V_{i}(k)\right]}$.
Substituting $I_{i}(k)$ into (12) yields
$V_{i}(k+1)=\sqrt{2 P_{i}(k) \Delta t / C_{i}+V_{i}^{2}(k)}$.
Substituting (13) and (14) into (9) yields
$\operatorname{SoC}_{i}(k+1)=\operatorname{SoC}_{i}(k)+\frac{2 P_{i}(k) \Delta t}{\operatorname{Cap}_{i} \cdot\left[V_{i}(k+1)+V_{i}(k)\right]}$.
Finally, the objective function becomes
$J(k)=\sum_{i} w_{i} \cdot\left[\operatorname{SoC}_{i}(k)+\frac{2 P_{i}(k) \Delta t}{\operatorname{Cap}_{i} \cdot\left[\sqrt{\frac{2 P_{i}(k) \Delta t}{C_{i}}}+V_{i}^{2}(k)+V_{i}(k)\right]}\right]$.

### 2.2. System constraints

The primary energy constraints being considered in this paper include the power available from the utility ( $P_{\text {utility }}$ ) and the maximum power ( $P_{\text {cmax }}$ ) that can be absorbed by a specific vehicle. The power demand of a PHEV/PEV cannot exceed the rated power output of the battery charger,
$\sum_{i} P_{i}(k) \leqslant P_{\text {utility }}(k) \times \eta$,
$0 \leqslant P_{i}(k) \leqslant P_{\text {cmax }}(k)$.
The overall charging efficiency of the parking deck is described by $\eta$. From the system point of view, $\eta$ is assumed to be constant at any time step.
$\mathrm{SoC}_{\text {cmax }}$ is the user-defined maximum battery SoC limit for the $i$ th PHEV/PEV. Once $\mathrm{SoC}_{i}$ reaches $\mathrm{SoC}_{i \text { max }}$, the $i$ th battery charger switches to a stand-by mode so as to reduce the risk of overcharging. In order to avoid large variations in charging rate over consecutive time steps, the SoC ramp rate is limited by the constraint $\Delta \mathrm{SoC}_{\text {max }}$. To accommodate the system dynamics, the energy scheduling is updated when (1) utility information updates; (2) a new vehicle is plugged-in; and (3) sample time $\Delta t$ has passed periodically.

$0 \leqslant \mathrm{SoC}_{i}(k) \leqslant \mathrm{SoC}_{\mathrm{i}, \max }$.
$0 \leqslant \mathrm{SoC}_{i}(k+1)-\mathrm{SoC}_{i}(k) \leqslant \Delta \mathrm{SoC}_{\max }$.

### 2.3. Battery model

Energy storage is the key enabling technology for EVs. Accurate battery state information is critical to ensure optimal utilization of available energy and to enable optimal control of the battery's charging and discharging process. A simple linear battery model cannot reflect the highly non-linear battery dynamics. More specifically, Fig. 3 shows the battery SoC-VoC relationship under various operating conditions. At the very beginning, VoC can be assumed to have a linear relationship with SoC. When SoC $>20 \%$, the relationship between SoC-VoC is highly non-linear. It is very important to gain precise knowledge of the battery state while the battery is being used. The needed battery state information (e.g., SoC) can only be obtained from an accurate battery model.

In the following sections, an accurate PHEV/PEV battery cell was scaled up to a certain level to represent a weighted average of PHEV/ PEV batteries. This battery cell model takes into account both the relaxation and hysteresis effects [10], as shown in Fig. 4. This general battery cell model is computationally simple enough for online usage and provides accurate results for a wide range of battery types and operating conditions. It is important to mention that the battery pack configuration was not taken into account in the following simulation. In this paper, the vehicle fleet includes several types of PHEVs/PEVs, namely, regular PHEVs ( 6 kW h battery capacity), small PEVs ( 12 kW h battery capacity), medium PEVs ( 24 kW h battery capacity), and heavy PEVs ( 30 kW h battery capacity).

### 2.4. Simulated input data

Many factors contributed to the energy management for large numbers of PHEVs/PEVs. Due to the lack of real market data, some of parameters (e.g., plug-in time, expected plug-out time, initial SoC, and battery capacity) are estimated or simulated according to published work and the statistical analysis on public data.

Battery chargers fall into three categories by voltage and power levels, as shown in Table 1. Level 2 is typically described as the "primary" and "standard" method for both private and public charging facilities, and specifies a single-phase branch circuit with typical voltage ratings from 208 VAC to 240 VAC. In this paper, all the battery chargers are assumed to be Level 2. Hence, $P_{\mathrm{i}, \max }=6.7 \mathrm{~kW} \mathrm{~h}$. The overall system efficiency is $90 \%$ all the time; $n(k)$ is the number of PHEVs/PEVs connected at any given sample time $k ; P_{\text {untry }}=90 \% \times n(k) \times P_{\text {i,max }}(k)$.

According to the analysis on the historical data, the expected plug-in/out can be estimated. To take into account the uncertainty and the limits on the random variables, a truncated normal distri-
![img-2.jpeg](img-2.jpeg)

Fig. 3. SoC-VoC relationship under various operating conditions.
![img-3.jpeg](img-3.jpeg)

Fig. 4. The equivalent circuit of an accurate battery cell model.

Table 1
US standard electric vehicle charging level.
bution was suggested in [20] to represent the parking time and the time at which vehicles complete the morning commute. Let $X \sim N\left(\mu, \sigma^{2}\right)$ be a normal distribution $\Phi$ with the mean $\mu$ and the variance $\sigma^{2}$. The parking time and the expected arrival time lie within the corresponding interval $(\alpha, b)$. The probability density distribution is given by:
$f(x ; \mu, \sigma, a, b)=\frac{\frac{1}{\mu} \Phi\left(\frac{\alpha-\mu}{\sigma}\right)}{\Phi\left(\frac{\alpha-\mu}{\sigma}\right)-\Phi\left(\frac{\alpha-\mu}{\sigma}\right)}$.
Figs. 5 and 6 illustrate the probability density function of the simulated plug-in time and the simulated plug-out time for a large fleet of vehicles.

To validate the probabilistic modeling, the authors generate the random input under a truncated normal distribution and then compare the simulation result with the historical data of an office parking deck in the city of Livermore, CA, during weekdays [21]. For the most part, the simulated number of PHEVs/PEVs connected to the grid at any given time matches the actual data quite well, as shown in Fig. 7.

The initial SoC indicates the remaining energy stored in the vehicle battery pack, which can be modeled as a random variable under log-normal distribution as found by [22,23]. In this paper, the average mileage per day per vehicle is assumed to be 32 miles. Accordingly, the daily distance is log-normally distributed with a mean of 32 miles and a standard deviation of 24 miles. EV battery range spans from 20 miles to 300 miles depending on the number and type of battery, weather, driving behavior, and terrain, which is out of scope in this paper. Thus, in the following simulation, the average battery range is simply assumed to be 100 miles. The relationship between initial SoC and typical daily travel distance is proposed in [24]. The initial SoC expressed in percent is $X$. The average battery range in miles is $R$. The probability density function of the daily mileage is $D$.
$f(X)=R^{2} / 100 \cdot D \cdot(1-X / 100)$.
Fig. 8 shows the corresponding probability density function obtained by applying statistical analysis on the typical driving pattern as well as the average PHEV/PEV travel range.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Probability density function of plug-in time.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Probability density function of plug-out time.

## 3. Theory

### 3.1. Estimation of Distribution Algorithm (EDA)

EDAs are evolutionary algorithms based on global statistical information extracted from promising solutions [25,26]. For most real-world problems, there is a reasonable assumption that good solutions have a similar structure. In brief, an EDA is mainly based on the global information. EDAs estimate the probability distribution of the most successful solutions and generate offspring by sampling the statistical model. The authors selected an EDA for solving this problem because it is robust for solving complex, large-scale, non-linear optimization problems (e.g. large-scale en-
ergy management for a PHEV/PEV enabled charging facility). An EDA-based charging algorithm was put forward in [12] to achieve the optimal energy allocation to a large number of PHEVs/PEVs at a municipal parking deck. Generally speaking, the principal steps of an EDA in solving this problem can be summarized as follows:
(1) Generate a group of random solutions $P=\left[p_{1}, p_{2}, p_{3}, \ldots, p_{n}\right]$ ( $n$ is the number of vehicles connected to grids at this time step; $p_{j}$ is the possible power allocation to the $j$ th PHEV/ PEV battery) in the feasible region. Since normally there is very little information about the global optima, these solutions are scattered over the search space as uniformly as possible.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Typical parking utilization over a period of 24 h .
![img-7.jpeg](img-7.jpeg)

Fig. 8. Probability density function of a typical initial SoC.
(2) Convert the constrained optimization problem into a simple unconstrained one by assigning a proper penalty to the constraint violation. Such a way can easily handle the constraints, eliminating the need for additional computation costs. Also, there is no limit to the number or format of the constraints.
(3) One of the major issues in EDAs is how to select most successful ones from parents. A widely-used selection method is the truncation selection. Individuals are sorted according to their fitness values in step (2). Then select the best $n_{s}$ ( $n_{s}<L$ ) candidates using a truncation selection.
(4) Another major issue in EDAs is how to build up a statistical model (probability distribution model) to extract the global information from promising solutions. In this paper, a continuous Gaussian model with diagonal covariance matrix (GM/DCM) is used. Then update the probability distribution model using the selected $n_{s}$ solutions. The joint density function of the $i$ th generation is written as follow:

$$
p_{f}(x)=\prod_{i=1}^{N} g\left(x_{i} ; \mu_{i}^{i} ; \sigma_{i}^{i}\right)=\prod_{i=1}^{N} \frac{1}{\sqrt{2 \pi} \bar{\sigma}_{i}} e^{j\left(\frac{x_{i}-\mu_{i}^{i}}{\sigma_{i}^{i}}\right)^{2}}
$$

The joint probability distribution is a factorized as product of $N$ univariate and independent normal distributions. The two parameters mean $\mu_{i}^{i}$ and standard deviation $\sigma_{i}^{i}$ can be estimated.
(5) Generate new solutions which have gene values $x_{i}$ with the probability $p_{f}\left(x_{i}\right)$ from step 4. Energy scheduling at a PHEV/ PEV parking deck is also subject to different constraints that limit the search space to a certain feasible region. Reset the individual value (i.e., the amount of power allocated to a specific vehicle) to the boundary if the constraints do not hold true.
(6) Replace some members from the current population with offspring generated in previous step.

(7) Repeat steps 2-6 until the maximum number of iterations or the minimum error criteria is met. Save the near-optimal solution (i.e., the amount of power allocated to each PEHVs/ PEVs under a set of system constraints).

### 3.2. Particle Swarm Optimization (PSO)

PSO is an iterative stochastic optimization method. It simulates the behavior of flocks of birds or schools of fish. In 1995, Kennedy and Eberhart presented a new, evolutionary computation algorithm called Particle Swarm Optimization (PSO) [27,28]. In PSO, each solution is a "bird" (or, more generally, a "particle") in the search space. All of the particles have (1) fitness values (which are evaluated by the fitness function to be optimized) and (2) velocities (which direct the flying of the particles). The particles fly through the search space by following the current optimum particles. At each iteration, each of the particles is updated by following the individual and group bests. Gradually, the particles tend toward the global "near-optima" region. A PSO-based control algorithm was put forward in [11] to optimally allocate power to PHEVs at a municipal parking deck. Generally speaking, the principal steps in PSO can be summarized as follows:
(1) Generate a group of random solutions (particles) in the feasible region. Since we normally have very little information about the global optima, these particles are scattered over the search space as uniformly as possible.
(2) Evaluate the distance between the new solution and the desired solution based upon a fitness function.
(3) Compare the fitness value at the current iteration with previous best, and update the individual best (phest) and group best (gbest).
(4) Update the velocities of the particles according to Eq. (24). Clamp the velocities if $\left|V_{\text {id }}(k)\right|>V_{\max }$ (where $V_{\max }$ is the velocity limit). If $V_{\max }$ is too small, the particles may become trapped in a local region. However, if $V_{\max }$ is too large, the particles are more likely to skip the best regions. In practice, $V_{\max }$ is often set at $10-20 \%$ of the range of the variables over a particular dimension.
(5) Update the positions of the particles according to Eq. (25).
(6) Repeat steps 2-5 until the maximum number of iterations or the minimum error criteria is met.

$$
\begin{aligned}
V_{\text {id }}(k+1)= & \omega \cdot V_{\text {id }}(k)+\alpha_{1} \cdot \operatorname{rand}_{1} \cdot\left(\text { pbest }_{\text {id }}-X_{\text {id }}(k)\right) \\
& +\alpha_{2} \cdot \operatorname{rand}_{2} \cdot\left(\text { gbest }_{\text {id }}-X_{\text {id }}(k)\right) \\
X_{\text {id }}(k+1)= & X_{\text {id }}(k))+V_{\text {id }}(k+1)
\end{aligned}
$$

where $V_{\text {id }}(k)$ is the velocity of the individual particle at iteration $k$; rand ${ }_{1}$ and rand ${ }_{2}$ are uniform random numbers between 0 and $1 ; X_{\text {id }}(k)$ is the position of a particle at iteration $k$; gbest is the best value achieved by the individual so far; gbest is the best value of the group; $\alpha_{1}$ and $\alpha_{2}$ represent the cognitive constant and social constant respectively. These constants represent the weights for the stochastic acceleration terms. In general, $\alpha_{1} \cdot \alpha_{1}=4$; to begin, $\alpha_{1}=\alpha_{1}=2$. Finally, $\omega$ is the inertia constant that balances the information sharing between an exploratory mode versus an exploitative mode. In practice, $\omega$ often decreases linearly from 0.9 to 0.4. Initially, a higher value allows particles to move freely throughout the search space to find the global optima. Once a near-optimal region is reached, $\omega$ is decreased to a lower value in order to more narrowly define the search. Therefore, $\omega$ is given according to the following equation [29]

$$
\omega=\omega_{\max }-\frac{\omega_{\max }-\omega_{\min }}{\text { iter }_{\max }} \cdot \text { iter }
$$

### 3.3. Interior point method

The interior-point approach to constrained minimization is to solve a sequence of approximate minimization problems. The original objective function is expressed as:
$\operatorname{Min} f(x)$,
where $x \in R^{N}$ and $N$ is the number of variables,
Subject to $g(x)=0$,
$h_{\text {low }} \leqslant h(x) \leqslant h_{\text {high }}$,
$x_{i} \leqslant x \leqslant x_{0}$.
Here, $g(x)$ is the function of equality constraint, and $h(x)$ is the function of inequality constraint.

This algorithm follows a barrier approach, where the bound constraints are replaced by logarithmic barrier terms which are added to the objective function, to give:
$\operatorname{Min} f(x)-\mu\left(\sum_{k=1}^{n} \ln l_{k}\right)-\mu\left(\sum_{k=1}^{n} \ln u_{k}\right)$,
Subject to $g(x)=0$,
$l_{k}=\left(x^{(k)}-x_{k}^{(k)}\right)$,
$u_{k}=\left(x_{0}^{(k)}-x^{(k)}\right)$,
$h(x)+u-h_{\text {high }}=0$,
$h(x)-l-h_{\text {low }}=0$.
where a barrier parameter $\mu$ should be larger than zero. $x^{(k)}$ denotes the $k$ th component of the vector $x$. Since the objective function of this barrier problem becomes arbitrarily large as $x^{(k)}$ approaches either of its bounds, a local solution $x^{*}(\mu)$ of this problem lies in the interior of this set. The degree of influence of the barrier is determined by the size of $\mu$, and under mild conditions a local solution $x^{*}(\mu)$ converges to a local solution $x^{*}$ of the original problem as $\mu$ is approaching 0 . Consequently, a strategy for solving the original non-linear problem is to solve a sequence of barrier problems for decreasing barrier parameters $\mu$. More details can be found in [30-33].

## 4. Results and discussion

The scheduling period is 24 h . The sample time $\Delta t$ is 1200 s ( 20 min ). It is important to note that each vehicle is assumed to be plugged in once a day. In this paper, multiple charging scenarios are not taken into account. A large-scale PHEV/PEV charging infrastructure digital testbed, as shown in Fig. 9, was developed in Matlab/Simulink to analyze the system performance. The "Real-world Transportation Scenarios" block simulates the real-world parking deck scenarios and incorporates some uncertainty. The proposed optimization algorithms are embedded in "Optimal Charging Algorithms" subsystem to determine how to dispatch most effectively the available power to a large PHEV/PEV fleet. The accurate battery model is implemented in the block "Charging Station \& Battery Model". The digital testbed allows researchers to evaluate a wide range of charging/discharging scenarios and the corresponding

![img-8.jpeg](img-8.jpeg)

Fig. 9. Large-scale PHEV/PEV charging infrastructure digital testbed (Simulink-based energy management module).
control strategies. Moreover, it offers more flexibility to prepare for the emergence of new technology (e.g., Vehicle-to-Grid, Vehicle-to-Building, and Smart Charging) which will become a reality in the near future.

Fig. 10 shows the process of the proposed energy management program. Depending on the computational capability of the central controller, the proposed computational intelligence-based methods can handle a large optimization problem to a certain level. To significantly reduce the computational cost, an intuitive way is to classify large numbers of vehicles into vehicles/users groups. It opens up the possibility of dividing multiple charging stations into clusters with common objectives/characteristics and assigning the responsibility of optimizing on each cluster to a suboptimization problem thereby translating the problem into the arena of distributed control. In this way, the proposed charging
algorithms can be easily extended to solve an even larger energy management problem with little additional cost.

Figs. 11 and 12 represent the instant SoC and power usage of a specific vehicle during the optimization process. Once the vehicle was plugged-in, the supervisory controller made a decision regarding the optimal power allocation to this specific vehicle battery.

The maximum number of generations is limited to 200; the population size is 200; the initial population is the same; the simulation is repeated 30 times. Population-based optimization method is a stochastic method and the maximum number of internal iterations is limited, thus there existed the chance of generating different solutions at each run. Despite this potential for variation, the standard deviation of the fitness value in both PSO and EDA was found to be less than $1 \%$ of the average, showing the accuracy and consistency of the final solutions.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Flow chart of the proposed energy management for a large number of PHEVs/PEVs.

![img-10.jpeg](img-10.jpeg)

Fig. 11. Plot of State-of-Charge to a specific vehicle.
![img-11.jpeg](img-11.jpeg)

Fig. 12. Plot of power allocation to a specific vehicle.

Because IPM only searches for local minima in the search space, it performs faster than the other algorithms. EDA and PSO are also less time-consuming than GA because they do not perform selection and crossover operations. In general, the optimization performance mainly relies on the parameter settings, which is a big challenge for a researcher who has less experience. EDA and PSO require few parameters to be tuned by users. PSO is also fairly immune to the size and non-linear nature of the problems being considered. Compared with the other techniques, PSO is relatively easier to implement because it relies on simple calculations, constraint handling is more straightforward, and there are fewer parameters to adjust. Additionally, because every particle remembers both its personal and neighborhood best values, PSO has a more effective memory capacity than GA. PSO is also more efficient at maintaining swarm diversity because the individual particles use information related to the most successful particle in order to improve them. In GA, the worst solutions are discarded, causing the population to evolve around a subset of only the best individuals [34]. PSO does achieve the highest quality solution (i.e., fitness value). PSO uses the previously stored system data in order to solve optimization problems. Any change to the system requires saving the new data and re-executing the algorithm.

The authors selected an EDA for solving this problem because it is robust for solving complex, large-scale, non-linear optimization problems (e.g. large-scale PHEV/PEV energy management). Since
an EDA explicitly extract global statistical information from promising solutions, EDA is also fairly immune to the local minima and non-linear nature of the problems being considered in this paper. EDAs extract global statistical information from the promising solutions in order to generate offspring. In terms of the fitness value, EDA is better than PSO and GA. In order to make real-time decisions related to the amount of power allocated to each vehicle, a large amount of raw data needs to be processed in a short amount of time. EDA can reach the near-optimal solution at a reasonable convergence rate (e.g., the execution time does not exponentially growing with respect to the number of variables). Moreover, the algorithm's performance is not largely affected by the computer memory limit, the size of the problem, or the dimension limits. Since the optimization is dealing with a large number of PHEVs (i.e., 3000 or greater) connected to the grid service, EDA is particularly suitable for solving this problem with relatively low computation costs when compared to other approaches. However, the local search ability of EDA still needs to improve. A hybrid EDA method can achieve a higher quality optimal solution.

The full comparison on the proposed computational intelli-gence-based algorithms is summarized in Table 3.

In order to fully compare all the algorithms, Fig. 13 shows the fitness values at time step $k$ achieved by four different methods over 30 trials. In this case, 500 vehicles were plugged-in simultaneously. It is important to mention that the 30 trials were

![img-12.jpeg](img-12.jpeg)

Fig. 13. Comparisons on fitness values over 30 runs.

Table 2
Comparison on EDA and PSO.

performed randomly and subject to a variety of system conditions and energy constraints. As shown in Fig. 13, EDA and IPM can achieve relatively higher fitness values over 30 runs.

A two-sample $t$-test was performed on the simulation results in order to determine which method outperforms others. In statistical significance testing, the $p$-value is the probability of obtaining a test statistic at least as extreme as the one that was actually observed, assuming that the null hypothesis is true. A small $p$-value indicates that the null hypothesis is less likely to be true. Since the performance of EDA and IPM is almost identical, authors will only compare EDA with the other two methods (i.e., PSO, GA) in the following sections.
$J_{\text {EDA }}$ is the fitness value achieved by the EDA, while $J_{E}$ is the fitness value achieved by other methods. First, authors compare the

EDA's performance with the other ones, where $J_{E}$ denotes the fitness value achieved by PSO and GA. Then, the null hypothesis is defined as
$H_{0}: \quad J_{\text {EDA }} \leqslant J_{E}$.
This is tested against the alternative hypothesis
$H_{1}: \quad J_{\text {EDA }}>J_{E}$.
$J_{\text {diff }}=J_{\text {EDA }}-J_{E}$.
The mean of $J_{\text {diff }}$ is $\bar{d}$, and $S_{d}$ is the standard deviation of $J_{\text {diff }}$.
$t=\frac{\bar{d}}{S_{d} / \sqrt{n}}=\frac{2.0211}{0.0924 / \sqrt{30}}=119.8054$.
The $p$-value is the probability of holding the null hypothesis. Corresponding to $t=119.8054$, the significant level $p$-value is much less than 0.0001 . The lower the $p$-value is, the less likely the null hypothesis is true. Thus authors reject the null hypothesis $H_{0}$ and draw the conclusion that there is significant evidence that the EDA can achieve better fitness values than others do (i.e., $J_{E}$. $\mathrm{DA}>J_{E}$ ). By following a similar procedure as described before, authors obtained the $p$-value for the other case (i.e., EDA vs. GA).

Table 3
Comparisons on PSO, EDA, IPM, and GA.

![img-13.jpeg](img-13.jpeg)

Fig. 14. Comparison of departure SoC.

The $p$-value is even smaller. Thus authors reject the null hypotheses and conclude that an EDA is much better than other methods in solving this specific problem.

The system performance is defined as
System.Performance $=\frac{\hat{J}_{\text {EDA }}-\hat{J}_{E}}{\hat{J}_{E}} \%$.
$\hat{J}_{\text {EDA }}$ and $\hat{J}_{E}$ are the fitness values achieved by the EDA and the other algorithms, respectively.

Therefore, based on the statistical information listed in Table 2, authors can further conclude that, in comparisons with PSO, and GA on the average, an EDA/IPM based methods improved the optimization performance by $21.03 \%$, and $23.03 \%$, respectively.

The authors further compared the optimization performance of the proposed SoC maximization method with Equal Priority [35], and Heuristic method [35]. The authors looked into the departure SoC of ten vehicles, as shown in Fig 14. Obviously, SoC maximization method being considered in this paper can provide a uniformly higher SoC for all PHEVs/PEVs at plug-out as compared with the alternative schemes. It also proves that the proposed function aims at ensuring some fairness in the SoC-distribution at each time step. This will help to ensure that a reasonable level of battery power is attained, even in the event of an early departure.

However, as mentioned in Section 2, a number of objective functions can be formulated depending on user preference and interest. The objective function being considered in this paper is the maximization of the average SoC (State-of-Charge) for all vehicles at the next time step. The simulation results show that EDA and IPM methods outperform the others in solving this specific optimization problem. It is not necessary to draw the conclusion that EDA and IPM methods are always the best candidates to achieve the optimal energy management at a large-scale PHEV/ PEV enabled municipal parking deck.

## 5. Conclusion

The emergence of PHEVs/PEVs is reshaping the traditional views of power system. The anticipation of a large penetration of PHEVs/ PEVs into the market brings up many potential technical problems that need to be addressed. The interface between the vehicle and the grid also needs to be better characterized, particularly for com-
munities and facilities where large numbers of PHEVs/PEVs may be concentrated. In this paper, the authors developed a suite of computational intelligence-based algorithms to manage the use of such highly concentrated chargers to minimize the strain on the power grid. The intelligent energy management system considers vehicle energy requirements, time of arrival and departure, power constraints from the utility, battery charging limit, desired departure SoC, energy cost, and other factors to determine how to most effectively dispatch the available power from the utility. The proposed energy management program can handle the energy management at a large-scale PHEV/PEV parking deck. By grouping the vehicle fleet, the proposed energy management program has the potential to be extended to solve a larger energy management problem with little additional cost. The simulation results were given to demonstrate the effectiveness of the proposed computational intelli-gence-based approaches in solving energy management at a municipal PHEV/PEV parking deck. The authors characterized the performance of the proposed methods using a Matlab/Simulink simulation, and compared it with other optimization techniques.

## Acknowledgements

This work was supported by Future Renewable Electric Energy Delivery and Management (FREEDM) Systems Center under grant NSF EEC-0812121 and this work is also an ongoing project in collaboration of Advanced Diagnosis Automation and Control (ADAC) Lab at North Carolina State University with Advanced Transportation Energy Center (ATEC). The authors would like to thank all colleagues at ADAC Lab for helpful discussion.
