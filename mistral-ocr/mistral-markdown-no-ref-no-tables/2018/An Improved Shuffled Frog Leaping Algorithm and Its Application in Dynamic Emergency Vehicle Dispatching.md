# Research Article 

## An Improved Shuffled Frog Leaping Algorithm and Its Application in Dynamic Emergency Vehicle Dispatching

Xiaohong Duan (1), Tianyong Niu, and Qi Huang<br>School of Economics and Management, North China University of Technology, Beijing 100144, China<br>Correspondence should be addressed to Xiaohong Duan; 12116350@bjtu.edu.cn

Received 22 November 2017; Revised 20 January 2018; Accepted 28 January 2018; Published 28 March 2018
Academic Editor: Guillermo Cabrera-Guerrero
Copyright © 2018 Xiaohong Duan et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

The traditional method for solving the dynamic emergency vehicle dispatching problem can only get a local optimal strategy in each horizon. In order to obtain the dispatching strategy that can better respond to changes in road conditions during the whole dispatching process, the real-time and time-dependent link travel speeds are fused, and a time-dependent polygonal-shaped link travel speed function is set up to simulate the predictable changes in road conditions. Response times, accident severity, and accident time windows are taken as key factors to build an emergency vehicle dispatching model integrating dynamic emergency vehicle routing and selection. For the unpredictable changes in road conditions caused by accidents, the dispatching strategy is adjusted based on the real-time link travel speed. In order to solve the dynamic emergency vehicle dispatching model, an improved shuffled frog leaping algorithm (ISFLA) is proposed. The global search of the improved algorithm uses the probability model of estimation of distribution algorithm to avoid the partial optimal solution. Based on the Beijing expressway network, the efficacy of the model and the improved algorithm were tested from three aspects. The results have shown the following: (1) Compared with SFLA, the optimization performance of ISFLA is getting better and better with the increase of the number of decision variables. When the possible emergency vehicle selection strategies are $8^{15}$, the objective function value of optimal selection strategies obtained by the base algorithm is $210.10 \%$ larger than that of ISFLA. (2) The prediction error of the travel speed affects the accuracy of the initial emergency vehicle dispatching. The prediction error of $\pm 10$ can basically meet the requirements of the initial dispatching. (3) The adjustment of emergency vehicle dispatching strategy can successfully bypassed road sections affected by accidents and shorten the response time.

## 1. Introduction

Urban Expressway can ease the traffic pressure on large cities and plays an important role in the urban traffic system. However, with the increasing amount of traffic, accidents often happen on expressways and cause great damage to people's life and property. Rapid emergency rescue can effectively reduce accident loss, and emergency vehicle dispatching is the key to emergency rescue.

Research of emergency vehicle dispatching started with assumptions of static travel time or distance, and the original dispatching problem mainly included two basic issues. In the problem with one accident, we only need to choose the nearest emergency vehicle to rescue the accident. The core is the shortest paths of emergency vehicles in the road network
[1]. In the problem with multiple accidents, choosing the nearest emergency vehicle need not be an optimal decision [2]. We also need to select suitable emergency vehicles for different accidents to minimize their response times. It is a combinatorial optimization problem. Therefore, models for solving combinatorial optimization, such as Hungarian method, direct cost model, and opportunity cost model, were used to solve the emergency vehicle dispatching [3]. Aiming at the random resource requirements of potential incidents, Ozbay et al. used probabilistic constraint to improve the opportunity cost model [4]. Emergency vehicle dispatching with multiple accidents is a complex problem relating to various factors. In addition to response time, factors such as fairness, cost, and loss were considered to set up multiobjective dispatching models [5, 6]. In order to solve these

NP-hard problems, ant colony algorithm [7], particle swarm optimization [8], genetic algorithm [9], and other intelligent optimization algorithms had been widely applied.

Emergency vehicle dispatching problem considering the dynamic change of link weight (travel time, distance) started in the late 1990s. Taking the minimum response time as objective, Zografos et al. [10] integrated routing and dispatching module to set up an emergency response decision support system. Haghani et al. [11] built a simulation model of emergency vehicle dispatching. The model can assist decision makers to select suitable emergency vehicles and guide them to avoid congested areas. Dan et al. [12] divided dynamic dispatching problem into a series of static problems. Dispatching strategy was updated based on the time axis. A multiobjective model was established to solve these static problems. Yang et al. [13] set up an online dispatching and routing model for emergency vehicles. One day was divided into a number of intervals, and dispatching strategy was updated according to link travel time in each interval. Fu et al. [14] calculated the earliest response time using iteration method. A dynamic emergency resource dispatching system was designed. This research is essentially a static method for solving the dynamic problem. Dispatching strategies are continuously adjusted based on real-time traffic data at each decision-making instant. They suppose traffic data remain unchanged in the decision-making horizon. Emergency vehicles may be stopped up on the way to accidents because of changes in road conditions.

If link weight is thought to be a time-dependence function, this network is a kind of time-dependence network. Research on the time-dependence network still focuses on universal shortest path problem. On the assumption of discrete link weight based on travel time, Cooke and Halsey [15] proposed a model of the time-dependence network. Iteration method was used to solve the shortest path problem. Kaufman and Smith [16] proved that the time-dependence shortest path problem can be solved by polynomials only when the network satisfies the first-in-first-out (FIFO) property. Most of the research on the shortest path of timedependence traffic network is based on FIFO property [17]. However, road network with discrete link travel time proposed by Cooke is not FIFO [16]. In order to solve this problem, Duan et al. [18] proposed a universal shuffled frog leaping algorithm for solving the shortest path of the nonFIFO and FIFO network. Ichoua et al. [19] replaced link travel time with link travel speed to build time-dependent function. Travel time calculated by travel speed function changes continuously and satisfies the FIFO property. Since link travel speed cannot be known ahead of the decisionmaking instant, Ichoua et al. divided a day into three horizons to distinguish between congestion and free flow. During each time horizon, link travel speed remains unchanged. If this travel speed function is used to solve emergency vehicle dispatching problem, the whole dispatching process may be at a certain time horizon with constant link travel speed. This travel speed function cannot satisfy the requirement of emergency vehicle dispatching. On the assumption that link travel speed decreases continuously with the entry instant, Yuan and Wang [20] proposed an emergency vehicle routing
model taking the shortest travel time as objective. Zhou et al. [21] built a multiobjective optimization model to solve the multiperiod dynamic emergency resource scheduling problems. In order to solve the model, a multiobjective evolutionary algorithm was proposed. Zhou and Liu [22] designed a multiagent genetic algorithm to solve the multiperiod emergency resource scheduling problem considering the uncertainty of traffic. The experimental results show that the multiagent genetic algorithm precedes genetic algorithm for the problem.

According to the review of the literature, link travel speed function can reflect the dynamic changes of road conditions. However, it is difficult to model link travel speed function and solve the dynamic dispatching problem, and the dynamic problem is usually divided into a series of static problems. It only can get a local optimal strategy in each horizon. In order to get the overall optimal strategy, real-time data (reflecting the real-time road condition at decision-making instant) fuses with prediction data (reflecting the change of road condition in the whole dispatching process) to establish the link travel speed function. Meanwhile, considering the unpredictable changes in road conditions during the dispatching process, dispatching strategies are adjusted according to real-time travel speed. Multiple-incident and multipleresponse (MIMR) emergency vehicle dispatching discussed in this paper is NP-hard problem with large scale variables. The metaheuristic algorithm has advantages in solving the NP-hard problem. Shuffled frog leaping algorithm (SFLA) is a relatively new heuristic algorithm. It was first proposed and applied in water distribution network designed by Eusuff et al. [23, 24]. This algorithm combines the advantages of particle swarm optimization (PSO) and shuffled complex evolution (SCE) algorithm, and it has been proved that the algorithm has good performance in convergence speed and solution precision $[25,26]$. It was used to solve many real-word problems such as job shop scheduling and cloud computing resource allocation [27-29].

According to the above, in this paper, the polygonal time-dependent function based on real-time and prediction link travel speed is built to simulate real road conditions in expressway network. Integrating routing and selection of emergency vehicles, a dynamic dispatching model is built. The model takes time-dependent travel speed, response time, time window, and accident severity as key factors to get the optimal strategy. And the dispatching strategy is adjusted when the new accidents happen. An improved shuffled frog leaping algorithm (IFSLA) is put forward to solve the dynamic dispatching model. The algorithm uses the probabilistic model of the distribution estimation algorithm to generate new frog population. It can avoid a local optimum of shuffled frog leaping algorithm.

## 2. Problem Statement

Based on graph theory, the expressway network is abstracted as a time-dependent directed network model $(N, E, T(t) \times Q)$ as shown in Figure 1. $N=\left\{n_{1}, n_{2}, \ldots, n_{M}\right\}$ is the node set. It consists of hubs and interchanges on the expressway. $M$ is the total number of nodes. The link arc between adjacent nodes $n_{i}$

![img-0.jpeg](img-0.jpeg)

Figure 1: Expressway network model.
and $n_{j}$ is road section $\left(n_{i}, n_{j}\right) \in E$. The expressway network is a directed network, so $\left(n_{i}, n_{j}\right) \neq\left(n_{j}, n_{i}\right)$. Emergency vehicles must run along the direction of the road section, and they
can change the direction at the nodes. $Q$ is the interested time horizon. $T_{i j}(t) \in T(t)$ is the link travel time function defined in time horizon $Q$. It represents a time for the emergency vehicle, leaving at an instant $t$, traveling from node $n_{i}$ to $n_{j}$. $\forall t \in Q, t+T_{i j}(t)$ is always defined. For $t \notin Q, T_{i j}(t)$ is defined as infinity.
(1) Link Travel Time Function. Taking $\kappa$ as the minimum time interval, $Q$ is divided into discrete time intervals, that are $Q=$ $\left\{\left[t_{0}, t_{1}\right],\left[t_{1}, t_{2}\right], \ldots,\left[t_{\phi}, t_{\phi+1}\right], \ldots,\left[t_{\Phi-1}, t_{\Phi}\right]\right\}, t_{\phi}=t_{0}+\phi \cdot \kappa$, $\phi=0,1, \ldots, \Phi-1 . t_{0}$ is the initial dispatching decisionmaking instant. $t_{\Phi}=t_{0}+\Phi \cdot \kappa$ is the last instant, and make sure it is large enough for the emergency vehicle to arrive at the accident during the time period $\left[t_{0}, t_{\Phi}\right] . v_{i j}(t)$ is the link travel speed function. It represents the average speed of the road section $\left(n_{i}, n_{j}\right) \in E$ at $t \in\left[t_{0}, t_{\Phi}\right]$. Based on the link travel speed function of Ichoua et al. [19], it is assumed that travel speed in each time interval changes in the form of the polygonal line, and the polygonal-shaped travel speed function is shown in Figure 2. At the decision-making instant $t_{0}$, the real-time link travel speed $v_{i j}^{1}\left(t_{0}\right)$ is known. However, the real-time link travel speed $v_{i j}^{1}(t), t \in\left\{t_{1}, t_{2}, \ldots, t_{\phi}, \ldots, t_{\Phi}\right\}$, $t_{\phi}=t_{0}+\phi \cdot \kappa, \phi=1,2, \ldots, \Phi$, cannot be obtained. Therefore, they are approximated by the prediction travel speeds $v_{i j}^{2}(\phi)_{t_{0}}$.

The polygonal-shaped travel speed function shown in Figure 2 can be expressed as

$$
v_{i j}(t)_{t_{0}}=\left\{\begin{array}{ll}
\frac{v_{i j}^{2}(1)_{t_{0}}-v_{i j}^{1}\left(t_{0}\right)}{\kappa} \cdot t+\frac{t_{1} \cdot v_{i j}^{1}\left(t_{0}\right)-t_{0} \cdot v_{i j}^{2}(1)_{t_{0}}}{\frac{\kappa}{v_{i j}^{2}(\phi+1)_{t_{0}}-v_{i j}^{2}(\phi)_{t_{0}}} \cdot t+\frac{t_{\phi+1} \cdot v_{i j}^{2}(\phi)_{t_{0}}-t_{\phi} \cdot v_{i j}^{2}(\phi+1)_{t_{0}}}{\kappa}} & t_{0} \leq t<t_{1} \\
t_{\phi} \leq t<t_{\phi+1}, \phi=1, \ldots, \Phi-1 .
\end{array}\right.
$$

$v_{i j}(t)_{t_{0}}$ is continuous on $\left[t_{0}, t_{\Phi}\right]$, and it must be integrable on the interval $\left[t_{0}, t_{\Phi}\right]$. If the emergency vehicle enters the road section $\left(n_{i}, n_{j}\right)$ at the instant $y\left(y \geq t_{0}\right)$, its travel distance is a function of travel time $x\left(y \leq x \leq t_{\Phi}\right)$.

$$
\begin{aligned}
\int_{y}^{x} v_{i j}(t)_{t_{0}} d t & =\int_{t_{0}}^{x} v_{i j}(t)_{t_{0}} d t-\int_{t_{0}}^{y} v_{i j}(t)_{t_{0}} d t \\
& =\eta(x)-\vartheta(y)
\end{aligned}
$$

in which,

$$
\begin{aligned}
& \eta(x)=\int_{t_{0}}^{x} v_{i j}(t)_{t_{0}} d t=\int v_{i j}(x)_{t_{0}} d x+C_{1} \\
& \vartheta(y)=\int_{t_{0}}^{y} v_{i j}(t)_{t_{0}} d t=\int v_{i j}(y)_{t_{0}} d y+C_{2}
\end{aligned}
$$

Let formula (2) equal to the length $L s_{i j}$ of the road section $\left(n_{i}, n_{j}\right)$; the time when the emergency vehicle leaves the road section is

$$
x=g\left(L s_{i j}+\vartheta(y)\right)
$$

in which, $g$ is the inverse function of $\eta$.

When the emergency vehicle enters the road section at instant $t$, the travel time function of the road section is

$$
T_{i j}(t)=g\left(L s_{i j}+\vartheta(t)\right)-t
$$

(2) Dynamic Emergency Vehicle Dispatching Process. $U(t)$ accidents are waiting for rescue at the instant $t$, and they compose set $A C(t) . A c_{u}(t) \in A C(t)$ is the $u$ th accident, $u=1,2, \ldots, U(t)$. The road section where the accident $A c_{u}(t)$ occurred is expressed as $\left(n_{u}^{n}, n_{i}^{n}\right) \in E$, and its location node is $N c_{u}(t)$, its rescue time window is $\left[0, T_{\text {max }}^{n}(t)\right]$, and the required number of emergency vehicles is $N a_{u}(t)>0 . A s_{u}(t)$ represents the severity of the accident $A c_{u}(t) . E V(t)$ is the emergency vehicle set, and $E v_{i}(t) \in E V(t), l=1,2, \ldots, L(t)$, stands for the $l$ th emergency vehicle. $L(t)$ is the total number of emergency vehicles. The road section where the emergency vehicle $E v_{i}(t)$ is locatized is expressed as $\left(n_{0}^{l}, n_{1}^{l}\right) \in E$, and its location node is $N v_{i}(t)$. When the emergency vehicle $E v_{i}(t) \in$ $E V(t)$ starts traveling at an instant $t$, the shortest time path to the accident $A c_{u}(t) \in A C(t)$ is $P_{u}(t)$, and the shortest travel time is $\mathrm{T}_{\mathrm{lu}}(t)$.

The basic purpose of emergency vehicle dispatching is to shorten the response time of accidents. The response time

![img-1.jpeg](img-1.jpeg)

Figure 2: Polygonal-shaped travel speed function.
mainly depends on the travel time of the emergency vehicles. In the complex expressway network, emergency vehicles can reach accidents through multiple paths. Therefore, the shortest time path problem should be solved and the shortest travel time $\mathrm{T}_{\mathrm{In}}(t)$ from each emergency vehicle $E v_{j}(t) \in E V(t)$ to each accident $A c_{\mathrm{u}}(t) \in A C(t)$ should be obtained firstly. Then, taking $\mathrm{T}_{\mathrm{In}}(t)$ as the key factor, the suitable emergency vehicles are selected to rescue the accidents, that is, to solve the problem of emergency vehicle selection.

According to the emergency vehicle selection strategy, emergency vehicles head for accidents along the shortest paths. In this process, if there are no new accidents in the road network, travel speed function of each road section does not change obviously, but once an accident happened,
travel speeds of road sections in the accident area will be greatly affected. In order to avoid the rescue delay caused by sudden changes in road conditions, it is necessary to update link travel speed function according to the real-time speed, and the dispatching decision should be adjusted. We only need to update the travel time functions of road sections where the new accidents are located and their upstream road sections. If the rescue paths of the accident go through the new accidents, the rescue strategy for the affected accident needs to be recalculated, and the rescue strategies for the new accidents need to be calculated too.

The dynamic dispatching process consists of two stages: (1) At the decision instant $t=t_{\varphi}$, taking the polygonalshaped travel speed function as the weight of the road section, the travel path from $E v_{j}\left(t_{\varphi}\right)$ to $A c_{\mathrm{u}}\left(t_{\varphi}\right)$ is planned and the shortest travel time $\mathrm{T}_{\mathrm{In}}\left(t_{\varphi}\right)$ is obtained. (2) Taking the shortest travel time $\mathrm{T}_{\mathrm{In}}\left(t_{\varphi}\right)$ as input, emergency vehicles are selected to rescue the accidents. (3) At the instant $t=t_{\mathrm{pr} 1}$, a new accident occurs in the road network. The dispatching strategy, including vehicle routing and selection, is dynamically adjusted according to the updated real-time link travel speed.

## 3. Dynamic Emergency Vehicle Dispatching Modeling

At the decision-making instant $t=t_{\varphi}$, the shortest travel time, the required number of emergency vehicles, the upper limit of rescue time window, and the accident severity are taken as the key factors. A dynamic dispatching model with vehicle routing is built. A list of all symbols is given in Symbols.

$$
\begin{aligned}
\min & \left\{\sum_{u} \sum_{l} A z_{u}\left(t_{\varphi}\right) \times \mathrm{T}_{I u}\left(t_{\varphi}\right) \times x_{I u}\left(t_{\varphi}\right)+\sum_{u} M \times z_{u}\left(t_{\varphi}\right)\right\} \\
& E v_{l} \in E V\left(t_{\varphi}\right) \\
& \forall A c_{\mathrm{u}} \in\left\{\begin{array}{ll}
A C\left(t_{\varphi}\right) & t_{\varphi}=t_{0} \\
A C^{1}\left(t_{\varphi}\right) & t_{\varphi} \neq t_{0}
\end{array}\right. \\
\text { s.t. } & \sum_{l} x_{I u}\left(t_{\varphi}\right)=N a_{u}\left(t_{\varphi}\right) \\
& E v_{l} \in E V\left(t_{\varphi}\right) \\
& \forall A c_{\mathrm{u}} \in\left\{\begin{array}{ll}
A C\left(t_{\varphi}\right) & t_{\varphi}=t_{0} \\
A C^{1}\left(t_{\varphi}\right) & t_{\varphi} \neq t_{0}
\end{array}\right. \\
& t_{\max }^{\mathrm{u}}\left(t_{\varphi}\right)-T_{\max }^{\mathrm{u}}\left(t_{\varphi}\right) \leq M \times z_{u}\left(t_{\varphi}\right) \\
& i_{\max }^{\mathrm{u}}\left(t_{\varphi}\right)=\max \left\{\mathrm{T}_{I u}\left(t_{\varphi}\right) \times x_{I u}\left(t_{\varphi}\right)\right\} \\
& E v_{l} \in E V\left(t_{\varphi}\right) \\
& \forall A c_{\mathrm{u}} \in\left\{\begin{array}{ll}
A C\left(t_{\varphi}\right) & t_{\varphi}=t_{0} \\
A C^{1}\left(t_{\varphi}\right) & t_{\varphi} \neq t_{0}
\end{array}\right.
\end{aligned}
$$

$$
\begin{aligned}
& \sum_{u} x_{l u}\left(t_{\varphi}\right)+\sum_{l} x x_{l}\left(t_{\varphi}\right)=1 \\
& A c_{u} \in A C\left(t_{\varphi}\right) \\
& \forall E v_{l} \in E V\left(t_{\varphi}\right) \\
& \sum_{l} x_{l u}\left(t_{\varphi}\right)+\sum_{l} x x_{l}\left(t_{\varphi}\right)=L\left(t_{\varphi}\right) \\
& E v_{l} \in E V\left(t_{\varphi}\right) \\
& \forall A c_{u} \in A C\left(t_{\varphi}\right) \\
& x_{l u}\left(t_{\varphi}\right)=0,1 \\
& \forall E v_{l} \in E V\left(t_{\varphi}\right) \\
& \forall A c_{u} \in\left\{\begin{array}{ll}
A C\left(t_{\varphi}\right) & t_{\varphi}=t_{0} \\
A C^{1}\left(t_{\varphi}\right) & t_{\varphi} \neq t_{0}
\end{array}\right. \\
& z_{u}\left(t_{\varphi}\right)=0,1 \\
& \forall A c_{u} \in\left\{\begin{array}{ll}
A C\left(t_{\varphi}\right) & t_{\varphi}=t_{0} \\
A C^{1}\left(t_{\varphi}\right) & t_{\varphi} \neq t_{0}
\end{array}\right. \\
& x x_{l}\left(t_{\varphi}\right)=0,1 \\
& \forall E v_{l}\left(t_{\varphi}\right) \in E V\left(t_{\varphi}\right) \\
& \mathrm{T}_{l u}\left(t_{\varphi}\right)=\min \sum_{n_{i}=N v_{l}(t)}^{n_{0}^{u}} T_{i, i+1}\left(t_{i}\right)_{t_{\varphi}}, \\
& \forall E v_{l}\left(t_{\varphi}\right) \in E V\left(t_{\varphi}\right) \\
& \forall A c_{u} \in\left\{\begin{array}{ll}
A C\left(t_{\varphi}\right) & t_{\varphi}=t_{0} \\
A C^{1}\left(t_{\varphi}\right) & t_{\varphi} \neq t_{0}
\end{array}\right. \\
& \text { s.t. } t_{i}= \begin{cases}t_{i-1}+T_{i-1, i}\left(t_{i-1}\right)_{t_{0}} & n_{i}=n_{1}^{l}, \ldots, n_{0}^{u} \\
t_{0} & n_{i}=N v_{l}(t)\end{cases} \\
& \left(N v_{l}(t), n_{1}^{l}\right),\left(n_{1}^{l}, n_{2}^{l}\right), \ldots,\left(n_{i}, n_{i+1}\right), \ldots,\left(n_{-1}^{u}, n_{0}^{u}\right),\left(n_{0}^{u}, N c_{u}(t)\right) \in E \\
& N v_{l}(t), n_{1}^{l}, \ldots, n_{i}, \ldots, n_{0}^{u}, N c_{u}(t) \in N \\
& n_{1}^{l} \neq \cdots \neq n_{i} \neq \cdots \neq n_{0}^{u} \\
& \left(n_{1}^{l}, n_{2}^{l}\right), \ldots,\left(n_{i}, n_{i+1}\right), \ldots,\left(n_{-1}^{u}, n_{0}^{u}\right) \neq\left(n_{0}^{u^{\prime}}, n_{1}^{u^{\prime}}\right) \\
& A c_{u} \neq A c_{u^{\prime}}
\end{aligned}
$$

Formula (6) is the objective function of emergency vehicle dispatching. It consists of two parts, the total travel time for emergency vehicles $E v_{l}$ to arrive at accidents $A c_{u}$ and the punishment caused by the exceeding rescue time. In which, $M$ is a huge constant. At the initial decision-making instant $t_{\varphi}=t_{0}$, every accident $A c_{u} \in A C\left(t_{0}\right)$ needs to be rescued. At

other decision-making instants, accident set $A C^{1}\left(t_{\varphi}\right)$ includes new accidents that happened at $t_{\varphi}$ and the accidents whose rescue paths at $t_{\varphi-1}$ are affected by new accidents. Emergency vehicle set $E V\left(t_{\varphi}\right)$ contains all emergency vehicles.

Formulas (7) are the emergency vehicle requirements constraints. They make sure that the vehicle requirements of each accident can be satisfied.

Formulas (8) are time window constraints of accidents. They guarantee that the latest arrival time $t_{\max }^{n}\left(t_{\varphi}\right)$ of emergency vehicle does not exceed the upper limit of the time window $T_{\max }^{n}\left(t_{\varphi}\right)$.

Formulas (9) are constraints for the state of emergency vehicles. The emergency vehicle $E v_{l}$ can only be dispatched to an accident $A c_{u}$ or in an idle state.

Formula (10) is the constraint for the total number of emergency vehicles. It ensures that the total number of emergency vehicles dispatched to the accidents and in the idle state is $L$.

Formulas (11) are constraints for the state of variables $x_{l u}\left(t_{\varphi}\right)$. At the decision-making instant $t_{\varphi}$, if the emergency vehicle $E v_{l}, l=1,2, \ldots, L$, is dispatched to the accident $A c_{u}, u=1,2, \ldots, U$, then $x_{l u}\left(t_{\varphi}\right)=1$; otherwise, $x_{l u}\left(t_{\varphi}\right)=0$.

Formulas (12) are constraints for the state of variables $z_{u}\left(t_{\varphi}\right)$. At the decision-making instant $t_{\varphi}$, if the latest rescue time for accident $A c_{u}, u=1,2, \ldots, U$, exceeds the upper limit of rescue time window, then $z_{u}\left(t_{\varphi}\right)=1$; otherwise, $z_{u}\left(t_{\varphi}\right)=0$.

Formulas (13) are constraints for the state of variables $x x_{l}\left(t_{\varphi}\right)$. At the decision-making instant $t_{\varphi}$, if the emergency vehicle $E v_{l}, l=1,2, \ldots, L$, is in the idle state, then $x x_{l}\left(t_{\varphi}\right)=$ 1 ; otherwise, $x x_{l}\left(t_{\varphi}\right)=0$.

Formula (14) is the objective function of rescue path for the accident $A c_{u}\left(t_{\varphi}\right)$. It minimizes the travel time of the emergency vehicle from node $N v_{l}\left(t_{\varphi}\right)$ to the destination $N c_{u}\left(t_{\varphi}\right)$, where road sections $\left(n_{i}, n_{i+1}\right)$ and $\left(n_{i+1}, n_{i+2}\right)$ are connected.

Formula (15) calculates the instant $t_{i}$ when the emergency vehicle enters the road section $\left(n_{i}, n_{i+1}\right), n_{i}=N v_{l}(t), \ldots, n_{0}^{n}$.

Formulas (16)-(18) are connectivity constraints of the path. They ensure that there are no loops in the path sequence.

Formulas (19) ensure that the emergency vehicles do not pass road sections with accidents.

## 4. Solution for the Emergency Vehicle Dispatching Model

The shuffled frog leaping algorithm (SFLA) is a kind of metaheuristic algorithm that imitates the frog population's behavior in obtaining food. The initial frog population is generated and divided into several memeplexes. Then the frogs search for the optimal solution within each memeplex for the defined number of times. Then frogs in different memeplex are shuffled so that the information can be exchanged globally. The group optimization and global information exchange alternate with each other until the convergence condition is satisfied. The mathematical model of SFLA is as follows.
(1) Initialization. $H$ frogs are randomly generated to compose the initial population IP. The position of the $h$ th frog is
encoded as $X_{h}=\left[x_{h 1}, x_{h 2}, \ldots, x_{h d}, \ldots, x_{h D}\right], h=1, \ldots, H$, in which, $D$ is the dimension of the optimization problem. Each $X_{h}$ represents a feasible solution to the optimization problem. And each feasible solution corresponds to a performance function $f\left(X_{h}\right)$ associated with the optimization objective.
(2) Rank and Grouping. $H$ frogs are ranked in descending order of performance function value. Position $P x=$ $\left[p x_{1}, p x_{2}, \ldots, p x_{d}, \ldots, p x_{D}\right]$ of the optimal frog in the population is marked. The population IP is divided into $a$ memeplexes, and there are $c$ frogs in each memeplex according to

$$
M_{o_{1}}=\left\{X_{o_{1}+a\left(o_{1}-1\right)} \in \text { IP } \mid 1 \leq o_{2} \leq c\right\} \quad\left(1 \leq o_{1} \leq a\right)
$$

(3) Local Search. Within each memeplex, the local optimization process is repeated for the specified number of iterations It.
(3.1) Positions of the frogs in the memeplex, the best and the worst, are marked as $P b=\left[p b_{1}, p b_{2}, \ldots, p b_{D}, \ldots, p b_{D}\right]$ and $P w=\left[p w_{1}, p w_{2}, \ldots, p w_{d}, \ldots, p w_{D}\right]$, respectively. $P w$ is renewed along with $P b$ according to

$$
\begin{aligned}
& D s_{d} \\
& =\left\{\begin{array}{ll}
\min \left[\operatorname{INT}\left(r \times\left(p b_{d}-p w_{d}\right)\right), D_{d}^{\max }\right] & p b_{d}-p w_{d} \geq 0 \\
\max \left[\operatorname{INT}\left(r \times\left(p b_{d}-p w_{d}\right)\right),-D_{d}^{\max }\right] & p b_{d}-p w_{d}<0 \\
& d=1,2, \ldots, D \\
p w_{d}^{\prime}=p w_{d}+D s_{d}, \quad d=1,2, \ldots, D
\end{array}\right. \\
& p w_{d}^{\prime}=\left\{\begin{array}{ll}
Z_{d}^{\max } & p w_{d}^{\prime}>Z_{d}^{\max } \\
p w_{d}^{\prime} & Z_{d}^{\min } \leq p w_{d}^{\prime} \leq Z_{d}^{\max } \\
Z_{d}^{\min } & p w_{d}^{\prime}<Z_{d}^{\min }
\end{array} \quad d=1,2, \ldots, D\right.
\end{aligned}
$$

in which, $r$ is a random number, $r \in[0,1] . D s_{d}$ is the adjustment of the $d$ th decision variable, $d=1,2, \ldots, D . D_{d}^{\max }$ is the maximum adjustment of the $d$ th decision variable. $p w_{d}^{\prime}$ is the renewed position of the $d$ th decision variable. $Z_{d}^{\max }$ and $Z_{d}^{\min }$ are the upper and lower limits of the position of the $d$ th decision variable.
(3.2) If the performance value of $P w^{\prime}=\left[p w_{1}^{\prime}, p w_{2}^{\prime}, \ldots\right.$, $\left.p w_{d}^{\prime}, \ldots, p w_{D}^{\prime}\right]$ is better than $P w$, then $P w=P w^{\prime}$; otherwise, $P b$ in formula (21) is replaced with $P x$, and the position updating is executed repeatedly.
(3.3) If the performance value of $P w$ is still better than $P w^{\prime}$, then $P w$ is substituted by a random frog location.
(4) Mix and Global Search. After a local search, all memeplexes are shuffled to form a new population. Frogs are ranked and the best frog $P x$ is marked. Then the next grouping and local search are performed until the specified number of global iterations IT is completed.
4.1. Solution for the Emergency Vehicle Dispatching Model Based on Improved Shuffled Frog Leaping Algorithm. In order to solve the dynamic emergency vehicle dispatching model, an improved shuffled frog leaping algorithm (ISFLA) is

![img-2.jpeg](img-2.jpeg)

Figure 3: Principle of the ISFLA.
proposed. As shown in Figure 3, the improved algorithm is guided by the idea of a base SFLA. The local search uses the optimization strategy of SFLA, and the global search uses the probability model of estimation of distribution algorithms (EDA) to avoid the partial optimal solution.
4.1.1. Encoding and Decoding. Decision variables of the emergency vehicle dispatching are $0-1$ numerical variables $x_{l u}\left(t_{\varphi}\right)$, which express whether the vehicle $E v_{l}\left(t_{\varphi}\right)$ should be dispatched to the accident $A c_{u}\left(t_{\varphi}\right)$. The working object of SFLA is integer vector, so it is necessary to convert $x_{l u}\left(t_{\varphi}\right)$ to integer variable $x_{l}\left(t_{\varphi}\right) . x_{l}\left(t_{\varphi}\right)$ represents the dispatching strategy of $E v_{l}\left(t_{\varphi}\right), l=1,2, \ldots, L$ at the decision-making instant $t_{\varphi}$. Each vehicle can go to one of the accidents $A c_{u}\left(t_{\varphi}\right), u=1,2, \ldots, U$ or in the idle state. The feasible set of $x_{l}\left(t_{\varphi}\right)$ is $x_{l}\left(t_{\varphi}\right)=\{0,1,2, \ldots, U\}$. The emergency vehicle is an idle vehicle while $x_{l}\left(t_{\varphi}\right)=0$. In this case, the encoding of frog position can be expressed as a row vector matrix.

$$
X\left(t_{\varphi}\right)=\left[x_{1}\left(t_{\varphi}\right), x_{2}\left(t_{\varphi}\right), \ldots, x_{l}\left(t_{\varphi}\right), \ldots, x_{L}\left(t_{\varphi}\right)\right]
$$

Similarly, $x_{l}\left(t_{\varphi}\right)$ should be decoded in the reverse way of encoding, and we can get the emergency vehicle dispatching strategy.
4.1.2. Performance Function. According to the objective function of the dynamic dispatching model of emergency vehicles, the performance function is defined as

$$
\begin{aligned}
& f\left(X\left(t_{\varphi}\right)\right)=-\left\{\sum_{u} \sum_{l} A s_{u} \times \mathrm{T}_{l u}\left(t_{\varphi}\right) \times x_{l u}\left(t_{\varphi}\right)\right. \\
& \left.\quad+\sum_{u} M \times y_{u}\left(t_{\varphi}\right)+\sum_{u} M \times z_{u}\left(t_{\varphi}\right)\right\}
\end{aligned}
$$

Using the quantification method in the literature [30], the accident severity $A s_{u}$ is divided into four levels, and the value is shown in Table 1.
4.1.3. Process of the Improved Shuffled Frog Leaping Algorithm. Process of the ISFLA is shown in Figure 4, and the specific process is as follows.
(1) Build Probability Model. The decision vector of emergency vehicle dispatching is $X\left(t_{\varphi}\right)=\left\{x_{1}\left(t_{\varphi}\right), x_{2}\left(t_{\varphi}\right), \ldots\right.$, $\left.x_{l}\left(t_{\varphi}\right), \ldots, x_{L}\left(t_{\varphi}\right)\right], x_{l}\left(t_{\varphi}\right)=\{0,1,2, \ldots, U\} . U \times L$ dimensional matrix $B_{U \times L}$ is used to describe the probability distribution of the frog population. $b_{u \times l} \in[0,1]$ is the element of the matrix $B_{U \times L}$. It represents the probability that the $l$ th decision variable $x_{l}\left(t_{\varphi}\right)$ is valued as $u$.
(2) Generate the Initial Population. The value of the element $b_{u \times l}$ is set as $1 / U$. According to a uniform distribution, $H$ frogs are generated randomly to form the initial population IP. Each frog's position $X_{h}=\left[x_{h, 1}, x_{h, 2}, \ldots, x_{h, L}\right]$ represents a feasible decision vector.
(3) Local Search. $H$ frogs are ranked in descending order of performance function value $f\left(X_{h}\right)$. Location $P x$ of the optimal frog in the population is marked. The population IP is divided into $a$ memeplexes, and there are $c$ frogs in each memeplex according to formula (20). Within each memeplex,

Table 1: Value of accident severity.

![img-3.jpeg](img-3.jpeg)

Figure 4: Process of the improved SFLA.

the local optimization process is repeated for the specified number of iterations It according to formula (21)-(23).
(4) Select the Superior Individual and Update the Probability Model. The performance function value $f\left(X_{h}\right)$ of each frog in the population is calculated. $H$ frogs are reordered in descending order of performance function value. The first $H / 2$ frogs are selected to calculate the distribution of decision variables, and then the probability matrix $B^{\prime}$ is obtained. The updated probability model is

$$
B=\theta \cdot B^{\prime}+(1-\theta) \cdot B
$$

in which, $\theta$ is the forgetting factor.
(5) Generate New Population. According to the updated probability model $B_{U \times L}, H$ frogs are generated to form a new population IP.

## 5. Illustrative Examples

Beijing expressway network shown as in Figure 1 was taken as an example to demonstrate the efficacy of the model and the improved algorithm. The interested time horizon $Q$ was 9:30 to 10:30 on December 1, 2016. The minimum time interval $\kappa$ was 5 minutes. Real link travel speeds at the instant $t \in[9: 30,9: 35,9: 40, \ldots, 10: 30]$ are given in Table 2. The upper limit of the time window $T_{\max }^{u}$ was 50 minutes. Firstly, based on real link travel speeds at the instant $t \in$ $\{9: 30,9: 35,9: 40, \ldots, 10: 30\}$, five examples with different scale variable were used to test the performance of the emergency vehicle dispatching based on ISFLA. Secondly, based on prediction link travel speeds with different error ranges, two examples were used to test the performance of the dynamic emergency vehicle dispatching based on the polygonalshaped travel speed function. Thirdly, we simulated a scene of a new accident to demonstrate the efficacy of adjustment mechanism of dispatching strategy.

### 5.1. Illustrative Examples of Emergency Vehicle Dispatching Based on the Improved Shuffled Frog Leaping Algorithm

(1) Calculating Link Travel Time Time-Dependent Function. Real link travel speeds $v_{i j}^{l}(t)$ at instant $t \in[9: 30,9: 35,9: 40$, $\ldots, 10: 30]$ were used to build the polygonal-shaped travel speed function. Then the travel time function $T_{i j}(t), t \in$ [9:30, 10:30], of each road section was calculated according to formula (5). Figure 5 shows travel speed timedependent functions of road sections $\left(n_{1}, n_{2}\right),\left(n_{2}, n_{1}\right)$, $\left(n_{18}, n_{32}\right),\left(n_{32}, n_{18}\right)$, and Figure 6 shows corresponding travel time time-dependent functions of these road sections.
(2) Parameters of Illustrative Examples of Emergency Vehicle Dispatching. We assume that there are 15 emergency vehicles at most in the expressway network. At 9:30, 7 accidents at most occurred simultaneously. Tables 3 and 4 list the parameters of the example.
(3) Calculating the Shortest Travel Time for Each Emergency Vehicle to Each Accident. We assume 5 emergency vehicle
dispatching examples with different complexity. The first example has 8 emergency vehicles and 3 accidents. Then, the numbers of emergency vehicles and accidents gradually increase, and the other four examples are formed. Emergency vehicles and accidents in each example are shown in Table 5.

The dynamic shortest path algorithm of emergency vehicles in expressway network proposed in our previous research [18] was used to calculate the shortest travel time and path, and the results are shown in Tables 6 and 7.

The expressway network is a directed network. When the emergency vehicle $E v_{l}, l=1,2, \ldots, L$, goes to the accident $A c_{\mathrm{u}}, u=1,2, \ldots, U$, it must run along the direction of the road section to arrive at the node $n_{1}^{l}$ and then choose the next road section. In which, $n_{1}^{l}$ is the end of the road section $\left(n_{0}^{l}, n_{1}^{l}\right)$ where the emergency vehicle $E v_{l}$ is located. Road section from the emergency vehicle's location $N v_{l}$ to node $n_{1}^{l}$ is a necessary way for emergency vehicle $E v_{l}$. In the same way, the emergency vehicle must arrive at the node $n_{0}^{u}$ and then run along the direction of the road section to reach the accident node $N c_{\mathrm{u}}$. In which, $n_{0}^{u}$ is the start of the road section $\left(n_{0}^{u}, n_{1}^{u}\right)$ where the accident $A c_{\mathrm{u}}$ is located. Road section from the node $n_{0}^{u}$ to the accident's location $N c_{\mathrm{u}}$ is a necessary way for emergency vehicle $E v_{l}$ too. We only need to calculate the optimal path from the node $n_{1}^{l}$ to the node $n_{0}^{u}$, so the optimal path from the node $n_{1}^{l}$ to the node $n_{0}^{u}$ is given in Table 7.
(4) Calculating the Optimal Dispatching Strategy. ISFLA was used to find the optimal dispatching strategy of the five examples. The improved algorithm was compared with SFLA. After some testing, parameters of ISFLA were defined as in Table 8. After ten runs, the best solutions of the five examples obtained by using these two algorithms are summarized in Table 9. Figure 7 shows the evolutionary processes of the two algorithms of example I and example V.
(5) Result Analysis. The applicability of the model and the improved algorithm for solving the emergency vehicle dispatching problems with different complexity were verified by the five illustrative examples. Under the constraints of emergency vehicle requirements and time windows, the optimal dispatching strategy takes accident severity as key factor to optimize the total travel times of emergency vehicles. The results correspond to the decision rules of emergency vehicle dispatching.

In example I, there are $4^{8}$ possible emergency vehicle selection strategies. Analyzing Table 9 shows that SFLA and ISFLA get the same optimal selection strategies. Their objective function values are 7987.

In example II, there are $5^{10}$ possible emergency vehicle selection strategies. Analyzing Table 9 shows that the objective function of optimal selection strategy obtained by using ISFLA is 8113. The SFLA is unwanted early convergence. Its objective function value of optimal selection strategies is $13.14 \%$ larger than that of ISFLA.

In example III, there are $6^{12}$ possible emergency vehicle selection strategies. Analyzing Table 9 shows that the objective function of optimal selection strategy obtained by using ISFLA is 10247 . The SFLA is unwanted early convergence.

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

Figure 5: Link travel speed time-dependent functions.

Table 3: Accident parameters of the illustrative example.
Table 4: Emergency vehicle parameters of the illustrative example.
![img-9.jpeg](img-9.jpeg)

Figure 6: Link travel time time-dependent functions.
![img-10.jpeg](img-10.jpeg)

Figure 7: Evolutionary processes of the two algorithms for solving the illustrative examples.

Table 5: Emergency vehicles and accidents in each example.
Its objective function value of optimal selection strategies is $34.91 \%$ larger than that of ISFLA.

In example IV, there are $7^{14}$ possible emergency vehicle selection strategies. Analyzing Table 9 shows that the objective function of optimal selection strategy obtained by using ISFLA is 12061. The SFLA is unwanted early convergence. Its objective function value of optimal selection strategies is $50.04 \%$ larger than that of ISFLA.

In example V, there are $8^{15}$ possible emergency vehicle selection strategies. Analyzing Table 9 shows that the objective function of optimal selection strategy obtained by using ISFLA is 12947. The SFLA is unwanted early convergence. Its objective function value of optimal selection strategies is $210.10 \%$ larger than that of ISFLA.

Therefore, compared with SFLA, the optimization performance of ISFLA is getting better and better with the increase of the number of decision variables. ISFLA preceded SFLA in realizing the optimal resolution for the complicated emergency vehicle selection problem.
5.2. Illustrative Examples of Dynamic Emergency Vehicle Dispatching Based on the Prediction Link Travel Speed. Examples I and II in Section 5.1 were used to test the performance of dynamic emergency vehicle dispatching based on the prediction link travel speed. Polygonal-shaped travel speed functions $v_{i j}(t), t \in[9: 30,10: 30], \forall\left(n_{i}, n_{j}\right) \in E$, were built using prediction travel speeds with different absolute error intervals $( \pm 3 \mathrm{~km} / \mathrm{h}, \pm 5 \mathrm{~km} / \mathrm{h}$, and $\pm 10 \mathrm{~km} / \mathrm{h})$. The present prediction methods can control the maximum absolute error of the prediction travel speed within $\pm 10 \mathrm{~km} / \mathrm{h}[31,32]$, so the maximum prediction error was assumed as $\pm 10 \mathrm{~km} / \mathrm{h}$. The prediction travel speed $v_{i j}^{2}\left(\phi\right) t_{i j}$ was randomly generated within the interval $\left[v_{i j}^{1}\left(t_{\phi}\right)-10, v_{i j}^{1}\left(t_{\phi}\right)+10\right]$, in which, $v_{i j}^{1}\left(t_{\phi}\right)$ is the real vehicle speed at the instant $t_{\phi}$. In order to analyze the effect of the decrease of prediction error on the initial emergency vehicle dispatching strategy, the two prediction errors $\pm 3 \mathrm{~km} / \mathrm{h}$ and $\pm 5 \mathrm{~km} / \mathrm{h}$ were assumed. Then the travel time functions $T_{i j}(t), t \in[9: 30,10: 30]$, of each road section were calculated according to formula (5). The dynamic shortest path algorithm of emergency vehicles in expressway network proposed in our previous research [18] was used to calculate the shortest travel time and path, and the results are shown in Tables 10 and 11.

ISFLA was used to find the optimal dispatching strategy of the two examples under three prediction errors, and the best solutions are shown in Table 12.

In example I, the optimal emergency vehicle dispatching strategy (including vehicle routing and selection), which is
based on the prediction link travel speed with prediction errors of $\pm 3, \pm 5$, is the same as the actual optimal strategy. However, when the prediction error is $\pm 10$, the rescue vehicle for the accident $A c_{2}$ is different from the actual optimal strategy. The emergency vehicle $E v_{7}$ instead of the vehicle $E v_{8}$ is dispatched to the accident $A c_{2}$. This led to a 23.4594 $-21.7823=1.6771$ minutes extension of the rescue time for the accident $A c_{2}$. The objective function value based on the prediction travel speed is 101 more than that based on the real travel speed. It can be seen that the prediction error of the travel speed affects the accuracy of the initial emergency vehicle dispatching, but when the absolute prediction error is within $\pm 10$, the effect is not obvious.

In example II, the optimal emergency vehicle dispatching strategy (including vehicle routing and selection), which is based on the prediction link travel speed with prediction errors of $\pm 3, \pm 5$, and $\pm 10$, is the same as the actual optimal strategy.

It is known from the two examples that the prediction error of $\pm 10$ can basically meet the requirements of the initial dispatching.
5.3. Illustrative Example of Dynamic Adjustment of Dispatching Strategy. Example 1 in Section 5.2 was used to test the performance of dynamic adjustment of dispatching strategy. Suppose that the prediction error of link travel speed was $\pm 5$. At 9:30, emergency vehicles were dispatched to accidents according to the optimal dispatching strategy obtained in Section 5.2. Emergency vehicle $E v_{3}$ was dispatched to accident $A c_{1}$. Emergency vehicle $E v_{3}$ was dispatched to accident $A c_{3}$. Emergency vehicle $E v_{4}$ was dispatched to accident $A c_{2}$. Emergency vehicle $E v_{8}$ was dispatched to accident $A c_{2}$. Emergency vehicles $E v_{1}, E v_{5}$, and $E v_{7}$ were idle vehicles. The optimal dispatching strategy is shown in Figure 8.

At 9:35, a new accident $A c_{4}$ happens on the road section $(9,20)$. According to the real link travel speed, location of each emergency vehicle was calculated. They are shown in Figure 9.

Due to the influence of the accident $A c_{4}$, road conditions of the accident section $(9,20)$ and its upstream sections $(8,9)$ and $(1,9)$ changed. In order to consider the impact of accident $A c_{4}$ on upstream sections, a weakening factor $\alpha_{i j}(t)$ to the travel speed of upstream section $\left(n_{i}, n_{j}\right)$ was introduced. Therefore, the travel speed functions of sections $(8,9)$ and $(1,9)$ were $v_{8,9}^{1}(t)=\alpha_{8,9}(t) \cdot v_{8,9}(t), v_{1,9}^{1}(t)=\alpha_{1,9}(t) \cdot v_{1,9}(t)$, respectively. Suppose that $\alpha_{i j}$ decreases linearly with time $t$. The initial value $\alpha_{i j}\left(t=t_{\phi}\right)=0.7$. When $t=t_{\phi}+30 \mathrm{~min}$, $\alpha_{i j}(t)=0.53$.

The travel speed of each road section was recollected at 9:35, and the prediction travel speed function was calculated. We suppose that travel speed prediction error of road sections $(8,9)$ and $(1,9)$ was $\pm 10$ and that of other road sections was $\pm 5$. Then, travel paths of emergency vehicles were replanned, and the dispatching strategy was adjusted. The optimal dispatching strategy at 9:35 is shown in Figure 10. The dynamic emergency vehicle dispatching process is shown in Table 13.

Table 6: The shortest travel time of the illustrative examples based on the real link travel speed.

Table 6: Continued.
![img-11.jpeg](img-11.jpeg)

Figure 8: Optimal emergency vehicle dispatching strategy at 9:30.

Table 7: The shortest travel time path of the illustrative examples based on the real link travel speed.
Table 7: Continued.
Table 7: Continued.

Note. BL means that the travel time of the optimal path exceeds the upper limit of the time window.
![img-12.jpeg](img-12.jpeg)

Figure 9: Locations of emergency vehicles and accidents at 9:35.

When the accident $A c_{4}$ happened at 9:35, the dynamical adjustment mechanism timely responded to sudden changes in road conditions of the optimal path $(8,9,20,21)$ of emergency vehicle $E v_{2}$. After recalculating the dispatching strategy, the idle emergency vehicle $E v_{1}$ replaced the emergency vehicle $E v_{2}$ to rescue the accident $A c_{1}$. The emergency vehicle successfully bypassed road sections $(9,20)$ and $(8,9)$ to ensure the time limit for emergency rescue. Meanwhile, the emergency vehicle $E v_{2}$ with the shortest travel time was dispatched to the new accident $A c_{4}$. Therefore, the adjustment
of emergency vehicle dispatching strategy can effectively shorten the response time of accident.

## 6. Conclusions

The emergency vehicle dispatching in urban expressway network includes dynamic routing and emergency vehicles election. And the dispatching strategy needs to be adjusted according to the dynamic road conditions. Firstly, polygonalshaped travel speed function based on real-time and

Table 8: Parameter selection of ISFLA.
![img-13.jpeg](img-13.jpeg)

Figure 10: Optimal emergency vehicle dispatching strategy at 9:35.
prediction link travel speed is set up, and the dynamic emergency vehicle dispatching process is illustrated. Secondly, taking the accident severity as the key factor and the travel time as the objective function, a dynamic dispatching model considering the vehicle routing was established. The model consists of two stages: initial dispatching and dynamic adjustment. Thirdly, in order to avoid unwanted early convergence of SFLA in solving complex dispatching problems, the basic

SFLA was combined with the probabilistic model of EDA, and the SFLA was improved. Finally, Beijing expressway network was taken as an example to test the efficacy of the model and the algorithm from three aspects. First, based on the real link travel speed, 5 emergency vehicle dispatching problems with different scale variable were modeled and solved by the improved shuffled frog leaping algorithm. Second, based on the prediction link travel speed and the

![img-14.jpeg](img-14.jpeg)

![img-15.jpeg](img-15.jpeg)

![img-16.jpeg](img-16.jpeg)

Table 10: The shortest travel time of the illustrative examples based on the prediction link travel speed.
Table 10: Continued.
real-time link travel speed, the dynamic emergency vehicle dispatching model and the improved SFLA were used to calculate the global optimal dispatching strategy. Third, a scene in which a new accident happened on the rescue path was simulated, and the dispatching strategy was adjusted. The results show the following: (1) The emergency vehicle dispatching model can obtain the optimal dispatching strategy under the constraints of accident demands and time windows. (2) For solving the complicated emergency vehicle selection problem, the improved SFLA has stronger search ability compared with the SFLA and can obtain more optimal dispatching strategy. (3) The optimal strategy obtained by the emergency vehicle dispatching model based on the prediction link travel speed takes into account the dynamic changes in the road conditions during the whole dispatching process. (4) The dynamic adjustment condition can timely respond to sudden changes in the road conditions and help emergency vehicles to avoid rescue delay.

## Symbols

$N$ :
The expressway network node set
$n_{i}, i=1,2, \ldots, M$ : The $i$ th expressway network node
$M$ : The total number of nodes in the expressway network

The road section set of the expressway network
The road section form the node $n_{i}$ to the node $n_{j}$
$Q$ :
The interested time horizon
$T_{i j}(t)$ :
The link travel time function defined in time horizon $Q$. It represents a time for the emergency vehicle, leaving at an instant $t$, from node $n_{i}$ to $n_{j}$
$T(t)$ :
The link travel time function set
$\kappa$ :
The minimum time interval
$t_{0}$ :
The initial dispatching decision-making instant
$t_{\phi}, \phi=0,1, \ldots, \Phi$ : The start time of the $\phi$ th time interval $t_{\Phi}$ :
$v_{i j}(t)$ :
The last instant of the interested time horizon
$v_{i j}(t)$ :
The link travel speed function of the road section $\left(n_{i}, n_{j}\right)$ at the instant $t$
$v_{i j}^{\mathrm{t}}\left(t_{0}\right)$ :
The real-time link travel speed of the road section $\left(n_{i}, n_{j}\right)$ at the instant $t_{0}$
$v_{i j}^{2}(\phi)_{t_{0}}$ :
The prediction travel speed at the instant $t_{\phi}$ calculated according to $v_{i j}^{\mathrm{t}}\left(t_{0}\right)$

Table 11: The shortest travel time path of the illustrative examples based on the prediction link travel speed.
Table 11: Continued.
Note. BL means that the travel time of the optimal path exceeds the upper limit of the time window.
$v_{i j}(t)_{t_{0}}$ :
The polygonal-shaped travel speed function at the instant $t_{0}$
$L s_{i j}$ :
The length of the road section $\left(n_{i}, n_{j}\right)$
$U(t)$ :
The total number of accidents at the instant $t$
$A C(t)$ :
The accident set at the instant $t$
$A c_{u}(t) \in A C(t)$,
$u=1,2, \ldots, U(t)$ :
$\left(n_{0}^{n}, n_{1}^{n}\right) \in E$ :
The road section where the accident
$A c_{u}(t)$ occurred at the instant $t$
$N c_{u}(t)$ :
The location node of the accident
$A c_{u}(t)$
$T_{\max }^{n}(t)$ :
The upper limit of rescue time window of the accident $A c_{u}(t)$
$N a_{u}(t)$ :
The required number of emergency vehicles for the accident $A c_{u}(t)$
$A s_{u}(t)$ :
The severity of the accident $A c_{u}(t)$
$E V(t)$ :
The emergency vehicle set at the instant $t$
$E v_{j}(t) \in E V(t)$,
The $l$ th emergency vehicle at the instant $t$
The total number of emergency
vehicles at the instant $t$
$N v_{l}(t)$ :
When the emergency vehicle
$P_{l u}(t)$ :
When the emergency vehicle
$E v_{l}(t) \in E V(t)$ starts traveling at an instant $t$, the shortest time path to the accident $A c_{u}(t) \in A C(t)$
The travel time of the shortest time path $P_{l u}(t)$ at the instant $t$
The $q$ th decision instant
The decision variable; at the decision-making instant $t_{\varphi}$, if the emergency vehicle $E v_{l}, l=1,2, \ldots, L$, is dispatched to the accident
$A c_{u}, u=1,2, \ldots, U$, then $x_{l u}\left(t_{\varphi}\right)=1$; otherwise, $x_{l u}\left(t_{\varphi}\right)=0$
The decision variable; at the decision-making instant $t_{\varphi}$, if the latest rescue time for accident
$A c_{u}, u=1,2, \ldots, U$ exceeds the upper limit of rescue time window, then $z_{u}\left(t_{\varphi}\right)=1$; otherwise, $z_{u}\left(t_{\varphi}\right)=0$
$L(t)$ :
A huge constant
$L(t)$ :
The total number of emergency
$A C^{1}\left(t_{\varphi}\right)$ :
The accident set includes new accidents that happened at $t_{\varphi}$ and the accidents whose rescue paths at $t_{\varphi-1}$ are affected by new accidents

![img-17.jpeg](img-17.jpeg)

![img-18.jpeg](img-18.jpeg)

Table 13: Dynamic emergency vehicle dispatching process.
$t_{\max }^{\mathrm{u}}\left(t_{\varphi}\right): \quad$| The latest rescue time of the accident |

$P b=\left[p b_{1}, p b_{2},\right.$ The position of the best frog in the memeplex
$P w=\left[p w_{1}, p w_{2},\right.$ The position of the worst frog in the
$\ldots, p w_{d}, \ldots, p w_{D}$ ] : memeplex
$D s_{d}, d=$ The adjustment of the $d$ th decision
$1,2, \ldots, D:$ variable
$r \in[0,1]:$ A random number
$D_{d}^{\max }:$ The maximum adjustment of the $d$ th decision variable
$p w_{d}^{\prime}:$ The renewed position of the $d$ th decision variable
$Z_{d}^{\max }$ : The upper limits of the position of the $d$ th decision variable
$Z_{d}^{\min }$ : The lower limits of the position of the $d$ th decision variable
IT: The total number of global iterations
$x_{l}\left(t_{\varphi}\right):$ The coding of the decision variable $x_{l u}\left(t_{\varphi}\right)$; it represents the dispatching strategy of $E v_{l}\left(t_{\varphi}\right), l=1,2, \ldots, L$, at decision-making instant $t_{\varphi}$ The probability distribution matrix of the frog population
$b_{\mathrm{u} \times l} \in[0,1]:$ The element of the matrix $B_{U \times I}$; it represents the probability that the $l$ th decision variable $x_{l}\left(t_{\varphi}\right)$ is valued as $u$ The forgetting factor.

## Conflicts of Interest

The authors declare that there are no conflicts of interest regarding the publication of this article.

## Acknowledgments

This work is supported by Funding for Scientific Research Startup of North China University of Technology.
