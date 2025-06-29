# An improved multiobjective estimation of distribution algorithm for environmental economic dispatch of hydrothermal power systems 

Yangyang Li*, Haiyang He, Yang Wang, Xia Xu, Licheng Jiao<br>Key Laboratory of Intelligent Perception and Image Understanding of Ministry of Education of China, Xidian University, Xi'an 710071, China


#### Abstract

ArticIcLe I N F O Article history: Received 15 July 2012 Received in revised form 3 November 2014 Accepted 30 November 2014 Available online 9 December 2014


Keywords:
Environmental economic dispatch
Regularity model-based multiobjective estimation of distribution algorithm (RM-MEDA)
Local learning
Repair mechanism

## A B S T R A C T

Environmental economic dispatch of fixed head of hydrothermal power systems is viewed as a multiobjective optimization problem in this paper. The practical hydrothermal system possesses various constraints which make the problem of finding global optimum difficult. This paper develops an improved multiobjective estimation of distribution algorithm to solving the above problem. A local learning operation is added into the original regularity model-based multiobjective estimation of distribution algorithm (RM-MEDA) in the improved approach so as to improve the local search ability and enhance the convergence efficiency. Furthermore, a repair mechanism is employed to repair the searched infeasible solutions in order to be able to search in the feasible region. In the experiment, the results obtained by the proposed approach have been compared with those from other three MOEAs: NSGA-II, NNIA, and RM-MEDA. Results from some pervious reported methods have also been employed to compare with our method. In addition, the results demonstrate the superiority of this proposed method as a promising MOEA to solve this power system multiobjective optimization problem.
(c) 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Scheduling is an important task in electric power systems. The purpose of traditional economic dispatch (ED) of electric power system is to allocate the generating unit outputs in the system so as to meet the load demand in the most economic way. However, as the increasing attention on environmental protection, minimum fuel cost is no longer the only criterion for dispatching electric power, the minimization of emissions caused by fossil fuel fired thermal power plants must also be taken into consideration. Therefore, a multiobjective optimization problem (MOP), environmental economic dispatch (EED) is proposed.

While the optimal EED in a hydrothermal power system (HPS) involves the allocation of the output of the hydro units and thermal plants in order to optimize the fuel cost and emission level simultaneously while satisfying various constraints for the hydraulic and power system network. The optimal EED problem of the HPS is formulated as a nonlinear constrained multiobjective optimization problem where fuel cost and environment impact are treated as competing objectives [1].

[^0]Various techniques have been reported to solve EED problem. Refs. [2-5] converted the multi-objective EED problem into a single-objective optimization problem by linearly combining different objectives through the weighted sum method. As only one solution can be generated in a single run by these approaches, multiple runs are needed to obtain a desired Pareto set of solutions. A $\varepsilon$-constraint method for multi-objective optimization was proposed to solve the EED problem in Refs. [6,7]. This approach is based on optimization of the most preferred objective and considering the other objectives as constraints bounder by some allowable levels " $\varepsilon$ ". However, this is a time-consuming approach and only some weakly nondominated solutions can be obtained. Simulated annealing (SA) procedure was used to solve the EED of hydrothermal power systems problem in Ref. [8]. This study used a new penalty function approach and a weighting method to linearly combine the objectives as a weighted sum. Chiang [9] proposed an approach based on the improved genetic algorithm (IGA), multiplier updating (MU) and the $\varepsilon$-constraint technique to solve the optimal EED problem in a hydrothermal power system.

Over the past ten years, multiobjective evolutionary algorithms (MOEAs) have got a great improvement. Numbers of successful MOEAs have been proposed, such as NSGA-II [10], SPEA2 [11], multiobjective Immune algorithm with nondominated neighbor-based selection (NNIA) [12] and regularity model-based multiobjective estimation of distribution algorithm (RM-MEDA) [13]. As MOEAs use a population-based approach which can produce a group of


[^0]:    * Corresponding author at: Key Laboratory of Intelligent Perception and Image Understanding of Ministry of Education of China, International Research Center for Intelligent Perception and Computation, Xidian University, Xi'an 710071, China. Tel.: +86 88202279.
    E-mail address: yyli@xidian.edu.cn (Y. Li).

solutions in a single run, they become the most effective methods in solving multi-objective optimization problems.

Due to the development of multiobjective evolutionary search strategies, the recent direction of solving EED problem is to handle both objectives simultaneously. Numbers of multi-objective evolutionary algorithms have been applied to solve the EED problem. NSGA-II was employed in Ref. [14] to solve the EED of HPS problem. In this study, a repair operation was adopted to optimization infeasible solution. Basu used three classical MOEAs including NSGA-II, MODE [15] and SPEA2 to solve the same problem in Ref. [16]. However, some solutions reported in this paper cannot satisfy the constraints of the EED of HPS problem.

The widely known traditional MOEAs [10], [11], [12] mainly adopt crossover and mutation to produce new solutions. However, only a few parent solutions are directly involved in these operations. There is no mechanism in conventional MOEAs for extracting global statistical information from the previous search and using it for guiding the further search. Thus, traditional MOEAs usually have a limited capacity for discovering. Estimation of distribution algorithms (EDAs) [17], [18], [19], [20] work in a quite different way, they maintain a probability model for characterizing the distribution of promising solutions at each generation, which serve as the vehicle to capture the data dependencies and the data structure as well. They sample from the probability model to produce new solutions. Nevertheless, EDAs often ignore the individuals information when sample new solutions. In this paper, an improved multiobjective estimation of distribution algorithms (IRM-MEDA) is proposed for the EED of HPS problem. A local learning mechanism is added into the original RM-MEDA for the purpose of improving the local search ability and enhancing the convergence efficiency.

The rest of the paper is organized as follows. Section 2 describes the problem formulation. Section 3 presents the constraint handling method. It is followed by the introduction of the improved algorithm, IRM-MEDA, in Section 4. Computational results and its comparison with other reported approaches are provided in Section 5. Finally, a conclusion is drawn in Section 6.

## 2. Problem formulation

The EED of HPS problem is to minimize fuel cost and emission simultaneously, while satisfying several equality and inequality constraints. The following objectives and constraints of the EED of HPS problem with $r \times\left(X_{\text {opp }}-X_{\text {low }}\right)$ thermal plants and $P(t)$ hydro units over $M$ time subintervals are considered. The problem can be formulated as follows [8], [9], [14].

### 2.1. Objectives

### 2.1.1. Fuel cost

The fuel cost of each thermal generating unit is expressed as the sum of a quadratic and a sinusoidal function. The superimposed sine component represents the rippling effects produced by the steam admission value opening [21]. The total fuel cost in term of real power output can be defined by

$$
\begin{aligned}
F 1= & \sum_{m=1}^{M} \sum_{i=1}^{N_{e}} t_{m}\left[a_{s i}+b_{s i} P_{s i m}+c_{s i} P_{s i m}^{2}\right. \\
& \left.+\left|d_{s i} \times \sin \left(e_{s i} \times\left(P_{s i}^{\min }-P_{s i m}\right)\right)\right|\right]
\end{aligned}
$$

In Eq. (1), F1 is the total fuel cost of thermal generators, $P_{s i m}$ is the real power generation of the $i$ th thermal unit during subinterval $m, P_{i n}^{\min }$ is the lower generation limit of the $i$ th thermal generator, $a_{s i}, b_{s i}, c_{s i}, d_{s i}$, and $e_{s i}$ are the cost coefficients of the $i$ th thermal generator and $t_{m}$ is the generating duration of subinterval $m$.

### 2.1.2. Emission

The emission of atmospheric pollutants caused by the operation of fossil-fueled thermal generation can be given as a function of its output, which is the sum of a quadratic and an exponential function [22]. The total emission can be expressed as
$F 2=\sum_{m=1}^{M} \sum_{i=1}^{N_{e}} t_{m}\left[\alpha_{s i}+\beta_{s i} P_{s i m}+\gamma_{s i} P_{s i m}^{2}+\eta_{s i} \exp \left(\sigma_{s i} P_{s i m}\right)\right]$,
where $F 2$ is the total emission of generator. $\alpha_{s i}, \beta_{s i}, \gamma_{s i}, \eta_{s i}$ and $\sigma_{s i}$ are the coefficients of the $i$ th thermal generator emission characteristics.

### 2.2. Constraints

While minimize the above objectives, the power balance constraints, water availability constraints and the system generation limits are taken into account simultaneously.

### 2.2.1. Power balance constraints

In each subinterval, the total electric power generation must be equal to the total of electric power demand and the real power loss in transmission. Hence
$\sum_{i=1}^{N e} P_{s i m}+\sum_{j=1}^{N h} P_{h j m}-P_{D m}-P_{L m}=0, \quad m=1, \ldots, M$,
where $P_{h j m}$ is the generation of the $j$ th hydro unit in the $m$ th subinterval. $P_{D m}$ is the total electric power demand in the $m$ th subinterval and $P_{L m}$ is the real power loss in transmission in the $m$ th subinterval, which is defined as follows [23]:
$P_{L m}=\sum_{l=1}^{N e+N h / N e+N h} P_{l m} B_{l r} P_{r m}$.
Here, $B$ is the loss formula coefficients matrix.

### 2.2.2. Water availability constraints

$\sum_{m=1}^{M} t_{m}\left(a_{0 h j}+a_{1 h j} P_{h j m}+a_{2 h j} P_{h j m}^{2}\right)-W_{h j}=0 \quad j=1, \ldots, N_{h}$,
where $a_{0 h j}, a_{1 h j}$ and $a_{2 h j}$ are coefficients for water discharge rate function of the $j$ th hydro unit. $B_{-} r$ is the volume of water available for generation by $j$ th hydro generator during the scheduling period.

### 2.2.3. Generation limits

For stable operation, the output of each generator is restricted by lower and upper limits:
$P_{h j m}^{\min } \leq P_{h j m} \leq \quad P_{h j m}^{\max } \quad$,
$P_{s i m}^{\min } \leq P_{s i m} \leq \quad P_{s i m}^{\max } \quad$,
where $P_{h j m}^{\min }$ and $P_{h j m}^{\max }$ are the minimum and maximum generation limits of the $j$ th hydro unit, respectively. $P_{s i m}^{\max }$ is the maximum generation limits of the $i$ th thermal generator.

### 2.3. Formulation

Aggregating the objectives and constraints, the EED of HPS multiobjective optimization problem can be mathematically formulated as
$\underset{\text { Subject to }}{\text { Minimize }} \quad[F 1(P), \quad F 2(P)]$
$\left\{\begin{array}{l}g(P)=0 \\ h(P) \leq 0\end{array}\right.$

where $P$ indicates the load dispatch scheme, $g$ is the equality constraint representing the power balance and water available, while $h$ is the inequality constraint representing the generation capacity.

## 3. Constraint handling

It is worth noting that the performance of an MOEA in tackling multisbjective constrained optimization problems may be largely dependent on the constraint handling technique used as well as the search algorithm. As we mainly focus on the performance of the search techniques in this paper, we adopt the same constraint handling strategy for all the algorithms.

The constrained-domination strategy [10] is used to handle constraints in this study. A solution $a$ is said to constrained-dominate a solution $b$, if any of the following conditions is true: (1) solution $a$ is feasible and solution $b$ is not; (2) solutions $a$ and $b$ are both infeasible, but solution $a$ has a smaller overall constraint violation; (3) solutions $a$ and $b$ are feasible and solution $a$ dominates solution $b$. The effect of using this constraints handling technique is that all feasible solutions has a better sort rank than any infeasible solution and infeasible solution with a smaller constraint violation has a better rank than one with a lager constraint violation.

According to the constraints in the EED of HPS problem, a penalty function is employed in this study to compute the constraint violation as follows:

$$
\begin{aligned}
S= & \sum_{m=1}^{M}\left|\sum_{i=1}^{N_{x}} P_{s i m}+\sum_{j=1}^{N_{b}} P_{h j m}-P_{D m}-P_{L m}\right| \\
& +\sum_{j=1}^{N_{b}}\left|\sum_{m=1}^{M} t_{m}\left(a_{0 j}+a_{1 j} P_{h j m}+a_{2 j} P_{h j m}^{2}\right)-W_{j}\right|
\end{aligned}
$$

## 4. IRM-MEDA

Offspring producer plays a vital importance role in any MOEA. It is an underlying assumption that good solutions have similar structure. This is also reasonable for most real world problems. Based on this assumption, an ideal offspring generator should be able to produce a solution that is close to the best solutions found so far. As only a few parent solutions are directly involved in most conventional generation operations, such as crossover and mutation, a new solution created by these strategies may be far from other best solutions found so far in the search [24]. EDAs instead, they generate new solutions by sampling from a probability distributions model which serve as the vehicle to capture the data dependencies and the data structure as well. But there is no mechanism in EDAs for directly using the location information of the best solutions.

In this study, local learning is incorporated into RM-MEDA [13] to efficiently overcome this shortcoming of EDAs. As local learning directly uses the location information of some perfect solutions to generate new solutions, the evolution process is accelerated and the local search ability is improved in our approach, IRM-MEDA. The details of the proposed method will be discussed in this section, we will first give the procedure of this algorithm in Fig. 1, the mainly steps will be further studied followed.

The major elements of IRM-MEDA are presented as follows.

### 4.1. Initialization

In a hydrothermal power system which includes $N_{h}$ hydroelectric units and $N_{t}$ thermal units, the structure of a solution $x(t)$ for hydrothermal scheduling problem is composed of a set of decision

Procedure:
Step1: Initialize $X(t),) X(t) \mathrm{i}=N, \mathrm{t}=0$.
Step2: Repair infeasible solutions in $X(t)$.
Step3: Evaluate $X(t)$.
Step4: If the number of nondominated solutions $p$ satisfies $2 \leq p \leq N / 2$, then go to step5. Otherwise, $\theta=0$, go to step6.
Step5: Generate $N \times \theta$ new individuals by local learning reproduction, merge these new individuals into $Q(t)$.
Step6: Build the probability mode of $X(t)$ and Sample $N \times(1-\theta)$ individuals from the probability model, merge these new individuals into $Q(t)$.
Step7: Repair infeasible solutions in $Q(t)$ and evaluate it.
Step8: Select $N$ solutions from $X(t) \cup Q(t)$ to create $X(t+1)$, tot +1 .
Step9: If the step condition is satisfied, then output the nondominated solutions from $X(t+1)$, otherwise go to Step3.

Fig. 1. The procedure of IRM-MEDA.
variables which represent the hydro and thermal generations during the $M$ subintervals.
$x(t)=[P 1, P 2, \ldots, P M]$
In Eq. (10), $P m=\left[P_{s 1 m}, P_{s 2 m}, \ldots, P_{s N_{t} m}, P_{h 1 m}, P_{h 2 m}, \ldots, P_{h N_{b} m}\right]$, $m=1, \ldots, M$. Thus, the dimension of a solution is equal to $\left(N_{t}+N_{b}\right) M$. During the initialization process, the element of each solution $x(t)$ is initial using the Latin Hypercube sampling method firstly within the feasible range defined by Eqs. (6) and (7). Then, for each solution $x(t)$, we define $S_{n}(t)$ as the penalty function of $x(t)$, the equation is as follow (Fig. 2):
$S_{n}(t)=S 1+S 2$
$S 1=\sum_{m=1}^{M}\left|\sum_{i=1}^{N_{x}} P_{s i m}+\sum_{j=1}^{N_{b}} P_{h j m}-P_{D m}-P_{L m}\right|$
$S 2=\sum_{j=1}^{N_{b}}\left|\sum_{m=1}^{M} t_{m}\left(a_{0 h j}+a_{1 h j} P_{h j m}+a_{2 h j} P_{h j m}^{2}\right)-W_{h j}\right|$

### 4.2. Repairing

For each infeasible solution, a repair operation is performed. First, the water availability constraints are considered, the hydro unit generation $\left(P_{h j m}\right)$ is adjusted to meet the constraints. Then, the thermal unit generation $\left(P_{s i m}\right)$ is amended to satisfy the power balance constraints.

### 4.2.1. Water availability constraints

We assume that the generation value $\left(P_{h j n}\right)$ of the $j$ th hydro unit during subinterval $u$ is an unknown $y$ to be calculated, other $P_{h j m}$, $m=1, \ldots, M, m \neq u$ are fixed as they are in the solution $x(t)$. We can find $y$ by solving the follow quadratic equation:

Adopt the Latin Hypercube Sampling method to initial $x(t)$
For each individual $x(t)=\left[P 1, P 2, \ldots, P M\right]$
If $x_{n}(t)=0: x(t)$ is feasible solution, go to step3 of the IRM-MEDA procedure in Fig. 1.
Else: go to step2 of the IRM-MEDA procedure in Fig. 1 to repair the infeasible solution.
End if
End for
Fig. 2. The initialization procedure of IRM-MEDA.

$$
\begin{aligned}
& y^{2}+\frac{a_{1 N_{1}}}{a_{2 N_{2}}} y+\frac{-W_{N_{2}}+a_{0 N_{2}} \sum_{m=1}^{M} t_{m}+\sum_{m=1}^{M} t_{m+1} \frac{f_{m} a_{1 N_{2}} P_{N m}}{P_{N_{2}} a_{2 N_{2}}} \\
& =0
\end{aligned}
$$

As $a_{1 N_{2}} / a_{2 N_{2}}$ is always positive, only one root can be positive. If this positive root locates within $\left[\begin{array}{ll}p_{\text {Nim }}^{\min } & p_{\text {Nim }}^{\max }\end{array}\right]$, this repair procedure is successful for the $j$ th hydro unit and we accept this root as $P_{N m}$. The above repair mechanism is performed for all $N_{h}$ hydro units. If the repair procedure for all $N_{h}$ hydro units is successful, then the power balance constraints are taken into account followed. Otherwise, this solution is declared as infeasible and no further consideration of power balance constraints.

### 4.2.2. Power balance constraints

The similar repair process as above is adopted to handle the power balance constraint. For each subinterval $m$, all the $N_{h}$ hydro units generation is known and we assume that one of the $N_{s}$ thermal units generation $\left(P_{s u m}\right)$ is an unknown $y$, so the power balance constraint can be written as

$$
\begin{aligned}
& B_{u n} y^{2}+\left(2 \sum_{l=1}^{N_{s}+N_{h}-1} B_{u l} P_{l m}-1\right) y+P_{0 m} \\
& \quad+\sum_{i=1}^{N s+N h-1 N s+N h-1} P_{i m} B_{i l} P_{j m}-\sum_{i=1}^{N_{s}-1} P_{s i m}-\sum_{j=1}^{N_{h}} P_{h j m}=0
\end{aligned}
$$

If the solved $y$ comes within $P_{\text {sum }}^{\min }$ and $P_{\text {sum }}^{\max }$, then this value is accepted and we go to next constraint involving the next time subinterval. Otherwise, another root-finding equation is tried for the next thermal unit. If the replacement for all $M$ subintervals is unsuccessful, this solution is declared infeasible and a penalty is computed by Eq. (9).

### 4.3. Local learning

In IRM-MEDA, local learning strategy is adopted to obtain new individuals by using the location information of nondominated solutions in the present population. The procedure of local learning is as follows: (1) randomly choose a nondominated individual $a$ from the population $X(t)$; (2) the individual $b$ with the minimal distance with $a$ in the objective space is selected; (3) uniformly sample five individuals from the [low, upp] by LHS method [25], where
$\operatorname{low}(i)=\min (a(i), b(i)), \quad i=1, \ldots,\left(N_{s}+N_{h}\right) M$,
$\operatorname{upp}(i)=\max (a(i), b(i)), \quad i=1, \ldots,\left(N_{s}+N_{h}\right) M ;$
(4) select a best solutions from those five individuals as a new individual generated by local learning. The local learning operation is repeated until there are $N \times \theta$ new individuals are generated.

### 4.4. Modeling and sampling

The modeling and sampling methods used in this improved algorithm are the same as in RM-MEDA [13]. Under certain smoothness conditions, it can be induced from the Karush-Kuhn-Tucker condition that the Pareto-optimal set (PS) of a continuous MOP is a ( $m-1$ )-D piecewise continuous manifold in decision space [26,27]. The probability model is build base on this regularity.

In an MOEA, it is desired that the solution set in decision space can approximate the PS as close as possible and at the same time, can locate around the PS. So the solution in the population can be supposed as an independent observation of a random vector whose
central is the PS. As the PS is a ( $m-1$ )-D piecewise continuous manifold, $\xi$ can be described as
$\xi=\varsigma+\varepsilon$
where $\varsigma$ is uniformly distributed over the manifold, and $\left|P^{*}\right|$ is an n-dimensional zero-mean noise vector.

### 4.4.1. Modeling

We first divide the population into K disjoint clusters $S^{1}, S^{2}, \ldots$, $S^{K}$ by the ( $m-1$ )-D Local PCA [28] approach. Then, for each cluster $S^{j}$, build its model $\psi^{j}$ as follows:
$a_{i}^{j}=\min _{x \in S^{j}}\left(x-\hat{x}^{j}\right)^{\top} U_{i}^{j}, \quad i=1, \ldots, m-1$
$b_{i}^{j}=\max _{x \in S^{j}}\left(x-\hat{x}^{j}\right)^{\top} U_{i}^{j}, \quad i=1, \ldots, m-1$
$\psi^{j}=\left\{x \in R^{n} \mid x=\hat{x}^{j}+\sum_{i=1}^{m-1} a_{i} U_{i}^{j}, a_{i}^{j}-0.25\left(b_{i}^{j}-a_{i}^{j}\right) \leq \alpha_{i} \leq b_{i}^{j}+0.25\left(b_{i}^{j}-a_{i}^{j}\right)\right\}$
where $\hat{x}^{j}$ is the mean of cluster $|P(t+1)|<N$ and $U_{i}^{j}$ is the $i$ th principal component of $|P(t+1)|<N . \lambda_{i}^{j}$ is the $i$ th largest eigenvalue of the covariance matrix of the points in $|P(t+1)|<N$. Then compute
$v o l\left(\psi^{j}\right)=\prod_{i=1}^{m-1}\left(b_{i}^{j}-\sigma_{i}^{j}\right)$
and
$\sigma_{j}=\frac{1}{n+m-1} \sum_{i=m}^{n} \lambda_{i}^{j}$.

### 4.4.2. Sampling

In order to uniformly sample the new solutions around the PS, the number of new trial solutions generated by each $\Psi^{j}$ is proportion to its volume $v o l\left(\psi^{j}\right)$. The reproduction by sampling includes three steps: (1) randomly generate an integer $t \in\{1,2, \ldots, K\}$ with $\operatorname{Prob}(t \neq j)$,
$\operatorname{Prob}(t \neq j)=\frac{v o l\left(\psi^{j}\right)}{\sum_{j=1}^{K} v o l\left(\psi^{j}\right)}$
(2) randomly sample a point $x^{\prime}$ from $\Psi^{j}$ and generate a noise $\varepsilon^{\prime} \sim N(0$, $\sigma_{j} l) ;(3)$ the new trial solution is $x=x^{\prime}+\varepsilon^{\prime}$.

### 4.5. Selection

Selection is performed to compare the constraint violation and fitness function value of two competing solutions. In the procedure of selection, constraint-domination is used in the evaluation of two solutions. For a set of solutions, the fast nondominated sort approach used in NSGA-II [10] is employed to sort solutions in our proposed method.

## 5. Experiment results and discussion

In this section, the EED of HPS problem is considered to assess the effectiveness of IRM-MEDA. This test system 1 includes two hydro units and four thermal units and test system 2 comprises of two hydro plants and two thermal plants, whose characteristics are the same as those in Refs. [8,14,16]. In detail, it can be seen in Tables A1 and A2 in Appendix I, respectively.

### 5.1. Compared algorithms and parameter settings

To identify the improvement due to the local learning strategy and the solution generation technique in IRM-MEDA, we firstly execute three MOEAs including RM-MEDA, NSGA-II and NNIA to tackle this complex problem. Then, a comparison of IRM-MEDA with two previous reported methods [8], [9] is presented followed. For fair comparison among the developed algorithms, ten different optimization runs are carried out for each approach.

In all the simulation runs, the population size is fixed at 100. The number of fitness function evaluation is taken as the terminal criterion which is restricted to 15,000 for all experiments performed. Crossover and mutation probabilities used in NSGA-II are chosen as 0.9 and 0.01 , respectively. In NNIA, the maximum size of dominant population $\left(n_{D}\right)$, the maximum size of active population $\left(n_{A}\right)$ and the size of clone population $\left(n_{C}\right)$ are fixed as 100, 20 and 20 respectively. Crossover and mutation probabilities are chosen as 1 and 0.01 , respectively. In RM-MEDA and IRM-MEDA, the number of cluster, $K$, used in Local PCA algorithm is set to be 5 . The proportional coefficient $\theta$ in IRM-MEDA is set to be 0.1 and 0.2 for test system 1 and test system 2 respectively.

### 5.2. Performance metric

Generally, the definition of quality in the case of multiobjective optimization is substantially more complex than for single objective optimization. To efficiently evaluate the approximation set attained by these different algorithms, two performance indicators are employed:

### 5.2.1. Hypervolume indicator $I_{H}(A)[29]$

This indicator measures the hypervolume of the portion of objective space that is weakly dominated by an approximation set $A$, and is to be maximized. In order to measure this quantity, the objective space must be bounded, if it is not, then a bounding reference point that is dominated by all solutions should be used. In our experiment, the reference point is formed by combining the maximum value of each objectives searched in all the optimization runs.

### 5.2.2. Coverage of two sets [30]

Let $A, B$ be two approximate Pareto-optimal sets. The function maps the ordered pair $(A, B)$ to the interval $[0,1]$ :
$I_{C}(A, B)=\frac{|\{b \in B ; \exists a \in A: a \geq b\}|}{|B|}$
where $\geq$ means dominate or equal (also called weakly dominate). The value $I_{C}(A, B)=1$ means that all decision vectors in $B$ are weakly dominated by $A . I_{C}(A, B)=0$ implies no decision vector in $B$ is weakly dominated by $A$. Note that both directions always have to be considered because $I_{C}(A, B)$ is not necessarily equal to $1-I_{C}(B, A)$.

### 5.3. Parameter study

In IRM-MEDA, There is a parameter need to be fixed in the procedure of local learning reproduction. The proportional coefficient $\theta$ represents the number of solutions generated by local learning. Local learning can help the population attain the regularity early and converge faster. However, if unsuitable $\theta$ are selected, the population may fall into the local optimal. So a proper selection of $\theta$ is important. Here, we study the effect of the variation of $\theta$ from 0 to 0.5 on the EED of HPS problem in term of the average $I_{H}$ in 10 runs.

As clearly shown in Figs. 3 and 4, IRM-MEDA can get a larger $I_{H}$ value when $\theta$ is 0.1 in test system 1 and 0.2 in test system 2. Therefore, for test system 1 and test system 2, we set $\theta=0.1,0.2$ for all the IRM-MEDA optimization runs in our experiment, respectively.
![img-0.jpeg](img-0.jpeg)

Fig. 3. The average $I_{H}$ values of system 1 under the different settings of the proportional coefficient.

### 5.4. Comparative study

### 5.4.1. Compared with MOEAs

First, hypervolume $I_{H}$ is adopted to measure the performance of the diversity and extent of the nondominated solutions. The Paretooptimal fronts with the maximum $I_{H}$ obtained by each technique out of ten runs are presented in Figs. 5-10. The Pareto-optimal fronts of IRM-MEDA has been compared with RM-MEDA, NINA, NSGA-II, It is clear that all the attained Pareto-optimal fronts have good diversity characteristic of nondominated solutions. This indicates the EED of HPS problem can be efficiently solved by these techniques.

The selection of reference point selection for each test system has a significant impact on the $I_{H}$ value. In our experiment, the joint reference point is formed by combining the maximum value of each objectives search in all the optimization runs. In detail, we set $2.9 \times 10^{4}, 9.0 \times 10^{4}$ and $10 \times 10^{4}, 750$ as the reference point for the test system 1 and system 2 respectively. For the simplicity of the comparative study, we normalize the $I_{H}$ to the interval $[0,1]$.

For further studying the extent characteristic of these techniques, the average value of $I_{H}$ over ten different optimization runs
![img-1.jpeg](img-1.jpeg)

Fig. 4. The average $I_{H}$ values of system 2 under the different settings of the proportional coefficient.

![img-6.jpeg](img-6.jpeg)

Fig. 5. Pareto-optimal fronts of test system 1 with the maximum $I_{H}$ value obtained by IRM-MEDA and RM-MEDA.
![img-7.jpeg](img-7.jpeg)

Fig. 6. Pareto-optimal fronts of test system 1 with the maximum $I_{H}$ value obtained by IRM-MEDA and NSGA-II.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Pareto-optimal fronts of test system 1 with the maximum $I_{H}$ value obtained by IRM-MEDA and NNIA.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Pareto-optimal fronts of test system 2 with the maximum $I_{H}$ value obtained by IRM-MEDA and RM-MEDA.
![img-6.jpeg](img-6.jpeg)

Fig. 9. Pareto-optimal fronts of test system 2 with the value obtained by IRM-MEDA and NINA.
![img-7.jpeg](img-7.jpeg)

Fig. 10. Pareto-optimal fronts of test system 2 with the value obtained by IRMMEDA and NSGA-II.

Table 1
The average $I_{H}$ value obtained by each technique in ten runs of test system 1 .
Table 2
The average $I_{H}$ value obtained by each technique in ten runs of test system 2 .
![img-8.jpeg](img-8.jpeg)

Fig. 11. Box plot of the $I_{H}$ values obtained by IRM-MEDA, RM-MEDA, NNIA and NSGA-II of test system 1.
is listed in Tables 1 and 2. The box plot of this measure value is also given in Figs. 11 and 12.

It can be learned from Tables 1 and 2 that the objective space size dominated by IRM-MEDA is larger than other techniques for both test system 1 and test system 2. And NSGA-II performs worst in this indictor.

For test system 1, the performance of RM-MEDA is better than NSGA-II while worse than NNIA and IRM-MEDA. The objective space size covered by NNIA is little smaller than that of IRM-MEDA. For test system 2, although RM-MEDA works better than NINA and NSGA-II. Our improved IRM-MEDA performs much better than RMMEDA. This could be attributed to the fact that IRM-MEDA can learn the information about these useful solutions, which can be used to create offspring solutions.

From the results obtained above, we conclude that the extent and diversity of IRM-MEDA outperforms other three MOEAs.

On the other hand, the coverage of two sets metric measure for comparing the convergence characteristics of these four MOEAs has been examined in this study of two systems. Tables 3 and 4 represent the average value of $I_{C}$ over ten different runs. Figs. 13 and 14 illustrate the results of this measure using box plots. In the following, " 1 " denotes the solution set obtained by IRM-MEDA, " 2 " denotes the solution set obtained by RM-MEDA, " 3 " and " 4 " denotes the solution set obtained by NNIA and NSGA-II, respectively.
![img-9.jpeg](img-9.jpeg)

Fig. 12. Box plot of the $I_{H}$ values obtained by IRM-MEDA, RM-MEDA, NNIA and NSGA-II of test system 2.

Table 3
Coverage of two sets obtained by MOEAs of system 1.

For test system 1, it can be known from Table 3 that the nondominated solutions of IRM-MEDA are barely covered. Only approximately $1.2 \%, 1.3 \%$ and $4.9 \%$ nondominated solutions of IRM-MEDA are covered by those of RM-MEDA, NSGA-II and NNIA, respectively. While, more than $80 \%$ nondominated solutions obtained by these three techniques are weakly dominated by those of IRM-MEDA. We estimate that IRM-MEDA has superiority over other three search algorithms in this problems as far as the coverage is concerned because the box plots of $I_{C}(1, B)$ are higher than the corresponding box plots of $I_{C}(B, 1)$, where $B \in(2,3,4)$.

Meanwhile, for the test system 2, it is clear from Table 4 that, in terms of $C$-metric, the coverage of non-dominated solutions of IRMMEDA are littleness, taking $C(1,2), C(2,1)$ as an example, on average, only $9.4 \%$ non-dominated solutions of IRM-MEDA are covered by those of RM-MEDA and vice versa. What need especially alludes is, NINA shows better results in terms of $I_{H}$ than those of NSGA-II, however, the $I_{C}$ obtained by NINA is strongly worse than NSGA-II. NINA performs not very well as in test system 1.

It can be learned from the above results that RM-MEDA performs better than NSGA-II in terms of $I_{H}$ and $I_{C}$. RM-MEDA is different from NSGA-II only in its individual generation in heuristic search, therefore, the better performance of RM-MEDA in contrast to NSGA-II results from the unique model-sampling solution generation in RM-MEDA, which is also used in IRM-MEDA. This generation mechanism can improve the ability of discovering compared to traditional individual production.

However, as the population has no obvious regularity at the start of iteration, solutions produced by RM-MEDA are always poor at that time, which makes the population converges very slowly. Fig. 11 shows that RM-MEDA performs worse than NNIA in terms of $I_{H}$ in system 1. Nevertheless, IRM-MEDA outperforms NNIA in both of these two indicators. This is mainly due to the local learning mechanism which effectively uses the location information of good solutions found to create solutions. Local learning in IRMMEDA can enhance the local search ability and make the population attain regularity early, so that a faster convergence is achieved.

### 5.4.2. Compared with previous methods

A comparison of IRM-MEDA with two reported methods [8,9] is discussed in this section. In Ref. [8], a simulated annealing procedure was used to solve the EED of HPS problem. An improved genetic algorithm cooperated with the multiplier updating technique (IGA-MU) was employed for solving the same problem in Ref. [9].

Table 4
Coverage of two sets obtained by MOEAs of test system 2.

![img-10.jpeg](img-10.jpeg)

Fig. 13. Box plots of the coverage of two sets obtained by MOEAs of test system 1.
![img-11.jpeg](img-11.jpeg)

Fig. 14. Box plots of the coverage of two sets obtained by MOEAs of test system 1.

Table 5
Optimally scheduling generations of SA, IGA-MU and the proposed IRM-MEDA for the best emission.

Nondominated solutions obtained by methods in Ref. [8,9] are drawn out with those of IRM-MEDA in Fig. 15. The result reveals that the Pareto-optimal front obtained by IRM-MEDA dominated most of the solutions obtained in the previous study. Furthermore, as these previous methods all converted this multiobjective
optimization problem to a single optimization problem, only one solution can be presented in a single run.

The best emission solutions and the cost solutions obtained by IRM-MEDA in the run with the maximum $I_{\mathrm{ff}}$ are compared with those of techniques in Ref. [8,9]. Results are shown in Tables 5 and 6 .

Table 6
Optimally scheduling generations of SA, IGA-MU and the proposed IRM-MEDA for the best cost.

![img-12.jpeg](img-12.jpeg)

Fig. 15. Pareto-optimal solutions obtained by IRM-MEDA and previous methods.
In the above tables, $S$ indicates the constraint violation. It is clear that the constraint violation of solutions attained by IRM-MEDA and IGA-MU are less than 0.1. While those of SA are approximate 10, which may be unacceptable.

## 6. Conclusion

In this paper, a novel approach based on multi-objective estimation of distribution algorithm (IRM-MEDA) has been proposed to
solve economic emission load dispatch of hydrothermal power system. The problem has been formulated with conflicting objectives and was subject to numbers of equality and inequality constraints. The proposed method added a local learning procedure into RMMEDA so that the local search ability and convergence efficiency could be enhanced. The optimization runs indicate that IRM-MEDA outperforms in this problem. In this paper fixed water head is assumed. With further consideration of variable water head the problem becomes more complicated. To resolve the variable head hydrothermal problem by the proposed method, some endeavors still have to be and which is worth continuing to work in the future.

## Acknowledgments

This work was supported by the Program for New Century Excellent Talents in University (No. NCET-12-0920), the Program for New Scientific and Technological Star of Shaanxi Province (No. 2014KJXX-45), the National Natural Science Foundation of China (Nos. 61272279, 61272282, 61001202 and 61203303), the Fundamental Research Funds for the Central Universities (Nos. K5051302049, K5051302023, K50511020011, K5051302002 and K5051302028), the Provincial Natural Science Foundation of Shaanxi of China (No. 2011JQ8020), the Fund for Foreign Scholars in University Research and Teaching Programs (the 111 Project) (No. B07048) and EU IRSES Project (No. 247619).

## Appendix I.

Table A1
Test system 1 parameters data.

Table A2
Test system 2 parameters data.
