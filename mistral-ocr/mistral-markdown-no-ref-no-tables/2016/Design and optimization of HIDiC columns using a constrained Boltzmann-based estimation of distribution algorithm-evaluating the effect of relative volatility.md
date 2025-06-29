# Design and optimization of HIDiC columns using a constrained Boltzmann-based estimation of distribution algorithm-evaluating the effect of relative volatility 

Roberto Gutiérrez-Guerra ${ }^{\mathrm{a}, \mathrm{c}, *}$, Rodolfo Murrieta-Dueñas ${ }^{\mathrm{b}, \mathrm{c}}$, Jazmin Cortez-González ${ }^{\mathrm{b}, \mathrm{c}}$, Juan Gabriel Segovia-Hernández ${ }^{\mathrm{c}}$, Salvador Hernández ${ }^{\mathrm{c}}$, Arturo Hernández-Aguirre ${ }^{\mathrm{d}}$<br>${ }^{a}$ Universidad Tecnológica de León, Campus I, Área de sustentabilidad para el desarrollo, Blvd. Universidad Tecnológica 225,Col. San Carlos, 37670 León, Guanajuato, Mexico<br>${ }^{\mathrm{b}}$ Instituto Tecnológico Superior de Guanajuato, Departamento de Cómputo Evolutivo Aplicado, Carretera Guanajuato-Puentecillas km 10.5, 36262 Guanajuato, Guanajuato, Mexico<br>${ }^{\text {c }}$ Universidad de Guanajuato, Campus Guanajuato, Departamento de Ingeniería Química, Noria Alta s/n, 36050 Guanajuato, Guanajuato, Mexico<br>${ }^{\mathrm{d}}$ Centro de Investigación en Matemáticas, A.C., Departamento de Computación, A.P. 402, Guanajuato, Guanajuato CP 3600, Mexico

## A R T I C L E I N F O

Article history:
Received 3 October 2015
Received in revised form 23 January 2016
Accepted 13 February 2016
Available online 16 February 2016

Keywords:
Distillation
HIDiC
Optimization
Boltzmann distribution
Energy savings
TAC

## A B STR A C T

In this paper we study the design and optimization of heat-integrated distillation columns (HIDiC) using a constrained Boltzmann-based estimation of distribution algorithm. The total annual cost was defined as the fitness function of the problem, and the effect of the relative volatility on the performance of the HIDiC configurations was evaluated.

We analyzed a set of equimolar mixtures with relative volatility varying from 1.12 to 2.4. The designoptimization strategy implemented was executed through Matlab-Excel-Aspen Plus ${ }^{\circledR}$ interface.

The results showed that the best interrelation between energy savings and TAC of the HIDiC columns were obtained in the separation of mixtures with relative volatilities between 1.12 and 1.5, particularly for mixtures of isomers. As a result, energy savings from 50 to $87 \%$ were obtained for this class of mixture. At the same time, we obtained HIDiC sequences with TACs lower than that TAC of conventional columns (2-16\%). Nevertheless, we found that the TAC of some HIDiC schemes resulted higher than the TAC of conventional columns (6-17\%). In addition, carbon dioxide emissions released into the atmosphere were reduced in the same proportion as savings in energy required to fuel the reboilers.
(c) 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

The world energy crisis derived from the exhaustion of petroleum and the phenomena of global warming are demanding more efficient and cleaner chemical processes.

It is well known that distillation is an energy intensive consumer in the chemical industry. At the same time, during the operation of distillation columns large amounts of carbon dioxide are released, produced from the fuels burned to obtain the energy used in the reboiler. Heat Integrated Distillation Column (HIDiC) is one of the technologies that claim to reduce energy consumption in distillation processes, especially in the separation

[^0]of close boiling mixtures. In addition, the implementation of this technology pursues reducing carbon dioxide emissions and improving the TAC of this fundamental separation process. The rectifying section is separated from the stripping section in the conventional sequence shown in Fig. 1, to give the HIDiC configuration observed in Fig. 2. Both sections (SR and SS) are connected each other using a compressor, a throttling valve and material streams. The compressor increases the pressure and temperature of SR, which makes possible the energy integration $\left(Q_{\text {int }}\right)$ from SR to SS.

This operational principle leads using the energy more efficiently in the HIDiC than a conventional configuration. For instance, the separation of a mixture made of benzene and toluene uses $70 \%$ of the energy required by a traditional column [1]. Besides, the separation of some ternary mixtures made of benzene, toluene, and $p$-xylene and $n$-pentane, cyclopentane, and 2methylheptane, resulted in energy savings of $30 \%$ and $50 \%$ [2]. Later, the separation of aromatics (benzene-toluene-p-xylene) via


[^0]:    * Corresponding author at: Universidad Tecnológica de León, Campus I, Área de sustentabilidad para el desarrollo, Blvd. Universidad Tecnológica 225,Col. San Carlos, 37670 León, Guanajuato, Mexico.

    E-mail addresses: rogutierrez@utleon.edu.mx, uranio_bz@hotmail.com (R. Gutiérrez-Guerra).

extractive distillation was investigated through a comparison between the conventional column, the HIDiC sequence and the Pettyuk column [3].The results revealed larger energetic benefits for the HIDiC scheme in relation with the other configurations. In addition, an energetic, economic and control analysis on a partially heat integrated refinery debutanizer (HIDBC) through a sensitivity analysis was achieved [4]. The results showed energy savings of $44 \%$, and the total annual cost was $14 \%$ lower than its conventional counterpart. Besides, the control strategy implemented was able to properly reject the disturbances imposed on the HIDBC. Likewise, it was performed the optimization of HIDiC columns used in the separation of several close boiling hydrocarbon binary mixtures via MINLP optimization [5]. Results disclosed that the HIDiC sequence is more energetically and economically favorable using mixtures with low relative volatility.

Furthermore, an optimization study of HIDiC schemes using genetic algorithms was achieved [6]. The separation of the mixture made of benzene and toluene was used as a study case. Results showed up to $6.60 \%$ and $9.75 \%$ TAC reduction in external and internal HIDiC optimization using the proposed method.

Recently, we achieved a study of design and optimization of HIDiC columns using a constrained Boltzmann-based estimation of distribution algorithm [7]. The algorithm called Boltzmann Univariate Marginal Distribution algorithm (BUMDA) was adapted to use both continuous and discrete variables. In addition, a truncation method and a reset mechanism were attached to it. The design-optimization strategy was executed by using the Matlab-
![img-0.jpeg](img-0.jpeg)

Fig. 1. Conventional sequence.
Excel-Aspen Plus interface. Rigorous simulations were performed in Aspen Plus ${ }^{\circledR}$ by using the RadFrac model. We evaluated the design and optimization strategy by considering the separation of three binary mixtures: n-butanol/isobutanol (M1), n-heptane/ cyclohexane (M2) and benzene/toluene (M3). The TAC was defined as the fitness function of the problem, whereas the constraints established were: purity, recovery and temperature driving force between rectifying and striping sections. The optimization process was carried employing 60 individuals and 50 generations. Two goals were underlined: (1) To evaluate the performance of the BUMDA to deal multivariable problems using rigorous modeling and (2) To determine energy savings and the best TAC possible for the HIDiC.

The results showed that the optimization algorithm carried out an intensified search for the optimal HIDiC designs. It was evident that the Boltzmann distribution and the truncation method led the exploration toward the best search region. In addition, we observed that the reset mechanism was frequently activated and refined solutions were obtained.
![img-1.jpeg](img-1.jpeg)

Fig. 2. HIDiC configuration.

Additionally, compared with the conventional designs, following results were obtained: (a) energy savings of the best HIDiC for the mixture M1 was $84 \%$, whereas the reduction of the total annual cost was $2 \%$. (b) The best HIDiC designs in the cases M2 and M3 showed energy savings of $62.5 \%$ and $52.5 \%$, respectively. In addition, the total annual cost of the HIDiC was $32 \%$ larger for M2 and $35 \%$ higher for M3.

Through analysis carried out, it is clear that BUMDA algorithm was able to deal successfully the optimization of the HIDiC sequences. Consequently, large energy savings and the best possible condition for the TAC were determined.

Under these findings, the search for enhancements for energy savings and TAC through the evaluation of mixtures properties is required. Thus, the challenge in this study is the assessing the effect of relative volatility of the mixtures on energy savings and TAC of HIDiC sequences, using BUMDA algorithm as optimizer.

## 2. Optimization strategies

Chemical processes optimization has been frequently addressed via two major approaches, the deterministic approach [5], [8], [9], [10], [11] and the stochastic approach [6], [7], [12], [13]. Algorithms based on the deterministic approach guarantee the global optimality of the obtained solution, but the modeling of the process is usually subject to simplifications. Algorithms based on the stochastic approach, which do not guarantee global optimality, are applicable to complete modeling, but can be inefficient due to the high numerical effort that is frequently required.

In this work, stochastic algorithms to perform the optimization were used. Through these methods a set of optimal solutions are obtained and the modeling of a multimodal function (fitness function) is conveniently treated as a black box by using of the process Simulator Aspen Plus ${ }^{\circledR}$.

Among the most common stochastic algorithms implemented to optimize chemical processes, we may find Genetic algorithms [6], [14], [16], Simulated Annealing [13], [17], Differential evolution [12], [18], [19], Harmony Search [20], dual algorithms [21], Boltz-mann-based estimation of distribution algorithms [7], [22], [23], among others.

Particularly, the stochastic algorithm called Boltzmann Univariate Marginal Distribution Algorithm (BUMDA) [23] is a robust strategy to optimize complex problems. This algorithm has been used to optimize diverse benchmark problems (Rosembroock, Sphere, Greenwark). The comparison with other stochastic methods (EMMA, UMDA) revealed that the BUMDA algorithm is a competitive option in terms of robustness and efficiency. Later, the performance of BUMDA was compared to genetic algorithms to optimize a distillation columns train [22]. The results indicated that the value of the fitness function (total annual cost) was minimized to a larger degree compared with the TAC determined by NSGAII. In addition, the computing time utilized by the BUMDA algorithm was below in relation to the other strategy.

Also, in a preceding work [7], the BUMDA algorithm was used to optimize heat-integrated distillation columns (HIDiC). The separation of several binary close boiling mixtures took place. The compression ratio, reflux ratio and total number of stages were
![img-2.jpeg](img-2.jpeg)

Fig. 3. Flow sheet for BUMDA algorithm.

used as optimization variables, while the TAC was established as the fitness function of the problem. In addition, the constraints of the problem were: purity, recovery and temperature driving force between SR and SS.

The results showed the intensive search promoted by the Boltzmann distribution, the truncation method and the reset mechanism. Moreover, the constraints established were preserved into the limits defined. Therefore, optimal HIDiC designs with large energy savings and the best condition possible of the TAC was determined.

### 2.1. Fundamentals of the Boltzmann distribution

As described in detail in previous studies [7], [22], the Boltzmann distribution is characterized by its continuous approximation to the fitness function $(g(x))$ through the probability model $(P(x))$ shown in Eq. (1). Thus, the algorithm makes the localization of the best values of the fitness function possible.
$P(x)=\frac{\exp ^{j g(x)}}{Z}$
The variable $Z$ included in Eq. (1) represents the assessing of the summation of the exponential function of the numerator on the whole search domain, as observed in Eq. (2).
$P\left(x_{i}\right)=\frac{\exp ^{j g\left(x_{i}\right)}}{\sum_{i} \exp ^{j g(x)}}$
Under these fundamentals, the BUMDA algorithm starts with the definition of the population size $\left(P_{0}\right)$ based on a normal distribution. Afterward, the exploration takes place within defined search parameters. During the processing, the algorithm approximating the optimal value via Kullback-Leibler divergence (KLD) and the evaluation of several parameters $(\mu, v, T, \beta)$.

Where $\mu$ and $v$ represent the mean and variance of the population, respectively, whereas $T$ is defined as a temperature and $\beta$ is a parameter that influences the selection pressure and the variance in the population.

As mentioned, a reset mechanism and a truncation method were attached to this algorithm. The reset mechanism activates when the fitness function value remains unchangeable in a determined number of functions. On the other hand, the truncation method is applied to limit the population to its best individuals. In this case, half of the population was selected.

In general terms, the Boltzmann distribution and truncation method guide the search, whereas reset mechanism performs an intensified exploration to find the best solutions.

The execution of the BUMDA algorithm is depicted in Fig. 3, which is described below:

1.     - Generation of the initial population $\left(P_{0}\right)$ using a normal distribution
2.     - Evaluation of the fitness function (TAC) of the population $\left(P_{0}\right)$
3.     - Comparison of the fitness function of the population
4.     - Selection of the best individuals
5.     - Generation of next population $\left(P_{1}\right)$ by using the fitness function of the best individual.

This cycle is repeated while the current function evaluations number is lower than the maximum function evaluations number defined.

Supported by the robustness shown in the previous studies [7], [22], BUMDA algorithm was implemented in the present study as optimizer of HIDiC sequences, evaluating the effect of relative volatility on energy savings and TAC of these configurations.

Table 1
Case study.
## 3. Case study

In this work, a set of equimolar mixtures of low relative volatility was selected, such as it is shown in Table 1. This range was chosen considering the important benefits of the HIDiC reported in the preceding study [7]. Besides, for each case study, a feed rate of $100 \mathrm{kmol} / \mathrm{h}$ of saturated liquid was used.

The thermodynamic model of Chao-Seader was used to simulate the cases M1-M3, M5 y M6. Moreover, the cases M7 and M9 were simulated with the UNIQUAQ model. In addition, the NRTL model was utilized to simulate the cases M4 and M8. Chao-Seader model was employed for the corresponding mixtures because these mixtures were made up of hydrocarbons [25], and they are relatively easy to separate. Furthermore, the UNIQUAQ model was used to represent the separation of the mixture of isomers, M9 [26]. On the other hand, the NRTL model was engaged to carry out the separation the mixtures indicated in agreement with the recommendations obtained from literature [25].

The targets for both purity and recovery were established as 0.995 , mol fraction. Likewise, the temperature driving force defined between SR and SS was found to be at least 1.67 K . The minimum compression ratio between SR and SS was defined as 1.1, and the pressure drop allowed was defined as 0.3 kPa , such as it has been employed in other studies [4], [7], [27].

Furthermore, the election of the minimum temperature driving force was based on the behavior of the temperature profiles between SR and SS, the amount of energy integrated and the heat transfer areas computed. That is, along the optimization process, both purity and recovery must be adjusted to the target established. Therefore, both reflux ratio and amount of energy integrated are constantly varying. Consequently, that is translated into a continuous variation of temperature profiles. Hence, after carry out some simple trials to determine a convenient $\Delta T_{\text {SR-SS-min }}$, 1.67 K represented a favorable value to get considerable energy integration and reasonable heat transfer areas when both purity and recovery have been reached.

Equally than in the recent study [7], in this work both the conventional sequence and the HIDiC sequence have the same total number of stages. Similarly, both rectifying and stripping sections have the same number of stages $\left(N_{\mathrm{SS}}=N_{\mathrm{SR}}=\mathrm{NT}(2)\right.$. This was done to explore the behavior of these configurations by evaluating the energy transference stage-by-stage at the same level of the column by using robust optimization strategies. Thus, the feed stream is introduced on the top stage of the stripping section.

## 4. Problem statement

The goal in this study is the minimization of the total annual cost, which represents the fitness function of the problem. It is showed in Eq. (3).
$\operatorname{Min} .(\mathrm{TAC})=f(\mathrm{NT}, \mathrm{CR}, \mathrm{RR})$

Subject to
$X_{\text {purity }}=X_{\text {recovery }}=0.995 \pm \delta ; \delta=0.0003 ; \Delta T_{\text {SR-SS }} \geq 1.67 \mathrm{~K}$
The compression and reflux ratios are the continuous variables of the problem. Meanwhile, the total stage number is the integer variable used in the optimization. Notice that constraints of the problem are given by the purity, recovery and temperature driving forces between SR and SS. In the model presented, we may observe that both purity and recovery are defined as inequality constraints, which were transformed into equality constraints by using a tolerance ( $\delta$ ) of 0.0003 . On the other side, the value for $\Delta T_{\text {SR-SS }}$ was constrained to be at least 1.67 K . The constraint for $\Delta T_{\text {SR-SS }}$ is indirectly considered into the CR.

The optimization variables were selected because of their influence on the energetic and economic behavior of this separation processes.

Through these variables we may determine the most convenient balance between economy and energy consumption. That is, such an interrelation is traduced in the amount and quality of the energy to be integrated and whose effect is reflected in the energy savings and the TAC.

On the other hand, the value of $\delta$ was established after doing several simple trials with different values. So, the value established led to a reasonable numerical effort and favorable behavior of the fitness function along the optimization process.

The limits of the optimization variables are shown in Table 2.
The lower limit for the total number of stages was obtained from the simulation by using shortcut method of Fenske-Underwood-Gilliland. In addition, the upper limit of the total number of stages was allowed to vary forty more stages in relation with the lower limit. On the other hand, the limits for compression ratio were established based on results recently reported [7]. Such results showed that the most favorable balance between energy consumption and TAC are obtained in HIDiC sequences whose compression ratios are larger than 1 and below 3. Nevertheless, considering the strong influence of CR on the TAC and energy savings, we defined a wider exploration range, from 1.1-10 for M1M5 and from 1.1-5 for the cases M6-M9. Particularly, the lower range (1.1-1.5) was selected due to convergence problems presented in the simulations when a superior CR is used. These limits allowed us to achieve an intensive search for the best solution carried out by the BUMDA algorithm [7].

At the same time, the reflux ratio was defined by performing a similar analysis to that done in the former studio [7]. In the first approximation, the lower limit of RR was determined by taking the RR obtained in the simulation of the column with an upper limit at a total number of stages. Similarly, the upper limit of RR was established using the values obtained in the simulation of the column with the lower limit at total stage number. Notice that RR was taken from the simulation when the purity was reached. Hereafter, some optimization trials of the HIDiC were performed using these initial limits. Results revealed that both energy savings

Table 2
Limits of optimization variables.
and TAC could be improved further. Thus, we decided to increase both limits of RR. The results after the increase led to better outcomes in terms of energy savings and TAC for the HIDiC in relation to the conventional sequence.

On the other hand, the evaluation of the fitness function used in the optimization (TAC) is carried out via Guthrie's method [28], considering 8000 operation hours per year. The fitness function is evaluated through the summation of operation costs plus the capital costs.

The costs of utilities were defined as follows [29], [30]: electricity: $0.1 \mathrm{USD} / \mathrm{kWh}$, steam: $0.016 \mathrm{USD} / \mathrm{kg}$ and cooling water: $0.0148 \mathrm{USD} / \mathrm{m}^{3}$.

The capital cost was computed assuming the costs of the compressor, heat transfer areas per stage, heat exchangers (reboilers and condensers), and columns shells. In addition the global heat transfer value $(U)$ used for sizing both transfer areas and the reboiler was established as $200 \mathrm{Btu} / \mathrm{hft}^{2} \cdot \mathrm{~F}\left(4085.62 \mathrm{~kJ} /\right.$ $\mathrm{hm}^{2} \mathrm{~K}$ ). On the other hand, the global heat transfer for the condenser was defined as $150 \mathrm{Btu} / \mathrm{hft}^{2} \cdot \mathrm{~F}\left(3064.22 \mathrm{~kJ} / \mathrm{hm}^{2} \mathrm{~K}\right)$. The values for both global heat transfer coefficients employed are common values found in the literature to design condensers and reboilers [30]. In addition, the evaluation of carbon dioxide emissions was carried out using the model presented by Gadalla et al. [31]. The total energy used by HIDiC configuration is given by the reboiler duty plus compressor duty, which is defined as $\mathrm{Q}_{\text {cons-HIDiC. }}$ In addition, the thermodynamic efficiency was determined through the model reported by Seader and Henley, 1998 [32].

Additionally, the heat to be integrated is the heat duty of the condenser of the rectifying section. This election was established because the SR operates at a higher pressure than the stripping column. On the other side, the model used to compute the quantity of energy to be integrated by stage, is given by Eq. (4) [33].
$\mathrm{Q}_{\mathrm{i}}=\Delta T_{\text {SRi-SSi }}\left(\frac{\mathrm{Q}_{\mathrm{T}}}{\sum_{i=1}^{n} \Delta T_{\text {SRi-SSi }}}\right)$
Similarly, the heat transfer area by stage and the total area are given by Eqs. (5) and (6) respectively [33].
$A_{i}=\left(\frac{Q_{i}}{U \Delta T_{\text {SRi-SSi }}}\right)$
$A_{i}=\sum_{i=1}^{n} A_{i}$
where $i$ represents the corresponding stage and n is the total stages number.

Observe that the temperature driving force used in this study is given by the difference of temperature between SR and SS. This approach is frequently employed to design HIDiC columns [33], [34]. Based on the design-optimization strategy implemented in this study, both temperatures are known and directly obtained from the simulator Aspen Plus. Therefore, were used them for sizing the heat exchange areas. The evaluation of the Logarithmic Mean Temperature Difference (LMTD) was not performed since the outlet temperatures were not evaluated after heat exchanging between SR and SS. However, the current approximation is considered reasonable because the design of the HIDiC is supported on the fundamental thermodynamic principle, i.e. the existence of temperature driving forces between SS and SR. As it was explained before, this condition is met because SR operates at higher pressure than SS.

On the other side, the determining LMTD will give the guidelines to establish the physical configuration of the heat exchange areas. For instance, it might be designed as a concentric configuration, where rectifying section is placed within stripping section or an external heat transfer panel may be designed to get the goal. If the available space between SS and SR is enough to place the heat exchange area, the heat exchange will be achieved within the column. Otherwise, the heat transfer area will be placed as an external heat exchanger panel [34].

## 5. Methodology

As determined in the preceding study [7], the methodology implemented showed a robust performance through the evaluation of several amounts of energy integrated between SR and SS on a same design. Thus, we used the same methodology in this study.

By application of this methodology, each individual (HIDiC design) generated by BUMDA algorithm is evaluated as follows:

1. Introduce the value of optimization variables (NT, CR and RR) in the Radfrac model of the HIDiC in the simulator Aspen Plus. Here, $Q_{\text {int }}=0$.
2. Simulate the HIDiC configuration.
3. If the convergence of the simulation is false, to assign automatically TAC $=1 \mathrm{E}+09$ and evaluate next individual (go to 1). Else, go to 4.
4. Determine the temperature driving forces and the amount of energy to be integrated by stage.
5. If the minimum temperature driving force is below 1.67 K , increase CR and go to 1 to update CR. Otherwise, go to 6.
6. Simulate the heat-integrated HIDiC.
7. If the convergence of the simulation is false, to assign automatically TAC $=1 \mathrm{E}+09$ and evaluate next individual (go to 1). Else, go to 8 .
8. Evaluate the constraints by using the results of the simulation
9. If the constraints are accomplished, compute TAC and go to 11. Otherwise, go to 10.
10. If the set of constraints is out of the established tolerance, manipulate both RR and $Q_{i}$ and execute the simulation. This point is repeated until constraints have been satisfied or when 10 internal evaluations have been achieved. Thereafter, compute and penalize TAC (see Fig. 4) and go to 11.
11. Store and sort the current individuals evaluated
12. Return to 1 to evaluate next individual

Once all individuals of the current generation have been evaluated, the next generation is produced, as indicated in the flow

```
% evaluate individual (HIDiC design) in Aspen Plus
if convergence is false then
    TAC=1E+09
else
    % compute TAC
    TAC= COP + CC
    %penalize TAC
    if abs(0.995 - X
    w
    TAC = f*(0.995 - X
    end
    if abs(0.995 - X
    w
    TAC = recovery**TAC
    end
    % compute TAC penalized by purity and recovery
    TAC
    % compute TAC penalized by number of constraints violated
    if number of constraints violated > 0 then
    TAC
    else
    TAC
    end
end
```

Fig. 4. Penalization strategy used in the optimization process of the HIDiC.

![img-3.jpeg](img-3.jpeg)

Fig. 5. HIDiC design assembled in Aspen Plus.
sheet shown in Fig. 3. Observe that this processing is repeated while NumEval $<$ NumEvalMax.

In addition, based on the results obtained in the precedent work [7], in this study we implemented the same penalization strategy. As defined, the BUMDA algorithm uses a constraint-handling method based on function penalization and the sum of constraint violations, as shown in Fig. 4.

The first criteria to penalize each individual (HIDiC design) is the convergence of the simulation. If the simulation does not converge, a relatively large TAC $(1 \mathrm{E}+09)$ is automatically assigned. Otherwise, if the simulation reached successful convergence, the TAC is evaluated and the penalization due to the purity, recovery, and a number of penalizations takes place. Observe that depending of the deviation of such constraints, the TAC is increased proportionally.

The weight factors ( $W_{\text {purity }}, W_{\text {recovery }}, W_{\text {num_pen }}$ ) and the factor $f$ were conveniently chosen to contribute to an effective guidance toward good values of the fitness function. The selection was carried out by doing several essays, taking as a reference the behavior of the fitness function. After a number of trials performed, a value of 10 was established for $f$. Thus, by using the targets established ( 0.995 ) together the purity and recovery obtained from simulations, the weight factors $W_{\text {purity }}$ and $W_{\text {recovery }}$ were determined. On the other side, the weight factor $W_{\text {num_pen }}$ was chosen as a function of number of penalizations unaccomplished. For instance, if the purity and recovery of both components are within the tolerance defined, there are four constraints
accomplished and $W_{\text {num_pen }}=0$. Otherwise, if both purity and recovery are out of the tolerance, there exist four constraints violated, and $W_{\text {num_pen }}=30$. In a similar way than the factor $f$, the evaluation of several values was performed to define the factor $W_{\text {num_pen }}$.

The representative HIDiC design to separate a feed into a distillate product and a bottom product in Aspen Plus is shown in Fig. 5 .

This diagram is obtained by using the RadFrac model to represent both the rectifying and stripping sections. In this configuration, each stream (e.g. Q1-Q5) represents the heat transferred from SR (source) to SS (sink). This heat transfer is generated by the operation of the compressor and the throttling valve under adequate conditions.

In thermodynamic terms, the heat transference between SR and SS depends on both quantity and quality of the energy in columns. The quantity of energy represents the amount of heat available in the source and the quality is given by the level of temperature of this. During the execution of the designoptimization strategy implemented in this study, a heat flow is transferred from SR to SS. The simulation of each individual involves a material and energy balance, which is internally performed. As we can see, this balance considers both liquid and vapor flows within the column, which is influenced by quantity and quality of the energy involved in the system. The variation of liquid and vapor flows along the SR and SS sections have been described in several studies [7], [35]. Results showed an increasing
![img-4.jpeg](img-4.jpeg)

Fig. 6. Optimization interface.

Table 3
Results of the optimization process, best HIDiC design for each case study.

of the vapor flow in SS and the increment of liquid flow at SR, which obeys to the heat transference from SR to SS.

On the other hand, as it was discussed, the arrangement to perform the heat exchange might be configured as a concentric exchanger, where the inner section is SR (high pressure) and the external section is SS (low pressure). So, the wall of the inner column (SR) is used as the heat exchange area. An important efficiency may be obtained in this configuration because the heat flow crosses the inner wall and is transferred to the liquid of SS before going to surroundings. However, the heat transfer area in the internal wall may be lower than the required area to carry out the heat exchange. To alleviate this limitation, the configuration for heat exchange can be designed as a compact heat transfer panel, which may be placed in the rectifying section or in the stripping section. When the panel is placed in SS, it is open to the rectifying section. Therefore, the steam from SR enters and condenses, generating the vapor in SS. This arrangement will give a large efficiency and the constraint of heat transfer area mentioned before may be eliminated. Alternatively, the heat transfer area might be placed as an external heat panel, where the steam from SR enters and condensates within the panel and the liquid of SS is vaporized.

To perform the design and optimization, it is used the interface depicted in Fig. 6. In this interface, the BUMDA algorithm is the master algorithm programmed in Matlab, which invokes the simulator Aspen Plus through Excel to get the design variables and evaluate the fitness function.

As in the previous study [7], in this work a population of 60 individuals and 50 generations were used. The simulations were made with a PC with an i5 processor core, clock frequency at 2.8 GHz , and 16 GB of RAM.

## 6. Results

Once optimization process was carried out, the best HIDiC designs were collected in Table 3.

Through results shown in Table 3, it was ratified that the best HIDiC configurations operate using low compression ratios, from 1.29 to 2.15. Furthermore, the total stage number varies from 28 to 138 stages. At the same time, the reflux ratio had a variation from 0.084 to 9.63 . In terms of reflux ratio, the highest value was presented on systems whose relative volatility was lower than 1.38. Likewise, we observe that the TAC is commonly increased as the relative volatility rises. We can also see that both purity and recovery constraints (taking as a reference the light component, A) were preserved within the limits established. These results reveal the capability of the BUMDA algorithm to optimize constrained problems through the methodology established. As it was discussed on detail in the precedent study, BUMDA algorithm preserves a continuous approximation to the optimal value by using the Boltzmann distribution, truncation method and the reset mechanism.

Besides, it is important to underline that when the fitness function has similar values during several generations, the algorithm tends to rapidly explore around the lower limit of CR even when reset mechanism is activated. Although this phenomenon is reasonable, i.e. a better performance of the HIDiC is obtained at low CR, this fact shows that algorithm may stop when the value of the fitness function lies within a tolerance established. This tolerance might be defined as a minimum difference between the anterior and current value of the fitness function. This condition will reduce the optimization time, because NumEval will be lower than NumEvalMax.

Either, it was evident that the initial values, randomly generated in the algorithm, influenced in the time used for the optimization. However the convergence was always reached. Regarding the latter point, it was determined that the optimization process will be enhanced by establishing shorter limits for the compression
![img-5.jpeg](img-5.jpeg)

Fig. 7. Variation of the TAC and $Q$ with the relative volatility.

Table 4
Requirements of compression ratio as a function of relative volatility.
ratio, e.g. $(1,3)$. Within these limits were obtained the best values of the fitness function for all case studies. Other phenomena observed in the optimization is the increasing of numeric effort and computational time implicated in the convergence as the relative volatility nears the unity.

### 6.1. Variation of the energy consumption and the TAC as a function of the relative volatility

It may be observed in Fig. 7 that the best HIDiC designs represent energy savings between 50 and $87 \%$ compared with traditional columns. At the same time, the TAC of HIDiC designs oscillates since considerable reductions ( $16 \%$ ) to HIDiC designs with a TAC $37 \%$ larger in relation to the corresponding traditional columns.

This fact ratifies the energetic and economic behavior derived from these separation technologies as a function of the mixture properties to be separated.

In addition, a detailed analysis carried out on Fig. 7 shows that $\%$ $Q$ reduces as relative volatility decreases. The maximum saving reached was $84 \%$. Afterward, a further reduction of the relative volatility, in relation with M4, the energy savings tends to decrease, reaching a maximum peak on the curb, whose energy saving was $50 \%$. After this maximum point, the behavior shows that an additional reduction of the relative volatility leads to further energy savings, reaching $87 \%$ of saving in the system of the relative volatility of 1.12 .

In a similar analysis, it was found that \%TAC diminishes as the relative volatility becomes smaller, obtaining a TAC saving of $2 \%$ for the M4 case. Moreover, when the relative volatility is reduced to 1.248 , a greater saving is achieved ( $16 \%$ ). Nevertheless, if the relative volatility is lower than 1.248 , HIDiC sequences become economically equal (M7) or even more expensive (M8 and M9) than the traditional columns. Observe that the points along the curve correspond to the mixtures that contain polar species.

This analysis reveals the general behavior around HIDiC columns, taking the relative volatility as a reference point. However, to explain why this behavior takes place, a more exhaustive analysis of relative volatility and the optimization variables is presented in the following subsections.

### 6.2. Effect of the compression ratio on the degree of energy integration

As may be noted in Table 4, we define two terms for the compression ratio, which are (a) Minimal compression ratio ( $\mathrm{CR}_{\text {min }}$ ), and (b) real compression ratio ( $\mathrm{CR}_{\text {real }}$ ). $\mathrm{CR}_{\text {min }}$ represents the minimum compression ratio required to generate feasible temperature driving forces. Similarly, $\mathrm{CR}_{\text {real }}$ is the condition of operation that provides the most convenient temperature driving forces to obtain a better interrelation between the energy savings and total annual costs for a given design.

At the same time, the tendencies of both operation conditions ( $\mathrm{CR}_{\text {min }}$ and $\mathrm{CR}_{\text {real }}$ ) indicate that as the relative volatility reduces (particularly from 2.4 to 1.38 ) the compression ratio also bears a reduction. Nonetheless, when the relative volatility reaches values lower than 1.38 (except for M8), an increasing of the compression ratio takes place.

This phenomenon is linked with the behavior of the temperature driving forces shown in Fig. 8. As it can be noted in Fig. 8, a diminution of the relative volatility from 2.4 to 1.44 causes a reduction of the compression ratio. Under this condition, these systems present temperature driving forces between 5.6 and 7.3 K . However, when the relative volatility moves toward a relative volatility of 1.38 , the temperature driving forces $\left(\Delta T_{S R .55 \text {-average }}\right)$ falls to a negative value. This fact shows that the temperature in most stages in SS was larger than the temperature in the stages of SR. Consequently, the average temperature driving forces were dominated by non-integrated stages. In this way, the energy integration is limited. Thus, in order to improve the thermodynamic feasibility to integrate larger amounts of energy, CR must be increased in mixtures whose relative volatility is lower than 1.38. This behavior can be generated due the natural difficulties caused by the similarity to the azeotropic behavior as the relative volatility nears to the unity.

This analysis indicates that when the components of a mixture have similar boiling points, the temperature driving forces tend to be smaller. So, an augment of CR helps to maintain them in a feasible operation range to achieve the energy integration. Thus, the best possible condition between TAC and the energy consumption for these cases study is found.

These results denotes the necessity to adequately control the temperature driving forces to get feasible HIDiC configurations in both economic and energetic terms.

### 6.3. Interrelation between number of stages, relative volatility, and the compression ratio in the HIDiC configurations

In terms of total stage number, results illustrated in Fig. 9 show that at relative volatilities lower than 1.5, the best HIDiC designs are made up by more than seventy total stages. These designs are characterized to operate at the lowest values of the compression ratio in relation with the complete range of relative volatility used. A simultaneous analysis of this behavior and the discussion observed in Fig. 8 leads us to establish that when HIDiC designs are made up of more than seventy stages the temperature driving forces reduce. Consequently, as it was explained above, this fact has been reverted by increasing the compression ratio.

### 6.4. Effect of the reflux ratio and the compression ratio on the energy consumption and the TAC

As shown in Fig. 10, the reflux ratio of the HIDiC columns is considerably less than the reflux ratio of traditional distillation columns. In fact, the minimal reduction obtained was about $55 \%$. Meanwhile, the maximum reduction was around $90 \%$. Notice that the highest reduction was located both in the low relative volatility mixtures as in the high relative volatility systems. However, it is important to highlight that the reduction of RR was better harnessed by the low volatility mixtures (particularly for the cases with the relative volatility of $1.12,1.248$ and 1.4). This is established because the maximum energy reduction was achieved for these cases.

The noticeable reduction of both energy consumption and reflux ratio for the HIDiC are derived of the characteristics of the mixture. For instance, M4 is a polar mixture of alcohols (n-butanol/ isobutanol) and the mixture itself is a mixture of isomers. Thus, this is considered as a difficult separation and large energy savings and low reflux ratios are experienced for the HIDiC. This obeys to the behavior of these configurations in the separation of mixtures with considerable difficulties to be separated.

In addition, as it can be seen in Fig. 10, it is observed that RR ratio mimics the profile corresponding to energy consumption ratio. This means that a reduction or increasing at RR will generate the

![img-6.jpeg](img-6.jpeg)

Fig. 8. Variation of the temperature driving force average $\left(\Delta T_{50-55}\right.$-average) as a function of compression ratio and relative volatility.
![img-7.jpeg](img-7.jpeg)

Fig. 9. Relationship between the relative volatility, total number of stages and the compression ratio.
![img-8.jpeg](img-8.jpeg)

Fig. 10. Behavior of RR and Q ratios with relative volatility.

![img-9.jpeg](img-9.jpeg)

Fig. 11. Variation of TAC and CR with relative volatility.
corresponding effect on the heat duty ratio. That is; the lower reflux ratio, less heat duty is used. Similarly, the larger reflux ratio, the larger heat duty is required. This fact corroborates the existent relationship between these variables in distillation systems.

The relative separation of the curves of $\% \mathrm{Q}$ and $\% \mathrm{RR}$ in Fig. 10, for relative volatilities larger than 1.44 , is generated due to the influence of the compressor duty in the separation of these mixtures. As it was shown before, the energy is less efficiently used in the separation of mixtures with large relative volatility. So, when the compression ratio is increased in the systems of relative volatility larger than 1.44 , the reduction of energy in the reboiler is achieved together with a considerable reduction in the reflux ratio. However, the total energy involved ( $Q_{R}$ plus $Q_{\text {comp }}$ ) in the HIDiC remains relatively large due to the energy used in the compressor. Differently, the mixtures with relative volatilities lower than 1.44 undergo less influence of the compressor duty. Thus, the curves of $\% \mathrm{Q}$ and $\% \mathrm{RR}$ remains nearer each other at relative volatilities lower than 1.44. Additionally, through Fig. 11 it is possible to verify that the TAC determined for the HIDiC sequences is more favorable at low relative volatilities as it has been mentioned. In this case, TAC reductions of $2 \%$ for the system

M4 and $16 \%$ for mixture M6 were obtained. The compression ratios for these cases were: 1.76 and 1.248 respectively. After this value of CR (1.248), the compression is augmented as the relative volatility is reduced. Thus, the TAC of the HIDiC designs is similar and even larger ( $6-17 \%$ ) than the TAC of conventional columns.

In addition, the analysis of Fig. 11 allows establishing that \%TAC follows a similar tendency to the compression ratio for most of cases studied.

Likewise, notice that the mixtures that include polar components undergo a deviation in relation to the behavior of the hydrocarbon mixtures. Despite this deviation, such mixtures are positioned in the range of relative volatility where the most benefits of the HIDiC configurations are obtained.

Particularly, observe that $\% R R$ for the alcohols mixture represents the minimum value found. Besides, \%Q was only slightly larger than the value obtained for the mixture of xylenes. This fact indicates that mixtures of isomers (M4 and M9) undergo the highest energy savings and the lowest reflux ratios.

As a summary, considering the analysis carried out in Figs. 10 and 11, it is established that the best energy savings are obtained for the mixtures of isomers M4 and M9; while the
![img-10.jpeg](img-10.jpeg)

Fig. 12. Behavior of CR and RR as a function of relative volatility.

mixture M6 gave the most suitable relationship of the \%TAC. Nonetheless, taking into consideration both variables, it was determined that M4 and M9 have a more profitable relationship between TAC and energy savings than M6. At the same time, comparing the mixtures of isomers (M4 and M9), the separation of alcohols has a better balance between TAC and energy savings of the HIDiC than the mixture made up xylenes.

This behavior of the TAC and energy savings is a result of the capital cost derived of the installation of large heat transfer areas and considerable electrical power required by the compressor for almost all configurations. It is important to remember that electrical energy is several times more expensive than heating steam. However the TAC for several HIDiC is about 20\% larger than conventional columns, as a result of large energy savings. The TAC could be alleviated trough a reduction of energy savings, which will demand less heat transfer area and lower power consumption in the compressor. The effect of other variables, such as: composition of the feed, energy integration at different level between $\%$ R and $\%$ S and intensification of the HIDiC, could lead to obtain HIDiC designs with large energy savings and TAC favorable. On the other hand, the consideration of carbon credits might be taken into account to make the final decision about the implementation of the process.

Through a comparative analysis of Figs. 7 and 12, it is worth emphasizing that \%Q has an analogous behavior to RR-ratio. Similarly, \%TAC has an analogous tendency to the compression ratio for almost all case studies. This performance takes place due to direct relationship between the reflux ratio and the energy consumption, such as discussed previously. On the other hand, the tendency between \%TAC and CR is a consequence of the capital cost of the compressor, heat transfer areas and the costs of electric power derived from the compression ratio used.

As we can see in the behavior discussed, there are important energetic benefits and attractive TAC for most of HIDiC sequences. At the same time, it is evident the existence of continuous oscillations in the trends for Q, RR, TAC, such a way that even some points were left out of the curves. These tendencies are result of the characteristics and properties of the mixtures. As may be inferred, the mixtures used in this study were selected taking as unique criteria the relative volatility of the components. The mixtures were made of hydrocarbons (e.g. n-heptane-cyclohexane), polar compounds (e.g. n-butanol/isobutanol) and hydrocarbons and polar species (e.g. benzene/1,1,1-trichloroethane). As we can see, different kinds of compounds lead to different characteristics and properties of the mixtures. Therefore, these factors influence the energetic and economic behavior of HIDiC configurations. Thus, the multivariable optimization under the influences mentioned gave as a result the oscillating behavior observed.

### 6.5. Design parameters of the best HIDiC and their corresponding conventional configurations

The collection of the design parameters of the best HIDiC sequences and the corresponding traditional columns is presented in Table 5.

Based on the information in Table 5, it is clear that by using an adequate compression ratio we find a meaningful reduction of the reflux ratio ( $55-90 \%$ ) and the heat duty ( $50-87 \%$ ). At the same time, notice that carbon dioxide emissions are notably reduced in a proportional amount to the energy consumption.

These results show that the benefits of HIDiC sequences are obtained as a consequence of the electrical power used in the compression system and the installation of considerably large heat transfer areas. At the same time, the total annual cost determined varies from considerable reductions ( $16 \%$ ) to similar and even superior TAC ( $6-17 \%$ ) in relation to the corresponding traditional sequences.

Table 5
Design and operation variables of the best HIDiC configurations and the corresponding conventional columns.
On the other hand, the values of the thermodynamic efficiency of the HIDiC configurations show the higher harnessing of the energy compared with traditional columns, such as it is presented in Table 5.

Likewise, the results in Table 5 make the advantages of HIDiC design evident versus a conventional column in terms of $\mathrm{CO}_{2}$. Through a simple analysis, there is a notorious reduction in $\mathrm{CO}_{2}$ emissions. In fact, calculations indicate that $\mathrm{CO}_{2}$ emissions follow the same tendency as energy consumption. This is the expected behavior taking into account the direct relationship between energy consumption and $\mathrm{CO}_{2}$ production. That is, as the more fuel burned, the larger the $\mathrm{CO}_{2}$ emissions generated.

## 7. Conclusions

In this work, the design and optimization of HIDiC configurations are achieved using a constrained Boltzmann-based algorithm. The design-optimization strategy was implemented by means of Matlab-Excel-Aspen Plus interface.

Results demonstrated that the BUMDA algorithm successfully led to the optimization of HIDiC schemes. The Boltzmann distribution and the truncation method conducted the search to the most profitable region, whereas the reset mechanism promoted an exhaustive exploration of that region. It could be established due to that the search was frequently directed to the best fitness function value.

At the same time, the implemented methodology allowed us to carry out diverse energy integration analysis on each HIDiC design in a systematic way.

In addition, the interrelation between the reflux ratio and the amount of energy integrated allowed us to ratify that the factor with the most influence on the performance of HIDiC is the compression ratio, followed by the reflux ratio. We also concluded that the greatest benefits of the HIDiC configurations are obtained for mixtures with a range of relative volatility from 1.12 to 1.5 . Within this range, energy savings oscillate between 50 and $87 \%$. At the same time, it was determined that the TAC varies from HIDiC designs with a lower TAC ( $16 \%$ ), similar and even higher ( $6-17 \%$ ) than traditional columns. Furthermore, it was established that the separation of mixtures of isomers, alcohols mixture, in particular, gave the best interrelation (energy savings and TAC) of HIDiC technology. In this case, we proved energy savings of $84 \%$ and a TAC of $2 \%$ less in relation to the conventional sequence. Nevertheless, the mixture of isomers, M9, showed large energy savings (87\%).

On the other hand, it is important to underline that the compression ratio controls the TAC. This is mainly due to the high capital and the power requirements of the compression system, in addition to the large heat transfer areas. In a similar way, the reflux ratio defines the behavior of the energy consumption in the reboiler of the column. Thus, the optimization allowed us to find the most effective conditions for both CR and RR, which strikes a balance between energy savings and TAC for each HIDiC design of each case studied.

## Acknowledgements

The authors acknowledge the financial support provided by CONACyT (México).

## Appendix A.

The costing of the main equipment was estimated by the cost equations shown in [30], considering carbon steel. These costs were updated with the CEPCI (Chemical Engineering Process Cost Index). The annual capital cost is the sum of the installed cost of each module, i.e., column shell, reboiler, condenser, trays,
compressor and heat transfer areas. In a summarized way, the procedure is as follows:

## Column (vessel)

$$
\begin{aligned}
& \log _{10} C_{\mathrm{p}}=K_{1}+K_{2} \log _{10} A+K_{3}\left(\log _{10} A\right)^{2} \\
& A=\text { height of vessel, (m) } \\
& F_{\mathrm{p}}=0.5146+0.6838 \log _{10} P+0.2970\left(\log _{10} P\right)^{2} \\
& +0.0235\left(\log _{10} P\right)^{6}+0.0020\left(\log _{10} P\right)^{8}
\end{aligned}
$$

where $P=$ Pressure (barg)
$C_{\mathrm{BM}}=C_{\mathrm{p}}\left(B_{1}+B_{2} F_{\mathrm{M}} F_{\mathrm{p}}\right)$

## Trays (sieve)

$C_{\mathrm{p}}=235+19.80 D+75.07 D^{2}$
$C_{\mathrm{BM}}^{\prime}=C_{\mathrm{p}} N F_{\mathrm{BM}} F_{\mathrm{q}}$
where $D$ : diameter of vessel, $\mathrm{m} . N$ : number of trays.
Condenser (floating head), reboiler (kettle) and heat transfer areas (kettle)
$\log _{10} C p=K_{1}+K_{2} \log _{10} A+K_{3}\left(\log _{10} A\right)^{2}$
$A=$ heat transfer area, $\mathrm{m}^{2}$
$\log _{10} F p=C_{1}+C_{2} \log _{10} P+C_{3}\left(\log _{10} P\right)^{2}$
where $P=$ Pressure (barg)
$C_{\mathrm{BM}}^{\prime}=C_{\mathrm{p}}\left(B_{1}+B_{2} F_{\mathrm{M}} F_{\mathrm{p}}\right)$

## Compressor

$\log _{10} C p=K_{1}+K_{2} \log _{10} A+K_{3}\left(\log _{10} A\right)^{2}$
$A=$ fluid power $(\mathrm{kW})$
$C_{\mathrm{BM}}^{\prime}=C_{\mathrm{p}} F_{\mathrm{BM}}$
Taking into account the plant life time, the annual capital cost of each module is calculated as:
$\mathrm{CCM}=\frac{\left[\left(1.18 C_{\mathrm{BM}}^{\prime}+0.35 C_{\mathrm{p}}\right)(\text { CEPCI ratio })\right]}{\text { Plant life time }}$
Thus, the total annual capital cost (CCT) is given by:
$\mathrm{CCT}=\sum_{i=1}^{n} \mathrm{CCM}_{i}$
where $n=$ number of modules.
Cost of utilities

Vapor cost $=$ vapor flow $\times$ unit cost $\times$ Operating hours

## Cooling water cost $=$ cwflow $\times$ unit cost <br> $\times$ Operating hours

Electricity cost $=\mathrm{kW} \times$ unit cost $\times$ Operating hours

Thus,

## TAC $=$ CCT + vapor cost + cooling water cost + electricity cost

Plant life time $=5$ years; Operating hours $=8000 \mathrm{~h} /$ year. The other parameter required were taken from [30].
