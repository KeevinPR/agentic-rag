# Chapter 15 

## Contents lists available at ScienceDirect

## Annals of Nuclear Energy

journal homepage: www.elsevier.com/locate/anucene

## Technical Note

## Optimization of depleted uranium loading in fresh core of large sized Indian PHWR by evolutionary algorithm

Surendra Mishra ${ }^{\mathrm{a}, *}$, R.S. Modak ${ }^{\text {b }}$, S. Ganesan ${ }^{\mathrm{c}}$<br>${ }^{a}$ Safety Directorate, Nuclear Power Corporation of India Limited, Mumbai 400 094, India<br>${ }^{\mathrm{b}}$ Theoretical Physics Division, Bhubha Atomic Research Centre, Mumbai 400 085, India<br>${ }^{\mathrm{c}}$ Reactor Physics Design Division, Bhubha Atomic Research Centre, Mumbai 400 085, India

## A R T I C L E I N F O

Article history:
Received 20 July 2010
Received in revised form 19 October 2010
Accepted 1 December 2010
Available online 7 January 2011

## Keywords:

Nuclear reactor PHWR Optimization Evolutionary algorithm Depleted uranium

## A B S T R A C T

Pressurised Heavy Water Reactors (PHWRs) are based on Natural Uranium (NU) fuel and heavy water as moderator and coolant. At the beginning of reactor life of PHWR, if all NU bundles are loaded, the power peaking is high and full power cannot be drawn. In order to draw full power, it is possible to flatten the power in fresh core by loading some depleted uranium (DU) (or Thorium) bundles. The determination of the best possible locations of DU bundles which maximize economy and preserve safety is a constrained combinatorial optimization problem. This paper presents optimization of DU bundle distribution in the fresh core of the 700 MWe PHWR. An evolutionary technique based on Estimation of Distribution Algorithm (EDA) is used to determine the optimum DU loading pattern. The best suitable locations for DU bundles are determined using EDA. In order to meet some additional constraints, some additional DU bundles are placed at 11th and 12th bundle locations in few channels. These channels are selected manually. The overall aim of the optimization is to maximize $K$-effective and get 100\% full power without violating safety parameters such as maximum permissible bundle power, channel power peaking factor and permitted reactivity worth in shut-down system. The optimum configuration is explicitly presented.
(c) 2010 Elsevier Ltd. All rights reserved.

## 1. Introduction

In India, a series of PHWR designs have evolved in course of time. The earliest reactors were of 220 MWe capacity with moderator dump as a shut-down system, which were later indigenized and standardized (Bajaj and Gore, 2006) with two independent shut-down systems. The 700 MWe PHWR is a more advanced large-sized design, expected to be commissioned in future. Like the 220 MWe PHWR, the 700 MWe PHWR is a horizontal tube type reactor fuelled with Natural Uranium (NU) with heavy water as both coolant and moderator. The coolant is physically separated from the moderator by being contained inside several pressure tubes where it is maintained at high temperature $\left(\sim 288^{\circ} \mathrm{C}\right)$ and pressure. The moderator heavy water is at a relatively low temperature $\left(\sim 76^{\circ} \mathrm{C}\right)$ and is un-pressurised. The reactor core consists of 392 horizontal pressure tubes arranged along a square lattice of 28.6 cm pitch. Fuel in the form of cluster of 37 element fuel pins and the coolant are contained within these pressure tubes. The direction of coolant flow in adjacent channels (pressure tubes) is opposite. The direction of the bundle movement (fuelling direction) is the same as that of the coolant flow, so that adjacent channels are fuelled in opposite directions. The direction of coolant flow

[^0](and fuelling) is referred to as axial direction. The fuel is in the form of a string of 12 bundles, each bundle is a 37 -pin cluster of 49.5 cm length. All the 12 bundles are in the active portion of the core. The 12 bundle locations are numbered as $1,2,3, \ldots, 12$; in the direction of fuelling.

For the purpose of reactor regulation there are 14 Zone Control Compartments (ZCC), 17 Adjuster Rods (AR) symmetrically grouped into eight banks and 4 Control Rods (CR). There are two independent shut-down systems called shut-down system-1 (SDS\#1) and shut-down system-2 (SDS\#2) for reactor protection. The SDS\#1 consists of 28 shut-off rods dropping from the top of the core. The SDS\#2 consists of six perforated horizontal tubes allowing large amount of neutron poison to get mixed in the moderator. In addition, there is a Regional Over power Protection (ROP) system which senses excess power in any local region of the core by means of two sets of detectors and trips the reactor (by sending signal to SDS\#1 or SDS\#2) to avoid the on-set of coolant dry out or fuel centre line melting. More detailed description can be found in reference (Bhardwaj, 2006). The optimum DU distribution is expected to preserve the worth of SDS\#1. The SDS\#2 has very large worth and need not be checked. Moreover, the DU loading should provide sufficient operating margin and not cause spurious trip by ROP. The channel power peaking factor (i.e. CPPF defined as maximum of ratio of instantaneous channel power to time averaged channel power) is used to limit the channel power for


[^0]:    * Corresponding author. Tel.: +91 222599 4678; fax: +91 222599 3318.

    E-mail address: smishra@npcil.co.in (S. Mishra).

700 MWe core. Lower CPPF value provides more operating margin from ROP trip.

At the beginning of the PHWR core life, when the entire core is loaded with fresh NU fuel bundles, the power distribution would be highly peaked in the centre due to lack of flux flattening. Hence, it will not be possible to get the full rated power from the core right from beginning unless some other way of achieving power flattening is followed. It is possible to flatten the power distribution by loading some Thorium or DU bundles in the central region of the core. The DU bundles are preferable over Thorium because they are easy to manufacture. The DU bundles contain about $0.3 \mathrm{wt} . \%$ $\mathrm{U}^{235}$. Because of lower content of $\mathrm{U}^{235}$ in DU, sometimes it is called Deeply depleted uranium (DDU) bundles.

While choosing the locations of DU bundles, the following considerations are taken into account:
(1) $K_{\text {eff }}$ is maximum as far as possible so that the pre-fuelling period of the reactor becomes longer leading to better fuel economy.
(2) Reactor power is close to $100 \% \mathrm{FP}$.
(3) Channel power peaking factor (CPPF) is less than the specified value.
(4) Maximum bundle power is less than the limiting value.
(5) Maximum channel power is less than the limiting value.
(6) Sufficient reactivity worth in the shut-down systems.
(7) The loading pattern should be convenient in practice.

Earlier a similar problem has been solved for the 220 MWe Indian PHWR for Thorium and DU bundles; which is smaller in size than the 700 MWe PHWR. The first solution was given about two decades ago by Balakrishnan and Kakodkar (1994) using gradient search method. A suitable distribution consisting of 35 Thorium bundles was arrived at. The same problem of Thorium loading was revisited recently by Mishra et al. (2009) using two stochastic techniques i.e. Genetic Algorithm (GA) and Estimation of Distribution Algorithm (EDA). The loading pattern for the 220 MWe PHWR using DU bundles having $0.6 \mathrm{wt} . \% \mathrm{U}^{235}$, was also obtained recently by EDA (Mishra et al., 2010).

In the present paper, we try to find optimum distribution using DU bundles ( $0.3 \mathrm{wt} . \% \mathrm{U}^{235}$ ) for 700 MWe Indian PHWR with some restrictions on locations. A simple loading pattern can be generated if DU bundles are chosen to lie at a fixed bundle position (say 7th bundle position in axial direction). The 700 MWe PHWR is larger and has more bundle locations than 220 MWe PHWR. However, it has more symmetry properties. Exploitation of symmetry and restrictions on DU locations mentioned earlier help to reduce the problem size. The 700 MWe PHWR has ROP system for reactor trip. The DU loading should leave sufficient operating margin. The best locations for DU bundle have been obtained using EDA algorithm and then to meet the required reactivity worth in 26 SRs ( 2 missing out of 28 SRs) few more DU bundles are loaded using heuristic information. The final pattern arrived at using EDA and heuristic information satisfies all criteria.

The paper is organized as follows: In Section 2, problem solving technique is presented. Section 3 presents results obtained by present approach. Section 4 gives conclusion and discussion.

## 2. Problem solving technique

There are total 392 fuel channels (from A-W in $Y$-direction and $1-22$ in $X$-direction) in 700 MWe reactor core. These channels are horizontal and extend in $Z$-direction up to about 500 cm . There is top-bottom and left-right symmetry in the core. In all there are $392 \times 12=4704$ fixed locations for fuel bundles. Choosing a few hundred best locations for DU bundles out of the 4704 locations
is a large-sized constrained combinatorial optimization problem. In the XY-plan, the core has reflective symmetry along both $X$ and $Y$ directions. There is also symmetry with respect to rotation in XY plane by $90^{\circ}$. We assume that the DU bundle locations also follow these symmetries. Thus it is enough to determine locations of DU bundles in the 53 channels. The locations in other channels are determined by symmetry. There are 12 bundles in each channel. The problem size is reduced further by making certain choices along $Z$-direction. The DU bundle is placed only at a fixed location along $Z$-direction, say the 7th location. The numbering of bundles in $Z$-direction is along direction of fuelling and adjacent channels are fuelled in opposite direction. Hence, the DU bundles will lie only in two planes perpendicular to $z$-axis. The generated loading pattern will be simple and easier for actual loading.

Four types of optimization studies are carried out: DU bundles are placed at only one axial location which can be 7th, 8th, 9th or 10th location. This is shown schematically in Fig. 1 as cases AD. The four cases analyzed are named as follows:

- Case A: The DU bundles can be loaded only in two radial planes at 7th bundle location along the direction of fuelling.
- Case B: The DU bundles can be loaded only in two radial planes at 8th bundle location along the direction of fuelling.
- Case C: The DU bundles can be loaded only in two radial planes at 9th bundle location along the direction of fuelling.
- Case D: The DU bundles can be loaded only in two radial planes at 10th bundle location along the direction of fuelling.

The search space reduces drastically due to various symmetries and restrictions on DU loading and hence parallel computing was not necessary. The optimization could be carried out on a serial computer.

### 2.1. The optimization problem

The optimization problem is defined as follows.
Objective: To maximize the effective multiplication factor $\left(K_{\text {eff }}\right)$. Constraints: Following constraints are imposed.

- The reactor power (FP) should not be less than FPO (100\% FP).
- The maximum channel power (MCP) should be less than MCPO ( 7.2 MW ).
- The maximum bundle power (MBP) should be less than MBPO ( 917 kW ).
- The maximum channel power peaking factor (CPPF) should be less than CPPF0. The maximum CPPF0 which allows $100 \%$ FP operation is about 1.12 but here we have considered CPPF0 $=1.10$.
- The reactivity worth of shut-down system (SDS) should not be less than SDS0 ( 70 mk ).

We use the "penalty method" for handling constraints. The penalty method penalizes infeasible (or unfavorable) individuals. In
![img-0.jpeg](img-0.jpeg)

Fig. 1. Possible location of DU in various cases.

general, it transforms a constrained optimization problem to an unconstrained problem by defining penalty function (Michalewicz, 1999). Here, the objective function to be maximized has been defined to take care of constraints as follows:
$\mathrm{Fit}=\mathrm{K}_{\mathrm{eff}}-\mathrm{F} 1-\mathrm{F} 2-\mathrm{F} 3-\mathrm{F} 4-\mathrm{F} 5$
where $\mathrm{F} 1=(\mathrm{FP} 0-\mathrm{FP}) \times$ Afp if $\mathrm{FP}<\mathrm{FP} 0$ and zero otherwise, $\mathrm{F} 2=$ (CP - CP0) $\times$ Acp if CP > CP0 and zero otherwise, F3 $=(\mathrm{CPF}-$ CPF0) $\times$ Acpf if CPF > CPF0 and zero otherwise, F4 $=(\mathrm{BP}-\mathrm{BP} 0) \times$ Abp if $\mathrm{BP}>\mathrm{BP} 0$ and zero otherwise, $\mathrm{F} 5=(\mathrm{SDS} 0-\mathrm{SDS}) \times$ Asds if SDS $<$ SDS0 and zero otherwise.

The notation used is as follows:
$\mathrm{FP} 0=100$, corresponding to $100 \% \mathrm{FP}$.
FP is the maximum allowable power in a given configuration.
CP0 is corresponding to maximum permitted channel power i.e. 7.2 MW.

CP is the maximum channel power in a given configuration.
CPF0 is corresponding to the permitted channel power peaking factor i.e. 1.10 .
CPF is the maximum channel power peaking factor in a given configuration.
BP0 is corresponding to maximum permitted bundle power i.e. 917 kW .
BP is the maximum bundle power in a given configuration.
SDS0 is the minimum worth of shut-down system i.e. 70 mk .
SDS is the worth of SDS in a given configuration.
Afp, Acp, Acpf, Abp and Asds are suitably chosen constants to give a weightage to each of the factors. The procedure to decide these constants is somewhat arbitrary and is based on experience. It is similar to the one used in the earlier work (Mishra et al., 2009, 2010).

The objective function (also called fitness function) given by Eq. (1) has to be evaluated to determine the fitness of any given configuration.

### 2.2. The computational tool

A 3-D 2-group neutron diffusion code is needed to evaluate the fitness of any given configuration. An in-house computer code 'DOLP' has been developed and validated against AECL PHWR benchmark (Judd and Rouben, 1981). It uses finite differencing and standard inner-outer iterations to solve the $K$-eigenvalue problem. The homogenized two energy group cross-sections for NU ( $0.7115 \mathrm{wt} . \% \mathrm{U}^{235}$ ) and DU ( $0.3 \mathrm{wt} . \% \mathrm{U}^{235}$ ) bundles, required for diffusion calculations, were obtained by two separate lattice calculations. The isotopic purity of $\mathrm{D}_{2} \mathrm{O}$ considered in the simulation is $99.8 \mathrm{wt} . \%$ and $99.7 \mathrm{wt} . \%$ for moderator and coolant respectively. For this purpose, the 2-D integral transport theory code CLUB (Krishnani, 1992) was used. In these calculations, 69 energy group WIMSD library derived from ENDF/B-VI. 8 basic evaluated nuclear data file was used.

### 2.3. Optimization methods

There exist gradient based methods (Carter, 1997) in which one starts with a guess distribution and make small changes to look for improvements. This generally requires a good degree of intuition and experience. Since small changes are made around a certain configuration, there is a possibility of getting trapped in a local minimum (Salomon, 1998). There exists another technique called "simulated annealing" (Kropaczek and Turinsky, 1991) in which the same gradient method is used, but one occasionally accepts an inferior solution with certain probability. This probability is
slowly reduced as the optimum solution is approached. This helps in getting out of local minima and reaching to a global optimum. There are yet other techniques based on Genetic Algorithms (GA), particle swarm optimization (PSO) and ant colony optimization (ACO). These algorithms can be found in Goldberg (1989), Carter (1997), Pereira et al. (1999), Mishra et al. (2009), Lima et al. (2008) and Meneses et al. (2009).

There exists slightly different algorithm called Estimation of Distribution Algorithm (EDA). In EDA (Jiang et al., 2006; Mishra et al., 2009, 2010), the combination in GA is replaced by estimation of distribution and sampling as per this distribution to generate new candidate solutions. The simulated annealing, GA, ACO PSO and EDA have been extensively used to solve light water reactor fuel management and control design problems (Pereira and Sacco, 2008; Montes et al., 2004; Jiang et al., 2006; Turinsky et al., 2005).

In the present paper, we have applied EDA technique to optimize the initial fuelling in PHWR.

### 2.4. Estimation of distribution algorithm

EDAs belong to the class of population based optimization algorithms. The two operators in EDA are estimation of distribution and sampling. In each generation, $N$ individuals are generated by sampling probability distribution. The fitness is evaluated for each of them by diffusion calculations and the best $M(<N)$ individuals are selected to estimate probability distribution. The probability that a given location is occupied by NU or DU bundle is estimated from the selected M individuals. The performance of an EDA highly depends on how well it estimates and samples the probability distribution. Univariate Marginal Distribution Algorithm (UMDA) assumes no interaction among variables. The probability distribution is estimated using UMDA (Jiang et al., 2006) in the present case. A pseudo model of the algorithm used for optimization is given in Fig. 2. The Probability Distribution Function (PDF) was generated using $30 \%$ dominated individuals [item 4 in Fig. 2] of the population size (i.e. 100). Alpha is chosen 0.05 . This value is tuned by some trial calculations. In general, smaller values of alpha are expected give better exploration but slower convergence.

We try to optimize the loading pattern with the number of DU bundles lying within a certain pre-decided range or interval. Let the interval be denoted by $\left(N_{d}-18, N_{d}+18\right)$. The values of $N_{d}$ considered here is: 20 . Thus in the optimization study the possible number of DU bundle is $2-38$ at selected locations in the 53 number of fuel channels. In EDA, the total number of DU bundles may not remain constant while going to next generation by the process of estimation of distribution and sampling. Hence, the number of DU bundles may fall outside the pre-decided interval. To keep the total number of DU bundles within the pre-decided interval, random correction method is applied. The probability of random correction is small since a very large interval is considered in the simulation. The excess bundles (of NU or DU) are randomly chosen and converted to other type.

## 3. Results

In all, four types of DU loadings (cases A-D) described in Section 2 were separately optimized using the EDA algorithm. The properties of optimum DU configuration obtained in each of the four cases are shown in Table 1.

It is seen that the configurations corresponding to cases A-C can give $100 \% \mathrm{FP}$ with sufficient excess reactivity, while keeping bundle power, channel power and CPPF within limits. The worth of 28 rods of SDS\#1 is also adequate. In case D, the CPPF is somewhat higher than the prescribed limit and hence it is not accepted.

1. Initialize the population (Size=N) randomly.
2. Evaluate the fitness of each individual based on their $\mathrm{K}_{\text {eff }}$, maximum permissible reactor power, channel power, channel power peaking factor, bundle power and the worth in shutdown system as obtained by diffusion code DOLP using Eq.(1) in section 2.1.
3. Either continue for new generation calculations or terminate the execution.
4. Select $\mathrm{M}<\mathrm{N}$ candidates based on termination selection method (the best fit M individuals among total N individuals).
5. Calculate Probability Distribution Function (PDF) using selected M individuals. At any generation (t) the PDF has been estimated as given below for each location.

$$
P D F(t+1)=P D F(t) \cdot(1-\alpha)+\alpha \frac{1}{M} \sum_{m=1}^{M} X_{m}(t)
$$

Where $\alpha$ is constant between $[0,1] . \mathrm{X}$ is binary matrix representation of loading pattern.
6. Generate new population (Size=N) using this new probability distribution function (PDF).
7. A correction operator is applied. The fuel type which is more in number than the specified value is randomly changed into other type.
8. The fitness of new N individuals is found out as in step 2 .
9. Go to step 3 .

Fig. 2. Pseudo EDA model used for optimization.

Table 1
The 700 MWe core properties for different type of loading.
Table 1 gives maximum power and safety parameters in the fresh core. It is necessary that the power level and constraints are satisfactory at later times also. To further study suitability of DU loadings, time dependent burnup simulation was carried out for all the four cases up to the pre-fuelling period. A time-step of 2.5 FPD (full power days) was used. The change in excess reactivity with FPD is shown in Fig. 3 for all the four cases. It is seen that excess reactivity becomes zero after about 116 FPD, which marks beginning of refuelling. The variation of CPPF with time is shown in Fig. 4 for all the four cases. The CPPF varies in narrow range for case A (DU at 7th location). The ROP detectors are calibrated with CPPF regularly. Case A permits more operating margin (lower CPPF) before the ROP trip as well as better safety (less variation in CPPF). Hence, the DU configuration in case A are considered as a better choice.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Variation in excess reactivity.
![img-2.jpeg](img-2.jpeg)

Fig. 4. Variation in channel power peaking factor.

The configuration in case A needs some further changes. There are 28 shut-off rods (SRs) in SDS\#1. The DU bundle at 7th location gives sufficient reactivity worth in SDS\#1 (28 SRs). In case, two rods with maximum worth fail to drop in the core during shutdown, the realized reactivity worth of SDS\#1 (26 SRs) is found to be less than 50 mk . In order to increase the worth of 26 SRs , some additional DU bundles are placed at 11th and 12th bundle locations in few channels. These channels are selected manually. DU bundles are kept at 7th location in the four fuel channels (F10, F11, F12 and F13) to reduce the non-uniformity in zone powers due to zone control compartments (ZCCs). The final loading pattern is shown in Fig. 5.

## 4. Conclusion and discussion

Earlier, optimum distributions of Thorium as well as DU bundles were successfully obtained by the EDA algorithm for

![img-3.jpeg](img-3.jpeg)

Fig. 5. The loading pattern with 248 DU bundles.

220 MWe Indian PHWRs. Here, the same algorithm is used to find optimum DU loading in the forthcoming large sized 700 MWe PHWR. The core lay-out, control devices and safety parameters of 700 MWe PHWR differ widely from those of 220 MWe. In 700 MWe, the effect of DU loading had to be checked only for one shut-down system namely SDS\#1 because the other system has very large worth. The core for 700 MWe has more symmetry properties than 220 MWe which helped in reducing problem size. The ROP system is a new feature, present only in the 700 MWe PHWR.

A requirement imposed in the present study was that the DU bundles should lie only at certain axial location to make loading operation easy. In all four types of DU loadings (cases A-D) were studied. The optimum fresh core configuration was obtained in each of the four cases. It was found that three cases satisfy all the safety constraints and give $100 \%$ FP. Later on, burn-up of the optimum configurations was simulated for about 115 FPD during
which no refuelling is needed. On the basis of behavior of maximum CPPF in this period, case A are found to be much better than other cases. Subsequently, on the basis of better operating margin and safety for ROP system, optimum configuration of DU in case A is found to be most suitable. Finally, to satisfy the stuck rod criterion, additional DU bundles were loaded at axial ends. It may be mentioned that the stuck rod criterion cannot be introduced in the form of penalty function because the maximum worth rods can vary with the various DU configurations tried by the EDA algorithm.
