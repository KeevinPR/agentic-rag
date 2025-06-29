# Shared manufacturing-based distributed flexible job shop scheduling with supply-demand matching 

Guangyan Wei ${ }^{\text {a }}$, Chunming Ye ${ }^{\mathrm{a}, *}$, Jianning Xu ${ }^{\mathrm{b}}$<br>${ }^{a}$ Business School, University of Shanghai for Science and Technology, Shanghai 200093, China<br>${ }^{\mathrm{b}}$ School of Mechanical Engineering, University of Shanghai for Science and Technology, Shanghai 200093, China

## A R TICLE INFO

Keywords:
Shared manufacturing
Distributed flexible job shop scheduling
Estimation of distribution algorithm
Tabu search

A B STR A C T

Shared Manufacturing (sharedMfg) is a peer-to-peer (P2P) paradigm for sharing manufacturing resources, derived from the sharing economy. In sharedMfg, manufacturing service resources are integrated into a large set with defined service types. Based on its resource organization structure, we build a model for the shared manufacturing-based distributed flexible job shop scheduling problem (SM-DFJSP) with supply-demand matching. The goal is to minimize both the total cost and the makespan. The SM-DFJSP model enables the scheduling of jobs requiring different manufacturing services across distributed, heterogeneous, and flexible service resource units (SRUs) with diverse manufacturing functions. To solve the SM-DFJSP, we propose a hybrid estimation of distribution algorithm and Tabu search (EDA-TS), including EDA and TS components. Additionally, a multi-populations strategy and non-dominated solutions memory mechanism are designed to improve the exploration ability of the algorithm. Within the EDA component, three probability distribution models and some dispatching rules are designed to generate a new population. In the TS component, three neighborhood search structures are built that adopt hybrid short and long memory tabu strategy. Finally, comparison and ablation experiments on 25 instances demonstrate the superior performance of the EDA-TS algorithm in solving the SMDFJSP, highlighting the effectiveness of the multi-population strategy and non-dominated solutions memory mechanism.

## 1. Introduction

Influenced by economic globalization and the sharing economy, the manufacturing industry has embraced a novel paradigm known as shared manufacturing (sharedMfg) (Yu et al., 2020), aided by technologies such as cyber-physical systems, the Internet of Things, and digital twin technology (Yu et al., 2020; Wang et al., 2021). SharedMfg extends the global manufacturing service network to the individual level and increases the sociality of manufacturing (Rozman et al., 2021; Yu et al., 2020). Given the distributed and heterogeneous nature of production resources, research in scheduling must address distributed scheduling modeling and optimization (Zhang et al., 2019). In addition, flexible production is ubiquitous in modern manufacturing systems (Xiong and Fu, 2018). Thus, this paper aims to study the resource scheduling problem in distributed flexible manufacturing systems under the background of sharedMfg.

Currently, distributed flexible job shop scheduling (DFJSP) is garnering significant attention in academia (Chang and Liu, 2017).

However, existing studies have mainly focused on production aspect (Wang et al., 2002) and ignored distributed manufacturing service scheduling based on demand (Cheng et al., 2021). In the related works of cloud manufacturing, similar to sharedMfg, there is considerable emphasis on resource allocation (He and Qian, 2020; Xue and Wang, 2019; Huo et al., 2022) and service composition optimization (Liu et al., 2019; Liu et al., 2019). But these studies only address the matching of service resource units (SRUs) with manufacturing tasks, neglecting the scheduling within the SRUs. This is likely attributed to the organization of resources in cloud manufacturing, where dispersed manufacturing resources make supply-demand matching very complex. Considering scheduling problems within the SRUs would significantly increase the scale of the scheduling model.

Compared with cloud manufacturing and social manufacturing, resource integration in sharedMfg is represented as a large set with defined service types, as depicted in Fig. 1 (Yu et al., 2020). This integration combines the discreteness of cloud manufacturing resources (Liu et al., 2017) with the clustering of social manufacturing resources (Jiang

[^0]
[^0]:    a Corresponding author.
    E-mail addresses: wei_g_y@126.com (G. Wei), yechm6464@163.com (C. Ye), 212171574@st.usst.edu.cn (J. Xu).

![img-0.jpeg](img-0.jpeg)

Fig. 1. Different ways of resources organization of Cloud, Social, and Shared manufacturing.
and Ding, 2018). The resource organization structure of sharedMfg allows us to abstractly represent supply-demand types. Subsequently, completing the matching becomes straightforward, and it can be seamlessly integrated with distributed scheduling to accomplish sup-ply-demand matching based distributed manufacturing resource scheduling. Building upon this, we construct a model for sharedMfg distributed flexible job shop scheduling problems (SM-DFJSP) with supply-demand matching.

Like other shop scheduling problems, SM-DFJSP also is an NP-hard problem. Up to now, heuristic algorithms have been applied to solve such problems (Turkylimaz et al., 2020). Such as the genetic algorithm (GA) (Zheng et al., 2021; Wu et al., 2021); particle swarm optimization algorithm (Tang et al., 2016; Nouiri et al., 2018), differential evolution algorithm (Li et al., 2022), etc. Compared with the other evolutionary algorithms, the estimation of distribution algorithm (EDA) extracts the distribution information from the population, enhancing the effectiveness of the search (Martins and Delbem, 2016; Fang et al., 2018). However, EDA also has the disadvantages such as weak local search ability and premature convergence. Therefore, some researches combine EDA with local search algorithms to solve scheduling problems (Hao et al., 2017; Du et al., 2021). Tabu search (TS) is a neighborhood search algorithm known for its excellent local search capability (Mahmud et al., 2021). It is usually used following a population-based algorithm, such as GA, to achieved outstanding results (Xie et al., 2023; Xu et al., 2021). So, in this study, we propose a hybrid estimation and distribution algorithm and Tabu search (EDA-TS) for solving the SMDFJSP. In the EDA-TS, a multi-population strategy with some dispatching rules and a non-dominated solutions memory mechanism are designed to increase population diversity and stability.

The main contributions of this study are as follows.

- This paper developed an SM-DFJSP model considering sup-ply-demand matching, optimizing both the maximum total cost and makespan.
- An efficient EDA-TS algorithm is proposed, and introduced two enhancement mechanisms: a multi-population strategy and a nondominated solutions memory mechanism.
- The proposed EDA-TS algorithm is implemented, and the compared algorithms are reduplicated. Experimental results show that the EDA-TS has significant advantages in solving the SM-DFJSP.

The organization of the remaining parts of this paper is as follows. Section 2 reviews the related works. Section 3 gives the constrained programming model for SM-DFJSP. Section 4 describes the proposed EDA-TS algorithm. Section 5 carries out the numerical experiments and analyzes the corresponding results. Finally, Section 6 presents conclusions and future work.

## 2. Related works

### 2.1. Supply-demand matching of manufacturing services

Currently, there is limited research focusing on the supply-demand matching of sharedMfg. However, for cloud manufacturing, similar to sharedMfg, extensive research has garnered attention. Such as Tao et al. proposed the concept of an SDM simulator based on hyper networks (Tao et al., 2017). This simulator integrates modeling, simulation, evaluation, and statistical analysis for the process and the results of supply-demand matching and scheduling. Li et al. constructed a machine tool demand-resource description framework and applied the Markov Decision Process and cross-entropy to optimize the matching process and model (Li et al., 2020). Xiang et al. proposed a two-sidedbased supply-demand matching model under a hesitant fuzzy environment (Xiang et al., 2022). Liu et al. proposes a hybrid MPA-GSO-DNN model based on manufacturing service to solve the personalized recommendation of service composition (Liu et al., 2019). Liang et al. designed a deep reinforcement learning algorithm to optimize the service composite problem (Liang et al., 2021). The optimization objective in these studies is generally the quality of services (Hu et al., 2019), which includes cost, time, manufacturing effectiveness, and so on. However, as these studies do not involve scheduling within the SRUs, the mentioned indicators are mainly generated through simulation rather than being calculated.

In contrast to cloud manufacturing, the resource organization structure of sharedMfg supports fast retrieval and matching based on supply-demand types. This convenient matching mode enables the SMDFJSP model to realize integrated scheduling, covering supply-demand matching and job shop production scheduling.

### 2.2. Distributed flexible job shop scheduling

The DFJSP tries to solve the optimizing sequence and assignment among flexible job shops scattered in different geographical locations (Sahman, 2021). So, we can draw inspiration from DFJSP studies to devise a solution for SM-DFJSP. In general, DFJSP involves three subproblems: job-to-factory allocation, operation sequencing, and operation-to-machine assignment (Lu et al., 2018). Meng et al. propose four mixed integer linear programming models and a constraint programming model to address the DFJSP (Meng et al., 2020). Xie et al. proposed a hybrid genetic tabu search algorithm for solving the DFJSP (Xie et al., 2023). Sang and Tan designed a high-dimensional multiobjective memetic algorithm to solve the DFJSP for intelligent factories (Sang and Tan, 2022). Some scholars have also studied DFJSP that consider other factors. Lin et al. built the DFJSP model considering the joint decision of process planning and scheduling and developed a genetic algorithm (Lin et al., 2020). Luo et al. and Xu et al. constructed the DFJSP models, which allowed the operations of a job to be processed in different factories (Xu et al., 2021; Luo et al., 2020). Duan and Wang

Table 1
Example of SM-DFJSP.
![img-1.jpeg](img-1.jpeg)

Table 2
Notations.

| Indices and sets |  |
| :--: | :--: |
| $x$ | The index of the supply-demand type, $x=1,2, \ldots, X$ |
| $n$ | The index of job or customer, $n=1,2, \ldots, N$ |
| $r$ | The index of the SRUs, $r=1,2, \ldots, R$ |
| $k, n k$ | The index of the operation for job $n, k, n k=1,2, \ldots, K_{n}$ |
| $m, r m$ | The index of the machine for SRU $r, m, r m=1,2, \ldots, M_{r}$ |
| Set $_{U}$ | The set of jobs with shape $\left(X, N^{r}\right)$ |
| Set $_{U}$ | The set of SRUs with shape $\left(X, R^{r}\right)$ |

## Parameters

| $X$ | The number of supply-demand types |
| :-- | :-- |
| $N$ | The number of jobs or customers |
| $R$ | The number of SRUs |
| $J_{n}^{u}$ | Job $n$ with type $x$ |
| $U_{n}^{u}$ | SRU $r$ with type $x$ |
| $N^{u}$ | The number of jobs with type $x$ |
| $R^{u}$ | The number of SRUs with type $x$ |
| $K^{u}$ | The number of the operations for jobs with type $x$ |
| $M^{u}$ | The number of the machines for SRUs with type $x$ |
| $K_{n}$ | The number of the operations for job $n$ |
| $M_{r}$ | The number of the machines for SRU $r$ |
| $O_{n k}$ | The $k$ th operation of job $n$ |
| $M_{r m}$ | The $m$ th machine in SRU $r$ |
| $O_{n m}$ | The $n$ th operation processed by $M_{n m}$ |
| $P_{n k r m}$ | The processing time of operation $O_{n k}$ on $M_{n m}$ |
| $S_{n k r m}$ | The beginning time of operation $O_{n k}$ on $M_{n m}$ |
| $E_{n k r m}$ | The ending time of operation $O_{n k}$ on $M_{n m}$ |
| $F_{n}$ | The completion time of job $n$ |
| $T_{n r}$ | The transportation time from the SRU $r$ to customer $n$ |
| $C P_{n k r m}$ | The processing cost per unit time of $M_{n m}$ to deal with the operation $O_{n k}$ |
| $C T_{n r}$ | Transportation cost per unit time from SRU $r$ to the customer $n$ |
| $C$ | Total cost of production |
| $M K$ | Makespan |
| $V$ | A large positive number |

## Variables

| $A_{n r}$ | If job $n$ is assigned to SRU $r, A_{n r}=1$; otherwise, $A_{n r}=0$ |
| :-- | :-- |
| $B_{n k r m}$ | If $M_{n n}$ is selected to process $O_{n k}, B_{n k r m}=1$; otherwise, $B_{n k r m}=0$ |
| $G_{n n}$ | If the type of job $n$ is $x, G_{n n}=1$; otherwise, $G_{n n}=0$ |
| $H_{n n}$ | If the type of SRU $r$ is $x H_{n n}=1$; otherwise, $H_{n n}=0$ |
| $Q_{g n n}$ | If $O_{g n n}$ is processed directly after $O_{g n n}$ on $M_{n n}, Q_{g n n}=1$; otherwise $Q_{g n n}=0$ |

built the DFJSP model with machine breakdowns considering machine idle time arrangement and machine speed level selection (Duan and Wang, 2021). In recent years, some researches have also paid attention to dynamic DFJSP. Wang et al. proposed an overall architecture of realtime DFJSP based on the edge computing and industrial internet of things (Wang et al., 2021). Zhu et al. proposed a dynamic DFJSP considering operation inspection and designed a modified memetic algorithm (Zhu et al., 2023).

However, all of these studies assumed that every factory could complete any job. In a sharedMfg environment, a batch of jobs may have different requirements, and different SRUs may provide various services. Hence, it becomes imperative to address SM-DFJSP with a focus on achieving supply-demand consistency.

### 2.3. Estimation of distribution algorithm

EDA is a non-deterministic, stochastic heuristic algorithm based on a probability distribution model (Muelas et al., 2011). It has been widely applied in production scheduling problems. Pérez-Rodríguez et al. used EDA to solve the flexible job shop scheduling problems (Perez-Rodríguez et al., 2014). Faraji Amiri et al. utilized EDA to address the multiobjective green flow shop scheduling problems under uncertainty (Amiri and Behnamian, 2020). Liu et al. designed a fast EDA to solve dynamic flexible job shop scheduling problem with fuzzy processing time (Liu et al., 2015). Zhang et al. designed a three-dimensional matrix-cube-based EDA for the distributed assembly permutation flow shop scheduling problem (Zhang et al., 2021). Liu et al. proposed an EDA with the neighborhood search strategy to solve the two-stage hybrid flow shop scheduling problem (Liu et al., 2023). Sheng et al. developed an EDA and designed some local search operators for the hybrid flow shop scheduling problem (Wang et al., 2013). Hao et al. proposed a multiobjective EDA with variable neighborhood search (VNS) for a bicriteria stochastic job shop scheduling problem (Hao et al., 2017). Du et al. proposed a hybrid EDA-VNS with self-adaptive parameters heuristic to solve the DFJSP (Du et al., 2021). Tzeng et al. proposed a hybrid EDA with an ant colony system to solve the permutation scheduling problem (Tzeng et al., 2012). Zhao et al. proposed an estimation of distribution algorithm-based hyper-heuristic to solve the distributed assembly mixed no-idle permutation flow shop scheduling problem (Zhao et al., 2023).

Mixing other algorithms or enhancement mechanisms is a common practice to improve EDA development capabilities. For solving the SMDFJSP model, a hybrid EDA-TS algorithm with dispatching rules is proposed. Moreover, to fully exploit the synergy between these two components, a non-dominated solutions memory mechanism is devised. Historical non-dominant solutions obtained from both EDA and TS components are involved in guiding the generation of candidate solutions.

## 3. Model description

### 3.1. Problem definition

The SM-DFJSP can be generalized as assigning jobs to SRUs based on their supply-demand types, determining the processing sequence of

![img-2.jpeg](img-2.jpeg)

Fig. 2. Gantt chat for the example.
operations, and arranging machines for operations. Compared to general DFJSP, the SM-DFJSP has the following characteristics:
(1) Diversity in job and SRU types. There exist different types of jobs and SRUs.
(2) Consideration of supply-demand consistency. When assigning jobs to an SRU, the consistency of supply-demand is considered.
(3) Heterogeneity of SRUs. SRUs are heterogeneous in terms of function type, number of machines, and processing efficiency.
(4) Inclusion of logistics cost and time. The SM-DFJSP considers the logistics cost and time from SRUs to customer locations.

To illustrate the SM-DFJSP scheduling process, we provide an example involving two types of six jobs and three SRUs. It's worth noting that the number of operations and machines may differ for various jobs and SRUs. Jobs and their operations for this case are represented by $J_{1}^{1}=$ $\left(O_{11}, O_{12}, O_{13}\right), J_{2}^{1}=\left(O_{21}, O_{22}\right), J_{3}^{2}=\left(O_{31}, O_{32}\right), J_{4}^{2}=\left(O_{41}, O_{42}, O_{43}\right), J_{5}^{2}$ $=\left(O_{51}, O_{52}\right), J_{6}^{2}=\left(O_{61}, O_{62}\right)$. SRUs and their available machines are represented by $U_{1}^{1}=\left(M_{11}, M_{12}\right), U_{2}^{2}=\left(M_{21}, M_{22}, M_{23}\right), U_{3}^{2}=\left(M_{31}, M_{32}\right)$. The detailed data are given in Table 1, and the definition of notations is shown in Table 2. There may be multiple scheduling schemes between the same type of jobs and SRUs, but there is no scheduling relationship between different types. The Gantt chart in Fig. 2 shows a scheduling scheme for this case.

### 3.2. Notations

The notations of paraments and indices used in this paper are summarized in Table 2.

### 3.3. Assumptions

The assumptions related to SM-DFJSP are as follows:
(1) Each job can be assigned to only one SRU of the same type, and each SRU can receive multiple jobs of the same type.
(2) Each operation of the jobs can be processed on any machine in the same SRUs as its type.
(3) All jobs are parallel tasks without precedence constraints.
(4) The execution process of an operation cannot be interrupted.
(5) At any time, each operation must be processed at one machine, and each machine can only have one job in progress.
(6) Transportation time and cost within SRUs are not considered.
(7) After the last operation of a job is completed, it will be sent to the customer immediately.

### 3.4. Mathematical model

The mathematical model of the SM-DFJSP is expressed as follows: Objective:
(1) minimization of total cost (C):

$$
\min C=\sum_{n=1}^{N} \sum_{k=1}^{K_{n}} \sum_{r=1}^{R} \sum_{n=1}^{N_{r}} P_{n k m} \times C P_{n k m} \times B_{n k m}+\sum_{n=1}^{N} \sum_{r=1}^{R} T_{n r} \times C T_{n r} \times A_{n r}
$$

(2) minimization of makespan (MK)
$\min M K=\max \left\{F_{n}+T_{n r} \times A_{n r} \mid n=1,2, \ldots, N\right\}, \forall r$
Subject to:
$A_{n r} \leq G_{n s} \times H_{r s}, \forall n, r, x$
$0 \leq \mathrm{X} \leq \min \{N, R\}$
$\sum_{n=1}^{R} A_{n r}=1, \forall n$
$\sum_{n=1}^{N} A_{n r} \geq 0, \forall r$
$\sum_{r=1}^{R} \sum_{n=1}^{N_{r}} B_{n k m}=1, \forall n, k$
$E_{n j m}-E_{n k m} \geq P_{n j m} \times Q_{j j m}+V \times\left(Q_{j j m}-1\right), \forall n, r, m$
$E_{n k m}=S_{n k m}+P_{n k m}, \forall n, k, r, m$
$S_{n k m} \geq \mathrm{E}_{n(k-1) m}, \forall n, r, m, k>1$
$\sum_{n=1}^{N_{r}} O_{n k} \times A_{n r} \times B_{n k m}=K_{n}, \forall n, k, r$
$A_{n r}= \begin{cases}1, & \text { IfjobnisassignedtoSRUr } \\ 0, \text { Otherwise }\end{cases}$
$B_{n k m}= \begin{cases}1, & \text { If } M_{m} \text { isselectedtoprocess } O_{n k} \\ 0, \text { Otherwise }\end{cases}$
$G_{n s}= \begin{cases}1, & \text { Ifthetypeofjobniss } \\ 0, \text { Otherwise }\end{cases}$
$H_{r s}= \begin{cases}1, & \text { IfthetypeofSRUrisx } \\ 0, \text { Otherwise }\end{cases}$
$Q_{j j m}= \begin{cases}1, & \text { If } O_{j m} \text { isprocesseddirectlyafter } O_{j m} \text { on } M_{r m} \\ 0, \text { Otherwise }\end{cases}$
The optimization objectives in this study are to minimize total cost and makespan, as shown in Eq. (1) and Eq. (2). The total cost includes all

![img-3.jpeg](img-3.jpeg)

Fig. 3. Encoding and decoding.
production costs and transportation costs between the SRU and the customer. The functions (3) to (16) are the constraint sets. Inequality (3) ensures the consistency between the job type and the designated SRU. Inequality (4) indicates that the types of jobs and SRUs are less than the number of jobs or SRUs. Constraints (5) and (6) signify that a job can only be assigned to one SRU, while each SRU can undertake multi jobs or none at all. Constraint sets (7) and (8) indicate that each operation can only be processed once on one machine and that each machine is capable of processing only one operation at any given time. Eq. (9) restricts that completing time of operation $O_{\text {uk }}$ on machine $M_{\mathrm{rns}}$ is the sum of the processing time and the start time. Inequality (10) ensures the processing route of the jobs, signifying that for two consecutive operations of a job, the latter can only be processed after the completion of the former operation. Eq. (11) ensures that all operations for each job must be performed. Constraints (12-16) represent the range of binary decision variables.

## 4. Hybrid EDA-TS algorithm for SM-DFJSP

EDA is an evolutionary algorithm that generates new individuals by sampling from the probabilistic distribution of the population (Zhang et al., 2021). While it boasts excellent global exploration ability, there's a risk of premature convergence and lack of diversity in its iterative process (Gao and de Silva, 2018; Utamina, 2021). TS is a very effective local search method in solving job shop scheduling problems (Nasiri and Kianfar, 2012). Employing TS after a population-based algorithm, which provides initial solutions to TS, can improve exploitation ability with lower computational expense (Mahmud et al., 2021). With the above analysis, we propose a hybrid EDA-TS algorithm that enhances development and exploration by integrating the EDA and TS components.

### 4.1. Encoding and decoding

In this study, we design a four-layer discrete encoding to describe the solution of SM-DFJSP. An individual code includes an SRU assignment layer (UA layer), an Operation sequencing layer (OS layer), an Operation processing layer (OP layer), and a Machine selection layer (MS layer), which respectively correspond to the job-SRU assignment, operation sequencing according to the job types, the processing order of operation in each SRU, and the execution sequence of machines in each SRU. Fig. 3 depicts an encoding scheme for the ( $2 X 6 J 3 U$ ) scale, involving two types, six jobs, and three SRUs. It is worth mentioning that in the OS layer, operations belonging to the same type of jobs are uniformly sorted, so there are $X$ vectors. Then, to determine the processing sequence of operations in each SRU, the operation sequence needs to be converted from the OS layer to the OP layer. So, there are $R$ operation
sequencing vectors in the OP layer. The codes of each layer are explained as follows:
(1) For the UA layer. Its length is equal to the number of jobs ( $N$ ). The vector's index represents the job number $(n)$, and the $n$th code ' $x, r$ ' means that the $J_{N}^{x}$ is assigned to the $U_{r}^{x}$;
(2) The OS layer includes $X$ vectors. In the $x$ th vector, there are $K^{x}$ codes, in which the code ' $n$ ' represents the $J_{N}^{x}$ and the count of ' $n$ ' called $k$, which means the $k$ th operations of $J_{N}^{x}\left(O_{\text {uk }}\right)$;
(3) The OP layer includes $R$ vectors. Where the $r$ th vector represents the execution sequences of the operations in $U_{r}^{x}$. The codes in these vectors are sorted according to their order in the OS layer.
(4) The MS layer includes $R$ vectors. In its $r$ th vector, the code ' $m$ ' represents the machine $M_{\mathrm{rns}}$ that processes the corresponding operation.

### 4.2. EDA component

EDA establishes the probability distribution by sampling the search space and statistical learning. Then utilizing the probability matrix to produce excellent new individuals (Dang et al., 2022). Based on the above encoding method, we design three probability matrices, $P M A$, $P M S$, and $P M M$. These matrices are employed to generate the UA, OS, and MS layers, respectively.

In order to ensure the supply-demand consistency of the US layer, the PMA is designed in the shape of $X \bullet N^{x} \bullet R^{x}$. The element $P A_{x, N, r}(g)$ in $P M A(g)$ represents the probability of $J_{N}^{x}$ being assigned to $U_{r}^{x}$ at the $g$ th iteration. The $P M A(0)$ is given as Eq. (17), and its update mechanism is expressed as Eq. (18), where $\alpha$ is the learning rate of the $P M A, E N(g)$ is the total number of elite and $g$ th-generation non-dominated solutions. In the generation of the UA layer at $g$ th iteration, $S P A(g)$ is introduced as an auxiliary matrix, and the element $s P A_{x, N, r}(g)$ of $S P A(g)$ is given as Eq. (20). For each job, produce a random number between $(0,1)$. From right to left, if $s P A_{x, N, r}(g) \geq \theta$, the $J_{N}^{x}$ is assigned to $U_{r}^{x}$.
$P A_{x, n, r}(0)=\frac{1}{R_{x}} \forall x, n \in \operatorname{Set}_{f}[x], r \in \operatorname{Set}_{U}[x]$

$$
\begin{aligned}
P A_{x, n, r}(g+1) & =(1-\alpha) \times P A_{x, n, r}(g)+\alpha \times \frac{\sum_{r=1}^{k N(g)} \Theta_{x, n, r}^{r}}{E N(g)}, \forall x, n \in \operatorname{Set}_{f}[x], r \\
& \in \operatorname{Set}_{U}[x]
\end{aligned}
$$

$\Theta_{x, n, r}^{r}=\left\{\begin{array}{c}1, I\left(J_{r}^{x}\right) \text { isassignedto } U_{r}^{x} \text { inindividualz } \\ 0, \text { Otherwise }\end{array}\right.$
$s P A_{x, n, r}(g)=\sum_{r=-1}^{R_{x}} P A_{x, n, r}(g), \forall x, n \in \operatorname{Set}_{f}[x], r \in \operatorname{Set}_{U}[x]$

![img-4.jpeg](img-4.jpeg)

Fig. 4. The generation methods and proportion of individuals.
The element $P S_{x, N, t}(g)$ in $P M S(g)$ represents the probability of the $J_{N}^{g}$ appearing at the $i$ th position in the $x$ th vector in OS layer at the $g$ th iteration. The PMS (0) is given as Eq. (21), and its update mechanism is expressed as Eq. (22), where $\beta$ is the learning rate of the PMS. The generation of the OS layer is shown as algorithm 1. $\operatorname{SPS}(g)$ is introduced as an auxiliary matrix, and the element $s P S_{x, N, t}(g)$ of $\operatorname{SPS}(g)$ is given as Eq. (24).
$P S_{x, n, t}(0)=\frac{1}{K_{x}} \forall x, n \in \operatorname{Set}_{f}[x], i \in\left[1, K^{v}\right]$
$P S_{x, n, t}(g+1)=(1-\beta) \times P S_{x, n, t}(g)+\beta \times \frac{\sum_{i=1}^{k N(g)} \Phi_{x, n, t}^{i}}{E N(g)} \times \frac{1}{K_{n}} \forall x, n \in \operatorname{Set}_{f}[x], i$
$\in\left[1, K^{v}\right]$
$\Phi_{x, n, t}^{i}=\left\{\begin{array}{c}1 . I f J_{n}^{g} a p p e a r s a t p o s i t i o n i i n O S l a y e r o f i n d i v i d u a l z \\ 0, \text { Otherwise }\end{array}\right.$
$s P S_{x, n, t}(g)=\sum_{i=1}^{R_{t}} P S_{x, n, t}(g), \forall x, n \in \operatorname{Set}_{f}[x], i \in\left[1, K^{v}\right]$

Algorithm 1: OS layer
Input: $S P S(g), X, N^{0}, K^{0}, K_{0}$
Output: OS layer
$\# V x$ : the $x$ th vector in OS layer, $x=1,2, \ldots, X$
\# POS: the set of remaining position in $x$ th vector, $x=1,2, \ldots, X$
\# $\theta$ : a random number
01: for $x$ in arrange $(1: X)$ do
02: $V x \leftarrow \operatorname{zeros}\left(1, K^{0}\right)$
03: $P O S \leftarrow$ arrange $\left(1, K^{0}\right)$
04: for $n$ in $N^{0}$ do
05: for $k$ in arrange $\left(1, K_{0}\right)$ do
06: $\quad \theta \leftarrow$ random $(0, \max \left(s P S_{x, N, t}\right))$
07: for $i$ in $P O S$ do
08: if $\theta \leq s P S_{x, n, t}$ then
09: $\quad V x[i] \leftarrow n$
10: $\quad$ def $P O S[i]$
11: break
12: else
(continued on next column)
(continued)

| Algorithm 1: OS layer |  |
| :--: | :--: |
| 13: | continue |
| 14: | end if |
| 15: | end for |
| 16: | end for |
| 17: | end for |
| 18: OS layer $(x)$ | $V x$ |
| 19: end for |  |
| 20: return OS layer |  |

Algorithm 2: MS layer
Input: OP layer, $S P M(g), X, S e t_{U}, M_{r}$
Output: MS layer
\# OPr: the $r$ th vector in OP layer, $r=1,2, \ldots, R$
\# MSr: the $r$ th vector in MS layer, $r=1,2, \ldots, R$
\# $\theta$ : a random number
01: for $x$ in arrange $(1: X)$ do
02: for $r$ in $\operatorname{Set}_{f}[x]$ do
03: $\quad$ MSr $\leftarrow \operatorname{zeros}\left(1, \operatorname{len}(O P r)\right.$ )
04: for $i$ in $O P r$ do
05: $\quad n \leftarrow \mathrm{OPr}[i]$
06: $\quad k \leftarrow$ OPr index of ( $n$ ) index of ( $i$ )
07: $\quad \theta \leftarrow$ random $(0,1)$
08: for $m$ in arrange ( $1: M_{r}$ ) do
09: if $\theta \leq s P M_{x, k, r, m}$ then
10: $\quad \operatorname{MSr}[i] \leftarrow m$
11: break
12: else
13: continue
14: end if
15: end for
16: end for
17: end for
18: MS layer $(r) \leftarrow M S r$
19: end for
20: return MS layer

The element $P M_{n, k, r, m}(g)$ in $P M M(g)$ represents the probability of $M_{r m}$ processing the operation $O_{n k}$ at the $g$ th iteration. The $P M M(0)$ is given as Eq. (25), and its update mechanism is expressed as Eq. (26), where $\gamma$ is the learning rate of $P M M$. The generation of MS layer is shown as algorithm 2. $\operatorname{SPM}(g)$ is introduced as an auxiliary matrix, and the element $s P M_{n, k, r, m}(g)$ of $\operatorname{SPM}(g)$ is given as Eq. (29).
$P M_{n, k, r, m}(0)=\frac{1}{M_{r}} \forall n \in S e t_{f}[x], r \in S e t_{U}[x], k, m$
$P M_{n, k, r, m}(g+1)=(1-\gamma) \times P M_{n, k, r, m}(g)+\gamma \times \Lambda(g), \forall n \in S e t_{f}[x], r$

$$
\in S e t_{U}[x], k, m
$$

$\Lambda(g)=\left\{\begin{array}{c}\sum_{i=1}^{k N(g)} \Psi_{n, k, r, m}^{i} \\ \sum_{i=1}^{k N(g)} \Theta_{x, n, r}^{i} \\ \Psi_{n, k, r, m}^{i} \end{array} \cdot I f \sum_{i=1}^{k N(g)} \Theta_{x, n, r}^{i} \neq 0\right.$
$P M_{n, k, r, m}$, Otherwise
$\Psi_{n, k, r, m}^{i}=\left\{\begin{array}{c}1 . \operatorname{If} M_{r m} p r o c e s s e s t h e o p e r a t i o n O_{n k} i n i n d i v i d u a l z \\ 0, \text { Otherwise }\end{array}\right.$
$s P M_{n, k, r, m}(g)=\sum_{m=1}^{M_{r}} P M_{n, k, r, m}(g), \forall n \in S e t_{f}[x], r \in S e t_{U}[x], k, m$

### 4.3. The multi-population strategy

Dispatching rules has been widely used in industry because they are concise, fast, and efficient for production scheduling (Zhang and Roy, 2019; Zhang et al., 2022). But no single dispatching rules is absolutely superior to any other rule under various environment (Luo et al., 2021). So, many researchers focus on composite dispatching rules combine with other optimization algorithms and techniques (Tay and Ho, 2008;

![img-5.jpeg](img-5.jpeg)

Fig. 5. Neighborhood structure I.
![img-6.jpeg](img-6.jpeg)

Fig. 6. Neighborhood structure II.
![img-7.jpeg](img-7.jpeg)

Fig. 7. Neighborhood structure III.
![img-8.jpeg](img-8.jpeg)

Fig. 8. The framework of the non-dominated solutions mechanism.

![img-9.jpeg](img-9.jpeg)

Fig. 9. The framework of the EDA-TS.

Table 3
Factor levels of the parameters of proposed algorithm.

| Factor levels | Parameters |  |  |  |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $\alpha$ | $\beta$ | $\gamma$ | $\mu$ | pop-size | $\varepsilon$ |
| 1 | 0.1 | 0.1 | 0.1 | 0.1 | 50 | 0.001 |
| 2 | 0.2 | 0.2 | 0.2 | 0.2 | 100 | 0.002 |
| 3 | 0.3 | 0.3 | 0.3 | 0.3 | 150 | 0.005 |
| 4 | 0.4 | 0.4 | 0.4 | 0.4 | 200 | 0.008 |
| 5 | 0.5 | 0.5 | 0.5 | 0.5 | 250 | 0.01 |

Oukil et al., 2022; Wang et al., 2023). In this study, a multi-population strategy is proposed which combines some dispatching rules with the EDA component to improve the quality and enrich the diversity of the population. Where the dispatching rules include MD, MC, and MCT. Their details are as follows:
(1) MD rule: Assign the job to the nearest SRU.
(2) MC rule: Arrange the operation to the machine with the lowest completion cost in the corresponding SRU.
(3) MCT rule: Starting from the first operation in the OP layer, arrange it to the machine with minimized makespan in the corresponding SRU.

During iteration, these rules are combined with the probability

Table 4
Combination of parameter levels and the average value of the ODS.

| Trial $^{\#}$ | $\alpha$ | $\beta$ | $\gamma$ | $\mu$ | popsize | $\varepsilon$ | avg_ODS | Trial $^{\#}$ | $\alpha$ | $\beta$ | $\gamma$ | $\mu$ | popsize | $\varepsilon$ | avg_ODS |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0.0664 | 14 | 3 | 4 | 1 | 3 | 5 | 2 | 0.1412 |
| 2 | 1 | 2 | 2 | 2 | 2 | 2 | 0.1126 | 15 | 3 | 5 | 2 | 4 | 1 | 3 | 0.1158 |
| 3 | 1 | 3 | 3 | 3 | 3 | 3 | 0.1282 | 16 | 4 | 1 | 4 | 2 | 5 | 3 | 0.1076 |
| 4 | 1 | 4 | 4 | 4 | 4 | 4 | 0.1423 | 17 | 4 | 2 | 5 | 3 | 1 | 4 | 0.0765 |
| 5 | 1 | 5 | 5 | 5 | 5 | 5 | 0.1321 | 18 | 4 | 3 | 1 | 4 | 2 | 5 | 0.1271 |
| 6 | 2 | 1 | 2 | 3 | 4 | 5 | 0.1287 | 19 | 4 | 4 | 2 | 5 | 3 | 1 | 0.1286 |
| 7 | 2 | 2 | 3 | 4 | 5 | 1 | 0.1431 | 20 | 4 | 5 | 3 | 1 | 4 | 2 | 0.0406 |
| 8 | 2 | 3 | 4 | 5 | 1 | 2 | 0.1230 | 21 | 5 | 1 | 5 | 4 | 3 | 2 | 0.1109 |
| 9 | 2 | 4 | 5 | 1 | 2 | 3 | 0.0497 | 22 | 5 | 2 | 1 | 5 | 4 | 3 | 0.1304 |
| 10 | 2 | 5 | 1 | 2 | 3 | 4 | 0.1168 | 23 | 5 | 3 | 2 | 1 | 5 | 4 | 0.0322 |
| 11 | 3 | 1 | 3 | 5 | 2 | 4 | 0.1192 | 24 | 5 | 4 | 3 | 2 | 1 | 5 | 0.0629 |
| 12 | 3 | 2 | 4 | 1 | 3 | 5 | 0.0349 | 25 | 5 | 5 | 4 | 3 | 2 | 1 | 0.0821 |
| 13 | 3 | 3 | 5 | 2 | 4 | 1 | 0.0970 |  |  |  |  |  |  |  |  |

![img-10.jpeg](img-10.jpeg)

Fig. 10. The trend of factor levels of the EDA-TS.

Table 5
Comparison results of the EDA-TS and Gurobi.

| Instances | EDA-TS |  |  |  | Gurobi | Gap |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| G01 | [1214.0, 70.0], [1377.0, 48.0], [1249.0, 54.0], [1229.0, 57.0], [1218.0, 61.0], [1259.0, 53.0], [1264.0, 52.0], [1244.0, 56.0], [1280.0, 51.0] |  |  |  | $\begin{aligned} & {[1218} \\ & 61] \end{aligned}$ | 0.0000 \% |
| G02 | [1731.0, 112.0], [1739.0, 78.0], [1781.0, 68.0], [1838.0, 61.0], [1697.0, 154.0], [1786.0, 66.0], [1714.0, 117.0], [1816.0, 64.0], [1823.0, 63.0], [1915.0, 55.0], [1972.0, 51.0], [1756.0, 73.0], [1829.0, 62.0], [1949.0, 52.0], [1775.0, 72.0] | [1739, <br> 78] | 1.0457 \% |
| G03 | $\begin{aligned} & {[2243.0,126.0], \text { [2234.0, 149.0], [2347.0, } \\ & 93.0], \text { [2263.0, 118.0], [2627.0, 69.0], } \\ & \text { [2393.0, 80.0], [2325.0, 98.0], [2316.0, } \\ & \text { 105.0], [2728.0, 60.0], [2687.0, 63.0], } \\ & \text { [2324.0, 99.0], [2736.0, 59.0], [2359.0, } \\ & \text { 88.0], [2384.0, 83.0], [2343.0, 97.0], } \\ & \text { [2470.0, 75.0], [2284.0, 110.0] } \end{aligned}$ |  |  |  | 0.5268 \% |

distribution model to generate new populations. The different generation modes and their proportions for individuals in the population are shown in Fig. 4. Especially where SiO represents the generation method of the OP layer, which operation is shown in Fig. 3.

### 4.4. TS component

In the TS component, we propose 3 neighborhood structures. To improve the dispersion of neighborhood solutions, we adopt a hybrid short-term and long-term memory strategy (Xu et al., 2021; Logendran et al., 2007) in which the Tabu list (T list) and frequency list are used to tabu previous operations. The details are described as follows:
(1) Neighborhood structure I.

The generation of a neighborhood solution based on structure I is shown in Fig. 5. Its main processes are as follows:

Step 1: In UA layer, if there are at least 2 SRUs can complete the selected job, reassign the job to others.

Step 2: For OS layer, the operations of the selected job are reassigned to the new SRU, while its position in OS layer stays the same.

Step 3: For OP layer, move the operations of the selected job from the initial SRU to the new SRU.

Step 4: For MS layer, reselect the machines randomly for the operations in the new SRU.

Repeating step1-4 yields NI neighborhood solutions. To minimize cost calculations, we randomly select only 5 jobs when dealing with a lot of jobs. Thus, the calculation method of NI is expressed as Eq. (30). The value of NI is observed to be dependent on the scale of the SM-DFJSP.
$N=1 \mathrm{I}=\sum_{s=1}^{5} \min \left\{5, N_{s}\right\} \times I_{s}, \forall x$
Where,
$I_{s}=\left\{\begin{array}{cc}1, \text { If } R^{*} \geq 2, & , \forall x \\ 0, \text { Others } & \forall x\end{array}\right.$
The frequency list LMLS is based on neighborhood structure I and adopts a long-term memory strategy. It is a $R \bullet N$ matrix which is used to record the movement of the job. When the $J_{n}^{S}$ is reassigned to $I J_{s}^{S}$, the element $L S_{i, p}$ in the $R \bullet N$ matrix adds 1 . If a neighborhood solution is worse than the current solution, its target value will be penalized as Eq. (32), where $e$ is the penalty factor.
$(C, M K)=\left(C+e \bullet C \bullet L S_{i, n}, M K+e \bullet M K \bullet L S_{i, n}\right)$
(2) Neighborhood structure II.

The generation of a neighborhood solution based on structure II is shown in Fig. 6. Its main processes are as follows:

Step 1: For the OS layer, select an operation at the $i I$ position;
Step 2: Insert the selected operation into a random position $i 2$ of the same $x(x \in X)$ as $i I$. Then move all operations between $i I$ and $i 2$ forward $(i 2>i I)$ or backward $(i I>i 2)$ one position;

Step 3: For the OP layer, adjust the operation sequence in the SRUs according to the OS layer.

For each neighborhood solution, the OS and OP layers are changed. By repeating the step1-3, we can obtain NII $\left(\sum_{s=1}^{8} \min \left(5, K^{*}\right)\right)$ neighborhood solutions, where the NII is the number of the neighborhood

Table 6
Factor levels of parameters of the compared algorithms.

| Factor levels | EDA |  |  |  |  | NSGA-II |  |  |  | EDA-VNS |  |  |  |  | H-GA-TS |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $\mu$ | $\alpha$ | $\beta$ | $\gamma$ | popsize | popsize | cr | mr | $\mu$ | $\alpha$ | $\beta$ | $\gamma$ | popsize | popsize | cr | mr | t | c |
| 1 | 0.2 | 0.2 | 0.2 | 0.2 | 50 | 50 | 0.6 | 0.1 | 0.2 | 0.2 | 0.2 | 0.2 | 50 | 50 | 0.2 | 0.02 | 10 | 0.01 |
| 2 | 0.3 | 0.3 | 0.3 | 0.3 | 100 | 100 | 0.7 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 100 | 100 | 0.4 | 0.05 | 20 | 0.02 |
| 3 | 0.4 | 0.4 | 0.4 | 0.4 | 150 | 150 | 0.8 | 0.5 | 0.4 | 0.4 | 0.4 | 0.4 | 150 | 150 | 0.6 | 0.08 | 30 | 0.03 |
| 4 | 0.5 | 0.5 | 0.5 | 0.5 | 200 | - | - | - | 0.5 | 0.5 | 0.5 | 0.5 | 200 | 200 | 0.8 | 0.1 | 40 | 0.04 |

![img-11.jpeg](img-11.jpeg)

Fig. 11. The trends of factors levels of the compared algorithm.

Table 7
The average GD, IGD and run times of EDA-TS and the compared algorithms.

| Instances | avg_GD |  |  |  |  |  | avg_IGD |  |  |  |  | run time (s) |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | EDA-TS | EDA | NSGA-II | EDA-VNS | H-GA-TS | EDA-TS | EDA | NSGA-II | EDA-VNS | H-GA-TS |  |  |
| SDMKO1 | 0.022 | 0.155 | 0.769 | 0.062 | 0.214 | 0.026 | 0.223 | 1.110 | 0.077 | 0.305 | 60 |  |
| SDMKO2 | 0.001 | 0.275 | 0.781 | 0.065 | 0.286 | 0.002 | 0.344 | 1.175 | 0.101 | 0.349 | 61 |  |
| SDMKO3 | 0.000 | 0.214 | 0.619 | 0.128 | 0.438 | 0.000 | 0.356 | 1.197 | 0.284 | 0.476 | 77 |  |
| SDMKO4 | 0.001 | 0.220 | 0.675 | 0.094 | 0.080 | 0.002 | 0.280 | 1.160 | 0.130 | 0.151 | 67 |  |
| SDMKO5 | 0.007 | 0.133 | 0.384 | 0.045 | 0.067 | 0.024 | 0.298 | 0.774 | 0.147 | 0.281 | 68 |  |
| SDMKO6 | 0.000 | 0.272 | 0.747 | 0.193 | 0.436 | 0.000 | 0.435 | 1.271 | 0.361 | 0.473 | 79 |  |
| SDMKO7 | 0.006 | 0.105 | 0.666 | 0.058 | 0.090 | 0.015 | 0.186 | 1.124 | 0.070 | 0.170 | 67 |  |
| SDMKO8 | 0.000 | 0.195 | 0.586 | 0.128 | 0.320 | 0.001 | 0.424 | 1.023 | 0.330 | 0.428 | 77 |  |
| SDMKO9 | 0.000 | 0.193 | 0.528 | 0.213 | 0.686 | 0.000 | 0.518 | 1.030 | 0.561 | 0.788 | 102 |  |
| SDMK10 | 0.000 | 0.200 | 0.534 | 0.224 | 0.679 | 0.000 | 0.554 | 1.062 | 0.597 | 0.764 | 106 |  |
| SDMK11 | 0.001 | 0.098 | 0.336 | 0.095 | 0.267 | 0.013 | 0.297 | 0.753 | 0.262 | 0.486 | 88 |  |
| SDMK12 | 0.000 | 0.143 | 0.358 | 0.158 | 0.503 | 0.000 | 0.406 | 0.856 | 0.440 | 0.644 | 99 |  |
| SDMK13 | 0.000 | 0.165 | 0.441 | 0.180 | 0.527 | 0.000 | 0.482 | 0.913 | 0.496 | 0.640 | 99 |  |
| SDMK14 | 0.000 | 0.192 | 0.429 | 0.216 | 0.669 | 0.000 | 0.554 | 0.906 | 0.629 | 0.792 | 126 |  |
| SDMK15 | 0.000 | 0.169 | 0.392 | 0.217 | 0.640 | 0.000 | 0.525 | 0.897 | 0.615 | 0.822 | 126 |  |
| SDMK16 | 0.032 | 0.121 | 0.430 | 0.022 | 0.193 | 0.046 | 0.315 | 0.793 | 0.178 | 0.401 | 63 |  |
| SDMK17 | 0.017 | 0.094 | 0.356 | 0.036 | 0.133 | 0.033 | 0.307 | 0.758 | 0.148 | 0.365 | 72 |  |
| SDMK18 | 0.007 | 0.080 | 0.326 | 0.062 | 0.335 | 0.017 | 0.301 | 0.752 | 0.211 | 0.530 | 87 |  |
| SDMK19 | 0.004 | 0.102 | 0.372 | 0.091 | 0.395 | 0.012 | 0.327 | 0.783 | 0.269 | 0.636 | 101 |  |
| SDMK20 | 0.003 | 0.090 | 0.305 | 0.092 | 0.363 | 0.015 | 0.321 | 0.747 | 0.261 | 0.640 | 97 |  |
| SDMK21 | 0.006 | 0.105 | 0.341 | 0.109 | 0.498 | 0.008 | 0.303 | 0.760 | 0.318 | 0.763 | 110 |  |
| SDMK22 | 0.007 | 0.100 | 0.309 | 0.139 | 0.589 | 0.011 | 0.268 | 0.717 | 0.389 | 0.873 | 137 |  |
| SDMK23 | 0.003 | 0.110 | 0.306 | 0.151 | 0.621 | 0.006 | 0.284 | 0.709 | 0.424 | 0.895 | 155 |  |
| SDMK24 | 0.001 | 0.101 | 0.333 | 0.142 | 0.656 | 0.005 | 0.309 | 0.724 | 0.409 | 0.920 | 152 |  |
| SDMK25 | 0.000 | 0.116 | 0.325 | 0.150 | 0.687 | 0.003 | 0.322 | 0.711 | 0.438 | 0.923 | 171 |  |

solutions.
The T list, utilizing a short-term memory strategy, employs solutions as tabu objects based on the neighborhood structure II. The length of the T list is $N I I$. When the T list is fully loaded, it follows the first in first out rule for updates. If a neighborhood solution is better than the optimal solution and is already in the tabu list, remove it from the tabu list. Then consider this solution as the current and optimal solution and re-add it to the tabu list.
(3) Neighborhood structure III.

The generation of a neighborhood solution based on structure III is shown in Fig. 7. It can be described as follows: select a machine in the MS layer and replace it with others in the same SRUs randomly. Repeat this operation, then we can obtain $N I I I\left(\sum_{k=1}^{K} \min \left(5 . K^{k}\right)\right)$ neighborhood
solutions, where the NIII is the number of the neighborhood solutions.
The frequency list LMLM based on neighborhood structure III adopts a long-term memory strategy. It is a $X \bullet M^{k} \bullet K^{k}$ frequency matrix, its element $L M_{C n}$ means that $M_{m n}$ is selected to process the $O_{n k}$. If a neighborhood solution is worse than the current solution, its target value will be penalized as Eq. (33).
$(C, M K)=(C+e \bullet C \bullet L M_{c n}, M K+e \bullet M K \bullet L M_{c n})$

### 4.5. Non-dominated solutions memory mechanism

To fully exploit the synergy between EDA and TS, we introduce a non-dominated solutions memory mechanism. During iteration, a nondominated solutions pool is established to record and update the

Table 8
The C_metrics of the EDA-TS and the compared algorithms.

| Instances | EDA-TS vs. EDA |  | EDA-TS vs. NSGA-II |  | EDA-TS vs. EDA-VNS |  | EDA-TS vs. H-GA-TS |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | C(A, B) | C(B, A) | C(A, B) | C(B, A) | C(A, B) | C(B, A) | C(A, B) | C(B, A) |
| SDMK01 | 0.983 | 0.000 | 1.000 | 0.000 | 0.629 | 0.326 | 0.967 | 0.007 |
| SDMK02 | 1.000 | 0.000 | 1.000 | 0.000 | 0.881 | 0.034 | 0.967 | 0.007 |
| SDMK03 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| SDMK04 | 1.000 | 0.000 | 1.000 | 0.000 | 0.978 | 0.005 | 0.767 | 0.038 |
| SDMK05 | 0.833 | 0.003 | 1.000 | 0.000 | 0.725 | 0.060 | 0.433 | 0.063 |
| SDMK06 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| SDMK07 | 0.983 | 0.000 | 1.000 | 0.000 | 0.767 | 0.144 | 0.800 | 0.044 |
| SDMK08 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 0.967 | 0.000 |
| SDMK09 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| SDMK10 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| SDMK11 | 0.927 | 0.002 | 1.000 | 0.000 | 0.888 | 0.010 | 0.967 | 0.000 |
| SDMK12 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| SDMK13 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| SDMK14 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| SDMK15 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| SDMK16 | 0.589 | 0.062 | 1.000 | 0.000 | 0.261 | 0.305 | 0.667 | 0.084 |
| SDMK17 | 0.604 | 0.017 | 1.000 | 0.000 | 0.625 | 0.144 | 0.533 | 0.066 |
| SDMK18 | 0.678 | 0.032 | 1.000 | 0.000 | 0.843 | 0.047 | 1.000 | 0.000 |
| SDMK19 | 0.753 | 0.033 | 1.000 | 0.000 | 0.883 | 0.030 | 1.000 | 0.000 |
| SDMK20 | 0.808 | 0.029 | 0.967 | 0.000 | 0.921 | 0.027 | 1.000 | 0.000 |
| SDMK21 | 0.869 | 0.017 | 1.000 | 0.000 | 0.941 | 0.029 | 1.000 | 0.000 |
| SDMK22 | 0.910 | 0.041 | 1.000 | 0.000 | 0.972 | 0.037 | 1.000 | 0.000 |
| SDMK23 | 0.937 | 0.030 | 1.000 | 0.000 | 0.994 | 0.000 | 1.000 | 0.000 |
| SDMK24 | 0.934 | 0.012 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| SDMK25 | 0.946 | 0.010 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 |

![img-12.jpeg](img-12.jpeg)

Fig. 12. C-metrics of EDA-TS and compared algorithms.
current non-dominated solutions from both the EDA and TS components. Once the EDA component completes its execution, the nondominated solutions pool updates based on its results. One of the nondominated solutions is then chosen as the initial solution for the TS component. Then, after the TS component executes, the non-dominated solutions pool updates again based on the TS results. The current nondominated solutions are then used by the EDA component for sampling to generate a new population. Upon reaching the iteration stop criterion, the solutions in the current non-dominated solutions pool are output as the optimal solutions. The implementation of the nondominated solutions memory mechanism is shown in Fig. 8.

### 4.6. Algorithm framework

The framework of the EDA-TS algorithm is shown in Fig. 9. There are seven parameters in the EDA-TS algorithm: $T_{\max }, \alpha, \beta, \gamma, \mu$, popsize, and $\varepsilon$. Where $T_{\max }$ is the startup times of the TS module in each iteration, $\alpha, \beta$,
and $\gamma$ are the learning rate of the probability matrices, $\mu$ is the elite rate, popsize is the scale of population, and $\varepsilon$ is the penalty factor.

The EDA-TS mainly includes the EDA and TS components. The EDA component involves initializing probability matrices, generating population, fast non-dominated sorting, elite selection, and updating probability matrices. Meanwhile, the TS component includes selecting an initial solution, generating neighborhood solutions, fast non-dominated sorting, and updating the current solution, tabu list, and optimal solution. After each iteration, both components utilize a non-dominated solutions memory mechanism to update the non-dominated solution set.

## 5. Experiment and discussion

To evaluate the performance of the EDA-TS algorithm for the SMDFJSP, we assigned some compared experiments. All algorithms were executed in Python3 on a computer equipped with an inter ${ }^{\circledR}$ i7 3.6 GHz and $4 \times 8$ GB RAM processor.

![img-13.jpeg](img-13.jpeg)

Fig. 13. Pareto-optimal front chart of comparison experiment.

### 5.1. Performance metrics

In this study, we adopted three prevailing metrics to compare the performance of the algorithms, including the generational distance (GD) (Wang et al., 2020), the inverted generational distance (IGD) (Luo et al., 2020; Wang et al., 2020), and coverage of two sets (C-metric) (Peng et al., 2022). The true Pareto-optimal front ( $\mathrm{PF}_{\text {true }}$ ) for the test problem was composed of the solutions in the net non-dominated Pareto $\left(\mathrm{PF}_{\text {known }}\right)$ obtained by all test algorithms. Detailed introduction and computation of these metrics are given as follows.
(1) The GD(A) is a metric to evaluate the convergence of the A algorithm, which represents the distance from each solution in the set of the first Pareto front obtained by the A algorithm $\left(\mathrm{PF}_{\mathrm{A}}\right)$ to $\mathrm{PF}_{\text {true }}$. It is formulated as Eq. (34).
$G D(A)=\frac{\sqrt{\sum_{i=1}^{n} d_{i}^{2}}}{p}$
where $p$ is the number of points in $\mathrm{PF}_{\mathrm{A}}, d_{i}$ is the Euclidean distance from the $i$ th point of the $\mathrm{PF}_{\mathrm{A}}$ to the nearest point of the $\mathrm{PF}_{\text {true }}$. The smaller the $\mathrm{GD}(\mathrm{A})$ value, the better the performance of the A algorithm.
(2) The IGD(A) can evaluate the convergence and diversity of the algorithm at the same time. It indicates the Euclidean distance from the $\mathrm{PF}_{\text {true }}$ to the $\mathrm{PF}_{\mathrm{A}}$. It is formulated as Eq. (35).
$I G D(A)=\frac{\sum_{i=1}^{n}\left|d_{i}^{2}\right|}{p^{2}}$
where $p^{*}$ is the number of points in $\mathrm{PF}_{\text {true }}, d_{i}{ }^{*}$ is the Euclidean distance from the $i$ th point of the $\mathrm{PF}_{\text {true }}$ to the nearest point of the $\mathrm{PF}_{\mathrm{A}}$. The smaller the $\operatorname{IGD}(\mathrm{A})$ value, the better the performance of the A algorithm.
(3) C-metric (A, B) represents the percentage of solutions in A that dominated solutions in B. It is formulated as Eq. (36):
$C(A, B)=\frac{|\{b \in B ; \exists a \in A: a \geqslant b\}|}{|B|}$
where $|B|$ is the number of solutions in B . If $\mathrm{C}(\mathrm{A}, \mathrm{B})>\mathrm{C}(\mathrm{B}, \mathrm{A})$, the quality of solutions in A is better than that in B. Especially, $\mathrm{C}(\mathrm{A}, \mathrm{B})=1$ means that some solutions in A dominated all solutions in B.

### 5.2. Experiment instances

In this section, we have three sets of instances. The first set is employed to validating the accuracy of the SM-DFJSP model in section 5.4. These instances, denoted as G01, G02, and G03. Where the number of supply-demand types is $X=\{2,3\}$, the number of jobs is $N=\{6,8$, 10), the number of SRUs is $R=\{3,4,4\}$, the number of machines in each SRU is randomly determined within the range (Wang et al., 2021; Zhang et al., 2019), the number of operations in each job is randomly determined within the range (Rozman et al., 2021; Wang et al., 2002), the processing time of each operation is randomly determined within the range (Zhang et al., 2019; He and Qian, 2020).

The remaining two sets of instances are used for the experiments in sections 5.5 and 5.6. The second set, named SDMK01-15, extends the classical benchmarks MK1-15 proposed by Brandimarte (Brandimarte, 1993), featuring two types of jobs and SRUs $(X=2)$ with $R=\{3,4\}$.

The third set SDMK16-25 comprises ten instances generated by us. For this set, the number of supply-demand types is $X=\{3,4,5,6,7\}$, and the number of jobs is $N=\{25,40,50,60,80,90,100\}$, and the number of SRUs is $R=\{5,8,10,12,15\}$. Other data settings mirror those of the first set of instances. These instances provide further verification of the proposed algorithm's performance in solving SM-DFJSP across different scales.

Across all instance groups, the processing cost per unit time, transportation time, and transportation cost per unit time are randomly generated within the intervals (Zhang et al., 2019; He and Qian, 2020); (Zhang et al., 2019; Tang et al., 2016), and (Yu et al., 2020; Rozman

![img-14.jpeg](img-14.jpeg)

Fig. 14. Gantt chart of a solution of SDMK05.
et al., 2021), respectively.

### 5.3. Experiment parameters

In this paper, the $T_{\max }$ is set to 10 . Then remain parameters of EDATS are determined by orthogonal tests using the Taguchi method of design of experiments (Zheng and Wang, 2015). Six parameters: $\alpha ; \beta, \gamma$, $\mu$, popsize, and $\varepsilon$, are considered, with each parameter having five levels, as presented in Table 3. The parameters of each experiment are combined according to the orthogonal table L2S $\left(5^{\circ}\right)$, as shown in Table 4. Every parameter combination is independently run 30 times, with each run lasting 100 s , using instance SDMK17.

We select the objectives deviation sum (ODS) (Luo et al., 2020) as an indicator to evaluate two objectives accurately. The smaller ODS, the better the experimental effect. The ODS is computed using Eq. (37). Where the $i_{n}$ is the total number of solutions in the Pareto-optimal front based on the $t$ th combination, the $o b j_{j n}$ is the $j$ th value of objectives in the $n$th solution.
$O D S_{i}=\sum_{j=1}^{7} \frac{o b j_{j n}}{} \frac{-\min \left\{o b j_{j n} \mid n=1,2, \ldots, i_{n}\right\}}{\min \left\{o b j_{j n} \mid n=1,2, \ldots, i_{n}\right\}}, i=1,2, \ldots, 25$
Table 4 shows the experimental results of parameters. Moreover,

Fig. 10 illustrates the trend of the relationship between factor levels and the average ODS value (avg_ODS) of running 30 times. According to Fig. 10, we set the combination of the parameters for EDA-TS as follows: $\alpha=0.5, \beta=0.5, \gamma=0.5, \mu=0.1$, popsize $=50, \varepsilon=0.008$.

### 5.4. Accuracy of the SM-DFJSP mathematical model

In order to verify the accuracy of the proposed SM-DFJSP model and algorithm, we use Gurobi solver (Xu et al., 2023; Lei et al., 2022) to solve the SM-DFJSP. For the first group of instances in section 5.2, we obtain solutions of solved by Gurobi solver with a time limit of 3600 s . In this section, the stop criterion of EDA-TS is 100 iterations. Gurobi solver adopts stratified sequencing method for multi-objective optimization. The solutions obtained by EDA-TS and Gurobi are shown in Table 5. The solutions of EDA-TS that are not dominated by the optimal solution of Gurobi are marked in bold.

As shown in Table 5, for G01 and G02, the non-dominant solutions obtained by EDA-TS includes the optimal solution obtained by Gurobi. For G03, although the optimal solution obtained by Gurobi is not in the non-dominated solutions of EDA-TS, some solutions of the EDA-TS are non-dominated with the optimal solutions. Therefore, it can be verified that the EDA-TS algorithm is effective for solving SM-DFJSP.

Table 9
Wilcoxon signed rank test comparing EDA-TS with EDA and NSGA-II.

| Instances | EDA-TS vs EDA |  |  |  |  |  | EDA-TS vs NSGA-II |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | GD |  |  | IGD |  |  | GD |  |  | IGD |  |  |
|  | Wm | $p$-value | w/m | Wm | $p$-value | w/m | Wm | $p$-value | w/m | Wm | $p$-value | w/m |
| SDMK01 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK02 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK03 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK04 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK05 | 1 | 6.28E-06 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK06 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK07 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK08 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK09 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK10 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK11 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK12 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK13 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK14 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK15 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK16 | 47 | 6.46E-04 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK17 | 13 | 9.07E-05 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK18 | 22 | 6.02E-05 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK19 | 11 | 1.90E-05 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK20 | 6 | 7.26E-06 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 2.56E-06 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK21 | 5 | 4.33E-06 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK22 | 3 | 9.31E-09 | $+$ | 1 | 3.73E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK23 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK24 | 1 | 3.73E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK25 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| $+\backslash-\backslash-$ |  | 25 $\cdot$ 0.0 |  |  | 25 $\cdot$ 0.0 |  |  | 25 $\cdot$ 0.0 |  |  | 25 $\cdot$ 0.0 |  |

Table 10
Wilcoxon signed rank test comparing EDA-TS with EDA-VNS and H-GA-TS.

| Instances | EDA-TS vs EDA-VNS |  |  |  |  |  | EDA-TS vs EDA-TS_no_ms |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | GD |  |  | IGD |  |  | GD |  |  | IGD |  |  |
|  | Wm | $p$-value | w/m | Wm | $p$-value | w/m | Wm | $p$-value | w/m | Wm | $p$-value | w/m |
| SDMK01 | 191 | 4.04E-01 | $=$ | 63 | 2.32E-04 | $+$ | 2 | 5.59E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK02 | 0 | 3.79E-06 | $+$ | 0 | 2.56E-06 | $+$ | 1 | 3.73E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK03 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK04 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 21 | 2.15E-05 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK05 | 7 | 3.54E-08 | $+$ | 0 | 1.86E-09 | $+$ | 47 | 9.85E-03 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK06 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK07 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 10 | 1.70E-05 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK08 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 2.56E-06 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK09 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK10 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK11 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 2.56E-06 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK12 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK13 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK14 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK15 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK16 | 182 | 3.09E-01 | $=$ | 7 | 3.54E-08 | $+$ | 34 | 1.96E-04 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK17 | 38 | 1.22E-05 | $+$ | 1 | 3.73E-09 | $+$ | 38 | 1.37E-03 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK18 | 6 | 2.61E-08 | $+$ | 1 | 3.73E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK19 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK20 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK21 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK22 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK23 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK24 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDMK25 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| $+\backslash-\backslash-$ |  | 23 $\cdot 2 \cdot 0$ |  |  | 25 $\cdot 0 \cdot 0$ |  |  | 25 $\cdot 0 \cdot 0$ |  |  | 25 $\cdot 0 \cdot 0$ |  |

### 5.5. Comparison experiment

To verify the performance of the EDA-TS algorithm, which is compared with EDA, NSGA-II (Deb et al., 2002), EDA-VNS (Du et al., 2021), and H-GA-TS (Xu et al., 2021). Due to these compared algorithms not being applied to SM-DFJSP, their parameters are determined by orthogonal tests. The factor levels of each parameter for each compared algorithm are set according to the corresponding studies, as shown in

Table 6. Where $c r$ and $m r$ respectively represent crossover rate and mutation rate, $t$ is the maximum number of iterations of TS in H-GA-TS, and other parameters are consistent with EDA-TS. The parameters of each experiment are combined separately according to the orthogonal table L16 $\left(4^{5}\right), L_{9}\left(3^{3}\right), L_{16}\left(4^{5}\right)$, and $L_{16}\left(4^{5}\right)$. Like the parameter experiment of EDA-TS, each parameter combination of every algorithm is independently run 30 times on instance SDMK17 and set the stop criterion to 100 s .

Table 11
Average GD and IGD of EDA-TS and the variants.

| Instances | avg_GD | avg_IGD | avg_IGD |
| :--: | :--: | :--: | :--: |
|  | EDA-TS | EDA-TS_no_m | EDA-TS_no_n |
| SDMK01 | 0.012 | 0.719 | 0.016 |
| SDMK02 | 0.012 | 0.785 | 0.033 |
| SDMK03 | 0.003 | 0.739 | 0.005 |
| SDMK04 | 0.007 | 0.706 | 0.010 |
| SDMK05 | 0.013 | 0.401 | 0.020 |
| SDMK06 | 0.004 | 0.777 | 0.004 |
| SDMK07 | 0.008 | 0.731 | 0.013 |
| SDMK08 | 0.007 | 0.538 | 0.009 |
| SDMK09 | 0.003 | 0.569 | 0.009 |
| SDMK10 | 0.003 | 0.636 | 0.009 |
| SDMK11 | 0.008 | 0.462 | 0.016 |
| SDMK12 | 0.006 | 0.480 | 0.009 |
| SDMK13 | 0.006 | 0.530 | 0.009 |
| SDMK14 | 0.003 | 0.542 | 0.009 |
| SDMK15 | 0.004 | 0.557 | 0.007 |
| SDMK16 | 0.021 | 0.419 | 0.035 |
| SDMK17 | 0.009 | 0.387 | 0.019 |
| SDMK18 | 0.005 | 0.414 | 0.018 |
| SDMK19 | 0.008 | 0.428 | 0.016 |
| SDMK20 | 0.008 | 0.416 | 0.013 |
| SDMK21 | 0.009 | 0.427 | 0.017 |
| SDMK22 | 0.013 | 0.402 | 0.018 |
| SDMK23 | 0.015 | 0.404 | 0.019 |
| SDMK24 | 0.008 | 0.430 | 0.012 |
| SDMK25 | 0.008 | 0.398 | 0.017 |

Table 12
Average C-metric of EDA-TS and the variants.

| Instances | EDA-TS vs. EDA- <br> TS_no_m |  | EDA-TS vs. EDA- <br> TS_no_n |  | EDA-TS vs. EDA- <br> TS_no_mn |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | C(A, B) | C(B, A) | C(A, B) | C(B, A) | C(A, B) | C(B, A) |  |
| SDMK01 | 1.000 | 0.000 | 0.505 | 0.356 | 1.000 | 0.000 |  |
| SDMK02 | 1.000 | 0.000 | 0.435 | 0.246 | 1.000 | 0.000 |  |
| SDMK03 | 1.000 | 0.000 | 0.549 | 0.351 | 1.000 | 0.000 |  |
| SDMK04 | 1.000 | 0.000 | 0.520 | 0.370 | 1.000 | 0.000 |  |
| SDMK05 | 1.000 | 0.000 | 0.573 | 0.329 | 1.000 | 0.000 |  |
| SDMK06 | 1.000 | 0.000 | 0.506 | 0.304 | 1.000 | 0.000 |  |
| SDMK07 | 1.000 | 0.000 | 0.537 | 0.375 | 1.000 | 0.000 |  |
| SDMK08 | 1.000 | 0.000 | 0.517 | 0.421 | 1.000 | 0.000 |  |
| SDMK09 | 1.000 | 0.000 | 0.623 | 0.263 | 1.000 | 0.000 |  |
| SDMK10 | 1.000 | 0.000 | 0.717 | 0.245 | 1.000 | 0.000 |  |
| SDMK11 | 1.000 | 0.000 | 0.594 | 0.329 | 1.000 | 0.000 |  |
| SDMK12 | 1.000 | 0.000 | 0.593 | 0.317 | 1.000 | 0.000 |  |
| SDMK13 | 1.000 | 0.000 | 0.540 | 0.315 | 1.000 | 0.000 |  |
| SDMK14 | 1.000 | 0.000 | 0.646 | 0.241 | 1.000 | 0.000 |  |
| SDMK15 | 1.000 | 0.000 | 0.557 | 0.318 | 1.000 | 0.000 |  |
| SDMK16 | 0.967 | 0.013 | 0.622 | 0.330 | 1.000 | 0.000 |  |
| SDMK17 | 1.000 | 0.000 | 0.574 | 0.303 | 1.000 | 0.000 |  |
| SDMK18 | 1.000 | 0.000 | 0.637 | 0.242 | 1.000 | 0.000 |  |
| SDMK19 | 1.000 | 0.000 | 0.628 | 0.239 | 1.000 | 0.000 |  |
| SDMK20 | 1.000 | 0.000 | 0.605 | 0.225 | 1.000 | 0.000 |  |
| SDMK21 | 1.000 | 0.000 | 0.574 | 0.244 | 1.000 | 0.000 |  |
| SDMK22 | 1.000 | 0.000 | 0.532 | 0.378 | 1.000 | 0.000 |  |
| SDMK23 | 1.000 | 0.000 | 0.591 | 0.286 | 1.000 | 0.000 |  |
| SDMK24 | 1.000 | 0.000 | 0.570 | 0.255 | 1.000 | 0.000 |  |
| SDMK25 | 1.000 | 0.000 | 0.520 | 0.377 | 1.000 | 0.000 |  |

According to avg_ODS values for each parameter combination, the trends of factor levels are shown in Fig. 11. According to Fig. 11, the parameters of the compared algorithms are set as follows: EDA $\mu=0.2$, $\alpha=0.5, \beta=0.2, \gamma=0.4$, popsize $=50$; NSGA-II popsize $=50, c r=0.7, m r$ $=0.3$; EDA-VNS $\mu=0.2, \alpha=0.5, \beta=0.2, \gamma=0.4$, popsize $=100$; H-GATS popsize $=50, c r=0.2, m r=0.02, t=40, \varepsilon=0.008$.

For fairness, the stopping criterion for each algorithm on each instance is the time required for 100 iterations of the EDA. The initial population of all algorithms is randomly generated. The encoding and decoding mode of the comparison algorithm follow the same approach
as that of the EDA-TS. Additionally, for the infeasible solutions that may arise during the crossover and mutation processes of NSGA-II and H-GATS, we have adopted the repair strategy of H-GA-TS to address them.

The run time and results of comparative experiments are given in Table 7 and Table 8. According to Table 7, the GD and IGD metrics of EDA-TS are superior to EDA, NSGA-II, EDA-VNS, and H-GA-TS in almost all instances in which the GD metric is slightly worse than EDA-VNS on SDMK16. Although the GD metric of EDA-TS on SDMK16 is worse than that of EDA-VNS, the IGD metric is still better than EDA-VNS. Thus, the solutions obtained by EDA-TS in all instances are superior to other compared algorithms in terms of convergence and distribution. In addition, the average C-metrics are shown in Table 8 with a box plot in Fig. 12, which implies the EDA-TS outperformed the compared algorithms in 25 instances.

For a more intuitive comparison between EDA-TS and other algorithms, we plotted the Pareto-optimal fronts obtained by each algorithm in a single run on SDMK05, SDMK14, SDMK19, and SDMK25. From Fig. 13, it can be clearly seen that the solutions obtained by the EDA-TS algorithm is generally superior to those of other algorithms. Moreover, Fig. 14 illustrates a Gantt chart based on the solution [4141, 86] from Fig. 13, showing the scheduling details of SM-DFJSP. The bars in Fig. 14 represent the processing time of the operations, marked as $J_{0}^{t}\left(O_{0, k}\right)$. The blue ${ }^{+\alpha}-{ }^{+\gamma}$ indicates the transportation time of the job after the completion of processing.

To reflect the performance difference between the proposed algorithm with the compared algorithms, the Wilcoxon sign-test (Wan et al., 2023) is conducted. The results of the Wilcoxon signed rank test between EDA-TS and the compared algorithms are shown in Table 9 and Table 10 at a $95 \%$ confidence level. In Table 9 and Table 10, we give the $W_{m}, p$ value, and win. Here, $W_{m}$ represents the minimum sum of ranks. If the win is ' + ', it indicates that EDA-TS performs significantly better than the compared algorithm. If the win is ' - ', it indicates that EDA-TS performs significantly worse than the compared algorithm. If the win is ' $=$ ', it indicates that there is no significant difference between EDA-TS and the compared algorithm. The p-values less than $5 \%$ are bolded. According to Tables 9 and 10, the EDA-TS significantly outperforms the compared algorithms in almost all instances and is not significantly worse than other algorithms. It can be verified that EDA-TS is more effective than other algorithms in solving SM-DFJSP.

![img-15.jpeg](img-15.jpeg)

Fig. 15. C-metrics of EDA-TS and the variants.

Table 13
Wilcoxon signed rank test comparing EDA-TS with the variants.

| Instances | EDA-TS vs. EDA-TS_no_m |  |  |  |  |  | EDA-TS vs. EDA-TS_no_n |  |  |  |  |  | EDA-TS vs. EDA-TS_no_mn |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Avg_GD |  |  | Avg_IGD |  |  | Avg_GD |  |  | Avg_IGD |  |  | Avg_GD |  |  | Avg_IGD |  |
|  | $W_{m}$ | $p$-value | win | $W_{m}$ | $p$-value | win | $W_{m}$ | $p$-value | win | $W_{m}$ | $p$-value | win | $W_{m}$ | $p$-value | win | $W_{m}$ | $p$-value | win |
| SDME01 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 149 | 8.79E-02 | $=$ | 167 | 1.84E-01 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME02 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 76 | 3.45E-02 | $+$ | 75 | 3.21E-02 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME03 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 115 | 1.45E-02 | - | 177 | 2.62E-01 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME04 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 158 | 1.29E-01 | $=$ | 166 | 1.77E-01 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME05 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 125 | 2.62E-02 | $+$ | 174 | 2.37E-01 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME06 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 192 | 4.16E-01 | $=$ | 177 | 2.62E-01 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME07 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 138 | 5.23E-02 | $=$ | 142 | 6.36E-02 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME08 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 123 | 2.34E-02 | - | 164 | 1.64E-01 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME09 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 54 | 8.86E-05 | $+$ | 115 | 1.45E-02 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME10 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 51 | 6.29E-05 | $+$ | 46 | 3.45E-05 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME11 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 88 | 2.19E-03 | $+$ | 52 | 7.06E-05 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME12 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 148 | 8.41E-02 | $=$ | 151 | 9.61E-02 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME13 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 151 | 9.61E-02 | $=$ | 90 | 2.56E-03 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME14 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 21 | 8.33E-07 | $+$ | 26 | 1.99E-06 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME15 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 120 | 1.97E-02 | - | 57 | 1.23E-04 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME16 | 1 | 3.73E-09 | $+$ | 0 | 1.86E-09 | $+$ | 51 | 6.29E-05 | $+$ | 37 | 9.50E-05 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME17 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 107 | 8.71E-03 | $+$ | 112 | 1.20E-02 | - | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME18 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 15 | 2.55E-07 | $+$ | 94 | 3.48E-03 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME19 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 102 | 6.19E-03 | $+$ | 55 | 9.90E-05 | - | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME20 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 73 | 6.08E-04 | $+$ | 71 | 5.05E-04 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME21 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 105 | 7.61E-03 | $+$ | 48 | 4.41E-05 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME22 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 186 | 3.49E-01 | $=$ | 137 | 4.97E-02 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME23 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 122 | 2.21E-02 | $+$ | 143 | 6.67E-02 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME24 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 82 | 1.34E-03 | $+$ | 36 | 9.22E-06 | $+$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| SDME25 | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ | 123 | 2.34E-02 | $+$ | 140 | 5.77E-02 | $=$ | 0 | 1.86E-09 | $+$ | 0 | 1.86E-09 | $+$ |
| $+\backslash=\backslash$ | 25 | 25 |  |  | 25 | 25 | 15 |  |  | 13 | 10 |  |  | 25 | 25 |  |  | 25 | 25 |

Table 14
Details of jobs and SRUs categorized by supply and demand type $\mathrm{X}=1$.

|  |  | U $_{1}^{1}$ | $\mathrm{M}_{1,1}$ | $\mathrm{M}_{1,2}$ | $\mathrm{M}_{1,3}$ | $\mathrm{M}_{1,4}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\mathrm{O}_{1,1}$ | J $_{1}^{1}$ | $(8,4)$ | $(6,2)$ | $(7,3)$ | $(2,2)$ | $(5,3)$ |
| $\mathrm{O}_{1,2}$ |  |  | $(5,3)$ | $(5,4)$ | $(3,2)$ | $(5,4)$ |
| $\mathrm{O}_{1,3}$ |  |  | $(7,2)$ | $(4,2)$ | $(6,2)$ | $(8,4)$ |
| $\mathrm{O}_{1,4}$ |  |  | $(2,3)$ | $(2,4)$ | $(6,4)$ | $(4,2)$ |
| $\mathrm{O}_{3,1}$ | J $_{3}^{1}$ | $(9,5)$ | $(3,3)$ | $(8,3)$ | $(8,3)$ | $(2,3)$ |
| $\mathrm{O}_{3,2}$ |  |  | $(3,2)$ | $(7,3)$ | $(3,2)$ | $(7,2)$ |
| $\mathrm{O}_{3,3}$ |  |  | $(2,3)$ | $(3,4)$ | $(6,2)$ | $(5,4)$ |
| $\mathrm{O}_{3,4}$ |  |  | $(2,2)$ | $(5,3)$ | $(7,3)$ | $(8,4)$ |
| $\mathrm{O}_{4,5}$ |  |  | $(2,2)$ | $(4,3)$ | $(5,3)$ | $(2,3)$ |
| $\mathrm{O}_{6,1}$ | J $_{6}^{1}$ | $(4,4)$ | $(3,2)$ | $(5,4)$ | $(7,2)$ | $(5,4)$ |
| $\mathrm{O}_{6,2}$ |  |  | $(5,4)$ | $(8,2)$ | $(2,4)$ | $(3,2)$ |
| $\mathrm{O}_{6,3}$ |  |  | $(3,2)$ | $(3,2)$ | $(2,3)$ | $(4,3)$ |
| $\mathrm{O}_{6,4}$ |  |  | $(6,4)$ | $(5,2)$ | $(8,2)$ | $(5,3)$ |
| $\mathrm{O}_{7,1}$ | J $_{7}^{1}$ | $(7,5)$ | $(4,2)$ | $(6,3)$ | $(4,4)$ | $(2,4)$ |
| $\mathrm{O}_{7,2}$ |  |  | $(2,2)$ | $(6,3)$ | $(7,3)$ | $(7,3)$ |
| $\mathrm{O}_{7,3}$ |  |  | $(8,3)$ | $(2,4)$ | $(6,4)$ | $(3,4)$ |
| $\mathrm{O}_{7,4}$ |  |  | $(6,2)$ | $(3,4)$ | $(4,3)$ | $(4,2)$ |
| $\mathrm{O}_{7,5}$ |  |  | $(2,3)$ | $(3,4)$ | $(3,2)$ | $(3,2)$ |
| $\mathrm{O}_{12,1}$ | J $_{12}^{1}$ | $(7,5)$ | $(3,4)$ | $(5,2)$ | $(8,2)$ | $(5,2)$ |
| $\mathrm{O}_{12,2}$ |  |  | $(8,2)$ | $(4,2)$ | $(5,2)$ | $(2,4)$ |
| $\mathrm{O}_{12,3}$ |  |  | $(8,2)$ | $(5,4)$ | $(7,3)$ | $(6,3)$ |
| $\mathrm{O}_{12,4}$ |  |  | $(3,3)$ | $(4,2)$ | $(6,3)$ | $(5,3)$ |
| $\mathrm{O}_{12,5}$ |  |  | $(6,3)$ | $(8,2)$ | $(6,3)$ | $(6,4)$ |

memory mechanism is adopted to obtain better solutions steadily. From a comprehensive perspective, these numerical experiments provide evidence that the multi-population strategy with dispatching rules and non-dominated solutions memory mechanism are beneficial for EDA-TS.

### 5.7. Case study

In this section, we consider applying the proposed algorithm to solve the SM-DFJSP within a mold-sharing manufacturing platform in China. This realistic case involves the processing of hot runner systems, mold frames, and other mold components. In general, different types of resource service units handle the processing of hot runners and other mold components. In this case, a batch of orders includes 15 jobs of the two types mentioned above, with 3 SRUs assigned to process these orders. The processing details of shared equipment for the primary operations of jobs are presented in Tables 14 and 15. The array in the cell corresponding to the job and SRU in these tables represents the transportation time and unit cost between the custom and the supplier. The array in the cell corresponding to the process and machine indicates
processing time and unit cost.
We compared the Pareto-optimal front obtained by EDA-TS with those of EDA, NSGA-II, EDA-VNS, and H-GA-TS. As shown in Fig. 16, the solutions obtained by EDA-TS are generally superior to those obtained by the other algorithms. Figs. 17 and 18 represent Gantt charts generated from the solution [2511, 79] provided by EDA-TS and a random solution [2594, 109] from Fig. 16, respectively. In these figures, the bars represent the processing time of the operation, and marked as $J_{6,6}^{e}(P)$, indicating the $k$ th operation of the $J_{6}^{e}$ and its processing time. The blue ${ }^{\text {** }}$ - ${ }^{* * *}$ indicates the transportation time of the job after the completion of processing. It can be seen, the arrangement in Fig. 17 is obviously more compact than that in Fig. 18, and the scheduling scheme in Fig. 18 can effectively shorten the total completion time while ensuring a lower cost.

## 6. Conclusions and future studies

In this study, we propose an SM-DFJSP model based on resource organization structure in sharedMfg, considering supply-demand matching in the scheduling process. A mathematical model aiming to minimizing total cost and makespan, was established to achieve distributed flexible scheduling in heterogeneous shared SRUs. To solve
![img-16.jpeg](img-16.jpeg)

Fig. 16. Pareto-optimal front chart of case study.

# Table 15 

Partial details of jobs and SRUs categorized by supply and demand type $\mathrm{X}=2$.

|  |  | U $_{1}^{2}$ | $\mathrm{M}_{2,1}$ | $\mathrm{M}_{2,2}$ | $\mathrm{M}_{2,3}$ | $\mathrm{M}_{2,4}$ | U $_{1}^{2}$ | $\mathrm{M}_{3,1}$ | $\mathrm{M}_{3,2}$ | $\mathrm{M}_{3,3}$ | $\mathrm{M}_{3,4}$ | $\mathrm{M}_{3,5}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\mathrm{O}_{2,1}$ | J $_{2}^{2}$ | $(7,6)$ | $(6,3)$ | $(15,4)$ | $(7,5)$ | $(23,3)$ | $(5,4)$ | $(11,5)$ | $(17,3)$ | $(18,4)$ | $(23,6)$ | $(6,5)$ |
| $\mathrm{O}_{2,2}$ |  |  | $(18,5)$ | $(16,4)$ | $(24,3)$ | $(24,6)$ |  | $(19,4)$ | $(20,4)$ | $(8,6)$ | $(12,3)$ | $(6,5)$ |
| $\mathrm{O}_{2,3}$ |  |  | $(3,5)$ | $(8,6)$ | $(3,5)$ | $(20,6)$ |  | $(21,6)$ | $(7,6)$ | $(5,5)$ | $(19,4)$ | $(6,5)$ |
| $\mathrm{O}_{2,4}$ |  |  | $(5,5)$ | $(13,6)$ | $(16,5)$ | $(19,6)$ |  | $(10,6)$ | $(24,5)$ | $(12,5)$ | $(3,6)$ | $(13,3)$ |
| $\mathrm{O}_{2,5}$ |  |  | $(21,4)$ | $(14,5)$ | $(5,6)$ | $(5,5)$ |  | $(6,4)$ | $(6,5)$ | $(21,4)$ | $(17,3)$ | $(6,5)$ |
| $\mathrm{O}_{2,6}$ |  |  | $(23,5)$ | $(20,6)$ | $(21,3)$ | $(17,6)$ |  | $(12,5)$ | $(4,6)$ | $(7,3)$ | $(13,3)$ | $(25,5)$ |
| $\mathrm{O}_{4,1}$ | J $_{4}^{2}$ | $(7,6)$ | $(14,3)$ | $(11,5)$ | $(14,6)$ | $(5,5)$ | $(9,4)$ | $(22,5)$ | $(19,6)$ | $(3,3)$ | $(25,3)$ | $(3,3)$ |
| $\mathrm{O}_{4,2}$ |  |  | $(9,4)$ | $(22,5)$ | $(17,3)$ | $(13,4)$ |  | $(22,5)$ | $(11,6)$ | $(16,5)$ | $(5,5)$ | $(6,6)$ |
| $\mathrm{O}_{4,3}$ |  |  | $(5,4)$ | $(14,3)$ | $(16,3)$ | $(19,3)$ |  | $(11,6)$ | $(11,6)$ | $(22,3)$ | $(11,5)$ | $(5,5)$ |
| $\mathrm{O}_{4,4}$ |  |  | $(23,3)$ | $(6,3)$ | $(15,6)$ | $(17,3)$ |  | $(3,4)$ | $(7,5)$ | $(6,3)$ | $(16,3)$ | $(14,6)$ |
| $\mathrm{O}_{4,5}$ |  |  | $(25,4)$ | $(16,6)$ | $(16,3)$ | $(14,5)$ |  | $(19,4)$ | $(24,4)$ | $(17,4)$ | $(19,6)$ | $(25,3)$ |
| $\mathrm{O}_{4,6}$ |  |  | $(24,3)$ | $(22,3)$ | $(4,4)$ | $(11,4)$ |  | $(3,5)$ | $(7,4)$ | $(9,3)$ | $(24,3)$ | $(16,4)$ |
| $\mathrm{O}_{4,7}$ |  |  | $(10,5)$ | $(18,4)$ | $(12,4)$ | $(21,6)$ |  | $(11,4)$ | $(25,3)$ | $(18,3)$ | $(14,3)$ | $(9,6)$ |
| $\mathrm{O}_{15,1}$ | J $_{5}^{1}$ | $(9,4)$ | $(13,3)$ | $(21,3)$ | $(6,6)$ | $(17,5)$ | $(4,5)$ | $(21,4)$ | $(8,5)$ | $(7,6)$ | $(20,5)$ | $(8,6)$ |
| $\mathrm{O}_{15,2}$ |  |  | $(6,6)$ | $(8,3)$ | $(11,6)$ | $(7,5)$ |  | $(20,5)$ | $(4,3)$ | $(21,6)$ | $(4,5)$ | $(17,4)$ |
| $\mathrm{O}_{15,3}$ |  |  | $(20,3)$ | $(10,6)$ | $(24,4)$ | $(14,5)$ |  | $(17,4)$ | $(19,4)$ | $(23,3)$ | $(4,4)$ | $(20,4)$ |
| $\mathrm{O}_{15,4}$ |  |  | $(15,6)$ | $(25,4)$ | $(17,6)$ | $(25,5)$ |  | $(3,3)$ | $(5,4)$ | $(22,4)$ | $(17,6)$ | $(21,6)$ |
| $\mathrm{O}_{15,5}$ |  |  | $(14,3)$ | $(23,4)$ | $(12,5)$ | $(17,3)$ |  | $(3,4)$ | $(15,5)$ | $(25,4)$ | $(12,5)$ | $(21,4)$ |
| $\mathrm{O}_{15,6}$ |  |  | $(7,6)$ | $(10,5)$ | $(6,6)$ | $(19,4)$ |  | $(15,5)$ | $(8,6)$ | $(23,5)$ | $(16,5)$ | $(19,5)$ |
| $\mathrm{O}_{15,7}$ |  |  | $(16,3)$ | $(21,6)$ | $(22,5)$ | $(20,5)$ |  | $(10,6)$ | $(20,5)$ | $(17,5)$ | $(6,3)$ | $(13,4)$ |

![img-17.jpeg](img-17.jpeg)

Fig. 17. Gantt chart of a solution obtained by EDA-TS.
![img-18.jpeg](img-18.jpeg)

Fig. 18. Gantt chart of a random solution.

SM-DFJSP, we proposed a hybrid EDA-TS algorithm with a multipopulation strategy and a non-dominated solutions memory mechanism. To verify the performance of EDA-TS, we compared it with Gurobi solver, EDA, NSGA-II, EDA-VNS, and H-GA-TS. Using Gurobi to solve SM-DFJSP, we verify the accuracy of the model. By comparing the results of EDA-TS with those of the Gurobi solver, we confirm the effectiveness of the proposed algorithm. And the results of the comparative experiments proved that the proposed EDA-TS algorithm has significant advantages in solving SM-DFJSP. And, the results of the ablation experiment validated that the multi-population strategy and nondominated solutions memory mechanism significantly enhance the performance of the proposed algorithm. Finally, we applied the proposed algorithm to solve the SM-DFJSP with a mold-sharing manufacturing platform in China. This validated the practicality of both the proposed algorithm and model.

In the future, we plan to explore real-time scheduling based on sharedMfg. Due to digital Twining and industrial internet technology, capturing the real-time state of production equipment has become more convenient. It would be very interesting to carry out dynamic scheduling on sharedMfg based on these technologies.

## CRediT authorship contribution statement

Guangyan Wei: Writing - original draft, Validation, Software, Methodology, Investigation, Data curation. Chunming Ye: Conceptualization, Funding acquisition, Supervision, Resources. Jianning Xu: Writing - review \& editing, Methodology, Formal analysis.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This work was supported in part by the National Natural Science Foundation of China under Grant (No. 71840003) and Scientific and Innovative Action Plan of Shanghai under Grants (No. 20692104300).

## References

M. F. Amiri, J. Behnamian, Multi-objective green flowdrop scheduling problem under uncertainty: Estimation of distribution algorithm, Journal of Cleaner Production 251 (2020). doi: 10.1016/j. j clepro. 2019. 119734.

Brandimarte, P. (1993). Routing and scheduling in a flexible job shop by tabu search. Annals of Operations Research, 41, 157-183.
Chang, H.-C., \& Liu, T.-K. (2017). Optimisation of distributed manufacturing flexible job shop scheduling by using hybrid genetic algorithms. Journal of Intelligent Manufacturing, 28(8), 1973-1986. https://doi.org/10.1007/s10845-015-1084-y Cheng, Y., Xie, Y., Wang, D., Gao, F., \& Ji, P. (2021). Manufacturing services scheduling with supply-demand dual dynamic uncertainties toward industrial internet platforms. IEEE Transactions on Industrial Informatics, 17(5), 2997-3018. https://doi. org/10.1109/TIJ. 2020. 3004248
Dang, Q., Guo, W., \& Gong, M. (2022). An efficient mixture sampling model for gaussian estimation of distribution algorithm. Information Sciences, 608, 1157-1182. https:// doi.org/10.1016/j.iss.2022.07.016
Deh, K., Pratap, A., Agarwal, S., \& Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm: Nega-ti. IEEE Transactions on Evolutionary Computation, 6(2), 182-197. https://doi.org/10.1109/4235.996017
Y. Du, J.-q. Li, C. Lan, L.-I. Meng, A hybrid estimation of distribution algorithm for distributed flexible job shop scheduling with crane transportations, Swarm and Evolutionary Computation 62 (AP8 2021). doi: 10. 1016/ j. swwo. 2021. 100861.
J. Duan, J. Wang, Energy-efficient scheduling for a flexible job shop with machine breakdowns considering machine idle time arrangement and machine speed level selection, Computers \& Industrial Engineering 161 (2021). doi: 10.1016/j. cie. 2021.107677

Fang, H., Zhou, A., \& Zhang, H. (2018). Information fusion in offspring generation: A case study in de and eda. Swarm and evolutionary computation, 42, 99-108. https:// doi.org/10.1016/j.swwo.2018.02.014
Gao, S., \& de Silva, C. W. (2018). Estimation distribution algorithms on constrained optimization problems. Applied Mathematics and Computation, 339, 323-345. https:// doi.org/10.1016/j.amc.2018.07.037
X. Hao, M. Gen, L. Lin, G. A. Suer, Effective multiobjective eda for bi-criteria stochastic job-shop scheduling problem, Journal of intelligent manufacturing 28 (3, 51) (2017) 833-845, 13th International conference on information and management sciences (IMS), Zhangjiajie, PEOPLES \& CHINA, AUG 03-08, 2014. doi: 10.1007 /s10845-014-1026-0.

He, L., \& Qian, Z. (2020). Intent-based resource matching strategy in cloud. Information Sciences, 538, 1-18. https://doi.org/10.1016/j.iss.2020.05.045
Hu, Y., Zhu, F., Zhang, L., Lai, Y., \& Wang, Z. (2019). Scheduling of manufacturers based on chaos optimization algorithm in cloud manufacturing. Robotics and ComputerIntegrated Manufacturing, 58, 13-20. https://doi.org/10.1016/j.rcim.2019.01.010 Huo, Y., Xiong, J., Guo, Z., Wenjun, X., \& Lei, L. (2022). A collaboration approach for cloud factories based on kubo-munkras algorithm. International Journal of Computer Integrated Manufacturing, 25(9), 972-988. https://doi.org/10.1080/ 09511925.2022.2027021
Jiang, P., \& Ding, K. (2018). Analysis of personalized production organizing and operating mechanism in a social manufacturing environment. Proceedings of the Institution of Mechanical Engineers, Part b: Journal of Engineering Manufacture, 232(14), 2670-2676. https://doi.org/10.1177/0954405417609016
Lei, K., Guo, P., Zhao, W., Wang, Y., Qian, L., Meng, X., \& Tang, L. (2022). A multi-action deep reinforcement learning framework for flexible job-shop scheduling problem. Expert Systems with Applications, 205, Article 117796. https://doi.org/10.1016/j. eewa.2022.117796
Li, X., Fang, Z., \& Yin, C. (2020). A machine tool matching method in cloud manufacturing using markov decision process and cross-entropy. Robotics and Computer-Integrated Manufacturing, 65. https://doi.org/10.1016/j.rcim.2020.101968
Li, H., Wang, X., \& Yang, J. (2022). A hybrid differential evolution algorithm for flexible job shop scheduling with out-sourcing operations and job priority constraints. Expert Systems with Applications, 201. https://doi.org/10.1016/j.ewaa.2022.117182
Liang, H., Wen, X., Liu, Y., Zhang, H., Zhang, L., \& Wang, L. (2021). Logistics-involved qos-aware service composition in cloud manufacturing with deep reinforcement learning. Robotics and Computer-Integrated Manufacturing, 67. https://doi.org/ 10.1016/j.rcim.2020.101951

Lin, C.-S., Li, P.-Y., Wei, J.-M., \& Wu, M.-C. (2020). Integration of process planning and scheduling for distributed flexible job shops. Computers \& Operations Research, 124. https://doi.org/10.1016/j.cor.2020.105053
Y. Liu, L. Zhang, F. Tan, L. Wang, Resource service sharing in cloud manufacturing based on the gain-slugley algorithm: Advantages and challenge, International Journal of Computer Integrated Manufacturing 30 (4-5, 51) (2017) 420-432. doi: 10.1080/ 09511925.2015.1067916.

Liu, H., et al., H. Liu, F. Zhao, L. Wang, J. Cao, J. Tang, Jonrinaldi, An estimation of distribution algorithm with multiple intensification strategies for two-stage hybrid flow-shop scheduling problem with sequence-dependent setup time, Applied Intelligence 53 (5) (2023) 5160-5178. doi: 10.1007/s10489-022-03853-1
Liu, B., Fan, Y., \& Liu, Y. (2015). A fast estimation of distribution algorithm for dynamic fuzzy flexible job-shop scheduling problem. Computers \& Industrial Engineering, 87, 193-201. https://doi.org/10.1016/j.cie.2015.04.029
Liu, Z., Guo, S., Wang, L., Du, B., \& Pang, S. (2019). A multi-objective service composition recommendation method for individualized customer: Hybrid mpa-guidon model. Computers \& Industrial Engineering, 128, 122-134. https://doi.org/ 10.1016/j.cie. 2018.12.042

Liu, Z.-H., Wang, Z.-J., \& Yang, C. (2019). Multi-objective resource optimization scheduling based on iterative double auction in cloud manufacturing. Advances in Manufacturing, 7(4), 374-388. https://doi.org/10.1007/s40436-019-00281-2

Logendran, R., McDonell, B., \& Smucker, B. (2007). Scheduling unrelated parallel machines with sequence-dependent setup. Computers \& Operations Research, 34(11), 3420-3438. https://doi.org/10.1016/j. cor. 2006. 02. 006
Lu, P.-H., Wu, M.-C., Tan, H., Peng, Y.-H., \& Chen, C.-F. (2018). A genetic algorithm embedded with a concise chroma-some representation for distributed and flexible job-shop scheduling problems. Journal of Intelligent Manufacturing, 29(1), 19-34. https://doi.org/10.1007/s10845-015-1083-z
Luo, Q., Deng, Q., Gong, G., Zhang, L., Han, W., \& Li, K. (2020). An efficient memetic algorithm for distributed flexible job shop scheduling problem with transfers. Expert Systems with Applications, 160. https://doi.org/10.1016/j. eewa.2020.113721
Luo, S., Zhang, L., \& Fan, Y. (2021). Dynamic multi-objective scheduling for flexible job shop by deep reinforcement learning. Computers \& Industrial Engineering, 159, Article 107489. https://doi.org/10.1016/j.ict. 2021.107489
S. Mahmud, A. Abbasi, R. K. Chakrabortty, M. J. Ryan, Multi-operator communication based differential evo- lution with sequential tabu search approach for job shop scheduling problems, Applied Soft Computing 108 (SEP 2021). doi:10.1016/j. asoc. 2021.107470
J. P. Martins, A. C. B. Delbem, Pairwise independence and its impact on estimation of distribution algorithms, Swarm and evolutionary computation 27 (2016) 80 96. doi: 10. 1016/j. swevo. 2015. 10. 001.

Meng, L., Zhang, C., Ren, Y., Zhang, B., \& Lv, C. (2020). Mixed-integra linear programming and constraint programming formulations for solving distributed flexible job shop scheduling problem. Computers \& Industrial Engineering, 142, Article 106347. https://doi.org/10.1016/j.cie.2020.106347
Muelin, S., Pena, J.-M., LaTorre, A., \& Robles, V. (2011). A new initialization procedure for the distributed estimation of distribution algorithms. Soft Computing, 15(4), 713-720. https://doi.org/10.1007/s00500-010-06653-1
M. M. Nasiri, F. Kianfar, A gns to algorithm for the job shop scheduling, Computers \& Industrial Engineering 62 (4) (2012) 946 952. doi: 10.1016/j. cie. 2011.12. 018. Nasiri, M., Bekrar, A., Jernai, A., Niar, S., \& Ammari, A. C. (2018). An effective and distributed particle swarm optimization algorithm for flexible job-shop scheduling problem. Journal of Intelligent Manufacturing, 29(3), 603-615. https://doi.org/ 10.1007/s10845-015-1039-3
Oukil, A., El-Bouri, A., \& Emrouznejad, A. (2022). Energy-aware job scheduling in a multi-objective production environment - an integrated qos-awa model. Computers \& Industrial Engineering, 168, Article 108065. https://doi.org/10.1016/j. cie. 2022.108065
D. Peng, C. Ye, M. Wan, A multi-objective improved novel discrete particle swarm optimization for emergency resource center location problem, Engineering Applications of Artificial Intelligence 111 (MAY 2022). doi: 10. 1016/j. engappai. 2022. 104725.

Perez-Rodriguez, R., Joens, S., Hernandes-Aguirre, A., \& Alberto-Ochoa, C. (2014). Simulation optimization for a flexible jobshop scheduling problem using an estimation of distribution algorithm. International Journal of Advanced Manufacturing Technology, 73(1-4), 3-21. https://doi.org/10.1007/s00170-014-5759-z
Rozman, N., Diaci, J., \& Corn, M. (2021). Scalable framework for blockchain-based shared manufacturing. Robotics and Computer-Integrated Manufacturing, 71. https:// doi.org/10.1016/j.rcim.2021.102159
Sahman, M. A. (2021). A discrete spotted hyena optimizer for solving distributed job shop scheduling problems. Applied Soft Computing, 106. https://doi.org/10.1016/j. asoc. 2021.107349
Y. Sang, J. Tan, Intelligent factory many-objective distributed flexible job shop collaborative scheduling method, Computers \& Industrial Engineering 164 (2022). doi: 10. 1016/ j. cie. 2021. 107884.
D. Tang, M. Dai, M. A. Salido, A. Giret, Energy-efficient dynamic scheduling for a flexible flow shop using an -improved particle swarm optimization, Computers in industry 81 (SI) (2016) 82 95. doi: 10. 1016/ j. compind. 2015.10. 001.
F. Tao, J. Cheng, Y. Cheng, S. Gu, T. Zheng, H. Yang, Sdmsim: A manufacturing service supply-demand matching simulator under cloud environment, Robotics and Computer-Integrated Manufacturing 45 (SI) (2017) 34-46. doi: 10.1016/j. scim. 2016.07.001.
Tay, J. C., \& Hu, N. B. (2008). Evolving dispatching rules using genetic programming for solving multi-objective flexible job-shop problems. Computers \& Industrial Engineering, 34(3), 453-470. https://doi.org/10.1016/j.cie.2007.08.004.
Turkylilmaz, A., Senvar, O., Unal, I., \& Bulkan, S. (2020). A research survey: heuristic approaches for solving multi objective flexible job shop problems. Journal of Intelligent Manufacturing, 31(8), 1949-1983. https://doi.org/10.1007/s10845-020-01547-4
Tzeng, Y.-R., Chen, C.-L., \& Chen, C.-L. (2012). A hybrid ada with car for solving permutation flow shop school-i-tig. International Journal of Advanced Manufacturing Technology, 60(9-12), 1139-1147. https://doi.org/10.1007/s00170-011-3671-1
Utamina, A. (2021). A comparative study of hybrid estimation distribution algorithms in solving the facility layout problem. Egyptian Informatics Journal, 22(4), 505 513. https://doi.org/10.1016/j.efj.2021.04.002
M. Wan, C. Ye, D. Peng, Multi-period dynamic multi-objective emergency material distribution model under uncertain demand, Engineering Applications of Artificial Intelligence 117 (A) (2023). 10.1016/j.engappai.2022.105530
Z. Wang, Q. Deng, L. Zhang, X. Liu, (2002). Integrated scheduling of production, inventory and imperfect maintenance based on mutual feedback of supplier and demander in distributed environment, Journal of Intelligent Manufacturing, 10.1007/s10845-022-01996-z.

G. Wang, L. Gao, X. Li, P. Li, M. F. Tsegetiren, Energy-efficient distributed permutation flow shop scheduling problem using a multi-objective whale swarm algorithm, Swarm and Evolutionary Computation 57 (SEP 2020). doi: 10. 1016/ j. swevo. 2020.100716

J. Wang, Y. Liu, S. Ren, C. Wang, W. Wang, Evolutionary game based real-time scheduling for energy-efficient distributed and flexible job shop, Journal of Cleaner Production 293 (2021) doi: 10. 1016/ j. j clepro. 2021. 126093.
Wang, H., Peng, T., Nassehi, A., \& Tang, R. (2023). A data-driven simulationoptimization framework for generating priority dispatching rules in dynamic job shop scheduling with uncertainties. Journal of Manufacturing Systems, 70, 288-308. https://doi.org/10.1016/j.jmsy.2023.08.001
Wang, S.-Y., Wang, L., Liu, M., \& Xu, Y. (2013). An enhanced estimation of distribution algorithm for solving hybrid flow-shop scheduling problem with identical parallel machines. International Journal of Advanced Manufacturing Technology, 68(9-12), 2043-2056. https://doi.org/10.1007/s00179-013-6819-y
Wang, G., Zhang, G., Guo, X., \& Zhang, Y. (2021). Digital twin-driven service model and optimal allocation of manufacturing resources in shared manufacturing. Journal of Manufacturing Systems, 59, 165-179. https://doi.org/10.1016/j.jmsy.2021.02.008
Wu, M., Yang, D., Zhou, B., Yang, Z., Liu, T., Li, L., Wang, Z., \& Hu, K. (2021). Adaptive population mega-iii with dual control strategy for flexible job shop scheduling problem with the consideration of energy consumption and weight. Machines, 9(12). https://doi.org/10.3390/machines9120344
Xiang, N., Dou, Y., Xia, B., Yang, K., \& Tan, Y. (2022). High-end equipment: An improved two-sided based sskm matching and a novel pareto refining method considering consistency. Expert Systems with Applications, 202. https://doi.org/10.1016/j. eswa.2022.117175
Xie, J., Li, X., Gao, L., \& Gui, L. (2023). A hybrid genetic tabu search algorithm for distributed flexible job shop scheduling problems. Journal of manufacturing systems, 71, 82-94. https://doi.org/10.1016/j.jmsy.2023. 09.002
Xiong, W., \& Fu, D. (2018). A new immune multi-agent system for the flexible job shop scheduling problem. Journal of Intelligent Manufacturing, 29(4), 857-873. https://doi. org/10.1007/s10845-015-1137-2
Xu, G., Bao, Q., \& Zhang, H. (2023). Multi-objective green scheduling of integrated flexible job shop and automated guided vehicles. Engineering Applications of Artificial Intelligence, 126, Article 106864. https://doi.org/10.1016/j.engappai.2023.106864
Xu, W., Hu, Y., Luo, W., Wang, L., \& Wu, R. (2021). A multi-objective scheduling method for distributed and flexible job shop based on hybrid genetic algorithm and tabu search considering operation outsourcing and carbon emission. Computers \& Industrial Engineering, 157. https://doi.org/10.1016/j. cie.2021.107318
Xue, X., Wang, S., Jun Zhang, L., \& Yong Feng, Z. (2019). Evaluating of dynamic service matching strategy for social manufacturing in cloud environment. Future Generation Computer Systems, 91, 311-326. https://doi.org/10.1016/j.future.2018.08.028

Yu, C., Jiang, X., Yu, S., \& Yang, C. (2020). Blockchain-based shared manufacturing in support of cyber physical systems: Concept, framework, and operation. Robotics and Computer-Integrated Manufacturing, 64, Article 101931. https://doi.org/10.1016/j. rcim.2019.101931
Yu, C., Xu, X., Yu, S., Sang, Z., Yang, C., \& Jiang, X. (2020). Shared manufacturing in the sharing economy: concept, definition and service operations. Computers \& Industrial Engineering, 146, Article 106602. https://doi.org/10.1016/j. cie. 2020.106602
H. Zhang, U. Roy, A semantics-based dispatching rule selection approach for job shop scheduling, Journal of Intelligent Manufacturing 30 (7, SI) (2019) 27592779. doi: 10. 1007 /s10845-018-1421-z.

Zhang, J., Ding, G., Zou, Y., Qin, S., \& Fu, J. (2019). Review of job shop scheduling research and its new perspectives under industry 4.0. Journal of Intelligent Manufacturing, 30(4), 1809-1830. https://doi.org/10.1007/s10845-017-1350-2
Zhang, Z.-Q., Qian, R., Hu, R., Jin, H.-P., \& Wang, L. (2021). A matrix-cube-based estimation of distribution algorithm for the distributed assembly permutation flowshop scheduling problem. Swarm and Evolutionary Computation, 60. https://doi.org/ 10.1016/j.swarm.2020.100785

Zhang, L., Hu, Y., Wang, C., Tang, Q., \& Li, X. (2022). Effective dispatching rules mining based on near-optimal schedules in intelligent job shop environment. Journal of Manufacturing Systems, 63, 424-438. https://doi.org/10.1016/j.jmsy.2022.04.019
Zhao, F., Zhu, B., \& Wang, L. (2023). An estimation of distribution algorithm-based hyper-heuristic for the distributed assembly mixed no-idle permutation flowshop scheduling problem. IEEE Transactions on Systems, Man, and Cybernetics: Systems, 53 (9), 5626-5637. https://doi.org/10.1109/TSMC.2023.3272311
Q.-Q. Zheng, Y. Zhang, H.-W. Tian, I.-J. He, An effective hybrid meta-heuristic for flexible flow shop schedul-ing with limited buffers and step-deteriorating jobs, Engineering Applications of Artificial Intelligence 106 (NOV 2021). doi: 10.1016/j. engappai. 2021.104503
Zheng, X., \& Wang, L. (2015). A multi-agent optimization algorithm for resource constrained project scheduling problem. Expert Systems with Applications, 42(15-16), 6039-6049. https://doi.org/10.1016/j.eswa.2015.04.009
Zhu, K., Gong, G., Peng, N., Zhang, L., Huang, D., Luo, Q., \& Li, X. (2023). Dynamic distributed flexible job-shop scheduling problem considering operation inspection. Expert Systems with Applications, 224, Article 119840. https://doi.org/10.1016/j. eswa.2023.119840