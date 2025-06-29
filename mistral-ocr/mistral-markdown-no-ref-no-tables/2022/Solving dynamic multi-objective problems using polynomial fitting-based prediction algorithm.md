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
# 3.4. Parameter settings 

The relevant parameters of all the compared algorithms are same as their original studies, and the population size is set to 100. Each algorithm is executed twenty-five independent runs on each benchmark instance. Besides that, ten percent of the population is used to detect each of the thirty times of change in dynamic optimization.

### 3.5. Experimental results

Test problems used in this paper involves two important control parameters, the severity of change $\left(n_{t}\right)$ and the frequency of change $\left(\tau_{t}\right)$, which take values from $(5,10,20)$ for evaluating the robustness of the proposed algorithm. MIGD values and t-test results are presented in Tables 1-3 (MSP, MHV results can be found in Supplementary Material), in which the best results are also highlighted in bold face.

It is observed from the MIGD and $t$ - test values reported in Tables 1-3 that PFPA clearly outperforms the other compared algorithms on majority of the test problems. In Table 1, the statistical $p$-values illustrate that there are not significant differences among all the algorithms on DF5 and DF11. As the parameters change, the differences become clear for DF10 and DF11. Totally, for different combinations of $n_{t}$ and $\tau_{t}$, PFPA can generate best results on most of the problems, which means that the proposed prediction mechanism is able to obtain high-quality populations for tracking the Pareto-optimal front effectively in dynamic environments.

Table 2
Mean and standard deviation values of MIGD obtained by five algorithm for $\left(n_{t}, \tau_{t}\right)=(10,10)$.
Table 3
Mean and standard deviation values of MIGD obtained by five algorithm for $\left(n_{i}, \tau_{i}\right)=(10,20)$.
Tables 1-3 (presented in Supplementary Material) present the MHV and $t$-test values of all the optimization algorithms, and demonstrate that when $n_{i}$ is five, PFPA performs much better than MOEADFD, PPS, NSGAA on the most of the problems, and slightly worse than TrDMOEA on DF5, DF11, DF12 according to the $p$-values. With the change of the parameters, the proposed algorithm still retains significant advantage and is competitive with TrDMOEA. Therefore, in terms of this metric, PFPA has stable and fast responses to dynamic changes.

It can be seen from the MSP and $t$-test values, shown in Tables 4-6 (presented in Supplementary Material), that PFPA has a significant advantage over the other algorithms on some bi-objective problems (e.g., DF1, DF7 and DF8) and performs ineffectively on tri-objective problems. The frequency and severity of change has not obvious impact on all the algorithms. The reason is that most of the algorithms have a good diversity maintenance mechanism (e.g., the decomposition framework for MOEADFD). Pareto-dominance based MOEAs do not seem to be effective for generating uniformly distributed solutions, especially in three-objective cases. However, it is necessary to measure the overall effectiveness of an algorithm from multiple metrics rather than one indicator. Therefore, although PFPA does not achieve good MSP values, it has significant advantages on other metrics.

Some convergence curves of MIGD values are provided in Fig. 4, which shows that the difference is small between PFPA and DNSGAA on DF4, but PFPA outperforms other algorithms in terms of convergence lines. For DF10, the proposed algorithm has a significant advantage in the late stage of environmental change. For other problems, PFPA has competitive performance. Overall, PFPA has more stable convergence and responds faster to changes than other compared algorithms on most of the problems.

Table 4
Performance comparison of different PFPA variants on MIGD
Fig. 5-8 present some POF approximations. It can be found that the individuals obtained by PFPA are closer to the real POF and are evenly distributed on DF3. For DF5, the PFPA algorithm can obtain individuals with good distribution, but there is a gap between the obtained solutions and the true POF. In later changes, the individuals obtained by PFPA are close to the POF with good distribution, and the convergence is obviously better than the other algorithms. The approximation of PFPA is significantly better than the other algorithms on DF7 and DF8. Thus, PFPA have a good approximation to the changing POF, which means that the designed algorithm has potential tracking ability in changing environments.

# 4. Discussion 

### 4.1. Component analysis

As mentioned before, the proposed dynamic response mechanism contains three different key strategies for generating high-quality population and tracking the changing Pareto front effectively. This subsection focuses on the impact of each strategy on the search performance of the proposed algorithm. Specifically, to illustrate the role of multi-step movement strategy, PAPFV1 is designed by integrating a one-step movement model which is widely employed in most existing prediction approaches for dynamism handling. PFPAV2 and PFPAV3 are designed by removing the polynomial fitting strategy and sampling strategy for showing the effect of the corresponding techniques,respectively. PFPA is also utilized to compare with these three modified versions, Table 4 presents the experimental and comparison results in detail.

Table 5
Performance comparison of PFPA variants on MIGD for $\left(n_{i}, \tau_{i}\right)=(10,10)$.
# 4.1.1. Multi-step movement strategy 

It is observed from Table 4 that, although there exists some similar results indicated by the p-values, PFPA performs much better than the other three variants on the majority of the test problems. This shows that the multi-step strategy is able to generate more better individuals close to the real POS and improves the diversity of the population and the search efficiency of the algorithm. Therefore, it can be seen that this strategy is an important part of the proposed algorithm. It is worth noting that this strategy is likely to generate boundary solutions, which may not benefit for global search. This strategy should be improved in future work.

### 4.1.2. Polynomial fitting-based Strategy

Table 4 clearly demonstrates that there are not differences between PFPA and PFPAV2 on DF6 and DF11, but PFPA is much superior to PFPAV2 on eleven benchmark problems, which means that this strategy is indeed able to improve the search performance of PFPA. This could be explained by the fact that this strategy fully considers the distribution relationship between variables, which is helpful to generate promising solutions to some extent.

### 4.1.3. Sampling strategy

This strategy aims to make full use of the relationship between variables to generate high-quality individuals to guide the search, thus speeding up the search efficiency of the algorithm. The experimental results also show that this strategy can improve the search performance of the algorithm to some extent in varying environments.

Table 6
Performance comparison of PFPA variants on MIGD for $\left(n_{i}, \tau_{i}\right)=(10,10)$.
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
Table 8
Experimental results considering MHV indicator for dynamic Welded Beam Design Problem

Table 9
Experimental results considering MHV indicator for Dynamic Speed Reducer Problem

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
