# An Augmented Estimation of Distribution Algorithm For Multi-Carpooling Problem With Time Window 

Fang Zhang<br>School of Computer and Communication Engineering, Liaoning Shihua University<br>Fushun 113001, Liaoning, China<br>zhangfang@lnpu.edu.cn

Z.J. Yang, Y. Wang ${ }^{\dagger}$, Member, IEEE<br>Lab. of Networked Control Systems,<br>Shenyang Institute of Automation,<br>Chinese Academy of Sciences<br>Shenyang 110016, Liaoning, China<br>\{yang, wangyang\}@sia.ac.cn

Fangjun Kuang<br>University of Stuttgart<br>Pfaffenwaldring 47, 70569 Stuttgart, Germany<br>kuangfn@studi.informatik.uni-stuttgart.de


#### Abstract

A multi-carpooling model is proposed for the multi-vehicle carpooling problem in distributed parallel computing environment. A two-stage stochastic optimization of the estimation of distribution algorithm solves the optimum of the multi-carpooling problem with a carpooling probabilistic matrix. A ridable matrix initiates the carpooling probabilistic matrix, and the carpooling probabilistic matrix continues updating during the optimization. The carpooling model mines efficient and compromised ridesharing routes for shared riders by the optimization iterations. Experimental results indicate that the carpooling model has the characteristics of effective and efficient traffic including shorter waiting time, more passenger load, and less average riding distance.


Keywords-carpooling problem; pickup and delivery problem; estimation of distribution algorithm; stochastic optimization.

## I. INTRODUCTION

The multi-carpooling problem is a NP sub-problem of Pickup and Delivery Problem which goal is to minimize the riding distances and thus alleviate urban traffic jams and the transportation pressure ${ }^{[1,2]}$. Meanwhile it subjects to the constraints of multi-variables including: location points of dynamic ridesharing, time windows for pickup and dropping, riding routes, passenger capacities, travel speed and etc. The implementation of the carpooling problem is to seek compromised multi-routes that are preferred by all qualified riders; however, stochastic disturbances of travel time make it hard to actionable merging the routes for all riders. Yan proposed a stochastic carpooling model formulated as an integer multiple commodity network flow problem; however, the model could be difficult to find optimal solutions especially with large problem sizes ${ }^{[3]}$. A more conventional approach is to use vehicle routing problem with hard time window to eliminate the uncertainty ${ }^{[4,5]}$. In addition, the multi-carpooling model is implemented in the multi-vehicle environment with distributed parallel computing ${ }^{[6-9]}$. The distributed computing for multi-carpooling is of high time and space complexity, hence, the temporal-spatial complexity results in the solving difficulties within a reasonable period of time. In order to reduce the complexity, $\operatorname{Pan}^{[4]}$ proposed a time difference insertion heuristics algorithm, $\operatorname{Shao}^{[9]}$ proposed a clustering heuristic algorithm based on matching degree, and $\operatorname{Xiao}^{[10]}$

This work was supported by the Natural Science Foundation of China under contact (61233007), the National High Technology Research and Development Program of China (863 Program: 2011AA040101, 2012AA041102-03, 2011AA040103), Foundation of Chinese Academy of Sciences under contract (XDA06020500, XDA06021100, XDA06020602).
Corresponding author: yang.wang.cn@ieee.org
used the fuzzy clustering and fuzzy recognition theory to study the carpooling problem. Though their heuristic algorithms are efficient, yet these models were simplified by a certain level of abstraction, the risk remains that the model would not represent reality sufficiently. As for the model-free method, service models ${ }^{[6-8]}$ are proposed as a data-driven approach considering GPS data sets, context information, and measurement based on the MapReduce model. Besides, genetic algorithm ${ }^{[5,11]}$ and ant colony algorithm ${ }^{[12]}$ are also be used to solve the carpooling problems in cloud computing.

For more efficient computing and effective solutions, an estimation of distribution algorithm (sometimes called probabilistic model-building genetic algorithm) is proposed as a stochastic optimization method to solve the optimum with a carpooling probabilistic matrix of promising carpooling solutions. The optimization consists of a series of incremental updates of the carpooling probabilistic matrix. If the carpooling probabilistic matrix is not the identity matrix $\mathbf{I}$, the multicarpooling problem is augmented with an intermediate stage for ridesharing among drivers. In addition, a notion of the virtual vehicle is introduced as a generalized profile of vehicles permitting arbitrary starting and ending points for drivers.

## II. PROBLEM FORMULIZATION

## A. Definition of carpooling model

Definition 1 The topology of urban transportation networks is denoted by the graph $g(\mathcal{V}, \mathcal{E}, \mathcal{W})$. Assuming that there are $m$ drivers and $n$ passengers, $m$ drivers only accept self-driving travel and ridesharing travel, and $n$ passengers only accept ridesharing travel and bus travel. Each vehicle keeps moving at a constant speed. The service-based multi-carpooling model automatically identifies the $m$ vehicles which are recommended for carpooling services, which provide ridesharing for qualified riders $(\leq m+n)$ in multiple pickup and dropping points.
Definition 2 The service time window specifies the waiting time interval $\left\{e_{t}, l_{t}\right\}$ for the pickup and dropping point $x$. All vehicles have to pick up and drop down riders in the specified time window. When a vehicle reaches a certain point $x$ at the time $t_{d+1}^{x}$, the waiting time is denoted by $t_{d+1}^{x}=\max \left\{e_{s}-t_{d+1}^{x}, 0\right\}$.

Definition 3 The virtual vehicle $\mathcal{S}=\left\{s_{j} \mid j \in[1, m]\right\}$ gives a generalized profile for the distributed vehicles which could be not recommended for carpooling services: If a virtual vehicle $s$ is recommended, then $\mathcal{I}_{s u}^{s}=T_{s d}^{s}=1$, If a virtual vehicle $s$ is not recommended, then $\mathcal{I}_{s d}^{s}=\mathcal{I}_{s d}^{s}=0$; , where $s_{j}$ denotes the index of vehicles, and the subscript $j$ denotes the dynamic driver who could be not the car owner. The initial value and the final value of $\mathcal{S}$ are both $\left\{s_{j} \mid j=1\right.$, $2, \ldots, m\}$.

TABLE I. NOTATION NOMENCLATURE

## B. Objectives of carpooling model

Objective 1 Minimum the number of vehicles for all the drivers' travel: $\quad \min \sum_{i \in \mathcal{S}} \bigcup_{d \in \mathcal{D}} \mathcal{I}_{d}^{s}, d \in \mathcal{D}, s \in \mathcal{S}$
, where $\sum$ denotes the cumulative operator for all recommended vehicles, and $U$ denotes the union operator for the carpooling of the drivers' ridesharing routes.
Objective 2 Maximum the number of riders for ridesharing travel:

$$
\max \sum_{i \in \mathcal{A}} \bigcup_{s \in \mathcal{S}} \mathcal{I}_{d}^{s}, a \in \mathcal{A}, s \in \mathcal{S}
$$

, where $\sum$ denotes the cumulative operator for all qualified riders, and $U$ denotes the union operator for the ridesharing routes of all recommended vehicles.

## C. Constraints of carpooling model

Constraint 1 for $m$ drivers-All of the $m$ drivers must be qualified as riders: $\quad \sum_{s \in \mathcal{S}} \mathcal{I}_{d}^{s}=1, \forall d \in \mathcal{D}$
Constraint 2 for virtual vehicles-All of recommended vehicles must be driven at the starting and ending points by the correlated car owners: $\mathcal{I}_{s d}^{s}, \mathcal{I}_{s d}^{s}=1, \exists s \in \mathcal{S}$
Constraint 3 for the time window-All of vehicles must arrive at the pickup and dropping point $x$ before upper bound of the time window:

$$
t_{A(s)}^{s} \leq l_{x}, \forall x \in \mathcal{V}
$$

Constraint 4 for the passenger capacity-The passenger load of all vehicles cannot be more than the passenger capacity at all points:

$$
q_{s}^{t} \leq Q^{t}, \forall s \in \mathcal{S}, \forall x \in \mathcal{V}
$$

Constraint 5 for pickup and dropping points-Every riders can get on and off at the pickup and dropping point $x$ only once:

$$
\sum_{s \in \mathcal{S}} \mathcal{I}_{d^{s} x}^{s}, \sum_{s \in \mathcal{S}} \mathcal{I}_{s d^{s}}^{s}=1, \forall x \in \mathcal{V}
$$

Constraint 6 for the ending point-The time for starting plus riding cannot be more than upper bound of the time window at the ending point: $\quad t_{A(s)^{+}}^{s}+t_{B(s)}^{s} \leq l_{a^{-}}, \forall a^{-} \in \mathcal{A}^{-}$
Constraint 7 for the waiting time-When a vehicle reaches a certain point $x$ at the time $t_{A(s)}^{s}$, if the service time window is still close (namely $t_{A(s)}^{s}<e_{s}$ ), then the vehicle has to wait for the lower bound of the time window until the leaving time:

$$
t_{E(s)}^{s}=\max \left\{t_{E(s)}^{s}, e_{s}\right\}, \exists t_{A(s)}^{s}<e_{s}
$$

Constraint 8 for the riding time-The riding time cannot be more than the time from starting point to ending point, because of waiting time: $\quad t_{B(s)}^{s} \leq t_{A(s)^{+}}^{s}-t_{E(s)^{+}}^{s}, \forall a \in \mathcal{A}$

## III. StOCHASTIC Optimization

In order to solve the objectives (1) and (2) subjected to the constraints (3)-(10), a stochastic optimization method based

on a two-stage estimation of distribution algorithm (EDA for short) is proposed.

## A. Ridable matrix

EDAs always use an explicit probability to reach a faster convergence than the implicit probability of most conventional evolutionary algorithms; however, identity matrix I usually used for initializing probabilistic matrix is not suitable for the multi-carpooling optimization. Since the identity matrix I will results in a large number of infeasible solutions especially in the initial stage of evolutionary computing, a ridable matrix $\boldsymbol{R}$ is proposed for improving the quality of initial probabilistic matrix. The ridable matrix $\boldsymbol{R}$ makes full use of the information including objective (1), objective (2), and constraints (3)-(10).
Definition 4 The ridable matrix $\boldsymbol{R}_{(m+n) \times(m+1)}$ denotes the relationship whether the $m+n$ riders are able to ride the $m$ vehicles or the 1 bus, where $i, j$ entry of $\boldsymbol{R}_{(m+n) \times(m+1)}$ is setup as:
$\boldsymbol{R}_{i j}=\left\{\begin{array}{l}1, \text { for } j \in\{1, \cdots, m\}, \text { if constraints (3)-(10) can hold for rider } i \\ 0, \text { for } j \in\{1, \cdots, m\}, \text { If constraints (3)-(10) cannot hold for rider } i \\ 1, \text { for } j=m+1, \text { If the rider is a passenger } i \in\{m+1, \cdots, m+n\} \\ 0, \text { for } j=m+1, \text { If the rider is a driver } i \in\{1,2, \cdots, m\}\end{array}\right.$

## B. Carpooling probabilistic matrix

Definition 5 The carpooling probabilistic matrix $\boldsymbol{P}_{(m+n) \times(m+1)}$ denotes the probability that the $m+n$ riders ride the $m$ vehicles and the bus, where the $(i, j)$ entry of $\boldsymbol{P}_{(m+n) \times(m+1)}$ denotes the probability of the rider $i$ picked up by the vehicle $j$.
The initial carpooling probabilistic matrix $\boldsymbol{P}^{(0)}$ is defined as:

$$
\boldsymbol{P}_{i j}^{(0)}= \begin{cases}\boldsymbol{R}_{i j} / \sum_{j=1}^{m+1} \boldsymbol{R}_{i j}, & \text { if } \sum_{j=1}^{m+1} \boldsymbol{R}_{i j} \neq 0 \\ 0, & \text { if } \sum_{j=1}^{m+1} \boldsymbol{R}_{i j}=0\end{cases}
$$

The update of carpooling probabilistic matrix $\boldsymbol{P}^{(k)}$ is defined as:

$$
\boldsymbol{P}_{i j}^{(k)}=\omega \boldsymbol{P}_{i j}^{(k-1)}+(1-\omega) \sum_{k}^{n} \boldsymbol{P}_{i j}^{(k)} / \kappa
$$

, where $\boldsymbol{P}_{i j}^{(k-1)}$ denotes the carpooling probabilistic of admissible solutions in the $k-1^{\text {th }}$ generation, $\omega$ denotes the inertia coefficient, $\kappa$ denotes the number of candidate solutions in the $k^{\text {th }}$ generation, $\boldsymbol{R}_{i j}^{(1)}$ denotes whether exists one satisfying the vehicle $j$ ridable by rider $i$ of the $\kappa$ candidate solutions in the $k^{\text {th }}$ generation.

## C. Fitness Function

According to the objective (1) minimizing recommended vehicles satisfying all drivers' travel, and the objective (2) maximizing qualified riders satisfying most passengers' ridesharing travel, the fitness function also takes the minimum riding distance of all recommended vehicles into account:

$$
\mathcal{F}(g, \mathcal{S}, \mathcal{A})=\left(\alpha \sum_{i \in \mathcal{S}, i \in \mathcal{V}} \mathcal{I}_{i j}+\beta\left(m+n-\sum_{i \in \mathcal{A}, i \in \mathcal{V}} \mathcal{I}_{i j}\right)+\gamma \sum_{i \in \mathcal{S}} \sum_{v, v \in \mathcal{V}} w_{i v} \mathcal{I}_{v v}\right)^{-1}
$$

## D. Augmented EDA

Augmented EDA consists of first stage and second stage.

Stage 1 is to implement ridesharing among drivers, namely, objective (1) minimizing recommended vehicles satisfying all drivers' travel.

TABLE II. First Stage of Augmented EDA
1 Initialize the ridable matrix $\boldsymbol{R}$ in Definition 4 and the carpooling probabilistic matrix $\boldsymbol{P}^{(0)}$ in Definition 5. Set $k=1, \kappa=0$.
2 Clear all the ridesharing routes, and set all the routes $\mathcal{I}_{i v v}^{+}=0$; do not recommend any vehicle $\mathcal{I}_{i v v}^{+}=0, \mathcal{I}_{i v v}^{+}=0$.
3 Randomly select one driver $i \in[1, m]$ who has not a qualified ridesharing route. Allocate a feasible virtual car $j$ for driver $i$ 's travel $d_{i} \in \mathcal{D}$ with the carpooling probability $\boldsymbol{P}_{i j}^{(k-1)}$.
4 If the driver $i$ selects his own vehicle, then recommend this vehicle, and set $\mathcal{I}_{i v v}^{+}=\mathcal{I}_{i v v}^{+}=1$; meanwhile, allocate a qualified ridesharing route for driver $i$ 's travel $d_{i} \in \mathcal{D}$, and set $\mathcal{I}_{i j}^{+}=1$.
5 If the driver $i$ has not a qualified ridesharing route, then allocate a qualified ridesharing route for driver $i$, and set $\mathcal{I}_{d}^{+}=1$.
6 If any one driver has not a qualified ridesharing route, then goto 3.
7 If all the $m$ drivers have qualified ridesharing routes, then generate a new candidate solution, set $\kappa=\kappa+1$.
If $\kappa=N$, then goto 2 .
8 Update the entries $\boldsymbol{P}_{i j}^{(1)}$ of carpooling probabilistic matrix $\boldsymbol{P}$ using (11)
9 If termination criteria $\mathcal{F} \leq \boldsymbol{\varepsilon}$ met, output; else set $k=k+1, \kappa=0$, goto 2 .
Stage 2 is to utilize the recommended vehicles for qualifying most riders' ridesharing routes, namely, objective (2) maximizing qualified riders satisfying most riders' ridesharing travel.

TABLE III. SEACOND STAGE OF AUGMENTED EDA
1 Initialize the ridable matrix $\boldsymbol{R}$ in Definition 4 and the carpooling probabilistic matrix $\boldsymbol{P}^{(0)}$ in Definition 5. Set $k=1, \kappa=0$.
2 Initialize the output of first stage to the ridesharing routes, and make all riders not qualified $\mathcal{I}_{i v}^{+}=0$.
3 Randomly select one rider $i \in[1, m+n]$ who has not a qualified ridesharing route. Allocate a feasible virtual car $j$ for rider $i$ 's travel $a_{i} \in \mathcal{A}$, with the carpooling probability $\boldsymbol{P}_{i j}^{(k+1)}$.
4 If the rider $i$ has not a qualified ridesharing route, then allocate a qualified ridesharing route for rider $i$, and set $\mathcal{I}_{i v}^{+}=1$.
5 If any one rider has not a qualified ridesharing route, then goto 3.
6 If all riders have qualified ridesharing routes, then generate a new candidate solution, set $\kappa=\kappa+1$.
If $\kappa=N$, then goto 2 .
7 Update the entries $\boldsymbol{P}_{i j}^{(k)}$ of carpooling probabilistic matrix $\boldsymbol{P}$ using (11)
8 If termination criteria $\mathcal{F} \leq \boldsymbol{\varepsilon}$ met, output; else set $k=k+1, \kappa=0$, goto 2 .

## E. Single-Stage EDA

Only making the carpooling probabilistic matrix $\boldsymbol{P}$ identity matrix $\mathbf{I}_{(m+n) \times(m+1)}$, the augmented EDA with two stages will eliminate the first stage, and directly degrade to a single-stage EDA. In single-stage EDA, all vehicles are recommended.

TABLE IV. Single Stage EDA
1 Initialize the ridable matrix $\boldsymbol{R}$ in Definition 4 and the carpooling probabilistic matrix $\boldsymbol{P}^{(\mathrm{N})}$ in Definition 5. Set $k=1, \kappa=0$.
2 Clear all the ridesharing routes, do not recommend any vehicle, make all the riders not qualified, thus set all $\mathcal{I}_{a r}^{+}=\mathcal{I}_{a r}^{+}=\mathcal{I}_{a r}^{-}=\mathcal{I}_{a r}^{+}=0$.
3 Randomly select one rider $j \in[1, m+n]$ who has not a qualified ridesharing route. Allocate a feasible virtual car $j$ for rider $i$ 's travel $a_{i} \in \mathcal{A}_{i}$ with the carpooling probability $\boldsymbol{P}_{i}^{(k+1)}$.
4 If the rider $i$ selects his own vehicle, then recommend this vehicle, and set $\mathcal{I}_{a r}^{+}=\mathcal{I}_{a r}^{+}=1$; meanwhile, allocate a qualified ridesharing route for driver $i$ 's travel $a_{i} \in \mathcal{A}$, and set $\mathcal{I}_{a r}^{+}=1$.
5 If the rider $i$ has not a qualified ridesharing route, then allocate a qualified ridesharing route for rider $i$, and set $\mathcal{I}_{a r}^{+}=1$.
6 If any one rider has not a qualified ridesharing route, then goto 3.
7 If all riders have qualified ridesharing routes, then generate a new candidate solution, set $\kappa=\kappa+1$.
If $\kappa=N$, then goto 2 .
8 Update the entries $\boldsymbol{P}_{i}^{(k)}$ of carpooling probabilistic matrix $\boldsymbol{P}$ using (11)
9 If termination criteria $\mathcal{F} \leqslant \varepsilon$ met, output; else set $k=k+1, \kappa=0$, goto 2.

## IV. NUMERIAL SIMULATION

We bought part travel data of Shenyang citizens from a tertiary commerce database. The data of 40 citizens' travel are randomly selected, including complete information from 20 drivers and 20 passengers. A visualization based on Java \& Processing has been programmed ${ }^{[8]}$. The comparison between non-carpooling (NC), first stage (FS), augmented EDA (AEDA), and single-stage EDA(SEDA) is incarnated according to the experimental results of the 40 travel data.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Average riding speed
![img-1.jpeg](img-1.jpeg)

Fig. 2. Average waiting time
![img-2.jpeg](img-2.jpeg)

Fig. 3. Average driving distance per vehicle
![img-3.jpeg](img-3.jpeg)

Fig. 4. Average riding distance per rider
![img-4.jpeg](img-4.jpeg)

Fig. 5. Passenger load per vehicle and total number of rides
The difference of average riding speeds between NC, FS, AEDA, and SEDA is small (Fig.1), respectively $35.1204 \mathrm{~km} / \mathrm{h}$, $34.7317 \mathrm{~km} / \mathrm{h}, 34.7233 \mathrm{~km} / \mathrm{h}$, and $35.0923 \mathrm{~km} / \mathrm{h}$ at $m=20$. The average waiting time of NC is zero all the time, since NC need not wait anybody at any pickup and dropping point. The average waiting time of FS, AEDA, and SEDA is 13.914 min , 9.37765 min , and 17.1596 min at $m=20$. Namely, AEDA reduces $33 \%$ waiting time compared by FS, and $45 \%$ waiting time compared by SEDA (in Fig. 2).

Because of dynamic ridesharing, AEDA takes up more riders than FS, SEDA, and NC in descending order. The average driving distances per vehicle of NC, FS, AEDA, and SEDA are $7.0685 \mathrm{~km}, 12.1953 \mathrm{~km}, 14.0871 \mathrm{~km}$, and 8.05993 km at $m=20$; however, the accumulative driving distances of NC, FS, AEDA, and SEDA are 141.37 km with 20 vehicles, 85.3671 km with 7 vehicles, 98.6096 km with 7 vehicles, and 161.19855 km with 20 vehicles at $m=20$ (in Fig. 3). AEDA reduces $65 \%$ vehicles compared with NC and SEDA, while

AEDA picks up $40 \%$ more passengers with $16 \%$ more distance than FS.

Every rider's average riding distance represents the efficiency of the carpooling service. Obviously AEDA is the most efficient with 3.52177 km at $m=20$ (Fig. 4). The values of NC, FS, and SEDA are $7.0685 \mathrm{~km}, 4.26835 \mathrm{~km}$, and 4.24207 km , which efficiency is $50 \%, 83 \%$, and $83 \%$ by AEDA.

As shown in Fig. 5, AEDA minimizes the number of recommended vehicles, and maximizes the number of qualified rides. The accumulative passenger load of NC, FS, AEDA, and SEDA reaches 20 riders with 20 vehicles, 20 riders with 7 vehicles, 28 riders with 7 vehicles, and 38 riders with 20 vehicles. Average passenger load per vehicle is 1 rider for NC, 2 riders for SEDA, 3 riders for FS, and 4 riders for AEDA.

TABLE V. COMPARISON BETWEEN NC, FS, AEDA, AND SEDA


Table V records comprehensive experimental results at $m=20$. The augmented estimation of distribution algorithm shows the most average driving distances per vehicle(Fig. 3), the least riding distance per rider(Fig. 4), the least recommended vehicles, and the most passenger load(Fig. 5).

## Conclusion and Future Works

A multi-carpooling model based on the two-stage estimation of distributed estimation algorithm is proposed for smarter traffic in intelligent transportation. The experimental results prove that the model is effcient and effective, and the optimization method can greatly reduce the traffic jam and the pressure of public transportation. This model is of high flexibility and feasibility. By modifying the carpooling
probabilistic matrix of the augmented EDA, the model can be generalized into other carpooling models. The future work will focus on integrating the information of the urban transportation network and the vehicular dynamic routing to realize a carpooling recommedation system with the high performance of distributed optimization.
