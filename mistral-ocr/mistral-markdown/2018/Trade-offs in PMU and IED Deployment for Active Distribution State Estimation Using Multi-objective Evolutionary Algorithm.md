# Trade-offs in PMU and IED Deployment for Active Distribution State Estimation Using Multi-objective Evolutionary Algorithm 

Sachidananda Prasad ${ }^{\circledR}$ and D. M. Vinod Kumar


#### Abstract

This paper proposes a new multi-objective optimization problem to find trade-offs in deployment of phasor measurement units (PMUs) and intelligent electronic devices (IEDs) for state estimation in active distribution networks. A new hybrid estimation of distribution algorithm (EDA) has been used to find the optimal number and location of measurement devices, such as PMU and IED, for accurate state estimation. The objective functions to be minimized in this optimization problem are the total cost of PMUs and IEDs, and the root mean square value of state estimation error. As the objectives are conflicting in nature, a multi-objective Pareto-based nondominated sorting (NDS) EDA algorithm is proposed. Moreover, to improve the local searching capability of the traditional EDA algorithm, the interior point method (IPM) is hybridized with EDA to get a near-global optimal solution. The hybridization of EDA with IPM brings a higher degree of balance between the exploration and exploitation capability of the traditional EDA during the search process. Furthermore, the random variation in loads and generations is also considered to check the reliability of the proposed meter placement technique. The viability of the proposed algorithm has been tested on the IEEE 69-bus system and Indian 85-bus system to validate the results. The obtained results have been compared with those of the conventional EDA algorithm, NDS genetic algorithm, and hybrid EDA-simulated annealing algorithm existing in the literature.


Index Terms-Distribution system state estimation (DSSE), estimation of distribution algorithm (EDA), interior point method (IPM), multi-objective optimization (MOO), nondominated sorting (NDS) approach.

## I. InTRODUCTION

$\mathrm{E}^{\mathrm{E}}$ECENTLY, the power distribution networks are becoming more and more dynamic and complex structures than before, because of the huge integration of renewable sources, distributed energy storage, intelligent electronic devices (IEDs), and smart meters (SMs) [1], [2]. Furthermore, distribution network configuration is changing dynamically to maintain minimum power loss and voltage deviations. Currently, due to the lack of metering infrastructure in distribution networks, the real-time reliable monitoring of distribution network becomes more challenging for the power engineers. Therefore, the currently existing metering infrastructure of the distribution network has to be modeled for reliable and secure operation of the power distribution networks.

[^0]This complex and dynamic structure of distribution network needs advance monitoring and metering infrastructure, control, and secure operation of the distribution networks. In this context, it may not be possible with a full deployment of the measuring devices at each place of the distribution network for monitoring purpose, because it is economically not feasible. Therefore, distribution system state estimation (DSSE) plays a vital role in achieving reliable and accurate situational awareness of the networks [3]-[7]. However, in distribution networks, there are insufficient numbers of real-time measurements. As a consequence, accurate estimation of system states is more challenging for the state estimator. Therefore, pseudomeasurements are being utilized highly to make the system observable. But, the accuracy of the pseudo-measurements is very low, as these are derived from the customers load profile data. As a result, the required accuracy level may not be achieved in state estimation. Thus, some additional real meters need to be located at suitable position to get better state estimation performance.

In distribution grids, due to the presence of different kinds of actors such as distributed generation (DG) and energy storage devices, system becomes more complex, dynamics, and uncertain in nature. Because of this changing behavior of actors, real-time monitoring and control becomes more challenging task for the power system engineers. Thus, phasor measurement units (PMUs) are of great interest because it provides synchronized measurements of voltage and current phasors. The application of PMU for state estimation in transmission system has been widely used to improve the performance of the state estimator. Therefore, it would be more advantageous to use PMUs in DSSE. In transmission systems, PMUs have been used widely to improve the state estimator performance using different approaches. Therefore, utilization of the phasor measurements in distribution network for state estimation is of great interest. The PMU provides synchronized measurements, e.g., voltage, current phasors, and frequency along with some indirect measurements. The measurements obtained from the PMUs are synchronized with the coordinated universal time. In transmission systems, the synchronized measurements obtained from PMUs along with the nonsynchronized measurements from supervisory control and data acquisition system have been used by many researchers for improving the performance of state estimator [9]-[11].

However, due to lack of sufficient direct measurements in distribution networks, locating PMUs is economically unreasonable. Therefore, the techniques used for locating PMUs


[^0]:    Manuscript received September 5, 2017; revised November 25, 2017; accepted December 6, 2017. The Associate Editor coordinating the review process was Dr. Carlo Muscas. (Corresponding author: Sachidananda Prasad.) The authors are with the Department of Electrical Engineering, NIT Warangal, Warangal 506004 India (e-mail: atulprasad.g@gmail.com). Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
    Digital Object Identifier 10.1109/TIM.2018.2792890

in transmission grids cannot be directly transformed at the distribution level. In order to compensate this, a large number of pseudo-measurements derived from historical customer load data are being used for the state estimation in distribution systems. But, as a result, it deteriorates the accuracy of state estimation to a very large extent. Many researchers have proposed different techniques to deploy PMUs in distribution grids [12]-[16].
In recent times, many alternative techniques have been developed for the enhancement of state estimation performance in distribution networks using meter placement techniques. In [17], meters need to be placed at the main switches, fuse locations, feeder sections, and on normally open tie switches used for network reconfiguration. This method of meter placement gives a good compromise solution between accuracy and computational cost, but it may not provide a global optimal solution. Muscas et al. [18], a meter placement method that is based on heuristic technique has been proposed. A nonlinear combinatorial constraint optimization problem has been designed to minimize the mean square error of the estimated quantities. The optimal number of meters and their position has been obtained using the dynamic programming method.
Liu et al. [19] proposed an optimal metering infrastructure technique for distribution network using genetic algorithm (GA). The objective of the optimization problem is to minimize the total cost combined with the specified accuracy index of the state estimation. In this optimization problem, relative voltage magnitude error and absolute phase angle deviations have been used as performance index. Moreover, an optimal trade-off solution is established between PMUs and SMs for better state estimation performance. Moreover, the optimization process is carried out, considering fixed number of PMU and SM. In [20], the optimal location of the measuring devices is obtained using the DP method. In state estimation, to check the robustness of the algorithm, the authors have considered both network parameter uncertainties as well as the metrological characteristic of the measuring instrument. Sing et al. [21] addressed meter placement scheme based on the ordinal optimization algorithm (OOA) in distribution network. During the optimization process, the meters are placed progressively until the errors come down to prespecified thresholds in $95 \%$ of the cases. However, the obtained solution using OOA may not be a global optimal solution, because authors have considered approximate value of the objective function. In [22], meter placement problem has been formulated as a multi-objective optimization problem (MOOP) to find optimal number and location of power flow meters. A trade-off solution is established among total configuration cost, voltage magnitude, and phase angle errors. Only power flow meters have been considered to find the best optimal solution. Whereas in this paper, both synchronized as well as nonsynchronized measurements are considered for state estimation study. The measurements considered are heterogeneous in nature. Furthermore, a trade-off solution is also established between the deployment of PMU and IED with respect to the total state estimation error. In this paper, further research is extended to find a trade-off solution between the number
of PMUs and IEDs, needed to estimate the state variable in a distribution network more accurately within the specified accuracy limits of the state variables in a multi-objective framework, which has not been addressed before.
In this paper, the metering problem is designed as an MOOP for active distribution state estimation. In this optimization problem, the objective is to find the trade-off between the number and location of PMUs and IEDs required to produce accurate state estimation results within the predefined threshold limits. Indirectly, a trade-off solution is obtained between synchronized and nonsynchronized measurements available at the distribution control center.
The optimal number and location of meters is determined using new hybrid EDA-interior point method (IPM) algorithm. The EDA is hybridized with IPM to improve the balance between exploration and exploitation capability of the traditional EDA algorithm which has poor exploitation capability to achieve global optimal solutions. The key contributions of this paper are presented in the following.

1) A new hybrid EDA-IPM algorithm is used to find the optimal number and location of measurement devices in distribution grids.
2) A trade-off solution between the number of PMUs and IEDs is established with respect to accuracy of the state estimator in a multi-objective framework.
The organization of this paper is as follows. Following the introduction, the DSSE in the presence of PMUs and IEDs is presented in Section II. Then, the meter placement problem is designed as an MOOP and discussed in Section III. The proposed multi-objective hybrid EDA-IPM algorithm has been discussed in Section IV. Section V describes the test and simulation conditions, and the results are presented in Section VI. Finally, Section VII concludes this paper.

## II. DISTRIBUTION SYSTEM StATE ESTIMATION IN THE PRESENCE OF PMUS AND IEDS

The state estimation is a mathematical relation between the system state variables and the available measurements that can estimate the system states accurately from the noisy measurement data. In this paper, the well-established weighted least square (WLS) algorithm has been employed to minimize the following objective function:

$$
\begin{gathered}
J=[z-h(x)]^{T} W^{-1}[z-h(x)] \\
\text { s.t.: } z=h(x)+r
\end{gathered}
$$

where $z$ is the measurement vector, $x$ is the system state vector, consisting of magnitude and phase angle of all branch current, $h(x)$ is a nonlinear measurement function of system state variables, $r$ represents a small noise following the Gaussian distribution, and $W$ is the covariance matrix of the measurement errors.

To improve the state estimation accuracy, PMUs have been employed along with the existing IEDs, for online monitoring of the distribution networks [24]-[26]. Therefore, in this paper, a mixed approach has been considered which includes measurements from PMUs and traditional measurements from IEDs to estimate the states of an active distribution network.

A mathematical model for state estimation based on PMU and IED data is described below.

There are different types of measurement such as substation measurement, pseudo-measurement, virtual measurement, SM measurement, and phasor measurement obtained from PMU have been utilized for state estimation in distribution network. Additionally, it is assumed that PMU installed at a particular bus provides voltage phasor measurements of that bus.

In this paper, for state estimation, the BCDSSE algorithm has been used where branch current magnitude and their phase angle are considered as state of the distribution system [26] and [27]. The initial values for the state variables are assumed as discussed in [27], and the WLS-based iterative process has been conducted to estimate the state variables.

The estimated value of the state variable $x$ at $(k+1)$ th iteration can be expressed as

$$
x_{k+1}=x_{k}+G\left(x_{k}\right)^{-1}\left[H\left(x_{k}\right)^{T} W^{-1}\right]\left[z-h\left(x_{k}\right)\right]
$$

where $H$ represents the Jacobian matrix, and it is calculated by taking the partial derivative of each nonlinear measurement function $h(x)$ with respect to state variable $x$ and $G$ represents the gain matrix, which is given as

$$
G\left(x_{k}\right)=H\left(x_{k}\right)^{T} W^{-1} H\left(x_{k}\right)
$$

The inverse of the covariance matrix $W$ can be defined as

$$
W^{-1}=\left[\begin{array}{cccccc}
W_{S}^{-1} & 0 & 0 & 0 & 0 & 0 \\
0 & W_{\mathrm{IED}}^{-1} & 0 & 0 & 0 & 0 \\
0 & 0 & W_{\mathrm{PMU}, \text { real }}^{-1} & 0 & 0 & 0 \\
0 & 0 & 0 & W_{\mathrm{PMU}, \text { imag }}^{-1} & 0 & 0 \\
0 & 0 & 0 & 0 & W_{\mathrm{PMU}, \text { imag }}^{-1}
\end{array}\right]
$$

The subscripts in (5) $S$, IED, $P$, and $V$ represent substation measurement, IED measurement, pseudo-measurement, and virtual measurement, respectively. In (5), $W_{\text {IED }}$ and $W_{\text {PMU }}$ represent the covariance matrix of the uncertainty of the IED measurement and phasor measurements obtained from PMU. The error vector $r$ can be expressed as

$$
r=\left[\begin{array}{c}
z_{S}-h_{S}(x) \\
z_{\mathrm{IED}}-h_{\mathrm{IED}}(x) \\
z_{\mathrm{PMU}, \text { real }}-h_{\mathrm{PMU}, \text { real }}(x) \\
z_{\mathrm{PMU}, \text { imag }}-h_{\mathrm{PMU}, \text { imag }}(x) \\
z_{P}-h_{P}(x) \\
z_{V}-h_{V}(x)
\end{array}\right]
$$

In state estimation, it is assumed that IEDs are used to measure real and reactive power flows in a line, and PMUs are incorporated to measure voltage phasors at a bus. According to state estimation theory [23], the diagonal elements of the error covariance matrix represent the estimation variances of the states and this can be expressed as

$$
E_{x x}=G(x)^{-1}
$$

Furthermore, this can be expressed as $E_{x x}=E_{x}(\bar{x} \cdot \bar{x})=$ $E_{x}\left(\bar{x}_{i}-x_{i}\right)^{2}$, where $E_{x}$ is the operator of statistical expectation. It includes both state estimation error variance of
bus voltage magnitude and phase angle. The error vector is represented as $\bar{x}=x-\bar{x}$.

## III. MATHEMATICAL MODEL OF THE PROPOSED MOOP

The proposed meter placement technique is designed as a three-objective optimization problem. The main objective is to determine the optimal deployment of PMU and IED in a distribution network to achieve minimum cost as well as it ensures that state variables are estimated within the predefined accuracy limit. The objective functions considered to be minimized are as follows: 1) the total cost of PMUs; 2) the total cost of IEDs; and 3) RMS value of state estimation error. As the objectives considered in this paper are conflicting in nature, the meter placement problem can be designed as the multi-objective Pareto-based optimization problem [28] and [29]. Furthermore, to find the optimal tradeoff solution, in this paper, a hybrid EDA-IPM algorithm has been utilized to find the optimal position of PMU and IED, ensuring the deviations in voltage and angle estimates to be within the prespecified threshold for $95 \%$ of the test cases. Mathematically, the proposed MOOP can be expressed as

$$
\begin{aligned}
\text { Minimize } J_{1} & =\sum_{i=1}^{n l} C_{\mathrm{IED}, i} \cdot P_{\mathrm{IED}, i} \\
J_{2} & =\sum_{i=1}^{n} C_{\mathrm{PMU}, i} \cdot P_{\mathrm{PMU}, i} \\
J_{3} & =\frac{1}{m} \sum_{i=1}^{m} \sqrt{\frac{1}{2 n} \sum_{i=1}^{n} E_{x}\left(\hat{x}_{i}-x_{i}\right)^{2}}
\end{aligned}
$$

Subjected to constraints: In $95 \%$ of the operating scenarios, the deviations in voltage magnitude and absolute deviation in angle estimates are to be within the specified limits given as

$$
\begin{aligned}
& \left|\frac{V_{i}^{a}-V_{i}^{\text {est }}}{V_{i}^{a}}\right|_{95}^{m} \times 100 \leq 1 \% \\
& \left|\delta_{i}^{a}-\delta_{i}^{\text {est }}\right|_{95}^{m} \leq 0.05 \times\left|\delta_{i}^{a}\right|
\end{aligned}
$$

where the three objective functions are represented as $J_{1}, J_{2}$, and $J_{3}, n$ and $n l$ represents the number of buses and lines, respectively, in a distribution network, $x$ is the state variable, $\hat{x}$ is the estimated value of the state variable $x, C_{\mathrm{IED}}$ and $C_{\mathrm{PMU}}$ are, respectively, the relative cost of an IED and PMU, and $m$ denotes the total number of operating scenarios. $P_{\text {IED }}$ and $P_{\text {PMU }}$ are treated as binary decision vectors, i.e., the presence and absence of a meter in a line or at a bus is indicated by 1 or $0, V_{i}^{a}$ and $\delta_{i}^{a}$ are the actual or true value of the voltage magnitude and angle of $i$ th bus, and $V_{i}^{\text {est }}$ and $\delta_{i}^{\text {est }}$ represent the estimated bus voltage magnitude and angle at $i$ th bus, respectively. In this paper, voltage magnitude error is expressed in relative percentage and phase angle error in absolute value to make it more meaningful in terms of phasor estimation.

## IV. Solution Methodology

To find the optimal solution of the proposed MOOP described in Section III, a hybrid EDA-IPM algorithm has been used in this paper. Therefore, in this section, a brief

introduction to the traditional EDA and IPM algorithm has been discussed as follows.

## A. Estimation of Distribution Algorithm

In conventional GA, crossover and mutation operators are being used for generating new solutions as well as to explore the search space for finding near global optimal solutions. However, these operators may disrupt the good solutions during the evolution process and also obstructing to get the optimal solutions. This situation is more likely to occur when the problem variables are correlated. Therefore, the estimation of distribution algorithm (EDA) has been using widely in various field of engineering applications to overcome these shortcomings of traditional GA [30] and [31]. It is a population-based evolutionary optimization algorithm that employs a probabilistic model to generate new solutions for the immediate generation. Moreover, the sampling of new individuals is based on the probabilistic model estimated from the database consisting of some selected individuals from the previous generation. Therefore, the EDA algorithm is good at exploring the search space to find prominent solutions.

The basic steps of a traditional EDA algorithm have been provided below. First, the initial solutions are generated randomly within the specified limits. Then, the fitness function is evaluated for each individual solution. Out of the total population $P, N<P$ solutions are selected as best solutions using any selection mechanism. Based on the selected individuals, a probabilistic model is estimated to lead the searching process toward the regions that contain better fitness values. However, the choice of probabilistic model influences the performance and efficiency of the EDA algorithms. Then, the offspring is created using different sampling techniques. The above steps are repeated until it meets the stopping criteria. The pseudocode of the above procedure is provided in the following.

## Begin

Initialization: Generate $P$ initial population randomly within the search space.

## - Do While (termination criteria is not met)

Evaluation: Calculate the fitness value of $P$ individuals.

Selection: By using any selection method, select $N<P$ individuals.

Probabilistic model: Estimate the probability $p_{x}(x)$ that an individual being among the selected population.

Sampling: Sample $P$ individuals from $p_{x}(x)$ using sampling technique.

## End Do

End

## B. Interior Point Method

The IPM is basically used to solve linear and nonlinear convex optimization problems [33]. In this, the Lagrange multipliers are employed to deal with the equality and inequality
constraints of the optimization problem. In order to avoid the negativity conditions of the slack variables, the logarithmic barrier functions have been added to the objective function [34]. In this paper, the decision variables are considered to be continuous. The proposed nonlinear constraint optimization problem can be transformed to unconstraint optimization problem as

$$
\begin{aligned}
& L(z, y, l, u, v, w) \\
& \quad=f(x)-v^{T}\left(x-l-x_{\min }\right)-y^{T} g(x) \\
& \quad+w^{T}\left(x+u-x_{\max }\right)-\mu \sum_{i}\left(\ln l_{i}+\ln u_{i}\right)
\end{aligned}
$$

where $u$ and $l$ are the slack variables; $y, v$, and $w$ are the Lagrange multipliers; and the barrier parameter is represented by $\mu$.

In order to satisfy the Karush-Kuhn-Tucker (KKT) conditions, the first-order derivatives of a set of nonlinear algebraic equations have to be formed and then Newton-Raphson method is employed to solve the above first-order differential equations. During the iterative procedure of the IPM, if the KKT conditions shown below are satisfied then the algorithm will stop. The KKT conditions are described as

$$
\begin{aligned}
\left\|L_{x}\right\| & =\left\|\nabla f(x)-\nabla g^{T}(x) y-v+w\right\| \prec \varepsilon \\
\left\|L_{y}\right\| & =\|g(x)\| \prec \varepsilon \\
\left\|L_{w}\right\| & =\left\|x+u-x_{\max }\right\| \leq \varepsilon \\
\left\|L_{v}\right\| & =\left\|x-l-x_{\min }\right\| \leq \varepsilon
\end{aligned}
$$

According to primal-dual theory, $x$ is the primal variable, $l$ and $u$ are the slack variables, $y, v$, and $w$ are the dual variables, respectively, and $\varepsilon$ is a very small number. Equations (15)-(17) are called the primal feasible conditions and (14) is known as dual feasible conditions. If the solution satisfies the above conditions, then it is an optimal solution for the optimization problem.

## C. Proposed Multi-objective Hybrid EDA-IPM Algorithm

The EDA algorithm has been used widely in a variety of engineering applications, because it is efficient in exploring search space more efficiently. Although EDA has good exploration ability, it suffers from poor exploitation capability [30]. Therefore, the optimal solutions obtained using EDA may not be a global optimal solution. On the other hand, local searching capability of IPM algorithm is more effective [33]. Hence, the traditional EDA algorithm has been hybridized with IPM to enhance the balance between exploration and exploitation capability of the traditional EDA algorithm to obtain near global optimal solutions.

The objective functions considered in this paper are modeled as an MOOP. Moreover, as the objectives are conflicting in nature, the simultaneous optimization needs a compromised solution because each objective in the model is conflicting to one another. Therefore, to achieve better compromised solution between the objectives, Pareto-based nondominated sorting (NDS) approach has been implemented [22], [29]. It states that, in a nondominated Pareto front, all solutions are equally important because no solution is dominating the other in the population. In MOOP, solution relies on a set

of solutions unlike single objective optimization problem. Therefore, Pareto-based NDS technique has been employed with hybrid EDA-IPM to achieve the best trade-off solution between the multiple objectives. In this paper, a trade-off solution between the total cost of PMU and IED needed for the accurate estimation of system states is determined using the multi-objective hybrid EDA-IPM algorithm. The pseudo-code of the proposed Bayesian-network-based probabilistic hybrid EDA-IPM algorithm is presented in the following.

In most EDAs, it is a common practice to estimate the probabilistic model of the selected solution obtained from the previous generation, and thereafter the sampling algorithm is expected to be used for generation of new solutions based on the statistics obtained from the selected solutions. In this paper, Gaussian Bayesian network has been used as a probabilistic model to estimate the new solution for the next generation during the optimization process. The proposed hybrid EDA-IPM algorithm uses this probabilistic model to study the characteristics of the selected solutions to generate new individuals for the optimization problem in searching for the optimal Pareto front. In the case of MOOP, one of the most commonly used ranking methods is NDS technique to rank each individual for the selection purpose [30]. In NDS, the solutions are sorted into nondominated Pareto fronts, and then each solution in the same Pareto front is sorted based on their crowding distances in the objective space. The new solutions are sampled from the probability distribution employed in the Bayesian network. Basically, in this paper, sample Gaussian UnivModel has been used to sample the solutions.

In the beginning of the optimization process, the initial solutions are generated randomly using the seeding approach within the search space. Each solution represents the combinations of the number of PMUs and IEDs as well as their locations. Based on each combination of PMUs and IEDs, the objective functions are evaluated using the BCDSSE algorithm. Then, the selection mechanism is used to select some of the best solutions so far. In order to achieve better performance, the selected solutions are updated using the IPM algorithm. After the update, the probabilistic Bayesian model has been used to predict the new solutions for the future generation by using the selected solution. During fitness calculation, the constraints violation checking has to be carried out. In each Monte-Carlo (MC) trial, the error in bus voltage magnitude and angle estimate is determined. For each combination of PMUs and IEDs in a solution, if in $95 \%$ of the simulated cases, the estimated errors are below the threshold limits, then for that solution the objective functions are evaluated and stored. In contrast, if it is not within the threshold limit, then for that particular solution, a higher value of objective is been assign. Hence, this particular solution can be eliminated during the next immediate generation. Then, the above steps are repeated until all the solutions in a given population size are in first front. The convergence criterion for the algorithm to stop is, when all the solutions are reached in optimal Paretofront curve. To get the best solution in the optimal Pareto front, fuzzy theory discussed in [35] has been used. In the optimization process, population size of different values like 20,30 , and 50 have been tried. However, it has been found
that there is no such significant variation in the result for taking different population sizes for the IEEE 69-bus system and Indian 85-bus system reported. Finally, a population size of 20 has been fixed for evaluating the performance of the proposed optimization algorithm.

## V. TEST AND SIMULATION CONDITION

This paper considered the following test and simulation conditions for analyzing the performance of the proposed state estimation formulation and algorithm in the MATLAB 2014b environment. To estimate the system state (branch current magnitude and angle), the BCDSSE algorithm has been utilized. The measurement data are generated by adding small Gaussian noise of $1 \%, 3 \%$, and $5 \%$ to the actual or reference value of the quantity of interest to be measured. There are different kinds of measurements have been considered for state estimation such as: substation measurement, pseudo-measurement, real measurement, and virtual measurement [34]. It is assumed that, the former two types of measurements give the information about real and reactive power injections at the buses. The real measurements are obtained from IEDs and PMUs. It is assumed that IED gives the information about real and reactive power flows in a line and PMU provides only the information about bus voltage phasors. PMU normally measures current when possible, but here only voltage phasor measurements are considered. Furthermore, the measurement uncertainties are considered based on the maximum percentage of error associated with each type of measurement [16]. Information about the measurement data is provided in the following.

1) Substation Measurements: The measurements that are collected from the substation are called as default measurements. Generally, the substation measurements are considered to have high accuracy, and therefore, in this test $1 \%$ error has been chosen for substation measurements.
2) Real Measurements: The measurements obtained from IEDs and PMUs are assumed as real measurements. In this test, different accuracy values have been chosen for IEDs measurements. For IEDs, the maximum allowable error considered is $1 \%, 3 \%$, and $5 \%$. In the case of PMU (synchronized measurements), the maximum allowable error of $0.7 \%$ have been considered [19].
3) Pseudo-Measurements: Basically, the pseudomeasurements are obtained from the historical customer load data, and the error associated with the pseudomeasurements is relatively very high. Thus, the maximum percentage of error assumed for this is $50 \%$.
4) Virtual Measurements: The measurements at the zero injection buses are treated as virtual measurements with a low variance of $10^{-7}$ [34].
Furthermore, in this study, for better visualization, random variations in load and generator have been considered. Different operating scenarios are simulated by considering the load demands and generator output as stochastic variable following the Gaussian distribution around the mean value with prefixed standard deviation. Moreover, the impacts of measurement uncertainties on state estimation performance have been stud-

Algorithm 1 Pseudo-Code of the Proposed Multi-objective Hybrid EDA-IPM Algorithm
Step1. Initialization: Generate random number and location of IEDs and PMUs for each individual solution in the population (Pop) within the limits. Where Pop represents size of the population
Do while ("Stopping criterion is not met")
Step 2. Fitness evaluation: Evaluate the objective functions $J_{1}, J_{2}$ and $J_{3}$ for each solution based on the position of PMUs and IEDs.
Step 3. Selection: Select $N<$ Pop solutions from Pop using Non-dominated sorting selection strategy. Pop is the size of the population and $N$ is a number less than Pop.

## Begin

Do while ("Stopping criterion is not met")
For $i=1: N$ (number of selected solutions)

1. Use each selected solution $s(i)$ as initial point in IPM algorithm to find a best solution $y(i)$ (location of PMU and IED) for that solution $i$.
2. Evaluation: Calculate the objective functions $J_{1}, J_{2}$ and $J_{3}$ and evaluate the fitness value for each $i$ using weighting approach.
3. Update solution:

$$
\begin{aligned}
& \text { if Fitness } y(i)<\text { Fitness } s(i) \\
& \text { \&\& if solution } \quad y(i) \text { dominates } s(i) \\
& \quad \text { then } s(i)=y(i)
\end{aligned}
$$

## End for $i$

## End Do

End
Step 4. Probabilistic graphical model: Estimate the probability distribution of the previous solutions and selected solution to predict new population for the next generation using Gaussian Bayesian network.
Mathematically, it can be expressed as:

$$
p\left(x_{i} \mid p a\left(X_{i}\right)\right)=\mathrm{N}\left(\mu_{i}+\sum_{X_{j} \in P a\left(X_{i}\right)} w_{i j}\left(x_{j}-\mu_{j}\right), v_{i}^{2}\right)
$$

where $\mu_{i}$ represents the mean of the variable $X_{i}, v_{i}$ is the standard deviation of the distribution and $w_{i j}$ is the weight associated with each of the parents and $x_{j}$ is the value of the variable $X_{j}$ in $p a\left(X_{i}\right)$.
Step 5. Sampling technique: Sample Pop number of solutions from the Gaussian Bayesian network using sample Gaussian UnivModel.

## End Do

Post-procession of the results

TABLE I
DG Installation BuS AND CAPACITY

| Test system | Bus Number | DG capacity( in MW) Base <br> Value |
| :--: | :--: | :--: |
| IEEE 69-bus <br> system | 50 | 0.180 |
| Practical <br> Indian 85-bus <br> system | 45 | 0.270 |

ied using MC simulation [22]. There are thousands of different network states that are generated from each network condition to study the impacts of measurement uncertainties on the state estimation performance. The total number of operating conditions considered is 100 . Hence, the total number of operating scenarios considered in this study is $100 \times 1000$. A standard deviation of $\pm 10 \%$ of the base value is assumed for each operating condition.

The number of IEDs and PMUs required and their locations in an active distribution network is presented in this paper. In the distribution network, if there is no source, such as DGs or energy storage devices, then the network
becomes passive in nature. This paper considered that DGs are integrated so the distribution network becomes active. The state estimation study in active distribution network is called as active distribution state estimation. It is assumed that the DG output is stochastic in nature and following normal distribution. Furthermore, it is specified that all DGs are injecting only real power to the buses where it is integrated. The base values of DG power output and their locations are provided in Table I [22], [36], [37]. In the simulation study, it is considered that the random load and generation value (as $10 \%$ of the base value) have been considered separately and after that both the values are sum together to find the net injection at a particular bus. Furthermore, the injection of DGs into the network brings no modification in the mathematical approach. All the parameters used in the EDA and NDS GA (NSGA-II) algorithm have been shown in Table II. Different parameters used in the EDA algorithm for probabilistic learning, sampling, selection, and repairing process are provided in Table II.

For the simulation study, the relative cost of each PMU is assumed as 1 pu , and for an IED, the cost is 0.6 pu [19]. Actually, in practice, the cost of the measurement devices

TABLE II
Parameters Used in EDA, NSGA-II, and Simulated Annealing Algorithm

| EDA | NSGA-II | Simulated Annealing (SA) |
| :--: | :--: | :--: |
| Learning method -Learn Gaussian Bayesian Model | Population size $=20$ | Initial Temperature $\left(T_{0}\right)=100$ |
| Sampling method- Sample Gaussian Universal Model | Cross over rate $=0.8$ | Scheduling factor $(\alpha)=0.99$ |
| Replacement method- Pareto Rank ordering | Mutation rate $=0.02$ |  |
| Selection method - Non-Dominated selection | Number of generation $=20$ |  |
| Repairing method-Set In Bounds repairing |  |  |
| Population size $=20$, number of generation $=20$ |  |  |

![img-0.jpeg](img-0.jpeg)

Fig. 1. Single-line diagram of IEEE 69 bus system.
depends on the application scenarios. Generally, the cost of a PMU is more than the IED; therefore, in this study, the relative cost of PMU and IED are considered as 1 and 0.6 pu , respectively. To obtain the optimal trade-off solution, fuzzy theory has been used and is discussed in [35].

## VI. SimULATION RESULTS AND DISCUSSION

## A. IEEE 69 Bus System

A standard IEEE 69-bus, 12.66-kV radial distribution network, has been considered to test the effectiveness of the proposed algorithm. This test system includes 69 buses, 68 lines along with 48 loads, and two DGs integrated at bus numbers 50 and 61 . The load and line parameters of the test system are obtained from [38]. The total load of the system is 3.802 MW and 2.692 MVAr, respectively. Fig. 1 represents single line diagram of the IEEE-69 bus system. In this system, there are 21 buses, where there is no source or load is connected. Therefore, these are treated as zero injection buses [22]. The real and reactive power injections at the zero injection buses are assumed as virtual measurements with a higher degree of accuracy level.

The obtained results using the proposed algorithm under different measurement uncertainties have been shown in Table III. The total number of PMU and IED required for quality state estimation results are also provided in Table III. It is seen that when $1 \%$ error is considered for IED measurements and $50 \%$ for pseudo-measurement, the total configuration cost is 3.8 using hybrid EDA-IPM and the RMS value of state estimation error is 0.0098 . Similarly, in the case of EDA-simulated annealing (SA), EDA, and NSGA-II, the total
![img-1.jpeg](img-1.jpeg)

Fig. 2. (a) Optimal Pareto front between objective J1 and J2 ( $1 \%$ error in IEDs and $50 \%$ for pseudo-measurements. (b) Optimal Pareto front between objective J1 and J3 ( $1 \%$ error in IEDs and $50 \%$ for pseudo-measurements). (c) Optimal Pareto front between objective J2 and J3 ( $1 \%$ error in IEDs and $50 \%$ for pseudo-measurements).
cost obtained is $4.4,4.6$, and 6.8 pu . The RMS values of state estimation error obtained using EDA-SA, EDA, and NSGA-II are $0.0114,0.0141$, and 0.0129 , respectively. Furthermore, the optimal Pareto fronts between the objectives $J_{1}, J_{2}$, and $J_{3}$ have been shown in Fig. 2. The optimal number and location of PMUs and IEDs are obtained from the optimal Pareto fronts for their respective algorithms using fuzzy theory discussed in [35]. From the figures, it is worth noting that the global optimal Pareto fronts have been achieved using the proposed algorithm due to its higher degree of balance between the exploration and exploitation during the search process. In most cases, it is seen that IEDs are placed at the main feeders to reduce the state estimation error and the combination of IEDs and PMUs provides a better solution to improve the state estimation accuracy in modern active distribution networks. Additionally, the maximum relative percentage error in the voltage magnitude and the maximum absolute phase angle error under all measurement uncertainty cases are also provided in Table III, to check the reliability of the respective algorithm.

Furthermore, the test has been carried out by considering $3 \%$ and $5 \%$ error in IEDs along with $50 \%$ error in pseudo-

TABLE III
Optimal Location of PMUs and IEDs in IEEE 69 Bus Active Distribution System

| Metrological <br> Error of <br> IEDs | Algorithm | PMUs location (Bus number) | IEDs location (Line number) | Objective functions value |  |  | Maximum relative percentage error in voltage magnitude (\%) | Maximum absolute phase angle error (crad) |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  | $J_{1}$ | $J_{2}$ | $J_{3}$ |  |  |
| $1 \%$ | Proposed <br> EDA-IPM | 27, 62 | 1, 2, 4 | 1.8 | 2 | 0.0098 | 0.2311 | 0.0243 |
|  | EDA-SA | 14, 15 | $1,3,9,13$ | 2.4 | 2 | 0.0114 | 0.3879 | 0.0586 |
|  | EDA | 62 | $1,2,42,45,56,60$ | 3.6 | 1 | 0.0141 | 0.3671 | 0.0597 |
|  | NSGA-II | 21, 27, 34, 49, 57 | $1,6,37$ | 1.8 | 5 | 0.0129 | 0.4127 | 0.0512 |
| $3 \%$ | Proposed <br> EDA-IPM | 21,51,62 | 1,2,8,11,32,48 | 3.6 | 3 | 0.0105 | 0.3499 | 0.0479 |
|  | EDA-SA | 39,47 | $\begin{gathered} 1,2,8,29,30,33,52,58 \\ 1,7,11,19,44,48,49,52,59 \\ 66,63 \end{gathered}$ | 4.8 | 2 | 0.0134 | 0.3967 | 0.1005 |
|  |  |  |  |  |  |  |  |  |
|  | NSGA-II | 17,39,43,48,57,63 | 1,9,16,31,42 | 3 | 6 | 0.0135 | 0.4003 | 0.1231 |
| $5 \%$ | Proposed <br> EDA-IPM | 27, 67 | 1,2,3,8,25,29,57,65 | 4.8 | 2 | 0.0152 | 0.3931 | 0.0725 |
|  | EDA-SA | 4,15 | 1,20,31,34,44,52,60,61,64 | 5.4 | 2 | 0.0179 | 0.5763 | 0.2430 |
|  | EDA | 26,31,40,60,62 | 1,9,27,40,53 | 3 | 5 | 0.0184 | 0.4061 | 0.2813 |
|  | NSGA-II | 14,17,36,44 | $\begin{gathered} 1,7,9,13,14,17,31,32 \\ 39,47,54,60,63 \end{gathered}$ | 7.8 | 4 | 0.0182 | 0.6437 | 0.2324 |

measurements. The obtained results have been reported in Table III. It is seen that the total cost of the configuration is slightly increased because of more noise that has been added to IED measurements. In these cases also, the performance of the proposed hybrid EDA-IPM algorithm is found to be better than those of all other algorithms used in this paper. The main advantage of using this multi-objective meter placement technique is that the operator can obtain a best compromised or a trade-off solution between the objectives to minimize the cost as well as the state estimation error. Basically, the selection of optimal solution depends on the decision maker. But in this paper, fuzzy theory has been used to find the best compromised solution between the objectives. Generally, meter placement techniques are used for the study of distribution systems. Therefore, the computational cost and complexity of the proposed technique do not have a significant impact on the planning study of the distribution system. The computational cost can be reduced if less number of MC trials is considered in the simulation study. However, if the MC value is high then more accurate results can be expected.

## B. Practical Indian 85 Bus System

The effectiveness of the proposed algorithm has also been tested on a large scale practical Indian 85 -bus, $11-\mathrm{kV}$ radial distribution network. The system includes 85 buses and 84 lines along with two DG at bus numbers 45 and 61, respectively. This system carries a total load of 2.574 MW and 2.622 MVAr. Furthermore, it includes 26 zero injection buses. The single line diagram of this test system is shown in Fig. 3. The network load and line data are taken from [39].

The simulation results for Indian 85 bus system using the proposed algorithm under different operating conditions have been shown in Table IV. When the IEDs accuracy is
![img-2.jpeg](img-2.jpeg)

Fig. 3. Single-line diagram of Indian 85-bus radial distribution network.
considered as $1 \%$, the total configuration cost is 4.2 pu using the proposed EDA-IPM algorithm. The RMS value of the state estimation error is 0.0096 . In the case of EDA-SA, EDA, and NSGA-II, the total cost is $5,4.6$, and 5.6 pu as well as the average RMS value of estimation errors obtained are $0.0143,0.0123$, and 0.0131 , respectively. Furthermore, the optimal Pareto fronts between the objectives $J_{1}, J_{2}$, and $J_{3}$ have been shown in Fig. 4. From the figures, it is seen that the global optimal Pareto fronts have been achieved using the proposed algorithm due its higher degree of balance between the exploration and exploitation during the search process. Moreover, to test the efficiency of the proposed algorithm, different metrological errors of the IEDs have been considered such as $3 \%$ and $5 \%$ along with $50 \%$ error in pseudo-measurements, and the obtained results have been reported in Table IV. It is observed that the total configuration

TABLE IV
Optimal Location of PMUs and IEDs in Indian 85 Bus Active Distribution System

| Metrological <br> Error of <br> IEDs | Algorithm | PMUs location (Bus number) | IEDs location (Line number) | Objective functions value |  |  | Maximum relative percentage error in voltage magnitude (\%) | Maximum absolute phase angle error (crad) |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  | $J_{1}$ | $J_{2}$ | $J_{3}$ |  |  |
| $1 \%$ | Proposed <br> EDA-IPM | 42,71,78 | 1,2 | 1.2 | 3 | 0.0096 | 0.2451 | 0.2871 |
|  | EDA-SA | 48,52 | 1,6,7,24,44 | 3 | 2 | 0.0143 | 0.4086 | 0.4869 |
|  | EDA | 40 | 1,3,36,51,68,73 | 3.6 | 1 | 0.0123 | 0.3217 | 0.5317 |
|  | NSGA-II | 72,76 | 1,8,14,43,47,69 | 3.6 | 2 | 0.0131 | 0.3986 | 0.4467 |
| $3 \%$ | Proposed <br> EDA-IPM | 27,67,78 | 1,2,4 | 1.8 | 3 | 0.0111 | 0.3139 | 0.4349 |
|  | EDA-SA | 37,59,68 | 1,35,53,73 | 2.4 | 3 | 0.0132 | 0.3890 | 0.6662 |
|  | EDA | 53,55 | $\begin{gathered} 1,3,5,6,16,17,29 \\ 30,35,42,43 \end{gathered}$ | 6.6 | 2 | 0.0137 | 0.4341 | 0.5970 |
|  | NSGA-II | 26,30,51,61 | $\begin{gathered} 1,2,4,5,19,65,67 \\ 71,78 \end{gathered}$ | 5.4 | 4 | 0.0129 | 0.3789 | 0.6791 |
| $5 \%$ | Proposed <br> EDA-IPM | 27,42,60,62,70,75 | 1,3,5 | 1.8 | 6 | 0.0146 | 0.4231 | 0.4719 |
|  | EDA-SA | 63,71,82,83 | $\begin{gathered} 1,6,8,18,26,28,42, \\ 45,51,66,69 \end{gathered}$ | 6.6 | 4 | 0.0154 | 0.5280 | 0.6743 |
|  | EDA | 67 | $\begin{gathered} 1,4,5,13,19,26,32, \\ 43,49,61,67,76,80 \end{gathered}$ | 7.8 | 1 | 0.0171 | 0.4950 | 0.7062 |
|  | NSGA-II | $\begin{gathered} 39,52,61,65,71 \\ 76,79,82 \end{gathered}$ | 1,3,5,6,34,37 | 3.6 | 8 | 0.0202 | 0.5327 | 0.8128 |

![img-3.jpeg](img-3.jpeg)

Fig. 4. (a) Optimal Pareto front between objective J1 and J2 ( $1 \%$ error in IEDs and $50 \%$ for pseudo-measurements). (b) Optimal Pareto front between objective J1 and J3 ( $1 \%$ error in IEDs and $50 \%$ for pseudo-measurements). (c) Optimal Pareto front between objective J2 and J3 ( $1 \%$ error in IEDs and $50 \%$ for pseudo-measurements).
cost is increased because of more noise that has been added in IED measurements. It is worth noting that the performance of the proposed hybrid EDA-IPM algorithm is found to be more superior than those of all other algorithms used in this paper due to its higher degree of balance between the intensification and diversification capability. This is possible due to the
hybridization of the IPM algorithm at a higher exploitation level with traditional EDA of having better exploration ability.

## VII. CONCLUSION

This paper formulated a new MOOP to find optimal tradeoffs in PMUs and IEDs deployment for state estimation in active distribution networks. A new hybrid EDA is proposed to find the optimal number and location of PMUs and IEDs for accurate state estimation. The local searching capability of the classical EDA algorithm is improved by hybridizing with the IPM. The hybridization of EDA and IPM brings a balance between the exploration and exploitation capability of the algorithm during the search process. Furthermore, different uncertainties level of measurement devices and load variations are also taken into consideration for testing the reliability of the state estimator. The performance of the hybrid EDA-IPM algorithm is tested on the standard IEEE 69 -bus system as well as on the Indian 85 -bus system. The obtained results using hybrid EDA-IPM algorithm are compared with those of the conventional EDA algorithm, NSGA-II, and the EDA-SA algorithm existing in the literature. It is found that the proposed algorithm is more efficient, reliable, and robust under various operating conditions and metrological characteristics of the measurement devices. Moreover, the performance of the proposed algorithm is found to be more superior than that of other algorithms used in this paper. Hence, the proposed multi-objective-based meter placement technique can be used for the planning study and for monitoring of smart distribution networks.

## REFERENCES

[1] J. Fan and S. Borlase, "The evolution of distribution," IEEE Power Energy Mag., vol. 7, no. 2, pp. 63-68, Mar. 2009.
[2] S. Repo, K. Maki, P. Jarventansta, and O. Samuelsson, "ADINEEU demonstration project of active distribution network," in Proc. IETC/RED Seminar Smart Grids Distrib., Jun. 2008, pp. 1-5.
[3] R. Singh, B. C. Pal, and R. B. Vinter, "Measurement placement in distribution system state estimation," IEEE Trans. Power Syst., vol. 24, no. 2, pp. 668-675, May 2009.
[4] O. Chilard, S. Grenard, O. Devaux, and L. de Alvaro Garcia, "Distribution state estimation based on voltage state variables: Assessment of results and limitations," in Proc. 20th Int. Conf. Exhibit. Electr. Distrib. (CIRED), Jun. 2009, pp. 1-4.
[5] S. M. S. Alam, B. Natarajan, and A. Pahwa, "Distribution grid state estimation from compressed measurements," IEEE Trans. Smart Grid, vol. 5, no. 4, pp. 1631-1642, Jul. 2014.
[6] Y. Deng, Y. He, and B. Zhang, "A branch-estimation-based state estimation method for radial distribution systems," IEEE Trans. Power Del., vol. 17, no. 4, pp. 1057-1062, Oct. 2002.
[7] M. E. Baran and A. W. Kelley, "A branch-current-based state estimation method for distribution systems," IEEE Trans. Power Syst., vol. 10, no. 1, pp. 483-491, Feb. 1995.
[8] R. Madlener, J. Liu, A. Monti, C. Muscas, and C. Rosen, "Measurement and metering facilities as enabling technologies for smart electricity grids in Europe," Special Study No. 1/2009, Sectoral e-Bus. Watch, Oct. 2009.
[9] J. De La Ree, V. Centeno, J. S. Thorp, and A. G. Phadke, "Synchronized phasor measurement applications in power systems," IEEE Trans. Smart Grid, vol. 1, no. 1, pp. 20-27, Jun. 2010.
[10] J. S. Thorp, A. Abur, M. Begovic, J. Giri, and R. Avila-Rosales, "Gaining a wider perspective," IEEE Power Energy Mag., vol. 6, no. 5, pp. 43-51, Sep. 2008.
[11] A. G. Phadke and J. S. Thorp, Synchronized Phasor Measurements and Their Applications. Springer, 2008.
[12] M. Pau, P. A. Pegoraro, and S. Sulis, "Efficient branch-current-based distribution system state estimation including synchronized measurements," IEEE Trans. Instrum. Meas., vol. 62, no. 9, pp. 2419-2429, Sep. 2013.
[13] G. T. Heydt, "The next generation of power distribution systems," IEEE Trans. Smart Grid, vol. 1, no. 3, pp. 225-235, Dec. 2010.
[14] M. Albu, G. T. Heydt, and S.-C. Cosmescu, "Versatile platforms for wide area synchronous measurements in power distribution systems," in Proc. North Amer. Power Symp. (NAPS), Sep. 2010, pp. 1-7.
[15] M. Paolone, A. Borghetti, and C. A. Nucci, "Development of an RTU for synchrophasors estimation in active distribution networks," in Proc. IEEE Bucharest PowerTech, Jul./Jul. 2009, pp. 1-6.
[16] R. Singh, B. C. Pal, and R. A. Jabr, "Choice of estimator for distribution system state estimation," IET Generat., Transmiss. Distrib., vol. 3, no. 7, pp. 666-678, Jul. 2009.
[17] M. E. Baran, J. Zhu, and A. W. Kelley, "Meter placement for real-time monitoring of distribution feeders," IEEE Trans. Power Syst., vol. 11, no. 1, pp. 332-337, Feb. 1996.
[18] C. Muscas, F. Pilo, G. Pisano, and S. Sulis, "Optimal allocation of multichannel measurement devices for distribution state estimation," IEEE Trans. Instrum. Meas., vol. 58, no. 6, pp. 1929-1937, Jun. 2009.
[19] J. Liu, J. Tang, F. Ponci, A. Monti, C. Muscas, and P. A. Pegoraro, "Trade-offs in PMU deployment for state estimation in active distribution grids," IEEE Trans. Smart Grid, vol. 3, no. 2, pp. 915-924, Jun. 2012.
[20] P. A. Pegoraro and S. Sulis, "Robustness-oriented meter placement for distribution system state estimation in presence of network parameter uncertainty," IEEE Trans. Instrum. Meas., vol. 62, no. 5, pp. 954-962, May 2013.
[21] R. Singh, B. C. Pal, R. A. Jabr, and R. B. Vinter, "Meter placement for distribution system state estimation: An ordinal optimization approach," IEEE Trans. Power Syst., vol. 26, no. 4, pp. 2328-2335, Nov. 2011.
[22] S. Prasad and D. M. V. Kumar, "Optimal allocation of measurement devices for distribution state estimation using multiobjective hybrid PSO-Krill herd algorithm," IEEE Trans. Instrum. Meas., vol. 66, no. 8, pp. 2022-2035, Aug. 2017.
[23] V. Ramesh, U. Khan, and M. D. Ilic, "Data aggregation strategies for aligning PMU and AMI measurements in electric power distribution networks," in Proc. North Amer. Power Symp. (NAPS), Aug. 2011, pp. 1-7.
[24] M. Zhou, V. Centeno, J. Thorp, and A. Phadke, "An alternative for including phasor measurements in state estimators," IEEE Trans. Power Syst., vol. 21, no. 4, pp. 1930-1937, Nov. 2006.
[25] IEEE Standard for Synchrophasor Measurements for Power Systems, IEEE Standard C37.118.1-2011 (Revision of IEEE Std C37.118-2005), Dec. 2011.
[26] H. Wang and N. N. Schulz, "A revised branch current-based distribution system state estimation algorithm and meter placement impact," IEEE Trans. Power Syst., vol. 19, no. 1, pp. 207-213, Feb. 2004.
[27] M. E. Baran and W. Kelley, "A branch-current-based state estimation method for distribution systems," IEEE Trans. Power Syst., vol. 10, no. 1, pp. 483-491, Feb. 1995.
[28] K. Deb, Multi-Objective Optimization Using Evolutionary Algorithms. New Delhi, India: Wiley, 2001.
[29] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, "A fast and elitist multiobjective genetic algorithm: NSGA-II," IEEE Trans. Evol. Comput., vol. 6, no. 2, pp. 182-197, Apr. 2002.
[30] V. A. Shim, K. C. Tan, and C. Y. Cheong, "A hybrid estimation of distribution algorithm with decomposition for solving the multiobjective multiple traveling salesman problem," IEEE Trans. Syst., Man, Cybern. C, Appl. Rev., vol. 42, no. 5, pp. 682-691, Sep. 2012.
[31] H. Karshenas, R. Santana, C. Bielza, and P. Larraluaga, "Multiobjective estimation of distribution algorithm based on joint modeling of objectives and variables," IEEE Trans. Evol. Comput., vol. 18, no. 4, pp. 519-542, Aug. 2014.
[32] W. Yan, F. Liu, C. Y. Chung, and K. P. Wong, "A hybrid genetic algorithm-interior point method for optimal reactive power flow," IEEE Trans. Power Syst., vol. 21, no. 3, pp. 1163-1169, Aug. 2006.
[33] Y. Wang and Q. Jiang, "Reactive power optimizatin of distribution network based on primal-dual interior point method and simplified branch and bound method," in Proc. IEEE PES T\&D Conf. Expo., Apr. 2004, pp. 1-4.
[34] W.-M. Lin and J.-H. Teng, "State estimation for distribution systems with zero-injection constraints," IEEE Trans. Power Syst., vol. 11, no. 1, pp. 518-524, Feb. 1996.
[35] S. Kayalvichi and D. M. V. Kumar, "Disparitable DG planning in distribution networks considering costs," in Proc. IEEE Int. Conf. Recent Develop. Control, Autom. Power Eng. (RDCAPE), Mar. 2015, pp. 320-325.
[36] B. Arandian, R.-A. Hooshmand, and E. Gholipour, "Decreasing activity cost of a distribution system company by reconfiguration and power generation control of DGs based on shuffled frog leaping algorithm," Int. J. Electr. Power Energy Syst., vol. 61, pp. 48-55, Oct. 2014.
[37] G. V. N. Lakshmi, A. J. Laxmi, and S. V. Reddy, "Optimal allocation and sizing of distributed generation in distribution network using ant colony search algorithm," in Proc. Int. Conf. Adv. Commun., Netw., Comput. (CNC), 2014, pp. 669-675.
[38] J. S. Savier and D. Das, "Impact of network reconfiguration on loss allocation of radial distribution systems," IEEE Trans. Power Del., vol. 22, no. 4, pp. 2473-2480, Oct. 2007.
[39] D. Das, D. P. Kothari, and A. Kalam, "Simple and efficient method for load flow solution of radial distribution networks," Int. J. Electr. Power Energy Syst., vol. 17, no. 5, pp. 335-346, Oct. 1995.
![img-4.jpeg](img-4.jpeg)

Sachidananda Prasad received the B.Tech. degree in electrical engineering from GHITM, Puri, India, and the M.Tech. degree in power systems engineering from VSSUT, Burla, India. He is currently pursuing the Ph.D. degree in electrical engineering with the National Institute of Technology, Warangal, India.

His current research interests include distribution system state estimation, smart grids, and application of artificial intelligence techniques in power systems.
![img-5.jpeg](img-5.jpeg)
D. M. Vinod Kumar received the B.E. degree in electrical engineering and the M.Tech. degree in power systems engineering from the University College of Engineering, Osmania University, Hyderabad, India, and the Ph.D. degree in electrical engineering from the Indian Institute of Technology, Kanpur, India.

He is currently a Professor with the Department of Electrical Engineering, National Institute of Technology, Warangal, India. His current research interests include power system deregulation, AI technique applications in power systems, power system stability, distribution system state estimation, and smart grids.