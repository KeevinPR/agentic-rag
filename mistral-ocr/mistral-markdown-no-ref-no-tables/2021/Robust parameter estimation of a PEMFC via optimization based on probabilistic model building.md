# Robust parameter estimation of a PEMFC via optimization based on probabilistic model building 

Luis Blanco-Cocom ${ }^{\mathrm{a}}$, Salvador Botello-Rionda ${ }^{\mathrm{a}}$, L.C. Ordoñez ${ }^{\mathrm{b}}$, S. Ivvan Valdez ${ }^{\mathrm{c}, *}$<br>${ }^{a}$ Centro de Investigación en Matemáticas, A.C., Jalisco S/N, Col. Valenciana CP: 36023, Guanajuato, Gto, México, Apartado Postal 402, CP 36000, Mexico<br>${ }^{\mathrm{b}}$ Unidad de Energía Renovable, Centro de Investigación Científica de Yucatán. Parque Científico Tecnológico de Yucatán, Mérida, Yucatán, CP 97302, Mexico<br>${ }^{\text {c }}$ Cátedra-CONACYT Research Fellow, Centro de Investigación en Ciencias de Información Geoespacial, CENTROGEO, A.C., Contoy 137, Col. Lomas de Padierna, Delegación Tlalpan, CP. 14240, CDMX, Mexico

Received 2 January 2020; received in revised form 18 November 2020; accepted 20 December 2020
Available online 31 December 2020


#### Abstract

In this work, we approximated a set of unknown physical parameters for a semi-empirical mathematical model of a PEMFC. We used an Estimation of Distribution Algorithm (EDA) known as $U M D A^{G}$ to find the tuple that best reproduces the experimental polarization curve. We tackled non-derivable objective functions to perform robust parameter estimation. We compared the sum of the squared error with published results, and the sum and the median of the absolute error values were used to diminish or remove the effect of possible noise or outliers. Since the $U M D A^{G}$ requires a single user-given parameter (the population size) and presents a natural reduction of the variance, it was possible to introduce a variance-based stopping criterion. The obtained results were compared with the most up-to-date evolutionary algorithms, demonstrating that this proposal is competitive. We used four previously reported experimental datasets to get the parameters or validate them. Two of them were used to test the method and to compare it with reported results of recent bio-inspired metaheuristics. Then, we used the identified parameters to simulate the cases of the remaining data sets validating the correct estimation. Finally, we introduced a posterior statistical analysis (hypothesis test), which provided further information about dependencies and the impact of each parameter on the cell performance.


(c) 2020 International Association for Mathematics and Computers in Simulation (IMACS). Published by Elsevier B.V. All rights reserved.

Keywords: Parameter estimation; $U M D A^{G}$; PEMFC; Polarization curve; Probabilistic model building optimization; Semiempirical model

## 1. Introduction

A proton exchange membrane Fuel cell (PEMFC) is an electrochemical system that converts the chemical energy of hydrogen and oxygen directly into electricity by electrocatalytic reactions. Fig. 1 shows the basic structure of a PEMFC. It consists of an ionomer membrane in contact on either side with a catalytic layer, a diffusion layer, and a terminal plate with flow channels for the reactants. At the anode, hydrogen flows into the flow channels, and it is transported through the diffusion layer (DL) to the catalytic layer (CL) usually conformed by Pt/C catalyst. At Pt

[^0]
[^0]:    * Corresponding author.

    E-mail address: sergio.valdez@conacyt.mx (S.I. Valdez).
    https://doi.org/10.1016/j.matcom.2020.12.021
    0378-4754(©) 2020 International Association for Mathematics and Computers in Simulation (IMACS). Published by Elsevier B.V. All rights reserved.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Basic structure of a proton exchange membrane fuel cell.
catalytic active sites, $\mathrm{H}_{2}$ is oxidized to produce protons and electrons. The former moves to the cathodic catalytic layer through the membrane, while the later moves to the cathode current collector via the external electric circuit. Meanwhile, oxygen flowing in the cathodic flow channels diffuses through the DL to the cathodic CL, usually based on $\mathrm{Pt} / \mathrm{C}$ or $\mathrm{PtRu} / \mathrm{C}$ catalysts, where it is reduced with the electrons and protons to produce water and heat (Reactions (1)-(3)) [40].

Anode reaction:

$$
\mathrm{H}_{2} \leftrightarrow 2 \mathrm{H}^{+}+2 e^{-}
$$

Cathode reaction:

$$
\frac{1}{2} \mathrm{O}_{2}+2 \mathrm{H}^{+}+2 e^{-} \leftrightarrow \mathrm{H}_{2} \mathrm{O}
$$

Global reaction:

$$
\mathrm{H}_{2}+\frac{1}{2} \mathrm{O}_{2} \leftrightarrow \mathrm{H}_{2} \mathrm{O}
$$

Mathematical models are useful for the study of a PEMFC performance and for improving its design. There are different studies related to the modeling and simulation of a PEMFC [26,40,46,48]. Nevertheless, every mathematical model requires a set of parameters that are difficult to obtain experimentally, and that needs to be estimated.

The estimation of parameters is posed as an optimization problem, in which the objective function is usually defined as an error minimization of the model output for fitting experimental data [16,39,41,56]. A recent review in [53], shows the most common objective functions used in estimating PEMFC parameters. A candidate solution to this estimation problem is a set of parameters. A derivative-based method, usually, models the problem as the sum of squared errors, to use a derivable smooth function. Nevertheless, estimation of distribution algorithms (EDAs) deals adequately with non-derivable functions such as the one approached in this research. Regarding the error function, a small perturbation of a solution in the parameter space leads to an abrupt change in the model output, due to the non-linearity of the optimization problem, additionally, it could present multiple minimums and non-smoothness. Considering the EDAs niche of application, we propose to minimize the sum of squared errors for comparing with previous studies, the sum of absolute error values, and the median for reducing or eliminating the effect of outliers.

Several numerical algorithms have been used for solving the parameter estimation problem in PEMFC, such as simulated annealing [40,41], genetic algorithm (GA) [35,39], RNA-genetic algorithm [56], particle swarm optimization (PSO) [47,54], artificial bee swarm in [3], harmonic search in [4], artificial immune system in [5], and differential evolution algorithm $[10,50]$.

In [39], a GA is used for estimating the parameters of a fuel cell, this approach found adequate parameters; however, the author uses arbitrary execution parameters, and solutions from different executions present a large statistical variance. Thus, the confidence of the results is more related to the expertise of the final decision maker

than to the method for estimating the cell parameters. It is desirable that the GA returns similar results in several executions and that the GA stops when the best solution is found. These drawbacks are circumvented in [56], via new operators for the RNA-GA that improve the results of previous proposals. They also introduced a stopping criterion that automatically stopped the search when no further improvement is detected. However, the new operators make obscure the search process as well as the parameter settings for this algorithm. The Hybrid Artificial Bee Colony algorithm (HABC) [57] is one of the most competitive approaches for this problem, and it has an understandable behavior based on bees paths. However, the parameters settings are not intuitive, and the stopping criterion is arbitrary or depends on the expert criteria.

The covariance matrix adaptation evolution strategy ( $C M A E S$ ), belongs to derivative-free and stochastic methods for numerical optimization of non-linear or non-convex continuous optimization problems. The algorithm bases its heuristics on the iterative adaptation of the complete covariance matrix of a normal distribution of mutations, decomposes the total covariance matrix into a covariance matrix C and the global variance, called the step size control [19-21]. The $C M A E S$ learns all pair-wise dependencies between all parameters by updating a covariance matrix for the sample distribution [44].

Most of the mentioned algorithms lack a convergence criterion; hence, an expert must set the number of iterations and other parameters to ensure successful executions. Finally, the mentioned stochastic algorithms do not ensure a local optimum nor bounded computation time.

In the recent literature, modifications to swarm-intelligence and bio-inspired optimization algorithms have been introduced in order to improve their performance to estimate adequate parameters of a PEMFC, for instance, the Cuckoo Search Algorithm [9] is inspired in the Cuckoo parasite bird, uses a Levy random flight to evolve a set of nets and eggs, it applied to the optimization of parameters of the polarization curve obtained from [35]. Shark Smell Optimizer [43] is inspired in the shark predatory capacity based on following the odor of prey, it is devoted to engineering applications since its introduction when it was applied to a control problem. This algorithm is used for optimizing parameters of the polarization curves from the Ballard V 5 kW , and the SR-12 PEM 500 W. Teaching-Learning Based Optimization with Differential Evolution (TLBO-DE) [17], in the same vein than the Shark Smell algorithm, Teaching-Learning base Optimization Algorithm was proposed for improving a mechanical design based on emulating a teaching experience, in [50], it is combined with the widely-used differential evolution, the authors used this algorithm to set the parameters of the experimental polarization curve obtained from the 250 MW PEMFC. An adaptation of the Cuckoo Search Algorithm with Onlooker Bee Search (ObCS) is proposed in [59] for tunning the parameters for the nonlinear modeling approach of a PEMFC using type-2 fuzzy neural network (T2FNN), the objective function was the minimum of the mean of the square sum error. The Improve Fluid Search Optimization Algorithm (IFSO) [42], simulates Bernoulli's principle in fluid mechanics and is applied to three practical case studies including Horizon H-12 stacks, NedStack PS6, and Ballard Mark V 5 kW under different operating conditions with temperature variations between $30^{\circ} \mathrm{C}$ and $55^{\circ} \mathrm{C}$ and pressure variations between 1.0/1.0 Bar and 3.0/3.0 Bar. The Chaotic Binary Shark Smell Optimization is proposed in [18] as a variant of the Shark Smell Optimizer, this algorithm emulates the ability of the sharks in finding their preys. The binary operator permits to obtain the best response of the individuals for levels of forwarding movement, rotational movement, and chaotic improvement. To validate the algorithm the authors used the experimental data from a 250 MW PEMFC stack [35], the objective function is given by the minimum of the SSE. A version of the Coyote Optimization Algorithm was proposed in [55], the algorithm is based on the adaptation of the behavior of the coyote to the environment and also the coyote's experiences exchanging, it has a balance between exploration and exploitation, the objective function was the sum of the absolute error between the experimental data and simulations. For validating this algorithm the authors used two different PEMFC models: (a) 2 kW Nexa FC, and (b) 6 kW NedSstack PS6 FC. In [22], algorithms based on social behavior (Shuffled frog-leaping algorithm, Imperialist competitive algorithm and Firefly optimization algorithm) are applied to estimate parameters using the fitness function based on minimize the sum of squared errors (SSE) between the output voltage of each PEMFC stack and the estimated voltage by the semiempirical model in three set of experimental data obtained from: (1) NedSstack PS6 PEMFC stack with the rated power of 6 kW , (2) BCS 500-W PEMFC stack, and (3) open cathode 500-W Horizon PEMFC.

The Harris Hawks Optimization (HHO) is presented in [2], this algorithm is a gradient-free optimization technique based on the nature of Harris' hawks, they can track and detect the prey by their eyes, occasionally the prey cannot be seen easily, then, the hawks wait, observe, and monitor the desert site to detect prey. This technique uses the idea of exploration (nature of the Harris' hawks) and exploitation (surprise pounce). The Chaotic Harris

Hawks Optimization (CHHO) is presented in [32], this modification uses the HHO with chaos maps to foretell actions by formulating a set of chaotic equations, and was applied to estimate parameters of the semi-empirical model, minimizing the square sum of the errors of the simulation respect to the data obtained from four different stacks: (a) 250 W stack, (b) BCS 500 W , (c) SR-12 PEM 500 W , and Temasek 1 kW .

In [52] a mathematics-based algorithm named JAYA-NM is proposed to estimate parameters of a semi-empirical mathematical model of a PEMFC, this algorithm consists of two stages: the coarse global search stage (JAYA) and the intensive local search stage (Nelder-Mead simplex search algorithm). The reported results were compared with other bio-inspired algorithms as Grasshopper Optimization Algorithm, GOA [45], and Salp Swarm Optimizer, SSO, [33]. This last set of experiments are the most recent and most competitive reported in the specialized literature, in the best of our knowledge, hence, they are used in this article for comparing our proposal.

The novelty of the paper is the application of estimation of distribution algorithms to the PEMFC parameter estimation, the comparison of different evolutionary and swarm intelligence algorithms, the use of a variance-based stopping criterion in order to avoid an arbitrary stopping criterion, such as number of generations or iterations, that are usual in applications of this kind of algorithms, the introduction of two objective functions that automatically diminish (the sum of absolute values) and remove (the median) the effect of the outliers. The sum of squared errors is the most widely used function and it is adequate when you have data that fits exactly the theoretical model, nevertheless, that is not the case for experimental data, noisy data is very common, hence one of the benefits of using derivative-free algorithms is the potential of using multimodal non-derivable objective functions, we take advantage of this characteristic, the results show that the sum of absolute values and the median reports similar estimated parameters than the sum of square errors, hence we validate that such functions in combination with the studied algorithms can successfully solve the problem.

# 2. The semi-empirical mathematical model 

The semi-empirical mathematical model describes the characteristic polarization curve of a PEMFC. This model involves several parameters, which describe the overpotential in the anode and the cathode as a function of oxygen and hydrogen partial pressures [7,31]. The cell output voltage VFC is defined by Eq. (4).

$$
V_{F C}=E_{\text {Nernst }}-\eta_{\text {act }}-\eta_{\text {Ohmic }}-\eta_{\text {con }},
$$

where, $E_{\text {Nernst }}$ is the thermodynamic potential of the global reaction, $\eta_{\text {act }}, \eta_{\text {Ohmic }}$ and $\eta_{\text {con }}$ are the activation, ohmic and concentration voltage drops, respectively. At lower currents, the main voltage drop is due to the activation losses. At higher currents, the voltage drop is caused by the concentration losses or resistance to the mass transfer processes; and at intermediate currents, the voltage drop occurs due to the ohmic losses [50]. Each term of Eq. (4) is described in Eqs. (5), (6), (8) and (11), according to [31]:

$$
E_{\text {Nernst }}=1.229-0.85 \times 10^{-3}(T-298.15)+4.308 \times 10^{-5} T\left[\ln \left(\mathrm{P}_{\mathrm{H}_{2}}\right)+\frac{1}{2} \ln \left(\mathrm{P}_{\mathrm{O}_{2}}\right)\right]
$$

where $T$ represents the cell temperature $(\mathrm{K}), \mathrm{P}_{\mathrm{H}_{2}}$ and $\mathrm{P}_{\mathrm{O}_{2}}$ are the partial pressures (atm) of hydrogen and oxygen, respectively (see Table 1).

The activation overpotential, $\eta_{\text {act }}$, occurs due to reactions on the active surface of the anode and cathode sides and it is defined by Eq. (6).

$$
\eta_{a c t}=-\left[\xi_{1}+\xi_{2} T+\xi_{3} T \ln \left(\mathrm{C}_{\mathrm{O}_{2}}\right)+\xi_{4} T \ln (i)\right]
$$

where, $i$ is the cell current (A), $\xi_{i}(i=1, \ldots, 4)$, are the semi-empirical coefficients, [11], the oxygen concentration in the cathode interface, $\mathrm{C}_{\mathrm{O}_{2}}\left(\mathrm{~mol} \mathrm{~cm}^{-3}\right)$, it is defined in Eq. (7).

$$
\mathrm{C}_{\mathrm{O}_{2}}=\frac{\mathrm{P}_{\mathrm{O}_{2}}}{5.08 \times 10^{6} \times e^{-(498 / T)}}
$$

The ohmic loss $\eta_{\text {Ohmic }}$ results from the sum of the resistance of the proton conduction through the membrane and the resistance of electrons to the external electrical circuit, Eq. (8).

$$
\eta_{\text {Ohmic }}=i\left(R_{M}+R_{C}\right)
$$

Table 1
List of important variables of the semi-empirical mathematical model.
where, $R_{M}(\Omega)$ is the equivalent membrane impedance, and $R_{C}(\Omega)$ is the contact resistances both between the membrane and electrodes as well as the electrodes and the bipolar plates. $R_{M}$ is described by Eq. (9).

$$
\begin{aligned}
& R_{M}=\frac{\rho_{M} \times L_{c}}{A} \\
& \rho_{M}=\frac{181.6\left[1+0.03 \cdot(i / A)+0.062 \cdot(T / 303)^{2} \cdot(i / A)^{2}\right]}{[\psi-0.634-3 \cdot(i / A)] \cdot \exp [4.18 \cdot(T-303 / T)]}
\end{aligned}
$$

where $A$ is the active cell area $\left(\mathrm{cm}^{2}\right), L_{c}$ is the membrane thickness $(\mathrm{cm})$ and $\rho_{M}(\Omega \mathrm{~cm})$ is the specific membrane resistivity. $\rho_{M}$ is described by Eq. (10) and $\psi$ is the parameter related to the water content of the membrane which ranges between 13 and 24 [50]. This work considers the Nafion ${ }^{\circledR}$ membrane from Dupont, specifically, Nafion 115 $\left(L_{c}=127 \mu \mathrm{~m}\right)$.

The concentration overpotential, $\eta_{\text {con }}$ is defined in Eq. (11).

$$
\eta_{c o n}=-B \cdot\left(1-\frac{J}{J_{\max }}\right)
$$

where $B$ is the parametric coefficient, $J$ is the current density $\left(\mathrm{A} \mathrm{cm}^{-2}\right), J_{\max }$ is the maximum current density ( A $\mathrm{cm}^{-2}$ ). The concentration voltage drop also occurs due to fuel crossover and internal currents.

The saturation pressure of water vapor $P_{\mathrm{H}_{2} \mathrm{O}}^{*}$ is a function of the cell temperature $T(\mathrm{~K})$ as expressed in Eq. (12).

$$
\log _{10}\left(P_{\mathrm{H}_{2} \mathrm{O}}^{*}\right)=2.95 \times 10^{-2}(T-273.15)-9.18 \times 10^{-5}(T-273.15)^{2}+1.44 \times 10^{-7}(T-273.15)^{3}-2.18
$$

When the reactants are air and $\mathrm{H}_{2}$, their partial pressures are calculated by Eqs. (13) and (14).

$$
\begin{aligned}
& \mathrm{P}_{\mathrm{N}_{2}}=\frac{0.79}{0.21} \mathrm{P}_{\mathrm{O}_{2}} \\
& \mathrm{P}_{\mathrm{O}_{2}}=P_{c}-\left(R H_{c} \times P_{\mathrm{H}_{2} \mathrm{O}}^{*}\right)-\mathrm{P}_{\mathrm{N}_{2}} \times\left(\frac{0.291(i / A)}{T^{0.832}}\right)
\end{aligned}
$$

When the reactants are $\mathrm{O}_{2}$ and $\mathrm{H}_{2}$, the partial pressures are computed according to Eqs. (15) and (16).

$$
\begin{aligned}
& \mathrm{P}_{\mathrm{O}_{2}}=R H_{c} \times P_{\mathrm{H}_{2} \mathrm{O}}^{*}\left[\left(\exp \left(\frac{4.192(i / A)}{T^{1.334}}\right) \times \frac{R H_{c} P_{\mathrm{H}_{2} \mathrm{O}}^{*}}{P_{c}}\right)^{-1}-1\right] \\
& \mathrm{P}_{\mathrm{H}_{2}}=0.5 R H_{a} \times P_{\mathrm{H}_{2} \mathrm{O}}^{*}\left[\left(\exp \left(\frac{1.635(i / A)}{T^{1.334}}\right) \times \frac{R H_{a} P_{\mathrm{H}_{2} \mathrm{O}}^{*}}{P_{a}}\right)^{-1}-1\right]
\end{aligned}
$$

where $P_{\mathrm{H}_{2} \mathrm{O}}^{*}$ is the saturation pressure of water vapor (atm), $\mathrm{P}_{\mathrm{N}_{2}}$ is the nitrogen partial pressure at the cathode flow channel (atm). $P_{a}$ and $P_{c}$ are the inlet pressures (atm) at the anode and cathode, respectively, $R H_{a}$ and $R H_{c}$ are the relative humidity of vapor in the anode and cathode, and $A$ is the area of the membrane. The output voltage of the fuel cell stack is expressed in Eq. (17).

$$
V_{s}=n \cdot V_{F C}
$$

where $n$ is the number of cells connected in series.
We selected a set of parameters $\vec{\theta}=\left\{\xi_{1}, \xi_{2}, \xi_{3}, \xi_{4}, R_{c}, B, \psi\right\}$ in order to estimate the operational values with our proposed algorithm $[35,50]$.

# 2.1. Objective functions 

For parameter estimation problems in PEMFC there are several works in which different objective functions are used, more information see [53]. In this work, we use three objective functions to estimate the set of unknown parameters, $\vec{\theta}$, for the semi-empirical model described in Section 2. The first objective function, $S S E: \Theta \rightarrow \mathbb{R}_{+}$, Eq. (18), is the sum of the squared error between the output of the model and experimental data obtained from a polarization curve. The main goal of using this objective function is comparing with reported results in the literature. When using squared errors a single point which does not fit with the model could completely change the fitted polarization curve, hence to diminish the effect of such points, the second objective function, $S A E: \Theta \rightarrow \mathbb{R}_{+}$, is the sum of the absolute error, Eq. (19). Finally, often, the semi-empirical mathematical model reproduces the polarization curve only under certain conditions, or for some range of values, or the data is noisy or contains errors. For these cases, it is not straight-forward to determine which part of the polarization curve can be reproduced, for this end, we propose to use the median of the absolute error, this objective function $M A E: \Theta \rightarrow \mathbb{R}_{+}$, automatically fits most of the experimental data removing the effect of the points that cannot be adequately fitted.

$$
\begin{aligned}
& S S E(\theta)=\sum_{i=1}^{m}\left|V_{F C, i}-V\left(z_{i} ; \vec{\theta}\right)\right|^{2} \\
& S A E(\theta)=\sum_{i=1}^{m}\left|V_{F C, i}-V\left(z_{i} ; \vec{\theta}\right)\right| \\
& M A E(\theta)=\text { median }\left\{\left|V_{F C, i}-V\left(z_{i} ; \vec{\theta}\right)\right|\right\}_{i=1}^{m}
\end{aligned}
$$

where $m$ is the number of the experimental data, $V_{F C, i}$ is the experimental data, and $V\left(z_{i} ; \vec{\theta}\right)$ is the voltage output of the semi-empirical model. The problem of parameter estimation consists in determining on the search space $\vec{\theta} \in \Theta$ such that the objective function returns a minimal value in $\vec{\theta}$.

### 2.1.1. Discussion about objective functions

The use of three objective functions has a double purpose: (a) Since SSE, Eq. (18), is the most widely used function in parameter estimation, we use it to obtain results comparable to those previously reported; (b) direct search methods, such as Evolutionary Algorithms and EDAs, only depend on the objective function evaluation; thus, there is no need for proposing derivable or smooth functions. This fact is used in the SAE, Eq. (19), which has the advantage of being more robust than SSE. It is well known that SSE is affected by outliers, which means that a single wrong measure in the experimental data provokes a significant change in the fitted model. Additionally, SAE proportionally weights the error of each point while SSE assigns larger weights, consequently, they delivered different visual results. Besides, minimizing the median of the absolute values (MAE) fits most of the data removing

the effect of the worst fitted points. Thus, the last two functions deliver a robust parameter estimation, furthermore, regarding that the semiempirical model, like any other model, is not valid for all inputs of the PEMFC, the median minimization detects the region of the polarization curve which can be reproduced with the semiempirical model.

# 3. Estimation of Distribution Algorithms 

Estimation of Distribution Algorithms (EDAs) constitute a kind of metaheuristic algorithm [8,27,28,37] derived from the probabilistic modeling of Genetic Algorithms [14,15]. They were introduced in the field of evolutionary computation by Mühlenbein and Paa $\beta$ in 1996 [37,58].

EDAs are based on populations in which the descendants of a generation are obtained by sampling from a probabilistic model, estimated from the parent set. Hence, EDAs incorporate learning by estimating a parametric probability distribution from the selected set, intending to associate the highest probability to most promising regions. This is different from other genetic algorithms and other evolutionary algorithms in which the evolution of the populations is carried out by crossover and mutation operators [6,14,15,23-25,30].

### 3.1. The Univariate Marginal Distribution Algorithm with Gaussian models

In this work, we use an EDA named The Univariate Marginal Distribution Algorithm with Gaussian models $\left(U M D A^{G}\right)$ [29], this EDA is the real-coded counterpart of the binary algorithm introduced by Mühlenbein [36], is a generalization of previous works from Syswerda (1993), Eshelman and Schaffer (1993) and Mühlenbein and Voigt (1996) [13,38,49].

The $U M D A^{G}$ assumes that the $l$-dimensional joint probability function, computed at each iteration, is factored as a product of $l$ univariate and independent probability functions, as it is shown in Eq. (21).

$$
\mathbf{P}_{k}\left(\vec{\theta}_{k, h} \mid S_{\theta_{k}}\right)=\mathbf{P}_{k}\left(\theta_{k, h}^{1}, \theta_{k, h}^{2}, \ldots, \theta_{k, h}^{l} \mid S_{\theta_{k}}\right)=\prod_{i=1}^{l} \mathcal{P}_{k, i}\left(\theta_{k, h}^{i} \mid S_{\theta_{k}}\right)
$$

The probability functions $\mathcal{P}_{k, i}\left(\theta_{k, h}^{i}\right)$ are Normal probability functions with mean $\mu_{k, i}$ and variance $\sigma_{k, i}^{2}$, for $0<i \leq l$. These parameters are computed as follows:

$$
\mu_{k, i}\left(S_{\theta_{k}}\right)=\sum_{s=1}^{N_{\text {ind }}} \theta_{k, s}^{i} p_{k, i}\left(\theta_{k, s}^{i}\right), \quad \sigma_{k, i}^{2}\left(S_{\theta_{k}}\right)=\sum_{s=1}^{N_{\text {ind }}}\left(\mu_{k, i}-\theta_{k, s}^{i}\right)^{2} p_{k, i}\left(\theta_{k, s}^{i}\right)
$$

where $p_{k, i}\left(\theta_{k, s}^{i} \mid S_{\theta_{k}}\right)$ are weights associated with the $N_{\text {ind }}$ individuals.
The weighs $p_{k, i}\left(\theta_{k, s}^{i} \mid S_{\theta_{k}}\right)$ in Eq. (22) are computed in each iteration $k$ using the selected set from the truncation method [51], that is, given a threshold $v$ and the subset $S_{\theta_{k}} \subset \theta_{k}$, the assigned probability to each $\theta_{k, s}^{i}$ in the iteration $k$, for $0<i \leq l$ and $\vec{\theta}_{k, s} \in \theta_{k}$, is given by,

$$
p_{k, i}\left(\theta_{k, s}^{i} \mid S_{\theta_{k}}\right)= \begin{cases}\frac{1}{v}, & \text { if } \vec{\theta}_{k, s} \in S_{\theta_{k}} \\ 0, & \text { if } \vec{\theta}_{k, s} \notin S_{\theta_{k}}\end{cases}
$$

An additional contribution of this work is the stop criterion based on a variance norm. The stop criterion is given by comparing the norm of the normalized variance in Eq. (24) of the parameters with the tolerance tol ${ }^{2}$, (see Algorithm 1). This criterion is less arbitrary of giving a number of generations, and it actually detects when the exploration of the search space is stopped and the best solution found is unlikely improved.

$$
\operatorname{norm}_{k}=\left\|\left\{\frac{\operatorname{var}\left(\theta_{i}\right)}{U_{-} \text {Bound }\left(\theta_{i}\right)-L_{-} \text {Bound }\left(\theta_{i}\right)}\right\}_{i=1}^{l}\right\|
$$

In this research, the $U M D A^{G}$ is applied to estimate the parameters $\vec{\theta}=\left\{\xi_{1}, \xi_{2}, \xi_{3}, \xi_{4}, R_{c}, B, \psi\right\}$.

### 3.2. Parameter settings

The execution parameters of the $U M D A^{G}$ are $N_{\text {ind }}=100$, the number of selected individuals is $v=50$, the tolerance for stopping the algorithm is set to $\operatorname{tol}=1 e^{-10}$ and the search limits, given by the upper and lower bounds for each parameter are shown in Table 2.

# Algorithm $1 U M D A^{G}$ 

1: Input: $N_{\text {ind }}, N_{\text {gen }}$, tol and $v$.
2: Generate an initial population $\theta_{0}$ with $N_{\text {ind }}$ individuals.
3: $k=0$
4: while $k<N_{\text {gen }}$ and norm $_{k}>\operatorname{tol}^{2}$ do
5: Evaluate $\theta_{k}$ on the objective function.
6: Select the $v$ best individuals, $S_{\theta_{k}} \subset \theta_{k}$
7: Compute normalized norm norm $_{k}$ of the variance of the $S_{\theta_{k}}$.
8: if norm $_{k}<\operatorname{tol}^{2}$ then
9: Break;
10: else
11: $\quad$ Estimate the probability distribution function $P\left(x \mid S_{\theta_{k}}\right)$, see Section 3.1.
12: $\quad$ Sample $\theta_{k+1}$ with $N_{\text {ind }}-1$ new individuals from $P\left(x \mid S_{\theta_{k}}\right)$.
13: Replace $\theta_{k}$ with $\theta_{k+1}$, preserving the best solution of the $\theta_{k}$ (elitism).
$k=k+1$.
15: end if
16: end while
17: Return the best solution as the solution of the minimization problem.

Table 2
Upper and lower bound for searching the PEMFC model parameters [35,39].

These parameters are straight forward to set, in contrast with other algorithms, for example, the tolerance is basically a precision criterion, so, the tolerance is set to the same order of magnitude than the desired precision of the variables. Certainly, it must be below to the physically possible precision, in this case, if the physical parameters can be set with a precision of $1 e^{-4}$, then we use a precision below this number that is to say $1 e^{-5}$. Then, the square of this number is $1 e^{-10}$, considering that the variance is a square of a distance. We recommend setting the number of generations sufficiently large to avoid stopping the algorithm by this condition and use this value only as a safety criterion.

Finally, for finding the adequate population size, it is set to 10 times the number of variables, then it is increased until the result does not improve. Lower population sizes could lead to premature convergence, and suboptimal results, and greater populations will deliver an adequate optimum approximation but using more computational resources than those needed. The threshold for truncating the population is set to half of the population size, reducing this value could slow-down the convergence and could reduce the exploitation. In our experience, for this problem and those reported in the literature [27,29], preserving the half of the population size delivers optimum approximations with high precision. The objective function value of the worst preserved solution is an informative indicator about this parameter, if the worst preserved solution is improved in most of the generations, then the size of the selected set is adequate, if it is not, the size of the selected set must be reduced.

The $U M D A^{G}$ is executed using the three objective functions discussed in Section 2.1. The label $U M D A^{G}$-SSE is used to identify the SSE as the objective function, $U M D A^{G}$-SAE for the SAE, and $U M D A^{G}$-MAE for the MAE objective function.

## 4. Results

This section presents results for 4 cases. For test cases we estimate the configuration parameters: $\left\{\xi_{1}, \xi_{2}, \xi_{3}, \xi_{4}, R_{c}\right.$, $B, \psi\}$ for validation cases we change the operating conditions of the estimated configuration to demonstrate that the configuration is valid for two different operating conditions. We explain the methodology below.

Table 3
Operational conditions [35].

# 4.1. Definition of test and validation cases 

The experimental data were obtained from [35] using the Engauge Digitizer software [34].
We use 4 polarization curves, named as Case 1, Case 2, Case 3 and Case 4, delivered by 2 PEMFC configurations with different operating conditions. A configuration is a set of values of the parameters: $\left\{\xi_{1}, \xi_{2}, \xi_{3}, \xi_{4}, R_{c}, B, \psi\right\}$ while operating conditions are the anode pressure $P_{a}$, the cathode pressure $P_{c}$ and temperature $T$, see Table 3. In the case studies presented in this article, Cases 1 and 3 use the same configuration but different operating conditions, and Cases 2 and Case 4 use another configuration with different operating conditions. In consequence, if the estimated configuration parameters for Case 1 are correct, they should also reproduce the polarization curve of Case 3, applying the corresponding operating conditions. In all cases, we consider a stack with $n=24$ connected PEMFC, with values of $A=27 \mathrm{~cm}^{2}, L_{c}=127 \mu \mathrm{~m}, J_{\max }=860 \mathrm{~mA} \mathrm{~cm}^{2}, R H_{a}=1$ and $R H_{c}=1$.

In this regard, we distinguish two kinds of cases named Test and Validation. On one hand, Test cases are used to estimate the configuration parameters $\left\{\xi_{1}, \xi_{2}, \xi_{3}, \xi_{4}, R_{c}, B, \psi\right\}$ for the numerical simulation that best reproduces the experimental polarization curve, these are the Cases 1 and 2. On the other hand, Validation cases use the estimated configuration for evaluating different operating conditions, to show that a single set of configuration parameters reproduces two polarization curves with different operating conditions. In other words, an optimization execution is used for estimating $\left\{\xi_{1}, \xi_{2}, \xi_{3}, \xi_{4}, R_{c}, B, \psi\right\}$ to approximate the polarization curve of Case 1. The resulting estimated parameters are used for a numerical simulation with the operating conditions of Case 3 to demonstrate that the same configuration reproduces polarization curves for both operating conditions.

Hence, Cases 1 and 2 are Test cases and Cases 3 and 4 are Validation cases, respectively. The estimated parameters, as well as the error, are compared with previously reported methods [3,10,39,52,56,57], with the Genetic Algorithm, Particle Swarm Optimization from the Matlab Optimization Toolbox, and the Covariance Matrix Adaptation Evolution Strategy from [19].

### 4.2. Numerical results

### 4.2.1. Comparison with estimated values reported in literature of different EAs

We compare the configuration parameters found by different evolutionary algorithms (EAs) reported in the specialized literature with those found by our $U M D A^{G}$ version, we carried out executions using the $G A_{M}$ and $P S O_{M}$ from the Matlab Optimization Toolbox, and the $C M A E S_{M}$ code in Matlab obtained from the study in [19].

The results for Case 1 are shown in Table 4, for instance, the first 6 columns show estimations of configuration parameters reported in the specialized literature by the following bio-inspired algorithms: ARNA-GA [56], SGA [39], RGA [39], MPSO [3], GOA [45,52], SSO [33,52], they include the most recent proposals in the topic. For the sake of completeness, we execute the Matlab versions of the GA and PSO, because they are welltested implementations. We compare all results with the $C M A E S$ due to this technique have shown competitive results in complex applications [20,21,44]. The main purpose of this table is to show that the $U M D A^{G}$ version, introduced here, delivers similar configuration parameters than those found independently by different researchers, using different methodologies and software implementations. Notice that the $U M D A^{G}-S S E$ reports the lowest SSE value, and the second and third best are the PSO and GA, respectively.

The best executions with the SAE and MAE objective functions are also reported. The SAE reduces the outlier effect, while the MAE removes completely the outliers because it only uses the median of the error. Notice that even if the MAE uses the error of a single datum, it reports values similar to those of all other methodologies which use the whole data set.

Table 4
Comparison of the best results reported in the literature with those of the $U M D A^{G}, G A, P S O$ and $C M A E S$ for Case 1 with $P_{o}=3$ bar, $P_{c}=5$ bar, $T=353.15 \mathrm{~K}$.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Polarization curve fitted with data from [35] for the Test Cases 1 and 2 using $U M D A^{G}$-SSE (sum of squared error), $U M D A^{G}$-SAE (sum of absolute error), and $U M D A^{G}$-MAE (median of absolute error).

For Case 2 in Table 5, the values of the estimated parameters present a larger variance than those of the Case 1 , nevertheless, the $U M D A^{G}$ reports the best objective function values compared with the reported parameter values obtained by HABC [57], ARNA-GA [56], RGA [39], CHHO [32], GOA [45,52] and SSO [33,52], however, $C M A E S_{M}$ gets a better SEE value than $U M D A^{G}$.

Fig. 2, shows the experimental polarization curves and those calculated with $U M D A^{G}$-SSE, $U M D A^{G}$-SAE, and $U M D A^{G}$-MAE for Cases 1 and 2. It shows the SSE fitting with a blue dotted line, the SAE fitting with a black line, and the MAE fitting with a magenta dashed line, Fig. 2-(a). For Case 1, we can observe that the SAE fitting is visually closer to the points, this is the effect of using absolute values instead of squared errors, in the Case 2, some points have a greater effect on the fitting, Fig. 2-(b). For the MAE case, the fitting is worse in most of the points, because it only uses the median error, so we are pointing out that this estimation can be performed with noisy data or with less data than the other, and even though it uses a single error value, the estimated parameters are quite close to those estimated with SAE or SSE.

Fig. 2-(a), for Case 1, in the region of ohmic losses, shows a datum at 17 V and 14 A . outside the trend, which forced an intersection between SSE and SAE. As expected, SAE and MAE are more robust and less impacted by this type of data, whose variation could be due to different physical phenomena within the fuel cell such as the resistance to the transfer of protons through the membrane by the effects on the water content in it. Fig. 2-(b) shows the polarization curves computed with the parameters estimated by the $U M D A^{G}$-SSE, $U M D A^{G}$-SAE, and $U M D A^{G}$ MAE methods. The three polarization curves closely fit the experimental data, however, notice that the MAE estimation is slightly different, because this estimation ignores the largest errors and focuses on the median, the main advantage of this estimation is that one can fit an experimental curve even if there are atypical data or noise, because this estimation is the minimization of a single error measurement, nevertheless, one cannot know a priori which such measurement is. Also, notice that a derivative-based algorithm could never approach this objective function.

# 4.3. Comparison with the most recently reported estimations using a standard dataset 

We compare the $U M D A^{G}$ respect to the competitive Adaptive Differential Evolution algorithm (ADE) presented in [10] in 2014, and the JAYA and JAYA-NM [52] that are two competitive algorithms published in 2019. Table 6 shows the best solution reported for all the comparing algorithms. In the previous comparison, the data is extracted from the plot of the polarization curve using specialized software, on the contrary, in this case, all the algorithms use exactly the same dataset as it is provided by [52]. The $U M D A^{G}$ version used here delivers the best results, recall that the difference between the results in Table 4 and those in Table 6 is due to the small differences in the

Table 5
Comparison of the best results reported in the literature with those of the $U M D A^{G}, G A, P S O$ and $C M A E S$ for Case 2 with $P_{o}=1$ bar, $P_{c}=1$ bar, $T=343.15 \mathrm{~K}$.

Table 6
Comparison of $U M D A^{G}$-SSE results using the experimental polarization curve reported in [52]. Case 1 with $P_{a}=3$ bar, $P_{c}=5$ bar, $T=353.15 \mathrm{~K}$.

Table 7
Comparison of $U M D A^{G}$-SSE results using the experimental polarization curve reported in [52]. Case $2\left(P_{a}=1\right.$ bar, $P_{c}=1$ bar, $T=343.15 \mathrm{~K}$ ).

datasets. Similarly, Table 7 presents the comparative results of the estimated parameters using the experimental data presented in [52]. Our results show a competitive value of SSE using the $U M D A^{G}$ compared to the JAYA and JAYA-NM algorithms. For the sake of completeness, the comparing algorithms for Case 1 and Case 2 are different because not all the authors report both cases.

# 4.4. Validation cases 

Test cases used for estimating the configuration parameters $\left\{\xi_{1}, \xi_{2}, \xi_{3}, \xi_{4}, R_{c}, B, \psi\right\}$, and validation cases use the same configuration but changing the operating conditions that are the anode pressure $P_{a}$, the cathode pressure $P_{c}$ and temperature $T$. The operational conditions for validation Cases 3 and 4 are in Table 3. Fig. 3, shows the polarization curve for the validation cases, if the estimated parameters for Case 1 are correct, then they must reproduce also the polarization curve of Case 3, because is the same configuration with different operational conditions. For this case, the minimum values of each objective function using by the $U M D A^{G}$ were $S S E=5.72271, S A E=5.97704$ and $M A E=0.24353$, respectively, see Fig. 3-(a). In the same vein, if the estimated parameters for Case 2 are correct, they must reproduce also the polarization curve of Case 4, thus, Fig. 3-(b), shows that the estimations are correct and the respective minimum values of objective functions were $S S E=1.45053, S A E=3.07005$ and $M A E=0.16672$.

We can observe that the SSE values of the validation cases are consistent with the SSE values of the estimation cases, this indicates that the results of the estimates can reproduce different operating conditions and with comparable values of the objective function with respect to the results of the parameter estimation cases.

### 4.5. Robustness and statistical analysis of 30 independent executions

Bio-inspired algorithms such as evolutionary and swarm-intelligence algorithms are stochastic methods that delivers a different solution each time they are executed. Hence, quite often, they are compared using statistical measures and hypothesis tests, using a series of independent executions. The previous comparisons show the competitiveness of this proposal with reported solutions in the specialized literature. These comparisons are made using the best solutions from each algorithm. According to the results in Tables 4 and 5 the most competitive

![img-2.jpeg](img-2.jpeg)

Fig. 3. Polarization curve fitting with data in [35] for the validation cases of $U M D A^{G}$-SSE, $U M D A^{G}$-SAE and $U M D A^{G}$-MAE.
algorithms are the $U M D A^{G}, P S O, G A$, and $C M A E S$, thus we perform statistical comparisons and hypothesis test among them.

The columns of Table 8, summarizes the results from 30 independent executions of $U M D A^{G}, G A_{M}, P S O_{M}$, and $C M A E S_{M}$. Notice that the configuration parameters delivered by the algorithms present a low standard deviation, and in most of the cases, the lowest is that of the $U M D A^{G}$. The standard deviations are smaller than the mean and the search limits, which means that the $U M D A^{G}$ reports a consistent estimation in all the executions, for instance, $\xi_{1}$ reports a standard deviation of three orders of magnitude below the mean. In most of the solutions, except one, the parameters of the best solution are inside the region of plus/minus the standard deviation. Thus, it is inferred that the $U M D A^{G}$ behaves similarly in all executions. This is a desirable characteristic for an optimization algorithm that is going to be used to evaluate the behavior of PEMFC at different experimental conditions, this shows that it is consistently delivering similar parameters in each execution. In the SSE row, it is shown that $U M D A^{G}$ has the minimum mean of the objective function as well as standard deviation, confirming that it is consistent in the estimated parameters and objective value. Hence, the $U M D A^{G}$ presents the best performance for this sample of executions, then, we test if this performance is significantly different from that of the other algorithms.

The Boostrap hypothesis test is a non-parametric test that does not assume anything about the shape of the distributions of the data [12], this is the exact case for these experiments in which we have not a basis to assume a parametric distribution of the results. The hypothesis test is applied over the mean of the objective function, $S S E$, for comparing $G A, P S O, C M A E S$ and $U M D A^{G}$. For Case 1, $U M D A^{G}$ is better than $G A_{M}$ with a $p$-value of $8.4 e^{-4}, U M D A^{G}$ is better than $P S O_{M}$ with a $p$-value of 0.0210 , and $U M D A^{G}$ is better than $C M A E S_{M}$ with a $p$-value of $5.5 e^{-5}$. For Case 2, $U M D A^{G}$ is better than $G A_{M}$ with a $p$-value of 0.000 , and it is better than $P S O_{M}$ with a $p$-value of 0.01689 , finally, the $C M A E S_{M}$ is better than the $U M D A^{G}$ with $p$-value of 0.0593 .

In order to demonstrate that the algorithm is consistent in the estimated configuration parameters even if the objective function is changed, columns four and five show the results from 30 independent executions of the algorithm with the sum of absolute error values (SAE), and the median of the absolute error (MAE), in addition, notice that the maximum change in the means of the parameters estimated with the SSE, SAE and MAE functions is the $R_{C}$ parameters, while the main visual change in the polarization curves of Figs. 2 and 3 is the curvature, hence, seemingly there is observed a correlation between the curvature of the polarization curve and the $R_{C}$ value, note that this observation comes directly from the execution data without using knowledge of the model.

# 4.6. Statistical analysis of parameter correlations 

This section introduces a statistical analysis using the output data from the 30 independent executions. They are used to compute a correlation matrix to infer the most crucial parameters for the fuel cell performance, if the interaction between the variables is known, we can understand better the operation of a PEMFC.

Table 8
Mean $\pm$ standard deviation of parameters and objective functions from 30 independent executions of different optimization algorithms.
In Fig. 4, the lower triangular matrix shows the correlation values between the row and column parameters, while the upper triangular matrix shows an ellipse if the two parameters are considered correlated. To know if two variables are correlated we applied a non-parametric hypothesis test with a 0.9 confidence level, using the cor.test function from the R language [1]. The obtained value was used to capture any possible relation between two variables. Correlations and a hypothesis test are computed, using the Kendall formula, to capture non-linear correlations. If a variable is highly correlated with the objective function, then, we elucidate that a perturbation in such a variable significantly perturbs the cell performance. Correspondingly, if two or more variables are correlated, one elucidates that such variables must be perturbed together to significantly modify the cell performance. Fig. 4 shows that in all cases, the most impacting variable in the objective function is the water content in the membrane, $\psi$, due to all four correlation matrices present thin ellipses in the position of $\psi$ row and objective function column. The purpose of showing matrices from SEE and SAE is to show the variables that are consistently correlated in both estimations, thus, it is more plausible that these correlations are correct, notice that $\psi$ is present in all matrices, which additionally is consistent with the physics of the cell. Other less impacting correlations with the objective functions are those of $\xi_{4}$ and $\xi_{2}$. Notice that $\xi_{2}$ shows a high correlation for the first case but not for the second. The semi-empirical coefficients $\xi$ cannot be directly tuned in a real-world fuel cell, because they are a function of other physical parameters which, for the sake of completeness, are explicitly defined in Ref. [11]. On the other hand, the water content in the membrane, $\psi$, is the most important correlation detected in this analysis, considering that it could be directly adjusted in a real fuel cell and that it is the most impacting parameter of the cell performance. Finally, notice that $\psi_{2}$ and $\psi_{4}$ present the second-largest correlation with the objective function for Case 1 and Case 2 , respectively.

# 4.7. Discussion 

There exist different mathematical models, each of them allows the study and analysis of different processes involved in the operation and performance of a fuel cell. The main advantage of the semi-empirical mathematical model is that it reproduces the whole polarization curve in contrast with the macro-homogeneous [26] and the agglomerate models [46], which partially reproduce the curve. On the opposite side, it obfuscates details of the internal processes and the impact of the fuel-cell geometry.

Hence, we recommend this model for a first-approach design, then, a more detailed design can be produced and simulated via the macro-homogeneous and the agglomerate models, in this sense, the different mathematical models are complementary. The semi-empirical model permits us to understand the effect of the semi-empirical parameters $\xi_{1}, \xi_{2}, \xi_{3}, \xi_{4}$ on the performance, measured via the polarization curve.

The application of the $U M D A^{G}$ in this article shows its feasibility as a tool for estimating parameters in the semi-empirical model for PEMFC, in addition to finding a solution with less error than all the other proposals in the literature. The results of the $U M D A^{G}$ are comparable with the results of the $G A$, the $P S O$, and the $C M A E S$. Table 8, shows that, for Case 1, the $U M D A^{G}$ presented a smaller standard deviation for SSE than the other algorithms, the $C M A E S$ presented a higher standard deviation for SSE compared to $G A, P S O$, and $U M D A$, and the bootstrap hypothesis test indicates that exists more variability in its solutions. Only for Case 2, the $C M A E S$ outperformed all algorithms in SSE values. Our proposal presents two important benefits: it requires of a single user-given parameter, that is the population size, which is straight forward set by increasing an initial guess until there is no improvement in the optimum approximation, besides, in contrast with other evolutionary algorithms, this proposal does not require of an arbitrary or expert-set stopping criterion, the convergence is detected via the norm of the variance of the current population and the algorithm is automatically stopped.

## 5. Conclusions

In this work, we present a statistical comparison of four evolutionary algorithms for the parameter estimation of a PEMFC, they are the $U M G A^{G}, G A, P S O$, and $C M A E S$, in addition, they are compared with reported results in the literature. We found advantageous to use the $U M D A^{G}$ in contrast with other methods, besides its simplicity, low computational cost in operations and memory, and its performance to estimate the parameters. Then, we propose to use the convergence, measured via the variance of the search distribution, as a stopping criterion for the $U M D A^{G}$. The convergence property, which is not the rule in Evolutionary Algorithms, is advantageous for reducing the number of execution parameters and avoiding arbitrary stopping criteria such as the number of

![img-3.jpeg](img-3.jpeg)

Case 1 with SSE
![img-4.jpeg](img-4.jpeg)

Case 2 with SSE
![img-5.jpeg](img-5.jpeg)

Case 1 with SAE
Fig. 4. Correlation matrix of 30 independent executions of cases 1 and 2 with SSE and SAE. The lower side of the correlation matrix shows numeric values, while the upper shows an ellipse representation, the narrower an ellipse is the higher the correlation.
iterations/generations, which provokes suboptimal solutions, wasted computations, or requires of expert tuning. The $U M D A^{G}$ improves the confidence of the results because it converges to a small region in the variable space and the objective space. This ensures two crucial features of the solution: (1) robustness, considering that the parameters estimated in 30 independent executions belong to a closed neighborhood and share similar objective values, that is to say, any of the 30 executions of our proposal delivers an adequate estimation, (2) the solution is a closed approximation to a local optimum because the algorithm intensively samples in a very small neighborhood of the best solution at the last iterations.

The $U M D A^{G}$ is suited for handling non-derivable and multimodal objective functions, we use this advantage for approaching the minimum of three objective functions, which solution is consistent with previously reported results, but presents a lower error, besides we approach robust estimations. In this regard, the SSE is quite sensitive to outliers, nevertheless, it is the most widely used in literature due to its differentiability. The objective function that uses the sum of the absolute values of the error, SAE, is less biased by atypical data, while MAE practically avoids any outlier.

The information from several executions is used to determine relations among variables and the objective function, in this regard, we infer that the water content in the membrane, $\psi$, is the most critical parameter in the PEMFCs used in this study.

The results showed that the $U M D A^{G}$ is a competitive algorithm compared with the state of the art and the most recent bio-inspired algorithms in the literature.

Future work contemplates the use of parameters estimated for the semi-empirical model to feed the agglomerate and macro-homogeneous models, to define consistent simulations of the same fuel cell through all of them.

# CRediT authorship contribution statement 

Luis Blanco-Cocom: Software, Data curation, Writing - original draft, Visualization, Investigation. Salvador Botello-Rionda: Project administration, Supervision, Conceptualization, Methodology, Resources. L.C. Ordoñez: Validation, Writing - review \& editing. S. Ivvan Valdez: Formal analysis, Writing - original draft, Writing - review \& editing, Conceptualization, Methodology, Supervision, Visualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This article was supported by CONACYT, Mexico under grant 100236.
S. Ivvan Valdez is supported by Grant Cátedras CONACYT, Mexico number 7795.
