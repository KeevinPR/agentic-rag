# An improved estimation of distribution algorithm for multi-compartment electric vehicle routing problem 

SHEN Yindong ${ }^{1, *}$, PENG Liwen ${ }^{1}$, and LI Jingpeng ${ }^{2}$<br>1. Key Laboratory of Image Processing and Intelligent Control, School of Artificial Intelligence and Automation, Huazhong<br>University of Science and Technology, Wuhan 430074, China; 2. Division of Computing Science and Mathematics, University of Stirling, Stirling FK94LA, UK


#### Abstract

The multi-compartment electric vehicle routing problem (EVRP) with soft time window and multiple charging types (MCEVRP-STW\&MCT) is studied, in which electric multi-compartment vehicles that are environmentally friendly but need to be recharged in course of transport process, are employed. A mathematical model for this optimization problem is established with the objective of minimizing the function composed of vehicle cost, distribution cost, time window penalty cost and charging service cost. To solve the problem, an estimation of the distribution algorithm based on Lévy flight (EDA-LF) is proposed to perform a local search at each iteration to prevent the algorithm from falling into local optimum. Experimental results demonstrate that the EDA-LF algorithm can find better solutions and has stronger robustness than the basic EDA algorithm. In addition, when comparing with existing algorithms, the result shows that the EDA-LF can often get better solutions in a relatively short time when solving medium and large-scale instances. Further experiments show that using electric multi-compartment vehicles to deliver incompatible products can produce better results than using traditional fuel vehicles.


Keywords: multi-compartment vehicle routing problem, electric vehicle routing problem (EVRP), soft time window, multiple charging type, estimation of distribution algorithm (EDA), Lévy flight.

DOI: 10.23919/JSEE.2021.000030

## 1. Introduction

The vehicle routing problem (VRP) was first developed by Dantzig and Ramser in 1959, which is a typical NPhard problem in combinatorial optimization. VRP has been studied extensively and rich research results have been achieved [1], in many of which only one type of products is considered. However, in many practical applications of VRP, more than one type of products are in-

[^0]volved and some are incompatible. Typical examples include (i) cold chain logistics [2] with refrigerated and nonrefrigerated products, in which product deterioration and low satisfaction for customers will be caused if these two types of products are mixed together in the same compartment in the course of distribution; (ii) domestic waste collection [3] with many types of products from different recycling boxes, in which mixing all types of garbage will increase the extra workload and even lead to the failure of this recycling task; and (iii) fuel delivery [4] with multiple petroleum products, in which mixing all types of oil will directly affect the performance of oil and even cause safety accidents. Moreover, the cost will be greatly increased if all incompatible products are separately distributed by vehicles with single compartment [5]. Therefore, considering the transport efficiency and cost, the capacity of a vehicle can be split into several compartments to serve different types of products simultaneously and the multi-compartment vehicle routing problem (MCVRP) is coined [6].

In addition to the above three applications, MCVRP is also applied in many other fields, such as grocery distribution [7], blood transportation [8], livestock feed distribution [9], milk collection problem [10] and so on. However, to the best of our knowledge, all research on MCVRP uses internal combustion engine vehicles, which increases the emission of greenhouse gases, pollutes the environment and consumes non-renewable energy. In recent years, government has started to take actions to reduce greenhouse gas emissions and noise levels by encouraging the adoption of electric vehicles (EVs). Many logistics companies now use EV fleets and their number is steadily increasing [11]. In view of this, we attempt to apply EVs to MCVRP and make a green distribution plan for the transportation of incompatible products. Moreover, considering that the soft time window is conducive to


[^0]:    Manuscript received November 30, 2020.
    *Corresponding author.
    This work was supported by the National Natural Science Foundation of China (71571076) and the National Key R\&D Program for the 13th-Five-Year-Plan of China (2018YFF0300301).

flexible distribution [12] and multiple charging types are conducive to flexible charging to better meet the time window and reduce expenses [13], and we also take these two factors which exist in reality into our problem. At this moment, a new problem, i.e., the multi-compartment EV routing problem with soft time window and multiple charging types (MCEVRP-STW\&MCT), is proposed which uses a comprehensive objective function that minimizes the total cost of fixed vehicle cost, distribution cost, penalty cost, and charging service cost.

Compared with the basic MCVRP, when combined with the electric VRP (EVRP), the routing decisions are more challenging in presence of the practical constraints, such as soft time window constraints, multi-compartment capacity constraints, power constraints and multiple charging types considerations. Therefore, the MCEVRP-STW \& MCT is a complex problem that requires innovative solution approaches. Considering that the MCVRP is an extension of the VRP and the estimation of the distribution algorithm (EDA) has a good performance in solving the VRP $[14,15]$, in this paper we develop an EDA based on Lévy flight (EDA-LF) to solve the MCEVRP-STW\& MCT. The EDA-LF algorithm performs a Lévy flight local search at each iteration to help EDA to effectively break out of the local optimum. Meanwhile, for comparison purpose, the performance is compared between the EDALF algorithm, the basic EDA algorithm without Lévy flight, and an existing algorithm. And the cost difference of the MCVRP between using EVs and traditional fuel vehicles is also compared.

The remainder of this paper is organized as follows. Section 2 reviews the relevant literature. Section 3 describes the problem and formulates the MCEVRP-STW\& MCT model. Section 4 describes the concrete procedures of the proposed EDA-LF algorithm. Section 5 presents the computational experiments and the analysis on the results. Finally, conclusions are drawn in Section 6.

## 2. Literature survey

With the increase of application scenarios, MCVRP has gradually attracted the attention of researchers in recent years. Note that this paper studies an MCVRP combined with EVs, so we first review work on the MCVRP and then discuss the EVRP.

### 2.1 MCVRP

The MCVRP, which involves vehicles with different compartments for the storage of different products, is a variant of the VRP. At present, there are four kinds of popular MCVRP studies and a literature review of these different aspects is as follows.
(i) MCVRP with heterogeneous fleet

In this case, the vehicles are not exactly the same in terms of vehicle capacity, driving speed, etc. Zhang et al. used multi-compartment vehicles with different capacities and different proportions of compartments for product oil distribution, and proposed a parallel neighborhood searching algorithm of relocation and exchange operators to obtain the optimized routing scheme of vehicles [4]. With the development of practical application and research, some scholars study this problem by considering flexible compartment sizes in which the size can be selected arbitrarily. Henke et al. introduced an MCVRP with flexible compartment sizes in the context of glass waste recycling in Germany in that glass of different colors should be collected separately, and a branch-and-cut algorithm was developed as the solution approach [16].
(ii) MCVRP with time windows

In this case, each customer has the requirement of service period. According to the customer's strictness of the time window, there are two categories, depending on whether hard time windows or soft time windows are used. The former refers to the situation that the customers must be served in the time windows, and the latter refers to that the time windows can be violated if the penalty is paid. Chen and Shi studied an MCVRP with time windows for urban distribution and proposed a hybrid particle swarm optimization with simulated annealing to solve it [17]. Zhan et al. established a multi-objective mathematical model for MCVRP with soft time windows and heterogeneous fleet, then proposed a variable neighborhood search algorithm for it [18].
(iii) MCVRP with split delivery

It reflects the customer's need for multiple products that can be split separately in different vehicles. Wang et al. studied a heterogeneous fixed fleet MCVRP with split delivery in which the demand for each product must be attended in a single visit, and proposed a hybrid guided reactive tabu search algorithm to solve it [19]. Furthermore, in order to split the demand more completely, Zhang et al. allowed to split delivery and each product to be delivered by multiple vehicles, and finally obtained a better distribution scheme [4].
(iv) MCVRP with stochastic factors

The stochastic factors mainly include stochastic demands or travel time. Goodson developed methods to calculate the expected time of the initial arrival to a particular customer on a priori route for the MCVRP with stochastic demands, and then described a cyclic-order simulated annealing algorithm for it [20]. Lu and Wang proposed a model of clustered multi-temperature joint distribution with fuzzy travel times, and the discrete firefly algorithm is developed to solve it effectively [21].

It is important to note that the existing MCVRP with

time window publications only use fuel vehicles for transportation and do not address the EVs.

### 2.2 EVRP

The EVRP focuses on scheduling EVs to optimize both economic and environmental costs during the distribution process. In contrast with distribution of traditional fuel vehicles, the facts that EVs are not capable of finishing a long distance due to its limited battery capacity and the number of charging stations is limited greatly increase the difficulty in solving this problem. Existing literature on EVRP often considers various factors specific to EVs, mainly including four and a literature review of these different aspects are as follows.
(i) Charging mode

At present, there are mainly six charging modes, namely slow, regular, fast charging [22], multiple charging [13], swapping battery [23], battery swaps and recharging capability which coexist in each station. Different charging modes correspond to different charging time and service price. Generally, slow charging takes 4 to 8 hours, regular charging spends 2 to 3 hours and fast charging needs 30 minutes to 1 hour [24], while swapping a new fully recharging battery takes only about 5 minutes [23] but building a battery swapping infrastructure is expensive and the battery swapping mode requires higher technology. In particular, the mode of multiple charging types provides a variety of optional charging rates and gets different recharging durations, which helps to better meet the customer's time window and reduce energy costs. Catay and Keskin made a study firstly that extended the modeling of EVRP with hard time windows to include multiple charging options, and solved it by CPLEX. The results showed that multiple charging options may reduce the fleet size and decrease the energy costs for small-size problems such as 15 customers [25]. Then, Keskin and Catay modeled the EVRP with hard time windows by allowing partial recharges with three recharging configurations which can be referred to as normal, fast and super-fast recharges, and developed a metaheuristic approach which couples the adaptive large neighborhood search approach with an exact method. The experimental results based on large-size instances and instances with tight time windows demonstrate the benefits of using multiple charging types in terms of the fleet size and the energy costs [13].
(ii) Electricity consumption

Earlier studies considered that the amount of battery discharged was either directly proportional to the distance traveled [25] or further related to vehicle load [26]. Recent researches consider a comprehensive and more realistic power estimation function that includes all im-
portant parameters such as speed, acceleration, load and grade [27].
(iii) Charging time

Some studies assume that it is constant which is a plausible assumption in applications where the charging station replaces a (partially) depleted battery with a fully charged one [24]. Other researchers consider that the battery level is assumed to be a linear function of the charging time [28] which is used in most researches. A few studies suggest that the actual charging function should be modeled as nonlinear [29].
(iv) Charging strategy

Firstly, according to whether partial charging is allowed, it can be divided into partial charging [30] and full charging. The former can reduce the charging time and better meet the time window, but it is more difficult to deal with. The latter is easier to solve and more concerned about charging time. Then, according to whether the charging station can be visited many times, it can be divided into single visit and multiple visits. Moreover, Desaulniers et al. [31] considered four variants of the EVRP with time windows as following and presented exact branch-price-and-cut algorithms for each: i) single full recharge; ii) multiple full recharges; iii) single partial recharge; iv) multiple partial recharges.

## 3. Problem description and formulation

### 3.1 Problem description

The MCEVRP-STW\&MCT can be defined as follows. A depot has a series of homogeneous EVs. Each EV has multiple fixed size compartments. The size of the compartments can be different and each compartment is assigned to a product. A compartment must not be loaded more than its capacity. Customers have demand for different types of products which must be put into different compartments. Each customer receives service only once by a vehicle. Vehicles deliver products to customers within a given soft time windows and early or late deliveries need to be penalized. The delivery must wait until the start of the window when the vehicle arrives early. Suppose that the service time of the vehicle providing service for a customer is proportional to the customer's demand and the ratio is 24 kg per minute. Each EV starts and ends at the depot. And as there is a restriction provided by the battery capacity, EV needs to visit the charging station nearest to the current customer point to recharge fully when it is found that the power at the next customer point is lower than the warning line for the remaining power. Since charging stations may be visited multiple times by the same vehicle or different vehicles, we create a sufficient number of copies and allow at most

one visit to each. Moreover, each station is equipped with three types of charging (i.e., slow, regular and fast charging) but only one is used at each visit to the station. The objective is to minimize the total cost, composed of fixed EV cost, distribution cost, penalty cost of violating the time window, and charging service cost.

### 3.2 Symbol definition

To facilitate reading, symbols related to sets, parameters and decision variables used in the MCEVRP-STW\&MCT are summarized as follows.
(i) Sets
$N$ : set of customers;
$R$ : set of charging stations;
$R^{\prime}$ : set of charging stations with their copies;
$V$ : set of nodes $V=O \cup N \cup R^{\prime} \cup O^{\prime}, O$ is the start depot node and $O^{\prime}$ is the end depot node;
$K$ : set of homogeneous vehicles;
$P$ : set of products.
(ii) Parameters
$C$ : total cost;
$C_{\text {veh }}$ : fixed vehicle cost;
$C_{\text {trans }}$ : distribution cost;
$C_{\text {penalty }}$ : penalty cost of violating the time window;
$C_{\text {service }}$ : charging service cost;
$c_{1}$ : per-unit fixed vehicle cost;
$c_{2}$ : per-unit distance distribution cost;
$c_{3}$ : per-unit early arrival penalty cost;
$c_{4}$ : per-unit delay arrival penalty cost;
$c_{e 1}$ : per-unit service cost for slow charging;
$c_{e 2}$ : per-unit service cost for regular charging;
$c_{e 3}$ : per-unit service cost for fast charging;
$\beta_{1}$ : slow charging rate;
$\beta_{2}$ : regular charging rate;
$\beta_{3}$ : fast charging rate;
$d_{i j}$ : distance from node $i$ to node $j$;
$Q_{p}$ : capacity of the compartment $p$;
$q_{i p}$ : demand of customer $i$ for product $p$;
$v_{0}$ : vehicle speed;
$e$ : per-unit distance power consumption;
$B$ : battery capacity of the vehicles;
$R B$ : remaining power warning line of the vehicles;
$T_{S i}$ : service time of customer $i$;
$T_{E i}$ : earliest arrival time at customer $i$;
$T_{L i}$ : latest arrival time at customer $i$;
$M$ : large enough constant.
(iii) Decision variables
$b_{i k}^{a}$ : battery level of vehicle $k$ at the arrival at node $i$;
$b_{i k}^{b}$ : battery level of vehicle $k$ at the departure at node $i$;
$T_{i k}^{a}$ : arrival time of vehicle $k$ at node $i$;
$T_{i k}^{d}$ : departure time of vehicle $k$ at node $i$;
$t_{i k}$ : charging time of vehicle $k$ at charging station (CS) $i$;
$x_{i j}^{k}: 1$ if vehicle $k$ travels from node $i$ to node $j ; 0$, otherwise;
$y_{i p}^{k}: 1$ if customer $j$ receives product $p$ from vehicle $k$; 0 , otherwise;
$h_{j k}: 1$ if vehicle $k$ is charged at CS $j ; 0$, otherwise;
$z_{j k}^{1}: 1$ if vehicle $k$ selects slow charging at CS $j ; 0$, otherwise;
$z_{j k}^{2}: 1$ if vehicle $k$ selects regular charging at CS $j ; 0$, otherwise;
$z_{j k}^{3}: 1$ if vehicle $k$ selects fast charging at CS $j ; 0$, otherwise.

### 3.3 Mathematical formulation

With the above-defined symbols, the MCEVRPSTW\&MCT problem can be modeled as follows:

$$
\min C=C_{\text {veh }}+C_{\text {trans }}+C_{\text {penalty }}+C_{\text {service }}
$$

where

$$
\begin{gathered}
C_{\text {veh }}=c_{1} \sum_{k \in K} \sum_{j \in N} x_{i j j}^{k} \\
C_{\text {trans }}=c_{2} \sum_{k \in K} \sum_{i \in N \cup R^{\prime} \cup O} \sum_{j \in N \cup R^{\prime} \cup O^{\prime}} d_{i j} x_{i j}^{k} \\
C_{\text {penalty }}=\sum_{k \in K} \sum_{i \in N \cup R^{\prime}}\left[c_{3} \cdot \max \left(T_{E i}-T_{i k}^{a}, 0\right)+\right. \\
\left.c_{4} \cdot \max \left(T_{i k}^{a}-T_{L i}, 0\right)\right] \\
C_{\text {service }}=\sum_{k \in K} \sum_{i \in N} \sum_{j \in R^{\prime}}\left(B-b_{j k}^{a}\right)\left(c_{e 1} \cdot z_{j k}^{1}+\right. \\
\left.c_{e 2} \cdot z_{j k}^{2}+c_{e 3} \cdot z_{j k}^{3}\right) x_{i j}^{k}
\end{gathered}
$$

s.t.

$$
\begin{gathered}
\sum_{k \in K} \sum_{i \in N \cup R^{\prime} \cup O} x_{i j}^{k}=1, \forall j \in N \\
\sum_{k \in K} \sum_{i \in N \cup O} x_{i j}^{k} \leqslant 1, \forall j \in R^{\prime} \\
\sum_{i \in N \cup R^{\prime} \cup O} x_{i j}^{k}=\sum_{i \in N \cup R^{\prime} \cup O} x_{j i}^{k}, \forall j \in N \cup R^{\prime} ; \forall k \in K \\
\sum_{i, j \in S} x_{i j}^{k} \leqslant|S|-1, \forall k \in K ; \forall S \in N ;|S| \geqslant 2 \\
\sum_{j \in N} y_{j p}^{k} \cdot q_{j p} \leqslant Q_{p}, \forall k \in K ; \forall p \in P \\
b_{O h}^{d}=B, \forall k \in K \\
b_{i k}^{d}-e \cdot d_{i j}-M\left(1-x_{i j}^{k}\right) \leqslant b_{j k}^{a}, \quad \forall i \in N \cup R^{\prime} \cup O ; \\
\forall j \in N \cup R^{\prime} \cup O^{\prime} ; \forall k \in K
\end{gathered}
$$

$$
\begin{gathered}
0 \leqslant b_{j k}^{a} \leqslant B, \forall j \in R^{\prime} \cup O^{\prime} ; \forall k \in K \\
R B \leqslant b_{j k}^{a} \leqslant B, \forall j \in N ; \forall k \in K \\
b_{i k}^{d}=b_{i k}^{a}, \forall i \in N ; \forall k \in K \\
b_{i k}^{d}=h_{i k} \cdot B, \forall i \in R^{\prime} ; \forall k \in K \\
{\left[\left(z_{j k}^{1}+z_{j k}^{2}+z_{j k}^{3}\right)-1\right] h_{j k}=0, \forall j \in R^{\prime} ; \forall k \in K} \\
t_{j k}=z_{j k}^{1} \cdot\left(B-b_{j k}^{a}\right) / \beta_{1}+z_{j k}^{2} \cdot\left(B-b_{j k}^{a}\right) / \beta_{2}+ \\
z_{j k}^{3} \cdot\left(B-b_{j k}^{a}\right) / \beta_{3}, \forall j \in R^{\prime} ; \forall k \in K \\
T_{E j}-\left\{d_{O j} / v_{0}\right\}-M\left(1-x_{O j}^{k}\right) \leqslant T_{O k}^{d} \\
\forall j \in N ; \forall k \in K \\
T_{i k}^{d}+d_{i j} / v_{0}-M\left(1-x_{i j}^{k}\right) \leqslant T_{j k}^{a}, \forall i \in N \cup R^{\prime} \cup O ; \\
\forall j \in N \cup R^{\prime} \cup O^{\prime} ; \forall k \in K \\
T_{j k}^{d}=T_{j k}^{a}+\max \left(T_{E j}-T_{j k}^{a}, 0\right)+T_{S j} \\
\forall j \in N ; \forall k \in K \\
T_{j k}^{a}+t_{j k}-M\left(1-h_{j k}\right) \leqslant T_{j k}^{d} \\
\forall j \in R^{\prime} ; \forall k \in K \\
x_{i j}^{k} \in\{0,1\}, \forall i \in N \cup R^{\prime} \cup O ; \forall j \in N \cup R^{\prime} \cup O^{\prime} ; \\
i \neq j ; k \in K \\
y_{j p}^{k} \in\{0,1\}, \forall j \in N ; \forall k \in K ; \forall p \in P \\
h_{j k} \in\{0,1\}, \forall j \in R^{\prime} ; \forall k \in K \\
z_{j k}^{1}, z_{j k}^{2}, z_{j k}^{3} \in\{0,1\}, \forall i \in R^{\prime} ; \forall k \in K
\end{gathered}
$$

Equation (1) is the objective function that minimizes the total cost, which is composed of fixed vehicle cost, distribution cost, penalty cost, and charging service cost, as defined in (2), (3), (4) and (5) respectively. Constraint (6) ensures that each customer is visited by exactly one vehicle. Constraint (7) ensures that each charging station may be visited at most once. Constraint (8) ensures the continuity of each route. Constraint (9) is a classical subtour elimination constraint. Constraint (10) states that a compartment must not be loaded more than its capacity. Constraint (11) ensures that vehicles depart from the depot with full battery. Constraint (12) represents the change of battery power after the vehicle successively visits two nodes. Constraint (13) ensures that the vehicle has enough power to reach the charging station or return to the end depot. Constraint (14) requires that the power of the vehicle when it reaches the customer node must be greater than the remaining power warning line. Con-
straint (15) states that the power of vehicle remains unchanged before and after visiting the customer node. Constraint (16) indicates that the battery is fully charged if the vehicle visits the charging station. Constraint (17) states that only one charging type can be selected if the charging station is visited. Constraint (18) represents the charging time of the vehicle at the charging station. Constraint (19) is the departure time of each vehicle from the start depot. Constraint (20) represents the arrival time of the vehicle at the next node. Constraint (21) presents the departure time of the vehicle after serving the customer node. Constraint (22) represents the departure time of the vehicle after charging at the charging station node. Finally, constraints (23) - (26) define the 0-1 decision variables.

## 4. EDA-LF for MCEVRP

In this section, the EDA-LF for solving the MCEVRPSTW\&MCT is presented in details. First, the encoding and decoding schemes, probability model and sampling process, adaptive updating mechanism, and local search based on Lévy flight are proposed. Then, the flowchart of the EDA-LF is provided.

### 4.1 Encoding and decoding schemes

Every individual of the population denotes a solution of the MCEVRP-STW\&MCT, which is represented by a sequence of all the customer numbers. The sequence decides the order of delivering products to customers. This solution representation has been widely used in the VRPs [32].

Decoding a sequence is to arrange the vehicles to serve all the customers which need multiple incompatible products and determine the charging plan for each vehicle, so as to generate a feasible schedule. In particular, for the charging plan, in addition to timely arranging the nearby charging stations for charging, it is also necessary to flexibly select the appropriate charging type according to the tightness of the next arrival node's time window. According to the constraints of MCEVRP-STW\&MCT and human experiences, we design an effective decoding scheme and the specific steps are as follows.

Step 1 Select the maximum value of the power consumption of all customers to their nearest charging station, and round up this value as the remaining power warning line $R B$.

Step 2 Insert depot node 0 at the beginning and end of the encoding sequence. Then, check the customer sequence from front to back and if compartment capacity is exceeded at a customer point, then insert two depot nodes 0 before that customer point. After that, all customers are assigned to the $H$ vehicles numbered $\{1,2,3, \cdots, H\}$,

namely $\left[0, x_{11}, x_{12}, \cdots, x_{1 K_{1}}, 0 ; 0, x_{21}, x_{22}, \cdots, x_{2 K_{1}}, 0 ; \cdots ; 0\right.$, $x_{H 1}, x_{H 2}, \cdots, x_{H K_{h}}, 0]$ where $x_{h j}$ means the number of the $j$ th customer to be served on the vehicle $h$ and $K_{h}$ is the total number of customers served by vehicle $h$. Set $h=1$.

Step 3 If $h$ is greater than $H$, go to Step 9 ; otherwise, go to Step 4.

Step 4 Set the departure time of vehicle $h$ leaved from start depot 0 by calculating the time $T_{O h}^{j}=T_{K x_{01}}-$ $\left\lfloor d_{O x_{01}} / v_{0}\right\rfloor$. Set $j=1$.

Step 5 If the remaining power calculated by constraint (12) at the $(j+1)$ th customer node is greater than $R B$ after the vehicle has served its $j$ th customer, then go to Step 6; otherwise, charge at the charging station nearest to the $j$ th customer node and set the mark flag=0, then go to Step 7.

Step 6 Set $j=j+1$ and if $j \neq K_{h}$, then go to Step 5; if $j=K_{h}$ and the current remaining power is not enough to return to end depot 0 , then charge at the charging station nearest to the $j$ th customer node and set flag=1, then go to Step 7; otherwise, go to Step 8.

Step 7 Select the charging type with the lowest total cost among the three charging types for the nearest charging station which is obtained by comparing the cost (namely the sum of the charging service cost corresponding to the charging type and the penalty cost of the time window at the next arrival node) of each charging type. If flag=0, then go to Step 6; otherwise, go to Step 8.

Step 8 Set $h=h+1$ and go to Step 3.
Step 9 End.
To better understand this decoding process, an example is given in Fig. 1 where $n$ and $m$ respectively represent the quantity of customers and charging stations whose numbers are $n+1$ to $n+m$, and I, II and III respectively represent the three charging types of slow, regular and fast charging. For the individual that the customer sequence is encoded as $\{1,2,3, \cdots, n-1, n\}$, its decoding process is shown in Fig. 1. After getting the distribution scheme by the above decoding process, the objective function in the mathematical model is used as the fitness function to evaluate the individual.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Schematic diagram of the decoding process

### 4.2 Probability model and sampling process

Different from the genetic algorithm (GA) that produces offspring through crossover and mutation operators, the EDA does it by sampling according to a probability model [33]. Thus, the probability model has a great effect on the performance of the EDA. In this paper, to well reflect the property of the considered problem, the probability model is designed as a probability matrix $\boldsymbol{P}(g)$ as follows:

$$
\boldsymbol{P}(g)=\left[\begin{array}{cccccc}
p_{11}(g) & p_{12}(g) & \cdots & p_{1 n}(g) \\
p_{21}(g) & p_{22}(g) & \cdots & p_{2 n}(g) \\
\vdots & \vdots & \ddots & \vdots \\
p_{n 1}(g) & p_{n 2}(g) & \cdots & p_{n n}(g)
\end{array}\right]
$$

The element $p_{i j}(g)$ of the probability matrix $\boldsymbol{P}(g)$ represents the probability that customer $j$ appears in position $i$ of the solution sequence at generation $g$. The value of $p_{i j}(g)$ refers to the importance of a customer when deciding the scheduling order. For all values of $i$ and $j, p_{i j}(0)$ is initialized to $p_{1 i}(0)=1 / n$, which ensures that the whole solution space can be sampled uniformly.

In each generation of the EDA, the new individuals are generated via sampling the solution space according to the probability matrix $\boldsymbol{P}(g)$. For every position $i$, customer $j$ is selected by the roulette-wheel method according to the $i$ th row of the probability matrix $\boldsymbol{P}(g)$. If customer $j$ has already appeared, it means that customer $j$ has been scheduled. Then, the whole $j$ th column of probability

matrix $\boldsymbol{P}(\mathrm{g})$ will be set as zero and all the elements of $\boldsymbol{P}(\mathrm{g})$ will be normalized to maintain that each row sums up to 1 . In such a way, an individual is constructed until all the customers appear in the sequence, and then its fitness value can be calculated.

According to this sampling strategy, in our EDA, the initial population can be generated by sampling $P_{-}$size times while the other generation population in the subsequent iteration process is composed of $(1-b \%) \times P_{-}$size sampling individuals and the best $b \% \times P_{-}$size elite individuals of the previous generation population, where $b$ represents the percentage of the population retained from the previous generation.

### 4.3 Adaptive updating mechanism

In addition to the sampling way based on the probability model, only by updating the probability model reasonably, the EDA-LF could trace the more promising search area. At each generation, the probability matrix is updated by the information of some elite solutions of the population. The elite sub-population consists of the best $S P_{-}$size solutions, where $S P_{-}$size $=\eta \% \times P_{-}$size and $\eta$ is the percentage of elite individuals in the population. To be specific, the updating process can be regarded as the following incremental learning [33]:

$$
p_{i j}(g+1)=(1-\alpha(g)) p_{i j}(g)+\frac{\alpha(g)}{S P_{-} \text {size }} \cdot \sum_{k=1}^{S P_{-} \text {size }} I_{i j}^{k}, \forall i, j
$$

where $I_{i j}^{k}$ is the indicator function of the $k$ th individual in the superior population.

$$
I_{i j}^{k}(g)= \begin{cases}1, & \text { if customer } j \text { appears in position } i \\ 0, & \text { otherwise }\end{cases}
$$

In addition, $\alpha(g)$ is the learning rate of the probability matrix $\boldsymbol{P}(\mathrm{g})$ at the $g$ th generation. To speed up convergence, the adaptive learning rate [34] is adopted as follows:

$$
\alpha(g)=\max \{\alpha(0) \cdot \exp (-0.01 g), 0.01\}
$$

where $\alpha(0)$ is the initial learning rate. In such a way, the learning rate may be relatively large at the earlier period of the search process to accelerate the speed of convergence. As the population evolves, the learning rates decrease exponentially so as to enhance the exploitation ability. To ensure certain learning efficiency, we set the learning rate no less than 0.01 for the above equations.

### 4.4 Local search strategy based on Lévy flight

The EDA pays more attention to global exploration while
its exploitation capability is relatively limited, which makes it easy to premature convergence and fall into local optimum. Thus, an effective EDA should balance the exploration and the exploitation abilities. Therefore, in this paper, a Lévy flight search is introduced into EDA to enhance its local exploitation around the best solution of the current population several times at every generation.

The Lévy flight search is an alternate way of walking with a short distance search combined with occasional longer distance walking [35], which is a random search path and it obeys a Lévy distribution [36], that is a probability distribution proposed by the French mathematician Lévy in the 1930s. Lévy flight can increase the diversity of the population and broaden the scope of the search, which makes it easier to jump out of local optimal points in the intelligent optimization algorithm such as firefly algorithms [37] and cuckoo search [38].

The Lévy flight location update formula is as follows:

$$
\boldsymbol{x}_{i}^{s+1}=\boldsymbol{x}_{i}^{s}+\phi \otimes \operatorname{Lévy}(\lambda), i=1,2, \cdots, n
$$

where $\boldsymbol{x}_{i}^{s}$ is the position of the $i$ th individual in the $n$th generation population, $\otimes$ represents point-to-point multiplication, $\phi$ is the step control amount which is set as 0.3 , and $\operatorname{Lévy}(\lambda)$ is a random search path which is essentially a random step and obeys the following Lévy distribution:

$$
\text { Lévy } \sim u=t^{-\lambda}, \quad 1<\lambda \leqslant 3
$$

Due to the complexity of Lévy distribution, it is usually simulated by the Mantegna algorithm and the step size $s$ is calculated as follows:

$$
s=\frac{\mu}{|v|^{1 / \beta}}
$$

where $\mu$ and $v$ obey the following normal distribution:

$$
\begin{gathered}
\mu \sim N\left(0, \sigma_{\mu}^{2}\right) \\
v \sim N\left(0, \sigma_{v}^{2}\right)
\end{gathered}
$$

And $\sigma_{\mu}=\left\{\frac{\Gamma(1+\beta) \sin (\pi \beta / 2)}{\Gamma[(1+\beta) / 2] 2^{\left(\beta-1 / 2\right.} \beta}\right\}, \sigma_{v}=1$, where $\beta$ is usually 1.5 .

It should be noted that the new solution $\boldsymbol{x}_{i}^{s+1}$ obtained by updating the current optimal solution through the Lévy flight search is a vector with continuous values, while the natural number encoding is used as solution representation in this paper and it is discrete. Therefore, it is necessary to construct a proper mapping from a vector with continuous values to non-repeated natural number permutation. For this, the rule based on ranked order value (ROV) in [39] is adopted to convert the continuous value of each position in the solution sequence into the discrete customer number after ranking according to the ROV rule to form a feasible solution.

In order to better understand the whole process of Lévy flight local search, an example is given in Fig. 2 below.
![img-2.jpeg](img-2.jpeg)

Fig. 2 Schematic diagram of Lévy flight local search
From Fig. 2, it can be found that the whole process of Lévy flight local search is similar to the exchange or insertion operation, or even the combination of these two neighborhood searches. That is, the change from $\boldsymbol{x}_{i}^{i}=$ $[1,2,3,4,5,6,7,8,9]$ to $\boldsymbol{x}_{i}^{(+1}=[1,2,3,5,4,9,6,7,8]$ can be understood as the exchange of customer 4 and customer 5 firstly and then inserting customer 9 before customer 6.

Moreover, in order to improve the possibility of improving the solution quality of the EDA algorithm in the local search process, it is necessary to use Lévy flight operation multiple times on the best individual of the current population at every generation. In general, the solution quality is easy to be improved at the earlier period of the search process while it becomes more and more difficult as the population evolves into the middle and later periods. Therefore, in order to save the running time of EDA and ensure the ability to jump out of the local optimum at the middle and later periods, we set the number of Lévy flight local search as in the following logistic curve:

$$
\text { Lévy_num }(t)=\left\lceil\frac{106.432}{1.0+53.587 \mathrm{e}^{-0.038 t}}\right\rceil
$$

which is related to iteration number $t$ and this curve is fitted by Matlab. After that, if the fitness value of the optimal individual obtained by multiple Lévy flight search is smaller than the best individual of the current population, then use the former to replace the latter.

### 4.5 Algorithm flowchart

With the above design, the flowchart of the EDA-LF for solving the MCEVRP-STW\&MCT is illustrated in Fig. 3.

At the initial stage of the evolution process, the whole search space is sampled uniformly. Then, the algorithm uses the EDA-based evolutionary search mechanism to sample a potential area. In addition, the local search based on Lévy flight is implemented in a promising region, aiming to obtain better solutions. With the benefit of combining EDA and Lévy flight local search, global exploration and local exploitation are balanced. In this
paper, the stopping condition is that the maximum number of generations reaches 200 .
![img-2.jpeg](img-2.jpeg)

Fig. 3 Flowchart of the EDA-LF

## 5. Computational experiments

To investigate the performance of the proposed EDA-LF approach for MCEVRP-STW\&MCT, we implement the algorithm using Microsoft Visual Studio 2013. A computer with Intel (R) Core (TM) i5-8250U CPU is adopted to run the code for all instances, and the operating system is Windows 10. We generate the MCEVRP-STW\& MCT instances and set the model parameters according to the existing literature firstly, then compare the performance of the EDA-LF, basic EDA (BEDA), and an existing algorithm, and finally compare the cost difference of the MCVRP scheme between using EVs and traditional fuel vehicles.

### 5.1 Test instances and model parameters

Since there are no internationally recognized instances for MCEVRP-STW\&MCT, we adopt the method proposed in [40] to generate the MCEVRP-STW\&MCT instances based on the VRP with time windows (VRPTW) instances of Solomon [41]. Those VRPTW instances have three set instances involving 25, 50 and 100 customers respectively. According to the customer position distribution, instances of each set are divided into clustered distribution C classes, scattered distribution R classes, and partial scattered and partial clustered distribution RC classes. In addition, considering the limited space, we

only consider the narrower time window " 1 " classes rather than the wider time window " 2 " classes. In consequence, Solomon's instances used in this paper are subdivided into three classes, C1, R1 and RC1. Then, those VRPTW instances are adapted into MCEVRP-STW\& MCT instances according to the method proposed by Reed [40], in which the data is obtained by dividing the vehicle capacity into two compartments in a ratio $3: 1$, and the customer demands are also divided by using a 3:1 ratio except the demands of the sub-region $\left(x_{\min } \leqslant x<x_{\min }+\frac{x_{\max }-x_{\min }}{2}\right.$, $\left.y_{\min } \leqslant y<y_{\min }+\frac{y_{\max }-y_{\min }}{2}\right)$ which are divided using a $2: 1$ ratio. In the representation of the sub-region, $x$ and $y$ are the horizontal and vertical coordinates of the customer position, $x_{\max }$ and $y_{\max }$ denote the maxima of the horizontal and vertical coordinates, $x_{\min }$ and $y_{\min }$ denote the minima of the horizontal and vertical coordinates.

In addition to setting the customers information as above, the location of the charging station should also be given. It is assumed that three set instances involving 25, 50 and 100 customers correspond to 5, 10 and 20 charging stations respectively, and these charging stations are uniformly distributed in a $100 \times 100$ area. Finally, some fixed parameters of the MCEVRP-STW\&MCT model are set in Table 1 in which most of the them are set by existing literature while a few are set in the paper.

Table 1 Model parameter setting

| Parameter | Description | Value | Reference |
| :--: | :--: | :--: | :--: |
| $\beta_{1}$ | Slow charging rate | $0.625 \mathrm{~kW} \cdot \mathrm{~h} / \mathrm{min}$ |  |
| $\beta_{2}$ | Regular charging rate | $1.25 \mathrm{~kW} \cdot \mathrm{~h} / \mathrm{min}$ | [24] |
| $\beta_{3}$ | Fast charging rate | $5 \mathrm{~kW} \cdot \mathrm{~h} / \mathrm{min}$ |  |
| $e$ | Per-unit distance power consumption | $1 \mathrm{~kW} \cdot \mathrm{~h} / \mathrm{km}$ |  |
| $c_{2}$ | Per-unit distance distribution cost | 0.6 yuan $/ \mathrm{km}$ |  |
| $v_{0}$ | Vehicle speed | $50 \mathrm{~km} / \mathrm{h}$ | [43] |
| $c_{3}$ | Per-unit early arrival penalty cost | 20 yuan/h |  |
| $c_{4}$ | Per-unit delay arrival penalty cost | 30 yuan/h | [44] |
| $c_{e 1}$ | Per-unit service cost for slow charging | 0.1 yuan $/ \mathrm{kW} \cdot \mathrm{h}$ | NDRC |
| $c_{e 2}$ | Per-unit service cost for regular charging | 0.2 yuan $/ \mathrm{kW} \cdot \mathrm{h}$ | Document <br> No. 1688 of 2014 |
| $c_{e 3}$ | Per-unit service cost for fast charging | 0.3 yuan $/ \mathrm{kW} \cdot \mathrm{h}$ |  |
| $c_{1}$ | Per-unit fixed vehicle cost | 1000 yuan |  |
| $B$ | Battery capacity of the vehicles | $150 \mathrm{~kW} \cdot \mathrm{~h}$ | This paper |
| $Q_{1} / Q_{2}$ | The ratio of compartment capacity | $1800 \mathrm{~kg} / 600 \mathrm{~kg}$ |  |

### 5.2 Parameters setting of EDA-LF algorithms

The proposed EDA-LF algorithm has four key parameters to be set: $P_{-}$size (population size), $\eta$ (percentage of elite solutions), the initial learning rate $\alpha(0)$, and $b$ (percentage of remaining elite individuals of the previous generation). To investigate the influence of these parameters on the performance of the EDA-LF, and explore whether different customer sizes or customer distribution types lead to differences in parameters setting, the Taguchi method of design-of-experiment (DOE) is implemented by using the first instances of each class with different customer sizes in Solomon's instances. Due to the limited space, only the specific DOE process of C101 instance with 25 customers is shown here. Combinations of different values of these parameters are listed in Table 2.

Table 2 Combinations of parameter values

| Parameter | Factor level |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  | 1 | 2 | 3 | 4 |
| $P_{-}$size | 50 | 100 | 150 | 200 |
| $\eta$ | 10 | 20 | 30 | 40 |
| $\alpha(0)$ | 0.1 | 0.3 | 0.5 | 0.7 |
| $b$ | 10 | 20 | 30 | 40 |

According to the number of parameters and the number of factor levels, we choose the orthogonal array $L_{10}\left(4^{4}\right)$. For each parameter combination, the EDA-LF is run 10 times independently and the average fitness value obtained by the EDA-LF is calculated as the response variable (RV) value. The orthogonal array and the obtained RV values are listed in Table 3.

Table 3 Orthogonal array and RV values

| Experiment <br> number | Factor |  |  |  | RV |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | $P_{-}$size | $\eta$ | $\alpha(0)$ | $b$ |  |
| 1 | 1 | 1 | 1 | 1 | 3888.195 |
| 2 | 1 | 2 | 2 | 2 | 3870.645 |
| 3 | 1 | 3 | 3 | 3 | 3898.374 |
| 4 | 1 | 4 | 4 | 4 | 3888.832 |
| 5 | 2 | 1 | 2 | 3 | 3886.850 |
| 6 | 2 | 2 | 1 | 4 | 3861.283 |
| 7 | 2 | 3 | 4 | 1 | 3884.690 |
| 8 | 2 | 4 | 3 | 2 | 3846.059 |
| 9 | 3 | 1 | 3 | 4 | 3900.421 |
| 10 | 3 | 2 | 4 | 3 | 3822.744 |
| 11 | 3 | 3 | 1 | 2 | 3869.779 |
| 12 | 3 | 4 | 2 | 1 | 3794.425 |
| 13 | 4 | 1 | 4 | 2 | 3895.055 |
| 14 | 4 | 2 | 3 | 1 | 3815.151 |
| 15 | 4 | 3 | 2 | 4 | 3760.516 |
| 16 | 4 | 4 | 1 | 3 | 3903.280 |

According to the orthogonal table, we figure out the average $\mathrm{RV}(\mathrm{ARV})$ values of each parameter to analyze its significance rank which is listed in Table 4. Then, the influence trend of each parameter is illustrated in Fig. 4.

Table 4 ARV and rank of each parameter

| Level | $P_{-}$size | $\eta$ | $\alpha(0)$ | $b$ |
| :--: | :--: | :--: | :--: | :--: |
| 1 | 3886.512 | 3892.630 | 3880.634 | $\mathbf{3 8 4 5 . 6 1 5}$ |
| 2 | 3869.721 | $\mathbf{3 8 4 2 . 4 5 6}$ | $\mathbf{3 8 2 8 . 1 0 9}$ | 3870.385 |
| 3 | $\mathbf{3 8 4 6 . 8 4 2}$ | 3853.340 | 3865.001 | 3877.812 |
| 4 | 3843.501 | 3858.149 | 3872.830 | 3852.763 |
| Delta | 43.011 | 50.174 | 52.525 | 32.197 |
| Rank | 3 | 2 | 1 | 4 |

![img-3.jpeg](img-3.jpeg)
![img-4.jpeg](img-4.jpeg)

Fig. 4 Influence trend of each parameter
From Table 4, it can be seen that the initial learning rate $\alpha(0)$ is the most significant one among the four parameters. This means that the initial learning rate is crucial to the performance of the EDA-LF. A small value of $\alpha(0)$ could lead to slow convergence while a large value could lead to premature convergence. Therefore, to ensure the effectiveness of the EDA-LF, an appropriate value of $\alpha(0)$ is very essential. In addition, $\eta$ ranks the second. A proper value is helpful to update the probability model efficiently. Besides, the significant rank of the population size is the third. A large value of $P_{-}$size makes the algorithm sample the solution space sufficiently but it will cause a large amount of computational budget. It can be seen from Fig. 4 that it makes no significant improvement when the size is too large. In this case, to reduce the computational budget, we set $P_{-}$size $=150$. Finally, although parameter $b$ has the slightest influence, adding some elite individuals of the previous generation to the current population will help the algorithm converge and further optimize. According to the above analysis, a good choice of parameter combination is suggested as $P_{-}$size $=150, \eta=$ $20, \alpha(0)=0.3, b=10$.

In order to explore whether different customer sizes or customer distribution types have an impact on the parameters setting, the DOE method is further used to other eight instances numbered 101. Finally, these nine DOE results are summarized in Table 5.

Table 5 Summary of nine DOE results

| Instance | $P_{-}$size | $\eta$ | $\alpha(0)$ | $b$ |
| :--: | :--: | :--: | :--: | :--: |
| 25C101 | 150 | 0.2 | 0.3 | 0.1 |
| 25R101 | 150 | 0.3 | 0.3 | 0.1 |
| 25RC101 | 150 | 0.2 | 0.3 | 0.2 |
| 50C101 | 200 | 0.2 | 0.5 | 0.1 |
| 50R101 | 150 | 0.2 | 0.5 | 0.1 |
| 50RC101 | 200 | 0.2 | 0.5 | 0.1 |
| 100C101 | 150 | 0.3 | 0.7 | 0.1 |
| 100R101 | 150 | 0.2 | 0.7 | 0.2 |
| 100RC101 | 200 | 0.3 | 0.7 | 0.1 |

From Table 5, it can be found that the initial learning rate $\alpha(0)$ gradually increases with the problem scale, while other obvious rules or conclusions have not been found yet. This is because that the solution space increases greatly with the problem scale, the initial learning rate $\alpha(0)$ also needs to be increased to make the algorithm converge quickly at the earlier period to get closer to the optimal solution which can achieve a better optimization effect. The results of the above algorithm parameter setting will be further applied to the following experiments.

### 5.3 Comparison of EDA-LF and BEDA

In order to verify the effectiveness of adding the Lévy flight local search strategy to the EDA algorithm, we still use the nine instances (i.e., the first instances of each class with different customer sizes in Solomon's instances) to compare the performance of EDA-LF and BEDA without Lévy flight local search. The two algorithms use the same parameter setting for each instance and the maximum number of iterations is 200 . After that, we can find that for the small, medium, large-scale instances (i.e., corresponding to 25,50 and 100 customers, respectively), the computational times are $46 \mathrm{~s}, 77 \mathrm{~s}$ and 198 s respectively, which are within an acceptable time range. Also, for each instance, we can get the best value, the mean value and the standard deviation that are achieved by running two algorithms 10 times independently, and the results are shown in Fig. 5, Fig. 6 and Fig. 7 respectively.
![img-5.jpeg](img-5.jpeg)

Fig. 5 Comparison between BEDA and EDA-LF for the best value
From Fig. 5 and Fig.6, we can see that the curves of EDA-LF are all below BEDA which indicates that the optimal value and average value found by the EDA-LF algorithm are better than those by BEDA. Therefore, the EDA-LF algorithm can find a better solution and the Lévy flight strategy is effective for solving the MCEVRPSTW\&MCT. In addition, it can be seen from Fig. 7 that
the standard deviations of the EDA-LF are all smaller than those of the BEDA. Accordingly, we conclude that the EDA-LF is more robust than the BEDA.
![img-6.jpeg](img-6.jpeg)

Fig. 6 Comparison between BEDA and EDA-LF for the mean value
![img-7.jpeg](img-7.jpeg)

Fig. 7 Comparison between BEDA and EDA-LF for the standard deviation

### 5.4 Comparison with an existing algorithm

Next, the EDA-LF is compared with the GA [45] which is proposed to solve the MCVRP with flexible compartment sizes by Koch et al. Moreover, to compare the performance of these two algorithms fairly, we all set the stopping criterion of 100 s , which is an acceptable short time. The parameters of the GA are set as follows: the crossover probability $P_{\text {co }}=0.9$, the probability in the swap mutation operator $P_{\text {swap }}=0.05$ and the probability in the inversion mutation operator $P_{\text {inv }}=0.05$. The parameters of the EDA-LF are set as in Table 5. For each of these 27 instances, the EDA-LF and the GA are used to solve the MCEVRP-STW\&MCT and run 10 times independently, then the mean values are listed and the difference values $\Delta_{\mathrm{E}-\mathrm{G}}$ are calculated in Table 6.

Table 6 Comparison between the EDA-LF and the GA

| Instance | EDA-LF | GA | $\Delta_{\text {E-G }}$ |
| :--: | :--: | :--: | :--: |
| 25C101 | 3641.12 | 3526.66 | 114.46 |
| 25C102 | 3452.69 | 3366.02 | 86.67 |
| 25C103 | 3310.58 | 3242.19 | 68.39 |
| 25R101 | 3838.06 | 3857.14 | $-19.08$ |
| 25R102 | 3597.19 | 3485.98 | 111.21 |
| 25R103 | 3385.55 | 3220.15 | 165.4 |
| 25RC101 | 3952.84 | 3854.62 | 98.22 |
| 25RC102 | 3785.50 | 3639.48 | 146.02 |
| 25RC103 | 3707.64 | 3614.13 | 93.51 |
| 50C101 | 6953.58 | 7137.88 | $-184.30$ |
| 50C102 | 6164.64 | 6311.49 | $-146.85$ |
| 50C103 | 5967.82 | 5871.14 | 96.68 |
| 50R101 | 8781.23 | 9123.15 | $-341.92$ |
| 50R102 | 7924.20 | 8243.74 | $-319.54$ |
| 50R103 | 7426.37 | 7593.56 | $-167.19$ |
| 50RC101 | 8825.67 | 8981.91 | $-156.24$ |
| 50RC102 | 8502.28 | 8637.63 | $-135.35$ |
| 50RC103 | 8066.88 | 8269.33 | $-202.45$ |
| 100C101 | 19334.72 | 19794.61 | $-459.89$ |
| 100C102 | 17026.35 | 17748.72 | $-722.37$ |
| 100C103 | 15329.84 | 15822.68 | $-492.84$ |
| 100R101 | 18446.71 | 18940.55 | $-493.84$ |
| 100R102 | 17223.95 | 17670.46 | $-446.51$ |
| 100R103 | 16176.47 | 16639.92 | $-463.45$ |
| 100RC101 | 20320.62 | 21047.13 | $-726.51$ |
| 100RC102 | 19771.89 | 20241.48 | $-469.59$ |
| 100RC103 | 18596.53 | 19310.20 | $-713.67$ |

From Table 6, it can be seen that the EDA-LF outperforms the GA in 18 instances, whose difference value is negative and bold. And we can also find that the EDA-LF is better than the GA for the medium and large-scale instances except for instance 50C103, while worse than the GA for the small-scale instances except for the instance 25R101. Therefore, in general, compared with the GA, the EDA-LF can often get better solutions in a relatively short time when solving medium and large-scale instances.

### 5.5 Comparison in MCVRP between using EVs and traditional fuel vehicles

The existing researches on MCVRP usually use the traditional fuel vehicles to transport incompatible products. In order to discuss the difference of MCVRP between using EVs and traditional fuel vehicles, we use the proposed EDA-LF algorithm to solve the multi-compartment fuel
vehicle routing problem (MCFVRP), in which the compartment capacity of a traditional fuel vehicle is the same as that of an EV in MCEVRP. Considering that there are many fuel stations and the refueling time is short, we ignore the refueling time in MCFVRP and set the per-unit distance distribution cost of the traditional fuel vehicle to 1.5 yuan according to [46]. For simplicity, only these 27 instances (i.e., the first three instances of each class with different customer sizes in Solomon's instances) are used and the mean value is achieved by running the EDA-LF algorithm 10 times independently. Finally, the relative percentage deviation (RPD, RPD $=(E-F) / F \cdot 100 \%$ ) between the mean value of MCEVRP and the MCFVRP is calculated, and the results are shown in Table 7.

Table 7 Comparison of EDA-LF solutions for MCEVRP and MCFVRP

| Instance | MCEVRP | MCFVRP | RPD/\% |
| :--: | :--: | :--: | :--: |
| 25C101 | 3712.534 | 4079.279 | $-8.99$ |
| 25C102 | 3483.933 | 3786.238 | $-7.98$ |
| 25C103 | 3368.160 | 3627.447 | $-7.15$ |
| 25R101 | 3934.316 | 4147.696 | $-5.14$ |
| 25R102 | 3645.238 | 3784.554 | $-3.68$ |
| 25R103 | 3506.247 | 3578.674 | $-2.02$ |
| 25RC101 | 4075.413 | 4415.153 | $-7.69$ |
| 25RC102 | 3879.339 | 4309.977 | $-9.99$ |
| 25RC103 | 3801.743 | 3994.450 | $-4.82$ |
| 50C101 | 6982.788 | 7931.015 | $-11.9$ |
| 50C102 | 6285.829 | 7225.835 | $-13.0$ |
| 50C103 | 6049.459 | 6838.175 | $-11.5$ |
| 50R101 | 8887.140 | 9030.583 | $-1.59$ |
| 50R102 | 8085.606 | 8273.162 | $-2.27$ |
| 50R103 | 7612.346 | 7786.252 | $-2.23$ |
| 50RC101 | 9101.333 | 9658.091 | $-5.76$ |
| 50RC102 | 8695.609 | 9190.063 | $-5.38$ |
| 50RC103 | 8271.000 | 8873.101 | $-6.79$ |
| 100C101 | 18728.26 | 20856.47 | $-10.2$ |
| 100C102 | 16343.28 | 18395.62 | $-11.1$ |
| 100C103 | 14874.99 | 16986.01 | $-12.4$ |
| 100R101 | 17862.33 | 18808.19 | $-5.03$ |
| 100R102 | 16879.04 | 17473.99 | $-3.40$ |
| 100R103 | 15676.09 | 16119.14 | $-2.75$ |
| 100RC101 | 19755.47 | 21048.47 | $-6.14$ |
| 100RC102 | 19195.64 | 19948.48 | $-3.77$ |
| 100RC103 | 17755.99 | 18616.22 | $-4.62$ |
| Average | - | - | $-6.57$ |

From the 27 rows of data in Table 7, it can be seen that the cost of MCEVRP using EVs is all less than that of MCFVRP using traditional fuel vehicles and the distribution cost of using EVs can be reduced by $6.57 \%$ on average. This shows that although the distribution mode of using EV will increase the charging service cost and its longer charging time may lead to higher penalty cost of the time window under the flexible choice of various charging types, it has a lower energy consumption compared with the distribution mode of using the traditional fuel vehicle which greatly reduces the distribution cost. Moreover, with the increase of punishment on exhaust emissions of fuel vehicles and considerable subsidy policy for distribution of EVs, the cost of MCEVRP will be further lower than that of MCFVRP. More importantly, the use of EVs has less pollution to the environment and helps to reduce greenhouse gas emissions.

Therefore, using multi-compartment EVs to transport incompatible products can not only reduce costs, but also protect the environment which makes it more attractive to logistics companies and more popular with the public than using traditional multi-compartment fuel vehicles. In addition, the multi-compartment EV distribution scheme developed in this paper will be helpful to guide the green logistics distribution of incompatible products.

## 6. Conclusions

In this paper, the MCEVRP-STW\&MCT is proposed, which is a combination of the MCVRP and the EVRP. After constructing the mathematical model of the problem, an EDA-LF is proposed, in which a specific decoding scheme is devised whilst a Lévy flight local search is employed to help the EDA algorithm jump out of the local optimum. Experiments for comparing the EDA-LF and the BEDA have been conducted, in which the DOE method is used to set the algorithm parameters. The results show that the EDA-LF algorithm can not only find a better solution, but also has a stronger robustness compared with the BEDA. In addition, when comparing with existing algorithms, the result shows that the EDA-LF can often get better solutions in a relatively short time when solving medium and large-scale instances. Furthermore, we use the proposed EDA-LF algorithm to solve the MCFVRP, and discuss the cost difference of MCVRP between using EVs and traditional fuel vehicles. In addition to protecting the environment, the result shows that the cost of using electric multi-compartment vehicles to distribute incompatible products is lower than that of using traditional multi-compartment fuel vehicles.

With the requirements of green logistics and the increase of distribution demand of incompatible products, the multi-compartment EV distribution scheme proposed
in this paper will be helpful to provide guidance for the distribution of incompatible products. Moreover, it is also helpful to promote the establishment of a low-carbon and low-pollution distribution system.

## References

[1] PANG Y, LUO H, XING L N, et al. A survey of vehicle routing optimization problems and solution methods. Control Theory \& Applications, 2019, 36(10): 1573-1584. (in Chinese)
[2] CHEN L, LIU Y, LANGEVIN A. A multi-compartment vehicle routing problem in cold-chain distribution. Computers \& Operations Research, 2019, 111: 58-66.
[3] MOFID-NAKHAEE E, BARZINPOUR F. A multi-compartment capacitated arc routing problem with intermediate facilities for solid waste collection using hybrid adaptive large neighborhood search and whale algorithm. Waste Management \& Research, 2019, 37(1): 38-47.
[4] ZHANG Y K, SUN L J, HU X P. Multi-compartment vehicle dispatching and routing for product oil distribution. Operations Research and Management Science, 2017, 26(7): 1-9.
[5] ABDULKADER M M S, GAJPAL Y, ELMEKKAWY T Y. Hybridized ant colony algorithm for the multi-compartment vehicle routing problem. Applied Soft Computing, 2015, 37: 196-203.
[6] BROWN G G, GRAVES G W. Real-time dispatch of petroleum tank trucks. Management Science, 1981, 27(1): 19-32.
[7] OSTERMEIER M, HUEBNER A. Vehicle selection for a multi-compartment vehicle routing problem. European Journal of Operational Research, 2018, 269(2): 682-694.
[8] GOCMEN E, EROL R. Location and multi-compartment capacitated vehicle routing problem for blood banking system. International Journal of Engineering Technologies, 2018, $4(1): 1-12$.
[9] KANDILLER L, ELIIYI D T, TASAR B. A multi-compartment vehicle routing problem for livestock feed distribution. Proc. of the Operations Research Conference, 2017: 149155.
[10] PAREDES-BELMAR G, MARIANOV V, BRONFMAN A, et al. A milk collection problem with blending. Transportation Research Part E-Logistics and Transportation Review, 2016, 94: 26-43.
[11] KESKIN M, LAPORTE G, CATAY B. Electric vehicle routing problem with time-dependent waiting times at recharging stations. Computers \& Operations Research, 2019, 107: 7794.
[12] SHI Y, BOUDOUH T, GRUNDER O. A hybrid genetic algorithm for a home health care routing problem with time window and fuzzy demand. Expert Systems with Applications, 2017, 72: 160-176.
[13] KESKIN M, CATAY B. A matheuristic method for the electric vehicle routing problem with time windows and fast chargers. Computers \& Operations Research, 2018, 100: $172-188$.
[14] PEREZ-RODRIGUEZ R, HERNANDEZ-AGUIRRE A. Bivariate dependency for the vehicle routing problem with time windows. International Journal of Industrial EngineeringTheory Applications and Practice, 2020, 27(3): 473-499.
[15] PEREZ-RODRIGUEZ R, HERNANDEZ-AGUIRRE A. A hybrid estimation of distribution algorithm for the vehicle

routing problem with time windows. Computers \& Industrial Engineering, 2019, 130: 75-96.
[16] HENKE T, SPERANZA M G, WAESCHER G. A branch-and-cut algorithm for the multi-compartment vehicle routing problem with flexible compartment sizes. Annals of Operations Research, 2019, 275(2): 321-338.
[17] CHEN J M, SHI J. A multi-compartment vehicle routing problem with time windows for urban distribution-a comparison study on particle swarm optimization algorithms. Computers \& Industrial Engineering, 2019, 133: 95-106.
[18] ZHAN H X, WANG X P, SUN Z L, et al. Variable neighborhood search for the multi-objective multi-compartment optimization of refined products distribution. Systems Engineering-Theory \& Practice, 2019, 39(10): 2660-2675. (in Chinese)
[19] WANG X, JI Q K, HU X P. A hybrid guided reactive tabu search for heterogeneous fixed fleet multi-compartment vehicle routing problem. Engineering Management, 2016, 30(3): 179-187. (in Chinese)
[20] GOODSON J C. A priori policy evaluation and cyclic-orderbased simulated annealing for the multi-compartment vehicle routing problem with stochastic demands. European Journal of Operational Research, 2015, 241(2): 361-369.
[21] LU S C, WANG X F. Discrete firefly algorithm for clustered multi-temperature joint distribution with fuzzy travel times. International Journal of Computational Intelligence Systems, 2018, 11(1): 195-205.
[22] BARCO J, GUERRA A, MUNOZ L, et al. Optimal routing and scheduling of charge for electric vehicles: a case study. Mathematical Problems in Engineering, 2017, 2017(Pt.11): $1-16$.
[23] VERMA A. Electric vehicle routing problem with time windows, recharging stations and battery swapping stations. Euro Journal on Transportation and Logistics, 2018, 7(4): 415451 .
[24] SHAO S, GUAN W, RAN B, et al. Electric vehicle routing problem with charging time and variable travel time. Mathematical Problems in Engineering, 2017, 2017(2): 1-13.
[25] CATAY B, KESKIN M. The impact of quick charging stations on the route planning of electric vehicles. Proc. of the IEEE Symposium on Computers and Communications, 2017: $152-157$.
[26] LIN J, ZHOU W, WOLFSON O. Electric vehicle routing problem. Transportation Research Procedia, 2016, 12: $508-521$.
[27] KANCHARLA S R, RAMADURAI G. An adaptive large neighborhood search approach for electric vehicle routing with load-dependent energy consumption. Transportation in Developing Economies, 2018. DOI: 10.1007/s40890-0180063-3.
[28] ZHAO M T, LU Y W. A heuristic approach for a real-world EV routing problem. Algorithms, 2019. DOI: 10.3390/a12020 045 .
[29] MONTOYA A, GUERET C, MENDOZA J E, et al. The electric vehicle routing problem with nonlinear charging function. Transportation Research Part B-Methodological, 2017, 103: 87-110.
[30] KESKIN M, CATAY B. Partial recharge strategies for the EV routing problem with time windows. Transportation Research Part C-Emerging Technologies, 2016, 65: 111-127.
[31] DESAULNIERS G, ERRICO F, IRNICH S, et al. Exact al-
gorithms for electric vehicle-routing problems with time windows. Operations Research, 2016, 64(6): 1388-1405.
[32] LIU R, TAO Y Y, XIE X L. An adaptive large neighborhood search heuristic for the vehicle routing problem with time windows and synchronized visits. Computers \& Operations Research, 2019, 101: 250-262.
[33] WU C G, WANG L, ZHENG X L. An effective estimation of distribution algorithm for solving uniform parallel machine scheduling problem with precedence constraints. Proc. of the IEEE Congress on Evolutionary Computation, 2016: 26262632.
[34] SHEN J N, WANG L, WANG S Y. A bi-population EDA for solving the no-idle permutation flow-shop scheduling problem with the total tardiness criterion. Knowledge-Based Systems, 2015, 74: 167-175.
[35] VISWANATHAN G M, AFANASYEV V, BULDYREV S V, et al. Levy flight search patterns of wandering albatrosses. Nature, 1996, 381(6581): 413-415.
[36] TSALLIS C, LEVY S V F, SOUZA A M C, et al. Statisticalmechanical foundation of the ubiquity of Levy distributions in nature. Physical Review Letters, 1995, 75(20): 3589-3593.
[37] SUMPUNSRI S, PUANGDOWNREONG D. Multiobjective Levy-flight firerly algorithm for optimal PIDA controller design. International Journal of Innovative Computing Information and Control, 2020, 16(1): 173-187.
[38] SHI W G, GUO M. Network delay prediction based on model of modified ensemble empirical mode decomposition-permutation entropy and cuckoo search-wavelet neural network. Systems Engineering and Electronics, 2020, 42(1): 184-190. (in Chinese)
[39] OUAARAB A, AHIOD B, YANG X S, et al. Discrete cuckoo search algorithm for job shop scheduling problem. Proc. of the IEEE International Symposium on Intelligent Control, 2014: 1872-1876.
[40] REED M, YIANNAKOU A, EVERING R. An ant colony algorithm for the multi-compartment vehicle routing problem. Applied Soft Computing, 2014, 15: 169-176.
[41] SOLOMON M M. Algorithms for the vehicle routing and scheduling problems with time window constraints. Operations Research, 1987, 35(2): 254-265.
[42] WANG Q Y, LI Y, LI H. Battery swap station location-routing problem of electric vehicles with soft time windows. Industrial Engineering and Management, 2019, 24(3): 99-106.
[43] MAVROVOUNIOTIS M, ELLINAS G, POLYCARPOU M. Ant colony optimization for the electric vehicle routing problem. Proc. of the 8th IEEE Symposium Series on Computational Intelligence, 2018: 1234-1241.
[44] GUO Z F, LI Y, JIANG X D, et al. The electric vehicle routing problem with time windows using genetic algorithm. Proc. of the 2nd IEEE Advanced Information Technology, Electronic and Automation Control Conference, 2017: 635639 .
[45] KOCH H, HENKE T, WASCHER G. A genetic algorithm for the multi-compartment vehicle routing problem with flexible compartment sizes. https://www.fww.ovgu.deffww_media/femm/femm_2016/2016_04.pdf.
[46] FENG W, FIGLIOZZI M A. Conventional vs electric commercial vehicle fleets: a case study of economic and technological factors affecting the competitiveness of electric commercial vehicles in the USA. Proc. of the 7th International Conference on City Logistics, 2012: 702-711.

## Biographies

![img-8.jpeg](img-8.jpeg)

SHEN Yindong was born in 1965. She received her Ph.D. degree from the School of Computing, University of Leeds, UK in 2001. She is a professor in the School of Artificial Intelligence and Automation, Huazhong University of Science and Technology. Her research interests include operation and optimization, vehicle routing optimization, public transport vehicle scheduling, and
crew scheduling.
E-mail: yindong@hust.edu.cn
![img-9.jpeg](img-9.jpeg)

PENG Liwen was born in 1994. He is currently working toward his M.S. degree in Huazhong University of Science and Technology, China. His research interests are intelligent computing, multicompartment vehicle routing optimization and electric vehicle routing optimization.
E-mail: 2537531989@qq.com
![img-10.jpeg](img-10.jpeg)

LI Jingpeng was born in 1969. He received his Ph.D. degree from University of Leeds, UK in 2002. He is a reader at the Division of Computer Science and Mathematics, University of Stirling, UK. His research focuses on computational search methodologies and models emerging from the complexity and uncertainty of real-world optimization problems and decision support systems.
E-mail: jli@cs.stir.ac.uk