# Development of a time-dependent economic method with start time consideration to optimise gas-lift allocation and scheduling 

S. Omid H. Miresmaeili*<br>Institute of Petroleum Engineering, University of Tehran, Tehran, Iran<br>Email: omiresmaeili@alumni.ut.ac.ir<br>*Corresponding author

## Peyman Pourafshary

Department of Petroleum and Chemical Engineering, Sultan Qaboos University, Muscat, Oman
Email: pourafshary@squ.edu.om

## Farhang Jalali Farahani

School of Chemical Engineering, University of Tehran, Tehran, Iran
Email: fjalali@ut.ac.ir


#### Abstract

The gas lift allocation optimisation is an important operational problem. In this paper, we present a method to optimise the lift gas allocation profile and determine the best time to start the gas-lift operation for each well. To tackle the nonlinear optimisation, an estimation of distribution algorithm (EDA) is employed based on Gaussian Bayesian networks and Gaussian kernels and the results are compared with those obtained by particle swarm optimisation (PSO) and genetic algorithms (GAs). Gas-lift performance for all the wells along with estimated cumulative production data are correlated over time to develop a model to show the field production behaviour as a function of the gas injection rates and initiation parameters. The developed model is coupled with an economic model to maximise the net present value of the gas-lift process for the field. [Received: 7 September 2014; Accepted: 30 September 2015]


Keywords: gas-lift allocation; gas-lift start time; economic optimisation; Gaussian network; estimation of distribution algorithm; EDA.

Reference to this paper should be made as follows: Miresmaeili, S.O.H., Pourafshary, P. and Farahani, F.J. (2016) 'Development of a time-dependent economic method with start time consideration to optimise gas-lift allocation and scheduling', Int. J. Oil, Gas and Coal Technology, Vol. 13, No. 1, pp.41-59.

Biographical notes: S. Omid H. Miresmaeili is currently a researcher in NIOC-IOR Research Institute in lieu of mandatory military service as Iran's National Elites Foundation member. He received his MSc in Petroleum Production and Drilling Engineering from the Institute of Petroleum Engineering, University of Tehran, Iran, in 2014. His research interests include artificial lift systems design and optimisation and application of artificial intelligence methods in modelling and optimisation of production systems.

Peyman Pourafshary received his PhD in Petroleum Engineering from University of Texas, Austin, in 2007. Currently, he works as an Assistant Professor in Department of Chemical and Petroleum Engineering at the Sultan Qaboos University, Oman. His research interests are in the fields of production engineering and production optimisation, well stimulation, formation damage and experimental studies and modelling of enhanced oil recovery methods. He has published more than 45 peer reviewed papers in these areas.

Farhang Jalali Farahani is currently Professor and faculty member at the University of Tehran. He received his PhD degree from University of Utah, in 1992, and his Master degree from Colorado State University, in 1988, USA. His field of interest is production optimisation in oil and gas industries. He has worked on many projects using high models and computational algorithms.

# 1 Introduction 

The growth in energy demand and rising oil consumption has given rise to the requirement for more efficient and economic oil production. Artificial lifting and in particular gas lifting is a common practice in achieving long-term stable production at commercial rates.

It is well known that as a reservoir's pressure declines, the ability of the reservoir to supply fluid to the wellbore deteriorates, which in turn causes a decrease in oil production. In order to address this problem and to sustain the desired production rate, the gas-lift process can be employed. The choice of the proper gas injection rate is crucial to gain optimal production. By increasing the gas-liquid ratio (GLR) the hydrostatic pressure difference from the bottom to the top of the well reduces, lowering the bottomhole pressure and increasing the reservoir drawdown. However, as the injection rate increases, the enhanced production rate begins to falter due to the additional frictional pressure drop in the tubing. Hence, an optimised value for the injection gas flow rate should be determined to maximise the production profit. Furthermore, in the case of a multiple-well production network and limited injection capacity, optimising the gas-lift allocation results in a more complicated problem.

Much literature has been published on solving the injection lift gas distribution problem. Redden et al. (1974) and Kanu et al. (1981) similarly considered consistent economic factors by including revenue from production and the operational costs. Nishikiori et al. (1989) proposed a first-order quasi-Newton method to tackle the problem under limited and unlimited available gas conditions. Martinez et al. (1994) presented the first-known use of a genetic algorithm (GA) for the gas-lift allocation problem. Alarcón et al. (2002) developed a sequential quadratic programming (SQP) algorithm to solve this

nonlinear problem. Mora et al. (2005) utilised a commercial simulation software with the purpose of maximising the net present value (NPV) of the asset under different gas-lift efficiencies and oil price scenarios. They employed a detailed economic model coupled with an integrated model of the reservoir, wells and fluid gathering system. Furthermore, the model was designed to handle changes in compression, gas availability and handling capacities and a sensitivity analysis for the oil price variation was also undertaken. Camponogara and Nakashima (2006) employed a dynamic programming (DP) formulation for the problem of determining which wells to produce and how much gas flow to distribute among the wells in the system. Gutierrez et al. (2007) used an iterative offline-online procedure to solve the gas-lift optimisation problem. Using predictive reservoir conditions and performing gas-lift allocations at different coupling steps, they solved the problem under various constraints including water handling, compressor power, and liquid production and gas injection rates. Ray and Sarker (2007) used a variant of the non-dominated sorting genetic algorithm (NSGA-II) and approached the gas-lift optimisation problem as a bi-objective problem, in which maximising the total oil production and minimising the gas injection rates were the objective criteria. Piecewise linear approximations of six- and 56-well gas injection data from Buitrago et al. (1996) were employed. Wang and Litvak (2008) tackled the problem using a heuristic method to solve the well-rate and gas-lift allocation problem while maximising production. They also introduced a multi-objective scheme to maximise oil production besides reducing rate oscillations. Huh et al. (2010) used a simulated annealing (SA) algorithm to optimise the net profit of the gas-lift process using piecewise cubic hermit interpolation as a function approximation tool and taking into account the produced gas cycle efficiency as the lift gas. Rashid (2010) proposed an iterative offline-online scheme to solve the gas-lift allocation problem with the intention of maximising daily production. The method calls for a multi-phase flow simulator in each iteration and takes into account the effect of the interaction among wells. Sharma et al. (2012) addressed the gas-lift allocation problem by incorporating a cascade control structure along the MATLAB optimisation toolbox and hill-climbing as the optimisation methods, with maximising total oil production as the optimisation criterion. Also, Codas and Camponogara (2012) dealt with the problem by maximising the production of all the gas-lift wells with respect to the routing of the wells to separators using a mixed integer linear programming (MILP) formulation. Posenato and Rosa (2012) employed a GA to solve the allocation problem with compressor capacity constraints. Ghaedi et al. (2014) dealt with the Buitrago et al. (1996) gas-lift data once more, this time with a variant of the ant colony algorithm, the continuous ant colony optimisation (CACO) algorithm. Again, the optimisation criterion was maximising daily oil production. It might also be observed that usually the well configurations and gas-lift design criteria, such as the number of gas-lift valves and their corresponding depths, are not taken into account in the gas-lift allocation problem, due to the fact that well configuration is already completed by the production stage and is generally considered invariable. Also, gas injection normally occurs at predetermined depths at the lowest valve at the available injection pressure, where the depths have been set in advance (Rashid et al., 2012).

Figure 1 Decline curve representation of typical delay in gas-lift operation
![img-0.jpeg](img-0.jpeg)

It can be seen that numerous authors have focused on the technical and economic problems of gas-lift allocation. In all of the mentioned works, it is assumed that the gas-lift process starts for all the wells at the same time. This approach ignores the importance of the initiating time of the gas lift. Also, with the exception of Mora et al. (2005), the time value of money is not considered during the course of the gas-lift project. In this study, we present a method to obtain the optimal gas-lift injection profiles in a time-dependent manner and determine the best time to start the gas-lift operation for each well. It will be shown that starting the gas-lift process from the beginning of a project is not always the best strategy and yields economically unattractive results. On the other hand, commencing the gas-lift operation in a well at a later stage of the project and withholding the natural lift rather than starting the gas-lift injection process at the beginning of the project (Figure 1) can lead to more cost-effective options due to the discounting concept. It should be pointed out that the effect of the declining pressure of the reservoir should be taken into account in order to consider the passing of time. To solve the gas-lift allocation and scheduling problem, an efficient estimation of distribution algorithm (EDA) is employed. The EDA utilises a set of Gaussian kernels of probability distribution functions (PDF) (Socha and Dorigo, 2008) as well as Gaussian Bayesian networks (BN) (Larrañaga et al., 2000) to guide the search and to discover possible interactions between variables. The promising solutions are generated by sampling the probabilistic models. It is worth noting that the EDA in this paper is a uniobjective version of a multi-objective implementation of the algorithm given in the literature (Miresmaeili et al., 2015). The key advantage of an EDA over classical evolutionary algorithms, such as the GA or simple particle swarm optimisation (PSO), is the absence of multiple parameters to be tuned (e.g., crossover and mutation probabilities) as opposed to the implicit models defined by the other metaheuristics. The main search process of an EDA is mostly dependent on its probabilistic models and particularly on the mechanism of generating new solutions (i.e., offspring) from an estimated distribution. In contrast to EDAs, classical GAs and other similar evolutionary algorithms use simple search operators, such as two-point crossover and binary tournament selection, which implicitly define a probabilistic distribution model based on the current population and the generated new population can be seen as samples of that distribution (Hauschild and Pelikan, 2011). In addition, EDAs have been proven to be better suited to some applications than the other evolutionary algorithms, such as GAs, since they are able to achieve economic and robust results in the majority of tackled problems (Armañanzas et al., 2008; Jarboui et al., 2009; Su and Chow, 2012). It is

indisputable that most often, a practical gas-lift optimisation problem involves a large search space with numerous decision variables. Hence, the simpler methods are not powerful enough to handle such large scale problems (Miresmaeili et al., 2015).

# 2 Workflow 

The optimisation problem includes an oil field model consisting of multiple gas-lift wells with a limited amount of available gas. Also, no shared flow line is assumed in the system, so there is no consequent back pressure in changing the injection rates. This is merely a simplification in order to only focus on the start time effect as a decision variable of the optimisation problem; however, this assumption is still valid for separate wells without common flow lines (Dutta-Roy and Kattapuram, 1997). The main purpose of the optimisation problem is to achieve maximum NPV of the production system through the proper distribution of injection gas and by determining the best start time of the injection for each well during the course of production. Hence, NPV is used as the objective function to compare the gas injection scenarios to find the most attractive. Furthermore, an oil reservoir model is incorporated to reflect the effects of changes in lift gas injection rates and the corresponding oil production on time-cumulative production relations during the course of the project. Also, the GLP changes over time should be considered. To tackle the problem, the following methodology is employed:

### 2.1 Step 1: Generating GLP curves

For each well a set of vertical lift performance (VLP) curves corresponding to different GLRs and an inflow performance relationship (IPR) representing reservoir pressure can be drawn as shown in Figure 2 (Economides et al., 1994).

Figure 2 Varying GLR for a single IPR curve
![img-1.jpeg](img-1.jpeg)

The procedure is repeated for different reservoir pressures and the intersection points are used to generate GLP curves. For example, Figure 3 shows the GLP data for Well 1 in the oil field model. The importance of GLP data for a depleting reservoir lies in the fact that the equivalent time to reach a certain reservoir pressure is not determined yet and, as discussed later, these data will help in correlating lift performance and reservoir pressure with time. It should be pointed out that, at this step, the more these initial data are presented to the optimisation algorithm the more valid and accurate the construction of the future dynamic models, although the search process and especially the variety of the curves should cover a wide range of different scenarios of gas-lift operation to train the

algorithm to predict various production scenarios. Of course, one way to address this limitation would be to couple the optimisation algorithm to a commercial simulator which would result in high computational cost but can increase the validity of the production model.

Figure 3 Example of GLP curve for depleting reservoir pressure (see online version for colours)
![img-2.jpeg](img-2.jpeg)

# 2.2 Step 2: Predicting reservoir performance 

For an undersaturated reservoir, fluid recovery depends entirely on fluid expansion due to declining reservoir pressure (Economides et al., 1994). Therefore, by assuming that compressibility is small and constant, the following expression can be derived from the isothermal compressibility definition:

$$
R=\frac{N}{O O I P}=e^{p_{r}\left(p_{i}-\bar{p}\right)}-1
$$

In equation (1), $R$ refers to the recovery factor, $N$ is the cumulative oil production, OOIP is the original oil in place, and ct is the total compressibility, while $p_{i}$ and $\bar{p}$ refer to initial and average reservoir pressure, respectively. Using equation (1) for each reservoir pressure interval, incremental cumulative production can be calculated.

If needed, a similar calculation can be made for a saturated oil reservoir. For example, for an internal gas drive reservoir and assuming uniform oil saturation in the whole reservoir, the technique presented by Muskat (1945) can be applied.

### 2.3 Step 3: Correlating reservoir and well performance data with time

Using the concept of IPR in conjunction with the reservoir performance predictions, the time required for a certain incremental cumulative production can be calculated. The following procedure can be employed to correlate predicted cumulative field production with time:
1 For each average reservoir pressure interval, the cumulative oil production, $\Delta N p$, is calculated by material balance calculations (step 2).
2 For a certain reservoir pressure interval, using the generated GLP curves and a set of gas injection rates (here, generated by the EDA), the average total field flow rate, $\left(Q_{s}\right)_{f i o l d}$, in the corresponding pressure interval is determined:

$$
\left(Q_{o}\right)_{\text {field }}=\sum_{i=1}^{\# \text { wells }}\left(Q_{o}\right)_{i}
$$

In equation (2), the term $\left(Q_{o}\right)_{i}$ denotes the average flow rate for well $i$ for a mean value of reservoir pressure within the pressure interval. It should be pointed out that the injection gas rate, $\left(Q_{g}\right)_{i}$, that is used for calculating the flow rate should satisfy the following constraint:

$$
\sum_{i=1}^{\# \text { wells }}\left(Q_{g}\right)_{i} \leq A G
$$

where $A G$ is the fixed daily available gas during the project.
3 Then the time, $\Delta t$, required for the corresponding incremental oil production is simply $\Delta t=\Delta N_{p} /\left(Q_{o}\right)_{\text {total }}$.
4 This procedure is repeated for all the reservoir pressure intervals and similarly the field flow rate and cumulative production are related to time.

# 2.4 Step 4: Calculating annual cash flow and NPV 

For economic analysis of the gas-lift operation, the annual cash flow, $F_{k}$, is calculated using the following expression:

$$
F_{k}=R_{k}-E_{k}=p_{o} N_{k}-O_{k}-C_{k}-r_{B} p_{o} N_{k}-T_{B} I_{b t, k}
$$

In equation (4), $R$ is revenues, $E$ is expenses, $p_{o}$ is the oil price, $N$ is the annual cumulative production, $C$ is the capital expenditure (CAPEX), and $O$ is the operating expenditure (OPEX) which is divided into a fixed part, expressed as a percentage of the cumulative project CAPEX and a variable part expressed as a cost per unit of daily oil produced. Also, $T_{B}$ and $r_{B}$ are tax rate and royalty rate, respectively, while $I_{b t}$ is income before tax, which is defined as:

$$
I_{b t, k}=p_{o} N_{k}-O_{k}-r_{B} p_{o} N_{k}-D\left(C_{k}, C_{k+1}, \ldots, C_{k-K}\right)
$$

In equation (5), $D$ is the straight line depreciation function and $K$ is the number of years over which the CAPEX can be depreciated. The CAPEX is simply divided into equal parts over a period of K years since the gas-lift start time.

To consider the time value of money, $R_{\text {disc }}$ that reduces the value of money during the course of the project is taken into account. Therefore, the discounted annual cash flow in year $k, F_{k, \text { disc }}$, is defined as follows.

$$
F_{k, \text { disc }}=F_{k} /\left(1+R_{\text {disc }}\right)^{n}
$$

where $n$ is the number of years since the investment. The summation of discounted annual cash flow results in the NPV. If we consider the objective function as $\mathrm{NPV}(\mathrm{X})$ on a yearly time interval basis, the X would refer to the difference between the present value of the future cash flows from the annual cumulative production and the cost of investment for that production. The size of X would correspond to the number of wells in the study as the annual cumulative production is the summation of the amount of production of each individual well, which is the key variable in the revenue and expense calculation as mentioned above. Such calculations provide an appropriate comparison

between profit and cost over time. For example, a scenario which delays the gas-lift operation for one year may excel over a case with an earlier gas-lift start time in terms of NPV. So, we should take into account the effect of different gas-lift start times on production and the economic aspects of the operation when optimising a gas-lift project (Figure 4).

Figure 4 Various gas-lift start times lead to different production behaviours (see online version for colours)
![img-3.jpeg](img-3.jpeg)

In short, the optimisation problem involves $\omega \times(1+\Delta)$ decision variables to be optimised, where $\omega$ is the number of wells, and $\Delta$ is the number of time intervals considered for the problem. With each set of solutions obtained from the algorithm the problem is solved for the NPV and, based on the stopping criterion, the optimisation process would continue or stop, i.e., the time at which the gas-lift operation starts is considered as an explicit variable rather than setting the gas injection rate to zero to indicate the natural production period.

# 3 Optimisation algorithm 

To maximise the objective function as defined in the above methodology under a constant constraint of limited gas [equation (3)], an EDA based on BN and Gaussian kernels is employed.

The core idea of an EDA is to build a probabilistic model in each iteration by using a set of promising solutions constructed so far and to take samples of the probabilistic model to generate new solutions and move to the next iteration (Figure 5).

Figure 5 Basic idea of the EDA (see online version for colours)
![img-4.jpeg](img-4.jpeg)

A BN can be used as the probabilistic model. It consists of a directed acyclic graph (DAG) in which nodes and edges represent the variables and interactions, respectively. To define these interactions, conditional dependencies between variables are employed. To learn the BN structure from the selected set of promising solutions (observation data), a scoring metric and a greedy search procedure, starting from an empty adjacent graph, are used. The greedy algorithm tries to add a possible edge that improves the scoring metric. The search process stops when no improvement can be attained by arc addition. The exception is that no cycle can be introduced in the graph. The scoring metric is based on the Bayesian information criterion (BIC) (Schwarz, 1978) which is simply defined as follows (Ahn et al., 2006):

$$
B I C(\zeta)=\sum_{j=1}^{|S|} \ln P(X)-0.5 \ln (|S|)|\theta|
$$

where $B I C(\zeta)$ refers to structure $\zeta$ score, $|S|$ is the number of observations as $S=\left\{x^{1}, \ldots, x^{|S|}\right\}$ and each x is an instant of variables, while $P(X)$ is the probability distribution function (PDF) of variables $X$, and $|\theta|$ is the number of parameters of the PDF to be estimated. The PDF can be encoded using a Bayesian factorisation as follows (Koller and Friedman, 2009):

$$
P(X)=\prod_{i=1}^{n} P\left(x_{i} \mid \pi_{x_{i}}\right)
$$

where $x_{i}$ is the node $i$ in the DAG of the Bayesian network and $\Pi_{i}$ is its associated set of parent nodes in the DAG (Figure 6). The PDF is the linear Gaussian model (Koller and Friedman, 2009). Generating new solutions is achieved by sampling the factorisations according to probabilistic logic sampling (PLS) (Henrion, 1988), in which the weak ordering implied by the DAG is considered and the process of generating instantiations of nodes (variables) is guided by their probability.

Figure 6 Example of a Bayesian factorisation
![img-5.jpeg](img-5.jpeg)

Note: $P(X)=P\left(X_{3}\right) \cdot P\left(X_{1} \mid X_{3}\right) \cdot P\left(X_{2} \mid X_{3}\right) \cdot P\left(X_{4} \mid X_{1}\right)$
While the Bayesian network is employed for discovering possible variable interactions within the optimisation process, another additional concept is used for efficient guidance of the optimisation algorithm. Here the basic idea is to construct Gaussian kernel PDFs (a weighted sum of multiple one-dimensional Gaussian functions). For each kernel the value of the $i^{\text {th }}$ variable of selected solutions is used as the means for that variable, $\mu_{i}$. Also, a vector of weights is created according to the following formula:

$$
w_{i}=\frac{1}{q N \sqrt{2 \pi}} e^{-0.5\left[(i-1) / q N\right]^{2}}
$$

In equation (9), $w_{l}$ refers to the weight of solution $l, q$ is a selection pressure and $N$ is the number of solutions (population size). Dividing the weights by the sum of weights gives the probability of choosing each Gaussian function for sampling. Standard deviations of each variable and each $\mathrm{PDF}, \sigma_{l}^{i}$ are defined as the average distance from the chosen solution, $S_{l}$, to other solutions:

$$
\sigma_{l}^{i}=\sum_{k=1}^{N} \frac{\left|S_{l}^{i}-S_{l}^{i}\right|}{N-1}
$$

Therefore, the Gaussian kernel for the variable $i$ is calculated as

$$
G^{i}(x)=\sum_{l=1}^{N} w_{l} \frac{1}{\sigma_{l}^{i}} \sqrt{2 \pi} e^{-0.5\left(\frac{x-\sigma_{l}^{i}}{\sigma_{l}^{i}}\right)^{2}}
$$

The sampling is achieved by choosing a Gaussian PDF according to probabilities and sampling the chosen Gaussian function using a standard normal random number generator.

# 4 Results and discussion 

To present the performance of our approach, the optimisation process is applied to a four-well production model for a five-year course of production. This means that there would be 24 decision variables in the optimisation problem comprising 20 gas rates corresponding to the four wells plus four start times for each well. In fact, the optimisation of 20 gas injection rate variables takes place at five different stages for five time intervals, because each time step has an immediate effect on the decline curves and predicted production values based on the newly constructed model; therefore, the 20 gas rate variables cannot be optimised at once. Upon each function call the model is evaluated based on the NPV and the evolutionary algorithms would use the last optimised solutions as the next generation of promising solutions. The GLP curves for various reservoir pressures are calculated according to step 1 of the presented procedure (Figure 7). The natural decline curves (without any gas injection) for the wells are shown in Figure 8. The incorporated reservoir model is an undersaturated oil reservoir with 150 million STB of initial oil in place and a total compressibility of $8 \times 10^{-6} \mathrm{psi}-1$ at $6,000 \mathrm{psi}$ reservoir pressure. The constraint of limited daily available gas is set to 10 million $\mathrm{scf} /$ day as follows.

$$
\sum_{i=1}^{4} Q_{g} \leq 10
$$

This constraint is fixed for each time interval. Also, no unused gas storage is considered through the optimisation procedure. The optimisation algorithm is implemented in such a way as to handle the estimation of the gas injection and start time variables and parse them according to steps 2 and 3 of the presented workflow. This requires prediction of the reservoir performance corresponding to the estimated gas injection rates and repeating steps 1 through 3 of the stated procedure. At the end of each iteration, the set of generated promising solutions is evaluated based on the NPV function as the objective

function of the current model (step 4). The economic parameters for the NPV calculations are shown in Table 1.

Figure 7 GLP for four wells (see online version for colours)
![img-6.jpeg](img-6.jpeg)

Figure 8 Natural decline curves for four wells (see online version for colours)
![img-7.jpeg](img-7.jpeg)

Table 1 Economic parameters for NPV calculations
For the EDA, the selection pressure $(q)$ is adjusted to 0.6 and the sample size is set to 200 generated solutions in each step. The fixed parameters of the EDA are listed in Table 2. Upon applying the EDA, the optimal starting time of the gas-lift operation for each well and the gas-lift injection rates are determined as shown in Table 3. For more discussion on the results, the optimisation procedure was also carried out based on the initial GLP curves (GLP curves corresponding to 6,000 psi reservoir pressure), and the injection rates were kept fixed during the whole course of the project. We call this scenario the 'base' case, and compare it with other scheduled cases (PSO, GA and EDA).

Table 2 List of EDA parameters

Table 3 Results of NPV maximisation problem
The injection plan obtained from the optimisation procedure results in a $\$ 637$ million NPV. To compare the performance of the EDA, the optimisation procedure was repeated using a simple GA (Haupt and Haupt, 1998) and PSO (Kennedy and Eberhart, 1995).

GA is somewhat similar to EDA in constructing new random solutions in the initiation phase of optimisation and generating new solutions based on promising solutions of the last iteration, but, instead of probabilistic models, the GA procedure includes three main operators, namely, crossover, mutation and selection. Crossover is a means of combining current solutions to obtain new ones; mutation ensures the exploration of the search process; and a selection process is used to choose the appropriate parents (current solutions) to generate promising solutions (Haupt and Haupt, 1998). On the other hand, PSO is a swarm-based optimisation algorithm in which each solution is considered as a particle in the search space. The particles have a velocity attribute which is considered as a means of information flow among particles. The velocity of a particle is updated in each iteration (generation) according to its best record in the search process as well as the global best record among the particles (Kennedy and Eberhart, 1995).

Figure 9 Comparison of EDA performance with GA and PSO (see online version for colours)
![img-8.jpeg](img-8.jpeg)

Comparing the efficiency of the algorithms was carried out via the number of function evaluations (NFEs) needed to achieve an acceptable solution. The best performances of the algorithms after multiple runs are demonstrated in Figure 9. The proposed EDA was capable of achieving a maximum NPV of $\$ 637$ million using fewer than 10,000 function calls, while the best solution obtained by the simple GA results in $\$ 628$ million NPV with a significantly higher NFEs (more than 100,000). Thanks to its information flow concept and swarm intelligence, the simple PSO algorithm performs better than GA. The PSO attains the same best solution with fewer than 25,000 function calls, but again fails to reach the best solution generated by the EDA and becomes stuck in a local optimum. All three evolutionary algorithms suggest the same start times for the lift gas injection, but the allocation of the local optimum obtained by GA and PSO differs from the one obtained by the proposed EDA. The main parameters of the utilised algorithms are their populations and/or sample sizes. For EDA, the size of the initial population is 10 individuals and the archive size (the number of individuals generated by sampling) is 200, while for GA and PSO a fixed population size of 400 is used; this was in order to help GA and PSO to yield better results and improve their performance, because the best results of GA and PSO after multiple runs using a population size of 200 individuals led to an NPV of $\$ 622$ million. The better performance of the EDA lies in its superior probabilistic-based solution construction process. Instead of fixed operators, such as simple mutation and crossover based on current best elite solutions, the EDA builds models and samples the search space based on a larger number of solutions; therefore, the search is more diversified and informed.

For the 'base' case, in which the gas injection rates are kept fixed during the whole course of the operation, the estimated injection rates (which are the same in applying the three evolutionary algorithms) are $3.88,0.99,2.15$ and 2.98 MMscf/day for the four wells. In this case, the predicted value of NPV became $\$ 543$ million, which is rather an undesirable and incompetent outcome compared to the $\$ 637$ million NPV obtained by the EDA. This shows the importance of introducing the start time decision variable into the optimisation problem. Figures 10 to 13 demonstrate the different production profiles of different gas-lift scenarios. Table 4 also summarises the results of these scenarios.

Figure 10 Decline curves for the 'base' case (see online version for colours)
![img-9.jpeg](img-9.jpeg)

Figure 11 Decline curves from GA scenario (see online version for colours)
![img-10.jpeg](img-10.jpeg)

Figure 12 Decline curves from PSO scenario (see online version for colours)
![img-11.jpeg](img-11.jpeg)

Figure 13 Decline curves from EDA scenario (see online version for colours)
![img-12.jpeg](img-12.jpeg)

The results shown in Figure 14 and Table 4 demonstrate the importance of time consideration for a gas-lift operation. The dynamic nature of the GLP curves challenges the accuracy and adequacy of the 'base' case, because this case does not take into account the changing nature of the performance curves over time. On the other hand, the higher potential of natural lift in the early part of the project and the lower value of money at the beginning of the operation encouraged the intelligent algorithms (GA, PSO and EDA) to focus less on the beginning of the project and to dedicate the gas-lift process to the future development of the operation. The local optimum solutions obtained from both GA and PSO are not significantly different from the best EDA solution, but yield $\$ 9$ million NPV less than the EDA result. Though mathematically this may be interpreted as a small difference $(1.4 \%)$, economically there is a significant distinction between these results.

Figure 14 The field production using base, GA, PSO and EDA schedules (see online version for colours)
![img-13.jpeg](img-13.jpeg)

Table 4 Summary of different gas-lift scenario results

# 5 Conclusions 

This study presents an economic approach that addresses the gas-lift allocation problem in a time-dependent manner. The proposed EDA, along with a simple GA and PSO, was used as the optimisation method to find the best injection profiles and gas-lift start times of the wells. Maximising the NPV of the project was considered as the optimisation criterion.

An example of a four-well production system incorporated with a typical reservoir model was used to test the presented optimisation procedure for five years of production. The performance of the optimisation algorithm was compared with two other optimisation algorithms: GA and PSO. Because the evolutionary algorithms are stochastic in nature (as opposed to deterministic) the results from multiple runs sometimes differ, but ultimately each algorithm converges to a definite local solution in most runs based on the implementations, configurations and, most importantly, the nature of the optimisation problem. The results show improved performance of the proposed optimisation algorithm. The underperformance of a non-NPV optimisation approach without considering the effect of the start time of gas-lift as an essential decision variable (the 'base' case) was also demonstrated. For a field with just four gas-lift wells, the EDA optimised schedule led to a $17.3 \%$ increase in profit and it can be expected that for an oil field with a larger number of wells such calculations can make an even more considerable difference. The nonlinearity of the problem made GA and PSO stick at a local optimum and rendered them incapable of finding the EDA solution. This is due to the fixed nature of the optimisation operators of the simple GA and PSO as opposed to the knowledge-based nature of the EDA algorithm. This indicates the inability of fixed operators to achieve global solutions in such problems with high dimensionality. We showed how a more intelligent and efficient optimisation algorithm can help provide better results.

# Appendix A 

The results of the GA for the four-well problem

# Appendix B 

The results of the PSO for the four-well problem
