# Advanced design and optimization of single mode photonic crystal fibers 

M. Pourmahayabadi* and S. Mohammad Nejad<br>Nanoptronics Research Laboratory, Department of Electrical Engineering, Iran University of Science and Technology, Tehran, Iran

(Received 13 April 2009; final version received 14 July 2009)


#### Abstract

This paper proposes a combination of differential evolution (DE) and estimation of distribution algorithm (EDA) to design photonic crystal fiber structures with desired properties over the C communication band. In order to determine the properties of PCFs such as dispersion, dispersion slope and loss, an artificial intelligence method, the Nero-Fuzzy system, is applied. In addition, a special cost function which simultaneously includes the confinement loss, dispersion and its slope is used in the proposed design approach. The results revealed that the proposed method is a powerful tool for solving this optimization problem. The optimized PCF exhibits an ultra low confinement loss and low dispersion at $1.55 \mu \mathrm{~m}$ wavelength with a nearly zero dispersion slope over the C communication band.


Keywords: differential evolution/estimation of distribution algorithm; dispersion, dispersion slope; loss; Nero-Fuzzy system; photonic crystal fiber

## 1. Introduction

Photonic crystals have attracted a great deal of attention in the optics community in recent years. One of the most promising applications of photonic crystals is the possibility of creating compact integrated optical devices with photons as the carriers of information, and then the speed and bandwidth of advanced communication systems can be increased dramatically [1,2]. Photonic crystal fibers (PCFs), a kind of two-dimensional photonic crystal, consisting of a central defect region surrounded by multiple airholes that run along the fiber length, have attracted much attention in recent years because of unique properties which are not realized in conventional optical fibers [3-5]. PCFs are divided into two different kinds of fibers. The first one is the index-guiding PCF, guiding light by total internal reflection between a solid core and a cladding region with multiple air-holes. The second one uses a perfectly periodic structure exhibiting a photonic band-gap (PBG) effect at the operating wavelength to guide light in a low-index core region.

Index-guiding PCFs, also called holey fibers or microstructure optical fibers, possess especially an attractive property of great controllability in chromatic dispersion over a large wavelength range [1,2,6]. By varying different parameters of the photonic crystal fibers, such as the pitch $(\Lambda)$ of the periodic array, the hole radius $(r)$, the number of air-hole rings $(N)$ and the refractive index $(n)$, one can engineer the
electromagnetic modes supported by the photonic crystal fibers and explore suitable properties for many practical applications.

The optimization of PCF design is often difficult due to the fact that the optical properties do not usually vary in a simple way with the fiber geometry parameters. The optimization problem of PCF gets more and more difficult as the number of variables $(\Lambda, N, r$ and $N)$ and the number of fiber properties that have to be considered (chromatic dispersion, slope of this dispersion, confinement losses etc.) are increased. The design optimization is usually performed by trial and test approach. However, this is a time consuming approach, both for the computer and the designer. In recent works, genetic algorithms (GAs) have been shown to offer a convenient platform for the solution of the optimization problems $[7-10]$.

The differential evolution (DE) is very successful in solving the global continuous optimization problem [10,11]. Another technique in which a probability model characterizes the distribution of excellent solutions is the estimation of distribution algorithm (EDA) [11-13]. This paper proposes a combination of DE and EDA (DE/EDA algorithm) to solve the optimization problem and to determine the PCF structure. This study is focused on the determination of the PCF structure that can lead to the minimum confinement loss and dispersion and nearly zero dispersion slope over the C communication band.

[^0]
[^0]:    *Corresponding author. Email: pmahyabadi@iust.ac.ir

On the other hand, the most common techniques for analyzing the PCFs are FDTD, FDFD methods (simple and versatile tools for exploring waveguide geometries) and the finite-element approach. The finite difference methods are very general approaches, well established and tested. They describe arbitrary structure, but are numerically intensive and require detailed treatment of boundaries [14-18]. Also FEM is a reliable (well tested) method and accurate modal description, but it needs complex definition of the calculation mesh $[19,20]$. So these conventional models that simulate the optical characteristics of PCFs are computationally expensive and may take hours even on several parallel processors to realize the properties for a given PCF structure. Therefore, a practical design process with trial and error cannot be done in a reasonable amount of time. Here, an artificial intelligence method, the Nero-Fuzzy system is used to establish a model that can predict the properties of PCFs. It has been shown that the proposed method can predict the properties of PCF structures much faster than any existing method. Based on our simulation results, the Nero-Fuzzy system with high accuracy of performance is suited to this particular application.

This paper is organized as follows: in the next section, the fiber geometry structures and problems associated with the optimizing fiber structure are stated. This is followed by Section 3, in which the principles of Nero-Fuzzy systems is introduced and the ability of this method to predict the PCF properties is shown and analyzed. Section 4 will focus on the principles of the DE/EDA algorithm, the simulation results, analyzing and making comparisons with similar works carried out in this field. The trend for future research works will be pointed out in Section 5 and finally the paper sets out its conclusion in the last section, Section 6.

## 2. Problem statement: fiber design and optimization

At present, the design and optimization of photonic crystal fibers is still an area of active research. As shown in Figure 1, all the air-holes in the section of typical PCFs are arrayed according to triangle regularity with identical pitch $\Lambda$, spacing of the neighbouring air-holes. The scale of the air-holes is denoted by $r$ of its radius. Background is pure silica. Because the effective refractive index of the core region is higher than the cladding region, total internal reflectivity (TIR) can occur in the interface between the core and cladding.

As mentioned in the previous section, a novel model based on an artificial intelligence system; which is a combination of the Nero-Fuzzy system and the DE/EDA is proposed (Figure 2). The Nero-Fuzzy system is applied for prediction of the properties of
![img-0.jpeg](img-0.jpeg)

Figure 1. Schematic representation of a typical PCF.
![img-1.jpeg](img-1.jpeg)

Figure 2. Block diagram of the proposed model. (The color version of this figure is included in the online version of the journal.)

PCFs structures and the DE/EDA method for the optimization of the structure with desired properties.

The logical constraints are considered in the optimization process. The refractive index range of silica is $1.44 \leq n \leq 1.46$. In the structure, the air-hole diameter changes between $0.25 \Lambda$ and $0.45 \Lambda$. In fact, unlike conventional fibers, triangular PCFs can be designed to be endlessly single-mode (ESM) that is to support only the propagation of the fundamental mode whatever the wavelength and the pitch value. Previous analyses on PCF cutoff properties have demonstrated that the ESM region is defined by $d / \Lambda<0.406[21,22]$.

Furthermore, the lattice constant or pitch might be set to any value (microns). The value of the lattice constant limits the value of the radius of a particular airhole. The radius should be lower than the half lattice constant as, mathematically, the diameter cannot be greater than the pitch and neither can it be equal to this value because the silica would cease to be continual. Here, the pitch varies in the range of 1.5 to $3 \mu \mathrm{~m}$. Also the number of air-hole rings is selected between 5 and 9 .

## 3. Fuzzy and Nero-Fuzzy systems

### 3.1. Fuzzy system

Fuzzy logic is an innovative technology that allows the description of a desired system behavior using

![img-2.jpeg](img-2.jpeg)

Figure 3. Fuzzy system. (The color version of this figure is included in the online version of the journal.)
everyday spoken language. It is well suited for controlling/predicting a process or system that is nonlinear or too poorly understood to use conventional control designs. In contrast to a crisp set, a Fuzzy set is a set without a crisp boundary. This means the transition from 'belong to' set and 'not belong to' set is gradual. This smooth transition is characterized by membership functions that give flexibility in modeling linguistic expressions. The essential components of a Fuzzy system are the Fuzzy inference engine, Fuzzy rule base and defuzzifier. The following definitions explain the blocks used in the Fuzzy system shown in Figure 3. Fuzzification is a process to control discrete or crisp input variables to Fuzzy variables. It is essential to map between the range of input to set membership values of each Fuzzy variable. Since the inputs in most applications are real numbers, the fuzzifier serves as the proper interface between the Fuzzy inference engine and the physical world. The criteria in designing a fuzzifier are:
(1) The Fuzzy set A should have a large membership value at $x$.
(2) The fuzzifier should simplify the computations involved in the Fuzzy inference engine.
In a Fuzzy inference engine, Fuzzy logic principles are used to combine the Fuzzy IF-THEN rules in the Fuzzy rule base into a mapping from a Fuzzy set in an $n$-dimensional universe of discourse to a Fuzzy set in a one-dimensional universe of discourse. Defuzzification translates the Fuzzy output from the inference process into a discrete or crisp output value. There are many suggestions for the calculation of the output values based on Fuzzy membership value [23-25].

In this section, the photonic crystal fiber system can be represented by a Fuzzy system with four input parameters; pitch, number of air-hole rings, refractive index, and air-hole radius that determine the structure of the photonic crystal. The system outputs are the PCF properties; dispersion, dispersion slope and confinement loss. The Fuzzy learning process starts by defining a number of overlapping Fuzzy sets to describe the
input parameters $(\Lambda, N, n$, and $r$ ) and the membership functions that describe the degree of belonging of each input parameter to the Fuzzy sets defined over its domain. These membership functions map elements of a Fuzzy set to real numbered values on the interval 0 and 1 that represent the degree of belonging of an element to the Fuzzy set. Triangular, trapezoid or Gaussian membership functions can be used. Here a Gaussian membership function is adopted for the input parameters and an impulse membership function with zero width is used for the outputs. It is important to realize that the membership functions do not represent probability of belonging to the Fuzzy set but rather the degree by which the variable belongs to the Fuzzy set. The modeling process depends on fuzzifying all four input domains and constructing a Fuzzy rule-base, which describes the relationship between the Fuzzy sets, defined on the input domains and the PCF properties.

Suppose that the Fuzzy rule base consist of $M$ rules in the form of
$\mathrm{Ru}^{(l)}$ : If $x_{1}$ is $A_{1}^{l}$ and $\ldots$ and $x_{n}$ is $A_{n}^{l}$, then $y$ is $B^{l}$
and that

$$
\mu_{A_{i}^{l}}\left(x_{i}\right)=\exp \left[-\left(\frac{x_{i}-\tilde{x}_{i}^{l}}{\sigma_{i}^{l}}\right)^{2}\right]
$$

where $\tilde{x}_{i}^{l}$ and $\sigma_{i}^{l}$ are constant parameters, $i=1,2, \ldots, n$ and $l=1,2, \ldots, M$. The Gaussian fuzzier maps $\mu_{i}^{l} \in U$ into Fuzzy set $A^{l}$ in $U$, which has the following Gaussian membership function:

$$
\mu_{A^{l}}(X)=\prod_{i=1}^{n} \exp \left[-\left(\frac{x_{i}-\tilde{x}_{i}^{l}}{\sigma_{i}^{l}}\right)^{2}\right]
$$

So, a Fuzzy system is designed with product inference engine, singleton fuzzier, center average defuzzier and Gaussian membership function. The objective functions for the proposed fuzzy system are as follow:

$$
\begin{aligned}
& F_{D}(X)=\frac{\sum_{i=0}^{M} D^{l} \prod_{i=1}^{n} \exp \left[-\left(\frac{x_{i}-\tilde{x}_{i}^{l}}{\sigma_{i}^{l}}\right)^{2}\right]}{\sum_{i=0}^{M} \prod_{i=1}^{n} \exp \left[-\left(\frac{x_{i}-\tilde{x}_{i}^{l}}{\sigma_{i}^{l}}\right)^{2}\right]} \\
& F_{D S}(X)=\frac{\sum_{i=0}^{M} D S^{l} \prod_{i=1}^{n} \exp \left[-\left(\frac{x_{i}-\tilde{x}_{i}^{l}}{\sigma_{i}^{l}}\right)^{2}\right]}{\sum_{i=0}^{M} \prod_{i=1}^{n} \exp \left[-\left(\frac{x_{i}-\tilde{x}_{i}^{l}}{\sigma_{i}^{l}}\right)^{2}\right]} \\
& F_{L}(X)=\frac{\sum_{i=0}^{M} L^{l} \prod_{i=1}^{n} \exp \left[-\left(\frac{x_{i}-\tilde{x}_{i}^{l}}{\sigma_{i}^{l}}\right)^{2}\right]}{\sum_{i=0}^{M} \prod_{i=1}^{n} \exp \left[-\left(\frac{x_{i}-\tilde{x}_{i}^{l}}{\sigma_{i}^{l}}\right)^{2}\right]}
\end{aligned}
$$

The learning process to generate a knowledge rulebase based on a training dataset is established. It starts by defining the membership functions for each input parameter using a Gaussian distribution. The Fuzzy model is tested using a testing dataset that is not used in the Fuzzy rules. The testing process allowed evaluating the Fuzzy rule-base by comparing the prediction of the output using the Fuzzy model with the testing outputs.

### 3.2. Nero-Fuzzy system

In the Fuzzy system, Fuzzy If-Then rules are first generated from input-output pairs and the Fuzzy system is constructed from these rules according to a certain choice of Fuzzy inference engine, fuzzier and defuzzier. However, there are some free parameters $\left(\sigma_{i}\right)$ in the structure which we selected with trial and error to obtain the desired performance. Here these parameters are determined according to the input-output pairs by using a training algorithm. This algorithm is the error back propagation (EBP) method which is the main training algorithm in neural networks [25,26]. To determine these parameters in some optimal fashion, it is helpful to represent the Fuzzy system $F(x)$ as a feedforward network. Our task is to design a Fuzzy system $F(x)$ in the form of Equation (4) such that the matching error,

$$
e=\frac{1}{2}\left(F(k)-F^{*}(k)\right)^{2}
$$

is minimized. That is the task of determining the parameter $\sigma_{i}$ for each objective function such that its error is minimized. Using the EPM we obtain the training algorithm for $\sigma_{i}$;

$$
\begin{aligned}
\sigma_{i}^{l}(k+1) & =\sigma_{i}^{l}(k)+\Delta \sigma_{i}^{l}(k) \\
\Delta \sigma_{i}^{l}(k) & =\gamma \frac{\partial \varepsilon_{\sigma_{i}}(k)}{\partial \sigma_{i}^{l}(k)} \\
\frac{\partial e}{\partial \sigma_{i}} & =\left(F(X)-F^{*}(X)\right) \frac{\partial F(X)}{\partial \sigma_{i}}
\end{aligned}
$$

Using this procedure, we can determine the optimal parameters. Therefore, there are three steps to establish the Nero-Fuzzy model: first, a learning process to determine the optimal design variables. Second, the knowledge rule-base, membership functions and the objective functions are modified to reduce the prediction error of the Fuzzy model by optimizing the learning parameters. Third, the Fuzzy model is tested using a testing dataset that is not used in the learning or the optimization steps. The testing process allowed evaluating the Fuzzy rule-base by comparing the prediction of the outputs using the Fuzzy model with
the testing outputs. This three-step process enabled establishment of a robust yet accurate Nero-Fuzzy based prediction model.

### 3.3. Implementation of Fuzzy and Nero-Fuzyy systems

The simulation study was carried out with the database generated by the FDFD method [14,15]. The database consists of 1200 samples which are divided into two parts; a training set ( 800 samples) and a testing set (400 samples). Every sample has seven features which are fiber parameters. The input features are the PCF parameters including pitch $(\Lambda)$, number of air-hole rings $(N)$, refractive index $(n)$, and air-hole radius $(r)$. The output features (PCF properties) consist of dispersion $(D)$, dispersion slope $(S)$ and confinement loss $(L)$.

The design variables (free parameter $\sigma_{i}$ ) that we selected with trial and error are presented in Table 1. The ability of the Fuzzy system in the predictability is shown in Table 2 for dispersion, dispersion slope and confinement loss characteristics. It is obvious that this initial non-optimized Fuzzy model can predict the PCFs properties with low accuracy.

The optimal design variables of the Nero-Fuzzy system, used to control objective functions, are presented in Table 1. The excellent ability of the Nero-Fuzzy system in predicting the PCFs properties is shown in Figures 4-6. The maximum error ( $\sim 1.298 \%$ ) is achieved for the confinement loss characteristics and it is ultra low for the other characteristics such as dispersion and dispersion slope. It is obvious that the Nero-Fuzzy outputs coincide with the desired outputs approximately. The prediction ability of the NeroFuzzy system on this test set is compared with the

Table 1. Design variables for Fuzzy and Nero-Fuzzy methods.

| Design variables | $\sigma_{\Lambda}$ | $\sigma_{N}$ | $\sigma_{n}$ | $\sigma_{r}$ |
| :-- | :--: | :--: | :--: | :--: |
| Fuzzy system | 0.44374 | 1.41266 | 0.00926 | 0.10345 |
| Nero-Fuzzy system | 0.07589 | 0.51323 | 0.00462 | 0.21533 |

Table 2. A comparison of the prediction error (\%) of Fuzzy and Nero-Fuzzy methods.

| Method | Dispersion <br> error (\%) | Dispersion <br> slope error (\%) | Loss <br> error (\%) |
| :-- | :--: | :--: | :--: |
| Fuzzy | 33.37 | 20.24 | 49.24 |
| Nero-Fuzzy | 0.099 | 0.01236 | 1.298 |

Fuzzy method in Table 2. So, the Nero-Fuzzy based model can be utilized to determine the complex relationship between the PCF's geometry and its properties.
![img-3.jpeg](img-3.jpeg)

Figure 4. Dispersion characteristics $\left(\mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}\right)$ for testing samples; Nero-Fuzzy system output (solid line) and desired output (dash line) coincided with each other. (The color version of this figure is included in the online version of the journal.)
![img-4.jpeg](img-4.jpeg)

Figure 5. Dispersion slope characteristics $\left(\mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}\right)$ for testing samples; Nero-Fuzzy system output (solid line) and desired output (dash line) coincided with each other. (The color version of this figure is included in the online version of the journal.)
![img-5.jpeg](img-5.jpeg)

Figure 6. Confinement loss characteristics $\left(\mathrm{dB} \mathrm{km}^{-1}\right)$ for testing samples; Nero-Fuzzy system output (solid line) and desired output (dash line) coincided approximately with each other. (The color version of this figure is included in the online version of the journal.)

## 4. Design strategy

Genetic algorithms, applied to inverse PCF design, involve a stochastic search for a globally optimal PCF structure that provides the best performance of a PCF for a specific function. In this paper, an optimum design technique for PCF that utilizes an algorithm combining DE and EDA (DE/EDA) is proposed. Simulation results demonstrate that DE/EDA outperforms both the DE algorithm and the EDA in optimization design.

### 4.1. Differential evolution

In this section, we briefly review the DE algorithm. In fact, it is the best GA-like algorithm for the global continuous optimization problem. The DE algorithm has several versions; we consider the best one [10]. This algorithm maintains a population of $N$ points in every generation, where each point is a potential solution. The algorithm evolves and improves the population iteratively. In each generation, a new population is generated based on the current population. To generate offsprings for the new population, the algorithm extracts distance and direction information from the current population members and adds random deviation for diversity. If an offspring has a lower objective function value than a predetermined population member, it will replace this population member. This evolution process continues until a stopping criterion is met (e.g. the current best objective function value is smaller than a given value or the number of generations is equal to a given maximum value) $[10,11]$.

Due to its ability to maintain the diversity and to do local search, the DE algorithm performs better than some other GAs. But the DE algorithm has no mechanism to directly use the global information about the search space to guide the population towards promising areas.

### 4.2. Estimation of distribution algorithm

Estimation of distribution algorithm (EDA) is a new class of GAs. EDA directly extracts the global statistical information about the search space from the search so far and builds a probability model of promising solutions. New solutions are sampled from the model thus built. Let $\operatorname{Pop}(t)$ be the population of solutions at generation $t$. EDAs work in the following iterative way:
Step 1: Selection. Select $M$ promising solutions from $\operatorname{Pop}(t)$ to form the parent set $Q(t)$ by a selection method;

Step 2: Modeling. Build a probabilistic model $p(x)$ based on the statistical information extracted from the solutions in $Q(t)$;
Step 3: Sampling. Sample new solutions according to the constructed probabilistic model $p(x)$;
Step 4: Replacement. Fully or partly replace solutions in $\operatorname{Pop}(t)$ by the sampled new solutions to form a new population $\operatorname{Pop}(t+1)$.

One of the major issues in EDAs is how to select parents. A widely-used selection method in EDA is the truncation selection. In the truncation selection, individuals are sorted according to their objective function values and only the best individuals are selected as parents. Another major issue in EDAs is how to build a probability distribution model $p(x)$. In EDAs for the global continuous optimization problem, the probabilistic model $p(x)$ can be a Gaussian distribution [11-13].

### 4.3. DEJEDA algorithm

The most important operation in the DE algorithm is to generate offspring. Each offspring is generated by crossing a solution from the current population and a solution obtained by the DE mutation. On the other hand, EDA tries to guide its search towards a promising area by sampling new solutions from a probability model. The EDA mechanism is incorporated into the DE algorithm in order to create solutions which are more promising than solutions generated by the DE recombination (crossover and mutation), and consequently, to explore the search space more effectively [11]. The DE/EDA algorithm is given as follows:
Step 1: Randomly generate $N$ solutions $x_{1}^{0}, x_{2}^{0}, \ldots, x_{N}^{0}$ from the feasible search space to form an initial population, set $k=0$;
Step 2: Generate a new solution $x_{i}^{k}$ according to the DE/EDA offspring generation scheme described in the above section;
Step 3: If the given stopping criterion is not met, $k=k+1$, go to Step 2.

At generation $k$, the proposed DE/EDA offspring generation scheme works as follows:
Step 1: Select the best $M$ solutions from the current population, construct a probability model as;

$$
\begin{gathered}
p_{k}(x)=\prod_{i=1}^{n} N\left(x_{i} ; \hat{\mu}_{i}^{k}, \hat{\sigma}_{i}^{k}\right) \\
\hat{\mu}_{i}^{k}=\tilde{X}_{i}^{k}=\frac{1}{M} \sum_{i=1}^{M} x_{i, i}^{k}, \quad \hat{\sigma}_{i}^{k}=\left[\frac{1}{M} \sum_{i=1}^{M}\left(x_{i, i}^{k}-\tilde{X}_{i}^{k}\right)^{2}\right]^{1 / 2}
\end{gathered}
$$

Step 2: Generate a trial solution $u=\left(u_{1}, u_{2}, \ldots, u_{n}\right)$ as follows: for all $j=1,2, \ldots, n$ if $(\operatorname{rand}(.)<\delta)$
$u_{j}=\left[\left(x_{i}^{k}\right)_{j}+\left(x_{i l}\right)_{j}\right] / 2+F \times\left[\left(x_{i l}\right)_{j}-\left(x_{i}^{k}\right)_{j}+\left(x_{i k}\right)_{j}-\left(x_{i}\right)_{j}\right]$,
else $u_{j}$ is sampled according to $N\left(x_{i}^{k} ; \mu_{i}^{k}, \sigma_{i}^{k}\right)$; where $\operatorname{rand}($.$) is an uniform random number in ( 0,1 ), and \delta$ $(1 \leq \delta \leq N)$ is a parameter.
Step 3: If $f(u) \leq f\left(x_{i}^{k}\right)$ then $x_{i}^{k+1}=u$, otherwise, set $x_{i}^{k+1}=x_{i}^{k}$.

The above offspring generation scheme is similar to the DE crossover. Like the DE offspring generation scheme, one part of a trial solution generated comes from the DE mutation. But the other part of the trial solution is sampled in the search space from the constructed probability distribution model. Therefore, a trail solution generated by the DE/EDA offspring generation scheme is based on the differential information and global statistical information. $\delta$ is used to balance contributions of the global information and the differential information.

Parameters involved in the proposed algorithm are $N, \delta$ and $F$. The number of solutions selected in Step 1 of the DE/EDA offspring generation scheme $M=N / 2$. Compared with the DE algorithm, DE/EDA has only a small extra computational cost in constructing the probability model. On the other hand, DE/EDA has the ability to utilize the global statistical information collected from the previous search, and it also can use the differential information in the DE way [11].

### 4.4. Implementation of genetic algorithms; results and discussion

As mentioned in Section 2, the Nero-Fuzzy system combined with the DE/EDA algorithm is used to optimize the fiber's profile as well as to accurately determine its modal properties. The simulation study was carried out with the database consisting of 500 individuals. Every individual has four features which are fiber parameters including pitch $(\Lambda)$, number of air-hole rings $(N)$, refractive index $(n)$, and air-hole radius $(r)$.

The characteristics of the individual chosen here are the confinement loss $(L)$, dispersion $(D)$ and its slope $(S)$ in the wavelength range from 1.53 to $1.565 \mu \mathrm{~m}$ (C communication band). These characteristics are calculated using the set of chromosomes $\{\Lambda, r, N, n\}$. We are now going to consider the following optimization problem;

$$
\min f(x)
$$

where $f(x)$ is a real-value function which has to be minimized to find the best solution. To do that, we need to define our preferred cost functions for the proposed algorithm. Here are three kinds of cost functions:

$$
\begin{gathered}
f_{1}(x)=\sum_{\lambda}|D| \\
f_{2}(x)=\sum_{\lambda}|D| \times \sum_{\lambda}|S| \\
f_{3}(x)=\sum_{\lambda}|D| \times \sum_{\lambda}|S| \times \sum_{\lambda}|L|
\end{gathered}
$$

As can be seen in the first case, dispersion is minimized and in the second case, both dispersion and dispersion slope are minimized while in the third one, dispersion, dispersion slope and loss are minimized simultaneously.

In this section the results of GA methods in order to optimize the PCF properties are presented. At the first generation of each GA, a population of 'individuals' is randomly created, each individual being a possible solution to the problem. In the particular case of this paper, each individual corresponds to a particular design of PCF and is made of four 'chromosomes' $\{\Lambda, r, N$ and $n\}$ which constitute the variables of the problem.

These following steps are performed 10 times; first of all 100 individuals are selected randomly. Then all three GA algorithms, explained above, are applied to this selected population. In order to calculate the cost function, we need to determine the PCF characteristics over the C communication band. As mentioned in Section 3, the Nero-Fuzzy system is applied to analyze the dispersion property of the triangular PCFs. This evolution process continues until the number of generations is equal to a given maximum value (it is 500 in our case). In the last step, the ten best individuals are selected and they are put in the pool as the new population.

Finally, a new population is created with 100 individuals. Again the GA algorithms are performed with this population and the best individual with the minimum cost function is selected as the solution. In this phase, the number of generations is made equal to 1000. In order to make a fair comparison, we repeat the process several times for each cost function of these algorithms.

### 4.4.1. Cost function with dispersion

The first cost function is the summation of absolute dispersion over all $\lambda$ (wavelength) in the specified wavelength range of optimization ( C band). The results

Table 3. The solution (PCF parameters) found by three methods with the first cost function.

| Method | $N$ | $\Lambda(\mu \mathrm{~m})$ | $n$ | $r(\mu \mathrm{~m})$ |
| :-- | :--: | :--: | :--: | :--: |
| DE | 9 | 2.5 | 1.46 | 0.3736 |
| EDA | 9 | 2.077 | 1.449 | 0.4569 |
| DE/EDA | 5 | 2.276 | 1.457 | 0.4112 |

Table 4. Dispersion value at $1.55 \mu \mathrm{~m}$ wavelength and dispersion slope over C band for the PCFs found by the three methods with the first cost function.

| Method | $D\left(\mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}\right)$ | $S\left(\mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}\right)$ |
| :-- | :--: | :--: |
| DE | -4.1 | 0.014285 |
| EDA | 0.35 | 0.114285 |
| DE/EDA | -0.55 | 0.085714 |

![img-6.jpeg](img-6.jpeg)

Figure 7. Dispersion characteristics as a function of wavelength for the PCFs found by the three methods with the first cost function.
of the optimization are summarized in Tables 3 and 4. Table 3 shows the best individuals achieved by the algorithms and the dispersion characteristics are depicted in Table 4 and also in Figure 7. As can be seen, the minimum value of dispersion at $1.55 \mu \mathrm{~m}$ wavelength is for the PCF (best solution) achieved by the EDA method whereas the best PCF found by the DE algorithm has the minimum dispersion slope. However, it is seen that overall the hybrid method, DE/EDA performs better than these two algorithms.

### 4.4.2. Cost function with dispersion and dispersion slope

The second cost function is the summation of the absolute dispersions over all $\lambda$ multiplied by the summation of absolute dispersion slope over all $\lambda$ in

Table 5. The solution (PCF parameters) found by the three methods with the second cost function.

| Method | $N$ | $\Lambda(\mu \mathrm{~m})$ | $n$ | $r(\mu \mathrm{~m})$ |
| :-- | :--: | :--: | :--: | :--: |
| DE | 9 | 2.5 | 1.44 | 0.3741 |
| EDA | 6 | 2.733 | 1.442 | 0.4447 |
| DE/EDA | 7 | 2.713 | 1.44 | 0.3798 |

Table 6. Dispersion value at $1.55 \mu \mathrm{~m}$ wavelength and dispersion slope over C band for the PCFs found by the three methods with the second cost function.

| Method | $D\left(\mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}\right)$ | $S\left(\mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}\right)$ |
| :-- | :--: | :--: |
| DE | -4.58 | 0.015714 |
| EDA | 0.4 | 0.057142 |
| DE/EDA | 0.22 | 0.025114 |

![img-7.jpeg](img-7.jpeg)

Figure 8. Dispersion characteristics as a function of wavelength for the PCFs found by the three methods with the second cost function.
the specified range of optimization. Tables 5 and 6 summarize the results of the optimization. Table 5 shows the best individuals achieved by the algorithms. The dispersion characteristics are depicted in Table 6 and also in Figure 8. It is obvious that the DE/EDA performs better than these two algorithms although the solution found by DE has dispersion slope characteristics slightly superior than that of DE/EDA.

### 4.4.3. Cost function with dispersion, dispersion slope and loss

In this case, the cost function is defined as Equation (13). Table 7 shows the best individuals achieved by the algorithms. The loss and dispersion characteristics of the optimized PCFs are depicted in

Table 7. The solution (PCF parameters) found by the three methods with the third cost function.

| Method | $N$ | $\Lambda(\mu \mathrm{~m})$ | $n$ | $r(\mu \mathrm{~m})$ |
| :-- | :--: | :--: | :--: | :--: |
| DE | 9 | 3 | 1.46 | 0.6352 |
| EDA | 9 | 2.989 | 1.46 | 0.6576 |
| DE/EDA | 9 | 3 | 1.459 | 0.6407 |

![img-8.jpeg](img-8.jpeg)

Figure 9. The loss characteristics as a function of wavelength for the PCFs found by the three methods with the third cost function.
![img-9.jpeg](img-9.jpeg)

Figure 10. Dispersion characteristics as a function of wavelength for the PCFs found by the three methods with the third cost function.

Figures 9 and 10. Also Table 8 summarizes the results of these optimizations. It is obvious that overall the DE/EDA performs better than the other algorithms although the solution found by DE has dispersion characteristics slightly superior than that of DE/EDA and the solution found by EDA has loss characteristics slightly better than that of DE/EDA.

Table 8. The properties of PCFs found by the three methods with the third cost function at $1.55 \mu \mathrm{~m}$ wavelength.

| Method | $\underset{\left(\mathrm{dB} \mathrm{km}^{-1}\right)}{\mathrm{L}}$ | $\underset{\left(\mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}\right)}{\mathrm{D}}$ | $\underset{\left(\mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}\right)}{\mathrm{S}}$ |
| :-- | :--: | :--: | :--: |
| DE | $2.1 \times 10^{-7}$ | 18.45 | 0.013428 |
| EDA | $2 \times 10^{-8}$ | 20.86 | 0.01187 |
| DE/EDA | $1.25 \times 10^{-7}$ | 18.85 | 0.01285 |

### 4.4.4. Discussion

To summarize, we have shown that for this specific optimization problem, the DE/EDA algorithm performs better than both DE and the EDA algorithms separately. Although, there are some reports on the design and optimization of photonic crystal fibers, most of the designed fibers do not provide single mode operation over the C communication band [27-30]. A related work that has used the simple GA was by Kerrinckx et al. [7]. In this work each individual has two chromosomes $\{\Lambda, r\}$ and the dispersion error is defined as the cost function. The best solution reported by Kerrinckx et al. [7] is a nine-ring structure of PCF with the pitch $\Lambda=2.35 \mu \mathrm{~m}$ and the radius $r=0.33 \mu \mathrm{~m}$. The dispersion and dispersion slope of this PCF are $2.5 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ at $1.55 \mu \mathrm{~m}$ wavelength and $0.03575 \mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}$, respectively. In another similar work the chromatic dispersion of $0.8 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ at $1.55 \mu \mathrm{~m}$ wavelength has been obtained for a nine-ring structure with the following parameters: $\Lambda=2.59 \mu \mathrm{~m}$ and $r=0.29 \mu \mathrm{~m}[31]$.

In our proposed approach, a PCF with the dispersion of $0.22 \mathrm{ps} \mathrm{nm}^{-1} \mathrm{~km}^{-1}$ at $1.55 \mu \mathrm{~m}$ wavelength and dispersion slope of $0.025114 \mathrm{ps} \mathrm{nm}^{-2} \mathrm{~km}^{-1}$ over the C communication band has been designed.

In addition, a special cost function which simultaneously includes the confinement loss, dispersion and its slope is used in the proposed design approach. The optimized PCF exhibits an ultra low confinement loss in the order of $10^{-7}$ and low dispersion at $1.55 \mu \mathrm{~m}$ wavelength with a dispersion slope of $\pm 0.012 \mathrm{ps} \mathrm{nm}^{-2}$ $\mathrm{km}^{-1}$ over the C communication band. So, it is revealed that the DE/EDA method is a powerful tool for optimum design of PCFs.

## 5. Future work

In further work, we are going to combine EDA with the hill climbing (HC) algorithm for tackling this optimization problem. Also we will try to present the cost function using a combination of dispersion, dispersion slope, loss, bending loss and mode area characteristics in order to design an optimum photonic crystal fiber. Furthermore, we will attempt to
demonstrate that the number of the individuals' chromosomes (PCF parameters) can be increased to achieve a PCF structure with better characteristics.

## 6. Conclusion

In this article, a novel design method based on the Nero-Fuzzy system and the DE/EDA method is introduced. We have investigated the suitability of the Nero-Fuzzy system to predict the properties of PCFs. After numerous tests, it is revealed that this method is remarkably effective in predicting the properties of PCF such as dispersion, dispersion slope and loss over the C communication band. It can predict the characteristics of PCFs with high accuracy of more than $99 \%$. The DE/EDA method is applied for the optimization of the structure with desirable properties. The simulation results demonstrate that DE/EDA is an excellent method in the optimization problem of the PCF structure. The optimized PCF exhibits an ultra low confinement loss in the order of $10^{-7}$ and low dispersion at $1.55 \mu \mathrm{~m}$ wavelength with a dispersion slope of $\pm 0.012 \mathrm{ps} \mathrm{nm}^{-2}$ $\mathrm{km}^{-1}$ over the C communication band. With further optimization of the structure and increasing the number of individuals' chromosomes in the DE/EDA method, PCF characteristics can be further improved.

## References

[1] Russell, P.S.J. J. Lightwave Technol. 2006, 24, 4729-4749.
[2] Calo, G.; D'Orazio, A.; De Sario, M.; Mescia, L.; Petruzzelli, V.; Prudenzano, F. Photonic Crystal Fibers, ICTON, Barcelona, Spain, July 3-7, 2005.
[3] Zhou, J.; Tajima, K.; Nakajima, K.; Kurokawa, K.; Fukai, C.; Matsui, T.; Sankawa, I. Opt. Fiber Technol. 2005, 11, 101-110.
[4] Pourmahyabadi, M.; Mohammad Nejad, S. Optimal Confinement Loss Reduction in Photonic Crystal Fiber with Ultra-flattened Dispersion. Symposium on High Capacity Optical Networks \& Enabling Technologies, HONET 08, Penang: Malaysia, 18-20 November, 2008.
[5] Hoo, Y.L.; Jin, W.; Ju, J.; Ho, H.L.; Wang, D.N. Opt. Commun. 2004, 242, 327-332.
[6] Chen, M.Y. Opt. Commun. 2006, 266, 151-158.
[7] Kerrinckx, E.; Bigot, L.; Douay, M.; Quiquempois, Y. Opt. Express 2004, 12, 1990-1995.
[8] Poletti, F.; Finazzi, V.; Monro, T.M.; Broderick, N.G.R.; Tse, V.; Richardson, D.J. Opt. Express 2005, 13, 3728-3736.
[9] Musin, R.R.; Zheltikov, A.M. Opt. Commun. 2008, 281, 567-572.
[10] Shahoei, H.; GhafooriFard, H.; Rostami, A.; Shahoei, W. Design of Flattened-Low Dispersion MII

Type Optical Fiber by using DE Algorithm; Tarbiat Modares University: Tehran, Iran, May, 2008.
[11] Sun, J.; Zhang, Q.; Tsang, E.P.K. Informat. Sci. 2005, $169,249-262$.
[12] Tsutsui, S.; Pelikan, M.; Goldberg, D.E. Evolutionary Algorithm Using Marginal Histogram Models in Continuous Domain. Proceedings of the 2001 Genetic and Evolutionary Computation Conference Workshop, San Francisco, CA, June 21, 2001.
[13] Rudlof, S.; Koppen, M. Stochastic Hill-Climbing with Learning by Vectors of Normal Distributions; Fraunhofer-Institute for Production System and Design Technology (IPK): Berlin, December, 1997.
[14] Arriaga, J.; Knight, J.C.; Russell, P.St.J. Physica E 2003, $17,440-442$.
[15] Zhu, Z.; Brown, T.G. Opt. Express 2002, 10, 853-864.
[16] Shuqin, L.; Zhi, W.; Guobin, R.; Shuisheng, J. Opt. Fiber Technol. 2005, 11, 34-45.
[17] Yu, C.P.; Chang, H.C. Opt. Quantum Electron. 2004, 36, $145-163$.
[18] Yu, C.P.; Chang, H.C. Opt. Express 2004, 12, 2795-2809.
[19] Bouwmans, G. Photonic Crystal Fibers. Physique des Lasers, Atomes et Molecules; Universite des Sciences et Technologies de Lille: France, 2005; pp 34-38.
[20] Szpulak, M.; Urbanczyk, W.; Serebryannikov, E.; Zheltikov, A.; Hochman, A.; Leviatan, Y.; Kotynski, R.; Panajotov, K. Opt. Express 2006, 14, $5699-5714$.
[21] Selleri, S.; Cucinotta, A.; Foroni, M.; Poli, F.; Bottacini, M. Proc. SPIE 2005, 5950, 59500U.
[22] Pourmahyabadi, M.; Mohammad Nejad, S. Design of Single Mode Photonic Crystal Fibers with Low-Loss and Flattened Dispersion at $1.55 \mu \mathrm{~m}$ Wavelength. 4th International Symposium on High Capacity Optical Networks and Enabling Technologies, Dubai, UAE, November 18-20, 2007.
[23] Farfan, G.B.; Rammohan, R.; Su, M.F.; El-Kady, I.; Reda Taha, M.M. Photon. Nanostruct. - Fundament. Applic. 2008, 6, 154-166.
[24] Jantzen, J. Tutorial on Fuzzy Logic; Technical Report, 98-E 868 (logic): Technical University of Denmark: Denmark, 2008.
[25] Haykin, S. Neural Networks; Macmillan College: New York, 1996.
[26] Wang, L.X. A Course in Fuzzy System and Control; Prentice-Hall: Englewood Cliffs, NJ, 1997; Chapter 11, p 105 .
[27] Wu, T.L.; Chao, C.H. IEEE Photon. Technol. Lett. 2005, 17, 67-69.
[28] Poli, F.; Cucinotta, A.; Selleri, S.; Bouk, A.H. IEEE Photon. Technol. Lett. 2004, 16, 1065-1067.
[29] Ferrando, A.; Silvestre, E.; Andres, P. Opt. Express 2001, 9, 687-697.
[30] Liu, Z.L.; Liu, X.D.; Li, S.G.; Li, G.Y.; Wang, W.; Hou, L.T. Opt. Commun. 2007, 272, 92-96.
[31] Reeves, W.H.; Knight, J.C.; Russell, P.St.J. Opt. Express 2002, 10, 609-613.

Copyright of Journal of Modern Optics is the property of Taylor \& Francis Ltd and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.