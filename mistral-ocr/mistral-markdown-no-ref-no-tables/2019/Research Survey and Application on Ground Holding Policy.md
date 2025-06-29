# Research Survey and Application on Ground Holding Policy 

Yongjie Yan<br>State Key Laboratory of Air Traffic Management System and Technology The 28th Research Institute of China Electronics Technology Group Corporation Nanjing, China<br>yanyongjie41403@sina.com

Yan Zhang<br>The 28th Research Institute of China Electronics Technology Group Corporation Nanjing, China<br>zylavender2010@163.com

Jing Tian
State Key Laboratory of Air Traffic Management System and Technology The 28th Research Institute of China Electronics Technology Group Corporation Nanjing, China
mooky@qq.com


#### Abstract

This paper introduces the origination, concept of ground holding policy and research literature review firstly. Next, three types of models are built for single airport ground holding problem (SAGHP), multi airport ground holding problem (MAGHP) and dynamic single airport ground holding problem (dSAGHP). For solving algorithms, two conventional methods of First Come First Served (FCFS) and dynamic Sequencing Window are explained briefly, then one heuristic algorithm named Estimation of Distribution Algorithm (EDA) is illustrated in detail to solve the ground delay problems, including problem-specific modeling, probability learning and new solutions sampling. Finally, experiment results based on simulation instances and discussions are given.


Keywords-Air Traffic Flow Management, Single Airport Ground Holding Problem, Multi-objective Optimization, Estimation of Distribution Algorithm

## I. INTRODUCTION

With the development of social economy and the continual growth of civil aviation, military aviation and general aviation, the pressure for air traffic management (ATM) becomes larger and aviation safety has raised more concern than ever. In order to ensure the flights safety, ATM department has to further utilize airspace resource with the novel technologies, by using the flow control measures, to control the aircraft flow under the capacity of airspace and controllers, and guarantee the safety of air traffic operations. However, till now, "flow control" in China is lack of information support, technology support and decision making support, meanwhile, decision making depends on the experience of controllers, without collaboration with other stakeholders in ATM. The output policies given by controllers are not stable but with high randomness. Therefore, it becomes one critical problem that how to realize flow control scientifically and reasonably. This paper aims to investigate effective solutions, based on the systematic study on one common and popular ATFM measure Ground Delay Program (GDP), which is a typical ATFM measure of ground holding.

## II. Literature REVIEW

## A. Origination of Ground Delay Program

In 1960s, national airspace system could not satisfy the rapid increase of transportation. In order to issue the problem of delay caused by air holding, FAA proposed arrival measure program, and converted arrival delay into en route, with the cooperation of en route measure program. These two
technologies compose the initial flight flow management method in USA.

Later, with the increase of air traffic flow, a lot of researches on ground delay approach were conducted, with the idea of transferring arrival delay into departure delay. Due to arrangement of traffic flow, capacity change by weather, local airspace congestion could make flights hold in the air, which increases fuel consumption and influences flight safety. In order to cover the situation, it becomes one important ATFM policy that postpones some flights later than their scheduled departure time, to realize balancing the traffic flow and capacity of airport and airspace. The essence of ground delay is to transfer from air holding with high cost to ground delay with lower cost. If all the delay flights could be controlled before departure, both economic and social benefits will be very high.

## B. Concept of Ground Delay Program

Ground Delay Program (GDP) is one important method to solve congestion problem in short time, because ground delay is much cheaper and safer than air holding. As a result, one airport could be very congesting, if all scheduled flights try to arrive on time. One possible way is to delay departure time of some flights, until the capacity of airport is restored. The critical issue of GDP is to determine which flights have to wait and how long they have to.

Flight plan, including scheduled flights and extra section flight, could be known 24 hours before. The capacity of airspace and airport could be predicted by weather forecast. Based on information of demand coming from flight plan and capacity given by weather forecast, ATFM controllers make a decision to use GDP, if there is imbalance between demand and capacity. When GDP is applied, assign some ground delay time to some flights, to avoid too long time of air holding, decreasing lose and improving the safety level.

GDP can be divided into two parts: stochastic part and dynamic part. Firstly, the capacity of airport is stochastic, because it depends on weather condition and is very hard to accurately forecast. Dynamic means expected departure time, arrival time and capacity of airport require adjusting with time.

Making use of GDP aims to minimize the total delay cost, satisfying airports and routes capacity constraints. In the domain of GDP, there are two sub-problems: single airport ground delay program (SAGDP) and multi airport ground delay program (MAGDP). In this paper, we mainly discuss single airport GDP. In MAGDP, more than one airport or

sector's capacity decrease, which makes the problem much more complicated. Single airport ground delay program is basic problem of GDP, including static SAGDP and dynamic SAGDP.

## C. Literature Review

From 1980s, a great many of GDP researches have already been conducted by researchers and institute, and several approaches and papers have been completed [1]. In the early 1990s, USA applied GDP to practical Air Traffic Flow Management (ATFM), distributed by ARTSCC. In 1987, Andeatta and Romanin-Jacur firstly tried to build mathematic model to solve slot assignment problem in GDP. Dynamic programming was used to assign departure time slots for flights, minimizing the total delay costs. In 1990, Terrab and Kolitz focused on single airport ground delay program problem, and developed minimal cost dynamic programming algorithm for stochastic SAGDP. Several experiential equation were also proposed. During 1992 and 1994, Vranas, Bertsima, Odoni et al conducted research on multi airport ground delay program by analyzing real time performance, and some heuristic algorithms were proposed in their papers. In 1993, Richetta and Odoni studied the stochastic SAGDP problem by minimal cost flow, and made comparisons on 4 methods given by them. In 1995, Richetta solved dynamic ground holding model with the dynamic linear programming. Robert Hoffman developed mathematic model for single airport ground holding problem with aircraft constraints in 1997. Andreatta and Brunetta well studied multi airport ground holding problems and built AT model in 1998. Later Bertsimas and Patterson enhanced the research, by adding en route capacity constraints, flights cancel and route change, to the problem of ground holding problem. In 2000, Christos Pangyioto et al proposed priority disturb analysis method, aiming to solve dynamic GHP problems. In 2001, Fabrizio Rossi et al developed enhanced branch and bound method to solve GDP problem, by analyzing the flights cancel influence.

In China, many theoretical research and application development started from middle of 1990s [2]. In 1995, Hu and Chen studied single airport ground holding problems, analyzing two mathematic models with deterministic capacity and stochastic capacity. In 1997, Hu and Qian studied the model and method of multi airport ground holding problems, proposed integer programming model for deterministic MAGHP, and a heuristic algorithm was developed. One year later, they gave model of deterministic multi airport ground holding policy, proposing AI based algorithm, and discussed stochastic MAGHP problem [3]. In year 2000, Hu, Li et al built a modified network flow programming model to solve SAGHP problem effectively, with simple network model and more practical operational constraints. In 2003, Luo and Zhang developed SAGHP model based on discrete event system (DES), involving deterministic model and stochastic model with runway service time. In 2004, Fan and Wang solved SAGHP with one neural network based heuristic algorithm.

## III. MATHEMATIC MODEL OF GDP

## A. Problem Description

If there is only one airport overcrowded, the capacity of airport could be estimated beforehand. Under the constraint
of satisfying airport capacity, ground holding time of each flight is calculated, to minimize the total delay costs. The situation mentioned above is simplified as Single Airport Ground Holding Policy problem (SAGHP), which is shown in Fig. 1.

SAGHP makes assumption of the following:

1) During time period $[0, \mathrm{~T}]$, there are totally N flights landing at destination airport Z , which are represented as set $F=\{1,2, \ldots, N\}$;
2) During time period $[0, \mathrm{~T}]$, there is only one capacity constrained airport $Z$;
![img-0.jpeg](img-0.jpeg)

Fig. 1. Single airport ground holding policy problem
3) The time period $[0, T]$ can be equally divided into T slots: $1,2, \ldots, \mathrm{~T}$;
4) Holding cost function is assumed in linear, under the reasonable air holding time (no longer than existing maximal air holding time), and other non-linear factors as safety are ignored;
5) For each flight, the scheduled departure time and flight time of each air route are known. Cost of air delay and ground delay can be calculated by departure time given.

As a sum, SAGHP is described as: for a given destination airport, under the constraints of airport capacity (AAR: airport arrival rate), assign ground holding time for each flight to minimize the total delay cost.

Airport capacity is defined as maximal landing airplanes during a given time period (usually 1 hour). If the forecasting capacity is static, the corresponding problem is called deterministic SAGHP, if impact of weather is considered, capacity of airport is not deterministic but stochastic. Usually the capacity is modeled as following some distribution, such as normal distribution. In that case, ground holding time and air holding time are required to be considered simultaneously. This problem is called stochastic SAGHP. In next subsection, several types of mathematic models are given in detail.

## B. Deterministic Single Airport Ground Holding Problem

The capacity of airport Z is assumed to be known beforehand and defined as deterministic time based function [4]. The mathematic model of deterministic SAGHP is given:

$$
\begin{aligned}
& \min \sum_{i=1}^{N} \sum_{j=}^{m+1} G_{i j} X_{i j} \\
& \text { s.t. } \sum_{j=m_{i}}^{m+1} X_{i j}=1 \quad \forall i \in F \\
& \sum_{i=1}^{N} X_{i j} \leq K_{j} \quad \forall j \in T
\end{aligned}
$$

$$
X_{i j}=\left\{\begin{array}{l}
1, \text { if flight } i \text { landing in period } j \\
0, \text { else }
\end{array}\right.
$$

where $m_{i}$ represents the index of landing time period of flight $i, \mathrm{G}_{\mathrm{ij}}$ represents the cost of flight i arrival at time slot $j$, and $\mathrm{K}_{\mathrm{j}}$ is the airport capacity in slot $j$. Equation (2) ensures that each flight has one and only one arrival slot. Equation (3) is constraints of airport capacity for each slot, guaranteeing the balance between capacity and demand.

## C. Stochastic Single Airport Ground Holding Problem

For stochastic SAGHP, decision maker has to determine arrival time and departure time of each flight. However, the airport capacity is not static, so that the problem can be viewed as various of possibilities of scenarios [5]. The objective output has to be evaluated by all possible scenarios. As a result, the model is given as follows:

$$
\begin{gathered}
\operatorname{Min} \sum_{q=1}^{Q} \operatorname{Cost}(q) \operatorname{Pr} o b(q) \\
\operatorname{Cost}(q)=\sum_{K=1}^{K} \sum_{i=1}^{T} \sum_{j=i+1}^{T=1} C_{g}(j-i) X_{q j}^{k i}+C_{a} \sum W_{q i} \\
\text { s.t. } \sum_{j=1}^{T+1} X_{q j}^{k i}=N_{k i} \quad k=1,2, \cdots, K, i=1,2, \cdots, T \\
W_{q i} \geq \sum_{k=1}^{K} \sum_{j=1}^{i}\left(X_{q i}^{k i}+W_{q i-1}-M_{q i}\right) \quad i=1,2, \cdots, T+1 \\
X_{q j}^{k i} W_{q i} \in N^{+} \quad \forall q \in\{1,2, \cdots, Q\}
\end{gathered}
$$

where $\mathrm{N}_{\mathrm{ki}}$ represents expected number of type K aircrafts during slot $i, \mathrm{M}_{\mathrm{qi}}$ is the airport capacity during slot $i$ under scenario $q, \mathrm{X}_{\mathrm{qi}}{ }^{\mathrm{ki}}$ means the number of type K aircrafts, whose scheduled arrival time is at slot $i$ and calculated arrival time is at slot $j$ under the scenario $q, \mathrm{~W}_{\mathrm{qi}}$ represents the number of aircrafts in air holding during slot $i$ under the scenario $q$. Equation (7) ensures the flights with scheduled arrival time $i$ must be assigned a new arrival slot equal or later than $i$, equation (8) guarantees capacity and demand balancing for each time period, equation (9) is non-negative constraint.

For deterministic model, the decision variable focuses on single flight, while for stochastic model, the decision variable is the flight set of arrival time from slot $i$ to $j$.

## D. Dynamic Single Airport Ground Holding Problem

With update of capacity forecasting information, no matter whether a flight is allowed to departure or ground holding, one new decision is made to possibly decrease the delay cost by ground and air holding. Thereafter, departure time has to be well considered. Dynamic capacity forecasting is modeled with the tree structure of scenario probability. One capacity forecasting having Q scenarios at least contains Q stages. In each stage, for airport arrival rate in future, the probabilities of each scenario are static. Therefore, dynamic programming for ground holding problems is to re-assign at the beginning time of each stage. The mathematic model is proposed as follows:

$$
\operatorname{Min} \sum_{q=1}^{Q} \operatorname{Cost}(q) \operatorname{Pr} o b(q)
$$

$$
\begin{gathered}
\operatorname{Cost}(q)=\sum_{K=i, j=1}^{K} \sum_{j=i+1}^{T=1} C_{g}(j-i) X_{q j}^{K i s}+C_{a} \sum W_{q i} \\
X_{q j}^{K i s}=X_{q+1, j}^{K i s}=\cdots=X_{q j}^{K i s} \\
\text { s.t. } \quad s=1,2, \cdots, Q-1 ; k=1,2, \cdots, K \\
i=t,+1, \cdots, T ; i \leq j \leq T+1 \\
\sum_{j=1}^{T+1} X_{q j}^{k i}=N_{k i s} \quad k=1,2, \cdots, K, i=1,2, \cdots, T \\
W_{q i} \geq \sum_{k=1}^{K} \sum_{j=1}^{T}\left(X_{q j}^{k i}+W_{q i-1}-M_{q i}\right) \\
i=1,2, \cdots, T+1 \quad q \in\{1,2, \cdots, Q\} \\
X_{q j}^{k i} W_{q i} \in N^{+} \quad \forall q \in\{1,2, \cdots, Q\}
\end{gathered}
$$

where $\mathrm{N}_{\mathrm{ksi}}$ represents expected number of aircrafts departing at slot $s$ and arriving at airport Z with slot $i . \mathrm{X}_{\mathrm{qi}}{ }^{\mathrm{ki} s}$ is the number of type K aircrafts arriving at airport Z under the scenario $q$, whose scheduled departure time is at slot $s$, scheduled arrival time is at slot $i$ and calculated arrival time is at slot $j$

## E. Multi-objective Single Airport Ground Holding Problem

In this paper, we propose one multi-objective optimization model for SAGHP, due to limitation of paper, MAGHP could be taken as future work.

From various papers conducted in the field of ground holding policy, usually delay cost is taken as one optimization criterion, besides, there are several other kinds of criteria to be well considered [6]. In this paper, we also consider fairness measure. Fairness measure is defined as the standard deviation among all airline companies. The deviation means the averaged deviation with optimal solution for aircrafts of each airline company.

As one multi-objective optimization problem, the mathematic model is proposed as follows:

$$
\begin{gathered}
\operatorname{Min} \omega_{f j} \times \sum_{i=1}^{N} \sum_{j=1}^{M}\left(c_{i j} \times x_{i j}\right)+\omega_{f^{\prime}} \times F\left(x_{i j}\right) \\
\text { s.t. } x_{i j}=\left\{\begin{array}{l}
1, \text { if flight } i \text { being assigned to slot } j \\
0, \text { else }
\end{array}\right. \\
c_{i j}=\omega_{i} \times\left(t_{j}-S L D T_{i}\right) \\
\sum_{j=1}^{M} x_{i j}=1 \\
\sum_{i=1}^{N} x_{i j} \leq 1 \\
t_{j} \geq S L D T_{i}, \quad \text { if } \quad x_{i j}=1 \\
d\left(x_{i j}\right)=\max \left(0,\left(\sum_{i=1}^{N} \sum_{j=1}^{M} c_{i j} \times x_{i j}-\sum_{i=1}^{N} c_{i}^{2}\right)\right) \\
m d\left(x_{i j}\right)=\frac{d\left(x_{i j}\right)-\min _{j=1}^{j=N} d\left(x_{i j}\right)}{\max ^{d}\left(x_{i j}\right)-\min ^{d}\left(x_{i j}\right)} \\
f_{q}\left(x_{i j}\right)=\frac{\sum_{i=1}^{N} n d\left(x_{i j}\right)}{N_{q}}
\end{gathered}
$$

$$
F\left(x_{i j}\right)=\frac{1}{Q} \sqrt{\left(f_{q}\left(x_{i j}\right)-f_{q}\left(x_{i j}\right)\right)^{2}}
$$

where in equation (17), $\mathrm{x}_{\mathrm{ij}}$ is binary value to represent whether flight $i$ is assigned to $j$. Equation (18) is used to calculate delay cost by comparing assigned slot time with scheduled time. Equation (19) is used to calculate a constraint for each flight, there is one and only one slot time assigned for it, and equation (20) shows that for one slot time, at most one flight can be assigned for it. Scheduled time constraints are shown in equation (21), that is for each flight, assigned slot time can not be earlier than scheduled one. Equation (22) and (23) are used to calculate the deviation and normalized deviation of calculated delay cost and optimal delay cost of $\mathrm{x}_{\mathrm{ij}}$. Equation (24) is used to calculate averaged normalization deviation for each airline company, and finally the fairness measure as standard deviation of all companies is defined in equation (25).

Notions:


## IV. Solving Algorithm and Discussion

Ground holding problem is one typical combinational optimization problem. The procedure of sequencing optimization is to assign all flights slot time, and to determine new position for each flight. At present, there are several popular and effective algorithms proposed, such as First Come First Served (FCFS), dynamic sequencing window and meta-heuristic algorithm [7].

## A. First Come First Served (FCFS)

The algorithm of FCFS is based on the sequence of expect time of arrival (ETA), to decide the sequence of approach and landing. When one flight enters the terminal sequence area, system will calculate its ETA, based on time of entering terminal, performance data of aircraft, and weather information. Next, system will give the corresponding aircraft the scheduled time of arrival (STA), with the help of calculated ETA and existing sequencing flights. If the interval of aircrafts queue is not suitable for inserting aircraft $i$, system will re-sequence all aircrafts after aircraft $i$ by ground holding or air holding, guaranteeing all aircrafts satisfying the interval standard. If the aircrafts can not be re-sequenced, system will give the instruction that aircraft $i$ has to hold in the air in a specific airspace, until the
interval of aircrafts queue satisfies. The flowchart of FCFS is shown in Fig. 2.

## B. Dynamic Sequencing Window

When we try to decide the new position for aircraft $i$, due to constraints of swap range, it will be trapped into low searching performance if we check all aircrafts. Alternative method is to pick up related aircrafts and search one suitable position among them. In this way, the calculation time could be decreased a lot, which is called dynamic sequencing windows algorithm, sequencing aircrafts through building time window dynamically.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Flowchart of FCFS algorithm
The main steps of algorithm are shown in Fig. 3: Firstly, model of sequencing window is built, including size of sequencing window (number of aircrafts in the window), moving step length, and separation step length (number of aircrafts separated after sequence window backward each time). At each time, only the aircrafts in the window are calculated and sequenced. Then the window moves backwards depending on the moving length, and the first several aircrafts in new window are added into the already decided queue.

## C. Heuristic Algorithm

For solving combinational optimization problems, lots of heuristic algorithms and meta-heuristic algorithms are developed, such as generic algorithms (GAs), simulated annealing (SA), particle swarm optimization (PSO), and ant colony optimization (ACO). All these algorithms have become popular techniques for finding satisfactory solutions within reasonable computation time [8].

The conventional GAs largely depend on the manner of crossover, mutation and the corresponding parameters. How to tune parameters becomes a critical task [9]. Different problems require different crossover probability.

Unfortunately, there is no special rule to guide how to set up those appropriate parameters, which is a state-of-the-art problem. Furthermore, for some complex problems, operators of crossover and mutation cannot ensure to get an optimal solution and how to deeply utilize the current promising data towards the final optimal solution is always one critical issue in the population-based optimization algorithms. Then, one probability model based algorithm without crossover is developed, called Estimation of Distribution Algorithm (EDA) [10], trying to overcome the drawback of conventional GAs.
![img-4.jpeg](img-4.jpeg)

Fig. 3. Flowchart of dynamic sequencing window
Compared with the conventional methods, the key point of EDA is using the probabilistic model to describe the distribution of value selection for each decision variable. The probability is extracted from some promising date coming from all candidate solutions. From lots of previous literatures, EDAs can achieve better optimality on some benchmark problems, especially when the decision variables are dependent due to a high level of interaction [11]. Flowchart of generic EDA is shown in Fig. 4.

For algorithm of EDA, the key points are probability model/matrix, method of sampling and estimation. In next subsections, we mainly discuss these three parts:
(a) Probability model/matrix

For one specific problem or application, the core issue is to construct the probability model [12]. In ground holding problems, the target is to minimize delay cost by determining slot assignment. As a result, we design the probability matrix to represent the probability of slot assignment for each flight. The probability matrix is:

$$
\mathrm{P}(t)=\left[\begin{array}{ccc}
p_{t 1} & \cdots \cdots & p_{t M} \\
\cdots & p_{g} & \cdots \cdots \\
p_{N 1} & \cdots \cdots & p_{N M}
\end{array}\right]
$$

where $\mathrm{p}_{\mathrm{ij}}$ in matrix means the priority value of flight $i$ for the slot $j$. Initially we set each value as $1 / \mathrm{J}$.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Flowchart of generic EDA
(b) Sampling method

In order to simplify the problems, we make the assumption that decision variables are independent. Therefore, when we generate next generation population, for slot $j$, only one column $j$ is required to be calculated.

Take the slot 1 (first column in matrix) for example. As shown in Fig. 5, in left side, $\mathrm{p}_{t 1}$ represents the probability of flight $i$ being assigned to slot 1 . For example, $\mathrm{p}_{11}=0.2$ and $\mathrm{p}_{21}=0.4$, it means the probabilities of flight 1 and 2 choosing slot 1 are $20 \%$ and $40 \%$, and flight 2 has higher priority than flight 1 for slot 1 . The total sum of probabilities is $100 \%$. From the right side, it shows some individuals sampled based on probability independently. The first gene of each individual represents the flight assignment for slot 1 . Based on $\mathrm{p}_{t 1}$, for each individual, we sample one flight as first bit. We also generate other positions with same manner, so that populations of N individuals are sampled.
(c) Estimation method

The process of estimation is to learn the probability matrix by some promising data. First step is to select some promising individuals as training data, based on given objectives. Next step is probability learning/updating. Based on the assumption of independent variables, we update the probability matrix for each column, without considering other columns.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Sampling method based on probability independently

The probability model is learned from the current promising data, but it may make the transition probability unstable, so we calculate the probability by:

$$
P_{t}(X=x)=(1-\lambda) \times P_{t-1}(X=x)+\lambda \times P_{t}^{r}(X=x)
$$

where $\lambda$ is the learning rate for the current generation, specially, the distribution is completely learned from the current one if $\lambda=1$.

## D. Discussion

In this subsection, some practical constraints are discussed for ground holding policy and problems in ATFM.

1) If there are some conflicts among flights, assign them according to the priority of flights;
2) Arrange the time interval of flight schedule with the unit of 5 minutes;
3) Assign the departure time of one flight. The capacity of destination airport should be considered, and vice versa;
4) In one time period, if there are some flights postponed from last period to this period, priority will be higher.

In general, the priority of flights is ranking according the following rules: (1) International flight has higher priority than one domestic flight; (2) The flight gaining scheduled departure time earlier has higher priority; (3) The flight that has more scheduled days has higher priority; (4) The large type aircraft has higher priority than smaller type one. It has to mention that, the priority level of one flight is not static, depending on the time period of ground holding.

Finally all flights are classified into three types: time-based-priority, flight-type-priority, and delay-period-priority. In three types of priorities, time-based-priority is more important than the other two.

## V. EXPERIMENT

In order to demonstrate the models and algorithms discussed above, we select two hour simulation flights (20:55-22:50) as a test case. Each time slot is 5 minutes. During periods $21: 00-21: 05,22: 00-22: 05,22: 05-22: 10$, 22:10-22:15, 22:30-22:35, demand is higher than capacity, which is shown with red and yellow color in Fig. 6. After regulation, for each time period, the expected traffic flows are represented by the right column with blue color. It is found that all flows are under the capacity constraints.

TABLE I. CTOT AND SUGGESTION




![img-5.jpeg](img-5.jpeg)

Fig. 6. Traffic flow and capacity before and after sequencing
In Table I, it shows the scheduled and calculated take off time (CTOT) for partial flights. Some suggestions about ground delay time are also given.

## VI. CONCLUSION

Airport ground holding policy is one popular ATFM measure for solving airport demand and capacity unbalancing. From theoretical evaluation and practical exercise, it has proved to be one appropriate method. In early periods, departure time is given by controllers based on his/her own experience, having neither historic and real time data nor decision support system. The models and algorithms for SAGHP/MAGHP provide one way to assist controllers to apply ground holding policy more reasonably and effectively.
