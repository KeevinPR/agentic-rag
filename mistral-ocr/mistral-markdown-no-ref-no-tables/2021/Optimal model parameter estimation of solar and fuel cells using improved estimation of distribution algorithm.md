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
Table 5
Calculated error - single diode model.
Error $\left(\boldsymbol{F}_{\boldsymbol{X} \cdot \boldsymbol{0} \boldsymbol{0}}\right.$ )
$\begin{array}{llllll}\text { (12) } & & & & \\ & \text { Step } 4: \text { Evaluate the objective function of solar PV and fuel cell. } & & \text { (12) }\end{array}$

Step 3
PEM fuel cell-parameter values.


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

Table 7
Single diode model parameter estimation-comparison.

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
Table 9
PEM fuel cell parameter estimation with range-2 values - comparison.
observed $\mathrm{F}_{\mathrm{FC}}$ is considerably a small value compared to the state-of-art literatures. For range-1 values, the lower value of $\mathrm{F}_{\mathrm{FC}}$ recorded is 7.611 and for range-2 values $\mathrm{F}_{\mathrm{FC}}=16.2322$.

From the above sections, it is clear that the proposed IED algorithm is performing well in estimating parameters with smaller objective function value for double diode solar cell modelling, single diode solar cell modelling and for fuel cell modelling.

## 6. Conclusion

An Improved Estimation of Distribution (IED) algorithm is discussed in this article to estimate the optimal parameters of fuel cell and solar cell. The proposed algorithm is compared with the fundamental optimisation techniques from literature and provided better comparable results for double diode and single diode solar cell models and PEM fuel cell model. The structure of the IED algorithm is much easier and the searching capacity is considerably improved. On the parameter identification of the PEM fuel cell and solar cell, the efficiency of the proposed IED distribution algorithm estimation is tested and confirmed. Intensive simulations demonstrate better performance in the assessment of the proposed IED algorithm than those described in the literatures.

## Declaration of Competing Interest

The author declare that there is no conflict of interest.
