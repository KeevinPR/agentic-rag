# An estimation of distribution algorithm with multiple intensification strategies for two-stage hybrid flow-shop scheduling problem with sequence-dependent setup time 

Huan Liu ${ }^{1,2}$ (D) $\cdot$ Fuqing Zhao ${ }^{1}$ $\cdot$ Ling Wang ${ }^{3} \cdot$ Jie Cao ${ }^{1} \cdot$ Jianxin Tang ${ }^{1} \cdot$ Jonrinaldi ${ }^{4}$

Accepted: 15 May 2022 / Published online: 20 June 2022
(C) The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2022


#### Abstract

The estimation of distribution algorithm (EDA) has recently emerged as a promising alternative to the traditional evolutionary algorithms for solving combinatorial optimization problems. In this paper, an estimation of distribution algorithm with multiple intensification strategies (EDA-MIS) is proposed to solve a typical kind of hybrid flow-shop scheduling problem. The two-stage heterogeneous hybrid flow-shop scheduling problem is investigated. The sequence-dependent setup time at the first stage is also considered. In the proposed EDA-MIS, the initial population is constructed through the heuristic method and random strategy. An order matrix is established to estimate the probabilistic model of promising solutions. Then the solutions of the algorithm are evolved through the processes of selection, recombination, sampling, and local search. The obtained results indicate that the EDA-MIS provides good solutions in the aspects of solution quality and computational efficiency.


Keywords Hybrid flow-shop scheduling problem $\cdot$ Sequence-dependent setup time $\cdot$ Estimation of distribution algorithm $\cdot$ Local search

## 1 Introduction

Scheduling is one of the most important research issues in steelmaking, textile, logistics, electronic components manufacturing, and other smart manufacturing fields [1-3]. Effective scheduling schemes can significantly reduce the production costs and the production cycle and improve the economic efficiency of enterprises [4]. The hybrid flow-shop scheduling problem (HFSP) is a kind of model that extends from the traditional flow-shop scheduling problem (FSP). In the HFSP, the processing of jobs is divided into several stages, where each stage has several machines to be selected [5]. This

[^0]model has some key problems that need to be solved, such as arranging the process sequence of jobs and selecting the right machine at different stages. The objective of scheduling is to reduce the corresponding production indicators, such as production cycle and total flow time [6].

Aiming at the actual workshop conditions of the production process, various studies have introduced several constraints into the basic HFSP [7, 8]. Considering the constraints of stage skipping and adjustable processing time, Long presented a realistic HFSP model that was extracted from the steelmaking-continuous casting production process [9]. Cai and Lei studied a distributed hybrid flow-shop scheduling

```
Jonrinaldi
jonrinaldi@eng.unand.ac.id
    School of Computer and Communication Technology, Lanzhou
    University of Technology, Lanzhou, China
College of Information Science and Technology, Gansu Agricultural
    University, Lanzhou 730070, China
    Department of Automation, Tsinghua University, Beijing 10084,
    China
    Department of Industrial Engineering, University Andalas,
    Padang 25163, Indonesia
```


[^0]:    52 Fuqing Zhao
    FZhao2000@hotmail.com

    Huan Liu
    liuh1204@hotmail.com
    Ling Wang
    wangling@tsinghua.edu.cn
    Jie Cao
    caoj2976016@qq.com
    Jianxin Tang
    582971672@qq.com

problem (DHFSP) with fuzzy processing time, and proposed a cooperated shuffled frog-leaping algorithm (CSFLA) to simultaneously optimize the fuzzy makespan, total agreement index, and fuzzy total energy consumption [10]. Li et al. studied the distributed heterogeneous hybrid flow-shop scheduling problem (DHHFSP) with unrelated parallel machines (UPM) and the sequence-dependent setup time (SDST) [11]. Meng et al. provided some mixed integer-linear programming (MILP) models of HFSP-UPM [12]. The energy consumption of HFSP-UPM has been analyzed in [13]. Zhong and Shi addressed the two-stage no-wait hybrid flow-shop scheduling problem with inter-stage flexibility in [14]. In [15], the HFSP with blocking and due window constraints has been tackled. Chamnanlor et al. studied a reentrant HFSP with time window constraints [16]. Several studies developed algorithms by adding the constraint of sequence-dependent setup time into the HFSP to solve the problem [17-20]. With the development of technology, distributed manufacturing has become the main mode of production in the manufacturing industry. In some studies, the HFSP has been extended to distributed manufacturing environments [7, 21].

The above-mentioned studies have proposed constraints on the relevant production models based on the actual production conditions and business needs. The constraints of the production models vary significantly in different types of machining plants [22-24]. Some studies proposed the relevant model constraints based on the production plants of glass, textile, and food processing to fit the actual production conditions. However, such production workshops differ from the rare earth production workshops in terms of production structure and production constraints. In this paper, an HFSP model with sequence-dependent setup time is constructed from the actual production shop of rare earth.

The two-stage HFSP with makespan minimization is an NP-hard problem. Recently, in the field of combinational optimization research, the HFSP has been regarded as an important research direction and an innovative theoretical method to optimize the problem. The main methods for HFSP can be divided into several categories: exact solution method [25], heuristic construction method [26], bio-inspired intelligent optimization method [27], multi-objective optimization algorithm [28-30] and hybrid method [21]. Zhang et al. introduced the constraint of lot streaming into the HFSP and developed a collaborative variable neighborhood descent (CVND) algorithm [31]. H. Öztop et al. presented four variants of iterated greedy algorithm and a variable block insertion heuristic for the HFSP with total flowtime minimization [26]. Luo et al. proposed hybrid branch and bound algorithms to minimize the makespan for the two-stage assembly scheduling problem with separated setup time [32]. Zhao et al. proposed an optimal block knowledge-driven backtracking search algorithm (BKBSA) to solve the distributed assembly no-wait flow-shop scheduling problem (DANWFSP) [33]. In the above-
mentioned methods, the improvements of the algorithm effectiveness are still substantially conducted based on the balance of intensification and diversification. The characteristics of the problem and the execution process of the algorithm are not organically integrated.

The estimation of distribution algorithm (EDA) has been widely used in scheduling problems as a meta-heuristic method. The EDA algorithm comes with a natural learning mechanism based on the evolution of probabilistic models. The process of the EDA algorithm is divided into sampling, selection, recombination, and updating of the probability model. The update of the probability model is based on the selected individuals of the population. The probability model directly affects the quality of the algorithm candidate solution and determines the optimization efficiency of the algorithm. In [34], the path relinking enhanced estimation of distribution algorithm has been proposed for the direct acyclic graph task scheduling problem. Sun and Gu proposed an effective hybrid estimation of distribution algorithm to solve the HFSP with an unrelated parallel machine [35]. The EDA structure and the teaching learning-based optimization (TLBO) strategy were used for global and local searches, respectively. Du et al. introduced a hybrid EDA for distributed flexible job shop scheduling with crane transportations [36]. An identification rule of four crane conditions was designed to make fitness calculation feasible. In the EDA component, the parameters in probability matrices are set to be self-adaptive for stable convergence to obtain better output. In the variable neighborhood search (VNS) component, five problem-specific neighborhood structures including global and local strategies are employed to enhance exploitation ability.

This paper optimizes the production process of the rare earth. The mathematical model, a two-stage heterogeneous hybrid flow-shop scheduling problem with sequencedependent setup time constraints (TSHHFSP with SDST), is extracted from the process of ion exchange in the immersion pond during the production of rare earth oxides. The objective of this optimization problem is the maximum completion time of jobs. According to the no free lunch theorem for optimization, the existing approaches may not be effective for solving the TSHHFSP with SDST. Therefore, it is a challenge to develop effective and efficient algorithms for TSHHFSP with SDST, especially for large-sized problems. In this paper, an estimation of the distribution algorithm with multiple intensification strategies (EDA-MIS) is proposed to solve the TSHHFSP model with SDST. The proposed algorithm is based on the framework of the EDA algorithm. The model studied in this paper incorporates a constraint of the sequencedependent setup time. A constructive heuristic strategy is designed based on this constraint in the initialization method. The initial solutions of the algorithm are generated through the heuristic and random construction method. The probability model of EDA-MIS is constructed based on the order of

jobs in the outstanding individuals of the parent population. The neighborhood search strategy is added to the algorithm to further optimize the performance of the solutions. The fundamental contributions of this paper are summarized as follows.

- A new scheduling model named TSHHFSP with SDST is developed based on the production process of rare earth. In this model, the production capacities of all machines in a certain stage are heterogeneous. The sequencedependent setup time of the first stage is considered in the new scheduling model.
- An estimation of distribution algorithm with multiple intensification strategies is proposed to solve the TSHHFSP with SDST. In the initialization phase of the proposed algorithm, some constructive heuristics based on the knowledge of the production data are presented. The EDA and two strategies of neighborhood search are used to further intensify the candidate solutions.

The remainder of this paper is organized as follows. Section 2 presents the modeling and application of the TwoStage Heterogeneous Hybrid Flow-shop Scheduling Problem (TSHHFSP) with Sequence-Dependent Setup Time (SDST). Section 3 provides the description and detailed decoding process of the TSHHFSP with SDST. Section 3 also describes the proposed EDA-MIS algorithm. The experimental analysis of the proposed algorithm and comparison experiments are presented in Section 4. Finally, conclusions are drawn in Section 5.

## 2 Two-stage heterogeneous hybrid flow-shop scheduling problem (TSHHFSP) with sequence-dependent setup time (SDST)

The HFSP is widely used in practical production processes, such as iron, and steel casting, glass processing, and paper production. In this paper, a TSHHFSP with the constraint of SDST is constructed. This model is derived from the actual production process of rare earth (RE) metals in the northwest region of China. The entire generating process can be divided into two stages: ion exchange in the leaching pool and electrolysis of RE metals. The specific production process is shown in Fig. 1. In the ion exchange process, the electrolyte solution is configured as a leaching agent according to the proportion requirements of RE metals. The RE ore containing an ionic phase is filtered and extracted in the leaching tank. The active ions in the solution exchange with RE ions and the ionic phase of RE are exchanged from the ore carrier to become a new state of RE. The leaching agents need to be reconfigured when different RE is produced in turn. Therefore, in this paper, the TSHHFSP model with SDST is abstracted from the actual production process of RE.

The HFSP can be regarded as a combination of two kinds of scheduling problems that are flow-shop scheduling and parallel machine scheduling. The two subproblems should usually be considered, namely, the sorting of jobs and the distribution of machines in each stage. In the TSHHFSP problem with SDST, the production process is divided into two stages. Several machines need to be selected in each stage, and the machines in the same stage are heterogeneous. There are $n$ jobs to be processed in the initial time. All jobs are processed from Stage 1 to Stage 2. The process of job $j \in J$ in machine $i$ of stage $k$ cannot be interrupted. The processing time of job $j$ $\in J$ in machine $i$ of stage $k$, named as $p_{j i k}$, is positive. At the same time, the job and the machine have a one by one relationship. In the first process stage of the job $j \in J$, the setup times of the jobs are sequence-dependent, as $s t_{k j q}$. All machines and jobs are available to be processed at time zero and job preemption is not allowed. The capacity of intermediate buffers between stages is unlimited. The travel time between consecutive stages is included in the processing times of jobs at the corresponding stages. The problem data is assumed to be deterministic and known in advance. The notations for the problem are listed in Table 1.

The TSHHFSP model with SDST aims to find a schedule that optimizes the maximum completion time (makespan). The problem can be denoted as $F H 2,\left(\left.R M^{(k)}\right|_{k=1} ^{2}\right)\left|S_{s d}^{(1)}\right|$ $C_{\max }$ according to the notation proposed by Vignier et al. [37], which follows the three-fields notation of [38]. The problem is NP-hard since the standard two-stage HFSP is known to be NP-hard [39].

The Mixed Integer Linear Planning (MIP) model of the TSHHFSP with SDST with the maximum completion time objective is constructed as follows.

Objective:
$\operatorname{Minimize}\left(\max C_{j}\right)$
Subject to:
$C_{j}=s_{2 j}+\sum_{i \in I_{2}} x_{j i 2} p_{j i 2}, \quad \forall j \in J$

$$
\begin{aligned}
& \sum_{i \in I_{k}} x_{j i k}=1, \quad \forall j \in J, k \in M \\
& s_{k j}+\sum_{i \in I_{k}} x_{j i k} p_{j i k}+s t_{k j q} \leq s_{k+1, j} \quad \forall j, q \in J,(k, k+1) \in M \\
& s_{k j} \sim\left(s_{k r}+\sum_{i \in I_{k}} x_{r i k} p_{r i k}+s t_{k r q}\right) \\
& \quad+Q\left(2+y_{k j r}-x_{j i k}-x_{r i k}\right) \geq 0, \quad \forall j, r, q \in J \\
& \quad: j<r, k \in M, i \in I_{k}
\end{aligned}
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1 The production process of rare earth metal

$$
\begin{aligned}
& s_{k r}-\left(s_{k j}+\sum_{i \in I_{k}} x_{j i k} p_{j i k}+s t_{k j q}\right) \\
& \quad+Q\left(3-y_{k j r}-x_{j i k}-x_{r i k}\right) \geq 0 \quad \forall j, r, q \in J \\
& \quad: j<r, k \in M, i \in I_{k} \\
& s_{k j}>0 \quad \forall k \in M, j \in J \\
& y_{k j r} \in\{0,1\} \quad \forall k \in M, j, r \in J \\
& x_{j i k} \in\{0,1\} \quad \forall j \in J, i \in I_{k}, k \in M \\
& \text { if } k=2, s t_{k j q}=0, \quad \forall j, q \in J, k \in M
\end{aligned}
$$

Table 1 Problem notations

The objective function (1) minimizes the maximum completion time. Constraint set (2) calculates the completion time of each job. Constraint set (3) guarantees that each job passes through all stages and is processed by exactly one machine at each stage. Constraint set (4) ensures that the next operation of a job starts only after its previous operation is completed. Constraint sets (5) and (6) prevent the overlapping of any two jobs on the same machine and define the sequence of the jobs. For any two jobs assigned to the same machine, the next job can start after the previous one is completed. Constraint set (7)-(10) defines the domains of decision variables.

## 3 The encoding strategy and numerical illustration

The effectiveness of a metaheuristic algorithm relies on the performance of encoding and decoding methods. Job permutation-based encoding method is the most widely used encoding method. The encoding and decoding methods of HFSP are different from the traditional permutation FSP. In the permutation FSP, the coding process is executed based on the sequence of processing jobs. In the decoding process, the sequence of the jobs is determined according to the coding sequence. Then the maximum completion time is calculated based on the processing time and job sequence.

The certain solution of the HFSP can be transformed into a specific code through the encoding method. The encoding method can be understood as a representation of the modern heuristic. A representation assigns the genotypes of the HFSP solution to corresponding phenotypes. The job permutationbased encoding method can effectively clarify the processing details. In the mutation phase of EDA, the probabilistic model is efficiently constructed by the job permutation-based encoding method. The locality of a representation describes how well the neighboring genotypes correspond to the round neighboring phenotypes. A representation with high locality means that the neighboring genotypes correspond neighboring phenotypes. The job permutation-based encoding method is a representation with a high locality. The job permutationbased encoding method is illustrated in Fig. 2.

An example of TSHHFSP with SDST is given as follows. In this instance, there are 10 jobs to be processed. The numbers of machines in the two stages are 2 and 3 . The instance is labeled as $\{10,(2,3)\}$. The matrix of process time is generated randomly as shown in Table 2.

Assuming that job $q$ is the successor of job $j$, the matrix of the sequence-dependent setup time $s t_{k j q}$ is randomly generated as Table 3.

The scheduling solution and its makespan can be generated based on the production data. Fig. 3 shows the Gannet diagram of a scheduling solution. The maximum competition time of the 10 jobs is the competition time of Job 2 and the makespan is 384 .

Table 2 The matrix of process time $p_{j d}$
In the HFSP, the machine allocation of stages should be considered in the process of coding and decoding. The coding rule used in this paper is still based on the job sequence. In the decoding process, the machine with the earliest completion time is selected for processing. In the second processing stage, the job completed early in the first stage is processed preferentially. For example, the sequence of operation in Fig. 3 is $(8,5,6,4,9,10,7,3,2,1)$. Job 9 precedes Job 10 in the first processing stage. The processing time of Job 9 is much longer than that of Job 10. Thus, Job 10 prepares early than Job 9 in the second processing stage. Then Job 10 precedes Job 9 in the
![img-1.jpeg](img-1.jpeg)

Fig. 2 The job permutation-based representation of the TSHHFSP with SDST solution

Table 3 The matrix of sequence-dependent setup time $s t_{h t g}$
second processing stage. Under this coding rule, the job sequence in Fig. 3 can be coded as $\pi=\{8,5,6,4,9,10,7,3$, $2,1\}$. In the decoding process, the process details can be obtained through the analysis of this code and are shown in Table 4.

## 4 The proposed EDA-MIS algorithm

### 4.1 The framework of the EDA-MIS algorithm

In the proposed EDA-MIS algorithm, the initial solutions are generated by the heuristic method and the stochastic method. In the evolutionary process, the candidate solutions of the algorithm are optimized by the EDA algorithm. Then the individuals in the population evolve ulteriorly by the strategy of neighborhood search. The specific process of the proposed EDA-MIS is shown in Algorithm 1.

## Algorithm 1: EDA-MIS Algorithm

Input: Produce Data
Output: Optimal Makespan
Initialization of algorithm parameters;
Initialization of population;
while The termination conditions are not met do
Selection;
Update of the probability model;
Sampling the new population;
Neighborhood search;
end
The EDA-MIS algorithm can learn the implicit knowledge of the HFSP in the evolutionary process and that knowledge can be used to decide the job sequence in the next generation. Figure 4 illustrates the framework of the proposed EDA-MIS algorithm.

The probability distribution model is constructed according to the excellent individuals of the candidate solution in the evolutionary process of EDA. The individuals of the next generation are obtained by sampling based on the probability distribution model. Then, the individuals are optimized by performing selection, model mutation, resampling, and other operations, until a certain stopping criterion is met. In this paper, an order matrix $\phi$ is constructed to count the order of jobs in the excellent individuals of the population.
$\phi=\left[\begin{array}{cccccc}\varphi_{1,1} & \varphi_{1,2} & \varphi_{1,3} & \cdots & \varphi_{1, n} \\ \varphi_{2,1} & \varphi_{2,2} & \varphi_{2,3} & \cdots & \varphi_{2, n} \\ \varphi_{3,1} & \varphi_{3,2} & \varphi_{3,3} & \cdots & \varphi_{3, n} \\ \cdots & \cdots & \cdots & \cdots & \cdots \\ \varphi_{n, 1} & \varphi_{n, 2} & \varphi_{n, 3} & \cdots & \varphi_{n, n}\end{array}\right]$
Where $\varphi_{j, i}$ is used to count the number of times job $j$ appears in and before the position $i$. The order matrix $\phi$ describes the order of jobs in the processing sequence. A new probability distribution model $P$ is obtained by normalizing

Fig. 3 A feasible scheduling solution of $\{10,(2,3)\}$ instance
![img-2.jpeg](img-2.jpeg)

Table 4 The details of the decoding processing
the order matrix and learning from the distribution model of the previous generation.
$P=\left[\begin{array}{cccccc}p_{1,1} & p_{1,2} & p_{1,3} & \cdots & p_{1, n} \\ p_{2,1} & p_{2,2} & p_{2,3} & \cdots & p_{2, n} \\ p_{3,1} & p_{3,2} & p_{3,3} & \cdots & p_{3, n} \\ \cdots & \cdots & \cdots & \cdots & \cdots \\ p_{n, 1} & p_{n, 2} & p_{n, 3} & \cdots & p_{n, n}\end{array}\right]$
The probability statistical model $P$ describes the probability distribution of the location of each job in the processing sequence. The individuals of the next generation are sampled from model $P$. The probability model is obtained by the previous probability model and the order matrix of the current generation. The specific update formula is as follows:

$$
P^{(g+1)}=\alpha P^{(g)}+(1-\alpha) \text { normlise }\{\phi\}
$$

where $\alpha$ is the learning factor and normlise $\{\phi\}$ represent the normalization results of the order matrix $\phi$.
![img-3.jpeg](img-3.jpeg)

Fig. 4 The framework of the proposed EDA-MIS algorithm

### 4.2 Heuristic rules

The HFSP is the coupling of many scheduling problems, including the combination optimization of job sequence and the choice of the processing machine. This paper studies the TSHHFSP with the constraint of SDST. Thus, compared with the traditional HFSP model, the reduction of the total sequence-dependent setup time should be considered when scheduling the job sequences. In this paper, several heuristic construction rules are proposed for the above research problems, which provide the initial solutions for the meta-heuristic algorithm.

## 1. Heuristic rule 1

The constraint of SDST is considered in the study model. In the model of this paper, there is no setup time before the first machining job of each machine. Therefore, the jobs with the largest setup time are operated preferentially in the construction heuristic method to avoid the maximum value of the SDST. The maximum value of SDST is found to decide which job operates first. Such as the maximum setup time in Table 3 is setup time from Job 2 to Job 8, i.e. $s t_{k 28}$. Then the successor job of this setup time, which is Job 8 , is chosen as the first machining job. Assuming that there are $k$ machines in the first stage. In this example, $k$ is 2 . The $k$ th maximum value is found in turn from the remaining SDST, the $s t_{k 36}$ of Table 3 is picked up. The successor jobs of these setup times, Jobs 6, are chosen as the first machining job in the remaining machines of the first stage. According to the above process, the first machining jobs in the machines of the first stage are determined. The job with the lowest setup time is identified as the subsequent machining job. This operation is repeated until all jobs are scheduled for processing in the first stage. The final processing sequence is obtained, the result of Table 3 is $\{8,6,4,10,2,7,3,9,5,1\}$.

```
Algorithm 2: Heuristic Rule 1
    Input: Process parameters \(s t_{k j q}\)
    Output: Process sequence \(\pi\) at stage 1
    Process parameters initialization;
    \(\max \left(s t_{k j q}\right)=s t_{k, a, b}\);
    Select job \(b\) as the first process job;
    Add \(b\) to process sequence \(\pi\);
    pre_job \(=b\);
    job_npset \(=1,2,3, \ldots, b-1, b+1, \ldots, n\);
    while distribution of jobs is not end do
        \(\min _{q \in j o b \_n p s e t}\left(k, s t_{\text {pre_ } \_j o b, q}\right)=s t_{k, p r e \_j o b, x}\);
        select job \(x\) as the next process job;
        Add \(x\) to process sequence \(\pi\);
        job_npset \(=\) job_npset \(-x\);
        pre_job \(=x\);
    end
```

2. Heuristic rule 2

In this paper, the proposed TSHHFSP problem with SDST consists of two stages. The start time of the second stage directly determines the final makespan. The jobs are processed as the planned sequence, in which the start time of each machine in the second stage is early as possible. In this heuristic construction method, the jobs, as well as the processed machines, with the shortest processing time in the first stage are identified in turn. Such as the processing time of Job 1 on machine 1 and Job 10 on machine 2 in Table 2 are selected. Then the jobs with the earliest completion time on each machine in the first stage are processed as successors.

```
Algorithm 3: Heuristic Rule 2
    Input: Process parameters \(p_{i j}\)
    Output: Process sequence \(\pi\) at stage 1
    Process parameters initialization;
    job_npset \(=J\);
    while \(i\) in the machine set of stage \(1, I_{1}\) do
        \(\min _{j \in J}\left(p_{i j}\right)=p_{i, x_{i}} ;\)
        \(x_{i}\) are not equal to the selected jobs;
        Add \(x_{i}\) to process sequence \(\pi\);
        job_npset \(=J-x_{i}\);
    end
    while distribution of jobs is not end do
        Update the earliest completion time of \(I_{1}\);
        \(\min \left(c_{i}\right)=c_{y}, i \in I_{1}\);
        \(\min _{j \in J}\left(p_{y j}\right)=p_{y, a}\);
        select job \(a\) as the next process job;
        Add \(a\) to process sequence \(\pi\);
        job_npset \(=\) job_npset \(-a\);
    end
```


### 4.3 Neighborhood search

In the proposed algorithm, two neighborhood search strategies are used to further optimize the performance of the population. These two strategies are reference-based neighborhood search and tabu-based neighborhood search.

## 1. Reference-based neighborhood search

In this method, the optimal individual in the population is recommended as the reference solution. The process of neighborhood search is performed based on the reference solution. Two locations $i$ and $j$, where $(i<j)$, are selected during the search process. The jobs at positions $i$ and $j$ in the reference solution are inserted into $i$ and $j$ positions of the population individuals, respectively. Then, the neighborhood search solution is obtained. The new solution is compared to the original population individual. If the performance of the new

solution is better than that of the original population individual, the original population individual is replaced by the corresponding neighborhood search solution.

```
Algorithm 4: Reference-based Neighborhood Search
    Input: Population of solution
    Output: New solutions
    Select the best individual as the reference solution;
    while indiv in the population of solution do
        random \(i, j\);
        if \((i>j)\) : swap \(i, j\);
        Select the jobs of \(i, j\) locations in the reference solution;
        Delete the two jobs from indiv;
        Insert the two jobs to the \(i, j\) locations of indiv;
        Mark the new solution as the new_indiv;
        Compare the objective of new_indiv and indiv;
        Replace indiv if new_indiv is better than indiv;
    end
```

2. Tabu-based neighborhood search

In the method, the truncated individuals of the population in the previous generation are added to the taboo table. The candidate solution is compared with the taboo table. If the candidate solution is included in the taboo table, the neighborhood search is not carried out. Otherwise, the neighborhood search is carried out. One strategy is randomly selected between swap and insertion operators for neighborhood search.

```
Algorithm 5: Tabu-based Neighborhood Search
    Input: Population of solution, Tabu table
    Output: New solutions
    while indiv in the population of solution do
        if indiv is included in the Tabu table then
            Not excute the process of neighborhood search;
        else
            Select one between insertion and swap;
            Excute the neighborhood search;
    end
end
```


### 4.4 Computational complexity of the EDA-MIS

In the proposed TSHHFSP model with SDST, the approximate optimal solution can be obtained by the EDA-MIS algorithm. The specific model is extracted from the actual production process. The computational time is an important indicator to measure the quality of the proposed algorithm. The consumed time is also an important indicator in the actual production process. In this section, the time complexity of the proposed EDA-MIS is analyzed.

Suppose that the number of the processing jobs is $n$. The numbers of machines in the two processing stages are $I_{1}$ and $I_{2}$. The population size of the proposed EDA-MIS is set as $N p$. The number of iterations is supposed as $T$. The EDA-MIS algorithm is composed of five phases, which are the initialization of the population and the other four operators for the further evolution of the solutions. In the initialization phase, the individuals are generated based on the two constructive heuristics and stochastic methods with the complexity $O\left(N p\right.$ $\times n^{2}$ ). For the sampling operation, each sequence is generated with the roulette strategy by sampling based on the probability matrix $P$. The time complexity of the sampling operator is also $O\left(N p \times n^{2}\right)$. In the selection process, the job sequence is decoded into the production details and then the objective value is obtained. The computational complexity of the selection operator is $O\left(N p \times n \times\left(I_{1}+I_{2}\right)\right)$. For model updating, the probability matrix $P$ is updated based on the selected solutions. The computational complexity of the model updating process is $O\left(N p \times n+n^{2}\right)$. Finally, the neighborhood search operator is executed for further evolution. The computational of this operator is $O\left(N p \times 2 n+N p \times n^{2}\right)$. Thus, the time complexity of the proposed EDA-MIS is calculated as follows.

$$
\begin{aligned}
& O(n, I, T, N p)=O(T) \times\left(O\left(N p \times n^{2}\right)+O\left(N p \times n \times\left(I_{1}+I_{2}\right)\right)+O\left(N p \times n+n^{2}\right)+O\left(N p \times 2 n+N p \times n^{2}\right)\right) \\
& =O(T) \times O\left(N p \times n^{2}+N p \times n \times\left(I_{1}+I_{2}\right)+N p \times n+n^{2}+N p \times 2 n+N p \times n^{2}\right) \\
& =O(T) \times O\left(2 \times N p \times n^{2}+N p \times n \times\left(I_{1}+I_{2}\right)+3 \times N p \times n+n^{2}\right) \\
& \quad \circ O(T) \times O\left(2 \times N p \times n^{2}+N p \times n \times\left(I_{1}+I_{2}\right)+n^{2}\right)
\end{aligned}
$$

## 5 Experiment and analysis

To verify the performance of the proposed EDA-MIS algorithm in solving the TSHHFSP, 140 test instances were randomly generated. The size of processed jobs is divided into 4 types, $5,10,20$, and 50 . For each size of the job, there are
various species of machine numbers. The specific test parameter combinations are shown in Table 5. Each combination of test problems contains 10 test instances. The specific processing time is a randomly generated integer between 1 to 99 . The SDST in the first stage is also a randomly generated integer between 1 to 10 .

Table 5 The list of parameters of the production process

During the experiment, each instance was solved 51 times by the algorithms [40]. The termination conditions of the experiment were set as follows: the number of iterations reaches $1000 * \mathrm{n}$ or the maximum stagnation iteration reaches 50 . All experiments were programmed in Python language and executed on a Windows 7 system. The integrated development environment of the experiment was Anaconda 3. The experimental computer processor was configured as a 2.3 GHz Intel Core i5. According to the experimental results, the average relative deviation percentage (ARPD) indicator value is selected as the evaluation indicator in this paper. The calculation formula for ARPD value is:
$A R P D=\underset{\text { ins }}{\text { Average }}\left(\frac{1}{R} \sum_{i=1}^{R} \frac{C_{i}-C_{\text {opt }}}{C_{\text {opt }}} \times 100 \%\right)$
where $C_{i}$ represents the makespan of the optimal solution obtained by an algorithm in the run $i, C_{\text {opt }}$ indicates the makespan of the optimal solution found, $R$ is the number of times the algorithm runs on a single instance and ins represents the instance label for each problem, ins $=1,2,3, \ldots, 10$.

In this paper, the estimation of distribution algorithm (EDA) [41], estimation of distribution algorithm with tabu search (EDA-TS) [42], estimation of distribution algorithm with iterated local search (EDA-iLS) [43], discrete artificial bee colony (DABC) [44], shuffled frog-leaping algorithm (SPLA) [10], and the genetic algorithm with tabu search (GA-TS) [45] are selected as the comparison algorithms. The population sizes of the comparison algorithms were uniformly set to $10 * n$, where $n$ was the number of jobs. In the EDA and its variant algorithms, the selection ratio of the population was set to 0.3 . The comparison of ARPD can be obtained according to the running results of the algorithm. The comparison results are shown in Table 6. The best
performances of the comparison algorithms in the test problems are marked as bold in the Table 6. The experimental results show that the ARPD value of the EDA-MIS algorithm is significantly better than that of the EDA, EDA-TS, EDAiLS, DABC and SFLA algorithms on most problems. It can be found that the performance of the GA-TS algorithm is better than that of the EDA-MIS algorithm in some problems of small sizes, such as $n=5,10$. However, the EDA-MIS algorithm is better than the GA-TS algorithm in the problems where the number of jobs is high, such as $n=20$ and 50 . In view of the makespan indicator, the EDA-MIS algorithm is also significantly better than the GA-TS algorithm.

In the actual production process, the number of jobs is generally very large. The weakness of the EDA-MIS algorithm in the low-level problems can be ignored. On the other hand, the TSHHFSP model with SDST in this paper is extracted from the actual production factory. In this model, the limitation of maximum stagnation iteration is added to the termination conditions. In some low-level problems, the termination condition of maximum stagnation iteration leads to the early ending of the evolution process in the EDA-MIS algorithm. Therefore, the performance of the proposed EDA-MIS algorithm in these instances is poor due to the iterations being less than that in other comparative algorithms. For example, the performances of the five algorithms are shown in Fig. 5. The number of jobs is 10. The numbers of machines in Stages 1 and 2 are 1 and 3, respectively. As Fig. 5 shows, the EDA-MIS algorithm stops evolution on the 70th iteration. While the GA-TS algorithm evolves to the iteration of 175 . When the iteration of evolution is 70 , the EDA-MIS algorithm outperforms other algorithms.

In addition, another set of experiments ware conducted for this problem. In the case where the number of jobs was 10 , the stop criteria of the GA-TS and EDA-MIS algorithms were uniformly set to a fixed iterations number of 1000 times. The performances of these two algorithms are compared in Table 7. It can be seen from the table that the EDA-MIS shows better performance than the GA-TS in the case of the same number of iterations. These results further validate the effectiveness of the proposed EDA-MIS.

The results of 51 runs of the EDA-MIS algorithm and each comparison algorithm in all test instances are statistically analyzed. The mean and the standard deviation of makespan solved by EDA-MIS and each comparison algorithm are obtained. Finally, the average values of the statistical results on 10 test instances of each problem are obtained. The results are shown in Table 8. The best performances of the comparison algorithms in the test problems are marked as bold in the Table 8.

It can be seen that the performance of the EDA-MIS algorithm is better than that of other comparison algorithms in solving large-scale problems. When the numbers of jobs are 5 and 10 , the performance of the EDA-MIS is slightly imperfect compared with the GA-TS. However, the EDA-MIS performs more effectively than the other five algorithms. As the

Table 6 Results of different algorithms in TSHHFSP problem with SDST

scale of the problem grows, the advantage of the solution performance of the proposed EDA-MIS algorithm becomes more apparent.

In the proposed EDA-MIS algorithm, the EDA algorithm is responsible for performing an exploration search on the decision space. The solution space is effectively explored by performing the operations such as selection, model updating and sampling. The reference-based neighborhood search strategy is responsible for the neighborhood search of the selected optimal reference solution. This strategy mainly performs the exploitation search. In the tabu-based neighborhood search strategy, some solutions with poor performance are liberated into the tabu list during the search process. If the neighborhood solution is included in the tabu list, the neighborhood search is abandoned to avoid an invalid search. An ablation experiment is conducted to verify the effectiveness of the two searches strategies in the proposed EDA-MIS algorithm. The results of the ablation experiment demonstrate that the combination of the two neighborhood search strategies can
![img-4.jpeg](img-4.jpeg)

Fig. 5 The convergence performance of the five comparison algorithms
lead to a performance boost. The results are shown in Table 9, where "Without RNS" and "Without TNS" represent the EDA-MIS algorithm without the reference-based and the tabu-based neighborhood search strategies, respectively. The best performances of the comparison algorithms in the test problems are marked as bold in the Table 9.

Figures 6 and 7 are the boxplots of the performance comparison between the EDA-MIS algorithm and the EDA, EDATS, EDA-iLS, DABC, SFLA and GA-TS algorithms in the TSHHFSP problems with SDST. The sizes of jobs in these problems are 20 and 50 . The experimental results show that the solving performance of the EDA-MIS algorithm in 20jobs and 50-jobs problems are better than that of the other four algorithms in terms of accuracy and stability.

The convergence plots of the compared algorithms are shown in Figs. 8 and 9 on TSHHFSP problems with SDST in which the numbers of jobs are 20 and 50 . It is observed that the convergence rate of the EDA-MIS is better than the other algorithms in these problems. In the proposed EDA-MIS algorithm, the EDA algorithm can learn the characteristic of the problems through the updating of the probability model. The performance of the EDA-MIS algorithm can be evolved further by the neighborhood search strategy. The modified EDA algorithm and the neighborhood search operations play a

Table 7 The performance of the comparison algorithms with the fixed iterations number

Table 8 The statistical results of the comparison experiment

Table 9 The results of the ablation experiment
desirable role to balance global exploration and local exploitation. The convergence rate and the convergence speed can be improved by the modified EDA algorithm and the neighborhood search operations. However, according to the no-free lunch theorem (NFL), no algorithm is better than the linear enumeration of the search space or the pure random search algorithm.

Wilcoxon rank tests are performed based on the above experimental results to further test the statistical performance of the proposed EDA-MIS algorithm. The algorithms are compared in pairs to check the significant difference between the EDA-MIS algorithm and the comparison algorithms. Tables 10, 11, 12 and 13 show the statistical results of the Wilcoxon test between EDA-MIS and the comparison algorithm at different scale problems, with the EDA-MIS algorithm as the control algorithm. In Tables 10, 11, 12 and 13, $\mathrm{R}+$ is the sum of the rank that EDA-MIS outperforms other algorithms in the current row, and $\mathrm{R}-$ is the sum of the levels that other algorithms in the current row outperform the EDA-

![img-5.jpeg](img-5.jpeg)

Fig. 6 The boxplots of different algorithms for TSHHFSP with SDST of 20 jobs

MIS. A yes means that EDA-MIS is significantly superior to other algorithms in the current row and a no means the opposite. The "yes" are marked as bold in the Tables 10, 11, 12 and 13. The table is bolded when the EDA-MIS significantly differs from the comparison algorithm and is superior to the comparison algorithm within the confidence interval. It
turns out that the proposed EDA-MIS algorithm has better results than the EDA, EDA-iLS, EDA-TS, DABC and SFLA algorithms in TSHHFSP problems with 5 and 10 jobs. The performance of the EDA-MIS is slightly worse compared to that of the GA-TS algorithm. The reasons that lead to this phenomenon are mentioned above in this paper. The stop

![img-6.jpeg](img-6.jpeg)

Fig. 7 The boxplots of different algorithms for TSHHFSP with SDST of 50 jobs

![img-7.jpeg](img-7.jpeg)

Fig. 8 The convergence plots of different algorithms for TSHHFSP with SDST of 20 jobs
![img-8.jpeg](img-8.jpeg)

Fig. 9 The convergence plots of different algorithms for TSHHFSP with SDST of 50 jobs

Table 10 The Wilcoxon's rank-sum test results for 5 jobs

Table 11 The Wilcoxon's rank-sum test results for 10 jobs

Table 12 The Wilcoxon's rank-sum test results for 20 jobs

Table 13 The Wilcoxon's rank-sum test results for 50 jobs

criterion of the maximum stagnation iterations in the actual problem is considered.

To evaluate the significance level of all algorithms, an additional Bonferroni-Dunn's procedure is applied as a post hoc procedure to calculate the critical difference for comparing their differences with $\alpha=0.05$ and $\alpha=0.1$.
$C D=q_{\alpha} \sqrt{\frac{k(k+1)}{6 N}}$
Where, the parameters $k$ and $N$ are the number of algorithms to be compared and the number of benchmarks, respectively. In the experimental evaluation, $k=5$ and $N=14$. When $\alpha=0.05, q_{\alpha}$ is 2.498 and $\alpha=0.1, q_{\alpha}$ is 2.241 from Table B. 16 (two-tailed $\alpha(2)$ ) of [46]. Figures 10, 11, 12 and 13 illustrate the results of Bonferroni-Dunn's test that considered the EDA-MIS as a control algorithm. The numerical results of the Friedman's test are shown in Tables 14, 15, 16 and 17.

When the numbers of jobs are 5 and 10 , there is no significant difference in the performance of the EDA-MIS and the GA-TS algorithms. The EDA-MIS algorithm is slightly worse than the GA-TS algorithm. However, the performance of EDAMIS on these small-scale problems has a clear advantage over the EDA, EDA-iLS, EDA-TS, DABC and SFLA algorithms in $\alpha=0.05$ and $\alpha=0.1$. In the case of larger-scale problems with 20 and 50 jobs, the proposed EDA-MIS algorithm has a significant advantage over the comparison algorithms. When the number of jobs is 20 , the performance of EDA-MIS is better than that of GA-TS. The proposed EDA-MIS algorithm has significant advantages over EDA, EDA-iLS, EDA-TS, DABC and SFLA algorithms. When the number of jobs is 50 , the proposed EDA-MIS performs better than the EDAiLS and offers significant performance advantages compared to GA-TS, EDA, EDA-TS, DABC and SFLA algorithms.

All in all, the proposed EDA-MIS is an effective and robust algorithm for solving the TSHHFSP with SDST. The superiority of the proposed algorithm owes to the following aspects.
![img-9.jpeg](img-9.jpeg)

Fig. 10 Results of Friedman's test of different algorithms for 5 jobs

![img-10.jpeg](img-10.jpeg)

Fig. 11 Results of Friedman's test of different algorithms for 10 jobs
![img-11.jpeg](img-11.jpeg)

Fig. 12 Results of Friedman's test of different algorithms for 20 jobs
![img-12.jpeg](img-12.jpeg)

Fig. 13 Results of Friedman's test of different algorithms for 50 jobs

Table 14 Ranking of Friedman's test for 5 jobs

Table 15 Ranking of Friedman's test for 10 jobs

Table 16 Ranking of Friedman's test for 20 jobs

Table 17 Ranking of Friedman's test for 50 jobs



(1) The self-learning probability model and the suitable updating mechanism are helpful to effectively explore the search space. (2) The multiple intensification mechanisms are helpful to reasonably intensify the qualities of solutions. (3) The suitable parameters setting is helpful to perform the EDA-MIS search.

## 6 Conclusion

This paper studies the actual production process of rare earth (RE) metals in the northwest region of China. The two-stage heterogeneous hybrid flow-shop scheduling problem (TSHHFSP) with sequence-dependent setup time (SDST) is constructed based on the analysis of the actual production process. The makespan criterion is selected as the optimized objective. The proposed model considers three sub-problems: the machining sequence of the jobs, the machine allocation of the jobs, and the constraints of the sequence-dependent setup time. In this paper, an EDA-MIS algorithm is proposed to solve the TSHHFSP problem with SDST. The performance of the proposed algorithm is compared with that of other algorithms in multiple test instances. The obtained results demonstrate that the performance of the proposed EDA-MIS algorithm is better than that of most of the comparison algorithms in small-scale problems. However, the advantages of the EDA-MIS algorithm are not significant compared with a few comparison algorithms. The performance of the EDA-MIS algorithm is superior in the larger-scale problems and has a significant advantage over all the comparison algorithms. A series of statistical analysis experiments are conducted to further demonstrate and validate the performance advantages of the proposed EDA-MIS algorithm compared with other comparison algorithms. In the evolution of the EDA-MIS algorithm, the characteristics of the TSHHFSP problem with SDST are learned by constructing the probability distribution model to optimize the solution. The combination of self-learning ability and neighborhood search improves the efficiency and accuracy of the EDA-MIS algorithm. The HFSP problem is a research direction with high research value and extensive application prospects. The HFSP problems with specific constraints deserve more research attention.

In future research, further consideration will be given to the manufacturing environment of multi-factory collaborative processing. Especially, the energy consumption and collaborative optimization of the production supply chain will be the focal concerns.

Acknowledgments This work was financially supported by the National Natural Science Foundation of China under grant 62063021. It was also supported by the Key talent project of Gansu Province (ZZ2021G50700016), the Key Research Programs of Science and Technology Commission Foundation of Gansu Province (21YF5WA086), Lanzhou Science Bureau project (2018-rc-98), and Project of Gansu Natural Science Foundation (21JR7RA204).
