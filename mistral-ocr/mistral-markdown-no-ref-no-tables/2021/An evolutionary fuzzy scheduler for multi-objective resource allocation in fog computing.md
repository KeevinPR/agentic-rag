# An evolutionary fuzzy scheduler for multi-objective resource allocation in fog computing 

Chu-ge $\mathrm{Wu}^{\mathrm{a}}$, Wei $\mathrm{Li}^{\mathrm{b}}$, Ling Wang ${ }^{\mathrm{a}, *}$, Albert Y. Zomaya ${ }^{\mathrm{b}}$<br>${ }^{a}$ Department of Automation, Tsinghua University, Beijing, 100084, PR China<br>${ }^{\mathrm{b}}$ Centre for Distributed and High Performance Computing, School of Computer Science, The University of Sydney, NSW 2006, Australia

## A R T I C L E I N F O

Article history:
Received 31 January 2020
Received in revised form 12 December 2020
Accepted 24 December 2020
Available online 30 December 2020

## Keywords:

Edge computing
Internet of Things
Evolutionary computation
Estimation of distribution algorithm
Fuzzy scheduling
Agreement index
Robustness

## A B STR A C T

With rapid development of the Internet of Things (IoT), a vast amount of raw data produced by IoT devices needs to be processed promptly. Compared to cloud computing, fog computing nodes are closer to data resource for decreasing the end-to-end transmission latency. Considering the limited resource of IoT devices, offloading computationally-intensive tasks to the servers with high computing capability is essential in the IoT-fog-cloud system to complete those tasks on time. In this work, we propose a fuzzy logical offloading strategy for IoT applications characterized by uncertain parameters to optimize both agreement index and robustness. A multi-objective Estimation of Distribution Algorithm (EDA) is designed to learn and optimize the fuzzy offloading strategy from a diversity of the applications. The algorithm partitions applications into independent clusters, so that each cluster can be allocated to the corresponding tier for further processing. Thus, system resources are saved by making scheduling decisions in a reduced search space. Simulation studies on benchmark problems and real-world cases are carried out to verify the efficiency of our proposed algorithm. Pareto sets produced by our algorithm outperformed classic heuristic solutions for $88.3 \%$ benchmark cases and dominated Pareto sets of two state-of-art multi-objective algorithms for $92.7 \%$ and $94.4 \%$ cases correspondingly.
(c) 2020 Elsevier B.V. All rights reserved.

## 1. Introduction

In recent years, the Internet of Things (IoT) paradigm has increasingly been applied to all spheres of our daily life [1]. The successful operation of many IoT applications is increasingly relied on timely and decisive response [2], such as gaming, virtual reality, motion control in cars, and mobile video streaming. To shorten the turnaround time, task offloading is a promising practice to exploit the nearby available computational resources to complete the tasks of those IoT applications [3]. Compared to cloud computing that generally handles on-demand heavy computational tasks, fog computing [4] can be seen as an intermediate tier to deliver just-in-time computing resources between cloud centres and IoT devices. The use of fog computing enables the processing close to data sources and reduces the transmission delay over the Internet, as well as guarantees the users' security and trust issues [5]. To achieve these goals with optimal efficiency, it is imperative to properly distribute tasks to devices in different tiers of the IoT-fog-cloud environment.

The IoT application tasks offloading onto the computing resources can be modelled as task scheduling problems on heterogeneous multi-processors and it is well-known that this kind of

[^0]problem is generally an NP-hard problem [6]. For our problem, the processors are located at three tiers with different capacities while the dependent tasks are labelled with different due dates. This can be affirmatively proved to be NP-hard which has no known polynomial solution. Considering the successful application of evolutionary algorithms for large scale offline scheduling problems, an evolutionary algorithm is employed in this work. In addition, to properly distribute tasks to the processors located at different tiers of the system, the state of the processors is key to the task allocation. It is a noticeable resource consumption when all states of the processors are collected at the times. As such, to reduce the overhead of collecting the states of processors can greatly help to diminish the relevant system resource consumption. Besides, seeking for the task allocation on a reduced search space can also help to save system resources, so that a pre-partition method for the application without considering processor states is required.

Apart from the heterogeneous computing environment and response-time-sensitive requests from the applications, many uncertainties may exist [7] in the IoT-fog-cloud environment, which bring new challenges to the task scheduling problem. To simplify our analysis and highlight the essence of our argument, in this work, the structure of IoT applications is assumed to be known to the system. Also, the processing time of each task and the communication overhead between the tasks are not known exactly


[^0]:    * Corresponding author.

    E-mail address: wangling@mail.tsinghua.edu.cn (L. Wang).

and have uncertainties. In this way, the fuzzy number is used to model the corresponding data since its effective representation of the vague states of information [8].

In addition, prior and posterior measures have been extensively studied on fuzzy scheduling issues to estimate the robustness of solutions [9]. The posterior measure can only perform when the scheduling solution is obtained, such as $\varepsilon$-robustness [10], where if a certain algorithm is $\varepsilon$-robust, then the relative deviation between the prediction and the real value is bounded by $1 \pm \varepsilon$. On the other hand, prior measures can be evaluated during the scheduling decision. As one of the prior measures, $R O B$ represents the maximum possible difference between the solutions. Based on the credibility theory of fuzzy numbers, it can be proved that $R O B(\bar{l})$ coincides with the entropy of $\bar{l}$ [11]. The prior measure is chosen as an objective to improve the robustness of our solution since it can provide error estimation from the uncertainties in the decision-making progress in this work.

To optimize the agreement index of the applications as well as to guarantee the robustness of our scheduling solution, we model the task offloading and scheduling problem as a multiobjective offline optimization problem and find out a fitness trade-off between performance index and the robustness. The remainder of the paper is organized as follows: Section 2 reviews the related work. Section 3 provides the basic concepts on multiobjective optimization problem, fuzzy theory and the problem statement including system and application model, mathematic model and the robustness analysis. Then, the proposed algorithm is detailed described in Section 4. In Section 5, the numerical studies are provided to demonstrate the effectiveness of our proposed algorithm. Finally, the paper draws some conclusions and outlines ideas for future work in Section 6.

## 2. Related work

To optimize the IoT-fog-cloud system performance, resource allocation and computational task offloading are core aspects to consider. The resource allocation and computational task offloading problems turn to be more difficult and complicated since inherent heterogeneity, uncertainty and dynamic within the computing environment as well as the different objectives raised up by users and operators. As the most important performance index, different expressions of indexes are proposed to mathematically describe the time-sensitive request of IoT applications. An online strategy [12] is proposed to maximize the number of tasks meeting deadlines. Tardiness [13] is set as a penalty variable within the fitness value. Delay constraints are adopted in [14] to obtain feasible solutions. Apart from the performance index, the objectives, such as cost and energy consumption, are taken into consideration under different situations. Some state-of-art evolutionary algorithms [15-17] are adopted and perform well in multi-objective problems as it is capable of adjusting the solution accordingly.

Apart from optimization objectives, different kinds of scheduling models are proposed to emulate practical condition. Task queue model [18-21] is adopted to describe the task generating and caching situation in the gateway, fog and cloud nodes. In spite of the task queue model, independent task model [22,23] is used to model user requests. Quality of Experiment (QoE) aware application placement solution is presented in [22] where tasks are clustered by fuzziness method and labelled with linguistic classification. Inspired by this work, fuzzy logic is employed to realize fuzziness and de-fuzziness onto the application tasks in our work.

In addition, to model the precedence constraints between tasks, Direct Acyclic Graph (DAG) is used to model the application. Heterogeneous earliest finish time (HEFT) [27] produces
![img-0.jpeg](img-0.jpeg)

Fig. 1. Membership function of a triangular fuzzy number [30].
scheduling schemes in heterogeneous processors environment for shortening application completion time. Tasks are sorted and opportunistically inserted to available processor idle time slot of towards the earliest finish time. HEFT is ranked as the best of twenty scheduling heuristic methods in terms of robustness and performance [28]. A mixed-integer linear programming is presented in [24] to model offloading the dependent tasks with deadline constraints in IoT-fog system. This work ignores IoT devices and takes the cloud computing tier as a processor with unlimited computing capability. To solve the multi-objective DAG task scheduling problem, multi-objective HEFT [29] is designed as a general framework to provide a set of solutions for the decision maker. New solutions are sorted according to crowding distance and best $K$ solutions are chosen as Pareto set. Fuzzy dominance is introduced to improve the performance of MOHEFT in [25], which optimizes both makespan and cost index. Related works on fog resource allocation problem are summarized in Table 1. In this work, we consider a fuzzy DAG task scheduling problem where the agreement index is used to evaluate task latency. Meanwhile, robustness is another objective which is considered to guarantee the stability of the algorithm.

## 3. System modelling and problem statement

### 3.1. Basic concepts of fuzzy number

In the practices, IoT application data is hard to be precisely determined in advance. Thus, the task processing time, inter-task communication data and the deadline of tasks are modelled as fuzzy numbers in this work. Related fuzzy theory is introduced below.

Fuzzy set and membership function [30]: Fuzzy set $\bar{A}$ in a universe of discourse $X$ is characterized by a membership function $\mu_{\bar{A}}(X)$. For each element $x$ in $X$, a real number value function $\mu_{\bar{A}}(x) \in(0,1)$ denotes the membership grade of $x$ in $\bar{A}$, which indicates how likely an element $x$ belongs to $\bar{A}$
$\mu_{\bar{I}}(x)= \begin{cases}0, & x<p \text { or } x \geq r \\ \frac{x-p}{q-p}, & p \leq x<q \\ \frac{x-r}{q-r}, & q \leq x<r\end{cases}$
Fuzzy number: A fuzzy number $\bar{l}$ is a fuzzy subset whose membership is convex and normal. According to the characteristic of membership functions, there are different types of fuzzy numbers, such as normal fuzzy number, triangular fuzzy number (TFN) and semi-trapezoid fuzzy number.

Triangular fuzzy number: TFN is chosen to model the task workload and data transfer overhead in this work. For TFN $\bar{l}$, it is denoted as ( $p, q, r)$, where ( $p, q, r$ ) represents correspond the smallest likely value, the most probable value, and the largest possible value of any fuzzy event. The membership function of a TFN is given below as Fig. 1.

Table 1
Literature classification for fog resource allocation problem.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Nearness calculation of TFNs [30].

The basic operations of TFN are shown as below. The sum of two TFNs $\widehat{I_{1}}=\left(p_{1}, q_{1}, r_{1}\right)$ and $\widehat{I_{2}}=\left(p_{2}, q_{2}, r_{2}\right)$ can be calculated as:
$\widehat{I_{1}}+\widehat{I_{2}}=\left(p_{1}+p_{2}, q_{1}+q_{2}, r_{1}+r_{2}\right)$
The maximum number of two TFNs can be calculated as $\left(\max \left(\boldsymbol{p}_{1}, \boldsymbol{p}_{2}\right), \max \left(\mathbf{q}_{1}, \mathbf{q}_{2}\right), \max \left(\boldsymbol{r}_{1}, \boldsymbol{r}_{2}\right)\right)$. In addition, to compare $\widehat{I_{1}}$ and $\widehat{I_{2}}$, signed distance is used for de-fuzzification to achieve the total cost estimate in the fuzzy sense. The signed distance of a TFN can be calculated as (3). In the rest of the paper, we will use it to rank and compare the given TFNs.
$\operatorname{dis}(l)=\frac{p+2 q+r}{4}$
Nearness degree: Nearness degree is a metric to measure the similarity of two fuzzy sets, which can be denoted as $N(\mathrm{~A}, \mathrm{~B})$. Considering the meaning of nearness degree, one of the nearness degree calculation methods is chosen to measure the closeness between the fuzzy numbers in this work which is formulated as (4).
$N_{1}(B, A)=\vee_{x \in X}\left(\mu_{B}(x) \wedge \mu_{A}(x)\right)$
where for $\wedge$ and $\vee$, we have $a \vee b=\max (a, b)$ and $a \wedge b=$ $\min (a, b)$.

Based on (4), for TFNs $\widehat{I_{1}}$ and $\widehat{I_{2}}, N_{1}\left(\widehat{I_{1}}, \widehat{I_{2}}\right)$ is calculated as the minimum point of intersection between two membership function curves as Fig. 2 shows.

### 3.2. Basic concepts of multi-objective optimization problem

The multi-objective optimization problem (MOP) is adopted to model the problem in this work to balance the performance and robustness of the solution. MOP aims to find out the optimal solution for more than one objective while the objectives are contradictive. Despite the optimization of each single objective, the trade-off between objectives is required to address during the decision making. The problem can usually be defined as follows.
$\min f(x)=\left(f_{1}(x), f_{2}(x), \ldots, f_{q}(x)\right)$
where $f(x) \in R^{q}$ is the objective vector that contains $q$ individual objectives. To evaluate solutions, non-dominated sorting method is adopted.

Pareto dominance: A solution $x_{1}$ is considered to dominate solution $x_{2}$ (denoted as $x_{1} \succ x_{2}$ ) if and only if:
$f_{i}\left(x_{1}\right) \leq f_{i}\left(x_{2}\right), \forall i \in\{1,2, \ldots, q\}$
$f_{i}\left(x_{1}\right)<f_{i}\left(x_{2}\right), \exists i \in\{1,2, \ldots, q\}$
Optimal Pareto solution: If one solution is not dominated by any other solutions, it is called the optimal Pareto solution.

Non-dominated solution set/archive set (AS): For a specific algorithm, the archive set consists of all optimal Pareto solutions of it. To reflect the dominance relationship between the solutions in two archive sets, say, $\mathrm{AS}_{1}$ and $\mathrm{AS}_{2}$, converge metric ( $C$ metric) is widely used, which is calculated as (8):
$C\left(A S_{1}, A S_{2}\right)=\frac{\left|\left\{x_{2} \in A S_{2} \mid \begin{array}{c}\exists x_{1} \in A S_{1}, x_{2} \prec x \\ \text { or } x_{2}=x_{1}\end{array}\right\}\right.\right|}{\left|A S_{2}\right|}$
where $C\left(\mathrm{AS}_{1}, \mathrm{AS}_{2}\right)$ reflects the percentage of the solutions in $\mathrm{AS}_{2}$ that are dominated by or identical to the solutions in $\mathrm{AS}_{1}$.

Another indicator, Inversed Generation Distance (IGD), is also widely used to compare archive sets. IGD estimates the distance from the obtained Pareto front to the true Pareto front. For each solution, the minimum Euclidean distance between the solution and the true Pareto front is calculated. A set of distances are calculated and the average value of them is IGD, which gives a measure of both diversity and convergence.

### 3.3. System and application models

A generalized three-tier IoT system [31] consisted of IoT devices, fog devices and cloud servers is considered in this work as Fig. 3.

The first tier is called things tier where various IoT devices are responsible for sensing, collecting raw data and processing the data accordingly before sending out for further computation. In this work, IoT devices are homogeneous and equipped with both sensing and actuating components. Devices are grouped into clusters according to their location. For each group, devices are fully connected.

The second tier is named fog tier. In this work, it is assumed that each fog node is connected with a certain clusters directly and fog nodes are fully connected. The cloud servers are the main computing component of the third tier [32]. Fog nodes are linked with cloud tier via wide area network. The more discussion on

![img-2.jpeg](img-2.jpeg)

Fig. 3. An overview of the three-tier loT system architecture [26].
![img-3.jpeg](img-3.jpeg)

Fig. 4. $\overline{d d l}(j)$ and the calculation of $A l_{j}[30]$.
the needs of the employment of fog computing can be found in [31].

DAG is adopted to model loT applications which consist of dependent tasks. Tasks are assumed to be non-preemptive and all the tasks can be processed after all its precedent tasks be finished and its input data is received in this work. A five-tuple vector $\left(V, E, \hat{w}, \hat{D}, \overline{d d l}\right)$ is used to model a DAG application, where $V$ denotes a set of non-communication tasks. $E=\left\{E_{i j}\right\}$ is a set of directed and weighted edges representing the precedence constraints. To model the uncertainty of loT applications, processing time, communication overhead and due date are described with fuzzy numbers where $\hat{w}_{j}$ represents the fuzzy processing time of $v_{j}$ and $\overline{D(i, j)}$ represents communication overhead of $E_{i j}$.

On the other hand, due time is assigned to each task in the applications to model the needs to users. $\overline{d d l}(j)$ indicates the due time of task $j$ and it is represented by a right semi-trapezoid fuzzy number $\left(d d l_{1}, d d l_{2}\right)$ as shown on the left of Fig. 4.

Similar to the tardiness index in crisp scheduling problem, Agreement Index (AI) [33] is introduced to measure and evaluate the tardiness of the scheduled task. $A l_{j}$ is calculated as (9) where $\overline{C_{j}}$ denotes the completion time of task $j$. It is illustrated as the right of Fig. 4 and obviously, $A l_{j} \in(0,1)$.
$A l_{j}=\frac{\operatorname{area} \overline{C_{j}} \cap \overline{d d l_{1}}}{\operatorname{area} \overline{C_{j}}}$
In addition, a priori robustness index, $R O B$, is used to evaluate the robustness of a solution. It represents the maximum possible deviation of the fuzzy interval. For TFN $\bar{l}=(p, q, r)$, it can be calculated as (10):
$\operatorname{ROB}(\bar{l})=\max (q-p, r-q)$

### 3.4. Fuzzy scheduling model

The objective of the computational offloading problem is to generate a robust schedule with high agreement index, i.e. to maximize the total agreement index and minimize the robustness index of a certain loT application simultaneously. Based on
the system and application models, the notations are given in Table 2. The mathematic formulation and constraints are given afterwards. The model regards the mathematic model in [24], where the crisp scheduling model is transferred to fuzzy one.
$\min \left(1-\left(\sum_{j=1}^{n} A l_{j}\right) / n, R O b_{C_{\max }}\right)$
Subject to:

$$
\begin{aligned}
& \sum_{t=1}^{n} \sum_{i=1}^{m} x_{j, i, r}=1, \forall j \\
& \sum_{j=1}^{n} x_{j, i, r} \leq 1, \forall i, r \\
& \sum_{j_{1}=1}^{n} x_{j_{1}, i, r} \geq \sum_{j_{2}=1}^{n} x_{j_{2}, i, r+1}, \forall r \leq n-1, i \\
& \tilde{C}_{j_{1}}-\tilde{C}_{j_{2}}+\tilde{M}\left(2-x_{j_{1}, i, r+1}-x_{j_{2}, i, r}\right) \geq \frac{\tilde{w}_{j_{1}}}{v_{1}}, \forall j_{1}, j_{2}, r \leq n-1, i \\
& \tilde{C}_{j_{1}}-\tilde{C}_{j_{2}} \geq \sum_{r=1}^{n} \sum_{i_{1}=1}^{m} x_{j_{1}, i_{1}, r} \cdot \frac{\tilde{w}_{j_{1}}}{v_{1_{1}}} \\
& \quad+\sum_{i_{1}=1}^{m} \sum_{i_{2}=1}^{m} \sum_{r=1}^{n} \sum_{r=1}^{n} x_{j_{1}, i_{1}, r} \cdot x_{j_{2}, i_{2}, r} \cdot \frac{\tilde{D}\left(j_{1}, j_{2}\right)}{B\left(i_{1}, i_{2}\right)}, \forall j_{1} \rightarrow j_{2} \\
& \tilde{C}_{\max } \geq \tilde{C}_{j}, \forall j
\end{aligned}
$$

where (11) defines the bi-objective optimization problem. Eqs. (12)-(14) guarantee the validity of the generated solution. More precisely, (12) ensures that each task can be processed once and only once. At a given position of the processor, no more than one task can be processed according to (13). The order of the queue is strictly met according to (14), which means $(r+1)$ th task does not exist in the queue if there is no the $r$ th task on the certain processor. As the completion time and data size are all fuzzy numbers, the operators in (15) and (16) are the fuzzy operators. Eq. (15) ensures that for two tasks on the same processor, the $(r+1)$ th task should not be processed before the completion time of the $r$ th task. Eq. (16) ensures the validity of precedence constraints between the tasks and (17) presents how makespan is calculated.

## 4. The details of the proposed algorithm

The proposed algorithm is designed to achieve a robust scheduling solution and its detail is given in this section. First of all, the flowchart of the algorithm is presented to provide an overview. And then, a fuzzy clustering method, which is used to pre classify the task graph and its specific operators are explained in details. After that, an enhanced EDA proposed for fuzzy partition rule learning is introduced. In addition, two local intensification methods designed for opportunistic improving the system performance are presented. A complexity analysis is offered at the end.

### 4.1. Flowchart

Our proposed algorithm is illustrated in Fig. 5. loT application is clustered through fuzzy pre partition method in accordance to task characteristics. After have been clustered into $L$ groups, these groups of tasks are assigned to corresponding tiers according to the "cluster-tier allocation rule", which is produced, evolved and optimized by fuzzy EDA.

Table 2
Notations for the models.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Diagram of the proposed algorithm.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Flow chart of the proposed algorithm.

The flow chart of the whole algorithm is provided in Fig. 6. It can be seen that the second part of the algorithm is fuzzy partition learning method, which is an enhanced EDA with a knowledge driven local intensification procedure. The AS containing Pareto solutions are outputted as the results.

### 4.2. Fuzzy pre partition

Fuzzy logic combines both numerical and linguistic information obtained from human experts. Task clustering is the first and essential step of the fuzzy logic based partition strategy that aims to partition the application without knowing the latest status of the processors. In this work, based on three features of tasks, all the tasks are classified into different clusters through the fuzzy nearness calculation method.

As the computational workload directly influences the computing resource requirement, and the communication overhead influences the latency between different tiers, three features of tasks: computational processing time, input and output communication overhead, are used to cluster the tasks. The input and output data size of task $k$ is calculated by (18) and (19), respectively:

$$
\begin{aligned}
& \widehat{D_{i n}}(k)=\sum_{j} \widehat{D(j, k)}, \forall j \in \text { Parents }(k) \\
& \widehat{D_{\text {out }}}(k)=\sum_{j} \widehat{D(k, j)}, \forall j \in \text { Children }(k)
\end{aligned}
$$

where Parents $(k)$ and Children $(k)$ denote the sets of parent and children tasks of task $k$. Then, the tasks are labelled by these three features:

![img-6.jpeg](img-6.jpeg)

Fig. 7. (a) Maximum nearness value (Upper) (b) Minimum distance (Below).
![img-7.jpeg](img-7.jpeg)

Fig. 8. Fuzzy Rule for task-tier assignment.

Computational processing time: $\hat{w} \in$ Short, Moderate, Long); Input/Output data size: $\hat{D}_{0 i} / \hat{D}_{\text {out }} \in$ (Small, Medium, Large) (see Fig. 7).

For each dimension, the tasks are sorted by fuzzy dominance to label the tasks. The detailed pseudo code is provided as Method 1. As shown in Method 1, for each dimension, tasks are sorted in the descending order of $\hat{I}$ and the minimum, average and maximum values are chosen as the centres of corresponding clusters. In this way, all the tasks are labelled with three levels.

Method 1: Procedure of fuzzy pre partition
For $r$ in (computational processing time, input data size, output data size)
$\hat{I}=\hat{w} / \hat{D}_{\text {out }}^{r} / \hat{D}_{\text {out }}^{r}$ and sort the tasks in accordance to the descending order of $\hat{I}$;
Large $:=\operatorname{max}(I)$; Medium $:=\operatorname{avg}(I)$; Small $:=\min (I)$;
For each task $k$
$N_{1 k}(k):=N_{1}(I$, Large $) ; N_{1 M}(k):=N_{1}(I$, Medium $) ; N_{1 S}(k):=N_{1}(I$, Small $)$.
If $3 N_{1 k}(k)>0, \forall x$ (As shown in Fig. 7 (b))
$d_{c}(k):=d i s(\operatorname{Small}, \hat{I}) ; d_{M}(k):=d i s(\operatorname{Small}, \hat{I}) ; d_{L}(k):=d i s(\operatorname{Small}, \hat{I})$.
Level $(k)=\operatorname{argmin}\left(d_{c}(k), d_{M}(k), d_{L}(k)\right)$;
Else (As shown in Fig. 7 (a))
Level $(k)$ : $=$ argmax $\left(N_{1 k}(k), N_{1 M}(k), N_{1 S}(k)\right)$;
End
End
End

## 4.3. "Cluster-Tier" allocation rule

After the pre partition, each task is labelled and all tasks are clustered into $3 \times 3 \times 3=27$ clusters. Then, it is needed to learn and determine the "cluster-tier" allocation rule as illustrated in Fig. 8. For each task cluster, there are four choices: things tier, fog tier, cloud tier and the whole system and the solution space of tier assignment is $4{ }^{27}$, which is too large for the Bruteforce approach. Thus, an EDA is employed to produce, evolve and optimize this rule.

Once the task-tier assignment rule is determined, the tasks will be assigned to the processors of corresponding tier by the insert based rule of heterogeneous earliest finish time first [27]. After that, the $A I$ and $R O B$ of each application can be achieved

Fig. 9. Example of encoding method.
accordingly. The details of our proposed EDA for fuzzy task-tier assignment rule learning are given in next section.

### 4.4. EDA for the allocation rule learning

EDA is a population based evolutionary algorithm which builds a probability model to describe the solution space and learns from the elite individuals. Many kinds of statistics sampling and updating methods could be chosen accordingly to learn, evaluate and build the possibility model. Standard EDA procedure is summarized as follows. Firstly, probability model $P$ is built, and the individuals are sampled with $P$. The generated individuals are then evaluated. Then, $P$ is updated in accordance to the elite individuals. After that, new individuals are sampled with the updated $P$ value until the stopping criterion is met.

## Encoding and decoding

Individuals are encoded according to the tier assignment rule as Fig. 9, where $t_{k}$ represents the tier assignment of the $k$ th cluster. We have $t_{k} \in\{0,1,2,3\}$ where $\{0,1,2\}$ refers to the things, fog, and cloud tier respectively and 3 represents the whole system, which represents the case of no exact tier assignment is recommended for this cluster of tasks.

HEFT is employed as the decoding method to schedule the tasks to corresponding processors after the tier assignment is determined. According to HEFT, tasks are sorted in sequence of the application DAG topological structure and all the computational nodes are considered as heterogeneous parallel processors. Each task is assigned to the earliest available processor or the valid idle space.

## Probability model and its initialization

Tier assignment probability model $P$ is designed as (20), where $p_{k, j}(g)$ represents the probability that the $k$ th category tasks should be encoded as $j$ at the $g$ th generation of the evolution. For each $k$, we have $\sum_{j} p_{k, j}(g)=1$. In addition, $P$ is initialized randomly, e.g. $p_{k, j}(0)=0.25$ for each $k, j$.
$P(g)=\left\{p_{k, j}(g)\right\}_{L \times 4}$

## Sampling and updating method

The $k$ th position of the encoding string in Fig. 9 is generated by sampling the $k$ th row with Roulette Wheel Method (RWM). In addition, the probability model is updated with individuals in AS, which is the set of Pareto solution achieved until the current generation. With individuals in AS, the probability model learns from both history data and current elite individuals. Population based incremental learning method (PBIL) [34] is used for updating as (21), where $\alpha \in(0,1)$ denotes the learning rate and $I_{k, j}^{\prime}(g)$ is the indicator function corresponding to the $i$ th individual of AS.

The pseudo code of the proposed EDA is presented as Method 2 .
$p_{i, j}(g+1)=(1-\alpha) \times p_{i, j}(g)+\alpha \times \sum_{i} I_{k, j}^{\prime}(g) /|A S|$
$I_{k, j}^{\prime}(g)= \begin{cases}1, & \text { kth task category is assigned to } \\ & j \text { in the } k \text { th individual } \\ 0, & \text { otherwise }\end{cases}$

## Method 2: EDA for the allocation rule learning

$P(g)$ : probability model at the $g$-th generation;
$G$ : the number of evolution generations;
$P_{k, g}(0)=0.25, \forall k, j$
While $g \in G$
For $l$ from 1 to $N$
For $k$ from 1 to $L$
$t_{k}=\mathbf{R W M}\left(p_{k, 1}(g), p_{k, 2}(g), p_{k, 3}(g), p_{k, k}(g)\right)$;
End
Decode the $l$-th individual with HEFT;
Update AS with the $l$-th individual;
End
For individual $x$ in AS
Implement Method 3 for $x$;
End
Update $P$ through (20); $g^{++}$;
End

## Local Intensification

To enhance the exploration of the proposed algorithm, a problem specific local search methods are designed to achieve better solutions. Here, we adjusted the tier assignment of tasks with small $A I$ within the limited local search calculation budget. The encoding string is altered directly when possible. For the specific solution in AS, to decrease the task latency, all the clusters of tasks are sorted in the ascending sequence of average $A I$. In this order, other tier assignment choices are tried until the stopping criterion is met.

After the evaluation of individuals in population, local search procedure is used for each solution in AS. AS is updated by the new solutions produced by the local search.

```
Method 3: Local intensification procedure
\(T=(0,1,2,3)\) as encoding section introduced;
For each solution \(x\left(\overline{t_{0} t_{1} \ldots t_{N} \ldots t_{L}}\right)\) in AS
For tasks in each cluster \(i\)
    \(\operatorname{avgA}(i)\left.=\sum_{j \in i} A I_{j} / \mid\right) \operatorname{cluster}_{i} \mid\)
End
Sort task clusters \(i\) in ascending order of \(\operatorname{avgA}(i) ; g=0 ; k=0\)
While \(g<L S\)
    \(k:=\operatorname{argmin}_{i} \operatorname{avgA}(i) t i)\) (for \(i\) has not been considered); \(t_{k}:=\) the
    tier assignment of \(k\)
    For \(S\) in \(T s c\)
        \(g^{++} ; t_{k}:=S\); Evaluate the new solution \(x^{\prime}\left(\overline{t_{0} t_{1} \ldots S \ldots t_{L}}\right)\) with HEFT;
        If \(x^{\prime} \succ x\) : Update AS with \(x^{\prime} ; x:=x^{\prime}\);
        Else If \(x \succ x^{\prime}\) : break;
        Else
            If \(\operatorname{rand}(0,1)<0.5\)
                Update AS with \(x^{\prime} ; x:=x^{\prime}\);
            End
        End
    End
    \(k\) has been considered;
End
End
```

Complexity analysis
The time complexity is analysed according to the flowchart in Fig. 6, and listed as follows:
(1) Fuzzy pre-partition operator: $O(n)$;
(2) Initialization operator: the time complexity is bounded by a constant.
(3) Evaluation of EDA (total $G$ generations):

Solution evaluation: HEFT has an $O\left(n \cdot M_{\mathrm{p}, \mathrm{c}} \cdot m\right)$ time complexity for $m$ processors, and $M_{\mathrm{p}, \mathrm{c}}$ denotes the max parents or children number. For each generation, time complexity is $O(n$. $\left.M_{\mathrm{p}, \mathrm{c}} \cdot m \cdot N\right)$.

Local intensification: $L S$ denotes the step length for each individual in AS. The total computation complexity can be calculated as $O\left(\mid A S \mid \cdot n \cdot M_{\mathrm{p}, \mathrm{c}} \cdot m \cdot L S\right)$. It is ruled that $|A S| \leq N$, then the complexity is transferred to $O\left(n \cdot M_{\mathrm{p}, \mathrm{c}} \cdot m \cdot N \cdot L S\right)$.

Probability model and AS updating: probability model updating is bounded by constant. For AS updating, suppose $|A S|=$ $N$, then the number of comparison between the solutions is $N^{2}$.

In conclusion, the time complexity is estimated as $O\left(\max \left(n\right.\right.$. $\left.M_{\mathrm{p}, \mathrm{c}} \cdot m \cdot N \cdot L S, N^{2}\right) \cdot G$ ).
The space complexity of our algorithm can be analysed as follows. Each solution needs an array of length $L$ to store its fuzzy rule and an array of length $n$ to store its corresponding tier assignment for the local intensification. For the probability model, a 4 L matrix is needed. To store the Pareto solutions, the scale of AS is up to $N$. Thus, the space complexity of our proposed algorithm is estimated as $O((n+L) \cdot N)$.

## 5. Simulation

To evaluate the performance of our proposed algorithm, we compare it with the selected algorithms, HEFT [27] and two novel multi-objective intelligent optimization algorithms: MOEA/D [35] and FDHEFT [25]. For fair comparison, the algorithms are all coded in $\mathrm{C}++$ and run on the same processor.

### 5.1. Comparison algorithms

HEFT is a popular heuristic algorithm to optimize workflow scheduling problems. As HEFT is a single objective scheduling algorithm, which produces a single solution once, the solution produced by HEFT is adopted as a baseline to evaluate the performance of AS produced by our EDA.

On the other hand, multi-objective evolutionary algorithm based on decomposition (MOEA/D) is chosen as it is a state-of-the-art multi-objective evolutionary algorithm. The multiobjective problem is converted into a number of single-objective sub-problems by using a decomposition approach [36]. FDHEFT is an algorithm tailored to solve multi-objective workflow scheduling problem with fuzzy logic method. It outperformed $\varepsilon$-fuzzy particle swarm optimization algorithm [37], multi-objective HEFT [38], and strength Pareto evaluation algorithm [39]. In this work, we modified the objectives of the algorithm to optimize agreement index and ROB and adopted it as a comparison algorithm.

### 5.2. Parameter settings

The system variables are set in advance as it is known before the scheduling. The detailed environment settings can be referred to [26]. In addition, to measure the impact of data transfer latency on computing performance, communication to computation ratio (CCR) is used in the simulation experiments. It is calculated as average communication time divided by average computation time.

Five parameters are considered in our experiments, which are the population size $(N)$, corresponding learning rate $(\alpha)$, and stopping criterion related parameter and the steps of local search operator (LS). To compare the algorithms fairly, the stopping criterion, e.g. the running time, set as $n / 10$ (s), where $n$ denotes the number of tasks. $L S$ is set by experience, which is proportional to the length of encoding string.

Population size $(N)$ and learning rate $(\alpha)$ are selected by the Taguchi method of the design-of-experiment method (DOE) [40], which is a statistical method and it is used to investigate how the change of parameters affects the performance of the proposed algorithm. Orthogonal arrays of four-parameter levels are

Table 3
Factor levels of parameters.
![img-8.jpeg](img-8.jpeg)

Fig. 10. Main effect plot.
employed as shown in Table 3, and $4^{2}$ full-factorial experiments are employed.

For each combination of Loose $\times C C R(3 \times 4=12)$, a random instance is produced, where Loose is due time related parameter. Under each pair of (Loose, CCR), 16 combinations of $(N, \alpha)$ are set as parameters independently and the obtained $\mathrm{AS}_{i j}(c i=1,2$, ..., 16) are stored. The final AS (FAS) are obtained by integrating $\mathrm{AS}_{1}, \mathrm{AS}_{2}, \ldots, \mathrm{AS}_{16}$. Then, the contribution of a certain combination (CON) is carried out, where $\operatorname{CON}(c i)=\left|A S_{i j}^{\prime}\right| /|F E|$ and $A S_{i j}^{\prime}=$ $\left\{X_{l} \in A S_{i j} \mid \exists X_{l^{\prime}} \in F A S, X_{l}=X_{l^{\prime}}\right\}$. The average CON of each combination is used as the response value (RV) and the main effect plot is generated as Fig. 10.

From Table 4 and Fig. 10, it can be seen it is better for $N$ to be set neither too big nor too small. Thus, $N=30$ and $\alpha=0.05$ are suggested as the parameters in the simulation experiments under the certain stopping criterion.

Table 4
The RV value.
Note: "RV" indicates the response value considered in design of experiment.

Table 5
Simulation settings.
### 5.3. Randomly generated application graphs

A pseudorandom task graph generator TGFF [41] is used to produce randomly generated DAGs. The DAG structure and computation workload for each task is determined by TGFF and for the transfer data size of each task, it is produced according to the normal distribution of a certain CCR. The maximum number of successors and processors of a certain task are both set as 10. After the DAG is achieved, the crisp task processing time and communication data size is transferred into triangle fuzzy number as (22).
$\bar{X}=(0.9 X, X, 1.1 X)$
The crisp due time of task is set by (23):
$d d l(i)=t l v l(i) /$ Loose
where $t l v l(i)$ is the largest sum of processing time of the task path from the entry task to task i. Loose controls the due dates where a larger Loose leads to tight due times. Fuzzy due times is achieved as follows:
$d d l_{1}(i)=d d l(i)$,
$d d l_{2}(i)=d d l(i) \times(1+\operatorname{rand}(0,1))$
Specific parameters of our simulation settings are listed in Table 5. For each level of CCR and Loose, 50 DAGs are produced randomly, $50 \times 4 \times 3=600$ instances are thus used to validate the efficiency of the proposed algorithm.

## Effects of task partition operator

As our algorithm produces the fuzzy "cluster-tier" allocation rule and the tasks are assigned to specific tiers rather than scheduled within the whole system. To verify the efficiency of the partition operator, we compare the results produced by our proposed algorithm with HEFT solutions. The comparison results are listed in Table 6 where the average value of 600 instances under each situation is calculated and HEFT solution is compared AS produced by our algorithm.

The column "dominating HEFT (\%)" denotes the percentage of the instances in which HEFT solution is dominated by any solution in our AS. Similarly, "equals to HEFT (\%)" denotes our AS contains only one solution and it equals to the HEFT solution,

Table 6
Results compared with HEFT heuristic method.

Table 7
C metrics results compared with multi-objective algorithms.

"non-dominating HEFT (\%)" denotes HEFT solution and AS solutions are non-dominated and "dominated by HEFT(\%)" denotes that at least one of our AS is dominated by HEFT solution.

The results show that a large proportion of HEFT solutions is dominated by our AS. For different CCR, it can be seen that when CCR is 0.1 , the proportion of instances where EDA dominates the HEFT solution is around $70 \%$. As CCR increases, the proportion of EDA dominating HEFT solution increases to $100 \%$. Our algorithm performs better for applications with heavy communication overhead and the possible reason is that the fuzzy partition improves the robustness of HEFT. When CCR is large, the communication latency between different processors and tiers increases, the pre task partition according to their corresponding characteristics plays an important role. In addition, under the same CCR, when the due time turns earlier, more HEFT solutions are dominated by our AS and the proportion of solutions dominated by HEFT solution decreases. The main reason is that when due time is loose, many tasks can be finished before its due time and its $A I$ value turns to be 1.0 and the domination relationship depends on the robustness index. When the due time turns tight, our algorithm is more efficient on $A I$ objective, so most HEFT solutions are dominated.

## Comparison with multi-objective algorithms

We compared our algorithm with the novel MOEA/D in terms of $C$ metrics. The average $C$ metric values of 600 instances under different situations are summarized in Table 7. Fuzzy EDA (fEDA), MOEA/D and FOHEFT refer to our proposed algorithm and these two comparison algorithms correspondingly.

From Table 6, it shows that $C$ (fEDA, MOEA/D) is much larger than $C$ (MOEA/D, fEDA), which means most MOEA/D solutions are
dominated by ours. This reveals that, fEDA is good at learning the "cluster-tier" allocation rule and the tailored knowledge driven local search operator is more efficient than genetic operators on this specific problem. Compared with FDHEFT, it can be seen that our solutions dominate FDHEFT solutions on this problem.

In addition, $I G D$ is used as a metric to evaluate the performance of algorithms as a supplement to $C$ metrics. As mentioned before, a small IGD means denotes a good multi-objective solution. Compared to MOEA/D and FOHEFT, it can be seen that solutions produced by fEDA performs better on both $A I$ and robustness according to $I G D$ values presented in Table 8.

### 5.4. Dags from real world problems

Besides the random produced DAGs, we consider two kinds of application DAGs from real world problems: Gauss elimination algorithm [42] and FFT [43] (Fast Fourier Transformation). The task number of Gauss elimination algorithm program is related to the matrix size (b) and equals to $\left(b^{2}+b-2\right) / 2$. The task number of FFT can be calculated as $\left(2 b-1+\operatorname{blog}_{2} b\right)$, where $b$ denotes the size of array and $b=2^{k}$. It is referred to [27] for more details.

For Gauss Elimination application, 10 different scales of DAGs are produced ( $b=10-19$ ). For FFT application, 5 different scales of DAGs are produced ( $k=3-7$ ). For each scale of DAG, CCR and Loose combinations in Table 5 are used to generate different cases. In this way, $10 \times 4 \times 3=120$ and $5 \times 4 \times 3=60$ instances are produced as a benchmark set respectively. Here, $I G D$ values are calculated and presented as follows. The plots show how the average IGD value varies in accordance $n$, CCR and Loose.

For Gaussian Elimination Application results presented in Fig. 11, it can be seen that fEDA performs much better on IGD

![img-9.jpeg](img-9.jpeg)
(b) 'IGD-Loose' histogram

Fig. 11. Variable dependent IGD value plots of Gaussian Elimination Application.

Table 8
IGD values compared with multi-objective algorithms.

values compared with MOEA/D and FDHEFT. As the task number increases from 50 to 200, IGD values of fEDA equals to 0.0 under most situations, which means that the solutions produced by fEDA accounts for a large proportion of the general Pareto front. From Fig. 11(b) and (c), it can be seen that under different kinds of due time constraints and CCR, fEDA provides a better performance compared with the other algorithms.

Fore FFT applications, there are more precedence constraints within the DAGs compared with Gaussian elimination application, which imposes more difficulty on scheduling and resource
allocation. As presented in Fig. 11, it can be seen that fEDA performs much better. As the task number increases from 40 to 1200, IGD values of fEDA equals to 0 except for the smallest-scale instance. When $n=40, I G D=(0.03,0.92,7.47)$, which denotes that when the problem scale is small, the performance gap is not obvious. As $n$ increases, the gap turns larger, which shows that our algorithm is effective as data scale increases. From Fig. 11(b) and (c), our algorithm performs better as the due time constraints are moderate and CCR is large.

There are more precedence constraints within the DAG of FFT Applications compared with Gaussian Elimination Application. This imposes more difficulty on scheduling and resource allocation. As presented in Fig. 12, it can be seen that fEDA performs much better on $I G D$ values. As the task number increases from 40 to 1200, IGD values of fEDA equals to 0 except for the smallestscale instance. When $n=40, I G D=(0.03,0.92,7.47)$, which denotes that when the problem scale is small, the performance gap is not obvious. As $n$ increases, the gap turns to be larger, which shows that our algorithm is effective as data scale increases. From Fig. 12(b) and (c), our algorithm performs better as the deadline constraints are not very tight and $C C R$ is large.

## 6. Conclusions

In this work, an evolutionary algorithm guided fuzzy rule partition method is proposed to solve the uncertain computation offloading problem in loT-fog-cloud system. The main contributions are listed as follows:

1. A detailed system, application and mathematic models are given to formally formulate the problem. Fuzzy number is

![img-10.jpeg](img-10.jpeg)
(a) $I G D-n^{\prime}$ plot
![img-11.jpeg](img-11.jpeg)

Fig. 12. Variable dependent IGD value plots of FFT Application.
adopted to model the uncertain characteristic of workloads and transfer data.
2. A fuzzy logic based partition method is introduced to cluster and assign different types of tasks of the application to different tiers. Based on this algorithm, an optimal DAG task offloading scheme is achieved. Tasks are offloaded to specific tier and a large amount of computation and scheduling capability is saved.
3. Knowledge based local search operators are introduced to efficiently improve the performance of the fuzzy logic based partition method.

Finally, simulation experiments conducted on different due date constraints and CCR cases show that our algorithm performs well on both agreement index and robustness objectives.

In the future, we plan to combine the offline training and online model due to the time complexity of our proposed algorithm is relatively high. In this way, the algorithm could be expanded to solve large scale and online problems in a timely manner. In addition, a prototype system will be built to validate our design.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This research is supported by the National Natural Science Fund for Distinguished Young Scholars of China [No. 61525304] and the National Natural Science Foundation of China [No. 61873328].
