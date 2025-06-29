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

| Accident level |  | Description of the accident |  |  |  | Accident severity |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | Death toll | The number of serious injuries (SI) | The number of slight injuries | Property loss (L) |  |
| Minor accident | Situation 1 | - | - | 1-2 | - | 40 |
|  | Situation 2 | - | - | - | Motor vehicle accidents: $<1,000$ <br> Nonmotor vehicle accidents: $<200$ |  |
| Ordinary accident | Situation 1 | - | $1-2$ | - | - | 60 |
|  | Situation 2 | - | - | $\geqslant 3$ | - |  |
|  | Situation 3 | - | - | - | $<30,000$ |  |
| Major accident | Situation 1 | $1-2$ | - | - | - | 80 |
|  | Situation 2 | - | $3 \leqslant \mathrm{SI}<10$ | - | - |  |
|  | Situation 3 | - | - | - | $30,000 \leqslant L<60,000$ |  |
| Extra serious accident | Situation 1 | $\geqslant 3$ | - | - | - | 100 |
|  | Situation 2 | - | $\geqslant 11$ | - | - |  |
|  | Situation 3 | 1 | $\geqslant 8$ | - | - |  |
|  | Situation 4 | 2 | $\geqslant 5$ | - | - |  |
|  | Situation 5 | - | - | - | $\geqslant 60,000$ |  |

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

| Accident no. | Accident node | Road section of accident | Location of accident | Accident level | Accident severity | Accident demand |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | $N c_{1} / n_{48}$ | $\left(n_{21}, n_{22}\right)$ | $L_{21,48}=L_{48,22}$ | Minor | 40 | 1 |
| 2 | $N c_{2} / n_{49}$ | $\left(n_{6}, n_{5}\right)$ | $L_{6,49}=L_{49,5}$ | Ordinary | 60 | 2 |
| 3 | $N c_{3} / n_{30}$ | $\left(n_{27}, n_{14}\right)$ | $L_{27,50}=L_{30,14}$ | Major | 80 | 2 |
| 4 | $N c_{4} / n_{31}$ | $\left(n_{16}, n_{13}\right)$ | $L_{16,51}=L_{51,15}$ | Minor | 40 | 1 |
| 5 | $N c_{5} / n_{32}$ | $\left(n_{9}, n_{20}\right)$ | $L_{9,52}=L_{52,20}$ | Minor | 40 | 2 |
| 6 | $N c_{6} / n_{33}$ | $\left(n_{38}, n_{39}\right)$ | $L_{38,53}=L_{53,39}$ | Ordinary | 60 | 2 |
| 7 | $N c_{7} / n_{24}$ | $\left(n_{47}, n_{44}\right)$ | $L_{47,24}=L_{24,44}$ | Minor | 40 | 1 |

Table 4: Emergency vehicle parameters of the illustrative example.

| Vehicle no. | 1 | 2 | 3 | 4 | 5 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Vehicle node | $N v_{1} / n_{55}$ | $N v_{2} / n_{56}$ | $N v_{3} / n_{57}$ | $N v_{4} / n_{58}$ | $N v_{5} / n_{59}$ |
| Road section of vehicle | $\left(n_{2}, n_{3}\right)$ | $\left(n_{9}, n_{8}\right)$ | $\left(n_{12}, n_{13}\right)$ | $\left(n_{18}, n_{17}\right)$ | $\left(n_{15}, n_{29}\right)$ |
| Location of vehicle | $L_{2,55}=L_{55,3}$ | $L_{9,56}=L_{56,8}$ | $L_{12,57}=L_{57,13}$ | $L_{18,58}=L_{58,17}$ | $L_{15,59}=L_{59,29}$ |
| Vehicle no. | 6 | 7 | 8 | 9 | 10 |
| Vehicle node | $N v_{6} / n_{60}$ | $N v_{7} / n_{61}$ | $N v_{8} / n_{62}$ | $N v_{9} / n_{63}$ | $N v_{10} / n_{64}$ |
| Road section of vehicle | $\left(n_{39}, n_{25}\right)$ | $\left(n_{30}, n_{31}\right)$ | $\left(n_{33}, n_{32}\right)$ | $\left(n_{19}, n_{33}\right)$ | $\left(n_{24}, n_{13}\right)$ |
| Location of vehicle | $L_{39,60}=L_{60,25}$ | $L_{30,61}=L_{61,31}$ | $L_{33,62}=L_{62,32}$ | $L_{19,63}=L_{63,33}$ | $L_{24,64}=L_{64,13}$ |
| Vehicle no. | 11 | 12 | 13 | 14 | 15 |
| Vehicle node | $N v_{11} / n_{65}$ | $N v_{12} / n_{66}$ | $N v_{13} / n_{67}$ | $N v_{14} / n_{68}$ | $N v_{15} / n_{69}$ |
| Road section of vehicle | $\left(n_{28}, n_{29}\right)$ | $\left(n_{12}, n_{23}\right)$ | $\left(n_{27}, n_{28}\right)$ | $\left(n_{2}, n_{10}\right)$ | $\left(n_{18}, n_{32}\right)$ |
| Location of vehicle | $L_{28,65}=L_{65,29}$ | $L_{12,66}=L_{66,23}$ | $L_{27,67}=L_{67,28}$ | $L_{3,68}=L_{68,10}$ | $L_{18,69}=L_{69,32}$ |

![img-9.jpeg](img-9.jpeg)

Figure 6: Link travel time time-dependent functions.
![img-10.jpeg](img-10.jpeg)

Figure 7: Evolutionary processes of the two algorithms for solving the illustrative examples.

Table 5: Emergency vehicles and accidents in each example.

| Example no. | Vehicle no. | Accident no. |
| :-- | :--: | :--: |
| I | $1,2,3,4,5,6,7,8$ | $1,2,3$ |
| II | $1,2,3,4,5,6,7,8,9,10$ | $1,2,3,4$ |
| III | $1,2,3,4,5,6,7,8,9,10,11,12$ | $1,2,3,4,5$ |
| IV | $1,2,3,4,5,6,7,8,9,10,11,12,13,14$ | $1,2,3,4,5,6$ |
| V | $1,2,3,4,5,6,7,8,9,10,11,12,13,14,15$ | $1,2,3,4,5,6,7$ |

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

| Vehicle no. | Example no. | Accident no. |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 1 | I | 31.2925 | 38.9665 | 54.9495 | $--$ | $--$ | $--$ | $--$ |
|  | II | 31.2925 | 38.9665 | 54.9495 | 54.2331 | $--$ | $--$ | $--$ |
|  | III | 31.2925 | 38.9665 | 54.9495 | 54.2331 | 34.8666 | $--$ | $--$ |
|  | IV | 31.2925 | 38.9665 | 54.9495 | 54.2331 | 34.8666 | 45.2505 | $--$ |
|  | V | 31.2925 | 38.9665 | 54.9495 | 54.2331 | 34.8666 | 45.2505 | co |
| 2 | I | 22.1482 | 31.9124 | co | $--$ | $--$ | $--$ | $--$ |
|  | II | 22.1482 | 31.9124 | co | 28.8721 | $--$ | $--$ | $--$ |
|  | III | 26.9763 | 31.9124 | co | 28.8721 | 15.2541 | $--$ | $--$ |
|  | IV | 26.9763 | 31.9124 | co | 28.8721 | 15.2541 | co | $--$ |
|  | V | 26.9763 | 31.9124 | co | 28.8721 | 15.2541 | co | $38.6391$ |
| 3 | I | 48.3611 | 47.2027 | 33.8637 | $--$ | $--$ | $--$ | $--$ |
|  | II | 48.3611 | 47.2027 | 33.8637 | 59.0018 | $--$ | $--$ | $--$ |
|  | III | 48.3611 | 47.2027 | 33.8637 | 59.0018 | 54.0921 | $--$ | $--$ |
|  | IV | 48.3611 | 47.2027 | 33.8637 | 59.0018 | 54.0921 | 28.6649 | $--$ |
|  | V | 48.3611 | 47.2027 | 33.8637 | 59.0018 | 54.0921 | 28.6649 | $--$ |
| 4 | I | 41.0760 | 16.3454 | 53.4742 | $--$ | $--$ | $--$ | $--$ |
|  | II | 41.0760 | 16.3454 | co | 10.1881 | $--$ | $--$ | $--$ |
|  | III | 41.0760 | 16.3454 | co | 10.1881 | 35.6330 | $--$ | $--$ |
|  | IV | 41.0760 | 16.3454 | co | 10.1881 | 35.6330 | co | $--$ |
|  | V | 41.0760 | 16.3454 | co | 10.1881 | 35.6330 | co | $19.4956$ |
| 5 | I | 49.9989 | 25.1126 | 38.7917 | $--$ | $--$ | $--$ | $--$ |
|  | II | 49.9989 | 25.1126 | 38.7917 | 19.8843 | $--$ | $--$ | $--$ |
|  | III | 49.9989 | 25.1126 | 38.7917 | 19.8843 | 43.5353 | $--$ | $--$ |
|  | IV | 49.9989 | 25.1126 | 38.7917 | 19.8843 | 43.5353 | 45.7355 | $--$ |
|  | V | 49.9989 | 25.1126 | 38.7917 | 19.8843 | 43.5353 | 45.7355 | $23.4806$ |
| 6 | I | 44.4116 | co | 26.3079 | $--$ | $--$ | $--$ | $--$ |
|  | II | 44.4116 | co | 26.3079 | co | $--$ | $--$ | $--$ |
|  | III | 44.4116 | co | 26.3079 | co | 54.4887 | $--$ | $--$ |
|  | IV | 44.4116 | co | 26.3079 | co | 54.4887 | 21.4419 | $--$ |
|  | V | 44.4116 | co | 26.3079 | co | 54.4887 | 21.4419 | co |
| 7 | I | 43.6867 | 23.4594 | 56.5536 | $--$ | $--$ | $--$ | $--$ |
|  | II | 43.6867 | 23.4594 | 56.5536 | 14.4705 | $--$ | $--$ | $--$ |
|  | III | 43.6867 | 23.4594 | 56.5536 | 14.4705 | 41.8074 | $--$ | $--$ |
|  | IV | 43.6867 | 23.4594 | 56.5536 | 14.4705 | 41.8074 | $--$ | $--$ |
|  | V | 43.6867 | 23.4594 | 56.5536 | 14.4705 | 41.8074 | $--$ | $12.3566$ |
| 8 | I | 42.6146 | 21.7823 | co | $--$ | $--$ | $--$ | $--$ |
|  | II | 42.6146 | 21.7823 | co | 21.3312 | $--$ | $--$ | $--$ |
|  | III | 42.6146 | 21.7823 | co | 21.3312 | 40.7481 | $--$ | $--$ |
|  | IV | 42.6146 | 21.7823 | co | 21.3312 | 40.7481 | co | $--$ |
|  | V | 42.6146 | 21.7823 | co | 21.3312 | 40.7481 | co | $20.0396$ |
| 9 | II | 37.8754 | 33.6324 | co | 30.5210 | $--$ | $--$ | $--$ |
|  | III | 37.8754 | 33.6324 | co | 30.5210 | 42.3188 | $--$ | $--$ |
|  | IV | 37.8754 | 33.6324 | co | 30.5210 | 42.3188 | co | $--$ |
|  | V | 37.8754 | 33.6324 | co | 30.5210 | 42.3188 | co | $29.6284$ |
| 10 | II | 42.3397 | 40.7709 | 28.2020 | 52.5731 | $--$ | $--$ | $--$ |
|  | III | 42.3397 | 40.7709 | 28.2020 | 52.5731 | 47.7124 | $--$ | $--$ |
|  | IV | 42.3397 | 40.7709 | 28.2020 | 52.5731 | 47.7124 | 24.0304 | $--$ |
|  | V | 42.3397 | 40.7709 | 28.2020 | 52.5731 | 47.7124 | 24.0304 | $--$ |
| 11 | III | co | 27.4119 | 40.8674 | 21.9920 | 45.8012 | $--$ | $--$ |
|  | IV | co | 27.4119 | 40.8674 | 21.9920 | 45.8012 | 48.8987 | $--$ |
|  | V | co | 27.4119 | 40.8674 | 21.9920 | 45.8012 | 48.8987 | 25.3691 |

Table 6: Continued.

| Vehicle no. | Example no. | Accident no. |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 12 | III | 25.3758 | 49.7617 | 48.7390 | 00 | 33.5190 | -- | -- |
|  | IV | 25.3758 | 49.7617 | 48.7390 | 00 | 33.5190 | 32.6388 | -- |
|  | V | 25.3758 | 49.7617 | 48.7390 | 00 | 33.5190 | 32.6388 | 00 |
| 13 | IV | 00 | 34.0944 | 21.9164 | 31.4456 | 54.1145 | 37.1084 | -- |
|  | V | 00 | 34.0944 | 21.9164 | 31.4456 | 54.1145 | 37.1084 | 33.8540 |
| 14 | IV | 10.1994 | 32.9815 | 00 | 48.1107 | 13.8316 | 54.7018 | -- |
|  | V | 10.1994 | 32.9815 | 00 | 48.1107 | 13.8316 | 54.7018 | 00 |
| 15 | V | 43.5208 | 22.7684 | 00 | 22.3348 | 41.7501 | 00 | 20.7021 |

![img-11.jpeg](img-11.jpeg)

Figure 8: Optimal emergency vehicle dispatching strategy at 9:30.

Table 7: The shortest travel time path of the illustrative examples based on the real link travel speed.

| Vehicle no. | Example no. | Accident no. |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 1 | I | 3, 2, 10, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | -- |  |  |  |
|  | II | 3, 2, 10, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | $\begin{aligned} & 3,2,1,6,18 \\ & 17,16 \end{aligned}$ |  |  |  |
|  | III | 3, 2, 10, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | $\begin{aligned} & 3,2,1,6,18 \\ & 17,16 \end{aligned}$ | 3, 2, 1, 9 | -- | -- |
|  | IV | 3, 2, 10, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | $\begin{aligned} & 3,2,1,6,18 \\ & 17,16 \end{aligned}$ | 3, 2, 1, 9 | 3, 12, 23, 37, 38 |  |
|  | V | 3, 2, 10, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | $\begin{aligned} & 3,2,1,6,18 \\ & 17,16 \end{aligned}$ | 3, 2, 1, 9 | 3, 12, 23, 37, 38 | BL |
| 2 | I | 8, 9, 20, 21 | 8, 7, 18, 6 | BL | -- |  |  |  |
|  | II | 8, 9, 20, 21 | 8, 7, 18, 6 | BL | 8, 7, 18, 17, 16 |  |  |  |
|  | III | 8, 9, 10, 21 | 8, 7, 18, 6 | BL | 8, 7, 18, 17, 16 | 8, 9 | -- | -- |
|  | IV | 8, 9, 10, 21 | 8, 7, 18, 6 | BL | 8, 7, 18, 17, 16 | 8, 9 | BL |  |
|  | V | 8, 9, 10, 21 | 8, 7, 18, 6 | BL | 8, 7, 18, 17, 16 | 8, 9 | BL | $\begin{gathered} 8,7,18,17,16,30, \\ 47 \end{gathered}$ |
| 3 | I | $\begin{gathered} 13,12,11,22, \\ 21 \end{gathered}$ | 13, 4, 5, 6 | 13, 14, 27 | -- |  |  |  |
|  | II | $\begin{gathered} 13,12,11,22, \\ 21 \end{gathered}$ | 13, 4, 5, 6 | 13, 14, 27 | 13, 4, 5, 15, 16 |  |  |  |
|  | III | $\begin{gathered} 13,12,11,22, \\ 21 \end{gathered}$ | 13, 4, 5, 6 | 13, 14, 27 | 13, 4, 5, 15, 16 | 13, 12, 11, 10, 9 | -- | -- |
|  | IV | $\begin{gathered} 13,12,11,22, \\ 21 \end{gathered}$ | 13, 4, 5, 6 | 13, 14, 27 | 13, 4, 5, 15, 16 | 13, 12, 11, 10, 9 | 13, 24, 38 | -- |
|  | V | $\begin{gathered} 13,12,11,22, \\ 21 \end{gathered}$ | 13, 4, 5, 6 | 13, 14, 27 | 13, 4, 5, 15, 16 | 13, 12, 11, 10, 9 | 13, 24, 38 | BL |
| 4 | I | $\begin{gathered} 17,18,6,1,2, \\ 10,21 \end{gathered}$ | 17, 18, 6 | $\begin{gathered} 17,16,15,14, \\ 27 \end{gathered}$ | -- |  |  |  |
|  | II | $\begin{gathered} 17,18,6,1,2, \\ 10,21 \end{gathered}$ | 17, 18, 6 | BL | 17, 16 |  |  |  |
|  | III | $\begin{gathered} 17,18,6,1,2, \\ 10,21 \end{gathered}$ | 17, 18, 6 | BL | 17, 16 | 17, 18, 7, 8, 9 | -- | -- |
|  | IV | $\begin{gathered} 17,18,6,1,2, \\ 10,21 \end{gathered}$ | 17, 18, 6 | BL | 17, 16 | 17, 18, 7, 8, 9 | BL | -- |
|  | V | $\begin{gathered} 17,18,6,1,2, \\ 10,21 \end{gathered}$ | 17, 18, 6 | BL | 17, 16 | 17, 18, 7, 8, 9 | BL | 17, 31, 47 |
| 5 | I | $\begin{gathered} 29,15,5,6,1, \\ 2,10,21 \end{gathered}$ | 29, 15, 5, 6 | 29, 28, 27 | -- |  |  |  |
|  | II | $\begin{gathered} 29,15,5,6,1, \\ 2,10,21 \end{gathered}$ | 29, 15, 5, 6 | 29, 28, 27 | 29, 15, 16 |  |  |  |
|  | III | $\begin{gathered} 29,15,5,6,1, \\ 2,10,21 \end{gathered}$ | 29, 15, 5, 6 | 29, 28, 27 | 29, 15, 16 | $\begin{gathered} 29,15,5,6,1, \\ 9 \end{gathered}$ | -- | -- |
|  | IV | $\begin{gathered} 29,15,5,6,1, \\ 2,10,21 \end{gathered}$ | 29, 15, 5, 6 | 29, 28, 27 | 29, 15, 16 | $\begin{gathered} 29,15,5,6,1, \\ 9 \end{gathered}$ | 29, 43, 42, 41, 40, | -- |
|  | V | $\begin{gathered} 29,15,5,6,1, \\ 2,10,21 \end{gathered}$ | 29, 15, 5, 6 | 29, 28, 27 | 29, 15, 16 | $\begin{gathered} 29,15,5,6,1, \\ 9 \end{gathered}$ | 29, 43, 42, 41, 40, |  |
|  | I | $\begin{gathered} 25,24,23,22, \\ 21 \end{gathered}$ | BL | 25, 26, 27 | -- |  |  |  |
|  | II | $\begin{gathered} 25,24,23,22, \\ 21 \end{gathered}$ | BL | 25, 26, 27 | BL |  |  |  |
|  | III | $\begin{gathered} 25,24,23,22, \\ 21 \end{gathered}$ | BL | 25, 26, 27 | BL | $\begin{gathered} 25,24,23,12, \\ 11,10,9 \end{gathered}$ | -- | -- |
|  | IV | $\begin{gathered} 25,24,23,22, \\ 21 \end{gathered}$ | BL | 25, 26, 27 | BL | $\begin{gathered} 25,24,23,12, \\ 11,10,9 \end{gathered}$ | 25, 24, 38 | -- |
|  | V | $\begin{gathered} 25,24,23,22, \\ 21 \end{gathered}$ | BL | 25, 26, 27 | BL | $\begin{gathered} 25,24,23,12, \\ 11,10,9 \end{gathered}$ | 25, 24, 38 | BL |

Table 7: Continued.

| Vehicle no. | Example no. | Accident no. |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 7 | I | $\begin{gathered} 31,32,33,19, \\ 20,21 \end{gathered}$ | $\begin{gathered} 31,17,18,6 \end{gathered}$ | $\begin{gathered} 31,30,29,28, \\ 27 \end{gathered}$ | $--$ |  |  |  |
|  | II | $\begin{gathered} 31,32,33,19, \\ 20,21 \end{gathered}$ | $31,17,18,6$ | $\begin{gathered} 31,30,29,28, \\ 27 \end{gathered}$ | $31,30,16$ |  |  |  |
|  | III | $\begin{gathered} 31,32,33,19, \\ 20,21 \end{gathered}$ | $31,17,18,6$ | $\begin{gathered} 31,30,29,28, \\ 27 \end{gathered}$ | $31,30,16$ | $\begin{gathered} 31,17,18,6,1, \\ 9 \end{gathered}$ | $--$ | $--$ |
|  | IV | $\begin{gathered} 31,32,33,19, \\ 20,21 \end{gathered}$ | $31,17,18,6$ | $\begin{gathered} 31,30,29,28, \\ 27 \end{gathered}$ | $31,30,16$ | $\begin{gathered} 31,17,18,6,1, \\ 9 \end{gathered}$ | BL | $--$ |
|  | V | $\begin{gathered} 31,32,33,19, \\ 20,21 \end{gathered}$ | $31,17,18,6$ | $\begin{gathered} 31,30,29,28, \\ 27 \end{gathered}$ | $31,30,16$ | $\begin{gathered} 31,17,18,6,1, \\ 9 \end{gathered}$ | BL | 31,47 |
| 8 | I | $\begin{gathered} 32,33,19,20, \\ 21 \end{gathered}$ | $32,18,6$ | BL | $--$ |  |  |  |
|  | II | $\begin{gathered} 32,33,19,20, \\ 21 \end{gathered}$ | $32,18,6$ | BL | $32,18,17,16$ |  |  |  |
|  | III | $\begin{gathered} 32,33,19,20, \\ 21 \end{gathered}$ | $32,18,6$ | BL | $32,18,17,16$ | $32,18,6,1,9$ | $--$ |  |
|  | IV | $\begin{gathered} 32,33,19,20, \\ 21 \end{gathered}$ | $32,18,6$ | BL | $32,18,17,16$ | $32,18,6,1,9$ | BL | $--$ |
|  | V | $\begin{gathered} 32,33,19,20, \\ 21 \end{gathered}$ | $32,18,6$ | BL | $32,18,17,16$ | $32,18,6,1,9$ | BL | $32,31,47$ |
| 9 | II | $33,19,20,21$ | $33,32,18,6$ | BL | $\begin{gathered} 33,32,18,17, \\ 16 \end{gathered}$ | $33,19,8,9$ | $--$ | $--$ |
|  | III | $33,19,20,21$ | $33,32,18,6$ | BL | $\begin{gathered} 33,32,18,17, \\ 16 \end{gathered}$ | $33,19,8,9$ | BL | $--$ |
|  | IV | $33,19,20,21$ | $33,32,18,6$ | BL | $\begin{gathered} 33,32,18,17, \\ 16 \end{gathered}$ | $33,19,8,9$ | BL | $--$ |
|  | V | $33,19,20,21$ | $33,32,18,6$ | BL | $\begin{gathered} 33,32,18,17, \\ 16 \end{gathered}$ | $33,19,8,9$ | BL | $33,32,31,47$ |
| 10 | II | $\begin{gathered} 13,12,11,22, \\ 21 \end{gathered}$ | $13,4,5,6$ | $13,14,27$ | $13,4,5,15,16$ |  |  |  |
|  | III | $\begin{gathered} 13,12,11,22, \\ 21 \end{gathered}$ | $13,4,5,6$ | $13,14,27$ | $13,4,5,15,16$ | $13,12,11,10,9$ | $--$ | $--$ |
|  | IV | $\begin{gathered} 13,12,11,22, \\ 21 \end{gathered}$ | $13,4,5,6$ | $13,14,27$ | $13,4,5,15,16$ | $13,12,11,10,9$ | $13,24,38$ | $--$ |
|  | V | $\begin{gathered} 13,12,11,22, \\ 21 \end{gathered}$ | $13,4,5,6$ | $13,14,27$ | $13,4,5,15,16$ | $13,12,11,10,9$ | $13,24,38$ | BL |
| 11 | III | BL | $29,15,5,6$ | $29,28,27$ | $29,15,16$ | $\begin{gathered} 29,15,5,6,1, \\ 9 \end{gathered}$ | $--$ | $--$ |
|  | IV | BL | $29,15,5,6$ | $29,28,27$ | $29,15,16$ | $\begin{gathered} 29,15,5,6,1, \\ 9 \end{gathered}$ | $\begin{gathered} 29,43,42,41,40, \\ 39,38 \end{gathered}$ | $--$ |
|  | V | BL | $29,15,5,6$ | $29,28,27$ | $29,15,16$ | $\begin{gathered} 29,15,5,6,1, \\ 9 \end{gathered}$ | $\begin{gathered} 29,43,42,41,40, \\ 39,38 \end{gathered}$ | $29,30,47$ |
| 12 | III | $23,22,21$ | $\begin{gathered} 23,12,3,2,1, \\ 6 \end{gathered}$ | $\begin{gathered} 23,24,25,26, \\ 27 \end{gathered}$ | BL | $23,12,11,10,9$ | $--$ | $--$ |
|  | IV | $23,22,21$ | $\begin{gathered} 23,12,3,2,1, \\ 6 \end{gathered}$ | $\begin{gathered} 23,24,25,26, \\ 27 \end{gathered}$ | BL | $23,12,11,10,9$ | $23,37,38$ | $--$ |
|  | V | $23,22,21$ | $\begin{gathered} 23,12,3,2,1, \\ 6 \end{gathered}$ | $\begin{gathered} 23,24,25,26, \\ 27 \end{gathered}$ | BL | $23,12,11,10,9$ | $23,37,38$ | BL |
| 13 | IV | BL | $28,29,15,5,6$ | $28,27$ | $28,29,15,16$ | $\begin{gathered} 28,29,15,5, \\ 6,1,9 \end{gathered}$ | $\begin{gathered} 28,42,41,40,39, \\ 38 \end{gathered}$ | $--$ |
|  | V | BL | $28,29,15,5,6$ | $28,27$ | $28,29,15,16$ | $\begin{gathered} 28,29,15,5, \\ 6,1,9 \end{gathered}$ | $\begin{gathered} 28,42,41,40,39, \\ 38 \end{gathered}$ | $28,29,30,47$ |
| 14 | IV | 10,21 | 10, 2, 1, 6 | BL | $\begin{gathered} 10,9,8,7,18, \\ 17,16 \end{gathered}$ | 10,9 | $\begin{gathered} 10,21,35,36,37, \\ 38 \end{gathered}$ | $--$ |
|  | V | 10,21 | 10, 2, 1, 6 | BL | $\begin{gathered} 10,9,8,7,18, \\ 17,16 \end{gathered}$ | 10,9 | $\begin{gathered} 10,21,35,36,37, \\ 38 \end{gathered}$ | BL |

Table 7: Continued.

| Vehicle no. | Example no. | Accident no. |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 15 | V | $\begin{gathered} 32,33,19,20 \\ 21 \end{gathered}$ | $32,18,6$ | BL | $32,18,17,16$ | $32,18,6,1,9$ | BL | $32,31,47$ |

Note. BL means that the travel time of the optimal path exceeds the upper limit of the time window.
![img-12.jpeg](img-12.jpeg)

Figure 9: Locations of emergency vehicles and accidents at 9:35.

When the accident $A c_{4}$ happened at 9:35, the dynamical adjustment mechanism timely responded to sudden changes in road conditions of the optimal path $(8,9,20,21)$ of emergency vehicle $E v_{2}$. After recalculating the dispatching strategy, the idle emergency vehicle $E v_{1}$ replaced the emergency vehicle $E v_{2}$ to rescue the accident $A c_{1}$. The emergency vehicle successfully bypassed road sections $(9,20)$ and $(8,9)$ to ensure the time limit for emergency rescue. Meanwhile, the emergency vehicle $E v_{2}$ with the shortest travel time was dispatched to the new accident $A c_{4}$. Therefore, the adjustment
of emergency vehicle dispatching strategy can effectively shorten the response time of accident.

## 6. Conclusions

The emergency vehicle dispatching in urban expressway network includes dynamic routing and emergency vehicles election. And the dispatching strategy needs to be adjusted according to the dynamic road conditions. Firstly, polygonalshaped travel speed function based on real-time and

Table 8: Parameter selection of ISFLA.

| Example no. | IP | $a$ | $c$ | IT | $\begin{gathered} D_{d}^{\max } \\ d=1, \ldots, D \end{gathered}$ | $\begin{gathered} Z_{d}^{\max } \\ d=1, \ldots, D \end{gathered}$ | $\begin{gathered} Z_{d}^{\min } \\ d=1, \ldots, D \end{gathered}$ | $D$ | $\theta$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| I | 150 | 15 | 10 | 150 | 3 | 4 | 1 | 8 | 0.05 |
| II | 150 | 15 | 10 | 350 | 4 | 5 | 1 | 10 | 0.05 |
| III | 300 | 20 | 15 | 600 | 5 | 6 | 1 | 12 | 0.05 |
| IV | 374 | 22 | 17 | 800 | 5 | 7 | 1 | 14 | 0.05 |
| V | 500 | 25 | 20 | 900 | 6 | 8 | 1 | 15 | 0.05 |

![img-13.jpeg](img-13.jpeg)

Figure 10: Optimal emergency vehicle dispatching strategy at 9:35.
prediction link travel speed is set up, and the dynamic emergency vehicle dispatching process is illustrated. Secondly, taking the accident severity as the key factor and the travel time as the objective function, a dynamic dispatching model considering the vehicle routing was established. The model consists of two stages: initial dispatching and dynamic adjustment. Thirdly, in order to avoid unwanted early convergence of SFLA in solving complex dispatching problems, the basic

SFLA was combined with the probabilistic model of EDA, and the SFLA was improved. Finally, Beijing expressway network was taken as an example to test the efficacy of the model and the algorithm from three aspects. First, based on the real link travel speed, 5 emergency vehicle dispatching problems with different scale variable were modeled and solved by the improved shuffled frog leaping algorithm. Second, based on the prediction link travel speed and the

![img-14.jpeg](img-14.jpeg)

![img-15.jpeg](img-15.jpeg)

![img-16.jpeg](img-16.jpeg)

Table 10: The shortest travel time of the illustrative examples based on the prediction link travel speed.

| Vehicle no. | Example no. | Prediction error (km/h) | Accident no. |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  | 1 | 2 | 3 | 4 |
| 1 | I | 0 | 31.2925 | 38.9665 | 54.9495 | $--$ |
|  |  | $\pm 3$ | 31.2737 | 38.5534 | 54.9460 | $--$ |
|  |  | $\pm 5$ | 32.1368 | 38.4649 | 55.5341 | $--$ |
|  |  | $\pm 10$ | 31.5763 | 42.7993 | 50.3388 | $--$ |
|  | II | 0 | 31.2925 | 38.9665 | 54.9495 | 54.2331 |
|  |  | $\pm 3$ | 31.2737 | 38.5534 | 54.9460 | 53.9916 |
|  |  | $\pm 5$ | 32.1368 | 38.4649 | 55.5341 | 53.4761 |
|  |  | $\pm 10$ | 31.5763 | 42.7993 | 50.3388 | co |
| 2 | I | 0 | 22.1482 | 31.9124 | co | $--$ |
|  |  | $\pm 3$ | 20.8670 | 32.3468 | co | $--$ |
|  |  | $\pm 5$ | 23.1840 | 31.3765 | co | $--$ |
|  | II | $\pm 10$ | 18.3767 | 32.2828 | co | $--$ |
|  |  | 0 | 22.1482 | 31.9124 | co | 28.8721 |
|  |  | $\pm 3$ | 20.8670 | 32.3468 | co | 28.8694 |
|  |  | $\pm 5$ | 23.1840 | 31.3765 | co | 30.9670 |
|  |  | $\pm 10$ | 18.3767 | 32.2828 | co | 26.4442 |
| 3 | I | 0 | 48.3611 | 47.2027 | 33.8637 | $--$ |
|  |  | $\pm 3$ | 46.8840 | 47.3166 | 33.7495 | $--$ |
|  |  | $\pm 5$ | 46.8704 | 47.2581 | 33.8035 | $--$ |
|  | II | $\pm 10$ | 46.4381 | 52.2131 | 33.2153 | $--$ |
|  |  | 0 | 48.3611 | 47.2027 | 33.8637 | 59.0018 |
|  |  | $\pm 3$ | 46.8840 | 47.3166 | 33.7495 | 59.8245 |
|  |  | $\pm 5$ | 46.8704 | 47.2581 | 33.8035 | co |
|  |  | $\pm 10$ | 46.4381 | 52.2131 | 33.2153 | 58.7999 |
| 4 | I | 0 | 41.0760 | 16.3454 | 53.4742 | $--$ |
|  |  | $\pm 3$ | 41.2953 | 16.4075 | 54.8336 | $--$ |
|  |  | $\pm 5$ | 41.6761 | 16.6789 | 52.0917 | $--$ |
|  | II | $\pm 10$ | 40.3378 | 17.3145 | 53.4260 | $--$ |
|  |  | 0 | 41.0760 | 16.3454 | co | 10.1881 |
|  |  | $\pm 3$ | 41.2953 | 16.4075 | co | 10.5117 |
|  |  | $\pm 5$ | 41.6761 | 16.6789 | co | 9.5027 |
|  |  | $\pm 10$ | 40.3378 | 17.3145 | co | 9.6885 |
| 5 | I | 0 | 49.9989 | 25.1126 | 38.7917 | $--$ |
|  |  | $\pm 3$ | 49.5269 | 25.4762 | 38.9094 | $--$ |
|  |  | $\pm 5$ | 50.8201 | 24.7458 | 38.8310 | $--$ |
|  | II | $\pm 10$ | 50.8567 | 28.2398 | 38.5163 | $--$ |
|  |  | 0 | 49.9989 | 25.1126 | 38.7917 | 19.8843 |
|  |  | $\pm 3$ | 49.5269 | 25.4762 | 38.9094 | 19.9819 |
|  |  | $\pm 5$ | 50.8201 | 24.7458 | 38.8310 | 18.5017 |
|  |  | $\pm 10$ | 50.8567 | 28.2398 | 38.5163 | 22.5535 |
| 6 | I | 0 | 44.4116 | co | 26.3079 | $--$ |
|  |  | $\pm 3$ | 43.5208 | 51.2845 | 25.8029 | $--$ |
|  |  | $\pm 5$ | 47.1051 | 51.4706 | 25.4729 | $--$ |
|  | II | $\pm 10$ | 50.1697 | 54.9481 | 31.6198 | $--$ |
|  |  | 0 | 44.4116 | co | 26.3079 | co |
|  |  | $\pm 3$ | 43.5208 | 51.2845 | 25.8029 | 59.7672 |
|  |  | $\pm 5$ | 47.1051 | 51.4706 | 25.4729 | co |
|  |  | $\pm 10$ | 50.1697 | 54.9481 | 31.6198 | co |

Table 10: Continued.

| Vehicle no. | Example no. | Prediction error (km/h) | Accident no. |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  | 1 | 2 | 3 | 4 |
| 7 | I | 0 | 43.6867 | 23.4594 | 56.5536 | $--$ |
|  |  | $\pm 3$ | 43.8486 | 23.8514 | 56.9816 | $--$ |
|  |  | $\pm 5$ | 42.8287 | 22.6855 | 53.4435 | $--$ |
|  |  | $\pm 10$ | 42.4865 | 24.9977 | 55.1983 | $--$ |
|  | II | 0 | 43.6867 | 23.4594 | 56.5536 | 14.4705 |
|  |  | $\pm 3$ | 43.8486 | 23.8514 | 56.9816 | 14.7354 |
|  |  | $\pm 5$ | 42.8287 | 22.6855 | 53.4435 | 13.9424 |
|  |  | $\pm 10$ | 42.4865 | 24.9977 | 55.1983 | 13.5972 |
| 8 | I | 0 | 42.6146 | 21.7823 | $\infty$ | $--$ |
|  |  | $\pm 3$ | 42.7782 | 21.8997 | $\infty$ | $--$ |
|  |  | $\pm 5$ | 42.5819 | 21.8541 | $\infty$ | $--$ |
|  | II | $\pm 10$ | 40.9011 | 26.2546 | $\infty$ | $--$ |
|  |  | 0 | 42.6146 | 21.7823 | $\infty$ | 21.3312 |
|  |  | $\pm 3$ | 42.7782 | 21.8997 | $\infty$ | 21.5001 |
|  |  | $\pm 5$ | 42.5819 | 21.8541 | $\infty$ | 20.9878 |
|  |  | $\pm 10$ | 40.9011 | 26.2546 | $\infty$ | 22.7096 |
| 9 | II | 0 | 37.8754 | 33.6324 | $\infty$ | 30.5210 |
|  |  | $\pm 3$ | 37.3625 | 33.4413 | $\infty$ | 29.9943 |
|  |  | $\pm 5$ | 39.1213 | 34.4820 | $\infty$ | 31.7022 |
|  |  | $\pm 10$ | 37.5274 | 35.6110 | $\infty$ | 29.7247 |
| 10 | II | 0 | 42.3397 | 40.7709 | 28.2020 | 52.5731 |
|  |  | $\pm 3$ | 40.9388 | 40.6356 | 28.5534 | 53.1496 |
|  |  | $\pm 5$ | 42.4467 | 40.9227 | 28.6415 | 55.0761 |
|  |  | $\pm 10$ | 41.3142 | 41.4190 | 26.8230 | 51.2051 |

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

| Vehicle no. | Example no. | Prediction error (km/h) | Accident no. |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  | 1 | 2 | 3 | 4 |
| 1 | I | 0 | 3, 2, 10, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | -- |
|  |  | $\pm 3$ | 3, 2, 10, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | -- |
|  |  | $\pm 5$ | 3, 12, 11, 22, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | -- |
|  |  | $\pm 10$ | 3, 12, 11, 22, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | -- |
|  |  | 0 | 3, 2, 10, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | 3, 2, 1, 6, 18, 17, 16 |
|  | II | $\pm 3$ | 3, 2, 10, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | 3, 2, 1, 6, 18, 17, 16 |
|  |  | $\pm 5$ | 3, 12, 11, 22, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | 3, 2, 1, 6, 18, 17, 16 |
|  |  | $\pm 10$ | 3, 12, 11, 22, 21 | 3, 2, 1, 6 | 3, 12, 13, 14, 27 | BL |
| 2 | I | 0 | 8, 9, 20, 21 | 8, 7, 18, 6 | BL | -- |
|  |  | $\pm 3$ | 8, 9, 20, 21 | 8, 7, 18, 6 | BL | -- |
|  |  | $\pm 5$ | 8, 9, 20, 21 | 8, 7, 1, 6 | BL | -- |
|  |  | $\pm 10$ | 8, 9, 20, 21 | 8, 7, 18, 6 | BL | -- |
|  |  | 0 | 8, 9, 20, 21 | 8, 7, 18, 6 | BL | $8,7,18,17,16$ |
|  | II | $\pm 3$ | 8, 9, 20, 21 | 8, 7, 18, 6 | BL | 8, 7, 18, 17, 16 |
|  |  | $\pm 5$ | 8, 9, 20, 21 | 8, 7, 1, 6 | BL | 8, 7, 18, 17, 16 |
|  |  | $\pm 10$ | 8, 9, 20, 21 | 8, 7, 18, 6 | BL | 8, 7, 18, 17, 16 |
| 3 | I | 0 | 13, 12, 11, 22, 21 | 13, 4, 5, 6 | 13, 14, 27 | -- |
|  |  | $\pm 3$ | 13, 12, 11, 22, 21 | 13, 4, 5, 6 | 13, 14, 27 | -- |
|  |  | $\pm 5$ | 13, 12, 11, 22, 21 | 13, 4, 5, 6 | 13, 14, 27 | -- |
|  |  | $\pm 10$ | 13, 12, 11, 22, 21 | 13, 4, 5, 6 | 13, 14, 27 | -- |
|  |  | 0 | 13, 12, 11, 22, 21 | 13, 4, 5, 6 | 13, 14, 27 | 13, 4, 5, 15, 16 |
|  | II | $\pm 3$ | 13, 12, 11, 22, 21 | 13, 4, 5, 6 | 13, 14, 27 | 13, 4, 5, 15, 16 |
|  |  | $\pm 5$ | 13, 12, 11, 22, 21 | 13, 4, 5, 6 | 13, 14, 27 | BL |
|  |  | $\pm 10$ | 13, 12, 11, 22, 21 | 13, 4, 5, 6 | 13, 14, 27 | 13, 14, 15, 16 |
| 4 | I | 0 | 17, 18, 6, 1, 2, 10, 21 | 17, 18, 6 | 17, 16, 15, 14, 27 | -- |
|  |  | $\pm 3$ | 17, 18, 6, 1, 2, 10, 21 | 17, 18, 6 | 17, 16, 15, 14, 27 | -- |
|  |  | $\pm 5$ | 17, 18, 7, 8, 19, 20, 21 | 17, 18, 6 | 17, 16, 15, 14, 27 | -- |
|  |  | $\pm 10$ | 17, 18, 6, 1, 2, 10, 21 | 17, 18, 6 | 17, 16, 15, 14, 27 | -- |
|  |  | 0 | 17, 18, 6, 1, 2, 10, 21 | 17, 18, 6 | BL | 17, 16 |
|  | II | $\pm 3$ | 17, 18, 6, 1, 2, 10, 21 | 17, 18, 6 | BL | 17, 16 |
|  |  | $\pm 5$ | 17, 18, 7, 8, 19, 20, 21 | 17, 18, 6 | BL | 17, 16 |
|  |  | $\pm 10$ | 17, 18, 6, 1, 2, 10, 21 | 17, 18, 6 | BL | 17, 16 |
| 5 | I | 0 | 29, 15, 5, 6, 1, 2, 10, 21 | 29, 15, 5, 6 | 29, 28, 27 | -- |
|  |  | $\pm 3$ | 29, 15, 5, 6, 1, 2, 10, 21 | 29, 15, 5, 6 | 29, 28, 27 | -- |
|  |  | $\pm 5$ | 29, 15, 5, 6, 1, 2, 10, 21 | 29, 15, 5, 6 | 29, 28, 27 | -- |
|  |  | $\pm 10$ | 29, 15, 5, 6, 1, 9, 20, 21 | 29, 15, 5, 6 | 29, 28, 27 | -- |
|  | II | 0 | 29, 15, 5, 6, 1, 2, 10, 21 | 29, 15, 5, 6 | 29, 28, 27 | 29, 15, 16 |
|  |  | $\pm 3$ | 29, 15, 5, 6, 1, 2, 10, 21 | 29, 15, 5, 6 | 29, 28, 27 | 29, 15, 16 |
|  |  | $\pm 5$ | 29, 15, 5, 6, 1, 2, 10, 21 | 29, 15, 5, 6 | 29, 28, 27 | 29, 15, 16 |
|  |  | $\pm 10$ | 29, 15, 5, 6, 1, 9, 20, 21 | 29, 15, 5, 6 | 29, 28, 27 | 29, 30, 16 |
| 6 |  | 0 | 25, 24, 23, 22, 21 | BL | 25, 26, 27 | -- |
|  | I | $\pm 3$ | 25, 24, 23, 22, 21 | 25, 24, 13, 4, 5, 6 | 25, 26, 27 | -- |
|  |  | $\pm 5$ | 25, 24, 23, 22, 21 | 25, 24, 13, 4, 5, 6 | 25, 26, 27 | -- |
|  |  | $\pm 10$ | 25, 24, 23, 22, 21 | 25, 24, 13, 4, 5, 6 | 25, 26, 27 | -- |
|  |  | 0 | 25, 24, 23, 22, 21 | BL | 25, 26, 27 | BL |
|  | II | $\pm 3$ | 25, 24, 23, 22, 21 | 25, 24, 13, 4, 5, 6 | 25, 26, 27 | 25, 24, 13, 4, 5, 15, 16 |
|  |  | $\pm 5$ | 25, 24, 23, 22, 21 | 25, 24, 13, 4, 5, 6 | 25, 26, 27 | BL |
|  |  | $\pm 10$ | 25, 24, 23, 22, 21 | 25, 24, 13, 4, 5, 6 | 25, 26, 27 | BL |

Table 11: Continued.

| Vehicle no. | Example no. | Prediction error (km/h) | Accident no. |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  | 1 | 2 | 3 | 4 |
| 7 | I | 0 | $31,32,33,19,20,21$ | $31,17,18,6$ | $31,30,29,28,27$ | -- |
|  |  | $\pm 3$ | $31,32,33,19,20,21$ | $31,17,18,6$ | $31,30,29,28,27$ | -- |
|  |  | $\pm 5$ | $31,32,33,19,20,21$ | $31,17,18,6$ | $31,30,29,28,27$ | -- |
|  |  | $\pm 10$ | $31,32,33,19,20,21$ | $31,17,18,6$ | $31,30,29,43,42,41,27$ | -- |
|  | II | 0 | $31,32,33,19,20,21$ | $31,17,18,6$ | $31,30,29,28,27$ | $31,30,16$ |
|  |  | $\pm 3$ | $31,32,33,19,20,21$ | $31,17,18,6$ | $31,30,29,28,27$ | $31,30,16$ |
|  |  | $\pm 5$ | $31,32,33,19,20,21$ | $31,17,18,6$ | $31,30,29,28,27$ | $31,30,16$ |
|  |  | $\pm 10$ | $31,32,33,19,20,21$ | $31,17,18,6$ | $31,30,29,43,42,41,27$ | $31,30,16$ |
| 8 | I | 0 | $32,33,19,20,21$ | $32,18,6$ | BL | -- |
|  |  | $\pm 3$ | $32,33,19,20,21$ | $32,18,6$ | BL | -- |
|  |  | $\pm 5$ | $32,33,19,20,21$ | $32,18,6$ | BL | -- |
|  |  | $\pm 10$ | $32,33,19,20,21$ | $32,18,6$ | BL | -- |
|  | II | 0 | $32,33,19,20,21$ | $32,18,6$ | BL | $32,18,17,16$ |
|  |  | $\pm 3$ | $32,33,19,20,21$ | $32,18,6$ | BL | $32,18,17,16$ |
|  |  | $\pm 5$ | $32,33,19,20,21$ | $32,18,6$ | BL | $32,18,17,16$ |
|  |  | $\pm 10$ | $32,33,19,20,21$ | $32,18,6$ | BL | $32,18,17,16$ |
| 9 | II | 0 | $33,19,20,21$ | $33,32,18,6$ | BL | $33,32,18,17,16$ |
|  |  | $\pm 3$ | $33,19,20,21$ | $33,32,18,6$ | BL | $33,32,18,17,16$ |
|  |  | $\pm 5$ | $33,19,20,21$ | $33,32,18,6$ | BL | $33,32,31,30,16$ |
|  |  | $\pm 10$ | $33,19,20,21$ | $33,32,18,6$ | BL | $33,32,18,17,16$ |
| 10 | II | 0 | $13,12,11,22,21$ | $13,4,5,6$ | $13,14,27$ | $13,4,5,15,16$ |
|  |  | $\pm 3$ | $13,12,11,22,21$ | $13,4,5,6$ | $13,14,27$ | $13,4,5,15,16$ |
|  |  | $\pm 5$ | $13,12,11,22,21$ | $13,4,5,6$ | $13,14,27$ | $13,4,5,15,16$ |
|  |  | $\pm 10$ | $13,12,11,22,21$ | $13,4,5,6$ | $13,14,27$ | $13,14,15,16$ |

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

| Decision making instant | Vehicle no. | Road section of vehicle | Location of vehicle | The optimal solution | Optimal emergency vehicle dispatching strategy |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 9:30 | 1 | $\left(n_{2}, n_{3}\right)$ | $L_{2,55}=L_{55,3}$ | $0,1,3,2,0,3,0,2$ | $E v_{2}$ to $A c_{1}:$ |
|  | 2 | $\left(n_{9}, n_{8}\right)$ | $L_{9,36}=L_{56,8}$ |  | $N v_{2} \rightarrow n_{8} \rightarrow n_{9} \rightarrow n_{20} \rightarrow n_{21} \rightarrow N c_{1}$ |
|  | 3 | $\left(n_{12}, n_{13}\right)$ | $L_{12,57}=L_{57,13}$ |  | $E v_{3}$ to $A c_{1}:$ |
|  | 4 | $\left(n_{18}, n_{17}\right)$ | $L_{18,58}=L_{58,17}$ |  | $N v_{4} \rightarrow n_{17} \rightarrow n_{18} \rightarrow n_{8} \rightarrow N c_{2}$ |
|  | 5 | $\left(n_{15}, n_{29}\right)$ | $L_{15,59}=L_{59,29}$ |  | $E v_{8}$ to $A c_{2}:$ |
|  | 6 | $\left(n_{39}, n_{25}\right)$ | $L_{39,60}=L_{60,25}$ |  | $N v_{8} \rightarrow n_{32} \rightarrow n_{18} \rightarrow n_{8} \rightarrow N c_{2}$ |
|  | 7 | $\left(n_{30}, n_{31}\right)$ | $L_{30,61}=L_{61,31}$ |  | $E v_{3}$ to $A c_{3}:$ |
|  | 8 | $\left(n_{35}, n_{32}\right)$ | $L_{35,62}=L_{62,32}$ |  | $N v_{6} \rightarrow n_{25} \rightarrow n_{26} \rightarrow n_{27} \rightarrow N c_{3}$ |
| 9:35 | 1 | $\left(n_{2}, n_{3}\right)$ | $L_{2,55}=L_{55,3}$ | $1,4,3,2,0,3,0,2$ | $E v_{1}$ to $A c_{1}:$ |
|  | 2 | $\left(n_{8}, n_{9}\right)$ | $L_{8,56}=0.12 \times L_{8,9}$ |  | $N v_{1} \rightarrow n_{3} \rightarrow n_{2} \rightarrow n_{10} \rightarrow n_{21} \rightarrow N c_{1}$ |
|  |  |  | $L_{36,9}=0.88 \times L_{8,9}$ |  | $E v_{4}$ to $A c_{1}:$ |
|  | 3 | $\left(n_{12}, n_{13}\right)$ | $L_{12,57}=0.77 \times L_{12,13}$ |  | $N v_{1} \rightarrow n_{3} \rightarrow n_{2} \rightarrow n_{10} \rightarrow n_{21} \rightarrow N c_{1}$ |
|  |  |  | $L_{57,13}=0.23 \times L_{12,13}$ |  | $E v_{4}$ to $A c_{2}: N v_{4} \rightarrow n_{6} \rightarrow N c_{2}$ |
|  | 4 | $\left(n_{18}, n_{6}\right)$ | $L_{18,58}=0.10 \times L_{18,6}$ |  | $E v_{8}$ to $A c_{2}: N v_{8} \rightarrow n_{18} \rightarrow n_{6} \rightarrow N c_{2}$ |
|  |  |  | $L_{58,6}=0.90 \times L_{18,6}$ |  | $E v_{3}$ to $A c_{3}: N v_{3} \rightarrow n_{13} \rightarrow n_{14} \rightarrow N c_{3}$ |
|  | 5 | $\left(n_{15}, n_{29}\right)$ | $L_{15,59}=L_{59,29}$ |  | $E v_{6}$ to $A c_{3}:$ |
|  | 6 | $n_{25}$ | $n_{25}$ |  | $N v_{6} \rightarrow n_{25} \rightarrow n_{26} \rightarrow n_{27} \rightarrow N c_{3}$ |
|  | 7 | $\left(n_{30}, n_{31}\right)$ | $L_{30,61}=L_{61,31}$ |  | $E v_{2}$ to $A c_{4}: N v_{2} \rightarrow n_{9} \rightarrow N c_{4}$ |
|  | 8 | $\left(n_{32}, n_{18}\right)$ | $\begin{gathered} L_{32,62}= \\ 0.16 \times L_{32,18} \\ L_{62,18}= \\ 0.84 \times L_{32,18} \end{gathered}$ |  |  |

$t_{\max }^{\mathrm{u}}\left(t_{\varphi}\right): \quad$| The latest rescue time of the accident |
| :--: |
| $A c_{u}\left(t_{\varphi}\right)$ |
| $x x_{l}\left(t_{\varphi}\right):$ | The decision variable; at the decision-making instant $t_{\varphi}$, if the emergency vehicle $E v_{l}, l=1,2, \ldots, L$ is in the idle state, then $x x_{l}\left(t_{\varphi}\right)=1$; otherwise, $x x_{l}\left(t_{\varphi}\right)=0$ |
| $T_{i, l+1}\left(t_{i}\right)_{t_{\varphi}}:$ | The link travel time function at the decision-making instant $t_{\varphi}$. It represents a time for the emergency vehicle, leaving at an instant $t_{i}$, from node $n_{i}$ to $n_{i+1}$ |
| $H:$ | The total number of frogs |
| IP: | The frog population |
| $X_{h}=\left[x_{h 1}, x_{h 2}\right.$ | The position of the $h$ th frog |
| $\left.\ldots, x_{h d}, \ldots, x_{h D}\right]$, |  |
| $h=1, \ldots, H:$ |  |
| $D:$ | The dimension of the optimization problem |
| $f:$ | The performance function of the optimization problem |
| $P x=\left[p x_{1}, p x_{2}\right.$ | The position of the optimal frog in the |
| $\ldots, p x_{d}, \ldots, p x_{D}\}$ | population IP |
| $a$ : | The total number of memeplexes |
| $c:$ | The total number of frogs in each memeplex |
| It: | The total number of iterations within each memeplex |

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

## References

[1] T. Yamada, "A network flow approach to a city emergency evacuation planning," International Journal of Systems Science, vol. 27, no. 10, pp. 931-936, 1996.
[2] G. M. Carter, J. M. Chaiken, and E. Ignall, "Response areas for two emergency units," Operations Research, vol. 20, pp. 571-594, 1972.
[3] H. D. Sherali and S. Subramanian, "Opportunity cost-based models for traffic incident response problems," Journal of Transportation Engineering, vol. 125, no. 3, pp. 176-185, 1999.
[4] K. Ozbay, C. Iyigun, M. Baykal-Gursoy, and W. Xiao, "Probabilistic programming models for traffic incident management operations planning," Annals of Operations Research, pp. 1-18, 2012.
[5] X. Song, J. Wang, and C. Chang, "Nonlinear continuous consumption emergency material dispatching problem," Systems Engineering, vol. 32, no. 2, pp. 163-176, 2017.
[6] W. Tang, L. Zou, and Q. Guo, "Grey multi-objective programming for materials dispatching from multiple supply points to multiple demand points," Open Journal of Safety Science and Technology, vol. 12, no. 11, pp. 148-152, 2016.
[7] J. Liu and K. Xie, "Emergency materials transportation model in disasters based on dynamic programming and ant colony optimization," Kybernetes, vol. 46, no. 4, pp. 656-671, 2017.
[8] X.-H. Li and Q.-M. Tan, "Particle swarm optimization algorithm for emergency resources dispatch scheduling," Recent Patents on Mechanical Engineering, vol. 7, no. 3, pp. 237-240, 2014.
[9] J. Liu, L. Guo, and J. Jiang, "Emergency material allocation and scheduling for the application to chemical contingency spills under multiple scenarios," Environmental Science Pollution Research, vol. 24, no. 1, p. 13, 2017.
[10] K. G. Zografos, K. N. Androutsopoulos, and G. M. Vasilakis, "A real-time decision support system for roadway network incident response logistics," Transportation Research Part C: Emerging Technologies, vol. 10, no. 1, pp. 1-18, 2002.
[11] A. Haghani, Q. Tian, and H. Hu, "Simulation model for realtime emergency vehicle dispatching and routing," Transportation Research Record: Journal of the Transportation Research Board, vol. 1882, pp. 176-183, 2004.
[12] B. Dan, W. Zhu, H. Li, Y. Sang, and Y. Liu, "Dynamic optimization model and algorithm design for emergency materials dispatch," Mathematical Problems in Engineering, vol. 2013, Article ID 841458, 2013.
[13] S. Yang, M. Hamedi, and A. Haghani, "Online dispatching and routing model for emergency vehicles with area coverage constraints," Transportation Research Record, no. 1923, pp. 1-8, 2005.
[14] B. Fu, D. G. Li, and M. K. Wang, "Review and prospect on research of cloud model," Application Research of Computers, vol. 28, no. 2, pp. 420-426, 2011.
[15] K. L. Cooke and E. Halsey, "The shortest route through a network with time-dependent internodal transit times," Journal of Mathematical Analysis and Applications, vol. 14, pp. 493-498, 1966.
[16] D. E. Kaufman and R. L. Smith, "Minimum travel time paths in dynamic networks with application to intelligent vehicle/highway systems," IVHS Journal, vol. 1, no. 1, pp. 1-19, 1993.
[17] M. Setak, M. Habibi, H. Karimi, and M. Abedzadeh, "A timedependent vehicle routing problem in multigraph with FIFO property," Journal of Manufacturing Systems, vol. 35, pp. 37-45, 2015.
[18] X.-H. Duan, J.-D. Zhao, and S.-X. Song, "Dynamic shortest paths of emergency vehicles in expressway network based on shuffled frog leaping algorithm," Journal of Transportation Systems Engineering and Information Technology, vol. 16, no. 3, pp. 181-186, 2016.
[19] S. Ichoua, M. Gendreau, and J. Potvin, "Vehicle dispatching with time-dependent travel times," European Journal of Operational Research, vol. 144, no. 2, pp. 379-396, 2003.
[20] Y. Yuan and D. Wang, "Path selection model and algorithm for emergency logistics management," Computers \& Industrial Engineering, vol. 56, no. 3, pp. 1081-1094, 2009.
[21] Y. Zhou, J. Liu, Y. Zhang, and X. Gan, "A multi-objective evolutionary algorithm for multi-period dynamic emergency resource scheduling problems," Transportation Research Part E: Logistics and Transportation Review, vol. 99, pp. 77-95, 2017.
[22] Y. Zhou and J. Liu, "A multi-agent genetic algorithm for multiperiod emergency resource scheduling problems in uncertain traffic network," in Proceedings of the 2017 IEEE Congress on Evolutionary Computation, CEC 2017, pp. 43-50, Spain, June 2017.
[23] M. M. Eusuff and K. E. Lansey, "Optimization of water distribution network design using the shuffled frog leaping algorithm," Journal of Water Resources Planning and Management, vol. 129, no. 3, pp. 210-225, 2003.
[24] M. Eusuff, K. Lansey, and F. Pasha, "Shuffled frog-leaping algorithm: a memetic meta-heuristic for discrete optimization," Engineering Optimization, vol. 38, no. 2, pp. 129-154, 2006.
[25] H. Amirian and R. Sahraeian, "Solving a grey project selection scheduling using a simulated shuffled frog leaping algorithm," Computers \& Industrial Engineering, vol. 107, pp. 141-149, 2017.
[26] D. Lei and X. Guo, "A shuffled frog-leaping algorithm for job shop scheduling with outsourcing options," International Journal of Production Research, vol. 54, no. 16, pp. 4793-4804, 2016.
[27] D. Lei, Y. Zheng, and X. Guo, "A shuffled frog-leaping algorithm for flexible job shop scheduling with the consideration of energy consumption," International Journal of Production Research, vol. 55, no. 11, pp. 3126-3140, 2016.
[28] D. Lei and X. Guo, "A shuffled frog-leaping algorithm for hybrid flow shop scheduling with two agents," Expert Systems with Applications, vol. 42, no. 23, pp. 9333-9339, 2015.
[29] B. Ning, Q. Gu, and Y. Wang, "Research based on effective resource allocation of improved SFLA in cloud computing," International Journal of Grid and Distributed Computing, vol. 9, no. 3, pp. 191-198, 2016.

[30] X. Duan, S. Song, and J. Zhao, "Emergency vehicle dispatching and redistribution in highway network based on bilevel programming," Mathematical Problems in Engineering, vol. 2015, Article ID 731492, pp. 1-12, 2015.
[31] T. Xu, Study on Dynamic Prediction of Road Operating Speed Based on Floating Car Data, Chongqing Jiaotong University, 2017.
[32] J. Weng, J. Rong, F. Ren et al., "Non-parametric regression model based short-term prediction for expressway travel speed," Journal of Highway Transportation Research and Development, vol. 24, no. 3, pp. 93-97, 2007.

![img-19.jpeg](img-19.jpeg)

Advances in Operations Research
![img-20.jpeg](img-20.jpeg)

International Journal of Engineering Mathematics
![img-21.jpeg](img-21.jpeg)

International Journal of Engineering Mathematics
![img-22.jpeg](img-22.jpeg)

Journal of Complex Analysis
![img-23.jpeg](img-23.jpeg)

International Journal of Stochastic Analysis
![img-24.jpeg](img-24.jpeg)

The Scientific World Journal
![img-25.jpeg](img-25.jpeg)

Hindawi
Submit your manuscripts at www.hindawi.com
![img-26.jpeg](img-26.jpeg)

Mathematical Problems in Engineering
![img-27.jpeg](img-27.jpeg)

International Journal of Differential Equations
![img-28.jpeg](img-28.jpeg)

Abstract and Applied Analysis
![img-29.jpeg](img-29.jpeg)

Journal of Probability and Statistics
![img-30.jpeg](img-30.jpeg)

Journal of Optimization
![img-31.jpeg](img-31.jpeg)

International Journal of Analysis
![img-32.jpeg](img-32.jpeg)

Discrete Dynamics in Nature and Society
![img-33.jpeg](img-33.jpeg)