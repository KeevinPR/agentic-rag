# An Estimation of Distribution Algorithm with Efficient Constructive Repair/Improvement Operator for the Dynamic Weapon-Target Assignment 

XIN Bin ${ }^{1,2}$, CHEN Jie ${ }^{1,3}$<br>1. School of Automation, Beijing Institute of Technology, Beijing 100081<br>E-mail: brucebin@bit.edu.cn

2. Decision and Cognitive Sciences Research Centre, Manchester Business School, University of Manchester, Manchester M15 6PB
3. Key Laboratory of Complex System Intelligent Control and Decision, Ministry of Education, Beijing 100081

E-mail: chenjie@bit.edu.cn


#### Abstract

This paper reports our recent research about new efficient problem-solvers for the dynamic weapon-target assignment (DWTA). A binary-encoding-based estimation of distribution algorithm (EDA) is proposed to solve DWTA problems. An elaborate constructive repair/improvement (CRI) operator is proposed and integrated into the EDA to achieve constraint saturation, which conduces to constraint satisfaction as well as the improvement of generated solutions. The performance comparison against another two EDAs which employ well-known constraint handling methods demonstrates the superiority of the CRI operator. The proposed EDA based on the CRI operator also shows very competitive and even better performance against several state-of-the-art DWTA algorithms.


Key Words: Dynamic weapon-target assignment, estimation of distribution algorithm, constructive repair/improvement operator, constraint handling

## 1 Introduction

The dynamic weapon-target assignment (DWTA) problem is a typical NP-Complete combinatorial optimization problem which is rooted in military operations research ${ }^{[1]-[4]}$. In practice, commanders have to react to the battle situation quickly while deliberating the whole combating effect through all stages to ensure the quality of decision schemes on resource allocation. The objective of DWTA is to minimize the own-force damage in defense scenarios or maximize the damage of enemies in offense scenarios by assigning available weapons to hostile targets on appropriate engagement occasions. In contrast to the static weapon-target assignment (SWTA) in which all weapons are assigned to targets in a single stage ${ }^{[1]}$, a distinct feature of DWTA lies in that DWTA considers the pairing of weapons and targets among multiple engagement stages ${ }^{[5]}$. In other words, the resource allocation in DWTA involves the triplet pairing of weapons, targets and stages ${ }^{[5]-[7]}$. In the following, we provide a brief review on previous DWTA research.

Most previous research on the weapon-target assignment has been focused on SWTA ${ }^{[4]}$. DWTA began to gain more attention of researchers only in recent years though it was formally put forward by Hosein and Athans in 1990 ${ }^{[2]}$. Cai et al. provided a survey on WTA research and set forth some basic concepts on DWTA ${ }^{[4]}$. Hosein and Athans made a pioneering effort to analyze a two-stage DWTA process and proposed a suboptimal algorithm to find some desirable solutions ${ }^{[8]}$. Khosla proposed a hybrid algorithm of genetic algorithm and simulated annealing to solve a DWTA problem for network-centric force coordination ${ }^{[9]}$. Zacherl

[^0]designed a genetic algorithm to solve the DWTA problem involved in a UAV's mission of striking time-sensitive targets ${ }^{[10]}$. Wu et al. proposed a DWTA algorithm based on genetic algorithm which handles targets one by one according to the deadlines of each weapon-target assignment pair ${ }^{[11]}$. Dionne et al. developed a sequential DWTA algorithm for naval warfare which considers all potential decisions and suffers from dimensional explosion ${ }^{[12]}$. Li et al. proposed a target-based DWTA model which aims at minimizing the total threat of the targets surviving through the whole defense process ${ }^{[13]}$. Recently, we built a generic defense-oriented asset-based DWTA model which incorporates different kinds of practical constraints ${ }^{[5]}$. We proposed an efficient permutation-based tabu search algorithm to solve the DWTA problem ${ }^{[6]}$. The tabu search algorithm takes advantage of a construction procedure to convert the permutations of available weapon-target-stage assignment pairs into saturated feasible solutions. In order to fit the real-time requirement of DWTA, we also proposed a constructive heuristic which uses the domain knowledge of DWTA in the form of three simple rules to obtain a high-quality solution very quickly ${ }^{[7]}$. The heuristic has a notable virtue of low computational complexity.

The contribution of this paper is twofold. First, a new sophisticated constructive repair/improvement operator is proposed to handle constraints in DWTA. The operator can be applied in any binary-encoding based DWTA algorithms. Second, an estimation of distribution algorithm is proposed to solve DWTA problems more efficiently.

## 2 Mathematical Model of the DWTA Problem

The objective of the DWTA decision-making process is to maximize the expected total value of own-force assets surviving through the whole defense process:


[^0]:    ${ }^{9}$ This work is supported by National Science Fund for Distinguished Young Scholars under Grant 60925011.

$$
J(\mathbf{X})=\sum_{k=1}^{K} v_{i} \prod_{j \in \mathscr{J}_{k}}\left[1-q_{j k} \prod_{t=1}^{S} \prod_{t \in \mathscr{P}_{j}^{t}}^{j}\left(1-p_{i j}(t)\right)^{x_{i j}(t)}\right]
$$

where $K$ and $S$ are the number of threatened assets and that of defense stages, respectively, $t$ is the stage index, $\mathbf{X}=\left[X_{1}, X_{2}, \cdots, X_{K}\right]$ with $X_{i}=\left[x_{i j}(t)\right]_{W \times T}$ is the decision matrix at stage $t$, and $x_{i j}(t)=1$ if weapon $i$ is assigned to target $j$ at stage $t, x_{i j}(t)=0$ otherwise; $\mathscr{J}_{k}$ is the index set of the targets which threaten asset $k ; \mathscr{P}_{j}^{t}$ is the index set of the weapons which are assigned in stage $t$ to intercept target $j ; v_{k}$ is the value of asset $k ; q_{j k}$ is the lethality probability that target $j$ destroys asset $k$, and $p_{i j}(t)$ is the lethality probability that weapon $i$ destroys target $j$ at stage $t$ which can be evaluated according to actual combat situations.

The following four kinds of constraints are considered in the DWTA model ${ }^{[3]}{ }^{[7]}$ :

$$
\begin{aligned}
& \sum_{j=1}^{T} x_{i j}(t) \leq n_{j}, \forall t \in\{1,2, \cdots, S\}, \forall i \in\{1,2, \cdots, W\} \\
& \sum_{i=1}^{W} x_{i j}(t) \leq m_{j}, \forall t \in\{1,2, \cdots, S\}, \forall j \in\{1,2, \cdots, T\} \\
& \sum_{i=1}^{S} \sum_{j=1}^{T} x_{i j}(t) \leq N_{i}, \quad \forall i \in\{1,2, \cdots, W\} \\
& x_{i j}(t) \leq f_{i j}(t), \quad \forall t \in\{1,2, \cdots, S\}, \\
& \forall i \in\{1,2, \cdots, W\}, \quad \forall j \in\{1,2, \cdots, T\}
\end{aligned}
$$

where $T$ and $W$ are the number of targets and that of weapons, respectively.

The constraint (2) reflects the weapons' capability of striking multiple targets at the same time. In practice, most weapons can only engage a single target each time. Besides, a superior weapon capable of engaging multiple targets concurrently can be regarded as multiple separate weapons. Accordingly, we set $n_{j}=1$ for $\forall i \in\{1,2, \cdots, W\}$. The constraint (3) restricts the ammunition consumption for each target at each stage. We assume that $m_{j}=1$ for $\forall j \in\{1,2, \cdots, T\}$. This is a rational setting for combating systems with high accuracy and lethality, consistent with the common "shoot-look-shoot" engagement policy ${ }^{[2]}$. The constraint (4) is a resource constraint, reflecting the amount of ammunition available for weapons. $N_{i}(i=1,2, \cdots, W)$ is the maximal number of times that weapon $i$ can be used. The constraint (5) reflects the engagement feasibility with $f_{i j}(t)$ indicating whether weapon $i$ can be used to strike target $j$ at stage $t$. $f_{i j}(t)=0$ if weapon $i$ cannot shoot target $j$ at stage $t$ for any potential reason (e.g., the time window of targets and weapons ${ }^{[4]}{ }^{[11]}{ }^{[13]}$ ), and $f_{i j}(t)=1$ otherwise.

A complete DWTA process is a multi-stage decisionmaking process. At each decision-making stage, the decision-maker (DM) needs to work out a global assignment scheme which takes into account the whole defense effect through all subsequent defense stages ${ }^{[6]}$. However, only the assignments which can be implemented immediately at the current stage are carried out. When entering the next stage, the DM has observed the outcomes of previous
engagements and has to reformulate a new global assignment scheme which covers the subsequent stages starting from the next stage ${ }^{[7]}$. Nevertheless, from the perspective of DWTA problem-solving, the DM at each stage faces a similar global assignment problem. Besides, the DWTA problems corresponding to latter stages usually become much easier due to the reduction of targets, available weapons and engagement occasions. Therefore, the same DWTA algorithm can be applied at different stages, which means that one is only interested in obtaining assignments for the present stage ${ }^{[2]}$. In the following, we will focus on the DWTA problem-solving at one decision-making stage to design and evaluate DWTA algorithms.

## 3 Estimation of Distribution Algorithm for DWTA problem-solving

Estimation of distribution algorithms (EDAs), also termed as probabilistic model-building genetic algorithms ${ }^{[14]}{ }^{[15]}$, are population-based stochastic search algorithms that explore the space of potential solutions by building and sampling the probability model of promising candidate solutions. EDAs maintain a population of solutions and follow a cyclic operation procedure composed by three primary operations: choosing a subset of elite solutions (selection), building a probability model from the chosen solutions (modeling), and generate new solutions from the constructed model (sampling).

### 3.1 Solution Encoding and Probability Model

An appropriate solution encoding scheme is crucial for any competent algorithm to solve combinatorial optimization problems. The decision matrix $\mathbf{X}$, apparently being a straightforward representation of solutions, is not an efficient encoding scheme as it contains many decision variables ( $x_{i j}(t)$ ) which may violate the constraints in (5). In fact, it is unnecessary to include the variables which correspond to $f_{i j}(t)=0$ since $x_{i j}(t)=1$ will obviously violate constraints in this case. Therefore, we only consider feasible assignment pairs corresponding to $f_{i j}(t)=1$ which are also termed as available assignment pairs (AAPs) in previous research ${ }^{[5]}{ }^{[7]}$. Arrange all AAPs by $A A P_{1}, A A P_{2}, \cdots, A A P_{L}$ where $L$ denotes the number of AAPs and $A A P_{k}=\left(i_{k}, j_{k}, t_{k}\right)(k=1,2, \cdots, L)$ is a triplet pairing of weapon $i_{k}$, target $j_{k}$ and stage $t_{k}$. We employ an $L$-sized $0-1$ vector $\mathbf{z}=\left[z_{1}, z_{2}, \cdots, z_{L}\right]$ to represent a DWTA solution where $z_{k}(k=1,2, \cdots, L)$ indicates whether $A A P_{k}$ is chosen ( $z_{k}=1$, equivalently, $x_{i_{k} j_{k}}\left(t_{k}\right)=1$ ) or not ( $z_{k}=0$, i.e., $x_{i_{k} j_{k}}\left(t_{k}\right)=0$ ).

The EDA's probability model for DWTA problem-solving is shown as follows:

$$
\begin{aligned}
& p\left(z_{k}=1\right)=\min \left\{\max \left\{\frac{1}{N} \sum_{n=1}^{N} z_{k}^{n}, 0,01\right\}, 0,99\right\} \\
& p\left(z_{k}=0\right)=1-p\left(z_{k}=1\right), k=1,2, \cdots, L
\end{aligned}
$$

where $p\left(z_{k}=1\right)$ is the probability that the component $z_{k}$ of elite solutions is one; $\mathbf{z}^{n}=\left[z_{1}^{n}, z_{2}^{n}, \cdots, z_{L}^{n}\right](n=1,2, \cdots, N)$

are elite solutions chosen for modeling; and $N$ is the number of elite solutions, i.e., the sample size. 0.01 and 0.99 are the lower and upper bounds for $p\left(z_{k}=1\right)$ to avoid the premature convergence of the probability model.

The rule for generating new solutions from the above probability model is shown as follows:

$$
z_{k}=\left\{\begin{array}{ll}
1, & \text { if } \operatorname{rand}<p\left(z_{k}=1\right), \text { for } k=1,2, \ldots, L \\
0, & \text { otherwise. }
\end{array}\right.
$$

where rand is a random number generated from the interval $(0,1)$.

Remark 1. The simple probability model was also employed in the classical univariate marginal distribution algorithm ${ }^{[16]}$. The linkage between different solution components may be considered to build a more sophisticated probability model such as a tree-based model or Bayesian network ${ }^{[14],[15]}$. However, complicated models may cause a serious issue of computational complexity which is unacceptable for real-time DWTA decision-making.

### 3.2 Constructive Repair/Improvement Operator

The solutions which will be generated from the above model may not satisfy the constraints in (2), (3) or (4), resulting in infeasible solutions. Besides, even if feasible solutions can be produced, they may be unsaturated, meaning that more AAPs can be chosen to produce better solutions without any constraint violations. It should be noted that a saturated feasible solution contains as many assigned AAPs as possible, and any further addition of other AAPs will give rise to constraint violation. From the above considerations, in the following we propose a novel constructive repair/improvement operator to ensure constraint satisfaction as well as improve the quality of feasible solutions:

Step 1. Convert the solution $\mathbf{z}=\left[z_{1}, z_{2}, \cdots, z_{L}\right]$ generated by the probability model into a new vector $\mathbf{r}=\left[r_{1}, r_{2}, \cdots, r_{L}\right]$ as follows:

$$
r_{k}=z_{k} * \operatorname{rand}_{k}^{1}-\left(1-z_{k}\right) * \operatorname{rand}_{k}^{2}, \text { for } k=1,2, \ldots, L
$$

where $\operatorname{rand}_{k}^{1}$ and $\operatorname{rand}_{k}^{2}$ are two random numbers generated from the interval $(0,1)$.

Step 2. Sort all AAPs in the descending order of the values of their corresponding elements in the vector $\mathbf{r}$. For example, the vector $\mathbf{r}=[-0.1,0.3,0.8,-0.6,0.2]$ which is generated from $\mathbf{z}=[0,1,1,0,1]$ will give the sorting result: $A A P_{3}, A A P_{2}, A A P_{5}, A A P_{1}, A A P_{4}$.

Step 3. Use the following construction procedure to generate a saturated feasible solution:

For $i=1$ to $L$
Check if assigning the $i$ th $\operatorname{AAP}\left(A A P_{k(i)}\right)$ in the sorted sequence will violate any constraints: if no constraints are violated, let $z_{k(i)}=1$; otherwise, let $z_{k(i)}=0$.

End

The above constructive repair/improvement (CRI) operator has the following features:

1) Be able to retain the information contained in the probability model to large extent. On one hand, in the solution generated from the probability model, the chosen AAPs will be endowed with positive $r$ values, and the unchosen ones lead to negative $r$ values. Consequently, the chosen AAPs will be arranged to the head of the AAP sequence in Step 2, and they will be preferred to be rechosen in Step 3. On the other hand, the chosen AAPs which do not violate constraints will be reserved in the solution finally produced by Step 3.
2) The construction procedure in Step 3 guarantees that all solutions generated by the CRI operator are saturated feasible solutions. The operator can not only repair infeasible solutions but also improve the quality of feasible solutions.
3) Among all the chosen AAPs generated by EDA's sampling procedure, the randomizing operation shown in (8) shows no preference to any of them. Therefore, any AAP which may have conflicts against other AAPs will have an opportunity to be included in the final solution produced by the CRI operator.

### 3.3 EDA

The procedure of the proposed EDA is presented as follows:

## Step 1. Initialization

Randomly generate $P S-1$ solutions with $p\left(z_{k}=1\right)=0.5(k=1,2, \cdots, L)$ and use the CRI operator to repair and improve the initial solutions. Use the rule-based heuristic proposed in [7] to generate a solution and add it into the population. Record the best solution in the whole population.

Remark 2. The rule-based heuristic in [7] is de facto a deterministic greedy algorithm which chooses AAPs according to their $v_{k} q_{j k} p_{j j}(t)$ values.

## Step 2. Elitist Selection

Sort the $P S$ solutions in the descending order of their objective values. Select the $N=P S * R(R \in(0,1))$ top solutions to build the probability model [see (6)].

## Step 3. Sampling

Use the constructed model to generate $P S-N$ new solutions, and use the CRI operator to repair and improve them. Replace the worst $P S-N$ solutions in the current population by the new solutions. Update the so-far-best solution.

## Step 4. Termination Criterion

If the termination criterion is satisfied, terminate the algorithm and output the so-far-best solution; otherwise, go to Step 2.

## 4 Computational Experiments and Performance Comparison

There are ten DWTA test instances involved in the experiments, including two simple small-sized instances in [6] and eight instances generated by the test-case generator proposed in [7]. The characteristic parameters of these instances are listed as follows.

Instance 1: Naval Single-Platform Combat Scenario
(W5T3S3K1, $L=29$ )
Instance 2: Ground-based Air Defense Scenario
(W8T5S3K5, $L=36$ )
Instance 3: W10T10S4K5 ( $L=209$ )
Instance 4: W20T10S4K5 ( $L=387$ )
Instance 5: W20T20S4K10 ( $L=815$ )
Instance 6: W20T20S4K20 ( $L=803$ )
Instance 7: W50T50S4K20 ( $L=495$ )
Instance 8: W50T50S4K20 ( $L=2023$ )
Instance 9: W100T50S4K50 ( $L=1017$ )
Instance 10: W100T100S4K50 ( $L=1999$ )
All experiments were carried out in Matlab (Version 6.5) on a laptop with Intel (R) Core i5 CPU (2.27GHz) and 1.92 GB internal memory. Regarding any instance, all algorithms independently run 30 times and results are statistically analyzed. Without specific claims, any algorithm will be terminated when the number of function evaluations reaches $\min \left\{5 W * T * S, 50000\right\}$. The EDA algorithm has two parameters: population size $(P S)$ and selection ratio $(R)$. Four kinds of settings are tested for each of them: $P S=50,100,200,500$ and $R=0.1,0.3,0.5,0.7$. There are totally sixteen combinations of the two parameters. It was found in preliminary experiments that $R=0.3$ is always a nice choice, and a smaller population size $(P S=50)$ fits small-sized instances while a larger population size $(P S=200)$ is a better choice for large-sized instances. To save space, the detailed results are not shown here and the identified setting is described as follows:
$P S=50$ and $R=0.3$ for instances with $L \leq 1000$; $P S=200$ and $R=0.3$ for instances with $L>1000$.
![img-0.jpeg](img-0.jpeg)

Fig. 1: The dynamic change of EDA's probability model and the EDA's convergence process (instance 7).

Fig. 1 shows the dynamic change of the EDA's probability model and the convergence process of EDA in solving instance 7. For clarity, only five components of the probability model, $p\left(z_{k}=1\right)(k=1,2,3,4,5)$, are shown in Fig.1. It is clear that with the increase of generations, the probability model tends to polarization, that
is to say, the probability values of the EDA model reach either its lower bound ( 0.01 ) or upper bound ( 0.99 ). Along with the polarization of the probability model, the algorithm converges as indicated by the curve of the average objective value of all solutions in the population.

The following experiments are arranged into two parts. The first part provides a comparison between different constraint handling methods which are embedded into the same EDA algorithm, including the CRI operator and two well-known constraint handling methods in the constrained evolutionary optimization research. The second part gives a comparison between the proposed EDA and two state-of-the-art DWTA algorithms.

### 4.1 Comparison on Constraint Handling Methods

There are many choices to handle constraints in constrained optimization ${ }^{[17]}$. The most common constraint handling methods are penalty functions which integrate the constraint handling and the improvement of objective values into a penalty function. Infeasible solutions will be penalized by decreasing (penalizing) their fitness according to their constraint violations. As pointed out by Runarrson and Yao, a crucial issue in the design of penalty functions is how to strike a balance between objective improvement and constraint satisfaction ${ }^{[18]}$. Runarsson and Yao proposed a stochastic ranking (SR) approach to balance the two goals in constrained optimization ${ }^{[18]}$. Deb proposed a straightforward approach based on three feasibility rules (FR) ${ }^{[19]}$. Both SR and FR allow the evolutionary population to include infeasible solutions. In SR, two feasible solutions are compared according to their objective values. In other cases, any two solutions are compared according to their objective values with probability $P_{f}$ and according to their constraint violations with probability $1-P_{f}{ }^{[19]}$. Obviously, SR balances constraint satisfaction and objective improvement stochastically. In contrast, FR adopts three simple rules for pairwise comparison of solutions: 1) any feasible solution is preferred to any infeasible one; 2) among two feasible solutions, the one having better objective value is preferred; 3) among two infeasible solutions, the one having smaller constraint violation is preferred ${ }^{[19]}$.

In the following, SR and FR will be incorporated into the EDA framework in the previous section to solve DWTA problems. For both SR and FR, the constraint violation of a solution (denoted by $\phi$ ) is measured as follows:

$$
\begin{aligned}
\phi= & \sum_{t=1}^{S} \sum_{i=1}^{W} H\left(\sum_{j=1}^{T} x_{i j}(t)-m_{i}\right)+\sum_{t=1}^{S} \sum_{j=1}^{T} H\left(\sum_{i=1}^{W} x_{i j}(t)-m_{j}\right) \\
& +\sum_{t=1}^{W} H\left(\sum_{i=1}^{T} \sum_{j=1}^{T} x_{i j}(t)-N_{i}\right)
\end{aligned}
$$

where $H(\cdot)$ is equal to the value of its argument if the argument is positive, and zero otherwise.

For brevity, the EDAs based on SR, FR and CRI are termed as EDA-SR, EDA-FR and EDA-CRI, respectively. The three EDA variants adopt the same probability model, the same sampling method as well as the same setting of EDA parameters. However, EDA-SR and EDA-FR do not employ the CRI operator to repair and/or improve solutions.

Table 1: Statistical Results on Different DWTA Algorithms in the Form of the Mean plus Standard Deviation of Finally Discovered Best Objective Values in 30 Runs.

| No. | EDA-CRI | EDA-SR | EDA-FR | Tabu search ${ }^{[6]}$ | TS-CH | Constructive heuristic ${ }^{(7)}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | $0.53007 \pm 0.00185$ | $0.45629 \pm 0.06675^{(30)^{*}}$ | $0.41763 \pm 0.09191^{(30)^{*}}$ | $\mathbf{0 . 5 3 0 8 9} \pm \mathbf{0 . 0 0 1 8 2}{ }^{\mathrm{T}}$ | $\mathbf{0 . 5 3 0 2 1} \pm \mathbf{0 . 0 0 1 7 6}{ }^{\mathrm{T}}$ | $0.52763 \pm 0^{*}$ |
| 2 | $171.104 \pm 0$ | $168.790 \pm 1.579^{(30)^{*}}$ | $168.040 \pm 1.905^{(30)^{*}}$ | $\mathbf{1 7 1 . 1 0 4} \pm \mathbf{0}^{*}$ | $\mathbf{1 7 1 . 1 0 4} \pm \mathbf{0}^{*}$ | $169.500 \pm 0^{*}$ |
| 3 | $\mathbf{3 1 2 . 7 6} \pm \mathbf{1 . 0 8}$ | $275.21 \pm 12.46^{(30)^{*}}$ | $273.72 \pm 10.58^{(30)^{*}}$ | $310.22 \pm 0.50^{*}$ | $311.28 \pm 0.21^{*}$ | $309.41 \pm 0.00^{*}$ |
| 4 | $\mathbf{3 3 2 . 2 6} \pm \mathbf{0 . 0 8}$ | $307.57 \pm 6.78^{(30)^{*}}$ | $304.53 \pm 7.74^{(30)^{*}}$ | $332.20 \pm 0.10^{*}$ | $332.21 \pm 0.03^{*}$ | $331.7 \pm 0^{*}$ |
| 5 | $\mathbf{5 7 8 . 3 6} \pm \mathbf{0 . 3 2}$ | $357.75 \pm 29.34^{(20)^{*}}$ | $325.29 \pm 31.14^{(38)^{*}}$ | $565.52 \pm 2.17^{*}$ | $\mathbf{5 7 7 . 7 3} \pm \mathbf{0}^{*}$ | $\mathbf{5 7 7 . 7 3} \pm \mathbf{0}^{*}$ |
| 6 | $\mathbf{1 2 9 6 . 7} \pm \mathbf{0 . 0}$ | $1029.6 \pm 37.7^{(28)^{*}}$ | $991.2 \pm 39.1^{(30)^{*}}$ | $1288.6 \pm 3.1^{*}$ | $\mathbf{1 2 9 6 . 7} \pm \mathbf{0}^{*}$ | $\mathbf{1 2 9 6 . 7} \pm \mathbf{0}^{*}$ |
| 7 | $\mathbf{1 0 0 4 . 2} \pm \mathbf{1 . 8}$ | $885.13 \pm 29.23^{(30)^{*}}$ | $830.43 \pm 21.51^{(30)^{*}}$ | $989.24 \pm 2.13^{*}$ | $996.68 \pm 2.53^{*}$ | $970.59 \pm 0^{*}$ |
| 8 | $\mathbf{9 2 8 . 4 2} \pm \mathbf{0 . 0 0}$ | $429.38 \pm 39.22^{(22)^{*}}$ | $410.50 \pm 37.98^{(25)^{*}}$ | $922.15 \pm 2.03^{*}$ | $\mathbf{9 2 8 . 4 2} \pm \mathbf{0 . 0 0}^{*}$ | $\mathbf{9 2 8 . 4 2} \pm \mathbf{0}^{*}$ |
| 9 | $\mathbf{2 9 8 8 . 7} \pm \mathbf{0 . 4}$ | $2569.9 \pm 37.8^{(30)^{*}}$ | $2514.5 \pm 44.6^{(30)^{*}}$ | $2986.5 \pm 0.6^{*}$ | $2984.2 \pm 1.3^{*}$ | $2980.9 \pm 0^{*}$ |
| 10 | $\mathbf{2 4 6 4 . 1} \pm \mathbf{0 . 0}$ | $1165.4 \pm 74.1^{(24)^{*}}$ | $1081.5 \pm 67.8^{(24)^{*}}$ | $2434.8 \pm 5.5^{*}$ | $\mathbf{2 4 6 4 . 1} \pm \mathbf{0}^{*}$ | $\mathbf{2 4 6 4 . 1} \pm \mathbf{0}^{*}$ |

The numbers in parentheses for EDA-SR and EDA-FR are the times that they find feasible solutions in each case.
${ }^{*}$ EDA-CRI performs better than the target algorithm, which is tested by the Wilcoxon rank sum test with a significance level 0.05 .
${ }^{\mathrm{T}}$ The performances of EDA-CRI and the target algorithm have no significant difference.
Table 2: Statistical Results on Different DWTA Algorithms in the Form of the Mean plus Standard Deviation of the Computation Time (in seconds) in 30 Runs

| No. | EDA-CRI | EDA-SR | EDA-FR | Tabu search ${ }^{[6]}$ | TS-CH | Constructive heuristic ${ }^{(7)}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | $0.053 \pm 0.008$ | $0.071 \pm 0.008$ | $0.071 \pm 0.008$ | $0.071 \pm 0.011$ | $0.071 \pm 0.011$ | $\mathbf{0 . 0 0 1} \pm \mathbf{0 . 0 0 4}$ |
| 2 | $0.160 \pm 0.077$ | $0.234 \pm 0.000$ | $0.234 \pm 0.003$ | $0.233 \pm 0.004$ | $0.232 \pm 0.004$ | $\mathbf{0 . 0 0 1} \pm \mathbf{0 . 0 0 4}$ |
| 3 | $0.781 \pm 0.036$ | $0.823 \pm 0.007$ | $0.824 \pm 0.007$ | $0.823 \pm 0.011$ | $0.823 \pm 0.009$ | $\mathbf{0 . 0 0 3} \pm \mathbf{0 . 0 0 8}$ |
| 4 | $2.090 \pm 0.057$ | $2.290 \pm 0.008$ | $2.290 \pm 0.008$ | $2.292 \pm 0.010$ | $2.291 \pm 0.010$ | $\mathbf{0 . 0 0 5} \pm \mathbf{0 . 0 0 7}$ |
| 5 | $7.299 \pm 0.223$ | $7.447 \pm 0.007$ | $7.446 \pm 0.008$ | $7.448 \pm 0.010$ | $7.447 \pm 0.010$ | $\mathbf{0 . 0 1 4} \pm \mathbf{0 . 0 0 9}$ |
| 6 | $7.134 \pm 0.078$ | $7.348 \pm 0.007$ | $7.347 \pm 0.006$ | $7.350 \pm 0.012$ | $7.348 \pm 0.011$ | $\mathbf{0 . 0 1 4} \pm \mathbf{0 . 0 0 9}$ |
| 7 | $44.54 \pm 1.42$ | $48.43 \pm 0.01$ | $48.43 \pm 0.01$ | $48.47 \pm 0.01$ | $48.45 \pm 0.01$ | $\mathbf{0 . 0 1 1} \pm \mathbf{0 . 0 0 8}$ |
| 8 | $108.99 \pm 3.38$ | $126.28 \pm 0.00$ | $126.28 \pm 0.00$ | $126.33 \pm 0.01$ | $126.29 \pm 0.01$ | $\mathbf{0 . 0 5 6} \pm \mathbf{0 . 0 1 9}$ |
| 9 | $75.84 \pm 0.64$ | $78.17 \pm 0.00$ | $78.17 \pm 0.00$ | $78.21 \pm 0.01$ | $78.19 \pm 0.01$ | $\mathbf{0 . 0 3 6} \pm \mathbf{0 . 0 1 0}$ |
| 10 | $129.84 \pm 2.26$ | $135.20 \pm 0.00$ | $135.20 \pm 0.00$ | $135.22 \pm 0.02$ | $135.22 \pm 0.02$ | $\mathbf{0 . 0 9 2} \pm \mathbf{0 . 0 2 6}$ |

Besides, it was observed that EDA-SR and EDA-FR spend less time generating new solutions. In the experiments, EDA-SR and EDA-FR are allowed to run until the maximal time that EDA-CRI takes among 30 runs has been exceeded. In EDA-SR, three different settings for its parameter $P_{f}$ are considered: $P_{f}=0.1,0.3,0.45$ where $P_{f}=0.45$ is suggested by Runarsson and Yao ${ }^{[18]}$. Only the results corresponding to the best setting are presented for EDA-SR in each case. The experimental results about the three EDAs are shown in Tables 1 and 2.

From Tables 1 and 2, it is obvious that EDA-CRI outperforms both EDA-SR and EDA-FR in all cases. EDA-SR and EDA-FR even failed to find feasible solutions in some cases. For example, EDA-SR and EDA-FR did not produce feasible solutions once and twice among 30 runs regarding instance 5, respectively. In fact, both EDA-SR and EDA-FR spend too much time on infeasible solutions. In contrast, EDA-CRI only produces saturated feasible solutions, which benefits EDA-CRI to focus its search on promising solutions.

### 4.2 Comparison against State-of-the-Art DWTA Algorithms

The tabu search (TS) based DWTA algorithm proposed in [6] and the rule-based constructive heuristic (CH) proposed in [7] are chosen for a further comparison with EDA-CRI. Like EDA, TS is a search algorithm; however, it relies on neighborhood exploration and diversification mechanisms to carry out a trajectory search rather than the population-based search in EDA. In contrast, CH is a deterministic greedy algorithm which produces a single solution without any iterative search. As claimed in [7], the main advantage of CH is its lower computational complexity which fits the DWTA requirement on real-time computation very well. Both TS and CH are employed to solve the above ten DWTA instances. Besides, CH is also employed to provide TS with an initial solution, and the resulting new TS variant is termed as TS-CH. TS and TS-CH are allowed to run until the maximal time that EDA-CRI spent in corresponding cases has expired. The computational results are shown in Tables 1 and 2.

As shown in Table 1, EDA-CRI performs comparatively against TS in solving instances 1 and 2, and outperforms TS in all of the remaining cases. Enhanced by $\mathrm{CH}, \mathrm{TS}-\mathrm{CH}$ obtained obviously better results than TS in instances 5, 6, 7, 8, 10. However, TS-CH in the optimization of instance 9 fails to outperform TS. This is mainly because TS itself could find high-quality solutions by its own search mechanism, while the initial solution provided by CH may retard the convergence of TS towards better solutions in this case. In fact, as shown in Table 1, TS did produce better results than CH in instance 9. On the whole, TS-CH is a nice DWTA solver, performing comparatively against EDA-CRI in instances $1,2,4,6,8$ and 10 . However, EDA-CRI has remarkable advantages over TS-CH when solving instances $3,5,7$, and 9 .

Compared with CH, EDA-CRI produces significantly better solutions in solving instances $1,2,3,4,5,7$ and 9 . It is not surprising that EDA-CRI did not lose to CH since EDA-CRI uses CH to provide an initial solution. However, EDA-CRI did not further improve the solution generated by CH in solving instances $5,6,8$ and 10 , which demonstrates that CH did provide high-quality solutions. From Table 2, there is no doubt that CH is the best DWTA algorithm in terms of time cost. This is because CH only relies on simple rules to generate a single solution without any iterative search. However, it is noteworthy that if the time for DWTA decision-making permits, any effort to improve the quality of decision schemes should be preferred. As shown in Table 2, EDA-CRI can solve smaller-sized instances (instances $1-6)$ within a few seconds, and solve larger-sized ones (instances 7-10) within a few minutes. In fact, the time cost can be reduced since EDA-CRI has converged earlier before the termination criterion is satisfied (see Fig.1). Besides, since EDA-CRI is a population-based optimizer, it is easy to implement EDA-CRI in parallel if the computing platform supports parallel computation, which can further reduce its time cost. In this sense, EDA-CRI is a desirable choice for DWTA problem-solving.

## 5 Conclusion and Future Work

An estimation of distribution algorithm based on a novel constructive repair/improvement operator is proposed for DWTA problem-solving. The repair/improvement operator not only effectively exploits the information on promising solutions extracted by EDA's probability model, but also helps to achieve constraint satisfaction as well as improve the quality of feasible solutions. It was shown that the repair/improvement operator is superior to two well-known constraint handling methods in solving DWTA problems. The proposed EDA incorporates the sophisticated operator and uses a rule-based constructive heuristic to provide an initial solution. Experimental results demonstrate the efficiency of the proposed EDA in DWTA problem-solving.

As a promising research line, it is possible to incorporate the domain knowledge of DWTA (e.g., rules similar to those used by the constructive heuristic in [7]) into EDA more efficiently, especially in the process of building EDA's probability model. The search bias induced by appropriate
heuristic rules may accelerate the convergence towards high-quality DWTA solutions and even global optimal decision schemes. How to build a more competent probability model for EDA deserves further research.

## References

[1] P. A. Hosein and M. Athans, Preferential defense strategies-Part I: The static case, MIT Laboratory for Information and Decision Systems with partial support, USA, Tech. Rep. LIPS-P-2002, 1990.
[2] P. A. Hosein and M. Athans, Preferential defense strategies-Part II: The dynamic case, MIT Laboratory for Information and Decision Systems with partial support, USA, Tech. Rep. LIPS-P-2003, 1990.
[3] S. P. Lloyd and H. S. Witsenhausen, Weapon allocation is NP-complete, in Proc. IEEE Summer Simulation Conference, Reno, Nevada, USA, 1986: 1054-1058.
[4] H. Cai, J. Liu, Y. Chen, and H. Wang, Survey of the research on dynamic weapon-target assignment problem, J. Syst. Eng. Elec., 17(3): 559-565, 2006.
[5] J. Chen, B. Xin, Z. H. Peng, L. H. Dou, and J. Zhang, Evolutionary decision-makings for dynamic weapon-target assignment problem, Science in China Series F: Information Sciences, 52(11): 2006-2018, 2009.
[6] B. Xin, J. Chen, J. Zhang, L. H. Dou, and Z. H. Peng, Efficient decision-makings for dynamic weapon-target assignment by virtual permutation and tabu search heuristics, IEEE Trans. Syst. Man Cybern. C, Appl. Rev., 40(6): 649-662, 2010.
[7] B. Xin, J. Chen, Z. H. Peng, L. H. Dou, and J. Zhang, An efficient rule-based constructive heuristic to solve dynamic weapon-target assignment problem, IEEE Trans. Syst. Man Cybern. A, Syst. Human., 41(3): 598-606, 2011.
[8] P. A. Hosein and M. Athans, Some analytical results for the dynamic weapon-target allocation problem, MIT Laboratory for Information and Decision Systems with partial support, USA, Tech. Rep. LIDS-P-1944, 1990.
[9] D. Khosla, Hybrid genetic approach for the dynamic weapon-target allocation problem, in Proc. SPIE, 4396, Orlando, USA, 2001: $244-259$.
[10] B. J. Zacherl, Weapon-target pairing: revising an air tasking order in real-time, Master Thesis, Naval postgraduate School, Monterey, California, 2006.
[11] L. Wu, H. Y. Xing, F. X. Lu, and P. F. Jia, An anytime algorithm based on modified GA for dynamic weapon-target allocation problem, in Proc. IEEE Cong. Evol. Comput., Hong Kong, China, 2008: 2020-2025.
[12] D. Dionne, E. Pogossian, A. Grigoryan, J. Couture, and E. Shahbazian, An optimal sequential optimization approach in application to dynamic weapon allocation in naval warfare, in Proc. 11th Inter. Conf. Info. Fusion, Colgone, Germany, 2008: 1-6.
[13] J. Li, R. Cong, and J. Xiong, Dynamic WTA optimization model of air defense operation of warships' formation, J. Syst. Eng. Elec., 7(1): 126-131, 2006.
[14] P. Larrahaga and J. A. Lozano, Estimation of distribution algorithms: a new tool for evolutionary computation. Boston: Kluwer Academic Publishers, 2002.
[15] M. Pelikan, D. E. Goldberg, and F. G. Lobo, A survey of optimization by building and using probabilistic models, Comput. Optim. Appl., 21(1): 5-20, 2002.
[16] H. Mühlenbein, The equation for response to selection and its use for prediction, Evol. Comput., 5(3): 303-346, 1998.
[17] C. A. C. Coello, Theoretical and numerical constraint-handling techniques used with evolutionary algorithms: a survey of the state of the art, Computer Methods in Applied Mechanics and Engineering, 191(11-12): 1245-1287, 2002.
[18] T. P. Runarsson and X. Yao, Stochastic ranking for constrained evolutionary optimization, IEEE Trans. Evol. Comput., 4(3): 284-294, 2000.
[19] K. Deb, An efficient constraint handling method for genetic algorithms, Comput. Method. Appl. Mech. Eng., 186(2-4): 311-338, 2000.