# Solving dynamic multi-objective problems using polynomial fitting-based prediction algorithm 

Qingyang Zhang ${ }^{\mathrm{a}, *}$, Xiangyu He ${ }^{\mathrm{a}}$, Shengxiang Yang ${ }^{\mathrm{b}}$, Yongquan Dong ${ }^{\mathrm{a}}$, Hui Song ${ }^{\mathrm{a}}$, Shouyong Jiang ${ }^{\mathrm{c}, *}$

${ }^{a}$ School of Computer Science and Technology, Jiangsu Normal University, Xuzhou, CO 221116, China
${ }^{\mathrm{b}}$ School of Computer Science and Informatics, De Montfort University, Leicester LE1 9BH, United Kingdom
${ }^{\mathrm{c}}$ Department of Computer Science, University of Aberdeen, Aberdeen AB24 3UE, United Kingdom

## A R T I C L E I N F O

Article history:
Received 18 February 2022
Received in revised form 5 August 2022
Accepted 6 August 2022
Available online 11 August 2022

## Keywords:

Dynamic multi-objective optimization
Polynomial fitting
Prediction mechanism
Dynamic engineering design

## A B S T R A C T

Recently, dynamic multi-objective optimization has received growing attention due to its popularity in real-world applications. Inspired by polynomial fitting, this paper proposes a polynomial fitting-based prediction algorithm (PFPA) and incorporates it into the modelbased multi-objective estimation of distribution algorithm (RM-MEDA) for solving dynamic multi-objective optimization problems. When an environment change is detected, the main mission of PFPA is to predict high-quality search populations for tracking the moving Pareto-optimal set effectively. Firstly, the non-dominated solutions obtained in past environments are utilized to predict high-quality solutions based on a multi-step movement strategy. Secondly, a polynomial fitting-based strategy is designed to fit the distribution of variables according to the obtained search populations, and capture the relationship between variables in the new search environment. Thirdly, some effective search agents are generated for improving population convergence and diversity based on characteristics of variables. To evaluate the performance of the proposed algorithm, experimental results on a set of benchmark functions, with a variety of different dynamic characteristics and difficulties, and two classical dynamic engineering design problems show that PFPA is competitive with some state-of-the-art algorithms.
(c) 2022 Elsevier Inc. All rights reserved.

## 1. Introduction

Dynamic multi-objective optimization problems(DMOPs) refers to solving multi-objective optimization problems (MOPs) in dynamic or uncertain conditions, and it has a growing number of applications [1]. Without loss of generality, considering the following minimization model of DMOPs.

$$
\begin{aligned}
\min _{x, t 1} F(x, t) & =\left(f_{1}(x, t), f_{2}(x, t), \ldots, f_{m}(x, t)\right)^{T} \\
\text { s.t. } h_{i}(x, t) & =0, \quad i=1,2, \ldots, n_{b} \\
g_{j}(x, t) & \leqslant 0, \quad j=1,2, \ldots, n_{g}
\end{aligned}
$$

[^0]
[^0]:    * Corresponding authors.

    E-mail addresses: sweqyian@126.com (Q. Zhang), shouyong.jiang@abdn.ac.uk (S. Jiang).

where $\Omega=\prod_{i=1}^{n}\left|I_{i}, U_{i}\right| \subset R^{0}$ is the feasible area of the decision space, and $F$ consists of $m$ time-varying objective functions. $x=\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ defines the decision vector involving $D$ variables, $I_{i}$, and $U_{i}$ represent the lower and upper bounds of the $i$ th variable $x_{i}$, respectively, $t$ is the time instant of the problem. $n_{h}$ and $n_{g}$ denote the number of equality and inequality constraints at time $t$, respectively.

Different from static MOPs, DMOPs require to consider two important problems, i.e., multiobjectivity and dynamism. the former involves conflicting objectives, which is a common characteristic of MOPs. The latter involves various changes that can occur in control parameters, Pareto optimal set (POS) or Pareto-optimal front (POF). They bring great challenges to the tracking ability of optimization algorithms during the course of search. It is difficult to obtain optimal tradeoff solutions satisfying the requirements in dynamic environments. One way to address DMOPs is that DMOPs can be regarded as a sequence of static MOPs along the time horizon. This means that solving dynamic multi-objective problems is a process of obtaining a sequence of approximate Pareto-optimal solutions.

Recently, a growing number of effective dynamic multi-objective evolutionary algorithms (DMOEAs) have been proposed based on various learning mechanisms and models. As shown in Algorithm 1 for a basic framework of DMOEAs, it is obvious that the overall course of solving DMOPs consists of two main components: change handling after detecting a change and multi-objective optimization algorithms.

```
Algorithm 1: The basic framework of DMOEAs
    1: Initialize time instance \(t=1\);
    2: Generate an initial population \(\mathrm{Pop}_{1}\);
    3: While the stopping criterion is not met
    4: Change Detection
    5: If change is not detected, optimize population using MOEAs;
    6: Otherwise, evolve population using DMOEAs;
    7: Return 3
```


# 1.1. Change detection 

Change detection is a core part of the framework, since it determines the timing of environmental change and whether there is a need to adopt environmental response mechanisms. Dynamic detection techniques include re-evaluating solutions [2] and checking population statistical information [3] through sensors. The former is more popular, since it is simple and easy to implement, but it also suffers from noise sensitivity. On the contrary, the latter is not sensitive to noise, but it needs some control parameters. Besides, sensors are placed appropriately for change detection [4] and need to be tested on various problems or applications. It is difficult to select an appropriate detection technique, since each method has its advantages and limitations for different DMOPs.

### 1.2. Multi-objective optimization algorithms

Apart from dynamic detection, multi-objective algorithm is also one of the key components for solving DMOPs. The existing research on multi-objective algorithms mainly focuses on three types described as follows. The first category is Pareto dominated-based algorithms, which utilize the dominance concept to determine whether the obtained individuals can be retained for next iteration. Various classical and representative algorithms have been proposed recently years, such as non-dominated sorting genetic algorithm II (NSGA-II) [5], NSGA-III [6] and strength Pareto evolutionary algorithm (SPEA2)[7]. In addition, some swarm intelligence algorithms are also adopted for multi-objective optimization, such as multi-objective grasshopper optimization algorithm (MOGOA) [8], and multi-objective multi-verse optimizer (MOMVO) [9], and so on. Pareto-dominance strategies perform well in different applications, but suffer from the risk of generating excessive boundary individuals in some cases.

The second category is indicator-based algorithms, which are designed according to performance metrics. The hypervolume [10], the epsilon indicator and the R2 have been widely employed to design optimization algorithms, such as indicatorbased EA (IBEA) [11], approximation-guided EMO (AGE) [12]. The last category is decomposition-based algorithms, which are designed by decomposing an MOP into several sub-problems and solving them simultaneously. Typically, MOEA based on decomposition (MOEA/D) [13] and multi-objective particle swarm optimization algorithm based on decomposition (MPSOD) [14]. This kind of algorithm is effective, but depends heavily on weight vectors.

In addition, the research on complicated real-world problems is also important for evaluating the algorithmic effectiveness and guiding the algorithmic design. Some practical applications in various areas are described briefly as follows. Mirjalili et al. [15] assessed the performance of algorithms by solving several popular engineering design problems including four-bar truss design, speed reducer design, disk brake design, welded beam design, cantilever beam design and brushless DC wheel motor. Wang et al. [16] investigated urban bus scheduling problem considering route, number of vehicles and drivers. Besides, there exist many different optimization models, such as change detection in SAR images [17], elevator group control[18] and so on.

# 1.3. Dynamic multi-objective optimization algorithms 

Influenced by the frequency or severity of change, diverse difficulties may appear in different forms, such as intensive computation, changing feasible region, irregular Pareto fronts and constraints. This requires that the optimization algorithm keep a good balance between diversity and convergence during the search of solutions. Research on dynamic multi-objective optimization algorithms can be classified into four categories: diversity-based algorithms, memory based algorithms, multipopulation based algorithms, and prediction based algorithms. Firstly, diversity-based algorithms aim to employ different effective strategy for keeping the diversity of population after change detection. Respectively, Li [19] proposed a basic framework for generating subpopulations with good diversity using hierarchical linkage clustering. Chang [20] proposed a querybased mechanism for producing some individuals for diversity. Ye [21] employs multiple source transfer learning for DMOPs. In addition, immigration-based techniques are also introduced for diversity, such as memory-based immigration [22], elitism-based immigration [23]. Deb [24] proposed two different versions of DMOEAs by combining NSGAII with diversity-increase mechanisms.

In memory-based algorithms, some promising historical individuals are recorded and reused for guiding search when a change is detected. In [25], the best agents of previous obtained population are saved in an archive and used to replace some members of the search population in the current environment. Xie [26] integrates decision variable classification-based cooperative co-evolutionary mechanisms for dynamic multiobjective problems. Azzouz [27] proposed an adaptive hybrid population management strategy by considering memory, local technique and random strategy. In [2], a steady-state mechanism is introduced for generating individuals and responding to dynamic change effectively. The kind of these algorithms performs well in periodically changing problems.

In multi-population based algorithms, the diversity of search population is maintained through multiple subpopulations. Xu et al. [28] proposed two multi-population algorithms based on PSO and NSGAII, each sub-population was endowed with different levels of sensitive variables and responses to dynamic changes using different models. Liu et al. [29] utilized an external archive to store the obtained promising individuals and each sub-population evolved one objective independently. In [30], multiple sub-populations are employed for dealing with different objectives, and an external archive was used to share information between sub-populations and enhance diversity preservation.

The main idea of prediction-based algorithms is to estimate the possible POS/POF position in new dynamic circumstances according to previously obtained individuals. Zhou [31] utilizes the univariate auto-regression (AR) model for predicting the manifold and search population after changes are detected. Muruganantham [32] designed a DMOEA based on Kalman filter for solving DMOPs. Hu [33] proposed multi-directional prediction mechanism for generating high-quality search agents during the process of evolution. Besides, various prediction approaches and models have been designed, such as knee points [34], and center points [35]. This kind of algorithm are much popular in DMOEAs, since they are easy to implement and understand.

In addition to those discussed above, real-world applications have also attracted growing attention in recent years, and the following discusses some practical examples involved in different areas. Deb et al. [24] explored power scheduling in hydrothermal generation systems, which involves two optimization objectives and three constraints about dynamic power demand, hydraulic,fuel cost and power system networks. Zhang, et al. [36] studied the dynamic welded beam design problem and dynamic speed reducer for evaluating the performance of dynamic artificial immune systems. In [37], a dynamic railway junction rescheduling problem with two objectives and dynamic constraints was investigated in railway networks. Kong et al. [38] investigated the dynamic power supply problem with dynamic changes of objectives and constraints. Gong et al. [39] solved dynamic multi-period portfolio selection problem using a similarity-based cooperative co-evolutionary algorithm. In addition, there are still various application problems such as dynamic scheduling [40], path planning [41] and so on.

It can be found from the above analysis that most of the existing dynamic multi-objective optimization algorithms are designed based on various knowledge or machine learning mechanisms and have been applied in various applications. However, a significant property, i.e., the relationship between variables, has not been well explored for generating promising individuals. Meanwhile, the polynomial fitting strategy can not only reflect the relationship between variables, but also be used to predict new variable values [42]. Motivated by this, this paper attempts to design an effective predictionbased algorithm for solving dynamic multiobjective optimization problems.

This paper can be summarized as follows. A new polynomial fitting-based prediction algorithm is proposed for generating high-quality search population when changes are detected. The designed algorithm consists of three different parts, a multistep movement strategy, a polynomial fitting-based strategy and a sampling strategy. Firstly, the multi-step movement strategy mainly utilizes two different step sizes to predict new individuals based on the obtained historical population. Secondly, the polynomial fitting-based strategy aims to predict the potential position of new individuals. Thirdly, the sampling strategy tends to sample some well-distributed individuals based on relationship properties of variables for guiding search and improving the convergence of population during the course of optimization. Experimental results carried on a set of recently proposed functions and two dynamic engineering design problems show that the proposed algorithm is very competitive with other compared algorithms.

The following provides the organization of this paper. Section 2 presents the framework of the proposed algorithm in detail. In Section 3, the effectiveness of the proposed algorithm is evaluated on a suite of bedsxnchmarks and compared with several existing optimization approaches. Section 4 discusses the influence of each component and key parameters in the proposed algorithm. The proposed algorithm is utilized for solving two dynamic engineering design problems in Section 5. The conclusion of this study can be found in Section 6.

# 2. Proposed PFPA 

The details of the proposed algorithm PFPA are presented in this section. Algorithm 2 provides the basic implementation steps of PFPA. When environment changes occur, PFPA introduces a prediction mechanism for generating a high-quality search population composed of three subpopulation resulting from different strategies. RMMEDA is employed for improving the quality of population over the course of optimization.

```
Algorithm 2: The overall framework of the proposed algorithm
    1: Initialize relevant parameters settings.
    2: Initialize and evaluate population \(\left(\operatorname{Pop}_{\text {iter }}\right)\) and set iter \(=1\).
    3: If the stop condition is not satisfied.
    4: If change detected, go to step 5; otherwise, go to step 10.
    5: Generate the first subpopulation \(\left(\operatorname{SubPop}_{1}\right)\) using an multi-step movement strategy.
    6: Generate the second subpopulation \(\left(\operatorname{SubPop}_{2}\right)\) based on a polynomial fitting based strategy.
    7: Generate the third subpopulation \(\left(\operatorname{SubPop}_{3}\right)\) by a sampling strategy [43].
    8: Merge these subpopulations MixPop \(=\operatorname{SubPop}_{1} \cup \operatorname{SubPop}_{2} \cup \operatorname{SubPop}_{3}\).
    9: Obtain a population of Popsize by non-dominated sorting of the merged population.
    10: Optimize population using RM-MEDA.
    11: iter \(=\) iter +1 , return to step 3 .
```


### 2.1. Multi-step movement strategy

The multi-step movement strategy is proposed to predict the position of non-dominated solutions after the change is detected. Non-dominated solutions have good information of the problem under consideration, so it is important to predict their new positions based on historical information. The proposed strategy involves two important parameters, stepsize and direction of movement, described as follows.

Inspired by the fact that the geometric center of the $\operatorname{POF} / \mathrm{POS}$ is a significant feature and can be utilized to represent the changing trend of data to some extent from the statistical point of view. Therefore, the movement direction is computed based on the center points of non-dominated solutions obtained in the last two consecutive generations. Here, suppose that Pop ${ }_{i}^{\text {center }}$ is the centroid of population $\left(\operatorname{Pop}_{i}\right)$ and $\operatorname{Pos}_{i}$ is the non-dominated sets of $\operatorname{Pop}_{i}$ at the time $t$. Then, the Pop ${ }_{i}^{\text {center }}$ can be calculated as follows.

$$
\operatorname{Pop}_{i}^{\text {center }}=\frac{\sum_{x_{t} \in P o p_{i}} x_{t}}{\left|\operatorname{Pop}_{i}\right|}
$$

where $\left|\operatorname{Pop}_{i}\right|$ refers to the population cardinality, $x_{t}=\left(x_{t}^{1}, x_{t}^{2}, \ldots, x_{t}^{n}\right)$ is a solution at time $t$, and the moving direction $\left(\operatorname{Dir}_{t}\right)$ at time $t$ can be obtained by

$$
\operatorname{Dir}_{t}=\operatorname{Pop}_{i}^{\text {center }}-\operatorname{Pop}_{i-1}^{\text {center }}
$$

Then, the possible position of $\operatorname{Pos}_{t+1}$ can be predicted using the formula below:

$$
P o s_{t+1}=P o s_{t}+\operatorname{Dir}_{t} \times \text { step }
$$

where step defines as the moving stepsize along the moving direction of $\operatorname{Dir}_{t}$. Here, two different values of step (i.e., 0.3 and 1.0) are utilized for representing two different moving levels of $\operatorname{Pos}_{i}$.

Fig. 1 gives the description of this movement strategy. We use multi-step strategy rather one-step strategy because different levels of dynamic change may occur to different population individuals. Therefore, generating two positions by our strategy for each individual has a higher chance to cover the true POS than generating only one by one-step strategy.

```
Algorithm 2: Multi-step movement strategy
    1: Retrieve the populations Pop and \(\operatorname{Pop}_{t-1}\) at time \(t\) and \(t-1\), respectively;
    2: Calculate the population centers according to Eq. (2);
    3: Predict the moving direction according to Eq. (3);
    4: Generate two subpopulations \(\operatorname{Pos}_{t+1}^{\text {pr1 }}\) and \(\operatorname{Pos}_{t+1}^{\text {pr2 }}\) using Eq. (4) with different step values;
    5: Save the subpopulations to \(\operatorname{SubPop}_{1}\).
```

![img-0.jpeg](img-0.jpeg)

Fig. 1. Description of Multi-step movement strategy.

# 2.2. Polynomial fitting-based strategy 

This subsection introduces the polynomial fitting-based strategy in detail, which aims at capturing complex relationship between variables according to the distribution of the population individuals, and using it to predict population positions in the new environment. This approach involves two important parts, i.e., curve prediction and generation of new individuals, which are described as follows.

Motivated by its success in machine learning applications, polynomial fitting as a simple linear model can address nonlinearity of data, in addition to its computationally efficiency. This inspires us to use it to explore the relationship between variables and then to generate non-dominated solutions in order to keep track of changes. Here, as shown in Fig. 2, $F c_{t-1}$ and $F c_{t}$ are obtained by polynomial fitting according to the last two consecutive population data at time $t-1$ and $t$, respectively. The moving direction of the curve formed by the population can be calculated using the following formulation.

$$
M V_{t}=F c_{t}-F c_{t-1}
$$

Then, the curve at time $t+1$ can be predicted using the following equation.

$$
F c_{t+1}=F c_{t}+M V_{t}
$$

The solutions of another subpopulation can be generated by

$$
I n d_{t+1}=F c_{t+1}+c r \times N D_{p}
$$

where $c r$ is a scaling parameter, which ensures that the newly generated individuals are not far from the fitted curve and $N D_{p}$ is generated by normal distribution to allow variations for the generated individuals.

Algorithm 4 presents the implementation steps of this strategy. In addition, as suggested in [43], the correlation matrix of variables can be utilized to distinguish these variables. Also, the study [44] suggests that the highest order of the fitting is not more than six. Therefore, the strategy will adaptively select the polynomial orders during the iterative process.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Description of polynomial fitting-based strategy.

Algorithm 4: Implementation details of polynomial fitting based strategy

1: Suppose the populations $\left(\operatorname{Pop}_{t}\right.$ and $\left.\operatorname{Pop}_{t-1}\right)$ at time $t$ and $t-1$, respectively.
2: Define the moving direction of characteristic curve based on Eq. (5).
3: Predict the possible polynomial curve according to Eq. (6).
4: Create the subpopulation $\operatorname{SubPop}_{2}$ sampled from the decision space using Eq. (7).

# 2.3. Sampling strategy 

The recent study [43] proposed a sampling strategy which is effective for handling dynamic changes. We intend to use this strategy to obtain some well-distributed individuals as the third subpopulation for improving the quality of the search population in the new environment. Fig. 3 illustrates the employed sampling strategy in a 2D scenario.

Specifically, suppose that $x_{d}$ is the identified most principal variable in the POS [43], $N_{1}$ is the number of sampled points for $x_{d}$. For any non-principal variable $x_{k}(k \in\{1, \ldots, D\} \backslash\{d\}), N_{2}$ denotes the number of sampling points computed by

$$
h x_{k}^{i}=L_{k}+i \times \frac{U_{k}-L_{k}}{N_{2}}, \quad\left(i=1, \ldots, N_{2}\right)
$$

where $L_{k}$ and $U_{k}$ denote the lower and upper bounds of $x_{k}$, respectively. Then, this strategy will generate a total of $N_{1} N_{2}$ sampling points (marked by black in Fig. 3) $\bar{x}=\left(x_{d}^{i}, h x_{k}^{i}\right), i=1, \cdots, N_{1}$ and $j=1, \cdots, N_{2}$, and these sampled points will be screened using the non-dominated sorting to obtain several promising agents (marked in red in Fig. 3) as the third subpopulation.

It is crucial to determine the values of $N_{1}$ and $N_{2}$ appropriately. Actually, the setting of $N_{1}$ and $N_{2}$ is problem-specific; large values may cause high computational complexity whereas small values may result in inadequate sampling. Therefore, for simplicity, $N_{2}$ is set to the number of variables $\left(N_{2}=D\right)$, and $N_{1}$ is set to a value such that $N_{1} N_{2}=N_{1} D \leqslant N / 2$.

## 3. Experiments

This section is to evaluate the effectiveness of the proposed algorithm through experimental studies. The experimental settings include benchmark problems, performance evaluation indicators, comparison algorithms and related parameter settings, followed by experimental results and analysis.

### 3.1. Test instances

This paper employs DF test problems [45], which consist of various difficulties and characteristics including irregular POF shapes, time-linkage, variable separability for comprehensive assessing the performance of algorithms.

### 3.2. Performance indicators

This paper utilizes different performance metrics described below for measuring the effectiveness of algorithms. Firstly, the widely used mean inverted generational distance (MIGD) is adopted to judge the convergence and diversity of the best
![img-2.jpeg](img-2.jpeg)

Fig. 3. An description of the sampling strategy in 2D case.

population obtained by an algorithm [32]. Secondly, the mean Schott's spacing metric (MSP) is considered to measure the distribution of the computed solutions [39]. Thirdly, the mean hypervolume (MHV) metric is used [38]. Finally, t-test is adopted to check whether the obtained results are statistically different among all the optimization algorithms at 0.05 significant level [46]. For each table of result, $\ddagger, \dagger$ or $t$ indicate that the performance of PFPA is better than, worse than or similar to that of the corresponding algorithm, respectively.

# 3.3. Compared algorithms 

This paper employs four different dynamic multi-objective optimization algorithms for comparison with PFPA, which are described below in detail. Firstly, a first-order difference model-based MOEA/D algorithm (MOEA/D-FD) [47] employs the historically recorded search population for determining movement directions and predicting potential locations of the new POF. Meanwhile, it has a decomposition-based framework that can ensure the distribution of individuals. Secondly, TrDMOEA aims to combine transfer learning mechanism with evolutionary algorithms to handle dynamic environments [48]. Thirdly, as a dynamic version of NSGA-II, DNSGAA aims to replace some existing population individuals using random solutions in the event of dynamic changes [24]. Finally, population prediction strategy (PPS) predicts a population after a change using population centers and manifolds through an autoregression (AR) model [31].

Table 1
Mean and standard deviation values of MIGD obtained by five algorithm for $\left(n_{i}, \tau_{i}\right)=(5,20)$.

| Fun. | $\left(n_{i}, \tau_{i}\right)$ | MOEA/D-FD | TrDMOEA | DNSGAA | PPS | PFPA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| DF1 | (5,20) | 1.179e-2(1.764e-4) | 1.777e-2(2.139e-3) | 6.227e-2(4.221e-3) | 3.668e-1(7.186e-2) | 1.038e-2(4.838e-4) |
|  | p | 1.761e-1 | 3.644e-2 | 3.917e-2 | 2.154e-10 | - |
|  | h | 0 | 1 | 1 | 1 | - |
| DF2 | (5,20) | 1.073e-2(3.404e-4) | 6.565e-3(6.454e-4) | 4.261e-2(4.281e-3) | 2.440e-1(5.131e-2) | 5.434e-2(6.335e-3) |
|  | p | 3.020e-11 | 1.087e-1 | 6.696e-11 | 2.813e-2 | - |
|  | h | 1 | 0 | 1 | 1 | - |
| DF3 | (5,20) | 4.606e-2(4.499e-3) | 5.734e-2(1.981e-2) | 2.581e-1(3.135e-2) | 1.797e-1(1.494e-1) | 4.581e-2(8.669e-3) |
|  | p | 3.020e-11 | 2.370e-10 | 3.012e-11 | 2.922e-9 | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF4 | (5,20) | 1.186e-1(2.085e-3) | 5.872e-1(1.742e-3) | 8.384e-2(2.346e-3) | 1.370e-1(1.003e-2) | 9.570e-2(1.939e-3) |
|  | p | 7.259e-4 | 1.168e-2 | 2.052e-3 | 5.570e-3 | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF5 | (5,20) | 2.027e-2(2.061e-4) | 2.808e-2(3.792e-4) | 7.844e-2(5.077e-3) | 3.723e-1(1.041e-1) | 1.520e-2(7.420e-4) |
|  | p | 1.154e-1 | 2.753e-1 | 8.418e-1 | 2.034e-9 | - |
|  | h | 0 | 0 | 0 | 1 | - |
| DF6 | (5,20) | 4.514e+0(4.384e-1) | 9.798e-1(2.154e-1) | 2.267e+0(2.674e-1) | 6.897e+0(8.883e-1) | 4.654e-1(1.293e-2) |
|  | p | 1.734e-9 | 6.889e-4 | 1.254e-7 | 1.492e-6 | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF7 | (5,20) | 8.858e-2(1.863e-2) | 3.829e-2(1.287e-3) | 3.193e-1(5.110e-2) | 6.720e-2(1.938e-2) | 1.051e-2(3.048e-4) |
|  | p | 3.020e-11 | 4.504e-11 | 4.975e-11 | 1.206e10 | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF8 | (5,20) | 5.631e-2(1.418e-3) | 8.208e-2(4.023e-4) | 4.055e-2(7.530e-4) | 4.636e-2(1.662e-3) | 3.695e-2(3.163e-4) |
|  | p | 1.004e-3 | 9.941e-1 | 6.669e-3 | 1.861e-6 | - |
|  | h | 1 | 0 | 1 | 1 | - |
| DF9 | (5,20) | 9.535e-2(1.959e-2) | 9.792e-2(2.423e-3) | 3.618e-1(3.253e-2) | 5.431e-1(1.111e-1) | 9.288e-2(5.959e-3) |
|  | p | 4.077e-11 | 1.072e-2 | 7.088e-8 | 8.841e-7 | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF10 | (5,20) | 1.877e-1(4.411e-2) | 2.804e-1(6.160e-3) | 1.228e-1(7.753e-3) | 1.931e-1(1.144e-2) | 1.106e-1(5.332e-3) |
|  | p | 4.060e-2 | 3.032e-2 | 3.112e-1 | 2.783e-7 | - |
|  | h | 1 | 1 | 0 | 1 | - |
| DF11 | (5,20) | 6.514e-1(4.128e-4) | 2.846e-1(3.159e-2) | 6.725e-1(1.669e-3) | 6.691e-1(2.447e-3) | 6.589e-1(1.662e-3) |
|  | p | 2.581e-1 | 7.192e-5 | 3.403e-1 | 3.042e-1 | - |
|  | h | 0 | 1 | 0 | 0 | - |
| DF12 | (5,20) | 8.731e-1(3.021e-2) | 3.266e-1(1.545e-2) | 5.107e-1(2.905e-2) | 3.123e-1(1.151e-2) | 2.801e-1(6.598e-3) |
|  | p | 6.010e-8 | 5.606e-5 | 5.072e-10 | 6.567e-2 | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF13 | (5,20) | 2.530e-1(1.364e-2) | 1.659e-1(2.258e-3) | 3.256e-1(2.346e-2) | 4.148e-1(4.258e-2) | 1.577e-1(6.645e-3) |
|  | p | 8.352e-8 | 5.997e-1 | 7.739e-6 | 8.153e-11 | - |
|  | h | 1 | 0 | 1 | 1 | - |
| DF14 | (5,20) | 1.282e-1(2.850e-3) | 7.204e-2(3.136e-4) | 1.572e-1(4.965e-2) | 1.552e-1(1.963e-2) | 5.689e-2(1.817e-3) |
|  | p | 1.729e-7 | 1.585e-4 | 9.063e-8 | 5.072e-10 | - |
|  | h | 1 | 1 | 1 | 1 | - |
|  | $\left(\int / \int\right)$ | 10/1/3 | 9/1/4 | 10/1/3 | 13/0/1 | - |

# 3.4. Parameter settings 

The relevant parameters of all the compared algorithms are same as their original studies, and the population size is set to 100. Each algorithm is executed twenty-five independent runs on each benchmark instance. Besides that, ten percent of the population is used to detect each of the thirty times of change in dynamic optimization.

### 3.5. Experimental results

Test problems used in this paper involves two important control parameters, the severity of change $\left(n_{t}\right)$ and the frequency of change $\left(\tau_{t}\right)$, which take values from $(5,10,20)$ for evaluating the robustness of the proposed algorithm. MIGD values and t-test results are presented in Tables 1-3 (MSP, MHV results can be found in Supplementary Material), in which the best results are also highlighted in bold face.

It is observed from the MIGD and $t$ - test values reported in Tables 1-3 that PFPA clearly outperforms the other compared algorithms on majority of the test problems. In Table 1, the statistical $p$-values illustrate that there are not significant differences among all the algorithms on DF5 and DF11. As the parameters change, the differences become clear for DF10 and DF11. Totally, for different combinations of $n_{t}$ and $\tau_{t}$, PFPA can generate best results on most of the problems, which means that the proposed prediction mechanism is able to obtain high-quality populations for tracking the Pareto-optimal front effectively in dynamic environments.

Table 2
Mean and standard deviation values of MIGD obtained by five algorithm for $\left(n_{t}, \tau_{t}\right)=(10,10)$.

| Fun. | $\left(n_{t}, \tau_{t}\right)$ | MOEA/D-FD | TrDMOEA | DNSGAA | PPS | PFPA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| DF1 | (10,10) | $9.522 \mathrm{e}-3(1.371 \mathrm{e}-4)$ | $8.431 \mathrm{e}-2(9.136 \mathrm{e}-2)$ | $6.020 \mathrm{e}-2(4.333 \mathrm{e}-3)$ | $3.729 \mathrm{e}-1(6.416 \mathrm{e}-2)$ | $5.819 \mathrm{e}-3(2.801 \mathrm{e}-4)$ |
|  | p | $1.492 \mathrm{e}-6$ | $1.094 \mathrm{e}-10$ | $2.439 \mathrm{e}-9$ | $3.338 \mathrm{e}-11$ | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF2 | (10,10) | $1.097 \mathrm{e}-2(2.093 \mathrm{e}-4)$ | $8.149 \mathrm{e}-3(5.478 \mathrm{e}-4)$ | $4.289 \mathrm{e}-2(4.726 \mathrm{e}-3)$ | $2.261 \mathrm{e}-1(4.723 \mathrm{e}-2)$ | $4.932 \mathrm{e}-2(5.571 \mathrm{e}-3)$ |
|  | p | $2.253 \mathrm{e}-4$ | $1.202 \mathrm{e}-8$ | $7.978 \mathrm{e}-2$ | $1.698 \mathrm{e}-8$ | - |
|  | h | 1 | 1 | 0 | 1 | - |
| DF3 | (10,10) | $3.386 \mathrm{e}-2(2.023 \mathrm{e}-3)$ | $3.358 \mathrm{e}-2(1.542 \mathrm{e}-2)$ | $2.896 \mathrm{e}-1(2.940 \mathrm{e}-3)$ | $1.460 \mathrm{e}-1(1.323 \mathrm{e}-1)$ | $8.859 \mathrm{e}-3(2.957 \mathrm{e}-3)$ |
|  | p | $1.311 \mathrm{e}-8$ | $3.255 \mathrm{e}-7$ | $7.398 \mathrm{e}-11$ | $1.777 \mathrm{e}-10$ | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF4 | (10,10) | $1.069 \mathrm{e}-1(1.686 \mathrm{e}-3)$ | $5.644 \mathrm{e}-1(1.407 \mathrm{e}-1)$ | $7.539 \mathrm{e}-2(2.606 \mathrm{e}-3)$ | $1.162 \mathrm{e}-1(1.222 \mathrm{e}-2)$ | $7.146 \mathrm{e}-2(1.925 \mathrm{e}-3)$ |
|  | p | $1.273 \mathrm{e}-2$ | $1.558 \mathrm{e}-7$ | $5.395 \mathrm{e}-1$ | $8.500 \mathrm{e}-2$ | - |
|  | h | 1 | 1 | 1 | 0 | - |
| DF5 | (10,10) | $1.455 \mathrm{e}-2(2.501 \mathrm{e}-4)$ | $2.583 \mathrm{e}-2(4.359 \mathrm{e}-3)$ | $5.705 \mathrm{e}-2(4.674 \mathrm{e}-3)$ | $3.628 \mathrm{e}-1(9.444 \mathrm{e}-2)$ | $6.819 \mathrm{e}-3(1.253 \mathrm{e}-3)$ |
|  | p | $4.311 \mathrm{e}-8$ | $4.195 \mathrm{e}-10$ | $4.563 \mathrm{e}-9$ | $4.504 \mathrm{e}-11$ | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF6 | (10,10) | $5.080 \mathrm{e}+0(5.327 \mathrm{e}-1)$ | $1.209 \mathrm{e}+0(2.704 \mathrm{e}-1)$ | $3.478 \mathrm{e}+0(2.177 \mathrm{e}-1)$ | $7.477 \mathrm{e}+0(7.384 \mathrm{e}-1)$ | $6.484 \mathrm{e}-1(5.727 \mathrm{e}-2)$ |
|  | p | $4.841 \mathrm{e}-2$ | $7.482 \mathrm{e}-2$ | $1.430 \mathrm{e}-5$ | $6.695 \mathrm{e}-11$ | - |
|  | h | 1 | 0 | 1 | 1 | - |
| DF7 | (10,10) | $9.106 \mathrm{e}-2(1.418 \mathrm{e}-2)$ | $3.546 \mathrm{e}-2(9.378 \mathrm{e}-4)$ | $2.583 \mathrm{e}-1(6.761 \mathrm{e}-2)$ | $6.051 \mathrm{e}-2(1.616 \mathrm{e}-2)$ | $9.755 \mathrm{e}-3(2.019 \mathrm{e}-4)$ |
|  | p | $3.020 \mathrm{e}-11$ | $6.066 \mathrm{e}-11$ | $3.020 \mathrm{e}-11$ | $1.329 \mathrm{e}-10$ | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF8 | (10,10) | $3.053 \mathrm{e}-2(2.051 \mathrm{e}-3)$ | $7.954 \mathrm{e}-2(7.347 \mathrm{e}-3)$ | $1.164 \mathrm{e}-2(1.017 \mathrm{e}-3)$ | $1.569 \mathrm{e}-2(1.487 \mathrm{e}-3)$ | $6.980 \mathrm{e}-3(3.363 \mathrm{e}-4)$ |
|  | p | $4.504 \mathrm{e}-11$ | $3.094 \mathrm{e}-6$ | $2.107 \mathrm{e}-1$ | $3.183 \mathrm{e}-3$ | - |
|  | h | 1 | 1 | 0 | 1 | - |
| DF9 | (10,10) | $8.732 \mathrm{e}-2(1.473 \mathrm{e}-2)$ | $7.540 \mathrm{e}-2(1.771 \mathrm{e}-2)$ | $3.489 \mathrm{e}-1(4.264 \mathrm{e}-2)$ | $4.713 \mathrm{e}-1(1.280 \mathrm{e}-1)$ | $6.349 \mathrm{e}-2(4.895 \mathrm{e}-3)$ |
|  | p | $9.000 \mathrm{e}-1$ | $2.708 \mathrm{e}-2$ | $1.957 \mathrm{e}-10$ | $8.153 \mathrm{e}-11$ | - |
|  | h | 0 | 1 | 1 | 1 | - |
| DF10 | (10,10) | $1.652 \mathrm{e}-1(3.667 \mathrm{e}-2)$ | $2.775 \mathrm{e}-1(1.289 \mathrm{e}-2)$ | $1.140 \mathrm{e}-1(8.672 \mathrm{e}-3)$ | $1.816 \mathrm{e}-1(1.075 \mathrm{e}-2)$ | $1.011 \mathrm{e}-1(4.221 \mathrm{e}-3)$ |
|  | p | $8.771 \mathrm{e}-2$ | $2.510 \mathrm{e}-2$ | $2.458 \mathrm{e}-1$ | $6.010 \mathrm{e}-8$ | - |
|  | h | 0 | 1 | 0 | 1 |  |
| DF11 | (10,10) | $6.373 \mathrm{e}-1(3.384 \mathrm{e}-4)$ | $2.877 \mathrm{e}-1(1.657 \mathrm{e}-2)$ | $6.575 \mathrm{e}-1(2.241 \mathrm{e}-3)$ | $6.551 \mathrm{e}-1(2.509 \mathrm{e}-3)$ | $6.417 \mathrm{e}-1(1.518 \mathrm{e}-3)$ |
|  | p | $5.592 \mathrm{e}-1$ | $2.430 \mathrm{e}-5$ | $5.895 \mathrm{e}-1$ | $5.395 \mathrm{e}-1$ | - |
|  | h | 0 | 1 | 0 | 0 |  |
| DF12 | (10,10) | $9.526 \mathrm{e}-1(1.738 \mathrm{e}-2)$ | $3.559 \mathrm{e}-1(4.370 \mathrm{e}-2)$ | $5.047 \mathrm{e}-1(3.102 \mathrm{e}-2)$ | $3.043 \mathrm{e}-1(9.512 \mathrm{e}-3)$ | $2.820 \mathrm{e}-1(4.677 \mathrm{e}-3)$ |
|  | p | $5.573 \mathrm{e}-10$ | $3.965 \mathrm{e}-8$ | $5.573 \mathrm{e}-10$ | $1.087 \mathrm{e}-1$ | - |
|  | h | 1 | 1 | 1 | 0 | - |
| DF13 | (10,10) | $2.239 \mathrm{e}-1(5.951 \mathrm{e}-3)$ | $1.542 \mathrm{e}-1(7.866 \mathrm{e}-3)$ | $3.183 \mathrm{e}-1(2.451 \mathrm{e}-2)$ | $4.057 \mathrm{e}-1(2.940 \mathrm{e}-2)$ | $1.474 \mathrm{e}-1(5.111 \mathrm{e}-3)$ |
|  | p | $2.572 \mathrm{e}-7$ | $3.871 \mathrm{e}-1$ | $3.835 \mathrm{e}-6$ | $8.153 \mathrm{e}-11$ | - |
|  | h | 1 | 0 | 1 | 1 | - |
| DF14 | (10,10) | $1.221 \mathrm{e}-1(4.208 \mathrm{e}-3)$ | $6.943 \mathrm{e}-2(3.387 \mathrm{e}-3)$ | $1.435 \mathrm{e}-1(5.549 \mathrm{e}-2)$ | $1.620 \mathrm{e}-1(2.177 \mathrm{e}-2)$ | $5.314 \mathrm{e}-2(1.898 \mathrm{e}-3)$ |
|  | p | 6.528 e -8 | $3.592 \mathrm{e}-5$ | $1.157 \mathrm{e}-7$ | $4.200 \mathrm{e}-10$ | - |
|  | h | 1 | 1 | 1 | 1 | - |
|  | $1 / 1 / 1$ | $10 / 1 / 3$ | $11 / 2 / 1$ | $10 / 0 / 4$ | $11 / 0 / 3$ | - |

Table 3
Mean and standard deviation values of MIGD obtained by five algorithm for $\left(n_{i}, \tau_{i}\right)=(10,20)$.

| Fun. | $\left(n_{i}, \tau_{i}\right)$ | MOEA/D-FD | TrDMOEA | DNSGAA | PPS | PFPA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| DF1 | (10,20) | $6.546 \mathrm{e}-2(1.322 \mathrm{e}-4)$ | 5.809e-2(1.091e-3) | $7.742 \mathrm{e}-2(8.680 \mathrm{e}-4)$ | $2.479 \mathrm{e}-1(5.558 \mathrm{e}-2)$ | $6.457 \mathrm{e}-2(3.287 \mathrm{e}-4)$ |
|  | p | $2.897 \mathrm{e}-6$ | $5.367 \mathrm{e}-1$ | $4.033 \mathrm{e}-3$ | $4.616 \mathrm{e}-10$ | - |
|  | h | 1 | 0 | 1 | 1 | - |
| DF2 | (10,20) | $9.222 \mathrm{e}-3(1.670 \mathrm{e}-4)$ | 8.197e-3(2.152e-5) | $1.955 \mathrm{e}-2(1.980 \mathrm{e}-3)$ | $1.508 \mathrm{e}-1(4.644 \mathrm{e}-2)$ | $4.218 \mathrm{e}-2(2.664 \mathrm{e}-3)$ |
|  | p | $4.975 \mathrm{e}-11$ | $1.359 \mathrm{e}-7$ | $6.066 \mathrm{e}-11$ | $9.521 \mathrm{e}-4$ | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF3 | (10,20) | $9.217 \mathrm{e}-2(1.145 \mathrm{e}-3)$ | 8.895e-2(1.175e-3) | $4.653 \mathrm{e}-1(4.629 \mathrm{e}-2)$ | $1.662 \mathrm{e}-1(1.457 \mathrm{e}-1)$ | $1.188 \mathrm{e}-1(1.303 \mathrm{e}-1)$ |
|  | p | $3.020 \mathrm{e}-11$ | $3.601 \mathrm{e}-11$ | $3.020 \mathrm{e}-11$ | $9.756 \mathrm{e}-10$ | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF4 | (10,20) | $4.451 \mathrm{e}-1(5.528 \mathrm{e}-3)$ | $5.588 \mathrm{e}-1(1.801 \mathrm{e}-2)$ | 4.115e-1(1.255e-2) | $4.808 \mathrm{e}-1(1.193 \mathrm{e}-2)$ | $4.398 \mathrm{e}-1(4.105 \mathrm{e}-3)$ |
|  | p | $1.850 \mathrm{e}-8$ | $4.625 \mathrm{e}-2$ | $1.596 \mathrm{e}-7$ | $1.248 \mathrm{e}-4$ | - |
|  | h | 1 | 1 | 1 | 1 |  |
| DF5 | (10,20) | $2.580 \mathrm{e}-2(1.771 \mathrm{e}-4)$ | $3.118 \mathrm{e}-2(2.894 \mathrm{e}-4)$ | $3.021 \mathrm{e}-2(5.962 \mathrm{e}-4)$ | $1.044 \mathrm{e}-1(2.204 \mathrm{e}-2)$ | 2.195e-2(4.480e-4) |
|  | p | $3.368 \mathrm{e}-4$ | $4.035 \mathrm{e}-1$ | $2.282 \mathrm{e}-1$ | $6.722 \mathrm{e}-10$ | - |
|  | h | 1 | 0 | 0 | 1 | - |
| DF6 | (10,20) | $3.235 \mathrm{e}+0(1.072 \mathrm{e}+0)$ | $1.953 \mathrm{e}+0(2.570 \mathrm{e}-1)$ | $1.692 \mathrm{e}+0(2.568 \mathrm{e}-1)$ | $4.032 \mathrm{e}+0(6.981 \mathrm{e}-1)$ | 3.864e-1(4.386e-2) |
|  | p | $2.371 \mathrm{e}-10$ | $5.841 \mathrm{e}-6$ | $4.573 \mathrm{e}-9$ | $1.174 \mathrm{e}-9$ | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF7 | (10,20) | $1.241 \mathrm{e}-1(1.096 \mathrm{e}-2)$ | $7.679 \mathrm{e}-2(9.822 \mathrm{e}-3)$ | $1.737 \mathrm{e}-1(3.238 \mathrm{e}-2)$ | $8.795 \mathrm{e}-2(8.222 \mathrm{e}-3)$ | 5.530e-2(3.028e-4) |
|  | p | $3.020 \mathrm{e}-11$ | $3.338 \mathrm{e}-11$ | $3.020 \mathrm{e}-11$ | $1.311 \mathrm{e}-8$ | - |
|  | h | 1 | 1 | 1 | 1 | - |
| DF8 | (10,20) | $1.374 \mathrm{e}-1(3.063 \mathrm{e}-3)$ | 8.472e-2(2.789e-5) | $1.319 \mathrm{e}-1(4.483 \mathrm{e}-3)$ | $1.390 \mathrm{e}-1(3.522 \mathrm{e}-3)$ | $1.303 \mathrm{e}-1(6.972 \mathrm{e}-4)$ |
|  | p | $5.012 \mathrm{e}-2$ | $1.174 \mathrm{e}-4$ | $6.787 \mathrm{e}-2$ | $7.119 \mathrm{e}-9$ | - |
|  | h | 0 | 1 | 0 | 1 |  |
| DF9 | (10,20) | $7.396 \mathrm{e}-2(1.394 \mathrm{e}-3)$ | $6.534 \mathrm{e}-2(1.396 \mathrm{e}-2)$ | $2.251 \mathrm{e}-1(4.792 \mathrm{e}-2)$ | $2.970 \mathrm{e}-1(1.167 \mathrm{e}-1)$ | 6.004e-2(3.336e-3) |
|  | p | $3.690 \mathrm{e}-11$ | $1.297 \mathrm{e}-1$ | $5.186 \mathrm{e}-7$ | $2.921 \mathrm{e}-2$ | - |
|  | h | 1 | 0 | 1 | 1 | - |
| DF10 | (10,20) | $3.147 \mathrm{e}-1(1.227 \mathrm{e}-2)$ | $2.867 \mathrm{e}-1(1.412 \mathrm{e}-2)$ | $2.632 \mathrm{e}-1(5.029 \mathrm{e}-3)$ | 2.491e-1(7.535e-3) | $2.606 \mathrm{e}-1(4.127 \mathrm{e}-3)$ |
|  | p | $1.154 \mathrm{e}-1$ | $9.470 \mathrm{e}-1$ | $5.793 \mathrm{e}-1$ | $9.705 \mathrm{e}-1$ | - |
|  | h | 0 | 0 | 0 | 0 | - |
| DF11 | (10,20) | $7.480 \mathrm{e}-1(3.787 \mathrm{e}-4)$ | 2.507e-1(2.641e-2) | $7.620 \mathrm{e}-1(1.107 \mathrm{e}-3)$ | $7.639 \mathrm{e}-1(1.988 \mathrm{e}-3)$ | $7.560 \mathrm{e}-1(1.422 \mathrm{e}-3)$ |
|  | p | $5.692 \mathrm{e}-1$ | $1.148 \mathrm{e}-7$ | $6.309 \mathrm{e}-1$ | $5.895 \mathrm{e}-1$ | - |
|  | h | 0 | 1 | 0 | 0 | - |
| DF12 | (10,20) | $9.348 \mathrm{e}-1(2.987 \mathrm{e}-2)$ | $3.369 \mathrm{e}-1(1.431 \mathrm{e}-2)$ | $4.763 \mathrm{e}-1(2.504 \mathrm{e}-2)$ | $3.199 \mathrm{e}-1(1.016 \mathrm{e}-2)$ | 3.149e-1(5.715e-3) |
|  | p | $6.121 \mathrm{e}-10$ | $3.339 \mathrm{e}-3$ | $5.462 \mathrm{e}-9$ | $3.183 \mathrm{e}-1$ | - |
|  | h | 1 | 1 | 1 | 0 | - |
| DF13 | (10,20) | $2.782 \mathrm{e}-1(1.351 \mathrm{e}-2)$ | $1.715 \mathrm{e}-1(2.208 \mathrm{e}-3)$ | $1.777 \mathrm{e}-1(6.624 \mathrm{e}-3)$ | $2.996 \mathrm{e}-1(1.908 \mathrm{e}-2)$ | 1.681e-1(4.608e-3) |
|  | p | $1.202 \mathrm{e}-8$ | $5.895 \mathrm{e}-1$ | $7.618 \mathrm{e}-1$ | $2.572 \mathrm{e}-7$ | - |
|  | h | 1 | 0 | 0 | 1 |  |
| DF14 | (10,20) | $1.427 \mathrm{e}-1(4.208 \mathrm{e}-3)$ | $7.995 \mathrm{e}-2(7.074 \mathrm{e}-3)$ | $7.382 \mathrm{e}-2(3.798 \mathrm{e}-3)$ | $1.095 \mathrm{e}-1(9.542 \mathrm{e}-3)$ | 6.729e-2(2.492e-3) |
|  | p | $5.967 \mathrm{e}-9$ | $3.183 \mathrm{e}-3$ | $7.483 \mathrm{e}-2$ | $8.841 \mathrm{e}-7$ | - |
|  | h | 1 | 1 | 0 | 1 | - |
|  | $\\|/\\|)$ | $9 / 2 / 3$ | $6 / 5 / 3$ | $6 / 2 / 6$ | $11 / 0 / 3$ | - |

Tables 1-3 (presented in Supplementary Material) present the MHV and $t$-test values of all the optimization algorithms, and demonstrate that when $n_{i}$ is five, PFPA performs much better than MOEADFD, PPS, NSGAA on the most of the problems, and slightly worse than TrDMOEA on DF5, DF11, DF12 according to the $p$-values. With the change of the parameters, the proposed algorithm still retains significant advantage and is competitive with TrDMOEA. Therefore, in terms of this metric, PFPA has stable and fast responses to dynamic changes.

It can be seen from the MSP and $t$-test values, shown in Tables 4-6 (presented in Supplementary Material), that PFPA has a significant advantage over the other algorithms on some bi-objective problems (e.g., DF1, DF7 and DF8) and performs ineffectively on tri-objective problems. The frequency and severity of change has not obvious impact on all the algorithms. The reason is that most of the algorithms have a good diversity maintenance mechanism (e.g., the decomposition framework for MOEADFD). Pareto-dominance based MOEAs do not seem to be effective for generating uniformly distributed solutions, especially in three-objective cases. However, it is necessary to measure the overall effectiveness of an algorithm from multiple metrics rather than one indicator. Therefore, although PFPA does not achieve good MSP values, it has significant advantages on other metrics.

Some convergence curves of MIGD values are provided in Fig. 4, which shows that the difference is small between PFPA and DNSGAA on DF4, but PFPA outperforms other algorithms in terms of convergence lines. For DF10, the proposed algorithm has a significant advantage in the late stage of environmental change. For other problems, PFPA has competitive performance. Overall, PFPA has more stable convergence and responds faster to changes than other compared algorithms on most of the problems.

Table 4
Performance comparison of different PFPA variants on MIGD

| Fun. | $\left(n_{i}, \tau_{i}\right)$ | PFPAV1 | PFPAV2 | PFPAV3 | PFPA |
| :--: | :--: | :--: | :--: | :--: | :--: |
| DF1 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.414 e-2(4.494 e-4) \\ 1.957 e-10 \\ 1 \end{gathered}$ | $\begin{gathered} 1.431 e-2(1.193 e-3) \\ 1.957 e-10 \\ 1 \end{gathered}$ | $\begin{gathered} 1.713 e-2(2.824 e-3) \\ 2.610 e-10 \\ 1 \end{gathered}$ | 5.819e-3(2.801e-4) |
| DF2 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.074 e-1(6.235 e-3) \\ 2.959 e-5 \end{gathered}$ | $\begin{gathered} 1.092 e-1(5.436 e-3) \\ 7.221 e-6 \end{gathered}$ | $\begin{gathered} 8.080 e-2(1.079 e-2) \\ 7.959 e-3 \end{gathered}$ | 4.932e-2(5.571e-3) |
| DF3 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 3.010 e-2(3.089 e-3) \\ 2.439 e-9 \end{gathered}$ | $\begin{gathered} 8.484 e-2(1.683 e-1) \\ 5.072 e-10 \end{gathered}$ | $\begin{gathered} 1.285 e-2(6.089 e-4) \\ 2.028 e-7 \end{gathered}$ | 8.859e-3(2.957e-3) |
| DF4 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 3.421 e-1(4.022 e-2) \\ 9.063 e-8 \end{gathered}$ | $\begin{gathered} 3.379 e-1(4.501 e-2) \\ 1.067 e-7 \end{gathered}$ | $\begin{gathered} 7.539 e-2(3.266 e-3) \\ 3.555 e-1 \end{gathered}$ | 7.146e-2(1.925e-3) |
| DF5 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.962 e-2(1.145 e-3) \\ 9.756 e-10 \end{gathered}$ | $\begin{gathered} 1.869 e-2(1.608 e-3) \\ 1.734 e-9 \end{gathered}$ | $\begin{gathered} 1.427 e-2(1.311 e-3) \\ 2.195 e-8 \end{gathered}$ | 6.819e-3(1.253e-3) |
| DF6 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | 6.377e-1(3.884e-2) <br> $3.671 e-1$ | $\begin{gathered} 6.714 e-1(5.660 e-2) \\ 3.122 e-1 \end{gathered}$ | $\begin{gathered} 4.336 e+0(2.895 e+0) \\ 1.023 e-1 \end{gathered}$ | 6.484e-1(5.727e-2) |
| DF7 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 2.674 e-2(9.112 e-4) \\ 3.020 e-11 \end{gathered}$ | $\begin{gathered} 2.761 e-2(1.256 e-3) \\ 3.020 e-11 \end{gathered}$ | $\begin{gathered} 2.033 e-2(6.670 e-4) \\ 1.464 e-10 \end{gathered}$ | 9.755e-3(2.019e-4) |
| DF8 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 2.944 e-2(2.595 e-3) \\ 3.020 e-11 \end{gathered}$ | $\begin{gathered} 3.120 e-2(2.704 e-3) \\ 3.020 e-11 \end{gathered}$ | $\begin{gathered} 1.333 e-2(5.485 e-4) \\ 1.411 e-9 \end{gathered}$ | 6.980e-3(3.363e-4) |
| DF9 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.271 e-1(4.815 e-3) \\ 1.892 e-4 \end{gathered}$ | $\begin{gathered} 1.289 e-1(5.378 e-3) \\ 4.639 e-5 \end{gathered}$ | $\begin{gathered} 2.430 e-1(8.753 e-2) \\ 1.167 e-5 \end{gathered}$ | 6.349e-2(4.895e-3) |
| DF10 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.648 e-1(1.005 e-2) \\ 4.077 e-11 \end{gathered}$ | $\begin{gathered} 2.928 e-1(3.636 e-2) \\ 3.020 e-11 \end{gathered}$ | $\begin{gathered} 1.017 e-1(5.247 e-3) \\ 7.845 e-1 \end{gathered}$ | 1.011e-1(4.221e-3) |
| DF11 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 6.704 e-1(1.363 e-3) \\ 4.918 e-1 \end{gathered}$ | $\begin{gathered} 6.947 e-1(7.635 e-3) \\ 4.204 e-1 \end{gathered}$ | $\begin{gathered} 6.462 e-1(1.197 e-3) \\ 8.534 e-1 \end{gathered}$ | 6.417e-1(1.518e-3) |
| DF12 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 3.384 e-1(6.099 e-3) \\ 1.194 e-6 \end{gathered}$ | $\begin{gathered} 3.919 e-1(1.369 e-2) \\ 6.010 e-8 \end{gathered}$ | $\begin{gathered} 2.839 e-1(7.839 e-3) \\ 8.303 e-1 \end{gathered}$ | 2.820e-1(4.677e-3) |
| DF13 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 2.602 e-1(1.897 e-2) \\ 1.777 e-10 \end{gathered}$ | $\begin{gathered} 5.469 e-1(1.226 e-1) \\ 4.077 e-11 \end{gathered}$ | $\begin{gathered} 1.540 e-1(6.515 e-3) \\ 4.305 e-1 \end{gathered}$ | 1.474e-1(5.111e-3) |
| DF14 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 4.368 e-1(1.382 e-2) \\ 3.197 e-9 \end{gathered}$ | $\begin{gathered} 1.342 e-1(7.323 e-3) \\ 5.967 e-9 \end{gathered}$ | $\begin{gathered} 5.106 e-2(1.661 e-3) \\ 2.973 e-1 \end{gathered}$ | 5.314e-2(1.898e-3) |
|  | $\begin{gathered} 1 / 1 / 1 / 1 / 0 / 2 \end{gathered}$ | $\begin{gathered} 1 \\ 11 / 0 / 2 \end{gathered}$ | $\begin{gathered} 1 \\ 11 / 0 / 2 \end{gathered}$ | $\begin{gathered} 0 \\ 7 / 0 / 7 \end{gathered}$ | - |

Fig. 5-8 present some POF approximations. It can be found that the individuals obtained by PFPA are closer to the real POF and are evenly distributed on DF3. For DF5, the PFPA algorithm can obtain individuals with good distribution, but there is a gap between the obtained solutions and the true POF. In later changes, the individuals obtained by PFPA are close to the POF with good distribution, and the convergence is obviously better than the other algorithms. The approximation of PFPA is significantly better than the other algorithms on DF7 and DF8. Thus, PFPA have a good approximation to the changing POF, which means that the designed algorithm has potential tracking ability in changing environments.

# 4. Discussion 

### 4.1. Component analysis

As mentioned before, the proposed dynamic response mechanism contains three different key strategies for generating high-quality population and tracking the changing Pareto front effectively. This subsection focuses on the impact of each strategy on the search performance of the proposed algorithm. Specifically, to illustrate the role of multi-step movement strategy, PAPFV1 is designed by integrating a one-step movement model which is widely employed in most existing prediction approaches for dynamism handling. PFPAV2 and PFPAV3 are designed by removing the polynomial fitting strategy and sampling strategy for showing the effect of the corresponding techniques,respectively. PFPA is also utilized to compare with these three modified versions, Table 4 presents the experimental and comparison results in detail.

Table 5
Performance comparison of PFPA variants on MIGD for $\left(n_{i}, \tau_{i}\right)=(10,10)$.

| Fun. | $\left(n_{i}, \tau_{i}\right)$ | PFPAS1 | PFPAS2 | PFPAS3 | PFPA |
| :--: | :--: | :--: | :--: | :--: | :--: |
| DF1 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.106 e-2(3.976 e-4) \\ 1.698 e-8 \\ 1 \end{gathered}$ | $\begin{gathered} 1.104 e-2(4.503 e-4) \\ 2.390 e-7 \\ 1 \end{gathered}$ | $\begin{gathered} 1.111 e-2(6.105 e-4) \\ 2.390 e-7 \\ 1 \end{gathered}$ | 5.819e-3(2.801e-4) |
| DF2 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 8.010 e-2(7.415 e-3) \\ 2.006 e-4 \end{gathered}$ | $\begin{gathered} 8.261 e-2(7.062 e-3) \\ 3.831 e-5 \end{gathered}$ | $\begin{gathered} 8.285 e-2(4.883 e-3) \\ 5.607 e-5 \end{gathered}$ | 4.932e-2(5.571e-3) |
| DF3 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 3.676 e-2(1.423 e-2) \\ 1.311 e-8 \end{gathered}$ | $\begin{gathered} 5.179 e-2(1.475 e-1) \\ 6.528 e-8 \end{gathered}$ | $\begin{gathered} 8.857 e-2(2.237 e-1) \\ 3.497 e-9 \end{gathered}$ | 8.859e-3(2.957e-3) |
| DF4 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 3.421 e-1(4.022 e-2) \\ 5.298 e-3 \end{gathered}$ | $\begin{gathered} 7.506 e-2(2.561 e-3) \\ 4.464 e-1 \end{gathered}$ | $\begin{gathered} 7.440 e-2(2.222 e-3) \\ 3.790 e-1 \end{gathered}$ | 7.146e-2(1.925e-3) |
| DF5 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.224 e-2(5.607 e-4) \\ 1.102 e-8 \end{gathered}$ | $\begin{gathered} 1.230 e-2(7.611 e-4) \\ 2.015 e-8 \end{gathered}$ | $\begin{gathered} 1.164 e-2(4.619 e-4) \\ 2.390 e-8 \end{gathered}$ | 6.819e-3(1.253e-3) |
| DF6 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 5.341 e-1(5.014 e-2) \\ 4.643 e-1 \end{gathered}$ | $\begin{gathered} 4.911 e-1(4.886 e-2) \\ 6.309 e-1 \end{gathered}$ | $\begin{gathered} 4.951 e-1(3.154 e-2) \\ 6.414 e-1 \end{gathered}$ | $\begin{gathered} 6.484 e-1(5.727 e-2) \\ - \end{gathered}$ |
| DF7 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.767 e-2(4.501 e-4) \\ 3.020 e-11 \end{gathered}$ | $\begin{gathered} 1.829 e-2(1.002 e-3) \\ 3.020 e-11 \end{gathered}$ | $\begin{gathered} 1.938 e-2(3.061 e-3) \\ 3.020 e-11 \end{gathered}$ | 9.755e-3(2.019e-4) |
| DF8 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.230 e-2(4.067 e-4) \\ 8.485 e-9 \end{gathered}$ | $\begin{gathered} 1.232 e-2(3.584 e-4) \\ 7.119 e-9 \end{gathered}$ | $\begin{gathered} 1.258 e-2(4.527 e-4) \\ 7.119 e-9 \end{gathered}$ | 6.980e-3(3.363e-4) |
| DF9 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 7.469 e-2(7.412 e-3) \\ 5.746 e-2 \end{gathered}$ | $\begin{gathered} 6.887 e-2(5.683 e-3) \\ 1.958 e-1 \end{gathered}$ | $\begin{gathered} 7.263 e-2(4.585 e-3) \\ 9.926 e-2 \end{gathered}$ | 6.349e-2(4.895e-3) |
| DF10 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.689 e-1(1.147 e-2) \\ 2.610 e-10 \end{gathered}$ | $\begin{gathered} 1.643 e-1(9.155 e-3) \\ 1.329 e-10 \end{gathered}$ | $\begin{gathered} 1.618 e-1(5.483 e-3) \\ 2.371 e-10 \end{gathered}$ | 1.011e-1(4.221e-3) |
| DF11 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 6.653 e-1(4.538 e-3) \\ 5.011 e-1 \end{gathered}$ | $\begin{gathered} 6.643 e-1(2.673 e-3) \\ 5.201 e-1 \end{gathered}$ | $\begin{gathered} 6.656 e-1(3.896 e-3) \\ 5.201 e-1 \end{gathered}$ | 6.417e-1(1.518e-3) |
| DF12 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 3.329 e-1(6.786 e-3) \\ 6.765 e-5 \end{gathered}$ | $\begin{gathered} 3.203 e-1(8.256 e-3) \\ 3.831 e-5 \end{gathered}$ | $\begin{gathered} 3.210 e-1(7.308 e-3) \\ 2.433 e-5 \end{gathered}$ | 2.820e-1(4.677e-3) |
| DF13 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 2.932 e-1(1.864 e-2) \\ 2.154 e-10 \end{gathered}$ | $\begin{gathered} 2.581 e-1(1.670 e-2) \\ 8.101 e-10 \end{gathered}$ | $\begin{gathered} 2.475 e-1(1.613 e-2) \\ 4.573 e-9 \end{gathered}$ | 1.474e-1(5.111e-3) |
| DF14 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 4.323 e-1(1.675 e-2) \\ 2.195 e-8 \end{gathered}$ | $\begin{gathered} 8.260 e-2(4.528 e-3) \\ 2.317 e-6 \end{gathered}$ | $\begin{gathered} 8.180 e-2(4.225 e-3) \\ 7.739 e-6 \end{gathered}$ | 5.314e-2(1.898e-3) |
|  | $1 / 1 / 1 / 1$ | $12 / 0 / 2$ | $10 / 0 / 4$ | $10 / 0 / 4$ | - |

# 4.1.1. Multi-step movement strategy 

It is observed from Table 4 that, although there exists some similar results indicated by the p-values, PFPA performs much better than the other three variants on the majority of the test problems. This shows that the multi-step strategy is able to generate more better individuals close to the real POS and improves the diversity of the population and the search efficiency of the algorithm. Therefore, it can be seen that this strategy is an important part of the proposed algorithm. It is worth noting that this strategy is likely to generate boundary solutions, which may not benefit for global search. This strategy should be improved in future work.

### 4.1.2. Polynomial fitting-based Strategy

Table 4 clearly demonstrates that there are not differences between PFPA and PFPAV2 on DF6 and DF11, but PFPA is much superior to PFPAV2 on eleven benchmark problems, which means that this strategy is indeed able to improve the search performance of PFPA. This could be explained by the fact that this strategy fully considers the distribution relationship between variables, which is helpful to generate promising solutions to some extent.

### 4.1.3. Sampling strategy

This strategy aims to make full use of the relationship between variables to generate high-quality individuals to guide the search, thus speeding up the search efficiency of the algorithm. The experimental results also show that this strategy can improve the search performance of the algorithm to some extent in varying environments.

Table 6
Performance comparison of PFPA variants on MIGD for $\left(n_{i}, \tau_{i}\right)=(10,10)$.

| Fun. | $\left(n_{i}, \tau_{i}\right)$ | PFPAR1 | PFPAR2 | PFPAR3 | PFPA |
| :--: | :--: | :--: | :--: | :--: | :--: |
| DF1 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.202 e-2(6.330 e-4) \\ 6.518 e-9 \\ 1 \end{gathered}$ | $\begin{gathered} 1.248 e-2(5.582 e-4) \\ 4.998 e-9 \\ 1 \end{gathered}$ | $\begin{gathered} 1.326 e-2(8.466 e-4) \\ 1.411 e-9 \\ 1 \end{gathered}$ | 5.819e-3(2.801e-4) |
| DF2 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 6.887 e-2(4.200 e-3) \\ 2.531 e-4 \end{gathered}$ | $\begin{gathered} 7.040 e-2(8.178 e-3) \\ 2.839 e-4 \end{gathered}$ | $\begin{gathered} 6.654 e-2(8.329 e-3) \\ 5.264 e-4 \end{gathered}$ | 4.932e-2(5.571e-3) |
| DF3 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.531 e-2(3.077 e-3) \\ 1.606 e-6 \end{gathered}$ | $\begin{gathered} 2.130 e-2(1.080 e-2) \\ 6.526 e-7 \end{gathered}$ | $\begin{gathered} 3.235 e-2(4.975 e-2) \\ 3.646 e-8 \end{gathered}$ | 8.859e-3(2.957e-3) |
| DF4 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 7.605 e-2(3.138 e-3) \\ 3.871 e-1 \end{gathered}$ | $\begin{gathered} 7.732 e-2(3.412 e-3) \\ 3.255 e-1 \end{gathered}$ | $\begin{gathered} 7.663 e-2(2.257 e-3) \\ 3.790 e-1 \end{gathered}$ | 7.146e-2(1.925e-3) |
| DF5 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.416 e-2(4.750 e-4) \\ 8.485 e-9 \\ 1 \end{gathered}$ | $\begin{gathered} 1.610 e-2(8.475 e-4) \\ 6.518 e-9 \\ 1 \end{gathered}$ | $\begin{gathered} 1.755 e-2(1.320 e-3) \\ 2.439 e-9 \\ 1 \end{gathered}$ | 6.819e-3(1.253e-3) |
| DF6 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | 6.180e-1(4.740e-2) <br> 8.500e-2 | $\begin{gathered} 6.473 e-1(4.496 e-2) \\ 5.188 e-2 \end{gathered}$ | $\begin{gathered} 6.606 e-1(4.750 e-2) \\ 4.841 e-2 \end{gathered}$ | 6.484e-1(5.727e-2) |
| DF7 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.787 e-2(6.005 e-4) \\ 3.020 e-11 \end{gathered}$ | $\begin{gathered} 1.798 e-2(7.292 e-4) \\ 3.020 e-11 \end{gathered}$ | $\begin{gathered} 1.844 e-2(6.913 e-4) \\ 3.020 e-11 \end{gathered}$ | 9.755e-3(2.019e-4) |
| DF8 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.399 e-2(4.383 e-3) \\ 1.174 e-9 \end{gathered}$ | $\begin{gathered} 1.558 e-2(9.046 e-4) \\ 4.200 e-10 \end{gathered}$ | $\begin{gathered} 1.787 e-2(1.247 e-3) \\ 1.094 e-10 \end{gathered}$ | 6.980e-3(3.363e-4) |
| DF9 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 7.893 e-2(5.033 e-3) \\ 1.837 e-2 \end{gathered}$ | $\begin{gathered} 8.880 e-2(4.479 e-3) \\ 2.380 e-3 \end{gathered}$ | $\begin{gathered} 9.118 e-2(8.936 e-3) \\ 6.912 e-4 \end{gathered}$ | 6.349e-2(4.895e-3) |
| DF10 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.304 e-1(6.197 e-3) \\ 1.596 e-7 \end{gathered}$ | $\begin{gathered} 1.282 e-1(6.893 e-3) \\ 2.377 e-7 \end{gathered}$ | $\begin{gathered} 1.344 e-1(7.392 e-3) \\ 3.081 e-8 \end{gathered}$ | 1.011e-1(4.221e-3) |
| DF11 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 6.497 e-1(1.566 e-3) \\ 6.627 e-1 \end{gathered}$ | $\begin{gathered} 6.486 e-1(2.148 e-3) \\ 7.062 e-1 \end{gathered}$ | $\begin{gathered} 6.494 e-1(1.646 e-3) \\ 6.414 e-1 \end{gathered}$ | 6.417e-1(1.518e-3) |
| DF12 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 3.113 e-1(7.675 e-3) \\ 6.912 e-4 \end{gathered}$ | $\begin{gathered} 3.075 e-1(4.426 e-3) \\ 1.518 e-3 \end{gathered}$ | $\begin{gathered} 3.020 e-1(6.396 e-3) \\ 6.972 e-3 \end{gathered}$ | 2.820e-1(4.677e-3) |
| DF13 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.904 e-1(5.077 e-3) \\ 2.678 e-6 \end{gathered}$ | $\begin{gathered} 1.900 e-1(1.015 e-1) \\ 4.421 e-6 \end{gathered}$ | $\begin{gathered} 1.885 e-1(6.361 e-3) \\ 2.491 e-6 \end{gathered}$ | 1.474e-1(5.111e-3) |
| DF14 | $\begin{gathered} (10,10) \\ p \\ h \\ 1 / 1 / 1 \end{gathered}$ | $\begin{gathered} 6.050 e-2(1.628 e-3) \\ 1.383 e-2 \end{gathered}$ | $\begin{gathered} 6.061 e-2(1.759 e-3) \\ 9.883 e-3 \end{gathered}$ | $\begin{gathered} 6.183 e-2(1.552 e-3) \\ 3.501 e-3 \end{gathered}$ | 5.314e-2(1.898e-3) |
|  | $1 / 1 / 1 /$ | $11 / 0 / 3$ | $12 / 0 / 2$ | $12 / 0 / 2$ | - |

# 4.2. Parameter analysis 

In addition to the above discussion, parameter analysis is also necessary. The proposed algorithm mainly includes two key control parameters, i.e., the step size (step) involved in the multi-step movement strategy and the compression ratio (cr) involved in the polynomial fitting strategy. The relevant comparison results are shown in Table 5 in detail.

### 4.2.1. Influence of step values

As described before, the multi-step movement strategy utilizes two different stepsizes for generating promising solutions. Here, to explore the influence of the step values, step $=1$ is fixed as it has proven effective in many prediction algorithms, and other step values are taken from the range $[0.1,0.7]$ (PFPAS1-PFPAS3), with an increment of 0.2 . It can be observed from Table 5 that, although the differences among them are not significant on some cases, PFPA performs better than the other modifications, according to the $p$-value results. Therefore, 1 and 0.3 are utilized as the movement stepsizes in PFPA.

### 4.2.2. Influence of cr values

Eq. (7) has a important parameter, i.e., compression ratio (cr), for generating possible better solutions for new environments. Here, $c r$ is varied from 0.1 to 1 (PFPAR1-PFPAR3) with an increment of 0.3 , and the results are summarized in Table 6, which illustrate that the proposed algorithm outperforms the other three versions on almost all the problems significantly. Therefore, this paper uses 0.1 as the best $c r$ value for the polynomial fitting strategy.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Mean IGD curves for different problems with $n_{1}=10$ and $\tau_{1}=10$.

# 4.3. Different multi-objective algorithms 

The main purpose of this subsection is to verify the feasibility of the proposed strategies by integrating them into three different and recently proposed multiobjective algorithms. The experimental results can be found in Table 7 and Tables 7,8 (provided in Supplementary Material). It is obvious that these algorithms are able to obtain effective results, but are not as effective as PFPA. Therefore, the proposed algorithm is suitable to be used with different algorithms to solve dynamic multiobjective optimization problems.

## 5. Experimental results on applications

To further evaluate the effectiveness of the proposed PFPA in practice, two widely used dynamic multi-objective engineering designed problems are adopted [36]. Note that the stopping condition, the number of runs and the other relevant settings remain the same as described in the previous sections, and a constraint handling technique [49] is also utilized to deal with the constraints that the problems have. In addition, different from the benchmark problems, the true POS/ POF cannot be known in advance in real applications, so MIGD and MSP cannot be used as the performance indicators. However, the MHV can be still used, and the relevant experimental results are summarized in Tables 8,9.

![img-4.jpeg](img-4.jpeg)

Fig. 5. POF approximations of five algorithms for D F3 with $n_{t}=10$ and $\tau_{t}=10$.
![img-5.jpeg](img-5.jpeg)

Fig. 6. POF approximations of five algorithms for DFS with $n_{t}=10$ and $\tau_{t}=10$.

# 5.1. Case 1 

The welded beam design problem was modified and proposed by integrating some time instances and dynamic factors into it to form the dynamic welded beam design problem, which consists of two important objectives: minimum total fabricating cost and minimum bar end deflection. As can be seen in the following mathematical model, there are four decision variables $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$ and four constraints.

$$
\begin{aligned}
& \operatorname{Min} f_{1}(x, t)=1.10471 x_{1}^{2} x_{2}+0.04811 x_{3} x_{4}\left(14+x_{2}\right) \\
& \operatorname{Min} f_{2}(x, t)=\frac{4 P_{1}\left(14^{2}\right.}{E e_{2}^{2} x_{4}} \\
& \text { s.t. } g_{1}(x)=\tau-13,600 \leqslant 0 \\
& g_{2}(x)=\frac{6 P_{1} t_{1} \lambda}{x_{4} e_{2}^{2}}-30,000 \leqslant 0 \\
& g_{3}(x)=x_{1}-x_{4} \leqslant 0 \\
& g_{4}(x)=P(t)-p c \leqslant 0
\end{aligned}
$$

![img-6.jpeg](img-6.jpeg)

Fig. 7. POF approximations of five algorithms for DF7 with $n_{t}=10$ and $\tau_{t}=10$.
$p c=\frac{4013 E \sqrt{\left(\frac{1}{36}\right)}}{14^{3}}\left(1-\left(\frac{25}{38} \sqrt{\left(\frac{1}{40}\right)}\right)\right), R=\sqrt{\left(\frac{27}{4}+\left(5 \sqrt{2} \sqrt{2}\right)^{2}\right), J}=2 \sqrt{(2)} x_{1} x_{2}\left(\frac{27}{13}+\left(5 \sqrt{2} \sqrt{2}\right)^{2}\right), \quad M=P(t)(14+x_{2} / 2), \tau_{2}=\frac{500}{3}, \tau_{1}=\frac{P(t)}{\sqrt{2\left(x_{1} x_{2}\right.}}$, $\tau=\sqrt{\left(\tau_{1}^{2}+2 \tau_{1} \tau_{2} \frac{x_{1}}{28}+\tau_{2}^{2}\right), E=3 \times 10^{7}, G=1.2 \times 10^{7}}, \quad(t, P(t))=(1,10000),(2,8000),(3,6000),(4,3000),(55 \leqslant x_{1} \leqslant 80,75 \leqslant$ $\left.x_{2} \leqslant 110,1000 \leqslant x_{3} \leqslant 3000,2 \leqslant x_{4} \leqslant 20\right.$

According to the experimental results listed in Table 8, although the standard deviation value of PFPA is worse than that of PPS and TrDMOEA, it outperforms the rest of the algorithms. There is not significant difference between the algorithms except MOEADFD. Such results indicate that the proposed algorithm is an attractive alternative optimizer for generating satisfactory results on challenging optimization problems.

# 5.2. Case 2 

As one of the most popular problems in the field of mechanical engineering, the dynamic speed reducer design problem aims to optimize the weight $\left(f_{1}\right)$ and stress $\left(f_{2}\right)$, which contains of eleven constraints and involves seven decision variables as follows, gear face width $\left(x_{1}\right)$, teeth module $\left(x_{2}\right)$, number of teeth of pinion $\left(x_{3}\right)$, distance between bearings $\left(x_{4}\right)$, distance between bearings $2\left(x_{5}\right)$, diameter of shaft $1\left(x_{6}\right)$, and diameter of shaft $2\left(x_{7}\right)$.

Table 7
Experimental results comparison of different multiobjective optimization algorithms on MIGD for $\left(n_{1}, \tau_{1}\right)=(10,10)$.

| Fun. | $\left(n_{1}, \tau_{1}\right)$ | MOMVO | MOALO | MOGOA | PFPA |
| :--: | :--: | :--: | :--: | :--: | :--: |
| DF1 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.182 \mathrm{e}-2(4.707 \mathrm{e}-4) \\ 1.157 \mathrm{e}-7 \\ 1 \end{gathered}$ | $\begin{gathered} 3.670 \mathrm{e}-2(2.492 \mathrm{e}-3) \\ 7.380 \mathrm{e}-10 \\ 1 \end{gathered}$ | $\begin{gathered} 4.737 \mathrm{e}-2(8.374 \mathrm{e}-3) \\ 3.197 \mathrm{e}-9 \\ 1 \end{gathered}$ | $\mathbf{5 . 8 1 9 e}-3(2.801 e-4)$ |
| DF2 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.279 \mathrm{e}-1(9.046 \mathrm{e}-3) \\ 1.492 \mathrm{e}-6 \end{gathered}$ | $\begin{gathered} 2.156 \mathrm{e}-1(1.932 \mathrm{e}-2) \\ 1.206 \mathrm{e}-10 \end{gathered}$ | $\begin{gathered} 1.903 \mathrm{e}-1(1.041 \mathrm{e}-2) \\ 2.872 \mathrm{e}-10 \end{gathered}$ | $\mathbf{4 . 9 3 2 e}-2(5.571 e-3)$ |
| DF3 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 6.044 \mathrm{e}-2(1.959 \mathrm{e}-2) \\ 2.670 \mathrm{e}-9 \end{gathered}$ | $\begin{gathered} 6.217 \mathrm{e}-2(9.415 \mathrm{e}-3) \\ 1.287 \mathrm{e}-9 \end{gathered}$ | $\begin{gathered} 7.898 \mathrm{e}-2(1.321 \mathrm{e}-2) \\ 1.174 \mathrm{e}-9 \end{gathered}$ | $\mathbf{8 . 8 5 9 e}-3(2.957 e-3)$ |
| DF4 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 9.836 \mathrm{e}-2(5.237 \mathrm{e}-3) \\ 1.335 \mathrm{e}-1 \end{gathered}$ | $\begin{gathered} 2.641 \mathrm{e}-1(4.634 \mathrm{e}-2) \\ 7.200 \mathrm{e}-5 \end{gathered}$ | $\begin{gathered} 1.952 \mathrm{e}-1(2.347 \mathrm{e}-2) \\ 9.792 \mathrm{e}-5 \end{gathered}$ | $\mathbf{7 . 1 4 6 e}-2(1.925 e-3)$ |
| DF5 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.089 \mathrm{e}-2(4.366 \mathrm{e}-4) \\ 1.407 \mathrm{e}-4 \end{gathered}$ | $\begin{gathered} 4.095 \mathrm{e}-2(3.865 \mathrm{e}-3) \\ 6.518 \mathrm{e}-9 \end{gathered}$ | $\begin{gathered} 3.651 \mathrm{e}-2(2.985 \mathrm{e}-3) \\ 1.429 \mathrm{e}-8 \end{gathered}$ | $\mathbf{6 . 8 1 9 e}-3(1.253 e-3)$ |
| DF6 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 6.693 \mathrm{e}-1(4.121 \mathrm{e}-2) \\ 2.707 \mathrm{e}-1 \end{gathered}$ | $\begin{gathered} 1.4932 \mathrm{e}+0(1.701 \mathrm{e}-1) \\ 3.387 \mathrm{e}-2 \end{gathered}$ | $\begin{gathered} 1.812 \mathrm{e}+0(3.526 \mathrm{e}-1) \\ 8.771 \mathrm{e}-2 \end{gathered}$ | $\mathbf{6 . 4 8 4 e}-1(5.727 e-2)$ |
| DF7 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 4.955 \mathrm{e}-2(9.104 \mathrm{e}-3) \\ 3.338 \mathrm{e}-11 \end{gathered}$ | $\begin{gathered} 4.825 \mathrm{e}-2(5.287 \mathrm{e}-3) \\ 3.020 \mathrm{e}-11 \end{gathered}$ | $\begin{gathered} 5.797 \mathrm{e}-2(6.698 \mathrm{e}-3) \\ 3.020 \mathrm{e}-11 \end{gathered}$ | $\mathbf{9 . 7 5 5 e}-3(2.019 e-4)$ |
| DF8 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.417 \mathrm{e}-2(1.117 \mathrm{e}-3) \\ 5.874 \mathrm{e}-4 \end{gathered}$ | $\begin{gathered} 2.617 \mathrm{e}-2(2.881 \mathrm{e}-3) \\ 8.841 \mathrm{e}-7 \end{gathered}$ | $\begin{gathered} 2.617 \mathrm{e}-2(2.368 \mathrm{e}-3) \\ 1.748 \mathrm{e}-5 \end{gathered}$ | $\mathbf{6 . 9 8 0 e}-3(3.363 e-4)$ |
| DF9 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.530 \mathrm{e}-1(7.793 \mathrm{e}-3) \\ 2.028 \mathrm{e}-7 \end{gathered}$ | $\begin{gathered} 1.862 \mathrm{e}-1(6.129 \mathrm{e}-3) \\ 1.202 \mathrm{e}-8 \end{gathered}$ | $\begin{gathered} 1.879 \mathrm{e}-1(1.085 \mathrm{e}-2) \\ 3.081 \mathrm{e}-8 \end{gathered}$ | $\mathbf{6 . 3 4 9 e}-2(4.895 e-3)$ |
| DF10 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.117 \mathrm{e}-1(6.022 \mathrm{e}-3) \\ 2.159 \mathrm{e}-1 \end{gathered}$ | $\begin{gathered} 1.566 \mathrm{e}-1(7.006 \mathrm{e}-3) \\ 9.919 \mathrm{e}-11 \end{gathered}$ | $\begin{gathered} 1.449 \mathrm{e}-1(1.396 \mathrm{e}-2) \\ 2.439 \mathrm{e}-9 \end{gathered}$ | $\mathbf{1 . 0 1 1 e}-1(4.221 e-3)$ |
| DF11 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 6.582 \mathrm{e}-1(2.923 \mathrm{e}-3) \\ 5.997 \mathrm{e}-1 \end{gathered}$ | $\begin{gathered} 6.874 \mathrm{e}-1(7.728 \mathrm{e}-3) \\ 4.733 \mathrm{e}-1 \end{gathered}$ | $\begin{gathered} 7.098 \mathrm{e}-1(8.849 \mathrm{e}-3) \\ 3.478 \mathrm{e}-1 \end{gathered}$ | $\mathbf{6 . 4 1 7 e}-1(1.518 e-3)$ |
| DF12 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 3.650 \mathrm{e}-1(2.923 \mathrm{e}-3) \\ 8.352 \mathrm{e}-8 \end{gathered}$ | $\begin{gathered} 3.941 \mathrm{e}-1(2.795 \mathrm{e}-2) \\ 4.421 \mathrm{e}-6 \end{gathered}$ | $\begin{gathered} 3.350 \mathrm{e}-1(2.088 \mathrm{e}-2) \\ 1.236 \mathrm{e}-3 \end{gathered}$ | $\mathbf{2 . 8 2 0 e}-1(4.677 e-3)$ |
| DF13 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 1.152 \mathrm{e}-1(5.209 \mathrm{e}-3) \\ 5.859 \mathrm{e}-6 \end{gathered}$ | $\begin{gathered} 1.130 \mathrm{e}+0(3.478 \mathrm{e}-1) \\ 1.329 \mathrm{e}-10 \end{gathered}$ | $\begin{gathered} 6.621 \mathrm{e}-1(3.637 \mathrm{e}-1) \\ 2.439 \mathrm{e}-9 \end{gathered}$ | $\mathbf{1 . 4 7 4 e}-1(5.111 e-3)$ |
| DF14 | $\begin{gathered} (10,10) \\ p \\ h \end{gathered}$ | $\begin{gathered} 5.116 \mathrm{e}-2(2.540 \mathrm{e}-3) \\ 5.692 \mathrm{e}-1 \end{gathered}$ | $\begin{gathered} 4.655 \mathrm{e}-1(7.299 \mathrm{e}-1) \\ 3.020 \mathrm{e}-11 \end{gathered}$ | $\begin{gathered} 1.994 \mathrm{e}-1(3.309 \mathrm{e}-1) \\ 3.825 \mathrm{e}-9 \end{gathered}$ | $\mathbf{5 . 3 1 4 e}-2(1.898 e-3)$ |
|  | $\begin{gathered} 11 / 1 / 1 \\ 8 / 0 / 6 \end{gathered}$ | $\begin{gathered} 8 / 0 / 6 \\ 8 / 0 / 6 \end{gathered}$ | $\begin{gathered} 13 / 0 / 1 \\ 13 / 0 / 1 \end{gathered}$ | $\begin{gathered} 1.143 \mathrm{e}-1 \\ 0 \end{gathered}$ | $\begin{gathered} 5.314 \mathrm{e}-2(1.898 \mathrm{e}-3) \\ - \end{gathered}$ |

Table 8
Experimental results considering MHV indicator for dynamic Welded Beam Design Problem

| Index | MOEADFD | TrDMOEA | DNSGAA | PPS | PFPA |
| :--: | :--: | :--: | :--: | :--: | :--: |
| MHV | $2.018 \mathrm{e}+0$ | $2.316 \mathrm{e}+0$ | $2.275 \mathrm{e}+0$ | $2.317 \mathrm{e}+0$ | $2.318 \mathrm{e}+0$ |
| std | $1.506 \mathrm{e}-2$ | $4.623 \mathrm{e}-3$ | $5.213 \mathrm{e}-3$ | $4.944 \mathrm{e}-3$ | $5.156 \mathrm{e}-3$ |
| p | $2.857 \mathrm{e}-2$ | $8.857 \mathrm{e}-1$ | $1.143 \mathrm{e}-1$ | $9.015 \mathrm{e}-1$ | - |
| h | 1 | 0 | 0 | 0 | - |

Table 9
Experimental results considering MHV indicator for Dynamic Speed Reducer Problem

| Index | MOEADFD | TrDMOEA | DNSGAA | PPS | PFPA |
| :--: | :--: | :--: | :--: | :--: | :--: |
| MHV | $5.604 \mathrm{e}+5$ | $5.426 \mathrm{e}+5$ | 2.265e+6 | $5.405 \mathrm{e}+5$ | $5.505 \mathrm{e}+5$ |
| std | $4.018 \mathrm{e}+4$ | $4.529 \mathrm{e}+4$ | $3.618 \mathrm{e}+2$ | $1.547 \mathrm{e}+4$ | $1.617 \mathrm{e}+4$ |
| p | $9.651 \mathrm{e}-1$ | $8.993 \mathrm{e}-1$ | $8.571 \mathrm{e}-2$ | $9.323 \mathrm{e}-1$ | - |
| h | 0 | 0 | 0 | 0 | - |

$$
\begin{aligned}
\operatorname{Min} f_{1}(x, t) & =a_{1}(t) x_{1} x_{2}^{2}\left(10 / 3 x_{3}^{2}+a_{2}(t) x_{3}-a_{3}(t)\right) \\
& -a_{4}(t) x_{1}\left(x_{6}^{2}+x_{7}^{2}\right)+a_{5}(t)\left(x_{6}^{3}+x_{7}^{3}\right) \\
& +a_{6}(t)\left(x_{4} x_{6}^{2}+x_{5}+x_{7}^{2}\right) \\
\operatorname{Min} f_{2}(x, t) & =\frac{\sqrt{\left(745 x_{4} / x_{5} x_{3}\right)^{2}-1.69 \times 10^{7}}}{a_{7} t / x_{8}^{4}} \\
\text { s.t. } g_{1}(x) & =\frac{1}{x_{1} x_{2}^{2} x_{3}}-\frac{1}{27} \leqslant 0 \\
g_{2}(x) & =\frac{1}{x_{1} x_{2}^{2} x_{3}^{2}}-\frac{1}{397.5} \leqslant 0 \\
g_{3}(x) & =\frac{x_{3}^{4}}{x_{2} x_{3} x_{4}^{4}}-\frac{1}{1.93} \leqslant 0 \\
g_{4}(x) & =\frac{x_{4}^{4}}{x_{3} x_{3} x_{5}^{4}}-\frac{1}{1.93} \leqslant 0 \\
g_{5}(x) & =x_{2} x_{3}-40 \leqslant 0 \\
g_{6}(x) & =x_{1} / x_{2}-12 \leqslant 0 \\
g_{7}(x) & =5-x_{1} / x_{2} \leqslant 0 \\
g_{8}(x) & =1.9-x_{4}+1.5 x_{6} \leqslant 0 \\
g_{9}(x) & =1.9-x_{5}+1.1 x_{1} \leqslant 0 \\
g_{10}(x) & =f_{1}(x, t) \leqslant 4300 \\
g_{11}(x) & =\frac{\sqrt{\left(745 x_{5} / x_{3} x_{3}\right)^{2}-1.515 \times 10^{6}}}{0.1 x_{1}^{2}} \leqslant 1100
\end{aligned}
$$

$a_{j}(t)=a_{j}+\frac{1}{10}, 1 \leqslant j \leqslant 6, a_{7}(t)=a_{7}+0.25-\frac{1}{1 / 4}, a_{1}=0.7854, a_{2}=14.933, a_{3}=43.0934, a_{4}=1.508, a_{5}=7.477, a_{6}=0.7854$, $a_{7}=0.1,2.6 \leqslant x_{1} \leqslant 3.6,0.7 \leqslant x_{2} \leqslant 0.8,17 \leqslant x_{3} \leqslant 28,7.3 \leqslant x_{4} \leqslant 8.3,7.3 \leqslant x_{5} \leqslant 8.3,2.9 \leqslant x_{6} \leqslant 3.9,5.0 \leqslant x_{7} \leqslant 5.5$

Table 9 clearly shows that PFPA is slightly worse than that of DNSGAA, but it is competitive with the other competitors in terms of MHV. The t-test values indicate that there is no significant difference between them. That means PFPA can be an alternative to existing approaches for handling complex dynamic multi-objective problems in real-world applications.

# 6. Conclusion 

In this paper, a polynomial fitting mechanism is employed for designing a dynamic multi-objective optimization algorithm, named PFPA, which includes three key parts for generating a high-quality search population after change detection. Each component plays an important role in improving population diversity and convergence during the course of optimization. Experimental results verified on a set of benchmark problems with various difficulties and two classical dynamic engineering design problems demonstrate that PFPA has competitive tracking ability compared with some state-of-the-art algorithms. In addition, each component and control parameter in the proposed algorithm is also analysed and discussed extensively. In our future work, prediction techniques and parameter settings will be further investigated.

## CRediT authorship contribution statement

Qingyang Zhang: Conceptualization, Writing - review \& editing, Funding acquisition, Resources. Xiangyu He: Methodology. Shengxiang Yang: Supervision, Project administration, Funding acquisition, Writing - review \& editing. Yongquan Dong: Supervision, Project administration, Funding acquisition, Writing - review \& editing. Hui Song: Formal analysis, Investigation. Shouyong Jiang: Supervision, Project administration, Funding acquisition, Writing - review \& editing.

## Data availability

Data will be made available on request.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work is supported by the National Natural Science Foundation of China under Grants 62006103 and 61872168, in part by the Jiangsu national science research of high education under Grand 20KJB110021, and in part by the Royal Society International Exchanges Scheme IEC|NSFC|211404.

# Appendix A. Supplementary data 

Supplementary data associated with this article can be found, in the online version, at https://doi.org/10.1016/j.ins. 2022. 08.020 .

## References

[1] K. Li, K. Deb, Q. Zhang, An evolutionary many-objective optimization algorithm based on dominance and decomposition, IEEE Trans. Evol. Comput. 19 (5) (2014), 694-176.
[2] S. Jiang, S. Yang, A steady-state and generational evolutionary algorithm for dynamic multiobjective optimization, IEEE Trans. Evol. Comput. 21 (1) (2016) 65-82.
[3] S. Gee, K. Tan, C. Alippi, Solving multiobjective optimization problems in unknown dynamic environments: An inverse modeling approach, IEEE Trans. Cybern. 47 (12) (2016) 4223-4234.
[4] C. Wang, G. Yen, M. Jiang, A grey prediction-based evolutionary algorithm for dynamic multiobjective optimization, Swarm. Evol. Comput. 100695 (2020).
[5] K. Deb, A. Pratap, S. Agarwal, T. Meyarivan, D fast and elitist multiobjective genetic algorithm: NSGA-II, IEEE Trans. Evol. Comput. 6 (2002) 182-197.
[6] K. Deb, H. Jain, An evolutionary many-objective optimization algorithm using reference-point based non-dominated sorting approach, part I: Solving problems with box constraints, IEEE Trans. Evol. Comput. 18 (4) (2014) 577-601.
[7] E. Zitzler, M. Laumanns, L. Thiele, SPEA2: Improving the Strength Pareto Evolutionary Algorithm. Technical Report 103, Computer Engineering and Networks Laboratory (TIK). Swiss Federal Institute of Technology (ETH), Zurich, Switzerland, 2001.
[8] S. Mirjalili, S. Mirjalili, S. Saremi, I. Aljarah, Grasshopper optimization algorithm for multi-objective optimization problems, Appl. Intell. 48 (2018) 805820 .
[9] S. Mirjalili, P. Jangir, S. Mirjalili, S. Saremi, I. Trivedi, Optimization of problems with multiple objectives using the multi-verse optimization algorithm, Knowl-based Syst. 134 (2017) 50-71.
[10] A. Auger, J. Bader, D. Brockhoff, E. Zitzler, Hypervolume-based multiobjective optimization: Theoretical foundations and practical implications, Theor. Comput. Sci. 425 (1) (2012) 75-103.
[11] D. Phan, J. Suzuki, R2-IBEA: R2 indicator based evolutionary algorithm for multiobjective optimization, IEEE Congr. Evol. Comput. (2013) 1836-1845.
[12] K. Bringmann, T. Friedrich, F. Neumann, M. Wagner, Approximation guided evolutionary multiobjective optimization, Proc. 21st Int. Joint Conf. Artif. Intell. (2011) 1198-1203.
[13] Q. Zhang, H. Li, MOEA/D: A multiobjective evolutionary algorithm based on decomposition, IEEE Trans. Evol. Comput. 11 (6) (2007) 712-731.
[14] D. Cai, W. Yuping, Y. Miao, a new multi-objective particle swarm optimization algorithm based on decomposition, Inf. Sci. 325 (2015) 541-557.
[15] S. Mirjalili, P. Jangir, S. Saremi, Multi-objective ant lion optimizer: a multi-objective optimization algorithm for solving engineering problems, Appl. Intell. 1-17 (2016).
[16] Z. Ma, Y. Wang, Shift-based penalty for evolutionary constrained multiobjective optimization and its application, IEEE Trans. Cybern. (2022) (in press).
[17] W. Han, H. Li, B. Xin, M. Gong, Automatic binary and ternary change detection in SAR images based on evolutionary multiobjective optimization, Appl. Soft Comput. 125 (2022) 109200.
[18] A. Vodopija, J. Stork, T. Bart-Beielstein, B. Filipic, Elevator group control as a constrained multiobjective optimization problem, Appl. Soft Comput. 115 (2022) 108277.
[19] C. Li, S. Yang, A general framework of multipopulation methods with clustering in indetectable dynamic environments, IEEE Trans. Evol. Comput. 16 (4) (2012) 556-577.
[20] R. Chang, H. Hsu, S. Lin, J. Ho, Query-based laerning for dynamic particle swarm optimization, IEEE Access. 5 (2017) 7648-7658.
[21] Y. Ye, Q. Lin, et al, Multiple source transfer learning for dynamic multiobjective optimization, Inform. Sci. 607 (2022) 739-757.
[22] J. Grefenstette, Genetic algorithm for changeing environments, Parallel Problem Solving from Nature 2 (1992) 137-144.
[23] S. Yang, Genetic algorithms with memory- and elitism-based immigrants in dynamic environments, Evol. Comput. 16 (3) (2008) 385-416.
[24] K. Deli, S. Karthik, Dynamic multi-objective optimization and decision-making using modified NSGA-II: a case study on hydro-thermal power scheduling, in: Lecture Notes in Computer Science. Springer Science mat, 803-817.
[25] J. Branke, Memory enhanced evolutionary algorithms for changing optimization problems, in: Proceedings of the 1999 congress on evolutionary computation. Institute of Electrical and Electronics Engineers, 1999.
[26] H. Xie, Z. Juan, S. Yang, et al, A decision variable classification-based cooperative coevolutionary algorithm for dynamic multiobjective optimization, Inf. Sci. 560 (2021) 307-330.
[27] R. Azzouz, S. Bechikh, L. Said, A dynamic multi-objective evolutionary algorithm using a change severity-based adaptive population management strategy, Soft Comput. 21 (4) (2015) 1-22.
[28] B. Xu, Y. Zhang, D. Gong, Y. Guo, M. Rong, Environment sensitivity-based cooperative co-evolutionary algorithms for dynamic multi-objective optimization, IEEE ACM Trans. Comput. Biol. 15 (6) (2017) 1877-1890.
[29] R. Liu, J. Li, C. Mu, L. Jiao, A coevolutionary technique based on multi-swarm particle swarm optimization for dynamic multi-objective optimization, Eur. J. Oper. Res. 261 (3) (2017) 1028-1051.
[30] X. Liu, Y. Zhou, X. Yu, Cooperative particle swarm optimization with reference-point-based prediction strategy for dynamic multiobjective optimization, Appl. Soft Comput. 87 (2020) 105988.
[31] A. Zhou, Y. Jin, Q. Zhang, A population prediction strategy for evolutionary dynamic multiobjective optimization, IEEE Trans. Cybern. 44 (1) (2014) 6677.
[32] A. Muruganantham, K. Tan, P. Vadakkepat, Evolutionary dynamic multiobjective optimization via kalman filter prediction, IEEE Trans. Evol. Comput. 46 (12) (2016) 2862-2873.
[33] Y. Hu, J. Ou, J. Zheng, et al, Solving dynamic multiobjective problems with an evolutionary multi-directional search approach, Knowl.-based Syst. 194 (2020) 1-15.
[34] A. Ahrari, S. Elsayed, R. Sarker, et al, Weighted pointwise prediction method for dynamic multiobjective optimization, Inf. Sci. 546 (2021) 349-367.
[35] Q. Li, J. Zhou, S. Yang, J. Zheng, G. Ruan, A predictive strategy based on special points for evolurionary dynamic multiobjective optimization, Soft Comput. 23 (2019) 3723-3739.
[36] Z. Zhang, S. Qian, Artificial immune system in dynamic environments solving time-varying non-linear constrained multi-objective problems, Soft Comput. 15 (7) (2011) 1333-1349.
[37] J. Eaton, S. Yang, M. Gongora, Ant colony optimization for simulated dynamic multi-objective railway junction rescheduling, IEEE Trans. Intell. Transp. 18 (11) (2017) 2980-2992.
[38] W. Kong, T. Chai, S. Yang, J. Ding, A hybrid evolutionary multiobjective optimization strategy for the dynamic power supply problem in magnesia grain manufacturing, Appl. Soft Comput. 13 (5) (2013) 2960-2969.
[39] D. Gong, B. Xu, Y. Zhang, Y. Guo, S. Yang, A similarity-based cooperative co-evolutionary algorithm for dynamic interval multiobjective optimization problems, IEEE Trans. Evol. Comput. 24 (1) (2019) 142-156.
[40] M. Hajiaghaei-Keshtehi, M. Aminnayeri, Solving the integrated scheduling of production and railtransportation problem by Keshtel algorithm, Appl. Soft comput. 25 (2014) 184-203.

[41] A. Yazici, G. Kirlik, O. Parlaktuna, A. Sipahioglu, A dynamic path planning approach for multirobot sensor-based coverage considering energy constraints, IEEE Trans. Cybern. 44 (3) (2014) 305-314.
[42] H. Ma, Z. Yang, P. You, M. Fei, Multi-objective biogeography-based optimization for dynamic economic emission load dispatch considering plug-in electric vehicles charging, Energy 135 (2017) 101-111.
[43] Q. Zhang, S. Yang, R. Wang, et al, Novel Prediction Strategies for Dynamic Multiobjective optimization, IEEE Trans. Evol. Comput. 24 (2) (2020) 260274.
[44] O. Theohald, Machine Learning for absolute beginners: A plain English Introduction, third ed., Scatterplot Press, 2021.
[45] S. Jiang, S. Yang, X. Yao, K. Tan, M. Kaiser, N. Krasnogor, Benchmark problems for CEC2018 Competition on Dynamic multiobjective optimization, 2018 IEEE Congress on Evolutionary Computation, Competition on Dynamic Multiobjective Optimisation (2018).
[46] W. Sohna, M. Jeong, K. Jeonga, Theoretical comparative study of t-tests and nonparametric tests for final status surveys of MARSSIM at decommissioning sites, Ann. Nucl. Energy 135 (2020) 106945.
[47] L. Cao, L. Xu, E. Goodman, H. Li, A First-Order Difference Model-Based Evolutionary Dynamic Multiobjective Optimization, Asia-Pacific Conference on Simulated Evolution and Learning, Simulated Evolution and Learning (2017) 644-655.
[48] M. Jiang, Z. Huang, L. Qiu, W. Huang, Transfer learning-based dynamic multiobjective opyimization algorithms, IEEE Trans. Evol. Comput. 22 (4) (2017) $501-514$.
[49] Q. Zhang, A. Zhou, S. Zhao, P. Suganthan, W. Liu, S. Tiwari, Multiobjective optimization Test Instances for the CEC, Special Session and Competition, IEEE Congress on Evolutionary Computation (CEC) 2009 (2009).