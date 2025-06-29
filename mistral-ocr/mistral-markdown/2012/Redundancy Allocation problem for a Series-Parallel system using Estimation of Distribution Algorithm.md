# Redundancy Allocation problem for a Series-Parallel system using Estimation of Distribution Algorithm 

Haydee Melo<br>Graduate School of Production,<br>Information and Systems<br>Waseda University<br>2-7 Hibikino, Wakamatsu, Kitakyushu<br>Fukuoka, Japan<br>melo.haydee@asagi.waseda.jp


#### Abstract

Reliability is an engineering field that recently has captivated the attention of researches. Its goal is to develop new techniques to improve the security and performance of the systems. The increasing complexity in the systems as a result of growing technology makes them more susceptible for failures. In the redundancy allocation problem (RAP) its principal objective is to maximize the availability while reducing the cost, volume or weight of the system. In this research an Estimation-ofDistribution Algorithm (EDA) approach is proposed for solving the redundancy allocation problem for a series-parallel system.


Index Terms-Reliability, Availability; Maintainability, Redundancy, Estimation of Distribution Algorithm.

| Nomenclature |  |
| :--: | :--: |
| $S$ | Number of subsystems in the system |
| $n$ | Number of components in the subsystem |
| $r_{i j}$ | The reliability of each component in the subsystem |
| $m_{i j}$ | The maintainability of each component in the subsystem |
| $a_{i j}$ | The availability of each component in the subsystem |
| $A$ | The system availability |
| $w_{i j}$ | The weight of each component in the subsystem |
| $c_{i j}$ | The cost of each component in the subsystem |
| $x_{i j}$ | The number of components in the subsystem |
| $C$ | The upper limit on the cost of the system |
| $W$ | The upper limit on the weight of the system |
| $c_{M T T R_{i j}}$ | The components repair cost |
| $W$ | The upper limit on the weight of the system |
| $R_{i}$ | The reliability of the subsystem i |
| $M_{i}$ | The maintainability of the subsystem i |
| $a_{i}, b_{i}$ | Coefficient of functional relationship between manufacturing cost and MTTR of component i |

## I. InTRODUCTION

Redundancy is used to offer protection and safety to the system by keeping the critical production services working even though some parts of the system fails. To improve system performance is necessary to increase its reliability by increasing the design lifetime, eliminating or reducing the failures or risks, and increasing its operation time. Failures lead not only production or economic loss but also cause severe or even lethal injuries. The need of reducing and dealing with these failures and the cost as a result of the loss of operation and repairs, pointed the necessity to develop new techniques and methods according to their complexity. However without understanding the causes and effects of these failures in the systems become difficult to optimize the system. As a result the study of failure becomes an increasingly important issue. At the same time the reliability analysis demonstrated to be a useful tool for the engineers to assess the level of safety in the system. Nowadays the research studies are focused on designing more reliable systems that ensures the performance and safety as well. The majority of recent approaches focus on maximizing the reliability to ensure the system performance. There are many approaches that try maximizing the reliability; one of the most used is the redundancy allocation. Designing a system is complex. A system consists of subsystems where each subsystem also can be divided in several subsystems or components making more susceptible to failures. A failure in one single component in the system would affect the performance of the system or even stop its operation. Also the locationing of these failures is time consuming.In the redundancy allocation problem (RAP) its principal objective is to maximize the reliability or the availability by assigning the corresponding redundancy level or number of components in each subsystem. The design is made under constraints as cost, volume or weight that made the system reliability difficult to be improved. Therefore the redundancy problem is considered a NP-hard problem where classical heuristic methods failed to solve due to the large search space. [2]

In this research an Estimation of Distribution Algorithm (EDA) approach is proposed for solving the redundancy allocation problem for a series-parallel system based on the results that this algorithm has yield with combinatorial problems and optimization problems. Even though classical meta-heuristics had proved to yield good results as GA global optimum is

not guaranteed and many modifications in the algorithms are needed to be done. The motivation of this research is not only to develop a new model for the redundancy allocation problem but also to create an optimization model by using the Estimation-of-Distribution-Algorithm advantages to assist engineers during the design phase for creating a system with high reliability and availability.

## II. PREVIOUS RESEARCH

In recent years almost all of the studies focused only in the reliability problem forgetting about availability or maintainability. There are many approaches that try to solve the problem by determining the redundancy allocation, as heuristics methods and meta-heuristics methods. However the determination of redundancy of a Parallel-Series is difficult as Chern [2] demonstrated. The redundancy problem is a NPHard problem, many approaches used the integer programming in order to find the optimal solution, however the search space is limited causing lost of information and possible better solutions. Another Heuristic method used for solving this problem is Branch-and Bound proposed by Sung et al. [5], considering that the redundancy optimization problem has multiple-choice and resource constraints. The problem is a non-linear integer programming as consequence of the proposed method; the solution space is reduced as a procedure. Radreja et al. [3] considered to find an allocation that minimize the sum of the absolute differences of cut-set hazard values from their averages by transforming the problem into a mixed integer linear programming involving constraints in its variables. His results encourage the use of his LP-based heuristic method, however this algorithm is not considered for experimentation in large structures due to the difficulties in finding a true optimal allocation by complete enumeration. David W. Coit et al. [4] used a Meta-heuristic approach to solve the redundancy allocation problem for a series-parallel system. They considered a system with 14 subsystems and with constrains on cost and weight. In this problem is formulated as integer programming with un-separable constraints and use the Fyffe, Hines Lee [4] where they used a Langragian multiplier with dynamic programming instead of langragian multiplier, they used GA to find the optimal solutions. Coit also presented a Column Generation Approach which involves the maximization of the system reliability by selecting components and redundancy levels based on the formulation of a restricted master problem and generation of possible better solutions through a set of sub-problems. In this approach it is considered that the objective function and constrains are separable in decision variables. In order to use Column Generation the problem is decomposed into two problems: a restricted Master Problem and Sub-problems, where each sub-problem has a unique integer solution vector. However Column Generation did not guarantee optimal solutions because of the approximation. A multiple weighted objectives heuristic method was introduced by Coit [8], where he considered a multiple components. This method is based on the transformation of the problem from a multiple objective optimization problems, and transformed
into a different single objective problem. The method achieved good solution although still not as good as the one achieved for the meta-heuristic. All the methods above consider only reliability for the Redundancy Allocation Problem; another approach is to take account to the Availability of the system instead of the Reliability. K.K. Govil [10] introduced the calculation for maintainability and availability calculations for series, parallel and r-out-of-n configurations, in this research a formulation for availability that includes the calculation of the maintainability of a single device or subsystem. However, the calculation is focused on calculating the MTTA (Mean-time-to-availability) and the MTTF (mean-time-to-failure, without the calculation of the reliability of each component.

## III. Problem Description

The growing complexity of the equipment and systems, as well as the rapidly increasing cost incurred by loss of operation and for maintenance, have brought to the fore the aspects of reliability, maintainability, availability, and safety. The expectation today is that complex equipment and systems are not only free from defects and systematic failures at time $t=0$ (when they are put into operation), but also perform the required function failure free for a stated time interval. However, the question of whether a given item will operate without failures during a stated period of time cannot be simply answered by yes or no on the basis of a complicated test. Experience shows that only a probability for this occurrence can be given. This probability is a measure of the item's availability. The Redundancy allocation Problem is considered as a series-parallel system. In this design there are $s$ subsystem where is necessary to determine the the optimal selection of number of components for each subsystem arregended in parallel. The goal is to optimally the number of components $j$ in subsystem $i$ so the availability of the system at decision variable $x, A(x)$, is maximized, considering cost and weight constraints. In this formulation $A_{i}\left(x_{i}\right)$ is a function of the component vector $x_{i}$. The problem can consider as follows:

$$
\max _{x} A(x)=\prod_{i=1}^{S} A_{i}\left(x_{i}\right)
$$

subject to:

$$
\begin{aligned}
& \sum_{i=1}^{S} \sum_{j=1}^{n} c_{i j} x_{i j} \\
& \sum_{i=1}^{S} \sum_{j=1}^{n} w_{i j} x_{i j}
\end{aligned}
$$

## A. Relaiability, Availability and Maintainability relationship

Availability is defined as the chance that a system will operate as designed or required without the risk that the system will not operate [16]. In other words the availability is the probability that the system is not failed or undergoing a repair and operates when the system is required for use. Availability is calculated in equation (4) by using the MTBF and MTRR

that are used to calculate the Reliability and Maintainability respectively.

$$
A(t)=\frac{M T B F}{M T B F+M T T R}
$$

TABLE I
RELATIONSHIP BETWEEN RELIABILITY, AVAILABILITY AND Maintainability

| Reliability | Availability | Maintainability |
| :--: | :--: | :--: |
| Increase | Increase | Constant |
| Decrease | Decrease | Constant |
| Constant | Increase | Increase |
| Constant | Decrease | Decrease |

Reliability and Maintainability are defined as a function of the Availability, some decrease or increase on these affect the Availability as shwon in table II. Availability combines the Reliability that is the probability of a component to function as specified and maintainability that is the probability that a component will be repaired to their full operational state given a period of time. However different values in these measures would have the same availability. The availability also can be calculated using the exponential law for the failure time and repair time, assuming that the availability is the probability of a component to function as specified. Analyzing the definition, the concept combines the reliability and maintainability, both of which are probabilities, the availability is calculated in the following [8],

$$
A(t)=1-e^{\mu t}\left(1-e^{-\lambda t}\right)
$$

where $\mu$ is the maintenance rate and $\lambda$ is the failure rate and $t$ is the time period [8]. The maintainability is calculated as $e^{\mu t}$ stands for the Maintainability and $-e^{\lambda t}$ for reliability this formulation can also be expressed as:

$$
A(t)=M(t)(1-R(t))
$$

## B. Reliability Block diagram

In order to determine the availabity of the system, the reliability block diagram is a useful tool that help to understand which elements are required for the system to function without failures that affect it. The reliability block diagram analyzes the function of each component and its role in the system and how it affects the entire system in case of a failure. This diagram is also used to determine the elements that are necessary in the allocation of the redundancy. Among all the possible system designs for the RAP, we consider the series-parallel system. Fig. 1 depicts an example of such system.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Reliability Block Diagram

1) Series Configuration: A series configuration is used when the necessary elements for the system are connected to each other. In case one of the components fails the system fails. The success of the performance of the system is determined by the success of all the components. Hence the reliability, maintainability and availability of the system are calculated as the product of all the components reliability, maintainability and availability. The products of all components are assumed to be independent each other with the same failure rate.
2) Parallel Configuration: In contrast with the series configuration, the elements in parallel are considered less important than the ones in series. Even if one of the elements failures, it does not affect the performance of the system. This configuration is used to allocate the redundant components.

TABLE II
BASIC CONCEPTS OF AVAILABILITY, RELIABILITY AND MAINTAINABILITY

| Reliability Diagram Block |  |  |
| :-- | :--: | :--: |
|  | Series | Parallel |
| Reliability | $R(t)=\prod_{i=1}^{S} R_{i}$ | $R(t)=1-\prod_{i=1}^{S} 1-R_{i}$ |
| Availability | $A(t)=\prod_{i=1}^{S} A_{i}$ | $A(t)=1-\prod_{i=1}^{S} 1-A_{i}$ |
| Maintainability | $M(t)=\prod_{i=1}^{S} M_{i}$ | $M(t)=1-\prod_{i=1}^{S} 1-M_{i}$ |

The formulas to calculate the Availability, Maintainability and Reliability of the system for each configuration in the RBD are given in table II . Therefore, by using the eq. (6) for a single component and the formulas in table II, the number of $x_{i j}$ components necessary in parallel in a series-parallel system is represented as follows:

$$
\max _{x} A(x)=\left[1-\left[\prod_{i=1}^{S} 1-\prod_{j=1}^{n} 1-\left[m_{i j}\left(1-r_{i j}\right)\right]^{x_{i j}}\right]\right]
$$

## C. Constraints

Desingning a system, our goal is not only to achieve a higher availability, but also the designer has to take into account the total cost and the weight of the system or other constraints in the design.
![img-1.jpeg](img-1.jpeg)

Fig. 2. MTRR and cost relationship
In this case the cost formula only consider the cost of each component in the system, but in a system when a failure or certain component in the system may had a malfunction that lead to the stop or partial stop of the system, there are some action that are taken to avoid such occurrence as the repair of the component. In this case the repair actions would generate extra cost. Assuming a linear relationship between MTTR and the repairing cost of components as fig. 2 shows, a lower MTTR indicates a higher repairing cost [11].Therefore the cost is re-formulated as follows, including the cost of the components repair as a penalty for choosing a component with higher MTTR.

$$
\sum_{i=1}^{S} \sum_{j=1}^{n}\left(c_{i j}+c_{M T R R_{i j}}\right) x_{i j}
$$

## IV. Estimation of Distribution Algorithm (EDA) OPTIMIZATION

Previous researches try to limit this space by heuristic methods but the best solutions for this problem are achieved by the Evolutionary algorithms. GA have been used to solve in the past many difficult engineering problems and are particularly effective for combinatorial optimization problems with large, complex searches as the redundancy allocation problem, although the optimality cannot be guaranteed. In this research an Estimation Distribution Algorithm is proposed for solving this combinatorial problem due to its ability to find good solutions efficiently and learning from the problem itself. The estimation of distribution algorithm (EDA) is a branch of the evolutionary computation that is considered to be the next generation in these population-based algorithms. The EDA integrate the learning to the algorithm, with this estimation the previous knowledge is incorporated into the search. Finding optimal solution in the Reliability Allocation Problem is not an easy task due to the large search space.One of the most
interesting algorithms is Estimation of Distribution Algorithms where it used a probabilistic model to give to the chromosome that contains partial good solution the high probability of being preserved in the child chromosome.

## A. Comparison with GA

The Estimation of Distribution Algorithm was developed along the lines of the Genetic Algorithms. Therefore the Estimation of Distribution Algorithm uses the basic concept of the Genetic Algorithm as the population, and applies some modifications to this algorithm. From the population a probability distribution for each variable could be estimated (over good solutions). These distributions can then be used to generate future individuals. Estimation of Distribution Algorithm changes the cross-over and the mutation for estimation of the distribution. Therefore the algorithm can also learn about the problem to find the optimal solution. One of the principal advantages of this algorithm is the absence of multiple parameters to be tuned. This algorithm yields to solve complex problems more efficiently and more reliable because their model move the search away to the area of promising solutions. The principal advantages of EDAs over genetic algorithms are the absence of multiple parameters to be tuned. Models can be more easily visualized than a dynamic population in a conventional Evolutionary algorithm.

## B. Pseudo Code

The Estimation of Distribution Algorithm replaces the search operators with the distribution estimation of the selected individuals that are sampled from this distribution as shwon in fig. 3. The objective is to avoid the use of arbitrary operators (mutation, crossover) and explode the distribution of promising solution. The Estimation of Distribution Algorithm pseudo code or steps is as follows:

- Step 1: Generate randomly M individuals (the initial population)
- Step 2: Repeat steps 3-5 for generations $l=1,2, \ldots$ until the stopping criteria met
- Step 3: Select $N \leq M$ individuals from $D_{i-l}$ according to a selection method
- Step 4: Estimate the probability distribution $p l(x)$ of an individual being among the selected individuals
- Step 5: Sample M individuals (the new population) from $p l(x)$

The solutions distribution estimation incorporate the previous knowledge into the search. After each iteration, two actions are executed: one is to generate a population with a probabilistic distribution. The second is after the new individuals are evaluated, the best ones are selected and its distribution is estimated.

1) Population: For a given population $p$, the initial population was determined by randomly selection $p$ solution vector. For each vector we considered the total number of subsystems in the problem and the range of the the subsystems are 1 as minimum and $n$ as the maximum of components in parallel. We use a integer values encoding of the solutions for the combinatorial optimization because is more efficient. Each solution, $S$ integers between w and $n$ were randomly selected to represent $n$ for a particular subsystem. Therefore the solutions encoding is a vector representation with the combination of components that are located in parallel for each subsystem.
2) Objective function: The objective function was the the calculation of the availability of system determined by the equation (4). It is important to guarantee the efficiency of the optimal solution for high constrained solutions This function is used to obtain the fitness values of the solutions obtained by the algorithm at each generation. The average fitness of the population at each generation is used to evaluate the behavior of the algorithm, the increase in the value means that the algorithm getting better solution.
3) Estimation: For this particular problem formulation a univariate Gaussian distribution algorithm (UMDA) is used with the following probability distribution:

$$
p l(x)=p\left(x \mid D_{l-1}^{\text {Selected }}\right)=\prod_{i=1}^{n} p_{l}\left(x_{i}\right)
$$

The UMDA does not consider any dependencies between its variables [16]. It is assumed there is no interrelation among the variables of the problems. Hence the n-dimensional joint probability distribution is factorized as a product of n -univariate and independent probability distribution [15]. The simplicity in the model helps to achieve good results in combinatorial problems. The UMDA assume that the $n$-dimensional joint probability distribution factorizes like a product of $n$ univariate and independent probability distributions, that is $p_{l}$, where $x_{i}(i=1, \ldots, n)$ represents the individual of $n$ genes and $D_{l}$ will denote the population of individuals from the population in the $l^{1} h$ generation. Similarly, $D_{l}^{N}$ will represent the population of the selected $N$ individuals from $D_{l-1}$. This joint probability must be estimated every generation over one individual $x$ being among the select individual. The basic idea consists in inducing probabilistic models from the best individuals of the population.
4) Sampling function: Once the probabilistic model has been estimated the model is sampled to generate new individuals (new solutions), which will be used to generate a new model in the new generation. This procedure is repeated until the stopped criteria is satisfied. The type of sampling method is therefore dependent on the class of probabilistic method used. In order to guarantee the feasibility of solution
we used a repair method that modifies a given individual to guarantee that the constraints are satisfied.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Procedure of Estimation-of-the-Distribution-algorithm

## V. NUMERICAL EXAMPLE

The experiment was carried out to test the performance of the Estimation-of-Distribution-Algorithm, using a system with 20 subsystems as shown in fig. 4 , where it is necessary to determine the number of components in parallel. The maximum number of components for each subsystem is 8 . The cost and the weight upper bounds are set to 250 .
![img-3.jpeg](img-3.jpeg)

Fig. 4. A considered parallel-series system

TABLE III
NUMERICAL EXAMPLE DATA

|  | Data for each subsystem |
| :-- | :-- |
| Reliability | $[0.81,0.82,0.97,0.98,0.96,0.83,0.80,0.80$, |
|  | $0.82,0.97, \quad 0.80,0.93,0.87,0.92,0.81,0.97$, |
|  | $0.95,0.85,0.86,0.98]$ |
| Maintainability | $[0.94,0.89,0.85,0.83,0.80,0.98,0.86,0.82$, |
|  | $0.93,0.92, \quad 0.87,0.81,0.93,0.82,0.96,0.80$, |
|  | $0.84,0.82,0.91,0.95]$ |
| Cost | $[3,3,1,2,3,1,1,3,2,2,1,2,1,3,2,1,1,3,2,1]$ |
| Repair Cost | $[5,2,3,1,1,4,3,2,1,2,4,2,2,5,3,3,1,2,3,2]$ |
| Weight | $[4,2,5,3,3,3,2,6,7,5,3,6,4,6,3,7,5,2,7,8]$ |

The data used for each component in the system is as follows:

## VI. RESULTS

The program is run in MATLAB in a Intel Core (TM) 2 Duo CPU 3.00 Hz and 4GB in RAM. For 50 generations. The number of variables was 20 for this problem, with a population of 100 and a maximum of 100 generations. However the EDA reach the optimal solution at the 50 generation.

TABLE IV
NUMERICAL EXAMPLE DATA

|  | Best solution |
| :-- | :-- |
| Number of components | $[5,3,3,1,2,1,3,1,2,2,4,1,3,1,4,1,3$, |
|  | $1,2,1]$ |
| Total Cost | 203 |
| Total Weight | 183 |
| System Availability | 0.999818278 |

## VII. DISCUSSION

The Estimation of distribution Algorithm is a new algorithm that has not tested in different fields or applications. In this research an Estimation-of-Distribution-Algorithm for a Reliability allocation Problem with high Availability and Maintainability is presented. A Gaussian Univariate Distribution is implemented and the preliminary results are presented. Although a preliminary result is presented, the algorithm seems to yield good solutions. The algorithm learn from the problem structure in order to find the best combinations for the number of components and get a optimal solution in small number of generations, however the search space for this problem is not so large so it is necessary to tested in a large space.

## VIII. CONCLUSION

For future work, a multi-choice component for the redundancy allocation, using components with different reliability and maintainability values. A real application is considered. Also, a comparison with other meta-heuristic methods for the redundancy allocation, such as PSO and GA is considered in
order to test the performance of the EDA. The RAP can also be considered as a multi-objective problem and the EDA could be used to find the optimal set of solutions for this problem.

## REFERENCES

[1] Armen Der Kiureghian, Ove D. Ditlevsen, Junho Song, "Availability, reliability and downtime of systems with repairable components", Reliability Engineering and System Safety, vol.92, no. 2, pp. 231-242, 2007.
[2] V. Rajendra Prasad, M. Raghavachari, Optimal Allocation of Interchangeable Components in a Series-Parallel System, IEEE Transactions on Reliability, vol. 47, No. 3, pp. 255-260, 1998.
[3] David W. Coit and Abdullah Konak, Multiple Weighted Objectives Heuristic for the Redundancy Allocation Problem, IEEE Transactions on Reliability, vol. 55, no. 3, pp. 551-558, 2006.
[4] Leila Zia and David W. Coit, Redundancy Alloction for Series-Parallel systems using a Colum Generation approach, IEEE Transactions on Reliability, vol. 59, no. 4, pp. 706-717, 2010.
[5] Sung Chang Sup and Cho Yong Kwon, Branch-and-Bound Redundancy Optimization for a Series System with Multiple-choice constraints, IEEE Transactions on Reliability, vol. 48, No. 2, pp.108-117, 1999 June.
[6] W. T. Yang and C. C. Lin, A reliability model for dependent failures in parallel redundant systems,IEEE Trans. Reliability, vol. R-23, no. 3, pp. 286287, 1974.
[7] N. Jack, Analysis of a repairable 2-unit parallel redundant system with dependent failures, IEEE Trans. Reliability, vol. R-35, no. 4, pp. 444446, 1986.
[8] David W. Coit and A.E. smith, Reliability optimization of series-parallel systems using genetics algorithm,IEEE Transactions on Reliability, vol. 45, no. 2, pp. 254-260. 1996.
[9] K.K. Govil, Maintainability and Availability calculations for series, parallel, and r-out-of n configuration, Microelectron, Reliability, vol. 23, no.5, pp. 785-787, 1983.
[10] S.P. Sharma, Dinesh Kumar and Ajay Kumar, Availability optimization of a series-parallel systems using genetic algorithms, in Proc. XXX National systems conference, NSC 208, pp. 640-644, 2008.
[11] Y.S. Juang, S.S. Lin and H.P. Kao, A knowledge management system for series parallel availability optimization and design, Expert Systems with Applications, vol. 34, no.1, pp. 181-193,2008.
[12] Shumeeet Baluja and Rich Caruana, "Removing the Genetics from the Standard Genetic Algorithm", Morgan Kaufmann Publishers, pp. 38-46, 1995.
[13] T. Chen, K. Tang, G. Chen, and X. Yao, On the analysis of average time complexity of estimation of distribution algorithms, in Proc. IEEE Congr. Evol. Comput. (CEC), pp. 453460, 2007.
[14] Larraaga P. Lozano J.A., Estimation of Distribution Algorithms: New Tool for Evolutionary Computation, emphBoston: Kluwer Academic Publishers, 2002.
[15] T. Chen, J. He, G. Sun, G. Chen, and X. Yao, A new approach to analyzing average time complexity of population-based evolutionary algorithms on unimodal problems, IEEE Trans. Syst., Man, Cybern. B, Cybern., vol. 39, no. 5, pp. 10921106, Oct. 2009.
[16] Rudolph Frederick Stapelberg, "Handbook of Reliability, Availability, Maintainability and Safety in Engineering Desing", Springer, 2009.