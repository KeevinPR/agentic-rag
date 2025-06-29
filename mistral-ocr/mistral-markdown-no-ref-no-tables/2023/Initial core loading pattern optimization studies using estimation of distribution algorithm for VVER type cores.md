# Initial core loading pattern optimization studies using estimation of distribution algorithm for VVER type cores 

Amit Thakur ${ }^{\mathrm{a}, *}$, Argala Srivastava ${ }^{\mathrm{a}}$, Vaibhav Kumar ${ }^{\mathrm{b}}$, Kislay Bhatt ${ }^{\mathrm{b}}$, Vibhuti Duggal ${ }^{\mathrm{b}}$, K. Rajesh ${ }^{\text {b }}$, Umasankari Kannan ${ }^{\mathrm{a}}$<br>${ }^{a}$ Reactor Physics Design Division, Bhabha Atomic Research Centre, Mumbai 400085, India<br>${ }^{\mathrm{b}}$ Computer Division, Bhabha Atomic Research Centre, Mumbai 400085, India


#### Abstract

Innovative fuel management schemes based on evolutionary algorithms (EAs) now form an integral part of design and operation for nuclear reactors. In the present study, Estimation of Distribution Algorithm (EDA) has been developed for light water reactors (LWRs) and as a case study EDA has been applied to optimize the core loading pattern of VVER X2 benchmark's initial core. EDA belongs to class of EAs where the optimization solution evolves through progress of generations and in each generation sampling of best candidates of previous generation is done. The main objectives of this study is firstly to develop and test EDA to optimize core loading pattern (LP) for VVER type cores and secondly to generate new optimized LPs having same safety features but with improved fuel utilization with respect to reference benchmark case. The most suitable values for internal parameters for EDA like population size ( N ), percentage best candidates ( M ) and weighting factor ' $a$ ' were evaluated for reaching a reasonable optimized solution in computationally efficient way. During this study, a number of optimized initial core loading patterns were generated, where the target parameters and safety limits are met. A comprehensive analysis for selected LPs has been carried out for full cycle and a comparison has been done for the reported safety and operational characteristics. It is observed that a few of the optimized LPs have better fuel economy than the benchmark LP.


## 1. Introduction

The efficient fuel management during all phases (initial, transition and equilibrium) ensures continuous, safe and economic operation of nuclear reactor. The main objective is to achieve a reasonably flat flux distribution so that full power operation is maintained along with safety limits. However, the leakage of neutrons also needs to be optimized so that maximum energy/burnup can be extracted from the core. Therefore, the efficient fuel management is a complex combinatorial optimization problem, where at each phase of reactor operation, loading pattern (LP) needs to be optimized. In equilibrium phase, LP is optimized considering a desired number of burnt fuel assemblies (FAs) to be replaced by fresh FAs along with reshufflings of partially burnt FAs at all lattice locations. In case of typical light water reactors (LWRs), one third of core FAs are discharged after a stipulated time of operation ( 12 months to 24 months). The flat flux distribution is reached by maintaining a proper burn-up and poison distributions. In case of initial core, all the assemblies are fresh, therefore, FAs with different enrichments are designed specifically for a flat flux distribution. In both initial and equilibrium phases, earlier times heuristics based approach was used (Galperin and Nissan, 1988; Galperin et al., 1989; Balakrishnan and Kakodkar, 1994). This approach was successful to solve these problems
but the optimized solutions are not one of the best LPs due to limitation of these methods that they can explore only limited cases of the vast search space. With enhancement of computational power and development of new methods and evolutionary algorithms like Genetic algorithm (GA)(Goldberg, 1989; Parks, 1996; Chapot et al., 1999), Estimation of Distribution Algorithm (EDA) (Jiang et al., 2006), Simulated annealing (SA) (Stevens et al., 1995), Ant Colony Algorithm (ACO) (Machado and Schirru, 2002) and Artificial Neural Networks (Kim et al., 1993, Ziver et al., 2004, Sadighi et al., 2002), the entire area of search space can be thoroughly explored in reasonable time and better optimized solutions can be generated for both initial and equilibrium phase.

Use of EAs has been quite common for PWR LPO problems (Wojciech et al., 2021, So et al., 2021, Guler et al., 2004, Nazari et al., 2013). GA has also been used for reaching the equilibrium cycle in PWRs (Rodrigues et al., 2022). For BN type fast reactors use of GA has also been described (Sobolev et al., 2017), and the efficiency of these methods for VVER type reactors has also been discussed. However, limited data has been presented (Sobolev et al., 2017). In another study, VVER 1000 initial core has been optimized using GA (Rafiei et al., 2013) and the results are described as a case for a probable benchmark (BM) and future reference for other researchers for comparison considering different evolutionary algorithms (EAs).

[^0]
[^0]:    a Corresponding author.

    E-mail address: thakur@barc.gov.in (A. Thakur).

Estimation of distribution Algorithm (EDA) (Jiang et al., 2006) has been applied successfully to CONSORT research reactor where five different types of fuels are to be loaded in 24 locations with the objective of maximization of K-effective. EDA has also been used for optimization of initial loading pattern of Advanced Heavy Water Reactor (AHWR) (Thakur et al., 2016). The initial core loading optimization of Pressurized heavy water reactors (PHWRs) has been successfully carried out (Mishra et. al., 2009) using EDA. The objective function in all these studies has been selected using penalty method (Mishra et al., 2009) where, maximizing k-effective is main objective and any loading pattern not meeting design limit will be de-prioritized by penalizing the objective function. Initial core for some VVER benchmarks like VVER 1000 MOX benchmark has been optimized using SA and GA (Tran et al., 2021; Rafiei et al., 2013). Loading pattern has been optimized for VVER MOX benchmark (NEA, 2005) using evolutionary simulated annealing (Tran et al., 2021). However, in literature search, studies related of VVER type cores aiming for a better initial core LP using EDA could not be found.

In the present studies, an attempt is made to optimize the initial core LP of VVER X2 Benchmark (Lótsch et al., 2012) using EDA (Jiang et al., 2006) which give similar performance as reported benchmark. The VVER X2 benchmark proposed during 19th\& 20th AER symposium is based on the of the second unit of the Khmelnitsky Nuclear Power Plant (NPP) VVER-1000 Ukraine. The benchmark specifies a set of the core LPs with different types of FAs and burn up cycles from initial phase to equilibrium phase. Initial core of the benchmark has 163 fuel locations with 5 fuel types. So, there are total of $5^{163}$ different core loadings possible. Using $1 / 6$ th core symmetry, the problem size can be reduced to $5^{28}$ or ( $3.7 \times 10^{19}$ ). For simulation of a single core configuration, it takes $\sim 3 \mathrm{~min}$ of computational time in present day computer. Therefore, simulation of all possible combinations is not a practical option to choose the best one in a reasonable time frame which gives a strong motivation to use modern population based evolutionary algorithm like EDA to arrive at the best/near best possible LP in realistic time.

The aim of the present study is to apply the EDA to VVER core loading and to suggest alternate initial core considering same FAs and same/similar Boron content, k-effective, radial peaking and axial peaking factor but having better cycle length and/or fissile inventory. In other words, the new optimized initial core will have same or similar safety features but better fuel utilization. A detailed fuel cycle analysis of optimized LPs has been carried out and is compared with benchmark operational burn-up data. This way a better LP will be guaranteed as the comparison for EOC has also been done. In our studies, other interesting outcomes were observed like; there is a possibility of reducing number of enrichments in initial core of VVER.

The paper has been organized as following. Section 2 describes the VVER X2 initial core and the problem size for initial core LP. The development of EDA has been described in section 3. Here, the objective function used is also illustrated. Further a study to optimize internal parameters for EDA has been described. Section 4 discusses the results of optimization of internal parameters of EDA. In section 5, fuel cycle studies for prominent optimized LPs is given. The conclusion and scope for future studies has been given in Section 6.

## 2. VVER X2 benchmark: Initial core

Comprehensive operational data such as cycle length, boron concentration in the coolant, power density distributions, measured reactivity coefficients and description of several operational transients has also been provided in VVER X2 benchmark (Lotsch et al., 2012).

Table 1 lists some salient features of the VVER 1000 X2 core. The reactor is a 1000 MWe and its core has 163 FAs. There are five different types of fuel assemblies in initial core having different enrichment and the Gd content in the fuel. While, reaching equilibrium core a total of 8 different types of fuel assemblies are used. The hexagonal fuel assemblies have a pin pitch of 1.275 cms and there are 331 pin locations in one hexagonal lattice. Out of these 331, fuel pins take 312 locations and 18

Table 1
VVER 1000 X2 Core salient details (Lótsch et al., 2012).
locations are Zr guide tubes which are filled by either light water coolant or Control and Protection System Absorber Rod (CPSAR) or Burnable absorber rods (BARs) depending on the reactor state and fuel cycle. The central location acts as the spacer capture rod for the FA. The Boron concentration in coolant can vary from 0 to 3000 ppm . The radius of fuel pins is 0.386 cm and the ID and OD of $\mathrm{Zr}-\mathrm{Nb}$ clad is 0.772 \& 0.910 cm respectively. Table 2 provides the fuel assembly data. As our study involves only initial phase of reactor, the description of initial core FAs (5 types only) has been provided in Table 3. It can be observed that the

Table 2
Basic Design Data of the fuel assemblies and their components (Lótsch et al., 2012).

Table 3
Description of composition of the FA types used for initial core (Lötsch et al., 2012).
fissile content increases from $1.3 \%$ to $3.9 \%$ as we go from type 1 to type 5. The type $4 \& 5$ are used in equilibrium fuel cycle also but the type 1 to type 3 (with lower enrichment) is specially designed to be used in initial phase of VVER. The uniform axial enrichment has been considered for all types as specified in benchmark. The first two fuel types (type1\&2 or13AU \& 22AU) have enrichment of $1.3 \%$ and $2.2 \%$ respectively in 312 fuel pins as shown in Fig. 1\&2.Fig. 2 The third fuel type (type-3 or 30AV5) has 303 fuel pins of enrichment of $3 \%$ and 9burnable absorber (BA) pins with different enrichment at different locations as shown in Fig. 3. Type 4 (39AWU) FA has 243 fuel pins with $4 \%$ enrichment and 60 pins have $3.6 \%$ enrichment. It also has 9 BA pins with different enrichment and Gd content at different location as shown in Fig. 4. Type 5 (390GO FA) has enrichment of 240 pins with enrichment of $4 \%$ and 66 pins have enrichment of $3.6 \%$ as shown in Fig. 5. Here, 6 BA pins with different gadolinium content and enrichment are placed at different location as shown in Fig. 5.

The initial core loading pattern used in benchmark using these five FAs has been given in Fig. 6. It is to be noted that this pattern has 48,42 , $37,24 \& 12$ FAs for type $1,2,3,4 \& 5$ respectively. Simulation and modeling of the hexagonal FAs are done with lattice code EXCEL (Jagannathan \& Jain, 2009). The core 3D diffusion solver for hexagonal lattices code TRIHEXFA (Jagannathan, 2009; Thilagam, 2019) has been used to study the core characteristics of the initial core. The reference
![img-0.jpeg](img-0.jpeg)

Fuel with Enrichment 1.3\%
Central Guide Tube
Guide Tube
Fig. 1. Pin Layout of fuel assembly type 13AU (Type-1).
![img-1.jpeg](img-1.jpeg)

Fig. 2. Pin Layout of fuel assembly type 22AU (Type-2).
![img-2.jpeg](img-2.jpeg)

Fig. 3. Pin Layout of fuel assembly type 30AV5 (Type-3).
benchmark has been analyzed in details (Srivastava Argala et al., 2022). The critical boron, K-effective and operational parameters like radial peaking factor (RPF), triangular peaking factor (TPF and axial peaking

![img-3.jpeg](img-3.jpeg)

Fig. 4. Pin Layout of fuel assembly type 39AWU (Type-4).
factor etc.) are found to be in excellent agreement with the benchmark values (Srivastava Argala et al., 2022). The initial fissile inventory is estimated to be 3297 Kgs . Core burn-up studies of the initial core indicated the cycle length of 330 FPDs. (Argala et al., 2022). TRIHEXFA code is used to simulate the benchmark case of VVER 1000 X2 core as well as for LPs generated in while optimizing the core using EDA.

## 3. Methodology: EDA for VVER loading pattern optimization (LPO)

In case of any optimization study using EAs, the first step is to define objective function. Following objectives are considered in evolving new LP:

1. K-effective should have target values as given in benchmark loading pattern
2. The radial peaking factor should be lower than benchmark LP
3. The triangular peaking factor should be lower than benchmark LP

To achieve higher cycle length (greater than 330 FPDs), a slightly higher target k -effective value of 1.005 has been chosen to keep some margin. If the initial fissile inventory of any optimized LP for this keffective value (1.005) is lower than the benchmark value ( 3256 Kg ), a better fuel utilization is expected. The main aim is to look for LPs to get equal or better performance than benchmark values. The radial peaking factor is defined as the maximum value of ratio of power of each assembly to average value of power. It was observed that the design limit on radial peaking factor (RPF) for VVER type cores is 1.5 , therefore, the same has been chosen as target value. Each hexagon has been further subdivided into 24 triangles for simulation. The ratio of maximum triangular power to overall average of triangular power is defined as triangular peaking factor. The target value for triangular peaking factor has been chosen as 2.32 on the basis of the design limit.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Pin Layout of fuel assembly type 390GO (Type-5).
![img-5.jpeg](img-5.jpeg)

Fig. 6. Core Layout of the Initial core of VVER X2 Benchmark.
The objective function (OF) for this problem is defined using penalty method (Mishra et al., 2009; Thakur et al., 2016) as given in Eq. (1). Since it is a multi-objective problem, multiple parameters like k-effective, radial peaking factor (RPF), triangular peaking factor (TPF), axial offsets, power distribution, buckling, worth of control system/ shut down system and flatness of flux etc. can be used to define OF. However, it was the first attempt towards LP optimization of VVER cores and for estimating all these may require multiple simulations for one LP. Therefore, to reduce the computational effort, only three parameters (keffective, radial peaking factor (RPF) and triangular peaking factor (TPF)) are considered for defining OF.

$O F=A_{1} K f a c t o r-A_{2}(R P F-1.5)-A_{1}(T P F-2.32)$
where $A_{1}, A_{2}$ and $A_{3}$ are constants. The values of these constants are based on experience and requirements. Initially few numerical experiments have been carried out to find out the appropriate values of these parameters (Thakur et al., 2016, Jiang et al., 2006). In these numerical experiments, values of A2 \& A3 has been varied from 0.05 to 0.4 while keeping A1 as 1 . The various cases studied were then compared with respect to computational effort and properties of optimized pattern.

Further, if k-effective of a LP is $<1.005$, then Kfactor $=$ keffective.
Else, Kfactor $=1.005-$ keffective.
if Radial peaking factor (RPF) of a LP is $<1.5$, then $\mathrm{A}_{2}=0$, else $\mathrm{A}_{2}=$ 0.15 .

Similarly, if triangular peaking factor (TPF) $<2.32$, then $\mathrm{A}_{3}=0$, else $\mathrm{A}_{3}=0.15$.

It is to be noted that choosing the OF in this way will not give any preference to LP having RPF and TPF less than target values. Penalty is imposed only when these parameters do not meet target value. The criteria are to maximize the K-effective to target value of 1.005 without compromising full power operation and safety of reactor.

After defining OF, the working of EDA has been described next. EDA belongs to class of EAs which are population based algorithms, similar to GA. Here, in each generation sampling of solutions is done based on best solutions of previous generation and the probability distribution model is updated. A random uniform probability distribution is considered to generate initial pool of solution candidates. The objective function for all candidate loading patterns of this pool is evaluated using parameters generated by TRIHEXFA code. In next step the few best solutions of the pool are used to modify the probability distribution function. In short, the working of EDA can be defined in following steps: -

Step-1 Initial distribution function is used to generate a pool of N loading patterns. Here, ' N ' is population in one generation. In the present study three different cases having studied where N is taken as 120, $240 \& 600$.

Step-2 All the candidate LPs are simulated using TRIHEXFA code and OF is evaluated.

Step-3 Top M (a predetermined percentage of N having highest OF values) candidates are chosen.

In present study, $M$ is considered as $10 \& 20 \%$ of $N$.
Step-4 The modification of distribution function (DF) (Baluja, 1994) is carried out using following equation
$D F(t+1)=D F(t)(1-\alpha)+\alpha X$
where, ' $\alpha$ ' (weighing factor) is a constant and its value is between 0 and 1. DF (t) and $X$ are having same structure. ' $t$ ' represents the generation number.

Where $X=\frac{1}{M} \sum_{i=1}^{M} X_{i}(t)$.
$X_{i}(t)$ is 0 or 1 based on the loading of a particular fuel in fuel lattice location.

Step-6 Modified DF is used to generate the population of different loading patterns in next generation.

Step-7 Go to step-2 and cycle is repeated till desired number of generation or the optimized LP is achieved.

In our present study, a uniform initial distribution function is considered. As we have 5 different fuel assemblies and 28 fuel locations. Therefore, initial probability for any fuel type at any location has been considered as 0.2 . Now, consider 1st location (out of 28 locations), at 1st generation, equal probabilities for 5 fuel types are given. So, if the random number generated has a value between $0 \& 0.2$, type 1 fuel will be loaded. If it is between $0.2 \& 0.4$, then type 2 fuel will be loaded and so on. For each location, 1 random number will be generated. And the value of random number will decide the loading of a particular type of fuel (type-1, 2, 3, 4 or 5) at that location. Same process is repeated for each location to generate one LP. And a population of LPs is generated for every generation. In each generation, top best LPs based on their OF
values are selected and these windows of $0,0.2,0.4,0.6,0.8 \& 1.0$ are modified based on selected LPs. For example, if the top best LPs have maximum number of fuel type 5 in location 1, then the window for type 5 will increase from 0.2 while for other types (1-4) will adjust such that total is 1 . The value of ' $a$ ' \& ' $M$ ' will decide the quantum of change. In the end of all generations, if type-5 is best suitable for location 1, then the window will be modified as $0.0,0.0,0.0,0.0 \& 1.0$.

## 4. Results of EDA for VVER 1000 X2 initial core loading pattern optimization

A computer program using fortran 90 has been developed for optimization of VVER using EDA. The ANUPAM-ATULYA distributed memory parallel computer system at BARC was used for parallelization and computation. Atulya Supercomputer is the latest in ANUPAM series of BARC's Supercomputers, which is running at 2 PFLOPs peak performance. Architecture wise, the Atulya Supercomputer falls under Distributed Memory Parallel Architecture, wherein, 368 numbers of high-end Compute Nodes are connected together through a high-speed HDR 100Gbps Infiniband based Interconnect. Each Compute Node is equipped with 40 Nos. of x86_64 CPU cores and 384 GBs of RAM. In each generation of EDA, different VVER initial core LPs are generated and 3D diffusion simulations for all these patterns are carried out parallelly on ANUPAM using TRIHEXFA code. It is to be noted that EDA has three important internal parameters (Thakur et al., 2016, Jiang et al., 2006) which are given below:
a) Population size in each generation (N)
b) Percent of best solution chosen for updating DF (M)
c) Weighting Factor ' $a$ '. This provides the percentage of solutions which will be updated based on best candidate LPs of previous generation.

The value of $\mathrm{N}, \mathrm{M}$ and $\alpha$ has been different for different problems. And it is usually required to do a few simulations to evaluate the best values of these parameters. Therefore, the study has been started first for optimizing initial parameters for EDA.

Initially, based on literature review (Jiang et al., 2006, Mishra et al., 2009), small value of $\alpha=0.05$ has been chosen. The value of N was considered to be 120 and M is fixed as $20 \%$ of N. However, it was observed that even after 300 generations the convergence was not achieved. And there appears to scope of better optimized LP. It is to be noted that the DF matrix will be modified with each generation. If the DF matrix reaches a state, where, for all fuel locations, one element out of 5 reaches a value of 1 then all the LPs generated will be same. Therefore, there will not be any benefit in going for more generations as no new LPs will generated and the same is defined as meaning convergence. Therefore, higher population size of 240 and 600 were chosen. But if computations are done for same number of generations (300), the number of simulations become very high. For example, in case of $\mathrm{N}=$ 120 and total generations considered is 300 this means total number of simulations is $36,000(120 \times 300)$. However, for $\mathrm{N}=240$ or 600 , for same number of generations will require $72,000 \& 180,000$ simulations. Therefore, cases for $\mathrm{N}=240$ and 600 have been restricted to lesser generations of $\sim 150$ and 100 respectively. For understanding the performance of EDA with these parameters, the average value of best 15 candidates of each generation is plotted in Fig. 7. It is to be noted that usually, multiple simulations for same case are done and average value of the best one among all these multiple solutions is plotted. However, to reduce simulations, we have avoided multiple simulations for same case. But instead of best solution, we have considered the average of best 15 solutions in each generation. This has resulted in providing a good picture of performance of algorithm without requirement of multiple runs for same case. It can be observed that, the smaller value of $\alpha$ makes the algorithm search in different areas of search space (more diverse search). But it makes the algorithm slow to reach for a converged value. As $\mathrm{N}=240 \& 600$ cases have been done with lesser number of

![img-6.jpeg](img-6.jpeg)

Fig. 7. OF Vs Generation number for case I, I-a \& I-b ( $\mathrm{N}=120$, alpha $=0.05$, $\mathrm{M}=20 \%$ ).
generations than $\mathrm{N}=120$, therefore, the objective function has not reached near to the optimum solution for these cases. However, $\mathrm{N}=120$ case has increased to higher value of objective function slowly and for more number of generations. The best value of OF observed during all simulations is 1.0049 and the observed LP has RPF and TPF within the designated limits. The k-effective value for this LP is 1.00495 . The RPF and TPF for best LP achieved for $\mathrm{N}=240 \& 600$ cases does not meet their design limit and hence are not discussed in text any further. It is interesting to note from the inset of Fig. 7, that the case with $\mathrm{N}=120$, in initial generations ( $\sim 100$ ) OF has a lower value than that of case with N $=240 \& 600$. This is because, $\mathrm{N}=240 \& 600$ more area of search space is explored in each generation. Therefore, for achieving a better optimized LP with $\mathrm{N}=240$ and 600 and $\alpha=0.05$, large number of generations are needed and hence it involves significantly higher computational effort.

In order to search for better optimized solution and without enhancing computational effort, two more cases with $\alpha=0.15 \& 0.5$ have been analyzed. These cases have been studied for all three values of N (120, $240 \& 600$ ). The average value of best 15 candidates of each generation for case with $\alpha=0.15$ has been plotted in Fig. 8 and for case
![img-7.jpeg](img-7.jpeg)

Fig. 8. OF Vs Generation number for case II,III \& IV.
with $\alpha=0.50$ has been plotted in Fig. 9. Here also, $\mathrm{N}=120,240 \& 600$ cases have been studied up to 300, 150 and 100 generations respectively. It may be noted by increasing value of $\alpha$, the performance of EDA will be accelerated. This is because; the algorithm will search more solutions near to the area where best solutions of previous generations were found. The drawback is that the probability of falling in local minima is also increased. It has been observed from Fig. 8 that now convergence of algorithm has been achieved for all values of $\mathrm{N}=120$, 240 and 600. However, from inset of Fig. 8, it is observed that $\mathrm{N}=240$ the OF reaches a slightly higher value than $\mathrm{N}=120$. Case with $\mathrm{N}=600$ also nears convergence in $\sim 100$ generations. The best optimized loading pattern for all the cases have k-effective near to 1.005 and RPF and TPF less than the designated limits. Table 4 lists the best objective function and computational efforts needed for all these cases. It is also worth noting that number of generations for reaching convergence for N $=120 \& 240 \& \alpha=0.15$ are $<150$. Therefore, it can be said that with lower value of $\alpha(0.05)$ and higher population size (N) desirable OF cannot be achieved even after increasing computational effort (from 36,000 to 60000). But the algorithm can be made computationally efficient even with lower N by increasing value of $\alpha$. Similar trend has been observed when $\alpha$ is increased to 0.5 and is shown in Fig. 9. It is observed that $<60$ generations are required for reaching converged solution for all three cases ( $\mathrm{N}=120,240 \& 600$ ). The converged value is almost same. Only difference is it takes slightly more number of generations ( $\sim 60$ ) for $\mathrm{N}=120$. But the cases with $\mathrm{N}=240 \& 600$ reaches a converged value in $<50$ generations. Since the final OF achieved is having similar properties therefore, it can be said that for case with $\alpha=$ $0.5 \& \mathrm{~N}=120$ and $\alpha=0.5 \& \mathrm{~N}=240$ a reasonably good optimized solution can be achieved with least computational effort (no. of simulations). It has been observed that maximum fuel utilization was found in case with $\boldsymbol{\alpha}=\mathbf{0 . 5} \& \boldsymbol{N}=\mathbf{2 4 0}$. Table 5 compares the salient parameters of optimized LPs for all cases.

Taking lower value of M and / or higher value of $\alpha$ will result in higher weightage of best solution for modification of DF. In other words, it makes the algorithm greedy and accelerates the convergence. Therefore, to further improve the performance and reduce the computational effort, value of M was changed to $10 \%$ from previous value of $20 \%$ for the most optimized case $(\mathrm{N}=240 \alpha=0.5)$ only. The comparison of this case with other cases is shown in Table 5. Fig. 10 compares this case with earlier optimized case for $\mathrm{M}=20 \%$. It has been observed that here the convergence is achieved in $\sim 18$ generations (case-VIII), therefore the number of simulations are only $240 \times 18=4320$. The optimized loading patterns for all the cases mentioned in Table 5 are shown in Figs. 11 to 18. No constraint has been imposed on number and locations of each
![img-8.jpeg](img-8.jpeg)

Fig. 9. OF Vs Generation number for case V, VI \& VII.

Table 4
Performance of EDA for different internal parameters for VVER initial core LPO problem.

${ }^{a}$ More generations required to reach optimized solution.
${ }^{b}$ Convergence is achieved so, more number of generations are not required.
type of FAs during the optimization process. Hence different number of fuel types with different locations in the core is observed in these patterns but having similar k-effective values. Preliminary analysis has shown that all the 8 LPs optimized in this study have similar/better characteristics compared to benchmark pattern.

## 5. Cycle characteristics for optimized LP using EDA

A detailed follow-up analysis has been carried out by simulating complete first cycle studies for optimized LP. It is to be noted that for case with $\alpha=0.05, \mathrm{~N}=240 \& \alpha=0.05, \mathrm{~N}=600$ are not shown as the optimized LP as these two cases were not meeting target objectives as discussed in last session. The burn up simulations for all these core loading patterns are carried out and the cycle length has been evaluated. The initial fissile inventory and control rod worth of group 10 has also been evaluated. All these parameters have been compared with VVER X2 benchmark results. The properties of the best loading patterns found are compared in Table 5. The number of different type of FAs is also compared with benchmark. Following are the main observations:
a) For all the cases, the optimized solution has k -effective -1.0046 to 1.005. And the cycle length for all the cases is in the range of 320 340 FPDs which is quite comparable to benchmark value of 330 FPDs.
b) The RPF \& TPF meet their desired limit for all optimized LPs.
c) The initial fissile inventory for all cases studied is lesser than benchmark case. Therefore, any case, where cycle length is more than benchmark case, will have better fuel utilization in cycle -1 . All the cases except Case I\&V have better initial fissile inventory and better/same cycle length than benchmark case.
d) Comparison of of control rod worth shows that for some LP, the worths are different from reference. This may be due to the fact that
flux distribution at core level may be different than benchmark case. Higher control rod worth has been observed for the LPs where the FA at location of control rod group is having a higher fissile content than the FA present for benchmark case. However, in none of the cases the worth is lower than 4 mk . A higher worth can be managed by
![img-9.jpeg](img-9.jpeg)

Fig. 10. OF Vs Generation number for case VI \& VIII.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Core Layout of Case I.

Table 5
Properties of loading pattern optimised using EDA for variation of population size ( N ) and $\alpha$.
![img-11.jpeg](img-11.jpeg)

Fig. 12. Core Layout of Case II.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Core Layout of Case III.
![img-13.jpeg](img-13.jpeg)

Fig. 14. Core Layout of Case IV.
changing number of control rods, control rod position or material. More studies may be required to certify this.
e) With respect to initial fissile requirement, the best case observed is case VI, where with initial fissile requirement is 2979 kg and cycle length is 330 FPDs. In case of benchmark (BM), these values are
![img-14.jpeg](img-14.jpeg)

Fig. 15. Core Layout of Case V.
![img-15.jpeg](img-15.jpeg)

Fig. 16. Core Layout of Case VI.
![img-16.jpeg](img-16.jpeg)

Fig. 17. Core Layout of Case VII.

3297 kg and 330 FPDs. With respect to highest cycle length, case II, IV \& VIII have higher cycle length of $340,335 \& 340$ FPDs respectively. However, for overall fuel utilization, case VI as initial fissile content is minimum ( 2979 kg ) for cycle length of 330 FPDs. The case

![img-17.jpeg](img-17.jpeg)

Fig. 18. Core Layout of Case VIII.
VIII also has a comparable overall fuel utilization characteristic. Here, a cycle length of 340 FPDs with initial fissile content of $\sim 3083$ Kgs is observed. The ratio of power in each hexagon at beginning of cycle (BOC) in core for case VI and benchmark case has been shown in Fig. 19. It is observed that for all hexagons in the outmost two rings this ratio is $<1.0$. Therefore, for case VI, the flux in outer region of the core has been reduced which has resulted in reduction in leakage. The ratio of power in each hexagon at end of cycle (EOC) in core for case VI and benchmark case has been shown in Fig. 20. It is observed that for all hexagons in the outmost two rings this ratio is $<$ 1.0. Therefore, for case VI, the low leakage flux in outer region of the core has been maintained till the EOC. The same trend has been observed for other cases also where better fuel economy is observed. This could be the main reason for better utilization of fuel. For case II, control rod worth and fuel utilization is similar to bench mark case. The ratio of power at BOC in each hexagon in core for case II and benchmark case has been shown in Fig. 21. It is observed that
except for few hexagons in core, power distribution has been comparable at almost all positions and the number is always near to 1.0. The ratio of power in each hexagon at end of cycle (EOC) in core for case II and benchmark case has been shown in Fig. 22. Here also similar trend of lower leakage is maintained. At EOC the power distribution for both case VI \& II becomes more comparable to benchmark case.

The behavior of core operational parameters namely critical Boron, RPF \& TPF with burn up for these cases is shown in Figs. 23, $24 \& 25$ respectively. The critical Boron has been normalized to the benchmark critical B at 0 FPD and the comparison of normalized critical B for or all cases with burn-up (case I to VIII) is shown in Fig. 10. The radial peaking factor (RPF) and triangular peaking factor (TPF) are normalized to their design limits of $1.5 \& 2.32$ respectively and the comparison for or all cases with burn-up (case I to VIII) is shown in Fig. 11. From the Fig. 11, it is noted that throughout the cycle, RPF limit are maintained for all cases except for case VII. For case VII, the design limit for RPF has been breached during the mid-cycle. It can be observed from Figs. 11-18, the LP for case VII (Fig. 17) has fuel type 3 (having higher fissile content than type $-1 \& 2$ ) located in central region of the core. All other configurations including the BM core, shows a reasonable number of type 1 FAs (least fissile content) in central region. Due to this different distribution in case VII, the RPF/TPF may be showing a different trend w.r.t other cases considered. Therefore, re-rating of power will be required for case VII during that short period of follow-up time when the operational parameters are beyond design limit. This analysis shows that merely optimizing an initial core LP (where all design parameters are meeting their limits) may not be sufficient but its corresponding cycle length study is also a necessity to demonstrate the safe and efficient operation of reactor. It is important to perform a complete cycle analysis for initial to equilibrium cores to quantify the adequacy of the LP.

## 6. Conclusions and future work

From the above analysis, it can be concluded that the EDA is very effective in solving LPO problem of VVER initial core. It was observed
![img-18.jpeg](img-18.jpeg)

Fig. 19. Ratio of core power distribution at BOC for case VI \& benchmark case.

![img-19.jpeg](img-19.jpeg)

Fig. 20. Ratio of core power distribution at EOC for case VI \& benchmark case.
![img-20.jpeg](img-20.jpeg)

Fig. 21. Ratio of core power distribution at BOC for case II \& benchmark case.
from initial phase study that more than $36,000(\mathrm{~N}=120, \alpha=0.05, \mathrm{M}=$ $20 \%$, Case-I) simulations are required to reach optimized loading pattern but no convergence of algorithm. It is to be noted that initially, it was thought that by increasing total number of simulations by increasing population size will result in better solutions. Therefore, higher N values of $240 \& 600$ were chosen. But, from analysis, it was observed that the algorithm is becoming inefficient in search of
optimized solution while exploring different areas of search space. Other internal parameters $\alpha \& \mathrm{M}$ were varied and found that case with $\alpha=0.5$, $\mathrm{N}=240 \& \mathrm{M}=10 \%$ are optimized value of EDA for VVER X2 benchmark initial core LPO problem. Moreover, using these values, $<5000$ simulations are required to reach optimized solution. Therefore, an important observation is that in EAs, by increasing number of simulations may not necessarily improve chances of reaching better optimized

![img-21.jpeg](img-21.jpeg)

Fig. 22. Ratio of core power distribution at EOC for case VI \& benchmark case.
![img-22.jpeg](img-22.jpeg)

Fig. 23. Normalized critical Boron Vs Full Power Days (FPDs).
solution. The choice of internal parameters is more important for algorithms performance.

The initial fissile requirement for all optimized LPs is lower than the benchmark case. All the optimized LPs have shown a better initial fissile content (Table 5) compared to benchmark case along with safe and continues operation at rated power during initial phase. All the cases except case I \& V have shown longer or same cycle length compared to benchmark case. Considering all the factors, the best case observed w.r.t fuel utilization is case VI $(\mathrm{N}=240, \mathrm{M}=20 \%$ and $\alpha=0.5)$. Here $-10 \%$ less fissile inventory is required compared to benchmark case for achieving higher cycle length of -340 FPDs compared to 330 FPDs. This has been achieved by changing the flux shape and reducing leakage. However, to prove that the fuel utilization has improved (if at all) from initial phase to equilibrium phase, a comprehensive study for full fuel
![img-23.jpeg](img-23.jpeg)

Fig. 24. Normalized Radial Peaking Factor (RPF) Vs Full Power Days (FPDs).
cycle analysis from initial to equilibrium phase, where, optimized LPs will be generated by EAs at each refueling is required. And detailed analysis is also required which includes estimation of safety parameters (reactivity co-efficients, shut down margins and axial offsets) for all the cycles upto equilibrium core. In the present study, we have limited our search for best LP considering only three parameters namely, k -eff, RPF \& TPF. The objective function itself can be modified to accommodate other safety parameters. The same has been planned in future work.

The worth of control rods for few cases (case II, IV, V, VI, VII \& VIII) of optimized patterns is quite different as compared to benchmark case. A study can be planned to observe the practical implications and possible ways to keep it similar by changing the position of FAs manually or control material.

It has been observed that optimized loading pattern with 4 fuel types

![img-24.jpeg](img-24.jpeg)

Fig. 25. Normalized Triangular Peaking Factor (TPF) Vs Full Power Days (FPDs).
is also possible as seen in case-II, IV, VI \&VIII (No FA of fuel type 5 for case II, IV \& VI and type 4 for case VIII respectively). Therefore, another effort has been planned for search of a simplified initial loading pattern with lesser number of fuel types ( $<5$ ) compared to benchmark case. Best pattern observed can be refined further through modification in algorithm/objective function or manual interventions for better fuel utilization and safe/longer operation. Although satisfactory results have been obtained using FDA further study can still be continued in search of better LPs considering other EAs like GA.

## CRediT authorship contribution statement

Amit Thakur: Conceptualization, Methodology, Data curation, Software, Writing - original draft, Formal analysis, Visualization. Argala Srivastava: Methodology, Software, Data curation, Formal analysis, Visualization, Writing - review \& editing. Vaibhav Kumar: Software, Data curation. Kislay Bhatt: Software, Investigation, Data curation. Vibhuti Duggal: Software, Data curation. K. Rajesh: Software, Supervision. Umasankari Kannan: Conceptualization, Visualization, Investigation, Supervision.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgements

The authors are thankful to Dr K. P Singh, Dr. R. Karthikeyan, Bhabha Atomic Research Centre, Mumbai \& Dr Thillagam of Safety Research Institute, AERB, Kalpakkam, India for their support during the course of this work. The authors are also thankful to Mr Sandeep Singh and Mr. Gopal Mapdar, Bhabha Atomic Research Centre, Mumbai for their help with programming and preparation of figures.
