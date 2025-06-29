Associate Professor Hongbo LI, PhD<br>School of Management, Shanghai University, China<br>E-mail: ishongboli@gmail.com, hongbo_li@shu.edu.cn<br>Ziyi HU, Master's degree<br>School of Management, Shanghai University, China<br>E-mail: 512608474@qq.com<br>Hanyu ZHU, Master student<br>School of Management, Shanghai University, China<br>E-mail: zhuhanyu1101@qq.com (Corresponding author)<br>Associate Professor Yinbin LIU, PhD (Corresponding author)<br>School of Management, Shanghai University, China<br>E-mail: yinbinliu@126.com

# PREEMPTIVE RESOURCE LEVELING IN PROJECTS 


#### Abstract

As a well-known NP-hard problem in project scheduling, the resource leveling problem (RLP) has attracted many researchers'attentions. In the RLP, a typical assumption is that activities are non-preemptive during project execution, which means that activities cannot be interrupted once they have been started. However, preemption is not uncommon in project management practice and existing studies already show that it is beneficial to consider preemption when leveling resource usage. Therefore, we investigate the preemptive resource leveling problem and design a genetic estimation of distribution algorithm (GEDA). To analyze the performance of the GEDA, we conduct extensively computational experiments on 2160 randomly generated instances. We also examine the impacts of various factors on the GEDA. Comparative experimental results show that the GEDA outperforms the existing meta-heuristic algorithm.


Keywords: Project scheduling; Resource leveling; Preemption; Meta-heuristic algorithms.

## JEL Classification: M11, C44, C61

## 1 Introduction

It is increasingly popular to manage work in the form of projects. $20 \%$ of the global economic activities are organized by projects, which generate an annual economic value of approximately 12 trillion dollars ( $\mathrm{Li} \&$ Hall 2019). In project

management, allocating various types of resources effectively is a critical success factor for projects. As a well-known NP-hard problem in project resource scheduling, the resource leveling problem (RLP) has attracted many researchers' attentions. In the RLP, a baseline schedule is formed by specifying start time for each activity. This schedule levels the resource utilization while satisfying the precedence relations constraints and the project deadline constraint. Leveled resource usage can reduce unnecessary capital expenditures and avoid hasty deployment of temporary resources (Doulabi et al. 2011; Li et al. 2018). The systematic reviews of the RLP can be further referred to Demeulemeester \& Herroelen (2002), Neumann et al. (2003).

In the RLP literature, a typical assumption is that activities are non-preemptive during project execution, which means that activities cannot be interrupted once they have been started. However, preemption is not uncommon in project management practice. Due to management needs or external conditions, the execution of certain activities may be temporarily interrupted, e.g., stopping machines after work, software developers switching between different tasks, etc. (Ballestín et al. 2009). Preemption has been considered in many project scheduling problems, such as multi-project scheduling (Bock \& Patterson 1990), multi-objective project scheduling (Nudtasomboon \& Randhawa 1997), resource-constrained project scheduling (Ballestín et al. 2008; Demeulemeester \& Herroelen 1996), etc.

In the RLP, taking preemption into consideration can lead to more levelled resource utilization (Doulabi et al. 2011; Liu et al. 2019). Therefore, more attentions are being paid to the preemptive resource leveling problem (PRLP) and several exact and meta-heuristic algorithms have been proposed. In terms of exact algorithms, Son \& Mattila (2004) develop a linear programming model based on binary variables for the PRLP. Hariga \& El-Sayegh (2011) study a mixed integer programming model to minimize the cost caused by resource fluctuations and activity preemption. Nadjafi et al. (2013) proposes a branch-and-bound procedure to solve the PRLP.

The research on the meta-heuristic algorithms for the PRLP is scarce. Razavi \& Mozayani (2007) propose a genetic algorithm and they only allow noncritical activities to be interrupted. Alsayegh \& Hariga (2012) design a hybrid meta-heuristic for PRLP, in which the cost of splitting activities is taken into consideration. Splitting critical activities is not allowed neither. Doulabi et al. (2011) design a genetic algorithm for the PRLP, in which not all activities are

allowed to be preempted. Their objective function consists of two terms: minimizing the cost caused by resource utilization variations and that by activity preemption. In their genetic algorithm, the proposed encoding scheme tends to generate individuals violating the precedence relations constraints. So the authors add a feasibility repair mechanism to the genetic algorithm. They validate the genetic algorithm using 220 randomly generated instances and the data of a tunnel construction project. Different from the above-mentioned studies, we allow any activity to be interrupted at any integer time point. In this case, although the searching space will be enlarged, it increases the possibility of finding a better schedule that results in more leveled resource utilization.

Due to the RLP is NP-hard (Neumann et al. 2003), exact algorithms are only suitable for small instances. They can even hardly obtain feasible solutions for large-scale instances in a reasonable time. In this situation, heuristic algorithms become the only option. In addition, the introduction of preemption further increases the complexity of the RLP, which makes the RLP more difficult to be solved. Specifically, at the end of each unit time period, decisions about which activities should be scheduled need to be made, which significantly increases the number of feasible solutions. While in the non-preemptive RLP, the timing for scheduling decisions only corresponds to the completion of activities. Therefore, efficient meta-heuristic algorithms need to be devised to handle the PRLP.

In this paper, we investigate the PRLP and develop a genetic estimation of distribution algorithm (GEDA) that combines the genetic algorithm (GA) and the estimation of distribution algorithm (EDA). Our main contributions are as follows:
(1) For the first time, a meta-heuristic, GEDA, is proposed for solving the PRLP, in which each activity is allowed to be interrupted at any integer time point. On the one hand, to the best of our knowledge, there has been no research on meta-heuristics for this kind of PRLP. On the other hand, GAs and EDAs have been successfully applied to various project scheduling problems (Li et al. 2018; Li \& Dong, 2018; Forghani \& Fatemi-Ghomi, 2019). However, no studies that apply the EDA to solve the PRLP are found.
(2) In the GEDA, a schedule is encoded into an individual consisting of an activity list and a shift key vector. This encoding mechanism ensures that an individual always corresponds to a feasible schedule. The activity list and the shift key vector are updated by specially designed operators based on the EAD and the GA, respectively.

(3) To analyze the effectiveness and efficiency of the GEDA, we conduct extensively computational experiments on 2160 randomly generated instances. The results show that, for small-scale instances with no more than 30 activities whose optimal solutions are known, in most cases, the difference between the solutions obtained by the GEDA and the optimal solutions is within $5 \%$, and the average calculation time of each instance is less than 0.6 seconds. For small-scale instances whose optimal solutions are not known and large-scale instances with 100 activities, the GEDA obtains better solutions than CPLEX on more than half of the instances, while requiring only about $1 / 1000$ of the calculation time of CPLEX.

The rest of the paper is organized as follows. Section 2 states the PRLP, presents the corresponding optimization model, and gives an example for the PRLP. Our GEDA is described in Section 3. We perform computational experiments to analyze the performance of the GEDA in Section 4. The last section summarizes the paper and prospects future research directions.

# 2. The preemptive resource leveling problem 

### 2.1 Problem statement

The PRLP is described as follows. A project is represented by an activity-on-node network $G=(N, A) . N$ is the set of nodes representing activities, $N=\{0,1,2 \ldots, n, n+1\}$. The activities are topologically numbered from 0 to $n+1$. Activities 0 and $n+1$ are dummy ones, indicating the start and the end of the project. $A$ is the set of arcs indicating the precedence relations among activities. If $(i, j) \in A$, activity $i$ is the predecessor of activity $j$, which means that activity $j$ cannot be started until activity $i$ is finished. This kind of precedence relations is the same as that used in the critical path method (Demeulemeester \& Herroelen 2002). The project deadline is $\bar{d}$.

The start time and duration of non-dummy activity $i$ are denoted as $s_{i}$ and $d_{i}$, respectively. The duration of dummy activities is 0 . Without loss of generality, we assume that all time-related parameters are integer. There are $K$ types of renewable resources. During the execution of non-dummy activity $i$, its requirement for resource type $k$ at each time period is $r_{i k}, k=1,2, \ldots, K$. Dummy activities do not need any resources.

In project management practice, it is not uncommon to interrupt some activities such that resources can be re-allocated to other more critical activities. The interrupted activity is resumed after the resources become sufficient again. Therefore, without loss of generality, we assume that each activity is allowed to be

interrupted at any integer time point during execution. For activity $i$, let $p_{i}$ denote its number of preemption, $p_{i} \in\left[0, P_{i}\right]$, where $P_{i}$ is its maximum number of preemption $\left(P_{i}=d_{i}-1\right)$. If $p=0$, then activity $i$ is executed without preemption; If $p=P_{i}$, then activity $i$ is interrupted after each time unit.

If activity $i$ is interrupted $p_{i}$ times, then activity $i$ can be viewed as $p_{i}+1$ sub-activities and these sub-activities form a set $I_{i}=\left\{i_{1}, i_{2}, \ldots, i_{p_{i}+1}\right\}$. For each sub-activity $i_{q} \in I_{i}\left(q=1,2, \ldots, p_{i}+1\right)$, its start time and duration are denoted as $s_{i q}$ and $d_{i q}$, respectively.

The PRLP aims at minimizing the variations in resource utilization by constructing a baseline schedule $S$ that decides the start time and duration of each sub-activity under a preemption environment, while meeting the precedence relation constraints and the project deadline constraint.

# 2.2 Optimization model 

Treating each activity $i$ as $d_{i}$ successive sub-activities, each of which has a duration of 1 , we present the optimization model for the PRLP as follows:

$$
\begin{array}{ll}
\text { Minimize } & \sum_{k=1}^{p} \sum_{i=1}^{d}\left(c_{k} \cdot u_{k t}^{2}\right) \\
\text { Subject to: } & s_{0,1}=0 \\
& s_{n+1,1} \leq \bar{d} \\
& s_{i, d_{i}}+1 \leq s_{j, 1} \\
& \forall(i, j) \in A \\
& s_{i, q}+1 \leq s_{i, q+1} \\
& \forall i \in N ; q=1,2, \ldots, d_{i}-1 \\
& \sum_{i \in V_{t}} r_{i k}=u_{k t} \\
& k=1,2, \ldots, K ; t=1,2, \ldots, \bar{d} \\
& s_{i, q} \geq 0 \\
& \forall i \in N ; q=1,2, \ldots, d_{i}
\end{array}
$$

The objective function (1) minimizes the weighted sum of the square of resource usage (Demeulemeester \& Herroelen 2002), where $u_{k t}$ is the usage of resource type $k$ at each time period $t$ and $c_{k}$ is the weight of resource type $k$. The constraint (2) ensures that the project begins at time zero. The constraint (3) promises that the project is completed no later than the deadline. The constraints (4) represent the precedence relations, which means that the successor activities cannot be started until the last sub-activities of its predecessor have been finished. The constraints (5) indicate that the sub-activities of each activity should be executed sequentially. The constraints (6) are used to calculate $u_{k t}$, in which $V_{t}$ is the set of sub-activities that are executing during time period $t$. The constraints (7) let the start time of each sub-activity be non-negative.

Obviously, the object function (1) is non-linear due to the existence of $u_{k t}^{2}$. In addition, the set $V_{t}$ in constraints (6) also make the constraints non-linear. Therefore,

the above model is non-linear. However, based on the linearization method proposed in Rieck et al. (2012) and Liu et al. (2019), this non-linear model can be transformed into a linear integer programming model.

The PRLP can be reduced to the RLP by allowing each activity to be interrupted zero times. This means that the PRLP is a generalization of the NP-hard RLP (Neumann et al., 2003). Therefore, the PRLP is also NP-hard. In this case, exact algorithms can hardly find a satisfactory solution in a reasonable time for the large-scale PRLPs. We will design a meta-heuristic algorithm in Section 3 to efficiently obtain satisfactory solutions for the PRLP.

# 2.3 Example 

We use an example to illustrate the PRLP and show that it is possible to obtain a more leveled schedule after considering preemption. Figure 1 displays a project network with 4 non-dummy activities. The rectangles and the arrows represent activities and precedence relations, respectively. There is one resource type. The number above (below) each rectangle is the duration (resource requirement) of the corresponding activity. The project deadline is 4 . The weight of the resource $c_{1}=1$.
![img-0.jpeg](img-0.jpeg)

Figure 1. Example project network
When the preemption is not allowed, Figure 2 shows the resulting optimal schedule $S=(0,0,0,2,3,4)$ with the value of the objective function being $\sum_{k=1}^{1} \sum_{t=1}^{4}\left(c_{k} \cdot u_{k t}^{2}\right)=3^{2}+3^{2}+4^{2}+2^{2}=38$.

If we allow the preemption, we can obtain the optimal schedule $S^{\prime}=$ $[0,(0,3), 0,2,3,4]$ as shown in Figure 3. In $S^{\prime}$, activity 1 is interrupted once. The first sub-activity (1a) of activity 1 starts at time 0 with a duration of 2 and the second one (1b) starts at time 3 with a duration of 1 . The corresponding objective value of $S^{\prime}$ is $\sum_{k=1}^{1} \sum_{t=1}^{4}\left(c_{k} \cdot u_{k t}^{2}\right)=3^{2}+3^{2}+3^{2}+3^{2}=36$. It can be seen that a more leveled schedule is constructed after allowing the preemption.

![img-2.jpeg](img-2.jpeg)

Figure 3. The optimal schedule with preemption
Figure 2. The optimal schedule without preemption

# 3. Genetic estimation of distribution algorithm 

The EDA is a prospering meta-heuristic for solving optimization problems. There are some similarities between the EDA and the GA, e.g., they are population-based algorithms and the population is updated at each iteration. The EDA is based on statistical learning theory. The core of the EDA is probability models that describe the distribution of potential solutions in the searching space. The EDA updates its populations by sampling according to the probability models.

In our GEDA, there are POP individuals in the population. Each individual consists of two elements: an activity list $A L$ and a shift key vector $S K$ (Section 3.2). New individuals are generated by applying the EDA and the GA operators to the activity list and the shift key vector, respectively (Sections 3.3 and 3.4).
![img-2.jpeg](img-2.jpeg)

Figure 4. The framework of the GEDA
The framework of the GEDA is described as follows (Figure 4). First, the probability model $P M$ and the shift key vector $S K$ are initialized. $P M$ is used to

# Hongbo Li, Ziyi Hu, Hanyu Zhu, Yinbin Liu 

generate activity lists. Then, based on the probability generating mechanism, POP activity lists are obtained by sampling the probability model $P M$. Next, the individuals are decoded into schedules (Section 3.2) and the corresponding objective function values are calculated. After that, $P M$ is updated based on the top $\mathrm{POP}^{\prime}$ individuals in terms of the objective function value. In the meanwhile, crossover and mutation operators are adopted to update the shift key vectors. The above process keeps iterating and the schedules are improved until a pre-determined termination condition is satisfied.

### 3.1 Unit time project network

To simplify the schedule encoding mechanism, we introduce the unit time project network.

Definition: Unit time project network $G^{\prime}=\left(N^{\prime}, A^{\prime}\right)$. For each activity $i \in N$, splitting it into $d_{i}$ sub-activities, each of which has a duration of 1 . Let $N^{\prime}$ denote the set of the resulting sub-activities. For any two adjacent sub-activities, adding a precedence relation between them. The newly added and original precedence relations form the set $A^{\prime}$. In this way, $N^{\prime}$ and $A^{\prime}$ form the unit time project network $G^{\prime}$.

The set $N^{\prime}$ contains $\operatorname{subn}=\sum_{i=1}^{n} d_{i}$ non-dummy sub-activities. We re-number these sub-activities according to the following rule: For sub-activity $i_{q}$ $\left(q=1,2, \ldots, d_{i}\right)$, its number in $N^{\prime}$ is $m=\sum_{j=1}^{i-1} d_{j}+q$. The dummy end activity in $N^{\prime}$ is numbered subn +1 . Figure 5 illustrate this rule using the example project shown in Figure 1.


Figure 5. Numbering the sub-activities
After introducing the unit time project network, we do not need to specifically consider the interruption in the PRLP. Because for any two adjacent sub-activities $i_{q 1}$ and $i_{q 2}$ belonging to the same activity, if the finish time of $i_{q 1}$ equals the start time of $i_{q 2}$, then it means that there is no interruption between $i_{q 1}$ and $i_{q 2}$; otherwise, there exists interruption. In the following, our GEDA acts on the unit time project network $G^{\prime}$ to obtain the schedule for the RPLP.

### 3.2 Encoding and decoding

Properly encoding and effectively evaluating a schedule is the key to design effective meta-heuristic algorithms for solving the PRLP. In project scheduling

research, the meta-heuristic algorithms usually operate on some kind of encoding of the schedule. The schedule generation mechanism is used to decode the encoded schedule.

In the GEDA, an individual corresponds to a schedule. The individual is represented by a tuple $(A L, S K)$ of the activity list $A L$ and the shift key vector $S K$. The activity list $A L=\left(\pi_{1}, \pi_{2}, \ldots, \pi_{i}, \ldots, \pi_{\text {subn }}\right)$ is a permutation of the sub-activities, where $\pi_{i}$ is the sub-activity number that appears on the $i$ th position. The number of elements in $A L$ equals that of sub-activities subn. It should be noted that the order of the sub-activities in $A L$ does not need to obey the precedence relations constraints, because we will deal with these constraints in the decoding procedure. There are also subn elements in the shift key vector $S K=\left(s k_{1}, \ldots s k_{i}, \ldots, s k_{\text {subn }}\right), s k_{i} \in[0,1] . s k_{i}$ indicates the degree to which the start time of sub-activity $i$ deviates from its earliest start time. In other words, the earliest and latest start times of sub-activity $i$ form a time window, and $s k_{i}$ is the ratio of the difference between the start time of the sub-activity $i$ and its earliest start time to the time window. In the initial population, $A L$ is sampled from the initial probability model (Section 3.3.1), and $S K$ is generated randomly.

In the GEDA, the resource levelling schedule generation scheme (RLSGS) (Li et al. 2018; Li \& Dong 2018) is used to decode individuals into schedules. The main process of the RLSGS is as follows. For an individual ( $A L, S K$ ), the first unscheduled sub-activity $i$ indicated by $A L$ is selected and its start time is set as $s_{i}=e s_{i}+\left[s k_{i} \times\left(l s_{i}-e s_{i}\right)\right]$, where $e s_{i}\left\langle l s_{i}\right\rangle$ is the earliest (latest) start time of sub-activity $i$ after considering the scheduled activities. Then the earliest and latest start times of unscheduled sub-activities are updated. It can be seen that the start time assigned to each sub-activity in the above manner is always within a feasible time window, so that the precedence relationships between the sub-activities are satisfied. The above process is repeated until all sub-activities have been assigned a start time. In this way, the schedule is obtained. Given a schedule, we calculate its objective function value according to Equation (1), which is then used to evaluate each individual.

# 3.3 Operators on the activity list 

In each iteration of the GEDA, the activity list $A L$ is the updated using the probability models.

### 3.3.1 Probability-generating mechanism

In the probability-generating mechanism (PGM), the probability model

$P M=\left(\alpha_{1}, \alpha_{2}, \ldots, \alpha_{i}, \ldots, \alpha_{\text {subn }}\right)$ predicts the probability $\alpha_{i}$ that sub-activity $i$ is chosen when constructing the sub-activity list $A L$. The basic idea of the PGM is as follows. The numbers in the interval $\left(0, \sum_{i=1}^{\text {subn }} \alpha_{i}\right)$ correspond to different sub-activities. The sub-activity list can be obtained by sampling from this interval according to the probability $\left(\alpha_{1}, \alpha_{2}, \ldots, \alpha_{i}, \ldots, \alpha_{\text {subn }}\right)$ of each sub-activity in $P M$. Details on the PGM is shown in Algorithm 1.

# Algorithm 1. Using the PGS to generate the sub-activity list 

Input: the probability model $P M$
Output: the sub-activity list $A L$
$A L=\emptyset$
$U=\sum_{i=1}^{\text {subn }} \alpha_{i}$
For $\operatorname{pos}=1$ to subn
$\pi=1$
$\operatorname{Pr}=\alpha_{\pi}$
Sample a random number $r$ from the interval $(0, U)$
While $r>\operatorname{Pr}: \pi=\pi+1, \operatorname{Pr}=\operatorname{Pr}+\alpha_{\pi}$;
$\pi_{\text {pos }}=\pi$
$U=U-\alpha_{\pi}$
$\alpha_{\pi}=0$
End for
Return $A L=\left(\pi_{1}, \pi_{2}, \ldots, \pi_{\text {subn }}\right)$
In Algorithm 1, the initial sub-activity list $A L$ is set to empty. The sub-activity number $\pi$ needs to be inserted into $A L$, and the order that the sub-activities are selected is determined by the probability model $P M . \pi_{\text {pos }}$ represents the sub-activity number in $A L$ and pos is the pos-th position in $A L$ (pos $=1,2, \ldots$, subn). Whenever a sub-activity is put into $A L$, the corresponding element in $P M$ is set to 0 (i.e. $\alpha_{i}=0$ ). In doing so, we ensure that each sub-activity is only selected once, which means that after a sub-activity is selected, it will not be selected again. Given a set $\overline{N^{T}}$ of sub-activities that have not been added to the sub-activity list $A L$, the probability that the sub-activity $i \in \overline{N^{T}}$ is selected into $A L$ is $\alpha_{i} / \sum_{j \in \overline{N^{T}}} \alpha_{j}$.

At the beginning of the GEDA, we initiate $P M=(1 / \operatorname{subn}, 1 / \operatorname{subn}, \ldots, 1 /$ subn) such that each sub-activity is chosen with an equal probability. This means that we sample uniformly from the solution space to form the initial sub-activity list. In this way, the diversity of the initial solutions in the solution space is guaranteed.

### 3.3.2 Probability model updating mechanism

At the end of each iteration, the probability model $P M$ needs to be updated such that $P M$ can better estimate the distribution of the solutions. Specifically,

$\mathrm{POP}^{\prime}$ best individuals are selected from the POP individuals generated using the PGM in terms of the objective function value. Then the elements in $P M$ are updated based on the following formula:

$$
\alpha_{i}^{i}=(1-\beta) \cdot \alpha_{i}+\frac{\beta}{P O P^{\prime}} \sum_{j=1}^{P O P^{\prime}} \omega_{i}^{j}, 1 \leq i \leq \text { subn }
$$

where $\alpha_{i}^{i}$ is the updated value of $\alpha_{i}$, and $\beta$ is the learning speed. $\omega_{i}^{j}$ reflects the importance of sub-activity $i$ appearing in different positions of the sub-activity list. When constructing a sub-activity list using the PGM, it is implied that the more front the activity in the sub-activity list, the more important it is. Therefore, to calculate $\omega_{i}^{j}$, we let the sub-activity that appears first in the sub-activity list has the largest weight subn, the weight of the subsequent sub-activity decreases by 1 , and so on. So the weight of the last sub-activity in the sub-activity list is 1 . Consequently, $\omega_{i}^{j}=\frac{\text { subn }- \text { pos }+1}{\text { subn }+(\text { subn }-1)+\cdots+1}=\frac{\text { subn }- \text { pos }+1}{(\text { subn }+1) \text { subn } / 2}$, where pos is the position of sub-activity $i$ in $A L$.

# 3.4 Operators on the shift key vector 

The crossover and mutation operators from the GA are applied to the shift key vector to update it.

### 3.4.1 Crossover

Two-point crossover is adopted in the GEDA. First, POP/2 individuals are chosen as father individuals with probability $P_{c}$; and top $P O P / 2$ individuals in terms of the objective function value are selected as mother individuals. Then, the father and mother individuals are randomly matched into $P O P / 2$ pairs of individuals. Next, two crossover points $t_{1}$ and $t_{2}\left(1 \leq t_{1}<t_{2} \leq \text { subn }\right)$ are selected randomly. The father's (mother's) gene between $t_{1}$ and $t_{2}$ are copied to son (daughter) individual. The remaining gene positions in the son (daughter) individual are filled with the genes on the corresponding positions of the mother (father) individual.

### 3.4.2 Mutation

The mutation operator used in the GEDA is one-point mutation. For each child individual, each element in the shift key vector has a mutation probability of $P_{m}$. Specifically, for each element $s k_{i}(i=1, \ldots, \operatorname{subn})$ in the shift key vector, we generate a random number rand $\in(0,1)$. If rand is smaller than the mutation probability $P_{m}$, then we replace $s k_{i}$ with a new random number between 0 and 1 .

## 4. Computational experiments

Our GEDA is implemented in Matlab R2014a. Our computational experiments are performed on a computer equipped with an Intel Core i5 2.5 GHz

# 4.1 Experimental setup 

Our computational experiments adopt two benchmark data sets: $T_{\mathrm{A}}$ and $T_{\mathrm{B}} . T_{\mathrm{A}}$ is from Liu et al. (2019). Both sets are generated using the project scheduling problem instance generator RanGen (Demeulemeester et al. 2003). Specifying various control parameters in RanGen, project networks with different number of activities, topological structures and resource types can be produced. The main parameters of the data sets $T_{\mathrm{A}}$ and $T_{\mathrm{B}}$ are shown in Table 1. The order strength (OS) is the ratio of the number of precedence relations in the project network to the theoretical maximum number of precedence relations. The OS represents the complexity of the project network structure. $E S_{\mathrm{n}+1}$ is the critical path length computed by the critical path method.

Table 1. The main parameters of data sets $T_{\mathrm{A}}$ and $T_{\mathrm{B}}$

Given the parameter values of $T_{\mathrm{A}}$ in Table 1, 90 instances are generated for each value combination and this results in $3 \times 3 \times 1 \times 2 \times 90=1620$ instances in $T_{\mathrm{A}}$. In terms of the number of activities contained in each instance, $T_{\mathrm{A}}$ is a small scale data set.

The main difference between $T_{\mathrm{A}}$ and $T_{\mathrm{B}}$ is the number of activities. $T_{\mathrm{B}}$ is a larger data set with 100 activities in each instance. Given the parameter values of $T_{\mathrm{B}}$ in Table 1, 90 instances are also generated for each value combination and this results in $1 \times 3 \times 1 \times 2 \times 90=540$ instances in $T_{\mathrm{B}}$.

For the GEDA parameters, after fine-tuning the parameters, we set the population size $\mathrm{POP}=200$, the number of individuals used to update the probability model $\mathrm{POP}^{\prime}=50$, the learning speed $\beta=0.5$, the crossover probability $P_{\mathrm{c}}=0.8$ and the mutation probability $P_{\mathrm{m}}=0.3$. The termination condition of the GEDA is to generate up to 1000 schedules.

### 4.2. Performance measures

To evaluate the performance of our GEDA, we take the mixed-integer linear programming algorithm in CPLEX as the baseline algorithm and compare it with the GEDA. Specifically, we transform the model (1) - (7) into a mixed-integer linear programming model according to Liu et al. (2019). Then the resulting model

is solved using CPLEX. For CPLEX, the time limit for each instance is set to 600 seconds. This means that an optimal solution will be output if it can be found within 600 seconds. Otherwise, the best feasible solution is output.

In our experiments, the following performance measures are employed:
(1) Average relative deviation (ARD): The average percentage deviations from the objective values obtained in CPLEX. The ARD is calculated as follows:

$$
\text { ARD }=\frac{\sum_{i=1}^{n}\left[\left(o_{i}^{G E D A}-o_{i}^{C P L E X}\right) / o_{i}^{C P L E X}\right]}{n} \times 100 \%
$$

where $O_{i}^{G E D A}\left(O_{i}^{C P L E X}\right)$ is the objective function value of the $i$ th instance obtained by the GEDA (CPLEX) and $n$ is the number of instances in the test set. The value of the ARD reflects the performance difference between the GEDA and CPLEX. A smaller ARD value means that the GEDA can obtain better solutions.
(2) Computation time (CPU): Average computation times in seconds for solving each instance.

# 4.3. Computational results 

We examine the performance of the GEDA by comparing it with CPLEX. Table 2 shows the computational results on the small-scale test set $T_{\mathrm{A}}$. It should be noted that CPLEX only obtains the optimal solutions of 358 instances in $T_{\mathrm{A}}$. The remaining instances have only feasible solutions so far (Liu et al., 2019). Accordingly, the results in Table 2 are divided into two groups corresponding to the columns labeled with "Instances with known optimal solutions" and "Instances with feasible solutions only", respectively. The cells filled with "-" mean that the optimal solutions of the corresponding instances have not been found. A negative value of the ARD indicates that our GEDA outperforms CPLEX in the corresponding condition.

From Table 2, it can be seen that for instances with known optimal solutions, the solutions obtained by the GEDA are close to the optimal ones. For instances with feasible solutions, the GEDA obtains better solutions in more than half of the cases (at this time, the ARD is negative); in the other cases, the results of the GEDA are close to CPLEX (the ARD is less than $2 \%$ ). In terms of the computation time, the average CPU time of the GEDA is less than 0.6 seconds, which is much faster than CPLEX. In summary, the results in Table 2 show that for the small-scale PRLP instances, the GEDA is able to obtain satisfactory solutions in a short time.

Because the scale of the data set $T_{\mathrm{B}}$ is larger, CPLEX has not found the optimal solutions. The ARDs in Table 3 indicate the comparison results between

the solutions obtained by the GEDA and the best solutions of CPLEX. We can see from Table 3 that the GEDA obtains better solutions when the project deadline is loose. For the tight project deadline, the solutions of the GEDA are only slightly worse than CPLEX, and the difference between objective values is within $2 \%$. In addition, the average CPU time of the GEDA is within 6 seconds, whose efficiency is much higher than CPLEX. In short, when solving large-scale instances, the effectiveness and efficiency of our GEDA are also satisfactory.

Table 2. Computational results on the data set $T_{\mathrm{A}}$
Table 3. Computational results on the data set $T_{\mathrm{B}}$

# 4.4. Sensitivity analysis 

In this subsection, we examine the impact of the number of activities, the project deadline and the OS on the performance of the GEDA (Figures 6-9). In Figures 6-9, the lower the line, the better the results.

Figures 6-8 display the results on the small-scale test set $T_{\mathrm{A}}$. It can be seen that there are no obvious patterns for the impact of the number of activities. When

other factors are given, the GEDA can get better results for instances with 10 and 30 activities. For the project deadline, a looser deadline leads to better solutions. When the number of activities is small $(|N|=10)$, the impact of the OS is not obvious; as this factor becomes larger $(|N|=20,30)$, the GEDA achieves the best performance when the OS is the smallest.
![img-6.jpeg](img-6.jpeg)

Figure 6. Impact of the number of activities and the project deadline (set $T_{\mathrm{A}}$ )
![img-4.jpeg](img-4.jpeg)

Figure 7. Impact of the number of activities and the OS (set $T_{\mathrm{S}}$ )

Figure 9 shows the results on the large-scale test set $T_{0}$. Different from the results on the small-scale test set, given the OS, the tighter the project deadline, the better the performance of the GEDA. The impact of the OS on the GEDA is dependent on the project deadline: When the deadline is loose, the impact of the OS is not obvious; when the deadline is tight, the performance of the GEDA improves as the OS increases.
![img-5.jpeg](img-5.jpeg)

Figure 8. Impact of the OS and the project deadline (set $T_{\mathrm{A}}$ )
![img-6.jpeg](img-6.jpeg)

Figure 9. Impact of the OS and the project deadline (set $T_{0}$ )

# 4.5. Comparison with existing meta-heuristic algorithm 

Prior to our GEDA, no meta-heuristic algorithm has been found for the specific PRLP studied in this paper. Therefore, it is difficult to directly compare the GEDA with the existing meta-heuristic algorithm. However, in the existing literature, there are meta-heuristic algorithms for solving other types of PRLP. Among them, the HGA of Doulabi et al. (2011) is currently the best performing

meta-heuristic algorithm. There are some differences between our PRLP and the problem of Doulabi et al. (2011), such as they consider preemption costs, allow only a part of activities to be interrupted, and the activities require different amounts of resources at different times. Therefore, our GEDA can only be indirectly compared with the HGA in this paper. The results are shown in Table 4.

Table 4. Comparison results between our GEDA and the HGA of Doulabi et al. 2011

Since the results in Table 4 are indirect comparison results, some explanations need to be made before explaining these results: (1) The instances solved by the GEDA are those with known optimal solutions in $T_{\mathrm{A}}$. The data set used by the HGA is generated by PROGEN/MAX (Schwindt 1995). The project deadlines in both data sets are the same and both of them equal $1.0 \cdot E S_{n+1}$. (2) The number of schedules produced by the GEDA is 1000 while that for the HGA is 2500 . (3) As mentioned earlier, there are some differences between the problems solved by the GEDA and the HGA.

Although there are some differences in the experimental environments of the GEDA and the HGA, both algorithms are evaluated in terms of the average deviations from the optimal objective function value (i.e., the ARDs). Therefore, according to the ARDs, the GEDA and the HGA can still be compared to a certain extent.

We observe from Table 4 that when the number of activities exceeds 10 , the computational results of the GEDA are better than the HGA; in other words, the solutions obtained by the GEDA is closer to the optimal ones. A possible explanation would be that the encoding method used in the HGA has a probability of producing infeasible solutions during the iteration process, which may reduce the optimization efficiency of the HGA. While in the GEDA, our encoding method can ensure that the solutions generated in each iteration are always feasible. In addition, the CPU frequency used by the GEDA is lower than the HGA, but the running time of the GEDA is far less than the HGA. In summary, the results in Table 4 indirectly indicate our GEDA outperforms the HGA in terms of the solution effectiveness and efficiency.

# 5 Conclusions and future research 

We have proposed an effective and efficient meta-heuristic algorithm, GEDA,

for the PRLP. In the PRLP, each activity is allowed to be interrupted at any integer time point. Prior to this paper, there has been no meta-heuristics for this type of resource balancing problems. In the proposed GEDA, a schedule is encoded as an individual consisting of an activity list and a shift key vector. Our encoding and decoding methods ensure that the generated schedule is always feasible. Considering the characteristics of the RPLP, several specially designed operators are also integrated into the GEDA, e.g., the probability models, the probability-generating mechanism, the probability updating mechanism, the crossover and mutation operators.

Based on a large number of benchmark instances, the performance of the GEDA is analyzed through extensive computational experiments. The experimental results show that the GEDA is able to find satisfactory solutions within a reasonable time. For the instances with known optimal solutions, the gap between the solutions obtained by the GEDA and the optimal solution is within $5 \%$ in most cases. For the remaining instances, the solutions obtained by the GEDA are better than or close to CPLEX, while the calculation time of the GEDA is only about $1 / 1000$ of CPLEX. In addition, the comparative experimental results reveal that the proposed GEDA outperforms the existing meta-heuristic algorithm.

It will be an important research direction to design more effective meta-heuristics for the PRLP. Considering uncertainties in the PRLP will also be an interesting topic.

# ACKNOWLEDGEMENTS 

This work was supported by the National Natural Science Foundation of China (Grant Number 71602106) and the Key Soft Science Project of Shanghai Science and Technology Innovation Action Plan (Grant Number 20692192400).
