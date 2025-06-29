# Articles 

## Applied Research on Distributed Generation Optimal Allocation Based on Improved Estimation of Distribution Algorithm

Lei Yang ${ }^{1}$, Xiaohui Yang ${ }^{1, *}$, Yue $\mathrm{Wu}^{2}$ and Xiaoping Liu ${ }^{1}$<br>1 College of Information Engineering, Nanchang University, Nanchang 330031, China; 416114316029@email.ncu.edu.cn (L.Y.); xpliu@sce.carleton.ca (X.L.)<br>2 State Grid Jilin Electric Power Company, Changchun 130000, China; 416114316039@email.ncu.edu.cn<br>* Correspondence: yangxiaohui@ncu.edu.cn

Received: 28 July 2018; Accepted: 24 August 2018; Published: 7 September 2018


#### Abstract

Most of the current algorithms used to solve the optimal configuration problem in the distributed generation (DG) of electricity depend heavily on control parameters, which may lead to local optimal solutions. To achieve a rapid and effective algorithm of optimized configuration for distributed generation, a hybrid approach combined with Bayesian statistical-inference and distribution estimation is proposed. Specifically, a probability distribution estimation model based on the theory of Bayesian inference is established, then a posteriori probability model with the prior distribution and the conditional distribution is generated, and new individual generators are formed into a dominant group. The information of each individual of this dominant group is used to update the probability model and the updated posteriori probability is used for sampling until the optimal solution is obtained. Finally, the 12 bus, 34 bus and 69 bus radial distribution system is used as an example and comparison is performed to show the effectiveness of the proposed algorithm.


Keywords: distributed generation; radial distribution system; estimation of distribution algorithm; bayesian statistical-inference; posterior probability

## 1. Introduction

Because of the high impedance ratio, a large part of the power loss in the power grid comes from the distribution network [1]. With the rapid development of the society, the load demand increases exponentially, which leads to higher power loss and lower voltage stability. The access of DGs can reduce the power loss, improve its voltage stability, and bring significant economic benefits to the power system [2,3]. However, the infiltration of DGs complicates the distribution network, and the power flow are changed in size and direction. The power loss of distribution network is closely related to the load demand and configuration of DGs. Therefore, the optimal configuration of DG is particularly important [4-6].

Many researchers have used different types of algorithms to solve the DG locating and sizing problem in distribution network. The methods they use mainly include analytical methods, classic optimization algorithms, and heuristics [7]. The advantages and disadvantages of these methods are shown in Table 1. The analytical methods are proposed to solve optimal configuration problems of DGs in different scenarios [8-11]. The drawback of analytical methods is its incompetence in handling the multi-objective optimization problems. The works presented in Refs. [12-15] used the classical optimization algorithm to solve the DG locating and sizing problem. There are also many papers using heuristic methods. Some authors had used genetic algorithm to solve the DG locating and sizing problem [16,17]. However, it is easy to premature, and its solution depends on

the initial population. The bat algorithm is used to solve the DG locating and sizing problem in Refs. [18,19]. However, its convergence speed is slow and the optimization precision is low. The artificial bee colony algorithm is also applied to the DG optimal allocation problem [20,21]. Unfortunately, when approaching the global optimal solution, it is easy to fall into local optimum, and the search speed slows down. Related research [22,23] used the bacterial foraging algorithm to solve the DG locating and sizing problem, but the convergence speed is slow and the high complexity of this algorithm limits its application. The particle swarm optimization algorithm is used to optimize the location and capacity of the DG in Refs. [24,25], but it performs poorly when dealing with discrete optimizations. The literatures [26,27] apply the simulated annealing algorithm to the problem of DG optimal allocation. However, its convergence speed is slow and parallel computing is difficult.

Table 1. Advantages and disadvantages of various algorithms.

| Algorithm | Advantage | Shortcoming |
| :--: | :--: | :--: |
| Analytical method | The method is simple and less workload | Dealing with single objective optimization problem only |
| Classical optimization algorithm | The model is accurate and the method is simple | The computation is large and the computation speed is slow |
| Genetic algorithm | The convergence speed is fast and the versatility is strong | It is more complex, easy to fall into premature convergence, and depends on the initial population |
| Bat algorithm | Simple structure, few parameters and strong robustness | The speed of convergence is slow and the precision of optimization is low |
| Artificial bee colony algorithm | The global search ability is strong and the convergence speed is fast | it is easy to fall into the local optimum, and the search speed slows down later |
| Bacterial foraging algorithm | Strong parallel search ability and easy to get out of local minimum | The convergence speed is slow and the computation is large |
| Particle swarm optimization | The training speed is fast, the efficiency is high, and the algorithm is simple | It is easy to fall into local optimal solution and poor handling of discrete optimization problems |
| Simulated annealing algorithm | Strong global search capability | Convergence speed is slow and parallel computing is difficult |

An improved estimation of distribution algorithm (IEDA) is proposed in this paper. The IEDA improves the convergence speed and eliminates some shortcomings of the estimation of distributed algorithm (EDA). The proposed algorithm is validated by the simulation of 12 bus, 34 bus and 69 bus radial distribution system and compared against two highly competitive algorithm: EDA and Genetic Algorithm (GA).

This paper is organized as follows: after this introduction, Section 2 shows the optimal configuration model of DG. In Section 3, detailed description of the IEDA is presented. Section 4 presents the power flow analysis. Section 5 provides the recurrence equations of power flow, while the simulation results is given in Section 6. Finally, Section 7 presents the conclusion.

# 2. Optimal Configuration Model of DG 

The optimal configuration model of DG is established, in which the objective is to minimize the total power loss. This problem is subject to power balance constraints, voltage and current constraints and limit transmission power constraints.

The objective function is given by,

$$
\min f=\min \left(T_{\text {Loss }}\right)
$$

where $T_{L o s s}$ is the total power loss of the radial distribution system.
Subject to,
(1) Power balance constraints:

$$
P_{L o s s}+\sum P_{D i}=\sum P_{D G i}
$$

where $P_{D G i}$ is the real power of the bus $i$ with the accessing of DG, $P_{D i}$ is the power demand of the bus $i, P_{\text {Loss }}$ is the line losses of the bus $i$.
(2) Voltage constraints:

$$
U_{\text {imin }} \leq U_{i} \leq U_{\text {imax }}
$$

where, $U_{\text {imax }}$ and $U_{\text {imin }}$ are the maximum and minimum allowable voltage limits of bus $i$.
(3) Current constraint:

$$
I_{i} \leq I_{\text {imax }}
$$

where, $I_{\text {imax }}$ is the maximum current value of branch $i$.

# 3. Algorithm Principle 

### 3.1. Estimation of Distribution Algorithm

The idea of EDA originates from genetic algorithm, but it is different from genetic algorithm. The genetic algorithm is a kind of searching method, which simulates the natural evolution at the micro level, while the EDA controls algorithm search at the macro level [28].

Compared with genetic algorithm, the EDA algorithm does not have crossover and mutation operators. Instead, the two steps of probability modeling and sampling are adopted. The EDA uses the global information of population to establish probability model and control the search procedure of the algorithm from the "micro" level. It has strong global search capability and the ability to solve complex problems of high dimension. In the EDA, a global manipulation mode of operation replaces the genetic operator [29]. The above-mentioned advantages have attracted the interest of many scholars. After more than ten years of development, The EDA algorithm has become a research hotspot in the field of intelligent computation.

The specific implementation steps of the EDA are as follows:
(1) Initialize the population
(2) Execute cycle-body

1. Selecting: Select several individuals to form a dominant group according to a certain selection mechanism.
2. Modeling: Establish a probability model according to a certain criteria.
3. Sampling: Use the proposed probability model to generate the next generation; determine whether the termination condition is met. if it is satisfied, output the optimal individual. If not, continue to execute the loop body.

The flow chart of EDA is shown in Figure 1.

![img-0.jpeg](img-0.jpeg)

Figure 1. The flow chart of EDA.

# 3.2. The Principle of Bayesian Statistical Inference 

The key to the EDA algorithm is how to establish and update the probability model reasonably and efficiently. The main feature of Bayesian statistical inference is the use of prior distribution. After getting the sample observation values, the posterior distribution is obtained from the information provided by the sample observations and the prior distribution by [30]. The posterior distribution which contains abundant information is the basis for Bayesian statistical inference. Due to the application of prior distribution, Bayesian statistical inference has a good statistical inference effect on both large and small samples. A typical Bayesian formula is:

$$
q\left(A_{i} / B\right)=\frac{q\left(A_{i}\right) q\left(B / A_{i}\right)}{\sum_{j=1}^{n} q\left(A_{i}\right) q\left(B / A_{i}\right)}
$$

where, event $A_{1}, A_{2}, \cdots, A_{n}$ are complete event group. $i=1,2, \cdots, n ; q\left(A_{i}\right)$ is the prior distribution probability model. And the occurrence of event B can affect the probability of occurrence of event $A_{1}, A_{2}, \cdots, A_{n}$. Therefore, it needs to be re-estimated. Finally, it is expressed in the form of the posterior distribution.

Therefore, the Bayesian inference model uses the prior information and the actual sample information to obtain the posterior information and it transforms the prior distribution into the posterior distribution, which forms the Bayesian statistical inference model.

### 3.3. The EDA with Bayesian Inference Improved

### 3.3.1. Establishment of IEDA Probability Model

In the multivariate related discrete optimization problem, the position or value of each variable in the individual directly affects the individual's fitness. Therefore, establishing a probability model that reflects the value of each variable is the key to solving such problems in the EDA. The probability model established by Bayesian inference includes three models: prior probability, conditional probability and posterior probability.
(1) Establishment of prior distribution probability model

The individual variables in the EDA algorithm in this paper are binary coded. Set the individual length to be $l . X=(x(1), x(2), \cdots, x(l))$ represents an individual. And $x(j)$ is a variable in the $j$ th

position. Establish a prior distribution probability for variables at each position. The prior probability of all variables composed a prior distribution probability model:

$$
q_{x}=\left(q_{1}, q_{2}, \cdots, q_{l}\right)^{T}
$$

(2) Establishment of conditional distribution probability model

$$
q_{y}^{t}=\left[\begin{array}{cccc}
q^{t}\left(x^{t^{*}}(1) / x^{t}(1)\right) & q^{t}\left(x^{t^{*}}(1) / x^{t}(1)\right) & \cdots & q^{t}\left(x^{t^{*}}(l) / x^{t}(1)\right) \\
q^{t}\left(x^{t^{*}}(1) / x^{t}(2)\right) & q^{t}\left(x^{t^{*}}(2) / x^{t}(2)\right) & \cdots & q^{t}\left(x^{t^{*}}(l) / x^{t}(1)\right) \\
\vdots & \vdots & \vdots & \vdots \\
q^{t}\left(x^{t^{*}}(1) / x^{t}(l)\right) & q^{t}\left(x^{t^{*}}(2) / x^{t}(l)\right) & \cdots & q^{t}\left(x^{t^{*}}(l) / x^{t}(l)\right)
\end{array}\right]
$$

Each variable in an individual will affect other variables, Therefore, a conditional probability vector can be used to indicate the influence of the remaining variables on the variable $x(j)$, which can be expressed as $q_{j}=(q(x(j) / x(1)), q(x(j) / x(2)), \cdots, q(x(j) / x(l)))^{T}$. The conditional probability can be obtained according to individual information in the dominant group, which characterizes the conditional probability of variable $x(j)$ when other variables take a certain value. Assuming the following conditions, the kth individual in the dominant group is represented as $X_{k}^{t}=\left(x_{k}^{t}(1), x_{k}^{t}(2), \cdots, x_{k}^{t}(l)\right)$ while the winning individual in the $t$ th generation is $X^{t^{*}}=\left(x^{t^{*}}(1), x^{t^{*}}(2), \cdots, x^{t^{*}}(l)\right)$ in the $t$ th generation. we can establish the conditional matrix $q_{y}^{t}$ of the $t$ th generation according to the winning individuals and dominant groups. And the conditional matrix is shown in Formula (7).

According to statistical theory:

$$
q^{t}\left(x^{t^{*}}(j) / x^{t}(i)\right)=q^{t}\left(x^{t^{*}}(j) \cdot x^{t}(i)\right) / q^{t}\left(x^{t}(i)\right)
$$

where, $q^{t}\left(x^{t^{*}}(j) \cdot x^{t}(i)\right)$ represent the probability when the variable $x(j)$ in the winning individual and the variable $x(i)$ in the dominant group take the specific value at the same time. And $q^{t}\left(x^{t}(i)\right)$ represent the probability when variable $x(i)$ takes a specific value in the dominant group.
(3) Establishment of posterior distribution probability model

When the population evolves to the $t$ th generation, the corresponding conditional probability matrix is $q_{y}^{t}$. By using the prior probability and the conditional probability, the posterior probability model $q_{h}^{t}:\left\{q_{i j}^{t}=q^{t}\left(i / x^{t^{*}}(j)\right), i, j=1,2, \cdots, l\right\}$ is established according to the Bayesian formula.

$$
q^{t}\left(i / x^{t^{*}}(j)\right)=q^{t}\left(x^{t^{*}}(j) / x^{t}(i)\right) \cdot q_{i}^{t} / \sum_{i}^{l} q^{t}\left(x^{t^{*}}(j) / x^{t}(i)\right) \cdot q_{i}^{t}
$$

where, the denominator is the sum product of the $j$ th column of the prior probability and the conditional probability matrix. It portrays the conditional probability of re-estimating the value of other variables under the condition that the corresponding variable of the optimal individual takes a specific value. The posterior probability matrix $q_{y}^{t}$ combines the prior information and the new information provided in the evolutionary process, so it has better statistical inference results.

# 3.3.2. Update of Probability Model 

The posterior distribution probability model is obtained through calculation of the prior distribution probability model and conditional distribution probability model. Therefore, the update of the probability model can be divided into two steps. First, updating the prior distribution probability model and the conditional probability model, and then combining the updated information of the two model to obtain an updated posterior distribution probability model.

(1) Update of prior distribution probability model

When the population evolve to the $t$ th generation, and the winning individuals is $X^{t^{*}}=$ $\left(x^{t^{*}}(1), x^{t^{*}}(2), \cdots, x^{t^{*}}(l)\right)$. According to the information of the individuals in the dominant group $D^{t}$, the updated prior distribution probability is as follows:

$$
\begin{gathered}
q_{j}^{t+1}= \begin{cases}{\left[1-\frac{\alpha}{m} \sum_{k=1}^{m}\binom{\delta_{j}^{t}}{k} q_{j}^{t}+\frac{\alpha}{m} \sum_{k=1}^{m}\binom{\delta_{j}^{t}}{k} \quad x_{k}^{t}(j)=x_{k}^{t^{*}}(j)\right.} \\
{\left[1-\frac{\alpha}{m} \sum_{k=1}^{m}\binom{\delta_{j}^{t}}{k} q_{j}^{t} \quad x_{k}^{t}(j) \neq x_{k}^{t^{*}}(j)\right.} \\
\delta_{j}^{t}= \begin{cases}1 & x_{k}^{t}(j)=x_{k}^{t^{*}}(j) \\
0 & x_{k}^{t}(j) \neq x_{k}^{t^{*}}(j)\end{cases}
\end{gathered}
$$

where, the value of $\delta_{j}^{t}(j=1,2, \cdots, l)$ is related to the value of the corresponding position of the individuals in the dominant group and the winning individuals. If the two are equal, the value take 1 , if not, take $0 . \alpha$ is a control parameter between $(0,1)$, and the larger $\alpha$ is, the greater the influence is implemented on the offspring. And $m$ is the number of individuals in the dominant group.
(2) Update of conditional distribution probability model

The update of conditional distribution probability model should be carried out through the information of the dominant group $D^{t}$, which can be formulated as follows:

$$
\begin{gathered}
q_{a, b}^{t+1}=(1-\beta) q_{a, b}^{t}+\frac{\beta}{m} \sum_{k=1}^{m} \lambda_{a, b}^{t} \\
\lambda_{a, b}^{t}= \begin{cases}1 & \text { The variable } a \text { and } b \text { are all } 0 \\
0 & \text { other }\end{cases}
\end{gathered}
$$

where, $q_{a, b}^{t+1}$ is an element in the conditional probability matrix model. $a=b=1,2, \cdots, l, \beta \in(0,1)$ $m$ parameter is the same as above. $t$ is an evolutionary algebra of the current dominant group. The function of the controlling parameter $\beta$ is similar to that of $\alpha$.
(3) Update the probability model of posteriori distribution

Using the updated prior distribution probability model and conditional distribution probability model, a new posterior probability model can be obtained by Bayesian formula.

# 3.3.3. Population Regeneration 

New individuals are generated based on the updated posterior probability model. The sampling method is setting each column of the updated posterior probability as basis, and adopting the roulette wheel selection repeatedly to select the value of each position and then produce a new individual, The new individual, together with the current dominant population, consist of the next generation. Then calculate the fitness of the new individual and judge the convergence.

### 3.4. Algorithm Steps

The flow chart of solving the distributed generation optimization configuration problem of the IEDA is shown in Figure 2. Use the Formula (1) as fitness function, the algorithm steps are as follows:

Step 1: Individual coding. Take the capacity of the distributed generation connected to each bus of the radial distribution system as a variable. $l$ buses corresponds to the $l$ variables, Therefore, the dimension of the individual $X$ is $l$. That is, one solution vector of the system is $X=\left(x_{1}, x_{2}, \cdots, x_{l}\right)$. Each variable can only be 0 or a non-zero constant C . A variable equals 0 means that the bus is not connected to the distributed generation. That the variable value is a non-zero constant C indicates that the bus is connected to the distributed power source, and C is the capacity of the access.

Step 2: Generate the initial population. Arrange a certain number of zero in the position of all variables randomly to form the initial population, which can be stored in the initial group N(d) if the network topology analysis meets the requirements.

Step 3: Calculate the fitness and choice of dominant groups. Calculate the individual fitness by the fitness function, and select a certain proportion of dominant individuals from the group to form the dominant group $\mathrm{D}(\mathrm{m})$. The selection rate M is determined by the size of initial population.

Step 4: Establish probability model based on dominant group. After establishing a priori distribution probability model, a conditional probability model and a posteriori probability model is formed through proportional selection. Update the prior probabilities and conditional probabilities according to the superior individuals and groups in $\mathrm{D}(\mathrm{m})$, and then update the posterior probability according to the updated priori probabilities and conditional probability.

Step 5: Generate new individuals by sampling from the posterior probability model. The updated posterior probability model is sampled through the roulette wheel selection to generate new individuals and calculate fitness. With the increase of evolutionary algebra, the probability of the emergence of the optimal individual increases gradually. When the probability reaches a certain value, the calculation would be terminated, and then the optimal solution is optimum individual in the current dominant group. Otherwise, a new dominant group is selected from the population and the step 6 is executed.

Step 6: Update the probability model, return to step 5, repeat the above steps until the terminating conditions are satisfied.
![img-1.jpeg](img-1.jpeg)

Figure 2. The flow chart of IEDA.

# 4. Load Flow Analysis 

Distribution load flow is an important part of distribution automation system and distribution management system. The solution of the network reconfiguration, reactive power optimization and

state estimation problem require efficient power flow calculation methods. Due to the High-impedance ratio of the distribution system, the fast decoupling and Newton Raphson load method is not suitable for the calculation of the load of the distribution system. Therefore, this paper uses a direct solution method to calculate the power flow of distribution network and get a better solution. Using two developed matrices, the bus-injection to branch-current matrix and the bus-current to bus-voltage matrix and a simple matrix multiplication are used to obtain load flow solutions [31].

For distribution networks, the expression for $S_{i}$ is

$$
S_{i}=P_{i}+Q_{i}, i=1,2, \cdots, N
$$

where $N$ is the number of buses, $P_{i}$ is the active power of bus $i$, and $Q_{i}$ is the reactive power of bus $i$. The injection current is calculated as follows:

$$
I_{i}=\left(S_{i} / V_{i}\right)^{*}
$$

The relationship between the injected bus current and the bus voltage is expressed as follows:

$$
[\Delta V]=[B C B V][B I B C][I]=[D L F][I]
$$

where BCBV is the branch-current to bus-voltage matrix. BIBC is the bus-injections to branchcurrents matrix.

The solution to the load of radial distribution system can be obtained with Equations (17)-(19).

$$
\begin{gathered}
I_{i}^{k}=\left(S_{i} / V_{i}^{k}\right)^{*} \\
{\left[\Delta V^{k+1}\right]=[D L F]\left[I^{k}\right]} \\
{\left[V^{k+1}\right]=\left[V_{0}\right]\left[\Delta V^{k+1}\right]}
\end{gathered}
$$

# 5. Power Calculation 

The power is calculated by a set of simplified recurrence equations.

$$
\begin{aligned}
P_{i+1} & =P_{i}-P_{L i+1}-R_{L i+1} \times \frac{\left(P_{i}^{2}+Q_{i}^{2}\right)}{\left|V_{i}^{2}\right|} \\
Q_{i+1} & =Q_{i}-Q_{L i+1}-X_{L i+1} \times \frac{\left(P_{i}^{2}+Q_{i}^{2}\right)}{\left|V_{i}^{2}\right|}
\end{aligned}
$$

where $P_{i}$ and $Q_{i}$ are the active and reactive power of bus $i$, and $P_{L i}$ and $Q_{L i}$ are the active and reactive load powers on bus $i$, respectively. The resistance and reactance of line parts between bus $i$ and $i+1$ are represented by $R_{l i+1}$ and $X_{l i+1}$, respectively. The power loss of the line part of the bus $i$ and $i+1$ can be calculated as follows:

$$
\begin{aligned}
& P_{L o s s}(i, i+1)=R_{L i+1} \times \frac{\left(P_{i}^{2}+Q_{i}^{2}\right)}{\left|V_{i}^{2}\right|} \\
& Q_{L o s s}(i, i+1)=X_{L i+1} \times \frac{\left(P_{i}^{2}+Q_{i}^{2}\right)}{\left|V_{i}^{2}\right|}
\end{aligned}
$$

The active, reactive and total power losses of the distribution system can be determined by summarizing the losses of all the lines in the distribution system.

$$
\begin{gathered}
P_{T, L o s s}=[B I B C] \times P_{L o s s}(i, i+1) \\
Q_{T, L o s s}=[B I B C] \times Q_{L o s s}(i, i+1) \\
T_{L o s s}=\sqrt{P_{T, L o s s}^{2}+Q_{T, L o s s}^{2}}
\end{gathered}
$$

# 6. Case Studies 

In order to evaluate the proposed algorithm, simulations implemented in 12 bus, 34 bus and 69 bus systems. The result of proposed algorithm is compared with that of the EDA and the GA. The initialization of parameters is as follows: the probability update control factor $\alpha=\beta=0.25$, the number of individuals in the initial population $s=100$, and the dominant population selection rate $M=0.4$.

### 6.1. Test System 1: 12 Bus Radial Distribution System

As shown in Figure 3, the test system consists of 12 buses and 11 branches. The total active load and total reactive load of the system are 0.4350 MVA and 0.390 MVAR. IEDA, EDA and GA are applied to DG optimal configuration problem. Figure 4 is the convergence curve of the No. 9 bus network loss optimization in the 12 bus radial distribution system obtained by IEDA, EDA and GA respectively. It is shown in the graph that the convergence rate of the IEDA is the fastest. After 70 iterations, the loss value of the network is almost converged. The convergence speed of EDA and GA is much slower than IEDA and GA. EDA iterate 120 times to stabilize and GA iterate 150 times to stabilize. In terms of network loss, IEDA is also more competitive than other algorithms. The best result obtained by IEDA is 0.0072 which is smaller than EDA's 0.0073 and GA's 0.0074 .
![img-2.jpeg](img-2.jpeg)

Figure 3. The 12 bus radial distribution system.
![img-3.jpeg](img-3.jpeg)

Figure 4. Evolution of the fitness function (total loss) with respect to number of generations for bus No. 9 in the 12 bus distribution test system.

Figure 5 is the voltage distribution of the 12 bus radial distribution system with the adoption of IEDA, EDA and GA respectively. Figure 6 is the power losses distribution of the 12 bus radial distribution system. From the graph, we can draw the conclusion that the No. 9 bus has the lowest power loss. As shown in Table 2, the best location of DG in the 12 bus radial distribution systems is the No. 9. The best result obtained by IEDA, EDA and GA is 0.2335 MW, 0.2378 MW and 0.2385 MW, respectively. Therefore, the improved algorithm has the fastest convergence speed as well as the best optimization results. Without changing the DG access capacity, this improved algorithm can obtain better results.

![img-4.jpeg](img-4.jpeg)

Figure 5. Voltage distribution of the 12 bus radial distribution system.

![img-5.jpeg](img-5.jpeg)

Figure 6. Distribution of network loss of each bus in the 12 bus radial distribution system.

Table 2. Test results of various bus radial distribution systems under different algorithms.

| Test <br> System | Total Load <br> (MVA) | $\sum P_{\text {Loss }}$ without <br> DG (MW) | Algorithm | Optimum Place <br> (bus no) | Optimum Size <br> (MW) | $\sum P_{\text {Loss }}$ <br> (MW) | Voltage <br> (p.u) |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 12 bus | $0.435+0.3900 \mathrm{i}$ | 0.145 | IEDA | 9 | 0.2335 | 0.0072 | 0.992 |
|  |  |  | EDA | 9 | 0.2378 | 0.0073 | 0.993 |
|  |  |  | GA | 9 | 0.2385 | 0.0074 | 0.991 |
| 34 bus | $4.6365+2.8735 \mathrm{i}$ | 0.1638 | IEDA | 21 | 2.9506 | 0.066 | 0.968 |
|  |  |  | EDA | 21 | 3.0023 | 0.068 | 0.969 |
|  |  |  | GA | 21 | 3.0112 | 0.070 | 0.967 |
| 69 bus | $3.8021+2.6945 \mathrm{i}$ | 0.2254 | IEDA | 61 | 1.8705 | 0.082 | 0.9815 |
|  |  |  | EDA | 61 | 2.0661 | 0.085 | 0.9835 |
|  |  |  | GA | 61 | 2.0845 | 0.087 | 0.9775 |

# 6.2. Test System 2: 34 Bus Radial Distribution System 

As shown in Figure 7, the test system consists of 34 buses and 33 branches. The total active load and total reactive load of the system are 4.6365 MVA and 2.8735 Mvar, respectively. Taking the minimization of total power loss as the objective function, IEDA, EDA and GA are used to locate and size the DG. Figure 8 is the convergence curve of the No. 21 bus network loss optimization in the 34 bus radial distribution system obtained by IEDA, EDA and GA respectively. It is shown in the graph that the convergence rate of the IEDA is the fastest. After 160 iterations, the loss value of the network is converged. The convergence speed of EDA and GA is much slower than IEDA and GA. EDA iterate 200 times and GA iterate 220 times before their convergence. In terms of network loss, IEDA is also more competitive than other algorithms. The best result obtained by IEDA is 0.066 which is smaller than EDA's 0.068 and GA's 0.07 .
![img-6.jpeg](img-6.jpeg)

Figure 7. The 34 bus radial distribution system.

Figure 9 is the voltage distribution of the 34 bus radial distribution system with the adoption of IEDA, EDA and GA respectively. Figure 10 is the power losses distribution of the 34 bus radial distribution system. From the graph, we can draw the conclusion that the No. 21 bus has the lowest loss. It can be seen from Table 2 that the best location of DG in the 34 buses radial distribution systems is the No. 21 The best result obtained by the IEDA, EDA and GA is 2.9506 MW, 3.0023 MW and 3.0112 MW respectively. Therefore, the improved algorithm has the fastest convergence speed as well as the best optimization results. Without changing the DG access capacity, this improved algorithm can obtain better results.

![img-7.jpeg](img-7.jpeg)

Figure 8. Evolution of the fitness function (total loss) with respect to number of generations for bus No. 21 in the 34 bus distribution test system.
![img-8.jpeg](img-8.jpeg)

Figure 9. Voltage distribution of the 34 bus radial distribution system.
![img-9.jpeg](img-9.jpeg)

Figure 10. Distribution of network loss of each bus in the 34 bus radial distribution system.

# 6.3. Test System 3: 69 Bus Radial Distribution System 

As shown in Figure 11, the test system consists of 69 buses and 68 branches. The total active load and total reactive load of the system are 3.8021 MVA and 2.6945MVAR, respectively. Taking the minimization of total power loss as the objective function, IEDA, EDA and GA are used to locate and size the DG respectively. Figure 12 is the convergence curve of the No. 61 bus network loss optimization in the 69 bus radial distribution system obtained by IEDA, EDA and GA respectively. It is shown in the graph that the convergence rate of the IEDA is the fastest. After 10 iterations, the loss value of the network is basically stable. EDA and GA converge appear to be much slower, EDA iterate 40 times to stabilize and GA iterate 60 times to stabilize. In terms of network loss, IEDA is also more competitive than other algorithms. The best result obtained by IEDA is 0.082 which is smaller than EDA's 0.085 and GA's 0.087 .
![img-10.jpeg](img-10.jpeg)

Figure 11. The 69 bus radial distribution system.
![img-11.jpeg](img-11.jpeg)

Figure 12. Evolution of the fitness function (total loss) with respect to number of generations for bus No. 61 in the 69 bus distribution test system.

Figure 13 is the voltage distribution of the 69 bus radial distribution system with the adoption of IEDA, EDA and GA respectively. Figure 14 is the bus losses distribution of the 69 bus radial distribution system. From the graph, we can draw the conclusion that the No. 61 bus has the lowest loss. It can be seen from Table 2 that the best location of DG in the 69 bus radial distribution systems is the No. 61 bus The best result obtained by the IEDA, EDA and GA is 1.8705MW, 2.0661MW and 2.0845MW respectively. Therefore, the improved algorithm has the fastest convergence speed as well as the best optimization results. Without changing the DG access capacity, this improved algorithm can obtain better results.

![img-12.jpeg](img-12.jpeg)

Figure 13. Voltage distribution of the 69 bus radial distribution system.
![img-13.jpeg](img-13.jpeg)

Figure 14. Distribution of network loss of each bus in the 69 bus radial distribution system.

# 7. Conclusions 

In this paper, Bayesian statistical-inference with distribution estimation creates a powerful optimization algorithm known as IEDA which reduces the total power loss and improves the voltage profile with proper allocation and sizing of DG. The global search ability of EDA algorithm is outstanding. Combined with Bayesian statistical reasoning, it can improve its convergence speed. EDA, GA and IEDA generate solutions which satisfy all the equality and inequality constraints. However, IEDA converges faster when compared to EDA and GA. The practical application and efficacy of this method was evaluated using three various common test systems (12, 34, and 69 bus). The comparative analysis of EDA, GA and IEDA methods for optimal placement and sizing of DG in a distribution system to minimize the total real power loss was successfully done. From the results, it is concluded that IEDA algorithm gives better results than EDA algorithm and GA algorithm, in terms of its accuracy and convergence speed. However, the optimum placement is identical to EDA and GA algorithms. IEDA algorithm can minimizes the real power loss simply and quickly without any complex calculations. Thus, the results obtained pave the way for new and promising research area, utilizing EDA algorithm with improvement, giving better results with high convergence speed.

In the future, to reduce the computational burden further optimal DG placement can be done by any of the recent methods such as sensitivity analysis, voltage stability consideration, loss sensitivity factor, etc. and the sizing can be done with IEDA.

Author Contributions: Conceptualization, L.Y.; Methodology, Y.W.; Project administration, X.Y.; Supervision, X.Y., Y.W. and X.L.; Validation, L.Y. and Y.W.; Writing-original draft, L.Y.; Writing-review and editing, X.Y

Acknowledgments: This work was supported in part by the National Natural Science Foundation of China (51765042, 61463031, 61773051 and 61662044), Jiangxi Provincial Department of Science and Technology (JXYJG-2017-02), Jiangxi Natural Science Foundation (20171ACB20007) and Jiangxi Provincial Department of Science and Technology (20121BBE50023 and 20133BCB22002).
Conflicts of Interest: The authors declare no conflict of interest.

# Nomenclature 

DG Distributed generation
IEDA Improved estimation of distribution algorithm
EDA Estimation of distribution algorithm
GA Genetic algorithm
$T_{\text {Loss }} \quad$ The total power loss of the radial distribution system
$P_{D G i} \quad$ The real power generation using DG at bus $i$
$P_{D i} \quad$ The power demand at bus $i$
$P_{\text {Loss }} \quad$ The line loss on the bus $i$
$U_{\text {min }} \quad$ The lower limits of voltages at bus $i$
$U_{\text {max }} \quad$ The upper limits of voltages at bus $i$
$I_{\text {max }} \quad$ The maximum current value of branch $i$
$S_{1} \quad$ The apparent power of bus $i$
$P_{i} \quad$ The active power of bus $i$
$Q_{i} \quad$ The reactive power of bus $i$
BCBV The branch-current to bus-voltage matrix
BIBC The bus-injections to branch-currents matrix
$P_{L i} \quad$ The active load powers on bus $i$
$Q_{L i} \quad$ The reactive load powers on bus $i$

## References

1. Cano, E.B. Utilizing fuzzy optimization for distributed generation allocation. In Proceedings of the TENCON 2007 IEEE Region 10 Conference, Taipei, Taiwan, 30 October-2 November 2007; pp. 1-4.
2. Keane, A.; Ochoa, L.F.; Borges, C.L.; Ault, G.W.; Alarcon-Rodriguez, A.D.; Currie, R.A.; Pilo, F.; Dent, C.; Harrison, G.P. State-of-the-art techniques and challenges ahead for distributed generation planning and optimization. IEEE Trans. Power Syst. 2013, 28, 1493-1502. [CrossRef]
3. Naderi, E.; Seifi, H.; Sepasian, M.S. A dynamic approach for distribution system planning considering distributed generation. IEEE Trans. Power Deliv. 2012, 27, 1313-1322. [CrossRef]
4. Peng, X.; Lin, L.; Zheng, W.; Liu, Y. Crisscross optimization algorithm and monte carlo simulation for solving optimal distributed generation allocation problem. Energies 2015, 8, 13641-13659. [CrossRef]
5. Devi, S.; Geethanjali, M. Application of modified bacterial foraging optimization algorithm for optimal placement and sizing of distributed generation. Expert Syst. Appl. 2014, 41, 2772-2781. [CrossRef]
6. Sheng, W.; Liu, K.Y.; Liu, Y.; Meng, X.; Li, Y. Optimal placement and sizing of distributed generation via an improved nondominated sorting genetic algorithm II. IEEE Trans. Power Deliv. 2015, 30, 569-578. [CrossRef]
7. Prakash, P.; Khatod, D.K. Optimal sizing and siting techniques for distributed generation in distribution systems: A review. Renew. Sustain. Energy Rev. 2016, 57, 111-130. [CrossRef]
8. Aman, M.; Jasmon, G.; Mokhlis, H.; Bakar, A. Optimal placement and sizing of a DG based on a new power stability index and line losses. Int. J. Electr. Power Energy Syst. 2012, 43, 1296-1304. [CrossRef]
9. Gitizadeh, M.; Vahed, A.A.; Aghaei, J. Multistage distribution system expansion planning considering distributed generation using hybrid evolutionary algorithms. Appl. Energy 2013, 101, 655-666. [CrossRef]

10. Hung, D.Q.; Mithulananthan, N.; Bansal, R. Analytical strategies for renewable distributed generation integration considering energy loss minimization. Appl. Energy 2013, 105, 75-85. [CrossRef]
11. Acharya, N.; Mahat, P.; Mithulananthan, N. An analytical approach for DG allocation in primary distribution network. Int. J. Electr. Power Energy Syst. 2006, 28, 669-678. [CrossRef]
12. Keane, A.; O'Malley, M. Optimal utilization of distribution networks for energy harvesting. Int. J. Electr. Power Energy Syst. 2007, 22, 467-475. [CrossRef]
13. Peng, X.; Lin, L.; Liu, Y.; Wang, X.; Meng, A. Optimal Dis-tributed Generator Allocation Method Based on Correlation Latin Hypercube Sampling Monte Carlo Simulation Embedded Crisscross Optimization Algorithm. Proc. CSEE 2015, 16, 4077-4085.
14. Atwa, Y.M.; El-Saadany, E.F. Probabilistic approach for optimal allocation of wind-based distributed generation in distribution systems. IET Renew. Power Gener. 2011, 5, 79-88. [CrossRef]
15. Atwa, Y.; El-Saadany, E.; Salama, M.; Seethapathy, R. Optimal renewable resources mix for distribution system energy loss minimization. IEEE Trans. Power Syst. 2010, 25, 360-370. [CrossRef]
16. Gandomkar, M.; Vakilian, M.; Ehsan, M. A genetic-based tabu search algorithm for optimal DG allocation in distribution networks. Electr. Power Compon. Syst. 2005, 33, 1351-1362. [CrossRef]
17. Wang, R.; Li, K.; Zhang, C.; Du, C.; Chu, X. Distributed Generation Planning Based on Multi-Objective Chaotic Quantum Genetic Algorithm. Power Syst. Technol. 2011, 12, 183-189.
18. Yammani, C.; Maheswarapu, S.; Matam, S.K. A Multi-objective Shuffled Bat algorithm for optimal placement and sizing of multi distributed generations with different load models. Int. J. Electr. Power Energy Syst. 2016, 79, 120-131. [CrossRef]
19. Yuvaraj, T.; Devabalaji, K.; Ravi, K. Optimal Allocation of DG in the Radial Distribution Network Using Bat Optimization Algorithm. In Advances in Power Systems and Energy Management; Springer: Berlin, Germany, 2018; pp. 563-569.
20. Seker, A.A.; Hocaoglu, M.H. Artificial Bee Colony algorithm for optimal placement and sizing of distributed generation. In Proceedings of the 2013 8th International Conference on Electrical and Electronics Engineering, Amman, Jordan, 28-30 November 2013; pp. 127-131.
21. Johan, N.F.M.; Azmi, A.; Rashid, M.A.; Yaakob, S.B.; Rahim, S.R.A.; Zali, S.M. Multi-objective using Artificial Bee Colony optimization for distributed generation placement on power system. In Proceedings of the 2013 IEEE International Conference on Control System, Computing and Engineering, Penang, Malaysia, 29 November-1 December 2013; pp. 117-121.
22. Zhao, F.; Si, J.; Wang, J. Research on optimal schedule strategy for active distribution network using particle swarm optimization combined with bacterial foraging algorithm. Int. J. Electr. Power Energy Syst. 2016, 78, 637-646. [CrossRef]
23. Kowsalya, M. Optimal size and siting of multiple distributed generators in distribution system using bacterial foraging optimization. Swarm Evolut. Comput. 2014, 15, 58-65.
24. Chen, Y.; Liu, L.G. Sizing and Locating of Distributed Generations Based on Chaos Particle Swarm Optimization Algorithm. In Applied Mechanics and Materials; Trans Tech Publications: Zurich, Switzerland, 2013; Volume 291, pp. 2119-2123.
25. Jamian, J.J.; Mustafa, M.W.; Mokhlis, H. Optimal multiple distributed generation output through rank evolutionary particle swarm optimization. Neurocomputing 2015, 152, 190-198. [CrossRef]
26. Dharageshwari, K.; Nayanatara, C. Multiobjective optimal placement of multiple distributed generations in IEEE 33 bus radial system using simulated annealing. In Proceedings of the 2015 International Conference on Circuits, Power and Computing Technologies (ICCPCT-2015), Nagykoyle, India, 19-20 March 2015; pp. 1-7.
27. Popović, Ž.; Kerleta, V.D.; Popović, D. Hybrid simulated annealing and mixed integer linear programming algorithm for optimal planning of radial distribution networks with distributed generation. Electr. Power Syst. Res. 2014, 108, 211-222. [CrossRef]
28. Salhi, A.; Rodríguez, J.A.V.; Zhang, Q. An estimation of distribution algorithm with guided mutation for a complex flow shop scheduling problem. In Proceedings of the 9th Annual Conference on Genetic and Evolutionary Computation, London, UK, 7-11 July 2007; pp. 570-576.
29. Li, D.; Peng, F.; Zhou, X.; Liu, C. Research of Batch Scheduling with Arrival Time Based on Estimation of Distribution Algorithm. In Proceedings of the 2014 Seventh International Symposium on Computational Intelligence and Design, Hangzhou, China, 13-14 December 2014; Volume 2, pp. 125-130.

30. Cai, C.; Yan, G.; Tang, J. Detection of fatigue cracks under environmental effects using Bayesian statistical inference. Int. J. Appl. Electromagn. Mech. 2016, 52, 1015-1021. [CrossRef]
31. Teng, J.H. A direct approach for distribution system load flow solutions. IEEE Trans. Power Deliv. 2003, 18, 882-887. [CrossRef]
(C) 2018 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).