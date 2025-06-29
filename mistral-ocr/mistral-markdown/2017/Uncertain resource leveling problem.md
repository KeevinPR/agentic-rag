# Uncertain resource leveling problem 

Hua Ke and Chenkai Zhao*<br>School of Economics and Management, Tongji University, Shanghai, China


#### Abstract

Resource leveling problem is to make a schedule for the minimization of resource fluctuation subject to precedence constraint and other specific constraints. When indeterminacies come into play, the leveled baseline schedule obtained by solving deterministic resource leveling problem can hardly be executed as planned and this schedule may even become infeasible. In this paper, on the basis of uncertainty theory, we consider an uncertain resource leveling problem in which activity durations are estimated by experts. In order to deal with these estimations, three uncertainty-theory-based project scheduling models are proposed and we utilize revised estimation of distribution algorithms to search quasi-optimal schedules. Numerical experiments are also provided to illustrate the effectiveness of the algorithms.


Keywords: Project scheduling, uncertainty theory, resource leveling, estimation of distribution algorithm

## 1. Introduction

Project scheduling is concerned with the temporal coordination of various tasks of a project, such as minimal project makespan, minimal fluctuations in resource utilization, etc [13]. Project scheduling problem can be divided into many subproblems, including resource-constrained project scheduling problem (RCPSP), resource leveling problem (RLP) and time-cost trade-off problem (TCTP). As a basic project scheduling problem, RLP is to meet the physical limits of construction resources, avoid day-to-day fluctuations in resource demand, and maintain an even flow of application for construction resources over the project horizon [35]. Resource leveling is motivated by the fact that some expensive resources need to be used as evenly as possible to reduce the financial burden or risks. This is because large fluctuations in resource requirements can be quite expensive on account of ineffectiveness of resources arrangement. Resources such as machineries with high cost for start-up and shut-down need to be used evenly and resources such as workers need to

[^0]be arranged smoothly to reduce idleness of manpower. To describe the resource fluctuation, different objective functions like absolute deviation from the average daily resource usage and variance of daily resource usage have been employed. In this paper, we consider a situation that daily resource supplies are predetermined before the start of a project. As an example, construction machineries invariably need to be fixed on the site before the start of a project, which means daily cost and daily capacity supply are both predetermined. Under these circumstances, the cost of resource fluctuations is due to the idle resources during project execution.

In early phase, researches were done with the assumptions of complete information and deterministic environment. The classical deterministic RLP aims at minimizing the fluctuations in resource utilization by constructing a project baseline schedule that specifies the planned activity starting times while satisfying both the precedence constraint and the project deadline constraint [5, 8]. The deterministic RLP has been extensively studied and numerous exact and heuristic methods have been proposed to solve it $[3,12,19,36]$. However, during execution it would be very rare that the project is not disrupted by unexpected events. Feasible sources of these events may be a shortage of machineries, a delayed delivery


[^0]:    *Corresponding author. Chenkai Zhao, School of Economics and Management, Tongji University, Shanghai 200092, China. Tel.: +86 18817598428; E-mail: 5zck@tongji.edu.cn.

of materials, absence of workers, and so on. In such a case, a baseline schedule may not contain enough information to guide the execution of a project. Thus, it is indispensable to consider indeterminate factors when solving RLP.

Researches into RLP under activity duration indeterminacies are limited. In project scheduling, there are mainly three ways to deal with activity duration indeterminacies: robust project scheduling, fuzzy project scheduling and stochastic project scheduling. Robust project scheduling combines a proactive strategy to generate a protected deterministic baseline schedule with a reactive strategy to repair the disrupted schedule caused by unexpected events during schedule execution [7, 20]. In fuzzy set theory, the decision can be estimated by experts based on their experiences and professional judgments [2, 33, 37]. However, fuzzy set theory may lead to counterintuitive results [26]. Unlike robust project scheduling and fuzzy project scheduling, stochastic project scheduling in RLP uses a so-called scheduling policy to guide the execution of the project. Generally, stochastic RLP (SRLP) aims at minimizing the fluctuations in resource utilization by taking a limited set of decisions during project execution [21].

In SRLP, activity durations are represented by random variables. The assumption is reasonable when there are enough historical data to precisely estimate variables' probability distributions. However, in project, it is arduous to get enough historical data for activities seldom or never executed. This situation is shared with the consideration of the uniqueness of projects. In this case, belief degrees given by experienced project managers or experts can be employed to estimate distributions of activity durations. Uncertainty theory, initiated by Liu [26], was founded to rationally deal with belief degrees, which inspired a new method of describing indeterministic phenomena. Uncertainty theory is a branch of axiomatic mathematics for modeling human uncertainty, which has been deeply developed in many fields, such as uncertain process [27], uncertain programming [25] and uncertain differential equation [27, 43]. For now, the new theory has been successfully applied to varieties of fields, such as game theory [10, 11, 40], stock problem [4], production control problem [17, 31], shortest path problem [42], etc. Ke et al. [16] researched project scheduling problem in the environment with uncertainty and randomness. For more details about uncertain project scheduling problem, readers may refer to $[14,15,39,41]$.

As far as we know, few researches pour attention into project scheduling problem with uncertain activity durations as well as resource leveling. In this paper, we build three uncertain models for solving uncertain resource leveling problem (URLP). Moreover, an intelligent algorithm called estimation of distribution algorithm (EDA) is utilized in this paper. In project scheduling problem, EDAs have been applied in multi-mode RCPSP and stochastic RCPSP [9, 38].

The remainder of this paper is as follows: Section 2 describes URLP in detail and proposes corresponding uncertain models to minimize resource fluctuation cost according to the demand of project managers. To solve these models, revised EDAs are designed in Section 3. Section 4 conducts some numerical experiments. Finally, conclusions are drawn in Section 5. Specially, some basic concepts in uncertainty theory are introduced in Appendix.

## 2. Formulations and models

### 2.1. Problem description

A project containing $n$ activities can be described by an activity-on-the-node network $G(N, A)$. The set of nodes $N=\{1,2, \cdots, n+2\}$ represents activities, and the set of arcs $A$ denotes finish-start, zero-lag precedence relations between activities. Activities 1 and $n+2$ don't consume time and resource, and only signify project starting point and finishing point, respectively. Specially, durations of all activities in URLP are represented by an uncertain vector $\boldsymbol{d}=\{0, \tilde{d}_{2}, \cdots, \tilde{d}_{n+1}, 0\}$ and the starting times of all activities are denoted as a vector $\boldsymbol{s}=\left\{0, \tilde{s}_{2}(\pi, \boldsymbol{d}), \cdots, \tilde{s}_{n+1}(\pi, \boldsymbol{d}), \tilde{s}_{n+2}(\pi, \boldsymbol{d})\right\}$. In this paper, we additionally take a due date $\delta$ into consideration. Moreover, there are totally $K$ types of renewable resources and each of them has a constant availability $a_{k}, k=1,2, \cdots, K$. In addition, the resource usage for resource type $k$ during period $t$ is denoted as $\tilde{u}_{k t}$. Every resource type $k$ has a weight $c_{k}$ that denotes the penalty cost per unit of resource type $k . r_{i k}$ denotes the daily consumption of resource type $k$ during the $i$ th activity execution. And $\tilde{R} f$ indicates the cost caused by resource fluctuation over the project horizon.

The URLP aims at minimizing resource fluctuation cost of a whole project with uncertain activity durations meanwhile satisfying the deadline constraint. Solving URLP is a dynamic decision process.

A decision maker decides to start which feasible activity at each decision point, including project starting time and activity finishing times. In the decision process, a decision maker can only utilize partial information which appears before his decision point.

Since activity durations are assumed to be uncertain variables, the finishing time of each activity is an uncertain variable as well. With a given activity list $\pi$, an executing order of activities, the completion time of activity $i$ can be calculated as follows:

$$
\tilde{f}_{i}(\pi, \boldsymbol{d})=\tilde{s}_{i}(\pi, \boldsymbol{d})+\tilde{d}_{i}
$$

Without resource constraint, the starting time of activity $i$ can be computed considering precedence relationship as follows:

$$
\tilde{s}_{i}(\pi, \boldsymbol{d})=\max _{(j, i) \in A} \tilde{f}_{j}(\pi, \boldsymbol{d})
$$

When resource constraint is considered, however, this formula is not invariably valid. Some activity may be feasible in precedence relationship logic if all of its predecessors have been finished while simultaneously infeasible for lack of available resources. In other words, an activity has predecessors in both precedence relation logic and resource logic. To produce feasible schedule effectively, resource flow network was presented by Artigues and Roubellat [1]. If there is a resource flow, extra relation is added into the original network between activities without precedence relationship. Thus an extended precedence relationship set $A^{*}$ is developed. Combined with the side constraint proposed by Ma et al. [32], the starting time of activity $i$ can be calculated by

$$
\tilde{s}_{i}(\pi, \boldsymbol{d})=\max _{\pi_{m}<\pi_{i}} \tilde{s}_{m}(\pi, \boldsymbol{d}) \vee \max _{(j, i) \in A^{*}} \tilde{f}_{j}(\pi, \boldsymbol{d})
$$

where $\pi_{i}$ is the position of activity $i$ in activity list $\pi$.
Therefore, $\tilde{s}_{n+2}(\pi, \boldsymbol{d})$ is strictly increasing with respect to $\boldsymbol{d}$. Then referring to Definition 4, we have

Theorem 1. Provided that the duration of activity $i$ has a regular distribution $\Phi_{i}(x)$ and an inverse uncertainty distribution $\Phi_{i}^{-1}(\beta)$, and $\tilde{s}_{i}(\pi, \boldsymbol{d})$ has an inverse uncertainty distribution $\Psi_{i}^{-1}(\pi, \beta)$, we can get a realized makespan with belief degree $\beta$ as follows:

$$
\begin{aligned}
& \Psi_{n+2}^{-1}(\pi, \beta)=\max _{\pi_{m}<\pi_{n+2}} \Psi_{m}^{-1}(\pi, \beta) \\
& \quad \vee \max _{(j, n+2) \in A^{*}}\left(\Psi_{j}^{-1}(\pi, \beta)+\Phi_{j}^{-1}(\beta)\right)
\end{aligned}
$$

Since $\tilde{R} f(\pi, \boldsymbol{d})$ is dependent on the starting times of activities and the activity durations are uncertain
variables, $\tilde{R} f(\pi, \boldsymbol{d})$ also becomes uncertain. Then the resource fluctuation cost can be calculated as follows:

$$
\tilde{R} f(\pi, \boldsymbol{d})=\sum_{k=1}^{K} c_{k} \sum_{t=0}^{\tilde{s}_{n+2}(\pi, \boldsymbol{d})}\left(a_{k}-\tilde{u}_{k t}\right)
$$

or

$$
\tilde{R} f(\pi, \boldsymbol{d})=\sum_{k=1}^{K} c_{k}\left(a_{k} \tilde{s}_{n+2}(\pi, \boldsymbol{d})-\sum_{i=2}^{n+1} r_{i k} \tilde{d}_{i}\right)
$$

### 2.2. Chance-constrained model

The chance-constrained model aims to minimize resource fluctuation cost by applying chanceconstrained programming [6]. For risk-averse decision makers, this model can realize the minimization of resource fluctuation cost with a relatively high belief degree. The model is proposed as follows:

$$
\left\{\begin{array}{l}
\min \overline{R f} \\
\text { subject to: } \\
M\left\{\sum_{k=1}^{K} c_{k}\left(a_{k} \tilde{s}_{n+2}(\pi, \boldsymbol{d})-\sum_{i=2}^{n+1} r_{i k} \tilde{d}_{i}\right)\right. \\
\leq \overline{R f}\} \geq \alpha \\
M\left\{\tilde{s}_{n+2}(\pi, \boldsymbol{d}) \leq \delta\right\} \geq \beta
\end{array}\right.
$$

where $\alpha, \beta$ are belief degrees.

### 2.3. Expected value model

The expected value model is widely used for solving various types of practical problems. In practice, decision makers may desire to make decisions with the minimum expected resource fluctuation cost under the expected makespan constraint for the project. In order to satisfy this type of demand, in URLP, we can build an expected value model as follows:

$$
\left\{\begin{array}{l}
\min E\left[\sum_{k=1}^{K} c_{k}\left(a_{k} \tilde{s}_{n+2}(\pi, \boldsymbol{d})-\sum_{i=2}^{n+1} r_{i k} \tilde{d}_{i}\right)\right] \\
\text { subject to: } \\
E\left[\tilde{s}_{n+2}(\pi, \boldsymbol{d})\right] \leq \delta
\end{array}\right.
$$

### 2.4. Chance maximization model

Dependent-chance programming (DCP) initiated by Liu [22] is to optimize the chance of a certain event. Readers who are interested in DCP may refer to Liu and Iwamura [30] and Liu [23-25]. In this paper, the goal is given in advance as that the belief

degree of $R f$ underrunning the goal should be as large as possible. The constraint is that the belief degree of finishing the project before the due date should be larger than or equal to a predetermined confidence level $\beta$. Hence, we can build the following chance maximization model:

$$
\left\{\begin{array}{l}
\max M\left\{\sum_{k=1}^{K} c_{k}\left(a_{k} \bar{s}_{n+2}(\pi, \boldsymbol{d})\right.\right. \\
\left.\left.-\sum_{i=2}^{n+1} r_{i k} \bar{d}_{i}\right) \leq \overline{R f}\right\} \\
\text { subject to: } \\
M\left\{\bar{s}_{n+2}(\pi, \boldsymbol{d}) \leq \delta\right\} \geq \beta
\end{array}\right.
$$

where $\beta$ is a belief degree and $\overline{R f}$ is an acceptable resource fluctuation cost.

## 3. Revised EDA

Since deterministic RLP is NP-hard [34], URLP, an extension of RLP, needs to be solved by heuristic or meta-heuristic algorithm. In this section, a revised intelligent heuristic algorithm is designed by applying corresponding uncertain serial schedule generation scheme (US-SGS) to EDA.

### 3.1. Revised uncertain serial schedule generation scheme

As discussed by Kolish and Hartmann [18], there are several types of feasible solution representations for project scheduling. For URLP in this paper, we choose the solution representation activity list $\pi$, which represents the executing order of activities. The US-SGS can be described as follows:

0 : Given a network $G(N, A) . \pi:=$ activity list; $\boldsymbol{d}:=$ duration time; $\boldsymbol{W}:=$ underway activity set; $\boldsymbol{U}:=$ unscheduled activity set; $\boldsymbol{s}:=$ starting time; $\boldsymbol{F}:=$ finishing time; $T:=$ time point; $n:=$ number of activities; $u:=$ resource usage during activity durations; $R f:=$ resource fluctuation cost.

1: $\boldsymbol{W}=\varnothing, \boldsymbol{U}=[1,2, \cdots, n+2]$,
$\boldsymbol{F}=[$ in $f$, inf, $\cdots$, inf $], \boldsymbol{s}=[0,0, \cdots, 0]$,
$\boldsymbol{d}=\left(0, \bar{d}_{2}, \bar{d}_{3}, \cdots, \bar{d}_{n+1}, 0\right)$
2: $\operatorname{im}=1, T=0$
3: While is empty $(U)=0$
4: $\quad s_{\pi_{i m}}=\max _{i<i m} s_{\pi_{i}} \vee \max _{\left(j, \pi_{i m}\right) \in A} F_{j}$
5: $\quad$ if $\sum_{i \in W} r_{i k}+r_{i m k} \leq a_{k}, k=1,2 \cdots K$
$\& s_{\pi_{i m}} \leq T$
6: $\quad F_{\pi_{i m}}=T+d_{\pi_{i m}}$
7: $\quad u_{k, \pi_{i m}}=r_{i m k} d_{\pi_{i m}}, k=1,2 \cdots K$
8: $\quad$ Put $\pi_{i m}$ into $\boldsymbol{W}$
9: $\quad i m=i m+1$
10: else
11: $\quad T=\min _{i \in \boldsymbol{W}}\left(F_{i}\right)$
12: $\quad$ Take out $i$ from $\boldsymbol{W}$ and $\boldsymbol{U}$ if: $F_{i} \leq T, i \in \boldsymbol{W}$
13: end
14: end
15: Return $s_{n+2}$,
Return $R f=\sum_{k=1}^{K} c_{k}\left(a_{k} s_{n+2}-\sum_{i m=0}^{n+1} u_{k, \pi_{i m}}\right)$.
3.1.1. Chance-constrained model

Referring to Axiom 4, we can possess:

$$
M\left\{\Omega_{R f}\right\}=\bigwedge_{k=2}^{n+1} M\left\{\Omega_{d_{k}}\right\}=M\left\{\Omega_{d_{k^{*}}}\right\}
$$

where $\Omega$ is called an event, $M\left\{\Omega_{R f}\right\}$ denotes the belief degree of the realized resource fluctuation cost, $M\left\{\Omega_{d_{k}}\right\}$ denotes the belief degree of the $k$ th realized activity duration and $d_{k^{*}}$ denotes the $k^{*}$ th realized activity duration which has the smallest belief degree.

Then the resource fluctuation cost with belief degree $\alpha$ can be calculated via uncertain simulations as follows:

1: Generate $\omega_{1}, \omega_{2}, \ldots, \omega_{N}$ according to uncertainty distribution functions, where $N$ is a sufficiently large number.

2: For each $\omega_{k}$, compute the function value $R f_{k}$ and the belief degree $M\left\{\Omega_{R f_{k}}\right\}$.

3: Build a set of $R f$ where $M\left\{\Omega_{R f}\right\} \geq \alpha$.
4: Return the smallest $R f$ among the above set.
It is worth mentioning that a realized makespan with confidence level $\beta$ must be subject to the due date constraint and if not, the corresponding activity list has to be abandoned.

### 3.1.2. Expected value model

The expected resource fluctuation cost and the expected makespan can be calculated via uncertain simulations as follows:

1: Set $U_{1}=0, U_{2}=0$.
2: Generate $\boldsymbol{\omega}=\left(0, d_{2}, d_{1}, \ldots, d_{n+1}, 0\right)$ according to different uncertainty distribution functions.

3: $U_{1}=U_{1}+R f, U_{2}=U_{2}+s_{n+2}$.
4: Repeat the second and third steps for $N$ times, where $N$ is a sufficiently large number.

5: $U_{1}=U_{1} / N, U_{2}=U_{2} / N$.

Note that an expected makespan must be subject to the due date constraint and if not, the corresponding activity list has to be abandoned.

### 3.1.3. Chance maximization model

According to uncertainty theory, the belief degree of $R f \leq \overline{R f}$ can be calculated via uncertain simulations as follows:

1: Generate $\omega_{1}, \omega_{2}, \ldots, \omega_{N}$ according to uncertainty distribution functions, where $N$ is a sufficiently large number.

2: For each $\omega_{k}$, compute the function value $R f_{k}$ and the belief degree $M\left\{\Omega_{R f_{k}}\right\}$.

3: Bulid a set of $M\left\{\Omega_{R f}\right\}$ where $R f \leq \overline{R f}$.
4: Return the largest $M\left\{\Omega_{R f}\right\}$ among the above set.

Also, the realized makespan with confidence level $\beta$ must be subject to the due date constraint and if not, the corresponding activity list has to be abandoned.

### 3.2. Revised EDA

In this section the US-SGS is embed into EDA. By this step, we employ the US-SGS to decode the activity lists and approximate the fitness of each solution by uncertain simulations. In contrast to genetic algorithm, EDA does not directly generate new solutions by crossover and mutation but by sampling from a probability distribution. The latter depicts the features of a selected set of feasible solutions of the problem. The outline of EDA is presented in Fig. 1.

In this paper, to revise the EDA, here are the steps: First, $N$ solutions are generated according to the initial probability matrix as the initial population and the probability matrix is updated according to the initial population. Each solution is an activity list, where one activity can only be assigned if all of its predecessors have been finished. Second, the US-SGS is utilized to generate schedules according to activity lists, filter infeasible solutions when realized makespan exceeds deadline and evaluate each solution. After evaluating the population, $P<N$ best individuals are selected from the population to form the elite set. And the elite set is chosen to update the probability matrix. Then the new probability matrix is employed to sample population of the next generation. After a certain number of generations, the solution with best fitness value is reported as quasi-optimal solution.
![img-0.jpeg](img-0.jpeg)

Fig. 1. The outline of EDA.

## 4. Numerical experiments

A project with 30 activities and 4 renewable resources is taken as an example in this section. A slice of specific information about the project is manifested in Table 1, including activity durations, resource requirements and successors. All the activity durations are assumed to be uncertain variables and described by uncertainty distributions estimated by experts.

Accordingly, the project structure is depicted in Fig. 2.

### 4.1. Chance-constrained model

Supposed that the belief degree $\alpha$ is 0.9 while the confidence level $\beta$ is 0.85 . The chance-constrained model can be written as:

$$
\left\{\begin{array}{l}
\min \overline{R f} \\
\text { subject to: } \\
M\left\{\sum_{k=1}^{4} c_{k}\left(a_{k} s_{32}-\sum_{i=2}^{31} r_{i k} \bar{d}_{i}\right) \leq \overline{R f}\right\} \geq 0.9 \\
M\left\{s_{32} \leq 120\right\} \geq 0.85
\end{array}\right.
$$

Table 1
Project information

| Activity | Duration | $R_{1}$ | $R_{2}$ | $R_{3}$ | $R_{4}$ | Successors |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 0 | 0 | 0 | 0 | 0 | $2,3,4$ |
| 2 | $Z(5,7,8)$ | 4 | 0 | 0 | 7 | $6,11,15$ |
| 3 | $Z(7,9,10)$ | 10 | 0 | 0 | 0 | $7,8,13$ |
| 4 | $L(1,3)$ | 5 | 0 | 0 | 0 | $5,9,10$ |
| 5 | $Z(1,3,4)$ | 9 | 5 | 0 | 0 | 20 |
| 6 | $L(8,10)$ | 4 | 4 | 7 | 9 | 30 |
| 7 | $Z(7,8,10)$ | 9 | 3 | 0 | 5 | 27 |
| 8 | $Z(1,3,4)$ | 0 | 0 | 8 | 0 | $12,19,27$ |
| 9 | $L(1,3)$ | 1 | 2 | 0 | 0 | 14 |
| 10 | $Z(8,10,11)$ | 9 | 10 | 0 | 7 | 16, 25 |
| 11 | $L(7,10)$ | 0 | 0 | 0 | 10 | 20, 26 |
| 12 | $Z(8,10,11)$ | 7 | 9 | 10 | 3 | 14 |
| 13 | $Z(1,3,4)$ | 0 | 0 | 0 | 8 | 17, 18 |
| 14 | $L(1,3)$ | 0 | 0 | 4 | 0 | 17 |
| 15 | $Z(3,5,6)$ | 0 | 0 | 10 | 7 | 25 |
| 16 | $L(2,4)$ | 0 | 10 | 0 | 0 | 21, 22 |
| 17 | $L(7,11)$ | 0 | 0 | 4 | 1 | 22 |
| 18 | $Z(6,8,9)$ | 4 | 4 | 0 | 7 | 20, 22 |
| 19 | $Z(2,4,5)$ | 9 | 5 | 0 | 0 | 24, 29 |
| 20 | $Z(7,10,11)$ | 0 | 7 | 10 | 0 | 23, 25 |
| 21 | $L(4,6)$ | 4 | 1 | 0 | 0 | 28 |
| 22 | $Z(2,4,5)$ | 0 | 4 | 0 | 4 | 23 |
| 23 | $L(3,5)$ | 10 | 0 | 7 | 4 | 24 |
| 24 | $Z(3,5,6)$ | 7 | 0 | 8 | 0 | 30 |
| 25 | $L(6,8)$ | 4 | 0 | 3 | 0 | 30 |
| 26 | $Z(4,5,7)$ | 9 | 3 | 9 | 2 | 31 |
| 27 | $L(1,3)$ | 3 | 0 | 5 | 0 | 28 |
| 28 | $Z(2,3,5)$ | 0 | 0 | 6 | 7 | 31 |
| 29 | $Z(1,2,4)$ | 0 | 0 | 0 | 2 | 32 |
| 30 | $Z(5,6,8)$ | 0 | 0 | 5 | 4 | 32 |
| 31 | $Z(4,6,7)$ | 8 | 0 | 0 | 0 | 32 |
| 32 | 0 | 0 | 0 | 0 | 0 |  |

Note: The limits of the four resources are $(19,19,25,14)$, the penalty costs of the four resources are $(3,4,2,5)$ and the deadline is 120 .
![img-1.jpeg](img-1.jpeg)

Fig. 2. The network of the project.

In this paper, the objective value is changeable according to belief degrees $(\alpha, \beta)$. To simplify the problem, we take $(\alpha, \beta)$ the same values $(0.05,0.05)$,
$(0.15,0.15), \ldots,(0.95,0.95)$ and the revised EDA runs 1000 generations with 10 times for 10 groups, respectively. Note that $\alpha$ and $\beta$ can be different

Table 2
The quasi-optimal solutions for chance-constrained model

| $(\alpha, \beta)$ | Quasi-optimal schedule | $R f$ | Makespan |
| :--: | :--: | :--: | :--: |
| $(0.05,0.05)$ | $\begin{aligned} & 1,2,4,9,10,6,11,5,3,8,16,26,7,15,19,13,21,12, \\ & 18,27,29,14,20,28,17,31,25,22,23,24,30,32 \end{aligned}$ | 9464 | 61.662 |
| $(0.15,0.15)$ | $\begin{aligned} & 1,2,3,8,7,6,13,4,5,12,11,10,9,26,18,27,19,14, \\ & 16,21,20,15,29,17,28,22,31,25,23,24,30,32 \end{aligned}$ | 10369 | 66.137 |
| $(0.25,0.25)$ | $\begin{aligned} & 1,4,2,6,3,5,15,10,9,7,13,8,18,11,12,16,19,27, \\ & 14,29,21,26,17,28,20,25,22,31,23,24,30,32 \end{aligned}$ | 11085 | 69.921 |
| $(0.35,0.35)$ | $\begin{aligned} & 1,4,2,5,9,10,15,3,8,11,12,13,26,16,14,6,21,7, \\ & 19,27,29,17,18,28,20,22,25,31,23,24,30,32 \end{aligned}$ | 11500 | 72.471 |
| $(0.45,0.45)$ | $\begin{aligned} & 1,2,11,3,4,6,8,7,10,19,9,5,16,15,12,29,21,13, \\ & 18,14,20,26,17,27,25,28,31,22,23,24,30,32 \end{aligned}$ | 12046 | 75.575 |
| $(0.55,0.55)$ | $\begin{aligned} & 1,2,3,13,8,7,15,4,19,18,9,10,11,5,12,26,27, \\ & 29,6,14,16,21,17,20,28,31,25,22,23,24,30,32 \end{aligned}$ | 12614 | 83.974 |
| $(0.65,0.65)$ | $\begin{aligned} & 1,3,2,4,5,8,7,13,6,18,9,15,10,11,12,16,19,27, \\ & 14,26,20,21,29,17,28,25,31,22,23,24,30,32 \end{aligned}$ | 13247 | 87.351 |
| $(0.75,0.75)$ | $\begin{aligned} & 1,3,2,4,9,8,7,6,11,27,19,12,5,13,10,14,16,15, \\ & 18,17,21,29,26,20,28,31,25,22,23,24,30,32 \end{aligned}$ | 13459 | 88.788 |
| $(0.85,0.85)$ | $\begin{aligned} & 1,2,3,8,7,13,6,11,19,12,4,9,14,27,10,18,15, \\ & 16,29,5,21,26,17,20,28,25,31,22,23,24,30,32 \end{aligned}$ | 13914 | 91.31 |
| $(0.95,0.95)$ | $\begin{aligned} & 1,2,3,6,4,8,7,13,18,5,9,10,15,11,12,19,16,14, \\ & 27,29,20,26,21,17,28,25,31,22,23,24,30,32 \end{aligned}$ | 14269 | 93.639 |

when project managers have different confidence level requirements on makespan plan and resource fluctuation control. In this paper, we emphasize our research on solving the quasi-optimal schedule that we consider the same values for $\alpha$ and $\beta$. Then we list the best solution of all 10 times for each group. The quasi-optimal solutions and $R f \mathrm{~s}$ are provided in Table 2.

The result may be beneficial to risk-averse decision makers from the following three aspects: First, a project manager can arrange the resource utilization
based on a makespan prediction according to given belief degrees; Second, a given belief degree corresponds with an optimal schedule. Third, a higher belief degree corresponds with a larger realized makespan and a larger realized resource fluctuation cost.

### 4.2. Expected value model

Based on the project information, the expected value model can be written as:

Table 3
The quasi-optimal solutions for expected value model

| No. | Quasi-optimal schedule | $E[R f]$ | $E[$ makespan $]$ |
| :--: | :--: | :--: | :--: |
| 1 | $\begin{aligned} & 1,2,3,4,10,9,8,6,7,11,12,16,26,5,14,13,18,21, \\ & 27,19,29,15,17,20,28,22,31,25,23,24,30,32 \end{aligned}$ | 12938 | 79.751 |
| 2 | $\begin{aligned} & 1,4,3,2,10,5,8,6,7,9,11,19,13,29,27,12,16,18, \\ & 14,15,21,20,25,17,28,26,22,31,23,24,30,32 \end{aligned}$ | 12908 | 81.652 |
| 3 | $\begin{aligned} & 1,2,3,4,5,15,7,9,10,8,6,13,18,11,12,16,26,27, \\ & 14,20,21,19,29,17,28,31,25,22,23,24,30,32 \end{aligned}$ | 12555 | 77.456 |
| 4 | $\begin{aligned} & 1,4,10,2,11,9,3,16,13,5,7,8,26,18,19,27,15,12, \\ & 14,20,6,17,21,28,25,29,31,22,23,24,30,32 \end{aligned}$ | 12601 | 78.446 |
| 5 | $\begin{aligned} & 1,2,3,8,4,15,5,11,19,12,13,9,7,6,14,10,18,16, \\ & 21,26,29,17,27,20,28,31,25,22,23,24,30,32 \end{aligned}$ | 13028 | 81.222 |
| 6 | $\begin{aligned} & 1,3,2,13,7,4,15,9,10,5,8,18,11,27,16,12,26,19, \\ & 14,29,6,17,21,20,25,28,22,31,23,24,30,32 \end{aligned}$ | 12874 | 82.536 |
| 7 | $\begin{aligned} & 1,3,2,8,7,4,6,11,9,12,13,5,19,15,18,14,10,17, \\ & 26,16,27,20,29,21,25,28,22,31,23,24,30,32 \end{aligned}$ | 12620 | 80.858 |
| 8 | $\begin{aligned} & 1,4,3,2,5,15,10,6,13,7,9,11,8,19,12,29,27,18, \\ & 26,14,16,17,21,20,28,31,25,22,23,24,30,32 \end{aligned}$ | 12477 | 77.753 |
| 9 | $\begin{aligned} & 1,4,10,9,2,3,8,16,15,11,12,19,13,18,14,6,5,21, \\ & 7,20,27,26,25,17,29,28,31,22,23,24,30,32 \end{aligned}$ | 12722 | 79.744 |
| 10 | $\begin{aligned} & 1,3,4,2,8,11,5,12,10,6,13,9,18,14,20,15,19,7, \\ & 17,16,29,27,21,26,25,28,22,31,23,24,30,32 \end{aligned}$ | 12969 | 80.319 |

Table 4
The effectiveness of the EDA

| Size | The best | The worst | The average | Error |
| :-- | :--: | :--: | :--: | :--: |
| 10 | 12477 | 13028 | 12769 | $4.23 \%$ |

$$
\left\{\begin{array}{l}
\min E\left[\sum _ { k = 1 } ^ { 4 } c _ k ( a _ k s _ 3 _ 2 - \sum _ { i = 2 } ^ { 3 } r _ i k \hat { d } _ i ) } \\
\text { subject to: } \\
E\left[s_{32}\right] \leq 120
\end{array}\right.
$$

The revised EDA runs 10 times with 1000 generations. The quasi-optimal solutions and $R f$ s are provided in Table 3.

According to Table 3, we can get the best $R f$, the worst $R f$, the average $R f$ and we can calculate the error as demonstrated in Table 4. The result indicates that the deviation denoted by percent error does not exceed $5 \%$, which implies the effectiveness of the algorithm integrating uncertain simulations. The result may help risk-neutral project managers arrange the resource utilization. Note that a larger realized makespan does not necessarily correspond with a larger realized resource fluctuation cost.

### 4.3. Chance maximization model

Supposed that the project manager wants to maximize the belief degree at which the resource fluctuation cost $R f$ does not exceed a predetermined acceptable cost 12000 under the constraint that the belief degree of finishing the project before the due date should be larger than or equal to a predetermined confidence level 0.85 . The chance maximization model can be written as:

$$
\left\{\begin{array}{l}
\max M\left\{\sum _ { k = 1 } ^ { 4 } c _ k ( a _ k s _ 3 _ 2 - \sum _ { i = 2 } ^ { 3 } r _ i k \hat { d } _ i ) ~ \leq ~ 1 2 0 0 0 \}}\right. \\
\text { subject to: } \\
\left.\left.M\left[s_{32} \leq 120\right] \geq 0.85 .\right.
\end{array}\right.
$$

In this paper, we test different values for $\overline{R f}$. The revised EDA runs 10 times with 1000 generations for 6 groups, respectively. The quasi-optimal solutions and $R f$ s are demonstrated in Table 5.

According to Table 5, we can compare the results with the chance-constrained model and the two models validate each other. The result may be beneficial to project managers from the following three aspects: First, a project manager can determine a belief degree at which a given resource fluctuation cost value can not be exceeded based on a makespan prediction; Second, a given predetermined resource fluctuation cost value corresponds with an optimal schedule. Therefore, for project managers, it is considerable to set applicable resource fluctuation cost goals and constraint belief degrees to solve this problem. Third, a higher resource fluctuation cost goal corresponds with a higher belief degree.

## 5. Conclusion and future work

In real project, the environment for project execution is full of indeterminacies. Considering the uniqueness of projects, it is shared that some activities are seldom or never executed before. As a result, it is formidable to describe activity durations by probability distributions for lack of historical data. Besides, fuzzy set theory may lead to counterintuitive results. This paper considered RLP with uncertain durations and a deadline constraint. To satisfy the demand of project managers, three uncertain models were built. We utilized a special SGS for our problem called US-SGS and added it into EDA. Furthermore, some numerical experiments were solved with our models and algorithms. We found that a larger realized makespan does not necessarily correspond with a larger realized resource fluctuation cost for uncertain

Table 5
The quasi-optimal solutions for chance maximization model

| $\overline{R f}$ | Quasi-optimal schedule | Belief degree | $R f$ |
| :--: | :--: | :--: | :--: |
| 14500 | 1,3,2,4,10,9,15,7,5,16,6,8,11,27,19,12,29,13, 14,21,26,18,17,20,28,25,31,22,23,24,30,32 | 0.98006 | 14466 |
| 13500 | 1,2,3,4,10,8,16,6,7,11,12,13,9,26,5,27,19,21, 18,15,28,14,20,17,25,31,29,22,23,24,30,32 | 0.75842 | 13465 |
| 12500 | 1,4,3,2,7,9,5,13,8,19,12,11,15,14,10,18,16, 29,26,6,21,27,20,17,28,31,25,22,23,24,30,32 | 0.52032 | 12353 |
| 11500 | 1,2,3,4,8,7,10,9,16,5,15,19,11,12,14,26,6,13, 29,18,21,27,17,20,28,25,31,22,23,24,30,32 | 0.32971 | 11449 |
| 10500 | 1,2,3,4,15,10,9,5,13,16,6,8,7,11,27,19,12,18, 21,26,14,17,20,29,28,31,25,22,23,24,30,32 | 0.15392 | 10464 |
| 9500 | 1,4,10,16,5,3,2,9,13,8,7,18,19,11,12,14,15,21, 26,20,6,17,27,29,25,28,31,22,23,24,30,32 | 0.03074 | 9374 |

resource leveling problem. Moreover, we can consider that a higher belief degree corresponds with a larger realized resource fluctuation cost according to the numerical experiments. We hope our work may provide a new viewpoint of resource leveling for project managers and give them criterion to solve uncertain resource leveling problem. For future work, we believe that it is worthwhile to take into account other objectives such as variance of resource utilization for RLP.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (No.71371141) and the Fundamental Research Funds for the Central Universities.

## Author details

School of Economics and Management, Tongji University, Shanghai 200092, China.

E-mails: hke@tongji.edu.cn; 5zck@tongji.edu.cn.

## References

[1] C. Artigues and F. Roubellat, A polynomial activity insertion algorithm in a multi-resource schedule with cumulative constraints and multiple modes, European Journal of Operational Research 127(2) (2000), 297-316.
[2] O. Atli and C. Kahraman, Resource-constrained project scheduling problem with multiple execution modes and fuzzy/crisp activity durations, Journal of Intelligent \& Fuzzy Systems 26(4) (2014), 2001-2020.
[3] F. Ballestin, C. Schwindt and J. Zimmermann, Resource leveling in make-to-order production: Modeling and heuristic solution method, International Journal of Operations Research 4(1) (2007), 50-62.
[4] R. Bhattacharyya, A. Chatterjee and S. Kar, Uncertainty theory based multiple objective mean-entropy-skewness stock portfolio selection model with transaction costs, Journal of Uncertainty Analysis and Applications 1(1) (2013), Article 16.
[5] A. Burgess and J.B. Killebrew, Variation in activity level on a cyclical arrow diagram, Journal of Industrial Engineering 13(2) (1962), 76-83.
[6] A. Charnes and W.W. Cooper, Chance-constrained programming, Management Science 6(1) (1959), 73-79.
[7] E. Demeulemeester and W. Herroelen, Robust Project Scheduling, volume 9. Now Publishers Inc, 2011.
[8] S.M. Easa, Resource leveling in construction by optimization, Journal of Construction Engineering and Management 115(2) (1989), 302-316.
[9] C. Fang, R. Kolisch, L. Wang and C. Mu, An estimation of distribution algorithm and new computational results for the stochastic resource-constrained project scheduling problem, Flexible Services and Manufacturing Journal 27(4) (2015), 585-605.
[10] J. Gao, Uncertain bimatrix game with applications, Fuzzy Optimization and Decision Making 12(1) (2013), 65-78.
[11] J. Gao, X. Yang and D. Liu, Uncertain shapley value of coalitional game with application to supply chain alliance, Applied Soft Computing (2016).
[12] T. Gather, J. Zimmermann and J.-H. Bartels, Exact methods for the resource levelling problem, Journal of Scheduling 14(6) (2011), 557-569.
[13] W. Herroelen, E. Demeulemeester and B. De Reyck, A classification scheme for project scheduling, In Project Scheduling: Recent Models, Algorithms and Applications, Kluwer, Amsterdam, 1999, pp. 1-26.
[14] H. Ke, A genetic algorithm-based optimizing approach for project time-cost trade-off with uncertain measure, Journal of Uncertainty Analysis and Applications 2(1) (2014), 8.
[15] H. Ke, Uncertain random time-cost trade-off problem, Journal of Uncertainty Analysis and Applications 2(1) (2014), Article 23.
[16] H. Ke, H. Liu and G. Tian, An uncertain random programming model for project scheduling problem, International Journal of Intelligent Systems 30(1) (2015), 66-79.
[17] H. Ke, T. Su and Y. Ni, Uncertain random multilevel programming with application to production control problem, Soft Computing 19(6) (2015), 1739-1746.
[18] R. Kolisch and S. Hartmann, Heuristic algorithms for the resource-constrained project scheduling problem: Classification and computational analysis, In Project Scheduling: Recent Models, Algorithms and Applications, Kluwer Academic Publishers, Netherlands, 1999, pp. 147-178.
[19] C. Kyriklidis and G. Dounias, Evolutionary computation for resource leveling optimization in project management, Integrated Computer-Aided Engineering 23(2) (2016), $173-184$.
[20] H. Li and E. Demeulemeester, A genetic algorithm for the robust resource leveling problem, Journal of Scheduling 19(1) (2016), 43-60.
[21] H. Li, Z. Xu and E. Demeulemeester, Scheduling policies for the stochastic resource leveling problem, Journal of Construction Engineering and Management 141(2) (2014), 04014072.
[22] B. Liu, Dependent-chance programming: A class of stochastic optimization, Computers \& Mathematics with Applications 34(12) (1997), 89-104.
[23] B. Liu, Uncertain Programming, John Wiley \& Sons, Inc., 1999.
[24] B. Liu, Uncertain programming: A unifying optimization theory in various uncertain environments, Applied Mathematics and Computation 120(1) (2001), 227-234.
[25] B. Liu, Theory and Practice of Uncertain Programming, Springer, 2002.
[26] B. Liu, Uncertainty Theory, 2nd edition, Springer-Verlag, Berlin, 2007.
[27] B. Liu, Fuzzy process, hybrid process and uncertain process, Journal of Uncertain systems 2(1) (2008), 3-16.
[28] B. Liu, Some research problems in uncertainty theory, Journal of Uncertain Systems 3(1) (2009), 3-10.
[29] B. Liu, Uncertainty Theory, 4th edition, Springer-Verlag, Berlin, 2010.
[30] B. Liu and K. Iwamura, Modelling stochastic decision systems using dependent-chance programming,

European Journal of Operational Research 101(1) (1997), 193-203.
[31] B. Liu and K. Yao, Uncertain multilevel programming: Algorithm and applications, Computers \& Industrial Engineering 89 (2015), 235-240.
[32] W. Ma, Y. Che, H. Huang and H. Ke, Resource-constrained project scheduling problem with uncertain durations and renewable resources, International Journal of Machine Learning and Cybernetics 7(4) (2016), 613-621.
[33] M. Masmoudi and A. HaiT, Project scheduling under uncertainty using fuzzy modelling and solving techniques, Engineering Applications of Artificial Intelligence 26(1) (2013), 135-149.
[34] K. Neumann, C. Schwindt and J. Zimmermann, Project Scheduling with Time Windows and Scarce Resources: Temporal and Resource-constrained Project Scheduling with Regular and Nonregular Objective Functions, Springer, 2002.
[35] K. Neumann and J. Zimmermann, Resource levelling for projects with schedule-dependent time windows, European Journal of Operational Research 117(3) (1999), $591-605$.
[36] J. Rieck, J. Zimmermann and T. Gather, Mixed-integer linear programming for resource leveling problems, European Journal of Operational Research 221(1) (2012), $27-37$.
[37] A.M. Vartouni and L.M. Khanli, A hybrid genetic algorithm and fuzzy set applied to multi-mode resource-constrained project scheduling problem, Journal of Intelligent \& Fuzzy Systems 26(3) (2014), 1103-1112.
[38] L. Wang and C. Fang, An effective estimation of distribution algorithm for the multi-mode resource-constrained project scheduling problem, Computers \& Operations Research 39(2) (2012), 449-460.
[39] L. Wang, H. Huang and H. Ke, Chance-constrained model for RCPSP with uncertain durations, Journal of Uncertainty Analysis and Applications 3(1) (2015), Article 12.
[40] X. Yang and J. Gao, Linear-quadratic uncertain differential game with application to resource extraction problem, IEEE Transactions on Fuzzy Systems 24(4) (2016), 819-826.
[41] X. Zhang and X. Chen, A new uncertain programming model for project scheduling problem, Information: An International Interdisciplinary Journal 15(10) (2012), 3901-3910.
[42] Y. Zhang, P. Liu, L. Yang and Y. Gao, A bi-objective model for uncertain multi-modal shortest path problems, Journal of Uncertainty Analysis and Applications 3(1) (2015), Article 8.
[43] Z. Zhang, R. Gao and X. Yang, The stability of multifactor uncertain differential equation, Journal of Intelligent \& Fuzzy Systems 30(6) (2016), 3281-3290.

## Appendix

Let $\Gamma$ be a nonempty set, $L$ a $\sigma$-algebra over $\Gamma$, and each element $\Omega$ in $L$ is called an event. Uncertain measure $M$ is a function from $L$ to $[0,1]$. It is defined over the following four axioms.

Axiom 1. [26] (Normality Axiom) $\mathrm{M}\{\Gamma\}=1$.
Axiom 2. [26] (Duality Axiom) $\mathrm{M}\{\Omega\}+\mathrm{M}\left\{\Omega^{c}\right\}=1$ for any event $\Omega$.

Axiom 3. [26] (Subadditivity Axiom) For every countable sequence of events $\left\{\Omega_{i}\right\}, i=1,2, \cdots$, we have:

$$
\mathrm{M}\left\{\bigcup_{i=1}^{\infty} \Omega_{i}\right\} \leq \sum_{i=1}^{\infty} \mathrm{M}\left\{\Omega_{i}\right\}
$$

Axiom 4. [28] (Product Measure Axiom) Let $\left(\Gamma_{k}, L_{k}, \mathrm{M}_{k}\right)$ be uncertainty spaces for $k=1,2, \cdots$ The product uncertain measure M is an uncertain measure satisfying

$$
\mathrm{M}\left\{\prod_{k=1}^{\infty} \Omega_{k}\right\}=\bigwedge_{k=1}^{\infty} \mathrm{M}_{k}\left\{\Omega_{k}\right\}
$$

where $\Omega_{k}$ are arbitrarily chosen events from $L_{k}$ for $k=1,2, \cdots$, respectively.

Definition 1. [26] An uncertain variable is a measurable function $\xi$ from an uncertainty space $(\Gamma, L, \mathrm{M})$ to the set of real numbers, i.e., for any Borel set $B$ of real numbers, the set

$$
\{\xi \in B\}=\{\gamma \in \Gamma \mid \xi(\gamma) \in B\}
$$

is an event.

The uncertainty distribution is indispensable to establish practical uncertain optimization models.

Definition 2. [26] The uncertainty distribution $\Phi$ of an uncertain variable $\xi$ is defined by

$$
\Phi(x)=\mathrm{M}\{\xi \leq x\}
$$

for any real number $x$.
An uncertainty distribution $\Phi$ is confirmed to be regular if its inverse function $\Phi^{-1}(\alpha)$ exists uniquely for each $\alpha \in[0,1]$.

Definition 3. [26] Let $\xi$ be an uncertain variable. The expected value of $\xi$ is defined by

$$
E[\xi]=\int_{0}^{+\infty} \mathrm{M}\{\xi \geq r\} \mathrm{d} r-\int_{-\infty}^{\Omega} \mathrm{M}\{\xi \leq r\} \mathrm{d} r
$$

provided that at least one of the above two integrals is finite.

Definition 4. [29] Let $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$ be independent uncertain variables with regular uncertainty distributions $\Phi_{1}, \Phi_{2}, \cdots, \Phi_{n}$, respectively. A function $f\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ is strictly increasing with respect to $x_{1}, x_{2}, \cdots, x_{m}$ and strictly decreasing with respect to $x_{m+1}, x_{m+2}, \cdots, x_{n}$. Then $\xi=f\left(\xi_{1}, \xi_{2}, \cdots, \xi_{n}\right)$ is an uncertain variable with inverse uncertainty distribution

$$
\begin{aligned}
& \Psi^{-1}(\alpha) \\
& \quad=f\left(\Phi_{1}^{-1}(\alpha), \cdots, \Phi_{m}^{-1}(\alpha), \Phi_{m+1}^{-1}(1-\alpha), \cdots, \Phi_{n}^{-1}(1-\alpha)\right)
\end{aligned}
$$