# An Efficient Probabilistic Approach Based on Area Grey Incidence Decision Making for Optimal Distributed Generation Planning 

Dawei Huang ${ }^{1}$, Hongwei Li ${ }^{1}$, Guowei Cai ${ }^{1}$, Nantian Huang ${ }^{1}$, Na Yu ${ }^{1}$,Zheng Huang ${ }^{1}$<br>${ }^{1}$ Key Laboratory of Modern Power System Simulation and Control \& Renewable Energy Technology, Ministry of Education (Northeast Electric<br>Power University), Jilin 132012, China

Corresponding author: Nantian Huang (e-mail: huangnantian@126.com).
This work were supported in part by the National Natural Science Foundation of China (51307019) and Provincial Industrial Innovation Project in Jilin Province (2018C034-7).

ABSTRACT The increase in the scale of distribution networks significantly reduces the efficiency of intelligent planning for distributed generation (DG). To improve the efficiency of intelligent DG planning and avoid the impact of uncertainty concerning renewable energy on it, this paper proposes a sensitivity index for the bus-embedded multi-objective estimation of distribution algorithm (MEDA) based on the semi-invariant probabilistic power flow approach to achieve an optimal solution. The sensitivity indices of the buses are comprehensively enabled to obtain a new index and determine their sensitivity sequences based on the area grey incidence decision making method. Subsequently, according to the uncertainty of wind turbine generators and photovoltaics, a probability model is established, and the semi-invariant method is used to solve for the probabilistic power flow according to a correlation model. Finally, the sensitivity of the proposed bus-embedded MEDA to enhancing the efficiency of the solution is examined. The optimal DG allocation scheme is obtained with the goal of achieving the lowest total cost in the planning year. Finally, the feasibility and effectiveness of the proposed model and method are verified using simulations of the IEEE 33-bus, IEEE 69-bus, and IEEE 118-bus test systems.

INDEX TERMS distributed generation; sensitivity index; multi-objective estimation of distribution algorithm; area grey incidence decision making; probabilistic power flow

## I. INTRODUCTION

Distributed generation (DG) has the advantage of cleanliness, and is environmentally friendly, low cost, and reliable [1-3]. The suitable installation of DG in distribution networks can improve the quality of voltage, reduce network loss, reduce peak-valley differences, and improve the reliability of power supply [4-5]. However, due to the randomness and volatility of outputs of DG, such as wind power and photovoltaics (PV), there are adverse effects on distribution networks, such as voltage fluctuation [6] and the influenced economics of distribution networks.

The incorporation of DG into distribution networks has an important impact on line losses and voltage distribution in distribution systems [7], and the power flow calculation is the primary approach to quantify this impact. An objective function is set based on the calculated bus voltage and line losses to carry out the DG planning [8].

DG planning generally consists of two tasks: selecting location and determining capacity. Reasonable optimal installation location and capacity of DG are obtained according to different planning objective. Depending on the planning objective, different planning methods can be used to optimize planning under different scenarios. Prevalent planning methods [9] can be divided into two categories: classical approaches and Artificial Intelligence algorithms. Classical approaches are mostly based on determining the mathematical solution to the given problem [10]. Reference [11] used linear programming (LP) to determine the optimal location and capacity of embedded generation (EG) under the constraints of the relevant phase technology. ElKhattam et al. proposed a mixed-integer non-linear programming (MINLP) model [12] to solve for the optimal location and capacity of a DG. However, as the size of the distribution network increases, the classical method becomes relatively time-consuming and is slow to converge.

To solve this problem, Artificial Intelligence-based algorithms have been widely used in DG planning. In Ref. [13] the authors established a multi-objective optimization model of power loss, cost, and voltage deviation, and used the multi-objective shuffled bat algorithm (MOShBAT) to determine the location and capacity of DG. In Ref. [14] studies the energy storage placement problem for voltage stability by using the GA algorithm. In Ref. [15] studies the energy storage placement problem from the small signal (oscillation damping) stability perspective by using PSO algorithms.

Although the above studies analyze the DG planning problem from different perspectives, the efficiency of intelligent planning is clearly reduced with an increase in the scale of the distribution network. As well as, in largescale distribution network planning, a single artificial intelligence method is prone to premature convergence and local optimum problems. And it is difficult to meet the requirements of distribution network planning.

To improve the efficiency of the Artificial Intelligence-based algorithms, many methods have been employed to analyze the sensitivity of buses of the distribution network to system fluctuations. Buses are ordered in descending order of sensitivity to reduce the scope of the potential solution space and speed up optimization. The voltage stability index (VSI) [16] analyzes vulnerable buses in the system as candidate access buses of the DG from the perspective of voltage stability. It then uses a search algorithm to determine the optimal capacity of the DG to minimize line losses. The loss sensitivity factors (LSFs) method [17] analyzes sensitive buses in the system as the DG access buses from the perspective of network loss, thereby significantly reducing the range of candidate locations for the installation of DG, and uses the ant lion optimization algorithm to determine the location and capacity of DG. In Ref. [18], the combined power loss sensitivity method, index vector method (IVM), and voltage stability index (VSI) method were used to determine the order of candidate positions for DG installation, and the best planning result was obtained by using the combined power loss sensitivity method. In the above literature, several methods that determine the optimal location of DG have been used to evaluate the sensitivity of the system bus. And buses with higher sensitivity have been selected to access the DG, which helps improve system reliability. However, different bus sensitivity indices consider the operating characteristics of the distribution network from different perspectives. Using different methods to analyze the sensitivity of buses may lead to conflicts in their analysis, and it is impossible to directly guide such planning. The comprehensive weighting method can effectively avoid such problems.

The DG accessed to highly sensitive nodes can improve the reliability of the system voltage. However, highly sensitive buses are vulnerable to the randomness of output of PVs and wind energy (WE), which reduces voltage stability. Therefore, it is important to consider the
influence of the randomness of output of the DG on the stability of the distribution network in DG planning. The conventional power flow does not consider this randomness in calculating the distribution network, and the results of its analysis thus cannot guide distribution network planning of highly volatile DGs. The investment in DG, and the costs of operating and maintaining of DG, and purchasing electricity from the main network are introduced into the objective function in this paper, which renders it divergent from optimal power flow (OPF). Therefore, when planning distribution networks that consider the randomness of outputs of PVs and WEs, probabilistic power-flow analysis should be used to analyze the impact on the system voltage and line losses after DG access based on an analysis of the characteristics of the output of the PV and WE. In Ref. [19], with the lowest total cost and minimum technical risk, the Monte Carlo method was used for probabilistic power flow analysis to solve problems related to the location and capacity of the DG. In Ref. [20], considering the randomness of PV and the random charging characteristics of electric vehicles, the 3 point estimation method (3PEM) was used for probabilistic power flow analysis to determine the location and capacity of DG. In Ref. [21], considering uncertainty in such factors as plug-in electric vehicles (PEV), DG, and fuel price, the Monte Carlo simulation method was used to calculate probabilistic power flow. And the genetic algorithm was used to solve the problem of the location and capacity of DG according to the results. Although the Monte Carlo simulation can provide accurate results, the computation is time-consuming, because of which it is not suitable for dealing with practical systems. The semi-invariant method using the Gram-Charlier series expansion avoids complicated convolution calculations, and can accurately calculate the probability distribution with fewer computations [22], which is more keeping with the requirements of efficient and intelligent distribution network planning.

To improve the efficiency of the distribution network through intelligent planning, and balance the conflict between methods used to determine the optimal location of DG. A sensitivity index of buses embedded multi-objective estimation of distribution algorithm (MEDA) based on the semi-invariant probability power-flow approach is proposed in this paper to obtain the optimal solution. The comprehensive empowerment of the LSFs, VSI, and IVM to obtain the new index and the sequence of sensitivities of the buses based on the area grey incidence decision making (AGIDM) method is first carried out. According to the uncertainty of WE and PV generators, a probability model is then established, and the semi-invariant method is used to solve for the probabilistic power flow of the distribution network according to a probability model. The constraints are then tested according to the results of flow, after which the objective function is calculated. Finally, the optimal DG configuration scheme with the lowest total cost in the planning year is obtained using the MEDA.

## II. MULTI-INDEX COMPREHENSIVE EMPOWERMENT BASED ON AGIDM

A single bus sensitivity index considers the operating characteristics of the distribution network system from a single perspective, and thus can make only limited use of system variables and parameters. When different methods are used to analyze the sensitivity of system buses, analyses of the same bus may cause a conflict, and planning cannot be directly guided in this case. To solve this problem, the AGIDM method is proposed to comprehensively weight multiple indices, and achieve a comprehensive evaluation of buses that are candidates for DG.

## A Methods to determine optimal DG location

1) Loss Sensitivity Factors

The sensitivity factor method is based on the principle of linearization of an originally nonlinear equation around the initial operating point, which helps reduce the number of solution space [17]. Buses with high LSF values can be considered candidates for installing DG. The LSFs approach analyzes sensitive buses in the system from the perspective of network loss, and can be computed from the following equation:
![img-0.jpeg](img-0.jpeg)

FIGURE 1. Equivalent circuit of radial distribution system

$$
\begin{gathered}
P_{L, k i}=\left(P_{b o a d, i}^{2}+Q_{b o a d, i}^{2}\right) R_{k i} / U_{i}^{2} \\
L S F s=\partial P_{L, k i} / \partial Q_{b o a d, i}=2 Q_{b o a d, i} R_{k i} / U_{i}^{2}
\end{gathered}
$$

Where $R_{k i}$ represents the resistance of branch $k-i . P_{b o a d, i}$ and $Q_{b o a d, i}$ represent the active and reactive powers of the load at the $i^{\text {th }}$ bus. $P_{L, k i}$ represents active loss of branch $k-i . U_{i}$ represents the voltage of the $i^{\text {th }}$ bus.
2) Voltage Stability Index

Reference [16] proposed a VSI method, which analyzes vulnerable buses in the system from the perspective of voltage stability. If the VSI is close to zero, the system is more stable. If the VSI is high, the system is vulnerable to stability. A bus with a high VSI is more sensitive and is selected for optimal DG deployment. It can be computed from the following equation:

$$
V S I=4\left(\left(P_{b o a d, i}^{2}+Q_{b o a d, i}^{2}\right) / Q_{b o a d, i}\right) X_{k i} / U_{k}^{2}
$$

Where $X_{k i}$ represents the reactance of branch $k-i$.
3) Index Vector Method

Index Vector is formulated by running the base case load flow on a given radial distribution network, and calculating the reactive component of current in the branches and the concentration of reactive power load at each node [18]. In this work, the IVM is used for the optimal DG allocation problem. It analyzes buses in the system that can
be installed with DG from the perspective of bus voltage, branch current, and the system reactive load. It can be computed from the following equation:

$$
I V M(i)=\frac{1}{U_{i}^{2}}+\frac{I_{q, k i}}{I_{p, k i}}+\frac{Q_{b o a d, i}}{Q_{a l l}}
$$

Where $I_{q, k i}$ and $I_{p, k i}$ represent the imaginary and real components, respectively, of the current of branch $k-i$, and $Q_{\text {aII }}$ represents the total reactive load of the given distribution system.

Different bus sensitivity indices consider the operating characteristics of the distribution network from different perspectives, because of which the variables and parameters of the system can only be used in a limited way. Single indices can meet only some optimization goals. However, using different methods to analyze the sensitivity of buses, may lead to conflicts in the analysis of the same bus, and it becomes impossible to directly guide planning.

## B Optimal comprehensive empowerment based on area grey incidence decision making

Because the grey relational decision-making method belongs to objective weighting method, it can effectively analyze the correlation and conflict among various indicators to determine the weight of different indicators. The area grey incidence decision-making method (AGIDM) improves the traditional grey relational decision making method, and uses the area to analyze the correlation and conflict between indicators. To solve the above problems, the comprehensive empowerment of multiple indices using the AGIDM method [23] to evaluate the sensitivity of buses of the distribution network is proposed to avoid conflicts between indices.

The procedure of optimal comprehensive empowerment for AGIDM is as follows.

The number of buses in the system is the number of candidate solutions for DG planning.
(1) Calculate the LSFs, VSI, and IVM to construct the original index matrix $A=\left(a_{i j}\right)_{n \in \alpha}$.

Where $\boldsymbol{\mu}_{\boldsymbol{\alpha}}$ and $n$ represent the numbers of buses and indices, respectively.
(2) Standardize $A$ to get $A=\left(a_{i j}\right)_{n \in \alpha}$. Then normalize $\hat{A}$ according to Eq. (5). According to Eq. (6), calculate the entropy of each index. Finally, calculate the weight of each index according to Eq. (7).

$$
\begin{gathered}
H_{i j}=a_{i j} / \sum_{i=1}^{m} a_{i j} \\
E_{i}=-(1 / \ln (n)) \sum_{j=1}^{n} H_{i j} \ln H_{i j} \\
\omega_{i}=\left(1-E_{i}\right) /\left(m-\sum_{i=1}^{m} E_{i}\right)
\end{gathered}
$$

Where $H_{i j}$ represents the normalized result of $a_{i j}, E_{i}$ represents the entropy of the $i^{\text {th }}$ index, and $\omega_{i j}$ represents the weight of the $i^{\text {th }}$ index.

(3) The maximum value of each index in $A^{*}$ is composed of the ideal ranking scheme vector $A^{*}$, and the minimum value constitutes the negative ideal ranking scheme vector $A^{-}$. The ideal ranking decision matrix $B=\left(A^{*} ; A\right)$ and the negative ideal ranking decision matrix $C=\left(A^{*} ; A\right)$ are constructed, respectively.
(4) Normalize $B$ and $C$ to obtain new matrices $B_{1}$ and $C_{1}$, respectively, according to Eq. (8).

$$
a_{i j}^{*}=\left(a_{i j}-m_{j}\right) /\left(M_{j}-m_{j}\right), a_{i j}^{*} \in[0,1]
$$

Where $m_{j}$ and $M_{j}$ represent the minimum and maximum values, respectively, of the $j^{\text {th }}$ index.
(5) Construct the area matrix of the ideal sorting scheme vector $S_{1}$ and negative ideal sorting scheme vector $S_{2}$ according to Eq. (9), and the area correlation coefficient matrices $\gamma^{+}$and $\gamma^{-}$according to Eq. (10).

$$
\begin{aligned}
S_{0 i}(k) & =\int_{k}^{k+1}\left|X_{0}^{0}(k)-X_{i}^{0}(k)\right| d t \\
& =\frac{\left|X_{i}^{0}(k+1)-X_{0}^{0}(k+1)\right|+\left|X_{i}^{0}(k)-X_{i}^{0}(k)\right|}{2} \\
& \gamma\left(X_{0}, X_{i}\right)=\frac{1}{n} \sum_{k=1}^{n} \gamma\left(X_{0}^{0}(k), X_{i}^{0}(k)\right)
\end{aligned}
$$

Where $X_{0}^{0}(k)$ and $X_{i}^{0}(k)$ represent the sequence of the ideal sorting scheme, and the candidate sorting scheme sequence is normalized. $S_{0 i}(k)$ represents the area formed by two adjacent indices between the curves of the ideal sequence of sorting schemes and the candidate sequence of sorting schemes. $\gamma\left(X_{0}, X_{i}\right)$ is called the area grey incidence of $X_{0}$ and $X_{i}$, and satisfies the four axioms of grey incidence.
(6) Calculate the incidence $\gamma_{0 i}^{*}$ between the candidate ranking scheme and the ideal ranking scheme, as well as incidence $\gamma_{0 i}^{-}$between the candidate ranking scheme and the negative ideal ranking scheme using the index weights values obtained in step (2).
(7) Calculate the grey incidence relative closeness value of each candidate sorting scheme according to Eq. (11), and sort the candidate sorting schemes according to size.

$$
C_{0 i}=\frac{\gamma_{0 i}^{*}}{\gamma_{0 i}^{*}+\gamma_{0 i}^{-}}
$$

The area grey incidence decision making method can consider the angles of analysis of several methods, and make better use of system parameters to obtain reasonable evaluation results. It can also better guide DG planning, to improve efficiency and effectiveness.

## III. PROBABILISTIC POWER FLOW OF DISTRIBUTION NETWORK BASED ON SEMI-INVARIANT METHOD

It is necessary to consider the impact of the randomness of output of WEs and PVs in DG planning. Therefore, the semi-invariant method is used to analyze the probabilistic flow of the distribution network with uncertain factors, and the probability distributions of voltage, phase angle, and power are obtained to analyze the influence of accessing DG on the distribution network in scenarios involving uncertainties.

## A Probabilistic modeling of DG

1) Wind energy

The output of the WE is significantly influenced by wind speed, and the change in wind speed can be described using a probability distribution function (PDF). For example, the PDF of the Weibull probability distribution [24] is:

$$
f(v)=\left(\frac{k}{v}\right)\left(\frac{v}{c}\right)^{k-1} \exp \left(-\frac{v}{c}\right)^{k}
$$

Where $v$ represents wind speed. $c$ and $k$ represent the scale and shape factors of the Weibull distribution function, respectively.

We compute the power generated by the WE as follows[25]:

$$
P_{W, W F}=\left\{\begin{array}{lr}
0, & 0 \leq v \leq v_{c i} \text { or } v \geq v_{c o} \\
P_{W, W r} \times\left(\frac{v-v_{c i}}{v_{r}-v_{c i}}\right), v_{c i} \leq v \leq v_{r} \\
P_{W, W r}, & v_{r} \leq v \leq v_{c o}
\end{array}\right.
$$

Where $P_{W, W r}$ represents the rated power of the WE. $v_{r}$ represents the rated wind speed. $v_{c i}$ and $v_{c o}$ represent the cut-in and cut-out speeds, respectively.
(2) Photovoltaic energy

The solar irradiance $r$ can be approximated as a Beta distribution [25] for a specific period of time, and its PDF is:

$$
f(r)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)} r^{\alpha-1}(1-r)^{\beta}
$$

Where $r$ is solar radiation, $W / m^{2} . \alpha$ and $\beta$ are the shape parameters of the Beta distribution, respectively. $\Gamma(\cdot)$ is an incomplete gamma function.

The relationship between the active output of the PV and solar radiation is as follows:

$$
P_{W, P V}=\left\{\begin{array}{lr}
P_{W, P V r}\left(\frac{r}{r_{C} r_{S T D}}\right) & 0 \leq r \leq r_{C} \\
P_{W, P V r}\left(\frac{r}{r_{S T D}}\right) & r_{C} \leq r \leq r_{S T D} \\
P_{W, P V r} & r_{S T D} \leq r
\end{array}\right.
$$

Where $P_{W, P V v}$ is the rated PV power. $r_{C}$ and $r_{S T D}$ [W/m2] represent a certain radiation point, which is usually set to $150 \mathrm{~W} / \mathrm{m}^{2}$, and the solar radiation in standard conditions is typically set to $1000 \mathrm{~W} / \mathrm{m}^{2}$.

## B Semi-invariant probabilistic power-flow method

The semi-invariant method using the Gram-Charlier series expansion avoids complicated convolution calculations, and can accurately calculate the probability distribution with fewer calculation amount, and improve the calculation efficiency [22]. The semi-invariant method is used to calculate the probabilistic power flow, which can better describe the probability characteristics of the wind turbine and the photovoltaic output. The expansion of the Gram-Charlier series, which is more keeping with the requirements of efficient and intelligent distribution network planning. The semi-invariant method is used to calculate probabilistic power flow as follows:
(1) Input the network parameters of the distribution network system to be planned.
(2) Calculate conventional power flow under normal operating conditions to obtain the state variables $X_{0}$, the branch power variable $Z_{0}$, the Jacobian matrix $J_{0}$, and the sensitivity matrix $S_{0}$ at the reference operating point. Perform probabilistic modeling for the characteristics of random output of PV and WE. Calculate the semi-invariant $\Delta W$ of the random output of PV, and WE, and the power of the bus with DG to the eighth order.
(3) Linearize the equations of bus flow and branch flow equation at the reference operating point, and obtain Eqs. (16) and (17), respectively. $\bar{X}$ is the state column vector, comprising the amplitude of the bus's voltage and its phase angle, and $\bar{Z}$ is the column vector, consisting of the active and the reactive power flow.

$$
\begin{aligned}
& \Delta X=X-X_{0}=J_{0}^{-1} \Delta W=S_{0} \Delta W \\
& \Delta Z=Z-Z_{0}=G_{0} \Delta X=G_{0} S_{0} \Delta W
\end{aligned}
$$

Where $\left.G_{0}=\frac{\partial Z}{\partial X}\right|_{X=X_{0}}$.
(4) The semi invariant of each order of $\Delta X$ and $\Delta Z$ can be calculated based on the above formula, and the PDF and cumulative distribution function of $\Delta X$ and $\Delta Z$ are obtained using the Gram-Charlier series expansion.

## IV. SENSITIVITY INDEX OF BUS EMBEDDED MEDA FOR DG EFFICIENT PLANNING

The WE and PV are used as planning objectives to establish the minimum objective function for the total cost of network loss, investment required for DG, the operation and maintenance of DG, and the cost of purchasing electricity from the main network. To solve the optimal DG allocation scheme, the sensitivity of the bus is embedded into the MEDA method [26] to improve the global optimization ability and efficiency of the algorithm.

## A Objective function

From an economic perspective, the costs of network loss, DG installation, operation and maintenance of DG, and the sum of the cost of purchasing electricity from the main network are used as the total cost in the planning year, with the lowest total cost used as objective function.

$$
\left\{\begin{array}{l}
\min f=\min \left(C_{\text {loss }}+C_{\text {im }}+C_{r e}+C_{b u c}\right) \\
C_{\text {loss }}=p_{c} \cdot T \cdot \sum_{m=1}^{N_{T}} \sum_{j=1}^{N_{L}} \beta_{m} P_{l o s s, j} \\
C_{b u c}=C_{W T}^{N_{T}} \sum_{i=1}^{N_{W T}} P_{W T, i}+C_{P V}^{N_{V}} \sum_{i=1}^{N_{P V}} P_{P V, i} \\
C_{r e}=\sum_{m=1}^{N_{T}} \beta_{m}\left(\sum_{i=1}^{N_{W T}} C_{W T, i}^{r e} P_{W T, i}+\sum_{i=1}^{N_{W T}} C_{P V, i}^{r e} P_{P V, i}\right) \\
C_{b u c}=p_{c} \cdot T \cdot \sum_{m=1}^{N_{T}} \beta_{m}\left(\sum_{i=1}^{N_{T}} P_{b a u d, i}+\sum_{j=1}^{N_{L}} P_{l o s s, j}-\sum_{i=1}^{N_{W T}} P_{W T, i}-\sum_{i=1}^{N_{W T}} P_{P V, i}\right)
\end{array}\right.
$$

Where $C_{\text {loss }}$ is the cost of network loss. $C_{\text {im }}$ is the cost of the DG investment. $C_{r e}$ is the cost incurred to operate and maintenance of DG. $C_{\text {buc }}$ is the cost of the cost of purchasing electricity from the main network. $p_{c}$ is unit electricity price. $T$ is the number of hours of the annual maximum loss of load. $N_{T}$ is the number of planning level years of DG. $N_{L}$ is the number of total branches of the distribution network. $\beta_{m}$ is the present value factor, $\beta_{m}=1 /(1+d)^{m}, d$ is the discount rate, and $m$ is an incremental interval (in a year). $P_{\text {loss }, j}$ is the active power loss of the $j^{\text {th }}$ branch. $C_{W T}^{i n v}$ is the investment cost of the unit capacity of WE. $C_{P V}^{i n v}$ is the investment cost of the unit capacity of PV. $N_{W T}$ is the total number of WEs installed in the distribution network. $N_{P V}$ is the total number of PVs installed in the distribution network. $P_{W T, i}$ is the installation capacity of the $i^{\text {th }} \mathrm{WE}$, and $P_{P V, i}$ is the installation capacity of the $i^{\text {th }} \mathrm{PV} . C_{W T, i}^{r e}$ and $C_{W T, i}^{r e}$ are the cost of operating and maintaining the $i^{\text {th }} \mathrm{WE}$ and PV , respectively. $N$ is the number of power system buses.

## B Constraints

The proposed DG allocation problem is designed to meet the following constraints:
(1) Constraints on active and reactive power flows

$$
\left\{\begin{array}{l}
P_{i n}-U_{i} \sum_{m \neq i} U_{i n}\left(G_{i m} \cos \delta_{i m}+B_{i m} \sin \delta_{i m}\right)=0 \\
Q_{i n}-U_{i} \sum_{m \neq i} U_{i n}\left(G_{i m} \sin \delta_{i m}-B_{i m} \cos \delta_{i m}\right)=0
\end{array}\right.
$$

(2) The chance constraint of bus voltage [27]

$$
P_{r}\left\{\left|U_{i}\right| \leq U_{i \max }\right\} \geq \varepsilon
$$

(3) The chance constraint of the branch power [27]

$$
P_{r}\left\{P_{j \min } \leq P_{j} \leq P_{j \max }\right\} \geq \theta
$$

(4) Constraint on the capacity of the DG

$$
\sum_{i=1}^{N_{D G}} S_{D G G} \leq S_{\max }
$$

Where $P_{m}$ and $Q_{m}$ are the active and reactive injection powers of the $i^{\text {th }}$ bus, respectively. $G_{m}$ and $B_{m}$ are the bus admittances of the system. $\delta_{m}$ is the difference in voltage angle between the $i^{\text {th }}$ bus and the $m^{\text {th }}$ bus. $P_{r}\{\cdot\}$ indicates the probability of branch power and bus voltage satisfying the constraints, and $U_{j \max }$ is the upper limit of the amplitude of voltage of the $i^{\text {th }}$ bus. $P_{j}$ is the transmitted power of the $j^{\text {th }}$ branch, $P_{j \min }$ and $P_{j \max }$ are the lower and upper limits of the transmitted power of the $j^{\text {th }}$ branch, respectively. $\varepsilon$ and $\theta$ are the confidence levels for the bus amplitude of voltage and branch power not exceeding limits. $S_{D G}$ is the capacity of the $i^{\text {th }} \mathrm{DG}$, and $S_{\max }$ is the total installed capacity required for DG to allow access.

To save space, the relevant constraints of WE and PV are described in Ref. [28].

## C Efficient MEDA based on bus sensitivity

The MEDA is a stochastic optimization algorithm developed using traditional genetic algorithm. According to the characteristics of the optimization and parameters of the MEDA, the sensitivity of the bus embedded MEDA is proposed as a solution to the problem of optimal DG allocation. The steps to solve the DG optimization model are as follows:
(1) Input the basic parameters of the distribution network, and set the population size to $N_{\text {stizpop }}$, and the maximum number of iterations to $N_{\max }$ ges.
(2) Run the power flow to calculate the LSFs, VSI, IVM, and AGIDM of each bus, and obtain the order of sensitivity of the buses of the DG to be installed to initialize the MEDA population. Then obtain the initial DG allocation scheme.
(3) Use the semi-invariant method to calculate the probabilistic power flow of the population, and calculate the objective function and fitness value according to the results of the power-flow. Check whether the constraint is met. If the constraint is met, the optimal solution is retained to perform the next step; otherwise, the fitness is added to the penalty M , and the next step is performed.
(4) According to the fitness value, update the allocation of the DG, and select the fitness group with a better fitness value. Determine whether the constraints are me and, if so, go to the next step; otherwise update the counter $N=N+1$ and go to the next step.
(5) According to the information of each individual in the dominant group, estimate the mean $\mu$ and variance $\sigma$ of each variable according to the normal distribution in Eqs. (23) and (24). The normal distribution probability model of the dominant group is thus obtained.

$$
\begin{gathered}
\mu=\bar{S}=\frac{1}{L} \sum_{k=1}^{L} S_{k} \\
\sigma=\sqrt{\frac{1}{L-1} \sum_{k=1}^{L}\left(S_{k}-\bar{S}\right)}
\end{gathered}
$$

(6) From the estimated normal distribution probability model, perform random sampling according to Eq. (25), and obtain $N_{\text {stizpop }}$ new solutions to form the new population.

$$
\left\{\begin{array}{l}
x_{1}=\mu+\sigma\left(-2 \ln y_{1}\right)^{1 / 2} \cos 2 \pi y_{2} \\
x_{2}=\mu+\sigma\left(-2 \ln y_{1}\right)^{1 / 2} \cos 2 \pi y_{2}
\end{array}\right.
$$

Where $y_{1}$ and $y_{2}$ are two independent random numbers in the interval $[0,1]$.

If the termination condition of the algorithm is met, the best individual in the new population is the optimal allocation. Otherwise, the algorithm performs (3). The process of the proposed method is shown in Fig.2.
![img-1.jpeg](img-1.jpeg)

FIGURE 2. Flowchart of AGIDM-MEDA

## V. NUMERICAL RESULT

To evaluate the advantages of the proposed method in terms of planning efficiency and effect, we implemented it on IEEE 33-bus, IEEE 69-bus and IEEE118-bus power systems. The parameters and values in calculation example are shown in Table 1. Considering the active and reactive powers injected by WE, the power factor was set to 0.9 . Considering that PV only provides active power, its power factor was set to 1 . The planning period considered in this paper is 20 years. In our experimental part, 10 simulations were carried out for each method to verify the proposed method, and the results were also averaged. The simulation was implemented in MATLAB.

TABLE I
PARAMETERS AND VALUES IN CALCULATION EXAMPLE

| Parameters | Values | Parameters | Values |
| :--: | :--: | :--: | :--: |
| $\boldsymbol{\lambda}$ | 1.8 | $C_{P V}^{i n v}(\$ / \mathrm{KW})$ | 1000 |
| $\boldsymbol{C}$ | 7.2 | $C_{W T}^{r v}(\$ / \mathrm{KW})$ | 1 |
| $\boldsymbol{\alpha}$ | 0.23 | $C_{P V}^{r v}(\$ / \mathrm{KW})$ | 1.5 |
| $\boldsymbol{\beta}$ | 1.31 | $\boldsymbol{\varepsilon}$ | 0.8 |
| $p_{c}(\mathrm{~S} / \mathrm{KWh})$ | 0.1 | $\boldsymbol{\beta}$ | 0.8 |
| $N_{T}$ | 20 | $N_{\text {scispop }}$ | 100 |
| $d$ | 0.08 | $N_{\text {max pos }}$ | 200 |

## A Distribution network planning based on probabilistic power flow

Although deploying DG at on vulnerable buses can improve system reliability, the volatility of DG may affect voltage stability of distribution systems. To avoid the impact randomness of output of DG on the stability of voltage of the buses, distribution network planning based on the MEDA optimization algorithm was performed using the results of the probabilistic flow analysis of the sorting of candidate buses for DG based on the AGIDM method. In the optimization, the probability of voltage limit in the probability flow was constrained to avoid PV or WE and other types of DG access, which can lead to a violation of the bus voltage. This improved the stability of the system following DG access. The results of the simulation show that the capacity of bus number 9 accessing PV was 1899 KVA , and the capacities of bus number 31 to access PV and WE were 305 KVA and 863 KVA , respectively. The capacity of bus number 13 to access WE was 655 KVA . The probability density curves of the amplitude of voltage before and after buses number 13 and 31 accessed DG are plotted in Figs. 3 and 4, respectively.
![img-4.jpeg](img-4.jpeg)

FIGURE 3. Probability density curves showing voltage of bus number 13
As shown in Fig.3, the amplitude of voltage of the bus was not limited before bus 13 accessed DG. After accessing the DG, it is known that the amplitude of voltage of the bus increased, and was concentrated at the required voltage.
![img-3.jpeg](img-3.jpeg)

FIGURE 4. Probability density curves showing voltage of bus number 31
Fig. 4 shows that depending on an analysis of the probabilistic flow, the amplitude of voltage of bus number 31 had a lower limit probability before it accessed DG, and the amplitude of voltage improved after its access to DG. The amplitude of voltage was distributed in [1, 1.02], and there was no voltage limit.

This indicates that when DG was placed in the vulnerable buses in the system, their amplitude of voltage improved. The use of the probabilistic power flow to obtain the probability distribution of bus voltage after accessing volatile DG, ensured that the voltage of the bus with the strong volatility of PV or WE, stabilized within the required voltage.

## B IEEE 33-bus power system

The IEEE 33-bus power system had a total load of 3720 KW and 2300 KVAr at a voltage of 12.66 KV . The system data are presented in Ref. [29].The values of the LSFs, VSI, IVM, and AGIDM for the IEEE 33-bus power system were as shown in Fig. 5 (a), (b), (c), and (d), respectively.
![img-4.jpeg](img-4.jpeg)

FIGURE 5. The values of (a)LSFs (b)VSI (c)IVM (d)AGIDM for IEEE 33bus power system

1) ANALYSIS OF ALGORITHM PERFORMANCE

In this section, the proposed intelligent algorithm MEDA as well as the prevalent optimization algorithms,

MOPSO (Multi-Objective PSO) [30], CSA (Crow Search Algorithm) [31], MOICA (Multi-Objective Imperialist Competitive) [32], and NSGA-II (Non-dominated Sorting Genetic Algorithm II) [33] are introduced. A comparative experiment was performed to show that the proposed MEDA has a higher planning efficiency and better planning effect. The group size of the five algorithms was 100, the maximum number of iterations was 200, and the penalty item $\mathrm{M}=1 \mathrm{e}^{15}$. The results of the experiment are shown in Table 2, and a comparative result of the curves of convergence to optimization of the methods is shown in Fig.6.

Fig. 6 shows that the rate of convergence of MEDA was higher than that of the other optimization algorithms. Combined with data in Table 2, it is clear that using CSA for distribution network planning is not ideal because the location of DG is not the most suitable. Although it provided a $61.079 \%$ reduction in total power losses, its value of $6.5396 \times 10^{7}(\$)$ was worst of the five optimization algorithms. MEDA, MOICA, and NSGA-II chose bus numbers 28 and 9 as the best locations for DG installation, but because of their different capacities for DG, the effects of planning were different. By using MEDA for planning, the optimal objective function value of $4.6871 \times 10^{7}(\$)$ is obtained in the minimum number of iterations, $28.327 \%$ lower than the function value obtained by planning with CSA, effectively reducing the network loss of $65.511 \%$. Moreover, the voltage level of system nodes tends to be more stable. This confirms that the proposed intelligent planning algorithm MEDA is more efficient in terms of planning the DG of the distribution network, and the obtained planning results are optimal.
![img-5.jpeg](img-5.jpeg)

FIGURE 6. Comparison of optimization convergence curves for IEEE 33bus power system
![img-6.jpeg](img-6.jpeg)

FIGURE 7. Optimization convergence curves of planning methods for IEEE 33-bus power system
2) COMPARISON OF THE PLANNING METHODS OF DIFFERENT OPTIMAL DG LOCATION METHODS COMBINED WITH MEDA
(1) A new intelligent algorithm MEDA that is not combined with any sort method;
(2) The LSFs method is combined with the MEDA (LSFsMEDA) method;
(3) The VSI method is combined with the MEDA (VSIMEDA) method;
(4) The IVM method is combined with the MEDA (IVMMEDA) method;
(5) The AGIDM method is combined with the MEDA (AGIDM-MEDA) method.

TABLE II
RESULTS OF OPTIMIZATION FOR IEEE 33-BUS POWER SYSTEM

| Algorithm | MEDA | MOICA | NSGA-II | MOPSO | CSA |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Optimization results |  |  |  |  |  |
| PV1 location | $\mathbf{2 8}$ | 28 | 28 | 6 | 28 |
| PV2 location | $\mathbf{9}$ | 9 | 9 | 13 | 13 |
| PV1 size (MVA) | $\mathbf{1 . 8 3 9}$ | 1.542 | 1.913 | 1.62 | 2.051 |
| PV2 size (MVA) | $\mathbf{1 . 6 7 3}$ | 1.974 | 1.598 | 1.989 | 0.96 |
| Performances |  |  |  |  |  |
| Worst fitness $\left(10^{7}\right)$ | $\mathbf{4 . 6 9 5 0}$ | 4.7064 | 4.7128 | 4.6982 | 6.5586 |
| Best fitness $\left(10^{7}\right)$ | $\mathbf{4 . 6 8 7 1}$ | 4.6970 | 4.7043 | 4.6883 | 6.5396 |
| Average fitness $\left(10^{7}\right)$ | $\mathbf{4 . 6 9 1 1}$ | 4.7017 | 4.7086 | 4.6933 | 6.5491 |
| Average iterations | $\mathbf{1 7 0}$ | 182 | 178 | 175 | 186 |
| Overall impact |  |  |  |  |  |
| Loss reduction (\%) | $\mathbf{6 5 . 5 1 1}$ | 59.948 | 60.963 | 60.982 | 61.079 |
| Maximum voltage (p.u.) | $\mathbf{1 . 0 0 6 2}$ | 1.0118 | 1.0048 | 1.0102 | 1 |
| Minimum voltage (p.u.) | $\mathbf{0 . 9 7 1 7}$ | 0.9699 | 0.9717 | 0.9526 | 0.9674 |

TABLE III
RESULTS OF PLANNING METHODS FOR IEEE 33-BUS POWER SYSTEM

| Planning methods | MEDA | LSFs-MEDA | VSI-MEDA | IVM-MEDA | AGIDM-MEDA |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Optimization results |  |  |  |  |  |
| PV1 location | 20 | 28 | 13 | 32 | 9 |
| PV2 location | 30 | 29 | 24 | 33 | 31 |
| WE1 location | 10 | 6 | 13 | 16 | 13 |
| WE2 location | 13 | 3 | 28 | 13 | 31 |
| PV1 size (MVA) | 0.835 | 0.225 | 0.659 | 1.574 | 1.899 |
| PV2 size (MVA) | 1.237 | 0.867 | 1.455 | 0.870 | 0.305 |
| WE1 size (MVA) | 0.880 | 2.134 | 0.467 | 0.413 | 0.655 |
| WE2 size (MVA) | 0.767 | 0.491 | 0.899 | 0.748 | 0.863 |
| Performances |  |  |  |  |  |
| Worst fitness $\left(10^{7} \%\right)$ | 3.8632 | 3.8908 | 4.7226 | 4.2698 | 3.8604 |
| Best fitness $\left(10^{7} \%\right)$ | 3.8545 | 3.8844 | 4.7145 | 4.2634 | 3.8514 |
| Average fitness $\left(10^{7} \%\right)$ | 3.8589 | 3.8876 | 4.7186 | 4.2666 | 3.8559 |
| Average iterations | 192 | 90 | 87 | 89 | 60 |
| Overall impact |  |  |  |  |  |
| Loss reduction (\%) | 70.137 | 69.526 | 72.270 | 71.172 | 75.209 |
| Maximum voltage (p.u.) | 1.0195 | 1.0094 | 1.0010 | 1.0402 | 1.0414 |
| Minimum voltage (p.u.) | 0.9717 | 0.9535 | 0.9626 | 0.9729 | 0.9824 |

TABLE IV
DETAILS OF THE POWER SYSTEMS UNDER STUDY

| Characteristics | IEEE 69 |  | IEEE 118 |  |
| :-- | :-- | :-- | :-- | :-- |
|  | Value | Details | Values | Details |
| Buses | 69 | $[34]$ | 118 | $[35]$ |
| Branches | 68 |  | 186 |  |
| Reference node | 1 | $\mathrm{Bus}_{1} 1$ | 1 | Bus $_{1} 69$ |
| Base KV | 1 | 12.66 | 1 | 138 |
| Load voltage |  | $[0.95$, |  | $[0.94$, |
| limits |  | 1.05] |  | 1.06] |

## C Medium and large-size power systems

Based on the advantages of the proposed AGIDMMEDA, a medium-size (IEEE 69-bus) and large-size (IEEE 118-bus) power system were used to verify its superiority with respect to planning efficiency and effect. The details of IEEE 69-bus power system and 118-bus power system are shown in Table 4. The 69-bus power system had a total load of 3802 KW and 2694 KVAr [34]. The 118-bus power system had a total load of 4242 MW and 1438 MVAr [35]. 1) COMPARISON OF PLANNING METHODS OF DIFFERENT OPTIMAL DG LOCATION METHODS COMBINED WITH MEDA

Likewise, from the planning efficiency and planning effect, this section presents details of the planning experiments, and contrasts the five planning methods on the IEEE 69-bus and IEEE 118-bus power systems. It verifies that the proposed AGIDM-MEDA can adapt to different scales of distribution network systems: the larger the scale of the distribution network, the higher its efficiency, and the better its effect. The results obtained from the experiment are shown in Table 5. The convergence curves of the five planning methods for the 69-bus and 118-bus power systems are shown in Figs. 9 and 10. The percentage of planning to increase the efficiency of different planning methods in the two systems is shown in Fig.11.

TABLE V
COMPARISON OF PLANNING METHODS FOR THE 69-BUS AND 118-BUS POWER SYSTEMS WITH FOUR DGS

| Power systems | Results | Planning methods |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | MEDA |  | LSFs-MEDA |  | VSI-MEDA |  | IVM-MEDA |  | AGIDM-MEDA |  |
| 69-bus power system | PV locations | 58 | 17 | 7 | 55 | 48 | 59 | 64 | 57 | 58 | 50 |
|  | WE locations | 60 | 62 | 58 | 55 | 61 | 50 | 64 | 57 | 60 | 62 |
|  | PV sizes (KVA) | 1133 | 894 | 1136 | 1455 | 1391 | 773 | 1445 | 760 | 2101 | 416 |
|  | WE sizes (KVA) | 914 | 856 | 927 | 281 | 807 | 828 | 807 | 706 | 378 | 903 |
|  | Total cost $\left(10^{11} \%\right)$ | 3.6826 |  | 3.6496 |  | 3.6583 |  | 3.6657 |  | 3.6431 |  |
|  | Loss reduction (\%) | 63.454 |  | 62.433 |  | 61.723 |  | 67.767 |  | 70.810 |  |
| 118-bus power system | PV locations | 75 | 112 | 69 | 88 | 76 | 74 | 75 | 38 | 76 | 75 |
|  | WE locations | 84 | 88 | 69 | 81 | 49 | 74 | 75 | 76 | 75 | 88 |
|  | PV sizes (MVA) | 237 | 195 | 256 | 195 | 335 | 81 | 201 | 191 | 264 | 286 |
|  | WE sizes (MVA) | 118 | 198 | 199 | 195 | 120 | 177 | 165 | 76 | 148 | 105 |
|  | Total cost $\left(10^{11} \%\right)$ | 1.6683 |  | 1.6333 |  | 1.6797 |  | 1.6755 |  | 1.6288 |  |
|  | Loss reduction (\%) | 15.656 |  | 17.959 |  | 17.206 |  | 18.480 |  | 20.335 |  |

![img-7.jpeg](img-7.jpeg)

FIGURE 9. Curves of optimization convergence of planning methods for 69-bus system

It is clear from Figs. 9 and 10 that the efficiency of AGIDM-MEDA was the higher of the two systems. As shown in Table5, it quickly converges to the optimal objective function values, which were $3.6431 \times 10^{7}(\$)$ and $1.6288 \times 10^{11}(\$)$, and effectively reduced the network loss by $70.810 \%$ and $20.335 \%$, respectively. Further, from Fig.11, we see that the planning efficiency of AGIDM-MEDA in the two systems was $70 \%$ and $75 \%$ higher than that in MEDA. The size of the distribution network system also increased, and the proposed AGIDM-MEDA method was more efficient when considering multiple DG programming. The results prove that the AGIDM-MEDA can adapt to the distribution network systems of different scales.
![img-8.jpeg](img-8.jpeg)

FIGURE 10. Optimization convergence curves of planning methods for 118 bus system
![img-9.jpeg](img-9.jpeg)

FIGURE 11. Efficiency increment of planning methods for two power systems

## VI. CONCLUSION

This paper considered the randomness of output of WEs and PVs to establish an optimal allocation model for DG based on the cost of the network loss, the total cost for the installation and investment of DGs, the operating and maintenance cost of the DGs, and the cost of purchasing electricity from the main network.
(1)The comprehensive application of the sensitivity indices of the bus were applied to obtain a new index and the sequence of the buses in order of sensitivity based on the AGIDM method to determine candidate buses for the location of deployment of DG.

(2)According to the uncertainty of WEs and PVs, a probability model is established, and the semi-invariant method is used to solve for the probabilistic power flow according to a correlation model.
(3)The sensitivity of the system's bus was determined to reduce the candidate solution space, and enhance the efficiency of the MEDA solution

In light of the impact of the strong fluctuation characteristics of load affected by the behavior of electricity consumption, the proliferation of electric vehicles in the future, and the development of energy storage equipment on distribution networks, our research in the future will consider planning DG reasonably under such complex fluctuation factors.

## REFERENCES

[1] Abapour S, Zare K, Mohammadi-Ivatloo B. Dynamic planning of distributed generation units in active distribution network [J]. Generation Transmission \& Distribution Iet, 2015, 9(12):1455-1463.
[2] Ehsan A, Yang Q. Optimal integration and planning of renewable distributed generation in the power distribution networks: A review of analytical techniques [J]. Applied Energy, 2018, 210.
[3] Xiao J, Zhang Z, Bai L, et al. Determination of the optimal installation site and capacity of battery energy storage system in distribution network integrated with distributed generation [J]. Iet Generation Transmission \& Distribution, 2016, 10(3):601-607.
[4] Evangelopoulos V A, Georgilakis P S. Optimal distributed generation placement under uncertainties based on point estimate method embedded genetic algorithm [J]. Iet Generation Transmission \& Distribution, 2014, 8(3):389-400.
[5] Tah A, Das D. Novel analytical method for the placement and sizing of distributed generation unit on distribution networks with and without considering P, and PQV, buses [J]. International Journal of Electrical Power \& Energy Systems, 2016, 78:401-413.
[6] Zhan H, Wang C, Wang Y, et al. Relay protection coordination integrated optimal placement and sizing of distributed generation sources in distribution networks[C]// Power and Energy Society General Meeting. IEEE, 2016:1-1.
[7] Zhao J H, Wen F, Dong Z Y, et al. Optimal Dispatch of Electric Vehicles and Wind Power Using Enhanced Particle Swarm Optimization [J]. IEEE Transactions on Industrial Informatics, 2012, 8(4):889-899.
[8] Kaabi S S A, Zeineldin H H, Khadkikar V. Planning Active Distribution Networks Considering Multi-DG Configurations [J]. IEEE Transactions on Power Systems, 2014, 29(2):785-793.
[9] Teng J H. Unsymmetrical open-conductor analysis for unbalanced weakly meshed distribution systems [J]. Iet Generation Transmission \& Distribution, 2010, 5(1):136-143.
[10] Mahmoud P H A, Huy P D, Ramachandaramurthy V K. A review of the optimal allocation of distributed generation: Objectives,
constraints, methods, and algorithms [J]. Renewable \& Sustainable Energy Reviews, 2017, 75:293-312.
[11] Prakash P, Khatod D K. Optimal sizing and siting techniques for distributed generation in distribution systems: A review [J]. Renewable \& Sustainable Energy Reviews, 2016, 57:111-130.
[12] Keane A, O'Malley M. Optimal allocation of embedded generation on distribution networks [J]. IEEE Transactions on Power Systems, 2005, 20(3):1640-1646.
[13] Khalesi N, Haghifam M R. Application of dynamic programming for distributed generation allocation [C]// Electrical Power \& Energy Conference. IEEE, 2009:1-6.
[14] X. Huang, G. Zhang, L. Xiao. Optimal Location of SMEs for Improving Power System Voltage Stability [J]. IEEE Trans. Appl. Supercond., vol. 20, no. 3, pp. 1316-1319, June 2010.
[15] Yongli Zhu, Chengxi Liu, Kai Sun. Optimization of Battery Energy Storage by Mixed-Integer PSO for Oscillation Damping. [J]. IEEE. Trans. Sustain. Energy, in press, doi: 10.1109/TSTE.2018.2858262.
[16] Murty V V S N, Kumar A. Optimal placement of DG in radial distribution systems based on new voltage stability index under load growth [J]. International Journal of Electrical Power \& Energy Systems, 2015, 69:246-256.
[17] Abdelaziz A.Y., Ali E.S., Abd Elazim S.M.. Flower Pollination Algorithm and Loss Sensitivity Factors for optimal sizing and placement of capacitors in radial distribution systems[J]. International Journal of Electrical Power \& Energy Systems, 2016, 78:207-214.
[18] Murthy V V S N, Kumar A. Comparison of optimal DG allocation methods in radial distribution systems based on sensitivity approaches [J]. International Journal of Electrical Power \& Energy Systems, 2013, 53(1):450-467.
[19] Soroudi A, Caire R, Hadjsaid N, et al. Probabilistic dynamic multiobjective model for renewable and non-renewable distributed generation planning [J]. Iet Generation Transmission \& Distribution, 2011, 5(5):1173-1182.
[20] Wu C, Wen F, Lou Y, et al. Probabilistic load flow analysis of photovoltaic generation system with plug-in electric vehicles [J]. International Journal of Electrical Power \& Energy Systems, 2015, 64:1221-1228.
[21] Liu Z, Wen F, Ledwich G. Optimal Siting and Sizing of Distributed Generators in Distribution Systems Considering Uncertainties [J]. IEEE Transactions on Power Delivery, 2011, 26(4):2541-2551.
[22] Zhang P, Lee S T. Probabilistic Load Flow Computation Using the Method of Combined Cumulants and Gram-Charlier Expansion [J]. IEEE Transactions on Power Systems, 2004, 19(1):676-682.
[23] Jiang S Q, Liu S F, Liu Z X, et al. Grey incidence decision making model based on area [J]. Control \& Decision, 2015, 30(4):685-690.
[24] Zhao J H, Wen F, Dong Z Y, et al. Optimal Dispatch of Electric

Vehicles and Wind Power Using Enhanced Particle Swarm Optimization [J]. IEEE Transactions on Industrial Informatics, 2012, 8(4):889-899.
[25] Morshed M J, Hmida J B, Fekih A. A probabilistic multi-objective approach for power flow optimization in hybrid wind-PV-PEV systems [J]. Applied Energy, 2018, 211:1136-1149.
[26] Prasad S, Kumar D M V. A Multi-objective Hybrid Estimation of Distribution Algorithm-Interior Point Method based Meter Placement for Active Distribution State Estimation [J]. let Generation Transmission \& Distribution, 2017.
[27] Cao Y, Tan Y, Li C, et al. Chance-Constrained Optimization-Based Unbalanced Optimal Power Flow for Radial Distribution Networks [J]. Power Delivery IEEE Transactions on, 2013, 28(3):1855-1864.
[28] Morshed M J, Hmida J B, Fekih A. A probabilistic multi-objective approach for power flow optimization in hybrid wind-PV-PEV systems [J]. Applied Energy, 2018, 211:1136-1149.
[29] Aman M M, Jasmon G B, Bakar A H A, et al. A new approach for optimum simultaneous multi-DG distributed generation Units placement and sizing based on maximization of system loadability using HPSO (hybrid particle swarm optimization) algorithm[J]. Energy, 2014, 66(4):202-215.
[30] Gitizadeh M, Ghavidel S, Aghaei J. Using SVC to economically improve transient stability in long transmission lines. IETE J Res 2014;60(4):319-27.
[31] Askarzadeh A. A novel metaheuristic method for solving constrained engineering optimization problems: Crow search algorithm [J]. Computers \& Structures, 2016, 169:1-12.
[32] Ghasemi M, Ghavidel S, Ghanbarian MM, Gharibzadeh M, Azizi Vahed A. Multiobjective optimal power flow considering the cost, emission, voltage deviation and power losses using multi-objective modified imperialist competitive algorithm. Energy 2014;78:276-89.
[33] Fangqiu X , Jicheng L , Shuaishuai L , et al. A multi-objective optimization model of hybrid energy storage system for non-gridconnected wind power: A case study in China[J]. Energy, 2018, $163: 585-603$.
[34] Aman M M, Jasmon G B , Bakar A H A , et al. A new approach for optimum simultaneous multi-DG distributed generation Units placement and sizing based on maximization of system loadability using HPSO (hybrid particle swarm optimization) algorithm[J]. Energy, 2014, 66(4):202-215.
[35] Fang X, Hu Q, Li F, Wang B, Li Y. Coupon-based demand response considering wind power uncertainty: a strategic bidding model for load serving entities [J]. IEEE Trans Power Syst 2016;31:1025-37.