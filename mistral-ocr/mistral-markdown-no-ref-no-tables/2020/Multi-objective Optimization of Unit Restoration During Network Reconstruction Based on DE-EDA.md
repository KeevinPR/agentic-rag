# Multi-objective Optimization of Unit Restoration During Network Reconstruction Based on DE-EDA 

Tao Wang<br>State Grid Weifang Power Supply Company<br>Weifang, China<br>e-mail: 987993623@qq.com<br>Zhonggang Wang<br>State Grid Weifang Power Supply Company<br>Weifang, China<br>e-mail: yhdong@sdu.edu.cn<br>Na Sun<br>State Grid Gaomi Power Supply Company<br>Weifang, China<br>e-mail: 2530651186@qq.com

Hainan Zhu<br>State Grid Weifang Power Supply Company<br>Weifang, China<br>e-mail: 649615315@qq.com<br>Yijie Wang<br>State Grid Weifang Power Supply Company<br>Weifang, China<br>e-mail: 201834322@sdu.edu.cn<br>Yunhui Dong<br>School of electrical engineering<br>Shandong University<br>Jinan, China<br>e-mail: 724444034@qq.com


#### Abstract

The restoration of unit is the basis of the whole power system restoration. The start-up sequence of units has an influence on both the target network reconstruction whose goal nodes are units which are selected to supply with cranking power and the total power generation capability over a restoration period during network reconstruction. This paper provides a multi-objective optimization model of unit restoration of which optimization goals are to minimize the restoration cost of the target network and to maximize the total power generation capability. The weight of lines is dynamically set to extent the search space for avoiding the loss of the optimal solution when the target network is reconstructed. The model is solved by differential evolution and estimation of distribution algorithm (DE-EDA). Simulation results on IEEE 30-loss system show that the proposed optimization model and algorithm are able to find the solutions which have better convergence and are better spread; the effectiveness of the proposed optimization model and algorithm is further validated by the simulation result on Shandong west power grid of China.


Keywords-unit restoration; network reconstruction; multiobjective optimization; DE-EDA

## I. INTRODUCTION

The whole power system restoration after major blackout can be divided into three stages: black start, network reconstruction and load recovery[1-6].The optimization goal of network reconstruction stage is to optimize the recovery path to send power to the target node at the least cost[7-8]. Except for extremely important load nodes, the target nodes are generally the unit nodes to be restored first, and then the load nodes. Therefore, network reconstruction stage can be
divided into two parts-network reconstruction with the units to be restored as the target whose optimization target is to provide maximum amount of power generation and the network reconstruction with the load nodes as the target[911]. Since the target nodes recovery sequence will affect the selection of different recovery path[12], and therefore a different order to restore the unit will not only affect the optimization target of unit restoration, but also the network selection with the units to be restored as the target. Therefore, in order to obtain a better recovery solution, it is necessary to combine the optimization of the unit recovery sequence and the optimization of the network reconstruction with the units to be restored as the target node.

Recently, a lot of research has done on the optimization of unit recovery sequence and network reconstruction. Reference [13] analyzes the various factors which determine the unit recovery sequence during the power system restoration process; Reference [9] uses a mixed integer programming method to solve the unit recovery sequencing problem; And in reference [10], the maximum power generation of the system within a certain period of time during the unit recovery process is taken as the optimization goal, and the classic backtracking algorithm is used to solve the "knapsack problem". Above research optimizes the recovery sequence of the unit, without considering the optimization of the corresponding network frame reconstruction. Reference [3] decouples network reconstruction optimization from target node optimization, and studies only on network reconstruction optimization; Reference [14] considers the uncertainty of operation time, and reconstructs the network with the maximum benefit as the goal. References $[8,12]$ comprehensively consider network reconstruction optimization and target node

sequence optimization, but only consider the time limit of the unit start-up without considering factors such as the climb rate and start-up power of the unit.

In this paper, the unit recovery sequence optimization and the network reconstruction optimization with the unit to be restored as the target node are comprehensively considered. A multi-objective optimization model of unit restoration during network reconstruction is established. The optimization goals are set to maximize the total power generation capability and to minimize the restoration cost of the target network. In this paper, a differential evolution and estimation of distribution algorithm (DE-EDA) is used to solve the multi-objective optimization problem, and a Pareto optimal scheme of unit recovery sequence and network reconstruction is proposed.

## II. Mathematical Model

## A. Objective Function

According to graph theory, the network whose target nodes are the units to be restored is a minimum spanning tree of a graph with black start power and the units to be restored as the vertex [3].In order to minimize the cost of the target network restoration, it can be optimized in two aspects: Firstly, minimize the restoration weight of the entire spanning tree, which will be discussed in section II-B; Secondly, minimize the number of lines in the spanning tree, that is, reduce the amount of the line recovery operations.

Suppose that there are $n$ units to be restored, according to the definition of the minimum tree, all the lines in the target network belong to the restoration paths of the $n$ units, so the restoration weight of the target network is the sum of the weight of the n restoration paths. Let $f_{1}$ be the recovery weight of the target network, and the optimization target be $\min \left(f_{1}\right)$, that is,

$$
\min \left(f_{1}\right)=\min \left(\sum_{i=1}^{n} W_{i}\right)
$$

Where $W_{i}$ means the restoration weight of the recovery path $i$ in the units to be restored.

Let $f_{2}$ be the amount of lines included in the target network, then the optimization goal should be $\min \left(f_{2}\right)$, and

$$
\min \left(f_{2}\right)=\min (k)
$$

Where $k$ represents the number of the lines in the whole target network.

Let $f_{3}$ be the amount of power that can be provided by all the units to be restored, that is, the benefits during the restoration process, and the optimization goal be $\max \left(f_{3}\right)$. For the convenience of solving, $f_{3}$ is negated, then the optimization goal will be $\min \left(f_{3}\right)$, that is,

$$
\min \left(f_{3}\right)=\min \left[-\sum_{i=1}^{n} \int_{0}^{T} P_{i}(t) d t\right]
$$

Where $T$ represents the whole time of restoration process, and $P_{i}(t)$ represents the contribution power function of unit
$i$ in the units to be restored.
In summary, there are three optimization goals considered in this paper: 1) The overall restoration weight $f_{1}$ of the network with the units to be restored as the target node should be minimum value; 2) The number of lines $f_{2}$ included in the target network should be minimum value; 3) The amount of power generation $f_{3}$ of all units to be restored during the restoration process should be maximum value (the reverse of $f_{3}$ should be minimum value); That is

$$
\min \left(f_{1}, f_{2}, f_{3}\right)
$$

Restrictions:

1) Time restriction[10]:

Suppose that the time it takes for unit $i$ from power-off to obtaining starting power is $t_{i 1}$, and the critical time for hot start is $T_{H S, i}$ then unit $i$ can get hot start when $t_{i 1}$ satisfies equation(5),

$$
0<t_{i 1}<T_{H S, i}
$$

When $t_{i 1}$ couldn't satisfy equation (5) and unit $i$ has minimum cold start time limit $T_{C S, i}$ unit $i$ can get started when $t_{i 1}$ satisfies equation (6), and the start time will be much longer than hot start time.

$$
t_{i 1}>T_{C S, i}
$$

2) Starting power restriction:

$$
\sum P_{t i}\left(t_{0}\right)-\sum P_{c i}\left(t_{0}\right) \geq 0
$$

Where $\sum P_{t i}\left(t_{0}\right)$ is the available power to guarantee safe operation for the already restored system and $\sum P_{c i}\left(t_{0}\right)$ is the auxiliary power of unit $i$ at current time $t_{0}$.
3) Power flow restriction: Every time the auxiliary machine or the line is restored, a steady-state power flow check should be performed to ensure that the generator output does not exceed limit with reserved power, the voltage of each node is within the allowable range, and the power flow of each branch does not exceed limit [8].
4) Auxiliary power start restriction:

$$
P_{i \max }^{\prime} \leq P_{i \max }
$$

Where $P_{i \max }^{\prime}$ is the maximum auxiliary machine capacity of unit $i, P_{i \max }$ is the maximum allowable single-time input motor capacity of the node where unit $i$ is located under the conditions of transient voltage safety and frequency safety [15].

## B. Line Restoration Weight

During network reconstruction, no-load charging operation is needed on the line, which may cause overvoltage and generator self-excitation[16]. Over-voltage is mainly created by the reactive power imbalance caused by the line-to-ground capacitance[3, 16]; Generator selfexcitation is caused by the positive feedback generated by the magnetizing effect of the charging capacitive current[17]. The line-to-ground capacitance is the main cause of the

above problems, so the restoration weight of line $j$, that is $w_{j}$, is set to

$$
w_{j}=B_{j} \frac{\varepsilon_{j}}{X_{\mathrm{i}, j}}
$$

where $B_{j}$ represents the ground susceptance of line $j ; X_{i, j}$ represents the parallel reactance of line $j ; \varepsilon_{j}$ is 1 or 0 depends on whether there is a parallel reactance on line $j$ or not. The parallel reactance of the line is taken into the definition of the line restoration weight, which can more accurately reflect the over-voltage and self-excitation problems that may be caused when the line is charged without load.

Suppose that there are $m$ lines in the recovery path of the unit $i$ to be restored, and the weight of this path is set to

$$
W_{i}=k_{i} k_{r} \sum_{j=1}^{m} w_{j}
$$

where $k_{i}$ is the influence factor of the number of voltage conversions in the current recovery path, and $k_{2}$ is a coefficient related to the recovery order of the current unit and the order of the recovery weights of its recovery paths in the recovery paths of all the units. The physical meaning of $k_{2}$ is that the recovery path of the units who have earlier recovery order should have a smaller recovery weight to increase the success rate of the unit recovering.

Suppose the number of voltage transitions in the recovery path of unit i to be restored is $h$, then $k_{1}$ can be seen as a function of $k_{1}$ as the independent variable:

$$
k_{1}= \begin{cases}\frac{h}{h_{\mathrm{i}}}, & h \leq h_{\mathrm{i}} \\ h, & h>h_{\mathrm{i}}\end{cases}
$$

where $h_{\mathrm{i}}$ is the maximum acceptable number of voltage conversions, which can be set according to the actual situation of the network[18].
$k_{2}$ is actually a penalty factor introduced to ensure that the recovery order of the units is consistent with the order of the recovery weights of their recovery paths, which can ensure that the recovery paths of the earlier recovery order units have smaller recovery weights and that the success rate of the unit recovering can be increased. Although the recovery weights of the recovery paths of recovery units who have later recovery order is relatively large, the system capacity and anti-disturbance are enhanced as the previous units continue to recover, which also increases the probability of subsequent units to successfully recover. For example, the recovery order of one unit is $m$. When the ascending order of the recovery weights of the recovery paths among all the recovery paths is $m$, the value of $k_{2}$ is 1 . When the order of the recovery weights is not equal to m , $k_{2}$ takes a value greater than 1 . The specific calculation formula of $k_{2}$ is as follows

$$
k_{2}= \begin{cases}1+\frac{|r-1|}{n}, \text { the first unit in the recovery path } \\ 1+\frac{\left|r_{\mathrm{i}}-r_{2}\right|}{n}, \text { the rest units in the recovery path }\end{cases}
$$

where $n$ is the quantity of all the units to be restored.For the first unit to be restored, search for the restoration paths corresponding to all units as the first to be restored and calculate their restoration weights, and then arrange the restoration weights in ascending order to obtain the order r of the restoration weights of the current unit; For the remaining units, when the first unit is determined, search for their corresponding restoration paths and calculate their restoration weights, and arrange the restoration weights in ascending order. $r_{\mathrm{i}}$ will be the order of the current unit's restoration path weights, and $r_{2}$ will be the sequence of the current unit in all the units to be restored.

## C. Line Restoration Time

The line restoration time refers to the time it takes to charge the bus bar at the end of the line through closing operation from the charging the bus bar at the beginning of the line. This paper uses the method for determining the line restoration time as described in [19].

## III. TARGET NETWORK SEARCH

Different recovery order of the units to be restored will lead to different target network [12]. When the unit recovery order is given, many studies use the classic Dijkstra algorithm to search for the target network [8, 12, 20], where the key step is the selection of line weights. However, the line has multiple attributes to choose from, such as the restoration weight of the line, the restoration time of the line, and the connection relationship of the lines(the network topology relationship), etc.. Generally, it is hard to search the entire feasible region using one or a combination of the two as the weight and to obtain the optimal solution in the entire feasible region. Figure 1 shows a simple example.
![img-0.jpeg](img-0.jpeg)

Figure 1. Four-node case for path finding

## IV. SIMULATION ANALYSIS

A multi-objective optimization program for unit restoration based on the DE-EDA at network reconstruction stage was compiled using Matlab, and simulation calculations were performed on the modified IEEE 30-node system and the actual system of the western Shandong power grid. Some results are as follows.

![img-1.jpeg](img-1.jpeg)

Figure 3. IEEE 30-bus system structure diagram

## A. Example of IEEE 30-node System

The modified IEEE 30-node system example includes 7 generators and 41 lines, shown in Fig.3. The weight value marked on the line in the figure represents the restoration time of the line (unit: min). Assume that the node 1 unit in Fig. 3 is a black start power supply. The node 3 unit has been successfully recovered by the black start unit during the black start stage. The remaining units on nodes $2,13,22,23$, and 27 are to be restored during the network reconstruction stage. The hot start time of the node 27 unit is set to 10 minutes, and if hot start cannot be performed, it is necessary to wait for 1 hour to perform cold start. The hot start time of the remaining units are set to 30 minutes. Set h1 to $3[18,25]$, when calculating the restoration weights of the recovery path. According to the number of units to be restored, the individual dimension is set to 6 , and the remaining parameters of DE-EDA are shown in Table 1.

TABLE I. PARAMETER SETTINGS OF DE-EDA

In order to compare the effectiveness of DE-EDA, the NSGA-II algorithm [8] is used to solve the optimization model under the same calculation conditions. The cross probability of NSGA-II algorithm is set to 0.9 and the mutation rate is 0.2 . Multi-objective optimization is respected not only to converge to the Pareto optimal solution, but also to ensure that the solution is evenly distributed on the Pareto front. The GD indicator and SP indicator [26] are used to compare the advantages and disadvantages of these two algorithms. The GD index reflects the convergence of the algorithm. The smaller the GD index is, the closer the solution set is to the Pareto optimal solution. The SP index can reflect the distribution of the optimal solution. The smaller the SP index is, the more uniform the distribution of the solution set is.Table 2 shows the GD index and SP index obtained by each of the two algorithms after 50 independent calculations. It can be seen from Table 2 that the GD index and SP index of DE-EDA are better than NSGA-II algorithm.

TABLE II. MERICs OF DE-EDA AND NSGA-II


Table 3 shows the partial Pareto optimal solution and the corresponding objective function values that passed the elite check. The column of the network solution in the table represents that when Dijkstra is used to search for the target grid, the line weights use different values. Network scheme 1 represents $V_{n+1} \in(0,1 / 3]$, and the line weight is assigned to the restoration weight; Network scheme 2 represents $V_{n+1} \in(1 / 3,2 / 3]$, and the line weight is assigned to the restoration time; Network frame scheme 3 represents $V_{n+1} \in(2 / 3,1)$, and the line assignment is the network topology relationship.

TABLE III. OPTIMIZATION SEQUENCE OF GENERATING UNITS RESTORATION AND SYSTEM RECONSTRUCTION OF IEEE30-bUS SYSTEM

When the optimization goal is set to a single goal $[9,10]$, that is the largest amount of power generation can be provided during the recovery process, scheme 1 in Table 3 is obtained. Compared with the other two kinds of scheme, the three objective functions of scheme 1 are non-dominated, and all belong to the Pareto optimal solution. Using the multi-objective optimization model, multiple Pareto optimal solutions in the solution space can be obtained. Decision makers can choose corresponding restoration schemes according to different preferences, and the rest can be used as backup restoration schemes. In addition, the obtained multiple Pareto optimal schemes also provide multiple options for dispatcher training [27].

## V. CONCLUSION

This paper proposes a multi-objective optimization model for unit restoration during the network restoration. The optimization goal is to minimize the overall restoration weight of the network with the unit to be restored as the target node, to minimize the amount of lines in the target network, and to provide maximum power generation. At the same time, multiple constraints such as the safe start of the auxiliary machine are considered. The hybrid intelligent optimization algorithm DE-EDA is used to solve the multiobjective optimization model. DE-EDA uses the global search performance of EDA and the local optimization ability of DE algorithm to obtain better optimization results. The IEEE 30-node simulation results show that compared with the NSGA-II algorithm, the optimal solution obtained by DE-EDA has better convergence and distribution. The

simulation of the actual system of western Shandong power grid shows that the model and algorithm proposed in this paper is effective in practical systems, and multiple Pareto optimal solutions can be obtained, which provides more choices for operation decision-makers
