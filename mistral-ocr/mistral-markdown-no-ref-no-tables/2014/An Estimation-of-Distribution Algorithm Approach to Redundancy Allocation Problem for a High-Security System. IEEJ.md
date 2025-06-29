# An Estimation-of-Distribution Algorithm Approach to Redundancy Allocation Problem for a High-Security System 

Haydee Melo ${ }^{a)}$ Non-member, Junzo Watada* Member<br>(Manuscript received Aug. 19, 2013, revised Feb. 3, 2014)


#### Abstract

Reliability is an issue that has recently captivated the attention of researchers. Its goal is to develop new techniques to design more reliable systems, which can operate without failing during operation. A result of this growth in technology is an increase in the complexity and susceptibility of more complex systems. The principal objective of redundancy allocation is to maximize the availability of a system while reducing the cost, volume or weight. This paper proposes an Estimation-of-Distribution Algorithm (EDA) approach as a new meta-heuristic method to solve a redundancy allocation problem (RAP) for a high security control system.


Keywords: reliability, availability, maintainability, redundancy, estimation of distribution algorithm, PLC

## 1. Introduction

In 1998, Blanchard defined availability as a "measure of the degree of a system to which extent the system is operable and committable at the start of mission when the mission is called for at an unknown random point in time" ${ }^{133}$. However, this definition was developed based on Barlow and Proschan's definition, given in 1975 as "the probability that the system is operating at a specified time $t^{\prime \prime 14}$. In 1977, Lie, Hwang and Tillman made a survey of a systematic classification of availability. In 1998, Mi compared the results of availability measures considering inherent availability. In 1975, Barlow and Proshman considered availability in maintenance modeling for a replacement model, Fawzi and Hawkes considered an $r$-out-of- $n$ system with spares and repairs in 1991, then in 1992, they applied availability for a series system with replacement and repair for imperfect repair models. In 1995 Murdock studied age replacement preventive maintenance models.

The redundancy of a system can make critical production services work continuously, even when some parts of the system fail. Failures bring not only production loss or economic loss but also cause severe or even lethal injuries to a society. New techniques and methods are required for reducing these failures and the expenses of the out-of-operation costs and repair costs to improve system performance. Redundancy enables us to increase the system's reliability and extend its operation time. However, understanding the causes and influence of these failures is essential to optimize the system redundancy. As a result, the study of failure is becoming an increasingly important issue.

At the same time, reliability analysis always plays a pivotal

[^0]role in keeping the level of system safety high ${ }^{125)}$. A failure of a single component in the system will affect the performance of the system or even stop its operation. Additionally, locating these failures is a time consuming task. Currently, the majority of recent approaches have focused on maximizing the reliability to ensure the continuity of system performance. One of the most used approaches is the redundancy allocation. The principal objective of redundancy allocation is to provide the corresponding redundancy level or a number of redundant components for each subsystem. However, in designing a complex system, the system consists of subsystems and each subsystem is composed of several subsystems or components.

Various designs are also constrained by cost, volume, weight and so on ${ }^{148}$. These constraints further complicate improving system reliability. In particular, the redundancy problem is an NP-hard problem where it is difficult to produce a solution with heuristic methods due to the huge search space ${ }^{158}$.
A GA has been widely used for several research studies on redundancy allocation for finding the minimal cost configuration of a series-parallel and $r$-out-of- $n$ systems under the constraints of reliability or availability. Although, GA has yielded good results in solving various NP hard problems, it does not guarantee global optimization and many modifications of the GA algorithm are necessary for each problem. GA depends on the selection of the genetic operators (such as selection, crossover, mutation, probabilities of crossover and mutation, population size and number of generations) and problem specific interactions among the genes sometimes results in premature convergence. To avoid the disruption of partial solutions the crossover recombination processes can be replaced by generating new solutions according to the probability distribution of all promising solutions in the previous generation. This new approach is called Estimation of distribution Algorithm (EDA).
The objective of this research is to propose an Estimation-of-Distribution Algorithm (EDA) approach for solving the


[^0]:    a) Correspondence to: Haydee Melo. E-mail: melo.haydee@asagi. waseda.jp

    * Graduate School of Information, Production and System, Waseda University
    2-7, Hibikino, Wakamatsu-ku, Kitakyushu, Fukuoka 808-0135, Japan

redundancy allocation problem (RAP) for a high-securitysystem, because this algorithm can yield an optimal solution for combinatorial optimization problems by predicting the movements of the populations in the search space and avoiding the several parameters associated with other evolutionary computation algorithms ${ }^{(9-17)}$. The motivation of this research is not only to develop a new formulation for the RAP but also to create an optimization model from the perspective of availability. It can assist engineers during the design phase by creating a highly reliable and available system.

The paper is organized as follows: Section 2 gives a review of previous research. Section 3 describes the mathematical formulation for a parallel-series redundancy allocation model. In Section 4 the EDA concept is explained, and the mathematical formulation for estimating the optimal solutions is illustrated. In Section 5, a real application is presented. The results are compared with the ones obtained by PSO. Finally, the results are discussed in Section 6. The conclusions are summarized in Section 7.

## 2. Previous Research

In recent years almost all of the studies on highly reliable systems have focused only on reliability without considering availability or maintainability ${ }^{(23)}$. Many approaches are used to try to solve the problem by determining the redundancy allocation with heuristics methods and meta-heuristics methods.

The RAP is an NP-hard problem. Many different mathematical approaches have been used, such as integer programming to find an optimum solution. However, the these approaches limited the search space artificially or made the problem linear, causing a loss of information and possible better solutions. Sung et al. ${ }^{(22)}$ take the redundancy optimization problem as a problem with multiple-choice and resource constraints and propose a Branch-and-Bound heuristic method. This method can narrow the solution space for solving a non-linear integer programming problem.

Rajendra et al. ${ }^{(19)}$ transform the problem into a mixed integer linear programming by involving constraints in the problem variables. Their results encourage the use of their LPbased heuristic method. However, this algorithm did not show any experimental results in large structures due to the difficulty of finding a true optimal allocation by complete enumeration.

David W. Coit et al. use a meta-heuristic approach to solve the RAP for a series-parallel system ${ }^{(20)}$. They used an example a system with 14 subsystems and with constrains on cost and weight. The problem was formulated as an integer programming one with un-separable constraints based on the the work by Fyffe et al. ${ }^{(11)}$, who used the GA to find the optimal solutions instead of the Lagrangian multiplier method. Coit also presented a column generation approach, which involves the maximization of the system's reliability by selecting components and redundancy levels based on the formulation of a constrained master problem and the generation of better possible solutions through a set of sub-problems. This approach assumes that an objective function and constrains are separable in decision variables. To use column generation the problem is decomposed into two problems: a constrained master problem and sub-problems, where each
sub-problem has a unique integer solution vector. However, the column generation did not guarantee optimal solutions because of its approximate computations. Coit and Smith ${ }^{(10)}$ introduce a multiple-weighted-objective heuristic method that transforms the problem from a multiple-objective optimization problem into a different single-objective problem. This method obtained good solution, although it is not as good as the best for the meta-heuristic.

All the methods above address the RAP only from the perspective of reliability. Another approach is to take into account the availability of the system instead of the reliability. K. K. Govil ${ }^{(12)}$ introduce the calculation of maintainability and availability for series, parallel and $k$-out-of- $n$ configurations. In this research a formulation for availability includes the calculation of the maintainability of a single device or subsystem. However, the calculation is based on mean-time-to-availability (MTTA) and mean-time-to-failure (MTTF), without calculating reliability of each component.

## 3. Problem Description

The RAP is an optimal configuration problem of a seriesparallel system that consists of $s$ subsystems in series, in which it is necessary to determine the optimum number of components for each subsystem arranged in parallel ${ }^{(25)}$ as shown in Fig. 1.

In this paper we demonstrate a mixed integer programming approach whose goal is to optimize the number of components $j$ in subsystem $i$ so that the availability $A(\mathbf{x})$ of the system is maximized for the decision variable $\mathbf{x}=$ $\left[x_{1}, x_{2}, \cdots, x_{s}\right]$ under the constraints of total cost $C$ and total weight $W$. In this formulation, $A(\mathbf{x})$ is a function of the component vector $\mathbf{x}$. As using the notations, shown Table 8, the problem can be rewritten as follows:

$$
\max _{\mathbf{x}} A(\mathbf{x})=\prod_{i=1}^{S} A_{i}\left(x_{i}\right)
$$

subject to:

$$
\begin{aligned}
& \sum_{i=1}^{S} \sum_{j=1}^{n_{i}} c_{i j} x_{i j} \leq C \\
& \sum_{i=1}^{S} \sum_{j=1}^{n_{i}} w_{i j} x_{i j} \leq W
\end{aligned}
$$

3.1 Relationship between Reliability, Availability and Maintainability Availability is the probability that the system does not fail or undergo repair and can operate when the system is required for use ${ }^{(13)}$. Availability is defined in
![img-0.jpeg](img-0.jpeg)

Fig. 1. Series-parallel system configuration

Table 1. Relationship between reliability, availability and maintainability

equation (4) by using the mean time to failure (MTTF) and mean time to repair (MTTR) to express the reliability and maintainability, respectively. Therefore, different values in these measures can result in the same availability.

$$
A(t)=\frac{M T T F}{M T T F+M T T R}
$$

Any change in reliability or maintainability affects availability, see Table 1. The availability can be calculated by using an exponential law for the failure time and repair time. In the following ${ }^{(10)(12)}$, the definition of the availability of the system consists of the reliability and the maintainability, both of which are probabilities.

$$
A(t)=1-e^{\mu t}\left(1-e^{-A t}\right)
$$

where $\mu$ is the maintenance rate, $A$ is the failure rate, $t$ is the time period, $e^{\mu t}$ stands for the maintainability and $1-e^{(t)}$ for the reliability. This formulation of availability can also be expressed as:

$$
A(t)=1-M(t)(1-R(t))
$$

3.2 Series-Parallel Configuration Out of all the possible system designs for the RAP, let us consider the design of a series-parallel system. Maximizing Eq. (6) can determine the optimal number of components in a series-parallel system. Eq. (6) is rewritten in the following equation:

$$
A(\mathbf{x})=\prod_{i=1}^{S}\left\{1-\prod_{j=1}^{n} 1-\left[m_{i j}\left(1-r_{i j}\right)\right)\right\}
$$

### 3.3 Multi-level Redundancy Allocation Optimization

The multilevel redundancy allocation model takes the hierarchical relationships among the different components into consideration. The system with the highest hierarchical level is named a master system, and the components in the lower level are named slave systems and slave components of their respective subsystems. Subsystems or components can be located in a intermediate or second level. Each system or subsystem can have a number of subordinate components or subsystems. These subordinate subsystems or components are referred to as slave subsystems or slave components, respectively ${ }^{(13)}$.

The proposed redundancy allocation model is represented in the schematic diagram in Fig. 2 for a generalized hierarchical redundancy allocation model to include the relationship of all components ${ }^{(15)(24)}$. Fig. 2 explains the allocation of a multi-level series system and the differentiation between slave components and redundant components. $S_{1}$ is the master system with slave subsystems $S_{11}, S_{12}$ and $S_{13}$, where $S_{111}, S_{112}$ and $S_{113}$ are considered slave components in the
![img-2.jpeg](img-2.jpeg)

Fig. 2. Redundancy Hierarchical level
![img-2.jpeg](img-2.jpeg)

Fig. 3. MTTR and cost relationship
slave subsystem $S_{11}$. In this multilevel configuration each component can have redundant units, and slave subsystems, so there are $S_{\text {min }}$ slave subsystems in the lower levels.

Summing all the maintainability in all levels of redundancy, the total availability can be calculated by using:

$$
A(x)=\prod_{i=1}^{S}\left\{1-\int_{j=1}^{n} 1-\left\{m_{i j}\left(1-r_{i j}\right)\right\}^{n_{i j}}\right\}
$$

3.4 Constraints Some actions are taken to avoid the stop or partial stop of the system due to an occurrence such as the repair of a component. In this case the repair actions would generate extra cost. Assuming a linear relationship between MTTR and the repair cost of components, as Fig. 3 shows, a lower MTTR indicates a higher repair cost ${ }^{(14)}$. Therefore, including the repair cost of components as a penalty for choosing a component with higher repair cost, the total cost of the system is re-formulated as follows:

$$
\sum_{i=1}^{S} \sum_{j=1}^{n}\left(c_{i j}+c_{M T T R_{i j}}\right) x_{i j}
$$

## 4. EDA Optimization

The Estimation-of-distribution algorithm (EDA) is a branch of evolutionary computation that is considered to be the next generation of population-based algorithms ${ }^{(2)}$. This algorithm incorporates knowledge of the previous studies into the search to learn about the problem structure. The EDA incorporates a learning technique by introducing a

![img-3.jpeg](img-3.jpeg)

Fig. 4. Procedure of the Estimation-of-Distributionalgorithm
probabilistic distribution to the population. Unlike Genetic Algorithm (GA) that uses mutation or crossover for generating new offspring, EDA generate the new offspring according to a probabilistic distribution learned from a population of parents (learning technique). In this paper, we use an univariate marginal distribution algorithm (UMDA). The UMDA is suited to solve combinatorial problems in which the relationships among the problem variables are unclear. Let us assume that the probability distribution of each feature is marginal. No dependence between the problem variables is taken into account when learning the factorization. Thus, the $n$-dimensional joint probability distribution factorizes as a product of $n$-univariate and independent probability distributions.
4.1 Pseudo Code The EDA replaces the search operators with the estimation-of-distribution of the selected individuals that are sampled from this distribution as shown in Fig. 3. The objective of using the estimation-of-distribution is to avoid the use of arbitrary operators (mutation, crossover) and enhance the distribution of promising solutions. After each iteration, two actions are executed: one is to pursue a population with a probabilistic distribution. After the new individuals are evaluated, the best ones are selected and their distribution is estimated. The algorithm is written as follows:

- Step 1: Randomly generate $M$ individuals (the initial population).
- Step 2: Repeat steps 3-5 for generations $l=1,2, \cdots$ until the stopping criteria are met.
- Step 3: Select $N$ individuals from $D_{l}^{l}$ according to a random selection method.
- Step 4: Estimate the probability distribution $p l(\mathbf{x})$ of each individual among the selected individuals.
- Step 5: Sample $M$ individuals (the new population) from $p l(\mathbf{x})$.
This procedure is repeated until the stopping criteria is satisfied.
4.1.1 Population The encoding of the problem uses several vectors to represent each level of the system, where $x_{i j}$ is the designed variable denoting the redundancy for the $i$-th sub-system of the $j$-th redundancy unit, where $j$ varies from 1 to $k_{i}$. Initially, the population is determined randomly. For each gene in the population, we consider the size of the subsystems in the corresponding hierarchical level of the problem as the size and range of the vector are defined as 1 as the minimum and $n$ as the maximum of components in parallel. The population is scored using the objective function. From this ranked population, the objective function selects a subset of the best solutions. Then, the algorithm constructs a probabilistic model which attempts to estimate the probability distribution of the selected solutions.

$$
p l(x)=\prod_{i=1}^{n} p l\left(x_{i}\right)
$$

4.1.2 Objective Function The objective function or fitness function has been applied to transform the constrained problem into a non-constrained problem, by including a penalty function in the objective function to restrict infeasible solutions for any violation of the constraints. To guarantee the efficiency of the optimal solution for high constrained solutions, this function is used to calculate the fitness values of the solutions obtained in each generation.

$$
\operatorname{evalf}(\mathbf{x})=A(\mathbf{x}) \times q(\mathbf{x})
$$

where, $A(\mathbf{x})$ and $q(\mathbf{x})$ are the system availability and penalty functions, respectively. We calculate the value of $q(\mathbf{x})$ for each individual. The penalty approach here adjusts the ratio of penalties adaptively at each generation to achieve a balance between the preservation of information, the selective pressure for infeasibility and the avoidance of excessive penalization.
4.1.3 Estimation In the EDA, a Gaussian distribution algorithm is usually used in the following for estimating the population distribution:

$$
p_{l}(\mathbf{x})=p l\left(\mathbf{x} \mid D_{l}^{S \text { selected }}\right)=\prod_{i=1}^{n} p_{l}\left(x_{i}\right)
$$

However, the UMDA does not consider any dependencies between its variables ${ }^{(21)}$. The problems are assumed to have no interrelation among the variables. Hence, the $n$ dimensional joint probability distribution is factorized as a product of $n$-univariate and independent probability distribution ${ }^{(7)}$. The $n$-dimensional joint probability distribution $p_{l}(\mathbf{x})$ factorizes as a product of $n$-univariate and independent probability distributions $p_{l}\left(x_{i}\right)$, that is $p l$, where $x_{i}(i=1, \cdots, n)$ represents the individual of $n$ genes and $D_{l}$ denotes the population of individuals selected from the population in the $l_{t h}$ generation. Similarly, $D_{l}^{N}$ represents the population of the $N$ individuals selected from $D_{l}$. This joint probability must be estimated every generation from one individual $\mathbf{x}$ being

among the selected individuals. Therefore, each univariate marginal distribution is estimated from marginal variables as follows:

$$
p l(\mathbf{x})=\frac{\sum_{j=1}^{N} \delta_{i}\left(X_{i}=x_{i} \mid D_{j}^{\text {Selected }}\right)}{N}
$$

where $\delta_{i}\left(X_{i}=x_{i} \mid D_{j}^{\text {Selected }}\right)=1$ if $j^{\text {th }}$ of the $D_{j}^{\text {Selected }} i^{\text {th }}$ gene is $X_{i}=x_{i}$ and 0 otherwise.
4.1.4 Sampling Function Once the probabilistic model has been estimated from the selected individuals the model is sampled to generate new individuals (new solutions). In this research the new population is sampled from a univariate Gaussian model. The objective is to sample new individuals that concentrate around the optimum solution.

## 5. High Security Facility System

This section is dedicated to the optimization of a real high security system. The system is located in a city in Northern Mexico. This control system is designated to operate the opening and closing of doors and controls of the alarm and communication systems. The system is principally composed of a control system, sensors, magnetic actuators, humanmachine interface (HMI) and communication network between the different areas. The facility is a three-story building, each floor is divided into 9 sections ( $V_{0}$ to $V_{9}$ ) as depicted in Fig. 5. In each sections there is a security room where several zones are monitored and by the security experts. In sections $V_{0}$ and $V_{1}$, the security room that access to the control room is located. In section $V_{2}$ is the access to the hallway to the control system. The section $V_{3}$ and section $V_{9}$ control and monitor the access to the machine room and storage room respectively. In section $V_{4}$, the security room that controls and monitors the access to the hallway for accessing for the following sections $V_{5}, V_{6}, V_{7}$ and $V_{8}$ that controls and monitors the adjacent zones (Zone 1 to Zone 9).

The master system is located at $V_{0}$ where it is responsible for access to the machine room, the general storage room, and their respective secure rooms, monitoring and alarm recordings and the information to PCs. The slave systems are located in the different sections for controlling the adjacent
![img-4.jpeg](img-4.jpeg)

Fig. 5. High-safety system layout
zones.
The control system has an hierarchy structure that is divided in 3 levels as depicted in Fig. 6, where each level is responsible for the control of a group of sections. The Functional structure of the high security control system is depicted in Fig. 7.

The system has a PC and a master PLC (Programmable Logic Controller) with 7 identical slaves PLC's that each control another slave PLC. Each slave PLC is a control subsystem with different components: CS1-PA207R (power supply), CS1-CPU67H (CPU), S8VS-090 (power supply), CS1IC102D (analog input model), CS1-ID261 (digital input) and CS1-OD261(digital output); see Table 2. Each component is critical and indispensable to each subsystem, and a malfunction of any component may interrupt the data communication and hence cause a loss of control of the subsection.
(1) Slave system 1 (containing CPU1). This slave subsystem controls sections $V_{0}$ which and $V_{1}$, where the control room is located, coordinates the communication between the others CPU and the control room, and controls the principal access to the facility.
(2) Slave system 2 (containing CPU2). This slave system controls access in section $V_{2}$ and part of section $V_{4}$, with 26 doors in total, communication system and the movement sensors.
(3) Slave system 3 (containing CPU3 \& CPU4). This slave system has a slave subsystem, both control 193 doors in sections $V_{5}$ and $V_{6}$; these sections are integrated with 24 movement sensors and 193 intercoms for the communication system.
(4) Slave system 4 (CPU5 \& CPU6). This slave system has also a slave subsystem, both control 257 doors that correspond to sections $V_{7}$ and $V_{8}$, respectively. They also receive the signals from 18 movement sensors and control the communication in these two sections.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Three level system

![img-6.jpeg](img-6.jpeg)

Fig. 7. Master-slave-slave system diagram
( 5 ) Slave system 5 (containing CPU7). This slave system controls 55 doors in section $V_{9}$ on the 3 levels, 12 movement sensors and 59 intercoms for the communication system, and alarm system respectively.
(6) Slave system 6 (containing CPU8). This slave system controls sections $V_{2}$ and $V_{3}$ and is integrated with 31 doors. It also receives the signal from 8 movement sensors and the communications between the doors.
The automation company that proposed the design of the control system need to establish a redundant system to improve the reliability and ensure the performance of the system. However, the facility has already installed a system and is considering replacing the repaired components with the new components. In this case, the availability is used to calculate the number of components that are necessary to enhance the performance of the system.

Then, we obtained the MTTR and MTTF data based on the manufacturer's data, to calculate the reliability and maintainability, respectively. The data were provided by the manufacturer and the company that designed the system, as described
in Tables 2, 3 and 4. In this system, the only constraint is the cost of the redundancy; the engineers designed the system to have $30 \%$ of the total modules as extras to provide a backup for system performance. The total budget of the system is set to $\$ 1,200,000.00$ as a constraint. The maximum number of components that are allowed for each module is 8 .

The system has three different levels of components. It is difficult to determine the optimal number of components in parallel. This calculation is to maximize the availability of the system. However, it is necessary to set the number of components at the lowest level first, then the upper levels are calculated. This system is in a master-slave configuration. However, the system is divided in 3 levels of hierarchy where the top level is a master level and the lower levels are the slave subsystems. We can re-divide this problem into three vectors that represent each level of the system. Then, we determine the lowest level of redundancy because there are no slave components in this level. Then, we determine the number of components in the second level and use the lowest level to calculate the fitness of the second level. Subsequently, in

Table 2. Safety Control System Component Function

Table 3. Safety Control System MTTR AND MTTF

the top level we use both results to obtain the number of components in parallel that maximize the availability of the entire system.

The data used for each component in the system are given in Tables 3 and 4.

## 6. Results

The program was run in MATLAB on an Intel Core ${ }^{(T M)} 2$ Duo 3.00 Hz CPU with 4 GB in RAM. Tables 5 and 6 show the best results for 50 independent runs; there were 20 variables for this problem, with a population of 100 and a maximum of 100 generations. The objective is to find the optimal number of components that are necessary for redundancy with the maximum of availability at each level of the system

Table 4. Cost and Number OF Components for Each Model in The System

Table 5. Availability Results

and its respective cost constraint.
Recently many meta-heuristics such as PSO and Tabu search have been employed for the reliability-redundancy optimization problems. These approaches have been demonstrated to yield good solutions in the Reliability Allocation Problem (RAP). The meta-heuristics have some advantages. PSO is one of the most recent stochastic methods developed for solving optimization problems. PSO is a populationbased meta-heuristic optimization technique that converge rapidly around the global optimization. TS has the ability to escape the trap of the local optimum and have good local search. TS have been employed to solve some reliability problems, such as series-parallel systems and it also demonstrated its efficiency in finding the optimal solution for the redundancy allocation. The PSO and TABU Search (TS) were used to compare and evaluate the solution by the EDA. However these algorithms never been used in real applications problems and with components that have been repaired. Tables 5 shows the availability archived by each algorithm in effective digits and Table 6 shows the total cost of the system

Table 6. Cost Results

Table 7. Convergence results of 50 runs
achieved for each algorithm.
The PSO used for the comparison was a canonical one. The learning rate for the swarm was $c_{1}=0.738$ and $c_{2}=1.51$. The size of the swarm was set to 100 the number of informants; in other words, exploration was allowed. The TS used for the comparison the classical TS, with the Tabu tenure is set to 6 and the number of neighborhoods is set to 841 . The size of the search space was set to 100 .

The solutions obtained for EDA, PSO and TS for availability and cost are shown in Tables 5 and 6 for the master system and the following subsystem and its respective subsystems. The components reliability and maintainability are high; as a result, the calculation of the availability is also high. Therefore, the resulting availability is shown as a probability between 0 and 1 , with significant digits. To have a better appreciation of the result, the values are presented in this form. The results in Tables 5 and 6 are the best 10 results among the 50 runs results of each method.

However, the highest system availability achieved by EDA as 0.9999 in several runs. The Tables show the cost of the allocated components in parallel for the entire system, where we observed that the highest cost is achieved by EDA. Although the cost in the PSO solution was lower than the one achieved by the EDA, this was the result of the total number of redundant components selected in the system.

Also, Tabu search achieve lower cost than the EDA due to the number of components allocated in parallel for each component in each subsystem. Increasing the number of components also increase the availability and the cost, however in EDA the components with lower maintainability have higher priority in the selection of the number of components in Parallel, and their hierarchy in the system, taking into account the importance in the system.

Statistical analysis for the 3 methods in 50 runs for the high security facility are summarized in Table 7. By using the results in Table 7, in terms of mean and best result, the solution
of EDA are better than the solutions found by PSO and TS methods for the redundancy allocation problem. In addition, the standard deviation of the results by EDA in 50 independents runs is also very small. When pursued by BehrensFisher's method, the t-test result supports that EDA is better than PSO and TS with significant level $1 \%$.

## 7. Discussion

The EDA is an innovative method that has not been widely applied in various academic fields. It has proved effective for combinatorial problems such as scheduling problems. In this research, an EDA was used for a reliability allocation problem to maximize the availability of the system. A Gaussian univariate distribution was implemented to find the best combination of components for the high security control system. The EDA yielded good solutions due to their learning technique introduced in the algorithm by introducing a probabilistic distribution into the population. The algorithm learned from the problem structure to find the best combination for a number of components and obtained an optimal solution in a small number of generations. This paper introduced a real application with a three level system; due to the system complexity, it was necessary to modify the equation to evaluate the entire system availability by setting the lower levels' availability to find the the upper levels' availability and, as a consequence the system optimum allocation.

Compared with PSO and TS, the EDA resulted in a superior performance in terms of solution quality and CPU time. Furthermore, the random mechanisms of crossover and mutation were avoided by the EDA approach and replaced by an estimation of the probability distribution, which exploits the search of promising solutions, at each run.

Compared to the EDA, the classical PSO used in this research had low convergence speed and prematurity that made the solution to converge to local optima; deciding the values of various parameters, such as the size of the swarm, the coefficients and the number of informants, depends on the user's experience. This fact makes it difficult to tune the parameters to achieve better results.

TS is an algorithm that uses memory-based strategies. TS starts from an initial solution, and at each step, a neighbor solution is chosen to improve the objective function value. However, this algorithm does not guarantee the optimum solution, and experimental results showed that it is not successful in finding near-optimum solution due to missing promising solutions in the search space, and the lack of information exchange between neighbors.

For PSO and TS to yield good solutions, it is necessary to modify both algorithms to achieve better efficacy.

## 8. Conclusions

Redundancy allocation optimization problems are often encountered in complex system designs. This paper proposed a new formula that takes into account the availability, instead of the reliability, of a system.

The availability of a system with repairable components provides a measure of the performance of all the components in the system by including the failure rate from the repaired components. Therefore, the system can be designed with components that have high MTTF with respect to MTTR, and

Table 8. Notations
maintenance time can be reduced by selecting elements with low MTTR.

In real life applications, systems are not only composed of new components but also repaired ones. In this case, the reliability is not a suitable measure for repaired components, and it is necessary to take into account the failure rate. A new series-parallel redundancy allocation mathematical model is formulated to maximize the system availability. This mixed integer problem is difficult to solve even by the heuristics method; therefore we proposed the EDA approach as a recently developed meta-heuristic method. We applied the EDA, PSO and Tabu Search algorithms, separately, to solve a high-security system redundancy allocation optimization problem. The optimal solution for this problem demonstrated that the EDA yields an optimal system availability that is better than the PSO and TS results, because the EDA learned from the structure of the problem. For future work, a more complex applications will be considered. Although the RAP can also be considered as a multi-objective problem, the EDA could be used to find the optimal set of solutions for this problem.

## Appendix

Haydee Melo was supported by the Ministry of Education, Culture, Sports, Science and Technology (MEXT) scholarship program for international Students. This work was supported in part by Grants-in-Aid for Scientific Research, MEXT (No.23500289).

Haydee Melo (Non-member) received the B.Sc. degree in Electro-
![img-7.jpeg](img-7.jpeg)
mechanics engineering from National Polytechnic Institute (IPN), Mexico and the M.Sc. degree from the Graduate School of Information, Production and Systems, Waseda University, Japan. She is currently a Doctor student in Graduate School of Information, Production and Systems, Waseda University, Japan as a scholarship recipient student from the Ministry of Education, Culture, Sports, Science and Technology, Japan. Her research interests include soft computing,
management engineering, reliability and Meta-heuristic algorithms.

Junzo Watada (Member) received his B.S. and M.S. degrees in electrical engineering from Osaka City University Japan, and Dr. of Engineering on "Fuzzy Multi-variant Analysis and Its Applications" from Osaka Prefecture University, Japan. His professional interests include soft computing, tracking system, knowledge engineering, and management engineering. Prof. Watada is a recipient of the Henri Coanda Gold Medal from Invention in Romania in 2002. He is a Life Fellow of Japan Society for Fuzzy Theory and intelligent Informatics (SOFT) and Biomedical Fuzzy System Association (BMFSA). He is the Principal Editor, Co-Editor, or Associate Editor of various international journals, including the International Journal of Biomedical Soft Computing and Human Sciences, ICIC Express Letters, the International Journal of Systems and Control Engineering, and Fuzzy Optimization and Decision Making.