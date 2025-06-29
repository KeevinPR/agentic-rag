# Multi-objective hybrid estimation of distribution algorithm-interior point methodbased meter placement for active distribution state estimation 

Sachidananda Prasad ${ }^{1 \text { b }}$, Vinod Kumar Dulla Mallesham ${ }^{1}$<br>${ }^{1}$ Department of Electrical Engineering, National Institute of Technology Warangal, Warangal 506 004, Telangana State, India<br>$\omega$ E-mail: atulprasad.g@gmail.com


#### Abstract

This study proposes a new multi-objective hybrid estimation of distribution algorithm (EDA)-interior point method (IPM) algorithm to obtain the optimal location of measuring devices for state estimation (SE) in active distribution networks. The objective functions to be minimised are, the total network configuration cost, the average relative percentage error of bus voltage magnitude and angle estimates. As the objectives are conflicting in nature, a multi-objective Pareto-based nondominated sorting EDA has been proposed in this study. Moreover, due to poor exploitation capability of the EDA, it is hybridised with IPM to improve its local searching ability in the search space. The hybridisation of EDA and IPM brings a higher degree of balance between the exploration and exploitation capability of the algorithm during the search process. Furthermore, the loads and generators are treated as stochastic variable and the impact of different type of distributed generations on SE performance has also been investigated. The efficiency of the proposed algorithm is tested on PG&E 69-bus system and Indian 85-bus radial distribution network. The obtained results are compared with conventional EDA, particle swarm optimisation, nondominated sorting genetic algorithm and also with existing techniques in the literature such as dynamic programming and ordinal optimisation algorithm.


## 1 Introduction

Recently, distribution grids are moving towards more dynamic and complex in structures because of the integration of renewable sources, distributed energy storage as well as intelligent electronic devices (IED) and Smart meters. The increasingly integration of distributed generation (DG) in a distribution network will affect the planning operation and control of a distribution network significantly. The active integration of DG results bi-directional power flows from distribution level to sub-transmission level as well as it exacerbates voltage unbalance in distribution networks [1, 2]. Furthermore, the reconfiguration of the distribution system is used to minimise the power loss, voltage deviations and restoration time. In most of the cases the distribution networks are weakly meshed structure. Thus, the states of the distribution systems such as bus voltage magnitude and angles have to be estimated more accurately for real-time monitoring and control of the networks [3-6]. To achieve this, real meters have been appended in distribution systems to estimate the states more accurately for other control actions such as network reconfiguration, Volt/Var control, generation control, restoration, voltage regulation and so on [7]. Actually, meters can be placed at each and every point of the distribution network. However, it would affect the total configuration cost of the distribution system.

Basically, in distribution networks, pseudo-measurements are being used more significantly than real measurements [8]. Therefore, state estimation (SE) algorithm is employed to estimate the state of a system more accurately from the noisy data available at the distribution control centres. However, in distribution system sufficient real-time measurements are not available. Therefore, accurate SE is a more challenging task for the power engineers. So, a large number of pseudo-measurements have been incorporated in the SE algorithm to make the system fully observable and also to avoid non-convergence of the SE algorithm [8]. In fact, the pseudomeasurements are comparatively less accurate in nature because these are extracted from the historical customer load data. As a consequence, more accurate SE cannot be expected in this scenario. Therefore, the adequate number of additional real meters
has to be located at a suitable location in a distribution network to produce quality of SE solution [9].

Recently, many researchers have been proposed different meter placement techniques based SE to enhance the accuracy of state estimators. In [9], three rules have been proposed to locate the meters at suitable positions such as (i) meters have to be appended at the main switches and fuse locations, (ii) meters need to be placed at feeder sections and also (iii) on normally open tie switches which is used for feeder reconfiguration. In fact, it provides a best compromise solution between the SE accuracy and computational complexity of the technique is concerned. However, this technique may not provide an optimal number of meters for accurate SE.

In [10], dynamic programming (DP) based step-by-step approach has been proposed to obtain the optimal number of meters in distribution networks for SE. The main objective of this optimisation technique is to minimise the mean of the weighted sum of the variance of the quantities to be estimated. The constraint for this optimisation process is, the system should be observable within the pre-defined accuracy limits with minimum number of meters. Since, the above technique is based on a step-by-step approach, the solution obtained may not be an optimal. Chen et al. [11] proposed a circuit representation model for the optimal deployment of current and voltage measurements to represent estimation errors. The authors have transformed the optimisation problem to a mixed-integer linear programming problem.

In [12, 13], the authors studied the meter placement problem when heterogeneous measurement data are obtained from the Phasor Measurement Units (PMUs) and Smart Metering (SM) devices, substation and historical customer load data in an active distribution network. The authors designed an optimal metering infrastructure for an active distribution network. A trade-off between the number of PMUs and SM has been obtained for better SE performance using genetic algorithm (GA). Moreover, the authors have further extended this work by considering the lack of detailed information about DG [14], for accurate SE in distribution networks by deploying PMU and SM at appropriate locations. In

[15], the authors have discussed about optimal location of PMUs for accurate SE. Damavandi et al. [16] proposed a robust meter placement in an active distribution network for SE. A robust submodular saturation algorithm has been used to find the optimal location of PMUs and voltage magnitude meters (VMMs) in distribution systems.

In [17], the optimal placement of measurement devices for distribution SE using DP has been proposed. The robustness of the proposed technique is tested by considering the uncertainty in network parameter and measurements for SE in distribution systems. Sing et al. [18] proposed a meter placement method based on ordinal optimisation algorithm in distribution network. In this method, the meters are placed progressively until the estimated errors are below the pre-defined accuracy limits. In [19], the authors have proposed a heuristic technique to place optimal number of VMMs so that the errors in voltage magnitude at the unmonitored buses can be reduced. In this method only the reduction of errors in voltage magnitude is achieved.

Most of the meter placement techniques discussed in the literature may not produce global optimal solution due to sequential approach. These methods may not be guaranteed minimum cost with required SE accuracy. In order to achieve this, the meter placement problem is formulated as a multi-objective optimisation problem for SE in distribution network. Furthermore, the impact of different kinds of DG on SE accuracy in a multiobjective framework has also been discussed. In this paper, the optimal number of power flow meters in the presence of default measurements such as VMMs is investigated. A compromised solution is established between the cost and SE accuracy to improve the performance of the state estimator.

In this paper, to achieve optimal number and location of power flow meters, hybrid estimation of distribution algorithm-interior point method (EDA-IPM) algorithm has been proposed. The EDA has poor exploitation capability to find global solution, whereas IPM is most efficient in exploitation. Therefore, in order to improve the local searching capability of the traditional EDA, the IPM is hybridized with it in a multi-objective framework. The contribution of this paper can be summarised as follows:
(i) A new hybrid EDA-IPM algorithm is proposed to find the optimal number and location of measurement devices in distribution networks.
(ii) Since, the objectives are conflicting nature, the optimisation problem is designed as a Pareto-based optimisation problem in multi-objective environment.
(iii) A trade-off solution is established between the cost and accuracy of the state estimator by plotting different Pareto-plots between the objectives.

The organisation of this paper is as follows: The mathematical model of the optimisation problem is described in Section 2. The proposed hybrid EDA-IPM algorithm for meter placement problem has been presented in Section 3. In Section 4, the simulation conditions and results are discussed. Finally, Section 5 concludes the paper.

## 2 Problem formulation

The proposed multi-objective-based meter placement optimisation problem considered three objective functions to minimise: (i) the total cost of configuration, (ii) the average relative percentage error (ARPE) of bus voltage magnitude and (iii) ARPE of voltage angle. From the observation, it is found that the above three objectives are conflicting in nature because if more number of meters are placed then estimation errors will get reduce and vice-versa. Therefore, the concept of optimal Pareto front and fast non-dominated sorting approach have been incorporated into this multi-objective optimisation problem to find the best compromised solution [21, 22]. The objectives to be minimised are described as follows:

$$
F_{1}=\sum_{i=1}^{m} C_{\mathrm{pf}, i} \cdot P_{\mathrm{pf}, i}+\sum_{i=1}^{n} C_{\mathrm{VMM}, i} \cdot P_{\mathrm{VMM}, i}
$$

$$
\begin{aligned}
& F_{2}=\frac{1}{m} \sum_{m} \frac{1}{n}\left(\sum_{i=1}^{n} \frac{n}{\left|\sum_{i}^{m}\right|}\left|\frac{\delta_{i}^{m}-\delta_{i}^{m}}{\delta_{i}^{n}}\right|\right) \times 100 \\
& F_{3}=\frac{1}{m} \sum_{m} \frac{1}{n}\left(\sum_{i=1}^{n}\left|\frac{\delta_{i}^{n}-\delta_{i}^{n}}{\delta_{i}^{n}}\right|\right) \times 100
\end{aligned}
$$

Subjected to constraints: The constraints imposed describe in (4) and (5) considers for $95 \%$ of the simulated cases [12, 20] and is expressed as

$$
\begin{aligned}
& \frac{\left|V_{i}^{n}-V_{i}^{n \mathrm{st}}\right|}{V_{i}^{n}} \times 100 \leq 1 \\
& \left|\frac{\delta_{i}^{n}-\delta_{i}^{n \mathrm{st}}}{\delta_{i}^{n}}\right| \times 100 \leq 5
\end{aligned}
$$

where $F_{1}, F_{2}$, and $F_{3}$ represent three objective functions, $n$ and $n l$ are the number of nodes and lines in a distribution network, $m$ is the number of operating scenarios, $C_{\mathrm{pf}}$ and $C_{\mathrm{VMM}}$ indicate the relative cost of a power flow and voltage magnitude meter, respectively. The cost of these meters is normalised to unity.

In the optimisation process, the cost value assigned to both power flow meter and VMM is supposed to be equal because VMMs are considered to be as default measurements. In this paper, the location and number of VMMs are taken as same for all optimisation algorithms considered. Different cost value can be assumed for both types of meters. However, in actual practice, the cost of a measuring instrument depends on specific application scenarios.

In the above equation, $P_{\mathrm{pf}}$ and $P_{\mathrm{VMM}}$ represent the binary decision variables, i.e. if a meter is situated in a bus or lines then its value becomes one, else its value will be treated as zero, $V_{i}^{n}$ and $\delta_{i}^{n}$ indicate the actual voltage magnitude and phase angle of $i$ th bus. Similarly, $V_{i}^{\text {nst }}$ and $\delta_{i}^{\text {nst }}$ are denoted as estimated voltage magnitude and angle of $i$ th bus, respectively.

The performance of the state estimator deteriorates due the presence of number of pseudo-measurements with high variances. However, the performance can be improved by deploying additional real meters at suitable locations. In this paper, the optimal number of VMMs and power flow meters has been considered for the design of measurement infrastructure of an active distribution system. For SE, branch current-based distribution system SE (BC-DSSE) algorithm is used for estimating the states of the system such as branch current magnitudes and their angles [23].

The following section of this paper describes the solution methodology for the above proposed multi-objective optimisation problem.

## 3 Solution methodology

For the solution of the multi-objective optimisation problem, a new hybrid EDA-IPM algorithm has been proposed in this paper. Therefore, in this section, a brief introduction to traditional EDA and interior point method (IPM) has been presented as follows.

### 3.1 Estimation of distribution algorithm

The EDA is a population-based evolutionary optimisation algorithm which employs a probabilistic model to generate new individuals for the next generation [24, 25]. It has efficient diversification capability to explore the search space to achieve prominent solutions for the optimisation problem.

In EDA, new solutions are generated without using crossover and mutation operators like in GA. A probabilistic model is estimated in order to sample the new individuals from the database containing previous generation data and some selected population. The movement of each individual in the population is predicted by the probability model used in EDA.

The pseudo-code of EDA is described as follows:

## Begin

1. Initialisation: Generate $R$ initial population randomly within limits.

## While termination criteria not met Do

2. Evaluation: Calculate the fitness value of $R$ individuals.
3. Selection: By using any selection method select $N<R$ individuals.
4. Probabilistic model: Estimate the probability $p_{n}(x)$ that an individual being among the selected population.
5. Sampling: Sample $R$ individuals from $p_{n}(x)$ using sampling technique.

## End while

## End

### 3.2 Interior point method

The primal-dual IPM is basically used to solve non-linear constraint optimisation problem [26]. The Lagrange multipliers are employed to deal with the equality and inequality constraints of the optimisation problem. In order to avoid the negativity conditions of the slack variables the logarithmic barrier functions are added to the objective function. In this method, the decision variables are considered to be continuous. The non-linear constraint optimisation problem can be transformed into an unconstraint optimisation problem of the following Lagrange function:

$$
\begin{aligned}
L\left(z, y, l, u, v, w\right) & =f(x)-v^{T}\left(x-l-x_{\min }\right)-y^{T} g(x) \\
& +w\left(x+u-x_{\max }\right)-p \sum_{i}\left(\ln l_{i}+\ln u_{i}\right)
\end{aligned}
$$

where $u$ and $l$ are the slack variables; $y, v$ and $w$ are the Lagrange multipliers; and the barrier parameter is represented by $\mu$.

In order to satisfy the Karush-Kuhn-Tucker (KKT) conditions, first-order derivatives of a set of non-linear algebraic equations have been formed and then Newton-Raphson method is employed to solve the above first-order differential equations [27, 28]. During the iterative procedure of the IPM, if the KKT conditions shown below are satisfied then the algorithm will stop. The KKT conditions are described as follows:

$$
\begin{gathered}
\left\|L_{n}\right\|=\left\|\nabla f(x)-\nabla g^{T}(x) y-v+w\right\|<\varepsilon \\
\left\|L_{p}\right\|=\|g(x)\|<\varepsilon \\
\left\|L_{w}\right\|=\left\|x+u-x_{\max }\right\| \leq \varepsilon \\
\left\|L_{v}\right\|=\left\|x-l-x_{\min }\right\| \leq \varepsilon
\end{gathered}
$$

According to primal-dual theory, $x$ is the primal variable, $l$ and $u$ are the slack variables, $y, v$ and $w$ are the dual variables, respectively. Equations (8)-(10) are called the primal feasible conditions and (7) is known as dual feasible conditions. If the solution satisfies the above conditions then it is an optimal solution for the optimisation problem.

### 3.3 Proposed multi-objective hybrid EDA-IPM algorithm

In this paper, the meter placement problem is formulated as multiobjective optimisation problem. The main advantage of using this approach is, a best compromised solution can be established between the various objectives described in Section 2. Simultaneously, the impacts of meter location on SE accuracy can be investigated. Therefore, a trade-off solution is essential between the objectives to reduce the cost and SE error. In order to achieve best compromised solution among the objectives, hybrid EDA-IPM algorithm has been proposed. The reason for this hybridisation of two algorithms is described as follows.

EDA has been used widely in a variety of engineering applications because of its efficient exploration capability in the search space. Although, EDA has good exploration ability but it
suffers from poor exploitation capability to get global optimal solution. However, the local searching capability of IPM algorithm is more effective. Therefore, the conventional EDA is hybridised with IPM to enhance the exploitation capability of the algorithm to get near global optimal solutions. The solution obtained from EDA is taken as inputs to IPM.

In multi-objective optimisation case if objective functions are conflicting in nature, then no solution can be improved itself in one objective without worsening the other objectives. Since the objectives are conflicting, non-dominated sorting principle has been incorporated to get the best optimal Pareto front [22]. All solutions in a non-dominated Pareto front are treated as best optimal solution. Thus, in this approach, the solution is not a single-optimal solution like single objective optimisation case rather it is a set of optimal solution. In this paper, non-dominated sorting approach has been employed with hybrid EDA-IPM algorithm to achieve best trade-off solutions between different objectives such as cost, ARPE in voltage magnitude and phase angle.

In the proposed algorithm, initially solutions are generated randomly using seeding approach within the search space. Each solution represents the number of power flow meters as well as their locations. Based on their location, the objective functions (1)(3) are evaluated using BC-DSSE algorithm [23]. Then, the selection mechanism has been used to select some of the best solutions obtained so far. These selected solutions are updated using an IPM algorithm to obtain best neighbourhood solution. After updating the selected solutions, probabilistic Bayesian model has been incorporated to predict the new solutions for future generation based on the selected solution. After evaluating the fitness, constraints violation checking has been carried out. To satisfy the constraints, Monte Carlo simulation is used and relative deviations in voltage magnitude and angle is determined at each bus for all Monte Carlo trials. In $95 \%$ of cases, if the relative errors are within the pre-specified limits, then that solution is stored for the next generation. On the other hand, if it is not, then a higher objective value is to be assigned to that solution so that this solution can be eliminated from the next generation. After that sampling technique is utilised. Then, this procedure is repeated till the convergence criterion is met. To get the best solution in optimal Pareto front, fuzzy theory [37] has been used.

In the optimisation process, different population sizes like 20, 30 and 50 have been tried. However, it has been found that there is no such significant variation in result for taking different population sizes for both the test system considered in this paper. Therefore, population size of 20 has been fixed for evaluating the performance of the proposed optimisation algorithm (Table 1). The flowchart of the proposed method has been shown in Fig. 1. Furthermore, the pseudo-code of the proposed multi-objective hybrid EDA-IPM algorithm has been presented as follows.

The steps of the proposed algorithm are shown in Fig. 2.

## 4 Simulation conditions and results discussion

To analyse the efficiency of the proposed SE formulation and algorithm, several test conditions and network operating scenarios have been considered in MATLAB 2014b environment. For SE in radial network, BC-DSSE algorithm has been employed. In BCDSSE, the magnitude of branch currents and their angles are treated as state variables [23]. In order to generate the measurement data for SE, first backward-forward sweep method has been used to obtain the load flow solution of a distribution network. This load flow solution is treated as the reference or actual values of the measured quantities. Then, the measurement data is generated by adding random noise following the Gaussian distribution to the actual values of the quantities obtained from the load flow solution. Mainly, there are four types of measurement data are considered in this paper for SE, such as substation measurements, real measurements, pseudo-measurements and virtual measurements [29]. The error associated with each type of measurement data is based on the maximum percentage of error assumed for that measurement. The following conditions are considered for the measurement uncertainties:

![img-0.jpeg](img-0.jpeg)

Fig. 1 Flowchart of the proposed multi-objective hybrid EDA-IPM algorithm
(i) Substation measurements: In this paper, it is assumed that only one flow meter at the first line and one VMM is present at the substation and maximum percentage of error associated with these measurements is $1 \%$. These measurements are called as default measurement.
(ii) Real measurements: Generally, the real measurements are more accurate. Therefore, the maximum error assumed for this is 1,3 and $5 \%$. The power flow meters are assumed as real meters and it measures both real and reactive power flows in a line.
(iii) Pseudo-measurements: Basically, the pseudo-measurements are obtained from the historical customer load data. Therefore, these measurements are less accurate than other types of measurements. The maximum percentage of error assumed for pseudo-measurements is $50 \%$ [29].
(iv) Virtual-measurements: The virtual measurements are obtained from the zero-injection buses and these measurements are highly accurate than other measurements with a variance value of $10^{-7}$ [30].

Furthermore, the load and generators are considered as stochastic variable to analyse the performance of the proposed meter placement scheme. Different measurement uncertainties for better analysis of the proposed technique have been considered. In
this paper, the load and generator outputs are stochastic in nature and it is assumed to be distributed normally around the mean value with fixed standard deviation. Moreover, the Monte Carlo trials have been utilised to study the effects of measurement uncertainties on SE performance. There are 100 number of different network operating conditions is generated. From each network operating condition, 1000 number of different network states is generated by using Monte Carlo simulation. Thus, in this simulation study, the total number of network scenarios considered is $100 \times 1000$. A standard deviation of $\pm 10 \%$ around the base value has been assumed for each operating condition. Different measurement uncertainties considered for real meters are 1,3 and $5 \%$, respectively.

The number of meters required and their locations in the presence of different types of DGs have also been investigated in this paper. Moreover, it is assumed that the locations of DGs are fixed $[31,32]$ and their output is a stochastic in nature. In this paper, various types of network scenarios such as meter placement impacts on passive as well as active distribution networks have been considered (Table 2). Further, the active network consists of DG only producing real power to the networks, DG producing real power as well as absorbing reactive power, and DG producing both real power as well as reactive power to the network. Since, the DG outputs are not controlled in this case so these are belongs to non-

The steps of the proposed algorithm are as follows:
Step1. Initialization: Generate random number of power flow meters and their locations for each individual in the population (Pop).
Do while ("Stopping criterion is not satisfied")
Step 2. Fitness evaluation: Evaluate the fitness functions for each individual in the Pop.
Step 3. Selection: Select $N<R$ solutions from Pop using Non-dominated sorting selection strategy. $R$ is the size of the population and $N$ is a number less than $R$.

## Begin

Do while ("Stopping criterion is not satisfied")
For $i=1: S_{\text {w/in }}$ (Number of selected solutions.)

1. Use each solution $i$ as initial point in IPM to find the best optimal solution for each $i$.
2. Evaluation: Calculate fitness value of $y(i)$ using weighting approach.
3. Update solution:
if Fitness $(y(i))<$ Fitness $(x(i))$
\&\& if solution y dominates $x$
then $x(i)=y(i)$
End for $i$
End Do
End
Step 4. Probabilistic graphical model: Estimate the probability distribution of the previous solutions and selected solution to predict new population for the next generation using Gaussian Bayesian network. Mathematically, it can be expressed as:

$$
p\left(x_{i} \mid p a\left(X_{i}\right)\right)=\mathrm{N}\left(\mu_{i}+\sum_{X_{j} \in P a\left(X_{i}\right)} w_{i j}\left(x_{j}-\mu_{j}\right), v_{i}^{2}\right)
$$

where $\mu_{i}$ represents the mean of the variable $X_{i}, v_{i}$ is the standard deviation of the distribution and $w_{i j}$ is the weight associated with each of the parents. $x_{j}$ is the value of the variable $X_{j}$ in $p a\left(X_{i}\right)$.
Step 5. Sampling technique: Sample $R$ number of solutions from the Gaussian Bayesian network using sample Gaussian UnivModel.
End Do
End
Fig. 2 Pseudo-code of the proposed multi-objective hybrid EDA-IPM algorithm
Table 1 Parameter values of PSO, NSGA-II and EDA algorithms
PSO population size $=20, C 1=2, C 2=2 W_{\max }=0.9, W_{\min }=0.4$ maximum number of generations $=50$
NSGA-II $\quad$ crossover rate $(P c)=0.8$, mutation rate $(M c)=0.02$, maximum number of generations $=50$ population size $=20$
EDA learning method: learn Gaussian Bayesian model, population size: 20sampling method: sample Gaussian Universal modelreplacement method: Pareto rank orderingselection method: non-dominated selectionrepairing method: set in bounds repairing

Table 2 DG installation bus and capacity

| Test system | Bus number | DG type and capacity (in MW) base value |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  |  | Type 1, $P$ | Type 2, $P-J Q$ | Type 3, $P+J Q$ |
| PG\&E 69-bus | 50 | 0.180 | $0.180 \div j 0.087$ | $0.180+j 0.087$ |
|  | 61 | 0.270 | $0.270 \div j 0.130$ | $0.270+j 0.130$ |
| Indian 85-bus | 45 | 0.277 | $0.235 \div j 0.145$ | $0.235+j 0.145$ |
|  | 61 | 0.290 | $0.246 \div j 0.152$ | $0.246+j 0.152$ |

dispatchable type. In the presence of these kinds of DGs, the meter placement impact on SE accuracy in a multi-objective environment has been discussed in this paper. The types of DG and their capacity are provided in Table 1.

The parameters used for particle swarm optimisation (PSO), non-dominated sorting GA (NSGA-II) and EDA are provided in Table 2. In PSO, the parameters used are inertia weight ( $W_{\max }, W_{\min }$ ) and the learning factors $C 1$ and $C 2$. The value of inertia weight decides the balance between exploration and exploitation capability

![img-1.jpeg](img-1.jpeg)

Fig. 3 Single-line diagram of PG\&E 69-bus system
Table 3 PG\&E 69-bus system: the number and location of the power flow meters of different meter accuracy (with no DG)

| Metrological errors, \% | Algorithm | location of flow meters (line number) | Number of flow meters | Objective functions value $F 1$ | $\begin{gathered} \text { Maximum } \\ \text { error in bus } \\ \text { voltage } \\ \text { magnitude } \\ (V), \% \end{gathered}$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | proposed <br> EDA-IPM | 1, 7, 24, 3, 51 | 5 | 6 | 0.0025 | 0.4821 | 0.0201 | 5.2137 |
|  | EDA | 1, 11, 17, 23, 41, 47, 56 | 7 | 8 | 0.0081 | 1.3421 | 0.0318 | 6.9784 |
|  | PSO | 1, 10,21, 27, 30, 32, 33, 49, 67 | 9 | 10 | 0.0053 | 0.8985 | 0.0375 | 8.4249 |
|  | NSGA-II | 1, 5, 17, 20, 25, 56, 67 | 7 | 8 | 0.0060 | 0.9352 | 0.0272 | 9.2313 |
|  | DP [16] | 1, 11, 18, 33, 41, 57 | 6 | 7 | 0.0042 | 0.7861 | 0.0212 | 8.1321 |
|  | OOA [17] | 1, 9, 17, 29, 42, 51, 57 | 7 | 8 | 0.0051 | 0.9292 | 0.0245 | 7.7547 |
| 3 | proposed <br> EDA-IPM | 1, 11, 19, 43, 52 | 5 | 6 | 0.0051 | 0.9657 | 0.0317 | 5.7321 |
|  | EDA | 1, 9, 17, 23, 29, 36, 44, 57 | 8 | 9 | 0.0072 | 1.2950 | 0.0475 | 7.9238 |
|  | PSO | 1, 4, 37, 39, 44, 49, 54, 58, 68 | 9 | 10 | 0.0102 | 1.9119 | 0.0338 | 10.7899 |
|  | NSGA-II | 1, 3, 4, 14, 17, 21, 43, 47, 48, 53, | 13 | 14 | 0.0063 | 1.3083 | 0.0434 | 9.9812 |
|  |  | 57, 61, 63 |  |  |  |  |  |  |
|  | DP [16] | 1, 7, 16, 23, 37, 41, 47, 58, | 8 | 9 | 0.0089 | 1.1123 | 0.0527 | 10.2333 |
|  | OOA [17] | 1, 9, 19, 33, 42, 49, 56, 63 | 8 | 9 | 0.0090 | 1.7123 | 0.0503 | 8.7230 |
| 5 | proposed <br> EDA-IPM | 1, 7, 14, 19, 28, 33, 47, 53, 61 | 9 | 10 | 0.0056 | 1.1273 | 0.0513 | 6.2379 |
|  | EDA | 1, 11, 19, 26, 33, 39, 44, | 12 | 13 | 0.0055 | 1.1289 | 0.07543 | 9.3417 |
|  |  | 47,53,57,61,65 |  |  |  |  |  |  |
|  | PSO | 1, 2, 11, 17, 18, 28, 32, 40, 45, 47, | 14 | 15 | 0.0074 | 1.7642 | 0.0538 | 13.2314 |
|  |  | 51, 57, 66, 67 |  |  |  |  |  |  |
|  | NSGA-II | 1, 4, 13, 14, 16, 25, 30, 3, 45, 56, | 12 | 13 | 0.0078 | 1.7876 | 0.0673 | 12.2324 |
|  |  | 63, 66 |  |  |  |  |  |  |
|  | DP [16] | 1, 7, 16, 29, 34, 46, 53, 59, 61,65 | 10 | 11 | 0.01512 | 1.8727 | 0.0644 | 11.1523 |
|  | OOA [17] | 1, 11, 17, 26, 31, 39, 47, 53, 58, 63 | 10 | 11 | 0.0223 | 1.7821 | 0.0604 | 9.2313 |

of the PSO algorithm. It is found that the best performance is obtained by setting $w$ initially to some relatively high value (e.g. 0.9 ) to perform extensive exploration in the search space. When $w$ is reduced gradually to a lower value (e.g. 0.4 ), the system becomes more dissipative and exploitative. This will improve the local searching capability of the algorithm. Therefore, the appropriate values of $W_{\text {max }}$ and $W_{\text {min }}$ chosen is 0.9 and 0.4 , respectively [33-36]. Furthermore, the parameters $C 1$ and $C 2$ represent the speed of flying of particles to the most optimise position of the swarm in the search space and its own best position. It regulates the length and time taken by particle to reach most optimum position. So that, the particle land in an appropriate position. For example, if too big a value of acceleration constants is selected, then the particle may fly past the appropriate position and for too small value, the particle will not be able to reach the target position. Generally, each of these constants is set to 2 to make the times taken to move towards the particle's personal best and swarm's global best as equal. Similarly, the parameters chosen for NSGA-II and EDA are shown in Table 1.

### 4.1 PG\&E 69-bus system

The performance of the proposed algorithm has been investigated on standard PG\&E 69-bus, 12.66 kV radial distribution network. This network consists of 69 buses, 68 lines along with 48 loads and DGs at bus numbers 50 and 61 . The system line and load data are taken from [38]. The total load of the system is 3.802 MW and 2.692 Mvar, respectively. The single-line diagram of the network is shown in Fig. 3. In this system, there are 21 number of zero injection buses. The virtual measurements are obtained from these zero injection buses. One VMM and a power flow meter are kept at the substation, which are treated as default meters.

From the simulation result, it is observed that when the meter accuracy is $1 \%$, the number of flow meters needed is 5 using the proposed hybrid EDA-IPM algorithm. On the other hand, the number of power flow meters required is 7,9 and 7 using EDA, PSO and NSGA-II, respectively. In case of DP and OOA, the number of meter requirements is 6 and 7. In Table 3, the ARPE of voltage magnitude and phase angle is specified. It is observed that ARPE of voltage magnitude and angle using proposed hybrid EDA-IPM algorithm is 0.0025 and $0.4821 \%$. In case of EDA and PSO these are $0.0081,1.3421 \%$ and $0.0053,0.8985 \%$ and using

![img-2.jpeg](img-2.jpeg)

Fig. 4 Optimal Pareto front between
(a) Objectives $F 3$ and $F 2$ ( $1 \%$ error in real and $50 \%$ in pseudo-measurements), (b) Number of flow meters and $F 2$ ( $1 \%$ error in real and $50 \%$ in pseudo-measurements),

NSGA-II it is 0.0060 and $0.9352 \%$, respectively. The optimal Pareto front of all the algorithms is shown in Fig. 4 when the meter accuracy is $1 \%$. Among all the solution in the Pareto front, the best optimal solution is selected by using fuzzy theory [36]. Furthermore, the results are compared with some existing techniques in the literature such as DP and OOA. From the observation, it is found that the proposed method is more superior to the other existing methods discussed in the literature. Because the existing techniques are following step-by-step approach. The obtained results using DP and OOA are also reported in Table 3 which shows the effectiveness of the proposed EDA-IPM algorithm over other algorithms and techniques considered in this paper. Moreover, the maximum relative percentage error using different methods in voltage and angle estimates are also presented in Table 3. It is worth noticing that the maximum deviations in state variables using the proposed algorithm are significantly lower than using PSO, EDA, NSGA-II, DP and OOA.

The optimal Pareto-front for meter accuracy of 3 and $5 \%$ between different objectives has also been shown in Figs. 5 and 6. In this case, the objectives $F_{2}$ and $F_{3}$ values are little higher than $1 \%$ case because meter error considered is higher than $1 \%$. It is observed that if the errors are more in direct measurements then its impacts on the SE accuracy is significant and also meters requirement is more. Moreover, it is worth noticing that the impact
of measurement uncertainties and meter locations on state estimator performance is more significant. In Table 3, it is seen that, for both EDA and OOA cases, the total number of power flow meters required is same, i.e. 7 but the SE accuracy value is different due to meters locations are not same. Fig. 4 shows the optimal Pareto-front between $F_{2}$ and $F_{3}$. It is observed that $F_{2}$ and $F_{3}$ are correlated to each other. Thus, the optimal Pareto is not established between the two objectives.

The results shown in Table 3 refer to a passive distribution network. From these two observations can be made, first as the accuracy of the meters decreases the number of power flow meters needed is more for better SE performance. Second, the efficiency of the proposed hybrid EDA-IPM algorithm is found to be better due to its higher degree of balance between the exploration and exploitation capability. This results in efficient searching ability of the proposed algorithm in the search space. Thus, a new hybrid EDA-IPM algorithm has been employed for the distribution SE in multi-objective framework to resolve the meter placement issues. The results obtained using PSO, EDA, NSGA-II, DP and OOA are compared with the proposed algorithm to test it's the efficiency.

Furthermore, the proposed methodology has also been tested in the presence of DG. There are different kinds of DGs considered in this paper are provided in Table 2. Two DGs of type 1 are installed at bus numbers 50 and 61 . To get minimum power loss and voltage

![img-3.jpeg](img-3.jpeg)

Fig. 5 Optimal Pareto front between
(a) Number of flow meters, (b) Number of flow meters and $F 3$ ( $3 \%$ error in real and $50 \%$ in pseudo-measurements) meters and $F 2$ ( $3 \%$ error in real and $50 \%$ in pseudomeasurements)
![img-4.jpeg](img-4.jpeg)

Fig. 6 Optimal Pareto front between
(a) Number of flow meters and $F 2$ ( $5 \%$ error in real and $50 \%$ in pseudo-measurements), (b) Number of flow meters and $F 3$ ( $5 \%$ error in real and $50 \%$ in pseudo-measurements)
deviation, the two DGs are placed at these buses. The obtained results are provided in Table 4. It is observed that, there is a reduction in the number of power flow meter requirement as compared to passive case. The phase angle error is also reduced. The reason is, DG provides power to the local bus. Therefore, the real power drawn by that load from the feeder section is reduced, i.e. the magnitude of current in the lines will go down. As a result, the magnitude of error associated with power flow measurements will get reduce. Moreover, due to the presence of DGs, the redundancy level of measurement is increased which helps to improve the accuracy of the estimator to a further extent. The presence of types 2 and 3 DG has been studied and the results obtained are provided in Table 5. It is observed that, in all the cases, the proposed algorithm outperforms all other algorithms used in this paper. In case of types 2 and 3 DGs, it is assumed that the DGs are generating both real and reactive power to the network. In one case DG supplying reactive power and in other case it is absorbing reactive power from the network.

### 4.2 Indian 85-bus system

To investigate the performance of the proposed algorithm, in practical distribution network, Indian 85 -bus, 11 kV radial distribution system has been taken into consideration. This system consists of 85 nodes and 84 number of lines. The total load of the system is 2.574 MW and 2.622 MVar , respectively. This system consists of 21 number of zero injection buses and the single-line diagram of the system is shown in Fig. 7. The network line and load data are obtained from [39]. Furthermore, the parameters of the algorithms specified in Table 1, can also be applicable for this test system.

The results obtained for this system are reported in Table 6. It is seen that when meter error is $1 \%$ and pseudo-measurement error is $50 \%$, the number of meters required is 7 by using proposed hybrid EDA-IPM algorithm, whereas in case of PSO, EDA and NSGA-II,
the number of meters required is 8,8 and 9 , respectively. The corresponding objective functions value is also provided in Table 6. The optimal Pareto-front curve between the objectives is shown in Figs. 8-10, for different measurement uncertainties of the power flow meters. It is noticed that if meter accuracy is decreased from 1 to $3 \%$ or $5 \%$, then the network needs more number of meters to improve the quality of SE. Therefore, more real meters are employed to bring down the relative errors in voltage and angle estimates below the pre-specified thresholds. The results obtained using DP and OOA have also been compared with the proposed hybrid EDA-IPM algorithm and it is provided in Table 6.

The performance of the proposed algorithm in the presence of different kinds of DGs at bus numbers 45 and 61 has also been tested. The results obtained using types 1, 2 and 3 DGs are provided in Tables $6-8$, respectively. From the results shown in Tables 6-8, the impact of different types of DGs on SE accuracy is clearly visualised. In case of type 1 DG , the phase angle error is reduced to a great extent because of DG supplies only real power to the local loads where it is connected. Therefore, the magnitude of power flow in the main feeder section is getting reduced. Table 7 represents the results obtained using the proposed hybrid EDAIPM algorithm. From the results reported in Tables 6-8, it is observed that both the location and measurement uncertainties significantly affecting the SE accuracy. The results obtained using DG types 2 and 3 are also reported in Tables 7 and 8, respectively. The main motive of using this Pareto-based multi-objective optimisation technique is to obtain a best compromised solution between the objectives such as relative percentage error in voltage magnitude and angle with respect to the total cost of meter.

## 5 Conclusion

This paper proposed a Pareto-based multi-objective optimisation technique that optimises the number and location of measuring devices for SE in smart distribution network. To find the optimal

Table 4 PG\&E 69-bus system: the number and location of the power flow meters of different meter accuracy (type 1 DG at buses 50 and 61)

| Metrological errors, \% | Algorithm | Location of flow meters (line number) | Number of flow meters | Objective functions value |  |  | Maximum error in bus voltage magnitude ( $V$ ), $\%$ | Maximum error in bus voltage angle $(\delta), \%$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  | $F 1$ | $F 2$ | F3 |  |  |
| 1 | proposed EDAIPM | 1, 49, 52, 60, 68 | 5 | 8 | 0.0018 | 0.3125 | 0.0130 | 5.2983 |
|  | EDA | 1, 28, 33, 37, 51, 62 | 6 | 9 | 0.0063 | 1.1021 | 0.0200 | 9.1936 |
|  | PSO | 1, 13, 24, 27, 30, 33, 49, 67 | 8 | 11 | 0.0047 | 0.7985 | 0.0347 | 7.9243 |
|  | NSGA-II | 1, 7, 19, 29, 34, 59, 67 | 7 | 10 | 0.0062 | 0.8152 | 0.0278 | 9.2713 |
|  | DP [16] | 1, 23, 38, 49, 51, 63 | 6 | 10 | 0.0037 | 0.7146 | 0.0272 | 8.2726 |
|  | OOA [17] | 1, 16, 27, 33, 39, 52, 61, 63 | 8 | 11 | 0.0049 | 0.9127 | 0.0321 | 7.1634 |
| 3 | proposed EDAIPM | 1, 19, 23, 29, 53 | 5 | 8 | 0.0043 | 0.8357 | 0.0204 | 6.0125 |
|  | EDA | 1, 5, 11, 19, 24, 33, 41, 44, 49, 51, 65, 67 | 7 | 10 | 0.0068 | 1.1027 | 0.0321 | 10.2773 |
|  | PSO | 1, 7, 17, 39, 41, 49, 57, 59, 63 | 9 | 12 | 0.0110 | 1.3411 | 0.0438 | 10.1324 |
|  | NSGA-II | 1, 5, 9, 15, 19, 28, 49, 57, 59, 61, 63 | 11 | 14 | 0.0049 | 1.0830 | 0.0374 | 9.1119 |
|  | DP [16] | 1, 6, 19, 28, 39, 47, 51, 57 | 8 | 11 | 0.0057 | 1.3782 | 0.0511 | 9.8975 |
|  | OOA [17] | 1, 7, 17, 28, 39, 46, 57, 62 | 8 | 11 | 0.0062 | 1.3452 | 0.0611 | 7.2451 |
| 5 | proposed EDAIPM | 1, 3, 17, 24, 33, 41, 50, 63 | 9 | 12 | 0.0051 | 1.1122 | 0.0230 | 6.9124 |
|  | EDA | 1, 4, 24, 36, 47, 54, 63, 64, 67 | 11 | 14 | 0.0049 | 1.1113 | 0.0319 | 10.0087 |
|  | PSO | 1, 7, 15, 17, 26, 37, 43, 45, 49, $51,58,62,65$ | 14 | 17 | 0.0072 | 1.0642 | 0.0317 | 13.9342 |
|  | NSGA-II | 1, 6, 9, 11, 15, 20, 22, 41, 54, 63, 65 | 11 | 14 | 0.0120 | 1.1834 | 0.0713 | 11.9807 |
|  | DP [16] | 1, 11, 14, 23, 37, 44, 59, 63, 67 | 9 | 12 | 0.0238 | 1.6345 | 0.0630 | 11.7981 |
|  | OOA [17] | 1, 11, 19, 26, 31, 39, 49, 52, 61, 63 | 10 | 13 | 0.0321 | 1.7952 | 0.0548 | 10.2398 |

Table 5 PG\&E 69-bus system: the number and location of the power flow meters of $1 \%$ accuracy (types 2 and 3 DGs at buses 50 and 61 )

| DG type | Algorithm | Location of flow meters (line number) | Number of power flow meters | Objective functions value |  |  | Maximum error in bus voltage angle $(\delta), \%$ | Maximum error in bus voltage angle $(\delta), \%$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  | $F 1$ | $F 2$ | F3 |  |  |
| Type 2 ( $P-j Q$ ) | proposed EDA-IPM | 1, 5, 24, 37, 42 | 5 | 8 | 0.0069 | 1.1807 | 0.0291 | 5.8912 |
|  | EDA | 1, 4, 14, 61, 65, 66 | 6 | 9 | 0.0086 | 1.6091 | 0.0314 | 6.3732 |
|  | PSO | 1, 2, 4, 14, 28, 43, 51, 68 | 8 | 11 | 0.0098 | 1.8356 | 0.0377 | 6.8123 |
|  | NSGA-II | 1, 5, 30, 39, 44, 58 | 6 | 9 | 0.0097 | 1.8651 | 0.0299 | 5.9927 |
|  | DP [16] | 1, 7, 15, 41, 56, 66 | 6 | 9 | 0.0085 | 1.6614 | 0.0524 | 6.7241 |
|  | OOA [17] | 1, 5, 13, 14, 20, 43, 54, 56, 57 | 9 | 12 | 0.0088 | 1.6137 | 0.0454 | 6.6634 |
| Type 3 ( $P+j Q$ ) | proposed EDAIPM | 1, 11, 32, 45, 51 | 5 | 8 | 0.0067 | 0.9864 | 0.0326 | 5.6734 |
|  | EDA | 1, 13, 34, 49, 51, 52, 60 | 7 | 10 | 0.0096 | 1.5240 | 0.0541 | 6.3422 |
|  | PSO | 1, 8, 9, 25, 35, 45, 49, 55 | 8 | 11 | 0.0098 | 1.4713 | 0.0491 | 6.4532 |
|  | NSGA-II | 1, 11, 32, 50, 51, 54, 60 | 7 | 10 | 0.0106 | 1.6617 | 0.0613 | 6.2459 |
|  | DP [16] | 1, 25, 31, 38, 65, 67, 68 | 7 | 10 | 0.0115 | 1.7095 | 0.0527 | 7.1134 |
|  | OOA [17] | 1, 6, 10, 19, 35, 45, 63, 64 | 8 | 11 | 0.0094 | 1.4584 | 0.0612 | 6.5980 |

placement of meters a new hybrid EDA-IPM algorithm has been proposed. The hybridisation of traditional EDA with IPM is done to improve the local searching capability of the EDA. In SE metrological characteristics of meters as well as the load variations has also taken into consideration to test the efficiency of the proposed meter placement technique. The best optimal trade-off solution between the objective functions such as cost and SE error is established. Moreover, the impact of different kinds of DGs on SE accuracy has also been presented in an active distribution network.

The proposed hybrid EDA-IPM algorithm-based meter placement technique is tested on PG\&E 69-bus system and practical Indian 85-bus distribution network. The obtained result using the proposed hybrid EDA-IPM algorithm has been compared with some existing algorithm in the literature such as PSO, EDA, NSGA-II, DP and OOA under various operating conditions of the distribution systems. It is reported that the proposed algorithm is robust, reliable and more superior than existing algorithms considered in this paper. Hence the proposed hybrid algorithmbased meter placement technique can be utilised for the planning study of the distribution networks.

![img-5.jpeg](img-5.jpeg)

Fig. 7 Single-line diagram of Indian 83-bus radial distribution network
Table 6 Indian 85-bus system: the number and location of the power flow meters of different meter accuracy (with no DG)

| Metrological errors, \% | Algorithm | Location of flow meters (line number) | Number of flow meters | Objective functions value $F 1$ | $\begin{gathered} \text { Gl | Maximum error in bus voltage magnitude (V), } \\ \% \end{gathered}$ | Maximum error in bus voltage angle $(\delta), \%$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | proposed EDA-IPM | 1, 13, 19, 25, 75, 78,84 | 7 | 8 | 0.0383 | 1.0952 | 0.1692 | 5.0660 |
|  | EDA | 1, 30, 32, 35, 36, 42, 43, 60, 68 | 8 | 9 | 0.0387 | 1.2323 | 0.2797 | 6.4132 |
|  | PSO | 1, 30, 32, 35, 36, 42, 43, 60, 68 | 8 | 9 | 0.0407 | 1.4739 | 0.2593 | 6.6143 |
|  | NSGA-II | 1, 16, 34, 37, 40, 42, 43, 50, 55 | 9 | 10 | 0.0411 | 1.4289 | 0.2897 | 7.7394 |
|  | DP [16] | 1, 13, 21, 32, 37, 47, 51, 54 | 8 | 9 | 0.0444 | 1.5213 | 0.2111 | 8.6072 |
|  | OOA [17] | 1, 9,16, 43, 62, 69, 70, 72, 76 | 9 | 10 | 0.0579 | 1.2356 | 0.2871 | 7.7322 |
| 3 | proposed EDAIPM | 1, 34, 40, 46, 52, 53, 67, 69 | 8 | 9 | 0.0427 | 1.0433 | 0.2117 | 5.2305 |
|  | EDA | 1, 28, 42, 52, 53, 58, 71, 74 | 8 | 9 | 0.0431 | 1.2486 | 0.3984 | 6.0022 |
|  | PSO | 1, 15, 18, 20, 23, 39, 45, 50, 77 | 11 | 12 | 0.0468 | 1.5478 | 0.3041 | 7.1198 |
|  | NSGA-II | 1, 10, 15, 17, 26, 42, 58, 70, 71, $74,26,84$ | 8 | 9 | 0.0438 | 1.3478 | 0.2999 | 9.9812 |
|  | DP [16] | 1, 11, 23, 29, 36, 45, 57, 59, 63, 67 | 10 | 11 | 0.0431 | 1.5888 | 0.2876 | 7.9811 |
|  | OOA [17] | 1, 33, 37, 41, 53, 60, 65, 80, 83 | 9 | 10 | 0.0735 | 1.5870 | 0.2987 | 7.3724 |
| 5 | proposed EDA-IPM | 1, 12, 20, 43, 50, 68, 75, 83 | 8 | 9 | 0.0452 | 1.4298 | 0.2896 | 5.4821 |
|  | EDA | 1, 9, 17, 23, 37, 53, 61, 67, 73 | 9 | 10 | 0.0464 | 1.5088 | 0.3342 | 6.7623 |
|  | PSO | 1, 17, 19, 20, 30, 40, 43, 49, 58, $66,71$ | 8 | 9 | 0.0461 | 1.4893 | 0.3211 | 8.3421 |
|  | NSGA-II | 1, 6, 21, 32, 68, 69, 70, 76 | 12 | 13 | 0.0482 | 1.5740 | 0.2898 | 8.4359 |
|  | DP [16] | 1, 7, 14, 19, 33, 39, 42, 48, 53, 59, 61 | 11 | 12 | 0.0518 | 1.6239 | 0.3011 | 8.1312 |
|  | OOA [17] | 1, 18, 21, 23, 34, 36, 37, 61, 63, $75,76$ | 11 | 12 | 0.0466 | 1.3689 | 0.3362 | 7.5843 |

![img-6.jpeg](img-6.jpeg)

Fig. 8 Optimal Pareto front between
(a) Number of flow meters and $F 2$ ( $1 \%$ error in real and $50 \%$ in pseudo-measurements), (b) Number of flow meters and $F 3$ ( $1 \%$ error in real and $50 \%$ in pseudo-measurements)
![img-7.jpeg](img-7.jpeg)

Fig. 9 Optimal Pareto front between
(a) Number of flow meters and $F 2$ ( $3 \%$ error in real and $50 \%$ in pseudo-measurements), (b) Number of flow meters and $F 3$ ( $3 \%$ error in real and $50 \%$ in pseudo-measurements)
![img-8.jpeg](img-8.jpeg)

Fig. 10 Optimal Pareto front between
(a) Number of flow meters and $F 2$ ( $5 \%$ error in real and $50 \%$ in pseudo-measurements), (b) Number of flow meters and $F 3$ ( $5 \%$ error in real and $50 \%$ in pseudo-measurements)

Table 7 Indian 85-bus system: the number and location of the power flow meters of different meter accuracy (type 1 DG at buses 45 and 61)

| Metrological errors, \% | Algorithm | Location of flow meters (line number) | Number of power flow meters | Objective functions value $F 1$ |  | Maximum error in bus voltage magnitude ( $V$ ), \% | Maximum error in bus voltage angle $(\delta), \%$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | proposed EDA-IPM | $1,9,23,28,44$ | 5 | 8 | 0.0367 | 1.0473 | 0.1423 | 5.0237 |
|  | EDA | $1,8,21,32,68,69,76$ | 7 | 10 | 0.0574 | 1.0585 | 0.2427 | 5.9823 |
|  | PSO | $1,25,39,55,65,73$ | 6 | 9 | 0.0583 | 1.3910 | 0.2137 | 5.1242 |
|  | NSGA-II | $1,16,30,33,44,51,68,73$ | 8 | 11 | 0.0575 | 1.1165 | 0.1998 | 6.1123 |
|  | DP [16] | $1,10,33,46,58,63,71,77,79$ | 9 | 12 | 0.0580 | 1.0967 | 0.2514 | 6.0758 |
|  | OOA [17] | $1,11,14,16,32,42,54,70$ | 8 | 11 | 0.0574 | 1.0841 | 0.1667 | 5.3879 |
| 3 | proposed EDAIPM | $1,11,37,51,79,84$ | 6 | 9 | 0.0333 | 1.0372 | 0.2073 | 5.3241 |
|  | EDA | $1,26,32,57,64,71,79$ | 7 | 10 | 0.0636 | 1.0223 | 0.3231 | 6.1226 |
|  | PSO | $1,23,26,36,43,55,83$ | 7 | 10 | 0.0644 | 1.2166 | 0.2981 | 6.8799 |
|  | NSGA-II | $1,23,26,36,43,55,83$ | 7 | 10 | 0.0646 | 1.2105 | 0.2861 | 7.1981 |
|  | DP [16] | $1,13,27,30,34,41,55,56,68$, 82 | 10 | 13 | 0.0637 | 1.1480 | 0.3215 | 6.9122 |
|  | OOA [17] | $1,16,20,26,42,45,49,75,83$ | 9 | 12 | 0.0646 | 1.2364 | 0.3724 | 5.3523 |
| 5 | proposed EDAIPM | $1,9,17,28,42,62,79$ | 7 | 10 | 0.0400 | 1.1001 | 0.2441 | 5.5134 |
|  | EDA | $1,14,33,37,41,65,83,84$ | 8 | 11 | 0.0696 | 1.4032 | 0.3244 | 6.5312 |
|  | PSO | $1,11,19,28,42,51,57,71,79$ | 9 | 12 | 0.0589 | 1.3891 | 0.4523 | 7.2213 |
|  | NSGA-II | $1,13,14,17,20,42,44,54,56$, 57 | 10 | 13 | 0.0661 | 1.3588 | 0.4129 | 7.4512 |
|  | DP [16] | $1,14,15,18,22,27,47,54,72$ | 9 | 12 | 0.6683 | 1.3053 | 0.3871 | 6.3123 |
|  | OOA [17] | $1,31,46,48,58,62,65,67,77$, 78 | 10 | 13 | 0.6742 | 1.3053 | 0.4519 | 7.0784 |

Table 8 Indian 85-bus system: the number and location of the power flow meters of $1 \%$ accuracy (types 2 and 3 DGs at buses 45 and 61 )

| DG type | Algorithm | Location of flow meters (line number) | Number of power flow meters | Objective functions value $F 2$ |  | Maximum error in bus voltage magnitude ( $V$ ), \% | Maximum error in bus voltage angle $(\delta), \%$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Type 2 (P-jQ) | proposed EDA-IPM | $1,17,25,29,34,58,80$ | 7 | 10 | 0.0386 | 1.1584 | 0.2741 | 5.4671 |
|  | EDA | $1,14,21,26,56,65,75,84$ | 8 | 11 | 0.0388 | 1.3619 | 0.4714 | 5.7417 |
|  | PSO | $1,11,12,17,20,27,41,71,74$ | 9 | 12 | 0.0396 | 1.2677 | 0.3939 | 5.9923 |
|  | NSGA-II | $1,17,20,24,27,37,68,69$ | 8 | 11 | 0.0395 | 1.3121 | 0.3428 | 6.1798 |
|  | DP [16] | $1,23,30,37,40,62,75$ | 7 | 10 | 0.0408 | 1.3911 | 0.4239 | 6.7547 |
|  | OOA [17] | $1,3,9,14,20,52,54,62,69$ | 9 | 12 | 0.0387 | 1.2929 | 0.4118 | 5.9986 |
| Type 3 ( $P+j Q$ ) | proposed EDAIPM | $1,23,31,49,58,59,61$ | 7 | 10 | 0.0500 | 1.1191 | 0.2998 | 5.7326 |
|  | EDA | $1,28,31,50,68,79$ | 6 | 9 | 0.0686 | 2.1611 | 0.3887 | 5.9679 |
|  | PSO | $1,14,33,37,41,65,83,84$ | 8 | 11 | 0.0525 | 1.3306 | 0.3924 | 6.8324 |
|  | NSGA-II | $1,10,13,26,48,60,73,74,80$, 82 | 10 | 13 | 0.0506 | 1.1375 | 0.4713 | 6.9813 |
|  | DP [16] | $1,18,25,35,66,70,76,82$ | 8 | 11 | 0.0513 | 1.2059 | 0.4327 | 7.1112 |
|  | OOA [17] | $1,14,33,37,41,65,83,84$ | 8 | 11 | 0.0534 | 1.3162 | 0.3895 | 6.8756 |

## 6 References

[1] Haughton, D.A., Heydt, G.T.: 'A linear state estimation formulation for smart distribution systems', IEEE Trans. Power Syst., 2013, 28, (2), pp. 1187-1195
[2] Sheng, W., Liu, K., Cheng, S.: 'Optimal power flow algorithm and analysis in distribution system considering distributed generation', IET Gener. Transm. Distrib., 2014, 8, (2), pp. 261-272
[3] Roytchnan, J., Shahidehpoor, S.: 'State estimation for electric power distribution systems in quasi real-time conditions', IEEE Trans. Power Deliv., 1993, 8, (4), pp. 2889-2013
[4] Lu, C.N., Teng, I.H., Liu, W.H.E.: 'Distribution system state estimation', IEEE Trans. Power Syst., 1995, 10, (1), pp. 229-240
[5] Li, K.: 'State estimation for power distribution system and measurement impacts', IEEE Trans. Power Syst., 1996, 11, (2), pp. 911-916
[6] Baran, M.E., Kelly, A.W.: 'A branch current based state estimation method for distribution system', IEEE Trans. Power Syst., 2004, 10, (1), pp. 207-213
[7] Saric, A.T., Ciric, R.M.: 'Integrated fuzzy state estimation and load flow analysis in distribution networks', IEEE Trans. Power Syst., 2003, 18, (2), pp. 571-578
[8] Pau, M., Pegoraro, P.A., Sulis, S.: 'Efficient branch-current-based distribution system state estimation including synchronized measurement', IEEE Trans. Instrum. Meas., 2013, 62, (9), pp. 2419-2429
[9] Baran, M., Zhu, J, Kelly, A.: 'Meter placement for real time monitoring of distribution feeders', IEEE Trans. Power Syst., 1996, 11, (1), pp. 332-337
[10] Muscas, C., Pilo, F., Pisano, G., et al.: 'Optimal allocation of multichannel measurement devices for distribution state estimation', IEEE Trans. Instrum. Meas., 2009, 58, (6), pp. 1929-1937
[11] Chen, X., Lin, J., Wan, C., et al.: 'Optimal meter placement for distribution network state estimation: a circuit representation based MILP approach', IEEE Trans. Power Syst., 2016, 31, (6), pp. 4357-4370

[12] Liu, J., Tang, J., Ponci, F., et al.: 'Trade-offs in PMU deployment for state estimation in active distribution grids', IEEE Trans. Smart Grid, 2012, 3, (2), pp. $915-924$
[13] Pegoraro, P.A., Tang, J., Liu, J., et al.: 'PMU and smart metering deployment for state estimation in active distribution grids'. 2nd IEEE Energy Conf., 2012, pp. 873 - 878
[14] Liu, J., Ponci, F., Monti, A., et al.: 'Optimal meter placement for robust measurement systems in active distribution grids', IEEE Trans. Instrum. Meas., 2014, 63, (5), pp. 1096-1105
[15] Akhlaghi, S., Zhou, N., Wu, N.E.: 'PMU placement for state estimation considering measurement redundancy and controlled islanding'. IEEE Power Engineering Society General Meeting, Boston, MA, USA, 2016, pp. 1-5
[16] Damavandi, M.G., Krishnamurthy, V., Marti, J.R.: 'Robust meter placement for state estimation in active distribution systems', IEEE Trans. Smart Grid, 2015, 6, (4), pp. 1972-1982
[17] Pegoraro, P.A., Sulis, S.: 'Robustness-oriented meter placement for distribution system state estimation in presence of network parameter uncertainty', IEEE Trans. Instrum. Meas., 2013, 62, (5), pp. 954-962
[18] Sing, R., Pal, B.C., Jahr, R.A., et al.: 'Meter placement for distribution system state estimation: an ordinal optimization approach', IEEE Trans. Power Syst., 2011, 26, (4), pp. 2328-2335
[19] Shafin, A., Jenkins, N., Sirtue, G.: 'Measurement location for state estimation of distribution networks with generation', IEE Proc.-Gener. Transm. Distrib., 2005, 152, (2), pp. 240-246
[20] Sing, R., Pal, B.C., Vinter, R.B.: 'Measurement placement in distribution system state estimation', IEEE Trans. Power Syst., 2009, 24, (2), pp. 668-675
[21] Deb, K.: 'Multi-objective optimization using evolutionary algorithms' (Wiley India Pvt. Ltd, New Delhi)
[22] Deb, K., Pratap, A., Agarwal, S., et al.: 'A fast and elitist multi-objective generic algorithm: NSGA-II', IEEE Trans. Evol. Comput., 2002, 6, (2), pp. $182-197$
[23] Wang, H., Schulz, N.N.: 'A revised branch current-based distribution system state estimation algorithm and meter placement impacts', IEEE Trans. Power Syst., 2004, 19, (1), pp. 207-213
[24] Shim, V.A., Tan, K.C., Cheong, C.Y.: 'A hybrid estimation of distribution algorithm with decomposition for solving the multi-objective multiple traveling salesman problems', IEEE Trans. Syst. Man Cybern. C, Appl. Rev., 2012, 42, (5), pp. 682-691
[25] Karsthenas, H., Santana, R., Larrangua, P.: 'Multi-objective estimation of distribution algorithm based on joint modeling of objectives and variables', IEEE Trans. Evol. Comput., 2014, 18, (4), pp. 519-542
[26] Yan, W., Liu, F., Chung, C.Y., et al.: 'A hybrid genetic algorithm-interior point method for optimal reactive power flow', IEEE Trans. Power Syst., 2006, 21, (3), pp. 1163-1169
[27] Wang, Y., Jiang, Q.: 'Reactive power optimization of distribution network based on primal dual interior point method and simplified branch and bound method'. IEEE PES T\&D Conf. and Exposition, 2004, pp. 1-4
[28] Minot, A., Lu, Y.M., Li, N.: 'A parallel primal-dual interior-point method for DC optimal power flow'. 2016 Power Systems Computation Conf. (PSCC), Genoa, 2016, pp. 1-7
[29] Sing, R., Pal, B.C., Jahr, R.A.: 'Choice of estimator for distribution system state estimation', IET Gener. Transm. Distrib., 2008, 3, (7), pp. 666-678
[30] Lin, W.M., Teng, J.H.: 'State estimation for distribution systems with zeroinjection constraints', IEEE Trans. Power Syst., 1996, 11, (1), pp. 518-524
[31] Avandin, B., Hooshemand, R., Gholspour, E.: 'Decreasing activity cost of a distribution system company, by reconfiguration and power generation control of DGs based on shuffled frog leaping algorithm', Int. J. Electr. Power Energy Syst., 2014, 61, pp. 48-55
[32] Lakshmi, G.V.N., Jaya Laxmi, A., Reddy, S.V.: 'Optimal allocation and sizing of distributed generation in distribution network using ant colony search algorithm'. Proc. of Int. Conf. Advances in Communication, Network, and Computing, CNC, 2014
[33] Nanchian, S., Mazumdar, A., Pal, B.C.: 'Three-phase state estimation using particle swarm optimization', IEEE Trans. Smart Grid, 2015, 99, pp. 1-12
[34] Naka, S., Genji, T., Yura, T., et al.: 'A hybrid particle swarm optimization for distribution state estimation', IEEE Trans. Power Syst., 2003, 18, (1), pp. 6068
[35] Janeja, M., Nagar, S.K.: 'Particle swarm optimization algorithm and its parameters: a review'. 2016 Int. Conf. Control, Computing, Communication and Materials (ICCCCM), pp. 1-5
[36] Narayanan, K., Siddiqui, S.A., Fozdar, M.: 'Hybrid islanding detection method and priority-based load shedding for distribution networks in the presence of DG units', IET. Gener. Transm. Distrib., 2017, 11, (3), pp. 586595
[37] Kayalvichi, S., Viood Kumar, D.M.: 'Disputchable DG planning in distribution networks considering costs'. IEEE Int. Conf. Recent Development in Control, Automation and Power Engineering (RDCAPE), 2015
[38] Savier, J.S., Das, D.: 'Impact of network reconfiguration on loss allocation of radial distribution systems', IEEE Trans. Power Deliv., 2007, 22, (4), pp. $2473-2480$
[39] Das, D., Kothari, D.P., Kalam, A.: 'Simple and efficient method for load flow solution of radial distribution network', Int. J. Electr. Power Energy Syst., 1995, 17, (5), pp. 335-346