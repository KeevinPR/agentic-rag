# An effective estimation of distribution algorithm for the multi-mode resource-constrained project scheduling problem 

Ling Wang*, Chen Fang<br>Tsinghua National Laboratory for Information Science and Technology (TNList), Department of Automation, Tsinghua University, Beijing 100084, China

## A R T I C L E I N F O

Available online 8 May 2011
Keywords:
Multi-mode resource-constrained project scheduling
Estimation of distribution algorithm
Probability model
Permutation based local search

## A B S T R A C T

In this paper, an estimation of distribution algorithm (EDA) is proposed to solve the multi-mode resource-constrained project scheduling problem (MRCPSP). In the EDA, the individuals are encoded based on the activity-mode list (AML) and decoded by the multi-mode serial schedule generation scheme (MSSGS), and a novel probability model and an updating mechanism are proposed for well sampling the promising searching region. To further improve the searching quality, a multi-mode forward backward iteration (MFBI) and a multi-mode permutation based local search method (MPBLS) are proposed and incorporated into the EDA based search framework to enhance the exploitation ability. Based on the design-of-experiment (DOE) test, suitable parameter combinations are determined and some guidelines are provided to set the parameters. Simulation results based on a set of benchmarks and comparisons with some existing algorithms demonstrate the effectiveness of the proposed EDA.
(c) 2011 Elsevier Ltd. All rights reserved.

## 1. Introduction

The multi-mode resource-constrained project scheduling problem (MRCPSP) is an extension of the resource-constrained project scheduling problem (RCPSP), which is concerned with scheduling the project activities over time and resources. Generally, the MRCPSP is much more close to the reality. In a multimode resource-constrained project, each activity has several execution modes, each of which has a related duration and nonrenewable/renewable resource requirements. The MRCPSP is more complex than the RCPSP. Kolisch and Drexl [1] have proven that even finding a feasible solution of the MRCPSP with more than one nonrenewable resource is NP-complete. Until now, only the MRCPSP with no more than 20 activities could be solved optimally using exact algorithms with acceptable computational time [2]. In practice, the MRCPSP usually should be solved in limited time. As a result, heuristics for the MRCPSP have gained increasing attention during the past decades.

Kolisch and Drexl [1] proposed a three phase local search approach: construction phase to generate the initial solution, local search phase to perform a neighborhood search on the set of feasible mode assignment, and intensification phase to generate a schedule with a near-optimal heuristic based on the mode assignment given by the local search phase. Hartmann [3]

[^0]developed a genetic algorithm (GA) to solve the MRCPSP, in which single-pass and multi-pass local search component were adopted as local search to improve the schedules. Hartmann also defined a unique similarity measure to analyze the similarity of the whole population, with which it concluded that the GA with inheritance mechanism deteriorated the quality of the solution in a long-term evolution. Józefowska et al. [4] proposed a simulated annealing (SA) algorithm to solve the MRCPSP, in which two versions of SA were discussed: SA without penalty function and SA with penalty function. Bouleimen and Lecocq [5] also proposed a simulated annealing algorithm for the MRCPSP, in which an approach was introduced to use two embedded search loops alternating activity and mode neighborhood exploration to improve the search. Alcaraz et al. [6] also proposed a GA to solve the MRCPSP. Different from the GA in [3], sophisticated designed solution representation and fitness function were incorporated to improve the performance. Zhang and Tam [7] proposed a particle swarm optimization (PSO) based approach, in which a procedure checking and adjusting infeasible particle-represented solutions was adopted to transform infeasible solutions into feasible ones. Jarboui et al. [8] proposed a combinatorial PSO approach, in which a unique representation and a local search procedure were adopted. Van Peteghem and Vanhoucke [9] proposed an artificial immune system (AIS) to solve the MRCPSP. For the initial population, the mode assignment procedure was translated to multi-choice multi-dimensional knapsack problem and the activity list was generated with priority rules. Wauters et al. [10] proposed a multi-agent learning approach, in which an agent


[^0]:    * Corresponding author. Tel.: +86 10 62783125; fax: +86 10 62786911.

    E-mail address: wangling@mail.tsinghua.edu.cn (L. Wang).

represented an activity node and for each node the related agent decided how to choose the mode of the activity and how to visit its successors. Damak et al. [11] proposed a differential evolution (DE) approach to solve the MRCPSP, and the effect of population size on the solution quality was analyzed. Elloumi and Fortemps [12] proposed a hybrid rank-based evolutionary algorithm that transformed the MRCPSP to a bi-objective problem with the objectives of makespan and nonrenewable resource consumption. As a result, the nonrenewable resource constraints were relaxed and the evolutionary operators were simplified. Ranjbar et al. [13] proposed a hybrid scatter search to solve the discrete time/ resource trade-off problem and the MRCPSP. Tseng and Chen [14] proposed a two-phase genetic local search algorithm that contained two phases: the first phase aimed at searching globally for promising areas while the second phase aimed at searching in the promising areas more thoroughly. Lova et al. [15] proposed an efficient hybrid GA to solve the MRCPSP, in which a unique mode assignment procedure was developed and a new fitness function was proposed to improve the results. Van Peteghem and Vanhoucke [16] proposed a bi-population GA to solve preemptive and non-preemptive MRCPSP that made use of two separate populations and extended the serial schedule generation scheme by introducing a mode improvement procedure.

Estimation of distribution algorithm (EDA) is a kind of stochastic optimization algorithm based on statistical learning [17]. Unlike GA explicitly applies crossover and mutation operator to generate new individuals, EDA generates new individuals by predicting the most promising area based on the distribution of elite individuals of former generations in the search space. Refer [17] for more details about EDA. So far, EDA has been developed to solve a variety of optimization problems in academic and engineering fields, such as feature selection [18], flow-shop scheduling [19], nurse rostering [20], quadratic assignment problem [21], multi-speed planetary transmission design [22], inexact graph matching [23], and software testing [24]. In this paper, we propose an EDA for solving the MRCPSP with the criterion to minimize makespan. In particular, the activity-mode list (AML) is adopted as the encoding scheme, and a novel probability model and updating mechanism are developed to help identify the most promising area, and a multi-mode forward backward iteration (MPBI) and a multi-mode permutation based local search method (MPBLS) are applied to the best individuals to exploit the neighborhood of the best individuals. We investigate the parameter setting of the proposed EDA based on DOE tests and carry out simulation test based on a set of benchmarks. Computational results and comparisons demonstrate the effectiveness of the EDA.

The remainder of the paper is organized as follows: In Section 2, the MRCPSP is described. In Section 3, the basic EDA is introduced. Then, the EDA for the MRCPSP is proposed in Section 4. Computational results and comparisons are provided in Section 5. Finally we end the paper with some conclusions in Section 6.

## 2. Multi-mode resource-constrained project scheduling problem

The MRCPSP is to study how to allocate renewable/nonrenewable resource and schedule activities to minimize the whole project makespan. Generally, the MRCPSP can be stated as follows. A project is composed of $j$ activities, and each activity has $M$ execution modes. The set of renewable resource is referred as $K^{\rho}$, and the per-period-availability is assumed to be constant $R_{k}^{\rho}$. The set of nonrenewable resource is referred as $K^{v}$, the total amount of availability is $R_{k}^{\prime}$. Precedence relationship for each activity $j=1,2, \ldots, j$ is defined by sets of its immediate predecessors $P_{j}$, which indicate that the activity $j$ cannot be executed
before any of its predecessors $i \in P_{j}$ is not completed yet. If activity $j=1,2, \ldots, j$ is executed in mode $m \in\left(1, \ldots, M_{j}\right)$, the duration is $d_{j m}$. In this duration, $r_{j m k}$ units of renewable resource $k \in K^{\rho}$ is consumed in each period of the non-preemptable duration, and $n_{j m k}$ units of nonrenewable $k \in K^{v}$ is consumed totally. The dummy activities $j=0$ and $j=j+1$ represent the start and end of the project, respectively. The dummy activities do not request any resource and have zero duration. The set of all activities can be denoted as $J^{+}=(0, \ldots, J+1)$. The objective is to minimize the makespan of the project. The MRCPSP can be formulated as follows:
$\operatorname{Minimize} \sum_{t=\overline{E f}_{j+1}}^{L f_{j+1}} t x_{j+1,1, t}$
subject to
$\sum_{m=1}^{M_{j}} \sum_{t=\overline{E f}_{j}}^{L f_{j}} x_{j m t}=1, \quad j \in J^{+}$
$\sum_{m=1}^{M_{j}} \sum_{t=\overline{E f}_{j}}^{L f_{j}} t x_{i m t} \leq \sum_{m=1}^{M_{j}} \sum_{t=\overline{E f}_{j}}^{L f_{j}}\left(t-d_{j}\right) x_{j m t}, j \in J^{+} ; i \in P_{j}$
$\sum_{j=1}^{l} \sum_{m=1}^{M_{j}} r_{j m k} \sum_{b=\max (t, E f j)}^{\min (t+q_{j m}-1, L f j)} x_{j m b} \leq R_{k}^{\rho}, \quad k \in K^{\rho}$
$\sum_{j=1}^{l} \sum_{m=1}^{M_{j}} n_{j m k} \sum_{t=\overline{E f}_{j}}^{L f_{j}} x_{j m t} \leq R_{k}^{\rho}, \quad k \in K^{v}$
$x_{j m t}= \begin{cases}1, & \text { if activity } j \text { is performed in mode } m \text { and finished at time } t \\ 0, & \text { otherwise }\end{cases}, j \in J^{+}$
where Eq. (1) defines the objective to minimize the makespan; Eq. (2) guarantees that each activity is executed exactly once; Eq. (3) confirms the precedence relationship to be satisfied; Eqs. (4) and (5) represent the renewable and nonrenewable resource restriction, respectively.

Fig. 1 illustrates a simple example with 11 activities (including two dummy activities $j=0$ and $j=J+1$ ), where each activity has two modes. In this example, one kind of renewable resource and one kind of nonrenewable resource are considered, and the available amounts of available renewable and nonrenewable resource are 2 and 28 , respectively. The resource requirements and corresponding durations for the two modes are listed in Table 1.

In Fig. 2, a schedule of this project is shown. The mode of each activity $j=1,2, \ldots, j$ is $2,1,2,1,2,2,2,2,1$, respectively. Since both precedence constraint and the amounts of nonrenewable resource consumed are 25 (less than 28), it is a feasible schedule with makespan 18 .
![img-0.jpeg](img-0.jpeg)

Fig. 1. An example of the MRCPSP.

## Estimation of distribution algorithm

Estimation of distribution algorithm (EDA) can be regarded as a general framework of statistical learning based optimization algorithms. With the tool of statistical analysis, the EDA tries to predict of the movement of population in the search space and estimates the underlying probability distribution of encoded variables of the elite individuals. After generating the initial population and initializing the probability matrix, an iterative procedure is carried out to estimate the distribution of the optimal solutions until the stopping condition is met. The general framework of the EDA is illustrated in Fig. 3.

The core of the EDA procedure is to estimate the probability distribution. Due to the difference of problem types, different probability models can be designed to estimate the underlying probability distribution. In the next section, we will propose a special probability model and an updating mechanism based on the searching mechanism of the EDA for solving the MRCPSP.

## 4. The EDA for MRCPSP

In this section, we first introduce the encoding scheme, probability model, probability generating mechanism, local search strategy, and updating mechanism. Then, we present the framework of the proposed EDA.

### 4.1. Preprocessing

Before starting the EDA, we utilize the reduction procedure developed by Sprecher et al. [25] to reduce the search space. This procedure could exclude the inefficient/non-executable mode as well as redundant resources. For integrity, we briefly introduce the definitions as follows:

Inefficient mode: A mode $m^{\prime}$ is called inefficient if there exists another mode $m$ with $d_{j m} \leq d_{j m^{\prime}}$ and $r_{j m k} \leq r_{j m^{\prime} k}$ for each renewable resource $k \in K^{v}$ and $n_{j m k} \leq n_{j m^{\prime} k}$ for each nonrenewable resource $k \in K^{v}$.

Table 1
Resource requirements and corresponding durations.

Non-executable mode: A mode $m^{\prime}$ is called non-executable if $\sum_{i=1, j \neq j}^{j} \min _{m} n_{j m k}+n_{j m^{\prime} k}>R_{k}^{*}$.
Redundant resource: A nonrenewable resource $k \in K^{v}$ is called redundant if $\sum_{i=1}^{j} \max _{j} n_{j m k} \leq R_{k}^{*}$. The pseudo code of the preprocessing is summarized in Fig. 4.

### 4.2. Encoding scheme

In our EDA, we adopt the activity-mode list (AML) based encoding scheme, which contains two parts: (1) an activity list (AL) $\left\{\pi_{0}, \pi_{1}, \pi_{2}, \ldots, \pi_{l+1}\right\} ;(2)$ a mode assignment list (ML) $\left\{\sigma_{0}, \sigma_{1}, \sigma_{2}, \ldots, \sigma_{l+1}\right\}$. The $\sigma_{j}$ in the ML indicates the mode of the $\pi_{l}$ in the AL. Kolisch and Hartmann [26] concluded by
![img-2.jpeg](img-2.jpeg)

Fig. 3. The general framework of EDA.

Step1: Remove all the non-executable modes;
Step2: Delete the redundant nonrenewable resources;
Step3: Eliminate all the inefficient modes;
Step4: If any mode has been erased within Step 3, go to Step2.
Fig. 4. Procedure of preprocessing.
![img-2.jpeg](img-2.jpeg)

Fig. 2. A feasible schedule of the example in Fig. 1.

![img-3.jpeg](img-3.jpeg)

Fig. 5. The AML representation for the schedule shown in Fig. 2.
experimental tests that procedures based on AL representations outperformed other procedures. In the MRCPSP, the mode assignment list is needed to assign every activity a mode. The EDA does not operate on a schedule but on the AML representation of a schedule. This character makes it convenient and effective for solving the MRCPSP.

With the above encoding scheme, a multi-mode schedule generation scheme (MSSGS) is used to transform the representation to a schedule. When a new AML is generated (the AL and ML part of the AML is changed by searching operation), the MSSGS is used to evaluate the AML. Consider the simple instance illustrated in Fig. 1, the AML representation for the schedule (as Fig. 2) is shown in Fig. 5. In the next section, we will present the multimode serial SGS (MSSGS) to implement the searching operations effectively in the EDA based on the AML.

### 4.3. Multi-mode serial schedule generation scheme

Schedule generation scheme (SGS) is an effective heuristic procedure that is used to decode solution representation of the RCPSP to a schedule [27]. Owing to the SGS, many algorithms could solve the RCPSP conveniently. However, it is more complicated to transform a solution representation of the MRCPSP to a schedule, since there are two more tough things that need to consider. First, there exists the nonrenewable resources infeasible solution representation that cannot be transformed into a schedule. Second, for the nonrenewable resources feasible representation, the nonrenewable resources may not be the utilized fully.

So far, many fitness functions have been proposed in literature for solving the MRCPSP, such as Hartmann [3], Alcaraz et al. [6], Jarboui et al. [8] and Lova et al. [15]. According to Lova et al. [15], their fitness function gave better results than other ones over all instances of PSPLIB. So, we adopt the fitness function proposed by Lova et al.. For an AML with ML $\left\{\sigma_{0}, \sigma_{1}, \sigma_{2}, \ldots, \sigma_{J+1}\right\}$, the fitness function is computed as follows:
$f(A M L)= \begin{cases}1-\frac{\text { max } \_ \text {mak } \_ \text {mob(AML) }}{\text { max } \_ \text {mak }}, & \text { if } \quad E R R(M L)=0 \\ 1+\frac{\text { mob(AML) } \_ \text {min_CP }}{\text { mob(AML) }}+E R R(M L) & \text { otherwise }\end{cases}$
where $\operatorname{mak}(A M L)$ is the makespan of AML; max_mak is the maximal makespan of feasible solutions related to individuals of the current generation; min_CP is the critical path using the minimal duration of each activity; and $E R R(M L)$ is the nonrenewable infeasible degree of ML, which is calculated as follows:
$E R R(M L)=\frac{\sum_{k=1}^{N} \max \left\{0, \frac{\sum_{j=1}^{J} n_{p_{j, k}}-R_{k}^{c}}{R_{k}^{c}}\right\}}{N_{k}^{c}}$.
It is noticeable that $E R R(M L)=0$ if the AML is nonrenewable resources feasible.

Based on that fitness function, we propose a multi-mode serial schedule generation scheme (MSSGS) for the MRCPSP. The MSSGS contains two procedures: infeasible tackling procedure to tackle infeasible representation and feasible tackling procedure to tackle feasible representation.

In order to transform a nonrenewable resource infeasible solution into a feasible one, we adopt the initial population local search procedure developed by Hartmann [3] as the infeasible tackling procedure, which chooses an activity randomly and changes its mode to a new one. If the $E R R$ is reduced, the new mode is kept. Such a procedure is repeated until the representation becomes nonrenewable resource feasible or the maximum iteration number SGS_adj is reached. If the solution is still infeasible, we calculate its fitness value. In our procedure, we adopt the number of activities $J$ as the maximum iteration number. That is, SGS_adj $=J$.

In order to fully use the nonrenewable resources, the feasible tackling procedure is developed, which is based on the multimode left shift bounding rule developed by Sprecher et al. [25]. The multi-mode left shift is a rule to improve the finishing time of activity one by one at the every decision point of the partial schedule by changing its mode without changing the modes and delaying the finishing times of any other activities. This rule could help utilize the nonrenewable resources more effectively. However, there is a weakness of the multi-mode left shift bounding rule. The activities scheduled earlier will occupy more amounts of nonrenewable resources. Whereas, the activities scheduled later will not have enough amounts of nonrenewable resources to use. As a result, this solution may trap into local minima. In our procedure, we develop a probability based selecting scheme controlled by a threshold SGS_Pper to guarantee that all the activities have equal opportunity to use nonrenewable resources.

The pseudo code of the MSSGS is illustrated in Fig. 6.
In a word, the MSSGS can reduce the nonrenewable resource consumption for infeasible representations to transform it into a feasible one and it also can increase the nonrenewable resource consumption to improve the makespan for feasible representations.

### 4.4. Probability model

Different from the GA that produces offspring through crossover and mutation operators, the EDA does it by sampling according to a probability model, which has a great effect on the performance. How to construct the probability model is the key issue to design the EDA [28].

In this paper, the probability model is composed of two probability matrixes: a $J \times J$ probability matrix Prob_act(t), and a $J \times M$ probability matrix Prob_mod(t).
(1) Prob_act(t): this matrix is used to predict the position of each activity in the $A L$.
$\operatorname{Prob}_{-} a c t(t)=\left(\begin{array}{ccc}\lambda_{11} & \cdots & \lambda_{1 j} \\ \vdots & \ddots & \vdots \\ \lambda_{j 1} & \cdots & \lambda_{j j}\end{array}\right)$
where the element $\lambda_{j j}$ represents the probability that the activity $j$ is placed at position $i$ of the $A L$ at generation $t$. That is, $\lambda_{j i}$ is an index to indicate how good it seems to place activity $j$ at position $i$.
This probability matrix is initialized as follows to ensure that the whole solution space can be sampled uniformly.
$\operatorname{Prob}_{-} a c t(0)=\left(\begin{cases}\} & \cdots \\ \vdots & \ddots \\ \} & \cdots \\ \} & \cdots\end{cases}\right)$

![img-4.jpeg](img-4.jpeg)

Fig. 6. Procedure of the MSSGS.
(2) $\operatorname{Prob} \_$mod $(t)$ : this matrix is used to predict the mode adopted by each activity.
$\operatorname{Prob} \_$mod $(t)=\left(\begin{array}{ccc}\mu_{11} & \cdots & \mu_{1 M} \\ \vdots & \ddots & \vdots \\ \mu_{j 1} & \cdots & \mu_{j M}\end{array}\right)$
where the element $\mu_{j i}$ represents the probability that the activity $j$ adopt mode $i$ at generation $t$. That is, $\mu_{j i}$ is an index to indicate how good it seems for activity $j$ to be carried out in mode $i$.

This probability matrix is initialized as follows to ensure that the whole solution space can be sampled uniformly.
$\operatorname{Prob} \_$mod $(0)=\left(\begin{array}{ccc}\frac{1}{M} & \cdots & \frac{1}{M} \\ \vdots & \ddots & \vdots \\ \frac{1}{M} & \cdots & \frac{1}{M}\end{array}\right)$

It needs to mention that $\mu_{j i}$ is set zero if the mode $i$ of activity $j$ is excluded as the inefficient or non-executable mode in the preprocessing procedure.

### 4.5. Probability generating mechanism

In order to generate a population based on the probability model, we should generate the selection probability of activity $j$ firstly. In this paper, we introduce a permutation-based probability generating mechanism (PGM).

At every position $i$, the selection probability of activity $j$, i.e. $P a_{i i}$, is calculated according to probability matrix $\operatorname{Prob}_{-} a c t(t)$ over the set of eligible activities $D_{i i}$, that is

$$
P a_{i i}=\frac{\lambda_{j i}}{\sum_{h=1}^{D_{i i}} \lambda_{h i}}
$$

![img-5.jpeg](img-5.jpeg)

Fig. 7. Procedure of the MPBLS.

If activity $j$ has already been placed in some positions, the whole line $\lambda_{j 1}, \lambda_{j 2}, \ldots, \lambda_{j l}$ of probabilistic matrix Prob_act is set zero. As a result, each activity could be selected only once in an $A L$. According to selection probability of each activity, we will generate an $A L$ by selecting activity one by one. Then we choose a mode for each activity in the AL according to the mode selection probability over the set of eligible modes $D_{m}$, that is
$P m_{j i}=\frac{\mu_{j i}}{\sum_{h=1}^{D_{m}} \mu_{h i}}$

### 4.6. Local search strategy

From the mechanism of the EDA, it seems that the EDA stresses more exploration than exploitation. To enhance the exploitation ability, a multi-mode version permutation-based local search strategy (MPBLS) is proposed to explore the neighborhood of the individual. The MPBLS exploits the neighborhood of AML systematically with the following procedure described in Fig. 7.

### 4.7. Multi-mode forward-backward iteration

Forward-Backward Improvement (FBI) is an effective technique for the RCPSP introduced by Li and Willis [29]. Basically, the procedure iteratively employs the SGS forward and backward scheduling until no further improvement in the makespan of project can be found. With the help of the MSSGS, we could extend the classic FBI to a multi-mode version FBI (MFBI). The MFBI could improve the fitness value not only by changing the AL sequence but also by changing the modes of activities to make use of nonrenewable resources more effectively. In Fig. 8, a single iteration step is used to illustrate procedure of the MFBI.

We now try to reduce the makespan of schedule in Fig. 2 by the MFBI. First, forward iteration shifts each activity to right as much as possible in descent order of activity ending times. With the help of the MSSGS, activity 5 is changed to mode 1. As a result, its duration reduces to 2 and NRC increases from 25 to 27 . In this way, we obtain a schedule with a makespan of 14 units. Second, backward iteration shift activities as much as possible to left in ascent order of activity starting times. Consequently, the makespan is reduced to 12 , as illustrated in Fig. 8.
![img-6.jpeg](img-6.jpeg)

Fig. 8. A single iteration step of MFBI and nonrenewable resource consumed (NRC).

### 4.8. Updating mechanism

In this paper, a population based updating mechanism is proposed to update the probabilistic matrixes Prob_act(t) and Prob_mod(t). First, a number of NP individuals are generated according to the matrixes, and MFBI and MPBLS are employed to renew the best $P$ individuals. Then, the best $P$ individuals are chosen to update the probabilistic matrixes according to the following equation:
$\operatorname{prob} \_a c t_{j i}(t+1)=(1-\beta) \cdot \operatorname{prob} \_a c t_{j i}(t)+\frac{\beta}{N} \sum_{k=1}^{P} I_{j i}^{k}:(1 \leq i, j \leq J)$
$\operatorname{prob} \_m o d_{j i}(t+1)=(1-\beta) \cdot \operatorname{prob} \_m o d_{j i}(t)+\frac{\beta}{N} \sum_{k=1}^{P} R_{j i}^{k}:(1 \leq i \leq M)_{i} 1 \leq j \leq J)$
where $\beta$ is the learning speed, $I_{j i}^{k}$ and $R_{j i}^{k}$ are the indicator functions.

The indicator functions are calculated as follows:
$I_{j i}^{k}= \begin{cases}1 & \text { if activity } j \text { is placed at position } i \\ 0 & \text { else }\end{cases}$
$R_{j i}^{k}= \begin{cases}1 & \text { if activity } j \text { chooses mode } i \\ 0 & \text { else }\end{cases}$

### 4.9. Procedure of the EDA

With the above design, the procedure of EDA for the MRCPSP is summarized as follows: First, the probability matrix is initialized uniformly. Second, the new population with $N P$ individuals is generated by sampling the probability matrix using the PGM. During every generation, all the individuals are evaluated by the MSSGS and sorted in ascent order according to the makespan values. The best $P(P<N P)$ individuals are selected from the population. Then the MFBI is applied to the selected $P$ individuals

![img-7.jpeg](img-7.jpeg)

Fig. 9. The framework of the EDA for the MRCPSP.
to improve the makespan value. After that, the MPBLS is applied to them for further improvement. After the local search operation, the probability matrixes $\operatorname{Prob}_{-} a c t(t)$ and $\operatorname{Prob}_{-} \operatorname{mod}(t)$ are updated based on the selected $P$ individuals. Straightforwardly, the framework of the EDA is illustrated in Fig. 9.

In the next section, we will carry out experiments based on a set of benchmarks and compare the EDA with some existing algorithms.

## 5. Computational experiments

We code the procedure in Visual C++ 2005 on IBM Thinkpad T61 with a Core 2 T7500 2.2 GHz processor and use the standard MRCPSP test data sets J10, J12, J14, J16, J18, J20 and J30 from the well-known PSPUB for testing, which are generated by the problem generator ProGen designed by Kolisch and Sprecher [30]. The optimal solutions for J10-20 sets are available, however no optimal solutions for J30 set were found. Each data set contains 640 instances, some of which are infeasible. We exclude the infeasible instances from our tests. Hence, we have 536 instances for J10, 547 instances for J20, 551 instances for J14, 550 instances for J16, 552 instances for J18, and 554 instances for J20. For the set J30, only 552 instances have found a feasible solution and not all optimal solutions are found. Each instance of J10-20 and J30 contains three modes (i.e. $M_{j}=3, j=1,2, \ldots, J ; M_{0}=1 ; M_{j+1}=1$ ), two renewable and two nonrenewable resources.

In the literature of the MRCPSP, two kinds of stopping conditions are used for comparison: the maximum number of the
generated schedules and the maximum CPU time consumed. We adopt the following three most frequently used stopping conditions for comparison: (1) 5000 generated schedules; (2) 1 s CPU time; (3) 0.15 s CPU time per activity. According to Lova et al. [15] and Van Peteghem and Vanhoucke [16], 1 generated schedule is defined as each activity of the project has obtained exactly only one feasible start time. In our MSSGS procedure, we have a probability $S G S \_$Pper for each activity to obtain the feasible start times for all the modes of this activity. In order to make a fair comparison with other algorithms available in literature, 1 schedule generated by the MSSGS is counted as
$\frac{\sum_{j=1}^{J}\left(S G S \_P p e r \cdot M_{j}+(1-S G S \_P p e r)\right)}{J}=1+2 \cdot S G S \_P p e r$
generated schedules.

### 5.1. Parameters setting

First, we use Taguchi method of design of experiment (DOE) [31] to determine a set of suitable parameters for the EDA. Since the J20 is the hardest data set of J10-20 sets, of which the optimal solutions are known, we choose the data set J20 to carry out the DOE test.

The EDA contains five key parameters: the population size of each generation $(N P)$, the number of selected individual to update the probability matrix $(P)$, the learning speed $(\beta)$, the MPBLS acceptance rate (EDA_Pper), and the threshold of the MSSGS (SGS_Pper). Combinations of different values of these parameters are shown in Table 2.

The average response variable (ARV) value is the following average deviation value for $N=554$ instances.
$A R V=\frac{\sum_{i=1}^{N} \cdot\left(\text { Makespan }_{i}-\text { OPT }_{i}\right)}{O P T_{i}} / N$
where Makespan $_{i}$ is the makespan of the $i$ th feasible instance in J20 obtained by the EDA; $O P T_{i}$ is the optimal makespan of $i$ th feasible instance in J20.

According to the number of parameters and the number of factor levels, we choose the orthogonal array $L_{25}\left(5^{5}\right)$. That is, the total number of treatments is 25 , the number of parameters is 5 , and the number of factor levels is 5 . The orthogonal arrays for J20 are listed in Table 3.

According to the orthogonal table, we illustrate the trends of each factor level with different stopping conditions in Figs. 10-12. Then, we figure out the response value changes of each parameter to analyze the significance rank of each parameter. The corresponding results are listed in Tables 4-6.

From Tables 4-6, it can be seen that: $\beta$ and $S G S \_$Pper are the two parameters that have the most significant impact on the algorithm no matter which stopping condition is used. According to the factor level trends, the best combinations of parameter values for the proposed EDA are determined, which are listed in Table 7.

Table 2
Combinations of parameter values.

From Table 7, we can see that the best parameters combination varies with maximum CPU time (the time of 5000 schedules equals to 0.143 s ). Consequently, we can see that the parameters $P, \beta$, and SGS_Pper decrease as the maximum CPU time increases and $N P$ keeps the same all the time. We utilize the linear least square method to determine the relationship between the value of each parameter (except NP) and the maximum CPU time (see Fig. 13). Since the EDA is some kind of incremental learning based method, the iterative number has a great impact on the parameters selection, e.g. in order to get a better result, the learning
speed with less number of generated schedules should be larger than the one with more number of generated schedules.

Clearly, different computers may have different computing power. To make sure the proposed EDA can be used on different computers, we provide the following guidelines to choose the EDA parameters based on maximum generated schedules $z$
$N P=100$

$$
p=-1.256 e^{-6} z+0.1806
$$

Table 3
Orthogonal table for the EDA.

Main Effects Plot (5000 schedules)
![img-8.jpeg](img-8.jpeg)

Fig. 10. Factor level trend with 5000 schedules.

![img-9.jpeg](img-9.jpeg)

Main Effects Plot ( $0.15 \mathrm{~s} /$ activity)
![img-10.jpeg](img-10.jpeg)

Fig. 12. Factor level trend with $0.15 \mathrm{~s} /$ activity.

Table 4
Response table for ARV with 5000 schedules.
Table 5
Response Table for ARV with 1 s .
$\beta=-4.399 e^{-6} z+0.5821$
$E D A \_P p e r=4.307 e^{-6} z+0.4253$
$S G S \_P p e r=-1.647 e^{-6} z+0.6462$
where $5000 \leq z \leq 104,895$.

### 5.2. Comparisons with existing algorithms

In this subsection, we compare the EDA with some existing algorithms based on the PSPLIB data sets to further show the effectiveness of the EDA.

We use Av. dev. to denote the average deviation from the lower bound. For the lower bound, the theoretically optimal values are used for set J10-20 and the critical-path based lower bounds are employed for set J30.

In Table 8, we compare the EDA with the simulated annealing developed by Józefowska et al. [4], the genetic algorithm developed by Alcaraz et al. [6], the hybrid scatter search developed by Ranjbar et al. [13], the hybrid rank-based evolutionary algorithm developed by Elloumi and Fortemps [12], the artificial immune system (AIS) developed by Van Peteghem and Vanhoucke [9], the two-phase genetic local search algorithm developed by Tseng and

Table 6
Response table for ARV with $0.15 \mathrm{~s} /$ activity.
Table 7
The best combination of parameters for the EDA.
![img-11.jpeg](img-11.jpeg)

Chen [14], and the efficient hybrid genetic algorithm developed by Lova et al. [15], the GA developed by Van Peteghem and Vanhoucke [16]. We denote these algorithms as JSA, AGA, RSS, EFEA, VPVAIS, TCGLS, LHGA, and VPVGA, respectively. The stopping condition for the comparison is 5000 generated schedules. It can be seen from the results in Table 8 that VPVGA and VPVAIS performs better than our algorithm, and VPVAIS has better performance than our EDA except J12. However, the EDA is among the most competitive algorithms. It can be seen that the EDA outperforms all the other algorithms for all sets.

In Table 9, we compare the EDA with EFEA and another efficient simulated annealing developed by Bouleimen and Lecocq [5] denoted as BLSA. The stopping condition for the comparison is

Table 8
Comparison with JSA, AGA, RSS, EFEA, VPVAIS, TCGLS, LHGA, and VPVGA (5000 generated schedules).
Table 9
Comparison with EFEA and BLSA (1 s CPU time).
[^0]Fig. 13. Parameters and stopping conditions (the time of 5000 schedules equals to 0.143 s ).


[^0]:    ${ }^{\text {a }}$ T7500 2.2 GHz, time limit 1 s .
    ${ }^{\text {b }}$ Pentium 3.00 GHz , time limit 1 s .
    ${ }^{\text {c }}$ Pentium 100 MHz , time limit five times the instance size (in seconds).

Table 10
Comparison with HGA and SDBB ( 1 s CPU time).

Table 11
Comparison with EFEA, JPSO, and DDE ( 0.15 s/activity).
1 s CPU time. It can be seen from Table 9 that our EDA not only has a higher optimal rate than EFEA and BLSA but also has lower average deviation with less computation resource.

In Table 10, we compare the EDA with the genetic algorithm developed by Hartmann [3] and the truncated branch and bound developed by Sprecher and Drexl [2], which are denoted as HGA and SDBB, respectively. The stopping condition for the comparison is 1 s CPU time. As a branch and bound algorithm, SDBB can solve J10 optimally. However, as the scale of problem increases, the performance of SDBB drops rapidly. It can be seen from Table 10 that the EDA outperforms SDBB in all sets except J10, and our EDA outperform HGA in all tested sets except that the feasible rate of our EDA for J30 is slightly lower than that of HGA.

In Table 11, we compare the EDA with the particle swarm optimization developed by Jarboui et al. [8] denoted as JPSO, the Differential Evolution developed by Damak et al. [11] denoted as DDE, and EFEA. The stopping condition for the comparison is 0.15 s CPU time per activity. It can be seen from Table 11 that our EDA not only has lower average deviation but also has better optimal rate than EFEA, JPSO and DDE for all the problem sets.

As an incremental learning method the EDA needs effort to find and track the most promising area at the beginning of the search procedure. As a result, some algorithms outperform the EDA when small computational effort (i.e. 5000 schedules as stopping condition) is allowed. However, the EDA can provide very competitive results when the allowed computational effort becomes relatively larger ( 1 s CPU time or 0.15 s/activity as stopping condition). All in all, the above comparisons between the EDA and many existing algorithms show that the proposed EDA is an effective algorithm for solving the MRCPSP.

## 6. Conclusion

This was the first reported work to design an estimation of distribution algorithm for solving the multi-mode resource-constrained project scheduling problem. By using an encoding scheme based on the activity-mode list and a decoding scheme based on the multi-mode serial SGS, the EDA could be applied to
the MRCPSP conveniently. By adopting a novel probability model and updating mechanism, the promising area could be tracked effectively to keep finding better solution. By applying the combined local search with multi-mode permutation based local search and multi-mode forward-backward improvement, the exploitation could be enhanced as well. Based on the DDE method, suitable parameter settings were determined, and the guidelines to set parameters of the EDA with different stopping conditions were provided. Simulation results based on the PSPLIB benchmarks and comparisons with some existing algorithms demonstrated the effectiveness of the proposed EDA. The further work is to develop an adaptive EDA with parameter learning mechanism and to extend the EDA method to solve other scheduling problems.

## Acknowledgments

The authors sincerely thank the Editor-in-Chief and the reviewers for providing the constructive and helpful comments to improve the quality of this paper. The authors also would like to thank Prof. Rainer Kolisch of the Technical University of Munich, Germany, for providing useful information about PSPLIB. This research is partially supported by National Science Foundation of China (Grant no. 70871065, 60834004) and the Program for New Century Excellent Talents in University (NCET-10-0505) as well as the Doctoral Program Foundation of Institutions of Higher Education of China (20100002110014).
