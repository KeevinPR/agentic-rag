# Multi-objective Estimation of Distribution algorithm based on Voronoi and Local search 

Elham Mohagheghi<br>Student of Master of Control Engineering<br>Ferdowsi University of Mashhad<br>Mashhad, Iran<br>E_mohagheghi@stu.um.ac.ir


#### Abstract

In this paper we propose an Estimation of Distribution Algorithm (EDA) equipped with Voronoi and local search based on leader for multiobjective optimization. We introduce an algorithm that can keep the balance between the exploration and exploitation using the local information in the searched areas through the global estimation of distribution algorithm. Moreover, the probability model in EDA, receives special statistical information about the amount of the variables and their important dependency. The proposed algorithm uses the Voronoi diagram in order to produce the probability model. By using this model, there will be a selection based on the area instead of selection based on the individual, and all individual information could use to produce new solution. In the proposed algorithm, considering the simultaneous use of global information about search area, local information of the solutions and the Voronoi based probability model lead to produce more diverse solutions and prevent sticking in local optima. Also, in order to reduce the data dimension, the principle component analysis is proposed. Several benchmarks functions with different complexity like linear and non-linear relationship between the variables, the continues!discontinues and convex!non-convex optima fronts use to show the algorithm performance.


Key Words
Estimation of distribution algorithms, Multiobjective optimization, Particle swarm optimization, Voronoi diagram.

## I. Introduction

The real world problems usually have a lot of criteria that could formulate as a multi-objective problem. Problems that have some disproportionate and often competitive cost functions usually recognize as the multiobjective optimization problems. In most of the optimization problems there are four challenges: a) The multiple conflicting goals, b) The very complex search area, c) Uncertainty, d) The
dynamic area. Efficient optimization strategies need to face these challenges.
The success of population based algorithm in multi-objective optimization problems reported in many papers. But random recombination in these algorithms may disturb the good building blocks, thus, forecasting to move to the optimize area may be difficult. To solve this problem, the estimation of distribution algorithms, with the idea of exploiting the relationship between variables, introduce as a new computing paradigm in the population based algorithms. In estimation of distribution algorithms crossover operator and mutation are not implemented. Instead, reproduction is done by making a representative probability model, and then new solutions produce by the sampling of this probability model. These algorithms could work with noisy information. Their parallel natures help them to optimize different areas of the search space simultaneously in order to find some promised solutions. But their weakness is that they model the solutions distribution even if they stuck in local optima, and use this probability information as a reference model to produce new generation. To avoid being stuck in local optima, the algorithm should be able to search and keep a diverse set of solutions. According to these algorithms that estimate the probability distribution of the best solutions and using just global information, whenever the kept solutions tend to special area, the algorithm may consider the kept solutions as desired and makes the probability distribution based on them. Thus it has a great importance to keep diversity, specially the ability to produce a set of diverse solutions. In this regard, inspired from local search based on leader in particle swarm algorithm, global search in estimation of

distribution algorithm and partitioning by Voronoi diagram, propose an algorithm that able to find more diverse solutions, better approximation of the optimal Pareto front and avoiding the algorithm to stick in local optima. Due to simplicity and it's consumedly performance in the principal component analysis, the use of this method proposed in order to reduce variables dependency and data dimension.

## II. Literature Review

The estimation of distribution algorithms performance is naturally depends on statistical modeling and sampling method. There is a good wealth of literature on probability modeling in estimation of distribution algorithms.
Bayesian network is one of these probability models, which could consider the dependency between variables and use to learn parameters relationship and problem structure. These networks approximate the conditional probability. Each node and connection in these networks relate to the conditional probability. Some of the multi-objective estimation of distribution algorithms that use Bayesian networks includes BMOA, mohBOA, DTMEDA, DP-MrBOA, [1-4]. MBN-EDA is a new modeling method in multi-objective estimation of distribution algorithm that uses multi dimensions Bayesian networks (MBN) to learn a common model of aims and variables. This model not only, like other estimation of distribution algorithms, considers the variables relationship, but also could consider the goals relationship [5].
Restricted Boltzmann machine is another statistical model that uses a hidden layer to model its variables distributions. This network includes hidden and visible units. The probabilities of the joint configuration over the hidden and visible units in network are trained until that distribution over the global state achieves a certain level of thermal equilibrium. Then, probability model is made by using network energy function. In RBM-EDA, Restricted Boltzmann machine model is introduced as the estimation of distribution algorithm in the multi-objective optimization filed [6]. In [7], EDA based on RBM combined with PSO for multi-objective optimization in noisy environment.
VEDA [8] and mohBOA ignore the regularity in making probability models. Since the probability modeling technics check widespread under special discipline and regularity in statistical
learning fields, thus it is possible to use discipline in designing estimation of distribution algorithms in continues multi-objective algorithms. In RM-MEDA, the regularity feature of continues multi-objective optimization problems use as a base for an estimation of distribution algorithm in facing variables relationship. RM-MEDA, model promised area in search space by a probability model that its gravity center is a piece continuous manifold. Local PCA algorithm uses to make this model [9].
Some methods combine the estimation of distribution algorithm with other heuristic search methods in order to increase the performance. The work presented in [10] is a combination of EDA and particle swarm algorithms. Gao et al. present an algorithm that combine EDA based on univariate distribution with particle swarm optimization (PSO) algorithm [11]. In [12], the combination of EDA and particle swarm optimization algorithm presented to control reservoir flood. This algorithm divides the population to some sub-population and makes the probability model for each of them. Based on the probability model, each sub-population reproduces new members with the estimation of distribution and particle swarm optimization algorithm. In [13], use univariate Gaussian model to estimate the solutions distributions. Some parameters of this model have the learning ability. In this method an EDA with comparative learning rate combine with chaos disorder search method.
While most of the multi-objective estimation of distribution algorithms are based on Pareto front, there are some study in other multi-objective optimization frame. In [14] the main idea is that any information from solutions near the weight vector should be helpful. Thus, making a probability model from all neighborhood solutions may have more efficient information than crossover operator [15]. In [16-19] cited some of estimation of distribution algorithm based on decomposition method. Shim et al. use a selection method based on decomposition in a combination of EDA based on univariate distribution and some local search methods [20]. In some of EDA a combination of some of probability models are used [21]. However, existing models could not reflect the problem completely. when the amount of variables and components increase, the optimization results become invalid [22]. Additionally, when consider all the relations between variables the computing cost increase.

## III Proposed Method

## A. Reducing Data Dimension

One of the reasons that could increase problem complexity is increase in data dimension. There are different methods to reduce problem complexity like correlation, the principal component analysis, linear programming and etc. Due to simplicity and performance of the principal component analysis, at first in the proposed method this procedure used to reduce the data dimension and variables transfer to coordinate system with fewer dimensions. In new coordination system problem solved and finally data return to the first coordinate system.

## B. Principal Component Analysis

Principal component analysis is a statistical method that is frequently used to evaluate a group of correlated variables. Uses an orthogonal linear transformation to takes data to a new coordinate system and can be used to reduce the data dimension. Select fewer factors as the principal components from primary factors, by delete some unimportant information. The first extracted principal component, consider the most scattering over all data. That means the first component correlate at least to some of variables. The second extracted component has two important features, first this component consider the most set of data that are not compute by the first component, second it has no correlation to the first component. In other words, ignore the pervious component, pass the first to the final components, each component explain less variance. It means that always the first principal component explains the greatest amount of variance and the final components explain the least amount of variance, thus by ignoring the final components not lose many information.

## C. Global search with estimation of distribution algorithm based on Voronoi

Voronoi partitioning has several advantages. Voronoi diagram has the ability to adapt the problem structure. Cover all the search space. Although unselected individual have low rank, but they may include well information, therefore, ignoring them may lose part of information. By partitioning, all individuals (selected and unselected) information could use to lead the search. After transferring the variables to new system, partition the search space by Voronoi diagram.

## D. Voronoi partitioning

The discrete Voronoi diagram presented in [8] is used for simplicity. At first, all the search space divided to small grid, in which at most a member is existed in each grid. Then allocate the member rank to the related grid. The next step is to allocate the rank to the neighbors, till all the grids have rank. When a grid places near some members, it achieves the worse rank. All the grids with the same rank form a Voronoi mesh. Therefore, each mesh has its own rank. This rank use to calculate that mesh selection probability. To calculate individual rank, non-dominated sorting algorithm used [24] and for calculate probability geometric distribution is used.
Mathematically, the geometric distribution is calculated as (1).
$\mathrm{P}=\mathrm{P}_{\mathrm{G}}\left(1-\mathrm{P}_{\mathrm{G}}\right)^{\mathrm{r}-1}$
In (1) $\mathrm{P}_{\mathrm{G}}$ is a number in $[0,1]$ and r is the related rank. In this paper $\mathrm{P}_{\mathrm{G}}=0.8$.

## E. Local search by particle swarm optimization algorithm

Each particle in particle swarm optimization algorithm, use local information of the best solutions that it has ever achieved (local optima) and the best answer that all particles have ever achieved (global optima). Using local information to exploitation could be helpful. In the proposed method, a mesh selected due to related probability. The control parameter $r(t)$ set the running algorithm steps. In the first steps due to keeping diversity and new areas exploration, the probability model sample and new solutions in selected mesh and produce by uniform distribution. But in final steps, after exploration of the best area, the local information use to produce new solutions by particle swarm algorithm. At the end, new solutions compare to pervious one and bests (non-dominated solutions) are kept. The proposed algorithm steps are shown in "Fig. 1".

## IV. Evaluations

The functions that choose for the test has complexity like linear/non-linear relationship between variables, continues/discontinues and convex/non-convex Pareto fronts. The first six functions are F1-F6 and F7-F9 are F8-F10 [9]. F10-F12 are respectively FON2, KUR1 and SCH1 functions in [8], F13-F15 are POLONNI,

ZDT3 and VIENNET functions, F16, F17 are respectively 2D and 3D DTLZ1 functions and F18 is DEB function.

1. Initialize population.
2. The principal component analysis and transferring data to the new coordinate system with fewer dimension
3. Making probability model
3.1. Dividing the search space to grids and producing Voronoi diagram
3.2. Determining the probability of each Voronoi mesh selection: $\mathrm{P}=$ $\mathrm{P}_{0}\left(1-\mathrm{P}_{0}\right)^{\mathrm{r}-1}$
4. Producing new population
4.1 Computing control parameter: $r(i t)=$ $1-\frac{\alpha}{\text { maxit }}$
4.2 Producing random number (rand)
4.3 Comparing random number to control parameter
4.3.1 rand $<r(i t)$
4.3.1.1 Selecting a Voronoi mesh based on determined probability (3.2)
4.3.1.2 Producing $\mathrm{n}_{\text {Sample }}$ by uniform distribution in selected mesh
4.3.1.3 Returning new data to the primary coordination system
4.3.2 rand $>r(i t)$
4.3.2.1 Grid search space
4.3.2.2 Selecting leader
4.3.2.3 Updating particle position and velocity
4.3.2.4 Adding non-dominated particles to archive and deleting non-dominated members
4.3.2.5 Updating grid
4.3.2.6 Returning new data to the primary coordinate system
5. Merging new population and pervious one
6. Evaluating the population and keeping nondominated members in archive
7. If the terminate condition is met, end otherwise return to (2).

P: selecting Probability of each mesh $\mathrm{P}_{0}=0.8$ : Geometric distribution parameter, r: Each mesh rank, r(it): Control parameter, it: Algorithm iteration, maxit: The max iteration, $\mathrm{n}_{\text {Sample }}$ : Number of new samples

Fig. 1. Proposed algorithm steps
A. Pareto front drawing

For sample in "fig. 2-4." the True and approximation Pareto fronts by proposed, RMMEDA [9] and MO-PSO-EDA [12] are shown.
![img-0.jpeg](img-0.jpeg)

MEDA (red) and MO-PSO-EDA (green) for ZDT3 function (discrete, non-convex)
![img-1.jpeg](img-1.jpeg)

ZDT1 function that $x$ change to $x^{2}$ (non-linear relationship)
![img-2.jpeg](img-2.jpeg)

Fig. 4. True Pareto front and proposed and RM-MEDA for DTLZ1 function

## B. Numerical criteria comparison

## B. 1 Quality criteria

C (A, B) between two approximations A and B of the Pareto front, is percent of B that dominate by A, and define as "(2)":

$$
C(A, B)=\frac{\langle[(b \in B)[\left.\cup \in A \in a d o m i n u t e s b]\right]\rangle}{(|B|)}
$$

This criteria could evaluate the quality of achieve solutions by two different methods. As C is larger, it means that more member of B is dominated by A. And show that A has better quality than B.
Normalizing the C, Q expressible as "(3)":

$$
Q(A, B)=C(A, B) /(C(A, B)+C(B, A))
$$

In "table I" the numerical criteria, Q is shown for three algorithms. The result reported as average and standard deviation of achieve solutions in 40 runs. The number that shows better performance is bold. As it is clear, the proposed method in 11 out of 18 test functions has better performance than RM-MEDA and outperforms of MO-PSOEDA in 11 of 16. Since MO-PSO-EDA did not show a sufficiently good quality on F9 and F15, these functions are not used here.

Table I. Comparing proposed (A), RM-MEDA (B) and MO-PSO-EDA (C) with Q criteria in 40 runs

|  | $\mathbf{Q}(\mathbf{A}, \mathbf{B})$ | $\mathbf{Q}(\mathbf{A}, \mathbf{C})$ |
| :--: | :--: | :--: |
| F1 | $\mathbf{0 . 7 9 8 1} \pm \mathbf{0 . 3 1 8 6}$ | $\mathbf{0 . 5 9 2 2} \pm \mathbf{0 . 3 4 3 8}$ |
| F2 | $\mathbf{0 . 9 6 7} \pm \mathbf{0 . 1 5 2 8}$ | $\mathbf{0 . 9 5 6 5} \pm \mathbf{0 . 0 8 3 7}$ |
| F3 | $\mathbf{0 . 1 1 2 2} \pm \mathbf{0 . 1 2 8 5}$ | $\mathbf{0 . 1 6 9 4} \pm \mathbf{0 . 2 7 2 0}$ |
| F4 | $\mathbf{0 . 2 1 6 4} \pm \mathbf{0 . 1 7 9 3}$ | $\mathbf{0 . 6 0 3 2} \pm \mathbf{0 . 2 2 5 3}$ |
| F5 | $\mathbf{0 . 9 9 9 9} \pm \mathbf{3 . 0 8 4 7 E}$ | $\mathbf{0 . 9 9 9 9} \pm \mathbf{2 . 7 7 3 2 E}$ |
| F6 | $\mathbf{0 . 9 9 4 7} \pm \mathbf{0 . 0 3 2}$ | $\mathbf{0 . 9 9 9} \pm \mathbf{0 . 0 0 4 4}$ |
| F7 | $\mathbf{0 . 8 7 6 5} \pm \mathbf{0 . 1 0 1 6}$ | $\mathbf{0 . 8 5 9 9} \pm \mathbf{0 . 8 4 6}$ |
| F8 | $\mathbf{0 . 9 4 2 9} \pm \mathbf{0 . 1 6 8 5}$ | $\mathbf{0 . 9 2 1 7} \pm \mathbf{0 . 1 4 1 3}$ |
| F9 | $\mathbf{1} \pm \mathbf{0}$ |  |
| F10 | $\mathbf{0 . 9 5 7 5} \pm \mathbf{0 . 0 2 9}$ | $\mathbf{0 . 2 1 7 0} \pm \mathbf{0 . 0 8 3 1}$ |
| F11 | $\mathbf{0} \pm \mathbf{0}$ | $\mathbf{0 . 0 4 2 9} \pm \mathbf{0 . 0 2 2 2}$ |
| F12 | $\mathbf{0 . 0 4 4 1} \pm \mathbf{0 . 0 3 3 2}$ | $\mathbf{0 . 1 0 3 3} \pm \mathbf{0 . 0 6 0 1}$ |
| F13 | $\mathbf{0 . 5 9 3 5} \pm \mathbf{0 . 1 2 1 9}$ | $\mathbf{0 . 5 9 4 7} \pm \mathbf{0 . 1 4 9 3}$ |
| F14 | $\mathbf{1} \pm \mathbf{0}$ | $\mathbf{0 . 8 2 5 3} \pm \mathbf{0 . 2 3}$ |
| F15 | $\mathbf{0 . 3 1 4 7} \pm \mathbf{0 . 1 3 1 8}$ |  |
| F16 | $\mathbf{0 . 0 0 2 8} \pm \mathbf{0 . 0 0 4 5}$ | $\mathbf{0 . 6 9 6 3} \pm \mathbf{0 . 1 3 5}$ |
| F17 | $\mathbf{0 . 5 2 2 2} \pm \mathbf{0 . 2 4 2 7}$ | $\mathbf{0 . 2 5 4 1} \pm \mathbf{0 . 1 5 9 4}$ |
| F18 | $\mathbf{0 . 1 0 5 5} \pm \mathbf{0 . 2 5 9 9}$ | $\mathbf{0 . 9 2 1 8} \pm \mathbf{0 . 0 9 8 1}$ |

## B. 2 Convergence and diversity criteria

The inverse generational distance (IGD) criteria could show not only the amount of diversity but also the solutions convergence. To compute this criterion, the test functions true Pareto front is needed, and because this optima front is available for 10 test functions, this criteria is used for these functions. If $P^{*}$ is a set of points with uniform distribution in fitness space along
the true pareto front, and P is an approximate of the Pareto front, the inverse generational distance define as "(4)":

$$
I G D\left(P^{*}, P\right)=\frac{\sum_{v \in P^{*}} d(v, P)}{\left|P^{*}\right|}
$$

In "(4)," $\mathrm{d}(\mathrm{v}, \mathrm{P})$ is the minimum Euclidean distance between v and the points in P . If $\left|\mathrm{P}^{*}\right|$ is large enough and could well explain the Pareto front, $\operatorname{IGD}\left(\mathrm{P}^{*}, \mathrm{P}\right)$ could measure both the diversity and convergence. As $\operatorname{IGD}\left(\mathrm{P}^{*}, \mathrm{P}\right)$ is smaller, the approximate front is closer to the true Pareto front.
In table II average and standard deviation of IGD reported in 40 runs for the proposed method and RMMEDA. Also p-value of t-test is reported.

Table II. IGD for proposed (A), RM-MEDA (B) and MO-PSO-EDA (C) in 40 run

|  | Method | MEAN $\pm$ STD | p-value | p-value |
| :--: | :--: | :--: | :--: | :--: |
| F1 | A | $\mathbf{0 . 0 0 1 8} \pm \mathbf{0 . 0 0 1 8}$ | A \& B | A \& C |
|  | B | $0.0037 \pm 0.0015$ | 0.0043 | $\mathrm{H}=0$ |
|  | C | $0.0031 \pm 0.0066$ |  |  |
| F2 | A | $\mathbf{0 . 0 0 2 0} \pm \mathbf{1 . 9 8 6 8 E}-4$ | $3.74 \mathrm{E}-5$ | $\mathrm{H}=0$ |
|  | B | $0.0071 \pm 0.0033$ |  |  |
|  | C | $0.0027 \pm 6.1347 \mathrm{E}-4$ |  |  |
| F3 | A | $0.0485 \pm 0.086$ | 0.004 | 0.0155 |
|  | B | $\mathbf{0 . 0 0 7 4} \pm \mathbf{0 . 0 0 3 4}$ |  |  |
|  | C | $0.0138 \pm 0.006$ |  |  |
| F4 | A | $0.0419 \pm 0.0134$ | $\begin{aligned} & 1.2043 \mathrm{E}- \\ & 11 \end{aligned}$ | $\begin{aligned} & 1.1698 \mathrm{E}- \\ & 05 \end{aligned}$ |
|  | B | $\mathbf{0 . 0 2 2} \pm \mathbf{0 . 0 0 4 2}$ |  |  |
|  | C | $0.0547 \pm 0.0142$ |  |  |
| F10 | A | $0.0025 \pm 1.1408 \mathrm{E}-4$ | $\begin{aligned} & 7.7825 \mathrm{E}- \\ & 33 \end{aligned}$ | $\begin{aligned} & 9.8177 \mathrm{E}- \\ & 08 \end{aligned}$ |
|  | B | $0.0045 \pm 2.7221 \mathrm{E}-4$ |  |  |
|  | C | $0.0023 \pm 11.8156 \mathrm{E}-4$ |  |  |
| F11 | A | $0.0575 \pm 0.0097$ | $\begin{aligned} & 6.1304 \mathrm{E}- \\ & 4 \end{aligned}$ | $\begin{aligned} & 3.6589 \mathrm{E}- \\ & 58 \end{aligned}$ |
|  | B | $\mathbf{0 . 0 5 1 8} \pm \mathbf{0 . 0 0 1 6}$ |  |  |
|  | C | $0.0525 \pm 0.0018$ |  |  |
| F12 | A | $\mathbf{0 . 0 1 9 7} \pm \mathbf{0 . 0 0 1 9}$ | $\begin{aligned} & 5.3377 \mathrm{E}- \\ & 17 \end{aligned}$ | $\begin{aligned} & 2.8285 \mathrm{E}- \\ & 11 \end{aligned}$ |
|  | B | $0.024 \pm 7.7952 \mathrm{E}-4$ |  |  |
|  | C | $0.0242 \pm 8.895 \mathrm{E}-4$ |  |  |
| F14 | A | $\mathbf{0 . 0 0 2 1} \pm \mathbf{0 . 0 0 3 9}$ | $\begin{aligned} & 1.5928 \mathrm{E}- \\ & 35 \end{aligned}$ | $\begin{aligned} & 1.1735 \mathrm{E}- \\ & 43 \end{aligned}$ |
|  | B | $0.3773 \pm 0.0512$ |  |  |
|  | C | $0.0030 \pm 3.5536 \mathrm{E}-4$ |  |  |
| F16 | A | $\mathbf{0 . 0 2 7 3} \pm \mathbf{0 . 0 0 4 2}$ | $\begin{aligned} & 2.1856 \mathrm{E}- \\ & 15 \end{aligned}$ | $\begin{aligned} & 9.2907 \mathrm{E}- \\ & 06 \end{aligned}$ |
|  | B | $0.2148 \pm 0.0953$ |  |  |
|  | C | $0.0313 \pm 0.0026$ |  |  |
| F17 | A | $0.0598 \pm 0.0051$ | 0.0251 | $\begin{aligned} & 3.4166 \mathrm{E}- \\ & 70 \end{aligned}$ |
|  | B | $\mathbf{0 . 0 5 7 8} \pm \mathbf{0 . 0 0 1 9}$ |  |  |
|  | C | $0.0594 \pm 0.0016$ |  |  |

As the results show the proposed method IGD criteria is better in 5 out of 10 .

## V. Conclusion

This paper introduce an algorithm that simultaneously use global search space information for better exploration and local information of the solutions for more accurate exploitation. Moreover, the use of Voronoi diagram in proposed algorithm tends to make more efficient probability model. As the simulation results show, the algorithm achieves appropriate approximation of continues!discontinues, convex!non-convex optimum fronts as it is helpful in problems with linear!non-linear relationship between variables.

## References

[1] M. Laumanns and J. O'cen'a'sek, "Bayesian optimization algorithms for multi-objective optimization," presented at 7th International Conference on Parallel Problem Solving from Nature (PPSN VII), 2002.
[2] M. Pelikan, K. Sastry, and D. E. Goldberg, "Multiobjective hBOA,clustering, and scalability," presented at Conference on Genetic and Evolutionary Computation (GECCO '05), New York, NY, USA: ACM, 2005.
[3] X. Zhong and W. L. I. C. Society, "A decision-treebased multi-objective estimation of distribution algorithm," presented at International Conference on Computational Intelligence and Security (CIS'07), 2007.
[4] C. W. Ahn and R. S. Ramakrishna, "Multiobjective real-coded Bayesian optimization algorithm revisited: Diversity preservation," presented at 9th Annual Conference on Genetic and Evolutionary Computation (GECCO '07), New York, NY, USA: ACM, 2007.
[5] H. Karshenas, R. Santana, C. Bielza, and P. Larraraga, "Multi-objective Estimation of Distribution Algorithm Based on Joint Modeling of Objectives and Variables," Evolutionary Computation, IEEE Transactions on vol. 18, no. 4, pp. 519-542, 2014.
[6] H. Tang, V. A. Shim, K. C. Tan, and J. Y. Chia, "Restricted Boltzmann machine based algorithm for multi-objective optimization," IEEE Congress on Evolutionary Computation (CEC'10), pp. 1-8, 2010.
[7] V. A. Shim, K. C. Tan, and J. Y. Chia, "Multi-objective optimization with estimation of distribution algorithm in a noisy environment," Evolutionary Computation, vol. 21, pp. 149-177, 2013.
[8] T. Okabe, Y. Jin, B. Sendoff, and M. Olhofer, "Voronoibased estimation of distribution algorithm for multiobjective optimization," IEEE Congress on Evolutionary Computation (CEC'04), vol. 2, pp. 15941601,2004.
[9] Q. Zhang, A. Zhou, and Y. Jin, "RM-MEDA: A regularity model based multiobjective estimation of distribution algorithm," IEEE Transactions on Evolutionary Computation, vol. 12, pp. 41-63,2008.
[10] C.W. Ahn, J. An, and J. Yoo, "Estimation of particle swarm distribution algorithms: Combining the benefits
of PSO and EDAs", Inf. Sci., vol.192, no. 1, pp. 109119, 2012.
[11]Y. Gao, X. Hu, H. Liu, and Y. Feng, "Multiobjective estimation of distribution algorithm combined with PSO for RFID network optimization," presented at International Conference on Measuring Technology and Mechatronics Automation (ICMTMA),2010.
[12] J. Luo, Y. Qi, J. Xie, and X. Zhang, "A hybrid multiobjective PSO-EDA algorithm for reservoir flood control operation," Applied Soft Computing, vol. 34, pp. 526-538, 2015.
[13] Q. Xu, Ch. Zhang, J. Sun and Li. Zhang, "Adaptive Learning Rate Elitism Estimation of Distribution Algorithm Combining Chaos Perturbation for Large Scale Optimization" The Open Cybernetics \& Systemics Journal., vol. 10, pp.20-40,2016.
[14] Q. Zhang and H. Li, "Moea/d: A multiobjective evolutionary algorithm based on decomposition, "Evolutionary Computation, IEEE Transactions on, vol. 11, no. 6, pp. 712-731, 2007.
[15]Bo Wang; Hua Xu; Yuan Yuan, "Scale adaptive reproduction operator for decomposition based estimation of distribution algorithm," in Evolutionary Computation (CEC), 2015 IEEE Congress on, pp.20422049, 25-28 May 2015.
[16]Y. Li, A. Zhou, and G. Zhang, "A decomposition based estimation of distribution algorithm for multiobjective knapsack problems," in Natural Computation (ICNC),2012 Eighth International Conference on. IEEE, pp. 803-80, 2012.
[17]A. Zhou, Q. Zhang, and G. Zhang, "A multiobjective evolutionary algorithm based on decomposition and probability model," in Evolutionary Computation (CEC), 2012 IEEE Congress on. IEEE, pp. 1-8, 2012.
[18]V. A. Shim, K. Tan, and C. Cheong, "A hybrid estimation of distribution algorithm with decomposition for solving the multiobjective multiple traveling salesman problem," Systems, Man, and Cybernetics, Part C: Applications and Reviews, IEEE Transactions on, vol. 42, no. 5, pp. 682-691, 2012.
[19]A. Zhou, F. Guo, and G. Zhang, "A decomposition based estimation of distribution algorithm for multiobjective traveling salesman problems," Computers \& Mathematics with Applications, vol. 66, no. 10, pp. 1857-1868, 2013.
[20]V. A. Shim, K. C. Tan, and C. Y. Cheong, "A hybrid estimation of distribution algorithm with decomposition for solving the multiobjective multiple traveling salesman problem," IEEE Transactions on Systems, vol. 42, pp. 682-691, 2012.
[21] W. Dong, and X. Yao, "Unified eigen analysis on multivariate Gaussian based estimation of distribution algorithms", Inf. Sci., vol. 178, no.15, pp. 3000-3023, 2008.
[22] P.A. Bosman, and D Thierens, "Numerical optimization with real-valued estimation of distribution algorithms", In: Scalable Optimization via Probabilistic Modeling. Springer: Berlin, Heidelberg, 2006, pp. 91-120.
[23] S. Muelas, A. Mendibara, A. LaTorre, and J. Peña, "Distributed estimation of distribution algorithms for continuous optimization: How does the exchanged information influence their behavior?", Inf. Sci., vol. 268, pp. 231-254, 2014.
[24] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, "A fast and elitist multiobjective genetic algorithm: Nsgaii," Evolutionary Computation, IEEE Transactions on Evolutionary Computation, vol. 6, no. 2, pp. 182-197, 20