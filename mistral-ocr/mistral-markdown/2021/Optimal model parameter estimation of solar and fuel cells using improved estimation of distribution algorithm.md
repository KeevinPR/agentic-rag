# Unit 

## Electrical Engineering

## Optimal model parameter estimation of solar and fuel cells using improved estimation of distribution algorithm

Benin Pratap Chandran ${ }^{\mathrm{a}, \mathrm{e}}$, A. Immanuel Selvakumar ${ }^{\mathrm{a}}$, G. Shine Let ${ }^{\mathrm{b}}$, S. Paul Sathiyan ${ }^{\mathrm{a}}$<br>*Department of EEE, Karunya Institute of Technology and Sciences, Coimbatore 641114, India<br>${ }^{\mathrm{b}}$ Department of ECE, Karunya Institute of Technology and Sciences, Coimbatore 641114, India

## A R T I C L E I N F O

## Article history:

Received 8 April 2020
Revised 11 June 2020
Accepted 26 July 2020
Available online 13 November 2020

## Keywords:

Solar cell
Fuel cell
Estimation of distribution algorithm
Optimization
Parameter estimation

## A B S T R A C T

Renewable energy through the use of fuel cells and solar cells is one of the popular developments in recent days that produce electricity. Accurate modelling of fuel cell and solar cells are essential in simulation and analysis of energy systems with these sources. However, the systems are extremely nonlinear and complicated. The model needs to be optimized under distinct operating circumstances. Enhanced and streamlined Improved Estimation of Distribution (IED) Algorithm is suggested in this paper to estimate the parameter through optimization for solar cell models and fuel cell models. This is accomplished through the introduction of an ideal approach to improve population quality and the use of a local search to improve the efficiency of the finest global solution further. The design of an IED algorithm is much more straightforward and search efficiency is greatly improved compared with the fundamental optimization techniques from the literature.
(c) 2020 The Authors. Published by Elsevier B.V. on behalf of Faculty of Engineering, Ain Shams University. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

## 1. Introduction

The keyphrase 'Green Energy Technology' attracted many world-wide scientists, researchers to develop/create electricity and fuel from the natural resources without pollution. Stringent environmental legislation and energy incentives were introduced around the world to encourage development and use of renewable energy resources, such as wind, solar energy, fuel cell, wave as well as other energy resources, to meet demands for sustainable energy production and to sustain environment [1]. Fuel cells and solar panels attracted a lot of attraction among multiple techniques to produce effective and clean electricity [2]. One of the most common fuel cell with many preferred properties, such as low working temperature, low noise, zero emission, increased lifespan, high power density, is a Polymer Electrolyte Membrane (PEM) [3,4].

[^0]For ion exchange purpose, proton is used for conduction; hence polymer electrolyte membrane fuel cell is also called as proton exchange membrane fuel cell. The solar cell (photovoltaic cell) transforms light energy into electric energy. Photovoltaic (PV) effect is called the method of transforming light energy to electrical energy [5]. The datasheets of solar cell provided by the manufacturer lacks several essential parameters required in mathematical modelling of the device [6]. Moreover the current and the voltage characteristics are highly nonlinear [7]. The accurate measurement of model parameters is of key importance in the modeling of PV systems $[8,9,10]$.

Various analytical and optimization strategies are employed to estimate solar cell and fuel cell model parameters. Analytical model uses mathematical equations and the equations are solved to estimate the model parameters, based on the data sheet provided by the manufacturer. Since there is much variation in temperature levels, the mathematical models are not able to predict the accurate voltage, current and power values. This problem has been solved using the meta-heuristic algorithms (MHAs) during the past years. The existence of non-linearity in the problem brought unsatisfactory results. Different heuristic algorithms used to estimate the PV single diode model, double diode model and fuel cell model are genetic algorithm (GA), particle swarm optimization (PSO), differential evolution (DE), artificial bee colony (ABC), Global-best Harmony Search algorithm (GHS), Regenerate genetic algorithm (GHA), teaching-learning based optimization (TLBO),

[^1]
[^0]:    * Corresponding author at: Department of EEE, Karunya Institute of Technology and Sciences, Coimbatore 641114, India.
    E-mail addresses: benin@karunya.edu (B. Pratap Chandran), immanuel@karunya.edu (A. Immanuel Selvakumar), shinelet@ gmail.com (G. Shine Let), sathiyan@ karunya.edu (S. Paul Sathiyan).
    Peer review under responsibility of Ain Shams University.

[^1]:    https://doi.org/10.1016/j.asej.2020.07.034
    2090-4479/© 2020 The Authors. Published by Elsevier B.V. on behalf of Faculty of Engineering, Ain Shams University.
    This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

Neural Network Algorithm (NNA) [11], Manta Rays Foraging Optimizer (MRFO) [12], etc. A Biogeography-based Heterogeneous Cuckoo Search (BHCS) algorithm has been proposed by Chen et al. to improvise the parameter estimation in solar photovoltaic models [3]. An Elite Opposition-based Jaya (EO-Jaya) algorithm based on swarm intelligence has been studied and discussed by wang et al. EO-Jaya algorithm has been tested by finding model parameters of a real PV cell [13]. Whale optimization and improved whale optimization is proposed in 2016 and 2018 respectively based on the hunting behaviour of whales, to estimate the solar cell and fuel cell model parameters [14], [15], [16]. To estimate the parameters of three-diode model of solar cell, different metaheuristics algorithms considered are sunflower optimization algorithm [17], Grasshopper Optimization Algorithm [18], Coyote optimization algorithm [19], Transient search optimization algorithm [20], Harris Hawks Optimization algorithm [21], etc. Latifa Sabri et al. suggested Cross Entropy Optimization (CEO) Algorithm to estimate the parameters of double diode model of solar cell [22]. In CEO algorithm, the mean and standard deviations are smoothened in each iteration and used to generate new set of populations. In IED algorithm, the mean and standard deviations are not smoothened in each iteration and the raw values are used generate new set of populations. The basic parameter estimation flow diagram is shown in Fig. 1.

In the proposed work, Improved Estimation of Distribution (IED) algorithm is used for extracting the parameters of various PV models and PEM fuel cell. The basic output of the IED algorithm is calculated by probability in the whole population [23]. The details of IED and the incorporation of IED algorithm for the estimation of solar and fuel cell model parameters are discussed in detail in the following sections.

## 2. Solar cell as diode modelling

The concept of solar cells describes how light energy is transformed into electrical current in photons when they hit an appropriate semi-conductor. The theoretical studies are useful because they foretell the basic limitations of a solar cell and provide direction on the phenomenon that contribute to solar cell efficiency and loss. To comprehend the solar cell's electrical behavior, it is helpful to build a model centered on separate optimal electrical parts with well-specified behavior. In parallel with the diode, the solar cell model should have a current source. The shunt resistance and
![img-0.jpeg](img-0.jpeg)

Fig. 1. Parameter Evaluation Flow Diagram.
series resistance are also added with the design. Initially, two diodes are considered beforehand of series and shunt resistances and is called as double diode modelling. The two diode modelling is simplified in the single diode modelling of Solar cell.

### 2.1. Double diode model

Modelling of the solar cell is by connecting two diodes in parallel with a series $\left(\mathrm{R}_{\mathrm{s}}\right)$ and shunt $\left(\mathrm{R}_{\mathrm{sh}}\right)$ resistors is the most common way of representing a double diode model of solar cell and is shown in Fig. 2. Metal contact and the bulk resistance of the semiconductor material is represented with series resistance. The terminal current $\left(I_{C}\right)$ in double diode model is based on the solar induced current $\left(I_{y h}\right)$, diode currents $\left(I_{D 1}, I_{D 2}\right)$ and the current through shunt resistor $\left(I_{s h}\right)$ and is represented by Eq. (1).
$I_{c}=I_{y h}+I_{D 1}+I_{D 2}+I_{s h}$
The two diode currents $\left(I_{D 1}, I_{D 2}\right)$ and current through shunt resistor $\left(\mathrm{I}_{\mathrm{sh}}\right)$ are given by Eqs. (2)-(4) respectively.
$I_{D 1}=I_{S A 1}\left\{\exp \left(\frac{q\left(V_{c}+I_{1} R_{s}\right)}{n_{1} k T}\right)-1\right\}$
$I_{D 2}=I_{S A 2}\left\{\exp \left(\frac{q\left(V_{c}+I_{1} R_{s}\right)}{n_{2} k T}\right)-1\right\}$
$I_{s h}=\frac{V_{c}+I_{1} R_{s}}{R_{s h}}$
The set of model parameters to be found using double diode model are based on series resistor $\left(\mathrm{R}_{\mathrm{s}}\right)$, shunt resistor $\left(\mathrm{R}_{\mathrm{sh}}\right)$, solar induced current $\left(\mathrm{I}_{\mathrm{gh}}\right)$, two diodes saturation currents $\left(\mathrm{I}_{\mathrm{S} A 1}, \mathrm{I}_{\mathrm{S} A 2}\right)$ and ideality constant of diodes $\left(n_{1}, n_{2}\right)$. This is given by: $X=\left\{\mathrm{R}_{\mathrm{s}}, \mathrm{R}_{\mathrm{sh}}, \mathrm{I}_{\mathrm{ph}}, \mathrm{I}_{\mathrm{S} A 1}, \mathrm{I}_{\mathrm{S} A 2}, \mathrm{n}_{1}, \mathrm{n}_{2}\right\}$.

### 2.2. Single diode model

The simplified version of the double diode model with a single diode is shown in Fig. 3.

The single diode model terminal current $\left(I_{c}\right)$, diode current $\left(I_{D}\right)$ and current through shunt resistance $\left(I_{s h}\right)$ are given by Eqs. (5)-(7).
$I_{c}=I_{y h}-I_{D}-I_{s h}$
$I_{D}=I_{S A}\left\{\exp \left(\frac{q\left(V_{c}+I_{1} R_{S}\right)}{n k T}\right)-1\right\}$
$I_{s h}=\frac{V_{c}+I_{1} R_{S}}{R_{s h}}$
The set of model parameters to be determined using single diode model are $X=\left\{\mathrm{R}_{\mathrm{s}}, \mathrm{R}_{\mathrm{sh}}, \mathrm{I}_{\mathrm{ph}}, \mathrm{I}_{\mathrm{S} A}, \mathrm{n}\right\}$
![img-1.jpeg](img-1.jpeg)

Fig. 2. Double Diode model.

![img-4.jpeg](img-4.jpeg)

Fig. 3. Single Diode model.

### 2.3. Objective function

The error value between the measured and the simulated current for double diode modelling is obtained by the objective function $\left(\mathrm{F}_{\text {sc-DD }}\right)$ given by Eq. (8).
$F_{\text {SC-DD }}=\sqrt{\frac{1}{N} \sum_{i=1}^{N}\left(f\left(V_{i}, I_{i}, x\right)-I_{i}\right)^{2}}$
The variable ' N ' is the number of solar cell, ' $V_{i}$ ' is the experimental voltage and ' $I i$ ' is the experimental current. The function $f\left(V_{i}, I_{i}, x\right)$ is given by Eq. (9).
$f\left(V_{i}, I_{i}, x\right)=I_{p h}-I_{D 1}-I_{D 2}-I_{t h}$
For single diode modelling, Eq. (8) objective function $\left(F_{S C-D D}\right)$ is used to calculate the error value, in which $f\left(V_{i}, I_{i}, x\right)=I_{p h}-I_{D}-I_{t h}$. The error of the proposed model obtained should be less to have higher accuracy.

## 3. Fuel cell modelling

Electrochemical energy conversion is obtained by using fuel cell. Electricity is generated and widely used in automobile applications during the energy conversion process [24]. Based on the electrolyte used, different types of fuel cells are Polymer Electrolyte Membrane (PEM) fuel cell, direct methanol fuel cell, molten carbonate fuel cell, alkaline fuel cells, etc. Due to its high power density, low weight / volume and high power to weight ratio, for vehicle applications PEM fuel cell is widely used [25]. PEM Fuel cell operated under diverse conditions such as different fuel mixeres, temperatures and humidity levels [26]. Modelling of PEM Fuel cell involves modelling of all three process namely electric, chemical and thermal process. The Model should make correct assumptions of numerical parameters [27]. The literature shows that the accu-
![img-3.jpeg](img-3.jpeg)

Fig. 4. Process of the PEM Fuel Cell.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Flow Diagram of IED Algorithm.

Table 1
Convergence analysis of different algorithm.

| Average Iterations to Converge into 0.001 Boundary |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| IED | ED | BBO-M | DE | ABSO | PS | SA |
| 82 | 93 | 87 | 98 | 96 | Not Able to Reach | Not Able to Reach |

racy is reduced with computational efficiency [28]. The process of PEM fuel cell is shown in Fig. 4 [29].

The mathematical equation used to govern the terminal voltage of PEM fuel cell obtained from the literatures [1], [2] and is given by Eq. (10).
$V_{c}=\left(E_{\text {Nernst }}-V_{\text {act }}-V_{\text {ohmic }}-V_{\text {con }}\right) \times N_{S}$
$E_{\text {Nernst }}, V_{\text {act }}, V_{\text {ohmic }}$ and $V_{\text {con }}$ are the reversible open circuit voltage, activation voltage loss by the anode and cathode activation, ohmic voltage loss by the resistance of protons through the exchange membrane, and concentration voltage loss from the transport of hydrogen and oxygen respectively. $\mathrm{N}_{\mathrm{s}}$ represents the number of fuel cells in the stack.

### 3.1. Objective function

The minimum error between terminal voltages of the PEM fuel cell is obtained by the objective function $\left(\mathrm{F}_{\mathrm{SC}}\right)$ given in Eq. (11). The definite figures from the datasheet V-I characteristics and the simulated results are compared, and error is minimised.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Convergence Curve of ED and IED algorithms.

Table 2
Solar cell-parameter values.

| Parameter | $\mathrm{R}_{\mathrm{s}}(\Omega)$ | $\mathrm{R}_{\mathrm{sh}}(\Omega)$ | $\mathrm{I}_{\mathrm{ph}}(\mathrm{A})$ | $\mathrm{I}_{\mathrm{SA}}(\mu \mathrm{A})$ | N |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Lower | 0 | 0 | 0 | 0 | 1 |
| Upper | 0.5 | 100 | 1 | 1 | 2 |

$F_{j c}=\min _{\left(\epsilon_{1}, \epsilon_{2}, \epsilon_{3}, \epsilon_{4}, \lambda, R_{c}, b\right)}\left(\sum_{i=1}^{N} \sum_{j=1}^{M}\left(V_{\text {actual }}-V_{c}\right)^{2}\right)$
The $\epsilon_{1}, \epsilon_{2}, \epsilon_{3}, \epsilon_{4}$ are parametric coefficients of the fuel cell, ' $\lambda$ ' is the parameter representing anode gas, ' $R_{s}$ ' represents contact resistance in ohms and ' $b$ ' indicates the concentration loss constant in volt.

## 4. Proposed IED algorithm

The general idea of IED algorithm is, finding better solution of an optimization problem from the estimated probability distribution of the good solutions found so far. The IED algorithm for model parameter estimation of solar PV cell and fuel cell is given below:

Step 1: Let X be the set of model parameters to be found out.
$X=\left\{\mathrm{R}_{\mathrm{s}}, \mathrm{R}_{\mathrm{sh}}, \mathrm{I}_{\mathrm{ph}}, \mathrm{I}_{\mathrm{SA} 1}, \mathrm{I}_{\mathrm{SA} 2}, \mathrm{n}_{1}, \mathrm{n}_{2}\right\}$ for Solar PV-Double Diode modelling
$X=\left\{\mathrm{R}_{\mathrm{s}}, \mathrm{R}_{\mathrm{sh}}, \mathrm{I}_{\mathrm{ph}}, \mathrm{I}_{\mathrm{SA}}, \mathrm{n}\right\}$ for Solar PV-Single Diode modelling
$X=\left\{\epsilon_{1}, \epsilon_{2}, \epsilon_{3}, \epsilon_{4}, \lambda, R_{C}, b\right\}$ for Fuel cell
Step 2: Let ' $m$ ' be the population size and ' $n$ ' be the number of model parameters.

Step 3: Generate initial population with uniform distribution within the limits as given in Eq. (12)
$X_{\text {initialization }}=\left[\begin{array}{cccc}x_{11} & x_{12} & \ldots & x_{1 m} \\ x_{21} & x_{22} & & x_{2 m} \\ \vdots & \ddots & \vdots \\ x_{n 1} & x_{n 2} & \cdots & x_{n m}\end{array}\right]$
Step 4: Evaluate the objective function of solar PV and fuel cell.

Table 4
Calculated error - double diode model.

| Benchmark Data [2] | $\mathrm{I}_{\mathrm{c}}(\mathrm{A})$ | Error $\left(\boldsymbol{F}_{\boldsymbol{X} \cdot \boldsymbol{0} \boldsymbol{0}}\right.$ ) |
| :-- | :-- | :-- |
| $\mathrm{V}_{\mathrm{f}}(\mathrm{V})$ | $\mathrm{I}_{\mathrm{c}}(\mathrm{A})$ |  |
| -0.2057 | 0.764 | 0.764058951 |
| -0.1291 | 0.762 | 0.762668723 |
| -0.0588 | 0.7605 | 0.761392353 |
| 0.0057 | 0.7605 | 0.760219413 |
| 0.0646 | 0.76 | 0.75914538 |
| 0.1185 | 0.759 | 0.758152581 |
| 0.1678 | 0.757 | 0.757215199 |
| 0.2132 | 0.757 | 0.756268435 |
| 0.2545 | 0.7555 | 0.755204231 |
| 0.2924 | 0.754 | 0.753756051 |
| 0.3269 | 0.7505 | 0.751444216 |
| 0.3585 | 0.7465 | 0.747361486 |
| 0.3873 | 0.7385 | 0.740086928 |
| 0.4137 | 0.728 | 0.727338971 |
| 0.4373 | 0.7065 | 0.706956785 |
| 0.459 | 0.6755 | 0.675335092 |
| 0.4784 | 0.632 | 0.630914022 |
| 0.496 | 0.573 | 0.572195159 |
| 0.5119 | 0.499 | 0.499975591 |
| 0.5265 | 0.413 | 0.414096445 |
| 0.5398 | 0.3165 | 0.31801773 |
| 0.5521 | 0.212 | 0.212712198 |
| 0.5633 | 0.1335 | 0.102865319 |
| 0.5736 | -0.01 | -0.008000921 |
| 0.5833 | -0.123 | -0.124671289 |
| 0.59 | -0.21 | -0.207475425 |

Table 5
Calculated error - single diode model.

| Benchmark Data [2] | $\mathrm{I}_{\mathrm{c}}(\mathrm{A})$ | Error $\left(\boldsymbol{F}_{\boldsymbol{X} \cdot \boldsymbol{0} \boldsymbol{0}}\right.$ ) |
| :-- | :-- | :-- |
| $\mathrm{V}_{\mathrm{f}}(\mathrm{V})$ | $\mathrm{I}_{\mathrm{c}}(\mathrm{A})$ |  |
| -0.2057 | 0.764 | 0.764090757 |
| -0.1291 | 0.762 | 0.762664281 |
| -0.0588 | 0.7605 | 0.761354796 |
| 0.0057 | 0.7605 | 0.760151913 |
| 0.0646 | 0.76 | 0.759051697 |
| 0.1185 | 0.759 | 0.758037509 |
| 0.1678 | 0.757 | 0.757085577 |
| 0.2132 | 0.757 | 0.75613407 |
| 0.2545 | 0.7555 | 0.755078319 |
| 0.2924 | 0.754 | 0.753653892 |
| 0.3269 | 0.7505 | 0.751379253 |
| 0.3585 | 0.7465 | 0.747340016 |
| 0.3873 | 0.7385 | 0.740100966 |
| 0.4137 | 0.728 | 0.727363683 |
| 0.4373 | 0.7065 | 0.706952823 |
| 0.459 | 0.6755 | 0.675261225 |
| 0.4784 | 0.632 | 0.630743468 |
| 0.496 | 0.573 | 0.571921132 |
| 0.5119 | 0.499 | 0.499609875 |
| 0.5265 | 0.413 | 0.413663022 |
| 0.5398 | 0.3165 | 0.317534334 |
| 0.5521 | 0.212 | 0.212185804 |
| 0.5633 | 0.1335 | 0.102283227 |
| 0.5736 | -0.01 | -0.008692791 |
| 0.5833 | -0.123 | -0.125496253 |
| 0.59 | -0.21 | -0.208478774 |

Error $\left(\boldsymbol{F}_{\boldsymbol{X} \cdot \boldsymbol{0} \boldsymbol{0}}\right.$ )
$\begin{array}{llllll}\text { (12) } & & & & \\ & \text { Step } 4: \text { Evaluate the objective function of solar PV and fuel cell. } & & \text { (12) }\end{array}$

Step 3
PEM fuel cell-parameter values.

| Parameter | $\mathbf{e}_{1}$ | $\mathbf{e}_{2}$ | $\mathbf{e}_{3}$ | $\mathbf{e}_{4}$ | $\lambda$ | $\mathrm{R}_{\mathrm{c}}$ | b |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Range1, min | -1.19969 | 0.001 | 3.60E-05 | -2.60E-04 | 10 | 0.0001 | 0.0136 |
| Range1, max | -0.8532 | 0.005 | 9.80E-05 | -9.54E-05 | 24 | 0.0008 | 0.5 |
| Range2, min | -0.952 | 0.001 | 7.40E-05 | -1.98E-04 | 14 | 0.0001 | 0.016 |
| Range2, max | -0.944 | 0.005 | 7.80E-05 | -1.88E-04 | 23 | 0.0008 | 0.5 |

![img-6.jpeg](img-6.jpeg)

Fig. 7. Double Diode model (a) I-V Characteristics (b) P-V Characteristics.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Single Diode model (a) I-V Characteristics (b) P-V Characteristics.

Step 5: Select the top m' (where $\mathrm{m}^{\prime}=10 \%$ of m) population member from $X_{\text {restritization. }}$ Calculate the mean and standard deviation of these members.

Step 6: Based on the mean and standard deviation generate as new set of ' $m$ ' population members.

Step 7: Repeat this process, until the stopping criterion is met.
In the proposed IED algorithm, in order to speedup the convergence, the standard deviation is modified in each iteration is calculated bassed on Eq. (13).
$\sigma_{\text {modified }}=\sigma_{\text {estimation }}\left(1-\frac{\text { iteration }}{\text { iterationmaximum }}\right)$
The flow diagram for the proposed IED algorithm is shown in Fig. 5.

To test the convergence ability of the proposed IED algorithm, double diode parameter optimization problem is taken into consideration. All the algorithms are made to run for 100 iterations with a population size of 50 . To have a fair comparison, the algorithms are executed for 50 trials. In each trial, the number of iterations to minimize the objective function below 0.001 has been observed. Average iterations for 50 trials are calculated and the rounded
values are illustrated in Table. 1. When compared to all the other algorithm, IED algorithm took less number of iterations to reach the convergence boundary. The convergence characteristics of ED and IED algorithms are displayed in Fig. 6. IED algorithm exhibits better convergence characteristic than Estimation of Distribution (ED) algorithm.

## 5. Parameter estimation and results

In this subdivision, the effectiveness of the IED algorithm is verified by estimating the double diode model, single diode model, and fuel cell model parameters. Based on the estimated parameters, current-voltage (I-V) characteristics are obtained. I-V values are compared with benchmark experimental I-V data. For the proposed IED algorithm, upper and lower limit for the parameters to be estimated is given as input. Table 2 gives the values considered for solar cell modelling [2]. Table 3 provides the parameters considered for PEM fuel cell modelling.

The terminal current ( $\mathrm{L}_{\mathrm{t}}$ ) is determined to demonstrate the efficiency of the proposed IED algorithm. Relative error (Error) is calculated by taking difference between the benchmark experimental

Table 6
Double diode model parameter estimation-comparison.

| Parameters | IED (Proposed) | BBO-M [2] | DE [30] | ABSO [31] | PS [32] | SA [33] |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $\mathrm{R}_{\mathrm{t}}(\Omega)$ | 0.03664 | 0.03664 | 0.03661 | 0.03657 | 0.032 | 0.0345 |
| $\mathrm{R}_{\text {th }}(\Omega)$ | 55.0494 | 55.0494 | 56.0213 | 54.6219 | 81.3008 | 43.1034 |
| $\mathrm{I}_{\text {ph }}(\mathrm{A})$ | 0.76083 | 0.76083 | 0.76079 | 0.76078 | 0.7602 | 0.7623 |
| $\mathrm{I}_{\text {SA3 }}(\mu \mathrm{A})$ | $5.91 \mathrm{E}-07$ | 0.59115 | 0.36605 | 0.26713 | 0.9889 | 0.4767 |
| $\mathrm{I}_{\text {SA2 }}(\mu \mathrm{A})$ | $2.45 \mathrm{E}-07$ | 0.24523 | 0.2632 | 0.38191 | 0.0001 | 0.01 |
| $\mathrm{n}_{1}$ | 2 | 2 | 1.91164 | 1.46512 | 1.6 | 1.5172 |
| $\mathrm{n}_{2}$ | 1.45798 | 1.45798 | 1.465 | 1.98152 | 1.192 | 2 |
| $\boldsymbol{F}_{\text {SC-20D }}$ | 0.0009826 | 0.00098272 | 0.001 | $9.83 \mathrm{E}-04$ | 0.01518 | 0.01664 |

Table 7
Single diode model parameter estimation-comparison.

| Parameters | IED (Proposed) | BBO-M [2] | DE [30] | IADE [30] | ABSO [31] | CPSO [35] | GA [34] | PS [32] | SA [33] | SA-MHJ [36] |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $\mathrm{R}_{\mathrm{t}}(\Omega)$ | 0.03636013 | 0.03642 | 0.03598 | 0.03621 | 0.03659 | 0.0354 | 0.0299 | 0.0313 | 0.0345 | 0.0358 |
| $\mathrm{R}_{\text {th }}(\Omega)$ | 53.6485741 | 53.36227 | 56.5533 | 54.7643 | 52.2903 | 59.012 | 42.3729 | 64.1026 | 43.1034 | 57.040 |
| $\mathrm{I}_{\text {ph }}(\mathrm{A})$ | 0.76077402 | 0.76078 | 0.76068 | 0.7607 | 0.7608 | 0.7607 | 0.7619 | 0.7617 | 0.762 | 0.7608 |
| $\mathrm{I}_{\text {SA }}(\mu \mathrm{A})$ | $3.24 \mathrm{E}-07$ | 0.31874 | 0.35515 | 0.33613 | 0.30623 | 0.4 | 0.8087 | 0.998 | 0.4798 | 0.3614 |
| n | $1.48145958$ | 1.47984 | 1.4908 | 1.4852 | 1.47583 | 1.5033 | 1.5751 | 1.6 | 1.5172 | 1.4924 |
| $\boldsymbol{F}_{\text {SC-20 }}$ | 0.0009861 | 0.00098634 | 0.001 | $9.89 \mathrm{E}-04$ | $9.91 \mathrm{E}-04$ | $1.39 \mathrm{E}-03$ | $1.91 \mathrm{E}-02$ | $1.49 \mathrm{E}-02$ | $1.90 \mathrm{E}-02$ | 0.0202 |

current $\left(I_{C}\right)$ and the calculated terminal current $\left(I_{t}\right)$ and is depicted in Eq. (14).

Error $=I_{t}-I_{c}$
Tables 4 and 5 demonstrates the relative error for the double diode and single diode solar cell models respectively. Using the proposed algorithm, the relative error is indeed very low which indicates the high exactness of the experimental data and measured data. The parameters identified for double diode model of solar cell is used to reconstruct the I-V characteristics and power-voltage (P-V) characteristics as depicted in Fig. 7 (a) \& (b) respectively. Fig. 8 (a) \& (b) also depicts the single diode solar cell model I-V characteristics and P-V characteristics respectively.

Tables 6 and 7 shows the result of parameter identification for double diode model and single diode model in comparison of proposed IED algorithm with Differential Algorithm (DE) [30],

Artificial Bee Swarm Optimization (ABSO) [31], Pattern Search [32], Simulated Annealing [33], Genetic Algorithm [34], Chaos Particle Swarm Optimization (CPSO) [35], semi-analytical-modified Hooke-Jeeves method (SA-MHJ) [36] and Modified Biogeography Based Optimization (BBO-M) [2]. The proposed algorithm provides a better minimum value ( F ) compared with other state-of-art literatures.

Based on Table 3, for fuel cell model two different range of values are considered for the parameters to be estimated. The proposed IED algorithm is used to estimate the optimum parametric values. Fig. 9(a) \& (b) shows the I-V characteristics and P-V characteristics respectively for the range-1 values considered for fuel cell model. The calculated I-V values matches very closely with the experimental values.

Tables 8 and 9 displays the results of PEM fuel cell parameter identification for range-1 and range-2 values respectively. The
![img-8.jpeg](img-8.jpeg)

Fig. 9. Fuel Cell Model I-V Characteristics (a) Identification (b) Va. Validation

Table 8
PEM fuel cell parameter estimation with range-1 values - comparison.

| Parameters | $\boldsymbol{\epsilon}_{1}$ | $\boldsymbol{\epsilon}_{2}$ | $\boldsymbol{\epsilon}_{3}$ | $\boldsymbol{\epsilon}_{4}$ | $\lambda$ | $\mathbf{R}_{\mathbf{c}}$ | $\mathbf{b}$ | $\mathbf{F}_{\mathbf{F C}}$ |
| :-- | :--: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| IED (Proposed) | -1.1877 | $3.41 \mathrm{E}-03$ | $6.42 \mathrm{E}-05$ | $-1.24 \mathrm{E}-04$ | 13.0912 | $1.00 \mathrm{E}-04$ | $3.27 \mathrm{E}-02$ | 7.6111 |
| BBBO-M [2] | -0.8574 | $2.59 \mathrm{E}-03$ | $7.65 \mathrm{E}-05$ | $-1.16 \mathrm{E}-04$ | 12.7455 | $1.00 \mathrm{E}-04$ | $3.34 \mathrm{E}-02$ | $7.62 \mathrm{E} \cdot 00$ |
| PSO-W [37] | -1.0446 | $3.00 \mathrm{E}-03$ | $6.72 \mathrm{E}-05$ | $1.15 \mathrm{E}-04$ | 12.4944 | $1.00 \mathrm{E}-04$ | $3.26 \mathrm{E}-02$ | $8.29 \mathrm{E} \cdot 00$ |
| GHS [38] | -1.0072 | $2.98 \mathrm{E}-03$ | $7.18 \mathrm{E}-05$ | $1.26 \mathrm{E}-04$ | 15.5959 | $8.00 \mathrm{E}-04$ | $3.73 \mathrm{E}-02$ | $8.30 \mathrm{E} \cdot 00$ |
| RGA [5] | -1.1568 | $3.42 \mathrm{E}-03$ | $6.42 \mathrm{E}-05$ | $-1.15 \mathrm{E}-04$ | 12.8989 | $1.45 \mathrm{E}-04$ | $3.43 \mathrm{E}-02$ | $8.49 \mathrm{E} \cdot 00$ |

Table 9
PEM fuel cell parameter estimation with range-2 values - comparison.

| Item | $\boldsymbol{\epsilon}_{1}$ | $\boldsymbol{\epsilon}_{2}$ | $\boldsymbol{\epsilon}_{3}$ | $\boldsymbol{\epsilon}_{4}$ | $\lambda$ | $\mathbf{R}_{\mathbf{c}}$ | $\mathbf{b}$ | $\mathbf{F}_{\mathbf{F C}}$ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| IED (Proposed) | -0.9519 | $3.01 \mathrm{E}-03$ | $7.69 \mathrm{E}-05$ | $-1.90 \mathrm{E}-04$ | 22.235 | $1.00 \mathrm{E}-04$ | $3.31 \mathrm{E}-02$ | 16.2322 |
| BBBO-M [2] | -0.952 | $2.94 \mathrm{E}-03$ | $7.80 \mathrm{E}-05$ | $-1.88 \mathrm{E}-04$ | $2.30 \mathrm{E} \cdot 01$ | $1.00 \mathrm{E}-04$ | $3.28 \mathrm{E}-02$ | $1.62 \mathrm{E} \cdot 01$ |
| PSO-W [37] | -0.9473 | $2.93 \mathrm{E}-03$ | $7.80 \mathrm{E}-05$ | $-1.88 \mathrm{E}-04$ | $2.30 \mathrm{E} \cdot 01$ | $1.31 \mathrm{E}-04$ | $3.25 \mathrm{E}-02$ | $1.63 \mathrm{E} \cdot 01$ |
| GHS [38] | -0.9513 | $2.94 \mathrm{E}-03$ | $7.80 \mathrm{E}-05$ | $-1.88 \mathrm{E}-04$ | $2.29 \mathrm{E} \cdot 01$ | $1.00 \mathrm{E}-04$ | $3.21 \mathrm{E}-04$ | $1.63 \mathrm{E} \cdot 01$ |
| RGA [5] | -0.9506 | $3.08 \mathrm{E}-03$ | $7.7524 \mathrm{E}-5$ | $-1.88 \mathrm{E}-04$ | $2.30 \mathrm{E} \cdot 01$ | $1.00 \mathrm{E}-04$ | $3.29 \mathrm{E}-02$ | $1.63 \mathrm{E} \cdot 01$ |

observed $\mathrm{F}_{\mathrm{FC}}$ is considerably a small value compared to the state-of-art literatures. For range-1 values, the lower value of $\mathrm{F}_{\mathrm{FC}}$ recorded is 7.611 and for range-2 values $\mathrm{F}_{\mathrm{FC}}=16.2322$.

From the above sections, it is clear that the proposed IED algorithm is performing well in estimating parameters with smaller objective function value for double diode solar cell modelling, single diode solar cell modelling and for fuel cell modelling.

## 6. Conclusion

An Improved Estimation of Distribution (IED) algorithm is discussed in this article to estimate the optimal parameters of fuel cell and solar cell. The proposed algorithm is compared with the fundamental optimisation techniques from literature and provided better comparable results for double diode and single diode solar cell models and PEM fuel cell model. The structure of the IED algorithm is much easier and the searching capacity is considerably improved. On the parameter identification of the PEM fuel cell and solar cell, the efficiency of the proposed IED distribution algorithm estimation is tested and confirmed. Intensive simulations demonstrate better performance in the assessment of the proposed IED algorithm than those described in the literatures.

## Declaration of Competing Interest

The author declare that there is no conflict of interest.

## References

[1] Niu Q, Zhang H, Li K. An improved TLBO with elite strategy for parameters identification of PEM fuel cell and solar cell models. Int J Hydrogen Energy 2014;39:3837-54. doi: https://doi.org/10.1016/j.ihhydene.2013.12.110
[2] Niu Q, Zhang L, Li K. A biogeography-based optimization algorithm with mutation strategies for model parameter estimation of solar and fuel cells. Energy Convers Manage 2014;86:1173-85. doi: https://doi.org/10.1016/j. encomman.2014.08.036
[3] Chen Y, Wang N. Cuckoo search algorithm with explosion operator for modeling proton exchange membrane fuel cells. Int J Hydrogen Energy 2019;44:3075-87. doi: https://doi.org/10.1016/j.ihhydene.2018.11.145
[4] Bosaicha A, Allagui H, Mami A, Agizim EH, Rouane A. Parameters identification of the complex impedance model of the PEM fuel cell using Matlab/Simulink. Int Conf Green Energy Convers Syst GECS 2017 2017. doi:10.1109/ GECS.2017.8066124.
[5] Ohenoja M, Leviská K. Validation of genetic algorithm results in a fuel cell model. Int J Hydrogen Energy 2010;35:12618-25. doi: https://doi.org/10.1088/0957-6233/12/11/322
[6] Ma J, Ting YO, Man KJ, Zhang N, Guan SU, Wong PWH. Parameter estimation of photovoltaic models via cuckoo search. J Appl Math 2013;2013:10-2. doi: https://doi.org/10.1155/2013/362619.
[7] Hejri M, Mokhtari H. On the comprehensive parametrization of the photovoltaic (PV) cells and modules. IEEE J Photovoltaics 2017;7:250-8. doi: https://doi.org/10.1109/JPSF0TOV.2016.2617038.
[8] Oliva D, Cuevas E, Pajares G. Parameter identification of solar cells using artificial bee colony optimization. Energy 2014;72:93-102. doi: https://doi. org/10.1016/j.energy.2014.05.011.
[9] Jordeth AB. Parameter estimation of solar photovoltaic (PV) cells: a review. Renew Sustain Energy Rev 2016;61:354-71. doi: https://doi.org/10.1016/j. rser.2016.03.049
[10] Chandran BP, Selvakumar AI, Mathew FM. Integrating multilevel converters application on renewable energy sources - a survey. J Renew Sustain Energy 2018;10. doi: https://doi.org/10.1063/1.5045320.
[11] Fawzi M, El-Fergany AA, Hasanien HM. Effective methodology based on neural network optimizer for extracting model parameters of PEM fuel cells. Int J Energy Res 2019;43:8136-47. doi: https://doi.org/10.1002/er.4809.
[12] Selem SI, Hasanien HM, El-Fergany AA. Parameters extraction of PEMFC's model using manta rays foraging optimizer. Int J Energy Res 2020;44:4629-40. doi: https://doi.org/10.1002/er.5384.
[13] Wang L, Huang C. A novel Elite Opposition-based Jaya algorithm for parameter estimation of photovoltaic cell models. Optik (Stuttg) 2018;155:351-6. doi: https://doi.org/10.1016/j.obo.2017.10.081
[14] Elazab OS, Hasanien HM, Elgendy MA, Abdeen AM. Whale optimisation algorithm for photovoltaic model identification. J Eng 2017;2017:1906-11. doi: https://doi.org/10.1040/ene.2017.0662
[15] Xiong G, Zhang J, Shi D, He Y. Parameter extraction of solar photovoltaic models using an improved whale optimization algorithm. Energy Convers Manage 2018;174:388-405. doi: https://doi.org/10.1016/j. encomman.2018.08.053.
[16] El-Fergany AA, Hasanien HM, Agwa AM. Semi-empirical PEM fuel cells model using whale optimization algorithm. Energy Convers Manage 2019;201. doi: https://doi.org/10.1016/j.engسمح.2019.112197
[17] Qais MH, Hasanien HM, Alghuwainem S. Identification of electrical parameters for three-diode photovoltaic model using analytical and sunflower optimization algorithm. Appl Energy 2019;250:109-17. doi: https://doi.org/10.1016/j.apenergy.2019.09.013
[18] Elazab OS, Hasanien HM, Ahaidan I, Abdelaziz AY, Muyeen SM. Parameter estimation of three diode photovoltaic model using grasshopper optimization algorithm. Energies 2020;13. doi: https://doi.org/10.3390/en13020497.
[19] Qais MH, Hasanien HM, Alghuwainem S, Nouh AS. Coyote optimization algorithm for parameters extraction of three-diode photovoltaic models of photovoltaic modules. Energy 2019;187. doi: https://doi.org/10.1016/j.energy.2019.116001
[20] Qais MH, Hasanien HM, Alghuwainem S. Transient search optimization for electrical parameters estimation of photovoltaic module based on datasheet values. Energy Convers Manage 2020;214:. doi: https://doi.org/10.1016/j.engomn.2020.112604112904.
[21] Qais MH, Hasanien HM, Alghuwainem S. Parameters extraction of three-diode photovoltaic model using computation and harris hawks optimization. Energy 2020;195. doi: https://doi.org/10.1016/j.energy.2020.117040
[22] Sabri L, Benzirar M, Zazoui M. Extracting double diode model parameters based on cross entropy optimization algorithm. Bull Electr Eng Informatics 2016;5:412-20. doi: https://doi.org/10.11551/encx5xk571.
[23] Hauschild M, Pelikan M. An introduction and survey of estimation of distribution algorithms. Swarm Evol Comput 2011;1:111-28. doi: https:// doi.org/10.1016/j.swarm.2011.08.003
[24] Yu K, Qu B, Yue C, Ge S, Chen X, Liang J. A performance-guided JAYA algorithm for parameters identification of photovoltaic cell and module. Appl Energy 2019;237:241-57. doi: https://doi.org/10.1016/j.apenergy.2019.01.008.
[25] Guo C, Lu J, Tian Z, Guo W, Darvishan A. Optimization of critical parameters of PEM fuel cell using TLBO-DE based on Elman neural network. Energy Convers

Manage 2019;183:149-58. doi: https://doi.org/10.1016/j. encomman.2018.12.088
[26] Petrone G, Russomando C, Zamboni W. Sensitivity analysis for the parameter identification of a PEM fuel cell. Proc IECON 2018-44th Annu Conf IEEE Ind Electron Soc 2018;1:5198-203. doi: https://doi.org/10.1109/ IECON. 2018.8591156
[27] Petrone R, Zheng Z, Hissel D, Péra MC, Pianese C, Sorrentino M, et al. A review on model-based diagnosis methodologies for PEMFCs. Int J Hydrogen Energy 2013;38:7077-91. doi: https://doi.org/10.1016/j.ijhydene.2013.03.106
[28] Ebrahimi S, Ghorbani B, Vijayaraghavan K. Optimization of catalyst distribution along PEMFC channel through a numerical two-phase model and genetic algorithm. Renew Energy 2017;113:846-54. doi: https://doi.org/ 10.1016/j.renewc.2017.06.007
[29] Kamarudin SK, Daud WRW, Md.Som A, Takriff MS, Mohammad AW. Technical design and economic evaluation of a PEM fuel cell system. J Power Sources 2006;157:641-9. doi:10.1016/j.jpewsour.2005.10.053.
[30] Jiang LL, Maskell DL, Patra JC. Parameter estimation of solar cells and modules using an improved adaptive differential evolution algorithm. Appl Energy 2013;112:185-93. doi: https://doi.org/10.1016/j.apenergy.2013.06.004
[31] Askarzadeh A, Rezazadeh A. Artificial bee swarm optimization algorithm for parameters identification of solar cell models. Appl Energy 2013;102:943-9. doi: https://doi.org/10.1016/j.apenergy.2012.09.052
[32] AlHajri MF, El-Naggar KM, AlRashidi MR, Al-Othman AK. Optimal extraction of solar cell parameters using pattern search. Renew Energy 2012;44:238-45. doi: https://doi.org/10.1016/j.renewc.2012.01.082
[33] El-Naggar KM, AlRashidi MR, AlHajri MF, Al-Othman AK. Simulated Annealing algorithm for photovoltaic parameters identification. Sol Energy 2012;86:266-74. doi: https://doi.org/10.1016/j.solener.2011.09.032
[34] AlRashidi MR, AlHajri MF, El-Naggar KM, Al-Othman AK. A new estimation approach for determining the I-V characteristics of solar cells. Sol Energy 2011;85:1543-50. doi: https://doi.org/10.1016/j.solener.2011.04.013
[35] Huang W, Jiang C, Xue L, Song D. Extracting solar cell model parameters based on chaos particle swarm algorithm. 2011 Int Conf Electr Inf Control Eng ICEICE 2011 - Proc 2011:398-402. doi:10.1109/ICEICE.2011.5777246
[36] Ayala-Matō F, Seuret-Jiménez D, Escobedo-Alatorre JJ, Vigil-Galán O, Courel M. A hybrid method for solar cell parameter estimation. J Renew Sustain Energy 2017;9:1-10.
[37] Tuppadung Y, Kurutach W. Comparing nonlinear inertia weights and constriction factors in particle swarm optimization. Int J Knowledge-Based Intell Eng Syst 2011;15:65-70. doi: https://doi.org/10.3233/KES-2010-0211
[38] Orozan MGH, Mahdavi M. Global-best harmony search. Appl Math Comput 2008;198:643-56. doi: https://doi.org/10.1016/j.amc.2007.09.004