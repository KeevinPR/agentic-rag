# Selection of fuel channels for Thermal Power Measurement in 700 MWe Indian PHWR by evolutionary algorithm 

Surendra Mishra ${ }^{\mathrm{a}, \mathrm{v}}$, R.S. Modak ${ }^{\mathrm{b}}$, S. Ganesan ${ }^{\mathrm{c}}$<br>${ }^{a}$ Safety Directorate, Nuclear Power Corporation of India Limited, Mumbai 400 094, India<br>${ }^{\mathrm{b}}$ Theoretical Physics Division, Bhubha Atomic Research Centre, Mumbai 400 085, India<br>${ }^{c}$ Reactor Physics Design Division, Bhubha Atomic Research Centre, Mumbai 400 085, India

## A R T I C L E I N F O

Article history:
Received 6 May 2011
Received in revised form 28 February 2012
Accepted 1 March 2012

## A B S T R A C T

This paper presents studies on the design of Thermal Power Monitoring System (TPMS) for the forthcoming 700 MWe Indian Pressurized Heavy Water Reactor (PHWR). This reactor contains total 392 horizontal fuel channels. Each channel contains clustered natural Uranium fuel along with associated heavy water coolant placed inside a pressure tube. The coolant in different fuel channels is physically and thermally isolated from each other inside the core. It is necessary to select 44 fuel channels (out of 392) for keeping instrumentation to measure flow and temperature of coolant. The reactor is logically divided into 7 radial zones each containing certain number of fuel channels. The selection of instrumented channels is to be made such that power measured by them in terms of per unit basis represents the true zone-wise and global powers fairly accurately. This should be possible for a large number of reactor configurations that can occur because of the movement of reactivity devices in the core. Such a study is useful to make the TPMS more accurate means to measure the reactor bulk power and zone powers. The choice of 44 channels is an optimization problem in which the error in zonal and global power prediction is to be minimized. There are several constraints on the selection of instrumented channels. Therefore, a constrained combinatorial optimization problem has to be solved. An evolutionary technique based on Estimation of Distribution Algorithm (EDA) is used for this purpose. A suitable pattern of 44 instrumented channels is obtained for which errors in zonal and global powers are less than $0.5 \%$ and $2.0 \%$ respectively. The equilibrium state of the core with 357 possible device configurations is considered for the optimization.
(c) 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

This paper is concerned with a monitoring system for Pressurized Heavy Water Reactors (PHWRs). In India, a series of PHWR designs have evolved in course of time. The earliest reactors were of 220 MWe capacity with the slow moderator dump as a shutdown system, which were later indigenized and standardized (Bajaj and Gore, 2006) with two independent fast-acting shutdown systems. Subsequently, two medium-sized 540 MWe PHWRs were constructed. The 700 MWe PHWR is a more advanced mediumsized design (Bhardwaj, 2006) to be commissioned in future. It has several safety features similar to modern CANDU (Canadian Deuterium Uranium) reactors (Vashaee et al., 2008).

The 700 MWe PHWR is a horizontal tube type reactor fueled with Natural Uranium (NU) with heavy water as both coolant and moderator. The coolant is physically separated from the moderator by being contained inside several pressure tubes where it is

[^0]maintained at high temperature and pressure. The moderator heavy water is at a relatively low temperature and is unpressurized. Fig. 1 shows schematically vertical cross-section of the reactor containing the 392 fuel channels. The fuel channels are numbered from 1 to 22 along $X$-axis and $A$ to $W$ along $Y$-axis. Fuel in the form of cluster of 37 element fuel pins and the coolant are contained within these pressure tubes. The direction of coolant flow in adjacent channels (pressure tubes) is opposite to each other. The direction of the bundle movement (fuelling direction) is the same as that of the coolant flow. The fuel is in the form of a string of 12 bundles, each bundle is a 37-pin cluster of 49.5 cm length. There are two independent shutdown systems called Shutdown System-1 (SDS\#1) and Shutdown System-2 (SDS\#2) for reactor protection.

The medium \& large sized PHWRs are neutronically loosely coupled and hence are prone to spatial flux tilts and xenon oscillations. The loose coupling arises due to larger size. The migration length of neutrons is about 20 cm in a PHWR. The typical dimension of the small sized 220 MWe PHWR is about 20-25 migration lengths and is tightly coupled. On the other hand, larger PHWR of size over 30 migration lengths is loosely coupled. Apart from size, loose coupling arises because of radial flux flattening. At the beginning of


[^0]:    ${ }^{a}$ Corresponding author. Tel.: +91 222599 4678; fax: +91 222599 3318.
    E-mail address: smishra@npcil.co.in (S. Mishra).

![img-0.jpeg](img-0.jpeg)

Fig. 1. Reactor core having 392 fuel channels.
life, a PHWR contains all Natural Uranium fuel. After few months, on-line fuelling starts. Every day the burnt fuel from more than one fuel channel is replaced by fresh fuel. This refueling is done in such a way that the central radial zone is fueled less frequently and thus contains more burnt fuel. This flattens the flux shape which enables drawing full power from the reactor. This further decreases the neutronic coupling. Mathematically, the loose coupling manifests itself in terms of reduced separation of first two most dominant K-eigenvalues. In case of 220 MWe PHWR, this separation is about 25 millik while it is less than 15 millik for large PHWRs. The excitation of second K-mode (which amounts to change in flux shape) is easy if its eigenvalue is closer to that of the first.

Such loosely coupled reactors need a sophisticated regulation and protection system. For the purpose of regulation, the core is conceptually divided into 14 spatial zones (Fig. 2). Each zone is equipped with one Zone Control Compartment (ZCC). The light water level in each compartment can be independently changed to control the flux shape. Apart from ZCCs, the reactor is equipped
![img-1.jpeg](img-1.jpeg)

Fig. 2. Reactor core having 14 zones ( 7 front and 7 rear).
with two more regulating devices: There are 17 Adjuster Rods (ARs) symmetrically grouped into 8 banks and 4 Control Rods (CRs) symmetrically grouped into 2 banks (Bhardwaj, 2006). The objective of reactor regulating system is to operate the reactor keeping bundle, channel power within prescribed limit and to keep zonal power close to the design value. Each zone contains a Zone Control Detector (ZCD) to assess the power in that zone. The fuel channels surrounding ZCDs are shown as dark circles in Fig. 1.

The three types of regulating devices mentioned above are operated based on the zone power measured by corresponding ZCD. The ZCDs measure local flux (power) and the power measured by these detectors needs to be corrected so that it represents zonal power. The correction is usually carried out using the power distribution obtained by more accurate systems like on-line flux mapping system (OFMS). In OFMS, there are 102 vanadium self powered neutron detectors (SPNDs). They are well distributed inside the reactor core. With the help of these vanadium detector readings and modal expansion method, detailed flux distribution in side core is obtained by flux mapping algorithm.

In case of unavailability of OFMS (or as an additional measure), the zone power correction is carried out using the Thermal Power Measurement System (TPMS) with which the present paper is concerned. TPMS is an accurate and direct means of obtaining reactor bulk and zonal powers. In the TPMS, some selected fuel channels are equipped with instruments to measure temperature, flow, etc. of that channel which in turn provides the power produced in those channels. These channels are called Instrumented channels (ICs). TPMS determines the reactor bulk power and 7 zonal powers using the power measured by these instrumented channels (ICs). The 7 zones relevant to TPMS are defined using the 14 conceptual zones shown in Fig. 2. This is done by combining zones with same radial location. More specifically,
zone $A=$ zone $1+$ zone8; zone $B=$ zone $2+$ zone9;
zone $\quad C=$ zone $3+$ zone 10 ; zone $\quad D=$ zone $4+$ zone 11 ; zone
$\mathrm{E}=$ zone $5+$ zone 12 ;
zone $\mathrm{F}=$ zone $6+$ zone 13 ; zone $\mathrm{G}=$ zone $7+$ zone 14 ;

In the present paper, hereafter, "zonal power" refers to power in zones A to G defined above. The TPMS is used to compute bulk power as well as the power in these 7 zones from the powers measured in the selected channels (ICs) by using certain formulae which are described in the next sub-section.

### 1.1. TPMS methodology

First of all, a "nominal state" of the reactor is chosen for a reference calculation. In nominal state, the three regulating devices (ZCC, AR \& CR) have certain specified status (to be described later). A detailed whole-core numerical simulation of the nominal state is carried out using neutron diffusion code. In this simulation, the power is normalized to $100 \%$ full power (FP), which is the bulk power. This simulation gives the power in the 7 zones, denoted by $\mathrm{P}_{\mathrm{A}}, \mathrm{P}_{\mathrm{B}}, \ldots, \mathrm{P}_{\mathrm{G}}$. It also gives power in the selected locations for instrumented channels denoted by $\mathrm{p}_{1}, \mathrm{p}_{2}, \ldots, \mathrm{p}_{44}$. (As will be seen later, there are 44 ICs in present studies.) This information is stored for prediction of bulk and zonal powers in various other operating states of reactor.

During operation, the reactor goes through many states that differ from the "nominal state" because of changes in the position of the three regulating devices. These are called off-nominal states. In such a state, the power produced in each of the 44 ICs denoted by $\left(\mathrm{m}_{1}, \mathrm{~m}_{2}, \ldots, \mathrm{~m}_{44}\right)$ are measured. Using them, the bulk and zonal powers are predicted as:
Bulk power $=\{$ Average of $\left(\frac{m_{i}}{p_{i}}\right)$ over all ICs $\} \times\{100 \%$ Full Power $\}$
Power in Zone $A=\{$ Average of $\left(\frac{m_{i}}{p_{i}}\right)$ over all ICs in zone $A\} \times P_{A}$

Similar formula is used for zones B, C, D, E, F and G.
The accuracy of above prediction would depend on the locations of 44 instrumented channels whose power can be measured. The problem studied here is to choose the best possible locations of the ICs which minimize the power prediction errors in all the off-nominal states. There are certain restrictions on the selection of channels for instrumentation. Thus one has to solve a constrained combinatorial optimization problem.

### 1.2. Optimization studies

In order to optimize IC locations, it is necessary to have a capability to evaluate how good is a particular choice of IC locations. For this, it is necessary to numerically simulate any off-nominal state of the reactor. This is done by static K-eigenvalue calculation for that state using neutron diffusion calculation which is described in some detail in Section 1.3. This gives power in all channels including the 44 ICs. These are treated as powers measured in 44 ICs (i.e. $\mathrm{m}_{1}, \mathrm{~m}_{2}, \ldots, \mathrm{~m}_{44}$ ). It also gives the zonal powers. Substituting these powers in ICs in Eqs. (1) and (2), the bulk and zonal powers are found out. They are compared with the actual bulk and zonal powers given by diffusion code to find out the errors. These errors are useful to assess the quality (or fitness) of the particular choice of IC locations. Of course it is necessary to try many possible offnominal states for making the design robust. This will be detailed later.

If the number of possible choices of IC locations were small, one could simply try out all choices, find the prediction errors for each of them and choose the best one. However, 44 channels can be chosen from the 392 channels in very large number of ways despite the
constraints. For such problems, stochastic optimization techniques are suitable. There exist gradient based and simulated annealing methods in which one starts with one specific guess solution (i.e. prescribed IC locations) and gradually makes small random changes to improve it. There are yet other population-based techniques called "evolutionary algorithms" in which one starts with a large number (say, $N$ ) of randomly chosen guess solutions rather than just one solution. Each of these guess solutions (also called individuals) is evaluated to assess its "quality" or "fitness". The solutions with higher fitness are identified (selection) and are used to generate a new set of $N$ solutions (regeneration) that are likely to have better fitness. These two processes of selection and regeneration are continued till a solution of required quality is obtained. There are many types of evolutionary algorithms. In the Genetic Algorithm (GA), regeneration is done by combining two candidate solutions. The GA was inspired by Darwinian evolution based on combination of parental genes. In the present paper, a population based technique called "Estimation of Distribution Algorithm" (EDA) (Jiang et al., 2006) has been used. This technique was earlier used by the authors (Mishra et al., 2009, 2010, 2011) to optimize the distribution of Thorium and Depleted Uranium in a fresh PHWR core. In EDA, certain probability distributions characterizing the selected individuals are identified and the new individuals are generated by sampling from this probability distribution. There are issues such as how much "selective" one should be. They have a bearing on the performance of algorithm and will be discussed later. There are other evolutionary algorithms such as particle swarm optimization (PSO) and ant colony optimization (ACO). A good description of evolutionary algorithms and applications in nuclear engineering can be found in Goldberg (1989), Carter (1997), Michalewicz (1999), Pereira et al. (1999), Pereira and Sacco (2008), Lima et al. (2008) and Meneses et al. (2009).

### 1.3. Reactor simulation

It is clear from Sections 1.1 and 1.2 that a neutronic simulation of full PHWR core in the nominal and off-nominal states is required. The purpose is to find detailed power distribution, in particular power in each channel for any given state of the core. This is done by a two step procedure. The structure containing a fuel channel along with associated moderator, called lattice, is repeated in the reactor core. First of all, a fine energy group transport theory calculation is done over a lattice with all spatial details using a 2-D neutron transport code CLUB (Krishnani, 1992) based on collision probability method to evaluate neutron spectrum. From this, two energy group condensed and homogenized cross-sections of fuel lattice are found. These homogenized cross-sections are used for solving the K-eigenvalue problem using neutron diffusion theory over the full reactor. An inhouse 3-D cartesian geometry diffusion code DOLP is used. This code has been validated against the AECL benchmark (Judd and Rouben, 1981). It has been used for several analyses of Indian PHWRs (e.g. Mishra et al., 2009). In DOLP, the multi-group neutron diffusion equation is discretised by using finite-difference approximation. The K-eigenvalue problem is solved by Power iteration method which in turn involves solution of within-group source problems using inner (Gauss-Seidel) iterations (Duderstadt and Hamilton, 1976).

The paper is organized as follows. Section 2 presents the constraints considered in the selection of fuel channels for TPMS. Section 3 describes the 357 off-nominal reactor core configurations considered during optimization. Section 4 defines the problem. Section 5 describes the method of solution. Section 6 gives numerical results. Section 7 gives conclusion and discussion.

## 2. Constraints in the problem

The two ends of fuel channels (as shown in Fig. 2) are designated as "north" and "south" face of the reactor core. The 392 fuel channels can be logically divided in 4 sets depending on its loop and header of coolant:
(1) Set 1: The fuel channels having coolant flow from north side inlet header to south side outlet header in loop 1
(2) Set 2: The fuel channels having coolant flow from south side inlet header to north side outlet header in loop 1
(3) Set 3: The fuel channels having coolant flow from north side inlet header to south side outlet header in loop 2
(4) Set 4: The fuel channels having coolant flow from south side inlet header to north side outlet header in loop 2

This design of coolant system with two loops is chosen because it reduces the reactivity gain due to void in coolant. As is known, the reduction in coolant density (or voiding) leads to positive reactivity addition in a PHWR and is a safety concern. To reduce the effect of coolant voiding, 700 MWe PHWR consists of two Primary Heat Transport (PHT) loops implied with checkerboard type distribution in the reactor core. There are two inlet and two outlet headers in each loop of the PHT system. The effect of accidental voiding is restricted to only one of the two loops.

The first constraint is that all the four sets of fuel channels contain an equal number of instrumented channels.

Suppose the flux/power increases or decreases at any point due to some cause such as reactivity device movement. The migration length of neutrons is of the order of lattice pitch. Hence, the change in flux propagates up to about 3 migration lengths or 3 pitches. Hence, any given channel whose power/flux is undergoing a change should not be more than 3 lattice pitches away from an instrumented channel. Therefore the selection of IC is made such that nowhere a core of size $4 \times 4$ pitches be left without an instrumented channel. This is the second constraint. This constraint is useful to estimate the total number of ICs needed. Let the 392 fuel channels be divided into $3 \times 3$ pitch regions each containing 9 fuel channels and suppose the central channel in each $3 \times 3$ pitch region is instrumented. Then, distance between 2 IC's would be 3 pitches and fulfill the constraint. Since there can $44(\approx 392 / 9)$ such regions, a minimum of 44 ICs should give adequate coverage of the whole core. Thus 11 ICs in each fuel channel set (as per first constraint) should get instrumented.

The third constraint arises from symmetry. The core has reflective symmetry along the $X$-axis whereas the reactivity devices disturb reflective symmetry along $Y$-axis. The symmetry of ICs about $X$-axis is avoided for better coverage and less redundancy.

There are 14 ZCDs to measure the zone powers. The fourth constraint in the design of TPMS is that each ZCD should be surrounded by minimum of two ICs. The ICs at ZCD nearby location are useful for inter-comparison purpose.

## 3. Core configurations

The choice of nominal and off-nominal core configurations (discussed in Section 1.1) has to be made. First of all, it should be noted that, in present studies, all these configurations have a burnup distribution which is the so-called "equilibrium time-averaged burn-up distribution". This term can be explained as follows. At the beginning of life, the PHWR contains all fresh fuel. This state is unique in its lifetime. After about $4-5$ months, the reactor needs to be fueled continuously. Every day, the burnt fuel from more than one fuel channel is replaced by fresh fuel. The fuelling is done in a planned manner. The fuel channels are divided in to two or
three conceptual radial zones. The average discharge bun-up for each zone is different. Refueling is done less frequently in the central zone. As a result, the central zone contains relatively more burnt fuel than the outer zones, leading to power flattening which enables operation at full power. After a few years, the core reaches an equilibrium state where the fuel feed rate, fuel discharge rate and average in-core burn-up in the core become constant for the rest of the life. In this state, it is possible to compute a "timeaveraged" burn-up distribution at each location. Further details on time-averaged burn-up distribution can be found in CRC Handbook (Bonalumi, 1986). It is this burn-up distribution that has been used in the nominal and off-nominal states of PHWR considered in this paper.

In Nominal state, ZCCs are at 50\%FL (full level), ARs are fully IN and CRs are fully OUT. Power is $100 \%$ Full power.

Off-nominal states differ from nominal state in status of the three regulating devices. The accuracy of TPMS in predicting power is to be checked for off-nominal states. In principle, there are infinite number of possible off-nominal states because, for instance, the light water level in ZCC can vary continuously from $0 \%$ to $100 \%$. We have considered certain discrete levels from $0 \%$ to $100 \%$ and should be adequate. Similarly, some partially inserted states of AR and CR are considered. Extreme accidental situations are not considered because they are not tackled by regulating system. Insertion of shut down devices is also not considered. Only configurations arising in normal operational regime are considered. The configurations with different burn-up distribution are not considered since their effect on power shape is much smaller than that due to regulating device movements. All off-nominal states are analyzed at $100 \%$ FP.

Total 357 reactivity device configurations are considered. The sequential withdrawal of AR banks at different ZCC levels is covered up to case number 124. From case no. 125 to 147, CR insertion cases are covered. From cases 148 to 236, single ZCC drain is represented. Beyond case number 236, least probable configurations such as draining of multiple ZCCs are considered. In the present analysis it is assumed that ICs read the corresponding channel powers.

The reactor bulk power and zone powers are estimated using Eqs. (1) and (2) for all 357 core configurations using powers in ICs (i.e. $\mathrm{m}_{\mathrm{j}}$ ) obtained by diffusion theory code. They are compared with the bulk and zonal powers given by the diffusion code. The predicted reactor bulk power per unit basis measured by ICs should be 1 in ideal case, since all 357 cases are corresponding to $100 \%$ FP. The $\%$ error in zone powers measured by ICs is determined.

## 4. The optimization problem

The optimization problem is defined as follows.
Objective: The error in estimated bulk power should be less than $\pm 0.5 \%$ and that in estimated zone powers should be less than $\pm 2 \%$.

Certain "fitness points" are allotted if the pattern (individual) satisfies the criterion mentioned above.

Constraints: The constraints are as follows:
(1) Total 44 numbers of channels should be selected and thus 11 numbers of channels should be there in each of the four sets of fuel channels.
(2) The channels which have been selected for instrumentation should not be symmetric about $X$-axis.
(3) Nowhere a gap of 4 pitch $\times 4$ pitch or more should be left without a instrumented channel.
(4) Each Zone Control Detector (ZCD) should have minimum two ICs at nearby location.

1. Initialize the population (Size $=\mathrm{N}$ ) randomly but satisfying the constraints described in section 4.
2. Evaluate the fitness of each individual as described in Eq.(3) in section 4.
3. If (maximum fitness.eq. 3570 ) terminate, else continue
4. Select $\mathrm{M}<\mathrm{N}$ candidates based on termination selection method (the best fit M individuals among total N individuals).
5. Calculate Probability Distribution Function (PDF) using selected M individuals. At any generation (t) the PDF has been estimated as given below for each location.

$$
P D F(t+1)=P D F(t) \cdot(1-\alpha)+\alpha \cdot \frac{1}{M} \sum_{m=1}^{M} X_{m}(t)
$$

Where $\alpha$ is constant between $[0,1] . \mathrm{X}$ is binary representation of Instrumented/Noninstrumented fuel channels. The PDF at ZCDs nearby locations is kept 0.9 always.
6. Generate new population (Size $=\mathrm{N}$ ) using this new probability distribution function (PDF) such that each individual satisfies the constraints.
7. The fitness of new N individuals is found out as in step 2 .
8. Go to step 3 .

Fig. 3. Pseudo EDA model used for optimization.

Here, the objective function to be maximized has been defined as follows:
Fitness $=\sum_{c \text { one }=1}^{357}(\mathrm{F} 0+\mathrm{F} 1+\mathrm{F} 2+\mathrm{F} 3+\mathrm{F} 4+\mathrm{F} 5+\mathrm{F} 6+\mathrm{F} 7)$
where summation is carried out over all 357 configurations and the terms are as follows:
$\mathrm{F} 0=3$, if the estimated bulk power $(\mathrm{P})$ is above $99.5 \% \mathrm{FP}$ and less than $100.5 \% \mathrm{FP}$, and zero otherwise (in fraction the condition means, $0.995<\mathrm{P}<1.005 ; \mathrm{P}$ is fractional full power)
$\mathrm{F} 1=1$, if error in zone A power is less than $\pm 2 \%$ and zero otherwise $\mathrm{F} 2=1$, if error in zone B power is less than $\pm 2 \%$ and zero otherwise $\mathrm{F} 3=1$, if error in zone C power is less than $\pm 2 \%$ and zero otherwise $\mathrm{F} 4=1$, if error in zone D power is less than $\pm 2 \%$ and zero otherwise $\mathrm{F} 5=1$, if error in zone E power is less than $\pm 2 \%$ and zero otherwise $\mathrm{F} 6=1$, if error in zone F power is less than $\pm 2 \%$ and zero otherwise $\mathrm{F} 7=1$, if error in zone G power is less than $\pm 2 \%$ and zero otherwise

The above fitness points are chosen by some intuitive thinking and need not be the best choice. Fitness points for predicting zonal power is chosen to be 1 for each zone since all zones are equally important. Higher points (=3) are chosen for bulk power prediction since it implies error in zone powers also.

The objective function (also called fitness function) given by Eq. (3) has to be evaluated to determine the fitness of any given set of selected channels. It can be seen from Eq. (3) that if all the errors are within specified limit for a power distribution the pattern (individual) is rewarded 10 points. There are total 357 power distributions and thus a suitable individual will acquire maximum 3570 points.

## 5. Estimation of Distribution Algorithm (EDA)

As mentioned in Section 1, EDA is a population based evolutionary algorithm. The two operators in EDA are estimation of probability distribution and sampling. In each generation, $N$ individuals (choices of 44 ICs) are generated by sampling certain probability distribution. They are generated (during initial and subsequent generations) in such a way that first three constraints are satisfied. The fitness is evaluated for each of them as described by Eq. (3) and the best $M(<N)$ individuals are selected to estimate probability distribution. Here $N$ is chosen as 200 and $M$ as 50 . The probability that a given fuel channel will get selected for instrumentation or not is estimated from the selected $M$ individuals. This probability is found for each of the 392 channels as follows. As an example, consider the channel number 1. Out of the $M$ configurations, suppose I configurations have channel 1 as an instrumented
channel. Then, the probability of being instrumented is $1 / M$ for the first generation. For sampling in any other generation, a weighted mean of probabilities in current and earlier generation is chosen. The weighting is governed by a factor $\alpha$ in Fig. 3.

As an exception, the channels adjacent to ZCDs are treated in a quite different way. The selection probabilities of the fuel channels which are adjacent to the ZCDs (as shown by dark circles in Fig. 1) are kept 0.9 always. This takes care of the fourth constraint. The reason is that with such a high probability, the channels adjacent to ZCDs are frequently chosen during sampling as needed by the fourth constraint. The authors do not know whether this is the best procedure. If the fourth constraint is treated like the first three, very large number of trial configurations have to be generated. Yet another alternative way to treat constraint four could be to use high penalty (by adding a term in Eq. (3)) for those configurations which do not satisfy the fourth constraint.

The Probability Distribution Function (PDF) was generated using $25 \%$ dominated individuals [item 4 in Fig 3] of the population size (i.e. $M / N=50 / 200=25 \%$ ). Alpha is chosen as 0.1 . In general, if $M / N$ is reduced or $\alpha$ is increased, selection pressure increases and the algorithm converges faster (in fewer generations), but the final result can be inferior due to insufficient exploration. On the other hand, if selection pressure is low, convergence is poor but final result can be superior. The specific choices in this paper were made based on our earlier experience in using EDA and seem to work well here. A parametric study with different choices of $M / N$ and $\alpha$ has not been done.

The performance of an EDA highly depends on how well it estimates and samples the probability distribution. Univariate Marginal Distribution Algorithm (UMDA) assumes no interaction among variables. The probability distribution is estimated using UMDA (Jiang et al., 2006; Mishra et al., 2009, 2010, 2011) in the present case. A pseudo model of the algorithm used for optimization is given in Fig. 3. The execution of the program is terminated either after completion of generation number 10,000 or when fitness 3570 is obtained.

## 6. Results

The evolution of fitness with generation number is shown in Fig. 4. After 3493 generations the maximum fit individual acquires 3570 points.

The best choice of instrumented channels is shown in Fig. 5. The fuel channels numbered as " 1 " are not instrumented whereas, the fuel channels numbered as " 2 " are instrumented. The pattern satisfies all the constraints. There are 11 fuel channels in each set. The selected channels are not symmetric about $X$-axis and nowhere

![img-4.jpeg](img-4.jpeg)

Fig. 4. Evolution of maximum and average fitness.
a gap of $4 \times 4$ pitches or more are left without an instrumented channel.

The reactor bulk power estimated using the best IC location channels for all 357 cases is shown in Fig. 6. The bulk power estimated by instrumented channels lies between 0.995 and 1.005 . Thus error in bulk power is less than $\pm 0.5 \%$.

The %error in zone power estimation is shown in Fig. 7 for all 7 zones and in all 357 cases. The \%error in estimating reactor zone power lies between $-2 \%$ and $2 \%$.

## 7. Conclusion and discussion

The problem of choosing 44 fuel channels (from amongst 392 fuel channels) which can predict reactor bulk power and zone powers accurately is solved using Estimation of Distribution Algorithm. The selected channels for instrumentation are also satisfying all the 4 imposed constraints. The pattern (i.e. selected channels) also exhibits some expected properties. The instrumented channels are distributed equally in both halves of the core (i.e. about $X$-axis and
![img-5.jpeg](img-5.jpeg)

Fig. 5. Reactor fuel channels (1: non-instrumented; 2: Instrumented).
![img-4.jpeg](img-4.jpeg)

Fig. 6. Reactor total power (fractional full power) estimated by instrumented channels for various core configurations.
about $Y$-axis). There are 7 instrumented channels each in Zone A, Zone B, Zone F and Zone G, which are symmetrically located. Zone C and Zone E have 6 instrumented channels each. The central Zone D has 4 instrumented channels.

It may be mentioned that earlier an effort had been made to design TPMS by manual trials and intuition. The design so obtained gave the errors in estimated reactor bulk and zone powers for various reactivity configurations of about $\pm 2.3 \%$ and $\pm 5.7 \%$ respectively. In the present studies, the aim was to obtain a better design with zonal power error less than $\pm 2.0 \%$ and bulk power error less than $\pm 0.5 \%$. It has been successfully obtained by the EDA algorithm. In the final generation, about 4 or 5 distributions of ICs were obtained which have almost same accuracy in power prediction. Amongst them, the distribution which provides maximum number of ICs near the ZCDs was considered to be the best choice and has been explicitly displayed in Fig. 5.

It would be interesting to consider the objective of further reducing the power prediction errors as far as possible. This may
![img-5.jpeg](img-5.jpeg)

Fig. 7. \% Error in zonal power estimated by instrumented channels for various core configurations.

possibly provide an even better pattern of ICs. It is also possible to vary various parameters in EDA algorithm such as $N, M, \alpha$ for better results. One can also try other evolutionary algorithms to solve the problem. The problem can also be treated as a multi-objective optimization problem.

## Acknowledgements

The authors are highly thankful to Shri. A.N. Kumar, Head, RP \& S and Smt. S. Ray, ACE, NPCIL for useful discussions and support.

## References

Bajaj, S.S., Gore, A.R., 2006. The Indian PHWR. Nucl. Eng. Des. 236, 701-722.
Bhardwaj, S.A., 2006. The future 700 MWe pressurized heavy water reactor. Nucl. Eng. Des. 236, 861-871.
Bonalumi, R.A., 1986. In: Ronen, Y. (Ed.), CRC Handbook of Nuclear Reactors Calculations, vol. II. CRC Press.
Carter, J.N., 1997. Genetic algorithm for incore fuel management and other recent developments in optimization. Adv. Nucl. Sci. Technol. 25, 113-149.
Duderstadt, J.J., Hamilton, L.J., 1976. Nuclear Reactor Analysis. Wiley, New York.
Goldberg, D.E., 1989. Genetic Algorithms in Search, Optimization and Machine Learning. Addison-Wesley, Reading, NY.
Jiang, S., Ziver, A.K., Carter, J.N., Pain, C.C., Goddard, A.J.H., Franklin, S., Phillips, H.J., 2006. Estimation of distribution algorithms for nuclear reactor fuel management optimization. Ann. Nucl. Energy 33, 1039-1057.
Judd, R.A., Rouben, B., 1981. Three dimensional kinetics benchmark problem in a heavy water reactor. Report No. AECL-7236.
Krishnani, P.D., 1992. CLUB - A multi-group integral transport code for Lattice calculations of PHWR cells. Report BARC/1992/E/017.
Lima, D., et al., 2008. A nuclear reactor core fuel reload optimisation using artificial ant colony connective networks. Ann. Nucl. Energy 35, 1606-1612.
Meneses, A.A.M., et al., 2009. Particle swarm optimisation applied to nuclear reload problem of a PWR. Prog. Nucl. Energy 51, 319-326.
Michalewicz, Z., 1999. Genetic Algorithms + Data Structures = Evolution Programs. Springer.
Mishra, S., Modak, R.S., Ganesan, S., 2009. Optimization of thorium loading in fresh core of Indian PHWR by evolutionary algorithms. Ann. Nucl. Energy 36, $948-955$.

Mishra, S., Modak, R.S., Ganesan, S., 2010. Optimization of depleted uranium bundle loading in fresh core of Indian PHWR by evolutionary algorithms. Ann. Nucl. Energy 37, 208-217.
Mishra, S., Modak, R.S., Ganesan, S., 2011. Optimization of depleted uranium loading in fresh core of large sized Indian PHWR by evolutionary algorithms. Ann. Nucl. Energy 38, 905-909.
Pereira, C.M.N.A., Schirru, R., Martinez, A.S., 1999. Basic investigations related to genetic algorithm in core designs. Ann. Nucl. Energy 26, 173-193.
Pereira, C.M.N.A., Sacco, W.F., 2008. A parallel genetic algorithm with niching technique applied to a nuclear reactor core design optimization problem. Prog. Nucl. Energy 50, 740-746.
Vashaee, D., Tayebi, L., Luxat, J., 2008. Reference model parameter identification of space-time dependent reactivity in a CANDU-PHWR. Ann. Nucl. Energy 35, $228-237$.

Shri Surendra Mishra, after acquiring M.Sc. degree in Physics from D.D.U. Gorakhpur University, India: joined Nuclear Power Corporation of India Limited in 2003 as Scientific Officer. He is involved in reactor physics calculation like determining fresh core fuel loading pattern, criticality calculation of power reactors, fuel bunrup optimization and design of reactor regulation and protection systems for Indian PHWR. He has 4 publications in International Journals.

Dr. R.S. Modak joined Bhabha Atomic Research Center, India; in 1978 as Scientific Officer after completing a one year orientation course. He has obtained Ph.D. in Physics from University of Mumbai. His main fields of interest have been Nuclear Reactor Physics and Computational methods. He has contributed to the development of many efficient computational schemes and computer codes for the solution of static and time-dependent neutron diffusion and transport problems. Recently he has also been working on optimization problems in Nuclear Reactors. He has published about 20 papers in peer-reviewed International Journals.

Prof. S. Ganesan is the Head of Nuclear Data Section in the Reactor Physics Division in BARC. He was Associate Fellow of International Center for Theoretical Physics, Trieste, Italy (1988-1993). He was Head, Nuclear Data Section at IGCAR, Kalpakkam until 1990. He served as a Nuclear Physicist in the International Atomic Energy Agency during 1990-1994 when he led the efforts to create the successful Fusion Evaluated Nuclear data Library, FENDL, tailored to ITER applications. He has been involved in the successful creation and implementation of the WIM5D nuclear data library update project, international criticality safety benchmark evaluation project (ICSBEP) of the US-DOE/NEADB and EXFOR activities of International Nuclear Reaction Data Center (NRDC) network. He involved in the creation of Nuclear Data Physics Center of India (NDPCI). Currently, he is involved in critical assessment of benchmark validations of thorium fuel cycle and in neutron time of flight experiments and analysis including in BARC's participation in the CERN TOF collaboration.