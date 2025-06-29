# Optimization of depleted uranium bundle loading in fresh core of Indian PHWR by evolutionary algorithm 

Surendra Mishra ${ }^{\text {a, }}$, R.S. Modak ${ }^{\text {b }}$, S. Ganesan ${ }^{\text {c }}$<br>${ }^{a}$ Safety directorate, Nuclear Power Corporation of India Limited, Mumbai 400 094, India<br>${ }^{\mathrm{b}}$ Theoretical Physics Division, Bhabha Atomic Research Centre, Mumbai 400 085, India<br>${ }^{c}$ Reactor Physics Design Division, Bhabha Atomic Research Centre, Mumbai 400 085, India

## A R T I C L E I N F O

Article history:
Received 14 May 2009
Received in revised form 23 October 2009
Accepted 1 November 2009
Available online 28 November 2009

## A B S T R A C T

This paper is concerned with the Indian design of a 220 MWe pressurized heavy water reactor (PHWR) having natural uranium (NU) fuel and heavy water as moderator and coolant. At the beginning of life, it is necessary to flatten the power by loading some depleted uranium (DU) bundles to achieve a nearly full power operation. The determination of best possible locations of DU bundles, which maximize fuel economy as well as safety, is a large-sized combinatorial optimization problem with constraints. In the past, 384 DU bundles have been loaded in locations determined by manual intuition in an Indian PHWR and maximum permissible power of $93 \%$ full power (FP) was obtained. In the present paper, a modern evolutionary algorithm called estimation of distribution algorithm (EDA) is used to improve upon this distribution. Optimum distributions of DU bundles which maximize $K_{\text {eff }}$ and give $100 \% \mathrm{FP}$ without violating safety parameters such as maximum permissible bundle power, channel power, channel outlet temperature and permitted reactivity worths of shut-down systems are obtained. Another aspect studied in this paper is to find out how far one can increase the number of DU bundles loaded in the core. This will minimize the NU bundles requirement, extract more power from DU bundles and thus provide better fuel utilization. The idea is to conserve NU bundles. The optimum distribution of DU bundles has been obtained for the total number of DU bundles ranging from a few hundreds to a few thousands. It is found that, depending on various conditions, about $60-80 \%$ of the core can be loaded with DU bundles leading to a substantial saving in NU bundles. Some variation in the implementation of EDA to generate loading pattern of PHWR reactor core is also studied.
(c) 2009 Elsevier Ltd. All rights reserved.

## 1. Introduction

The pressurized heavy water reactor (PHWR) designs originated in Canada belong to two categories: small sized PHWR ( 220 MWe ) with moderator dump as a shutdown system and large sized PHWR ( 540 MWe and above) having shutoff rods and liquid poison addition for shutdown. There is an Indian PHWR design ( 220 MWe ) which is small in size and yet does not have moderator dump system. It uses two independent shut-down systems: 14 mechanical shutoff rods known as primary shutdown system (PSS) and 12 liquid poison tubes known as secondary shutdown system (SSS). There are nine such power plants in operation and three more plants are awaited (Bajaj and Gore, 2006). The present studies are concerned with an optimization problem of loading of depleted uranium (DU) bundles for power flattening in the initial core of this type of reactors.

[^0]The PHWR is a horizontal tube type reactor fuelled with natural uranium (NU) with heavy water as both coolant and moderator. The coolant is physically separated from the moderator by being contained inside the pressure tube where it is maintained at high temperature $\left(\sim 271^{\circ} \mathrm{C}\right)$ and pressure. The moderator heavy water is at a relatively low temperature $\left(\sim 54.4^{\circ} \mathrm{C}\right)$ and is un-pressurized. The reactor core consists of 306 pressure tubes arranged along a square lattice of 22.86 cm pitch. The fuel pins and the coolant are contained within these pressure tubes. The direction of coolant flow in adjacent channels is opposite. The direction of the bundle movement (fuelling direction) is the same as that of the coolant flow, so that alternate channels are fuelled in opposite directions. The fuel is in the form of a string of 12 bundles, each bundle is a 19 -rod cluster of 49.5 cm length. Of the 12 bundles, 10 are in the active portion of the core, the remaining two; one bundle on each side, is outside the core. For the purpose of reactor regulation there are four adjuster rods, two regulating rods and two shim rods. As mentioned above, there are two independent shut-down systems called PSS and SSS. More detailed description can be found in reference (Balakrishnan and Kakodkar, 1994).


[^0]:    * Corresponding author. Tel.: +91 222599 4678; fax: +91 222599 3318.

    E-mail addresses: smishra@npcil.co.in (S. Mishra), rsmodak@barc.gov.in (R.S. Modak), ganesan@barc.gov.in (S. Ganesan).

### 1.1. Nature of the problem

Since NU bundles are used as fuel, there is little excess reactivity in the hot equilibrium core. Hence, to operate the PHWR reactor on continuous basis, fuelling is done on-power by simply pushing eight fresh NU bundles in a selected channel almost everyday. The fuelling direction is opposite in adjacent channels. It helps in axial flux flattening. For the radial flux flattening, the core is treated as consisting of two radial zones for the purpose of fuelling: inner and outer. The fuel discharge burnup of inner region is higher than that of the outer region or in other words, fuelling is less frequent in inner zone channels than outer zone channels. This helps in radial power/flux flattening so that more power can be extracted from the core than if the burnup had been uniform throughout. This is true for an equilibrium core. However, at the beginning of the core life, when the entire core is loaded with fresh NU fuel, the power distribution would be highly peaked in the centre due to lack of flux flattening. Hence, it will not be possible to get the full rated power from the core right from beginning unless some other way of achieving power flattening is followed. It is possible to flatten the power distribution by loading some thorium or DU bundles in the central region of the core. While choosing the locations of thorium or DU bundles, the following considerations are taken into account:
(1) $K_{\text {eff }}$ is maximum possible so that reactor can operate without fuelling for longer time leading to better fuel economy.
(2) The operating limit on channel outlet temperature $\left(299^{\circ} \mathrm{C}\right)$ is obeyed.
(3) Maximum bundle power is less than 440 kW .
(4) The reactivity worth of each shutdown device is not less than 30 mK .

The problem of obtaining an optimum distribution of thorium bundles which satisfies above criteria was solved successfully about two decades ago (Balakrishnan and Kakodkar, 1994) and a suitable distribution consisting of 35 thorium bundles was arrived at. The same problem was revisited recently by Mishra et al. (2009) using two stochastic techniques, i.e. genetic algorithm (GA) and estimation of distribution algorithm (EDA).

In the present paper, we try to find optimum distribution of DU bundles in stead of thorium. It is interesting to have a look at the differences between thorium and DU loading. Thorium has relatively large neutron capture cross-section than DU. While a few tens of thorium bundles are enough for flux flattening, a few hundreds of DU bundles are needed for the same purpose. As a result, the search space (number of possible arrangements) will be larger in the DU case. However, there is one simplification in the DU case. The neutron flux gets sharply depressed around the thorium bundle location due to higher absorption. This affects the worth of PSS and SSS shut-down systems adversely. This problem is generally insignificant in DU loading. Another point to be noted is that in contrast with thorium bundles, DU bundles are fissionable. Hence, there exists a possibility of loading a very large number of DU bundles (a few thousands) in the core. This will minimize the NU bundles requirement, extract more power from DU bundles and thus provide higher fuel utilization. In case of thorium, it may not be possible to load more than about hundred bundles since $K_{\text {eff }}$ would fall below unity.

The problem of choosing a few hundred DU bundle locations in the fresh core of PHWR in order to obtain nearly full power has been addressed earlier by manual trial. The central 32 channels were loaded with DU bundles (total 384 bundles) as shown in Fig. 1. The figure shows the vertical (XY) cross-section of the reactor in which each small square is a coolant channel. The notation used in this figure is as follows. An arabic numeral (say $x$ ) is printed
in each channel. The table just below the core map shows axial distribution of fuel bundles (NU/DU) for each value of $x$. Table 1 lists the properties of configuration in Fig. 1. It can be seen that this configuration is satisfactory with respect to the four aspects listed above. It gives $93 \%$ FP without reducing the worth of PSS and SSS. The excess reactivity is about 21 mK . This configuration was actually loaded in an Indian PHWR. It may be mentioned that if all NU is loaded in fresh core, only about $70 \%$ FP can be obtained.

In the present paper, the optimum distribution of DU bundles is obtained by using a modern evolutionary algorithm called estimation of distribution algorithm (EDA). The EDA was successfully used in our earlier work on thorium (Mishra et al., 2009). There are several aims of the present study:
(1) The first aim is to see whether the specific configuration in Fig. 1 obtained manually can be improved upon. The idea is to check whether we can get better $K_{\text {eff }}$ and higher power level (or better flattening) than for Fig. 1 with a similar number (few hundreds) of DU bundle loading.
(2) The second aim is to find out whether the number of DU bundles loaded in the core can be further increased. As mentioned earlier, this will minimize the NU bundles requirement, extract more power from DU bundles and thus provide better fuel utilization. In general, as number of loaded DU bundles is increased, the maximum possible $K_{\text {eff }}$ is expected to reduce. It is necessary to find best possible arrangements of DU bundles which flatten the flux sufficiently to get $100 \%$ FP and also maximize the $K_{\text {eff }}$ as far as possible.
(3) A hypothetical case is also analyzed in which additional measures are taken to maximize the fuel utilization. We relax the requirement of $100 \%$ FP to above $50 \%$ FP. In this case, one can afford to have a power distribution peaked at the centre since the bundle power limits are not easily violated because of lower total power. This gives higher $K_{\text {eff }}$. It may be mentioned that the adjuster rods (AR) are usually parked inside the core for the purpose of xenon override in the so-called "nominal configuration". The cases (1) and (2) listed above adhere to the nominal configuration. In the present case, as an effort to maximize fuel utilization, the adjuster rods are kept out of the core. This further increases the $K_{\text {eff }}$ and hence the fuel utilization. Under the two conditions namely more than $50 \%$ power and AR out, one has to find out the best possible arrangement of DU bundles and check how far the number of DU bundles can be increased.

### 1.2. Plan of the paper

Our paper is organized as follows. In Section 2, combinatorial complexity of the problem is highlighted. Section 3 covers the details of overall methodology followed in present studies. Section 4 describes the parallelization of the problem. Section 5 presents results obtained by present approach. Section 6 gives conclusion and discussion.

## 2. Combinatorial complexity

There are total 306 fuel channels (from A-T in Y-direction and 1-20 in X-direction) as shown in Fig. 1. These channels are horizontal and extend in Z-direction up to about 500 cm . There is no top-bottom symmetry in the core. There is however, left-right symmetry. Thus there is reflective symmetry along $X$-direction. In addition, there is reflective symmetry along Z-direction also. In some of the studies presented here, reflective symmetry along both

![img-0.jpeg](img-0.jpeg)

Fig. 1. Loading pattern containing 384 DU bundles by manual intuition.

Table 1
Properties of configuration (for Fig. 1) obtained by manual intuition.

| Case | $\#$ DU <br> bundles | $K_{\text {eff }}$ | $\%$ FP | CP | BP | COT | PSS | SSS |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Manual | 384 | 1.0207 | 93.0 | 3.02 | 442.4 | 293.8 | 30.9 | 31.7 |

X- and Z-directions are exploited. In that case, one has to choose locations of DU bundles in only one-fourth core which contains 153 channels and six bundle locations in half channel length. Thus there are $153 \times 6=918$ fixed locations. Some of these locations have to be loaded with DU bundles. The symmetry in Z-direction implies that there must be only even number of DU bundles in any channel containing DU. It was felt that this will restrict the distribution of DU bundles in radial plane. Hence, in addition to the one-fourth core, optimization of DU bundles was done which respects only symmetry in $X$-direction or half-core symmetry. In half-core, there are $1836(153 \times 12)$ bundle locations. As will be seen later, results of comparable merits were obtained in half-core and quarter-core symmetry cases.

It is possible to estimate the number of ways in which a given number of DU bundles can be arranged in the reactor. As an example, suppose one has to load 500 DU bundles in the full core. This amounts to choosing 250 bundle locations in half core if the DU loading respects only $X$-symmetry or 125 bundle locations in quarter core in case of $X-Z$-symmetry. The number of possible configurations is ${ }^{1836} \mathrm{C}_{250}$ or ${ }^{918} \mathrm{C}_{125}$. The latter number is smaller and is of the order of $10^{158}$. In order to assess the merit of any configuration, it is necessary to make a $K$-eigenvalue calculation for that configuration. In our case we use two energy groups (thermal and fast) and three-dimensional $X-Y-Z$ geometry and diffusion theory based core calculations. From the $K$-eigenvalue and power distribution, one can check whether the desired conditions are fulfilled. Additional calculations are needed per configuration to compute the worth of PSS and SSS.

Thus, a brute force approach will involve $10^{158}$ core calculations, one for each configuration, for choosing the best one. This is obviously impossible and some techniques are needed so that desired optimum is obtained with much smaller number of calculations. Such techniques are discussed in the next section.

## 3. Methodology

### 3.1. Optimization techniques

There exist gradient based methods (Carter, 1997) in which one starts with a guess distribution and make small changes to look for improvements. This generally requires a good degree of intuition and experience. Since small changes are made around a certain configuration, there is a possibility of getting trapped in a local minimum (Salomon, 1998). There exists another technique called "simulated annealing" (Kropaczek and Turinsky, 1991) in which the same gradient method is used, but one occasionally accepts an inferior solution with certain probability. This probability is slowly reduced as the optimum solution is approached. This helps in getting out of local minima and reaching to a global optimum.

There are yet other techniques based on genetic algorithms (GA). They are based on a philosophy which is completely different from the gradient methods. One starts with many different candidate configurations instead of just one in the gradient method. Fitness of these configurations is evaluated. Parents are selected from these configurations. Candidates with better fitness have higher chance of getting selected. Then, children are formed by crossover between two parents. The process is continued for several generations till convergence. Occasionally, a mutation is performed which involves a small random change in the configuration. This algorithm mimics the process of natural evolution of biological species and more details can be found in Goldberg (1989), Carter (1997) and Pereira et al. (1999). Unlike gradient based methods, the GA does not require a reasonable guess to start with. It does not usually get trapped in local minima and explores the full solution space leading to near global optimum.

There exists slightly different algorithm called estimation of distribution algorithm (EDA). In EDA (Jiang et al., 2006; Mishra et al., 2009), the combination process in GA is replaced by estimation of distribution and sampling as per this distribution to generate new candidate solutions. The simulated annealing, GA and EDA have been extensively used to solve light water reactor fuel management and control design problems (Pereira and Sacco, 2008; Montes et al., 2004; Jiang et al., 2006; Turinsky et al., 2005).

In the present paper, we have applied EDA technique to optimize the initial fuelling in PHWR. The implementation of the EDA algorithm needs several thousands of neutronics computations. This is possible thanks to the high speed processors and parallel computing facilities available today.

### 3.2. The neutron diffusion code

As mentioned in Section 2, a 3-D 2-group neutron diffusion code is needed to evaluate the fitness of any given configuration. An in-house computer code 'DOLP' has been developed as part of the present study and used for 3-D 2-group neutron diffusion calculations. It solves neutron diffusion equation by finite difference approximation. The code has been validated against AECL PHWR benchmark (Judd and Rouben, 1981). The homogenized two energy group cross-sections for NU ( $0.7115 \mathrm{wt} . \% \mathrm{U}^{235}$ ) as well as DU ( $0.6 \mathrm{wt} . \% \mathrm{U}^{235}$ ) bundles, required for diffusion calculations, were obtained by two separate lattice calculations. For this purpose, the 2-D integral transport theory code CLUB (Krishnani, 1992) was used. In these calculations, 69 energy group WIMSD library derived from ENDF/B-VI. 8 basic evaluated nuclear data file was used. The details of the WIMSD library are available in the website: http://www-nds.indcentre.org.in/wimsd/downloads2.htm.

### 3.3. The Optimization problem

The optimization problem is defined as follows:
Objective: To maximize the effective multiplication factor $\left(K_{\text {eff }}\right)$.
Constraints: Following constraints are imposed.

- Total numbers of DU bundles are restricted within a predetermined interval. The number of DU bundles lies within $N_{\mathrm{d}} \pm 250$.
- The reactor power should be equal to or greater than the specified power level.
- The maximum channel power (MCP) should be less than 3.08 MW.
- The maximum bundle power (MBP) should not cross the operating limit 440 kW .
- The maximum channel outlet temperature (MCOT) should not be more than $299^{\circ} \mathrm{C}$.
- The reactivity worth of two independent shut-down systems, i.e. PSS and SSS should not be less than 30 mK .

We use the "penalty method" for handling constraints. The penalty method penalizes infeasible (or unfavorable) individuals. In general, it transforms a constrained optimization problem to an unconstrained problem by defining penalty function (Michalewicz, 1999). Here, the objective function to be maximized has been defined to take care of constraints as follows:
Fit $=K_{\text {eff }}-F 1-F 2-F 3-F 4-F 5-F 6$
where
$F 1=($ FP0-FP $) *$ Afp if FP $<$ FP0 and zero otherwise.
$F 2=($ CP-CP0 $) *$ Acp if $\mathrm{CP}>\mathrm{CP} 0$ and zero otherwise.
$F 3=($ COT-COT0 $) *$ Acot if COT $>$ COT0 and zero otherwise.
$F 4=($ BP-BP0 $) *$ Abp if $\mathrm{BP}>\mathrm{BP} 0$ and zero otherwise.
$F 5=($ PSS0-PSS $) *$ Apss if PSS < PSS0 and zero otherwise.
$F 6=($ SSS0-SSS $) *$ Asss if SSS < SSS0 and zero otherwise.
The notation used is as follows:
FP0 $=100$ or 50 , corresponding to specified power level.

FP is the maximum allowable power in a given configuration. $\mathrm{CP} 0=3.08$, corresponding to maximum permitted channel power.
CP is the maximum channel power in a given configuration.
COT0 $=299$, corresponding to maximum permitted channel outlet temperature.
COT is the maximum channel outlet temperature in a given configuration.
$\mathrm{BP} 0=440$, corresponding to maximum permitted bundle power.
BP is the maximum bundle power in a given configuration.
PSS0 $=32$, a slightly higher value than minimum worth of PSS in mK .
PSS is the worth of PSS in a given configuration.
SSS0 $=32$, a slightly higher value than minimum worth of SSS in mK .
SSS is the worth of SSS in a given configuration.
Afp, Acp, Acot, Abp, Apss and Asss are suitably chosen constants to give a weightage to each of the factors. The procedure to decide these constants is somewhat arbitrary and is based on experience. It is similar to the one used in the earlier work (Mishra et al., 2009). For some random population, $K$-eigenvalue and flux distribution were obtained. The fluxes were normalized to get either $\mathrm{FP}=100$ or $\mathrm{CP}=3.08$, whichever gives smaller flux. From these results, the extent of deviation of parameters FP, COT, etc. from the limiting values FP0, COT0, etc. is estimated. The constants Afp, Acot, etc. are chosen such that corresponding penalty term in Eq. (1) for such a deviation is of the order of unity.

The objective function (also called fitness function) given by Eq. (1) has to be evaluated to determine the fitness of any given configuration. It can be seen from Eq. (1) that if maximum achievable power is closer to specified power level, Fitness increases. If the worth of shutdown system is less than 32 mK , fitness will be lesser. Similarly, other terms in Eq. (1) can be understood.

### 3.4. Use of estimation of distribution algorithm

EDAs belong to the class of population based optimization algorithms. The two operators in EDA are estimation of distribution and sampling. In each generation, $N$ individuals are generated by sampling probability distribution. The fitness is evaluated for each of them by diffusion calculations and the best $M(<N)$ individuals are selected to estimate probability distribution. The probability that a given location is occupied by NU or DU bundle is estimated from the selected $M$ individuals. The performance of an EDA highly depends on how well it estimates and samples the probability distribution. Univariate marginal distribution algorithm (UMDA) assumes no interaction among variables. The probability distribution is estimated using UMDA (Jiang et al., 2006) in the present case. A pseudo-model of the algorithm used for optimization is given in Fig. 2. The probability distribution function (PDF) was generated using $30 \%$ dominated individuals (item 4 in Fig. 2) of the population size. Alpha is chosen 0.05 .

The reactor model (Fig. 1) has reflective symmetry along $X$-and $Z$ direction. $Z$ direction is the direction of coolant flow as well as direction of fuelling. The calculations presented in this paper are of two types:
(1) X-symmetry: Model based on exploitation of $X$-symmetry alone, in which one chooses DU bundle locations only in half-core. The locations in other half are decided by symmetry.
(2) $X-Z$-symmetry: Model based on both $X$ - and $Z$-symmetry in which one has to choose DU bundle locations only in quarter core; other locations being decided by symmetry.

1. Initialize the population (Size=N) randomly.
2. Evaluate the fitness of each individual based on their $\mathrm{K}_{\text {eff }}$, maximum permissible reactor power, channel power, channel outlet temperature, bundle power and the worths of PSS and SSS as obtained by diffusion code DOLP using Eq.(1) in section 3.3.
3. Either continue for new generation calculations or terminate the execution.
4. Select $\mathrm{M}=\mathrm{N}$ candidates based on termination selection method (the best fit M individuals among total N individuals).
5. Calculate Probability Distribution Function (PDF) using selected M individuals. At any generation (t) the PDF has been estimated as given below for each location.
$P D F(t+1)=P D F(t) \cdot(1-\alpha)+\alpha \cdot \frac{1}{M} \sum_{m=1}^{M} X_{m}(t)$
Where $\alpha$ is constant between $[0,1] . \mathrm{X}$ is binary matrix representation of loading pattern.
6. Generate new population (Size=N) using this new probability distribution function (PDF).
7. The newly generated individuals may not have desired number of NU or DU bundles. Hence a correction operator is applied. The fuel type which is more in number than the specified value is randomly changed into other type.
8. The fitness of new N individuals is found out as in step 2 .
9. Go to step 3 .

Fig. 2. Pseudo EDA model used for optimization.
The search space is obviously smaller in the $X-Z$-symmetry case and hence convergence would be faster. Use of $Z$-symmetry implies that one has to put only even number of DU bundles in each coolant channel. It was felt that this may reduce flexibility in distributing the available DU bundles in different coolant channels. Hence, the case with $X$-symmetry alone was also analyzed. However, as will be seen later, configurations of similar merit are obtained in the two cases.

It may be mentioned that while using $X$-symmetry alone, we choose a pair of channels in which DU bundles is to be loaded consistent with this symmetry. However, the coolant flow as well as fuelling direction is opposite to each other in this pair of channels. Hence the location of DU bundle in this pair of channels is chosen to be anti-symmetric in $Z$-direction.

A systematic study to obtain optimum distribution of DU bundles has been carried out for number of DU bundles ranging from a few hundreds up to a few thousands. For implementing this, two approaches were followed.

### 3.4.1. Random correction approach

We try to optimize the loading pattern with the number of DU bundles lying within a certain pre-decided range or interval.

Let the interval be denoted by $\left(N_{\mathrm{d}}-250, N_{\mathrm{d}}+250\right)$. The values of $N_{\mathrm{d}}$ considered are: $250,750,1250,1750,2250,2750$ and 3250 . The optimization study is carried out for all these ranges or intervals. In EDA, the total number of DU or NU bundles does not remain constant while going to next generation by the process of estimation of distribution and sampling (Fig. 2). Hence, the number of DU bundles may fall outside the pre-decided interval. To keep the total number of DU bundles within the pre-decided interval, random correction method is applied. The excess bundles (of NU or DU) are randomly chosen and converted to other type. As a result, certain members of population are prevented from participating in the evolution and one may get sub-optimal results. This possibility is absent in the next approach.

### 3.4.2. Additional penalty approach

The total number of DU bundles is kept close to a certain predecided number by using additional penalty. An additional penalty term F7 is subtracted from RHS of Eq. (1). The F7 term is defined as follows:
$F 7=\operatorname{abs}\left(N_{\mathrm{d}}-N_{\mathrm{a}}\right) * A_{\mathrm{DU}}$
where $N_{\mathrm{d}}$ is pre-decided number of DU bundles, $N_{\mathrm{a}}$ is the actual number of DU bundles in the individual under consideration in EDA and $A_{\text {DU }}$ is an appropriately chosen positive constant. 'abs' stands for absolute value. The values of $N_{\mathrm{d}}$ considered are: 250 , $750,1250,1750,2250,2750$ and 3250 .

## 4. Parallelization

The most time consuming part in execution of EDA is the evaluation of fitness of $N(=1000)$ individuals in each generation as given by Eq. (1). For each individual, this requires three $K$-eigenvalue calculations, one for evaluation of $K_{\text {eff }}$, maximum bundle power, channel outlet temperature, etc. and two more to evaluate worth of PSS and SSS. These calculations are completely independent and hence quite suitable for parallel computing. The remaining work in EDA algorithm is to estimate probability distribution from which new individuals are to be made. This work needs earlier individuals simultaneously and is not suitable for parallelization. Hence, this work can be done by one of the processor; namely the rank 0 processor, usually referred to as master. The master

Table 2
Properties of configurations obtained by EDA (only $X$-symmetry, AR IN).

| Case | \#DU bundles | $K_{\text {eff }}$ | \% FP | CP | BP | COT | PSS | SSS |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $250 \pm 250$ | 438 | 1.0244 | 100 | 3.05 | 439.8 | 297.3 | 32.6 | 32.0 |
| $750 \pm 250$ | 554 | 1.0244 | 100 | 3.06 | 439.9 | 296.8 | 32.5 | 32.0 |
| $1250 \pm 250$ | 1082 | 1.0241 | 100 | 3.07 | 440.0 | 297.6 | 33.2 | 32.0 |
| $1750 \pm 250$ | 1500 | 1.0236 | 100 | 3.06 | 437.7 | 296.6 | 33.3 | 32.0 |
| $2250 \pm 250$ | 2000 | 1.0169 | 100 | 3.07 | 439.2 | 297.6 | 34.5 | 33.2 |
| $2750 \pm 250$ | 2502 | 1.0057 | 100 | 3.07 | 441.1 | 296.7 | 34.8 | 35.2 |
| $3250 \pm 250$ | 3000 | 0.9878 | 98.5 | 3.08 | 440.8 | 295.9 | 33.9 | 32.1 |

Table 3
Properties of configurations obtained by EDA ( $X-Z$-symmetry, AR IN).

| Case | \#DU bundles | $K_{\text {eff }}$ | \% FP | CP | BP | COT | PSS | SSS |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $250 \pm 250$ | 284 | 1.0246 | 100 | 3.08 | 426.8 | 297.2 | 33.5 | 30.7 |
| $250 \pm 250$ | 472 | 1.0236 | 100 | 3.07 | 439.5 | 297.4 | 32.6 | 32.0 |
| $750 \pm 250$ | 628 | 1.0239 | 100 | 3.06 | 439.6 | 297.5 | 32.6 | 32.0 |
| $1250 \pm 250$ | 1036 | 1.0241 | 100 | 3.07 | 440.0 | 297.2 | 33.2 | 32.0 |
| $1750 \pm 250$ | 1500 | 1.0236 | 100 | 3.08 | 440.0 | 297.2 | 33.4 | 32.1 |
| $2250 \pm 250$ | 2000 | 1.0164 | 100 | 3.08 | 439.4 | 297.1 | 34.1 | 33.0 |
| $2750 \pm 250$ | 2500 | 1.0056 | 100 | 3.07 | 440.4 | 297.0 | 34.3 | 35.6 |
| $3250 \pm 250$ | 3000 | 0.9876 | 98.8 | 3.08 | 440.2 | 297.5 | 33.2 | 32.0 |

Table 4
Properties of configurations obtained by EDA using additional penalty approach ( $X-Z$ symmetry, AR IN).

| Case | #DU bundles | $K_{\text {eff }}$ | %FP | CP | BP | COT | PSS | SSS |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 250 | 280 | 1.0247 | 97.7 | 3.08 | 440.1 | 297.1 | 32.0 | 32.0 |
| 750 | 748 | 1.0227 | 100 | 3.04 | 439.8 | 295.7 | 32.5 | 32.0 |
| 1250 | 1248 | 1.0222 | 100 | 3.04 | 439.1 | 297.5 | 32.9 | 32.0 |
| 1750 | 1748 | 1.0200 | 100 | 3.08 | 439.2 | 297.3 | 33.7 | 32.1 |
| 2250 | 2248 | 1.0107 | 100 | 3.06 | 440.2 | 296.8 | 34.2 | 34.0 |
| 2750 | 2748 | 0.9964 | 99.8 | 3.08 | 439.5 | 295.7 | 32.8 | 32.2 |
| 3250 | 2956 | 0.9887 | 100 | 3.06 | 439.7 | 297.6 | 33.0 | 32.1 |

sends the details of 1000 new individuals to other processors called slave processors. Using MPI, programs can be written which can define the role of rank 0 and other processors as described above. The parallelization was achieved using the MPI Library functions (Pacheco, 1997) as follows: the rank 0 processor is called here as MASTER processor and others are SLAVE processors. The MASTER will start with a population containing $N(=1000)$ individuals. If there are S SLAVE processors, each SLAVE is assigned the job of evaluating fitness of $(N / S)$ individuals by diffusion calculations.

The results are returned to the MASTER. The MASTER will generate new population and send $(N / S)$ individuals to each slave for fitness evaluation. This is continued for all the generations. The computer code DOLP has been written to execute this using standard message passing interface (MPI) library functions in FORTRAN. The supercomputer EKA built at Computational research laboratories (CRL) in Pune, India was used. The detailed information about EKA is available at website: http://www.crlindia.com.

## 5. Results

### 5.1. All adjusters IN and reactor power nearly $100 \%$ FP

### 5.1.1. Random correction approach

The reactor power should be nearly 100\% FP, hence FP0 in Eq. (1) is chosen 100. Optimized distributions of DU bundles were obtained by EDA using random correction approach described in Section 3.4. Both $X$-symmetry and $X-Z$-symmetry were considered. The results obtained using only $X$-symmetry (half core) are shown in Table 2. The results obtained using $X$ - and $Z$-symmetry (quarter core) are shown in Table 3. The observations are as follows:
![img-2.jpeg](img-2.jpeg)

Fig. 3. Fitness evolution with generation for random correction method (row 4 of Table 2 and row 5 of Table 3) and additional penalty method (row 3 of Table 4).
![img-2.jpeg](img-2.jpeg)

Fig. 4. $K_{\text {eff }}$ versus total DU bundles by various methods (Tables 2-4).

Table 5
Properties of configurations obtained by EDA (only $X$-symmetry, AR OUT).

| Case | \#DU bundles | $K_{\text {eff }}$ | \% FP | CP | BP | COT | PSS | SSS |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $250 \pm 250$ | 16 | 1.0451 | 79.1 | 3.08 | 440.0 | 294.3 | 33.7 | 34.6 |
| $750 \pm 250$ | 520 | 1.0451 | 79.1 | 3.08 | 440.0 | 294.3 | 33.7 | 34.6 |
| $1250 \pm 250$ | 1000 | 1.0446 | 78.4 | 3.08 | 439.7 | 294.3 | 33.9 | 35.1 |
| $1750 \pm 250$ | 1500 | 1.0424 | 78.3 | 3.08 | 439.8 | 294.3 | 34.4 | 37.2 |
| $2250 \pm 250$ | 2000 | 1.0383 | 70.8 | 3.08 | 439.5 | 294.3 | 35.4 | 39.0 |
| $2750 \pm 250$ | 2500 | 1.0314 | 62.7 | 3.08 | 439.8 | 294.4 | 36.4 | 39.7 |
| $3250 \pm 250$ | 3000 | 1.0194 | 53.5 | 3.08 | 439.1 | 294.3 | 37.8 | 39.6 |

Table 6
Properties of configurations obtained by EDA ( $X-Z$-symmetry, AR OUT).

| Case | \#DU bundles | $K_{\text {eff }}$ | \% FP | CP | BP | COT | PSS | SSS |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $250 \pm 250$ | 16 | 1.0450 | 79.0 | 3.08 | 438.4 | 294.2 | 34.2 | 35.3 |
| $750 \pm 250$ | 520 | 1.0449 | 79.1 | 3.08 | 439.2 | 294.3 | 34.3 | 35.2 |
| $1250 \pm 250$ | 1000 | 1.0447 | 78.5 | 3.08 | 439.0 | 294.3 | 34.4 | 36.1 |
| $1750 \pm 250$ | 1500 | 1.0426 | 76.0 | 3.08 | 439.6 | 294.3 | 35.0 | 38.1 |
| $2250 \pm 250$ | 2000 | 1.0383 | 69.6 | 3.08 | 437.9 | 294.1 | 36.1 | 39.5 |
| $2750 \pm 250$ | 2500 | 1.0314 | 61.3 | 3.08 | 438.8 | 294.3 | 37.5 | 39.1 |
| $3250 \pm 250$ | 3000 | 1.0194 | 52.0 | 3.08 | 433.6 | 293.8 | 39.1 | 39.2 |

(1) Table 1 presents the properties of optimum configuration (Fig. 1) obtained manually and loaded in one of the Indian PHWRs. This may be compared with the first configuration given in first row of Table 2 and also with the first two rows of Table 3. The said configurations in Tables 2 and 3 (obtained using EDA) have higher $K_{\text {eff }}$ as well as higher permissible power than the manually obtained configuration in Table 1. The number of DU bundles is similar in all these cases. Thus EDA has provided several configurations with features better than manually obtained configuration.
(2) As seen from Tables 2 and 3, up to about 2500 DU bundles can be loaded in the core and full power can be obtained though with a small excess reactivity of about 5 mK .

### 5.1.2. Additional penalty approach

This approach was used with $X-Z$-symmetry. Properties of optimum configurations obtained by EDA for different numbers of DU bundles are listed in Table 4.

### 5.1.3. Overall results

Some sample curves showing change of fitness with generation number are shown in Fig. 3. The fitness or objective function given by Eq. (1) increases rapidly up to 200-300 generations and then gradually approaches optimum value. The $X-Z$-symmetric case with random correction approach converges faster than $X$-symmetric case with same approach as expected.

In general, as the number of DU bundles increases, the maximum possible $K_{\text {eff }}$ will reduce (Tables 2-4). The EDA tries to max-
![img-3.jpeg](img-3.jpeg)

Fig. 5. Loading pattern of 284 DU bundles (row 1 of Table 3).

![img-4.jpeg](img-4.jpeg)

Fig. 6. Loading pattern of 1500 DU bundles (row 5 of Table 3).

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| A |  |  |  |  |  |  |  | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |  |  |
| B |  |  |  |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
| C |  |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |
| D |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |
| E |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |
| F |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 11 | 11 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 |  |
| G |  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 5 | 6 | 6 | 5 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |  |
| H | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 5 | 6 | 6 | 5 | 2 | 2 | 1 | 1 | 1 | 1 | 1 |  |
| J | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 5 | 6 | 6 | 5 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |  |
| K | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | 6 | 9 | 9 | 6 | 5 | 5 | 8 | 3 | 1 | 1 | 1 | 1 |
| L | 1 | 1 | 1 | 1 | 3 | 3 | 2 | 5 | 5 | 6 | 6 | 5 | 5 | 2 | 3 | 3 | 1 | 1 | 1 | 1 |
| M | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 | 6 | 6 | 6 | 6 | 5 | 7 | 1 | 1 | 1 | 1 | 1 | 1 |
| N |  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 5 | 6 | 6 | 5 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |  |
| 0 |  | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 3 | 4 | 4 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |  |
| P |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 3 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |
| Q |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |
| R |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |
| S |  |  |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |
| T |  |  |  |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
| 1 |  | DU |  |  | N | N | N | N | N | N | N | N | N | N | N | DU | DU | DU |  |  |
| 2 |  | DU |  |  | N | N | N | N | N | N | N | N | N | N | DU | DU | DU |  |  |  |
| 3 |  | DU |  | N | N | N | N | DU | DU | N | N | N | N | N | DU | DU |  |  |  |  |
| 4 |  | DU |  | N | N | N | DU | DU | DU | DU | N | N | N | N | DU | DU | DU |  |  |  |
| 5 |  | DU |  | DU | N | N | N | DU | DU | N | N | N | N | DU | DU | DU |  |  |  |  |
| 6 |  | DU |  | DU | N | DU | DU | DU | DU | N | DU | N | DU | DU | DU | DU |  |  |  |  |
| 7 |  | DU |  | N | DU | N | N | N | N | N | N | N | N | N | DU | N | DU |  |  |  |
| 8 |  | DU |  | N | N | DU | N | N | DU | N | N | DU | N | N | DU | DU | DU |  |  |  |
| 9 |  | DU |  | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU |  |  |  |
| 10 |  | DU |  | DU | DU | DU | N | DU | DU | N | DU | DU | DU | DU | DU | DU | DU | DU |  |  |  |
| 11 |  | DU |  | N | N | DU | DU | DU | DU | DU | N | N | DU | DU | DU | DU | DU |  |  |  |  |
| 11 |  | DU |  | N | N | DU | DU | DU | DU | DU | N | N | DU | DU | DU |  |  |  |  |  |

Fig. 6. Loading pattern of 1500 DU bundles (row 5 of Table 3).

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| A |  |  |  |  |  |  | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |  |  |  |
| B |  |  |  |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
| C |  |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |
| D |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |
| E |  |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |
| F |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |
| G |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
| H | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
| J | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 | 6 | 4 | 3 | 1 | 1 | 1 |
| K | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
| L | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
| M | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
| N |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
|  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
|  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |  |  |  |  |
|  | 1 |  | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU | DU |  |  |  |  |
|  | 2 |  | DU | DU | DU | DU | DU | N | N | DU | DU | DU | DU | DU | DU | DU |  |  |  |  |  |
|  | 3 |  | DU | DU | DU | DU | N | N | N | N | N | N | DU | DU | DU | DU |  |  |  |  |  |
|  | 4 |  | DU | DU | DU | N | N | N | N | N | N | N | N | DU | DU | DU |  |  |  |  |  |
|  | 5 |  | DU | DU | DU | DU | N | DU | DU | N | DU | DU | DU | DU | DU | DU |  |  |  |  |  |
|  | 6 |  | DU | DU | N | N | N | N | N | N | N | N | N | N | N | DU | DU |  |  |  |  |
|  | 7 |  | DU | DU | N | N | N | DU | DU | N | N | N | N | DU | DU |  |  |  |  |  |  |
|  | 8 |  | DU | N | N | N | N | N | N | N | N | N | N | N | N | N | DU |  |  |  |

Fig. 7. Loading pattern of 3000 DU bundles (row 7 of Table 6).
imize the $K_{\text {eff }}$ as far as possible by optimizing the distribution of DU bundles. In Fig. 4, the $K_{\text {eff }}$ is plotted against total number of DU
bundles present in the core for Tables 2-4. It is seen that the results given in Table 2-4 have similar trend.

It is clear from Fig. 4 that the number of DU bundles cannot exceed 2500 because $K_{\text {eff }}$ falls below 1.0 and reactor cannot be operated. In next section, the possibility of further increasing the number of DU bundles is considered.

### 5.2. All adjusters OUT and reactor power greater than $50 \%$ FP

In Section 5.1, the aim was to achieve 100\% FP. In this section, the reactor power is desired to be greater than $50 \%$ FP. Hence the FP0 in Eq. (1) is set equal to 50 and the corresponding penalty is added only if FP is less than 50 . The removal of adjuster rods out of the reactor core gives additional positive reactivity, which helps in increasing the number of DU bundles in the configuration. The random correction approach is used. The optimization is carried out for $X$-symmetry as well as $X-Z$-symmetry of the core. The properties of optimum configurations obtained by EDA are shown in Tables 5 and 6 for half and quarter-core symmetry respectively. It is seen that half core and quarter-core results are of comparable quality.

An interesting result (Tables 5 and 6) is that one can load as many as 3000 DU bundles and operate the reactor. Thus only 672 NU bundles are required to operate the reactor with about $52 \%$ FP and 19 mK excess reactivity. This would lead to substantial conservation of NU bundles. It may be mentioned that if all the bundles in reactor are DU, the reactor would be sub-critical by about 21 mK . Thus, 672 NU bundles in the optimum configuration enhance core reactivity by about 40 mK .

### 5.3. Actual disposition of DU bundles

Some of the optimized loading patterns obtained by EDA are explicitly shown in Figs. 5-7. They are for quarter core symmetric case. Fig. 5 shows the disposition of 284 DU bundles (row 1 of Table 3) pattern which is symmetric in $X Z$-direction and satisfies all the safety criteria for nominal ( $100 \%$ FP and AR IN position) core configuration. This configuration is superior to that given in Fig. 1 in terms of $K_{\text {eff }}$ and maximum permissible reactor power. In Fig. 6, a pattern with 1500 DU bundles (row 5 of Table 3) with quarter-core symmetry is shown. Fig. 7 shows a pattern containing 3000 DU bundles (row 7 of Table 6).

## 6. Conclusion and discussion

Several small sized 220 MWe PHWRs have been constructed and are in operation in India and a few more units are awaited. The problem of choosing locations of DU bundles in the initial core of such a PHWR to achieve nearly full power was considered. This is a fairly complex combinatorial problem with many conflicting requirements. One has to obtain full reactor power, maximum possible reactivity, permitted bundle and channel powers and sufficient shutdown system worth. In one of the Indian PHWRs, 384 DU bundles were loaded at manually intuited locations. Here, the problem of DU loading is explored by using an evolutionary algorithm EDA. For this, it is necessary to perform a very large number $\left(\sim 10^{5}\right)$ of neutron diffusion calculations. The parallel super computer system EKA built at computational research laboratory (CRL) in Pune, India was used.

Several alternative configurations with 438, 284, 472 and 280 DU bundles (listed in Tables 2-4) have been found which can give higher $K_{\text {eff }}$ and higher power than the manually obtained configuration in Table 1. The possibility of increasing DU loading was also studied. It is found that up to about 2500 DU bundles (Fig. 4 and Tables 2-4) can be loaded and 100\% FP can be obtained in nominal core configuration without violating any safety features.

Some additional measures were contemplated to further increase the loading of DU bundles and thus reduce the loading of NU bundles. One can think of relaxing the total power requirement to greater than $50 \%$ FP. At the cost of xenon override time, one can keep the ARs out of the core. With these two measures, it is found that the optimum configuration has as many as 3000 DU bundles (about $80 \%$ of total bundles) with sufficient excess reactivity leading to a huge saving of NU bundles.

A clarification regarding maximum bundle power is in order. The precise safety limit of maximum permissible bundle power is 462 kW , which cannot be violated. In reactor operation, however, usually the maximum bundle power is kept below 440 kW to allow some margin. Hence, in the computations also, the limit of 440 kW was used. A slightly higher value, however, is seen to occur in Tables 1-3 and is acceptable. Such slightly higher value of MBP is occasionally found in optimum pattern due to following reasons. While performing the thousands of whole core diffusion calculations needed by the algorithm, the relative convergence criteria on point wise fluxes are not kept too tight to save CPU time. Few of the best configurations obtained at the end of full EDA execution are re-evaluated by diffusion calculations with very tight convergence of about $1.0 \mathrm{E}-8$, which may give slightly different results. Finally, only one of these few (almost equally good) configurations is chosen by inspection of the various criteria.

Two models have been used: The $X Z$-model which requires optimization in one-fourth core and $X$-model which requires optimization in one-half core. The random correction approach and penalty approach were initially applied to the cheaper $X Z$-model for the $100 \%$ FP case (Table 3 and 4). It was observed that quality of solution obtained by the two approaches is not much different. Hence, to save time, only one of the approaches, namely the random approach was retained for the costlier $X$-model for the $100 \%$ FP case. All other studies with $50 \%$ FP were also done with only random approach. Thus, only one approach was used in many cases to save labor and make best use of the limited parallel computational facility available to us.

If one relies solely on manual guess-work, one would choose only the central locations in the core for placing the DU bundles as in the configuration shown in Fig. 1. This is because one expects that DU bundles far from core centre would increase the peaking. The evolutionary algorithms, on the other hand explores all possible combinations and bring out the fact that in an optimum arrangement, some bundles have to be kept away from the centre, both axially and radially. This is ultimately useful in terms of better safety and economy.

On the whole, a variety of options of DU loading which differ widely in terms of number of DU bundles and their arrangements have been analysed using EDA. An appropriate choice can be made depending on the priorities and requirements at any given time. Indian nuclear power program involves further development of small and large sized PHWRs of 220 MWe, 540 MWe and 700 MWe capacities. The present method can be used to solve similar optimization problems in these reactors.

## Acknowledgements

The authors are highly thankful to Shri A.N. Kumar, Head, RP\&S Section, NPCIL and Smt. S. Ray, NPCIL for useful discussions and support.

## References

Bajaj, S.S., Gore, A.R., 2006. The Indian PHWR. Nucl. Eng. Des 236, 701-722.

Balakrishnan, K., Kakodkar, A., 1994. Optimization of the initial fuel loading of the Indian PHWR with thorium bundles for achieving full power. Ann. Nucl. Energy 21, 1-9.
Carter, J.N., 1997. Genetic algorithm for incore fuel management and other recent developments in optimization. Adv. Nucl. Sci. Technol. 25, 113-149.
Goldberg, D.E., 1989. Genetic Algorithms in Search Optimization and Machine Learning. Addison-Wesley, Reading, New York.
Jiang, S., Ziver, A.K., Carter, J.N., Pain, C.C., Goddard, A.J.H., Franklin, S., Phillips, H.J., 2006. Estimation of distribution algorithms for nuclear reactor fuel management optimization. Ann. Nucl. Energy 33, 1039-1057.
Judd, R.A., Rouben, B., 1981. Three dimensional kinetics benchmark problem in a heavy water reactor. Report No. AECL-7236.
Krishnani P.D., 1992. CLUB - a multi-group integral transport code for lattice calculations of PHWR cells. Report BARC/1992/E/017.
Kropaczek, D.J., Turinsky, P.J., 1991. In-core fuel management optimization for PWRs utilizing simulated annealing. Nucl. Technol. 95, 9-31.
Michalewicz, Z., 1999. Genetic Algorithms + Data Structures = Evolution Programs. Springer.

Mishra, Surendra, Modak, R.S., Ganesan, S., 2009. Optimization of thorium loading in fresh core of Indian PHWR by evolutionary algorithms. Ann. Nucl. Energy 36, $948-955$.
Montes, J.L., Ortiz, J.J., Requena, I., Perusquia, R., 2004. Searching for full power control rod patterns in a boiling water reactor using genetic algorithm. Ann. Nucl. Energy 31 (16), 1939.
Pacheco, P.S., 1997. Parallel Programming with MPI. Morgan Kaufmann Publishers Inc., San Francisco, CA.
Pereira, C.M.N.A., Sacco, W.F., 2008. A parallel Genetic Algorithm with niching technique applied to a nuclear reactor core design optimization problem. Prog. Nucl. Energy 50, 740-746.
Pereira, C.M.N.A., Schirru, R., Martinez, A.S., 1999. Basic investigations related to genetic algorithm in core designs. Ann. Nucl. Energy 26, 173-193.
Salomon, R., 1998. Evolutionary algorithm and gradient search: similarities and differences. IEEE Trans. Evolution. Comput. 2 (2), 45-55.
Turinsky, P.J. et al., 2005. Evolution of nuclear fuel management and reactor operational aid tools. Nucl. Eng. Technol. 37 (1), 79-90.