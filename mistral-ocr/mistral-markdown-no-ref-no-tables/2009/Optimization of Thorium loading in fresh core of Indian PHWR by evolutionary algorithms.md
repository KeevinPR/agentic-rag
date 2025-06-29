# Optimization of Thorium loading in fresh core of Indian PHWR by evolutionary algorithms 

Surendra Mishra ${ }^{\mathrm{a}, \mathrm{a}}$, R.S. Modak ${ }^{\text {b }}$, S. Ganesan ${ }^{\mathrm{c}}$<br>${ }^{a}$ Safety Directorate, Nuclear Power Corporation of India Limited, Mumbai 400 094, India<br>${ }^{\mathrm{b}}$ Theoretical Physics Division, Bhabha Atomic Research Centre, Mumbai 400 085, India<br>${ }^{\mathrm{c}}$ Reactor Physics Design Division, Bhabha Atomic Research Centre, Mumbai 400 085, India

## A R T I C L E I N F O

Article history:
Received 24 October 2008
Received in revised form 23 February 2009
Accepted 1 March 2009
Available online 5 April 2009

## A B S T R A C T

This paper is concerned with the Indian design of a 220 MWe Pressurized Heavy Water Reactor having Natural Uranium fuel and heavy water as moderator and coolant. At the beginning of life, it is necessary to flatten the power by loading some Thorium bundles to achieve a nearly full power operation. The determination of best possible locations of Thorium bundles, which maximize fuel economy as well as safety, is a complex combinatorial optimization problem. About two decades ago, an optimum configuration of Thorium bundles was successfully arrived at by using a gradient based method and this pattern was actually loaded in the Indian PHWR at Kakrapar which went critical in 1992 [Balakrishnan, K., Kakodkar, A., 1994. Optimization of the initial fuel loading of the Indian PHWR with Thorium bundles for achieving full power. Annals of Nuclear Energy 21, 1-9]. Here, the same problem is revisited for two reasons. Firstly, computational techniques based on completely different philosophy namely "Genetic Algorithm" (GA) and "Estimation of Distribution Algorithm" (EDA) have been used. Secondly, the enormous increase in computing power during the last two decades is expected to provide a more exhaustive search. Indeed, it has been possible to find out many feasible Thorium configurations of comparable merit. Our results are similar with the result of the earlier BARC study but provide a range of additional configurations. As in earlier BARC work, we find that one can get from $95 \%$ to $97 \%$ full power without violating various safety aspects such as maximum bundle power, maximum channel power, channel outlet temperature and worth of the two shutdown systems. In the present work, the number of Thorium bundles which can be loaded range from 22 to 34 . One of the outcomes of this study is that the computational techniques suitable for this type of problems have been identified and developed. Further studies involving the use of some other evolutionary methods and problems such as optimization of depleted Uranium loading are in progress.
(c) 2009 Elsevier Ltd. All rights reserved.

## 1. Introduction

The Pressurized Heavy Water Reactor (PHWR) designs originated in Canada belong to two categories: small sized PHWR ( 220 MWe ) with moderator dump as a shutdown system and large sized PHWR ( 540 MWe and above) having shutoff rods and liquid poison addition for shutdown. There is an Indian PHWR design ( 220 MWe ) which is small in size and yet does not have moderator dump system. It uses two independent shutdown systems: 14 mechanical shutoff rods known as Primary Shutdown System (PSS) and 12 liquid poison tubes known as Secondary Shutdown System (SSS). There are nine such power plants in operation and three more plants are awaited (Bajaj and Gore, 2006). The present

[^0]studies are concerned with an optimization problem of loading of Thorium bundles for power flattening in the initial core of this type of reactors.

The PHWR is a horizontal tube type reactor fuelled with Natural Uranium (NU) with heavy water as both coolant and moderator. The coolant is physically separated from the moderator by being contained inside the pressure tube where it is maintained at high temperature $\left(\sim 271^{\circ} \mathrm{C}\right)$ and pressure. The moderator heavy water is at a relatively low temperature $\left(\sim 54.4^{\circ} \mathrm{C}\right)$ and is unpressurized. The reactor core consists of 306 pressure tubes arranged along a square lattice of 22.86 cm pitch. The fuel pins and the coolant are contained within these pressure tubes. The direction of coolant flow in adjacent channels is opposite. The direction of the bundle movement (fuelling direction) is the same as that of the coolant flow, so that alternate channels are fuelled in opposite directions. The fuel is in the form of a string of 12 bundles, each bundle is a 19 -rod cluster of 49.5 cm length. Of the 12 bundles, 10 are in the active portion of the core, the remaining two; one bundle on each

[^1]
[^0]:    ${ }^{a}$ Corresponding author. Tel.: +91 222599 4678; fax: +91 222599 4691.
    E-mail addresses: smishra@npcil.co.in (S. Mishra), rsmodak@barc.gov.in (R.S. Modak), ganesan@barc.gov.in (S. Ganesan).

[^1]:    0306-4549/5 - see front matter (c) 2009 Elsevier Ltd. All rights reserved. doi:10.1016/j.anucene.2009.03.003

side, is outside the core. For the purpose of reactor regulation there are four adjuster rods, two regulating rods and two shim rods. As mentioned above, there are two independent shutdown systems called PSS and SSS. More detailed description can be found in reference (Balakrishnan and Kakodkar, 1994).

### 1.1. Nature of the problem

Since NU bundles are used as fuel, there is little excess reactivity in the hot equilibrium core. Hence, to operate the PHWR reactor on a continuous basis, fuelling is done on-power by simply pushing eight fresh bundles in a selected channel almost everyday. The fuelling direction is opposite in adjacent channels. It helps in axial flux flattening. For the radial flux flattening, the core is treated as consisting of two radial zones for the purpose of fuelling: inner and outer. The fuel discharge burnup of inner region is higher than that of the outer region or in other words, fuelling is less frequent in inner zone channels than outer zone channels. This helps in radial power/flux flattening so that more power can be extracted from the core than if the burnup had been uniform throughout. This is true for an equilibrium core. However, at the beginning of the core life, when the entire core is loaded with fresh NU fuel, the power distribution is highly peaked in the centre due to lack of radial flux flattening. Hence, it will not be possible to get the full rated power from the core right from beginning unless some other way of achieving power flattening is followed. It is possible to flatten the power distribution by loading some depleted uranium bundles in the central region of the core. However, there is an incentive in the Indian context for replacing the Depleted Uranium (DU) by Thorium (Th) bundles to initiate thorium fuel cycle studies. However, choosing locations of Th bundles is more difficult. Since thorium is a much stronger absorber than depleted Uranium, it causes stronger flux depressions in its vicinity. This affects the reactivity worth of the two shutdown systems. On the whole, the number and locations of Th bundles have to be chosen so that the following conditions are fulfilled:
(1) $K_{\text {eff }}$ is maximum possible so that reactor can operate without fuelling for longer time leading to better fuel economy.
(2) The operating limit on channel outlet temperature $\left(299^{\circ} \mathrm{C}\right)$ is obeyed.
(3) Maximum bundle power is less than 440 KW .
(4) The reactivity worth of each shutdown device is not less than 30 mk .

The problem of obtaining an optimum distribution of Thorium bundles which satisfies above criteria was solved successfully about two decades ago (Balakrishnan and Kakodkar, 1994) and a suitable distribution consisting of 35 Th bundles was arrived at. This pattern was subsequently loaded in the Indian PHWR at Kakrapar (KAPS-1), which went critical in September 1992. A gradient based method was used to find the solution.

Here, the above optimization problem is revisited by using some modern techniques which have evolved recently and are completely different than the gradient method. Two techniques belonging to the class of evolutionary algorithms have been used. In the present studies, it was possible to exploit the several orders of magnitude higher computing power available now-a-days. We were able to obtain many possible distributions of Thorium which fulfill the required criteria. Several acceptable configurations in which the number of Th bundles required varies from about 2234 were found as solutions. The solutions obtained here are comparable in quality with the earlier solution (Balakrishnan and Kakodkar, 1994). One of the outcomes of present studies is to establish utility of evolutionary methods for this class of problems. These methods start with fully random guess solutions and do not
need any prior experience or intuition on the nature of desired optimum solution.

The fabrication and loading of Thorium bundles is a non-standard procedure and it should be preferable to use as small number of Th bundles as possible. However, in general, it is useful to know the features of best configurations that can be obtained by using different number of Th bundles so as to make an appropriate choice. The present paper is directed towards achieving this. One way to do this is to find out the optimum configuration that can be obtained with a certain fixed number of Thorium bundles, say $N_{\mathrm{Th}}$, by evolutionary algorithms; and then repeat the study for various values of $N_{\mathrm{Th}}$. This requires too many optimization studies. Hence, in the present work, we have found optimum configurations that can be obtained with $N_{\mathrm{Th}}$ lying in some interval and then repeated the study for a few different intervals.

### 1.2. Plan of the paper

Our paper is organized as follows: in Section 2, combinatorial complexity of the problem is highlighted. In Section 3, earlier work by Balakrishnan and Kakodkar (1994) is briefly described and the particular solution obtained by them is explicitly presented. Section 4 covers the methods followed in present studies. Section 5 describes the parallelization of the problem. Section 6 presents results obtained by present approach. Section 7 gives conclusion and discussion.

## 2. Combinatorial complexity

The cross-sectional view of reactor core in $X-Y$ plane is shown in Fig. 1. There are 306 channels (from $A-T$ in $Y$-direction and 120 in $X$-direction). These channels are horizontal and extend in $Z$ direction up to about 500 cm . There is no top-bottom symmetry in the core. There is however, left-right symmetry. Hence, only half part of the core (only 153 channels) has been considered to reduce the problem size. Therefore, there are $153 \times 12=1836$ fixed bundle locations. The given number of Th bundles has to be arranged in these locations in an optimum manner. As an example, for 30 Th bundles, this can be done in ${ }^{1836} \mathrm{C}_{30}$ ways (approximately $10^{65}$ ). In order to assess the merit of any configuration, it is necessary to make a K-eigenvalue calculation for that configuration. In our case we use two energy groups (thermal and fast) and threedimensional $X-Y-Z$ geometry and diffusion theory based core cal-
![img-0.jpeg](img-0.jpeg)

Fig. 1. Loading derived by gradient search method by Balakrishnan and Kakodkar (1994).

culations. From the K-eigenvalue and power distribution, one can check whether the desired conditions are fulfilled. Additional calculations are needed per configuration to compute the worth of PSS and SSS.

Thus, a brute force approach will involve about $10^{65}$ transport/ diffusion core calculations, one for each configuration for choosing the best one. This is obviously impossible and some techniques are needed so that desired optimum is obtained with much smaller number of calculations. Such techniques are discussed in the next two sections.

## 3. Earlier studies

As mentioned earlier, there are total $3672(306 \times 12)$ locations where one has to decide whether NU or Th bundle is to be loaded. This problem was solved earlier by Balakrishnan and Kakodkar (1994) using a gradient based method as follows: a few decision variables are chosen to characterize a given Thorium bundle distribution. For instance the mean distance of all shutoff rods from all Th bundles is a decision variable. An objective function was defined which characterizes flux flattening, shutoff devices worth, etc. One starts with a guess distribution of Th bundles. The gradient of objective function with respect to decision variables is estimated and used to gradually update the Th distribution till an optimum is reached. The specific configuration reached was successfully loaded in the KAPP-1 220 MWe power station in 1992. The optimum Th bundle configuration obtained by Balakrishnan and Kakodkar (1994) is explicitly shown in Fig. 1. There are 35 Th bundles in 35 different channels. The figure shows all the 306 channels. In the channel containing Th bundle, a number in Arabic numerals is written. This number indicates axial position of the Th bundle in active part of that channel. This number lies between 1 and 10 . The serial number of bundle is counted in the direction of coolant flow in that channel which is also direction of fuelling. The channels in Fig. 1 where no number is written are fully occupied by NU bundles. The maximum allowed power with this configuration was $95.5 \mathrm{XFP}$ and it satisfied all other constraints. It can be seen that the Thorium bundles are widely distributed in radial as well as axial directions.

## 4. Present studies

### 4.1. Computational techniques used

The use of gradient based search method, described above, generally requires a good degree of intuition and experience. Since small changes are made around a certain configuration, there is a possibility of getting trapped in a local minimum (Salomon, 1998). There exists another technique called "simulated annealing" (Kropaczek and Turinsky, 1991) in which the same gradient method is used, but one occasionally accepts an inferior solution with certain probability. This probability is slowly reduced as the optimum solution is approached. This helps in getting out of local minima and reaching to a global optimum.

There are yet other techniques based on Genetic Algorithms (GA). They are based on a philosophy which is completely different from the gradient methods. One starts with many different candidate configurations instead of just one in the gradient method. The fitness of these configurations is evaluated. Parents are selected from these configurations. Candidates with better fitness have higher chance of getting selected. Then, children are formed by cross-over between two parents. The process is continued for several generations till convergence. Occasionally, a mutation is performed which involves a small random change in the configuration. This algorithm mimics the process of natural evolution of biological species and more details can be found in Goldberg (1989)
and Pereira et al. (1999). Unlike gradient based methods, the GA does not require a reasonable guess to start with. It does not usually get trapped in local minima and explores the full solution space leading to near global optimum.

We have also tried another slightly different algorithm called Estimation of Distribution Algorithm (EDA). In EDA (Jiang et al., 2006), the combination process in GA is replaced by estimation of distribution and sampling as per this distribution to generate new candidate solutions. The simulated annealing, GA and EDA have been extensively used to solve light water reactor fuel management and control design problems (Pereira and Sacco, 2008; Montes et al., 2004; Jiang et al., 2006; Turinsky et al., 2005). In the present paper, we have applied GA and EDA techniques to optimize the initial fuelling in PHWR. Both these algorithms belong to the general class of evolutionary algorithms.

The implementation of the GA and EDA algorithms needs several thousands of neutronics computations. This is possible thanks to the high speed processors and parallel computing facilities available today.

It may be mentioned that the reactor core (Fig. 1) has left-right symmetry. Hence we choose a pair of channels in which Thorium is to be loaded consistent with this symmetry. However, the coolant flow as well as fuelling direction is opposite to each other in this pair of channels. Hence the location of Thorium bundle in this pair of channels is chosen to be anti-symmetric in Z-direction.

### 4.2. The neutron diffusion code

As mentioned in Section 2, a 3-D 2-group neutron diffusion code is needed to evaluate the fitness of any given configuration. An in-house computer code 'DOLP' has been developed as part of the present study and used for 3-D 2-group neutron diffusion calculations. It solves neutron diffusion equation by finite difference approximation. The code has been validated against AECL PHWR benchmark (Judd and Rouben, 1981). The results obtained by this code for the configuration shown in Fig. 1 are presented in Table 1. In previous studies by Balakrishnan and Kakodkar (1994) the cross-sections available at that time were used. Now, we have used the presently available library to find the two group cross-sections. Hence, there are slight differences in our results and previous work but they do not affect conclusions.

The homogenized two energy group lattice cross-sections for NU as well as Th bundles, required for diffusion calculations, were generated using the 2-D transport theory code CLUB (Krishnani, 1992) using the 69 energy group WIMSD library derived from ENDF/B-VL8 basic evaluated nuclear data file. The details of the WIMSD library are available in the website: http://www-nds.indcentre.org.in/wimsd/downloads2.htm.

### 4.3. The optimization problem

The optimization problem is defined as follows:
Objective: to maximize the effective multiplication factor $\left(K_{\text {eff }}\right)$.

Table 1
Comparison of the results obtained by in-house code DOLP with the earlier work (Balakrishnan and Kakodkar, 1994) for configuration shown in Fig. 1.

Constraints: following constraints are imposed:

- Total numbers of Th bundles are restricted within a predetermined interval.
- The reactor power should be close to $100 \%$ Full Power (FP).
- The maximum channel power (MCP) should be less than 3.08 MW.
- The maximum bundle power (MBP) should not cross the operating limit 440 KW .
- The maximum channel outlet temperature (MCOT) should not be more than $299^{\circ} \mathrm{C}$.
- The reactivity worth of two independent shutdown systems, i.e. SDS-1 and SDS-2 should not be less than 30 mk .

We use the "penalty method" for handling constraints. The penalty method penalizes infeasible (or unfavorable) individuals. In general, it transforms a constrained optimization problem to an unconstrained problem by defining penalty function (Michalewicz, 1999). Here, the objective function to be maximized has been defined to take care of constraints as follows:
$\mathrm{Fit}=K_{\text {eff }}-\mathrm{F} 1-\mathrm{F} 2-\mathrm{F} 3-\mathrm{F} 4-\mathrm{F} 5-\mathrm{F} 6$
where
$\mathrm{F} 1=(\mathrm{FP} 0-\mathrm{FP}) \times$ Afp if FP $<$ FP0 and zero otherwise.
$\mathrm{F} 2=(\mathrm{CP}-\mathrm{CP} 0) \times$ Acp if $\mathrm{CP}>\mathrm{CP} 0$ and zero otherwise.
$\mathrm{F} 3=(\mathrm{COT}-\mathrm{COT} 0) \times$ Acot if COT $>$ COT0 and zero otherwise.
$\mathrm{F} 4=(\mathrm{BP}-\mathrm{BP} 0) \times$ Abp if $\mathrm{BP}>\mathrm{BP} 0$ and zero otherwise.
$\mathrm{F} 5=(\mathrm{PSS} 0-\mathrm{PSS}) \times$ Apss if $\mathrm{PSS}<\mathrm{PSS} 0$ and zero otherwise.
$\mathrm{F} 6=(\mathrm{SSSO}-\mathrm{SSS}) \times$ Asss if SSS $<$ SSS0 and zero otherwise.
The notation used is as follows:
$\mathrm{FP} 0=100$, corresponding to full rated power.
FP is the maximum allowable power in a given configuration.
$\mathrm{CP} 0=3.08$, corresponding to maximum permitted channel power.
CP is the maximum channel power in a given configuration.
$\mathrm{COT} 0=299$, corresponding to maximum permitted channel outlet temperature.
COT is the maximum channel outlet temperature in a given configuration.
$\mathrm{BP} 0=440$, corresponding to maximum permitted bundle power.
BP is the maximum bundle power in a given configuration.
PSSO $=32$, a slightly higher value than minimum worth of PSS in millik.
PSS is the worth of PSS in a given configuration.
$\mathrm{SSSO}=32$, a slightly higher value than minimum worth of SSS in millik.
SSS is the worth of SSS in a given configuration.
The parameters Afp, Acp, Acot, Abp, Apss and Asss are suitably chosen constants to give a weight to each of the factors. The procedure to decide these constants is somewhat arbitrary. About 1000 random configurations containing 36 Th bundles were generated. The $K$-eigenvalue and flux distribution were calculated for each of them. The fluxes were normalized to get the maximum channel power equal to the CPO (=3.08). The PSS and SSS worths were also found for each configuration. From these results, the typical extent of deviations of FP, COT, BP, PSS and SSS from the limiting values FP0, COT0, BP0, PSS0 and SSS0 were estimated. The constants Afp, Acot, Abp, Apss and Asss were found such that the penalty caused by each factor for such deviation is of the order of $K_{\text {eff }}$ (which is of order unity). The constant Acp is arbitrary, since the
term containing Acp in Eq. (1) always vanishes. It may be mentioned that one can obtain the constants in some other way also and Eq. (1) is a general expression.

In both the methods GA and EDA, the objective function (also called fitness function) given by Eq. (1) has to be evaluated to determine the fitness of any given configuration. It can be seen from Eq. (1) that if the maximum achievable power is close to full power, fitness increases. If the worth of shutdown system is less than 32 mk , fitness will be lesser. Similarly, other terms in Eq. (1) can be understood.

### 4.4. Use of Genetic Algorithm

As mentioned earlier, GAs are optimization techniques based on selection and recombination of promising solutions. The collection of candidate solutions is called population of the GA whereas candidate solutions are sometimes called as individuals, chromosomes, etc. Each individual is an encoded representation of variables of the problems at hand. Each component (variable) in an individual is termed as gene. A pseudo model of the algorithm is depicted in Fig. 2. For the tournament selection (Goldberg, 1989) [item 4 in Fig. 2], the number $M$ was chosen to be 2 . There are two primary factors to be considered: population diversity and selective pressure. An increase in selective pressure decreases the diversity of the population and vice versa. Too much selective pressure gives a faster but premature convergence. As $M$ increases, selective pressure increases. The value of $M=2$ has been found to be good in several applications (Michalewicz, 1999, p. 61) and was used by us.

Our selection of genotype is not based on binary strings. As mentioned by Carter (1997), the representation should be as natural as possible. In the PHWR, there are 306 channels, each containing 12 bundles. For each channel, we generate a uniformly distributed integer number, say $p$, between 1 and 12 . As a result of cross-over, the offspring has 1 to $p$ bundles identical to first parent and $(p+1)$ to 12 bundles identical to the second parent for that particular channel.

### 4.5. Use of Estimation of Distribution Algorithm

EDAs belong to the class of population based optimization algorithms. EDAs are motivated by the idea of discovering and exploiting the interaction between variables in the solution. In EDAs, the two GA operations of recombination and mutation are replaced by estimation of distribution and sampling. In each generation, $N$ individuals are generated by sampling probability distribution. The fit-

1. Initialize the population (Size=N) randomly
2. Evaluate the fitness of each individual based on their $\mathrm{K}_{\text {eff }}$, maximum permissible reactor power, channel power, channel outlet temperature, bundle power and the worths of PSS and SSS as obtained by diffusion code DOLP using Eq.(1) in section 4.3 .
3. Either continue for new generation calculations or terminate the execution.
4. Selection of a pair of individuals based on tournament selection method (tournament between $\mathrm{M} \times \mathrm{N}$ candidates and best one wins).
5. Generate new individual by using uniform crossover operator on the selected pair of individuals with Pc crossover rate. The newly generated individual may not have desired number of NU or Th bundles. Hence a correction operator is applied. The fuel type which is more in number than the specified value is randomly changed into other type.
6. Steps 4 and 5 are repeated to generate N new individuals.
7. The newly generated N individuals are subjected to mutation operator with Pm mutation rate. The shuffle type mutation operator has been used. The fitness of new N individuals is found out as in step 2 .
8. We have N old and N new individuals with known fitness. Out of these, N individuals with better fitness are retained.
9. Go to step 3 .

Fig. 2. Pseudo GA model used for optimization.


Fig. 3. Pseudo EDA model used for optimization.
ness is evaluated for each of them by diffusion calculations and the best $M$ individuals are selected to estimate probability distribution. The probability that given location is occupied by NU or Th bundle is estimated from the selected $M$ individuals. The performance of an EDA highly depends on how well it estimates and samples the probability distribution. Univariate Marginal Distribution Algorithm (UMDA) assumes no interaction among variables. The probability distribution is estimated using UMDA (Jiang et al., 2006) in the present case. A pseudo model of the algorithm used for optimization is given in Fig. 3. In case of EDA, the Probability Distribution Function (PDF) was generated using $30 \%$ dominated individuals [item 4 in Fig. 3] of the population size. Alpha is chosen 0.05 .

## 5. Parallelization

The evolutionary algorithms (GA and EDA) evolve population of candidate solutions. They take a great amount of computational time. The most time consuming part is the evaluation of "fitness" corresponding to each individual of the population. This requires full core simulation by diffusion calculation from which objective function or "fitness" given by Eq. (1) can be computed. Hence, these diffusion calculations for different individuals in the population were carried out in parallel. The parallelization was achieved using the MPI Library functions (Pacheco, 1997) as follows: The rank 0 processor is called here as MASTER processor and others are SLAVE processors. The MASTER will generate population containing $N$ individuals. If there are $S$ SLAVE processors, each SLAVE is assigned the job of evaluating the fitness of $(N / S)$ individuals by diffusion calculations. The results are returned to the MASTER. The MASTER will generate new population and send ( $N / S$ ) individuals to each slave for fitness evaluation. This is continued for all the generations. The computer code DOLP has been written to execute this using standard message passing interface (MPI) library functions in FORTRAN. The distributed memory parallel computer systems (Apte et al., 2008) AMEYA/AJEYA at BARC were used.

## 6. Results

### 6.1. Studies with $36 \pm 4$ Thorium bundles

At the outset, it was decided to try number of Thorium bundles nearly similar to the number (35) in the earlier work. Thus the bundles were restricted to lie within $36 \pm 4$, i.e. in the interval
![img-2.jpeg](img-2.jpeg)

Fig. 4. The variation of fitness function for population size 1000 and Th bundles $36 \pm 4$.
(32, 40). As mentioned in Section 3, the left-right symmetry is exploited. Owing to this, only even number of Th bundles is considered. Thus, the possible numbers are $32,34,36,38$ and 40 . Both GA and EDA methods were used.

Analysis with GA and EDA was carried out for four sizes of population of configurations, namely, 1000, 4000, 6000 and 8000. The observations are as follows:
(1) The variation of the fitness function derived from GA and EDA (keeping total number of Thorium bundles $36 \pm 4$ ) against generation number for population size 1000, 4000, 6000 and 8000 is presented in Figs. 4-7. EDA gives better fitness than GA for all population sizes. For population size greater than 1000, GA initially evolves faster than EDA, but gets saturated after about 50 generations. The fitness with EDA keeps improving beyond 50 generations and gives better result.
(2) GA and EDA dependencies on population size are shown in Figs. 8 and 9. In case of GA, final result improves with population size. Hence, with GA one needs to use a large population size. On the other hand, with EDA, result is almost same for all population sizes 1000, 4000, 6000 and 8000. The CPU time (computational effort) is proportional to the product of the population size and the number of generations. Hence, the use of population size 1000 is considered adequate in
![img-2.jpeg](img-2.jpeg)

Fig. 5. The variation of fitness function for population size 4000 and Th bundles $36 \pm 4$.

![img-6.jpeg](img-6.jpeg)

Fig. 6. The variation of fitness function for population size 6000 and Th bundles $36 \pm 4$.
![img-4.jpeg](img-4.jpeg)

Fig. 7. The variation of fitness function for population size 8000 and Th bundles $36 \pm 4$.
our studies in case of EDA. It can be seen from Fig. 9 that, the total number of diffusion calculations needed by EDA is minimum for this population size.

It is important to note that, the above observations are based on the specific GA and EDA model used here and are not a general
![img-5.jpeg](img-5.jpeg)

Fig. 8. GA performance for different population size for $36 \pm 4$ Th bundles.
![img-6.jpeg](img-6.jpeg)

Fig. 9. EDA performance for different population size for $36 \pm 4$ Th bundles.
conclusion. This is further explained in Section 7. Table 2 shows the characteristics of some configurations with around 36 bundles which satisfy all constraints.

### 6.2. Studies for different number of Thorium bundles

It was felt that it may be possible to use a different number of Thorium bundles and yet obtain all the desired characteristics. To

Table 2
Optimization results with $36 \pm 4$ Thorium bundles for different population size using EDA.
Table 3
Optimization results with different Thorium bundles for 1000 population size using EDA.
![img-7.jpeg](img-7.jpeg)

Fig. 10. The optimum configuration with $32(36 \pm 4)$ Thorium bundles.
![img-8.jpeg](img-8.jpeg)

Fig. 11. The optimum configuration with $30(28 \pm 4)$ Thorium bundles.
study this, three more bundle number intervals $28 \pm 4,24 \pm 4$ and $18 \pm 4$ were tried using EDA keeping a population size of 1000 . In all these cases, satisfactory configurations were obtained. They are listed in Table 3.

### 6.3. Actual disposition of Thorium bundles

Figs. 10-13 give detailed pictures of four different optimum configurations with different number of Th bundles. In these figures, an Arabic numeral (say $x$ ) is printed in some channels. These channels contain one or more Thorium bundles. The table just
![img-9.jpeg](img-9.jpeg)

Fig. 12. The optimum configuration with $24(24 \pm 4)$ Thorium bundles.
![img-10.jpeg](img-10.jpeg)

Fig. 13. The optimum configuration with $22(18 \pm 4)$ Thorium bundles.
below the core map shows axial distribution of fuel bundles (U/ Th) for each value of $x$.

## 7. Conclusion and discussion

Several small sized 220 MWe PHWRs have been constructed and are in operation in India and a few more units are awaited (Bajaj and Gore, 2006). The problem of choosing locations of Thorium bundles in the initial core of such a PHWR to achieve nearly full power was considered. This is a fairly complex combinatorial problem with many conflicting requirements. One has to obtain more than $95 \%$ full power, maximum possible reactivity, permitted bundle and channel powers and sufficient shutdown system worth. This problem was successfully solved about two decades ago by using a gradient based method and a specific configuration 35 Thorium bundles was loaded in the PHWR at Kakrapar, India. Here, the problem is revisited in order to explore it further by using two

evolutionary algorithms GA and EDA, which are based on quite different principles than gradient based method. In our approach, it is necessary to perform a very large number $\left(\sim 10^{5}\right)$ of neutron diffusion calculations. This has been possible due to the use of parallel super computer system ANUPAM at BARC.

It is found that one can have a number of configurations which meet all the required criteria. We find that the number of Thorium bundles to be loaded range from 22 to 34. Figs. 10-13 explicitly show the locations of Thorium bundles for some of the configurations obtained in this study. One general observation is that the bundles are less widely distributed in XY plane if their total number is small as seen in the case of 22 thorium bundles (Fig. 13). Another interesting point to be noted is that in our result we obtain occasionally the presence of more than one Thorium bundle ( 2,3 or even 4 bundles) in the same channel. It seems unlikely to guess this feature by pure logic because normally one would expect to have only one Thorium bundle in one channel so as to make best use of limited Thorium bundles for power flattening. One of the observations in the present studies is that EDA is to be preferred over GA because it gives much better results with lesser computational effort. However, it should be pointed out that, in each optimization study, we need the number of Th bundles $N_{\mathrm{Th}}$ to lie in a certain interval say ( $\mathrm{n} 1, \mathrm{n} 2$ ). The parents obey this property. But when cross-over takes place, the progeny may not have $N_{\mathrm{Th}}$ lying in this interval. At this stage, the excess bundles are randomly converted to other type as shown in Fig. 2 for the GA. Similar random correction is done in EDA algorithm (Fig. 3). This procedure of randomly correcting the non-valid solution may cause some loss of search pattern driven by fitness. This can affect the performance. Hence the conclusions obtained are restricted to the particular way of finding solution followed here and are not general conclusions on the performance of GA and EDA.

If certain models like specific cross-over PMX are used, the random correction used here is not needed. Alternatively, it may also be possible to include a penalty for those configurations which have number of thorium bundles outside the intended interval; instead of making a random correction. This will retain these solutions in the evolution process. It is planned to investigate these aspects in a subsequent work.

The Indian nuclear power program involves further development of small and large sized PHWRs of 220 MWe, 540 MWe and 700 MWe capacities. The present method can be used to solve fuel optimization problems in these reactors. We have carried out similar optimization studies which use depleted $U$ in place of Thorium
under a variety of constraints. We hope to present these results in near future.

## Acknowledgements

The authors are highly thankful to the referee for many thought provoking and constructive suggestions which have been useful to improve the manuscript. We also thank NPCIL and BARC authorities and Shri. A.N. Kumar, Head, RP\&S Section, NPCIL and Smt. S. Ray, NPCIL for their interest and support.
