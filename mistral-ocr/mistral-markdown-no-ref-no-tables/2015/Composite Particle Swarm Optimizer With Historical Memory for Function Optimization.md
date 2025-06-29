# Composite Particle Swarm Optimizer With Historical Memory for Function Optimization 

Jie Li, JunQi Zhang, Senior Member, IEEE, ChangJun Jiang, and MengChu Zhou, Fellow, IEEE


#### Abstract

Particle swarm optimization (PSO) algorithm is a population-based stochastic optimization technique. It is characterized by the collaborative search in which each particle is attracted toward the global best position (gbest) in the swarm and its own best position (pbest). However, all of particles' historical promising phests in PSO are lost except their current pbests. In order to solve this problem, this paper proposes a novel composite PSO algorithm, called historical memorybased PSO (HMPSO), which uses an estimation of distribution algorithm to estimate and preserve the distribution information of particles' historical promising pbests. Each particle has three candidate positions, which are generated from the historical memory, particles' current pbests, and the swarm's gbest. Then the best candidate position is adopted. Experiments on 28 CEC2013 benchmark functions demonstrate the superiority of HMPSO over other algorithms.


Index Terms-Estimation of distribution algorithm (EDA), historical memory, particle swarm optimization (PSO).

## I. INTRODUCTION

PARTICLE swarm optimization (PSO) [1], [2] is a population-based stochastic optimization technique, and has been used to solve a wide variety of continuous and discrete optimization problems. PSO contains a swarm of particles and each particle that corresponds to a potential solution can fly in a search space with its velocity. Its significant characteristic is that all particles follow collaborative search in which each particle is attracted toward

[^0]the global best position (gbest) in the swarm and its own best position (pbest). In recent years, improving PSO's performance by designing different methods has been an active research topic. Reference [3] presents a cooperative particle swarm optimizer (CPSO) that uses multiple swarms to optimize different components of the solution vector cooperatively. Reference [4] presents a fully informed particle swarm (FIPS) that uses all the neighbors to influence the flying velocity. Reference [5] presents a self-organizing hierarchical particle swarm optimizer with time-varying acceleration coefficients (HPSO-TVAC) that uses time-varying acceleration constants. Reference [6] presents a comprehensive learning particle swarm optimizer (CLPSO) that uses all particles' current pbests to update the velocity of any one particle. Reference [7] presents a PSO with an aging leader and challengers (ALCPSO) by using an aging mechanism. Reference [8] presents a self-government PSO in which each particle updating depends on local best information searched at the last iteration as well as pbest and gbest. It is applied to solve a texaco gasification problem. Reference [9] presents two PSO-based multiobjective feature selection algorithms in classification. Reference [10] presents a co-evolutionary PSO algorithm associating with the artificial immune principle. It is verified in multiparameter estimation of permanent magnet synchronous machines. Reference [11] presents a hybrid PSO and genetic algorithm to solve a multiple unmanned aerial vehicle formation reconfiguration problem. Reference [12] presents a novel PSO method using swarm intelligence to solve an optimal power flow problem with distributed generator failures in power networks.
Although the aforementioned algorithms have obtained satisfactory results, they tend to strike in the local optimum. A key reason behind these PSOs is that they use only the information of gbest and a particle's own current best position (pbest), while they fail to utilize all of particles' historical promising pbests except their current pbests. In this case, a particle will move in a local optimum and it may be impossible to jump out of the local optimum area once its pbest falls into the same local optimum region where the gbest locates.

Intuitively, the historical memory of particles can help PSO to overcome the drawback and improve performance. The reason is that the implicit or explicit historical memory allows PSO to store promising solutions and reuse their information later so as to improve the search process. On one hand,


[^0]:    Manuscript received January 27, 2015; accepted April 9, 2015. This work was supported in part by the National Natural Science Foundation of China under Grant 61272271, Grant 61332008, and Grant 91218301, in part by the NSF of USA under Grant CMMI-1162482, in part by the National Basic Research Program of China (973 Program) under Grant 2014CB340404, in part by the Natural Science Foundation Program of Shanghai under Grant 12ZR1434000, and in part by the International Cooperation Project of Chinese Ministry of Science and Technology under Grant 2012DFG11580. This paper was recommended by Associate Editor Jun Zhang. (Corresponding authors: JunQi Zhang and ChangJun Jiang.)
    J. Li, J. Q. Zhang, C. J. Jiang, and M. C. Zhou are with the Department of Computer Science and Technology, Key Laboratory of Embedded System and Service Computing, Ministry of Education, Tongji University, Shanghai 201804, China (e-mail: lijiejsh@gmail.com; zhangjunqi@tongji.edu.cn; cjjiang@tongji.edu.cn).
    M. C. Zhou is also with the Department of Electrical and Computer Engineering, New Jersey Institute of Technology, Newark, NJ 07102 USA (e-mail: zhou@njit.edu).

    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

    Digital Object Identifier 10.1109/TCYB.2015.2424836

the historical memory preserves the information of optimum solution space that particles have searched, which enable particles to return to these optimum regions if they fall into local optima. On the other hand, the historical memory that derives from different particles can also maintain the diversity of population to some extent.

However, traditional historical memory methods store a great number of promising solutions, thereby requiring a large memory space and a complex memory management scheme. Estimation of distribution algorithm (EDA) introduced in [13] has good potential to solve this problem. EDA belongs to a class of probability model-based evolutionary algorithms (EAs), where the processes of learning and sampling the probability model replace the crossover and mutation operations in a conventional genetic algorithm. A probability model indicates the joint probability distribution of high-performance solutions, i.e., it characterizes the set of promising solutions. If the historical information could be stored as probability models, we would not only save the memory space drastically but also simplify the memory management scheme. Consequently, EDA may play the role of historical memory in PSO.

Next, we consider how can one dig out and use the historical information to advance PSO? To answer it, this paper proposes a novel composite PSO algorithm, called historical memory-based PSO (HMPSO), which uses EDA to estimate and preserve distribution information of particles' historical promising pbests, then forms historical memory information, and finally integrates it into PSO to guide the search. Each particle is expected to have more comprehensive learning and search ability with the help of historical memory information. So far, there are three types of useful information existing in PSO, i.e., historical memory, particles' current pbests, and the swarm's gbest. Thus, how to systematically and best use them becomes a thorny and interesting problem. To solve it, we define a new particle generation mechanism whose primary idea is to generate a new particle through competing among three candidate particles that are generated by the information at each iteration.

In order to show the advantages of HMPSO, we compare it with CPSO-H6 [3], CLPSO [6], ALCPSO [7], FIPS [4], HPSO-TVAC [5], EDA-PSO [14], and particle swarm EDA (PSEDA) [15]. These algorithms are popular and their performance is better than most PSO algorithms. Moreover, two HMPSO variants are proposed and compared. They build the historical memory via a local distribution model for each particle and a multivariate Gaussian distribution for the population, respectively. Experiments on 28 CEC2013 benchmark functions demonstrate the superiority of HMPSO over them due to the use of historical memory and the related particle generation mechanism.

This paper is organized as follows. In Section II, traditional PSO, CLPSO, and EDA algorithms are introduced together with the similar state-of-the-art techniques using memory-based EAs and the hybridization of PSO and EDA. The proposed HMPSO is presented in Section III. Extensive simulation results are presented in Section IV. Finally, the conclusion is given in Section V.

## II. RELATED WORKS

## A. PSO and Comprehensive Learning PSO

PSO [1], [2] has been in existence as an EA for roughly twenty years, and has shown excellent performance in many application domains since it owns a simple social learning model. In PSO, a particle represents a potential solution in a search space, and many particles form a swarm. Each particle adjusts dynamically its flying direction according to the gbest of the swarm and the experience of personal best position (pbest).

Initially, PSO is equipped with a swarm of $Q$ possible particles randomly generated from a search space. The position and velocity of the $i$ th particle are updated at each iteration by the following rules for $d=1,2, \ldots, D$ :

$$
\begin{aligned}
V_{i}^{d}=\omega \times V_{i}^{d}+c_{1} \times r 1_{i}^{d} & \times\left(\text { pbest }_{i}^{d}-X_{i}^{d}\right) \\
& +c_{2} \times r 2_{i}^{d} \times\left(\text { gbest }^{d}-X_{i}^{d}\right) \\
X_{i}^{d}=X_{i}^{d}+V_{i}^{d} & \text { (1) }
\end{aligned}
$$

where $\mathbf{X}_{i}=\left(X_{i}^{1}, X_{i}^{2}, \ldots, X_{i}^{D}\right)$ is the position of the $i$ th particle, $\mathbf{V}_{i}=\left(V_{i}^{1}, V_{i}^{2}, \ldots, V_{i}^{D}\right)$ is its velocity, $\mathbf{p b e s t}_{i}^{d}=$ $\left(\right.$ pbest $\left.{ }_{i}^{1}, \mathrm{pbest}_{i}^{2}, \ldots, \mathrm{pbest}_{i}^{D}\right)$ is its personal best position, gbest $^{d}=\left(\right.$ gbest $\left.{ }^{1}, \mathrm{gbest}^{2}, \ldots, \mathrm{gbest}^{D}\right)$ is the global best position discovered by the whole swarm, $D$ is the dimension of the problem to be optimized, $r 1_{i}^{d}$ and $r 2_{i}^{d}$ are two random numbers in the range $[0,1]$ for particle $i, c_{1}$ and $c_{2}$ are acceleration constants, and $\omega$ is inertia weight that is used to balance the global and local search.

PSO has a serious defect, i.e., it is easy to be trapped into a local optimum when it solves multimodal problems [6], [16]. CLPSO [6] is proposed to solve such premature convergence problem. It ensures the diversity of swarm because all particles' pbests are used to update the velocity of any one particle. The velocity updating equation is

$$
\begin{aligned}
& V_{i}^{d}=\omega \times V_{i}^{d}+c \times r_{i}^{d} \times\left(\text { pbest }_{f i(d)}^{d}-X_{i}^{d}\right) \\
& X_{i}^{d}=X_{i}^{d}+V_{i}^{d}
\end{aligned}
$$

where $\operatorname{pbest}_{f i(d)}^{d}$ is the $d$ th component of any particle's pbest in the swarm, $\mathbf{f}_{i}=\left\{f_{i}(1), f_{i}(2), \ldots, f_{i}(D)\right\}$ is the function that decides which particle's pbest in the swarm particle $i$ should follow, $r_{i}$ is a random number in the range $[0,1]$ for particle $i$, and $c$ is an acceleration constant. CLPSO is described as follows.

1) Select two particles from the current swarm randomly excluding particle $i$ whose velocity is to be updated.
2) Compare the fitness values of two selected particles' pbests through a tournament selection procedure and select the better one.
3) Use the winner's pbest as an exemplar to update velocity (3) for the corresponding component.

## B. Estimation of Distribution Algorithm

EDA [13], [17] is a new class of evolutionary computation methods. The main difference between EDA and traditional evolutionary computation algorithms is that the interrelations

in EDA are expressed explicitly through the joint probability distribution associated with the individuals selected by a certain selection procedure from the previous generation, while the interactions in the latter are implicitly kept. New offspring in EDA are generated by sampling the probability distribution that is estimated from the selected individuals of the previous generation. The most difficult work in EDA is the estimation of the joint probability distribution associated with selected individuals. The following is a description of EDA.

1) Generate the initial population randomly.
2) Select promising individuals from the population according to their fitness values by using a certain selection procedure.
3) Estimate the joint probability distribution of the selected promising individuals.
4) Sample new offspring individuals according to the joint probability distribution.
5) Use new sampled offspring individuals to replace some worse individuals in the previous population.

## C. Memory-Based Evolutionary Algorithms

Memory is an essential feature of all living systems and a significant part of physical, chemical, and engineering systems. EAs are inspired by a biological evolutionary process in nature. From the evolutionism point of view, the effects of memory can be used in the process of EAs.

In the past few decades, there was a great deal of meaningful work in this field. For example, the work in [18] presents a memory mechanism by introducing memory modules into a membrane algorithm for solving knapsack problems. Reference [19] presents a stochastic evolution algorithm for solving multiobjective shortest path problems by using memory efficiently. Reference [20] presents a modified harmony search algorithm together with a new memory consideration scheme based on a roulette wheel mechanism. It is applied to solve economic load dispatch and combined economic and emission load dispatch problems. Reference [21] investigates the evolving ability of a cellular automaton with a type of memory based on the least mean square algorithm. Reference [22] presents a memory-efficient stochastic evolution-based algorithm for solving multiobjective shortest path problems. Reference [23] presents a clonal selection subpixel mapping framework by building a memory cell population. Reference [24] presents a directional feature in standard covariance matrix adaptation and evolution strategy by utilizing potentially useful memory information from the previous generation. Reference [25] presents several memory-based multiobjective EAs and applies them to solve multiobjective dynamic optimization problems. Reference [26] presents a model of an evolutionary game with a memory mechanism. Reference [27] presents a new model of memory in cellular learning automata-based evolutionary computing, which is used to address those time-varying optimization problems.

Although these studies have achieved great success, a challenge still remains, i.e., their methods require a large memory space and a complex memory management scheme. In order to solve this problem to some extent, EDA is a potential
algorithm to store historical information by using its probability models, which can not only save the memory space effectively, but also simplify the memory management scheme greatly. Among the attempts to use EDA for this purpose, the work in [28] presents a reactive and EA, which modifies tentative solutions by local search with memory guided by EDA. Reference [29] presents an environment identification-based memory management scheme by EDAs for solving dynamic optimization problems.

## D. Hybridization of PSO and EDA

Memory is a very effective mechanism to enhance the performance of EAs. EDA is an algorithm to store and build historical information by its probability model. Next, we will introduce the existing hybrid algorithms of PSO and EDA to show how EDA is used in PSO.

Liu et al. [30] presented hybrid PSO-EDA to solve a permutation flowshop scheduling problem through the sharing of information from the collective experience of EDA and PSO. Zhou et al. [31] developed a discrete estimation of distribution PSO algorithm to solve combinatorial optimization problems by utilizing the statistical information collected from particles' current pbests. Wang et al. [32] presented a discrete PSO algorithm based on EDA to solve polygonal approximation problems by incorporating the global statistical information collected from EDA into PSO, and generating a new particle via the random use of the information from PSO or EDA. Wang et al. [33] proposed a novel discrete quantum behaved PSO based on EDA for the combinatorial optimization problem in which EDA is used to extract global statistical information of current promising solutions. Wang [34] presented a modified genetic PSO based on EDA for combinatorial optimization problems where EDA is used to collect the global statistical information from particles' local best solutions. Alguliev et al. [35] proposed a discrete PSO based on EDA that models the distribution of promising solutions for document summarization.

Besides, the hybridization of PSO and EDA has been performed to solve some continuous optimization problems. A significant work is EDA-PSO [14] where the population is split into chunks, and the update of particles within a chunk follows PSO rules, while the global update is based on EDA. EDA is used to estimate the current selected promising solutions and some new offspring are from both EDA and PSO. Reference [15] presents PSEDA in which the position update process is simulated as a mixture of Gaussian distribution, which is in turn used to generate new offspring. Reference [36] presents PSO_Bounds that uses EDA to manipulate the allowable bounds for PSO particles, in which the location of current promising particles is estimated by EDA while new offspring are generated in an estimated appropriate interval. Reference [37] presents a hybrid EDA-PSO method in which EDA uses a Gaussian model to capture current promising solutions' characteristics and generate new individuals. Reference [38] presents an estimation of distribution PSO that borrows ideas from ant colony optimization. Reference [39] presents the hybrids of EDA and two PSO

variants through probabilistic modeling of best solutions in the swarm. Reference [40] presents an estimation of particle swarm distribution algorithm where EDA is used to estimate the distribution of current selected promising solutions and some portions in a new particle are generated from EDA that can provide global information and others are supplied by PSO that owns local information.
Through the above analysis, we can see clearly that the existing methods use only EDA to estimate the distribution of their current selected particles or pbests. EDA is never used to store the historical memory of particles' promising pbests that may be helpful to improve the performance of PSO. This paper is the first to use EDA to store the historical memory of particles' promising pbests in PSO and then define a new particle generation mechanism.

## III. PROPOSED HMPSO

Original PSO may be trapped into a local optimum because all particles in the swarm may easily be attracted to the gbest region. CLPSO [6] is proposed to avoid its premature convergence to a certain extent. Any particle in it can learn from other particles' current pbests, i.e., each component of a particle's position and velocity can potentially learn from a different particle, thereby giving the particles more chances to use the beneficial information of the swarm, and eventually having a larger potential space to fly. However, both original PSO and CLPSO fail to retain and use all of particles' historical promising pbests except their current pbests. In order to do so, this paper presents HMPSO by innovatively using EDA to estimate and preserve the distribution information of particles' historical promising pbests that are selected by a tournament procedure.
The advantage of incorporating EDA into HMPSO is that the pbests' historical promising information of particles in the swarm can be estimated and preserved. Historical memory is formed, and it is beneficial because it is able to reflect the distribution of particles' historical promising pbests in the solution space. Thus, we can see that the main role of EDA is that it can build a distribution model of this historical memory and extract meaningful information from it to guide the search of each particle. In this way, each particle has more comprehensive learning and search ability with the help of this historical memory information than CLPSO.
HMPSO carries the following information: historical memory, particles' current pbests, and the swarm's gbest. We define a new particle generation mechanism to use them.

## A. Historical Memory $H$

Historical memory $H$ is decided as follows.

1) Generate randomly a swarm of $Q$ particles from a search space and calculate their fitness values, and then obtain all particles' pbests and swarm's gbest.
2) Select $N$ promising pbests from the swarm according to their fitness values by using a selection procedure, e.g., a tournament procedure.
3) Adopt EDA to estimate the distribution of good regions in the search space based on the selected
promising pbests. Population-based incremental learning (PBIL) [41] is used to model the distribution of the selected promising pbests and construct historical memory. So there is a distribution vector $\mathbf{P}=$ $\left(p^{1}, p^{2}, \ldots, p^{d}, \ldots, p^{D}\right), \quad 1 \leq d \leq D$, in which $p^{d}$ is used to characterize the $d$ th component's distribution of the selected promising pbests in the search space, and it is learned and updated from the distribution of historical selected promising pbests' memory and current selected promising pbests. Here, the distribution vector $\mathbf{P}$ is considered as the historical memory for every component. New offspring are generated by sampling the updated distribution model. Let $\widetilde{p}^{d}$ be a distribution of the $d$ th component by estimating current selected promising pbests. In HMPSO, we assume that the distribution of each component follows a normal distribution, thereby demanding EDA to estimate and preserve two parameters only, i.e., mean and standard deviation, expressed as $\widetilde{p}_{m}^{d}$ and $\widetilde{p}_{s}^{d}$, respectively. That is, $\widetilde{p}^{d}=\left\{\widetilde{p}_{m}^{d}, \widetilde{p}_{s}^{d}\right\}$ and $p^{d}=\left\{p_{m}^{d}, p_{s}^{d}\right\}$. The initial value $\widetilde{p}^{d}(1)$ is calculated in (7) and (8) when $t=0$ and is treated as the initial value of $p^{d}$. The updating formulas of $p_{m}^{d}, p_{s}^{d}, \widetilde{p}_{m}^{d}$, and $\widetilde{p}_{s}^{d}$ at time $t+1$ are as follows:

$$
\begin{aligned}
& p_{m}^{d}(t+1)=\left(1-m_{\lambda}\right) \times p_{m}^{d}(t)+m_{\lambda} \times \widetilde{p}_{m}^{d}(t+1) \\
& p_{s}^{d}(t+1)=\left(1-\operatorname{Var}_{\lambda}\right) \times p_{s}^{d}(t)+\operatorname{Var}_{\lambda} \times \widetilde{p}_{s}^{d}(t+1) \\
& \widetilde{p}_{m}^{d}(t+1)=\frac{\sum_{i=1}^{N} \text { pbest }_{i}^{d}}{N} \\
& \widetilde{p}_{s}^{d}(t+1)=\sqrt{\frac{\sum_{i=1}^{N}\left(\text { pbest }_{i}^{d}-\widetilde{p}_{m}^{d}(t+1)\right)^{2}}{N}}
\end{aligned}
$$

where $p_{m}^{d}$ and $p_{s}^{d}$ can be regarded as the distribution of mean and standard deviation for modeling the particles' historical promising pbests. $m_{\lambda}$ and $\operatorname{Var}_{\lambda} \in[0,1]$ are the learning parameters of mean and standard deviation, respectively. They are used to balance the contributions between historical memory and the information extracted from the current particles' pbests. The bigger $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$, the greater contribution of current particles' pbests; while the smaller $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$, the greater contribution of historical memory. Thus, the setting of learning parameters $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$ has a direct impact on exploration and exploitation abilities. For example, if $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$ are 0 , there is no exploitation and the offspring solutions are sampled based on cumulative historical memory completely. As $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$ increase, the exploitation ability increases, while the exploration ability to search the portions of historical memory in a problem space diminishes.

## B. Information Pool Used in HMPSO

In HMPSO, historical memory $H$, particles' current pbests, and the swarm's gbest constitute an information pool $I=$ $\left(H_{i}^{d}\right.$, Cpbest $\left._{i}^{d}\right.$, gbest $\left._{i}^{d}\right)^{T}$, to be explained next.

1) $H_{i}^{d}$. It is obtained from particles' historical promising pbests via a tournament selection procedure. When it is selected as the next value of the $i$ th particle's

$d$ th component, we perform the learning based on historical memory.
2) $\operatorname{Cphest}_{i}^{d}$ : It is obtained from other particle's pbests. When it is selected as the $i$ th particle's $d$ th component, we perform comprehensive learning [6]. The way that selects it is as same as CLPSO.
a) Select two particles from current population randomly excluding particle $i$.
b) Compare the fitness values of two selected particles' pbests through a tournament selection procedure and choose the better one.
c) Use the winner's pbest to update the velocity for that component.
3) $\operatorname{gbest}_{i}^{d}$ : It is the swarm's global gbest. When it is selected as the next value of the $i$ th particle's $d$ th component, we perform in-depth learning [1].
Note that pbests and gbest are obtained according to the general procedure in PSO.

## C. Velocity Updating and Position Generating Strategy

A new velocity updating equation is designed and used to generate new one

$$
V_{i_{-} j}^{d}(t+1)=\omega \times V_{i}^{d}(t)+c \times r_{i_{-} j}^{d} \times\left(Y_{i_{-} j}^{d}(t)-X_{i}^{d}(t)\right)
$$

where $Y_{i_{-} j}^{d}$ denotes the information that is used in the $d$ th component for the $j$ th candidate position in the $i$ th particle, $V_{i_{-} j}^{d}$ is its velocity, $r_{i_{-} j}^{d}$ is a random number in the range $[0,1]$. Then a new candidate's position is generated

$$
\operatorname{Pos}_{i_{-} j}^{d}(t+1)=X_{i}^{d}(t)+V_{i_{-} j}^{d}(t+1)
$$

where $\mathbf{P o s}_{i_{-} j}=\left(\operatorname{Pos}_{i_{-} j}^{1}, \operatorname{Pos}_{i_{-} j}^{2}, \ldots, \operatorname{Pos}_{i_{-} j}^{D}\right)$ is the $j$ th candidate position of the $i$ th particle. $j \in\{1,2,3\}$ is the index of three elements in information pool $I$, respectively. Here, we assume that the optimization function is to be minimized. The index of the best candidate position is calculated as

$$
\begin{aligned}
m_{i} & =\arg \min _{j \in\{1,2,3\}} F\left(\operatorname{Pos}_{i_{-} j}(t+1)\right) \\
Y_{i_{-} m_{i}}^{d}(t+1) & =e_{m_{i}}(t+1) \times\left(H_{i}^{d}, \operatorname{Cphest}_{i}^{d}, \operatorname{gbest}_{i}^{d}\right)^{T} \\
e & =\left(\begin{array}{l}
e_{1} \\
e_{2} \\
e_{3}
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)
\end{aligned}
$$

where $m_{i} \in\{1,2,3\}$ defines the best candidate position index from a fitness function $F\left(\operatorname{Pos}_{i_{-} j}(t+1)\right)$ and it is used to update all components of the $i$ th particle. $Y_{i_{-} m_{i}}^{d}$ represents the information as calculated by the product of $e_{m_{i}}$ and information pool $I . e$ is a $3 \times 3$ unit matrix and $e_{m_{i}}(t+1)$ is used to indicate which row vector is at iteration $t+1 . Y_{i_{-} m_{i}}^{d}(t+1)$ determines the best velocity $V_{i_{-} m_{i}}^{d}(t+1)$ in (9) and the best candidate position $\operatorname{Pos}_{i_{-} m_{i}}^{d}(t+1)$ in (10).

The final position is generated from the best candidate position

$$
X_{i}^{d}(t+1)=\operatorname{Pos}_{i_{-} m_{i}}^{d}(t+1)
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. Flowchart of HMPSO. $t$ : time counter from 1 to max_ $t$.

## D. Complete Procedure of HMPSO

The flowchart of HMPSO is given in Fig. 1. The details of the proposed HMPSO process are presented in Algorithm 1. At each iteration, historical memory, particles' current pbests, and the swarm's gbest in the information pool are used to create three new candidate positions. Then the best one enters the next iteration.

HMPSO differs from other PSO algorithms in the following two aspects.

1) It uses EDA to form historical memory, while other PSO algorithms fail to do so. EDA can estimate and preserve the distribution of some particles' historical promising pbests. It is beneficial because it is able to reflect the promising regions in a search space.

## Algorithm 1 HMPSO

```
begin
do
```

3: At iteration $t \geq 1$, calculate the fitness value for each particle in the swarm and update their own pbests and the swarm's gbest;
4: Select two particles from the current population randomly excluding particle $i$ whose velocity needs update;
5: Compare the fitness values of two selected particles' pbests through a tournament selection procedure and select the better one;
6: The winner's pbest is preserved to construct the set of promising pbests for a component;
7: Through PBIL, estimate the distribution of promising regions in the search space based on (5)-(8) and generate the historical memory by the estimated distribution;
8: For every particle, generate three new candidate positions $\operatorname{Pos}_{i_1}, \operatorname{Pos}_{i_2}$, and $\operatorname{Pos}_{i_3}$ via the information pool $I$;
9: Evaluate the fitness function values of the three new candidate positions and select the best one as the current particle $X_{i}$;
10: until The end condition is satisfied.
11: end
12) It defines a new particle generation mechanism. The idea behind it is to generate a new particle through the competition among those generated based on historical memory, particles' current pbests, and the swarm's gbest.

## IV. EXPERIMENTAL EVALUATION

Extensive simulations are carried out in order to compare HMPSO with CPSO-H6 [3], CLPSO [6], ALCPSO [7], FIPS [4], HPSO-TVAC [5], EDA-PSO [14], and PSEDA [15]. Further experimental evaluations with two HMPSO variants are then carried out to analyze and compare the performance of proposed HMPSO when it uses two different ways to build historical memory. All the mentioned algorithms are coded in MATLAB-R2010a and simulations are executed on a 2.4 GHz Xeon E5-2665 processor with 32 GB main memory running under Windows server 2008 environment.

## A. Benchmark Functions and Algorithm Configuration

In order to study their performance deeply, 28 benchmark functions in CEC2013 [42] are used for the experimental tests here, which have been widely used for real-parameter optimization, as shown in Table I. The dimension D is set to 50. A relatively universal evaluation method is used to test the average and standard deviation of the function value error, which is defined as $f(\vec{x})-f\left(\overrightarrow{x^{2}}\right)$, where $\vec{x}$ is the best solution found by the algorithm in a test instance and $\overrightarrow{x^{2}}$ is the global optimum of the benchmark function. All results of the algorithms are obtained from 51 independent runs. In addition, we assume that the termination criterion of all algorithms is

TABLE I
28 CEC2013 Benchmark Functions, Search Range: $[-100,100)^{D}$


TABLE II
PSO Algorithms Used in the COMPARISON

a fixed number of function evaluations, which is set to be 500000 . The population size in all algorithms is 40 .

The parameter configurations for the seven existing PSO algorithms that compare with HMPSO are given in Table II, according to their corresponding references.

In HMPSO, the value of $\omega$ is decreased linearly from 0.9 to 0.4 for all benchmark functions [3], [5], [6], $N=40$ and $c=1.49445$. Besides, it has its own unique parameters. $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$ are the learning parameters of mean and standard deviation, respectively, in EDA. Their ranges are $[0,1]$. " 0 " means that all new offspring will be sampled based on historical memory, while " 1 " means that all new offspring will be sampled based on the distribution of current particles' pbests. In this paper, we set the values of $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$ to be same. The first reason for doing so is to try to simplify the parameter settings since there exists too many of their combinations. The second reason is that the performance of HMPSO is relatively better when $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$ are set to be equal through a great number of tests. Next, in our preliminary experiments, we focus only on finding the most suitable parameters for them. The results in Fig. 2 illustrate the influences of different $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$ on some functions F2, F7, F8, F14, F22, and F27. Their increment is 0.1 . Each plot in Fig. 2 contains multiple boxplots. Each boxplot corresponding to a particular value of $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$ uses the minimum, first quartile, median, third quartile, and maximum values of a set of experimental data to describe statistics intuitively. Its function is primarily to identify the exceptional value, to estimate the skewness and tail weight of data distribution, to compare the distribution shape characteristics and the dispersion degree

![img-1.jpeg](img-1.jpeg)

Fig. 2. Influences of different $m_{\lambda}$ and $\operatorname{Var}_{\lambda}$ on HMPSO performance, which range from 0 to 1 on functions (a) F2, (b) F7, (c) F8, (d) F14, (e) F22, and (f) F27.

TABLE III
Experimental Results of CPSO-H6, CLPSO, ALCPSO, FIPS, HPSO-TVAC, EDA-PSO, PSEDA, and HMPSO Over 51 Independent Runs on 28 Functions. "Mean $E$ " and "Std $D$ " indicate the Mean and Standard Deviation of the Function Value Errors. " $=$," " $>$," and " $\circ$ " Denote That the Performance of the Corresponding Algorithm is Worse Than, Better Than, and Similar to That of HMPSO

of different grouped experimental data, etc. It seems that the setting of $m_{\lambda}=\operatorname{Var}_{\lambda}=0.5$ is more appropriate and robust than other parameters. Hence, 0.5 is adopted for all further experiments in this paper.

## B. Comparison With Seven PSO Algorithms

The experimental results are given in Table III, which show the mean and standard deviation of 28 benchmark functions. Each is obtained from 51 independent runs. The last three rows of Table III summarize the experimental results. The best results obtained by eight algorithms are shown in bold.

1) Functions F1-F5 are unimodal functions. Clearly, HMPSO is overall the best algorithm among
these methods. It outperforms other seven algorithms on all five benchmark functions. The outstanding performance of HMPSO should be due to the use of the swarm's global gbest and particles' historical promising pbests that provide a promising search area, which leads to a very fast and precise convergence.
2) F6-F20 are basic multimodal functions. HMPSO is significantly better than the others on nine rotated functions, i.e., F6, F7, F9, F10, F12, F13, F15, F19, and F20. All algorithms have same performance on rotated Ackley's function F8, which is a nonseparable and asymmetrical function where the plains are vast and its global optimum is difficult to locate. Specially, HMPSO outperforms EDA-PSO and PSEDA on fourteen

![img-2.jpeg](img-2.jpeg)

Fig. 3. Evolution of the base 2 logarithm of the mean of function value errors derived from all algorithms over 51 independent runs on functions (a)-(p) F1-F16.
functions except F8. It achieves the best results on most rotated multimodal functions. This implies that it is more effective in solving functions with more linkage due to its historical memory of particles' promising pbests that are selected by a tournament procedure, which pays attention to the relationship among different components to some extent by the competition of the fitness values that are calculated by considering all components of different particles' pbests. CPSO-H6, CLPSO, ALCPSO, and HPSO-TVAC outperform HMPSO on F11, F14, and F17. CPSO-H6 is the best. Rastrigin's function F11 is a multimodal, asymmetrical function and owns a huge number of local optima. Schwefel's function F14 is a multimodal function in which local optima count is huge. Lunacek bi-Rastrigin function F17 is a nonseparable multimodal. CPSO-H6 performs well on the three unrotated functions since it can utilize its cooperative mechanism by decomposing a larger search space into several smaller ones, which ensures that the search space is sampled more thoroughly when the number of local optima is huge. On Rotated Katsuura function F16, CPSO-H6, CLPSO, ALCPSO, and HPSO-TVAC outperform HMPSO. CLPSO is the winner since it can successfully avoid falling into the deep local optimum
which is far from the global optimum. FIPS, CLPSO, and ALCPSO outperform HMPSO on Rotated Lunacek bi-Rastrigin function F18 that is a nonseparable multimodal function, and FIPS is the winner by using the information of the entire neighborhood to guide the particles. To sum up, HMPSO is ranked first in all algorithms since it wins nine rotated functions.
3) Finally, F21-F28 are composition functions. Composition functions are constructed based on some basic benchmark functions to obtain more challenging problems with a randomly located global optimum and several randomly located deep local optima. They are much harder than the others. Overall, the performance of HMPSO is better than its seven competitors. It outperforms them on four rotated functions F23-F25 and F27. HMPSO outperforms CPSO-H6 on six functions except F21 and F22. CLPSO outperforms HMPSO on F21, F22, F26, and F28 since the former is good at complex multimodal problems irrespective of whether they are unrotated or rotated. ALCPSO and FIPS are better than HMPSO on F21 only. HPSO-TVAC is better than HMPSO on F22 only. Besides, HMPSO outperforms EDA-PSO and PSEDA on all the eight functions.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Evolution of the base 2 logarithm of the mean of function value errors derived from all algorithms over 51 independent runs on functions (a)-(l) F17-F28.

The evolution of the base 2 logarithm of the mean of function value errors derived from the eight algorithms over 51 independent runs on 28 benchmark functions are shown in Figs. 3 and 4. Comparing their results and convergence, it is easy to observe the performance advantage of HMPSO over its competitors. The last three rows in Table III indicate that the numbers of functions for which HMPSO are better than CPSO-H6, CLPSO, ALCPSO, FIPS, HPSO-TVAC, EDA-PSO, and PSEDA are 21, 18, 21, 25, 22, 27, and 27, respectively. The numbers of functions for which they are similar to 1 . Among these eight PSO algorithms, CPSO-H6 presents the best performance on some unrotated multimodal functions. However, its performance is seriously affected after rotation. CLPSO presents the best performance on some multimodal and composition functions irrespective of whether they are unrotated or rotated. However, it does not perform well when the functions are unimodal or simple multimodal. ALCPSO and FIPS present excellent performance on some rotated multimodal functions. However, their performance on unimodal functions is similar to CLPSO, and they do not perform well on composition functions. HPSO-TVAC presents excellent performance on some unimodal and unrotated multimodal functions. However, its performance is not good on rotated multimodal functions and composition ones. EDA-PSO and PSEDA present excellent performance on some rotated multimodal functions. However, they are inferior to other PSO algorithms. HMPSO achieves the best results on all unimodal functions, and a key reason is that it uses the information of swarm's global gbest and particles' historical promising pbests that provide a promising search area from its information pool. Moreover, HMPSO presents excellent performance on most rotated multimodal and composition
functions. This implies that the HMPSO is effective in solving functions with more linkage. This property is due to the historical memory in HMPSO that preserves the correlation information among the components to a certain extent. In addition, facing composition functions, HMPSO is more competitive than CLPSO.

## C. Comparison With HMPSO Variants

In this section, two HMPSO variants with novel mechanisms to build historical memory are proposed. In HMPSO, the historical memory is represented as a single global distribution model that is built by those selected promising particles' pbests. It can thus be viewed as the memory of overall population. In the first variant, we utilize the historical pbests of a particle to build a local distribution model for that particle, and this local distribution model is represented as the historical memory of a particle. Each particle in population generates an offspring through its local historical memory. This variant is called HMPSO-L.

Next, in HMPSO, we assume that each component follows a normal distribution. A single global distribution model is built without considering the relationship among different components deeply. In the second variant, we utilize a multivariate Gaussian distribution to represent different components' relationship and assume the whole population to follow a normal distribution. Then all components of a particle can be generated simultaneously. This variant is called HMPSO-M. Its historical memory can also be viewed as the memory of overall population.

The experimental results over 51 independent runs on 28 benchmark functions among HMPSO-L, HMPSO-M,

TABLE IV
EXPERIMENTAL RESULTS OF HMPSO-L, HMPSO-M, AND HMPSO
OVER 51 INDEPENDENT RUNS ON 28 BENCHMARK FUNCTIONS

and HMPSO are shown in Table IV, where "Mean $E$ " and "Std $D$ " indicate the mean and standard deviation of the function value errors, respectively. " $<,"$ " $>," and " $\doteqdot$ " denote that the performance of the corresponding algorithm is worse than, better than, and similar to that of HMPSO, respectively. The last three rows of Table IV summarize the experimental results. The best results among the three algorithms are shown in bold.

1) Functions F1-F5 are unimodal functions. Clearly, HMPSO is overall the best. It outperforms the other two on all five benchmark functions. These results indicate that the historical memory built by assuming the distribution of each component follows a normal distribution in HMPSO outperforms the other two mechanisms on unimodal functions.
2) F6-F20 are basic multimodal functions. HMPSO is significantly better than HMPSO-L and HMPSO-M on ten rotated functions, i.e., F6, F7, F9, F12, F13, F15-F17, F19, and F20. All algorithms have same performance on F8. HMPSO achieves the best results on most rotated multimodal functions. HMPSO-L outperforms HMPSO-M and HMPSO on F10, F14, and F18. This implies that the history memory built by a local distribution model for that particle has good ability to solve these unrotated and rotated functions. HMPSO-M outperforms HMPSO on four functions F10, F11, F14, and F18. Especially, on function F11, HMPSO-M is
the best. This implies that the historical memory built by a multivariate Gaussian distribution by assuming the whole population to follow a normal distribution is more competitive than HMPSO-L and HMPSO on these unrotated and rotated functions.
3) Finally, F21-F28 are composition functions. Overall, HMPSO ranks the first. It outperforms the other two on six functions F23-F28. HMPSO-L and HMPSO-M outperform HMPSO on functions F21 and F22. HMPSO-L is the best on these two functions.
The last three rows in Table IV indicate that the numbers of functions for which HMPSO is better than HMPSO-L and HMPSO-M are 22 and 21, respectively. The numbers of functions for which they are similar to 1 . It is clear from the results that with the historical memory that built by assuming the distribution of each component to follow a normal distribution, HMPSO presents the best performance on all unimodal functions, and majority of rotated multimodal and composition functions. HMPSO-L presents excellent performance on some unrotated and rotated multimodal functions. HMPSO-M is more competitive than HMPSO-L and HMPSO on some unrotated and rotated functions. These results indicate that the performance of HMPSO has the potential to be improved with the help of integrating the historical memory built by a local distribution model for each particle or a multivariate Gaussian distribution.

## D. Analysis and Statistics of HMPSO

In order to supply a thorough comparison among all algorithms, a $t$-test [43] is carried out. Table V presents the $t$ - and $P$-value on every benchmark function of this two-tailed test with a significance level of 0.05 between HMPSO and other algorithms. It should be mentioned that when the $t$-value is negative, it means that HMPSO outperforms the corresponding algorithm in terms of both mean and standard deviation; and vice versa. A $P$-value represents the estimated probability of getting the observed or more extreme results, assuming that the null hypothesis is true. It is a measure of how much evidence we have against the null hypothesis. If the $P$-value is less than 0.05 or 0.01 , one often rejects the null hypothesis and declares the result to be statistically significant. If the $P$-value is near zero, it suggests that at least one sample median is significantly different from the others. Row "General Merit" represents the number of benchmark functions that HMPSO performs significantly better than other algorithms based on the $t$ - and $P$-value.

From Table V, it can be seen that $21 t$ values are negative on functions F1-F7, F9, F10, F12, F13, F15, F18-F20, and F23-F28 in CPSO-H6, $19 t$ values are negative on functions F1-F10, F12, F13, F15, F19, F20, F23-F25, and F27 in CLPSO, $21 t$ values are negative on functions F1-F7, F9, F10, F12, F13, F15, F19, F20, and F22-F28 in ALCPSO, $25 t$ values are negative on functions F1-F7, F9-F17, F19, F20, and F22-F28 in FIPS, $23 t$ values are negative on functions F1-F10, F12, F13, F15, F18-F21, and F23-F28 in HPSO-TVAC, $27 t$ values are negative on functions F1-F7 and F9-F28 in EDA-PSO, $28 t$ values are negative on

TABLE V
COMPARISONS BETWEEN HMPSOI AND OTHER ALGORITHMS ON $t$-TESTS

functions F1-F28 in PSEDA, 23 $t$ values are negative on functions F1-F9, F11-F13, F15-F17, F19, F20, and F23-F28 in HMPSO-L, and 22 $t$ values are negative on functions F1-F9, F12, F13, F15-F17, F19, F20, and F23-F28 in HMPSO-M. In brief, HMPSO outperforms its competitors on these benchmark functions.

Among all the obtained $P$ values, 25 P values are much smaller than the 0.01 on functions F1-F5, F7, F9-F20, and F22-F28 in CPSO-H6, 24 P values are much smaller than the 0.01 on functions F2-F7, F9-F18, and F20-F27 in CLPSO, 23 P values are much smaller than the 0.01 on functions F2-F7, F9-F15, F17-F20, and F23-F28 in ALCPSO, 19 P values are much smaller than the 0.01 on functions F1, F2, F4, F5, F7, F9-F15, F18-F20, F22-F24, and F28 in FIPS, 25 P values are much smaller than the 0.01 on functions F1-F7, F9-F20, F22-F25, F27, and F28 in HPSO-TVAC, 26 P values are much smaller than the 0.01 on functions F1-F7, F9-F15, and F17-F28 in EDA-PSO, 26 P values are much smaller than the 0.01 on functions F1-F7, F9-F15, and F17-F28 in PSEDA, 17 P values are much smaller than the 0.01 on functions

F1-F3, F5, F7, F9, F12, F13, F15, F18-F20, F22-F25, and F27 in HMPSO-L, and 15 P values are much smaller than the 0.01 on functions F1, F2, F4, F5, F7, F9, F12, F15, F18-F20, F22, F24, F25, and F27 in HMPSO-M. In brief, the experimental results obtained via HMPSO and other algorithms are statistically significant.

It seems that a two-tailed $t$-test in Table V is appropriate. However, there is no mention about the fact that data are normally distributed or not. In order to ensure the correctness of the experimental results, we simultaneously adopt another nonparametric test method, i.e., Wilcoxon's rank sum test. Such test on every benchmark function at a 0.05 significance level between HMPSO and other algorithms $P$ values as shown in Table VI. Twenty-seven $P$ values are much smaller than 0.05 on functions F1-F20 and F22-F28 in CPSO-H6, so are 25 P values on functions F2-F7, F9-F18, and F20-F28 in CLPSO, 27 P values on F1-F7 and F9-F28 in ALCPSO, 24 P values on F1, F2, F4-F7, F9-F15, F17-F26, and F28 in FIPS, 27 P values on F1-F7 and F9-F28 in HPSO-TVAC, 27 P values on F1-F7 and F9-F28 in EDA-PSO, 26 P values

TABLE VI
Comparisons Between HMPSO and Other Algorithms on Wilcoxon's Rank Sum Test at a 0.05 Significance Level

![img-4.jpeg](img-4.jpeg)

Fig. 5. Evolution of a selected best index in HMPSO on functions (a) F1, (b) F3, (c) F7, (d) F8, (e) F11, (f) F13, (g) F16, (h) F18, (i)-(k) F21-F23, and (l) F26.
on F1-F7, F9-F15, and F17-F28 in PSEDA, 23 P values on F1-F3, F5-F7, F9, F12-F15, and F17-F28 in HMPSO-L, and 22 P values on F1, F2, F4-F7, F9, F12, F14-F22, and F24-F28 in HMPSO-M. They suggest that the experimental results obtained via HMPSO and other algorithms are statistically significant.

In order to show the evolution of a selected best index in HMPSO clearly, we present the evolution curves on some functions, as described in Fig. 5. " 1 " denotes that the current best index is derived from the historical memory. " 2 " denotes that the current best index is derived from other particles'
pbests as same as CLPSO. " 3 " denotes that the current best index is derived from the swarm's global gbest.

It is clear from Fig. 5 that with historical memory, HMPSO can pursue good solutions continuously through the interaction of three kinds of information, i.e., historical memory, particles' current pbests, and the swarm's gbest. The historical memory retains particles' historical promising pbests information, which can be reused so as to improve the search process. The historical memory can help the particles return to those optimum-likely regions that they have searched while keeping high population diversity.

## V. CONCLUSION

In this paper, a new PSO algorithm is proposed, called HMPSO, which uses EDA to estimate and preserve the distribution information of particles' historical promising pbests. New particles are generated by the competition among those generated based on historical memory, particles' current pbests, and the swarm's gbest from an information pool. The three kinds of information have the distinct advantages and therefore they can complement one another. The structure of HMPSO is simple and it is easy to implement. Moreover, under our framework, the users can easily build their own information pool for solving different problems.

The significance of HMPSO mainly lies in two aspects. First, memory is an essential feature of all living systems, From the evolutionism point of view, it is worthwhile examining if historical memory is helpful to the process of evolution algorithms. In this paper, we make the first attempt on this topic to propose an HMPSO algorithm and show that historical memory built by particles' historical promising pbests is helpful to PSO. Second, the proposed HMPSO manages to prevent premature convergence and keeps the fastconverging feature via the competition among three kinds of information.

As shown in the experiments on 28 CEC2013 benchmark functions, HMPSO achieves the best results on all unimodal functions, and a key reason is that it uses the information of swarm's global gbest and particles' historical promising pbests that determine a promising search area. In addition, although HMPSO uses the information of the swarm's gbest, it presents excellent performance on most rotated multimodal functions and composition functions. This property indicates that HMPSO owns the abilities to effectively prevent premature convergence by particles' current pbests and historical memory. Next, two HMPSO variants with novel mechanisms to build historical memory are presented. One uses the historical pbests of a particle to build a local distribution model for that particle, while the other uses a multivariate Gaussian distribution to represent different components' relationship and takes it as the whole historical memory. The results indicate that the performance of HMPSO may be promoted through the help of these two mechanisms.

In the future, we first plan to design a coordination mechanism to integrate historical memory built by a local distribution model for each particle or a multivariate Gaussian distribution effectively. Secondly, we plan to assess the performance of HMPSO when applied to other optimization functions and industrial optimization problems, e.g., multiobjective evolutionary optimization [25] and optimal power flow problem [12]. Its use to solve some discrete optimization problems should be pursued [44]-[47].
