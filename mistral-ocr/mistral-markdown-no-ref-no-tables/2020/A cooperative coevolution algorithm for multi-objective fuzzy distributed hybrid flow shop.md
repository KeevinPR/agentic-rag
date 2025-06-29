# A cooperative coevolution algorithm for multi-objective fuzzy distributed hybrid flow shop ${ }^{\ominus}$ 

Jie Zheng, Ling Wang*, Jing-jing Wang<br>Department of Automation, Tsinghua University, Beijing, 100084, China

## A R TICLE I N F O

## Article history:

Received 17 October 2019
Received in revised form 16 December 2019
Accepted 16 January 2020
Available online 20 January 2020

## Keywords:

Multi-objective fuzzy distributed hybrid flow shop
Fuzzy processing times and due dates
Robustness
Cooperative coevolution algorithm Estimation of distribution algorithm Iterated greedy search

## A B S T R A C T

With consideration of uncertainty in the distributed manufacturing systems, this paper addresses a multi-objective fuzzy distributed hybrid flow shop scheduling problem with fuzzy processing times and fuzzy due dates. To optimize the fuzzy total tardiness and robustness simultaneously, a cooperative coevolution algorithm with problem-specific strategies is proposed by reasonably combining the estimation of distribution algorithm (EDA) and the iterated greedy (IG) search. In the EDA-mode search, a problem-specific probability model is established to reduce the solution space and a sample mechanism is proposed to generate new individuals. To enhance exploitation, a specific local search is designed to improve performance of non-dominated solutions. Moreover, destruction and reconstruction methods in the IG-mode search are employed for further exploiting better solutions. To balance exploration and exploitation capabilities, a cooperation scheme for mode switching is designed based on the information entropy and the diversity of elite solutions. The effect of the key parameters on the performances of the proposed algorithm is investigated by Taguchi design of experiment method. Comparative results and statistical analysis demonstrate the effectiveness of the proposed algorithm in solving the problem.
(c) 2020 Elsevier B.V. All rights reserved.

## 1. Introduction

Under the trend of globalization, the multi-shop co-production pattern has become increasingly popular. Distributed manufacturing will conduce to share resources, enhance economic benefits and respond to market changes rapidly. In such a situation, a variety of distributed shop scheduling problems have been studied, such as the distributed flow shop scheduling [14], the distributed job shop scheduling [5] and the distributed flexible job shop scheduling [6]. Compared with the traditional single-shop problems, the distributed shop scheduling problems consider both assignment of jobs to different shops and job sequencing in each shop. Thus, it is more difficult to solve the distributed shop scheduling problems.

Nowadays, the hybrid flow shop scheduling problem (HFSP) has been widely applied in industries, such as electronic, glass, textiles, and semiconductors [7,8]. The HFSP is an extension of the classical permutation flow shop scheduling problem for the flexible manufacturing system where multiple parallel machines

[^0]are employed at each stage. To solve the HFSP effectively, a lot of meta-heuristics have been proposed, including genetic algorithm (GA) [9], artificial bee colony algorithm (ABC) [10], iterated greedy (IG) algorithm [11], and estimation of distribution algorithm (EDA) [12]. To the best of our knowledge, few research works have been carried out on the distributed hybrid flow shop scheduling problem (DHFSP). To minimize the makespan of the DHFSP with multiprocessor tasks, Ying and Lin [13] proposed a mixed integer linear programming formulation and a self-tuning IG (SIG) algorithm by using an adaptive cocktail decoding mechanism. Hao et al. [14] presented a hybrid brain storm optimization algorithm with distributed Nawaz-Enscore-Ham (NEH) method [15] to solve the DHFSP.

In real world manufacturing systems, there are various uncertain factors, including model-inherent uncertainty such as kinetic constants, process-inherent uncertainty such as processing time, external uncertainty such as product demands, and discrete uncertainty such as machine maintenance [16]. Therefore, it is significant to study the DHFSP under uncertain environment. Fuzzy set theory is a common technique to handle uncertainty and vagueness [17]. During recent years, some research has been carried out on the scheduling problems with uncertain parameters by introducing the fuzzy set theory into the framework of the algorithms. For the fuzzy flexible job shop problem (FFJSP), Palacios et al. [18] proposed a cooperative coevolution algorithm (CCA), with the consideration of different ranking methods for


[^0]:    ${ }^{\oplus}$ No author associated with this paper has disclosed any potential or pertinent conflicts which may be perceived to have impending conflict with this work. For full disclosure statements refer to https://doi.org/10.1016/j.knosys. 2020.105536.

    Corresponding author.
    E-mail address: wangling@mail.tsinghua.edu.cn (L. Wang).

fuzzy numbers and the study of their influence on the solution robustness. Wang [19] presented an estimation of distribution algorithm, modeling job processing times as fuzzy numbers and employing fuzzy number operations to calculate the scheduling objective value. And Lin [20] combined biogeography-based optimization with some heuristics to solve the same problem. In addition, Gao et al. [21] considered the uncertainty of both processing times and new job insertion, and proposed a two-stage ABC based on rescheduling with fuzzy set theory. For HFSP with fuzzy processing times, Hong et al. [22] combined fuzzy largest processing time rule with fuzzy Johnson algorithm, but it cannot obtain satisfactory and robust solutions for large-scale problems. Rezaie et al. [23] presented a mixed-integer programming model for FHFSP to maximize the satisfaction level of meeting due dates, but it is not suitable for large-scale problems due to explosive growth of computing time. Behnamian and Ghomi [24] combined GA and particle swarm optimization to minimize both makespan and the sum of the earliness and tardiness for FHFSP. Zare and Fakhrzad [25] proposed a hybrid GA with the attribute-deductive data mining method. However, the robustness of the solution is not considered in the above research.

Taking into account both robustness and economic indicator, it becomes a multi-objective problem. The methods to solve the multi-objective problems can be roughly classified into four types: weighting approach, the constraint transformation method, Pareto-based approach, and the decomposition approach. For the stochastic HFSP, Wang et al. [26] assigned different weight for each objective to transfer the multi-objective problem to a single-objective one. For the aero-assisted vehicle trajectory planning problem, Chai et al. [27] embed the priority requirements into the model and transfer the original problem to a single-objective formulation. Deb et al. [28] proposed the nondominated sorting genetic algorithm (NSGA-II), generating the Pareto front of a multi-objective problem by non-dominated sorting procedure and crowding distance metric. Chai et al. [29] applied the Pareto-based approach and proposed a game theory based adaptive differential evolution method with a control logic. Besides, Zhang et al. [30] presented a multi-objective evolutionary algorithm based on decomposition by decomposing a multi-objective optimization problem into a number of scalar sub-problems.

This paper takes first attempt to address the multi-objective FDHFSP (MFDHFSP) with fuzzy processing times and due dates. Since the MFDHFSP is a complex NP-hard multi-objective problem with uncertainty, large search space and strongly coupled sub-problems, we will propose a Pareto-based cooperative coevolution algorithm according to the characteristics of the problem. For uncertainty, we take into account the robustness of the solutions. To deal with multiple objectives, the Pareto-based approach is applied in the coevolution framework. To solve the strongly coupled sub-problems, i.e., shop allocation, job sequence and machine assignment, specific encoding and decoding methods with virtual jobs are utilized. Besides, the EDA-mode search and the IG-mode search are cooperated to balance exploration and exploitation of the algorithm. To reduce the search space, a problem-specific probability model and a suitable sampling mechanism are designed. Moreover, the local search based on critical shops is used to further enhance exploitation capability. The effect of the key parameters is investigated and the effectiveness of the proposed algorithm is demonstrated by extensive simulation comparisons.

The remainder of the paper is organized as follows. In Section 2, operations of fuzzy set and common concepts of Paretobased approach are introduced, and the MFDHFSP are described. In Section 3, the CCA is presented in details. Simulation results and statistical analysis are provided in Section 4. Finally, we end the paper with some discussions, conclusions and future work in Section 5.

## 2. The fuzzy distributed hybrid flow shop problem

### 2.1. Operations on fuzzy processing time and fuzzy due date

To deal with fuzzy processing times and due dates in the MFDHFSP, the arithmetic operations of fuzzy numbers are used, including addition, subtraction, maximum, and ranking operation. For two triangular fuzzy numbers (TFNs) $A=\left(a^{1}, a^{2}, a^{3}\right)$ and $B=\left(b^{1}, b^{2}, b^{3}\right)$, addition, subtraction and maximum operations are shown as follows [31].
$A+B=\left(a^{1}+b^{1}, a^{2}+b^{2}, a^{3}+b^{3}\right)$
$A-B=\left(a^{1}-b^{3}, a^{2}-b^{2}, a^{3}-b^{1}\right)$
$\max (A, B) \approx \max (A, B)$

$$
=\left(\max \left(a^{1}, b^{1}\right), \max \left(a^{2}, b^{2}\right), \max \left(a^{3}, b^{3}\right)\right)
$$

where $\max _{i}$ is the approximation of $\max (A, B)$ [32].
The expected value of the TFN $A$ is given as follows [33].
$E(A)=\left(a^{1}+2 a^{2}+a^{3}\right) / 4$
Besides, the following criterions are adopted to rank two TFNs [34].

Step1: The greatest number $Z_{1}(A)=E(A)$ will be chosen as the first criterion to rank two TFNs.

Step2: If there exist ties, $Z_{2}(A)=a^{2}$ is used as the second criterion.

Step3: If $Z_{1}$ and $Z_{2}$ are identical, $Z_{3}(A)=a^{3}-a^{1}$ will be chosen as the third criterion.

### 2.2. Basic concepts of multi-objective optimization

Generally, a multi-objective optimization problem can be described as follows.
$\operatorname{Minimize} y=f(x)=\left(f_{1}(x), f_{2}(x), \ldots, f_{\text {num }}(x)\right)$
where $x \in \Omega$ is the decision solution, $\Omega$ is the domain of definition, $f_{i}(x)(i=1, \ldots, n u m)$ is the value of the $i$ th objective, and $y$ is the objective vector with num objectives.

In this paper, we employ the Pareto-based approach to deal with the multiple objectives and some common concepts are as follows.

Pareto dominance: A feasible solution $a$ is said to dominate another feasible solution $b$ if and only if $f_{i}(a) \leq f_{i}(b), i=$ $1,2, \ldots, n u m$, and $\exists i \in\{1,2, \ldots, n u m\} \vdots f_{i}(a)<f_{i}(b)$.

Pareto optimality: A feasible solution $a$ is optimal if it is not dominated by any other feasible solutions.

Optimal Pareto set/Pareto Front: The solution set containing all optimal Pareto solutions is defined as the optimal Pareto set in solution space or the Pareto Front in objective space.

Non-dominated solution set/archive set (AS): The optimal Pareto set obtained by a certain algorithm is defined as a nondominated solution set/archive set (AS).

### 2.3. Description of MFDHFSP

The MFDHFSP is descripted with following notations.
$n$ : number of jobs
$s$ : number of stages in one shop
$F$ : number of shops
$i$ : index of stages, $i=1, \ldots, s$
$j$ : index of jobs, $j=1, \ldots, n$
$m_{i}$ : number of machines at $i$ th stage
$l$ : index of machines, $i=1, \ldots, m_{i}$
$M_{1, i}$ : the $i$ th machine at stage $i$
$v_{i, l}$ : machine speed of $M_{1, l}$

$O_{i, j}$ : the operator of job $j$ at stage $i$
$p_{i, j}$ : the fuzzy process time of job $j$ at stage $i, p_{i, j}=\left(p_{i, j}^{1}, p_{i, j}^{2}, p_{i, j}^{3}\right)$
$d_{j}$ : the fuzzy due date of job $j, d_{j}=\left(d_{j}^{1}, d_{j}^{2}, d_{j}^{3}\right)$
$C_{i, j}$ : the fuzzy completion time of $O_{i, j}, C_{i, j}=\left(C_{i, j}^{1}, C_{i, j}^{2}, C_{i, j}^{3}\right)$
$C_{j}$ : the fuzzy completion time of job $j, C_{j}=C_{s, j}$
$T_{j}$ : the fuzzy tardiness of job $j, T_{j}=\max \left(C_{j}-d_{j}\right.$, zero $)$
$T T$ : the fuzzy total tardiness of a solution
$E T T$ : the expected value of the fuzzy total tardiness
$\operatorname{Rob}^{D}$ : robustness indicator
The MFDHFSP comprises $n$ jobs, $F$ identical shops, and each shop contains $s$ stages. Stage $i(i=1, \ldots, s)$ contains $m_{i}$ uniform parallel machines $\left\{M_{i, 1}, M_{i, 2}, \ldots, M_{i, m}\right\}$ in each shop. The machine speeds $v_{i, i}\left(i=1, \ldots, m_{i}\right)$ satisfy $1 \leq v_{i, 1} \leq v_{i, 2} \leq \cdots \leq$ $v_{i, m i}$, VI.

Each job is assigned to one of the $F$ shops, and sequentially processed at $s$ stages, which is expressed by operations $O_{i, j}(i=$ $1, \ldots, s)$. The processing time of $O_{i, j}$ is represented as a TFN $p_{i, j}=\left(p_{i, j}^{1}, p_{i, j}^{2}, p_{i, j}^{3}\right)$, where $p_{i, j}^{1}$ is the shortest processing time, $p_{i, j}^{2}$ is the most possible processing time and $p_{i, j}^{3}$ is the longest processing time. If $O_{i, j}$ is conducted on machine $M_{i, i}$, the actual processing time becomes $p_{i, j} / v_{i, j}$. Each job has a TFN due date $d_{j}=\left(d_{j}^{1}, d_{j}^{2}, d_{j}^{3}\right)$, where $d_{j}^{1}$ is the earliest due date, $d_{j}^{2}$ is the most possible due date and $d_{j}^{3}$ is the latest due date. Similarly, the fuzzy completion time of $O_{i, j}$ is defined as a TFN $C_{i, j}=\left(C_{i, j}^{1}, C_{i, j}^{2}, C_{i, j}^{3}\right)$, and the tardiness of job $j$ equals to the TFN $T_{j}=\max \left(C_{j}-d_{j}\right.$, zero $)$, where $C_{j}$ is the fuzzy completion time of job $j, C_{j}=C_{s, j}$, and the fuzzy number zero $=(0,0,0)$.

In addition, it assumes that all jobs are independent, and their release times are 0 ; preemption is not allowed; every machine is continuously available and can only process one job at a time; every job is processed in the same sequence, and only can be processed on one machine at a time; and if a job is assigned to a shop, it cannot be reassigned to other shops afterwards. The objective functions include the minimum expected total tardiness $(E T T)$ and the maximum robustness. The ETT is defined as the expected value of the TFN total tardiness $T T=\left(T T^{1}, T T^{2}, T T^{3}\right)$. The robustness denoted as $\operatorname{Rob}^{D}$ is defined as the maximum difference between the modal value $T T^{2}$ and the bounds of the fuzzy interval $T T[33,34]$ as follows. Obviously, a smaller $\operatorname{Rob}^{D}$ implies better robustness.
$T T=\left(T T^{1}, T T^{2}, T T^{3}\right)=\sum_{j=1}^{n} T_{j}$
$E T T=\left(T T^{1}+2 T T^{2}+T T^{3}\right) / 4$
$\operatorname{Rob}^{D}=\max \left(T T^{2}-T T^{1}, T T^{3}-T T^{2}\right)$

## 3. The cooperative coevolution algorithm for the MFDHFSP

Cooperative coevolution is an effective way to improve the performance of evolutionary algorithms in solving complex optimization problems [35,36]. To solve the FJSP, Wang et al. [37] proposed a bi-population EDA by using population cooperation to adjust the machine assignment and operation sequence respectively. To solve the FFJSP, Palacios et al. [18] presented a cooperative coevolution algorithm with two sub-populations. As we known, it is important to balance global exploration and local exploitation for evolutionary algorithms. To solve the MFDHFSP effectively, we combine the probability model based EDA search and greedy strategy based IG search [38]. Besides, we also present a cooperation scheme for coevolution by reasonably fusing the EDA-mode search and the IG-mode search. Next, we will present the algorithm with encoding and decoding methods, population initialization, the EDA-mode search, the IG-mode search, the cooperation scheme and the complexity analysis.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of an encoded solution.

Table 1
Fuzzy processing times and machine speeds.
### 3.1. Encoding and decoding

In this paper, a solution is represented by $n+F-1$ permutation sequence $\Pi$, including $F-1$ virtual jobs and $n$ actual jobs. Each virtual job is used to separate actual jobs to different shops and the sequences of actual jobs denote the processing orders at the first stage in each shop. For an example with 5 jobs and 2 shops, a feasible solution encoded as 2-3-5-6-4-1 denotes that jobs $2 \rightarrow 3 \rightarrow 5$ are assigned to shop 1 and processed sequentially at the first stage while jobs $4 \rightarrow 1$ are assigned to shop 2 . The virtual job 6 separates all the actual jobs into two shops. Such an encoded solution is illustrated in Fig. 1.

In each shop, jobs are assigned to the uniform machine with the earliest finish time. Besides, List scheduling (LS) rule [12] is applied to determine the job processing sequences after the first stage. According to $L S$ rule, the jobs at stage $i(i=2, \ldots, s)$ are scheduled in an ascending order of their completion times at the previous stage.

For the above example, suppose the fuzzy processing times and speeds of all uniform parallel machines are given in Table 1. The Gantt chart of the schedule is shown in Fig. 2, where the triangles above the dotted lines are fuzzy start times of the corresponding operations, and the triangles below the dotted lines are their fuzzy completion times.

### 3.2. Population initialization

Considering both quality and diversity, a heuristic named modified NEH2 [15] (mNEH2) and a random method are used in a hybrid way to initialize the population. The procedure of the mNEH2 is as follows.

Step 1: Let initial sequence be $\Pi_{0}=\{n+1, n+2, \ldots, n+F-1\}$;
Step 2: Rank $n$ actual jobs according to their due dates in an ascending order, $J=\left(J_{(1)}, J_{(2)}, \ldots, J_{(n)}\right)$. Let $j=1$.

Step 3: Insert job $J_{(j)}$ to all possible positions in $\Pi_{0}$, and calculate the corresponding $T T$ of the partial sequence. The partial sequence with lowest $T T$ is denoted as $\Pi_{\text {new }}$. If there exist ties, then choose the one with minimum $\operatorname{Rob}^{D}$ as $\Pi_{\text {new }}$. If their $\operatorname{Rob}^{D}$ values are the same, then select the one with minimum fuzzy completion time as $\Pi_{\text {new }}$. Let $\Pi_{0}=\Pi_{\text {new }}$.

Step 4: If $j<n, j=j+1$, go to Step 3; otherwise, output $\Pi_{0}$.
By employing the mNEH2, a solution with certain quality can be generated. To ensure the diversity of initial population, other Psize -1 solutions are generated randomly, where Psize is the population size. Besides, the AS is initialized as the set of all non-dominated solutions in the initial population.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Gantt chart of the encoded solution.

### 3.3. EDA-mode search

As a population-based evolutionary algorithm, the EDA [39] is of good global exploration capability. The main concept of the EDA is statistical learning, where a probability model is established to describe the distribution of solution space. Then a new population is generated by sampling the probability model, and the model is updated by the elite individuals of the population [12]. The EDA has been successfully used to solve resource allocation and scheduling problems in recent years [40,41]. In our algorithm, the EDA is adopted to explore promising solutions.

### 3.3.1. Probability model initialization

Since the MFDHFSP has a large solution space with the scale $\mathrm{O}\left((n+F-1)!\times \prod_{i=1}^{n} m_{i}^{n}\right)$, it is important to employ knowledge -based strategy to reduce the search space. It has been proved that there must be at least one job in each shop in the optimal solution when $n>F$ [1]. By employing such a property, a problem-specific probability model and a sampling mechanism are designed, which are able to reduce the search space to $\mathrm{O}(n!\times$ $\left.C_{n-1}^{-n-F+1} \times \prod_{i=1}^{n} m_{i}^{n}\right)$.

The probability model $Q$ of the EDA is designed to consider both the shop assignment and job sequence. Each element $q_{j, p o s}(e)$ of $Q$ represents the probability of job $J_{j}(j=1,2, \ldots, n+F-1)$ assigned to position pos in the sequence in the eth updating process. To ensure that every shop has at least one job, $Q(0)=$ $\left\{q_{j, p o s}(0)\right\}$ is initialized as follows.

$$
\begin{aligned}
& q_{j, p o s}(0) \\
& \quad=\left\{\begin{array}{cc}
\frac{1}{n+F-1}, & j=1, \ldots, n ; p o s=1, \ldots, n+F-1 \\
\frac{1}{n-F+1}, & j=n+1, \ldots, n+F-1 ; p o s=2 j-2 n, \ldots, 2 j-n-F \\
0, & \text { else }
\end{array}\right.
\end{aligned}
$$

where the first $n$ rows indicate that each actual job can be assigned to every position in the sequence. The last $F-1$ rows imply that each virtual job $J_{j}(j=n+1, n+2, \ldots, n+F-1)$ can only be assigned to the position from the $(2 j-2 n)$ th ranging to the $(2 j-n-F)$ th in the sequence to ensure that every shop should have at least one job. It is obvious that the positions with probability 0 will not be sampled during the sampling process. Therefore, the probabilities of the same positions in the updated probability model will also be 0 . That is, the probabilities of these positions are always 0 during the evolution process.

For each row of $Q(0)$, the probability of every possible position is set equally to ensure that the whole solution space can be sampled uniformly. Obviously, $\forall j, \sum_{i p o s=1} q_{j, p o s}(0)=1$.

### 3.3.2. Sampling mechanism

New individuals are generated by sampling the probability model $Q(e)$. The sampling process is described as follows.
First, set $Q^{\prime}=Q(e)$ as a temporary probability matrix. Then, determine the position pos of job $J_{j}$ in the permutation sequence by sampling $Q^{\prime}$ using the roulette wheel method. The elements in the posth column and $j$ th row of $Q^{\prime}$ are set as 0 to ensure each position can only be occupied once. To guarantee that each shop has at least one job, the corresponding elements of other virtual jobs are set as 0 when a virtual job is assigned. Afterwards, normalize each row of $Q^{\prime}$. Repeat the above steps until all the jobs are assigned. Thus, a new individual is generated. The pseudo code of the sampling process is given as Algorithm 1.

### 3.3.3. Updating probability model

In general, the probability model of the EDA is updated with the elite individuals. In this paper, the non-dominated sorting method based on crowding distance is used to select the elite individuals for the multi-objective problem. For all the non-dominated solutions of current population, their crowding distances are calculated as Algorithm 2.

```
Algorithm 2: Procedure of calculating crowding distances
Input non-dominated solutions NDS
Output crowding distances
    for each solution \(X\) in NDS
        \(d(X)=0 ; / / d(\cdot)\) denotes the crowding distance;
    end
    for each objective \(m / / m=1,2\) is the index of the objectives
        NDS \(^{1}=\) sort NDS with \(n\) th objective in ascending order;
        \(/ /\) NDS \((i)\) is the \(i\) th solution in the current solution set;
        \(d(\operatorname{NDS}(1))=\operatorname{infinite} ;\)
        \(d(\operatorname{NDS}(N))=\operatorname{infinite} ; / / N\) is the size of NDS;
    for \(i=2\) to \(N-1\)
        \(d(i)=d(i)+\operatorname{NDS}(i+1) \cdot \mathrm{m}-\operatorname{NDS}(i-1) \cdot \mathrm{m}\)
        \(/ /\) NDS \((i) \cdot \mathrm{m}\) denotes the value of \(n\) th objective of NDS \((i)\).
    end
end
```

The non-dominated solutions with largest $\eta \% \times$ Psize crowding distances constitute the elite set (ES), where $\eta \%$ is the ratio of elite solutions. If the number of the non-dominated solutions is less than $\eta \% \times$ Psize, all of them constitute the ES. The elite solutions in the ES are used to update $Q(e)$ as follows.
$q_{j, p o s}(e)=(1-\alpha) q_{j, p o s}(e-1)+\frac{\alpha}{\eta \% \times \text { Psize }} \sum_{h=1}^{\eta \%+\text { Psize }} \mathrm{I}_{\mathrm{pos}}^{h}, \forall j, p o s$

```
Algorithm 1: Sampling Procedure
Input \(Q(c)\)
Output a permutation sequence \(\Pi\)
    \(Q^{\prime}:=Q(c) ; j=n+F-1\)
    while \(j>0\) do
        Sample \(Q^{\prime}\left(j_{i}:\right)\) with roulette wheel method to determine position pos of \(J_{j}\) in the permutation
sequence;
    \(\square Q^{\prime}\left(j_{i}:\right)\) is the \(j\)-th row of \(Q^{\prime}\)
    \(\Pi(\operatorname{pos})=j\);
    for \(w=1\) to \(n+F-1\)
        \(Q^{\prime}(w, \operatorname{pos})=0 ; Q^{\prime}(j, w)=0\);
    end
    \(Q^{\prime}(j, \operatorname{pos})=1\);
    if \(j=n\)
        \(w=j-1 ;\)
            while \(w>n\) do
                for \(k=\operatorname{pos}+2 w-2 j\) to \(2 w-n-F\)
                    \(Q^{\prime}(w, k)=0\);
            end
            \(w=w-1 ;\)
        end
    end
    Normalize each row of \(Q^{\prime}\);
    \(j=j-1\);
    end
```

where $\alpha \in(0,1)$ is the learning rate, and $I_{\text {j }}^{\mathrm{h}}$ is the following indicator function of $h$ th individual in the ES.
$I_{\text {j }}^{\mathrm{h}}=\left\{\begin{array}{ll}1, & \text { if } J_{j} \text { appears in position pos } \\ 0, & \text { else }\end{array}\right.$
3.3.4. Local search based on critical shops

To improve the quality of the individuals in the ES, a local search is designed based on critical shops, including the shops with maximum and minimum $T T$ denoted as Smax and Smin, respectively. Besides, the job with maximum tardiness in Smax is denoted as a critical job Jmax.

The local search performs the following three operators one by one on each individual $X_{i}$ in the ES until no non-dominated solution is generated.

- Insert_inS: insert Jmax into a random position in Smax and generate a new solution $X_{i}^{\prime}$. If $X_{i}$ is dominated by $X_{i}^{\prime}, X_{i}$ is replaced by $X_{i}^{\prime}$.
- Swap_BS: randomly select a job in Smax and another in Smin, then exchange their positions and generate a new solution $X_{i}^{\prime}$. If $X_{i}$ is dominated by $X_{i}^{\prime}, X_{i}$ is replaced by $X_{i}^{\prime}$.
- Insert_BS: insert Jmax into a random position in Smin and generate a new solution $X_{i}^{\prime}$. If $X_{i}$ is dominated by $X_{i}^{\prime}, X_{i}$ is replaced by $X_{i}^{\prime}$.

After the local search phase, the AS is updated by the newly non-dominated solutions.

### 3.4. IG-mode search

As a simple mate-heuristic, the IG algorithm [42] is of powerful exploitation capability. So far, the IG has been successfully applied to a variety of scheduling problems such as the flow shop scheduling [42], the HFSP [43], and the DHFSP [44]. In this paper, the IG is cooperated with the EDA to balance exploration and exploitation capabilities. The main procedure of the IG-mode search includes destruction and reconstruction.

The destruction phase consists of the following steps.

Step 1: Randomly select one actual job from the shops with largest $\alpha_{\text {IG }}$ total tardiness respectively, where $\alpha_{\text {IG }}$ is the number of removed jobs in the destruction phase. If $\alpha_{\text {IG }}>F$, randomly select the rest $\alpha_{\text {IG }}-F$ jobs from the remaining actual jobs.

Step 2: All the selected jobs are removed from the current permutation $\Pi$, and constitute the new sequence $\Pi_{S}$. The partial sequence of the remaining jobs (including virtual jobs) is denoted as $\Pi_{R}$.

The reconstruction phase is performed as follows.
Step 1: Let $j=1$. Reinsert the $j$ th job of $\Pi_{S}$ into the best position of $\Pi_{R}$, and obtain the new partial sequence $\Pi_{R}^{*}$, where the best position is determined by non-dominated sorting.

Step 2: $\Pi_{R}=\Pi_{R}^{*}$. If $j<\alpha_{\text {IG }}, j=j+1$, go to Step 1. Otherwise, output $\Pi_{R}$.

In the IG-mode search, the destruction and reconstruction methods are performed on each individual $X_{i}$ in the AS. If the newly generated solution $X_{i}^{\prime}$ is not dominated by $X_{i}$, the AS will be updated by $X_{i}^{\prime}$.

### 3.5. Cooperation scheme

To balance the EDA-based exploration and the IG-based exploitation, the cooperation scheme is designed based on the information entropy and the diversity of elite individuals in the AS.

### 3.5.1. Convergence evaluation of the EDA-mode search

Information entropy is used to measure the uncertainty of stochastic variables [44]. In this paper, we employ information entropy to evaluate the disorder degree of the probability model and the convergence of the EDA-mode search.

The information entropy of a random variable $X$ is calculated as follows.
$H(X)=\sum_{i}-p\left(x_{i}\right) \log _{b}\left(p\left(x_{i}\right)\right)$
where $x_{i}$ is the $i$ th possible value of $X, p\left(x_{i}\right)$ is the probability of $x_{i}$, and $b=2$ is the base of the logarithm.

For independent variables $X_{i}(i=1, \ldots, n)$, their joint information entropy is calculated as follows.
$H\left(X_{1}, X_{2}, \ldots, X_{n}\right)=-\sum_{i} \sum_{j}-p\left(x_{i j}\right) \log _{b}\left(p\left(x_{i j}\right)\right)$
where $x_{i j}$ is the $j$ th value of $X_{i}$ and $p\left(x_{i j}\right)$ is the probability of $x_{i j}$.
In the EDA-mode search, each element of the probability model $Q(e)$ can be viewed as a random variable. Accordingly, the information entropy of $Q(e)$ is expressed as Eq. (14).
$H(\mathrm{Q}(e))=-\sum_{j=1}^{n+F-1} \sum_{p \in \mathrm{~s}=1}^{n+F-1} q_{j, p \in \mathrm{~s}}(e) \log 2\left(q_{j, p \in \mathrm{~s}}(e)\right)$
Thus, the information entropy of $Q(0)$ can be derived as follows, denoted as $H_{0}$.

$$
\begin{aligned}
H_{0}= & -\sum_{j=1}^{n} \sum_{p \in \mathrm{~s}=1}^{n+F-1} \frac{1}{n+F-1} \log 2\left(\frac{1}{n+F-1}\right) \\
& -\sum_{j=n+1}^{n+F-1} \sum_{p \in \mathrm{~s}=2 j-2 n}^{2 n-n+F} \frac{1}{n-F+1} \log 2\left(\frac{1}{n-F+1}\right) \\
= & n \log _{2}(n+F-1)+(F-1) \log 2(n-F+1)
\end{aligned}
$$

Since $H(Q(e))$ can measure the uncertainty of $Q(e), H(Q(e))$ will be close to a certain number when $Q(e)$ converges. Therefore, if the information entropy of two adjacent generations varies slightly, the probability model is basically unchanged which can be regarded as the convergence of the EDA-mode search to some extent. So, we design a terminal condition 1 (TC1) according to the change of information entropy as follows. If TC1 holds, the algorithm will switch to IG-mode search.
$\frac{\left|H_{i}-H_{i-1}\right|}{H_{0}} \leq 0.01$ and $H_{i}<H_{i-1}$
where $H_{i}$ is the information entropy of $Q(e)$ in the $i$ th iteration of the EDA-mode search.

### 3.5.2. Diversity evaluation of the IG-mode search

In the IG-mode search, the diversity of the individuals in the AS can be evaluated by the number of solutions in the AS as well as the number of newly generated non-dominated solutions. So, we design a terminal condition 2 (TC2) for the IG-mode search as follows. If the number of solutions in the AS is less than $\eta \% \times$ Psize or there is no new non-dominated solution generated by the IGmode search, then the algorithm will switch to the EDA-mode search. Once the mode is switched, $Q(e)$ will be updated by the elite solutions in the AS, i.e., the best $\eta \% \times$ Psize solutions.

With the above switch scheme, the algorithm can adaptively choose to perform the EDA-mode search or the IG-mode search. Thus, it can avoid the slow convergence of the pure EDA-mode search and the premature convergence (loss of diversity) of the pure IG-mode search. Therefore, the global exploration and local exploitation can be well balanced. The mechanism of the cooperative coevolution algorithm is illustrated in Fig. 3 and the procedure of the CCA is shown in Algorithm 3.

### 3.6. Complexity analysis

Suppose that there are $n$ jobs, $s$ stages and $F$ shops in the MFDHFSP. The computation complexity of computing $T T$ is $O(n s)$. In the initial phase, the computational complexity of the mNEH2 and random method are $O\left(n \log n+n s \times n^{2}\right)$ and $O(n s \times n \times($ Psize 1)) respectively. Therefore, the computation complexity of the initial phase is approximately equal to $O\left(n^{3} s+n^{2} s \times\right.$ Psize $)$.

In each iteration of the loop in the EDA-mode search, it needs to sample model, select elite solutions, local search, update model
![img-2.jpeg](img-2.jpeg)

## Cooperative coevolution

Fig. 3. The mechanism of the CCA.
and calculate information entropy. According to Algorithm 1, the computation complexity of sampling is $O($ Psize $\times n s \times\left(n \times(n+\right.$ $\left.F-1)+(F-1)^{2} \times(n-F))\right) \approx O\left(\right.$ Psize $\times\left(n^{3} s+n_{2} s F^{3}-s n F^{3}\right)$ ). Selecting Elite solutions consists of 3 steps: find non-dominated solutions, calculate the crowding distance and select the first $\eta \% \times$ Psize solutions with computation complexity $O\left(\right.$ Psize $\left.^{2}\right), O(E n \times$ $\log E n+E n)$ and $O(E n \times \log \left(\eta \% \times\right.$ Psize $)$, respectively, where En $<$ Psize is the number of non-dominated solutions. Besides, the computation complexities of updating model and calculating information entropy can be derived as $O\left(\eta \% \times\right.$ Psize $\times(n+F-1)+$ $\left.(n+F-1)^{2}\right)$ and $O\left((n+F-1)^{2}\right)$ respectively. As for local search, the computation complexity of one iteration is $O($ Psize $\times n s)$. Therefore, the computation complexity of the EDA-mode search in one iteration is as follows, where $l s$ is the run times of the local search.

$$
\begin{aligned}
& O(n, s, F, \text { Psize, } \eta, \text { En, } l s) \approx O\left(\text { Psize } \times\left(n^{3} s+n^{2} s F^{2}-s n F^{3}\right)\right) \\
& \quad+O\left(\text { Psize }^{2}\right)+O(E n \times \log E n+E n) \\
& \quad+O(E n \times \log (\eta \% \times \text { Psize }))+O(\eta \% \times \text { Psize } \times(n+F-1) \\
& \quad+(n+F-1)^{2})+O\left((n+F-1)^{2}\right)+O(l s) \times O(\text { Psize } \times n s) \\
& \quad \approx O\left(\text { Psize } \times n s\left(n^{2}+n F^{2}-F^{3}+l s\right)+\text { Psize }^{2}\right)
\end{aligned}
$$

In each iteration of the loop in the IG-mode search, the algorithm needs to perform destruction and construction. The computation complexity of sorting and job removing in destruction are $O\left(n \log \left(\alpha_{I G}\right)\right)$ and $O(n s)$. The computation complexity of construction for one solution is $O\left(n s \times \sum_{i=1}^{\alpha_{I G}}\left(n-\alpha_{I G}+i\right)^{2}\right)$. Because $\alpha_{I G} \leq$ $n$, the computation complexity can be simplified as $O\left(\alpha_{I G} \times n^{3} s\right)$. Therefore, the computation complexity of the IG-mode search in one iteration is $O\left(b \times \alpha_{I G} \times n^{3} s\right)$, where $b$ is the size of the AS.

In summary, the computation complexity of the CCA with $k_{1}$ iterations of EDA-mode search and $k_{2}$ iterations of IG-mode search is shown as follows.

$$
\begin{aligned}
& O\left(k_{1}, k_{2}, \alpha_{I G}, n, F, s, l s\right)=O\left(n^{3} s+n^{2} s \times\right. \text { Psize } \left.)\right. \\
& \quad+O\left(k_{1}\right) O\left(\text { Psize } \times n s\left(n^{2}+n F^{2}-F^{3}+n s \times l s\right)+\text { Psize }^{2}\right) \\
& \quad+O\left(k_{2}\right) O\left(b \times \alpha_{I G} \times n^{3} s\right)
\end{aligned}
$$

## 4. Experimental results and comparisons

In this section, extensive numerical tests are conducted to evaluate the performances of the proposed algorithm. The testing instances are generated by extending the instances from [13] for the DHFSP. To be specific, the speeds of machines at each stage are set as a random number uniformly distributed in $[1,1.5]$ denoted as $v_{i, 1} \sim U(1,1.5)$, satisfying $1 \leq v_{i, 1} \leq v_{i, 2} \leq \cdots \leq v_{i, n o}, \forall i$.

```
Algorithm 3: Procedure of the CCA
Input A MFDHFSP instance
Output the archive set (AS)
    Initialize the population by mNEH2 and random method;
    Initialize the probability model \(Q(0)\);
    Calculate the initial entropy \(H_{0}\);
    Find non-dominated solutions of the population and update AS; Let \(e=0\);
    while terminal condition is not satisfied do
    \(i=1\);
    while TC1 is not satisfied do // the EDA-mode search
        Generate Psize individuals by sampling \(Q(e)\);
        Find non-dominated solutions of the new generated individuals;
        Calculate the crowding distance and select elite solutions to form the ES;
        for each individual in the ES
            Perform local search based on critical shops;
        end
        \(e=\alpha+1\);
        Update \(Q(e)\) by the ES and update the AS;
        Calculate information entropy \(H_{i}\) of \(Q(e)\);
        \(i=i+1\);
    end
    while TC2 is not satisfied do // the IG-mode search
        for each individual in the \(A S\)
            Perform destruction and reconstruction;
        end
        Update the AS;
    end
    \(e=\alpha+1 ;\) Update \(Q(e)\) by elite solutions in the AS
    end
    return AS
```

The processing times of jobs are described as symmetric TFNs according to literature [32]. That is, $p_{i, j}=\left(p_{i, j}^{1}, p_{i, j}^{2}, p_{i, j}^{3}\right), p_{i, j}^{2}=$ $p_{i, j}^{1}+p, p_{i, j}^{3}=p_{i, j}^{1}+2 p$, where $p \sim U(1,5)$ is a random number and $p_{i, j}^{1}$ is the original deterministic processing time. Besides, the due dates are set as $d_{j}=\left\{\left(1+\lambda \times \mu\right) \times \sum_{i} p_{i j}\right\}$, where $\mu \sim U(0,1)$, and $\lambda \in\{0.5,2,4\}$ is the tardiness factor, representing the tight, middle and loose cases respectively [45]. The algorithm is coded in $\mathrm{C}++$ and run on a PC with Intel(R) Core(TM) i7-8700 CPU @ 3.2 GHz .

For the MFDHFSP, the performances of the solution algorithms should be evaluated in terms of the quantity, quality and distribution of the obtained archive set. In this paper, three widely used metrics [46] are employed.

ONVG: the metric overall non-dominated vector generation (ONVG) is defined as the number of distinct non-dominated solutions in set $A$, denoted as $|A|$. Intuitively, it reflects the quantity of the non-dominated solution set. A larger ONVG means there are more choices for the decision maker.

CM: the C metric (CM) is used to reflect the dominance relationship between two non-dominated sets $A_{1}$ and $A_{2}$ by comparing the quality of the solutions in the two sets.
$C\left(A_{1}, A_{2}\right)=\frac{\left|\left(x_{2} \in A_{2}\right) \exists x_{1} \in A_{1}, x_{2} \prec x_{1}\right.}{\left|A_{1}\right|}$
where $C\left(A_{1}, A_{2}\right)$ denotes the percentage of the solutions in $A_{2}$ that are dominated by or the same as the solution in $A_{1}$. The closer $C\left(A_{1}, A_{2}\right)$ is to 1 , the more approximate $A_{1}$ is to the optimal Pareto set.

TS: the TS calculated is used to measure how evenly the solutions are distributed.
$T S=\sqrt{\frac{1}{|A|} \sum_{i}^{|\A|} \frac{\left(D_{i}-\bar{D}\right)^{2}}{\bar{D}}}$
where $\bar{D}=\sum_{i=1}^{|\A|} D_{i} /|A|$, and $D_{i}$ is the Euclid distance in objective space between the solution $i$ and its nearest neighbor solution. The smaller the TS is, the more uniformly the solutions are distributed.

### 4.1. Parameters setting

The CCA contains four key parameters: the population size Psize, the learning rate of $\mathrm{Q}(e)$, i.e. $\alpha$, the radio of elite solutions $\eta \%$, and the number of selected jobs in IG-mode search, i.e. $\alpha_{\mathrm{IG}}$. To investigate the effect of these parameters on the performance of the algorithm, we implement the Taguchi method of design of experiment [47] by using a moderate scale instance n50_s5_F3_1 $(n=50, s=5, F=3, \lambda=0.5)$.

Four levels of each parameter are set as shown in Table 2. According to the number of parameters and levels, an orthogonal table $L_{10}\left(4^{4}\right)$ is generated. Thus, there are 16 combinations of parameter values in total. For each combination, we run the CCA 10 times independently on n50_s5_F3_1 and set $0.3 \times n \times s$ seconds as the termination condition. Then it obtains a composite non-dominated solution set for each combination. Furthermore, the final non-dominated solution set is obtained by aggregating the 16 composite sets of all combinations. Subsequently, the proportion of the non-dominated solution set obtained by a composite set of a combination is calculated as the response value (RV). Obviously, the larger the RV, the better the combination of parameter values. The orthogonal table and response values are listed in Table 3. The significant rank of each parameter is listed in Table 4. And the trend of each factor level is shown in Fig. 4.

From Table 4, it can be seen that Psize is the most significant parameter. If Psize is too small, the solution space cannot be sampled sufficiently. However, the algorithm will converge slowly if Psize is too large. Besides, $\alpha_{\text {IG }}$ ranks the second. A proper value of $\alpha_{\text {IG }}$ ensures sufficient local search in the IG-mode search. The learning rate $\alpha$ ranks the third. A large value of $\alpha$ could lead to premature convergence while a small value of $\alpha$ could

![img-3.jpeg](img-3.jpeg)

Fig. 4. Factor level trend of the CCA.

Table 2
Combinations of parameter values.

Table 3
Orthogonal array and RV values.

Table 4
Response value and rank of each parameter.

lead to slow convergence. As for $\eta \%$, although it has the slightest influence, an appropriate value can help the algorithm update the probability model reasonably. According to above analysis, the parameters of the CCA are suggested as Psize $=40, \alpha_{1 C}=$ $2, \alpha=0.5$, and $\eta=0.3$, which will be used in the following experiments.

### 4.2. Simulation comparisons

In this section, we consider the problems with $n$ jobs, $s$ stages, and $F$ shops, where $n \in\{20,50,100\}, s \in\{2,5,8\}$ and $F \in\{2$, $3,4,5,6\}$. For each combination of $n, s$, and $F, 10$ instances are generated, resulting $3 \times 3 \times 5 \times 10=450$ instances. Moreover, we set 3 levels of due dates for every instance. Thus, 1350 instances in total will be tested.

To the best of our knowledge, there is no published work addressing the MFDHFSP. Therefore, we generalize EDA [2] for DFSP, SIG [13] for DHFSP and NSGA-II [28] [48] to solve the MFDHFSP. To compare the CCA and the above three algorithms, we run each algorithm 5 times independently for each instance with $0.3 \times n \times s$ seconds CPU time as terminal condition. The results are listed in Tables 5-7 grouped by different tardiness factor $\lambda$, where C, E, S, N represent the CCA, EDA, SIG, NSGA-II respectively. Moreover, the nonparametric tests (Kruskal-Wallis tests) [49] with $95 \%$ confidence interval are carried out for each pair of $C M$. If $p$-value is smaller than 0.05 , it implies the difference between the compared $C M$ is significant.

From Tables 5-7, it can be seen that the CCA is better than other three algorithms in terms of $C M$ on most groups of instances. As $n$ increases, the superiority of the CCA becomes more obvious. For the groups with same $n$, the differences between $\mathrm{C}(\mathrm{C}, \mathrm{E})$ and $\mathrm{C}(\mathrm{E}, \mathrm{C})$ as well as $\mathrm{C}(\mathrm{C}, \mathrm{N})$ and $\mathrm{C}(\mathrm{N}, \mathrm{C})$ are larger with smaller value of $F$. So, it can be concluded that the CCA performs significantly better than the other three algorithms, especially on the instances with large $n$ and small $F$. In addition, the $p$-values show the superiority of the CCA when $\lambda=0.5$. However, when $\lambda=2$ or 4 the $p$-values on some instances are larger than 0.05 or "-", where "-" means the objective values obtained by the two tested algorithms are the same. It implies that these instances can be solved relatively easily at loose due dates.

For ONVG and TS metrics, the comparative results are given in Table 8. It can be seen that ONVG of the EDA is better than that of SIG especially when $\lambda=0.5$ while the results are opposite on instances with large value of $F$ when $\lambda=2$ or 4 . The main reason is that the EDA has a better ability of exploration than the SIG. However, most solutions generated by the EDA can be dominated with loose due dates when $\lambda=2$ or 4 . Since the CCA combines the advantages of the EDA-mode search and the IG-mode search, the results of the CCA is the best on all groups of instances, which means it can find more non-dominated solutions. As for TS, from

Table 5
Results of the $\mathrm{CM}(\lambda=0.5)$.

Table 6
Results of the $\mathrm{CM}(\lambda=2)$.

Table 7
Results of the $\mathrm{CM}(\lambda=4)$.

Table 8 it can be seen that the results of the CCA are better than both EDA and NSGA-II on most instances and better than SIG on average. That is, the non-dominated solutions obtained by the CCA are of better distribution.

In addition, the Pareto fronts obtained by the four algorithms when solving the instance n100_s8_F3_1 $(n=100, s=8, F=$ $3, \lambda=0.5$ ) are illustrated in Fig. 5. Clearly, the Pareto front obtained by the CCA is the best in terms of quantity, quality and distribution.

## 5. Discussions and conclusions

In this paper, we address the multi-objective fuzzy distributed hybrid flow shop problem with the minimization of the total tardiness and the maximization of the robustness. A coevolution algorithm composed of EDA and IG with a reasonable cooperation scheme is proposed to solve this problem. From extensive numerical tests, it can be seen that the convergence of our algorithm is significantly better than other algorithms on the instances with tight due dates. If the due dates are relatively loose, the diversity

Table 8
Results of the algorithms of ONVG and TS.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Pareto fronts obtained by the four algorithms.
and distribution of the solutions obtained by our algorithm are obviously better. So, our algorithm is able to obtain feasible solutions with good quality, quantity and distribution for the above case. The superiority of our algorithm mainly owes to the follows.
(1) Cooperation of the EDA-mode search and the IG-mode search to balance exploration and exploitation of the algorithm.
(2) Utilization of the specific encoding and decoding methods with virtual jobs to deal with the strong coupling of shop allocation, job sequence and machine assignment.
(3) Hybridization of the heuristic and random method to produce a population with good quality and diversity.
(4) Utilization of the problem-specific probability model and sampling mechanism to effectively reduce the search space.
(5) Utilization of local search based on critical shops to enhance exploitation capability.

The above problem-specific designs make our algorithm suitable for such a complex scheduling problem. Since our algorithm is a population-based coevolution algorithm, some random operators are used to maintain the diversity of the population. Potential strategy to remove the negative effect of the randomness would enhance the practicability. Meanwhile, it will benefit from parameter variations. So, in our future work we will study adaptive strategies for parameter control and operator utilization.

Especially, we will focus on the knowledge fusion optimization algorithms by studying knowledge utilization and learning mechanism to further enhance the performance. In addition, it is interesting to solve the distributed scheduling problems with other types of uncertainties, and it is also important to generalize the problems with more objectives including other robustness criteria.

## CReIiT authorship contribution statement

Jie Zheng: Conceptualization, Data curation, Formal analysis, Methodology, Writing - original draft, Writing - review \& editing. Ling Wang: Conceptualization, Data curation, Formal analysis, Methodology, Writing - original draft, Writing - review \& editing. Jing-jing Wang: Conceptualization, Data curation, Formal analysis, Methodology, Writing - original draft, Writing - review \& editing.

## Acknowledgments

This research is supported by the National Science Fund for Distinguished Young Scholars of China [No. 61525304], the National Natural Science Foundation of China [No. 61873328], and Meituan-Dianping Group.
