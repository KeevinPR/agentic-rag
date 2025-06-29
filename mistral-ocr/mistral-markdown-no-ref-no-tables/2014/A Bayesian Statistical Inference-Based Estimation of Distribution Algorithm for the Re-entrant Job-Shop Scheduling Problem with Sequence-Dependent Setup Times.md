# A Bayesian Statistical Inference-Based Estimation of Distribution Algorithm for the Re-entrant Job-Shop Scheduling Problem with Sequence-Dependent Setup Times 

Shao-Feng Chen ${ }^{1,2}$, Bin Qian ${ }^{1,2, *}$, Bo Liu ${ }^{3}$, Rong $\mathrm{Hu}^{1,2}$, and Chang-Sheng Zhang ${ }^{1}$<br>${ }^{1}$ Department of Automation, Kunming University of Science and Technology, Kunming 650500, China<br>${ }^{2}$ Key Laboratory of Computer Technologies Application of Yunnan Province, Kunming 650500, China<br>${ }^{3}$ Academy of Mathematics and Systems Science Chinese Academy of Sciences, Beijing 100190, China<br>bin.qian@vip.163.com


#### Abstract

In this paper, a bayesian statistical inference-based estimation of distribution algorithm (BEDA) is proposed for the re-entrant job-shop scheduling problem with sequence-dependent setup times (RJSSPST) to minimize the maximum completion time (i.e., makespan), which is a typical NP hard combinatorial problem with strong engineering background. Bayesian statistical inference (BSI) is utilized to extract sub-sequence information from high quality individuals of the current population and determine the parameters of BEDA's probabilistic model (BEDA_PM). In the proposed BEDA, BEDA_PM is used to generate new population and guide the search to find promising sequences or regions in the solution space. Simulation experiments and comparisons demonstrate the effectiveness of the proposed BEDA.


Keywords: bayesian statistical inference, estimation of distribution algorithm, re-entrant job-shop scheduling problem, setup times.

## 1 Introduction

This paper presents a meta-heuristic for the re-entrant job-shop scheduling problem with sequence-dependent setup times (RJSSPST). The criterion is to minimize the maximum completion time (i.e., makespan). The RJSSPST is a general job-shop scheduling problem characterized by re-entrant work flows and sequence-dependent setup times. This problem extends the classical job-shop scheduling problem (JSSP) by allowing for sequence-dependent setup times between adjacent operations on any machine and relaxing the restriction that each job visits a machine only once. The JSSP is well-known to be NP-complete [1]. From the point of view of computational complexity, the JSSP obviously reduces to the RJSSPST, which means the RJSSPST is also NP-complete. Moreover, the RJSSPST is commonly encountered in today's

[^0]
[^0]:    * Corresponding author.

manufacturing environment. Thus, it is meaningful and practical to make the work of developing effective scheduling algorithms for the considered problem.

Although the RJSSPST appears frequently in commercial printing, plastic manufacturing, metal processing, cylinder-head manufacturing, side frame press shop, and semiconductor manufacturing, but mainly because of its complexity, it has received little attention from researchers. Recently, Sun [2] proposed a genetic algorithm (GA), a modified version of the nearest-setup heuristic [3], and a modified version of the shifting-bottleneck heuristic [4] to solve the RJSSPST. The test results show that GA performs better than the other algorithms.

In recent years, a novel probabilistic-model based evolutionary algorithm, i.e., the estimation of distribution algorithm (EDA), was first introduced by Baluja [5] for addressing the traveling salesman problem and the JSSP. EDA adopts a bran-new evolution scheme to drive the evolution process, which has no traditional crossover and mutation operations in the algorithm. The evolution process of EDA can be regarded as a process of competitive learning, and its probabilistic model is updated by the better solutions at each generation to accumulate the information of excellent individuals. Due to its simple framework and outstanding global exploration ability, EDA has attracted much attention and has been used to solve some production scheduling problems. Salhi et al. [6] presented an EDA for the complex flow shop scheduling problem. Wang et al. [7] designed an EDA to deal with the flexible JSSP. Liu et al. [8] used a combination of particle swarm optimization with EDA for the permutation flowshop scheduling problem. Wang et al. [9] developed a bi-population based EDA for the flexible JSSP. Zhou et al. [10] applied a decomposition-based EDA for the multiobjective traveling salesman problems.

However, there are some shortcomings in the current EDA's model. As shown in Ruiz et al. [11], there are many similar blocks of jobs within the individuals' sequences in the latter stages of evolutionary methods. These similar blocks may occupy the same positions or different positions. If these blocks are disrupted, the algorithm has a high probabilistic to produce offspring with worse makespan values. In this paper, a bayesian statistical inference-based estimation of distribution algorithm (BEDA) is proposed. The purpose of bayesian statistical inference (BSI) is to describe the condition probabilistic of each decision variable [12]. And the new model of conditional probabilistic is built based on the frequencies of sub-sequences or neighbor operations in the high quality individuals. By combining the BSI with the EDA, the proposed BEDA can overcome the shortcomings in the current EDA's model to some extent.

The rest of this paper is arranged as follows. In section 2, the RJSSPST is briefly introduced. In section 3, the BEDA is proposed and described in details. In section 4, computational results and comparisons are provided. Finally, we end the paper with some conclusions and future work in section 5.

# 2 RJSSPST 

### 2.1 Mathematical Model of RJSSPST

The following describes the mathematical model for the RJSSPST. For the purpose of simplification, in the following model, each operation of each job is denoted by a unique notation.

$i, j \quad$ Notations used for operations
$B \quad$ a large enough positive number
$D \quad$ The set of operations in the shop floor
$M \quad$ The set of machines available in the shop floor
$L \quad$ The repeat or reentrant times
$M_{j} \quad$ The specific machine that operation $j$ requires according to its process route
$t_{j} \quad$ Standard processing time of operation $j$
$C_{j} \quad$ Completion time of operation $j$
$\mathrm{F}_{j} \quad$ the start time of operation $j$
$R_{k} \quad$ The dummy operation that describes the first activity in machine $k$
$S_{i j} \quad$ The setup time between operation $i$ and operation $j$ if operation $i$ performs just before operation $j$
$x_{i j k} \quad$ The indicator variable
With the above notations, the RJSSPST can be formulated as a mixed integer programming problem as follows. Let

$$
x_{i j k}=\left\{\begin{array}{l}
1, \text { if operation } j \text { is just after operation } i \text { in the machine } k \\
0, \text { otherwise }
\end{array}\right.
$$

Then,
Min makespan $=\max \left(C_{i}=F_{i}+t_{i}\right) \quad i \in D$
s.t.
$\sum_{i \in D} x_{i j k}=L$
$\sum_{j \in D} x_{i j k}=L$
$F_{i}+t_{i}+S_{i j} \leq F_{j}+B\left(1-X_{i j k}\right)$
$F_{i}+t_{i} \leq F_{j}$
$i, j \in S_{i j}$
$t_{R_{k}}=0$
$k \in M$
$S_{R_{k} i}=0, S_{i R_{k}}=0$,
$i \in D,\left(i, k \mid k=M_{i}\right)$

Equation 1 presents the objective function, which aims to reduce the cycle time of all jobs called makespan. Constraint 2 and constraint 3 force the job scheduling to have a available sequence in a schedule sequence of each machine. Constraint 4 requires that the start time of each operation in one machine should be larger than the completion time of the operation that performs just before this operation considering the setup times between the pervious operation and current operation. Constraint 5 ensures that an operation could not start until its preceding operation is done. In constraint 6 and constraint 7, processing time and the relationship of setup times between dummy operations and other operations, which require the same machine, are set to zero. The existence of variable $F_{i}$ in the mathematical model eliminates the subtours in the solutions. It should be noted that the operation, which starts in the next location after dummy operation of a machine, is the starting point of sequence and consequently no setup is required to perform this operation.

# 2.2 Statement of RJSSPST 

The above mathematical model is only used to depict the characteristics of RJSSPST. The following statement is utilized to code and decode each sequence or individual in the proposed BEDA. The RJSSPST has the following usual assumptions. There are $m$ machines, $n$ jobs and $L$ times re-entrant in the production system. The problem size can be denoted by $n \times m \times L$. Each job consists of a set of operations that have to be processed in a specified sequence. Each operation has to be processed on a definite machine and has a processing time and a setup time which are deterministically known. Moreover, each job should be processed on each machine $L$ times and the setup times of operations on each machine are sequence dependent. Once an operation is started, it must be completed without any interruption. At any time, each machine can process at most one job.

Denote $\pi=\left[\pi_{1}, \pi_{2}, \ldots, \pi_{\text {seven } L}\right]$ the sequence or schedule of operations to be processed. The RJSSPST with the makespan criterion is to find a schedule $\pi^{*}$ in the set of all schedules $\Pi$ such that

$$
\pi^{*}=\arg \left(C_{\max }\right) \rightarrow \min , \quad \forall \pi \in \Pi
$$

## 3 BEDA for RJSSPST

In this section, we will present BEDA after explaining the solution representation, decoding scheme, population initialization, probabilistic model and updating mechanism, new population generation method and new probabilistic model construction strategy.

### 3.1 Solution Representation

Based on the properties of RJSSPST, we adopt the operation-based solution representation, that is, every individual of the population is a feasible solution of the

RJSSPST, for example, $\left[\pi_{1}, \pi_{2}, \ldots, \pi_{3 \times 2 \times 2}\right]=[1,2,1,3,2,1,3,3,1,2,3,2]$ is an individual when the problem's scale $n \times m \times L$ is set to $3 \times 2 \times 2$.

# 3.2 Decoding Scheme 

Due to the constraints of RJSSPST, we can improve the solution to minimize the makespan criterion by converting the semi-active schedule to the active one. Thus, when decoding we check the possible idle interval before appending an operation at the last position, and fill the first idle interval before the last operation (called active decoding). The details of active decoding scheme used in this paper are very similar to that used in [13]. The difference between the two schemes only lies in the treatment of the setup times. In [13], the setup times of each operation are not considered.

### 3.3 Population Initialization

In order to search different regions in the huge solution space, we need to ensure that the initial individuals have widely distributed in the space. Therefore, BEDA adopts stochastic method to generate the initial population.

### 3.4 Probabilistic Model and Its Updating Mechanism

### 3.4.1 Probabilistic Model

A bayesian network in [14] is used as the probabilistic model of BEDA, whose structure (including nodes and directed arcs in the network) is partially predetermined. This probabilistic model can describe the probabilistic distribution of favorable values based on the high quality individuals in population. The operations in each high quality individual can be represented by a directed acyclic network as shown in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. The structure of bayesian network

The directed arc from node $N_{\alpha, \beta}$ to node $N_{\alpha+1, \beta^{\prime}}(\beta^{\prime} \in 1, \ldots, n)$ represents the dependent relationship between the two nodes, which records the sub-sequence information of the high quality individuals.

# 3.4.2 Updating Mechanism 

The probabilistic model is a most important part for the BEDA, because it is built for guiding generation new population. Building or updating the probabilistic model is equivalent to determining the bayesian network's parameters (i.e., the weights of directed arcs) according to the high quality individuals. After that, each individual of the next generation can be produced by iteratively sampling the probabilistic model from the first layer (i.e., $N_{1, \beta}$ ) to the last layer (i.e., $N_{n \times m \times L, \beta}$ ), which is useful for obtaining promising offspring.
![img-1.jpeg](img-1.jpeg)

Fig. 2. A example network
The weights of directed arcs can be obtained simply by calculating the frequencies of sub-sequences or neighbor operations in the high quality individuals. Here we provide a concrete example to illustrate the calculation process in Fig. 2. In this example, $n \times m \times L$ is set to $2 \times 2 \times 1$, the high quality individuals are set as $\pi_{1}^{\text {high_quality }}=[1,2,1,2], \quad \pi_{2}^{\text {high quality }}=[1,2,1,2], \quad \pi_{3}^{\text {high quality }}=[1,2,2,1], \pi_{4}^{\text {high quality }}=[2$, $1,2,1], \pi_{5}^{\text {high quality }}=[1,1,2,2], \pi_{6}^{\text {high quality }}=[2,2,1,1]$. Then, the weight of each directed arc (i.e., the number placed on the arc) can be updated.

By using the weights of directed arcs as approximation probabilities, the conditional probabilities of all the near nodes can be calculated as follows:

$$
\begin{aligned}
& P\left(N_{1,1}\right)=(1+3) / 6, P\left(N_{1,2}\right)=(1+1) / 6 \\
& P\left(N_{2,1} \mid N_{1,1}\right)=1 /(1+3), P\left(N_{2,2} \mid N_{1,1}\right)=3 /(1+3) \\
& P\left(N_{2,1} \mid N_{1,2}\right)=1 /(1+1), P\left(N_{2,2} \mid N_{1,2}\right)=1 /(1+1) \\
& P\left(N_{3,1} \mid N_{2,1}\right)=0 /(0+2), P\left(N_{3,2} \mid N_{2,1}\right)=2 /(0+2) \\
& P\left(N_{3,1} \mid N_{2,2}\right)=3 /(3+1), P\left(N_{3,2} \mid N_{2,2}\right)=1 /(3+1) \\
& P\left(N_{4,1} \mid N_{3,1}\right)=1 /(1+2), P\left(N_{4,2} \mid N_{3,1}\right)=2 /(1+2) \\
& P\left(N_{4,1} \mid N_{3,2}\right)=2 /(2+1), P\left(N_{4,2} \mid N_{3,2}\right)=1 /(2+1)
\end{aligned}
$$

Obviously, if a weight of directed arc is equal to 0 , it should be deleted from the bayesian network. This means a corresponding sub-sequence (i.e., two successive operations connected by this arc) can never be obtained in the iterative sampling process. For the purpose of keeping the diversity and dispersivity of the population to some extent, we replace each number 0 on the arc to 1 . Therefore, the above conditional probabilities with number 0 on the arc should be changed as follows:

$$
P\left(N_{3,1} \mid N_{2,1}\right)=1 /(1+2), P\left(N_{3,2} \mid N_{2,1}\right)=2 /(1+2)
$$

# 3.5 New Population Generation Method 

In each generation of the algorithm, the new individuals are generated by sampling the conditional probabilistic matrix mentioned in 3.4.2. Denote $P S$ the size of the population, $\pi_{j}(j \in\{1, \ldots, n \times m \times L\})$ the $j$ th operation in $\pi, \operatorname{pop}(g e n)$ the population at generation gen, $\pi^{\text {best }}$ (gen) the best individual of $\operatorname{pop}(g e n), \pi_{1}(\mathbf{g e n})=\left\{\pi_{i 1}(\right.$ gen $)$, $\pi_{i 2}(\text { gen }), \ldots, \pi_{i(n \times m \times L)}(\text { gen })\}$ the $i$ th individual in $\operatorname{pop}(g e n)$, and $\operatorname{Job}\left(\pi_{1}(\right.$ gen $), j)$ the function of selecting a job in the $j$ th position of $\pi_{1}(\mathbf{g e n})$ by using the conditional probabilistic matrix. Without loss of generality, we assume that $P\left(N_{1, \beta} \mid N_{0, \beta^{\prime}}\right)$ $=P\left(N_{1, \beta}\right) \quad\left(\beta, \beta^{\prime} \in 1, \ldots, n\right)$. The procedure of $\operatorname{Job}\left(\pi_{1}(\right.$ gen $), j)$ is described as follows:

Step 1: Set $\alpha=j, \beta^{\prime}=\pi_{i(j-1)}(\text { gen })$
Step 2: Randomly create a probabilistic $r$ where $r \sim[0,1)$.
Step 3: Get a candidate job $C J$ by the roulette-wheel selection scheme.
Step 3.1: If $r \sim\left[0, P\left(N_{\alpha, 1} \mid N_{\alpha-1, \beta^{\prime}}\right)\right.$, then set $C J=1$ and go to Step 4.
Step 3.2: If $r \sim\left\{\sum_{\beta=1}^{w-1} P\left(N_{\alpha, \beta} \mid N_{\alpha-1, \beta^{\prime}}\right), \sum_{\beta=1}^{w} P\left(N_{\alpha, \beta} \mid N_{\alpha-1, \beta^{\prime}}\right)\right\} \quad$ and $\quad w \in\{2$, $\cdots, n\}$, then set $C J=w$ and go to Step 4.
Step 4: Return $C J$.

Let $l\left(C J, \pi_{i}(\operatorname{gen}+1)\right)$ denote the repeat times of $C J$ in $\pi_{i}(\operatorname{gen}+1)$. Then, the new population generation method is given as the following steps:

Step 1: Set $i=1$.
Step 2: Generate a new individual $\pi_{i}(\operatorname{gen}+1)$.
Step 2.1: Set $\pi_{i j}(\operatorname{gen}+1)=0$ for $j=1, \cdots, n \times m \times L$.
Step 2.2: Set $j=1$.
Step 2.3: $C J=\operatorname{Job}\left(\pi_{i}(\operatorname{gen}+1), j\right)$.
Step 2.4: If $l\left(C J, \pi_{i}(\operatorname{gen}+1)\right)=m \times L$, then go to Step 2.3.
Step 2.5: Set $\pi_{i j}(\operatorname{gen}+1)=C J$.
Step 2.6: Set $j=j+1$.
Step 2.7: If $j \leq n \times m \times L$, then go to Step 2.3.
Step 3: Set $i=i+1$.
Step 4: If $i \leq P S$, then go to Step 2.

# 3.6 New Probabilistic Model Construction Strategy 

Based on Schiavinotto and Stützle [15], the diameter of Insert is $n \times m \times L-1$, which is one of the shortest diameters. That is, using Insert at most $n \times m \times L-1$ times, one solution $\boldsymbol{\pi}$ can transit to any other solution $\boldsymbol{\pi}^{\prime}$. This means Insertion-based neighborhood can perform a more efficient and thorough search than the other kinds of neighborhoods with the same running time. So, we utilize the Insertion-based neighborhood to generate $(n \times m \times L-1)^{2}$ neighbors of $\pi^{\text {best }}(\mathbf{g e n})$. Then, the best $\mathrm{e} \%$ of the generated neighbors and $\operatorname{pop}(\mathrm{gen})$ (i.e., the high quality individuals) are selected to construct the probabilistic model of BEDA.

### 3.7 Procedure of BEDA

Based on the contents in the above subsections, we propose the procedure of BEDA as follows:

Step 0: Denote $\pi^{\text {E. best }}$ the global best individual and genMax the maximum generation.
Step 1: Initialization.
Step 1.1: Set gen $=0$.
Step 1.2: Generate the initial population $\operatorname{pop}(1)$ by using the method in subsection 3.3.
Step 2: Set gen $=$ gen +1 .
Step 3: Calculate the makespan of each individual in $\operatorname{pop}($ gen $)$.
Step 4: Construct new probabilistic model by using the strategy in subsection 3.6, and update $\pi^{\text {E.best }}$.

Step 5: Generate $\operatorname{pop}(g e n+1)$ by using the new population generation method in subsection 3.5 .
Step 6: If gen $<$ genMax, then go to Step2.
Step 7: Output $\pi^{\text {g_best }}$.
It can be seen from Steps 4 and 5 that the new generated individuals can aptly absorb the sub-sequences information of the high quality individuals during the evolution process and then guide the search to more promising regions. Thus, the algorithm is hopeful to obtain good results.

# 4 Simulation Result and Comparisons 

### 4.1 Experimental Design

In order to test the performance of the proposed BEDA, a set of instances under different scales is randomly generated. The $n \times m \times L$ combinations include $10 \times 10 \times 2$, $10 \times 10 \times 3,20 \times 10 \times 3$, and $30 \times 10 \times 3$. For each scale, we generate 5 groups of data. The processing time $t_{j}$ is generated from a uniform distribution [1,100] and the setup time $S_{i j}$ is generated from [1,20]. All algorithms are coded in Delphi 2010 and are executed on Mobile Intel Core 4 Duo 2.2 GHz processor with 8GB memory.

For each instance, each algorithm is run 20 times independently. Based on our previous experiments, the parameters of BEDA are set as follows: the population size $P S=100$, and the proportion of the high quality individuals $\mathrm{e} \%=20 \%$. The parameters of GA are set the same as those in [2].

### 4.2 Comparisons of GA, BEDA_V1 and BEDA

For the purpose of showing the effectiveness of BEDA, we compare BEDA with GA and BEDA_V1 (i.e., a variant of BEDA). The difference between BEDA and BEDA_V1 lies in the probabilistic model and updating mechanism. The BEDA_V1 uses the probabilistic model and updating mechanism proposed by Baluja [5]. The learning rate $\alpha$ of BEDA_V1 is set to 0.1 . The maximum generations of algorithms are set to 500 . The running time of the algorithms are decided only by the scale of problems. The simulation results are listed in Table 1, where BEST denotes the best makespan, AVG denotes the average makespan and WORST denotes the worst makespan.

From Table 1, it can be seen that BEDA performs much better than GA and BEDA_V1 with respecting to solution quality. The values of BEST, AVG and WORST obtained by BEDA are much better than those obtained by GA and BEDA_V1. Specifically speaking, for instances 1 to 20 , BEDA is better than GA and BEDA_V1 on all statistical indicators (i.e., BEST, AVG and WORST) except the WORST indicator of instances 09 and 12, and the BEST indicator of instance 18. So, it can be concluded that BEDA is an effective algorithm for the RJSSPST. Moreover, the test results also manifest a bayesian statistical inference-based probabilistic model is more suitable for guiding the search to the promising regions in the solution space of RJSSPST.

Table 1. Comparisons of BEST, WORS and AVG of GA, BEDA_V1 and BEDA
# 5 Conclusion and Future Work 

This paper proposed a bayesian statistical inference-based estimation of distribution algorithm (BEDA) to solve the re-entrant job-shop scheduling problem with sequence-dependent setup times (RJSSPST). In BEDA, the initial population was generated by using stochastic method, and the search in the solution space was executed through sampling and updating the probabilistic model of BEDA. Simulation results and comparisons based on a set of instances showed the effectiveness of the proposed BEDA. To the best of our knowledge, this is the first paper on the application of estimation of distribution algorithm (EDA) for the RJSSPST. Our future work is to develop some BEDA-based algorithms to deal with re-entrant no-wait job-shop scheduling problem.

Acknowledgments. This research was partially supported by National Science Foundation of China (No. 60904081, 71101139), 2012 Academic and Technical Leader Candidate Project for Young and Middle-Aged Persons of Yunnan Province (No. 2012HB011), and Discipline Construction Team Project of Kunming University of Science and Technology (No. 14078212).
