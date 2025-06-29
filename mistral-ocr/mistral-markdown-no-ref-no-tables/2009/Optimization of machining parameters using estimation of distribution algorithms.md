# Optimization of Machining Parameters Using Estimation of Distribution Algorithms 

Shu-tong Xie, Yin-biao Guo*, Hai-bin Huang, Jing Lin<br>Department of Mechanical and Electrical Engineering<br>Xiamen University<br>Xiamen 361005, P.R.China<br>E-mail: stxie@126.com


#### Abstract

In computer numerical control (CNC) machining problems, it is important to reduce the production cost. To deal with the nonlinear optimization problem of machining parameters which aims to minimize the unit production cost (UC) in multi-pass turning operations, two estimation of distribution algorithms (EDAs) incorporated with gene repair method are proposed to search the optimal solution for machining parameters. Computer simulation results show that the proposed algorithms are efficient in searching the optimal machining parameters, which significantly reduce the unit production cost.


Keywords- Machining parameters; Optimization; Estimation of distribution algorithm; Turning

## I. INTRODUCTION

In manufacturing world, the primary objective in machining operations is to produce high-quality products with low cost. In order to minimize the machining cost for machining economics problem, the optimization of machining parameters is one of the most important issues since these parameters strongly affect the cost and quality [1]. The machining optimization problem in multipass turnings becomes very complicated when plenty of practical constraints have to be considered [2]. Conventional optimization techniques, such as geometric programming [3] and dynamic programming [4, 5], may be useful for some specific problems. However they are inclined to give local optimal results. Therefore, meta-heuristic algorithms have been introduced in solving machining economics problems because of their power in global searching and robustness as well. Chen and Tsai [6] have employed the combination of simulated annealing (SA) and pattern search (PS) for solving these problems. Genetic algorithm (GA) was used by many researchers [7-9] to optimize the machining parameters in multi-pass turnings. To deal with the same optimization problem in multipass turnings, Ants colony optimization (ACO) [9-11] was also developed. Recently, particle swarm optimization (PSO) [12] was applied to optimize the multi-pass turning operations. We attempted to develop estimation of distribution algorithms (EDAs) [13-16] with gene repair method to tackle the complicated optimization problems.

The rest of this paper is organized as follows. Section 2 introduces a machining model of multipass turning operations. Section 3 proposes two EDAs to search the optimal results of machining parameters. And the handling methods of constraints are described in detailed. Simulation results and discussions are given in section 4. In the last section, we conclude this work.

[^0]
## II. MATHEMATICAL MODEL OF MULTI-PASS TURNING OPERATIONS

In this paper, the multi-pass turning operations include multiple rough cuts and a single finish cut. The mathematical model proposed by Chen and Tsai $[6,9]$ was adopted for optimizing machining parameters. The objective of the optimization was to determine the optimal machining parameters, including cutting speed, feed rate and depth of cut for both rough and finish machining (namely $V_{r}, V_{s}, f_{r}, f_{s}, d_{r}, d_{s}$ ), in order to minimize UC. The UC for multi-pass turning operations can be divided into four basic cost elements.
(1) Cutting cost by actual time in cut $\left(C_{M}\right)$.
(2) Machine idle cost for loading and unloading operations and idling tool motion $\left(C_{I}\right)$.
(3) Tool replacement cost $\left(C_{R}\right)$.
(4) Tool $\operatorname{cost}\left(C_{T}\right)$.

Hence UC can be represented as

$$
\begin{aligned}
& U C=C_{M}+C_{I}+C_{R}+C_{T} \\
& =\left[\frac{\pi D L}{1000 V_{r} f_{r}}\left(\frac{d_{r}-d_{s}}{d_{r}}\right)+\frac{\pi D L}{1000 V_{s} f_{s}}\right] k_{0} \\
& +\left[t_{c}+\left(h_{1} L+h_{2}\right)\left(\frac{d_{r}-d_{s}}{d_{r}}+1\right)\right] k_{0} \\
& +\left[\frac{\pi D L}{1000 V_{r} f_{r}}\left(\frac{d_{r}-d_{s}}{d_{r}}\right)+\frac{\pi D L}{1000 V_{s} f_{s}}\right] \frac{t_{c}}{T_{p}} k_{0} \\
& +\left[\frac{\pi D L}{1000 V_{r} f_{r}}\left(\frac{d_{r}-d_{s}}{d_{r}}\right)+\frac{\pi D L}{1000 V_{s} f_{s}}\right] \frac{k_{r}}{T_{p}}
\end{aligned}
$$

Where
$U C$ : Unit production cost excluding material cost (\$/piece)
$k_{0}$ : Direct labor cost, including overhead (\$/min)
$k_{t}: \quad$ Cutting edge cost (\$/edge)
$D, L:$ Diameter and length of work-piece (mm)


[^0]:    This work is supported by the Important Sci-Tech Special Projects of Fujian Province(No.2006HZ0002-4) and Science Foundation for the Youth of Fujian Province, China (2009J05136), * Corresponding author

$d_{1}: \quad$ Depth of material to be removed (mm)
$h_{1}, h_{2}$ : Constants relating to cutting tool travel and approach/departure time (min)
$t_{e}$ : Preparation time for loading and unloading time (min)
$t_{o}$ : Time required to exchange a tool (min)
$T_{p}$ : Tool life of weighted combination of $T_{s}$ and $T_{s}$ (min)
$V_{e}, V_{s}$ : Cutting speeds in rough and finish machining ( $\mathrm{m} / \mathrm{min}$ )
$f_{e}, f_{s}$ : Feed rates in rough and finish machining ( $\mathrm{mm} / \mathrm{rev}$ )
$d_{r}, d_{s}$ : Depths of cut for each pass of rough and finish machining $(\mathrm{mm})$
$n: \quad$ Number of rough cuts, an integer

$$
n=\frac{d_{r}-d_{s}}{d_{r}}, \text { and } n \in Z_{e}
$$

For the minimization of UC, practical constraints that present the states of machining process are to be considered, which are listed as following. And Detailed constraints equations can be seen in $[6,9]$
(1) Parameter bounds
(2) Tool-life constraint
(3) Operating constraints consisting of surface finish constraint, force and power constraint
(4) Stable cutting region constraint
(5) Chip-tool interface temperature constraint
(6) Roughing and finishing parameter relations

## III. ESTIMATION OF BISTRIBUTION ALGORITHMS

EDA is a class of population-based evolutionary algorithm [13-16]. While evolutionary algorithms, like GA, use a population of configurations to search for a solution to an optimization problem, EDA uses a probability function to represent an individual in the population. This probability function will be replaced in each generation. For this reason, EDA is also often called "probability-model building evolutionary algorithm". According to different probability model used in EDA, EDA can be classified into three classes: without dependencies, bivariate dependencies and multivariate dependencies. In this paper, two kinds of EDA with the probability without dependencies, population based incremental learning (PBIL) and univariate marginal distribution algorithm (UMDA) [13-16], are developed to search the optimal machining parameters set.

The joint probability distribution of random vector $P(x)$ in PBIL is represented by

$$
P_{l+1}(x)=(1-\alpha) P_{l}(x)+\alpha \frac{1}{N} \sum_{k=1}^{N} x_{l}^{k}
$$

Where $l$ stands for the number of generations in the population, $\alpha$ is the learning rate, $N$ is the number of selected best individuals.

On the other hand, the probability vector in UMDA can be calculated by (3) where $\alpha$ equals one, which is only different from the PBIL algorithm.

## A. Probability Vector and the Framework of EDAs

The probability vector $P(x)$ is consists of five variables to be optimized, i.e., cut speed, feed rates of both rough and finish machining, and the depths of cut of finish machining. Each variable is represented by a 20-bit binary string, as shown in Table 1. The depth of cut of rough $d_{r}$ can be obtained by (2) $n=\left(d_{r}-d_{s}\right) / d_{r}$ when $n$ is fixed.

TABLE I. REPRESENTATION OF PROBABILITY VECTOR

The probability vector encoding, named as constraints-encoding method, is different from the chromosome encoding method in GA or PSO algorithms proposed previously [7-12]. The difference is that encoding bounds of the variables $V_{r}, V_{s}, f_{r}, f_{s}, d_{s}$ are adjusted reasonably according to the specific constraints, while the previous algorithms directly use the given bound of these variants.

There are three advantages in using this encoding method, which are described as follows:
(1) It can greatly reduce the number of infeasible individuals in the population;
(2) It eliminates some constraints, such as the surface finish constraint, to avoid the corresponding penalty functions and to reduce the complexity of the problems;
(3) It reduces the running time of the algorithm as the length of variables is reduced because the available bounds of them get small.

The framework of PBIL (UMDA) is shown in Fig. 1, in which MaxGen is the maximum number of iterations of the algorithm. The handling of constraints methods, penalty functions and gene repair, will be described in following sub-sections. To realize the extensive exploration in the first period of evolution, and speedy convergence in the last period of it, the gene repair method is employed after the half of number of iterations.

![img-0.jpeg](img-0.jpeg)

Figure 1. Flow chart of the proposed PBIL (UMDA) algorithm

## B. Handling of Constraints

1) Penalty function

The penalty function is used to penalize the individuals who violate the constraints. The more the constraints are violated, the heavier the penalty will be needed. As a result, the fitness of them will be small, which leads to the probability in the probability vector to generate them being smaller. In this way, the penalty function is expressed as

$$
\begin{aligned}
& \text { Penalty }(X)=\sum_{i=1}^{k} a_{i} \times h_{i} \text {, where } \\
& a_{i}= \begin{cases}0 & \text { Satisfy constraints } \\
1 & \text { Violate constraint }(s)\end{cases}
\end{aligned}
$$

where $k$ is the number of constraints, $h_{i}$ is a penalty constant.

The individual that obtains lower UC gets higher fitness value. Thus the fitness function can be formulized as

$$
\text { fitness }(X)=\left\{\begin{aligned}
-U C(X) & \text { Satisfy constraints } \\
-(U C(X)+\text { Penalty }(X)) & \text { Violate constraint }(s)
\end{aligned}\right.
$$

## 2) Gene repair

During the reproduction of the offspring some invalid individuals which violate some constraints will be generated. In fact, a number of them can be turned into valid individuals
by modifying the wrong gene of them, which is a gene repair method. However it is very difficult to repair all wrong genes in a vector (chromosome) generally. The depths of cut of finish machining $d_{s}$ which is a gene in vector must satisfy the maximum of number of constraints at the same time. So in order to decrease the complexity of gene repair method, we only repair the gene $d_{s}$ by adjust the value of it to satisfy all the relative constraints.

## IV. SIMULATION AND DISCUSSION

In all the simulations, algorithms were run in a computer with a Core Duo T2080 CPU and 1GB memory. Each problem was tested 100 times with different random initial populations. As for PBIL, the population and offspring sizes are both set to 2000 and the algorithm stops after 50 generations. The truncation selection rate and learning rate is set to 0.9 and 0.9 , respectively. As for UMDA, the parameters are the same as those of the PBIL. But it need not set the learning rate. We used the machining experiment example in Chen and Tsai [6, 9].

Fig. 2 compares the results obtained by the proposed algorithms and other previous meta-heuristic algorithms when the total depth of cuts $d_{s}=6$. It can be seen from this figure that the proposed algorithms can achieve much better results than GA [9], PSO [12], SA [6] and FEGA [8]. From Table 11, the average optimal UC obtained by PBIL and UMDA are still smaller than those given by previous algorithms. The number of points searched by our algorithms is not so big. At last, the performance of PBIL is similar to the UMDA. The main reason should be that the probability model used by two algorithms is the same, namely variants without dependencies.
![img-1.jpeg](img-1.jpeg)

Figure 2. Comparison of optimal results between our algorithms and others

## V. CONCLUSION

Two EDA-based algorithms, PBIL and UMDA, were proposed to optimize machining parameters in multi-pass turning operations. By incorporating vector constraints-encoding and gene repair method into EDAs, the number of infeasible individuals in the evolutionary population was greatly reduced. Computer simulations showed that the proposed algorithms were efficient and effective. The optimal results achieved by our algorithms were much better than those obtained by other algorithms proposed previously, and the unit production cost was significantly reduced.
