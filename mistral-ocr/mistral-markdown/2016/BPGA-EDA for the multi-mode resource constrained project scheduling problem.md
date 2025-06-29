# BPGA-EDA for the Multi-Mode Resource Constrained Project Scheduling Problem 

Mayowa Ayodele, John McCall, Olivier Regnier-Coudert<br>Robert Gordon University<br>Aberdeen, Scotland<br>Email: \{m.m.ayodele,j.mccall,o.regnier-coudert\}@rgu.ac.uk


#### Abstract

The Multi-mode Resource Constrained Project Scheduling Problem (MRCPSP) has been of research interest for over two decades. The problem is composed of two interacting sub problems: mode assignment and activity scheduling. These problems cannot be solved in isolation because of the interaction that exists between them. Many evolutionary algorithms have been applied to this problem most commonly the Genetic Algorithm (GA). It has been common practice to improve the performance of the GA with some local search techniques. The Bi-population Genetic Algorithm (BPGA) is one of the most competitive GAs for solving the MRCPSP. In this paper, we improve the BPGA by hybridising it with an Estimation of Distribution Algorithm that focuses on improving how modes are generated. We also suggest improvement to the existing experimental methodology.


## I. INTRODUCTION

The Multi-Mode Resource Constrained Project Scheduling Problem (MRCPSP) is a generalisation of the well-known Resource Constrained Project Scheduling Problem (RCPSP). The RCPSP entails assigning start and finish times to activities that make up a project such that precedence and resource constraints are respected. The most common objective of this problem is to reduce the total project duration (makespan) [1]. Other objectives based on tardiness or earliness have also been considered in previous research [2]. The RCPSP captures real-world situations originating from different industries such as planning, maintenance, management and manufacturing [3]. However the RCPSP does not adequately capture the interaction between man-hours required for a job and the resources used [4]. This additional factor is considered in the formulation of the MRCPSP.

MRCPSP is considered to be more complex than the standard RCPSP. This is because, in addition to determining the order in which activities are executed (i.e activity scheduling), decision needs to be made as to how each activity will be executed (i.e mode assignment). The activity scheduling and mode assignment aspects of the MRCPSP are interrelated and cannot be solved in isolation.

Activity scheduling entails assigning priorities to activities that make up a project such that precedence constraints are respected (i.e each activity must be performed before its successor(s)). Mode assignment entails assigning a mode of execution to each activity of a project while respecting resource limits. A mode of execution is a vector of resources (renewable and non-renewable) and the corresponding duration required to completely perform an activity. Renewable resources are replenished per period of time while non-renewable resources are limited for the entire project. The modes of execution of an activity have varying resource and time requirements. A solution to the MRCPSP is an allocation of modes, start and finish times to all the activities of a project such that precedence and resource constraints are respected. This is with the overall aim of minimising makespan of the project.

Several meta-heuristics such as Scatter Search, Simulated Annealing, Particle Swarm Optimisation, Ant Colony Optimisation, Genetic Algorithms (GA) and Estimation of Distribution Algorithms (EDA) have been applied to this problem. A review of applications of meta-heuristics to the MRCPSP is presented in [5] and we will be making a lot of reference to this literature. The GA has been a frequent choice amongst researchers applying metaheuristics to MRCPSP [6], [7], [8], [9], [10], [11]. Although Scatter Search reports better solutions than other meta-heuristics on many problem sets, the best performing GAs [6], [8] are however better on larger problems $[5]$.

Performances of algorithms particularly the GAs differ much from each other. This can be attributed to some implementation choices, one such choice is the use of local search procedures, which has been reported to significantly improve the performance of GAs [5]. GAs that use more local search procedures perform better than the ones that use few or none [5]. We seek to understand the effect of configuration choices on algorithm performance. We particularly investigate the mode improvement local search method presented in [8] which performs two major tasks: feasibility and makespan improvement.

Generally, local search methods have been applied to the mode assignment sub-problem questioning the suitability of the GA for this aspect of the MRCPSP. The crossover operator of the GA is limited in its ability to learn the interrelations between problem parameters [12]. We aim to improve the GA by applying EDA to the mode assignment aspect of the problem.

The rest of the paper is structured as follows. In Section 2, we present a background to our study. Here, we formulate the problem, present a brief review of GA configuration choices and motivation for a hybrid approach. In Section 3, we present our proposed solution approach. Section 4 presents the experimental configurations and parameter settings while results and analysis are described in Section 5. Section 6 presents our conclusions and suggests directions for future research.

## II. BACKGROUND

## A. Problem Formulation

The MRCPSP can be formerly defined as follows: A project consists of a set of $n$ activities. Every activity $i$ is labeled from $1, \ldots, n$. Activity $i, i \in[2, n]$ has a set of predecessors $\operatorname{Pred}_{i}$ which suggests that activity $i$ cannot be performed until every predecessor $h, h \in \operatorname{Pred}_{i}$ has been completed. Activity $i$ must be performed in a mode $k \in\left[1, m_{i}\right]$, where $m_{i}$ is the number of possible modes of $i$. Given that there are $A$ renewable resources, each renewable resource $r$, $r \in[1,|A|]$ is available per period of time. The maximum per period availability of $r$ is denoted by $\alpha \max _{r}$. Apart from renewable resources, there are also $B$ non-renewable resources that cannot be renewed but available for the entire project duration. The overall availability of the non-renewable resource $l, l \in[1,|B|]$ is denoted by $\beta \max _{l}$. Each mode of execution $k$ of an activity $i$ is composed of an integer vector of renewable resources $\left(\alpha_{i, k, 1}, \ldots, \alpha_{i, k,|A|}\right)$, an integer vector of non-renewable resources $\left(\beta_{i, k, 1}, \ldots, \beta_{i, k,|B|}\right)$ and the associated duration/execution time $t_{i, k}$.

The aim of the MRCPSP is to select exactly one mode of execution for each activity subject to resource and precedence constraints. This is such that makespan is minimised. We formulate the MRCPSP as follow.

Minimise $f t_{\alpha}$ subject to:

$$
\forall i \in[1, n], s t_{i} \geq f t_{h} \forall h \in \operatorname{Pred}_{i}
$$

Let $C_{p}$ be the set of activities being executed during time period $[\mathrm{p}-1, \mathrm{p}]$, then

$$
\begin{aligned}
\sum_{i \in C_{p}} \alpha_{i, k_{i}, r} & \leq \alpha \max _{r} \forall r, r \in[1,|A|], \forall p \\
\sum_{i=1}^{n} \beta_{i, k_{i}, l} & \leq \beta \max _{l} \forall l, l \in[1,|B|]
\end{aligned}
$$

We denote the start and finish times of activity $i$ by $s t_{i}$ and $f t_{i}$ respectively. The precedence constraint is presented in (1) while the renewable and non-renewable resource constraints are respectively presented in (2) and (3). In (2) and (3), $k_{i}$ is the allocated mode of $i$ and can only be one of the predefined modes of $i$. Also, $\alpha_{i, k_{i}, r}$ and $\beta_{i, k_{i}, l}$ are respectively the amount of renewable resource $r$ and non-renewable resource $l$ required by activity $i$ performed in mode $k_{i}$.

## B. Algorithm Configuration for Leading GAs

Genetic algorithms are amongst the most competitive algorithms for solving the MRCPSP. Results in [5] show that GAs are better on common large problem sets. The Bi-Population Genetic Algorithm (BPGA) [8] performs better than other GAs [5]. Hence, we consider it state of the art. In this section, we describe the conventional configuration choices in the most competitive GAs at solving the MRCPSP. This is with particular attention to local search methods.

The preprocessing technique of Sprecher et al. [13] is commonly executed before applying GAs to the MRCPSP. This technique which is not only limited to GA applications is formerly defined in [13]. It reduces the search space of feasible
solutions by eliminating non-executable modes, redundant resources and inefficient modes. The preprocessing technique has been used in [6], [8], [7] amongst others.

Furthermore, the use of local search procedures has also been very common when solving the MRCPSP with metaheuristics. Four main local search procedures are commonly used: improvement of initial population, makespan improvement, feasibility improvement and forward-backward procedures, these are described in [5]. These local search methods have mainly been applied to mode solutions. Their effects range from improving feasibility to improving makepsan of a solution by refining its mode selection.

The generation of initial population of solutions is often done with a quality improvement procedure: improvement of initial population local search. This improves the feasibility of a mode solution by changing the mode selections of randomly selected activities until feasibility is attained or a number of iterations have been reached [8], [6] .

The Schedule Generation Scheme (SGS) is the principal procedure for most heuristic solution to a project scheduling problem [14]. This is a step-wise procedure that builds a schedule from a schedule representation by activity incrementation (serial) or time incrementation (parallel) [14]. The parallel SGS is however less common because it is sometimes unable to reach optimal [15]. The SGS has been extended to the MRCPSP and is the conventional approach for generating schedules. Furthermore, some extensions of the SGS have been proposed which mainly combine SGS with local search.

In this paper, we investigate the extended SGS [8] which combines SGS with a mode improvement local search. The mode improvement procedure is a combination of makespan improvement and feasibility improvement and is described as follows. For an activity $i$, another mode $m_{i}{ }^{\prime}$ is selected. The Excess Resource Requirement $E R R$ of the new mode solution $x^{\prime}$ is evaluated by summing the additional non-renewable resource requirements of $x^{\prime} . E R R\left(x^{\prime}\right)$ is compared with that of the original mode solution $x$. If $E R R(x)$ is not better than $E R R\left(x^{\prime}\right)$, the procedure further checks for improvement in the finish time of that activity. If an improvement is achieved in the finish time of activity $i$, mode solution $x$ is set to $x^{\prime}$. Otherwise, mode solution $x$ is retained. The pseudocode for the mode improvement procedure is presented in [8]. This procedure is reported to significantly improve the SGS.

Another extension of the SGS is the forward-backward SGS proposed in [6] which combines the forward-backward local search and the SGS. The forward-backward SGS seeks to improve mode selection during scheduling and iteratively transforms left justified schedules (jobs are scheduled as early as possible) into right justified schedules (jobs are scheduled as late as possible) and vice versa until no further improvement can be made in the makespan. The concept of scheduling jobs forward and backward has also been used in [8]. They proposed the BPGA which is a GA with two populations, one is a population of left justified schedules while the other is a population of right justified schedules. The GAs presented in [6] and [8] are considered the most competitive GA applications for the MRCPSP [5].

In this paper, we focus on the mode improvement local search of the BPGA.

## C. Motivation for Hybridising GA with EDA

To the best of our knowledge, there are only two applications of EDAs [16], [17] to the MRCPSP.

EDAs, different from GAs have further relied on local search methods to improve activity solutions. One is the MultiMode Version Permutation-Based Local Search Strategy (MPBLS) in [16]. MPBLS swaps two activities in a list alongside their corresponding modes subject to precedence constraints. Another activity based local search is the random walk local search in [17]. An improvement was made to the algorithm in [16] by introducing random walk local search for the purpose of better exploring the space of activity solutions [17]. Both implementations use the Population-Based Incremental Learning (PBIL) based on two separate probabilistic models. One is used for generating activity lists while the other is used for generating mode lists.

These applications of EDA are however not as competitive as the GAs. These applications have identified the need to explore the search space of activity solutions better which is not the case with the GA. We therefore consider the GA more suitable for generating activity solutions. Furthermore, given that the GA relies on local search to improve the way modes are generated, we attribute this to its limitation in learning the structure of a problem. The EDA is designed to tackle this kind of problem by sampling a probabilistic model of promising solutions [12]. It is able to preserve structure and learn mode selections that contribute to more promising solutions. We therefore consider it more suitable for generating mode solutions. This motivates the hybridisation of BPGA with an EDA.

## III. SOLUTION APPROACH

In this section, we present the BPGA-EDA which is an extension of the BPGA approach in [8]. The BPGA-EDA is the BPGA assisted by an EDA for the generation of mode solutions. We use a PBIL style which refines those presented in [17] and [16]. BPGA-EDA is configured as follows.

## A. Representation

The BPGA-EDA uses the random key representation for activity solutions as presented in the BPGA [8]. Each RK value serves as a priority value for the activity defined by that index. Activity with a lower priority value is considered before that with a higher value. The mode assignment is represented as a string of integers and the value at each index defines the mode in which the activity defined by that index will be performed. The string lengths correspond to the number of activities in the project.

## B. Initial Population

The BPGA-EDA generates its initial population of mode and activity solutions at random. The improvement of initial population local search is afterward applied to mode solutions in the same way as the BPGA [8].

## C. Fitness Computation

This is a measure of the quality of a solution. As much as makespan is a good discriminatory factor, it cannot be directly used as the fitness function because resource infeasible solutions will eliminate good solutions in the search. We use the fitness function proposed in [7] which is the one that has been used for the BPGA. The fitness function is as follows:

The fitness of a feasible solution is equal to its makespan. However, the makespan of infeasible solutions are penalised. The maximum makespan amongst the feasible solutions in a population is denoted by max_mak_feas_pop. Also, the minimal critical path obtained by selecting modes with the least duration and assuming there is no resource restriction is denoted by $\min \_C P$. The difference between max_mak_feas_pop and $\min \_C P$ as well as $E R R(x)$ are added to the makespan of an infeasible solution.

## D. Probabilistic Model

To create a mode solution, we sample a probability matrix. The probability matrix is defined as follows.

$$
M_{p}=\left(\begin{array}{ccc}
p_{t 1} & \cdots & p_{t m} \\
\vdots & \ddots & \vdots \\
p_{n 1} & \cdots & p_{n m}
\end{array}\right)
$$

Each probability value $p_{i k}$ in this $n$ by $m$ probability matrix is the probability that activity $i$ will be performed in mode $k$. Modes of an activity that are impossible or have been eliminated during the preprocessing stage will have probability scores equal to 0 . This is because they will not have occurred in the initial population as we execute the preprocessing procedure before the initial population is generated.

The scatter search procedure in [18] which is one of the most competitive meta-heuristic for solving the MRCPSP [5] used Sum of Durations $S U D$ to select modes for the first population. This is a measure of mode solutions only and has been reported to have a strong correlation with fitness [18]. It is calculated as follows.

$$
S U D=\sum_{i=1}^{n} t_{i, k}
$$

The execution time $t_{i, k}$ for each activity in its allocated mode is summed up to obtain the $S U D$ value. This approach improved the quality of their initial solutions and we initialise our EDA in a similar way.

To create the initial probability matrix, each solution in the initial population is evaluated using the $S U D$. This means that in our fitness function (for the first population), the makespan is replaced with the $S U D$ value and infeasible solutions are penalised in the same way as the makespan. We rank all mode solutions in the population from best (lowest fitness value) to least (highest fitness value). The top (best) $b$ solutions are

selected from the population using truncation selection. The probability score is calculated as follows. For an activity $i$, we divide the number of occurrences of each possible mode of execution by $b$. e.g if the truncation size is ten and amongst the best ten solutions, activity 2 was executed in mode 1 : six times, mode 2 : four times and no occurrence of mode 3. The probability values $p_{21}, p_{22}$ and $p_{23}$ will be $0.6,0.4$ and 0 respectively.

Initialisation based on $S U D$ is an improvement on previous approaches [17], [16] that initialise their model using equal probabilities. The disadvantage of the previous approach is the possibility of sampling impossible modes, to tackle this problem an additional step of setting impossible modes to 0 is performed. We however do not require this additional step.

Subsequently, the mode solutions are paired with activity solutions to form complete solutions. This is done in order of solution generation. These solutions are then ranked according to their fitness (based on makespan). Probability scores are recalculated for each mode of every activity. Since we use a PBIL, we update the model using a learning rate $l r$ as shown in (7).

$$
p_{i k}(g)=\left(l r * p_{i k}(g)\right)+((1-l r) * p_{i k}(g-1))
$$

In (7), $p_{i k}(g)$ and $p_{i k}(g-1)$ are $p_{i k}$ values at generations $g$ and $g-1$ respectively. The probabilistic model is updated at the end each generation until the stopping criteria is met. This is because it is more computationally efficient than updating after the creation of each solution.

## E. BPGA-EDA Workflow

The BPGA approach involves the use of two separate populations $P O P_{L}$ and $P O P_{R} . P O P_{L}$ is a population of left justified schedules while $P O P_{R}$ is a population of right justified schedules. In a left-justified schedule, activities are scheduled using the SGS (activities are scheduled as early as possible) while in a right-justified schedule, activities are scheduled using the backward SGS (activities are scheduled as late as possible).

In the BPGA, each individual $i$ in $P O P_{L}$ or $P O P_{R}$ goes through crossover and serves as the first parent (parent1), the second parent (parent2) is selected by tournament selection of size two. Two offspring are generated via crossover. The activity and mode solutions of the offspring go through mutation at specified rates. The best of the two offspring from $P O P_{L}$ replaces individual $i$ in $P O P_{R}$ and vice versa. The best solutions in $P O P_{L}$ or $P O P_{R}$ are however not replaced except the new offspring is better. The overall best solution is returned at the end of each generation. The algorithm is stopped once optimal or maximum number of schedule is reached.

In the BPGA-EDA, parameter: $e d a r \in[0,1]$ is introduced to determine the rate at which EDA will be applied for generating mode solutions. We use the following notation BPGA-EDA ${ }_{e d a r}$ to express the type of BPGA-EDA used. BPGA-EDA ${ }_{0}$ is equivalent to the BPGA (i.e when $e d a r=0$, EDA is not used), but BPGA-EDA ${ }_{1}$ indicates that all mode solutions are generated by the EDA.

In the algorithm, we build two models $M_{p 1}$ and $M_{p 2}$ based on $P O P_{R}$ and $P O P_{L}$ respectively. We use the same crossover approach for RKs presented in the BPGA to generate activity solutions from parent1 and parent2. We generate mode solution for $P O P_{R}$ and $P O P_{L}$ by sampling $M_{p 1}$ and $M_{p 2}$ respectively.

The BPGA-EDA is formerly defined as follows.

1: execute preprocessing procedure
2: generate initial population $P O P_{L}$
3: compute fitness for each individual in $P O P_{L}$
4: repeat
5: if $e d a r>0$ then
6: select best $b<\left|P O P_{L}\right|$ solutions to form $S$.
7: build probabilistic model $M_{p}$ from mode assignments of solutions in $S$
8: initialise probabilistic models $M_{p 1}$ and $M_{p 2}$ with $M_{p}$
9: end if
10: for $i=1$ to $\left|P O P_{L}\right|$ do
11: set individual $i$ in $P O P_{L}$ as parent1
12: generate parent2 by tournament selection on $P O P_{L}$
13: if $r a n d<e d a r$ then
14: perform crossover to generate two offspring activity solutions
15: sample $M_{p 1}$ to produce two offspring mode solutions
16: generate two offspring solutions by combining each pair of offspring activity and mode solutions else
17: perform crossover to generate two offspring solutions
end if
18: perform mode mutation
19: perform activity mutation
20: apply backward SGS to the two offspring update $P O P_{R}$ with the best offspring end for
for $i=1$ to $\left|P O P_{R}\right|$ do
21: set individual $i$ in $P O P_{R}$ as parent1
22: generate parent2 by tournament selection on $P O P_{R}$
23: if $r a n d<e d a r$ then
24: perform crossover to generate two offspring activity solutions
25: sample $M_{p 2}$ to produce two offspring mode solutions
26: generate two offspring solutions by combining each pair of offspring activity and mode solutions else
27: perform crossover to generate two offspring solutions
end if
28: perform mode mutation
29: perform activity mutation
30: apply SGS to the two offspring
31: update $P O P_{L}$ with the best offspring end for
32: if $e d a r>0$ then
33: update $M_{p 1}$ using $P O P_{R}$
34: update $M_{p 2}$ using $P O P_{L}$
end if
35: until stopping criteria satisfied

45: return overall best solution
Note that rand is a random number between 0 and 1.

## IV. EXPERIMENTS

One of the principal factors in assessing the performance of an algorithm is the measure of performance. Although the meta-heuristics applied to the MRCPSP are non-deterministic, previous literature do not give information about variance. In this paper, we investigate variance as part of the measure of performance. We also describe the choice of problem set, a proposed sampling method and the measure of complexity used for parameterising BPGA-EDA.

## A. Benchmark Problems

There are many benchmark problems in previous research such as Boctor [19], PSPLIB [20] and the recently designed MMLIB [5] problem sets. In this paper, we use the J10, J20 and J30 problem sets from the well-known PSPLIB available at http://www.om-dh.wi.tum.de/psplib/. We chose these three as they are the most common in literature, hence useful for comparison. However, not all instances of these problem sets have at least one feasible solution, we therefore exclude them in our computation as conventionally done. After eliminating such problems, the J10, J20 and J30 have 536, 554 and 552 instances respectively.

## B. Stopping Criterion and Performance Measure

When applying an algorithm to these problem sets, previous researchers have used the number of schedules as the stopping criterion. This is often set to 5000 number of schedules. The maximum CPU time is another criterion that has been used in the past. For ease of comparison, we use the maximum number of schedules as this is most commonly used. We note that a schedule refers to a single time (start and finish) assignment for each activity of a project. However, some local search methods like the makespan improvement [6], [8] may require more than one time assignment for an activity. To cater for this, Lova et al. [6] calculate the number of schedules by dividing the number of times the activities of a project have been assigned a start time by the total number of activities. This implies that each change in the start time of an activity contributes to a fraction of a schedule. For instance, if each activity of a project have been assigned a feasible start time twice, the number of schedule will be equal to 2 . This method of calculating number of schedules have also used in [8], [5]. We use the same calculation in this paper.

The most common performance measure using number of schedules as stopping criteria is the average percentage deviation from optimal (Ave\%.Dev.Optimal). Where there are no optimal values, the critical path based lower bound (CPBLB) is used instead of the optimal. The CPBLB is estimated using the critical path based on the modes with the least durations. The $A v e \% . D e v . O p t i m a l$ is calculated as follows

$$
\text { Ave\%.Dev.Optimal }=\frac{\sum_{i=1}^{n}((|\text { bestFit-optimal }| / \text { optimal }|)+100)}{n}
$$

In eq. (8), bestFit is the fitness of the best solution generated by the algorithm.

In this paper, we average the $A v e \% . D e v . O p t i m a l$ over ten runs.

## C. Generation of Sample Set

We have identified the non-deterministic nature of the BPGA. For instance, ten runs of our implementation of the BPGA on J10 produced Ave\%.Dev.Optimal values ranging from 0.018 to 0.096 as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Results for J10 - Ave\%.Dev.Optimal

The reported $A v e \% . D e v . O p t i m a l$ value for the BPGA on J10 is 0.01 . Our results are consistent with the reported BPGA performance being the best over several runs. In order to make the most meaningful comparisons amongst algorithms, in this paper we will report average performance with variance alongside best performance over several runs.

Considering the nature of the algorithm and the number of instances in the problem sets, the computational cost of experiments grow very quickly. To be able to make comparisons based on several runs and also control the computational cost, we make use of samples from the problem sets. To ensure that the samples are representative of the problem sets, we sort them by complexity and sample uniformly across the distribution. This leads us to the choice of the measure of complexity. A description of the proposed measure of complexity and sample generation technique is as follows.

Relative Resource Availability: The measures of complexity that exists in literature include the order strength, resource factor and resource strength. The order strength which is the number of precedence relationship in the problem is not only constant across each problem set but measures only the complexity of the activity scheduling aspect of the problem. Also, the resource factor and resource strength are not specific to mode generation. Since our focus is on the generation of highly fit mode assignments, we proposed a measure that relates to the ease of generating mode feasible solutions. Also, this approach takes the preprocessing technique into consideration as we only calculate the complexity after executing the preprocessing technique. Modes or constraints that are eliminated during preprocessing are therefore not taken into consideration. This means that instances with redundant non-renewable resources will have a complexity score of 0 . To generate the RRA score, we used the following formula.

$$
R R A=\operatorname{Max}\left(\frac{\sum_{i=1}^{n} \frac{\sum_{j=1}^{m} \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot

TABLE II. BPGA-EDA Parameters using SGS- trunCation SIzE(\% OF POPULATION SIZE)/LEARNING RATES

| Problem Sets | BPGA-EDA $_{0.5}$ | BPGA-EDA $_{1}$ |
| :-- | :--: | :--: |
| J10 | 10/1.0 | 10/1.0 |
| J20 | 20/0.8 | 20/0.4 |
| J30 | 20/0.5 | 30/0.5 |

## V. RESULTS AND ANALYSIS

In this section, we present the results from comparing the BPGA-EDA ${ }_{0.5}$ and BPGA-EDA ${ }_{1}$ with our implementation of the BPGA. We have shown that there are variations in multiple runs of the BPGA but results for only one run is reported in literature. For this reason, we use our implementation of the BPGA so that we can compare based on average and standard deviations over several runs. Also, for a fairer assessment, we have used the same algorithm with just an additional parameter $e d a r$ to determine how much of EDA is used for mode generation. This means that we are comparing based on same conditions and implementation.

TABLE III. Results BASED ON SGS - AVERAGE Ave\%..Dev. Optimal (STANDARD DEVIATION) OF TEN RUNS

| Problem sets | BPGA | BPGA-EDA $_{0.5}$ | BPGA-EDA $_{1}$ |
| :-- | :--: | :--: | :--: |
| J10 | 0.61 (0.08) | $\mathbf{0 . 1 9 ( 0 . 0 5 )}$ | $\mathbf{0 . 2 0 ( 0 . 0 4 )}$ |
| J20 | 2.34 (0.05) | $\mathbf{1 . 2 1 ( 0 . 0 6 )}$ | $\mathbf{1 . 6 0 ( 0 . 0 7 )}$ |
| J30 | 17.89 (0.18) | $\mathbf{1 4 . 6 7 ( 0 . 0 6 )}$ | $\mathbf{1 5 . 0 6 ( 0 . 0 7 )}$ |

TABLE IV. ReXults BASED ON EXTENDED SGS - AVERAGE Ave\%..Dev. Optimal (STANDARD DEVIATION) OF TEN RUNS

| Problem sets | BPGA | BPGA-EDA $_{0.5}$ | BPGA-EDA $_{1}$ |
| :-- | :--: | :--: | :--: |
| J10 | 0.05 (0.02) | $\mathbf{0 . 0 3 ( 0 . 0 2 )}$ | $\mathbf{0 . 0 3 ( 0 . 0 2 )}$ |
| J20 | 0.88 (0.04) | $\mathbf{0 . 5 3 ( 0 . 0 4 )}$ | $\mathbf{0 . 6 9 ( 0 . 0 4 )}$ |
| J30 | 14.41 (0.05) | $\mathbf{1 3 . 6 8 ( 0 . 0 3 )}$ | $\mathbf{1 3 . 0 7 ( 0 . 0 7 )}$ |

In Tables III and IV, we present for each problem set, the average of $A v e \%$. Dev. Optimal and the standard deviation (in brackets) over ten runs. These results are based on our implementation of the BPGA, BPGA-EDA ${ }_{0.5}$ and BPGAEDA $_{1}$ on the J10, J20 and J30. We compare the BPGA-EDA ${ }_{0.5}$ and BPGA-EDA ${ }_{1}$ with the BPGA. Results that are statistically better than the BPGA are displayed in bold. In this paper, we use the student t-test and a 0.05 level of significance.

- Comparison Based on the SGS: Table III shows results using the SGS for schedule generation. The BPGAEDA $_{0.5}$ and BPGA-EDA ${ }_{1}$ have significantly lower Ave\%..Dev. Optimal than the BPGA on all the problem sets: J10, J20 and J30. We observe a significant improvement in the use of EDA for mode generation
- Comparison Based on the Extended SGS: Table IV shows results that are based on the extended SGS. The BPGA-EDA ${ }_{0.5}$ and BPGA-EDA ${ }_{1}$ produce statistically lower Ave\%..Dev. Optimal than the BPGA on J10, J20 and J30. Again, a significant improvement is achieved by using EDA for mode generation.
- Impact of Extended SGS: SGS extended by the local search method (mode improvement) not only improves the results produced by the BPGA but also improves the results of the BPGA-EDA ${ }_{0.5}$ and BPGA-EDA ${ }_{1}$. Inasmuch as there is a clear advantage of hybridising

EDA with BPGA (BPGA-EDA), the mode improvement local search method cannot be eliminated by applying the BPGA-EDA without compromising the quality of results produced. The results in Tables III and IV therefore also show that the BPGA-EDA ${ }_{0.5}$ and BPGA-EDA ${ }_{1}$ without mode improvement are worse than the BPGA with mode improvement.

- BPGA-EDA ${ }_{0.5}$ and BPGA-EDA ${ }_{1.0}$ : comparing the two versions of BPGA-EDA: BPGA-EDA ${ }_{0.5}$ and BPGA-EDA ${ }_{1.0}$, the former produces significantly better Ave\%..Dev. Optimal than the later on the J20 and J30 but not significantly better on the J10. This is true when the SGS or the extended SGS is used. In general, we observed that the BPGA-EDA ${ }_{0.5}$ performs better than the BPGA-EDA ${ }_{1.0}$. This is based on the results shown in Tables III and IV and can be attributed to the exploration ability of the GA and the exploitation ability of EDA. This is consistent with advantages of GA-EDA hybridisation noted by other researchers [21], [22].

For the purpose of comparison with existing published values, Table V shows the BPGA-EDA's best of ten runs as well as the published value of the BPGA.

TABLE V. RESULTS BASED ON EXTENDED SGS - AVERAGE \% DEVIATION FROM OPTIMUM - BEST OF TEN RUNS

| Problem sets | BPGA | BPGA-EDA $_{0.5}$ | BPGA-EDA $_{1}$ |
| :-- | :--: | :--: | :--: |
| J10 | 0.01 | 0.01 | 0.00 |
| J20 | 0.57 | 0.46 | 0.62 |
| J30 | 13.75 | 13.73 | 13.61 |

The results in Table V are similar and it is not clear which approach is better than which. We assert that results averaged over several runs provide a fairer assessment of the algorithms.

## VI. CONCLUSION AND FURTHER WORK

In this paper, we propose a hybrid algorithm: BPGA-EDA, which is a Bi-population Genetic Algorithm assisted by an EDA for the generation of mode solutions. Experiments comparing the BPGA-EDA with BPGA show that hybridisation with EDA produces significant performance improvements. We are able to conclude that EDAs are better suited for generating mode solutions and GAs are well suited for generating activity solutions.

Furthermore, we show that the mode improvement local search not only improves the BPGA but also the BPGA-EDA. We have not been able to eliminate the mode improvement local search of the BPGA by using the EDA for mode generation without compromising the quality of results produced. We however note that the BPGA-EDA based on SGS may be more competitive on larger problem sets because we observed more comparable results on the larger problem set: J30. We also note that parameters of BPGA have been retained in BPGA-EDA for ease of comparison and parameter tuning. They may not be the best set of parameters for the BPGA-EDA.

Although each problem set has instances with similar characteristics, we have demonstrated that results averaged over many runs rather than one are required to fully capture the variance in the performance of an algorithm. We recommend the use of this approach.

Finally, the fact that different algorithms may be suitable for different aspects of multi-component optimisation problems (i.e. problems that can be divided into smaller optimisation problems) makes them suitable for hybrid approaches. We recommend this area for future research.

## REFERENCES

[1] M. B. Wall, "A genetic algorithm for resource-constrained scheduling," Ph.D. dissertation, Massachusetts Institute of Technology, 1996.
[2] S. Hartmann and D. Briskorn, "A survey of variants and extensions of the resource-constrained project scheduling problem," European Journal of Operational Research, vol. 207, no. 1, pp. 1-14, 2010.
[3] K. S. Hindi, H. Yang, and K. Fleszar, "An evolutionary algorithm for resource-constrained project scheduling," Evolutionary Computation, IEEE Transactions on, vol. 6, no. 5, pp. 512-518, 2002.
[4] A. Drexl, R. Nissen, J. H. Patterson, and F. Salewski, "Progen/ $\pi \mathrm{x}$-an instance generator for resource-constrained project scheduling problems with partially renewable resources and further extensions," European Journal of Operational Research, vol. 125, no. 1, pp. 59-72, 2000.
[5] V. Van Peteghem and M. Vanhoucke, "An experimental investigation of metaheuristics for the multi-mode resource-constrained project scheduling problem on new dataset instances," European Journal of Operational Research, vol. 235, no. 1, pp. 62-72, 2014.
[6] A. Lova, P. Tormos, M. Cervantes, and F. Barber, "An efficient hybrid genetic algorithm for scheduling projects with resource constraints and multiple execution modes," International Journal of Production Economics, vol. 117, no. 2, pp. 302-316, 2009.
[7] J. Alcaraz, C. Maroto, and R. Ruiz, "Solving the multi-mode resourceconstrained project scheduling problem with genetic algorithms," Journal of the Operational Research Society, vol. 54, no. 6, pp. 614-626, 2003.
[8] V. V. Peteghem and M. Vanhoucke, "A genetic algorithm for the preemptive and non-preemptive multi-mode resource-constrained project scheduling problem," European Journal of Operational Research, vol. 201, no. 2, pp. 409-418, 2010.
[9] M. Mori and C. C. Tseng, "A genetic algorithm for multi-mode resource constrained project scheduling problem," European Journal of Operational Research, vol. 100, no. 1, pp. 134-141, 1997.
[10] S. Hartmann, "Project scheduling with multiple modes: a genetic algorithm," Annals of Operations Research, vol. 102, no. 1-4, pp. 111135, 2001.
[11] J. P. Reddy, S. Kumanan, and O. K. Chetty, "Application of petri nets and a genetic algorithm to multi-mode multi-resource constrained project scheduling," The International Journal of Advanced Manufacturing Technology, vol. 17, no. 4, pp. 305-314, 2001.
[12] P. Larrañaga and J. A. Lozano, Estimation of distribution algorithms: A new tool for evolutionary computation. Springer, 2002, vol. 2.
[13] A. Sprecher, S. Hartmann, and A. Drexl, "An exact algorithm for project scheduling with multiple modes," Operations-ResearchSpektrum, vol. 19, no. 3, pp. 195-203, 1997.
[14] R. Kolisch and S. Hartmann, Heuristic algorithms for the resourceconstrained project scheduling problem: Classification and computational analysis. Springer, 1999.
[15] R. Kolisch, "Serial and parallel resource-constrained project scheduling methods revisited: Theory and computation," European Journal of Operational Research, vol. 90, no. 2, pp. 320-333, 1996.
[16] L. Wang and C. Fang, "An effective estimation of distribution algorithm for the multi-mode resource-constrained project scheduling problem," Computers \& Operations Research, vol. 39, no. 2, pp. 449-460, 2012.
[17] O. S. Soliman and E. A. Elgendi, "A hybrid estimation of distribution algorithm with random walk local search for multi-mode resource-constrained project scheduling problems," arXiv preprint arXiv:1402.5645, 2014.
[18] V. Van Peteghem and M. Vanhoucke, "Using resource scarceness characteristics to solve the multi-mode resource-constrained project scheduling problem," Journal of Heuristics, vol. 17, no. 6, pp. 705728, 2011.
[19] F. F. Boctor, "Heuristics for scheduling projects with resource restrictions and several resource-duration modes," The international journal of production research, vol. 31, no. 11, pp. 2547-2558, 1993.
[20] R. Kolisch and A. Sprecher, "Psplib-a project scheduling problem library: Or software-orsep operations research software exchange program," European Journal of Operational Research, vol. 96, no. 1, pp. 205-216, 1997.
[21] J. Pena, V. Robles, P. Larrañaga, V. Herves, F. Rosales, and M. S. Pérez, "Ga-eda: Hybrid evolutionary algorithm using genetic and estimation of distribution algorithms," in Innovations in Applied Artificial Intelligence. Springer, 2004, pp. 361-371.
[22] Q. Zhang, J. Sun, E. Tsang, and J. Ford, "Hybrid estimation of distribution algorithm for global optimization," Engineering computations, vol. 21, no. 1, pp. 91-107, 2004.
[23] E. Theodorsson-Norheim, "Friedman and quade tests: Basic computer program to perform nonparametric two-way analysis of variance and multiple comparisons on ranks of several related samples," Computers in biology and medicine, vol. 17, no. 2, pp. 85-99, 1987.