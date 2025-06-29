# A Histogram Estimation of Distribution Algorithm for Reversible Lanes Optimization Problems 

Rui You<br>School of Computer Science and Engineering, South China University of Technology<br>Guangzhou

Wei-Neng Chen<br>School of Computer Science and Engineering, South China University of Technology<br>Guangzhou<br>cwnraul634@aliyun.com<br>Yue-Jiao Gong<br>School of Computer Science and Engineering, South China University of Technology<br>Guangzhou

Ying Lin
Department of Psychology, Sen Yat-sen University
Guangzhou

Jun Zhang
School of Computer Science and
Engineering, South China University of
Technology
Guangzhou

[^0]Yue-Jiao Gong
School of Computer Science and Engineering, South China University of Technology Guangzhou

Abstract-The Reversible lanes optimization problem (RLOP) is a complex optimization problem in traffic management. The objective of this problem is to find an optimal direction assignment of lanes in an urban traffic network, so that the traffic capacity of urban streets could get the utmost promotion. To solve this problem efficiently, we particularly devise a histogram-based estimation of distribution algorithm (HEDA) in this paper. Specifically, during the estimation of the distribution, this algorithm considers different individuals differently based on their contributions. Besides, HEDA also combines both the current and historical population distribution information to generate offspring. Experiments conducted on ten different traffic network instances substantiate that HEDA achieves better performance than the compared method on most instances, especially on large-scale network instances.

Keywords-Estimation of distribution algorithms (EDA), reversible lanes optimization problems, transportation management

## I. INTRODUCTION

Traffic congestion is a very serious urban management problem to be solved in most metropolitan areas. The main causes of this issue are the increasing number of vehicles and limited carrying capacity of the road networks.

To solve this problem, many approaches have been attempted. For example, in the very early time, urban planners came up with very intuitive yet effective solutions [1, 2], such as building more roads and widening existing roads. But in reality, most regions do not support large-scale land acquisition and demolition to construct or expand roads. As a consequence, the planners have to make full use of junctions between roads. To improve the capacities of junctions, intelligent traffic signal control systems [3] have emerged. Based on the massive real-time traffic data, the system discovers the traffic state and optimizes the traffic signal scheme automatically. However, traffic signal control systems could only relieve traffic congestion in junctions and do not help to solve the congestion problem among roads. To take full advantage of the road sections between junctions, the reversible lanes optimization system was proposed [4-6].

In a reversible roadway, the traffic directions of some

[^1]lanes could be reversed based on the change of traffic flows [5]. For example, in large metropolitan areas, the traffic flows in the morning and evening commuter periods vary greatly. To be specific, in the morning rush hour, most traffic demands are driving from residential areas to office areas. While in the evening peak time, the situation is totally reversed. For many backbone networks, the spatio-temporal nature of this traffic leads to imbalanced traffic flows. These imbalanced traffic flows have resulted in a serious waste of resources as well as traffic congestions. In view of this problem, reversible lanes optimization is to increase the number of lanes to meet the major traffic flow by reversing the directions of lanes originally meeting the other traffic flow without constructing additional roads [5].

In general, the RLOP is to find an optimal direction assignment of lanes in an urban traffic network to improve the traffic capacity of urban streets. It is common that such a problem contains a large number of decision variables due to the huge traffic road network. Additionally, the RLOP is essentially a combinatorial optimization problem in network design, which has been proved to be NP-hard [7]. Many evolutionary algorithms (EAs) [8-12] have been proposed to solve this kind of NP-hard problems. Due to the above properties, RLOP is usually a very challenging optimization problem.

In the literature, researchers usually modeled the RLOP as a bi-level optimization problem, where two optimization problems exist and one problem is nested in the other [13]. Particularly, in the RLOP, the objective in the lower level is to solve the user equilibrium (UE) assignment problem, while the target in the upper level is often related to the system optimum (SO) and has different forms for different purposes. Between the two optimization problems, the user equilibrium flows solved in the lower level generally act as input variables of the problem in the upper level.

Previously, a few studies have attempted to solve RLOP. Specifically, the UE assignment problem in the lower level is usually solved by the Frank-Wolfe (FW) algorithm [14], which is a popular constrained convex optimization method. As for the optimization problem in the upper level, Wu et al. [6] combined an advanced traveler information system (ATIS) with a traditional bi-level optimization model to solve RLOP. In this approach, ATIS was used to provide travelers with navigational assistance in their unfamiliar area, so that better decisions could be made. Zhang and Gao


[^0]:    Forced-Die Reversible lanes optimization problem (RLOP) is a complex optimization problem in traffic management. The objective of this problem is to find an optimal direction assignment of lanes in an urban traffic network, so that the traffic capacity of urban streets could get the utmost promotion. To solve this problem efficiently, we particularly devise a histogram-based estimation of distribution algorithm (HEDA) in this paper. Specifically, during the estimation of the distribution, this algorithm considers different individuals differently based on their contributions. Besides, HEDA also combines both the current and historical population distribution information to generate offspring. Experiments conducted on ten different traffic network instances substantiate that HEDA achieves better performance than the compared method on most instances, especially on large-scale network instances.

    Keywords-Estimation of distribution algorithms (EDA), reversible lanes optimization problems, transportation management

[^1]:    This work was supported in part by the National Natural Science Foundation of China under Grant 61622206, Grant 61332002, and Grant 61876111, in part by the Natural Science Foundation of Guangdong under Grant 2015A030306024, and in part by the Science and Technology Plan Project of Guangdong Province under Grant 2018B050502006. Corresponding author: Wei-Neng Chen (cwnraul634@aliyun.com)

[15] proposed a heuristic approach based on a discrete particle swarm optimization (DPSO) technique to reallocate reversible lanes in the road network. In this approach, the ATIS was also adopted to solve the UE assignment problem in the lower level. However, with the increase of the network scale, the complexity of the bi-level optimization problem increases dramatically, which may easily lead to the premature convergence of PSO. To alleviate this concern, we propose a histogram estimation of distribution algorithm to solve the RLOP in this paper.

Particularly, estimation of distribution algorithms (EDAs) [16-19] are a kind of stochastic optimization algorithms in the field of evolutionary computation (EC) [20]. Instead of adopting selection, mutation and crossover operators in other EAs [21-24], an EDA generates offspring via a probability distribution model, which is estimated from the current population. Benefiting from such an offspring generation strategy, EDAs could maintain the population diversity at the population level and thus have a small probability to fall into local areas. Due to this advantage, EDAs have been widely utilized to solve many complicated optimization problems [25, 26] including NP-hard optimization problems [27-30].

Taking the above advantage of EDAs, we propose a histogram estimation of distribution algorithm (HEDA) to solve RLOP in this paper. Specifically, we use frequency distribution histogram to estimate the distribution of optimal solution. For every variable, an independent histogram is built in every iteration. From such a statistic model, HEDA could easily estimate the true optima distributions.

To verify the effectiveness and efficiency of the proposed HEDA, we conduct experiments on 10 different traffic network instances via comparing with another metaheuristic method.

The remainder of this paper is organized as follows. In section II, the preliminary of RLOP is introduced. Section III elucidates the proposed HEDA in detail. In Section IV, experiments are conducted to demonstrate the performance of HEDA. At last, in Section V, we conclude this paper and provide some further research considerations.

## II. REVERSIBLE LANES OPTIMIZATION PROBLEM

In this section, the brief introduction of RLOP is presented. Fig. 1 shows the direction settings of lanes in a two-way roadway under a symmetric flow. Specifically, the flow from node $i$ to node $j$ is almost the same as that from node $j$ to node $i$. In this case, the number of lanes from $i$ to $j$ is equals to that from $j$ to $i$ and all equal to 2 as the Fig. 1 shows. However, in most cases, the road traffic flows are highly different and thus asymmetric due to different daily
![img-0.jpeg](img-0.jpeg)

Fig. 1 The direction settings of lanes in reversible roadways between node $i$ and node $j$ under symmetric flow distributions
commute peaks. In this paper, we assume all roadways in the specific road network are reversible. As a result, the number of decision variables in RLOP is the number of lanes in the entire road network.

## A. Model Definition

Consider a traffic network $G=(V, E)$, which contains a node set $V$ and a directed road edge set $E$. Because of the nature of traffic network, each road edge consists of a pair of roadways with two opposite directions and each roadway has several lanes. We use a set $A$ to denote all these roadways. Obviously, the size of $A$ is the twice as the size of the set $E$. Fig. 2. shows a simple network with 6 nodes and 16 roadways. In simple terms, how many lanes are arranged on a roadway is the problem we want to optimize.
![img-1.jpeg](img-1.jpeg)

Fig. 2 An example traffic network with 6 nodes and 16 roadways
Each roadway is denoted by four parameters $\left\{a, t_{a}^{0}, K_{a}, n_{a}\right\}$, where $a$ denotes the index of roadway in set $A, t_{a}^{0}$ is the free-flow of roadway $a$, which represents the travel time cost when the actual traffic flow equals to zero. $K_{a}$ is the unit traffic capacity of a single lane on roadway $a$, which is used to measure the traffic capacity. These two parameters are directly related to road quality, and the values vary from road to road. $n_{a}$ is the number of lanes on roadway $a$. In fact, the roadways always appear in pairs, for specific roadway $a$ there must exist a reverse direction roadway $a^{\prime}$. Usually $a^{\prime}$ and $a$ have the same freetime and unit traffic capacity. Eq. (1) shows the summation of $n_{a}$ and $n_{a^{\prime}}$ is a fixed value $N_{a a^{\prime}}$, where $N_{a a^{\prime}}$ denotes the maximum number of lanes on two-way roads $a$ and $a^{\prime}$. Since in RLOP model the road cannot be widened, the total number of lanes in one pair of two-way roads is fixed. Besides, in reality, the number of lanes must be integers. Thus, the number of roadway $a$ and $a^{\prime}$ could only take integers from 0 to $N_{a a^{\prime}}$. In particular, when $n_{a}$ equals to 0 the roadway $a$ will be taken out of set $A$. In that case, $n_{a^{\prime}}$ will reach $N_{a a^{\prime}}$ and the roadway become one-way street. Similar scenario happens when $n_{a}$ equals to $N_{a a^{\prime}}$.

$$
\begin{gathered}
n_{a}+n_{a^{\prime}}=N_{a a^{\prime}} \\
n_{a}, n_{a^{\prime}}=\left\{0,1, \cdots, N_{a a^{\prime}}\right\}
\end{gathered}
$$

To measure the travel time in a specific roadway scientifically, we propose an improved BPR function in (3). The BPR function first designed by the Bureau of Public Road is used to calculate the average travel time in a road. In (3), the road travel time is proportional to the free-flow time cost $t_{a}^{0}$ and have positive correlation with the ratio of traffic flow $x_{a}$ and road capacity $n_{a} / K_{a}$. After further observation, we could find that when $x_{a}$ equals to zero, the travel time is exactly $t_{a}^{0}$, which follows the definition of freeflow travel cost. And when $n_{a}$ equals zero, the road is not exist at all, so the time cost could be regarded as infinite.

$$
t_{a}\left(x_{r}, n_{r}\right)=t_{r}^{0}\left(1+0.15\left(\frac{x_{r}}{n_{r} K_{a}}\right)^{4}\right), n_{r} \neq 0
$$

Apart from the network information given by the graph $G$, the RLOP also takes origin-destination (O-D) pairs as input variables. An O-D pair consists of an origin node, a destination node and a flow demand between these two nodes. Usually a RLOP includes several O-D pair demands. The number of O-D pair will affect the complexity of RLOP.

## B. Problem Objectives

In the lower-level model, the objective function of UE assignment problem is as Eq. (4) shows. In our work, we adopt FW algorithm [14] to solve this problem. In particular, when $n_{a}$ equals to 0 , roadway $a$ will not exist in set $A$. Thus, there is no need to consider that roadway in objective functions. The optimal solution of lower-level is $x_{a}$, which denotes the equilibrium flow in roadway $a$. To be specific, $x_{a}$ has to contain all the O-D pair demands that pass through roadway $a$. In fact, some nodes may be isolated in some solutions, which let the traffic demands toward these isolated nodes cannot be satisfied. In that case, the lowerlevel optimization may not have feasible solution.

$$
\min W\left(x_{a}, n_{a}\right)=\sum_{a=1}^{n_{a}}\left[t_{a}^{x_{a}}, x_{a}, n_{a}\right] d x_{a}
$$

In the upper-level model, the objective is to minimize the total system cost. For a single roadway $a$, the travel cost is modeled as the product of travel time cost $t_{a}\left(x_{a}, n_{a}\right)$ and traffic flow $x_{a}$. The total system cost is the summation of all roadways' travel cost as Eq. (5) shows.

$$
\min Z\left(x_{a}, n_{a}\right)=\sum_{a=1}^{n_{a}} t_{a}\left(x_{a}, n_{a}\right) x_{a}
$$

In this paper, we mainly pay attention to the upper-level optimization model. To solve upper-level problem, we propose a histogram estimation of distribution algorithm.

## III. THE METHOD OF HISTOGRAM EDA FOR RLOP

First, conventional estimation of distribution algorithms (EDA) is outlined in Algorithm 1. After initializing $M$ individuals, EDA iteratively proceeds until the termination criterion is reached. In each generation, $m$ high-quality individuals will be selected based on their fitness values. The set of these $m$ individuals referred to $P_{\text {select }}$. Then a probability model $H$ is established by the solution distribution in $P_{\text {select }}$. With the help of probability model $H$ and many selection methods we could generate offspring $P_{\text {new }}$, where the size of $P_{\text {new }}$ is $M$. Finally, $P$ will be set to $P_{\text {new }}$ in the next generation. Repeat aforementioned steps until termination criterion is met. Based on the conventional EDA, we proposed a histogram EDA, which use fixed-width frequency distribution histogram to build probability

## Algorithm 1 EDA

Input: population size $M$, selection size $m$;
Step 1: Initialize population $P$ with $M$ individuals;
Step 2: While termination criterion is not met do
$P_{\text {select }} \leftarrow$ Select high-quality $m$ individuals based on their fitness value from population $P$;
Build probability model $H$ of $P_{\text {select }}$;
$P_{\text {new }} \leftarrow$ Sample new population from $H$;
$P \leftarrow P_{\text {new }}$
End While
Output: the best individual and its fitness value
distribution model. The main steps of HEDA are outlined in Algorithm 2. The core steps are as following parts show.

## Algorithm 2 HEDA

Input: population size $M$, sample size $m$, variable size $N$, the maximum value of $n^{t h}$ variable $m a x_{n}$
Step 1: Initialize population $P$ with $M$ individuals;
Set initial model $H_{0}^{0}$ with uniform distribution;
Set generation counter $t \simeq 1$;
Step 2: While stopping criterion is not met do Calculate fitness value of $M$ individuals; Sort $M$ individuals in ascending order by their fitness value;
Update the global best solution gbest;
Select first $m$ individuals and build histogram model $H_{0}^{t}$ for $n^{t h}$ variable;
$H_{0}^{t}(j) \leftarrow n H_{0}^{-1}(j)+(1-\alpha) H_{0}^{t}(j)$, for each variable $n$ and each bin $j, j \in\left[0, m a x_{n}\right]$.
$P^{t} \leftarrow$ new population sampled with model $H_{0}$;
Replace population $P$ with $P^{t}$;
$t \approx t+1$;
End While
Output: the gbest and its fitness value

## A. Coding Strategy of HEDA

For RLOP, the decision variables are the number of lanes of each reversible roadways, which are denoted as $n_{a}$. So, it is natural for us to use a real-number encoding chromosome representation. In a chromosome, the decision variables are directly stored in decimal form. The length of a chromosome is the same as the number of reversible roadways. It should be noted that, for different variables, the feasible solution space is also different.

## B. Fitness Evaluation of HEDA

In HEDA, all the fitness value of individuals will be evaluated in every iteration. For every individual, we use $n_{a}$ to represent the input variables. First we solve the lowerlevel optimization problem in (4) with the input value $n_{a}$. In this paper, the FW algorithm [14] is adopted in this step. Then with the optimal solution $x_{a}$ in lower-level and decision variables $n_{a}$, we could derive the total travel cost using (5). The objective function value of lower-level optimization is directly treated as the fitness value of corresponding individual.

In particular, for some individuals, once their solutions could not fulfill all the O-D pairs demand their fitness values will be set to infinite. By doing that, these individuals will be ignored when building the probability model. Thus,
![img-2.jpeg](img-2.jpeg)

Fig. 3 The fixed-width histogram

the validity of probability model can be guaranteed.

## C. Estimation of Distribution Model

In the process of model building of HEDA, we use the fixed-width histogram to represent the probability of all potential solutions in a specific variable. Fig. 3 shows the basic form of the fixed-width histogram model. Initially, the heights of all histograms are set to zero.

First, total M individuals will be sorted in ascending order by their fitness values. Then the first $m$ individuals will be chosen to build the probability model. When deciding the contributions of each individual, their rankings will be taken into consideration. Thus the individuals with low travel cost could have more important impact on the probability model. Benefit from this, the probability model could represent the distribution of optimal solution precisely and find optimal solution quickly. Specifically, in HEDA the corresponding added height of $k^{\mathrm{m}}$ individual in $m$ individuals could be derived by Eq. (6). The height will be added to the corresponding histogram. It is obvious that the total increasement is also normalized in (7).

$$
\begin{gathered}
\Delta h_{k}=\frac{2(m-k+1)}{m(m+1)}, k=\{\mathrm{I}, \cdots m\} \\
\sum_{k=1}^{m} \Delta h_{k}=1
\end{gathered}
$$

Once the current histogram probability distribution model is built, the learning strategy will be adopted to update the historical model. In (8), $\alpha(0 \leq \alpha<1)$ is the learning factor which determines the importance of the historical model in the new histogram model. To maintain the normalization of histogram model, the new model is the normalized linear combination of current model $H_{n}^{i}(j)$ and the historical model $H_{n}^{i+1}(j)$.

$$
H_{n}^{i}(j)=\alpha H_{n}^{i-1}(j)+(1-\alpha) H_{n}^{i}(j)
$$

By adjusting the value of the learning factor, the performance of the EDA model can be changed. The value of $\alpha$ can be neither too small nor too large. When $\alpha=0$, the new model will replace the old model completely in each generation. Obviously $\alpha$ could not reach 1 , which is meaningless and will not exploit the optimal solution.

## D. Generate New Population

After building histogram model, we could generate offspring by their probability in each iteration. The Eq. (9) shows the probability of $n^{\mathrm{m}}$ decision variable equals to $j$ in $t^{\mathrm{m}}$ generation, where max $_{n}$ denotes the maximum value that $n^{\mathrm{m}}$ variable could take. Because of the previous normalization operations, the height of each bins are also normalized (10). For simplicity, in this edition of HEDA we just use the new population to replace the old one, which could increase the searching space of HEDA and avoid falling into local areas.

$$
\begin{gathered}
P_{n}^{i}(j)=\frac{H_{n}^{i}(j)}{\sum_{i=0}^{n^{\max }} H_{n}^{i}(i)} \\
\sum_{i=0}^{n^{\max }} H_{n}^{i}(i)=1
\end{gathered}
$$

## IV. EXPERIMENTS AND ANALYSES

In this section, to show the process and performance of proposed method in RLOP, we arrange several experiments on specific network instances. First, we present a detail explanation about how HEDA works on RLOP. A specific instance is presented in this part. Second, to evaluate the performance of HEDA, several problem instances are simulated both in HEDA and genetic algorithm (GA). Since the GA is also a metaheuristic method and was original designed in discrete space, we believe these two algorithms are comparable in RLOP.

## A. Experimental Settings

The parameters settings are shown in Table I. The crossover probability and the mutation probability follow literature [31].

TABLE I
PARSHUPTIES SETTINGS

| Acconetive | G | M | m | $\alpha$ | $n_{i}$ | $n_{p}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| HEDA | 100 | 200 | 50 | 0.5 | $/$ | $/$ |
| GA | 100 | 200 | $/$ | $/$ | 0.7 | 0.07 |

For test instances, we generate two different size of networks with the same mesh structure manually. One contains 9 nodes and the other contains 16 nodes. About the characteristic of roadways, the free flow cost $t_{0}^{0}$ is generated randomly between 0 to 0.1 ; the feasible unit lane capacity $K_{a}$ are among set $\{2.5,5,7.5,10\} ; n_{a}$ are randomly chosen in set $\{1,2,3,4\}$. The O-D pair demands are uniformly distributed between 0 and 1 except that the destination point is the last node. The O-D pair demands that reach the last node are uniformly distributed over (3.0, 4.0). The reason why we set O-D demands like this is that we want to simulate the asymmetric flow as authentic as possible.

Additionally, it is worthwhile to mention that all results are averaged over 30 independent simulations and all experiments are conducted on a PC with Intel(R) Core (TM) (7-7700 3.60GHz CPU, 8Gb memory. Besides, the Wilcoxon rank-sum test is carried out to show that the results have significant difference between HEDA and GA.

## B. The Analyses of Numerical Example

The numerical example shown in Fig. 4 is a simple urban traffic network. It contains 9 nodes 12 edges and 24 roadways. Some basic network parameters and O-D demands are shown in Table II and III, which are generated according the above settings. Observe this figure, we can acquire several findings:
![img-3.jpeg](img-3.jpeg)

Fig. 4 Numerical Example with 9 nodes 24 roadways

- Each road lane denoted by three parameters to denote the capacity characteristics. And for each pair of twoway roadways, the characteristics are the same, which is reasonable in the real situation. Because, in most cases, the objective conditions of a small area of roads are very similar.
- For every roadway, initial lane number is assigned as default, which is exactly half of the maximum number. The diagonal elements of O-D pair matrix are undefined, since the demands should not be selfclosed.
- The demands in the O-D matrix do not obey uniform distribution. Compared to other nodes, node 8 absorbs the most flow demands. Besides, in the O-D matrix, the flow demands in first 8 columns are uniformly distributed between 0 and 1 . While the flow demands toward to node 8 (last column in O-D matrix) are uniformly distributed over (3.0, 4.0). In short, the flow demands in this example are not symmetric, which give us the space and room to optimize.

TABLE II
NUMBER AL. TRAFFE NOTWORF DATA

| Roadway | $\underline{t 2}$ | $\underline{\boldsymbol{x}}_{\boldsymbol{o}}$ | $\boldsymbol{n}_{\boldsymbol{o}}$ |
| :--: | :--: | :--: | :--: |
| 0 and 2 | 0.06 | 10 | 4 |
| 1 and 7 | 0.04 | 2.5 | 1 |
| 3 and 5 | 0.05 | 5 | 2 |
| 4 and 10 | 0.1 | 10 | 4 |
| 6 and 14 | 0.02 | 5 | 2 |
| 8 and 11 | 0.08 | 2.5 | 1 |
| 9 and 17 | 0.03 | 7.5 | 3 |
| 12 and 15 | 0.02 | 5 | 2 |
| 13 and 19 | 0.04 | 5 | 2 |
| 16 and 22 | 0.05 | 5 | 2 |
| 18 and 20 | 0.05 | 7.5 | 3 |
| 21 and 23 | 0.04 | 7.5 | 3 |

TABLE III
O-D Path M-19IY

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 0 |  | 0.90 | 0.29 | 0.93 | 0.80 | 0.87 | 0.99 | 0.02 | 3.04 |
| 1 | 0.21 |  | 0.77 | 0.28 | 0.51 | 0.06 | 0.61 | 0.10 | 3.44 |
| 2 | 0.80 | 0.58 |  | 0.16 | 0.68 | 0.85 | 0.08 | 0.79 | 3.05 |
| 3 | 0.67 | 0.42 | 0.44 |  | 0.75 | 0.70 | 0.74 | 0.92 | 3.09 |
| 4 | 0.24 | 0.87 | 1.00 | 0.36 |  | 0.07 | 0.12 | 0.25 | 3.98 |
| 5 | 0.95 | 0.47 | 0.44 | 0.97 | 0.56 |  | 0.36 | 0.43 | 3.71 |
| 6 | 0.11 | 0.39 | 0.09 | 0.08 | 0.30 | 0.18 |  | 0.91 | 3.94 |
| 7 | 0.73 | 0.76 | 0.01 | 0.08 | 0.39 | 0.56 | 0.10 |  | 3.59 |
| 8 | 0.55 | 0.63 | 0.18 | 0.71 | 0.47 | 0.94 | 0.57 | 0.19 |  |

For every solution, we first need to judge whether the road network can hold all the O-D pair demands. That is because in some situations, roadways turn to full one-way roadway, which will cause some point become unreachable. However, holding all the O-D pair demands is one of the strong constraints in traffic optimization problem. Once the solution makes some demands cannot be satisfied, this solution should be dismissed or give it a worst fitness value.

On the contrary, the rest of solutions, which could fulfill all the demands are recorded as feasible solutions. In fact, in the process of simulation, the ratio of infeasible solution is constantly decreasing. Meanwhile, the HEDA only selects $m$ individuals to build the probability model, which naturally dismisses the infeasible solutions since these solutions lie in the back part of the population after sorting procedure.

Table IV shows the number of lanes in 24 roadways and their actual traffic flow after optimization. As mentioned earlier, it is quite clear that node 8 collect a large amount of traffic demands. This kind of asymmetric O-D demands will cause asymmetric flow. To be specific, roadway 16 and 21 connect to node 8 directly. Thus these two roadways have to carry a relatively larger traffic burden. As expected, the optimization results show that the roadways towards to node 8 receive more lanes than the roadways away from node 8 . Another noteworthy issue is that roadway 4 has no flow path through, which indicates in the fourth decision variable is complete irrelevant in the RLOP optimization. One of possible reason is that the free flow time cost $t_{0}^{0}$ of road 4 and road 10 is much larger compare to other roads, when considering path planning most drivers will avoid this road and make the flow in this road nearly reduce to 0 . In fact, this example gives us an inspiration, once there are some emergency situations cause specific road section congest, this congestion status will increase the free flow time cost immediately. In that case, applying reversible lanes problem optimization could get an optimal assignment, which could relieve the traffic congestion dynamically.

TABLE IV
OPTIMAL REGULTS FOR NUMERICAL EXAMPLE ATTES OPTIMIZATION

| Roadway | $\boldsymbol{n}_{\boldsymbol{o}}$ | $\boldsymbol{x}_{\boldsymbol{o}}$ | Roadway | $\boldsymbol{n}_{\boldsymbol{o}}$ | $\boldsymbol{x}_{\boldsymbol{o}}$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 0 | 5 | 5.83 | 2 | 3 | 2.84 |
| 1 | 1 | 3.69 | 7 | 1 | 3.11 |
| 3 | 3 | 8.99 | 5 | 1 | 4.04 |
| 4 | 7 | 0.00 | 10 | 1 | 1.00 |
| 6 | 3 | 13.54 | 14 | 1 | 4.82 |
| 8 | 1 | 1.96 | 11 | 1 | 1.72 |
| 9 | 4 | 7.18 | 17 | 2 | 2.64 |
| 12 | 1 | 5.40 | 15 | 3 | 5.84 |
| 13 | 3 | 4.38 | 19 | 1 | 2.30 |
| 16 | 3 | 14.16 | 22 | 1 | 2.22 |
| 18 | 5 | 10.28 | 20 | 1 | 3.30 |
| 21 | 5 | 13.69 | 23 | 1 | 2.03 |

## C. Results and Comparisons for Test Instances

In this part, we investigate the influence of the network size and O-D pair demands number on the HEDA method and simple GA approach. Apparently one of the complexities of this problem is embodied in the topology structure of network. To measure the performance of our method on complexity problem compare to the simple one, we expand the node number as well as the road number but keep the mesh structure and flow distribution the same as the small one.

We apply these two methods on 2 different scale networks, and in each network, 4 different sizes of O-D demands are compared. The results and comparisons are shown in Table V and Fig. 5. The scale [9, 24] means that the network contains 9 nodes and 24 roads. The entry of Rank Sum is the optimal results of Wilcoxon rank-sum tests between HEDA and GA over 30 independently simulations.

It should be noticed that all the test network instances are generated manually, thus we have no idea about the optimal solutions to these problems.

TABLE V
Optimal Fitness and Wilcoxon Rank-Out Results in 10 Instances of HEDA and GA

| NET | O-D PAR <br> DeMANDS | HEDA | GA | Rank <br> $\mathrm{St} / \mathrm{M}$ |
| :--: | :--: | :--: | :--: | :--: |
| $[9,24]$ | 18 | $2.9488 \pm 4.73 \mathrm{e}-05$ | $2.9490 \pm 2.23 \mathrm{e}-03$ | $5.7 \mathrm{e}-08$ |
|  | 36 | $3.7256 \pm 4.84 \mathrm{e}-04$ | $3.7262 \pm 1.47 \mathrm{e}-03$ | $3.9 \mathrm{e}-07$ |
|  | 54 | $4.9808 \pm 7.23 \mathrm{e}-05$ | $4.9815 \pm 5.40 \mathrm{e}-03$ | $3.9 \mathrm{e}-08$ |
|  | 72 | $5.4556 \pm 1.68 \mathrm{e}-04$ | $5.4575 \pm 2.39 \mathrm{e}-02$ | $4.7 \mathrm{e}-07$ |
| $[16,48]$ | 54 | $9.3799 \pm 4.13 \mathrm{e}-02$ | $9.4510 \pm 7.58 \mathrm{e}-02$ | $8.1 \mathrm{e}-11$ |
|  | 72 | $11.0552 \pm 1.99 \mathrm{e}-02$ | $11.1249 \pm 8.85 \mathrm{e}-02$ | $9.9 \mathrm{e}-11$ |
|  | 144 | $16.4214 \pm 2.87 \mathrm{e}-01$ | $16.6487 \pm 2.34 \mathrm{e}-01$ | $8.9 \mathrm{e}-10$ |
|  | 176 | $19.4237 \pm 1.23 \mathrm{e}-01$ | $19.7042 \pm 2.84 \mathrm{e}-01$ | $5.0 \mathrm{e}-11$ |
|  | 208 | $20.7905 \pm 1.23 \mathrm{e}-01$ | $21.1431 \pm 3.03 \mathrm{e}-01$ | $3.3 \mathrm{e}-11$ |
|  | 240 | $27.6578 \pm 2.89 \mathrm{e}-01$ | $27.9900 \pm 5.59 \mathrm{e}-01$ | $5.5 \mathrm{e}-08$ |

First, observing Table V, we can find that in all instances the HEDA could find better optima than GA. The results shown in Rank Sum entry indicate these two different algorithms have significant difference in all instances. Besides, the solutions gained by HEDA are more stable than use GA, since from these tables we could find that all the optima intervals of HEDA are smaller compare to GA.

Second, from these tables, we can also observe that when the O-D pair demands are same, with the increase of the network size, the travel time cost of both HEDA and GA are getting larger. This is because in a complex road network, the path from origin to destination is long and tortuous. When the traffic capacity of each section is exact same, the travel time is proportional to the length of path. Even under this condition, HEDA could obtain a smaller objective function value.

Third, in the same network, with the increase of O-D pair demands, the fitness value of HEDA and GA are getting worse. This is because the number of O-D pair demands could reflect the busyness of traffic. When the traffic capacity of each section remains the same, the travel time cost has positive correlation with the size of traffic flow. Despite this, HEDA could get better optimization compare to GA. The gap between these two methods is gradually increasing.

To have a better view of the convergence speed with these two algorithms in solving different RLOP, we plot the average current best fitness value in the process of iteration and the figs are presented in Fig. 5. The horizontal ordinate denotes the generation and the vertical ordinate denotes the fitness value. Red solid lines represent HEDA and black solid lines represent GA. From Fig. 5 several findings can be obtained:

First, on the whole, HEDA could get a better solution with a first convergence speed in all instances compare to GA. At the beginning of the program, both methods have almost the same speed. This is because the HEDA and GA are all stochastic search algorithms. For some instances in Network (2), in the first few generations, GA seems to find a better solution quickly. But the problem is that, GA falls
into local optimum prematurely, and it is difficult to jump out of the local optima to global optima.
![img-4.jpeg](img-4.jpeg)

Fig. 5 HEDA and GA convergence results in 10 instances
Second, we can also observe that when the network scale remains same, with the number of O-D demands increase. The convergence speeds of HEDA have not too much change. In Network (1), 4 instances stop before 20 generations, and in Network (2), 6 instances stop before 40 generations. While for GA the convergence speed decrease intensely. In Network (1), 4 instances stop between 60 to 80 generations, in Network (2), 6 instances do not converge in 100 generations.

Third, when the number of O-D pair demands keep same and the size of network became larger, the convergence speed decrease both in HEDA and GA. This shows in RLOP the network size has significant influence on the complexity. When the network size increase the size of decision variables is also increase. Thus, the search space becomes larger, resulting in a low convergence speed.

Comprehensively, we can conclude that HEDA can possess higher convergence speed and precision than GA under most instances especially in large-scale.

## V. CONCLUSION

In this paper, we proposed a HEDA for RLOP. The problem is modeled as a bi-level optimization problem. In upper level the objective is to minimize the total system cost. In the lower level model, the problem is referred to UE assignment problem. The input knowledge including network topology structures and several O-D pair demands. After several experiments, the comparison results show that HEDA is promising in finding optimal solution as well as holding higher efficiency in RLOP. For future work, it would be interesting to apply parallel and cooperatively coevolutionary algorithms [32][33] to solve large-scale RLOP in city-level.

## REFERENCES

[1] J. Q. Xu, "Approach to Several Problems of Urban Road Planning Design," Urban Roads Bridges \& Flood Control, 2001.
[2] T. Kimoto et al., "Integrating Heterogeneous Data Sources for Planning Road Reconstruction," Procedka Computer Science, vol. 60, pp. 1720-1727, 2015.
[3] Y. Wang, D. Wang, S. Jin, N. Xiao, Y. Li, and E. J. I. T. o. C. S. T. Frazzoli, "Iterative Tuning With Reactive Compensation for Urban Traffic Signal Control," IEEE Transactions on Control Systems Technology, vol. 25, no. 6, pp. 2047-2059, 2017.
[4] J. R. D. Frejo, I. Papamichail, M. Papageorgiou, and E. F. Camacho, "Macroscopic Modeling and Control of Reversible Lanes on Freeways," IEEE Transactions on Intelligent Transportation Systems, vol. 17, no. 4, pp. 948-959, 2016.
[5] B. Wolikon and L. Lambert II, "Planning and operational practices for reversible roadways," Institute of Transportation Engineers. ITE Journal, vol. 76, no. 8, pp. 38-43, 2006.
[6] J. Wu, H. Sun, Z. Gao, and H. Zhang, "Reversible lane-based traffic network optimization with an advanced traveller information system," Engineering Optimization, vol. 41, no. 1, pp. 87-97, 2009.
[7] J. Alber, "Exact Algorithms for NP Hard Problems on Networks: Design, Analysis, and Implementation," University of Tübingen, Germany, 2002.
[8] Y. Jia et al., "Distributed Cooperative Co-evolution with Adaptive Computing Resource Allocation for Large Scale Optimization," IEEE Transactions on Evolutionary Computation, pp. 1-1, 2018.
[9] X. Yu, W. Chen, T. Gu, H. Yuan, H. Zhang, and J. Zhang, "ACO-A*: Ant Colony Optimization Plus A* for 3D Traveling in Environments with Dense Obstacles," IEEE Transactions on Evolutionary Computation, pp. 1-1, 2018.
[10] W. Chen, Y. Jia, F. Zhao, X. Luo, X. Jia, and J. Zhang, "A Cooperative Co-evolutionary Approach to Large-Scale Multisource Water Distribution Network Optimization," IEEE Transactions on Evolutionary Computation, pp. 1-1, 2019.
[11] X. Yu et al., "Set-Based Discrete Particle Swarm Optimization Based on Decomposition for Permutation-Based Multiobjective Combinatorial Optimization Problems," IEEE Transactions on Cybernetics, vol. 48, no. 7, pp. 2139-2153, 2018.
[12] Y. Jia et al., "A Dynamic Logistic Dispatching System With SetBased Particle Swarm Optimization," IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 48, no. 9, pp. 1607-1621, 2018.
[13] A. Sinha, P. Malo, and K. Deb, "A Review on Bilevel Optimization: From Classical to Evolutionary Approaches and Applications," IEEE

Transactions on Evolutionary Computation, vol. 22, no. 2, pp. 276295, 2018.
[14] L. J. LeBlanc, E. K. Morlok, and W. P. Pierskalla, "An efficient approach to solving the road network equilibrium traffic assignment problem," Transportation Research Part B: Methodological, vol. 9, no. 5, pp. 309-318, 1975.
[15] H. Zhang and Z. Guo, "Two-way road network design problem with variable lanes," Journal of Systems Science and Systems Engineering, vol. 16, no. 1, pp. 50-61, 2007.
[16] P. Larrañaga and J. A. Lozano, Estimation of distribution algorithms: A new tool for evolutionary computation. Springer Science \& Business Media, 2001.
[17] P. Larranaga, "A review on estimation of distribution algorithms," in Estimation of distribution algorithms: Springer, 2002, pp. 57-100.
[18] Q. Yang, W. Chen, Y. Li, C. L. P. Chen, X. Xu, and J. Zhang, "Multimodal Estimation of Distribution Algorithms," IEEE Transactions on Cybernetics, vol. 47, no. 3, pp. 636-650, 2017.
[19] Y. Sun, G. G. Yen, and Z. Yi, "Improved Regularity Model-based EDA for Many-objective Optimization," IEEE Transactions on Evolutionary Computation, vol. 22, no. 5, pp. 662-678, 2018.
[20] V. A. Shim, K. C. Tan, and C. Y. Cheong, "An Energy-Based Sampling Technique for Multi-Objective Restricted Boltzmann Machine," IEEE Transactions on Evolutionary Computation, vol. 17, no. 6, pp. 767-785, 2013.
[21] Q. Yang et al., "Segment-Based Predominant Learning Swarm Optimizer for Large-Scale Optimization," IEEE Transactions on Cybernetics, vol. 47, no. 9, pp. 2896-2910, 2017.
[22] Q. Yang et al., "Adaptive Multimodal Continuous Ant Colony Optimization," IEEE Transactions on Evolutionary Computation, vol. 21, no. 2, pp. 191-205, 2017.
[23] Q. Yang, W. Chen, J. D. Deng, Y. Li, T. Gu, and J. Zhang, "A LevelBased Learning Swarm Optimizer for Large-Scale Optimization," IEEE Transactions on Evolutionary Computation, vol. 22, no. 4, pp. 578-594, 2018.
[24] X. Wen et al., "A Maximal Clique Based Multiobjective Evolutionary Algorithm for Overlapping Community Detection," IEEE Transactions on Evolutionary Computation, vol. 21, no. 3, pp. 363377, 2017.
[25] W. Dong, T. Chen, P. Tibo, and X. Yao, "Scaling Up Estimation of Distribution Algorithms for Continuous Optimization," IEEE Transactions on Evolutionary Computation, vol. 17, no. 6, pp. 797822, 2013.
[26] X. Liang, H. Chen, and J. A. Lozano, "A Boltzmann-Based Estimation of Distribution Algorithm for a General Resource Scheduling Model," IEEE Transactions on Evolutionary Computation, vol. 19, no. 6, pp. 793-806, 2015.
[27] J. Ceberio, E. Inuroski, A. Mendiburu, and J. A. Lozano, "A DistanceBased Ranking Model Estimation of Distribution Algorithm for the Flowshop Scheduling Problem," IEEE Transactions on Evolutionary Computation, vol. 18, no. 2, pp. 286-300, 2014.
[28] H. Karshenas, R. Santana, C. Bielza, and P. Larrañaga, "Multiobjective Estimation of Distribution Algorithm Based on Joint Modeling of Objectives and Variables," IEEE Transactions on Evolutionary Computation, vol. 18, no. 4, pp. 519-542, 2014.
[29] S. Y. Wang and L. Wang, "An estimation of distribution algorithmbased memetic algorithm for the distributed assembly permutation flow-shep scheduling problem," IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 46, no. 1, pp. 139-149, 2016.
[30] W. Shi, W. Chen, Y. Lin, T. Gu, S. Kwong, and J. Zhang, "An Adaptive Estimation of Distribution Algorithm for Multi-Policy Insurance Investment Planning," IEEE Transactions on Evolutionary Computation, vol. 23, no. 1, pp. 1-14, 2019.
[31] A. Rossi, M. Antonetti, M. Barloscio, and M. Lanzetta, "Fast genetic algorithm for roundness evaluation by the minimum zone tolerance (MZT) method," Measurement, vol. 44, no. 7, pp. 1243-1252, 2011.
[32] W. Chen, Y. Jia, F. Zhao, X. Luo, X. Jia, and J. Zhang, "A Cooperative Co-evolutionary Approach to Large-Scale Multisource Water Distribution Network Optimization", IEEE Transactions on Evolutionary Computation, in press, 2019.
[33] Q. Yang, W. Chen, T. Gu, H, Zhang, H, Yuan, S. Kwong and J. Zhang, "A Distributed Swarm Optimizer with Adaptive Communication for Large Scale Optimization", IEEE Trans. on Cybernetics, in press, 2019.