# Estimation of distribution algorithm enhanced particle swarm optimization for water distribution network optimization 

Xuewei Q1 ${ }^{1}$, Ke LI ( $\boxtimes)^{2}$, Walter D. POTTER ${ }^{3}$<br>1 Department of Electrical and Computer Engineering, University of California, Riverside, CA 92507, USA<br>2 College of Engineering, University of Georgia, Athens, GA 30605, USA<br>3 Institute of Artificial Intelligence, University of Georgia, Athens, GA 30605, USA

(c) Higher Education Press and Springer-Verlag Berlin Heidelberg 2015


#### Abstract

The optimization of a water distribution network (WDN) is a highly nonlinear, multi-modal, and constrained combinatorial problem. Particle swarm optimization (PSO) has been shown to be a fast converging algorithm for WDN optimization. An improved estimation of distribution algorithm (EDA) using historic best positions to construct a sample space is hybridized with PSO both in sequential and in parallel to improve population diversity control and avoid premature convergence. Two water distribution network benchmark examples from the literature are adopted to evaluate the performance of the proposed hybrid algorithms. The experimental results indicate that the proposed algorithms achieved the literature record minimum ( 6.081 M\$) for the small size Hanoi network. For the large size Balerma network, the parallel hybrid achieved a slightly lower minimum $(1.921 \mathrm{M} €)$ than the current literature reported best minimum $(1.923 \mathrm{M} €$ ). The average number of evaluations needed to achieve the minimum is one order smaller than most existing algorithms. With a fixed, small number of evaluations, the sequential hybrid outperforms the parallel hybrid showing its capability for fast convergence. The fitness and diversity of the populations were tracked for the proposed algorithms. The track record suggests that constructing an EDA sample space with historic best positions can improve diversity control significantly. Parallel hybridization also helps to improve diversity control yet its effect is relatively less significant.


Keywords particle swarm optimization (PSO), diversity control, estimation of distribution algorithm (EDA), water distribution network (WDN), premature convergence, hybrid strategy

[^0]
## 1 Introduction

A water distribution network (WDN) is a network of components (e.g. pipes, pumps, valves, tanks, etc.) that transports water from a source (e.g. reservoir, treatment plant, tank, etc.) to the consumers (e.g. domestic, commercial, and industrial users). Due to the substantial cost associated with the installation and material of WDN, it is necessary to optimize its design by selecting the lowest cost combination of appropriate component sizes and component settings while the hydraulic and resilience constraints are satisfied. In water industry practice, the diameter of the pipeline determines the size of components and the installation cost. Therefore, the selection of pipe diameters, namely pipe sizing, becomes the classical WDN optimization challenge.

In the past three decades, a variety of optimization methods for WDN have been proposed. Pioneer researchers in this field attempted to solve this optimization problem with classical operational research techniques (including linear programming, dynamic programming, and nonlinear programming). These models were mostly applied to branched networks and relied heavily on the starting point in the search process to avoid local optima [1-3]. With the development of evolutionary algorithms (EAs), many EAs have been introduced to optimize WDN design [4-7]. High computational expense and premature convergence were common challenges for existing algorithms. Only a few algorithms were tested on large scale network examples.

In the past decade, particle swarm optimization (PSO) was introduced to optimize WDN and proved successful due to its low computational complexity and fast convergence rate $[8,9]$. Compared to other heuristic search algorithms, PSO converges quickly during the early stage of the search process [10]. However, premature convergence remains a challenge and the search process is apt to


[^0]:    Received November 3, 2014; accepted January 20, 2015
    E-mail: keli@engr.uga.edu

be trapped in a local optimum especially for complex multi-modal-search problems such as WDN optimization [11,12]. This could be detrimental when the problem has high dimensionality. Parameter tuning is a conventional way to improve PSO performance as well as address parameter convergence yet fast diversity lose is still a challenge. Most recent efforts to tackle premature convergence were through topology control [13-15], randomness injection [16,17], and, hybridization [18]. Of the three abovementioned strategies, hybridization is gaining popularity for preventing premature convergence of the evolutionary algorithm. One research trend that emerged in the past few years is the hybridization of PSO with estimation of distribution algorithms (EDAs). This type of hybrid has been shown to be successful in many global optimization problems [19-24] but not yet applied in the optimization of water networks. The major benefit of hybridizing PSO with EDA is that EDA can help to keep diversity in the PSO population.

This paper attempts to enhance water network optimization through a new way of utilizing EDA to improve the capability of PSO to search for global optima. The novelty lies in the hypothesis that information contained in the historical generations can be used to help search global optimum. Constructing an EDA sampling space based on the best of all previous generations may preserve population diversity and increase the chance of finding global optima, which means prevention of premature convergence. The proposed algorithms are applied to two benchmark water distribution networks to demonstrate their capability for solving the WDN optimization problem. The optimization results are comprehensively compared to existing algorithms with the same benchmarks. The mechanism for diversity preservation in the PSO is also discussed.

## 2 Methodologies

2.1 Problem formulation and representation

Pipe size optimization for a water distribution network with a pre-specified layout can be described as:

$$
\text { Minimize } C_{\text {total }}=\sum_{1}^{N} C_{i} L_{i}
$$

where $C_{\text {total }}$ is the total cost of all the pipes in the network; $L_{i}$ is the length of the $i^{\text {th }}$ link; $C_{i}$ is the cost per unit length of the pipe used in $i^{\text {th }}$ link; and $N$ is the number of the links (pipes) used in the network. The above minimization is subject to the following constraints:

- Hydraulic constraints:

$$
\begin{gathered}
\sum_{\mathrm{in}(k)} q_{i} \cdot \sum_{\text {out }(k)} q_{i}=Q_{k} \quad k=1,2, \cdots, M \\
\sum_{i \in L} J_{i}=0, i=1,2, \cdots, N
\end{gathered}
$$

$$
q_{i}=K c h_{i} d_{i}^{\alpha}\left(J_{i} / J_{i}\right)^{\beta}
$$

where $M$ and $L$ are the number of existing nodes and loops in the network respectively; $q_{i}$ is the flow rate in the $i^{\text {th }}$ pipe; $Q_{k}$ s the required demand at consumption node $k ; J_{i}$ is the head loss in the $i^{\text {th }}$ pipe; $c h_{i}$ is the Hazen-Williams coefficient for the $i^{\text {th }}$ pipe and $\alpha=2.63, \beta=0.54$, and $K=$ 0.281 for $q$ in cubic meters and $d$ in meters. These constraints, therefore, describe the flow continuity at nodes, head loss balance in loops and the Hazen-Williams equation.

- Head loss equation (Darcy-Weisbach equation)

$$
h_{f}=f_{D} \frac{L}{D} \frac{V^{2}}{2 g}
$$

where $h_{f}$ is the head loss due to friction (SI units: $\mathrm{m} ; \mathrm{L}$ is the length of the pipe $(\mathrm{m}) ; D$ is the hydraulic diameter of a pipe (for a circular section pipe, this equals the internal diameter of the pipe) (m); $V$ is the average velocity of the fluid flow, equal to the volumetric flow rate per unit crosssectional wetted area ( $\mathrm{m} / \mathrm{s}) ; \mathrm{g}$ is the local acceleration due to gravity $\left(\mathrm{m} / \mathrm{s}^{2}\right)$; and, $f_{D}$ is a dimensionless coefficient called the Darcy friction factor.

- Head constraints:

$$
H_{\min } \leqslant H_{k} \leqslant H_{\max } \quad k=1,2, \cdots, M
$$

- Pipe size availability constraints:

$$
d_{\min } \leqslant d_{i} \leqslant d_{\max }, d_{i} \in S_{d} \quad k=1,2 \cdots, M
$$

where $H_{k}$ is the nodal head; $H_{\min }$ and $H_{\max }$ are minimum and maximum allowable nodal heads; $d_{i}$ is the commercially available pipe diameter and $S_{d}$ is the set of these diameters; while $d_{\text {min }}$ and $d_{\text {max }}$ are minimum and maximum values of available pipe diameters, respectively.

When applying a population-based evolutionary algorithm to this optimization problem, each individual represents a network which is encoded as a string of integers, and each element of the string represents the diameter of that pipe link in the network. Normally, pipes with larger diameters are more expensive. Therefore, they are given a larger integer in the algorithm.

Individuals are evaluated at each iteration according to Eqs. (1) to (7). A penalty method is used to formulate this constrained optimization as an unconstrained optimization leading to a new problem defined by minimization of the following penalized objective function:

$$
\begin{gathered}
\text { Minimize } C_{\text {total }}=\sum_{1}^{N} C_{i} L_{i}(1+H D) \\
H D=\sum_{k \in M}\left(H_{k, \min }-H_{k, \text { actual }}\right)
\end{gathered}
$$

where $H_{k, \min }$ and $H_{k, \text { actual }}$ denote the required minimal head pressure and actual head pressure in node $k$ respectively. Equation (9) sums up the head pressure deficit (HD) where the actual head pressure is lower than the required minimal

head pressure. Total cost will be increased by means of the hydraulic head deficit. EPANET 2.0 [25], a free hydraulic simulator, is adopted for the hydraulic calculations. One candidate solution in the population is a set of diameters for all the pipes in the water distribution network. The input for the hydraulic simulator (EPANET2.0) is one candidate solution (diameter set) and output is the actual head pressure of each node in the network. With the output head pressure, the fitness for the input solutions is then calculated using Eqs. (8) and (9). The general flow chart for pipe size optimization is provided in Appendix A.

### 2.2 Particle swarm optimization and diversity measurement

In Particle Swarm Optimization (PSO), the population is regarded as a flock which consists of a number of individuals called particles. Each particle in the flock holds the following information:

- The current position $X_{j}^{i}(t)$
- The current velocity $V_{j}^{i}(t)$
- Personal best position ( $\mathrm{P}_{\text {best }}$ ): the best position that the particle has achieved so far $\hat{X}_{j}^{i}(t)$
- Global best position ( $\mathrm{G}_{\text {best }}$ ): the best position from which all the particles in the swarm have ever traveled $\Omega_{i}^{i}(t)$

At each iteration, each particle updates its position toward its personal best position $\hat{X}_{j}^{i}(t)$ and the current global best position $\Omega_{i}^{i}(t)$. Meanwhile, each dimension is updated according to the following equations:

$$
\begin{aligned}
V_{j}^{i}(t+1)= & w V_{j}^{i}(t)+c_{1} r_{1}\left(\hat{X}_{j}^{i}(t)-X_{j}^{i}(t)\right) \\
& +c_{2} r_{2}\left(\Omega_{i}^{i}(t)-X_{j}^{i}(t)\right) \\
X_{i}^{i}(t+1)= & X_{j}^{i}(t)+V_{j}^{i}(t)
\end{aligned}
$$

where $j$ denotes the dimension index and $i$ is the index of the particle; $w$ is the inertia weight and $t$ is the iteration index number; $r_{1}$ and $r_{2}$ are two random numbers uniformly distributed in the range $[0,1] ; c_{1}$ and $c_{2}$ are the acceleration coefficients. After all the particles are updated, $\hat{X}_{j}^{i}(t)$ and $\Omega_{i}^{i}(t)$ are also updated if better results are found. $c_{1}, c_{2}$ and $w$ are set to the tuned best values.

When described in matrix form, Let $P_{m}^{n}(t)=$ $\left\{X_{m}^{n}(t), \hat{X}_{m}^{n}(t), \Omega_{m}^{n}(t), V_{m}^{n}(t)\right\}$ be a configuration of the particle swarm in the current generation, where $n$ is the population size and $m$ is the dimensionality. $X_{m}^{n}(t)$ represents the whole swarm, $\hat{X}_{m}^{n}(t)$ denotes all the personal best positions, $\Omega_{m}^{n}(t)$ is a matrix in which every row is the current global best particle; and $V_{m}^{n}(t)$ is the velocity matrix of the current generation. Noting that each matrix is an $n \times$ $m$ matrix, the update process of the PSO could be simply described as below:

$$
\begin{aligned}
& X_{m}^{n}(t), \hat{X}_{m}^{n}(t), \Omega_{m}^{n}(t), V_{m}^{n}(t) \rightarrow X_{m}^{n}(t+1), \hat{X}_{m}^{n}(t+1) \\
& \Omega_{m}^{n}(t+1), V_{m}^{n}(t+1)
\end{aligned}
$$

where the left and right sides of the arrow are the configurations of the current and the next generations, respectively. What is noteworthy is the relationship among $X_{m}^{n}(t), \hat{X}_{m}^{n}(t)$, and $\Omega_{m}^{n}(t)$. An individual (a row in the matrix) in $\hat{X}_{m}^{n}(t)$ is updated if the corresponding individual in $X_{m}^{n}(t)$ is better. All the individuals in $\Omega_{m}^{n}(t)$ are updated with the best individual in $\hat{X}_{m}^{n}(t)$ if it is better. Therefore, the average fitness of all the individuals in $\Omega_{m}^{n}(t)$ is better than $\hat{X}_{m}^{n}(t)$, and $X_{m}^{n}(t)$ is better than $X_{m}^{n}(t)$.

Understanding the mechanism of convergence for PSO is helpful for addressing the premature convergence problem. According to Eqs. (10) and (11), in a classical PSO updating process, the position at time step $t$ is decided by the velocity at time step $t$ (Eq. (11)). The velocity update of particles consists of three parts and they are: the inertia; the cognitive acceleration which represents the particle's own experience; and, the social acceleration which represents the social interactions among particles. When most of the particles are approaching their personal best positions and all the personal best positions are close to each other, the velocities will approach 0 , indicating a convergence. Then, the population tends to lose its diversity. If the current global best is not the global optima, premature convergence occurs.

### 2.3 Estimation distribution algorithm

Estimation of distribution algorithms (EDAs) are evolutionary algorithms with only one update operator. During the iteration process, EDAs estimate the probability distribution by selecting a certain percent (tuneable parameter) of the top individuals in the previous generation to construct a probabilistic model. The new population is generated by sampling the estimated probability distribution. The probabilistic model in EDAs continuously updates as it approaches the actual distribution, which leads the new generations to continually approach the global optima. A typical structure of an EDA can be found in Appendix B1.

For the WDN optimization problem, it is assumed that the distributions of good diameters of each pipe follow a Gaussian distribution independently. Therefore, sampling and estimating the distribution of diameters at each dimension are independent. The flow chart for EDA estimation and sampling is provided in Appendix B2.

### 2.4 EDA enhanced PSO

The success of EDA depends largely on the collection of the right sample to construct the probabilistic distribution model. A good sample could more accurately cover the

most promising region of the search space and guide the search toward it. In the literature, the most commonly used sample for EDA is the better half of either personal best position $\left(\bar{X}_{m}^{n}(t)\right)$ or the current swarm $\left(X_{m}^{n}(t)\right)$ [19-24].

By the assumption that all swarms contain some useful information, it is proposed that historically good positions, denoted as $H_{m}^{n}(t)$, could harvest all useful information to find the most promising region. $H_{m}^{n}(t)$ records historically best positions that all particles have ever traveled in the search space rather than the personal best positions of each particle recorded in $\bar{X}_{m}^{n}(t)$. Table 1 illustrates the advantage of $H_{m}^{n}(t)$ over $\bar{X}_{m}^{n}(t)$. Assuming a population size of $5(n=$ 5) and the fitness value of each individual in each different matrix is given as the configuration of the particle swarm at two consecutive generations in Table 1, in generation $t+1$, the personal best position of the second particle is updated from 5 to 6 , and the particle with fitness 5 is discarded from $\bar{X}_{m}^{n}(t+1)$. However, the particle with fitness 5 is actually a very good particle which could be preserved in $H_{m}^{n}(t+1)$. Assuming the top $40 \%$ were selected as the sample, the top of the $\bar{X}_{m}^{n}(t+1)$ would consist of particles with fitness value 6 and 4 while the top of the $H_{m}^{n}(t+1)$ would include particles with fitness value 6 and 5 . In this case, the top individuals in the historically best positions offer a better sample position for EDA. If the particle with fitness 5 did not exist, the top of the group will perform similarly to the top of the personal best. In the following sections, an improved hybrid algorithm of PSO and EDA is proposed using the historical best positions and compared with previous studies.

### 2.5 Population diversity

Maintaining high diversity is crucial for preventing premature convergence in multi-modal optimization. The population diversity can be measured by either genotype or phenotype space. The diversity of phenotype space is indicated by the distribution of fitness values of individuals in the population. The diversity of a swarm $S$ is calculated by the following equation:

$$
S=\sqrt{\frac{1}{n} \sum_{1}^{n}\left(f_{i}-\bar{f}\right)^{2}}
$$

where $n$ is the population size; $f_{i}$ is the fitness value for the $i^{\text {th }}$ individual in the population; and $\bar{f}$ is the average fitness of the population. For a problem with high dimensionality, too many different individuals may have the same fitness value. As a result, the diversity of phenotype space may be misleading. The population diversity of genotype space, on the other hand, is independent of the population size, the dimensionality of the problem, and, the search range of each dimension. The calculation of the genotype diversity of a swarm Sis adopted from Monson and Seppi [17]:

$$
S=\frac{1}{n \times|L|} \cdot \sum_{1}^{|n|} \sqrt{\sum_{1}^{m}\left(p_{i j}-\bar{p}_{j}\right)}
$$

where $S$ is the swarm; $n$ is the population size; $|L|$ is the length of longest diagonal in the search space; $m$ is the dimensionality of the problem; $p_{i j}$ is the $j^{\text {th }}$ value of the $i^{\text {th }}$ particle and $\bar{p}_{j}$ is the average value of the $j^{\text {th }}$ dimension. Genotype diversity is selected in the present study.
2.6 Improved sequential combination of PSO and EDA (ISEDPSO)

The discussion above suggests a potential way to prevent premature convergence by "boosting the personal best position $\left(\bar{X}_{m}^{n}(t)\right)$." When the particles approach their personal best positions, EDA can be used to improve the personal best positions by introducing the experiences gained from previous iterations. While existing literature suggests the top individuals of the personal best positions or the current swarm for constructing the sampling space for EDA, it is hypothesized that the historically best positions could improve the sample space for building the probabilistic model in EDA. This will result in more space for fitness improvement when the search process is close to convergence. To save computational resources, the engagement of the EDA process can be controlled by two tuneable parameters, the start generation $M_{s}$ and the start frequency $M_{f} . M_{s}$ is the index of the generation at which EDA is engaged. $M_{f}$ controls the number of generations to skip before the next EDA calculation. This will eliminate the generally sub-optimal results in the beginning of the optimization process and the redundant information in the generations between two EDA sam-

Table 1 Explanation of historical best positions

| generation $t$ |  |  |  | generation $t+1$ |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $X_{m}^{n}(t)$ | $\bar{X}_{m}^{n}(t)$ | $\Omega_{m}^{n}(t)$ | $H_{m}^{n}(t)$ | $X_{m}^{n}(t+1)$ | $\bar{X}_{m}^{n}(t+1)$ | $\Omega_{m}^{n}(t+1)$ | $H_{m}^{n}(t+1)$ |
| fitness | 2 | 3 | 6 | 6 | 4 | 3 | 6 | 6 |
|  | 5 | 6 | 6 | 3 | 4 | 6 | 6 | 5 |
|  | 1 | 2 | 6 | 2 | 3 | 2 | 6 | 4 |
|  | 3 | 1 | 6 | 2 | 3 | 3 | 6 | 3 |
|  | 4 | 2 | 6 | 1 | 5 | 4 | 6 | 2 |

plings. For WDN optimization that involves complex hydraulic calculations at each iteration, these two parameters are critical to reduce calculation demands. The Pseudo-code of this improved sequential PSO-EDA (ISEDPSO) algorithm can be found in Appendix C.

For the purpose of exploring the benefit of using historical best positions, two other variants of this algorithm, ISEDPSO-1 and ISEDPSO-2 are designed. While ISEDPSO algorithm uses historical best positions to construct the EDA samples, ISEDPSO-1 and ISEDPSO-2 use the better half of the personal best $\left(\mathrm{P}_{\text {best }}\right)$ and the better half of the global best $\left(\mathrm{G}_{\text {best }}\right)$, respectively.

### 2.7 Parallel hybridization of PSO and EDA (PEDPSO)

In previous versions of hybridization of the PSO with EDA that are discussed in the literature review, although they have different specific implementation strategies, it is a common practice that the PSO and EDA update in sequence. They either update the particles using PSO and EDA alternately, or select a PSO and EDA update process for each particle. In the proposed ISEDPSO, the PSO and EDA update processes are implemented alternately for the whole population. In an effort to further improve the calculation efficiency and preserve diversity, a novel parallel hybridization strategy for PSO and EDA is proposed to address the premature convergence problem. In the parallel hybrid algorithm, a standard PSO and a simple EDA process are combined in parallel rather than sequentially as depicted in Fig. 1.

The parallel algorithm starts by ranking and splitting the whole population into two sub- populations: the better half is going to be updated by a typical EDA process, the worst half is updated by a typical PSO process. The rationale behind this strategy is that PSO is strong in improving very bad positions very fast (fast convergence ability), and EDA has to use a set of good positions to construct the correct probabilistic distribution model for estimation. After each iteration, the two new sub-populations (P1 and P2) generated by the PSO and EDA processes will be mixed with the current population. The better half from the new population will be selected as the next generation. This strategy has two advantageous features. First, the new population is surely to contain the historically best positions throughout the search process, because the current population and the newly generated population are mixed and the better half is selected from the mixture to form the next generation. This ensures that the search process always starts from very good positions in which the swarm has ever traveled. The historical best will also help to improve the probabilistic model of EDA. Secondly, in the PSO process, the worst half is updated using the better half of the population as the personal best positions. As a result, the diversity of the population is enhanced and the convergence process is slowed down. This strategy is similar to the "boosting personal best positions" strategy
used in ISEDPSO but is more efficient because it ensures the personal best position for each particle in the PSO process to be better than the particle, which cannot be guaranteed in sequential hybrids. In summary, the parallel hybridization strategy combines the fast convergence advantage of PSO and the better historical sample space of EDA to control the population diversity and prevent premature convergence.

### 2.8 Benchmark examples and experiment setup

All of the above algorithms are tested on the following two benchmark examples.

The Hanoi network presented by Fujiwara and Khang [26], requires the optimal design of 34 pipes, allowing a minimum hydraulic head of 30 m for all its 32 nodes, by means of 6 available diameters. The total solution space is then equal to $6^{34}$. It serves as a prototype of a small size network for the evaluation of optimization algorithms.

The Balerma network was originally proposed by Reca et al. [27]. It has a total of 443 demand nodes supplied by 4 source nodes. There are 454 pipes, arranged in 8 loops. There are 10 available pipe diameters that range from 125 to 600 mm with an absolute roughness coefficient $k=$ 0.0025 mm . Total enumeration of the search space is $10^{454}$. The Darcy-Weisbach equation has been adopted to calculate the head losses, using EPANET2. The minimum required pressure head is 20 m at each node. The Balerma network serves as a large sized WDN prototype for optimization algorithm evaluation. Figures of the two networks can be found in the literature or in Appendix D1 and D2.

The Darcy-Weisbach equation is selected for the Balerma network and the Hazen-Williams equation is used for the Hanoi network when applying the hydraulic calculations.

### 2.9 Experiment setup and parameter settings

In the experiment phase, two algorithms (ISEDPSO and PEDPSO) are implemented to solve the pipe sizing problems for the two benchmarks above.

A few parameters are adjustable for the hybrid algorithms. The absolute value of the boundary when updating velocity of each particle $\left(V_{\max }\right)$ is set to $50 \%$ of the velocity range of each particle. Each algorithm runs 30 times on each of the benchmark networks. The population size is set at 100 and the maximum number of generations is 2500 . The number of generations before the EDA process starts $\left(M_{s}\right)$ and the frequency of implementing EDA in ISEDPSO $\left(M_{I}\right)$ are 100 and 50 , respectively. The inertia weight $w$ is 0.8 . The acceleration coefficients $c_{1}$ and $c_{2}$ are 1.8 and 2 , respectively. These parameters are obtained through preliminary experiments and kept consistent throughout the comparative study below.

![img-0.jpeg](img-0.jpeg)

Fig. 1 Flow chart of parallel hybridization of EDA and PSO(PEDPSO)

## 3 Results and discussion

The best and average fitness value (network cost) achieved from 30 runs of different algorithms are shown in Fig. 2 (a) for the Hanoi network and Fig. 2 (b) for the Balerma network. The detailed pipeline diameters for the optima of Balerma by the parallel hybrid EDA and PSO (PEDPSO) can be found in Appendix E.

For both networks, the simple integer PSO (IPSO) and ISEDPSO-2 give the weakest performance. For the Hanoi network, the best performances of the two algorithms arecomparable to others with differences of $0.28 \mathrm{M} \$$ and $0.33 \mathrm{M} \$$. However, the average performance of the two algorithms is much higher than the other three algorithms. The disadvantages of these two algorithms are even more obvious for the large Balerma network. This comparison indicates that the better half of swarm position is not a good
sample for the studied water network optimization problem.

For both networks, PEDPSO achieves the lowest minimum cost, which indicates that parallel combination of EDA and PSO can further improve the performance of WDN optimization.

The algorithm using historic best (ISEDPSO) shows slightly better results than the one using personal best results as the sample (ISEDPSO-1). For the small Hanoi network, both algorithms achieved the best minimum, yet the average of the ISEDPSO is $6.21 \mathrm{M} \$$ compared to the $6.31 \mathrm{M} \$$ average of the ISEDPSO-1. For the large Balerma network, ISEDPSO achieved an optimum $5 \%$ less than the ISEDPSO-1. The average performance of ISEDPSO is also better than ISEDPSO-1 which suggests the advantage of using historic best instead of personal best to construct the sample space for EDA.

![img-2.jpeg](img-2.jpeg)

Fig. 2 Experimental results of the Hanoi (a) and the Balerma network (b)

### 3.1 Diversity control analysis and comparison

The fitness tracks in the runs which achieve the best solution for each algorithm are recorded in Fig. 3. To show the overall trend of convergence, the fitness values from the 1st generation were included. However, the results for ISEDPSO-1, ISEDPSO and PEDPSO cannot be clearly differentiated. The inserts provide a clear view of the comparison of the three algorithms using the data from
![img-2.jpeg](img-2.jpeg)

Fig. 3 Fitness track of different algorithms (Balerma network)

1500 generations.
The IPSO and ISEDPSO-2 converge fast enough but fail to achieve minimum fitness. The other three algorithms, including the two novel algorithms proposed in this paper, can achieve much better results and the track record of the last 1500 generations can be observed in Fig. 3 inserts. Figure 3 shows that the two proposed algorithms outperform the others while PEDPSO achieved the minimum fitness. Therefore, hybridization with EDA using the better half of historical and personal best positions converges slower than using the better half swarm position. Parallel hybridization performs slightly better than sequential hybridization.

To investigate the relationship between search performance and diversity control ability of PSO, the change of population diversity on the Balerma network is also tracked and recorded in Fig. 4. The population diversity is calculated according to Eq. (13). As shown in Fig. 4, IPSO loses diversity very quickly and converges after only 250 iterations. On the contrary, ISEDPSO-2, which uses the better half of swarm positions for EDA, maintains very high diversity throughout the search process. As a result, it acts as an almost random search, therefore, cannot achieve the best minimum. The other three algorithms successfully control the population diversity smoothly. The diversity of ISEDPSO-1, which uses the better half of personal best positions, decreases quicker and approaches 0 after approximately 2000 iterations. ISEDPSO and PEDPSO, both using the better half of the historically best positions, maintain relatively higher diversity through the search process and approach 0 at around 3000 iterations later. Therefore, in the case studied, using the better half of historically best positions improved diversity control. In addition, parallel hybridization controls the population diversity better than sequential hybridization when both use historical best positions for EDA. When both the convergence and diversity control are considered, the EDA using the better half of historically best positions is superior to other methods. Parallel hybridization is slightly better than sequential hybridization but not as critical as the EDA sampling method.

The above analysis indicates that population diversity control affects the overall performance of PSO in the WDN optimization problem. A smoothly decreasing trajectory of the population diversity throughout the search process could help preventing premature convergence for the PSO. Using historical best positions in the EDA process can effectively help PSO to better control the diversity and achieve better results than using personal best positions or swarm positions. Population diversity control and the capability to search for global optimum can be further enhanced by a parallel combination of EDA and PSO.

### 3.2 Comparison with previous methods

To justify the advantages of the proposed PSO based

![img-3.jpeg](img-3.jpeg)

Fig. 4 Diversity track of different algorithms (Balerma network)
algorithms over existing methods, they are compared with previous studies. All the most recent related studies adopting 10.6668 as the Hazen-Williams roughness coefficient for hydraulic calculations on the Hanoi network and the Darcy-Weisbach roughness coefficient of 0.0025 for the Balerma network are selected. The selected studies also include all the previous attempts of applying PSO to this problem. The comparisons on the Hanoi network and Balerma network are shown in Tables 2 and 3, respectively.

For the Hanoi network, as shown in Table 2, ISEDPSO and PEDPSO can achieve the best reported cost for the network. Although the number of evaluation calls of both proposed algorithms (17,600 and 23,400, respectively) is a little higher than the best of the other models $(16,600)$, the proposed two novel algorithms perform very well in terms of reliability: The successful rates for ISEDPSO and PEDPSO are $93 \%$ and $90 \%$ respectively, only one previous study achieved a better success rate that was over $90 \%$.

Since the Hanoi network is relatively smaller and less complex, most of the recent methods could achieve this result ( 6.0811 MS). Since no one was able to find a better result so far, including the two proposed algorithms, this result is probably the actual global optima for this problem.

For the Balerma network, the advantage of the proposed algorithms is more obvious. Thus far, no commonly recognized best result has ever been identified. Researchers are still trying to achieve a new record cost for this network. Table 3 shows the optimization results of the Balerma network. Both ISEDPSO and PEDPSO are tested 30 times on this large size network and both of them can achieve a very good cost with much less computation effort, compared to work the literature. Specifically, PEDPSO successfully achieved a new record best result, which is $1.9214 \mathrm{M} €$, using only 217,400 fitness evaluations. Although the ISEDPSO algorithm did not achieve the best minimum, the number of evaluations $(201,400)$ it

Table 2 Comparison of the best cost achieved by different algorithms (Hanoi network)

| algorithms | min cost/M\$ | average | success rate | average No. of evaluations |
| :-- | :--: | :--: | :--: | :--: |
| GA $^{3}[28]$ | 6.173 | $\mathrm{n} / \mathrm{a}$ | $\mathrm{n} / \mathrm{a}$ | 26,457 |
| $\mathrm{ACO}^{2}[29]$ | 6.134 | $\mathrm{n} / \mathrm{a}$ | $\mathrm{n} / \mathrm{a}$ | 35,433 |
| $\mathrm{HS}^{3}[30]$ | 6.081 | $\mathrm{n} / \mathrm{a}$ | $1 / 81$ | 27,721 |
| PSHS $^{4}[31]$ | 6.081 | $\mathrm{n} / \mathrm{a}$ | $1 / 81$ | 17,980 |
| $\operatorname{GHEST}^{5}[32]$ | 6.081 | $\mathrm{n} / \mathrm{a}$ | $6 / 10$ | 16,600 |
| PSO $^{6}[8]$ | 6.133 | $\mathrm{n} / \mathrm{a}$ | $3 / 100$ | $\mathrm{n} / \mathrm{a}$ |
| HD-DDS $^{7}[33]$ | 6.081 | $6 / 252$ | $8 / 100$ | 5000,000 |
| NLP-DE $^{8}[34]$ | 6.081 | $\mathrm{n} / \mathrm{a}$ | $98 / 100$ | 48,724 |
| ISEDPSO (Present study) | $\mathbf{6 . 0 8 1}$ | $\mathbf{6 . 1 0 2}$ | $\mathbf{2 8 / 3 0}$ | $\mathbf{1 7 , 6 0 0}$ |
| PEDPSO (Present study) | $\mathbf{6 . 0 8 1}$ | $\mathbf{6 . 1 0 3}$ | $\mathbf{2 7 / 3 0}$ | $\mathbf{2 3 , 4 0 0}$ |

[^0]
[^0]:    Notes: In all algorithms, Hazen-Williams roughness coefficient for hydraulic calculations is $10.6668 ;{ }^{1}$ Genetic algorithm; ${ }^{2}$ Ant colony optimization; ${ }^{3}$ Harmony search; ${ }^{4}$ Particle-swarm harmony search; ${ }^{5}$ Estimation of particle swarm algorithms; ${ }^{6}$ Particle swarm optimization; ${ }^{7}$ Hybrid discrete dynamically dimensioned search; ${ }^{8}$ Nonlinear programming-differential evolution

Table 3 Comparison of the best cost achieved by different algorithms (Balerma network)

| algorithms | min cost <br> $/ \mathrm{M} €$ | average | success rate | average no. of evaluations |
| :-- | :--: | :--: | :--: | :--: |
| GA [28] | $2.302,000$ | $\mathrm{n} / \mathrm{a}$ | $\mathrm{n} / \mathrm{a}$ | $10,000,000$ |
| HS [30] | $2.018,000$ | $\mathrm{n} / \mathrm{a}$ | $1 / 81$ | $10,000,000$ |
| HD-DDS [33] | $1.940,923$ | $2.165,000$ | $\mathrm{n} / \mathrm{a}$ | $30,000,000$ |
| GHEST [32] | $2.002,387$ | $\mathrm{n} / \mathrm{a}$ | $1 / 10$ | 254,400 |
| NLP-DE [34] | $1.923,000$ | $1.927,000$ | $\mathrm{n} / \mathrm{a}$ | $1,427,850$ |
| ISEDPSO(Present study) | $\mathbf{1 . 9 3 3 , 4 0 7}$ | $\mathbf{1 . 9 7 6 , 6 7 2}$ | $\mathbf{1 6 / 3 0}$ | $\mathbf{2 0 1 , 4 0 0}$ |
| PEDPSO(Present study) | $\mathbf{1 . 9 2 1 , 4 2 8}$ | $\mathbf{1 . 9 4 2 , 2 3 1}$ | $\mathbf{1 7 / 3 0}$ | $\mathbf{2 1 7 , 4 0 0}$ |

Notes: In all algorithms, Darcy-Weisbach roughness coefficient for hydraulic calculations is 0.0025
took to achieve a decent optima ( $1.933 \mathrm{M} €$ ) is $8 \%$ less than that of PEDPSO $(217,400)$. This suggests that ISEDPSO inherited the fast convergence of PSO while PEDPSO preserves diversity better due to the fact that the worst half was also utilized in the optimization process. Both of the proposed algorithms outperform all the previous studies in terms of the number of evaluations needed for achieving the minimum cost. The high efficiency on the large Balerma network implies their great potential of solving even larger real-world water distribution networks.

To further reveal the benefit of the proposed methods, the best results of the proposed algorithms are compared with those of literature reported algorithms with the same number of fitness evaluation calls. Only a few previous studies reported the fitness evaluation calls and those are all included in the comparison in Table 4. As expected, due to its capability of fast convergence, ISEDPSO achieved the lowest cost with required evaluation calls $(45,400)$. Given the 45,400 evaluations, PEDPSO achieved a $10 \%$ higher minimum cost. This observation indicates that the proposed algorithms still maintain a certain level of fast convergence ability in the early stage of the search which is the inherent advantage of PSO. One reported algorithm, GHEST, achieved a minimum better than PEDPSO but not as good as ISEDPSO. The fact that both algorithms achieved low minimum within the given evaluations demonstrates their capability of fast convergence while
controlling the population diversity and avoiding the premature convergence problem. The comparison of ISEDPSO and PEDPSO suggests that parallel hybrids can further control diversity losses and find better global optimum. However, when computational resources are limited, ISEDPSO can be a better alternative due to its capability of fast convergence.

## 4 Conclusions

Using historical best to construct the sample space for EDA can help the PSO-EDA hybrid algorithms control diversity losses and prevent premature convergence effectively. The proposed parallel hybrid (PEDPSO) preserves diversity the best in both experiment benchmark water distribution networks and is able to find the best minimum to date. The sequential hybrid (ISEDPSO) achieved the best minimum for the Hanoi network and the second best minimum for the Balerma network, yet it requires the least amount of evaluations. Compared with the literature reported algorithms for the same benchmarks indicates both proposed algorithms can effectively control population diversity and prevent the premature convergence problem of PSO. Analysis of the diversity track record of the different algorithms for the Balerma network indicates that the capability of PEDPSO to maintain

Table 4 Comparison with the same number of evaluations (Balerma network)

| algorithms | min cost $/ \mathrm{M} €$ | No. of evaluations |
| :-- | :--: | :--: |
| GA [28] | 3.738 | 45,400 |
| $\mathrm{SA}^{1}$ [27] | 3.476 | 45,400 |
| $\mathrm{MSATS}^{2}[27]$ | 3.298 | 45,400 |
| $\mathrm{HS}[30]$ | 2.601 | 45,400 |
| $\mathrm{PSHS}[31]$ | 2.633 | 45,400 |
| $\mathrm{MA}^{3}[35]$ | 3.120 | 45,400 |
| GHEST [32] | 2.178 | 45,400 |
| ISEDPSO (Present study) | $\mathbf{2 . 1 0 8 3}$ | $\mathbf{4 5 , 4 0 0}$ |
| PEDPSO (Present study) | $\mathbf{2 . 3 7 8 1}$ | $\mathbf{4 5 , 4 0 0}$ |

Notes: In all algorithms, Darcy-Weisbach roughness coefficient for hydraulic calculations is $0.0025 ;{ }^{1}$ Simulated annealing; ${ }^{2}$ Mixed simulated annealing and Tabu search; ${ }^{3}$ Memetic algorithm

adequate population diversity is the key to finding the optimum.

Acknowledgements This work was supported by the National Science Foundation Award 0836046. The opinions expressed in this paper are solely those of the authors, and do not necessarily reflect the views of the funding agency.

Supplementary material is available in the online version of this article at http://dx.doi.org/ 10.1007/s11783-015-0776-z and is accessible for authorized users.

## References

1. Walski T M. State-of-the-art: pipe network optimization. In: Toeno H C, ed. Computer Applications in Water Resources, ASCE, New York, 1985, 559-568
2. Fujiwara O, Jenchaimahakoon B, Edirishinghe N C P. A modified linear programming gradient method for optimal design of looped water distribution networks. Water Resources Research, 1987, 23 (6): $977-982$
3. Kessler A, Shamir U. Analysis of the linear programming gradient method for optimal design of water supply networks. Water Resources Research, 1989, 25(7): 1469-1480
4. Walters G A, Cembrowicz R G. Optimal design of water distribution networks. In: Cabrera E and Martinez F, eds. Water Supply Systems, State-of-the-Art And Future Trends. Computational Mechanics Inc., 1993, 91-117
5. Simpson A R, Dandy G C, Murphy L J. Genetic algorithms compared to other techniques for pipe optimization. Journal of Water Resources Planning and Management, 1994, 120(4): 423443
6. Vairavamoorthy K, Ali M. Optimal design of water distribution systems using genetic algorithms. Computer-Aided Civil and Infrastructure Engineering, 2000, 15(5): 374-382
7. Kadu M S, Gupta R, Bhave P R. Optimal design of water networks using a modified genetic algorithm with reduction in search space. Journal of Water Resources Planning and Management, 2008, 134 (2): $147-160$
8. Montalvo I, Izquierdo J, Pérez R, Tung M M. Particle swarm optimization applied to the design of water supply systems. Computers \& Mathematics with Applications (Oxford, England), 2008, 56(3): 769-776
9. Qi X. Water Distribution Network Optimization: A Hybrid Approach. Dissertation for the Master Degree. Athens, Georgia: University of Georgia, 2013
10. Eberhart R C, Shi Y. Comparison Between Genetic Algorithms and Particle Swarm Optimization, Evolutionary Programming VII, Lecture Notes in Computer Science: Springer, 1998, 611-616
11. Chen M R, Li X, Zhang X, Lu Y Z. A novel particle swarm optimizer hybridized with extremal optimization. Applied Soft Computing, 2010, 10(2): 367-373
12. Qi X, Rasheed K, Li K, Potter D. A Fast Parameter Setting Strategy for Particle Swarm Optimization and Its Application in Urban Water Distribution Network Optimal Design, The 2013 International

Conference on Genetic and Evolutionary Methods (GEM), 2013
13. Kennedy J, Mendes R. Population structure and particle swarm performance. IEEE Congress on Evolutionary Computation, 2002, $1671-1676$
14. Li X. Niching without niching parameters: particle swarm optimization using a ring topology. IEEE Transactions on Evolutionary Computation, 2010, 14(1): 150-169
15. Kennedy J. Small worlds and mega-minds: effects of neighborhood topology on particle swarm performance. Proceedings of the 1999 Conference on Evolutionary Computation, 1999, 1931-1938
16. Krink T, Vesterstrom J, Riget J. Particle swarm optimization with spatial particle extension. Proceedings of the Congress on Evolutionary Computation, 2002
17. Monson C K, Seppi K D. Adaptive diversity in PSO. In: Proceedings of the 8th Annual Conference on Genetic and Evolutionary Computation (GECCO'06), ACM, New York, NY, USA, 2006, 59-66
18. Angeline P. Evolutionary optimization versus particle swarm optimization: philosophy and performance differences. In: Proceedings of the Conference on Evolutionary Computation 1998, 1998, $601-610$
19. Zhou Y, Jin J. EDA-PSO-A new hybrid intelligent optimization algorithm. In: Proceedings of the Michigan University Graduate Student Symposium, 2006
20. Iqbal M, Montes de Oca M A. An estimation of distribution particle swarm optimization algorithm. In: Proceedings of the 5th International Workshop on Ant Colony Optimization and Swarm Intelligence, 2006
21. Kulkarni R V, Venayagamoorthy G K. An estimation of distribution improved particle swarm optimization algorithm. In: 3rd International Conference on Intelligent Sensors, Sensor Networks and Information, 2007, 539-544
22. El-Abd M, Kamel MS. Particle swarm optimization with varying bounds. In: Proceedings of IEEE congress on Evolutionary Computation. 2007, 4757-4761
23. El-Abd M. Preventing premature convergence in a PSO and EDA hybrid. In: Proceedings IEEE congress on Evolutionary Computation. 2009, 3060-3066
24. Ahn C W, An J, Yoo J C. Estimation of particle swarm distribution algorithms: combining the benefits of PSO and EDAs. Information Sciences, 2012, 192: 109-119
25. EPANET 2.0, 2002. http://www.epa.gov/nrmrl/wswrd/epanet.html
26. Fujiwara O, Khang D B. A two-phase decomposition method for optimal design of looped water distribution networks. Water Resources Research, 1991, 27(5): 985-986
27. Reca J, Martinez J, Gil C, Baños R. Application of several metaheuristic techniques to the optimization of real looped water distribution networks. Water Resources Management, 2008, 22(10): $1367-1379$
28. Reca J, Martinez J. Genetic algorithms for the design of looped irrigation water distribution networks. Water Resources Research, 2006, 42(5): W05416
29. Zecchin A C, Simpson A R, Maier H R, Leonard M, Roberts A J, Berrisford M J. Application of two ant colony optimisation algorithms to water distribution system optimisation. Mathematical and Computer Modelling, 2006, 44(5-6): 451-468

30. Geem Z W. Optimal cost design of water distribution networks using harmony search. Engineering Optimization, 2006, 38(3): 259280
31. Geem Z W. Particle-swarm harmony search for water networks design. Engineering Optimization, 2009, 41(4): 297-311
32. Bolognesi A, Bragalli C, Marchi A, Artina S. Genetic Heritage Evolution by Stochastic Transmission in the optimal design of water distribution networks. Advances in Engineering Software, 2010, 41 (5): $792-801$
33. Tolson B A, Asadzadeh M, Maier H R, Zecchin A C. Hybrid
discrete dynamically dimensioned search (HD-DDS) algorithm for water distribution system design optimization. Water Resources Research, 2009, 45(12): W12416
34. Zheng F F, Simpson A R, Zecchin A C. A combined NLPdifferential evolution algorithm approach for the optimization of looped water distribution systems. Water Resources Research, 2011, 47(8): W08531
35. Baños R, Gil C, Reca J, Montoya G G. A memetic algorithm applied to the design of water distribution networks. Applied Soft Computing, 2010, 10(1): 261-266