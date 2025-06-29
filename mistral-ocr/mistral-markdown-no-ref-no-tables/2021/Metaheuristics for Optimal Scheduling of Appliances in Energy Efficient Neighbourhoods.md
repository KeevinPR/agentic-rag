# Metaheuristics for Optimal Scheduling of Appliances in Energy Efficient Neighbourhoods 

Amaia Alfageme ${ }^{1,2}$ (D), Iker Esnaola-Gonzalez ${ }^{1(\boxtimes)}$ (D), Francisco Javier Díez ${ }^{1}$, and Eduardo Gilabert ${ }^{1}$<br>${ }^{1}$ TEKNIKER, Basque Research and Technology Alliance (BRTA), C/Iñaki Goenaga 5, 20600 Eibar, Spain<br>iker.esnaola@tekniker.es<br>${ }^{2}$ Faculty of Informatics, University of the Basque Country (UPV/EHU), Paseo Manuel Lardizabal 1, 20018 Donostia-San Sebastián, Spain


#### Abstract

As a consequence of the continuous growth in the worldwide electricity consumption, supplying all customer electrical requests is becoming increasingly difficult for electricity companies. That is why, they encourage their clients to actively manage their own demand, providing several resources such us their Optimal Demand Profile (ODP). This profile provides to users a summary of the demand they should consume during the day. However, this profile needs to be translated into specific control actions first, such as the when each appliance should be used. In this article a comparison of the performance of two metaheuristic optimisation algorithms (Tabu Search and Estimation of Distribution Algorithm (EDA)) and their variants for the calculation of optimal appliance scheduling is presented. Results show that Tabu Search algorithm can reach better feasible solutions at faster execution times than EDA does.


Keywords: Appliance scheduling optimisation $\cdot$ Optimal Demand
Profile $\cdot$ Tabu Search $\cdot$ Estimation of Distribution Algorithm

## 1 Introduction

Electricity demand is globally increasing as the different sectors require more energy to carry out their tasks. According to the International Energy Agency ${ }^{1}$, in 2018, the industry sector was the sector with the highest consumption, followed by the residential sector. However, the tendency for the residential sector is to increase its electricity consumption more sharply than the rest of the sectors, reaching the industrial sector amounts by 2050 .

Balancing electricity supply and demand is currently a reality among electric companies, who aim to improve these optimisation techniques, and this is

[^0]
[^0]:    ${ }^{1}$ https://www.iea.org/.
    (c) Springer Nature Switzerland AG 2021
    G. Marreiros et al. (Eds.): EPIA 2021, LNAI 12981, pp. 151-162, 2021.
    https://doi.org/10.1007/978-3-030-86230-5_12

why different methods have been proposed, including Demand Side Management (DSM) activities. DSM includes the reduction of electricity usage and shifts of energy usage to other off-peak periods in order to match energy demand with energy supply side [7]. In this regard, Demand Response (DR) [13] programs are introduced into the smart grids as a mechanism for active demand management which implies that the price of energy rises or falls based on a series of circumstances, such as the amount of energy demanded, transport costs, etc.

Some electricity companies encourage their customers to actively manage their demand by providing them a customised Optimal Demand Profile (ODP). This indicates customers how much electricity they should consume at any given time, in order to ensure that they contribute to the energy demand peak reductions and maximisation of renewable energies, among others. The definition of ODP takes into account different features of the electricity grid as a whole, such as the energy price, customer energy production availability, energy storage capacity, and their consumption habits. However, ODPs need to be translated into specific control actions, for instance, by determining the optimal scheduling of appliances.

This article solves the neighbourhood appliances scheduling optimisation problem to adapt households real consumption to neighbourhood ODP. Section 2 analyses the related work, Sect. 3 defines the problem to be solved and the model proposed, and Sect. 4 presents the different variants to be tested. Obtained results are compared and discussed in Sect. 5 and, finally, conclusions are shown in Sect. 6.

# 2 Related Work 

Residential users are expected to play a key role in improving the efficiency of the network through the adoption of intelligent mechanisms for managing the energy demand. This type of networks motivates users to actively manage their daily demand, evaluating energy prices and being participants in the production and storage of electricity $[6,11]$. In fact, the most current lines of research regarding the generation of ODP consider customers capacity to produce renewable energy [1] (photovoltaic generally) and its subsequent storage through batteries.

In [2] the ODP is generated through the prediction of photovoltaic (PV) energy production, user consumption habits according to their electrical appliances, and the electricity taxes. The goal is to minimise the cost on the end users bill. There are different studies about the methods to solve the problem of obtaining the ODP for one or more households. The most applied method is through linear optimisation algorithms, where demand and production flow are defined as linear functions [9]. Also distributed algorithms [5] are considered. The generation of the ODP can be generated for a single household or for several (a neighbourhood), where balancing and coordinating the demand of all households and their joint capacity for electricity production is important.

The most common representation of appliances scheduling solution is by defining the use of each appliance from the solution as $a[t]$ vector where each

position takes 1 value if $a$ has to run at $t$, and 0 otherwise. Some research distinguishes the running mode $(k)$ of appliances [5], where appliances solutions are represented as $a[t, k]$ matrix.

Some models are defined for a single household [10], and others manage residential electricity demand [12] coordinating all households appliances in realtime. In [4] a model for off-grid neighbourhoods is defined, where the ODP is generated through electricity production and storage capability.

The planning problem for the use of household appliances in a neighbourhood can be posed as an NP-hard problem with a discrete number of solutions if the ODP is discretised in units of time. One resolution technique is through heuristic methods and derivatives, where algorithms capable of reaching nearoptimal solutions are proposed when evaluating some of the feasible solutions of the problem. In [14] an hybrid algorithm of Ant Colony and Simulated Annealing algorithms is proposed for a two-stage scheduling optimisation.

# 3 Problem Definition 

As mentioned before, the goal of households is to adjust their demand to their personalised neighbourhood ODP, so that they achieve a reduction in their consumption bill and they contribute to a more sustainable environment by maximising the exploitation of renewable energies. Towards that goal, customers provide their appliances information to the method proposed in this article, specifying the mean consumption by unit of time and the duration of each one. They also indicate the aimed availability, that is, the time range customers would like the appliance to operate. As a result, the proposed method returns the moments of the day when each appliance should be used if the given ODP is aimed.

### 3.1 Representation of the Solution and Objective Function

Solution representation is given as $X$, which is a two dimensional matrix $\left(I_{u} x T\right)$ whose values can be 0 or 1 as shown in Eq. 1.

$$
\begin{aligned}
& X=\left\{\left(x_{1_{1}}^{1}, \ldots, x_{1_{U}}^{1}, \ldots, x_{I_{U}}^{1}, \ldots, x_{I_{U}}^{T}\right) \mid x_{i_{u}}^{t} \in\{0,1\}, \forall u=1, \ldots, U \wedge \forall i=1, \ldots, I \wedge \forall t=1, \ldots, T\right\}\right. \\
& X_{1} \rightarrow\left(\begin{array}{ccc}
x_{1_{1}}^{1} & \cdots & x_{1_{1}}^{T} \\
\vdots & \ddots & \vdots \\
x_{I_{1}}^{1} & \cdots & x_{I_{1}}^{T}
\end{array}\right) \ldots X_{U} \rightarrow\left(\begin{array}{ccc}
x_{1_{U}}^{1} & \cdots & x_{1_{U}}^{T} \\
\vdots & \ddots & \vdots \\
x_{I_{U}}^{1} & \cdots & x_{I_{U}}^{T}
\end{array}\right) \\
& x_{i_{u}}^{t}=\left\{\begin{array}{l}
0 \rightarrow i_{u} \text { off at } t \\
1 \rightarrow i_{u} \text { on at } t
\end{array}\right.
\end{aligned}
$$

The objective is to solve the appliances scheduling optimisation problem minimizing the difference between optimal $(o)$ and real $(r)$ demand, that is, the absolute value of the difference between these two metrics for each instant of time $(t)$.

Optimal demand is unique for all household of the neighbourhood, but real demand is calculated as the sum of the individual fixed $(z)$ and variable demand of each household, where variable demand is composed by the consumption $\left(p_{i}\right)$ of all its appliances $(i)$ as shown in Eq. 2.

$$
\min _{X} f_{o b j}=\sum_{t=1}^{T}\left|\left(\sum_{u=1}^{U}\left(\sum_{i_{u}=1}^{I_{u}}\left(p_{i_{u}} \times x_{i_{u}}^{t}\right)+z_{t, u}\right)-o_{t}\right)\right|
$$

# 3.2 Constraints 

Problem constraints are divided into two. On the one hand, the format constraints, which indicate where the 0 's and 1 's can be located on the solution, and on the other, the value limit constraints, which limit demand values.

The formulated format constraints are:

- Running time of $i_{u}$ appliance is known and must be equal to $y_{i_{u}}$ :

$$
\forall i_{u}\left(\sum_{t=1}^{T} x_{i_{u}}^{t}=y_{i_{u}}\right)
$$

This condition is achieved if the sum of all elements of the solution matrix is equal to the value $y_{i_{u}}$.

- Running time of $i_{u}$ appliance is consecutive:

$$
\forall i_{u}\left(\exists t_{1}=\min \left(t \mid x_{i_{u}}^{t}=1\right), t_{2}=\max \left(t \mid x_{i_{u}}^{t}=1\right) \mid t_{2}-t_{1}=y_{i_{u}}-1\right)
$$

This condition is achieved if the difference between highest and lowest instants of time with 1 value $\left(t_{2}\right.$ and $\left.t_{1}\right)$ for each appliance $i_{u}$ is equal to the number of instants of time that $i_{u}$ must run $\left(y_{i_{u}}\right)$ minus 1.

- Running time of each appliance $i_{u}$ is inside a known time range $\left(w_{i_{u}}=\right.$ $\left.w_{i_{u}}^{\max }-w_{i_{u}}^{\min }+1\right)$ :

$$
\forall x_{i_{u}}^{t}=1 \rightarrow t>w_{i_{u}}^{\min } \wedge t<w_{u}^{\max }
$$

This condition is achieved if all 1 values of each appliance $i_{u}$ are set at $t$ higher than $w_{i_{u}}^{\min }$ and lower than $w_{i_{u}}^{\max }$.

The formulated value limit constraints are:

- For each instant of time, real demand is below a given $d_{\max }$ parameter value:

$$
r_{t}=\sum_{u=1}^{U}\left(z_{t, u}+\sum_{i_{u}=1}^{I_{u}}\left(p_{i_{u}} \times x_{i_{u}}^{t}\right)\right) \leq d_{\max , u} \forall t=1, \ldots, T
$$

This condition is achieved adapting the variable demand (appliances consumption).

- For each instant of time, absolute difference between optimal and real demand is below a given $v_{\max }$ parameter value:

$$
\left|\sum_{u=1}^{U}\left(z_{t, u}+\sum_{i_{u}=1}^{I}\left(p_{i_{u}} \times x_{i_{u}}^{t}\right)\right)-o_{t}\right|=\left|r_{t}-o_{t}\right| \leq v_{\max } \forall t=1, \ldots, T
$$

This condition is achieved adapting the variable demand (appliances consumption).

# 3.3 Search Space 

The set of possible solutions of the problem is composed by all three dimensional matrices limited by the number of households, appliances and instants of time, where format constraints are fulfilled:

$$
\begin{aligned}
X= & \left\{\left(x_{1_{1}}^{1}, \ldots, x_{1_{U}}^{1}, \ldots, x_{I_{U}}^{1}, \ldots, x_{I_{U}}^{T}\right) \mid x_{i_{u}}^{t} \in\{0,1\}, \forall u=1, \ldots, U \wedge \forall i=1, \ldots, I \wedge \forall t=1, \ldots, T\right. \\
& \wedge \forall u \forall i\left(\sum_{t=1}^{T} x_{i_{u}}^{t}=y_{i_{u}}\right) \wedge \forall u \forall i\left(\exists t_{1}=\min \left(t \mid x_{i_{u}}^{t}=1\right), t_{2}=\max \left(t \mid x_{i_{u}}^{t}=1\right)\right. \\
& \left.\left|t_{2}-t_{1}=\sum_{t=1}^{T} x_{i_{u}}^{t}=y_{i_{u}}-1\right)\right\} \\
& \wedge \forall x_{i_{u}}^{t}=1 \rightarrow t>w_{i_{u}}^{\min } \wedge t<w_{i_{u}}^{\max } \}
\end{aligned}
$$

The size of the solution search space is obtained by multiplying the number of positions that each appliance from the solution can take for all neighbourhood households:

$$
\sigma=\prod_{u=1}^{U} \prod_{i=1}^{I}\left(w_{i_{u}}^{\max }-w_{i_{u}}^{\min }-y_{i_{u}}+2\right)=\prod_{u=1}^{U} \prod_{i=1}^{I}\left(w_{i_{u}}-y_{i_{u}}+1\right)
$$

### 3.4 Algorithms for Solving the Problem

Metaheuristic methods are high-level heuristic methods, that is, methods that look for a sub-optimal solution, or in other words, a solution close to the optimal but at reasonable computational cost. This way, they try to overcome the inconveniences from heuristic algorithms, avoiding cycling on local optimas and searching for sub-optimal solutions in a more efficient way.

Considering the model definition, the number of possible solutions of the problem is finite. Dozens or even millions of feasible solutions (with high parameters) can be generated, but there is always possible to determine a discrete amount, that is, the size of the search space is calculable. Therefore, two different metaheuristics techniques have been used for the problem resolution: Tabu Search and Estimation of Distribution Algorithm algorithms. The reason for selecting these two algorithms, is that historically they have had a very scarce presence in problems related to the DSM.

Tabu Search Customization: Tabu Search is an algorithm which uses memory and tabu constraints. The objective is to get closer to the optimal solution of the problem avoiding getting stuck in local optimas by the use of memory. The algorithm stores the movements it has made, and gives priority to other movements that might ease the algorithm to move through other areas of the solutions search space.

- Initial solution: two configurations are defined for the calculation of the initial solution, either randomly, or through greedy heuristic method, starting the execution of the algorithm from a suboptimal solution.
- Neighbourhood system: a strategy is defined to represent the neighbourhood system of a solution, composed by all those feasible solutions in which the starting runtime moment of an appliance from the current solution has been modified. A secondary neighbourhood system is defined as a strategy to get out of local optimas when the algorithm gets stuck. So that, it is composed of all feasible solutions in which the operating moment of two or more household appliances are updated.
- Tabu list: two configuration are defined. The right/left method stores the direction in which the operation of an appliance has moved, that is, left if it is executed at lower time, right otherwise, updating the restriction value on direction column of the corresponding appliance. The position method stores the specific start time of the new operation of an appliance, that is, the restriction value is added to the column that indicates the unit of time for the new start time.
- Additional configurations: a secondary objective function is defined which determines neighbour solution objective value by updating current solution objective value to reduce computational complexity of the problem resolution. Also, the algorithm accepts not feasible solutions in order to widely move throughout solutions search space and to avoid get stuck in local optimas.

Estimation of Distribution Algorithm Customization: Estimation of Distribution Algorithm (EDA) is a derivative of the evolutionary algorithms, based on the probabilistic models learned from a set or population of individuals, to generate new individuals based on mentioned probability distribution. Initially, a population of candidate individuals is generated, then an estimation of the distribution is done from a reduced selection of the population, and finally a new candidate population is generated.

- Initial population: the random method is used, that is, $N$ individuals (or solutions) are randomly selected from the set of feasible solutions of the problem.
- Selection method: Tournament Selection and Rank Selection are compared.
- Probabilistic model, population distribution and sampling: UMDA (Univariate Marginal Distribution Algorithm) probabilistic model adapted to problem variables dependency is applied.

- Additional configurations: an additional technique is applied to control premature convergence, through which a small percentage of cases from sampling process has been reserved to generate solutions that are not feasible in value. Three configurations of the algorithm are defined regarding this percentage of reserved probability $(0,0.01,0.05,0.1 \%)$.


# 4 Experimental Setup 

Different variants of both algorithms have been configured based on the customisation of their hyperparameters as shown in Table 1. For the Tabu Search algorithm variants, the list type (which can take right/left (R/L) and position values) and tabu tenure (which can take values 10,100 and 500) hyperparameter have been combined. As for the EDA, first of all, the UMDA (Univariate Marginal Distribution Algorithm) model has been selected for the generation of new individuals. Then, the selection method (which can take the rank or tournament values) and $\%$ of reserved probability (which can take values $0,0.01,0.05$ and 0.1) hyperparameters have been combined. The performance of all these variants for both algorithms has been calculated and compared between them.

Table 1. Algorithms variants used in the experiments.
All the algorithm variants have been evaluated with pseudo-random data. This pseudo-random consumption data has been generated for a variable number of households and based on the real consumption data and use of household

appliances from a group of dwellers of the Aran Islands (Ireland), Aarhus (Denmark) and Madrid (Spain) who participated in the RESPOND project ${ }^{2}$. This algorithm clusters real appliance consumption data to determine appliance mean consumption, duration and aimed available time range.

More specifically, 30 problem instances have been generated for 10, 100 and 200 households, each one with 1 to 10 appliances with real simulated appliances. Each problem instance has been evaluated 10 times for each algorithm variant, and the execution time and reached suboptimal values have been stored. Then, a comparison has been made between all the variants regarding their performance in terms of execution time and precision on the achieved optimal values, where performance profile and accuracy profile $[3,8]$, have been used to evaluate these metrics.

# 5 Results and Discussion 

The following tables show the results of execution time and optimal values achieved by the objective function after testing both algorithms by its variants.

Table 2 shows the results of the performance obtained by the Tabu Search variants, while Table 3 shows the results of the performance of the EDA variants.

Table 2. Performance of Tabu Search algorithm variants.
[^0]
[^0]:    ${ }^{2}$ http://project-respond.eu/.

Table 3. Performance of EDA algorithm variants.
Regarding the performance of the Tabu Search algorithm variants, less time is required when using the $\mathrm{R} / \mathrm{L}$ instead of position for the tabu list hyperparameter. As a matter of fact, when $\mathrm{R} / \mathrm{L}$ is used, the minimum performance values are reached, specifically when 500 value is used as tabu tenure (TS3). In contrast, when position is set for the tabu list hyperparameter, the algorithm is able to reach more accurate suboptimal values, reaching the best results with a tabu tenure hyperparameter value of 10 (TS4).

As for the EDA algorithm variants, when the rank selection method is set, more accurate optimal values are obtained compared with the tournament selection method. Furthermore, execution times are also lower for the rank selection method. Regarding the performance, the minimum execution time values have been obtained using the rank selection method using the parameter 0.1 (mostly) as percentage of reserved probability (EDA1). Moreover, when tournament selection method has been used, the minimum optimal values have been reached with no probability reserved (EDA5).

Figure 1 shows best mentioned algorithms variants according to their performance and accuracy. A complex scenario is proposed where the EDA4 method is

the one that achieves the best execution times for $58 \%$ of the problems (TS3 do so in the remaining $42 \%$ ), but for the remaining percentage of problems is only able to be second best algorithm for an additional $7.5 \%$. In the remaining $34.5 \%$, TS3 is placed as the second best variant, that is, from the $58 \%$ of problems that TS3 does not lead, it is the second best method in a $\approx 33 \%$ of the problems.

According to optimal values accuracy, TS4 method stands out above the rest, since it obtains a maximum precision value ( $\approx 5$ points) in $83 \%$ of the executions, while TS3 does so in $17 \%$ and EDA algorithm variants are not able to reach this value.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Best variants execution time performance (a) and optimal values accuracy (b) comparison.

Tabu Search algorithm is the one that has obtained the best results both in terms of performance at execution time and precision of reached optimal values from all different problems. TS3 variant (tabu list R/L and tabu tenure of 500) is the best when execution time is prioritised, and TS4 variant (position tabu list and tabu tenure of 10) has highlighted in obtaining the lowest possible optimal values. Since the values of any parameter of the methods do not match, it is observed that the average performance values of TS4 method are $128.82 \%$ greater than those shown by TS3, while TS3 presents optimal values $38.76 \%$ higher. Thus, TS3 method is selected as the best variant of Tabu Search algorithm and for the hole comparison.

This algorithm applied to organise the use of household appliances can lead to a considerable decrease in the final bill. Users with electricity price of $0.10 € / \mathrm{kWh}$ who are able to produce and store their own electrical energy through renewable sources, and whose home is $100 \%$ electric could save more than $35 \%$ of his final bill, depending on the optimal conditions of electricity production.

# 6 Conclusion 

The ODP represents the optimal amount of electrical demand to be consumed by customers in order to, on the one hand, help electric companies balance energy

supply and demand, and on the other, help customers reduce their monthly bills and contribute to a more sustainable environment. To do so, users adapt the use of their appliances to approximate their total consumption to the target ODP, although it can sometimes be difficult for users to make this approximation.

This paper analyses two metaheuristic algorithms for neighbourhood appliances scheduling optimisation problem by comparing several variants for each of them. The algorithms are applied for neighbourhood scenario with various households, where each one pretends to adapt its appliances uses to adjust the demand to an optimal demand profile previously provided by its electricity supplier. When ODPs are defined to maximise the use of the energy produced by neighbourhoods, the defined algorithms organise the use of household appliances in such a way that the use of the energy produced by the users is maximised, thus reducing the cost of purchasing and transporting electricity. In addition, the energy prices provided by the supplier company are taken into account, trying to balance the cheapest prices with users consumption habits.

After evaluating all algorithms variants through 30 problem instances, Tabu Search algorithm variants have performed better results than EDA both for execution time and reached optimal values. When R/L tabu list and 500 tabu tenure are used, fastest execution time values are obtained, but lowest optimal values are reached when position tabu list is selected. However, this second variant gets very high computational time values, so the best algorithm for neighbourhood appliances use optimisation problem guided by ODP is Tabu Search, in particular when it is customised with R/L tabu list and 500 tabu tenure.

Acknowledgements. This work was supported by the SPRI-Basque Government's project 3KIA [grant number KK-2020/00049] of the ELKARTEK program.
