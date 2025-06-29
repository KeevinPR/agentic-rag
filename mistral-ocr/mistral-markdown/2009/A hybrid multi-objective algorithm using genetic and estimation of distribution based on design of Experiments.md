# A Hybrid Multi-objective Algorithm Using Genetic and Estimation of Distribution Based on Design of Experiments 

Guangming Dai<br>School of Computer<br>China University of Geoscience<br>Wuhan, China<br>gmdai@cug.edu.cn<br>Jianwen Wang<br>School of Computer<br>China University of Geoscience<br>Wuhan, China<br>wjwconfidence@gmail.com<br>Jiankai Zhu<br>School of Computer<br>China University of Geoscience<br>Wuhan, China<br>jiankai.cs@gmail.com


#### Abstract

In this paper, we design a hybrid multi-objective algorithm using genetic and estimation of distribution based on design of Experiments. At first, we apply orthogonal design and uniform design to generate an initial population so that the population individual solutions scattered evenly in the feasible solutions space. Second, we proposed a new convergence criterion to check whether the distribution of population has the obvious regularity. When the population is convergence, we use the model-based method to reproduce new individual solutions, otherwise genetic operator was employed to generate offspring. The results of systematic experiments show that the hybrid algorithm this paper proposed capable of finding much better convergence near the Pareto-optimal solutions and better spread of solutions than RM-MEDA.


Keywords-Multi-objective optimizing; Estimation of Distribution Algorithm; Orthogonal design; Uniform design; Optimal Design of Constellation

## I. INTRODUCTION

In scientific research and engineering areas, many optimization problems (MOPs) belong to multi-objective optimization problems. As multi-objective evolutionary algorithms (MOEAs) work with a population of candidate solutions, and can produce a set of Pareto optimal solutions to approximate the Pareto set or Pareto front in single run [1]. MOEAs are becoming the most effective approach to solve multi-objective problems.

The basic idea of traditional MOEAs, i.e. NSGA-11 [2], SPEA2[3] is that the new trial solutions were produced by genetic recombination operator and guided to approximate the Pareto set quickly. But traditional MOEAs have its drawbacks. When the algorithm approaches to convergence, if we continue to put blindly crossover and mutation operator on individual solutions, it may reduce the performance of the algorithm.

The method of generation offspring based on probability model in Estimation of Distribution Algorithm (EDA) is new method to reproduce offspring. Unlike traditional MOEAs, EDAs have no crossover and mutation genetic operator. Instead,

[^0]they build a probability distribution model of promising solutions by extracting globally statistical information from the selected solutions and new solutions are sampled from the model.

However, these EDAs[4]-[6] neglected the distribution regularity of Pareto set in the decision space of continuous MOPs. For the sake of overcoming this shortcoming, Qingfu Zhang proposed a Regularity Model-Based Multi-objective Estimation of Distribution Algorithm (RM-MEDA) [1].

On the basis of RM-MEDA, we propose a hybrid multiobjective algorithm using genetic and estimation of distribution based on design of Experiments.

## II. Problem Definition and Theoretical Basis

In this paper, we only take consideration of the continuous multi-objective optimization problem (continuous MOP) as following:

$$
\min _{x \in X} \bar{F}(x)=\left(f_{1}(x), f_{2}(x), \ldots, f_{m}(x)\right)^{T}
$$

where $x=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{T} \subset R^{n}$ is the decision variable vector, and $X \subset R^{n}$ is the decision space. $\bar{F}: X \rightarrow R^{m}$ is composed of $f_{i}(x)(i=1,2, \cdots, m)$, and each objective function $f_{i}$ is real-valued continuous. $R^{m}$ is the objective space.

The distribution of Pareto set (PS) of a continuous MOP shows certain regularity [7].The PS of a continuous biobjective problem is piecewise continuous curve in decision space, while the PS of a continuous three objectives problem is a piecewise continuous surface.

## III. Algorithm

## A. Basic Idea

In this paper, we introduce two methods to generate initial population, orthogonal design and uniform design, so that the individuals make a more representative distribution in the


[^0]:    This work was supported by the National Natural Science Foundation of China under Grant 60873107, 863 plan under Grant 2008AA12A201 and Natural Science Foundation of Hubei Province under Grant 2008CDB348.

feasible solutions space.
On the one hand, we expect new trial solutions can approximate to the Pareto set rapidly. Conventional crossover and mutation operator will meet the requirement. On the other hand, the distribution of population individuals was observed to have the obvious regularity. At this time, model-based method of RM-MEDA was used.

But how can we determine the distribution of population have the regularity? Inspired by MEA/HB [8] and based on principle component analysis (PCA), a convergence criterion was employed to check the population's convergence here.

## B. Algorithm Framework

Step 0: Set $\mathrm{t}=0$. Generate an initial population Pop(0) by orthogonal design or uniform design.
Step 1: If the population is convergence, go to Step 3; otherwise go to Step 2.
Step 2: Perform crossover and mutation on the total population and store them in $Q(t)$.
Step 3:
3.1 Partition $P(t)$ into $C^{k}, k=1, \cdots, K$ by local PCA algorithm [9];
3.2 For each cluster $C^{k}$, build a 1-D linear model or 2-D plane surface
3.3 Sample new solutions from the models and store them in $Q(t)$
Step 4: Select $P(t+1)$ from $P(t) \cup Q(t)$
Step 5: If the stopping condition is met, stop; otherwise go to Step 1.
C. Generate an initial population Pop(0) by design of experiments
We define $x=\left(x_{1}, x_{2}, \cdots, x_{n}\right) \in X$ is decision variable vector, and $x_{i}, x_{i} \in\left[l_{i}, u_{i}\right]$ is the i-th factor, so there are $n$ factors in our experiment.

1) Generate an initial population Pop(0) by orthogonal design.

Orthogonal design has some properties. First, it has no two repeat experiments. Second, any two results have no comparability.

Suppose there are $Q(Q$ is an odd) levels per factors. The algorithm, which generating an initial population by orthogonal design, work as follows [10]:
Step 1: Set the value of $Q$, construct orthogonal array

$$
\left[a_{i, j}\right]_{m \times n} \text { according to reference [10]; }
$$

Step 2: If $n>n$, delete the last $n-n$ columns, and obtained orthogonal array $\left[a_{i, j}\right]_{m \times n}$
Step 3: Quantize the orthogonal array $\left[a_{i, j}\right]_{m \times n}$
2) Generate an initial population Pop(0) by uniform design.

Uniform design is similar to orthogonal design, it also uses a set of uniform table to design experiments. The algorithm, which generating an initial population by uniform design, work as follows [11]:
Step 1: Construct a uniform design table.
1.1 Suppose population size is $N$ (experiment number), calculate the vector $h=\left(h_{1}, h_{2}, \cdots, h_{r}\right)$, which $h_{i}(i=1,2, \cdots, s)$ fulfill that the greatest common divisor of $h_{i}$ and $N$ is one.
1.2 Construct i-th column of uniform table by (4). $u_{i},=j h_{i}[\bmod N]$
where $i=1,2, \cdots, s, j=1,2, \cdots, N$.
After 1.1 and 1.2, we can obtain a uniform design table $U(\times \times s)$
Step 2: Construct a useful table.
The dimension of decision vector is $n$, but there are $s(n<s)$ columns in design table $U$. So we need to choose $n$ columns in $U$. In this paper, we using a random method. Thus we can obtain a matrix $U^{\prime}(N \times n)$.
Step 3 Quantize the matrix $U^{\prime}$ by (5)

$$
\begin{aligned}
& \operatorname{pop}(i, j)=U^{\prime}{ }_{i j} \times\left(u_{j}-l_{j}\right) / N \\
& \text { where } i=1,2, \cdots, N, \quad j=1,2, \cdots, n \\
& u_{j} \text { is upper limit of } x_{i}, l_{j} \text { is lower limit of } x_{i}
\end{aligned}
$$

TABLE I.
RESULTS ON CONVERGENCE METRIC $\gamma^{\prime}$ OF ZDT1, ZDT1.1, ZDT2,ZDT2.1 ZDT3,ZDT4

| Algorithm | ZDT1 |  | ZDT1.1 |  | ZDT2 |  | ZDT2.1 |  | ZDT3 |  | ZDT4 |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | mean | std | mean | std | mean | std | mean | std | mean | std | mean | std |
| RM-MEDA | 0.02039 | 0.0057 | 0.00138 | 0.0001 | 0.08292 | 0.0087 | 0.00980 | 0.0001 | 0.09303 | 0.0346 | 39.0554 | 2,6491 |
| IORM-MEDA | 0.00112 | 0.0001 | 0.00152 | 0.0002 | 0.00095 | 0.0001 | 0.00068 | 0.0004 | 0.00171 | 0.0001 | 0.00171 | 0.0001 |
| IURM-MEDA | 0.00110 | 0.0014 | 0.00139 | 0.0002 | 0.00193 | 0.0005 | 0.00192 | 0.0003 | 0.00188 | 0.0001 | 0.00187 | 0.0001 |

TABLE II. RESULTS ON CONVERGENCE METRIC $\gamma^{\prime}$ OF ZDT6, ZDT6.1, DTLZ1, DTLZ2, DTLZ2.1, DTLZ7

| Algorithm | ZDT6 |  | ZDT6.1 |  | DTLZ1 |  | DTLZ2 |  | DTLZ2.1 |  | DTLZ7 |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | mean | std | mean | std | mean | std | mean | std | mean | std | mean | std |
| RM-MEDA | 1.06350 | 0.1343 | 0.08411 | 0.0005 | 0.08292 | 0.0087 | 0.05433 | 0.0053 | 0.02399 | 0.0073 | 0.01008 | 0.0037 |
| IORM-MEDA | 0.02332 | 0.0110 | 0.09216 | 0.0006 | 0.00237 | 0.0001 | 0.00595 | 0.0004 | 0.04009 | 0.0110 | 0.01963 | 0.0020 |
| IURM-MEDA | 0.02377 | 0.0135 | 0.07382 | 0.0004 | 0.00234 | 0.0001 | 0.00585 | 0.0002 | 0.03250 | 0.0044 | 0.02039 | 0.0030 |

## D. Convergence Criterion

According to the theory of PCA, the distribution of population data points in decision space has the relation on eigenvalue of its covariance.

Suppose the algorithm is running in generation $t$, the decision variable is n-dimension, $\sum^{t}$ is covariance Matrix of current population, $\lambda_{i}^{t}, i=1, \cdots, n$ is the i-th largest eigenvalue of $\sum^{t}$. In this paper, we define a convergence criterion for the population as follows:
![img-0.jpeg](img-0.jpeg)

Where $t \geq 5$.
If $\varphi<\varepsilon$, we judge the current population is convergence, where $\varepsilon$ is a parameter. In this paper, we set $\varepsilon<1 \times 10^{-7}$.

## E. Offspring generation

1) Offspring generation by genetics-based.

In this paper, the crossover and mutation operator was employed on the total population when the population was not convergence. We selected simulated binary crossover and polynomial mutation of NSGA-II.
2) Offspring generation based on the regularity of Pareto set.

The Pareto set of a continuous bi-objective optimization problem is a piecewise continuous curve, while the Pareto set of a continuous with three-objectives is a piecewise continuous surface, so we can partition the data into several
group, we can build a group of linear models to approximate a principle curve or a principle surface. And a 1-D linear model will be built to characterize each cluster if the MOPs is biobjective problem, while a 2-D plane model to characterize each cluster for three-objectives problem. The algorithm is omitted here, please refer [1] for the detail information.

## IV. EXPERIMENTS AND DISCUSSION

## A. Test problems and performance metrics

We choose eight test bi-objective problems(ZDT1, ZDT2, ZDT3, ZDT4, ZDT6, [2],ZDT1.1, ZDT2.1, ZDT6.1[1]) and four three-objective problems(DTLZ1, DTLZ2, DTLZ7 [12],DTLZ2.1[1])to evaluate the performance of our algorithm proposed in this paper.

We use two different metrics to measure the performance of the algorithms: $\gamma$ metric measure the convergence, that is to say, closeness of the non-dominated solutions to the Pareto front; $\Delta$ metric measures the diversity of the solutions obtained by an algorithm.

## B. Experimental results

In this paper, we used two strategies, including orthogonal design and uniform design, to generate initial population. We called the algorithm which using orthogonal design as IORMMEDA. And we called the other one as IURM-MEDA.

We compare the improved algorithms proposed by this paper, including IORM-MEDA and IURM-MEDA, with RMMEDA.

For RM-MEDA, the population size is 250 , the cluster number of (K) is 5 . For IORM-MEDA and IURM-MEDA, crossover probability is 0.9 , the mutation probability is 0.1 . And set $\eta_{r}=20, \eta_{n}=10$, the rest of parameters is same as RM-MEDA. The statistical results are based on 10 runs of the three algorithms. The codes of RM-MEDA can be downloaded from http://cswww.essex.ac.uk/staff/uzhang/.

TABLE III. RESULTS ON DIVERSITY METRIC $\Delta$ OF ZDT1, ZDT1.1, ZDT2,ZDT2.1

| Algorithm | ZDT1 |  | ZDT1.1 |  | ZDT2 |  | ZDT2.1 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | mean | std | mean | std | mean | std | mean | std |
| RM-MEDA | 0.2187 | 0.0912 | 0.1733 | 0.0774 | 0.2514 | 0.1048 | 0.1754 | 0.0781 |
| IORM-MEDA | 0.1623 | 0.0736 | 0.1667 | 0.0751 | 0.1775 | 0.0802 | 0.4209 | 0.3660 |
| IURM-MEDA | 0.1580 | 0.0700 | 0.1786 | 0.0797 | 0.1708 | 0.0765 | 0.1754 | 0.0780 |

TABLE IV. RESULTS ON DIVERSITY METRIC $\Delta$ OF ZDT3, ZDT4, ZDT6, ZDT6.1,

| Algorithm | ZDT3 |  | ZDT4 |  | ZDT6 |  | ZDT6.1 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | mean | std | mean | std | mean | std | mean |
| RM-MEDA | 0.6487 | 0.2638 | 0.9105 | 12.062 | 0.8513 | 0.0772 | 0.0793 |
| IORM-MEDA | 0.4291 | 0.1914 | 0.1784 | 0.0801 | 0.2587 | 0.1196 | 0.0851 |
| IURM-MEDA | 0.4286 | 0.1912 | 0.1738 | 0.0772 | 0.2638 | 0.1208 | 0.0705 |

The convergence metric results are shown in Table I - II. From them ,we can see that: (1) IORM-MEDA shows the best performance on ZDT2, ZDT3, ZDT4 ,ZDT6, and DTLZ7, IURM-MEDA shows the best performance on ZDT1,ZDT6.1, DTLZ1, DTLZ2. RM-MEDA shows the best performance on ZDT1.1, ZDT2.1 and DTLZ2.1. (2)RMMEDA performs very badly on ZDT4, ZDT6 and DTLZ2.1. The reason might be that when the population individual solutions have no obvious regularity, the model used in RMMEDA does not guide the search to objective direction. (3) Although RM-MEDA shows best performance on ZDT1.1, ZDT2.1 and DTLZ2.1, it only slightly outperforms IORMMEDA and IURM-MEDA. However, IORM-MEDA and IURM-MEDA perform significantly better than RM-MEDA on the other test problems.

The diversity metric results are shown in Table III and Table IV. Note that no results have been obtained the four three-objective test problems. We can see that: (1)Except for ZDT1.1, both IORM-MEDA and IURM-MEDA perform
significantly better than RM-MEDA. (2)In most case, IURMMEDA shows the best performance on diversity metric.

Due to space limitations, we only choose some representative test instances, and plot their non-dominated fronts obtained by RM-MEDA, IORM-MEDA and IURMMEDA. Figs 1-3 plot the final non-dominated front obtained in 10 runs of each algorithm on test instances we chosen.

In Fig1-3, the part (a) of them show the non-dominated fronts with the lowest $\gamma$-metric obtained by each algorithm, while part (b) of them plot all the 10 fronts together found by each algorithm.

From Fig1-3, we can see that both IORM-MEDA and IURM-MEDA capable of finding better convergence near the Pareto fronts on test instances consist of ZDT1, ZDT6, DTLZ2 problems.
![img-2.jpeg](img-2.jpeg)

Figure 1. Comparison of RM-MEDA, IORM-MEDA and IURM-MEDA on ZDT1 problem
![img-2.jpeg](img-2.jpeg)

Figure 2. Comparison of RM-MEDA, IORM-MEDA and IURM-MEDA on ZDT6 problem

![img-3.jpeg](img-3.jpeg)

Figure 3. Comparison of RM-MEDA, IORM-MEDA and IURM-MEDA on DTLZ2 problem

## V. CONCLUSIONS

In this paper, we have introduced two strategies consist of orthogonal design and uniform design to generate an initial population, which can make the initial population scatter evenly in the feasible solutions space. Because the no obvious distribution regularity of population can be observed in early stage of RM-MEDA, simulated binary crossover and polynomial mutation were introduced when the population is not convergence. A new convergence criterion based on the PCA theory was used to check whether the population is convergence. And in order to testify the performance of the improved algorithm proposed in this paper, we choose eight bi-objective problems and four three-objective test problems. Experiments results of them have shown that in most case, the improved algorithms proposed by this paper perform better convergence and diversity than RM-MEDA.

Our future work is to introduce a better manifold learning algorithm to capture distribution of the population and build an exacter probabilistic model to generate new trial solutions.

## REFERENCES

[1] Qingfu Zhang, Aimin Zhou, Yaochu Jin. RM-MEDA: A Regularity Model-Based Multiobjective Estimation of Distribution Algorithm. Evolutionary Computation, IEEE Transactions on Volume 12, Issue 1, Feb. 2008 Page(s):41 - 63.
[2] Deb K. ,Agrawal S. , Pratap A. , Meyarivan T. A fast and elitist multiobjective genetic algorithm: NSGAII. Danpur Genetic Algorit hms Laboratory ( KanGAL ) , Indian Institute ofTechnology, Kanpur : Technical Report, 2002, 6(2) . 182 - 197.
[3] Zitzler E. , Laumanns M. , Thiele L. SPEA2 : Improving the strength Pareto evolutionary algorithm. ETH Zent rum, Zurich, Switzerland : TIK2Report 103, 2001,200-210.
[4] D. Thierens and P. A. N. Bosman, "Multi-objective mixture-based iterated density estimation evolutionary algorithms," in Proceedings of the Genetic and Evolutionary Computation Conference. San Francisco, California: Morgan Kaufmann, 2001, pp. 663-670.
[5] Nazan Khan, David E Goldberg, and Martin Pelikan. Multi-objective bayesian optimization algorithm. In Genetic and Evolutionary Computation Conference, page 684, New York, USA, July 2002. Morgan Kaufmann.
[6] Tatsuya Okabe, Yaochu Jin, Bernhard Sendhoff, Markus Olhofer. Voronoi-based Estimation of Distribution Algorithm for Multi-objective Optimization[C].cec2004, 1594-1602.
[7] K. Miettinen. Nonlinear Multiobjective Optimization[M]. Norwell, MA: Kluwer, 1999, vol. 12, Kluwer's International Series in Operations Research\& Management Science.
[8] Aimin Zhou, Y. Jin, Q. Zhang, B. Sendhoff, and E. Tsang. Combining model-based and genetics-based offspring generation for multiobjective optimization using a convergence criterion[J]. in Proc. Congress. Evolutionary Computation. (CEC 2006), Vancouver, BC, Canada, 2006, pp. 3234-3241.
[9] Nandakishore Kambhatla and Todd K. Leen. Dimension reduction by local principal component analysis. Neural Computation, 9(7):14931516, October 1997.
[10] Leung Y W., Wang Y.. An orthogonal genetic algorithm with quantization for global numerical optimization [J]. IEEE Transactions on Evolutionary Computation. 2001, 5(1) : 41-53.
[11] Hong Wei, Wu Chengehen. Design of Experiments and analysisprinciple.opreation.example [M]. 2004, China Forestry Publishing House, Beijing, China.
[12] Kalyaninoy Deb, Lothar Thiele, Marco Laumanns etc. Scalable MultiObjective Optimization Test Problems[J]. Congress on Evolutionary Compuation (CEC' 2002) 12-17 May 2002, 825-830.