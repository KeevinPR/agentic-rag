# A Pareto-Based Estimation of Distribution Algorithm for Solving Multiobjective Distributed No-Wait Flow-Shop Scheduling Problem With Sequence-Dependent Setup Time 

Weishi Shao ${ }^{\odot}$, Dechang $\mathrm{Pi}^{\odot}$, and Zhongshi Shao


#### Abstract

Influenced by the economic globalization, the distributed manufacturing has been a common production mode. This paper considers a multiobjective distributed no-wait flowshop scheduling problem with sequence-dependent setup time (MDNWFSP-SDST). This scheduling problem exists in many real productions such as baker production, parallel computer system, and surgery scheduling. The performance criteria are the makespan and the total weight tardiness. In the MDNWFSPSDST, several identical factories are considered with the related flow-shop scheduling problem with no-wait constraints. For solving the MDNWFSP-SDST, a Pareto-based estimation of distribution algorithm (PEDA) is presented. Three probabilistic models including the probability of jobs in empty factory, two jobs in the same factory, and the adjacent jobs are constructed. The PWQ heuristic is extended to the distributed environment to generate initial individuals. A sampling method with the referenced template is presented to generate offspring individuals. Several multiobjective neighborhood search methods are developed to optimize the quality of solutions. The comparison results show that the PEDA obviously outperforms other considered multiobjective optimization algorithms for addressing MDNWFSP-SDST.


Note to Practitioners-This paper is motivated by the process cycles in multiproduction factories (or lines) of baker production, surgery scheduling, and parallel computer systems. In these process cycles, jobs are assigned to multiproduction factories (or lines), and no interruption exists between consecutive operations. This paper models this process as a multiobjective distributed no-wait flow-shop scheduling with SDST. Scheduling becomes more challenging when facing distributed factories.

[^0]This paper provides an estimation of distributed algorithm with Pareto dominate concept which uses a probabilistic model to generate offspring. Experiment results suggest that the proposed algorithm can find superior solutions of large-scale instances. This scheduling model can be extended to practical problems by considering other constraints, such as assembly process, mixed no-wait, and transporting times. Besides, the proposed algorithm can be applied to solve other distributed scheduling problems and industrial cases, once their constraints are known, i.e., the processing time of operations, the setup time of machines.

Index Terms-Distributed no-wait flow-shop scheduling problem (MDNWFSP), estimation of distribution algorithm (EDA), makespan, multiobjective, sequence-dependent setup time (SDST), total weight tardiness (TWT).

## NOMENCLATURE

## Parameters


Index
$i$ Index for jobs where $i=1,2, \ldots, n$.
$j$ Index for machines where $j=1,2, \ldots, m$.
$f$ Index for factories where $f=1,2, \ldots, F$.
$k$ Index for job position in a given sequence $k=1,2, \ldots, n$.

## Variable

$C_{i, j} \quad$ Continuous variable for the completion time of job $J_{i}$ on machine $M_{j}$.
$T_{i} \quad$ Tardiness time of job $J_{i}$.
$X_{i, k} \quad\left\{\begin{array}{l}1, \text { if } J_{k} \text { is processed immediately after job } J_{i} \\ 0, \text { otherwise. }\end{array}\right.$


[^0]:    Manuscript received August 10, 2018; revised December 1, 2018; accepted December 7, 2018. Date of publication January 7, 2019; date of current version July 1, 2019. This paper was recommended for publication by Associate Editor F. Basile and Editor S. Reveliotis upon evaluation of the reviewers' comments. This work was supported in part by the Fundamental Research Funds for the Central Universities under Grant NP2017208, in part by the Funding of Jiangsu Innovation Program for Graduate Education under Grant KYLX16_0382, in part by the Postgraduate Research and Practice Innovation Program of Jiangsu Province under Grant KYCX17_0287, and in part by the National Natural Science Foundation of China under Grant U1433116. (Corresponding author: Dechang Pi.)
    W. Shao and Z. Shao are with the College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing 211106, China (e-mail: shaoweishi@hotmail.com; shaozhongshi@hotmail.com).
    D. Pi is with the College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing 211106, China, and also with the Collaborative Innovation Center of Novel Software Technology and Industrialization, Nanjing 210093, China (e-mail: nuaacs@126.com).
    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
    Digital Object Identifier 10.1109/TASE.2018.2886303

## I. INTRODUCTION

THE no-wait constraint in scheduling occurs when two consecutive operations of a job must be processed without any interruption [1]. This scheduling constraint appears in many real production scenarios because it can be employed for all kinds of time-dependent industries such as food, steel manufacturing, and chemical processing industries. As seen in Fig. 1, it shows the common process in a bakery which mainly includes dough production, dough rest, dividing and forming, and proofing and baking. Most of the baking products require proofing and the most commonly used proofing agent is yeast. Then, the proofing is the process of the fermentative decomposition of glucose to $\mathrm{CO}_{2}$ and other components. This process is strictly time sensitive since the microorganisms get in contact with water and subtrates under preferable conditions of temperature and humidity. Therefore, the basic production in bakeries is commonly subject to a no-wait flow-shop scheduling problem (MDNWFSP) with setup time since there are very small tolerances for waiting time of yeast containing doughs during the production process [2].

However, in today's world, because of the globalization trend and competitive situation, more and more managers realize that traditionally centralized factory cannot be insufficiently flexible to changing production and the requirement from clients and market, so they have changed the single factory to decentralized production centers or distributed factories. These factories or production centers are unnecessary to lie in geographically in the same place or close to each other, and they can lie in different countries or continents. Therefore, the distributed manufacturing has been a common production mode, which can make the factories have effective marketing policies, reduce production cost and management risks, and flexibly adapt to market change. As seen in Fig. 2, we can model the above-mentioned basic bakery production in the distributed environment as a distributed MDNWFSP with setup time. In this distributed scheduling problem, there is a set of $F$ identical factories located at different places, and each factory includes an MDNWFSP with $m$ machines. Jobs need to be assigned to factories and a schedule must be established for each factory. In this paper, we will consider a distributed MDNWFSP with setup time. Certainly, this scheduling model also exists in other real production problems that need to satisfy the no-wait constraint, such as baker production, parallel computer system, and surgery scheduling.

Practical distributed scheduling problems show that the single optimization criterion is inadequate to represent real-world scenarios because scheduling problems in the manufacturing industry typically include multiple conflicting objectives. As a result, a multiobjective optimization problem needs to be addressed. The common objectives used in practical production contain makespan, total flow time, total costs, total tardiness, maximum lateness, and so on. For the distributed scheduling problem with the setup time, a decision-maker generally, first, hopes to minimize the makespan that is equal to the difference between the time when the last job is finished on the final machine and the setup time of the first job on the beginning machine. However, the decision-maker also
![img-0.jpeg](img-0.jpeg)

Fig. 2. Basic bakery production model in distributed environment.
concerns with the due date for their customers' satisfaction. The tardiness is the difference between the completion time and the due date which reflects strict requirements on the due date. As we know, it is not always preferable that the completion time is earlier than the due date, since a job completed earlier than its due date is possible to increase the inventory levels and floor space requirements, leading to losses [3]. Therefore, it is necessary to optimize both makespan and total weight tardiness (TWT).

Along with the development of economic globalization, coproduction between companies is more and more common nowadays. As a result, the distributed scheduling and distributed manufacturing systems receive more concern in recent research. So far, the study on distributed scheduling has two directions, one is scheduling models, and the other is optimization methods. For scheduling models, Naderi and Ruiz [4] first proposed distributed permutation flow-shop scheduling (DPFSP), and they proposed two job assignment rules and 12 heuristics to solve this problem. Lin and Ying [5] and Shao et al. [6] studied the distributed MDNWFSP and developed several iterated greedy (IG) algorithms to solve this problem. Hatami et al. [7], [8] presented the distributed assembly flow-shop scheduling problem, which has two stages: distributed permutation scheduling (production part) and assembly flow-shop scheduling (assembly part). After that, Lin et al. [9] proposed a backtracking search hyperheuristic where they designed several heuristic rules to construct the low-level heuristics, and the backtracking search algorithm was used as the high-level strategy. Ribas et al. [10] studied the distributed flow-shop scheduling problem with blocking constraint (DBFSP) and employed the iterated local search and the IG algorithm to solve it. Then, Ying and Lin [11] also proposed three version of hybrid IG algorithms to solve the DBFSP. They mixed the IG with variable Tabu list, the constant Tabu list, and the cooling schedule. It should note that, although there is a growing number of research studies in this subject, the studies are still limited to the simple DPFSP concept. Regarding the multiobjective distributed scheduling, the literature is limited. Deng et al. [12] presented

a competitive memetic algorithm (CMA) for addressing the multiobjective DPFSP (MODPFSP) with makespan and total tardiness. The CMA uses two populations corresponding to two different objectives, and several objective-specific operators for each population. Later on, Deng et al. [13] considered the carbon-efficient constraint in the DPFSP. They used CMA to address the MODPFSP with the objective of minimizing makespan and total carbon emissions. Cai et al. [14] studied the multiobjective distributed DPFSP with transportation and eligibility constraints. They considered three objectives that are makespan, maximum lateness, and the total costs of transportation costs and setup costs and proposed an improve NSGAII algorithm to solve this problem. Rifai et al. [15] presented a multiobjective distributed reentrant permutation flow-shop scheduling problem where a set of jobs with several reentrant layers are processed in the factories. Three objectives, i.e., the minimization of makespan, total cost, and average tardiness, are simultaneously taken account. Since most of distributed scheduling problems are NP-hard problems, the effectiveness of optimization methods plays a critical role in solving problems. Now, the optimization methods for distributed scheduling are still limited. Some heuristics and metaheuristics have been proposed, such as Nawaz-EnscoreHam (NEH) with branch and bound [16], variable neighborhood search [17], electron-magnetism metaheuristics [18], genetic algorithm (GA) [19], [20], scatter search [21], Tabu search [22], IG [23], hybrid immune algorithm (HIA) [24], estimation of distribution algorithm (EDA) [25], and chemical reaction optimization [26].
The EDA [27] is regarded as a statistics theory-based metaheuristic. The EDA, first, selects elite individuals from the population and, then, builds a probabilistic model by extracting the statistical information from elite individuals, finally, uses the probabilistic model to generate offspring individuals. Due to the good global search ability of the EDA, it has been used to address the amount of scheduling problems [27]-[31]. However, the EDA for multiobjective scheduling problems is very limited. Tiwari et al. [32] proposed a Pareto block-based EDA which employs a bivariate probabilistic model to produce blocks of jobs, and the nondominated sorting method was used to distinguish the solutions. Wang et al. [33] used the Pareto elite individuals to estimate the probabilistic information of solution space, and the population was separated into two subpopulations based on a splitting criterion. Several operators based on different optimization objectives were developed for these two subpopulations to produce the offspring. Hao et al. [34] proposed a multiobjective EDA to solve the bicriteria stochastic job-shop scheduling problem with the uncertainty of processing time. Wang et al. [35] presented a Pareto-archived EDA for addressing the multiobjective resource-constrained project scheduling problem with the objective of minimizing makespan and resource investment criteria.
According to the aforementioned investigation, we think there exist following directions for further researchers.

1) Although many distributed scheduling problems have been investigated, more realistic constraints need to be considered to meet real production. This paper considers
a multiobjective distributed MDNWFSP which widely exists in multiproduction factories or lines of bakery production, surgery scheduling, and so on.
2) Several metaheuristics are developed to improve computational time or solution quality of distributed flow-shop scheduling problems. However, still more researchers need to obtain a desirable result for different types of distributed scheduling problems.
Motivated by the application of the above-mentioned constraints in realistic production practice, this paper proposes a multiobjective distributed MDNWFSP with sequence-dependent setup time (MDNWFSP-SDST), whose optimization objectives are makespan and TWT.
Compared with previous studies on distributed flow-shop scheduling problems, the contribution of this paper can be summarized as follows. The MDNWFSP-SDST is proposed according to the real-time scenario of distributing scheduling. To the best of our knowledge, this paper is the first attempt to solve the MDNWFSP-SDST. Previous studies on the distributed scheduling problems do not consider all of no-wait constraint, multiobjective, and setup time. Moreover, we establish the mixed integer linear programming (MILP) model of MDNWFSP-SDST. A Pareto-based EDA (PEDA) is proposed, which provides a new direction for using the EDA to solve distributed scheduling problems. First, most of previous EDAs for distributed scheduling problems only consider jobs position information, but this paper considers the probability of jobs in empty, jobs in common factory, and two adjacent jobs. Second, we propose a sample method with a referenced template which does not appear in previous EDAs that are used to solve distributed scheduling problems. Third, we propose the multiobjective local search. Although these neighborhood searches may have existed in several methods, these neighborhood searches are not used for multiobjective optimization problem, and these neighborhood search greatly enhance the local searching ability. Furthermore, we compare the proposed PEDA with other multiobjective optimization algorithms, the experimental results show the PEDA can solve the MDNWFSP-SDST effectively and efficiently.
The remainder of this paper is organized as follows. Section II shows the detail of MDNWFSP-SDST. Section III presents each component of PEDA. Section IV calibrates the parameters of PEDA and carries out the comparison results. Section V presents the conclusion and future study.

## II. Multiobjective Distributed No-Wait Flow-SHOP Scheduling Problem With Sequence-Dependent SETUP TIME

## A. Basic Definition of Multiobjective Optimization Problem

To better explain the proposed MDNWFSP-SDST, we give a brief introduction of basic concept of a multiobjective problem. Generally, a multiobjective problem can be defined as follows (for minimization problem):

$$
\begin{gathered}
\min f(\boldsymbol{X})=\min \left[f_{1}(\boldsymbol{X}), f_{2}(\boldsymbol{X}), \ldots, f_{m}(\boldsymbol{X})\right] \\
\boldsymbol{X}=\left(x_{1}, x_{2}, \ldots, x_{n}\right) \in R^{n}
\end{gathered}
$$

s.t. $\begin{cases}g_{i}(\boldsymbol{X}) \geq 0 & i=1, \ldots, k \\ h_{i}(\boldsymbol{X})=0 & j=1, \ldots, p\end{cases}$
where $f_{m}(\boldsymbol{X})$ denotes the $m$ th subobjective function. $\boldsymbol{X}$ is a solution, which should satisfy the above-mentioned constraints. $R^{n}$ is the decision variable space. $k$ and $p$ represent the number of equality and inequality constraints, respectively.

1) Pareto Dominance: Let $\boldsymbol{a}$ and $\boldsymbol{b}$ denote two feasible solutions. The solution $\boldsymbol{a}$ dominates the solution $\boldsymbol{b}$ (denoted by $\boldsymbol{a} \prec \boldsymbol{b}$ ) if and only if $f_{i}(\boldsymbol{a}) \leq f_{i}(\boldsymbol{b}), \forall i \in\{1,2, \ldots, m\}$ and $f_{l}(\boldsymbol{a})<f_{l}(\boldsymbol{b}), \exists l \in\{1,2, \ldots, m\}$.
2) Pareto Optimal Solution: A solution $\boldsymbol{X}^{*} \in R^{n}$ is a Pareto optimal solution if there does not exist any other solution which dominates $\boldsymbol{X}^{*}$. The corresponding objective function is called the Pareto optimal front vector $f\left(\boldsymbol{X}^{*}\right)$.
The set of all Pareto optimal solutions is known as Pareto set, and the set of all Pareto optimal front vectors is known as the Pareto optimal front $(\boldsymbol{P F})$. The purpose of multiobjective optimization is to find $\boldsymbol{P F}$.

## B. Problem Description

The MDNWFSP-SDST is described as follows: a set of jobs $\left\{J_{1}, J_{2}, \ldots, J_{n}\right\}$ are available at time zero. They have been allocated to $F$ factories $\left\{F a_{1}, F a_{2}, \ldots, F a_{F}\right\}$ and be processed in each factory with the same processing order. Each factory contains an identical flow shop with $m$ machines [ $M_{1}, M_{2}, \ldots, M_{m}$ ]. Each job contains $m$ processing operations $\left\{O_{i, 1}, O_{i, 2}, \ldots, O_{i, m}\right\}$. When a job has been allocated to a certain factory, all its operations should be processed only in this factory. All operations of each job are no-wait constrained. That is to say, once processing a specific job is started, the job should be processed by the successive machines with no interruption between the consecutive operations. Every operation should not be stopped once it began. No job can be processed on more than one machine, and no machine can process more than one job at a time. The transit time between operations is ignored. The setup process has to be executed between the completion of one job and the start of another job on each machine. Here, we consider the SDSTs which depend on the current job being processed and on the next job in the sequence. The aim of MDNWFSP-SDST is to reasonably allocate jobs to factories and determine the processing order of jobs in each factory to optimize multiple scheduling objectives. The makespan (denoted by $C_{\max }$ ) and the TWT criteria are to be minimized in this paper. The makespan is production-oriented criterion, but it neglects an important aspect of production which is client satisfaction. The TWT has been used to satisfy different customer demand. These two objectives are not optimized simultaneously since the makespan is the main priority as long as the due date constraint is satisfied. Therefore, the MDNWFSP-SDST can be defined as multiobjective mathematical model with the objective of minimization of makespan and TWT.

A mathematical model is an abstract and good approach that uses mathematical language to describe a problem in detail. Inspired by the fifth mathematical model proposed in [4] for the DPFSP, we propose the MILP model of

MDNWFSP-SDST. The following notations are used to describe the MILP of MDNWFSP-SDST.

Since we use sequenced-based variables, dummy jobs 0 need to be defined. The MDNWFSP-SDST can be formulated as follows.

Objective Function

$$
\begin{aligned}
& \min \left(f_{1}, f_{2}\right), f_{1}=C_{\max }, f_{2}=\sum_{i=1}^{n} w_{i} \times T_{i} \\
& \text { s.t. } \sum_{i=0, i \neq k}^{n} X_{i, k}=1 \quad \forall k \\
& \sum_{k=0, i \neq k}^{n} X_{i, k} \leq 1 \quad \forall k \\
& \sum_{k=1}^{n} X_{0, k}=F \\
& \sum_{i=1}^{n} X_{i, 0}=F-1 \\
& X_{i, k}+X_{k, i} \leq 1 \quad \forall i \in\{1,2, \ldots, n-1\}, k>i \\
& C_{k, j}=C_{k, j-1}+p_{k, j} \quad \forall i, j, k \\
& C_{k, j} \geq C_{i, j}+p_{k, j}+s_{i, k, j} \\
& \quad+\left(X_{i, k}-1\right) \cdot M \quad \forall i, k, j, k \neq i \\
& C_{\max } \geq C_{i, m} \quad \forall j \\
& T_{i} \geq C_{i, m}-d_{i} \quad \forall i \\
& C_{i, j} \geq 0 \quad \forall i, j \\
& T_{i} \geq 0 \quad \forall i \\
& X_{i, k} \in\{0,1\} \quad \forall i, k, i \neq k
\end{aligned}
$$

The objective function, as presented in (4), is minimization of makespan $\left(f_{1}\right)$ and TWT $\left(f_{2}\right)$. Constraint sets (5) guarantee that every job must have exactly one processor. Constraint sets (6) indicate that each job has at most one succeeding job. Constraint sets (7) guarantee that dummy job 0] appears $F$ times in the sequence as a predecessor. Constraint sets (8) ensure that dummy job 0 should be a successor $F-1$ times. Constraint sets (9) ensure that a job cannot be both predecessor and successor of another job simultaneously. Constraint sets (10) state that the starting of processing a job on a machine is exactly to the completion time of processing the job on the preceding machine. This constraint ensures the no-wait constraint. Constraint sets (11) indicate the difference between the completion times of two consecutive jobs on a machine is larger than the summation of the setup time and processing time of the job processed as the later job. Constraint sets (12) define the maximum completion time of the whole process. Constraint sets (13) formulate the tardiness of every job. Constraint sets (14) and (15) guarantee that the completion time of each job on each machine and the tardiness of each job should be nonnegative. Constraint sets (16) define the binary decision variables.

In order to distinguish our model from the DPFSP model of [4], we describe their differences as follows. First, the objectives of MDNWFSP-SDST are $C_{\max }$ and TWT [see constraint sets (4), (12), (13), (14), and (15)], the objective of

DPFSP is $C_{\max }$. Then, the MDNWFSP-SDST should satisfy the no-wait constraint [see constraint sets (10)] that is the starting of processing a job on a machine is exactly equal to the completion time of processing the job on the preceding machine. The DPFSP only ensures that, for every job, the current operation cannot begin before the preceding operation completes. Third, the MDNWFSP-SDST considers the setup time [see constraint sets (11)], while the DPFSP ignores the setup time.

Since the MDNWFSP-SDST can be regarded as an extension of the no-wait permutation flow-shop scheduling for makespan and total tardiness, the latter problem is known to be a strongly NP-hard problem for $m \geq 3$ when the objectives are the makespan and the total tardiness [36], [37]. Moreover, in any case, since the MDNWFSP-SDST can reduce to the classical no-wait permutation flow-shop scheduling problem if $F=1$, therefore, the MDNWFSP-SDST is an NP-complete problem with the objective of makespan and total tardiness if $n>F$ and $m \geq 3$.

## C. Computing Makespan and Total Weight Tardiness

Let $\pi=\left\{\pi^{1}, \pi^{2}, \ldots, \pi^{F}\right\}$ be a given feasible schedule, where $\pi^{f}=\left\{\pi^{f}(1), \pi^{f}(2), \ldots, \pi^{f}\left(n^{f}\right)\right\}$ is the processing order of jobs in factory $f . n^{f}$ is the number of jobs belonging to factory $f$. According to [38], the no-wait constraint has a feature that the completion time of consecutive jobs $J_{i-1}$ and $J_{i}$ is fixed when the processing time and the setup time is predefined. Note that a dummy job 0 needs to be defined for each factory, whose processing time is zero. Let $D_{\pi} \wedge_{(i-1), \pi} \wedge_{(i)}$ denote the difference of completion time between consecutive jobs $\pi^{f}(i-1)$ and $\pi^{f}(i) . D_{\pi} \wedge_{(i-1), \pi} \wedge_{(i)}$ can be computed as follows:

$$
\begin{aligned}
D_{\pi} \wedge_{(i-1), \pi} \wedge_{(i)}=\max _{j=1,2, \ldots, m} & \left\{\sum_{p=j}^{m}\left(t_{\pi} \wedge_{(i), p}-t_{\pi} \wedge_{(i-1), p}\right)\right. \\
& \left.+t_{\pi} \wedge_{(i-1), j}+S_{\pi} \wedge_{(i-1), \pi} \wedge_{(i), j}\right\}
\end{aligned}
$$

Next, the makespan $C_{\max }(\pi)$ is computed as follows:

$$
\begin{aligned}
C_{\max }\left(\pi^{f}\right)= & \sum_{i=0}^{n^{f}-1} D_{\pi} \wedge_{(i), \pi} \wedge_{(i+1)}, \quad f=1,2, \ldots, F \\
C_{\max }(\pi)= & \max \left\{C_{\max }\left(\pi^{f}\right)\right\}, \quad f=1,2, \ldots, F
\end{aligned}
$$

$\operatorname{TWT}(\pi)$ is computed as (20) and (21)

$$
\begin{aligned}
C_{\pi} \wedge_{(i), m}= & \sum_{k=0}^{i-1} D_{\pi} \wedge_{(k), \pi} \wedge_{(k+1)} \\
T_{\pi} \wedge_{(i)}= & C_{\pi} \wedge_{(i)}-d_{\pi} \wedge_{(i)}, \\
& f=1,2, \ldots, F, \quad i=1, \ldots, n^{f} \\
\operatorname{TWT}(\pi)= & \sum_{i=1}^{n} w_{i} \times T_{i}
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 3. Example of MDNWFSP-SDST.
The purpose of the MDNWFSP-SDST is to find a scheduling $\pi^{+}$with the minimization of makespan and TWT. According to [38], $D_{\pi} \wedge_{(i-1), \pi} \wedge_{(i)}$ is only closely related to $\pi^{f}(i-1)$ and $\pi^{f}(i)$. In order to decrease the evaluation time in searching process, we can compute $D_{\pi(i-1), \pi(i)}$ for each pair of jobs in the initial phase.

In order to illustrate the MDNWFSP-SDST clearly, we show an example including seven jobs and two factories. The processing sequences of jobs in two factories are $\pi^{1}=$ $[1,2,3,4]$ and $\pi^{2}=[5,6,7]$. The Gantt chart of $\pi^{1}$ and $\pi^{2}$ is displayed in Fig. 3, where $D_{0,1}$ represents the difference of completion time between dummy jobs 0 and $1, D_{1,2}$ denotes the difference of completion time between jobs 1 and 2 , the rest $D$ can be done in the same manner. It can clearly be seen from Fig. 3, $C_{\max }\left(\pi^{1}\right)=D_{0,1}+D_{1,2}+D_{2,3}+D_{3,4}$ and $C_{\max }\left(\pi^{2}\right)=D_{0,5}+D_{5,6}+D_{6,7}$.

## III. Pareto-Based Estimation of Distribution Algorithm

The EDA is a metaheuristic that collects the distribution information of candidate solutions via sampling a probabilistic model established from promising solutions found so far [39]. With statistical analysis technique, the EDA makes the population track the promising search areas based on the available experience. The key step of EDA is the construction of probabilistic model. Since there exist different types of problems, the suitable probabilistic models and updating mechanism need to be constructed in order to estimate the distribution of solutions. The probabilistic model can reduce the destruction of building blocking and enhance the global exploration, but the local exploitation of EDA is still limited. For an effective optimization algorithm, it can make a tradeoff between the global exploration and local exploitation. In this section, we will propose a PEDA to address the MDNWFSP-SDST.

## A. Achieve Set AS

In this paper, we use an achieve set (AS) to store all Pareto optimal solutions that construct the Pareto optimal front in the objective space. The achieve set is iteratively updated during the searching process. For a given solution, if it is dominated by any solution in AS, we discard this solution. Otherwise, we remove all the solutions which are dominated by this solution and add this solution to AS.

## B. Solution Representation

The complete representation designed by Naderi and Ruiz [4] is used in this paper, which can represent all possible solutions. There are $F$ lists in

![img-2.jpeg](img-2.jpeg)

Fig. 4. Example of solution representation.
the solution representation, and every list has a partial permutation that is the processing order of jobs at each factory. In Fig. 4, we give an example with 10 jobs and 3 factories. The operation sequence of jobs for factories 1,2 , and 3 is $5 \rightarrow 2 \rightarrow 9 \rightarrow 4,1 \rightarrow 8 \rightarrow 10$, and $6 \rightarrow 3 \rightarrow 7$, respectively.

## C. Population Initialization

In this paper, we improve a biobjective heuristic PWQ presented by Pan et al. [40], it is adopted to address the MDNWFSP in single factory. The PWQ first generates two job sequences $\sigma^{P}$ and $\sigma^{E}$ by sorting jobs in descending sums of their total processing time and the EDD heuristic [41] and, then, computes the weighted sum of job position value $\phi_{j}=w_{1} \times \varphi_{j}\left(\sigma^{P}\right)+w_{2} \times \varphi_{j}\left(\sigma^{E}\right), j=1,2, \ldots, n . \varphi_{j}\left(\sigma^{P}\right)$ and $\varphi_{j}\left(\sigma^{E}\right)$ denote the position values of job $j$ in $\sigma^{P}$ and $\sigma^{E} . w_{1}$ and $w_{2}$ denote the weight of $f_{1}$ and $f_{2}$, which are decided by the population size $(P S)$ and the index $l$ of current individual, i.e., $\left(w_{1}, w_{2}\right)$ as $(l /(\mathrm{PS}-1), 1-(l /(\mathrm{PS}-1)))$. Next, a sequence $\sigma^{0}$ is produced by sorting the jobs in ascending weighted sum of job position value. Finally, each job in $\sigma^{0}$ is inserted into a new sequence by using the insertion procedure of NEH [42]. When evaluating the quality of intermediate sequence $\sigma$, the PWQ heuristic employs a weighted sum to combine $f_{1}$ and $f_{2}$, as shown in the following equation:

$$
f(\sigma)=w_{1} \times f_{1}(\sigma)+w_{2} \times f_{2}(\sigma)
$$

However, (23) is not reasonable to all objectives that have different orders of magnitude or units. In order to maintain consistency, we normalize the objectives, as shown in the following equation:

$$
f(\sigma)=w_{1} \times \frac{f_{1}(\sigma)-f_{1}^{\min }}{f_{1}^{\max }-f_{1}^{\min }}+w_{2} \times \frac{f_{2}(\sigma)-f_{2}^{\min }}{f_{2}^{\max }-f_{2}^{\min }}
$$

where $f_{1}^{\min }$ and $f_{1}^{\max }$ denote the minimum and the maximum $C_{\max }$ of all current subsequences that are generated by inserting a job to $\sigma . f_{2}^{\min }$ and $f_{2}^{\max }$ denote the minimum and the maximum TWT of all current subsequences that are generated by inserting a job to $\sigma$. We extend PWQ heuristic to distributed flow-shop scheduling, shown as Pseudocode 1. First, the improved PWQ generates two job sequences $\sigma^{P}$ and $\sigma^{E}$ by sorting jobs in descending sums of their processing time and due date. Second, the weighted sum of job position value of each job is computed, and then a permutation $\sigma^{0}$ by sorting jobs in ascending weighted sum of their position values is generated. Third, the first $F$ jobs of $\sigma^{0}$ are extracted and inserted into each factory of new sequence $\pi$, i.e., $\pi^{f}(1)=$ $\sigma^{0}(f), f=1,2, \ldots, F$, and next, the rest jobs of $\sigma^{0}$ are inserted into all possible positions of $\pi$, the position resulting in the minimum weighted sum of $f_{1}$ and $f_{2}$ is selected.

Different from the original version of PWQ, the improved PWQ uses (24) to normalize the objectives to maintain consistency, and the jobs are assigned to all possible positions of all factories by using the insertion of procedure of NEH.

Pseudocode 1 Improved PWQ
Input: The population size $P S$
Output: The initial population POP

1: Generate a job sequence $\sigma^{P}$ by sorting jobs in descending sums of their processing times.
2: Generate a job sequence $\sigma^{E}$ by sorting jobs in descending sums of their due date. Let $l=1$.
3: while $l \leq \mathrm{PS}$ do
4: Set a weight vector $\left(w_{1}, w_{2}\right)$ as $(l /(\mathrm{PS}-1), 1-(l /(\mathrm{PS}-$ 1))).

5: Calculate the weighted sum of job position values $\phi_{j}=$ $w_{1} \times \varphi_{j}\left(\sigma^{P}\right)+w_{2} \times \varphi_{j}\left(\sigma^{E}\right)$ for $j=1,2, \cdots, n$, where $\varphi_{j}\left(\sigma^{P}\right)$ and $\varphi_{j}\left(\sigma^{E}\right)$ denote the position values of job $j$ in permutation $\sigma^{P}$ and $\sigma^{E}$.
6: Generate a permutation $\sigma^{0}$ by sorting jobs in ascending weighted sum of their position values $\phi_{j}$. Let $\pi$ represent the new generated individual.
7: The first $F$ jobs $\left[\sigma^{0}(1), \sigma^{0}(2), \cdots, \sigma^{0}(F)\right]$ of $\sigma^{0}$ are taken and let $\pi^{f}(1)=\sigma^{0}(f), f=1,2, \cdots, F$.
8: Take job $\sigma^{0}(k), k=F+1, F+2, \cdots, n$, insert it into all possible positions of $\pi$, and the position resulting in the minimum weighted sum of the two objectives values $f(\pi)$ is selected. Insert $\sigma^{0}(k)$ to this position.
9: $\quad \operatorname{POP}(\mathbf{l})=\pi, l=l+1$
10: end while

## D. Probabilistic Model and Updating Mechanism

Different from the GA which generates offspring individual by crossover and mutation operators, the EDAs generate offspring via sampling a probabilistic model which greatly influences the performance of EDAs. Therefore, it is critical to design an effective probabilistic model for EDA. This section proposes a hybrid probabilistic model to describe the promising search areas of MDNWFSP-SDST. According to the characteristic of different problems, different probabilistic models should be established to estimate the reasonable promising probability distribution. Since the distributed no-wait flowshop scheduling has two tasks: assigning jobs to factory and determining job sequence in the factory, we consider three kinds of position relationship between jobs and factories, i.e., the jobs in empty factory, the two jobs in same factory, and the adjacent jobs. Since the factories are identical, two solutions have identical job sequences but the sequences exist in different factories. In fact, these two solutions are same and they have the same makespan and TWT. Therefore, the above-mentioned three kinds of relationship could reduce the complexity of establishing model. In the following paragraphs, we establish three probabilistic models to describe the solution space.

1) The probability $\boldsymbol{P E}$ of jobs in empty factory, donated as (25), where $p e_{i}$ denotes the probability of job $i$ in

empty factory, i.e., the probability of jobs in the first position of any factory. $p e_{i}$ can be computed as (26), where $I E_{i}(l)$ is an indicator function which shows whether the job $i$ appears in the first position of any factory in the $l$ th individual in AS, and Asize represents the size of AS. For all values of $i, p e_{i}$ is initialized to $1 /(F n)$, which ensures that the whole solution space can be sampled uniformly

$$
\begin{aligned}
\boldsymbol{P} \boldsymbol{E} & =\left[p e_{1}, p e_{2}, \ldots, p e_{n}\right] \\
p e_{i} & =\frac{\sum_{l=1}^{\text {Asize }} I E_{i}(l)}{\text { Asize }} \\
I E_{i}(l) & = \begin{cases}1, & \text { job } i \text { in the first position of any factory } \\
& \text { in the } l \text {-th individual in AS } \\
0, & \text { otherwise. }\end{cases}
\end{aligned}
$$

2) The probability $\boldsymbol{P} \boldsymbol{C}$ of two jobs in the same factory, denoted as (28), where $p c_{i, i^{\prime}}$ denotes the probability of job $i$ and job $i^{\prime}$ in the same factory. $p c_{i, i^{\prime}}$ can be computed as (29), where $I C_{i, i^{\prime}}(l)$ is an indicator function which is equal to 1 when job $i$ and job $i^{\prime}$ appears in the same factory in the $l$ th individual in AS. For all values of $i$ and $i^{\prime}, p c_{i, i^{\prime}}$ is initialized to $1 /\left(n^{2}\right)$

$$
\begin{aligned}
\boldsymbol{P} \boldsymbol{C} & =\left[\begin{array}{cccc}
p c_{1,1} & p c_{1,2} & \cdots & p c_{1, n} \\
p c_{2,1} & p c_{2,2} & \cdots & p c_{2, n} \\
\vdots & \vdots & \vdots & \vdots \\
p c_{n, 1} & p c_{n, 2} & \cdots & p c_{n, n}
\end{array}\right] \\
p c_{i, i^{\prime}} & =\frac{\sum_{l=1}^{\text {Asize }} I C_{i, i^{\prime}}(l)}{\sum_{i^{\prime}=1}^{n} \sum_{l=1}^{\text {Asize }} I C_{i, i^{\prime}}(l)} \\
I C_{i, i^{\prime}}(l) & = \begin{cases}1, & \text { job } i \text { and job } i^{\prime} \text { appear in the same } \\
& \text { factory in the } l \text {-th individual in AS } \\
0, & \text { otherwise. }\end{cases}
\end{aligned}
$$

3) The probability $\boldsymbol{P} \boldsymbol{A}$ of two adjacent jobs, denoted as (31), where $p a_{i, i^{\prime}}$ represents the probability that job $i^{\prime}$ appears immediately after the job $i . p a_{i, i^{\prime}}$ can be computed as (32), where $I A_{i, i^{\prime}}(l)$ is an indicator function which is equal to 1 when job $i^{\prime}$ appears immediately after the job $j$ in the $l$ th individual in AS. For all values of $i^{\prime}$ and $i, p a_{i, i^{\prime}}$ is initialized to $1 /\left(n^{2}\right)$

$$
\begin{aligned}
\boldsymbol{P} \boldsymbol{A} & =\left[\begin{array}{cccc}
p a_{1,1} & p a_{1,2} & \cdots & p a_{1, n} \\
p a_{2,1} & p a_{2,2} & \cdots & p a_{2, n} \\
\vdots & \vdots & \vdots & \vdots \\
p a_{n, 1} & p a_{n, 2} & \cdots & p a_{n, n}
\end{array}\right] \\
p a_{i, i^{\prime}} & =\frac{\sum_{l=1}^{\text {Asize }} I A_{i, i^{\prime}}(l)}{\sum_{i^{\prime}=1}^{n} \sum_{l=1}^{\text {Asize }} I A_{i, i^{\prime}}(l)} \\
I A_{i, i^{\prime}}(l) & = \begin{cases}1, & \text { job } i^{\prime} \text { appears immediately after job } i \\
& \text { in } l \text {-th individual in AS } \\
0, & \text { otherwise. }\end{cases}
\end{aligned}
$$

The probabilistic model should be adjusted in each generation to track the promising searching region. The Heb rule is used to update probabilistic models, shown as (34)-(36), where $t$ represents the number of generation, $\alpha \in(0,1)$ is a constant learning rate of probabilistic models

$$
\begin{aligned}
& \boldsymbol{P} \boldsymbol{E}(t+1)=\alpha \cdot \boldsymbol{P} \boldsymbol{E}(t-1)+(1-\alpha) \cdot \boldsymbol{P} \boldsymbol{E}(t) \\
& \boldsymbol{P} \boldsymbol{C}(t+1)=\alpha \cdot \boldsymbol{P} \boldsymbol{C}(t-1)+(1-\alpha) \cdot \boldsymbol{P} \boldsymbol{C}(t) \\
& \boldsymbol{P} \boldsymbol{A}(t+1)=\alpha \cdot \boldsymbol{P} \boldsymbol{A}(t-1)+(1-\alpha) \cdot \boldsymbol{P} \boldsymbol{A}(t)
\end{aligned}
$$

## E. Sample With Referenced Template

Sampling the probabilistic model is one of the key steps in the EDA. From [43], it can be known that the EDA has a shortcoming which is that occasionally solutions generated by sampling that are not very representative of the current probabilistic model, but nevertheless are good, are not fully exploited in the future iterations. To deal with this limitation, we present a sampling method with reference template according to the literature [44]-[47]. This sampling method first randomly selects one solution from the population as the referenced template individual. Then, $d$ jobs are randomly selected from the referenced individual regardless of factories, and the rest jobs are copied to a new solution. Finally, the selected $d$ jobs are inserted to the new solution according to the probabilistic model. During the procedure of inserting a job, we first decide which factory the job should be placed in and, then, ensure which position the jobs should be inserted into this factory. The procedure of sample with referenced template is shown as Pseudocode 2.

## F. Multiobjective Local Search

The purpose of solving multiobjective optimization problems is to find a Pareto front where the set of nondominated solutions is as close as possible to the true Pareto front and at the same time distributed as evenly as possible [48]. Since the local exploitation of EDA is limited, this section proposes five neighborhood search methods to improve the quality of solutions, which employs the operator of insert and swap move between factories or in the factory. Due to the multiobjectives, we keep all the solutions in the searching procedure, and these solutions are added into a temporary nondominated set. For a given solution to be improved, the neighborhood search methods can be described as follows.

1) Pareto Insert Search: First, every job is taken out from its original position successively, then reinserted all possible positions of the sequences of all factories. During insertion, all the solutions are stored. This procedure continues until all jobs are checked. After insertion, all the solutions generated by this procedure are added into a nondominated set, and return this nondominated set.
2) Pareto Swap Search: Each job is exchanged with other jobs of all factories. During swapping two jobs, all the solutions are kept. This procedure continues until all jobs are checked. All solutions generated by this procedure are added into a nondominated set and return this nondominated set.

Pseudocode 2 Sample With Referenced Template
Input: the number of selected jobs $d$, a referenced template individual $\pi_{r}$ from POP, $\boldsymbol{P} \boldsymbol{E}, \boldsymbol{P} \boldsymbol{C}, \boldsymbol{P} \boldsymbol{A}$.
Output: A new individual $\pi$.
1: randomly select $d$ jobs from $\pi_{r}$ and add them into $\sigma=$ $\left[\sigma_{1}, \sigma_{2}, \cdots, \sigma_{d}\right]$.
2: copy the rest jobs in $\pi_{r}$ to $\pi$.
3: for each job $\sigma_{i}$ do
4: for $f=1$ to $F$ do
5: $\quad p=1.0$
6: for $j=1$ to $n^{f}$ do
$p=p \times p c_{\pi^{f}(j), \sigma_{i}}$
end for
record the probability of $\sigma_{i}$ in factory $f$, i.e. Record $P[f]=p$.
end for
select the factory with the maximum probability in Record $\boldsymbol{P}$, and denoted as $f_{r}$.
Let Record $P^{\prime}[1]=p e_{\sigma_{i}}$
for $j=2$ to $n^{f_{r}}$ do
Record $P^{\prime}[j]=p a_{\pi^{f_{r}}(j), \sigma_{i}}$
end for
select the position recordpos with the maximum probability in $\boldsymbol{R e c o r d} \boldsymbol{P}^{\prime}$
insert $\sigma_{i}$ into the position recordpos in factory $f_{r}$ in $\pi$.
end for
3) Pareto Insert Search for Tardiness: The job with the maximum tardiness is taken out from its original position, and then reinserted all possible positions of the sequence of all factories. During inserting a job, all of the solutions are stored. This procedure continues until all jobs are checked. All solutions generated by this procedure are added into a nondominated set and return this nondominated set.
4) Pareto Swap Search for Tardiness: The job with the maximum tardiness is exchanged with other jobs of all factories. During exchanging two jobs, all the solutions are kept. This procedure continues until all jobs are checked. All solutions generated by this procedure are added into a nondominated set and return this nondominated set.
5) Pareto Insert Search for Critical Factory: The critical factory refers to the factory with maximum makespan. Each job is removed in the critical factory from its original position successively, and then reinserted all possible positions of the sequences of all factories. During insertion, all of the solutions are stored. This procedure continues until all jobs are checked. All solutions generated by this procedure are added into a nondominated set and return this nondominated set.

In order to apply the above-mentioned neighborhood search methods, we present a multiobjective local search algorithm to optimize the solutions in the archive set and new generated solutions. If a solution $s$ is fully explored by the
above-mentioned neighborhood search methods, the solution is marked. The solutions in the returned nondominated set which are not weakly dominated by $s$ or by any solution in the archive set are added to the archive set. The solutions in the AS dominated by the newly added solution are removed. We also save all solutions obtained by multiobjective local search in LPOP. The procedure of multiobjective local search is shown as Pseudocode 3.

Pseudocode 3 Multiobjective Local Search
Input: A solution $s$, the achieve set AS, the population generated by multiobjective local search LPOP.
Output: AS, LPOP

1: if $s$ is not visited then
$N S e t_{1}=$ Pareto Insert Search $(\boldsymbol{s})$
$N S e t_{2}=$ Pareto Swap Search $(\boldsymbol{s})$
$N S e t_{3}=$ Pareto Insert Search for Tardiness $(\boldsymbol{s})$
$N S e t_{4}=$ Pareto Swap Search for Tardiness $(\boldsymbol{s})$
$N S e t_{5}=$ Pareto Insert Search for Critical Factory $(\boldsymbol{s})$
$N S e t_{5}=$ Pareto Insert Search for Critical Factory $(\boldsymbol{s})$
Mark $\boldsymbol{s}$ as being visited.
for $s^{\prime} \in\left\{N s e t_{1}, N s e t_{2}, N s e t_{3}, N s e t_{4}, N s e t_{5}, s\right\}$ do
if $s^{\prime}$ is not dominated by any solution in AS then
Add $s^{\prime}$ into AS, and delete the solutions in AS that are dominated by $s^{\prime}$.
Add $s^{\prime}$ into LPOP.
end if
end for
end if

## G. Framework of PEDA

To make the EDA applicable to solve MDNWFSP-SDST under consideration, this paper proposes a PEDA. The framework of PEDA is shown as Pseudocode 4. The PEDA mainly includes four components, i.e., initialize population, construct the probabilistic model, sample from the probabilistic model, and multiobjective local search. In the initial phase, we use an improved PWQ heuristic to generate the initial population and store the nondominated solutions from the population in the archive set. Then, the probability of jobs in the empty factory, the probability of two jobs in the same factory, the probability of two adjacent jobs is computed by extracting the distribution of solutions in the archive set. Next, the offspring individuals are produced by sampling from the probabilistic model. Finally, the multiobjective local search is applied to the solutions in the offspring population and the archive set. The above-mentioned procedure is repeated until the termination criterion is satisfied. Fig. 5 shows the flowchart of PEDA.

## H. Complexity of PEDA

Suppose that there are $n$ jobs, $m$ machines, and $F$ factories in the MDNWFSP-SDST. Because of using the speed-up method to compute makespan and total tardiness, so the computational complexity of computing $C_{\max }$ and TWT are $O(n)$, respectively. In the initial phase, the computational complexity

## Pseudocode 4 Framework of PEDA

Input: The parameter PS, $\alpha, d$
Output: The archive set AS
1: Set the archive set $\mathbf{A S}$ to be empty.
2: Generate the population POP by using improved PWQ heuristic, and evaluate each solution in the population.
3: Save the nondominated solutions determined from the initial population in the AS.
4: Initialize the probabilistic matrix $\boldsymbol{P E}, \boldsymbol{P C}, \boldsymbol{P A}$.
5: while the termination criterion is not met do
6: Construct the probabilistic matrix $\boldsymbol{P E}, \boldsymbol{P C}, \boldsymbol{P A}$ by extracting the distribution of solutions in AS.
7: Update $\boldsymbol{P E}, \boldsymbol{P C}, \boldsymbol{P A}$
8: Generate the offspring population POP with PS solutions by sampling from $\boldsymbol{P E}, \boldsymbol{P C}, \boldsymbol{P A}$ and evaluate the offspring individuals.
9: Store the nondominated solutions determined from offspring population in AS.
10: For each solution in the offspring population, perform multiobjective local search, add the solutions generated by multiobjective local search to AS.
11: For each solution that not be performed local search in AS, perform multiobjective local search, add the solutions generated by multiobjective local search to LPOP.
12: UPOP $=$ POP $\cup$ OPOP $\cup$ LPOP
13: Perform fast nondominated sorting on UPOP.
14: $\mathbf{P O P}=\mathbf{U P O P}[1:$ PS $]$, set $\mathbf{O P O P}$ and $\mathbf{L P O P}$ to be empty.
15: end while
of computing weight, sorting the jobs, and inserting operation are $O(n), O(n \log n)$, and $O\left(n^{2} \times 2 n\right)$, respectively. Then, the computational complexity of generating $p$ individuals is $O\left(p\left(n+n \log n+n^{2} \times 2 n\right)\right)$. The computational complexity of computing the probability matrix $\boldsymbol{P E}$ of job in empty factory, $\boldsymbol{P C}$ of two jobs in the same factory, and $\boldsymbol{P A}$ of two adjacent jobs are $O\left(3 p n^{2}\right)$. The computational complexity of generating $p$ individuals by sampling is $O(2 p n)$. The computational complexity of Pareto Insert Search, Pareto Swap Search, Pareto Insert Search for Tardiness, Pareto Swap Search for Tardiness, and Pareto Insert Search for Critical Factory is $O\left(n^{3}\right), O\left(n^{2}\right), O\left(n^{3}\right)$, and $O\left(n^{3}\right)$. Then, the computational complexity of applying the local search on the archive set and offspring is $O\left((a+p) O\left(4 n^{3}+n^{2}\right)\right)$, where $a$ is the size of archive set. The computation complexity of fast nondominated sorting is $O\left(2 \beta^{2}\right)$, where $\beta$ is the size of UPOP. In summary, in $k$ iterations, the computation complexity of PEDA is shown as follows:

$$
\begin{aligned}
& O(k, n, m, F, p) \\
& =O\left(p\left(n+n \log n+n^{2} \times n\right)\right)+O(k)\left[O\left(3 p n^{2}\right)+O(2 p n)\right. \\
& \left.\quad+(a+p) O\left(n^{3}+n^{3}+n^{2}+n^{2}+n^{3}\right)+O\left(2 \beta^{2}\right)\right] \\
& \approx O\left(n^{3}\right)+O(k) O\left[p n+p n^{2}+(a+p) n^{3}+2 \beta^{2}\right] \\
& \approx O\left(k(a+p) n^{3}+2 k \beta^{2}\right)
\end{aligned}
$$

![img-3.jpeg](img-3.jpeg)

Fig. 5. Flowchart of PEDA.

## IV. EXPERIMENTAL COMPARISON

## A. Experiment Setup

In order to demonstrate the effectiveness of PEDA, this section carries out an experiment to test the performance of PEDA with testing instances. Since there is no published benchmark instance for the MDNWFSP-SDST, we generate two sets of testing instances (denoted as SSD50 and SSD125) based on the literature [4], [49]. Each set includes several combinations of the number of jobs, machines, and factories. The combinations of $n \times m$ are $\{20,50,100\} \times$ $\{5,10,20\}, 200 \times\{10,20\}$. Each combination consists of 10 different replicates which results in 110 instances in total. We increase these 110 instances with six classes of factories $F=\{2,3,4,5,6,7\}$. It leads to 660 instances in total. The processing time, the setup time, the weight, and the due date of each job come from the literature [49]. The setup time of SSD50 and SSD125 is uniformly distributed in the range $[0-49]$ and $[50-124]$, respectively. The weight of each job is generated by a uniform $U[1,10]$ distribution, and a tight due date $d_{j}$ is adopted for each job $j$ following the expression: $d_{j}=p_{j} \times(1+\operatorname{random} \times 3)$ where $p_{j}$ denotes the total processing time of job $j$, and random is a random number uniformly in $[0,1]$. All of the testing instances can be downloaded from the website at http://soa.iti.es. Note that all algorithms are implemented with Java language (JDK 1.6) and performed on a server with two Intel Xeon E5-2650 CPUs and 128 G RAM.

TABLE I
Parameter Setting of Compared Algorithms


TABLE II
ANOVA ReSults OF $I_{H}$


TABLE III
ANOVA ReSults of $I_{c}^{1}$


## B. Adaption of Existing Compared Algorithms

Because this paper is the first attempt to solve the MDNWFSP-SDST, so there is no specific existing algorithm presented in former studies. We extend nine algorithms to solve the MDNWFSP-SDST, which include NSGAII of Deb et al. [48], PESAII of Corne et al. [50], SPEAII of Zitzler et al. [51], MOEA/D of Zhang et al. [52], hMGA of Yandra and Tamura [53], INSGAII of Cai et al. [14], PGA_ALS of Pasupathy et al. [54], CMA of Deng and Wang [12], and HIA of Xu and Wang [24]. In these algorithms, NSGAII, PESAII, SPEAII, and MOEA/D are proposed for multiobjective function optimization, PGA_ALS and hMGA are presented for addressing the multiobjective permutation flow-shop scheduling problem, INSGAII and CMA are developed for addressing the multiobjective DPFSP, and the HIA is proposed for the DPFSP. The HIA combines the immune search operators and local search. Since the HIA
![img-4.jpeg](img-4.jpeg)

Fig. 6. Main effects plot for hypervolume $\left(I_{H}\right)$ and unary epsilon $\left(I_{c}^{1}\right)$ of each parameter.
is proposed for the single-objective optimization, we use the fast nondominated sorting and crowding distance to sort the individuals in the parent and offspring population, and the archive set is used to collect the nondominated solutions in the searching process.

Note that since hMGA, INSGAII, MOEA, NSGAII, PESAII, PGA_ALS, and SPEAII are not initially used to solve the distributed flow-shop scheduling problem, we adopt the same crossover and mutation operation. The crossover operator proposed by Gao and Chen [19] is used in this section. Suppose there are two parent individuals $\boldsymbol{s} \mathbf{1}$ and $\boldsymbol{s} \mathbf{2}$. The crossover operator first randomly selects points for each factory of the parent $\boldsymbol{s} \mathbf{2}$, which are used to divided job sequence of $\boldsymbol{s} \mathbf{1}$. The set of corresponding jobs on right side of $\boldsymbol{s} \mathbf{2}$ is removed from $\boldsymbol{s} \mathbf{1}$. Then, the remaining jobs in each factory of $\boldsymbol{s} \mathbf{1}$ are placed in the order of their appearance and inherited to the child. The right-side jobs of $\boldsymbol{s} \mathbf{2}$ are conjoined to the corresponding factories of the child. The mutation operator randomly swaps some pairs of jobs, and the number of pair is $n / 4$. It should note that we carefully follow all explanations and details described in the original literature to implement these compared algorithms, their parameters are strictly calibrated by the analysis of variance (ANOVA) method. Due to the limited space, we just list the final parameter setting of each algorithm in Table I. In order to make an effective comparison, the same experimental conditions are employed in testing.

## C. Performance Evaluation Indicators

In our experiment, the hypervolume indicator $I_{H}$ [55] and the unary epsilon indicator $I_{c}^{1}$ [36] are considered as performance evaluation indicators, which have been widely used to assess the performance of multiobjective algorithms.

The hypervolume indicator $I_{H}$ was proposed by Zitzler and Thiele [55], which measures the normalized volume of the solution space dominated by the Pareto

![img-5.jpeg](img-5.jpeg)

Fig. 7. Mean plot and Tukey's HSD results for hypervolume and unary epsilon of PEDA_I, PEDA_A, PEDA_N, PEDA_S, and PEDA.
![img-6.jpeg](img-6.jpeg)

Fig. 8. Mean plot of hypervolume and unary epsilon for compared algorithms.
![img-7.jpeg](img-7.jpeg)

Fig. 9. Pareto fronts obtained by using nine comparative algorithms for the 110th instance from SSD50. (a) $f=2$. (b) $f=3$. (c) $f=4$. (d) $f=5$. (e) $f=6$. (f) $f=7$.
approximation generated by an algorithm. As [49], the point $(1.2,1.2)$ is considered as the reference point. Suppose there is a set of Pareto frontiers $\boldsymbol{P F}$, and $p f \in \boldsymbol{P F}$ is a frontier. $s$ is a solution belonging to $p f \in \boldsymbol{P F}$. The hypervolume indicator for biobjectives is shown as (37), where $f_{1}^{i}$ and $f_{2}^{i}$ denote the objective values of the solution $s$ belonging to the Pareto frontier $p f$, and $f_{1}^{\min }, f_{1}^{\max }, f_{2}^{\min }, f_{2}^{\max }$ denote the best (minimum) and the worst (maximum) value of $f_{1}$ and $f_{2}$ over all the Pareto
frontiers $\boldsymbol{P F} . N S o l$ is the number of solutions in the Pareto frontier $p f$. It should note that when comparing two Pareto frontiers, the higher value of $I_{H}$ means a better frontier
$I_{H}=\sum_{i=1}^{N s o l} \frac{f_{1}^{i}-1.2 \times f_{1}^{\min }}{1.2 \times\left(f_{1}^{\max }-f_{1}^{\min }\right)}+\frac{f_{2}^{i}-1.2 \times f_{2}^{\min }}{1.2 \times\left(f_{2}^{\max }-f_{2}^{\min }\right)}$.
The unary epsilon indicator $I_{\epsilon}^{1}$ was proposed by Zitzler et al. [36], which computes the distance between an

![img-8.jpeg](img-8.jpeg)

Fig. 10. Mean interaction plot of hypervolume and unary epsilon between algorithms and instances.
![img-9.jpeg](img-9.jpeg)

Fig. 11. Mean interaction plot of hypervolume and unary epsilon between algorithms and running time.
![img-10.jpeg](img-10.jpeg)

Fig. 12. Mean interaction plot of hypervolume and unary epsilon between algorithms and jobs.
![img-11.jpeg](img-11.jpeg)

Fig. 13. Mean interaction plot of hypervolume and unary epsilon between algorithms and factories.
obtained Pareto front and the referenced Pareto front. As [49], because the optimal Pareto front for each instance is not known, so we collect the whole of nondominated solutions
generated by all considered algorithms as a reference set. Each objective of solutions should be also normalized to one unit by the following equation: $f_{j}^{\prime}=\left(f_{j}-f_{j}^{\min }\right) /\left(f_{i}^{\max }-f_{i}^{\min }\right)+1$.

TABLE IV
Computational Result of PEDA_I, PEDA_A, PEDA_N, PEDA_S, AND PEDA

The values of $I_{c}^{1}$ are between 1 and 2 . The value close to 1 means the considered frontier is close to the reference set, and the value being close to 2 means that the set of solution is distant. Let $\mathbf{B}$ be the reference set and $\mathbf{A}$ be an approximation to the Pareto front. $I_{c}^{1}$ for two objectives is shown as (38), where $f^{1}=\left(f_{1}^{1}, f_{2}^{1}\right)$ and $f^{2}=\left(f_{1}^{2}, f_{2}^{2}\right)$ represent two objective values belonging to $\mathbf{A}$ and $\mathbf{B}$, respectively, and $m$ denote the number of objectives

$$
I_{c}^{1}(\mathbf{A}, \mathbf{B})=\max _{f^{2} \in \mathbf{B}} \min _{f^{1} \in \mathbf{A}} \max _{1 \leq i \leq m} \frac{f_{i}^{1}}{f_{i}^{2}}
$$

## D. Calibration of PEDA

To develop an efficient and effective algorithm, we must find the suitable parameters setting for the PEDA. The PEDA includes three parameters that are the $P S$ the number of selected jobs $d$, and the learning rate $\alpha$. This section employs a full factorial design of experiment to calibrate the PEDA. The levels of each parameter are $P S=\{20,30,40,50\}, d=$ $\{4,6,8,10\}$, and $\alpha=\{0.1,0.2,0.3,0.4,0.5\}$. In order to prevent overfitting, we randomly generate 22 other testing instances based on the structure of SSD50 and SSD125, and each combination includes one instance. The number of factories are chosen as 4 and 5 . Thus, there are 44 testing instances used to test the parameters of PEDA. Each instance is run with five times and the maximum running time $T_{\max }=$ $n \times m \times f \times 15 \mathrm{~ms}$. The ANOVA method is used to analyze the computational results, in which the $p$-value being close to zero demonstrates that there exists a statistical significant difference between each level of factor or interaction. If the $p$-value is closed to zero, the $F$-ratio will be used to determine the significance.

Tables II and III show the ANOVA results of $I_{H}$ and $I_{c}^{1}$ for the PEDA. From these figures, it can be observed that the PS and the number of selected jobs are significant parameters since the $p$-values of their $I_{H}$ and $I_{c}^{1}$ are less than 0.05 . The number of selected jobs $d$ is the largest significant parameter which has the largest $F$-value. From the main effect plot of $d$ in Fig. 6, the smaller value leads to better results, because the small $d$ may benefit to save local search information. The choice of $d=4$ results in the best result. The PS is the second significant parameter. It demonstrates
that PS has the obvious influence on the performance of the PEDA. From Fig. 6, PS $=30$ leads to better solutions than other candidate levels. The small-scaled population may reduce the diversity of population after performing an amount of local search on it, but if there are overmuch individuals in the population, performing many local searches on them may cost more time. The learning rate $\alpha$ has no significant impact on the performance of the PEDA, so the value of $\alpha$ is set as 0.5 according to the main effect plot. According to the above-mentioned investigation, the parameters setting of PEDA is PS $=30, d=4$, and $\alpha=0.5$.

## E. Performance Analysis of Each Part of PEDA

This section tests and analyzes the contribution of critical components of PEDA: the improved PWQ heuristic, the combination of local search and PEDA, and the sample method with referenced template. Four variants of PEDA are generated: PEDA_I, PEDA_A, PEDA_N, and PEDA_S. PEDA_I randomly generates the initial population. PEDA_A and PEDA_N are obtained by removing local searching method applied to the achieve set and the offspring individuals, respectively. In PEDA_S, each offspring individual is produced through sampling the probabilistic model directly. First, we determine the first job of each factory by sampling the probability matrix $\boldsymbol{P} \boldsymbol{E}$ of job in empty factory. Then, the jobs in the same factory are decided through sampling the probability matrix $\boldsymbol{P} \boldsymbol{C}$ of job in the same factory. Finally, we get the processing order via sampling the probability matrix $\boldsymbol{P} \boldsymbol{A}$ of adjacent jobs. It should note that the roulette wheel selection is used as the sampling method. All considered algorithms adopt the same termination criterion, i.e., the maximum running time $T_{\max }=n \times m \times f \times 25 \mathrm{~ms}$. The $\mathbf{S S D 5 0}$ is employed to verify the performance of each considered algorithm. Table IV lists the computation result of PEDA_I, PEDA_A, PEDA_N, PEDA_S, and PEDA. Fig. 7 shows the mean plot and Tukey's HSD results of $I_{H}$ and $I_{c}^{1}$ for all compared algorithms.

As seen in Table IV, the PEDA achieves larger $I_{H}$ and smaller $I_{c}^{1}$ values than PEDA_I, PEDA_A, PEDA_N, and PEDA_S. From Fig. 7, the mean values of $I_{H}$ and $I_{c}^{1}$ are close to 1.44 and 1 , respectively, and there is no overlapping interval between PEDA and PEDA_I, PEDA_A, PEDA_N, and PEDA_S. It shows that the contribution of each component to the PEDA. The PEDA_A obtains worse results among considered variants of PEDA, it implies that the local search for achieve set plays a key contribution. The results of PEDA_S are worse than PEDA, it demonstrates that the high effectiveness and efficiency of our proposed sample method. Based on the above-mentioned results, we can conclude that the PEDA can make a good balance between each component.

## F. Computational Result

To demonstrate the effective performance of PEDA for addressing the MDNWFSP-SDST, this section carries out the computational results in detail. The PEDA is compared to other nine algorithms in Section IV-B, i.e., NSGAII, PESAII, SPEAII, MOEA/D, hMGA, INSGAII, PGA_ALL, CMA, and

TABLE V
Statistical Results of Hypervolume and Unary Epsilon for Compared Algorithms

HIA. We run these 10 algorithms based on the 660 instances of SSD50 and SSD125, respectively. For making a fair comparison, each comparative algorithm has the same termination criterion, i.e., the maximum stopping time. Two kinds of maximum stopping time are considered, which are $T_{\max }=$ $n \times m \times f \times \rho \mathrm{~ms}, \rho=25,50$. Table V summarizes the statistical results for $I_{H}$ and $I_{v}^{1}$ of each comparative algorithm grouped by different factories. As seen in Table V, in the average values of the measure indicators, i.e., hypervolume and unary epsilon, the PEDA turns out to be the best performance, the second in ranking is CMA and INSGAII whose results are close to each other, and the worst is PESAII. Fig. 8 shows the mean plot with $95 \%$ confidence interval of results of $I_{H}$ and $I_{v}^{1}$ for all compared algorithms. Since the results of PESAII are much worse than other algorithms, in order to show the comparison results clearly we do not display its results in statistical figures. As seen in Fig. 8, the union $I_{H}$ value of PEDA is the nearest to 1.44 as well as its $I_{v}^{1}$ is the nearest
to 1 . Moreover, there is no overlapping interval between PEDA and other algorithms, it demonstrates that PEDA is better than other compared algorithms significantly from statistical perspective. In addition, the algorithms with Pareto-based local search methods, i.e., PEDA, CMA, INSGAII, HIA, and PGA_ALS are obviously superior to that without any local search, which verifies the effectiveness of Pareto-based local search. Fig. 9 shows the Pareto fronts obtained by using nine comparative algorithms for the 110th instance from SSD50. It can be seen from these figures that the Pareto fronts yielded by PEDA and CMA are much closer to the bottom-left corner of coordinate axis than other algorithms, it demonstrates their strong exploration and exploitation ability. However, although the CMA obtains some same or better solutions compared to PEDA, the distribution of solutions of CMA is poor because its solutions only exist around the original point, and it has lesser solution that lies around the coordinate axes. Therefore, the Pareto front of CMA is worse than that of PEDA.

To evaluate whether the differences of computational results are significant from the statistical perspective, the ANOVA method is used to analyze the interaction between compared algorithms and the scale of jobs, the numbers of factories, the maximum stopping running time, and the testing instances. Figs. 10-13 display mean interaction plots of hypervolume and unary epsilon between algorithms and the above-mentioned factors. From these figures, it can be concluded as follows.

1) All algorithms obtain better solutions for SSD50 than SSD125, it demonstrates the influence of the setup time, i.e., larger setup time may increase the difficulty of MDNWFSP-SDST.
2) PEDA, CMA, and HIA obtain better solutions with additional running time, while $I_{H}$ and $I_{c}^{1}$ of other algorithms are not changed significantly.
3) The $I_{H}$ values increase and the $I_{c}^{1}$ values of PEDA decrease with the higher number of jobs, whereas other algorithms obtain the opposite results. Moreover, the results of PEDA are better than other algorithms in most of the scales of jobs.
4) The $I_{H}$ values increase and the $I_{c}^{1}$ values of PEDA, CMA, and INSGAII reduce with higher number of factories, whereas other algorithms obtain the better results in the small-scale factories, i.e., $f=2$.

It demonstrates the strong searching ability of PEDA, CMA, and INSGAII for large-scale factories. Furthermore, for all factories, the $I_{H}$ values of PEDA locate above-mentioned other algorithms and the $I_{c}^{1}$ values lie under other algorithms, it demonstrates that the results of PEDA are better than other algorithms. According to above-mentioned experimental results and analysis, it can draw a conclusion that the PEDA can solve the MDNWFSP-SDST effectively and efficiently.

## V. CONCLUSION

This paper studies a multiobjective distributed MDNWFSP-SDST with two performance criteria, i.e., makespan and TWT. There exist several same factories in the MDNWFSP-SDST and each factory includes a flow-shop scheduling problem with no-wait constraint. The setup process is considered between the completion of one job and the start of next job on each machine. The task of MDNWFSP-SDST is to reasonably assign jobs to factories and find the processing sequence of jobs in each factory to optimize multiple scheduling objectives. For the MDNWFSP-SDST, this paper develops a PEDA. The PWQ heuristic is extended to the distributed environment to generate the initial individuals. Three probabilistic models, i.e., the probability of the jobs in empty factory, the two jobs in same factory, and the adjacent jobs are established. A sampling method with referenced template is presented to generate offspring individuals. To optimize the local exploitation ability, the multiobjective local search is performed on the solutions in the offspring population and the archive set.

Comprehensive statistical analysis has been used to investigate the performance of proposed method. From the results, PEDA performs better than other compared algorithms.

It demonstrates the high effectiveness and efficiency of PEDA. Based on the applicability of studied problem and the proposed methods, our work displays a promising prospect in addressing more complex distributed scheduling problems.

For future study, it would be interesting to consider distributed distinct factories environment that is much closer to practical production. The development of effective multiobjective optimization algorithms is another future research direction. Furthermore, the problem properties of MDNWFSP-SDST should be studied further.
