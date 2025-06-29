# Probabilistic Based Evolutionary Optimizers in Bi-objective Travelling Salesman Problem 

Vui Ann Shim, Kay Chen Tan, and Jun Yong Chia<br>Department of Electrical and Computer Engineering, National University of Singapore, 4 Engineering Drive 3, 117576, Singapore<br>\{g0800438, eletankc, g0900313\}@nus.edu.sg


#### Abstract

This paper studies the probabilistic based evolutionary algorithms in dealing with bi-objective travelling salesman problem. Multi-objective restricted Boltzmann machine and univariate marginal distribution algorithm in binary representation are modified into permutation based representation. Each city is represented by an integer number and the probability distributions of the cities are constructed by running the modeling approach. A refinement operator and a local exploitation operator are proposed in this work. The probabilistic based evolutionary optimizers are subsequently combined with genetic based evolutionary optimizer to complement the limitations of both algorithms.


Keywords: Estimation of distribution algorithm, evolutionary multi-objective optimization, restricted Boltzmann machine, travelling salesman problem.

## 1 Introduction

Travelling salesman problem (TSP) is one of the famous permutation based combinatorial optimization problems [1]. The problem aims to minimize the total distance travelled, in which each city is visited exactly once and the salesman must return to the starting depot. The adaptation of TSP into multi-objective framework (MOTSP) is another promising area which can be explored [2-3]. In the multi-objective formulation, the aim is to simultaneously optimize several conflicting objectives, such as shortest travelling distance, minimum time, minimum cost and lowest risk [4].

Probabilistic based evolutionary algorithms (EAs), commonly known as Estimation of distribution algorithms (EDAs) [1], mimic the biological evolutionary principle to guide the search. The primary difference between EDAs and genetic based EA (specifically genetic algorithm) is that no genetic operators (crossover and mutation) are implemented in EDAs. The reproduction is based on building of probabilistic model from the selected solutions and sampling from the constructed model.

Several researches have been carried out to study the single objective permutation based problems (specifically TSP) by using EDAs [1]. However, there is no research which studies multi-objective permutation based problems (specifically MOTSP) by using EDAs. In this paper, binary representation of multi-objective univariate marginal probability algorithm (MOUMDA) and multi-objective restricted Boltzmann machine (MORBM) [5] are adapted into a permutation based representation to solve Bi-TSP. The two objectives being considered are travelling distance and travelling cost. Permutation

refinement operator is proposed to refine the cities in a chromosome to guarantee that no city is repeated. A local exploitation operator is also presented to enhance the search capability of the algorithms. Probabilistic based EAs are subsequently combined with genetic based EA to increase the spread of the trade-off solutions.

# 2 Algorithms' Framework 

### 2.1 Modeling and Reproduction

Two modeling approaches are considered in this paper. UMDA [6] learns the distributions of the cities without considering their linkage dependencies with other cities. In the modeling, a $n x n$ probability matrix which models the distribution of the cities is constructed, according to the following equation.

$$
\operatorname{Prob}_{\mathrm{g}}\left(\mathrm{C}_{\mathrm{i}, \mathrm{j}}\right)=\frac{\sum_{\mathrm{k}=1}^{\mathrm{pop}} \delta_{\mathrm{k}}\left(\mathrm{C}_{\mathrm{i}, \mathrm{j}}=\mathrm{c}_{\mathrm{i}}\right)+1 / \mathrm{n}}{\mathrm{pop}+\mathrm{pop}_{\mathrm{n}}} \text { where } \delta_{\mathrm{k}}\left(\mathrm{C}_{\mathrm{i}, \mathrm{j}}=\mathrm{c}_{\mathrm{i}}\right)=\left\{\begin{array}{l}
1 \text { if } \mathrm{C}_{\mathrm{i}, \mathrm{j}}=\mathrm{c}_{\mathrm{i}} \\
0 \text { otherwise }
\end{array}\right.
$$

$\operatorname{Prob}_{\mathrm{g}}\left(\mathrm{C}_{\mathrm{i}, \mathrm{j}}\right)$ is the marginal probability of city i at the $\mathrm{j}^{\text {th }}$ place of the chromosome at generation $\mathrm{g}, \mathrm{c}_{\mathrm{i}}$ is the city i , pop is the population size, and n is the number of cities.

RBM is energy based neural network [5] which learns the distribution of the input stimuli through unsupervised learning. The probabilistic model is constructed as

$$
\begin{gathered}
\operatorname{Prob}_{\mathrm{g}}\left(\mathrm{C}_{\mathrm{i}, \mathrm{j}}\right)=\frac{\sum_{\mathrm{k}=1}^{\mathrm{pop}} \mathrm{P}_{\mathrm{k}}\left(\mathrm{C}_{\mathrm{i}, \mathrm{j}}=\mathrm{c}_{\mathrm{i}}\right)+\mathrm{z}_{\mathrm{j}} /(\text { pop }+ \text { numc })}{\mathrm{z}_{\mathrm{i}}+{ }^{\mathrm{z}_{\mathrm{j}} / \text { pop }}} \text { where } \\
\mathrm{P}_{\mathrm{k}}\left(\mathrm{C}_{\mathrm{i}, \mathrm{j}}=\mathrm{c}_{\mathrm{i}}\right)=\left\{\begin{array}{l}
\sum_{\mathrm{h}=1}^{\mathrm{H}} \mathrm{e}^{-\mathrm{E}\left(\mathrm{v}=\mathrm{c}_{\mathrm{i}}, \mathrm{~h}\right)} \text { if } \mathrm{C}_{\mathrm{i}, \mathrm{j}}=\mathrm{c}_{\mathrm{i}}, \mathrm{Z}_{\mathrm{j}}=\sum_{\mathrm{x}, \mathrm{y}} \mathrm{e}^{-\mathrm{E}(\mathrm{x}, \mathrm{y})} \\
0 \text { otherwise }
\end{array}\right. \\
\mathrm{E}(\mathrm{v}, \mathrm{~h})=\sum_{\mathrm{i}} \sum_{\mathrm{j}} \mathrm{v}_{\mathrm{i}} \mathrm{~h}_{\mathrm{j}} \mathrm{w}_{\mathrm{ij}}-\sum_{\mathrm{i}} \mathrm{v}_{\mathrm{i}} \mathrm{~b}_{\mathrm{i}}-\sum_{\mathrm{j}} \mathrm{~h}_{\mathrm{j}} \mathrm{~b}_{\mathrm{j}}
\end{gathered}
$$

where v is the input state and h is the hidden state of the network, w and b is the synaptic weights and biases, Z is the normalizing constant, and E is the energy value of the network. The simple probabilistic sampling mechanism [5] is applied to generate offspring based on the built probabilistic model.

For evolutionary optimizer [7], the variation operators are based on crossover and mutation. Single point crossover is used to create the offspring. This operator randomly selects the position to cut the chromosomes for crossing over between two parents. This single point crossover is equivalent to route inter-crossing. After which, mutation is carried out by swapping between two randomly selected alleles within the chromosome. This genetic perturbation provides exploitation capability to the optimizer to search within fitter region.

# 2.2 Refinement Operator and Local Exploitation Operator 

After reproduction some cities may not be visited, while others are visited more than once. To overcome this problem, a refinement operator is proposed. Firstly, the repeated and unvisited cities in a chromosome are detected. An insertion is carried out by inserting the unvisited cities to the position of the repeated cities. The average distance and cost (normalized) between the adjacent cities in the permutation are calculated and served as the main criteria for insertion. In order to enhance the search, a local exploitation operator is also proposed. The process flow of this operator is as follow. Firstly, a set of k number of cities to be relocated is randomly selected. Distances and costs among all the selected cities are calculated. The permutation of the cities is re-determined according to the distances and costs information. Due to optimization of two objective functions in this paper, three types of relocation criteria are considered. The first criterion determines the permutation based on the shortest distance in first objective function. Second considers the lowest cost in second objective function, and last criterion computes the normalized average distance and cost from both objective functions.

### 2.3 Overall Framework

The algorithmic process flow of the proposed algorithm is shown in Fig. 1. Firstly, initialization is performed by randomly generating permutation in integer number. Then, evaluation is carried out. Based on the objective domain, a new fitness is assigned to each solution based on Pareto ranking and crowding distance [7]. Binary tournament selection is applied to choose the promising solutions. The selected solutions will undergo modeling based on univariate or RBM approach. Based on the constructed model, probabilistic sampling is carried out to produce n offspring, where n is the population size. Then, the refinement operator is performed. To further improve the routing, a local exploitation is incorporated. The local exploitation will only be performed if the generated random value is smaller than a predefined local exploitation rate. After this, an archive is created to store the promising solutions found. The same procedure is iterated until the stopping criterion is met. The same process flow is implemented in genetic based EA. As for combination of genetic and probabilistic based EAs, the algorithms starts with probabilistic based optimizers and alternated with genetic based optimizer every 500 generation.

## 3 Simulation Results and Discussions

The experimental settings are shown in Table 1. TSP with two objectives is studied. The information of the distance and cost among cities is randomly generated in the range of $[0,1000]$ as done in [8]. Two performance metrics namely inverter generational distance (IGD) and non-domination ratio (NR) are utilized. IGD measures the proximity as well as the spread of the optimal solutions to the evolved solutions. NR measures the non-dominated ratio of solutions in one algorithm compared to other algorithms. The approximate optimal solutions set is formed from all the nondominated solutions found in all algorithms [8]. EA refer to genetic based EA. UMEA and RBMEA is the combination of UMDA and RBM with EA.

![img-0.jpeg](img-0.jpeg)

Table 1. Parameter setting for the algorithms

| Parameter | Value |
| :--: | :--: |
| Population size | Number of cities |
| Number of cities | 100, 200, 500 |
| Stopping criterion | 2000 generations |
| Local search rate | 0.5 |
| Crossover rate | 0.8 |
|  | 0.05 |
| Mutation rate |  |
| Independent runs | 10 |

Fig. 1. Process flow of MOEDAs

Results for 100 cities are plotted in Fig. 2. EDAs give better performance than EA in term of IGD and NR. This is because EDAs consider the overall distribution of the population to guide the search, which is different from EA which use individual chromosome to generate offspring. From convergence trace, it is observed that RBM has the fastest convergence rate at early evolution, while EA has the lowest convergence rate. Furthermore, the Pareto front curve shows that UMDA has good proximity but poor spread. The corporation between EDAs with EA improves the spread of the algorithms with the cost of sacrificing proximity.

Results for 200 cities are presented in Fig. 3. Most of the final non-dominated solutions are generated from RBM. RBM and RBMEA take advantages from the dependencies of the cities. Thus, outperform other algorithms. Furthermore, the incorporation of EDAs with EA seems to improve the performance of sole algorithms.
![img-1.jpeg](img-1.jpeg)

Fig. 2. NR, Evolution trace and, Evolved Pareto front with 100 cities
![img-2.jpeg](img-2.jpeg)

Fig. 3. NR, Evolution trace and, Evolved Pareto front with 200 cities

![img-3.jpeg](img-3.jpeg)

Fig. 4. NR, Evolution trace and, Evolved Pareto front with 500 cities
The simulation results for problem with 500 cities are presented in Fig. 4. Overall, the EDAs and EAs alone are unable to evolve a set of good trade-off solutions. The corporation between EDAs and EAs improve the overall performance.

# 4 Conclusions 

This paper has studied the probabilistic based EAs in solving Bi-TSP. It is among the first attempts to employ EDAs in the study of permutation based multi-objective problems. Two probabilistic modeling techniques have been adapted. They include univariate modeling and RBM approach. A refinement operator has been proposed to make sure the hard constraints of the problem are not violated. In addition, a local search operator is defined to enhance the exploitation of the algorithms. As the limitation of EDAs in evolving a set of good spread solutions, genetic based evolutionary optimizer is incorporated with EDAs to complement their weaknesses. The empirical results show that EDAs have better proximity while EA has better spread in their final evolved solutions. The incorporation between EDAs and EA mutually complements each other's limitation; thus yielding better performance.

## References

1. Larrañaga, P., Lozano, J.A.: Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Kluwer, Norwell (2001)
2. Jahne, M., Li, X., Branke, J.: Evolutionary Algorithms and Multi-objectivization for the TSP. In: Genetic and Evolutionary Computation Conference, pp. 595-602 (2009)
3. Herrera, F., Garcia-Martinez, C., Cordon, O.: A taxonomy and an Empirical Analysis of Multiple Objective Ant Colony Optimization Algorithms for the Bi-criteria TSP. European Journal of Operational Research 180(1), 116-148 (2007)
4. Yang, M., Kang, L, Guan, J.: An Evolutionary Algorithm for Dynamic Multi-objective TSP. In: Conference on Advances in Computation and Intelligence, pp. 62-71 (2007)
5. Tang, H.J., Shim, V.A., Tan, K.C., Chia, J.Y.: Restricted Boltzmann Machine based Algorithm for Multi-objective Optimization. In: Congress on Evolutionary Computation (2010)
6. Muhlenbein, H., Paass, G.: From Recombination of Genes to the Estimation of Distributions I. Binary Parameters. In: Conference on Parallel Problem Solving from Nature, pp. 178-187 (1996)
7. Deb, K., Pratap, A., et al.: A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II. Transactions on Evolutionary Computation 6(2), 182-197 (2002)
8. Peng, W., Zhang, Q., Li, H.: Comparison between MOEA/D and NSGAII on the Multiobjective Travelling Salesman Problem. In: Multi-objective Memetic Algorithms, vol. 171, Springer, Heidelberg (2009)