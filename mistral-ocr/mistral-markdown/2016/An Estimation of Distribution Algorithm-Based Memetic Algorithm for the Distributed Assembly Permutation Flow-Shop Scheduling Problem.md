# An Estimation of Distribution Algorithm-Based Memetic Algorithm for the Distributed Assembly Permutation Flow-Shop Scheduling Problem 

Sheng-Yao Wang and Ling Wang


#### Abstract

In this paper, an estimation of distribution algorithm (EDA)-based memetic algorithm (MA) is proposed for solving the distributed assembly permutation flow-shop scheduling problem (DAPFSP) with the objective to minimize the maximum completion time. A novel bi-vector-based method is proposed to represent a solution for the DAPFSP. In the searching phase of the EDA-based MA (EDAMA), the EDA-based exploration and the local-search-based exploitation are incorporated within the MA framework. For the EDA-based exploration phase, a probability model is built to describe the probability distribution of superior solutions. Besides, a novel selective-enhancing sampling mechanism is proposed for generating new solutions by sampling the probability model. For the local-search-based exploitation phase, the critical path of the DAPFSP is analyzed to avoid invalid searching operators. Based on the analysis, a critical-path-based local search strategy is proposed to further improve the potential solutions obtained in the EDA-based searching phase. Moreover, the effect of parameter setting is investigated based on the Taguchi method of design-of-experiment. Suitable parameter values are suggested for instances with different scales. Finally, numerical simulations based on 1710 benchmark instances are carried out. The experimental results and comparisons with existing algorithms show the effectiveness of the EDAMA in solving the DAPFSP. In addition, the best-known solutions of 181 instances are updated by the EDAMA.


Index Terms-Critical path, distributed production scheduling, estimation of distribution algorithm (EDA), memetic algorithm (MA).

## I. INTRODUCTION

PRODUCTION scheduling [1]-[3] plays an important role in the decision making of a manufacturing system. Modeling and optimization for production scheduling are significant topics in the field of system engineering. Besides, effective and efficient algorithms for scheduling

[^0]problems can improve the efficiency of the manufacturing process. Therefore, it is important to study production scheduling problems, especially when developing effective solution algorithms.

As one of the most general scheduling problems, the assembly permutation flow-shop scheduling problem (APFSP) exists in many manufacturing systems. After the pioneer work of Lee et al. [4] and Potts et al. [5], in recent years the APFSP has been widely studied. Koulamas and Kyparisis [6] considered the collection and transportation operation between the production stage and assembly stage. They analyzed the worst-case ratio bound of several heuristics and the worst-case absolute performance bound for an asymptotically optimal heuristic based on compact vector summation techniques. Aiming at minimizing the total weighted flowtime, Tozkapan et al. [7] incorporated a lower bounding procedure and a dominance criterion into a branch and bound procedure. They also used a heuristic procedure to derive an initial upper bound. Allahverdi and Al-Anzi [8] considered the APFSP with respect to a maximum lateness performance measure and proposed three heuristics. Then, they considered the setup times of the operations and proposed a self-adaptive differential evolution heuristic [9]. Mozdgir et al. [10] addressed the APFSP with multiple nonidentical assembly machines to minimize the weighted sum of makespan and mean completion time. They developed a hybrid algorithm by combining the variable neighborhood search algorithm and a heuristic.

The above research makes a common assumption that all jobs are assumed to be processed and assembled in the same factory, which means one production center environment. Nevertheless, with the development of the business concept, multiplant companies and supply chains are taking a more important role in practice [11]. Besides, coproduction between companies becomes more and more common nowadays [12]. The distributed manufacturing strategy enables companies to achieve higher product quality, lower production costs, and lower management risks [13].

## A. Literature on Distributed Production Scheduling

Scheduling for distributed production systems is more difficult than classical shop scheduling. It should determine the factory assignment of jobs as well as the processing sequences in all the factories. Obviously, both sub-problems


[^0]:    Manuscript received November 12, 2014; revised January 23, 2015; accepted February 22, 2015. Date of publication April 3, 2015; date of current version December 14, 2015. This work was supported in part by the National Key Basic Research and Development Program of China under Grant 2013CB329503, in part by the National Science Foundation of China under Grant 61174189, and in part by the Doctoral Program Foundation of Institutions of Higher Education of China under Grant 20130002110057. This paper was recommended by Associate Editor N. Wu.

    The authors are with the Department of Automation, Tsinghua University, Beijing 100084, China (e-mail: wangshengyao10@mails.tsinghua.edu.cn).

    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

    Digital Object Identifier 10.1109/TSMC.2015.2416127

are related to each other and cannot be solved sequentially if high performance is desired [14]. Compared to classical shop scheduling, literature on distributed production scheduling is relatively limited. Jia et al. [15], [16] studied the distributed job shop scheduling problem under different criteria by employing a standard genetic algorithm (GA). Later, Jia et al. [17] refined the previous GA to solve small- and medium-scaled distributed scheduling problems. Chan et al. [18] proposed an adaptive GA to solve large-scaled distributed job shop scheduling problems with makespan as criterion. Then, Chan et al. [19] presented a GA with dominant genes approach to deal with distributed flexible manufacturing system scheduling problems subject to machine maintenance constraint. De Giovanni and Pezzella [20] proposed an improved GA to solve a distributed and flexible job-shop scheduling problem (FJSP). Naderi and Ruiz [14] addressed a distributed permutation flow-shop scheduling problem (DPFSP) and presented 14 heuristics based on constructive heuristics and variable neighborhood descent (VND) methods. After the pioneer work of Naderi and Ruiz [14], some intelligent optimization algorithms have been proposed for the DPFSP, such as Tabu search [21], iterated greedy algorithm [22], and estimation of distribution algorithm (EDA) [23]. The first effort that considered the assembly flowshop problem in a distributed manufacturing environment is made by Hatami et al. [24]. They presented a mixed integer linear programming model for a distributed APFSP (DAPFSP) and designed a VND algorithm accordingly.

## B. Literature on Memetic Algorithms and EDA

The memetic algorithms (MAs) [25], [26] have gained increasing attention and wide applications during recent years [27]-[33]. With the MA framework, the performances of evolutionary algorithms can be improved by combining problem-dependent local searches [26]. Liu et al. [27] proposed a particle swarm optimization (PSO)-based MA for a permutation flow-shop scheduling problem and discussed the effects of different local searches on optimization performances. Tseng and Chen [28] presented an MA by combining GA with a local search method to solve a multimode resource-constrained project scheduling problem (RCPSP). To solve the real-time multirobot path-planning problem, Rakshit et al. [29] proposed an adaptive MA by using differential evolution for global search and Q-learning for local refinement. Mei et al. [30] proposed an MA for the periodic capacitated arc routing problem, where a route-merging procedure was devised and embedded to tackle the insensitive objective. Liu et al. [31] proposed a new MA for multiobjective optimization by combining the global search ability of PSO with a synchronous local search heuristic for directed local fine-tuning. Tang and Yao [32] presented an MA for an integrated-circuit floorplanning problem. Hrncic et al. [33] applied an MA for grammatical inference in the field of domain-specific languages.

As a population-based evolutionary algorithm, the EDA [34] is a hot research topic in the field of evolutionary
computation. The main characteristic of the EDA is its explicit probability model, which is employed to perform optimization procedure [34]. The probability model represents the probability distribution of promising solutions. At each generation, the new solutions are generated by sampling the probability model. To trace a more promising searching area, the probability model is adjusted by information of some superior solutions in the population. In such an iterative way, it evolves and obtains satisfactory solutions. The EDA has already been successfully applied to solve a variety of academic and engineering optimization problems [35]. As for scheduling problems, the EDAs have been proposed for solving the RCPSP [36], flow-shop scheduling problem [37], single machine scheduling problem [38], hybrid flow-shop scheduling problem (HFSP) [39], FJSP [40], nurse scheduling problem [41], and so on. The EDAs stress more on global exploration while their local exploitation needs to be enhanced. For this purpose, the MA framework is expected to be an effective method.

## C. Introduction of This Paper

In our previous works, several EDA-based algorithms with different probability models have been proposed for the multimode RCPSP [36], HFSP [39], FJSP [40], and DPFSP [23], respectively. In this paper, an effective EDA-based MA (EDAMA) is proposed for solving the DAPFSP with the criterion of minimizing the maximum completion time. The new contributions of this paper are as follows.

1) To execute the searching operator efficiently, a novel bi-vector-based method is proposed to represent a solution for the DAPFSP. Compared with the solution representation in [23], an additional vector, i.e., the factory assignment vector is adopted in this paper to represent the corresponding factory for each job.
2) Because of an additional assembly stage, the DAPFSP is more complex than the DPFSP studied in [23]. To avoid invalid searching operators, critical path of the DAPFSP is analyzed in this paper. Accordingly, a critical-path-based local search (CPLS) strategy is proposed to perform exploitation in the EDAMA. The effectiveness of a CPLS strategy is demonstrated by comparative experiments.
3) In the DAPFSP, each job belongs to a defined product. A uniform sampling mechanism for the EDA in [23] is not helpful to start an assembly stage of products early. Therefore, a novel selective-enhancing sampling mechanism is proposed for the EDAMA in this paper. The results from the analysis of variance (ANOVA) show that the novel selective-enhancing sampling mechanism is significantly better than the uniform sampling mechanism [23].
4) In the EDAMA, the EDA-based exploration and CPLS-based exploitation are incorporated within the MA framework. Based on 1710 benchmark instances, numerical simulations and comparisons with the existing algorithms show the effectiveness of the EDAMA for

![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of the DAPFSP.
solving the DAPFSP. In addition, the best-known solutions of 181 instances are updated by the EDAMA.
The remainder of this paper is organized as follows. In Section II, the DAPFSP is described. Then, the EDAMA for the DAPFSP is introduced in Section III. Numerical results and comparisons are provided in Section IV. Finally, the conclusion is given in Section V.

## II. Distributed Assembly Permutation Flow-Shop Scheduling Problem

The DAPFSP [24] is illustrated in Fig. 1. There are $n$ jobs $\left\{J_{1}, J_{2}, \ldots, J_{n}\right\}$ to be processed and assembled to produce $S$ final products $\left\{P_{1}, P_{2}, \ldots, P_{S}\right\}$. Each product consists of some defined jobs and each job belongs to a defined product, i.e., $\sum_{r=1}^{S}\left|P_{r}\right|=n$. The production procedure consists of two stages: processing and assembly ones. There are $F$ factories at the processing stage. Each factory contains $m$ machines $\left\{M_{1}, M_{2}, \ldots, M_{m}\right\}$. Each job $J_{i}$ requires a sequence of $m$ operations $\left\{O_{i, 1}, O_{i, 2}, \ldots, O_{i, m}\right\}$ to be processed one after another in any one of the factories. Operation $O_{i, j}$ is executed on machine $M_{j}$ with processing time $t_{i, j}$. Besides, the jobs cannot be transferred to another factory during the processing procedure. As for the assembly stage, an assembly machine $M_{A}$ in an assembly factory assembles all jobs into products. After all the corresponding jobs of product $P_{r}$ are finished at the processing stage, they are assembled with an assembly time $t_{i}^{A}$. Besides, the following assumptions for the classical flow-shop scheduling are adopted: all the jobs are independent and available at time 0 . Each machine can process only one job at a time and each job can be processed by only one machine at a time. Preemption is not allowed, i.e., each operation must be completed without interruption once it is started. Setup time of machines and transportation time between operations are contained in the processing time. The DAPFSP is to assign jobs to factories and sequence jobs for all machines to optimize a certain scheduling objective. In this paper, the objective is to minimize the maximum completion time (makespan).

Denote $\lambda^{k}=\left[\lambda^{k}(1), \lambda^{k}(2), \ldots, \lambda^{k}\left(n_{k}\right)\right]$ as the job sequence in factory $k$ at the processing stage, where $n_{k}$ is the total number of jobs assigned to factory $k$. Denotes $C_{i, j}$ as the completion time of $O_{i, j}$. For a schedule $\mathbf{A}$ of the DAPFSP, i.e., a set of sequences $\left\{\lambda^{1}, \lambda^{2}, \ldots, \lambda^{F}\right\}$, the makespan $C_{\max }(\mathbf{A})$ is
calculated as follows:

$$
\begin{aligned}
C_{\lambda^{k}(1), 1}= & t_{\lambda^{k}(1), 1}, k=1,2, \ldots, F \\
C_{\lambda^{k}(i), 1}= & C_{\lambda^{k}(i-1), 1}+t_{\lambda^{k}(i), 1} \\
& k=1,2, \ldots, F ; \quad i=2,3, \ldots, n_{k} \\
C_{\lambda^{k}(1), j}= & C_{\lambda^{k}(1), j-1}+t_{\lambda^{k}(1), j} \\
& k=1,2, \ldots, F ; \quad j=2,3, \ldots, m \\
C_{\lambda^{k}(i), j}= & \max \left\{C_{\lambda^{k}(i-1), j}, C_{\lambda^{k}(i), j-1}\right\}+t_{\lambda^{k}(i), j} \\
& k=1,2, \ldots, F ; \quad i=2,3, \ldots, n_{k} ; j=2,3, \ldots, m
\end{aligned}
$$

Then, the product sequence on the assembly machine is obtained according to the completion time of all jobs. Denote $\lambda^{A}=\left[\lambda^{A}(1), \lambda^{A}(2), \ldots, \lambda^{A}(S)\right]$ as the product sequence and $C_{r}^{P}$ as the latest completion time of the jobs belonging to product $\lambda^{A}(r)$. Denote $C_{r}^{A}$ as the completion time of assembling product $\lambda^{A}(r)$

$$
\begin{aligned}
C_{1}^{A} & =C_{1}^{P}+t_{r}^{A} \\
C_{r}^{A} & =\max \left\{C_{r-1}^{A}, C_{r}^{P}\right\}+t_{r}^{A}, r=2,3, \ldots, S \\
C_{\max }(\mathbf{A}) & =C_{S}^{A}
\end{aligned}
$$

The objective of solving the DAPFSP is to find a schedule $\mathbf{A}^{*}$ with the minimum makespan. However, as an NP-hard problem [24], the DAPFSP cannot be solved by any polynomial time algorithms. Therefore, the objective of the solution methods is to obtain an approximate optimal schedule within an acceptable computing time.

## III. EDAMA FOR DAPFSP

## A. Solution Representation

In EDAMA, the population is composed of a set of solutions for the DAPFSP. A solution is represented by a job priority vector $\pi$ and a factory assignment vector $\xi$ as shown in Fig. 2. The elements in the job priority vector are denoted by job numbers. In addition, the element $\pi(i)$ represents that job $J_{\pi(i)}$ has the processing priority of $i$. The elements in the factory assignment vector are denoted by factory numbers, which determine corresponding factories for processing jobs. Specifically, element $\xi(i)$ represents that job $J_{i}$ is assigned to factory $\xi(i)$ at the processing stage.

For decoding a given solution into a feasible schedule, jobs are arranged to their corresponding factories in the order of the

| Job priority vector | Factory assignment vector |
| :--: | :--: |
| $\boldsymbol{\pi}=[\pi(1), \pi(2), \cdots, \pi(n)]$ | $\boldsymbol{\xi}=[\xi(1), \xi(2), \cdots, \xi(n)]$ |

Fig. 2. Solution representation in EDAMA.

TABLE I
DATA FOR THE EXAMPLE INSTANCE

| Product | Job | Processing time |  |  |  | Assembly time |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | $M_{1}$ | $M_{2}$ | $M_{3}$ | $M_{4}$ |  |  |  |
| $P_{1}$ | $J_{4}$ | 11 | 60 | 41 |  |  |  |  |
|  | $J_{5}$ | 95 | 37 | 22 |  |  |  |  |
|  | $J_{6}$ | 90 | 12 | 85 |  |  |  |  |
|  | $J_{10}$ | 27 | 10 | 93 | 48 |  |  |  |
|  | $J_{11}$ | 86 | 51 | 89 |  |  |  |  |
|  | $J_{12}$ | 89 | 56 | 90 |  |  |  |  |
|  | $J_{1}$ | 92 | 27 | 88 |  |  |  |  |
|  | $J_{2}$ | 58 | 83 | 25 |  |  |  |  |
| $P_{2}$ | $J_{3}$ | 24 | 33 | 92 |  |  |  |  |
|  | $J_{5}$ | 27 | 28 | 45 |  |  |  |  |
|  | $J_{6}$ | 7 | 22 | 79 |  |  |  |  |
|  | $J_{8}$ | 13 | 92 | 41 |  |  |  |  |

Job priority vector

| 8 | 7 | 9 | 3 | 2 | 1 | 12 | 5 | 11 | 10 | 4 | 6 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Factory assignment vector |  |  |  |  |  |  |  |  |  |  |  |
| 1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 |
| $J_{1}$ | $J_{2}$ | $J_{3}$ | $J_{4}$ | $J_{5}$ | $J_{6}$ | $J_{7}$ | $J_{8}$ | $J_{9}$ | $J_{10}$ | $J_{11}$ | $J_{12}$ |

Fig. 3. Feasible solution of the example instance.
![img-1.jpeg](img-1.jpeg)

Fig. 4. Corresponding Gantt chart of the solution.
job priority vector. Then, processing sequences of jobs in all factories are obtained, i.e., $\left\{\lambda^{1}, \lambda^{2}, \ldots, \lambda^{F}\right\}$. The makespan value of the solution is calculated as introduced in Section II. To explain the solution representation and decoding procedure, an example instance with 12 jobs and two factories is provided in Table I. The representation of a feasible solution is illustrated in Fig. 3. Processing sequences of jobs in two factories are $\lambda^{1}=(8,9,1,5,11,4)$ and $\lambda^{2}=(7,3,2,12,10,6)$, respectively. The Gantt chart of the corresponding schedule is illustrated in Fig. 4.

## B. Probability Model

A crucial part of the EDA is its probability model that describes the distribution of the searching space. Generally, the
probability model is built based on characteristics of superior solutions. Besides, the EDA generates new solutions by sampling according to the probability model. Therefore, a proper probability model is critical to the performance of EDA-based algorithms.

In this paper, the optimization objective is to minimize the makespan for the DAPFSP. According to the above solution representation, the processing priorities of jobs affect the objective value of a solution. Therefore, the probability model is designed as a probability matrix $\boldsymbol{Q}$, which is related to the job priority vector of a solution

$$
\boldsymbol{Q}=\left[\begin{array}{cccc}
q_{11}(l) & q_{12}(l) & \cdots & q_{1 n}(l) \\
q_{21}(l) & q_{22}(l) & \cdots & q_{2 n}(l) \\
\vdots & \vdots & \ddots & \vdots \\
q_{n 1}(l) & q_{n 2}(l) & \cdots & q_{n n}(l)
\end{array}\right]
$$

Element $q_{i j}(l)$ in the probability matrix $\boldsymbol{Q}$ represents the probability that job $J_{j}$ appears before or in the $i$ th position of the job priority vector at the $i$ th generation. The value of $q_{i j}(l)$ refers to the importance of a job when decoding a solution into a schedule. At the initialization stage of the EDAMA, the elements in matrix $\boldsymbol{Q}$ are initialized as $q_{i j}(0)=1 / n$ (for all $i$ and $j$ ), which implies a uniform distribution in the searching space.

## C. Selective-Enhancing Sampling Mechanism

At each generation of the EDAMA, job priority vector $\boldsymbol{\pi}$ of a new solution is generated by sampling the searching space according to the probability matrix $\boldsymbol{Q}$. To be specific, it determines job number $\pi(i)$ for each position of $\boldsymbol{\pi}$ from $i=1$ to $n$. In considering the decoding procedure and the optimization objective, jobs belonging to the same product are expected to be close to each other in job priority vector $\boldsymbol{\pi}$. In this way, it is helpful to start the assembly stage of the corresponding product as early as possible. Consequently, it is more probable to obtain a better makespan value. To implement this method in the sampling procedure, some elements in the probability matrix $\boldsymbol{Q}$ are selectively enhanced. Denote $p_{i j}(l)$ as the probability of selecting job $J_{j}$ for the $i$ th position. It calculates $p_{i j}(l)$ as follows:

$$
p_{i j}(l)= \begin{cases}q_{i j}(l), & i=1 \\ \frac{\delta(i, j) \cdot q_{i j}(l)}{\sum_{k=1}^{n} \delta(i, k) \cdot q_{i k}(l)}, & i>1\end{cases}
$$

where $\delta(i, j)$ is the enhancing factor defined as follows:

$$
\delta(i, j)= \begin{cases}\mu, & \text { if } J_{j} \text { belongs to the same product of } J_{\pi(i-1)} \\ 1, & \text { else }\end{cases}
$$

Parameter $\mu(\mu>1)$ can be regarded as the intensity to enhance the probability, which controls the compactness of jobs belonging to the same product. If the value of $\mu$ is too small, the corresponding jobs may not be compact so that the assembly stage of a product cannot be started early. On the other hand, a too large value of $\mu$ may cause a greedy sampling process, which results in a loss of diversity of a new population. Considering the total number of jobs to be selected in

Input job priority vector $\pi$.
Output factory assignment vector $\boldsymbol{\xi}$.

## Begin

For $i=1$ to $F$
$\xi[\pi(i)]=i$;
For $i=F+1$ to $n$
Find the factory $k$ that can process job $J_{\pi(i)}$ with the earliest completion time;
$\xi[\pi(i)]=k$;
End

Fig. 5. Pseudocode of the ECF rule [23].
the sampling process, it sets $\mu=n$ in this paper. The effect of the sampling mechanism and the impact of $\mu$ are further investigated in Section IV. In addition, if job $J_{i}$ has already been selected, the whole $i$ th column in probability matrix $\boldsymbol{Q}$ is set as zero. Then, all the elements in $\boldsymbol{Q}$ are normalized to maintain that each row sums up to 1 .

In such a sampling way, job priority vector $\pi$ is obtained until all the job numbers are selected. Then, factory assignment vector $\boldsymbol{\xi}$ is determined according to $\pi$ based on the earliest completion factory (ECF) rule [23]. Aiming at obtaining a small makespan value, the ECF rule arranges each job to a factory that can process it with the earliest completion time. The pseudocode of the ECF rule is illustrated in Fig. 5.

Based on the sampling mechanism, a solution is generated and decoded to calculate the makespan value. At each generation of the EDAMA, $P_{-}$Size solutions are generated to form a new population.

## D. Updating Mechanism

The probability model should be well adjusted to make the search procedure tract the promising searching region. As a consequence, an updating mechanism is employed to adjust the model at each generation. First, the superior sub-population that consists of SP_Size elite solutions is determined by the widely-used two-tournament selection strategy [42], where SP_Size $=\eta \% \cdot P_{-}$Size. Then, probability matrix $\boldsymbol{Q}$ is updated based on the information of the superior sub-population and the historical information of searching. The updating process can be regarded as a kind of increased learning as follows:

$$
q_{i j}(l+1)=(1-\alpha) q_{i j}(l)+\frac{\alpha}{i \times \text { SP_Size }} \sum_{k=1}^{\text {SP_Size }} I_{i j}^{k} \quad \forall i, j
$$

where $\alpha \in(0,1)$ is the learning rate of $\boldsymbol{Q}$ and $I_{i j}^{k}$ is the following indicator function of the $k$ th solution in the superior sub-population:

$$
I_{i j}^{k}=\left\{\begin{array}{ll}
1, & \text { if job } J_{j} \text { appears before or in the } i \text { th position } \\
0, & \text { else }
\end{array}\right.
$$

![img-2.jpeg](img-2.jpeg)

Fig. 6. Illustration of the critical path.

## E. Critical-Path-Based Local Search

The EDAs pay more attention to global exploration while their exploitation capability is relatively limited. The MA framework provides an effective method to balance the exploration and exploitation abilities for EDAs. It is commonly recognized that incorporating local search into the framework of evolutionary computing can improve the optimization capability. Such idea has also been adopted in designing an MA for scheduling problems [27]. Therefore, a CPLS strategy is proposed to enhance the local exploitation of the EDA.

For shop scheduling problems, a critical path refers to a continuous job-path from the beginning to end of the solution with no idle time between any two jobs [43]. The makespan value of a solution is equal to the length of the critical path. Therefore, the only way to improve a solution is to adjust jobs of its critical path [40]. As for the DAPFSP, the critical path of a solution consists of two parts: 1) processing and 2) assembly ones. Fig. 6 illustrates the critical path of the example in Fig. 4.

In a critical path of the solution, the factory of the processing part is defined as the critical factory (e.g., factory 1 in Fig. 6). The jobs of the processing part are defined as the critical jobs (e.g., $J_{1}, J_{5}$, and $J_{9}$ in Fig. 6). Then, five local search operators are designed based on the critical path, including three job-based operators and two factory-based operators.

The three job-based operators adjust the job priority vector of the solution only. First, a critical job $J_{C}$ and another job $J_{R}$ from the critical factory are selected randomly. Then the following steps are executed.

1) Job-Swap: Swap the priorities of jobs $J_{C}$ and $J_{R}$ in the job priority vector.
2) Job-Insert: Insert job $J_{C}$ to the position after job $J_{R}$ in the job priority vector.
3) Job-Inverse: Invert the subsequence between the position of jobs $J_{C}$ and $J_{R}$ in the job priority vector.
The two factory-based operators adjust both job priority vector and factory assignment vector of a solution. First, a critical job $J_{C}$ from the critical factory $F_{C}$ is selected randomly. Second, another factory $F_{R}$ and a job $J_{R}$ from $F_{R}$ are selected randomly. Then the following steps are executed.

![img-3.jpeg](img-3.jpeg)

Fig. 7. Iteration of the CPLS strategy.
4) Factory-Swap: Swap the priorities of jobs $J_{C}$ and $J_{R}$ in the job priority vector and swap the factories of jobs $J_{C}$ and $J_{R}$ in the factory assignment vector.
5) Factory-Insert: Insert job $J_{C}$ to the position after job $J_{R}$ in the job priority vector and change the factory of job $J_{C}$ to $F_{R}$ in the factory assignment vector.
If a new solution obtained by any of the local search operators is better, the old solution is replaced. Besides, the critical path of a new solution is reidentified for the next operator. An iteration of the CPLS strategy is illustrated in Fig. 7.

At each generation of the EDAMA, the CPLS strategy is implemented by LS times to improve the best solution of the population. Considering the problem scale, the value of LS is set as $\mathrm{LS}=\gamma \cdot n$, where $\gamma$ implies the intensity of the local search.

## F. EDA-Based MA

With the above design, the flowchart of the EDAMA for solving the DAPFSP is illustrated in Fig. 8.

At the initial stage of evolution process, the whole searching area is sampled uniformly. Then, the algorithm uses the EDA-based evolutionary search mechanism to sample a potential area. Moreover, a CPLS strategy is performed in a promising region, aiming to obtain better solutions. With the benefit of combining the EDA-based search and CPLS strategy, global exploration and local exploitation are balanced. As for the stopping condition of the EDAMA, the algorithm stops after a total number of Max_G solutions are generated.

## G. Computational Complexity Analysis

At each generation of the EDAMA, the computational complexity can be roughly analyzed as follows.

For the updating process, first it has a computational complexity of $O$ (SP_Size) by using the tournament selection method to select the elite solutions from population; then, it has a computational complexity of $O[n\left(\mathrm{SP}_{-} \text {Size }+n\right)]$ to update all the elements of $\boldsymbol{Q}$. For the sampling process,
![img-4.jpeg](img-4.jpeg)

Fig. 8. Flowchart of EDAMA for DAPFSP.
it generates the job priority vector by the roulette strategy via sampling $\boldsymbol{Q}$ with a computational complexity of $O\left(n^{2}\right)$. Then, the factory assignment vector is determined with a computational complexity of $O(n F)$.

From the above analysis, it can be concluded that the computational complexity of the proposed EDAMA is not large.

## IV. NUMERICAL RESULTS AND COMPARISONS

To test the performance of the EDAMA, numerical tests are carried out by using two sets of benchmark instances [24]. The data for each instance is available at http://soa.iti.es. The first set consists of 900 small-scaled instances, where $n=$ $\{8,12,16,20,24\}, m=\{2,3,4,5\}, F=\{2,3,4\}$, and $S=$ $\{2,3,4\}$. The second set consists of 810 large-scaled instances, where $n=\{100,200,500\}, m=\{5,10,20\}, F=\{4,6,8\}$, and $S=\{30,40,50\}$. In considering the problem scale, the value of Max_G in the stopping condition is set as 5000 and 10000 for the first and second set, respectively.

TABLE II
Parameter Values of Each Factor Level

| Parameters | Factor level |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 2 | 3 | 4 |  |
| $P_{-}$Size | 50 | 100 | 150 | 200 |  |
| $\eta$ | 10 | 20 | 30 | 40 |  |
| $\alpha$ | 0.1 | 0.2 | 0.3 | 0.4 |  |
| $\gamma$ | 0.25 | 0.50 | 0.75 | 1.00 |  |

TABLE III
Orthogonal Array and RV Values

| Experiment <br> Number | Factor Level |  |  |  | RV |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | $P_{-}$Size | $\eta$ | $\alpha$ | $\gamma$ | First Set | Second Set |
| 1 | 1 | 1 | 1 | 1 | 1.39 | 0.12 |
| 2 | 1 | 2 | 2 | 2 | 1.46 | 0.13 |
| 3 | 1 | 3 | 3 | 3 | 1.40 | 0.14 |
| 4 | 1 | 4 | 4 | 4 | 1.25 | 0.19 |
| 5 | 2 | 1 | 2 | 3 | 1.57 | 0.14 |
| 6 | 2 | 2 | 1 | 4 | 1.47 | 0.18 |
| 7 | 2 | 3 | 4 | 1 | 1.46 | 0.15 |
| 8 | 2 | 4 | 3 | 2 | 1.45 | 0.14 |
| 9 | 3 | 1 | 3 | 4 | 1.33 | 0.17 |
| 10 | 3 | 2 | 4 | 3 | 1.69 | 0.13 |
| 11 | 3 | 3 | 1 | 2 | 2.10 | 0.19 |
| 12 | 3 | 4 | 2 | 1 | 1.83 | 0.18 |
| 13 | 4 | 1 | 4 | 2 | 1.72 | 0.15 |
| 14 | 4 | 2 | 3 | 1 | 1.79 | 0.15 |
| 15 | 4 | 3 | 2 | 4 | 1.64 | 0.20 |
| 16 | 4 | 4 | 1 | 3 | 2.16 | 0.20 |

To evaluate the performance of the EDAMA, as in [24], experimental results are evaluated by relative percentage deviation (RPD) as follows:

$$
\mathrm{RPD}=\frac{\mathrm{alg}-\mathrm{opt}}{\mathrm{opt}} \times 100
$$

where opt is the best-known makespan from http://soa.iti.es and alg corresponds to the makespan of the solution obtained by a certain algorithm. If the obtained RPD value is less than 0 , it implies that a new better solution is found.

## A. Parameters Setting

The proposed EDAMA has four key parameters: 1) $P_{-}$Size (population size); 2) $\eta$ (percentage of the superior sub-population); 3) $\alpha$ (learning rate of $\boldsymbol{Q}$ ); and 4) $\gamma$ (intensity of local search). To investigate the influence of these parameters on the performance of the EDAMA, the Taguchi method of design-of-experiment (DOE) [44] is implemented. As the stopping conditions for two sets of benchmarks are different, two DOE testings are carried out, respectively. For the first set, a moderate-scaled instance $\mathrm{I} \_16 \_5 \_3 \_2 \_1$ is used, where $16 \_5 \_3 \_2$ denotes the instance scale $(n=16, m=5, F=3$, and $S=2)$ and 1 denotes that it is the first instance of this scale. Similarly, instance I_200_5_6_40_7 is used for the second set.

Four factor levels are employed. Combinations of different values of these parameters are listed in Table II. Accordingly, the orthogonal array $L_{16}\left(4^{4}\right)$ is chosen. For each parameter combination, the EDAMA is run 20 times independently and the average RPD value of 20 runs is obtained as the response variable (RV) value. The orthogonal array and RV values are listed in Table III.
![img-5.jpeg](img-5.jpeg)

Fig. 9. Factor level trends of small-scaled instances.
![img-6.jpeg](img-6.jpeg)

Fig. 10. Factor level trends of the large-scaled instances.

TABLE IV
Response Table for Small-Scaled Instance

| Level | $P_{-}$Size | $\eta$ | $\alpha$ | $\gamma$ |
| :-- | :--: | :--: | :--: | :--: |
| 1 | $\mathbf{1 . 3 7 2 9}$ | $\mathbf{1 . 5 0 1 3}$ | 1.7801 | 1.6187 |
| 2 | 1.4881 | 1.6012 | 1.6253 | 1.6802 |
| 3 | 1.7373 | 1.6495 | $\mathbf{1 . 4 9 0 3}$ | 1.7011 |
| 4 | 1.8251 | 1.6714 | 1.5277 | $\mathbf{1 . 4 2 3 4}$ |
| Delta | 0.4522 | 0.1701 | 0.2897 | 0.2777 |
| Rank | 1 | 4 | 2 | 3 |

TABLE V
Response Table for Large-Scaled Instance

| Level | $P_{-}$Size | $\eta$ | $\alpha$ | $\gamma$ |
| :-- | :--: | :--: | :--: | :--: |
| 1 | $\mathbf{0 . 1 4 3 6}$ | $\mathbf{0 . 1 4 3 3}$ | 0.1718 | $\mathbf{0 . 1 4 8 2}$ |
| 2 | 0.1512 | 0.1490 | 0.1616 | 0.1530 |
| 3 | 0.1664 | 0.1689 | $\mathbf{0 . 1 4 7 1}$ | 0.1505 |
| 4 | 0.1744 | 0.1744 | 0.1551 | 0.1839 |
| Delta | 0.0309 | 0.0311 | 0.0247 | 0.0357 |
| Rank | 3 | 2 | 4 | 1 |

According to the orthogonal table, trends of each factor level for different sets of benchmarks are illustrated in Figs. 9 and 10. Then, the response value of each parameter is figured out to analyze the significance rank. The results are listed in Tables IV and V.

From Fig. 9 and Table IV, it can be seen that $P_{-}$Size has the most significant impact on small-scaled instances. With a fixed total number of solutions, a small value of $P_{-}$Size allows sufficient evolution with more generations. The significance of learning rate $\alpha$ ranks the second. Small value of $\alpha$ could lead to slow convergence while large value could lead to premature convergence. From Fig. 10 and Table V, it can be seen that the intensity of CPLS procedure has the most

TABLE VI
Suggested Combinations of Parameters

| Instances | $P$ _Size | $\eta$ | $n$ | $Y$ | Max, $G$ |
| :-- | :--: | :--: | :--: | :--: | :--: |
| Small-scaled | 50 | 10 | 0.3 | 1.00 | 5000 |
| Large-scaled | 50 | 10 | 0.3 | 0.25 | 10000 |

TABLE VII
Comparison of EDA Without CPLS, CPLS, and EDAMA

| n | Pure EDA |  | CPLS |  | EDAMA |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Average <br> RPD | CPU <br> (ms) | Average <br> RPD | CPU <br> (ms) | Average <br> RPD | CPU <br> (ms) |
| 8 | 0.11 | 22 | 0.02 | 22 | 0.00 | 22 |
| 12 | 0.26 | 37 | 0.08 | 33 | 0.00 | 33 |
| 16 | 0.35 | 54 | 0.18 | 42 | $-0.01$ | 42 |
| 20 | 0.38 | 74 | 0.14 | 52 | $-0.12$ | 52 |
| 24 | 0.44 | 97 | 0.14 | 61 | $-0.23$ | 63 |
| Average | 0.31 | 57 | 0.11 | 42 | $-0.07$ | 42 |

significant impact on large-scaled instances. A small value of $\gamma$ also allows sufficient evolution with more generations. The significance of $\eta$ ranks the second. A smaller value is helpful to update the probability model more accurately. According to the analysis, the suggested combinations of parameter values for the proposed algorithm are determined, which are listed in Table VI. This setting will also be used in the following comparison.

## B. Effect of MA Method

To demonstrate the effectiveness of MA method, the pure EDA (without CPLS), CPLS strategy, and EDAMA are compared by using the first set of instances. The three algorithms have the same stopping condition. Besides, pure EDA has the same parameters as EDAMA. The CPLS strategy generates a new population randomly and implements local search procedure on the best solution at every generation. The three algorithms are run 20 times independently and the best RPD values are obtained. Table VII summarizes the results including the CPU times grouped by different values of $n$ (180 data per average).

From Table VII, it can be seen that EDAMA is the most effective one among the three algorithms. The average RPD value obtained by EDAMA is -0.07 while pure EDA is 0.31 and CPLS is 0.11 . As for the CPU time, both the EDAMA and CPLS spend an average of 42 ms to solve all instances. It takes an average of 57 ms for pure EDA, which is more than the other two algorithms. Compared with pure EDA, EDAMA is more efficient. The reason is that more solutions are generated in CPLS procedure of EDAMA at each generation. Therefore, the generation of EDAMA is less than that of pure EDA under the same stopping condition (i.e., maximum generated solution number).

In summary, within MA framework, the proposed EDAMA is more effective and efficient than pure EDA.

## C. Effect of Selective-Enhancing Sampling Mechanism

Next, we investigate the effect of selective-enhancing sampling mechanism and the impact of $\mu$ by using instance I_24_5_3_2_1. The EDAMA with each different value of $\mu$ is

TABLE VIII
EFFECTS OF THE SAMPLING MECHANISM

| $\mu$ | Best | Average | Worst | Standard deviation |
| :-- | :--: | :--: | :--: | :--: |
| 1 | 2.20 | 8.23 | 11.97 | 2.48 |
| $0.5 n$ | $\mathbf{0}$ | 1.45 | 4.67 | 2.03 |
| $n$ | $\mathbf{0}$ | $\mathbf{0 . 1 1}$ | $\mathbf{0 . 5 3}$ | $\mathbf{0 . 1 8}$ |
| $2 n$ | $\mathbf{0}$ | 0.32 | 1.94 | 0.46 |

![img-7.jpeg](img-7.jpeg)

Fig. 11. Interval plots by different values of $\mu$.
TABLE IX
ANOVA ReSULTS OF THE SAMPLING MECHANISM

| Source | DF | SS | MS | F | $p$ |
| :-- | :--: | :--: | :--: | :--: | :--: |
| $\mu$ | 3 | 887.86 | 295.95 | 112.90 | 0.00 |
| Error | 76 | 199.22 | 2.62 |  |  |
| Total | 79 | 1087.08 |  |  |  |

run 20 times independently. The statistical results are listed in Table VIII, including the best, average, and worst RPD values as well as the standard deviation. Besides, the interval plots by different values of $\mu$ are illustrated in Fig. 11. Note that, the case of $\mu=1$ means that traditional uniform sampling mechanism [23] is employed. In addition, ANOVA is carried out at $95 \%$ confidence level. The results of ANOVA are listed in Table IX.

From Table VIII and Fig. 11, it can be seen that EDAMA performs better when $\mu$ is larger than 1. From Table IX, it also can be seen that $p$-value is $0<0.05$. Therefore, selective-enhancing sampling mechanism is considered to be significantly better than uniform sampling mechanism [23]. In addition, it can be seen from Fig. 11 that the value of $\mu$ should be neither too small nor too large. This is consistent with the analysis in Section III.

## D. Results and Comparison for Small-Scaled Instances

By using 900 small-scaled instances, EDAMA is compared with all the existing heuristic algorithms in [24]. For each instance, EDAMA runs 20 times independently and the best RPD values are obtained. Table X summarizes the results grouped by each combination of $n$ and $F$ ( 60 data per average) as in [24], where the results of comparative algorithms are directly from literature.

From Table X, it can be seen that EDAMA is the best one among all the algorithms for small-scaled instances. The corresponding RPD values of the best solutions are nonpositive for all the instance groups except for $\{3 \times 12\}$ and $\{4 \times 16\}$.

TABLE X
Results of Small-Scaled Instances

| $F \times n$ | $\mathrm{H}_{11}$ | $\mathrm{H}_{12}$ | $\mathrm{H}_{21}$ | $\mathrm{H}_{22}$ | $\mathrm{H}_{31}$ | $\mathrm{H}_{32}$ | $\mathrm{VND}_{011}$ | $\mathrm{VND}_{012}$ | $\mathrm{VND}_{021}$ | $\mathrm{VND}_{022}$ | $\mathrm{VND}_{031}$ | $\mathrm{VND}_{032}$ | $\mathrm{~VND}_{033}$ | $\mathrm{EDAMA}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $2 \times 8$ | 14.62 | 13.61 | 6.91 | 5.99 | 13.55 | 12.17 | 1.00 | 0.76 | 1.00 | 0.76 | 1.02 | 0.78 | $\mathbf{0 . 0 0}$ |  |
| $2 \times 12$ | 13.70 | 12.78 | 5.74 | 5.17 | 11.58 | 11.05 | 0.93 | 0.87 | 0.93 | 0.87 | 0.93 | 0.87 | $\mathbf{0 . 0 0}$ |  |
| $2 \times 16$ | 12.52 | 11.40 | 5.77 | 5.10 | 10.00 | 9.16 | 0.73 | 0.55 | 0.72 | 0.53 | 1.09 | 0.53 | $\mathbf{- 0 . 0 5}$ |  |
| $2 \times 20$ | 10.23 | 9.59 | 4.55 | 3.78 | 8.96 | 8.46 | 0.53 | 0.36 | 0.51 | 0.37 | 0.57 | 0.37 | $\mathbf{- 0 . 3 3}$ |  |
| $2 \times 24$ | 8.71 | 8.34 | 5.00 | 4.74 | 7.54 | 7.15 | 0.54 | 0.21 | 0.54 | 0.21 | 0.54 | 0.21 | $\mathbf{- 0 . 4 8}$ |  |
| $3 \times 8$ | 11.35 | 9.96 | 4.57 | 3.15 | 8.92 | 7.79 | 1.09 | 0.70 | 1.15 | 0.76 | 1.15 | 0.76 | $\mathbf{0 . 0 0}$ |  |
| $3 \times 12$ | 9.96 | 9.13 | 3.03 | 2.55 | 8.72 | 7.50 | 0.44 | 0.28 | 0.44 | 0.28 | 0.44 | 0.28 | $\mathbf{0 . 0 1}$ |  |
| $3 \times 16$ | 10.10 | 9.16 | 3.77 | 3.14 | 9.59 | 8.73 | 0.86 | 0.56 | 0.91 | 0.56 | 0.91 | 0.56 | $\mathbf{- 0 . 0 1}$ |  |
| $3 \times 20$ | 9.86 | 8.93 | 2.72 | 2.19 | 8.53 | 7.84 | 0.43 | 0.43 | 0.43 | 0.43 | 0.43 | 0.43 | $\mathbf{0 . 0 1}$ |  |
| $3 \times 24$ | 7.77 | 6.48 | 3.11 | 2.52 | 7.24 | 6.32 | 0.64 | 0.33 | 0.64 | 0.33 | 0.64 | 0.33 | $\mathbf{- 0 . 1 6}$ |  |
| $4 \times 8$ | 9.03 | 8.01 | 2.16 | 1.25 | 6.41 | 5.25 | 1.08 | 0.63 | 0.99 | 0.63 | 0.99 | 0.63 | $\mathbf{0 . 0 0}$ |  |
| $4 \times 12$ | 5.63 | 4.53 | 1.82 | 1.38 | 4.58 | 3.58 | 0.74 | 0.47 | 0.74 | 0.47 | 0.74 | 0.56 | $\mathbf{0 . 0 0}$ |  |
| $4 \times 16$ | 7.21 | 6.34 | 2.86 | 2.27 | 6.14 | 5.18 | 0.59 | 0.28 | 0.59 | 0.28 | 0.59 | 0.28 | $\mathbf{0 . 0 3}$ |  |
| $4 \times 20$ | 6.80 | 6.00 | 2.96 | 2.61 | 5.66 | 5.04 | 1.10 | 0.63 | 1.10 | 0.63 | 1.10 | 0.63 | $\mathbf{- 0 . 0 1}$ |  |
| $4 \times 24$ | 5.14 | 4.43 | 2.02 | 1.60 | 4.87 | 4.19 | 0.57 | 0.26 | 0.57 | 0.26 | 0.57 | 0.26 | $\mathbf{- 0 . 0 5}$ |  |
| Average | 9.51 | 8.58 | 3.80 | 3.16 | 8.15 | 7.29 | 0.75 | 0.49 | 0.75 | 0.49 | 0.78 | 0.50 | $\mathbf{- 0 . 0 7}$ |  |

TABLE XI
Results of Large-Scaled Instances

|  | $\mathrm{H}_{11}$ | $\mathrm{H}_{12}$ | $\mathrm{H}_{21}$ | $\mathrm{H}_{22}$ | $\mathrm{H}_{31}$ | $\mathrm{H}_{32}$ | $\mathrm{VND}_{011}$ | $\mathrm{VND}_{012}$ | $\mathrm{VND}_{021}$ | $\mathrm{VND}_{022}$ | $\mathrm{VND}_{031}$ | $\mathrm{VND}_{032}$ | $\mathrm{EDAMA}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 4 | 5.57 | 5.09 | 0.32 | 0.19 | 2.96 | 2.56 | 0.06 | 0.03 | 0.05 | 0.01 | 0.05 | 0.01 | $\mathbf{- 0 . 0 1 3}$ |
| F 6 | 3.77 | 3.29 | 0.11 | 0.06 | 1.64 | 1.31 | 0.03 | 0.01 | 0.02 | 0.00 | 0.02 | 0.00 | $\mathbf{- 0 . 0 0 4}$ |
| 8 | 3.09 | 2.66 | 0.04 | 0.02 | 1.21 | 0.93 | 0.02 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | $\mathbf{- 0 . 0 0 4}$ |
| 30 | 3.78 | 3.34 | 0.21 | 0.11 | 2.23 | 1.86 | 0.03 | 0.01 | 0.04 | 0.01 | 0.04 | 0.01 | $\mathbf{- 0 . 0 1 1}$ |
| s 40 | 4.30 | 3.85 | 0.15 | 0.10 | 1.94 | 1.62 | 0.04 | 0.02 | 0.02 | 0.01 | 0.02 | 0.01 | $\mathbf{- 0 . 0 0 8}$ |
| 50 | 4.36 | 3.85 | 0.11 | 0.05 | 1.65 | 1.32 | 0.04 | 0.01 | 0.02 | 0.00 | 0.02 | 0.00 | $\mathbf{- 0 . 0 0 3}$ |
| 100 | 6.30 | 5.61 | 0.17 | 0.08 | 2.02 | 1.58 | 0.05 | 0.02 | 0.03 | 0.01 | 0.03 | 0.01 | $\mathbf{- 0 . 0 0 8}$ |
| n 200 | 3.76 | 3.28 | 0.15 | 0.07 | 1.92 | 1.55 | 0.03 | 0.01 | 0.02 | 0.00 | 0.02 | 0.00 | $\mathbf{- 0 . 0 0 6}$ |
| 500 | 2.37 | 2.16 | 0.14 | 0.10 | 1.87 | 1.67 | 0.03 | 0.01 | 0.03 | 0.01 | 0.03 | 0.01 | $\mathbf{- 0 . 0 0 7}$ |
| Average | 4.14 | 3.68 | 0.16 | 0.09 | 1.94 | 1.60 | 0.04 | 0.01 | 0.03 | 0.01 | 0.03 | 0.01 | $\mathbf{- 0 . 0 0 7}$ |

TABLE XII
CPU Time (SECONDs) FOR LARGE-Scaled InSTANCES

|  | $\mathrm{H}_{11}$ | $\mathrm{H}_{12}$ | $\mathrm{H}_{21}$ | $\mathrm{H}_{22}$ | $\mathrm{H}_{31}$ | $\mathrm{H}_{32}$ | $\mathrm{VND}_{011}$ | $\mathrm{VND}_{012}$ | $\mathrm{VND}_{021}$ | $\mathrm{VND}_{022}$ | $\mathrm{VND}_{031}$ | $\mathrm{VND}_{032}$ | $\mathrm{EDAMA}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 4 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 4.39 | 6.79 | 2.90 | 7.67 | 2.55 | 42.87 | 22.06 |
| F 6 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 3.49 | 7.73 | 2.85 | 8.94 | 1.95 | 6.11 | 22.84 |
| 8 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 3.26 | 9.56 | 1.86 | 10.21 | 1.83 | 20.64 | 24.58 |
| 30 | 0.01 | 0.01 | 0.02 | 0.02 | 0.01 | 0.01 | 3.64 | 8.05 | 3.14 | 11.00 | 2.70 | 45.20 | 23.22 |
| s 40 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 3.59 | 7.12 | 2.45 | 8.05 | 1.96 | 5.54 | 23.31 |
| 50 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 3.91 | 8.91 | 2.02 | 7.77 | 1.66 | 18.88 | 22.96 |
| 100 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 1.09 | 2.84 | 0.27 | 0.72 | 0.24 | 0.43 | 3.57 |
| n 200 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 2.02 | 3.85 | 0.58 | 2.22 | 0.66 | 1.37 | 11.27 |
| 500 | 0.03 | 0.02 | 0.03 | 0.04 | 0.03 | 0.02 | 8.03 | 17.39 | 6.76 | 23.88 | 5.41 | 67.81 | 54.65 |
| Average | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 3.71 | 8.03 | 2.54 | 8.94 | 2.11 | 23.20 | 23.16 |

The average RPD value obtained by the EDAMA is -0.07 , which implies that some of the best-known solutions are updated by EDAMA. In particular, EDAMA obtains new best makespan values for 87 small-scaled instances.

## E. Results and Comparison for Large-Scaled Instances

Next, EDAMA is tested by using large-scaled instances. Considering number of factories, products, and jobs, a summarized result of average RPD is shown in Table XI.

Form Table XI, it can be seen that EDAMA outperforms the other algorithms in solving all the groups of large-scaled instances. In particular, EDAMA obtains new best makespan values for 94 large-scaled instances. In addition, the CPU time spent by the algorithms is listed in Table XII. The EDAMA is implemented with Intel Core i5/2.3 GHz processor. The other algorithms are carried out with Intel XEON E5420/2.5 GHz processor.

From Table XII, it can be seen that EDAMA spends more time than most heuristics. However, the efficiency of the EDAMA is at the same level of $\mathrm{VND}_{I I 32}$. The large-scaled instances are solved by EDAMA within an average of 23.16 s . Considering the effectiveness of EDAMA, it is acceptable to spend a little more time for obtaining better solutions.

## F. Discussion of Experimental Results

In the above sections, the performance of EDAMA is tested and compared with existing algorithms by using 900 small-scaled instances and 810 large-scaled instances. From the comparative results, it can be concluded that EDAMA outperforms the state-of-the-art in solving the benchmark instances. Especially, the best-known solutions of 87 small-scaled instances and 94 large-scaled instances are updated by EDAMA. The effectiveness of EDAMA in solving the DAPFSP owes to the following aspects.

1) The EDA-based exploration is effective by using a welldesigned probability model and suitable updating mechanism. The selective-enhancing sampling mechanism is helpful to obtain a schedule with small makespan.
2) The CPLS is capable of enhancing the exploitation in the promising region. The CPLS-based exploitation is also efficient since some invalid search can be forbidden.
3) The hybridization of the EDA and CPLS within an MA framework can well balance the global and local exploitations.

## V. CONCLUSION

In this paper, an effective EDAMA is proposed for the DAPFSP. To the best of our knowledge, this is the first reported work of the EDA-based algorithm for the DAPFSP. Within the MA framework, the EDA-based exploration and local-search-based exploitation are integrated. For the exploration phase, a probability model is built to describe the probability distribution of superior solutions. Besides, a novel selective-enhancing sampling mechanism is proposed for generating new solutions by sampling the probability model. The effectiveness of the proposed sampling mechanism is shown by comparing with uniform sampling mechanism. For the exploitation phase, a CPLS strategy is proposed to perform exploitation for potential solutions. The CPLS strategy can be adopted in other evolutionary algorithms to enhance the exploitation ability. In addition, the effect of parameter setting is investigated based on the Taguchi method of DOE. Suitable parameters are suggested for instances with different scales. Finally, numerical simulations based on 1710 benchmark instances are carried out. The results and comparison with existing algorithms show the effectiveness and efficiency of the proposed EDAMA. Moreover, the best-known solutions of 181 instances are updated. As for the future work, distributed job-shop scheduling problems as well as multiobjective scheduling problems are worth being studied based on EDA.

## REFERENCES

[1] B. B. Li, L. Wang, and B. Liu, "An effective PSO-based hybrid algorithm for multi-objective permutation flow shop scheduling," IEEE Trans. Syst., Man, Cybern. A, Syst., Humans, vol. 38, no. 4, pp. 818-831, Jul. 2008.
[2] Y. Yin, M. Liu, J. Hao, and M. Zhou, "Single-machine scheduling with job-position-dependent learning and time-dependent deterioration," IEEE Trans. Syst., Man, Cybern. A, Syst., Humans, vol. 42, no. 1, pp. 192-200, Jan. 2012.
[3] D. Li, M. Li, X. Meng, and Y. Tian, "A hyperheuristic approach for intercell scheduling with single processing machines and batch processing machines," IEEE Trans. Syst., Man, Cybern., Syst., vol. 45, no. 2, pp. 315-325, Feb. 2015.
[4] C. Y. Lee, T. C. E. Cheng, and B. M. T. Lin, "Minimizing the makespan in the 3-machine assembly-type flowshop scheduling problem," Manage. Sci., vol. 39, no. 5, pp. 616-625, May 1993.
[5] C. N. Potts, S. V. Sevast'janov, V. A. Strusevich, L. N. Van Wassenhove, and C. M. Zwaneveld, "The two-stage assembly scheduling problem: Complexity and approximation," Oper. Res., vol. 43, no. 2, pp. 346-355, Mar. 1995.
[6] C. Koulamas and G. J. Kyparisis, "The three-stage assembly flowshop scheduling problem," Comput. Oper. Res., vol. 28, no. 7, pp. 689-704, Jun. 2001.
[7] A. Tozkapan, O. Kirca, and C. S. Chung, "A branch and bound algorithm to minimize the total weighted flowtime for the two-stage assembly scheduling problem," Comput. Oper. Res., vol. 30, no. 2, pp. 309-320, Feb. 2003.
[8] A. Allahverdi and F. S. Al-Anzi, "A PSO and a Tabu search heuristics for the assembly scheduling problem of the two-stage distributed database application," Comput. Oper. Res., vol. 33, no. 4, pp. 1056-1080, Apr. 2006.
[9] F. S. Al-Anzi and A. Allahverdi, "A self-adaptive differential evolution heuristic for two-stage assembly scheduling problem to minimize maximum lateness with setup times," Eur. J. Oper. Res., vol. 182, no. 1, pp. 80-94, Oct. 2007.
[10] A. Mozdgir, S. M. T. F. Ghomi, F. Iolai, and J. Navaei, "Two-stage assembly flow-shop scheduling problem with non-identical assembly machines considering setup times," Int. J. Prod. Res., vol. 51, no. 12, pp. 3625-3642, Jun. 2013.
[11] C. Moon, J. Kim, and S. Hur, "Integrated process planning and scheduling with minimizing total tardiness in multi-plants supply chain," Comput. Ind. Eng., vol. 43, no. 1, pp. 331-349, Jul. 2002.
[12] L. Wang and W. Shen, Process Planning and Scheduling for Distributed Manufacturing, London, U.K.: Springer, 2007.
[13] K. B. Kahn, G. A. Castellion, and A. Griffin, The PDMA Handbook of New Product Development, New York, NY, USA: Wiley, 2004.
[14] B. Naderi and R. Ruiz, "The distributed permutation flowshop scheduling problem," Comput. Oper. Res., vol. 37, no. 4, pp. 754-768, Apr. 2010.
[15] H. Z. Jia, J. Y. H. Fuh, A. Y. C. Nee, and Y. F. Zhang, "Web-based multi-functional scheduling system for a distributed manufacturing environment," Concurr. Eng. Res. A., vol. 10, no. 1, pp. 27-39, Mar. 2002.
[16] H. Z. Jia, A. Y. C. Nee, J. Y. H. Fuh, and Y. F. Zhang, "A modified genetic algorithm for distributed scheduling problems," J. Intell. Manuf., vol. 14, nos. 13-14, pp. 351-362, Jun. 2003.
[17] H. Z. Jia, J. Y. H. Fuh, A. Y. C. Nee, and Y. F. Zhang, "Integration of genetic algorithm and Gantt chart for job shop scheduling in distributed manufacturing systems," Comput. Ind. Eng., vol. 53, no. 2, pp. 313-320, Sep. 2007.
[18] F. T. S. Chan, S. H. Chung, and P. L. Y. Chan, "An adaptive genetic algorithm with dominated genes for distributed scheduling problems," Expert. Syst. Appl., vol. 29, no. 2, pp. 364-371, Aug. 2005.
[19] F. T. S. Chan, S. H. Chung, L. Y. Chan, G. Finke, and M. K. Tiwari, "Solving distributed FMS scheduling problems subject to maintenance: Genetic algorithms approach," Robot. Comput. Integr. Manuf., vol. 22, no. 5, pp. 493-504, Oct. 2006.
[20] L. De Giovanni and F. Pezzella, "An improved genetic algorithm for the distributed and flexible job-shop scheduling problem," Eur. J. Oper. Res., vol. 200, no. 2, pp. 395-408, Jan. 2010.
[21] J. Gao, R. Chen, and W. Deng, "An efficient Tabu search algorithm for the distributed permutation flowshop scheduling problem," Int. J. Prod. Res., vol. 51, no. 3, pp. 641-651, Feb. 2013.
[22] S. W. Lin, K. C. Ying, and C. Y. Huang, "Minimising makespan in distributed permutation flowshops using a modified iterated greedy algorithm," Int. J. Prod. Res., vol. 51, no. 16, pp. 5029-5038, Aug. 2013.
[23] S. Y. Wang, L. Wang, M. Liu, and Y. Xu, "An effective estimation of distribution algorithm for solving the distributed permutation flow-shop scheduling problem," Int. J. Prod. Econ., vol. 145, no. 1, pp. 387-396, Sep. 2013.
[24] S. Hatami, R. Ruiz, and C. Andrés-Romano, "The distributed assembly permutation flowshop scheduling problem," Int. J. Prod. Res., vol. 51, no. 17, pp. 5292-5308, Sep. 2013.
[25] X. Chen, Y. S. Ong, M. H. Lim, and K. C. Tan, "A multi-facet survey on memetic computation," IEEE Trans. Evol. Comput., vol. 15, no. 5, pp. 591-607, Oct. 2011.
[26] Q. H. Nguyen, Y. S. Ong, and M. H. Lim, "A probabilistic memetic framework," IEEE Trans. Evol. Comput., vol. 13, no. 3, pp. 604-623, Jun. 2009.
[27] B. Liu, L. Wang, and Y. H. Jin, "An effective PSO-based memetic algorithm for flow shop scheduling," IEEE Trans. Syst. Man, Cybern. B, Cybern., vol. 37, no. 1, pp. 18-27, Feb. 2007.
[28] L. Y. Tseng and S. C. Chen, "Two-phase genetic local search algorithm for the multimode resource-constrained project scheduling problem," IEEE Trans. Evol. Comput., vol. 13, no. 4, pp. 848-857, Aug. 2009.
[29] P. Rakshit et al., "Realization of an adaptive memetic algorithm using differential evolution and Q-learning: A case study in multirobot path planning," IEEE Trans. Syst., Man, Cybern., Syst., vol. 43, no. 4, pp. 814-831, Jul. 2013.

[30] Y. Mei, K. Tang, and X. Yao, "A memetic algorithm for periodic capacitated arc routing problem," IEEE Trans. Syst. Man, Cybern. B, Cybern., vol. 41, no. 6, pp. 1654-1667, Dec. 2011.
[31] D. Liu, K. C. Tan, C. K. Goh, and W. K. Ho, "A multiobjective memetic algorithm based on particle swarm optimization," IEEE Trans. Syst. Man, Cybern. B, Cybern., vol. 37, no. 1, pp. 42-50, Feb. 2007.
[32] M. Tang and X. Yao, "A memetic algorithm for VLSI floorplanning," IEEE Trans. Syst. Man, Cybern. B, Cybern., vol. 37, no. 1, pp. 62-69, Feb. 2007.
[33] D. Hrncic, M. Mernik, and B. R. Bryant, "Improving grammar inference by a memetic algorithm," IEEE Trans. Syst., Man, Cybern. C, Appl. Rev., vol. 42, no. 5, pp. 692-703, Sep. 2012.
[34] P. Larranaga and J. A. Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Boston, MA, USA: Kluwer, 2002.
[35] J. Ceberio, E. Irurozki, A. Mendiburu, and J. A. Lozano, "A review on estimation of distribution algorithms in permutation-based combinatorial optimization problems," Progr. Artif. Intell., vol. 1, no. 1, pp. 103-117, Apr. 2012.
[36] L. Wang and C. Fang, "An effective estimation of distribution algorithm for the multi-mode resource-constrained project scheduling problem," Comput. Oper. Res., vol. 39, no. 2, pp. 449-460, Feb. 2012.
[37] B. Jarboui, M. Eddaly, and P. Siarry, "An estimation of distribution algorithm for minimizing the total flowtime in permutation flowshop scheduling problems," Comput. Oper. Res., vol. 36, no. 9, pp. 2638-2646, Sep. 2009.
[38] S. H. Chen, M. C. Chen, P. C. Chang, Q. Zhang, and Y. M. Chen, "Guidelines for developing effective estimation of distribution algorithms in solving single machine scheduling problems," Expert. Syst. Appl., vol. 37, no. 9, pp. 6441-6451, Sep. 2010.
[39] S. Y. Wang, L. Wang, M. Liu, and Y. Xu, "An enhanced estimation of distribution algorithm for solving hybrid flow-shop scheduling problem with identical parallel machines," Int. J. Adv. Manuf. Technol., vol. 68, nos. 9-12, pp. 2043-2056, Oct. 2013.
[40] L. Wang, S. Y. Wang, Y. Xu, G. Zhou, and M. Liu, "A bi-population based estimation of distribution algorithm for the flexible job-shop scheduling problem," Comput. Ind. Eng., vol. 62, no. 4, pp. 917-926, May 2012.
[41] U. Aickelin and J. Li, "An estimation of distribution algorithm for nurse scheduling," Ann. Oper. Res., vol. 155, no. 1, pp. 289-309, Nov. 2007.
[42] T. Suraç and A. Sipahioglu, "Generalized quadratic multiple knapsack problem and two solution approaches," Comput. Oper. Res., vol. 43, pp. 78-89, Mar. 2014.
[43] J. Grabowski and M. Wodecki, "A very fast Tabu search algorithm for the permutation flow shop problem with makespan criterion," Comput. Oper. Res., vol. 31, no. 11, pp. 1891-1909, Sep. 2004.
[44] D. C. Montgomery, Design and Analysis of Experiments. Hoboken, NJ, USA: Wiley, 2005.
![img-8.jpeg](img-8.jpeg)

Sheng-Yao Wang received the B.Sc. degree from Tsinghua University, Beijing, China, in 2010, where he is currently pursuing the Ph.D. degree.

His current research interests include manufacturing scheduling and intelligent optimization methods.
![img-9.jpeg](img-9.jpeg)

Ling Wang received the B.Sc. and Ph.D. degrees from Tsinghua University, Beijing, China, in 1995 and 1999, respectively.

Since 1999, he has been with the Department of Automation, Tsinghua University, where he became a Full Professor in 2008. His current research interests include intelligent optimization and scheduling. He has authored five academic books and over 200 referred papers.

Prof. Wang was a recipient of the Outstanding Paper Award at the International Conference on Machine Learning and Cybernetics in 2002, the Best Paper Award at the International Conference on Intelligent Computing in 2011, the Top Cited Article Award by the Engineering Applications of Artificial Intelligence (Elsevier), the National Natural Science Award (Second Place) in 2014, the Science and Technology Award of Beijing City in 2008, and the Natural Science Award (First Place in 2003, and Second Place in 2007) nominated by the Ministry of Education (MOE) of China. He was the Rising Star of Science and Technology of Beijing City in 2004, the Academic Young Talent of Tsinghua University in 2009, and the Program for New Century Excellent Talents in University by the MOE of China in 2009. He is the Co-Editor-in-Chief for the Open Operational Research Journal. He was a reviewer for several IEEE journals such as the IEEE Transactions on Automation Science and Engineering, the IEEE Computational Intelligence Magazine, the IEEE Transactions on Evolutionary Computation, the IEEE Transactions on Neural Networks, and the IEEE Transactions on Systems, Man, and Cybernetics. He is an Editorial Board Member for several journals, including Memetic Computing, Swarm and Evolutionary Computation, the International Journal of Automation and Control, and the International Journal of Artificial Intelligence and Soft Computing.