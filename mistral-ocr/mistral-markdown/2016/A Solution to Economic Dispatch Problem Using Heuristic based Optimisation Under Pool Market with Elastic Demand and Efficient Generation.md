# A Solution to Economic Dispatch Problem Using Heuristic based Optimisation Under Pool Market with Elastic Demand and Efficient Generation 

Debraj Das, Baishali Mullick, S.Prabhakar Karthikeyan<br>School of Electrical Engineering, VIT University, Vellore, Tamil Nadu, India. 632014<br>debraj.das2012@vit.ac.in, baishali.mullick2012@vit.ac.in, spk25in@yahoo.co.in


#### Abstract

With the current level of pollution in atmosphere caused by fossil fuel emissions, coupled with the ominous fuel scarcity, efficient generation at the power stations is necessary. This paper proposes a multi-objective optimization model to maximize social welfare using the Bees Foraging Algorithm (BFA) and Estimation of Distribution Algorithm (EDA) highlighting the importance of treating generator efficiency parameters along with generation bid. This is because the generator bids alone are a poor representation of efficiency, being influenced by economic attitudes. Along with Economic Load Dispatch (ELD), the model reduces fossil fuel emissions and increases the efficiency of operating generators through curtailment to shift the operating point of generators to a more efficient region, while maintaining constraints of the system. The generation side curtailment is reflected on distribution side, where curtailment schemes based on the willingness to pay of the consumer and priority based incentive is used, thereby performing environmental dispatch. The improved efficiency reduces fuel consumption per MW thereby reducing fuel cost (Rsch) and emission (ton/h), therefore maintaining generation efficiency with profit retention. The paper therefore establish that Independent System Operator (ISO), by real-time control of incentives and curtailment, encourage efficient consumption pattern among consumers and production among generating companies (GENCO). The results confirm that the proposed model benefits the society i.e. consumers, power producers and the environment.


Keywords-Economic Load Dispatch; load curtailment; generator efficiency; bees foraging algorithm; Estimation of distribution algorithm

## I. InTRODUCTION

The traditional electric power systems minimizes the total fuel cost without due consideration of fuel emissions [2]. Electric power systems maximize the social welfare by minimizing the generator bids. The generator bid is a poor representation of the efficiency, often trumped by economic attitudes. The paper identifies efficiency as a individual parameter and develops an economic dispatch model. Here, the consumer demand is met with optimum generator schedules, where, along with the generator cost, its emission and operating efficiency is taken into account. From Fig 1, it is seen that the multi-objective algorithm primarily focuses on: (1) Minimization of fuel cost of the generating units, (2) Minimization of the total emission, (3) Maximization of
consumer utility bid and (4) Maintaining efficiency of generators and (5) economic Demand Response Management .
![img-0.jpeg](img-0.jpeg)

Fig. 1. Proposed optimal dispatch model [10]
The emissions from fossil fuel generators include harmful greenhouse gases like $\mathrm{CO}_{2}, \mathrm{SO}_{2} \mathrm{NO}_{x}$ etc. The emissions per unit of electricity are estimated to be in the range of 0.91 to $0.95 \mathrm{~kg} / \mathrm{kWh}$ for $\mathrm{CO}_{2}, 6.94$ to $7.20 \mathrm{~g} / \mathrm{kWh}$ for $\mathrm{SO}_{2}$, and 4.22 to $4.38 \mathrm{~g} / \mathrm{kWh}$ for $\mathrm{NO}_{x}$ during the period 2001-02 to 2009-10 [3]. A study by the International Energy Agency (IEA), indicates electricity production accounts for $32 \%$ of total global fossil fuel use and around $41 \%$ of total energy-related $\mathrm{CO}_{2}$ emissions. If all countries produce electricity at maximum efficiencies, the energy savings capacity and ability to reduce $\mathrm{CO}_{2}$ emission observed were $42 \%$ for coal, $52 \%$ for natural gas and $45 \%$ for oil-fired power generation, corresponds to 10 EJ and 860 Mtonne $\mathrm{CO}_{2}$, respectively [4].

The optimization model developed in this paper aims at maximization of the social welfare function. The power transactions between GENCOs and Utilities is carried out by the ISO. Thus from the perspective of the ISO, maximization of the consumer bid and minimization of the generator bid maintains optimum economic welfare of the society. The paper proposes to schedule the GENCOs such that the efficiency is maximized and emission produced by GENCOs is minimized. To meet the objective, the paper presents two load curtailment schemes for profit retentive curtailment transfer from the generation to the load. The required load curtailment is derived from the economic load dispatch (ELD), wherein to maintain generation efficiency the reduction in supply is reflected on the demand side such that the system power balance is maintained.

## II. POOL MARKET STRUCTURE

In a centralized pool market, the Independent System Operator (ISO) plays the role of economic power exchange between the generator side (GENCO) and the consumer side [6]. In such a model, the generating companies participating in the pool market, submit their generation bids at which they are ready to sell unit power to the ISO. Similarly the consumers submit their respective market bids to the pool at which they are ready to buy unit power from the ISO. The economic load dispatch is scheduled by the ISO so as to minimize the overall generation cost while the consumer bids are selected and demand power is allocated in such a way that maximizes the overall consumer benefit thereby maximizing the objective function, i.e., the social welfare of the system [14] [7].

It is noted that quadratic functions have been used to represent the generation cost function instead of stepped bids. Owing to unexpected changes in the generation bids due to several unknown factors, stepped bids do not give a true representation of the cost function thus quadratic bids are generally used [8].

## III. PROPOSED EFFICIENCY MANAGEMENT

Even today the world often depends on fossil fuel to meet their energy requirements due to its reliability [11]. Due to GENCOs capital outlay, fuel distribution, waste management, subsidies and taxes, generation bid is a poor representation of the plant efficiency which is used by the ISO for the Economic dispatch. For efficient dispatch, efficiency as a parameter should be factored in load dispatch.

Every machine has their efficient operating points. Intelligent Demand side Management reflecting generation curtailment for efficiency is the ideal solution to the minimization of environmental issues of fuel scarcity and pollution from power generation.

The efficiency of the generators indicate energy usage and the total output of the generator compared to the fuel fed. Diesel generators are mostly operated at a fraction of their rated capacity for issues of generation reserves and incorrect generator sizing, and often kept on standby to offset the cost of startup and shutdown. The general idea is that efficiency decreases with decrease in load or on overloading. Therefore generators must be run near their optimum points for optimum efficiency.

The algorithm moves the operating points of the generators to their efficient region by supply reduction and reflection of this on the demand side as curtailment. In case of curtailment limit violation it can redistribute the load on other generators which may result in marginal decrease in individual efficiency, but overall increase in efficiency of the system.

## IV. DEMAND RESPONSE MANAGEMENT

The smart grid system enables consumers to participate in the energy management process through introduction of Advanced Metering Infrastructure wherein consumers can make smart decisions towards energy management and efficiency improvement [10]. Demand Response (DR) is an
important ingredient of the emerging smart grid paradigm. [10][13] . This paper proposes curtailment schemes based on two DR programs i.e. price-based demand response (PDR) and incentive-based demand response (IDR). These encourage customers to change their consumption habits according to variable electricity prices or incentivizes participating customers for reducing their electricity usage on DR requests [12] respectively. The first scheme is based on the consumer's price responsiveness to changes in demand. The incremental consumer bid is an indication of the consumer's willingness to pay. Thus a higher willingness to pay indicates that the consumer is capable of paying more for electricity price per unit of power. The slope of the consumer bid curve indicates the willingness to pay [1]. Thus
willingness to pay $=\tan \theta=(f(d 2)-f(d 1)) /(d 2-d 1)$
where $d 1$ and $d 2$ are two points on the bid curve as shown in equation 1.

The demand side curtailment is inversely proportional to willingness to pay. Thus based on the willingness to pay of the two consumers the curtailment is done such that the consumer with higher willingness to pay will have lower power curtailed.

The second scheme implements an incentive demand response in which the consumers are given incentives by utilities in order to reduce a certain amount of load during certain hours of the day. This system is based on incentive bids released by the consumer units into the market. Based on the bids, the DR utility arranges the curtailment in such a way that minimizes the total incentives paid. Here the incentive bids are assumed to be quadratic in nature. Thus the minimization of the total incentives gives the power curtailments allotted to the various consumers. IDR programs in the smart grid, enables the demand response provider (DRP) to perform prioritization of individual power curtailments and incentives [12]. For example Electric Reliability Council of Texas (ERCOT) offers several energy incentive programs where federal customers can receive rewards for allowing load curtailments. Some of these programs are: Load Resource Participation in the Ancillary Services Markets, Voluntary Load Response [20].These DR schemes for load curtailment impose changes in the consumer power usage habit thereby infusing a power saving habit into consumers.

## V. PROBLEM FORMULATION

The economic/environment load dispatch finds the optimal combination of the power generating schedules satisfying the demand such that the individual generators operate in/near their most efficient regions, emissions are at their lowest, and that the system runs at the minimum cost.

The essential constraints considered in the model are; Equation (2), the power balance constraint where power produced by generators is consumed by customers. Equation (3), the power limit constraints i.e. the generators operate

within their specified range and equation (4), a limit to the maximum allowed curtailment given by the $C^{\max }$ [1].

List of Constraints:

$$
\begin{gathered}
\Sigma G_{i}=\Sigma D_{i} \\
P_{i}{ }^{\min }<G_{i}<P_{i}^{\max } \\
\Sigma C<C^{\max }
\end{gathered}
$$

$C^{\max }=\Sigma$ (maximum limit of requested demand) $-\Sigma$ (minimum limit of requested demand).

The concept entails curtailment on both generators and consumers and does not concern the revenue loss suffered by the GENCOs, TRANSCOs and DISCOMs. It is tested on a 3 generator 2 load system. Generators in the system are assumed to be diesel in nature.

The success of market dictated utility operation requires the bids to reflect the true costs of generation and demand bids [8]. Therefore the assumed generating cost function is of the form given in equation (5).

$$
\begin{gathered}
G_{i}=a P_{i}^{2}+b P_{i}+c+P e n_{i} \\
P e n_{i}=F\left(C_{i}, L_{i}\right)
\end{gathered}
$$

F is the penalty function as decided by the ISO as in equation (6). The consumer benefit function is represented in equation (7).

$$
C_{i}=p D_{i}^{2}+q D_{i}+r
$$

The emissions function given in equation (8) is also assumed to be a quadratic[16].

$$
E m_{i}=I P_{i}^{2}+m P_{i}+n
$$

The coefficients of the equations (5), (7) and (8) are given in Tables I and II. Both minimization of emission as well as reduction of fuel cost is required for the optimal production of power. This economic/environmental dispatch problem deals with competing objectives such that some reasonable trade off between the two objectives is made. [2] [15].

The multi-objective optimization model considers the following objectives (1) Social Welfare with desired operating conditions given by equation (9) [1], (2) Minimum Emission given by equation (10) and (3) Maximum efficiency in equation (11). The efficiency of the generator is taken from individual generator's efficiency vs. load curve to identify the high efficiency regions.

$$
\text { ISO benefit }=\Sigma C_{i}\left(D_{i}\right)-\Sigma G_{i}\left(P_{i}, C_{i}, L_{i}\right)
$$

Where: $D_{i}=$ Demand of Consumer
$G_{i}$ : Generator bid function of $i^{\text {th }}$ generator
$C_{i}$ : Consumer bid function of the $i^{\text {th }}$ consumer
$P_{i}$ : Power Generated by $i^{\text {th }}$ generator
$C_{i}$ : The Curtailment On generation
$L:$ Limit violation

$$
A=\operatorname{Min}\left(\Sigma E m_{i}\left(P_{i}\right)\right)
$$

Where: $E m_{i}=$ Emission function of $i^{\text {th }}$ generator

$$
B=\operatorname{Max}\left(\Sigma \eta_{i}\left(P_{i}\right)\right)
$$

$\eta_{i}=$ efficiency of $i^{\text {th }}$ generator at its operating point
The model is tuneable and ISO is at liberty to decide the priority of the schedules as in equation (12) and therefore can alter the coefficients of the augmented objective function i.e. $\alpha, \beta$, and $\gamma$ to alter the focus of the algorithm among the objectives and $\delta$ to control amount of curtailment and thereby to control his economic losses born out of curtailment.

$$
Y=\alpha \times \text { ISO benefit }+\beta \times A+\gamma \times B+\delta \times \Sigma C_{i}
$$

TABLE I. COEFFICIENT OF GENERATOR AND CONSUMER BID FUNCTIONS[8]

| Generator | $\mathbf{P}_{\text {min }}(\mathbf{M W})$ | $\mathbf{P}_{\text {max }}(\mathbf{M W})$ | a | b | c |
| :-- | :--: | :--: | :--: | :--: | :--: |
| G1 | 50 | 500 | 0.003 | 2 | 80 |
| G2 | 50 | 500 | 0.015 | 1.45 | 100 |
| G3 | 50 | 500 | 0.01 | 0.95 | 120 |
| Consumer | $\mathbf{P}_{\text {min }}(\mathbf{M W})$ | $\mathbf{P}_{\text {max }}(\mathbf{M W})$ | $\mathbf{p}$ | $\mathbf{q}$ | $\mathbf{r}$ |
| C1 | 50 | 500 | -0.002 | 5 | 150 |
| C2 | 50 | 650 | -0.001 | 6 | 200 |

TABLE II. COEFFICIENTS OF EMISSION FUNCTION [2]

| Emission | $\mathbf{1}$ | $\mathbf{m}$ | $\mathbf{n}$ |
| :-- | :--: | :--: | :--: |
| Em1 | 0.016 | -1.5 | 23.33 |
| Em2 | 0.031 | -1.82 | 21.022 |
| Em3 | 0.013 | -1.249 | 22.050 |

## VI. RESULTS AND DISCUSSIONS

Estimation of Distribution Algorithm (EDA) and Bees Foraging Algorithm (BFA) has been used to implement the proposed dispatch model. Tables III and Table IV shows the variation of social welfare function before considering efficiency of generation and after considering it using both the algorithms respectively. For optimal production a trade-off is necessary between the competing objectives: economic dispatch and generation efficiency management. Inclusion of efficiency reduces the overall social welfare in turn increasing

efficiency as shown by Fig 2. [11] The demand column indicates arbitrarily ISO set demands for the dispatch model.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Generator operating points for different dispatch methods at demand=700MW and corresponding change in efficiency using EDA [11].

TABLE III. VARIATION OF SOCIAL WELEARE FUNCTION BEFORE AND AFTER TAKING GENERATION EFFICIENCY INTO CONSIDERATION USING EDA

| Demand <br> (MW) |  | Generator <br> fuel <br> cost(Rs/hr) | Consumer <br> bid <br> (Rs/hr) | Social Welfare <br> function(Rs/hr) | Emission <br> (tonne/hr) |
| :--: | :-- | :--: | :--: | :--: | :--: |
| 700 | Before | 2592.9703 | 4070 | 1477.0296 | 1957.6704 |
|  | After | 2493.4445 | 3975.0332 | 1481.5887 | 1946.9441 |
| 600 | Before | 2116.0356 | 3592.4995 | 1476.4639 | 1327.0303 |
|  | After | 2025.4536 | 3511.8019 | 1486.3482 | 1333.8133 |
| 500 | Before | 1688.2354 | 3092.4929 | 1404.2575 | 816.9570 |
|  | After | 1609.3063 | 3008.8833 | 1399.5770 | 809.9070 |
| 400 | Before | 1309.9510 | 2572.4991 | 1262.5480 | 427.0788 |
|  | After | 1240.3826 | 2485.6637 | 1245.2811 | 424.4068 |

TABLE IV. VARIATION OF SOCIAL WELEARE FUNCTION BEFORE AND AFTER TAKING GENERATION EFFICIENCY INTO CONSIDERATION USING BFA

| Demand <br> (MW) |  | Generator <br> fuel <br> cost(Rs/hr) | Consumer <br> bid <br> (Rs/hr) | Social Welfare <br> function(Rs/hr) | Emission <br> (tonne/hr) |
| :--: | :-- | :--: | :--: | :--: | :--: |
| 700 | Before | 2564.2547 | 4067.8613 | 1503.6066 | 2029.9299 |
|  | After | 2620.5461 | 3978.1835 | 1357.6370 | 2026.6091 |
| 600 | Before | 2084.1042 | 3557.0529 | 1472.9487 | 1378.5951 |
|  | After | 2188.3959 | 3489.6328 | 1301.2369 | 1303.1417 |
| 500 | Before | 1669.8093 | 3094.5419 | 1424.7325 | 923.82501 |
|  | After | 1683.7768 | 2955.7770 | 1272.0002 | 832.2835 |
| 400 | Before | 1289.2091 | 2579.5693 | 1290.3602 | 477.0225 |
|  | After | 1291.3334 | 2471.6155 | 1180.2820 | 467.2074 |

In Fig 2, the efficiency curve has been used for all the generators. The comparison of operating points shows that the proposed load dispatch algorithm results in higher efficiencies for the generators as shown in Fig 2.

Method 1: Shows traditional ELD
Method 2: Shows ELD with efficiency as objective, neglecting emissions

Method 3: Proposed algorithm with both emission and efficiency as objectives.

TABLE V. GENERATOR AND LOAD SCHEDULES BEFORE AND AFTER CURTAILMENT USING BFA

|  | Demand <br> (MW) | $\mathbf{7 0 0}$ | $\mathbf{6 0 0}$ |
| :-- | :-- | :--: | :--: |
| Pg1(MW) | Before curtailment | 289.6115 | 219.6987 |
|  | After curtailment | 283.6697 | 216.3791 |
| Pg2(mw) | Before curtailment | 173.8934 | 134.1830 |
|  | After curtailment | 165.6578 | 118.4946 |
| Pg3(MW) | Before curtailment | 236.4950 | 246.1181 |
|  | After curtailment | 230.6726 | 245.1263 |
| Pd1(MW) | Before curtailment | 75.0 | 78.2608 |
|  | After curtailment | 68.5 | 71.7608 |
| Pd2(MW) | Before curtailment | 625.0 | 521.7391 |
|  | After curtailment | 611.5 | 508.2391 |
| Objective <br> function <br> (Rs/h) | Final value | 1357.6370 | 1301.2369 |

## A. Emission minimization

The proposed algorithm using EDA shows significant reduction in emission compared to the traditional ELD, as shown in Fig 3. Thus if a compromise is made using the proposed algorithm a suitable balance can be achieved between the environmental and economic aspect of power generation thereby greatly reducing harmful emission levels in the process.

## B. Results of demand response management

The Table V shows the variation of generated power and demand power before and after curtailment using BFA. At the generation side, efficiency management is done through reduction in supply power in order to shift the operating point to a higher efficiency region of the curve as shown in Fig 2. The new supply is given in the Table V. This reduction in generation is reflected to the demand side through prioritized curtailment sharing and curtailment based on price responsiveness to Demand.

1) Curtailment based on price responsiveness of demand

The willingness to pay by the two consumers are found from their respective consumer bids and the curtailment is prioritized. Thus from Table VI Consumer 1 has lower willingness to pay and thereby has higher curtailment than Consumer 2.

## 2) Curtailment based on incentive bids

The incentive bids of the two consumers are arbitrarily assumed as in equations (13) and (14):
$\operatorname{Bid}_{1}=4 * \mathrm{x}_{1}{ }^{2}+4^{*} \mathrm{x}_{1}$
(13) , Bid $_{2}=2 * \mathrm{x}_{2}{ }^{2}+2 * \mathrm{x}_{2}$

Where $x_{l}$ and $x_{2}$ are curtailments of the two consumer units.

Thus from Table VII for minimization of the total incentive to be paid by the DR utility at ISO demand of 700 MW, the curtailment for Consumer 1 was found to be lower than that of Consumer 2. This can be explained with an example: suppose the Consumer 1 is a hospital unit and the Consumer 2 is a residential home. The hospital requires more incentive to curtail unit power compared to the home unit.

Thus decreasing curtailment for the hospital and increasing curtailment for the home will minimize the total incentive payable by the utility

TABLE VI. PRICE BASED CURTAILMENT

| Demand <br> (MW) | Willingness <br> to pay of <br> Consumer 1 <br> (Rs/MWh) | Willingness <br> to pay of <br> Consumer 2 <br> (Rs/MWh) | Curtailment <br> of <br> Consumer 1 <br> (MW) | Curtailment <br> of <br> Consumer 2 <br> (MW) |
| :-- | :-- | :-- | :-- | :-- |
| 700 | 4.33 | 4.933 | 10.6509 | 9.3490 |
| 600 | 4.594 | 5.001 | 10.4241 | 9.5758 |

TABLE VII. INCENTIVE BASED CURTAILMENT

| Demand <br> (MW) | Incentive bid <br> of Consumer <br> $\mathbf{1}(\mathbf{R s} / \mathbf{h})$ | Incentive bid <br> of Consumer <br> $\mathbf{2}(\mathbf{R s} / \mathbf{h})$ | Curtailment <br> of <br> Consumer 1 <br> (MW) | Curtailment <br> of <br> Consumer 2 <br> (MW) |
| :-- | :-- | :-- | :-- | :-- |
| 700 | 195.0 | 391.5 | 6.5 | 13.5 |

![img-2.jpeg](img-2.jpeg)

Fig. 3. Variation of emission values in traditional ELD and proposed ELD using EDA

## VII. CONCLUDING REMARKS

The current market which orients towards profit and stable economy ignores sustainability and the effects of fossil fuel emission. Apart from the capital investment, operation and maintenance costs, fossil fuels have external costs indirectly borne by society that are unaccounted for, such as damage to human health due to pollutant emission, land damaged due to mining activities, environmental pollution etc. Therefore it is not only important to have economic dispatch but also to consider environmental impact i.e. focusing on efficiency by both generating plants and consumers.

Although fossil fuels cause ecological damage, these conventional energy sources have high reliability and are more controllable than renewable energy sources such as wind energy, solar energy etc. Till now the power system cannot depend completely on non-conventional sources due to less reliability. Thus fossil fuel scarcity poses a threat to stable and reliable power generation. Generation at higher efficiency ensures reduction in fuel consumption and fuel cost thus maintaining reliability.

The curtailment technique proposed in this paper involves providing credits similar to production tax credit (PTC). PTC encourages development and integration of wind farms. This concept can be used to incentivize consumers so that they cooperate with the ISO to allow scheduled load shedding.

Prioritizing load curtailment with respect to the willingness to pay by the consumer also allows participation of consumer in the decisions of load curtailment scheduling. Incorporation of such systems by the ISO inculcates a practice of energy saving in consumers.

## VIII. APPENDIX A: OVERVIEW OF PROPOSED ALOGRITHMS

## A. Bees Foraging Algorithm

Bees Foraging Algorithm emulates the navigating and foraging behaviour of bees. Bees algorithm demonstrates the swarm based communication between bees in deciding suitable nectar sites which is comparable to finding the most optimal point in a solution space

## 1) Bees in nature

Scout bees set out to scan some neighbourhood patches and return back to communicate about the quality and distance of the visited patches to the other foraging bees through a form of dancing called 'waggle dance' [17] . The lesser fit nectar sites are discarded and more scout bees are recruited for better fit sites. Thus more scout bees are sent to elite sites (having higher fitness) than other sites. The bees take their decision based on swarm communication. [18].

## 2) Flowchart of BFA algorithm

![img-3.jpeg](img-3.jpeg)

Fig. 4. Flowchart of bees algorithm.

## B. Estimation of Distribution Algorithm

## 1) Theory of $E D A$

EDA is an optimization strategy where candidate solutions is a representation of variables of the problem at hand. Each candidate solution is called Individual and are not directly dependent on other individuals in the problem. A probability distribution (PD) is maintained which is updated by the best $\mathrm{k} \%$ of the population, rest of the population is mutated with the help of new Individuals created from the shared PD. It is to be noted for the multi-variable approach in the problem, global probability for each variable is maintained separately i.e. every individual follows a set of independent PD. [19].

## 2) Flowchart of EDA algorithm

![img-4.jpeg](img-4.jpeg)

Fig. 5. Flowchart of EDA

## REFERENCES

[1] Chanda Sandip, and Abhinandan De, "A multi-objective solution algorithm for optimum utilization of smart grid infrastructure towards social welfare.", International Journal of Electrical Power \& Energy Systems 58 (2014), pp.307-318.
[2] Mishra Neha, and Manjaree Pandit, "Environmental/Economic Power Dispatch Problem Using Particle Swarm Optimization.", International Journal of Electronics and Computer Science Engineering (IJECSE) 2.02 (2013), pp. 512-519.
[3] Mittal, Moti L., Chhemendra Sharma, and Richa Singh, "Estimates of emissions from coal fired thermal power plants in India.", 2012 International Emission Inventory Conference. 2012, pp. 13-16.
[4] Graus, W. H. J., M. Voogt and E. Worrell, "International comparison of energy efficiency of fossil power generation.", Energy policy 35.7 (2007), pp. 3936-3951.
[5] Demirel, Y., and A. Demiroren, "Economic and minimum emission dispatch.", energy 2.1 (2004), p. 12
[6] S. Stoff, Power System Economics: Designing Markets For Electricity. IEEE Press:John Wiley and Sons, 2002.
[7] R. D. Christie, B. F. Woolenberg, and I. Wangensteen, "Transmission management in the deregulated environment," Proceedings of the IEEE, vol. 88, no. 2, pp. 170-195, February 2000.
[8] Bijuna Kunju, K., and PS Nagendra Rao, "Determination of market clearing price in pool markets with elastic Demand.", Fifteenth National Power Systems Conference (NPSC), IIT Bombay. 2008.
[9] M. A. Abido, " Multi objective particle swarm optimization for environmental/ economic dispatch". Electric Power Syst. Res . 79, pp. $1105-1113,2009$.
[10] Rahimi, Farrokh, and Ali Ipakchi. "Demand response as a market resource under the smart grid paradigm." Smart Grid, IEEE Transactions on 1.1 (2010): 82-88.
[11] Katiraei, Farid, and Chad Abbey. "Diesel plant sizing and performance analysis of a remote wind-diesel microgrid." Power Engineering Society General Meeting, 2007. IEEE. IEEE, 2007.
[12] Gong, Y., Cai, Y., Guo, Y. and Fang, Y., 2015. A Privacy-Preserving Scheme for Incentive-Based Demand Response in the Smart Grid.U. DOE, "Benefits of demand response in electricity markets and recommendations for achieving them," 2006.
[13] U. DOE, "Benefits of demand response in electricity markets and recommendations for achieving them," 2006.
[14] J. Vara Prasad, Dr. K.Chandra Sekhar, " A Novel Approach for Social Welfare Maximization in day-ahead Market during Congestion Period ", journal of ElectricalEngineering(JEE),Volume12/2012,Issue:4,Article:6, pp.1-7.
[15] King, Robert TF Ah, Harry CS Rughooputh, and Kalyanmoy Deb. "Evolutionary multi-objective environmental/economic dispatch: Stochastic versus deterministic approaches." Evolutionary MultiCriterion Optimization. Springer Berlin Heidelberg, 2005.
[16] Mbamalu, George AN. "Effect of demand prioritization and load curtailment policy on minimum emission dispatch." Electric Power Systems Research53.1 (2000): 1-5.
[17] Pham, D.T., Ghanbarzadeh, A., Koc, E., Otri, S., Rahim, S. and Zaidi, M., 2011, July. The Bees Algorithm-A Novel Tool for Complex Optimization. InIntelligent Production Machines and Systems-2nd $1^{\text {st }}$ PROMS Virtual International Conference 3-14 July 2006 (p. 454). Elsevier.
[18] Quijano, Nicanor, and Kevin M. Passino. "Honey bee social foraging algorithms for resource allocation: Theory and application." Engineering Applications of Artificial Intelligence 23.6 (2010): 845-861.
[19] Paul, Topon Kumar, and Hitoshi Iba. "Linear and combinatorial optimizations by estimation of distribution algorithms." 9th MPS symposium on Evolutionary Computation, IPSJ, Japan. Vol. 12. 2002.
[20] http://energy.gov/eere/femp/energy-incentive-programs-texas