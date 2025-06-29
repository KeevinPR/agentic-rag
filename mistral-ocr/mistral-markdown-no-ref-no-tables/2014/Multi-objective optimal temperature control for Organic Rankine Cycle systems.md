# Multi-objective Optimal Temperature Control for Organic Rankine Cycle Systems* 

Jianhua Zhang<br>State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources<br>North China Electric Power University<br>Beijing, 102206, China<br>zjhncepu@163.com


#### Abstract

The Organic Rankine Cycle (ORC) has attracted a lot of interests for its ability to recover low-grade heat and the possibility to be implemented in decentralized low-capacity power plants. In this paper, a new optimal temperature control method is proposed for ORC systems with non-Gaussian disturbances which influence the quality of exhaust gas. The objective here is to control the speed of the pump so that the superheated vapor temperature follows a target one. It means that the error between those two temperatures is minimized both in magnitude and randomness, which are characterized by mean value and entropy, respectively. Therefore, the proposed control strategy is regarded as a multi-objective optimization problem. To solve this problem, a Multi-Objective Estimation of Distribution Algorithm (MOEDA) is adopted to obtain all the possible optimal control inputs. Simulation results show the effectiveness of the proposed technique.


Index Terms - Organic Rankine Cycle (ORC) systems, nonGaussian disturbances, multi-objective optimized problem, multiobjective estimation of distribution algorithm (MOEDA).

## NOMENCLATURE


Mifeng Ren, Jing Xiong and Mingming Lin
School of Control and Computer Engineering
North China Electric Power University Beijing, 102206, China
renmifeng@126.com, iriszhuhai@qq.com, linmm1232008@126.com
$w$
$l$
$g$
$i$
$o$
$n$
$sh$

## wall

saturated liquid saturated vapor inlet or inner outlet or outer nominal Superheated vapor

## I. INTRODUCTION

With the growing concern over the accelerated consumption of fossil fuels and global warming problems, Organic Rankine Cycle (ORC) has attracted a lot of attention since it can efficiently convert the low grade waste heat [1]. There have been a large range of ORC applications, such as ORC biomass power plants, solar ORC-RO desalination systems, industrial waste heat recovery, and so on [2]. Some literatures about ORC systems have been published, which mainly focused on working fluids [3-6], process of integration [7-8], performance analysis and cycle optimal design [9-15].

It is essential for ORC systems to keep the temperature at evaporator outlet within a narrow range. The main reasons lie in following two aspects: 1) excessive critical temperature of the working fluid can deteriorate the system performance; 2) when the temperature is too low, the wet vapor may enter the expander. Hence, the superheated vapor temperature at the outlet of the evaporator should be well controlled. However, only a limited number of researchers have investigated the control methodology of ORCs. Quoilin et al. [16] addressed three different control strategies for variable heat sources. By using a PI controller in each single loop, the expander speed and pump flow rate were manipulated to control the evaporating temperature and the superheating, respectively. Zhang et al. [17] proposed an optimal multivariable control strategy by combining a linear quadratic regulator with a PI controller and evaluated it on a 100 kW waste heat utilizing process operating on an organic Rankine cycle. A physically based mathematical model was used and model reduction was

[^0]
[^0]:    * This work is supported by National Basic Research Program of China under Grant (973 Program 2011 CB710706) and China National Science Foundation under Grant (61374052).

applied to get a simplified control structure. In [18] the generalized predictive control approach was applied for a waste heat recovery process with organic Rankine cycle. However, the above mentioned results didn't consider the disturbances existed in ORC systems.

As a matter of fact, waste heat sources recovered by ORC systems are always time variant. Disturbances imposed on temperature and mass flow rate of the heat source can actually cause fluctuations of superheat. Moreover, these disturbances are usually unknown and non-symmetrically distributed. It has been shown that the minimum entropy principle can be used to deal with the optimal control problem for stochastic systems with non-Gaussian disturbances [19]. With the increasing quality requirements for industrial dynamic processes, more than one design objective should be satisfied. Traditionally, based upon the generalized minimum entropy criterion, the multi-objective stochastic control problem could be transformed into a single-objective dynamic optimization, where the weights denoted the different relative importance of different objectives [20]. This method is easy to understand, but the value of the weights usually could be only decided by try-and-error method, based on engineering experiences, repeating simulations and other information. And another important disadvantage is that only one optimal control signal is obtained by using this method, which cannot meet the requirements of decision maker from different aspects. Although we could get different Pareto solutions by parametrically varying the weights in the combined single objective function, the convexity and previous required information make it difficult to be solved. These complexities call for alternative approaches, evolutionary algorithms, to deal with certain types of multi-objective optimal problems. In [21, 22], differential evolution method was adopted to investigate the multi-objective minimum entropy control problems for nonlinear and non-Gaussian stochastic systems.

Motivated by the above presentation, this paper presents a new temperature control problem for ORC systems considering non-Gaussian temperature and mass flow rate of exhaust gas. For this purpose, firstly, a dynamic evaporator model is developed. Then two objective functions are carried out to make the superheated vapor temperature approach to a target one with small randomness, which can be characterized by mean value and entropy, respectively. Since the objectives may be non-differentiable and highly nonlinear, MultiObjective Estimation of Distribution Algorithm (MOEDA) [23] is applied to search the Pareto optimal solutions.

## II. PROBLEM FORMULATION

## A. Dynamic Evaporator Model

The basic organic Rankine cycle running with R245fa as working fluid is illustrated in Fig.1. The evaporator is driven by exhaust heat, where the working fluid is heated and vaporized. The vapor drives the expander to generate power and then is condensed by cooling air in the condenser. The condensed working fluid is pumped back to the evaporator to close the cycle. In reality a receiver is always considered between the condenser and pump to ensure sub-cooling.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Schematic representation of a basic ORC system
The dynamics of an ORC system are mainly dominated by the dynamics of the heat exchangers. A lumped parameter evaporator model with a moving interface boundary is proposed here. According to the phase of refrigerant, the evaporator can be divided into three parts: sub-cooled liquid section, saturated mixture section and superheated vapor section (see Fig.2). It is assumed that: 1) the evaporator is a long, thin, horizontal tube; 2) the refrigerant flowing through the evaporator tube can be modeled as a one-dimensional fluid flow; 3) axial conduction of refrigerant is negligible; 4) pressure drop along the evaporator tube is negligible.
![img-1.jpeg](img-1.jpeg)

Fig. 2 A diagram of an evaporator model for moving boundary approach
Based on above assumptions, the partial differential equations for conservation of refrigerant mass and energy can be formulated as

1) Refrigerant mass balance:

$$
\frac{\partial A \rho}{\partial t}+\frac{\partial \dot{m}}{\partial z}=0
$$

2) Refrigerant energy balance:

$$
\frac{\partial(\rho A h-A P)}{\partial t}+\frac{\partial \dot{m} h}{\partial z}=\pi D_{o} \alpha_{c}\left(T_{w}-T_{r}\right)
$$

Since the mass flow rate and pressure in the side of exhaust gas can be assumed to be invariant, only the energy conservation equation for the incompressible secondary fluid is considered, which satisfies

$$
\frac{\partial\left(\rho_{o} A_{o} h_{o}-A_{o} P\right)}{\partial t}+\frac{\partial \dot{m}_{o} h_{o}}{\partial z}=\pi D_{o} \alpha_{o}\left(T_{w}-T_{o}\right)
$$

The heat transfer in the heat-exchanger wall is governed by the following form of the one-dimensional energy equation:

$$
(C \rho A)_{w} \frac{\partial T_{w}}{\partial t}=\pi D_{i} \alpha_{i}\left(T_{r}-T_{w}\right)+\pi D_{o} \alpha_{o}\left(T_{o}-T_{w}\right)
$$

The spatial dependence of (1)-(4) can be removed by integrating them along the axial coordinate for each of the three regions using Leibniz's Rule.

Therefore, the state space representation of the evaporator is given below:

$$
\dot{x}_{e v a}=D^{-1} f\left(x_{e v a}, u_{e v a}\right)
$$

where $x_{e v a}=\left[L_{1}, L_{2}, P, h_{a}, T_{w 1}, T_{w 2}, T_{w 3}, T_{u 1}, T_{u 2}, T_{u 3}\right]^{\mathrm{T}}$ are the system states, $u_{e v a}=\left[\dot{m}_{1}, h_{1}, \dot{m}_{u}, v_{u}, T_{u 1}\right]^{\mathrm{T}}$ is the control input. $f(\cdot, \cdot)$ and $D$ are defined as follows:

$$
f=\left[\begin{array}{c}
\dot{m}_{1}\left(h_{1}-h_{1}\right)+\alpha_{11} \pi D_{1} L_{1}\left(T_{w 1}-T_{v 1}\right) \\
\dot{m}_{1}\left(h_{1}-h_{g}\right)+\alpha_{12} \pi D_{1} L_{2}\left(T_{w 2}-T_{v 2}\right) \\
\dot{m}_{u}\left(h_{g}-h_{u}\right)+\alpha_{13} \pi D_{1} L_{3}\left(T_{u 3}-T_{v 3}\right) \\
\dot{m}_{1}-\dot{m}_{u} \\
\alpha_{11} \pi D_{1}\left(T_{v 1}-T_{u 1}\right)+\alpha_{u} \pi D_{u}\left(T_{u 1}-T_{u 1}\right) \\
\alpha_{12} \pi D_{1}\left(T_{v 2}-T_{w 2}\right)+\alpha_{u} \pi D_{u}\left(T_{u 2}-T_{u 2}\right) \\
\alpha_{13} \pi D_{1}\left(T_{v 3}-T_{w 3}\right)+\alpha_{u} \pi D_{u}\left(T_{u 3}-T_{u 3}\right) \\
\dot{m}_{u}\left(h_{u 2}-h_{u 2}\right)+\alpha_{u} \pi D_{u} L_{3}\left(T_{u 1}-T_{u 1}\right) \\
\dot{m}_{u}\left(h_{u 1}-h_{u 2}\right)+\alpha_{u} \pi D_{u} L_{3}\left(T_{u 2}-T_{u 2}\right) \\
\dot{m}_{u}\left(h_{u 1}-h_{u 1}\right)+\alpha_{u} \pi D_{u} L_{3}\left(T_{u 3}-T_{u 3}\right)
\end{array}\right]
$$

$D=\left[\begin{array}{cccccccccccc}d_{11} & 0 & d_{11} & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ d_{21} & d_{22} & d_{23} & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ d_{31} & d_{32} & d_{33} & d_{34} & 0 & 0 & 0 & 0 & 0 & 0 \\ d_{41} & d_{42} & d_{43} & d_{44} & 0 & 0 & 0 & 0 & 0 & 0 \\ d_{51} & 0 & 0 & 0 & d_{55} & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & d_{66} & 0 & 0 & 0 & 0 \\ d_{71} & d_{72} & 0 & 0 & 0 & 0 & d_{77} & 0 & 0 & 0 \\ d_{81} & 0 & 0 & 0 & 0 & 0 & 0 & d_{88} & 0 & 0 \\ d_{91} & d_{92} & 0 & 0 & 0 & 0 & 0 & 0 & d_{99} & 0 \\ d_{1001} & d_{1002} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & d_{1010} \end{array}\right]$
The elements in matrix $D$ are given in the appendix.
It is obvious from (5) that the quality of exhaust gas has influence on the temperature of working fluid at the outlet of evaporator, $T_{v h}$. The factors influencing the quality of exhaust gas considered in this paper are the temperature at the inlet of evaporator and the mass flow rate of exhaust gas. And these disturbances are not necessarily Gaussian in real ORC process.

Here, the temperature of working fluid at the outlet of the evaporator is regulated by manipulating the speed of the pump. According to (5), the discretized ARMAX model of the superheated vapour temperature in ORC processes can be formulated as:

$$
y_{k}=F\left(y_{k-1}, \cdots, y_{k-n}, u_{k}, u_{k-1}, \cdots, u_{k-m}, \xi_{k}\right)
$$

where $y_{k}$ is the superheated vapor temperature $\left(T_{v h}\right), u_{k}$ the speed of the pump $(\omega), \xi_{k}=\left[\begin{array}{ll}\xi_{1 k} & \xi_{2 k}\end{array}\right]^{T}$ is the external nonGaussian disturbance vector, where $\xi_{1 k}$ and $\xi_{2 k}$ represent the disturbances imposed on the flow velocity and the temperature of exhaust, respectively. $F()$ is a known nonlinear function that represents the system dynamics.
B. Performance Index Functions

For the given target superheated vapor temperature $r_{k}$, the temperature error can be denoted as

$$
e_{k}=r_{k}-y_{k}
$$

Due to the non-Gaussianity of the flow velocity and the temperature of exhaust, the tracking error $e_{k}$ is also a nonGaussian random variable. The aim of this paper is to determine the speed of the pump $u_{k}$ such that $e_{k}$ approaches to zero as close as possible with a small randomness. Therefore the first objective is to minimize the squared mean error, which can be expressed as

$$
J_{1}\left(u_{k}\right)=\left(r_{k}-E\left(y_{k}\right)\right)^{2}
$$

Moreover, the second objective is to minimize the process variability caused by the non-Gaussian random disturbances. In this paper, quadratic Renyi's entropy of system output is used as a measure of uncertainty:

$$
J_{2}\left(u_{k}\right)=-\ln \int \gamma_{r_{k}}^{2}\left(u_{k}, x\right) d x
$$

where $\gamma_{r_{k}}\left(u_{k}, x\right)$ is the probability density function (PDF) of output $y_{k}$, which can be estimated using the on-line measurement data. Suppose that we have $N$ independent and identically distributed samples $\left\{y_{k}^{1}, y_{k}^{2}, \cdots, y_{k}^{N}\right\}$, then $\gamma_{r_{k}}$ can be estimated by the well-known Kernel Density Estimation method from the samples using an Gaussian Kernel function $\mathrm{K}_{\sigma}$, which are presented as follows:

$$
\hat{\gamma}_{r_{k}}(x)=\frac{1}{N \sigma} \sum_{i=1}^{N} \mathrm{~K}\left(\frac{x-y_{k}^{i}}{\sigma}\right)
$$

where $\sigma$ is the kernel size or bandwidth parameter. Consider the definition of quadratic Renyi's entropy, which can also be written using an expectation operator as:

$$
H\left(y_{k}\right)=-\ln \int \gamma_{r_{k}}^{2}(x) d x=-\ln E\left[\gamma_{r_{k}}(x)\right]
$$

Approximating the expectation operator with the sample mean as it is commonly done in density estimation, it can be obtained that

$$
H\left(y_{k}\right) \approx-\ln \frac{1}{N} \sum_{i=1}^{N} \gamma_{r_{k}}\left(y_{k}^{j}\right)
$$

Substituting the Parzen window estimator of PDF (10) in (12), and rearranging terms, the nonparametric estimator for quadratic Renyi's entropy can be formulated to give

$$
H\left(y_{k}\right)=-\ln \frac{1}{N} \sum_{i=1}^{N}\left(\sum_{i=1}^{N} \mathrm{~K}_{\sigma}\left(y_{k}^{j}-y_{k}^{i}\right)\right)
$$

This means that the system output entropy objective function has the following form:

$$
J_{2}=-\ln \frac{1}{N} \sum_{i=1}^{N}\left(\sum_{i=1}^{N} \mathrm{~K}_{\sigma}\left(y_{k}^{j}-y_{k}^{i}\right)\right)
$$

At the same time, the mean value of the system output can be expressed as

$$
E\left(y_{k}\right)=\frac{1}{N} \sum_{i=1}^{N} y_{k}^{i}
$$

Therefore, the task of this paper is to find appropriate $u_{k}$ so that the following multi-objective cost function is minimized:

$$
J\left(u_{k}^{*}\right)=\min _{u_{k}}\left\{J_{1}, J_{2}\right\}
$$

where $J_{1}$ and $J_{2}$ are defined in (8) and (9), respectively. In the next section, a numerical solution based on estimation of distribution algorithm is proposed for solving (16).

## III. Multi-Objective Estimation of Distribution Algorithm

Since the objective functions are usually nonlinear, nonsmooth and even non-differentiable, it is difficult to find the optimal solutions to the multi-objective optimization problem analytically. Therefore, many evolutionary optimal methods have been well investigated, such as multi-objective genetic algorithm, niched Pareto genetic algorithm (NPGA), nondominated sorting genetic algorithm, strength Pareto evolutionary algorithm (SPEA), Pareto-frontier Differential Evolution (PDE) algorithm, and so on. In this paper, Estimation of distribution algorithm (EDA), sometimes called probabilistic model-building genetic algorithms (PMBGA), is adopted to obtain the optimal control inputs. This algorithm is a stochastic optimization method that guides the search for the optimum by building and sampling explicit probabilistic models of promising candidate solutions.
Denote $u_{k}=u_{k-1}+\Delta u_{k}$, the EDA method is used to find the optimal $\Delta u_{k}$ by minimizing $J_{1}$ and $J_{2}$ simultaneously. The algorithm consists of four main stages, namely, initialization, modelling, reproduction and selection, which are briefly presented as follows. The initial population is chosen randomly to span the initial boundary of decision variable $\Delta u_{k}$ according to the uniform distribution:

$$
P_{G=0}=\left\{\Delta u_{k, G=0}^{1}, \cdots, \Delta u_{k, G=0}^{N}\right\}
$$

where $N$ is the total number of populations. By using the non-domination sorting selection method, the Pareto optimal solutions can be obtained. Choose the probability density function of these solutions as the probability model of the EDA. Generate a new set $Q=\left\{\Delta u_{k, G=t}^{1}, \Delta u_{k, G=t}^{N}, \cdots, \Delta u_{k, G=t}^{N}\right\}$ with $N$ random numbers according to the established model. Select $N$ optimal individuals from $Q \cup P_{G=t}$ to create $P_{G=t+1}$ according to the following principles:

1) Use the fast non-dominated sorting approach to establish the partial ordering relation of population $Q\left[\bigsqcup \operatorname{Pop}(t): J^{1} \succ J^{2} \succ \cdots \succ J^{l} .\right.$ Denote $\operatorname{Pop}(t+1)=\varnothing$, and $\quad \operatorname{Pop}(t+1)=\operatorname{Pop}(t+1)\left(\bigsqcup J^{n} \quad, \quad n=1,2, \cdots, l \quad\right.$ until $\|(\operatorname{Pop}(t+1)) \mid>N$.
2) If $\|(\operatorname{Pop}(t+1)) \mid>N$, for all the members in $\operatorname{Pop}(t+1) \cap J^{n}$, compute their crowding distances using the following equation:

$$
\begin{aligned}
d\left[\Delta u_{k, G=t+1}^{l}\right]= & \left|J_{1}\left[\Delta u_{k, G=t+1}^{l+1}\right]-J_{1}\left[\Delta u_{k, G=t+1}^{l-1}\right]\right| \\
& +\left|J_{2}\left[\Delta u_{k, G=t+1}^{l+1}\right]-J_{2}\left[\Delta u_{k, G=t+1}^{l-1}\right]\right|
\end{aligned}
$$

Remove the element in $\operatorname{Pop}(t+1) \cap J^{n}$ with the smallest crowding distance from $\operatorname{Pop}(t+1)$. In the case when there are more than one member with the smallest crowding distance, randomly choose one and remove it.
The EDA for problem (16) at instant $k$ can be summarized as follows:
Step 1 Initialization: Given $u_{k-1}$ and set $t:=0$. Generate an initial population $P_{G=0}=\left\{\Delta u_{k, G=0}^{1}, \cdots, \Delta u_{k, G=0}^{N}\right\}$ and compute the $J$ -value of each individual solution $\left(J\left(u_{k}^{1}\right), J\left(u_{k}^{2}\right), \cdots, J\left(u_{k}^{N}\right)\right)$ in $P_{G=0}$.
Step 2 Modelling: Build the probability model of the Pareto optimal solutions in generation $P_{G=t}$.
Step 3 Reproduction: Generate a new solution set $Q$ according to the model established in Step 2. Evaluate the $J$ value of each solution in $Q$.
Step 4 Selection: Select $N$ individuals from $Q \cup P_{G=t}$ to create $P_{G=t+1}$.
Step 5 Set $t=t+1$ and go to Step 2.
In the next section, a simulation study is proposed to demonstrate the effectiveness of the method.

## IV. Simulation Results

In this section, the proposed MOEDA is applied to control the temperature at evaporator outlet in ORC systems.

To solve the multi-objective cost function (16) for $u_{k}$, a MOEDA with population size 300, maximum algorithm iterations 300 and the sampling period $T_{s}=0.5 \mathrm{~s}$ is used here. The ORC process operates at a steady state before 40 s , the target superheated vapor temperature increases from $137.6^{\circ} \mathrm{C}$ to $142.8^{\circ} \mathrm{C}$ at 40 s and lasts forever.

The response of the superheated vapor temperature is shown in Fig. 3, it can be seen that the proposed approach can stabilize the superheated vapor temperature around the target value with small oscillation. In this multi-objective optimal control problem, the control input (the pump speed) chosen must minimize both objective functions simultaneously. At each instant, MOEDA finds optimal solutions belonging to the Pareto front. Fig 4 illustrates the Pareto front found at the end of 300 iterations. Moreover, the individual objective functions are examined to verify the effectiveness of the method. Firstly, the minimization of the tracking error can be shown in Fig. 3. For the second objective function, PDFs of the tracking error are presented in Fig. 5 and 6. It can be seen that the shape of the PDFs of tracking error become narrower and sharper along with sampling time, which indicates that the proposed controller can efficiently decrease the uncertainties of the tracking errors.

The above simulation results demonstrate that the superheated vapor temperature can be kept within admissible

limits when the system is subject to non-Gaussian disturbances coming from mass flow rate and temperature of exhaust gas.
![img-4.jpeg](img-4.jpeg)

Fig. 3 Response of the superheated vapor temperature
![img-5.jpeg](img-5.jpeg)

Fig. 4 Pareto front
![img-4.jpeg](img-4.jpeg)

Fig. 5 PDF of error
![img-5.jpeg](img-5.jpeg)

Fig. 6 PDFs at typical instants

## V. CONCLUSIONS

In this paper, Multi-Objective Estimation of Distribution Algorithm (MOEDA) is proposed for regulating the superheated vapor temperature in ORC systems with nonGaussian heat source temperature and mass flow rate. Existing temperature control methods have not considered the effect of random variations in ORC processes. The main purpose of this paper is to control the speed of the pump so that the superheated vapor temperature follows a target one with small randomness. Therefore, two objective functions are formulated both from magnitude and randomness perspective. And the controller is tuned so that two objectives, namely the squared mean value of tracking error and the entropy of the superheated vapor temperature, are minimized simultaneously. Since the multi-objective optimization problem is highly nonlinear, an evolutionary method based on MOEDA is used to find the global solutions to the temperature control problem. Simulation results illustrate the effectiveness of the proposed approach.

## APPENDIX

$d_{11}=\frac{h_{i}-h_{i}}{2} A \rho_{i}$
$d_{13}=A L_{3}\left(\frac{\rho_{2}}{2} \frac{d h_{i}}{d P}-1\right)$
$d_{21}=-A \rho_{i}\left(h_{g}-h_{i}\right)$
$d_{22}=-A(1-\bar{\gamma}) \rho_{i}\left(h_{g}-h_{i}\right)$
$d_{23}=A L_{2}\left[-\left(1-\bar{\gamma}\right) \frac{d \rho_{i}\left(h_{g}-h_{i}\right)}{d P}+\rho_{2} \frac{d h_{g}}{d P}-1\right]$
$d_{31}=-\frac{1}{2} A\left(h_{a}-h_{g}\right) \rho_{3}$
$d_{32}=-\frac{1}{2} A\left(h_{a}-h_{g}\right) \rho_{3}$
$d_{33}=A L_{3}\left[\frac{\rho_{2}}{2} \frac{d h_{g}}{d P}+\frac{1}{2}\left(h_{a}-h_{g}\right) \frac{\partial \rho_{3}}{\partial P}-1\right]$
$d_{34}=A L_{3}\left[\frac{\rho_{3}}{2}+\frac{1}{2}\left(h_{a}-h_{g}\right) \frac{\partial \rho_{3}}{\partial h_{a}}\right]$
$d_{41}=A\left(\rho_{i}-\rho_{s}\right)$
$d_{42}=A\left(\rho_{2}-\rho_{s}\right)$
$d_{43}=A L_{3} \frac{\partial \rho_{3}}{\partial P}+A L_{2} \frac{d \rho_{2}}{d P}$
$d_{44}=A L_{3} \frac{\partial \rho_{3}}{\partial h_{a}}$
$d_{51}=(C \rho A)_{\mathrm{w}} \frac{T_{w 3}-T_{w 2}}{L_{3}}$
$d_{53}=(C \rho A)_{\mathrm{w}}$
$d_{66}=(C \rho A)_{\mathrm{w}}$
$d_{71}=(C \rho A)_{\mathrm{w}} \frac{T_{w 2}-T_{w 3}}{L_{3}}$
$d_{72}=(C \rho A)_{\mathrm{w}} \frac{T_{w 2}-T_{w 3}}{L_{3}}$
$d_{77}=(C \rho A)_{\mathrm{w}}$
$d_{81}=A_{a} \rho_{a} \frac{h_{a a}-h_{a 2}}{2}$
$d_{88}=(C \rho A)_{a} L_{1}$
$d_{91}=-A_{a} \rho_{a}\left(h_{a 1}-h_{a 2}\right)$
$d_{92}=A_{a} \rho_{a} \frac{h_{a 2}-h_{a 1}}{2}$
$d_{99}=(C \rho A)_{a} L_{2}$
$d_{1001}=-A_{a} \rho_{a} \frac{h_{a}-h_{a 1}}{2}$
$d_{1002}=-A_{a} \rho_{a} \frac{h_{a}-h_{a 1}}{2}$
$d_{1010}=\frac{1}{2}(C \rho A)_{a}$