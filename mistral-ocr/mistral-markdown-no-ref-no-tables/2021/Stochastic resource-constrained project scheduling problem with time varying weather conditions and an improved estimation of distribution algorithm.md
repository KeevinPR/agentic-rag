# Stochastic resource-constrained project scheduling problem with time varying weather conditions and an improved estimation of distribution algorithm 

Yifan Zhou ${ }^{\mathrm{a}, *}$, Jindan Miao ${ }^{\mathrm{a}}$, Bin Yan ${ }^{\mathrm{b}}$, Zhisheng Zhang ${ }^{\mathrm{a}}$<br>* School of Mechanical Engineering, Southeast University, Nanjing 21100, PR China<br>${ }^{\text {a }}$ Beijing Goldwind Science \& Creation Windpower Equipment Co., Ltd, Beijing 100176, PR China

## A R T I C L E I N F O

Keywords:
SRCPSP
Estimation of distribution algorithm
Ranking and selection
Common random numbers

## A B STR A CT

Construction projects with outdoor operations are affected by time-varying weather conditions. However, most existing research on stochastic resource-constrained project scheduling problems (SRCPSPs) considers activity duration as a random variable from a time-independent distribution. To address this issue, this study investigates SRCPSP under time-varying weather conditions; an improved estimation of distribution algorithm (EDA) including a ranking and selection method using common random numbers is proposed for enhancing the performance of project scheduling. The benchmark J120 dataset from PSPUB and a practical case of windfarm construction are used to validate the improved EDA. For three randomly selected cases from the J120 dataset, the improved EDA can reduce the expected makespan by $17.0,29.4$, and 12.5 days when compared with deterministic scheduling. The corresponding makespan reductions obtained by the original EDA are $10.8,22.7$, and 7.1 days. Similarly, the improved EDA obtains $23 \%$ higher expected makespan reduction for the practical case.

## 1. Introduction

Weather conditions are one of the most important factors affecting outdoor activities; for example, most activities in a windfarm construction project cannot be executed during rainy and windy weather. Therefore, it is practically significant to consider uncertain weather conditions for project scheduling. Weather conditions change with the seasons, and therefore, the durations of activities executed outdoors are time-dependent random variables that have rarely been considered in existing research. To the best of our knowledge, Huang and Ding (2011) considered activity durations to be both random and time dependent. They scheduled a software project without including resource constraints. To bridge this research gap, this study investigates an SRCPSP under time-varying weather conditions using an improved EDA.

According to Herroelen and Leus (2005), three approaches can address uncertainties in the SRCPSP: proactive scheduling, reactive scheduling, and stochastic scheduling. Among these, proactive scheduling aims to obtain a baseline schedule that can absorb variability during project execution; this variability includes the uncertainty of activity durations and resources. Lamas and Demeulemeester (2016) generated a proactive scheduling procedure using a branch-and-cut
method wherein new robustness measures were proposed. Bruni, Beraldi, and Guerriero (2015) developed a chance-constrained-based heuristic algorithm to derive the baseline schedule of an SRCPSP and illustrated a practical case study of student apartment construction. Reactive scheduling is used to repair or reformulate the baseline schedule when the initial schedule is infeasible (Deblaere, Demeulemeester, \& Herroelen, 2011). Proactive and reactive scheduling methods are often used together through a combined cost function for the baseline schedule and reactions during execution (Davari \& Demeulemeester, 2019). The third approach is stochastic scheduling, where the duration of an activity is regarded as a random variable. The result of stochastic scheduling is no longer a definite plan; instead it is a scheduling policy that decides how to schedule activities dynamically in each possible scenario. Stochastic scheduling was adopted in this research.

Stochastic scheduling can be divided into exact evaluation and simulation-based methods according to the method employed for evaluating the objective function (Rostami, Creemers, \& Leus, 2018). The exact evaluation method is largely based on Markov analysis. Creemers (2015) developed backward stochastic dynamic programming to solve SRCPSP with exponential and phase-type distributed activity durations; Markov analysis was used to evaluate the objective function. Owing to

[^0]
[^0]:    a Corresponding author.
    E-mail address: yifan.zhou@seu.edu.cn (Y. Zhou).


$N_{\max } \quad$ Largest number of scenarios to evaluate an individual during the EDA
$P_{p p r}$ Probability to alter the execution order of an activity during local search
$Q \quad$ Number of elite individuals
$r_{j, k} \quad$ Demand of resource $k$ by activity $j$
$R_{k} \quad$ Total amount of resource $k$
$S_{j} \quad$ Start time of activity $j$
$T \quad$ Planning horizon
$u_{y, t} \quad$ Binary indicator of workable weather condition at time $t$ in years
$w(t) \quad$ Workable probability of day $t$
$\eta \quad$ Proportion of elite individuals in the whole population
$\Phi_{j, t} \quad$ Probability distribution of the duration of activity $j$ starting fromt
$\Phi_{j, t}^{-1}(\cdot) \quad$ Inverse cumulative distribution function of distribution $\Phi_{j, t}$
$A_{t} \quad$ Set of activities that are in execution at time $t$
$P_{j} \quad$ Set of precedence activities of activity $j$
$\psi \quad$ Set of activities which have been scheduled
$\chi \quad$ Eligible set containing unscheduled activities whose predecessors have all been scheduled
$\Omega \quad$ Set of individuals in the EDA
Decision variables
$\lambda=\left\{a_{0}, a_{1}, \cdots, a_{J-1}\right\}$ Execution order of activities
$a_{m} \in\{0,1, \cdots, J+1\}$ Index of $m^{\text {th }}$ activity in vector $\lambda$
$\tau \quad$ Start time of a project
$\pi=[\lambda, \tau]$ Solution of SRCPSP
the memory bottlenecks, the approach proposed by Creemers (2015) was effective for small and medium problems (up to 62 activities). Creemers, Leus, and Lambrecht (2010) solved an SRCPSP to maximise the net present value (NPV) by adopting Markov analysis. Rostami et al. (2018) proposed an exact evaluation method based on Markov analysis to solve SRCPSP with exponentially distributed activity durations. The above-mentioned literature indicates that the exact evaluation method is appropriate for only small and medium SRCPSPs.

A simulation-based method is effective for processing large-scale problems. Ballestín and Leus (2009) developed a greedy randomised adaptive search procedure to solve the SRCPSP. The numerical study showed that generating 10 scenarios for each solution could help identify considerably better results than applying a larger number of scenarios; this is consistent with the conclusion of Ballestín (2007). Rostami et al. (2018) developed a two-phase metaheuristic algorithm that includes a greedy randomised adaptive search procedure and a genetic algorithm (GA) to search for a high-quality scheduling policy. Further, they adopted a descriptive sampling method to reduce the variance in activity durations in different scenarios.

The EDA is a commonly used heuristic approach in project scheduling and related areas (Jarboui, Eddaly, \& Siarry, 2009; Shi et al., 2019; Tian, Hao, \& Gen, 2019). Unlike the classical GA, the EDA builds an explicit distribution model to select individuals during recombination, and this results in a stronger global searching ability. Wang and Fang (2012) adopted the EDA to solve a multimode project scheduling problem with the aim of minimising the makespan. The effectiveness of the EDA was investigated using benchmark cases. Hao, Sun, and Gen (2018) developed a new EDA hybridised with the GA for robust project scheduling. A scenario-based simulation was used to measure the robustness. Fang, Kolisch, Wang, and Mu (2015) applied the EDA to solve SRCPSP, and the Taguchi experimental design method was adopted to identify the best combination of parameters in the EDA. In
addition, the EDA was used and improved in this study to solve SRCPSP.
Most existing studies treated the search of the optimal solution and the evaluation of objective functions as two independent processes when solving SRCPSP via simulation (Bruni, Beraldi, Guerriero, \& Pinto, 2011; Chen, Demeulemeester, Bai, \& Guo, 2018; Tao, Wu, Sheng, \& Wang, 2018). In these studies, different solutions received the same simulation efforts, and unnecessary replications were generated for solutions with low quality. Chen (2016a) found that generating the realisations of objective functions is the most time-consuming part during optimisation via simulation. Therefore, the optimisation efficiency can be enhanced by appropriately allocating the simulation efforts to different solutions. Choi and Kim (2018) developed a robust and efficient R\&S algorithm by allocating limited simulation resources. Gao, Shi, Gao, and Xiao (2019) investigated the problem of selecting the optimal subset, and a simulation budget allocation rule was proposed using the large deviation theory. The common random number (CRN) is a simulation technique for variance reduction, which compares different individuals under similar circumstances. Individuals are evaluated using positively correlated inputs (Chen, 2016b). Kesur (2009) optimised traffic signals using GA where the CRN was used to reduce the variance in the simulation. Hedlund and Mollaghasemi (2001) applied the CRN method to GA. A two-step indifference-zone R\&S method was employed to determine the number of replications simulated for each solution. A recent study by Nazzal, Mollaghasemi, Hedlund, and Bozorgi (2012) provided a more comprehensive introduction of the methodology of Hedlund and Mollaghasemi (2001).

References that combined heuristic algorithms and simulation-based methods are summarised in Table 1. These references were selected from the project scheduling and related areas. Table 1 shows that the R\&S and CRN methods have not been used for project scheduling. Studies that embedded both R\&S and CRN into heuristic algorithms are also limited. The two most related papers (Hedlund \& Mollaghasemi, 2001; Nazzal

Table 1
References that combine heuristic algorithms with simulation-based methods.
et al., 2012) adopted both the R\&S and CRN in GA. The two studies used the R\&S method to identify the number of replications for a solution that guarantees the probability of correct selection. However, the same number of replications were generated for different solutions in an iteration of the GA, and the unnecessary simulation of inferior solutions was not avoided.

According to the above literature review, the combination of the R\&S and CRN methods with heuristic algorithms has not received the necessary attention, especially in project scheduling. Thus, this study develops an improved EDA to solve SRCPSPs where an R\&S procedure based on the CRN is utilised to select elite solutions. Through this procedure, promising solutions receive more simulation effort than other low-quality solutions. In the investigated SRCPSP, activity durations are time-dependent random variables, and both resource and precedence constraints are considered. The start date of a project is adopted as an additional decision variable during optimisation because the start date affects the makespan of the project when the distributions of activity durations are time-dependent. Numerical examples modified from benchmark instances in the J120 dataset of the PSPLIB are studied to validate the performance of the improved EDA. A practical case study of windfarm construction is analysed, and the results show that the improved EDA can effectively solve the SRCPSP under time-varying weather conditions.

The major contributions of this paper can be summarised as follows: (1) an R\&S method using the CRN is combined into the EDA; (2) Timedependent and random activity durations are considered in SRCPSP; and (3) a practical case about the construction of a windfarm is analysed.

The rest of this manuscript is organised as follows. Section 2 introduces the formulation and assumptions of the time-dependent SRCPSP. Section 3 proposes an optimisation model of time-dependent SRCPSP. The improved EDA including an R\&S procedure is developed in Section 4. Section 5 evaluates the performance of the improved EDA
using numerical examples modified from benchmark instances in the J120 dataset of PSPLIB. Finally, a practical case study of windfarm construction is presented in Section 6.

## 2. Problem formulation and assumptions

The SRCPSP can be regarded as scheduling a set of activities under precedence and resource constraints considering uncertainties. In this study, only the uncertainty of activity durations induced by weather conditions is considered, whereas other parameters (availability and amount of resources, precedence constraints, and execution mode of activities) are assumed to be determinate. There are $J+2$ activities in the project, i.e. $\{0,1, \cdots, J, J+1\}$. Activities 0 and $J+1$ are dummy activities that represent the start and end of the project, respectively. The duration of the two dummy activities is zero. The precedence constraint between activities $j$ and $\bar{j}$ is modelled by an indicator function $I(j, j)$. Activity $j$ is a predecessor of activity $j$ if $I(j, j)=1$. Then, $P_{j}=\{j \mid I(j, j)=1\}$ is the set of precedence activities of activity $j$. For simplifying the scheduling problem, it is assumed that the execution of an activity cannot be interrupted by another activity. There are $K$ types of renewable resources, and $R_{k}$ units of resource $k$ are available throughout the project. Activity $j$ needs $r_{j, k}\left(0 \leq r_{j, k} \leq R_{k}\right)$ units of resource $k$. The two dummy activities do not consume any resource, i.e. $r_{0, k}=r_{J+1, k}=0$ for $\forall k \in\{1,2, \cdots, K\}$. Unlike the deterministic problem, it is impossible to identify the exact start time $S_{t}$ and end time $E_{t}$ of activity $j$ caused by the influence of uncertain weather conditions. Therefore, the scheduling result is modelled as a scheduling policy $\pi=[\lambda, \tau]$. Vector $\lambda=\left[a_{0}, a_{1}, \cdots\right.$ $\left., a_{J+1}\right]$ represents the execution order of activities, where $a_{m} \in\{0,1, \cdots, J+1\}$ denotes the index of the $m^{\text {th }}$ activity. The first and last activities are two dummy activities, i.e. $a_{0}=0$ and $a_{J+1}=J+1$. The variable $\tau$ represents the start time of the project. The objective of scheduling is to identify a policy $\pi^{*}$ that incurs the shortest expected makespan or the largest expected NPV.

The activity durations in this study are influenced by time-varying weather conditions. Therefore, the distribution of the duration of activity $j$ depends on the start time of the activity given by
$d_{j, t} \sim \Phi_{j, t}, \forall j=1,2 \cdots J ; t=1,2, \cdots, T$.
Here, $d_{j, t}$ refers to the duration of activity $j$ that starts from $t$, and $\Phi_{j, t}$ is the corresponding probability distribution. Constant $T$ is the planning horizon.

```
Algorithm 1 Calculating durations of activity \(j\) starting at time \(t\) in different years
    Initialise \(D_{j, t}=\varnothing\)
    for \(y=1\) to \(Y\)
    Initialise the accumulative effective working time: \(\operatorname{count}=0\), the duration of
    activity \(j\) starting at day \(t\) in year \(y: d_{j, y t}^{0}=0\), and the time index \(t^{-}=t\)
        while count \(<d_{j}^{*}\left(d_{j}^{*}\right.\) is the standard duration of activity \(j)\)
        count \(=\operatorname{count}+u_{p, t} \cdot d_{j, j, t}^{0}=d_{j, j, t}^{0}+1\), and \(t^{-}=t^{-}+1\)
        end while
        \(D_{j, t}=D_{j, t} \cup d_{j, j, t}^{0}\)
    end for
```

Probability distribution $\Phi_{j, t}$ is fitted using the historical durations of activity $j$ starting at time $t$ in different years. The detailed steps for calculating the historical durations of activity $j$ are listed in Algorithm 1. The daily historical weather data for $Y$ years are available. In Algorithm $1, u_{p, t}$ denotes a binary indicator of workable weather conditions. When the weather of day $t$ in year $y$ is suitable for work, $u_{p, t}=1$; otherwise, $u_{p, t}=0$. Using the binary variables $u_{p, t}$, the probability that an activity

can be executed on day $t$ is calculated as
$w(t)=\left(\sum_{j=1}^{V} a_{j, t}\right) / Y, \forall t=1,2, \cdots, 365$.
After the set of historical durations $D_{j, t}=\left\{d_{j, t, t}^{H} \mid \gamma=1, \cdots, V\right\}$ is calculated using Algorithm 1, distribution $\Phi_{j, t}$ can be fitted to durations in $D_{j, t}$.

## 3. Optimisation model for time dependent SRCPSP

According to the formulation and assumptions of SRCPSP, decision variables of the scheduling problem include $a_{1}, a_{2}, \cdots, a_{J}$, and $\tau$. The start time of a project affects the makespan when the distribution of activity durations is time-dependent. Therefore, the start time $\tau$ of a project is a decision variable as well, and this is different from research that considers the time-independent distributions of activity durations.

Two objectives are considered in SRCPSP. The first objective is to minimise the expected makespan of the project given by $E\left(E_{J-1}(\pi)\right)-\tau$. The other objective is to maximise the expected NPV, which is the difference between the present values of cash inflows (incomes) and cash outflows (expenditures). The money earned in the future is less than that at present because of inflation and the benefits from investments. Consequently, all cash flows are discounted to the start time of the project to calculate the NPV. Inspired by Kerkhove and Vanhoucke (2017), the NPV of a project is calculated as
$N P V=\frac{C_{s n d}}{(1+I R)^{E_{J-1}}}-\sum_{j=1}^{J}\left[\frac{C_{j}^{f}}{(1+I R)^{S_{j}}}+\frac{C_{j}^{v}\left(E_{j}-S_{j}\right)}{(1+I R)^{E_{j}}}\right]$
Here, $C_{\text {end }}$ is the reward for completing the project, and this is acquired at the end of the project; $I R$ is the discount rate; and $C_{j}^{f}$ and $C_{j}^{v}$ are the fixed and variable costs of activity $j$, respectively. In a practical case study on windfarm construction, the expected makespan and expected NPV are both adopted as objective functions. In the numerical studies of instances modified from the J120 dataset, only the expected makespan is used as the objective function.

The mathematical model of the SRCPSP is formulated as
$\min E\left(E_{J-1}(\pi)\right)-\tau$
$\max E(N P V(\pi))$
Subject to
$S_{j} \geq \max _{j \in P_{j}} E_{j}, \forall j \in\{1,2, \cdots, J, J+1\}$
$\sum_{j \in \mathcal{S}_{j}} r_{j k} \leq R_{k}, \forall k \in\{1,2, \cdots, K\}, \forall t \in[1, T]$
$S_{j} \geq \max _{j \in \mathcal{S}_{j}} S_{j}, \forall j \in\{1,2, \cdots, J, J+1\}$
Inequality (6) represents the precedence constraints among activities, where the start time of activity $j$ cannot be earlier than the end times of its predecessors. Inequality (7) is a constraint on the resource, in which
$\lambda_{t}=\left\{j \mid S_{j} \leq t \leq E_{j}, j \in\{1,2, \cdots, J\}\right\}$
is the set of activities in execution at time $t$. Indeed, the amount of resource $k$ occupied by the activities in execution cannot be larger than $R_{k}$ at each time point. Inequality (8) is the constraint on the execution
order of the activities. Set $G_{j}$ contains activities whose execution order is before activity $j$ in $\lambda$.

The expected makespan and NPV cannot be calculated analytically because of the random activity durations, resource constraints, and precedence constraints. Therefore, this study uses the Monte Carlo method to estimate the two objective functions. Here, the evaluation of the expected NPV is demonstrated as an example, and the expected makespan can be estimated in the same way. A realisation of activity durations $\mathbf{D}_{\boldsymbol{n}}$ is generated according to distributions $\Phi_{j, t}$. Here, $\mathbf{D}_{\boldsymbol{n}}$ represents a matrix, and element $\left(\mathbf{D}_{\boldsymbol{n}}\right)_{j, t}$ represents the realisation of the duration of activity $j$ starting from $t$. The subscript $n$ represents the index of realisation in the simulation. The realisation of the activity duration $\mathbf{D}_{\boldsymbol{n}}$ is called a scenario. The $N P V\left(\boldsymbol{\pi}, \mathbf{D}_{\boldsymbol{n}}\right)$ denotes the NPV given by policy $\boldsymbol{\pi}$ and scenario $\mathbf{D}_{\boldsymbol{n}}$. The expected NPV under policy $\boldsymbol{\pi}$ can be estimated using $N$ scenarios as
$E(\widehat{N P V}(\boldsymbol{\pi}))=\frac{1}{N} \sum_{n=1}^{N} N P V\left(\boldsymbol{\pi}, \mathbf{D}_{\boldsymbol{n}}\right)$.
The expected makespan can be estimated similarly as $E\left(\widehat{E_{J-1}}(\boldsymbol{\pi})\right)-\tau$. Unfortunately, the calculation of $N P V\left(\boldsymbol{\pi}, \mathbf{D}_{\boldsymbol{n}}\right)$ is not straightforward. Policy $\boldsymbol{\pi}$ only contains the execution order of activities and the start time of the first dummy activity; the start and end times of other activities are not available. This research uses the schedule generation scheme (SGS) to calculate the start and end times of activities under policy $\boldsymbol{\pi}$ and scenario $\mathbf{D}_{\boldsymbol{n}}$. The SGS selects activities to execute at each decision point and obtains the start time of each activity based on the constraints (6) (8). Two commonly used SGS methods include the parallel (PSGS) and serial (SSGS) SGS (Kolisch, 1996). According to Kolisch (1996), neither SSGS nor PSGS is dominant. The ranking of the two methods is case dependent. The PSGS has better results when the problem is highly resource constrained. The SSGS is more appropriate for problems with moderate resource constraints. This paper follows the choice of several papers on SRCPSP where the SSGS was used (Ballestin, 2007; Zhao, Ke, \& Chen, 2016).

```
Algorithm 2 The SSGS to identify the start and end times of activities
Input: Policy \(\boldsymbol{\pi}=\left\{a_{0}, a_{1}, \cdots, a_{J+1}, r\right\}\) and Scenario \(\mathbf{D}_{\boldsymbol{n}}\)
    Initialise the remaining resources at time \(t: R_{k, t}=R_{k} \forall t=1,2, \cdots, T\)
    Initialise the start and end times of the first dummy activity \(S_{0}=E_{0}=\tau\) and
        the set of scheduled activities \(\psi=\{0\}\)
    For \(m=1\) to \(J+1\)
    Next activity to schedule is \(j=a_{m}\)
    Latest end time of the predecessors of activity \(j: t^{E}=\max \left\{E_{j} \mid j^{\prime} \in P_{j}\right\}\)
    Latest start time of activities that are executed before activity \(j: t^{E}=\)
    \(\max \left\{S_{n_{m}} \mid m^{\prime}<m\right\}\)
    Earliest start time of activity \(j\) is \(S^{\prime}=\max \left\{t^{E}, t^{E}\right\}\)
    While \(R_{k, t}<r_{j, k}, \forall t \in\left[S^{\prime}, S^{\prime}+\left(\mathbf{D}_{\boldsymbol{n}}\right)_{j, k^{\prime}}\right]\)
    \(S^{\prime}=\min \left\{E_{j} \mid E_{j}>\hat{S}, j \in \psi\right\}\)
    end while
    \(S_{j}=S^{\prime}, E_{j}=S_{j}+\left(\mathbf{D}_{\boldsymbol{n}}\right)_{j, k_{j}}\) and \(\psi=\psi \cup\left\{a_{m}\right\}\)
    Update the remaining resources as \(R_{k, t}=R_{k, t}-r_{j k}\) for \(t \in\left[S_{j}, E_{j}\right]\)
    end
    Return \(\left\{S_{0}, S_{1}, S_{2}, \cdots, S_{J}, S_{J+1}\right\}\) and \(\left\{E_{0}, E_{1}, E_{2}, \cdots, E_{J}, E_{J+1}\right\}\)
```

The detailed steps of the SSGS are provided in Algorithm 2, which sequentially chooses activities in vector $\lambda$. The start time of activity $j$ is postponed until constraints (6)-(8) are satisfied. After all activities are scheduled, the start and end times of activities under policy $\boldsymbol{\pi}$ and scenario $\mathbf{D}_{\boldsymbol{n}}$ are obtained. The corresponding NPV can then be calculated using Eq. (3).

Although only the uncertainty caused by the weather condition is considered in this study, other types of uncertainties can be processed after they are modelled in the simulation process. For example, when the uncertainty caused by recourses is considered, the repair time and time between the breakdown of a resource can be assumed to follow the exponential distribution (Fu, Lau, \& Varakantham, 2015). Uncertain logistic delays can be considered using a random lead time that follows an appropriate distribution (Xu, Zhao, \& Chen, 2012). Further, the budget can be modelled by a random variable, and a constraint on the budget is added to the project scheduling model (Yang, 2005). Given space limitations, the consideration of other uncertainties is regarded as a future research direction.

## 4. Improved EDA with an R\&S procedure

An improved EDA is shown in Algorithm 3; this EDA can achieve better performance when solving the SRCPSP. An R\&S procedure using the CRN is embedded into the EDA to identify elite individuals more efficiently and accurately. The sampling probability model for the next generation is modified from that of Fang et al. (2015). Compared with Fang et al. (2015), the start time of a project is adopted as an additional decision variable, and it is included in the sampling probability model. Furthermore, the method to sample the new population in Fang et al. (2015) is improved by considering resource constraints and activity durations, which are provided in Algorithm 5. In addition, the local search method proposed by Fang et al. (2015) is replaced by a more general version for a broader search scope. The flowchart of the improved EDA in Algorithm 3 is shown in Fig. 1; it explains the relationship between the algorithms and expressions in this study. Algorithm 1 is used to prepare data for the probability distributions of activity durations that are the inputs of the improved EDA. Algorithm 2 is used to calculate the objective function, and it is involved in different steps in the improved EDA. Algorithms 1 and 2 are not shown in Fig. 1.

```
Algorithm 3: Framework of the improved EDA
Step
    Generating initial population: Generate \(M\) initial individuals \(\Omega_{0} \cdot\left\{\pi_{0,1}\right.\) :
    \(\left.\pi_{0,2}, \cdots, \pi_{0, M}\right\}$ as indicated in Section 4.1. Initialise the probability matrix
    \(\boldsymbol{\pi}_{0}\) through Fig. (19). Set the optimal solution \(\boldsymbol{\pi}^{*}=\pi_{0,1}\) and the index of
    iteration \(g=0\)
Step Selecting elite individuals: Select \(Q\) elite individuals from population \(\Omega_{0}\)
    using the R\&S procedure in Algorithm 4. The selected elite set is denoted as
    \(\Omega_{0}^{Q} \cdot\left\{\pi_{0,1}^{Q}, \pi_{0,2}^{Q}, \cdots, \pi_{0, Q}^{Q}\right\}\)
Step Improving elite individuals by local search: Generate new individuals
    from the elite set \(\Omega_{0}^{Q}\) using the local search method suggested in Section 4.3.
    The set of \(Q\) new elite individuals is then obtained as
    \(\Omega_{0}^{Q} \cdot\left\{\pi_{0,1}^{Q}, \pi_{0,2}^{Q}, \cdots, \pi_{0, Q}^{Q}\right\} \cdot\) The solution with the smallest makespan or
    largest NPV is denoted as \(\pi_{0}^{Q^{*}} \cdot\) If \(\pi_{0}^{Q^{*}}\) surpasses \(\boldsymbol{\pi}^{*}, \boldsymbol{\pi}_{0}^{Q^{*}}\) is selected as the new
    optimal solution \(\boldsymbol{\pi}^{*}\)
Step Updating individual sampling probabilities: Update the probability
    matrix \(\boldsymbol{\pi}_{0,1}\) using the elite set \(\Omega_{0}^{Q}\) through Fig. (20).
Step Sampling new population: Sample \(M\) individuals according to \(\boldsymbol{\pi}_{0,1}\) through Algorithm 5 to form a new population \(\Omega_{0,1}\)
Step Stopping criterion: If the stopping criterion is not satisfied, the index of the iteration is updated as \(g=g+1\); then, the algorithm goes to Step 2.
    Otherwise, the algorithm is stopped, and \(\boldsymbol{\pi}^{*}\) is regarded as the optimal
    scheduling policy. The total number of generated schedules is used as the
    stopping criterion to control the computation time because the simulation
    is the most time-consuming part of this algorithm. Here, performing SSGS
    under a scenario for a policy \(\boldsymbol{\pi}\) is counted as one schedule.
```

![img-0.jpeg](img-0.jpeg)

Fig. 1. Flowchart of the improved EDA.

### 4.1. Generating initial population

In the first step of the EDA, an initial population $\Omega_{0} \cdot\left\{\pi_{0,1}, \pi_{0,2}, \cdots\right.$, $\pi_{0, M}\}$ that includes $M$ feasible solutions is generated. The start time of the project in the initial solutions is set to be the first time point of the planning horizon. Initial execution orders of the activities are created through random priority values and the earliest start times of the activities. The priority value of activity $j$ is a uniformly distributed random variable $\rho_{j}$. The earliest start time of activity $j$ is calculated using the expected value of activity durations, which ignores resource constraints as
$\gamma_{j}=\max _{i \cup j} \cdot\left(\gamma_{j}+\left(\overline{\mathbf{D}}_{i, j}\right)_{j}, j \in \chi(\psi)\right.$.
Here, $\left(\overline{\mathbf{D}}\right)_{j, i}$ denotes the average duration of activity $j$ starting from $t, \psi$ denotes a set that contains all scheduled activities, and $\chi(\psi)$ represents the eligible set containing unscheduled activities whose predecessor activities have been scheduled. Activities in $\chi(\psi)$ are selected according to
$\chi(\psi)=\{j \mid j \notin \psi$ and $P_{j} \subset \psi\}$
Starting from $\psi=\{0\}$, activity $j \in \chi(\psi)$ with the smallest value of $\rho_{j} \times \gamma_{j}$ is selected to be scheduled next; this set of scheduled activities is updated as $\psi=\psi \cup\{j\}$. After all activities are scheduled, a precedence

feasible individual is generated.

### 4.2. Selecting elite solutions via the R\&S procedure with the CRN

Estimating objective functions through simulation is the most timeconsuming part of the optimisation. Instead of generating the same number of scenarios for different solutions, a sequential R\&S procedure with the CRN is adopted in this study to identify the elite solutions. Thus, the simulation efforts are allocated to different solutions more appropriately.

The CRN is an effective method to reduce the variance when comparing two or more populations by generating positively correlated samples. In this study, the objective function is estimated by realising activity durations. Therefore, a positive correlation of the objective function corresponding to different solutions can be achieved by positively correlated activity durations. First, a random variable $\xi_{j, n}$ that is uniformly distributed between 0 and 1 is generated for activity $j$ in scenario $n$ for all solutions. The durations of activityj starting from different times are generated based on the same variable $\xi_{j, n}$ as
$d_{i, t, n}=\Phi_{i, j}^{-1}\left(\xi_{j, n}\right)$
Here, $\Phi_{j, t}^{-1}(\cdot)$ denotes the inverse cumulative distribution function of distribution $\Phi_{j, t}$. Consequently, the durations of the same activity that starts from different time points are positively correlated. Thus, objective functions of different solutions estimated based on these durations are positively correlated. The paired $t$-test is then used to test the difference between the expected objective functions of different solutions.

The sequential R\&S procedure using the CRN is developed as Algorithm 4 to identify elite solutions. In Algorithm $4, \zeta_{n}=\left[\xi_{1, n}, \xi_{2, n}, \cdots \xi_{J, n}\right]$ is the vector of random variables used to generate the activity durations in scenario $n$.

```
Algorithm 4: Identifying elite solutions using R\&S procedure
\(\operatorname{Input}: \Omega_{g}=\left[\pi_{g, 1}, \pi_{g, 2}, \cdots \pi_{g, M}\right]\)
    Set the initial set of individuals \(\mathscr{I}_{0}=\Omega_{g}\) and the index of the iteration \(z=0\).
    The number of simulated observations of the objective function corresponding
to solution \(t\) is defined as \(n_{0}\) and \(\left|\mathscr{I}_{3}\right|\) denotes the number of individuals in \(\mathscr{I}_{3}\).
Generate additional \(3-n_{0}\) observations of the objective function for individual
\(\pi_{g, 1}\) in \(\mathscr{I}_{3}\) if \(\pi_{0}<3\) with \(\zeta_{n_{0}-1}, \cdots, \zeta_{3}\).
while the number of solutions in set \(\mathscr{I}_{3}\) is larger than 2
Generate one observation of the objective function with \(\zeta_{n_{0}-1}\) for each \(\pi_{g, 1}\) in
\(\mathscr{I}_{3}\) and \(\pi_{0}=\pi_{0}=1\)
The solutions in set \(\mathscr{I}_{4}\) are ranked according to the value of objective
functions as \(\pi_{g, 1}, \pi_{g, 2}, \cdots, \pi_{g, J_{n}}\).
When the expected makespan (NPV) is used as
the objective function, the solutions are sorted in an ascending (descending)
order.
    if the smallest number of observations for an individual in \(\mathscr{I}_{3}\) exceeds \(\mathrm{N}_{\max }\)
    The R\&S procedure is terminated, and the elite solution set is obtained as
\(\Omega_{g}^{H}=\left[\pi_{g, 1}, \cdots, \pi_{g, Q}\right]\).
    end if
    for \(i_{1}=Q+1\) to \(\left|\mathscr{I}_{3}\right|\)
    Initialise the number of solutions that are significantly better than \(\pi_{g, 1}\) as
\(\operatorname{count}=0\).
    for \(i_{2}=1\) to \(i_{1}-1\)
    Perform the paired \(t\)-test using \(n=\min \left(\pi_{g, 1} \pi_{g, 2}\right)\) pairs of observations of
objective functions corresponding to the solutions \(\pi_{g, 0}\) and \(\pi_{g, 0}\).
if the paired \(t\)-test indicates that solution \(\pi_{g, 0}\) is statistically worse than
\(\pi_{g, 0}\) at a significance levels
    count \(=\operatorname{count}+1\);
    end if
    end for
    if count \(\geq Q \quad\) Solution \(\pi_{g, 0}\) is removed from set \(\mathscr{I}_{4}\)
end if
end for
\(\mathscr{I}_{3+1}=\mathscr{I}_{3}\) and \(z=z+1\)
end while
Return the elite solution set: \(\Omega_{g}^{H}=\mathscr{I}_{3}\)
```


### 4.3. Local search method

A local search method is adopted to further enhance the exploitation ability of the EDA, which is realised through the weighted random sampling of the start time $\tau$ and random alteration of the execution order of activities. In weighted random sampling, each item is randomly selected according to a probability equal to its relative weight (Efraimidis \& Spirakis, 2006). In this study, the relative weight of the start time $\tau$ is computed according to its working probability as
$p_{\tau}^{\sigma}=w(\tau) / \sum_{\tau=T_{S T}}^{T_{S D}} w(\tau), \tau \in\left[T_{S T}, T_{E D}\right]$
$T_{S T}$ and $T_{E D}$ are the predetermined upper and lower bounds of the start date $\tau$, respectively. First, $n_{W}$ different start times are selected for a solution $\pi_{g, j}^{H}$ in the elite set $\Omega_{g}^{H}$. Thus, $n_{W}$ additional solutions are generated according to $\pi_{g, J}^{H}$. These $n_{W}+1$ solutions are evaluated using Algorithm 4, and the optimal individual is selected as a member of the new solution set $\Omega_{g}^{W}$.

For a solution in set $\Omega_{g}^{W}$, each activity has a probability $P_{p w}$ to be selected. The selected activity $j$ is inserted into the position of another randomly selected activity $x$ between $R M_{j}$ and $L M_{j}$. As shown in Fig. 2, $R M_{j}$ is the rightmost position of the predecessor activities of activity $j$, and $L M_{j}$ is the leftmost position of the successor activities of activity $j$. If the position of activity $x$ is on the left of $j, j$ will be inserted before activity $x$. Otherwise, $j$ will be placed after activity $x$. Activities between $R M_{j}$ and $L M_{j}$ have the same probability of being selected as activity $x$. Then, new individuals are evaluated together with $\Omega_{g}^{W}$, and $Q$ individuals are selected as the new elite set $\Omega_{g}^{E}$.

### 4.4. Probability model to sample individuals for the next generation

New individuals in the next generation of the EDA are sampled according to the probability model built using elite individuals in $\Omega_{g}^{E}$. To build this probability model, a solution $\pi=[\lambda, \tau]$ is transferred into a matrix of binary variables
$\mathbf{X}=\left[\begin{array}{ccc}A_{1,1} & \cdots & A_{1, J} & A_{1, J+1} \\ 1 & \ddots & 1 & A_{1, J} & A_{2, J+1}\end{array}\right]$
$A_{2,1} \quad \cdots \quad A_{2, J} \quad A_{2, J+1}$
Here,
$A_{i, j}=\left\{\begin{array}{ll}1, & j \text { is scheduled before } j \text { in } \pi \\ 0, & \text { else }\end{array}\right.$
The first and last dummy activities are not considered here. The last column of matrix $\mathbf{X}$, i.e. $\left[A_{1, J+1}, A_{2, J+1}, \cdots, A_{2, J+1}\right]^{\mathrm{T}}$, is the binary form of the start date $\tau$. Here, $A_{2, J+1}$ is the lowest bit of the binary vector. Thus, solution $\pi$ is mapped into a binary matrix $\mathbf{X}$ through a function $\mathbf{X}=$ $G(\pi)$. For instance, the solution $\pi=[0,2,3,1,4,3]$ with dummy activities 0 and 4 is converted to
$\mathbf{X}=\left[\begin{array}{llll}0 & 0 & 0 & 0 \\ 1 & 0 & 1 & 1 \\ 1 & 0 & 0 & 1\end{array}\right]$
The probability matrix of generation $g$ is defined as
$\boldsymbol{\psi}_{\pi}=\left[\begin{array}{ccc}\operatorname{Pr}\left(A_{j, 1}^{\tau}=1\right) & \cdots & \operatorname{Pr}\left(A_{1, J}^{\tau}=1\right) & \operatorname{Pr}\left(A_{1, J+1}^{\tau}=1\right) \\ \vdots & \ddots & \vdots & \vdots \\ \operatorname{Pr}\left(A_{j, 1}^{\tau}=1\right) & \cdots & \operatorname{Pr}\left(A_{j, J}^{\tau}=1\right) & \operatorname{Pr}\left(A_{j, J+1}^{\tau}=1\right)\end{array}\right]$

![img-1.jpeg](img-1.jpeg)

Fig. 2. Alteration of the execution order of activities during local search.

The initial probability matrix $\boldsymbol{\varphi}_{0}$ is assumed as
$\boldsymbol{\varphi}_{0}=\left[\begin{array}{cccccccc}0 & 0.5 & \cdots & 0.5 & 0 \\ 0.5 & 0 & \cdots & \vdots & \vdots \\ \vdots & \vdots & \ddots & 0.5 & 0 \\ 0.5 & \cdots & 0.5 & 0 & 1\end{array}\right]$
The probabilistic model $\boldsymbol{\varphi}_{g}$ is updated according to the solutions in elite set $\Omega_{g}^{E}$ as
$\boldsymbol{\varphi}_{g+1}=L_{\text {max }} \frac{1}{Q} \sum_{s=1}^{Q} G\left(\pi_{g s}^{g}\right)+\left(1-L_{\text {min }}\right) \boldsymbol{\varphi}_{g}$.
Here, $L_{\text {min }} \in(0,1)$ is the learning rate.

### 4.5. Sampling a new population from the probability model

The probability matrix $\boldsymbol{\varphi}_{g+1}$ is used to sample the population of generation $g+1$. The sampling probability for the $j^{\text {th }}$ bit of $\tau$ is
$P_{S T j}=\left(\varphi_{g+1}\right)_{j, j+1} \forall j \in\{1,2, \cdots, J\}$.
Here, $\left\{\boldsymbol{\varphi}_{g+1}\right\}_{j, j+1}$ denotes the element of the matrix $\boldsymbol{\varphi}_{g+1}$ in row $j$ and column $J+1$. Then, a binary random number $A_{j, j+1} \in\{0,1\}$ is generated according to the probability $\operatorname{Pr}\left(A_{j, j+1}=1\right)=P_{S T j}$. Finally, a sampled $\tau$ is given by
$\tau=\sum_{j=1}^{J} A_{j, j+1} \times 2^{J-j}$.
Unlike the sampling method in Fang et al. (2015), the execution order of activities is obtained according to the duration of activities and resource constraints. The detailed process is listed in Algorithm 5. At each step, an activity $j$ is selected from the set of unscheduled activities $\chi$ based on the probability
$P_{L i n j}=\sum_{j \in g}\left(\boldsymbol{\varphi}_{g+1}\right)_{j j} / \sum_{j \downarrow \in g}\left(\boldsymbol{\varphi}_{g+1}\right)_{j, j}$.
The sampling procedure is repeated $M$ times, and $M$ new individuals are obtained as the new population.

```
Algorithm 5 Process of sampling the execution order of activities
    Input: Probability matrix \(\boldsymbol{\varphi}_{g}\) and average activity durations \(\overline{\mathbf{D}}\)
        Initialize remaining resources at time \(t: R_{k, t}=R_{k} \forall t=1,2, \cdots, T\)
        Initialize start and end times of the first dummy activity \(S_{0}=E_{0}=t\), and the
        set of scheduled activities \(\varphi=\{0\}\)
        for \(m=1\) to \(J+1\)
        Sample an activity \(j\) from the unscheduled activities \(\chi\) according to the
        probabilities in Eq. (23).
            The earliest start time of activity \(j\) is \(S^{\prime}=\max \left\{E_{j} \mid j^{\prime} \in P_{j}\right\}\)
            While \(R_{k, t}<r_{j k}, \forall t \in\left\lfloor S^{\prime}, S^{\prime}+\left(\mathbf{D}\right)_{j, k}\right\rfloor\)
            \(S^{\prime}=\min \left\{E_{j} \mid E_{j^{\prime}}>S^{\prime}, j^{\prime} \in \psi\right\}\)
            end while
            \(S_{j}=S^{\prime}, E_{j}=S_{j}+\left(\overline{\mathbf{D}}\right)_{j, k}\) and \(\varphi=\psi \cup\{j\}\)
        Update the remaining resources as \(R_{k, t}=R_{k, t}-r_{j, k}\) for \(t \in\left\langle S_{j}, E_{j}\right\rfloor\)
        end
    Return A solution \(\boldsymbol{\pi}=\left[\begin{array}{lll}a_{0}, a_{1}, \cdots, a_{m}, \cdots, a_{J+1}, t\end{array}\right]\) where \(S_{a_{m}}<S_{a_{m_{j}}}\) if \(m<m\) '
```


## 5. Numerical studies using the J120 dataset from PSPLIB

The J120 dataset from PSPLIB provides benchmark instances of project scheduling that contains 600 RCPSPs with 120 non-dummy activities (Kolisch \& Sprecher, 1997). For the numerical study, 60 RCPSPs were randomly selected from the J120 dataset. Then, the 60 RCPSPs were modified to SRCPSPs by assuming random activity durations that depend on time-varying weather conditions. This section evaluates the performance of the improved EDA using modified benchmark project instances. Only the expected makespan was used as the objective function in this section. The algorithms were implemented on a desktop computer with an Intel i9-9900 CPU and 8 GB of memory using MATLAB 2018b.

### 5.1. Weather condition modelling

Simulated weather conditions were used for the numerical study. The time unit was one day, and the horizon of the weather condition model was one year. The effect of weather conditions on construction operations was described by climate reduction coefficients (CRCs) (Ballesteros-Pérez, Smith, Lloyd-Papworth, \& Cooke, 2018). The CRCs refer to the proportion of workable days during the same time in

historical years. The sine wave was used to model the CRC data, which is given by
$w(t)=0.5+0.2 \cos (2 \pi(t / 365-0.5)), t \in\{1,2,3, \cdots, 365\}$
Here, $\boldsymbol{w}(t)$ denotes the probability that day $t$ is a workable day. Then, the expected activity duration $d_{i, t}^{E}$ is calculated using Algorithm 6. Further, it was assumed that the activity duration follows a continuous uniform distribution within the interval $\left[0,2 d_{i, t}^{E}\right]$.

```
Algorithm 6 Calculation of expected duration of activity \(j\) starting from time \(t\)
    Set the accumulate effective working time: \(\operatorname{count}=0\), and set the expected
        duration of activity \(j\) starting from \(t d_{i, t}^{E}=0\)
    While count \(<d_{i}^{\prime}\)
        count \(=\operatorname{count}+w(t)\) and \(d_{i, t}^{\prime \prime}=d_{i, t}^{\prime \prime}+1\)
        \(t=t+1\), and set \(t=1\) when \(t=366\)
    end while
```


### 5.2. Overall performance of improved EDA

According to Ballestin (2007), the performance of an algorithm for an RCPSP was measured through the relative deviation between the optimal expected makespan $M S=F\left(\boldsymbol{\pi}^{*}\right)$ and the critical path-based lower bound $L B$; this is equated as $(M S-L B) / L B$. To measure the overall performance of the improved EDA on the J120 dataset, the average deviation from the lower bound (Ave.Dev.LB) of the 60 selected instances was used as the indicator.

The performance of the improved EDA depends on the parameters of the algorithm. Inspired by Fang et al. (2015), an orthogonal experiment was conducted to identify an appropriate combination of parameters. Important parameters in the EDA include the population size $M$, proportion of elite individuals $\eta$, sample size of the start date $n_{W}$ in the local search, probability $P_{p a r}$ of selecting an activity in the local search, and learning rate $L_{\text {rate }}$. Four factor levels were set for each parameter during the orthogonal experiment. According to the orthogonal table $L_{16}\left(\boldsymbol{\lambda}^{2}\right)$, 16 parameter combinations were tested. For each combination, 30,000 schedules were generated to determine the optimal expected makespan for each problem. The makespan corresponding to the optimal solution for each instance was evaluated using 1,000 additional simulated schedules for a more accurate estimate.

The two additional parameters used by the improved EDA are $N_{\max }$ and $\alpha$. Because of the interaction between parameters, the result of the
orthogonal experiment became unreliable when $N_{\max }$ and $\alpha$ were selected via an orthogonal experiment. Consequently, two parameters were determined outside the orthogonal experiment. After several trials, the two parameters were selected as $N_{\max }=50$ and $\alpha=0.01$. There are more suitable combinations of $N_{\max }$ and $\alpha$; however, the numerical examples in the rest of the paper show that the improved EDA using $N_{\max }=$ 50 and $\alpha=0.01$ already outperform the original EDA. Therefore, this research did not search for a better combination of the two parameters. The performance trends of the factor levels of the improved EDA are illustrated in Fig. 3. Accordingly, the parameters used by the improved EDA were selected as $M=100, \eta=0.01, n_{W}=20, P_{p a r}=0.1, L_{\text {rate }}=$ $0.9, N_{\max }=50$, and $\alpha=0.01$. Under these parameters, the Ave.Dev.LB of the 60 selected J120 instances calculated by the improved EDA was 1.409 .

### 5.3. Comparisons between different versions of EDAs

In the existing research on SRCPSP, the fitness function of a solution is often evaluated with a fixed number of simulation scenarios. Ballestin (2007) confirmed that a small number of simulation scenarios are beneficial because more solutions can be found and evaluated. Therefore, in the original EDA without the R\&S method, 10 scenarios were generated for each solution. Other parameters of the original EDA were selected using the orthogonal experiment as $M=150, \eta=0.01, n_{W}=$ $10, P_{p a r}=0.05$, and $L_{\text {rate }}=0.9$. The Ave.Dev.LB of the 60 instances was then calculated as 1.451 using 30,000 schedules for each instance. The Ave.Dev.LB obtained by the improved EDA using the same number of schedules is 1.409. A deterministic scheduling approach using the EDA is adopted in this section, where the makespan is calculated directly using the expected activity durations. Deterministic scheduling was repeated 20 times for each instance; the optimal policy identified by deterministic scheduling was evaluated in 1,000 simulated scenarios. The Ave.Dev.LB obtained by deterministic scheduling was 1.501 . Therefore, the original and improved EDA reduced the Ave.Dev.LB by $3.33 \%$ and $6.09 \%$, respectively, when compared with the deterministic scheduling approach.

Three projects with different characteristics were randomly selected from the J120 dataset to further explore the convergence process of the EDA; they are named projects \#1, \#2, and \#3. Parameters of the three projects are listed in the first row of Table 2. The parameters of the EDAs were selected using an orthogonal experiment, and the results are listed
![img-2.jpeg](img-2.jpeg)

Fig. 3. Trend of factor levels of parameters in the orthogonal experiment.

Table 2
Parameters of the three projects and those used in the EDAs.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Convergence processes of EDAs corresponding to project\#1 with $\mathrm{RF}=0.25, \mathrm{RS}=0.1$, and $\mathrm{NC}=1.5$.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Convergence processes of EDAs corresponding to project\#2 with $\mathrm{RF}=0.5, \mathrm{RS}=0.3$, and $\mathrm{NC}=1.8$.
in the second and third rows of Table 2. The convergence processes of projects \#1, \#2, and \#3 are plotted in Figs. 4-6. Each convergence curve in the figures is the average result of 20 replications of the EDA. The convergence processes in Figs. 4-6 show that the improved EDA can obtain a shorter makespan compared to the original EDA during the entire convergence process. The makespan obtained by deterministic scheduling is also provided in the figures for comparison. Compared with deterministic scheduling, the makespan reduction of stochastic scheduling is calculated in Table 3. The results show that the improved EDA can obtain a more significant makespan reduction than the original EDA. The elapsed time and optimal makespan obtained at different stages of the EDA are compared in Table 4. Table 4 indicates that the computing time of the improved EDA is longer than that of the original

EDA under the same number of schedules because of the additional operators in the R\&S procedure. However, the improved EDA can still obtain a better solution by using less computing time. The improved EDA can obtain an expected makespan 441.5 days in 287 s when scheduling project \#1. In contrast, the original EDA required 587 s to achieve an average makespan 444.6 days. Therefore, the improved EDA is more efficient and can obtain a shorter expected makespan.

### 5.4. Analysis of optimisation process

An important contribution of this study is embedding the R\&S procedure into the EDA, and therefore, it is necessary to investigate the performance of the R\&S procedure for identifying elite solutions. To this

![img-5.jpeg](img-5.jpeg)

Fig. 6. Convergence processes of EDAs corresponding to project\#3 with $\mathrm{RF}=1, \mathrm{RS}=0.5$, and $\mathrm{NC}=2.1$.

Table 3
Makespan reduction compared with deterministic scheduling.

Table 4
Elapsed time and optimal makespan obtained at different stages of EDAs.

end, 100 policies of project\#1 visited by the original EDA were randomly selected. First, 10 simulated schedules were generated for each solution, and two elite solutions were selected according to the mean values of the simulated makespans. Subsequently, the R\&S procedure was adopted to identify two elite solutions from the 100 solutions, and the R\&S procedure terminated when the total number of simulated schedules was greater than 1,000 . The two methods were repeated 50 times to process the same 100 policies. Each obtained elite solution was evaluated using 1,000 additional simulated schedules to obtain more accurate estimates of the makespan. The makespans of the elite solutions identified by the two methods are compared in Fig. 7; this figure shows that the elite solutions obtained by the R\&S procedure incur significantly shorter makespans. Further, the variance among the results of different replications of the R\&S method are significantly smaller. Further, 41 out of 50 replications of the R\&S procedure consumed less than 1,000 simulated schedules to identify two elite solutions. Thus, the R\&S procedure can select elite solutions more effectively.

The R\&S procedure is more effective because some inferior solutions are removed at an early stage. The histogram of the number of simulated schedules for a solution in a randomly selected convergence process of
![img-6.jpeg](img-6.jpeg)

Fig. 7. Boxplot of the makespans of the elite solutions.

![img-7.jpeg](img-7.jpeg)

Fig. 8. Histogram about the number of schedules simulated for a solution by the improved EDA.
![img-8.jpeg](img-8.jpeg)

Fig. 9. Boxplots of the correlation coefficients of makespans in the improved EDA.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Boxplots of correlation coefficients of makespans in the original EDA.

Table 5
Effect of project characteristics on scheduling result.

the improved EDA for project\#1 is plotted in Fig. 8; it shows that most solutions are removed from the R\&S procedure after less than five simulated schedules. Thus, extensive simulation of low-quality solutions is avoided, and the simulation efforts are allocated more appropriately.

The method for generating positively correlated makespans of different solutions via the CRN is validated. Simulated makespans generated in the two versions of the EDA when scheduling project\#1 were analysed; the simulated makespans of 25 randomly selected solutions were collected. The boxplots of the correlation coefficients corresponding to the two algorithms are shown in Figs. 9 and 10, respectively. Each boxplot in the two figures represents the distribution of the correlation coefficients between the makespan of a solution and those of the other 24 solutions. Fig. 9 shows that the simulated makespans of most solutions are positively correlated when the CRN is used. Fig. 10 indicates that the simulated makespan is almost statistically independent without the CRN. Therefore, the simulation-based method using CRN can derive positively correlated makespans that can reduce the variance of the difference between the average makespan of different solutions.

### 5.5. Sensitivity analysis of results obtained by improved EDA

Instances in the J120 dataset were generated according to three parameters: network complexity ( $N C \in\{1.5,1.8,2.1\}$ ), resources factor $(R F \in\{0.25,0.5,0.75,1\})$, and resource strength ( $R S \in\{0.1,0.2,0.3$. $0.4,0.5\}) . N C$ is defined as the average number of predecessors per activity; $R F$ refers to the average fraction of resource types required by a non-dummy activity, $R S$ reflects the relationship between resource requirements and supply, and a small value of $R S$ implies a scarce resource supply.

The results for some selected project instances are listed in Table 5. Ave.Dev.LB increases with $R F$ and decreases with $R S$. The change in Ave. Dev.LB is nonmonotonic when NC increases. These findings are similar to those reported by Fang et al. (2015). A large RF value and a small RS value indicate more severe resource constraints on the SRCPSP. Therefore, the difference between the obtained makespan and lower bound that does not consider the resource constraints is more obvious. In contrast, a large NC value reveals that precedence constraints on the activities are strict. The precedence constraints affect both the obtained makespan and lower bound of the makespan. Consequently, Ave.Dev.LB does not change monotonically when NC increases.

Table 6
Steps to construct a wind turbine.
## 6. Case study about windfarm construction

A windfarm construction project was studied to demonstrate the performance of the proposed method in real-world case studies; the case study also reveals management implications of the proposed method in practical project scheduling problems. The data and parameters used in this case study are not provided in the text because of confidentiality policies. Detailed information about the project has been not been provided for the same reason.

### 6.1. Windfarm construction project

There are ten wind turbines on the windfarm, and 14 steps are required to construct a wind turbine. Therefore, the construction project contains a total of 140 activities. The 14 steps required to construct a wind turbine are listed in Table 6 ; the required resources for each step are also demonstrated. A total of 9 renewable resources with limited amounts were considered; each resource was represented by a number. Renewable resources include engineering machines and technicians required for different construction activities.

A payment is received from the owner of the windfarm after the project is completed. There is a fixed cost for an activity in the project, which is independent of the duration of the activity. The fixed cost is spent preparing for the execution of the activity; for example, the transportation of materials, equipment, and technicians. Further, the variable cost of an activity is proportional to the duration of the activity, and it includes the salary of technicians and the rent of equipment. The NPV is used as another objective function besides the makespan, and this is calculated using the project payment, fixed activity cost, and variable activity cost.

These activities are sensitive to weather conditions. For example, there is a safety threshold for the wind speed for hoisting, and most activities cannot be performed in rain or snow. Therefore, the duration of activities is calculated considering weather conditions. This case study uses historical weather data from the China Meteorological Data Service Centre, which contains daily mean values of wind speed and perception over 40 years (from 1979 to 2018). After standard durations of activities were provided by relevant experts, the activity durations were re-calculated using Algorithm 1. The beta distribution was used to model activity durations, and the three-point estimation method in Hajdu (2013) was used to identify the parameters. The expected value $\mu(j, t)$ and the two parameters of the beta distribution (i.e. $a(j, t)$ and $b(j, t))$ for the duration of activity $j$ starting from $t$ were calculated as
$\mu(j, t)=\left(V_{t 0}(j, t)+V_{P}(j, t)+4 \times V_{M}(j, t)\right) / 6$
$a(j, t)=\frac{\left(\mu(j, t)-V_{t 0}(j, t)\right) \times\left(2 \times V_{M}(j, t)-V_{t 0}(j, t)-V_{P}(j, t)\right)}{\left(V_{M}(j, t)-\mu(j, t)\right) \times\left(V_{P}(j, t)-V_{t 0}(j, t)\right)}$
and
$b(j, t)=a(j, t) \times\left[V_{P}(j, t)-\mu(j, t)\right] /\left[(\mu(j, t)-V_{t 0}(j, t)\right]$
Here, $V_{t 0}(j, t), V_{P}(j, t)$, and $V_{M}(j, t)$ represent the minimum value, maximum value, and mode of the activity durations in set $D_{j, t}$, respectively. After normalisation, the distribution of the duration of activity $j$ starting from time $t$ is given by
$\left[d_{j, t}-V_{P}(j, t)\right] /\left[V_{t 0}(j, t)-V_{P}(j, t)\right] \sim \operatorname{beta}(a(j, t), b(j, t))$

![img-10.jpeg](img-10.jpeg)

Fig. 11. Convergence processes of EDAs to minimise the expected makespan.
![img-11.jpeg](img-11.jpeg)

Fig. 12. Convergence processes of EDAs to maximise the expected NPV.
![img-12.jpeg](img-12.jpeg)

Fig. 13. Pareto solutions for the SRCPSP about windfarm construction.

![img-13.jpeg](img-13.jpeg)

Fig. 14. Distributions of the makespan of hoisting under different objective functions.

### 6.2. Scheduling results and comparisons

When the project was scheduled according to the objective function of the expected makespan, the parameters of the original and improved EDA were selected using the orthogonal experiment as $(M=100, \eta=$ $0.01, n_{W}=20, P_{p a r}=0.05, L_{\text {rate }}=0.9)$ and $(M=100, \eta=0.01, n_{W}=$ $5, P_{p a r}=0.2, L_{\text {rate }}=0.9)$, respectively. The convergence processes of the improved EDA and original EDA are plotted in Fig. 11, the results of the deterministic scheduling are marked in the figure. Compared with the result of deterministic scheduling, the original and improved EDA reduced the expected makespan by 17.5 and 22.7 days, respectively.

When the expected NPV was considered an objective function, the parameters of the original and improved EDA were selected as ( $M=$ $200, \eta=0.02, n_{W}=15, P_{p a r}=0.1, L_{\text {rate }}=0.9)$ and $(M=150, \eta=$ $0.01, n_{W}=10, P_{p a r}=0.2, L_{\text {rate }}=0.9)$, respectively. The comparison result of the three methods is shown in Fig. 12. The results indicated that the original and improved EDA increased the NPV by 19.24 and 30.60 , respectively, based on the result of deterministic scheduling. Consequently, the improved EDA achieves a shorter expected makespan and a larger expected NPV in a practical case study.

When both the expected makespan and NPV are considered during scheduling, the SRCPSP becomes a bio-objective optimisation problem. This research converts the bio-objective optimisation problem to several single-objective optimisation problems that use weighted combinations of NPV and makespan as the objective function. The solutions of the single-objective optimisation problems are non-dominated solutions of the bio-objective optimisation problem. The weights of NPV and makespan were selected as $(0,1),(1,2),(1,1),(1,0.5)$, and $(1,0)$. Five corresponding Pareto solutions are illustrated in Fig. 13.

A short makespan can increase the NPV because the project payment is not received until it is completed. Further, the NPV is influenced by the cost of the activities. The duration of an activity with a large variable cost should be reduced to increase NPV. For example, the hoisting of turbines requires a crane and other devices. The rents of these devices are expensive. Therefore, a short duration of hoisting is desired to reduce the variable cost and increase the NPV. Two solutions under the objective functions of the expected project makespan and NPV were selected. According to each of the two solutions, 1,000 simulated schedules were generated. Distributions of the hoisting duration under the two different objective functions are plotted in Fig. 14. The average durations of the hoisting under the objective function of makespan and NPV were 2.14 and 1.88 , respectively. The p -value of the $t$-test was $2.86 \times 10^{-52}$, which indicates that the average duration of hoisting under the objective function of the NPV is significantly shorter.

## 7. Conclusions

This study investigated an SRCPSP considering weather conditions. The execution order of the activities and the start date of the project were optimised, which allowed decision makers to schedule activities under time-varying weather conditions. Both the expected makespan and the expected NPV were considered as objective functions to reduce the average project makespan and shorten the average durations of activities with large variable costs. An improved EDA was developed to solve the SRCPSP, which includes a recursive R\&S method to allocate simulation efforts to different solutions appropriately. The CRN was introduced into the generation of scenarios to further enhance the performance of the scheduling algorithm. The improved EDA was used to schedule 60 benchmark projects selected and modified from the J120 dataset in the PSPLIB. The results showed that the improved EDA can obtain a shorter expected makespan than the original EDA. Furthermore, the improved EDA converged to the optimal solution more quickly. The improved EDA was used to process a practical scheduling problem for windfarm construction, where both the expected makespan and NPV were adopted as the objective function. The results of the practical case study confirm the superiority of the improved EDA.

In addition to weather conditions, other uncertain factors can be processed by the improved EDA after these factors are considered in the simulation process. The proposed algorithm can be applied to similar domains. For example, in some practical job-shop scheduling problems, the processing time of an operation is a random variable because of the uncertain conditions of machines and operators. The improved EDA can be used to solve job-shop scheduling problems after appropriate modification. Another possible direction for future research is enhancing the efficiency of the improved EDA by further reducing simulation efforts. Subsequently, SRCPSPs of a larger scale can be solved. Finally, SGS methods that are more timesaving and resource efficient than the SSGS can be developed to enhance the performance of the project scheduling algorithm.

## CRediT authorship contribution statement

Yifan Zhou: Conceptualization, Methodology, Writing - review \& editing, Software. Jindan Miao: Writing - original draft, Software, Visualization. Bin Yan: Investigation, Resources. Zhisheng Zhang: Writing - review \& editing.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

The research work is supported by the National Natural Science Foundation of China (Grant Nos. 71671041).
