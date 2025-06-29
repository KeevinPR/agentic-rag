# Design and optimization of heat-integrated distillation configurations with variable feed composition by using a Boltzmann-based estimation of distribution algorithm as optimizer 

Roberto Gutiérrez-Guerra ${ }^{a, b, \text { a }}$, Rodolfo Murrieta-Dueñas ${ }^{b}$, Jazmín Cortez-González ${ }^{b}$, Juan Gabriel Segovia-Hernández ${ }^{b}$, Salvador Hernández ${ }^{b}$, Arturo Hernández-Aguirre ${ }^{c}$<br>${ }^{a}$ Universidad Tecnológica de León, Campus I, Área de sustentabilidad para el desarrollo, Blvd. Universidad Tecnológica 225, Col. San Carlos, 37670 León, Gto., Mexico<br>${ }^{\text {b }}$ Universidad de Guanajuato, Campus Guanajuato, Departamento de Ingeniería Química, Noria Alta s/n, 36050 Guanajuato, Gto., Mexico<br>${ }^{c}$ Centro de Investigación en Matemáticas, A.C., Departamento de Computación, A.P. 402, Guanajuato, Gto. CP 36000, Mexico

## A R T I C L E I N F O

Article history:
Received 16 October 2016
Received in revised form 6 April
2017
Accepted 24 May 2017
Available online 3 June 2017

## Keywords:

Optimization
Heat-integrated distillation columns
Feed composition
Boltzmann distribution
Energy savings
TAC

A B STR ACT

The economic, energetic, and environmental performance of heat-integrated distillation columns used to separate close-boiling mixtures with variable feed composition is presented. A Boltzmann-based estimation of distribution algorithm was used as optimizer. The total annual cost was defined as the fitness function of the problem. We study three mixtures of hydrocarbons and one mixture of polar compounds. The results show that the BUMDA algorithm leads continuously to obtain good values of the fitness function. The analysis carried out showed that the influence of the feed composition was larger in the energy consumption than in the TAC at each case study. In addition, the best compromise between energy consumption and the total annual cost was obtained in mixtures with a feed composition of $0.75 / 0.25$ for most case studies. These HIDiC configurations showed energy savings between 85 and $87 \%$. Thus, similar reductions in the energy consumption, carbon dioxide emissions and cooling water were obtained. On the other hand, the TAC of the best HIDiC designs varies from HIDiC designs with a reduction of $27 \%$ to HIDiC schemes with a TAC $2 \%$ larger than the corresponding TAC of the traditional configurations.
(c) 2017 Institution of Chemical Engineers. Published by Elsevier B.V. All rights reserved.

## 1. Introduction

Sustainability for development is a sought-after goal for the chemical industry around the world. The generation of new chemical plants is achieved under the fundamentals established to design chemical processes. However, the heavy focus on process optimization makes this a complex task for chemical engineering.

A reality regarding most chemical processes is the large amount of energy engaged in separation processes, particularly in distillation columns. The high purities achieved by this process support the use of this separation method. Thus, the technology is applied to purify more than $90 \%$ of the fluids used in the chemical industry (Humphrey, 1995). So, the current challenge is the reduction of the energy consumption and environmental footprint produced by chemical processes.

[^0]
[^0]:    ${ }^{a}$ Corresponding author at: Universidad Tecnológica de León, Campus I, Área de sustentabilidad para el desarrollo, Blvd. Universidad Tecnológica 225, Col. San Carlos, 37670 León, Gto., Mexico.

    E-mail addresses: rogutierrez@utleon.edu.mx, uranio.bz@hotmail.com (R. Gutiérrez-Guerra).
    http://dx.doi.org/10.1016/j.cherd.2017.05.025
    0263-8762/© 2017 Institution of Chemical Engineers. Published by Elsevier B.V. All rights reserved.

## Nomenclature

TAC Total annual cost (USD/year)
CC Capital cost (USD/year)
COP Operation cost (USD/year)
SR Rectifying section
SS Stripping section
NT Total number of stages
CR Compression ratio
RR Reflux ratio
$\Delta \mathrm{T}_{\text {SR-SS }}$ Temperature driving force ( K )
Qcomp Compressor duty ( $\mathrm{k} / / \mathrm{h}$ )
Qint Total heat integrated ( $\mathrm{k} / \mathrm{h}$ )
Qi Heat integrated at stage i ( $\mathrm{k} / \mathrm{h}$ )
Q ratio Heat duty of HIDiC/heat duty of conven-
tional column
QC Condenser duty ( $\mathrm{k} / \mathrm{h}$ )
TAC ratio TAC HIDiC/TAC conventional column
$\mathrm{CO}_{2 \text { emiss }}$ Carbon dioxide emissions (t/year)
$\mathrm{CO}_{2}$ ratio $\mathrm{CO}_{2 \text { emiss }} \mathrm{HIDiC} / \mathrm{CO}_{2 \text { emiss }}$ conventional column
CWcons Cooling water consumption ( $\mathrm{kg} / \mathrm{h}$ )
CW ratio CW-HIDiC/CW-conventional column
VF Vapor flow ( $\mathrm{kmol} / \mathrm{h}$ )
A Heat transfer area $\left(\mathrm{m}^{2}\right)$

Heat-integrated distillation columns are technologies that use energy efficiently and might provide a profitable TAC at difficult separations, such as close boiling mixtures (Kiss and Olujić, 2014; Gutiérrez-Guerra et al., 2016). The conventional column shown in Fig. 1 is the base to build the hypothetical HIDiC configuration observed in Fig. 2., by relocating the rectifying and stripping sections. The operation
![img-0.jpeg](img-0.jpeg)

Fig. 1 - Traditional column.
![img-1.jpeg](img-1.jpeg)

Fig. 2 - HIDiC configuration.
![img-2.jpeg](img-2.jpeg)

Fig. 3 - Concentric HIDiC column.
of the compressor and the throttling valve promote that SR operates at larger pressure and temperature than SS. Thus, the internal heat exchanging from SR to SS takes place. On the other hand, the translation of the hypothetical model of the HIDiC into a real configuration is depicted in Fig. 3. As it is observed, this arrangement may be assembled in a concentric configuration, where SR is placed inside SS (Govind, 1987; Aso et al.,1996/1998).

The operational principles and the structural configuration of the HIDiC sequences lead to large energy savings and profitable total annual cost. For instance, energy savings of $60 \%$ in the separation of binary mixtures (e.g. benzene/toluene) using the HIDiC sequence were determined by Nakaiwa et al. (1997). In addition, Iwakabe et al. (2006) achieved the separation of two mixtures made of benzene/toluene/psylene and twelve-hydrocarbon, respectively, using the HIDiC column. They determined that the HIDiC column used to separate the ternary mixture requires $30 \%$ less energy than the conventional configuration. Besides, the separation of the twelve-hydrocarbon mixture uses $50 \%$ of the energy consumed by the conventional column. On the other hand, Olujic et al. (2006), computed reductions of $20 \%$ of the TAC of the HIDiC sequence in relation to the vapor recompression system (VCR). The separation of propane-propylene was used as case study. Later, the evaluation of the performance of HIDiC configuration in a refiner debutanizer was examined by Jana and Mali (2010). Results evidenced energy savings of $44 \%$ and a total annual cost of $14 \%$ lower than the corresponding TAC of the conventional column. Also, Harwardt et al. (2010) performed an optimization study of HIDiC sequences to split a set of close boiling hydrocarbon mixtures by using a MINLP strategy. Results disclosed that the HIDiC sequence is more energetically and economically favorable using mixtures with low relative volatility. On

the other hand, the optimization of a HIDiC sequence via genetic algorithms was achieved (Shahandeh et al., 2014). The separation of the mixture made of benzene and toluene as a case study was used. Results showed energy savings up to $6.6 \%$ and a reduction of the TAC of about $9.75 \%$.

Later, the implementation of a constrained Boltzmann-based Estimation of Distribution Algorithm (BUMDA) to optimize HIDiC configurations was achieved (Gutiérrez-Guerra et al., 2014). Three equimolar binary mixtures were used as a case study: $n$-butanol/isobutanol, $n$-heptane/cyclohexane, and benzene/toluene. Compared with the traditional sequences, the results showed energy savings of $84 \%$ for the mixture of alcohols, whereas the reduction of the total annual cost was $2 \%$. Besides, energy savings of 62.5\% and 52.5\% for mixtures made of nheptane/cyclohexane and benzene/toluene, respectively, for the HIDiC designs were obtained. However, the total annual cost of the HIDiC was $32 \%$ larger for the mixture made of n-heptane/cyclohexane and $35 \%$ greater for the mixture made of benzene/toluene.

More recently, the effect of the relative volatility in the optimization of HIDiC sequences by using a constrained Boltzmann-based estimation of distribution algorithm was performed (Gutiérrez-Guerra et al., 2016). The range of relative volatility varied from 1.12 to 2.4. The total annual cost was defined as the fitness function of the problem. The results showed that the best interrelation between energy savings and TAC of the HIDiC columns were obtained in the separation of mixtures with relative volatilities between 1.12 and 1.5 , particularly for mixtures of isomers. As a result, energy savings from 50 to $87 \%$ were obtained for this class of mixture. At the same time, we obtained HIDiC sequences with TACs lower than that TAC of conventional columns (2-16\%). Nevertheless, it was found that the TAC of some HIDiC schemes resulted higher than the TAC of conventional columns (6-17\%). In addition, carbon dioxide emissions released into the atmosphere were reduced in the same proportion as savings in energy required to fuel the reboilers.

Although the energetic and economic performance of HIDiC configurations has been broadly studied, research related to the evaluation of feed composition using optimization strategies is absent. Thus, the potential of these configurations under the effect of feed composition by using robust optimization strategies must be evaluated.

Hence, the goal of this study is to find the best behavior of HIDiC sequences with variable feed composition by using the Boltzmannbased estimation of distribution algorithm and rigorous simulations using the Radfrac model in Aspen thus ${ }^{9}$. This goal is pursued by means of the separation of several close boiling point mixtures. The feed compositions selected vary from equimolar mixtures to larger and lower compositions regarding this composition. The feed compositions proposed are established to assess the fitness function (TAC), energy consumption, cooling water consumption and carbon dioxide emissions. The decision variables of the problem are given by the total number of stages, compression ratio and reflux ratio.

## 2. Optimization strategies

The optimization of constrained nonlinear and multivariable problems has been tackled by using deterministic methods (Smith and Pantelides, 1995; Caballero and Grossmann, 1999; Segovia-Hernández et al., 2015; Lopez-Saucedo et al., 2016). The global optimum obtained using these strategies makes it possible to find the best performance of chemical processes under the goals and constraints established. The broad application and continuous development of deterministic strategies have made of them robust tools. In these strategies, a great math treatment and the tuning of good initial values to obtain the global optimum are required.

On the other side, the application of stochastic methods leads to a set of suboptimal solutions of the optimization problem. Nevertheless, differently than the other strategies, the process modeling may be handled as a black box, and no initial values are required to start the search. The flexibility and
robustness observed at stochastic methods used to optimize complex problems support their great usefulness (GutiérrezAntonio and Briones-Ramírez, 2010; Bonilla-Petriciolet et al., 2010, 2011; Shahandeh et al., 2014; Gómez-Castro et al., 2015). Moreover, solutions obtained by using these methods give important enhancements in the performance of chemical processes, even when the global optimum is not warranted. At the same time, considering the reasonable time involved in carrying out a search, these strategies are an important option for chemical engineering.

Using stochastic strategies makes it possible to obtain a set of HIDiC configurations with different requirements of energy consumption and TAC. Thus, the decision maker is able to select the sequence that meets the energetic and economic goals along with the environmental constraints imposed on a determined industry. So, if a meaningful energy saving and a profitable TAC for a particular design are determined, this configuration may be chosen. However, if there is a distillation process with multiple energetic and/or environmental constraints, but with economic support (e.g. carbon credits), the implementation of the configuration with the minimum energy consumption and a reasonable TAC might be performed.

BUMDA algorithm (Valdez et al., 2013) is an efficient optimizer that belongs to the estimation of distribution algorithm (EDAs). In EDAs, a probability distribution is used to select the best individuals of the population and produce each new generation. This stochastic strategy keeps a continuous approximation to the fitness function $[\mathrm{g}(\mathrm{x})]$ by means of the probability model shown in Eq. (1).
$P(x)=\frac{\exp ^{j \rho(x)}}{Z}$
At the same time, the model of Eq. (1) depends on the variables $\beta$ and $Z . \beta$ is defined by the inverse product between the Boltzmann's constant ( k ) and the temperature ( T ), $1 /(\mathrm{kT})$. In EDAs, this parameter has a direct relationship with the selection pressure and the variance. Besides, the Z parameter is evaluated by the summation of the exponential function of the numerator on the whole search domain. Thus, the probability distribution for the individuals is given by Eq. (2).
$P\left(x_{i}\right)=\frac{\exp ^{j \rho\left(x_{i}\right)}}{\sum_{x} \exp ^{j \rho(x)}}$
It is important to underline that this modeling requires that an infinite population is evaluated. As it is not a feasible condition, the Boltzmann distribution has been approached by a normal distribution, represented by a Gaussian distribution, which is a function of mean $(\mu)$ and variance $(\nu)$ of the population. To keep the essence of Boltzmann distribution, the minimization of the Kullback-Leibler Divergence (KLD) between the Gaussian distribution and the Boltzmann distribution is achieved.

In addition, BUMDA algorithm works using a truncation method. This method is in charge to limit the current population to the best individuals. So, each new generation is produced with the characteristics of the best individuals selected in the previous population.

On the other side, with the aim to obtain a better performance, a reset mechanism was attached in the BUMDA. This mechanism resets the population when a minimum value of the variance of decision variables is reached. This action

makes it possible to perform intensified searches for the best individuals. The value of the minimum variance allowed in this work was 0.001 .

Notice that a more detailed description of the BUMDA algorithm might be found at Gutiérrez-Guerra et al. (2014).

## 3. Problem statement

The design-optimization problem of the heat-integrated columns defined in this work is given in Eq. (3). This problem is represented by a non-linear multivariable model with three decision variables: the total number of stages, reflux ratio, and compression ratio. The total number of stages represents a discrete variable, while compression ratio and reflux ratio are the continuous variables of the problem. The total annual cost is the fitness function of the problem.
$\operatorname{Min}_{1}(\mathrm{TAC})=f(N T, C R, R R)$

Subject to
$X_{\text {purity }}=X_{\text {recovery }}=0.995 \pm \delta_{i} \delta=0.0003 ; \Delta T_{\text {SR-SS }} \geq 1.67 \mathrm{~K}$

The optimization problem includes equality and nonequality constraints. The equality constraints are converted to inequality constraints with a $\delta$ threshold. For instance, the equality constraint: $\mathrm{X}_{\text {purity }}-0.995 \approx 0$ is treated as: $\left|X_{\text {purity }}-0.995\right| \leq \delta$.

Furthermore, the temperature driving forces to perform the heat exchange between SR and SS was the third constraint imposed in the problem. That is, the minimum temperature driving force to perform heat transference between both sections is 1.67 K . In particular, the constraint of temperature driving force is implicitly handled by means of the compression ratio used. So, the energy integration will take place only when the CR used generates temperature driving forces equal or larger than 1.67 K between SR and SS.

The total annual cost was calculated using the Guthrie method (Guthrie, 1974) and the cost equations shown in Turton et al. (2004). In this work, 8000 operation hours per year were considered. The TAC is given by the summation of the operation and capital costs. Operation costs include the costs of heating steam used in the reboiler, cooling water consumption in the condenser and electrical power used to drive the compressor. The costs of utilities were established based on values reported in the literature (Nakaiwa et al., 2001; Turton et al., 2004; Gutiérrez-Guerra et al., 2016). Electricity: $0.1 \mathrm{USD} / \mathrm{kWh}$, heating steam: $0.016 \mathrm{USD} / \mathrm{kg}$ and cooling water: $0.0148 \mathrm{USD} / \mathrm{m}^{3}$.

Capital cost involves the cost of the main elements of the HIDiC: columns, reboiler, condenser, compressor and heat transfer areas. The overall heat transfer coefficient used for sizing both heat transfer areas and reboiler was established as $1135 \mathrm{~W} / \mathrm{m}^{2} \mathrm{~K}$. The overall heat transfer coefficient for the condenser was defined as $851 \mathrm{~W} / \mathrm{m}^{2} \mathrm{~K}$. The costs of utilities and correlations used to compute the capital costs were widely discussed in Gutiérrez-Guerra et al. (2016). In addition, the heat duty of the HIDiC is the result of reboiler duty plus compressor duty. On the other side, the heat duty for the conventional column is given by reboiler duty. Carbon dioxide emissions were calculated using the model developed by Gadalla et al. (2005).

Table 1 - Case studies.

| Mixture |  |  | Feed composition |  |
| :--: | :--: | :--: | :--: | :--: |
| M1 (n-butanol/isobutanol) |  |  | 0.25/0.75 |  |
| M2 (n-octane/ethylbenzene) |  |  | 0.35/0.65 |  |
| M3 (ethylbenzene/o-xylene) |  |  | 0.5/0.5 |  |
| M4 ( $m$-xylene/o-xylene) |  |  | 0.65/0.35 |  |
|  |  |  | $0.75 / 0.25$ |  |

Table 2 - Limits of optimization variables.

| Mixture | Feed composition | Optimization variables |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  |  | NT | CR | RR |
| M1 | 0.25/0.75 | 50-90 | $1.1-3$ | $1.5-20$ |
|  | 0.35/0.65 | 50-90 |  | $1.5-20$ |
|  | 0.5/0.5 | 48-88 |  | $1.5-20$ |
|  | 0.65/0.35 | 48-88 |  | $1.5-20$ |
|  | 0.75/0.25 | 48-88 |  | $1.5-20$ |
| M2 | 0.25/0.75 | 56-96 | $1.1-3$ | 8-35 |
|  | 0.35/0.65 | 60-100 |  | 8-35 |
|  | 0.5/0.5 | 70-110 |  | 8-25 |
|  | 0.65/0.35 | 73-113 |  | 8-35 |
|  | 0.75/0.25 | 78-118 |  | 8-35 |
| M3 | 0.25/0.75 | 64-114 | $1.1-3$ | 20-50 |
|  | 0.35/0.65 | 65-115 |  | 20-50 |
|  | 0.5/0.5 | 70-110 |  | 8-25 |
|  | 0.65/0.35 | 64-114 |  | 8-25 |
|  | 0.75/0.25 | 64-114 |  | 8-25 |
| M4 | 0.25/0.75 | 92-132 | $1.1-3$ | 70-350 |
|  | 0.35/0.65 | 96-136 |  | 80-250 |
|  | 0.5/0.5 | 102-142 |  | 65-90 |
|  | 0.65/0.35 | 110-150 |  | 50-150 |
|  | 0.75/0.25 | 116-156 |  | 30-150 |

## 4. Case study

The case studies shown in Table 1 are binary mixtures made of chemical compounds of industrial concern. For instance, alcohols are used in the process of production of active pharmaceutical ingredients. The other materials are feedstock to produce plastics and synthetic fibers, and some are used as fuels. The mixtures include isomers for most cases, such as the mixtures M1, M3, and M4. The characteristics of the components of the mixture M2 leads to a difficult separation due to its low relative volatility. These mixtures were selected based on the outcomes obtained in the previous study (GutiérrezGuerra et al., 2016). As it was widely discussed in that study, the best performance of both energy savings and total annual cost (TAC) of the HIDiC configurations was determined at low relative volatility, particularly in the range of 1.12-1.5. Thus, in order to obtain further benefits of this technology, in this work, the behavior of the HIDiC columns at feed composition larger and less than 0.5 is explored. A feed rate of $100 \mathrm{kmol} / \mathrm{h}$ of saturated liquid was established. In this work the feed stream of the conventional sequence enters at the middle of the column. Thus, the feed stream of the HIDiC configuration is introduced in the first stage (dome) of stripping section. This was done because the approach used to assemble the HIDiC configurations is the separation of the traditional column into two symmetric sections, SR and SS. In Addition, the target for both purity and recovery was established as 0.995 , mol fraction.

The limits of the optimization variables shown in Table 2 were defined considering the results obtained in the earlier study (Gutiérrez-Guerra et al., 2016). The limits of

the total number of stages were determined using the Fenske-Underwood-Gilliland method. An increase of forty stages was allowed to assess the behavior of the fitness function. A range of compression ratio from 1.1 to 3 was established. Similarly, the limits of the reflux ratio were selected taking as a reference the maximum and minimum number of stages of the columns. So, the maximum number of stages was taken as a reference to establish the lower limit of RR, whereas the upper limit was established using the minimum number of stages. Both limits were increased in order to obtain a substantial content of energy to be transferred from SR to SS. The total number of stages was obtained from the simulation of conventional columns (using the DSTWU module) for different compositions.

The limits of both total number of stages and reflux ratio make evident the difficulties of separation of the mixtures used in this work. As mentioned previously, both variables were relaxed in order to broaden the exploration range to get the best HIDiC designs through the optimization process. It is important to take into account that the considerably large reflux ratio ranges (e.g. 350) are values initially established to obtain large amounts of energy to be integrated. However, this variable experiences a reduction when the energy integration is performed. In fact, the reduction of reflux ratio along the optimization process is used to control the constraints (purities) established. Thus, this manipulation leads getting HIDiC designs with feasible values for reflux ratio. This reduction is performed because the energy integration commonly increases the purity of distillation products beyond the target established. Hence, the alternative to keep the constraints under the values defined, the reflux ratio is reduced.

It is important to underline that Aspen Plus does not contain a model to simulate HIDiC configurations. Hence, the HIDiC sequences were designed by a direct rearrangement of conventional columns, by establishing a symmetric distribution of SS and SR. So, the heat transfer from SR to SS is performed at the same level of these sections.

The RadFrac model with reboiler is selected to represent the stripping section and the RadFrac model with condenser is used to assemble the rectifying section. Both sections are connected by using the models for the isentropic compressor, the throttling valve, and the heat streams. The heat-stream model of Aspen Plus ${ }^{\circledR}$ is used to represent the internal heat integration between SR and SS.

Modeling the thermodynamic behavior of the mixtures was established taking recommendations from the literature (Rodrigues et al., 2005; Seader and Henley, 2006). The separation of alcohols was performed using the thermodynamic model of NRTL. This model was employed due to the polar character of the mixture of isomers and its low relative volatility. On the other side, the low relative volatility of isomers of xylenes led to establishing the thermodynamic model of UNIQUAC to separate these mixtures. In addition, the Chao-Seader model was used to simulate the separation of hydrocarbons with larger relative volatility.

The evaluation of the energy consumption and total annual cost in the separation of equimolar mixtures by using HIDiC columns has been an important starting point to disclose the performance of HIDiC sequences. However, the analysis of the feed compositions used in this study makes it possible to obtain more generalized results.

Despite the separation of equimolar mixtures by using HIDiC sequences giving great benefits, the establishment of lower and larger feed compositions than equimolar com-
positions enables the identification of the most convenient performance of this technology. Besides, this evaluation is done with the aim to disclose the performance of HIDiC columns at feed compositions more similar to the compositions of real processes.

The development of this study is based on the thermodynamic principles to transfer heat from rectifying section to stripping section. The heat transference takes place from SR to SS at the same level of the columns.

The heat integration is theoretically allowable from stages of SR to stages of SS, leaving with no heat exchange the corresponding stages to the condenser and reboiler. However, the thermodynamic constraints established in the optimization limit the heat integration only on those stages with a minimum temperature driving force between SR and SS.

The amount of heat integrated at each stage is calculated by means of Eq. (4), using the condenser duty.
$\mathrm{Qi}=\Delta T_{\mathrm{SR} 0 \text {-SS1 }}\left(\frac{\mathrm{QC}}{\sum_{\mathrm{i}=1} \Delta \mathrm{~T}_{\mathrm{SR} i-\mathrm{SSI}}}\right)$
In addition, the heat transfer area by stage was calculated by using Eq. (5).
$\mathrm{Ai}=\left(\frac{\mathrm{Q}_{\mathrm{i}}}{\mathrm{U} \Delta T_{\mathrm{SR} i-\mathrm{SSI}}}\right)$
where i represents the corresponding stage.
The selection of condenser duty as the available energy to be integrated is based on operational principles of a distillation process. As is widely known, conventional distillation columns use energy inefficiently. This behavior is produced because the heat supplied to the reboiler is simply eliminated in the condenser by using cooling water. The energy eliminated in the condenser is usually released to the environment because of its low quality to achieve work. Thus, instead of using the energy in the traditional way, a large portion of the heat to be eliminated in the condenser of the conventional column is integrated in the feasible stages of the HIDiC column. Therefore, the duties of both reboiler and condenser are reduced. As it is observed in the Eq. (4), the temperature driving forces were the parameters used to compute the quantities of energy to be exchanged stage by stage. So, the quality (temperature) controls the amount of heat integrated. In other words, the amounts of available energy to be integrated from the vapor flows of SR (which is the source of heat) to the liquid flows of SS (sink of heat) are constrained by the temperature driving forces. This strategy leads obtaining thermodynamically feasible HIDiC designs, and obeys the structural and economic guidelines to design heat exchangers.

Even the structural design is out of the goals of this study, it is important to mention some possibilities to build HIDiC configurations (Aso et al., 1998; Noda et al., 2006; Nakanishi et al., 2008). Among the possible configurations to assemble HIDiC columns the following are worth mentioning: (a) concentric arrangement, (b) compact heat exchanger (plate-fin), (c) configuration type multi-tube heat exchanger, (d) design of external heat transfer panels, among other arrangements.

![img-3.jpeg](img-3.jpeg)

Fig. 4 - Flowchart of design-optimization of HIDiC columns.

## 5. Methodology

The design-optimization procedure of the HIDiC configurations is shown in Fig. 4. The evaluation of each new generation, produced by BUMDA algorithm, starts with the design of the conventional column, followed by the assembling and heat integration of the HIDiC scheme. Henceforward, the accomplishing of constraints in the HIDiC column is performed and the TAC is computed (Fig. 5). As it was explained before, the best individuals of each generation is selected by BUMDA algorithm to produce the next population. So the fitness function is continuously improved.

The factors used to perform the penalization were tuned to take into account the variation of the fitness function and the computing time. The values for these factors were given in the previous study.

The design-optimization process takes place by means of the interface: Excel ${ }^{\oplus}$-Matlab ${ }^{\oplus}$-Aspen Plus ${ }^{\oplus}$. In this strategy, Excel ${ }^{\oplus}$ has two functions: 1 . performs as a database and 2 . links the BUMDA optimizer programmed in Matlab ${ }^{\circledR}$ and the simulator Aspen Plus ${ }^{\circledR}$ to evaluate the design variables and compute the fitness function. In this work, we used a population of 50 individuals and 3000 function evaluations.

## 6. Results and discussion

The optimization carried out showed a robust performance of the optimization strategy, which achieved an intensified search for the best fitness function of this constrained multivariable problem.

The generalized behavior of the fitness function along the optimization process using the BUMDA algorithm is depicted

$$
\begin{aligned}
& \% \text { compute TAC } \\
& \text { TAC }=\text { COP }+ \text { CC } \\
& \% \text { penalize TAC } \\
& \text { if abs }\left(0.995-X_{\text {purity }}\right)>\delta \\
& \omega_{\text {purity }}=\mathrm{f}^{*}\left(0.995-X_{\text {purity }}\right) * 2 \\
& \text { TAC }_{\text {purity }}=\text { TAC }+\omega_{\text {purity }}{ }^{*} \text { TAC } \\
& \text { end } \\
& \text { if abs }\left(0.995-X_{\text {recovery }}\right)>\delta \\
& \omega_{\text {recovery }}=\text { factor }^{*}\left(0.995-X_{\text {recovery }}\right) * 2 \\
& \text { TAC }_{\text {recovery }}=\text { TAC }+\omega_{\text {recovery }}{ }^{*} \text { TAC } \\
& \text { end } \\
& \% \text { compute TAC penalized by purity and recovery } \\
& \text { TAC }_{\text {penalized }}=\text { TAC }_{\text {purity }}+\text { TAC }_{\text {recovery }} \\
& \% \text { compute TAC penalized by number of constraints violate: } \\
& \text { if number of constraints violated }>0 \text { then } \\
& \text { TAC }_{\text {numpan }}=\omega_{\text {num_ass }}{ }^{*} \text { TAC }_{\text {penalized }} \\
& \text { else } \\
& \text { TAC }_{\text {numpan }}=\text { TAC }_{\text {penalized }} \\
& \text { TAC }=\text { TAC }_{\text {numpan }}
\end{aligned}
$$

Fig. 5 - Penalization strategy used in the design-optimization process of the HIDiC.
in Fig. 6. We observe that as the function evaluations number is increased, the total annual cost experiences a reduction. It is clear that there are several ranges of function evaluations where the value of the fitness function undergoes a relatively steady state. That is, during the evaluation of a determined number of evaluations there is a stable range of the TAC. This range is modified when the search is directed toward a different zone. This leap is produced by the activation of the reset mechanism included in the strategy. The activation of this mechanism is performed when the value of the variance is less than 0.01 . This activation leads to diversify the population and intensify the exploration for better solutions. In Fig. 6 we observed that reset mechanism was activated twice. The first activation was achieved between 1800 and 2000 function evaluations, while the second activation took place at about 2700 function evaluations.

Through the results shown in Table 3, it is clear that the TAC experienced a more uniform trend than the tendency undergone by the heat duty ratio at each case study, at the respective feed compositions. This behavior is produced as a consequence of the variation of compression ratio and reflux ratio. As observed, the compression ratio undergoes less varia-
tion compared with the relation of reflux ratio. Thus, as it was discussed in the recent study (Gutiérrez-Guerra et al., 2016), the total annual cost is mostly influenced by the compression ratio, whereas the heat duty ratio shows an analogous behavior to reflux ratio.

By comparing the five feed compositions of each mixture, the following results were obtained: in the mixtures M1 and M2, CR varies only at 0.55 and 0.95 units as the maximum value, respectively. For the case M3, this variable undergoes a maximum variation of only 0.1 units. Meanwhile, the variation of CR for M4 is as much 0.17 units.

In a similar analysis, notice that the reflux ratio showed a maximum variation of around 0.9 units for M1, while RR ratio for M2 varies at about 9.0 units. In addition, M3 experiences a difference of 2.4 units as a maximum variation, whereas the major difference of RR for M4 is about 7.5 units.

At the same time, it is observed that the total number of stages for the most feasible HIDiC designs concentrates near the upper limit for the mixtures M2, M3, and M4, while the number of stages for the mixture M1 is located near the middle range defined.

Through the results presented in Table 3, we may ratify that the HIDiC configurations experience large reductions in the energy consumption and favorable total annual costs in relation with the traditional columns. The above was determined by analyzing the TAC ratio and the Q ratio for the set of feed compositions assessed.

By a comparison of HIDiC designs obtained for the mixture M1, the best TAC ratio was determined for the feed composition of $0.65 / 0.25$. The TAC for this composition was of $10 \%$ less than the TAC of the conventional column. In addition, the corresponding energy saving obtained for this configuration was $78 \%$. However, notice that the Q ratio and the TAC ratio for the equimolar composition were 84 and $98 \%$, respectively. Thus, the best TAC ratio was determined for the feed composition of $0.65 / 0.35$, but the energy was better harnessed for the equimolar composition.

The corresponding analysis for the mixtures M2-M4 showed that the best HIDiC configuration for each mixture is obtained for the feed composition of $0.75 / 0.25$. Considering the mixture M2, the best HIDiC design showed energy savings of $87 \%$ and a TAC of $27 \%$ less than the corresponding TAC of the conventional sequence. In the case of M3, the reduction of energy consumption was $85 \%$ while the TAC was only $2 \%$ larger than the TAC of the traditional scheme. Similarly, the
![img-4.jpeg](img-4.jpeg)

Fig. 6 - Generalized trend of the optimization process.

Table 3 - Results of optimization for the best HIDiC designs.

| Mixture | Variable | Feed composition |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Traditional columns |  |  |  |  | HIDiC configurations |  |  |  |  |
|  |  | 0.25/0.75 | 0.35/0.65 | 0.5/0.5 | 0.65/0.35 | 0.75/0.25 | 0.25/0.75 | 0.35/0.65 | 0.5/0.5 | 0.65/0.35 | 0.75/0.25 |
| M1 | NT | 56 | 76 | 72 | 76 | 80 | 56 | 76 | 72 | 76 | 80 |
|  | CR | - | - | - | - | - | 1.87 | 1.88 | 1.76 | 1.64 | 2.18 |
|  | RR | 11.65 | 7.04 | 5.27 | 4.10 | 3.70 | 0.98 | 0.29 | 0.084 | 0.106 | 0.19 |
|  | TAC (USD/year) | 1.13E +06 | 1.11E +06 | 1.18E +06 | 1.26E +06 | 1.32E +06 | 1.24E +06 | 1.22E +06 | 1.16E +06 | 1.14E +06 | 1.25E +06 |
|  | Heat duty (kJ/h) | 1.23E +07 | 1.10E +07 | 1.23E +07 | 1.30E +07 | 1.39E +07 | 1.84E +06 | 1.71E +06 | 2.20E +06 | 2.81E +06 | 3.60E +06 |
|  | $\mathrm{CO}_{2}$ emiss (t/year) | 7.06E +03 | 6.30E +03 | 8.58E +03 | 7.47E +03 | 7.98E +03 | 1.03E +03 | 0.98E +03 | 1.19E +03 | 1.61E +03 | 2.06E +03 |
|  | CWcons (kg/h) | 5.57E +05 | 4.80E +05 | 5.05E +05 | 5.60E +05 | 6.34E +05 | 8.33E +04 | 7.30E +04 | 9.31E +04 | 1.20E +05 | 1.51E +05 |
|  | TAC ratio | - | - | - | - | - | 1.10 | 1.10 | 0.98 | 0.91 | 0.95 |
|  | Q ratio | - | - | - | - | - | 0.15 | 0.16 | 0.16 | 0.22 | 0.26 |
|  | $\mathrm{CO}_{2}$ ratio | - | - | - | - | - | 0.15 | 0.16 | 0.14 | 0.22 | 0.26 |
|  | CW ratio | - | - | - | - | - | 0.15 | 0.15 | 0.18 | 0.21 | 0.24 |
| M2 | NT | 90 | 86 | 74 | 98 | 90 | 90 | 86 | 74 | 98 | 90 |
|  | CR | - | - | - | - | - | 2.29 | 1.53 | 1.34 | 1.75 | 1.59 |
|  | RR | 24.00 | 21.00 | 23.56 | 13.00 | 12.40 | 3.33 | 1.12 | 9.63 | 1.57 | 0.68 |
|  | TAC (USD/year) | 1.96E +06 | 2.44E +06 | 3.33E +06 | 2.86E +06 | 3.01E +06 | 1.73E +06 | 2.00E +06 | 2.73E +06 | 2.34E +06 | 2.21E +06 |
|  | Heat duty (kJ/h) | 2.05E +07 | 2.52E +07 | 4.05E +07 | 3.00E +07 | 3.33E +07 | 3.55E +06 | 2.52E +06 | 1.86E +07 | 5.64E +06 | 4.35E +06 |
|  | $\mathrm{CO}_{2}$ emiss (t/year) | 1.10E +04 | 1.36E +04 | 2.18E +04 | 1.62E +04 | 1.79E +04 | 1.91E +03 | 1.36E +03 | 9.29E +03 | 3.03E +03 | 2.34E +03 |
|  | CWcons (kg/h) | 8.45E +05 | 1.10E +6 | 1.78E +06 | 1.28E +06 | 2.35E +06 | 1.48E +05 | 1.10E +05 | 7.96E +05 | 2.20E +05 | 1.82E +05 |
|  | TAC ratio | - | - | - | - | - | 0.88 | 0.82 | 0.82 | 0.82 | 0.73 |
|  | Q ratio | - | - | - | - | - | 0.17 | 0.10 | 0.45 | 0.19 | 0.13 |
|  | $\mathrm{CO}_{2}$ ratio | - | - | - | - | - | 0.17 | 0.10 | 0.43 | 0.19 | 0.13 |
|  | CW ratio | - | - | - | - | - | 0.18 | 0.10 | 0.45 | 0.17 | 0.08 |
| M3 | NT | 94 | 94 | 78 | 102 | 90 | 94 | 94 | 78 | 102 | 90 |
|  | CR | - | - | - | - | - | 1.51 | 1.56 | 1.46 | 1.51 | 1.47 |
|  | RR | 22.30 | 15.70 | 13.20 | 7.44 | 7.00 | 2.10 | 0.83 | 2.55 | 0.43 | 0.12 |
|  | TAC (USD/year) | 2.00E +06 | 1.97E +06 | 2.41E +06 | 1.88E +06 | 2.08E +06 | 2.11E +06 | 2.13E +06 | 2.42E +06 | 2.04E +06 | 2.12E +06 |
|  | Heat duty (kJ/h) | 1.92E +07 | 1.97E +07 | 2.54E +07 | 1.86E +07 | 2.00E +07 | 2.64E +06 | 2.30E +06 | 6.38E +06 | 3.30E +06 | 3.01E +06 |
|  | $\mathrm{CO}_{2}$ emiss (t/year) | 1.05E +04 | 1.07E +04 | 1.30E +04 | 1.00E +04 | 1.09E +04 | 1.42E +03 | 1.23E +03 | 3.25E +03 | 1.8E +03 | 1.62E +03 |
|  | CWcons (kg/h) | 8.81E +05 | 8.41E +05 | 1.10E +06 | 7.93E +05 | 9.19E +05 | 1.12E +05 | 9.00E +04 | 2.66E +05 | 1.31E +05 | 1.26E +05 |
|  | TAC ratio | - | - | - | - | - | 1.06 | 1.08 | 1.00 | 1.09 | 1.02 |
|  | Q ratio | - | - | - | - | - | 0.14 | 0.12 | 0.25 | 0.18 | 0.15 |
|  | $\mathrm{CO}_{2}$ ratio | - | - | - | - | - | 0.14 | 0.11 | 0.25 | 0.18 | 0.15 |
|  | CW ratio | - | - | - | - | - | 0.13 | 0.11 | 0.24 | 0.17 | 0.14 |
| M4 | NT | 130 | 134 | 138 | 118 | 134 | 130 | 134 | 138 | 118 | 134 |
|  | CR | - | - | - | - | - | 1.50 | 1.34 | 1.56 | 1.38 | 1.51 |
|  | RR | 74.98 | 47.60 | 33.92 | 37.00 | 26.40 | 9.90 | 8.00 | 4.25 | 4.90 | 2.37 |
|  | TAC (USD/year) | 5.97E +06 | 5.26E +06 | 5.32E +06 | 7.26E +06 | 6.50E +06 | 5.10E +06 | 4.47E +06 | 5.68E +06 | 6.31E +06 | 5.52E +06 |
|  | Heat duty (kJ/h) | 6.34E +07 | 5.84E +07 | 7.22E +07 | 8.53E +07 | 6.95E +07 | 9.30E +06 | 1.09E +07 | 9.59E +06 | 1.31E +07 | 8.78E +06 |
|  | $\mathrm{CO}_{2}$ emiss (t/year) | 3.47E +04 | 3.16E +04 | 3.27E +04 | 4.61E +04 | 3.81E +04 | 5.00E +03 | 5.84E +03 | 4.89E +03 | 7.05E +03 | 4.72E +03 |
|  | CWcons (kg/h) | 2.93E +06 | 2.49E +06 | 2.75E +06 | 3.64E +06 | 3.44E +06 | 4.13E +05 | 4.60E +05 | 4.02E +05 | 5.52E +05 | 3.87E +05 |
|  | TAC ratio | - | - | - | - | - | 0.86 | 0.85 | 1.07 | 0.87 | 0.85 |
|  | Q ratio | - | - | - | - | - | 0.15 | 0.19 | 0.13 | 0.15 | 0.13 |
|  | $\mathrm{CO}_{2}$ ratio | - | - | - | - |  | 0.14 | 0.18 | 0.15 | 0.15 | 0.12 |
|  | CW ratio | - | - | - | - | - | 0.14 | 0.18 | 0.15 | 0.15 | 0.11 |

best HIDiC column for M4 uses $87 \%$ less energy, and its cost is $15 \%$ lower than the TAC of the conventional configuration.

As a summarized analysis of the discussion achieved above, the behavior of the TAC ratio and Q ratio as a function of feed composition is depicted through Figs. 7-10. We observe that the best relationship for TAC ratio and Q ratio is experienced in the composition of $0.75 / 0.25$ for the mixtures M2-M4. Notice that for the case M1 the optimal values for the TAC were obtained for feed compositions larger than 0.5 . However, larger energy savings were determined by the equimolar mixture.

Although the trends of Q ratio and TAC ratio undergo oscillation, the results allow determining that higher benefits are obtained in feed compositions larger than the equimolar composition, particularly for the feed composition of $0.75 / 0.25$ for most case studies. Thus, energy savings between 85 and $87 \%$ were determined for the mixtures M2-M4. Additionally,
the total annual cost varies from HIDiC designs with a TAC $27 \%$ lower to a TAC slightly larger ( $2 \%$ ) than the conventional sequence. In the case of M1, the optimal values of the TAC showed a reduction between 5 and $10 \%$ for compositions larger than 0.5 . The corresponding energy savings vary from 74 to $78 \%$. However, larger energy savings ( $84 \%$ ) were obtained for the equimolar mixture, whose cost is $2 \%$ lower than the TAC of the conventional design.

As a consequence of the large reductions in energy consumption obtained by HIDiC configurations under different feed compositions, the cooling water flow and the carbon dioxide emissions were considerably reduced. In fact, both cooling water consumption and carbon dioxide emissions were minimized by a similar percentage as energy consumption. Both reductions are a consequence of the influence of energy consumption on these variables. That is, when the reboiler duty decreases, the flow of hydrocarbons to be burned to fuel the

![img-5.jpeg](img-5.jpeg)

Fig. 7 - Behavior of the TAC ratio and the $Q$ ratio for variable feed composition of the mixture M1.
![img-6.jpeg](img-6.jpeg)

Fig. 8 - Behavior of the TAC ratio and the $Q$ ratio for variable feed composition of the mixture M2.
![img-7.jpeg](img-7.jpeg)

Fig. 9 - Behavior of the TAC ratio and the $Q$ ratio for variable feed composition of the mixture M3.
reboilers is lower. Thus, less carbon dioxide emissions are released. Similarly, if a lower amount of external energy to vaporize the mixture is used, the condenser duty becomes less. So, the water flow fed to the condenser decreases.

It is important to consider that the optimization of HIDiC columns with the strategy used becomes more difficult when the feed composition is different from the equimolar composition. The above is produced due to two reasons: problems of convergence of the simulations and difficulties to reach the purity required. This fact reveals the sensitivity of HIDiC
columns to the feed composition. Therefore, this is an additional reason why the study of several feed compositions using robust optimization algorithms is worthwhile.

On the other hand, the large benefits given by the HIDiC configurations reflect harnessing the operational characteristics of these columns. Table 4 shows some fundamental variables that support the good performance of these distillation sequences.

As it is known, the main variable that makes the operation of a HIDiC sequence possible is the compression ratio. As it

![img-8.jpeg](img-8.jpeg)

Fig. 10 - Behavior of the TAC ratio and the $Q$ ratio for variable feed composition of the mixture M4.

Table 4 - Variables that drive the performance of HIDiC columns.

| Mixture | Variable | Feed composition |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | 0.25/0.75 | 0.35/0.65 | 0.5/0.5 | 0.65/0.35 | 0.75/0.25 |
| M1 | CR | 1.87 | 1.88 | 1.76 | 1.64 | 2.18 |
|  | $\Delta \mathrm{T}_{\text {SR-SS }}$ (K) | 10.46 | 10.00 | 7.13 | 5.00 | 14.68 |
|  | VF (kmol/h) | $5.80 \mathrm{E}+02$ | $4.67 \mathrm{E}+02$ | $4.50 \mathrm{E}+02$ | $4.12 \mathrm{E}+02$ | $3.72 \mathrm{E}+02$ |
|  | Qcomp (kJ/h) | $1.57 \mathrm{E}+06$ | $1.22 \mathrm{E}+06$ | $1.15 \mathrm{E}+06$ | $8.71 \mathrm{E}+05$ | $1.24 \mathrm{E}+06$ |
|  | Qint (kJ/h) | $1.93 \mathrm{E}+07$ | $1.52 \mathrm{E}+07$ | $1.50 \mathrm{E}+07$ | $1.24 \mathrm{E}+07$ | $1.00 \mathrm{E}+07$ |
|  | $\mathrm{A}\left(\mathrm{m}^{3}\right)$ | $5.09 \mathrm{E}+02$ | $4.29 \mathrm{E}+02$ | $5.24 \mathrm{E}+02$ | $5.67 \mathrm{E}+02$ | $1.79 \mathrm{E}+02$ |
| M2 | CR | 2.29 | 1.53 | 1.34 | 1.75 | 1.59 |
|  | $\Delta \mathrm{T}_{\text {SR-SS }}$ (K) | 21.72 | 5.30 | 4.45 | 12.60 | 9.25 |
|  | VF (kmol/h) | $6.07 \mathrm{E}+02$ | $9.92 \mathrm{E}+02$ | $1.26 \mathrm{E}+03$ | $1.07 \mathrm{E}+03$ | $1.18 \mathrm{E}+03$ |
|  | Qcomp (kJ/h) | $2.25 \mathrm{E}+06$ | $1.88 \mathrm{E}+06$ | $1.70 \mathrm{E}+06$ | $2.65 \mathrm{E}+06$ | $2.41 \mathrm{E}+06$ |
|  | Qint (kJ/h) | $1.32 \mathrm{E}+07$ | $2.73 \mathrm{E}+07$ | $2.24 \mathrm{E}+07$ | $2.56 \mathrm{E}+07$ | $3.08 \mathrm{E}+07$ |
|  | $\mathrm{A}\left(\mathrm{m}^{3}\right)$ | $1.58 \mathrm{E}+02$ | $1.59 \mathrm{E}+03$ | $1.15 \mathrm{E}+03$ | $5.25 \mathrm{E}+02$ | $9.04 \mathrm{E}+02$ |
| M3 | CR | 1.51 | 1.56 | 1.46 | 1.51 | 1.47 |
|  | $\Delta \mathrm{T}_{\text {SR-SS }}$ (K) | 6.17 | 7.15 | 5.12 | 5.40 | 4.90 |
|  | VF (kmol/h) | $1.07 \mathrm{E}+03$ | $1.12 \mathrm{E}+03$ | $1.30 \mathrm{E}+03$ | $9.29 \mathrm{E}+02$ | $1.06 \mathrm{E}+03$ |
|  | Qcomp (kJ/h) | $2.01 \mathrm{E}+06$ | $2.26 \mathrm{E}+06$ | $2.39 \mathrm{E}+06$ | $1.74 \mathrm{E}+06$ | $1.85 \mathrm{E}+06$ |
|  | Qint (kJ/h) | $3.25 \mathrm{E}+07$ | $3.42 \mathrm{E}+07$ | $3.87 \mathrm{E}+07$ | $2.7 \mathrm{E}+07$ | $3.15 \mathrm{E}+07$ |
|  | $\mathrm{A}\left(\mathrm{m}^{3}\right)$ | $1.50 \mathrm{E}+03$ | $1.29 \mathrm{E}+03$ | $1.88 \mathrm{E}+03$ | $1.4 \mathrm{E}+03$ | $1.82 \mathrm{E}+03$ |
| M4 | CR | 1.50 | 1.34 | 1.56 | 1.38 | 1.51 |
|  | $\Delta \mathrm{T}_{\text {SR-SS }}$ (K) | 6.77 | 4.20 | 8.24 | 4.00 | 7.51 |
|  | VF (kmol/h) | $3.52 \mathrm{E}+03$ | $3.33 \mathrm{E}+03$ | $4.03 \mathrm{E}+03$ | $4.98 \mathrm{E}+03$ | $4.06 \mathrm{E}+03$ |
|  | Qcomp (kJ/h) | $6.54 \mathrm{E}+06$ | $4.44 \mathrm{E}+06$ | $8.58 \mathrm{E}+06$ | $7.34 \mathrm{E}+06$ | $7.62 \mathrm{E}+06$ |
|  | Qint (kJ/h) | $1.07 \mathrm{E}+08$ | $1.00 \mathrm{E}+08$ | $1.24 \mathrm{E}+08$ | $1.52 \mathrm{E}+08$ | $1.22 \mathrm{E}+08$ |
|  | $\mathrm{A}\left(\mathrm{m}^{3}\right)$ | $4.11 \mathrm{E}+03$ | $6.70 \mathrm{E}+03$ | $3.84 \mathrm{E}+03$ | $9.00 \mathrm{E}+03$ | $4.23 \mathrm{E}+03$ |

can be seen in Table 4, the optimal HIDiC sequences obtained use low values of compression ratio (1.34-2.29). Particularly, the compression ratio for most compositions of M3 and M4 were lower as compared to the CR for M1 and M2. Thus, larger temperature driving forces were experienced for most compositions of M1 and M2 in comparison with the other mixtures. This is a consequence of the increase in difficulties of the separation of the M3 and M4 mixtures.

Additionally, we observe that the compression duty is strongly dependent on the amount of vapor to be compressed and the compression ratio handled. Considering as an example the M1 mixture, we notice that the largest compressor duty was determined in the composition $0.25 / 0.75$. This value of compression duty is reasonable because the flow of vapor is the largest value and CR for this separation is a mean value in relation with the other compositions. However, we observe that despite the lowest vapor flow being determined in the composition $0.75 / 0.25$, the compressor duty for this feed com-
position was larger than the corresponding value for the other compositions, which operate with a larger vapor flow. This behavior is produced because the compression ratio is larger in this composition when compared to the CR for the other compositions. This fact ratifies that the compressor duty is a function of both the compression ratio used and the vapor flow. As may be noted in Table 4, a similar influence of VF and CR on the compression duty is experienced by the other case studies. Thus, a right balance between vapor flow and compressor ratio must be determined.

Furthermore, the generation of vapor in the stripping section is related to the amount of energy integrated. Table 4 shows that as we move from M1 to M4, the vapor flow to be compressed is augmented in most cases. This behavior evidences a progressive energy transfer requirement (from SR to SS) from M1 to M4.

As can be seen in Table 4, the average value of $\mathrm{Q}_{\text {int }}$ is about 15 million of $\mathrm{kJ} / \mathrm{h}$ for M1, and 22 million of $\mathrm{kJ} / \mathrm{h}$ for M2, while

the amounts of energy integrated for M3 and M4 are 34 and 118 million of $\mathrm{kJ} / \mathrm{h}$, respectively. This phenomenon is linked to the difficulties of separation as the relative volatility of the mixtures reduces. That is, at lower relative volatility, more energy-demanding traditional columns are obtained. However, as was established before, the energy integration is better harnessed by HIDiC configurations when the separation difficulties are increased.

The considerations previously discussed influence the size of heat exchange areas. As is widely known, the design of a heat exchanger depends on the quantity and quality of the energy to be exchanged. In the design of HIDiC sequences, both the source of energy and the quality are defined. For example, a simple approach is the integration of the equivalent amount of heat in the condenser, distributed along the stages of SR and SS. The corresponding quality is implicitly defined in the CR established and the temperature driving force allowed. These constraints are imposed in order to get economic and physically feasible heat exchange areas. Table 4 shows that the size of the heat exchange areas increases from M1 to M4. This is generated because the amount of energy integrated is largely increased from M1 to M4, as was explained previously. In addition, this behavior reflects the influence of the temperature driving forces obtained from each mixture. The size of the heat transfer areas varies from hundreds of square meters to about nine thousand square meters. The installation of these areas might be carried out taking into account the arrangements available. For example, large areas may be assembled as a compact heat exchanger or heat transfer panels. The areas of some hundreds of square meters might be configured as concentric columns or multitube exchangers.

## 7. Conclusions

The design and optimization of heat-integrated distillation columns with variable feed composition using a Boltzmannbased estimation of distribution algorithm as optimizer were performed. The results show that the optimization strategy led to the best values of the fitness function through an intensified search. It was evident that the fitness function enhanced as the function evaluations number increased. Besides, it was ratified that the compression undergoes less variation when compared with the reflux ratio among the compositions of each mixture. So, the TAC showed a more uniform trend than the energy consumption. In addition, results showed large energy savings of the HIDiC regarding the conventional column for all mixtures. Nonetheless, larger energy savings and more favorable TAC for compositions other than the equimolar for most of the mixtures were determined. The detailed analysis disclosed that the best compromise between energy consumption and TAC for the mixtures with a feed composition of $0.75 / 0.25$ for most case studies. Thus, energy savings between 85 and $87 \%$ were determined. At the same time, the TAC of the HIDiC varied since reductions of $27 \%$ to a TAC slightly larger ( $2 \%$ ) than the conventional sequence. As a consequence of the energy savings, similar reductions of cooling water and carbon dioxide emissions were obtained. Based on these results, the evaluation of multiple feed compositions allowed us to determine a large energetic and economic potential of the HIDiC. This fact ratified the worth of the examination of several feed compositions of the mixtures by using robust optimization strategies.

The results obtained showed the generalized behavior of HIDiC sequences as a function of feed composition. To translate this theoretical study toward industrial application requires evaluation. However, the results presented in this work give a guide to the probable behavior and benefits obtained in the application of HIDiC columns in a further particular experimental or industrial case.

On the other hand, the feed flow used in this work was $100 \mathrm{kmol} / \mathrm{h}$. This is a typical value to perform simulation and optimization studies. The optimization of this variable is out of goals of this study. Nevertheless, as was shown in a related work (Nakaiwa et al., 2003), this variable considerably influences the performance of HIDiC configurations in the separation of a binary mixture. In fact, it was determined that the HIDiC columns loss their economic advantages regarding the traditional columns when the feed flow is larger than $230 \mathrm{kmol} / \mathrm{h}$. This behavior is caused due to two reasons: (a) increasing energy demands and (b) the electricity used in the compressor is several times more expensive than the heating steam. Thus, the inclusion of this variable in the optimization of HIDiC configurations in further studies is worthwhile.

## Acknowledgement

The authors acknowledge the financial support provided by PRODEP México.

## References

Aso, K., Matsuo, H., Noda, H., Takada, T., Kobayashi, N. (1996/1998). Heat integrated distillation column, US Patent 5,783,047.
Bonilla-Petriciolet, A., Pandu Rangaiah, G., Segovia-Hernández, J.G., 2011. Constrained and unconstrained Gibbs free energy minimization in reactive systems using genetic algorithm and differential evolution with tabu list. Fluid Phase Equilib. 300, 120-134.
Bonilla-Petriciolet, A., Pandu Rangaiah, G., Segovia-Hernández, J.G., 2010. Evaluation of stochastic global optimization methods for modeling vapor-liquid equilibrium data. Fluid Phase Equilib. 287, 111-125.
Caballero, J.A., Grossmann, I.E., 1999. Aggregated models for integrated distillation systems. Ind. Eng. Chem. Res. 38, 2330.
Gadalla, M.A., Olujić, Ž., Jansens, P.J., Jobson, M., Smith, R., 2005. Reducing $\mathrm{CO}_{2}$ emissions and energy consumption of heat-integrated distillation systems. Environ. Sci. Technol. 39, 6860-6870.
Govind, R., 1987. Dual distillation columns. US patent 4, 681, 661. Gómez-Castro, F.I., Segovia-Hernández, J.G., Hernández, S., Gutiérrez-Antonio, C., Briones-Ramírez, A., Gamiño-Arroyo, Z., 2015. Design of non-equilibrium stage separation systems by a stochastic optimization approach for a class of mixtures. Chem. Eng. Proc. 88, 58-69.
Guthrie, K.M., 1974. Process Estimating Evaluation and Control. Craftsman Book Co., Solana Beach, CA.
Gutiérrez-Antonio, C., Briones-Ramírez, A., 2010. Speeding up a multiobjective genetic algorithm with constraints through artificial neuronal networks. Comput. Aided Chem. Eng 28, 391-396.
Gutiérrez-Guerra, R., Murrieta-Dueñas, R., Cortez-González, J., Segovia-Hernández, J.G., Hernández, S., Hernández-Aguirre, A., 2016. Design and optimization of HIDiC columns using a constrained Boltzmann-based estimation of distribution algorithm-evaluating the effect of relative volatility. Chem. Eng. Proc. 104, 29-42.
Gutiérrez-Guerra, R., Cortez-González, J., Murrieta-Dueñas, R., Segovia-Hernández, J.G., Hernández, S., Hernández-Aguirre, A., 2014. Design and optimization of heat-integrated distillation column schemes through a new robust

methodology coupled with a Boltzmann-based estimation of distribution algorithm. Ind. Eng. Chem. Res. 53, 11061-11073.
Harwardt, A., Kraemer, K., Marquardt, W., 2010. Identifying optimal mixture properties for HIDiC application. Proc. Distillation Absorption, 55-60.
Humphrey, J.L., 1995. Separation processes: playing a critical role. Chem. Eng. Prog. 91, 31-41.
Iwakabe, K., Nakaiwa, M., Huang, K., Nakanishi, T., Røsjorde, A., Ohmori, T., 2006. Performance of an internally heat-integrated distillation column (HIDiC) in separation of ternary mixtures. J. Chem. Eng. Jpn. 39, 417-425.

Jana, A.K., Mali, S.V., 2010. Analysis and control of a partially heat integrated refinery debutanizer. Comput. Chem. Eng. 34, 1296-1305.
Kiss, A.A., Olujić, Ž., 2014. A review on process intensification in internally heat-integrated distillation columns. Chem. Eng. Proc. 86, 125-144.
Lopez-Saucedo, E.S., Grossmann, I.E., Segovia-Hernández, J.G., Hernández, S., 2016. Rigorous modeling, simulation and optimization of a conventional and nonconventional batch reactive distillation column: a comparative study of dynamic optimization approaches. Chem. Eng. Res. Des. 111, 83-99.
Nakaiwa, M., Huang, K., Endo, A., Ohmori, T., Akiya, T., Takamatsu, T., 2003. Internally heat-integrated distillation columns: a review. Trans. IChemE 81, 162-177.
Nakaiwa, M., Huang, K., Naito, K., Endo, A., Akiya, T., Nakane, T., Takamatsu, T., 2001. Parameter analysis and optimization of ideal heat integrated distillation columns. Comput. Chem. Eng. 25, 737-744.
Nakaiwa, M., Huang, K., Owa, M., Akiya, T., Nakane, T., Sato, M., Takamatsu, T., 1997. Energy savings in heat-integrated distillation columns. Energy 22, 621-625.

Nakanishi, T., Adachi, N., Aso, K., Iwakabe, K., Matsuda, K., Hourichi, K., Nakaiwa, M., Takamatsu, T., 2008. Development of a high performance distributor for an internally heat-integrated distillation column. Kagaku Kogaku Ronbunshu 34, 224-229.
Noda, H., Mukaida, T., Kaneda, M., Kataoka, K., Nakaiwa, M., 2006. Internal column-to-column heat transfer characteristics for energy-saving distillation system. Distillation and Absorption, 737-744.
Olujić, Ž., Sun, L., De Rijke, A., Jansens, P.J., 2006. Conceptual design of an internally heat integrated propylene-propane splitter. Energy 31, 3083-3096.
Rodrigues, W.L., Mattedi, S., Abreu, J.C.N., 2005. Experimental vapor-liquid equilibria data for binary mixtures of xylene isomers. Chem. Eng. Braz. 22 (03), 453-462.
Seader, J.D., Henley, E., 2006. Separation Process Principles. John Wiley and Sons, New York.
Segovia-Hernández, J.G., Hernández, S., Bonilla Petriciolet, A., 2015. Reactive distillation: a review of optimal design using deterministic and stochastic techniques. Chem. Eng. Proc. 97, 134-143.
Shahandeh, H., Ivakpour, J., Kasiri, N., 2014. Internal and external HIDiCs (heat-integrated distillation columns) optimization by genetic algorithm. Energy 64, 875-886.
Smith, E.M.B., Pantelides, C.C., 1995. Design of reaction/separation networks using detailed models. Comput. Chem. Eng. 19, S83.
Turton, R., Bailie, R.C., Whiting, W.B., Shaeiwitz, J.A., 2004. Analysis Synthesis and Design of Chemical Process, 2nd edition. Prentice Hall, USA.
Valdez, S.I., Hernandez, A., Botello, S., 2013. A Boltzmann based estimation of distribution algorithm. Inf. Sci. 236, 126-137.