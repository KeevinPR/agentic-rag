# NSGA-II/EDA Hybrid Evolutionary Algorithm for Solving Multi-objective Economic/Emission Dispatch Problem 

Kehinde Olukunmi Alawode, ${ }^{1}$ Gabriel Adebayo Adegboyega, ${ }^{2}$ and Jubril Abimbola Muhideen ${ }^{2}$<br>${ }^{1}$ Department of Electrical and Electronic Engineering, Osun State University, Osogbo, Nigeria<br>${ }^{2}$ Department of Electronic and Electrical Engineering, Obafemi Awolowo University, Ile-Ife, Nigeria

## CONTENTS

1. Introduction
2. Economic/Emission Power Dispatch Problem
3. Non-dominated Sorting Genetic Algorithm/estimation Of Distribution Algorithm Hybrid (NSGA-II/EDA)
4. Test Results
5. Conclusions

References

Keywords: multi-objective evolutionary algorithm, hybrid evolutionary algorithm, combined economic-emission dispatch problem
Received 12 July 2016; accepted 26 May 2018
Address correspondence to A. M. Jubril, Department of Electronic and Electrical Engineering, Obafemi Awolowo University, Ile-Ife, Nigeria. E-mail: ajubril@oauife.edu.ng
Color versions of one or more of the figures in the article can be found online at www.tandfonline.com/uemp.


#### Abstract

In this study, a hybrid algorithm which combines the NSGA-II with a modified form of the marginal histogram model Estimation of Distribution Algorithm (EDA), herein called the NSGA-II/EDA is proposed for solving the multi-objective economic/emission power dispatch problem. The goal is to improve the convergence while preserving the diversity properties of the obtained solution set. The effect of variable interaction on the marginal histogram EDA model is reduced by performing multi-scale Principal Component Analysis on the population of solutions. Also, the concepts of non-domination and elitism have been introduced into the marginal histogram model in order for it to handle multiple objectives. Several optimization runs were carried out on the standard multi-objective test problems, including the IEEE 30- and the 118 -bus test systems. Standard metrics are used to compare the performance of the developed hybrid approach with that of other multi-objective evolutionary algorithms. The effectiveness of the proposed approach in improved convergence, with good diversity is demonstrated.


## 1. INTRODUCTION

The basic goal of any solution approach to solve the economic dispatch problem is to obtain the schedule of generating units in a power plant that will minimize the total generation cost while satisfying all unit and system equality and inequality constraints. However, thermal power plants produce sulfur dioxide $\left(\mathrm{SO}_{2}\right)$, nitrogen oxides, and carbon dioxide $\left(\mathrm{CO}_{2}\right)$ emissions in addition to air-borne inorganic particles such as fly ash and soot which can cause health and environmental problems, including global warming [1]. Different strategies to reduce atmospheric emissions include installation of pollutant-cleaning equipment, switching to low-emission fuels, and replacement of aged fuel burners and generator units [2, 3]. These approaches, however, lead to increased cost of operation and can be taken as long-term solutions. An attractive

short-term alternative is emission dispatching option in which both emission and generation cost are to be minimized [4]. This makes the problem a multi-objective optimization problem.

Several methods have been used in the literature to solve the multi-objective economic/emission power dispatch (EED) problem and they can be classified as classical, evolutionary algorithm (EA), and hybrid approaches. Classical aggregation methods include the weighted sum method [5] and the $\epsilon$-constraint method [6, 7]. In the weighted sum method, the two objectives are linearly combined into one by forming their weighted sum. Although this method is simple to implement, it requires multiple runs with different weights to obtain different non-dominated solutions. It also cannot find Pareto-optimal solutions located in a non-convex Pareto-optimal front [8, 9]. The $\epsilon$-constraint method optimizes a most preferred objective and restricts the others within user-specified values. The method overcomes difficulties experienced by the weighted sum method in non-convex solution spaces but the obtained solution set depends on proper choice of the $\epsilon$-vector [10].

EA methods are nature-inspired, population-based approaches which can find multiple Pareto-optimal solutions in a single optimization run. They are also less susceptible to the shape or continuity of the Pareto front [9]. The multi-objective EED problem was solved using the Strength Pareto Evolutionary Algorithm (SPEA), Niched Pareto Genetic Algorithm (NPGA), and Non-dominated Sorting Genetic Algorithm (NSGA) in [8, 11] and [12], respectively. A comparative study on the performance of the NPGA, NSGA, and the SPEA was presented in [4]. The study concluded that SPEA performed better in solving the EED problem. The elitist NSGA-II and a later improvement to it called NSGA-III were applied to solve both the EED problem in [13] and [14], respectively. Evolutionary programing [15, 16], differential evolution [17], and other nature-inspired algorithms such as ant colony optimization [18], harmony search [19], and simulated annealing [20] have also been used to solve the economic/ emission dispatch problem. A hybrid algorithm based on particle swarm optimization and gravitational search algorithm was presented in [21].

In spite of the successes of EAs in solving complex optimization problems, there is no guarantee of convergence to the "true" Pareto-optimal front [22]. Different hybrid approaches have been developed to improve the quality of solutions obtained by these EAs. A review of different hybrid architectures reported in the literature is
given by [23] and these include hybridization between different EAs [24], neural network assisted EA [25], and Ant Colony Optimization assisted EA [26].

### 1.1. Contributions

Although the NSGA-II has been widely used to solve different multi-objective optimization problems, it still faces the computational challenge associated with populationbased algorithms in converging to Pareto-optimal front while simultaneously maintaining the spread of its population along the entire front [27]. In this study, a hybrid algorithm, NSGA-II/EDA, which combines good diversity property of NSGA-II with guaranteed uniform convergence of marginal histogram model Estimation of Distribution Algorithm (EDA) [28], is presented for solving the multiobjective optimization problems. The effect of variable interaction on the marginal histogram EDA model is reduced by performing multi-scale Principal Component Analysis (MSPCA) on the population of solutions. Also, the concepts of non-domination and elitism have been introduced into the marginal histogram model in order for it to handle multiple objectives.

Several runs were carried out on standard multiobjective optimization problems, including the IEEE 30and the 118 -bus test systems. Standard metrics are used to compare the performance of the developed hybrid approach with that of other multi-objective evolutionary algorithms (MOEAs). The effectiveness of the proposed approach in improving convergence and diversity in the obtained solution set is demonstrated.

## 2. ECONOMIC/EMISSION POWER DISPATCH PROBLEM

The EED problem seeks to minimize two conflicting objective functions, fuel cost and emission while satisfying equality and inequality constraints imposed by different requirements of the power system. The problem can be represented mathematically as

$$
\begin{array}{ll}
\operatorname{minimize} & {\left[F\left(P_{G}\right), E\left(P_{G}\right)\right]} \\
\text { subjectto: } & g_{j}\left(P_{G}\right) \leq 0, \quad j=1,2, \ldots, J ; \\
h_{k}\left(P_{G}\right)=0, \quad k=1,2, \ldots, K ; \\
& P_{G i}^{\min } \leq P_{G i} \leq P_{G i}^{\max }, \quad i=1,2, \ldots, N ;
\end{array}
$$

where $F\left(P_{G}\right)$ and $E\left(P_{G}\right)$ are the fuel cost and emission cost functions, respectively; $g_{j}$ are the equality constraints, and $h_{k}$ are the inequality constraints. $P_{G i}$ is the real power output of the $i$ th generator. $P_{G}$ is the vector of real power output of

generators and is defined as $P_{G}=\left[P_{G 1}, P_{G 2}, \ldots, P_{G N}\right]^{T} . N$ is the number of generating units while $J$ and $K$ are the number of inequality and equality constraints, respectively.

### 2.1. Problem Objectives

2.1.1. Total Fuel Cost Objective Function. The total fuel $\operatorname{cost} F\left(P_{G}\right)$ in $/ h$ is represented by a quadratic function and can be expressed as [4]

$$
F\left(P_{G}\right)=\sum_{i=1}^{N}\left(a_{i} P_{G i}^{2}+b_{i} P_{G i}+c_{i}\right)
$$

where $a_{i}, b_{i}, c_{i}$ are the fuel cost coefficients of the $i$ th generator.
2.1.2. Emission Objective Function. The total emission of atmospheric pollutants $E\left(P_{G}\right)$ in ton/h can be expressed as [8]

$$
E\left(P_{G}\right)=\sum_{i=1}^{N} 10^{-2}\left(d_{i} P_{G i}^{2}+e_{i} P_{G i}+f_{i}\right)+g_{i} \exp \left(h_{i} P_{G i}\right)
$$

where $d_{i}, e_{i}, f_{i}, g_{i}, h_{i}$ are the coefficient of the $i$ th generator emission characteristics.

### 2.2. Problem Constraints

2.2.1. Generation Capacity Constraint. The real power output of each generator is restricted by its lower and upper limits such that

$$
P_{G i}^{\min } \leq P_{G i} \leq P_{G i}^{\max }
$$

2.2.2. Power Balance Constraint. The total power generated must be sufficient to meet the load demand $P_{D}$, taking into consideration the real power losses $P_{L}$ during transmission, i.e.

$$
\sum_{i=1}^{N} P_{G i}-P_{D}-P_{L}=0
$$

$P_{L}$ is calculated from the system's transmission loss coefficients $B, B_{0}$ and $B_{00}$ using

$$
P_{L}=\sum_{i=1}^{N} \sum_{j=1}^{N} P_{G i} B_{i j} P_{G j}+\sum_{i=1}^{N} B_{0 i}+B_{00}=0
$$

As a multi-objective optimization problem, the objectives are usually conflicting in nature, this implies that the objectives cannot be simultaneously minimized; hence, such problems give rise to a set of Pareto-optimal solutions
rather than a single optimal solution. The set of objective vectors corresponding to the Pareto set is called the Paretooptimal front [29].

### 2.3. Performance Metrics

There are two basic requirements of a good multi-objective optimization algorithm [9]:

1. To find a set of solutions as close as possible to the ideal Pareto-optimal front, called the convergence requirement; and
2. To find a set of solutions as diverse as possible, also called the diversity requirement.
These two requirements form the basis of the performance metrics for assessing various MOEAs. Some of the important performance measures in the literature are discussed as follows:
2.3.1. Set Coverage Metric. This metric suggested in [30] evaluates convergence to the Pareto front. It is used to get an idea of the relative spread of solutions between two sets of solution vectors A and B. The set coverage metric $\mathbf{C}(A, B)$ calculates the proportion of solutions in B, which are weakly dominated by solutions of A:

$$
\mathbf{C}(A, B)=\frac{|\{b \in B \mid \exists a \in A: a \leqslant b\}|}{|B|}
$$

2.3.2. Spacing Metric. This diversity metric [31] measures how uniformly spaced solutions in the obtained nondomination set $Q$ are. It is given by

$$
S=\sqrt{\frac{1}{|Q|} \sum_{i=1}^{|Q|}\left(d_{i}-\bar{d}\right)^{2}}
$$

where

$$
d_{i}=\min _{k \in Q \wedge k \neq i} \sum_{m=1}^{M}\left|f_{m}^{i}-f_{m}^{k}\right|
$$

and

$$
\bar{d}=\sum_{i=1}^{|Q|} d_{i} /|Q|
$$

When the solutions are near uniformly spaced, the corresponding distance measure will be small. Thus, an algorithm finding a set of non-dominated solutions having a smaller spacing is better.
2.3.3. Extent Metric. This measure of diversity defined in [30] is also called the maximum spread metric. It measures

the length of the diagonal of a hyperbox formed by the extreme values observed in the non-dominated set $Q$

$$
D=\sqrt{\sum_{m=1}^{M}\left(\max _{i=1}^{|Q|} f_{m}^{i}-\min _{i=1}^{|Q|} f_{m}^{i}\right)^{2}}
$$

An algorithm finding a set of non-dominated solutions having a larger extent value is better.
2.3.4. Contribution to Reference Pareto Front. In this convergence metric suggested in [4], all non-dominated sets obtained by the different techniques over all optimization runs are combined to form a pool. An index to each solution is added to refer to the associated technique. Then, the dominance conditions are applied for all solutions in the pool and the non-dominated solutions are extracted from it to form an elite set of Pareto-optimal solutions obtained by all techniques. The percentage contribution of each technique to this reference Pareto set is a measure of its convergence property.

## 3. NON-DOMINATED SORTING GENETIC ALGORITHM/ESTIMATION OF DISTRIBUTION ALGORITHM HYBRID (NSGA-II/EDA)

The elitist NSGA-II is one of the most attractive multiobjective evolutionary optimization algorithms due to its simple structure, availability, the existence of experience in practical applications, and its excellent performance on the majority of test problems [32]. It, however, has the problem of restricted and non-uniform convergence due to its usage of crowded comparison. The EDA is EAs that do not use conventional crossover and mutation operators, but estimates the distribution of the selected promising population and then samples from this distribution. Although it is designed to handle single-objective function, its ability to build and select from the promising population ensures a uniform convergence of its solution. In order to improve the performance of the NSGA-II in terms of its convergence, while preserving its diversity characteristics, it is hybridized with a modified form of the marginal histogram model EDA. The resulting hybrid EA is herein called the NSGA-II/EDA.

### 3.1. Elitist NSGA

The elitist NSGA-II uses an elite-preserving strategy to enhance convergence as well as an explicit diversity preserving mechanism to preserve diversity [9]. An offspring population $Q_{t}$ of size $N$ is first created from a randomly
generated parent population $P_{t}$ by using the binary tournament selection, crossover, and mutation genetic operators. The two populations are then combined together and each solution is assigned a rank by sorting the combined population into different non-dominated fronts. A secondary ranking measure called the crowding distance which is a measure of the population density around each solution is also assigned to each solution in the population. The best $N$ members of the combined population are selected on the basis of rank and crowding distance.

The details of the steps involved in the implementation of NSGA-II can be found in [33]. A modification of the original NSGA-II which utilizes a dynamic crowding distance (DCD) assignment strategy can be found in $[34,35]$.

### 3.2. Modified Marginal Histogram Model EDA

EDA [36] is a branch of EAs that do not use conventional crossover and mutation operators, but instead estimates the distribution of the selected "parent" population and then samples from this distribution. EDAs build a model based on selected promising solutions and depending on the complexity of such a model, they lead to the production of better offspring solutions. This is unlike the random crossover and mutation operators which do not guarantee the production of better offsprings as they can cause disruption of good solutions and convergence to local optimum.

An EDA approach that uses both the fixed width and the fixed height marginal histogram models for estimating the probability distribution of promising solutions was presented in [28]. The models were found to work well with single-objective test functions with no or weak interaction among the variables. To achieve a more efficient exploration and exploitation of the search space, the surrounding effect and shrinking strategies were introduced into the model in [38].
3.2.1. Fixed Width Marginal Histogram Model EDA. To construct the fixed width marginal histogram model, let the current population of size $N$ be $\left(x^{1}, x^{2}, \ldots x^{N}\right)^{T}$ from which $S$ solutions are selected by tournament selection to constitute the "parent" population. The search space $\left[a_{i}, b_{i}\right]$ of each variable is divided into $H$ sub-intervals (or bins) such that the $j$ th sub-interval is $\left[a_{i}+\frac{j-1}{H}\left(b_{i}-a_{i}\right), a_{i}+\right.$ $\left.\frac{j}{H}\left(b_{i}-a_{i}\right)\right),(1 \leq j \leq H)$. The number of selected solutions whose values of $x_{i}$ fall in the $j$ th bin, $W(i, j)$ is then determined. For each bin, the model $M$ is formed from the

marginal probability density of $x_{i}$ given by
$p_{i}\left(x_{i}\right)= \begin{cases}\frac{W(i, 1)}{S} \cdot \frac{H}{b_{i}-a_{i}} & a_{i} \leq x_{i} \leq a_{i}+\frac{1}{H}\left(b_{i}-a_{i}\right) \\ \frac{W(i, 2)}{S} \cdot \frac{H}{b_{i}-a_{i}} & a_{i}+\frac{1}{H}\left(b_{i}-a_{i}\right) \leq x_{i} \leq a_{i}+\frac{2}{H}\left(b_{i}-a_{i}\right) \\ \frac{W(i, H)}{S} \cdot \frac{H}{b_{i}-a_{i}} & a_{i}+\frac{H-1}{H}\left(b_{i}-a_{i}\right) \leq x_{i} \leq b_{i}\end{cases}$
A new solution $\tilde{x}=\left(\tilde{x_{1}}, \tilde{x_{2}}, \ldots, \tilde{x_{n}}\right)$ is generated by sampling the value of each $x_{i}$ from Eq. (12) independently. This is repeated until the desired number of solutions is sampled.
3.2.2. Modifications to the Marginal Histogram EDA. Since the marginal histogram model EDA does not take variable interaction into consideration and it has only been applied to solving single-objective optimization problems, the following modifications have been introduced into the original algorithm for the marginal histogram EDA in order to improve its effectiveness and adapt it for solving multiobjective optimization problems:

1. MSPCA [39] is carried out on the selected set of promising solutions in order to reduce the effect of variable interactions on the quality of the model developed. MSPCA extracts the principal components of the selected solution set to yield a solution set with reduced dimensionality and variable interaction.
2. The population of solutions is sorted into different nondominated fronts and crowding distance is assigned to each solution.
3. Elitism is also introduced by forming a combination of the old and new populations before selecting the desired number of solutions to propagate to the next generation.
MSPCA combines the ability of PCA to extract the cross-correlation or relationship between the variables, with that of orthonormal wavelets to separate deterministic features from stochastic processes and approximately decorrelate the autocorrelation among the measurements [40]. Principal component analysis is used to track new factors capturing the main features [41]. Wavelets, on the other hand, have found wide use in signal analysis and noise removal in various fields of study due to their ability to represent deterministic and stochastic features in terms of different coefficients. MATLAB's Wavelet Toolbox contains the implementation of MSPCA used in this study. The concepts of non-dominated sorting, crowding distance
assignment, and elitism are directly carried over from the NSGA-II implementation.

The steps involved in the implementation of the modified fixed width marginal histogram model are outlined in Algorithm 1.

### 3.3. NSGA-II/EDA Hybrid Evolutionary Algorithm

Algorithm 2 outlines the steps involved in the proposed NSGA-II/EDA hybrid algorithm. NSGA-II is run alone during the first gen $/ 2$ generations to produce a diverse set of non-dominated solutions, where gen is the maximum number of generations which determines the stopping criterion. In each of the remaining gen/2 cycles, the modified fixed width marginal histogram EDA is used to improve solutions obtained by NSGA-II.

Feasibility of the obtained solution set is maintained by using the constrained-domination principle discussed in [33] while performing non-dominated sorting. The effect of using this approach is that any feasible solution is assigned a better non-domination rank than any infeasible solution. All feasible solutions are ranked according to their nondomination level based on the objective function values. However, among two infeasible solutions, the solution with a smaller constraint violation has a better rank.

```
Algorithm 1. Modified marginal histogram model EDA
INPUT: Generation counter \(t=0\), random population \(P(t=0)\) of
    size \(N\), maximum number of generations gen, number of bins \(H\)
OUTPUT: \(P(t=\) gen\).
    1: Evaluate the multiple objective function values of the solution
    vectors in \(P(t)\)
    2: Perform non-dominated sorting
    3: Assign crowding distance to each solution
    4: Select a set of promising solutions \(S(t)\) from \(P(t)\) using
    tournament selection
    5: Perform multi-scale principal component analysis of the
    promising solution set \(\mathrm{S}(\mathrm{t})\) to yield a simplified solution
    set \(I(t)\)
    6: Divide the search space of each variable of \(I(t)\) into \(H\) sub-
    intervals or bins
    7: Construct a marginal histogram model \(M(t)\) of the vector
    values in \(I(t)\)
    8: Sample a set of new solution vectors \(O(t)\) from \(M(t)\)
    9: Evaluate the multiple objective function values of the solution
    vectors in \(O(t)\)
    10: Form \(R(t)\) by combining \(O(t)\) with \(P(t)\), then sort \(R(t)\) into
    different non-domination levels and assign crowding distance
    to each solution
    11: Create a new population \(P(t+1)\) by selecting the best \(N\)
    solutions from \(R(t)\) based on non-domination level and
    crowding distance information
12: Increment \(t\) by unity
```

13: if $t$ is not greater than gen then
14: Repeat Steps 4-12
15: end if
16: Obtain solutions in $P(t)$

## Algorithm 2. NSGA-II/EDA hybrid EA

INPUT: Generation counter $t \leftarrow 0$, population $P(t)$ of size $N$, number of generations gen, number of bins $H$, UseEDA $=$ True/False
OUTPUT: Non-dominated solution set $P_{h t h}(t=\operatorname{gen})$
1: Initialize population $P(t)$ of size $N$
2: Evaluate multiple objective function values of the population
3: Assign rank (level) to each solution based on nondominated sorting
4: for $t=1$ to gen do
5: Generate child population of size $N$ using binary tournament selection, recombination and mutation operators
6: Evaluate objective function values for the child population
7: Combine parent and child populations to have a combined intermediate population of size $2 N$
8: Assign rank to each solution based on non-dominated sorting
9: Assign crowding distance to each solution
10: Select best $N$ solutions from the combined population on the basis of their ranks and crowding distances
11: Form new parent population $P_{\text {seqs2 }}$ by replacing old parent population with the selected $N$ solutions
12: if $\left(t>\binom{\frac{2 N}{2}}{2}\right) \& \&$ UseEDA $==$ True) then
13: Select a set of promising solutions $S(t)$ from $P_{\text {seqs2 }}$ using tournament selection
14: Perform multi-scale principal component analysis of the promising solution set $\mathrm{S}(\mathrm{t})$ to yield a simplified solution set $I(t)$
15: Divide the search space of each variable of $I(t)$ into $H$ subintervals or bins
16: Construct a marginal histogram model $M(t)$ of the vector values in $I(t)$
17: Sample a set of new solution vectors $P_{c o l a}$ from $M(t)$
18: Evaluate the multi-objective function values of the solution vectors in $P_{\text {cola }}$
19: Form $P_{\text {comb }}$ by combining $P_{\text {cola }}$ with $P_{\text {seqs2 }}$, then sort $P_{\text {comb }}$ into different non-domination levels and assign crowding distance to each solution
20: Create a new population $P_{h t h}$ by selecting the best $N$ solutions from $P_{\text {comb }}$ based on non-domination level and crowding distance information
21: end if
22: end for

### 3.4. Selecting a Compromise Solution

Since NSGA-II and the hybrid, NSGA-II/EDA, yield a population of non-dominated solutions to the multiobjective EED problem, a decision-maker has to choose a
particular solution from the non-dominated solutions generated by the algorithms. A fuzzy-based cardinal priority ranking of the non-dominated solutions has been used in this study to extract a compromise solution for the decision-maker to work with $[4,42]$.

For each of the objective functions $F_{m}$, the solution in the Pareto-optimal set is represented by a membership function $\mu_{m}$ defined as [43]:

$$
\mu_{m}=\left\{\begin{array}{cc}
1 ; & F_{m} \leq F_{m}^{\min } \\
\frac{F_{m}^{\max }-F_{m}}{F_{m}^{\max }-F_{m}^{\min }} ; & F_{m}^{\min } \leq F_{m} \leq F_{m}^{\max } \\
0 ; & F_{m} \geq F_{m}^{\max }
\end{array}\right.
$$

where $F_{m}^{\min }$ and $F_{m}^{\max }$ are the maximum and minimum values of the $m$ th objective function, respectively. The membership function represents the degree of achievement of the $m$ th objective function with $\mu_{m}=1$ as completely satisfactory and $\mu_{m}=0$ as unsatisfactory.

For each non-dominated solution $k$, the normalized membership function is calculated as

$$
\mu^{k}=\frac{\sum_{m=1}^{N_{c o l a}} \mu_{m}^{k}}{\sum_{j=1}^{N, k} \sum_{m=1}^{N_{n} / i j} \mu_{m}^{j}}
$$

where $N$ is the number of non-dominated solutions. The chosen compromise solution is the one having the maximum of $\mu^{k}$.

## 4. TEST RESULTS

The implementation of NSGA-II/EDA for the EED problem was done using version 7.8.0 (R2009a) of MATLAB language on an Intel Core Duo processor running at 2.33 GHz with 1 GB RAM.

### 4.1. Multi-objective Benchmark Test Functions

The performance of NSGA-II/EDA is compared with that of the stand-alone NSGA-II and SPEA2 techniques on some bi-objective test functions, namely ZDT1, ZDT3, ZDT6, and KUR, which are commonly used in evaluating the performance of multi-objective optimization techniques. The details of these problems can be found in [11]. Each algorithm was run for a total of 22,500 function evaluations with a population size of 75 . The number of generations was set at 300 and 200 for NSGA-II and NSGA-II/EDA, respectively. Figures 1-4 are typical Pareto fronts obtained at the end of the specified number of function evaluations.

![img-0.jpeg](img-0.jpeg)

FIGURE 1. Non-dominated solutions of KUR.
![img-1.jpeg](img-1.jpeg)

FIGURE 2. Non-dominated solutions of ZDT1.
![img-2.jpeg](img-2.jpeg)

FIGURE 3. Non-dominated solutions of ZDT3.

The figures show the effectiveness of NSGA-II/EDA in solving the test problems.

### 4.2. IEEE Test Systems Description

The standard IEEE 30 -bus 6 generator and IEEE 118-bus 54 generator test systems have been used to demonstrate
![img-3.jpeg](img-3.jpeg)

FIGURE 4. Non-dominated solutions of ZDT6.
the effectiveness of the hybrid NSGA-II/EDA in solving the EED problem. The IEEE 30 -bus system has a total load of 283.4 MW and its line and bus data were taken from [4]. Details of the IEEE 118-bus system parameters with a total load of 4242 MW can be found in MATPOWER [44]. The values of the generator cost and emission coefficients for the 30 -bus system are provided in [4]. Generator cost coefficients for the 118 -bus system were taken from [44] while the emission coefficients for the system were taken from [44].

### 4.3. Parameter Settings for NSGA-II and NSGAII/EDA

The same initial random population has been used for both NSGA-II and NSGA-II/EDA and several simulation runs were first carried out to set their parameters. Table 1 shows the values of the population size $N$, number of generations, gen, crossover and mutation probabilities as well as the number of bins, $H$ used in the implementation of the algorithms for both the IEEE 30-bus and 118-bus test systems. Values of $N$ and gen were selected such that both NSGA-II and NSGA-II/EDA have the same number of function evaluations in each run. The mutation probability was chosen as $1 / V$, where $V$ is the number of decision variables ( $V=6$ for the IEEE 30 -bus system and $V=54$ for the 118 -bus system). The number of bins was selected to be equal to $V+1$. The distribution indices for crossover and mutation were set equal to 20 for both algorithms.

### 4.4. Results and Discussion

In order to establish a good basis for comparing both NSGA-II and NSGA-II/EDA, 12 different optimization runs were carried out for each algorithm and their performance compared by considering their best solutions for both

TABLE 1. Parameter settings for IEEE 30-bus and 118-bus test systems.
minimum fuel cost and minimum emissions. Further comparison was also done in terms of the performance metrics discussed in Section 2.3.
4.4.1. Best Solutions for Fuel Cost and Emission. Figures 5 a and b show the Pareto-optimal fronts obtained by both NSGA-II and NSGA-II/EDA during the best optimization run carried out using data for the IEEE 30-bus and 118-bus systems, respectively. The figures represent the tradeoff between fuel cost and emissions. They indicate that NSGA-II/EDA is able to find non-dominated solutions with good convergence and diversity characteristics. The extreme solutions in Figure 5 for both NSGA-II and NSGA-II/EDA are the solutions corresponding to minimum fuel cost and minimum emissions.

For the IEEE 30-bus system, the generation schedules that will yield the minimum fuel cost (along with the corresponding emission) are given in Table 2 with the best fuel cost value that was achieved rendered in bold numerals. The table also shows the best fuel cost solutions that were obtained by other EA techniques for the same EED problem. NSGA-II/EDA returned the lowest value for minimum fuel cost. Similarly, the generation schedules that will lead to minimum gaseous emissions are given in Table 3. NSGA-II and NSGA-II/EDA returned the same lowest value for minimum emissions.

Table 4 shows the best fuel cost and emission values obtained by both algorithms for the IEEE 118-bus test case. The generation schedules that will yield these minimum values are however not shown due to space constraints. The NSGA-II/EDA hybrid algorithm returned a clearly lower value for minimum fuel cost than the standalone NSGA-II. On the other hand, NSGA-II yielded a lower minimum emissions value than the hybrid algorithm.
4.4.2. Performance Metric Results. For a qualitative comparison of the performance of the stand-alone NSGA-II with the hybrid NSGA-II/EDA algorithm, the set coverage metric was used to compare the convergence of solutions obtained by both algorithms while the extent and spacing
![img-4.jpeg](img-4.jpeg)
(b)IEEE118-bussystem

FIGURE 5. Pareto-optimal fronts for best optimization runs: (a) IEEE 30-bus system and (b) IEEE 118bus system.
metrics were used to compare the solution sets in terms of diversity. The convergence property was also measured using the percentage contribution of each algorithm to a reference Pareto front.
(a) Set Coverage, Extent and Spacing Metrics for IEEE 30-Bus System.. Figure 6 shows boxplots of the different performance metrics for the IEEE 30-bus test system.


TABLE 2. Best solutions out of twelve runs for fuel cost (IEEE 30-bus).


TABLE 3. Best solutions out of twelve runs for emission (IEEE 30-bus). The bold was to show the best values computed for all the algorithms.


TABLE 4. Best fuel cost and emission out of twelve runs (IEEE 118-bus).
The bold was to show the best values computed for all the algorithms.

From the set coverage metric values shown in Figure 6a, NSGA-II/EDA consistently yielded solutions which dominated those obtained by NSGA-II. A median $61 \%$ of solutions obtained by NSGA-II were dominated by those of NSGA-II/EDA while only about $13 \%$ of NSGA-II/EDAobtained solutions were dominated by those of NSGA-II. These median values are significantly different at the $5 \%$ significance level since the regions indicated by the triangular markers in the plot for each algorithm do not intersect [39]. Thus, the hybrid NSGA-II/EDA algorithm yielded solutions with better convergence properties than NSGA-II.

Figure 6b shows that the median extent metric values are 42.6585 and 43.8486 for NSGA-II and NSGA-II/EDA, respectively. These values are significantly different at the $5 \%$ significance level. Since NSGA-II/EDA gave the higher value, its solution sets are better than those of NSGA-II in terms of maximum spread.

Similarly, from Figure 6c, the median spacing metric value is 0.5342 for NSGA-II and 0.5232 for NSGA-II/ EDA. Although the lower median value obtained for NSGA-II/EDA is desirable, it is not significantly different from that of NSGA-II (since the regions marked out by the triangles in each boxplot of Figure 6c intersect). Hence, the values obtained by both NSGA-II and NSGA-II/EDA are comparable.
(b) Set Coverage, Extent and Spacing Metrics for IEEE 118-Bus System.. Figure 7 shows boxplots of the different performance metrics for the IEEE 118-bus test system. From the set coverage metric values shown in Figure 7a, NSGA-II/EDA consistently yielded solutions which dominated those obtained by NSGA-II. A median $57.5 \%$ of solutions obtained by NSGA-II were dominated by those of NSGA-II/EDA while only about $8.5 \%$ of NSGA-II/EDA-

![img-5.jpeg](img-5.jpeg)

FIGURE 6. Performance metric boxplots (IEEE 30-bus system): (a) Boxplot of set coverage metric values, (b) Boxplot of extent metric values, and (c) Boxplot of spacing metric values.
(a)
![img-6.jpeg](img-6.jpeg)
(b)
![img-7.jpeg](img-7.jpeg)
(c)
![img-8.jpeg](img-8.jpeg)

FIGURE 7. Performance metric boxplots (IEEE 118-bus system): (a) Boxplot of set coverage metric values, (b) Boxplot of extent metric values, and (c) Boxplot of spacing metric values.

![img-9.jpeg](img-9.jpeg)

FIGURE 8. Percentage contribution to reference Pareto front: (a) IEEE 30-bus system and (b) IEEE 118bus system.
obtained solutions were dominated by those of NSGA-II. These median values are significantly different at the $5 \%$ significance level since the regions indicated by the triangular markers in the plot for each algorithm do not intersect. Thus the hybrid NSGA-II/EDA algorithm yielded solutions with better convergence properties than NSGA-II.

Figure 7b shows that the median extent metric values are 503.4368 and 507.3151 for NSGA-II and NSGA-II/ EDA, respectively. Although the value for NSGA-II/EDA is higher, the extent values are not significantly different at the $5 \%$ significance level (since the regions marked out by the triangles in each boxplot of the figure intersect), hence they are comparable.

Similarly, Figure 7c shows that the median spacing metric value is 1.9287 for NSGA-II and 1.8615 for NSGA-II/ EDA. Although the lower median value obtained for NSGA-II/EDA is desirable, it is not significantly different from that of NSGA-II. Hence, the values obtained by both NSGA-II and NSGA-II/EDA are comparable.
(c) Contribution to Reference Pareto Front.. Figure 8a shows the percentage contribution of each of NSGA-II and NSGA-II/EDA to the reference Pareto front extracted from the solutions obtained over all runs for the IEEE 30-bus system test case. While NSGA-II contributed about $30 \%$ of solutions in the reference Pareto set, NSGA-II/EDA contributed the balance of almost $70 \%$. For the IEEE 118-bus test system (see Figure 8b), NSGA-II/EDA contributed $84 \%$ of the reference Pareto set that was extracted. These figures show that the hybrid NSGA-II/EDA algorithm possesses improved convergence characteristics than NSGA-II.

## 5. CONCLUSIONS

This paper presents a hybrid EA developed from the elitist NSGA and the modified marginal histogram model EDA. This algorithm called the NSGA-II/EDA has been used in this study to solve the EED problem using the IEEE 30bus and 118 -bus test system datasets. The effectiveness of the developed hybrid algorithm in improving the convergence while maintaining the diversity properties of the obtained solution set over the stand-alone NSGA-II algorithm has also been demonstrated.
