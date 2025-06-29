# Performance Evaluation of an EDA-Based Large-Scale Plug-In Hybrid Electric Vehicle Charging Algorithm 

Wencong Su, Student Member, IEEE, and Mo-Yuen Chow, Fellow, IEEE


#### Abstract

The anticipation of a large penetration of plug-in hybrid electric vehicles (PHEVs) into the market brings up many technical problems that need to be addressed. In the near future, a large number of PHEVs in our society will add a large-scale energy load to our power grids, as well as add substantial energy resources that can be utilized. An emerging issue is that a large number of PHEVs simultaneously connected to the grid may pose a huge threat to the overall power system quality and stability. In this paper, the authors propose an algorithm for optimally managing a large number of PHEVs (e.g., 3000) charging at a municipal parking station. The authors used the estimation of distribution algorithm (EDA) to intelligently allocate electrical energy to the PHEVs connected to the grid. A mathematical framework for the objective function (i.e., maximizing the average state-ofcharge at the next time step) is also given. The authors considered real-world constraints such as energy price, remaining battery capacity, and remaining charging time. The authors also simulated the real-world parking deck scenarios according to the statistical analysis based on the transportation data. The authors characterized the performance of EDA using a Matlab simulation, and compared it with other optimization techniques.


Index Terms-Estimation of distribution algorithm (EDA), intelligent energy management, performance evaluation, plug-in hybrid electric vehicle (PHEV), smart grid.

## I. INTRODUCTION

ECONOMIC AND environmental incentives, as well as advances in technology, are reshaping the traditional view of power systems. Plug-in hybrid electric vehicles (PHEVs) have received increasing attention because of their low pollution emissions and high fuel economy. Ultimately, PHEVs will shift energy demands from crude oil to electricity for the personal transportation sector [1]. By drawing on and supplying power to the power grid, electric vehicles could displace the use of petroleum. This would reduce pollution and alleviate

[^0]security issues related to oil extraction, importation, and combustion. Along with the utilization of grid power, PHEVs also have the potential to transfer power to the grid to alleviate peak power demand and provide ancillary services to the grid [2].

The U.S. Department of Energy projects that approximately 1 million PHEVs will be on the road by 2015 and 425000 PHEVs will be sold in 2015 alone. At this penetration rate, PHEVs would account for $2.5 \%$ of all new vehicle sales in 2015 [3]. The Electric Power Research Institute (EPRI) projects that $62 \%$ of the entire U.S. vehicle fleet will consist of PHEVs by 2050 using a moderate penetration scenario [4]. Accordingly, there is a growing need to address the implications of this technology on the power grid. Large numbers of PHEVs have the potential to threaten the stability of the power system. For example, the aggregated load in a municipal parking deck needs to be managed very carefully in order to avoid interruption when several thousand PHEVs are introduced into the system over a short period of time (e.g., during the early morning hours when people arrive at work). Moreover, due to variations in the needs of the PHEVs parked in the deck at any given time, the demand pattern will also have a significant impact on the electricity market.

In order to maximize customer satisfaction and minimize disturbances to the grid, a sophisticated controller will need to be designed in order to regulate multiple loads from a cluster of PHEVs appropriately. This controller must take into consideration real-world constraints (i.e., communication and infrastructure variations among individual vehicles). The controller must also accommodate for differences in arrival and departure times, as well as the number of PHEVs in the parking deck. The algorithm should also be robust to uncertainty, be capable of making decisions in real-time with limited communication bandwidth, and work seamlessly with existing utilities.

A theoretical system of a PHEV municipal parking deck has been studied in [5]-[7]. The initial algorithms have been implemented in Matlab/Simulink and Labview. In [8], the authors analyzed the optimal performance of the proposed charging algorithms under certain operating conditions and various types of battery models. A particle swarm optimization (PSO) based control algorithm was put forward in [9] to optimally allocate power to PHEVs at a municipal parking deck. In [10], the authors evaluated the impact of the large penetration of PHEVs under various charging scenarios.

This paper addresses the performance evaluation of different control strategies in real-world PHEV parking deck operating conditions under various energy constraints. This paper first simulates the parking deck scenarios (e.g., plug-in time, initial


[^0]:    Manuscript received January 18, 2011; revised March 21, 2011; accepted April 28, 2011. Date of publication June 13, 2011; date of current version February 23, 2012. This work was supported by THE Future Renewable Electric Energy Delivery and Management (FREEDM) Systems Center under Grant NSF EEC-0812121; this work is also an ongoing project in collaboration with the Advanced Diagnosis Automation and Control Lab at North Carolina State University with the Advanced Transportation Energy Center (ATEC). Paper no. TSG-00007-2011.

    The authors are with the Department of Electrical and Computer Engineering, North Carolina State University, Raleigh, NC 27606 USA (e-mail: wsu2@ncsu. edu; chow@ncsu.edu).

    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

    Digital Object Identifier 10.1109/TSG.2011.2151888

![img-0.jpeg](img-0.jpeg)

Fig. 1. Proposed structure of large-scale PHEV/PEV charging/V2G infrastructure in smart grid environment.

SOC, expected charging time, user preference, etc.) according to the statistical analysis based on transportation data. Specifically, the authors are investigating the use of the EDA for developing real-time, large-scale optimizations for allocating power to PHEVs at a municipal parking deck. EDAs, sometimes called probabilistic model-building genetic algorithms (PMBGAs), have recently been used to solve a variety of problems in different application areas. In EDAs, a probability distribution is extracted from a population and new candidate solutions can be obtained by sampling this distribution.

The remainder of this paper is organized as follows. Section II will describe the specific problem solved in mathematical term. The authors will provide the optimization objective and certain system constraints, as well as the simulated parking deck scenarios. Section III will review the EDA-based method, as well as describe how the algorithm works for the proposed optimization problems. The results of the simulation, as well as further analysis of the parking deck scenarios, are presented in Section IV. Finally, the authors will summarize this paper in Section V.

## II. Problem Formulation

As shown in Fig. 1, the proposed model of a PHEV/PEV municipal parking deck consists of three major subsystems: 1) the traditional power utility and local-scale renewable energy resource; 2) an intelligent parking deck controller; 3) PHEV/PEV battery chargers and customers. The following sections will highlight the modeling of the second subsystem, which is embedded in the solid red block as shown in Fig. 1.

## A. Objective Function

A number of objective functions can be formulated depending on the user's preference and interest. For example, the objective could be to maximize the customer benefits by following demand side management [6]. If we consider the aggregated PHEV/PEV batteries as potential energy storage, another objective could be to maximize the capability of this aggregated battery to mitigate the unpredictable fluctuation of renewable energy [11].

The objective function being considered in this paper is the maximization of the average state-of-charge (SOC) for all vehicles at the next time step. The authors will consider the energy price, charging time, and current SOC in this model. In
order to make the system more robust, the authors will also allow vehicles to leave prior to their expected departure time (i.e., the PHEV is unplugged abruptly). This would result in a serious failure in terms of optimal power allocation, and the PHEV battery may not be adequately charged (even if it has been plugged-in for a long time) [12]. Therefore, the proposed function aims at ensuring some fairness in the SOC distribution at each time step. This will help to ensure that a reasonable level of battery power is attained, even in the event of an early departure.

Maximize the objective function $J$ at any given time $k$

$$
\begin{aligned}
J(k) & =\sum_{i} w_{i}(k) \cdot \operatorname{SoC}_{i}(k+1) \\
w_{i}(k) & =f\left(\operatorname{Cap}_{r, i}(k), T_{r, i}(k), D_{i}(k)\right) \\
\operatorname{Cap}_{r, i}(k) & =\left(1-\operatorname{SoC}_{i}(k)\right) * \operatorname{Cap}_{i}
\end{aligned}
$$

where $\operatorname{Cap}_{r, i}(k)$ is the remaining battery capacity required to be filled for the $i$ th PHEV at time step $k ; \operatorname{Cap}_{i}$ is the rated battery capacity (Ah) of the $i$ th PHEV; $T_{r, i}(k)$ is the remaining time for charging the $i$ th PHEV at time step $k ; D_{i}(k)$ is the price difference between the real-time energy price and the price that a specific customer at the $i$ th PHEV charger is willing to pay at time step $k ; w_{i}(k)$ is the charge weighting term of the $i$ th PHEV at time step $k$ (this is a function of the energy price, the remaining charging time, and the current SOC); $\operatorname{SoC}_{i}(k+1)$ is the state of charge of the $i$ th PHEV at time step $k+1$.

The weighting term gives a reward proportional to the attributes of a specific PHEV. For example, if a vehicle has a lower initial SOC and less remaining charging time, but the driver is willing to pay a higher price, the controller allocates more power to this PHEV charger

$$
w_{i}(k) \propto\left[\operatorname{Cap}_{r, i}(k)+D_{i}(k)+1 / T_{r, i}(k)\right]
$$

Since the three terms $\operatorname{Cap}_{r, i}(k), D_{i}(k), 1 / T_{r, i}(k)$ are not on the same scale, all terms need to be normalized in order to assign similar importance to each

$$
\begin{aligned}
c_{r, i}(k) & =\frac{\operatorname{Cap}_{r, i}(k)-\operatorname{Min}\left[\operatorname{Cap}_{r,:}(k)\right]}{\operatorname{Max}\left[\operatorname{Cap}_{r,:}(k)\right]-\operatorname{Min}\left[\operatorname{Cap}_{r,:}(k)\right]} \\
d_{r, i}(k) & =\frac{D_{r, i}(k)-\operatorname{Min}\left[D_{r,:}(k)\right]}{\operatorname{Max}\left[D_{r,:}(k)\right]-\operatorname{Min}\left[D_{r,:}(k)\right]} \\
t_{r, i}(k) & =\frac{1 / T_{r, i}(k)-\operatorname{Min}\left[1 / T_{r,:}(k)\right]}{\operatorname{Max}\left[1 / T_{r,:}(k)\right]-\operatorname{Min}\left[1 / T_{r,:}(k)\right]}
\end{aligned}
$$

The parking deck operators may also have different interests and assign different importance factors to $c_{r, i}(k), t_{i}(k)$, and $d_{i}(k)$ depending on their own preferences. Thus

$$
w_{i}(k)=\alpha_{1} c_{r, i}(k)+\alpha_{2} t_{i}(k)+\alpha_{3} d_{i}(k)
$$

The charging current is also assumed to be constant over $\Delta t$

$$
\begin{aligned}
& {\left[\operatorname{SoC}_{i}(k+1)-\operatorname{SoC}_{i}(k)\right] \cdot \operatorname{Cap}_{i}=Q_{i}=I_{i}(k) \Delta t} \\
& \operatorname{SoC}_{i}(k+1)=\operatorname{SoC}_{i}(k)+I_{i}(k) \Delta t / \operatorname{Cap}_{i}
\end{aligned}
$$

where $\Delta t$ is the sample time defined by the parking deck operators; $I_{i}(k)$ is the charging current over $\Delta t$.

The battery model is considered to be a capacitor circuit. $C_{i}$ is the battery capacitance (Farad)

$$
C_{i} \cdot d V_{i} / d t=I_{i}
$$

Therefore, over a short period of time, one can approximate the voltage change to be linear

$$
\begin{aligned}
& C_{i} \cdot\left[V_{i}(k+1)-V_{i}(k)\right] / \Delta t=I_{i} \\
& V_{i}(k+1)-V_{i}(k)=I_{i} \Delta t / C_{i}
\end{aligned}
$$

Since the decision variable is the power allocated to the PHEVs, replace $I_{i}(k)$ with $P_{i}(k)$

$$
I_{i}(k)=\frac{P_{i}(k)}{0.5 \times\left[V_{i}(k+1)+V_{i}(k)\right]}
$$

Substituting $I_{i}(k)$ into (12) yields

$$
V_{i}(k+1)=\sqrt{2 P_{i}(k) \Delta t / C_{i}+V_{i}^{2}(k)}
$$

Substituting (14) and (15) into (10) yields

$$
\mathrm{SoC}_{i}(k+1)=\mathrm{SoC}_{i}(k)+\frac{2 P_{i}(k) \Delta t}{\operatorname{Cap}_{i} \cdot\left[V_{i}(k+1)+V_{i}(k)\right]}
$$

Finally, the objective function becomes (17) at the bottom of the page.

## B. System Constraints

Possible real-world constraints could include the charging rate (i.e., slow, medium, and fast), the time that the PHEV is connected to the grid, the desired departure SOC, the maximum electricity price that a user is willing to pay, certain battery requirements, etc. Furthermore, the available communication bandwidth could limit sampling time, which would have effects on the processing ability of the vehicle.

The primary energy constraints being considered in this paper include the power available from the utility ( $P_{\text {utility }}$ ) and the maximum power ( $P_{i, \text { max }}$ ) that can be absorbed by a specific vehicle. The overall charging efficiency of the parking deck is described by $\eta$. From the system point of view, $\eta$ is assumed to be constant at any time step. $\mathrm{SoC}_{i, \text { max }}$ is the user-defined maximum battery SOC limit for the $i$ th PHEV/PEV. Once $\mathrm{SoC}_{i}$ reaches $\mathrm{SoC}_{i, \text { max }}$, the $i$ th battery charger switches to a standby mode. The SOC ramp rate is limited by the constraint $\Delta \mathrm{SoC}_{\text {max }}$. The intelligent control process is updated when 1) utility information updates; 2) a new vehicle is plugged-in; 3)
sample time $\Delta t$ has passed periodically. The system constraints are defined as

$$
\begin{aligned}
& \sum_{i} P_{i}(k) \leq P_{\text {utility }}(k) \times \eta \\
& 0 \leq P_{i}(k) \leq P_{i, \max }(k) \\
& 0 \leq \mathrm{SoC}_{i}(k) \leq \mathrm{SoC}_{i, \max } \\
& 0 \leq \mathrm{SoC}_{i}(k+1)-\mathrm{SoC}_{i}(k) \leq \Delta \mathrm{SoC}_{\max }
\end{aligned}
$$

## C. Simulated Input Data

To simulate the real-world parking deck scenarios incorporating some uncertainty, researchers need to come up with a series of decent probabilistic models, namely, plug-in time, expected plug-out time, initial SOC, and battery capacity.

The battery capacity of each vehicle is defined as a continuous uniform random number between 6.5 and 25 .

To take into account the uncertainty and the limits on the random variables, a truncated normal distribution was suggested in [13] to represent the parking time and the time at which vehicles complete the morning commute. Let $X \sim N\left(\mu, \sigma^{2}\right)$ be a normal distribution $\Phi$ with the mean $\mu$ and the variance $\sigma^{2}$. The parking time and the expected arrival time lie within the corresponding interval $(a, b)$. The probability density distribution is given by

$$
f(x ; \mu, \sigma, a, b)=\frac{\frac{1}{\sigma} \Phi\left(\frac{x-\mu}{\sigma}\right)}{\Phi\left(\frac{b-\mu}{\sigma}\right)-\Phi\left(\frac{a-\mu}{\sigma}\right)}
$$

To validate the probabilistic modeling, the authors generate the random input under a truncated normal distribution and then compare the simulation result with the historical data of an office parking deck in the city of Livermore, CA, during weekdays [14]. Table I summarizes the parking utilization over a period of 24 h . For the most part, the simulated number of $\mathrm{PHEVs} / \mathrm{PEVs}$ connected to the grid at any given time matches the actual data quite well, as shown in Fig. 2.

The initial SOC can be modeled as a random variable under log-normal distribution as found by [15] and [16]. The average mileage per day per vehicle is assumed to be 32 miles. Accordingly, the daily distance is log-normally distributed with a mean of 32 miles and a standard deviation of 24 miles. EV battery range spans from 20 miles to 300 miles depending on the number and type of battery, weather, driving behavior, and terrain, which is out of scope in this paper. Thus, in the following simulation, the average battery range is simply assumed to be 100 miles. The relationship between initial SOC and typical daily travel distance was proposed in [17]. $X$ is the initial SOC

$$
J(k)=\sum_{i} w_{i} \cdot\left[\operatorname{SoC}_{i}(k)+\frac{2 P_{i}(k) \Delta t}{\operatorname{Cap}_{i} \cdot\left[\sqrt{\frac{2 P_{i}(k) \Delta t}{C_{i}}+V_{i}^{2}(k)+V_{i}(k)\right]}\right]
$$

![img-2.jpeg](img-2.jpeg)

Fig. 2. Typical parking utilization over a period of 24 h .

TABLE I
Typical Hourly Parking Utilization During Weekdays

![img-2.jpeg](img-2.jpeg)

Fig. 3. Probability density function of a typical initial SOC.
expressed in percent. $R$ is the average battery range in miles. $D$ is the probability density function of the daily mileage

$$
f(X)=R^{2} / 100 \cdot D \cdot(1-X / 100)
$$

Fig. 3 shows the corresponding probability density function obtained by applying statistical analysis on the typical driving pattern as well as the average PHEV/PEV travel range.

## III. Estimation of Distribution Algorithm

EDAs are evolutionary algorithms based on global statistical information extracted from promising solutions [18], [19]. For most real-world problems, there is a reasonable assumption that good solutions have a similar structure in some sense. In brief, an EDA estimates the probability distribution of the most successful solutions and generates offspring by sampling the statistical model. An EDA does not use mutation and crossover. There are few parameters to adjust in EDA.

Generally speaking, the principal steps of an EDA in solving this problem can be summarized as follows.

1) Generate a group of random solutions $P=\left[p_{1}, p_{2}, p_{3}, \ldots, p_{n}\right]$ ( $n$ is the number of vehicles connected to grids at this time step; $p_{j}$ is the possible power allocation to the $j$ th PHEV/PEV battery) in the feasible region. Since normally there is very little information about the global optima, these solutions are scattered over the search space as uniformly as possible.
2) Convert the constrained optimization problem into a simple unconstrained one by assigning a penalty to the constraint violation [19], [20]. Such a way can easily handle the constraints, eliminating the need for additional computation costs. Also, there is no limit to the number or format of the constraints. $\gamma$ is a large positive penalty value. Then evaluate the fitness function according to (24) and select the best $n_{s}\left(n_{s}<n\right)$ candidates using a truncation selection, subject to (19)-(21)

$$
\begin{aligned}
J_{\text {new }}(k)= & J(k) \\
& +\gamma \cdot \operatorname{Min}\left\{0, \eta \cdot P_{\text {utility }}(k)-\sum_{i} P_{i}(k)\right\}
\end{aligned}
$$

3) Update the probability distribution model using the selected $n_{s}$ solutions. Implement a continuous Gaussian univariate marginal distribution algorithm (UMDA) [22]-[25] in Matlab to solve this optimization problem.

$$
p_{l}\left(x_{i}\right)=\frac{\sum_{j=1}^{N} \delta_{j}\left(X_{i}=x_{i} \mid D_{l-1}^{\text {Selected }}\right)}{N}
$$

$\delta_{j}\left(X_{i}=x_{i} \mid D_{l-1}^{\text {Selected }}\right)=1$, if the $j$ th selected individual's $i$ th gene is $x_{i}$; otherwise it is 0 .
4) Generate new solutions which have gene values $x_{i}$ with the probability $p_{l}\left(x_{i}\right)$ from step 3. Energy scheduling at a PHEV/PEV parking deck is also subject to different constraints that limit the search space to a certain feasible region. Reset the individual value (i.e., the amount of power allocated to a specific vehicle) to the boundary if the constraints do not hold true.
5) Replace some members from the current population with offspring generated in step 3.
6) Repeat steps 2-5 until the maximum number of iterations or the minimum error criteria is met. Save the near-optimal solution (i.e., the amount of power allocated to each PEHVs/PEVs under a set of system constraints).
The authors selected an EDA for solving this problem because it is robust for solving complex, large-scale, nonlinear optimization problems (e.g., large-scale PHEV/PEV energy management). EDA is fairly immune to the local minima and nonlinear nature of the problems being considered in (17). In order to make real-time decisions related to the amount of power allocated to each vehicle, a large amount of raw data needs to be processed in a short amount of time. EDA can reach the near-optimal solution at a reasonable convergence rate. Moreover, the algorithm's performance is not largely affected by the computer memory limit, the size of the problem, or the dimension limits. Since the authors are dealing with a large number of PHEVs (i.e., 3000 or greater) connected to the grid service, EDA is particularly suitable for solving this

![img-3.jpeg](img-3.jpeg)

Fig. 4. The flowchart of EDA implementation.
problem with low computation costs when compared to other approaches (e.g., Genetic Algorithms).

## IV. SIMULATION RESULTS AND ANALYSIS

All simulations were run on an Intel(R) Core i5 CPU M450@2.40 GHz, 6.00 GB, Windows 7, and Matlab 2009b. In this paper, the authors used a PC to perform the calculations for algorithm testing. In actual commercial deployment, the proposed algorithm can be easily implemented in a special-purpose device (e.g., microcontroller, DSP, FPGA). The low-cost hardware implementation can facilitate the commercial deployment of the proposed PHEV charging algorithm. Maximum charger limit $P_{i, \max }(k)$ is 10 KW ; the system efficiency is $90 \%$ all the time; $n(k)$ is the number of $\mathrm{PHEVs} / \mathrm{PEVs}$ connected at any given sample time $k ; P_{\text {stility }}(k)=90 \% \times n(k) \times P_{i, \max }(k)$; the scheduling period is 24 hours. In EDA, the maximum number of generations is limited to 200; the population size is 800. The sample time $\Delta t$ is 1200 seconds. Level 2 charging (i.e., 240 VAC, 32 Amps, and 7.7 KVA single phase outlet) is typically described as the "primary" and "preferred" method for an electric vehicle charger in both private and public facilities. In the following simulations, the parking deck electrification infrastructure is based on Level 2 charging. It is important to note that each vehicle is assumed to be plugged-in once a day. Multiple charging scenarios are not taken into account.

The typical evolution process of the EDA in solving this problem at time step $k$ is described in Fig. 5.

The red line represents the best fitness value while the blue dots represent the mean value. Gradually, the entire population reached the near-optima region, but the diversity of the population was still maintained. Eventually, they converged on the global near-optima. Fig. 5 shows the worst case, in which 300 vehicles were charged simultaneously. An optimal fitness value of 6.328 was achieved at the 200th generation.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Convergence tendency of the proposed EDA method.

TABLE II
AVERAGE CPU Time Over 30 Runs Using EDA

TABLE III
COMPARISON ON EDA AND GA WITH 50 VEHICLES


![img-5.jpeg](img-5.jpeg)

Fig. 6. Box-and-whisker diagram over 30 runs.

However, because the EDA is a stochastic method and the maximum number of internal iterations was limited, there existed the chance of generating different solutions at each run. Despite this potential for variation, the standard deviation was found to be less than $0.0079 \%$ of the average, showing the accuracy and consistency of the final solutions. Furthermore, the simulation results show that the proposed method is capable of obtaining high quality solutions with stable convergence characteristics.

Initially, the authors simulated the algorithm with 30 PHEVs. Then, the authors increased the number of PHEVs to 300 and 3000. Compared with the sampling time $\Delta t, 5 \mathrm{~s}$ is a reasonable decision making time on 3000 vehicles. As seen in Table II, the execution time does not exponentially grow with respect to the number of $\mathrm{PHEVs} / \mathrm{PEVs}$, demonstrating that the EDA-

![img-6.jpeg](img-6.jpeg)

Fig. 7. Comparisons on fitness values over 30 runs.

TABLE IV
Optimal Solutions With 300 PHEVs/PEVs


based method is suitable for energy management at a large-scale municipal parking deck.

The computational speed of EDA and GA is compared in Table III. EDA is less time-consuming than GA because it does not perform selection and crossover operations. GA requires several parameters to be tuned by users. Accordingly, the optimization performance mainly relies on the parameter settings, which is a big challenge for a researcher who has less experience. Instead, EDAs extract global statistical information from the promising solutions in order to generate offspring. In terms of the fitness value shown in Table III, EDA is also better than GA.

The authors then compare the optimization performance of the EDA algorithm with the equal priority algorithm [26], the genetic algorithm (GA) method, and the heuristic algorithm [26]. The optimal solutions achieved by all the methods are compared in Table IV. Fig. 7 shows the fitness values at time step $k$ achieved by different methods over 30 trials. In this case, 300 vehicles were plugged in simultaneously. The corresponding box-and-whisker plot is shown in Fig. 6. It is important to mention that the 30 trials were performed randomly and subject to a variety of system conditions and energy constraints.

A two-sample $t$-test was performed on the simulation results in order to determine whether an EDA-based method outperforms others. In statistical significance testing, the $p$-value is the probability of obtaining a test statistic at least as extreme as the one that was actually observed, assuming that the null hypothesis is true. A small $p$-value indicates that the null hypothesis is less likely to be held.
$J_{\text {EDA }}$ is the fitness value achieved by the EDA, while $J_{E}$ is the fitness value achieved by other methods. First, the authors compare the EDA's performance with the second best one,
where $J_{E}$ denotes the fitness value achieved by the equal priority method. Then, the null hypothesis is defined as

$$
H_{0}: J_{\mathrm{EDA}} \leq J_{E}
$$

This is tested against the alternative hypothesis

$$
\begin{aligned}
& H_{1}: J_{\mathrm{EDA}}>J_{E} \\
& J_{\text {diff }}=J_{\mathrm{EDA}}-J_{E}
\end{aligned}
$$

The mean of $J_{\text {diff }}$ is $\bar{d}$, and $S_{d}$ is the standard deviation of $J_{\text {diff }}$

$$
t=\frac{\bar{d}}{S_{d} / \sqrt{n}}=\frac{0.5056}{0.0186 / \sqrt{30}}=148.9
$$

The $p$-value is the probability of holding the null hypothesis. Corresponding to $t=148.9$, the significant level $p$-value is $1.162 \mathrm{e}^{-12}<0.0001$. The lower the $p$-value is, the less likely the null hypothesis is true. Thus the authors reject the null hypothesis $H_{0}$ and draw the conclusion that there is significant evidence that the EDA can achieve better fitness values than others do (i.e., $J_{\mathrm{EDA}}>J_{E}$ ). By following a similar procedure as described before, the authors obtained the $p$-value for the other two cases (i.e., EDA versus GA, and EDA versus heuristic method). Both $p$-values are even smaller. Thus the authors reject the null hypotheses and conclude that an EDA is much better than other methods in solving this specific problem.

The system performance is defined as

$$
\text { System_Performance }=\frac{\bar{J}_{\mathrm{EDA}}-\bar{J}_{E}}{\bar{J}_{E}} \%
$$

$\bar{J}_{\text {EDA }}$ and $\bar{J}_{E}$ are the fitness values achieved by the EDA and the other algorithms, respectively.

Therefore, based on the statistical information listed in Table II, the authors can further conclude that, in comparisons with the equal priority method, GA, and the heuristic method on the average, an EDA-based method improved the optimization performance by $8.75 \%, 29.83 \%$, and $22.63 \%$, respectively.

To further analyze the simulation results from EDA, equal priority, and GA, the authors looked into the departure SOC of ten vehicles, as shown in Fig. 8. Obviously, the authors found

![img-7.jpeg](img-7.jpeg)

Fig. 8. Comparison of departure SOC.
that EDA can provide a uniformly higher SOC for all PHEVs/ PEVs at plug-out as compared with the alternative schemes.

## V. CONCLUSION

In this paper, the authors described the performance evaluation of an EDA-based large-scale PHEV/PEV charging algorithm from a mathematical and statistical perspective. In this model, the authors considered the constraints imposed by the battery charging limit, the utility limit, the time that a PHEV/PEV is connected to the grid, the desired departure SOC, certain battery requirements to satisfy both customer interests and the needs of the power grid. In order to manage the energy allocated to the PHEVs/PEVs in real time and enable the smooth integration of PHEVs/PEVs into the power grid, the authors have applied an EDA-based approach. It can handle the energy management at a large-scale (e.g., 3000 vehicles) PHEV/PEV parking deck. The simulation results were given to demonstrate the effectiveness of the proposed EDA-based approach in solving energy management at a municipal PHEV/PEV parking deck. Since an EDA explicitly extract global statistical information from promising solutions, it is immune to the potential local minimum and the nonlinear nature of the problem. The simulation results also demonstrated that the algorithm converged to a better solution than some of the more traditional methods.

## ACKNOWLEDGMENT

The authors would like to thank all colleagues at ADAC Lab for helpful discussion.
